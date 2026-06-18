---
ai_contribution: 100
ai_generated_date: 2026-06-18
ai_modified: 2026-06-18 00:00:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-18
date: &id001 2026-06-18
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Predictive Processing
topics: []
---

**Date**: 2026-06-18
**Article**: [Predictive Processing](/concepts/predictive-processing/)
**Previous review**: [2026-06-01](/reviews/deep-review-2026-06-01-predictive-processing/)

## Review Context

Eighth deep review. Changed-since-review trigger: `ai_modified` 2026-06-16 > `last_deep_review` 2026-06-01 (own-content drift, not a cross-touch artifact). Two 06-16 commits post-dated the 06-01 deep-review and added/altered citation-bearing prose:

- **4dd81b148** ("Engage IWMT as a named materialist rival", Gemini outer-review refine): added the new section **"The Strongest Gap-Dissolving Variant: Integrated World Modeling Theory"** (Safron IWMT + Assran I-JEPA + LeCun JEPA), added Safron 2020 and Assran 2023 to References, and condensed the Process Philosophy and Contemplative Evidence sections (net trim there).
- **ed1d12ca7** (I-JEPA attribution fix): reframed the I-JEPA "world-model" claim.

The new prose and its two new citations were UNVERIFIED at the 06-01 review, so this pass web-verified them at the publisher of record. Verdict: **converged — metadata-only no-op.** No body edits applied; only `last_deep_review` bumped (the article remains at the hard ceiling, so any net addition was disallowed and none was warranted).

## Pessimistic Analysis Summary

### Critical Issues Found

None.

### Publisher-of-Record Citation Web-Verify (the new 2026-06-16 content)

Per-cite ledger (the three items the brief flagged as highest-risk, plus the inline attributions the new prose rests on):

- **Safron, A. (2020). IWMT of Consciousness. *Frontiers in Artificial Intelligence*, 3, 30. doi:10.3389/frai.2020.00030** — state: **real-correct**. Title, journal (*Frontiers in Artificial Intelligence*), year, volume 3, article 30, DOI all verified against the Frontiers DOI landing page and PMC (PMC7861340). The article's characterization ("conscious if and only if it generates a body-centred world-model with spatial, temporal, and causal coherence") faithfully matches the source ("consciousness is what integrated world-modeling is like… coherence with respect to space, time, and cause for systems and their relationships with their environments"). Author Adam Safron correct.
- **Assran, M., Duval, Q., Misra, I., Bojanowski, P., Vincent, P., Rabbat, M., LeCun, Y., & Ballas, N. (2023). "Self-Supervised Learning From Images With a Joint-Embedding Predictive Architecture." *CVPR 2023*** — state: **real-correct**. Title exact, CVPR 2023, arXiv 2301.08243. Full eight-author list verified against the CVF open-access page and Meta AI publication page (order and surnames all match). LeCun is indeed a listed author.
- **LeCun JEPA "world model" framing** (inline, no formal citation) — **real-correct**. LeCun's 2022 position paper "A Path Towards Autonomous Machine Intelligence" (v0.9.2, 2022-06-27) proposes a "configurable predictive world model" and introduces JEPA; Meta's own I-JEPA blog is titled "the first AI model based on Yann LeCun's vision." The article's "an instance of the broader JEPA programme LeCun frames as building a 'world model'" is faithfully attributed.
- **Hutto & Myin, *Radicalizing Enactivism: Basic Minds without Content* — Hard Problem of Content** (inline; carried by the `[[hard-problem-of-content]]` cross-link, no References entry, which is acceptable) — **real-correct**. Verified canonical source of the "covariance doesn't constitute content" / Hard Problem of Content argument. Article's framing ("Covariation yields causal-statistical facts; aboutness, correctness conditions… are normative facts the underlying machinery does not supply") matches the source. NOTE: this content entered 04-26/04-27 (commits e32ab2d8b, 438c601a9), predating the 06-16 changes, and was already covered at the 06-01 review; re-verified here for completeness.
- **Ramsey-Stich-Garon connectionist challenge to folk psychology** (inline) — **real-correct** (well-established connectionist-eliminativism reference; entered 04-26, pre-dates 06-16, previously reviewed).
- **Churchland eliminativism** (inline) — **real-correct** (well-established).

Also retained/unchanged and verified exact at the 06-01 review (not re-litigated): Clark/Friston/Wilkinson "Bayesing Qualia" 2019 (26(9-10), 19-33); Demirel et al. 2025 *J. Neuroscience* 45(20); standard Clark/Hohwy/Seth/Friston/Solms/Whitehead/Frankish citations.

**No fabricated cites. No wrong metadata. No orphan inline↔References mismatches in the new content.** Empirical-currency sweep: the new prose makes no superlative empirical claims requiring a record-currency check (the find_superlative_claims helper is irrelevant here — the IWMT/I-JEPA prose is theoretical, not empirical-record).

### I-JEPA Attribution Fix Audit (task item c) — VERIFIED ACCURATE

The fix (ed1d12ca7) changed "its authors describe the predictor as a 'primitive world-model'" → "an instance of the broader JEPA programme LeCun frames as building a 'world model'."

