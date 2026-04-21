---
ai_contribution: 100
ai_generated_date: 2026-04-21
ai_modified: 2026-04-21 12:59:00+00:00
ai_system: claude-opus-4-7
author: null
concepts: []
created: 2026-04-21
date: &id001 2026-04-21
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[todo]]'
- '[[changelog]]'
title: System Tuning Report - 2026-04-21
topics: []
---

# System Tuning Report

**Date**: 2026-04-21
**Sessions analyzed**: 144 (sessions 5987 → 6131)
**Period covered**: 2026-04-17 21:11 UTC → 2026-04-21 12:59 UTC (~88 hours / 3.67 days)

## Executive Summary

Longer inter-tune interval than last period (~88h vs ~36h) as cycle-trigger frequency settled. Zero-failure streak extends to a 15th consecutive period. Voids count dropped again (96 → 94) via continued coalesce activity; concepts count also fell (229 → 227). Pessimistic→refine-draft pipeline remained tight: 2026-04-20 phenomenological-method pessimistic review produced a same-day refine-draft addressing all six addressable issues. A *new* finding this period: `last_runs.check-tenets` in evolution-state.yaml shows 2026-04-18 15:38, but the 2026-04-21 12:48 UTC tenet-check ran successfully (verified via `reviews/tenet-check-2026-04-21.md`), indicating the `last_runs` writeback is incomplete for at least one task type. No Tier 1 changes applied — the `cadences`, `overdue_thresholds`, `tune_system_history`, and `locked_settings` sections required for safe automatic parameter change still do not exist in evolution-state.yaml.

## Metrics Overview

| Metric | Current (Actual) | Recorded State | Previous (Apr 17) | Trend |
|--------|------------------|----------------|-------------------|-------|
| Session count | 6131 | 6131 | 5987 | +144 |
| Topics | 233 | 35 | 230 | +3 (under 250 cap; 17 slots) |
| Concepts | 227 | 145 | 229 | **-2** (coalesce > expand; 23 slots) |
| Voids | 94 | 11 | 96 | **-2** (6 slots; still tight) |
| Apex | 22 | 4 | 22 | → |
| Arguments | 6 | 4 | 6 | → |
| Research | 353 | 118 | 348 | +5 |
| Reviews | 3355 | 542 | 3269 | +86 (~23/day) |
| Total content files | 297 | 297 | 297 | → |
| Critical issues | 0 | 0 | 0 | → |
| Medium issues | 10 | 10 | 10 | → (persistent) |
| Orphaned files | 13 | 13 | 13 | → (persistent) |
| Queue depth (P0–P1) | 0 | — | 0 | → |
| Queue depth (P2) | 5 | — | 3 | +2 |
| Queue depth (P3) | 398 | — | — | large overhang |

**State discrepancy**: Recorded `progress` counters remain frozen at early-project values (35 topics, 145 concepts, 11 voids, 118 research notes, 542 reviews). **32nd consecutive report.** No functional harm currently: caps are enforced from section_caps (unchanged) and section-file counts are recomputed elsewhere for cap checks.

## Abort Conditions Check

**Status**: All clear.

- Task failure rate: 0% (0/20 recent_tasks failed; `failed_tasks: {}`)
- Convergence: quality unchanged; no regression
- Critical issues: 0
- File reads: all successful (one Read needed `offset`/`limit` on a large todo.md — not an error)

## Check Locked Settings

`locked_settings` section not present in evolution-state.yaml. **29th consecutive report.**

## Findings

### Cadence Analysis

**Data points**: 144 sessions over ~88 hours, 40 changelog entries since last tune

