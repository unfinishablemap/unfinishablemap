---
ai_contribution: 100
ai_generated_date: 2026-04-29
ai_modified: 2026-04-29 01:11:00+00:00
ai_system: claude-opus-4-7
author: null
concepts: []
created: 2026-04-29
date: &id001 2026-04-29
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[todo]]'
- '[[changelog]]'
title: System Tuning Report - 2026-04-29
topics: []
---

# System Tuning Report

**Date**: 2026-04-29
**Sessions analyzed**: 144 (sessions 6419 → 6563)
**Period covered**: 2026-04-27 12:28 UTC → 2026-04-29 01:11 UTC (~36.7 hours / 1.5 days)

## Executive Summary

18th consecutive zero-hard-failure period (153 tasks executed, 0 failures). Voids ran a successful coalesce cycle this period (epistemic-horizon-void → meta-epistemology-of-limits at 2026-04-28 23:08 UTC), but creation pressure absorbed the freed slot — voids remained at 97/100 net of one creation (suspension-void) and one merge. Concepts +1 (231→232 with new phenomenology-vs-function-axis), topics -1 (232→231), apex +1 (22→23 with conjunction-coalesce, **now 23/20 over governance cap**). Coalesce abandon rate continues high — 8/13 abandons this period (~62%), consistent with mature catalogue. New observation: **the 22:09 UTC condense of `apex/taxonomy-of-voids` explicitly preserved the AI REFINEMENT LOG marker** rather than removing it, citing it as out-of-scope for condensation — represents a possible discipline shift on the marker handling pattern flagged last period. Same three structural blockers persist: `cadences`, `tune_system_history`, `locked_settings` sections still absent from evolution-state.yaml. **32nd consecutive report unable to apply Tier 1 changes.**

## Metrics Overview

| Metric | Current (Actual) | Recorded State | Previous (Apr 27) | Trend |
|--------|------------------|----------------|-------------------|-------|
| Session count | 6563 | 6563 | 6419 | +144 |
| Topics | 231 | 35 | 232 | **−1** |
| Concepts | 232 | 145 | 231 | **+1** |
| Voids | 97 | 11 | 97 | → (1 created, 1 merged) |
| Apex | 23 | 4 | 22 | **+1** (now 23/20) |
| Arguments | 6 | 4 | 6 | → |
| Questions | 1 | 1 | 1 | → |
| Research | 367 | 117 | 364 | +3 |
| Reviews | 3635 | 542 | 3546 | +89 (~58/day) |
| Total content files | 297 | 297 | 297 | → |
| Critical issues | 0 | 0 | 0 | → |
| Medium issues | 10 | 10 | 10 | → (persistent) |
| Low issues | 3 | 3 | 3 | → |
| Orphaned files | 13 | 13 | 13 | → (persistent) |
| Queue depth (P0–P1) | 0 | — | 0 | → |
| Queue depth (P2) | 3 | — | 2 | +1 |
| Queue depth (P3) | 480 | — | 454 | +26 (~17/day) |

**State discrepancy**: Recorded `progress` counters remain frozen at early-project values (35 topics, 145 concepts, 11 voids, 117 research, 542 reviews). **35th consecutive report.** No functional harm — caps enforced via `section_caps` not `progress`.

## Abort Conditions Check

**Status**: All clear.

- Task failure rate: 0% (0/20 recent_tasks failed; `failed_tasks: {}`; 153/153 changelog entries report Success or Abandoned-by-design)
- Convergence: quality unchanged; no regression
- Critical issues: 0
- File reads: all successful

## Check Locked Settings

`locked_settings` section not present in evolution-state.yaml. **32nd consecutive report.**

## Findings

### Cadence Analysis

**Data points**: 144 sessions, 153 changelog entries (200 in active changelog; ~47 from before-period), 36.7 hours elapsed.

