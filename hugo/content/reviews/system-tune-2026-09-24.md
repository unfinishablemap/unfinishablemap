---
ai_contribution: 100
ai_generated_date: 2026-09-24
ai_modified: 2026-09-24 00:00:48+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-09-24
date: &id001 2026-09-24
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-24 00:00:48+00:00
modified: *id001
related_articles:
- '[[todo]]'
- '[[changelog]]'
title: System Tuning Report - 2026-09-24
topics: []
---

# System Tuning Report

**Date**: 2026-09-24
**Sessions analysed**: session_count 21204, cycle_position 13824 (since the 2026-09-19 run at session 20966, cycle_position 13680)
**Period covered**: 2026-09-19T17:10 to 2026-09-24T00:00 UTC

## Executive Summary

No abort condition was met, and no Tier 1 change was applied. This is the fourteenth run in a row with no Tier 1 change. The cause is unchanged: `evolution-state.yaml` has no `cadences`, `overdue_thresholds`, `locked_settings` or replenishment-weight fields, so none of the three permitted automatic change types has a setting to act on. Since 09-19 the system has improved in one way: `expand-topic` has started running again. Three things have got worse: the NEEDS-HUMAN backlog, coalesce's run of no-ops, and reports-only priority lists that nobody acts on. This run also fired only 4.3 days after the last one, because the 30-day minimum-age gate does not apply under `/unfin-cycle`.

## Abort conditions: none met

| Condition | Measured | Status |
|---|---|---|
| >50% of last 10 tasks failed | `recent_tasks`: 19/20 `success`, 1 `failed` (agentic-social, 09-23) | pass |
| `quality.critical_issues > 0` | 0 | pass |
| File read errors | none | pass |
| Convergence regressed 3+ sessions | article counts rising in every section (below) | pass |

**Locked settings**: `locked_settings` is absent. Nothing is locked, but nothing can be tuned either.

## Metrics Overview

| Metric | Current (09-24) | Previous (09-19) | Trend |
|--------|---------|----------|-------|
| session_count | 21204 | 20966 | +238 |
| Recent-task failure rate | 1/20 (5%) | 0/20 | ↑ (one Moltbook verification) |
| `failed_tasks` | {} | {} | → |
| Changelog `Status: Failed` | 0 | 0 | → |
| topics / cap (`count_section_files`) | 329 / 360 | 328 / 360 | +1 |
| concepts / cap | 327 / 360 | 326 / 360 | +1 |
| voids / cap | 103 / 115 | 103 / 115 | → |
| positions / cap | 22 / 80 | 21 / 80 | +1 |
| apex | 44 | 43 | +1 |
| Queue P2 / P3 (`queue_status`) | 8 / 88 | 8 / 88 | → (stale: last replenish 09-09) |
| NEEDS-HUMAN open / ever closed | 75 / 1 | 70 / 1 | ↑ |
| `quality.medium_issues` (target 3) | 10 | 10 | → |

Note on the caps: `count_section_files` lives in `tools/evolution/state.py:347`. The caps in `evolution-state.yaml` (`section_caps`) are 360/360/115/80. The table in CLAUDE.md still says 320/320/100/80.

## Findings

### Cadence Analysis

- **No cadence configuration exists** (grep for `cadence`, `overdue_threshold`, `locked_settings` and `weight` in `evolution-state.yaml` finds only prose inside earlier notes). Scheduling is hard-coded in `tools/evolution/cycle.py` and `time_trigger.py`. This finding is carried from the 09-19 report (T1).
- **tune-system over-fires.** Five reports in 20 days (09-04, 09-08, 09-11, 09-17, 09-19) and now 09-24, against the skill's monthly intent. There are 90 `system-tune-*` reports in total. Cause, as recorded 09-17: `filter_triggers_by_min_age()` is only called on the `evolve_loop.py` path, and `/unfin-cycle` drains triggers without it. Fixing this means changing Python (Tier 3).
- `add-highlight-tweet` has not run since 2026-08-20 (35 days), while `add-highlight` runs daily. See the X API item below.
- `validate-all` last ran 2026-01-24 (243 days ago). Carried.

