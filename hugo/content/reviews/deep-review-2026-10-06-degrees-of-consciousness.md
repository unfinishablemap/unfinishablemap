---
ai_contribution: 100
ai_generated_date: 2026-10-06
ai_modified: 2026-10-06 10:13:00+00:00
ai_system: claude-fable-5-1
author: null
concepts: []
created: 2026-10-06
date: &id001 2026-10-06
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-06 10:13:00+00:00
modified: *id001
related_articles: []
title: Deep Review - Degrees of Consciousness
topics: []
---

**Date**: 2026-10-06
**Article**: [Degrees of Consciousness](/concepts/degrees-of-consciousness/)
**Previous review**: [2026-07-16](/reviews/deep-review-2026-07-16-degrees-of-consciousness/) (7th review overall; prior: 2026-03-20, 2026-03-21, 2026-04-27, 2026-06-01, 2026-06-17, 2026-07-16)

Unlike the 2026-07-16 no-op pass, the delta since the last review is substantive: a reworked lead (2026-09-06, presence/content split and the `moral-status-threshold-or-degrees` reciprocal), a rewritten Clinical Disorders paragraph with a new Schnakers 2009 cite (2026-10-01, covert-consciousness ledger batch D), two altered References entries (Bodien 2024 author list; Metzinger 2020 page range), and the neural-correlates filter-calibration edits across Filter Theory / Emergence vs. Interface / Dualism (2026-10-02). The References block changed, so the §2.4 web-verify pass was mandatory this time. It found no metadata defect in the altered entries but surfaced three uncited-or-overstated empirical claims in prose that six prior passes had carried forward, plus one tier-upgrade on the New York Declaration.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Unsupported superlative + over-specified PCI claim (Anaesthesia §)**: "PCI measurements—*the most rigorous current quantitative probe* of conscious capacity—show continuous, graded changes *under propofol* rather than a sharp threshold." No cite. Casali et al. 2013 (*Sci Transl Med*, PubMed-verified) tested "different levels of sedation induced by anesthetic agents (midazolam, xenon, and propofol)" and reports PCI "reliably discriminated the level of consciousness" — a graded wake→sedation→anaesthesia profile across agents, not a propofol-specific continuous curve, and no publisher calls PCI "the most rigorous current" probe. `find_superlative_claims` returned no hits (the phrase "most rigorous current" is outside its pattern set). **Resolution**: rewritten to "a theory-driven quantitative probe ... falls progressively from wakefulness through sedation to anaesthetic unconsciousness rather than at a single step (Casali et al. 2013)"; ketamine sentence now cites Sarasso et al. 2015. Both added to References.
- **Two unsupported agent-profile claims (Anaesthesia §)**: "Propofol creates relatively sharp transitions" (contradicts the graded-PCI sentence two lines above) and "Xenon produces graded dimming" (Sarasso 2015: xenon abolishes reportable experience — "no conscious experience" — via a global stereotypical slow wave; nothing graded). **Resolution**: replaced with the Sarasso-supported contrast — propofol and xenon abolish reportable experience through distinct cortical response patterns; ketamine preserves vivid states while severing access and motor control.
- **Possibility/probability slippage on the New York Declaration (Animal Cognition §)**: "endorses the view that consciousness is *probably* more widely distributed than previously assumed, *implying* it exists at levels ... that shade continuously downward." The Declaration (live NYU text, fetched) says "strong scientific support" for mammals and birds and "at least a realistic possibility" for all vertebrates and many invertebrates. "Probably" upgrades the tier, and "implying" attributes the Map's continuous-shading inference to the source. A tenet-accepting reviewer would still flag this. **Resolution**: now quotes the two tiers and marks the shading inference as "on this page's reading". The 06-17 ledger's "cited at its own stated evidential level" was wrong on this sentence.
- **Lead/body terminological inconsistency**: lead said anaesthesia reveals "three distinct *levels*" while the Bayne/Hohwy/Owen paragraph declares *levels* talk untenable and the body calls them *states*. **Resolution**: lead → "states" (zero word cost).
- **Orphan References** (§2.4 step 5): Block 1995, Tononi 2008, Ginsburg & Jablonka 2019, Metzinger 2020 and Bodien et al. 2024 had References entries but no inline cite. The 06-17 ledger's "no orphans in either direction" counted topical support as citation. **Resolution**: inline cites installed at the exact supported claim (access consciousness; Φ varies continuously; UAL; minimal phenomenal experience; CMD on imaging). The internal Southgate & Oquatre-cinq entry is served by the `[[minimal-consciousness]]` wikilinks — house convention, not stripped.

### Citation Web-Verify Ledger (§2.4)

