---
ai_contribution: 100
ai_generated_date: 2026-06-03
ai_modified: 2026-06-03 01:36:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-03
date: &id001 2026-06-03
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[todo]]'
- '[[changelog]]'
title: System Tuning Report - 2026-06-03
topics: []
---

# System Tuning Report

**Date**: 2026-06-03
**Sessions analyzed**: current long `/loop` session (2026-06-02 → 2026-06-03), against the prior daily reports (06-02, 06-01, 05-31, 05-27)
**Period covered**: 2026-06-02 05:20 (last tune-system run) → 2026-06-03 01:35

## Executive Summary

System health is excellent: ~100% task success across the session, `quality.critical_issues = 0`, links clean, tenets uniformly aligned, coalesce correctly declining. The session's defining work was **citation integrity** — ~30 distinct citation defects caught via live publisher web-verification, including **three corpus-wide citation-family resolutions**, many surviving 5–12+ prior "citations verified" reviews. **0 Tier-1 changes applied** (the standing recommendations are Tier-2/3 code/process items, not cadence/threshold tweaks; and tune-system is firing ~daily via the cycle-trigger, so oscillating settings would violate the monthly-cadence design).

## Metrics Overview

| Metric | Current | Notes |
|--------|---------|-------|
| Task success rate | ~100% | recent_tasks all `success`; no abort condition |
| critical_issues | 0 | abort-clear |
| medium/low issues | 10 / 3 | stable |
| orphaned_files | 0 | clean |
| Queue depth (P0–P2) | ~3–5 | replenish-at-floor alternation (expected steady state) |
| Sections (on disk) | topics 260/270, concepts 250/270, voids 101/100 | voids +1 over cap |
| voids vs state field | 101 on disk / 101 state | voids current; topics(246)/concepts(245) state fields STALE vs on-disk 260/250 |

## Findings

### Cadence Analysis
- **tune-system is firing ~daily, not monthly.** Reports exist for 06-03, 06-02, 06-01, 05-31, 05-27. The cycle-trigger (`every 6 cycles`) fires it far more frequently than the SKILL.md's monthly design at fast `/loop` speed, producing near-duplicate daily reports. → **Tier 3** (gate tune-system on a 30-day wall-clock like literature-drift, or lower its cycle-trigger frequency).
- Other maintenance tasks (check-links/2, check-tenets/3, embed-videos/1) are firing on schedule; outer-review commission/collect cadences nominal.

### Failure Pattern Analysis
- **No failures.** recent_tasks all `success`; no abort condition. No environmental error cluster.

### Queue Health Analysis
- Replenish-at-floor alternation is the **expected** steady state (floor of 3 cleared repeatedly via genuine large-gap staleness picks). No starvation; LIFO-starvation mitigated by top-insertion. P3 maintenance tasks accumulating but not blocking.

### Review Finding Patterns
- **Dominant recurring pattern: citation-metadata defects in recent/specialist cites**, surviving multiple prior "verified" reviews because intra-corpus consistency *ratifies* them. Caught ONLY by live publisher web-verify. Defect density clusters in quantum-biology / quantum-PK / animal-consciousness / recently-added syntheses; canonical pre-2020 cites verify clean (recency-clustering). See Tier-2 #1.

### Convergence Progress
- Corpus is **converged and deliberately fine-grained**: coalesce correctly declines (2 clean no-ops this session), check-tenets clean (0 misalignments across 646 articles), check-links clean (0 broken inter-article links). Content reviews increasingly land in the converged tail (clean passes / minor metadata), with real catches still surfacing in the recent-cite and quote-attribution slots.

## Changes Applied (Tier 1)

*No changes applied.* Rationale: the actionable findings are Tier-2 (process) / Tier-3 (code/human-review), not Tier-1 cadence/threshold/weight tweaks; and tune-system's ~daily cycle-trigger firing means any setting change would oscillate, violating the cooldown/monthly-cadence design. No 5+-session new evidence for a cadence change since the 06-02 run.

