---
title: "Deep Review - Immunity to Error through Misidentification"
created: 2026-10-04
modified: 2026-10-04
human_modified: null
ai_modified: 2026-10-04T12:01:23+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-04
last_curated: null
---

**Date**: 2026-10-04
**Article**: [[immunity-to-error-through-misidentification|Immunity to Error through Misidentification]]
**Previous review**: Never (article created 2026-10-04 10:13Z by expand-topic, commit ccbcc7b147)
**Word count** (`analyze_length`, includes the reference list): 2,877 → 2,925 (+48; concepts soft 2,500 / hard 3,500, gate `>=`; status soft_warning, length-neutral mode, budget ~3,100)

## Method

Every quoted span of 25+ characters was checked against a raw source fetched this session, not against the research note: archive.org OCR full text (Wittgenstein *Blue Book*; Strawson *Bounds of Sense*; Anscombe *Collected Papers* vol. 2), the Cambridge Core HTML of Child 2026, the live SEP entry and both supplements, OpenAlex and Semantic Scholar abstract text, Crossref metadata, and Google Books search-within on Shoemaker's *Identity, Cause, and Mind* (id `VrbWAAAAMAAJ`; positive control "Self-reference and self-awareness" hit pp. 6 and 15). WebSearch was exhausted for the session, so the session used only direct fetches.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Subject splice, Strawson 1966 p. 166 (L83).** The article had "Kant's insight, he adds, 'explains why that notion, so used, is really quite empty of content'". In Strawson the subject of "explains" is "the key fact, that immediate self-ascription of thoughts and experiences involves no application of criteria of subject-identity"; Kant "sees clearly how" that fact explains it. The predicate was verbatim and the subject was wrong. The error came from the research note. **Fixed:** "Kant, he adds, 'sees clearly' how that fact 'explains why that notion, so used, is really quite empty of content' (p. 166)."
2. **SEP overstatement, wh-IEM (L45).** The article had "Since Pryor, the Stanford Encyclopedia reports, immunity to wh-misidentification has been treated as the more fundamental notion". The SEP says wh-IEM "might legitimately be considered the more fundamental notion (as it is by Pryor 1999)". A hedged, one-author claim had become a field trend. **Fixed:** the SEP's own modal is quoted and the view is attributed to Pryor.
3. **Constructed disagreement, Strawson vs Shoemaker on memory (L43).** "So the two disagree over whether the immunity reaches across time" is in neither source. Shoemaker grants memory *de facto* immunity, so for him the immunity does reach across time. The documented dispute is Shoemaker vs Evans (García-Carpintero 2024 abstract: "Shoemaker argued that memory judgments ... are not strictly speaking IEM; Gareth Evans disputed this"). **Fixed:** Strawson's "directly remembered" scope stays as a fact, and the dispute is now attributed to Evans through the abstract.
4. **Unsourced superlative, twice.** The lead had "the most discussed counterexample" and L53 had "The most discussed is thought insertion". No source read says this, and the SEP lists thought insertion as one of five actual cases. **Fixed:** "a much-discussed counterexample" and "This article takes up thought insertion".

### Medium Issues Found

