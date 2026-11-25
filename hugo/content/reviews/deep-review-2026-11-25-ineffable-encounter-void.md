---
ai_contribution: 100
ai_generated_date: 2026-11-25
ai_modified: 2026-11-25 10:23:54+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-25
date: &id001 2026-11-25
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-25 10:23:54+00:00
modified: *id001
related_articles:
- '[[ineffable-encounter-void]]'
- '[[presence-type-and-absence-type-voids]]'
title: Deep Review - The Ineffable Encounter Void
topics: []
---

**Date**: 2026-11-25
**Article**: [The Ineffable Encounter Void](/voids/ineffable-encounter-void/)
**Previous review**: [2026-06-27](/reviews/deep-review-2026-06-27-ineffable-encounter-void/) (also 2026-05-31 and 2026-04-21; pessimistic review 2026-08-06)
**Review context**: The driver picked this page because voids are outside the selector's pool. Since 2026-11-16, every void page built from early-2026 research notes that got a full source pass has turned up critical quotation or source-reporting defects. This page merges two such pages, `archive/voids/numinous-void.md` and `archive/voids/resonance-void.md`, built from [research/voids-numinous-void-2026-04-12.md](/research/voids-numinous-void-2026-04-12/) and [research/voids-resonance-void-2026-03-24.md](/research/voids-resonance-void-2026-03-24/). The three earlier deep reviews called it converged, but they checked reference metadata, not wording, so that verdict was not treated as binding. Scope: every attributed quotation, and every attributed claim or paraphrase, checked against the source, plus the wording put in by the four repair commits since 06-27 (1b32406572 and 5bb477ca1a on 08-06, dceca644ac on 08-25, 73cbadd64b on 11-13, ab12b379d7 on 11-14).

## Sources Read This Pass

- **James 1902**: archive.org `varietiesofrelig03jame` (Longmans, Green 1902), djvu full text, whitespace and line-break hyphens collapsed before grepping. Project Gutenberg was down for maintenance.
- **Otto**: archive.org `in.ernet.dli.2015.166007`, Harvey translation, Oxford University Press / Humphrey Milford, 1928 impression ("revised with additions"), djvu full text, collapsed.
- **Harrison and Loui 2014**: PMC4107937 via `efetch db=pmc` (XML, tags stripped).
- **Keltner and Haidt 2003**: the published PDF (pp. 297–314) from the Haidt lab, retrieved through the Wayback Machine. Extraction is sound: "perceived vastness" has 5 hits, "Burke" 12.
- **Griffiths et al. 2006**: PubMed abstract (PMID 16826400), plus the full paper as archived by Johns Hopkins (Wayback, `hopkinsmedicine.org/Press_releases/2006/GriffithsPsilocybin.pdf`).
- **Granqvist et al. 2005** and **Beauregard and Paquette 2006**: PubMed abstracts (PMIDs 15849873 and 16872743), plus the PubMed record of Persinger and Koren's 2005 reply. The Beauregard recall design is confirmed by the 2006 press coverage (Nature News, Scientific American), not by the paper's methods section, which I did not read.
- **Taves 2008**: OpenAlex abstract (DOI 10.1016/j.religion.2008.01.005).
- **Rosa**: his 2018 *Global Dialogue* article "The Idea of Resonance as a Sociological Concept" (PDF), and the English Wikipedia blockquote citing the Polity 2019 translation. The book itself could not be reached (archive.org copy restricted; Google Books API quota exhausted).
- **Polanyi, Gendlin, Katz, Proudfoot**: archive.org copies are lending-only and search-inside returns 403, so only secondary sources were available (noted per entry below).

## Pessimistic Analysis Summary

### Critical Issues Found (9, all fixed)

