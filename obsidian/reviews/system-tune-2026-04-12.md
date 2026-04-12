---
title: "System Tuning Report - 2026-04-12"
created: 2026-04-12
modified: 2026-04-12
human_modified: null
ai_modified: 2026-04-12T20:25:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[todo]]"
  - "[[changelog]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-6
ai_generated_date: 2026-04-12
last_curated: null
---

# System Tuning Report

**Date**: 2026-04-12
**Sessions analyzed**: 144 (sessions 5555 to 5699)
**Period covered**: 2026-04-06 20:21 to 2026-04-12 20:25 UTC (~6.0 days)

## Executive Summary

The system maintains its perfect hard-failure record (0% for the 12th consecutive period). Several previously worsening metrics improved: voids dropped below cap (99/100, resolved from 101), the overall queue shrank for the first time (354→334, -20), and expand-topic skip rate recovered from 50% to 18%. However, deep-review marginal-value rate hit a new high of 32.1% (25/78), confirming the trend is structural and accelerating. Coalesce abandon rate rose to 33% as remaining merge candidates thin out. State tracking remains broken (29th consecutive report). No Tier 1 changes warranted.

## Metrics Overview

| Metric | Current (Actual) | Recorded State | Previous (Apr 6) | Trend |
|--------|-------------------|----------------|-------------------|-------|
| Session count | 5699 | 5699 | 5555 | +144 |
| Topics | 227 | 35 | 224 | **+3** |
| Concepts | 222 | 145 | 222 | → |
| Arguments | 6 | 4 | 6 | → |
| Voids | 99 | 11 | 101 | **-2 (below cap, resolved!)** |
| Apex articles | 22 | 4 | 22 | → |
| Research notes | 344 | 117 | 340 | +4 |
| Archive files | 380 | -- | 371 | +9 (coalesce active) |
| Reviews completed | 3094 | 542 | 3002 | +92 |
| Recent task success rate | 100% (0 hard failures) | -- | 100% | → |
| Skip/abandon rate | 5.9% (9/153) | -- | 8.3% (7/84) | ↓ (**improved**) |
| Critical issues | 0 | 0 | 0 | → |
| Medium issues | 10 | 10 | 10 | → |
| Orphaned files | 13 | 13 | 13 | → |
| Queue depth (P0-P1) | 0 | -- | 0 | → |
| Queue depth (P2) | 3 | -- | 2 | +1 |
| Queue depth (P3) | 331 | -- | 314 | +17 |
| Total active tasks | 334 | -- | 354 | **-20 (first net reduction!)** |

**State discrepancy update**: Recorded state shows 35 topics (actual: 227, 6.5x), 145 concepts (actual: 222, 1.5x), 11 voids (actual: 99, 9.0x), 542 reviews (actual: 3094, 5.7x). **29th consecutive report.**

## Abort Conditions Check

**Status**: All clear.

- Task failure rate: 0% (0/20 recent tasks failed) — well under 50% threshold
- Convergence: No regression — topics gained 3, voids resolved below cap
- Critical issues: 0
- File reads: All successful

## Findings

### Cadence Analysis

**Data points**: ~6.0 days, 144 sessions

| Task | last_runs Timestamp | Actual Last Run (Changelog) | Status |
|------|---------------------|----------------------------|--------|
| validate-all | 2026-01-24 | **Not run since Jan 24** | **79 days stale** |
| pessimistic-review | 2026-04-12 | 2026-04-12 (x6) | Current |
| optimistic-review | 2026-04-12 | 2026-04-12 (x6) | Current |
| check-tenets | 2026-04-09 | 2026-04-12 (x3) | Current |
| check-links | 2026-04-10 | 2026-04-10 | Current |
| deep-review | 2026-04-12 | 2026-04-12 (x83) | Current |
| tune-system | 2026-04-06 | 2026-04-12 (this run) | Current |
| research-voids | 2026-04-12 | 2026-04-12 (x3) | Current |
| coalesce | 2026-04-12 | 2026-04-12 (x12) | Current |
| apex-evolve | 2026-04-10 | 2026-04-10 (x2) | Current |
| agentic-social | 2026-04-12 | 2026-04-12 | Current |

