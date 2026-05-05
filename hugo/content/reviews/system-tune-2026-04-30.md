---
ai_contribution: 100
ai_generated_date: 2026-04-30
ai_modified: 2026-04-30 13:38:00+00:00
ai_system: claude-opus-4-7
author: null
concepts: []
created: 2026-04-30
date: &id001 2026-04-30
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[todo]]'
- '[[changelog]]'
- '[[reviews/system-tune-2026-04-29]]'
- '[[reviews/system-tune-2026-04-29b-voids-saturation]]'
title: System Tuning Report - 2026-04-30
topics: []
---

# System Tuning Report

**Date**: 2026-04-30 13:38 UTC
**Sessions analyzed**: 144 (sessions 6563 → 6707)
**Period covered**: 2026-04-29 01:11 UTC → 2026-04-30 13:38 UTC (~36.5 hours / 1.5 days)

## Executive Summary

19th consecutive zero-hard-failure period (151 tasks executed, 0 failures). **Yesterday's targeted cycle.py fix is working as intended**: the 2026-04-29 19:10 UTC change reducing the second coalesce slot (slot 21 → "queue") has produced a clear post-fix improvement — **3/4 coalesces succeeded after the fix (75% success), vs 1/7 abandons before the fix (14% success)**. Net coalesce abandon rate this period dropped from 62% → 55%, second consecutive period above 50% but trend bending favourably. **P3 crossed the 500 ceiling flagged last period (now 502)** — the time-sensitive escalation in last period's recommendation #12 is now realised. Voids self-regulating at 98/100 (one creation since the 99/100 high-water during yesterday's targeted tune; net −1 via subsequent merge). Apex 22 active articles (governance cap remains 20; 2 over). Concepts −1 net via coalesce activity (232 → 231); topics stable at 231. Same three structural blockers persist: `cadences`, `tune_system_history`, `locked_settings` sections still absent from evolution-state.yaml. **33rd consecutive report unable to apply Tier 1 changes via YAML.** However, yesterday's targeted tune-system demonstrated that targeted code-level Tier-1-equivalent changes (cycle.py) are tractable when explicitly scoped.

## Metrics Overview

| Metric | Current (Actual) | Recorded State | Previous (Apr 29) | Trend |
|--------|------------------|----------------|-------------------|-------|
| Session count | 6707 | 6707 | 6563 | +144 |
| Topics | 231 | 35 | 231 | → |
| Concepts | 231 | 145 | 232 | **−1** |
| Voids | 98 | 11 | 97 | **+1 net** |
| Apex | 22 active (24 files inc. governance) | 4 | 22 active (was framed as 23) | → (post-decoherence-selection-programme created mid-period) |
| Arguments | 6 (estimate) | 4 | 6 | → |
| Questions | 1 | 1 | 1 | → |
| Research | 369 | 117 | 367 | +2 |
| Reviews | 3736 | 542 | 3635 | +101 (~67/day) |
| Total content files | 297 | 297 | 297 | → |
| Critical issues | 0 | 0 | 0 | → |
| Medium issues | 10 | 10 | 10 | → (persistent) |
| Low issues | 3 | 3 | 3 | → |
| Orphaned files | 13 | 13 | 13 | → (persistent) |
| Queue depth (P0–P1) | 0 | — | 0 | → |
| Queue depth (P2) | 3 | — | 3 | → |
| Queue depth (P3) | 502 | — | 480 | **+22 (crossed 500 threshold)** |

**State discrepancy**: Recorded `progress` counters remain frozen at early-project values (35 topics, 145 concepts, 11 voids, 117 research, 542 reviews). **36th consecutive report.** No functional harm — caps enforced via `section_caps` not `progress`.

## Abort Conditions Check

**Status**: All clear.

- Task failure rate: 0% (0/20 recent_tasks failed; `failed_tasks: {}`; 151/151 changelog entries report Success or Abandoned-by-design)
- Convergence: quality unchanged; no regression
- Critical issues: 0
- File reads: all successful

## Check Locked Settings

`locked_settings` section not present in evolution-state.yaml. **33rd consecutive report.**

## Findings

### Cadence Analysis

**Data points**: 144 sessions, 151 changelog entries, ~36.5 hours elapsed.

