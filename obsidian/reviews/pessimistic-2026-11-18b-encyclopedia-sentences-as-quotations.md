---
title: "Pessimistic Review - 2026-11-18b - Encyclopedia Sentences as Quotations"
created: 2026-11-18
modified: 2026-11-18
human_modified: null
ai_modified: 2026-11-18T23:05:49+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-fable-5-2
ai_generated_date: 2026-11-18
last_curated: null
---

# Pessimistic Review

**Date**: 2026-11-18
**Content reviewed**: every page in `topics/`, `concepts/`, `apex/` and `voids/` (911 pages), on one question: how many quotations are an encyclopedia author's sentence set in quotation marks under a philosopher's name?

## Executive Summary

The defect is real but rare in the form this method can see. Of 5,301 quotations of eight words or more, 334 share an eight-word run with one of 150 fetched encyclopedia entries; 190 of those are demonstrably the encyclopedist's own prose, and 181 of the 190 (95%) are credited to the entry or its author. Five are credited to a philosopher instead (two on topics pages, one on a concept page, two on void pages, none on apex pages), and a looser seven-word pass adds two more on the same pages. This is a lower bound: 2,724 quotations sit on pages that cite no encyclopedia anywhere, only 150 of 496 candidate entries were fetched, and a reworded or short quotation escapes an exact-match test.

Two of the five had been "verified" by earlier deep reviews. One review restored the encyclopedia sentence verbatim under Zahavi's name after checking it against the encyclopedia; the other recorded a primary-text match for van Inwagen that the primary text does not contain (0 hits in the full paper).

## Method and Control

1. **Population.** For each page, every double-quoted string of at least eight words in the body, plus markdown block quotations, skipping frontmatter, code and reference sections. Each page's encyclopedia links (SEP, IEP, Wikipedia) were collected, plus those of its research notes. A note was mapped to a page when the page wikilinks it or when the note's filename minus its date (and minus a `voids-` prefix) equals the page slug.
2. **Fetch.** 150 entries from the official sites, one request each with a two-second pause: the 110 SEP, 25 IEP and 15 Wikipedia entries with the most long quotations on the pages and notes citing them. SEP bibliographies and IEP reference lists were cut before matching so that titles could not match.
3. **Match.** Text was normalised (case, quotes, apostrophes, non-breaking spaces, accents, punctuation), each quotation split at ellipses and bracketed insertions, and every eight-word window tested against every fetched entry. Each hit was labelled by whether the matched text in the entry lies inside quotation marks or a block quotation (the entry quoting someone) or in the entry's own prose.
4. **Reading.** Every prose hit was read against the page's sentence to decide the attribution: 156 rows carried an entry or entry-author cue and were skimmed; 77 carried none and were read in full context.

**Control result.** Run on the pre-fix versions of this week's known cases:

| Known case | Pre-fix commit | Result |
|---|---|---|
| `voids/transformative-experience-void`, definition of "epistemically transformative" | 39038241ea | Flagged, 12 of 12 words, entry prose (Chan, SEP, first published 1 June 2023). The pre-fix sentence carried a parenthetical "(Stanford Encyclopedia of Philosophy)", so on a strict reading it was credited to the entry while defining Paul's term in the entry's words. |
| `voids/origin-of-consciousness`, Chalmers "stark choice" | 593f95433d | Flagged, 18 of 24 words, entry prose (Weisberg, IEP), credited to Chalmers. This is the clean positive control. |
| `voids/origin-of-consciousness`, Chalmers "irreducible to lower-level physical facts" | 593f95433d | Not flagged. Its source, Wikipedia "Panpsychism", fell outside the 150-entry cap. |
| `voids/embodiment-cognitive-limits`, "I can" before "I know" | ec72afc990 | Not testable. The quotation is shorter than eight words and was reworded. |
| `voids/nomic-void`, Chalmers "probably not naturally possible" | 7af293b4f6 | Not flagged, correctly: the wording is Chalmers's own and the defect was the cited work. |

The method flags both known cases it could have flagged, and the two it missed show its two blind spots (entries outside the cap, and short or reworded quotations). No change to the method was needed after the control.

## Population and Fetch Counts

| | topics | concepts | apex | voids | total |
|---|---|---|---|---|---|
| Pages scanned | 370 | 371 | 45 | 125 | 911 |
| Pages with at least one long quotation | 309 | 300 | 37 | 110 | 756 |
| Long quotations | 2,202 | 2,117 | 181 | 801 | 5,301 |
| Pages with a fetched entry (via page or note) | 98 | 117 | 1 | 57 | 273 |
| Quotations tested (on those pages) | 841 | 1,024 | 5 | 446 | 2,316 |
| Untestable: page and note cite entries, none fetched | 123 | 102 | 0 | 36 | 261 |
| Untestable: page and note cite no encyclopedia | 1,238 | 991 | 176 | 319 | 2,724 |

- Distinct entries cited by pages: 160 (142 SEP, 17 IEP, 1 Wikipedia), on 167 pages.
- Distinct entries cited by mapped research notes: 459 (202 SEP, 188 Wikipedia, 69 IEP); 448 of 911 pages have a mapped note.
- Candidate entries (page or mapped note): 496. Across all 773 research notes: 700; union with pages: 715.
- Fetched: 150 of 496 (30%). Unobtained: 0.
- All 5,301 quotations were also run against all 150 entries regardless of citation. This second pass is how the most prominent hit was found: [[mine-ness]] cites no encyclopedia at all.

## Rates

**Hits.** 383 quotation-entry pairs; 334 distinct quotations.

| Class | Count |
|---|---|
| PRIMARY-IN-ENCYCLOPEDIA (entry is itself quoting) | 119 |
| of which OK-SECONDARY (page credits the entry or "as quoted") | 28 |
| of which LOCATED (page gives a page, section or work locator) | 32 |
| of which UNLOCATED (primary work named, no locator) | 59 |
| ENCYCLOPEDIA-AUTHOR'S prose, ATTRIBUTED-TO-ENTRY | 181 |
| ENCYCLOPEDIA-AUTHOR'S prose, **ATTRIBUTED-TO-PHILOSOPHER** | **5** |
| ENCYCLOPEDIA-AUTHOR'S prose, UNATTRIBUTED | 4 |
| Not from the entry (stock phrase, coincidental run, or primary wording the entry displays without marks) | 25 |

