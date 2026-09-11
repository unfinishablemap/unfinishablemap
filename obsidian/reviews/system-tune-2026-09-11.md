---
title: "System Tuning Report - 2026-09-11"
created: 2026-09-11
modified: 2026-09-11
human_modified: null
ai_modified: 2026-09-11T02:34:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[todo]]"
  - "[[changelog]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-09-11
last_curated: null
---

# System Tuning Report

**Date**: 2026-09-11
**Sessions analyzed**: 20 `recent_tasks` entries (sessions to 20461), `cycle_position` 13392
**Period covered**: 2026-09-10 to 2026-09-11 (recent_tasks window); cadence analysis spans all 87 prior reports, 2026-01-08 to 2026-09-08

## Executive Summary

Eleventh consecutive zero-Tier-1 run, for the unchanged structural reason: the entire tunable
surface Step 6 acts on is absent from state. System health is clean — 10/10 recent tasks
successful, zero critical issues, no cap pressure in any section. **The value of this run is
subtractive**: it withdraws one Tier 2 recommendation and corrects one Tier 3 mechanism from
`reviews/system-tune-2026-09-08.md`, both of which rested on measurement errors, and records one
new finding with a mechanism rather than a lament — that a reports-only review's yield is
determined by its own closing priority list, not by its findings.

## Metrics Overview

| Metric | Current | Previous (09-08) | Trend |
|--------|---------|------------------|-------|
| `session_count` | 20461 | 20201 | +260 |
| Recent-task failure rate | 0/10 | 0/20 | → clean |
| `quality.critical_issues` | 0 | 0 | → |
| `quality.medium_issues` | 10 (target 3) | 10 | → breached |
| `quality.low_issues` / orphans | 3 / 0 | 3 / 0 | → |
| Queue P0–P2 | 10 (was 8 in state) | 4 | ↑ |
| Queue P3 | 91 | 113 | ↓ |
| Tier 1 changes applied | 0 | 0 | → 11th consecutive |
| Sections at cap | 0 of 4 | 0 of 4 | → |

`progress`: topics 328, concepts 326, voids 103, positions 18, apex 42, arguments 5, research
notes 582, reviews 7507.

## Findings

### Cadence Analysis

**This run should not have fired, for the eleventh time.** `tune-system` last ran
2026-09-08T01:20:47Z — **73.2 hours ago** — against a documented **720-hour** minimum. The gate is
inert under `/unfin-cycle` and the reason is unchanged (Tier 3 below).

The evidence base is now much larger than prior runs stated. Across **87 reports and 86
consecutive gaps** spanning 2026-01-08 to 2026-09-08, the **maximum gap ever recorded is 11 days**
and the number of gaps reaching 30 days is **zero**. The last fourteen gaps are 1, 2, 1, 8, 3, 1,
3, 1, 5, 9, 3, 6, 9, 4 days — mean 4.0. A 30-day cadence has never once been honoured.

**NEW — one `last_runs` key is an orphan of the replaced orchestrator, and it manufactures false
staleness.** `last_runs["add-highlight-tweet"]` reads 2026-08-20T08:12:31Z, **522.4 hours (21.8
days) stale**, which in a naive cadence audit looks like a broken daily trigger. It is not.
`check_add_highlight_tweet` (`tools/evolution/time_trigger.py:127`) emits
`TriggerDecision(skill="add-highlight", args="--tweet")`, so the `/loop` path records the run under
`add-highlight` (last run 1.0 h ago) and never under the hyphenated name. The only writer of the
`-tweet` key is `scripts/evolve_loop.py:870`, the orchestrator `/loop` replaces. The trigger itself
is correctly gated and idempotent — it keys on `state.last_tweet_date`, which reads **2026-09-10**,
so a tweet did go out yesterday and the 02:33 hour is correctly below `TWEET_HOUR_UTC`.

This is the **same root cause as the standing min-age Tier 3 item**: state that only the replaced
orchestrator maintains. Severity is low — nothing reads the key — but any future cadence audit will
trip over it, as this one nearly did.

`validate-all` has not run since 2026-01-24 (230 days). It remains reachable
(`tools/evolution/task_selector.py:223`) and is listed in the staleness tables at
`tools/evolution/staleness.py:109` and `:159`. **This run did not determine why it is never
selected** and does not speculate; its stated function overlaps `check-links` and
`scripts/validate.py` in the build pipeline. Recorded for a human glance, not as a finding.

