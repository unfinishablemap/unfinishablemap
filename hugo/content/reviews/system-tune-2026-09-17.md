---
ai_contribution: 100
ai_generated_date: 2026-09-17
ai_modified: 2026-09-17 01:44:19+00:00
ai_system: claude-fable-5-1
author: null
concepts: []
created: 2026-09-17
date: &id001 2026-09-17
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-17 01:44:19+00:00
modified: *id001
related_articles:
- '[[todo]]'
- '[[changelog]]'
title: System Tuning Report - 2026-09-17
topics: []
---

# System Tuning Report

**Date**: 2026-09-17
**Sessions analyzed**: 20 `recent_tasks` entries (sessions to 20721, `cycle_position` 13536); 120 changelog entries 2026-09-14 to 2026-09-17; 37 loop iterations of the live 15-minute `/loop` session from 2026-09-16 15:00 UTC
**Period covered**: 2026-09-11 (previous tune) to 2026-09-17; the cadence series spans all 86 prior reports, 2026-01-08 to 2026-09-11

## Executive Summary

Twelfth consecutive zero-Tier-1 run, for the unchanged structural reason: the entire surface Step 6
may act on — `cadences`, `overdue_thresholds`, `locked_settings`, replenishment weights — is absent
from `evolution-state.yaml` at every depth (recursive key walk, this run). Health is clean: 20/20
recent tasks succeeded, `failed_tasks` is empty, the last 146 changelog entries carry zero
`Failed` statuses, `critical_issues` is 0, and no section is at cap (topics 328/360, concepts
326/360, voids 103/115, positions 21/80, measured with `count_section_files`). The one finding that
matters is a queue-gate mechanism, new this run and about to bite: `count_p0_p2_tasks`
(`tools/evolution/task_selector.py:57`) counts **blocked** P2 tasks, so the four human-blocked P2s
plus the single pickable P2 read as 5 against a floor of 3. When the loop consumes that one
pickable P2, replenish will not fire and every queue slot (16 of 24) will emit a `queue_empty`
idle until a human clears a blocked P2 or mints. The 09-11 Category D finding — a reports-only
review's yield is its closing priority list — was tested this cycle and held for a third time.

## Metrics Overview

| Metric | Current | Previous (09-11) | Trend |
|--------|---------|------------------|-------|
| `session_count` | 20721 | 20461 | +260 (6 days, ~43/day) |
| Recent-task failure rate | 0/20 | 0/10 | → clean |
| Changelog `Failed` statuses (146 entries) | 0 | 0 | → |
| `quality.critical_issues` | 0 | 0 | → |
| `quality.medium_issues` | 10 (target 3) | 10 | → breached, no writer in code |
| `quality.low_issues` / orphans | 3 / 0 | 3 / 0 | → |
| Queue P0–P2 as `count_p0_p2_tasks` reads it | 5 | 10 | ↓ |
| Queue P0–P2 actually pickable (`Status: pending`) | **1** | 8 | ↓↓ |
| Queue P3 (pending / blocked) | 77 / 4 | 91 | ↓ |
| Loop throughput, 09-16 | 76 posts in 96 ticks | — | fork-bound at 15 min |
| Tier 1 changes applied | 0 | 0 | → 12th consecutive |
| Sections at cap | 0 of 4 | 0 of 4 | → |

`progress`: topics 328, concepts 326, voids 103, positions 21, apex 43, arguments 5, research notes
599, reviews 7568. `content_stats.total_files` still reads 297 (stale; carried).

## Findings

### Cadence Analysis

**The min-age gate is inert for the twelfth time.** `tune-system` last ran 2026-09-11T02:38Z, 143
hours ago, against the 720-hour minimum in `TRIGGER_MIN_AGE_HOURS` (`tools/evolution/cycle.py:78`).
`filter_triggers_by_min_age` is still called from exactly one site, `scripts/evolve_loop.py:1370`,
which `/loop` does not use. Across **86 reports and 85 consecutive gaps** the maximum gap is 11 days
and no gap has reached 30; the last sixteen are 2, 1, 2, 1, 8, 3, 1, 3, 1, 5, 9, 3, 6, 9, 4, 3
(mean 3.8). Carried as Tier 3; no state setting controls it.