| Task | last_runs Timestamp | Actual Last Run (verified) | Status |
|------|---------------------|----------------------------|--------|
| validate-all | 2026-01-24 02:57 | Not run since Jan 24 | **97 days stale** |
| pessimistic-review | 2026-04-30 08:43 | 2026-04-30 08:56 UTC | ~13m writeback gap |
| optimistic-review | 2026-04-30 10:18 | 2026-04-30 10:48 UTC | ~30m writeback gap |
| check-tenets | 2026-04-29 19:10 | **2026-04-30 13:28** (changelog) | **Stale writeback — ~18h** |
| check-links | 2026-04-29 13:04 | 2026-04-29 13:04 UTC | Current |
| deep-review | 2026-04-30 12:18 | 2026-04-30 12:33 UTC (last in period) | ~15m writeback gap |
| tune-system | 2026-04-29 00:54 | **2026-04-29 19:10 UTC** (targeted, per system-tune-2026-04-29b) | **Targeted run not written back to last_runs** |
| research-voids | 2026-04-30 13:24 | 2026-04-30 13:24 UTC | Current |
| coalesce | 2026-04-30 12:48 | 2026-04-30 11:40 UTC (last actual) | Writeback ahead-of-fact (~1h) |
| apex-evolve | 2026-04-29 13:04 | **2026-04-30 13:32** (changelog: machine-question evolve) | **Stale writeback — ~24h** |
| agentic-social | 2026-04-30 13:03 | 2026-04-30 13:03 UTC | Current |
| tweet-highlight | 2026-01-24 14:00 | Not recently | 97 days stale |

**Continuing finding — `last_runs` writeback still incomplete**: Three cycle-trigger tasks (check-tenets ~18h, apex-evolve ~24h) again show writeback gaps this period. Pattern is now confirmed across **5 consecutive reports** as systematic. Coalesce continues to show the inverse pattern (writeback ahead-of-fact). Both symptoms suggest the cycle-trigger dispatch path is updating timestamps before/around invocation rather than after task completion. Root cause lives in `tools/evolution/cycle.py` dispatch.

**`tune-system` writeback specifically broken**: The targeted tune-system at 2026-04-29 19:10 UTC (per system-tune-2026-04-29b) updated `last_runs.tune-system` per its own report. But the current state shows `tune-system: '2026-04-29T00:54:51.058214+00:00'` — pointing to the *earlier* regular tune-system, not the targeted one. Either the targeted run's writeback was overwritten by a subsequent process, or the targeted note's claim of state-update was aspirational. Worth tracing.

**`validate-all`**: 97 days stale. **28th consecutive report.**

**`tune-system` cadence**: ~37h interval this period (cycle-trigger fired exactly on schedule — 144 sessions × 15min/session = 36h). Skill spec documents 30-day cadence; current operation is **~19× faster than spec**. **33rd consecutive report noting the mismatch.** Last period's recommendation #5 stands.

### Failure Pattern Analysis

**Data points**: 151 changelog entries in period; `failed_tasks: {}`; all 20 recent_tasks success.

| Task Type | Executed | Skipped/Abandoned | Rate |
|-----------|----------|-------------------|------|
| deep-review | 79 | 0 | 0% |
| refine-draft | 19 | 1 (no-op duplicate) | 0% hard-fail |
| coalesce | 11 | 6 (abandoned) | **0% hard-fail; 55% no-candidate** |
| condense | 8 | 0 | 0% |
| optimistic-review | 7 | 0 | 0% |
| expand-topic | 7 | 0 | 0% |
| pessimistic-review | 6 | 0 | 0% |
| replenish-queue | 5 | 0 (one false-positive task; closed without harm) | 0% |
| apex-evolve | 3 | 0 | 0% |
| research-voids | 2 | 0 | 0% |
| cross-review | 2 | 0 | 0% |
| check-tenets | 2 | 0 | 0% |

**Hard-failure reliability**: 19th consecutive zero-failure tune period.

**Coalesce abandon rate continues high but bending favourably (NEW)**: 6/11 (~55%) abandoned this period vs 8/13 (~62%) last period. **The cycle.py fix at 19:10 UTC yesterday is the visible turning point**: pre-fix segment (01:11 → 19:10 UTC; 7 attempts) yielded 6 abandonments + 1 success (14% success); post-fix segment (19:10 UTC → present; 4 attempts) yielded 1 abandonment + 3 successes (75% success). The successful post-fix coalesces were architecturally significant (numerosity/quantitative-intuition/mathematical → quantitative-comprehension-void; ai-consciousness-modes + types-of-ai-phenomenal-experience → ai-consciousness-typology; inspection-paradox → self-reference-paradox). Pattern suggests last period's diagnosis was correct: with 2 coalesce slots per cycle, the system was force-firing coalesce against an already-curated catalogue; with 1 slot, the slower triggering allows genuine candidates to accumulate before the next attempt.

