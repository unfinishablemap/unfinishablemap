---
ai_contribution: 100
ai_generated_date: 2026-10-10
ai_modified: 2026-10-10 15:21:47+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-10-10
date: &id001 2026-10-10
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-10 15:21:47+00:00
modified: *id001
related_articles:
- '[[todo]]'
- '[[changelog]]'
title: System Tuning Report - 2026-10-10
topics: []
---

# System Tuning Report

**Date**: 2026-10-10
**Sessions analyzed**: 245 loop posts (`cycle_post done` lines in `../unfinishablemap_log/evolve_loop.log*` after 2026-10-07 03:42 UTC)
**Period covered**: 2026-10-07 03:42 → 2026-10-10 15:21 UTC (3.5 days)

## Executive Summary

The loop is healthy: 241 of 245 posts succeeded, `failed_tasks` is empty, there are no critical issues, and all four failures were Chrome-driven commissions. This is the **nineteenth consecutive run with no Tier 1 change**: the four Tier 1 levers (`cadences`, `overdue_thresholds`, `locked_settings`, replenishment weights) are still absent from `evolution-state.yaml`. The main operational cost is now at the hand-off between forks and the queue. The driver hand-copied task fields into all 8 queue dispatches today. It also minted 10 tasks and 3 addenda by hand from findings that forks and check-tenets reported but cannot queue themselves.

## Metrics Overview

| Metric | Current | Previous (10-07) | Trend |
|--------|---------|------------------|-------|
| Loop posts in window | 245 (3.5 d) | 235 (3.3 d) | → (~70/day) |
| Post status | 241 SUCCESS / 4 FAILURE | 234 / 1 | ↑ failures, all commissions |
| `failed_tasks` | {} | {} | → |
| Kind mix | queue 102 · trigger 46 · cycle 42 · social 36 · commission 10 · collect 6 · combine 3 | queue 97 · trigger 45 · cycle 40 · social 35 · … | → (queue share 42%) |
| Quality | critical 0 · medium 10 · low 3 | critical 0 · medium 10 | → |
| Sections (`progress`) | topics 343/360 · concepts 349/360 · voids 113/115 · positions 23/80 | 343 · 347 · 113 · 23 | → |
| Active tasks (parse_tasks) | 73: P2 21 (13 pending, 8 blocked) · P3 52 (45 pending, 7 blocked) | P2 count 11 | ↑ P2 (outer-review + driver mints) |
| `task_chains.pending_articles` | 12, none minted to expand-topic | 11 | ↑ (stalled) |
| Coalesce ABANDON streak | ≈42 (6 runs in window, all no-candidate) | 36 | ↑ |
| Driver hand-commits | 4 (3 `auto(todo)` mints, 1 `auto(sync)`) in this session alone | 15 of 273 | → |
| tune-system interval | 3.5 d (30-day cadence) | 3.3 d | gate inert |

## Findings

### Cadence Analysis

- **No cadence configuration exists to tune** (re-checked with grep: no `cadences:`, `overdue_thresholds:` or `locked_settings:` key). Cadence lives in code (`tools/evolution/cycle.py`, `time_trigger.py`).
- **tune-system fired 3.5 days after the previous run**, against a nominal 30-day cadence. That makes 19 runs at a 3–4.3-day interval. The cycle-trigger path ("every 6 cycles") is what governs it, not the 30-day gate. Carried as Tier 2.
- **commission-claude-review is blocked until 2026-10-14 04:00Z** (`commission-claude-review-blocked-until`) after the weekly Fable limit. The 10-10 03:21 post recorded FAILURE. This matches `claude-commission-weekly-fable-limit-needs-manual-backoff`; the backoff key is present, so no action is needed.

### Failure Pattern Analysis

