---
title: "System Tuning Report - 2026-08-03"
created: 2026-08-03
modified: 2026-08-03
human_modified: null
ai_modified: 2026-08-03T20:10:46+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[todo]]"
  - "[[changelog]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-08-03
last_curated: null
---

# System Tuning Report

**Date**: 2026-08-03
**Sessions analyzed**: session_count 18382, cycle_position 12384 (cycle 516 completed this run)
**Period covered**: 2026-08-02T08:42Z (previous tune-system run) to 2026-08-03T20:10:46+00:00

## Executive Summary

Operational health is good and the tuning mechanism is not. Zero task failures across the
full 20-entry `recent_tasks` window, zero critical issues, zero orphans. But this is the
**fourth consecutive run that applied zero Tier-1 changes, and the fourth that could not have
applied any** — the settings this skill is designed to adjust do not exist in
`evolution-state.yaml`. Separately, this run fired **35.4 hours** after the previous one against
a **720-hour** gate that is correctly configured and simply never consulted on this code path.
Both findings are Tier 3 and both are now well past their evidence thresholds.

## Metrics Overview

| Metric | Current | Previous | Trend |
|--------|---------|----------|-------|
| Failure rate (recent_tasks, n=20) | 0% | 0% | → |
| Critical issues | 0 | 0 | → |
| Medium issues | 10 | — | over target (max 3) |
| Low issues | 3 | — | — |
| Orphaned files | 0 | 0 | → |
| Queue P0/P1/P2/P3 | 0 / 0 / 5 / 21 | — | P2 at floor+2 by promotion |
| Replenishment sources yielding | 0 of 8 | 0 of 8 | → exhausted |
| Tier-1 changes applied | 0 | 0 | → 4th consecutive |
| Interval since last tune-system | 35.4 h | ~57 h | under a 720 h gate |

## Findings

### Cadence Analysis

**FINDING C1 (Tier 3, carried and now confirmed a fourth time): the per-skill min-age gate is
inoperative on the `/unfin-cycle` path.**

Verified in code this run:

- `TRIGGER_MIN_AGE_HOURS` in `tools/evolution/cycle.py:67` correctly sets `"tune-system": 30 * 24`
  (720 h), with a comment recording that without it the skill "was running daily (9 reports in
  9 days, each declining to apply Tier-1 changes)".
- `filter_triggers_by_min_age` (`cycle.py:74`) implements the gate correctly.
- `grep -rn filter_triggers_by_min_age scripts/ tools/` returns exactly **one** call site:
  `scripts/evolve_loop.py:1370`.
- `cycle_post` enqueues cycle-completion triggers **without** calling it — this run's
  `cycle_post` printed `enqueued cycle triggers: [... 'tune-system']` with the previous run
  35.4 h old.
- `cycle_pick.py:143-146` drains the pending list unconditionally
  (`if pending: _emit_invoke("trigger", pending[0]); return 0`) — no age check.

So the gate is bypassed at both enqueue and drain. Measured age at fire time: **35.4 h against a
720 h gate**. Evidence is now five reports in nine days (07-26, 07-29, 07-30, 08-02, 2026-08-03)
against a documented monthly cadence — well past the 5-session threshold.

**Not fixable by this skill**: the remedy is a code change in `cycle_post`/`cycle_pick`, and the
skill is explicitly barred from modifying loop tooling.

### Failure Pattern Analysis

**No finding.** `failed_tasks` is empty and all 20 `recent_tasks` entries carry
`outcome: success`, spanning refine-draft (5), deep-review (2), agentic-social (2), and one each
of coalesce, harvest-research-subjects, research-topic, check-model-fallback, replenish-queue,
condense, embed-videos, check-links, research-voids, check-tenets, apex-evolve. The 3-occurrence
threshold is not met in any category. This is a genuine clean result, not an absence of data.

### Queue Health Analysis

**FINDING Q1 (Tier 2): all eight replenishment sources are yielding zero, and the floor is being
held by promotion rather than generation.**

`replenishment_source_counts` reads `chain: 0, unconsumed_research: 0, gap_analysis: 0,
length_analysis: 0, staleness: 0, orphan_integration: 0, positions_register_gap: 0,
applied_apex_gap: 0`. The last two replenish runs (926, 927) both recorded
`last_replenishment_mode: zero-mint-triple-promotion` and restored the floor by promoting three
verified P3s each time.

This is not stagnation — run 926's three promotions all executed and drained within about two
hours — but it means a cycle slot is consumed roughly every six hours by a replenish that mints
nothing. The queue is **mis-sorted, not empty**: 21 P3 against 5 P2, and the floor counts only
P0-P2.

**Recommendation (Tier 2, not applied)**: count P3 tasks toward a pickable floor, or lower
`MIN_QUEUE` while the P3 pool is deep. Both are behavioural changes beyond this skill's
magnitude limits, and the underlying constraint is real — `topics/` 318/320, `concepts/` 317/320,
`voids/` 100/100 — so generative sources are cap-blocked rather than broken.

### Review Finding Patterns

**FINDING R1 (Tier 3, 4 instances this period — threshold met): convergence is tracked per
article, but defects are per lens.**

Four independent instances in a single day, each caught by a lens no prior pass had run:

1. `topics/the-enteric-nervous-system-...` — two prior deep-reviews cleared it; both verified
   citation **metadata only**. A verbatim-span check found defects in **both** external quoted
   spans, including a misquote absent from the cited book.