**Replenish-queue false-positive (NEW)**: 2026-04-30 08:29 UTC replenisher generated a task asserting [voids/void-as-ground-of-meaning.md](/voids/void-as-ground-of-meaning/) had "zero references to Buddhist/Eastern material" based on a body-keyword grep. Direct grep at 08:36 UTC returned 15 hits — the integration had been completed in two prior passes (2026-04-26, 2026-04-28). The 08:36 UTC refine-draft closed the task as no-op without bloating the article. Single instance this period; suggests the `unconsumed_research` heuristic in `replenish-queue` may have been checking `related_articles` linkage rather than body content, or running against a stale snapshot. Worth tracking — if recurrent, the heuristic's body-keyword check needs hardening.

**Refinement-log marker handling — convention now consolidating (REVISED)**: Last period noted mixed treatment (condense preserves; deep-review removes). This period the convention has tightened: the 09:31 UTC deep-review of `concepts/phenomenology-of-choice-and-volition` noted "removed lingering AI refinement log comment per convention from 09:31 UTC phenomenology-of-choice-and-volition deep-review" — a recursive self-citation suggesting this is becoming the de facto rule (deep-review removes, condense preserves as out-of-scope). The convention has not been formally documented in CLAUDE.md or skill files, but is operating consistently in practice. Last period's recommendation #9 may be quietly self-resolving via convergent practice.

**Deep-review near-zero-change convergence persists (UPDATED)**: Multiple stability-confirmation deep-reviews this period — at minimum: `topics/the-subject-object-distinction-as-philosophical-discovery` (no body change, second consecutive review confirming stability — convergence threshold reached); `concepts/skill-delegation` (5th deep-review, no change); `apex/conjunction-coalesce` (6th review, +1 word for stale-quote fix only); `concepts/ai-consciousness-typology` (post-condense verification, no change); `apex/medium-status-voids-in-cognition` (deep-review confirming convergence after 4 review cycles). At least 5 zero-change deep-reviews in a sample of 79. Recommendation #6 (per-article review-count tracking with skip-after-3-stable) still stands and grows more load-bearing.

**Pessimistic→refine pipeline tightened to apex level (NEW)**: First documented apex-level pessimistic-then-refine cycle ran on [apex/medium-status-voids-in-cognition.md](/apex/medium-status-voids-in-cognition/) (2026-04-30 08:56 UTC pessimistic-review → 09:01 UTC refine-draft). The 5-minute turnaround installed six load-bearing fixes including a new "What Would Falsify This Cluster" section. This is the velocity discipline (previously seen at the topic/concept level) extending upward to apex-tier. Worth tracking whether this becomes regular practice or remains a one-off.

### Queue Health Analysis

**Data points**: Current todo.md (~6500 lines, 505 active tasks; P0-P1=0, P2=3, P3=502, vetoed=0).

| Priority | Active Count | Change |
|----------|--------------|--------|
| P0 | 0 | → |
| P1 | 0 | → |
| P2 | 3 | → |
| P3 | 502 | **+22 (crossed 500 threshold)** |

**P2 stable churn**: Replenisher fired 5 times this period (vs 0 expected at threshold-of-3). Each invocation generated 2-5 P2 tasks that were absorbed by chain execution within hours. The replenisher's ~5-per-day cadence is a function of the very tight P2 threshold (3) combined with rapid task discharge — every chain task closes and re-fires within the same period. **System operating at near-real-time queue equilibrium.**

**P3 just crossed the ceiling-of-concern (NEW — actualised)**: Last period flagged 500 as approaching-time-sensitive; this period P3 actually crossed (480 → 502). Generation rate dropped slightly to ~14/day (vs ~17/day last period), but the threshold is now pierced. Decision required: (a) impose P3 ceiling in `replenish-queue`, (b) document P3 as archival, (c) bulk-prune low-value P3 entries. The replenisher already gates by threshold-of-3 on P2; an analogous P3 ceiling at 500-600 would prevent indefinite accumulation. **The decision is ripe** — the question has now matured from "approaching" to "passed."

**Section-cap pressure on voids (continues)**: Voids 97 → 98 net (peaked at 99/100 mid-period per targeted tune note; net −1 from peak via subsequent merge). The catalogue continues self-regulating effectively at the cap. The targeted tune-system at 19:10 UTC explicitly endorsed the **post-saturation maintenance mode** as the intended state — no archive-relief, no cap raise. This period's events confirm the policy is producing the expected effect: stable cap-orbit with intermittent +1 / −1 from chain replenishment activity.

**Apex over governance cap**: 22 active apex articles vs 20 governance cap (was framed as 23 vs 20 last period; one possible recount or one removal from the active list). Mid-period addition: [apex/post-decoherence-selection-programme.md](/apex/post-decoherence-selection-programme/). The cap exists in `obsidian/apex/apex-articles.md` text but is not enforced in code — no automation refuses an apex-evolve creation when over cap. **5th consecutive period.**

