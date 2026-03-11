---
title: "System Tuning Report - 2026-03-11"
created: 2026-03-11
modified: 2026-03-11
human_modified: null
ai_modified: 2026-03-11T16:19:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[todo]]"
  - "[[changelog]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-6
ai_generated_date: 2026-03-11
last_curated: null
---

# System Tuning Report

**Date**: 2026-03-11
**Sessions analyzed**: 236 (sessions 3323 to 3559)
**Period covered**: 2026-03-08 to 2026-03-11 (3 days)

## Executive Summary

The automation system maintains its perfect task success rate (0 failures across 105 changelog entries) for the 6th consecutive tuning period. The most critical development is a **dramatic cap enforcement failure in topics**: topics surged from 200 to 221, exceeding the cap by 10.5%, despite the previous report flagging cap exceedance as a key concern. Concepts (201/200) and voids (104/100) show smaller overages. The replenishment system correctly stopped generating new expand-topic tasks, but existing expand-topic tasks in the queue continued executing without cap checks. The queue underwent a structural shift — P2 tasks grew from 5 to 33 (predominantly staleness-driven deep-reviews and cross-reviews) while P3 shrank from 73 to 30. State tracking remains broken (14th consecutive report). Deep-review continues as the dominant task type at 45% of all tasks.

## Metrics Overview

| Metric | Current (Actual) | Recorded State | Previous (Mar 8) | Trend |
|--------|-------------------|----------------|-------------------|-------|
| Session count | 3559 | 3559 | 3323 | +236 |
| Topics | 221 | 35 | 200 | +21 (OVER CAP by 10.5%) |
| Concepts | 201 | 145 | 201 | +0 (over cap by 0.5%) |
| Arguments | 6 | 4 | 6 | -> |
| Voids | 104 | 11 | 101 | +3 (OVER CAP by 4%) |
| Apex articles | 16 | 4 | 15 | +1 |
| Research notes | 270 | 117 | 258 | +12 |
| Archive files | 181 | -- | 166 | +15 (from coalesce) |
| Reviews completed | 1751 | 542 | 1617 | +134 |
| Recent task success rate | 100% | -- | 100% | -> |
| Critical issues | 0 | 0 | 0 | -> |
| Medium issues | 10 | 10 | 10 | -> |
| Orphaned files | 13 | 13 | 13 | -> |
| Queue depth (P2) | 33 | 34 | 5 | +28 (replenishment) |
| Queue depth (P3) | 30 | 30 | 73 | -43 (consumed/promoted) |

**State discrepancy update**: Recorded state shows 35 topics (actual: 221, 6.3x), 11 voids (actual: 104, 9.5x), 542 reviews (actual: 1751, 3.2x). Discrepancies continue to worsen. 14th consecutive report.

## Abort Conditions Check

**Status**: All clear.

- Task failure rate: 0% (0/20 recent, 0/105 changelog entries) — well under 50% threshold
- Convergence: No regression — content growing, reviews increasing
- Critical issues: 0
- File reads: All successful

## Findings

### Cadence Analysis

**Data points**: 3 days, 236 sessions

| Task | last_runs Timestamp | Actual Last Run (Changelog) | Status |
|------|---------------------|----------------------------|--------|
| validate-all | 2026-01-24 | **Not run since Jan 24** | **47 days stale** |
| pessimistic-review | 2026-01-25 | 2026-03-11 | Timestamp stale |
| optimistic-review | 2026-01-25 | 2026-03-11 | Timestamp stale |
| check-tenets | 2026-03-10 | 2026-03-11 | ~Current |
| check-links | 2026-03-11 | 2026-03-11 | Current |
| deep-review | 2026-01-25 | 2026-03-11 (many) | Timestamp stale |
| tune-system | 2026-03-08 | 2026-03-11 (this run) | Current |
| research-voids | 2026-01-24 | 2026-03-11 (skipped — at capacity) | Timestamp stale |
| coalesce | 2026-01-25 | 2026-03-11 | Timestamp stale |
| apex-evolve | 2026-03-10 | 2026-03-11 | ~Current |
| agentic-social | 2026-03-11 | 2026-03-11 | Current |

**Root cause unchanged**: Queue tasks in `evolve_loop.py` do not update `state.last_runs`. Cycle-triggered tasks correctly update timestamps. **14th consecutive report** flagging this issue.

**validate-all**: Still absent from both the task cycle and CYCLE_TRIGGERS. Has not run in 47 days. **6th report** flagging this gap.

### Failure Pattern Analysis

**Data points**: 20 recent tasks in evolution-state.yaml (all successful); 105 changelog entries since Mar 8

