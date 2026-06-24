---
title: "Deep Review - Presentiment and Retrocausality"
created: 2026-06-24
modified: 2026-06-24
human_modified: null
ai_modified: 2026-06-24T21:05:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-8[1m]
ai_generated_date: 2026-06-24
last_curated: null
---

**Date**: 2026-06-24
**Article**: [[presentiment-and-retrocausality|Presentiment and Retrocausality]]
**Previous review**: [[deep-review-2026-05-26-presentiment-and-retrocausality|2026-05-26]]

Seventh deep review (plus a dedicated pessimistic review earlier today,
[[pessimistic-2026-06-24c-presentiment-and-retrocausality|2026-06-24c]]). The
article was modified earlier today by a `refine-draft` pass (commit ec36906bd,
20:50 UTC) that addressed the two citation defects the morning pessimistic review
flagged. This review verifies those fixes against the publishers of record rather
than re-litigating the long-converged structural content. No further body changes
were warranted; only `last_deep_review` was advanced.

## What Changed Since Last Review

The 2026-06-24 refine-draft (ec36906bd) made two corrections:

1. **Mossbridge et al. (2012) confidence interval** — was "0.21 (95% CI: 0.15-0.27,
   p < 2.7 × 10⁻¹²)"; now "0.21 (random-effects 95% CI: 0.13-0.29, p < 5.7 × 10⁻⁸;
   the more restrictive fixed-effect model gives a narrower 0.15-0.27)".
2. **Wagenmakers "10²⁰ to 1" prior odds** — was presented as a figure Wagenmakers
   et al. (2011) "set"; now Wagenmakers is attributed only what they actually did
   ("default Bayesian t-test", "weak to nonexistent"), and the 10²⁰ figure is
   explicitly recast as "the Map's own illustration, not a value Wagenmakers
   tabulated".

## Pessimistic Analysis Summary

### Critical Issues Found
None. Both items the morning pessimistic review raised were already resolved before
this review and are verified correct (ledger below).

### §2.4 Publisher-of-Record Citation Web-Verify (per-cite ledger)

- Mossbridge, Tressoldi & Utts 2012 (Front. Psychol. 3:390) — **real-correct**.
  Verified at the Frontiers/PMC source: the paper reports BOTH a fixed-effect model
  (ES 0.21, 95% CI 0.15–0.27, p < 2.7 × 10⁻¹²) and a random-effects model
  (ES 0.21, 95% CI 0.13–0.29, p < 5.7 × 10⁻⁸). The article's current text states
  the random-effects interval as the headline (with its *matching* random-effects
  p-value) and keeps the fixed-effect interval as a parenthetical. This is faithful
  and is the canonically-restated figure (Duggan & Tressoldi 2018 restate the
  original as "0.21, 95% CI 0.13–0.29"). The refine resolved the morning review's
  Issue 1 *better* than the proposed one-token swap by preserving both models and
  pairing each CI with its own p-value, avoiding a new cross-model inconsistency.
- Duggan & Tressoldi 2018 (F1000Research 7:407) — **real-correct**. Pre-registered
  0.31 (95% CI 0.18–0.45) vs non-pre-registered 0.24 (95% CI 0.08–0.41) verified at
  PMC; the overall update effect is 0.28 (95% CI 0.18–0.38). The article's 0.31/0.24
  split is faithful. This resolves the item the morning review marked "verify on next
  refine, low priority."
- Galak, LeBoeuf, Nelson & Simmons 2012 (JPSP 103(6):933-948) — **real-correct**.
  Seven experiments, N = 3,289, meta-analytic effect ≈ zero (d = .04). Faithful.
- Bem 2011 (JPSP 100(3):407-425) — **real-correct** (metadata stable across prior
  reviews; "Feeling the Future" verified).
- Bem, Tressoldi, Rabeyron & Duggan 2016 (F1000Research 4:1188) — **real-correct**.
  Bayes factor reported "on the order of 10⁹" (actual ≈ 5.1 × 10⁹) — order-of-
  magnitude framing, accepted by all prior reviews.