Changed or new since 2026-06-17 (verified at Crossref / PubMed / publisher this pass):
- Bodien, Y. G., Allanson, J., Cardone, P., et al. 2024 (*NEJM* 391(7):598-608, DOI 10.1056/NEJMoa2400645) — **real-correct**; Crossref author order Bodien→Allanson→Cardone→Bonhomme (A.)→Carmona confirms the 2026-10-01 correction from the former "Bodien, Claassen et al." form. Result-direction: CMD detected on imaging in behaviourally unresponsive patients — article's claim faithful.
- Metzinger 2020 (*PhiMiSci* 1(I)) — **real-correct**; Crossref `page` = 1-44 (the journal also uses article no. 7; both forms are standard — the 2026-10-01 change to 1-44 is faithful).
- Schnakers et al. 2009 (*BMC Neurology* 9:35, DOI 10.1186/1471-2377-9-35) — **real-correct**; eight authors match Crossref exactly. Result-direction (PubMed abstract, verbatim): "Of the 44 patients diagnosed with VS based on the clinical consensus of the medical team, 18 (41%) were found to be in MCS following standardized assessment with the CRS-R." Article's 41% and direction faithful; the "source's lesson is that unstandardized judgement errs" framing is the paper's own.
- Casali, A. G., Gosseries, O., Rosanova, M., et al. 2013 (*Sci Transl Med* 5(198):198ra105, DOI 10.1126/scitranslmed.3006294) — **newly added, real-correct** (PubMed 23946194). Supports graded PCI across wake/sedation/anaesthesia; does NOT support "continuous ... under propofol" specifically or any "most rigorous" superlative — prose rescoped accordingly.
- Sarasso, S., Boly, M., Napolitani, M., et al. 2015 (*Current Biology* 25(23):3099-3105, DOI 10.1016/j.cub.2015.10.014) — **newly added, real-correct** (Crossref). Result-direction: ketamine → "wakefulness-like, complex spatiotemporal activation pattern" with "long, vivid dreams"; propofol/xenon → low complexity, "no conscious experience". Canonical form already used in `concepts/cross-mechanism-convergence` — no new variant minted.
- Andrews, Birch & Sebo 2024 (New York Declaration) — **real-correct** metadata; **body paraphrase corrected** (tier upgrade "probably" → quoted "at least a realistic possibility"; see Critical Issues).

Unchanged since the full 2026-06-17 ledger and not re-verified (byte-identical entries): Block 1995, Tononi 2008, Ginsburg & Jablonka 2019, Bonhomme et al. 2019, Montupil et al. 2023, Bayne/Hohwy/Owen 2016, Southgate & Oquatre-cinq 2026.

- **Empirical-record currency sweep**: `find_superlative_claims` → no hits; the manual read found the "most rigorous current" superlative it missed (now removed). The Map-internal "catalogue's strongest clinical exhibit" and "cleanest clinical demonstration" are evaluative claims about the Map's own catalogue, not literature superlatives; the latter was folded into a non-superlative clause during the rewrite.
- **Inline ↔ References**: now closed in both directions (11 inline cite forms ↔ 13 entries, with Montupil paired to Bonhomme inline and the internal self-cite served by wikilink).
- **Cited-author-stance leg**: Casali/Sarasso/Tononi are IIT-aligned and are cited for the measurement only; the article's sentence that filter theory reads the ketamine dissociation differently sits in the sibling anaesthesia article, and this page's Emergence vs. Interface already marks the pattern "underdetermined ... not independent confirmations of filter models". No author is presented as endorsing the Map.

### Reasoning-Mode Classification (§2.6)
No named-opponent refutation engagements (unchanged). Production models and IIT engaged descriptively and hedged. Label-leak grep clean.

### Possibility/Probability Slippage Check
One instance found and fixed (Declaration tier, above). The 2026-10-02 calibration edits (Dualism: "compatible ... without discriminating"; Emergence vs. Interface: "discriminate neither"; Filter Theory: "production accounts ... predict it too") are sound and were preserved; the Dualism paragraph was tightened to point at the body pattern rather than restate it.

### Medium Issues Found
- Sleep § ("subjects awakened from slow-wave sleep sometimes report vague, thought-like mentation") and Psychedelic DMN-entropy claims remain uncited. Both are standard-literature claims (Siclari et al. 2017; Carhart-Harris et al. 2014) covered in the linked `dream-consciousness` / `default-mode-network` pages. Deferred — adding cites here would cost ~60 apparatus words on a page sitting at the soft threshold; the hosting pages carry them.

### Counterarguments Considered
Bedrock disagreements from six prior reviews (physicalist gradation-compatibility, MWI rejection, Buddhist no-self) remain standing and were NOT re-flagged.

## Optimistic Analysis Summary

### Strengths Preserved
- Multidimensional intensity/richness/complexity/access analysis with concrete dissociation examples; the dimmer-in-the-interface metaphor nuanced by the Bayne et al. caveat; four-domain evidence organisation; three-position Lower Bound Problem; five substantive tenet connections; the 2026-09-06 presence/content split in the lead and the 2026-10-02 "discriminate neither" calibration.

### Enhancements Made
- Anaesthesia § now carries the two primary PCI sources and states only what they report.
- Declaration quoted at its own two tiers.
- Five topical References promoted to inline cites at the claim they support.
- Lead/body terminology aligned ("states").

### Cross-links
None added or removed; the `is-conscious-being-a-natural-kind` Further Reading blurb was tightened (−15 words) as a length offset.

## Length
2489 → 2528 words total (`analyze_length`, which counts reference apparatus). Split: References +55 (two new entries), Further Reading −15, prose −16 (PCI rewrite, agent-profile rewrite, redundant "multidimensional phenomenon" clause, Dualism restatement, "But the empirical pattern is more complex", ethics sentence). Prose is now ~2055 words; the article sits at 101% of the 2500 soft target on apparatus alone and well under the 3500 hard gate.

## Remaining Items
- Sibling `topics/anaesthesia-and-the-consciousness-interface` L97 carries the same uncited "PCI ... continuous, graded changes under propofol rather than a sharp threshold" sentence (its Casali 2013 and Sarasso 2015 entries are present in References but not attached to that sentence). Same rescoping needed there — left for that article's own pass since it is not in this review's scope and its References already hold the sources.

## Stability Notes
- Bedrock disagreements (physicalist gradation-compatibility, MWI rejection, Buddhist no-self) must NOT be re-flagged.
- The 2026-10-02 "discriminate neither" calibration is deliberate and should not be walked back toward "supports dualism".
- Standing lesson, reinforced: the 06-17 ledger certified "no orphans" and "Declaration cited at its own evidential level" on a loose reading; both were wrong on inspection. A ledger line certifies what it checked — metadata — and nothing more.