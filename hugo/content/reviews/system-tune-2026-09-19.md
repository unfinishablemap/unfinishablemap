---
ai_contribution: 100
ai_generated_date: 2026-09-19
ai_modified: 2026-09-19 17:09:01+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-19
date: &id001 2026-09-19
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-19 17:09:01+00:00
modified: *id001
related_articles:
- '[[todo]]'
- '[[changelog]]'
title: System Tuning Report - 2026-09-19
topics: []
---

# System Tuning Report

**Date**: 2026-09-19
**Sessions analysed**: session_count 20966; cycle 570 closed this run (cycle_position 13680)
**Period covered**: since last tune-system 2026-09-17T01:49

## Executive Summary

No abort condition; no Tier 1 change applied — **and the reason no cadence change was applied is itself the headline finding: `cadences` and `overdue_thresholds` do not exist in `evolution-state.yaml`**, so this skill's primary automatic lever has no configuration to act on. Two further structural findings dominate: the **NEEDS-HUMAN escalation channel is effectively write-only** (70 open, 1 ever closed, oldest 2026-06-01), and **article creation has stalled** while research accumulates (`expand-topic` idle 12 days, every organic replenishment source at zero).

## Abort conditions — none met

| Condition | Measured | Status |
|---|---|---|
| >50% of last 10 tasks failed | `recent_tasks`: 20/20 `outcome: success`, `failed_tasks: {}` | pass |
| `quality.critical_issues > 0` | 0 | pass |
| File read errors | none | pass |
| Convergence regressed 3+ sessions | no regression signal available | pass (n/a) |

`locked_settings` is absent, so nothing was locked against change.

## Findings

### 1. The cadence config this skill tunes does not exist (Tier 3)

`evolution-state.yaml` top-level keys are: `agentic_social, audit_triple, content_stats, convergence_targets, cycle_position, failed_tasks, last_git_push, last_runs, last_tweet_date, last_updated, progress, quality, queue_status, recent_tasks, section_caps, session_count, task_chains, tune_system_history`.

**`cadences` → None. `overdue_thresholds` → None.** Both are described in this skill's step 4A and in CLAUDE.md's "Adding New Skills" section, and both are the target of two of the three Tier 1 change types. `last_runs` exists and is healthy (36 entries), so *when* things ran is known; *how often they should run* is not recorded anywhere machine-readable. Scheduling is instead hard-coded in `tools/evolution/cycle.py` and `time_trigger.py`.

**Consequence**: tune-system can never apply its two main Tier 1 change types. It has applied exactly **one** Tier 1 change in its history (2026-07-15, a `queue_status` prune). This is not a malfunction of any run — it is a missing interface.

### 2. The NEEDS-HUMAN channel is write-only (Tier 3)

Counted from `todo.md` by header date:

| Month opened | Still open |
|---|---|
| 2026-06 | 4 |
| 2026-07 | 17 |
| 2026-08 | 31 |
| 2026-09 | 10 |
| undated | 8 |
| **Total open** | **70** |
| **Ever closed** (`### ✓` + NEEDS-HUMAN) | **1** |

Oldest still open: **2026-06-01** — 110 days. Five were added today.

**Verdict: not healthy.** A resolution rate of 1-in-71 means "record it for the operator" currently functions as deferral, not escalation. The loop is generating operator-facing analysis at roughly 0.5–1.0 items/day and consuming none of it. The August peak (31) coincides with the period of heaviest structural discovery.

⚠️ This does **not** imply the entries are wrong — several were re-verified today and hold. It implies the channel has no drain.

### 3. Article creation has stalled while research accumulates (Tier 2)

| Signal | Value |
|---|---|
| `expand-topic` last run | 2026-09-07 (12 days) |
| `replenish-queue` last run | 2026-09-09 (10 days) |
| `integrate-orphan` last run | 2026-06-18 (93 days) |
| `task_chains.pending_articles` | 2 (both `target_section: voids`) |
| voids research notes / free slots | ~109 residual untriaged / 12 |
| Section headroom | topics 328/360, concepts 326/360, voids 103/115 |

Caps are **not** the constraint — there are 32 topic and 34 concept slots free. The constraint is that nothing is converting research into articles.

### 4. Replenishment runs entirely on recycling (Tier 2)

`replenishment_source_counts` from run 1032: **every organic source is 0** — `chain`, `gap_analysis`, `staleness`, `unconsumed_research`, `orphan_integration`, `optimistic_review`, `check_tenets`, `outer_review_synthesis`, `review_spillover`, `length_analysis`, `defect_family`, all three `positions_*`. The only non-zero source is `promotion_from_p3: 6`.