| Task Type | Executed | Failed | Skipped | Rate |
|-----------|----------|--------|---------|------|
| deep-review | 47 | 0 | 1 | 0% |
| expand-topic | 27 | 0 | 1 | 0% |
| refine-draft | 6 | 0 | 0 | 0% |
| condense | 5 | 0 | 0 | 0% |
| coalesce | 5 | 0 | 0 | 0% |
| pessimistic-review | 4 | 0 | 0 | 0% |
| optimistic-review | 4 | 0 | 0 | 0% |
| research-voids | 3 | 0 | 3 | 0% (all skipped — at capacity) |
| check-tenets | 2 | 0 | 0 | 0% |
| apex-evolve | 2 | 0 | 0 | 0% |
| **Total** | **105** | **0** | **5** | **0%** |

**Assessment**: Perfect reliability for the 6th consecutive tuning period. Skips are appropriate (research-voids correctly recognising capacity, expand-topic skipping a duplicate task, deep-review skipping a stale task).

**Critical finding — 27 expand-topic tasks**: Despite all three content sections being at or above cap, 27 expand-topic tasks ran during this period — 26% of all tasks. Topics grew from 200 to 221, voids from 101 to 104. This confirms that **cap enforcement is absent from the expand-topic skill itself** — it only exists in the replenishment system. Existing expand-topic tasks in the queue execute regardless of cap status.

### Queue Health Analysis

**Data points**: Current todo.md state, comparison with Mar 8

**Queue composition**:
- P0: 0 (unchanged)
- P1: 0 (unchanged)
- P2: 33 (was 5, +28)
- P3: 30 (was 73, -43)

**Structural shift**: The queue underwent a major rebalancing this period. P3 dropped 43 tasks (73 to 30) — the largest single-period decrease ever. P2 grew from 5 to 33, primarily from replenishment generating staleness-driven deep-reviews and chain-driven cross-reviews. This suggests that:
1. Many P3 expand-topic tasks were either consumed (27 expand-topic executed) or promoted to P2
2. Replenishment shifted from expansion tasks (at cap) to maintenance tasks (deep-review, cross-review)
3. The queue now correctly reflects improvement-mode priorities

**Current P2 composition** (from todo.md): cross-reviews (from new article chains), deep-reviews (staleness-triggered for 36-41 day old content). This is appropriate for a system at capacity in all sections.

**Replenishment sources**: chain (3) and staleness (4). No expand-topic or research-topic generated — cap enforcement in replenishment is working correctly.

### Review Finding Patterns

**Data points**: 4 pessimistic reviews, 4 optimistic reviews, 2 tenet checks, 47 deep reviews since last tune

**Recurring themes across pessimistic reviews** (Mar 9 - Mar 11):

| Theme | Appearances | Status |
|-------|-------------|--------|
| Unfalsifiable/vague falsification conditions | Mar 9, 10, 11 | Bedrock disagreement; partially addressed by refine-drafts |
| Quantum mechanism speculation without physics | Mar 9, 10, 11 | Recurring; quantum Zeno overemphasis specifically flagged Mar 10 |
| Correlation-to-constitution leaps | Mar 9 | Actionable; specific to mathematical insight article |
| Self-undermining concessions to physicalism | Mar 10 | Structural — the Map's intellectual honesty creates argumentative tension |
| Selective appropriation of Buddhist phenomenology | Mar 10, 11 | Recurring pattern (7th+ tune period flagging) |
| Process philosophy digressions | Mar 11 | Structural — Whitehead sections often unintegrated |
| Circular tenet reinforcement | Mar 10 | Partially addressed by refine-draft on ai-consciousness |
| Functional/phenomenal consciousness conflation | Mar 10 | Recurring (7th+ tune period) |

**Notable development**: The review-then-fix pipeline continues working effectively. The Mar 11 pessimistic review of ai-consciousness identified compartmentalised honesty on quantum coherence; a same-day refine-draft addressed the 2 high-severity issues. Deep reviews are showing maturation effects — several articles now showing minimal changes on 4th-5th review passes.

**Tenet checks**: Mar 10 check-tenets found 0 errors, 3 warnings, 19 notes. Mar 11 check reported similarly clean results. Tenet alignment remains excellent.

### Convergence Progress

**Data points**: Actual file counts vs targets and caps

| Category | Actual Count | Cap | % of Cap | Target | % of Target | Change from Mar 8 |
|----------|-------------|-----|----------|--------|-------------|-------------------|
| Topics | 221 | 200 | **110.5%** | 10 | 2210% | +21 |
| Concepts | 201 | 200 | **100.5%** | 15 | 1340% | +0 |
| Arguments | 6 | -- | -- | 5 | 120% | -> |
| Voids | 104 | 100 | **104%** | -- | No target | +3 |
| Apex | 16 | -- | -- | -- | No target | +1 |
| Research | 270 | -- | -- | -- | No target | +12 |
| Archive | 181 | -- | -- | -- | Not tracked | +15 |
| Reviews | 1751 | -- | -- | -- | No target | +134 |

