---
title: "System Tuning Report - 2026-08-02"
created: 2026-08-02
modified: 2026-08-02
human_modified: null
ai_modified: 2026-08-02T08:45:00+00:00
draft: false
description: "Monthly meta-review: the 30-day min-age gate that should throttle this skill is bypassed on the /unfin-cycle path, so this is the 12th tuning report in 17 days."
topics: []
concepts: []
related_articles:
  - "[[todo]]"
  - "[[changelog]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-08-02
last_curated: null
---

# System Tuning Report

**Date**: 2026-08-02
**Sessions analyzed**: session_count 18162, cycle_position 12240 (cycle 510 completed this run)
**Period covered**: 2026-07-30T23:57Z (previous tune-system run) → 2026-08-02T08:45Z — **2.36 days**

## Executive Summary

The system is operationally healthy: zero failures across the last 47 logged task
completions, `critical_issues: 0`, `orphaned_files: 0`. No abort condition is met.

Two structural findings dominate, and neither is fixable from this skill's Tier-1
licence. First, **the 30-day wall-clock gate written specifically to stop this skill
running too often is not applied on the code path that actually invoked it** — this is
the 12th tuning report in 17 days. Second, **all three Tier-1 change types remain
structurally impossible** because the settings they target are absent from state, a
finding now recorded for the third consecutive run without resolution.

Zero Tier-1 changes applied.

## Metrics Overview

| Metric | Current | Previous (07-30) | Trend |
|--------|---------|------------------|-------|
| session_count | 18162 | — | ↑ |
| cycle_position | 12240 | — | ↑ (cycle 510 completed) |
| Failure rate (last 47 logged) | 0% | 0% | → |
| critical_issues | 0 | 0 | → |
| medium_issues | 10 | — | **over target (max 3)** |
| Queue P0/P1/P2/P3 | 0 / 0 / 5 / 27 | 0 / 0 / 2 / 31 | P2 ↑, P3 ↓ |
| orphaned_files | 0 | 0 | → |
| topics / concepts / voids | 318 / 318 / 100 | — | at or near cap |

## Findings

### A. Cadence Analysis

**A1 (new, concrete) — the tune-system min-age gate is bypassed on the `/unfin-cycle` path.**

`tools/evolution/cycle.py` defines `TRIGGER_MIN_AGE_HOURS = {"tune-system": 30 * 24}`,
with a comment recording exactly the pathology it was written to prevent: *"without this
gate it was running daily (9 reports in 9 days, each declining to apply Tier-1 changes)."*

The gate is enforced in exactly one place — `scripts/evolve_loop.py:1370`, inside the
Python orchestrator's session loop. The `/unfin-cycle` path does not go through that
function. `tools/evolution/cycle_pick.py` drains `.unfin/pending-triggers.json` serially
(its step 2) and emits whatever it finds, with no min-age filtering.

Evidence: `last_runs["tune-system"]` was 2.36 days old when this run was dispatched,
against a 30-day gate. Reports on disk: 2026-07-17, 07-18, 07-26, 07-29, 07-30, 08-02 —
**12 `system-tune-*` reports carry a July-or-August date**, against a documented monthly
cadence. The gate is correct; its application is incomplete.

This is Tier 3 (code change) and is the highest-value item in this report, because it is
the direct cause of the redundancy every recent tuning report has noted about itself.

**A2 — dead `last_runs` keys.** `validate-all` (190.2d) and `tweet-highlight` (189.8d)
have not run in over six months; `tweet-highlight` is marked DEPRECATED in CLAUDE.md and
`validate-all` has been superseded by in-pipeline validation. Three
`commission-*-chrome-unavailable-at` keys are 19 days stale. These are inert but they
make `last_runs` misleading to read.

**A3 — `integrate-orphan` at 45.2 days** is not a cadence failure: `orphaned_files: 0`,
so there is nothing for it to do. Correct silence.

### B. Failure Pattern Analysis

**No findings — evidence threshold not met, and that is the correct outcome.**
`failed_tasks` is empty (`{}`) and the last 200 log lines contain 47 task completions,
**all `status=SUCCESS`**. There is no failure pattern to analyse. Recorded so a future
run does not read the empty section as an omission.

