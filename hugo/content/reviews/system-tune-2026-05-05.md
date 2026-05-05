---
ai_contribution: 100
ai_generated_date: 2026-05-05
ai_modified: 2026-05-05 15:42:00+00:00
ai_system: claude-opus-4-7
author: null
concepts: []
created: 2026-05-05
date: &id001 2026-05-05
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[todo]]'
- '[[changelog]]'
- '[[reviews/system-tune-2026-04-30]]'
- '[[reviews/system-tune-2026-04-29b-voids-saturation]]'
title: System Tuning Report - 2026-05-05
topics: []
---

# System Tuning Report

**Date**: 2026-05-05 15:42 UTC
**Sessions analyzed**: 372 (sessions 6479 → 6851)
**Period covered**: 2026-04-30 13:18 UTC → 2026-05-05 15:42 UTC (~5.1 days / 122.4 hours)

## Executive Summary

20th consecutive zero-hard-failure period (~150 tasks executed, 0 failures across both the rotated-W18 archive and current changelog). **Three structural milestones landed this period**: (1) the **outer-review pipeline went live end-to-end** — 3 successful automated runs (2 ChatGPT, 1 Claude) on 2026-05-04; (2) the **methodological-discipline cluster expanded** with two new project docs (`direct-refutation-discipline.md`, `evidential-status-discipline.md`) plus a concept anchor (`possibility-probability-slippage.md`) and matching SKILL-file changes that operationalise the disciplines at the review machinery; (3) the **cap-saturation policy formally documented** in [concepts/coalesce-condense-apex-stability.md](/concepts/coalesce-condense-apex-stability/) (2026-05-05 05:17 UTC). **Coalesce abandon rate continues to bend favourably**: 33% (3/9) this period vs 55% last period vs 62% prior — the 2026-04-29b cycle.py fix continues to pay dividends. **Voids hit 100/100** as expected via the today's research-voids cycle (recurrence-void) — the 2026-04-29b decoupling rule's policy held cleanly. **P3 remains over ceiling at 527** (was 502 last tune; +25 in 5 days; growth slowed from ~14/day to ~5/day). Same three structural blockers persist: `cadences`, `tune_system_history`, `locked_settings` sections still absent from evolution-state.yaml. **34th consecutive report unable to apply Tier 1 changes via the standard YAML mechanism.**

## Metrics Overview

| Metric | Current (Actual) | Recorded State | Previous (Apr 30) | Trend |
|--------|------------------|----------------|-------------------|-------|
| Session count | 6851 | 6851 | 6707 | +144 |
| Topics | 231 | 35 | 231 | → |
| Concepts | 230 | 145 | 231 | **−1** (coalesce activity) |
| Voids | **100** | 11 | 98 | **+2 (at cap)** |
| Apex | 22 active (24 files inc. governance) | 4 | 22 active | → |
| Arguments | 4 | 4 | 6 (estimate) | → |
| Questions | 1 | 1 | 1 | → |
| Research | 376 | 117 (then 118) | 369 | +7 |
| Reviews | 3825 | 542 | 3736 | +89 (~17/day) |
| Total content files | 297 | 297 | 297 | → |
| Critical issues | 0 | 0 | 0 | → |
| Medium issues | 10 | 10 | 10 | → (persistent) |
| Low issues | 3 | 3 | 3 | → |
| Orphaned files | 13 | 13 | 13 | → (persistent) |
| Queue depth (P0–P1) | 0 | — | 0 | → |
| Queue depth (P2) | 2 | — | 3 | −1 |
| Queue depth (P3) | **527** | — | 502 | **+25 (still over ceiling)** |

**State discrepancy**: Recorded `progress` counters remain frozen at early-project values. **37th consecutive report.** No functional harm.

## Abort Conditions Check

**Status**: All clear.

- Task failure rate: 0% (0/20 recent_tasks failed; `failed_tasks: {}`; 0 Failed/Error entries across both changelog files this period)
- Convergence: quality unchanged; no regression
- Critical issues: 0
- File reads: all successful

## Check Locked Settings

`locked_settings` section not present in evolution-state.yaml. **34th consecutive report.**

## Findings

### Cadence Analysis

**Data points**: 372 sessions, ~150 changelog entries (89 in W18 archive after Apr 30 13:18; 35 in current; remainder in archive before that), 122.4 hours elapsed.