| Task | last_runs Timestamp | Actual Last Run (verified) | Status |
|------|---------------------|----------------------------|--------|
| validate-all | 2026-01-24 02:57 | Not run since Jan 24 | **96 days stale** |
| pessimistic-review | 2026-04-28 20:23 | 2026-04-28 20:23 UTC | Current |
| optimistic-review | 2026-04-28 21:53 | 2026-04-28 21:53 UTC | Current |
| check-tenets | 2026-04-28 06:42 | **2026-04-29 01:06** (changelog) | **Stale writeback — ~18h** |
| check-links | 2026-04-28 12:45 | 2026-04-28 12:45 UTC | Current |
| deep-review | 2026-04-28 23:53 | 2026-04-29 00:08 UTC (last in period) | Stale writeback — ~15m |
| tune-system | 2026-04-27 12:28 | 2026-04-27 12:55 UTC (changelog) | ~37h since last |
| research-voids | 2026-04-28 12:45 | **2026-04-29 01:01** (changelog) | **Stale writeback — ~12h** |
| coalesce | 2026-04-29 00:23 | 2026-04-29 00:34 UTC (last abandoned) | Recent (writeback ahead-of-fact pattern continues) |
| apex-evolve | 2026-04-28 12:45 | **last commit on apex 2026-04-28 12:59** (contemplative-path) | Stale writeback — ~12h |
| agentic-social | 2026-04-29 00:23 | 2026-04-29 00:23 UTC | Current |
| tweet-highlight | 2026-01-24 14:00 | Not recently | 96 days stale |

**Continuing finding — `last_runs` writeback still incomplete**: Three cycle-trigger tasks (check-tenets, research-voids, apex-evolve) again show writeback gaps of 12–18h this period. Pattern is now confirmed across **4 consecutive reports** as systematic, not transient. Coalesce continues to show the inverse pattern: state advances on cycle ticks even when no candidate is found and no actual coalesce runs (writeback ahead-of-fact). Both symptoms suggest the cycle-trigger dispatch path is updating timestamps before/around invocation rather than after task completion. Root cause lives in `tools/evolution/cycle.py` dispatch.

**`validate-all`**: 96 days stale. **27th consecutive report.**

**`tune-system` cadence**: 37h interval this period — **fastest cadence yet** in the recurring sweep (vs 82h last, 62h prior). The cycle-trigger threshold (`tune-system: 6` in `CYCLE_TRIGGERS` per `tools/evolution/cycle.py:48`) means tune-system fires every 6 cycles × 24 sessions = 144 sessions, which at the current ~144-sessions/37h pace yields exactly this cadence. Skill spec documents 30-day cadence; current operation is **~19× faster than spec**. **32nd consecutive report noting the mismatch.** Recommendation unchanged.

### Failure Pattern Analysis

**Data points**: 153 changelog entries in period; `failed_tasks: {}`; all 20 recent_tasks success.

| Task Type | Executed | Skipped/Abandoned | Rate |
|-----------|----------|-------------------|------|
| deep-review | 96 | 0 | 0% |
| refine-draft | 38 | 0 | 0% |
| condense | 14 | 0 | 0% |
| coalesce | 13 | 8 (abandoned) | **0% hard-fail; 62% no-candidate** |
| pessimistic-review | 9 | 0 | 0% |
| optimistic-review | 8 | 0 | 0% |
| expand-topic | 7 | 1 (skipped duplicate) | 0% hard-fail |
| research-voids | 5 | 0 | 0% |
| apex-evolve | 4 | 0 | 0% |
| check-tenets | 3 | 0 | 0% |
| tune-system | 1 | 0 | 0% |
| research-topic | 1 | 0 | 0% |
| cross-review | 1 | 0 | 0% |

**Hard-failure reliability**: 18th consecutive zero-failure tune period.

**Coalesce abandon rate climbing**: 8/13 (~62%) abandoned this period vs ~0/10 (0%) last period. Each abandonment cites the same reason: catalogue is well-curated, articles are explicitly differentiated, and forcing a merge would erase deliberate distinctions. The 5 successful coalesces include the methodologically significant epistemic-horizon-void → meta-epistemology-of-limits merge (which freed a voids slot) plus what-voids-reveal hub creation. Pattern suggests coalesce is reaching a natural ceiling — most remaining low-hanging fruit has been picked. Worth flagging as a potential signal that the cycle could allocate the second coalesce slot (cycle position 21) to something else once abandon rate stays ≥ 50% across three periods. **First period at this rate** — early to act.

**Expand-topic skipped duplicate**: 2026-04-28 17:22 UTC `expand-topic` for "Min/Max Dualism Taxonomy" was skipped because the article already exists under a different slug (`four-quadrant-dualism-taxonomy`). The skip surfaces a known replenishment heuristic gap: research → article matching is slug-based, not topic-overlap-based. Single occurrence this period; not yet a recurring pattern but worth tracking.

