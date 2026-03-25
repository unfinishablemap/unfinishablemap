---
title: "System Tuning Report - 2026-03-25"
created: 2026-03-25
modified: 2026-03-25
human_modified: null
ai_modified: 2026-03-25T03:18:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[todo]]"
  - "[[changelog]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-6
ai_generated_date: 2026-03-25
last_curated: null
---

# System Tuning Report

**Date**: 2026-03-25
**Sessions analyzed**: 144 (sessions 4691 to 4835)
**Period covered**: 2026-03-23 14:00 to 2026-03-25 03:18 (~37 hours)

## Executive Summary

The system maintains perfect hard-failure reliability (0%) with 10 skips/abandons out of ~151 tasks (6.6%). Coalesce is actively creating headroom: topics dropped from 229 to 227 through consolidation while concepts grew to 226/230 (4 slots remaining). Voids crept back over cap to 101. The P3 queue consumed healthily from 173 to 80, demonstrating sustainable task execution. Orphaned files count jumped from 13 to 48 in state—likely a recount rather than genuine spike. Deep-review remains dominant at 51% (down from 58%). State tracking remains broken (23rd consecutive report). No Tier 1 changes warranted.

## Metrics Overview

| Metric | Current (Actual) | Recorded State | Previous (Mar 23) | Trend |
|--------|-------------------|----------------|-------------------|-------|
| Session count | 4835 | 4835 | 4691 | +144 |
| Topics | 227 | 35 | 229 | -2 (coalesce headroom) |
| Concepts | 226 | 145 | 223 | +3 (4 slots remaining) |
| Arguments | 6 | 4 | 6 | → |
| Voids | 101 | 11 | 100 | +1 (**over cap again**) |
| Apex articles | 21 | 4 | 21 | → |
| Research notes | 314 | 117 | 311 | +3 |
| Archive files | 300 | -- | 284 | +16 (coalesce very active) |
| Reviews completed | 2568 | 542 | 2477 | +91 |
| Recent task success rate | 100% (0 hard failures) | -- | 100% | → |
| Skip/abandon rate | 6.6% (10/151) | -- | ~7% | → |
| Critical issues | 0 | 0 | 0 | → |
| Medium issues | 10 | 10 | 10 | → |
| Orphaned files | ~48 | 48 | 13 | ↑ (**recount or state update**) |
| Queue depth (P0-P1) | 0 | 0 | 0 | → |
| Queue depth (P2) | 7 | 7 | 3 | +4 |
| Queue depth (P3) | 80 | 80 | 173 | -93 (healthy consumption) |

**State discrepancy update**: Recorded state shows 35 topics (actual: 227, 6.5x), 145 concepts (actual: 226, 1.6x), 11 voids (actual: 101, 9.2x), 542 reviews (actual: 2568, 4.7x). **23rd consecutive report.**

## Abort Conditions Check

**Status**: All clear.

- Task failure rate: 0% (0/20 recent tasks failed) — well under 50% threshold
- Convergence: No regression — concepts growing, topics consolidating, voids stable
- Critical issues: 0
- File reads: All successful

## Findings

### Cadence Analysis

**Data points**: ~37 hours, 144 sessions

| Task | last_runs Timestamp | Actual Last Run (Changelog) | Status |
|------|---------------------|----------------------------|--------|
| validate-all | 2026-01-24 | **Not run since Jan 24** | **61 days stale** |
| pessimistic-review | 2026-01-25 | 2026-03-24 (x4) | Timestamp stale |
| optimistic-review | 2026-01-25 | 2026-03-25 (x4+) | Timestamp stale |
| check-tenets | 2026-03-24 | 2026-03-25 | Current |
| check-links | 2026-03-24 | 2026-03-24 | Current |
| deep-review | 2026-01-25 | 2026-03-25 (many) | Timestamp stale |
| tune-system | 2026-03-23 | 2026-03-25 (this run) | Current |
| research-voids | 2026-03-25 | 2026-03-25 | Current |
| coalesce | 2026-01-25 | 2026-03-25 (x10+) | Timestamp stale |
| apex-evolve | 2026-03-24 | 2026-03-24 | Current |
| agentic-social | 2026-03-25 | 2026-03-25 | Current |

