# Practice Protocol

This is a self-contained beginner protocol derived from the documented logic of Controlled Remote Viewing (CRV), declassified session forms, modern blinding practice, and the source split described in this module.

It is **not** a verbatim reproduction of any manual. It is an original, public-safe practice design.

## 1. What you need

### Roles

For the cleanest team session:

- **Target manager:** prepares the pool, randomly assigns the target, holds the private assignment, and reveals feedback only after the transcript is locked.
- **Viewer:** receives only an opaque cue and records impressions.
- **Monitor (optional):** keeps the viewer on procedure. The monitor must be blind to target identity and target class.
- **Judge:** compares the locked transcript with the target and decoys. The judge must not know which candidate is correct while ranking.
- **Analyst:** aggregates scores across sessions. This can be the judge after rankings are frozen, but separating the role is stronger.

One person must not quietly perform every role and then call the result double-blind.

### Materials

- unlined white paper;
- a dark pen that moves easily;
- a timer;
- the [`session-template.md`](session-template.md);
- a private target pool;
- the included target manager or an equivalent auditable randomizer;
- a way to scan or photograph every page before feedback;
- a session ledger.

CRV is commonly performed awake, seated, eyes open, and writing continuously. Closing the eyes briefly is not a scientific violation, but a cinematic trance is neither required nor evidence of better viewing.

## 2. Prepare the target correctly

### Target-pool rules

For training, create at least 24 targets with clear feedback and high contrast across:

- natural vs human-made;
- land vs water;
- open vs enclosed;
- static vs energetic;
- vertical vs horizontal;
- sparse vs crowded;
- organic vs metallic;
- hot/dry vs cold/wet.

Avoid pools where many targets share the same dominant gestalt. Four waterfalls and four bridges make matching easier without improving perception.

For a formal study:

- freeze the pool before the first trial;
- retain exact target images or scene definitions;
- assign target and decoy sets symmetrically;
- record provenance and rights;
- prevent the viewer and monitor from browsing the pool;
- prevent filenames or IDs from encoding the target;
- predeclare whether the target is a photograph, physical site, object, video, event, or future feedback item.

The included [`example-target-pool.json`](example-target-pool.json) is a tooling demonstration, not a formal research pool.

### Create the task

From the repository root:

```bash
python3 research/remote-viewing/tools/target_manager.py assign \
  --pool research/remote-viewing/example-target-pool.json \
  --session-id RV-PRACTICE-001 \
  --public-task /tmp/RV-PRACTICE-001-task.json \
  --private-assignment /secure/RV-PRACTICE-001-assignment.json
```

The target manager gives the viewer only the public task. The private assignment and target pool remain inaccessible.

An opaque cue does not need geographic meaning. Its purpose is to identify the task without describing the target.

## 3. Pre-session record

Before seeing the cue, the viewer records:

- date and time;
- sleep duration and quality;
- caffeine, alcohol, medication, acute illness, and major stress;
- prior knowledge of the pool, if any;
- expectation about target class;
- confidence before session;
- any reason the trial might later be excluded.

Exclusion decisions made after feedback are not valid unless the exact rule was predeclared.

### Two-minute reset

Use a brief neutral reset:

1. silence notifications;
2. sit with both feet supported;
3. breathe normally for ten slow breaths;
4. notice current thoughts without trying to suppress them;
5. write pre-session assumptions as **front-loaded AOL**;
6. begin.

Meditation may help some practitioners, but it is not a mandatory mechanism. Keep the reset identical across trials if you intend to measure progress.

## 4. The session

A beginner session can last 20–40 minutes. Stop at the predeclared time even if the target feels unfinished. The aim is a comparable series, not a masterpiece.

### Universal notation

Use these labels consistently:

- `S:` sensory descriptor;
- `D:` dimensional or spatial descriptor;
- `E:` energetic or movement descriptor;
- `M:` material descriptor;
- `B:` biological or life-related descriptor;
- `A:` activity;
- `AI:` aesthetic/emotional impact on the viewer;
- `C:` conceptual or functional impression;
- `AOL:` object-level guess or story;
- `AOL/S:` possible AOL with a persistent sensory basis;
- `BREAK:` intentional pause;
- `?` uncertain;
- `!` unusually strong impression.

Do not erase. Cross out once and continue. Every correction is part of the record.

### Stage I — cue, spontaneous mark, broad gestalt

1. Write the session ID and opaque cue.
2. Immediately make one fast, spontaneous pen movement without planning.
3. Write the first broad gestalt impressions that arise:
   - land;
   - water;
   - structure;
   - biological presence;
   - open space;
   - movement;
   - energetic event.
4. Repeat the cue and one rapid mark up to three times if the protocol calls for it.

The mark is not a Rorschach puzzle. Do not spend minutes decoding it. Record the immediate response and move on.

**Common error:** deciding that a curve “must be a river” and building the rest of the session around it.

### Stage II — raw sensory qualities