1. **Otto, a word dropped inside quote marks.** Before: cannot be taught, "only evoked, awakened in the mind". The Harvey text (ch. II) reads "our X cannot, strictly speaking, be taught, it can only be evoked, awakened in the mind". After: cannot be taught: "it can only be evoked, awakened in the mind". **Seed**: [research/voids-resonance-void-2026-03-24.md](/research/voids-resonance-void-2026-03-24/) L59, which drops "be". The note's own L61 Quote field has the correct form.
2. **James's thesis misstated.** Before: "James makes ineffability the defining feature of mystical states". James (1902, pp. 380–81) calls ineffability "the handiest of the marks" and says ineffability and noetic quality together "will entitle any state to be called mystical". After: "James names ineffability and *noetic* quality as the two marks that 'entitle any state to be called mystical'". **Seed**: resonance note L79 ("the first and defining mark", sourced to a 1000-Word Philosophy summary).
3. **Gendlin, an unsupported strengthening.** Before: the felt sense is something "which premature articulation destroys (Gendlin, 1997)". No Gendlin text found says this. His method treats attention as what lets a felt sense form, and a word that does not fit fails to resonate with it. That is not destruction. The clause also sat awkwardly with the page's own Katz reply, which says dissolution under attention is "a nuisance for Gendlin's clinical method rather than a prediction of it". After: the clause is cut, and the strand keeps "whose content exceeds articulation". **Seed**: resonance note L145 ("attempting to verbalise it prematurely destroys it").
4. **Keltner and Haidt said to build on Otto, which is false.** Before: "Keltner and Haidt build on Otto explicitly, so the agreement between the two accounts is continuity rather than independent corroboration." "Otto" has 0 hits in the 2003 paper, and its reference list goes Ohman → Ortony → Piaget. After: "Keltner and Haidt do not cite Otto, but both draw on the same scriptural record, Paul's conversion among it, so their agreement is not independent corroboration." Keltner and Haidt work through Paul's conversion at length. Otto cites the "autobiographical testimony of the 'converted' from St. Paul onward". The anti-independence point the 08-06 repair wanted therefore survives on a true premise. **Seed**: no research-note line. **The 08-06 repair (1b32406572) installed it.** It replaced the archive's opposite error, "two independent methodologies converge" (`archive/voids/numinous-void.md` L65).
5. **Keltner and Haidt, a proposal stated as a finding, with its hedge dropped.** Before: "Contemporary psychology grounds this phenomenology empirically… the stimulus violates existing mental schemas and forces cognitive restructuring", followed by an uncited list of effects. The paper is a prototype proposal that its authors "derive … from a review of what has been written about awe". Its need for accommodation is "an inability to assimilate an experience into current mental structures", and they stress it "may or may not be satisfied". After: the proposal is framed as one, both phrases are quoted verbatim, and the effects claim is cut back to what Piff et al. (2015) report ("diminishment of the individual self", prosociality). The time-perception item had no citation and was dropped, as was the gloss "in ways the experiencer cannot fully explain". **Seed**: numinous note L71–73 (L72 "the mind must restructure its conceptual frameworks"; L73 "Recent research shows…", uncited).
6. **Harrison and Loui, a proposal stated as a finding, with emotion recast as cognition.** Before: "Neuroscience of frisson reveals that the body responds to resonant meaning before or alongside cognition… They argue it need not be downstream of a cognitive appraisal". The paper (PMC4107937) is an integrative review. It criticises studies "which assume that frissons are the effect of emotions, rather than part of their cause or an unrelated but simultaneous phenomenon". It is about emotion, not appraisal or cognition, and it is a critique, not a result. After: "Frisson research suggests the body may register resonant meaning alongside emotion rather than only after it… They question the assumption that frissons are simply 'the effect of emotions': they may be 'part of their cause or an unrelated but simultaneous phenomenon'." **Seeds**: resonance note L149 ("the body responds to meanings the mind hasn't yet processed") and L160 ("The body responds before or alongside cognition"). The phrase "downstream of a cognitive appraisal" came in with **the 08-06 repair 5bb477ca1a**, which correctly removed the two fabricated quotes.
7. **Granqvist et al. 2005, an overstated result.** Before: "effects predicted entirely by suggestibility". The abstract says suggestibility was measured through personality characteristics (absorption, signs of temporal-lobe lability, "new age" orientation), which "significantly predicted outcomes", so that suggestibility "may account for previously reported effects". After: "suggestibility-related personality traits rather than the fields predicted outcomes (Granqvist et al., 2005), a result Persinger disputed". The dispute is Persinger and Koren 2005, *Neurosci Lett* 380:346–7. The 08-06 pessimistic review named both gaps and neither repair acted on them. **Seed**: numinous note L100 ("predicted entirely by suggestibility and personality traits"). The live page also dropped the note's "and personality traits".
8. **Beauregard, a dropped condition.** Before: "Beauregard's fMRI studies of Carmelite nuns revealed distributed networks rather than a localised 'God spot', complicating any simple reductive account." There is one fMRI study (2006). The nuns were scanned while recalling, and by their report reliving, their most intense experience of union, because, they said, God cannot be summoned at will. Distributed activation counts against a single locus, not against reduction. After: the recall design is stated, the claim is narrowed to "a 'God spot'", and the page notes that the study imaged remembered union, which "the reflexivity argument above distinguishes from the state". That resolves the internal contradiction the 08-06 pessimistic review raised (Issue 4) and that no repair acted on. **Seed**: numinous note L107–109 and L176 (no recall condition; "distributed neural signature makes simple reductive explanations harder").
9. **The research note's synthesis credited to the traditions.** Before: "Their convergent finding: direct *approach* is possible, direct *evaluation* is not", presented as what apophatic theology, Zen and Advaita found. That sentence is the research note's own synthesis, with no source given. After: "On the Map's reading of their record, they converge on one point: …". The wikilink to `apophatic-cartography-four-criteria#cross-observer-convergence` is kept. **Seed**: numinous note L166.

