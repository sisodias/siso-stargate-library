# Civilian Tools, Communities, Media, and Solo Automation

> **Observed:** 2026-08-07.  
> **Purpose:** audit the civilian remote-viewing ecosystem and specify a solo practice system that reduces ordinary leakage without pretending that software, testimony, or a polished interface proves anomalous perception.

## 1. Evidence boundary

Civilian remote-viewing material comes in several evidentiary classes that must not be collapsed:

| Class | What it can establish | What it cannot establish by itself |
|---|---|---|
| Source code and repository history | what a tool is designed to do; whether its implementation can be inspected; license and maintenance state | that remote viewing works, that a deployment matches the code, or that a scoring model is valid |
| Product or app documentation | what the vendor says the product does; current public workflow and pricing | independent efficacy, absence of leakage, correct randomization, or reproducible scoring |
| Community target pools and session posts | practice opportunities, protocol conventions, examples, and research leads | complete trial accounting, representative performance, or controlled evidence |
| Interviews and demonstrations | testimony, historical recollection, and visible procedure | adequate blinding, hidden edits, target-pool fairness, chance calibration, or replication |
| Controlled studies and archival records | the design and reported result of a defined test or programme | universal mechanism, broad trainability, or operational usefulness beyond the tested conditions |

A useful tool can be methodologically incomplete. A compelling video can be genuine testimony and still be weak evidence. A proprietary app can make strong claims while exposing too little information to audit them.

## 2. Audited civilian tools and platforms

### `psitool/psitool`

**Status:** verified public source repository; Rust; GPL-3.0.  
**Primary source:** `SRC-GH-PSITOOL`.

The repository provides command-line utilities for:

- selecting a target from one or more local pools;
- avoiding already completed targets;
- downloading candidate practice images from Wikimedia;
- retaining source metadata and license fields;
- supporting private image or text target pools;
- producing a content-derived remote-viewing identifier;
- revealing a selected target after the user completes a session;
- recording the user's own hit, score, and notes.

**Strong use:** local pool management and self-blind target selection.

**Not supplied by the documented workflow:** an independently held assignment, an immutable pre-feedback transcript lock, a blind decoy judge, a preregistered analysis, or an objective automatic score. Its self-entered “hit” and 0–100 score are practice notes, not scientific measurements.

### `nykotar/rvme`

**Status:** verified public source repository; Django application; AGPL-3.0; repository archived.  
**Primary source:** `SRC-GH-RVME`.

The archived README describes a collaborative target-pool website with difficulty levels, moderated target submissions, additional feedback, no-repeat targets, personal encrypted targets, and a precognitive mode in which the target is selected at reveal.

**Strong use:** a concrete open-source design reference for target-pool workflow and future-target assignment.

**Limit:** archived code is not evidence that a public deployment remains available, secure, or methodologically current. “Encrypted personal targets” and “precognitive mode” must be verified in the exact deployed revision before relying on them.

### `lukeskytorep-bot/echo-claw`

**Status:** verified public repository; CC BY 4.0; experimental architecture and templates rather than a finished validation platform.  
**Primary source:** `SRC-GH-ECHO-CLAW`.

The repository proposes separate AI Monitor and Viewer roles, a protected target vault, external memory, post-reveal correction logs, and future multi-agent analysis. Its own README says it is not proof, not a finished commercial product, and not a guarantee of successful remote viewing.

**Strong use:** design ideas for isolating target knowledge from a guided viewer agent.

**Limit:** role labels do not create isolation. The implementation must prove that the Viewer process, prompt context, logs, retrieval layer, tool permissions, and model provider never receive target or feedback data before lock.

### ClairV

**Status:** a JavaScript web application was reachable at the reviewed domain; no public source repository was identified in this review.  
**Primary source:** `SRC-CLAIRV-WEB-2026`.

Treat it as an opaque practice surface unless a specific source repository, deployed commit, target-selection procedure, privacy policy, and scoring specification are supplied. “Free” and “blind” describe access and intended workflow, not auditability.

### VEREVIO

**Status:** proprietary mobile application with in-app purchases.  
**Primary source:** `SRC-VEREVIO-APPSTORE-2026`.

The App Store listing describes remote-viewing, telepathy, precognition, postcognition, “scan box,” quiz, whiteboard, target, and statistics features. It also contains broad promotional claims about ESP and describes user-content and identifier handling in its privacy disclosure.

**Strong use:** surveying current consumer training interfaces and exercise types.

**Limit:** vendor-authored descriptions and app-store ratings are not independent evidence. The target pool, randomizer, exclusion rules, quiz ontology, scoring formula, server logs, model versions, and complete trial data would need separate inspection.