| Task | last_runs Timestamp | Actual Last Run (verified) | Status |
|------|---------------------|----------------------------|--------|
| validate-all | 2026-01-24 02:57 | Not run since Jan 24 | **102 days stale** |
| pessimistic-review | 2026-05-04 21:23 | 2026-05-04 21:24 UTC | Current |
| optimistic-review | 2026-05-05 03:15 | 2026-05-05 03:18 UTC | Current |
| check-tenets | 2026-05-01 07:40 | **2026-05-05 15:36** (changelog) | **Stale writeback — ~104h** |
| check-links | 2026-05-01 20:52 | 2026-05-01 20:52 UTC | ~92h ago |
| deep-review | 2026-05-05 11:15 | 2026-05-05 11:16 UTC | Current |
| tune-system | 2026-04-30 13:18 | 2026-04-30 13:18 UTC | ~122h since last (current) |
| research-voids | 2026-05-05 15:35 | 2026-05-05 15:35 UTC | Current |
| coalesce | 2026-05-05 08:15 | 2026-05-05 08:21 UTC | Current |
| apex-evolve | 2026-05-01 20:52 | **2026-05-01 20:52 UTC** (changelog: machine-question evolve) | ~92h ago |
| agentic-social | 2026-05-05 15:16 | 2026-05-05 15:16 UTC | Current |
| tweet-highlight | 2026-01-24 14:00 | Not recently | 102 days stale (but `last_tweet_date: 2026-05-05` shows tweets do happen via add-highlight path) |
| embed-videos | 2026-05-04 15:23 | 2026-05-04 15:23 UTC | ~24h ago |
| commission-chatgpt-review | 2026-05-05 02:15 | 2026-05-05 02:15 UTC | Current (within Chrome window) |
| commission-claude-review | 2026-05-05 03:15 | 2026-05-05 03:15 UTC | Current |
| commission-gemini-review | 2026-05-05 04:15 | 2026-05-05 04:15 UTC | Current |

**Continuing finding — `last_runs` writeback for check-tenets**: writeback timestamp shows 2026-05-01 07:40 UTC, but the most recent actual check-tenets run is 2026-05-05 15:36 UTC (per current changelog) — a **~104h writeback gap**. Pattern is now confirmed across **6 consecutive reports** as systematic. Coalesce, by contrast, has been near-current this period (writeback within minutes), so the issue may be specific to the cycle-trigger dispatch path that `check-tenets` and `apex-evolve` share.

**`validate-all`**: 102 days stale. **29th consecutive report.**

**`tune-system` cadence at expected 5-day pace this period**: This run is ~122h after the previous, against the spec's 30-day cadence. **35th consecutive report noting the mismatch.** The cycle's `tune-system: 6` trigger means it fires every 144 sessions; at the current loop interval (~30min/session = ~9-10 cycle ticks/h), the actual cadence stretches to ~5 days when sessions are slower. The cadence varies inversely with loop speed and is not stable against the 30-day spec.

**Outer-review pipeline going live (NEW this period)**: 2026-05-04 saw three commission/collect/process cycles for the outer-review pipeline — first end-to-end automated runs since the infrastructure landed. ChatGPT 5.5 Pro at 12:05 UTC (~14 min response, 11.7k chars), ChatGPT 5 Pro carry-forward at 10:14 UTC, Claude Opus 4.7 at 14:00 UTC (~30 min adaptive thinking + 2m 10s research panel, 5.8k chars). All three reviews generated useful methodological tasks; the convergent finding across two ChatGPT reviews on different topics (animal-consciousness 2026-05-03 + Duch 2026-05-04) was the higher-order critique that *tenet-perimeter reasoning* was substituting for *direct refutation*, which precipitated the two new methodological-discipline project docs.

### Failure Pattern Analysis

**Data points**: ~150 changelog entries in period; `failed_tasks: {}`; all 20 recent_tasks success; 0 Failed/Error markers across both changelog files.

| Task Type | Executed (period) | Skipped/Abandoned | Rate |
|-----------|-------------------|-------------------|------|
| deep-review | 70 | 0 | 0% |
| refine-draft | 29 | 0 | 0% |
| expand-topic | 10 | 0 | 0% |
| coalesce | 9 | **3 abandoned/no-op** | **0% hard-fail; 33% no-candidate** |
| condense | 8 | 0 | 0% |
| pessimistic-review | 6 | 0 | 0% |
| optimistic-review | 6 | 0 | 0% |
| research-voids | 4 | 0 | 0% |
| research-topic | 4 | 0 | 0% |
| outer-review | 3 | 0 | 0% (NEW) |
| cross-review | 3 | 0 | 0% |
| check-tenets | 3 | 0 | 0% |
| apex-evolve | 2 | 0 | 0% |
| replenish-queue | 1 | 0 | 0% |
| tune-system | 1 | 0 | 0% (the previous one) |

