# Source Map

This map is the human reading guide for [`source-index.json`](source-index.json). It deliberately combines government records, positive studies, negative studies, opposing expert assessments, practitioner manuals, and current reviews.

## Reading rule

Do not ask a source to prove more than it can.

- A **programme file** proves that a programme, task, session, or evaluation record existed.
- A **training manual** proves what practitioners were taught.
- A **session transcript** records an output, not necessarily its accuracy or value.
- A **session evaluation** records an evaluator's judgment, not necessarily a blind or calibrated score.
- A **positive experiment** supports the result under its own design and analysis.
- A **failed replication or critique** identifies failure under its own design or an alternative explanation.
- A **review** depends on its source selection, coding, assumptions, and available evidence.
- An **expert consensus survey** maps expert opinion; it does not substitute for an experiment.

The source ledger uses stable local IDs so every module claim can point to a defined evidence object.

## Fastest balanced route

Read these in order:

1. **`SRC-CIA-AIR-1995`** — the government-commissioned closeout, including laboratory and operational conclusions.
2. **`SRC-UTTS-1995`** and **`SRC-HYMAN-1995`** — the two expert assessments whose shared observations and divergent inferences are often flattened in retellings.
3. **`SRC-CRV-MANUAL-1986`** — the actual CRV stage language and practitioner theory.
4. **`SRC-DIA-USSR-1972`** — the Cold War foreign-programme assessment, read as a U.S. intelligence source rather than proof of Soviet capability.
5. **`SRC-CIA-PAT-1975`** and **`SRC-CIA-DAT-1995`** — the programme’s positive contractor case and a later formal mechanism hypothesis.
6. **`SRC-CIA-RV018-1985`**, **`SRC-CIA-LIII-1978`**, **`SRC-CIA-876-1982`**, and **`SRC-CIA-XCI`** — a small mixed set of worked, null, low-correlation, and unusual tasking cases.
7. **`SRC-TARG-PUTHOFF-1974`**, **`SRC-MARKS-KAMMANN-1978`**, and **`SRC-TART-PUTHOFF-TARG-1980`** — an early positive report, critique, and reply.
8. **`SRC-NRC-1988`** — the independent consensus review.
9. **`SRC-TRESSOLDI-KATZ-2023`** — a modern positive meta-analysis.
10. **`SRC-AKIN-TRESSOLDI-KATZ-2026`** — current expert-practice guidance, read as expert opinion.

This sequence makes it difficult to inherit only one camp's bibliography.

## A. Government archive and programme record

| ID | Record | Why it matters | Do not infer |
|---|---|---|---|
| `SRC-CIA-AIR-1995` | AIR evaluation commissioned by CIA | Best single public closeout document; separates laboratory anomaly from operational utility and contains opposing expert reviews | That every archive file was reviewed, every later study is covered, or every programme question is settled |
| `SRC-CRV-MANUAL-1986` | CRV Stages I–VI and glossary | Defines ideogram, sensory and dimensional data, AOL, Stage-IV structure, probing, and modeling in the documented training system | That the Matrix or signal line is an established physical mechanism |
| `SRC-CIA-CRVT-1982` | Controlled Remote Viewing Training report | Early structured-training and feedback-classification record | That training activity establishes efficacy |
| `SRC-CIA-RV018-1985` | Solar One / RV-018 | Worked CRV-era example identified as reaching Stage IV | That a single session proves accuracy or usefulness |
| `SRC-CIA-LIII-1978` | Session LIII | Explicit no-correlation and protocol-deviation case | That one failure disproves every protocol |
| `SRC-CIA-876-1982` | Session 876 | Explicit very-low-correlation case | A programme-wide miss rate |
| `SRC-CIA-XCI` | Session XCI | Coordinate-error/apparent-correlation case relevant to competing cue hypotheses | That the striking interpretation is uniquely causal |
| `SRC-CIA-CD58-1980` | Iran hostage tasking | Shows real operational tasking and “raw intelligence” boundary | Correctness, rescue impact, or validation by tasking alone |
| `SRC-CIA-SUN-STREAK-1987` | SUN STREAK session 8715 | Later programme procedure and reporting language | Continuity of performance across programme names |
| `SRC-DIA-USSR-1972` | U.S. foreign-programme assessment | Cold War collection and concern about reported Soviet work | Soviet efficacy, operational capability, or a complete primary Soviet record |
| `SRC-CIA-PAT-1975` | SRI final contractor research report | What the investigators did, reported, and claimed to the sponsor | Independent confirmation or a complete programme-wide success rate |
| `SRC-CIA-DAT-1995` | SAIC-era theoretical report | Formal decision-augmentation hypothesis and mechanism-separating predictions | An established mechanism or proof of precognition |

### Archive reconstruction priorities

The CIA Reading Room contains a much larger, uneven collection than this first index. A later Source Inventory should:

- preserve original document IDs and page order;
- distinguish tasking, transcript, summary, feedback, evaluation, correspondence, training, finance, and retrospective files;
- link files that belong to the same session;
- retain duplicate scans as provenance while identifying likely duplicates;
- record OCR confidence rather than silently repairing unclear text;
- code explicit positive, null, low-correlation, ambiguous, and unevaluated outcomes under one rule;
- record who knew the target, when feedback arrived, how judging was performed, and whether evaluation was blind;
- avoid extracting only famous stories.

The future Library object should be a **Source Inventory referencing the archive**, not a copied dump presented as SISO-owned content.

## B. Early experimental case and published dispute