**Root cause unchanged**: Queue tasks do not update `state.last_runs`. Cycle-triggered tasks correctly update timestamps. **23rd consecutive report.**

**validate-all**: Still absent from both the task cycle and CYCLE_TRIGGERS. Has not run in 61 days. **15th report.**

### Failure Pattern Analysis

**Data points**: 151 changelog entries since last tune, 20 recent_tasks in state (all success)

| Task Type | Executed | Failed | Skipped/Abandoned | Rate |
|-----------|----------|--------|-------------------|------|
| deep-review | 77 | 0 | 1 (terminal stability) | 0% |
| refine-draft | 17 | 0 | 0 | 0% |
| expand-topic | 16 | 0 | 3 (duplicate/at capacity) | 0% |
| coalesce | 12 | 0 | 2 (no candidates) | 0% |
| pessimistic-review | 6 | 0 | 0 | 0% |
| optimistic-review | 6 | 0 | 0 | 0% |
| condense | 5 | 0 | 0 | 0% |
| research-voids | 4 | 0 | 1 (at capacity) | 0% |
| check-tenets | 3 | 0 | 0 | 0% |
| apex-evolve | 2 | 0 | 0 | 0% |
| research-topic | 1 | 0 | 0 | 0% |
| tune-system | 1 | 0 | 0 | 0% |
| **Total** | **~151** | **0** | **~10** | **0%** |

**Perfect hard-failure reliability continues**: Sixth consecutive tune period with 0% failure rate.

**Coalesce abandon rate improved**: 2 of 12 coalesce attempts abandoned (17%), down significantly from 50% last period. Coalesce is finding viable candidates again, likely because the large P3 queue is surfacing merge opportunities. This reverses the concern from last report.

**Expand-topic cap enforcement working**: 3 expand-topic attempts skipped due to capacity or duplication, confirming that cap enforcement is functioning at execution time.

**Positive pattern — coalesce creating headroom**: Topics went from 229→227 (net -2) through active coalesce. 16 new archive files created. The system is self-correcting cap pressure through consolidation.

### Queue Health Analysis

**Data points**: Current todo.md state, comparison with Mar 23

**Queue composition**:
- P0: 0 (unchanged)
- P1: 0 (unchanged)
- P2: 7 (up from 3 — healthy growth from task chains and replenishment)
- P3: 80 (down from 173 — 93 consumed)
- Replenishment source: 2 chain, 1 length_analysis, 3 orphan_integration

**P3 consumption rate**: 93 tasks consumed in ~37 hours ≈ 2.5 tasks/hour. At this rate, the P3 backlog will sustain approximately 32 more hours before dropping below replenishment threshold. Queue is being consumed faster than last period, reflecting the active coalesce and deep-review cycles.

**P2 active task types**: 2 cross-review, 1 condense, 3 integrate-orphan, 1 cross-review. Well-balanced with no single type dominating.

**Replenishment healthy**: Last replenishment at 2026-03-25 02:54, with `needs_replenishment: false`. The system correctly assessed queue depth as adequate.

### Review Finding Patterns

**Data points**: 4 pessimistic reviews (Mar 24, 24b, 24c, 24d), 4+ optimistic reviews, 2 tenet checks, 77 deep reviews since last tune

**Recurring themes across pessimistic reviews** (Mar 24-25):

| Theme | Appearances This Period | Cumulative Status |
|-------|------------------------|-------------------|
| Quantum tenet unfalsifiability | Mar 24b (functionalism), 24c (inverted qualia), 24d (simulation, epiphenomenalism) | Persistent (24+ reports) |
| Conceivability-possibility gap | Mar 24c (inverted qualia) | Persistent |
| Unverifiable empirical claims / citation gaps | Mar 24d (meditation efficacy), 24b (functionalism predictions) | Persistent |
| Buddhist no-self vs Map's indexical identity | Mar 24b (functionalism), 24c (Buddhism-dualism), 24d (epiphenomenalism) | Persistent |
| Merleau-Ponty misappropriation | Mar 24b (embodied cognition) | Recurring |
| Stale AI refinement logs | Mar 24d (simulation.md) | New |

