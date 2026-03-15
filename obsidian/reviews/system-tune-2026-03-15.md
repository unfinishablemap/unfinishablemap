---
title: "System Tuning Report - 2026-03-15"
created: 2026-03-15
modified: 2026-03-15
human_modified: null
ai_modified: 2026-03-15T10:13:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[todo]]"
  - "[[changelog]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-6
ai_generated_date: 2026-03-15
last_curated: null
---

# System Tuning Report

**Date**: 2026-03-15
**Sessions analyzed**: 144 (sessions 3703 to 3847)
**Period covered**: 2026-03-12 to 2026-03-15 (3 days)

## Executive Summary

The automation system maintains its perfect task success rate (0 failures) for the 8th consecutive tuning period across 146 changelog entries. Topics grew to 224/200 (12% over cap, up from 223), voids to 106/100 (6% over cap, up from 105), while concepts held steady at 200/200. Cap enforcement remains absent from the execution path — expand-topic ran 3 times this period despite all target sections being at or above cap. The queue was massively replenished: P2 grew from 2 to 22, P3 from ~28 to 94. However, most P2 tasks are expand-topic tasks targeting sections at/above cap, making them unexecutable — a replenishment system regression. State tracking remains broken (16th consecutive report). Deep-review continues as the dominant task type at ~60% of all tasks, with many articles now showing stability on review (0 word count changes).

## Metrics Overview

| Metric | Current (Actual) | Recorded State | Previous (Mar 12) | Trend |
|--------|-------------------|----------------|-------------------|-------|
| Session count | 3847 | 3847 | 3703 | +144 |
| Topics | 224 | 35 | 223 | +1 (OVER CAP by 12%) |
| Concepts | 200 | 145 | 200 | 0 (AT CAP) |
| Arguments | 6 | 4 | 6 | → |
| Voids | 106 | 11 | 105 | +1 (OVER CAP by 6%) |
| Apex articles | 17 | 4 | 16 | +1 |
| Research notes | 279 | 117 | 270 | +9 |
| Archive files | 197 | -- | 187 | +10 (from coalesce) |
| Reviews completed | 1955 | 542 | 1862 | +93 |
| Recent task success rate | 100% | -- | 100% | → |
| Critical issues | 0 | 0 | 0 | → |
| Medium issues | 10 | 10 | 10 | → |
| Orphaned files | 13 | 13 | 13 | → |
| Queue depth (P1) | 3 | -- | 0 | +3 (coalesce tasks) |
| Queue depth (P2) | 22 | -- | 2 | +20 (replenishment) |
| Queue depth (P3) | 94 | -- | ~28 | +66 (replenishment) |

**State discrepancy update**: Recorded state shows 35 topics (actual: 224, 6.4x), 11 voids (actual: 106, 9.6x), 542 reviews (actual: 1955, 3.6x). Discrepancies continue to worsen. 16th consecutive report.

## Abort Conditions Check

**Status**: All clear.

- Task failure rate: 0% (0/20 recent tasks, all successful) — well under 50% threshold
- Convergence: No regression — reviews increasing, content stable or growing
- Critical issues: 0
- File reads: All successful

## Findings

### Cadence Analysis

**Data points**: 3 days, 144 sessions

| Task | last_runs Timestamp | Actual Last Run (Changelog) | Status |
|------|---------------------|----------------------------|--------|
| validate-all | 2026-01-24 | **Not run since Jan 24** | **51 days stale** |
| pessimistic-review | 2026-01-25 | 2026-03-15 | Timestamp stale |
| optimistic-review | 2026-01-25 | 2026-03-15 (x2) | Timestamp stale |
| check-tenets | 2026-03-14 | 2026-03-15 | Current |
| check-links | 2026-03-15 | 2026-03-15 | Current |
| deep-review | 2026-01-25 | 2026-03-15 (many) | Timestamp stale |
| tune-system | 2026-03-15 | 2026-03-15 (this run) | Current |
| research-voids | 2026-01-24 | 2026-03-15 (skipped — at capacity) | Timestamp stale |
| coalesce | 2026-01-25 | 2026-03-15 (x2) | Timestamp stale |
| apex-evolve | 2026-03-14 | 2026-03-15 | ~Current |
| agentic-social | 2026-03-15 | 2026-03-15 | Current |

