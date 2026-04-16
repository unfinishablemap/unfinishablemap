---
ai_contribution: 100
ai_generated_date: 2026-04-16
ai_modified: 2026-04-16 09:21:00+00:00
ai_system: claude-opus-4-6
author: null
concepts: []
created: 2026-04-16
date: &id001 2026-04-16
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[todo]]'
- '[[changelog]]'
title: System Tuning Report - 2026-04-16
topics: []
---

# System Tuning Report

**Date**: 2026-04-16
**Sessions analyzed**: 144 (sessions 5699 to 5843)
**Period covered**: 2026-04-12 20:25 to 2026-04-16 09:21 UTC (~3.9 days)

## Executive Summary

The system maintains its perfect hard-failure record (0% for the 13th consecutive period). Expand-topic achieved 0% skip rate (down from 18.2%), its best performance yet. However, two section caps are now breached: topics at 231/230 (+1) and voids at 102/100 (+2). Coalesce abandon rate surged to 58.3% (up from 33.3%) as merge candidates continue to thin. Deep-review marginal-value rate improved to 23.9% (down from 32.1%), partly because orphan-integration work produced value even in zero-word-change reviews. A persistent false-positive pattern in gap analysis continues generating tasks for articles in `arguments/` that it can't find because it only searches `concepts/`. State tracking remains broken (30th consecutive report). No Tier 1 changes warranted.

## Metrics Overview

| Metric | Current (Actual) | Recorded State | Previous (Apr 12) | Trend |
|--------|-------------------|----------------|-------------------|-------|
| Session count | 5843 | 5843 | 5699 | +144 |
| Topics | 231 | 35 | 227 | **+4 (OVER CAP: 231/230)** |
| Concepts | 228 | 145 | 222 | **+6** |
| Arguments | 6 | 4 | 6 | → |
| Voids | 102 | 11 | 99 | **+3 (OVER CAP: 102/100)** |
| Apex articles | 22 | 4 | 22 | → |
| Research notes | 346 | 117 | 344 | +2 |
| Archive files | 387 | -- | 380 | +7 (coalesce active) |
| Reviews completed | 3184 | 542 | 3094 | +90 |
| Recent task success rate | 100% (0 hard failures) | -- | 100% | → |
| Skip/abandon rate | 9.1% (13/143) | -- | 5.9% | ↑ (coalesce-driven) |
| Critical issues | 0 | 0 | 0 | → |
| Medium issues | 10 | 10 | 10 | → |
| Orphaned files | 13 | 13 | 13 | → |
| Queue depth (P0-P1) | 0 | -- | 0 | → |
| Queue depth (P2) | 3 | -- | 3 | → |
| Queue depth (P3) | ~18 active | -- | 331 | Significant reduction |

**State discrepancy update**: Recorded state shows 35 topics (actual: 231, 6.6x), 145 concepts (actual: 228, 1.6x), 11 voids (actual: 102, 9.3x), 542 reviews (actual: 3184, 5.9x). **30th consecutive report.**

## Abort Conditions Check

**Status**: All clear.

- Task failure rate: 0% (0/20 recent tasks failed) — well under 50% threshold
- Convergence: No regression in quality
- Critical issues: 0
- File reads: All successful

## Findings

### Cadence Analysis

**Data points**: ~3.9 days, 144 sessions

| Task | last_runs Timestamp | Actual Last Run (Changelog) | Status |
|------|---------------------|----------------------------|--------|
| validate-all | 2026-01-24 | **Not run since Jan 24** | **83 days stale** |
| pessimistic-review | 2026-04-16 | 2026-04-16 (x1) | Current |
| optimistic-review | 2026-04-16 | 2026-04-16 (x2) | Current |
| check-tenets | 2026-04-12 | 2026-04-16 (x1) | Current |
| check-links | 2026-04-15 | 2026-04-15 | Current |
| deep-review | 2026-04-16 | 2026-04-16 (x76) | Current |
| tune-system | 2026-04-12 | 2026-04-16 (this run) | Current |
| research-voids | 2026-04-15 | 2026-04-16 (x1 skipped) | Current (but skipped — at capacity) |
| coalesce | 2026-04-16 | 2026-04-16 (x12) | Current |
| apex-evolve | 2026-04-15 | 2026-04-16 (x1) | Current |
| agentic-social | 2026-04-16 | 2026-04-16 | Current |

**`validate-all`**: Still absent from automation. Has not run in 83 days. **22nd consecutive report.**

