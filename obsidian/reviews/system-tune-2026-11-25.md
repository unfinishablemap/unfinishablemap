---
title: "System Tuning Report - 2026-11-25"
created: 2026-11-25
modified: 2026-11-25
human_modified: null
ai_modified: 2026-11-25T16:27:11+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[todo]]"
  - "[[changelog]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-25
last_curated: null
---

# System Tuning Report

**Date**: 2026-11-25
**Sessions analyzed**: 263 (session_count 25028 to 25291; cycle_position 15984 to 16128, which is six full cycles)
**Period covered**: 2026-11-18T20:50Z (previous run) to 2026-11-25T16:20Z. The loop was idle from 2026-11-20T14:14Z to 2026-11-24T00:21Z, about 82 hours with no commits and no loop log files for 11-21 to 11-23, so the window holds about 81 hours of operation.

## Executive Summary

The loop is healthy by every measure it records. All 169 changelog entries in the window succeeded or were reasoned declines, failed_tasks is empty, and 11 of 12 outer-review legs were collected. No setting was changed, for the thirtieth consecutive run: the three change types this skill may apply (cadence, overdue threshold, replenishment weight) still have no keys in `evolution-state.yaml`.

Three findings are new this run, and all three were checked in code or in git history:

- **Changelog archiving.** 954 changelog entries carry a bare-time heading (`## 16:02 - apex-evolve`). `parse_changelog_date` returns `None` for that form, so `archive_changelog` keeps those entries in `changelog.md` permanently. 870 of them date from 2026-08-02 to 2026-11-08 and make up 2.62 MB of the 2.87 MB file. The size problem in the open NEEDS-HUMAN task about the changelog comes from this.
- **Quality block.** No code writes `quality.critical_issues` or `quality.medium_issues`. `medium_issues` has read 10 at every commit since at least 2026-01-21, so the critical-issues abort condition can never fire, and the "medium 10 against a target of 3" that earlier reports watched is a frozen number, not a measurement.
- **Monthly gate.** The 30-day gate for this skill exists only on the `evolve_loop.py` path. `cycle_post.py` L449 enqueues cycle triggers without it. That is why this "monthly" skill has run 11 times since 2026-10-10.

The open queue grew from 430 to 523 tasks (+93) over four active days. The 33 tasks blocked on human decisions are unchanged, and none of the 11-18 report's Tier 2 or Tier 3 items has been acted on.

## Status of the 2026-11-18 report's items

No commit since 2026-11-18T20:50Z touches `.claude/skills/`, `tools/`, `scripts/`, `hugo/config.toml` or `hugo/layouts/`. The only human-authored commits in the window are the four automated add-highlight commits. Every item below is therefore still open unless a line says otherwise.

| 11-18 item | Status 2026-11-25 | Evidence |
|---|---|---|
| T2: queue condense tasks for over-gate pages | **Open, worse** | 73 pages at or over the hard gate in topics/concepts/voids/apex (26/15/23/9), against 70 on 11-18; positions adds 10 more. The only condense task is a NEEDS-HUMAN one on `voids/assent-void`, and `last_runs.condense` is still 2026-11-18T10:21Z. |
| T2: exclude section indexes from the length gate | **Open, half of it was a false alarm** | `get_length_warnings` already skips `voids/voids.md` (its rule is `name == f"{section}.md"`). Only `apex/apex-articles.md` (14,128 words) is wrongly measured. |
| T2: run this skill monthly | **Open, cause found** | See Cadence Analysis: the gate is in `tools/evolution/cycle.py` but `cycle_post.py` never calls it. |
| T3 (a) deep review's default lens | **Open as a skill question; mostly adopted in practice** | All 23 deep reviews since 11-19 carry a §2.4 citation-ledger section (two are titled "Quotation Ledger"). I did not re-measure the 11-18 definition (quotations checked against the full text). |
| T3 (b) closing tasks without running them | **Dormant** | Not re-measured. It is a convention, and no new instance was reported. |
| T3 (c) register bands for P-RR1/P-RR2 | **Open** | `positions/replies-to-rivals.md` still has `human_modified: null`. |
| T3 (d) the tenet check's default lens | **Open** | Checks 169 (11-20) and 170 (11-25) found 7 and 10 warnings. See Review Finding Patterns. |
| T3 (e) queue order within a priority | **Open, new evidence** | See Queue Health: five voids expand tasks from 11-01 to 11-06 sit behind 82 pending P3s while voids has had one free slot since at least 11-18. |
| T3 (f) human decisions outstanding | **Open, unchanged** | Still 33 blocked tasks (P1 2, P2 14, P3 17). The oldest is 84 days old (2026-09-02). |
| T3 (g) pages over their length gate | **Open** | Same item as the first Tier 2 row. |
| T3 (h) outer reviewers that did not read the page | **Open, recurring** | Four of four cycles: on 11-19 Gemini ("This website is inaccessible"); on 11-20 both Claude and Gemini could not fetch `voids/plenitude-void`; on 11-24 Claude could not fetch the apex index; on 11-25 Claude could not fetch the tenets page or six dependencies. |
| T3 (i) social-post selection | **Open** | Merged with driver item 1 below. |

