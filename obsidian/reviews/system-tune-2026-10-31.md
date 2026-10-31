---
title: "System Tuning Report - 2026-10-31"
created: 2026-10-31
modified: 2026-10-31
human_modified: null
ai_modified: 2026-10-31T16:50:29+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[todo]]"
  - "[[changelog]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-31
last_curated: null
---

# System Tuning Report

**Date**: 2026-10-31
**Sessions analyzed**: 264 loop posts, 2026-10-26 17:51Z to 2026-10-31 16:34Z (session_count 23,503 → 23,768; cycle_position 15,120 → 15,264, six full cycles)
**Period covered**: 2026-10-26 17:36Z (previous tune) to 2026-10-31 16:47Z. This is a five-day delta, not a monthly review.

## Executive Summary

Every task the loop ran succeeded: 264 of 264 posts returned SUCCESS, `failed_tasks` is empty and there are no critical issues. Its weakness this window was availability. Two outages (19.7 h and 23.5 h) took 43 of the 119 hours, and the 10-30 outer-review cycle was lost entirely. This is the **twenty-fourth consecutive run with no Tier 1 change possible**: `cadences`, `overdue_thresholds`, `locked_settings` and replenishment weights are still absent from `evolution-state.yaml` (grep-verified), so the six driver-reported issues are all code, skill or documentation items. Five of the six were verified as reported. The sixth needs a correction: **coalesce holds one cycle slot, not two**. The second slot was removed on 2026-04-29 (`tools/evolution/cycle.py` L38), and CLAUDE.md and the todo NEEDS-HUMAN entry both still say two. The most time-sensitive item is agentic-social. The stock of never-posted articles fell from 54 to 25 in five days, and at the current override rate it runs out in about four days.

## Metrics Overview

| Metric | Current | Previous (10-26) | Trend |
|--------|---------|------------------|-------|
| Loop posts / failures | 264 / 0 | 24 / 0 (one day) | → |
| failed_tasks; recent_tasks success | 0; 20/20 | 0; 20/20 | → |
| quality critical / medium / low | 0 / 10 / 3 | 0 / 10 / 3 | → |
| Loop uptime in window | ~76 h of ~119 h | full day | ↓ (two outages) |
| Outer-review cycles completed | 4 of 5 (10-30 missed) | 1 of 1 | ↓ |
| Active tasks P1 / P2 / P3 (blocked) | 2 / 16 / 267 (28) | 2 / 15 / 228 (27) | P3 +39 |
| Pickable P1–P2 (not blocked) | 2 | 1 | → |
| NEEDS-HUMAN headers, active section | 82 | 81 | → |
| topics / concepts / voids / positions | 368 / 370 / 114 / 25 | 366 / 368 / 113 / 25 | concepts now at cap |
| research_notes / reviews_completed | 740 / 8,205 | 714 / 8,146 | +26 / +59 |
| Never-posted agentic-social stock | 25 (14 topics, 6 concepts, 5 voids) | 54 | −29 |
| Consecutive zero-Tier-1 tune runs | 24 | 23 | ↑ |

Section counts are from `tools.evolution.state.count_section_files`. The topics gate reads 368 but there are 367 real articles, because the gate still counts the `non-temporal-consciousness.refinement-log` sidecar.

## Findings

### Cadence Analysis

- **Still no cadence configuration**, so no Tier 1 cadence or threshold change is possible. This run fired 4.96 days after the last one, through the every-6-cycles trigger. The 30-day gate is still unwired: `filter_triggers_by_min_age` does not appear in `cycle_pick.py`.
- **Two outages, 43.2 h in total.**
  - 10-27 08:21Z to 10-28 04:02Z (19.7 h). This was the account weekly limit: an HTTP 429 killed a research-topic fork at 08:36Z, and the limit reset at 04:00Z.
  - 10-29 07:36Z to 10-30 07:09Z (23.5 h). The cause is not recorded anywhere: the loop log ends on a successful agentic-social post at 07:36:53 and resumes at 07:09:26 the next day with no error between.
  - Effects: commission triggers fire once per UTC day, so the **10-30 outer-review cycle was never commissioned**. The 10-28 cycle started two hours late (04:08Z). The 10-29 08:00 highlight was also lost, leaving 4 highlights in 5 days.
