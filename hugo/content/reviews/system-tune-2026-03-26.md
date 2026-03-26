---
ai_contribution: 100
ai_generated_date: 2026-03-26
ai_modified: 2026-03-26 17:22:00+00:00
ai_system: claude-opus-4-6
author: null
concepts: []
created: 2026-03-26
date: &id001 2026-03-26
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[todo]]'
- '[[changelog]]'
title: System Tuning Report - 2026-03-26
topics: []
---

# System Tuning Report

**Date**: 2026-03-26
**Sessions analyzed**: 144 (sessions 4835 to 4979)
**Period covered**: 2026-03-25 00:02 to 2026-03-26 17:22 UTC (~41 hours)

## Executive Summary

The system maintains perfect hard-failure reliability (0%) for the seventh consecutive period, but the skip/abandon rate has nearly doubled from 6.6% to ~12% (19/163). The primary driver is duplicate/already-exists skips in expand-topic, suggesting queue replenishment is generating tasks for articles that already exist or were recently coalesced. The P3 queue exploded from 80 to 214 through aggressive replenishment — far exceeding consumption rate. Topics dropped to 226 (-1, coalesce creating headroom), concepts stable at 226/230 (4 slots), voids persist at 101/100 (over cap for second consecutive period). State tracking remains broken (24th consecutive report). No Tier 1 changes warranted.

## Metrics Overview

| Metric | Current (Actual) | Recorded State | Previous (Mar 25) | Trend |
|--------|-------------------|----------------|-------------------|-------|
| Session count | 4979 | 4979 | 4835 | +144 |
| Topics | 226 | 35 | 227 | -1 (coalesce headroom) |
| Concepts | 226 | 145 | 226 | → (pressure stable) |
| Arguments | 6 | 4 | 6 | → |
| Voids | 101 | 11 | 101 | → (**still over cap**) |
| Apex articles | 21 | 4 | 21 | → |
| Research notes | 316 | 117 | 314 | +2 |
| Archive files | 316 | -- | 300 | +16 (coalesce active) |
| Reviews completed | 2662 | 542 | 2568 | +94 |
| Recent task success rate | 100% (0 hard failures) | -- | 100% | → |
| Skip/abandon rate | ~12% (19/163) | -- | 6.6% | ↑ (**doubled**) |
| Critical issues | 0 | 0 | 0 | → |
| Medium issues | 10 | 10 | 10 | → |
| Orphaned files | 13 | 13 | 48 | ↓ (**reset or fixed**) |
| Queue depth (P0-P1) | 0 | 0 | 0 | → |
| Queue depth (P2) | 2 | 2 | 7 | -5 (consumed) |
| Queue depth (P3) | 214 | 214 | 80 | +134 (**massive replenishment**) |

**State discrepancy update**: Recorded state shows 35 topics (actual: 226, 6.5x), 145 concepts (actual: 226, 1.6x), 11 voids (actual: 101, 9.2x), 542 reviews (actual: 2662, 4.9x). **24th consecutive report.**

## Abort Conditions Check

**Status**: All clear.

- Task failure rate: 0% (0/20 recent tasks failed) — well under 50% threshold
- Convergence: No regression — topics consolidated, concepts stable
- Critical issues: 0
- File reads: All successful

## Findings

### Cadence Analysis

**Data points**: ~41 hours, 144 sessions

| Task | last_runs Timestamp | Actual Last Run (Changelog) | Status |
|------|---------------------|----------------------------|--------|
| validate-all | 2026-01-24 | **Not run since Jan 24** | **62 days stale** |
| pessimistic-review | 2026-01-25 | 2026-03-26 (x6) | Timestamp stale |
| optimistic-review | 2026-01-25 | 2026-03-26 (x7) | Timestamp stale |
| check-tenets | 2026-03-25 | 2026-03-26 | Current |
| check-links | 2026-03-26 | 2026-03-26 | Current |
| deep-review | 2026-01-25 | 2026-03-26 (many) | Timestamp stale |
| tune-system | 2026-03-25 | 2026-03-26 (this run) | Current |
| research-voids | 2026-03-26 | 2026-03-26 (skipped — at capacity) | Current |
| coalesce | 2026-01-25 | 2026-03-26 (x14) | Timestamp stale |
| apex-evolve | 2026-03-25 | 2026-03-26 | Current |
| agentic-social | 2026-03-26 | 2026-03-26 | Current |