| ID | Contribution | Evidential role |
|---|---|---|
| `SRC-TARG-PUTHOFF-1974` | Reports information transfer under sensory shielding | Early positive primary experiment |
| `SRC-PUTHOFF-TARG-1976` | Extended historical and experimental case in *Proceedings of the IEEE* | Positive programme account and protocol source |
| `SRC-MARKS-KAMMANN-1978` | Failed duplication and transcript/judging-cue critique | Negative result and ordinary-artifact hypothesis |
| `SRC-TART-PUTHOFF-TARG-1980` | Response to Marks and Kammann | Proponent methodological reply |
| `SRC-SCOTT-1982` | Further critical analysis | Independent critical interpretation |

### How to use the dispute

The old debate can be converted into modern tests:

- publish cue-scrubbed and original transcripts before judging;
- construct decoys under a frozen rule;
- conceal correct-candidate position from judges and analysts;
- estimate inter-rater reliability;
- run the same locked artifacts through proponent, critic, and neutral judging rubrics;
- predefine which analysis is confirmatory;
- report every attempted trial and every candidate score.

A historical argument becomes scientifically useful when it generates controls that both sides accept before seeing the outcome.

## C. Independent and government-requested reviews

### `SRC-NRC-1988`

The National Research Council's *Enhancing Human Performance* assessed remote viewing inside a broader review of performance-enhancement claims. Its critical conclusion is an important independent counterweight to programme and proponent accounts. Because its evidence window ends before later SAIC work, it must be represented as a scoped review rather than a timeless final word.

### `SRC-CIA-AIR-1995`

The AIR review should be read as four nested products:

1. programme and evidence summary;
2. laboratory assessment;
3. operational-utility assessment;
4. paired expert analyses by Utts and Hyman.

The most important distinction is:

```text
statistical anomaly in reviewed laboratory work
    ≠ identified paranormal cause
    ≠ reliable person-level diagnosis
    ≠ specific actionable intelligence
    ≠ demonstrated decision value
```

### `SRC-UTTS-1995` and `SRC-HYMAN-1995`

Treat these as a designed disagreement. Both reviewers regarded the better SAIC results as statistically non-random in the analyses before them. Utts regarded the accumulated evidence as establishing psychic functioning; Hyman regarded that inference as premature without independent replication and stronger exclusion of alternatives. The Library should preserve the exact overlap before presenting the dispute.

## D. Current research and synthesis

| ID | Type | Appropriate use | Main caution |
|---|---|---|---|
| `SRC-TRESSOLDI-KATZ-2023` | Systematic review and meta-analysis | Source map, effect-size claims, study-universe reconstruction | Independently test dependence, heterogeneity, risk of bias, selection, and outlier choices |
| `SRC-ESCOLA-GASCON-2023` | Modern empirical study | Generate individual-difference and measurement hypotheses | Do not generalize without checking design, corrections, and replication |
| `SRC-AKIN-TRESSOLDI-KATZ-2026` | Expert consensus survey | Candidate protocol factors and disagreement map | Expert agreement is not causal evidence |

A high-value next project is an independent, machine-readable re-extraction of the 2023 review. Each effect should carry study, sample, protocol, target type, sender condition, feedback timing, scoring method, analyst flexibility, independence cluster, preregistration, missing-data rule, and risk-of-bias fields.

## E. Foreign-programme evidence boundary

`SRC-DIA-USSR-1972` matters because it documents what U.S. intelligence considered worth collecting and assessing about reported Soviet work. It is not a substitute for Soviet laboratory notebooks, complete datasets, internal evaluations, or independent replications. A later foreign-programme inventory should separate:

1. primary Soviet/Russian scientific or government records;
2. translated open-source reporting;
3. U.S. intelligence summaries and threat estimates;
4. later memoirs and practitioner histories; and
5. claims about capability from evidence that actually measures capability.

Reciprocal attention is historical evidence. It is not a two-source replication.

## F. Practitioner source

### `SRC-CENTERLANE-MANUAL-READER`

This is a convenient secondary reading surface, not an official government archive. Use it to navigate stage terminology and the externally preserved 1986 manual scan, while retaining the manual’s uncertain revision and custody history. Practitioner commentary can be valuable for operationalizing ambiguous instructions, but it must be labeled as commentary and tested rather than promoted into fact.

## Source-quality ladder

The ladder is about claim fit, not prestige alone.

| Grade | Typical source | Suitable claims |
|---|---|---|
| A | Exact primary record, full protocol/data, direct government file, preregistered replication | What occurred, what was measured, exact result under defined design |
| B | Peer-reviewed primary study or independent review with inspectable methods | Study-level or review-level conclusions with stated limits |
| C | Expert assessment, historical synthesis, practitioner manual with provenance | Interpretation, method vocabulary, hypotheses, research leads |
| D | Memoir, interview, documentary, unsourced retrospective story | Discovery lead or testimony only |
| E | Anonymous post, generated summary, repeated anecdote without a source chain | Search lead; never final evidence |

A dramatic Grade-D story does not outrank a mundane Grade-A null result.

## Rights and preservation boundary

- External government records, journal articles, and practitioner sites retain their source identity and applicable terms.
- A public locator is not a blanket permission to mirror or transform a payload.
- The first module stores titles, IDs, dates, source roles, bounded summaries, and links.
- Any future corpus import requires document-level provenance, rights classification, integrity receipts, OCR lineage, and a deletion/correction mechanism.
- Quotations should be short and necessary. Original synthesis is preferred.

## Known gaps in this first map

- complete programme-name and agency-transfer chronology;
- complete session-level archive inventory;
- exact budget receipts by programme and year;
- Soviet and other non-U.S. primary-source programmes;
- page-level manual revision lineage;
- trial-level reconstruction of the SRI, SAIC, and later experimental datasets;
- independent risk-of-bias and dependence coding for the 2023 meta-analysis;
- registered replications after the 1995 review;
- prospective operational decision-value trials;
- complete rights and preservation review for every linked payload.

These are explicit research queues, not invitations to fill gaps with confident inference.