Move quickly through modalities:

- colours and luminosity;
- temperature;
- textures;
- sounds;
- smells;
- tastes;
- pressure, density, weight;
- basic dimensions such as tall, narrow, broad, deep, hollow, layered;
- movement such as rotating, falling, pulsing, flowing, rising.

Prefer adjectives and verbs over nouns.

Good:

```text
cool
smooth
hard
bright reflection
repeating impact sound
upward / narrow
moving air
```

Fragile:

```text
bell tower
helicopter
airport
```

Record each fragile object guess as AOL:

```text
AOL — helicopter
```

Then take a five-second break and ask for the underlying features:

```text
E: rotating / rhythmic
S: loud chopping sound
D: overhead
```

### Stage III — spatial sketching

Draw relationships, not artwork:

- horizon or dominant axis;
- major masses and voids;
- boundaries;
- vertical and horizontal elements;
- relative scale;
- curves, angles, repetitions;
- position of water, land, structure, and movement;
- near/far, inside/outside, above/below.

Annotate the sketch with descriptors. Add arrows for motion and dotted lines for uncertain boundaries.

Do not redraw to resemble an AOL. The first awkward sketch is often more informative than a polished reconstruction.

### Stage IV — structured matrix

Create columns or labelled zones:

| Category | Questions |
|---|---|
| Sensory | What colour, temperature, texture, sound, smell, or taste? |
| Dimensional | What shape, scale, depth, orientation, enclosure, or spacing? |
| Energetic | What moves, radiates, repeats, falls, rises, vibrates, or changes? |
| Material | Natural, stone, wood, metal, glass, fabric, soil, liquid, composite? |
| Biological | Presence, number, density, posture, motion—without naming identities? |
| Activity | What is happening? |
| AI | What immediate atmosphere or bodily response appears? |
| Concept/function | What might the place or object be for? Treat this as lower-confidence. |
| AOL | What named object, place, person, or story is the mind proposing? |

Stage IV is where stories become tempting. Keep conceptual/function data visibly separate from sensory and spatial data.

### Stage V — focused probing

Select one earlier datum, not a preferred story.

Examples:

```text
Probe: "repeating metallic impact"
Subcomponents: hollow / regular interval / hard surfaces / vibration
Relationship: source above and to the left of central mass
```

Use neutral probes:

- “What produces this sensory quality?”
- “What is the relationship between X and Y?”
- “Describe the material of X.”
- “Describe the activity at X.”
- “What changes over time?”

Avoid leading probes:

- “Describe the submarine.”
- “Why is this military?”
- “Show me the alien base.”

A leading question can manufacture detail even in ordinary imagination.

### Stage VI — model and controlled perspective

Use only when earlier data are stable.

Options:

- larger annotated diagram;
- top-down map;
- side elevation;
- simple clay model;
- scale comparison;
- movement exercise such as “from 100 metres above, describe the largest spatial relationships.”

Every movement instruction must be written before its answer. Do not retroactively claim that a sketch came from a special perspective.

For beginners, Stage VI is optional. More detail is not automatically more accuracy.

## 5. Session close

Before feedback:

1. write a three-layer summary:
   - **high-confidence raw features;**
   - **medium-confidence spatial/activity features;**
   - **low-confidence concepts and AOL;**
2. name the dominant gestalt without naming a specific target;
3. record post-session confidence from 0 to 100;
4. number every page;
5. scan or photograph all pages;
6. save a plain-text or PDF transcript;
7. lock the file.

Example:

```bash
python3 research/remote-viewing/tools/target_manager.py lock \
  --session-id RV-PRACTICE-001 \
  --transcript sessions/RV-PRACTICE-001.md \
  --out sessions/RV-PRACTICE-001-lock.json
```

No sentence, sketch, page order, or confidence value may be changed after the lock. Corrections belong in a separate post-feedback note.

## 6. Blind judging

### Candidate set

Present the judge with the locked session and at least four candidate targets: one actual target and three decoys selected under a rule fixed before the trial.

The judge should not know:

- which candidate is correct;
- which viewer produced the transcript, when practical;
- the viewer’s prior success;
- the target manager’s expectations;
- whether the trial is being treated as a “special” case.

### Simple rank-order rubric

Score each candidate from 0 to 4 in each category:

- dominant gestalt;
- sensory qualities;
- geometry/spatial layout;
- materials;
- energy/movement;
- biological/activity;
- distinctive low-base-rate features;
- contradictions.

Record both positive matches and contradictions. Then rank all candidates from best to worst. Do not award points to a candidate merely because it fits one AOL.

For a four-candidate set:

- top rank is a hit under the simplest outcome;
- chance top-rank rate is 25% if assignment and candidate construction are valid;
- one hit is uninformative;
- performance must be assessed over a predeclared series.

A second and third judge allow inter-rater reliability to be measured.

## 7. Reveal and feedback

