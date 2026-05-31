---
title: "System Tuning Report - 2026-05-31"
created: 2026-05-31
modified: 2026-05-31
human_modified: null
ai_modified: 2026-05-31T11:30:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[todo]]"
  - "[[changelog]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-05-31
last_curated: null
---

# System Tuning Report

**Date**: 2026-05-31
**Sessions analyzed**: ~cycle 311→324 (long babysat `/loop 5m /unfin-cycle` run, 2026-05-29 → 2026-05-31)
**Period covered**: 2026-05-29 → 2026-05-31

## Executive Summary

System health is **excellent**: zero task failures across the run, zero critical issues, a converged corpus, and a stable, self-governing queue. The dominant operational finding is not a malfunction but an **opportunity**: a standing "web-verify every load-bearing citation" steer on deep-reviews surfaced ~42 citation defects (fabricated titles/co-authors/quotes/statistics, prominent-name-magnet misattributions, wrong-paper-same-author) that intra-corpus review had propagated for months — a defect class **independently confirmed by all three external outer reviewers**. The highest-leverage system improvements are therefore (1) making citation web-verification a scheduled cadence and (2) repointing inbound references at coalesce/archive time. Both are Tier 3 (code/skill) and are logged for human decision; no Tier 1 automatic changes were warranted this session.

## Metrics Overview

| Metric | Current | Notes |
|--------|---------|-------|
| Session count | 8773 | cycle_position 7776; cycle 324 just completed |
| Recent task failures | 0 / 20 | `failed_tasks: {}` — clean run |
| Critical issues | 0 | at convergence target (max 0) |
| Medium issues | 10 | above the soft target of 3 — see note |
| Topics / Concepts / Voids | 246 / 245 / 101 | voids 1 over its 100 cap |
| Apex articles | 29–30 | over the informal ~20 audit target |
| Reviews completed | 542 | heavy review cadence |
| Orphaned files | 0 | clean |
| Queue (P0–P2) | floor-bouncing 2↔5 | documented steady state, healthy |

## Findings

### Cadence Analysis
The state file no longer carries a `cadences:` / `overdue_thresholds:` block — scheduling migrated to the deterministic 24-slot cycle (`tools/evolution/cycle.py`) plus wall-clock time-triggers. So the classic cadence-tweak knobs this skill targets do not exist to adjust. Cadence health is instead governed by the cycle ratios, which are operating as designed (deep-review 17%, queue 67%, etc.). **No cadence change available or warranted.** One emergent pattern worth a code-level damping term: see Convergence Progress below.

### Failure Pattern Analysis
**Zero failures** in the recent-task window (`failed_tasks: {}`; 20/20 success). The only non-content "failure-shaped" events were *intentional, well-handled* no-ops: agentic-social verification math-challenges (auto-solved or manually recovered), research-voids halting at the section cap, coalesce declining on the age-floor, and same-day-duplicate deep-reviews closed without re-running. None indicate a defect. **No action.**

### Queue Health Analysis
The queue oscillates between 2 and 5 actionable (P0–P2) tasks — the documented "replenish-at-floor alternation," which is expected, not a bug. Replenishment is honest (promotes grounded staleness/length work rather than minting speculative tasks against near-cap sections + a ~460-task P3 backlog). Three latent code issues observed (Tier 3, below): blocked-offender re-queue, LIFO-within-priority starvation, and replenish/cycle-slot staleness collision. All currently mitigated by driver-side `#veto`s and same-day dedup.

### Review Finding Patterns
The recurring, high-yield review finding is **citation-metadata unreliability** — see Executive Summary. The second recurring theme is **archival-link-rot**: coalesce/archive operations strand inbound references (wikilinks, `apex_sources`, task targets) that then survive for weeks. Both are Tier 3 durable fixes. A third, milder theme: condense correctly *declines* on wall-to-wall-argument flagships (recommending human splits) — this is the discipline working, not a defect.

### Convergence Progress
The corpus is **at convergence** (0 critical issues, all section minimums far exceeded). Consequence: staleness-scored selection keeps re-reviewing long-converged articles (7th–10th passes), ~8 of which this run explicitly recommended a longer interval. These are mostly metadata-only — BUT not pure waste: converged Nth reviews still caught real fabrications (e.g. Saad→Vaassen on a 7th-review article). The reconciliation is a convergence-damping term that lengthens *light* re-review cadence while preserving periodic web-verify passes.

