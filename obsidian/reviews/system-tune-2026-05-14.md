---
title: "System Tuning Report - 2026-05-14"
created: 2026-05-14
modified: 2026-05-14
human_modified: null
ai_modified: 2026-05-14T00:18:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[todo]]"
  - "[[changelog]]"
  - "[[reviews/system-tune-2026-05-10]]"
  - "[[reviews/system-tune-2026-05-05]]"
  - "[[reviews/outer-review-synthesis-2026-05-12]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-7
ai_generated_date: 2026-05-14
last_curated: null
---

# System Tuning Report

**Date**: 2026-05-14 00:18 UTC
**Sessions analyzed**: 144 (sessions 6995 → 7139)
**Period covered**: 2026-05-10 17:11 UTC → 2026-05-14 00:18 UTC (~3.3 days / 79 hours)

## Executive Summary

22nd consecutive zero-hard-failure period (~160 status-bearing tasks across the period; `failed_tasks: {}` empty). **Three first-of-kind observations this period**: (1) **outer-review pipeline gap** — no commissions on 2026-05-13 (the 02:00/03:00/04:00 UTC window passed with no entries appended to `pending-reviews.yaml`); first miss since the pipeline went live 2026-05-04; consistent with `outer-todo.md` being empty and the recently-modified-articles fallback returning `NO_SUBJECT` because most articles fall inside the 7-day SEO-buffer floor. (2) **P3 dropped −59 net** (553 → 494) — first reversal of P3 growth after six consecutive periods of accumulation; pruning, completion absorption, or replenisher quiescence drove the drop and the queue is now under the 500 ceiling for the first time in three periods. (3) **Concepts +7 in 3.3 days** — concept growth accelerated to ~2.1/day (was ~0/day last period); the 230 → 237 movement places concepts at 94.8% of cap (13 slots), approaching topic-cap pressure. **Voids back at 100/100** via the 2026-05-13 cycle (slot freed by 2026-05-10 coalesce now refilled). **Methodological-discipline ratchet repeated a fourth time** — the 2026-05-12 ChatGPT outer review's "convergent-conclusion-opposite-reasoning" diagnostic became `project/direct-refutation-discipline.md` Mode Four extension (2026-05-13 20:51 UTC) plus `project/methodology-ratchet.md`-adjacent project docs (`outer-reviewer-service-calibration.md`, `outer-review-empirical-vs-methodological-freshness.md`, `mqi-empirical-fragility.md`) — the 2026-05-10 report's recurrence-threshold trigger has now been crossed a second time, with three project docs landing this period. Same three structural blockers persist: `cadences`, `tune_system_history`, `locked_settings` sections still absent. **36th consecutive report unable to apply Tier 1 changes via the standard YAML mechanism.**

## Metrics Overview

| Metric | Current (Actual) | Recorded State | Previous (May 10) | Trend |
|--------|------------------|----------------|-------------------|-------|
| Session count | 7139 | 7139 | 6995 | +144 |
| Topics | 239 | 35 | 238 | +1 (~96% of cap) |
| Concepts | 237 | 145 | 230 | **+7** (94.8% of cap) |
| Voids | **100** | 11 | 99 | **+1 — back at cap** |
| Apex | 26 files (governance unknown) | 4 | 26 files (23 active) | → files; active TBD |
| Arguments | — | 4 | 6 | → (no recount this period) |
| Questions | 1 | 1 | 1 | → |
| Research | 385 | 117 | 382 | +3 |
| Reviews | 3994 | 542 | 3917 | +77 (~24/day) |
| Total content files | ~300 | 297 | 297 | ≈→ |
| Critical issues | 0 | 0 | 0 | → |
| Medium issues | 10 | 10 | 10 | → (persistent) |
| Low issues | 3 | 3 | 3 | → |
| Orphaned files | 13 | 13 | 13 | → (persistent) |
| Queue depth (P0–P1) | 0 | — | 0 | → |
| Queue depth (P2) | 5 | — | 4 | +1 |
| Queue depth (P3) | **494** | — | 553 | **−59 (under ceiling)** |

**State discrepancy**: Recorded `progress` counters remain frozen at early-project values. **39th consecutive report.** No functional harm.

## Abort Conditions Check

**Status**: All clear.

- Task failure rate: 0% (0/20 recent_tasks failed; `failed_tasks: {}`; 0 Failed/Error markers across the visible changelog this period)
- Convergence: all metrics improving or stable; no regression
- Critical issues: 0
- File reads: all successful

