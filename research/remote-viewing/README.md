# Remote Viewing Research & Practice

> **Status:** authored Research module; not yet a registered Great Library Work or Release.  
> **Observed:** 2026-08-07.  
> **Purpose:** learn the historical methods, run clean blinded sessions, preserve every result, and let evidence—not belief or ridicule—do the adjudicating.

## Why this belongs in Research

Remote viewing sits at the intersection of four different things:

1. a declassified government programme family commonly grouped under **STARGATE**;
2. a laboratory paradigm for testing descriptions of hidden or remote targets;
3. practitioner methods, especially **Controlled Remote Viewing (CRV)**;
4. unresolved arguments about statistical anomalies, mechanism, replication, and operational value.

That combination makes it a Research programme, not merely a History shelf, an Intelligence technique, a meditation skill, or a collection of unusual documents. The Great Library should preserve the primary record, make the practice reproducible, and keep claims attached to their evidence.

This first publication is intentionally isolated under `research/remote-viewing/`. It does not create a second registry and does not modify generated `site/` files. Promotion to an independently addressable Work, immutable Release, Source Inventory, and successor whole-Library Snapshot comes only after active registry lanes close and the source/rights boundary is reviewed.

## The operating stance

The requested starting premise is practical: stop spending the whole conversation on “is it possible?” and investigate **how remote viewing is said to work and how one actually does it**.

This module preserves that stance without smuggling an answer into the evidence:

- **Practice track — assume enough to execute.** During a session, behave as though weak target-related information may arrive. Record first impressions quickly, separate description from interpretation, and follow the protocol.
- **Evidence track — assume nothing in the analysis.** Blind the viewer and monitor, precommit the target, lock the transcript before feedback, use decoys and independent judging, and publish misses with hits.
- **Theory track — force hypotheses to compete.** “Matrix,” “signal line,” telepathy, clairvoyance, precognition, cueing, target-set artifacts, judge effects, selective reporting, and ordinary inference make different predictions. Design tests that separate them.

A practitioner can therefore work from a first-principles possibility premise while the Library remains honest about what is established, disputed, or unknown.

## Start here

| Goal | Read or run |
|---|---|
| Understand the programme and the evidence split | [`history-and-evidence.md`](history-and-evidence.md) |
| Understand “signal line,” AOL, and competing mechanisms | [`mechanism-hypotheses.md`](mechanism-hypotheses.md) |
| Conduct a first clean session | [`practice-protocol.md`](practice-protocol.md) |
| Design a study that can survive criticism | [`experimental-method.md`](experimental-method.md) |
| Print a session worksheet | [`session-template.md`](session-template.md) |
| Inspect the primary-source universe | [`source-map.md`](source-map.md) and [`source-index.json`](source-index.json) |
| Inspect claim status without reading prose | [`claims.json`](claims.json) |
| Create a committed blind task and reveal it later | [`tools/target_manager.py`](tools/target_manager.py) |
| Check the whole module | `python3 research/remote-viewing/verify_module.py` |

## What “remote viewing” means here

For this module, a **remote-viewing trial** is an information-gathering task in which:

- the viewer attempts to describe a target unavailable through ordinary access at the time of the session;
- the viewer receives no target-identifying information beyond an opaque cue;
- the session output is fixed before feedback;
- target assignment, judging, and analysis are auditable.

This operational definition does **not** decide whether any correspondence comes from clairvoyance, telepathy, precognition, ordinary leakage, inference, chance, or another process. It defines the experiment before debating the explanation.

**Controlled Remote Viewing (CRV)** is one historically documented structured method. It is not synonymous with all remote viewing, and its stage language is not itself a scientific mechanism.

## What the source record actually says

The record is not a simple victory or debunking story:

- Early SRI publications reported target correspondence under sensory shielding and blind judging.
- Published critics reported failed duplication and transcript-cueing problems.
- Declassified training and operational files include apparent correlations, explicit low-correlation sessions, and raw reports whose interpretation was left to requesters.
- A 1972 U.S. assessment documents concern about reported Soviet parapsychology and behavior-influence research; it establishes collection and motivation, not Soviet efficacy.
- The 1975 SRI final report preserves the investigators’ positive programme case, while later critiques and reviews test whether those claims survive independent controls and operational evaluation.
- Decision Augmentation Theory is preserved as a testable 1995 mechanism hypothesis, not as a settled explanation.
- The 1995 American Institutes for Research review said laboratory hits occurred above chance, but found that the cause was unresolved and the operational product was vague, inconsistent, and not actionable.
- The two principal AIR expert reviewers agreed that the better experiments contained a statistical anomaly and disagreed about whether that established paranormal functioning.
- A 2023 meta-analysis reported a positive aggregate effect; its conclusions do not erase concerns about study independence, protocol heterogeneity, target/judge effects, or the field’s contested status.
- A 2026 survey of eleven remote-viewing experts found provisional agreement on blinding, training, neutral conditions, and multiple viewers, but it was expert opinion—not a randomized comparison of methods.

