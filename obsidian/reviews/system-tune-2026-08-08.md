---
title: "System Tuning Report - 2026-08-08"
created: 2026-08-08
modified: 2026-08-08
human_modified: null
ai_modified: 2026-08-08T01:04:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[todo]]"
  - "[[changelog]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-08-08
last_curated: null
---

# System Tuning Report

**Date**: 2026-08-08
**Sessions analyzed**: session_count 18673, cycle_position 12528 (cycle 522 complete)
**Period covered**: 2026-08-03 20:11 UTC → 2026-08-08 01:04 UTC (4.2 days since previous run)

## Executive Summary

System health is good on every operational metric that this skill can actually measure: zero critical issues, zero orphaned files, one failure in the last twenty tasks, and a queue at its floor rather than empty. **The finding of this run is not about the corpus — it is about this skill.** For the fifth consecutive run, zero Tier-1 changes were applied, and this was not a judgement call: the three settings blocks Tier-1 is defined to adjust (`cadences`, `overdue_thresholds`, `locked_settings`) have been **absent from `evolution-state.yaml`** since commit `dd6ce48fa`. Simultaneously the skill is firing at roughly **15× its designed rate**. Both facts have now been reported three to five times without resolution, which makes *the reporting loop itself* the thing needing attention.

## Metrics Overview

| Metric | Current | Notes |
|--------|---------|-------|
| Session count | 18673 | |
| Cycle position | 12528 | cycle 522 complete |
| Critical issues | **0** | abort condition not met |
| Medium / low issues | 10 / 3 | |
| Orphaned files | 0 | |
| Failures in last 10 tasks | **1** | `research-voids` stall; abort threshold is >5 |
| `failed_tasks` | `{}` | empty |
| Queue P0/P1/P2/P3 | 0 / 0 / 4 / 28 | at floor, not starved |
| Tier-1 changes applied | **0** | fifth consecutive run; *structurally impossible* |

## Findings

### A. Cadence Analysis — T1 (recurring, confirmed in code again)

`TRIGGER_MIN_AGE_HOURS["tune-system"] = 720` (`tools/evolution/cycle.py:67-71`), and the config carries a comment anticipating exactly this failure: *"the every-6-cycles trigger otherwise fires it ~daily at fast --interval."*

`filter_triggers_by_min_age` has **exactly one call site**: `scripts/evolve_loop.py:1370`. The `/unfin-cycle` path does not use it — `cycle_post` enqueues to `.unfin/pending-triggers.json` and `cycle_pick.py` drains it (L143-146) and emits directly, **gated at neither end**.

**Evidence, well past the 5-point threshold — 81 `system-tune-*` reports exist.** The last eight intervals:

| Run | Gap |
|---|---|
| 2026-07-15 | — |
| 2026-07-17 | +2d |
| 2026-07-18 | +1d |
| 2026-07-26 | +8d |
| 2026-07-29 | +3d |
| 2026-07-30 | +1d |
| 2026-08-02 | +3d |
| 2026-08-03 | +1d |
| 2026-08-08 (this) | +4d |

Mean ≈ 2.9 days against a designed 30. **This run was handed the finding as if new; it is not — it was confirmed in code by the 2026-08-02 and 2026-08-03 runs and recorded in `tune_system_history.last_run_note`.** Recording it a fourth time adds nothing. It is escalated below as T3 instead.

### B. Failure Pattern Analysis — below evidence threshold

One failure in the recent window: `research-voids` stalled 2026-08-07 23:15 UTC (watchdog, 600s, zero output, no partial writes). `failed_tasks` is empty. **One occurrence does not meet the 3-occurrence threshold** and no pattern is claimed.

Two reliability observations are recorded for future accumulation, both below threshold as *state* findings but notable in volume: **five separate forks set `ai_modified` to a future timestamp** in one day (largest +6 minutes), each caught and corrected by the driver; and the driver twice ran `cycle_post` before a fork had finished, once capturing an intermediate draft that was superseded before the push. Neither is a settings problem, so neither is tunable here.

### C. Queue Health Analysis — healthy, no action

P0-P2 at 4 against a floor of 3; 28 P3. `needs_replenishment: false`. Two replenishments on 2026-08-07 (13:40, 15:25), both minting rather than promoting, with the run-943 note recording that promotion was preferred but genuinely unavailable and the candidates verified unowned. That is the documented steady state, not a defect.

### D. Review Finding Patterns — T2 (meets threshold)

**54 open `NEEDS-HUMAN` entries.** By category:

| Category | Count |
|---|---|
| length decision | 9 |
| loop tooling | 8 |
| methodology / methodology ratification | 10 |
| calibration policy | 2 |
| other (14 singleton categories) | 25 |

The two largest clusters are **batchable**: the 8 `loop tooling` entries are small, individually verified defects that already cross-reference one another as *"RELATED, DECIDE TOGETHER"* (the `count_section_files` sidecar over-count, the `anchoring.py` hedge counter, the `altered_state_symmetry.py` vocabulary, `find_superlative_claims` recall, the missing `scripts/curate.py`, the agentic-social selector, the `check-model-fallback` dedup). The 9 `length decision` entries are the same shape at a different layer — each asks whether one flagship may exceed a threshold. **These are ~17 of 54 entries that plausibly resolve as two decisions rather than seventeen.**

### E. Convergence Progress — measured, no stall

