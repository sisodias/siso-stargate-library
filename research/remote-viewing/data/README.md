# Psychoenergetics Terrain Data

> **Status:** authored extension to the Remote Viewing Research & Practice module.  
> **Observed:** 2026-08-07.  
> **Scope:** ancient and religious analogues, modern scientific disputes, U.S. and foreign intelligence records, archives, datasets, and research tooling.

The research request named a standalone `data/` skeleton. The Great Library already gives remote viewing one canonical home under `research/remote-viewing/`, so the requested structure is implemented here:

| Requested path | Canonical path |
|---|---|
| `data/raw/` | `research/remote-viewing/data/raw/` |
| `data/index/source_vectors.json` | `research/remote-viewing/data/index/source_vectors.json` |
| `data/releases/master_terrain_scope.md` | `research/remote-viewing/data/releases/master_terrain_scope.md` |

This avoids creating a second registry or pretending that a separate `siso-stargate-library` repository already exists.

## Contents

- [`index/source_vectors.json`](index/source_vectors.json) — programme lineage, 77 source vectors, claim adjudications, repository links, search terms, and explicit evidence gaps.
- [`raw/acquisition_manifest.json`](raw/acquisition_manifest.json) — link-first acquisition plan for official scans, secondary mirrors, OCR corpora, and research datasets.
- [`raw/README.md`](raw/README.md) — why external payloads are not silently copied into Git.
- [`releases/master_terrain_scope.md`](releases/master_terrain_scope.md) — the master intelligence-style terrain assessment.
- [`verify_terrain.py`](verify_terrain.py) — standard-library validation of JSON structure, identifiers, references, paths, and publication boundaries.

## Evidence rule

Every major subject is separated into three layers:

1. **record** — what a source, document, experiment, ritual, or archive demonstrably contains;
2. **source interpretation** — what the source author or institution says the record means;
3. **terrain assessment** — what can be concluded after checking competing explanations and source authority.

A government programme can be historically real while its claimed method remains scientifically unproved. A statistical departure can be interesting without identifying a paranormal cause. A method manual can document practice without validating a mechanism. A historical analogy can be structurally useful without demonstrating one continuous “signal line.”

## Raw-payload policy

The Great Library is a discovery and publication surface, not an uncontrolled PDF warehouse. Official and third-party payloads remain upstream until a governed data plane records:

- exact document identifier and custodial source;
- SHA-256, byte size, and page count;
- scan and OCR provenance;
- redaction/release state;
- rights and redistribution status;
- relationship to duplicates, revisions, appendices, and split/merged files.

The manifest therefore records acquisition vectors rather than committing thousands of scans or proprietary audio files.