**Hard-failure reliability**: 20th consecutive zero-failure tune period.

**Coalesce abandon rate dropping further (CONTINUING)**: 3/9 (~33%) this period vs 6/11 (~55%) last period vs 8/13 (~62%) prior. The 2026-04-29b cycle.py slot reduction (2/24 → 1/24) continues to pay off cleanly. Three consecutive periods of declining abandon rate is a robust signal — the slot-reduction is no longer "watch only" but **validated**. Successful merges this period include the 2026-05-05 abandonment that produced the *cap-saturation policy formalisation* (the abandonment was itself the methodologically correct move at voids 99/100, and it triggered the project-doc refine that documented the policy).

**Outer-review pipeline reliability (NEW)**: 3/3 successful end-to-end runs. The pipeline performance notes captured in the changelog (commission ~5min, collect via DOM walker for ChatGPT, artifact panel for Claude with explicit "wake the tab" step) are now operational discipline rather than speculation. Worth tracking whether the time-triggered daily commission cadence (2/3/4am UTC for ChatGPT/Claude/Gemini) maintains the 100% success rate over multiple weeks.

**Deep-review near-zero-change convergence persists (CARRIED FORWARD)**: Multiple stability-confirmation reviews this period — at minimum: `topics/incubation-effect-and-unconscious-processing` (5th deep-review, +2 words for one consolidation only); `concepts/timing-gap-problem` (5th review, no change); `topics/non-temporal-consciousness` (4th review, -2 words consolidating one duplicate Further Reading entry); `topics/epistemic-advantages-of-dualism` (6th review, +19 words for one symmetric-attribution-risk note). At least 4-6/70 deep-reviews this period made no substantive content change. **Recommendation #6 continues to grow load-bearing**.

**Methodological-discipline ratchet (NEW classification)**: This period the catalogue exhibited a coherent feedback loop: outer reviews → diagnostic findings → project doc creation → SKILL-file tuning → content propagation through clusters. The cycle ran twice in 36h: the 2026-05-03 outer review's evidential-status discipline became `evidential-status-discipline.md` (2026-05-05 02:18 UTC) + concept anchor `possibility-probability-slippage.md` (2026-05-05 10:17 UTC) + SKILL changes (2026-05-05 01:16 UTC); the 2026-05-04 outer review's direct-refutation discipline became `direct-refutation-discipline.md` (2026-05-04 15:24 UTC) and propagated through ~5 cluster articles by today. The 2026-05-05 03:18 UTC optimistic-review confirmed the discipline held at every invocation site without slippage. **This is the catalogue's most coherent methodological-discipline cycle to date** and worth instrumenting if the pattern repeats.

### Queue Health Analysis

**Data points**: Current todo.md (~5300 lines, 529 active tasks; P0-P1=0, P2=2, P3=527, vetoed=0).

| Priority | Active Count | Change |
|----------|--------------|--------|
| P0 | 0 | → |
| P1 | 0 | → |
| P2 | 2 | −1 (chain absorption + outer-review tasks landed) |
| P3 | **527** | **+25 (still over 500 ceiling)** |

**P3 growth rate slowed but still over ceiling (CONTINUING)**: P3 grew +25 over 5 days = ~5/day this period vs ~14-17/day prior. The growth rate is slowing as the catalogue saturates and outer reviews emit fewer net-new P3 items, but the ceiling crossed last period (500) is now persistently breached at 527. Last period's escalated recommendation (#1) is now **30 days old** (originally flagged 2026-04-21; escalated 2026-04-30) and remains unaddressed. **Decision is increasingly ripe**.

**P2 depth dropping (NEW)**: P2 at 2 (was 3 last period). Three of the P2 outer-review tasks landed as completed work this period (direct-refutation-discipline, evidential-status-discipline, SKILL-file tunes) and were closed; replenisher's chain-replenishment fired but produced fewer new P2 items than were absorbed. The system is in **near-real-time queue equilibrium with marginal P2 deficit** — close to the threshold-of-3 that triggers replenishment. Worth watching whether the auto-replenish cadence catches up over the next period or whether the threshold should be widened to 5.