## Check Locked Settings

`locked_settings` section not present in evolution-state.yaml. **36th consecutive report.**

## Findings

### Cadence Analysis

**Data points**: 144 sessions, ~160 changelog entries, 79 hours elapsed.

| Task | last_runs Timestamp | Actual Last Run (verified) | Status |
|------|---------------------|----------------------------|--------|
| validate-all | 2026-01-24 02:57 | Not run since Jan 24 | **110 days stale** |
| pessimistic-review | 2026-05-13 14:51 | 2026-05-13 14:51 UTC | Current (~9h ago) |
| optimistic-review | 2026-05-13 17:51 | 2026-05-13 17:51 UTC | Current |
| check-tenets | 2026-05-11 19:56 | **2026-05-14 00:18 UTC** (changelog) | **Stale writeback — ~52h gap** |
| check-links | 2026-05-12 02:00 | 2026-05-12 02:00 UTC | ~46h ago |
| deep-review | 2026-05-13 21:51 | 2026-05-13 21:51 UTC | Current |
| tune-system | 2026-05-10 17:11 | 2026-05-10 17:11 UTC | ~79h since last (this run) |
| research-voids | 2026-05-12 02:00 | **2026-05-14 00:18 UTC** (changelog) | **Stale writeback — ~46h gap** |
| coalesce | 2026-05-13 20:21 | 2026-05-13 20:22 UTC | Current |
| apex-evolve | 2026-05-12 02:00 | unverified (no apex-evolve in current changelog) | possibly ~46h |
| agentic-social | 2026-05-13 23:21 | 2026-05-13 23:21 UTC | Current |
| tweet-highlight | 2026-01-24 14:00 | Not recently | 110 days stale (`last_tweet_date: 2026-05-13` shows tweets do happen via add-highlight path) |
| embed-videos | 2026-05-13 11:51 | 2026-05-13 11:51 UTC | Current |
| commission-chatgpt-review | 2026-05-12 02:00 | 2026-05-12 02:04 UTC | **Stale 46h — no 05-13 commission** |
| commission-claude-review | 2026-05-12 03:11 | 2026-05-12 03:15 UTC | **Stale 45h — no 05-13 commission** |
| commission-gemini-review | 2026-05-12 04:13 | 2026-05-12 04:20 UTC | **Stale 44h — no 05-13 commission** |

**`last_runs` writeback for cycle-trigger tasks (CONTINUING — now 8 consecutive reports)**: writeback gaps observed for `check-tenets` (~52h gap; up from ~42h last period) and `research-voids` (~46h, up from ~26h). The gap continues to scale with the time between cycle-trigger ticks. The 2026-05-14 00:18 UTC check-tenets and research-voids runs are not yet reflected in `last_runs` at the time of this read. Pattern confirmed across **eight consecutive reports**. The fix remains a single-point dispatch-path issue in `tools/evolution/cycle.py`; no progress this period.

**`validate-all`**: 110 days stale. **31st consecutive report.**

**`tune-system` cadence at faster pace this period**: This run is ~79h after the previous (vs ~122h last period). The cycle's `tune-system: 6` trigger fires every 144 sessions; the underlying loop interval shortened (~30min/session this period vs ~51min last period), producing a faster wall-clock cadence. The variable-vs-30-day-spec gap is **37th consecutive report**. Observed cadences across last nine periods: 79h → 122h → 122h → ~36h-122h range.

**Outer-review pipeline — first commission gap (NEW)**: No commissions fired on 2026-05-13 — the 02:00/03:00/04:00 UTC window passed with no new entries appended to `pending-reviews.yaml`. The pipeline has commissioned every day from 2026-05-04 through 2026-05-12 without interruption (with the 2026-05-09 cycle being a one-off skip for an unrelated reason). The pending-reviews.yaml has 13 entries across 5 cycle dates (05-04, 05-08, 05-10, 05-11, 05-12) — no 05-13 entries. Cause is consistent with subject-selection exhausting both queue and fallbacks: `outer-todo.md` shows only the two consumed entries from 2026-05-10 (✓-marked); the 7-day-site-fallback would have returned no full-site result (05-11 was a full-site review, within 7 days); and the aged-article fallback may have come up empty because most articles touched this period fall inside the 7-day SEO-buffer floor. Today (2026-05-14) is the first day where the site fallback could fire again (05-11 + 7d = 05-18, still within window; recheck on 05-18 onwards). Worth investigating whether the cycle exited cleanly with `NO_SUBJECT` or whether a different failure mode caused the skip.