### C. Queue Health Analysis

**C1 — every standard replenishment source is dry.** `replenishment_source_counts` from
run 925 reads `lens_divergent_verbatim_quote: 0`, `orphan_integration: 0`,
`length_analysis: 0`, `staleness: 0`, `unconsumed_research: 0`. All five at zero.

**C2 — the floor metric measures the wrong thing.** Run 925 minted **zero** tasks and
instead promoted three P3s and closed one superseded task, on the finding that the queue
is 32 deep while the floor counts only P0–P2. Runs 919–924 had each minted two fresh P2s
against an unpicked 27-to-31-task P3 backlog. The selector sorts `(priority,
line_number)`, so P3 work is unreachable while any P2 exists — and replenishment
guarantees one always does.

This is a genuine structural finding, already acted on once by promotion. The durable fix
is a floor definition that counts pickable work rather than P0–P2 specifically, which is
Tier 3.

### D. Review Finding Patterns

**D1 — the dominant recurring theme across this period's reviews is a single mechanism:
a correct ruling that never propagates past the file it was made in.** Instances closed
in the last 24 hours alone: Wallace 2003 page range (4 loci + record correction), four
BBS commentary-inclusive page ranges (41 files), the BBS triage tail (2 further families),
Kripke 1972/Harvard tuple (6 loci), Chalmers 2006/2007 (21 loci), the 2±1 attribution
family (3 loci, including one on a served archive page that a prior sweep had declared
closed), and six canonical quotations still corrupted in `research/` and `archive/` after
the live tree was fixed (29 replacements).

`/check-tenets` independently named the same shape today as **Family Q**, with a new
variant: not a failed *inheritance* but a failed *diffusion* — a distinction stated
correctly in thirteen places that never left the cluster that invented it.

**D2 — reviews ratify defects, they do not merely miss them.** Three instances this
period: a quote-fidelity lens that *exempted* the corpus's one fabricated quotation for
being a self-quote; a deep-review ledger that blessed the broken `1972 + Harvard` tuple
as "real-correct (canon)"; and a July ruling that invented a print-vs-online mechanism to
justify a year the publisher contradicts. A confirming prior review is not evidence.

**D3 — `medium_issues: 10` against `convergence_targets.max_medium_issues: 3`.** This is
the one live quality-target breach. It is not a regression — the count reflects findings
raised faster than they are closed, which is what a productive review system looks like —
but the target has not been met and no run has flagged it.

### E. Convergence Progress

**E1 — the convergence targets are vestigial.** `min_topics: 10` against 318 written;
`min_concepts: 15` against 318; `min_arguments: 5` against 5 (exactly met). These were
floor targets for a young corpus and have been met by one to two orders of magnitude.
They no longer describe anything the system is steering toward.

**E2 — the real constraint is now the cap, not the floor.** `topics/` 318/320,
`concepts/` 318/320, `voids/` 100/100. Roughly **two article slots remain corpus-wide**.
`research-voids` recorded its fifth consecutive cap-blocked no-op today; an optimistic
review identified a genuine uncovered subject (enhancement-through-disruption) and
correctly declined to mint it because there is nowhere to put it.

`topics/` and `concepts/` were raised 300→320 on 2026-06-20; `voids/` has never moved
from 100. CLAUDE.md's section table still reads ~273 topics / ~265 concepts.

## Changes Applied (Tier 1)

*No changes applied.*

All three licensed Tier-1 change types target keys that are **absent from
`evolution-state.yaml`**:

| Licensed change type | Target key | Status |
|---|---|---|
| Cadence adjustment | `cadences.*` | **absent** |
| Overdue threshold | `overdue_thresholds.*` | **absent** |
| Replenishment weight | top-level source weights | **absent** |

`locked_settings` is also absent, so the pre-change lock check has nothing to read. The
17 top-level keys present are: `agentic_social`, `audit_triple`, `content_stats`,
`convergence_targets`, `cycle_position`, `failed_tasks`, `last_git_push`, `last_runs`,
`last_tweet_date`, `last_updated`, `progress`, `quality`, `queue_status`, `recent_tasks`,
`section_caps`, `session_count`, `tune_system_history`.

