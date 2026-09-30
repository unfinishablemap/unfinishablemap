---
ai_contribution: 100
ai_generated_date: 2026-09-30
ai_modified: 2026-09-30 08:09:14+00:00
ai_system: claude-fable-5-1
author: null
concepts: []
created: 2026-09-30
date: &id001 2026-09-30
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-30 08:09:14+00:00
modified: *id001
related_articles:
- '[[todo]]'
- '[[changelog]]'
title: System Tuning Report - 2026-09-30
topics: []
---

# System Tuning Report

**Date**: 2026-09-30
**Sessions analyzed**: 21721 cumulative; this report covers the 56 loop iterations logged since the 2026-09-27 run (all driven by the `/unfin-cycle` /loop, sessions unfinishablemap-30/34)
**Period covered**: 2026-09-27T06:36Z – 2026-09-30T08:09:14+00:00

## Executive Summary

The system is healthy on every automatic gate: recent_tasks 19/20 success, `failed_tasks` empty, 0 critical issues, 104 of 112 changelog entries since 09-27 are Success and the 4 Abandoned are coalesce declines by design. For the sixteenth consecutive run there is **no Tier 1 lever** (`cadences`, `overdue_thresholds`, `locked_settings`, replenishment weights all absent, grep-verified), and this run fired 3.06 days after the last because the min-age gate is still not enforced on the /loop path. The period's operational cost came from four things outside the tuning surface: a ~9 h Fable usage-limit stall (18:58Z 09-29 → 04:05Z 09-30) that killed an expand-topic fork mid-write and cost the 02:00/03:00 commission slots; a masked replenish gate (all 14 active P0–P2 tasks NEEDS-HUMAN blocked while `count_p0_p2_tasks` read 8); the Gemini Deep Research leg failing again (now 3 of the last 3 cycles); and per-iteration driver repairs of fork pipeline order (changelog entry after sync, changelog frontmatter stamp not aligned) in roughly 60% of iterations.

## Metrics Overview

| Metric | Current | Previous (09-27) | Trend |
|--------|---------|------------------|-------|
| Session count | 21721 | (not recorded) | → |
| recent_tasks success | 19/20 | 19/20 | → |
| failed_tasks | 0 | 0 | → |
| Changelog Success / non-success since prior run | 104 / 8 (4 Abandoned coalesce, 2 Warnings, 2 Complete) | 0 Failed | → |
| Loop-log FAILURE posts since prior run | 1 (commission-gemini 09-30) | 1 (commission-gemini 09-27) | → |
| quality.critical / medium / low | 0 / 10 / 3 | 0 / 10 / — | → |
| Section counts (count_section_files) | topics 335/360, concepts 335/360, voids 111/115, positions 23/80, apex 44 | 332 / 331 / 103 / 23 / 44 | ↑ |
| Queue depth (live parse) | P0 0 / P1 8 / P2 14 / P3 7 (blocked: P2 8, P3 6) | p2 13 / p3 7 (state) | → |
| Coalesce consecutive declines | 27 | 21 | ↑ |
| Gemini leg outcome, last 3 cycles | abandoned, abandoned, commission FAILURE | 3 of 4 failed | ↓ |

## Findings

### Cadence Analysis

- No `cadences` or `overdue_thresholds` keys exist in `evolution-state.yaml` (grep-verified this run, as in the 09-19/09-24/09-27 reports), so cadence analysis has no configured baseline. Observed last_runs are all fresh except three legacy keys (`validate-all`, `tweet-highlight`, `integrate-orphan`) that no longer run as skills.
- tune-system itself fired 4.3d, 3.3d and now 3.06d after its predecessor: the every-6-cycles trigger fires roughly every 3 days at the current loop speed, against the skill's stated monthly cadence. Carried as T2.

### Failure Pattern Analysis