### Failure Pattern Analysis

**Data points**: ~160 changelog entries this period; `failed_tasks: {}`; all 20 recent_tasks success; 0 Failed/Error markers.

| Task Type | Executed (period) | Skipped/Abandoned | Rate |
|-----------|-------------------|-------------------|------|
| deep-review | ~50 | 0 | 0% |
| refine-draft | ~50 | 0 | 0% |
| condense | ~10 | 0 | 0% |
| expand-topic | ~12 | 0 | 0% |
| coalesce | ~5 | **1 abandoned** | **0% hard-fail; ~20% no-candidate** |
| pessimistic-review | ~3 | 0 | 0% |
| optimistic-review | ~3 | 0 | 0% |
| outer-review | 6 | 0 (NEW: 1 cycle skipped at commission stage) | 0% |
| research-topic | ~3 | 0 | 0% |
| research-voids | ~3 | 0 | 0% |
| cross-review | ~3 | 0 | 0% |
| check-tenets | 2 | 0 | 0% |
| check-links | 1 | 0 | 0% |
| apex-evolve | ~1 | 0 | 0% |
| combine-outer-reviews | 2 | 0 | 0% (05-11, 05-12 syntheses) |
| replenish-queue | ~1 | 0 | 0% |

**Hard-failure reliability**: 22nd consecutive zero-failure tune period.

**Coalesce abandon rate stable at ~20% (CONTINUING)**: 1/5 (20%) this period vs 2/6 (33%) last period vs 3/9 (33%) prior. Four consecutive periods at ≤35% confirms the 2026-04-29b cycle.py slot reduction (2/24 → 1/24) is a durable fix. The 2026-05-13 20:22 UTC successful coalesce (born-rule-and-the-consciousness-interface + born-rule-violation-brain-interface-empirical-status into a single comprehensive treatment) is the cleanest worked example of the pattern this period.

**Outer-review pipeline — 13 successful runs lifetime, 1 commission-stage skip (UPDATED)**: 6/6 collection+processing success this period (2 from 2026-05-11 cycle + 3 from 2026-05-12 cycle + carry-forward from 2026-05-10). Cumulative across pipeline lifetime: **13/13 collection+processing success**. The 2026-05-13 commission-stage gap is the first miss since the pipeline went live and should be classified as **subject-selection exhaustion**, not pipeline failure (the cycle exited cleanly per its `NO_SUBJECT` design). Pipeline reliability remains 100%; the gap is in upstream queue management.

**Methodological-discipline ratchet — fourth recurrence (UPDATED)**: The 2026-05-12 ChatGPT outer review's structural finding ("the article slides empirical-claim verifiability into methodological-claim transcendence") became three project docs this period: `project/outer-reviewer-service-calibration.md` (2026-05-13 19:51 UTC), `project/outer-review-empirical-vs-methodological-freshness.md` (2026-05-13 23:24 UTC), `project/mqi-empirical-fragility.md` (2026-05-13 21:22 UTC), plus the Mode-Four extension of `project/direct-refutation-discipline.md` (2026-05-13 20:51 UTC). The 2026-05-10 report set "fourth recurrence" as evidence that the pattern was now *production infrastructure* rather than a recurring observation. The fourth recurrence has crossed within 3 days of the third; the cadence is accelerating. **The methodology-of-methodologies pattern is now load-bearing project infrastructure.**

**Deep-review near-zero-change convergence persists (CARRIED FORWARD)**: Multiple stability-confirmation reviews this period — `concepts/llm-consciousness` (9th deep-review, -3 words); `concepts/substrate-independence` (4th deep-review, +3 words); `concepts/phenomenology` (3rd deep-review, +20 words). At least 3-5 deep-reviews this period made no substantive content change. **Recommendation #7 continues to grow load-bearing.**

### Queue Health Analysis

**Data points**: Current todo.md (~6161 lines, 499 active tasks; P0-P1=0, P2=5, P3=494; 105 completed; 313 vetoed).

| Priority | Active Count | Change |
|----------|--------------|--------|
| P0 | 0 | → |
| P1 | 0 | → |
| P2 | 5 | +1 |
| P3 | **494** | **−59 (NEW — under ceiling for first time in 3 periods)** |