## Metrics Overview

| Metric | Current | Previous (11-18) | Trend |
|--------|---------|------------------|-------|
| Session count | 25,291 | 25,028 | +263 |
| Commits in window | 276 (about 3.4 per hour of operation) | n/a | n/a |
| Failure rate | 0% (169 changelog entries: 160 success, 4 abandoned, 3 complete, 2 warnings; recent_tasks 20/20) | 0% | → |
| Convergence | not measurable (see Convergence Progress) | not measurable | → |
| Queue depth (P0-P2) | 22 (P1 2 blocked; P2 14 blocked, 6 pending) | 20 | ↑ |
| Open tasks | 523 (482 P3 pending) | 430 | +93 |
| Blocked on a human | 33 | 33 | → |
| Pages at or over the hard gate (topics, concepts, voids, apex) | 73 | 70 | ↑ |
| Sections (`count_section_files`) | topics 370/370, concepts 370/370, voids 124/125, positions 29/90, apex 44 | same | → |
| Research notes | 795 (state); 246 `voids-*` | 772 | +23 |
| reviews_completed | 8,531 | 8,475 | +56 |
| Outer-review legs collected | 11 of 12 (11-24 Gemini abandoned) | 9 of 9 | → |
| `changelog.md` size | 2,870,244 bytes | n/a (1.47 MB on 2026-10-15) | ↑ |

## Abort conditions

None met. The last ten recorded tasks include no failure. `quality.critical_issues` is 0, but that field has no writer (see Convergence), so this condition is untestable and was not a real check this run. No file failed to read. Convergence regression cannot be assessed.

## Locked settings

None. `evolution-state.yaml` has no `locked_settings` key. Every grep hit for the name is inside the prose of `tune_system_history`.

## Findings

### Cadence Analysis

**No Tier 1 lever.** The state file still has no `cadences`, `overdue_thresholds` or weight keys. `tools/evolution/staleness.py` reads `state.cadences` with a 168-hour default, so the code would honour such keys, but none exist to adjust.

**This skill's own cadence (evidence threshold met: 11 data points).** Runs on 10-10, 10-14, 10-20, 10-23, 10-26, 10-31, 11-03, 11-09, 11-12, 11-15, 11-18 and 11-25 were 3 to 7 days apart, with a mean of about 4.6 days. None came close to 30. The cause, checked in code:

- `tools/evolution/cycle.py` defines `TRIGGER_MIN_AGE_HOURS = {"tune-system": 30 * 24}` and `filter_triggers_by_min_age()`.
- Only `scripts/evolve_loop.py` L1370 calls that filter.
- The `/loop` path enqueues triggers in `tools/evolution/cycle_post.py` L449 (`triggers = get_cycle_triggers(cycles_completed)`) and writes them to `.unfin/pending-triggers.json` unfiltered. Today the file held `["tune-system"]` at cycle 672 (672 mod 6 = 0).

The 2026-08-02 report made the same point ("enforced only at scripts/evolve_loop.py:1370"). Nobody has acted on it in four months. See Tier 2.

The 82-hour idle period (11-20 14:14Z to 11-24 00:21Z) left no failed or orphaned task. I read it as the operator not driving the loop. It is not read as overdue cadence.

### Failure Pattern Analysis

Below threshold: there are no failures. Two near-misses were caught by the driver (items 4 and 7 under Tier 3). The 11-24 Gemini leg was abandoned after its research stalled at the first stage, which is the third distinct Gemini hang shape on record (10-28, 11-10, 11-24). That is three occurrences of Gemini legs failing to finish, but each failed a different way and the driver handled each one correctly, so there is nothing to tune.

### Queue Health Analysis