- **Gemini Deep Research**: 09-24 abandoned, 09-25 abandoned, 09-27 commission FAILURE, 09-29 abandoned (stuck at launch, 131 min), 09-30 commission FAILURE ("I encountered an error doing what you asked. Could you try again?" after ~5 min, no research plan). Five consecutive cycles without a collected Gemini review; the last two syntheses ran at 2/3 coverage. Pattern is server-side at the plan stage, not a Chrome/login sentinel. Carried as T4 with raised urgency.
- **Usage-limit stall** (new): the Fable 5.1 limit returned HTTP 429 at 18:58Z 09-29 inside an expand-topic fork, which died after writing its draft but before length-check/register/sync/changelog; the driver session itself was blocked until ~04:05Z 09-30. Cost: the handedness-void draft needed a finish-the-draft refine pass; the 02:00 ChatGPT and 03:00 Claude commissions did not fire on time (the driver ran them at 04:24/04:40, still inside the window). Nothing in the loop detects a stalled driver; the cron ticks queue up and collapse into one iteration on resume. New T8.
- **Fork pipeline order** (extends T5): in this period the driver re-ran `sync.py` after the fork in 5 iterations (fork prepended its changelog entry after syncing, or never synced the changelog/review file) and re-aligned the changelog frontmatter `ai_modified` to the newest entry heading in 11 iterations. No content was lost, but every occurrence is a driver round-trip. The fix is a one-line ordering rule in the per-task skills (Tier 3).
- **Moltbook challenge** (new): one post burned 09-29 17:5x because the agentic-social solver submitted a verb-cued sum where a bare `*` sat between the number-words; the recorded tier rule (bare operator outranks the verb) was applied by hand on the retry and the post landed. The skill's CLI still auto-submits the solver's answer blind. New T9.

### Queue Health Analysis

- **Masked replenish gate confirmed** (T6, urgency raised): at 17:40Z 09-29 cycle_pick returned `queue_empty` while `count_p0_p2_tasks` read 8, because all 14 active tasks were NEEDS-HUMAN blocked and the counter filters on priority only (`tools/evolution/task_selector.py` L75–84: it iterates `parsed["active"]` and tests priority and skip_types, never `status`). Automatic replenishment cannot fire while ≥3 blocked P0–P2 entries exist, and the blocked population only grows. The driver invoked `/replenish-queue` by hand; 6 tasks were minted (2 chain, 3 unconsumed research, 1 staleness).
- Source health since 09-27: chain entries are now being written by research-voids (preference-void, 09-30) and consumed by replenish (assent, handedness); the harvester has found nothing to mint in its last three runs (backlog empty); unconsumed non-voids research remains the deepest well (11 notes from 09-15..09-24 per the 09-29 replenish note).
- Reports-only priority lists (R2): the check-tenets rows went unminted for five reports (140–142) until the driver minted four on 09-30. The outer-review collect/combine path DOES mint (6 tasks on 09-30, 4 upgraded to P1 by combine), so the asymmetry is specific to check-tenets and the pessimistic/optimistic wing reviews. Recommendation R2 renewed with the concrete routing option below.
- Coalesce declined its 26th and 27th consecutive slots (09-29 07:22 and 16:53): topics 0/221 and voids 0/78 affordable pairs at any age; concepts 135 affordable pairs but every evaluated pair fails on role split or human-reserved blocks. R1 renewed.

### Review Finding Patterns

- 30 deep-reviews, 6 pessimistic, 6 optimistic, 8 outer reviews and 4 syntheses since 09-27. The recurring lens is quote fidelity at the primary source: the Chinese Room review found a wrong-work attribution the August review had *introduced* by relocating an objection without checking the destination; the habit review found a paraphrase-as-quote the August review had left open; the Zher-Wen 2023 sweep found BOTH prior ledgers wrong (an invented co-author in one, a dropped co-author in the other). Pattern: metadata-level certification ratifies readings; the fix that works is raw-text retrieval, which today's forks did (wikisource, Gutenberg, OpenAlex inverted index, PubMed esummary).
- Convergent outer-review finding (09-30 synthesis, 2/3 coverage, 8 verified clusters after adjudication excluded 5 reviewer errors): `concepts/galilean-exclusion` reversed the Assayer reading; corrected same day (6930c9c8) with primary-text verification; 5 P1 follow-ups queued.
- check-tenets 142 surfaced a **propagation family**: three tenets-only commits (09-02, 09-04, 09-05) fixed `tenets.md` and left 12 dependents on the old wording. This is the same shape as `tenet-repairs-are-not-propagated-to-their-dependents`; a P1 sweep is now queued.

