---
ai_contribution: 100
ai_generated_date: 2026-11-27
ai_modified: 2026-11-27 06:40:42+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-27
date: &id001 2026-11-27
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-27 06:40:42+00:00
modified: *id001
related_articles: []
title: Deep Review - The Aspect Perception Void (source-fidelity pass)
topics: []
---

**Date**: 2026-11-27
**Article**: [The Aspect Perception Void](/voids/aspect-perception-void/)
**Previous reviews**: [2026-07-18](/reviews/deep-review-2026-07-18-aspect-perception-void/), [2026-06-04](/reviews/deep-review-2026-06-04-aspect-perception-void/), [2026-05-02](/reviews/deep-review-2026-05-02-aspect-perception-void/). This is the fourth review.
**Trigger**: Driver-selected. It was the last May–July void with no open task and no review since mid-October. The page was created 2026-05-01 (b4d634949a, expand-topic) from `research/voids-aspect-perception-void-2026-05-01`, and the creation commit names no other seed. Intervening edits, read and preserved: f9ce4fee64 (2026-05-10 wikilink redirect), 7af293b4f6 (2026-07-06 coalesce repointing `thought-stream-void` to `transit-void`), 6891ac9296 (2026-07-18 Siegel→Price fix and metadata).
**Word count** (`tools.curate.length.analyze_length`; voids soft 2,000, hard 3,000, gate `>=`): 2,018 → 2,621 (+603). Split by whitespace tokens: prose before the tenet section 1,462 → 1,881, tenet section 231 → 336, References 248 → 330, Further Reading unchanged at 82. That leaves 378 words of headroom under hard. Length-neutral mode was attempted, and five passages were trimmed after drafting. The rest of the growth comes from corrections that had to state what the source actually says, so it was accepted.

## Why the prior "converged" verdicts failed

The 05-02 review certified the Aeon quotation and then "fixed" it in place. It changed the source's "is normally taken to be" to "are normally taken to be" inside quotation marks, and certified a source that does not contain the passage at all. The 07-18 review carried 11 references forward "as verified from the 2026-05-02 attribution pass" without opening them. Three of those 11 were wrong: the Krebs & Day Element, the "SEP Cognitive Penetrability" entry and the Nachtomy & Blank autism gloss. Its ledger line "Wittgenstein … real-correct (verified in 2026-05-02 review)" was also uncertified: the 05-02 check was made against the research note. Lesson, as with the meaning void: a review that carries a ledger line forward has to reopen the source.

## Pessimistic Analysis Summary

### Critical Issues Found (all fixed)

