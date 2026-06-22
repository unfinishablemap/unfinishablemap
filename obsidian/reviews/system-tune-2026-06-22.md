---
title: "System Tuning Report - 2026-06-22"
created: 2026-06-22
modified: 2026-06-22
human_modified: null
ai_modified: 2026-06-22T20:11:57+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[todo]]"
  - "[[changelog]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-22
last_curated: null
---

# System Tuning Report

**Date**: 2026-06-22
**Sessions analyzed**: ~1.4 days since last run (5th consecutive over-frequency fire)
**Period covered**: 2026-06-21 → 2026-06-22

## Executive Summary

System health is good: 0 critical issues, 1/20 recent failures (5%, a transient server-side API rate-limit on the check-tenets tenet-scan subagents — not a system fault), convergence stable. **No Tier-1 changes applied** — the cadences/thresholds live in code (`tools/evolution/`), not in `evolution-state.yaml`, so there is no in-file Tier-1 surface, and only ~1.4 days have elapsed since the prior run (far below the 5-session evidence threshold). This is the 5th consecutive over-frequency fire: the every-6-cycles cycle-trigger vastly outpaces the intended 30-day cadence.

## Metrics Overview

| Metric | Current | Notes |
|--------|---------|-------|
| Recent failure rate | 5% (1/20) | transient API rate-limit, not a fault |
| critical_issues | 0 | |
| medium_issues | 10 | stable |
| orphaned_files | 0 | |
| Queue depth (P0-P2) | 3 (floor) | documented replenish-at-floor steady state |

## Findings & Changes Applied (Tier 1)

*No Tier-1 changes applied* — no in-file adjustable surface; insufficient elapsed time/evidence; system within documented healthy steady state.

## Recommendations (Tier 2) — re-logged, standing

### Gate tune-system on its 30-day cadence (5th time recommended)
- **Proposed change**: stop firing tune-system from the every-6-cycles cycle-trigger; gate it on `last_runs["tune-system"]` ≥ 30 days like the other wall-clock-cadenced skills (literature-drift-review pattern).
- **Rationale**: it has now fired 5 times in ~1 week, each a 0-change no-op, because the cycle cadence outpaces the monthly intent. Wasteful; dilutes the evidence window.
- **Risk**: Low. **To approve**: move tune-system off the cycle-trigger table into interval-gated wall-clock dispatch.

## Items for Human Review (Tier 3) — recurring, corroborated this session

This session (the /loop unfin-cycle run, ~70 iterations) produced strong fresh evidence for the standing Tier-3 items. All need operator/code fixes (out of tune-system's automatic scope):

1. **Queue LIFO starvation (minting-placement corollary) — observed TWICE, fixed manually both times.** Replenish top-inserts each fresh floor-restore mint, and `task_selector.select_queue_task` sorts `(priority, line_number)`, so pre-existing same-priority tasks at the bottom never become the lowest-line pickable. (a) The 2 embodied-interface chain-successors starved ~20 cycles; (b) the 2 standing Torres-Alegre deep-reviews (interface-specification-programme, delegatory-causation) starved ~16 replenish runs. Both fixed by P2→P1 promotion (priority beats line). **Durable fix**: make replenish insert floor-restore mints at the BOTTOM of the priority group (so the oldest drains first), OR wire `select_queue_task` to FIFO/age-aware scoring (`tools/evolution/scoring.py` exists but is unused by the selector).

2. **Forked skills that spawn a background subagent/task yield before reporting** (coalesce ×2, cycle/queue deep-review citation-verify, check-tenets, apex-evolve, check-links all did this). The Skill tool returns a "monitor armed / I'll wait" stub; the subagent result + completion arrive to the PARENT, which must reconstruct the outcome from git state and complete the skill's decision logic. Not a fault per se, but the orchestrator must always `git status`-reconstruct after such a yield (clean tree = no-op/decline; dirty tree = verify-or-revert).

3. **apex-evolve can expand a human-deferred over-ceiling flagship further over the hard ceiling** (this session: machine-question 5001→5200w, no compensating trim; reverted). apex synthesis should be length-neutral on already-over-ceiling articles, or skip them pending the human length decision.

4. **Accumulated internal link rot surfaced by the first /check-links run**: 23 distinct broken link targets (418 total instances, inflated by referrer fan-in) = 11 genuinely-dangling (renamed/archived slugs) + 12 wrong-section (converter slug-collision exclusion renders wrong section paths). `sync.py`/`validate.py` exit 0 on these. Needs a corpus-wide repoint pass + a converter slug-collision-resolution fix.

5. **Cosmetic-drift re-review churn**: the cycle-slot deep-review scorer keeps re-picking long-converged articles whose `ai_modified` was bumped only by sibling cross-link adds (3 such no-ops this session: ensemble-level-epiphenomenalism, phenomenal-acquaintance, etc.). Replenish already filters these (git-verifies cosmetic vs own-body); the cycle-slot candidate scorer does not. **Suggested**: add the same cosmetic-cross-touch damping to `tools.curate.deep_review.get_review_candidates`.

## Next Tuning Session

- **Recommended**: 2026-07-22 (30 days out) — and please gate it there rather than letting the cycle-trigger re-fire it in ~1.5 days.
- **Focus areas**: whether the LIFO durable fix landed; check-links link-rot remediation progress.