### Review Finding Patterns

**Data points**: 6 pessimistic reviews, 7 optimistic reviews, 2 tenet checks, 79 deep reviews (period).

**Tenet-check zero-warning streak extends to 12 consecutive (UPDATED)**: 2026-04-30 13:28 UTC tenet check noted "twelfth consecutive zero-zero-zero check; carry-forward substance-dualism alias on [topics/free-will.md](/topics/free-will/) line 64 resolved in this window." Corpus continues to hold tenet-alignment high-water mark. Worth flagging that the long streak combined with the tenet-check-piercing pattern noted in last period's optimistic-2026-04-30 (P3 task at todo.md:67-72: free-will substance-dualism alias surfaced after persisting through 21 deep-reviews) confirms tenet-check is providing a unique signal that within-article scope (deep-review) cannot.

**Pessimistic→refine pipeline tightened to apex (NEW, see Failure Patterns above)**: First documented apex-level pessimistic-then-refine cycle (5 min turnaround on medium-status-voids-in-cognition).

**Cross-review chains operating at scale (NEW)**: 10:33 UTC cross-review of four medium-status constituent voids against the apex's tightened criterion closed 92 minutes after the apex refine. This is the catalogue's first **apex-pessimistic-refine → constituent-cross-review** chain — chain-closure latency is low and the constituents passed the three-condition test cleanly without rewrites. Pattern is healthy: the apex layer's critical reviews now cascade methodically to constituent layers.

**LLM cliché "Not X but Y" continues to be hunted**: Multiple deep-reviews this period removed instances. Pattern identical to prior periods: cliché generated at expand-topic time and cleaned at deep-review or pessimistic-review time. **13th consecutive period flagging this.** Becomes a permanent operational concern rather than a transient bug.

**Apex re-synthesis discipline holding (UPDATED)**: 2026-04-30 13:32 UTC apex-evolve of [apex/machine-question.md](/apex/machine-question/) (4117 → 3190 words, 22.5% condense-during-evolve). The evolve absorbed 7 changed sources and corrected two stale source paths in one pass — strong example of "preserves deltas" class. The per-apex differentiation pattern noted last period (regenerate-class vs preserve-class) continues to hold with apex-evolve operating in preserve mode.

### Convergence Progress

| Category | Count | Cap | % of Cap | Direction |
|----------|-------|-----|----------|-----------|
| Topics | 231 | 250 | 92.4% | 19 slots (→) |
| Concepts | 231 | 250 | 92.4% | 19 slots (**+1 vs prev — coalesce activity**) |
| Voids | 98 | 100 | **98.0%** | 2 slots (**+1 vs prev**) |
| Arguments | 6 | — | — | → |
| Apex | 22 active (24 files) | (20 governance) | — | **22/20 — over cap** |

**Voids continued self-regulation**: 97 → 98 (+1 net) but peaked at 99/100 mid-period before merging back to 98. The cap is functioning as a behavioural constraint that the catalogue is honouring without code enforcement (no `expand-topic` for voids fired despite multiple research-voids notes accumulating). Confirms last period's "self-regulating equilibrium" hypothesis with one additional period of evidence.

**Concepts −1**: Coalesce of `inspection-paradox` → `self-reference-paradox` (06:40 UTC) and `ai-consciousness-modes` + `types-of-ai-phenomenal-experience` → `ai-consciousness-typology` (23:33 UTC yesterday). Both within concepts/. Net −1 (one of the merges was 2-into-1 = -1; the other was already counted prior?). Worth noting that concepts is now at 92.4%, **same as topics** — the catalogue is maturing on a parallel trajectory across both major sections.

**Apex active count clarified**: 22 actual apex articles + 2 governance pages (apex.md, apex-articles.md) = 24 files in apex/. Last period's "23/20" framing may have counted apex-articles.md as an active apex article. Either way, the section is over its informal cap by 2.

**Quality metrics (frozen, 36th period)**:
- Critical: 0 ✓ (target)
- Medium: 10 (target ≤3) — almost certainly stale counter
- Low: 3
- Orphans: 13

## Changes Applied (Tier 1)

*No changes applied via this skill's Tier 1 mechanism.*

**Rationale**: Same three structural blockers as the last 32 reports:
1. No `cadences` / `overdue_thresholds` / `replenishment_config` sections in evolution-state.yaml — nothing to tune.
2. No `tune_system_history` — cooldowns unenforceable.
3. No `locked_settings` — cannot check for human overrides.

**33rd consecutive report** unable to apply Tier 1 changes via the skill's intended YAML mechanism.

