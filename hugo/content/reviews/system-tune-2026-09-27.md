---
ai_contribution: 100
ai_generated_date: 2026-09-27
ai_modified: 2026-09-27 06:36:28+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-09-27
date: &id001 2026-09-27
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-27 06:36:28+00:00
modified: *id001
related_articles:
- '[[todo]]'
- '[[changelog]]'
title: System Tuning Report - 2026-09-27
topics: []
---

# System Tuning Report

**Date**: 2026-09-27
**Sessions analysed**: session_count 21464, cycle_position 13968. The previous run (2026-09-24) was at session 21204 and cycle_position 13824.
**Period covered**: 2026-09-24T00:00 to 2026-09-27T06:36 UTC

## Executive Summary

No abort condition was met and no Tier 1 change was applied, for the fifteenth consecutive run. The cause has not changed: `evolution-state.yaml` still has no `cadences`, `overdue_thresholds`, `locked_settings` or replenishment-weight fields. A grep for those keys finds them only inside earlier tune-system notes. This run fired 3.3 days after the last one, so the monthly min-age gate is still not enforced on the `/unfin-cycle` path (T2 below). Since 09-24 there is one improvement: hand-minting from tenet-check priority lists now works (minted rows get fixed; unminted rows still do not). Two things have got worse. The Gemini outer-review leg failed in 3 of the last 4 cycles, and the coalesce no-op streak went from 15 to 21.

## Abort conditions: none met

| Condition | Measured | Status |
|---|---|---|
| >50% of last 10 tasks failed | Last 10 in `recent_tasks`: 1 failed (`commission-gemini-review`, 09-27). Last 20: 1 failed. | pass |
| `quality.critical_issues > 0` | 0 | pass |
| File read errors | none | pass |
| Convergence regressed 3+ sessions | Article counts are flat or rising in every section (table below) | pass |

**Locked settings**: `locked_settings` is absent, so nothing is locked. There is also nothing to tune.

## Metrics Overview

| Metric | Current (09-27) | Previous (09-24) | Trend |
|--------|---------|----------|-------|
| session_count | 21464 | 21204 | +260 |
| Recent-task failure rate (last 20) | 1/20 (5%) | 1/20 (5%) | → (different task: Gemini commission, not Moltbook) |
| `failed_tasks` | {} | {} | → |
| Changelog `Status: Failed` entries | 0 | 0 | → |
| topics / cap (`count_section_files`) | 332 / 360 | 329 / 360 | +3 |
| concepts / cap | 331 / 360 | 327 / 360 | +4 |
| voids / cap | 103 / 115 | 103 / 115 | → |
| positions / cap | 23 / 80 | 22 / 80 | +1 |
| apex | 44 | 44 | → |
| Queue, live `parse_tasks` (P1 / P2 pending / P2 blocked / P3 pending) | 4 / 1 / 8 / 21 | 0 / 6 / 7 / 27 (HEAD before 09-24) | P1s arrive from outer-review convergence |
| `queue_status` block (stale since 09-09) | 8 P2 / 88 P3 | same | not refreshed |
| NEEDS-HUMAN open / ever closed | 75 / 1 | 75 / 1 | → |
| `quality.medium_issues` (target 3) | 10 | 10 | → |
| Outer-review legs collected, last 4 cycles (09-24 to 09-27) | ChatGPT 4/4, Claude 4/4, Gemini 1/4 | n/a | ↓ Gemini |

## Findings

### Cadence Analysis (2 findings)

- **There is still no cadence configuration.** Carried from 09-19 and 09-24 (T1). Scheduling is hard-coded in `tools/evolution/cycle.py` and `time_trigger.py`.
- **tune-system still over-fires.** Runs so far: 09-19, 09-24 and now 09-27, 3.3 days apart. `TRIGGER_MIN_AGE_HOURS["tune-system"] = 720` exists at `tools/evolution/cycle.py:78`, but `filter_triggers_by_min_age()` is called only from `scripts/evolve_loop.py:1370`. I grep-verified that no other call site exists and that `tools/` and `scripts/` have had no commit since 09-24. This run adds no new information on cadence. Carried as T2.
- Carried unchanged, not recounted as new findings: `add-highlight-tweet` last ran 2026-08-20 (38 days ago), and `validate-all` last ran 2026-01-24.

### Failure Pattern Analysis (3 findings)