**Root cause unchanged**: Queue tasks in `evolve_loop.py` do not update `state.last_runs`. Cycle-triggered tasks correctly update timestamps. **16th consecutive report** flagging this issue.

**validate-all**: Still absent from both the task cycle and CYCLE_TRIGGERS. Has not run in 51 days. **8th report** flagging this gap.

### Failure Pattern Analysis

**Data points**: 20 recent tasks in evolution-state.yaml (all successful); 146 changelog entries since Mar 12

| Task Type | Executed | Failed | Skipped | Rate |
|-----------|----------|--------|---------|------|
| deep-review | ~60 | 0 | 2 | 0% |
| refine-draft | ~8 | 0 | 0 | 0% |
| pessimistic-review | 5 | 0 | 0 | 0% |
| optimistic-review | 4 | 0 | 0 | 0% |
| expand-topic | 4 | 0 | 0 | 0% |
| condense | 3 | 0 | 0 | 0% |
| coalesce | 3 | 0 | 0 | 0% |
| check-tenets | 2 | 0 | 0 | 0% |
| research-voids | 0 | 0 | 2 | 0% (all skipped — at capacity) |
| apex-evolve | 2 | 0 | 0 | 0% |
| check-links | 1 | 0 | 0 | 0% |
| agentic-social | multiple | 0 | 0 | 0% |
| **Total** | **~95** | **0** | **4** | **0%** |

**Assessment**: Perfect reliability for the 8th consecutive tuning period. Skips are appropriate (research-voids correctly recognising capacity, deep-reviews skipping archived files).

**Cap enforcement**: 4 expand-topic tasks executed this period, creating articles in topics/ and voids/ despite both sections being over cap. Topics grew from 223 to 224, voids from 105 to 106. Cap enforcement gap persists at execution level (3rd report since identification).

### Queue Health Analysis

**Data points**: Current todo.md state, comparison with Mar 12

**Queue composition**:
- P0: 0 (unchanged)
- P1: 3 (was 0, +3 — all coalesce tasks)
- P2: 22 (was 2, +20)
- P3: 94 (was ~28, +66)

**Critical finding — P2 expand-topic regression**: The 22 P2 tasks are predominantly expand-topic "Write article on..." tasks. These target topics/, concepts/, or voids/ — all sections at or above cap. This represents a **replenishment system regression**: the previous report noted that replenishment had correctly shifted to improvement-mode tasks (deep-reviews, cross-reviews), but the current replenishment round generated a large batch of expand-topic tasks that cannot execute without cap increases.

**Positive development — P1 coalesce tasks**: The 3 P1 tasks are strategically targeted coalesce operations, each merging 4 topics articles into 1. If all 3 execute successfully, topics/ would lose 9 articles (224 → 215), making meaningful progress toward the 200 cap. The replenishment system correctly identified this as the highest-priority action.

**Active tasks (P0-P2)**: 25 (was 2). Well above the replenishment threshold of 3. However, most P2 tasks are unexecutable expand-topic tasks.

**Assessment**: The queue is inflated with unexecutable tasks. The P1 coalesce work is well-targeted, but the P2 expand-topic tasks are dead weight that will either fail or further exceed section caps.

### Review Finding Patterns

**Data points**: 5 pessimistic reviews, 4 optimistic reviews, 2 tenet checks, ~60 deep reviews since last tune

**Recurring themes across pessimistic reviews** (Mar 13-15):

| Theme | Appearances | Status |
|-------|-------------|--------|
| Quantum mechanism speculation without physics grounding | Mar 13, 14, 14-evening, 14-night | Recurring (9th+ tune period) |
| Unfalsifiable/vague falsification conditions | Mar 13, 14-night, 15 | Recurring |
| Functional/phenomenal consciousness conflation | Mar 13, 14 | Recurring (9th+ tune period) |
| Buddhist philosophy appropriation | Mar 13, 14, 14-evening, 15 | Recurring (8th+ tune period) |
| Asymmetric vulnerability treatment (own position gets soft questions) | Mar 15 | Recurring |
| Missing/incomplete citations | Mar 14-evening, 15 | Recurring — actionable |
| Empirical claims overstated | Mar 14, 14-night | Recurring |
| Circular tenet dependencies | Mar 13 | Recurring |
| Embodiment evidence undermining dualist framing | Mar 14-night | New pattern |
| Powers as redescription (causal powers not explanatory) | Mar 14 | Actionable |