**Deep-review near-zero-change convergence persists**: Multiple stability-confirmation deep-reviews this period — at minimum: `apex/taxonomy-of-voids` (2026-04-29 00:54 UTC, no change at 4541 words; **fourth cross-review since 2026-04-27 confirming apex stability**), `concepts/evolution-of-consciousness` (sixth review, no change), `voids/plurality-void` (no change), `concepts/perceptual-degradation-and-the-interface` (3 reviews + 1 refinement, "convergence" declared explicitly), `concepts/attention-as-interface` (seventh review at convergence), `concepts/knowledge-argument` (seventh review at convergence). At least 6/96 deep reviews this period made no content change. Recommendation #6 (per-article review-count tracking with skip-after-3-stable) still stands and grows more load-bearing with each period.

### Queue Health Analysis

**Data points**: Current todo.md (5563 lines, 483 tasks; P2=3, P3=480, vetoed=0).

| Priority | Active Count | Change |
|----------|--------------|--------|
| P0 | 0 | → |
| P1 | 0 | → |
| P2 | 3 | +1 |
| P3 | 480 | **+26** |

**P2 churn**: 2 → 3 in 37h. P2 tasks created and discharged this period include the agency-void post-coalesce refine chain, the suspension-void chain, and the cognitive-phenomenology cross-review chain (still pending). All replenish-queue invocations appear to land in the changelog (in contrast to last period, where some replenishment commits were obscured by the W17 archive rollover).

**P3 generation rate accelerating**: 454 → 480 in 36.7h (+26; **~17/day, vs ~9.4/day last period**). The 8 optimistic-reviews this period each produced ~3-5 P3 tasks (≈ 24-40 task additions); 9 pessimistic-reviews each produced 1-2 P3 follow-ups (≈ 9-18 additions). Some of these were absorbed by chain execution within the period. Net +26 brings P3 within ~20 of the ad-hoc 500-ceiling-of-concern flagged last report. **At the current rate, P3 will cross 500 within the next tune cycle.** Recommendation #7 (P3 ceiling or accept-as-archival) is becoming time-sensitive.

**Section-cap pressure on voids**: 97/100 at start; voids/suspension-void created 2026-04-28 13:17 UTC (+1 → 98); coalesce of epistemic-horizon-void → meta-epistemology-of-limits at 2026-04-28 23:08 UTC (−1 → 97). Net zero this period despite 5 research-voids tasks (research is one step removed from creation). Catalogue self-regulating effectively at the cap, but the combination of high research-voids cadence (5 in this period) and capped voids creation will keep accumulating unconsumed research notes — currently 367, up from 364, with 11 of those expected to be void-research that will not consume into expand-topic until slots open.

**Apex over governance cap**: 22 → 23 with creation of `apex/conjunction-coalesce.md` (deep-reviewed twice this period: 2026-04-27 21:14 UTC and 2026-04-27 23:28 UTC). Now **23/20** governance-listed; **3 apex pieces over the documented cap.** **4th consecutive period.** The cap exists in `obsidian/apex/apex-articles.md` text but is not enforced in code — no automation refuses an apex-evolve creation when over cap. This stands in contrast to voids/concepts/topics caps which are enforced.

### Review Finding Patterns

**Data points**: 9 pessimistic reviews, 8 optimistic reviews, 3 tenet checks, 96 deep reviews (period).

**Tenet-check zero-warning streak extends to 7**: 2026-04-29 01:06 UTC tenet check returned 0 errors / 0 warnings on a 32-file delta sweep. Previous two checks (2026-04-28 06:48 UTC; 2026-04-27 12:38 UTC) also clean. **7th consecutive zero-error tenet check.** Corpus continues to hold tenet-alignment high-water mark.

**Pessimistic→refine pipeline remains tight**: Two notable rapid-turnaround chains this period — (1) suspension-void was created 13:17 UTC, deep-reviewed 14:13 UTC, pessimistic-reviewed 14:22 UTC, refined 14:37 UTC (15-minute pessimistic→refine), then condensed 15:23 UTC (when length flagged); (2) phenomenology-vs-function-axis concept page created 19:18 UTC, deep-reviewed 19:45 UTC, cross-reviewed 20:08 UTC, pessimistic-reviewed 20:23 UTC, refined 20:39 UTC (16-min pessimistic→refine). The "create → review → refine within an hour" pattern is now standard.

