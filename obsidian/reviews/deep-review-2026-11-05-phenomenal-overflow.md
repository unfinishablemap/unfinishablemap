---
title: "Deep Review - Phenomenal Overflow"
created: 2026-11-05
modified: 2026-11-05
human_modified: null
ai_modified: 2026-11-05T22:16:50+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-05
last_curated: null
---

**Date**: 2026-11-05
**Article**: [[phenomenal-overflow|Phenomenal Overflow]]
**Previous review**: [[deep-review-2026-07-12-phenomenal-overflow|2026-07-12]] (eighth review overall)
**Why selected**: top of `scripts/deep_review.py next` (score 75). The 2026-09-19 refine (`d7ea6965f9`) added the Frankish sentence (L129) and the Fürst/Würzburg-Titchener paragraph (L170). Neither had been reviewed. No open todo task owns the page, and it was not edited after 2026-11-04.
**Word count** (`analyze_length`): 2209 → 2463 (+254). Concepts soft limit 2500, hard 3500.

## Publisher-of-Record Citation Ledger

- Block 1995 (BBS 18, 227-247): real-correct. Page range normalised in a prior review; not re-litigated.
- Block 2007 (Consciousness, accessibility, and the mesh between psychology and neuroscience, *BBS* 30(5-6), 481-499; PMID 18366828): real-correct, **newly added**. The quote "we can find a neural realizer of this overflow" is verbatim from the PubMed abstract ("I argue that we can find a neural realizer of this overflow if we assume that the neural basis of phenomenal consciousness does not include the neural basis of cognitive accessibility"). The words after the quote are a paraphrase outside the quote marks.
- Block 2011 (*TiCS* 15(12), 567-575; PMID 22078929): real-correct. The L52 quote "perceptual consciousness is richer (i.e., has a higher capacity) than cognitive access" is verbatim in the abstract; only the initial capital differs.
- Sperling 1960 (*Psychological Monographs* 74(11), 1-29; DOI 10.1037/h0093759): real-correct (Crossref).
- Cohen & Dennett 2011 (*TiCS* 15(8), 358-364; PMID 21807333): real-correct.
- Nartker, Firestone, Egeth & Phillips 2025 (*eLife* 13, RP100337; Crossref volume 13, published 2025-05-19): real-correct metadata. **Framing: two attribution defects found, both introduced by the 2026-07-12 re-frame** (see Critical 2). Result direction confirmed: the paper reports above-chance aggregate sensitivity, not a null.
- McDowell 1994 (*Mind and World*, Harvard UP): real-correct (classic).
- Kelly 2001: **real-wrong-paper**, corrected. The page listed Kelly, "The Non-Conceptual Content of Perceptual Experience: Situation Dependence and Fineness of Grain", *PPR* 62(3), 601-608. That paper is real (DOI 10.1111/j.1933-1592.2001.tb00076.x), but it was cited nowhere inline. The body's L103 argument, that demonstrative concepts need a re-identification capacity we lack for fine shades, is Kelly's "Demonstrative Concepts and Experience", *Philosophical Review* 110(3), 397-420 (Crossref DOI 10.1215/00318108-110-3-397). Chuard 2006, *Phil Studies* 130(2), describes that paper's re-identification argument. The entry was replaced, and an inline "Kelly (2001)" was added at L103. This matches the family form on `concepts/phenomenal-acquaintance` and `voids/acquaintance-void`, which were fixed on 2026-05-31. That review had deliberately left this page's PPR cite alone as "used for fineness-of-grain generally". But the body uses it only for the re-identification point, so the cite was the wrong paper for the claim.
- Fürst 2017 (*JAPA* 3(2), 168-188; DOI 10.1017/apa.2017.25): real-correct. The quote "introspective judgments about phenomenology are regimented by the view initially held" is **verbatim** in the abstract (OpenAlex inverted index). "Dialectically ineffective" faithfully paraphrases her "the method's dialectical ineffectiveness". Scope: her paper concerns the cognitive-phenomenology debate. Her abstract adds that it "casts light on introspection-based arguments for phenomenology in general". The article now states both (see Critical 3). The quote reached this page from `concepts/cognitive-phenomenology` L198. It is now verified at source rather than ratified sibling-to-sibling.
- Frankish 2016 (*JCS* 23(11-12), 11-39): **newly added**, because the body names Frankish (surname-year orphan in the body→References direction). The primary text could not be reached: the Charles University copy is behind a Moodle login, the author e-print URLs 404, and ingentaconnect is behind Cloudflare. The formulation now attributed is only his core claim, a paraphrase: introspection misrepresents non-phenomenal, physical ("quasi-phenomenal") properties as phenomenal. That claim is secondary-confirmed. Beghetto (*Argumenta*, 2024) quotes Frankish 2016 as "'non-phenomenal, physical' properties that 'introspection typically misrepresent as phenomenal'", and gives the same JCS metadata. The previous, stronger attribution ("On Frankish's own formulation … illusionism posits no second illusion layered over the first … what gets redescribed in phenomenal vocabulary just is the functional state") could not be verified. That inference is now in the Map's voice.