- **Growth.** 523 open tasks against 430 a week ago. 112 open tasks carry a Generated date of 11-19 or later (28 on 11-19, 17 on 11-20, 38 on 11-24, 29 on 11-25). The loop executed about 79 refine-drafts, 24 deep reviews and 21 research-topics in the same time, so net growth was +93, about 23 tasks per active day.
- **Age.** Of 481 dated pending tasks, only 4 are more than 30 days old, so the old tail is small. Topics and concepts are full and nearly all new work is refine-draft (448 of 488 pending).
- **Voids slot.** voids has stood at 124/125 since at least 11-18. Five ordinary voids expand-topic tasks (amodal, noseeum, substitution, compartment, geometry; minted 11-01 to 11-06) plus one NEEDS-HUMAN (contingency) compete for the one slot. They sit at todo L2557 to L4024 with 82 pending P3s above the first of them. Under the picker's top-first order within a priority (11-18 item (e)), none has been reached; `last_runs.expand-topic` is 2026-11-17. Meanwhile research-voids ran three more times in the window. This supports driver item 2.
- **Capped-section expand.** `topics/diachronic-harm-and-the-momentary-locus` (todo L2772) is a pending expand task for a section at 370/370. Its own Notes say to measure first and block, so it guards itself, but it will still cost a slot when picked.
- **Replenishment.** `queue_status` has not been updated since replenish run 1034 on 2026-09-29. Its p2/p3 counts (13/7) are stale and the gate is never reached, because the queue never falls below the floor.

### Review Finding Patterns

Threshold met (three or more reviews) for two patterns.

1. **Repairs leave their sibling sentences behind.** Tenet check 169 (11-20): 4 of 7 warnings are "sentences the window's calibration edits left above grade on pages they otherwise repaired". Tenet check 170 (11-25): 4 of 10 are "sentences left above grade beside sibling sentences the window re-graded", and all seven 11-20 warnings were still live. The optimistic wing reviews show the same thing at page level: 11-24 anomalous-evidence ("three sibling-drift repairs"), 11-25 comparative-cognition ("the hub page lags three repairs its neighbours made"), and 11-19 intrinsic-nature ("three pages overstate in their closing or framing sentences"). The 11-15 report made this Tier 2 #1 (brief tenet-check tasks to cover the paragraph and its siblings). The pattern has continued. Carried forward.
2. **Outer reviewers cannot fetch the pages they audit.** This happened in four of four cycles (detail in the status table, item (h)). Two reviews said the public changelog is "at least five weeks behind" or asked to "restore a live changelog". Both are consistent with a page too large to fetch whole (2.98 MB of source in `hugo/content/`), which the archiving defect under Convergence Progress keeps growing.

A positive pattern: all 23 deep reviews since 11-19 carry a citation ledger, so the §2.4 step that `deep-review/SKILL.md` mandates is now routine.

### Convergence Progress

Insufficient evidence for a rate. The content counts are flat because the sections are at their caps (no new article since 11-17), and only research notes (+23) and reviews (+56) move. Two measurement defects matter more than the rate:

- **The quality block has no writer.** `grep` over `tools/`, `scripts/` and `.claude/` finds `critical_issues` and `medium_issues` read in `tools/evolution/state.py` (serialisation, and a penalty at L472-473) and assigned nowhere. `git log -G'medium_issues:'` shows every change since 2026-03-11 rewriting the same value, 10. The convergence targets (`max_medium_issues: 3`) and this skill's `critical_issues > 0` abort condition therefore test a constant. Reports from 10-10 to 11-03 read "medium 10 against target 3" as a quantity parked in NEEDS-HUMAN entries. That reading was unfounded.
- **Changelog entries with bare-time headings are never archived.** `tools/archive/workflow.parse_changelog_date` returns `None` for `## 16:02 - apex-evolve` and a date for `## 2026-11-18 20:50 UTC - tune-system`. Tested on all three heading forms this run. `archive_changelog` keeps undated sections unconditionally. Result: `changelog.md` holds 954 undated entries, 84 from 11-24 to 11-25 and 870 from 2026-08-02 to 2026-11-08, and none from 11-09 to 11-23 (those used dated headings and were archived, and the loop was idle from 11-20 to 11-24). The file grew from 1,559,615 bytes (10-15) to 2,870,244 now. 16 SKILL.md files template the heading as a bare time, this skill's included. This entry uses a dated heading so it will archive.

## Changes Applied (Tier 1)

*No changes applied.* The three permitted change types have no keys in the state file. No setting is locked and no cooldown applies. `tune_system_history` was updated: a no-change entry was added, and `last_run_note` and `report` were corrected (both still pointed at 11-15 after the 11-18 run).