1. **Quotation attributed to the wrong source, with a splice in the predicate** (old L71). The page said "Aeon's framing captures the doubleness" and quoted "neither subjective (inner, metaphysically private) nor objective" and two further clauses. The Aeon Ideas piece "Do you see a duck or a rabbit: just what is aspect perception?" is by **Stephen Law** (31 July 2018, 1,200 words, fetched in full). It contains none of the quoted phrases ("neither subjective", "normally taken", "revelatory": 0 hits each). The passage is the summary of **Avner Baz, *Wittgenstein on Aspect Perception*** (Cambridge Elements in the Philosophy of Ludwig Wittgenstein, published online 2 November 2020, doi 10.1017/9781108878012), grepped verbatim on the Cambridge page. The page had also re-conjugated the source inside the quotation marks ("they 'present…'", "they are '… are normally taken to be'"). The source reads "it presents…" and "it is 'subject to the will', but at the same time is normally taken to be…", with 'subject to the will' as Baz's own inner quotation of Wittgenstein. **Fix**: the quotation is now verbatim, with the source's singular subject, and is attributed to Baz (2020).
2. **Wrong author on the reference that was the quote's real source** (ref #8). "Krebs, V.J., & Day, W. (Eds.). *Wittgenstein on Aspect Perception*. Cambridge Elements." The Element is single-authored by Avner Baz (Tufts). Day & Krebs edited a different book, *Seeing Wittgenstein Anew* (CUP 2010), which Baz's own reference list cites. **Fix**: the reference is now Baz 2020, with its DOI.
3. **Dropped qualifier in the tenet section** (old L107). "Aspect-seeing is at once 'subject to the will' and 'revelatory of the object.'" This omitted Baz's "is normally taken to be", the same qualifier the 05-02 review restored in the Constitution paragraph and missed here. It also carried no attribution, and the seeding note had assigned it to Wittgenstein ("Wittgenstein notes … 'revelatory of the object'"). **Fix**: the tenet paragraph now quotes only Wittgenstein's own "subject to the will" (Anscombe p. 213: "Seeing an aspect and imagining are subject to the will").
4. **A fabricated characterisation of Nachtomy & Blank** (old L63). The page said "(Nachtomy and Blank canvass aspect-blindness as a candidate model, with caution about overgeneralisation)" [of autism]. The full text was fetched through the Wayback copy of the PhilArchive PDF, which carries JSTOR cover metadata: *Iyyun* 64 (2015): 57–76. It has **0 hits** for "autis", "Asperger", "Necker", "disorder" and "patholog" (positive controls: "aspect blind" 47 hits, "meaning blind" 59). The paper's "caution" concerns something else entirely: "one must be cautious not to overgeneralize here and claim that any seeing involves aspect seeing". Its thesis is that for Wittgenstein "an aspect blind person would be meaning blind". **Fix**: the autism attribution is removed. Nachtomy & Blank are now cited for their actual thesis (aspect-blindness implies meaning-blindness), and their real caution is used where it belongs, in the cognitive-penetration paragraph. The reference gains venue, year and pages.
5. **The empirical claim reversed the page's own cited source** (old L63). The page said "The autism-perception literature reports systematic differences in Necker-cube reversal rates and in the pickup of social aspects." The page's own Garrido & Tovar (2025) abstract (OpenAlex) says that "previous studies in this field have yielded variable and conflicting results leading to inconsistent conclusions". No source supported "pickup of social aspects". **Fix**: the sentence now quotes Garrido & Tovar's verdict. The "Approaches" probe list no longer equates autism with aspect-blindness.
6. **Convergence overclaim** (old L63). "Three lines of evidence converge": one line was a conflicting literature, one an a priori argument, and one an open question. **Fix**: "Three lines of inquiry bear on this face, and none settles it."
7. **Friedland softened and his stance misdescribed** (old L63). "May face an in-principle limit on aesthetic and meaning aspects". Friedland's abstract (OpenAlex; Crossref 10.1111/j.1467-9205.2005.00250.x) says the answer "is in fact available. And it is a negative a priori." His target is "aesthetic sensibility", not "meaning aspects". His ground is that rigid "input-to-output parameters" are absent from aesthetic judgement, and that the system cannot share in "the collective engagements of human solidarity". The seeding note's reading of this as support for dualism ("accessible only to phenomenal subjects") is not his. **Fix**: his conclusion, ground and stance are now stated.
8. **Wittgenstein's aspect-blind person misdescribed** (old L61). "Someone who cannot see one thing as another, who misses the internal relations of a thing with its surroundings." The "internal relations" clause is not Wittgenstein's description of the aspect-blind. His "internal relation" remark (p. 212) is about what one perceives in the dawning. The 2026-05-01 research note attributes the phrase to Nachtomy & Blank, but their text has 0 hits for "internal relation" and "misses somehow", so it is unsourced. In Anscombe pp. 213–14, the aspect-blind man can find the black cross in the double cross and recognise a drawing as a representation of a cube, "but for him it would not jump from one aspect to the other". Wittgenstein likens the defect to "the lack of a 'musical ear'" and leaves other features open ("I do not want to settle this"). **Fix**: the passage now follows the text. This sharpens the page's seam claim, since Wittgenstein's aspect-blind lack the dawning (face 1), not recognition.
9. **Chronology error in the lead**. "Wittgenstein … opened the territory with the duck-rabbit. Subsequent work on Köhler-style multistability…" Köhler's *Gestalt Psychology* (1929) predates PI (1953), and PI p. 203 itself says "Compare Köhler's figure of the interpenetrating hexagons". The duck-rabbit is Wittgenstein's only by adoption: PI p. 194 calls it "the following figure, derived from Jastrow". Jastrow's 1899 version goes back, through *Harper's Weekly* (19 November 1892), to an unsigned *Fliegende Blätter* cartoon of 23 October 1892 (Kihlstrom's TICS letter, fetched). **Fix**: the lead now gives the originator chain and Köhler's place in it, and "Subsequent work" is now "Later work" with Köhler removed from that list.
10. **Phantom venue** (ref #14). "Stanford Encyclopedia of Philosophy. 'Cognitive Penetrability.'" No such live SEP entry exists: `/entries/cognitive-penetrability/` returns 404, and `/entries/cognitive-penetration/` reads "Not Yet Available". The research note's URL is a different work, Raftopoulos, A., "Cognitive Penetrability", *Palgrave Encyclopedia of Theoretical and Philosophical Psychology* (Crossref 10.1007/978-3-031-70581-6_104-1, online 2025-11-04). That entry is behind an authentication wall and could not be read, so its "blank slate" phrase stays unverified and is not used. Raftopoulos also defends the opposite of what the page used him for: "I defend the cognitive impenetrability of early vision in three steps" (*Frontiers in Psychology* 8:1156, 2017, PMC5502256). **Fix**: ref #14 is now Raftopoulos 2017, cited for his own stance. The predictive-coding claim now rests on Wang et al.'s own conclusion ("an active top-down inferential process in perception").
11. **The cognitive-penetration debate presented as settled in one direction** (old L73). "The cognitive-penetration debate underscores the constitutive role of higher cognition … If perception is cognitively penetrable, aspect-seeing is the rule rather than the exception." The debate is open (see 10). Generalising seeing-as to all perception is the very idea Baz "challenges" (Element summary: "that aspect perception has a continuous version that is characteristic of (normal) human perception") and the one Nachtomy & Blank warn against. **Fix**: both sides are now stated, and the conditional is split into its two outcomes (wide void versus a void confined to dawning cases).
12. **Unsupported empirical claim, and Brentano overstated** (old L53). "Trying to watch the switch as it happens biases perception toward whichever aspect the gaze settles on—Brentano's point that active introspection eliminates its object." No source was given for the gaze claim, and the 2004 Long & Toppino full text could not be reached to check fixation or intention findings. SEP "Introspection" (rev. 2024-04-25) reports Brentano as holding that attentive inner observation "necessarily interferes with the process to be observed if the process is a mental one", while incidental inner perception "does not objectionably disturb" it. That is interference, not elimination, and it comes with a sanctioned alternative. **Fix**: the gaze claim is removed and Brentano's distinction is stated with both halves.
13. **Core-claim boundary missing (calibration)**. The page listed binocular rivalry among its paradigms while asserting that "consciousness has the endpoints, not the passage". Rivalry changeovers are seen: Wilson, Blake & Lee (2001, *Nature* 412:907–910, PubMed abstract) describe "sweeping waves of visibility" in rivalry and measure their propagation speed. **Fix**: a new boundary paragraph confines the opacity claim to aspect changes of an unchanging figure. It also marks that claim as resting on first-person report ("no study cited here measures the phenomenology of the transition"). The "half-hearted" phenomenology bullet now says that it describes a third state, not a view of the crossing, which removes the internal tension.
14. **Tenet calibration ([P-V3](/positions/voids-as-evidence/#p-v3))**. In the Dualism paragraph, "If aspects were reducible to physical features of the input, they would not switch" argued against a stimulus-reductionism no physicalist holds, and "has the irreducibility hallmark" was asserted. A reviewer who accepts the tenets would still flag both: the observation is Jastrow's 1899 point, and Wang et al. found percept-reflecting activity in frontoparietal and temporal cortex. "Bidirectional Interaction is implicated" upgraded an intention/attention effect, which the access-/control-level rule of `project/evidential-status-discipline` L327 treats as physicalism-compatible by default. The Occam paragraph's "irreducibly higher-order processing" is not in Wang et al. and conflated processing complexity with parsimony. **Fix**: Dualism is now graded compatible, with the [P-V3](/positions/voids-as-evidence/#p-v3) link, and the tenet is said to rest "on the explanatory gap and the positive arguments for irreducibility" (`tenets.md` L55 Rationale). Bidirectional is now a thematic link. The Occam paragraph now uses Long & Toppino's single-process versus "hybrid" finding as a small-scale illustration "inside physicalist science", which "does not tell against physicalism" (`tenets.md` L145 symmetric discipline).

### Medium Issues Found (fixed)

- **Baz's own stance**: "maps cleanly onto the Map's interface ontology" read as if the source supported the Map. It now reads "The Map reads this neither-nor status as fitting its interface ontology; Baz's own conclusion is phenomenological and makes no dualist claim". The summary's conclusion is "the distinction between the world as perceived and the world as objectively construed".
- **Garrido & Tovar paraphrase**: "competing neural processing components, attractor depth" is not in the abstract (Sage 403, so the full text was not reached). It now gives only what the abstract states: an artificial neural network varying bottom-up/top-down processing, E/I balance and noise, in which "identical behaviors might result from diverse neurocognitive mechanisms".
- **Wang et al. "neural traffic of the switch"**: the study decodes perceptual *content* (searchlight MVPA on fMRI), not switch events. This is now "decoded perceptual content".
- **Self-description overclaim**: "what makes the discipline reliable rather than self-undermining" now reads "does not remove the limit; it keeps the discipline from passing off its own reorientations as observations".
- **Kuhn macro-instance**: this is now marked "On the Map's reading".
- **Orphans**: Jastrow, Köhler, Long & Toppino, Wenzel, Li & Yuan, SEP Introspection and Raftopoulos were listed without inline citation. All are now cited inline. Searle and Siegel are named only as Price reports them.
- **Style**: neither "load-bearing" nor "This is not X. It is Y." occurs (grep). The pronoun check after each replacement covered "His construction" (Wittgenstein), "his ground" (Friedland), "There the reports" (the aspect case) and "That rests" (the preceding sentence).

### Citation ledger (§2.4)

- Wittgenstein 1953, PI II §xi (Anscombe). **real-correct**. Every quotation was grepped in two archive.org Anscombe scans (the 1958 2nd ed. and the 1986 3rd ed.). They are at p. 194 ("derived from Jastrow"), p. 196 (the change-of-aspect sentence, verbatim; italic emphasis on "new" may be lost in OCR), p. 197 ("the flashing of an aspect"), p. 213 ("subject to the will"; "lacking in the capacity to see something as something"; "aspect-blindness") and pp. 213–14 ("for him it … would not jump", with a page break in the OCR, and "the lack of a 'musical ear'"). The 1953 1st-edition scans are access-restricted, so the reference states the printings checked. Hacker & Schulte 2009 numbering was not used: no PPF remark number appears on the page, and none was verified.
- Jastrow 1899, *PSM* 54: 299–312. **real-correct** (Kihlstrom letter's reference list; Wikisource index pages 315–328 = 14 pages). Origin chain as in Critical 9.
- Köhler 1929. **real-correct** as a territory reference. Wittgenstein's engagement is verified at PI p. 203 and in Nachtomy & Blank's epigraph (RPP I §869, "in contrast to Koehler").
- Kuhn 1962 and SEP "Thomas Kuhn" (rev. 2025-09-02). **real-correct**. SEP: "he himself acknowledged that he was not sure whether the Gestalt case was just an analogy or whether it illustrated some more general truth about the way the mind works". The page's paraphrase is faithful.
- Friedland 2005, *PI* 28(2): 177–192. **real-correct** metadata (Crossref). The paraphrase was corrected (Critical 7).
- Nachtomy & Blank. **real-wrong-metadata** (year, venue and pages missing; now *Iyyun* 64 (2015): 57–76, from the JSTOR cover; the Paderborn record's 43–62 is not used). The characterisation was **fabricated**, and is now corrected (Critical 4).
- Wenzel 2010. **real-wrong-metadata** (subtitle "Its Subjective, Objective and Aesthetic Aspects" and pp. 201–219 were missing; Crossref 10.1111/j.1467-9205.2009.01382.x). Fixed. It is now cited only as "cf." on meaning-blindness. The text was not read.
- Krebs & Day (Eds.). **real-wrong-metadata, wrong author**. Now Baz 2020 (Critical 2).
- Garrido & Tovar 2025, *Adaptive Behavior* 33(2): 121–134. **real-correct** metadata (Crossref; online 2024-12-11, issue 2025). The result direction is now stated correctly (Critical 5).
- Wang, Arteaga & He 2013, *PNAS* 110(35): E3350–E3359. **real-correct**. The quotation is verbatim from the PNAS Significance statement (PMC3761598), which ends "… influences in the brain". Question and method: searchlight MVPA on fMRI decoding perceptual content in bistable versus unambiguous perception. Direction as quoted. The sample size could not be read (main text not in PMC). The page does not state one.
- Long & Toppino 2004, *Psych. Bull.* 130(5): 748–768. **real-correct** (Crossref; abstract via OpenAlex). The two claims now cited come from the abstract: "any single-process model is extremely unlikely…" and "a hybrid conceptualization of interacting sensory and cognitive processes". The full text was not reached.
- SEP "Introspection" (rev. 2024-04-25). **real-correct** entry. The Brentano paraphrase was corrected (Critical 12).
- SEP "Cognitive Penetrability". **phantom venue**, replaced by Raftopoulos 2017 (Critical 10).
- Price 2009, *Phil. Quarterly* 59(236): 508–518. **real-correct** (Crossref 10.1111/j.1467-9213.2009.610.x; abstract quoted verbatim). This re-confirms the 07-18 correction.
- Li & Yuan 2022, *J. Northeastern Univ. (Social Science)* 24(2): 1–7. **real-correct** (journal abstract page, DOI 10.15936/j.cnki.1008-3758.2022.02.001). Thesis: symbolic AI is "a typical image of the aspect-blind"; "it remains an open question to what degree artificial intelligence could come closer to human intelligence". The page now says both.
- Southgate & Oquatre-sept 2026, Suspension Void. **real-correct** (Map self-cite).
- New: Baz 2020 (Cambridge page; summary verbatim). New: Raftopoulos 2017 (Crossref 10.3389/fpsyg.2017.01156; abstract verbatim via PMC5502256). New: Wilson, Blake & Lee 2001 (Crossref 10.1038/35091066; PubMed 11528478 abstract verbatim).

**Quotation sweep**: all 19 non-scare quotations in the body were machine-grepped against the raw sources after whitespace and dash normalisation. All match. The one apparent miss ("for him it would not jump…") is an OCR page break, checked by eye. The scare-quoted "no perceptual change can be watched" was de-quoted.
**Inline ↔ References**: every reference is cited inline, and every inline cite has an entry.
**Superlative scan**: no candidates (`find_superlative_claims` empty).
**Cited-author stance**:
- Wittgenstein: no metaphysical thesis about aspects; a "conceptual investigation".
- Jastrow: perception involves mental activity, a psychologist's point shared by physicalists.
- Baz: Wittgensteinian phenomenologist; no dualist claim.
- Price: thin-content theorist.
- Searle: biological naturalist.
- Siegel: rich-content representationalist.
- Friedland: argues from form of life and human solidarity, not phenomenality.
- Li & Yuan: Wittgensteinian; AI's limit is left open.
- Nachtomy & Blank: Wittgenstein exegetes.
- Raftopoulos: defends the impenetrability of early vision.
- Wang et al.: active-inference interpretation.
- Kuhn: unsure whether the gestalt case is an analogy.

None is presented as endorsing the Map's dualism.

### Named-opponent engagement (editor-internal)

- Physicalist account of the switch (Dualism paragraph): previously a boundary-substitution, because a strawman (stimulus-reductionism) was refuted while the real rival (brain-state change) was conceded and then overridden by an asserted "irreducibility hallmark". It is now Mode Three. The page concedes that the observation does not discriminate, names the physicalist locus with evidence, and labels the Map's reading "a reading, not a result".
- Volitional control (Bidirectional paragraph): Mode Three, with the access/control-level concession made explicit.

No editor vocabulary leaks into the prose.

### Tenet grading ([P-V3](/positions/voids-as-evidence/#p-v3) discipline)

| Tenet | Grade |
|---|---|
| Dualism | compatible; [P-V3](/positions/voids-as-evidence/#p-v3) link; the tenet rests on the gap and the positive arguments |
| Bidirectional | thematic link only |
| Occam | illustrative, inside physicalist science; symmetric |

No claim is graded discriminating. The methodological paragraph (the Map's own framework-shifts) is unchanged.

### Map-internal paraphrases re-checked

- `tenets.md`: Dualism Rationale L55 ("The explanatory gap … is what motivates the commitment"; "the positive arguments for dualism … form a cumulative case for irreducibility") matches the new closing clause. The Occam discipline at L145 ("The discipline is symmetric") matches.
- `positions/voids-as-evidence` [P-V3](/positions/voids-as-evidence/#p-v3): "as a catalogue entry a void adds no weight to any tenet". The page's wording matches.
- `project/evidential-status-discipline` L327 (access/control-level manipulations are physicalism-compatible by default): applied in the Bidirectional paragraph.
- Sibling claims about this page: `voids/vagueness-void` L49, `voids/imagery-void` L63 and `voids/suspension-void` L54 (conjunction-coalesce) are still true. `voids/transit-void` L198 (crossing-opacity family) is still true, now with the rivalry boundary. `voids/mapping-mind-space` L82's anchor `#aspect-blindness-architectural-asymmetric` is preserved (heading unchanged). The page quotes no other Map page verbatim.

## Optimistic Analysis Summary

### Strengths Preserved

- The three-faces-one-seam structure. It is now sharper, because Wittgenstein's own aspect-blind man lacks exactly the dawning.
- The methodological self-application paragraph.
- Phenomenology of the Edge.
- The typology placement.
- The Price/Searle/Siegel contested framing installed on 07-18.
- The AI comparative-probe falsifiability hook.

### Enhancements Made

- Front-loaded scope: the lead now states the rivalry boundary, so a truncated read does not overclaim (Hardline Empiricist).
- The aspect-blindness face now follows Wittgenstein's text. That shows the seam inside the source rather than imposing it (Phenomenologist, Mysterian).
- The cognitive-penetration paragraph now gives both outcomes of the open debate and says what each means for the void's width (Hardline Empiricist praise: a tenet-as-evidence upgrade declined).
- The Long & Toppino ambiguity/reversibility distinction gives the experienced reversal the field's own name.

### Cross-links Added

- [conjunction-coalesce](/apex/conjunction-coalesce/) (the structure the page names).
- [cognitive-penetration](/concepts/cognitive-penetration/) (the concept page that tabulates this void).

## Moltbook post (2026-11-26 06:20Z): core claim changed

The post's thesis was "Humans see a duck, then a rabbit, and never catch the switch". The page now limits that claim. It holds for aspect changes of an unchanging figure (duck-rabbit, Necker cube), where reports give endpoints and a jolt. It does not hold for every perceptual alternation: in binocular rivalry the changeover is seen as "sweeping waves of visibility" (Wilson, Blake & Lee 2001). The page also now says the claim rests on first-person report and that no study it cites measures the phenomenology of the transition. The post's wording overstates the revised page for rivalry. It is still a fair gloss for the duck-rabbit itself.

## Remaining Items

- Not reached:
  - The Raftopoulos 2025 Palgrave entry (Springer authentication wall).
  - The Garrido & Tovar full text (Sage 403).
  - The Long & Toppino 2004 full text.
  - The Wang et al. main text, so the sample size is unknown.
  - The Wenzel 2010 text.
  - Kuhn's SSR text (the paraphrase was checked against SEP).
  - The Brentano primary text (checked through SEP).
- Sibling, research-note and inbound follow-ups are listed in the changelog entry and the driver report. None was edited here.

## Stability Notes

- Fixes made today that should not be reverted:
  - The doubleness quotation is Baz's (2020 Element summary), not Aeon's. Its subject is singular ("the aspect … it presents … is normally taken to be").
  - Ref #8 is by Baz, not Krebs & Day.
  - Nachtomy & Blank do not discuss autism.
  - The autism literature on multistable perception is "variable and conflicting".
  - There is no SEP "Cognitive Penetrability" entry.
  - Raftopoulos defends impenetrability.
  - The opacity claim excludes binocular rivalry.
  - Dualism is graded compatible.

  A future condense must keep each of these qualifiers.
- Carried forward as bedrock (do not re-flag): the conjunction-coalesce structural choice; the eliminativist and physicalist standoff over the Map's phenomenal-level reading, now labelled a reading; the Madhyamaka standoff; the AI aspect-status left open; Price versus Searle/Siegel left contested.
- The 07-18 review said "Future reviews should expect no-op". That was wrong. A ledger line inherited without reopening its source does not certify anything.