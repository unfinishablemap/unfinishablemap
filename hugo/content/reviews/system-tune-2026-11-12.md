---
ai_contribution: 100
ai_generated_date: 2026-11-12
ai_modified: 2026-11-12 12:19:15+00:00
ai_system: claude-fable-5-2
author: null
concepts: []
created: 2026-11-12
date: &id001 2026-11-12
description: 'Twenty-seventh consecutive zero-Tier-1 tune-system run: no cadence or
  threshold keys exist to adjust; health green; topics and concepts are both at cap,
  so the new-article pipeline now runs through voids only.'
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-12 12:19:15+00:00
modified: *id001
related_articles:
- '[[todo]]'
- '[[changelog]]'
title: System Tuning Report - 2026-11-12
topics: []
---

# System Tuning Report

**Date**: 2026-11-12
**Sessions analyzed**: the 20 entries in `recent_tasks` plus the changelog since the 2026-11-09 report
**Period covered**: 2026-11-09 09:50Z to 2026-11-12 12:18Z

## Executive Summary

The system is healthy. `failed_tasks` is empty, `quality.critical_issues` is 0 (medium 10, low 3, orphaned 0), and all 20 `recent_tasks` entries are `success`. No abort condition holds.

This is the twenty-seventh consecutive run with no Tier 1 change. `cadences`, `overdue_thresholds`, `locked_settings` and replenishment weights are still absent from `evolution-state.yaml`, so the skill has no setting it is permitted to change. The run fired three days after the last one; the 30-day cadence the skill describes is not what triggers it (it runs every six completed cycles).

The one new structural fact: `topics/` reached its cap today (370/370) and `concepts/` was already there (370/370). New articles can now land only in `voids/` (118/125) and `positions/` (28/90).

## Metrics Overview

| Metric | Current | 2026-11-09 | Trend |
|--------|---------|-----------|-------|
| Failure rate (recent_tasks) | 0% (0/20) | 0% | → |
| Critical issues | 0 | 0 | → |
| topics / concepts / voids / positions | 370/370, 370/370, 118/125, 28/90 | topics below cap | topics now full |
| Open tasks above the Completed marker | 399 (P1 2, P2 22, P3 375) | — | — |
| Open tasks by status | 341 pending, 43 blocked, 42 needs-human | — | — |

Counts are of task headers and Status lines above `## Completed Tasks`; a few headers there carry a completed or done status, so the totals do not sum exactly.

## Findings

### Cadence Analysis

No cadence keys exist. Wall-clock triggers ran on schedule in the window: the three commissions at 02:05Z, 03:06Z and 04:06Z on 11-12, all three collects, the synthesis at 05:01Z, the highlight at 08:08Z, and harvest at 06:33Z. `replenish-queue` last ran 2026-09-29 and `skip-queue-slot` 2026-09-28: the queue has not dropped below its replenish gate for six weeks, which matches 22 open P2s.

### Failure Pattern Analysis

No failures. One driver error is worth recording because an earlier draft of this session's notes read it as a code defect: a hand call to `chain_new_research_notes` raised `KeyError: 'voids'`. The cause was the caller passing the raw `section_caps` block (keys `max_topics`, `max_concepts`, `max_voids`). `cycle_post.py` (L404–409) builds the argument correctly as `{"topics": ..., "concepts": ..., "voids": ...}`, so the function and its production caller agree. No code change is needed for that.

What remains true is the gap carried from 11-03 and 11-09: `cycle_post` calls the chain only when `kind == "queue"` and `skill == "research-topic"`. A `research-voids` run posts as `kind=trigger`, so its note never reaches the chain. Today's `voids-wakefulness-void-2026-11-12` note (verdict `article`) again needed a hand-mint.

### Queue Health Analysis

- **Capped sections.** Above the Completed marker there are 11 `expand-topic` tasks and 5 `research-topic` tasks. At least two expand tasks target full sections (`concepts/collapse-priority-problem`, `topics/boltzmann-brains-without-a-zombie-shield`). `cycle_pick` still offers such tasks; the expand skill then refuses. The harvester only mints for `topics`/`concepts`, so every research task it creates from now on leads to an article that cannot be placed. Research notes still have value as fold or refine sources, but the `article` verdict is a dead end for those two sections until a slot opens.
- **Coalesce.** Of the 37 coalesce entries in the changelog, 2 report a merge; the latest abandon entry counts its 40th consecutive no-candidate run. The two cycle slots (8% of the cycle) cost a fork each and return nothing. With both main sections at cap, coalesce is also the only automated route to a free slot, so the slot matters more while the candidate search finds less.
- **P3 backlog.** 375 open P3s against 22 P2s. Queue slots take P0–P2 first, so P3 work is reached only when P2 drains, which it has not done since September.

### Review Finding Patterns

Check 164 (today) found 0 errors and 6 warnings; five of the six are an older sentence left standing beside a line a recent edit calibrated. The same shape appeared in check 163, whose three tasks are still pending. Fixes are landing on the sentence a review names and leaving its neighbours, which is a brief-writing matter for refine tasks and not a setting.

### Convergence Progress

All `convergence_targets` minima were passed long ago; `max_medium_issues: 3` is exceeded (10) and has been in every recent report. Pages at or over their hard length gate, by `analyze_length` with sidecars excluded:

| Section | Pages | At or over hard |
|---|---|---|
| topics | 369 | 27 |
| concepts | 370 | 16 |
| voids | 118 | 19 |
| apex | 44 | 10 (9 excluding the `apex-articles` index) |
| positions | 28 | 10 |

These are totals including reference lists and embed boilerplate, so the count overstates how many pages have over-length prose. Seven condense tasks are open.

## Changes Applied (Tier 1)

*No changes applied.* No adjustable setting exists.

## Recommendations (Tier 2)

### 1. Decide what the article pipeline does while topics and concepts are full
- **Proposed change**: one of (a) raise the two caps, (b) let the harvester and `cycle_pick` skip article-bound work for full sections, or (c) accept research-only output with fold/refine verdicts until coalesce or archiving frees slots.
- **Rationale**: without a decision, research tasks keep being minted and picked for articles that cannot be created.
- **Risk**: Low for (b) and (c); (a) is an editorial choice.

### 2. Run the research chain for research-voids output (carried from 11-03, 11-09)
- **Proposed change**: extend the `cycle_post` chain condition to `kind == "trigger"`, `skill == "research-voids"`.
- **Rationale**: voids is the only section with article headroom, and its notes are the only ones not chained.
- **Risk**: Low.

### 3. Gate the coalesce slot on a cheap precondition (carried)
- **Proposed change**: skip the slot when no article has been added or removed since the last no-candidate run, or cut the allocation from 2 slots to 1.
- **Rationale**: 2 merges in 37 logged runs.
- **Risk**: Low.

### 4. Agentic-social selector (carried from 11-03, 11-09)
- No new evidence gathered this run; the item stands as written on 11-09.

## Items for Human Review (Tier 3)

- **Tune-system trigger.** The skill text says monthly; the trigger is every six cycles and has produced 27 no-change reports. Either give it settings to tune or lengthen the trigger.
- **`apex/post-decoherence-selection-programme` at 4,996/5,000** after today's reciprocal link; it cannot take another sentence without a condense.
- **43 blocked and 42 needs-human tasks** sit above the Completed marker and are invisible to the replenish gate's count.
- **Still open from earlier reports**: the items listed under the same heading on 11-09.

## Next Tuning Session

- **Recommended**: when a cadence or weight setting exists, or 2026-12-12.
- **Focus areas**: whether capped-section research tasks are stalling; whether the research-voids chain is still hand-minted.