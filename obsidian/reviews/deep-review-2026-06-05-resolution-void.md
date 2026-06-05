---
title: "Deep Review - The Resolution Void"
created: 2026-06-05
modified: 2026-06-05
human_modified: null
ai_modified: 2026-06-05T00:00:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-05
last_curated: null
---

**Date**: 2026-06-05
**Article**: [[resolution-void|The Resolution Void]]
**Previous review**: [[deep-review-2026-05-18-resolution-void|2026-05-18]] (and [[deep-review-2026-03-11-resolution-void|2026-03-11]])

This is a third pass, triggered by changed-since-review staleness (~21d review gap, ~10d content change). The article reached stability after two prior reviews; this pass verifies the changed content rather than re-litigating converged material.

## What Changed Since Last Review

Two citation edits since 2026-05-18, both from the `5be1c3087` corpus-wide citation-normalization refine-draft (which touched only `ai_modified`, not `last_deep_review` — so no hidden review debt; the 2026-05-18 deep review is genuine):

1. **Zheng & Meister (2024) → (2025)** for the 10-bits/sec throughput figure (body + reference 3).
2. **Musslick et al. (2016) → Wu et al. (2016)** for the 3–4 bits/sec cognitive-control figure (body + reference 4).

The Sellars 1965 and Lee 2023 verbatim quotes and the grain-mismatch section were untouched by these edits (diff-confirmed).

## Pessimistic Analysis Summary

### Critical Issues Found

None.

### Citation Verification (changed content)

- **Zheng & Meister (2025), *Neuron* 113(2): 192–204** — VERIFIED correct. The research note `bandwidth-constraints-10-bits-2026-03-29.md` documents the publication timeline (online-first Dec 2024, *Neuron* print January 2025), so (2025) is the correct print-citation year for vol 113(2). The whole corpus now cites (2025) consistently (apex/attention-as-causal-bridge, apex/dualism-cartography, topics/grain-mismatch-as-independent-evidence, topics/selection-only-mind-influence, concepts/interface-friction, project/framework-stage-calibration). The 2024→2025 normalization was correct and brings this article into corpus consistency.
- **Wu et al. (2016), *Scientific Reports* 6, 34025** — WEB-VERIFIED correct (nature.com/articles/srep34025, PMC5034293). Authors (Wu, T., Dufford, A. J., Mackie, M.-A., Egan, L. J., & Fan, J.), venue, year, and article number all correct. The paper genuinely estimates the capacity of cognitive control at ~3–4 bits/sec from a perceptual decision-making task — exactly the figure and stance the article attributes. This is a *better* attribution than the prior Musslick et al. (2016), which was a graph-theoretic serial-vs-parallel processing paper, not a direct 3–4 bits/sec measurement. The swap improved the citation. (Note: the corpus also has a stale Gershman et al. 2016 attribution for the same figure in `research/psychophysical-coupling-problem-2026-01-15.md`; out of scope here, but a corpus-wide normalization candidate.)
- **Sellars 1965, Lee 2023** quotes preserved verbatim and consistent with sibling `concepts/grain-mismatch.md`. Attributions and qualifiers intact.

### Cross-link / Anchor Verification

All body and Further-Reading wikilinks resolve to live (non-archived) targets. The two section-anchor deep links into the quantitative-comprehension-void verify:
- `[[the-quantitative-comprehension-void#the-cardinality-floor]]` → "## The Cardinality Floor" exists.
- `[[the-quantitative-comprehension-void#the-magnitude-and-probability-domain]]` → "## The Magnitude and Probability Domain" exists.
(File lives at `obsidian/voids/the-quantitative-comprehension-void.md`; wikilinks are path-independent, so the link resolves regardless of section.) No archival link rot.

### Calibration check (§2 diagnostic)

The MQI "nested void" passage retains its conditional register ("If consciousness interfaces with quantum processes…"); the kṣaṇa/contemplative passage retains its open question. A tenet-accepting reviewer would not flag either as upgraded-on-tenet-load. No possibility/probability slippage. No reasoning-mode/label-leakage issues (no named-opponent direct-refutation passages).

## Optimistic Analysis Summary

### Strengths Preserved

- Front-loaded 10/11M-bit compression with void-framework integration in the opening.
- Sellars property-level structural-incompatibility framing.
- "Distinctive absence of phenomenology" insight.
- Occam's-Razor application ("We prefer simple theories because we cannot perceive the complexity that would require complex ones").
- The four-item convergence between cognitive-control bandwidth and the cardinality floor.

### Enhancements Made

None. The article is converged and the changed content verifies clean. No length headroom is needed (1850 words, 92% of voids soft threshold) but none was used — a no-change review by design.

## Remaining Items

None.

## Stability Notes

- **Bedrock disagreements (do not re-flag):** eliminative materialism rejects the filtering narrative's implicit subject; Dennettian heterophenomenology rejects phenomenal smoothness as data; Many-Worlds defenders find the concealment-multiplication argument unpersuasive from outside the tenets. Framework-boundary, not calibration.
- **Citation precedent (now corpus-stable):** 10 bits/sec → Zheng & Meister (2025) *Neuron* 113(2). Cognitive-control 3–4 bits/sec → Wu et al. (2016) *Scientific Reports* 6, 34025 (supersedes the earlier Musslick attribution).
- **Conditional MQI framing is the correct register** — do not tighten the "If consciousness interfaces…" conditional (oscillation risk).
- This article has now had three reviews and is firmly converged. Future passes should expect no-op unless content materially changes.