Four failures, all `kind=commission`. Two of them are the Gemini leg (10-07 04:34, 10-08 04:25). The other two were on 10-10: ChatGPT at 02:04 (Chrome unavailable; it succeeded on retry at 04:11) and Claude at 03:21 (weekly limit). Gemini recovered: `collect-gemini-review` succeeded on 10-10 at 04:50, and `combine-outer-reviews` ran on 10-10 at 06:18. **There is no non-Chrome failure in 235 non-commission posts.** None of this meets the 3-same-type threshold for a new action, and the Gemini pattern noted in earlier reports now looks resolved.

### Queue Health Analysis

1. **P3 tasks are not being executed.** 45 P3 tasks are pending. The three P3 rows minted from `tenet-check-2026-10-08` (split-brain, clinical-dissociation, forward-in-time) are still open after two days, while every P2 dispatched this window ran. This matches `a-reports-only-reviews-yield-is-its-priority-list-not-its-findings`: a finding is fixed only if it reaches a P0–P2 row. Today the driver minted check-tenets priority-list items at P2 so that they would run. The memory-channel P3, which carries priority item 4, will not run until it is promoted.
2. **`pending_articles` keeps growing with no minting path while replenish is idle.** It rose 11 → 12, and the last replenishment was 2026-09-29. With 13 pending P2 tasks the replenish gate is correctly closed, so nothing converts banked research into expand-topic tasks. This was carried from 10-07 and is unchanged. The research pipeline (harvest → research-topic) is producing input. For example, today's harvest minted `assent-and-ascertainment-in-buddhist-epistemology` at P3.
3. **The P2 inflow today was dominated by the 10-10 outer-review cycle and driver follow-ups.** 21 P2 rows are open. The outer-review rows are being consumed at about one per queue slot.

### Review Finding Patterns

These are the main findings of this run. Each is a recurring pattern with 3 or more instances in the window.

1. **The dispatch gap is still open (carried from 10-03, verified again).** `task_to_skill` forwards only File, Notes and Review file. Today the driver hand-copied `Headroom`, `Secondary files` or `Coordination` into **all 8 queue dispatches**. Without this, the forks would not have seen the length limits of 2–6 words on `free-will`, `post-decoherence` and `amplification-mechanisms`, or the sibling-task ownership on `continual-learning-argument`.
2. **Sibling defects that forks find are not queued by anyone except the driver.** Refine-draft briefs tell forks not to edit `todo.md`, because a mid-fork insert shifts line numbers and `cycle_post` would mark the wrong task. As a result, forks report sibling defects in prose only. Today:
   - Six forks reported 9 verified sibling defects.
   - check-tenets reported 4 priority items and 2 coordination notes, and, by its contract, mints nothing.
   - The driver minted 10 tasks and appended 3 addenda across 4 commits.

   Earlier memory notes record that defects reported only in prose stay unfixed (`review-findings-get-discharged-in-prose-not-as-tasks`).
3. **A fix created a contradiction the same day.** The 13:24Z `free-will` L66 rewrite came verbatim from the outer-review task's prescription ("count against illusionist or epiphenomenal readings"), and check-tenets flagged it the same afternoon against `tenets.md` L101. Outer-review task notes are not checked against `tenets.md` before dispatch. One instance, so this is recorded, not acted on.
4. **ai_system over-attribution.** 1 of 7 content forks today, the quantum-biology refine, appended `+claude-opus-5-5` for an edit of about 4.5%. The driver reverted it. Since then, briefs have said "leave ai_system unchanged unless you substantially re-author", and 0 of 6 later forks changed it.
5. **Obsidian-only writers leave Hugo stale.** `embed-videos` (by contract) and `research-voids` research-note edits both reached `cycle_post` unsynced. The driver synced both by hand. `cycle_post` sometimes commits synced files (seen at 14:07) but does not run sync itself.

### Convergence Progress

