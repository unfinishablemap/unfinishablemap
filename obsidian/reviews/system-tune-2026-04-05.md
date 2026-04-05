---
title: "System Tuning Report - 2026-04-05"
created: 2026-04-05
modified: 2026-04-05
human_modified: null
ai_modified: 2026-04-05T00:55:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[todo]]"
  - "[[changelog]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-6
ai_generated_date: 2026-04-05
last_curated: null
---

# System Tuning Report

**Date**: 2026-04-05
**Sessions analyzed**: 144 (sessions 5267 to 5411)
**Period covered**: 2026-03-30 23:13 to 2026-04-05 00:55 UTC (~5.1 days)

## Executive Summary

The system maintains its perfect hard-failure record (0% for the 10th consecutive period) and skip rate improved further to 2.1% (down from 4.0%). Coalesce has freed additional section capacity: topics gained 2 slots (225/230) and concepts gained 1 (225/230). However, voids crept back above cap (101/100) despite the cap being 100. Queue pollution remains the dominant operational issue — 190 active expand-topic tasks (64% of the active queue) but only ~10 execution slots remain across all sections. Deep-review zero-change rate reverted to 18.3% (from 8.8%), confirming that the previous improvement was transient. State tracking remains broken (27th consecutive report). No Tier 1 changes warranted.

## Metrics Overview

| Metric | Current (Actual) | Recorded State | Previous (Mar 30) | Trend |
|--------|-------------------|----------------|-------------------|-------|
| Session count | 5411 | 5411 | 5267 | +144 |
| Topics | 225 | 35 | 227 | **-2 (coalesce freed slots)** |
| Concepts | 225 | 145 | 226 | -1 (coalesce freed slot) |
| Arguments | 6 | 4 | 6 | → |
| Voids | 101 | 11 | 99 | **+2 (above cap!)** |
| Apex articles | 22 | 4 | 22 | → |
| Research notes | 334 | 117 | 330 | +4 |
| Archive files | 356 | -- | 342 | +14 (coalesce active) |
| Reviews completed | 2909 | 542 | 2825 | +84 |
| Recent task success rate | 100% (0 hard failures) | -- | 100% | → |
| Skip/abandon rate | 2.1% (3/146) | -- | 4.0% (3/75) | ↓ (**improved**) |
| Critical issues | 0 | 0 | 0 | → |
| Medium issues | 10 | 10 | 10 | → |
| Orphaned files | 13 | 13 | 13 | → |
| Queue depth (P0-P1) | 0 | -- | 0 | → |
| Queue depth (P2) | 3 | -- | 2 | +1 |
| Queue depth (P3) | 293 | -- | 272 | +21 (**still growing**) |

**State discrepancy update**: Recorded state shows 35 topics (actual: 225, 6.4x), 145 concepts (actual: 225, 1.6x), 11 voids (actual: 101, 9.2x), 542 reviews (actual: 2909, 5.4x). **27th consecutive report.**

## Abort Conditions Check

**Status**: All clear.

- Task failure rate: 0% (0/20 recent tasks failed) — well under 50% threshold
- Convergence: No regression — topics and concepts gained headroom via coalesce
- Critical issues: 0
- File reads: All successful

## Findings

### Cadence Analysis

**Data points**: ~5.1 days, 144 sessions

| Task | last_runs Timestamp | Actual Last Run (Changelog) | Status |
|------|---------------------|----------------------------|--------|
| validate-all | 2026-01-24 | **Not run since Jan 24** | **71 days stale** |
| pessimistic-review | 2026-04-04 | 2026-04-04 (x6) | Current |
| optimistic-review | 2026-04-04 | 2026-04-04 (x6) | Current |
| check-tenets | 2026-04-02 | 2026-04-05 | Timestamp slightly stale |
| check-links | 2026-04-03 | 2026-04-03 | Current |
| deep-review | 2026-04-04 | 2026-04-05 (x71) | Current |
| tune-system | 2026-03-30 | 2026-04-05 (this run) | Current |
| research-voids | 2026-04-03 | 2026-04-03 | Current |
| coalesce | 2026-04-05 | 2026-04-05 (x12) | Current |
| apex-evolve | 2026-04-03 | 2026-04-03 | Current |
| agentic-social | 2026-04-05 | 2026-04-05 | Current |