**`research-voids` blocked**: Skipped on Apr 16 because voids is now at 102/100 (over cap). This is correct cap enforcement, but voids research is effectively paused until coalesce or archive operations free slots.

### Failure Pattern Analysis

**Data points**: 143 changelog entries since last tune, 20 recent_tasks in state (all success)

| Task Type | Executed | Skipped/Abandoned | Skip Rate |
|-----------|----------|-------------------|-----------|
| deep-review | 71 | 5 (3 archived, 1 already-reviewed, 1 skipped) | 6.6% |
| refine-draft | 15 | 3 (2 false positive, 1 invalid) | 16.7% |
| coalesce | 5 | 7 (no candidates) | **58.3%** |
| expand-topic | 17 | 0 | **0%** |
| pessimistic-review | 6 | 0 | 0% |
| optimistic-review | 6 | 0 | 0% |
| research-voids | 2 | 1 (at capacity) | 33.3% |
| condense | 2 | 0 | 0% |
| apex-evolve | 2 | 0 | 0% |
| check-tenets | 1 | 0 | 0% |
| **Total** | **127** | **16** | **11.2%** |

**Hard-failure reliability continues**: 13th consecutive tune period with 0% failure rate.

**Overall skip rate increased**: 11.2% (up from 5.9%), driven primarily by coalesce abandon rate.

**Coalesce abandon rate surged**: 58.3% (7/12) — up sharply from 33.3%. This confirms the previous report's observation: merge candidates are thinning rapidly. 5 of 7 abandoned coalesces explicitly noted "well-differentiated" articles after searching 5+ candidate clusters. The coalesce function is approaching natural exhaustion for the current content corpus.

**Expand-topic perfect run**: 0% skip rate (17/17 successful) — the best performance ever, down from 18.2% last period and 50% two periods ago. Replenishment quality has clearly improved.

**Refine-draft false positives persist**: 3 of 18 refine-draft tasks were false positives or invalid (16.7%). Two distinct patterns:
1. **Gap analysis/arguments confusion** (3rd+ occurrence each): Tasks generated to "fix broken wikilinks" to `[many-worlds-argument](/arguments/many-worlds-argument/)` and `[epiphenomenalism-argument](/arguments/epiphenomenalism-argument/)` — articles that exist in `arguments/` but gap analysis only searches `concepts/`. The `[epistemological-limits-of-occams-razor](/arguments/epistemological-limits-of-occams-razor/)` false positive is on its 5th investigation.
2. **Root cause**: The gap analysis in replenishment doesn't search all content sections.

**Deep-review archived-article skips**: 3 skips targeting archived articles (down from 5 last period). Some improvement but the filter is still not in place.

**Deep-review marginal-value analysis**:

Zero-word-change deep-reviews: 13/71 effective = 18.3%

However, this metric needs refinement. Of the 13 zero-word-change reviews:
- **8 performed useful orphan integration** — added cross-links from other articles to the target, resolving orphan status. These produced real value despite zero target word changes.
- **5 were truly zero-value** — articles confirmed stable after 3-8+ prior reviews with no cross-linking work.

Near-zero change (±10 words, minimal): 4 additional reviews.

| Metric | This Period | Previous | Trend |
|--------|------------|----------|-------|
| Raw zero-word-change rate | 18.3% (13/71) | 32.1% (25/78) | ↓ **Improved** |
| True zero-value rate | 7.0% (5/71) | ~32.1% | ↓ **Significantly improved** |
| Near-zero rate | 23.9% (17/71) | 32.1% | ↓ **Improved** |

The improvement is partly due to deep-reviews being more frequently assigned orphan integration work, which produces value even on stable articles. Articles with 4+ prior reviews and zero changes that still get re-reviewed remain the primary waste.

### Queue Health Analysis

**Data points**: Current todo.md state

**Queue composition**:
- P0: 0 (unchanged)
- P1: 0 (unchanged)
- P2: 3 (unchanged; 2 condense, 1 expand-topic)
- P3: ~15 active tasks visible (significant reduction from 331)
- Resolved/superseded: 2 visible

**Queue appears dramatically smaller**: The visible todo.md shows far fewer active tasks than the 334 reported previously. This may reflect either bulk cleanup or tasks being consumed faster than generated. The 143 tasks executed this period significantly exceeded the previous queue depth growth.

**Task type distribution in queue**:
- deep-review: 8 (staleness-driven)
- refine-draft: 3 (pessimistic review chains)
- expand-topic: 2 (1 P2, 1 P3)
- condense: 2 (P2, length violations)
- cross-review: 1 (chain from expand-topic)