- **Source label, Coliva 2002.** Semantic Scholar's "abstract" is the paper's opening paragraph (it carries footnote marker 1 and announces the paper's sections). "Abstract" → "opening paragraph" at L55, at L57 and in References. "Coliva concludes" → "Coliva argues", because the paragraph announces a thesis.
- **SEP counterexample list (L53).** The SEP gives the five cases as the *actual* cases, as distinct from thought-experiment ones. "Lists the proposed counterexamples" → "lists the actual cases proposed as counterexamples".
- **SEP on imagined cases (L57).** "The harder challenges are imagined cases" ranked cases the SEP does not rank. The SEP's actual contrast is that only the fantasy cases would involve implicit self-identification, and whether they do "depends at least in part on the conditions of de re ... thought". Rewritten to that.
- **García-Carpintero paraphrase (L59).** "Since the answer varies with the kind of thought at issue" goes beyond the abstract, which says only that "specific types of thoughts [should be] countenanced". Rewritten to "in favour of specific types of thought".
- **Wiseman 2019 (L39).** "Reads it as a warning against the distinction" → "finds no immunity thesis in it". The abstract (OpenAlex) says "Wittgenstein's work does not contain the thesis, nor any version of the thesis". The reference annotation is now "(Abstract.)" in place of "(Position via Child 2026.)".
- **Anscombe's "endless" (L77).** Dropped qualifier: she calls the dispute "self-perpetuating, endless, irresoluble, so long as we adhere to the initial assumption ... that 'I' is a referring expression". Restored as "so long as 'I' is assumed to refer".
- **Child fidelity (L71, L93).** "Where the subject is plainly a body" → "plainly an embodied person". Child's words are "an embodied human being" and "a human person".
- **Gallagher 2000 reference.** The subtitle was missing. Crossref subtitle: "A cognitive model of immunity to error through misidentification". Added.
- **Smith 2024 reference.** The Evans reconstruction (L47, L79) comes from the SEP supplement "Evans on First-Person Thought", which the reference did not name. Both supplements are now named in full.

### Low Issues (noted, not changed)

- Strawson's Kant credit (L83) drops his hedge "(I think it could be said, without serious exaggeration, that ...)". The quoted fragment is verbatim, and the hedge does not change what is claimed. Left as is.
- L45's ("that person is me") is an example identity content, not a quotation of Pryor. Pryor is otherwise paraphrased only.

### Publisher-of-Record Citation Ledger

- Anscombe 1975/1981 ("The First Person") — state: real-correct. The reprint is *Collected Papers* vol. 2 pp. 21–36: the index has "Guttenplan 21n", and the source note is on the first page. All seven quoted spans were grep-verified in OCR. "Thus we discover ...", "Nothing but a Cartesian Ego will serve. Or, rather, a stretch of one" and "ten thinkers thinking in unison" are on p. 31 (no running head; placed by position before the p. 32 head). "Getting hold of the wrong object ...", "Others in effect treat selves as postulated objects ...", "endless" and "'I' is neither a name ..." fall between the p. 32 head and the "The First Person 33" head, so the pp. 30–32 range holds. The Guttenplan pp. 45–65 range was not independently fetched.
- Campbell 1999 — state: real-correct (Crossref: *Monist* 82(4), 609–625). The quoted claim is verbatim in Coliva's opening paragraph.
- Child 2026 — state: real-correct (Crossref: *Philosophy*, online 2 Oct 2026, pp. 1–23, DOI as given). All three quotes were grep-verified in the Cambridge Core HTML. Both passages sit in §3, "Three interpretative issues".
- Coliva 2002 — state: real-correct metadata (Crossref: *PPP* 9(1), 27–34). Both quotes verified; source label corrected to "opening paragraph".
- Evans 1982 — not quoted. "Here" vs "this", identification-free channels, reference failure (§5.4 and §7.6) and the answer to Anscombe's sensory-deprivation argument were all verified in the SEP supplement "Evans on First-Person Thought".
- Gallagher 2000 — state: real-wrong-metadata (subtitle missing; corrected). His stance, that he resists the counterexample, rests on the SEP listing him "for critical discussion" of the actual cases and on the subtitle. The chapter was not read in full, and the reference says so.
- García-Carpintero 2024 — state: real-correct (online 9 May 2024; vol. 38(3) is the 2025 issue, pp. 1201–1224; clarified in References). Both abstract quotes verified (OpenAlex).
- Kant 1998 — state: real-correct (standard edition). A352–353 is used only in the section labelled as the Map's reconstruction, matching the Kant page.
- Lane & Liang 2011 — state: real-correct (Crossref: *J. Phil.* 108(2), 78–99). Both abstract quotes verified verbatim (OpenAlex).
- Longuenesse 2017 — state: real-correct. Chapter 5 is "Kant on 'I' and the Soul", pp. 102–139: the Crossref chapter record gives the title and pages, and Google Books p. 102 reads "5. Kant on 'I' and the Soul". The abstract quote was verified verbatim (OpenAlex).
- Pryor 1999 — state: real-correct (Crossref: *Phil. Topics* 26(1), 271–304). Paraphrase only. The SEP confirms that Pryor treats wh-IEM as the more fundamental notion.
- Shoemaker 1968 — state: real-correct (Crossref: *J. Phil.* 65(19), first page 555; reprint pp. 6–18 per the Crossref chapter record). The p. 8 sentence, "absolute" / "circumstantial" (p. 8) and "is not due to my having identified as myself something" (p. 9) were verified as Google Books [S] snippets. For p. 15, "does not involve what I have called" and "presented to oneself as an object" both hit p. 15, but the snippets do not show them joined: **partial**.
- Shoemaker 1970 — state: real-correct (reprint pp. 19–48 per Crossref). "De facto immunity to error through misidentification" on p. 46 was verified [S]. "Quasi-remembering, as I shall use the term" hits p. 24, so guard (b)'s TERM claim holds. The APQ 7(4) 269–285 range was not fetched (JSTOR challenge).
- Smith 2024 (SEP "Self-Consciousness", Joel Smith; first published 13 July 2017, substantive revision 14 June 2024) — state: real-correct. All five quotes were grep-verified in the live entry and supplements. Fidelity defects (wh-IEM, the actual-cases list, the fantasy cases) are fixed above.
- Strawson 1966 — state: real-correct. Every quote was grep-verified in the OCR: "the fact that lies at the root of the Cartesian illusion" spans the page break at pp. 164–165; "no use whatever ...", "are not in practice severed", "directly remembered" and the Kant credit are on p. 165; "the illusion of a purely inner and yet subject-referring use for 'I'", "an object of singular purity and simplicity ..." and "explains why that notion ..." are on p. 166. The subject splice is fixed above.
- Wiseman 2019 — state: real-correct (Crossref: *J. Phil.* 116(12), 663–677). Her position is now taken from the abstract.
- Wittgenstein 1958 — state: real-correct. The four quotes were verified in the OCR against running heads: p. 66 (two cases), p. 67 (broken arm; "would be nonsensical"), p. 69 ("this creates the illusion ...").
- Map self-citations — "no independent evidence discriminates" is at `positions/individuation-and-subjecthood` L53, and "is stated unconditionally but argued conditionally" is P-I2's heading (L62). Both verbatim.

**Result-direction leg.** Lane & Liang: IEM is contingent and sometimes fails (the article reports the dissent correctly). Coliva: thought insertion is not a counterexample. SEP: "none obviously challenge". Child: identification-freedom where the subject is embodied. All are reported in the direction their sources give. No numerical claims.

**Cited-author-stance leg.** Wittgenstein and Strawson diagnose a Cartesian *illusion*. Anscombe holds in the same paper that "Self-knowledge is knowledge of the object that one is, of the human animal that one is" (OCR, p. 35). Child: a human person. Evans rejects Anscombe's no-reference claim. Longuenesse: the first-person standpoint gives no knowledge of what kind of entity we are. Lane & Liang argue from pathology and experimental illusions. None is presented as endorsing the Map. L77 places the Map's posit among positions in Anscombe's "endless" dispute, which is the reverse of an endorsement.

**Superlative / currency sweep.** `find_superlative_claims` returned nothing. A manual pass found and fixed "most discussed" (×2), "Three readings dominate" (→ "recur"), "the three main readings" (→ "the three readings") and "the strongest case" (scoped; see Calibration).

### Attribution guards (a)–(i)

- (a) PASS. Shoemaker 1968 is cited at pp. 8, 9, 15 and 1970 at p. 46, by reprint pagination; References give the journal pages and the reprint ranges.
- (b) PASS. The text says "Shoemaker's quasi-memory", with no "coined". Quasi-memory gets exactly two sentences (L43, L97), and still does after the edit.
- (c) PASS. The pp. 30–32 range is cited, and the OCR confirms the quotes fall on pp. 31–32.
- (d) PASS. "On the standard reading the passage states the immunity thesis."
- (e) PASS. Child is cited by section (§3), and §3 is verified.
- (f) PASS, vacuously. Coliva 2006 is not cited ("logically IEM" is Coliva 2002, verified).
- (g) PASS. No "no dualist" (grep 0).
- (h) PASS. No "resists physicalist" or "physicalist reduction" (grep 0).
- (i) PASS. Zahavi & Kriegel are omitted; Zahavi appears only as editor of Gallagher's volume.
- Also: nothing is quoted from Evans (only the bare words "here", "this", "I" are mentioned). Pryor is paraphrased. The [A] works are attributed as abstracts. Campbell appears only through Coliva.

### Calibration (Lens 3)

- The lead's "IEM is no evidence that the subject is non-physical" stands. One later sentence leaned against it: L75, "This horn is the strongest case for reading IEM as support for a Cartesian subject", which ranks against a field the research note could not survey (guard g's sibling). It is now scoped: "the closest any of the three readings comes to treating IEM as support". The adjoining "a stretch of one" ceiling is kept.
- L61 asserted the ownership/self-identification separation outright, two paragraphs after "The debate is open". It is now conditional: "If the self/other reply is right, the case shows a separation."
- RSP Tenet 5: "stops ... from settling" → "denies that ... settles". The tenet weakens an economy argument; it does not block one.
- RSP Tenet 4: "on independent grounds" restored to the P-I1 would-shift clause (verbatim at register L57). The P-I2 dependency is already conceded, so no new concession is made.
- RSP Tenet 3: "No bearing" is kept. There is no universal causal-efficacy claim, and the actual-vs-capacity quantifier is untouched.
- Tenet 1: "its case for irreducibility does not rest on first-person reference" was checked against `tenets.md` L55, whose rationale is the explanatory gap. It holds.
- The bi-aspectual "aspects vs persisting subject" tension is not touched; it stays open.
- §(4), the three exposures, is labelled at L89: "From here the mapping is the Map's own reconstruction; none of the authors above discusses the Map."
- Genealogy transition check (L69, "IEM explains why the Cartesian picture ... tempts us, and so cannot confirm it"). Label: *documented textual claim* (Wittgenstein, Strawson) carried as exposition of the first reading. "Origin ⇒ validity" is not invoked. The conclusion concerns the evidential force of the *temptation*, and its separate premise is named: every reading predicts IEM, and Child's crossed-legs control shows identification-freedom where the subject is embodied. PASS.

