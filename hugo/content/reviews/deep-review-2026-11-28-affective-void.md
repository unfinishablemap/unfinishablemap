---
ai_contribution: 100
ai_generated_date: 2026-11-28
ai_modified: 2026-11-28 09:27:50+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-28
date: &id001 2026-11-28
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-28 09:27:50+00:00
modified: *id001
related_articles: []
title: Deep Review - The Affective Void
topics: []
---

**Date**: 2026-11-28
**Article**: [The Affective Void](/voids/affective-void/)
**Previous review**: [2026-07-16](/reviews/deep-review-2026-07-16-affective-void/)

## Outcome

Driver-selected: `deep_review.py` never picks voids, and this page is from the early cohort (created 2026-02-02 from `research/voids-affective-void-2026-01-31`). This run grepped every quoted string against raw source text. The 2026-07-16 ledger had called the citation seam "exhausted". It was not. Four of its "verified" items were defective:

- the Freitas quote was the wording of a different work;
- both de Waal quotes came from an interview, not the cited book;
- one de Waal quote had a spliced subject, and "immediately adds" was false;
- the Tomkins line was an uncredited near-verbatim lift from Frank & Wilson.

Five more defects came from the later-cohort and tenet lenses. All were fixed.

- **Length** (`analyze_length`): 2,163 → 2,220 (+57). Voids soft limit 2,000, hard 3,000.
- **Reference block**: about +5 net. Two entries were removed (the de Waal book, and the orphan Scarantino entry) and two added (Reese 2019, Frank & Wilson 2020).
- **Prose**: about +52, almost all of it attribution apparatus the fixes need ("on Frank and Wilson's reading", the de Waal qualifier, the Cowen–Keltner self-report correction, the Tenet 5 converse). Trims offset part of it: the redundant L54 sentence, the L109 "We don't experience the gap…" sentence, the MQI "quantum biases…" phrase, and two Further Reading glosses.

## Quotation Verification Ledger (every quoted string, grepped in raw source, whitespace collapsed)

| Quoted string (article) | Source grepped | Result |
|---|---|---|
| "fully comparable in richness of detail to our own" | Nagel 1974, *Phil. Review* 83(4) text (cs.ox.ac.uk e-library PDF, pdftotext) | **verbatim**. Nagel's sentence is about "bats and Martians". The article's "permanently inaccessible" gloss matches his next sentence, "such an understanding may be permanently denied to us by the limits of our nature". |
| "cognitively closed" | McGinn 1989, *Mind* 98(391) (OUP-downloaded copy, header "Mind, Vol. xcviii, no. 391, July 1989") | **verbatim**. The unquoted paraphrase "concept-forming procedures … cannot extend to grasp" matches McGinn's definition. |
| "bridged by continuous gradients" | Cowen & Keltner 2017, PMC5617253 (efetch: title, abstract and significance only) | **verbatim** (title). |
| "inherited affect programs are elements in, rather than the executive administrators of, affective life" | Frank & Wilson 2020, *A Silvan Tomkins Handbook*, Manifold (manifold.umn.edu) section 629f0805…, between page-breaks p36 and p37 | **verbatim, Frank & Wilson's words, p. 36**. Their sentence begins "In the end, for Tomkins, …". It is absent from PMC6057353 (Hutto, Robertson & Kirchhoff 2018), the URL the research note cites for it: 0 hits for "executive" and "administrat". |
| "Alien species, having evolved … than we, also could have a different but equally adaptive emotional repertoire" | Freitas 1984, "Xenopsychology", *Analog* 104 (April 1984) 41–53, as reproduced at rfreitas.com/Astro/Xenopsychology.htm | **verbatim (new wording)**. The OLD wording "should also have" is the *Xenology* (1979; online 2008) §20.2.3 text at xenology.info, a different work from the one cited. |
| "no direct analog in human experience" | Freitas 1984, and *Xenology* §20.2.3 | **verbatim in both** |
| "I cannot name any emotion that is uniquely human" | Hope Reese, Longreads interview, 12 March 2019 | **verbatim**. The full sentence is "But the more I think about it, I cannot name any emotion that is uniquely human." |
| "the most unsolved question" | Reese 2019 | **verbatim** (the source has a capital T: "The most unsolved question is what animals feel.") |
| "the whole aspect of consciousness and feelings is beyond our science at the moment" | Reese 2019 | **verbatim**. It is the answer to the interview's last question, not adjacent to the first quote. |
| "doesn't need to stay that way" | Reese 2019 | **verbatim** (the source has a curly apostrophe) |
| "basic emotions"; "beyond human reach", "affect missing here", "something more", "missing" | none | Scare quotes or hypothetical markers. No author is attributed. |