**Fork-bound, not cadence-bound — measured.** In the live session from 2026-09-16 15:00 UTC the
loop landed 37 posts in 41 fifteen-minute ticks (4 lost). Gap-before-post by skill: `research-topic`
n=6, 16–60 min, mean 28; `research-voids` 25; `pessimistic-review` 23; `deep-review` 8–22;
`refine-draft` 9–20 (mean 13.6); `agentic-social` 12–17. Only 1 of 36 inter-post gaps reached 30
minutes. The whole of 09-16 produced 76 posts in 96 ticks. The driver's observation (research forks
8–46 min, check-tenets 16) is consistent with these figures. This is the expected steady state at a
15-minute interval and needs no change; the interval is a driver argument, not a state setting.

**`last_runs` staleness audit** (all others are within a day): `validate-all` 236 days (reachable
at `task_selector.py:223`, never fires under `/loop`; carried); `integrate-orphan` 91 days (orphans
read 0, so correct); `add-highlight-tweet` 28 days — the orphan key of the replaced orchestrator
recorded 09-11, still present, still a false-staleness trap (`add-highlight` itself ran 09-16
08:04); `expand-topic` 10 days (see Queue Health); `replenish-queue` 8 days (see Queue Health);
`skip-queue-slot` 54 days.

Evidence threshold (5 sessions) met for every series above; no cadence setting exists to adjust.

### Failure Pattern Analysis

No failures: `failed_tasks: {}`, 20/20 `recent_tasks` success, 0 of 146 changelog entries with a
`Failed` or `Error` status. The 3-occurrence threshold is not met for any task type.

One sub-threshold pattern is recorded for the count. `agentic-social`'s built-in challenge solver
(`solve_challenge`, `.claude/skills/agentic-social/scripts/agentic_social_api.py:117`) produced a
ghost post on 2026-09-16 by answering subtraction to a "loses N … what is the total" prompt; the
same shape burned a post on 2026-09-05 22:32. That is **2 of the same shape**, below the threshold
of 3, inside a wider record of 5 lost posts since 2026-08-22 across four shapes (08-22 ×2, 09-05,
09-08, 09-16) against 9 recorded solves plus the routine silent successes (12 posts landed on
09-16 alone). The prompt at lines 87–99 tells the solver both that "total" means add and that
"loses" means subtract, then asks for `UNCERTAIN` on operator ambiguity — the two rules collide on
exactly this template. Fix is a code/prompt change: Tier 3 below.

### Queue Health Analysis

**Blocked P2s hold the replenish floor closed — new, with mechanism.** Live parse of `todo.md`: 86
active blocks; P2: 1 pending (L1851, minted by the driver from the 09-17 tenet check) + 4 blocked
(L61, L82, L201, L1557 — all `NEEDS-HUMAN`, dated 08-24 to 09-14); P3: 77 pending + 4 blocked.
`cycle_pick` (`tools/evolution/cycle_pick.py:265`) fires replenish when `count_p0_p2_tasks < 3`.
That function (`tools/evolution/task_selector.py:57–83`) filters on priority and wall-clock-only
types but **not on status**, so it returns **5** while the number the loop can actually pick is
**1**. Consequence: the next queue slot consumes L1851; from then on every queue slot emits
`_emit_idle("queue_empty")` (`cycle_pick.py:277`) and replenish never fires, because 4 ≥ 3. On
2026-09-09 (run 1032) only two P2s were blocked, the count read 2, and replenish fired — that is
why it has not fired since: two further P2s were blocked on 09-14, not because the queue was
healthy. Since 09-09 the floor has been held by hand: 8 `mint` commits (3 outer-review, 2
research-topic, 1 check-tenets, 2 driver `task(mint)`), zero replenish runs.