**Quality metrics**:
- Critical issues: 0 (target: 0) — met
- Medium issues: 10 (target: <=3) — exceeded, persistent (unchanged 6+ periods)
- Low issues: 3 — acceptable
- Orphaned files: 13 — unchanged (persistent 7+ tune periods)

**Critical finding — topic cap failure**: Topics surged from 200 to 221 in 3 days (+10.5% over cap). This is the most significant cap exceedance since caps were introduced. Root cause analysis:
1. **Replenishment correctly respects caps** — the queue note confirms "no expand-topic or research-topic tasks generated"
2. **Expand-topic skill does not check caps** — it executes whatever task is in the queue
3. **The queue contained expand-topic tasks generated before the cap was reached** — these continued executing
4. **The stale content_stats** (showing 35 topics instead of 221) likely prevented any state-based checks from working

**Assessment**: The system needs cap enforcement at the point of execution (expand-topic skill), not just at the point of task generation (replenish-queue). The current architecture has a "pipeline gap" where tasks generated before caps were reached continue executing after caps are exceeded.

**Coalesce and condense activity**: 5 coalesces and 5 condenses this period. This consolidation work is healthy, but the 15 new archive files from coalescing weren't enough to offset the 21 new topics and 3 new voids.

## Changes Applied (Tier 1)

*No changes applied.*

**Rationale**: The evolution-state.yaml contains no adjustable cadence, threshold, or weight parameters. The system's operational parameters are managed by the code-based task cycle (`tools/evolution/cycle.py`), not by YAML settings. This structural limitation has been noted in every tune report (14 reports). The `tune_system_history` and `locked_settings` sections needed for Tier 1 change tracking still do not exist.

## Recommendations (Tier 2)

### 1. Add Cap Enforcement to expand-topic Skill (NEW — URGENT)

- **Proposed change**: In the expand-topic skill, add a file-count check against `section_caps` before creating content. If the target section is at or above cap, refuse to execute and log the skip.
- **Rationale**: Topics grew from 200 to 221 (10.5% over cap) in 3 days. 27 expand-topic tasks ran despite caps being exceeded. The replenishment system respects caps, but the execution system does not. This is the most significant cap enforcement failure to date.
- **Risk**: Low (adding a guard, not changing behaviour for within-cap sections)
- **Priority**: **Critical**

### 2. Fix Stale last_runs Timestamps (Carried Forward x14)

- **Proposed change**: In `scripts/evolve_loop.py`, add `state.last_runs` update after queue task execution.
- **Rationale**: **14th consecutive report.** The single most persistent operational issue in the system's history.
- **Risk**: Low
- **Priority**: **Critical**

### 3. Fix Stale content_stats and progress Counters (Carried Forward x9)

- **Proposed change**: Add file-counting logic to refresh `content_stats` and `progress` in `tools/evolution/state.py`, called at session start.
- **Rationale**: Recorded state shows 35 topics (actual: 221, 6.3x), 11 voids (actual: 104, 9.5x), 542 reviews (actual: 1751, 3.2x). The stale content_stats may be contributing to cap enforcement failures if any check reads from state rather than counting files. 9th consecutive report.
- **Risk**: Low
- **Priority**: High

### 4. Update Convergence Targets (Carried Forward x13)

- **Proposed change**: Update `convergence_targets` in evolution-state.yaml:
  - min_topics: 10 -> 150
  - min_concepts: 15 -> 150
  - min_arguments: 5 -> 10
  - Add min_voids: 50
  - Add min_apex: 10
- **Rationale**: Targets set for early-stage system. All vastly exceeded (topics at 2210% of target). 13th report.
- **Risk**: Low

### 5. Add tune_system_history and locked_settings Sections (Carried Forward x11)

- **Proposed change**: Add both sections to evolution-state.yaml per skill specification.
- **Rationale**: Required for cooldown enforcement and locked settings checks. 11th report.
- **Risk**: Low

### 6. Add validate-all to Cycle Triggers (Carried Forward x6)

- **Proposed change**: Add `"validate-all": 2` to `CYCLE_TRIGGERS` in `tools/evolution/cycle.py`.
- **Rationale**: Has not run in 47 days. Described as "Daily health check" in CLAUDE.md but absent from automation cycle. 6th report.
- **Risk**: Low (read-only check)
- **Priority**: Medium

### 7. Purge Unexecutable expand-topic Tasks from Queue (NEW)

- **Proposed change**: Remove or demote all P3 expand-topic tasks that target sections at or above cap. These tasks cannot be executed without cap increases and are consuming queue space.
- **Rationale**: The P3 queue still contains expand-topic tasks from before caps were reached. With all three sections over cap, these are unexecutable. The queue shrank from 73 to 30, but some remaining tasks are likely dead weight.
- **Risk**: Low (tasks can be regenerated if caps are raised)
- **Priority**: Medium