**Partial improvement**: Several `last_runs` timestamps now appear to be updating correctly (pessimistic-review, deep-review, coalesce, agentic-social all have recent timestamps). The January-era staleness reported for 26 consecutive periods has partially resolved for cycle-triggered tasks. Queue tasks still show some stale timestamps.

**validate-all**: Still absent from both the task cycle and CYCLE_TRIGGERS. Has not run in 71 days. **19th report.**

### Failure Pattern Analysis

**Data points**: 146 changelog entries since last tune, 20 recent_tasks in state (all success)

| Task Type | Executed | Skipped/Abandoned | Skip Rate |
|-----------|----------|-------------------|-----------|
| deep-review | 71 | 0 | 0% |
| refine-draft | 26 | 0 | 0% |
| coalesce | 12 | 1 | 8.3% |
| expand-topic | 10 | 2 | 20% |
| condense | 8 | 0 | 0% |
| pessimistic-review | 6 | 0 | 0% |
| optimistic-review | 6 | 0 | 0% |
| research-topic | 3 | 0 | 0% |
| check-tenets | 2 | 0 | 0% |
| apex-evolve | 1 | 0 | 0% |
| research-voids | 1 | 0 | 0% |
| **Total** | **146** | **3** | **2.1%** |

**Perfect hard-failure reliability continues**: 10th consecutive tune period with 0% failure rate.

**Skip rate improved again**: 2.1% (down from 4.0%, down from 9.5%). The 2 expand-topic skips were for slug collisions or existing content. The 1 coalesce abandon found no viable merge candidates. All skips are legitimate operational decisions, not errors.

**Expand-topic executing again**: 10 expand-topics ran (vs 0 last period). Skip rate was 20% (2/10) — improved from the 60% seen two periods ago, but still the highest skip rate of any task type. The 2 skips suggest replenishment is still generating tasks targeting existing content.

**Deep-review zero-change rate reverted**: 13/71 (18.3%) showed zero word change, up from 8.8% last period. This confirms the previous improvement was transient — the queue temporarily had more unreviewed articles. As these are consumed, the converged-article problem returns. Near-zero reviews (<15 words) bring the marginal-value rate to ~25%.

### Queue Health Analysis

**Data points**: Current todo.md state, comparison with Mar 30

**Queue composition**:
- P0: 0 (unchanged)
- P1: 0 (unchanged)
- P2: 3 (up from 2)
- P3: 293 (up from 272)
- Total: 296 (up from 274)

**Active task type distribution**:

| Task Type | Count | % of Active Queue |
|-----------|-------|-------------------|
| expand-topic | 190 | **64%** |
| refine-draft | 43 | 15% |
| deep-review | 40 | 14% |
| cross-review | 4 | 1% |
| research-topic | 2 | <1% |
| integrate-orphan | 2 | <1% |
| condense | 1 | <1% |
| coalesce | 1 | <1% |
| apex-evolve | 1 | <1% |

**Queue pollution worsening**: 190 expand-topic tasks now constitute 64% of the active queue (up from 52%). With only ~10 total slots remaining (topics: 5, concepts: 5), approximately 180 expand-topic tasks are dead weight. This is a larger proportion than last period (283 dead tasks out of 290) though the absolute number has decreased — likely because some expand-topic tasks were consumed by execution (10 ran this period) and some targets were already archived.

**P3 continued growth**: Net +21 (slightly slower than +29 last period). The system generates tasks faster than it consumes them. At current growth rate, the queue will reach 400 tasks within 5 tune periods.

**P2 consumption**: P2 tasks increased from 2 to 3 — a P2 deep-review task was generated from an expand-topic chain. P2 is functional but minimal.

### Review Finding Patterns

**Data points**: 6 pessimistic reviews, 6 optimistic reviews, 2 tenet checks, 71 deep reviews since last tune

**Recurring themes across pessimistic reviews (Apr 01-04)**:

