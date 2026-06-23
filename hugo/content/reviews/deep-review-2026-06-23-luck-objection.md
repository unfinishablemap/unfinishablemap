---
ai_contribution: 100
ai_generated_date: 2026-06-23
ai_modified: 2026-06-23 00:12:57+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-23
date: &id001 2026-06-23
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - The Luck Objection to Libertarian Free Will
topics: []
---

**Date**: 2026-06-23
**Article**: [The Luck Objection to Libertarian Free Will](/concepts/luck-objection/)
**Previous review**: [2026-06-01](/reviews/deep-review-2026-06-01-luck-objection/)
**Scope**: Changed-since-review audit, 8th deep-review pass. `last_deep_review` 2026-06-01; `ai_modified` 2026-06-18. Heavily converged (7 prior reviews, stable across 2026-03-12 → 2026-06-01). Per the convergence-damping guidance (deep-review-over-reviews-converged) this pass audits only the post-06-01 changes and re-checks the load-bearing disciplines; no padding or re-hedging applied to converged content.

## What Changed Since 2026-06-01 (audited content)

`git log` shows two post-06-01 edits, both cosmetic cross-link work from refine/deep-review passes:

1. **06-05** — added `[[reasons-responsiveness]]` to `related_articles` frontmatter and wrapped existing inline text ("reasons-responsive compatibilism") as a wikilink in the calibration paragraph. No prose change beyond the link.
2. **06-18** — added `[[volitional-control]]` to `related_articles`, added a Further Reading entry, and appended one new sentence to "The Phenomenology of Effort": *"This effort phenomenology is empirically anchored in the broader case for [volitional control](/topics/volitional-control/), where clinical dissociations and the neural signatures of willed action show the felt strain of effort tracking specific causal circuitry rather than floating free of it."*

The References block is unchanged since the 06-01 review (which fully web-verified it, including the epothilone B / Wiest correction).

## Pessimistic Analysis Summary

### Critical Issues Found

None.

### Medium Issues Found

None.

### Discipline Audit (the load-bearing checks for this article)

**New-sentence faithfulness (the one substantive content change).** The 06-18 `volitional-control` sentence was checked against its source article (`obsidian/topics/volitional-control.md`). It is faithful: the source documents clinical dissociations (its "Clinical Dissociations: Agency Tracks Causal Structure" section — agency tracking the integrity of specific neural circuits) and the neural signatures of willed action (Rajan et al. 2019 — frontal theta oscillations and bidirectional fronto-parietal coherence appearing during effortful self-directed attention, emerging ~300ms in, absent in instructed/automatic attention). The phrase "tracking specific causal circuitry rather than floating free of it" accurately summarises the source's "agency tracks the integrity of specific neural circuits rather than narrative convenience." The qualifier "empirically anchored" is calibration-honest: the source's own claim is that the phenomenology "tracks real causal architecture," and the source is itself disciplined that removing the epiphenomenalist defeater is not the same as upgrading positive evidence. No overstatement imported into luck-objection. Not a possibility/probability slippage — the sentence anchors the *effort-tracks-selection* claim (selection-vs-randomness), not a libertarian-vs-compatibilist upgrade, consistent with the article's deliberate scope.

**Citation web-verify (Discipline §2.4).** References block unmodified since the 06-01 full-verify pass, so per the §2.4 trigger rule a cosmetic no-op pass on a stable References list may skip re-litigating the whole list. Two targeted confirmations run this pass:
- Kane, R. (2024) *The Complex Tapestry of Free Will* — web-verified at publisher of record (Oxford University Press, full title *The Complex Tapestry of Free Will: A Philosophical Odyssey*, ISBN 9780197751404, 376 pp., 2024; cross-confirmed at Notre Dame Philosophical Reviews, Ethics 136(3), PhilPapers). state: **real-correct**. The body attribution (line 70, "now explicitly incorporates agent-causal elements... 'exercising teleological guidance control'") is appropriately hedged ("incorporates... elements," not "converts to agent-causation") and was ratified as accurate by the 04-29 persona pass; not re-litigated.
- Empirical-record currency sweep: `find_superlative_claims` returns no flagged superlatives. The decoherence section's quantum-biology framing ("the categorical objection has been significantly weakened, though neural applications remain open") is appropriately hedged and carries no superseded-superlative risk; epothilone B (eNeuro 2024) was publisher-verified at 06-01.