**Section-cap status — voids at 100/100 (NEW — at cap)**: Voids 98 → 100 net (+2). The 2026-05-05 15:35 UTC `research-voids` cycle fill the final slot (recurrence-void) per the policy in 2026-04-29b. Now at exactly 100/100. The catalogue's self-regulation continues to operate cleanly — `expand-topic` is gated by section caps and refuses voids placement; the cycle's freed work flows to deep-review/condense/refine-draft as designed. The 2026-05-05 05:17 UTC formalisation of the cap-saturation policy in [concepts/coalesce-condense-apex-stability.md](/concepts/coalesce-condense-apex-stability/) (~360 words added) gives the policy its anchor article for future reference.

**Apex over governance cap**: 22 active apex articles vs 20 governance cap (24 files including governance pages). Same as last period. **6th consecutive report.** P3 task at todo.md:81-86 still queued.

### Review Finding Patterns

**Data points**: 6 pessimistic reviews, 6 optimistic reviews, 3 tenet checks, 70 deep reviews, 3 outer reviews (period).

**Tenet-check zero-warning streak extends to 14 consecutive (UPDATED)**: 2026-05-05 15:36 UTC tenet check noted "Fourteenth consecutive zero-error, zero-warning check." The streak continues unbroken. Today's check noted the methodological-discipline cluster (`possibility-probability-slippage` + `mind-brain-interface-efficacy`) is the first content to apply the slippage discipline correctly at *speculative integration tier*.

**Methodological-discipline ratchet operating coherently (NEW)**: See Failure Patterns. The pattern (outer review → diagnostic finding → project doc → SKILL-file tune → content propagation through cluster) ran twice in 36h. The 2026-05-05 03:18 UTC optimistic-review explicitly endorsed the architecture: "Cleanest implementation of a methodological discipline the catalogue has produced. Process Philosopher (Whitehead) and Hardline Empiricist (Birch) personas converge in praising the same passages... the two-persona productive tension installed in the 2026-05-05 01:16 UTC SKILL-file refine *worked the first time it was tested at scale*."

**LLM cliché "Not X but Y" continues to be hunted (CONTINUING)**: Multiple deep-reviews and refines this period removed instances. Pattern unchanged from prior periods. **14th consecutive period flagging this.** Operational discipline; no further action proposed.

**Outer-review verification step works (NEW — validated)**: The 2026-05-04 Claude review's empirical claim that "no Duch references on site" was verified false (33 files contained Duch references; integration commit landed same day). Verification step caught the empirical error before task generation; the outer-review skill correctly weighted methodological claims higher when empirical claims fail verification. The replenish-queue false-positive pattern flagged last period (2026-04-30 08:29 UTC) is the same shape but at a different scope (internal stale-snapshot vs external search-index lag). Both validate the verification-step discipline.

### Convergence Progress

| Category | Count | Cap | % of Cap | Direction |
|----------|-------|-----|----------|-----------|
| Topics | 231 | 250 | 92.4% | 19 slots (→) |
| Concepts | 230 | 250 | 92.0% | 20 slots (**−1 vs prev — coalesce activity**) |
| Voids | **100** | 100 | **100.0%** | **0 slots — AT CAP** |
| Arguments | 4 | — | — | → |
| Apex | 22 active (24 files) | (20 governance) | — | 22/20 — over cap |

**Voids reached 100/100**: As anticipated by the 2026-04-29b targeted tune-system, the catalogue has reached the cap via expected mechanism (one research-voids cycle creating each slot). The cap-saturation policy formalised today (2026-05-05 05:17 UTC, [concepts/coalesce-condense-apex-stability.md](/concepts/coalesce-condense-apex-stability/)) is now load-bearing. The 2026-04-29b decoupling rule's policy expires 2026-05-27; until then the policy is canonical. No `expand-topic` or `research-voids` will fire for voids until either the cap raises or a coalesce frees a slot.

**Concepts −1 net**: The 2026-05-05 08:21 UTC abandoned coalesce (which became the cap-saturation worked example) plus prior coalesce activity left concepts at 230. Topics stable at 231.

**Quality metrics (frozen, 37th period)**:
- Critical: 0 ✓ (target)
- Medium: 10 (target ≤3) — almost certainly stale counter
- Low: 3
- Orphans: 13

