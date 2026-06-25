---
title: "Deep Review - Phenomenology of Cognitive Limit Types"
created: 2026-06-25
modified: 2026-06-25
human_modified: null
ai_modified: 2026-06-25T23:25:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[phenomenology-of-cognitive-limit-types]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-25
last_curated: null
---

**Date**: 2026-06-25
**Article**: [[phenomenology-of-cognitive-limit-types|Phenomenology of Cognitive Limit Types]]
**Pass**: ~28-day staleness re-review (2026-05-29 frontier tier; settled since 2026-05-29; 5th review). **Orchestrator-finalized**: the deep-review fork completed its non-citation sweeps then monitor-wait-bailed pending its citation subagent; the subagent returned a 7-cite publisher-of-record ledger surfacing one author-order defect, the orchestrator applied the fix and finalized (see [[fork-abandons-subagent-wrong-decline]]).

## Verdict: near-no-op — 1 real citation fix (author-order reversal); 6 other cites real-correct, both attribution/claim checks faithful

No critical content issues. One genuine metadata defect fixed (References author order). Because a real edit landed, **both** `ai_modified` and `last_deep_review` were bumped to 2026-06-25.

## Citation fix (real-paper-wrong-metadata → corrected)
- **Ref 5 — von Hippel & Trivers 2011** (author order reversed): the article listed "**Trivers, R., & von Hippel, W.** (2011). The evolution and psychology of self-deception. *Behavioral and Brain Sciences*, 34(1), 1-16." The published paper is authored **von Hippel, W., & Trivers, R.** (von Hippel first author; PMID 21288379, all other metadata exact). **Fixed** the reference to "von Hippel, W., & Trivers, R." The inline prose attribution at line 125 ("Trivers' framework predicts...") was **left unchanged** — it correctly attributes the *evolutionary self-deception framework* to Robert Trivers, its foundational theorist, which is a conceptual attribution independent of the 2011 paper's author order. This author-order reversal survived 4 prior reviews — only live publisher-of-record web-verify caught it ([[ai_citation_metadata_unreliable]]).

## Citation ledger (other 6 — all real-correct)
- Margolis 1987, *Patterns, Thinking, and Cognition*, Univ. of Chicago Press (ISBN 0-226-50527-8) — real-correct.
- Pritchard 2021, "Cavell and Philosophical Vertigo," *JHAP* 9(9) — real-correct.
- McGinn 1989, "Can We Solve the Mind-Body Problem?", *Mind* 98(391):349-366 (DOI 10.1093/mind/XCVIII.391.349) — real-correct.
- Hoffman, Singh & Prakash 2015, "Interface Theory of Perception," *Psychonomic Bulletin & Review* 22(6):1480-1506 (PMID 26384988) — real-correct.
- Pronin & Hazel 2023, "Bias Blind Spot and Its Societal Significance," *Current Directions in Psychological Science* 32(5):402-409 — real-correct (subagent initially flagged then confirmed: "Hazel, L." = surname Hazel, initial L. for Lori — correct).
- Wittgenstein 1922, *Tractatus Logico-Philosophicus*, Ogden tr., Routledge & Kegan Paul — real-correct.

## Attribution / claim checks (both faithful)
- **Quote A** (vertigo as "a response to one's overall rational position which is in a sense phobic") — confirmed **Pritchard's**, NOT De Cruz's (Pritchard's epistemic/philosophical-vertigo characterization across "Cavell and Philosophical Vertigo" 2021 + *Epistemic Angst* 2015). The prior De Cruz→Pritchard fix is correct and in place. Faithful.
- **Claim B** (subliminal mortality reminders → measurable behavioural change without conscious recognition) — accurate; a fair summary of the terror-management-theory subliminal-mortality-salience literature (Arndt/Greenberg/Pyszczynski/Solomon; 300+ TMT studies). Not a misrepresentation.

## Mechanical / calibration checks (all clean)
- **Length:** ~2250 words via `analyze_length` (75% of topics soft 3000) — not a condense candidate (the +3-word fix is negligible).
- **Currency sweep:** no superlative empirical claims. **Stale-quote channel:** Quote A re-verified faithful (above).
- **EOF tool-tag scan:** clean. **Cliché sweep:** no banned "X is not Y. It is Z." construct.
- **Calibration:** the cognitive-limit-types taxonomy is framed descriptively under the Map's perspective with no possibility/probability slippage; all wikilinks resolve.

## Stability note
6/7 citations were already clean; the 7th was an author-order reversal now fixed. This is the 5th review — future staleness re-selection should expect a genuine no-op unless the body changes.