### Convergence Progress

- Section counts rose in every section over the period (topics +3, concepts +4, voids +8) with all caps intact; voids at 111/115 has 4 slots and one chain entry pending (preference-void). `quality.medium_issues` flat at 10; critical 0. `convergence_targets` are all long since met (min_topics 10 etc.) and no longer discriminate; carried under T1.

## Changes Applied (Tier 1)

*No changes applied* — no Tier 1 lever exists (sixteenth consecutive run; see T1). Recorded in `tune_system_history.no_change_runs`.

## Recommendations (Tier 2)

### R1. Reassign coalesce's 2 cycle slots (renewed, fourth report)
- **Proposed change**: move both coalesce slots in `tools/evolution/cycle.py` to deep-review (or one to a positions-evolve slot); keep coalesce reachable by manual invocation and by a replenish-minted task when a real pair appears.
- **Rationale**: 27 consecutive declines; the pool is arithmetically dead in topics and voids and role-split in concepts. Two of 24 slots (8%) produce a changelog line and nothing else.
- **Risk**: Low. **To approve**: edit the cycle table; no state migration needed.

### R2. Route reports-only priority lists into minting (renewed, with a concrete option)
- **Proposed change**: either let check-tenets mint its ≤4 priority rows itself (as outer-review processing already does), or have replenish-queue read the newest `reviews/tenet-check-*.md` §Priority list as a generator when the queue needs tasks.
- **Rationale**: 14 carried ERRORs sat unminted across five reports until the driver minted by hand on 09-30; the yield of a reports-only review is its priority list.
- **Risk**: Low (cap 4). **To approve**: edit the check-tenets SKILL.md contract or add the generator to replenish.

### R3. Refresh the CLAUDE.md section-cap table (renewed)
- **Proposed change**: topics 335/360, concepts 335/360, voids 111/115, positions 23/80 as of 2026-09-30, with the existing "re-measure before acting" warning kept.
- **Risk**: None. **To approve**: edit CLAUDE.md.

### R4. Make `count_p0_p2_tasks` status-aware (promoted from T6)
- **Proposed change**: exclude tasks whose Status is blocked / NEEDS-HUMAN from the count (or count them separately) so the replenish gate reflects executable depth.
- **Rationale**: the masked gate is no longer theoretical — it fired on 09-29 and required a manual replenish; the blocked population (14 then, 14 now) only grows.
- **Risk**: Low; one filter in `task_selector.py` plus a test. **To approve**: code change.

### R5. Add a driver stall sentinel
- **Proposed change**: have `cycle_post` write a heartbeat timestamp the loop log already carries, and have the 08:00 add-highlight path (or a cheap wall-clock check) log a WARN when the last post is older than 3× the loop interval; optionally re-fire missed commission triggers once if still inside the Chrome window.
- **Rationale**: the 9 h usage-limit stall was invisible until the queued ticks arrived; the commissions were only recovered because the stall ended before 07:00.
- **Risk**: Low. **To approve**: code change in `tools/evolution/`.

## Items for Human Review (Tier 3)

### T1. Create `cadences` / `overdue_thresholds`, or rewrite tune-system to match reality (carried, fourth report)
- **Issue observed**: the skill's only automatic levers act on keys the state file does not have; sixteen consecutive zero-Tier-1 runs.
- **Suggested action**: either add the keys (with locked_settings for the intentional ones) or rewrite the skill's Tier 1 table around levers that exist (cycle slot table, MIN_QUEUE_TASKS, replenish caps).

### T2. Enforce the tune-system min-age gate on the /loop path (carried)
- **Issue observed**: fires every ~3 days at current loop speed against a monthly contract.
- **Suggested action**: gate the cycle trigger in `cycle_pick` on `last_runs["tune-system"]` age ≥ 30 days.