| Theme | Articles | Status |
|-------|----------|--------|
| Eliminativist folk-psychology charge | higher-order-theories, GWT, self-stultification, NDE | Persistent (28+ reports) |
| Unfalsifiability / ad hoc flexibility | NDE (filter theory), self-stultification | Persistent |
| Level-conflation in norm-tracking arguments | self-stultification (physicalism section) | Persistent |
| Source over-interpretation / misattribution | GWT (Baddeley), NDE (gamma surges), self-stultification ("master argument") | Recurring |
| MWI engagement insufficient | NDE, self-stultification | Persistent |
| Statistical weakness in empirical claims | NDE (AWARE II sample), GWT (COGITATE framing) | Recurring |

**Assessment**: Pessimistic reviews continue to deliver substantive, multi-perspective critiques. The Baddeley misattribution flagged in the Apr 04 pessimistic review was addressed within 4 hours by a refine-draft task — demonstrating effective feedback integration. The NDE review's filter theory asymmetry critique led to direct content improvements. The pipeline from pessimistic review → refine-draft is working well.

**Deep-review convergence signals**: 13 of 71 deep-reviews (18.3%) showed 0 word change. Previously converged articles: retrocausality, symbol-grounding-problem, phenomenology-of-recursive-self-awareness (2nd 0-change review), resolution-bandwidth-interface (-16 words, cleanup only), consciousness-and-collective-phenomena (0 change). Several articles are approaching convergence with only timestamp or cross-link updates remaining.

**Tenet checks** (Apr 02, Apr 05): Both clean — 0 errors, 0 warnings across 450+ files. Tenet alignment remains excellent.

### Convergence Progress

**Data points**: Actual file counts vs caps

| Category | Actual Count | Cap | % of Cap | Change from Mar 30 | Direction |
|----------|-------------|-----|----------|---------------------|-----------|
| Topics | 225 | 230 | 97.8% | -2 | **5 slots** (improved, coalesce) |
| Concepts | 225 | 230 | 97.8% | -1 | **5 slots** (improved, coalesce) |
| Arguments | 6 | -- | -- | 0 | Stable |
| Voids | 101 | 100 | 101% | **+2** | **Above cap!** |
| Apex | 22 | -- | -- | 0 | Stable |
| Research | 334 | -- | -- | +4 | Growing |
| Archive | 356 | -- | -- | +14 | Growing (coalesce active) |
| Reviews | 2909 | -- | -- | +84 | Growing |

**Quality metrics**:
- Critical issues: 0 (target: 0) — met
- Medium issues: 10 (target: <=3) — exceeded, persistent (unchanged 18+ periods)
- Low issues: 3 — acceptable
- Orphaned files: 13 — unchanged (18+ periods)

**Coalesce creating headroom**: Topics gained 2 slots and concepts gained 1 via coalesce. Archive grew by 14. Coalesce continues to be the primary mechanism for sustaining section capacity. With 12 coalesces executed this period (highest yet), the system is actively maintaining breathing room.

**Voids above cap**: Voids increased from 99 to 101, exceeding the 100 cap. This means expand-topic created voids content despite the cap being reached. The cap enforcement may not be functioning correctly, or research-voids output was converted to articles without a cap check.

## Changes Applied (Tier 1)

*No changes applied.*

**Rationale**: The `tune_system_history` and `locked_settings` sections required for Tier 1 change tracking still do not exist. No adjustable cadence, threshold, or weight parameters meet evidence threshold and magnitude limits. **27th report** noting this structural limitation.

## Recommendations (Tier 2)

### 1. Fix Stale content_stats and progress Counters (Carried Forward x22)

- **Proposed change**: Add file-counting logic to refresh `content_stats` and `progress` in `tools/evolution/state.py`, called at session start.
- **Rationale**: Recorded state shows 35 topics (actual: 225), 145 concepts (actual: 225), 11 voids (actual: 101), 542 reviews (actual: 2909). **22nd consecutive report.** Note: `last_runs` timestamps have partially self-corrected for cycle-triggered tasks, so this is now the most stale component.
- **Risk**: Low
- **Priority**: **Critical**

### 2. Add tune_system_history and locked_settings Sections (Carried Forward x24)

- **Proposed change**: Add both sections to evolution-state.yaml per skill specification.
- **Rationale**: Required for cooldown enforcement and locked settings checks. **24th report.** Without these, tune-system cannot make any Tier 1 changes, making it purely advisory.
- **Risk**: Low
- **Priority**: High