**Review-fix pipeline**: Continues working effectively. The Mar 15 pessimistic review of hard-problem-of-consciousness generated specific findings (asymmetric vulnerability, missing citations, length); a same-day refine-draft addressed citations and added "Open Problems for the Map's Framework" section.

**Tenet checks** (Mar 14, 15): 0 errors, 0 warnings (Mar 15). Tenet alignment excellent.

**Deep review maturation**: Many articles showing stability on repeated review passes — multiple articles with +0 or single-digit word count changes. This confirms content convergence in the most-reviewed articles.

### Convergence Progress

**Data points**: Actual file counts vs targets and caps

| Category | Actual Count | Cap | % of Cap | Target | % of Target | Change from Mar 12 |
|----------|-------------|-----|----------|--------|-------------|-------------------|
| Topics | 224 | 200 | **112%** | 10 | 2240% | +1 |
| Concepts | 200 | 200 | **100%** | 15 | 1333% | 0 |
| Arguments | 6 | -- | -- | 5 | 120% | → |
| Voids | 106 | 100 | **106%** | -- | No target | +1 |
| Apex | 17 | -- | -- | -- | No target | +1 |
| Research | 279 | -- | -- | -- | No target | +9 |
| Archive | 197 | -- | -- | -- | Not tracked | +10 |
| Reviews | 1955 | -- | -- | -- | No target | +93 |

**Quality metrics**:
- Critical issues: 0 (target: 0) — met
- Medium issues: 10 (target: <=3) — exceeded, persistent (unchanged 7+ periods)
- Low issues: 3 — acceptable
- Orphaned files: 13 — unchanged (persistent 9+ tune periods)

**Cap exceedance continues**: Topics grew +1 (224 vs 223), voids +1 (106 vs 105) since last tune. Growth rate has slowed significantly (was +21 in the Mar 8-11 period, +2 in Mar 11-12, now +1/+1) — likely because most expand-topic tasks have been consumed and the remaining P2 expand-topic tasks haven't yet executed.

**Archive growth healthy**: +10 archive files (197 total) confirms ongoing consolidation activity. Concepts stable at exactly 200 (at cap).

**Content convergence signal**: 93 reviews in 3 days. Many deep reviews now finding articles stable with 0-7 word count changes. The review system is approaching diminishing returns on the most-reviewed content.

## Changes Applied (Tier 1)

*No changes applied.*

**Rationale**: The evolution-state.yaml contains no adjustable cadence, threshold, or weight parameters. The system's operational parameters are managed by the code-based task cycle (`tools/evolution/cycle.py`), not by YAML settings. This structural limitation has been noted in every tune report (16 reports). The `tune_system_history` and `locked_settings` sections needed for Tier 1 change tracking still do not exist.

## Recommendations (Tier 2)

### 1. Add Cap Enforcement to expand-topic Skill (Carried Forward x3 — CRITICAL)

- **Proposed change**: In the expand-topic skill, add a file-count check against `section_caps` before creating content. If the target section is at or above cap, refuse to execute and log the skip.
- **Rationale**: Topics at 224/200 (12% over), voids at 106/100 (6% over). 4 expand-topic tasks executed this period despite caps being exceeded. **3rd report since identification.**
- **Risk**: Low (adding a guard, not changing behaviour for within-cap sections)
- **Priority**: **Critical**

### 2. Fix Replenishment Generating Unexecutable expand-topic Tasks (NEW — URGENT)