Three `*-chrome-unavailable-at` markers are present and all stale (July–August), so no current
Chrome outage. `tweet-highlight` at 5508 h is correct — `CLAUDE.md` marks it DEPRECATED.
`integrate-orphan` at 2038 h is correct with `orphaned_files: 0`.

### Failure Pattern Analysis

Nothing to report, and the absence is the result. Last 10 `recent_tasks`: **10/10
`outcome: success`**. `failed_tasks` is an empty dict. No environmental errors, no read errors
during analysis.

⚠️ **Method note carried forward, because it is the specific way this category produces a false
abort.** The `recent_tasks` entry keys are `task` / `type` / `date` / `outcome` / `kind`. A query
using `skill` / `status` returns `None` for every field, which reads as **100% failure** and would
falsely trip the >50% abort condition.

### Queue Health Analysis

**Correction to this run's own first pass, recorded because it is the category's recurring failure
mode.** An initial check keyed on top-level `evolution-state.yaml` keys and reported
`replenishment_source_counts` absent. It is **present**, nested at
`queue_status.replenishment_source_counts`, fully populated. Category C does have data. A
recursive walk of the whole document, matching leaf key names at any depth, is the reliable test —
the same walk confirms the four Tier-1 keys are absent everywhere, not merely at top level.

Last replenishment (run 1032, 2026-09-09T04:23Z, mode `promotion-only`): **zero minted, six
promoted from P3**. Every non-promotion source reads zero — `chain`, `gap_analysis`,
`unconsumed_research`, `staleness`, `orphan_integration`, `length_analysis`, `check_tenets`,
`defect_family`, `optimistic_review`, `outer_review_synthesis`, `review_spillover`, and all three
`positions_*` sources. `promotion_from_p3: 6`.

The shape is unchanged and correctly diagnosed by prior runs: the queue is short of
**loop-visible** work, not of work. `loop_pickable_open: 6` against 91 open P3. `task_chains`
holds `pending_articles: 0` and `pending_cross_reviews: 0`.

### Review Finding Patterns

**NEW, and the strongest item in this report: a reports-only review's yield is its closing
priority list, not its findings.**

`check-tenets` has no task-minting step — correct for a reports-only skill — so a finding enters
the queue only if a driver or human reads the report and mints. `reviews/tenet-check-2026-09-08.md`
reported **13 warning families** and closed with a section naming **four** in priority order.

| | outcome within two days |
|---|---|
| the 4 families **on** the closing priority list | **4 of 4** fixed and ✓-marked in `todo.md` |
| the 8 families **off** it | **0 of 8** — re-verified still verbatim, at zero line drift, on 2026-09-11 |

A fifth family landed because it already held an open P2. **No family lacking either a queue task
or a place on the closing list was fixed.** Items 5–13 of a 13-family report are, empirically,
invisible.

The mechanism is confirmed at line granularity, which is what raises this above correlation.
Commit `2cc1cf5585` (2026-09-10 14:10Z) rewrote `topics/completeness-in-physics-under-dualism`
**L98** — the exact line carrying two of the unactioned loci — changing only `Process 1` to
`Process 3`, and carried both over-concessions through verbatim, because that task keyed on a
different string. **Being edited is not being reviewed.** The unit of review is the locus table of
whichever task is running, and a defect absent from that table is structurally unreachable however
often its file is touched.

Resolution rate for this series is otherwise healthy once a finding is queued: five of five queued
Tenet families were closed inside 33 hours (2026-09-09 and 2026-09-10), which is the fastest
actioning this series has seen.

### Convergence Progress

No regression; no stall requiring action. `quality.critical_issues` 0 meets its target of 0.
`min_topics` 10, `min_concepts` 15 and `min_arguments` 5 are all met many times over (328 / 326 /
5). `max_medium_issues` remains breached at **10 against a target of 3**, unchanged since at least
2026-09-04 — already carried as a Tier 2 recommendation by the 09-08 report and not re-argued here.

No section is under cap pressure. Gate figures from
`tools.evolution.state.count_section_files`: topics **328**/360, concepts **326**/360, voids
**103**/115, positions **18**/80; apex 42 (uncapped). ⚠️ A bare `ls obsidian/<section>/*.md`
returns **+1 on every section** (329/327/104/19/43) because it counts an editor-internal sidecar —
use the state module.

## Changes Applied (Tier 1)

*No changes applied* — and for the eleventh consecutive run this is the correct output, not a
shortfall.