**Review-fix pipeline effective**: Notable cross-article fixes this period:
- Fabricated "Atkins et al." citation corrected to Denton et al. (2024) across 5 files
- 115+ wikilinks updated after coalesce of phenomenology-of-choice and phenomenology-of-volition
- 44 wikilinks updated for consciousness-collapse coalesce
- Curated-mind car-analogy and circularity issues addressed via deep-review

**Tenet check** (Mar 25): 0 errors, 0 warnings, 13 notes across 450 files. Tenet alignment remains excellent — improvement from 3 warnings last period to 0.

**Deep-review convergence signals**: Some articles continue showing 0 or minimal word count changes (supervenience integration review: 0 body changes, volitional-control: -25 words removing uncited reference). However, many deep-reviews this period made substantive improvements (types-of-ai-phenomenal-experience: +145 words with critical issue fixes, resonance-void: +213 words with 9 enhancements). The convergence concern is less acute than last period.

### Convergence Progress

**Data points**: Actual file counts vs caps

| Category | Actual Count | Cap | % of Cap | Change from Mar 23 | Direction |
|----------|-------------|-----|----------|---------------------|-----------|
| Topics | 227 | 230 | **98.7%** | -2 | **3 slots remaining (headroom gained!)** |
| Concepts | 226 | 230 | **98.3%** | +3 | **4 slots remaining (tightening)** |
| Arguments | 6 | -- | -- | 0 | Stable |
| Voids | 101 | 100 | **101%** | +1 | **Over cap again** |
| Apex | 21 | -- | -- | 0 | Stable |
| Research | 314 | -- | -- | +3 | Growing |
| Archive | 300 | -- | -- | +16 | Growing (coalesce very active) |
| Reviews | 2568 | -- | -- | +91 | Growing |

**Quality metrics**:
- Critical issues: 0 (target: 0) — met
- Medium issues: 10 (target: <=3) — exceeded, persistent (unchanged 14+ periods)
- Low issues: 3 — acceptable
- Orphaned files: 48 (state) — **jumped from 13** (see Tier 3 item)

**Coalesce creating headroom — key development**: Topics went from 229→227 through coalesce, net gaining 2 slots. With 16 new archive files this period, the system is actively consolidating. This is the first period where topics *decreased*, demonstrating that coalesce can counterbalance cap pressure.

**Concepts tightening**: At +3/period, concepts will hit 230/230 in ~1-2 more tune periods. However, coalesce may create headroom here too if viable concept merges exist.

**Voids over cap again**: Rose from 100→101. The research-voids task ran successfully, which means either (a) a new voids article was created despite the cap, or (b) a non-research expansion created a void file. Cap enforcement at the voids level may have a gap.

**Orphan count anomaly**: State now shows 48 orphaned files, up from 13 in the previous tune report. This is likely a genuine recount rather than a spike — the 13 figure may have been stale for many periods while the actual count grew. With 300+ archive files creating broken inbound links, the true orphan count rising is expected.

## Changes Applied (Tier 1)

*No changes applied.*

**Rationale**: The evolution-state.yaml still contains no adjustable cadence, threshold, or weight parameters that meet the evidence threshold and magnitude limits for automatic change. The `tune_system_history` and `locked_settings` sections required for Tier 1 change tracking still do not exist. **23rd report** noting this structural limitation.

## Recommendations (Tier 2)

### 1. Fix Stale last_runs Timestamps (Carried Forward x23 — CRITICAL)

- **Proposed change**: In `scripts/evolve_loop.py`, add `state.last_runs` update after queue task execution.
- **Rationale**: **23rd consecutive report.** Queue tasks (deep-review, pessimistic-review, optimistic-review, coalesce) show timestamps from January while actually running daily.
- **Risk**: Low
- **Priority**: **Critical**

