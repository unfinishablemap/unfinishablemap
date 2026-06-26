---
ai_contribution: 100
ai_generated_date: 2026-06-26
ai_modified: 2026-06-26 19:50:42+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-26
date: &id001 2026-06-26
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[mqi-empirical-fragility]]'
- '[[changelog]]'
title: Deep Review - MQI Empirical Fragility (2026-06-26)
topics: []
---

# Deep Review: [project/mqi-empirical-fragility.md](/project/mqi-empirical-fragility/)

**Date**: 2026-06-26
**Type**: First-ever deep review (never previously deep-reviewed; created 2026-05-13, opus-4-7 cohort)
**Outcome**: Success — 2 issues fixed, all citations web-verified at publisher of record.

This is a Tenet-2 load-bearing methodology document (the MQI empirical-exposure ledger). The review was orchestrator-salvaged after the deep-review fork came to rest before stamping frontmatter / writing this archive; the fork's two content edits were inspected and confirmed correct, and the citation verification was completed by two parallel verification subagents.

## Issues Fixed

1. **Stale self-count (medium)** — the discipline-sequence sentence said this was the "**sixth** named methodological pattern" but enumerated six prior patterns (closed-loop-opportunity-execution, coalesce-condense-apex-stability, bedrock-clash-vs-absorption, framework-stage-calibration, direct-refutation-discipline, evidential-status-discipline), making this the **seventh**. Corrected sixth → seventh to match its own list. (Stale-internal-count drift — the apex-stale-internal-quote-channel pattern in a project meta-doc.)

2. **Inline↔References orphan (critical class)** — the body cited the 2022 Majorana Demonstrator collapse-search result but the References block had no matching entry. Added as References entry 3 with the correct attribution **Arnquist, I. J. et al. (Majorana Collaboration) (2022), Phys. Rev. Lett. 129, 080401** (NOT "Majorana Demonstrator" as a bare author); References renumbered 1–8 sequentially.

## Citation Web-Verify Ledger (publisher of record)

All five external citations verified **real-correct**:

- **Donadi, S. et al. (2021)** — *Nature Physics* 17, 74–78 (Gran Sasso underground test; falsifies the parameter-free Diósi–Penrose model). ✓
- **Tegmark, M. (2000)** — *Phys. Rev. E* 61, 4194 (neural decoherence times ~10⁻¹³–10⁻²⁰ s). ✓
- **Arnquist et al. (Majorana Collaboration) (2022)** — *Phys. Rev. Lett.* 129, 080401 (PMID 36053678). ✓ Note: the headline constraint is on **CSL**; the Diósi–Penrose improvement is secondary and an **Erratum (PRL 2023)** corrected the DP bound to R_DP > (2.54 ± 0.03) × 10⁻¹⁰ m — use the erratum value if any specific DP figure is later quoted. The article's "strengthened … by roughly an order of magnitude" gloss is fair.
- **Maier, M. A., Dechamps, M. C., & Pflitsch, M. (2018)** — *Frontiers in Psychology* 9, 379, doi:10.3389/fpsyg.2018.00379 (PMID 29619001; preregistered Bayesian evidence against micro-PK, BF01 ≈ 10, ~12,571 subjects). ✓ Do not confuse with the similarly-titled Commentary (doi:10.3389/fpsyg.2018.01350).
- **Zheng, J. & Meister, M. (2025)** — *Neuron* 113(2), 192–204 (PMID 39694032). ✓ The **2025** year is correct for the journal version (print issue 2026-01-22; the 2024 figure is the arXiv:2408.10234 preprint).

## Other Checks

- Length 3076 words (soft_warning, under hard) — no condensation; methodology spec.
- `validate.py` ✓ Valid; no EOF tool-call artifact; all wikilinks resolve.
- No superlative/currency claims beyond the verified collapse-bound figures.

## Stability Note

This is a physics-dependence ledger whose value is currency: re-verify the collapse-bound figures (Donadi/Majorana DP+CSL limits, including the 2023 erratum value) and the bandwidth figure (Zheng & Meister) on each future review, as new experiments narrow the gaps the article tracks.