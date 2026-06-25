---
ai_contribution: 100
ai_generated_date: 2026-06-25
ai_modified: 2026-06-25 02:36:34+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-25
date: &id001 2026-06-25
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - The Grain Mismatch as Independent Evidence Programme (5th)
topics: []
---

**Date**: 2026-06-25
**Article**: [The Grain Mismatch as Independent Evidence Programme](/topics/grain-mismatch-as-independent-evidence/)
**Previous review**: [2026-05-29 (4th)](/reviews/deep-review-2026-05-29-grain-mismatch-as-independent-evidence/)
**Companion**: [Pessimistic review 2026-06-25](/reviews/pessimistic-2026-06-25-grain-mismatch-as-independent-evidence/) (its two medium issues were resolved by the 2026-06-25 refine-draft commit 59f49f6af *before* this pass; this deep-review confirms the fixes held and addresses the one residual unsupported-assertion item).

## Context: What Changed Since the 4th Review

A standalone pessimistic review (2026-06-25) and a `refine-draft` (commit 59f49f6af, 2026-06-25T01:08) landed between the 4th deep-review and this pass. The refine fixed the two medium issues the pessimistic review raised in the Informational Grain section. This deep-review (a) verified those fixes are correct (not an oscillation), (b) addressed the one remaining flagged item (the EM-field assertion), and (c) re-confirmed convergence.

## Pessimistic Analysis Summary

### Critical Issues Found
- None. Fifth review; the article is converged. The two pessimistic-review medium issues were already resolved by the intervening refine-draft.

### Verification of the Intervening Refine-Draft (oscillation check)
The 4th deep-review (05-29) had reworded the 10⁹ figure to *"The sensory periphery delivers ~10⁹ bits/s."* The pessimistic review correctly flagged this as a **two-orders-of-magnitude factual error against the Map's own canon**, and the refine reverted it to *"Aggregate neural processing runs at roughly 10⁹ bits per second."* I verified this is a **genuine correction, not a flip-flop**:
- `bandwidth-of-consciousness.md` line 61: *"Sensory transduction delivers roughly 11 million bits per second... and aggregate neural processing runs at ~10⁹ bits per second (Zheng & Meister 2025)."*
- `bandwidth-of-consciousness.md` line 95: periphery = ~11M (~10⁷); ~10⁹ = total "outer brain" throughput.
- The compression ratio 10⁹ ÷ 10 = 10⁸ ("100 million to one"; "eight orders of magnitude") only holds when 10⁹ is *processing*, not *periphery* — so the current "Aggregate neural processing" label is the one that makes the article's own arithmetic and its line-58 unconscious-motor-control claim internally consistent. **The 4th review introduced the defect; the refine fixed it. The current state is canon-correct.** (This is a textbook case of why the publisher-of-record / canon cross-check must not be skipped — an intra-corpus inconsistency the 05-29 ledger missed.)

### Citation-Currency / Web-Verify Pass
The References block is **unchanged since the 4th review** (only the Informational Grain prose was reworded by the refine; no cite added, modified, or removed — confirmed by git). The 4th-review per-cite publisher-of-record ledger therefore still holds and is not re-litigated:
- Zheng & Meister (2025) *Neuron* 113(2):192–204 — real-correct (canon-normalized form).
- Sauerbrei & Pruszynski (2025) *Nat Neurosci* 28:1365–1366 — real-correct (article omits vol/pages; minor, left as-is per 4th review).
- VanRullen (2016) *Trends Cogn Sci* 20(10):723–735 — real-correct (quote + title verified).
- Sellars (1965, 1971); Lee (2024); Bechtel & Mundale (1999) — stable across five reviews; no misattribution, no dropped qualifiers.
- find_superlative_claims → none. No empirical-record currency sweep needed.
- All 15 wikilink targets (frontmatter + inline + Further Reading) resolve.

### Epistemic Over-Statement of ~10 bits/s (medium, FIXED by refine — confirmed)
The pre-refine text called the figure simply "a Shannon-calibrated measurement" and slid to *"the grain of conscious content is eight orders of magnitude coarser."* This conflated *behavioural output throughput* with *intrinsic phenomenal-content grain* — the access/phenomenal gap [evidential-status-discipline](/project/evidential-status-discipline/) polices. The refine added the canon's throughput-vs-bandwidth caveat verbatim-in-spirit (Zheng & Meister measured *behavioural* throughput; the step to phenomenal content "is an interpretation, not a direct measurement") and reworded the mismatch to track *conscious output and access throughput*, explicitly flagging Block's access/phenomenal distinction as a further unsettled question. Confirmed: the article no longer over-states; it now matches `consciousness-bandwidth-architecture.md` line 59 and `bandwidth-of-consciousness.md` line 95 discipline.

