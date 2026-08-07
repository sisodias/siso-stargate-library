# SISO Stargate Library

Remote viewing and psychoenergetics research. Split out of the Great Library of
SISO on 2026-08-07 with full history from both contributing branches.

This repository name is the module's own stated destination. Its
`research/remote-viewing/data/README.md` recorded that it was avoiding
"pretending that a separate `siso-stargate-library` repository already exists" —
it now does.

## The three-track truth boundary

The module keeps three tracks separate on purpose:

- **practice** — assume enough to execute;
- **evidence** — assume nothing in the analysis;
- **theory** — force hypotheses to compete.

This lets a practitioner work from a possibility premise while the record stays
honest. Core rule 6 holds that above-chance scoring, paranormal cause, specific
mechanism, trainability, and operational usefulness are **five different
claims**; most writing collapses them.

## What the claims actually say

`claims.json` holds 33 claims, each with an `update_gate` naming the exact
evidence that would change its status: 14 not_established, 11 documented_record,
2 reported_positive, 2 reported_negative, 3 methodological_rule, 1 unknown.

Note RV-C003 (AIR found above-chance lab results, documented_record) sits beside
RV-C004 (AIR established operational value, reported_negative) — the same source,
split honestly.

## Tools

- `tools/target_manager.py` (+ tests) — SHA-256 commitment `SHA256(nonce||target)`,
  transcript lock before feedback, tamper detection. Its HANDOFF states plainly
  what it does *not* do: it does not encrypt, does not make a self-run
  double-blind, does not build balanced decoys, does not score, and "does not
  establish target correspondence or paranormal ability."
- `verify_module.py` — standard-library structural verification of the module.

Verified after the split on 2026-08-07: `test_target_manager.py` 7/7 OK, and
`verify_module.py` PASS at sources=36, claims=33, relative_links_checked=16.

## Provenance

Reunites `agent/remote-viewing-research-module` (25 commits) and
`agent/psychoenergetics-terrain-scan` (21 commits), which forked at `c9e4876`
and where neither contained the other. Merged without conflict, then filtered to
this path set. Registered as a Work in the Great Library with a
`source_repository` locator.