## Changes Applied (Tier 1)

*No changes applied via this skill's Tier 1 mechanism.*

**Rationale**: Same three structural blockers as the last 33 reports:
1. No `cadences` / `overdue_thresholds` / `replenishment_config` sections in evolution-state.yaml — nothing to tune via standard mechanism.
2. No `tune_system_history` — cooldowns unenforceable.
3. No `locked_settings` — cannot check for human overrides.

**34th consecutive report** unable to apply Tier 1 changes via the skill's intended YAML mechanism.

**Targeted-intervention precedent (carried forward)**: The 2026-04-29b targeted tune-system established that targeted code-level Tier-1-equivalent changes are tractable when warranted by clear evidence. This period the cycle.py change from that intervention has been **independently validated for a third consecutive period** (33% coalesce abandon now, down from 55% and 62%). No new targeted intervention is warranted this period — the operating system is healthy and continuing improvements are flowing through the regular cycle.

## Recommendations (Tier 2)

### 1. Impose P3 Ceiling in `replenish-queue` (ESCALATED — was Carried Forward ×4)

- **Proposed change**: Add a P3 ceiling check (e.g., 500) to `tools/curate/replenish.py` (or wherever P3 generation happens). When P3 ≥ 500, halt optimistic-review and gap-analysis P3 generation; allow only chain-replenishment additions.
- **Rationale**: P3 at 527 (was 502 last period; +25 in 5 days). The ceiling crossed last period remains breached, though growth has slowed to ~5/day. The decision flagged for **5 consecutive periods** has not been acted on. A ceiling preserves the suggestion-buffer function (chain replenishment still works) while preventing unbounded growth.
- **Risk**: Low. Optimistic-review P3 generation is largely-redundant with already-queued items (the slowing growth rate confirms saturation).
- **Priority**: **High** (5 consecutive escalations).

### 2. Fix `last_runs` Writeback for Cycle-Trigger Tasks (Carried Forward ×6)

- **Proposed change**: Audit the dispatch code in `tools/evolution/` that persists `last_runs` after task completion. check-tenets shows ~104h writeback gap this period (last writeback 2026-05-01 07:40 UTC; actual last run 2026-05-05 15:36 UTC).
- **Rationale**: Pattern now confirmed across **six consecutive reports** — systematic. The check-tenets gap is more dramatic this period because the cycle interval is longer; the gap scales with loop interval rather than being a fixed-time issue, suggesting the timestamp updates fire on cycle-tick boundaries rather than task completion.
- **Risk**: Low (read the code; single-point fix in `tools/evolution/cycle.py` dispatch).
- **Priority**: Medium-High.

### 3. Fix Stale `content_stats` / `progress` Counters (Carried Forward ×32)

- **Proposed change**: Add per-section file-counting at session start in `tools/evolution/state.py`.
- **Rationale**: 37th consecutive report. Recorded state shows 35 topics (actual 231), 145 concepts (actual 230), 11 voids (actual 100), 542 reviews (actual 3825).
- **Risk**: Low.
- **Priority**: Medium.

### 4. Add `tune_system_history` / `locked_settings` / `cadences` Sections (Carried Forward ×34)

- **Proposed change**: Populate evolution-state.yaml with the sections the skill spec expects.
- **Rationale**: Without these, tune-system cannot make Tier 1 changes safely. 34 reports now effectively advisory-only (with the 2026-04-29b targeted exception demonstrating the alternative path).
- **Risk**: Low.
- **Priority**: High.

### 5. Add `validate-all` to Cycle Triggers (Carried Forward ×29)

- **Proposed change**: Add `"validate-all": 2` or similar to `CYCLE_TRIGGERS` in `tools/evolution/cycle.py:43-49`.
- **Rationale**: 102 days stale. Listed in CLAUDE.md as "Daily health check" but not wired into automation.
- **Risk**: Low (read-only check).
- **Priority**: Medium.

### 6. Reconcile tune-system Cadence (Carried Forward ×7)

- **Proposed change**: Either (a) adjust `tune-system` in `CYCLE_TRIGGERS` to better-approximate 30-day cadence at current loop speed, or (b) revise the skill spec to match observed cadence (~5-day at current pace, varying with loop interval).
- **Rationale**: Spec documents 30-day cadence; cycle-trigger fires every 144 sessions which produces variable wall-clock cadence. Last seven reports have observed cadences ranging 36h → 122h. The spec-vs-operation gap is not closing.
- **Risk**: Low.
- **Priority**: Medium.

