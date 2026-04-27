---
title: "System Tuning Report - 2026-04-27"
created: 2026-04-27
modified: 2026-04-27
human_modified: null
ai_modified: 2026-04-27T12:55:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[todo]]"
  - "[[changelog]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-7
ai_generated_date: 2026-04-27
last_curated: null
---

# System Tuning Report

**Date**: 2026-04-27
**Sessions analyzed**: 144 (sessions 6275 → 6419)
**Period covered**: 2026-04-24 02:46 UTC → 2026-04-27 12:50 UTC (~82 hours / 3.4 days)

## Executive Summary

17th consecutive zero-hard-failure period (150 tasks, 0 failures). Substantial creation pressure on voids: agency-void coalesce (involuntariness-void + agency-verification-void → agency-void) plus an additional voids merge brought the count to 97/100, three slots remaining. P2 queue depth dropped 5 → 2 as chains discharged; P3 grew 422 → 454 (+32, ~9.4/day, same generation rate as last period). The same structural blockers persist: `cadences`, `overdue_thresholds`, `tune_system_history`, `locked_settings` and `replenishment_config` sections still absent from evolution-state.yaml. **31st consecutive report unable to apply Tier 1 changes.** New observation this period: the W17 archive rollover at 2026-04-27 01:48 UTC truncated the active changelog to ~13h of recent entries — mechanism is working as designed and frees the file from unbounded growth.

## Metrics Overview

| Metric | Current (Actual) | Recorded State | Previous (Apr 24) | Trend |
|--------|------------------|----------------|-------------------|-------|
| Session count | 6419 | 6419 | 6275 | +144 |
| Topics | 232 | 35 | 232 | → |
| Concepts | 231 | 145 | 227 | **+4** |
| Voids | 97 | 11 | 96 | **+1** (creation > coalesce) |
| Apex | 22 | 4 | 22 | → (still over 20 cap) |
| Arguments | 6 | 4 | 6 | → |
| Questions | 1 | 1 | — | → |
| Research | 364 | 117 | 358 | +6 |
| Reviews | 3546 | 542 | 3449 | +97 (~28/day) |
| Total content files | 297 | 297 | 297 | → |
| Critical issues | 0 | 0 | 0 | → |
| Medium issues | 10 | 10 | 10 | → (persistent) |
| Low issues | 3 | 3 | 3 | → |
| Orphaned files | 13 | 13 | 13 | → (persistent) |
| Queue depth (P0–P1) | 0 | — | 0 | → |
| Queue depth (P2) | 2 | — | 5 | **−3** (chains discharged) |
| Queue depth (P3) | 454 | — | 422 | +32 |

**State discrepancy**: Recorded `progress` counters remain frozen at early-project values (35 topics, 145 concepts, 11 voids, 117 research, 542 reviews). **34th consecutive report.** No functional harm — caps enforced via `section_caps` not `progress`.

## Abort Conditions Check

**Status**: All clear.

- Task failure rate: 0% (0/20 recent_tasks failed; `failed_tasks: {}`; 150/150 changelog entries in period report Success)
- Convergence: quality unchanged; no regression
- Critical issues: 0
- File reads: all successful

## Check Locked Settings

`locked_settings` section not present in evolution-state.yaml. **31st consecutive report.**

## Findings

### Cadence Analysis

**Data points**: 144 sessions, 150 changelog entries (52 in active changelog + 98 in W17 archive), 82 hours elapsed.

| Task | last_runs Timestamp | Actual Last Run (verified) | Status |
|------|---------------------|----------------------------|--------|
| validate-all | 2026-01-24 02:57 | Not run since Jan 24 | **94 days stale** |
| pessimistic-review | 2026-04-27 07:58 | 2026-04-27 07:58 UTC | Current |
| optimistic-review | 2026-04-27 09:28 | 2026-04-27 09:28 UTC | Current |
| check-tenets | 2026-04-26 18:22 | **2026-04-27 12:38** (changelog) | **Stale writeback — 18h** |
| check-links | 2026-04-27 00:22 | 2026-04-27 00:22 UTC | Current |
| deep-review | 2026-04-27 11:28 | 2026-04-27 12:13 UTC (last in period) | Stale writeback — ~45m |
| tune-system | 2026-04-24 02:28 | 2026-04-24 02:46 UTC | ~82h since last |
| research-voids | 2026-04-27 00:22 | **2026-04-27 12:33** (changelog) | **Stale writeback — 12h** |
| coalesce | 2026-04-27 11:58 | 2026-04-27 05:59 UTC (last successful) | Writeback ahead-of-fact (skip-no-candidates) |
| apex-evolve | 2026-04-26 02:28 | **2026-04-27 12:43** (changelog) | **Stale writeback — 34h** |
| agentic-social | 2026-04-27 11:58 | 2026-04-27 11:58 UTC | Current |
| tweet-highlight | 2026-01-24 14:00 | Not recently | 94 days stale |

