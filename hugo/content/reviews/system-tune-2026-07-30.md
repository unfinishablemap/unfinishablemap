---
ai_contribution: 100
ai_generated_date: 2026-07-30
ai_modified: 2026-07-30 23:57:47+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-07-30
date: &id001 2026-07-30
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[todo]]'
- '[[changelog]]'
title: System Tuning Report - 2026-07-30
topics: []
---

# System Tuning Report

**Date**: 2026-07-30
**Sessions analyzed**: session_count 17911, cycle_position 12096 (cycle 504 closed this period)
**Period covered**: 2026-07-29T01:28Z → 2026-07-30T23:57Z (~46 hours)

## Executive Summary

Operationally the system is healthy: zero failures across the recorded window, zero critical issues, zero orphaned files, and the queue is holding its floor. The finding that matters is not an operational one — it is that **this skill has been structurally unable to perform its primary function since 2026-01-25**. All three of its licensed Tier-1 change types target keys (`cadences`, `overdue_thresholds`, replenishment weights) that do not exist in `evolution-state.yaml`. Zero Tier-1 changes were applied this run, and that is a consequence of the schema, not of caution.

A second theme runs through every category below: **several of the metrics this skill is instructed to reason from are dead.** `content_stats` reports 297 files against an actual 1356; `convergence_targets` still asks for 10 topics against 318 written; `quality.medium_issues` has read 10 across at least three consecutive reports. Nothing in `tools/` computes any of them.

## Metrics Overview

| Metric | Current | Previous | Trend |
|--------|---------|----------|-------|
| Session count | 17911 | 17652 | +259 |
| Recorded task outcomes | 20/20 success | 20/20 | → |
| Failure rate | 0% | 0% | → |
| Critical issues | 0 | 0 | → |
| Medium issues | 10 | 10 | → (target 3, **breached, unchanged ≥3 reports**) |
| Orphaned files | 0 | 0 | → |
| Queue depth (P0–P2) | 4 | 4 | → (floor is 3) |
| P3 depth | 29 | 14 | **+15, doubled** |
| Replenishment runs this period | 901, 902, 903 | 880–882 | all `zero-mint-single-promotion` |

Content: topics 318/320, concepts 317/320, voids **100/100 (capped)**, positions 11/80, apex 39, research notes 523, reviews 7017.

## Findings

### Cadence Analysis

**A1 — The cadence tuning surface does not exist. (Evidence: definitive, code + history.)**

`cadences` and `overdue_thresholds` are absent from `evolution-state.yaml`. They were removed on **2026-01-25** in commit `dd6ce48fa` ("feat(evolution): AI evolution work — deep reviews, condense, voids research"), which appears to be an incidental casualty of a content run rather than a deliberate schema change.

Three things have been inconsistent ever since:

- **`CLAUDE.md` still documents both** (lines 449, 452) as the place to register a new skill's cadence and overdue threshold.
- **Live code still reads both** — `tools/evolution/staleness.py` at lines 74, 129, 170 and 187, each with a hardcoded fallback: `state.cadences.get(skill_name, 168)` and `state.overdue_thresholds.get(skill_name, 72)`. `tools/evolution/state.py:172-173` defaults them to empty dicts.
- **Therefore every skill silently runs on the defaults** — 168h cadence, 72h overdue threshold — regardless of what it needs, and the per-skill tuning documented in CLAUDE.md is inert.

The consequence for this skill is direct: its Tier-1 table licenses exactly three change types — cadence adjustment, overdue threshold, replenishment weight. The first two target absent keys. The third has no target either: `replenishment_source_counts` exists but is a *counter* (`{'promotion_only': 1}`), not a weight, and there is no `replenishment_config`. **Tier 1 is empty by construction.**

**A2 — This skill runs ~11× more often than its own instructions permit. (Evidence: 78 reports.)**

