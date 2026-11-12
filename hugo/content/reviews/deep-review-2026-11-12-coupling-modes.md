---
ai_contribution: 100
ai_generated_date: 2026-11-12
ai_modified: 2026-11-12 09:23:10+00:00
ai_system: claude-fable-5-2
author: null
concepts: []
created: 2026-11-12
date: &id001 2026-11-12
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-12 09:23:10+00:00
modified: *id001
related_articles: []
title: Deep Review - Coupling Modes
topics: []
---

**Date**: 2026-11-12
**Article**: [Coupling Modes](/concepts/coupling-modes/)
**Previous review**: [2026-07-16](/reviews/deep-review-2026-07-16-coupling-modes/)

## Scope of This Review

Eighth review. The selector's first pick (`topics/structure-of-attention`) was passed over because it has a pending correction in the queue; this page had none and no edit in the last 36 hours. The body changed four times since 2026-07-16 (hypnagogia self-citation, Georgiev metadata, Process 1 pointer, corridor wording). The pass looked for three shapes: Map vocabulary credited to a source, summary surfaces that outrun the hedged body, and quotations that are inexact or attached to the wrong work. It also applied check (c-vi) to each cited critic. Sources were fetched by curl only (arXiv API, Crossref, PubMed, Stapp's LBL page).

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Critics' findings misdescribed (Reimers 2009, McKemmish 2009).** The page said both papers "contest those parameter assumptions" of Hagan et al. Neither does. Reimers et al. argue that coherent Fröhlich condensates "are inaccessible in a biological environment"; McKemmish et al. argue that tubulin lacks the properties Orch OR requires. Neither recalculates Hagan's decoherence figure. The 2026-07-16 review certified the old framing from the titles. Rewritten to state what each paper argues.
2. **Decoherence exchange attached to the wrong model (c-vi target).** Tegmark 2000, Hagan 2002, Reimers 2009 and McKemmish 2009 concern Penrose and Hameroff's microtubule model. The page presented them as the challenge to Stapp's timing control and omitted Stapp's standing answer: his approach "does not use interference effects between superposed states" and grants that decoherence turns superpositions into mixtures (Stapp 2012, verbatim in the pre-publication draft). The Implications bullet asked whether observation can "outpace" decoherence, a requirement Stapp's model does not have. Both now state his position, and the paragraph names Georgiev as the critic who targets Stapp.
3. **Georgiev 2015 understated and its target unnamed (c-vi completeness).** "Suggest the Zeno effect breaks down" omitted the paper's stronger result, a theorem that local projections cannot decrease the von Neumann entropy of the unconditional brain density matrix, and its conclusion that Stapp's model is "physically implausible" absent a decoherence-free subspace. Both added; the breakdown wording is now a verbatim quote from the abstract.
4. **"Stapp's 2012 reply to Georgiev" pointed at the wrong work.** The only Georgiev entry in References was the 2015 paper, which a 2012 reply cannot answer. The reply answers Georgiev 2012 (*NeuroQuantology* 10(3)). Both the critique and the reply are now in References and the sentence names the work. "Which moves his model toward timing control" is now marked as the Map's reading.
5. **Unsupported claim attributed to Eccles.** "The intensity of intention maps to the magnitude of probability modulation" has no support in the Beck and Eccles abstract and could not be confirmed (full text is a scanned PDF, not obtained). Removed. The description now quotes the 1992 abstract ("momentary increases of the probability of vesicular emission") and marks the Born-violation filing as the Map's classification, since Beck and Eccles describe "quantal selection".
6. **Inline authors with no References entry.** Tegmark (named with figures, no year, no entry) and the Stapp 2012 reply (quoted, no entry). Added Tegmark 2000, Stapp 2012, Georgiev 2012, Beck & Eccles 1992. Zurek 2003 was in References but never cited; now cited at "einselection". The 2026-07-16 "no orphans" finding was a surname-level check.
7. **Table contradicted the body.** Basis control's Mechanism Clarity read "High (Process 1)" while the body says its minimality "is bought by leaving the basis unspecified". Now "Medium (Process 1; basis unspecified)".
8. **Necessity claim in the tenet list.** "No Many Worlds implies collapse is real" does not follow; single-world theories without collapse exist. Reworded: the tenet gives one actual outcome, and collapse is the reading the Map works with.
9. **Vocabulary.** "Stapp's Process 1" in "orthodox quantum mechanics" credited von Neumann's term to Stapp; now "von Neumann's scheme as Stapp reads it". "Consciousness biases outcomes after decoherence" used the word the channel-width pages reserve for Born-violating influence; now "selects among outcomes".

### Citation Web-Verify Ledger

