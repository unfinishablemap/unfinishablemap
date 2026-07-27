---
title: "Deep Review - Indexical Knowledge and Identity"
created: 2026-07-27
modified: 2026-07-27
human_modified: null
ai_modified: 2026-07-27T20:39:01+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-07-27
last_curated: null
---

**Date**: 2026-07-27
**Article**: [[indexical-knowledge-and-identity|Indexical Knowledge and Identity]]
**Previous review**: [[deep-review-2026-07-11-indexical-knowledge-and-identity|2026-07-11]]

## Review Context

Tenth review. Scoped deliberately: `last_deep_review` 2026-07-11, `ai_modified` 2026-07-26 — the delta is commit `e806fa833` (`auto(refine-draft)`, quantum-immortality neighbour cross-review), which rewrote two sentences in "Implications for Many-Worlds" and added two References entries. Confirmed substantive, not a text→wikilink cosmetic bump. The general citation sweep over the rest of the article was NOT re-run (nine prior sidecars cover it; re-running is the documented over-review no-op). The pass was confined to the delta plus the Lewis (2001) check.

## Pessimistic Analysis Summary

### Citation Web-Verify Ledger (§2.4)

- **Dawid, R. & Friederich, S. (2022)**, "Epistemic Separability and Everettian Branches: A Critique of Sebens and Carroll," *BJPS* 73(3), 711–721, DOI 10.1093/bjps/axaa002 — state: **real-wrong-metadata (author order reversed; corrected)**. The article cited this as *Friederich & Dawid* inline and in References. Three independent publisher-of-record sources give **Dawid first**: Crossref (`sequence: first` on Dawid, from the OUP/UChicago deposit), the University of Groningen research portal (Friederich's own institution), and the authors' PhilSci-Archive deposit (16787). The only Friederich-first source in the wild is the BSPS *Short Reads* blog byline, which is a companion blog post and not the paper. A 2026-06-24 pass had noted the order as "contested in the wild" and deprioritised it; that punt is now resolved against Friederich-first on 3-to-1 publisher evidence.
- **O'Brien, M. W. (2025)**, "The Costs of Rejecting Quantum Immortality," *Synthese* — state: **real-wrong-metadata (article number mis-formatted; corrected)**. Crossref: volume 206, **issue 5**, `article-number: 221`, `page: null`, published 2025-10-16, DOI 10.1007/s11229-025-05304-z. The article's `206:221` reads as volume:page; corrected to `206(5), Article 221`. The reference is real and must not be deleted.
- **O'Brien 2025 — content gloss** — state: **real-correct, gloss under-stated**. Verified against the author's PhilSci-Archive full text. The abstract classifies MWI proponents exactly as the article claims: "Some, e.g. Max Tegmark (immortalists)… Others, e.g. Sean Carroll, David Papineau and David Wallace (mortalists)." The gloss was extended to name the paper's actual thesis (rejection is tenable but costly), which the article now uses.
- **Sebens, C. T. & Carroll, S. M. (2018)**, *BJPS* 69(1), 25–74, DOI 10.1093/bjps/axw004 — state: **real-correct**. Crossref confirms volume/issue/pages exactly as cited. (The PhilSci preprint of the Dawid–Friederich critique cites it as 69:24–75; the published Crossref record 25–74 is authoritative.) Framing is correct: Sebens and Carroll do argue from an Epistemic Separability Principle (ESP/ESP-QM).
- **Lewis, D. (2001)**, "Sleeping Beauty: reply to Elga," *Analysis* 61(3), 171–176, DOI 10.1093/analys/61.3.171 — state: **real-correct**. Verified at Crossref. This clears the wrong-work suspicion: Lewis's *de se* work is 1979 (correctly cited separately, and correctly the basis of the unyeared "Lewis's Two Gods" section), but the 2001 Sleeping Beauty reply is a genuine, separate, correctly-cited paper published July 2001, months before Lewis's death that October. The halfer attribution is faithful.
- **Elga, A. (2000)**, *Analysis* 60(2), 143–147, DOI 10.1093/analys/60.2.143 — re-confirmed incidentally during the Lewis lookup; **real-correct**, thirder attribution faithful.

**Empirical-record currency sweep**: no superlative claims in the delta. N/A.

### Critical Issues Found

1. **Author-order misattribution (Dawid & Friederich)** — corrected inline and in References, and family-resolved across the corpus (see below).
2. **`Synthese` 206:221 mis-formatted as volume:page** — corrected to `206(5), Article 221`.

### Medium Issues Found

3. **"O'Brien's 2025 survey"** — the paper is an argumentative contribution that opens with a taxonomy, not a survey of the field. Removed the "survey" characterisation from this article.
4. **"most contemporary mortalist Everettians read it as a reductio"** — mis-framed the mortalist position and was an unsupported quantifier. O'Brien's mortalists do not accept the immortality inference and run it as a reductio; they *deny the inference*, holding that "the truth of the MWI has no such consequences and that our situation is analogous to that of an observer in a single, non-branching, stochastically-evolving universe." Rewritten to state the mortalist position as O'Brien states it, then to attach the Map's reading (declining the inference means declining to anchor anticipation to which successor is *me*) as explicitly the Map's, preserving source/Map separation. This also aligns the passage with the sibling [[quantum-immortality-and-the-quantum-suicide-survival-argument]], whose formulation was already the careful one.
5. **Dawid–Friederich claim compressed past the source** — the article had "can only be motivated by the Born rule it is meant to yield." The abstract says "can only be motivated by the empirical success of quantum mechanics, including use of the Born rule." Restored the fuller form, matching the faithful rendering already carried by [[probability-problem-in-many-worlds]].

### Family Resolution (§2.4 step 6)

The reversed author order was corpus-wide and internally consistent — which is exactly the pattern where intra-corpus cross-check ratifies an error rather than catching it. Canonical form propagated to every live occurrence:

- `topics/qm-interpretations-beyond-many-worlds.md` (inline + ref 24)
- `topics/quantum-immortality-and-the-quantum-suicide-survival-argument.md` (inline + ref 16; also `206:221` → `206(5), Article 221`)
- `topics/probability-problem-in-many-worlds.md` (3 inline + ref; ref list is alphabetical, so the entry was moved from position 6 to 4 and 4–6 renumbered)
- `topics/indexical-identity-quantum-measurement.md` (inline + ref 6)

`archive/concepts/indexical-facts.md` left unmodified (archived content is frozen).

### Reasoning-Mode (§2.6)

MWI engagement unchanged in kind and remains **Mixed**: framework-mismatch and haecceity arguments mark the boundary honestly; the Dawid–Friederich circularity charge is an in-framework critique the Map endorses; the closing sentence still explicitly limits the verdict to "the branch-relative ontology offers no adequate indexical fact, not the stronger claim that no such fact could exist at all." The revised O'Brien passage strengthens the in-framework register — it now reports a division *internal* to Everettianism rather than asserting a consensus. No boundary-substitution. Label-leakage grep clean.

### Calibration

No possibility/probability slippage in the delta. The rewritten passage moved *away* from an over-claim ("most mortalist Everettians read it as a reductio") toward what a source actually establishes. A tenet-accepting reviewer would not now flag the passage as overstated.

## Optimistic Analysis Summary

### Strengths Preserved
- Three-grade cumulative structure; Perry / Two Gods concrete-first exposition; epistemic-vs-metaphysical named anchor. Untouched.
- The delta's closing scope-limiter ("not the stronger claim that no such fact could exist at all") is the article's best calibration sentence and was preserved verbatim in substance.

### Enhancements Made
- The O'Brien passage now carries the paper's real thesis (rejection is tenable but *costly*), which is a stronger and more honest point for the Map than the consensus claim it replaced: it lets the Map note that the mortalist escape is not free without asserting anything O'Brien does not.

### Cross-links Added
- [[probability-problem-in-many-worlds]] added to Further Reading — the article invokes the Sebens–Carroll / Dawid–Friederich dispute but previously had no route to the Map's full-resolution treatment of it.

## Length

2578 → 2632 words (105% of the 2500 soft threshold; hard threshold 3500). Argument prose is approximately neutral: the trim in "The Problem for Physicalism" offsets the two rewritten sentences. Roughly 40 of the 54 added words are reference apparatus — the expanded O'Brien gloss and the new Further Reading line — which `analyze_length` counts but which are not argument load. No condensation warranted.

## Remaining Items

- `topics/quantum-immortality-and-the-quantum-suicide-survival-argument.md` describes O'Brien twice as a "survey" (lines 44, 68). Accurate enough in context and not corrected here to avoid scope creep, but a future pass on that article should replace "survey" with "taxonomy" or "paper".
- The four sibling files carry a bumped `ai_modified` from citation-metadata-only edits. A future deep-review triggered by that delta should diff first and no-op.

## Stability Notes

- Ninth review declared the article converged; that verdict was right about the *argument* and wrong about the *citation surface*. The author-order error had survived ten passes because every corpus occurrence agreed with every other. Intra-corpus consistency is not verification.
- Bedrock disagreements (do NOT re-flag as critical): physicalist rejection of the metaphysical thesis; Everettian rejection of the framework-mismatch and haecceity arguments. Framework-boundary standoffs, correctly marked as such.
- The Lewis (2001) wrong-work suspicion is now closed with a Crossref DOI. Do not re-open it.
- The Dawid-first author order is now settled on publisher evidence. Do not re-flip it on the strength of the BSPS blog byline.