SKILL.md lists *"Run more frequently than monthly"* under **DO NOT**, and the cadence comment says 30 days. `obsidian/reviews/` holds **78 `system-tune-*` reports dated 2026-01-08 to 2026-07-30** — about one every 2.7 days — of which **11 are from July alone**. The cause is registration: tune-system is a *cycle* trigger firing every 6 cycles, and 6 cycles is currently ~46 hours.

This is not merely noisy. The change-cooldown safeguard is *"2 tune-system sessions **OR** 60 days"*. At this cadence the two-session arm expires in under a week, so a guard designed to prevent oscillation over two months permits it within days. **Until the cadence is fixed, only the 60-day arm should be treated as binding.**

### Failure Pattern Analysis

**No finding — evidence threshold not met, and that is good news.** `failed_tasks` is empty; all 20 entries in `recent_tasks` record `outcome: success`, spanning 13 distinct task types (refine-draft ×6, agentic-social ×2, replenish-queue ×2, and one each of coalesce, deep-review, positions-evolve, harvest-research-subjects, check-model-fallback, embed-videos, check-links, research-voids, check-tenets, apex-evolve). The threshold is 3+ occurrences of a pattern; there are zero failures of any kind.

### Queue Health Analysis

**C1 — Replenishment is in a stable zero-mint steady state, correctly.** Runs 901, 902 and 903 all recorded `MINTED ZERO, FLOOR RESTORED` with mode `zero-mint-single-promotion`; `replenishment_source_counts` is `{'promotion_only': 1}`. With `topics/` at 318/320 and `concepts/` at 317/320, gap analysis exhausted, and harvest yielding nothing, **this is the system behaving correctly rather than failing to generate work.** No change recommended.

**C2 — The pipeline holds zero `research-topic` and zero `expand-topic` tasks**, across 35 active tasks (29 `refine-draft`, 3 `positions-evolve`, plus 3 minted today). Two independent causes are on record: ~86% of outer-review output is single-article audits (`subject_type: recent`) rather than coverage surveys, leaving ~14% harvestable; and optimistic reviews now correctly decline to nominate new articles because there is nowhere to put them. **New-article generation is closed by cap, not broken.** This bears on the operator's standing caps decision and is stated here for that purpose only.

**C3 — P3 depth doubled, 14 → 29, while P0–P2 held at 4.** Work is accumulating in the un-executed tier faster than promotion drains it. Not yet a problem — the floor mechanism is working — but if P3 keeps growing while promotion runs at one per replenishment, the backlog becomes permanent. Worth watching next run.

**C4 — `relocated_starved_p2` reads 0 while starvation was live for five cycles.** The counter exists in `queue_status` alongside `promoted_p3_to_p2`, but **no code in `tools/` or `scripts/` writes either** — they are set ad hoc by replenishment forks. A counter that does not increment during the exact phenomenon it names cannot be used as a health signal. See Tier 3 item 1.

### Review Finding Patterns

**D1 — The archive-propagation theme recurs in 29 reviews (threshold: 3).** A defect fixed on a live article does not reach its archived predecessor, which continues serving the old text at a preserved URL. This was not merely raised again today — it *produced* a fix: `archive/concepts/cognitive-closure.md`, the archived predecessor of [concepts/mysterianism.md](/concepts/mysterianism/), was found serving a **stronger** form of the same confirmation-bias inference the live article was being calibrated for. A `check-tenets` sweep the same day found three further loci existing **only** in `archive/`.

The pattern is well-attested and partially addressed by driver-side discipline (sweeping all three trees), but nothing structural propagates fixes backward. Recurring across 29 reviews without a systemic remedy is exactly what this category is meant to surface.