**Root cause unchanged**: Queue tasks do not update `state.last_runs`. Cycle-triggered tasks correctly update timestamps. **24th consecutive report.**

**validate-all**: Still absent from both the task cycle and CYCLE_TRIGGERS. Has not run in 62 days. **16th report.**

### Failure Pattern Analysis

**Data points**: 163 changelog entries since last tune, 20 recent_tasks in state (all success)

| Task Type | Executed | Failed | Skipped/Abandoned | Rate |
|-----------|----------|--------|-------------------|------|
| deep-review | 76 | 0 | 0 | 0% |
| expand-topic | 17 | 0 | 2 (duplicate/redirect) | 0% |
| refine-draft | 16 | 0 | 3 (no-op/invalid) | 0% |
| coalesce | 14 | 0 | 3 (no candidates) | 0% |
| optimistic-review | 7 | 0 | 0 | 0% |
| pessimistic-review | 6 | 0 | 0 | 0% |
| deep-review (cross) | 6 | 0 | 0 | 0% |
| condense | 3 | 0 | 0 | 0% |
| deep-review (orphan) | 3 | 0 | 0 | 0% |
| check-tenets | 3 | 0 | 0 | 0% |
| research-voids | 3 | 0 | 1 (at capacity) | 0% |
| research-topic | 2 | 0 | 0 | 0% |
| apex-evolve | 2 | 0 | 0 | 0% |
| tune-system | 1 | 0 | 0 | 0% |
| **Total** | **~163** | **0** | **~19** | **0%** |

**Perfect hard-failure reliability continues**: Seventh consecutive tune period with 0% failure rate.

**Skip/abandon rate doubled**: 19/163 (12%) vs 10/151 (6.6%) last period. Primary drivers:
- **Expand-topic duplicates**: Tasks generated for articles that already exist or were recently coalesced. This wastes a cycle slot.
- **Coalesce no-candidates**: 3 abandoned coalesce attempts (21% of coalesce runs). After 316 archive files and heavy consolidation, genuine merge candidates are becoming scarce.
- **Refine-draft no-ops**: 3 tasks based on outdated or incorrect information — likely stale queue items targeting already-fixed issues.

**Positive pattern**: Deep-review (including cross-review and orphan integration) totals 85 of 163 entries (52%), consistent with last period (51%). The task is heavily represented but not growing as a percentage.

### Queue Health Analysis

**Data points**: Current todo.md state, comparison with Mar 25

**Queue composition**:
- P0: 0 (unchanged)
- P1: 0 (unchanged)
- P2: 2 (down from 7 — 5 consumed)
- P3: 214 (up from 80 — massive net growth despite ~90+ consumed)
- Total actionable (P0-P2): 2 (low — may trigger replenishment again soon)

**P3 explosion**: From 80 to 214, a net growth of +134 despite consuming ~93 tasks. The replenishment system is generating tasks much faster than the loop can consume them. At current consumption rate (~2.5 tasks/hour), the 214 P3 queue would sustain ~86 hours before depletion — roughly 3.5 days.

**Task type distribution in queue**: Heavy on expand-topic (5+ pending), refine-draft (10+ from reviews), deep-review (10+ staleness-driven). The queue is well-diversified.

**P2 depletion concern**: Only 2 P0-P2 tasks remain. Since the loop prioritises P0-P2 over P3, this means nearly all upcoming queue slots will pull from the large P3 pool. The P3→P2 promotion rate appears slow — most tasks stay at P3 unless human intervention promotes them.

### Review Finding Patterns

**Data points**: 6 pessimistic reviews (Mar 25-26), 7 optimistic reviews, 3 tenet checks, 85 deep reviews since last tune

**Recurring themes across pessimistic reviews** (Mar 25-26):

