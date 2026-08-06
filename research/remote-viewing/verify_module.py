#!/usr/bin/env python3
"""Offline structural, provenance, safety, and tool checks for the module."""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

MODULE = Path(__file__).resolve().parent
REQUIRED_FILES = {
    "README.md",
    "history-and-evidence.md",
    "mechanism-hypotheses.md",
    "practice-protocol.md",
    "experimental-method.md",
    "session-template.md",
    "source-map.md",
    "source-index.json",
    "sources/government-and-practice.json",
    "sources/scholarly-and-reviews.json",
    "claims.json",
    "example-target-pool.json",
    "HANDOFF.md",
    "tools/target_manager.py",
    "tools/test_target_manager.py",
}
ALLOWED_CLAIM_STATUSES = {
    "documented_record",
    "reported_positive",
    "reported_negative",
    "contested",
    "not_established",
    "unknown",
    "methodological_rule",
}
SOURCE_ID_RE = re.compile(r"\bSRC-[A-Z0-9-]+\b")
MARKDOWN_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
FORBIDDEN_PAYLOAD_SUFFIXES = {".pdf", ".zip", ".doc", ".docx", ".rtf", ".sqlite", ".db"}
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    "OpenAI-style key": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
}
MACHINE_PATH_PATTERNS = {
    "macOS home path": re.compile(r"/Users/[A-Za-z0-9._-]+/"),
    "Linux home path": re.compile(r"/home/[A-Za-z0-9._-]+/"),
    "Windows user path": re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+\\"),
}


