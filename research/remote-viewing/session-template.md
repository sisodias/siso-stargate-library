# Remote-Viewing Session Worksheet

> Use one copy per session. Complete every pre-session field before reading the cue. Do not add or edit session data after the transcript lock; post-feedback learning belongs in the final section.

## A. Session registry

| Field | Entry |
|---|---|
| Study ID | |
| Session ID | |
| Viewer ID | |
| Date | |
| Start time and time zone | |
| Planned protocol/stages | |
| Public task file | |
| Target manager ID | |
| Monitor ID or `none` | |
| Judge IDs, assigned later | |
| Candidate-set size | |
| Predeclared abort rule | |

### State before cue

| Measure | Value |
|---|---|
| Sleep, hours | |
| Alertness, 0–10 | |
| Stress, 0–10 | |
| Mood, short label | |
| Hunger/thirst/discomfort | |
| Caffeine/medication relevant to attention | |
| Prior knowledge of target pool | none / possible / known |
| Environmental interruptions expected | |

Protocol deviations already known:

```text

```

---

## B. Public task

| Field | Entry |
|---|---|
| Opaque cue | |
| Session commitment | |
| Task issued at | |
| Task wording | Describe the target associated with the cue. Record raw sensory and spatial data before interpretation. |

Viewer declaration before beginning:

- [ ] I cannot access the private assignment or target pool.
- [ ] No person present knows the target identity or target class.
- [ ] I will label object-level interpretations as AOL.
- [ ] I will preserve all pages and lock the complete record before feedback.

---

## C. Stage I — immediate response and gestalt

Write the cue once. On first exposure, make one rapid spontaneous mark without trying to draw an object.

**Cue:** ______________________________

**Ideogram / spontaneous mark:**

```text




```

Trace once, without inventing detail. Record the first broad impressions:

| Category | Immediate impression |
|---|---|
| Major gestalt | land / water / structure / biological / open space / motion / unknown |
| Movement | |
| Scale | |
| Verticality | |
| Density | |
| First affect | |

AOLs triggered immediately:

```text
AOL:
```

---

## D. Stage II — raw sensory and dimensional data

Use short words or fragments. Do not turn the list into a scene.

| Channel | Raw descriptors |
|---|---|
| Colours / light | |
| Temperatures | |
| Textures | |
| Sounds | |
| Smells | |
| Tastes | |
| Pressure / weight | |
| Motion / rhythm | |
| Energy / intensity | |
| Shapes | |
| Size / scale | |
| Distance / depth | |
| Natural / artificial qualities | |
| Other | |

For every object or place name, write it here rather than hiding it:

```text
AOL:
AOL:
AOL:
```

Breaks or disturbances:

```text

```

---

## E. Stage III — spatial sketch

Draw boundaries, masses, relationships, perspective, horizons, paths, motion, and relative scale. Label only with raw descriptors or neutral element IDs such as `A`, `B`, and `C`.

```text









```

### Spatial inventory

| Element | Position / relationship | Shape / mass | Movement | Confidence 0–100 |
|---|---|---|---|---:|
| A | | | | |
| B | | | | |
| C | | | | |
| D | | | | |

AOLs from sketching:

```text
AOL:
```

---

## F. Stage IV — structured data matrix

Record data first; interpretive or conceptual material gets a lower evidential weight unless the study specifies otherwise.

| Category | Data |
|---|---|
| Sensory | |
| Dimensional / spatial | |
| Energetic / movement | |
| Materials | |
| Natural features | |
| Man-made features | |
| Biological presence | |
| Human activity | |
| Emotional atmosphere / aesthetic impact | |
| Function / purpose / concept | |
| Names, labels, symbols, numbers | |
| AOL / object-level story | |

### Element matrix

| Element | Sensory | Spatial | Material | Activity / function | AOL risk |
|---|---|---|---|---|---|
| A | | | | | |
| B | | | | | |
| C | | | | | |

---

## G. Stage V — neutral probing

Probe only a datum already recorded. Write the probe exactly as used. Avoid “Is it a bridge?” or any question that supplies an answer.

Recommended neutral forms:

```text
Describe the source of [datum].
Describe the relationship between [A] and [B].
Describe what is immediately above / below / inside / beyond [element].
Describe the most distinctive low-level feature of [element].
```

| Probe | Immediate response | Follow-up raw data | AOL |
|---|---|---|---|
| | | | |
| | | | |
| | | | |
| | | | |

---

## H. Stage VI — model, map, or movement exercise

Use only when the protocol calls for it. Record the exact movement instruction before the response.

