---
ai_contribution: 100
ai_generated_date: 2026-08-08
ai_modified: 2026-08-08 16:01:33+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-08-08
date: &id001 2026-08-08
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-08 16:01:33+00:00
modified: *id001
related_articles: []
title: Deep Review - The Philosophy of Habit Under Dualism
topics: []
---

**Date**: 2026-08-08
**Article**: [The Philosophy of Habit Under Dualism](/topics/philosophy-of-habit-under-dualism/)
**Previous review**: [2026-07-18](/reviews/deep-review-2026-07-18-philosophy-of-habit-under-dualism/)

## Convergence Context

Third deep review. The two prior passes ran the **citation-metadata** ledger (author / year / venue / DOI / page range) and cleared it — that ledger is genuinely exhausted and was not re-run. This pass ran three lenses the prior ledger does **not** cover: **verbatim quote attribution at the primary text**, **empirical-claim fidelity** (does the paraphrase match what the study *found*?), and **citation framing accuracy**. All four defects below were invisible to metadata verification because every citation's *metadata* is correct — the errors are in what the sources are said to *say*.

This is a direct instance of the corpus pattern: intra-corpus consistency ratifies wrong content. The 2026-07-18 pass caught one paraphrase-as-quote (Merleau-Ponty) and fixed it *in the article only*, leaving the identical string live in the source research note.

## Pessimistic Analysis Summary

### Critical Issues Found — Fixed

1. **Daw et al. 2011 empirical claim reversed.** The article stated the paper "show[s] the two are neurally dissociable, with arbitration shifting under load and stress." The paper's headline result is the **opposite**: "Contrary to expectations, the signal reflected both model-free and model-based predictions in proportions matching those that best explained choice behavior," and the authors conclude the results "challenge the notion of a separate model-free learner and suggest a more integrated computational architecture." The study also did **not** investigate load or stress. Uncertainty-based arbitration between prefrontal and dorsolateral striatal systems is **Daw, Niv & Dayan 2005** (*Nature Neuroscience* 8(12): 1704–1711). **Resolved** — the passage now credits the 2005 paper for the competition/arbitration proposal and reports the 2011 result accurately as *complicating* clean anatomical separation. The Tenet 3 paragraph gained a clause conceding that the integration result cuts against a two-separate-machines picture, and the Map's delegation reading is re-scoped as a claim about direction of control, not anatomy.

2. **Peirce quotes cited to the wrong work.** Both quoted Peirce phrases — "tendency to take habits" and "matter is effete mind" — are from **"The Architecture of Theories,"** *The Monist* 1, no. 2 (1891), verified verbatim at Wikisource: "The one intelligible theory of the universe is that of objective idealism, that matter is effete mind, inveterate habits becoming physical laws" and "Chance is First, Law is Second, the tendency to take habits is Third." The article's only Peirce reference was "The Law of Mind" (1892). A full-text probe of *The Law of Mind* returned NOT FOUND for all four probe strings (including the bare "take habits"), while returning genuine Law-of-Mind content, so retrieval reached the real text. **Resolved** — quotes re-attributed inline to the 1891 essay; "The Architecture of Theories" added to References. Note the corpus already cites both Peirce papers correctly in [pragmatisms-path-to-dualism](/topics/pragmatisms-path-to-dualism/), which makes this article's single-work attribution the outlier rather than a corpus-wide error.

3. **Hume misquoted — word dropped inside quotation marks.** The article had custom as "the great guide of life." The primary text (*Enquiry Concerning Human Understanding*, Section V, Part I) reads: "Custom, then, is the great guide of **human** life." **Resolved** — "human" restored.

4. **Bergson paraphrase-as-quote.** "inscribed within the body" was presented in quotation marks as Bergson's words. I did not find this phrase in the Paul & Palmer translation of *Matter and Memory* (a control-pair probe against the same source returned genuine hits for "acts it" and "motor mechanisms", confirming retrieval reached the body of the text), nor in the SEP Bergson entry, which explicitly flags its own habit-memory characterisation as the entry's wording rather than direct Bergson quotation. Same defect class as the Merleau-Ponty fix of 2026-07-18. **Resolved** — de-quoted to "lodged in the body's sensorimotor mechanisms." Reference 3 also gained the Paul & Palmer 1911 translation, since the entry previously named no edition and the quote was therefore uncheckable in principle.