`topics_written` 319, `concepts_written` 315, `voids_written` 99, `positions_written` 14, `apex_articles` 39, `research_notes` 537. Both large sections are within 5 of their 320 cap, so convergence in those sections is now **cap-bound rather than effort-bound** — the loop has correctly shifted to improvement work. `positions/` at 14 of 80 is the one domain with real headroom, and it grew by 2 entries today.

## The cross-cutting pattern this run was asked to test

The brief proposed two candidate common causes. **Both are supported, and they are the same mechanism at different layers: a producer changed and its consumers were never updated, because nothing checks consumers.**

Instances evidenced within the last 24 hours:

| Consumer still expecting | Producer that changed |
|---|---|
| `refine-draft/SKILL.md` step 3 | `scripts/curate.py` deleted in a LiteLLM-skeleton cleanup |
| **this skill's Tier-1 mechanism** | `cadences` / `overdue_thresholds` / `locked_settings` removed from state at `dd6ce48fa` |
| CLAUDE.md cap table; a queued task quoting it | section counts grew; `count_section_files` counts a sidecar |
| an open P3's named grep stem `prefers Stapp` | corpus gained `prefers **Henry** Stapp's` (2 live loci) |
| six `description:` blurbs | their own bodies were corrected by later passes |
| `agentic-social` overlap filter | the posting window saturated to 0 survivors of 670 |

Each was *true when written*. None is a bug in the usual sense; each is a reference that silently outlived its referent. **The failure is uniform: there is no check that a documented instruction, a cited figure, or a named stem still resolves.** That is why these surface one at a time, always incidentally, and always to whoever happens to read the consumer.

This also explains the second candidate — "instruments that report but cannot act." **This skill is the purest case**: 81 reports produced, Tier-1 inoperative for five consecutive runs, firing 15× more often than designed. The instrument is not broken; its *actuator* was removed and its *governor* was bypassed, and it has faithfully reported both several times into a channel that has not acted.

## Changes Applied (Tier 1)

*No changes applied.* **Not a judgement — structurally impossible.** `cadences`, `overdue_thresholds` and `locked_settings` are all absent from `evolution-state.yaml` (verified this run). Every Tier-1 change type defined in this skill targets one of those three blocks, so the mechanism has nothing to write to. This is the fifth consecutive zero-change run for the same reason.

## Recommendations (Tier 2)

### Batch the two largest NEEDS-HUMAN clusters into two decisions
- **Proposed change**: group the 8 `loop tooling` entries into a single operator sitting, and the 9 `length decision` entries into a second.
- **Rationale**: the tooling entries already declare themselves mutually related; each is small, verified and operator-gated only because it touches `scripts/` or `tools/`. Resolving them individually costs 8 context loads; together, one.
- **Risk**: Low — no entry is time-critical, and none is a content change.
- **To approve**: human triage; no automation change required.

## Items for Human Review (Tier 3)

### 1. Restore the Tier-1 settings blocks, or retire the Tier-1 mechanism
- **Issue observed**: `cadences`, `overdue_thresholds` and `locked_settings` vanished from state at `dd6ce48fa`. This skill's SKILL.md documents three Tier-1 change types, all of which write to those blocks, plus a cooldown and locked-settings protocol that reference them.
- **Why human needed**: this is a choice between two coherent designs — restore the blocks and let the skill tune again, or accept that cadence is now code-defined (`TRIGGER_MIN_AGE_HOURS`) and **rewrite SKILL.md to drop Tier-1**, making the skill explicitly report-only. Either is defensible; continuing to document a capability that cannot execute is not.
- **Suggested action**: decide the design, then update `SKILL.md` (operator territory — this skill must not edit it).

### 2. The 30-day gate is inoperative on the `/unfin-cycle` path
- **Issue observed**: `filter_triggers_by_min_age` is called only at `scripts/evolve_loop.py:1370`; `cycle_pick.py` drains pending triggers at L143-146 without it. Result: 81 reports at a ~2.9-day mean against a 30-day design.
- **Why human needed**: a one-call-site code change in `tools/evolution/`, which content automation is barred from touching.
- **Suggested action**: apply the same gate at the `cycle_pick` drain, or remove `tune-system` from the cycle-trigger table and let the wall-clock path own it. **Reported for the fourth time; if it is intentional, please close it as such so the report stops recurring.**

### 3. No mechanism detects a reference outliving its referent
- **Issue observed**: six instances in 24 hours (table above) of a documented instruction, cited figure or named grep stem that was true when written and silently is not now.
- **Why human needed**: the fix is a new check, not a tuned parameter — e.g. a cheap CI-style pass asserting that paths named in `SKILL.md` files exist, and that figures quoted in `CLAUDE.md` match what the gating function returns.
- **Suggested action**: consider whether one such check would retire a recurring class of defect. This is the highest-leverage item in the report.

## What this run did not analyse

- **Per-source queue productivity** (`replenishment_source_counts`): the key is absent from state, so source-to-execution rates could not be computed.
- **Convergence *rate*** per session: `progress` holds current totals only, with no time series in state, so trend claims would be unfounded. Section counts against caps are reported instead.
- **The 25 singleton `NEEDS-HUMAN` categories** were counted but not individually read.
- **Fork-reliability trends** (stalls, future-dating) beyond this session — no historical series exists in state to compare against.

## Next Tuning Session

- **Recommended**: 2026-09-07 (30 days), *if* the gate is repaired. Absent repair, expect the next firing in ~2-3 days.
- **Focus areas**: whether Tier-3 items 1 and 2 have been decided; whether the NEEDS-HUMAN backlog has been batched or has grown past 60; whether any reference-rot check was adopted.