After ranking is frozen, the target manager reveals:

```bash
python3 research/remote-viewing/tools/target_manager.py reveal \
  --private-assignment /secure/RV-PRACTICE-001-assignment.json \
  --transcript-lock sessions/RV-PRACTICE-001-lock.json \
  --out sessions/RV-PRACTICE-001-reveal.json
```

Feedback has two purposes:

- close the learning loop;
- create a complete audit trail.

It does not license rewriting the session.

### Post-feedback review

Use different ink or a new file. Mark:

- direct correspondences;
- partial correspondences;
- contradictions;
- generic descriptors that fit many candidates;
- AOL that helped;
- AOL that hijacked the session;
- data that matched a decoy better;
- possible cueing or procedural contamination;
- one specific adjustment for the next session.

Do not write only the exciting matches.

## 8. A solo practice design

True role separation is harder alone. Use one of these:

### Delayed manager

Ask a trusted person to create assignments for a block of sessions and reveal only after each lock.

### Script plus inaccessible private directory

Run the assignment command in an account or directory you cannot inspect during the session. Give yourself only the public task. This is self-blind only to the extent that the private file is genuinely inaccessible.

### Target-after-lock precognition design

Complete and lock the session before an external randomizer selects the target. This strongly prevents ordinary target leakage but tests a different hypothesis—future target/feedback correspondence—not ordinary preselected-target clairvoyance.

Never call a self-chosen target blind.

## 9. Eight-week beginner programme

The unit of progress is a clean trial, not a dramatic story.

### Weeks 1–2: raw description

- 10 sessions;
- Stage I and II only;
- targets with strong, distinct gestalts;
- score sensory and dimensional descriptors;
- practice immediate AOL logging.

### Weeks 3–4: space

- 10 sessions;
- add Stage III;
- judge sketches separately from words;
- track whether object naming improves or harms rank.

### Weeks 5–6: structured detail

- 10 sessions;
- add Stage IV;
- keep concepts/functions lower-weight than sensory/spatial data;
- introduce multiple blind judges.

### Weeks 7–8: probing and replication

- 10 sessions;
- add carefully written Stage V probes and optional Stage VI models;
- pre-register a primary outcome for the final ten;
- hold out a new target pool;
- have another target manager reproduce the workflow.

Forty complete sessions provide a meaningful learning record. They still do not prove a paranormal mechanism.

## 10. Metrics to track

Per trial:

- candidate-set size;
- rank of actual target;
- category scores for every candidate;
- high-confidence descriptor count;
- contradiction count;
- AOL count and AOL accuracy;
- viewer confidence;
- judge identity;
- duration;
- protocol deviations.

Across a block:

- top-rank hit rate;
- mean rank of actual target;
- effect of viewer, target, judge, and protocol stage;
- inter-judge agreement;
- confidence calibration;
- predeclared versus exploratory results;
- miss and abort rates;
- change over time;
- performance on held-out targets.

Do not optimize on the same block used to claim success.

## 11. Failure modes

| Failure | Why it matters | Repair |
|---|---|---|
| Viewer knows the target class | ordinary inference narrows the pool | opaque cue and isolated pool |
| Monitor knows target | verbal and nonverbal cueing | blind monitor |
| Target selected after an unsatisfactory result | optional assignment | immutable randomization log |
| Transcript edited after reveal | hindsight contamination | hash before feedback |
| Judge sees only the correct target | unconstrained matching | rank against decoys |
| Only best sessions retained | selection bias | session registry before start |
| AOL treated as forbidden | guesses are hidden rather than measured | label and preserve AOL |
| Every miss called displacement | theory cannot lose | predeclare displacement rule or do not use it |
| Viewer confidence substitutes for score | confidence may be uncalibrated | record both independently |
| Multiple viewers discussed target first | correlated errors masquerade as convergence | independent sessions before aggregation |
| Pool reused until memorized | pool knowledge leaks | rotate and hold out pools |
| “Energetic” target always means explosion | target ontology is biased | balance target classes |
| Private-person target | ethical and legal risk | public, consented, or synthetic practice targets only |

## 12. Ethics and decision boundary

Do not use remote-viewing sessions to:

- accuse a named person of a crime, affair, illness, motive, or hidden identity;
- locate or contact a missing person outside an authorized, consented research or public-safety process;
- diagnose or treat health conditions;
- trade, gamble, or make material financial decisions;
- bypass privacy, authentication, or security controls;
- target intimate spaces, children, private residences, or non-public operations;
- replace ordinary evidence in legal, military, rescue, or intelligence decisions.

A session can generate a hypothesis for a low-stakes practice target. It cannot validate a real-world allegation.

## 13. A clean first objective

Do not begin with “view a secret base.” Begin with:

> Across 20 preregistered four-choice trials using a balanced target pool and two blind judges, does the actual target receive a better mean rank than expected under the randomization model?

That question is small enough to answer and strong enough to teach the entire discipline.
