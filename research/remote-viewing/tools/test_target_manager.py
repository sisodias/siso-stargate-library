#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
TOOL = HERE / "target_manager.py"
POOL = HERE.parent / "example-target-pool.json"


class TargetManagerCliTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_context = tempfile.TemporaryDirectory()
        self.temp = Path(self.temp_context.name)
        self.task = self.temp / "task.json"
        self.private = self.temp / "private.json"
        self.transcript = self.temp / "session.md"
        self.lock = self.temp / "lock.json"
        self.reveal = self.temp / "reveal.json"

    def tearDown(self) -> None:
        self.temp_context.cleanup()

    def run_tool(self, *args: str, expected: int = 0) -> subprocess.CompletedProcess[str]:
        result = subprocess.run(
            [sys.executable, str(TOOL), *args],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(
            expected,
            result.returncode,
            msg=f"stdout:\n{result.stdout}\nstderr:\n{result.stderr}",
        )
        return result

    def assign(self) -> None:
        self.run_tool(
            "assign",
            "--pool",
            str(POOL),
            "--session-id",
            "RV-TEST-001",
            "--cue",
            "1234-5678",
            "--public-task",
            str(self.task),
            "--private-assignment",
            str(self.private),
        )

    def lock_transcript(self) -> None:
        self.transcript.write_text("# Session\nraw: cool, curved, movement\nAOL: bridge\n", encoding="utf-8")
        self.run_tool(
            "lock",
            "--session-id",
            "RV-TEST-001",
            "--transcript",
            str(self.transcript),
            "--out",
            str(self.lock),
        )

    def test_validate_example_pool(self) -> None:
        result = self.run_tool("validate", "--pool", str(POOL))
        self.assertIn("12 unique targets", result.stdout)

    def test_public_task_contains_no_target_or_nonce(self) -> None:
        self.assign()
        public_text = self.task.read_text(encoding="utf-8")
        public = json.loads(public_text)
        private = json.loads(self.private.read_text(encoding="utf-8"))
        pool = json.loads(POOL.read_text(encoding="utf-8"))

        self.assertEqual("remote_viewing_public_task", public["record_type"])
        self.assertNotIn("target", public)
        self.assertNotIn("nonce", public)
        self.assertEqual(public["commitment"], private["commitment"])
        self.assertEqual("1234-5678", public["cue"])

        for target in pool["targets"]:
            self.assertNotIn(target["id"], public_text)
            self.assertNotIn(target["title"], public_text)
            self.assertNotIn(target["feedback_locator"], public_text)
        self.assertNotIn(private["nonce"], public_text)

    def test_full_assign_lock_reveal_verification(self) -> None:
        self.assign()
        self.lock_transcript()
        self.run_tool(
            "verify-lock",
            "--lock",
            str(self.lock),
            "--transcript",
            str(self.transcript),
        )
        self.run_tool(
            "reveal",
            "--private-assignment",
            str(self.private),
            "--transcript-lock",
            str(self.lock),
            "--out",
            str(self.reveal),
        )
        verified = self.run_tool("verify-reveal", "--reveal", str(self.reveal))
        reveal = json.loads(self.reveal.read_text(encoding="utf-8"))
        private = json.loads(self.private.read_text(encoding="utf-8"))
        self.assertEqual(private["target"], reveal["target"])
        self.assertEqual(private["nonce"], reveal["nonce"])
        self.assertIn("PASS", verified.stdout)

    def test_tampered_private_assignment_is_rejected(self) -> None:
        self.assign()
        self.lock_transcript()
        private = json.loads(self.private.read_text(encoding="utf-8"))
        private["target"]["title"] = "tampered title"
        self.private.write_text(json.dumps(private), encoding="utf-8")
        result = self.run_tool(
            "reveal",
            "--private-assignment",
            str(self.private),
            "--transcript-lock",
            str(self.lock),
            "--out",
            str(self.reveal),
            expected=2,
        )
        self.assertIn("commitment", result.stderr.lower())
        self.assertFalse(self.reveal.exists())

    def test_modified_transcript_fails_lock_verification(self) -> None:
        self.assign()
        self.lock_transcript()
        self.transcript.write_text(
            self.transcript.read_text(encoding="utf-8") + "post-feedback edit\n",
            encoding="utf-8",
        )
        result = self.run_tool(
            "verify-lock",
            "--lock",
            str(self.lock),
            "--transcript",
            str(self.transcript),
            expected=2,
        )
        self.assertIn("hash mismatch", result.stderr.lower())

    def test_outputs_are_never_silently_overwritten(self) -> None:
        self.assign()
        original = self.task.read_bytes()
        result = self.run_tool(
            "assign",
            "--pool",
            str(POOL),
            "--session-id",
            "RV-TEST-002",
            "--public-task",
            str(self.task),
            "--private-assignment",
            str(self.temp / "private-2.json"),
            expected=2,
        )
        self.assertIn("overwrite", result.stderr.lower())
        self.assertEqual(original, self.task.read_bytes())

    def test_duplicate_target_ids_are_rejected(self) -> None:
        pool = json.loads(POOL.read_text(encoding="utf-8"))
        pool["targets"][1]["id"] = pool["targets"][0]["id"]
        bad_pool = self.temp / "bad-pool.json"
        bad_pool.write_text(json.dumps(pool), encoding="utf-8")
        result = self.run_tool("validate", "--pool", str(bad_pool), expected=2)
        self.assertIn("duplicate target id", result.stderr.lower())


if __name__ == "__main__":
    unittest.main(verbosity=2)