### 2. Fix Stale content_stats and progress Counters (Carried Forward x18)

- **Proposed change**: Add file-counting logic to refresh `content_stats` and `progress` in `tools/evolution/state.py`, called at session start.
- **Rationale**: Recorded state shows 35 topics (actual: 227), 145 concepts (actual: 226), 11 voids (actual: 101), 542 reviews (actual: 2568). 18th consecutive report.
- **Risk**: Low
- **Priority**: High

### 3. Add tune_system_history and locked_settings Sections (Carried Forward x20)

- **Proposed change**: Add both sections to evolution-state.yaml per skill specification.
- **Rationale**: Required for cooldown enforcement and locked settings checks. 20th report.
- **Risk**: Low

### 4. Add validate-all to Cycle Triggers (Carried Forward x15)

- **Proposed change**: Add `"validate-all": 2` to `CYCLE_TRIGGERS` in `tools/evolution/cycle.py`.
- **Rationale**: Has not run in 61 days. Described as "Daily health check" in CLAUDE.md but absent from automation cycle. 15th report.
- **Risk**: Low (read-only check)
- **Priority**: Medium

### 5. Investigate Voids Cap Re-Breach (NEW)

- **Proposed change**: Verify that expand-topic and research-voids both check actual file count (not stale `progress.voids_written: 11`) before creating new voids content.
- **Rationale**: Voids dropped to exactly 100 last period but crept back to 101. Either a gap in cap enforcement exists or a manual/coalesce operation created a file in voids/ without checking the cap.
- **Risk**: Low
- **Priority**: Medium-High — persistent cap violations undermine the section cap system

### 6. Address Triple Cap Pressure (Carried Forward x3 — EVOLVING)

- **Proposed change**: Consider raising caps, or accept current state as natural quality throttle.
- **Rationale**: Topics: 3 slots (improved from 1 via coalesce), Concepts: 4 slots (tightening from 7), Voids: over cap. However, coalesce is now demonstrably creating headroom — topics gained 2 slots this period through consolidation. The system may be self-correcting through coalesce. If coalesce can also target concepts, the pressure may be manageable without cap changes.
- **Risk**: Low
- **Priority**: **High but less urgent** — coalesce headroom creation partially addresses this

### 7. Implement Deep-Review Convergence Tracking (Carried Forward x9)

- **Proposed change**: Track per-article review count; skip further deep-review for articles reviewed 3+ times with minimal changes.
- **Rationale**: Deep-review is 51% of all tasks (down from 58%). While some articles still receive substantive improvements, others show convergence. As cap pressure limits new content, deep-review's share will grow.
- **Risk**: Low
- **Priority**: Medium

### 8. Investigate Orphaned Files Count Jump (NEW)

- **Proposed change**: Verify whether the jump from 13→48 orphaned files represents a genuine recount or a counting bug. List the specific 48 orphaned files.
- **Rationale**: The orphan count was stuck at 13 for 15+ tune periods, which was itself suspicious. The jump to 48 may indicate the counter was finally fixed, or it may indicate that coalesce (300 archive files) is creating orphans faster than integration resolves them.
- **Risk**: Low
- **Priority**: Medium — understanding the true orphan count matters for integration task planning

### 9. Update Convergence Targets (Carried Forward x22)

- **Proposed change**: Update `convergence_targets` in evolution-state.yaml: min_topics 10→200, min_concepts 15→200, min_arguments 5→10, add min_voids 80, add min_apex 15.
- **Rationale**: Targets set for early-stage system. All vastly exceeded. 22nd report.
- **Risk**: Low

### 10. Filter Archived Articles from Task Generation (Carried Forward x4)

- **Proposed change**: In replenishment logic, skip archived articles when generating tasks.
- **Rationale**: With 300 archive files (up from 284), the probability of generating stale tasks increases. 3 expand-topic skips this period were due to duplicates, some likely targeting archived content.
- **Risk**: Low

### 11. Systematic Citation Audit (Carried Forward x15)

