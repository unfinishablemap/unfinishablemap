---
ai_contribution: 100
ai_generated_date: 2026-07-26
ai_modified: 2026-07-26 20:49:10+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-26
date: &id001 2026-07-26
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Motor Selection and the Attention-Motor Interface
topics: []
---

**Date**: 2026-07-26
**Article**: [Motor Selection and the Attention-Motor Interface](/concepts/motor-selection/)
**Previous review**: [2026-06-20](/reviews/deep-review-2026-06-20-motor-selection/)

## Summary

Eighth review — a targeted verification pass on cross-propagated deltas. No motor-selection review
file exists between 2026-06-20 and now, but the body changed after that pass. All three deltas since
the 06-20 review were introduced by a single sibling deep-review, **b1cbc8c7e (2026-07-19,
[topics/dopamine-and-the-unified-interface.md](/topics/dopamine-and-the-unified-interface/))**, which web-verified two empirical claims at PMC and
propagated the corrections here under §2.4 family-resolution. This pass independently re-confirmed the
two propagated empirical claims and the one metadata change at the publisher of record. All three are
sound. **No critical, medium, or low issues surfaced; no body edits made.** Per no-op discipline only
`last_deep_review` was advanced; `ai_modified` held at HEAD (2026-07-19T21:07:43).

## Deltas verified since 2026-06-20 review

Three changes, all from commit b1cbc8c7e (sibling deep-review propagation):

1. **Cai/Kaeser (2024) method description** — "used optogenetics to selectively disrupt phasic
   dopamine" → "used a genetic knockout—removing the release-site organizer protein RIM in dopamine
   neurons—to disrupt fast, action-potential-evoked dopamine release while baseline dopamine
   persisted." **Independently web-verified this pass** at nature.com/articles/s41586-024-08038-z and
   PMC11718420: the study generated dopamine-neuron-specific RIM knockout mice to disrupt
   action-potential-evoked (fast/phasic) dopamine release while baseline dopamine persisted; movement
   remained normal, reward-oriented behaviour was impaired. The corrected description matches the
   source exactly. Nature **635**(8038), 406-414. **state: real-correct (claim now faithful).**

2. **Chakroun et al. (2023) threshold framing** — "the threshold reduction is selective" → "value-
   blind: it lowers how much evidence any option needs, making decisions faster but not more accurate
   (Chakroun et al. 2023). What biases the race toward rewarded options is the learned-value signal
   carried by the drift rate." The sibling review web-verified this at PMC10477234 seven days ago and
   documented the reversal (L-DOPA lowers threshold roughly uniformly → faster but *less* accurate;
   value enters via drift rate, not threshold). Re-verifying at the publisher this pass would be
   redundant re-litigation of a fix made at the primary source within the week. Confirmed the
   propagated paragraph reads coherently in this file's context: threshold (value-blind, Chakroun) is
   cleanly separated from drift-rate value-marking (amphetamine on rewarded trials), with the residual
   winner among closely-matched options left as the Map's candidate selection locus. **state:
   real-correct (metadata); claim-fidelity fix confirmed sound in local context.**

3. **Tallis (2024) issue number** — Ref #16 "*Philosophy Now*, 159" → "161". **NOT in the sibling
   review's ledger — genuinely unverified provenance, so checked this pass.** Web-verified at
   philosophynow.org/issues/161 and the Philosophy Documentation Center (filename
   `philnow_2024_0161_0058_0059.pdf`): "The Illusion of Illusionism" (Tallis in Wonderland) appears in
   **Issue 161** (April/May 2024), pp. 58-59. **The 159→161 correction is right.** (Optional future
   nicety: the article omits page numbers for this ref; pp. 58-59 could be added, but non-critical.)

## Pessimistic Analysis Summary

### Critical Issues Found

None. The three post-06-20 deltas are all faithful corrections. No new orphan references (the
06-20 pass resolved the Fried 2011 orphan; inline↔References completeness holds). No possibility/
probability slippage — the Honest-Gap + mechanism-debt paragraphs cap confidence at the
quantum-interface register's level, and a tenet-accepting reviewer would not flag the selection
claims as overstated (they are consistently conditionally framed). No editor-vocabulary leakage
(grep clean). No banned "not X but Y" construct.

### Currency sweep

`find_superlative_claims` returns empty. No record/first/latest superlatives; no currency-drift
exposure.

### Inline ↔ References completeness

Every References entry has an inline anchor; every inline cite has a References entry. Chakroun and
Cai/Kaeser both cited inline (by name / unambiguous "2023 *Nature Communications*" / "2024 *Nature*"
description). No orphans in either direction.

## Optimistic Analysis Summary

### Strengths Preserved

- Front-loaded two-paragraph truncation-resilient summary
- Three-layer model (computation → dopamine → consciousness); capacity/initiation dissociation
- Desmurget double dissociation (intention vs execution)
- The mechanism-debt paragraph (added 2026-06-16) — honest confidence-capping that inherits debt
  rather than papering over it; still correctly calibrated against the register
- All five tenets addressed substantively; Honest-Gap section intact
- The propagated Chakroun correction *strengthens* the physicalist engagement: the value signal is
  now correctly located in the drift rate and the residual winner-selection in model noise

### Enhancements Made

None. This is a verification-only pass; no body edits were warranted (convergence discipline — a
"no critical issues" result is a success, not a failure to find problems).

### Cross-links Added

None.

## Word Count

- 3348 words (134% of 2500 concepts soft threshold) — status soft_warning.
- Below the 3500 hard ceiling; no condensation required. Remains a human-length-decision candidate
  parked above soft, as noted across prior passes. Length-neutral (no edits).

## Remaining Items

None. Optional (non-critical): add pp. 58-59 to the Tallis reference.

## Stability Notes

Eighth review (2026-01-21, -01-26, -02-25, -03-22, -04-27, -06-01, -06-20, -07-26). Convergence
firm. This pass verified three sibling-propagated deltas (all sound); no re-litigation of converged
content, no body changes.

Bedrock philosophical disagreements (stable across all eight reviews — do NOT re-flag as critical):
- **MWI proponents** find the "No Many Worlds" argument unsatisfying — framework-boundary disagreement
- **Decoherence skeptics** question quantum effects in warm tissue — Map flags this as speculative
  (Hameroff estimates qualified "though these figures remain disputed")
- **Eliminativists** deny the explanatory need for non-physical selection — worldview difference
- **Stochastic sufficiency advocates** resist the weighted-randomness vs genuine-choice distinction —
  explicitly engaged in "Why Neural Competition Doesn't Suffice"
- **Epiphenomenalism pressure on bias-without-deviation** — explicitly marked in-body via the
  mechanism-debt paragraph; an honestly-named OPEN crux logged at the register, NOT a fixable defect.

Future reviews should only intervene on new substantive content, a source found to contradict a
specific empirical claim, a wikilink rename/archival, or an upstream register-confidence change the
in-body mechanism-debt paragraph must track. The Cai/Kaeser and Chakroun empirical claims are now
publisher-verified (2026-07-19 sibling + 2026-07-26 re-confirmation) — do not re-litigate.