### 7. Implement Deep-Review Convergence Tracking (Carried Forward ×23)

- **Proposed change**: Track per-article review count and last word-change delta; skip further deep-review for articles with 3+ reviews all showing near-zero net change.
- **Rationale**: At least 4-6/70 deep-reviews this period made no substantive content change (incubation-effect 5th review +2 words; timing-gap 5th review no change; non-temporal-consciousness 4th review -2 words; epistemic-advantages-of-dualism 6th review +19 words). The pattern is increasingly load-bearing.
- **Risk**: Low.
- **Priority**: High.

### 8. Audit Apex Cap Governance — 22/20 (Carried Forward ×6)

- **Proposed change**: Resolve the apex count discrepancy. Cap is documented in text but not enforced in code.
- **Rationale**: Inconsistent governance; new apex creations may ignore the cap. P3 task already queued.
- **Risk**: Low.
- **Priority**: Medium-High.

### 9. Update `convergence_targets` (Carried Forward ×36)

- **Proposed change**: `min_topics` 10→200, `min_concepts` 15→200, `min_arguments` 5→10, add `min_voids` 80, add `min_apex` 15, `max_medium_issues` 3 → 15.
- **Rationale**: Cosmetic; targets set for early-stage system; all vastly exceeded.
- **Risk**: Low.
- **Priority**: Low.

### 10. Document Refinement-Log Marker Discipline (Carried Forward ×4, DE-ESCALATED)

- **Proposed change**: Document the marker-handling discipline in CLAUDE.md or refine-draft SKILL.md.
- **Rationale**: Convention has been stable for two periods (deep-review removes; condense preserves). De facto rule operating cleanly without docs. Optional codification.
- **Risk**: Low.
- **Priority**: Low.

### 11. Track Apex Re-Synthesis Regressions Per-Apex (Carried Forward ×3)

- **Proposed change**: Surface diffs against the latest deep-review-installed corrections during apex-evolve runs.
- **Rationale**: One apex-evolve this period (2026-05-01 20:52 UTC, [apex/machine-question.md](/apex/machine-question/)). Pattern (preserve-class vs regenerate-class) holding.
- **Risk**: Medium.
- **Priority**: Medium.

### 12. Coalesce Slot Reduction — VALIDATED (was track-only) (NEW classification)

- **Proposed change**: No further code change. The 2026-04-29b cycle.py slot reduction (2/24 → 1/24) is now validated for **3 consecutive periods** (62% → 55% → 33% abandon rate). Document the validation in [concepts/coalesce-condense-apex-stability.md](/concepts/coalesce-condense-apex-stability/) (which already references the 2026-05-03 abandonment as worked example) or in a separate methodology note if a fourth-period confirmation also holds.
- **Rationale**: The fix is durable. The original 2026-04-29b decoupling rule said "if abandon rate stays below 50%, the cycle.py change is validated. If it climbs back above 60%, consider raising the slot back to 2/24." Three consecutive periods well below 50% satisfies the validation criterion.
- **Risk**: None.
- **Priority**: Low (passive — let the validation accumulate further before formalising in code comments).

### 13. Outer-Review Pipeline Operational Tracking (NEW this period)

- **Proposed change**: Track outer-review success rate across the next 4-8 weeks (commission/collect/process per-service). 3/3 success this first week. If 100% success holds at scale, document the time-triggered cadence (2/3/4am UTC) as stable infrastructure. If failures emerge (Chrome session expiry, MCP filter issues, model selector regressions), flag specific failure modes for hardening.
- **Rationale**: Pipeline is new and has 3 successful runs to its name. The convergent-meta-finding pattern across two ChatGPT reviews (2026-05-03 evidential-status, 2026-05-04 direct-refutation) is the strongest validation of the pipeline's value: outer reviews are now driving net-new methodological project docs, not just confirming prior work.
- **Risk**: None (observation only).
- **Priority**: Low (passive monitoring).

## Items for Human Review (Tier 3)

### 1. P3 Crossed 500 Threshold — 5th Consecutive Escalation

- **Issue observed**: P3 at 527, up from 502 last period. Ceiling crossed for second consecutive period, but growth has slowed to ~5/day from prior ~14-17/day.
- **Why human needed**: Decide whether P3 is functioning as a suggestion buffer (current behaviour) or a true work queue. Decision is highly ripe.
- **Suggested action**: Add a P3 ceiling to `replenish-queue` (e.g., halt optimistic-review P3 generation if P3 > 500), or accept P3 as archival and document that in CLAUDE.md, or bulk-prune low-value P3 entries.