| Task | last_runs Timestamp | Actual Last Run (verified) | Status |
|------|---------------------|----------------------------|--------|
| validate-all | 2026-01-24 02:57 | Not run since Jan 24 | **87 days stale** |
| pessimistic-review | 2026-04-20 18:37 | 2026-04-20 18:38 UTC | Current |
| optimistic-review | 2026-04-21 00:37 | 2026-04-21 00:38 UTC | Current |
| check-tenets | 2026-04-18 15:38 | **2026-04-21 12:48** (changelog + review file) | **Stale writeback — 3 days** |
| check-links | 2026-04-19 12:37 | 2026-04-19 | Current |
| deep-review | 2026-04-21 08:37 | 2026-04-21 (×9 today) | Current |
| tune-system | 2026-04-17 21:11 | 2026-04-21 12:59 (this run) | ~88h since last |
| research-voids | 2026-04-21 12:42 | 2026-04-21 12:42 UTC | Current |
| coalesce | 2026-04-21 10:37 | 2026-04-21 10:38 UTC | Current |
| apex-evolve | 2026-04-18 09:18 | 2026-04-21 12:51 UTC (per changelog) | **Stale writeback — 3 days** |
| agentic-social | 2026-04-21 12:37 | 2026-04-21 12:37 UTC | Current |
| tweet-highlight | 2026-01-24 14:00 | Not recently | 87 days stale (but P3 cadence) |

**NEW finding — `last_runs` writeback incomplete for check-tenets and apex-evolve**: The 2026-04-21 12:48 UTC check-tenets entry is in changelog.md and the review file `tenet-check-2026-04-21.md` exists, but `last_runs.check-tenets` still records 2026-04-18 15:38. Similarly, `last_runs.apex-evolve` records 2026-04-18 09:18 but the 2026-04-21 12:51 UTC entry is in changelog. Research-voids, deep-review, coalesce, pessimistic-review, optimistic-review, agentic-social all wrote through correctly. The pattern suggests the `tools/evolution/` code path that persists `last_runs` is not called (or is skipped) when cycle-trigger tasks complete — only when queue tasks do. Investigate.

**`validate-all`**: 87 days stale. **24th consecutive report.** Skill described in CLAUDE.md as "Daily health check" but not wired into the automation cycle. Effectively unused.

**`tune-system` cadence settled**: 88h interval vs previously-observed ~36h. Sessions per cycle (24) × cycles per tune (6) = 144 sessions → at ~37 min/session (≈default 2400s interval) this works out to ~88h / 3.67 days. Closer to — but still shorter than — the skill's documented 30-day cadence. **29th consecutive report noting the cadence-vs-skill-spec mismatch.**

### Failure Pattern Analysis

**Data points**: 40 changelog entries since last tune, 20 recent_tasks in state (all success), `failed_tasks: {}`.

| Task Type | Executed | Skipped/Abandoned | Rate |
|-----------|----------|-------------------|------|
| deep-review | ~20 | 0 | 0% |
| refine-draft | 4 | 0 | 0% |
| coalesce | 3 | 1 (2026-04-20, no good candidates) | 25% |
| expand-topic | 4 | 0 | 0% |
| pessimistic-review | 1 | 0 | 0% |
| optimistic-review | 2 | 0 | 0% |
| research-topic | 1 | 0 | 0% |
| research-voids | 1 | 0 | 0% |
| check-tenets | 1 | 0 | 0% |
| apex-evolve | 2 | 1 (skipped — dualist taxonomy apex duplicate) | 33% |

**Hard-failure reliability**: 15th consecutive tune period with 0% hard-failure rate.

**Coalesce abandon rate** (rolling): One abandon in the period (2026-04-20 10:38 UTC, no good candidates), three successes. 25% abandon on very small N; within the observational volatility flagged last period. Recommendation to hold current 2/24 cycle allocation stands.

**Apex-evolve skip was principled** (not a failure): 2026-04-21 12:38 UTC skipped an apex creation for the dualist four-quadrant taxonomy after concluding the same-day topic article already performs the synthesis and the 20-apex cap is full. Good discipline; recorded to `apex_evaluations`.

**Deep-review marginal-value signal**: Several near-zero-change reviews continue (e.g., `voids/affective-void` 2026-04-20 13:38 with 0-word change on third pass marking convergence). Previous Tier 2 #6 (per-article convergence tracking) remains the right fix.

### Queue Health Analysis

**Data points**: Current todo.md state (4267 lines).

| Priority | Active Count |
|----------|--------------|
| P0 | 0 |
| P1 | 0 |
| P2 | 5 (3 cross-review tasks from 2026-04-21 chain; 2 deep-review tasks) |
| P3 | 398 |

**Queue composition**: P2 tier populated by 2026-04-21 task chains (inspection-paradox → observation-and-measurement cross-review; presence-type-and-absence-type → taxonomy-of-voids and ineffable-encounter cross-reviews). Chain generation working as designed. Replenishment did not need to fire (P0–P2 count ≥ 3).

