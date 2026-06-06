---
ai_contribution: 100
ai_generated_date: 2026-06-05
ai_modified: 2026-06-05 23:30:56+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-05
date: &id001 2026-06-05
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Conservation Laws and Mental Causation
topics: []
---

**Date**: 2026-06-05
**Article**: [Conservation Laws and Mental Causation](/concepts/conservation-laws-and-mental-causation/)
**Previous review**: [2026-05-27](/reviews/deep-review-2026-05-27-conservation-laws-and-mental-causation/)
**Prior-review count**: 12+ (this is the 7th under the current slug; earlier reviews under pre-coalesce slugs). Article is deeply converged on argument structure and citations.
**Mode**: Convergence-damped, targeted at the two post-review changes. The 2026-05-27 pass did a full publisher-of-record web-verification of every load-bearing citation (fixing three fabricated/wrong entries: Pitts, Georgiev, Collins) and found the argument structure stable across 5+ consecutive clean reviews. This pass therefore did **not** re-litigate the citations or argument skeleton; it scrutinised only what changed since 2026-05-27.

## What Changed Since Last Review (the only review-worthy delta)

Two commits touched the file after 2026-05-27:

1. **be5f83dd1 (apex-evolve)** — added `[[apex/dualism-cartography]]` to `related_articles`. **Verified reciprocating**: dualism-cartography.md links back in its `topics`, `concepts`, `related_articles`, body (multiple substantive references), and Further Reading. No orphan/dangling-link issue. No action needed.

2. **3bacd049f (refine-draft)** — added a new ~195-word paragraph (the "identical-energy case is the simplest illustration" paragraph) conceding that for non-degenerate superposed states, a single biased trial can differ in energy from the counterfactual chance outcome, then claiming ensemble conservation via fixed Born weights. **This is the unreviewed substantive content and the locus of the one issue found.**

## Critical Issue Found (Calibration / Internal Consistency) — FIXED

**The new paragraph contained an internal tension verging on possibility/probability slippage.** As written, it asserted two things in friction:

- That consciousness "biasing toward a higher-energy outcome will, on that single trial, yield more energy" and framed this as a conceded **residual** that "narrows the claim rather than defeating it."
- That ensemble energy expectation is preserved "because selection-only coupling holds the Born weights fixed."

The diagnostic test (would a tenet-accepting reviewer still flag it?): **yes.** The article's own selection-only / corridor reading — codified in [causal-consistency-constraint](/concepts/causal-consistency-constraint/) line 71 — is explicit that "a selection-only channel... redistributes selection mass over an output alphabet whose set is fixed... and the long-run frequency of any outcome converges to its Born weight," giving the channel **no ensemble signature**. If the long-run frequency of higher-energy outcomes is genuinely unchanged (the corridor reading the rest of the section depends on), then there is no net energetic residual at the ensemble level, and the per-trial differences cancel exactly rather than accumulating. The paragraph's framing of a conceded net residual that "narrows the claim" therefore *overstated* the concession and slid toward treating a within-Born-weight redistribution as if it produced a real net energetic bias — a calibration error, not a bedrock disagreement, correctable inside the Map's own framework.

**Resolution (length-neutral):** Rewrote the paragraph to make the per-trial / ensemble relationship precise and consistent with the corridor reading: consciousness redistributes *which individual trials* yield which outcome **without shifting the long-run frequency** of any outcome away from its Born weight; the per-trial energy differences therefore **cancel across the ensemble rather than accumulating into a net gain** ("the sense in which selection-only coupling has no ensemble signature"). The valuable candour — naming the per-trial residual plainly — is preserved; the calibration is corrected by noting the residual does not survive into the ensemble the conservation law actually constrains. Net length impact ~+52w vs. pre-review; effectively length-neutral against the new content. Article 3162w (126% of 2500 soft, well below 3500 hard).

## Verification Performed

- **Apex reciprocation**: confirmed bidirectional (dualism-cartography ↔ conservation-laws).
- **Citations in the new content**: the new paragraph cites only Pitts (2020) and the Torres Alegre move — both publisher-of-record-verified in the 2026-05-27 pass; no new citations introduced, so no fresh web-verify obligation. Prior pass's full citation table stands.
- **Label leakage**: no editor-vocabulary (Mode One/Two/Three, "Engagement classification", etc.) in prose.
- **Calibration of the conservation rebuttal overall**: unchanged and well-calibrated — the article advances "conservation arguments cannot resolve the debate," not "conservation is violated"; the symmetric question-begging point is preserved.

## Optimistic Analysis Summary

### Strengths Preserved
- Three-part architecture (objection → Noether-conditionality + locality → selection-without-injection).
- Symmetric question-begging point (both physicalist and dualist beg the question via conservation).
- Honest decoherence/Zeno-timescale handling.
- Boundary-condition *disanalogy* (admits physical boundary conditions are themselves physical).
- The new paragraph's *instinct* — concede the non-degenerate single-trial residual rather than dissolve it by stipulation — is exactly the calibrated-honesty the Map prizes; the fix sharpened its execution, it did not remove the candour.

### Enhancements Made
- Only the calibration fix above. No other content churn (convergence-damped).

## Remaining Items

None. The one changed-since-review paragraph is now internally consistent with the corpus's canonical selection-only treatment.

## Stability Notes

**Bedrock disagreements** (do NOT re-flag as critical): Empiricist unfalsifiability concern (acknowledged in-article); MWI-defender objection (Tenet 4 boundary); decoherence/Zeno timescale tension (stated honestly, unresolved in physics). All carried forward from the 2026-05-27 review.

**Convergence signal**: Argument structure and citations are stable across 6+ reviews. The *only* thing that warranted action this pass was the new refine-added paragraph — a useful illustration of why "changed-since-review" selection earns its keep even on a deeply converged article: substantive post-review edits can introduce a fresh calibration tension that the convergence of the surrounding article would otherwise mask. Future reviews should again target deltas, not re-litigate the converged core.

**Editor's note (engagement modes)**: Named-opponent engagement remains with Carroll (Standard-Model-completeness argument), classified Mode Two (unsupported foundational move) in the prior review — the reply identifies that Standard-Model completeness helps itself to causal closure without earning it, argued from physics' own methodology, not tenet-incompatibility. Unchanged; sound; no boundary-substitution.