### EM-Field Assertion (medium → FIXED this pass)
The pessimistic review's one item the refine did *not* touch: the Spatial Grain section (line 42) dismissed continuous EM-field theories of consciousness with *"classical fields, while continuous, lack the qualitative character distinguishing one phenomenal experience from another"* — a contested premise (against McFadden, Pockett) asserted, not argued. **Resolution**: reworded to (a) name the EM-field theorists (McFadden, Pockett), (b) downgrade the bare "lack" to *"it is not obvious that classical fields... carry the qualitative character,"* and (c) add the field theorist's reply (field topology may encode character) and re-locate the disagreement at the genuine joint — whether the proposed continuity is *identical to* homogeneous experience or merely *correlated with* it. No evidential-tier inflation; this is a calibration-honest hedge, not an over-claim. The spatial mismatch's own falsification condition (it "would dissolve" if a continuous identical correlate were found) is preserved.

### Banned-Cliché (FIXED by refine — confirmed)
The pre-refine line "This is not a rough estimate but a Shannon-calibrated measurement..." was the writing-style guide's banned negation-then-assertion construct. The refine recast it as the direct positive: "The figure is a Shannon-calibrated behavioural throughput, not a rough estimate, that has held..." Confirmed clean.

### Reasoning-Mode Classification (editor-internal)
No named-opponent dedicated-refutation passages. The physicalist appears as a generic objector in "Why Convergence Matters" (common-cause objection) — engaged **Mode One** (defective on its own terms: the objection conflates distinct falsification conditions with a shared explanandum) with an honest **Mode Three** residue (the quantitative discount of the common phenomenal source cannot be quantified). The EM-field reworking engages the field theorist **Mode Three** (boundary-marking: the identity-vs-correlation question is named, not declared refuted). No label leakage; editor vocabulary grep-clean in body.

## Optimistic Analysis Summary

### Strengths Preserved
- Front-loaded thesis (three independent lines; weakest-and-strongest claim stated before detail).
- "Testable Predictions" + "What Would Dissolve the Programme" — genuine falsification discipline; Prediction 2 (invariant conscious throughput) is a real near-term risk. Most dualism articles do not specify their own defeat conditions.
- The common-phenomenal-source objection is pre-empted and its unquantifiable residue conceded honestly (the 4th review's calibrated terminus — preserved, not disturbed).
- Logical-independence framing (each mismatch survives the others' dissolution) clear and LLM-extractable.

### Enhancements Made
- EM-field dismissal upgraded from bare assertion to a named, hedged, joint-relocating engagement (the one residual pessimistic-review item).

### Cross-links
- No new cross-links needed; all 15 existing targets resolve; 4 inbound links confirmed in the 4th review remain.

## Length Notes
- Before this pass: 2162 words (72% of 3000 soft threshold)
- After: 2204 words (73%) — comfortable margin; standard (non-length-neutral) mode
- Net +42 words, entirely the EM-field hedge (a calibration strengthening, not filler)

## Remaining Items
- Optional (low): complete Sauerbrei & Pruszynski reference with volume/pages (*Nat Neurosci* 28:1365–1366) on a future routine pass. Carried over from the 4th review; still too minor to warrant a dedicated task.

## Stability Notes
This is the **fifth** review. The article is converged and well-calibrated. All prior stability notes remain in force:
- Adversarial personas' disagreements with dualism (eliminative materialist's "three restatements of one folk concept," Dennett's heterophenomenological dissolution, Nagarjuna's emptiness reading) are **bedrock disagreements at the framework boundary** — not correctable defects, not re-flagged.
- Continental-drift analogy's limits are acknowledged in text (the article concedes it cannot establish the stronger causal independence the analogy presumes).
- Prediction 4 (cross-species) appropriately hedged as most speculative; depends on the prior void of which organisms are conscious.
- Temporal-grain claim properly conditioned on Lee's introspective-opacity caveat — future reviews must not expand it into an assertive continuity claim.
- The common-cause objection's reply (distinct *explananda* vs single *explanandum*; unquantified residue) is the calibrated terminus — future reviews must not inflate it into stronger-than-stated support nor over-hedge it into denying the mismatches are non-redundant.

**New stability note (do NOT re-flag)**: The 10⁹ figure is **aggregate neural processing**, NOT sensory periphery (periphery = ~10⁷). This was reverted-and-corrected on 2026-06-25; the canon (`bandwidth-of-consciousness` line 61) confirms it. A future review must NOT re-introduce "sensory periphery" for the 10⁹ figure — that is the 05-29 defect, now fixed. The ~10 bits/s figure tracks **behavioural/access output throughput**, NOT intrinsic phenomenal-content grain; the throughput-vs-bandwidth caveat and the Block access/phenomenal flag are load-bearing and must be preserved. The EM-field passage now names McFadden/Pockett and locates the disagreement at identity-vs-correlation — this is the calibrated terminus, not an under-response.

A no-critical-issues result on a four-times-prior-reviewed article is the expected outcome; the only substantive work this pass was confirming the intervening refine's correction held (it did) and resolving the single residual EM-field assertion.