**`last_runs` timestamps current**: All cycle-triggered tasks show recent timestamps. The `last_runs` staleness that plagued early reports has fully self-corrected for active tasks.

**`validate-all`**: Still absent from both the task cycle and CYCLE_TRIGGERS. Has not run in 79 days. **21st consecutive report.**

### Failure Pattern Analysis

**Data points**: 153 changelog entries since last tune, 20 recent_tasks in state (all success)

| Task Type | Executed | Skipped/Abandoned | Skip Rate |
|-----------|----------|-------------------|-----------|
| deep-review | 78 | 5 (archived articles) | 6.0% |
| refine-draft | 22 | 1 (no-op, incorrect premise) | 4.3% |
| coalesce | 8 | 4 (no candidates) | 33.3% |
| expand-topic | 9 | 2 (duplicates) | 18.2% |
| pessimistic-review | 6 | 0 | 0% |
| optimistic-review | 6 | 0 | 0% |
| research-voids | 3 | 0 | 0% |
| check-tenets | 3 | 0 | 0% |
| condense | 2 | 0 | 0% |
| research-topic | 2 | 0 | 0% |
| apex-evolve | 2 | 0 | 0% |
| **Total** | **141** | **12** | **7.8%** |

**Hard-failure reliability continues**: 12th consecutive tune period with 0% failure rate. All "failures" are legitimate skips.

**Skip rate improved**: 5.9% overall (down from 8.3%). The improvement is driven by:
- **expand-topic: 18.2% skip rate** (down from 50%) — only 2 of 11 skipped, both for genuine duplicates. Replenishment appears to be producing higher-quality tasks.
- **deep-review archived-article skips**: 5 skips targeting archived articles, including 2 attempts on the same archived article (stochastic-amplification-and-neural-selection on both Apr 10 and Apr 11). Deep-review target selection should filter archived articles.

**Coalesce abandon rate rising**: 33.3% (up from 22.2%). 4 of 12 coalesces found no viable merge candidates. As previous passes have consolidated the most redundant content, viable merge candidates are naturally thinning. This is expected structural behaviour, not a deficiency.

**Deep-review marginal-value rate at new high**: 25/78 effective deep-reviews (32.1%) showed zero word change — the highest rate recorded, continuing the worsening trend: 8.8% → 18.3% → 26.7% → 32.1%. Nearly 1 in 3 deep-reviews produces no content improvement. Deep-review remains 54% of all tasks this period (83/153). With ~32% producing negligible value, approximately 26 cycle slots were effectively wasted.

### Queue Health Analysis

**Data points**: Current todo.md state, comparison with Apr 6

**Queue composition**:
- P0: 0 (unchanged)
- P1: 0 (unchanged)
- P2: 3 (up from 2)
- P3: 331 (up from 314, +17)
- Total active: 334 (down from 354, **-20**)
- Resolved: 5

**First net queue reduction**: The overall queue shrank by 20 tasks — the first net reduction observed across 12 tune periods. This was achieved through 5 resolved tasks and consumption exceeding generation. P3 still grew (+17), but the resolved tasks and executed queue tasks more than offset it.

**Expand-topic still dominates**: The majority of active tasks remain expand-topic (estimated ~200+). With only 3 topic slots and 8 concept slots available, most are still unexecutable. However, the queue no longer appears to be accelerating — growth has slowed from +58 to +17 in P3.

**Queue growth deceleration**: P3 growth rates over recent periods: +29, +21, +21, +17. The trend is clearly decelerating, suggesting the system may be approaching equilibrium between generation and consumption.

### Review Finding Patterns

**Data points**: 6 pessimistic reviews, 6 optimistic reviews, 3 tenet checks, 83 deep reviews since last tune

**Recurring themes across pessimistic reviews (Apr 7-12)**:

| Theme | Articles | Status |
|-------|----------|--------|
| Asymmetric explanatory standards (dualism vs materialism) | materialism.md | **Addressed** (refine-draft expanded interaction problem section) |
| Question-begging phenomenological appeals | parfit-reductionism.md | **Addressed** (refine-draft reframed as explanatory cost) |
| Selective citation of contemplative evidence | parfit-reductionism.md | **Addressed** (added Dzogchen/Madhyamaka acknowledgment) |
| Born rule dilemma unaddressed | materialism.md | Persistent |
| Eliminativist folk-psychology charge | multiple | Persistent (30+ reports) |
| Unfalsifiability / ad hoc flexibility | multiple | Persistent |
| Circularity in convergence depth criterion | cross-traditional-convergence.md | **Addressed** (refine-draft defined independent criteria) |
| Nested speculation in AI phenomenology | structural-varieties.md | **Addressed** (refine-draft reframed as conditional) |