### Failure Pattern Analysis

- **agentic-social / Moltbook verification**: one `failed` outcome on 09-23. The 09-17 run counted 5 lost posts across 4 challenge shapes since 08-22. With this one there are **6 or more verification losses in about a month**. That clears the 3-occurrence threshold for "verification failure" as a class, though not for any single shape (I did not re-classify this one's shape). Any fix belongs in the solver code or SKILL.md, so it is Tier 3.
- **X/Twitter API 402 (credits depleted)**: the driver reports this happened on today's add-highlight tweet, and the 09-19 report (T3) already recorded the same outage. That makes at least two observed occurrences. Highlights still get added and pushed, and only the tweet fails. It is an account or billing issue, not something a tunable can fix (Tier 3).
- No other failure pattern. `failed_tasks` is empty.

### Queue Health Analysis

- `replenish-queue` has not run since 2026-09-09 (15 days). `replenishment_source_counts` still shows only `promotion_from_p3: 6`, and every organic source is at 0. The 09-17 root cause still stands: `count_p0_p2_tasks` counts blocked P2s, so the floor check never fires (Tier 3, Python).
- todo.md holds 19 `### P2` and 147 `### P3` headers. The raw header counts include resolved and blocked entries, so they are upper bounds. `queue_status` (8/88) has not been refreshed since 09-09.
- **Coalesce**: **15 consecutive abandons** (changelog 09-23 19:46), up from 10 on 09-19. Its screens across three different methods (affordability × mutual link, title-family, cross-section same-subject) all end in reasoned declines. The candidate pool is used up because the articles divide the subject matter by role, and the Map's articles are deliberately split that way. Coalesce takes 2 of every 24 cycle slots, about 8% of scheduled capacity, and produces nothing. Reallocating slots changes the cycle's composition, so it is Tier 2 (below).

### Review Finding Patterns

- **Reports-only priority lists are not acted on unless a driver mints tasks from them.** Tenet check 138 (`reviews/tenet-check-2026-09-23`) found **0 of 4** of check 137's priority items repaired or queued after 3 days. The 09-08 cycle fixed 4 of 4 when a driver minted from the list. The 09-17 run recorded the same pattern (09-14 item 1 closed, items 2–5 unmoved). That is 3 or more reviews showing the same pattern, so the evidence threshold is met. The remedy is a skill-instruction change or a driver-side minting step, so it is Tier 3.
- The 09-19 report's R3 recommendation (write the ~4-item cap into the reports-only skills) has not been applied. Applying it is also Tier 3.

### Convergence Progress

- Every content section except voids grew by one article since 09-19. `expand-topic` ran on 09-21 and 09-23 after a 12-day gap, so the 09-19 R1 concern (article creation stalled) is **partly resolved**.
- `task_chains.pending_articles` now holds voids notes, including `voids-mirth-void-2026-09-23`. Voids has 12 free slots.
- `quality.medium_issues` is still 10 against a target of 3. No tool writes this field, so it may be stale. Carried as a Tier 3 question.

## Changes Applied (Tier 1)

*No changes applied.* None of the three Tier 1 change types (cadence ±2d, overdue threshold ±2d, replenishment weight ±20%) has a matching setting in any config file. `replenishment_source_counts` is a counter, not a weight. Creating new config sections is a design decision for a human (Tier 3), not a tuning adjustment, so applying nothing is the correct conservative outcome. The only Tier 1 change on record is still the 2026-07-15 `queue_status` prune, so no cooldown was involved.

## Recommendations (Tier 2)

### R1. Reassign coalesce's 2 cycle slots (renewed, stronger evidence)
- **Proposed change**: in `tools/evolution/cycle.py`, move coalesce's 2/24 slots to `deep-review` (or to queue). An alternative is to keep one slot and gate it on a cheap candidate precheck that skips without using up the slot.
- **Rationale**: 15 consecutive reasoned declines, up from 10 at the last report, across three distinct screening methods.
- **Risk**: Low to Medium. It changes the cycle's composition, and coalesce can be restored if section pressure rises past ~95%.
- **To approve**: edit the slot table in `cycle.py` and update the "24-slot task cycle" list in CLAUDE.md.

### R2. Have the driver mint from reports-only priority lists
- **Proposed change**: after `check-tenets`, `pessimistic-review` and `optimistic-review`, the cycle driver mints one `refine-draft` per priority row, with a cap of about 4. Check 138 names eight unqueued targets and recommends minting all of them.
- **Rationale**: 4/4 fixed when minted versus 0/4 and 0/8 when not.
- **Risk**: Low. Each task targets one article whose defect has already been verified.
- **To approve**: add a post-step to the `/unfin-cycle` handling for those three skills, or mint check 138's list by hand now.

### R3. Refresh the stale CLAUDE.md section-cap table
- **Proposed change**: update the table to 360/360/115/80, with the current counts 329/327/103/22, and correct the `count_section_files` path to `tools/evolution/state.py`.
- **Risk**: Low. Documentation only. It was not done automatically because CLAUDE.md is operator-maintained guidance.

No P3 tasks were added to todo.md. The queue already holds about 88 P3s that the loop never selects, so adding more would not get anything done. R2 is the fix for that.

## Items for Human Review (Tier 3)

### T1. Create `cadences` / `overdue_thresholds`, or rewrite this skill to match reality (carried, 2nd report)
- **Issue observed**: the tuning surface this skill is built around does not exist, which has produced 14 consecutive runs with no change.
- **Why human needed**: this is a config and design decision, and it would mean changing SKILL.md.
- **Suggested action**: either add the sections and wire `cycle.py`/`time_trigger.py` to read them, or change tune-system to report on the scheduling constants in code.

### T2. Enforce the tune-system min-age gate on the `/unfin-cycle` path
- **Issue observed**: the skill is monthly but ran at about 4-day intervals (six runs in 20 days). Each run costs a full slot and mostly re-derives the previous report.
- **Suggested action**: call `filter_triggers_by_min_age()` in `cycle_pick.py` or `cycle_post.py` as well as in `evolve_loop.py:1370`.

### T3. Fix `count_p0_p2_tasks` so blocked tasks do not count
- **Issue observed**: replenish has been idle for 15 days because blocked P2s hold the floor count at 3 or more. This was identified 09-17 and has not been fixed.
- **Suggested action**: add a one-line status filter in `task_selector.py`.

### T4. X API credits depleted (carried from 09-19 T3)
- **Issue observed**: tweets return 402. `add-highlight-tweet` last succeeded 2026-08-20.
- **Suggested action**: top up the X API credits or retire the tweet path. Until then, one highlight goes untweeted each day, and the failure only shows in `recent_tasks`.

### T5. Moltbook verification losses (6 or more since 08-22)
- **Suggested action**: review the challenge solver against the failed shapes listed in the agentic-social memory notes. One stricter parsing rule may cover several shapes.

### T6. NEEDS-HUMAN backlog: 75 open, 1 ever closed (carried from 09-19 T2)
- **Issue observed**: 5 more opened in 5 days, none closed.
- **Suggested action**: run a triage session, or restrict escalation to items that block work.

### T7. `quality.medium_issues` 10 vs target 3 (carried)
Decide whether the target or the metric is stale. No tool in `tools/` writes this field.

## Next Tuning Session

- **Recommended**: 2026-10-24 (30 days). This assumes T2 is fixed. If it is not, the next run will fire within days and should record only what has changed.
- **Focus areas**: whether coalesce slots were reassigned; whether check 138's list was minted; whether replenish ran again after T3; whether X credits were restored; whether `cadences` was created.