### Medium Issues Found (all fixed)

- **Alston's relation to Swinburne reversed.** Before: Alston's model "strengthens this". The research note (L90) and the archive (L71) both say, correctly, that Alston's case is *more modest* than Swinburne's. The flip happened at the 04-17 coalesce/condense. After: "argues more modestly that".
- **A gloss credited to the apophatic authors.** Before: Pseudo-Dionysius, Eckhart and the *Cloud* "all insist that thought, conditioned by finite experience, domesticates the transcendent". "Conditioned by finite experience" is the research note's web gloss (numinous note L118, "conditioned by space, time, and finite experience"), not a rationale those authors give. After: "all hold that positive description falls short of the transcendent".
- **Internal link points at the wrong page.** Before: "catalogued as [dissolution under attention](/voids/compound-failure-signatures/)". That page tabulates eight signatures, and dissolution under attention is not among them. The signature is catalogued at `concepts/presence-type-and-absence-type-voids` § Dissolution Under Attention (L87) and in the taxonomy apex. After: the link is repointed there, and `compound-failure-signatures` stays in Further Reading.
- **Embodied cognition "confirms".** Changed to "holds". The programme is contested, and the next sentence already marks the comparative claim as conjecture.
- **Bidirectional coda.** "The self-undermining attention pattern suggests this channel…" now opens "On the dualist reading". The previous sentence ends on the physicalist reading, so an unlabelled "this channel" read as the Map's own claim. "On that reading" was tried and rejected, because it would have pointed back to the physicalist reading.

### Per-Cite Ledger (§2.4)