- **Proposed change**: In `/replenish-queue`, add cap check before generating expand-topic tasks. The current replenishment round generated ~20 P2 expand-topic tasks targeting sections at/above cap.
- **Rationale**: The Mar 12 report noted replenishment had correctly shifted to improvement-mode tasks. The current replenishment round regressed, producing expand-topic tasks that cannot execute. This inflates the queue with dead weight and may cause further cap exceedance if the tasks execute before cap enforcement is added.
- **Risk**: Low
- **Priority**: **Critical**

### 3. Fix Stale last_runs Timestamps (Carried Forward x16)

- **Proposed change**: In `scripts/evolve_loop.py`, add `state.last_runs` update after queue task execution.
- **Rationale**: **16th consecutive report.** The single most persistent operational issue in the system's history.
- **Risk**: Low
- **Priority**: **Critical**

### 4. Fix Stale content_stats and progress Counters (Carried Forward x11)

- **Proposed change**: Add file-counting logic to refresh `content_stats` and `progress` in `tools/evolution/state.py`, called at session start.
- **Rationale**: Recorded state shows 35 topics (actual: 224, 6.4x), 11 voids (actual: 106, 9.6x), 542 reviews (actual: 1955, 3.6x). 11th consecutive report.
- **Risk**: Low
- **Priority**: High

### 5. Update Convergence Targets (Carried Forward x15)

- **Proposed change**: Update `convergence_targets` in evolution-state.yaml:
  - min_topics: 10 → 150
  - min_concepts: 15 → 150
  - min_arguments: 5 → 10
  - Add min_voids: 50
  - Add min_apex: 10
- **Rationale**: Targets set for early-stage system. All vastly exceeded (topics at 2240% of target). 15th report.
- **Risk**: Low

### 6. Add tune_system_history and locked_settings Sections (Carried Forward x13)

- **Proposed change**: Add both sections to evolution-state.yaml per skill specification.
- **Rationale**: Required for cooldown enforcement and locked settings checks. 13th report.
- **Risk**: Low

### 7. Add validate-all to Cycle Triggers (Carried Forward x8)

- **Proposed change**: Add `"validate-all": 2` to `CYCLE_TRIGGERS` in `tools/evolution/cycle.py`.
- **Rationale**: Has not run in 51 days. Described as "Daily health check" in CLAUDE.md but absent from automation cycle. 8th report.
- **Risk**: Low (read-only check)
- **Priority**: Medium

### 8. Purge Unexecutable expand-topic Tasks from Queue (Carried Forward x3)

- **Proposed change**: Remove or demote all P2/P3 expand-topic tasks that target sections at or above cap. Approximately 20+ P2 expand-topic tasks and additional P3 tasks target topics/, concepts/, or voids/ — all at/above cap.
- **Rationale**: These tasks cannot execute without cap increases and inflate the queue. The queue grew from 2 active to 25 active tasks, but most are unexecutable. Replenishment will regenerate appropriate tasks if caps are raised.
- **Risk**: Low
- **Priority**: High

### 9. Systematic Citation Audit (Carried Forward x8)

- **Proposed change**: Add P2 task to audit articles flagged for unverifiable empirical claims.
- **Rationale**: Missing/incomplete citations continues as one of the most consistently actionable findings across pessimistic reviews. The Mar 14-evening and Mar 15 reviews flagged specific citation gaps (Churchland 1986/1996, Block 1978, McGinn 1989, specific Sperry/Miller publications). 8th report.
- **Risk**: Low

## Items for Human Review (Tier 3)

### 1. Cap Enforcement Still Failing — 3rd Report Since Identification

- **Issue observed**: Topics grew from 223 to 224, voids from 105 to 106 since last tune. 4 expand-topic tasks ran despite both sections being over cap. First identified in the Mar 8 tune report; urgently flagged in Mar 11, Mar 12; still not fixed.
- **Why human needed**: Code change required in expand-topic skill and/or evolve_loop.py task execution logic.
- **Suggested action**: Add cap check to expand-topic skill before content creation. Consider also purging unexecutable expand-topic tasks from the queue.

### 2. Replenishment System Regression — New Issue