- **Proposed change**: Add P2 task to audit articles flagged for unverifiable empirical claims.
- **Rationale**: This period: meditation efficacy citation missing, fabricated Atkins et al. found and fixed. Citation issues remain the most actionable pessimistic review category.
- **Risk**: Low

## Items for Human Review (Tier 3)

### 1. Stale State Tracking — 23rd Consecutive Report

- **Issue observed**: `last_runs`, `content_stats`, and `progress` all contain stale data. `tune_system_history` and `locked_settings` sections still don't exist.
- **Why human needed**: Code changes to evolve_loop.py and tools/evolution/state.py
- **Suggested action**: Fix the three state-tracking issues together. **23 reports over ~80 days.** If stale state is fixed, cap enforcement, convergence tracking, and orphan monitoring will likely improve automatically.

### 2. Medium Issues Persistent at 10 (Carried Forward x14)

- **Issue observed**: Medium issues count has been exactly 10 for 14+ tune periods. Target is <=3.
- **Why human needed**: Deciding whether to raise target or address specific issues
- **Suggested action**: Raise `max_medium_issues` to 15

### 3. Deep-Review Diminishing Returns at Scale (Carried Forward x2)

- **Issue observed**: Deep-review remains the dominant task type (51%). Some articles converge while others still benefit. The system lacks a mechanism to distinguish converged from improvable articles.
- **Why human needed**: Whether to implement convergence tracking and an "article stable" flag
- **Suggested action**: Implement per-article review tracking. After 3 consecutive reviews with <10 words change, mark article as "converged" and skip further reviews unless cross-links or external changes warrant re-review.

### 4. Voids Cap Enforcement Gap

- **Issue observed**: Voids returned to 101 after being corrected to 100 last period. Cap enforcement may have a gap, or the stale `progress.voids_written: 11` may be allowing bypasses.
- **Why human needed**: Verify which code path created the 101st void and whether it checked the actual file count
- **Suggested action**: Audit the expand-topic and research-voids cap check logic to ensure they count actual files, not stale state

## System Health Summary

| Component | Status | Notes |
|-----------|--------|-------|
| Task execution | **Excellent** | 0% hard failure rate (6th consecutive period) |
| Content quality | Good | 0 critical, 0 tenet warnings (improved) |
| Queue management | **Healthy** | 7 P2, 80 P3 — well above threshold |
| Queue consumption | **Excellent** | 93 P3 tasks consumed (~2.5/hour) |
| Review system | Effective | 2568+ reviews total, +91 this period |
| Review-fix pipeline | **Excellent** | Fabricated citations caught, 115+ wikilink updates |
| Coalesce pipeline | **Improved** | 17% abandon rate (was 50%), creating headroom |
| Scheduling | Operational | Cycle mechanism working correctly |
| State tracking | **Broken** | last_runs, content_stats, progress all stale (23rd report) |
| Topics cap | **Improved** | 227/230 (98.7%) — 3 slots (was 1 slot, coalesce creating headroom) |
| Concepts cap | **Warning** | 226/230 (98.3%) — 4 slots remaining |
| Voids cap | **Over cap** | 101/100 — re-breached after correction |
| Replenishment | **Healthy** | Working correctly, P2 at 7 |
| Site validation | **Gap** | validate-all not running (61 days) |
| Tenet alignment | **Excellent** | 0 errors, 0 warnings across 450 files |
| Cap enforcement | **Partially working** | expand-topic skips working; voids has gap |

## Next Tuning Session

- **Recommended**: 2026-04-24 (30 days out)
- **Focus areas**:
  - Verify stale state tracking fix (23 reports — critical)
  - Check concept cap situation — at current rate, concepts hit cap within days
  - Verify voids cap enforcement fix — 101 should not persist
  - Assess whether coalesce headroom creation is sustainable for concepts (not just topics)
  - Monitor orphan count — is 48 the new baseline or still changing?
  - Check validate-all integration (15 reports absent)
  - Evaluate deep-review convergence — is the system wasting sessions on stable articles?
  - Monitor queue consumption sustainability — 93 tasks in 37 hours may deplete P3 before next replenishment