The three PRIMARY sub-classes were assigned by pattern, not by reading, and 39 of the 59 UNLOCATED hits matched an entry the page does not cite (famous lines such as the Tractatus's closing sentence). Treat 59 as an upper bound on that lesser defect.

**Defect rate by section** (ATTRIBUTED-TO-PHILOSOPHER, eight-word method):

| Section | Defects | Per tested quotation | Per quotation shown to be an encyclopedist's prose |
|---|---|---|---|
| topics | 2 | 2 of 841 (0.24%) | 2 of 75 (2.7%) |
| concepts | 1 | 1 of 1,024 (0.10%) | 1 of 94 (1.1%) |
| apex | 0 | 0 of 5; 0 of 181 on the all-entries pass | 0 of 2 |
| voids | 2 | 2 of 446 (0.45%) | 2 of 19 (10.5%) |
| all | 5 | 5 of 2,316 (0.22%) | 5 of 190 (2.6%) |

The voids figure is after this week's ten void reviews removed their cases; the control shows at least two more stood there on 17 November. Apex pages are effectively unmeasured by citation (one page of 45 has a fetched entry), so their zero rests on the all-entries pass alone.

**Lower bound.** A laundering leaves a trace this method can follow only if the entry was fetched and the wording survived intact. 2,724 quotations (51%) are on pages where neither page nor mapped note cites any encyclopedia; 346 candidate entries were not fetched; only 15 Wikipedia entries were fetched against 188 cited by notes; the SEP text is today's revision, not the one a January note read.

**Sensitivity passes.**
- Seven-word window on quotations with no eight-word hit: 60 prose matches, 54 after dropping stock phrases, two real (both on pages already listed): `topics/eliminative-materialism` L80 and `voids/counterfactual-void` L62.
- Whole-quotation match for quotations of five to seven words (2,912 of them) against entries cited by the page or note: 86 verbatim hits, none credited to a philosopher, three unattributed (listed below).

**Seeding entries.**

| Entry | Author, version | Mis-credited quotations |
|---|---|---|
| SEP "The Epistemology of Modality" | Mallozzi, Vaidya & Wallner; rev. 7 July 2023 | 2 (one by seven-word pass), plus a paraphrased analogy |
| SEP "Eliminative Materialism" | William Ramsey; rev. 12 November 2024 | 2 (one by seven-word pass) |
| SEP "Self-Consciousness" | Joel Smith; rev. 14 June 2024 | 1 |
| SEP "Panpsychism" | Goff, Seager & Allen-Hermanson; rev. 13 May 2022 | 1 |
| IEP "Everettian Interpretations of Quantum Mechanics" | Christina Conroy; IEP prints no version date | 1 (probable) |

**Mis-credited philosophers.** One each: Dan Zahavi; Ramsey, Stich & Garon (1990 paper); Patricia Churchland; Peter van Inwagen; Stephen Yablo; Sam Coleman; Albert & Loewer. No philosopher recurs. Chalmers, the repeat case on the void pages, does not appear.

## ATTRIBUTED-TO-PHILOSOPHER Hits

Seven in total (five by the eight-word method, two by the seven-word pass), most prominent page first. Inbound counts are files under `obsidian/` that wikilink the slug.

**1. [[mine-ness]] L54** (concepts; 125 inbound; 27 of 27 words)
- Page: Mine-ness, on Zahavi's account, is the dimension of pre-reflective self-awareness that accompanies every conscious state: "In being aware of a thought, action, emotion, perceptual experience, memory, bodily experience (and also my body itself), I am aware of it as being my own."
- Entry (SEP "Self-Consciousness" §3.3, Joel Smith, rev. 14 June 2024): "…(Flanagan 1992; Martin 1995; Dokic 2003; Marcel 2003; Zahavi 2005: ch. 5; … García-Carpintero and Guillot 2023). According to some, a fundamental aspect of conscious experiences is that they seem, in each case, to be mine. In being aware of a thought, action, emotion, perceptual experience, memory, bodily experience (and also my body itself), I am aware of it as being my own. This sense of ownership arguably does some work…"
- The sentence is Smith's own gloss on a view he gives to "some", with Zahavi one of eleven sources cited. The page's reference list cites no encyclopedia.
- History: `reviews/deep-review-2026-07-15-mine-ness` found a paraphrase in quotation marks here, checked it against this SEP section, called the SEP sentence "Zahavi's actual wording (verbatim at publisher)" and restored it under his name.

**2. [[eliminative-materialism]] L106** (topics; 69 inbound; 18 of 18 words)
- Page: The argument runs: in feedforward connectionist networks trained to perform belief-like tasks, "there do not appear to be any structures in these networks that might serve as candidates for beliefs." … There are no causally distinct structures that stand for specific states of affairs.
- Entry (SEP "Eliminative Materialism", William Ramsey, rev. 12 November 2024): "…Rather, it is that in these networks there are no causally distinct structures that stand for specific states of affairs. Consequently, there do not appear to be any structures in these networks that might serve as candidates for beliefs and other propositional attitudes."
- The page presents this as the argument of Ramsey, Stich and Garon's 1990 paper (named at L104). The wording is Ramsey's, writing alone in the encyclopedia thirty years later. The page's last sentence in that paragraph is also the entry's, verbatim, with no quotation marks. Reference 16 cites the entry, dated 2019. Origin: `research/eliminative-materialism-2026-04-26` L102.

**3. [[eliminative-materialism]] L80** (seven-word pass; 7 of 9 words)
- Page: The book argues that "neuroscience portends a bleak future for commonsense mental states" and presses for vector-coding replacements of linguistic-format representation.
- Entry (same): "Patricia Churchland's provocative 1986 book, Neurophilosophy, suggests that developments in neuroscience point to a bleak future for commonsense mental states."
- Ramsey's summary, reworded ("portends" is in neither) and printed as the book's words.

**4. [[many-minds-interpretation]] L76** (topics; 38 inbound; 8 of 8 words; probable)
- Page: MMI was meant to recover Born statistics as a *measure over minds*—"the proportion of minds associated with each term" (Albert and Loewer 1988: 208).
- Entry (IEP "Everettian Interpretations of Quantum Mechanics", Christina Conroy): "The many minds view takes the norm squared of the coefficients on the terms to be interpreted as giving the proportion of minds associated with each term in the state of the system. In this view, probabilities “refer . . . to sequences of states of individual minds” (208)."
- The quoted words are Conroy's prose; the page number belongs to the entry's next quotation. Albert and Loewer 1988 was not obtained, so it is not excluded that they use the same phrase. The page cites the IEP entry (reference list and "(IEP)" elsewhere in the paragraph). Origin: `research/many-minds-interpretation-2026-06-24` L70.

**5. [[plurality-void]] L51** (voids; 36 inbound; 20 of 20 words)
- Page: Sam Coleman's subject-summing argument reveals the logical structure: … Combining your viewpoint and mine would require the resulting mind to have "both your experiences to the exclusion of all other experiences and my experiences to the exclusion of all other experiences"—a direct contradiction.
- Entry (SEP "Panpsychism", Goff, Seager & Allen-Hermanson, rev. 13 May 2022): "Sam Coleman (2014), for example, has argued that subject-summing is incoherent… If my point of view and your point of view were to be combined into an “uber-mind”, then that uber-mind would have to have both your experiences to the exclusion of all other experiences and my experiences to the exclusion of all other experiences. This seems flatly contradictory, assuming that you and I have different experiences."
- The entry's authors restating Coleman in their own voice. Coleman 2014 was not obtained. The page's references list Coleman 2014 and Goff 2017 but not this entry; "a direct contradiction" is firmer than the entry's "seems flatly contradictory". Origin: `research/voids-plurality-void-2026-02-24` L62, which prints the sentence as a quotation from "Sam Coleman".

**6. [[counterfactual-void]] L66** (voids; 34 inbound; 9 of 18 words, both halves present)
- Page: Peter van Inwagen pushes this further with a vision analogy: objects at the periphery of our visual field are judged less reliably than those at the centre. … but argues we should "withhold judgment concerning what we conceive or imagine... when outside the range of reliability of the specified capacity."
- Entry (SEP "The Epistemology of Modality", Mallozzi, Vaidya & Wallner, rev. 7 July 2023): "Van Inwagen (1998) voices skepticism about extraordinary cases by an analogy with vision. We do and should withhold judgment concerning what we see, when it is outside the range of reliability in our field of vision. … Similarly, we ought to withhold judgment concerning what we conceive or imagine or infer about modal reality, when they are outside the range of reliability of the specified capacity or method."
- Checked at source: the full text of van Inwagen 1998 (author-archive PDF, 18 pages, 7,661 words extracted) has 0 hits for "withhold", "reliab", "range of reliability", "specified capacity", "vision" and "periphery". His analogy is judging distance by eye ("many of our modal judgments are analogous to judgments of distance made by eye", pp. 69–70). Both the quotation and the visual-field analogy are the entry's. The page cites no encyclopedia.
- History: `reviews/deep-review-2026-07-19-counterfactual-void` L32 records this sentence as found in the primary text at that same PDF.

**7. [[counterfactual-void]] L62** (seven-word pass; 7 of 8 words)
- Page: Stephen Yablo argues that a proposition is conceivable if you can "imagine a world that one takes to verify" it.
- Entry (same): displays Yablo's definition as "(CON) p is conceivable for X, if X can imagine a world that X takes to verify p" (1993: 29), then writes in its own prose "involves imagining a world that one takes to verify some proposition p".
- The "one takes" wording is the entry's. The 07-19 review passed it as "a short standard fragment consistent with Yablo 1993; not independently re-run".

**UNATTRIBUTED (lesser; not ranked, no task proposed).**
- [[pudgalavada]] L41 "the fire is not the same as the fuel…", L43 "a real basis for identifying oneself…" and "the operation of karma is incomprehensible…": Priestley's IEP prose, in paragraphs that name Priestley nearby, but worded as the Personalists' own arguments. Also L79 "must change as they change" (Gold, SEP "Vasubandhu").
- [[no-self-objection-to-phenomenal-value]] L72 "phenomena do not endure for more than a moment": Coseru's SEP prose, between two sentences that do credit Coseru.
- [[russellian-monism]] L129 "play indispensable roles in physical causation": Alter and Pereboom's SEP prose, given as what "Russellian monism claims".
- [[mathematical-structure-of-the-consciousness-physics-interface]] L134 "quantum mind without quantum brain": Atmanspacher's SEP phrase, no one named.

## Critiques by Philosopher

This review applied one cross-corpus source-fidelity lens, so the six personas were not run page by page. Their common complaint against the seven hits is the same: an opponent who checks the quotation against the cited philosopher finds it absent, and the page's other attributions lose credit with it.

### The Eliminative Materialist
Churchland would note that [[eliminative-materialism]] puts a word in Patricia Churchland's mouth ("portends") that neither she nor the encyclopedia wrote, on the page that claims to engage her position most seriously.

### The Hard-Nosed Physicalist
Dennett would say the [[mine-ness]] case shows the Map's phenomenology citations resting on a third party's first-person gloss, which is the inflation of report into datum he warns about.

### The Quantum Skeptic
Tegmark would point at [[many-minds-interpretation]]: a page number from a 1988 physics-philosophy paper attached to a sentence the paper may not contain.

### The Many-Worlds Defender
Deutsch would add that the same sentence is the page's statement of how many-minds recovers the Born rule, so the weakest citation sits on the claim the page then attacks.

### The Empiricist
A Popperian would observe that two of these quotations survived a review that recorded them as verified. A check that passes a sentence absent from the source is not a test.

### The Buddhist Philosopher
Nagarjuna would note that [[pudgalavada]] lets a modern scholar's reconstruction stand as the Personalists' own speech, which settles by typography a question the page itself says is unsettled.

## Critical Issues

### Issue 1: Seven quotations credit a philosopher with an encyclopedist's sentence
- **File**: [[mine-ness]], [[eliminative-materialism]], [[many-minds-interpretation]], [[plurality-void]], [[counterfactual-void]]
- **Location**: listed above
- **Problem**: quotation marks under a philosopher's name around wording that is the encyclopedia author's
- **Severity**: High for [[mine-ness]] (125 inbound, and the quotation is the page's definition of its subject); Medium for the rest
- **Recommendation**: the four tasks below

### Issue 2: Two earlier deep reviews ratified the encyclopedia wording
- **File**: `reviews/deep-review-2026-07-15-mine-ness`, `reviews/deep-review-2026-07-19-counterfactual-void`
- **Problem**: one verified a "Zahavi" quotation against the SEP and called the SEP "the publisher"; the other reports a primary-text match that a raw grep of the same PDF does not reproduce
- **Severity**: Medium (process)
- **Recommendation**: see "For the operator"

## Counterarguments to Address

### "The encyclopedist may be silently reusing the philosopher's words"
- **Current content says**: the quotation is the philosopher's
- **A critic would argue**: SEP authors sometimes paraphrase closely, so entry prose could be near-verbatim primary text
- **Suggested response**: where the primary was obtainable (van Inwagen) it has none of the words. For Zahavi, Coleman, and Albert and Loewer the primary was not obtained, and each repair task asks the fork to try it first; if the wording is found there, the fix becomes a locator instead of a re-attribution.

## Unsupported Claims

| Claim | Location | Needed Support |
|---|---|---|
| Van Inwagen uses a visual-field analogy | [[counterfactual-void]] L66 | His text has distance judged by eye (p. 70); the visual-field version is the SEP's |
| "(Albert and Loewer 1988: 208)" for "the proportion of minds…" | [[many-minds-interpretation]] L76 | The page number belongs to a different quotation in the IEP entry |
| Zahavi wrote the "In being aware of a thought…" sentence | [[mine-ness]] L54 | No Zahavi text checked; the sentence is Joel Smith's |

## Language Improvements

| Current | Issue | Suggested |
|---|---|---|
| "—a direct contradiction" ([[plurality-void]] L51) | Firmer than the source's "seems flatly contradictory" | "—an apparent contradiction" |
| "The book argues that" ([[eliminative-materialism]] L80) | The entry has "suggests" | "suggests" |

## Priority List (four tasks)

Word counts are `tools.curate.length.analyze_length` taken in this session (about 23:05Z, 2026-11-18); gates fire at `>=`. No further ATTRIBUTED-TO-PHILOSOPHER hits remain outside these four tasks; the seven UNATTRIBUTED strings above are not included.

### Task 1 (P2): [[mine-ness]] L54 — the page's defining quotation is Joel Smith's SEP sentence, printed as Zahavi's
- **File**: obsidian/concepts/mine-ness.md
- **Length**: 3,494 against concepts hard 3,500. Five words of room. NET ≤ 0 is mandatory; the proposed NEW is −3.
- **Existing tasks**: one open task names this file on a Secondary-files line (todo L5766, for L48 "implicit tag"). It does not cover L54. Same file, so run them in one fork or in sequence.
- **OLD**: Mine-ness, on Zahavi's account, is the dimension of pre-reflective self-awareness that accompanies every conscious state: "In being aware of a thought, action, emotion, perceptual experience, memory, bodily experience (and also my body itself), I am aware of it as being my own."
- **Entry**: SEP "Self-Consciousness" §3.3, Joel Smith, first published 13 July 2017, rev. 14 June 2024 (passage quoted under hit 1).
- **NEW (paraphrase, no quotation marks, −3 words)**: Mine-ness, on Zahavi's account, is the dimension of pre-reflective self-awareness that accompanies every conscious state: whatever I am aware of (a thought, an action, an emotion, a perception, a memory, my body) I am aware of as my own.
- **Before applying**: try Zahavi 2005 ch. 5 and Zahavi 2014 for his own formulation. If one is found, quote it with a page instead. If not, the paraphrase stands as a description of his account. The alternative of crediting Smith by name costs about nine words plus a reference line and does not fit.
- **Do not** edit `reviews/deep-review-2026-07-15-mine-ness`; note in the new review that its "verbatim at publisher" finding is overturned.

### Task 2 (P2): [[eliminative-materialism]] L80 and L106 — two Ramsey (SEP) sentences printed as Patricia Churchland's book and as the 1990 Ramsey, Stich and Garon paper
- **File**: obsidian/topics/eliminative-materialism.md
- **Length**: 3,940 against topics hard 4,000. 59 words of room, and an open task (todo L4601) already plans +3. The proposed NEWs total +2.
- **Existing tasks**: two open tasks name this file (todo L2354, Sellars at L78; todo L4601, Dennett at L98). Neither covers L80 or L106. Fold all three into one fork.
- **L106 OLD**: The argument runs: in feedforward connectionist networks trained to perform belief-like tasks, "there do not appear to be any structures in these networks that might serve as candidates for beliefs." Information is distributed across weight matrices in ways that lack causally discrete, semantically evaluable units. There are no causally distinct structures that stand for specific states of affairs.
- **L106 NEW (−6 net: +7 for the attribution, −13 for the dropped final sentence)**: In Ramsey's later encyclopedia summary of the argument, in feedforward connectionist networks trained to perform belief-like tasks "there do not appear to be any structures in these networks that might serve as candidates for beliefs" (Ramsey 2024). Information is distributed across weight matrices in ways that lack causally discrete, semantically evaluable units.
  (The dropped final sentence is the entry's verbatim with no quotation marks, and repeats the sentence before it.)
- **L80 OLD**: The book argues that "neuroscience portends a bleak future for commonsense mental states" and presses for vector-coding replacements of linguistic-format representation.
- **L80 NEW (+8)**: The book, in Ramsey's summary, "suggests that developments in neuroscience point to a bleak future for commonsense mental states" (Ramsey 2024), and presses for vector-coding replacements of linguistic-format representation.
- **Reference 16**: "substantively revised 2019" → the live entry reads "substantive revision Tue Nov 12, 2024". Zero words.
- **Entry**: SEP "Eliminative Materialism", William Ramsey, first published 8 May 2003, rev. 12 November 2024.
- **Do not** edit `research/eliminative-materialism-2026-04-26` (origin, L102).

### Task 3 (P2): [[counterfactual-void]] L62 and L66, [[plurality-void]] L51 — SEP summaries printed as van Inwagen's, Yablo's and Coleman's words
- **Files**: obsidian/voids/counterfactual-void.md; obsidian/voids/plurality-void.md (two files)
- **Length**: counterfactual-void 2,393 and plurality-void 2,434 against voids hard 3,000. Room for the added reference lines; net-zero is not required.
- **Existing tasks**: counterfactual-void is on a Secondary-files line of one open task (todo L2591, zero-word wikilink pipes). It does not cover these lines. plurality-void: none.
- **counterfactual-void L66 OLD**: Peter van Inwagen pushes this further with a vision analogy: objects at the periphery of our visual field are judged less reliably than those at the centre. Similarly, extraordinary modal claims fall outside the reliable range of our modal faculty. Van Inwagen accepts everyday modal knowledge — this glass could break, I could have taken the other road — but argues we should "withhold judgment concerning what we conceive or imagine... when outside the range of reliability of the specified capacity."
- **NEW**: Peter van Inwagen pushes this further with an analogy to distance: "many of our modal judgments are analogous to judgments of distance made by eye" (1998, pp. 69–70), accurate at everyday range and useless for the sun and stars. Van Inwagen accepts everyday modal knowledge — this glass could break, I could have taken the other road — and on Mallozzi, Vaidya and Wallner's summary holds that "we ought to withhold judgment concerning what we conceive or imagine or infer about modal reality, when they are outside the range of reliability of the specified capacity or method" (2023).
  The "everyday range … sun and stars" gloss paraphrases p. 70; re-read it before keeping it. Add the SEP entry to References (Mallozzi, A., Vaidya, A. & Wallner, M., "The Epistemology of Modality", rev. 2023).
- **counterfactual-void L62 OLD**: Stephen Yablo argues that a proposition is conceivable if you can "imagine a world that one takes to verify" it.
- **L62 NEW (no quotation marks)**: Stephen Yablo argues that a proposition is conceivable for someone if they can imagine a world that they take to verify it (1993, p. 29).
- **plurality-void L51 OLD**: Combining your viewpoint and mine would require the resulting mind to have "both your experiences to the exclusion of all other experiences and my experiences to the exclusion of all other experiences"—a direct contradiction.
- **L51 NEW**: Combining your viewpoint and mine, as Goff, Seager and Allen-Hermanson put the argument, would require the resulting mind to have "both your experiences to the exclusion of all other experiences and my experiences to the exclusion of all other experiences"—an apparent contradiction.
  Add the SEP entry to References (Goff, P., Seager, W. & Allen-Hermanson, S., "Panpsychism", rev. 2022). Try Coleman 2014 (*Erkenntnis* 79(1)) first; if his own wording is found, quote that with a page.
- **Entries**: SEP "The Epistemology of Modality" (first published 5 December 2007, rev. 7 July 2023); SEP "Panpsychism" (first published 23 May 2001, rev. 13 May 2022).
- **Do not** edit the two February research notes or the 07-19 review; record in the new review that the 07-19 primary-text finding for van Inwagen is overturned (0 hits in the full paper).

### Task 4 (P3): [[many-minds-interpretation]] L76 — an IEP sentence carries Albert and Loewer's page number
- **File**: obsidian/topics/many-minds-interpretation.md
- **Length**: 2,493 against topics hard 4,000 (below soft 3,000). The proposed NEW is −4.
- **Existing tasks**: none name this file.
- **OLD**: MMI was meant to recover Born statistics as a *measure over minds*—"the proportion of minds associated with each term" (Albert and Loewer 1988: 208).
- **NEW**: MMI was meant to recover Born statistics as a *measure over minds*—"the proportion of minds associated with each term" (IEP).
- **Before applying**: try Albert and Loewer 1988, "Interpreting the Many Worlds Interpretation" (*Synthese* 77: 195–213; metadata from memory, confirm it), p. 208. If the phrase is there, keep the original citation and close the task as a false alarm. The IEP attaches "(208)" to a different quotation: "refer . . . to sequences of states of individual minds".
- **Entry**: IEP "Everettian Interpretations of Quantum Mechanics", Christina Conroy (no version date shown).

## What the Method Cannot See

- A laundering whose encyclopedia is cited by neither the page nor a mapped note, unless the entry happened to be among the 150 (this is how [[mine-ness]] was caught, and why 51% of quotations are effectively untested).
- The 346 candidate entries not fetched, including 173 of 188 Wikipedia entries cited by mapped notes.
- Research notes not mapped to a page by slug or wikilink (463 of 911 pages have no mapped note).
- Reworded quotations. The seven-word pass caught two; anything looser needs a reader.
- Quotations under eight words (the Merleau-Ponty case). The five-to-seven-word pass tested exact whole-string matches only.
- An entry that has been revised since the note was written.
- Entry prose that silently reuses the philosopher's wording (it would be mis-flagged as a defect), and the reverse error: a quotation the entry gives to philosopher A that the page gives to philosopher B (not checked among the 119 PRIMARY hits).
- Encyclopedia prose reused with no quotation marks at all. One instance surfaced by accident ([[eliminative-materialism]] L106, final sentence).

## For the Operator

Observations, not tasks.

- The corpus is in better shape on this axis than the void reviews suggested: 181 of 190 demonstrably encyclopedic quotations name the entry or its author. Many pages do this carefully ("as the incompatibilism entry reconstructs it", "(Maund 2024, §2.5)").
- Four of the five affected pages took the sentence from a research note dated February to June 2026 that gives it as the philosopher's (the plurality-void note prints it under "**Quote**" with "— Sam Coleman"); the fifth, mine-ness, got it from a July deep review. A research-note template could require each quotation to carry the URL it was copied from and a one-word source type (primary, encyclopedia, abstract, secondary).
- Two reviews ratified the laundering. A deep-review checklist line could say: a quotation verified only against an encyclopedia is verified as the encyclopedist's, and the attribution must then name the entry. A "found in primary text" finding could be required to state the grep count.
- The scripts and the 150 cached entries are in the session scratchpad and will not survive it. If this lens is worth repeating, the matcher is about 150 lines and could live under `tools/curate/`; the next run would best spend its fetches on the 173 unfetched Wikipedia entries and on entries cited by apex pages' source articles.
- The 59 UNLOCATED primary quotations (a famous line with no page number) are a separate, lower-value sweep and were not read individually.

## Strengths (Brief)

Recent pages attribute encyclopedia wording carefully and often flag when an entry's author is a party to the debate ("Clarke co-wrote that entry, so this is his own voice, not independent corroboration"). Preserve that habit.

## Appendix: Classified Hit Table

All 334 quotations with an eight-word match, by page. Class codes: P-OK, P-LOC, P-UNLOC = PRIMARY-IN-ENCYCLOPEDIA with OK-SECONDARY / LOCATED / UNLOCATED (pattern-assigned); E-ENTRY = encyclopedist's prose credited to the entry; **E-PHIL** = credited to a philosopher; E-UNATT = unattributed; NOT = not from the entry. "Cited" says whether the entry is cited by the page (p), a mapped note (n) or neither (o).

| Page | Line | Entry | Run/words | Cited | Class | Opening words |
|---|---|---|---|---|---|---|
| [[acquaintance-without-causation]] (topics) | 84 | SEP epiphenomenalism | 21/21 | p | E-ENTRY | our knowledge of them cannot be what… |
| [[acquaintance-without-causation]] (topics) | 86 | SEP epiphenomenalism | 14/14 | p | E-ENTRY | rejecting interactionism for virtually the same reason… |
| [[acquaintance-without-causation]] (topics) | 86 | SEP epiphenomenalism | 14/14 | p | E-ENTRY | does not have any property that contains… |
| [[agent-causation-and-acting-for-reasons]] (topics) | 42 | SEP incompatibilism-theories | 29/29 | p | E-ENTRY | Standard agent-causal views deny that events such… |
| [[agent-causation-and-acting-for-reasons]] (topics) | 42 | SEP freewill | 22/22 | p | E-ENTRY | must explain how reasons can explain and… |
| [[agent-causation-and-acting-for-reasons]] (topics) | 50 | SEP incompatibilism-theories | 27/27 | p | E-ENTRY | agents do not cause free decisions; rather,… |
| [[agent-causation-and-acting-for-reasons]] (topics) | 54 | SEP incompatibilism-theories | 14/14 | p | E-ENTRY | that only the agent cause what is… |
| [[agent-causation-and-acting-for-reasons]] (topics) | 60 | SEP incompatibilism-theories | 19/19 | p | E-ENTRY | can provide the same accounts of acting… |
| [[akrasia-and-weakness-of-will]] (topics) | 52 | SEP weakness-will | 27/29 | p | P-OK | No one...who either knows or believes that… |
| [[akrasia-and-weakness-of-will]] (topics) | 74 | SEP weakness-will | 26/34 | p | P-OK | what is the agent's reason for doing… |
| [[akrasia-and-weakness-of-will]] (topics) | 84 | SEP dynamic-choice | 15/15 | p | E-ENTRY | even though each choice in the series… |
| [[akrasia-and-weakness-of-will]] (topics) | 94 | SEP weakness-will | 8/8 | p | P-LOC | An agent's best judgment is just another… |
| [[akrasia-and-weakness-of-will]] (topics) | 106 | SEP weakness-will | 8/8 | p | E-ENTRY | does not actually engage the will at… |
| [[animal-consciousness]] (topics) | 102 | SEP phenomenal-intentionality | 8/15 | o | P-UNLOC | if and only if there is something… |
| [[assent-before-descartes]] (topics) | 40 | SEP stoicism | 16/16 | p | P-OK | 'in our power' or 'up to us'… |
| [[assent-before-descartes]] (topics) | 44 | SEP stoicism | 16/16 | p | E-ENTRY | is entirely free of opinion, since she… |
| [[assent-before-descartes]] (topics) | 50 | SEP stoicism | 43/43 | p | P-UNLOC | just as the person who pushed the… |
| [[assent-before-descartes]] (topics) | 58 | SEP skepticism-ancient | 8/8 | p | E-ENTRY | envisage three attitudes that cognizers take to… |
| [[assent-before-descartes]] (topics) | 62 | SEP skepticism-ancient | 22/22 | p | E-ENTRY | Non-doxastic assent is, from the point of… |
| [[assent-before-descartes]] (topics) | 62 | SEP skepticism-ancient | 8/8 | p | P-OK | does assent to the experiences forced upon… |
| [[assent-before-descartes]] (topics) | 64 | SEP skepticism-ancient | 25/25 | p | E-ENTRY | do not describe themselves as making an… |
| [[assent-before-descartes]] (topics) | 74 | SEP doxastic-voluntarism | 10/10 | p | P-OK | preconception by the will, an act of… |
| [[assent-before-descartes]] (topics) | 84 | SEP doxastic-voluntarism | 10/10 | p | E-ENTRY | compels assent—depriving the will of a choice… |
| [[assent-before-descartes]] (topics) | 84 | SEP doxastic-voluntarism | 34/34 | p | P-OK | our understanding is determined by the will,… |
| [[assent-before-descartes]] (topics) | 90 | SEP holkot | 16/16 | p | E-ENTRY | belonged to the first generation of scholars… |
| [[assent-before-descartes]] (topics) | 90 | SEP doxastic-voluntarism | 13/13 | p | E-ENTRY | would give both psychological and conceptual arguments… |
| [[assent-before-descartes]] (topics) | 92 | SEP doxastic-voluntarism | 42/42 | p | P-OK | every man, who does not want to… |
| [[assent-before-descartes]] (topics) | 94 | SEP doxastic-voluntarism | 18/18 | p | P-OK | I believe that this proposition is true,… |
| [[assent-before-descartes]] (topics) | 96 | SEP doxastic-voluntarism | 12/12 | p | E-ENTRY | presciently maintains that we may exercise some… |
| [[assent-before-descartes]] (topics) | 96 | SEP holkot | 11/11 | p | E-ENTRY | a version of what has come to… |
| [[buddhist-perspectives-on-meaning]] (topics) | 89 | SEP ethics-indian-buddhism | 12/12 | n | E-ENTRY | historically, most Buddhists have taken this system… |
| [[co-optimization-reply-to-the-correlation-problem]] (topics) | 63 | SEP epiphenomenalism | 24/24 | o | E-ENTRY | What 'pleasure' refers to in any possible… |
| [[colour-ontology-and-the-secondary-quality-residue]] (topics) | 49 | SEP color | 14/14 | p | E-ENTRY | On the face of it, only two… |
| [[colour-ontology-and-the-secondary-quality-residue]] (topics) | 49 | SEP color | 23/23 | p | E-ENTRY | The crucial issue between these two theories,… |
| [[colour-ontology-and-the-secondary-quality-residue]] (topics) | 53 | SEP color | 18/18 | p | E-ENTRY | powers to appear in distinctive ways to… |
| [[colour-ontology-and-the-secondary-quality-residue]] (topics) | 53 | SEP color | 12/12 | p | E-ENTRY | but, he thinks, giving this up is… |
| [[colour-ontology-and-the-secondary-quality-residue]] (topics) | 57 | SEP color | 14/14 | p | E-ENTRY | the Eliminativist is a Color Primitivist, but… |
| [[colour-ontology-and-the-secondary-quality-residue]] (topics) | 57 | SEP color | 15/15 | p | E-ENTRY | Most versions of Color Eliminativism/Irrealism commit one… |
| [[colour-ontology-and-the-secondary-quality-residue]] (topics) | 57 | SEP color | 13/13 | p | E-ENTRY | (i) dualist subjectivism, according to which subjective… |
| [[colour-ontology-and-the-secondary-quality-residue]] (topics) | 61 | SEP color | 8/8 | p | E-ENTRY | simple intrinsic, non-relational, non-reducible, qualitative properties… |
| [[colour-ontology-and-the-secondary-quality-residue]] (topics) | 67 | SEP color | 9/9 | p | E-ENTRY | on a questionable form of the doctrine… |
| [[colour-ontology-and-the-secondary-quality-residue]] (topics) | 77 | SEP color | 23/23 | p | E-ENTRY | Cohen and Hardin argue that there is… |
| [[colour-ontology-and-the-secondary-quality-residue]] (topics) | 85 | SEP perception-auditory | 15/15 | p | E-ENTRY | According to theories in which sounds are… |
| [[colour-ontology-and-the-secondary-quality-residue]] (topics) | 85 | SEP perception-auditory | 16/16 | p | E-ENTRY | sensations or projected features of auditory experiences,… |
| [[colour-ontology-and-the-secondary-quality-residue]] (topics) | 89 | SEP perception-auditory | 10/10 | p | E-ENTRY | commonly reject the identification of pitch with… |
| [[consciousness-and-the-epistemic-condition-on-responsibility]] (topics) | 43 | SEP moral-responsibility-epistemic | 19/19 | p | E-ENTRY | whether awareness is actually required at all… |
| [[consciousness-and-the-epistemic-condition-on-responsibility]] (topics) | 75 | SEP moral-responsibility-epistemic | 8/19 | p | NOT | an agent is responsible for F just… |
| [[consciousness-and-the-epistemic-condition-on-responsibility]] (topics) | 77 | SEP moral-responsibility-epistemic | 15/15 | p | E-ENTRY | such as forgetting a friend's birthday, sometimes… |
| [[consciousness-and-the-epistemic-condition-on-responsibility]] (topics) | 77 | SEP moral-responsibility-epistemic | 10/10 | p | P-OK | is not capable of bringing to consciousness… |
| [[consciousness-and-the-epistemic-condition-on-responsibility]] (topics) | 81 | SEP moral-responsibility-epistemic | 24/24 | p | E-ENTRY | or if they should and could be… |
| [[consciousness-and-the-metaphysics-of-composition]] (topics) | 105 | SEP panpsychism | 15/31 | n | P-LOC | Take a hundred of them, shuffle them… |
| [[consciousness-and-the-metaphysics-of-individuation]] (topics) | 53 | SEP consciousness-unity | 10/10 | o | P-LOC | nowhere will there be a consciousness of… |
| [[consciousness-as-activity]] (topics) | 49 | IEP hard-problem-of-conciousness | 10/10 | o | NOT | Why is the performance of these functions… |
| [[consciousness-defeats-explanation]] (topics) | 72 | SEP dualism | 8/11 | o | NOT | therefore there is something it is like… |
| [[constitutive-exclusion]] (topics) | 57 | SEP consciousness-animal | 8/8 | o | P-UNLOC | What Is It Like to Be a… |
| [[decoherence-and-macroscopic-superposition]] (topics) | 52 | SEP qm-decoherence | 24/24 | n | E-ENTRY | Decoherence as such does not provide a… |
| [[eighteenth-century-influx-debate]] (topics) | 43 | SEP wolff-christian | 13/13 | p | E-ENTRY | the pre-established harmony is a more probable… |
| [[eighteenth-century-influx-debate]] (topics) | 43 | SEP wolff-christian | 9/9 | p | E-ENTRY | that nothing significant turns on settling this… |
| [[eighteenth-century-influx-debate]] (topics) | 59 | SEP wolff-christian | 32/32 | p | E-ENTRY | On 8 November 1723, the king issued… |
| [[eighteenth-century-influx-debate]] (topics) | 59 | SEP wolff-christian | 40/40 | p | E-ENTRY | exploited their personal connections with the king,… |
| [[eighteenth-century-influx-debate]] (topics) | 65 | SEP wolff-christian | 15/15 | p | E-ENTRY | according to which one substance produces a… |
| [[eliminative-materialism]] (topics) | 106 | SEP materialism-eliminative | 18/18 | n | **E-PHIL** | there do not appear to be any… |
| [[eliminative-materialism]] (topics) | 120 | SEP materialism-eliminative | 8/28 | n | P-LOC | where the existence of conscious states is… |
| [[first-quantum-free-will-wave-1927-1940]] (topics) | 49 | SEP moral-responsibility | 17/17 | o | P-LOC | Freedom means the opposite of compulsion; a… |
| [[hard-problem-of-consciousness]] (topics) | 288 | SEP consciousness-animal | 8/8 | o | P-UNLOC | What Is It Like to Be a… |
| [[hempels-dilemma]] (topics) | 35 | SEP physicalism | 15/15 | p | E-ENTRY | clear enough to do the job that… |
| [[hempels-dilemma]] (topics) | 69 | SEP physicalism | 12/12 | p | E-ENTRY | the sort of property had by paradigmatic… |
| [[hempels-dilemma]] (topics) | 85 | SEP physicalism | 17/17 | p | P-OK | an attitude one takes to form one's… |
| [[hempels-dilemma]] (topics) | 89 | SEP physicalism | 10/12 | p | E-ENTRY | a particular proposal about how to define… |
| [[hempels-dilemma]] (topics) | 89 | SEP physicalism | 8/8 | p | E-ENTRY | what type of theory a physical theory… |
| [[hempels-dilemma]] (topics) | 109 | SEP physicalism | 19/19 | p | P-OK | it is the year 3000 AD and… |
| [[history-of-the-interaction-problem]] (topics) | 85 | IEP donald-davidson-anomalous-monism | 16/16 | o | P-UNLOC | The order and connection of ideas is… |
| [[indexical-identity-quantum-measurement]] (topics) | 85 | SEP qt-consciousness | 15/15 | n | E-ENTRY | introducing mental states as the essential missing… |
| [[indexical-identity-quantum-measurement]] (topics) | 91 | SEP qm-relational | 9/9 | n | E-ENTRY | There is nothing subjective, idealistic, or mentalistic,… |
| [[indexical-identity-quantum-measurement]] (topics) | 91 | SEP qm-relational | 9/9 | n | E-ENTRY | Subjects, or agents play no special role… |
| [[inheritance-problem-for-the-psychophysical-law]] (topics) | 70 | SEP panpsychism | 9/13 | o | NOT | produce and thereby (metaphysically) necessitate their effects… |
| [[interventionist-and-counterfactual-dualism]] (topics) | 92 | IEP mat-comp | 9/14 | o | NOT | has nothing to do with the fact… |
| [[invertebrate-consciousness-as-interface-test]] (topics) | 85 | SEP consciousness-animal | 20/21 | n | E-ENTRY | Phenomenally conscious perception of a stimulus facilitates,… |
| [[kants-paralogisms-and-the-maps-subject]] (topics) | 43 | SEP kant-mind | 9/11 | n | P-LOC | nothing further is represented than a transcendental… |
| [[kants-paralogisms-and-the-maps-subject]] (topics) | 54 | SEP kant-mind | 18/32 | n | P-LOC | It would be a great, or indeed… |
| [[kants-paralogisms-and-the-maps-subject]] (topics) | 82 | SEP self-consciousness | 11/11 | o | P-LOC | the fact that lies at the root… |
| [[language-recursion-and-consciousness]] (topics) | 92 | SEP phenomenal-intentionality | 16/16 | o | P-UNLOC | a kind of intentionality, pervasive in human… |
| [[leibnizs-mill-argument]] (topics) | 37 | SEP chinese-room | 93/93 | o | P-UNLOC | Moreover, it must be confessed that perception… |
| [[leibnizs-mill-argument]] (topics) | 67 | SEP chinese-room | 8/8 | o | P-UNLOC | never anything by which to explain a… |
| [[many-minds-interpretation]] (topics) | 48 | IEP everett | 14/14 | p | P-LOC | one cannot tell from the state of… |
| [[many-minds-interpretation]] (topics) | 56 | SEP qm-manyworlds | 8/8 | p | E-ENTRY | every sentient being has a continuum of… |
| [[many-minds-interpretation]] (topics) | 56 | SEP qm-manyworlds | 25/25 | p | E-ENTRY | the minds of this sentient being evolve… |
| [[many-minds-interpretation]] (topics) | 58 | IEP everett | 11/11 | p | E-ENTRY | not subject to the rules of quantum… |
| [[many-minds-interpretation]] (topics) | 58 | IEP everett | 12/12 | p | E-ENTRY | to which an observer has direct introspective… |
| [[many-minds-interpretation]] (topics) | 64 | SEP qm-manyworlds | 12/19 | p | E-ENTRY | the MMI of Albert and Loewer (1988)… |
| [[many-minds-interpretation]] (topics) | 76 | IEP everett | 8/8 | p | **E-PHIL** | the proportion of minds associated with each… |
| [[many-minds-interpretation]] (topics) | 76 | SEP qm-manyworlds | 16/16 | p | E-ENTRY | comes at the price of introducing additional… |
| [[moral-status-threshold-or-degrees]] (topics) | 57 | SEP grounds-moral-status | 38/38 | p | E-ENTRY | Once the importance of some feature, such… |
| [[neural-refresh-rates-and-the-smoothness-problem]] (topics) | 77 | SEP consciousness-temporal | 20/20 | n | P-UNLOC | stands permanent, like the rainbow on the… |
| [[panpsychisms-combination-problem]] (topics) | 51 | SEP panpsychism | 15/15 | n | P-LOC | shut in its own skin, windowless, ignorant… |
| [[phenomenology-of-recursive-self-awareness]] (topics) | 97 | SEP self-consciousness | 11/11 | o | P-UNLOC | I never can catch myself at any… |
| [[precommitment-and-the-diachronic-agent]] (topics) | 61 | SEP identity-ethics | 26/26 | p | E-ENTRY | If psychological continuity is relevant here, she… |
| [[precommitment-and-the-diachronic-agent]] (topics) | 61 | SEP transformative-experience | 15/26 | o | P-UNLOC | He might add, 'I regard my ideals… |
| [[precommitment-and-the-diachronic-agent]] (topics) | 77 | SEP decision-theory | 9/9 | p | E-ENTRY | stick to the strategy that was initially… |
| [[precommitment-and-the-diachronic-agent]] (topics) | 77 | SEP decision-theory | 10/10 | p | E-ENTRY | really points at which an agent is… |
| [[precommitment-and-the-diachronic-agent]] (topics) | 87 | SEP identity-ethics | 23/23 | p | E-ENTRY | not a lot of people have explicitly… |
| [[primary-secondary-quality-boundary]] (topics) | 39 | SEP qualities-prim-sec | 17/17 | p | P-UNLOC | nothing in the objects themselves but powers… |
| [[protocol-analysis]] (topics) | 105 | SEP introspection | 12/12 | p | E-ENTRY | people’s reports about their stream of thoughts… |
| [[quantum-non-equilibrium-and-the-contingency-of-the-born-rule]] (topics) | 37 | SEP qm-bohm | 16/16 | p | E-ENTRY | emerge naturally from an analysis of 'equilibrium'… |
| [[quantum-non-equilibrium-and-the-contingency-of-the-born-rule]] (topics) | 49 | SEP qm-bohm | 10/10 | p | E-ENTRY | the status of, and justification for, equilibrium… |
| [[reactive-attitudes-and-strawsonian-responsibility]] (topics) | 34 | SEP moral-responsibility | 15/40 | n | P-LOC | the very great importance that we attach… |
| [[sherrington-dualist-lineage]] (topics) | 27 | SEP dualism | 27/27 | p | E-ENTRY | some distinguished neuroscientists, such as Charles Sherrington… |
| [[singular-thought-and-acquaintance]] (topics) | 43 | SEP propositions-singular | 11/11 | p | E-ENTRY | For any purely qualitative condition Bill satisfies,… |
| [[singular-thought-and-acquaintance]] (topics) | 47 | SEP knowledge-acquaindescrip | 21/21 | o | P-UNLOC | when I have a direct cognitive relation… |
| [[singular-thought-and-acquaintance]] (topics) | 47 | SEP knowledge-acquaindescrip | 17/17 | o | P-UNLOC | Every proposition which we can understand must… |
| [[split-brain-consciousness]] (topics) | 94 | IEP phen-con | 8/39 | o | NOT | the psychological integration displayed by the patients… |
| [[synaesthesia]] (topics) | 88 | SEP stoicism | 10/13 | o | NOT | represent two colours to be in the… |
| [[tactile-consciousness-and-the-interface]] (topics) | 50 | IEP merleau | 17/17 | o | P-UNLOC | an ambiguous set-up in which both hands… |
| [[the-comic-and-humor-as-an-aesthetic-category]] (topics) | 55 | SEP humor | 15/15 | p | P-LOC | Laughter is an affection arising from the… |
| [[the-comic-and-humor-as-an-aesthetic-category]] (topics) | 55 | SEP humor | 41/41 | p | P-LOC | The cause of laughter in every case… |
| [[the-comic-and-humor-as-an-aesthetic-category]] (topics) | 55 | SEP humor | 20/20 | p | P-LOC | In every suddenly appearing conflict between what… |
| [[the-consequence-argument-for-incompatibilism]] (topics) | 72 | SEP freewill | 14/18 | o | NOT | I am able to do something such… |
| [[the-divided-will]] (topics) | 51 | SEP weakness-will | 10/15 | o | P-LOC | the actor cannot understand himself: he recognizes,… |
| [[the-steelman-for-process-monism]] (topics) | 57 | SEP mulla-sadra | 8/8 | p | P-OK | the change in him is substantial and… |
| [[the-steelman-for-process-monism]] (topics) | 59 | SEP mulla-sadra | 11/29 | p | P-OK | Existence is a single, simple reality having… |
| [[the-strong-emergence-of-consciousness]] (topics) | 81 | SEP properties-emergent | 12/29 | o | P-LOC | characteristic behaviour of the whole could not,… |
| [[time-symmetric-selection-mechanism]] (topics) | 74 | SEP qm-retrocausality | 10/10 | p | E-ENTRY | in principle compatible with a variety of… |
| [[vestibular-consciousness-and-the-interface]] (topics) | 36 | SEP bodily-awareness | 17/17 | p | E-ENTRY | Besides cases of dizziness, there seems to… |
| [[vestibular-consciousness-and-the-interface]] (topics) | 42 | SEP bodily-awareness | 10/10 | p | E-ENTRY | sensitive to motion acceleration as our head… |
| [[vestibular-consciousness-and-the-interface]] (topics) | 42 | SEP bodily-awareness | 11/11 | p | E-ENTRY | (1) 'Which way is up?' and (2)… |
| [[visual-indexes-and-demonstrative-reference]] (topics) | 69 | SEP attention | 15/15 | p | E-ENTRY | cannot demonstrate attention to a thing in… |
| [[wheelers-participatory-universe-and-it-from-bit]] (topics) | 148 | SEP qt-consciousness | 9/9 | p | E-ENTRY | approaches toward a neither-mental-nor-material base reality… |
| [[william-james-consciousness]] (topics) | 57 | SEP consciousness-temporal | 18/51 | o | P-UNLOC | Consciousness, then, does not appear to itself… |
| [[william-james-consciousness]] (topics) | 83 | SEP attention | 9/9 | o | P-UNLOC | My experience is what I agree to… |
| [[william-james-consciousness]] (topics) | 87 | SEP attention | 9/36 | o | P-UNLOC | Millions of items of the outward order… |
| [[access-consciousness]] (concepts) | 45 | SEP consciousness-neuroscience | 14/33 | o | P-UNLOC | A representation is access conscious if it… |
| [[anomalous-monism-and-the-denial-of-strict-psychophysical-laws]] (concepts) | 33 | SEP mental-causation | 9/20 | o | NOT | where there is causality, there must be… |
| [[anomalous-monism-and-the-denial-of-strict-psychophysical-laws]] (concepts) | 35 | SEP mental-causation | 13/18 | o | NOT | there are no strict deterministic laws on… |
| [[apophatic-approaches]] (concepts) | 58 | SEP wittgenstein | 9/9 | n | P-UNLOC | Whereof one cannot speak, thereof one must… |
| [[basic-argument-and-constitutive-luck]] (concepts) | 40 | SEP moral-responsibility | 12/15 | n | NOT | appears to prove that we cannot be… |
| [[basic-argument-and-constitutive-luck]] (concepts) | 47 | SEP skepticism-moral-responsibility | 21/21 | p | NOT | True self-determination is impossible because it requires… |
| [[basic-argument-and-constitutive-luck]] (concepts) | 51 | SEP skepticism-moral-responsibility | 22/22 | p | P-LOC | it could be just to punish some… |
| [[basic-argument-and-constitutive-luck]] (concepts) | 55 | SEP moral-luck | 14/14 | p | P-OK | when I first introduced the expression moral… |
| [[basic-argument-and-constitutive-luck]] (concepts) | 71 | SEP freewill | 9/9 | p | E-ENTRY | fully explain an agent's choice without causally… |
| [[basic-argument-and-constitutive-luck]] (concepts) | 71 | SEP freewill | 9/9 | p | E-ENTRY | the agent himself causes the choice that… |
| [[basic-argument-and-constitutive-luck]] (concepts) | 71 | SEP freewill | 17/17 | p | E-ENTRY | it is not true that there is… |
| [[basic-argument-and-constitutive-luck]] (concepts) | 73 | SEP freewill | 10/10 | p | E-ENTRY | argues that Strawson misconstrues the locus of… |
| [[basic-argument-and-constitutive-luck]] (concepts) | 77 | SEP skepticism-moral-responsibility | 8/8 | p | E-ENTRY | could, in theory, supply this sort of… |
| [[basic-argument-and-constitutive-luck]] (concepts) | 77 | SEP skepticism-moral-responsibility | 8/8 | p | E-ENTRY | cannot be reconciled with our best physical… |
| [[carrolls-regress]] (concepts) | 59 | SEP wittgenstein | 24/24 | o | P-LOC | no course of action could be determined… |
| [[causal-relevance-of-content]] (concepts) | 42 | SEP mental-causation | 9/9 | p | E-ENTRY | depends on its having the right sort… |
| [[causal-relevance-of-content]] (concepts) | 42 | SEP mental-causation | 9/9 | p | E-ENTRY | This is something the vending machine cares… |
| [[causal-relevance-of-content]] (concepts) | 42 | SEP mental-causation | 14/14 | p | E-ENTRY | not qua quarter, but only qua possessor… |
| [[causal-relevance-of-content]] (concepts) | 42 | SEP mental-causation | 8/8 | p | E-ENTRY | they are not causes as (or qua)… |
| [[causal-relevance-of-content]] (concepts) | 48 | SEP content-narrow | 10/10 | p | E-ENTRY | abandoned the idea that narrow content is… |
| [[causal-relevance-of-content]] (concepts) | 50 | SEP mental-causation | 20/20 | p | E-ENTRY | would seem to be sensitive only to… |
| [[causal-relevance-of-content]] (concepts) | 50 | SEP mental-causation | 23/23 | p | E-ENTRY | If intentional properties are relevant at all,… |
| [[causal-relevance-of-content]] (concepts) | 52 | SEP mental-causation | 9/9 | p | E-ENTRY | whether causal connections grounding these explanations involve… |
| [[causal-relevance-of-content]] (concepts) | 54 | SEP mental-causation | 15/15 | p | E-ENTRY | would at best seem to be addressing… |
| [[causal-relevance-of-content]] (concepts) | 94 | SEP mental-causation | 12/12 | p | E-ENTRY | no less problematic than mind–body interaction is… |
| [[chinese-room-argument]] (concepts) | 29 | SEP chinese-room | 9/9 | p | E-ENTRY | is not directly supported by the original… |
| [[consciousness-and-scientific-explanation]] (concepts) | 74 | SEP consciousness-animal | 8/8 | o | P-UNLOC | What Is It Like to Be a… |
| [[depersonalisation]] (concepts) | 37 | IEP higher-order-theories-of-consciousness | 12/12 | o | P-OK | Parts of my body feel as if… |
| [[depersonalisation]] (concepts) | 73 | SEP self-consciousness-phenomenological | 21/21 | p | E-ENTRY | that the subject claims not to be… |
| [[doxastic-voluntarism]] (concepts) | 42 | SEP doxastic-voluntarism | 14/14 | p | E-ENTRY | an existential claim: the view that at… |
| [[doxastic-voluntarism]] (concepts) | 44 | SEP doxastic-voluntarism | 11/11 | p | P-UNLOC | 'right away' or 'just like that', via… |
| [[doxastic-voluntarism]] (concepts) | 55 | SEP doxastic-voluntarism | 25/25 | p | E-ENTRY | insofar as these arguments rely on a… |
| [[doxastic-voluntarism]] (concepts) | 61 | SEP doxastic-voluntarism | 10/10 | p | E-ENTRY | we have neither basic nor non-basic control… |
| [[doxastic-voluntarism]] (concepts) | 67 | SEP doxastic-voluntarism | 10/10 | p | E-ENTRY | to believe p is to take p… |
| [[doxastic-voluntarism]] (concepts) | 69 | SEP doxastic-voluntarism | 10/10 | p | E-ENTRY | is widely held to be unsuccessful—at least… |
| [[emergence]] (concepts) | 58 | SEP properties-emergent | 12/29 | o | P-LOC | characteristic behaviour of the whole could not,… |
| [[evolution-of-consciousness]] (concepts) | 59 | SEP consciousness-animal | 10/10 | n | P-UNLOC | all mammals and birds, and many other… |
| [[evolution-of-consciousness]] (concepts) | 115 | SEP properties-emergent | 12/38 | n | P-LOC | characteristic behaviour of the whole could not,… |
| [[first-order-representationalism]] (concepts) | 58 | SEP introspection | 16/16 | o | P-UNLOC | the only features there to turn your… |
| [[geometric-model-of-mind]] (concepts) | 108 | SEP consciousness | 8/11 | o | NOT | this is what it is like to… |
| [[global-workspace-theory]] (concepts) | 162 | SEP consciousness-neuroscience | 20/20 | n | E-ENTRY | correlation cannot tell us whether the observed… |
| [[heterophenomenology]] (concepts) | 116 | SEP phenomenal-intentionality | 8/52 | o | P-UNLOC | The fact that an organism has conscious… |
| [[immunity-to-error-through-misidentification]] (concepts) | 42 | SEP kant-mind | 10/10 | o | P-LOC | is not due to my having identified… |
| [[immunity-to-error-through-misidentification]] (concepts) | 46 | SEP self-consciousness | 8/8 | p | E-ENTRY | might legitimately be considered the more fundamental… |
| [[immunity-to-error-through-misidentification]] (concepts) | 50 | SEP self-consciousness | 13/13 | p | E-ENTRY | is always relative, then, to the grounds… |
| [[immunity-to-error-through-misidentification]] (concepts) | 70 | SEP self-consciousness | 11/13 | p | NOT | the illusion of a purely inner and… |
| [[immunity-to-error-through-misidentification]] (concepts) | 70 | SEP self-consciousness | 11/11 | p | P-LOC | the fact that lies at the root… |
| [[immunity-to-error-through-misidentification]] (concepts) | 70 | SEP self-consciousness | 14/14 | p | P-OK | gives rise to the idea that they… |
| [[indexical-knowledge-and-identity]] (concepts) | 54 | SEP self-consciousness | 9/11 | o | NOT | I came to believe that John Perry… |
| [[inference-to-the-best-explanation-against-dualism]] (concepts) | 44 | SEP physicalism | 16/16 | p | E-ENTRY | it is rational to be guided in… |
| [[inference-to-the-best-explanation-against-dualism]] (concepts) | 44 | SEP physicalism | 9/9 | p | E-ENTRY | seems just as persuasive — in fact,… |
| [[inference-to-the-best-explanation-against-dualism]] (concepts) | 70 | SEP dualism | 14/14 | p | E-ENTRY | breaches ordinary standards of theory choice by… |
| [[inference-to-the-best-explanation-against-dualism]] (concepts) | 72 | SEP abduction | 12/12 | p | E-ENTRY | may well lead us to believe 'the… |
| [[intentionality]] (concepts) | 167 | IEP cognitive-phenomenology | 9/9 | o | P-UNLOC | the intentionality of phenomenology and the phenomenology… |
| [[interpretive-sensory-access-theory]] (concepts) | 48 | SEP introspection | 30/30 | p | E-ENTRY | presents a case for parity of access… |
| [[interpretive-sensory-access-theory]] (concepts) | 52 | SEP introspection | 10/10 | p | E-ENTRY | sympathetic to skepticism about special access even… |
| [[interpretive-sensory-access-theory]] (concepts) | 52 | SEP introspection | 19/19 | p | E-ENTRY | that people confabulate not just in reporting… |
| [[interpretive-sensory-access-theory]] (concepts) | 52 | SEP introspection | 20/20 | p | E-ENTRY | not only about the cause of their… |
| [[interpretive-sensory-access-theory]] (concepts) | 72 | SEP introspection | 11/11 | p | E-ENTRY | that theoretical inference and self-monitoring are distinct… |
| [[interpretive-sensory-access-theory]] (concepts) | 80 | SEP introspection | 10/10 | p | E-ENTRY | according to which one is self-blind in… |
| [[introspection]] (concepts) | 151 | SEP self-consciousness | 11/11 | o | P-UNLOC | I never can catch myself at any… |
| [[inverted-qualia]] (concepts) | 96 | SEP qualia-inverted | 22/22 | p | E-ENTRY | almost uncontroversially: if an inverted spectrum argument… |
| [[inverted-qualia]] (concepts) | 98 | SEP qualia-inverted | 22/22 | p | E-ENTRY | Shoemaker is a notable dissenter on this… |
| [[lawful-appearance-problem]] (concepts) | 54 | SEP panpsychism | 9/13 | o | NOT | produce and thereby (metaphysically) necessitate their effects… |
| [[lived-objectified-body-distinction]] (concepts) | 90 | SEP merleau-ponty | 14/14 | o | NOT | the most important lesson of the reduction… |
| [[measurement-problem]] (concepts) | 59 | SEP qm-manyworlds | 8/11 | n | NOT | Either the wavefunction...is not everything, or it… |
| [[mental-causation-and-downward-causation]] (concepts) | 111 | SEP zombies | 8/11 | o | NOT | every physical effect has a physical cause… |
| [[mine-ness]] (concepts) | 54 | SEP self-consciousness | 27/27 | o | **E-PHIL** | In being aware of a thought, action,… |
| [[modal-epistemology]] (concepts) | 45 | SEP modality-epistemology | 15/15 | p | E-ENTRY | be constrained by some crucial information about… |
| [[modal-epistemology]] (concepts) | 59 | SEP modality-epistemology | 10/10 | p | P-UNLOC | carries with it the cognitive capacity to… |
| [[modal-epistemology]] (concepts) | 59 | SEP modality-epistemology | 18/18 | p | P-OK | the epistemology of metaphysically modal thinking is… |
| [[modal-epistemology]] (concepts) | 75 | SEP modality-epistemology | 29/29 | p | E-ENTRY | either skeptical or silent about extraordinary or… |
| [[modal-epistemology]] (concepts) | 81 | SEP modality-epistemology | 8/8 | p | E-ENTRY | Modal knowledge is, thus, for Vetter, distinctively… |
| [[mysterianism]] (concepts) | 90 | SEP consciousness-animal | 8/8 | o | P-UNLOC | What Is It Like to Be a… |
| [[neural-correlates-of-consciousness]] (concepts) | 81 | IEP dualism-and-mind | 14/14 | p | E-ENTRY | interactionism actually predicts that mental events are… |
| [[new-dispositionalism]] (concepts) | 31 | SEP abilities | 14/28 | p | P-LOC | An agent has the ability to A… |
| [[new-dispositionalism]] (concepts) | 45 | SEP abilities | 10/10 | p | P-OK | not so choosing, I am utterly unable… |
| [[new-dispositionalism]] (concepts) | 47 | SEP abilities | 29/29 | p | E-ENTRY | it may be that the failures of… |
| [[new-dispositionalism]] (concepts) | 53 | SEP moral-responsibility | 8/19 | o | NOT | the truth of determinism does not entail… |
| [[new-dispositionalism]] (concepts) | 67 | SEP abilities | 20/20 | p | P-OK | then even if I have a capacity… |
| [[no-self-objection-to-phenomenal-value]] (concepts) | 72 | SEP mind-indian-buddhism | 17/17 | p | E-ENTRY | postulates that human beings are reducible to… |
| [[no-self-objection-to-phenomenal-value]] (concepts) | 72 | SEP mind-indian-buddhism | 12/12 | p | E-ENTRY | is nothing but a conventional designation that… |
| [[no-self-objection-to-phenomenal-value]] (concepts) | 72 | SEP mind-indian-buddhism | 9/9 | p | E-UNATT | phenomena do not endure for more than… |
| [[no-self-objection-to-phenomenal-value]] (concepts) | 72 | SEP mind-indian-buddhism | 14/14 | p | E-ENTRY | precisely in order to avoid the metaphysical… |
| [[objectivity-and-consciousness]] (concepts) | 48 | SEP consciousness | 8/8 | o | NOT | What it is like to be a… |
| [[ontic-structural-realism]] (concepts) | 35 | SEP structural-realism | 8/8 | p | P-OK | one of form or structure, not of… |
| [[ontic-structural-realism]] (concepts) | 43 | SEP structural-realism | 17/17 | p | E-ENTRY | tell us only about the form or… |
| [[ontic-structural-realism]] (concepts) | 43 | SEP structural-realism | 29/35 | p | E-ENTRY | a metaphysical position according to which... the… |
| [[ontic-structural-realism]] (concepts) | 51 | SEP structural-realism | 24/24 | p | E-ENTRY | Peter Unger (1979) also argues that our… |
| [[ontic-structural-realism]] (concepts) | 77 | SEP structural-realism | 13/13 | p | E-ENTRY | structure is not sufficient to uniquely pick… |
| [[ontic-structural-realism]] (concepts) | 93 | SEP russellian-monism | 15/21 | p | P-UNLOC | There are respectable structuralist or dispositionalist views… |
| [[ontic-structural-realism]] (concepts) | 93 | SEP russellian-monism | 10/17 | p | P-UNLOC | many find these views objectionable, because they… |
| [[panprotopsychism]] (concepts) | 31 | SEP russellian-monism | 15/15 | o | P-UNLOC | are not phenomenal (there is nothing it… |
| [[penfield-interactionist-dualism]] (concepts) | 52 | SEP dualism | 27/27 | p | E-ENTRY | some distinguished neuroscientists, such as Charles Sherrington… |
| [[phenomenal-consciousness]] (concepts) | 48 | SEP dualism | 9/20 | o | NOT | experience; what makes a state phenomenally conscious… |
| [[phenomenal-conservatism]] (concepts) | 40 | IEP phen-con | 19/26 | p | NOT | If it seems to S that P,… |
| [[phenomenal-constitution-thesis]] (concepts) | 60 | IEP cognitive-phenomenology | 19/19 | p | E-ENTRY | a non-causal explanatory relation that can alternatively… |
| [[phenomenal-constitution-thesis]] (concepts) | 64 | SEP phenomenal-intentionality | 16/16 | p | P-OK | a kind of intentionality, pervasive in human… |
| [[prebiotic-collapse]] (concepts) | 54 | WP Consciousness_causes_collapse | 32/32 | n | P-UNLOC | they would exist only in linearly superposed… |
| [[primitive-identities-and-strong-necessities]] (concepts) | 67 | SEP physicalism | 29/29 | p | E-ENTRY | if one wants to defend a posteriori… |
| [[primitive-identities-and-strong-necessities]] (concepts) | 79 | SEP zombies | 22/22 | p | P-OK | it is fair of the physicalist to… |
| [[problem-of-other-minds]] (concepts) | 232 | SEP consciousness-animal | 8/8 | o | P-UNLOC | What Is It Like to Be a… |
| [[process-philosophy]] (concepts) | 128 | IEP emergence | 8/8 | o | P-LOC | nothing more than the sum of its… |
| [[pudgalavada]] (concepts) | 39 | IEP pudgalavada-buddhist-philosophy | 8/8 | p | E-ENTRY | by far the largest of the Shrāvakayāna… |
| [[pudgalavada]] (concepts) | 41 | IEP pudgalavada-buddhist-philosophy | 11/11 | p | E-ENTRY | characterize a real self, a self that… |
| [[pudgalavada]] (concepts) | 41 | IEP pudgalavada-buddhist-philosophy | 21/31 | p | E-UNATT | the fire is not the same as… |
| [[pudgalavada]] (concepts) | 41 | IEP pudgalavada-buddhist-philosophy | 38/38 | p | P-UNLOC | 'inexpressible,' that is, as indeterminate in its… |
| [[pudgalavada]] (concepts) | 43 | IEP pudgalavada-buddhist-philosophy | 10/16 | p | E-UNATT | a real basis for identifying oneself ...… |
| [[pudgalavada]] (concepts) | 43 | IEP pudgalavada-buddhist-philosophy | 17/17 | p | E-UNATT | the operation of karma is incomprehensible if… |
| [[pudgalavada]] (concepts) | 47 | IEP pudgalavada-buddhist-philosophy | 16/16 | p | E-ENTRY | quite limited, much of it surviving only… |
| [[pudgalavada]] (concepts) | 49 | IEP pudgalavada-buddhist-philosophy | 36/44 | p | E-ENTRY | seem to have regarded the self, at… |
| [[pudgalavada]] (concepts) | 53 | SEP mind-indian-buddhism | 22/22 | p | E-ENTRY | a good case for taking the Pudgalavādins… |
| [[pudgalavada]] (concepts) | 63 | SEP vasubandhu | 10/10 | p | E-ENTRY | everything that is real or substantial (dravya)… |
| [[pudgalavada]] (concepts) | 63 | SEP vasubandhu | 11/11 | p | E-ENTRY | only to indicate the Buddhist position's comparative… |
| [[pudgalavada]] (concepts) | 83 | SEP vasubandhu | 11/11 | p | E-ENTRY | something like an incredulous denial that we… |
| [[pudgalavada]] (concepts) | 83 | SEP vasubandhu | 9/9 | p | E-ENTRY | the possibility of change in a self-regulating… |
| [[quantum-interpretations]] (concepts) | 84 | SEP qm-relational | 9/9 | o | E-ENTRY | There is nothing subjective, idealistic, or mentalistic,… |
| [[relational-quantum-mechanics]] (concepts) | 83 | SEP qm-relational | 9/9 | p | E-ENTRY | There is nothing subjective, idealistic, or mentalistic,… |
| [[revelation-thesis]] (concepts) | 42 | SEP color | 20/20 | p | E-ENTRY | The intrinsic nature of canary yellow is… |
| [[revelation-thesis]] (concepts) | 54 | IEP hard-problem-of-conciousness | 8/11 | o | E-ENTRY | there is no good reason to think… |
| [[rollback-argument-against-agent-causation]] (concepts) | 47 | SEP incompatibilism-theories | 35/35 | p | E-ENTRY | Nothing about the world prior to the… |
| [[rollback-argument-against-agent-causation]] (concepts) | 57 | SEP freewill | 20/20 | p | E-ENTRY | is not exercised prior to, but at… |
| [[rollback-argument-against-agent-causation]] (concepts) | 57 | SEP incompatibilism-theories | 10/10 | p | E-ENTRY | is a matter of how Leo exercises… |
| [[rollback-argument-against-agent-causation]] (concepts) | 75 | SEP freewill | 18/18 | p | E-ENTRY | might present special problems beyond those posed… |
| [[seemings]] (concepts) | 39 | IEP phen-con | 18/18 | p | E-ENTRY | continue to appear a certain way even… |
| [[seemings]] (concepts) | 41 | IEP phen-con | 16/16 | p | E-ENTRY | I have not defined “appearance”, and I… |
| [[seemings]] (concepts) | 54 | IEP phen-con | 20/20 | p | E-ENTRY | one is disposed to believe that P… |
| [[self-blindness]] (concepts) | 65 | SEP introspection | 12/12 | p | E-ENTRY | are accounts according to which one is… |
| [[self-blindness]] (concepts) | 65 | SEP introspection | 17/17 | p | E-ENTRY | confabulate not just in reporting the causes… |
| [[self-blindness]] (concepts) | 106 | SEP self-knowledge | 21/21 | p | E-ENTRY | if a conception of rationality is too… |
| [[self-control-as-skill-and-scaffolding]] (concepts) | 40 | SEP weakness-will | 17/17 | p | E-ENTRY | diachronic regulation and external scaffolding may be… |
| [[self-control-as-skill-and-scaffolding]] (concepts) | 54 | SEP weakness-will | 17/17 | p | E-ENTRY | a kind of skill or a set… |
| [[self-reference-paradox]] (concepts) | 90 | SEP self-consciousness | 11/11 | o | P-UNLOC | I never can catch myself at any… |
| [[the-ownerless-suffering-argument]] (concepts) | 41 | SEP ethics-indian-buddhism | 11/11 | p | P-UNLOC | they are to be warded off simply… |
| [[the-ownerless-suffering-argument]] (concepts) | 49 | SEP shantideva | 33/33 | p | P-OK | 101. The continuum of consciousness, like a… |
| [[the-ownerless-suffering-argument]] (concepts) | 51 | SEP shantideva | 25/25 | p | P-UNLOC | 102. Without exception, no sufferings belong to… |
| [[the-ownerless-suffering-argument]] (concepts) | 57 | SEP ethics-indian-buddhism | 8/8 | p | E-ENTRY | some scholars now call the Ownerless Suffering… |
| [[the-ownerless-suffering-argument]] (concepts) | 71 | SEP ethics-indian-buddhism | 22/22 | p | E-ENTRY | it's hard to see how the Ownerless… |
| [[the-ownerless-suffering-argument]] (concepts) | 79 | SEP shantideva | 8/8 | p | P-LOC | The person who experiences suffering does not… |
| [[the-ownerless-suffering-argument]] (concepts) | 87 | SEP ethics-indian-buddhism | 37/37 | p | E-ENTRY | From the perspective of this argument, your… |
| [[the-ownerless-suffering-argument]] (concepts) | 103 | SEP shantideva | 45/45 | p | E-ENTRY | regards the Ownerless Suffering Argument as itself… |
| [[transparency-method-of-self-knowledge]] (concepts) | 30 | SEP introspection | 24/29 | p | P-LOC | I get myself in a position to… |
| [[transparency-method-of-self-knowledge]] (concepts) | 36 | SEP introspection | 14/14 | p | P-UNLOC | one's eyes are, so to speak, or… |
| [[transparency-method-of-self-knowledge]] (concepts) | 36 | SEP introspection | 12/12 | p | P-UNLOC | Do you think there is going to… |
| [[transparency-method-of-self-knowledge]] (concepts) | 60 | SEP introspection | 9/9 | p | P-LOC | BEL If p, believe that you believe… |
| [[transparency-method-of-self-knowledge]] (concepts) | 62 | SEP self-knowledge | 11/11 | p | E-ENTRY | limits his account to explaining self-knowledge of… |
| [[transparency-method-of-self-knowledge]] (concepts) | 66 | SEP introspection | 13/13 | p | E-ENTRY | can drive the accurate self-ascription of all… |
| [[transparency-method-of-self-knowledge]] (concepts) | 66 | SEP introspection | 8/8 | p | E-ENTRY | something like an expressive account of self-ascription… |
| [[transparency-method-of-self-knowledge]] (concepts) | 72 | SEP self-knowledge | 8/8 | p | E-ENTRY | it will not appear reasonable to the… |
| [[type-a-type-b-and-type-c-physicalism]] (concepts) | 103 | IEP hard-problem-of-conciousness | 19/19 | p | E-ENTRY | we can still identify consciousness with physical… |
| [[type-a-type-b-and-type-c-physicalism]] (concepts) | 105 | IEP hard-problem-of-conciousness | 11/11 | p | E-ENTRY | Identities have no explanation: a thing just… |
| [[type-a-type-b-and-type-c-physicalism]] (concepts) | 105 | IEP hard-problem-of-conciousness | 15/15 | p | E-ENTRY | the question of mental causation still provides… |
| [[types-of-consciousness]] (concepts) | 45 | SEP consciousness | 8/17 | o | NOT | the phenomenally conscious aspect of a state… |
| [[unity-of-consciousness]] (concepts) | 117 | SEP panpsychism | 14/14 | o | P-UNLOC | each remains the same feeling it always… |
| [[vitalism]] (concepts) | 62 | IEP hard-problem-of-conciousness | 10/19 | o | NOT | Our vitalist can surely ask the same… |
| [[witness-consciousness]] (concepts) | 76 | SEP self-consciousness | 11/11 | n | P-UNLOC | I never can catch myself at any… |
| [[cross-modal-capability-division]] (apex) | 96 | SEP bodily-awareness | 8/8 | p | E-ENTRY | a paucity of vestibular experiences in normal… |
| [[embodied-interface]] (apex) | 89 | SEP bodily-awareness | 8/8 | o | E-ENTRY | a paucity of vestibular experiences in normal… |
| [[mereology-of-mind]] (apex) | 85 | SEP panpsychism | 13/13 | o | P-UNLOC | remains the same feeling it always was,… |
| [[what-it-might-be-like-to-be-an-ai]] (apex) | 72 | SEP consciousness-animal | 8/8 | o | P-LOC | What is it like to be a… |
| [[what-it-might-be-like-to-be-an-ai]] (apex) | 136 | SEP consciousness-animal | 8/8 | o | P-UNLOC | what is it like to be a… |
| [[apophatic-cartography]] (voids) | 60 | SEP wittgenstein | 9/9 | o | P-UNLOC | Whereof one cannot speak, thereof one must… |
| [[appetitive-void]] (voids) | 69 | WP Four_Noble_Truths | 19/19 | o | P-UNLOC | The complete cessation of that very thirst… |
| [[assent-void]] (voids) | 63 | SEP doxastic-voluntarism | 10/10 | p | E-ENTRY | to believe p is to take p… |
| [[assent-void]] (voids) | 63 | SEP doxastic-voluntarism | 10/10 | p | E-ENTRY | is widely held to be unsuccessful—at least… |
| [[assent-void]] (voids) | 79 | SEP introspection | 20/21 | o | P-LOC | in making a self-ascription of belief, one's… |
| [[beloved-void]] (voids) | 55 | SEP love | 15/15 | p | E-ENTRY | What, if anything, justifies my coming to… |
| [[beloved-void]] (voids) | 55 | SEP love | 14/14 | p | E-ENTRY | the best we can do is offer… |
| [[beloved-void]] (voids) | 55 | SEP love | 22/22 | p | E-ENTRY | there can be no answer to question… |
| [[beloved-void]] (voids) | 55 | SEP love | 13/13 | p | P-OK | reason is vital in determining whom we… |
| [[beloved-void]] (voids) | 65 | SEP love | 15/15 | p | E-ENTRY | my beloved is not fungible—that no one… |
| [[beloved-void]] (voids) | 65 | SEP love | 10/10 | p | E-ENTRY | though she insists that it is very… |
| [[beloved-void]] (voids) | 77 | SEP love | 22/22 | p | E-ENTRY | appraisal is a response to value that… |
| [[beloved-void]] (voids) | 77 | SEP love | 9/10 | p | P-OK | love…confers importance no matter what the object… |
| [[binding-void]] (voids) | 57 | SEP consciousness-unity | 35/35 | p | P-UNLOC | Then stand the men in a row… |
| [[binding-void]] (voids) | 73 | SEP consciousness-unity | 10/10 | p | E-ENTRY | could itself be a mechanism for unifying… |
| [[blindspot-void]] (voids) | 37 | SEP epistemic-paradoxes | 17/17 | p | E-ENTRY | A blindspot for a propositional attitude is… |
| [[blindspot-void]] (voids) | 43 | SEP epistemic-paradoxes | 11/11 | p | E-ENTRY | The speaker has managed to contradict himself… |
| [[blindspot-void]] (voids) | 43 | SEP epistemic-paradoxes | 16/16 | p | P-OK | 'I am a poet but I do… |
| [[blindspot-void]] (voids) | 45 | SEP fitch-paradox | 16/16 | p | E-ENTRY | if any truth can be known then… |
| [[boredom-void]] (voids) | 58 | IEP boredom | 14/14 | n | P-UNLOC | not being bored can be a sign… |
| [[conceptual-scheme-void]] (voids) | 66 | SEP thomas-kuhn | 14/14 | o | P-UNLOC | see different things when they look from… |
| [[confabulation-void]] (voids) | 57 | SEP introspection | 10/10 | o | P-UNLOC | you need a shovel to clean out… |
| [[counterfactual-void]] (voids) | 66 | SEP modality-epistemology | 9/18 | n | **E-PHIL** | withhold judgment concerning what we conceive or… |
| [[embodiment-cognitive-limits]] (voids) | 132 | SEP embodied-cognition | 12/12 | p | E-ENTRY | reject the idea that mentality is fundamentally… |
| [[emergence-void]] (voids) | 62 | SEP properties-emergent | 10/12 | p | P-LOC | could not, even in theory, be deduced… |
| [[language-thought-boundary]] (voids) | 69 | SEP wittgenstein | 9/9 | n | P-UNLOC | Whereof one cannot speak, thereof one must… |
| [[molyneux-void]] (voids) | 49 | SEP molyneux-problem | 14/21 | p | P-LOC | whether by his sight, before he touched… |
| [[molyneux-void]] (voids) | 49 | SEP molyneux-problem | 17/21 | p | P-UNLOC | has not yet obtained the experience, that… |
| [[molyneux-void]] (voids) | 71 | SEP molyneux-problem | 33/33 | p | E-ENTRY | robust visual shape recognition normally requires a… |
| [[molyneux-void]] (voids) | 73 | SEP molyneux-problem | 8/8 | p | E-ENTRY | may turn out to require a scientific… |
| [[narrative-void]] (voids) | 57 | SEP introspection | 10/10 | o | P-UNLOC | you need a shovel to clean out… |
| [[observation-and-measurement-void]] (voids) | 88 | IEP qualia | 27/27 | o | P-LOC | Every subjective phenomenon is essentially connected with… |
| [[observation-and-measurement-void]] (voids) | 94 | SEP introspection | 8/8 | o | E-ENTRY | a shifting confluence of many processes, recruited… |
| [[origin-of-consciousness]] (voids) | 61 | SEP consciousness-neuroscience | 13/13 | o | P-UNLOC | Why should physical processing give rise to… |
| [[origin-of-consciousness]] (voids) | 123 | SEP zombies | 18/18 | o | P-UNLOC | invariably underestimate the task of conception (or… |
| [[plurality-void]] (voids) | 51 | SEP panpsychism | 20/20 | n | **E-PHIL** | both your experiences to the exclusion of… |
| [[plurality-void]] (voids) | 53 | SEP consciousness-unity | 20/20 | n | P-OK | there is nothing that would even count… |
| [[preference-void]] (voids) | 71 | SEP preferences | 10/10 | p | E-ENTRY | treats answers as agents' privileged access to… |
| [[self-opacity]] (voids) | 78 | SEP self-consciousness | 11/11 | o | P-UNLOC | I never can catch myself at any… |
| [[the-silence-void]] (voids) | 93 | SEP wittgenstein | 9/9 | o | P-UNLOC | Whereof one cannot speak, thereof one must… |
| [[the-silence-void]] (voids) | 93 | SEP wittgenstein | 11/14 | o | P-UNLOC | There are, indeed, things that cannot be… |
| [[void-as-ground-of-meaning]] (voids) | 63 | SEP wittgenstein | 9/9 | o | P-UNLOC | Whereof one cannot speak, thereof one must… |
| [[wakefulness-void]] (voids) | 72 | SEP dreams-dreaming | 19/19 | p | P-OK | As if I did not remember other… |