- **Issue observed**: The replenishment system generated ~20 P2 expand-topic tasks targeting sections at/above cap. The Mar 12 report noted replenishment had correctly shifted to improvement-mode tasks, but this round regressed. The queue now contains 22 P2 tasks, most of which are unexecutable expand-topic tasks.
- **Why human needed**: Code investigation needed — why did replenishment generate expand-topic tasks when sections are at/above cap? Possible cause: stale content_stats showing 35 topics instead of 224.
- **Suggested action**: Fix content_stats first (stale counts may be misleading replenishment logic), then verify replenishment respects caps.

### 3. Stale Timestamps — 16th Consecutive Report

- **Issue observed**: The `last_runs` stale timestamp bug has been reported in every tune report since the system began. Also the `content_stats` and `progress` sections (11th report) and the missing `tune_system_history`/`locked_settings` sections (13th report).
- **Why human needed**: Code changes to evolve_loop.py and tools/evolution/state.py
- **Suggested action**: Fix the three state-tracking issues together. The stale content_stats may be the root cause of the replenishment regression.

### 4. Medium Issues Persistent at 10 (Carried Forward x7)

- **Issue observed**: Medium issues count has been exactly 10 for 7+ months across many tune periods. Target is <=3.
- **Why human needed**: Deciding whether to raise target or address specific issues
- **Suggested action**: Raise `max_medium_issues` to 15

### 5. Orphaned Files Persistent at 13 (Carried Forward x7)

- **Issue observed**: Orphaned file count has been 13 for 9+ tune periods despite ~93 reviews this period (many adding cross-links). The count is completely static.
- **Why human needed**: The count being exactly 13 across hundreds of reviews suggests the counting mechanism may be broken or orphans are created at the same rate they are resolved.
- **Suggested action**: List the specific 13 orphaned files and investigate

### 6. Deep-Review Diminishing Returns (Carried Forward x2)

- **Issue observed**: Multiple articles showing stability on 4th-5th+ review passes with 0 or single-digit word count changes. Deep-review remains ~60% of all tasks. While effective at catching issues on first/second pass, subsequent passes on stable articles consume resources without benefit.
- **Why human needed**: Deciding whether to add a "review_stable" field or skip articles reviewed in last 14 days with no changes.
- **Suggested action**: Consider tracking last review date and change magnitude per article, skipping deep-review for recently-reviewed stable articles.

## System Health Summary

| Component | Status | Notes |
|-----------|--------|-------|
| Task execution | Excellent | 100% success rate, 8th consecutive period |
| Content quality | Good | 0 critical, ~60 deep reviews in 3 days |
| Queue management | **Degraded** | Inflated with 20+ unexecutable P2 expand-topic tasks |
| Review system | Effective | 1955+ reviews, articles reaching convergence |
| Review-fix pipeline | Effective | Same-day pessimistic → refine-draft cycles working |
| Scheduling | Operational | Cycle mechanism working correctly |
| State tracking | **Broken** | last_runs, content_stats, progress all stale (16th report) |
| Section caps | **Exceeded** | Topics 224/200, concepts 200/200, voids 106/100 |
| Cap enforcement | **Failing** | expand-topic ignores caps; topics +1, voids +1 this period |
| Replenishment | **Regressed** | Generated unexecutable expand-topic tasks at P2 |
| Site validation | **Gap** | validate-all not running (51 days) |
| Coalesce pipeline | Working | 3 coalesces, +10 archive files |
| Tenet alignment | Excellent | 0 errors, 0 warnings |

## Next Tuning Session

- **Recommended**: 2026-04-14 (30 days out)
- **Focus areas**:
  - Verify cap enforcement fix at expand-topic level (critical — 3rd report, topics 12% over)
  - Verify replenishment respects caps (new regression)
  - Verify last_runs timestamp fix (16 reports — critical)
  - Verify content_stats refresh (11 reports — may be root cause of replenishment regression)
  - Check if P1 coalesce tasks successfully reduced topics count
  - Monitor whether unexecutable P2 tasks were purged
  - Check if validate-all was added to cycle (51+ days absent)
  - Evaluate orphaned files (static at 13 for 9+ periods)
  - Check if tune_system_history/locked_settings sections were added
  - Assess deep-review diminishing returns mitigation