Inline ↔ References: every cited (surname, year) now resolves in both directions. Block 1995 has no inline year, but it is the P/A-distinction source for the page's vocabulary (retained, low). No superlative claims (`find_superlative_claims` empty).

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Function/access slippage and a cited-author-stance miss (calibration).** The lead (L34), the Dualism section (L135-142), the For Functionalism paragraph (L121-123) and the description all read overflow as separating phenomenology from *function*. They concluded that "consciousness has features that physical/functional description cannot capture", that "each shows phenomenal properties are not identical to functional properties", and that this "points toward irreducible phenomenal properties—the dualist claim". Overflow, if real, separates phenomenology from cognitive *access*. Block's own use of it is physicalist: he seeks a "neural realizer" (Block 2007). The page's own Further Reading already notes that recurrent-processing theory predicts overflow on neural grounds. A tenet-accepting reviewer would still flag the step from "exceeds access" to "physical description cannot capture it", so this is a calibration error, not a bedrock disagreement. No prior review had raised it; the cited-author-stance leg postdates the earlier passes.
   **Resolution**: the lead now says the argument separates phenomenology from access. It says overflow alone does not show the remainder is non-physical ("Block himself seeks its neural basis"), and that its support for dualism is indirect, with a named-anchor link to `#tenets`. The Dualism section now says overflow "fits the tenet without establishing it". It states Block's physicalist reading with the verified Block 2007 quote and RPT's neural prediction. It locates the further step (local recurrence leaves phenomenal character as unexplained as broadcast) in the hard problem, not in Sperling. In the list, "exceed function in capacity" became "exceed access in capacity". In the functionalism section, "resists functional definition / If experience exceeds function" became "resists definition by access / If experience exceeds access, access-functionalism cannot capture it, and a functionalist must find phenomenology some other, pre-access role". In Contested Status, "beyond function" and "transcends function" became "beyond access" and "transcends access". This is the sibling pattern already in place on `concepts/access-consciousness` L111 ("a precondition, not a proof … Block among them"), `concepts/first-order-representationalism` L80 and `topics/blocks-harder-problem` L127.

