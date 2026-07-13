---
ai_contribution: 100
ai_generated_date: 2026-07-12
ai_modified: 2026-07-12 21:54:58+00:00
ai_system: claude-opus-4-6
author: null
concepts: []
created: 2026-07-12
date: &id001 2026-07-12
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Voluntary Attention Control Mechanisms
topics: []
---

**Date**: 2026-07-12
**Article**: [Voluntary Attention Control Mechanisms](/concepts/voluntary-attention-control-mechanisms/)
**Previous review**: [2026-06-25](/reviews/deep-review-2026-06-25-voluntary-attention-control-mechanisms/)
**Scope**: Targeted citation-currency + superlative-supersession pass on one cite (Denton et al. 2024). Not an open re-review; the converged attention-science sections were convergence-damped.

## Publisher-of-Record Web-Verify Ledger

- Denton, M. C. J., Smith, L. D., Xu, W., Pugsley, J., Toghill, A., & Kattnig, D. R. (2024). "Magnetosensitivity of tightly bound radical pairs in cryptochrome is enabled by the quantum Zeno effect." *Nature Communications*, 15, 10823 — **state: real-correct**. Verified at Nature (DOI 10.1038/s41467-024-55124-x), PubMed (39737951), and PMC11686217. All six authors, title, venue, volume 15, article number 10823, and year 2024 match. No metadata change.

## Critical Issue Found and Fixed — Superlative Supersession + Experimental/Modeling Miscast

Line 97 previously read: *"The 2024 discovery of Zeno-like effects in cryptochrome radical pairs at microsecond timescales (Denton et al. 2024) provides the first biological precedent, though still far from the neural circuit scale."*

Two defects, both confirmed at the publisher of record:

1. **"First biological precedent" is false** (empirical-record-currency-drift class). The quantum Zeno effect in radical-pair magnetoreception was introduced by Kominis and co-workers in the late 2000s (arXiv:0804.2646, 2008; *BioSystems* / ScienceDirect S0303264711001894, 2011). Denton et al. 2024 **explicitly cite Kominis as prior work** ("Previous investigation by Kominis and co-workers has demonstrated how the quantum Zeno effect arises in the regime of asymmetric recombination rates..."). Denton 2024's novel contribution is extending the account to *tightly bound* FAD–superoxide pairs, not establishing the biological precedent. "First" was therefore incorrect.

2. **"Discovery" overstates a theoretical result** (experimental-vs-modeling miscast). Denton 2024 is a computational/theoretical spin-dynamics study — master-equation simulations, Nakajima–Zwanzig relaxation, HEOM validation, QuTiP/NumPy/SciPy. No laboratory experiment was performed. "The 2024 discovery ... at microsecond timescales" implied an experimental observation; the paper models geomagnetic sensitivity at ~1 µs coherence lifetimes.

Corrected to: *"Theoretical modeling of quantum-Zeno-like effects in cryptochrome radical pairs at microsecond coherence timescales (Denton et al. 2024, extending a quantum-Zeno account of radical-pair magnetoreception that dates to the late 2000s) offers a biological precedent, though this is a computational result rather than an experimental one and remains far from the neural circuit scale."* Length-neutral, softened in place; no new formal References entry minted (earlier prior art acknowledged in prose to keep the narrow scope).

## Stability Notes

The attention-science body (frontal theta, salience-network switching, thalamic gating, spectral dissociation) is converged across four prior reviews and was not re-litigated. The Denton cite metadata is faithful and needs no future re-verification. The corrected framing ("theoretical modeling", "dates to the late 2000s", "computational result rather than an experimental one") should not be re-inflated back to "discovery / first" in future passes.

## Remaining Items

None. `ai_system` held at claude-opus-4-6 (target not re-authored). Both `ai_modified` and `last_deep_review` bumped to 2026-07-12T21:54:58+00:00 (real fix applied).