**Continuing finding — `last_runs` writeback still incomplete**: Three cycle-trigger tasks (check-tenets, research-voids, apex-evolve) have writeback gaps of 12–34h this period. Pattern is now confirmed across **3 consecutive reports** as systematic, not transient. Coalesce shows the inverse pattern: state advances on cycle ticks even when no candidate is found and no actual coalesce runs (writeback ahead-of-fact). Both symptoms suggest the cycle-trigger dispatch path is updating timestamps before/around invocation rather than after task completion. Root cause lives in `tools/evolution/` dispatch code.

**`validate-all`**: 94 days stale. **26th consecutive report.**

**`tune-system` cadence**: 82h interval this period vs 62h last, both well under the skill's documented 30-day cadence. Slight deceleration this period (the loop interval may have lengthened, or cycle position drift) but still ~9× faster than spec. **31st consecutive report noting the mismatch.** Recommendation unchanged: raise the cycle-trigger threshold (e.g., to every 30 cycles) OR revise the skill spec to match observed cadence.

### Failure Pattern Analysis

**Data points**: 150 changelog entries in period; `failed_tasks: {}`; all 20 recent_tasks success.

| Task Type | Executed | Skipped/Abandoned | Rate |
|-----------|----------|-------------------|------|
| deep-review | 82 | 0 | 0% |
| refine-draft | 15 | 0 | 0% |
| expand-topic | 10 | 0 | 0% |
| coalesce | 10 | 0* | 0% |
| condense | 8 | 0 | 0% |
| pessimistic-review | 6 | 0 | 0% |
| optimistic-review | 6 | 0 | 0% |
| research-voids | 3 | 0 | 0% |
| research-topic | 3 | 0 | 0% |
| cross-review | 2 | 0 | 0% |
| check-tenets | 2 | 0 | 0% |
| apex-evolve | 2 | 0 | 0% |
| replenish-queue | 1 | 0 | 0% |

*Coalesce no-candidate tickless events appear in `git log` (commits like 70cdc370b "no candidates found" and 8ce67e835 "no merge in voids section") but are not surfaced as changelog entries. Cycle position advanced on those ticks.

**Hard-failure reliability**: 17th consecutive zero-failure tune period.

**Deep-review near-zero-change convergence persists**: Multiple stability-confirmation deep-reviews this period (`placebo-effect-and-mental-causation` -0 net at 7th review, `machine-question` -0 at 3rd review, `social-construction-of-self-vs-phenomenal-self` -0 at 5th review, `responsibility-gradient-from-attentional-capacity` -0 at 4th review, `contemplative-pathology-and-interface-malfunction` -0 at 3rd review). At least 5 of the 82 deep reviews this period made no content change. Recommendation #6 (per-article review-count tracking) still stands and is becoming more load-bearing.

### Queue Health Analysis

**Data points**: Current todo.md (5057 lines, 456 tasks; P2=2, P3=454, vetoed=1).

| Priority | Active Count | Change |
|----------|--------------|--------|
| P0 | 0 | → |
| P1 | 0 | → |
| P2 | 2 | **−3** (chains discharged) |
| P3 | 454 | **+32** |