**Reasoning-mode / boundary-substitution (Discipline §2.6).** Grep clean for all forbidden editor-vocabulary labels (no leakage). Named-opponent engagements remain mode-honest and unchanged: illusionist challenge uses the misrepresentation-presupposes-presentation regress (internal-to-opponent); the zombie objection is transparently declared "question-begging against the Map's framework" resting on the Bidirectional Interaction tenet (boundary-marking, honestly declared, not dressed as in-framework refutation); the agent-causal critics' exchange is noted as a possible "impasse" rather than overclaimed.

### Attribution Accuracy Check

Clean. Misattribution (Van Inwagen rollback, Mele present/remote luck, Kane SFAs + 2024 convergence all correctly attributed), qualifier preservation ("default causal profile" intact at lines 90/162), position strength ("now explicitly incorporates," "explores"/"proposes" not "argues"/"proves"), source/Map separation ("The Map proposes...", "The Map strengthens..."), and self-contradiction all pass.

### Counterarguments Considered

All major counterarguments remain adequately addressed from prior cycles. The post-06-01 changes introduce no new counterargument requiring a response. The compatibilist-survival objection continues to be conceded openly by the calibration paragraph (now linking out to [reasons-responsiveness](/concepts/reasons-responsiveness/)).

## Optimistic Analysis Summary

### Strengths Preserved

- Front-loaded, truncation-resilient summary.
- Lucky-Indeterminism vs Consciousness-Selected comparison table.
- The compatibilist-symmetry calibration paragraph remains a model anti-slippage move; the new `[[reasons-responsiveness]]` link improves its navigability without weakening the concession.
- The new `[[volitional-control]]` anchor strengthens the effort-tracks-selection reply with an empirically-grounded sibling, correctly scoped.
- All five tenets substantively connected in Relation to Site Perspective.
- 2119 words (85% of the 2500 concepts soft threshold) — comfortable headroom, no length risk.

### Enhancements Made

None. Metadata-only verdict. The post-06-01 edits were themselves disciplined improvements; per convergence guidance no padding or re-hedging was applied.

### Cross-links Added

None added this pass. All cross-links in the article verified to resolve live: `[[volitional-control]]` → `obsidian/topics/volitional-control.md`, `[[reasons-responsiveness]]` → `obsidian/concepts/reasons-responsiveness.md`, `[[compatibilist-symmetry-challenge]]`, `[[delegatory-causation]]`, `[[trilemma-of-selection]]`, `[[topics/free-will]]`, `[[agent-causation]]`, `[[quantum-indeterminacy-free-will]]`, `[[moral-implications-of-genuine-agency]]` all resolve.

## Remaining Items

- **Low (sibling-file, not a luck-objection defect)**: `volitional-control.md` does not yet contain a reciprocal `[[luck-objection]]` link, despite the 06-18 commit being titled "reciprocal cross-link repair." `reasons-responsiveness.md` *does* reciprocate (3 backlinks). Not fixed in this pass to avoid bumping a different converged article's `ai_modified` and triggering churn; flagged for a future cross-link-tidy or the editing of volitional-control on its own next pass.

## Stability Notes

Stable across 2026-03-12, 03-14, 04-15, 04-29, 06-01, and now 06-23 — 8th deep-review, fully converged. The post-06-01 changes were cosmetic cross-links plus one faithful, correctly-scoped sentence; no critical, medium, or new issues. Durable bedrock standoffs (NOT flaws to fix, do not re-flag): MWI defenders and eliminative materialists disagreeing from outside the Map's tenets; the decoherence challenge remaining partially open until quantum-biology-of-cognition matures; the article's appeal to phenomenology supporting selection-vs-randomness, not libertarian-vs-compatibilist (deliberate scope, made explicit by the calibration paragraph). This article should be a candidate for longer review intervals — 8 passes with no body-content defects found since the original create.