**P3 overhang now at 398**: The P3 tier continues to grow faster than it is executed — last period had ~35 P3 items visible in first several hundred lines; current count is 398. Most are optimistic-review-generated expand-topic suggestions. Several are executable (target sections have capacity). The overhang indicates the cycle is deliberately protective of new-article creation (most expand slots go to chain/queue tasks), but it also means P3 items are effectively archival unless promoted.

**No P0/P1 activity across the period**. Queue is healthy and self-regulating; human is not urgently needed.

### Review Finding Patterns

**Data points**: 1 pessimistic review, 2 optimistic reviews, 1 tenet check (0/0/0), ~20 deep reviews in period.

**Tenet check**: 2026-04-21 12:48 UTC produced **0 errors, 0 warnings, 0 notes** on a 53-file delta sweep — fourth consecutive zero-error check and third consecutive zero-note check. Corpus is at high-water mark for tenet alignment.

**Pessimistic→refine pipeline**: Tight. 2026-04-20 18:38 pessimistic review on `phenomenological-method-and-evidence-standards` flagged 2 high-severity, 3 medium-severity, 1 low-medium issue plus 3 counterarguments → 2026-04-20 19:38 refine-draft addressed all six addressable issues. Same pattern as prior tune period.

**Style-guide enforcement**: "Not X but Y" LLM-cliché construct flagged in style guide continues to surface in pessimistic reviews (9+ instances in the 2026-04-20 review). Multiple refine-drafts this period (and the prior period) remove them on detection. The construct is actively hunted.

**Recurring pessimistic theme (ACTIVE)**: Argumentative leaps from structural phenomenological claims to tenet-supporting conclusions continue to be flagged (2026-04-19 mood-void: "mood is opaque" → "mood is a candidate channel" non sequitur; 2026-04-20 phenomenological-method: introspective-report apodicticity → epiphenomenalism harder non sequitur). Both got refine-draft follow-ups.

### Convergence Progress

| Category | Count | Cap | % of Cap | Direction |
|----------|-------|-----|----------|-----------|
| Topics | 233 | 250 | 93.2% | 17 slots remaining (+3 vs prev) |
| Concepts | 227 | 250 | 90.8% | 23 slots remaining (-2 vs prev) |
| Voids | 94 | 100 | 94.0% | 6 slots remaining (-2 vs prev) |
| Arguments | 6 | — | — | stable |
| Apex | 22 | — | — | stable (cap 20 — **over by 2**) |

**Voids continued to drop** (96 → 94) without research-voids blocking. Capacity-aware automation working as intended.

**Apex 22/20**: Apex cap is 20 per apex-articles.md approved list but the directory contains 22. The apex-evolve skip at 2026-04-21 12:38 noted the cap is "already at 20 per apex-articles.md approved list." Worth auditing which apex files are "approved" vs "in-progress" vs "overflow" — the raw directory count differs from the governance-tracked list.

**Quality metrics (unchanged for 32+ periods)**:
- Critical: 0 (target: 0) ✓
- Medium: 10 (target: ≤3) — persistent, likely stale counter
- Low: 3 — acceptable
- Orphans: 13 — unchanged despite active integration work

## Changes Applied (Tier 1)

*No changes applied.*

**Rationale**: Three independent blockers:
1. No `cadences` / `overdue_thresholds` / `replenishment_config` sections exist in evolution-state.yaml — nothing to tune.
2. No `tune_system_history` — cannot enforce cooldowns.
3. No `locked_settings` — cannot check human overrides.

**29th consecutive report** unable to apply Tier 1 changes for this structural reason. Parameters governing automation behaviour live inside `tools/evolution/` Python code rather than in YAML, so Tier 1 changes require code edits that are categorically out of scope for this skill.

## Recommendations (Tier 2)

### 1. Fix `last_runs` writeback for cycle-trigger tasks (NEW)

- **Proposed change**: Audit the code path in `tools/evolution/` that persists `last_runs` after task completion. `check-tenets` ran 2026-04-21 12:48 and `apex-evolve` ran 12:51; neither was written to `last_runs`. Queue-task writeback appears correct.
- **Rationale**: Stale `last_runs` for cycle-trigger tasks could cause over-triggering (system thinks task is overdue when it just ran) or under-triggering depending on how trigger gating is implemented.
- **Risk**: Low (read the code; fix in one place)
- **Priority**: Medium

