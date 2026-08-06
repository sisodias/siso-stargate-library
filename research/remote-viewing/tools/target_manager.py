#!/usr/bin/env python3
"""Create auditable blind remote-viewing practice tasks.

This is an integrity and role-separation aid, not an encryption system. The
private assignment and target pool must be stored somewhere the viewer cannot
access during the session.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import secrets
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, NoReturn

TOOL_VERSION = "0.1.0"


class TargetManagerError(Exception):
    """A user-facing validation or workflow error."""


def fail(message: str, *, exit_code: int = 2) -> NoReturn:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(exit_code)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError as exc:
        raise TargetManagerError(f"file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise TargetManagerError(
            f"invalid JSON in {path}: line {exc.lineno}, column {exc.colno}: {exc.msg}"
        ) from exc
    except OSError as exc:
        raise TargetManagerError(f"could not read {path}: {exc}") from exc


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def assignment_commitment(nonce: str, target: dict[str, Any]) -> str:
    material = f"{nonce}\n{canonical_json(target)}".encode("utf-8")
    return sha256_bytes(material)


def ensure_https(value: Any, field: str) -> None:
    if not isinstance(value, str) or not value.startswith("https://"):
        raise TargetManagerError(f"{field} must be an https:// URL")


def validate_pool(pool: Any) -> dict[str, Any]:
    if not isinstance(pool, dict):
        raise TargetManagerError("target pool must be a JSON object")
    if pool.get("record_type") != "remote_viewing_target_pool":
        raise TargetManagerError("record_type must be remote_viewing_target_pool")
    if not isinstance(pool.get("schema_version"), str):
        raise TargetManagerError("schema_version is required")
    if not isinstance(pool.get("pool_id"), str) or not pool["pool_id"].strip():
        raise TargetManagerError("pool_id is required")
    if not isinstance(pool.get("warning"), str) or len(pool["warning"].strip()) < 20:
        raise TargetManagerError("pool warning must clearly state its limitations")
    targets = pool.get("targets")
    if not isinstance(targets, list) or len(targets) < 2:
        raise TargetManagerError("target pool must contain at least two targets")

    seen_ids: set[str] = set()
    for index, target in enumerate(targets):
        prefix = f"targets[{index}]"
        if not isinstance(target, dict):
            raise TargetManagerError(f"{prefix} must be an object")
        required_strings = (
            "id",
            "title",
            "target_class",
            "feedback_locator",
            "feedback_definition",
            "rights_note",
        )
        for field in required_strings:
            value = target.get(field)
            if not isinstance(value, str) or not value.strip():
                raise TargetManagerError(f"{prefix}.{field} must be a non-empty string")
        ensure_https(target["feedback_locator"], f"{prefix}.feedback_locator")
        target_id = target["id"]
        if target_id in seen_ids:
            raise TargetManagerError(f"duplicate target id: {target_id}")
        seen_ids.add(target_id)
        features = target.get("features")
        if not isinstance(features, list) or not features or not all(
            isinstance(item, str) and item.strip() for item in features
        ):
            raise TargetManagerError(f"{prefix}.features must be a non-empty string array")
    return pool


def validate_session_id(session_id: str) -> str:
    value = session_id.strip()
    if not value:
        raise TargetManagerError("session id must not be empty")
    allowed = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_.")
    if any(char not in allowed for char in value):
        raise TargetManagerError(
            "session id may contain only letters, numbers, hyphen, underscore, and period"
        )
    if len(value) > 128:
        raise TargetManagerError("session id is too long")
    return value


def generate_cue() -> str:
    return f"{secrets.randbelow(10_000):04d}-{secrets.randbelow(10_000):04d}"


def check_output_paths(paths: list[Path]) -> None:
    normalized: list[Path] = []
    for path in paths:
        resolved = path.expanduser().resolve(strict=False)
        if resolved in normalized:
            raise TargetManagerError("output paths must be distinct")
        normalized.append(resolved)
        if path.exists():
            raise TargetManagerError(f"refusing to overwrite existing file: {path}")
        parent = path.parent
        if parent.exists() and not parent.is_dir():
            raise TargetManagerError(f"output parent is not a directory: {parent}")


def write_json_exclusive(path: Path, value: Any, *, private: bool = False) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    flags = os.O_WRONLY | os.O_CREAT | os.O_EXCL
    mode = 0o600 if private else 0o644
    fd: int | None = None
    try:
        fd = os.open(path, flags, mode)
        payload = (json.dumps(value, indent=2, ensure_ascii=False) + "\n").encode("utf-8")
        with os.fdopen(fd, "wb") as handle:
            fd = None
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        if private:
            try:
                os.chmod(path, 0o600)
            except OSError:
                # Permission hardening is best effort on non-POSIX filesystems.
                pass
    except FileExistsError as exc:
        raise TargetManagerError(f"refusing to overwrite existing file: {path}") from exc
    except OSError as exc:
        raise TargetManagerError(f"could not write {path}: {exc}") from exc
    finally:
        if fd is not None:
            os.close(fd)


def assign_command(args: argparse.Namespace) -> None:
    pool_path = Path(args.pool)
    public_path = Path(args.public_task)
    private_path = Path(args.private_assignment)
    check_output_paths([public_path, private_path])

    pool = validate_pool(load_json(pool_path))
    session_id = validate_session_id(args.session_id)
    cue = args.cue.strip() if args.cue else generate_cue()
    if not cue or len(cue) > 128:
        raise TargetManagerError("cue must contain 1 to 128 characters")

    target = secrets.choice(pool["targets"])
    nonce = secrets.token_hex(32)
    commitment = assignment_commitment(nonce, target)
    issued_at = utc_now()

    private_assignment = {
        "schema_version": "0.1.0",
        "record_type": "remote_viewing_private_assignment",
        "tool_version": TOOL_VERSION,
        "session_id": session_id,
        "pool_id": pool["pool_id"],
        "cue": cue,
        "issued_at": issued_at,
        "commitment_algorithm": "sha256(nonce + newline + canonical_target_json)",
        "commitment": commitment,
        "nonce": nonce,
        "target": target,
        "security_warning": (
            "This file reveals the target and is not encrypted. Keep it inaccessible to the "
            "viewer, blind monitor, and blind judge until the required locks are complete."
        ),
    }

    public_task = {
        "schema_version": "0.1.0",
        "record_type": "remote_viewing_public_task",
        "tool_version": TOOL_VERSION,
        "session_id": session_id,
        "pool_id": pool["pool_id"],
        "cue": cue,
        "issued_at": issued_at,
        "task": pool.get(
            "default_task",
            "Describe the target associated with the opaque cue. Record raw data before interpretation.",
        ),
        "commitment_algorithm": "sha256(nonce + newline + canonical_target_json)",
        "commitment": commitment,
        "viewer_rules": [
            "Do not access the target pool or private assignment.",
            "Complete and lock the full transcript before feedback.",
            "Record object-level interpretations as AOL rather than deleting them.",
        ],
    }

    # Write the sensitive file first, but roll it back if the public write fails.
    write_json_exclusive(private_path, private_assignment, private=True)
    try:
        write_json_exclusive(public_path, public_task, private=False)
    except Exception:
        try:
            private_path.unlink()
        except OSError:
            pass
        raise

    print(f"assigned session: {session_id}")
    print(f"public task: {public_path}")
    print(f"private assignment: {private_path}")
    print(f"commitment: {commitment}")
    print("WARNING: the private assignment is not encrypted; enforce role separation.")


def lock_command(args: argparse.Namespace) -> None:
    session_id = validate_session_id(args.session_id)
    transcript_path = Path(args.transcript)
    output_path = Path(args.out)
    check_output_paths([output_path])
    try:
        payload = transcript_path.read_bytes()
    except FileNotFoundError as exc:
        raise TargetManagerError(f"transcript not found: {transcript_path}") from exc
    except OSError as exc:
        raise TargetManagerError(f"could not read transcript {transcript_path}: {exc}") from exc
    if not payload:
        raise TargetManagerError("refusing to lock an empty transcript")

    lock = {
        "schema_version": "0.1.0",
        "record_type": "remote_viewing_transcript_lock",
        "tool_version": TOOL_VERSION,
        "session_id": session_id,
        "locked_at": utc_now(),
        "transcript_name": transcript_path.name,
        "byte_count": len(payload),
        "hash_algorithm": "sha256",
        "transcript_sha256": sha256_bytes(payload),
        "integrity_note": "Any change to the transcript bytes after this lock changes the digest.",
    }
    write_json_exclusive(output_path, lock)
    print(f"locked transcript for session: {session_id}")
    print(f"lock file: {output_path}")
    print(f"sha256: {lock['transcript_sha256']}")


def verify_lock_record(lock: Any, transcript_path: Path | None = None) -> dict[str, Any]:
    if not isinstance(lock, dict) or lock.get("record_type") != "remote_viewing_transcript_lock":
        raise TargetManagerError("not a remote_viewing_transcript_lock record")
    for field in ("session_id", "transcript_sha256", "hash_algorithm", "byte_count"):
        if field not in lock:
            raise TargetManagerError(f"transcript lock missing field: {field}")
    if lock["hash_algorithm"] != "sha256":
        raise TargetManagerError("unsupported transcript hash algorithm")
    digest = lock["transcript_sha256"]
    if not isinstance(digest, str) or len(digest) != 64:
        raise TargetManagerError("invalid transcript SHA-256 digest")

    if transcript_path is not None:
        try:
            payload = transcript_path.read_bytes()
        except FileNotFoundError as exc:
            raise TargetManagerError(f"transcript not found: {transcript_path}") from exc
        except OSError as exc:
            raise TargetManagerError(f"could not read transcript {transcript_path}: {exc}") from exc
        actual = sha256_bytes(payload)
        if actual != digest:
            raise TargetManagerError(
                f"transcript hash mismatch: expected {digest}, calculated {actual}"
            )
        if len(payload) != lock["byte_count"]:
            raise TargetManagerError("transcript byte count does not match lock")
    return lock


def verify_lock_command(args: argparse.Namespace) -> None:
    lock = verify_lock_record(load_json(Path(args.lock)), Path(args.transcript))
    print(f"PASS: transcript lock verifies for session {lock['session_id']}")


def reveal_command(args: argparse.Namespace) -> None:
    assignment_path = Path(args.private_assignment)
    lock_path = Path(args.transcript_lock)
    output_path = Path(args.out)
    check_output_paths([output_path])

    assignment = load_json(assignment_path)
    if not isinstance(assignment, dict) or assignment.get("record_type") != "remote_viewing_private_assignment":
        raise TargetManagerError("private assignment has the wrong record_type")
    required = ("session_id", "pool_id", "cue", "commitment", "nonce", "target", "issued_at")
    for field in required:
        if field not in assignment:
            raise TargetManagerError(f"private assignment missing field: {field}")
    if not isinstance(assignment["target"], dict) or not isinstance(assignment["nonce"], str):
        raise TargetManagerError("private assignment target or nonce has the wrong type")

    recomputed = assignment_commitment(assignment["nonce"], assignment["target"])
    if not secrets.compare_digest(recomputed, str(assignment["commitment"])):
        raise TargetManagerError("private assignment commitment does not verify; file may be altered")

    lock = verify_lock_record(load_json(lock_path))
    if lock["session_id"] != assignment["session_id"]:
        raise TargetManagerError(
            "session mismatch between private assignment and transcript lock"
        )

    reveal = {
        "schema_version": "0.1.0",
        "record_type": "remote_viewing_reveal",
        "tool_version": TOOL_VERSION,
        "session_id": assignment["session_id"],
        "pool_id": assignment["pool_id"],
        "cue": assignment["cue"],
        "issued_at": assignment["issued_at"],
        "revealed_at": utc_now(),
        "commitment_algorithm": assignment.get(
            "commitment_algorithm", "sha256(nonce + newline + canonical_target_json)"
        ),
        "commitment": assignment["commitment"],
        "nonce": assignment["nonce"],
        "target": assignment["target"],
        "transcript_lock": {
            "locked_at": lock.get("locked_at"),
            "transcript_name": lock.get("transcript_name"),
            "byte_count": lock["byte_count"],
            "hash_algorithm": lock["hash_algorithm"],
            "transcript_sha256": lock["transcript_sha256"],
        },
        "verification_note": (
            "The target commitment verified and the session ID matched the transcript lock. "
            "This verifies workflow integrity, not target correspondence or remote-viewing accuracy."
        ),
    }
    write_json_exclusive(output_path, reveal)
    print(f"revealed session: {assignment['session_id']}")
    print(f"target id: {assignment['target'].get('id', '<missing>')}")
    print(f"reveal file: {output_path}")


def verify_reveal_record(reveal: Any) -> dict[str, Any]:
    if not isinstance(reveal, dict) or reveal.get("record_type") != "remote_viewing_reveal":
        raise TargetManagerError("not a remote_viewing_reveal record")
    for field in ("session_id", "commitment", "nonce", "target", "transcript_lock"):
        if field not in reveal:
            raise TargetManagerError(f"reveal missing field: {field}")
    if not isinstance(reveal["target"], dict) or not isinstance(reveal["nonce"], str):
        raise TargetManagerError("reveal target or nonce has the wrong type")
    expected = assignment_commitment(reveal["nonce"], reveal["target"])
    if not secrets.compare_digest(expected, str(reveal["commitment"])):
        raise TargetManagerError("reveal commitment does not verify")
    lock = reveal["transcript_lock"]
    if not isinstance(lock, dict):
        raise TargetManagerError("reveal transcript_lock must be an object")
    digest = lock.get("transcript_sha256")
    if not isinstance(digest, str) or len(digest) != 64:
        raise TargetManagerError("reveal contains an invalid transcript digest")
    return reveal


def verify_reveal_command(args: argparse.Namespace) -> None:
    reveal = verify_reveal_record(load_json(Path(args.reveal)))
    print(
        f"PASS: reveal verifies for session {reveal['session_id']} "
        f"and target {reveal['target'].get('id', '<missing>')}"
    )


def validate_command(args: argparse.Namespace) -> None:
    pool = validate_pool(load_json(Path(args.pool)))
    print(f"PASS: {pool['pool_id']} contains {len(pool['targets'])} unique targets")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Manage blind practice-target assignment, transcript locking, and reveal receipts. "
            "Private assignments are not encrypted."
        )
    )
    parser.add_argument("--version", action="version", version=TOOL_VERSION)
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser("validate", help="validate a target pool")
    validate_parser.add_argument("--pool", required=True)
    validate_parser.set_defaults(func=validate_command)

    assign_parser = subparsers.add_parser("assign", help="assign one private target and create a public task")
    assign_parser.add_argument("--pool", required=True)
    assign_parser.add_argument("--session-id", required=True)
    assign_parser.add_argument("--public-task", required=True)
    assign_parser.add_argument("--private-assignment", required=True)
    assign_parser.add_argument("--cue", help="optional opaque cue; a random 4-digit pair is generated by default")
    assign_parser.set_defaults(func=assign_command)

    lock_parser = subparsers.add_parser("lock", help="hash and lock a completed transcript before feedback")
    lock_parser.add_argument("--session-id", required=True)
    lock_parser.add_argument("--transcript", required=True)
    lock_parser.add_argument("--out", required=True)
    lock_parser.set_defaults(func=lock_command)

    verify_lock_parser = subparsers.add_parser("verify-lock", help="verify a transcript against a lock record")
    verify_lock_parser.add_argument("--lock", required=True)
    verify_lock_parser.add_argument("--transcript", required=True)
    verify_lock_parser.set_defaults(func=verify_lock_command)

    reveal_parser = subparsers.add_parser("reveal", help="verify assignment integrity and create a reveal receipt")
    reveal_parser.add_argument("--private-assignment", required=True)
    reveal_parser.add_argument("--transcript-lock", required=True)
    reveal_parser.add_argument("--out", required=True)
    reveal_parser.set_defaults(func=reveal_command)

    verify_reveal_parser = subparsers.add_parser("verify-reveal", help="verify a reveal commitment")
    verify_reveal_parser.add_argument("--reveal", required=True)
    verify_reveal_parser.set_defaults(func=verify_reveal_command)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        args.func(args)
    except TargetManagerError as exc:
        fail(str(exc))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
