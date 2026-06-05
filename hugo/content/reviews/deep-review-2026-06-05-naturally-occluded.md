---
ai_contribution: 100
ai_generated_date: 2026-06-05
ai_modified: 2026-06-05 00:00:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-05
date: &id001 2026-06-05
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[naturally-occluded]]'
- '[[three-kinds-of-void]]'
- '[[apex/taxonomy-of-voids]]'
- '[[fitness-beats-truth]]'
- '[[possibility-probability-slippage]]'
- '[[evidential-status-discipline]]'
title: Deep Review - Naturally Occluded
topics: []
---

**Date**: 2026-06-05
**Article**: [Naturally Occluded](/concepts/naturally-occluded/)
**Previous review**: [2026-05-16](/reviews/deep-review-2026-05-16-naturally-occluded/) (plus cross-review [2026-05-16c](/reviews/deep-review-2026-05-16c-cross-review-naturally-occluded/))
**Word count**: 2935 → 2947 (+12; length-neutral, soft_warning preserved, well under 3500 hard)

## Context: Why This Review Found Real Issues

The article was first-review-stable on 2026-05-16. On **2026-05-19 a coalesce** merged `concepts/adaptive-cognitive-limits/` into this page, adding ~430 words (the "Extensions Beyond Perception" restructure, a new Rancourt 2025 result, the McGinn "architectural closure as adaptive product" bullet, and the "Detection Methods" section). The coalesce bumped `last_deep_review` to 2026-05-19 **without the merged content ever passing a deep review** — so this content was effectively unreviewed despite the timestamp. This pass scrutinised the coalesce-introduced material specifically and found three correctable defects, one of which was a regression of an issue the 2026-05-16 review had already resolved.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Count mismatch introduced by coalesce** (line 69): the lead of "Extensions Beyond Perception" read "**Four** independent results converge," but the section lists **five** bolded results (Heuristic simplification, Strategic self-opacity, Negative information value, Epistemic virtue of limitation, Architectural closure as adaptive product). The coalesce added the Rancourt and McGinn items without updating the count. **Resolution applied**: changed to "Five further results converge…" (also clarifies these are *further* results beyond the FBT perceptual anchor, which is no longer one of the bullets).

- **Attribution regression reintroduced by coalesce** (line 73): the bullet read "**Robert Trivers** argues that self-deception evolved…" with the citation "(von Hippel & Trivers 2011)" — von Hippel is first author of the cited paper. The 2026-05-16 review had explicitly fixed this exact single-author framing ("Robert Trivers' analysis" → "von Hippel and Trivers"); the coalesce drew the bullet from the adaptive-cognitive-limits source and reverted it. **Resolution applied**: "Von Hippel and Trivers argue…" — restores byline-order attribution match.

- **FBT dominance overstatement / lead-body inconsistency** (line 45, pre-existing): the lead said fitness-tuned strategies "**strictly dominate** veridical ones," but the body (line 63) correctly states "**equal or higher** expected fitness." The FBT theorem proves *weak* dominance (≥), with truth-tuned perceptions *generically* (not universally) driven to extinction in the Monte Carlo runs. "Strictly dominate" both overstates the formal result and contradicts the article's own accurate body statement. **Resolution applied**: lead now reads "do at least as well as veridical ones and generically drive them to extinction" — matches the theorem and the body.

### Medium Issues Found

None requiring action. The McGinn "Architectural closure as adaptive product" bullet folds an *Unexplorable*-flavoured result under an "adaptive extensions" banner, but the bullet itself flags this honestly ("sits at the boundary between adaptive and architectural limits… suggesting the two categories overlap"), consistent with the article's own non-exclusivity claim (line 59). Not a calibration error.

### Possibility/Probability Slippage Check

PASSES. The new content is appropriately hedged. The McGinn overlap claim uses "suggesting"; "AI probes" uses "may reveal"; the Rancourt result is an epistemic-agency claim, not a tier-upgrade. The tier-stratified calibration burden section (formal-perception *strongly supported* / extensions *realistic possibility, contested* / catalogue assignments *live hypothesis*) survives the coalesce intact. The diagnostic test ("would a tenet-accepting reviewer flag any claim as overstated?") answers NO across the article after the three fixes above.

### Attribution Check (new content)

- **Rancourt, B. T. (2025). The virtue of ignorance: How epistemic agency needs cognitive limitations. *Southern Journal of Philosophy* 62.** — VERIFIED via web search. Author, title, journal, volume, thesis, and the quoted phrase ("considering all possible doubt, leaving a tractable space of possibilities") all match the published article (DOI 10.1111/sjp.12588, North Carolina State University). Sound.
- McGinn (1989) cognitive closure — correct, ref #6 present.
- All other citations carried over from the prior review's verification (Hoffman/Singh/Prakash, Prakash et al., Todd & Gigerenzer, von Hippel & Trivers, Field & Bonsall, Rebouillat et al.) — unchanged and previously verified.

### Counterarguments Considered

No change from the 2026-05-16 review's bedrock-disagreement findings (eliminativist, Dennett, Tegmark/Deutsch, Popper, Nāgārjuna). All remain at the framework boundary and are NOT re-flagged. See Stability Notes.

### Engagement Mode Classifications

No named-opponent counterargument engagements. McGinn is used as honest extension/boundary-marking, not refutation. No label leakage in prose. Unchanged from prior review.

## Optimistic Analysis Summary

### Strengths Preserved (Do Not Change)

- The four "commits to:" parallel paragraphs (lines 51-57) — clean inspectable taxonomy.
- The bounded-anchor discipline at the perceptual layer (line 65).
- The tier-stratified calibration burden (lines 109-121) with three named falsifiability classes.
- "A cognitive wall announces itself through frustration; an adaptive limit disguises itself as adequacy" (line 103) — load-bearing aphorism.
- The bootstrapping treatment in Relation to Site Perspective (line 145) — substantive, not a wave-away.
- The coalesce's "Distinctive Phenomenology" + "Detection Methods" additions are genuine value from the merged adaptive-cognitive-limits page; they integrate cleanly.

### Enhancements Made

Three length-neutral corrections (count, attribution, dominance wording). No expansion — article is at soft_warning and mature.

### Cross-links Added

None. Cross-link density already high and appropriate.

## Remaining Items

None.

## Stability Notes

The article is at **post-coalesce-stable** state. The 2026-05-19 coalesce was the substantive change since first review; its three defects are now resolved. Future reviews should treat the four-kinds extension and the absorbed adaptive-cognitive-limits content as editorial commitments, not open questions.

Bedrock disagreements that must NOT be re-flagged as critical (carried from 2026-05-16):
- Eliminativist rejection of the dualist framework the category presupposes.
- MWI/Tegmark objection to tenet 2 and the Stapp-engagement reading (held at *live hypothesis* — the most calibration-honest position available).
- Popper-style "evolutionary explanations are unfalsifiable" — partially addressed via the three falsifiability classes; residual concern honestly bounded.
- Nāgārjuna-style objection to the "selecting for" causal-agent framing.

Convergence note: the recurring lesson here is that a **coalesce can bump `last_deep_review` without the merged content being reviewed**, and can **regress a previously-fixed issue** (the Trivers attribution). When an article's `last_deep_review` was last set by a coalesce/refine commit rather than an actual deep-review run, scrutinise the merged content specifically — the timestamp understates the review debt.