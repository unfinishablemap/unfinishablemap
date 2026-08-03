---
title: "Apex Evolve Review — The Contemplative Path"
created: 2026-08-03
modified: 2026-08-03
human_modified: null
ai_modified: 2026-08-03T20:00:07+00:00
draft: false
description: "Apex-evolve review archive: two new Eastern sources admitted (Kyoto School as a counter-line, Yogacara as internal support), Metzinger's SMT installed as the named rival to the witness argument, corpus-wide illusionist recalibration absorbed, Evidence and Dependency retrofitted, 4201 to 3999 words."
topics: []
concepts: []
related_articles:
  - "[[apex/contemplative-path]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-08-03
last_curated: null
---

# Apex Evolve Review — The Contemplative Path

**Article**: `obsidian/apex/contemplative-path.md`
**Effective baseline before this run**: 2026-07-06 (`last_deep_review`); `apex_last_synthesis` was 2026-06-25
**Selected because**: highest staleness score among *actionable* apex candidates — 28 days since effective baseline x 7 of 7 sources modified since = 189.

## Selection Audit

The raw scorer's top two candidates were both rejected on inspection, and the rejection reasons matter more than the scores:

1. **`phenomenal-variation-within-a-species` (198)** — declined. Three refine-draft commits on 2026-08-01/02 (`56e22ac71`, `24744f664`, `bb2831f0a`) had already reconciled it against exactly the source changes the scorer was counting: the source-attribution defects corrected in `topics/source-attribution-divergence` on 08-02, the synaesthetic-class paragraph versus the predictive-processing concession, and the alexithymia fifth-class integration. Picking it would have re-run absorbed work. This is the same failure mode the Step 1 `max(apex_last_synthesis, last_deep_review)` fix guards against, one level out: a targeted *refine* can absorb source drift just as a deep-review can, and the scorer sees neither.
2. **`phenomenal-output-causal-machinery-dissociation` (140)** — declined, **hard block**. It is genuinely the most drifted apex by body-edit recency (no body edit since 2026-07-14) and at 6904 words is over the apex *critical* threshold of 6500. But todo.md L1392 carries a standing `#veto`: "Do NOT re-queue for condense; un-veto only after the human split decision." A prior structural condense was a near-no-op (6990 to 6989w) because every paragraph carries distinct citations or calibration language. Integrating 7 changed sources into it would have pushed it further over critical against an explicit human-decision hold. Left untouched; the veto stands.

`contemplative-path` was then the top actionable candidate and is genuinely due: 28 days, every one of its 7 sources modified, and no `## Evidence and Dependency` section.

## Changed Sources (7 of 7)

| Source | Modified | What changed that mattered |
|---|---|---|
| `topics/eastern-philosophy-consciousness` | 08-03 | Two new sibling articles landed (Yogacara storehouse consciousness; Kyoto School). Illusionist regress recalibrated: bare regress "proves nothing", pressure relocated. |
| `topics/aesthetics-and-consciousness` | 08-02 | Five arguments audited down to **three premises**, "only the last stands clear"; "concentration, not tally". |
| `concepts/introspection` | 07-31 | Frankish restriction installed; relocation move stated precisely ("gains only if the second question is tractable"). |
| `topics/contemplative-practice-as-philosophical-evidence` | 07-31 | Fox et al. 2012 neural-prediction over-claim corrected (already propagated here by `af82cbe8a`). |
| `concepts/witness-consciousness` | 07-30 | New Further Reading entry: Metzinger's SMT as "the naturalist no-self rival: the witness read as a still-representational model of tonic alertness". |
| `topics/epistemic-advantages-of-dualism` | 07-30 | "Minimal datum survives on illusionism's own terms" — careful vs careless statement. |
| `concepts/meditation-and-consciousness-modes` | 07-25 | Bidirectional calibration: meditation plasticity is *evidence shared with physical learning*, constraining rather than establishing. |

Verified that the two corpus sweeps which touched this file (`52d78a23f` illusionism restriction, `e94f82da3` aesthetics premise count) had landed in **both** obsidian and hugo trees. They had.

## Pessimistic Review

**Clarity Critic.** The aesthetics section still argued the *old* five-spoke shape while its own sentence conceded "three premises rather than five" — the concession was bolted onto a paragraph that then listed five spokes anyway. The reader could not see which three. Rewritten to name the three premises (constitutive holism, the structure-experience gap, the causal argument from creation) with the two-grain point folded into the first.

**Redundancy Hunter.** Substantial. The contemplative traditions were enumerated three separate times (witness section, two-modes section, illusionist convergence); the explanatory-gap point was made four times; "intensifies rather than dissolves" appeared three times in the aesthetics section alone; the process/content distinction occupied two paragraphs saying the same thing; the Lutz-studies calibration restated its own summary; the moral-architecture cross-link paragraph had grown to ~190 words of hub accretion for one structural point.

**Narrative Flow Analyst.** The Eastern Philosophy section ended on a note of settled synthesis ("yields a sophisticated position") immediately before the Illusionist Challenge, with no acknowledgement that any Eastern tradition might *disagree* with the Map — which made the convergence argument three sections later look unearned.