**Gap analysis false positives**: The queue still contains an epistemological-limits-occams-razor false positive deep-review. The gap analysis module needs to search all content sections (topics, concepts, arguments, voids) rather than just concepts.

### Review Finding Patterns

**Data points**: 6 pessimistic reviews, 6 optimistic reviews, 1 tenet check, 76 deep reviews since last tune

**Recurring themes across pessimistic reviews (Apr 13-16)**:

| Theme | Articles | Status |
|-------|----------|--------|
| Concession-convergence overreach | functionalism.md | Task created (P3 refine-draft) |
| Question-begging phenomenological appeals | phenomenology.md | Task created (P3 refine-draft) |
| Length violations | functionalism.md (3640w), phenomenology.md (3604w) | Tasks created (P2 condense) |
| Conceivability-vitalism gap | conceivability-possibility-inference.md | **Addressed** (refine-draft Apr 13) |
| Born rule dilemma | materialism.md | Persistent (carried forward) |
| Selective citation of evidence | multiple | Persistent |

**Assessment**: Pessimistic → refine-draft pipeline continues to function well. Tasks are being generated and executed within hours to days.

**Tenet check (Apr 16)**: 0 errors, 2 warnings, 6 notes across 457 files. Tenet alignment remains excellent.

**Deep-review convergence signals**: Articles confirmed fully stable this period: blindsight (5th review), phenomenology-of-the-edge (8th review), purpose-and-alignment (4th review), continual-learning-argument (converged), bergson-and-duration (4th review). These should be excluded from future deep-review targeting.

### Convergence Progress

**Data points**: Actual file counts vs caps

| Category | Actual Count | Cap | % of Cap | Change from Apr 12 | Direction |
|----------|-------------|-----|----------|---------------------|-----------|
| Topics | 231 | 230 | **100.4%** | +4 | **OVER CAP (+1)** |
| Concepts | 228 | 230 | 99.1% | +6 | **2 slots** (reduced from 8) |
| Arguments | 6 | -- | -- | 0 | Stable |
| Voids | 102 | 100 | **102%** | +3 | **OVER CAP (+2)** |
| Apex | 22 | -- | -- | 0 | Stable |
| Research | 346 | -- | -- | +2 | Growing |
| Archive | 387 | -- | -- | +7 | Growing (coalesce active) |
| Reviews | 3184 | -- | -- | +90 | Growing |

**Two section caps now breached**:
- **Topics**: 231/230 — exceeded by 1. The previous report warned this would happen (3 slots remaining, ~9 expand-topics per period). Despite the warning, topics continued expanding.
- **Voids**: 102/100 — exceeded by 2. Was 99 last period (below cap, resolved), now back over. 2 new voids were created (predictive-construction-void, interested-party-void) pushing it back over.

**Concepts approaching cap**: 228/230 — only 2 slots remaining (was 8 last period). At the rate of +6 per period, concepts will breach cap next period.

**Cap enforcement gaps**: The expand-topic skill is supposed to refuse placement in full sections, but topics reached 231 despite a 230 cap. Either the cap check uses stale counts (the state shows 35 topics) or the check is not running.

**Quality metrics**:
- Critical issues: 0 (target: 0) — met
- Medium issues: 10 (target: <=3) — exceeded, persistent (unchanged 21+ periods)
- Low issues: 3 — acceptable
- Orphaned files: 13 — unchanged (8+ periods)

## Changes Applied (Tier 1)

*No changes applied.*

**Rationale**: The `tune_system_history` and `locked_settings` sections required for Tier 1 change tracking still do not exist. No adjustable cadence, threshold, or weight parameters are present in evolution-state.yaml to modify. **30th report** noting this structural limitation.

## Recommendations (Tier 2)

### 1. Fix Stale content_stats and progress Counters (Carried Forward x25 — CRITICAL)

- **Proposed change**: Add file-counting logic to refresh `content_stats` and `progress` in `tools/evolution/state.py`, called at session start.
- **Rationale**: Recorded state shows 35 topics (actual: 231), 145 concepts (actual: 228), 11 voids (actual: 102), 542 reviews (actual: 3184). **25th consecutive report.** The stale counts are now causing functional harm — section cap enforcement appears to be checking these stale values rather than actual file counts, allowing topics and voids to exceed their caps.
- **Risk**: Low
- **Priority**: **Critical** — now causing cap enforcement failures

### 2. Add tune_system_history and locked_settings Sections (Carried Forward x27)