- James 1902 (*Varieties*): **real-correct** metadata. "states of insight into depths of truth unplumbed by the discursive intellect" and "a curious sense of authority for after-time" are **verbatim** (pp. 380–81). The paraphrase "the defining feature" was **wrong** (critical 2, fixed).
- Otto 1917/1923 (*Idea of the Holy*, trans. Harvey, OUP): **real-correct**. "wholly other" verbatim (41 hits). "only evoked…" had a **dropped word** (critical 1, fixed). Ch. II says the numinous state of mind is "perfectly sui generis and irreducible to any other". "Genuine cognition" matches Otto's "they must certainly be termed cognitions, modes of knowing" in the divination chapter. The composite *mysterium tremendum et fascinans* is not a string in the Harvey text: Otto writes "mysterium tremendum" and adds that it "at the same time exercises a supreme 'fascination'". It is a conventional scholarly label, italicised and not quoted, so it is kept. Genealogy: Otto quotes *Varieties* (p. 58) and says "James is debarred by his empiricist and pragmatist stand-point", so "Otto read *Varieties* and drew on it directly while rejecting James's empirical method" is **real-correct**. Note: the translator's preface sentence praising James's "famous Gifford lectures … published just over twenty years ago" is Harvey's, not Otto's.
- Gendlin 1997 (*Experiencing and the Creation of Meaning*, Northwestern UP): metadata **real-correct**. Paraphrase **unsupported** (critical 3, fixed). Open: the 1962/1997 book's central term is "felt meaning"; whether it uses "felt sense" was not checked at the text.
- Polanyi 1966 (*The Tacit Dimension*, Doubleday): **real-correct** metadata. "we can know more than we can tell" is attested at p. 4 by several secondary sources. The book was not reached.
- Rosa 2016/2019 (*Resonance*, Polity): metadata **real-correct**. "is not an echo, but a responsive relationship, requiring that both sides speak with their own voice" appears verbatim in Wikipedia's blockquote citing the Polity translation (no page). The book was not reached, so this is **unverified verbatim at the book** (the 08-06 review's "verbatim" gives no route). The non-manufacturability point is confirmed in Rosa's own words in the 2018 *Global Dialogue* piece: "We can never simply establish resonance instrumentally or bring it about at will".
- Harrison and Loui 2014 (*Front. Psychol.* 5:790): **real-correct** metadata. "strongly correlated to the onset of musical frisson" verbatim. "a dualist view (Becker, 2004, p. 6) wherein the body is subordinate to the mind" and "implicit mind–body hierarchy" verbatim. Characterisation **wrong** (critical 6, fixed). Result-direction: a theoretical review, not an experiment.
- Keltner and Haidt 2003 (*Cogn. Emot.* 17(2):297–314): **real-correct** metadata. "perceived vastness", "need for accommodation", "an inability to assimilate an experience into current mental structures" and "may or may not be satisfied" all verbatim. Otto claim **false** (critical 4). Framing **wrong** (critical 5). Both fixed.
- Piff et al. 2015 (*JPSP* 108(6):883–899): **added**. Metadata checked at OpenAlex. Its abstract reports awe producing "a diminishment of the individual self" and increased prosocial behaviour, in that direction. Keltner is a co-author.
- Swinburne 2004 (*The Existence of God*, 2nd ed., OUP) and Alston 1991 (*Perceiving God*, Cornell): **real-correct** metadata. Standard paraphrases. Alston's relation to Swinburne fixed (medium).
- Granqvist et al. 2005 (*Neurosci Lett* 379(1):1–6): **real-correct** metadata. Result **overstated** (critical 7, fixed). Direction: null for the fields, positive for the personality predictors.
- Beauregard and Paquette 2006 (*Neurosci Lett* 405(3):186–190): **real-correct** metadata. Condition **dropped** (critical 8, fixed).
- Katz 1978 (in *Mysticism and Philosophical Analysis*, OUP): **real-correct** metadata. The paraphrase "no unmediated experiences" matches "There are NO pure (i.e. unmediated) experiences" (p. 26), as attested by two secondary sources. The book was not reached.
- Proudfoot 1985 (*Religious Experience*, UC Press): **real-correct** metadata. The paraphrase fits the book's structure ("Ineffability" in ch. 4; "Protective Strategies" in the Explanation chapter, per its table of contents and the 1987 *Thought* review). Not checked at page.
- Griffiths et al. 2006 (*Psychopharmacology* 187(3):268–283): **real-correct**. The conclusion quote is **verbatim** (abstract). Double-blind, methylphenidate comparison, volunteers "reporting regular participation in religious or spiritual activities", and questionnaires "immediately after and 2 months after sessions" are all confirmed. The Stace claim is confirmed in the full text: the Pahnke–Richards questionnaire "is based on the classic descriptive work … by Stace (1960)", and the Mysticism Scale's factors correspond to "dimensions described by Stace (1960)".
- Taves 2008 (*Religion* 38(2):125–140): **real-correct**. "Something like [ascriptions of qualities] may take place below the threshold of consciousness" and "experiences … that subjects experience as inherently religious" match the page's paraphrase. The abstract also cites Proudfoot and Shaver 1975 as the attributional ancestor, which supports "develops his attributional line".
- Taves 2009 (*Religious Experience Reconsidered*, Princeton): metadata **real-correct**. "Generic building blocks allow cross-cultural agreement without shared vocabulary" is a Map reconstruction of the building-block approach, not a quoted thesis, and is low-risk.
- Merleau-Ponty, "motor intentionality": the term is his. No reference entry, as before.
- Map self-references (Silence Void, Surplus Void, Apophatic Cartography): **removed**. They were never cited inline as references, and all three pages remain wikilinked in the body and in Further Reading.
- Inline cites and References agree both ways after the edits (17 entries).
- No superlative claims (helper not needed; none present).

### Cited-Author Stance (§2.4 item 8)

Harrison and Loui criticise a dualist view, and the page says so. Keltner and Haidt treat awe as a natural emotion. Granqvist is a naturalist. Beauregard is a non-materialist, though the page uses only his imaging result. Katz, Proudfoot and Taves are constructivists or attributionists, presented as rivals. No author is presented as endorsing the Map's conclusion.

### Reasoning-Mode Classification (editor-internal)