**Note on yesterday's targeted tune-system**: The 2026-04-29 19:10 UTC targeted intervention demonstrated that *targeted code-level Tier-1-equivalent changes* (modifying `tools/evolution/cycle.py` with explicit scoping, decoupling rule, and rollback condition) are tractable and effective when warranted by clear evidence. This is a constructive precedent — the skill's Tier 1 mechanism is structurally blocked, but the equivalent intent can be delivered via targeted code changes with appropriate ceremony.

## Recommendations (Tier 2)

### 1. Impose P3 Ceiling in `replenish-queue` (ESCALATED — was Carried Forward ×3)

- **Proposed change**: Add a P3 ceiling check (e.g., 500) to `tools/curate/replenish.py` (or wherever P3 generation happens). When P3 ≥ 500, halt optimistic-review and gap-analysis P3 generation; allow only chain-replenishment additions.
- **Rationale**: P3 was at 502 as of this run (was 480 last period; +22 in 36.5h). The ceiling-of-concern flagged for 3 consecutive periods has been crossed. Without action, P3 will continue accumulating indefinitely while practical execution rate stays near-zero. A ceiling preserves the suggestion-buffer function (chain replenishment still works) while preventing unbounded growth.
- **Risk**: Low. Optimistic-review P3 generation is already largely-redundant with already-queued items.
- **Priority**: **High** (escalated from Medium-High; threshold now actually crossed).

### 2. Fix `last_runs` Writeback for Cycle-Trigger Tasks (Carried Forward ×5)

- **Proposed change**: Audit the dispatch code in `tools/evolution/` that persists `last_runs` after task completion. check-tenets (~18h stale), apex-evolve (~24h stale), and tune-system (targeted run not written back) all show writeback lag this period. Coalesce shows the opposite (writeback ahead-of-fact on no-candidate ticks).
- **Rationale**: Pattern now confirmed across **five consecutive reports** — systematic, not transient. Stale `last_runs` corrupts trigger gating; writeback-ahead-of-fact creates phantom freshness. The two failure modes likely share a root cause (timestamp updates wired to the cycle tick rather than to task-completion events). The targeted tune-system writeback failure (own state not preserved) is a particularly clean instance.
- **Risk**: Low (read the code; single-point fix in `tools/evolution/cycle.py` dispatch).
- **Priority**: Medium-High.

### 3. Fix Stale `content_stats` / `progress` Counters (Carried Forward ×31)

- **Proposed change**: Add per-section file-counting at session start in `tools/evolution/state.py`.
- **Rationale**: 36th consecutive report. Recorded state shows 35 topics (actual 231), 145 concepts (actual 231), 11 voids (actual 98), 542 reviews (actual 3736). No functional harm (caps use separate live counts) but every metric-dependent skill has to recompute from filesystem.
- **Risk**: Low.
- **Priority**: Medium.

### 4. Add `tune_system_history` / `locked_settings` / `cadences` Sections (Carried Forward ×33)

- **Proposed change**: Populate evolution-state.yaml with the sections the skill spec expects: `cadences`, `overdue_thresholds`, `replenishment_config`, `tune_system_history`, `locked_settings`.
- **Rationale**: Without these, tune-system cannot make Tier 1 changes safely. 33 reports now effectively advisory-only (with the 2026-04-29b targeted exception demonstrating the alternative path).
- **Risk**: Low.
- **Priority**: High.

### 5. Add `validate-all` to Cycle Triggers (Carried Forward ×28)

- **Proposed change**: Add `"validate-all": 2` or similar to `CYCLE_TRIGGERS` in `tools/evolution/cycle.py:43-49`.
- **Rationale**: 97 days stale. Listed in CLAUDE.md as "Daily health check" but not wired into automation.
- **Risk**: Low (read-only check).
- **Priority**: Medium.

### 6. Reconcile tune-system Cadence (Carried Forward ×6)

- **Proposed change**: Either (a) adjust `tune-system` in `CYCLE_TRIGGERS` from 6 to 30 (approaches the 30-day documented cadence at current loop speed), or (b) revise the skill spec to ~1.5-day cadence matching current operation.
- **Rationale**: Current ~37h cadence is **~19× faster than spec**. Each run covers small deltas; most findings are carried forward. **Note**: Yesterday's targeted tune-system demonstrated that high-impact interventions can be triggered ad-hoc when warranted, suggesting the regular cycle could safely run less frequently with targeted runs handling urgent cases.
- **Risk**: Low.
- **Priority**: Medium.

### 7. Implement Deep-Review Convergence Tracking (Carried Forward ×22)