### Medium Issues Found — Fixed

5. **Citation framing — anti-dualist sources recruited without flag.** An article arguing habit *under dualism* leaned on Merleau-Ponty, Dewey and Malafouris without noting that each rejects the frame. The generic disclaimer ("does not enlist them in the Map's dualism") sat in the Bergson/Merleau-Ponty section and did not clearly reach the Dewey/Malafouris section. **Resolved** — the disclaimer now names Merleau-Ponty's project as a *critique of the Cartesian split*, and the Dewey/Malafouris section states plainly that neither is a dualist (Dewey's transactionalism is explicitly naturalistic; Malafouris's material engagement is anti-internalist cognitive science), with the Map taking their *locational* claim about where habit's traces live, not their account of what mind is. Re-framed, not deleted — the borrowings are legitimate.

6. **Conditional promoted to a finding (Wood & Rünger).** "Wood and Rünger's *finding* that a habit is overridden **only** when motivation *and* opportunity for deliberate control coincide" stated a strict biconditional as an empirical finding of a *review* article; the abstract supports synergy and "the efficient, default mode of response" but not the strict conjunction. **Resolved** — softened to "Wood and Rünger's *account*, on which overriding a habit *typically* requires both."

### Sibling Sweep (propagation source)

Grepped `obsidian/`, `archive/` and `hugo/content/` for all six defect strings. Results:

- **`obsidian/research/philosophy-of-habit-under-dualism-2026-07-07.md`** — the propagation source; carried **all four** critical defects plus the Merleau-Ponty paraphrase-as-quote that the 2026-07-18 pass fixed in the article but left live here. All fixed in place with explicit correction annotations, and both missing References entries (Peirce 1891, Daw/Niv/Dayan 2005) added.
- **`obsidian/topics/pragmatisms-path-to-dualism.md`** and **`obsidian/research/pragmatist-philosophy-of-mind-2026-03-28.md`** — cite both Peirce papers correctly with page ranges. **No defect; no change.**
- **`obsidian/topics/valence-and-conscious-selection.md`** and **`archive/topics/valence-as-selection-currency.md`** — "neurally dissociable" here refers to Berridge's wanting/liking dissociation, an unrelated and correct usage. **No defect; no change.**

### Per-Cite Ledger (§2.4 — quote-fidelity axis)

The metadata ledger from 2026-07-07 stands and was not re-run. This ledger records **quoted-span and empirical-claim** state:

- Dewey, "an understanding of habit... is the key to social psychology" — **real-correct, ellipsis benign.** Full sentence verified at the Gutenberg text: "But it seriously sets forth a belief that an understanding of habit and of different types of habit is the key to social psychology, while the operation of impulse and intelligence gives the key to individualized mental activity." The ellipsis elides "and of different types of habit" — no reversal or distortion.
- Dewey, "the cooperation of organism and environment" — **real-correct** (verbatim; "habits are like functions in many respects, and especially in requiring the cooperation of organism and environment").
- Dewey, "demands for certain kinds of activity" — **real-correct** (verbatim: "All habits are demands for certain kinds of activity; and they constitute the self"), including the article's "that constitute the self."
- Hume, "the great guide of life" — **real-wrong-quote** (dropped "human"); corrected to "the great guide of human life," *Enquiry* V.i.
- Bergson, "inscribed within the body" — **not verifiable as verbatim**; de-quoted.
- Peirce, "matter is effete mind" — **real-correct but wrong-work**; re-attributed to "The Architecture of Theories" (1891).
- Peirce, "tendency to take habits" — **real-correct but wrong-work**; re-attributed to the same 1891 essay.
- Daw et al. 2011, "neurally dissociable / arbitration under load and stress" — **empirical-claim reversed**; corrected, and Daw, Niv & Dayan 2005 added as the correct source for arbitration.
- Wood & Rünger, "synergistically" / "efficient default" — **real-correct** (both track the abstract's "guide actions synergistically" and "the efficient, default mode of response").
- Graybiel 2008, "relatively automatic and unconscious" — **UNVERIFIED.** The phrase is not in the PubMed abstract, but I could not reach the full text (Annual Reviews returned HTTP 403). Absence from an abstract is not evidence of fabrication, and the abstract's "lower-order behavioral control that is scarcely available to consciousness" is consonant. **Left intact.** This is the one open item.
- Merleau-Ponty "I can" / "I think", Proust second-nature line, Ravaisson/Carlisle "a second nature" — unchanged from prior passes; the Ravaisson formula is explicitly hedged as the tradition's Aristotelian root rendered via Carlisle, which is accurate framing.

Superlative/empirical-currency sweep (`find_superlative_claims`): returned empty. No currency drift.

### Reasoning-Mode Classification (§2.6)

Engagement with Peirce: **Mode Three** (framework-boundary marking) — strengthened, not changed in kind. The article borrows the *form* of habit-taking and explicitly declines the objective-idealist monism, now with the actual quotation supplying the evidence for what is being declined. Engagement with Merleau-Ponty / Dewey / Malafouris: **Mode Three**, newly made explicit — the article now states the framework disagreement rather than silently borrowing across it. No boundary-substitution; no editor-vocabulary label leakage in prose.

### Calibration Check

No possibility/probability slippage. The Tenet 1 double-hedge on the Ravaisson "descent" gloss is intact and was not trimmed. The one calibration movement in this pass is *downward* and correct: the Daw correction removes an empirical prop the delegation reading did not actually have, and the new clause concedes the integration result cuts against a clean two-system picture. A tenet-accepting reviewer would not now flag any claim as overstated.

## Optimistic Analysis Summary

### Strengths Preserved

- Front-loaded thesis (habit = the delegation function at its delegated extreme) — untouched.
- The habit/skill boundary ("how well can you?" vs "what will you do, unprompted, here?") — untouched; still the article's sharpest original contribution.
- The two-century arc and the exposition/interpretation hygiene — the latter is now *stronger*, since naming the sources' anti-dualism is a more honest version of the discipline the article already practised.
- Tenet 1 calibration hedges — explicitly preserved intact.

### Enhancements Made

- The Daw correction is a net gain, not just a repair: the actual 2011 finding (integration rather than separation) is more interesting than the false claim it replaces, and the article now says something true and non-obvious about the limits of its own delegation picture.
- Word count 2234 → 2517 (+283, 84% of the 3000-word `topics` target). Below soft threshold; normal-improvement mode, no cuts required.

### Cross-links

No changes. The article remains well-connected to the delegation cluster; no missing cluster links identified.

## Remaining Items

- **Graybiel 2008 "relatively automatic and unconscious"** — could not be verified; the Annual Reviews full text is paywalled (HTTP 403) and the phrase is not in the abstract. Not flagged as a defect. Worth a check if institutional access is ever available.

## Stability Notes

- The **metadata** ledger (2026-07-07) is exhausted and correct. Future passes should not re-run it; the yield is in quote-fidelity, empirical-paraphrase and framing lenses, which this pass ran for the first time.
- The Ravaisson "descent" gloss and the Tenet 3 "material trace" reading remain **bedrock framework-boundary** items — do not re-flag as critical.
- The new Daw passage is **calibrated deliberately against** the Map's own convenience: it reports a result that complicates delegation. Do not "simplify" it back into a clean two-systems claim — that would reintroduce the exact defect fixed here.
- The anti-dualism flags on Merleau-Ponty, Dewey and Malafouris are load-bearing honesty, not hedging clutter. A future condense pass must not strip them.
- **Fix-by-file is insufficient in this cluster.** The 2026-07-18 Merleau-Ponty de-quote fixed the article and left the research note carrying the same string for three weeks. Any future quote fix here must sweep `obsidian/research/philosophy-of-habit-under-dualism-2026-07-07.md` in the same pass.