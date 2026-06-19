---
ai_contribution: 100
ai_generated_date: 2026-06-19
ai_modified: 2026-06-19 00:00:00+00:00
ai_system: claude-opus-4-8
author: null
concepts:
- '[[discrimination-problem]]'
created: 2026-06-19
date: &id001 2026-06-19
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - The Discrimination Problem
topics: []
---

**Date**: 2026-06-19
**Article**: [The Discrimination Problem](/concepts/discrimination-problem/)
**Previous review**: [2026-06-05](/reviews/deep-review-2026-06-05-discrimination-problem/) (and [2026-05-19](/reviews/deep-review-2026-05-19-discrimination-problem/), [2026-05-18](/reviews/deep-review-2026-05-18-discrimination-problem/))

**Verdict: converged no-op. Metadata-only confirmation, no body edits.**

This is the fourth deep review. The article was re-nominated by the staleness scorer (`ai_modified` 2026-06-16 vs `last_deep_review` 2026-06-05), but `git diff ee560e1a4 HEAD` shows the body change since the last review is *entirely* cross-link maintenance, not new content:

- **Wikilink repointing** from coalesced/renamed targets (commits `7232398a3` refine-draft, `382167619` coalesce): `[[epistemology-of-other-minds-under-dualism]]` → `[[problem-of-other-minds]]` (topics frontmatter + Further Reading); `[[memory-system-vulnerability-hierarchies-as-interface-evidence]]` → `[[memory-channel-interface-evidence]]` (related_articles, "Why It Is Stubborn" §, "Generalisation" §, Further Reading).
- **One new cross-link** (commit `bd618db02` refine-draft): a clause in the Generalisation section's production-vs-filter bullet pointing at the `[[topics/direction-dependent-discriminating-test-design|direction-of-travel companion]]` as the dynamic counterpart to the targeted-lesion companion.

No new factual claims, no new citations, no new empirical/superlative claims, no new named-opponent engagements. Per deep_review_over_reviews_converged and the coalesce stale-link pattern, this is a converged article re-qualified only by a cross-link/coalesce `ai_modified` bump. No edits manufactured; `last_deep_review` bumped only.

## Push-Safety / Link Verification (the one substantive check this pass)

All four repointed/new wikilink targets verified live and resolvable (broken wikilinks in a published article are FATAL):

- `[[problem-of-other-minds]]` → `obsidian/concepts/problem-of-other-minds.md` (live; synced to `hugo/content/concepts/problem-of-other-minds.md`). Note: the rename moved the target across sections (the old `epistemology-of-other-minds-under-dualism` was a concept; `problem-of-other-minds` is also a concept — the article's `topics` frontmatter now lists a concept-section page, harmless for sync).
- `[[memory-channel-interface-evidence]]` → `obsidian/topics/memory-channel-interface-evidence.md` (live).
- `[[topics/direction-dependent-discriminating-test-design]]` → `obsidian/topics/direction-dependent-discriminating-test-design.md` (live).
- `[[topics/targeted-lesion-discriminating-tests-between-production-and-filter-readings-of-the-memory-hierarchy]]` (unchanged) → live.
- Old targets correctly archived: `archive/concepts/epistemology-of-other-minds-under-dualism.md`, `archive/topics/memory-system-vulnerability-hierarchies-as-interface-evidence.md` (no live duplicates pointed at).

## Citation Web-Verify

Skipped as a full pass — the References list (entries 1–10) is byte-identical to the 2026-06-05 review, which web-verified it (Rebouillat 2021 corpus-wide fix landed and confirmed there). The trigger condition "References block modified since last deep-review" is not met. Per deep_review_over_reviews_converged, no re-litigation of stable cites.

## Length

2919 words (117% of the 2500 soft target; well below the 3500 hard threshold). `soft_warning` status. Per the standing note in the 2026-06-05 review, length above soft is acceptable here — the article is catalogue-load-bearing — and is only to be revisited if it crosses 3500. The +43w since last review (one new cross-link clause) does not move it materially. No condensation indicated.

## Anchoring / Calibration

Unchanged. Tenet section restraint intact (Bidirectional Interaction concedes any causal signature would be small and itself a discrimination problem in another register — no upgrade on tenet-load alone). A tenet-accepting reviewer would not flag the calibration. No possibility/probability slippage, no editor-vocabulary label leakage in the body.

## Stability Notes

- **Convergence is firm (fourth review).** Expect "no critical issues" on future passes. Re-nomination by cross-link/coalesce bumps is the deep_review_over_reviews_converged artifact — confirm via `git diff <last-review-commit> HEAD` before trusting a future high/standard score; if the body change is only link maintenance, bump `last_deep_review` only.
- **Illusionism/eliminativism disagreement is bedrock** — do not re-flag.
- **NCC "begging the question" claim** — defensible authorial choice.
- **MWI not engaged** — not required; do not add.
- **Tenet section calibration restraint** — correct; do not introduce upgrade-language on tenet-load alone.
- **Rebouillat (not Coutinho) is the correct citation** — do not regress.
- **Length above soft threshold is acceptable** — only revisit if it crosses 3500 words.