- Katz: Mode One attempted (constructivism's own prediction; two features said to resist tradition-sourcing), with the residue stated as smaller.
- Proudfoot and Taves: Mode Three, honestly marked as unanswered ("Neither surviving feature has been shown to resist her account").
- Naturalist neural-correlates reply: Mode Three ("Neither side lands a decisive blow", stalemate symmetric).

No label leakage.

### Counterarguments Considered

- Heterophenomenology and the confabulation reading of evaluator dissolution: bedrock, deferred to `presence-type-and-absence-type-voids` per prior stability notes.
- The MWI indexical reply: already conceded in the coda. Not re-flagged.

## Optimistic Analysis Summary

### Strengths Preserved

- The two-register, one-axis structure, and the presence-type framing in paragraph two.
- The 08-06 regrouping of sources into two strands plus one narrow source, and the Katz reply on the two features that resist tradition-sourcing.
- The Otto→James genealogy, which is now verified at the text.
- The Griffiths falsifier-3 audit (11-13) and the Stace sentence (11-14), both verified at source.
- The symmetric stalemate sentence, and the Dualism coda's "the tenet does the work rather than the evidence".

### Enhancements Made

- Piff et al. (2015) now supports the awe-effects claim that was uncited.
- Persinger's reply is named, so the reader no longer gets a cleaner kill than the record supports.
- The Beauregard recall design is used as a point *for* the reflexivity argument, as the 08-06 pessimistic review suggested.

### Tenet Section against [P-V1](/positions/voids-as-evidence/#p-v1)–[P-V3](/positions/voids-as-evidence/#p-v3)

The page claims no cumulative weight. It reads the recurrence as genealogical, not independent, which is the [P-V1](/positions/voids-as-evidence/#p-v1) lineage variant. The Dualism and Bidirectional codas say the tenet does the work and the practices illustrate rather than evidence it, which is [P-V2](/positions/voids-as-evidence/#p-v2). Tenet 5 is held symmetric. No change was needed beyond the Bidirectional label.

## Length

`analyze_length`: **2984 → 2983** (voids hard 3000, gate `>=`). The corrections and the Piff entry (about +80) were paid for by:

- cutting the three Map self-reference entries (about −34);
- cutting the falsifier-2 restatement, which repeated the result recorded twice above (−22), and "with the result recorded above" (−5);
- dropping nine Further Reading entries that duplicate body wikilinks and stay in `related_articles` (−18; `compound-failure-signatures` was kept after the link repoint);
- trimming the apophatic gloss (−5) and the uncited "in ways the experiencer cannot fully explain".

No calibration qualifier and no rival's reply was cut. A rival's reply was added (Persinger).

## Remaining Items

- Archived predecessors carry the same defective strings (tasks minted). `archive/voids/resonance-void.md`: L61 (Gendlin "premature articulation destroys"; plus an unverified Gendlin quote), L63 (Otto "only evoked"; Otto's "modes of knowing … intuitive outcome of feeling", verbatim but about divinatory intuitions, applied to the numinous at large), L69 (James "defining feature"), L79 ("reveals … before or alongside cognition"; "downstream of a cognitive appraisal"). `archive/voids/numinous-void.md`: L61 ("empirical grounding"; "forces cognitive restructuring"), L63 (uncited effects), L65 ("two independent methodologies converge"; Keltner and Haidt called "a contemporary research programme using fMRI"), L73 (Granqvist "entirely"; Beauregard without the recall design), L79 (traditions' "convergent finding"), L81 ("inevitably domesticates"), L45 ("structural, not temporary — it persists regardless of future advances", a calibration over-claim).
- Research notes need dated Correction lines (task minted): resonance note L59, L79, L145, L149/L160; numinous note L56 (an Otto "quote" ending "utterly abashed": 0 hits in Harvey, a Wikipedia-style gloss), L71–73, L100, L107–109/L176, L108 (a Beauregard quote from press coverage, unverified), L118, L166. Resonance note L50: the Gendlin quote is unverified.
- Out of scope, not tasked: `concepts/presence-type-and-absence-type-voids` L137 describes `compound-failure-signatures` as "the failure-signature framework that includes dissolution under attention". Its own L89 says that framework tabulates eight signatures, with dissolution supplied by the taxonomy apex.
- Unverified at the primary text (book access unavailable): the Rosa sentence; Polanyi p. 4; Katz p. 26; Proudfoot's ineffability chapter; Gendlin's terminology in the 1962/1997 book.

## Stability Notes

- The earlier "converged" verdicts (04-21, 05-31, 06-27) rested on metadata checks. This pass is the first with every attributed string checked at source. Future reviews should treat the ledger above as the baseline and re-check only lines edited after 2026-11-25.
- Do not restore "Keltner and Haidt build on Otto". The paper does not cite him. The shared-scriptural-record wording carries the anti-independence point.
- Do not restore the "premature articulation destroys" clause to Gendlin without a page-cited Gendlin passage.
- Carry-forward bedrock notes from 06-27 still apply: heterophenomenology stays deferred; do not split the two registers; keep the presence-type framing. The convergence and stalemate sections should not be "strengthened".
- At 2983 words against a hard limit of 3000, any future addition must be strictly length-neutral.