## Optimistic Review

**Connection Finder.** Two clear openings from the changed sources:
- **Yogacara** (`concepts/yogacara-alaya-vijnana-storehouse-consciousness`) supplies a Buddhist-internal continuity mechanism — karmic seeds in a flowing substrate, continuity without a permanent thing. This does real work the flame analogy was carrying alone: it shows the Map is not smuggling a substance where Buddhism forbade one. It also has a clean limit — the storehouse individuates causally, not primitively, so it does *not* supply thisness. Installed with both halves.
- **Metzinger's SMT** (`concepts/self-model-theory-of-subjectivity`) was the missing named rival. The witness section asserted the subject-object structure as "phenomenological support for the Map's dualism" with no opponent in view, which is exactly the shape of claim the corpus has been recalibrating everywhere else.

**Synthesis Strengthener.** The **Kyoto School** is the strongest addition and it runs *against* the article. Nishida's pure experience is prior to the subject-object division; if right, the witness structure this piece treats as basement fact is a derived articulation. Installed as a counter-line, explicitly excluded from the convergence tally, and logged in the Evidence and Dependency ledger as the one externally-sourced line cutting the other way. The convergence-problem response was amended to match ("convergence on what is found, not on what it means").

**Human Reader Advocate.** Cut three enumerations to one, merged the two-paragraph process/content point, and removed the redundant second analogy in the training paragraph.

## Length Assessment

| Stage | Words |
|---|---|
| Before | 4,201 (over the 4,000 apex soft threshold) |
| After additions only (E&D + Kyoto + Yogacara + SMT + illusionist recalibration) | 4,722 |
| After condensation | **3,999** (status `ok`) |

Net: ~530 words of new content absorbed and ~725 words of redundancy removed. Every hedge, citation-framing qualifier, and evidential-status caveat was preserved through the condensation — the cuts were enumerations, restated summaries, and doubled analogies, not calibration.

## Evidence and Dependency (retrofit)

Installed; the article previously had none (10 of 40 apex articles now carry one). Classification made:

- **Externally evidenced**: two-mode neural contrast, jhana imaging, lucid-dreaming signatures, Petitmengin prodrome result, Fox trainability finding.
- **Independently argued**: cross-tradition structural convergence (needs only a historical claim about mutual non-influence).
- **Inherited from tenets**: correlation-without-explanation as ontological boundary (T1, T5); neuroplasticity as downward causation (T3, and the article now concedes the evidence does not discriminate); the quantum Zeno gloss (T2, no independent weight).
- **Inherited from another synthesis / mutually coherent only**: process haecceitism, imported from `apex/identity-across-transformations`, asserted by no contemplative tradition.
- **Counted against**: the Kyoto reading.

## Changes Applied

1. Aesthetics paragraph restructured to the source's corrected three-premise audit.
2. Metzinger SMT installed as named rival in the witness section; dualism inference calibrated to "the structural datum is robust; what it licenses is contested".
3. Yogacara paragraph merged into the haecceity treatment (support plus its limit).
4. Kyoto School paragraph added as a counter-line; convergence-problem response amended.
5. Illusionist regress: relocation move stated positively. Training response retitled "Training refines rather than dissolves", marked as the independent load-bearer, with the illusionist's quasi-phenomenal-fidelity reply conceded.
6. Tenet 3 paragraph given the shared-with-physical-learning discriminator from `meditation-and-consciousness-modes`.
7. `## Evidence and Dependency` installed.
8. ~30 condensation edits across every section.
9. Frontmatter: `apex_sources` 7 to 9, three `related_articles` added, `ai_system` appended to `claude-opus-4-7+claude-opus-5`, `ai_modified` and `apex_last_synthesis` bumped.

## Not Done / Flagged

- **`phenomenal-output-causal-machinery-dissociation` remains the corpus's most drifted apex** (no body edit since 07-14, 6,904 words, over critical) and remains human-blocked. Its `#veto` note proposes extracting "The Strongest Materialist Reading" plus "Independent Traditions on the Same Architecture" into a companion piece. That decision is still owed.
- The phrase "This apex article synthesizes:" survives here and in 9 other apex articles despite the media-neutral rule. Corpus-wide, out of scope for this run.
- `apex_last_synthesis` drift is real across the tree (this article's was 11 days behind its `last_deep_review`), but the stale field is a known harmless artifact and was not retro-reconciled elsewhere.

## Quote and Citation Check

- Nishida "just as it is without the least addition of deliberative discrimination" — grep-verified verbatim against `topics/japanese-philosophy-of-mind-kyoto-school.md`, which attributes it to Nishida 1911/1990.
- Metzinger 2020 — reused from the SMT article's already-verified reference list (*Philosophy and the Mind Sciences* 1(I), 1-44); "tonic alertness" is the paper's own term, appearing in its title.
- Murdoch and Weil quotes preserved verbatim from the prior revision; no new attribution introduced.
- No citation was deleted during condensation.