2. `concepts/psychophysical-laws` — three deep-reviews (05-31, 06-20, 07-17) passed over a
   framework misattribution, because a ledger checking author/year/venue finds nothing wrong
   with a real, correctly-described Chalmers-McQueen paper.
3. `concepts/pragmatism` — a 06-25 deep-review recorded an inference as "correctly framed as the
   Map's move"; it was a bare conditional attributed to van Fraassen. That review made zero
   enhancements on "already-stable, well-calibrated" grounds.
4. `check-tenets` Family S — a lens keyed on the `^tenet-3-standing` imperative had **never been
   run**; zero prior `tenet-check-*.md` files contain the strings it audits. It found two Map
   pages giving opposite verdicts on the same datum.

**Implication for tuning**: a staleness or convergence metric counting *reviews* over-states
coverage, because it cannot distinguish a file reviewed four times through one lens from a file
reviewed once through four. The same shape appeared in scheduling this period — the apex
staleness scorer's top two candidates were both non-actionable, one already reconciled by a
targeted refine that neither `apex_last_synthesis` nor `last_deep_review` records.

**Not actionable at Tier 1**: no existing weight or threshold expresses lens coverage.

### Convergence Progress

Content: topics 318, concepts 317, voids 100, positions 14, apex 39, research notes 529,
reviews 7110. Three of four sections are at or within three articles of cap, so convergence is
now bounded by cap policy rather than by generation rate.

Against `convergence_targets`: `max_critical_issues: 0` — **met** (0). `max_medium_issues: 3` —
**not met** (10). `min_topics: 10`, `min_concepts: 15`, `min_arguments: 5` — all met many times
over; these floors were set for a young corpus and no longer discriminate.

**No Tier 1 action**: `convergence_targets` adjustments are explicitly Tier 2, and the medium-issue
overage is better addressed by working the 10 issues than by moving the target.

## Changes Applied (Tier 1)

*No changes applied.* **And none were possible.** See T1 below — this is the fourth consecutive
run in that position.

## Recommendations (Tier 2)

### Count P3 tasks toward the pickable floor
- **Proposed change**: have the floor check count P3, or reduce `MIN_QUEUE` while `p3_tasks > 15`.
- **Rationale**: two consecutive replenish runs consumed a cycle slot to mint nothing, restoring
  the floor by promoting P3s that were already pickable in every sense except the counter's.
- **Risk**: Low. Promotion is already the de-facto mechanism; this removes the ceremony.
- **To approve**: adjust the floor logic in the replenish path.

### Retire or re-scope the stale convergence floors
- **Proposed change**: `min_topics`/`min_concepts`/`min_arguments` are 10/15/5 against actual
  318/317/5. Either raise them to something discriminating or drop them.
- **Rationale**: they always read "met" and so contribute nothing to convergence assessment.
- **Risk**: Low — reporting only.

## Items for Human Review (Tier 3)

### T1 — The Tier-1 mechanism is structurally dead
- **Issue observed**: this skill's entire Tier-1 apparatus adjusts `cadences`,
  `overdue_thresholds` and `locked_settings`. **None of these keys exists in
  `evolution-state.yaml`.** Present top-level keys are: `agentic_social`, `audit_triple`,
  `content_stats`, `convergence_targets`, `cycle_position`, `failed_tasks`, `last_git_push`,
  `last_runs`, `last_tweet_date`, `last_updated`, `progress`, `quality`, `queue_status`,
  `recent_tasks`, `section_caps`, `session_count`, `tune_system_history`. They have been absent
  since commit `dd6ce48fa`.
- **Why human needed**: either the keys should be restored (and the skill resumes tuning them),
  or the skill's Tier-1 section should be rewritten to target settings that exist — for example
  `section_caps`, `convergence_targets`, or the replenishment floor. Both are edits to
  loop tooling or skill definitions, which this skill must not make.
- **Suggested action**: decide which of the two, then apply. Until then every tune-system run is
  a report generator, which is useful but should be named as such rather than presented as
  "0 changes applied" — that phrasing implies none were warranted.

### T2 — The min-age gate never runs on this path
- **Issue observed**: see Finding C1. Correctly configured at 720 h, called only from
  `scripts/evolve_loop.py:1370`, and the `/unfin-cycle` path reaches neither enqueue-time nor
  drain-time filtering. Fired this run at 35.4 h.
- **Why human needed**: the fix is a code change in `cycle_post` (filter before enqueue) or
  `cycle_pick` (filter before drain). Filtering at **enqueue** is preferable — a gated skill
  should not sit in the pending list consuming a slot's worth of attention on each drain.
- **Suggested action**: call `filter_triggers_by_min_age` in the `cycle_post` enqueue path and
  log gated skills, mirroring `evolve_loop.py:1370`.
- **Note**: this compounds T1 — a skill that cannot act, running twenty times more often than
  designed, produces a report every day or two whose main content is that it could not act.

## Next Tuning Session

- **Recommended**: 2026-09-02 (30 days), *if* T2 is fixed. Absent that fix the trigger will fire
  again within days regardless of what is written here.
- **Focus areas**: whether T1 was resolved and in which direction; whether the P3 floor change
  landed and what it did to replenish frequency; whether medium_issues moved off 10; and whether
  any lens-coverage metric was introduced in response to R1.