A recursive walk of the entire `evolution-state.yaml` document, matching leaf key names at any
depth, returns **truly absent** for all four settings Step 6 is defined over: `cadences`,
`overdue_thresholds`, `locked_settings`, `replenishment_config`. The document's top-level keys are
exactly `agentic_social, audit_triple, content_stats, convergence_targets, cycle_position,
failed_tasks, last_git_push, last_runs, last_tweet_date, last_updated, progress, quality,
queue_status, recent_tasks, section_caps, session_count, task_chains, tune_system_history`.

`tune_system_history.changes_applied` holds **one** entry in the project's history, dated
2026-07-15. Creating the four missing keys in order to have something to tune would be a schema
change dressed as a cadence adjustment, and is declined again.

`locked_settings` does not exist, so no setting is human-locked.

## Withdrawals and corrections to the 2026-09-08 report

This section exists because a meta-review that cannot retract its own recommendations accumulates
error at the same rate it accumulates findings.

### WITHDRAWN — Tier 2 #1, "Allocate the last 12 voids slots deliberately, and stand `research-voids` down"

The recommendation rested on a measurement that **selects on the dependent variable**. It paired
each research note with an article of the **same slug**, a join that can only find notes which
became their own article; a note **absorbed into a differently-named host that already existed** is
invisible to it by construction. The reported "median lag 0 days, no article ever written from a
note older than 69 days" therefore describes only the sub-population that was never at risk.

Measured by pairing notes with the articles that **cite** them:

| | as reported 09-08 | corrected |
|---|---|---|
| pairs | 67 (same-slug) | **32** (citation) |
| negative lag — host predates note | 0, impossible by construction | **20 of 32** |
| maximum lag | 69 d | **83 d** |
| banked subjects | 33 | **24** |

**Absorption into a pre-existing host, at zero cap cost, is the dominant mode** — and the corpus
states the discipline explicitly. `obsidian/voids/voids.md` L257 records Absorbed and Folded as
"outcomes of the absorption-over-proliferation discipline, not gaps awaiting their own article."
So "all 33 become permanently unwritable" misreads the design as a defect, and the
12-slots-versus-33 arithmetic compares a queue against a population that was never queued.

The bank figure was also high. Careful alias resolution gives 41 subjects with no article under any
form, of which **17 are cited by live content** under semantic renames no slug matcher can see —
`voids-translation-void-2026-05-09` seeded `topics/consciousness-and-the-phenomenology-of-translation`.
That leaves **24** genuinely banked, 22 of them more than 150 days old.

Replaced by the Tier 2 recommendation below.

### CORRECTED — Tier 3, "`agentic-social`'s selector cannot reach never-posted articles"

The observation stands; the stated **mechanism does not**. The 09-08 report attributed it to the
topic-overlap filter penalising well-integrated articles (survivors averaging 2.2 topics against
3.2 for never-posted articles). That correlation is real but is not the cause: the 7-day URL dedup
window makes never-posted articles only **3.3%** of the pool, so the expected count of never-posted
articles among 8 survivors is **0.27**. Observing zero is the unremarkable result of a small
sample. **The window, not the filter, is the lever.** Driver ranking remains the only effective
dedup.

## Recommendations (Tier 2)

### Triage the 24 banked voids subjects — the aged bank is untriaged, not locked out

- **Proposed change**: assign an Absorbed / Folded / Surveyed disposition to each of the 24 banked
  subjects in the Research-Stage Voids register in `obsidian/voids/voids.md`. Do **not** stand
  `research-voids` down, and do **not** raise `max_voids`.
- **Rationale**: the register is the corpus's only triage ledger. It carries **19** entries against
  **41** subjects lacking a standalone article, and **zero of the 24** appear in it. Voids sits at
  103/115, so the cap gate does not fire and there is nothing to relieve. The binding constraint is
  disposition, not throughput or supply.
- **Risk**: Low. Nothing is deleted and nothing is minted; the ledger is brought level with the
  bank.
- **To approve**: operator decision — the register is a published page and its dispositions are
  editorial. Note `obsidian/voids/voids.md` L269 already nominates one subject as a candidate for a
  remaining slot and flags it as an operator decision.

### Make the driver's mint of a reports-only review's top findings an explicit expectation

- **Proposed change**: after any reports-only review (`check-tenets`, `pessimistic-review`,
  `optimistic-review`), the driver mints the top **2–3** items from the report's closing priority
  list, and the report re-carries the remainder by name and line in its successor.