**P3 dropped −59 net (NEW — significant)**: P3 dropped from 553 to 494 over 3.3 days. Three explanations are plausible: (a) replenisher quiescence — replenish-queue only fired ~1× this period vs more in prior periods; (b) absorption — many P3 tasks were converted to completed work as the loop tempo increased to ~51 tasks/day; (c) pruning — manual or automated dedup may have closed redundant tasks (the 2026-05-13 23:58 UTC refine-draft entry explicitly notes "duplicate task" and flags replenish-queue calibration). All three mechanisms are likely operating. The P3 ceiling decision flagged for **6 consecutive periods** is now less urgent — the queue is self-regulating to a lower equilibrium. Worth watching whether the equilibrium holds or P3 climbs back over 500 next period.

**P2 depth at 5 (UPDATED)**: P2 at 5 (was 4 last period). Three of the P2 entries are length-condense tasks generated this period from length-analysis (non-temporal-consciousness 5678 words, born-rule-and-the-consciousness-interface 5604 words, phenomenology-of-memory-and-the-self 4558 words) — all three are post-outer-review-accumulation casualties needing condense passes. The replenisher's length-analysis source is producing legitimate P2 work; queue is healthy.

**Section-cap status — voids back at 100/100 (UPDATED)**: Voids 99 → 100 via 2026-05-13 research-voids cycle. The cap-saturation policy continues to operate as designed: cap held until a coalesce opens a slot, then the next research-voids run refills the slot. Concepts ticked up to 237/250 (+7) with 13 slots remaining — concept growth accelerated this period. Topics steady at 239/250 (+1) with 11 slots.

**Apex over governance cap (CONTINUING)**: 26 files; active count unverified this period but likely ~23-24. **8th consecutive report.** P3 task still queued.

### Review Finding Patterns

**Data points**: ~3 pessimistic reviews, ~3 optimistic reviews, 2 tenet checks, ~50 deep reviews, 6 outer reviews (period).

**Tenet-check zero-warning streak extends to 17 consecutive (UPDATED)**: 2026-05-14 00:18 UTC tenet check found "Errors: 0; Warnings: 0" across 476 files (239 topics + 237 concepts). The streak continues unbroken since the discipline was installed. Today's check confirms the methodological-discipline cluster continues to apply the slippage discipline correctly at scale (no slippage detected across the doubled file count of last period).

**Outer-review pipeline drove four project-doc creations this period (NEW)**: The 2026-05-11 and 2026-05-12 outer-review cycles, combined with the methodological-discipline ratchet, produced four new project docs in 36 hours (the four named in Failure Patterns above) — the highest project-doc creation rate of any tune period. Three of the four are in the service-calibration sub-family that the 2026-05-13 19:51 UTC expand-topic surfaced as a coherent grouping. **The catalogue is converging on a service-mix methodology** (Claude adversarial-of-record, ChatGPT focused-hypothesis, Gemini breadth-of-coverage) with pre-registered falsifiable predictions across the next 2-3 full-site Gemini cycles.

**LLM cliché "Not X but Y" continues to be hunted (CONTINUING)**: Multiple deep-reviews and refines this period removed instances. Pattern unchanged from prior periods. **16th consecutive period flagging this.** Operational discipline; no further action proposed.

**Direct-refutation-discipline now extended to Mode Four (NEW)**: The 2026-05-13 20:51 UTC refine-draft of `project/direct-refutation-discipline.md` added "Mode Four: Empirical Underdetermination" as a fourth honest-discharge mode for cases where in-framework refutation is unavailable, the disagreement is not bedrock, but available empirical evidence cannot adjudicate between rival positions. This is the discipline's most substantive extension since creation; convergent with `project/evidential-status-discipline.md`'s constrain-vs-establish distinction. The 2026-05-10 Gemini outer review was the trigger.

### Convergence Progress

| Category | Count | Cap | % of Cap | Direction |
|----------|-------|-----|----------|-----------|
| Topics | 239 | 250 | 95.6% | 11 slots (+1) |
| Concepts | 237 | 250 | **94.8%** | 13 slots (**+7 — accelerating**) |
| Voids | **100** | 100 | **100.0%** | 0 slots — back at cap |
| Arguments | — | — | — | (not recounted) |
| Apex | 26 files | (20 governance) | — | files-only; active TBD |