This is the **third consecutive run** to report zero Tier-1 changes for this reason
(2026-07-29, 2026-07-30, 2026-08-02). The skill's automatic-adjustment tier has been
inert since the keys were dropped in commit `dd6ce48fa` (2026-01-25).

## Recommendations (Tier 2)

### R1 — Retire or re-base the convergence targets
- **Proposed change**: replace the `min_*` floors with targets that describe the current
  regime — e.g. cap headroom, review-debt closure rate, or `medium_issues` trend.
- **Rationale**: finding E1. Targets exceeded 30× measure nothing.
- **Risk**: Low. They are read for reporting, not for dispatch.
- **To approve**: edit `convergence_targets` in `evolution-state.yaml`.

### R2 — Prune the dead `last_runs` keys
- **Proposed change**: drop `tweet-highlight`, `validate-all`, and the three
  `commission-*-chrome-unavailable-at` keys.
- **Rationale**: finding A2. They make the section misleading at a glance.
- **Risk**: Low, but *not* zero — confirm nothing reads them before removing.
- **To approve**: manual edit; do not let a fork do this unattended.

## Items for Human Review (Tier 3)

### T1 — Apply the min-age gate on the `/unfin-cycle` path *(highest value in this report)*
- **Issue observed**: finding A1. `filter_triggers_by_min_age` is called only at
  `scripts/evolve_loop.py:1370`. `tools/evolution/cycle_pick.py` drains
  `.unfin/pending-triggers.json` without it, so every per-skill wall-clock gate is
  inoperative whenever the loop is driven by `/unfin-cycle` — which is how it has been
  driven throughout this period.
- **Why human needed**: code change in the dispatch path.
- **Suggested action**: call `filter_triggers_by_min_age` in `cycle_pick.py`'s
  pending-trigger drain, re-queueing or dropping gated entries. This alone would end the
  12-reports-in-17-days pattern and restore the intended monthly cadence.

### T2 — Restore or formally retire the cadence schema
- **Issue observed**: the Tier-1 table above; third consecutive inert run.
- **Why human needed**: either re-add `cadences` / `overdue_thresholds` /
  `locked_settings` to state (and reconcile with the cycle-trigger schedule that
  currently owns scheduling), or amend this SKILL.md to stop licensing changes to keys
  that do not exist. Amending a SKILL.md is explicitly outside this skill's authority.
- **Suggested action**: decide which mechanism owns scheduling — `cadences` in state, or
  `CYCLE_TRIGGERS` in `tools/evolution/cycle.py` — and delete the other.

### T3 — Section caps are the binding constraint
- **Issue observed**: finding E2. ~2 slots remain across `topics/` and `concepts/`;
  `voids/` full since before 06-20.
- **Why human needed**: raising a cap or authorising an archival pass is a content-scope
  decision.
- **Suggested action**: raise the caps, or authorise archival, or formally park the
  research-generation lane so `harvest-research-subjects` and `research-voids` stop
  producing no-ops. Also update CLAUDE.md's section table, which reads ~273/~265 against
  a real 318/318.

### T4 — Redefine the replenishment floor
- **Issue observed**: finding C2.
- **Why human needed**: changes dispatch behaviour.
- **Suggested action**: count pickable open work rather than P0–P2 specifically, so a
  27-task P3 backlog does not read as an empty queue.

### T5 — Coalesce's cap-relief mandate
- **Issue observed**: eleven consecutive reasoned ABANDONs with eleven distinct
  discriminators, the latest today. Five separate passes have now recommended retirement.
- **Why human needed**: removes a cycle slot allocation.
- **Suggested action**: retire the mandate and reallocate its two slots per 24-cycle, or
  accept the slots as a periodic no-op audit.

## Next Tuning Session

- **Recommended**: 2026-09-01 (30 days), **contingent on T1** — without the gate fix this
  skill will fire again within roughly 2–3 days.
- **Focus areas**: whether T1 landed and the cadence normalised; whether
  `medium_issues` closes toward its target of 3; whether cap headroom was resolved.
