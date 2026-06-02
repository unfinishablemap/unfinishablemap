---
ai_contribution: 100
ai_generated_date: 2026-06-02
ai_modified: 2026-06-02 05:30:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-02
date: &id001 2026-06-02
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[todo]]'
- '[[changelog]]'
title: System Tuning Report - 2026-06-02
topics: []
---

# System Tuning Report

**Date**: 2026-06-02
**Sessions analyzed**: 1 long `/loop` session (cycle_position ~8010→8064, ~90 loop iterations across 2026-06-01/02)
**Period covered**: 2026-06-01 — 2026-06-02
**Note**: Prior tune-system ran 2026-06-01T07:31 (~22h ago, via the 6-cycle trigger). Per the monthly-cadence intent this is a **focused operational pass**, not a full re-analysis of the five categories already covered yesterday. No tunable cadence/threshold/weight settings exist in `evolution-state.yaml` (cadences live in `tools/evolution/cycle.py`), so **0 Tier-1 changes** are possible from state alone.

## Executive Summary

System health is **strong**: 0 critical issues, 20/20 recent tasks succeeded, 0 failures, content-review backlog (changed-since-review) worked through, the 3-service outer-review triple completed end-to-end with strong cross-reviewer convergence, structural fronts (coalesce/links) converged. The session's signal finding is operational, not content: **~18 distinct citation defects were caught by live web-verify, many surviving 5–24 prior "citations verified" reviews** — strong evidence that intra-corpus cross-check ≠ accuracy and that a scheduled web-verify cadence is the single highest-value automation improvement. Five code/methodology fixes are also recommended.

## Metrics Overview

| Metric | Current | Notes |
|--------|---------|-------|
| critical_issues | 0 | abort condition clear |
| Recent-task failure rate | 0% (0/20) | healthy |
| Outer-review triple | 3/3 collected+processed+synthesized | strong convergence on tenet-smuggling |
| Citation defects caught (web-verify) | ~18 | the session's dominant finding |
| Content sections | topics 260/270, concepts 250/270, voids 101/100 | voids at/over cap |

## Changes Applied (Tier 1)

*No changes applied.* No cadence/threshold/weight settings exist in `evolution-state.yaml` to tune (they live in `cycle.py`); prior tune-system was <24h ago (cooldown); and all six findings below are code/methodology (Tier 2/3), not Tier-1 parameter tweaks.

## Recommendations (Tier 2)

### R1 — Schedule a web-verify-MANDATED deep-review cadence on citation-heavy articles (HIGHEST VALUE)
- **Proposed change**: Bake a "web-verify each load-bearing citation against publisher of record" requirement into the cycle-slot/queue deep-review candidate scorer (`tools/curate/deep_review.get_review_candidates`), prioritising articles with recent/post-2020/specialist citations (the fabrication zone). Or add a dedicated periodic web-verify pass.
- **Rationale**: ~18 distinct citation-metadata/source-conclusion defects this session — fabricated co-authors (Bharioke; Denton "Greaves, Hiscock"), fabricated titles (Hoel "Proximity Argument"; Strawson "Silliest Claim"; Travis 2024), wrong-author/same-group (penrose Großardt/Fein; Bhatt→Rouleau&Cimino; Stoll→Zheng&Meister stance-reversal), uniform 6-file venue errors (Lennon→Erkenntnis), page-range/orphan defects (free-will Read+Sjöberg at the **24th** review), precision errors (room-temp→UV superradiance). Many survived 5–24 prior "verified" reviews because intra-corpus cross-check ratifies the error. **Externally corroborated**: 2 of 3 outer reviewers independently caught the same MPE-92M misattribution this cycle.
- **Risk**: Low. Web-verify returns clean on sound articles (no false positives observed); cost is fork web calls.
- **To approve**: human edits the scorer/skill to carry the web-verify mandate, or schedules a periodic web-verify pass.

### R2 — Refine the changed-since-review filter to the four-bucket model
- **Proposed change**: Classify staleness candidates from the DIFF (not the commit message): (a) mechanical-sweep = false signal → deprioritize; (b) own-content development → high value; (c) calibration-import / hub cross-link → lower value (review only if citation-heavy); (d) same-session-already-vetted → light-verify or skip.
- **Rationale**: The naive `ai_modified > last_deep_review` filter returned 174 candidates; only ~10-15 were genuine own-development. This session validated all four buckets end-to-end (own-development reviews were sound; mechanical-sweeps were false signals; same-session-vetted got light-verified without churn).
- **Risk**: Low. **To approve**: bake the diff-based classifier into replenish/scorer logic.

## Items for Human Review (Tier 3 — code)

### H1 — Scorer counts frontmatter ISO tokens in word/cite counts
- **Issue**: The candidate scorer over-counts both word-count and "N post-2020 cites" by including frontmatter ISO date tokens. Confirmed 5×: illusionism reported 3597w/over-hard (actual 3499/under-hard); subject-object & intentionality reported 5/7 post-2020 cites (actual 0).
- **Why human**: code change in the scorer. **Suggested**: strip frontmatter before counting words/cites. Impact: false over-hard length flags (→ unwarranted condense/human-defer) and false fabrication-zone steers.

### H2 — `cycle_post` sentinel substring trap
- **Issue**: `tools/evolution/cycle_post` substring-scans the `--note` for `LOGIN_REQUIRED`/`CHROME_UNAVAILABLE`/etc. without negation/word-boundary awareness. A SUCCESS note saying "no LOGIN_REQUIRED" set a false 24h commission backoff this session (remediated by hand).
- **Why human**: code change. **Suggested**: match only a standalone/leading sentinel token, not any substring. (Workaround in place: never write the literal token in a note unless it genuinely fired.)

### H3 — Human-decision length tasks queued into Active (mis-picked)
- **Issue**: `deep-review` queues "human length decision" (over-ceiling-from-OWN-calibration) tasks as `Type: refine-draft` into `## Active Tasks`, where the loop mis-picks them and would auto-condense the very article they protect (caught once this session; the task was diverted to Blocked by hand).
- **Why human**: code change in deep-review's task-emit. **Suggested**: emit these into `## Blocked Tasks (Needs Human)`, not Active.

### H4 — `progress.{topics,concepts}_written` state fields stale
- **Issue**: 246/245 in state vs ~260/250 on disk. Cap-enforcement reading the field sees false headroom. **Suggested**: recompute from disk, or have cap checks count on disk (already the operative workaround).

## Next Tuning Session

- **Recommended**: 2026-07-02 (30 days), OR sooner if a human acts on R1 (the web-verify cadence) and wants to measure its catch-rate.
- **Focus areas**: (1) whether R1 was implemented and its defect-catch rate; (2) the outer-review convergence pattern (does tenet-smuggling/boundary-substitution keep recurring across subjects?); (3) the recent-physics/specialist-citation fabrication zone.