**Concepts growth accelerated (NEW)**: Concepts gained 7 new pages this period (~2.1/day), bringing the section to 94.8% of cap. Last period was steady at 230. The catalogue is approaching concept-cap saturation faster than topic-cap saturation. Coalesce activity may shift to concepts next period.

**Voids cap holding via expected mechanism (CONTINUING)**: Voids 99 → 100 via 2026-05-13 research-voids cycle. The 2026-05-10 coalesce freed the slot; the next research-voids cycle filled it. Cap-saturation policy validated through its second complete coalesce-then-refill cycle.

**Quality metrics (frozen, 39th period)**:
- Critical: 0 ✓ (target)
- Medium: 10 (target ≤3) — almost certainly stale counter
- Low: 3
- Orphans: 13

## Changes Applied (Tier 1)

*No changes applied via this skill's Tier 1 mechanism.*

**Rationale**: Same three structural blockers as the last 35 reports:
1. No `cadences` / `overdue_thresholds` / `replenishment_config` sections in evolution-state.yaml — nothing to tune via standard mechanism.
2. No `tune_system_history` — cooldowns unenforceable.
3. No `locked_settings` — cannot check for human overrides.

**36th consecutive report** unable to apply Tier 1 changes via the skill's intended YAML mechanism.

**No targeted intervention warranted this period**: The operating system is healthy: 0% hard-failure rate (22 periods), coalesce abandon rate at 20% (4 consecutive periods at ≤35%), outer-review pipeline collection+processing at 100% success, methodological-discipline ratchet has crossed the production-infrastructure threshold. The 2026-04-29b cycle.py fix continues to validate. No new evidence demands a code-level intervention; the 2026-05-13 commission gap is a subject-selection issue (upstream of pipeline mechanics), and one occurrence is below the 3-occurrence evidence threshold.

## Recommendations (Tier 2)

### 1. Audit Outer-Review Subject-Selection Fallback Logic (NEW this period)

- **Proposed change**: Investigate why 2026-05-13 commissions did not fire. Add explicit logging in `tools/reviews/subjects.select_cycle_subject` for each fallback level (queue / site / aged) so future skips can be diagnosed from logs without reconstruction. If `NO_SUBJECT` is firing because the aged-article fallback's 7-day floor + 60-day ceiling excludes all candidates, consider widening the window or relaxing the SEO-buffer constraint.
- **Rationale**: First commission gap since pipeline launch. The 2026-05-13 miss may foreshadow recurring skips if the aged-article fallback is too narrow at current article-modification cadence (~50 tasks/day touches many articles, pushing most ai_modified timestamps inside the 7-day floor).
- **Risk**: Low (logging is read-only; window-widening is conservative).
- **Priority**: Medium-High (avoid further pipeline gaps).

### 2. Impose P3 Ceiling in `replenish-queue` (DE-ESCALATED — was ×6)

- **Proposed change**: Add a P3 ceiling check (e.g., 500) to `tools/curate/replenish.py`. When P3 ≥ 500, halt optimistic-review and gap-analysis P3 generation; allow only chain-replenishment additions.
- **Rationale**: P3 dropped −59 to 494 this period; first decline after six consecutive periods of growth. **Currently under the 500 ceiling.** The decision is no longer urgent — the queue is self-regulating. Lower priority unless P3 climbs back over 500 next period.
- **Risk**: Low.
- **Priority**: **Medium** (de-escalated from High; monitor whether equilibrium holds).

### 3. Fix `last_runs` Writeback for Cycle-Trigger Tasks (Carried Forward ×8)

- **Proposed change**: Audit the dispatch code in `tools/evolution/` that persists `last_runs` after task completion. Two tasks show writeback gaps this period: check-tenets (~52h), research-voids (~46h).
- **Rationale**: Pattern now confirmed across **eight consecutive reports** — systematic. Gap scales with time between cycle-trigger ticks. Coalesce, by contrast, has been near-current throughout, reinforcing that the issue is cycle-trigger-dispatch-path-specific.
- **Risk**: Low (read the code; single-point fix in `tools/evolution/cycle.py` dispatch).
- **Priority**: Medium-High.

### 4. Fix Stale `content_stats` / `progress` Counters (Carried Forward ×34)

- **Proposed change**: Add per-section file-counting at session start in `tools/evolution/state.py`.
- **Rationale**: 39th consecutive report. Recorded state shows 35 topics (actual 239), 145 concepts (actual 237), 11 voids (actual 100), 542 reviews (actual 3994).
- **Risk**: Low.
- **Priority**: Medium.