Queue composition: **P0 0, P1 0, P2 8, P3 88**, `loop_pickable_open: 6`. The run's own note is accurate: the queue is "short of loop-VISIBLE work, not of work". 88 P3s exist that the cycle never selects.

### 5. Quality target breach (Tier 3, low severity)

`quality.medium_issues` = **10** against `convergence_targets.max_medium_issues` = **3**. `critical_issues` 0 and `orphaned_files` 0 are both within target. Flagged rather than actioned: the target may be stale rather than the metric bad, and that is a human call.

### 6. Review finding patterns — corroborated, not re-derived

Per the driver brief, four scheduled operations were measured today and found structurally blocked, not unlucky: `coalesce` (10th consecutive no-op; 0 viable pairs of 5,253 in voids, 2 of 53,301 in topics), `research-voids` (supply 9:1 over slots; LIFO makes a new note net-negative), `check-links` (424 broken, **article prose 0**), and the Tenet-5 "parsimony tiebreaker" family (root cause found: a rule stated in ~10 files that `tenets.md` never states; flagged in six consecutive checks). **I did not re-run these.**

One correction to the brief: `recent_tasks` entries carry an **`outcome`** field, not `status` — and it *is* populated (20/20 `success`). The brief's claim that it is unusable was wrong. It is still weak evidence, because it records only what `cycle_post` was told.

## Changes Applied (Tier 1)

*No changes applied.* Cadence and overdue-threshold adjustments — two of the three permitted change types — are impossible because the config sections are absent (Finding 1). The third type (replenishment weight) has no weight field either; `replenishment_source_counts` is a counter, not a tunable. **Applying nothing is the correct conservative outcome, not a skipped step.**

## Recommendations (Tier 2)

### R1. Give the research→article pipeline a drain
- **Proposed**: schedule or queue explicit triage of the ~109-note voids research bank, then `expand-topic` runs against the survivors into the 12 free voids slots.
- **Rationale**: 32 topic + 34 concept + 12 void slots are free while `expand-topic` has been idle 12 days and 607 research notes exist.
- **Risk**: Low. Does not change any cadence.

### R2. Reallocate or gate the coalesce slots
- **Proposed**: either reassign coalesce's 2-of-24 slots to `deep-review`, or gate coalesce behind a cheap precondition that skips without consuming a slot when no pair fits.
- **Rationale**: 10 consecutive no-ops, provably impossible in 2 of 3 sections; `deep-review` produced 4 critical findings in 4 runs today.
- **Risk**: Medium — this is a cycle-composition change, hence Tier 2 not Tier 1.

### R3. Encode the ~4-item priority-list cap in the reports-only skills
- **Proposed**: add the cap to `pessimistic-review`, `optimistic-review` and `check-tenets` SKILL.md.
- **Rationale**: measured 4/4 on-list findings fixed vs 0/8 below the list.
- ⚠️ **Tier 3 by this skill's own rules** (skill-instruction modification is explicitly forbidden here) — recorded as a recommendation only, for a human to apply.

## Items for Human Review (Tier 3)

### T1. Create `cadences` / `overdue_thresholds`, or retire the claim that they exist
Either add the sections (making tune-system able to do its job) or amend this skill and CLAUDE.md to describe the real mechanism, which is code in `cycle.py`/`time_trigger.py`. **Leaving the documentation describing a config that does not exist is the worst of the three.**

### T2. Drain the NEEDS-HUMAN backlog, or change what the loop does with operator findings
70 open / 1 closed. If the operator cannot consume ~0.5–1.0 items/day, the loop should be told to stop producing them at that rate — bundling into a periodic digest, or a standing rule that only blocking items are escalated.

### T3. X API credits exhausted
`add-highlight --tweet` adds and pushes a highlight, passes its own deploy gate, and fails silently at the tweet. One un-tweeted highlight accrues per day. `last_tweet_date` is day-stamped on both paths, so the trigger correctly does not retry — the outage is invisible except in `recent_tasks`.

### T4. `quality.medium_issues` 10 vs target 3
Decide whether the target or the metric is stale.

## Next Tuning Session

- **Recommended**: 2026-10-19 (30 days).
- **Focus areas**: whether the NEEDS-HUMAN backlog drained; whether `expand-topic` resumed; whether coalesce slots were reallocated; whether `cadences` was created.