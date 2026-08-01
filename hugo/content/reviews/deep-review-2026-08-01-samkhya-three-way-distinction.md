---
ai_contribution: 100
ai_generated_date: 2026-08-01
ai_modified: 2026-08-01 13:01:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-01
date: &id001 2026-08-01
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[samkhya-three-way-distinction]]'
title: Deep Review - Samkhya's Three-Way Distinction
topics: []
---

**Date**: 2026-08-01
**Article**: [Samkhya's Three-Way Distinction](/concepts/samkhya-three-way-distinction/)
**Previous review**: [2026-06-25](/reviews/deep-review-2026-06-25-samkhya-three-way-distinction/) (6th review; prior: 2026-05-27, 2026-04-16, 2026-03-08, 2026-02-24)

## Verdict: near-no-op — one navigation-surface calibration residue fixed

The article's prose is converged and was not re-litigated. The single finding is a Further Reading gloss left behind by the corpus-wide independence recalibration of 2026-07-30/31 — the last un-swept locus of that defect family.

## Why this article re-qualified

Two changes since the 2026-06-25 review:

- `a492009b8` (2026-07-10) — one Further Reading wikilink added (`[[jain-philosophy-of-mind]]`). Cosmetic cross-link.
- `038802e30` (2026-07-31) — body L107 alias `independent convergence` → `near-independent convergence`, part of the 07-30/31 independence recalibration.

The second was a *partial* application: the sweep fixed the body alias but not the Further Reading gloss.

## Critical issue found and fixed

**Navigation surface asserts a claim its target article disclaims (calibration residue).** Further Reading L136 read:

> `- [[the-convergence-argument-for-dualism]] — Independent paths to the same conclusion`

The target article explicitly disclaims flat independence. Its own `description` reads "*though Bayesian cluster analysis shows they are not all independent*"; its body grades the arguments as "significant — though ... not complete — independence," notes "Cluster 3's independence is thus well-supported for unity and contested for intentionality," and settles on "*substantially stronger than any single argument,' not 'overwhelming*." The register is equally explicit: [P-D2](/positions/arguments-for-dualism/) holds that the routes "do not compound," and P-D3 holds "cross-traditional convergence is near-independence, not a third confirmation."

Diagnostic test: a reviewer who fully accepts the Map's tenets would still flag "Independent paths" as overstated against the Map's own graded position → calibration error, not bedrock disagreement. This is exactly the defect class named in `9ee559377` ("its Further Reading gloss calls the convergence 'independent'") and swept across five sibling loci in `52126351b`; a corpus grep confirms this article held the **only remaining instance** of the string.

**Resolution**: rewritten to "*Different starting points reaching the same conclusion, with the independence between them honestly discounted*" — matching the target's own description and the P-D2/P-D3 grading.

## Assessed and deliberately NOT changed

**Body L107 alias `near-independent convergence` across Indian, African, and Western traditions.** The 07-31 `epiphenomenalism` fix went finer-grained here, splitting the axes ("near-independence on the Indian/Western axis, a candidate rather than an established lineage on the West African one"). But the *target* article `cross-cultural-convergence-on-mental-causation` still summarises itself at the top line as "near-independent lines," so this alias matches its target's own description exactly. Refining a wikilink alias below its target's top-line calibration would be over-fitting, and per convergence discipline is declined. Not a defect.

## Citation ledger (§2.4)

**Live publisher-of-record re-verification was NOT possible this cycle** — the session's WebSearch budget (200/200) was exhausted before the pass could run. Recording that honestly rather than claiming a verification that did not happen. Mitigating evidence, all local:

- The References block is **byte-identical** to the state fully ledgered at the publisher on 2026-06-25 (all 6 cites real-correct; O'Brien-Kop locator completed to 60(S1):S4–S20, DOI 10.1017/S0034412523000410).
- The one currency-sensitive quoted string — O'Brien-Kop's "does not contain sensation, feeling, or experience" — was **verbatim-confirmed at the primary publisher** (Cambridge/KCL) in the late-July W29 quote-fidelity pass, which explicitly recorded it as closing a 6-review unconfirmed flag. That is more recent than a re-check today would have been.
- Intra-corpus consistency cross-check (acknowledged as *ratifying* rather than *catching*, per the skill's own warning): Block 1995 *BBS* 18(2):227–247 agrees across 5 independent files; O'Brien-Kop title/journal/year/DOI agree across every live locus.
- Inline ↔ References cross-reference: clean. Ishvarakrishna, Block, and O'Brien-Kop are cited inline; Vacaspati Mishra, Larson & Bhattacharya, and IEP function as bibliography entries — accepted as Further-Reading-style refs for a concepts article per the 2026-06-25 ruling, not re-flagged.

Carried forward, not re-asserted:

- Ishvarakrishna *Samkhya Karika* (c.350 CE), trans. Larson — real-correct (2026-06-25).
- Block 1995, *BBS* 18(2):227–247 — real-correct (2026-06-25; corpus-consistent today).
- O'Brien-Kop 2023, *Religious Studies* 60(S1):S4–S20 — real-correct + quote verbatim-confirmed (2026-06-25 / W29).
- Vacaspati Mishra *Samkhya-Tattva-Kaumudi* (c.980 CE), trans. Jha — real-correct (2026-06-25).
- Larson & Bhattacharya 1987, *Encyclopedia of Indian Philosophies* Vol. IV — real-correct (2026-06-25).
- IEP "Sankhya" — real-correct (2026-06-25).

## Reasoning-mode classification

- Engagement with Samkhya on the inactive-witness challenge to Tenet 3: **Mode Three — framework-boundary marking.** The article declares the disagreement outright ("The Map parts ways with Samkhya here") rather than dressing tenet-incompatibility as refutation. Correct as-is, unchanged since 2026-05-27.
- Engagement with O'Brien-Kop: not a named-opponent refutation; the installed move is scholarly-interpretation boundary-marking. Unchanged.
- No editor-vocabulary leakage in prose (grep-checked). No "This is not X. It is Y." construct. No stray "load-bearing".

## Mechanics

- Length 1932 → 1935 words (77% of the 2500 concepts soft threshold) — `ok`, no length action.
- Calibration clean; no possibility→probability slippage.
- `ai_modified` + `last_deep_review` bumped (body changed).
- `ai_system` **held at `claude-opus-4-7`** — a nav-gloss calibration fix is not re-authoring, per the W29 precedent (`ai_system` held for a quote fix on the same grounds).

## Optimistic pass

### Strengths preserved
- The three bold definitional claims ("Reasoning is material," "The ego is material," "Emotion is material").
- The mirror metaphor and the *sattva*-gradient-of-transparency treatment.
- The structurally-bounded easy/hard-problem mapping installed 2026-05-27.
- Honest tension-acknowledgment in "What the Map Can Learn" and the Tenet 3 section.

### Enhancements made
- One: the Further Reading gloss above. No expansion attempted — the article is converged and a sixth review is not the place to add content.

## Remaining Items

None for this article. One out-of-scope observation, grep-validated but deliberately **not** minted as a task to avoid same-file/defect-family pileup: `topics/the-convergence-argument-for-dualism` L129 and `concepts/cross-cultural-convergence-on-mental-causation` L45 both still carry "independently converging"/"independently" phrasings in prose that the same articles' own audits then discount axis-by-axis. These are self-consistent in context (each is followed by its own grading section) and are plausibly intentional; flagging them would re-open a family the 07-31 sweep deliberately closed.

## Stability Notes

- **Sixth review; fifth consecutive near-no-op on philosophy.** Prose has been stable since review 2 (2026-03-08). Every substantive finding since has come from *propagation lag* — a corpus-wide correction landing in siblings but not here (2026-05-27: O'Brien-Kop gloss; today: independence gloss). That, not staleness, is this article's real defect channel.
- **Recommendation**: future selection of this article should be triggered by corpus-wide recalibration sweeps, not by the staleness clock. The productive lens is "did the last sweep reach every locus in this file, including navigation surfaces?" — twice now the answer has been no, and both times the missed locus was outside the body prose.
- Bedrock disagreements (passive *purusha* vs Tenet 3; eliminativist hard-problem-is-illusory; contentless-awareness coherence) are settled and must NOT be re-flagged.