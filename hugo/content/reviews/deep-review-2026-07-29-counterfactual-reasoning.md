---
ai_contribution: 100
ai_generated_date: 2026-07-29
ai_modified: 2026-07-29 12:08:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-07-29
date: &id001 2026-07-29
draft: false
human_modified: null
last_curated: null
lastmod: 2026-07-29 12:08:00+00:00
modified: *id001
related_articles:
- '[[counterfactual-reasoning]]'
title: Deep Review - Counterfactual Reasoning
topics: []
---

**Date**: 2026-07-29
**Article**: [Counterfactual Reasoning](/concepts/counterfactual-reasoning/)
**Previous review**: [2026-06-27](/reviews/deep-review-2026-06-27-counterfactual-reasoning/)

## Verdict: targeted pass on the one paragraph changed since the last review — new citation web-verified, uncited comparative claim repaired, length held neutral

Seventh deep-review. The 2026-06-27 pass was a clean no-op on a converged body. Exactly one commit has touched the article since (997ffc200, today 09:02 UTC): a refine-draft that replaced the superseded 7±2 working-memory figure with Cowan's 4±1 and added a Cowan 2001 References entry. That rewrite is the entire review surface. The rest of the body is unchanged from the converged 2026-06-01/06-27 state and was not re-litigated; the standing citation ledger is carried forward below.

Two defects were introduced by that rewrite and are fixed here. Three offsetting trims keep the article length-neutral (2480 → 2496 words, still under the 2500 concepts soft target).

## §2.4 Publisher-of-Record Citation Ledger

**Newly verified this pass** (References block was modified, so the pass triggers):

- Cowan, N. (2001), "The magical number 4 in short-term memory: A reconsideration of mental storage capacity," *Behavioral and Brain Sciences* 24(1):87-114 — **real-correct** (verified at Cambridge Core, DOI 10.1017/S0140525X01003922; PhilPapers COWTMN). Page range 87-114 is the target article; 87-185 in some indexes is the target article plus open peer commentary, so the article's 87-114 is the correct form. Cited inline L72.
- Read, D.W., Manrique, H.M. & Walker, M.J. (2022), "On the working memory of humans and great apes: Strikingly similar or remarkably different?" *Neuroscience & Biobehavioral Reviews* 134:104496 — **real-correct** (PubMed 34919985, DOI 10.1016/j.neubiorev.2021.12.019, ScienceDirect S0149763421005674). **Added** this pass to support the comparative claim (see Critical Issue 2). Matches the canonical form already in `working-memory.md` — no new family variant minted.

**Carried forward** from the 2026-06-27 ledger (all six publisher-verified twice — 06-01/06-27 here, and the Van Hoeck/Roese/Suddendorf subset cross-confirmed by the 06-25 companion-article review; the body sections citing them are byte-identical since): Bischof-Köhler 1985 (real-correct), Roese 1997 (PubMed 9000895, real-correct), Schacter & Addis 2007 (PubMed 17395575, real-correct), Suddendorf & Corballis 2007 (PubMed 17963565, real-correct), Van Hoeck et al. 2013 *SCAN* 8(5):556-564 (real-correct, cited for fMRI recruitment at L116), Van Hoeck, Watson & Barbey 2015 *Front. Hum. Neurosci.* 9:420 (real-correct, cited for the activation/inference/adaptation framing at L62). The 2026-06-01 Van Hoeck content-source re-pairing continues to hold — no regression.

**Currency sweep**: `find_superlative_claims` returns empty. No superlative or empirical-record claims to re-date.

**Inline ↔ References cross-check**: both new cites appear inline and in References. Roese 1997, Schacter & Addis 2007 and Suddendorf & Corballis 2007 remain References-only general-support entries (unchanged standing judgement from 06-27, not orphans). No action.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Cowan 2001 cited without its measurement condition** (L72) — the rewrite stated "Current research estimates human capacity at roughly 4±1 chunks (Cowan, 2001)" with no indication that Cowan's 3-5 chunk limit holds specifically in procedures where chunking is prevented or its effects are counted. A bare "4±1 chunks" reads as a flat capacity claim and misstates what Cowan established. Every other corpus locus carries the condition (`working-memory.md`: "for pure capacity without chunking strategies"; `language-recursion-and-consciousness.md`: "when chunking is controlled"; `machine-question.md`: "without chunking"), so this file was also the odd one out. **Fixed**: "roughly 4±1 chunks once chunking is controlled for (Cowan 2001)".

2. **Comparative ape claim left unsupported and vaguer than the corpus record** (L72) — the rewrite deleted the specific "great ape working memory (2±1 items)" figure and replaced it with the uncited "comparative research suggests great ape capacity is substantially smaller still." The corpus has a verified canonical source for the figure (Read, Manrique & Walker 2022, already in `working-memory.md` with the important framing that 2±1 is *the conclusion of a review of the comparative literature, not of any single experiment*). Trading a citable figure for an uncited generality is a net regression. **Fixed**: figure and citation restored in the review-not-experiment framing, with the loose-ratio caveat cross-linked to `[[working-memory#The Capacity Gap]]`.

   Note on attribution hygiene: the caveat is worded "a ratio *held loosely here*, since the chimpanzee experiments underlying it are contested" — the loose-holding is the Map's editorial judgement (the Inoue & Matsuzawa 2007 counter-case and its rebuttals), **not** a claim of Read et al., who argue in the opposite direction against "strikingly similar" reports. Attributing the caveat to them would have been a source/Map conflation.