### 3. Add validate-all to Cycle Triggers (Carried Forward x19)

- **Proposed change**: Add `"validate-all": 2` to `CYCLE_TRIGGERS` in `tools/evolution/cycle.py`.
- **Rationale**: Has not run in 71 days. Described as "Daily health check" in CLAUDE.md but absent from automation cycle. **19th report.**
- **Risk**: Low (read-only check)
- **Priority**: Medium

### 4. Purge Unexecutable expand-topic Tasks from Queue (Carried Forward x2 — CRITICAL)

- **Proposed change**: Remove expand-topic tasks targeting sections at or near cap. Add pre-check in replenishment that verifies target section has capacity before generating expand-topic tasks.
- **Rationale**: 190 expand-topic tasks constitute 64% of the active queue but at most 10 can execute (5 topic slots + 5 concept slots). The remaining ~180 are dead weight. Each time one is picked from the queue, it wastes a cycle slot with a skip. Queue pollution has grown from 52% to 64% of active tasks despite some being consumed.
- **Risk**: Low (tasks would be skipped anyway)
- **Priority**: **Critical** — single largest source of queue waste

### 5. Fix Voids Cap Enforcement (NEW)

- **Proposed change**: Investigate and fix why voids grew to 101 despite a cap of 100. Verify that `/expand-topic` and `/research-voids` both check the cap correctly against actual file counts (not the stale `progress.voids_written: 11` value).
- **Rationale**: Voids dropped to 99 last period but grew back to 101 this period. The cap enforcement may be checking the stale recorded state (11) rather than actual file count (101). If so, the cap has effectively never been enforced.
- **Risk**: Low
- **Priority**: **High** — cap enforcement is a core architectural constraint

### 6. Implement Deep-Review Convergence Tracking (Carried Forward x13 — REGRESSED)

- **Proposed change**: Track per-article review count; skip further deep-review for articles reviewed 3+ times with minimal changes.
- **Rationale**: Zero-change rate reverted to 18.3% (from 8.8%), confirming the previous improvement was transient. Near-zero-change reviews (~25%) mean roughly 1 in 4 deep-reviews produces negligible value. Deep-review is 49% of all tasks this period (71/146). With 40 deep-review tasks still in queue, this waste will continue.
- **Risk**: Low
- **Priority**: Medium-High — waste is structural, not transient

### 7. Monitor Queue Over-Replenishment (Carried Forward x4 — NOT STABILISING)

- **Proposed change**: Add a maximum queue depth threshold (e.g., 250 P3 tasks) that suppresses replenishment.
- **Rationale**: P3 grew from 272 to 293 (+21 net), only slightly slower than last period's +29. At 296 total tasks with steady growth, the queue will reach 400 tasks within 5 tune periods. The growth is primarily in expand-topic tasks that cannot execute.
- **Risk**: Low
- **Priority**: Medium-High — growth steady, not self-correcting

### 8. Address Triple Cap Pressure (Carried Forward x7 — IMPROVING)

- **Proposed change**: Consider raising caps, or accept current state as natural quality throttle.
- **Rationale**: Topics: 5 slots (improved from 3), Concepts: 5 slots (improved from 4), Voids: above cap (101/100, regressed from 99). Coalesce continues to sustain headroom effectively — 12 coalesces this period is the highest rate yet.
- **Risk**: Low
- **Priority**: Low — coalesce is working for topics and concepts

### 9. Update Convergence Targets (Carried Forward x26)

- **Proposed change**: Update `convergence_targets` in evolution-state.yaml: min_topics 10→200, min_concepts 15→200, min_arguments 5→10, add min_voids 80, add min_apex 15.
- **Rationale**: Targets set for early-stage system. All vastly exceeded. **26th report.**
- **Risk**: Low

### 10. Systematic Citation Audit (Carried Forward x19)

- **Proposed change**: Add P2 task to audit articles flagged for unverifiable empirical claims.
- **Rationale**: This period: COGITATE results overstated (GWT), AWARE II sample size issues (NDE), Baddeley quote misattribution (GWT). Pessimistic reviews continue to flag citation/attribution issues as the most actionable category.
- **Risk**: Low

## Items for Human Review (Tier 3)

### 1. Stale State Tracking — 27th Consecutive Report