- **Gemini outer-review leg: 3 failures in 4 cycles.** This meets the 3-occurrence threshold. In `pending-reviews.yaml`, the 09-24 and 09-25 Gemini entries are `abandoned` and both have `failure_reason: None`. On 09-26 the leg was collected. On 09-27 it has no entry, and `recent_tasks` shows `commission-gemini-review` as `failed`. The operator reports that the research plan never rendered. As a result, `/combine-outer-reviews` has been running on 2 of 3 reviewers for most of the week. The fix is in the skill's UI handling or in Gemini's current DOM, so it is Tier 3. The empty `failure_reason` on abandoned entries also removes the diagnostic trail (T4).
- **Chrome skill UI drift across all three services (reported by the operator; not verified in the DOM by this run).** ChatGPT no longer has `#prompt-textarea`, and replies now render in `[class*="MarkdownRoot"]`. The skills' literal checks therefore report false "logged out" or "not sent" results. The operator measured the screenshot scale at 0.665 on all three legs today. The memory note `screenshot-scale-is-1-0-skills-hardcode-a-wrong-constant` says 1.0, so the scale is display-dependent, not a constant. Claude's project selector now shows "Opus 5.5" rather than Fable 5 / Opus 4.8; the 09-24 to 09-27 files are named `claude-opus-5-5`, which is consistent with this. In addition, the Chrome extension typically connects about 15 s after launch, and one collect fork bailed with `CHROME_UNAVAILABLE` before that and succeeded when dispatched again. Together these are more than 3 occurrences of one class of problem: skill instructions encoding UI or timing constants that have drifted. Tier 3 (T3).
- **Refine-draft forks skipping `sync.py`** (reported by the operator). A spot check found no obsidian file edited since 09-26 in topics/concepts/voids/apex/positions whose hugo copy is older, because the parent synced. The pattern is already recorded in memory (`fork-sync-omission-pattern-verify-hugo-every-report`). Tier 3 (T5).
- No new agentic-social failure: both `agentic-social` runs today succeeded. `failed_tasks` is empty.

### Queue Health Analysis (2 findings)

- **The queue is flowing, fed by outer reviews rather than by replenish.** `replenish-queue` has not run since 2026-09-09 (18 days). The live parse shows 5 executable P1 or P2 tasks, and all 4 P1s come from the outer-review convergence path. Eight P2s are blocked. `queue_status` (8/88) still reports the 09-09 snapshot. Blocked P2s probably still count toward the replenish floor (T6 in this report; T3 in the 09-24 report), but the loop is not starved, because outer-review and hand-minted tasks keep the P1/P2 tier above zero. This is lower priority than it was on 09-24.
- **Coalesce: 21 consecutive reasoned abandons** (changelog 09-27T01:20), up from 15 on 09-24. The coalesce run itself describes this as "the expected steady-state outcome". Its pool grows only through the 7-day age floor, and each new crosser has so far been declined on a role split. Coalesce still takes 2 of every 24 cycle slots. Tier 2 R1 is renewed.

### Review Finding Patterns (2 findings)

- **Minting is the deciding factor, and the evidence now covers 4 reviews.** Tenet-check 139 (09-25) found that all 4 of check 138's hand-minted priority rows were fixed within hours, while none of the 18 unminted WARNING loci moved. Tenet-check 140 (09-27) found check 139's minted priorities 1–3 repaired, and unminted priority 4 (`concepts/dualism` L172/L154) untouched, now on its second report. The earlier data points are 09-17 and 09-23. The operator is hand-minting, which works. R2 (have the driver mint automatically) is renewed.
- **Partial repairs leave siblings live.** Check 140 records that refine and sweep commits fix the flagged sentence and leave same-claim siblings in the same file: the causal-closure dilution at L120/L196, `kabbalah-tzimtzum` L78 after the ae32dee539 sweep, and `phenomenal-depth` L86 surviving a deep review. Its recommendation is that refine briefs name the *claim* and have the executor grep for siblings. This changes skill instructions, so it is Tier 3 (T7).

### Convergence Progress (1 finding)

- Topics went up by 3, concepts by 4 and positions by 1 in 3.3 days. `expand-topic` ran on 09-25, 09-26 and 09-27, so the article-creation stall from 09-19 is resolved. Voids stays at 103/115, with 6 voids research notes waiting in `task_chains.pending_articles`, the newest `voids-causal-impression-void-2026-09-27`. The pipeline is accumulating notes faster than it writes voids articles. There is only one data point so far, which is below the 5-session evidence threshold, so this is a watch item only. `quality.medium_issues` is still 10 against a target of 3, and no tool writes this field (carried).

## Changes Applied (Tier 1)

*No changes applied.* None of the three Tier 1 change types has a setting to act on:

- cadence ±2 days: no `cadences` key exists
- overdue threshold ±2 days: no `overdue_thresholds` key exists
- replenishment weight ±20: no weight key exists; `replenishment_source_counts` is a counter, not a weight

