---
ai_contribution: 100
ai_generated_date: 2026-07-15
ai_modified: 2026-07-15 21:49:56+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-15
date: &id001 2026-07-15
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[todo]]'
- '[[changelog]]'
title: System Tuning Report - 2026-07-15
topics: []
---

# System Tuning Report

**Date**: 2026-07-15
**Sessions analyzed**: current /loop session (≈20 iterations) plus prior 07-15 replenish history in state
**Period covered**: 2026-07-12 → 2026-07-15

## Executive Summary

The automation is healthy and converging: this session ran a long clean sequence
(three converged-no-op staleness deep-reviews, a coalesce no-op, a full tenet
scan with zero violations, three attribution audits all closing no-op, and — the
generative bright spot — a working harvest→research-topic→research-note chain).
The one real operational problem is **state-file bloat**: `queue_status` had
accumulated 93 append-only `last_floor_restore_note_*` audit keys, growing
`evolution-state.yaml` to 602KB that is parsed and re-serialised on every
`cycle_post`/replenish. One Tier 1 hygiene change was applied (pruned to the 3
most-recent; 602KB → 399KB). The long-standing "replenish leans only on the
staleness seam" finding is now being mitigated by the harvester and needs no
replenish-side change yet.

## Metrics Overview

| Metric | Current | Previous | Trend |
|--------|---------|----------|-------|
| Pickable queue (P0-P2) | 3 (floor) | 3 | → |
| Replenish source diversity | 1 (staleness only) | 1 | → (mitigated by harvest) |
| Harvest yield this session | 3 research-topic tasks | 0 | ↑ |
| Tenet violations | 0 | 0 | → |
| Failed tasks this session | 0 | — | → |
| evolution-state.yaml size | 399KB (post-prune) | 602KB | ↓ |

## Findings

### Cadence Analysis

tune-system reports exist for 07-06, 07-08, 07-09, 07-10, 07-12, 07-14, and now
07-15 — i.e. it is firing every 1–2 days, not on its intended 30-day cadence.
This is the every-6-cycles cycle-trigger outrunning the 30-day `cadences.tune-system`
value at the current fast `--interval`. Each run is a conservative no-op/report,
so the harm is limited to a report file and a cycle slot per run, but the reports
are low-yield at this frequency. **Tier 3** (the trigger frequency lives in
`tools/evolution/cycle.py`, not a state param) — recommend gating the cycle-trigger
behind the 30-day cadence so it does not fire monthly-work multiple times per day.

### Failure Pattern Analysis

Zero failures this session. Three model-fallback attribution audits were queued
by `check-model-fallback` and all three closed as no-ops (the Opus-served windows
did only reviews/queue-maintenance, no authored content) — the "session sticks
self-attribute correctly" pattern holding. No action.

### Queue Health Analysis

The dominant multi-session pattern (flagged 9+ times in the pruned floor-restore
notes): every floor-restore this session drew on **staleness (Source 4)** because
chains, unconsumed-research, gap analysis, orphans, positions-audit, and
applied-apex were all dry or cap-governed. This produced a run of converged-no-op
deep-reviews before the harvester introduced genuine work. **However**, the 6h
`harvest-research-subjects` trigger minted 3 `research-topic` tasks from one
optimistic review this session, and the first already produced a solid research
note — the research→expand pipeline the earlier notes asked for now exists and is
working. Recommendation is therefore **to monitor, not to intervene** on the
replenish side yet (see Tier 2).

### Review Finding Patterns

The tenet scan (6 parallel agents over topics/concepts/positions) found zero
violations, confirming the corpus is calibration-stable. Deep-reviews this session
were near-no-ops (one one-token bibliographic fix across five reviews), consistent
with a mature, converged corpus. This corroborates the queue-health reading: the
corpus needs *new* territory (harvest) more than it needs re-review (staleness).

### Convergence Progress

Corpus is at/near section caps (topics ~317/320, concepts ~316/320, voids 100/100)
and citation-converged. No regression. The generative frontier is now cap-headroom
+ harvester-fed new articles, not review churn.

## Changes Applied (Tier 1)

| File | Setting | Old | New | Rationale |
|------|---------|-----|-----|-----------|
| evolution-state.yaml | queue_status.last_floor_restore_note_* | 93 keys (602KB) | 3 keys (399KB) | Pure append-only audit prose, zero logic dependence (grep-verified); unbounded per-replenish growth was bloating every YAML parse |

## Recommendations (Tier 2)

### Monitor harvest efficacy before any replenish-side change
- **Proposed change**: none yet — watch whether the 6h harvester keeps the queue
  fed with generative research→expand work over the next ~1 week.
- **Rationale**: the staleness-only floor-restore finding is real but the harvester
  is already backfilling it. Lowering MIN_QUEUE or slowing replenish now would be
  premature and could starve the named cycle slots.
- **Risk**: Low.
- **To approve**: no action; revisit at next tune-system if harvest yield drops
  and staleness churn resumes.

## Items for Human Review (Tier 3)

### Replenish should cap the floor-restore audit notes
- **Issue observed**: `/replenish-queue` appends a new `last_floor_restore_note_*`
  key to `queue_status` on every run, unbounded (93 accumulated, 602KB). This tune
  pruned them once, but they will regrow.
- **Why human needed**: the fix is in the replenish tool's note-writing logic
  (keep only N most-recent), not a state parameter.
- **Suggested action**: add a ring-buffer cap (e.g. keep 5 most-recent) to the
  note-append path in the replenish tooling.

### MIN_QUEUE and replenish cadence are code-level, not state-tunable
- **Issue observed**: `MIN_QUEUE_TASKS = 3` is hardcoded in
  `tools/evolution/cycle_pick.py`; there is no `replenishment_config` in state.
  The repeatedly-suggested "lower MIN_QUEUE / slow replenish" levers cannot be
  applied by tune-system.
- **Why human needed**: code change.
- **Suggested action**: only if harvest proves insufficient (see Tier 2) — consider
  MIN_QUEUE 3→2 to reduce converged-no-op churn. Not warranted while harvest works.

### tune-system cycle-trigger outruns its 30-day cadence
- **Issue observed**: running every 1–2 days via the every-6-cycles trigger.
- **Why human needed**: trigger frequency is in `tools/evolution/cycle.py`.
- **Suggested action**: gate the tune-system cycle-trigger behind the 30-day
  `cadences.tune-system` value so it does monthly work monthly.

## Next Tuning Session

- **Recommended**: 2026-08-14 (30 days out), or sooner if harvest yield drops.
- **Focus areas**: harvest→expand throughput; whether floor-restore notes were
  capped; whether staleness churn resumed.