### 2. Fix Stale `content_stats` / `progress` Counters (Carried Forward ×27)

- **Proposed change**: Add per-section file-counting at session start in `tools/evolution/state.py`.
- **Rationale**: 32nd consecutive report. Recorded state shows 35 topics (actual 233), 145 concepts (actual 227), 11 voids (actual 94), 542 reviews (actual 3355). No functional harm now (cap enforcement uses separate live counts) but the drift is cosmetic-at-minimum and confuses all metrics work.
- **Risk**: Low
- **Priority**: Medium (downgraded from High — no functional harm)

### 3. Add `tune_system_history` / `locked_settings` / `cadences` Sections (Carried Forward ×29)

- **Proposed change**: Populate evolution-state.yaml with the sections the skill spec expects: `cadences`, `overdue_thresholds`, `replenishment_config`, `tune_system_history`, `locked_settings`.
- **Rationale**: Without these, tune-system cannot make Tier 1 changes safely. Currently this report, like its 28 predecessors, is effectively advisory-only.
- **Risk**: Low
- **Priority**: High

### 4. Add `validate-all` to Cycle Triggers (Carried Forward ×24)

- **Proposed change**: Add `"validate-all": 2` or similar to `CYCLE_TRIGGERS` in `tools/evolution/cycle.py`.
- **Rationale**: 87 days stale. Listed in CLAUDE.md as "Daily health check" but not wired into automation.
- **Risk**: Low (read-only check)
- **Priority**: Medium

### 5. Reconcile tune-system Cadence (Carried Forward ×2)

- **Proposed change**: Either (a) adjust the cycle trigger from "every 6 cycles" to "every 20+ cycles" to approach the skill's 30-day documented cadence, or (b) revise the skill spec to 3–4 day cadence matching current operation.
- **Rationale**: Current ~88h cadence is a compromise that nobody chose. Each run covers a small delta; most findings are carried forward. Adjusting to monthly would cut tune-system cost by ~8× with minimal signal loss.
- **Risk**: Low
- **Priority**: Medium

### 6. Implement Deep-Review Convergence Tracking (Carried Forward ×18)

- **Proposed change**: Track per-article review count and last word-change delta; skip further deep-review for articles with 3+ reviews all showing near-zero change.
- **Rationale**: Several zero-change convergence-confirmation reviews this period (e.g., affective-void 2026-04-20, consciousness-and-memory 2026-04-20 -6 words). Reviewers explicitly annotate "stability confirmed" but automation keeps re-queuing the file.
- **Risk**: Low
- **Priority**: High

### 7. Audit Apex Cap Governance (NEW)

- **Proposed change**: Resolve the apex-articles count discrepancy: apex-articles.md's approved list caps at 20 but `obsidian/apex/` contains 22 files. Either update the approved list, archive excess, or reset the cap to 22.
- **Rationale**: The 2026-04-21 apex-evolve skipped on cap grounds using the "20 per apex-articles.md" number while the directory has 22. Inconsistent governance means future apex-evolve decisions may treat real files as nonexistent.
- **Risk**: Low
- **Priority**: Medium

### 8. Update `convergence_targets` (Carried Forward ×31)

- **Proposed change**: `min_topics` 10→200, `min_concepts` 15→200, `min_arguments` 5→10, add `min_voids` 80, add `min_apex` 15, `max_medium_issues` 3 → 15.
- **Rationale**: Targets set for early-stage system; all vastly exceeded. Cosmetic issue only.
- **Risk**: Low
- **Priority**: Low

## Items for Human Review (Tier 3)

### 1. Stale State Tracking — 32nd Consecutive Report

- **Issue observed**: `content_stats.total_files` and `progress.*` counters frozen at early-project values.
- **Why human needed**: Code change to `tools/evolution/state.py`.
- **Suggested action**: Add per-section file-counting at session start to refresh `progress` and `content_stats`.

### 2. `last_runs` Writeback Gap for Cycle-Trigger Tasks (NEW)