The module therefore keeps positive, negative, mixed, and practitioner sources in one ledger.

## Core rules

1. **Blind before belief.** A session that leaks the target may be interesting introspection, but it is not defensible remote-viewing evidence.
2. **Description before naming.** “Cold, metallic, curved, repetitive impact” is data; “submarine” is an interpretation. Record the interpretation as **AOL** rather than deleting it.
3. **Lock before feedback.** Hash or otherwise freeze the complete transcript and drawings before anyone reveals the target.
4. **Judge against decoys.** A narrative that seems impressive in isolation can match many targets. Forced comparison makes that visible.
5. **Preserve nulls.** No discarding “bad energy,” tired sessions, inconvenient targets, or failed viewers after seeing results.
6. **Separate claims.** Above-chance scoring, a paranormal cause, a specific mechanism, trainability, and operational usefulness are five different claims.
7. **Do not operationalize a single session.** Remote-viewing output is not a basis for medical, legal, financial, security, rescue, or allegations about a person.
8. **Respect privacy and consent.** Do not target private people, residences, passwords, intimate activity, health conditions, or non-public operations.
9. **Link; do not silently republish.** External papers, manuals, and archives retain their own rights. This module contains original synthesis and metadata, not copied payload collections.
10. **Never convert confidence into accuracy.** Record both; measure their relationship later.

## The six-stage CRV map, in one page

The detailed protocol is in [`practice-protocol.md`](practice-protocol.md). The historical stage map is:

| Stage | Working purpose | Primary output | Main failure mode |
|---|---|---|---|
| I | Rapid site contact / gestalt | ideogram-like mark; land/water/structure/open-space impressions | interpreting the mark after the fact |
| II | Elementary sensory qualities | colour, temperature, texture, sound, smell, taste, basic dimensionals | naming an object from one sensation |
| III | Spatial relationships | freehand sketches, boundaries, mass, movement, perspective | beautifying a sketch to fit a guess |
| IV | Structured categories | sensory, dimensional, energetic, material, biological, activity, aesthetic, conceptual/function data | high-level story construction |
| V | Probe prior data | subcomponents and relationships derived from a selected Stage-IV datum | leading questions and confirmation |
| VI | Model / expanded perspective | detailed diagrams, maps, clay or other spatial models, movement exercises | unconstrained imaginative elaboration |

“Matrix” and “signal line” are preserved as CRV practitioner vocabulary. The module does not label them established physical entities.

## Minimum viable first session

1. A target manager privately creates or loads a target pool.
2. The manager runs `target_manager.py assign`, keeps the private assignment, and gives the viewer only the public task.
3. The viewer completes a 20–40 minute session using the worksheet, recording raw descriptors and marking every object-level guess as AOL.
4. The viewer runs `target_manager.py lock` on the transcript before receiving any feedback.
5. A judge ranks the locked transcript against the target plus three or more decoys using a predeclared rubric.
6. Only then does the manager run `target_manager.py reveal`.
7. The complete task, transcript lock, ranking, reveal, score, and feedback notes enter the session ledger—even when the result is poor.

Twenty clean sessions teach more than one spectacular anecdote.

## Publication and safety boundary

This is a historical, methodological, and experimental-learning resource. It does not certify paranormal ability, provide intelligence tradecraft, or recommend action against real people. The tool manages opaque practice targets and integrity commitments; it does not hide classified data, scrape targets, or automate surveillance.

The user-provided conversation that motivated the module is not republished. Its durable contribution is represented as public-safe intent: investigate the method from a first-principles possibility stance and build a usable research department around it.

## Promotion gates

The module becomes a formal Great Library Work only after all of the following are true:

- the active whole-Library Snapshot lane has closed;
- at least the government archive, CRV manual lineage, AIR review, core experimental papers, critiques, and current reviews have direct source receipts;
- rights and redistribution states are explicit;
- ten or more clean pilot sessions demonstrate that the task, lock, reveal, judge, and ledger workflow is usable;
- the claim and source schemas have stabilized;
- an independent reviewer can reproduce the module checks from a clean checkout.

A future Release should identify the exact Git revision of this module. A future Source Inventory should reference, not contain, the external STARGATE corpus and scholarly payloads.