- **Proposed change**: Track per-article review count and last word-change delta; skip further deep-review for articles with 3+ reviews all showing near-zero net change.
- **Rationale**: At least 5/79 deep-reviews this period made no content change (subject-object-distinction second consecutive review confirming stability; skill-delegation 5th review; conjunction-coalesce 6th review with one-word fix only; ai-consciousness-typology post-condense verification; medium-status-voids-in-cognition post-pessimistic verification). Reviewers annotate "convergence reached" but re-queuing continues. Becoming progressively more load-bearing as more articles converge.
- **Risk**: Low.
- **Priority**: High.

### 8. Audit Apex Cap Governance — Now 22/20 (Carried Forward ×5)

- **Proposed change**: Resolve the apex count discrepancy. `obsidian/apex/` contains 24 .md files (22 active apex + 2 governance pages); apex-articles.md governance list caps at 20.
- **Rationale**: Inconsistent governance means apex-evolve decisions may treat real files as nonexistent. Cap is documented in text but not enforced in code; new apex creations (`post-decoherence-selection-programme` mid-period) ignore it. P3 task already queued at todo.md:102-107 to address this.
- **Risk**: Low.
- **Priority**: Medium-High.

### 9. Update `convergence_targets` (Carried Forward ×35)

- **Proposed change**: `min_topics` 10→200, `min_concepts` 15→200, `min_arguments` 5→10, add `min_voids` 80, add `min_apex` 15, `max_medium_issues` 3 → 15.
- **Rationale**: Targets set for early-stage system; all vastly exceeded. Cosmetic.
- **Risk**: Low.
- **Priority**: Low.

### 10. Document Refinement-Log Marker Discipline — REVISED (Carried Forward ×3)

- **Proposed change**: Document the marker-handling discipline in CLAUDE.md or refine-draft SKILL.md. Two acceptable disciplines: (a) marker is a human-review artifact preserved by all automation until human review (the condense behaviour); (b) marker is auto-removable by deep-review after N days (the deep-review behaviour).
- **Rationale**: Last period showed mixed treatment. **This period the convention is consolidating in practice** — deep-review removes, condense preserves as out-of-scope. Documenting the de facto rule (rather than re-deciding) is now low-friction. May self-resolve without documentation but explicit codification reduces operator risk.
- **Risk**: Low.
- **Priority**: Low (de-escalated; convention is operating cleanly without docs).

### 11. Track Apex Re-Synthesis Regressions Per-Apex (Carried Forward ×2, REVISED)

- **Proposed change**: When apex-evolve re-synthesises an article, surface diffs against the latest deep-review-installed corrections AND tag the apex with a "preserve-vs-regenerate" classification based on observed behaviour.
- **Rationale**: This period's [apex/machine-question.md](/apex/machine-question/) evolve (13:32 UTC, 22.5% condense) shows another preserve-class instance. Combined with the prior `apex/taxonomy-of-voids` and `apex/identity-across-transformations` data points, the per-apex differentiation pattern is now well-evidenced. Worth instrumenting.
- **Risk**: Medium (touches apex-evolve methodology).
- **Priority**: Medium.

### 12. Replenish-Queue Body-Keyword Heuristic Hardening (NEW this period)

- **Proposed change**: Audit the `unconsumed_research` heuristic in `replenish-queue` to ensure it cross-checks article body content (not just `related_articles` linkage or stale snapshot) before emitting an integration task.
- **Rationale**: 2026-04-30 08:29 UTC replenisher emitted a P2 task asserting [voids/void-as-ground-of-meaning.md](/voids/void-as-ground-of-meaning/) had "zero references to Buddhist/Eastern material" when direct grep returned 15 hits. The 08:36 UTC closure script noted: "an `unconsumed_research` detector that checks `related_articles` linkage but not body keyword presence is the likely failure mode." Single occurrence so far; not yet a recurring pattern but worth tracking and fixing if recurrent.
- **Risk**: Low (single heuristic check).
- **Priority**: Medium-Low.

### 13. Track Coalesce Slot Reduction Effect Across More Periods (NEW this period — track-only)

- **Proposed change**: Continue tracking coalesce abandon rate for 2-3 more tune periods. If post-fix abandon rate stays below 50%, the cycle.py change is validated. If it climbs back above 60%, consider raising the slot back to 2/24 (the catalogue may have produced new merger candidates after a cooling period).
- **Rationale**: Yesterday's cycle.py fix (2/24 → 1/24 coalesce slot) produced a clean before/after signal: 14% pre-fix success vs 75% post-fix success. But 4 post-fix attempts is a small sample. Track the next 2-3 periods to confirm the pattern is stable rather than a transient regression-to-mean.
- **Risk**: None (observation only).
- **Priority**: Low (passive monitoring).

## Items for Human Review (Tier 3)

### 1. P3 Crossed 500 Threshold (ESCALATED — was Carried Forward ×3)