| Theme | Appearances This Period | Cumulative Status |
|-------|------------------------|-------------------|
| Quantum tenet unfalsifiability | Mar 26 (downward-causation, filter-theory), Mar 25 (consciousness-physics) | Persistent (25+ reports) |
| Conceivability-possibility gap | Mar 25b | Persistent |
| Unverifiable empirical claims / citation gaps | Mar 26 (meditation efficacy), 26pm (Schwartz OCD), Mar 25 (Pati preprint) | Persistent |
| Buddhist no-self vs Map's indexical identity | Mar 26 (simulation), 26pm (attention) | Persistent |
| Selection trilemma incompleteness | Mar 26pm (attention interface) — NEW | Emerging |
| AST dismissal grounds apply reflexively | Mar 26pm (attention interface) — NEW | Emerging |

**Two new critique patterns**:
1. **Selection trilemma**: The deterministic/random/conscious trichotomy omits compatibilist and emergentist alternatives. Flagged in attention-and-the-consciousness-interface review.
2. **Reflexive critique**: The grounds used to dismiss AST (models don't experience) apply equally to the Map's own interface framework. A legitimate structural concern.

**Tenet check** (Mar 26): 0 errors, 0 warnings, 28 notes across 452 files. Notes are broken wikilink anchors, not philosophical conflicts. Tenet alignment remains excellent.

**Deep-review convergence signals**: Multiple articles showed 0 word count change this period (consciousness-and-the-problem-of-other-properties: 3rd review with no changes, consciousness-and-social-understanding: stable after 3rd review, authentic-vs-inauthentic-choice: converged). The system lacks a mechanism to stop re-reviewing converged articles.

### Convergence Progress

**Data points**: Actual file counts vs caps

| Category | Actual Count | Cap | % of Cap | Change from Mar 25 | Direction |
|----------|-------------|-----|----------|---------------------|-----------|
| Topics | 226 | 230 | **98.3%** | -1 | **4 slots (headroom gained)** |
| Concepts | 226 | 230 | **98.3%** | 0 | **4 slots (stable)** |
| Arguments | 6 | -- | -- | 0 | Stable |
| Voids | 101 | 100 | **101%** | 0 | **Still over cap** |
| Apex | 21 | -- | -- | 0 | Stable |
| Research | 316 | -- | -- | +2 | Growing |
| Archive | 316 | -- | -- | +16 | Growing (coalesce active) |
| Reviews | 2662 | -- | -- | +94 | Growing |

**Quality metrics**:
- Critical issues: 0 (target: 0) — met
- Medium issues: 10 (target: <=3) — exceeded, persistent (unchanged 15+ periods)
- Low issues: 3 — acceptable
- Orphaned files: 13 (state shows 13, previously 48 — either reset or deep-review orphan integration resolved 35 files)

**Coalesce sustaining headroom**: Topics gained another slot (227→226), keeping 4 available. With 16 new archive files, coalesce remains the primary headroom creation mechanism. However, coalesce abandon rate rose to 21% — viable merges are becoming scarcer.

**Concepts stable**: The concern from last report (concepts tightening) has not materialised — concepts held at 226/230 for a full tune period. Coalesce may be balancing expansion.

**Voids still over cap**: 101/100 persists for the second consecutive period. No new voids were created (research-voids correctly skipped), but no voids were archived or coalesced to reduce the count below 100.

**Orphan count resolution**: Dropped from 48 to 13. If genuine, this represents excellent work by the deep-review orphan integration tasks (3 ran this period, each integrating 5-11 articles). However, the counter may simply be unreliable.

## Changes Applied (Tier 1)

*No changes applied.*

**Rationale**: The evolution-state.yaml still contains no adjustable cadence, threshold, or weight parameters that meet the evidence threshold and magnitude limits for automatic change. The `tune_system_history` and `locked_settings` sections required for Tier 1 change tracking still do not exist. **24th report** noting this structural limitation.

## Recommendations (Tier 2)

### 1. Fix Stale last_runs Timestamps (Carried Forward x24 — CRITICAL)

- **Proposed change**: In `scripts/evolve_loop.py`, add `state.last_runs` update after queue task execution.
- **Rationale**: **24th consecutive report.** Queue tasks (deep-review, pessimistic-review, optimistic-review, coalesce) show timestamps from January while actually running daily.
- **Risk**: Low
- **Priority**: **Critical**

### 2. Fix Stale content_stats and progress Counters (Carried Forward x19)

- **Proposed change**: Add file-counting logic to refresh `content_stats` and `progress` in `tools/evolution/state.py`, called at session start.
- **Rationale**: Recorded state shows 35 topics (actual: 226), 145 concepts (actual: 226), 11 voids (actual: 101), 542 reviews (actual: 2662). 19th consecutive report.
- **Risk**: Low
- **Priority**: High

### 3. Add tune_system_history and locked_settings Sections (Carried Forward x21)

- **Proposed change**: Add both sections to evolution-state.yaml per skill specification.
- **Rationale**: Required for cooldown enforcement and locked settings checks. 21st report.
- **Risk**: Low

### 4. Add validate-all to Cycle Triggers (Carried Forward x16)

- **Proposed change**: Add `"validate-all": 2` to `CYCLE_TRIGGERS` in `tools/evolution/cycle.py`.
- **Rationale**: Has not run in 62 days. Described as "Daily health check" in CLAUDE.md but absent from automation cycle. 16th report.
- **Risk**: Low (read-only check)
- **Priority**: Medium

### 5. Filter Queue Tasks Against Existing Content (NEW — HIGH PRIORITY)

- **Proposed change**: In replenishment logic, check whether the target article already exists before generating expand-topic tasks. Also check whether the target file has been archived (coalesced into another).
- **Rationale**: Skip/abandon rate doubled from 6.6% to 12%, primarily driven by expand-topic duplicates and refine-draft no-ops. With 316 archive files, stale task generation targeting already-coalesced content is increasingly wasteful. Each skipped task wastes a cycle slot.
- **Risk**: Low
- **Priority**: **High** — directly impacts execution efficiency

### 6. Address Voids Cap Persistence at 101 (Carried Forward x2)

- **Proposed change**: Either archive or coalesce one void to bring count to 100, or raise cap to 105.
- **Rationale**: Voids have been at 101 for two consecutive tune periods. No mechanism is actively reducing the count — research-voids correctly skips, but nothing removes the excess.
- **Risk**: Low
- **Priority**: Medium — cap violation is stable but persistent

### 7. Implement Deep-Review Convergence Tracking (Carried Forward x10)

- **Proposed change**: Track per-article review count; skip further deep-review for articles reviewed 3+ times with minimal changes.
- **Rationale**: Deep-review is 52% of all tasks. Multiple articles this period showed 0 word count change on 3rd review (problem-of-other-properties, social-understanding, authentic-choice). Each unnecessary review wastes a cycle slot.
- **Risk**: Low
- **Priority**: Medium-High — the problem is growing as more articles converge

### 8. Monitor Queue Over-Replenishment (NEW)

- **Proposed change**: Add a maximum queue depth threshold (e.g., 200 P3 tasks) that suppresses replenishment.
- **Rationale**: P3 grew from 80 to 214 (+134 net) in one tune period despite consuming ~93 tasks. At this rate, the queue will grow indefinitely. Very large queues may contain increasingly marginal tasks. A soft cap would prevent queue bloat.
- **Risk**: Low
- **Priority**: Medium

### 9. Address Triple Cap Pressure (Carried Forward x4 — STABILISING)

- **Proposed change**: Consider raising caps, or accept current state as natural quality throttle.
- **Rationale**: Topics: 4 slots (improved), Concepts: 4 slots (stable — concern from last report did not materialise), Voids: over cap (persistent). Coalesce is sustaining headroom for topics and concepts. However, coalesce abandon rate is rising (21% this period) — viable merges may be exhausted within 2-3 more periods.
- **Risk**: Low
- **Priority**: Medium — less urgent than last report, but monitor coalesce viability

### 10. Update Convergence Targets (Carried Forward x23)

- **Proposed change**: Update `convergence_targets` in evolution-state.yaml: min_topics 10→200, min_concepts 15→200, min_arguments 5→10, add min_voids 80, add min_apex 15.
- **Rationale**: Targets set for early-stage system. All vastly exceeded. 23rd report.
- **Risk**: Low

### 11. Systematic Citation Audit (Carried Forward x16)

- **Proposed change**: Add P2 task to audit articles flagged for unverifiable empirical claims.
- **Rationale**: This period: Schwartz OCD over-interpretation, Pati preprint weight, meditation efficacy citation gap. Citation quality remains the most actionable pessimistic review category.
- **Risk**: Low

### 12. Filter Archived Articles from Task Generation (Carried Forward x5)

- **Proposed change**: In replenishment logic, skip archived articles when generating tasks.
- **Rationale**: 316 archive files. 2 expand-topic skips this period were due to duplicates/redirects targeting archived content. Merged with Recommendation 5 above.
- **Risk**: Low

## Items for Human Review (Tier 3)

### 1. Stale State Tracking — 24th Consecutive Report

- **Issue observed**: `last_runs`, `content_stats`, and `progress` all contain stale data. `tune_system_history` and `locked_settings` sections still don't exist.
- **Why human needed**: Code changes to evolve_loop.py and tools/evolution/state.py
- **Suggested action**: Fix the three state-tracking issues together. **24 reports over ~82 days.** This is the single highest-value fix available.

### 2. Medium Issues Persistent at 10 (Carried Forward x15)

- **Issue observed**: Medium issues count has been exactly 10 for 15+ tune periods. Target is <=3.
- **Why human needed**: Deciding whether to raise target or address specific issues
- **Suggested action**: Raise `max_medium_issues` to 15

### 3. Deep-Review Diminishing Returns at Scale (Carried Forward x3)

- **Issue observed**: Deep-review is 52% of all tasks. Articles are converging — 3+ showed 0 word change this period. Without convergence tracking, the system will keep reviewing stable articles.
- **Why human needed**: Whether to implement convergence tracking and an "article stable" flag
- **Suggested action**: After 3 consecutive reviews with <10 words change, mark article as "converged" and skip further reviews unless modified by other tasks.

### 4. Skip Rate Doubling — Structural or Transient?

- **Issue observed**: Skip/abandon rate went from 6.6% to 12%. If structural (queue generating bad tasks), this wastes 12% of compute. If transient (post-heavy-coalesce period), it may self-correct.
- **Why human needed**: Determine whether queue generation logic needs filtering fixes (Tier 2 #5) or whether this is temporary
- **Suggested action**: Monitor next period. If skip rate stays >10%, implement duplicate-checking in replenishment.

## System Health Summary

| Component | Status | Notes |
|-----------|--------|-------|
| Task execution | **Excellent** | 0% hard failure rate (7th consecutive period) |
| Content quality | Good | 0 critical, 0 tenet warnings |
| Queue management | **Mixed** | Queue over-replenished (214 P3), P2 depleted (2) |
| Queue consumption | **Good** | ~94 tasks consumed (~2.3/hour) |
| Review system | Effective | 2662+ reviews total, +94 this period |
| Review-fix pipeline | **Effective** | Citation issues caught, cross-links added |
| Coalesce pipeline | **Maturing** | 21% abandon rate (up from 17%) — viable merges becoming scarce |
| Scheduling | Operational | Cycle mechanism working correctly |
| State tracking | **Broken** | last_runs, content_stats, progress all stale (24th report) |
| Topics cap | **Good** | 226/230 (98.3%) — 4 slots (headroom gained) |
| Concepts cap | **Stable** | 226/230 (98.3%) — 4 slots (unchanged, concern resolved) |
| Voids cap | **Over cap** | 101/100 — persistent for 2 periods |
| Replenishment | **Over-aggressive** | +134 net growth despite consuming ~93 |
| Site validation | **Gap** | validate-all not running (62 days) |
| Tenet alignment | **Excellent** | 0 errors, 0 warnings across 452 files |
| Skip rate | **Warning** | 12% (doubled from 6.6%) |

## Next Tuning Session

- **Recommended**: 2026-04-25 (30 days out)
- **Focus areas**:
  - Verify stale state tracking fix (24 reports — critical)
  - Monitor skip/abandon rate — if >10% again, queue filtering is needed
  - Check coalesce viability — will abandon rate continue rising?
  - Verify voids count — has 101 been resolved?
  - Monitor queue depth — is 214 P3 self-correcting or growing further?
  - Check validate-all integration (16 reports absent)
  - Evaluate deep-review convergence — how many articles are being re-reviewed without changes?
  - Assess whether concepts cap pressure re-emerges