## Publisher-of-Record Citation Ledger

- **Nagel 1974** (*Phil. Review* 83(4):435–450): real-correct. Quote and gloss verified above.
- **McGinn 1989** (*Mind* 98(391):349–366): real-correct. Stance: McGinn is a naturalist mysterian ("there exists some property of the brain that accounts naturalistically for consciousness", p. 352 region). The article does not enlist him for dualism.
- **Ekman 1992** (*Cognition & Emotion* 6(3–4):169–200): real-correct at Crossref (10.1080/02699939208411068). The Ekman PDF at paulekman.com is image-only with no text layer, so it was not grepped directly. The "dedicated neural substrate" gloss is checked at second hand: Hutto et al. 2018 (PMC6057353) quote Ekman 1992 as "it is necessary to posit emotion-specific central nervous system (CNS) activity in my account of basic emotions", and add that Ekman "clearly rejects the idea that affect programs are literally neuronally instantiated computer programs". The article frames this as a programme-level claim that is "contested rather than settled", which is adequate.
- **Cowen & Keltner 2017** (*PNAS* 114(38):E7900–E7909, PMC5617253): metadata real-correct. **Result-direction: FIXED.**
  - The paper's finding comes from *self-report*: the videos "reliably elicit 27 distinct varieties of reported emotional experience", which "categorical labels … better capture … than commonly measured affective dimensions".
  - The article had inferred that "our own emotional space exceeds our introspective capacity", which inverts that finding. Self-report captured the richness; the standard models under-described it.
  - "at least 27" appears only in the 2018 TICS reply (Cowen & Keltner 2018, 22(4):274–276, PMC5866789: "this requires at least 27 dimensions … most current taxonomies detail 10–15 distinct states"). It was dropped, and "reported" was added.
  - The 2018 reply also uses "dimensions" for the 27. The 07-16 "dimensions → categories" change is therefore harmless but was not a correction of an error.
- **Freitas 1984** (*Analog* 104(4), April 1984, pp. 41–53): metadata real-correct. **Quote cited to the wrong work: FIXED.**
  - The article quoted *Xenology*'s "should also have", which is a stronger modal than the cited Analog text's "also could have".
  - "some entirely emotionless" hardened the source's "Very smart aliens … may be emotionless". It is now "some perhaps emotionless".
- **de Waal**: the 2019 book *Mama's Last Hug* (W. W. Norton; title verified at library catalogues) was REMOVED as the cite. **Both quotes come from Reese 2019 (Longreads interview): FIXED.**
  - "immediately adds" was false: the second quote answers the interview's final question.
  - The OLD quote "what animals feel... is beyond our science at the moment" was spliced in the subject. The source's subject is "the whole aspect of consciousness and feelings". The source says "The most unsolved question is what animals feel."
  - The article had dropped de Waal's qualifier "it doesn't need to stay that way" while using the quote as evidence for an *unexplorable* void. The qualifier is restored, and the void's further question ("whether part of it must") is marked as the Map's.
  - Whether the first line also appears in the book was not checked. No full text was reached.
  - Stance: de Waal is a naturalist who separates observable emotions from inaccessible feelings. He is not enlisted for dualism.
