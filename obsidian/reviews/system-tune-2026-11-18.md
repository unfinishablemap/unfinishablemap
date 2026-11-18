---
title: "System Tuning Report - 2026-11-18"
created: 2026-11-18
modified: 2026-11-18
human_modified: null
ai_modified: 2026-11-18T20:50:05+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[todo]]"
  - "[[changelog]]"
ai_contribution: 100
author: null
ai_system: claude-fable-5-2
ai_generated_date: 2026-11-18
last_curated: null
---

# System Tuning Report

**Date**: 2026-11-18
**Period covered**: 2026-11-15 (previous run) to 2026-11-18
**Run by**: the loop driver, inline (the skill loaded in the driving session, not in a fork)

## Executive Summary

The loop is healthy by its own measures: 20 of the last 20 recorded tasks succeeded, no critical issues are recorded, and no task has failed in the window. No setting was changed, because the settings this skill is allowed to change do not exist in the state file. This is the twenty-ninth consecutive run with nothing to tune, and the skill ran three days after its last run.

What changed in how the system behaves is in the review lenses, not the settings. Reviews that check quotations at the primary text keep finding defects that earlier reviews had marked verified; a check for tenets used as conclusions found 87 above-grade sentences where the standard contradiction check finds none; and grades recorded in the positions register hold where grades living only on a hub page cost dozens of follow-up tasks. Those are skill-level matters for the operator (Tier 3 below).

Three numbers deserve attention: 70 pages are at or over their hard length gate and only 2 have a condense task; 33 tasks are blocked awaiting a human decision, the oldest from early September; and 410 of 430 open tasks are P3.

## Metrics Overview

| Metric | Current | Note |
|--------|---------|------|
| Recent tasks recorded | 20, all success | failed_tasks is empty |
| Critical issues | 0 | medium 10, low 3 |
| Open tasks | 430 | P1 2, P2 18, P3 410 |
| Pending / blocked | 395 / 33 | 2 superseded |
| Sections (measured) | topics 370 of 370; concepts 370 of 370; voids 124 of 125; positions 29 of 90 | by count_section_files |
| Pages at or over hard length gate | 70 | topics 26, concepts 15, voids 20, apex 9 |
| Social posts recorded, last 14 days | 82 on 81 distinct pages | the record only reaches back to 2026-11-11 |

## Abort conditions

None met. Last ten tasks: 0 failed. quality.critical_issues is 0. No file failed to read. Convergence regression cannot be assessed (see Convergence).

## Findings

### Cadence Analysis

Insufficient evidence, and nothing to act on. The state file has no `cadences` and no `overdue_thresholds` keys. The loop is driven one iteration at a time from an interactive session, so intervals between runs reflect the operator's invocation rhythm and one usage-limit outage of about fourteen hours (roughly 14:20Z on 2026-11-17 to 04:00Z on 2026-11-18). That gap is not task failure and is not read as overdue cadence.

One cadence observation: this skill is documented as monthly but is triggered every six cycles, which at the present pace is every three days (previous runs 2026-11-12 and 2026-11-15). Each run costs a slot and has had nothing to change since 2026-09-19.

### Failure Pattern Analysis

Below threshold (three failures of one kind are required; there are none). One fork was killed mid-edit by the usage limit on 2026-11-17 and was resumed the next morning; its work completed. Two smaller process slips are recorded in the changelog for 2026-11-18: a fork made one request to a general search engine by mistake, and a scanned paper was downloaded from a web archive and deleted unread. Briefs since then forbid both.

### Queue Health Analysis

- **Order.** The picker sorts pending tasks by priority and then by position in the file (`tools/todo/processor.get_next_task`). The driver suspected P3 tasks were jumping ahead of P2 tasks; that is wrong. Every P2 other than the two minted today is blocked on a human decision, so P3 was the highest pending priority each time. Within a priority the file position decides, and new tasks are inserted at the top, so the newest P3 is always picked first.
- **Consequence.** 41 P3 tasks were minted in the last three days and sit above the older ones. 13 P3 tasks are more than 30 days old, 5 more than 60 and 1 more than 90 (114 days). Under top-first order they are reached only when minting stops.
- **Blocked tasks.** 33 tasks are blocked, nearly all awaiting a human decision. The oldest date from 2026-09-02 to 2026-09-14 (length decisions on `topics/basal-and-bioelectric-cognition` and `apex/born-preserving-causal-efficacy`; approval for register scope changes to propagate; the Chalmers-anthology date reconciliation). Both P1 tasks are human decisions on the positions register, 35 days old. The Tenet 3 quantifier question has been open since 2026-10-03.
- **Books.** The Completed section of the task file holds no parsed blocks at present and 42 weekly archive files exist, so archiving is keeping up. The file is still 10,534 lines, of which about 5,900 are open tasks.

### Review Finding Patterns

Threshold met (three or more reviews showing the same pattern) for three patterns:

1. **Quotations verified by metadata only.** Of 215 deep reviews in the last 30 days, 9 carry a source ledger (quotations checked at the primary text). All 9 found misattributions or unsupported quotations; the three run on 2026-11-18 overturned notes from earlier reviews that had recorded the same citations as verified.
2. **Tenets stated as supported.** The 2026-11-18 tenet check found no contradiction and 87 sentences on about 78 pages above the registered grade, with 21 of 125 void tenet sections not at grade. The same finding recurred page by page in the deep reviews of 2026-11-15 to 2026-11-18.
3. **Fixes that did not hold were closed without running.** The durability audit tested 69 completed repair tasks; 68 held. The failures were tasks closed by consolidation. Closures of that kind number 6 in June and 1 in July in the files searched here and none since, so the practice appears to have stopped. (The audit counted 61 such closures using a wider pattern; the difference is in what was matched, not a disagreement about the trend.)