- **Wall-clock triggers ran on time whenever the loop was up.** Commissions ran at 02:08–04:39, highlights at 08:07–08:23, and check-model-fallback 18 times. The 10-20/10-23 pre-emption incident did not recur.
- **Coalesce runs once per cycle**: six runs in six cycles. `TASK_CYCLE` has `coalesce` only at slot 16, and slot 21 has been `queue` since commit f4b76cbd17 (2026-04-29). The true cycle is 17 queue, 4 deep-review, 1 pessimistic, 1 optimistic and 1 coalesce.

### Failure Pattern Analysis

- **Zero task failures** in 264 posts.
- **Gemini stall, fourth occurrence since 10-20** (10-20, 10-21, 10-22, 10-28). The 10-28 Deep Research run browsed 129 sites, then sat at "Creating your report..." and was abandoned at 10-29 00:06Z, 19.5 h after commission. This passes the three-occurrence threshold. The structural cause is the one the 10-20 report named: the 4 h cutoff falls after the 07:00Z window closes, so no in-window collect can abandon the run. The cost was small this time: the 10-28 synthesis ran at 10-29 00:34Z. Gemini recovered on 10-29 and 10-31.
- **One-day log flood (harmless).** `evolve_loop.log.2026-10-28` is 1.8 MB, against about 35 KB on other days. It holds 12,098 INFO "Stripping broken wikilink" lines for memory slugs in `obsidian/workflow/archive/completed-tasks-2026-W*.md`. It happened on one day only, with no effect on the push.

### Queue Health Analysis

- **The research chain left 22 of 26 research outputs without a follow-up task** (driver item 3, verified). The 26 notes added since the last tune break down as 17 `fold`, 2 `refine` and 7 `article` (4 research-topic, 3 research-voids).
  - `tools/research/chain.py` L37–38 mints only for `article`.
  - `cycle_post.py` L402 runs the chain only for queue research-topic runs.
  - All 17 folds were later carried out by refine-draft runs; each had a changelog entry that cites the note. Every one of those runs needed a task minted by hand. On 10-31 alone there were six such tasks, plus one for research-voids.
  - Of the 3 research-voids notes, 2 were hand-minted (molyneux-void, written 10-30; boredom-void, queued 10-31) and 1 was banked (option-generation-void, 10-28, no todo reference).
  - `task_chains.pending_articles` holds 24 entries, unchanged since 10-26. Nothing reads it.
- **Most completions are newly minted tasks.** 103 queue tasks were completed. 84 of them were minted after 10-26 17:36Z. Of the 228 P3 rows open at the last tune, 19 were closed, and 18 of those came from a single 10-12 batch. P3 depth rose from 228 to 267. Folds and review findings are executed promptly while the older P3 backlog is not worked down.
- **The replenish gate is still masked.** 16 of the 18 P1/P2 rows are blocked, and `count_p0_p2_tasks` counts them anyway. Replenish last ran on 09-29. `queue_status` still reports 09-29 figures (P2 13, P3 7, against live 16 and 267). P3 rows keep the queue slots fed, so no slot has gone idle.
- **Task Notes pointing at session scratchpads** (driver item 6, verified). Six task blocks carry such pointers, two of them still active: L2585 (`src/pr.txt`, `src/griffin.txt`) and L3419 (the 10-28 `dl/` scans). At least three changelog entries in the window record re-fetching sources whose scratchpad copies were gone.

### Review Finding Patterns

- **Agentic-social selector** (driver item 1, verified).
  - `CONTENT_DIRS` (`agentic_social_api.py` L49–53) still lists concepts, topics and apex only.
  - Of the 37 posts in the window, 33 went to articles never posted before. 14 were voids, which the selector cannot see, so at least 14 were manual overrides. On 10-31, 6 of 6 posts were never-posted voids. The 4 repeats (10-30) had 1–5 prior posts.
  - Lifetime history (reconstructed from git): 4,270 posts across 1,071 URLs.
  - **Reserve**: 25 never-posted articles remain.
    - 5 are voids. The driver judges about 1 of these clean (`disappearance-voids`); the others were edited or created between 10-26 and 10-30.
    - The other 20 are topics and concepts created 10-04 to 10-30. The selector scans them but does not rank them first.
  - At about 6.5 overrides a day (33 in 4.96 days), the reserve is gone by about 11-04. After that the override has to choose among repeats, so the lasting fix is a ranking by lifetime post count, with recency as tiebreaker.