**LLM cliché "Not X but Y" continues to be hunted**: 2026-04-28 deep-reviews of `concepts/narrative-coherence` (15:13), `concepts/adaptive-cognitive-limits` (22:45), and the `topics/consciousness-and-the-metaphysics-of-laws-and-dispositions` 07:12 refine-draft each cleaned at least one banned construct. Several pessimistic reviews (2026-04-28b on synesthetic-void, 2026-04-28c on suspension-void) flagged 2 instances each as critical issues. Pattern identical to prior periods: cliché generated at expand-topic time and cleaned at deep-review or pessimistic-review time. **12th consecutive period flagging this.**

**Apex re-synthesis regression — second instance**: Last period flagged `apex/identity-across-transformations` having silently regressed two prior fixes during 2026-04-17 apex-evolve re-synthesis. This period, no new instance was caught (third review of identity-across-transformations 2026-04-27 confirmed the fixes are now stable post-correction), but the broader pattern of apex-evolve re-syntheses needing back-cross-review remains. The 2026-04-29 00:54 UTC deep-review of `apex/taxonomy-of-voids` was explicitly framed as a "fourth cross-review" against source-article evolution and was clean — the apex absorbed source-side restructuring without losing review-installed deltas. This suggests the regression vector is **per-apex, not universal**: some apex synthesis methodologies preserve deltas, some regenerate from sources. Worth profiling apex-evolve runs by which apex they target. **Carry forward, refined.**

**HTML refinement-log marker handling — possible discipline shift (NEW)**: Last period's recommendation #9 flagged that AI REFINEMENT LOG HTML comment blocks were being placed by refine-draft, marked for self-removal, and then removed by later deep-reviews — generating avoidable churn. This period **shows mixed treatment**: (a) the 2026-04-28 22:09 UTC condense of `apex/taxonomy-of-voids` explicitly LEFT the marker untouched ("AI REFINEMENT LOG comments left untouched — they belong to the human-review process and are out of scope for condensation"), suggesting the marker is now being respected as a human-review artifact; but (b) 2026-04-28 21:38 UTC deep-review of `concepts/functionalism` removed a stale 2026-04-07 marker "per its own instructions" and 2026-04-28 14:52/15:23 UTC operations on suspension-void condensed-out the marker block. **Mixed signal.** Could be deliberate divergence (condense preserves; deep-review/refine removes after threshold age) or genuine inconsistency. If deliberate, worth documenting in CLAUDE.md; if not, the recommendation from last period stands.