### T3. Chrome skill UI and timing drift (carried, new evidence)
- **Issue observed**: screenshot scale measured 0.665, 0.665, 0.665 and 1.0 across four launches on 09-30; click coordinates are in the screenshot frame on this extension version (a DOM-rect click landed on the wrong element). ChatGPT: no `#prompt-textarea`, `[data-message-author-role]` returns 0, the assistant turn lives in one `[data-turn-key]` div; composer is `div.ProseMirror[contenteditable]` labelled by the project name. Gemini: Deep Research back at the top level of the "+" menu; menuitem enumeration returns empty for ~1–2 s while the menu animates. claude.ai: project default model is now Opus 5.5 Medium (the "Opus 4.8" prose in CLAUDE.md and the skills table is stale).
- **Suggested action**: one pass over the six Chrome skills to (a) measure scale per run and multiply DOM rects, (b) replace the retired selectors, (c) add a re-poll grace window, (d) update the model prose.

### T4. Gemini leg failing (carried, urgency raised)
- **Issue observed**: no collected Gemini review in five cycles; two syntheses at 2/3 coverage.
- **Suggested action**: decide whether to keep the leg (retry once in a fresh conversation on the next tick when the failure is the plan-stage server error), replace Deep Research with the plain Pro model for this leg, or accept 2/3 coverage and mark the leg optional in combine.

### T5. Fork pipeline order and stamp discipline (carried, quantified)
- **Issue observed**: 5 re-syncs and 11 changelog-stamp alignments by the driver in 56 iterations.
- **Suggested action**: add to the shared skill preamble: "prepend the changelog entry and set its frontmatter `ai_modified` to the entry timestamp BEFORE running sync; sync last". Tier 3 because it edits SKILL.md files.

### T6. `outer-todo.md` code-fence example reads as a live task
- **Issue observed**: L36 "### P1: How robust is the dualism-as-ai-risk-mitigation argument…" sits inside the fenced "How to add a task" example (fence L35–40); a `^### P` grep — including the driver's — mistakes it for the queue's only open entry. The commission skill's selector handled it correctly.
- **Suggested action**: change the example's heading to a non-matching form (e.g. `### P{N}: …`) or move it below a comment.

### T7. Refine briefs should name the claim, not the sentence (carried)

### T8. Usage-limit resilience (new)
- **Issue observed**: a 429 "Fable limit" inside a fork kills it mid-pipeline; the driver session then stalls until the limit lifts, with no record in state.
- **Suggested action**: decide whether forks should fall back to another model on 429 (attribution then needs the plus-joined `ai_system` form) or whether the loop should simply pause with a state marker; and whether cron ticks that pile up during a stall should be de-duplicated.

### T9. Moltbook solver submits blind (new)
- **Issue observed**: the agentic-social CLI `post` auto-solves and auto-submits; the recorded challenge tiers (bare operator between number-words outranks the verb; dimension mismatch; no derived numerals) live only in memory and driver briefs. One post burned 09-29.
- **Suggested action**: add a `--no-auto-verify` path or encode the tiers in `solve_challenge` (operator territory per the memory note).

### T10. Apex pieces without `## Evidence and Dependency` (new, already NEEDS-HUMAN)
- **Issue observed**: 14 of 44 apex articles lack the required section; apex is outside the deep-review pool, so nothing automated reaches them except apex-evolve's staleness pick (one per trigger).
- **Suggested action**: the standing NEEDS-HUMAN entry at todo.md L1254 reserves this sequencing; approve a capped apex-evolve sweep or leave it.

## Next Tuning Session

- **Recommended**: 2026-10-30 (30 days out). If T2 is not fixed, the next run will fire within days and should again record only.
- **Focus areas**: whether R4 landed (masked gate), Gemini leg decision (T4), Chrome skill drift pass (T3), and whether the five P1 galilean-exclusion / tenet-propagation sweeps executed without dropped files.