**Movement instruction:**

```text

```

**Expanded sketch / model notes:**

```text









```

If a physical model was made, record photograph or artifact IDs:

```text

```

---

## I. Close before feedback

### Dominant raw pattern

In no more than five lines, summarize the most repeated low-level data without naming the target:

```text
1.
2.
3.
4.
5.
```

### AOL summary

```text
Most persistent AOL:
Other AOLs:
Did AOL change the session path? yes / no / uncertain
```

### Confidence and quality

| Measure | Value |
|---|---:|
| Confidence target correspondence exists, 0–100 | |
| Confidence dominant gestalt is correct, 0–100 | |
| Perceived signal clarity, 0–10 | |
| Perceived analytical interference, 0–10 | |
| Fatigue at close, 0–10 | |

### Completion

| Field | Entry |
|---|---|
| End time | |
| Total minutes | |
| Page count | |
| Digital transcript path | |
| Drawings/model artifact paths | |
| Known protocol deviations | |
| Abort? If yes, rule triggered | |

Viewer declaration:

- [ ] This is the complete session record.
- [ ] I have not seen feedback or the candidate targets.
- [ ] All pages are included and numbered.
- [ ] The transcript is ready to lock.

**Transcript-lock command:**

```bash
python3 research/remote-viewing/tools/target_manager.py lock \
  --session-id SESSION_ID \
  --transcript PATH_TO_COMPLETE_TRANSCRIPT \
  --out PATH_TO_LOCK_JSON
```

**Transcript SHA-256:** ______________________________

**Locked at:** ______________________________

---

## J. Blind judging sheet

Complete this before the correct candidate is revealed.

| Field | Entry |
|---|---|
| Judge ID | |
| Candidate-set ID | |
| Judging started | |
| Judging completed | |
| Judge blind to correct candidate? | yes / no |
| Judge blind to viewer identity/history? | yes / no |
| Rubric version | |

### Candidate scoring

Use the same rubric for every candidate. Record contradictions as well as matches.

Suggested dimensions, each scored `0`–`4`:

- major gestalt;
- geometry and spatial layout;
- sensory qualities;
- materials;
- motion or energy;
- distinctive low-base-rate features;
- activity or function, lower weight unless preregistered;
- contradiction penalty.

| Candidate ID | Gestalt | Spatial | Sensory | Material | Motion | Distinctive | Function | Contradiction penalty | Total | Rank |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |
| | | | | | | | | | | |

Judge notes explaining the ranking:

```text

```

Ranking frozen at: ______________________________

Judge signature or integrity receipt: ______________________________

---

## K. Reveal

Run only after every required judge ranking is frozen.

```bash
python3 research/remote-viewing/tools/target_manager.py reveal \
  --private-assignment PATH_TO_PRIVATE_ASSIGNMENT \
  --transcript-lock PATH_TO_LOCK_JSON \
  --out PATH_TO_REVEAL_JSON
```

| Field | Entry |
|---|---|
| Reveal file | |
| Reveal verified | yes / no |
| Actual target ID | |
| Correct-candidate position | |
| Actual target rank | |
| Top-rank hit | yes / no |
| Target feedback opened at | |

---

## L. Post-feedback comparison

This section is learning data and must never be merged back into the locked transcript.

### Strong correspondences

```text
1.
2.
3.
4.
5.
```

### Clear contradictions

```text
1.
2.
3.
4.
5.
```

### Generic descriptors that fit many candidates

```text

```

### AOL outcomes

| AOL | Correct / partly correct / wrong / unjudgeable | Did it help or derail? |
|---|---|---|
| | | |
| | | |
| | | |

### Calibration

| Measure | Pre-reveal | Outcome note |
|---|---:|---|
| Overall confidence | | |
| Gestalt confidence | | |
| Signal clarity | | |

### Learning note

What one procedural change, if any, is allowed for the next **training** block?

```text

```

Do not change a confirmatory protocol mid-block. Record proposed changes for the next preregistered block.

---

## M. Session ledger closeout

| Field | Entry |
|---|---|
| Trial status | complete / abort / major deviation / fatal deviation |
| Included in confirmatory analysis | yes / no / pending blind rule |
| Reason if excluded | |
| All files preserved | yes / no |
| Assignment commitment verified | yes / no |
| Transcript lock verified | yes / no |
| Judge ranking preserved | yes / no |
| Reveal receipt preserved | yes / no |
| Data-entry checker | |
| Closed at | |

One session is one row in a larger series. Preserve it whether it looks impressive, ordinary, or completely wrong.