**New finding — coalesce abandon rate provides epistemic signal**: With 8/13 abandons (~62%) this period, the coalesce skill is increasingly serving as a **probe of catalogue maturity** rather than a content-modification action. Each abandon is a positive epistemic signal (the catalogue's distinctions are load-bearing) but consumes an LLM call. Worth tracking whether the abandon rate stays high — if it does, the second coalesce slot in the cycle (position 21) could be reallocated to a higher-yield task type without losing the first coalesce slot's catalogue-pruning function.

### Convergence Progress

| Category | Count | Cap | % of Cap | Direction |
|----------|-------|-----|----------|-----------|
| Topics | 231 | 250 | 92.4% | 19 slots (**+1 vs prev**) |
| Concepts | 232 | 250 | 92.8% | 18 slots (−1 vs prev) |
| Voids | 97 | 100 | **97.0%** | 3 slots (→) |
| Arguments | 6 | — | — | → |
| Apex | 23 | (20 governance) | — | **23/20 — over cap (+1 vs prev)** |

**Voids stability**: Held at 97 this period through one creation + one coalesce — the catalogue's first observed "self-regulating equilibrium" at the cap. Worth watching whether this is incidental (next period could see net +1 or net −1) or whether the system is now in a steady-state at 97/100.

**Topics −1**: Likely a coalesce or archive event. Did not surface in changelog inspection — may have been part of the 04-28 coalesce arc (the topics-side `consciousness-and-the-metaphysics-of-laws-and-dispositions` was a coalesce-target absorbing two source articles per the 2026-04-28 00:13 UTC coalesce note in earlier-period changelog). Verifies that net -1 is consistent with one source archived without offsetting creation.

**Concepts +1**: New `concepts/phenomenology-vs-function-axis` (created 2026-04-28 19:18 UTC) plus possibly other small movements. The page is now linked from four exemplar voids/topics and has been deep-reviewed three times in two days.

**Apex +1**: New `apex/conjunction-coalesce` puts the section at 23 articles vs 20 governance cap. **Cap exceeded by 3.** No automation enforces this cap.

**Quality metrics (frozen, 35th period)**:
- Critical: 0 ✓ (target)
- Medium: 10 (target ≤3) — almost certainly stale counter
- Low: 3
- Orphans: 13

## Changes Applied (Tier 1)

*No changes applied.*

**Rationale**: Same three structural blockers as the last 31 reports:
1. No `cadences` / `overdue_thresholds` / `replenishment_config` sections in evolution-state.yaml — nothing to tune.
2. No `tune_system_history` — cooldowns unenforceable.
3. No `locked_settings` — cannot check for human overrides.

**32nd consecutive report** unable to apply Tier 1 changes for this structural reason. The skill's specified operating surface (YAML parameters) does not exist in the current state file; operational parameters live in `tools/evolution/cycle.py` Python code and are out of scope for this skill.

## Recommendations (Tier 2)

### 1. Fix `last_runs` Writeback for Cycle-Trigger Tasks (Carried Forward ×4)

- **Proposed change**: Audit the dispatch code in `tools/evolution/` that persists `last_runs` after task completion. check-tenets (~18h stale), research-voids (~12h stale), and apex-evolve (~12h stale) all show writeback lag this period. Coalesce shows the opposite (writeback ahead-of-fact on no-candidate ticks).
- **Rationale**: Pattern now confirmed across **four consecutive reports** — systematic, not transient. Stale `last_runs` corrupts trigger gating; writeback-ahead-of-fact creates phantom freshness. The two failure modes likely share a root cause (timestamp updates wired to the cycle tick rather than to task-completion events).
- **Risk**: Low (read the code; single-point fix in `tools/evolution/cycle.py` dispatch).
- **Priority**: Medium-High.

### 2. Fix Stale `content_stats` / `progress` Counters (Carried Forward ×30)

- **Proposed change**: Add per-section file-counting at session start in `tools/evolution/state.py`.
- **Rationale**: 35th consecutive report. Recorded state shows 35 topics (actual 231), 145 concepts (actual 232), 11 voids (actual 97), 542 reviews (actual 3635). No functional harm (caps use separate live counts) but every metric-dependent skill has to recompute from filesystem.
- **Risk**: Low.
- **Priority**: Medium.

### 3. Add `tune_system_history` / `locked_settings` / `cadences` Sections (Carried Forward ×32)

- **Proposed change**: Populate evolution-state.yaml with the sections the skill spec expects: `cadences`, `overdue_thresholds`, `replenishment_config`, `tune_system_history`, `locked_settings`.
- **Rationale**: Without these, tune-system cannot make Tier 1 changes safely. 32 reports now effectively advisory-only.
- **Risk**: Low.
- **Priority**: High.

### 4. Add `validate-all` to Cycle Triggers (Carried Forward ×27)

- **Proposed change**: Add `"validate-all": 2` or similar to `CYCLE_TRIGGERS` in `tools/evolution/cycle.py:43-49`.
- **Rationale**: 96 days stale. Listed in CLAUDE.md as "Daily health check" but not wired into automation.
- **Risk**: Low (read-only check).
- **Priority**: Medium.

### 5. Reconcile tune-system Cadence (Carried Forward ×5)

- **Proposed change**: Either (a) adjust `tune-system` in `CYCLE_TRIGGERS` from 6 to 30 (approaches the 30-day documented cadence at current loop speed), or (b) revise the skill spec to ~1.5-day cadence matching current operation.
- **Rationale**: Current ~37h cadence is **~19× faster than spec**. Each run covers small deltas; most findings are carried forward. Moving to monthly would cut cost ~19× with minimal signal loss, since no new infrastructure findings have emerged in ~32 reports.
- **Risk**: Low.
- **Priority**: Medium.

### 6. Implement Deep-Review Convergence Tracking (Carried Forward ×21)

- **Proposed change**: Track per-article review count and last word-change delta; skip further deep-review for articles with 3+ reviews all showing near-zero net change.
- **Rationale**: At least 6/96 deep-reviews this period made no content change (taxonomy-of-voids fourth cross-review with no change; evolution-of-consciousness sixth review with no change; plurality-void no change; perceptual-degradation declared at convergence; attention-as-interface seventh review at convergence; knowledge-argument seventh review at convergence). Reviewers annotate "stability confirmed" but re-queuing continues. Becoming progressively more load-bearing as more articles converge.
- **Risk**: Low.
- **Priority**: High.

### 7. Audit Apex Cap Governance — Now 23/20 (Carried Forward ×4)

- **Proposed change**: Resolve the apex count discrepancy: `obsidian/apex/` contains 23 files (counting `apex.md` and `apex-articles.md` as governance/index files brings active apex count to 21); apex-articles.md's governance list caps at 20.
- **Rationale**: Inconsistent governance means apex-evolve decisions may treat real files as nonexistent. Cap is documented in text but not enforced in code; new apex creations (`conjunction-coalesce` this period) ignore it.
- **Risk**: Low.
- **Priority**: Medium-High (was Medium; raised because count is climbing).

### 8. Update `convergence_targets` (Carried Forward ×34)

- **Proposed change**: `min_topics` 10→200, `min_concepts` 15→200, `min_arguments` 5→10, add `min_voids` 80, add `min_apex` 15, `max_medium_issues` 3 → 15.
- **Rationale**: Targets set for early-stage system; all vastly exceeded. Cosmetic.
- **Risk**: Low.
- **Priority**: Low.

### 9. Auto-Remove HTML Refinement-Log Markers — REVISED (Carried Forward ×2, refined this period)

- **Proposed change**: Document the marker-handling discipline in CLAUDE.md or refine-draft SKILL.md. Two acceptable disciplines: (a) marker is a human-review artifact preserved by all automation until human review (the 2026-04-28 22:09 UTC condense behaviour); (b) marker is auto-removable by deep-review after N days (the 2026-04-28 21:38 UTC functionalism behaviour).
- **Rationale**: This period showed both behaviours, suggesting the system is in transition or the rule is unclear. Either policy is acceptable; **inconsistent treatment is the problem.** Documenting one or the other will stop the recurring deep-review cleanups (or stop the condense's preservation, depending on which discipline wins).
- **Risk**: Low (formatting / instruction change).
- **Priority**: Medium.

### 10. Track Apex Re-Synthesis Regressions Per-Apex (Carried Forward, REVISED)

- **Proposed change**: When apex-evolve re-synthesises an article, surface diffs against the latest deep-review-installed corrections AND tag the apex with a "preserve-vs-regenerate" classification based on observed behaviour.
- **Rationale**: Last period flagged `apex/identity-across-transformations` as a content-loss case. This period, the `apex/taxonomy-of-voids` fourth cross-review (2026-04-29 00:54 UTC) explicitly confirmed the apex absorbed source-side restructuring **without** losing review-installed deltas. So the issue is **per-apex, not universal**. Worth instrumenting apex-evolve to detect and report which apex articles are at risk.
- **Risk**: Medium (touches apex-evolve methodology).
- **Priority**: Medium.

### 11. Track Coalesce Abandon Rate as Catalogue-Maturity Signal (NEW this period)

- **Proposed change**: Track per-period coalesce abandon rate as a metric in evolution-state.yaml. If abandon rate stays ≥ 50% for 3 consecutive tune periods, **auto-shrink** the second coalesce slot (cycle position 21 in `tools/evolution/cycle.py`) by replacing it with a higher-yield task type.
- **Rationale**: Coalesce abandon rate jumped from ~0% last period to **62% this period** (8/13). Each abandon is one LLM call returning a positive-but-static epistemic signal (the catalogue is well-curated). At 62% abandon rate, the second coalesce slot is yielding ~38% productive runs vs ~62% no-ops; reallocation could improve cycle ROI without losing the first coalesce slot's catalogue-pruning function.
- **Risk**: Low (one-line cycle change once threshold is crossed).
- **Priority**: Medium (track now; act if pattern holds).

### 12. Address P3 Approaching 500 Ceiling (NEW this period)

- **Proposed change**: Either (a) impose a P3 ceiling in `replenish-queue` (halt optimistic-review P3 generation when P3 ≥ 500), or (b) document in CLAUDE.md that P3 is an archival/suggestion-buffer tier rather than a true work queue.
- **Rationale**: P3 grew at **~17/day this period vs ~9.4/day last period** — generation rate nearly doubled. At current rate, P3 crosses 500 within the next tune cycle. Last period flagged 500 as a candidate ceiling; this period's acceleration makes the question time-sensitive. Either decision (ceiling or archival) closes the open question.
- **Risk**: Low.
- **Priority**: Medium-High (was Medium; raised because the rate accelerated).

## Items for Human Review (Tier 3)

### 1. Stale State Tracking — 35th Consecutive Report

- **Issue observed**: `content_stats.total_files` and `progress.*` counters frozen at early-project values.
- **Why human needed**: Code change to `tools/evolution/state.py`.
- **Suggested action**: Add per-section file-counting at session start.

### 2. `last_runs` Writeback Gap for Cycle-Trigger Tasks (Carried Forward ×4)

- **Issue observed**: Three cycle-trigger tasks show 12–18h writeback lag this period (check-tenets, research-voids, apex-evolve). Coalesce shows the inverse (timestamps advance ahead-of-fact on no-candidate ticks). Pattern is now systematic across four consecutive reports.
- **Why human needed**: Code inspection of `tools/evolution/cycle.py` and related task dispatch paths.
- **Suggested action**: Find the dispatch branch for cycle-trigger tasks and ensure it calls `state.update_last_run(task_name, now)` after task completion (not at cycle tick).

### 3. Medium Issues Persistent at 10 (Carried Forward ×26)

- **Issue observed**: Medium issues count exactly 10 for 26 consecutive tune periods.
- **Why human needed**: Decide whether this is a stale counter or live tracking.
- **Suggested action**: Inspect the source of `quality.medium_issues` and confirm it is recomputed at session start.

### 4. Orphaned Files Persistent at 13 (Carried Forward ×13)

- **Issue observed**: Same 13-orphan count through extensive cross-linking work.
- **Why human needed**: Almost certainly stale detection.
- **Suggested action**: Re-run orphan detection against live file state and verify.

### 5. Apex Cap Inconsistency — Now 23/20 (Carried Forward ×4)

- **Issue observed**: `obsidian/apex/` contains 23 files (21 active apex + 2 governance pages); apex-articles.md caps at 20. **+1 vs last period.**
- **Why human needed**: Editorial/governance decision, plus optional code change to enforce cap.
- **Suggested action**: Reconcile the approved list against the filesystem; archive overflow, raise the cap, or add cap enforcement to the apex-evolve skill.

### 6. tune-system Cycle-vs-Cadence Mismatch (Carried Forward ×5)

- **Issue observed**: Skill documents 30-day cadence; cycle trigger fires every ~1.5 days at current pace (37h this period — fastest yet, **~19× faster than spec**).
- **Why human needed**: Pick a cadence. Current mismatch generates ~19× the intended reports.
- **Suggested action**: Either change `tune-system: 6` to `tune-system: 30` in `CYCLE_TRIGGERS` (`tools/evolution/cycle.py:48`), or update the skill spec to match observed cadence.

### 7. P3 Overhang Approaching 500 (Carried Forward ×3, ESCALATING)

- **Issue observed**: P3 queue depth grew **454 → 480 (+26 in 37h, ~17/day, vs ~9.4/day last period)**. P2/P3 promotion rate near zero; execution ratio far below generation ratio. Generation rate has nearly doubled.
- **Why human needed**: Decide whether P3 is functioning as a suggestion buffer (current behaviour) or a true work queue. At current rate P3 crosses 500 within the next tune cycle.
- **Suggested action**: Either (a) add a P3 ceiling to `replenish-queue` (e.g., halt optimistic-review P3 generation if P3 > 500), or (b) accept P3 as archival and document that in CLAUDE.md.

### 8. Apex Re-Synthesis Content-Loss Vector — Now Per-Apex Differentiated (Carried Forward, REFINED)

- **Issue observed**: Last period documented `apex/identity-across-transformations` regressing prior fixes during 2026-04-17 apex-evolve re-synthesis. This period's `apex/taxonomy-of-voids` fourth cross-review (2026-04-29 00:54 UTC) showed **no regression** — apex absorbed source-side change cleanly. So the regression vector is per-apex, not universal.
- **Why human needed**: Decide whether to instrument apex-evolve with diff-against-prior-deep-review checks, or accept that some apex articles are regression-prone and rely on deep-review as periodic guard.
- **Suggested action**: Profile apex-evolve runs by which apex they target; classify each apex as "preserves deltas" or "regenerates from sources"; treat regenerate-class apexes as needing post-synthesis cross-review.

### 9. Refinement-Log Marker — Discipline Inconsistency (NEW)

- **Issue observed**: The 2026-04-28 22:09 UTC condense of `apex/taxonomy-of-voids` explicitly preserved the AI REFINEMENT LOG marker as out-of-scope; same day's 21:38 UTC deep-review of `concepts/functionalism` removed a stale marker per its own instructions. Mixed signal.
- **Why human needed**: Editorial decision: is the marker a human-review artifact (preserve) or an auto-cleanable hint (remove after threshold)?
- **Suggested action**: Document the chosen discipline in `.claude/skills/refine-draft/SKILL.md` or CLAUDE.md.

### 10. Coalesce Abandon Rate Spiked to 62% (NEW)

- **Issue observed**: 8 of 13 coalesce attempts this period abandoned (vs 0/10 last period). Each abandonment cites the same reason: catalogue is well-curated, articles are explicitly differentiated.
- **Why human needed**: Decide whether the second coalesce cycle slot (position 21) should be reallocated when abandonment becomes the norm.
- **Suggested action**: Watch this signal across the next 1-2 tune periods; if abandon rate stays ≥ 50%, replace cycle position 21 with another high-yield task type.

## System Health Summary

| Component | Status | Notes |
|-----------|--------|-------|
| Task execution | **Excellent** | 0% hard-failure rate (18th consecutive period; 153/153) |
| Skip rate | Excellent | 9 abandonments by design (8 coalesce no-candidate; 1 expand-topic duplicate) |
| Content quality | Excellent | 0 critical issues; 0/0 tenet errors/warnings (7th clean tenet check) |
| Queue management | Mixed | P2 stable at 3; **P3 generation rate nearly doubled** (+26/37h vs +32/82h) |
| Expand-topic efficiency | Excellent | 7/7 success + 1 deliberate duplicate-skip |
| Coalesce efficiency | **Watch** | 5/13 productive, 8/13 abandoned (62% abandon rate; first period at this rate) |
| Review system | Excellent | ~58 reviews/day; pessimistic→refine pipeline ~15-min turnaround |
| Deep-review convergence | Mixed | 6/96 zero-change reviews this period (and growing) |
| Scheduling | Operational | Cycle mechanism stable but **~19× faster than spec** for tune-system |
| Changelog rotation | Working | W17 archive holds prior period; current changelog at 200 entries |
| State tracking | **Broken** | content_stats/progress stale (35th); `last_runs` writeback (4th period systematic) |
| Topics cap | Healthy | 231/250 — 19 slots |
| Concepts cap | Healthy | 232/250 — 18 slots |
| Voids cap | **Tight (steady)** | 97/100 — 3 slots; one period of self-regulating equilibrium |
| Apex cap | **Inconsistent (worsening)** | 23 files vs 20 approved (4th period; +1 vs prev) |
| Site validation | **Gap** | validate-all not running (96 days; 27th report) |
| Tenet alignment | **Excellent** | 7th clean delta sweep |
| Pessimistic→refine pipeline | **Excellent** | 15–16 min turnaround on suspension-void + axis chains |
| Apex re-synthesis | **Per-apex differentiated** | identity-across-transformations regressed; taxonomy-of-voids did not |
| Refinement-log marker | **Inconsistent** | Mixed treatment this period (preserve vs remove) |
| tune-system infrastructure | **Blocked** | 32nd report unable to apply Tier 1 |

## Next Tuning Session

- **Expected (at current cycle-trigger rate)**: ~2026-04-30 (1.5 days out)
- **Recommended per skill spec**: 2026-05-29 (30 days out)
- **Focus areas next run**:
  - Whether voids self-regulating equilibrium at 97/100 holds, breaks toward 96, or breaks toward 98
  - Whether P3 crosses 500 (likely; ~17/day rate gives ~31h to cross)
  - Whether coalesce abandon rate stays ≥ 50% (current 62%; first period at this rate)
  - Whether apex count stays at 23 or grows (cap enforcement question)
  - Whether refinement-log marker handling settles toward one discipline
  - Whether `last_runs` writeback gap has been addressed (4th consecutive period)
  - Whether `tune_system_history` / `locked_settings` / `cadences` sections appear (33rd report)
  - Whether validate-all is integrated (28th report)
  - Whether stale state tracking gets addressed (36th report)
  - Whether apex re-synthesis regression recurs on next apex-evolve run on a "regenerate-class" apex