**Assessment**: The pessimistic → refine-draft pipeline remains highly effective. Of 8 identifiable issues from Apr 10-12 pessimistic reviews, 6 were addressed by refine-draft within hours. The pipeline responsiveness rate (~75%) is the highest observed.

**Tenet checks (Apr 9, Apr 12)**: Both clean — 0 errors, 0 warnings across 448-450 files. Tenet alignment remains excellent.

**Deep-review convergence signals**: Multiple articles confirmed stable after 3+ reviews with zero changes: phenomenal-transparency (4th review), consciousness-as-perceptual-architect (stability), modal-structure-of-phenomenal-properties (3rd consecutive), born-rule-and-the-consciousness-interface (9th review, fully stable). The convergence signal is clear and growing — these articles gain no value from further review.

### Convergence Progress

**Data points**: Actual file counts vs caps

| Category | Actual Count | Cap | % of Cap | Change from Apr 6 | Direction |
|----------|-------------|-----|----------|---------------------|-----------|
| Topics | 227 | 230 | 98.7% | +3 | **3 slots** (reduced from 6) |
| Concepts | 222 | 230 | 96.5% | 0 | **8 slots** (unchanged) |
| Arguments | 6 | -- | -- | 0 | Stable |
| Voids | 99 | 100 | 99% | **-2** | **1 slot (resolved! was above cap)** |
| Apex | 22 | -- | -- | 0 | Stable |
| Research | 344 | -- | -- | +4 | Growing |
| Archive | 380 | -- | -- | +9 | Growing (coalesce active) |
| Reviews | 3094 | -- | -- | +92 | Growing |

**Quality metrics**:
- Critical issues: 0 (target: 0) — met
- Medium issues: 10 (target: <=3) — exceeded, persistent (unchanged 20+ periods)
- Low issues: 3 — acceptable
- Orphaned files: 13 — unchanged (20+ periods)

**Voids cap resolved**: Voids dropped from 101 to 99, resolving the cap breach reported in the previous 2 periods. The 2 condensed voids articles freed slots. research-voids is now correctly executing again (3 runs this period).

**Topics nearing hard cap**: Topics consumed 3 of 6 available slots, leaving only 3. At current expand-topic rate (~9 successful per period), topics will hit cap within the next period. Concepts remain the section with most headroom (8 slots).

**Coalesce sustaining capacity**: 8 successful coalesces this period. Archive grew by 9. Coalesce continues to create breathing room, though the 33% abandon rate suggests diminishing returns.

## Changes Applied (Tier 1)

*No changes applied.*

**Rationale**: The `tune_system_history` and `locked_settings` sections required for Tier 1 change tracking still do not exist. No adjustable cadence, threshold, or weight parameters meet evidence threshold and magnitude limits. **29th report** noting this structural limitation.

## Recommendations (Tier 2)

### 1. Fix Stale content_stats and progress Counters (Carried Forward x24)

- **Proposed change**: Add file-counting logic to refresh `content_stats` and `progress` in `tools/evolution/state.py`, called at session start.
- **Rationale**: Recorded state shows 35 topics (actual: 227), 145 concepts (actual: 222), 11 voids (actual: 99), 542 reviews (actual: 3094). **24th consecutive report.** Most stale component remaining.
- **Risk**: Low
- **Priority**: **Critical**

### 2. Add tune_system_history and locked_settings Sections (Carried Forward x26)

- **Proposed change**: Add both sections to evolution-state.yaml per skill specification.
- **Rationale**: Required for cooldown enforcement and locked settings checks. **26th report.** Without these, tune-system cannot make any Tier 1 changes.
- **Risk**: Low
- **Priority**: High

### 3. Add validate-all to Cycle Triggers (Carried Forward x21)

