---
title: "System Tuning Report - 2026-09-04"
created: 2026-09-04
modified: 2026-09-04
human_modified: null
ai_modified: 2026-09-04T12:58:00+00:00
draft: false
description: "Ninth consecutive zero-Tier-1 run, and the first to identify why it fired at all: the /loop dispatch path omits the 30-day min-age gate that gates this skill under evolve_loop.py."
topics: []
concepts: []
related_articles:
  - "[[todo]]"
  - "[[changelog]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-09-04
last_curated: null
---

# System Tuning Report

**Date**: 2026-09-04
**Sessions analyzed**: session_count 19937; window since the 2026-08-26T19:56 tune-system run
**Period covered**: 2026-08-26 → 2026-09-04 (8.7 days)

## Executive Summary

No Tier 1 changes applied — the **ninth consecutive zero-Tier-1 run**, for the same
structural reason as the previous eight: every setting this skill is licensed to adjust
(`cadences`, `overdue_thresholds`, `replenishment_config`, `locked_settings`) is **absent
from `evolution-state.yaml`**, re-verified `None` this run. Tier 1 is not "declined" here,
it is unreachable.

This run adds the missing explanation for a second anomaly: **this session should not have
fired at all.** It ran 8.7 days after its predecessor against a documented 30-day cadence
and an explicit SKILL.md prohibition on sub-monthly runs. The cause is now located.

System health is otherwise good: 0 critical issues, 0 failures in the last 12 recorded
tasks, 0 orphaned files.

## Metrics Overview

| Metric | Current | Target / Previous | Trend |
|--------|---------|-------------------|-------|
| critical_issues | 0 | max 0 | → meets target |
| medium_issues | 10 | max 3 | ✗ **3.3× over target** |
| low_issues | 3 | — | → |
| orphaned_files | 0 | — | → |
| Recent task failures | 0 of 12 | — | → |
| topics / concepts | 324 / 360, 323 / 360 | — | no cap pressure |
| voids / positions | 99 / 115, 17 / 80 | — | no cap pressure |

## Findings

### Cadence Analysis — the gate exists but this path does not apply it

`tools/evolution/cycle.py` defines `TRIGGER_MIN_AGE_HOURS = {"tune-system": 30 * 24}`,
with a comment recording exactly the failure it was built to stop: *"without this gate it
was running daily (9 reports in 9 days, each declining to apply Tier-1 changes)."*

`filter_triggers_by_min_age()` is imported and called at **exactly one site**:
`scripts/evolve_loop.py:1370`. It is called **nowhere** in the `/loop` dispatch path —
`tools/evolution/cycle_post.py` enqueues cycle triggers at L430–433 with no filter, and
`tools/evolution/cycle_pick.py` drains them at L188 with no filter.

So when the loop is driven by `/unfin-cycle` rather than `scripts/evolve_loop.py`,
tune-system fires purely on the every-6-cycles count, and the monthly gate is inert. That
is why this run happened 8.7 days after its predecessor. Left alone, the `/loop` driver
will reproduce the original "9 reports in 9 days" pathology the gate was written to end.

**Evidence**: the two call sites above, grep-verified this run; `tune_system_history.last_run`
= 2026-08-26T19:56:45Z against a run at 2026-09-04T12:52Z.

This is a **Tier 3** item — it is a code change to dispatch machinery, not an operational
parameter, so it is reported and not applied.

### Failure Pattern Analysis

No findings. `failed_tasks` is empty; the last 12 `recent_tasks` are all `success`
(refine-draft ×5, deep-review, agentic-social, harvest-research-subjects, embed-videos,
check-links, research-voids, check-tenets). Below the 3-occurrence evidence threshold in
every category.

### Queue Health Analysis

No Tier 1 findings. `replenishment_source_counts` is absent from state, so the
source-versus-execution comparison this section specifies cannot be computed — the same
structural gap that blocks Tier 1. Observationally the chain source is live: the
2026-09-03 replenishment (run 1023) minted from the expand→cross-review chain, and this
session executed a research→article chain mint plus several review-derived tasks without
queue starvation.