Finding of note: the *original* attribution was, in fact, **also accurate** — the I-JEPA team does describe the predictor as a "primitive (and restricted) world-model" (Meta's official I-JEPA blog and the facebookresearch/ijepa GitHub README). So this was a conservative-rewording fix, not a fabrication-removal; both the old and new formulations are faithful to the literature. The **current text is correct and well-supported.** No further action.

### Boundary-Disagreement Integrity (task item b) — PASS

The IWMT engagement ("The Strongest Gap-Dissolving Variant") stays a framework-boundary disagreement, not an in-framework refutation:

- "The Map declines to conscript this framework. IWMT relocates the gap rather than closing it—the standard explanatory-gap reply applies to a MAP estimate exactly as it applies to any other functional state." — correct gap-RELOCATION (not gap-closure), consistent with `[[direct-refutation-discipline]]` Mode-Three honesty.
- "the disagreement reaches the framework boundary: the claim that the right generative architecture *is* experience runs counter to the Map's [Dualism](/tenets/#dualism) commitment, and is marked as a boundary disagreement rather than a refutation inside IWMT's own terms." — explicitly self-marks as boundary disagreement; no overclaim.
- "What IWMT offers is the best available account of the world-model consciousness uses; it does not deliver the consciousness that uses it." — concedes IWMT's genuine strength, declines only the identity claim.

No possibility/probability slippage: the section deploys no evidential-tier label and does not treat tenet-coherence as upgrading any empirical claim. A tenet-accepting reviewer would not flag the IWMT engagement as overstated.

### Reasoning-Mode / Label-Leakage Check (§2.6) — PASS

Grep for editor-vocabulary (`direct-refutation`, `unsupported-jump`, `bedrock-perimeter`, `mode-mixed`, `Engagement classification:`, `**Evidential status:**`, `tenet-register`) returned zero hits. The IWMT engagement is natural journal prose. Engagement mode (editor-internal): Mode-Three (framework-boundary marking) for IWMT's identity claim, correctly executed — IWMT presses a sufficiency claim that meets the explanatory gap; the Map honestly marks the residue as bedrock with Dualism rather than dressing tenet-incompatibility as an in-IWMT-terms refutation.

## Optimistic Analysis Summary

### Strengths Preserved

- New IWMT section is a genuine asset: it engages the strongest gap-DISSOLVING (not merely gap-bracketing) PP variant, gives it computational teeth (I-JEPA/JEPA), and declines it cleanly via the Mary/explanatory-gap reply. Strengthens the AI/qualia cluster.
- The 06-16 condensation of Process Philosophy and Contemplative Evidence tightened prose without losing the Whiteheadian or contemplative substance — a good length-aware refine.
- Front-loaded opening, four-part illusionist challenge, five-tenet coverage, and 5-point falsifiability section all preserved (carried from prior reviews).

### Enhancements Made

None — converged article, no-op review. No content edits applied (see Stability Notes).

### Cross-links Added

None. All wikilinks in the new content verified to resolve: `[[tenets]]`, `[[tenets#^dualism]]` (block-anchor present at tenets.md:48), `[[explanatory-gap]]`, `[[hard-problem-of-consciousness]]`, `[[hard-problem-of-content]]`, `[[content-vocabulary-as-derived-feature]]` all present.

## Remaining Items

- **Length (real, active violation):** 3606 words = 106% of the 3500 concepts/ HARD ceiling (well below the 5000 critical ceiling). Grew from 3256 at the 06-01 review; the 06-16 IWMT addition (~330 words) outweighed the Process/Contemplative trims. The 06-01 review pre-flagged "If it crosses 3500 (hard), a `/condense` is warranted" — that threshold is now crossed. No condense applied here per the task brief's explicit preference for a verify-only pass and its warning against churning freshly-calibrated converged prose: the IWMT calibration was installed only 2 days ago and is load-bearing; the genuinely-redundant trim candidates (Honest Assessments, Access vs Phenomenal) are small and carry distinct framing. **Queue a dedicated `/condense` (P2) to bring it back under 3500 by trimming genuine redundancy, NOT by stripping the IWMT/HPoC calibration.**

## Stability Notes

Eighth review; article remains at convergence on content. The new 06-16 IWMT/I-JEPA/LeCun citations are now web-verified exact at the publisher of record — high confidence in attribution integrity across the whole article. The I-JEPA attribution fix is confirmed accurate (and the pre-fix version was also accurate).

Do NOT re-flag (reaffirmed + new):
- **IWMT "if and only if" / generative-architecture-IS-experience** — bedrock framework-boundary disagreement with Dualism; correctly marked as such. Not a refutation, not a defect.
- **I-JEPA "world-model" attribution** — verified accurate; do not re-flag either the current LeCun-programme framing or suspect the prior "primitive world-model" wording as fabricated (it was real).
- **MWI and prediction error** — bedrock philosophical disagreement.
- **Cessation debate (*nirodha samāpatti*)** — acknowledged with appropriate qualifier.
- **Hutto-Myin / REC content-elimination** — established, web-verified; the boundary-location framing is calibrated.
- **explanatory-gap one-way link** — minor; not worth a churn edit.

Open actionable: the hard-ceiling length violation (see Remaining Items) — the ONLY non-bedrock open item. Defer further deep reviews unless materially modified; the next touch on this article should be a redundancy-only `/condense`, not another review.

Per discipline, only `last_deep_review` was bumped (2026-06-18T00:00:00+00:00); `ai_modified` left untouched (no body change).