- **Proposed change**: Add `"validate-all": 2` to `CYCLE_TRIGGERS` in `tools/evolution/cycle.py`.
- **Rationale**: Has not run in 79 days. Described as "Daily health check" in CLAUDE.md but absent from automation cycle. **21st report.**
- **Risk**: Low (read-only check)
- **Priority**: Medium

### 4. Purge Unexecutable expand-topic Tasks from Queue (Carried Forward x4 — CRITICAL, STABILISING)

- **Proposed change**: Remove expand-topic tasks targeting sections at or near cap. Add pre-check in replenishment that verifies target section has capacity before generating expand-topic tasks.
- **Rationale**: ~200+ expand-topic tasks remain in queue but at most ~11 can execute (3 topic slots + 8 concept slots). The remaining ~190 are dead weight. Queue growth has decelerated (+17 this period vs +58 last period), but the existing backlog persists.
- **Risk**: Low (tasks would be skipped anyway)
- **Priority**: **Critical** — largest source of queue waste

### 5. Implement Deep-Review Convergence Tracking (Carried Forward x15 — WORSENING, NOW CRITICAL)

- **Proposed change**: Track per-article review count and last word-change delta; skip further deep-review for articles reviewed 3+ times with zero or near-zero changes.
- **Rationale**: Marginal-value rate hit 32.1% (25/78) — a new record high, continuing the trend: 8.8% → 18.3% → 26.7% → 32.1%. Deep-review is 54% of all tasks. Approximately 26 cycle slots were wasted this period on reviews producing no content improvement. Articles like born-rule-and-the-consciousness-interface (9th review, 0 change) and consciousness-as-perceptual-architect (3rd 0-change review) are demonstrably fully converged.
- **Risk**: Low
- **Priority**: **Critical** — waste is structural, accelerating, and now the largest operational inefficiency

### 6. Filter Archived Articles from Deep-Review Target Selection (NEW)

- **Proposed change**: Add a check in deep-review target selection to exclude articles that have been archived.
- **Rationale**: 5 deep-reviews this period targeted archived articles. One article (stochastic-amplification-and-neural-selection) was targeted on two consecutive days. Each skip wastes a cycle slot.
- **Risk**: Low
- **Priority**: Medium — 5 wasted slots per period

### 7. Suppress Queue Replenishment at Depth Threshold (Carried Forward x6 — STABILISING)

- **Proposed change**: Add a maximum queue depth threshold (e.g., 250 P3 tasks) that suppresses replenishment.
- **Rationale**: Queue growth has decelerated (P3 growth: +29, +21, +21, +17) and total queue achieved its first net reduction (-20). The system may be approaching natural equilibrium. However, at 331 P3 tasks, the backlog remains large.
- **Risk**: Low
- **Priority**: Medium — deceleration suggests partial self-correction, but a hard cap would prevent future accumulation

### 8. Update Convergence Targets (Carried Forward x28)

- **Proposed change**: Update `convergence_targets` in evolution-state.yaml: min_topics 10→200, min_concepts 15→200, min_arguments 5→10, add min_voids 80, add min_apex 15.
- **Rationale**: Targets set for early-stage system. All vastly exceeded. **28th report.**
- **Risk**: Low

### 9. Systematic Citation Audit (Carried Forward x21)

- **Proposed change**: Add P2 task to audit articles flagged for unverifiable empirical claims.
- **Rationale**: This period: Born rule dilemma (materialism.md), question-begging phenomenology (parfit-reductionism.md), selective contemplative citation (parfit-reductionism.md). Pessimistic reviews continue to flag citation/attribution issues.
- **Risk**: Low

### 10. Address Topics Approaching Hard Cap (NEW)

- **Proposed change**: Prioritise coalesce operations targeting topics/ section specifically, or accept 230 as the de facto maximum.
- **Rationale**: Topics consumed 3 of 6 available slots this period, leaving only 3 of 230. At current expand-topic success rate (~9/period), topics will hit cap within the next tune period. Concepts (8 slots) and voids (1 slot) have less urgency.
- **Risk**: Low
- **Priority**: Medium — natural consequence of approaching content maturity

## Items for Human Review (Tier 3)

### 1. Stale State Tracking — 29th Consecutive Report