**D2 — Review-type distribution is heavily skewed toward `deep-review`.** Of the 300 most recent review files: deep-review 198, outer-review 31, pessimistic 24, optimistic 23, outer-review-synthesis 11, apex-evolve 6, tenet-check 5, system-tune 2. Deep-review is ~66% of all review output. This matches the cycle allocation (4 of 24 slots plus queue tasks) and is not obviously wrong, but the adversarial lenses — pessimistic and optimistic — together account for under 16%, and today's pessimistic-review output produced four confirmed defects in one article. Noted for the operator; no automatic change is licensed here.

### Convergence Progress

**E1 — `convergence_targets` are degenerate and no longer measure anything.** They ask for `min_topics: 10` against 318 written (31×), `min_concepts: 15` against 317 (21×), and `min_arguments: 5` against exactly 5 (met). Three of five targets were passed months ago by more than an order of magnitude.

The only live signal is `max_medium_issues: 3` against an actual **10** — breached, and **unchanged across at least three consecutive reports**, which means either nothing is resolving medium issues or nothing is recomputing the number.

**E2 — `content_stats` is frozen and wrong by 4.5×.** It reports `total_files: 297, published_files: 192` against an actual **1356** content files under `obsidian/`; `progress` separately sums to 751 written articles. `tools/evolution/state.py:246-249` only *serialises* `content_stats` — it round-trips whatever is already in the file. **No code computes it.** The same appears true of `quality.medium_issues`.

A skill instructed to "calculate convergence rate" and "identify stalled areas" from these fields is reasoning from numbers nothing maintains. This is the root of E1 and, arguably, of why every recent tune-system report shows `→` for most rows.

## Changes Applied (Tier 1)

*No changes applied.*

Not a judgement call: **all three licensed Tier-1 change types target settings that do not exist** (finding A1). `cadences` and `overdue_thresholds` have been absent since 2026-01-25; there is no replenishment weight setting. Recreating them is a schema restoration that would activate a dormant control surface for every skill at once — well outside the ±2-day magnitude limit in effect if not in letter — so it is routed to Tier 3 rather than applied.

The one prior Tier-1 change on record (2026-07-15, pruning `queue_status.last_floor_restore_note_*`) remains inside its 60-day cooldown and was not revisited.

## Recommendations (Tier 2)

### R1 — Refresh `convergence_targets` to values that can still be missed
- **Proposed change**: retire `min_topics`, `min_concepts`, `min_arguments` (all passed, two by >20×) and replace them with targets meaningful at current maturity — e.g. citation-verification coverage, share of articles with a `last_deep_review` inside 90 days, or archive-propagation closure. Keep `max_critical_issues: 0`; keep `max_medium_issues` but make it computed.
- **Rationale**: three of five targets cannot be missed, so convergence analysis is currently vacuous.
- **Risk**: Low — reporting only, no behavioural coupling.
- **To approve**: edit `convergence_targets` in `evolution-state.yaml`.

### R2 — Re-register tune-system as wall-clock monthly rather than a 6-cycle trigger
- **Proposed change**: move tune-system off the cycle-trigger table onto a wall-clock schedule, as `check-model-fallback`, `harvest-research-subjects` and `literature-drift-review` already are.
- **Rationale**: 78 runs since 2026-01-08 against a documented 30-day cadence, and the two-session cooldown arm is rendered meaningless (finding A2). Wall-clock also makes the cadence stable across `--interval` changes, which is precisely why the other three were moved.
- **Risk**: Low. **My read: yes, it should move.** A meta-review that fires every 46 hours cannot accumulate the 5-session evidence its own thresholds require, and re-deriving the same `→` rows every two days is the observable symptom.
- **To approve**: a registration change in `tools/evolution/cycle.py` / `time_trigger.py`.

## Items for Human Review (Tier 3)