The evidence threshold (5 sessions) is met by the 09-09 note plus this run's live parse and the
git record; the fix is a one-line status filter in Python, which this skill must not make — Tier 3.
The short-term operator lever is to resolve one of the four blocked P2s (or hand-mint), and that is
also the pre-condition for the loop to reach replenish's promotion-only mode, which on 09-09 lifted
six P3s and all were consumed.

**Research → article conversion this month.** 38 research notes carry a 2026-09 date; 31 are cited
by no live article, and only 8 of those 31 are named in any open task. `expand-topic` last ran
2026-09-07 while `research-topic` ran 8 times in the last 60 changelog entries (6 of them since
09-16 15:00). The research forks now mint downstream `refine-draft` tasks (two on 09-16) rather
than `expand-topic`, and the one BUILD verdict of the session (Cotard, 0 live articles, concepts
326/360) minted nothing. Pending `expand-topic` tasks number 6, all P3, none pickable. With 32/34
open slots in topics/concepts this is a chain design choice rather than cap pressure; recorded as
Tier 2 for the operator, not actioned.

`replenishment_source_counts` for the last run: `promotion_from_p3: 6`, every generative source 0 —
consistent with the 09-09 note. `task_chains.pending_articles` holds 2 voids entries (taboo,
categorical-perception) and nothing consumes it (the 09-08 finding stands).

### Review Finding Patterns

**Category D confirmed a third time (threshold 3 met).** The 09-11 report predicted that only a
reports-only review's closing list gets actioned. Since then: the two P2 tasks minted from
`tenet-check-2026-09-11` were both consumed (archive `completed-tasks-2026-W37.md` L127, L131);
`tenet-check-2026-09-14` had its single "if only one thing" item (Family A) closed in 36 minutes by
`5c89e615c4` and its Part 3 standalone minted as P3 (todo L1734), while items 2–5 and the re-carried
tail are verified unmoved at the same lines in both trees on 09-17; `tenet-check-2026-09-17` kept
its list at four and the driver minted the top three as tasks at 01:09 UTC (`58ae8f4473`). Three
consecutive reports, same shape. The 09-11 Tier 2 ("driver mints the top 2–3") is therefore
operating in practice without a skill change; the Tier 3 to encode it in the reports-only SKILL.md
files is carried.

**Positions register has no adversarial lens.** `pessimistic-2026-09-16-individuation-and-subjecthood`
records that its subject had zero reviews of any type, and the coverage numbers bear it out:
filename-subject deep/pessimistic/optimistic reviews cover 327/327 topics, 326/326 concepts, 42/43
apex, 102/103 voids, but **7/21 positions (33%)**; 14 register files have never been the named
subject of an adversarial review, and two (`perception-and-the-interface`,
`value-in-selection-calibration-history-p-vs2`) are mentioned by no review at all. The cause is
`find_review_candidates` in `tools/curate/deep_review.py:210`, whose default
`content_types` is `["topics", "concepts", "tenets", "arguments"]`. Per instruction the pool is
**not** widened here; recorded as Tier 3, and one P3 `positions-evolve` audit task is minted for the
unmentioned register file (Tier 2).

**Voids research bank: 30 unconsumed notes, untriaged.** `research-voids` on 09-17 listed 29
banked notes and added a 30th (`voids-dormancy-void`); a crude stem/citation join this run gives 36
as an upper bound. The Research-Stage Voids register in `obsidian/voids/voids.md` still carries 19
entries, unchanged since 09-11 (`git log` empty), and none of the five September notes
(perceptual-history 09-09, prevalence 09-10, taboo 09-14, categorical-perception 09-15, dormancy
09-17) appears in it. Voids sits at 103/115 so no cap relief is needed; the 09-11 correction stands
(absorption is the design, not a defect). One scoped P3 task is minted to register the five
September notes (Tier 2); the older 24 remain an operator triage.