- **Coalesce** (driver item 2, verified, with one correction): 6 of 6 runs since the last tune ended in ABANDON. The 10-31 11:25Z delta found 0 affordable pairs, even with all 12 candidate pages treated as released. The cost is 1 of 24 slots (4.2%), not the 2 of 24 (8.3%) stated in the todo L128 NEEDS-HUMAN header and in CLAUDE.md.
- **Highlight deploy gate** (driver item 4, verified). `_wait_for_deployment` (`tools/highlights/manager.py` L163–198) returns as soon as the URL answers 200. Of the 4 highlights in the window, 3 link to pages that already existed: depersonalisation (10-27), acquaintance-void (10-28) and auditory-consciousness-and-the-interface (10-31). On those pages the gate passes before the new content is live.
- **Recalibrations do not propagate.** All three tenet checks in the window (156: 14 warnings; 157: 15; 158: 9; 0 errors in each) and three of the four syntheses (10-28 C3/C5, 10-29 C3/C7, 10-31 C10) report a repair that stopped at one page. The open decision is the 2026-08-03 NEEDS-HUMAN (methodology ratification) at todo L731, which already holds addenda from both 10-31 legs.
- **Stale-changelog report checked; the live site is fine.** The 10-29 Claude reviewer said the live changelog page served a 10-15 copy. At 16:4xZ today the live page returned HTTP 200 with its top entry at 2026-10-31T14:35:52, which matches the 14:37Z push. Deployment is current. At 4.1 MB of HTML, the page is probably being cached or truncated by the reviewer's fetch tool.

### Convergence Progress

`concepts/` reached its cap (370/370) when depersonalisation-nosology and psychophysical-indexing-law landed on 10-28, so expand-topic can no longer place articles there. `topics/` is at 368/370 by the gate (367 real), `voids/` at 114/125 and `positions/` at 25/90. Five articles were added in the window. Content work was mostly calibration and fold-ins of research. Tenet-check warnings went 14 → 15 → 9 with no errors.

## Changes Applied (Tier 1)

*No changes applied.* `evolution-state.yaml` has no cadence, threshold or weight settings to adjust. The cycle slots and trigger frequencies live in `tools/evolution/cycle.py`, which is code.

Bookkeeping only: `tune_system_history` gained `no_change_runs` entries for 2026-10-26 (backfilled, since that run did not write one) and 2026-10-31. `report`, `last_run`, `last_run_note` and `last_runs.tune-system` were updated in place.

## Recommendations (Tier 2)

Ranked by urgency.

### 1. Agentic-social: rank by lifetime post count and scan voids
- **Proposed change**: in `.claude/skills/agentic-social/scripts/agentic_social_api.py`:
  - add `obsidian/voids` to `CONTENT_DIRS`;
  - order candidates by lifetime post count, ascending, then by oldest last post;
  - exempt candidates with 0–1 lifetime posts from the 7-day topic-overlap test.
- **Rationale**: overrides were needed on 33 of 37 posts, and on every post on 10-31. The never-posted reserve fell from 54 to 25 and runs out in about four days, after which the hand override has nothing better to choose from.
- **Risk**: Low. The overrides already apply this ordering by hand, and posts made that way verified normally.
- **To approve**: code change in the selector.

### 2. Research chain: mint the follow-up for `fold` and run the chain for research-voids
- **Proposed change**:
  - for `fold`, have `chain_note` mint a refine-draft whose File is the host the note names and whose Notes point at the note's fold brief;
  - lift the `cycle_post.py` L402 gate so trigger-kind research-voids runs also chain, honouring the voids cap and the voids-slot NEEDS-HUMAN.
- **Rationale**: 22 of 26 research outputs needed a hand-minted task; that is 17 of 17 folds and 2 of 3 voids notes.
- **Risk**: Low.
- **To approve**: code change in `tools/research/chain.py` and `tools/evolution/cycle_post.py`.

