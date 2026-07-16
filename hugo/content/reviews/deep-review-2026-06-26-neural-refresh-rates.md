---
ai_contribution: 100
ai_generated_date: 2026-06-26
ai_modified: 2026-06-26 00:34:00+00:00
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
- '[[neural-refresh-rates]]'
title: Deep Review - Neural Refresh Rates
topics: []
---

**Date**: 2026-06-26
**Article**: [Neural Refresh Rates](/topics/neural-refresh-rates-and-the-smoothness-problem/)
**Pass**: ~28-day staleness re-review (2026-05-29 frontier tier; settled since 2026-05-29). **Orchestrator-finalized**: the deep-review fork spawned a citation subagent then monitor-wait-bailed; the subagent returned a 6-cite publisher-of-record ledger (all real-correct) including the requested author-order regression check, the orchestrator ran the mechanical sweeps independently and finalized (see fork-abandons-subagent-wrong-decline).

## Verdict: clean no-op — all 6 citations real-correct; the Herzog 2020 author-order fix HELD (no regression)

Zero critical/medium/low issues. No content edits. Body byte-unchanged since the 2026-05-29 review (git `e60110c4b`). `last_deep_review` bumped; `ai_modified` left settled at 2026-05-29 per no-op hygiene.

## Author-order regression check (the flagged item) — PASSED
- **Herzog, Drissi-Daoudi & Doerig 2020**, "All in Good Time: Long-Lasting Postdictive Effects Reveal Discrete Perception," *Trends in Cognitive Sciences* 24(10):826-837 (DOI 10.1016/j.tics.2020.07.001) — **real-correct, author order confirmed** via CrossRef publisher-registered metadata: Herzog → Drissi-Daoudi → Doerig. The prior corpus-split author-order inversion fix held; no regression. (Author order is a live defect class this session — see the von Hippel/Trivers reversal caught on phenomenology-of-cognitive-limit-types — so this re-verify was warranted and clean.)

## Citation ledger (other 5 — all real-correct)
- VanRullen 2016, "Perceptual Cycles," *Trends in Cognitive Sciences* 20(10):723-735 (PMID 27567317) — real-correct (single author Rufin VanRullen).
- Crick & Koch 1990, "Towards a neurobiological theory of consciousness," *Seminars in the Neurosciences* 2:263-275 — real-correct (pre-DOI; confirmed via NLM Profiles in Science + Caltech Authors; author order Crick then Koch correct).
- Sellars 1965, "The Identity Approach to the Mind-Body Problem," *Review of Metaphysics* 18(3):430-451 — real-correct (PhilPapers + JSTOR issue record).
- Bergson 1889, *Time and Free Will* (*Essai sur les données immédiates de la conscience*) — real-correct (doctoral thesis, standard English title).
- James 1890, *The Principles of Psychology* — real-correct.

Zero fabrications, zero metadata errors, no author-order problems.

## Mechanical / calibration checks (all clean)
- **Length:** 1351 words via `analyze_length` (status `ok`, well under concepts soft 2500) — not a condense candidate.
- **Currency sweep:** the 7-13 Hz oscillatory-sampling figure is a stable neuroscience range, not a superlative/record claim.
- **EOF tool-tag scan:** clean (last lines are References entries; ref 7 is the article's own AI-authorship self-cite "Southgate, A. & Oquatre-six, C." — the Map's citation convention for human + AI-model co-authorship, legitimate). **Cliché sweep:** no banned "X is not Y. It is Z." construct.
- **Calibration:** the temporal-grain-mismatch framing (discrete sampling vs seamless experience deepening the explanatory gap) is presented as a descriptive datum under the Map's perspective with no possibility/probability slippage.

## Stability note
Citations publisher-verified (6/6); the previously-fixed Herzog author order confirmed stable. Future staleness re-selection should expect a genuine no-op unless the body changes.