### Social RV

**Status:** proprietary/community platform with public product documentation.  
**Primary source:** `SRC-SOCIAL-RV-2026`.

The platform says it assigns a random target, accepts scanned session pages, reveals after submission, and uses an AI judge to rank the target against nine decoys.

**Strong use:** a practical reference for upload-before-reveal and decoy-based AI judging.

**Limit:** “AI judge” is not automatically independent. A defensible evaluation needs the exact model and version, frozen prompt, candidate-set construction, image/text preprocessing, target-label blindness, retry policy, temperature or seed settings, missing-session policy, and raw rank outputs.

### IRVA, Focal Point, and public talks

**Status:** active practitioner/research association and community programmes.  
**Primary sources:** `SRC-IRVA-2026`, `SRC-IRVA-FOCAL-POINT-2026`, and `SRC-IRVA-FIRESIDE-2026`.

IRVA provides educational material, conference recordings, historical work, a research unit, and the Focal Point practice-target programme. These are valuable for terminology, practitioner history, target practice, reviewer recruitment, and leads to primary records.

**Limit:** an association page, conference talk, or membership programme represents the organization or speaker. It is not an independent controlled trial.

### The Monroe Institute

**Status:** active commercial training provider.  
**Primary source:** `SRC-MONROE-RV-2026`.

Its current programme materials describe Viewer, Monitor, and Judge roles; double-blind independently judged trials; audio exercises; live instruction; and recorded presentations by Joseph McMoneagle.

**Strong use:** documenting a contemporary training model and locating first-person historical presentations.

**Limit:** course descriptions, testimonials, demonstrations, and trainer biographies are provider claims. They should be indexed as testimony or practice material unless the underlying blinded trial artifacts and analysis are available.

### `r/remoteviewing`

**Status:** large user-generated community with guides, target links, discussions, and posted sessions.  
**Primary source:** `SRC-REDDIT-RV-2026`.

**Strong use:** finding tools, current practice conventions, public session sheets, software leads, and potential replication collaborators.

**Limit:** posts are self-selected, can be edited or deleted, and often reveal only successful or interesting sessions. A subreddit is a discovery layer, not a trial registry.

## 3. What replacing a coordinator with software really solves

A software coordinator can reduce several ordinary channels:

- facial expression, tone, or body-language cueing;
- a human monitor accidentally revealing target class;
- deliberate target switching after seeing a weak session;
- repeated targets, if the pool ledger is reliable;
- casual peeking, if the target remains server-side or in a protected account;
- lost timing information, if events are automatically timestamped.

It does **not** automatically solve:

- filenames, thumbnails, EXIF data, alt text, cache entries, browser previews, or API responses leaking the target;
- an unbalanced pool that makes “water,” “mountain,” or “building” high-probability guesses;
- a user repeatedly abandoning trials before reveal;
- editing or adding transcript material after feedback;
- choosing favorable scoring rules after seeing the result;
- an AI judge knowing which candidate is correct;
- decoys that are visibly less compatible than the target;
- silent target reuse or removal;
- selective publication;
- a model provider retaining target and session content;
- a voice agent receiving target information through shared memory, retrieval, tools, or conversation history;
- the possibility that a positive result comes from chance, inference, or an artifact rather than anomalous information transfer.

“Software-mediated” and “double-blind” are not synonyms. Blinding is a property of the complete information flow.

## 4. Minimal rigorous solo architecture

```text
                          ┌──────────────────────────┐
                          │  frozen target manifest  │
                          │ hashes, rights, classes  │
                          └─────────────┬────────────┘
                                        │
                         private only   ▼
┌──────────────┐       ┌──────────────────────────┐
│ entropy / RNG│──────>│ assignment + commitment  │
└──────────────┘       │ target, nonce, pool hash │
                       └─────────────┬────────────┘
                                     │ public task contains no target
                                     ▼
                       ┌──────────────────────────┐
                       │ viewer session client    │
                       │ cue, paper/audio, stages │
                       └─────────────┬────────────┘
                                     │ complete artifacts
                                     ▼
                       ┌──────────────────────────┐
                       │ immutable transcript lock│
                       │ pages, audio, metadata   │
                       └─────────────┬────────────┘
                                     │
                 ┌───────────────────┴───────────────────┐
                 ▼                                       ▼
      ┌──────────────────────┐                ┌──────────────────────┐
      │ blind candidate pack │                │ append-only ledger   │
      │ target + decoys      │                │ every trial / abort  │
      └──────────┬───────────┘                └──────────────────────┘
                 ▼
      ┌──────────────────────┐
      │ blind human/AI judge │
      │ ranks all candidates │
      └──────────┬───────────┘
                 ▼
      ┌──────────────────────┐
      │ reveal + audit receipt│
      │ verifies all hashes  │
      └──────────────────────┘
```