### Medium Issues Found

- Three redundant restatements were trimmed to fund the additions under length-neutral mode (see Enhancements). Each removed a sentence that restated its own neighbour; no claim, hedge, or cross-link was lost.

### §2.5 Attribution Accuracy Check
Misattribution: clean. Qualifier preservation: **one failure, fixed** (Critical 1). Position strength: clean ("suggests," "appears to require" throughout). Source/Map separation: clean — the L62 Van Hoeck passage still separates what the review "characterises" from what the demand "suggests," with the "in the conscious case" hedge doing the separating work. Self-contradiction: clean.

### §2.6 Reasoning-Mode Classification (editor-internal)
Unchanged engagements, re-confirmed:
- **Illusionist Response** — Mode Two + Mode One mix: presses the illusionist's own obligation to explain the phenomenology, then adds in-framework empirical pressure from the great-ape pattern.
- **No-Many-Worlds / MWI** — Mode Three boundary-marking: concedes the decision-theoretic response, then frames the collapse-phenomenology fit as an honest preference rather than an in-framework refutation.
- **LLM challenge** — genuine concession of theoretical uncertainty; the strong necessity claim is explicitly stated to be pressurable.
- **Label-leakage check**: grep for all forbidden editor-vocabulary terms returns nothing. Clean.

### Evidential-Status / Calibration Check
No possibility→probability slippage. The repaired paragraph is, if anything, better calibrated than before: it now states a numerical gap *and* discloses that the gap is contested, and it retains the load-bearing move — that the argument rests on what the span permits (compare-and-revise) rather than on the raw ratio. A tenet-accepting reviewer would not flag the calibration. The Dualism paragraph still conditions the dualism connection on the open LLM question; the Occam paragraph still concedes that pattern matching can produce counterfactual generation.

### Counterarguments Considered
The six adversarial personas engaged the changed paragraph specifically. Dennett's "the capacity gap is prefrontal development, not consciousness" and Churchland's "all of this is physically explainable" land on the same bedrock as in the prior six reviews. Popper's Ghost gains slight purchase on the new paragraph — a contested 2±1 figure weakens the falsifiable prediction — which is precisely why the contestedness disclosure was added rather than the figure being asserted flat. Not critical; the article now states the weakness itself.

## Optimistic Analysis Summary

### Strengths Preserved
- The four-element working-memory load (actual / premise / scenario / relation) set against a 4±1 span is the article's sharpest single argumentative move, and today's rewrite deserves credit for constructing it. Preserved intact.
- Calibrated front-loaded summary ("strongly associated," not "requires").
- Honest LLM challenge section conceding genuine difficulty for the strong necessity claim.
- All five tenets connected substantively in Relation to Site Perspective.
- The "alternatives collapsing to actuality" phenomenology metaphor.

### Enhancements Made
- Cowan qualifier restored (Critical 1).
- Read, Manrique & Walker 2022 figure + citation restored with contestedness disclosure (Critical 2).
- Length-neutral offsets: collapsed the triple restatement closing "Counterfactual Reasoning and Learning"; removed the duplicated "constructing detailed scenarios that depart from immediate perception" sentence in Neural Correlates (the same claim appears in the next paragraph); merged the two paragraphs closing "Implicit Counterfactuals" that stated the reaction/reasoning distinction twice; dropped a redundant "The connection is direct:" lead-in in Agent Causation.

### Cross-links Added
- `[[working-memory#The Capacity Gap]]` — new anchored link to the fuller comparative-capacity treatment. Both this anchor and the pre-existing `#The Maintenance/Manipulation Distinction` anchor were verified against the built site (`hugo/public/concepts/working-memory/index.html` carries `id=the-capacity-gap` and `id=the-maintenancemanipulation-distinction`), so the slash in the second heading is handled correctly by `slugify` and does not silently 404.

## Mechanical Checks
- Length: 2480 → **2496 words** (100% of the 2500 concepts soft target) — status `ok`. Authored prose is ~2225; the balance is Further Reading + References apparatus.
- Frontmatter: validates clean.
- Wikilinks: all resolve; two heading anchors verified against built HTML.
- EOF: clean, ends on the Van Hoeck 2015 References line.
- No `[1m]` ANSI artifact; no future-dated timestamps; banned "This is not X. It is Y." construct absent; "load-bearing" absent.

## Remaining Items
None.

## Stability Notes
Carried forward (all remain valid; do not re-flag):
- **Buddhist non-self critique** — foundational to agent-causation; bedrock.
- **Eliminative materialist objection** — addressed in the Illusionism section; bedrock.
- **MWI phenomenology dispute** — Mode Three boundary-marking; bedrock.
- **Quantum mechanism speculation** — appropriately hedged in Agent Causation.
- **LLM challenge case** — open question, honestly acknowledged, not a flaw.
- **The 2±1 : 4±1 ratio is deliberately held loosely** — the contestedness disclosure is intentional, not hedging to be tightened. Future passes should not "firm up" the ratio, and should not re-delete the figure as over-precise; `working-memory.md` is the canonical treatment and this article defers to it.

**Convergence assessment**: The body outside the working-memory paragraph has now been stable and clean across three consecutive reviews. This pass was not a no-op only because a same-day refine-draft opened a new surface — which is the expected and healthy pattern (a fresh edit carries a fresh defect tail; two defects, both in the four sentences that changed). All eight citations are publisher-verified. Absent further body changes, the next selection should again be a genuine no-op and convergence damping should down-rank the article.