### Counterarguments Considered

- **Eliminative materialist / Dennett.** IEM is a fact about a self-model's indexing, and the article's verdict already concedes it gives the posit no support. No in-framework reply is owed. The article claims nothing a physicalist must reject.
- **Lane & Liang (empirical dissent).** Reported at full strength, from their own abstract, and the verdict is "open". The SEP's self/other reply is reported as the SEP's.
- **Nagarjuna.** No referent for "I" is close to Anscombe's horn, which the article states. No change.
- **Popper's ghost.** The article's one evidential claim is negative (IEM discriminates nothing), and the article does not test it. That fits a concepts page.
- **Tegmark, Deutsch.** No quantum or Many-Worlds content beyond the Tenet 4 deflation, which is conceded as conditional.

## Optimistic Analysis Summary

### Strengths Preserved
- The verdict-first lead, with the compatible / no support / defeater-for-one-inference triple stated in the first two paragraphs.
- Child's crossed-legs control case, the article's most distinctive and best-sourced move.
- Anscombe's "a stretch of one" as the ceiling of the Cartesian horn, and "ten thinkers thinking in unison" mapped onto A352–353.
- Per-reference access annotations: (Abstract.), (Paraphrased.), (Not quoted; content via ...). These let a reader see how far each source was read.
- An explicit label separating the source exposition from the Map's reconstruction.