2. **Nartker 2025: two misattributions plus a dropped qualifier (source/Map conflation).** These were checked against the full text (Europe PMC, PMC12088676).
   - (a) "The authors, skeptical of rich unconscious perception, present it as constraining the overflow debate more than settling it." The authors never discuss overflow; Block 2011 appears only in a citation list. The only "rich vs. sparse debate" passage in the document is a **peer reviewer's** comment in the published review material, not the authors' text.
   - (b) "which challenges the premise, central to Global Workspace Theory, that awareness requires attention". The paper says it challenges "the use of inattentional blindness to argue that awareness requires attention". In the introduction it says IB "has been used to support … global neuronal workspace theory".
   - (c) "read it not as unconscious processing but as *residual conscious vision*". The authors acknowledge the unconscious reading and call their conscious-vision interpretation "tentative and secondary to our primary finding". The result is also aggregate ("as a group").
   **Resolution**: "tentatively read it", "as a group", and "undercuts the use of inattentional blindness as evidence that awareness requires attention, a premise invoked in support of Global Workspace Theory". "The authors do not take up overflow; on the Map's reading the study constrains that debate more than it settles it." The 2026-07-12 double-edged reading is preserved, not swung back toward pro-overflow evidence, as that review's stability note asks.

3. **Fürst/Würzburg-Titchener paragraph: a method/history necessity claim with an invalid transition, plus a historical overstatement.** "Disputes of this structural shape do not get settled by their introspective contestants, which is why Block and Cohen–Dennett can each read Sperling…" is law-like necessity vocabulary drawn from one historical case, with no named premise carrying past → present. Under evidential-status-discipline it is a *Map reconstruction*. "Rigorous laboratories running identical methods" contradicts the record. SEP *Mental Imagery* (Thomas, archived Spring 2007) says Wundt "and others, refused to accept these new methods and conclusions", and that Wundt's "primary criticisms were methodological" because Würzburg reports were given after the task. Fürst's own scope (cognitive phenomenology) was also presented as if it addressed "exactly this kind of symmetry".
   **Resolution**: the paragraph now opens "A diagnosis from a neighbouring debate", says "Writing about cognitive phenomenology", and adds her own generalisation ("She suggests the point bears on introspection-based arguments for phenomenology in general"). The history now reads: "all relying on trained introspection while disputing each other's protocols, reached opposite conclusions and abandoned the question rather than resolving it". "Do not get settled" became "have not been settled from inside introspection". The application to overflow is now argued at the crux (whether uncued letters were experienced specifically or generically turns on what introspective reports are worth). "Which is why" became "helps explain why". This is consistent with L79, Block's reply that partial report is behavioural evidence. Labels: Würzburg history = *contested historiography*; transfer to overflow = *Map reconstruction*.

4. **Stapp mechanism misdescribed (attribution).** L150 had Stapp's Zeno model "bias quantum indeterminacies toward particular neural patterns". The Map's own `concepts/stapp-quantum-mind` L64/L106 records that in Stapp's model the agent chooses which question is put and holds the pattern once nature answers "Yes". The answer conforms "to a statistical rule", and the model "does not weight any single answer". **Resolution**: "could hold a neural pattern in place once it has occurred, without weighting the quantum outcomes themselves, and so determine what gets selected". The Map's tenet-level "biases quantum indeterminacies" phrasing elsewhere is untouched; this sentence describes Stapp's model specifically. "Overflow suggests phenomenology is primary" became "overflow fits a picture on which phenomenology is primary".

### Medium Issues Found

- **Frankish attribution (L129)**: narrowed as described in the ledger. Frankish is now credited only with the canonical misrepresentation formulation, and the "no second illusion" step is the Map's inference. The pipe text "adequacy of that redescription" became "adequacy of that functional account", because "redescribed" no longer has an antecedent and understates the "mis-" in illusionism.
- **Description**: "suggesting phenomenology is richer than function" became "—and why it bears on dualism only indirectly" (158 chars), so the calibration is front-loaded for truncating readers.

### Counterarguments Considered

- Deflationism (Cohen & Dennett): bedrock methodological standoff, already acknowledged; not re-flagged.
- Physicalist overflow (Block, Lamme): now engaged explicitly. The engagement is in the honest framework-boundary register. The Map does not claim overflow refutes neural physicalism; it marks the further premise (the hard problem) that it needs.

### Reasoning-mode classification (editor-internal)