Creating those sections would be a design decision, not a tuning adjustment. Cooldowns were not involved. The only Tier 1 change on record is still the 2026-07-15 `queue_status` prune.

## Recommendations (Tier 2)

### R1. Reassign coalesce's 2 cycle slots (renewed, third report)
- **Proposed change**: in `tools/evolution/cycle.py`, move coalesce's 2/24 slots to deep-review or to queue. The alternative is to keep one slot, gated on a cheap precheck that tests whether any article crossed the age floor since the last run.
- **Rationale**: 21 consecutive declines. The runs from 09-25 onward state outright that there was "no pool movement", which makes them nearly zero-information runs.
- **Risk**: Low. The change is reversible if section pressure passes about 95%.
- **To approve**: edit the slot table in `cycle.py` and update the 24-slot list in CLAUDE.md.

### R2. Driver-side minting from reports-only priority lists (renewed, evidence now 4 reviews)
- **Proposed change**: after check-tenets, pessimistic-review and optimistic-review, have the cycle driver mint one `refine-draft` per priority row, capped at about 4.
- **Rationale**: minted rows were fixed 4/4 (check 138) and 3/3 (check 139). Unminted rows were fixed 0/18 and 0/1.
- **Risk**: Low.
- **To approve**: add a post-step to `/unfin-cycle` handling, or keep hand-minting. Check 140's priority list and `concepts/dualism` L172/L154 are waiting now.

### R3. Refresh the CLAUDE.md section-cap table (renewed)
- **Proposed change**: caps 360/360/115/80. Current counts 332/331/103/23. The `count_section_files` path is `tools/evolution/state.py:347`, and its signature is `count_section_files(section)`.
- **Risk**: Low. This is documentation only.

No P3 tasks were added to todo.md. The queue is fed by outer reviews, and hand-minting covers the priority lists.

## Items for Human Review (Tier 3)

### T1. Create `cadences` / `overdue_thresholds`, or rewrite tune-system to match reality (carried, third report)
This is the root cause of 15 consecutive no-change runs.

### T2. Enforce the tune-system min-age gate on the `/unfin-cycle` path (carried)
Call `filter_triggers_by_min_age()` from the cycle_pick/cycle_post path as well as from `evolve_loop.py:1370`. Runs are currently 3–5 days apart against a 30-day intent.

### T3. Chrome skill UI and timing drift (new)
- **Issue observed**: ChatGPT selectors are stale (`#prompt-textarea` is gone and replies render in `MarkdownRoot`), which produces false logged-out or not-sent bails. The screenshot scale is 0.665, not a constant. The Claude model label is now "Opus 5.5". Gemini's research plan does not render. The extension connects about 15 s after launch, while forks give up on their first check.
- **Why human needed**: the fix means editing six commission/collect SKILL.md files.
- **Suggested action**: rely on semantic checks (role or aria selectors, and result state) instead of literal IDs. Measure the scale at run time rather than hard-coding it. Poll for the extension for about 30 s before declaring `CHROME_UNAVAILABLE`. Accept any "Opus" label as the fallback.

### T4. Gemini leg failing 3 of 4 cycles, with empty `failure_reason` (new)
- **Suggested action**: investigate the Gemini Deep Research plan stage manually. Make `mark_abandoned` require a non-empty reason so that the next tune run can classify the failures.

### T5. Refine-draft forks skipping `sync.py` (new, operator-reported)
- **Suggested action**: have the cycle driver always run `scripts/sync.py` after a content-modifying fork instead of relying on the fork. The alternative is to add a hard final step to the refine-draft skill.

### T6. `count_p0_p2_tasks` counts blocked tasks (carried as the 09-24 T3; lower urgency now)
Replenish has been idle for 18 days, but the loop is not starving because outer reviews feed it.

### T7. Refine briefs should name the claim, not the sentence (new; from tenet-check 140)
Partial repairs leave same-claim siblings live in the same file. This requires a change to the refine-draft and deep-review instructions.

### Also carried
X API 402 (`add-highlight-tweet` last ran 08-20). NEEDS-HUMAN backlog at 75 open with 1 ever closed. `quality.medium_issues` is 10 against a target of 3, and no tool writes it.

## Next Tuning Session

- **Recommended**: 2026-10-27 (30 days out). If T2 is not fixed, the next run will fire within days and should record only what changed.
- **Focus areas**: Gemini leg recovery (T3/T4); whether R1 is applied; whether check 140's priority 4 was minted and repaired; growth in voids `pending_articles`; whether `cadences` was created.