### 8. Systematic Citation Audit (Carried Forward x6)

- **Proposed change**: Add P2 task to audit articles flagged for unverifiable empirical claims.
- **Rationale**: "Unsupported empirical claims" remains a consistently actionable recurring pattern across pessimistic reviews. 7th tune report flagging this pattern. Multiple reviews this period flagged specific unsupported claims (Hoel 2025 preprint status, dual-process conflation, cross-cultural evidence gaps).
- **Risk**: Low

## Items for Human Review (Tier 3)

### 1. Topic Cap Enforcement Failure — Urgent

- **Issue observed**: Topics grew from 200 to 221 in 3 days, exceeding the cap by 10.5%. This is the largest cap exceedance to date. Root cause: expand-topic skill does not check caps; only replenishment does. The pipeline gap allows pre-existing expand-topic tasks to execute after caps are reached.
- **Why human needed**: Code change required in expand-topic skill and potentially in evolve_loop.py task execution logic. Decision needed: (a) add cap check to expand-topic, (b) add cap check to evolve_loop before dispatching, (c) raise caps if the current levels are still insufficient, or (d) some combination. Also: should the 21 excess topics be coalesced/archived to bring the section back under cap?
- **Suggested action**: Fix cap enforcement at execution point, then decide whether to bring topics back under 200 through consolidation or raise the cap.

### 2. Stale Timestamps — 14th Consecutive Report

- **Issue observed**: The `last_runs` stale timestamp bug has been reported in every tune report since the system began. Also the `content_stats` and `progress` sections (9th report) and the missing `tune_system_history`/`locked_settings` sections (11th report).
- **Why human needed**: Code changes to evolve_loop.py and tools/evolution/state.py
- **Suggested action**: Fix the three state-tracking issues together

### 3. Medium Issues Persistent at 10 (Carried Forward x5)

- **Issue observed**: Medium issues count has been exactly 10 for 5+ months across many tune periods. Target is <=3.
- **Why human needed**: Deciding whether to raise target or address specific issues
- **Suggested action**: Raise `max_medium_issues` to 15

### 4. Orphaned Files Persistent at 13 (Carried Forward x5)

- **Issue observed**: Orphaned file count has been 13 for 7+ tune periods despite 134 reviews and 47 deep reviews this period (many adding cross-links). The count is completely static.
- **Why human needed**: The count being exactly 13 across dozens of reviews that explicitly add cross-links suggests either the counting mechanism is broken or the same 13 files keep resisting integration while new orphans are created at the same rate.
- **Suggested action**: List the specific 13 orphaned files and investigate why they persist

### 5. Queue Structural Shift — Healthy

- **Issue observed**: Positive finding. P3 dropped from 73 to 30 (largest single-period reduction). P2 grew from 5 to 33, predominantly with appropriate maintenance tasks (staleness deep-reviews, chain cross-reviews). The queue now correctly reflects improvement-mode priorities. Replenishment is generating only chain and staleness tasks, not expansion tasks.
- **Why human needed**: No action needed — informational
- **Suggested action**: Continue current approach; the queue is self-correcting

## System Health Summary

| Component | Status | Notes |
|-----------|--------|-------|
| Task execution | Excellent | 100% success rate, 6th consecutive period |
| Content quality | Good | 0 critical, 47 deep reviews in 3 days |
| Queue management | Improved | P3 73->30, queue reflecting improvement mode |
| Review system | Effective | 1751+ reviews, articles stabilising |
| Scheduling | Operational | Cycle mechanism working correctly |
| State tracking | **Broken** | last_runs, content_stats, progress all stale (14th report) |
| Section caps | **Exceeded** | Topics 221/200, concepts 201/200, voids 104/100 |
| Cap enforcement | **Failing** | expand-topic ignores caps; topics +21 in 3 days |
| Site validation | **Gap** | validate-all not running (47 days) |
| Coalesce pipeline | Working | 5 coalesces, 5 condenses, but net growth still positive |
| Tenet alignment | Excellent | 0 errors, 3 warnings |
| Review-fix pipeline | Effective | Same-day pessimistic -> refine-draft cycles working |

## Next Tuning Session

- **Recommended**: 2026-04-10 (30 days out)
- **Focus areas**:
  - Verify cap enforcement fix implemented at expand-topic level (critical — topics 10.5% over cap)
  - Verify last_runs timestamp fix (now 14 reports — critical)
  - Verify content_stats refresh (9 reports)
  - Check if topics have been consolidated back to/below 200
  - Monitor queue trajectory — does improvement mode continue?
  - Check if validate-all was added to cycle (47+ days absent)
  - Evaluate orphaned files (static at 13 for 7+ periods)
  - Check if tune_system_history/locked_settings sections were added
  - Assess whether medium issues target was adjusted