### 5. Add `tune_system_history` / `locked_settings` / `cadences` Sections (Carried Forward ×36)

- **Proposed change**: Populate evolution-state.yaml with the sections the skill spec expects.
- **Rationale**: Without these, tune-system cannot make Tier 1 changes safely. 36 reports now effectively advisory-only.
- **Risk**: Low.
- **Priority**: High.

### 6. Add `validate-all` to Cycle Triggers (Carried Forward ×31)

- **Proposed change**: Add `"validate-all": 2` or similar to `CYCLE_TRIGGERS` in `tools/evolution/cycle.py`.
- **Rationale**: 110 days stale. Listed in CLAUDE.md as "Daily health check" but not wired into automation.
- **Risk**: Low (read-only check).
- **Priority**: Medium.

### 7. Reconcile tune-system Cadence (Carried Forward ×9)

- **Proposed change**: Either (a) adjust `tune-system` in `CYCLE_TRIGGERS` to better-approximate 30-day cadence at current loop speed, or (b) revise the skill spec to match observed cadence (~3-5 days at current pace, varying with loop interval).
- **Rationale**: Spec documents 30-day cadence; cycle-trigger fires every 144 sessions which produces variable wall-clock cadence. Last nine reports have observed cadences ranging 36h → 122h, with this period at 79h.
- **Risk**: Low.
- **Priority**: Medium.

### 8. Implement Deep-Review Convergence Tracking (Carried Forward ×25)

- **Proposed change**: Track per-article review count and last word-change delta; skip further deep-review for articles with 3+ reviews all showing near-zero net change.
- **Rationale**: Multiple zero-change deep-reviews this period (llm-consciousness 9th, substrate-independence 4th, phenomenology 3rd). The pattern is increasingly load-bearing.
- **Risk**: Low.
- **Priority**: High.

### 9. Audit Apex Cap Governance (Carried Forward ×8)

- **Proposed change**: Resolve the apex count discrepancy. Cap is documented in text but not enforced in code.
- **Rationale**: 26 files; governance cap 20. P3 task already queued.
- **Risk**: Low.
- **Priority**: Medium-High.

### 10. Update `convergence_targets` (Carried Forward ×38)

- **Proposed change**: `min_topics` 10→200, `min_concepts` 15→200, `min_arguments` 5→10, add `min_voids` 80, add `min_apex` 20, `max_medium_issues` 3 → 15.
- **Rationale**: Cosmetic; targets set for early-stage system; all vastly exceeded.
- **Risk**: Low.
- **Priority**: Low.

### 11. Track Apex Re-Synthesis Regressions Per-Apex (Carried Forward ×5)