- **Proposed change**: Add both sections to evolution-state.yaml per skill specification.
- **Rationale**: Required for cooldown enforcement and locked settings checks. **27th report.** Without these, tune-system cannot make any Tier 1 changes.
- **Risk**: Low
- **Priority**: High

### 3. Add validate-all to Cycle Triggers (Carried Forward x22)

- **Proposed change**: Add `"validate-all": 2` to `CYCLE_TRIGGERS` in `tools/evolution/cycle.py`.
- **Rationale**: Has not run in 83 days. Described as "Daily health check" in CLAUDE.md but absent from automation cycle. **22nd report.**
- **Risk**: Low (read-only check)
- **Priority**: Medium

### 4. Fix Section Cap Enforcement Using Actual File Counts (NEW — URGENT)

- **Proposed change**: Update `expand-topic` and `replenishment` cap checks to count actual files on disk rather than reading from `evolution-state.yaml` progress counters.
- **Rationale**: Topics reached 231/230 and voids reached 102/100 despite caps of 230 and 100. The stale state (showing 35 topics and 11 voids) means cap enforcement never triggers. This is the first functional failure directly caused by the stale counters.
- **Risk**: Low
- **Priority**: **Urgent** — sections are already over cap

### 5. Fix Gap Analysis to Search All Content Sections (NEW)

- **Proposed change**: Update gap analysis in replenishment to search `arguments/`, `apex/`, and `voids/` sections in addition to `topics/` and `concepts/`.
- **Rationale**: Three distinct false-positive patterns keep recurring because gap analysis only searches `concepts/`:
  - `[many-worlds-argument](/arguments/many-worlds-argument/)` — exists in `arguments/`, investigated 3 times
  - `[epiphenomenalism-argument](/arguments/epiphenomenalism-argument/)` — exists in `arguments/`, investigated multiple times
  - `[epistemological-limits-of-occams-razor](/arguments/epistemological-limits-of-occams-razor/)` — exists in `arguments/`, investigated 5 times
  Each investigation wastes a cycle slot on a refine-draft that concludes "false positive."
- **Risk**: Low
- **Priority**: Medium — recurring waste

### 6. Implement Deep-Review Convergence Tracking (Carried Forward x16 — IMPROVING BUT STILL NEEDED)

- **Proposed change**: Track per-article review count and last word-change delta; skip further deep-review for articles reviewed 3+ times with zero or near-zero changes.
- **Rationale**: Although the raw zero-word-change rate improved to 18.3% (from 32.1%), this was partly driven by orphan-integration work masking the metric. 5 articles were reviewed despite being confirmed stable after 4-8 prior reviews. Articles like phenomenology-of-the-edge (8th review, 0 changes) are clearly wasting slots.
- **Risk**: Low
- **Priority**: High — orphan integration provides a partial workaround but doesn't address the fundamental issue

### 7. Reduce Coalesce Cycle Frequency (NEW)

- **Proposed change**: Reduce coalesce from 2 of 24 cycle slots (8.3%) to 1 of 24 (4.2%), or shift to cycle-trigger at lower frequency.
- **Rationale**: Coalesce abandon rate surged to 58.3% (7/12) — up from 33.3% last period and 22.2% the period before. More than half of coalesce attempts now find no viable candidates. Each abandoned attempt searches 5+ candidate clusters and consumes a full cycle slot. The trend is structural: prior coalesce passes have consolidated most redundant content.
- **Risk**: Low — successful coalesces still occur (5 this period) but at diminishing rate
- **Priority**: Medium

### 8. Purge Unexecutable expand-topic Tasks from Queue (Carried Forward x5)

- **Proposed change**: Remove expand-topic tasks targeting sections at or near cap.
- **Rationale**: With topics over cap (231/230), concepts nearly full (228/230), and voids over cap (102/100), most remaining expand-topic tasks in the queue are unexecutable. Queue appears much smaller this period but any remaining expand-topic tasks for full sections are dead weight.
- **Risk**: Low
- **Priority**: Medium

### 9. Update Convergence Targets (Carried Forward x29)

- **Proposed change**: Update `convergence_targets` in evolution-state.yaml: min_topics 10→200, min_concepts 15→200, min_arguments 5→10, add min_voids 80, add min_apex 15.
- **Rationale**: Targets set for early-stage system. All vastly exceeded. **29th report.**
- **Risk**: Low

### 10. Suppress Queue Replenishment at Depth Threshold (Carried Forward x7)

