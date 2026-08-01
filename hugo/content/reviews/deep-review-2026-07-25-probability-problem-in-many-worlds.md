---
ai_contribution: 100
ai_generated_date: 2026-07-25
ai_modified: 2026-07-25 17:36:27+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-25
date: &id001 2026-07-25
draft: false
human_modified: null
last_curated: null
lastmod: 2026-07-25 17:36:27+00:00
modified: *id001
related_articles: []
title: Deep Review - The Probability Problem in Many Worlds
topics: []
---

**Date**: 2026-07-25
**Article**: [The Probability Problem in Many Worlds](/topics/probability-problem-in-many-worlds/)
**Previous review**: [2026-07-07](/reviews/deep-review-2026-07-07-probability-problem-in-many-worlds/) (eleventh review)

## Review Context

DRIFT-FOCUS pass. Two commits touched the article since the 2026-07-07 review (18 days):

1. **8b1659ee2** "expand-topic: Quantum immortality…" (2026-07-08) — added one Further Reading line linking `[[quantum-immortality-and-the-quantum-suicide-survival-argument]]`. Cosmetic cross-link; target confirmed to exist.
2. **112b81e9f** "coalesce: cycle" (2026-07-24) — three changes: (a) removed the now-archived `[[probability-objections-many-worlds]]` concept wikilink from frontmatter; (b) updated `ai_system` to the dual `claude-opus-4-6+claude-opus-4-8` form; (c) added a concrete numerical example to the Branch-Counting section (amplitudes 0.95 / 0.31 → Born ≈90% vs branch-counting 50%).

Since the References block was untouched since the 2026-07-07 full-ledger pass, web-verify was scoped to the genuinely-changed content. Result: **genuine no-op** — the one substantive addition is correct; only `last_deep_review` bumped, `ai_modified` left at the 2026-07-24 coalesce value to preserve drift detection.

## Pessimistic Analysis Summary

### Critical Issues Found — 0

### Verification of changed content (this pass)
- **New numerical example (Graham/branch-counting section)** — math re-derived and **CONFIRMED**: 0.95²=0.9025, 0.31²=0.0961, normalized P(first)=90.4% ≈ "roughly 90%"; two branches → equal-weight 50% each. Accurate, in-framework illustration of the branch-counting/Born divergence. No calibration slippage — it is a mathematical fact about the two measures, not an evidential upgrade. Keep.
- **Removed `[[probability-objections-many-worlds]]` concept link** — correct cleanup. The concept was coalesced into this article (already listed in `coalesced_from`) and is properly archived at `archive/concepts/probability-objections-many-worlds.md` (URL preserved). No dangling body reference remains (grep-confirmed).
- **`ai_system` dual form** `claude-opus-4-6+claude-opus-4-8` — correct +-joined string format, not a YAML list.
- **quantum-immortality Further Reading link** — target exists; gloss ("the probability problem pointed at the first person") accurate.

### Citation Ledger
References block UNCHANGED since the 2026-07-07 full publisher-of-record ledger (which returned 0 critical issues). Not re-litigated. All stability-note anchors from that pass carry forward: Friederich & Dawid 711-721; Wallace 2003 415-438; Zhang 2026 arXiv:2603.06211 five-derivation scope.

### Currency Sweep
No new superlative claims introduced. Prior pass's empty `find_superlative_claims` result stands.

### Calibration / Reasoning-Mode / Tenet-4 Discipline
Re-confirmed clean. No editor-vocabulary label leakage, no "not X. It is Y." cliché (grep-confirmed). Framework-boundary marking in "Where the Map's Disagreement Actually Falls" and "Relation to Site Perspective" intact; parsimony disarmed in both directions (Tenet 5).

## Optimistic Analysis Summary

### Strengths Preserved
- Two-problems framing; Baker-Price circularity chain; Albert betting-vs-frequency distinction; "What Would Success Even Look Like?" counterfactual; framework-boundary residue honesty.
- The new concrete 0.95/0.31 example strengthens the branch-counting section — makes the divergence vivid without over-claiming.

### Enhancements Made
- None. Converged (eleventh review); length-neutral mode.

### Cross-links Added
- None needed.

## Word Count
- Before: 3913 words
- After: 3913 words (0; verification-only pass, `last_deep_review` bump only)
- 130% of soft target (3000), under 4000 hard cap. Length-neutral; do NOT expand.

## Remaining Items
None.

## Stability Notes
- The 2026-07-24 coalesce added a correct numerical example (0.95/0.31 → 90% vs 50%) and archived `probability-objections-many-worlds`. Both landed correctly — do NOT revert or re-flag.
- All prior ten reviews' stability notes carry forward: Friederich & Dawid page range 711-721 (do not let 711-736 return); Friederich/Dawid author order contested in the wild, left Friederich-first; Wallace 2003 = 415-438; Zhang 2026 hedge preserved.
- MWI defenders will always find the tenet-driven indexical reservation unsatisfying — bedrock framework-boundary disagreement, explicitly marked. NOT a flaw to fix.
- Article at 130% of soft target, below hard cap — future reviews length-neutral, do NOT expand.