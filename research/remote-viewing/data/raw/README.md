# Raw Source Boundary

This directory does **not** contain copied CIA discs, scholarly articles, Monroe audio, practitioner manuals, historical translations, or user conversation transcripts.

[`acquisition_manifest.json`](acquisition_manifest.json) records what should be acquired, from where, under whose custody, and what must be verified before a payload can enter a governed data store.

## Why link first

The public STAR GATE corpus appears in multiple forms:

- official CIA document pages and PDFs;
- the original multi-disc/TIFF release and later PDF conversions;
- Internet Archive mirrors;
- practitioner-curated indexes;
- Hugging Face raw, OCR, entity, topic, and embedding datasets;
- commercial or community semantic-search layers.

Those surfaces disagree on document and page counts, split and merge files differently, use OCR of varying quality, and attach licences that may cover only a compilation or derived metadata. Copying them into Git without reconciliation would create false certainty and provenance drift.

## Promotion contract

A raw item may be mirrored only after it has:

1. a stable source-vector identifier;
2. an official or explicitly labelled secondary locator;
3. a normalized document or archive identifier;
4. a cryptographic hash and byte count;
5. a verified page count and page order;
6. a custody and release-state note;
7. a rights decision for the exact payload;
8. a publication-safety review;
9. a duplicate/revision relationship to other copies;
10. a reproducible retrieval receipt.

Until then, `payload_policy` remains `link_only`, `external_mirror_only`, or `metadata_first`.