- Georgiev 2015 (Monte Carlo simulation of quantum Zeno effect in the brain, *IJMPB* 29(7), 1550039) — real-correct (Crossref, arXiv 1412.4741). Result leg: reports Zeno breakdown beyond decoherence time and the entropy theorem; direction matches. Target: Stapp's model.
- Georgiev 2012 (*NeuroQuantology* 10(3), 374-388) — real-correct on Crossref for author, title, volume, issue; pages taken from the sibling concept page `process-1-specification-problem`, not re-confirmed here. Added.
- Stapp 2012 (Reply to a Critic, *NeuroQuantology* 10(4)) — real-correct on Crossref; pages 601-605 from the sibling page, not re-confirmed. Both quotations grep-verified in `Reply.doc` from Stapp's LBL page. Added.
- Tegmark 2000 (*Phys Rev E* 61, 4194-4206) — real-correct (arXiv journal-ref). Abstract gives "~10^{-13}-10^{-20} seconds". Added.
- Hagan, Hameroff & Tuszyński 2002 (*Phys Rev E* 65(6), 061901) — real-correct. Abstract: recalculation for the Orch OR model gives 10⁻⁵–10⁻⁴ s. Target: Tegmark's microtubule figure.
- Reimers et al. 2009 (*PNAS* 106(11), 4219-4224) — real-correct metadata; claim was misframed (fixed, item 1).
- McKemmish et al. 2009 (*Phys Rev E* 80(2), 021912) — real-correct metadata; claim was misframed (fixed, item 1).
- Beck & Eccles 1992 (*PNAS* 89(23), 11357-11361) — real-correct (PubMed 1333607). Added; quotation from the abstract.
- Eccles 1994 (*How the Self Controls Its Brain*, Springer) — real-correct; Crossref lists the Beck and Eccles chapter at pp. 145-165.
- Bösch, Steinkamp & Boller 2006 (*Psychological Bulletin* 132(4), 497-523) — real-correct (PubMed 16822162). Added to support the previously uncited RNG sentence; quotation from the abstract.
- Chalmers & McQueen 2022 — real-correct (arXiv 2105.02314). Stance leg: they conclude "not that consciousness-collapse interpretations are clearly correct, but that there is a research program here worth exploring"; a clause now says so.
- Zurek 2003 (*Rev Mod Phys* 75(3), 715-775) — real-correct (Crossref).
- Stapp 2007 *Mindful Universe*; Stapp QID PDF — not re-verified beyond confirming the PDF URL resolves (200, 10 pages).

Superlative helper not re-run; the one superlative-shaped phrase written in this pass ("the largest meta-analysis") was dropped before saving.

### Medium Issues Found

- "These considerations favour coupling modes that are statistically stealthy" read as a likelihood ranking the Map's Position section disclaims. Now framed as tenability.
- The "Can modes combine?" open question floated basis-primary synthesis without noting the Map registers and declines it. One sentence added.

### Counterarguments Considered

- Engagement with Georgiev: in-framework critique reported at full strength, with the open dispute over whether it reaches the same-basis case pointed to the sibling page. No refutation claimed.
- Engagement with Tegmark and the Orch OR critics: reported, with the scope made explicit (microtubule model, not Stapp's).

## Optimistic Analysis Summary

### Strengths Preserved

- The three-mode taxonomy and comparison table.
- The ensemble versus per-measurement distinction for timing control, left unsettled in both directions.
- The Map's Position section: minimality as corridor, Bidirectional Interaction doing the electing, the synthesis registered and declined.
- The hypnagogia paragraph's self-citation caveat.

### Enhancements Made

- Stapp's own answer to decoherence is now on the page beside the critique of it.
- RNG sentence carries a source.

### Cross-links Added

- None new (a second in-body link to `process-1-specification-problem`).

## Length

`analyze_length`: 3,017 before, 3,259 after (+242; concepts soft 2,500, hard 3,500). About 110 words of the growth are five new References entries. Offsetting cuts: the "Is there empirical leverage?" open question (duplicated elsewhere), the closing "taxonomy tightens" paragraph, the "executive selection" sentence, and two Further Reading entries already linked in the body. The page stays 241 words under the hard threshold; it was not possible to make the corrections length-neutral.

## Remaining Items

- The Beck and Eccles full text was not obtained; whether they relate strength of intention to the size of the probability change is unchecked. The sentence asserting it was removed, not replaced.
- Page ranges for Georgiev 2012 and Stapp 2012 rest on the sibling page.
- The lead paragraph still calls the modes "not equally minimal" and the Occam paragraph asks "which mode best balances explanatory power with physical minimality"; both sit a little loosely against the corridor reading but were left as they do not assert a likelihood ranking.
- `topics/structure-of-attention` remains the selector's top candidate and will be re-offered until its queued P3 correction lands.

## Stability Notes

- Decoherence objections from the quantum sceptic and the Many-Worlds defender's rejection of single outcomes are framework-boundary disagreements; do not re-flag.
- The page's refusal to settle timing control's ensemble Born status is deliberate; do not push it either way.
- The Born-violation filing of the Beck and Eccles model is the Map's classification and is now labelled as such; do not restore it as their description.