- **Cytowic 1995** ("Synesthesia: Phenomenology and Neuropsychology. A Review of Current Knowledge", *Psyche* 2(10), July 1995): real-correct. The subtitle was added. It was verified at the Wayback snapshot of psyche.cs.monash.edu.au (2009-09-12), §1.2: "the rare capacity to hear colors, taste shapes". **Former orphan, now cited inline** at the synesthesia sentence.
- **Scarantino 2010** (*BJPS* 61(4):729–768): real-correct at Crossref (10.1093/bjps/axq011), but an **orphan**, never cited inline. **REMOVED.**
- **Berridge & Robinson 1998** (*Brain Res. Rev.* 28(3):309–369, 10.1016/S0165-0173(98)00019-8): real-correct at Crossref.
  - Result-direction checked in the full text (lecerveau.mcgill.ca PDF): "Although incentive salience attribution ordinarily is coordinated by associative learning and hedonic activation, it can be triggered independently of them by some neural and pharmacological manipulations" (pp. 312–313). Footnote 4 says the core processes "can exist and control human and animal behavior even in the absence of the subjective states".
  - That supports both "run with hedonic impact absent" and "need not be felt at all".
  - Note: the paper's *own* new experiment shows the reverse direction (liking survives the loss of wanting after dopamine depletion). The wanting-without-liking direction is reviewed from Berridge & Valenstein (ref. 44).
  - Scare quotes were added around 'wanting'/'liking', per the paper's own convention (fn 4).
- **Frank & Wilson 2020** (*A Silvan Tomkins Handbook: Foundations for Affect Theory*, University of Minnesota Press; copyright page "Adam J. Frank and Elizabeth A. Wilson"): ADDED. Stance: humanities affect theorists. The quote characterizes Tomkins and is attributed as their reading.
- **Reese 2019** (Longreads, 12 March 2019, "'I Cannot Name Any Emotion That Is Uniquely Human.'"): ADDED.
- **Superlatives**: none in the article.

## Pessimistic Analysis Summary

### Critical Issues Found (9, all fixed)

1. **Freitas quote cited to the wrong work, with a hardened modal.**
   - OLD: "…than we, should also have a different but equally adaptive emotional repertoire"—some entirely emotionless
   - NEW: "…than we, also could have a different but equally adaptive emotional repertoire"—some perhaps emotionless (cited 1984)
2. **de Waal: wrong work, false adjacency, spliced subject, dropped qualifier.**
   - OLD: claims "I cannot name…," but immediately adds that "what animals feel... is beyond our science at the moment."
   - NEW: told an interviewer "I cannot name…," yet called what animals feel "the most unsolved question": "the whole aspect of consciousness and feelings is beyond our science at the moment" (Reese 2019). He holds that this "doesn't need to stay that way"; the affective void asks whether part of it must.
3. **Cowen & Keltner result-direction inversion.**
   - OLD: "identifies at least 27 distinct categories of emotion … If our own emotional space exceeds our introspective capacity…"
   - NEW: "identifies 27 distinct categories of reported emotion … Self-report captured that richness where the standard models had not. If our own emotional space outruns the models built to describe it…"
4. **Tomkins: uncredited near-verbatim lift of Frank & Wilson's sentence, with no reference entry.**
   - OLD: "These affect programs are, in Silvan Tomkins's account, elements in rather than the executive administrators of affective life."
   - NEW: "Silvan Tomkins gave such programs a humbler role: on Frank and Wilson's reading, 'inherited affect programs are elements in, rather than the executive administrators of, affective life' (2020, 36)." The contrast with Ekman, which Frank & Wilson draw explicitly ("running the show"), is now visible.
5. **Internal contradiction and quasi-epiphenomenal drift (Bidirectional paragraph).**
   - OLD: "we cannot access either their experiences or the causal contributions those experiences make". This contradicted the article's own "We infer from behaviour".
   - NEW: "those affects would leave observable traces in behaviour—the emotions de Waal says he can see—while the felt character that produced them stays out of reach."