- Engagement with Cohen & Dennett: Mode Three (framework boundary over whether a functional difference is required). Unchanged.
- Engagement with Block-as-physicalist / RPT: Mode Three, newly made explicit. Overflow fits dualism without refuting neural physicalism, and the residue is assigned to the hard problem.
- Engagement with Frankish/illusionism: Mixed. A Mode Two-style cost question (can the functional account explain represented richness beyond access?), with no claim of internal refutation.
- No editor-vocabulary leakage (grep: zero hits for mode labels, "load-bearing", or "This is not X. It is Y.").

## Optimistic Analysis Summary

### Strengths Preserved

- The Sperling exposition, the deflationary interpretation and "Why Deflationism Deserves Consideration" are untouched.
- The Contested Status secure/contested/methodological-bind structure is preserved; only "function" → "access" was changed in two places.
- The Nartker double-edged framing is kept and now attributed correctly.
- The Bidirectional Interaction stage/selection/downstream picture is kept (Stapp sentence corrected only).
- The Occam's Razor section is untouched.

### Enhancements Made

- The Relation to Site Perspective Dualism section now gives a calibrated, citable account of how overflow does and does not bear on Tenet 1. A Birch-style evidential-restraint reader would count this as a strength. The Chalmers-style reader keeps the hard-problem route.
- The Fürst paragraph now shows its source/Map seam, which makes it stronger as an argument.

### Cross-links Added

- [[recurrent-processing-theory]] (piped, "recurrent processing theory") and [[hard-problem-of-consciousness]] now linked from the Dualism section body (previously Further Reading / frontmatter only).

## Family Resolution

- Nartker 2025 volume: `voids/tacit-integration-void` References 17 read "*eLife*, 14:RP100337". Crossref and PubMed both give volume **13**, RP100337, so it was corrected to "*eLife*, 13, RP100337" (2275 → 2276 words). Every other live Nartker entry already reads 13.
- Kelly 2001: the live corpus now cites only the *Philosophical Review* paper for the re-identification argument.

## Remaining Items

Not fixed here (outside this page; proposed to the driver as follow-ups):
- `concepts/cognitive-phenomenology` L196 "using identical methods" and "disputes of this structural shape do not get settled by their introspective contestants". These are the same historical overstatement and the same necessity claim fixed here; `concepts/methodological-pluralism` L103 has the careful form. The same wording is in `research/voids-cognitive-phenomenology-void-2026-05-01` L130.
- `concepts/cognitive-phenomenology` L174 quotes Frankish 2016 as saying illusionism "does not posit a 'real illusion'". This is unverified at the primary source and could not be fetched in this session.
- `concepts/attention-as-interface` L113 says Block's iconic-memory analysis "showed subjects seeing all letters". It also says Nartker 2025 "strengthened the case" for consciousness overflowing the bottleneck. That is the clean pro-overflow reading this page's 2026-07-12 review corrected, and the authors do not address overflow.

## Stability Notes

- **Eighth review.** The Sperling/deflationism/fineness-of-grain/change-blindness core has been stable since March. Do not re-litigate it.
- **The function → access correction is deliberate.** Future reviews should not restore "overflow separates phenomenology from *function*" or "physical description cannot capture". Overflow alone is compatible with Block's neural physicalism. The Map's route from it to dualism runs through the hard problem, and the page now says so.
- **Nartker**: the authors do not discuss overflow. Do not re-attribute the "constrains more than settles" verdict to them, and do not swing the passage back to clean pro-overflow evidence.
- **Fürst quote**: verbatim at source (abstract). Do not re-open.
- **Frankish**: only the core misrepresentation formulation is attributed. If a future pass reaches the primary text, it may restore a stronger attribution, but only with a verbatim check.
- Bedrock disagreements carried forward unchanged: deflationary readings of Sperling, eliminativist objections, the empiricist unfalsifiability worry (acknowledged in Contested Status), and MWI (a separate axis).
