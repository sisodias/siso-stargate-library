# Handoff — Remote Viewing Research & Practice

## Scope delivered

This branch adds one isolated authored Research module under:

```text
research/remote-viewing/**
```

It also closes the append-only initiative Event started on canonical `main`:

```text
gls:thread:remote-viewing-research-module
```

The module includes:

- a placement and operating constitution;
- a declassified-programme and evidence review;
- a mechanism-hypothesis map separating practitioner language from established claims;
- a detailed six-stage CRV practice protocol;
- a preregistration, blinding, judging, statistics, and replication guide;
- a printable session worksheet;
- a balanced human source map;
- machine-readable source and claim ledgers;
- an explicitly non-research demonstration target pool;
- a standard-library target manager for assignment commitments, transcript locks, and reveals;
- offline structural, safety, provenance, and tool tests.

## Placement decision

Remote viewing belongs in **Research** because it combines:

- historical government records;
- laboratory methodology;
- practitioner training systems;
- operational-use claims;
- competing causal explanations;
- unresolved replication and evidence questions.

It should connect later to History and declassified-government-document collections, but neither of those projections should own its stable identity.

This first change remains authored research rather than creating a formal Work, Release, Source Inventory, Snapshot, or generated site page. At publication time, active draft lanes already owned:

- the next whole-Library Snapshot and related Work/Release registry surfaces;
- `CURRENT_STATE.md` and generated `site/**`;
- root and documentation indexes used by the UNSOLVEABLE Mathematics programme.

The isolated path avoids overwriting those lanes. After they close, a follow-up can promote this module through the normal Great Library contracts.

## Truth boundary

The module intentionally preserves three simultaneous positions:

1. **Practice premise:** execute the method as though weak target-related information may be available.
2. **Evidence discipline:** blind, precommit, lock, judge against decoys, and preserve every result.
3. **Theory uncertainty:** do not call Matrix, signal line, telepathy, clairvoyance, precognition, or any ordinary artifact established without a design that distinguishes it.

The public record supports all of the following at once:

- government programmes and training records existed;
- early and later researchers reported positive laboratory results;
- critics reported failed duplication and methodological artifacts;
- declassified files include apparently correlated, null, low-correlation, ambiguous, and unevaluated sessions;
- the 1995 AIR review reported above-chance laboratory results but rejected demonstrated operational utility;
- its principal expert reviewers disagreed about paranormal attribution;
- current positive synthesis and expert-practice papers exist, but do not create a settled scientific consensus.

No claim in this module treats programme duration, renaming, testimony, institutional interest, or a striking session as a substitute for measured performance.

## Tool boundary

`tools/target_manager.py` is an integrity aid. It:

- selects one target with Python's `secrets` module;
- writes a target-free public task;
- writes a private unencrypted assignment;
- commits the exact target with a random nonce and SHA-256;
- locks transcript bytes with SHA-256 before feedback;
- verifies the assignment commitment and session identity at reveal;
- refuses silent overwrites;
- verifies later that transcript and reveal receipts have not changed.

It does **not**:

- encrypt the private assignment;
- make a self-run task truly double-blind;
- construct balanced decoy sets;
- score a session;
- prove randomization was free from every host compromise;
- establish target correspondence or paranormal ability.

A target manager must keep the private assignment and pool inaccessible to the viewer, monitor, and blind judge.

## Validation

Run from the repository root:

```bash
python3 research/remote-viewing/verify_module.py
```

The module verifier checks:

- required files and UTF-8 text;
- JSON parsing and record shapes;
- unique and resolvable local source IDs;
- positive, negative, unknown, and not-established claim states;
- HTTPS source and target locators;
- rights and limitations notes;
- relative Markdown links;
- absence of copied PDF/database/archive payloads;
- common credential and machine-path patterns;
- Python compilation;
- target-manager integration and tamper tests.

The tool test suite covers:

- example-pool validation;
- no target or nonce leakage into the public task;
- full assignment → lock → reveal verification;
- rejection of a tampered private assignment;
- rejection of a transcript changed after locking;
- overwrite protection;
- duplicate-target rejection.

The complete repository `npm run verify` must still run in the authoritative pull-request environment. This work was produced through the GitHub connector without a full local repository checkout, so the module's offline verifier is strong but not a substitute for the repository schema, generated-site, immutable-history, link, and publication gates.

## Source and rights limitations

- `source-index.json` is selective, not a complete STARGATE corpus inventory.
- Government-document dates recorded only at year precision remain explicitly marked for page-level verification.
- The CRV manual reader and 1986 scan are external practitioner-archive surfaces; no official DIA document number or CIA Reading Room custody has been established, so preservation and revision lineage remain open gates.
- No external paper, manual, scan, PDF, database, or image payload is copied into the module.
- A public locator is not treated as a redistribution license.
- The example pool links to public feedback pages but is not a rights-cleared or statistically balanced research pool.
- The module does not independently reconstruct the underlying SRI/SAIC trial-level data or re-run the 2023 meta-analysis.

## Promotion sequence

After the active registry and documentation lanes close:

1. review every source locator, date, provenance claim, and rights note;
2. create a preservation-aware Source Inventory for the external government and scholarly corpus without copying the payloads;
3. run at least ten clean pilot sessions to validate the task/lock/reveal/judge workflow;
4. obtain independent review from one methodologically sympathetic and one critical reader;
5. register an independently addressable Remote Viewing Research & Practice Work;
6. publish an immutable Release pinned to the exact source commit;
7. select it through the next successor whole-Library Snapshot;
8. generate, rather than hand-edit, its public Library page;
9. update the relevant Research and declassified-document browse projections through typed relationships.

## Next high-value research

- Build a complete, deduplicated CIA session graph linking tasking, transcript, feedback, evaluation, and correspondence.
- Sample the archive under a declared rule and estimate positive, negative, ambiguous, and unevaluated proportions.
- Reconstruct trial-level SRI and SAIC datasets where rights and records allow.
- Independently re-extract the 2023 meta-analysis with dependence and risk-of-bias coding.
- Run a preregistered CRV-training versus matched observation-control study.
- Run sender-present, sender-absent, preselected-target, and target-after-lock conditions in one mechanism-separating design.
- Test whether multi-viewer aggregation improves held-out performance under a frozen rule.
- Measure operational specificity and incremental decision value rather than narrative impressiveness.

## Merge boundary

Expected changed paths are limited to:

```text
research/remote-viewing/**
registry/events/2026-08-07-remote-viewing-research-completed.json
```

The start Event already exists on `main` and must not be rewritten. Generated `site/**`, existing Works, Releases, Snapshots, Decisions, `CURRENT_STATE.md`, root indexes, and other active research modules remain untouched.