### Enhancements Made
- Five fidelity corrections that bring quoted and paraphrased sources into line with the raw text (Critical 1–3, Medium).
- Four calibration tightenings (Calibration above).
- Three reference corrections (Gallagher subtitle; García-Carpintero issue year; SEP supplements named) and two annotation corrections (Coliva, Wiseman).

### Cross-links Added
- None. The article already links every relevant neighbour and is in length-neutral mode.

## Integration Seams (Lens 4; verdicts only, no edits to other pages)

- **topics/kants-paralogisms-and-the-maps-subject L82.** "No use whatever of any criteria of personal identity is required" (p. 165) and "the fact that lies at the root of the Cartesian illusion" (pp. 164–165) are both verbatim in the OCR. The subject is correct: in Strawson, "the fact" is criterionless self-ascription. The citation spans the right pages. "A current experience" narrows Strawson's "current or directly remembered state", which is acceptable outside quotation marks. "What later work calls immunity to error through misidentification" is accurate, since Shoemaker 1968 postdates the 1966 book. **PASS.**
- **concepts/thought-insertion, the new paragraph at L102.** The SEP's other-misidentification reading and "obviously challenge" are both verified in the supplement. "The verdict is disputed" is accurate. "It holds on Billon's reading as much as on the universalists'" is best read as "neither reading contradicts it", and that holds, since on neither does the patient self-ascribe the thought. The conclusion ("cannot decide whether the asymmetry is phenomenal") is correctly calibrated. Smith 2024 is the right entry and author (Joel Smith, SEP "Self-Consciousness", revised 14 June 2024). The quoted phrase comes from the supplement, which the reference URL does not separately name; that is minor. **PASS.**
- **topics/consciousness-and-the-ownership-problem.** The L84 caveat ("Taken alone, though, that omission is no evidence that ownership is non-physical ...; Child 2026") is calibrated. Child supplies the bodily identification-free case, and the step to "an impersonal description would omit 'whose'" is the page's own inference, not attributed to Child. **PASS.** The L126 reword ("omit who experiences what, an omission first-person reference predicts on any metaphysics. On the Map's reading, ownership is part of what makes consciousness irreducible") no longer infers non-physicality from the omission, and the remaining claim is labelled as the Map's reading. **PASS.** The Child 2026 reference entry matches Crossref (title, *Philosophy*, First View, pp. 1–23, DOI). **PASS.**
- **concepts/indexical-knowledge-and-identity L112.** **DEFECT (dropped qualifier).** "First-person self-ascription uses no such criteria at all, which is why it enjoys immunity to error through misidentification" makes a universal claim that IEM itself denies. IEM is relative to grounds: self-ascriptions made on observation or testimony use criteria and can misidentify (Wittgenstein's "use as object"; SEP §2.3). It also contradicts this article's lead ("some first-person judgements ... relative to the grounds"). The second clause ("since every account of the first person predicts that immunity, it cannot by itself answer the prior question") is correctly calibrated. Confirmed live in both trees (grep -c = 1). `git log -S` shows it was introduced by ccbcc7b147 and never repaired. **Minted** a P2 refine-draft (word-neutral: "First-person" → "Introspective").
- **Zero-word piped links** (mine-ness, self-and-self-consciousness, self-opacity, vertiginous-question, self-reference-paradox): all read. Each is a link on existing text with no new claim. **PASS.**

## Remaining Items

- P2 refine-draft minted for `concepts/indexical-knowledge-and-identity` L112 (above).
- Not independently fetched this pass: the Guttenplan 1975 page range (45–65), the APQ 1970 page range (269–285), and the contiguous join of Shoemaker's p. 15 quotation. All are consistent with the research note and standard bibliographies. A future pass with a working JSTOR or Google Books session can close them.

## Stability Notes

- The verdict (compatible, no support, defeater for one inference) is the Map's settled calibration for IEM. Future reviews should not upgrade it toward support for a non-physical subject, and should not read the Tenet 5 sentence as defeater-removal: IEM removes no defeater.
- Physicalist and Buddhist personas will always find the posit idle here. The article already concedes the posit gets no support, so this is not a defect.
- The thought-insertion verdict is "open" by design. Do not re-flag it in either direction unless new literature (beyond Lane & Liang 2011 and García-Carpintero 2024) is brought.
- Quasi-memory is capped at two sentences because the quasi-memory article owns the topic. Do not expand it here.