### Review Finding Patterns

One pattern crosses the 3-review threshold and is worth recording: **recommendations that
ask an existing task to be amended do not execute, while recommendations that mint a new
task do.** The 2026-09-04 tenet check names this directly — its predecessor Warnings 2/3/4
produced no task, and the Tenet 5 self-binding family has gone unminted for three
consecutive checks while growing. Both `/check-tenets` and `/optimistic-review` are
read-only by contract, so their findings reach the queue only if the driver mints them.

### Convergence Progress

`medium_issues` stands at 10 against a `convergence_targets.max_medium_issues` of 3, and
has not been at target in the observed window. `critical_issues` is 0 and at target.
Adjusting a convergence target is a Tier 2 action and is recommended, not applied — the
honest reading is that 3 was set optimistically rather than that quality regressed, but
that judgement is the operator's.

## Changes Applied (Tier 1)

*No changes applied.* Two independent reasons, either sufficient:

1. Every Tier 1-eligible setting is absent from `evolution-state.yaml` (ninth run).
2. This run is 8.7 days after its predecessor; SKILL.md prohibits sub-monthly runs, so
   applying settings changes here would compound the dispatch defect above.

## Recommendations (Tier 2)

### Re-baseline `max_medium_issues`, or mint against the backlog
- **Proposed change**: either raise `convergence_targets.max_medium_issues` from 3 to a
  value the corpus has actually held, or treat the 10 open medium issues as a backlog to
  be minted down.
- **Rationale**: a target never met is not a target; it stops being read.
- **Risk**: Low. No automation gates on this value.
- **To approve**: edit `convergence_targets` in `evolution-state.yaml`, or ask the driver
  to mint the medium issues as P3 tasks.

### Decide whether the absent settings blocks should exist at all
- **Proposed change**: either add `cadences`, `overdue_thresholds` and
  `replenishment_config` blocks to `evolution-state.yaml`, or amend this SKILL.md to drop
  the Tier 1 table.
- **Rationale**: nine consecutive runs have produced a report whose central section is
  structurally empty. One of the two documents is wrong about how this system works.
- **Risk**: Low either way; the second option is the smaller change.

## Items for Human Review (Tier 3)

### The `/loop` dispatch path omits `filter_triggers_by_min_age`
- **Issue observed**: `filter_triggers_by_min_age()` is called only at
  `scripts/evolve_loop.py:1370`. `tools/evolution/cycle_post.py` (L430–433, enqueue) and
  `tools/evolution/cycle_pick.py` (L188, drain) do not call it, so every per-skill
  wall-clock gate in `TRIGGER_MIN_AGE_HOURS` is inert under `/unfin-cycle`.
- **Why human needed**: it is a code change to shared dispatch machinery, and the fix has
  a design choice in it — filter at enqueue time in `cycle_post`, or at drain time in
  `cycle_pick`. Draining is the safer semantics (a gated trigger stays queued rather than
  being silently dropped), but that is the operator's call.
- **Suggested action**: apply the filter in `cycle_pick._load_pending_triggers()`'s
  consumer so gated skills are skipped-and-retained rather than discarded, and confirm no
  other `evolve_loop.py`-only guard is missing from the `/loop` port.

### Read-only review skills have no route to the queue
- **Issue observed**: `/check-tenets` and `/optimistic-review` are read-only by contract.
  Their findings execute only when a driver mints them, and the 2026-09-04 tenet check
  documents three consecutive checks where they did not.
- **Why human needed**: changing a skill's read-only contract is explicitly Tier 3.
- **Suggested action**: either accept that the driver must mint (and say so in the skill),
  or grant a narrow minting licence for findings the skill has verified on disk.

## Next Tuning Session

- **Recommended**: 2026-10-04 (30 days), **and not before** — if a run occurs sooner, the
  dispatch defect above has not been fixed, and that fact is itself the finding.
- **Focus areas**: whether the min-age gate now applies under `/loop`; whether the absent
  settings blocks were added or the Tier 1 table removed; `medium_issues` against target.
