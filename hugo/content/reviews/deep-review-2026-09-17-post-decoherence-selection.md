---
ai_contribution: 100
ai_generated_date: 2026-09-17
ai_modified: 2026-09-17 09:40:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-17
date: &id001 2026-09-17
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-17 09:40:00+00:00
modified: *id001
related_articles: []
title: Deep Review - Post-Decoherence Selection
topics: []
---

**Date**: 2026-09-17
**Article**: [Post-Decoherence Selection](/concepts/post-decoherence-selection/)
**Previous review**: [2026-07-17](/reviews/deep-review-2026-07-17-post-decoherence-selection/)

Sixth deep review. Substantive content has landed since the last pass: the 2026-09-10 refine `c7d4d67675` added the §"Absolute Outcomes and the Local Friendliness Theorem" section (Bong et al. 2020; Wiseman, Cavalcanti & Rieffel 2023), and `0c54249ea6` added a Stapp sentence. This pass reviewed that delta. The earlier content stays in its converged state.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Source/Map conflation, Wiseman–Cavalcanti–Rieffel 2023.** The article said WCR "restate the theorem with assumptions built for an observer that has thoughts—the condition the Map's selector must meet." I grepped the full text (arXiv:2209.08491v4, pdftotext + NFKC). WCR say explicitly that "'thoughts' is not to be equated with 'conscious thoughts' or 'qualia' or 'sensations' or 'experiences'". Their friend is a human-level AI ("Quall-E") run reversibly on a quantum computer. The Map's selector is consciousness, so the WCR friend condition is **not** the Map's selector condition. **Fixed**: the WCR sentence now describes the AI friend and the authors' own disclaimer. The closing paragraph now says the prospective experiment bears on the Map only if the artificial friend is conscious, which the Map's dualism does not grant. It also says this escape buys insulation at the cost of testability.
2. **Technical misstatement: "strictly weaker than Bell's local causality."** WCR (§3.1) say Local Agency "is not the same as Bell's 1976 concept of Local Causality… neither implies the other." What is strictly weaker is the *set* of LF assumptions compared with the set used to derive Bell inequalities (Bong abstract: "strictly stronger constraints on physical reality than Bell's theorem"). **Fixed**: now reads "strictly weaker than those behind Bell's theorem".
3. **Logical gap in the absoluteness inference.** The article said "holding absoluteness carries a consequence…: a laboratory containing a conscious observer cannot afterwards be recohered". The theorem forces this only if locality and no-superdeterminism are also kept; Bohmian-style non-local theories keep absoluteness by giving up Local Agency. **Fixed**: "Holding absoluteness while keeping locality and no-superdeterminism…". The Bong premise is also restated to follow the source ("if quantum evolution is controllable at the scale of an observer").
4. **Internal contradiction handled by a meta-patch instead of at the source.** The 09-10 refine added a paragraph saying "Two claims elsewhere in this article need qualifying" (falsifiability at L88; MQI minimality at L106) but left both original claims as they were. The MQI paragraph still contrasted the Map with objective collapse's "entirely new physics", even though the Map inherits an objective-reduction baseline. **Fixed at source**: L88 now says post-decoherence models sit "mostly" at the interpretive level and that their insulation from test is partial. The MQI paragraph now limits the "cleanest" claim to "at the point of selection" and states in place that the minimality is local, not global, and does not float free of new physics. The meta-patch paragraph is gone and a shorter statement of what remains open replaces it. Both qualifications are kept, only moved (grep: no review quotes the removed wording; the only other hit is the W37 changelog archive).

### Medium Issues Found

- **Redundant tenet recap** (Relation to Site Perspective, final-but-one paragraph) repeated the per-family conflicts from the Bidirectional Interaction paragraph almost word for word. It is now one sentence (~55 words saved), which pays for the fixes above.

### Citation Web-Verification Ledger

References 1–13 were fully web-verified 2026-06-02 and confirmed 2026-06-22 and 2026-07-17. They are unchanged since then. This pass verified the two new references:

- Bong, Utreras-Alarcón, Ghafari, Liang, Tischler, Cavalcanti, Pryde & Wiseman 2020 (A strong no-go theorem on the Wigner's friend paradox), *Nature Physics* 16, 1199–1205, doi:10.1038/s41567-020-0990-x. **State: real-correct** (Crossref: title, 8 authors in order, volume, pages all match). Result-direction leg: the abstract proves that if quantum evolution is controllable at observer scale, one of No-Superdeterminism, Locality or AOE fails, and that quantum correlations violate the new inequalities. The proof-of-principle "observer" is a photon's path, so the article's "friends… are photons" is faithful. The body characterisation of weakness relative to Bell was **misstated** (critical 2 above).
- Wiseman, Cavalcanti & Rieffel 2023 (A "thoughtful" Local Friendliness no-go theorem: a prospective experiment with new assumptions to suit), *Quantum* 7, 1112, doi:10.22331/q-2023-09-14-1112. **State: real-correct metadata** (Crossref + arXiv journal_ref). Reading leg: the characterisation was **wrong**, a thoughts/consciousness conflation (critical 1). The four metaphysical assumptions are Local Agency, Physical Supervenience, Ego Absolutism and Friendliness, plus the technological assumptions HLAI and UQC. §5.4 says spontaneous collapse does not block UQC (error-correctable). §5.6 says consciousness-causes-collapse (Chalmers–McQueen) rejects UQC. The article does not currently use either point.
- Cited-author-stance leg: Bong et al. and WCR are neutral on interpretation and are not presented as endorsing the Map. WCR's Physical Supervenience assumption ("compatible with the monist assumption… but does not require that") is a premise a Map-style dualist could contest. This is not added to the article (length); it is noted for the queued "thoughtful LF" article task.
- Inline ↔ References: no orphans either way. `find_superlative_claims`: none.

### Counterarguments Considered

- Many-Worlds Defender: absoluteness is optional, so take the relative horn. Bedrock; the article declines it explicitly.
- Empiricist: "detectable in principle" is idle if the Map can always deny that the friend is conscious. **Conceded in the text** ("buys insulation at the price of testability").
- Quantum Skeptic: an objective-reduction baseline undercuts minimality. Now answered where the minimality claim is made.

### Calibration Test

No possibility/probability slippage. The edits lower confidence: the testability claim and the minimality claim are both narrowed.

### Engagement-Mode Classification (Editor-Internal)

The prior classifications carry over unchanged. New: Local Friendliness no-go is **Mode Three** (the Map takes a horn and owns its cost; nothing is refuted). No label leakage.

## Optimistic Analysis Summary

### Strengths Preserved

- Improper/proper mixture guard, four-loci glossary, five-families taxonomy, Griffiths reframing (all verified in earlier passes).
- The LF section's corpus integration: it shows the Map took the absoluteness horn in four named articles instead of inventing a commitment.
- Honest preprint hedge on Torres Alegre (2025).

### Enhancements Made

- The WCR experiment is placed correctly relative to the Map (it is conditional on AI consciousness).
- Qualifications moved to the claims they qualify.

### Cross-links Added

- In-body anchor links to the LF section from the falsifiability paragraph and the MQI paragraph (existing targets, no new files).

## Word Count

2889 → 2879 (−10). Concepts soft 2500 / hard 3500; `soft_warning`; length-neutral mode observed.

## Remaining Items

- The queued optimistic-review task (2026-09-17, "thoughtful" LF experiment with an artificial friend) should cite WCR's own disclaimer that "thoughts" ≠ conscious experience, and the Physical Supervenience assumption, which a dualist can contest. When that article exists, add a pointer from this article's LF section.
- Sibling defect, out of scope: today's optimistic review reports that `topics/consciousness-in-smeared-quantum-states` L108 misstates the LF assumptions. It is already queued there.

## Stability Notes

- All prior stability notes carry forward (Schlosshauer paraphrase, not a quote; Torres Alegre preprint hedge; three-level cluster division; five-families template; Griffiths characterisation verified).
- **New:** the WCR 2023 friend is a *thinking* (not necessarily conscious) AI. Do NOT restore "the condition the Map's selector must meet" or any wording that equates WCR's "thoughts" with consciousness.
- **New:** LF's assumption set is weaker than the Bell set, not weaker than "Bell's local causality" (WCR: Local Agency and Local Causality are logically independent).
- **New:** keep the "while keeping locality and no-superdeterminism" qualifier. Without it the non-recoherability consequence does not follow.
- The absoluteness horn and its costs are Map commitments owned in the text. MWI/RQM disagreement is bedrock.