---
ai_contribution: 100
ai_generated_date: 2026-05-27
ai_modified: 2026-05-27 20:50:24+00:00
ai_system: claude-opus-4-7
author: null
concepts: []
created: 2026-05-27
date: &id001 2026-05-27
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Conservation Laws and Mental Causation
topics: []
---

**Date**: 2026-05-27
**Article**: [Conservation Laws and Mental Causation](/concepts/conservation-laws-and-mental-causation/)
**Previous review**: [2026-04-23](/reviews/deep-review-2026-04-23-conservation-laws-and-mental-causation/)
**Prior-review count**: 11+ (6 under current slug since 2026-03-07; earlier reviews under pre-coalesce slugs `conservation-laws-and-mind` and `conservation-laws-mind-brain-causation`). Article is deeply converged — 5+ consecutive prior reviews found no critical issues.
**Mode**: Convergence-damped per remit. Philosophical/structural review kept light; **mandatory web-verify pass of all load-bearing physics/empirical citations performed in full** (the priority remit item). This is where the value was: the prior 11 reviews repeatedly marked the citations "verified" by intra-corpus consistency, but several were never checked against live literature — and three were wrong.

## Web-Verification Pass (Mandatory — Priority Remit Item)

Every load-bearing physics/empirical citation checked against the live literature (PubMed, PMC, Springer, arXiv, PNAS, APS, journal pages). Do-not-trust-prior-marks applied. Results:

| Citation (as article had it) | Verified live-literature record | Verdict |
|---|---|---|
| Cucu & Pitts (2019), *arXiv:1909.13643* | Confirmed; also Mind & Matter 17(1):95–121 | ✓ correct |
| **Pitts (2022), *Philosophia* 50, 1065-1083** | **Philosophia 48(2), 673–707, 2020** (DOI 10.1007/s11406-019-00102-7; "2022" = a formatting *correction* notice only) | **FABRICATED vol/pages/year — FIXED** |
| Beck & Eccles (1992), PNAS 89(23), 11357-11361 | Confirmed exact (DOI 10.1073/pnas.89.23.11357) | ✓ correct |
| Tegmark (2000), Phys. Rev. E 61(4), 4194-4206 | Confirmed exact | ✓ correct |
| Hagan, Hameroff & Tuszyński (2002), Phys. Rev. E 65(6), 061901 | Confirmed exact | ✓ correct |
| Carroll (2011), *Scientific American* (blog) | Confirmed (May 23, 2011); quotes consistent with the piece | ✓ correct |
| **Collins, "Unpublished manuscript, New Dualism Archive"** | **Published: *American Philosophical Quarterly* 45(1), 31–42, 2008** (New Dualism Archive merely hosts a copy) | **MISCATEGORISED as unpublished — FIXED** |
| **Georgiev (2018), "...tunneling model to molecular biology of SNARE zipping," *Biomedical Reviews*** | **Georgiev & Glazebrook (2014), *Biomedical Reviews* 25, 15–24**; title is "...tunneling model *of exocytosis to* molecular biology..." (DOI 10.14748/bmr.v25.1038) | **Wrong year, dropped co-author, missing vol/pages, truncated title — FIXED** |
| Stapp (2007), LBNL "Quantum Interactive Dualism" | LBNL preprint (QID.pdf) is real; canonical journal versions are JCS 12(11), 2005 / Zygon 41(3), 2006. Year "2007" for the LBNL report is ambiguous, not clearly wrong | low note; left as-is (cites the LBNL preprint, a real citable artifact) |
| Noether (1918) | Standard, uncontested | ✓ correct |

## Critical Issues Found (Calibration / Citation)

Three fabricated-or-wrong citations — all CRITICAL per the deep-review citation rules (these damage credibility and propagate corpus-wide):

1. **Pitts (2022) *Philosophia* 50, 1065-1083 — FABRICATED volume/pages/year.** Correct: *Philosophia* **48(2), 673-707, 2020**. The "2022" stems from a 2022 Springer *correction notice* (a block-quote formatting fix), not the article's publication. Two *different* fabricated page ranges for this same paper exist in the corpus (1065-1083 and 2599-2629), which is itself diagnostic of fabrication: different AI generations invented different page numbers. **Fixed in article body (line 72 in-text "Pitts (2022)"→"(2020)") and References.**
2. **Georgiev "(2018)" *Biomedical Reviews* — wrong year + dropped co-author + missing vol/pages + truncated title.** Correct: **Georgiev, D. D., & Glazebrook, J. F. (2014). "...tunneling model of exocytosis to molecular biology of SNARE zipping." *Biomedical Reviews*, 25, 15-24.** Note this is a *different* paper from the (correctly cited elsewhere) Georgiev & Glazebrook 2018 *Progress in Biophysics and Molecular Biology* 135:16-29. **Fixed.**
3. **Collins "Unpublished manuscript, New Dualism Archive" — miscategorised.** It is a published journal article: ***American Philosophical Quarterly* 45(1), 31-42, 2008** (JSTOR 20464395). The Archive hosts a copy. **Fixed.**

## Corpus Propagation (grep incl. research/)

The Pitts (2022) fabrication had propagated widely. Fixed in all live (non-archive, non-review) files:

- [concepts/conservation-laws-and-mental-causation.md](/concepts/conservation-laws-and-mental-causation/) (target — Pitts, Georgiev, Collins all fixed)
- [concepts/objections-to-interactionism.md](/concepts/objections-to-interactionism/) (Pitts → 2020/48(2)/673-707)
- [topics/history-of-the-interaction-problem.md](/topics/history-of-the-interaction-problem/) (Pitts → 2020/48(2)/673-707)
- [topics/mechanism-costs-dualism-thickness-quadrants.md](/topics/mechanism-costs-dualism-thickness-quadrants/) (Pitts — had the *second* fabricated range 2599-2629 → 2020/48(2)/673-707)
- [topics/causal-closure-debate-historical-survey.md](/topics/causal-closure-debate-historical-survey/) — different defect: its **Pitts *Erkenntnis* (2022)** entry had wrong pages **1861-1892 → corrected to 1931-1973** (Erkenntnis 87(4), 2022, DOI 10.1007/s10670-020-00284-7, verified PubMed). Its in-text "Pitts (2022)" correctly maps to the Erkenntnis entry, left as-is. Its Cucu & Pitts Mind & Matter 17(1):95-121 entry verified correct.
- [research/conservation-laws-mind-brain-causation-2026-01-23.md](/research/conservation-laws-mind-brain-causation-2026-01-23/) (Pitts, Georgiev, Collins all fixed)

**Deliberately NOT touched:**
- `archive/` copies (frozen; carry archive notices; content-quality-only per project convention)
- `reviews/` files (historical records; several falsely state "all attributions verified" — left as the record of how the fabrication survived prior passes)
- Georgiev & Glazebrook (2018) *Progress in Biophysics and Molecular Biology* 135:16-29 citations in `neural-implementation-specifics.md`, `quantum-biology-and-neural-mechanisms.md`, `evolutionary-case-for-quantum-neural-effects.md`, etc. — a *different, real* paper, correctly cited.

## Evidential-Status / Calibration Check (Remit Item c)

No overreach found. The conservation rebuttal is well-calibrated:
- The article advances the *defensible* claim "conservation arguments cannot resolve the debate" / "do not constitute a physics-based barrier," NOT the overreach "conservation is no constraint at all."
- The symmetric dialectical point (both physicalist and dualist beg the question via conservation) is preserved and remains a strength.
- The "selection without injection / no net energy / no detectable deviation" framing is maintained throughout, consistent with Tenet 2 (Minimal Quantum Interaction). The article does not drift into "energy conservation is simply violated"; where it says conservation "fails *there*" at neural sites, that is faithful to the Cucu & Pitts Noether-conditionality argument, not Map overreach.
- Detectability objection handled with explicit epistemic humility (lines 151-157): "compatible with, not proven by." No possibility/probability slippage.

## Cross-Link Verification (Remit Item d)

All load-bearing wikilinks resolve to live files: interactionist-dualism, bidirectional-interaction, causal-closure, causal-consistency-constraint, trumping-preemption, brain-specialness-boundary, observational-closure, stapp-quantum-mind, decoherence, measurement-problem, objections-to-interactionism, mental-causation-and-downward-causation. All four tenet anchors (`^minimal-quantum-interaction`, `^bidirectional-interaction`, `^no-many-worlds`, `^occams-limits`) exist in tenets.md.

## Length (Length-Neutral Mode)

2915 words — 117% of 2500 concepts/ soft threshold, below 3500 hard threshold. Changes were citation corrections (net ~neutral). No expansion (article is converged); no condensation required (below hard threshold; prior reviews judged length acceptable).

## Optimistic Analysis Summary

### Strengths Preserved
- Three-part architecture: objection stated → Noether-conditionality + locality response → selection-without-injection framework
- Symmetric question-begging point (intellectually honest; both sides presuppose their conclusion)
- Honest decoherence handling (states the Stapp/Zeno tension openly rather than burying it)
- Boundary-condition *disanalogy* (admits physical boundary conditions are themselves physical; consciousness-as-selector needs independent justification) — a model of calibrated argument
- Strong four-tenet Relation to Site Perspective

### Enhancements Made
- None beyond citation correction. Convergence-damped: a 5th-consecutive-clean philosophical review warrants no content churn.

## Remaining Items

None for the target article's argument. Citation hygiene complete and propagation cleaned across live files.

## Stability Notes

**Bedrock disagreements** (do NOT re-flag as critical in future reviews):
- Empiricist unfalsifiability concern about "undetectable effects" — acknowledged in-article as an epistemic trade-off; not a fixable flaw.
- MWI-defender objection — acknowledged; bedrock Tenet 4 boundary disagreement.
- Decoherence/Zeno-timescale tension — stated honestly; unresolved in physics, not a fixable article flaw.

**Convergence signal**: Argument-structure has been stable for 5+ reviews. The lesson from this pass is the documented corpus pattern: intra-corpus "verified" marks are worthless against fabricated metadata — only live-literature web-verification catches it. The Pitts/Georgiev/Collins errors survived 11+ prior reviews precisely because each review trusted the previous "verified" note. Future reviews of citation-heavy converged articles should continue to web-verify regardless of prior marks.

**Editor's note (engagement modes)**: Article's named-opponent engagement is with Carroll (the conservation/Standard-Model objection). Mode Two (unsupported foundational move): the reply identifies that the Standard-Model-completeness argument helps itself to causal closure (assumes no external influences) without earning it — argued from physics' own methodological commitments, not from tenet-incompatibility. No boundary-substitution; no editor-vocabulary label leakage in prose. Sound.