### Required invariants

1. **Frozen pool:** publish or privately commit to a manifest before the series begins.
2. **Opaque public task:** no target title, class, URL, filename, alt text, or pool query appears in viewer-visible state.
3. **Unpredictable assignment:** use an operating-system cryptographic random source or a documented external randomness service.
4. **Commitment before session:** commit to target identity, pool version, nonce, and assignment metadata.
5. **Complete lock:** hash every page, audio file, typed note, session setting, start/stop time, and confidence value.
6. **No silent aborts:** every initiated session receives a ledger state such as completed, predeclared abort, technical failure, or protocol violation.
7. **Blind candidates:** the judge sees candidate labels randomized independently of target identity.
8. **Symmetrical decoys:** choose decoys under a rule fixed before judging; do not hand-pick obviously poor alternatives after reading the transcript.
9. **Frozen judge:** preserve human rubric or AI model, version, prompt, preprocessing, parameters, and raw outputs.
10. **Verifiable reveal:** reveal must fail if the assignment, transcript, candidate pack, or ranking has changed.
11. **Exportability:** users can export all trials, misses, metadata, target receipts, and scores in a documented format.
12. **Holdout testing:** optimize on a training pool and evaluate on a new pool with rules fixed in advance.

The included [`tools/target_manager.py`](tools/target_manager.py) supplies assignment commitment, public/private separation, transcript locking, reveal verification, and overwrite protection. It intentionally does not claim to be a full application, target downloader, judge, or statistical analysis service.

## 5. Target-blind voice monitor

A voice agent can remove the viewer's need to remember stage instructions, but only when it is separated from target state.

### The monitor may receive

- session ID and opaque cue;
- current stage and elapsed time;
- the viewer's spoken data, if recording is consented;
- a fixed prompt library;
- predeclared neutral probes;
- protocol-stop conditions.

### The monitor must not receive

- target identity, target class, feedback image, target URL, or target metadata;
- candidate set or correct candidate;
- previous reveal text that encodes likely pool patterns;
- private assignment files;
- analytics that say whether a live impression is “close”;
- web browsing or retrieval over the target vault;
- a shared conversation memory containing target preparation.

### Neutral prompt contract

The agent should:

- speak only from a versioned prompt schedule;
- ask for raw sensory, dimensional, material, movement, and spatial data;
- remind the viewer to label AOL without confirming or rejecting it;
- never supply example targets during a live session;
- never praise a specific impression as a hit;
- mark every movement instruction before the response;
- timestamp prompts and responses;
- stop at the predeclared duration;
- produce a prompt log that is locked with the transcript.

A safe minimal system prompt is:

```text
You are a target-blind procedural monitor. You have no target access and must not
infer, name, search for, or score the target. Guide the viewer through the frozen
session schedule using neutral prompts only. Ask for observable qualities and
relationships, not object names. When the viewer gives an object-level guess,
say only: “Mark that as AOL; return to the underlying qualities.” Do not alter
the schedule based on whether an impression sounds plausible. End at the fixed
time and export the complete timestamped prompt log.
```

An LLM used later as a judge must be a separate process with no access to target labels, reveal state, viewer identity, past score, or conversational history.

## 6. Scoring: correct the “percentage of matching words” myth

There is no single universal “SRI score” in which every adjective that appears compatible with the revealed image receives one point and the total is divided by all words.

Historically important laboratory work often used blind judges who matched or rank-ordered transcripts against a target set. The AIR review describes standard rank-order judging and gives the expected rank and effect-size calculation for five choices. Other programme work used additional methods, including binary features or fuzzy-set analyses.

A raw descriptor percentage is fragile unless all of the following were fixed before the trial:

- the descriptor ontology;
- synonym and contradiction rules;
- whether generic terms count;
- feature prevalence across the whole pool;
- partial-credit rules;
- who performs coding and whether they are blind;
- treatment of missing, repeated, or negated descriptors;
- weighting of distinctive versus common features;
- the denominator;
- inter-rater reliability.

For a first replication, use rank of the actual target among symmetrical candidates as the primary outcome. Descriptor coding can remain a secondary diagnostic measure.

## 7. Training-duration claims

The reviewed historical manual and current expert/practitioner sources document training systems, practice recommendations, and beliefs about skill development. They do not establish one universal threshold such as:

- “several hundred sessions before the signal separates”;
- “six to twelve months for the basics”;
- “two to three years before operational readiness”;
- a fixed number of sessions after which anyone becomes reliable.

Those statements may describe individual schools or recollections. They should not be presented as measured population facts without cohort records, common tests, attrition data, and held-out outcomes.

A better training metric is:

> Does performance on preregistered held-out trials improve relative to baseline, chance, and a matched control condition while protocol violations and judge disagreement remain visible?

Track clean trial count, actual-target rank, confidence calibration, AOL rate, contradiction rate, inter-judge agreement, and held-out performance. Hours or repetitions are inputs, not proof of learning.

## 8. State, brainwave, food, and substance claims

The reviewed remote-viewing sources do not establish a required alpha/theta frequency, an empty-stomach advantage, a universal caffeine rule, or a cannabis benefit.

The cannabis theory in the motivating conversation was: THC might reduce analytical chatter and therefore reduce AOL. That is a hypothesis, not a finding. A randomized crossover study outside remote viewing reported that acute oral THC impaired visual working memory, increased mind wandering, and reduced metacognitive accuracy. That does not prove THC worsens remote viewing, but it directly undermines the assumption that intoxication is a free reduction in “analytical noise.” See `SRC-THC-WORKING-MEMORY-2020`.

For ordinary practice:

- establish a sober baseline first;
- do not treat subjective vividness, dissociation, or confidence as accuracy;
- record sleep, illness, stress, caffeine, alcohol, cannabis, medication, timing, and dose category before the session;
- predeclare any exclusion rule;
- do not compare a hand-picked intoxicated “best session” against a complete sober series;
- do not operate vehicles, machinery, or make material decisions while impaired;
- follow applicable law and clinical advice.

For formal substance research, use ethics review, medical screening, controlled dosing, placebo and blinding where lawful and appropriate, preregistration, and a design powered for an interaction with remote-viewing performance. This module does not recommend substance use as training.

## 9. How to use communities, interviews, and videos

Use them as a discovery and documentation layer:

1. record the exact speaker, title, venue, upload date, and publisher;
2. separate what the speaker personally witnessed from what they heard;
3. extract document IDs, session numbers, dates, names, and claimed outcomes;
4. locate the underlying tasking, transcript, feedback, evaluation, and complete trial series;
5. check whether the demonstration was live, edited, target-blind, independently judged, and preregistered;
6. preserve misses and contradictory accounts;
7. label memoir and testimony as such.

Footage is especially useful for learning page layout, pacing, monitor language, and practitioner phenomenology. It is not a substitute for the hidden parts of the protocol.

## 10. Build specification for a SISO solo trainer

### Version 0.1 — integrity first

- local or server-side target vault;
- target and pool content hashes;
- rights/provenance fields for every feedback item;
- target-class balance report;
- cryptographic assignment commitment;
- target-free public task;
- paper-photo, typed, and audio capture;
- target-blind deterministic voice monitor;
- transcript and prompt-log lock;
- candidate-pack commitment;
- blind human ranking;
- optional blind AI ranking with frozen model card;
- reveal receipt;
- append-only trial ledger;
- complete JSON/CSV export;
- automated protocol-violation flags;
- no delete-from-analysis button.

### Version 0.2 — research mode

- series preregistration;
- multiple viewers with independent sessions;
- multiple judges and inter-rater agreement;
- held-out target pools;
- automated chance simulations;
- stopping-rule enforcement;
- blinded condition comparisons;
- substance/state covariate capture;
- public de-identified artifact bundles;
- reproducible analysis notebook;
- signed software/version manifest.

### AI scoring card

Every AI score should ship with:

```json
{
  "model_provider": "recorded",
  "model_name": "recorded",
  "model_version_or_date": "recorded",
  "system_prompt_sha256": "recorded",
  "candidate_order_seed": "recorded",
  "target_label_hidden": true,
  "temperature": "recorded",
  "retries": 0,
  "preprocessing_sha256": "recorded",
  "raw_output_preserved": true
}
```

Without this card, a numerical AI score is not independently reproducible.

## 11. Bottom line

The civilian ecosystem is real: open-source target tools, archived community applications, proprietary practice platforms, practitioner organizations, training providers, forums, interviews, and recorded talks all exist.

The correct inference is not “therefore remote viewing is proven.” It is:

> There is enough public infrastructure to run a much cleaner solo test than a self-chosen picture and a post-reveal impression match.

The Great Library standard is stricter: freeze the target universe, isolate target knowledge, lock the complete session, judge blind against decoys, preserve every trial, and distinguish software functionality from evidence of the phenomenon.