### Convergence Progress

Insufficient evidence. The state file records counts (topics and concepts at cap, voids one below, 44 apex articles, 772 research notes) but no per-session convergence series to compute a rate from. With topics and concepts at their caps, new-article work is closed and the loop is wholly in review and repair, which is the designed behaviour at capacity.

## Changes Applied (Tier 1)

*No changes applied.* The three permitted change types (cadence, overdue threshold, replenishment weight) have no keys in the state file to act on. No setting is locked. No cooldown applies.

## Recommendations (Tier 2)

### Queue condense tasks for pages over their hard gate
- **Proposed change**: mint condense tasks, a few at a time, for over-gate pages whose excess is prose and that carry no human length decision. 70 pages are at or over gate; 2 have a condense task. Worst cases after the two section indexes: `apex/phenomenal-output-causal-machinery-dissociation` (6,897 against 5,000), `topics/epistemology-of-convergence-arguments` (5,745 against 4,000), `topics/ethics-of-cognitive-enhancement-under-dualism` (5,700), `topics/born-rule-and-the-consciousness-interface` (5,442).
- **Rationale**: over-gate pages block every additive correction; several of today's fixes had to be made length-neutral for that reason, and three over-gate pages were found only by accident.
- **Risk**: Medium. Condensing has in the past cut calibration qualifiers, and reviews attribute part of the excess to reference lists, not prose. Each task should state the prose and apparatus split first.
- **To approve**: tell the driver to mint them, or run `/replenish-queue` and confirm its length-violation source is producing tasks.

### Exclude the two section indexes from the length gate
- **Proposed change**: `apex/apex-articles` (14,128 words) and `voids/voids` (8,667) are listing pages measured as ordinary articles, so they read as critical at any size.
- **Rationale**: they distort every over-gate count and can never pass.
- **Risk**: Low.
- **To approve**: a code change in the length tool's skip list (only `apex.md` is skipped today).

### Run this skill monthly
- **Proposed change**: trigger tune-system on a wall-clock monthly schedule instead of every six cycles.
- **Rationale**: twenty-nine consecutive runs with nothing to tune; at the present pace it runs every three days.
- **Risk**: Low.
- **To approve**: change the trigger in `tools/evolution/cycle.py`.

## Items for Human Review (Tier 3)

### (a) Deep review's default lens
- **Issue observed**: 9 of 215 deep reviews in 30 days checked quotations at the primary text; all 9 found defects that metadata checks had passed.
- **Why human needed**: it is a change to a skill's instructions and to what a review costs.
- **Suggested action**: consider making the source ledger the default for pages built from research notes, and requiring a review to say which of its "verified" marks were checked at the text.

### (b) Closing tasks without running them
- **Issue observed**: the only repair tasks found not to hold were closed by consolidation; the practice appears to have stopped after July.
- **Why human needed**: it is a convention, not a setting.
- **Suggested action**: if it is ever used again, require the closing note to quote the sentence as it then stands.

### (c) Checking settled grades into the register
- **Issue observed**: grades recorded as positions are cited by anchor and hold; the illusionism reply lived only on its hub page and 54 pages drifted above it. Two entries were added today (P-RR1, P-RR2) with provisional bands.
- **Why human needed**: the bands and the choice of file are the operator's.
- **Suggested action**: confirm or change the bands; consider having review skills propose a register entry whenever they settle a grade that more than a few pages state.

### (d) The tenet check's default lens
- **Issue observed**: the standard pass looks for contradictions and finds none; the yield came from asking where tenets are used as conclusions.
- **Why human needed**: skill instructions.
- **Suggested action**: consider adding that lens to the skill.

### (e) Queue order within a priority
- **Issue observed**: within a priority the task nearest the top of the file is picked, and new tasks go to the top, so the newest are done first and older P3 tasks wait indefinitely.
- **Why human needed**: it is a design choice in the picker.
- **Suggested action**: decide whether same-priority tasks should be taken oldest first, or leave as is and accept the tail.

### (f) Human decisions outstanding
- **Issue observed**: 33 blocked tasks, the oldest eleven weeks old; both P1 tasks are among them.
- **Why human needed**: they are the operator's decisions by definition.
- **Suggested action**: the five oldest are named under Queue Health; the Tenet 3 quantifier census is in today's tenet check.

### (g) Pages over their length gate
- **Issue observed**: see the first Tier 2 item.

### (h) Outer reviewers that did not read the page
- **Issue observed**: all nine commissions of the last three nights were collected, but the review files record that the Claude reviewer could not load the target page on all three nights and Gemini on two; only ChatGPT read it each night. Only three cycles are on record in the pending file, so this is a short series.
- **Why human needed**: the fix is in the commission prompts or in how the page is supplied to the reviewer.
- **Suggested action**: paste the page text into the prompt, or have the collect step mark a review that did not read its target so the synthesis discounts it.

### (i) Social-post selection
- **Issue observed**: the driver has overridden the selector's choice on every post; 82 posts on 81 distinct pages are recorded for the last week.
- **Why human needed**: whether to change the selector or keep the override is a design choice.
- **Suggested action**: none urgent; the override works.

## Next Tuning Session

- **Recommended**: 2026-12-18, if the trigger is changed; otherwise it will recur in about three days.
- **Focus areas**: whether over-gate pages are being condensed; the age of the blocked queue; whether the three lens patterns above recur.
