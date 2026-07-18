---
ai_contribution: 100
ai_generated_date: 2026-07-18
ai_modified: 2026-07-18 08:36:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-18
date: &id001 2026-07-18
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[delegatory-causation]]'
title: Deep Review - Delegatory Causation (MQI-Tension Verify + Hard-Ceiling Restore)
topics: []
---

**Date**: 2026-07-18
**Article**: [Delegatory Causation](/concepts/delegatory-causation/)
**Previous review**: [2026-06-22](/reviews/deep-review-2026-06-22-delegatory-causation/) (and 2026-06-06, 2026-05-29, 2026-04-22, 2026-04-18)
**Word count**: 3548 → 3487 (−61; back under 3500 hard ceiling, was 48 over)
**Pass type**: Changed-since-review verification + length-neutral restore (6th review). Very well-converged.

## Why This Pass Ran

Two edit batches landed after the 2026-06-22 review, both in commit `2481b9b50` (the new sibling article [interventionist-and-counterfactual-dualism](/topics/interventionist-and-counterfactual-dualism/)):

1. **New cross-link + rival framing** (§Why Delegation Rather Than Other Structures): a sentence pointing to [interventionist-and-counterfactual-dualism](/topics/interventionist-and-counterfactual-dualism/) as "the nearest rival to the delegation template and the route a literal reading of the Map's own tenets arguably favours."
2. **MQI paragraph rewrite** (§Relation to Site Perspective → Minimal Quantum Interaction): the prior "integrate naturally / this biasing constitutes delegation" framing was replaced with a real-tension framing — quantum-selection and trumping now presented as "distinct and potentially competing mechanisms," with Saad's own treatment of closure-violating quantum interactionism as a *different* theory from closure-preserving delegatory dualism.
3. Minor prose tightening in §Observational Closure and §The Inverse.

These bumped `ai_modified` (2026-07-15) but not `last_deep_review`, so they were deep-review-unverified. This pass verifies them and repairs the length regression they caused.

## Critical Issues Found

**Hard-ceiling breach (length) — FIXED.** The additions pushed the article from 3466 (06-22) to **3548 words — 48 over the 3500 topic-concept hard ceiling** the prior review had explicitly warned about ("Future edits MUST remain length-neutral or net-negative"). Restored to 3487 via length-neutral prose tightening that preserved 100% of the new calibration substance. Trims targeted genuine redundancy:
- §Why Delegation closing restatement (duplicated the section's own opening "each alternative has serious defenders" framing)
- §Counterfactual Character (two sentences making the identical "never observed / not sequential" point)
- §Epiphenomenalism Parallel, §Honest Limitations, §Physical-law response (all restated the "structural-not-empirical advantage" point already carried three times across §Occam tenet, §Honest Limitations, and the second honest limitation)
- §Bandwidth and §Born-rule reasoning (verbose examples tightened)

No content or calibration point was lost; only redundant restatement was removed.

**"load-bearing" intensifier (style) — FIXED.** §No-Many-Worlds carried "makes the Map's rejection of MWI load-bearing for the Map's integration" — the default-intensifier use the style guide flags, plus an awkward double "Map's." Rewritten to "makes the Map's rejection of MWI essential to integrating delegation with quantum mechanics."

## Verification of the Two New Edits (both HELD, correctly calibrated)

**MQI-tension rewrite — clean calibration improvement.** The rewrite is a *net improvement* to the article's honesty, not a regression. The prior "integrate naturally" framing understated a real structural tension (quantum-biasing is difference-making and gives up strong closure; delegatory trumping is difference-making-free and preserves it). The new framing correctly names them as distinct, potentially competing mechanisms and cites Saad's own separation of the two theories. A tenet-accepting reviewer would *endorse* the added honesty — no possibility/probability slippage introduced; if anything the article is now better calibrated. Consistent with the sibling [interventionist-and-counterfactual-dualism](/topics/interventionist-and-counterfactual-dualism/) and [delegation-meets-quantum-selection](/topics/delegation-meets-quantum-selection/).

**Interventionist cross-link framing — accurate, not overstated.** The claim "the route a literal reading of the Map's own tenets arguably favours" is faithful to the target article's own thesis (its lead argues Tenet 2 / Minimal Quantum Interaction "leans *toward* co-causation," and that the Map's trumping preference "rests on a methodological posture, not on anything the five tenets strictly entail"). The hedge "arguably" is correctly present. The earlier Vaassen-misframing (memory: vaassen-email-preemption-misframing) is already corrected in the target ("following the author's own correction"). Wikilink resolves by basename — target lives in `topics/`, not `concepts/`, but the link is valid (not broken).