class VerificationError(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise VerificationError(message)


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        raise VerificationError(f"non-UTF-8 text file: {path.relative_to(MODULE)}") from exc


def read_json(name: str) -> Any:
    path = MODULE / name
    try:
        return json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        raise VerificationError(
            f"invalid JSON in {name} at line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc


def check_required_files() -> None:
    actual_files = {
        str(path.relative_to(MODULE))
        for path in MODULE.rglob("*")
        if path.is_file() and "__pycache__" not in path.parts
    }
    missing = sorted(REQUIRED_FILES - actual_files)
    require(not missing, f"missing required files: {', '.join(missing)}")
    for relative in REQUIRED_FILES:
        path = MODULE / relative
        require(path.stat().st_size > 0, f"required file is empty: {relative}")

    forbidden = sorted(
        str(path.relative_to(MODULE))
        for path in MODULE.rglob("*")
        if path.is_file() and path.suffix.lower() in FORBIDDEN_PAYLOAD_SUFFIXES
    )
    require(not forbidden, f"external payload-like files must not be committed: {forbidden}")


def check_source_index() -> tuple[dict[str, Any], set[str]]:
    index = read_json("source-index.json")
    require(isinstance(index, dict), "source-index.json must be an object")
    require(index.get("record_type") == "remote_viewing_source_index", "source index record_type is wrong")
    source_files = index.get("source_files")
    require(
        isinstance(source_files, list) and source_files and all(isinstance(name, str) and name for name in source_files),
        "source index must declare non-empty source_files",
    )
    sources: list[dict[str, Any]] = []
    for source_file in source_files:
        require(source_file.startswith("sources/") and ".." not in Path(source_file).parts, f"unsafe source file path: {source_file}")
        payload = read_json(source_file)
        require(isinstance(payload, dict), f"{source_file} must be an object")
        require(payload.get("record_type") == "remote_viewing_source_records", f"{source_file} record_type is wrong")
        records = payload.get("sources")
        require(isinstance(records, list) and records, f"{source_file} must contain source records")
        sources.extend(records)
    require(len(sources) >= 15, "source files must contain at least 15 sources")

    ids: set[str] = set()
    types: set[str] = set()
    authorities: set[str] = set()
    for position, source in enumerate(sources):
        prefix = f"combined source records[{position}]"
        require(isinstance(source, dict), f"{prefix} must be an object")
        for field in (
            "id",
            "title",
            "authors_or_owner",
            "date",
            "source_type",
            "locator",
            "authority",
            "stance_or_result",
            "limitations",
            "rights_note",
        ):
            require(
                isinstance(source.get(field), str) and source[field].strip(),
                f"{prefix}.{field} must be a non-empty string",
            )
        source_id = source["id"]
        require(SOURCE_ID_RE.fullmatch(source_id) is not None, f"invalid source id: {source_id}")
        require(source_id not in ids, f"duplicate source id: {source_id}")
        ids.add(source_id)
        require(source["locator"].startswith("https://"), f"source locator must use HTTPS: {source_id}")
        roles = source.get("evidence_role")
        require(
            isinstance(roles, list) and roles and all(isinstance(role, str) and role for role in roles),
            f"{prefix}.evidence_role must be a non-empty string array",
        )
        types.add(source["source_type"])
        authorities.add(source["authority"])

    require(any("government" in source_type for source_type in types), "source index lacks government records")
    require(any("critique" in source_type or "replication" in source_type for source_type in types), "source index lacks critical or replication sources")
    require("expert_opinion_study" in authorities, "source index lacks a clearly labeled expert-opinion source")
    require("primary_government_record" in authorities, "source index lacks primary government records")
    index["sources"] = sources
    return index, ids


def check_claims(source_ids: set[str]) -> tuple[dict[str, Any], set[str]]:
    ledger = read_json("claims.json")
    require(isinstance(ledger, dict), "claims.json must be an object")
    require(ledger.get("record_type") == "remote_viewing_claim_ledger", "claim ledger record_type is wrong")
    claims = ledger.get("claims")
    require(isinstance(claims, list) and len(claims) >= 15, "claim ledger must contain at least 15 claims")

    claim_ids: set[str] = set()
    observed_statuses: set[str] = set()
    for position, claim in enumerate(claims):
        prefix = f"claims.json claims[{position}]"
        require(isinstance(claim, dict), f"{prefix} must be an object")
        for field in ("id", "claim", "status", "confidence", "interpretation", "update_gate"):
            require(
                isinstance(claim.get(field), str) and claim[field].strip(),
                f"{prefix}.{field} must be a non-empty string",
            )
        claim_id = claim["id"]
        require(re.fullmatch(r"RV-C\d{3}", claim_id) is not None, f"invalid claim id: {claim_id}")
        require(claim_id not in claim_ids, f"duplicate claim id: {claim_id}")
        claim_ids.add(claim_id)
        status = claim["status"]
        require(status in ALLOWED_CLAIM_STATUSES, f"invalid claim status for {claim_id}: {status}")
        observed_statuses.add(status)
        refs = claim.get("source_ids")
        require(isinstance(refs, list) and refs, f"{claim_id} must cite at least one source")
        unknown = sorted(set(refs) - source_ids)
        require(not unknown, f"{claim_id} cites unknown source ids: {unknown}")

    require("reported_positive" in observed_statuses, "claim ledger lacks positive source-reported claims")
    require("reported_negative" in observed_statuses, "claim ledger lacks negative source-reported claims")
    require("not_established" in observed_statuses, "claim ledger lacks explicit not-established claims")
    require("unknown" in observed_statuses, "claim ledger lacks explicit unknowns")
    return ledger, claim_ids


def check_target_pool() -> tuple[dict[str, Any], set[str]]:
    pool = read_json("example-target-pool.json")
    require(isinstance(pool, dict), "target pool must be an object")
    require(pool.get("record_type") == "remote_viewing_target_pool", "target pool record_type is wrong")
    warning = pool.get("warning")
    require(isinstance(warning, str) and "NOT A FORMAL RESEARCH POOL" in warning, "demo-pool warning is missing")
    targets = pool.get("targets")
    require(isinstance(targets, list) and len(targets) >= 8, "demo target pool must contain at least eight targets")
    ids: set[str] = set()
    classes: set[str] = set()
    for position, target in enumerate(targets):
        prefix = f"example-target-pool.json targets[{position}]"
        require(isinstance(target, dict), f"{prefix} must be an object")
        for field in ("id", "title", "target_class", "feedback_locator", "feedback_definition", "rights_note"):
            require(
                isinstance(target.get(field), str) and target[field].strip(),
                f"{prefix}.{field} must be a non-empty string",
            )
        require(target["id"] not in ids, f"duplicate target id: {target['id']}")
        ids.add(target["id"])
        classes.add(target["target_class"])
        require(target["feedback_locator"].startswith("https://"), f"target locator must use HTTPS: {target['id']}")
        features = target.get("features")
        require(
            isinstance(features, list) and len(features) >= 3 and all(isinstance(item, str) and item for item in features),
            f"{prefix}.features must contain at least three strings",
        )
    require(len(classes) >= 6, "demo pool must contain at least six target classes")
    return pool, ids


def check_markdown_links() -> int:
    checked = 0
    for path in sorted(MODULE.glob("*.md")):
        text = read_text(path)
        for raw_link in MARKDOWN_LINK_RE.findall(text):
            link = raw_link.strip().split()[0].strip("<>")
            if not link or link.startswith(("https://", "http://", "mailto:", "#")):
                continue
            relative = link.split("#", 1)[0]
            if not relative:
                continue
            target = (path.parent / relative).resolve(strict=False)
            require(
                MODULE.resolve() in target.parents or target == MODULE.resolve(),
                f"relative link escapes module in {path.name}: {link}",
            )
            require(target.exists(), f"broken relative link in {path.name}: {link}")
            checked += 1
    return checked


def check_source_references(source_ids: set[str]) -> int:
    unknown_mentions: set[str] = set()
    all_text = ""
    for path in MODULE.rglob("*"):
        if not path.is_file() or "__pycache__" in path.parts:
            continue
        if path.suffix.lower() in {".md", ".json", ".py"}:
            text = read_text(path)
            all_text += "\n" + text
            unknown_mentions.update(set(SOURCE_ID_RE.findall(text)) - source_ids)
    require(not unknown_mentions, f"module mentions unknown source IDs: {sorted(unknown_mentions)}")

    source_map = read_text(MODULE / "source-map.md")
    claims_text = read_text(MODULE / "claims.json")
    uncontextualized = sorted(
        source_id for source_id in source_ids if source_id not in source_map and source_id not in claims_text
    )
    require(not uncontextualized, f"sources lack source-map or claim context: {uncontextualized}")
    return len(SOURCE_ID_RE.findall(all_text))


def check_publication_safety() -> int:
    scanned = 0
    for path in MODULE.rglob("*"):
        if not path.is_file() or "__pycache__" in path.parts:
            continue
        if path.suffix.lower() not in {".md", ".json", ".py"}:
            continue
        text = read_text(path)
        scanned += 1
        for label, pattern in SECRET_PATTERNS.items():
            require(pattern.search(text) is None, f"possible {label} in {path.relative_to(MODULE)}")
        for label, pattern in MACHINE_PATH_PATTERNS.items():
            require(pattern.search(text) is None, f"machine-specific {label} in {path.relative_to(MODULE)}")
    return scanned


def run_python_checks() -> int:
    scripts = [MODULE / "tools" / "target_manager.py", MODULE / "tools" / "test_target_manager.py", MODULE / "verify_module.py"]
    subprocess.run(
        [sys.executable, "-m", "py_compile", *map(str, scripts)],
        check=True,
        cwd=MODULE,
    )
    completed = subprocess.run(
        [sys.executable, str(MODULE / "tools" / "test_target_manager.py")],
        check=True,
        cwd=MODULE,
        text=True,
        capture_output=True,
    )
    match = re.search(r"Ran (\d+) tests?", completed.stderr + completed.stdout)
    return int(match.group(1)) if match else 0


def main() -> int:
    try:
        check_required_files()
        source_index, source_ids = check_source_index()
        claims, claim_ids = check_claims(source_ids)
        pool, target_ids = check_target_pool()
        link_count = check_markdown_links()
        source_reference_count = check_source_references(source_ids)
        scanned_files = check_publication_safety()
        test_count = run_python_checks()
    except (VerificationError, subprocess.CalledProcessError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    print("PASS: remote-viewing module verifies")
    print(f"sources={len(source_index['sources'])}")
    print(f"claims={len(claims['claims'])}")
    print(f"demo_targets={len(pool['targets'])}")
    print(f"relative_links_checked={link_count}")
    print(f"source_id_mentions={source_reference_count}")
    print(f"publication_safe_files_scanned={scanned_files}")
    print(f"target_manager_tests={test_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