- **Issue observed**: `content_stats` and `progress` contain stale data. `tune_system_history` and `locked_settings` sections still don't exist.
- **Why human needed**: Code changes to `tools/evolution/state.py`
- **Suggested action**: Fix `content_stats`/`progress` refresh (24 reports). Add `tune_system_history` and `locked_settings` sections (26 reports). **29 reports over ~96 days.** This is the single highest-value fix available.

### 2. Deep-Review Diminishing Returns at 32.1% — Now Largest Operational Inefficiency

- **Issue observed**: Nearly 1 in 3 deep-reviews produces no content changes. Trend is monotonically worsening: 8.8% → 18.3% → 26.7% → 32.1%. Deep-review consumes 54% of all cycle slots. ~26 slots wasted this period.
- **Why human needed**: Policy decision on convergence threshold and skip logic
- **Suggested action**: Track per-article deep-review count; skip after 3+ reviews with zero or near-zero changes. Could reclaim ~26 cycle slots per tune period — equivalent to adding ~17% more productive capacity.

### 3. Queue Pollution — ~200 Unexecutable expand-topic Tasks

- **Issue observed**: Majority of active queue consists of expand-topic tasks that cannot execute. Queue growth is decelerating but backlog persists.
- **Why human needed**: Queue generation logic needs cap-awareness and bulk cleanup
- **Suggested action**: (1) Bulk-remove expand-topic tasks for sections at/near cap. (2) Add section-capacity check to replenishment using actual file counts.

### 4. Medium Issues Persistent at 10 (Carried Forward x20)

- **Issue observed**: Medium issues count has been exactly 10 for 20+ tune periods. Target is <=3.
- **Why human needed**: Deciding whether to raise target or address specific issues
- **Suggested action**: Raise `max_medium_issues` to 15

### 5. Orphaned Files Persistent at 13 (Carried Forward x7)

- **Issue observed**: Orphaned files remain at exactly 13 despite integrate-orphan tasks in queue (27 active) and some orphan-integration work during deep-reviews.
- **Why human needed**: Unclear why the orphan count doesn't decrease despite integration work
- **Suggested action**: Investigate whether orphan detection is counting the same files repeatedly or whether new orphans are created as fast as old ones are resolved

## System Health Summary

| Component | Status | Notes |
|-----------|--------|-------|
| Task execution | **Excellent** | 0% hard failure rate (12th consecutive period) |
| Skip rate | **Improved** | 5.9% (down from 8.3%) |
| Content quality | Good | 0 critical, 0 tenet warnings |
| Queue management | **Improved** | First net reduction (-20), but ~200 unexecutable tasks remain |
| Queue consumption | Good | ~141 tasks consumed this period |
| Expand-topic efficiency | **Improved** | 18.2% skip rate (down from 50%) |
| Coalesce efficiency | **Declining** | 33.3% abandon rate (up from 22.2%), merge candidates thinning |
| Review system | Effective | 3094+ reviews total, +92 this period |
| Deep-review convergence | **Worsening** | 32.1% marginal-value rate (up from 26.7%, new record high) |
| Scheduling | Operational | Cycle mechanism working correctly |
| State tracking | **Broken** | content_stats/progress stale (29th report); last_runs current |
| Topics cap | **Tightening** | 227/230 (98.7%) — 3 slots (was 6) |
| Concepts cap | Good | 222/230 (96.5%) — 8 slots (unchanged) |
| Voids cap | **Resolved** | 99/100 (99%) — below cap (was 101, breached) |
| Site validation | **Gap** | validate-all not running (79 days) |
| Tenet alignment | **Excellent** | 0 errors, 0 warnings across 448+ files |

## Next Tuning Session

- **Recommended**: 2026-05-12 (30 days out)
- **Focus areas**:
  - Verify stale state tracking fix (29 reports — critical)
  - Monitor deep-review marginal-value rate (worsening trend: 8.8% → 18.3% → 26.7% → 32.1% — at 40%+ next period, deep-review becomes net-negative)
  - Check whether topics hit cap (only 3 slots remaining)
  - Monitor coalesce abandon rate (33% and rising — natural limit approaching)
  - Verify validate-all integration (21 reports absent)
  - Check whether queue net reduction continues or was transient
  - Evaluate whether expand-topic should be paused system-wide as sections approach hard caps