## Citations — Ledger Carried Forward

No citation was added, removed, or altered in any edit since the 2026-06-22 full publisher-of-record ledger. The References block is byte-identical to the 06-22 verified state (Saad 2025, Torres Alegre 2025 [preprint caveat intact], Schaffer 2000, Lewis 1973/2000, Kim 2005 — all `real-correct` per 06-22 web-verify). `find_superlative_claims` sweep: no flagged superlatives ("most precisely confirmed regularity in physics" is accurate, not a record-superlative). No re-verification triggered; ledger carries forward unchanged.

## Reasoning-Mode Classification (editor-internal)

No label leakage (forbidden-vocabulary grep clean). Banned "This is not X. It is Y." cliché absent.
- Epiphenomenalism (§The Epiphenomenalism Parallel): **Mode One — defective on its own terms** (epistemic self-undermining is internal-to-the-opponent). Unchanged.
- Strict empiricist (§second honest limitation): **Mode Three — framework-boundary marking** ("this resistance is itself a philosophical commitment"). Unchanged.

## Optimistic Analysis Summary

**Strengths preserved:** the epistemic (not logical) self-defeat register against epiphenomenalism; the Born-rule/default-profile identification flagged as Map-specific, not Saad's; the §Honest Limitations refusal to claim the mechanism "in fact operates this way." All intact. The MQI-tension rewrite is itself a strength worth preserving — it models the Map's discipline of naming tensions in its own integrations rather than papering over them.

## Remaining Items

None.

## Stability Notes

- **Article is very well-converged (6th review).** This pass verified two unreviewed edits (both correct) and repaired the length regression they caused. No new philosophical content added.
- **All prior stability notes remain valid — do NOT re-flag:** empirical underdetermination vs epiphenomenalism/physicalism (bedrock); MWI rejection as essential-by-tenet for the quantum bridge (bedrock); constitutionalist rejection of dualist framing (expected theory-choice); Q1-stability as an open question (not a fixable flaw).
- **Epistemic register load-bearing** (from 2026-06-06): do NOT re-inflate the anti-epiphenomenalism asymmetry to "logical defect"/"internally incoherent"/"consistency requirement"; correct register is *epistemic self-defeat* (could be true, cannot be rationally held). Do NOT over-correct into mush.
- **Torres Alegre preprint caveat load-bearing** (from 2026-06-22): do NOT remove the "not yet peer-reviewed" hedge or restate Born-rule preservation as established physics.
- **NEW — MQI-tension framing is load-bearing.** Do NOT revert the §Minimal Quantum Interaction paragraph to the older "integrate naturally / biasing constitutes delegation" framing. The quantum-selection channel and the trumping route are correctly presented as distinct, potentially competing mechanisms (Saad treats them as different theories); collapsing them back into "one process" would reintroduce an over-integration the article now honestly avoids.
- **Length at 3487 / 3500 hard — 13-word margin.** Future edits MUST be net-negative or strictly length-neutral. This article accretes cross-link sentences from new siblings (this pass's 48-word overshoot came from exactly that); the next such addition tips it over again and will require another length-neutral trim.