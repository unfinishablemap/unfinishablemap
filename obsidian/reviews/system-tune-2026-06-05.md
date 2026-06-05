---
title: "System Tuning Report - 2026-06-05"
created: 2026-06-05
modified: 2026-06-05
human_modified: null
ai_modified: 2026-06-05T10:15:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[todo]]"
  - "[[changelog]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-05
last_curated: null
---

# System Tuning Report

**Date**: 2026-06-05
**Trigger**: cycle-360 close (every-6-cycles cadence)
**Prior run**: 2026-06-04T12:30 (< 24h ago)

## Executive Summary

System health is good: `critical_issues: 0`, `failed_tasks: {}`, recent tasks succeeding, orphaned_files: 0. This run was triggered by the 6-cycle cadence but fires **less than 24 hours after the prior tune-system run** — far inside the 30-day monthly cadence the skill mandates. Per the skill's "DO NOT run more frequently than monthly" rule and the 5-sessions-minimum evidence thresholds (unmeetable in <1 day of new data), **no Tier-1 changes are applied**. The value of this run is the Tier-2/Tier-3 recommendations below, which are backed by strong evidence accumulated over ~130 loop iterations this session.

## Changes Applied (Tier 1)

*No changes applied.* Rationale: (a) prior run <24h ago — insufficient new data to meet evidence thresholds (5+ sessions for cadence/queue/convergence); (b) no `cadences`/`tune_system_history` block is present in `evolution-state.yaml`, and per the documented cycle_post-strips-unmodeled-top-level-blocks behavior, any such block written here would be silently dropped next cycle — so Tier-1 cadence edits cannot reliably persist until that is addressed (see Tier-3 #1).

## Recommendations (Tier 2)

### Convergence-damping for the staleness/changed-since-review selector
- **Proposed change**: the deep-review candidate selector should diff BODY content, not key off `ai_modified` mtime.
- **Rationale (strong, this session)**: a large share of changed-since-review re-triggers are **metadata-vs-content artifacts** — corpus-wide citation-hygiene sweeps and cross-link installs bump `ai_modified` across many files without changing the argument, so they re-enter the changed-since-review pool and produce no-op verifications (observed repeatedly: process-and-consciousness 5th pass, biological-cognitive-closure 3rd, mine-ness 4th, disconnection-neuroscience, etc.). The fork-reported pool is ~178–192 candidates, much of it cosmetic-churn re-picks. NOT pure waste (the no-ops confirm sweep fixes landed), but a body-diff gate would focus the pool on genuine unreviewed content.
- **Risk**: Low. **To approve**: code change in `tools/evolution` candidate selection.

### Citation-verification scope: verify ALL authors, not just load-bearing cites
- **Rationale (strong)**: this session caught ~24 citation/empirical defects; several wrong-author defects (Calderone mis-cited as Rodríguez-Martín; the attention-schema "2025 MIT study" misattribution) survived 2–5 prior reviews because those passes web-verified only the directionality/argument-load-bearing citations, not background/history references. Reviews that spot-check only load-bearing cites systematically miss wrong-author defects in supporting refs.
- **Risk**: Low (more thorough verification). **To approve**: steer deep-review/refine forks to web-verify every citation's author surname.

## Items for Human Review (Tier 3)

### 1. cycle_post strips unmodeled top-level YAML blocks (blocks tune-system Tier-1 persistence)
- **Issue**: `evolution-state.yaml` has no `cadences`/`locked_settings`/`tune_system_history` blocks visible, and cycle_post re-serializes through a fixed schema that silently drops unmodeled top-level blocks. This means tune-system's own Tier-1 mechanism (editing cadences/recording history) cannot persist. Forks have repeatedly worked around this (declining to write `queue_status` etc.).
- **Why human needed**: code change to cycle_post's schema (add the tune-system-owned blocks to the modeled set), or relocate tune-system state outside the cycle_post-managed file.

### 2. Anchoring-audit (Audit Three) re-emits structurally-unsatisfiable false-high tasks every cycle
- **Issue**: articles whose anchor concept is an intrinsically ultra-hedge-dense CONCEPT PAGE (qualia 8.22/kw, valence 7.16/kw) get a hedge_density refine task re-emitted EVERY cycle, because the 60%-of-anchor floor (~4.3–4.9/kw) is mathematically unreachable for a calibrated topic/void without over-hedging into mush. Observed re-emitting on `wanting-liking-and-the-value-in-mechanism-fork` at consecutive cycle closes (358, 359) despite a correct light-touch refine + optimistic-review judging it calibration-exemplar. Harmless (each is a quick verify-then-close) but recurring queue churn.
- **Suggested action**: in `tools/curate/anchoring.py`, exclude ultra-dense concept-page anchors from the hedge-density check, cap the target, or skip re-emission when the article's strong-assertions are already at the floor.

### 3. Over-ceiling flagship cohort needs human length-decisions
- **Issue**: a growing set of high-quality articles sit over their hard length caps with load-bearing, calibration-protected content that auto-condense cannot safely reduce: `argument-from-reason` (4489w), `agency-void` (3171w), `edge-states-and-void-probes` (3634w, grew from the outer-review triple), `epistemic-advantages-of-dualism`, plus the standing flagship splits (`epistemology-of-convergence-arguments` 6479w, `born-rule` 5064w, `phenomenal-output-causal-machinery-dissociation` 6831w #veto). Each was confirmed this session as redundancy-harvested-then-stopped (calibration intact). They need editorial calls: split, accept-over-cap, or restructure.

### 4. Section caps at/over limit
- **Issue**: topics 270/270 (at hard cap), voids 101–102/100 (over). Automation has correctly shifted to improvement-only there; coalesce repeatedly (and correctly) abandons — the corpus is deliberately differentiated, so caps can't be relieved by automated merge. Needs a human decision: raise caps, or designate specific consolidations/archivals.

### 5. Corpus-wide citation-verification sweep (high value)
- **Issue**: ~24 citation/empirical defects caught this session across dangling-cite, orphan-ref, wrong-author, wrong-paper, wrong-institution, wrong-year, and fabricated variants — several cross-propagated through the corpus (Vervaeke wrong-author across 5 files; Coutinho→Rebouillat; Craddock 613 THz sweep in 2+ variants). Intra-corpus cross-checking PROPAGATES these; only live web-verification catches them. A dedicated corpus-wide sweep (grep every inline `Author et al. YYYY`, web-verify author/title/venue/year, check inline↔References both directions) would surface and fix a sizable batch at once rather than waiting for per-article reviews.

## Next Tuning Session

- **Recommended**: 2026-07-04 (30 days out) — or honour the monthly cadence rather than the 6-cycle trigger, which fires far too often at fast `--interval`.
- **Focus areas**: whether the Tier-2 body-diff selector and citation-scope changes were adopted; the over-ceiling cohort's resolution; cap decisions.