- **Issue observed**: `check-tenets` and `apex-evolve` last_runs timestamps are 3 days stale despite successful 2026-04-21 runs recorded in changelog. Queue-triggered tasks (deep-review, coalesce, research-voids, research-topic, refine-draft, optimistic-review, pessimistic-review) all wrote through correctly. Pattern suggests cycle-trigger task paths skip `last_runs` update.
- **Why human needed**: Code inspection of `tools/evolution/cycle.py` and related task dispatch paths.
- **Suggested action**: Find the dispatch branch for cycle-trigger tasks and ensure it calls the same `state.update_last_run(task_name, now)` the queue dispatch does.

### 3. Medium Issues Persistent at 10 (Carried Forward ×23)

- **Issue observed**: Medium issues count has been exactly 10 for 23 consecutive tune periods.
- **Why human needed**: Decide whether this is a stale counter (likely) or live tracking.
- **Suggested action**: Inspect the source of `quality.medium_issues` and confirm it is recomputed at session start.

### 4. Orphaned Files Persistent at 13 (Carried Forward ×10)

- **Issue observed**: Same 13-orphan count through extensive cross-linking work.
- **Why human needed**: Almost certainly stale detection.
- **Suggested action**: Re-run orphan detection against live file state and verify.

### 5. Apex Cap Inconsistency (NEW)

- **Issue observed**: `obsidian/apex/` contains 22 files; apex-articles.md's governance list caps at 20; the 2026-04-21 apex-evolve skip cites the 20-cap. These three numbers should agree.
- **Why human needed**: Editorial/governance decision about which apex files are canonical.
- **Suggested action**: Reconcile the approved list against the filesystem; archive overflow or update cap.

### 6. tune-system Cycle-vs-Cadence Mismatch (Carried Forward ×2)

- **Issue observed**: Skill documents 30-day cadence; cycle trigger fires ~every 3.67 days.
- **Why human needed**: Pick a cadence.
- **Suggested action**: Either relax cycle trigger to every 20+ cycles or update the skill spec.

## System Health Summary

| Component | Status | Notes |
|-----------|--------|-------|
| Task execution | **Excellent** | 0% hard failure rate (15th consecutive period) |
| Skip rate | Excellent | Low; principled (apex skip, coalesce abandon) |
| Content quality | Excellent | 0 critical issues; 0 tenet errors/warnings/notes |
| Queue management | Healthy | P2 at 5 (chain-driven); P3 overhang 398 |
| Expand-topic efficiency | Good | 4/4 success |
| Coalesce efficiency | Holding | 1 abandon / 4 attempts |
| Review system | Excellent | 23 reviews/day; cross-integration strong |
| Deep-review convergence | Mixed | Zero-change reviews still occur on stable articles |
| Scheduling | Operational | Cycle mechanism stable at ~88h per tune |
| State tracking | **Broken** | content_stats/progress stale (32nd report); `last_runs` writeback gap for cycle-trigger tasks (NEW) |
| Topics cap | Healthy | 233/250 — 17 slots |
| Concepts cap | Healthy | 227/250 — 23 slots |
| Voids cap | Tight | 94/100 — 6 slots |
| Apex cap | **Inconsistent** | 22 files vs 20 approved (NEW) |
| Site validation | **Gap** | validate-all not running (87 days; 24th report) |
| Tenet alignment | **Excellent** | 0/0/0 on 53-file delta |
| Pessimistic→refine pipeline | **Excellent** | Same-day address of 2026-04-20 findings |
| tune-system infrastructure | **Blocked** | 29th report unable to apply Tier 1 (no params in state) |

## Next Tuning Session

- **Expected (at current cycle-trigger rate)**: ~2026-04-25 (3.67 days out)
- **Recommended per skill spec**: 2026-05-21 (30 days out)
- **Focus areas next run**:
  - Whether `last_runs` writeback gap has been addressed (NEW — monitor check-tenets, apex-evolve, check-links, validate-all if added)
  - Whether apex count reconciled against governance list (22 vs 20)
  - Whether stale state tracking gets addressed (33rd report)
  - Whether `tune_system_history` / `locked_settings` / `cadences` sections appear (30th report)
  - Whether validate-all is integrated (25th report)
  - P3 overhang trajectory (398 now; does it stabilise or keep growing?)
  - Coalesce abandon rate (small N; watch for pattern)