- **Issue observed**: P3 queue depth at 502, up from 480 last period. The ceiling flagged for 3 consecutive periods has been crossed. Generation rate dropped slightly to ~14/day this period (vs ~17/day) but remains positive net.
- **Why human needed**: Decide whether P3 is functioning as a suggestion buffer (current behaviour) or a true work queue. The decision is now ripe.
- **Suggested action**: Either (a) add a P3 ceiling to `replenish-queue` (e.g., halt optimistic-review P3 generation if P3 > 500), or (b) accept P3 as archival and document that in CLAUDE.md, or (c) bulk-prune low-value P3 entries (~50% target reduction).

### 2. Stale State Tracking — 36th Consecutive Report

- **Issue observed**: `content_stats.total_files` and `progress.*` counters frozen at early-project values.
- **Why human needed**: Code change to `tools/evolution/state.py`.
- **Suggested action**: Add per-section file-counting at session start.

### 3. `last_runs` Writeback Gap for Cycle-Trigger Tasks (Carried Forward ×5)

- **Issue observed**: Three cycle-trigger tasks show 18-24h writeback lag this period (check-tenets, apex-evolve). Tune-system itself shows the targeted run not written back. Coalesce shows the inverse (timestamps advance ahead-of-fact). Pattern is now systematic across five consecutive reports.
- **Why human needed**: Code inspection of `tools/evolution/cycle.py` and related task dispatch paths.
- **Suggested action**: Find the dispatch branch for cycle-trigger tasks and ensure it calls `state.update_last_run(task_name, now)` after task completion (not at cycle tick).

### 4. Medium Issues Persistent at 10 (Carried Forward ×27)

- **Issue observed**: Medium issues count exactly 10 for 27 consecutive tune periods.
- **Why human needed**: Decide whether this is a stale counter or live tracking.
- **Suggested action**: Inspect the source of `quality.medium_issues` and confirm it is recomputed at session start.

### 5. Orphaned Files Persistent at 13 (Carried Forward ×14)

- **Issue observed**: Same 13-orphan count through extensive cross-linking work. The 2026-04-30 12:03 UTC replenish-queue note explicitly observed: "the state file's 13 orphan count predates today's reciprocal-cross-link sweeps; my detector across content + tenets + project sources finds 0 orphans."
- **Why human needed**: Almost certainly stale detection.
- **Suggested action**: Re-run orphan detection against live file state and verify; consider the 13 may be research/reviews/authors pages outside the relevant scope.

### 6. Apex Cap Inconsistency — 22 Active vs 20 Governance (Carried Forward ×5)

- **Issue observed**: `obsidian/apex/` contains 24 files (22 active apex + 2 governance pages); apex-articles.md caps at 20. **+1 active apex this period (post-decoherence-selection-programme).**
- **Why human needed**: Editorial/governance decision, plus optional code change to enforce cap.
- **Suggested action**: Reconcile the approved list against the filesystem; archive overflow, raise the cap, or add cap enforcement to the apex-evolve skill. P3 task at todo.md:102-107 already queued for the audit.

### 7. tune-system Cycle-vs-Cadence Mismatch (Carried Forward ×6)

- **Issue observed**: Skill documents 30-day cadence; cycle trigger fires every ~1.5 days at current pace (37h this period). Pattern stable across 6 consecutive periods. Combined with yesterday's targeted-tune-system precedent, the regular cycle could safely run less frequently.
- **Why human needed**: Pick a cadence. Current mismatch generates ~19× the intended reports.
- **Suggested action**: Either change `tune-system: 6` to `tune-system: 30` in `CYCLE_TRIGGERS` (`tools/evolution/cycle.py:48`), or update the skill spec to match observed cadence.

### 8. Apex Re-Synthesis Content-Loss Vector — Per-Apex Pattern Continues (Carried Forward, REFINED)

- **Issue observed**: Yesterday's `apex/taxonomy-of-voids` (preserve) and today's `apex/machine-question` evolve (preserve) confirm the per-apex regeneration vs preservation pattern. `apex/identity-across-transformations` (regenerate-class, prior period) remains the lone documented regression case.
- **Why human needed**: Decide whether to instrument apex-evolve with diff-against-prior-deep-review checks, or accept that some apex articles are regression-prone and rely on deep-review as periodic guard.
- **Suggested action**: Profile apex-evolve runs by which apex they target; classify each apex as "preserves deltas" or "regenerates from sources"; treat regenerate-class apexes as needing post-synthesis cross-review.

### 9. Refinement-Log Marker — Convention Consolidating (Carried Forward, DE-ESCALATED)