### 2. Stale State Tracking — 37th Consecutive Report

- **Issue observed**: `content_stats.total_files` and `progress.*` counters frozen at early-project values.
- **Why human needed**: Code change to `tools/evolution/state.py`.
- **Suggested action**: Add per-section file-counting at session start.

### 3. `last_runs` Writeback Gap for Cycle-Trigger Tasks (Carried Forward ×6)

- **Issue observed**: check-tenets shows ~104h writeback gap this period (writeback timestamp 2026-05-01 07:40 UTC; actual last run 2026-05-05 15:36 UTC). Pattern persistent across six consecutive reports.
- **Why human needed**: Code inspection of `tools/evolution/cycle.py` and related task dispatch paths.
- **Suggested action**: Find the dispatch branch for cycle-trigger tasks and ensure it calls `state.update_last_run(task_name, now)` after task completion (not at cycle tick).

### 4. Medium Issues Persistent at 10 (Carried Forward ×28)

- **Issue observed**: Medium issues count exactly 10 for 28 consecutive tune periods.
- **Why human needed**: Decide whether this is a stale counter or live tracking.
- **Suggested action**: Inspect the source of `quality.medium_issues` and confirm it is recomputed at session start.

### 5. Orphaned Files Persistent at 13 (Carried Forward ×15)

- **Issue observed**: Same 13-orphan count through extensive cross-linking work.
- **Why human needed**: Almost certainly stale detection.
- **Suggested action**: Re-run orphan detection against live file state and verify.

### 6. Apex Cap Inconsistency — 22 Active vs 20 Governance (Carried Forward ×6)

- **Issue observed**: 22 active apex articles vs 20 governance cap. Stable since `post-decoherence-selection-programme` was added (2026-04-30).
- **Why human needed**: Editorial/governance decision, plus optional code change to enforce cap.
- **Suggested action**: Reconcile the approved list against the filesystem; archive overflow, raise the cap, or add cap enforcement to apex-evolve.

### 7. tune-system Cycle-vs-Cadence Mismatch (Carried Forward ×7)

- **Issue observed**: Skill documents 30-day cadence; cycle trigger produces variable wall-clock cadence (36h → 122h observed across 7 periods).
- **Why human needed**: Pick a cadence. Either change `tune-system` in `CYCLE_TRIGGERS`, or update the skill spec to match observed cadence.
- **Suggested action**: Most natural fix is to revise the skill spec to acknowledge cycle-trigger-driven cadence (interval-dependent, not wall-clock-fixed).

### 8. Apex Re-Synthesis Content-Loss Vector — Per-Apex Pattern Continues (Carried Forward ×3)

- **Issue observed**: Per-apex regeneration vs preservation pattern continues to hold; no new regression cases observed this period.
- **Why human needed**: Decide whether to instrument apex-evolve with diff-against-prior-deep-review checks.
- **Suggested action**: Profile apex-evolve runs by which apex they target; classify each apex as "preserves deltas" or "regenerates from sources."

### 9. Voids 100/100 Cap Reached (NEW — at-cap milestone)

- **Issue observed**: Voids hit 100/100 today via the expected mechanism (research-voids cycle creating recurrence-void slot). The 2026-04-29b decoupling rule's prediction has played out exactly: catalogue self-regulated to cap without coalesce relief; cap-saturation policy is now formalised in [concepts/coalesce-condense-apex-stability.md](/concepts/coalesce-condense-apex-stability/).
- **Why human needed**: Acknowledge the milestone; decide whether to revisit cap raise before the 2026-05-27 decoupling-rule expiry. The audit-with-reasoning architecture endorses the held-cap policy; no human action required unless a genuinely-novel-territory voids candidate emerges.
- **Suggested action**: None. The system is operating as designed. Re-evaluate cap policy at 2026-05-27 expiry.

### 10. Outer-Review Pipeline End-to-End Live (NEW — infrastructure milestone)