## Recommendations (Tier 2)

### 1. Mandatory publisher web-verify for citation-heavy / recent-cite / specialist deep-reviews (HIGHEST VALUE)
- **Evidence**: this session caught ~30 citation defects via live web-verify, incl. **3 corpus-wide family resolutions** — (a) niaf011 "Babcock/Hameroff" → **Wiest, M.C.** (famous-domain-name substitution, ~8 files; PMID 40342554); (b) Kerskens "Pérez, D.L."/"Pérez López" → **López Pérez, D.** (compound-surname order, 23 files / 31 instances; IOPscience 10.1088/2399-6528/ac94be); (c) Han "Phys Lett A / On the Born rule…" → **Han, Y.D. & Choi, T., Sci Rep 6:22986** (wrong venue+title+missing-coauthor, 4 files; arXiv:1307.2026). Plus fabricated titles (Ehrsson 2007), fabricated/mis-sourced quotes (Schlosshauer=Wikipedia text; Polanyi 1966→1977), and figure-attributed-to-review-not-primary (Olivares 2015 vs Petitmengin 2013). Many survived 5–12+ prior reviews.
- **Proposed change**: bake a publisher-of-record web-verify step into `deep-review` whenever an article carries recent/post-2020/specialist citations (or add a dedicated web-verify review cadence focused on the quantum/specialist defect-dense zone). Driver memory `ai-citation-metadata-unreliable` now documents 28 defect classes + detection vectors.
- **Risk**: Low. **To approve**: edit deep-review SKILL.md to require the web-verify pass for the recent-cite case (Tier-3 since it's a skill-file edit — see below).

### 2. Encode the citation-family-resolution workflow
- **Proposed change**: codify the repeatable pattern — deep-review detects a result cited under inconsistent metadata across the corpus (finding-level cross-article divergence) → web-verify once at publisher → grep the full corpus landscape → propagate canonical form with exclusions + multi-file completeness verification. As a deep-review sub-step or a named skill.
- **Risk**: Low. **To approve**: human decides skill vs sub-step.

## Items for Human Review (Tier 3)

### A. Scorer frontmatter-token over-count (code)
- The candidate scorer counts frontmatter ISO-date tokens in BOTH word-count and "N post-2020 cites" → FALSE over-hard length flags and FALSE citation-heavy steers (confirmed this session: pain-asymbolia mis-flagged "post-2020 citation-heavy" with all-pre-2008 sources; out-of-body scorer mis-read the ai_modified signal). **Fix**: strip frontmatter before the scorer's word/cite counts (canonical `analyze_length` already does; the scorer should match).

### B. Citation-lint for the cheap pre-filters (code)
- A lint pass could cheaply flag, without web access: orphaned body-cite not in ref list; a "title" that is a position-name (doctrine label); a review/survey cited for a primary numeric result; a same-document or same-field famous-name in the author vector; compound-surname order anomalies. These are the pre-filters the session catalogued (28 classes).

### C. Stale progress fields + voids cap (code/operator)
- `progress.{topics,concepts}_written` (246/245) lag the on-disk counts (260/250); voids 101/100 is +1 over cap. Cap enforcement should count on disk, not the state field. Either bump `max_voids` to 101–102 or accept +1 as steady state (research-voids already correctly skips at capacity).

### D. tune-system firing ~daily, not monthly (config)
- Gate tune-system on a 30-day wall-clock (like literature-drift) or lower its cycle-trigger frequency, to stop daily near-duplicate reports and respect its monthly design.

### E. deep-review SKILL.md edit for Tier-2 #1
- Implementing the mandatory-web-verify recommendation requires a skill-file edit (Tier-3 by policy).

## Next Tuning Session

- **Recommended**: 2026-07-03 (30 days out) — or sooner if findings A–D are implemented and need verification.
- **Focus areas**: whether the web-verify recommendation reduces the recent-cite defect rate; scorer-fix verification; voids-cap resolution.