### 3. Highlight deploy gate: wait for a content marker
- **Proposed change**: pass a short marker string from the highlighted change into `_wait_for_deployment`, and require it in the response body, not just HTTP 200.
- **Rationale**: 3 of 4 highlights linked to pages that already existed. The driver now pushes first and polls for the marker by hand.
- **Risk**: Low.
- **To approve**: code change in `tools/highlights/manager.py`.

### 4. Correct stale figures in CLAUDE.md and two todo premises
- **Proposed change**:
  - **CLAUDE.md Section Caps table**: caps 370 / 370 / 125 / 90; counts 368 (367 real) / 370 / 114 / 25.
  - **CLAUDE.md gating path**: `tools.evolution.state.count_section_files`. `tools.evolution.quality` raises ModuleNotFoundError.
  - **CLAUDE.md 24-slot cycle**: 17 queue and 1 coalesce, not 16 and 2.
  - **CLAUDE.md research-voids line**: drop "voids at capacity".
  - **todo L128 header**: "2 of 24 cycle slots" should read 1 of 24.
  - **todo L1492/L1495**: the task quotes voids at 113/115 with "the last two slots"; the live figure is 114/125, 11 free.
- **Rationale**: forks keep reading the stale figures. The driver repeated the coalesce figure this run.
- **Risk**: Low (documentation only).

### 5. Coalesce: gate on a cheap precondition or give up slot 16
- **Proposed change**: before a coalesce slot launches a fork, check whether any affordable, body-linked pair exists (the delta-check method is already documented at todo L128). If none exists, skip without spending a fork. Alternatively, reassign slot 16 to deep-review or queue.
- **Rationale**: 6 of 6 abandons in the window, and 0 affordable pairs again on 10-31. The cost is 4.2% of cycle capacity, half the figure the open entry assumes.
- **Risk**: Low.
- **To approve**: operator decision on the L128 entry, then a code change in `cycle.py` or `cycle_pick.py`.

### 6. Task Notes cite public sources, never session paths
- **Proposed change**: a rule for minting drivers and skills. Notes name the public URL and the verification method (for example, an archive.org identifier with a normalised grep), never a scratchpad path.
- **Rationale**: there are 2 live pointers, and at least 3 forks in the window had to re-fetch sources.
- **Risk**: Low.

## Items for Human Review (Tier 3)

### Loop availability and the weekly limit
- **Issue observed**: 43 h of downtime in 119 h. One outage was the account weekly limit; the other has no recorded cause. The 10-30 outer-review cycle and the 10-29 highlight were lost.
- **Why human needed**: this concerns the account budget and loop throughput, which are not loop parameters.
- **Suggested action**: record the cause of each outage when the loop restarts. Decide whether to buy usage credits or slow the loop near the weekly reset. research-topic, at 26 runs of 14–24 minutes each in the window, is the largest single consumer.

### Gemini abandon cutoff versus the Chrome window
- **Issue observed**: the fourth stall since 10-20. The 4 h cutoff cannot fire inside the window.
- **Suggested action**: as recommended on 10-20, either `min(commissioned + 4h, window_end)` or a stall heuristic (page text unchanged across two collects).

### P3 backlog worked newest-first
- **Issue observed**: 84 of 103 completions were tasks minted in the window, and P3 grew from 228 to 267.
- **Suggested action**: an operator triage pass, or an age weight in queue picking.

### Still open, unchanged since 10-26 (no new incident this window)
- the tune-system min-age gate is unwired;
- task-to-skill drops fields above Notes;
- cycle triggers can pre-empt wall-clock triggers;
- `gemini-2-5-pro` is still the slug in `services.py` L50 and in both Gemini skills, and the ChatGPT collect skill still uses the old DOM selectors;
- the combine skill writes an absolute length ledger;
- the anchoring hedge regex;
- `count_section_files` counts the sidecar;
- the deep-review pool excludes apex, voids and positions;
- `queue_status` is stale;
- the voids bank outnumbers the free voids slots;
- 82 NEEDS-HUMAN headers are open.

## Next Tuning Session

- **Recommended**: 2026-11-30 (30 days). Because the min-age gate is unwired, the every-6-cycles trigger will fire it again around 11-05.
- **Focus areas**:
  - whether the agentic-social reserve ran out before the selector was changed;
  - whether the fold chain was fixed;
  - outage frequency and cause;
  - concepts at cap and topics at 368/370.