## Changes Applied (Tier 1)

*No changes applied.* The state file exposes no adjustable `cadences`/`weights` knobs (deterministic cycle scheduling), and no setting met the evidence + cooldown + magnitude criteria. Consistent with the skill's "when in doubt, recommend rather than apply."

## Recommendations (Tier 2)

### R1 — Medium-issue count (10) above soft target (3)
- **Proposed**: track whether the 10 `quality.medium_issues` are genuine open items or stale counters; most "medium" findings this run were resolved same-session (citation fixes, calibration recasts).
- **Rationale**: the counter may be lagging actual resolution.
- **Risk**: Low. **To approve**: audit `quality.medium_issues` provenance; reset if stale.

## Items for Human Review (Tier 3 — code / skill / editorial; never automatic)

### T3-1 — Scheduled citation web-verify cadence  *(highest confidence)*
~42 citation defects caught this run via a manual web-verify steer; triple-confirmed by external reviewers. **Suggested**: add a scheduled cadence that web-verifies (metadata + source-conclusion + full author vector) the load-bearing citations of citation-heavy articles, biased toward (a) recent/specialist-cite articles and (b) articles not web-verified recently; and a **write-time citation gate at research-note creation** (research roots are the propagation source). Reconciles with convergence-damping: "lengthen light re-reviews, but every Nth pass is a web-verify pass."

### T3-2 — Repoint inbound references at coalesce/archive time  *(highest leverage)*
One coalesce stranded ~35 inbound wikilinks that survived **6 weeks**; same root cause hits `apex_sources` (6 fixed this run) and task targets. **Suggested**: have `/coalesce` and `/archive` do a vault-wide repoint at move time of inbound `[[old-slug]]`/`[[old-slug|alias]]` wikilinks, `apex_sources:` entries, and open todo `File:` targets → the `superseded_by` replacement.

### T3-3 — Replenish/queue code fixes
(a) `length_analysis` should EXCLUDE any article with an open `#veto` or a condense within ~7 days (it re-queued the apex flagship and a same-day-condensed article this run). (b) Wire `select_queue_task` to the existing `scoring.py` urgency/age term to fix LIFO-within-priority oldest-task starvation. (c) De-duplicate replenish staleness-promotions against the cycle-slot deep-review (same scorer collides on one article same-day).

### T3-4 — Convergence-damping on staleness selection
Add a damping term that lengthens the staleness threshold each time an article converges with no content change — but retain periodic web-verify passes (see T3-1).

### T3-5 — Stale skill-doc reference
`refine-draft/SKILL.md:44` calls `uv run python scripts/curate.py review`; `scripts/curate.py` does not exist (verified). Non-breaking (forks work around it). Repoint to the right entry point or drop the step.

### T3-6 — Editorial split decisions (3 length-blocked flagships)
All `#veto`'d so they don't churn; each needs a human split decision:
- `apex/phenomenal-output-causal-machinery-dissociation.md` (6989w) → extract "The Strongest Materialist Reading" + "Independent Traditions on the Same Architecture" into a companion apex.
- `topics/epistemology-of-convergence-arguments.md` (6479w) → extract "Compound Signatures" (→ concept page) + "The Anti-Realist Challenge" (→ debunking-arguments article).
- `topics/born-rule-and-the-consciousness-interface.md` (5053w) → condense-churn-vetoed; structural review.

### T3-7 — Capacity items
Voids at 101/100 (over by 1; resolvable via the age-floor-deferred `source-attribution-void`/`confabulation-void` coalesce ~2026-06-03). Apex at ~30 vs informal ~20 — over-cap audit P3 open. Minor index drift: `perceptual-reality-monitoring-void.md` exists standalone but is still listed under "Research-Stage Voids" in the voids index.

### T3-8 — Calibration discipline: time-varying quantities
A true-but-growing figure (NY Declaration signatory count) was repeatedly "corrected" *downward* by reviews against stale snapshots; live verify showed 599 (current). **Discipline**: for any time-varying quantity, web-verify the *current* live value; a high number is not prima facie an inflation; prefer dated/sourced forms ("N as of <date>").

## Next Tuning Session

- **Recommended**: ~2026-06-06 (or next 6-cycle trigger).
- **Focus areas**: whether T3-1/T3-2 were implemented; medium-issue counter accuracy; whether the deferred ~2026-06-03 coalesce brought voids back to 100.