- **Proposed change**: Add a maximum queue depth threshold that suppresses replenishment.
- **Rationale**: Queue appears to have been cleaned up significantly this period, but without a hard cap, it could re-accumulate.
- **Risk**: Low
- **Priority**: Low — less urgent given apparent queue reduction

## Items for Human Review (Tier 3)

### 1. Stale State Tracking — 30th Consecutive Report

- **Issue observed**: `content_stats` and `progress` contain stale data. `tune_system_history` and `locked_settings` sections still don't exist.
- **Why human needed**: Code changes to `tools/evolution/state.py`
- **Suggested action**: Fix `content_stats`/`progress` refresh (25 reports). Add `tune_system_history` and `locked_settings` sections (27 reports). **30 reports over ~100 days.** Now causing functional harm (cap enforcement failures).

### 2. Section Cap Breaches — Topics 231/230, Voids 102/100

- **Issue observed**: Two sections now exceed their configured caps. Cap enforcement is ineffective because it reads stale progress counters instead of counting actual files.
- **Why human needed**: Policy decision: (a) raise caps, (b) fix counter refresh, or (c) both. Also need to decide whether to coalesce/archive content to get back under caps or simply raise them.
- **Suggested action**: Fix stale counters (Tier 2 #1 and #4), then decide whether current caps are still appropriate given the site's maturity.

### 3. Coalesce Approaching Exhaustion — 58.3% Abandon Rate

- **Issue observed**: More than half of coalesce attempts now fail to find viable candidates. This is structural — the site's remaining content is well-differentiated.
- **Why human needed**: Deciding whether to (a) reduce coalesce frequency, (b) change coalesce strategy (e.g., target different section types), or (c) accept that coalesce's primary utility phase has passed.
- **Suggested action**: Reduce coalesce cycle allocation and monitor whether the abandon rate continues rising.

### 4. Medium Issues Persistent at 10 (Carried Forward x21)

- **Issue observed**: Medium issues count has been exactly 10 for 21+ tune periods. Target is <=3.
- **Why human needed**: Deciding whether to raise target or address specific issues
- **Suggested action**: Raise `max_medium_issues` to 15

### 5. Orphaned Files Persistent at 13 (Carried Forward x8)

- **Issue observed**: Orphaned files remain at exactly 13 despite extensive orphan-integration work during deep-reviews this period (8 deep-reviews focused on orphan integration, adding 50+ inbound cross-links).
- **Why human needed**: The orphan count appears to be a stale metric — the same 13 number has persisted despite significant cross-linking work.
- **Suggested action**: Investigate whether orphan detection is re-counting or using stale data (likely related to the general state staleness issue).

## System Health Summary

| Component | Status | Notes |
|-----------|--------|-------|
| Task execution | **Excellent** | 0% hard failure rate (13th consecutive period) |
| Skip rate | Acceptable | 11.2% (up from 5.9%, coalesce-driven) |
| Content quality | Good | 0 critical, 0 tenet issues |
| Queue management | **Improved** | Queue significantly smaller |
| Expand-topic efficiency | **Excellent** | 0% skip rate (best ever, down from 18.2%) |
| Coalesce efficiency | **Poor** | 58.3% abandon rate (up from 33.3%) — structural |
| Review system | Effective | 3184+ reviews total, +90 this period |
| Deep-review convergence | **Improved** | 18.3% zero-change rate (down from 32.1%) |
| Scheduling | Operational | Cycle mechanism working correctly |
| State tracking | **Broken** | content_stats/progress stale (30th report) |
| Topics cap | **BREACHED** | 231/230 (100.4%) — over cap by 1 |
| Concepts cap | **Critical** | 228/230 (99.1%) — 2 slots remaining |
| Voids cap | **BREACHED** | 102/100 (102%) — over cap by 2 |
| Site validation | **Gap** | validate-all not running (83 days) |
| Tenet alignment | **Excellent** | 0 errors, 2 warnings across 457 files |
| Cap enforcement | **Broken** | Stale counters prevent enforcement |

## Next Tuning Session

- **Recommended**: 2026-05-16 (30 days out)
- **Focus areas**:
  - Verify stale state tracking fix (30 reports — critical, now causing harm)
  - Check whether section cap breaches are resolved (topics 231/230, voids 102/100)
  - Monitor concepts cap (228/230 — likely to breach next)
  - Monitor coalesce abandon rate (58.3% and rising — may need frequency reduction)
  - Verify validate-all integration (22 reports absent)
  - Check gap analysis false-positive fix (arguments/ section)
  - Track deep-review convergence with orphan-integration distinction