- **Rationale**: measured 4-of-4 actioned on-list against 0-of-8 off-list. The list, not the
  finding, is the actioning mechanism, and 4 is a size the queue demonstrably consumes while 13 is
  not. Minting all seven survivors into a queue holding 91 P3 would bury them.
- **Risk**: Low, and bounded by the cap of 2–3.
- **To approve**: no code change; this run already applied it once — two P2 `refine-draft` tasks
  were minted from `reviews/tenet-check-2026-09-11.md`, with the remaining five families named in
  the second task's note.

## Items for Human Review (Tier 3)

### The min-age trigger gate is inert under `/loop` — eleventh recorded instance

- **Issue observed**: `TRIGGER_MIN_AGE_HOURS` (`tools/evolution/cycle.py:78`) holds one entry,
  `"tune-system": 30 * 24` = 720 h. `filter_triggers_by_min_age`
  (`tools/evolution/cycle.py:85`) is called from exactly one site,
  `scripts/evolve_loop.py:1370` — the orchestrator `/loop` replaces. The `/loop` path enqueues at
  `tools/evolution/cycle_post.py:429` with no filter and drains `pending[0]` at
  `tools/evolution/cycle_pick.py:188`. This run fired at 73.2 h against 720 h.
- **Why human needed**: code change. Every `TRIGGER_MIN_AGE_HOURS` entry is currently dead, so the
  gate will silently fail for anything added later, not only `tune-system`.
- **Suggested action**: call `filter_triggers_by_min_age` from the `/loop` drain path, or move the
  gate into `get_cycle_triggers`.

### `last_runs["add-highlight-tweet"]` is an orphan key of the replaced orchestrator

- **Issue observed**: written only by `scripts/evolve_loop.py:870`; the `/loop` path records the run
  under `add-highlight` instead (`tools/evolution/time_trigger.py:134`). Reads 21.8 days stale
  while the trigger is in fact healthy and fired yesterday (`last_tweet_date: 2026-09-10`).
- **Why human needed**: deleting a state key is a schema change, and `cycle_post.py:374` still
  accepts the name in a tuple.
- **Suggested action**: drop the key, or have `cycle_post` alias it so cadence audits stop reading a
  false 3-week outage. Low severity — nothing consumes it.

### Cap reports-only priority lists, and require the remainder be re-carried

- **Issue observed**: a 13-family report yielded 4 fixes, all of them the 4 on its closing list.
- **Why human needed**: skill-instruction change, which `tune-system` must not make.
- **Suggested action**: amend the reports-only SKILL.md files to cap the closing list at ~4 and to
  require the unactioned remainder be re-listed by name and line in the next run's report.

### Carried unchanged from prior runs

- **`CLAUDE.md`'s section-caps table still reads 320/320/100/80** against real caps of
  **360/360/115/80**, and its `Current` column is months stale. A queued task has previously copied
  the stale figure into its own justification.
- **`content_stats` is stale**: `total_files: 297` against **822** files in the five content
  sections alone.
- **`cycle_dates_to_synthesize()`** (`tools/reviews/synthesis.py`) reads only the live
  `pending-reviews.yaml`, so a weekly rotation can permanently destroy a cross-reviewer synthesis.
- **Under `/unfin-cycle` nothing enforces the 4-hour abandon cutoff** for a stalled outer-review
  leg; `find_abandoned` and `mark_abandoned` are called only from `scripts/evolve_loop.py`. The
  driver is the only actor who can clear a stuck leg.

## Next Tuning Session

- **Recommended**: 2026-10-11 (30 days). In practice the inert gate will fire it within ~3–9 days;
  the twelfth consecutive zero-Tier-1 run carries no information and should be written as three
  lines plus whatever is genuinely new.
- **Focus areas**: whether the two P2 tasks minted from the 09-11 tenet report were consumed, and
  whether the five remaining families moved — that is the direct test of this run's Category D
  finding. Whether the voids register gained dispositions. Whether `max_medium_issues` was revised
  or the 10 medium issues assigned owners.

## Method note

Every figure in this report was measured this run rather than carried from the previous one, and
two of the previous run's figures did not survive that. The recursive whole-document key walk, the
citation-pairing of research notes, and the `### `-block classification of `todo.md` coverage are
the three tests that produced the corrections; a top-level key check, a same-slug join, and a
filename grep are the three that produced the errors they replaced. All file references are
backticked rather than linked: the report body contains **zero** wikilinks, because reviews are
synced and one unresolvable wikilink in a synced file makes the pre-push sync skip the push for the
whole repository.