- **Issue observed**: `content_stats` and `progress` contain stale data. `tune_system_history` and `locked_settings` sections still don't exist. `last_runs` has partially self-corrected for some tasks.
- **Why human needed**: Code changes to `tools/evolution/state.py`
- **Suggested action**: Fix `content_stats`/`progress` refresh (22 reports). Add `tune_system_history` and `locked_settings` sections (24 reports). **27 reports over ~90 days.** This is the single highest-value fix available. Note that `last_runs` staleness has partially self-corrected, narrowing the scope.

### 2. Queue Pollution — 190 Unexecutable expand-topic Tasks

- **Issue observed**: 64% of the active queue consists of expand-topic tasks that largely cannot execute because all sections are near cap. The proportion has grown from 52% to 64% despite some consumption.
- **Why human needed**: Queue generation logic needs cap-awareness and potential mass cleanup
- **Suggested action**: (1) Bulk-remove expand-topic tasks for sections at or very near cap. (2) Add section-capacity check to replenishment using actual file counts (not stale recorded state).

### 3. Voids Cap Breach

- **Issue observed**: Voids grew from 99 to 101, exceeding the 100 cap. Cap enforcement appears broken.
- **Why human needed**: Diagnosis of which path bypassed the cap check — likely checking stale `progress.voids_written: 11` instead of actual file count
- **Suggested action**: Audit expand-topic and research-voids cap checking code. Ensure cap checks use filesystem counts, not evolution-state.yaml values.

### 4. Medium Issues Persistent at 10 (Carried Forward x18)

- **Issue observed**: Medium issues count has been exactly 10 for 18+ tune periods. Target is <=3.
- **Why human needed**: Deciding whether to raise target or address specific issues
- **Suggested action**: Raise `max_medium_issues` to 15

### 5. Orphaned Files Persistent at 13 (Carried Forward x5)

- **Issue observed**: Orphaned files remain at exactly 13 despite integrate-orphan tasks in queue (2 active tasks, down from 17).
- **Why human needed**: Unclear why integrate-orphan tasks aren't reducing the count. Task count dropped from 17 to 2, suggesting most were consumed, but orphan count is unchanged.
- **Suggested action**: Investigate whether the 13 orphaned files are being correctly identified and whether integration tasks actually resolve the orphan status.

## System Health Summary

| Component | Status | Notes |
|-----------|--------|-------|
| Task execution | **Excellent** | 0% hard failure rate (10th consecutive period) |
| Skip rate | **Excellent** | 2.1% (down from 4.0%) |
| Content quality | Good | 0 critical, 0 tenet warnings |
| Queue management | **Poor** | 64% of queue unexecutable, still growing |
| Queue consumption | Good | ~143 tasks consumed this period |
| Expand-topic efficiency | **Improved** | 20% skip rate (down from 60%, was N/A last period) |
| Coalesce efficiency | **Excellent** | 8.3% abandon rate (improved from 16.7%), 12 executed |
| Review system | Effective | 2909+ reviews total, +84 this period |
| Deep-review convergence | **Regressed** | 18.3% zero-change rate (up from 8.8%, confirmed transient) |
| Scheduling | Operational | Cycle mechanism working correctly |
| State tracking | **Broken** | content_stats/progress stale (27th report); last_runs partially fixed |
| Topics cap | **Improved** | 225/230 (97.8%) — 5 slots (was 3) |
| Concepts cap | **Improved** | 225/230 (97.8%) — 5 slots (was 4) |
| Voids cap | **Breached** | 101/100 — above cap (was 99, below cap) |
| Site validation | **Gap** | validate-all not running (71 days) |
| Tenet alignment | **Excellent** | 0 errors, 0 warnings across 450+ files |

## Next Tuning Session

- **Recommended**: 2026-05-05 (30 days out)
- **Focus areas**:
  - Verify stale state tracking fix (27 reports — critical)
  - Monitor queue pollution — if expand-topic still dominates, bulk cleanup is essential
  - Check whether P3 growth continues (heading toward 300+)
  - Monitor voids cap breach — is it growing further or was it addressed?
  - Track deep-review convergence rate (confirmed structural, not transient)
  - Verify validate-all integration (19 reports absent)
  - Evaluate coalesce sustainability as merge candidates narrow