### T1 — Queue starvation is structural: two minting skills disagree on insert position
- **Issue observed**: `/replenish-queue` **prepends** to `## Active Tasks`; `/pessimistic-review` **appends**. `select_queue_task` sorts `(priority, line_number)` (`tools/evolution/task_selector.py:158`), so every pessimistic-review task is born last in its priority tier and can only run when the queue is otherwise empty. Three P2s minted at 02:5xZ today sat at lines 1944–1966 on the day they were created while five consecutive replenishments promoted head tasks that took each queue slot; `recent_tasks` recorded zero executions of them.
- **Why human needed**: the fix is a code change in a selector or two skill files — outside this skill's mandate.
- **Suggested action**: make the two skills agree on insert position, or make the selector FIFO-within-priority. Note `tools/evolution/scoring.py:score_task` already implements priority + urgency scoring and the selector does not use it, which looks like the original design intent. **This is not cosmetic**: when the starved tasks finally ran they carried four real defects plus a fifth in an archived predecessor.

### T2 — `apex-evolve`'s staleness scorer is multiplicative and therefore degenerate
- **Issue observed**: Step 1 computes `score = days_since_baseline × changed_source_count`. Measured across all 38 apex articles: **37 score exactly 0**, and the single non-zero sits inside the 7-day no-op gate. A zero change-count annihilates unbounded staleness, so the stalest apex (`embodied-interface`, 38 days) was unreachable permanently rather than deprioritised. Worst for `apex_type: applied`, whose real dependency is the positions register, which the scorer does not read at all.
- **Why human needed**: skill-instruction change.
- **Suggested action**: fix the multiplication first — make staleness additive, or floor the multiplier at 1 — so age alone eventually surfaces anything. Only then add positions as an input, diffing at `Asserts`-field granularity; a whole-block or char-count diff gave a 57% false-positive rate this run, because the `Confidence:` → `Calibration:` schema migration grew every block without changing content.

### T3 — `research-voids` is a permanent no-op that still costs a full dispatch
- **Issue observed**: `voids/` is at 100/100 and the trigger is daily. The skill's only licensed output is a research note carrying `target_section: voids`, which at cap is actively harmful — it becomes an unconsumed-research signal that later prompts an `expand-topic` task aimed at a section that cannot accept the article. The cap check runs inside the agent, so every fire pays dispatch cost to produce a decline.
- **Why human needed**: dispatcher change.
- **Suggested action**: gate at dispatch on `voids_count < max_voids`. `/replenish-queue` already implements this pattern for expand-topic tasks targeting full sections.

### T4 — `cycle_post`'s state advance trails its own commit by one iteration
- **Issue observed**: commit `a4aa55a1` is labelled `auto(check-model-fallback)` but its payload is the *harvest* advance; the check-model-fallback timestamp remained uncommitted until the next `cycle_post` swept it up.
- **Why human needed**: commit-sequencing change in `cycle_post`.
- **Suggested action**: low severity — nothing is lost in a running loop. But an advance would be stranded if the loop stopped mid-lag, so it is worth recording.

### T5 — Restore or retire the cadence schema, and decide what owns the dead metrics
- **Issue observed**: findings A1, E1 and E2. `cadences` and `overdue_thresholds` are documented in CLAUDE.md and read by `staleness.py` but absent from state since 2026-01-25; `content_stats` and `quality.medium_issues` are serialised but never computed.
- **Why human needed**: restoring the keys silently changes scheduling for every skill simultaneously; deleting the CLAUDE.md section instead is an equally valid resolution. That is a design decision.
- **Suggested action**: pick one direction and make all three of CLAUDE.md, `state.py` and the state file agree. Either way, **give `content_stats` and `quality` a computing owner or remove them** — a metric nothing maintains is worse than a missing one, because it is reasoned from.

## Next Tuning Session

- **Recommended**: 2026-08-29 (30 days out), contingent on R2 — at the current 6-cycle registration the next run lands in ~46 hours.
- **Focus areas**: whether P3 depth continues to climb past 29 while P0–P2 holds at 4 (C3); whether `medium_issues` moves off 10 once something computes it (E1/E2); and whether T1 recurs — specifically whether any newly minted pessimistic-review task goes unexecuted for more than three replenishment cycles.