### Convergence Progress

`convergence_targets` are met on every count-based target (topics 328 ≥ 10, concepts 326 ≥ 15,
arguments 5 ≥ 5, critical 0 ≤ 0) and breached on `max_medium_issues` (10 vs 3) as in every run
since the field was set; nothing in `tools/` writes `quality.medium_issues`, so the figure is a
manual ledger that no process moves. Section counts moved topics 328 → 328, concepts 326 → 326,
voids 103 → 103, positions 18 → 21 since 09-11 (positions +3 = the only structural growth). No
stalled area in the sense of the template; the corpus is in the improve-not-expand regime by
design. Threshold (5 sessions) met; no target adjustment proposed.

## Changes Applied (Tier 1)

*No changes applied* — twelfth consecutive run. The tunable surface (`cadences`,
`overdue_thresholds`, `locked_settings`, replenishment weights) does not exist in
`evolution-state.yaml` at any depth, so no setting is available to adjust within the contract. No
`locked_settings` block exists; nothing is under cooldown (`tune_system_history.changes_applied`
holds one 2026-07-15 entry, a state prune, not a cadence).

## Recommendations (Tier 2)

### Audit the one positions-register file no review has ever touched
- **Proposed change**: minted this run as a P3 `positions-evolve` audit task on
  `obsidian/positions/perception-and-the-interface.md` (end of Active Tasks).
- **Rationale**: 0 filename-subject reviews and 0 mentions in 7,568 review files; the 09-16
  pessimistic pass on a sibling register file found two P2 defects on first adversarial read.
- **Risk**: Low; audit mode edits calibration notes only.
- **To approve**: promote or leave for replenish's promotion pass.

### Register the five September banked voids notes
- **Proposed change**: minted this run as a P3 `refine-draft` on `obsidian/voids/voids.md` — add
  the five 2026-09 notes to the Research-Stage Voids register with a disposition (default
  *Surveyed*, as the Suggestion and Notation voids are) and correct the "Nineteen" count.
- **Rationale**: the register is the only triage ledger and has not moved since 09-11; the older 24
  remain an operator call (09-11 Tier 2, carried), but the five newest are mechanical.
- **Risk**: Low; no note is deleted, no article minted.
- **To approve**: promote, or fold into the next `research-voids` run.

### Clear one blocked P2 so replenish can fire
- **Proposed change**: operator resolves any one of the four `NEEDS-HUMAN` P2s at todo L61, L82,
  L201, L1557 (decide, demote, or complete). Priority changes are outside this skill's remit.
- **Rationale**: see Queue Health — with 4 blocked P2s the gate reads 5 ≥ 3 and replenish cannot
  fire once L1851 is consumed; the loop then idles on 16 of 24 slots.
- **Risk**: Low. The durable fix is Tier 3 below.

### Decide whether research notes should mint `expand-topic` again
- **Proposed change**: operator decision on the research → expand chain: 31 of 38 September notes
  are uncited by any live article, 6 `expand-topic` P3s are queued, `expand-topic` last ran 09-07,
  and the newest BUILD verdict minted nothing. Either accept refine-only consumption as the policy
  at 328/360 and 326/360, or let `harvest`/`research-topic` mint one `expand-topic` per BUILD
  verdict.
- **Rationale**: the caps were raised 320 → 360 on 2026-06-20 for exactly this pipeline; the slots
  are not being used.
- **Risk**: Medium — new articles carry the create-defect tail; hence not minted here.

## Items for Human Review (Tier 3)