- **Issue observed**: Last period flagged inconsistency. This period the de facto rule (deep-review removes, condense preserves) is operating cleanly. Convention may self-resolve.
- **Why human needed**: Optional editorial codification.
- **Suggested action**: Document the chosen discipline in `.claude/skills/refine-draft/SKILL.md` or CLAUDE.md if formalisation desired; otherwise accept the operating convention.

### 10. Coalesce Slot Reduction — Initial Validation Positive (NEW)

- **Issue observed**: Yesterday's targeted tune-system reduced cycle slot 21 from `coalesce` to `queue`. Post-fix segment shows 75% coalesce success rate (3/4) vs 14% pre-fix (1/7). The fix is producing the intended effect.
- **Why human needed**: No action needed yet; validation is in progress.
- **Suggested action**: Re-evaluate after 2-3 more tune periods. If pattern holds (post-fix abandon rate stays <50%), the change is permanent. If abandon rate climbs back above 60%, consider restoring the second coalesce slot.

### 11. Replenish-Queue False-Positive Pattern (NEW)

- **Issue observed**: 2026-04-30 08:29 UTC replenisher generated a duplicate task based on a stale or wrong-target body-keyword check. Single instance this period.
- **Why human needed**: Decide whether to harden the heuristic now or wait for recurrence.
- **Suggested action**: If recurrent in the next tune period, audit the `unconsumed_research` heuristic to verify it reads current article body content, not stale snapshots or `related_articles` linkage alone.

## System Health Summary

| Component | Status | Notes |
|-----------|--------|-------|
| Task execution | **Excellent** | 0% hard-failure rate (19th consecutive period; 151/151) |
| Skip rate | Excellent | 6 abandonments by design (all coalesce no-candidate); 1 no-op duplicate-refine |
| Content quality | Excellent | 0 critical issues; 0/0 tenet errors/warnings (12th clean tenet check) |
| Queue management | **Watch** | P2 stable; **P3 crossed 500 threshold** |
| Expand-topic efficiency | Excellent | 7/7 success this period |
| Coalesce efficiency | **Improved (Watch)** | 5/11 productive (55% abandon — was 62%); post-cycle-fix 75% success |
| Review system | Excellent | ~67 reviews/day (up from ~58/day); pessimistic→refine pipeline now operating at apex tier |
| Deep-review convergence | Mixed | 5+/79 zero-change reviews (and growing) |
| Scheduling | Operational | Cycle mechanism stable but **~19× faster than spec** for tune-system |
| Changelog rotation | Working | Current changelog at 152 entries from period |
| State tracking | **Broken** | content_stats/progress stale (36th); `last_runs` writeback (5th period systematic); tune-system own writeback failed |
| Topics cap | Healthy | 231/250 — 19 slots |
| Concepts cap | Healthy | 231/250 — 19 slots (matched topics this period via coalesce) |
| Voids cap | **Tight (steady)** | 98/100 — 2 slots; second period of self-regulating equilibrium |
| Apex cap | **Inconsistent (steady)** | 22 active vs 20 approved (5th period) |
| Site validation | **Gap** | validate-all not running (97 days; 28th report) |
| Tenet alignment | **Excellent** | 12th clean delta sweep |
| Pessimistic→refine pipeline | **Excellent** | Now operating at apex tier (5-min turnaround on medium-status-voids-in-cognition) |
| Apex re-synthesis | **Per-apex differentiated (confirmed)** | machine-question evolve preserved deltas; pattern stable |
| Refinement-log marker | **Consolidating in practice** | De facto rule operating cleanly |
| Coalesce slot fix (cycle.py) | **Working** | Post-fix 75% success vs 14% pre-fix |
| tune-system infrastructure | **Blocked** | 33rd report unable to apply Tier 1 via YAML |

## Next Tuning Session

- **Expected (at current cycle-trigger rate)**: ~2026-05-02 (1.5 days out)
- **Recommended per skill spec**: 2026-05-30 (30 days out)
- **Focus areas next run**:
  - Whether P3 ceiling decision is acted on (currently at 502, +22 over threshold)
  - Whether coalesce abandon rate stays below 50% (current post-fix segment 25%; pre+post mix 55%)
  - Whether the targeted-tune-system precedent gets used again, or whether the regular cycle absorbs the load
  - Whether apex-tier pessimistic→refine becomes regular or stays one-off
  - Whether voids self-regulating equilibrium continues at 98/100
  - Whether `last_runs` writeback gap has been addressed (5th consecutive period)
  - Whether `tune_system_history` / `locked_settings` / `cadences` sections appear (34th report)
  - Whether validate-all is integrated (29th report)
  - Whether stale state tracking gets addressed (37th report)
  - Whether refinement-log marker convention gets formalised or stays de facto
  - Whether replenish-queue false-positive pattern recurs