6. **[P-V3](/positions/voids-as-evidence/#p-v3) calibration: the void was graded as tenet support.**
   - OLD: "Dualism makes the void intelligible … The affective void is one instance of consciousness exceeding what any single form of embodiment can access."
   - NEW: "Dualism is compatible with the void but gains no support from it … the evolutionary and architectural sources of closure are ones a physicalist accepts too, so the void does not discriminate between the views."
7. **The synesthetic-void summary dropped the sibling's qualifiers.** The sibling's L63 says *externalist* representationalism and *surface* stimuli; its L113 says "This reply works"; its L111 grants each physicalist reading a serious version. "Some report qualia with no match" also overgeneralized the sibling's "at least one well-documented case".
   - OLD: "**Synesthesia demonstrates unexploited phenomenal dimensions.** … some report qualia with no match … challenge functionalist and representationalist accounts: identical inputs produce different phenomenal states"
   - NEW: "**Synesthesia shows that the phenomenal palette is not shared.** … (Cytowic 1995). … press on functionalist and externalist representationalist accounts, since identical surface stimuli appear to yield different phenomenal states, while granting each physicalist reading a serious reply."
   - The "Martian colours" claim was dropped here because its source is not in the sibling's References (see follow-ups).
8. **An uncited overgeneralization that contradicts a sibling.**
   - OLD: "practitioners consistently report reaching limits beyond which experience cannot go. The limits themselves are data about the boundary."
   - NEW: "the traditions [disagree about how their deepest states feel](/topics/affective-tone-divergence-across-meditative-traditions/); whether any reported ceiling marks the edge of affect or only of description is unsettled."
9. **Orphan references.** Scarantino 2010 was removed. Cytowic 1995 is now cited inline.

### Medium Issues Found (fixed)

- **Tenet 5 was used one way only.** The Occam paragraph now says the tenet "cuts both ways": it disarms the simplicity argument but "gives no positive reason to think the larger space is populated".
- **Conceptual closure was hardened.**
  - OLD: "Every emotional concept we possess is defined through contrast … literally unthinkable"
  - NEW: "If emotional concepts are defined largely by contrast … unthinkable except as the bare schema of a feeling we lack" (this keeps the lead's "not forbidden but unthinkable").
- **Evidence-section framing.**
  - OLD: "suggest the affective void is genuine rather than merely unexplored"
  - NEW: "are consistent with the affective void without establishing it"
- **"Vast space" hardening**, three places:
  - L69: "of what may be a vast possibility space";
  - the closing: "rather than others that may be possible";
  - the description: "the perhaps vast space".
- **Banned negation-correction constructs**, three rephrased:
  - L95: "This is not a matter of … but of the wrong wiring";
  - the closing: "not privileged windows …—they are";
  - L69: "not just *more* …—they may be".
- **MQI paragraph**: the muddled-direction phrase "quantum biases generating our particular affective palette" was removed. The paragraph's own hedges were kept.
- **Redundant sentence**: "Different environments, different bodies…" was removed. It duplicated the lead's "Different selection pressures would have produced different affects".

### Counterarguments Considered

- **Deflationary objection**: unchanged. The reply is a framework-boundary engagement, per the stability notes. The Dualism paragraph now names it as the reading dualism supplies.
- **Engagement modes** (editor-internal; changelog only):
  - Deflationary objection: Mixed. A Mode Two move (the functional-exhaustion premise is unearned), then a Mode Three boundary.
  - Synesthesia physicalist readings: delegated to the sibling, which carries the Mode One and Mode Two work. This page now reports that honestly.

### Tenet Readings (PRIORITY 3)

- **[P-V3](/positions/voids-as-evidence/#p-v3)**: the dualism link is graded compatible, non-discriminating (fixed, Critical #6).
- **Tenet 5**: binds both sides (fixed, Medium #1).
- **[P-M2](/positions/methodology-and-calibration/#p-m2)**: the page makes no cross-tradition convergence claim. The contemplative paragraph now cites the traditions' *divergence*.
- **Epiphenomenalism**: not conceded. Critical #5 removed the "cannot access the causal contributions" drift.

## Optimistic Analysis Summary

### Strengths Preserved

- The Nagel-framed lead and its "not forbidden but unthinkable" phrasing.
- The evolutionary-contingency toolkit argument.
- The dimensional-geometry metaphor.
- The five-source closure taxonomy.
- The appetitive-boundary paragraph (Berridge & Robinson, now verified).
- The phenomenology bullets.
- The valence/mood closing triad.

### Enhancements Made

- One piped cross-link: `affective-tone-divergence-across-meditative-traditions`. It replaces an uncited claim with the sibling that carries the evidence.
- The Bidirectional paragraph now ties back to de Waal's emotion/feeling distinction, which makes the void's interactionist reading concrete.

### Pronoun / next-sentence check

- "Either way, they form our inherited emotional toolkit": *they* = the affect programs. The next sentence's "toolkits" still binds.
- "He holds that this…" refers to the beyond-science limit, and "part of it" refers to the same limit.
- "the felt character that produced them": *them* = those affects.
- "that web of contrasts": the antecedent was restored after the rewrite.

## Seeding Note Defects (`research/voids-affective-void-2026-01-31`; NOT edited)

1. **L51 Nagel "cow … hay … delightful sweetness or bland starch"**: absent from Nagel 1974 (0 hits for "cow" in the full text). A quotation invented in a famous author's mouth.
2. **L95 McGinn "like trying to see ultraviolet light"**: absent from McGinn 1989 (the refine of 2026-09-11 removed it from the article). Still live in the note.
3. **L54/L62/L230 Freitas**:
   - the URL is *Xenology* (1979) §20.2.3, while the citation is "Freund, R. (1980) … *Analog* 100(4)" (wrong author, year and volume);
   - the quote drops "than we";
   - the cited *Analog* 1984 text says "also could have", not "should also have".
4. **L98/L104/L106 Tomkins**: the phrase is Frank & Wilson 2020, p. 36, and is absent from the cited PMC6057353. L106 presents it as a stand-alone "Quote" of Tomkins.
5. **L117 de Waal**: the quote is filed under the psychedelic source (tandfonline). Its real source is Reese 2019 (Longreads).
6. **L120–L128**: the de Waal quotes are attributed to PMC6966324 (Paul et al., "Towards a comparative science of emotion"), where neither appears. L126 carries the spliced subject. The L128 "Quote" ("Due to unique features of the human brain…") is absent from PMC6966324: 0 hits for "unique features of the human brain", "linguistic distinctions" and "feelings like us".
7. **L65–L73 Cowen & Keltner**:
   - the URL PMC5866789 is the 2018 TICS reply, not the 2017 PNAS paper;
   - "at least 27 dimensions" and "continuous gradients between categories traditionally thought of as discrete" are 2018 wording;
   - L149 and L213 infer "inaccessible to introspection" from a *self-report* finding, which is the source of the article's inversion.
8. **L80 "Demonstrates that the human qualia space has unexploited dimensions"**: the note's own gloss, presented under the IEP source.
9. **L233 citation 7 "Carhart-Harris, R., et al. (2025)"**: Crossref for 10.1080/09515089.2025.2526652 gives **Cova, F., & Seragnoli, F.** (2025), "The role of self-transcendent emotions in psychedelic experiences: a two-process proposal", *Philosophical Psychology*. The author is wrong and the subtitle is missing.

## Remaining Items

None for this article. Corpus follow-ups are listed in the changelog entry for the driver to queue.

## Stability Notes (what was checked, exactly)

1. **Every quoted string** in the body was grepped in raw source text this run (whitespace collapsed). The table above names the file and source for each. Unlike the 07-16 claim, this ledger can be re-run from named sources.
2. **The Tomkins line is now a credited quotation of Frank & Wilson (2020, p. 36).** Do NOT de-quote it, and do NOT re-attribute it to Tomkins's own words. The 07-16 note was right that the words are not Tomkins's, but leaving them unquoted left Frank & Wilson's sentence uncredited.
3. **The Freitas quote follows the cited 1984 *Analog* text ("also could have").** Restore "should also have" only if the citation is switched to *Xenology* (1979/2008) §20.2.3.
4. **The de Waal quotes are cited to Reese 2019**, the interview. Do not re-cite them to *Mama's Last Hug* unless a full-text grep of the book finds them. The qualifier "doesn't need to stay that way" must travel with the "beyond our science" quote.
5. **Cowen & Keltner is a self-report finding.** No sentence may infer from it that emotion exceeds introspection.
6. **The Dualism paragraph grades the void as compatible and non-discriminating ([P-V3](/positions/voids-as-evidence/#p-v3)).** Do not restore "makes the void intelligible" or "one instance of consciousness exceeding…".
7. **Not reached** (so not certified):
   - Ekman 1992 full text (image-only PDF). Only the substrate gloss was checked, via Hutto et al.'s quotation of it.
   - The *Mama's Last Hug* full text.
   - The Cowen & Keltner 2017 body text (PMC returns front matter only).
   - Ramachandran & Hubbard 2001 for "Martian colours" (which is why the claim was dropped here).
   - Cytowic 1995 was checked against a 2009 Wayback snapshot, because the publisher of record (Psyche) is defunct.
8. Carried forward: the deflationary objection is a bedrock framework-boundary disagreement. Do not expand past the voids soft threshold without equal cuts.