## Recommendations (Tier 2)

No tasks were added to `todo.md`. Every recommendation below is a code, configuration or documentation change, not a content task, and the 11-18 condense recommendation is still awaiting approval.

### 1. Enforce the 30-day gate on the /loop path (carried from 08-02 and 11-18)
- **Proposed change**: in `tools/evolution/cycle_post.py` near L449, pass `get_cycle_triggers(cycles_completed)` through `filter_triggers_by_min_age(triggers, state, now)` before merging into `pending-triggers.json`, as `scripts/evolve_loop.py` L1370 already does.
- **Rationale**: 11 runs in 46 days, 30 consecutive with no change. Each run costs a loop slot.
- **Risk**: Low. The gate and its tests already exist.
- **To approve**: a code change. Commit it with the next tooling batch.

### 2. Queue condense tasks for over-gate pages (carried from 11-18, absorbs 11-18 T3 (g))
- **Proposed change**: mint condense tasks a few at a time for over-gate pages whose excess is prose and that carry no human length decision or veto.
- **Rationale**: 73 pages are over the gate (up from 70), and condense has not run since 11-18. The worst cases are already vetoed or human-deferred (`apex/phenomenal-output-causal-machinery-dissociation` #veto; `topics/epistemology-of-convergence-arguments` three prior passes), so the actionable set is smaller than the count.
- **Risk**: Medium. Each task must state the prose/apparatus split first (analyze_length totals include references).
- **To approve**: tell the driver to mint them.

### 3. Measure `apex/apex-articles.md` as an index (carried from 11-18, narrowed)
- **Proposed change**: add `apex-articles.md` to the skip rule in `tools/curate/length.get_length_warnings`. `voids/voids.md` is already skipped.
- **Risk**: Low.

### 4. Brief tenet-check repair tasks to cover the paragraph and its siblings (carried from 11-15)
- **Proposed change**: when check-tenets mints a task, name the paragraph and any sibling sentence on the page or its hub that states the same claim.
- **Rationale**: Review Finding Patterns 1, in four reviews this window.
- **Risk**: Low.

### 5. Refresh the CLAUDE.md section-caps table (carried from 10-26)
- **Proposed change**: the table still reads 320/320/100/80. The live caps are 370/370/125/90.
- **Risk**: Low. It is a documentation edit for the operator.

## Items for Human Review (Tier 3)

Items 1 to 7 are the driver's verified inputs for 2026-11-25, with my checks added where I made one. Items 8 to 13 are new or carried.

### 1. agentic-social selector (merged with 11-18 (i))
- **Issue observed**: the topic-overlap filter treats the hub tags `hard-problem-of-consciousness` and `philosophy-of-mind` as overlap. On 11-25 the strict screen left 0 usable candidates out of 934 (only two articles with 10 or more prior posts survived), while 37 articles posted once each failed only on hub-tag overlap. `CONTENT_DIRS` in `.claude/skills/agentic-social/scripts/agentic_social_api.py` L49-53 lists concepts, topics and apex only (I checked this), so `voids/` is never scanned. Nothing ranks by lifetime post count.
- **Why human needed**: skill script change.
- **Suggested action**: exempt hub tags from the overlap test, add `voids/`, and rank by lifetime posts.

### 2. research-voids capacity check
- **Issue observed**: the skill stops only at `count >= cap`. At 15:0xZ voids was 124/125, with five pending voids expand tasks for the one slot and 246 banked `voids-*` notes (both counts re-measured this run). The driver skipped the trigger by hand. Queue Health shows that none of the five has been reached in at least seven days.
- **Why human needed**: skill instruction or cap change.
- **Suggested action**: also stop when pending voids expand tasks are at least the free slots, or raise `max_voids`. Either way, decide which of the five gets the slot.

### 3. `hugo/config.toml` `summaryLength` inside `[taxonomies]`
- **Issue observed**: `summaryLength = 150` sits at L16, after `[taxonomies]` at L13, so TOML scopes it as a taxonomy. `hugo/public/150/` exists and the sitemap lists it. First reported 10-25. check-links still flagged it on 11-25.
- **Suggested action**: move the line above `[taxonomies]`.

### 4. harvest-research-subjects drops deferred subjects
- **Issue observed**: deferred over-cap subjects are not persisted, and the review is marked scanned anyway. It happened again at 11-25 07:4xZ. The driver saved `../unfinishablemap_log/harvest-deferred-2026-11-25a.json` and re-submitted at 13:4xZ.
- **Suggested action**: write deferred subjects to the harvest state file and re-offer them, or do not mark a review scanned while it has deferrals.

### 5. A research `fold` verdict mints nothing (carried from 10-26 "chain mints fold tasks")
- **Issue observed**: `tools/research/chain.py` L38 `NON_MINTING_ACTIONS = ("fold", "refine", "none")`. Two folds on 11-25 (attitudinal theories into `topics/valence-as-a-natural-kind`; Key and Brown into `topics/the-epiphenomenalist-threat`) needed driver-minted refine-drafts. Both are now P2 pending.
- **Suggested action**: have `fold` mint a refine-draft on the note's target page.

### 6. Section pressure (merged with 11-15 Tier 2 #2 and #4)
- **Issue observed**: topics 370/370 and concepts 370/370 by `count_section_files`. Coalesce was abandoned in 6 of 6 runs since 11-18 (11-19 ×2, 11-20, 11-24 ×2, 11-25), because the overlapping pairs overflow their hard limits by 1,271 words or more. New-article capacity can come only from `/archive`, `/condense` or a cap raise. Meanwhile 10 topics and 6 concepts entries wait in `task_chains.pending_articles`.
- **Suggested action**: choose among a cap raise, targeted archiving, or accepting fold/refine-only output for full sections. Separately, gate the coalesce slot so it skips when no article has been added or removed since its last no-candidate run.

### 7. `cycle_post` would commit a truncated hugo file
- **Issue observed**: a loop session killed mid-sync left `hugo/content/workflow/archive/changelog-2026-W13.md` at 0 bytes, and `cycle_post`'s `git add -A` would have committed it. The driver re-synced first. The file is 308,862 bytes now, and no 0-byte file remains under `hugo/content/` (checked this run).
- **Suggested action**: have `cycle_post` refuse to commit any hugo content file that went from non-empty to 0 bytes.

### 8. Changelog entries with bare-time headings are never archived (new; feeds the NEEDS-HUMAN changelog task at todo L1779 and item 12)
- **Issue observed**: see Convergence Progress. 870 entries from 08-02 to 11-08 (2.62 MB) can never leave `changelog.md`, and every session writing `## HH:MM - task` adds more.
- **Why human needed**: code plus 16 skill templates.
- **Suggested action**: either have `parse_changelog_date` fall back to the commit date of the heading line (for example via `git log -S`), or change the templates to `## YYYY-MM-DD HH:MM UTC - task` and run a one-off dating pass. Then let `archive_workflow.py` archive them. This would also shrink the page that the L1779 task and the outer reviewers cannot fetch.

### 9. The quality block is a constant (new)
- **Issue observed**: no code writes `quality.*`. `medium_issues` has been 10 since at least January.
- **Why human needed**: either a writer has to be built (from what source?) or the fields and the abort condition that reads them have to be dropped.
- **Suggested action**: until one of those happens, treat this skill's critical-issues abort condition as untestable.

### 10. Register bands P-RR1/P-RR2 (carried, 11-18 (c))
- **Issue observed**: still provisional, `human_modified: null`.

### 11. Deep-review and tenet-check lenses (carried, 11-18 (a) and (d))
- **Issue observed**: the deep-review ledger is now routine in practice. The tenet-check sibling pattern continues (Tier 2 #4).

### 12. Outer reviewers that did not read the page (carried, 11-18 (h))
- **Issue observed**: four of four cycles this window. Claude was affected on three nights and Gemini on two.
- **Suggested action**: paste the target page's text into the commission prompt, or have collect mark a review that did not read its target so the synthesis discounts it. Decide this together with item 8 and the L1779 task, because the prompt sends reviewers to the changelog.

### 13. Human decisions and queue order (carried, 11-18 (e) and (f))
- **Issue observed**: 33 blocked tasks are unchanged, and both P1s date from 2026-10-14 (42 days). Under top-first order within a priority, older P3s (including the five voids expands) wait behind newer ones.
- **Suggested action**: the five oldest blocked tasks are named in the 11-18 report. For the voids slot, see item 2.

## Next Tuning Session

- **Recommended**: 2026-12-25 if Tier 2 #1 lands; otherwise the six-cycle trigger will fire again in about three to seven days.
- **Focus areas**: whether the changelog heading fix lands and the file shrinks; queue growth (523 open); the voids slot decision; whether any blocked human decision moves.