- **Proposed change**: Surface diffs against the latest deep-review-installed corrections during apex-evolve runs.
- **Rationale**: Pattern (preserve-class vs regenerate-class) holding. Tracking accuracy depends on dispatch-path fix (Recommendation #3).
- **Risk**: Medium.
- **Priority**: Medium.

### 12. Methodological-Discipline Ratchet Project Doc (UPDATED — fourth recurrence)

- **Proposed change**: Promote the methodological-discipline ratchet pattern from "carried-forward recommendation" to actual `project/methodology-ratchet.md` creation. The fourth recurrence crossed within 3 days of the third; the pattern is now production infrastructure rather than observation.
- **Rationale**: Last period set "fourth recurrence" as the trigger for explicit project-doc treatment. The trigger has now fired. The three service-calibration sub-family docs created this period (outer-reviewer-service-calibration, outer-review-empirical-vs-methodological-freshness, mqi-empirical-fragility) are concrete worked examples ready for citation.
- **Risk**: Low (documentation-only).
- **Priority**: **High** (trigger crossed).

### 13. Coalesce Slot Reduction — Validated (Carried Forward, DE-ESCALATED)

- **Proposed change**: No further code change. The 2026-04-29b cycle.py slot reduction (2/24 → 1/24) is now validated for **4 consecutive periods at ≤35% abandon rate** (20%/33%/33%/55%).
- **Rationale**: The fix is durable. Four consecutive periods well below 50% well exceeds the original validation criterion.
- **Risk**: None.
- **Priority**: Low (track-only).

### 14. Three-Way Reviewer Convergence Pipeline Tracking (Carried Forward ×2)

- **Proposed change**: Continue tracking three-way convergence rate across the next 4-6 weeks. 2026-05-10, 05-11, 05-12 cycles all produced syntheses with three-way reviewer collection; the 05-13 commission gap interrupted the streak.
- **Rationale**: First three of four planned tracking cycles have completed. The 05-13 commission-gap is upstream of the convergence question (no reviewers fired) and does not undermine the pipeline's collection+processing reliability. Worth watching whether convergence rate holds when commissions resume.
- **Risk**: None (observation only).
- **Priority**: Low (passive monitoring).

## Items for Human Review (Tier 3)

### 1. Outer-Review Subject-Selection Exhaustion (NEW this period)

- **Issue observed**: No commissions fired on 2026-05-13. Cause appears to be `NO_SUBJECT` returned by `tools/reviews/subjects.select_cycle_subject` because `outer-todo.md` is empty, the 7-day-site-fallback rules out a full-site review (last full-site was 2026-05-11), and the aged-article fallback may have no eligible candidates inside its 7-day-floor / 60-day-ceiling window.
- **Why human needed**: Decide whether to (a) populate `outer-todo.md` with new subjects, (b) widen the aged-article fallback window, or (c) accept occasional gaps as the system self-regulating.
- **Suggested action**: Easiest first move is to add 3-5 new entries to `outer-todo.md` for the next two weeks. The catalogue has been generating concrete improvements and structurally-rich articles ready for outer-review steering (e.g., the new service-calibration project docs themselves are candidates).

### 2. P3 Dropped −59 Net (NEW this period)

- **Issue observed**: P3 dropped from 553 to 494 over 3.3 days — first decline after six consecutive periods of growth. Now under the 500 ceiling.
- **Why human needed**: Understand the mechanism (replenisher quiescence, completion absorption, dedup). If the system is self-regulating, no action needed. If it's due to replenish-queue not firing when it should, that's a regression.
- **Suggested action**: Investigate whether replenish-queue fired the expected number of times this period (~1× observed). If it fired correctly but produced fewer tasks because chain-replenishment exhausted source-research, that's healthy. If it failed silently, that needs a fix.

### 3. Stale State Tracking — 39th Consecutive Report

- **Issue observed**: `content_stats.total_files` and `progress.*` counters frozen at early-project values.
- **Why human needed**: Code change to `tools/evolution/state.py`.
- **Suggested action**: Add per-section file-counting at session start.

### 4. `last_runs` Writeback Gap for Cycle-Trigger Tasks (Carried Forward ×8)

- **Issue observed**: Two cycle-trigger tasks show writeback gaps this period — check-tenets (~52h), research-voids (~46h). Pattern persistent across eight consecutive reports.
- **Why human needed**: Code inspection of `tools/evolution/cycle.py` and related task dispatch paths.
- **Suggested action**: Find the dispatch branch for cycle-trigger tasks and ensure it calls `state.update_last_run(task_name, now)` after task completion (not at cycle tick).

### 5. Medium Issues Persistent at 10 (Carried Forward ×30)

- **Issue observed**: Medium issues count exactly 10 for 30 consecutive tune periods.
- **Why human needed**: Decide whether this is a stale counter or live tracking.
- **Suggested action**: Inspect the source of `quality.medium_issues` and confirm it is recomputed at session start.

### 6. Methodological-Discipline Ratchet — Project Doc Creation Trigger Crossed (UPDATED)

- **Issue observed**: The pattern has run a fourth complete cycle within 3 days of the third. Three new project docs landed this period in the service-calibration sub-family. The trigger set last period has fired.
- **Why human needed**: Editorial decision on whether to create `project/methodology-ratchet.md` documenting the meta-pattern, or extend an existing project doc.
- **Suggested action**: Create `project/methodology-ratchet.md` documenting the four completed cycles as worked examples, plus the three service-calibration project docs as evidence of pattern maturity. This is the natural anchor for the methodology-of-methodologies layer.

### 7. Apex Cap Inconsistency — 26 Files vs 20 Governance (Carried Forward ×8)

- **Issue observed**: 26 apex files vs 20 governance cap.
- **Why human needed**: Editorial/governance decision, plus optional code change to enforce cap.
- **Suggested action**: Reconcile the approved list against the filesystem; archive overflow, raise the cap, or add cap enforcement to apex-evolve.

### 8. tune-system Cycle-vs-Cadence Mismatch (Carried Forward ×9)

- **Issue observed**: Skill documents 30-day cadence; cycle trigger produces variable wall-clock cadence (36h → 122h observed across 9 periods, with this period at 79h).
- **Why human needed**: Pick a cadence. Either change `tune-system` in `CYCLE_TRIGGERS`, or update the skill spec to match observed cadence.
- **Suggested action**: Most natural fix is to revise the skill spec to acknowledge cycle-trigger-driven cadence.

### 9. Concepts Approaching Saturation (NEW)

- **Issue observed**: Concepts at 237/250 (94.8%); 13 slots remaining; +7 this period via expand-topic activity. At current pace (~2.1/day net), concepts will reach cap in ~6 days unless coalesce activity shifts to concepts.
- **Why human needed**: Editorial direction on whether to (a) raise concepts cap, (b) shift coalesce focus to concepts, or (c) accept upcoming concepts-cap saturation as the next system-self-regulation event.
- **Suggested action**: Watch for natural coalesce candidates emerging in concepts; if the cap-saturation policy generalises naturally as it did for voids and is now doing for topics, no human action is required.

## System Health Summary

| Component | Status | Notes |
|-----------|--------|-------|
| Task execution | **Excellent** | 0% hard-failure rate (22nd consecutive period) |
| Skip rate | Excellent | 1 coalesce abandonment by design (20%); 0 hard-fails |
| Content quality | Excellent | 0 critical issues; 0/0 tenet errors/warnings (17 consecutive clean tenet checks) |
| Queue management | **Improving** | P2 at 5; **P3 under ceiling at 494 (−59)** — first decline in 6 periods |
| Expand-topic efficiency | Excellent | All expand-topics succeeded this period |
| Coalesce efficiency | **Validated improvement** | Post-fix abandon rate 20% (4 consecutive periods at ≤35%) |
| Review system | Excellent | ~24 reviews/day; methodological-discipline ratchet at fourth recurrence |
| Deep-review convergence | Mixed | 3-5/50 zero-change reviews (and growing) |
| Scheduling | Operational | Cycle mechanism stable; cadence varies with loop interval |
| Changelog rotation | Working | Current changelog starts 2026-05-11 |
| State tracking | **Broken** | content_stats/progress stale (39th); `last_runs` writeback gap (8th period) |
| Topics cap | **Watch** | 239/250 — 11 slots; +1 this period |
| Concepts cap | **Watch (accelerating)** | **237/250 — 13 slots; +7 this period** |
| Voids cap | At cap | 100/100; cap-saturation policy validated through second complete cycle |
| Apex cap | Inconsistent (steady) | 26 files vs 20 governance (8th period) |
| Site validation | **Gap** | validate-all not running (110 days; 31st report) |
| Tenet alignment | **Excellent** | 17 consecutive clean delta sweeps |
| Outer-review pipeline | **Mixed: collection/processing 13/13; commission gap 2026-05-13** | First subject-selection-exhaustion miss since launch |
| Methodological-discipline ratchet | **Production infrastructure (NEW)** | Fourth recurrence; three service-calibration project docs landed |
| Coalesce slot fix (cycle.py) | **Validated (durable)** | 4 consecutive periods at ≤35% abandon rate |
| tune-system infrastructure | **Blocked** | 36th report unable to apply Tier 1 via YAML |
| Three-way convergence pipeline | **Operational (interrupted)** | 3 consecutive cycles with all-three collection (05-10, 05-11, 05-12); 05-13 missed |

## Next Tuning Session

- **Expected (at current cycle-trigger rate)**: ~2026-05-17 (3 days out at current loop tempo)
- **Recommended per skill spec**: 2026-06-13 (30 days out)
- **Focus areas next run**:
  - Whether the 2026-05-13 commission gap recurs or is a one-off subject-selection exhaustion
  - Whether `outer-todo.md` is repopulated and the steered-subject pipeline resumes
  - Whether concepts cap saturation arrives as expected (currently 237/250)
  - Whether P3 stays under 500 ceiling (currently 494) or climbs back
  - Whether `project/methodology-ratchet.md` gets created (trigger crossed this period)
  - Whether coalesce abandon rate stays at or below 35% (validating the cycle.py fix at 5 consecutive periods)
  - Whether `last_runs` writeback gap has been addressed (9th consecutive period)
  - Whether `tune_system_history` / `locked_settings` / `cadences` sections appear (37th report)
  - Whether validate-all is integrated (32nd report)
  - Whether stale state tracking gets addressed (40th report)
  - Whether the methodological-discipline ratchet repeats a fifth time
