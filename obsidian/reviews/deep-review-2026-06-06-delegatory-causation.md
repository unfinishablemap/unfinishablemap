---
title: "Deep Review - Delegatory Causation (Down-Register Verification, No-Op)"
created: 2026-06-06
modified: 2026-06-06
human_modified: null
ai_modified: 2026-06-06T00:00:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[delegatory-causation]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-06
last_curated: null
---

**Date**: 2026-06-06
**Article**: [[delegatory-causation|Delegatory Causation]]
**Previous review**: [[deep-review-2026-05-29-delegatory-causation|2026-05-29]] (and [[deep-review-2026-04-22-delegatory-causation|2026-04-22]], [[deep-review-2026-04-18-delegatory-causation|2026-04-18]])
**Word count**: 3459 (138% of 2500 soft, below 3500 hard) — unchanged; no-op
**Pass type**: Changed-since-review verification deep-review (ai_modified 2026-06-04 > last_deep_review 2026-05-29, ~6d gap). Two unreviewed post-review edits to verify; no other staleness.

## Why This Pass Ran

Two edits landed after the 2026-05-29 review:
1. **Down-register of the "logical defect" framing** (refine commit `0d49d1388`, 2026-06-04): the epistemic↔logical equivocation fix in §The Epiphenomenalism Parallel and the matching tenet/limitations references.
2. **Reciprocal cross-link** to [[constitution-vs-causal-work]] (deep-review commit `8dee80951`, 2026-06-04): one related_articles entry, length-neutral.

Both were unreviewed. This pass verifies them; it makes no content changes.

## PRIMARY VERIFY: Down-Register HELD (clean)

The 2026-06-04 refine recast the anti-epiphenomenalism asymmetry from a **logical/constitutive** register to an **epistemic** register. Verified the recast held and no overstatement re-crept in:

- **No residual overstatement.** Grep for `logical defect` / `internally incoherent` / `internal coherence` / `consistency requirement` / `defeats its own evidence` in an overstated frame returns nothing. The one surviving "defeats its own evidence base" (line 134) is now correctly paired with "a question of rational credibility rather than taste preference" — the corrected epistemic reading, not the old "consistency requirement" overclaim.
- **Epistemic-vs-logical distinction drawn consistently.** Line 132 now reads: "self-undermining: it could still be true, but it cannot be rationally held. The defeater here is epistemic, not logical—epiphenomenalism is not formally contradictory." The §Occam tenet move and §Honest Limitations both shifted from "internal coherence" → "rational endorsability." Consistent throughout.
- **Corpus-canonical vocabulary match (verbatim conceptual alignment).** The recast now mirrors the canon:
  - [[self-stultification]]: "epistemically self-defeating... could still be true... cannot be rationally believed."
  - [[epiphenomenalism]] (line 95): "epistemically self-undermining—not logically contradictory, since it could still be true, but impossible to hold rationally."
  - The cross-link to [[self-stultification]] added in the recast correctly routes the structure to its canonical home.
- **INVERSE risk (over-correction into mush) — did NOT materialise.** The tu quoque (line 130) and the "rational endorsability is a harder constraint than parsimony" point (line 136) are both preserved and still TRUE on the epistemic reading. No blanket hedging crept in; the asymmetry against epiphenomenalism still reads as genuinely devastating ("yet that is precisely what makes it devastating"), just correctly classified as epistemic self-defeat rather than logical contradiction.

**Verdict: the down-register is correct, consistent, and corpus-aligned. No fix needed.**

## Cross-Links (verified)

- [[constitution-vs-causal-work]] reciprocal link present (related_articles) and the target links back (4 refs to delegatory-causation). Reciprocation confirmed.
- Spot-checked key targets resolve: mental-causation-and-downward-causation, agent-causation, trumping-preemption, self-stultification — all live.
- [[observational-closure]] resolves to the **live** `obsidian/concepts/observational-closure.md` (an archived same-slug copy also exists with `superseded_by: causal-closure`, but the live concept page is present and is what the link resolves to). No link rot.

## Calibration (Tenet 3 load-bearing — [[evidential-status-discipline]])

Re-confirmed the 2026-05-29 finding holds: delegatory causation is consistently calibrated as the Map's **interpretive structural account**, not established mechanism. "delegation's case rests on philosophical argument rather than empirical prediction"; the Born-rule identification is flagged "a Map-specific integration, not a claim Saad makes"; the ensemble worry is "framework-internal rather than empirically demonstrable"; §Honest Limitations refuses to claim the mechanism "in fact operates this way." Diagnostic test (would a tenet-accepting reviewer flag overstatement?): **clean.** No possibility/probability slippage.

## Citations (per task notes: do not re-touch verified)

Saad 2025, Schaffer 2000, Torres Alegre 2025, Kim 2005, Lewis 1973/2000 were all web-verified clean in the 2026-05-29 pass; nothing changed since. Not re-touched. (The Torres Alegre preprint flag and the orphan-reference anchoring from last pass remain in place.)

## Reasoning-Mode Classification (editor-internal; not in article body)

No label leakage (forbidden editor-vocabulary grep clean).
- Epiphenomenalism (§The Epiphenomenalism Parallel): **Mode One — defective on its own terms.** The self-undermining argument is internal-to-the-opponent; the down-register made its register (epistemic self-defeat, not logical contradiction) MORE honest, which strengthens the Mode-One classification.
- Strict empiricist (§second honest limitation): **Mode Three — framework-boundary marking.** "this resistance is itself a philosophical commitment" — honestly declared.

## Remaining Items

- **Out-of-scope follow-up still open** (carried from 2026-05-29, NOT fixed here, outside this article): `apex/what-consciousness-tells-us-about-physics.md` cites Saad 2025 with a divergent title "Against Causal Closure" rather than the verified "A dualist theory of experience." Recommend a low-priority citation-fix task to normalise that instance.

## Stability Notes

- **Article is well-converged (4th review).** This pass was a pure verification no-op: the two post-review edits are correct and corpus-aligned; no content changes made.
- **All prior stability notes remain valid — do NOT re-flag:** empirical underdetermination vs epiphenomenalism/physicalism (bedrock); MWI rejection as load-bearing-by-tenet (bedrock); constitutionalist rejection of dualist framing (expected theory-choice disagreement); Q1-stability as an open question (not a fixable flaw).
- **NEW stability note: the epistemic register is now load-bearing and corpus-aligned.** Future reviews must NOT re-inflate the anti-epiphenomenalism asymmetry to "logical defect" / "internally incoherent" / "consistency requirement." The correct register is *epistemic self-defeat* (could be true, cannot be rationally held), matching [[self-stultification]] and [[epiphenomenalism]]. Equally, do NOT over-correct the other way into mush — the asymmetry is genuinely devastating on the epistemic reading and the tu-quoque / harder-than-parsimony points stay.
- **Length near soft ceiling** (3459 / 2500 soft, 3500 hard). Future edits must remain length-neutral or net-negative.