**P2 thinning**: 5 → 2 in 82h. The 2026-04-23/24 chain (deep-review + 2 cross-review tasks from the meta-voids cluster) executed and cleared. With only 2 P2 tasks remaining and 0 P0/P1, the queue is effectively pulling from P3 indirectly through chain regeneration. Replenishment trigger fired once this period (replenish-queue at 2026-04-26 02:29 UTC adding 4 P2 tasks; subsequent runs added 5 + 3 P2 tasks per `git log` evidence — those weren't logged to changelog because the active changelog was rolled to W17 mid-period). Worth verifying that replenish-queue invocations are being captured in the post-rollover changelog cleanly.

**P3 overhang growing steadily**: 422 → 454 in 82h (+32; ~9.4/day, indistinguishable from last period's 9/day rate). Optimistic-review remains the dominant generator (6 optimistic-reviews this period × ~5 tasks each ≈ 30 P3 additions). Threshold-of-concern question still open (last report flagged 500 as a candidate ceiling).

**Section-cap pressure on voids**: 96 → 97 (one creation net of one coalesce). Down to 3 slots. Coalesce ran 10× this period across all sections; voids-coalesce specifically ran twice (involuntariness+agency-verification → agency-void on 2026-04-27 05:59 UTC, plus an earlier merger I couldn't pin precisely from the active changelog window). Continued creation at this rate plus capped capacity will force more aggressive coalescing.

### Review Finding Patterns

**Data points**: 6 pessimistic reviews, 6 optimistic reviews, 2 tenet checks, 82 deep reviews (period), tune-system reports growing to 30+ in calendar 2026.

**Tenet check zero-warning streak extends**: 2026-04-27 12:38 UTC produced **0 errors, 0 warnings, 1 note** on a 28-file delta sweep. The single note: `topics/free-will.md` wikilink alias `[[tenets#^dualism|substance dualism]]` characterizes the tenet's neutrality between substance and property dualism imprecisely. Substantive position defensible; presentation slightly overreaches. Low-priority correction. **6th consecutive zero-error tenet check.** Corpus continues to hold tenet-alignment high-water mark.

**Pessimistic→refine pipeline remains tight**: 2026-04-27 07:58 pessimistic on `voids/agency-void` (post-coalesce) → 08:14 refine-draft addressed two High-severity issues plus the description-frontmatter overclaim → 10:29 follow-up refine-draft addressed deferred Medium-severity issues. ~16-min and ~145-min turnarounds; no review-finding rotted on the queue.

**LLM cliché "Not X but Y" construct**: Continues to be hunted at review time. 2026-04-27 09:44 deep-review of `voids/mood-void` rewrote two banned constructs. 2026-04-27 09:58 deep-review of `voids/erasure-void` rewrote two more. 2026-04-27 10:58 deep-review of `apex/what-it-might-be-like-to-be-an-ai` rewrote two further instances. The pattern is being generated routinely at expand-topic time and only cleaned at deep-review time. **11th consecutive period flagging this.**

**Apex re-synthesis silent regression**: 2026-04-27 12:13 deep-review of `apex/identity-across-transformations` caught that the 2026-04-17 apex-evolve re-synthesis silently regressed two prior fixes (Mashour 2023 reference mismatch reintroduced; process-haecceitism cross-link lost). Reviewer added a caveat that future re-syntheses should consult latest deep-review enhancements before regenerating. **NEW pattern this period.** Worth watching: if re-synthesis regularly drops review-installed corrections, the deep-review→apex-evolve interaction becomes a content-loss vector.

**HTML refinement-log self-removal flagged at multiple sites**: 2026-04-27 09:44 (mood-void) and 10:58 (apex/what-it-might-be-like-to-be-an-ai) both removed AI refinement-log HTML comment blocks that the prior refine-draft had self-flagged for removal "after human review". The marker is being placed and not auto-removed; deep-review is doing the removal. Either remove the marker (so refine-draft removes the log itself) or escalate the marker to a structured task type.

### Convergence Progress

| Category | Count | Cap | % of Cap | Direction |
|----------|-------|-----|----------|-----------|
| Topics | 232 | 250 | 92.8% | 18 slots (→) |
| Concepts | 231 | 250 | 92.4% | 19 slots (−4 vs prev) |
| Voids | 97 | 100 | **97.0%** | 3 slots (−1 vs prev) |
| Arguments | 6 | — | — | → |
| Apex | 22 | (20 governance) | — | **22/20 — over cap** |

**Voids pressure**: 96 → 97. Three slots remaining. Next research-voids tasks may be auto-skipped if voids fills further; per CLAUDE.md, `/research-voids` skips when voids is at capacity. Monitoring the coalesce vs creation ratio — this period was net +1 (creation slightly outpaced coalesce in voids).

**Concepts +4**: 227 → 231 over 82h. New articles include `concepts/hard-problem-of-content` (created 2026-04-27 00:34) and `concepts/status-of-content` (per `git show HEAD~57 --stat`). Concept-extraction methodology continues to operate (see optimistic-2026-04-26b).

**Apex 22/20 discrepancy unchanged**: Same as last 2 periods. Last period's new finding remains unresolved.

**Quality metrics (frozen, 34th period)**:
- Critical: 0 ✓ (target)
- Medium: 10 (target ≤3) — almost certainly stale counter
- Low: 3
- Orphans: 13

## Changes Applied (Tier 1)

*No changes applied.*

**Rationale**: Same three structural blockers as the last 30 reports:
1. No `cadences` / `overdue_thresholds` / `replenishment_config` sections in evolution-state.yaml — nothing to tune.
2. No `tune_system_history` — cooldowns unenforceable.
3. No `locked_settings` — cannot check for human overrides.

**31st consecutive report** unable to apply Tier 1 changes for this structural reason. The skill's specified operating surface (YAML parameters) does not exist in the current state file; operational parameters live in `tools/evolution/` Python code and are out of scope for this skill.

## Recommendations (Tier 2)

### 1. Fix `last_runs` Writeback for Cycle-Trigger Tasks (Carried Forward ×3)

- **Proposed change**: Audit the dispatch code in `tools/evolution/` that persists `last_runs` after task completion. check-tenets (18h stale), research-voids (12h stale), and apex-evolve (34h stale) all show writeback lag this period. Coalesce shows the opposite (writeback ahead-of-fact on no-candidate ticks).
- **Rationale**: The pattern is now confirmed across three consecutive reports — systematic, not transient. Stale `last_runs` corrupts trigger gating; writeback-ahead-of-fact creates phantom freshness. The two failure modes likely share a root cause (timestamp updates wired to the cycle tick rather than to task-completion events).
- **Risk**: Low (read the code; single-point fix in `tools/evolution/cycle.py` dispatch).
- **Priority**: Medium-High.

### 2. Fix Stale `content_stats` / `progress` Counters (Carried Forward ×29)

- **Proposed change**: Add per-section file-counting at session start in `tools/evolution/state.py`.
- **Rationale**: 34th consecutive report. Recorded state shows 35 topics (actual 232), 145 concepts (actual 231), 11 voids (actual 97), 542 reviews (actual 3546). No functional harm (caps use separate live counts) but every metric-dependent skill has to recompute from filesystem.
- **Risk**: Low.
- **Priority**: Medium.

### 3. Add `tune_system_history` / `locked_settings` / `cadences` Sections (Carried Forward ×31)

- **Proposed change**: Populate evolution-state.yaml with the sections the skill spec expects: `cadences`, `overdue_thresholds`, `replenishment_config`, `tune_system_history`, `locked_settings`.
- **Rationale**: Without these, tune-system cannot make Tier 1 changes safely. 31 reports now effectively advisory-only.
- **Risk**: Low.
- **Priority**: High.

### 4. Add `validate-all` to Cycle Triggers (Carried Forward ×26)

- **Proposed change**: Add `"validate-all": 2` or similar to `CYCLE_TRIGGERS` in `tools/evolution/cycle.py`.
- **Rationale**: 94 days stale. Listed in CLAUDE.md as "Daily health check" but not wired into automation.
- **Risk**: Low (read-only check).
- **Priority**: Medium.

### 5. Reconcile tune-system Cadence (Carried Forward ×4)

- **Proposed change**: Either (a) adjust the cycle trigger from "every 6 cycles" to "every 30 cycles" (approaches the 30-day documented cadence), or (b) revise the skill spec to 3-day cadence matching current operation.
- **Rationale**: Current ~82h cadence is 9× faster than documented. Each run covers small deltas; most findings are carried forward. Moving to monthly would cut cost ~9× with minimal signal loss, since no new infrastructure findings have emerged in ~31 reports.
- **Risk**: Low.
- **Priority**: Medium.

### 6. Implement Deep-Review Convergence Tracking (Carried Forward ×20)

- **Proposed change**: Track per-article review count and last word-change delta; skip further deep-review for articles with 3+ reviews all showing near-zero net change.
- **Rationale**: At least 5/82 deep-reviews this period made no content change (placebo-effect-and-mental-causation 7th review zero-change; machine-question 3rd; social-construction-of-self-vs-phenomenal-self 5th; responsibility-gradient-from-attentional-capacity 4th; contemplative-pathology-and-interface-malfunction 3rd). Reviewers annotate "stability confirmed" but re-queuing continues. Becoming more load-bearing as more articles converge.
- **Risk**: Low.
- **Priority**: High.

### 7. Audit Apex Cap Governance (Carried Forward ×3)

- **Proposed change**: Resolve the 22-vs-20 apex count discrepancy: `obsidian/apex/` contains 22 files; apex-articles.md's governance list caps at 20.
- **Rationale**: Inconsistent governance means apex-evolve decisions may treat real files as nonexistent.
- **Risk**: Low.
- **Priority**: Medium.

### 8. Update `convergence_targets` (Carried Forward ×33)

- **Proposed change**: `min_topics` 10→200, `min_concepts` 15→200, `min_arguments` 5→10, add `min_voids` 80, add `min_apex` 15, `max_medium_issues` 3 → 15.
- **Rationale**: Targets set for early-stage system; all vastly exceeded. Cosmetic.
- **Risk**: Low.
- **Priority**: Low.

### 9. Auto-Remove HTML Refinement-Log Markers (NEW this period)

- **Proposed change**: Either (a) remove the AI refinement-log HTML comment marker from refine-draft outputs entirely, or (b) wire refine-draft to remove the log block in a follow-up pass when the previous-state-recorded review has cleared.
- **Rationale**: The pattern of "log self-marks for removal after human review; deep-review later removes it" generates avoidable churn. 2 deep-reviews this period (mood-void, what-it-might-be-like-to-be-an-ai) cleaned this up; one of the latter (10:58) noted the previous review had also claimed to do it but the block had been re-added — i.e. the marker is being regenerated. Either kill the marker or make refine-draft itself responsible for removal.
- **Risk**: Low (formatting change, no semantic impact).
- **Priority**: Medium.

### 10. Investigate Apex Re-Synthesis Regression Path (NEW this period)

- **Proposed change**: When apex-evolve re-synthesises an article, surface diffs against the latest deep-review-installed corrections so the re-synthesis can preserve them.
- **Rationale**: 2026-04-27 12:13 deep-review of `apex/identity-across-transformations` caught that the 2026-04-17 apex-evolve re-synthesis silently regressed two prior fixes (Mashour 2023 reference mismatch reintroduced; process-haecceitism cross-link lost). If this is a structural feature of how apex-evolve regenerates from sources rather than diffing-and-patching, it's a content-loss vector. The deep-review's caveat ("future re-syntheses should consult latest deep-review enhancements") is a workaround placed in the article, not a fix.
- **Risk**: Medium (touches apex-evolve methodology).
- **Priority**: Medium.

## Items for Human Review (Tier 3)

### 1. Stale State Tracking — 34th Consecutive Report

- **Issue observed**: `content_stats.total_files` and `progress.*` counters frozen at early-project values.
- **Why human needed**: Code change to `tools/evolution/state.py`.
- **Suggested action**: Add per-section file-counting at session start.

### 2. `last_runs` Writeback Gap for Cycle-Trigger Tasks (Carried Forward ×3)

- **Issue observed**: Three cycle-trigger tasks show 12–34h writeback lag this period (check-tenets, research-voids, apex-evolve). Coalesce shows the inverse (timestamps advance ahead-of-fact on no-candidate ticks). Pattern is now systematic across three consecutive reports.
- **Why human needed**: Code inspection of `tools/evolution/cycle.py` and related task dispatch paths.
- **Suggested action**: Find the dispatch branch for cycle-trigger tasks and ensure it calls `state.update_last_run(task_name, now)` after task completion (not at cycle tick).

### 3. Medium Issues Persistent at 10 (Carried Forward ×25)

- **Issue observed**: Medium issues count exactly 10 for 25 consecutive tune periods.
- **Why human needed**: Decide whether this is a stale counter or live tracking.
- **Suggested action**: Inspect the source of `quality.medium_issues` and confirm it is recomputed at session start.

### 4. Orphaned Files Persistent at 13 (Carried Forward ×12)

- **Issue observed**: Same 13-orphan count through extensive cross-linking work.
- **Why human needed**: Almost certainly stale detection.
- **Suggested action**: Re-run orphan detection against live file state and verify.

### 5. Apex Cap Inconsistency (Carried Forward ×3)

- **Issue observed**: `obsidian/apex/` contains 22 files; apex-articles.md caps at 20.
- **Why human needed**: Editorial/governance decision.
- **Suggested action**: Reconcile the approved list against the filesystem; archive overflow or update cap.

### 6. tune-system Cycle-vs-Cadence Mismatch (Carried Forward ×4)

- **Issue observed**: Skill documents 30-day cadence; cycle trigger fires every ~3 days (82h this period, 62h last).
- **Why human needed**: Pick a cadence. Current mismatch generates ~9× the intended reports.
- **Suggested action**: Either relax cycle trigger to every 30 cycles or update the skill spec.

### 7. P3 Overhang Growth (Carried Forward ×2)

- **Issue observed**: P3 queue depth grew 422 → 454 (+32 in 82h, ~9.4/day, same rate as last period). P2/P3 promotion rate near zero; execution ratio far below generation ratio.
- **Why human needed**: Decide whether P3 is functioning as a suggestion buffer (current behaviour — generated but rarely executed) or a true work queue (would need promotion heuristics or a ceiling).
- **Suggested action**: Either (a) add a P3 ceiling to `replenish-queue` (e.g., halt optimistic-review P3 generation if P3 > 500), or (b) accept P3 as archival and document that in CLAUDE.md.

### 8. Apex Re-Synthesis Content-Loss Vector (NEW)

- **Issue observed**: 2026-04-27 12:13 deep-review of `apex/identity-across-transformations` documented that the 2026-04-17 apex-evolve re-synthesis silently regressed two prior fixes (factual reference correction, cross-link). The deep-review installed a caveat in the article asking future re-syntheses to consult latest enhancements first.
- **Why human needed**: Decide whether apex-evolve should diff-and-patch rather than regenerate, or whether it's acceptable for deep-review to act as a periodic guard.
- **Suggested action**: Inspect apex-evolve's source-handling logic; if it regenerates from underlying sources without preserving review-installed deltas, consider switching to a patch-style update.

## System Health Summary

| Component | Status | Notes |
|-----------|--------|-------|
| Task execution | **Excellent** | 0% hard-failure rate (17th consecutive period; 150/150) |
| Skip rate | Excellent | 0 skips/abandons in the period |
| Content quality | Excellent | 0 critical issues; 0 tenet errors/warnings (1 low-priority note) |
| Queue management | Mixed | P2 thinned to 2 (chains discharged); P3 still growing (+32) |
| Expand-topic efficiency | Excellent | 10/10 success |
| Coalesce efficiency | Excellent | 10/10 success |
| Review system | Excellent | ~28 reviews/day; pessimistic→refine pipeline tight (16-min turnaround) |
| Deep-review convergence | Mixed | At least 5/82 zero-change reviews this period |
| Scheduling | Operational | Cycle mechanism stable but ~9× faster than spec |
| Changelog rotation | **Working** | W17 archive rolled at 2026-04-27 01:48 UTC; mechanism functional |
| State tracking | **Broken** | content_stats/progress stale (34th); `last_runs` writeback (3rd period systematic) |
| Topics cap | Healthy | 232/250 — 18 slots |
| Concepts cap | Healthy | 231/250 — 19 slots |
| Voids cap | **Tight** | 97/100 — 3 slots |
| Apex cap | **Inconsistent** | 22 files vs 20 approved (3rd period) |
| Site validation | **Gap** | validate-all not running (94 days; 26th report) |
| Tenet alignment | **Excellent** | 0/0/1 (note only) on 28-file delta |
| Pessimistic→refine pipeline | **Excellent** | 16-min turnaround on agency-void cluster |
| Apex re-synthesis | **Watch** | Silent regression of prior fixes detected (NEW finding) |
| tune-system infrastructure | **Blocked** | 31st report unable to apply Tier 1 |

## Next Tuning Session

- **Expected (at current cycle-trigger rate)**: ~2026-04-30 (3 days out)
- **Recommended per skill spec**: 2026-05-27 (30 days out)
- **Focus areas next run**:
  - Whether `last_runs` writeback gap has been addressed (now confirmed systematic across 3 periods)
  - Whether voids capacity reaches 98 or 99 (3 slots remaining; pressure rising)
  - Whether P3 overhang stabilises or keeps growing past 500
  - Whether apex count reconciled against governance list (22 vs 20)
  - Whether stale state tracking gets addressed (35th report)
  - Whether `tune_system_history` / `locked_settings` / `cadences` sections appear (32nd report)
  - Whether validate-all is integrated (27th report)
  - Whether apex re-synthesis regression pattern recurs on next apex-evolve run
  - Whether HTML refinement-log marker is removed from refine-draft outputs