### `count_p0_p2_tasks` counts blocked tasks, so blocked P2s hold the replenish gate closed
- **Issue observed**: `tools/evolution/task_selector.py:57–83` filters on `priority <= 2` and
  wall-clock-only types only; `Status: blocked` P2s are counted. Live value 5 (1 pickable + 4
  blocked) versus `MIN_QUEUE_TASKS = 3` (`cycle_pick.py:65`). The 09-09 replenish note computed
  "executable P0–P2 = 0" by a different rule, so the skill and the gate disagree.
- **Why human needed**: Python change.
- **Suggested action**: add `and t.status == TaskStatus.PENDING` (or exclude `blocked_by`) to the
  comprehension, mirroring `select_queue_task(executable_only=True)`.

### The deep-review pool excludes `apex/`, `voids/` and `positions/`
- **Issue observed**: `tools/curate/deep_review.py:210` default `content_types` omits three
  sections; positions coverage is 7/21 by filename against 100% for topics and concepts. Not widened
  by this run, per instruction.
- **Why human needed**: widening changes the 4-slot deep-review mix and the missing
  `last_deep_review` scores highest, so all ~167 excluded files would flood the top of the ranking.
- **Suggested action**: either add `positions` alone (21 files, smallest blast radius) or route
  register files to `positions-evolve` audit mode on a cadence.

### `agentic-social` solver: the "loses … total" template
- **Issue observed**: 2 same-shape ghost posts (09-05, 09-16); 5 lost posts in 26 days across four
  shapes. Prompt lines 87–99 of `agentic_social_api.py` give contradictory rules for this template.
- **Why human needed**: prompt/code change; below the 3-occurrence threshold for the shape.
- **Suggested action**: make the "N and another loses M … total" shape return `UNCERTAIN` (the
  hand-verify path) or fix the precedence: result-noun governs, verb only in its absence.

### The min-age trigger gate is inert under `/loop` — twelfth recorded instance
- **Issue observed**: fired at 143 h against 720 h; `filter_triggers_by_min_age` is called only
  from `scripts/evolve_loop.py:1370`.
- **Suggested action**: unchanged from 09-11 — call the filter from the `/loop` drain path.

### Carried unchanged from prior runs
- `last_runs["add-highlight-tweet"]` is an orphan key (28 days stale; `add-highlight` is healthy).
- `CLAUDE.md`'s section-caps table reads 320/320/100/80 against real caps 360/360/115/80 and live
  counts 328/326/103/21.
- `content_stats.total_files: 297` against ~820 live articles in the five content sections.
- `quality.medium_issues` (10 vs target 3) has no writer in `tools/`; assign owners or revise.
- `cycle_dates_to_synthesize()` reads only the live `pending-reviews.yaml`; a rotation can lose a
  synthesis.
- Nothing enforces the outer-review 4-hour abandon cutoff under `/unfin-cycle`.
- `validate-all` 236 days stale; the reports-only priority-list cap belongs in SKILL.md files.
- The older 24 banked voids notes remain an operator triage; do not raise `max_voids` for them.

## Next Tuning Session

- **Recommended**: 2026-10-17 (30 days). The inert gate will fire it within ~3–9 days; that run
  should be short unless the queue gate above has bitten.
- **Focus areas**: whether replenish fired at all after L1851 was consumed (the direct test of the
  `count_p0_p2_tasks` finding); whether either P3 minted here was promoted or consumed; whether
  the three tenet-check mints of 09-17 were consumed and the four off-list families moved;
  whether the voids register gained the five September entries.

## Method note

Every figure was measured this run: recursive key walk of `evolution-state.yaml`;
`count_section_files` for caps; `parse_tasks` and `count_p0_p2_tasks` on the live `todo.md`;
inter-post gaps from `../unfinishablemap_log/evolve_loop.log*` (the log records post times, not
pick times, so durations are upper bounds); filename-subject matching restricted to
`deep-review-`, `pessimistic-`, `optimistic-` prefixes (an earlier pass that admitted `apex-evolve-`
files read 43/43 and was discarded). The report body contains zero wikilinks; file references are
backticked.