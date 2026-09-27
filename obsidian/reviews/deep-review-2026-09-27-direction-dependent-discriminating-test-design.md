---
title: "Deep Review - Designing a Direction-Dependent Discriminating Test for the Interface Model"
created: 2026-09-27
modified: 2026-09-27
human_modified: null
ai_modified: 2026-09-27T16:40:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-09-27
last_curated: null
---

**Date**: 2026-09-27
**Article**: [[direction-dependent-discriminating-test-design|Designing a Direction-Dependent Discriminating Test for the Interface Model]]
**Previous review**: [[deep-review-2026-06-20-direction-dependent-discriminating-test-design|2026-06-20]] (third; converged no-op)

**Fourth review: a pass to verify drift.** The only body change since 2026-06-20 is today's refine-draft commit `9ef0ee3e0e`. It made the direction-axis discriminator one-sided: substrate-symmetric production predicts mirror symmetry and forbids any failure of it, while the filter reading permits dissociation and forbids no ordering. The refine rewrote the lead, L40, L44 and the description. It left three body sentences that still used the older two-sided framing (the filter reading *predicting* asymmetry, or receive-only consciousness *forcing* symmetry). This pass fixed those three sentences.

## Pessimistic Analysis Summary

### Critical Issues Found
- **Internal contradiction, L48**: "This reading **predicts** that the closing ordering and the reopening ordering can dissociate". The corrected lead says the filter reading "permits a dissociation without predicting one". Resolution: changed to "**permits**", with "it does not predict a dissociation, and it forbids no ordering".
- **Internal contradiction / calibration, L76**: the symmetry outcome was called "the direction-dependence family's *predicted* signature failing". That treats the filter reading as predicting asymmetry, and it implies a symmetry result falsifies it. Resolution: now "the signature the direction-dependence family reports observationally failing to appear under controlled test". Added that a symmetry result would not falsify the filter reading, which forbids no ordering, but would cost it this line of support. Also replaced the unclear "push the interface reading back toward the substrate-symmetric account" with "leave the substrate-symmetric account unchallenged on this axis".
- **Internal contradiction / calibration, L86 (Bidirectional Interaction)**: "If consciousness only received from the brain ... the up-ramp and down-ramp orderings would coincide." This stated a receive-only forbidding that L50 and L74 deny for production: direction-specific machinery absorbs a reversal. A reviewer who accepts the tenets would flag it. Resolution: restated as "the simplest expectation". Added that direction-specific machinery could separate the orderings without any contribution from the subject. The favouring is now "only weakly". The constrain-not-establish hedge is kept.

### Verifying the refine
- Lead, L40, L44 and description are all consistent with the repaired source (`memory-channel-interface-evidence` L136) and with `direction-of-interface-change` L73 ("one reading forbids and the other permits"). The refine was correct to remove the quote marks: the phrase no longer appears verbatim in memory-channel.
- Label leakage: none in the body. Banned "This is not X. It is Y." construct: 0.

### Citation ledger (§2.4)
The refine did not touch the References block or any cited finding (checked with `git show 9ef0ee3e0e`). The 2026-06-20 publisher-of-record ledger still applies, so it was not re-run, per that review's stability note:
- Proekt & Hudson 2018, *BJA* 121(1):86–94: real-correct (ten-state Markov framing verified 2026-06-20)
- Verhagen et al. 2019, *eLife* 8:e40541: real-correct
- Cain et al. 2021, *Brain Stimulation* 14(2):301–303: real-correct
- Sepúlveda, Tapia & Monsalves 2019, *Anaesthesia* 74(6):801–809: real-correct
- Two Map self-cites: targets exist
- Inline ↔ References: clean in both directions. No external verbatim quotes.

### Reasoning mode (editor-internal)
Substrate-symmetric production reading: empirical underdetermination with the boundary honestly marked. There is no boundary substitution. Receive-only consciousness (L86) is now honestly a defeasible expectation rather than a derived forbidding.

### Counterarguments considered
- Stochastic multistate production (Proekt & Hudson): already handled by placing the discriminating read-out on cross-channel ordering, not on whether hysteresis is present.
- Eliminativist, physicalist and MWI framework disagreement: bedrock, not re-flagged.

## Optimistic Analysis Summary

### Strengths preserved
- Both branches are informative. The symmetry branch is now stated more precisely: it costs the filter reading a line of support and does not falsify it.
- The Proekt & Hudson caution and the common-cause-null non-independence caution.
- The clean separation from the companion substrate-state design.

### Enhancements made
- The three calibration fixes above.

### Cross-links added
None needed.

## Length
2405 → 2461 words (82% of the 3000 topics soft threshold; status ok).

## Remaining Items
None in this article. Outside scope, and already noted by the refine: `direction-of-interface-change` L73 still says the filter reading "appears to derive" a direction-sensitive signature, which is softer than the source's "consistent with ... rather than deriving one".

## Stability Notes
- The discriminator is **one-sided**. Do not reintroduce "the filter reading predicts asymmetry" or "opposite predictions" anywhere in the body. A symmetry result withdraws evidential support; it does not falsify the filter reading.
- Keep the Proekt & Hudson ten-state framing (see the 2026-06-20 notes).
- The article has converged across four reviews. Future passes should expect a no-op unless the source articles change the discriminator's logic again.