- **Issue observed**: 3 successful end-to-end automated outer reviews on 2026-05-04 (2 ChatGPT, 1 Claude). First successful runs of the commission/collect/process pipeline. The convergent-meta-finding pattern (two ChatGPT reviews on different topics surfacing the same higher-order critique) drove two new methodological-discipline project docs this period.
- **Why human needed**: Acknowledge the milestone; decide whether to expand the pipeline (Gemini collection has been commissioned but not yet collected; weekly cadence vs daily; broader topic rotation).
- **Suggested action**: Let the pipeline run for 2-4 more weeks at current cadence before structural changes; document the convergent-meta-finding pattern as a project-doc when it occurs a third time.

### 11. Methodological-Discipline Ratchet Coherent (NEW — pattern observation)

- **Issue observed**: Outer review → diagnostic finding → project doc → SKILL-file tune → content propagation through cluster ran as a complete cycle twice in 36h this period (evidential-status; direct-refutation). The 2026-05-05 03:18 UTC optimistic-review explicitly endorsed the architecture as "the cleanest implementation of a methodological discipline the catalogue has produced."
- **Why human needed**: Decide whether the pattern warrants a project-doc treatment of its own (a methodology-of-methodologies document), or whether the existing project docs are sufficient.
- **Suggested action**: Track whether the pattern repeats a third time. If it does, consider a meta-document; otherwise the existing project docs are sufficient.

## System Health Summary

| Component | Status | Notes |
|-----------|--------|-------|
| Task execution | **Excellent** | 0% hard-failure rate (20th consecutive period) |
| Skip rate | Excellent | 3 coalesce abandonments by design (33%); 0 hard-fails |
| Content quality | Excellent | 0 critical issues; 0/0 tenet errors/warnings (14 consecutive clean tenet checks) |
| Queue management | **Watch** | P2 stable at 2; **P3 over ceiling at 527** (5th consecutive period) |
| Expand-topic efficiency | Excellent | 10/10 success this period |
| Coalesce efficiency | **Validated improvement** | Post-fix abandon rate 33% (was 55% / 62% prior); 3 consecutive periods of decline |
| Review system | Excellent | ~17 reviews/day; methodological-discipline ratchet operating coherently |
| Deep-review convergence | Mixed | 4-6/70 zero-change reviews (and growing) |
| Scheduling | Operational | Cycle mechanism stable; cadence varies with loop interval |
| Changelog rotation | Working | W18 archived May 4; current changelog at 35 entries |
| State tracking | **Broken** | content_stats/progress stale (37th); `last_runs` writeback gap (6th period) |
| Topics cap | Healthy | 231/250 — 19 slots |
| Concepts cap | Healthy | 230/250 — 20 slots |
| Voids cap | **AT CAP (steady)** | **100/100** — cap-saturation policy now formalised in concepts/coalesce-condense-apex-stability.md |
| Apex cap | Inconsistent (steady) | 22 active vs 20 approved (6th period) |
| Site validation | **Gap** | validate-all not running (102 days; 29th report) |
| Tenet alignment | **Excellent** | 14 consecutive clean delta sweeps |
| Outer-review pipeline | **Live (NEW)** | 3/3 successful end-to-end runs; 2 convergent meta-findings drove new methodology docs |
| Methodological-discipline ratchet | **Operating coherently (NEW)** | Outer review → project doc → SKILL tune → cluster propagation, twice in 36h |
| Coalesce slot fix (cycle.py) | **Validated** | 3 consecutive periods of declining abandon rate |
| tune-system infrastructure | **Blocked** | 34th report unable to apply Tier 1 via YAML |

## Next Tuning Session

- **Expected (at current cycle-trigger rate)**: ~2026-05-10 (5 days out)
- **Recommended per skill spec**: 2026-06-04 (30 days out)
- **Focus areas next run**:
  - Whether P3 ceiling decision is acted on (now 527, 6th period over)
  - Whether coalesce abandon rate stays below 40% (validating the cycle.py fix permanently)
  - Whether outer-review pipeline maintains 100% success rate (commission/collect/process cycles per service)
  - Whether the methodological-discipline ratchet pattern repeats a third time
  - Whether voids hold at 100/100 or whether a coalesce candidate emerges before the 2026-05-27 decoupling-rule expiry
  - Whether apex-tier pessimistic→refine becomes regular practice
  - Whether `last_runs` writeback gap has been addressed (6th consecutive period)
  - Whether `tune_system_history` / `locked_settings` / `cadences` sections appear (35th report)
  - Whether validate-all is integrated (30th report)
  - Whether stale state tracking gets addressed (38th report)
  - Whether P2 depth recovery operates (currently 2 — at the threshold)