Article counts are flat (topics 343, concepts 349, voids 113, positions 23) because the window was a calibration window: almost all queue work was refine-draft from the 10-10 outer-review cycle and its follow-ups. Voids sits two slots from its cap of 115. research-voids ran gap-closure work instead of minting, and coalesce cannot free voids slots: the two shortest voids articles total 3,203 words, over the 2,999 limit for one article. The operator's voids-slot decision (NEEDS-HUMAN cycle allocation, todo L124) is the binding constraint. Medium issues are steady at 10.

## Changes Applied (Tier 1)

*No changes applied.* No Tier 1 lever exists in `evolution-state.yaml` (the same four keys as before are absent, re-checked with grep).

## Recommendations (Tier 2)

### Give tune-system a real minimum interval
- **Proposed change**: enforce the 30-day cadence on the /loop path, or move tune-system to a wall-clock weekly trigger like literature-drift-review.
- **Rationale**: 19 consecutive runs at 3–4 day intervals, each finding no lever. The report is useful as a weekly operational digest, but a 3.5-day cadence mostly re-confirms carried items.
- **Risk**: Low.
- **To approve**: change the trigger registration in `tools/evolution/cycle.py` / `time_trigger.py`.

### Reallocate the two coalesce slots while voids is capped (carried)
- **Proposed change**: until the voids-slot decision lands, redirect the 2/24 coalesce slots to deep-review or to queue.
- **Rationale**: about 42 consecutive abandons. In voids and topics no pair can merge under the hard limit, and the only fitting concepts pairs were all declined earlier for good reasons and have not changed.
- **Risk**: Low; reversible.
- **To approve**: see the open NEEDS-HUMAN (cycle allocation) entry at todo L124.

### Promote check-tenets priority-list items by default
- **Proposed change**: mint the ≤4 priority-list items of each tenet check at P2 (as the driver did today), not P3.
- **Rationale**: P3 rows are not executed, as the three 10-08 P3 rows show, and the priority list is the only part of a reports-only review that historically gets fixed.
- **Risk**: Low; capped at 4 per check.

## Items for Human Review (Tier 3)

### Forward all task fields to forks
- **Issue observed**: `task_to_skill` drops every field above `Notes` except File and Review file, so the driver hand-copied fields in 8 of 8 dispatches today. This was first reported on 10-03.
- **Why human needed**: a code change to the dispatch path.
- **Suggested action**: append `Headroom`, `Secondary files`, `Coordination`, `Caution` and `Carry` to the args string in `task_to_skill`.

### A sanctioned channel for fork-discovered follow-ups
- **Issue observed**: forks find verified sibling defects but are told not to write `todo.md`, which avoids mismarks by `cycle_post`. So follow-ups depend on a driver reading the prose.
- **Why human needed**: this changes the skill contract and `cycle_post` behaviour.
- **Suggested action**: let forks write `.unfin/followups.jsonl`, which `cycle_post` mints after marking the picked task, deduplicated by file and quoted span. Applying the same path to check-tenets priority lists would close Tier 2 item 3.

### Sync inside cycle_post when obsidian content changed
- **Issue observed**: `embed-videos` and research-note edits reached commit with Hugo stale. This is the same family as `embed-videos-leaves-hugo-stale-with-stale-ai-modified`.
- **Suggested action**: have `cycle_post` run `scripts/sync.py` before committing whenever `obsidian/` has changes. This keeps embed-videos a pure obsidian writer while removing the stale window.

### check-links should read `_redirects`
- **Issue observed**: 424 reported, of which 376 are Netlify 301s that the dev server ignores. Article sections have 0 broken links (independent build check: 65,193 links).
- **Suggested action**: teach the checker to apply `hugo/static/_redirects` so that it can serve as a pre-push gate.

## Next Tuning Session

- **Recommended**: 2026-11-09 (30 days). On current behaviour the trigger will fire in about 3.5 days.
- **Focus areas**:
  - whether the dispatch-field and follow-up channels are built;
  - P3 execution rate;
  - `pending_articles` growth;
  - the voids-slot decision;
  - whether outer-review prescriptions keep colliding with `tenets.md`.