- Wagenmakers et al. 2011 (JPSP 100(3):426-432) — **real-correct metadata**; the
  attribution defect (presenting a self-derived 10²⁰ as Wagenmakers' stated value)
  is now fixed by recasting the figure as the Map's own illustration. Faithful.
- Cramer 1986, Wheeler 1978, Dalkvist et al. 2002 — metadata stable across prior
  reviews; no change.
- Inline ↔ References cross-check: every inline `Author YYYY` has a References entry
  and vice versa. No orphans.
- Empirical-record currency sweep: helper returns no superlative claims; n/a.

### Attribution Accuracy Check
- The Wagenmakers recast is the key item and is now correct: Wagenmakers et al. are
  credited only with what they did (default Bayesian reanalysis; "weak to
  nonexistent" verdict) and the 10²⁰ illustration is explicitly the Map's own. No
  remaining misattribution, dropped qualifier, overstated position, or
  source/Map conflation.

### Reasoning-Mode Classification (engagement with Tegmark / decoherence)
- **Engagement with Tegmark's decoherence objection: Mode Three (framework-boundary
  marking), correctly applied** — unchanged from the 6th review. The article
  voluntarily concedes the decoherence threat applies to the Map's own neural
  interface ("in degree, not kind") and defers the substantive single-event response
  to [[quantum-consciousness]] rather than dressing it as a refutation of Tegmark. No
  boundary-substitution; no editor-vocabulary label leakage in prose.

### Medium Issues Found
None requiring a change. The morning pessimistic review raised two dialectical
pressure points that do NOT require edits:
- *The degree-not-kind asymmetry lacks a quantitative anchor* — the article already
  gestures at the load-bearing information-availability disanalogy (selection over
  internally-instantiated superposed states vs. anticipatory coupling to an external
  event "the organism has no information about"). Strengthening this to an explicit
  kind-claim is an optional enhancement, not a defect; the article's honest "degree
  of implausibility, not a clean line" framing is itself the calibration the house
  style rewards. Left as-is to avoid oscillation on a converged passage.
- *Front-loading one sentence of the single-event decoherence response* — optional
  truncation-hardening, not a defect. Deferred; the deferral to
  [[quantum-consciousness]] is honest.

## Optimistic Analysis Summary

### Strengths Preserved
1. The firewall framing (physics-based retrocausality vs. contested presentiment) —
   the article's signal virtue; lets the Map present hostile evidence honestly
   without staking its foundations on it.
2. Self-surfaced decoherence concession — exemplary intellectual honesty; the
   Hardline-Empiricist persona's praise-worthy "tenet-coherent, not
   evidence-elevating" restraint.
3. Even-handed treatment of both meta-analytic support and replication-failure /
   Bayesian-skeptic sides.
4. Clean Libet (internal-decision timing) vs. presentiment (external-event
   anticipation) separation.
5. The Bayesian-debate paragraph illustrates prior-dependent evidential weight
   clearly, now with the 10²⁰ figure honestly flagged as illustrative.

### Enhancements Made
None. The refine-draft applied the corrections earlier today; this review confirms
they are sound against the publishers of record rather than adding further changes.

### Cross-links Added
None needed. Eight Further Reading entries, all verified to resolve.

## Word Count
- Before: 1972 words
- After: 1972 words (no content changes this review)

## Remaining Items
None. Two optional enhancements noted above (quantitative anchor for the
degree-not-kind asymmetry; front-loaded single-event decoherence sentence) are
deferred as enhancement opportunities, not deferred defects.

## Stability Notes

Seventh deep review. The article fully converged by the 4th/5th review. The two
calibration corrections in May (Wheeler claim, mechanism-gap symmetry) and the two
citation corrections today (Mossbridge CI, Wagenmakers attribution) have only
*improved* calibration and faithfulness; no new problems have been introduced. The
article is now more robust against drift than at any prior review — every figure a
tenet-accepting reviewer could legitimately flag has been web-verified at the
publisher of record.

Bedrock disagreements to NOT re-flag in future reviews (carried forward from the
6th review):
1. **Physicalist rejection of quantum interactionism** — framework-boundary, not fixable.
2. **MWI defender dissatisfaction** — the Map rejects MWI by tenet; expected standoff.
3. **Skeptic vs. proponent stalemate on presentiment data** — the article correctly
   reports the literature as genuinely contested and does not take a side; a feature,
   not a flaw.
4. **The firewall is comparative, not a testability claim** — the article already
   states it "buys ... comparative, not absolute" advantage and that "a confirmed
   phenomenon is not a confirmed interpretation." A strict Popperian's point that
   empirically-equivalent interpretations are not differentially testable is a
   framework-boundary pressure point the article has already absorbed honestly; do
   not mistake the comparative framing for an overstated testability claim.
