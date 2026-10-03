---
ai_contribution: 100
ai_generated_date: 2026-10-03
ai_modified: 2026-10-03 12:12:15+00:00
ai_system: claude-opus-5-5
author: null
concepts:
- '[[type-a-type-b-and-type-c-physicalism]]'
- '[[phenomenal-concepts-strategy]]'
- '[[the-relocation-objection]]'
- '[[type-identity-theory]]'
- '[[explanatory-gap]]'
- '[[kripke-a-posteriori-necessity-argument]]'
- '[[conceivability-possibility-inference]]'
- '[[zombie-master-argument]]'
- '[[psychophysical-laws]]'
- '[[parsimony-epistemology]]'
- '[[inference-to-the-best-explanation-against-dualism]]'
- '[[russellian-monism]]'
created: 2026-10-03
date: &id001 2026-10-03
description: 'Research notes on Chalmers''s verdict that Type-B physicalism costs
  primitive identities or strong necessities: verified definitions, the identities-need-no-explanation
  exchange, Levine''s gappy identities, whether any other case exists, and what the
  cost does at the Map''s tiers.'
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-10-03 12:12:15+00:00
modified: *id001
related_articles:
- '[[tenets]]'
- '[[positions/methodology-and-calibration]]'
- '[[positions/arguments-for-dualism]]'
- '[[type-a-type-b-and-type-c-physicalism-2026-10-02]]'
title: 'Research: Primitive Identities and Strong Necessities'
topics:
- '[[hard-problem-of-consciousness]]'
- '[[arguments-against-materialism]]'
- '[[modal-structure-of-phenomenal-properties]]'
- '[[parsimony-case-for-interactionist-dualism]]'
---

# Research: Primitive Identities and Strong Necessities

**Date**: 2026-10-03
**Origin**: harvested P2 research-topic; source review `obsidian/reviews/optimistic-2026-10-02-physicalist-typing-wing.md` (§New Article Subjects, item 1). The task notes named the output `-2026-10-02.md`; the skill names research notes by run date, hence `-2026-10-03`.
**Search queries used**: none. The session's web-search budget was exhausted, so every source was reached by direct fetch: consc.net author texts (Chalmers 1999, 2003, 2010 draft; Chalmers & Jackson 2001); the Wayback capture (2015-12-31) of Block's NYU copy of the JSTOR scan of Block & Stalnaker 1999; davidpapineau.co.uk uploads (Papineau 1993, 1998, 2007, 2011; Goff & Papineau author's draft); the Google Books `SearchWithinVolume2` endpoint for Levine's *Purple Haze* (positive control "explanatory gap": 20 hits; negative control "zebra crossing": 0); SEP and IEP entries; Crossref and OpenAlex for metadata and abstracts. PhilPapers and the Philosophers' Imprint site returned Cloudflare challenges; the Google Books API quota was zero.
**Verification**: every quotation attributed to a fetched full text was re-checked by script against that text after whitespace normalisation. Levine quotations are checked against the snippet text the Google Books endpoint returned (page numbers from the endpoint). Hill & McLaughlin 1999 and Loar 1999 quotations are relayed by the SEP and are marked secondary.

## Verdict (assess-first)

**A new concept page is warranted, in the 2,300–2,700-word range for the prose, on two conditions.** It must lead with the distinction between ontological and epistemic primitiveness, which is the hinge of the whole exchange and which no Map page states; and it must report the Map's tier against Type-B as unchanged (*compatible*), with the cost argument filed as defeater-removal under [P-M1](/positions/methodology-and-calibration/#p-m1).

Why a page rather than another paragraph (lengths measured 2026-10-03 with `tools.curate.length.analyze_length`; concepts hard gate 3,500, topics 4,000, both `>=`):

- The identity half of the exchange already has **three parallel partial hosts** that do not cite one another: `topics/parsimony-case-for-interactionist-dualism` L75 ("Brute identity", 3,924 words, 75 of headroom), `concepts/the-relocation-objection` L78 and L84 (Block–Stalnaker–Papineau rival and the Chalmers–Jackson counter; 2,487, headroom 1,012), and `concepts/type-identity-theory` L71 (the "identities are brute" reply answered through Kripke's appearance/reality point; 2,322, headroom 1,177). Each runs a different counter. A single host stops the drift.
- The modal half (strong necessities) has **no host at all**. "Strong necessit" matches one live file, `concepts/counterfactual-reasoning`, in an unrelated sense; "modal dualism" and "non-derivation" match none.
- The routing page's row "Two-dimensional argument | B" points to `concepts/kripke-a-posteriori-necessity-argument`, which has 0 hits for "two-dimensional", "primary intension" or "secondary intension". The two-dimensional argument actually runs on `concepts/zombie-master-argument` L96–102 and `concepts/conceivability-possibility-inference` L84–94. The new page is the natural target for that row.
- Concepts stand at **342/360** by `tools.evolution.state.count_section_files("concepts")` (08:55Z), so a slot is available.

**License to decline, considered and rejected.** The relocation page could absorb ~400 words, but its scope is identity and constitution claims advanced by scientific theories of consciousness, and the modal half (strong necessities, modal monism) does not belong there. Declining would leave the Map's main argument against its live opponent split across three pages with three different counters and the strong-necessity half nowhere.

**What the page must not do.** It must not restate Chalmers's A/B/C taxonomy (the routing page owns it), must not re-run the zombie argument, must not claim that the cost lifts the Map's tier against Type-B, and must not repeat the zombie page's claim that the coincidence of primary and secondary intensions is the argument's key premise (Chalmers twice says it is inessential; see Corpus Seams).

## Executive Summary

Chalmers's verdict in "Consciousness and its Place in Nature" is that "the only remotely viable options for the materialist are type-A materialism and type-B materialism", at the cost of "denying the manifest explanandum in the first case, and embracing primitive identities or strong necessities in the second case". The disjunction tracks two formulations of Type-B. The identity formulation says phenomenal states *are* physical states; its cost is that the identity is **epistemically primitive**, not deducible from the complete physical truth, which elsewhere is the mark of a fundamental law. The necessitation formulation says only that the physical truth necessitates the phenomenal truth; its cost is that this necessity must be a **strong necessity**, an a posteriori necessity whose primary (epistemic) intension is itself necessary, unlike every Kripkean example.

The type-B rejoinder that "identities need no explanation" is verified in Papineau (1993, 1998, 2011) and in Block & Stalnaker (1999: "Identities don't have explanations"). Chalmers & Jackson (2001) answer that it "seems to conflate ontological and epistemological matters": "Identities are ontologically primitive, but they are not epistemically primitive." Levine's "gappy identity" is verified as his term (*Purple Haze*, 2001, p. 84): an identity claim for which a request for explanation is intelligible. Levine, whom Chalmers lists as type-B, concedes the psychophysical identity is gappy where water/H₂O is not, and holds this gives the anti-materialist "more ammunition" but "not quite enough to deal materialism a death blow".

On whether any identity or necessity outside consciousness is primitive in this sense, the anti-materialist's own catalogue (Chalmers 2010, fifteen candidates) finds no clear case; the hardest are unknowable mathematical truths and metamodal claims, neither a physical identity. The physicalist's strongest answer grants the uniqueness and denies that it is evidence: phenomenal concepts are unique, so uniqueness is predicted (Loar; Papineau), and metaphysical modality need not track conceivability at all (Goff & Papineau 2014). Schaffer (2017, abstract only) argues that such gaps are everywhere, bridged by principles of grounding.

For the Map: the cost establishes a **parity** result that Type-B largely concedes. The explanatory structure of Type-B "is just like the explanatory structure of property dualism" (Chalmers & Jackson), a physical component plus an epistemically primitive bridge. Whether the bridge is an identity or a law is then decided by analogy, by parsimony, and by the epistemology of modality. [Tenet 5](/tenets/#occams-limits) discounts the parsimony arguments on *both* sides, including Chalmers's own one-modal-primitive argument; analogy is answered by the predicted-uniqueness reply unless Chalmers's 2007 master argument succeeds; the epistemology-of-modality argument survives Tenet 5 but is a priori. **Type-B stays at *compatible*.** The cost removes a defeater (physicalism's claimed explanatory and parsimony advantage) and raises no tier.

## Terminology and Coinage

- **"Strong necessities" is Chalmers's label, introduced in the 1999 reply** ("Let us call these a posteriori necessities not explicable by the 2-D framework strong necessities."), shortening *The Conscious Mind*'s "strong metaphysical necessities" (1996, p. 136, by Chalmers's own report in the 1999 paper; Levine 2001, p. 55, independently attributes "strong metaphysical necessity" to Chalmers 1996). The book itself was not checked.
- **The definition.** 1999: "A strong necessity, by contrast, is an a posteriori necessity with a necessary primary intension." 2010: "an a posteriori necessity is a strong a posteriori necessity, or just a strong necessity, iff S has a necessary primary intension. Strong necessities are a posteriori necessities that are verified by all centered metaphysically possible worlds." Ordinary Kripkean necessities are **weak**: necessary secondary intension, contingent primary intension, so some world verifies their negation (the XYZ-world for "water is H2O").
- **The equivalence that matters for the Map.** Chalmers 2010: "It is easy to see that CP- is equivalent to the thesis that there are no strong necessities." Denying strong necessities *is* accepting the conceivability–possibility thesis in its negative form. So the strong-necessity cost and the two-dimensional argument are one dispute seen from two sides (see Map Relevance, [P-D1](/positions/arguments-for-dualism/#p-d1)).
- **"Primitive identity" is Chalmers's phrase in this sense** ("explanatorily primitive identities", 2003; "epistemically primitive", 2001 with Jackson). **Naming collision on the Map:** `topics/consciousness-and-the-metaphysics-of-individuation` L91 uses "Primitive identity" for Nida-Rümelin's primitive identity of conscious subjects, and cites Adams (1979) "Primitive Thisness and Primitive Identity". The new page must disambiguate in its first section.
- **Neutral vocabulary.** The SEP "Physicalism" entry (Stoljar, revision of 16 Sep 2026) distinguishes a **derivation view** of the necessary a posteriori (such truths "can be derived a priori from truths which are a posteriori and contingent") from a **non-derivation view** (there are "non-derived necessary a posteriori truths"), and concludes that "if one wants to defend a posteriori physicalism, one will have to defend the non-derivation view of the necessary a posteriori. However, the non-derivation view is controversial". The derivation/non-derivation pair maps onto weak/strong necessity without the two-dimensional machinery.
- **"Gappy identity" is Levine's term**, introduced in *Purple Haze* (OUP 2001), section "Gappy Identities" from p. 81; the index runs "gappy identity, 81, 84-94, 111, 146, 151, 163-166". On p. 84 he calls an identity that supports an "intelligible request for explanation a "gappy identity."" (the snippet begins mid-sentence), and on p. 163: "a gappy identity claim is one for which a request for explanation is intelligible." Whether the term occurs earlier in Levine's work (for example his 1998 *Noûs* paper) was not checked.
- **Levine's own taxonomy cuts the type-B camp in two** (p. 50): "exceptionalists" (E-type), who grant "that the framework developed by the anti-materialist for handling the standard cases of a posteriori necessities is the right one" but hold qualia special, and "non-exceptionalists" (NE-type), who reject the general semantic account. Loar is the paradigm exceptionalist; Block & Stalnaker are non-exceptionalists. The page can use this pair to sort the replies.
- **"New wave materialism" is a critics' label.** Horgan & Tienson's "Deconstructing New Wave Materialism" (2001, CUP, pp. 307–318) opens by describing how "A new wave of materialists has appeared on the scene with a new strategy for explaining the a posteriori na[ture]…" of mind–brain identities (OpenAlex/Cambridge opening text, truncated there). McLaughlin's "In Defense of New Wave Materialism: A Response to Horgan and Tienson" (same volume, pp. 319–330) adopts it. Brief McLaughlin as a holder, not the coiner. His opening defends the type identity thesis as what "would offer the best explanation of the correlation thesis", the abductive route.
- **"Theft over honest toil"** is Russell's (1919), used by Chalmers without attribution (already verified in the 2026-10-02 research note).

## Key Sources

### Chalmers, "Consciousness and its Place in Nature" (2003)
- **URL**: https://consc.net/papers/nature.html ; DOI 10.1002/9780470998762.ch5 (Stich & Warfield eds., *Blackwell Guide to Philosophy of Mind*, pp. 102–142)
- **Type**: Book chapter
- **Access**: full text (author's version)
- **Key points**:
  - The type-B materialist "must hold that the identification between consciousness and physical or functional states is epistemically primitive: the identity is not deducible from the complete physical truth."
  - The cost argument: "the type-B materialist recognizes a principle that has the epistemic status of a fundamental law, but gives it the ontological status of an identity", and "fundamental laws always connect distinct properties". "Unless there is an independent case for primitive identities, the suggestion will seem at best ad hoc and mysterious, and at worst incoherent."
  - Three type-B replies sorted: Papineau 1993 ("identities do not need to be explained, so are always primitive"), Block and Stalnaker 1999 (even water and genes are not deducible), Loar 1990/1997 (uniqueness explained by "unique features of the concept of consciousness"), which Chalmers calls "perhaps the most interesting".
  - The necessitation formulation appeals to Kripke, "though it should be noted that Kripke himself denies this claim".
  - Thesis (ii) of the two-dimensional argument (a conceivable statement is verified by some world) is "the only hope for the type-B materialist" to deny. The coincidence of primary and secondary intensions for phenomenal concepts is flagged as optional: "(This claim is not required for the argument to go through, but it is plausible and makes things more straightforward.)"
  - Closing judgement: "Overall, my own view is that there is little reason to think that explanatorily primitive identities or strong necessities exist." Ruling them out yields "a disjunction" of type-D, type-E and type-F.
- **Tenet alignment**: Aligns with Tenet 1; leaves D/E/F undecided, so gives no specific support to Tenets 2–3.
- **Quote**: "By labeling these principles identities or necessities rather than laws, the view may preserve the letter of materialism; but by requiring primitive bridging principles, it sacrifices much of materialism's spirit."

### Chalmers, "Materialism and the Metaphysics of Modality" (1999)
- **URL**: https://consc.net/papers/modality.html ; DOI 10.2307/2653685 (*Philosophy and Phenomenological Research* 59(2); Crossref first page 473; the author's header gives 473–93)
- **Type**: Journal article; reply to the PPR symposium on *The Conscious Mind* (Hill & McLaughlin, Loar, Shoemaker, Yablo)
- **Access**: full text (author's version)
- **Key points**:
  - §3.3 lists six charges against strong necessities: no analogy; a more radical necessity than Kripke's, "requiring a distinction between logical and metaphysical possibility at the level of worlds"; "an ad hoc proliferation of modalities"; "deep questions of coherence"; "brute and inexplicable"; and "the only motivation to postulate such necessities is the desire to save materialism".
  - On analogy: "Loar accepts explicitly that there are no other counterexamples to the 2-D model: he thinks that psychophysical necessities are sui generis. Hill & McLaughlin appear to accept the same thing." Shoemaker's necessary laws and Yablo's necessary god are rejected as candidates.
  - §3.4 on explanations: Hill & McLaughlin explain only why zombies are conceivable ("There will always be a cognitive explanation of a modal intuition!"); a successful explanation "has to show us why a state-of-affairs should be conceivable while at the same time being impossible". Loar's account "presupposes strong psychophysical necessities".
  - §3.5 modal rationalism: admitting strong necessities is "modal dualism", which "requires two modal primitives"; the second "is a primitive that answers to no-one and does no work".
  - §3.5 concedes that "the position remains at least formally open"; §3.6 records that type-B "will (in effect) accept my conclusions about explanation. It remains the case that crossing the gap requires epistemically primitive bridging principles."
  - §3.1: the coincidence of intensions for phenomenal concepts "is inessential to the argument".
- **Tenet alignment**: Aligns with Tenet 1. Its main weapon against modal dualism is partly a parsimony argument, which [Tenet 5](/tenets/#occams-limits) discounts (see Map Relevance).
- **Quote**: "These principles will be called "identities" or "necessities" rather than "laws", but their role in a theory will be much the same."

### Chalmers & Jackson, "Conceptual Analysis and Reductive Explanation" (2001)
- **URL**: https://consc.net/papers/analysis.html ; DOI 10.1215/00318108-110-3-315 (*Philosophical Review* 110(3): 315–360 per Crossref; author's header gives 315–61)
- **Type**: Journal article; in part a reply to Block & Stalnaker 1999
- **Access**: full text (author's version)
- **Key points**:
  - The entailment base is **PQTI** (physical, phenomenal, "that's all" and indexical truths), not microphysics alone. Macroscopic truths and the water, heat and gene identities are claimed to be "implied by PQTI". Because Q is in the base, ordinary phenomena are reductively explainable "modulo phenomenology". The page should not report the claim as "derivable from physics alone".
  - The core reply: "It is sometimes held that "identities do not need to be explained" (e.g. Papineau 1993). Block and Stalnaker say something similar ("Identities don't have explanations"). But this seems to conflate ontological and epistemological matters. Identities are ontologically primitive, but they are not epistemically primitive."
  - Parity: on type-B, psychophysical identities "are inferred from regularities between brain processes and consciousness, in order to systematize and explain those regularities"; "Ontologically, these identities may differ from laws. But epistemically, they are just like laws."
  - The law-mark premise (§7): "what it is to be a fundamental law of nature is precisely to be an objective, epistemically primitive counterfactual-supporting regularity".
  - Footnote on warrant: "In the absence of warrant to accept such deducibility, scientists will only be warranted in accepting correlation, not identity."
- **Tenet alignment**: Aligns with Tenet 1.
- **Quote**: "But the explanatory structure of this materialist view is just like the explanatory structure of property dualism."

### Chalmers, "The Two-Dimensional Argument Against Materialism" (2009/2010)
- **URL**: https://consc.net/papers/2dargument.html ; DOI 10.1093/acprof:oso/9780195311105.003.0006 (*The Character of Consciousness*, OUP 2010, pp. 141–206 per Crossref); abridged in *The Oxford Handbook of Philosophy of Mind* (2009), pp. 313–336, DOI 10.1093/oxfordhb/9780199262618.003.0019
- **Type**: Book chapter
- **Access**: full text of the author's pre-publication version (it still carries "(??)" citation placeholders), so wording may differ from the printed chapter
- **Key points**:
  - §7 defines weak and strong a posteriori necessities and proves the equivalence with CP- (above).
  - §8 audits fifteen putative strong necessities: Kripke cases (Cicero/Tully), essential modes of presentation, homophonous expressions, demonstratives, dancing qualia, ordinary macroscopic truths, unknowable mathematical truths, inscrutable truths, the deeply contingent a priori, disquotational truths, response-enabled concepts, laws of nature, a necessary God, metamodal claims, and the conceivability of materialism. Verdict: "Perhaps the most serious challenges come from mathematical cases such as the Continuum Hypothesis and from metamodal cases"; even these are cases "where the initial situation is unclear, rather than cases where there is a clear counterexample".
  - §9 calls the phenomenal-concept explanation of uniqueness "the most interesting and attractive strategy for the defense of type-B materialism", and refers it to the 2007 master argument.
  - §10 adds an epistemological argument distinct from parsimony: if metaphysical modality is an independent primitive, "it becomes quite unclear why conceivability should be any guide to it at all? Why should not there be just one metaphysically possible world, or 37?" But it also leans on simplicity: grounding metaphysical in logical modality "yields a simple explanation, and a simple epistemology".
- **Tenet alignment**: Aligns with Tenet 1; the §10 simplicity strand is exposed to Tenet 5.

### Block & Stalnaker, "Conceptual Analysis, Dualism, and the Explanatory Gap" (1999)
- **URL**: http://web.archive.org/web/20151231074138/http://www.nyu.edu/gsas/dept/philo/faculty/block/papers/ExplanatoryGap.pdf ; DOI 10.2307/2998259 (*Philosophical Review* 108(1): 1–46; the JSTOR cover sheet gives pp. 1-46; Crossref records first page only)
- **Type**: Journal article
- **Access**: full text (JSTOR scan with OCR; some words split by OCR spacing, verified after normalisation)
- **Key points**:
  - Identities are justified abductively: identities "allow a transfer of explanatory and causal force not allowed by mere correlations", so "we are justified by the principle of inference to the best explanation in inferring that these identities are true" (p. 24).
  - The Mark Twain/Samuel Clemens case (p. 24): "it does not make the same kind of sense to ask for an explanation of the identity. Identities don't have explanations (though of course there are explanations of how the two terms can denote the same thing). The role of identities is to disallow some questions and allow others." Their footnote 6: "One of us heard this story somewhere, but we don't know where". Papineau 1993 n. 16 says Block told it to him.
  - Non-exceptionalism (p. 29): "the facts about water are not a priori entailed by the microphysical facts either", so the zombie thought experiments "don't show any disanalogy between the concept of consciousness and the concept of water". The psychophysical identity would be justified "By using the kinds of methodological consideration sketched in our discussion of simplicity above", the same as for water = H2O.
  - A concession the page should use (p. 29): "(Note that we are not saying that the identity closes the gap all by itself.)"
  - On two-dimensionalism (p. 38): "why do we not have equal justification to assume that it might be a microphysical truth about the actual world that pyramidal cell activity is the satisfier of the primary intension of 'consciousness'?"
- **Tenet alignment**: Conflicts with Tenet 1. Its justification of the identity is explicitly a simplicity/IBE inference, the point where [Tenet 5](/tenets/#occams-limits) reaches it.

### Papineau: 1993, 1998, 2011 (the "identities need no explanation" line)
- **URLs**: https://www.davidpapineau.co.uk/uploads/1/8/5/5/18551740/physicalism_consciousness_and_the_antipathetic_fallacy.pdf ; .../nous_-_2002_-_papineau_-_mind_the_gap.pdf ; .../explanatorygappdf.pdf
- **Metadata**: 1993 *Australasian Journal of Philosophy* 71(2): 169–183, DOI 10.1080/00048409312345182; 1998 "Mind the Gap", *Philosophical Perspectives* 12: 373–388, DOI 10.1111/0029-4624.32.s12.16 (the upload's filename says "nous 2002", but the PDF header and Crossref give *Phil. Perspectives* 12, 1998); 2011 "What Exactly is the Explanatory Gap?", *Philosophia* 39(1): 5–19, DOI 10.1007/s11406-010-9273-6
- **Type**: Journal articles
- **Access**: full text (publisher PDFs as uploaded by the author)
- **Key points**:
  - 1993, p. 180: "If they were, they were, and there's an end on it." and "If they really are the same thing, then we can't explain why they are the same thing." This is the passage Chalmers cites.
  - 1998, §6 "Identities Need no Explaining", p. 379: "If they are C-fibre firings, they don't "arise" from them, they are them, and that's it." §7 grants a sense in which identities flanked by a description get explained ("we are explaining why it satisfies some description"), which is the opening Chalmers–Jackson exploit.
  - 2011, p. 9: "Identities need no explanation. Identities are necessary. They could not have been otherwise. So they are not the kind of fact that calls for explanation." Also against Jackson: "Identities can be evidenced more directly in a number of ways. We might simply observe that the two kinds at issue co-occur."
  - *Thinking about Consciousness* (2002), ch. 5 "The Explanatory Gap", pp. 141–160 (DOI 10.1093/0199243824.003.0006): **metadata only**. The relocation page cites 2002 for the claim; the verified loci are 1993, 1998 and 2011.
- **Tenet alignment**: Conflicts with Tenet 1.

### Goff & Papineau, "What's Wrong with Strong Necessities?" (2014)
- **URL**: https://www.davidpapineau.co.uk/uploads/1/8/5/5/18551740/whats_wrong_with_strong_necessities_as_of_jan__2013.docx ; DOI 10.1007/s11098-013-0195-6 (*Philosophical Studies* 167(3): 749–762; online 2013-09-04, issue February 2014)
- **Type**: Journal article, co-written, splitting into two single-author halves
- **Access**: full text of the author's draft dated January 2013; published wording not checked
- **Key points**:
  - The case-by-case debate is "inevitably inconclusive", and even universal agreement that there are no strong necessities elsewhere would not settle it: "Why shouldn't it still be open to a posteriori physicalists to hold that mind-brain necessities are an exception?"
  - Strong necessities arise from "radically opaque" terms: a term is radically opaque "if and only if it does not reveal any substantive information about its referent"; "Cicero is Tully" is offered as a possible case.
  - Goff's half: "stress-free modal dualism" defines metaphysical possibility as conceivability under a *transparent* conception, so two modal spaces need no primitive metaphysical modality. Goff, a panpsychist critic of physicalism, uses this to argue *against* physicalism if phenomenal concepts are transparent (Goff 2011).
  - Papineau's half: "I shall defend strong necessities by arguing that metaphysical modality has nothing to do with conceivability"; modality is "grounded in counterfactual thinking", geared to causal structure. His father/birthplace case argues that de re necessities are not grounded in conceivability.
  - Both report Chalmers's argument against modal dualism as a simplicity argument ("this would lose the simplicity of the uniform explanation").
- **Tenet alignment**: Papineau's half conflicts with Tenet 1; Goff's half is a dualist route that runs through transparency rather than modal rationalism.

### Levine, *Purple Haze: The Puzzle of Consciousness* (2001)
- **URL**: https://books.google.co.uk/books?id=RR4SDAAAQBAJ (also live: `g4svYoFDAkwC`); DOI 10.1093/0195132351.001.0001 (OUP; Crossref date 2001-01-18)
- **Type**: Monograph
- **Access**: snippet-level via Google Books search-within (verbatim snippets with page numbers; not continuous text)
- **Key points**:
  - p. 81: "I generally endorse the claim that pure identities are not suitable candidates for explanation. Yet, when we look more closely, it seems that things are not quite so straightforward." There is "a sharp epistemic contrast between various standard cases of identity claims and the case of an identity claim like (3) R = B".
  - p. 86: does gappy identity "give the anti-materialist more ammunition for her metaphysical conclusion? I think so, but not quite enough to deal materialism a death blow."
  - p. 91: "In cases of non-gappy identities, such as "water = H2O," while there is no a priori route from the "H2O"-described facts to the "water"-described facts, still there is the definite sense that when all the chemical facts are in, the whole …" (snippet ends there). So Levine agrees with Block & Stalnaker that there is no a priori route for water, yet locates the difference in gappiness.
  - p. 151: "Gappy identities, I argued, involve representations that express substantive, determinate modes of presentation, quite different from the "presentationally thin" contents associated with terms like "water.""
  - p. 88 extends the argument into "gappy psycho-physical identities as bridge principles", turning "the materialist's own argument against her".
  - pp. 55–58 discuss Chalmers's "strong metaphysical necessity" directly.
- **Tenet alignment**: Neutral to mildly aligned with Tenet 1. Levine is on Chalmers's type-B list and remains a materialist, but concedes the explanatory asymmetry.
- **Bibliographic flag**: Chalmers 2003's reference list gives "Levine, J. 2000. Purple Haze: The Puzzle of Conscious Experience. MIT Press." The book is OUP, 2001, subtitled *The Puzzle of Consciousness* (Crossref; Google Books title). The Map's `concepts/explanatory-gap` reference (L233) is correct; do not copy Chalmers's entry.

### Weisberg, "Hard Problem of Consciousness" (IEP)
- **URL**: https://iep.utm.edu/hard-problem-of-conciousness/
- **Type**: Encyclopedia
- **Access**: full text
- **Key points**: The "weak reductionism" family (cited: Block 2002, Block & Stalnaker 1999, Hill 1997, Loar 1997, 1999, Papineau 1993, 2002, Perry 2001) rests the identity on "the most parsimonious and productive theory"; "Identities have no explanation: a thing just is what it is." The entry then runs its own version of the cost argument: "We are asked to accept a brute identity here, one that seems unprecedented in our ontology given that consciousness is a macro-level phenomenon. Other examples of such brute identity—of electricity and magnetism into one force, say—occur at the foundational level of physics." Its fallback for the weak reductionist is causal closure.
- **Tenet alignment**: Neutral survey; the cost passage aligns with Tenet 1.

### Supporting sources (verified at the level stated)
- **SEP "Physicalism"** (Stoljar; revision of 16 Sep 2026; full text): the derivation/non-derivation distinction, quoted above.
- **SEP "Zombies"** (Kirk; revision of 25 Mar 2023; full text): §5.1 relays Hill & McLaughlin 1999, p. 446: "Given psychophysical identities, it is an 'a posteriori' fact that any physical duplicate of our world is exactly like ours in respect of positive facts about sensory states" (secondary). §5.2 relays Loar 1999, p. 467: "it is fair of the physicalist to request a justification of the assumption that conceptually distinct concepts must express metaphysically distinct properties" (secondary). Page range for the Chalmers 2010 chapter given there as 141–205; Crossref gives 141–206.
- **Hill & McLaughlin 1999**, PPR 59(2): 445–, DOI 10.2307/2653682 (metadata only). **Hill 1997**, *Philosophical Studies* 87(1): 61–85, DOI 10.1023/A:1017911200883 (metadata only). **Loar 1990**, *Philosophical Perspectives* 4: 81–, DOI 10.2307/2214188 (metadata only; revised 1997).
- **Goff 2011**, "A Posteriori Physicalists Get Our Phenomenal Concepts Wrong", *Australasian Journal of Philosophy* 89(2): 191–209, DOI 10.1080/00048401003649617 (abstract): the physicalism of Papineau and Loar "departs from common sense in holding that our phenomenal concept of pain is opaque"; Goff's claim is that "phenomenal concepts are not opaque". **Díaz-León 2014** (online 2013), *Ratio* 27(1): 1–16, DOI 10.1111/rati.12018 (abstract): replies that a posteriori physicalists can explain how phenomenal concepts "reveal at least something" of their referents.
- **Schaffer 2017**, "The Ground Between the Gaps", *Philosophers' Imprint* 17(11) (volume and number from the Michigan handle 2027/spo.3521354.0017.011; abstract via OpenAlex W2908008164; full text blocked): gaps "are pervasive, lurking in the transition from the physical to the chemical and in every concrete transition from more to less fundamental", and are "unproblematic, so long as they are bridged by substantive principles of metaphysical grounding" ("ground physicalism"). Abstract only. Do not attribute any argument beyond the abstract.
- **Papineau 2007**, "Kripke's Proof Is Ad Hominem Not Two-Dimensional", *Philosophical Perspectives* 21: 475–494, DOI 10.1111/j.1520-8583.2007.00133.x (full text fetched, not read beyond locating the thesis): cited by Goff & Papineau for the claim that Kripke "was perfectly open to the possibility of strong necessities involving radically opaque terms". Chalmers 2003 says the opposite of Kripke on P⊃Q. Report both readings; do not adjudicate Kripke.

## Major Positions

### Primitive-identity type-B (identity formulation)
- **Proponents**: Papineau (1993, 1998, 2002, 2011); Block & Stalnaker (1999); McLaughlin (2001); the IEP's "weak reductionism".
- **Core claim**: phenomenal properties are identical to physical or functional properties; the identity is known a posteriori and justified by its explanatory and causal payoff; it needs no explanation because identities never do.
- **Key arguments**: identities are necessary and so not the kind of fact that calls for explanation; the identity is the best explanation of psychophysical correlation; mental causation requires it, given causal closure.
- **Relation to site tenets**: conflicts with Tenet 1. The parsimony half of its justification meets [Tenet 5](/tenets/#occams-limits); the causal half rests on closure, which [Tenet 2](/tenets/#minimal-quantum-interaction) denies at quantum indeterminacy. Both are defeater-removals.

### Strong-necessity type-B (necessitation formulation; Levine's "exceptionalists")
- **Proponents**: Loar (1990/1997, 1999); Hill & McLaughlin (1999); Balog (on Chalmers & Jackson's reading, n. on sui generis necessities); Papineau's half of Goff & Papineau.
- **Core claim**: P⊃Q is necessary but a posteriori, and unlike Kripke's examples its primary intension is necessary too. The case is sui generis because phenomenal concepts are sui generis.
- **Key arguments**: phenomenal concepts are recognitional and express the properties they refer to (Loar); separate cognitive faculties explain zombie conceivability (Hill & McLaughlin); metaphysical modality tracks causal structure, not conceivability (Papineau).
- **Relation to site tenets**: conflicts with Tenet 1. Chalmers's 2007 master argument is the reply that reaches the concept-based explanation.

### Non-exceptionalist type-B
- **Proponents**: Block & Stalnaker (1999); Levine's NE-type.
- **Core claim**: no macroscopic identity is a priori entailed by microphysics, so the psychophysical case is not special.
- **Relation to site tenets**: conflicts with Tenet 1. It is answered by Chalmers & Jackson's PQTI entailment thesis and by Levine's observation that water is non-gappy even without an a priori route.

### Anti-materialist (Chalmers; Chalmers & Jackson)
- **Core claim**: there are no epistemically primitive identities or strong necessities among natural phenomena; an epistemically primitive connection is a fundamental law; fundamental laws connect distinct properties; so the psychophysical bridge is a law and consciousness is not physical (unless type-F).
- **Relation to site tenets**: aligns with Tenet 1. It supports type-D, type-E and type-F *alike*, so it gives no specific support to Tenets 2–3.

### Ground physicalism (Schaffer 2017; abstract only)
- **Core claim**: explanatory gaps are pervasive across levels and are bridged by principles of grounding, so the psychophysical gap is not special.
- **Relation to site tenets**: conflicts with Tenet 1, but concedes Chalmers's cost in a generalised form: a primitive bridging principle at every level.

## Key Debates

### 1. Do identities need explanation?
- **Sides**: Papineau, Block & Stalnaker and the IEP gloss say no; Chalmers & Jackson say the question conflates two kinds of primitiveness; Levine says pure identities need none, but some identity claims are "gappy".
- **Core disagreement**: whether "no explanation of *why* a = a" (ontological) also licenses "no derivation of *that* a = b from the underlying truths" (epistemic). Chalmers & Jackson concede the first and deny the second.
- **Current state**: the ontological point is common ground, so the page should grant it. The live dispute is whether epistemic primitiveness is a mark of lawhood.

### 2. Is there any other case?
- **Sides**: Chalmers (1999, 2003, 2010) and the IEP say no clear case exists; Block & Stalnaker say even water is not derivable; Goff & Papineau say cases are inconclusive and beside the point; Schaffer says gaps are everywhere.
- **Current state**: no uncontested physical identity or necessity of the strong kind has been produced. Loar and (per Chalmers) Hill & McLaughlin concede the psychophysical case is sui generis. See next section.

### 3. Can the uniqueness be explained without dualism?
- **Sides**: Loar, Hill & McLaughlin, Papineau and the phenomenal-concepts strategy generally say yes; Chalmers (1999 §3.4; 2007 master argument) says every such explanation either explains only the conceivability or presupposes the necessity.
- **Core disagreement**: whether an explanation of why the identity *seems* contingent also explains why the appearance is *unreliable*. Chalmers: "an explanation of a strong necessity has to do two things".
- **Current state**: ongoing; this is the point on which the cost argument ultimately depends (see Map Relevance).

### 4. Must metaphysical modality track conceivability?
- **Sides**: Chalmers (modal rationalism, one modal primitive); Papineau (modality grounded in counterfactual and causal thinking); Goff (two spaces, both defined epistemically; strong necessities possible, but phenomenal transparency may still defeat physicalism).
- **Core disagreement**: whether a second modal space is an unexplained primitive (Chalmers) or has an explanation that does not run through conceivability (Papineau).
- **Current state**: ongoing, and the most fundamental of the four. Chalmers's case has a parsimony strand ("one modal primitive … gives us everything") and an epistemological strand ("Why should not there be just one metaphysically possible world, or 37?").

## Is Any Identity Outside Consciousness Primitive?

Research question 4, answered by source:

| Candidate | Proposed by | Status after the exchange |
|---|---|---|
| Water/H₂O, heat/molecular motion, genes/DNA | Block & Stalnaker (not a priori entailed by microphysics) | Chalmers & Jackson: implied by PQTI, Q included. Levine: no a priori route, yet "non-gappy". Not a strong necessity on any party's account. |
| Cicero = Tully (radically opaque names) | Goff & Papineau; Chalmers 2010 §8 case (1) | Chalmers: a world where the two causal chains pick out different people verifies "Cicero is not Tully". Goff & Papineau: the case debate is "inevitably inconclusive". Not physical in any case. |
| Laws of nature, if metaphysically necessary | Shoemaker | Chalmers: "at least as tendentious as psychophysical necessities (and far less widely accepted)". |
| A necessary God; metamodal claims | Yablo | Chalmers denies a necessarily existing god is ideally conceivable; ranks metamodal cases among the most serious. Not physical. |
| Unknowable mathematical truths (Continuum Hypothesis) | Chalmers 2010 §8 (7)–(8) | The most serious challenge by Chalmers's own ranking; "inscrutable" truths open no gap between conceivable and possible *worlds*. Not physical. |
| Electricity and magnetism as one force | IEP (Weisberg) | The IEP's example of a brute identity, at "the foundational level of physics", which is the point of its contrast with a macro-level phenomenon. |
| Physical-to-chemical transitions | Schaffer 2017 (abstract) | Gaps "pervasive", bridged by grounding principles. Contested, and concedes a primitive bridging principle at every level. |

**Finding.** No source supplies an uncontested *physical, non-fundamental* identity or necessity that is epistemically primitive in Chalmers's sense. The "no other case" claim survives as a description of the literature. **Its evidential weight is small**, because the strongest physicalist answer predicts it.

**The strongest physicalist answer.** Grant the uniqueness and deny it is evidence. Phenomenal concepts are the only concepts that are, in Loar's terms, recognitional while presenting their referent non-contingently, or, in Goff & Papineau's terms, radically opaque about a referent picked out by another radically opaque concept; so the one case of gappiness is where the one anomalous concept type occurs. Add Papineau's denial that metaphysical modality is answerable to conceivability, which removes the modal-rationalist ground for calling the second modal space ad hoc. On this combined answer the absence of other cases is what Type-B predicts, and the likelihood ratio on "no other case" is close to one. It departs from one only if Chalmers's master argument shows that no concept-based explanation can account for why the appearance of contingency is unreliable. That is why the cost argument cannot stand alone.

## Map Relevance: What the Cost Does at the Map's Evidential Tiers

Research question 5. The routing page keeps Type-B at *compatible* and says only "a second-order comparison favouring dualism by stated criteria would lift it to suggestive". [P-M1](/positions/methodology-and-calibration/#p-m1): "defeater-removal never raises the evidential tier of a claim."

**What the cost establishes, at the level Type-B concedes.** On the explanation register, Type-B and property dualism have the same structure: a physical component plus an epistemically primitive psychophysical bridge. Chalmers & Jackson state it, Chalmers 1999 reports that type-B "will (in effect) accept my conclusions about explanation", Block & Stalnaker write that they are "not saying that the identity closes the gap all by itself", and Levine concedes the identity is gappy. Call this the **parity result**. It removes a defeater: the claim that physicalism enjoys, on consciousness, the explanatory advantage it enjoys for water, heat and genes. That defeater is real in the literature, since the IEP's weak reductionist rests the identity on "the most parsimonious and productive theory".

**What decides between "identity" and "law" once parity is granted.**

1. *Analogy* (every other epistemically primitive regularity is a law; every other identity is derivable). This is the cost argument proper. Type-B grants the disanalogy and predicts it from phenomenal concepts, so analogy discriminates only if the 2007 master argument succeeds. It is the Map's strongest consideration, but conditional.
2. *Parsimony*, on both sides: the identity posits one property where the law posits two plus a law (Block & Stalnaker; McLaughlin's "best explanation"); modal monism posits one modal primitive where modal dualism needs two (Chalmers 1999 §3.5; 2010 §10). [Tenet 5](/tenets/#occams-limits) discounts both. The routing page already states the symmetry ("the Map cannot discount simplicity in the physicalist's identity inference while relying on it in its own abductions"); the new page must apply it to Chalmers's own modal argument, which no Map page has done.
3. *The epistemology of modality*: if metaphysical modality is an independent primitive, conceivability gives no access to it. This strand survives Tenet 5, because it concerns access rather than economy. It is a priori, though, and it meets Papineau's counter that modal knowledge comes through counterfactual and causal reasoning.
4. *The productiveness half*: Block & Stalnaker's "transfer of explanatory and causal force" is a causal argument resting on closure. [Tenet 2](/tenets/#minimal-quantum-interaction) denies closure at quantum indeterminacy ([causal-closure](/concepts/causal-closure/)), another defeater-removal.

**Verdict.** Does the cost, with Tenet 5, lift any reply to *suggestive*? **No.** Tenet 5 disables the parsimony tiebreak that would otherwise favour Type-B's identity reading, which leaves a tie on the explanation register with no tiebreak, and nothing empirical has entered. The cost argument is an *input* to the second-order comparison the routing page has not yet run ("which reading of an epistemically primitive bridge fits the way primitives behave elsewhere in science"), not a substitute for it. If that comparison is run, the cost argument supplies one criterion on dualism's side, and the predicted-uniqueness reply supplies Type-B's answer to it.

**What the cost does NOT show** (the page should state each):
- That the psychophysical identity is false. Chalmers: "the position remains at least formally open".
- That dualism is true rather than type-F: ruling out primitive identities and strong necessities yields "a disjunction" of D, E and F, and type-F "can be seen as a sort of materialism" (routing page).
- Anything specific to interactionism. An interactionist psychophysical law is just as epistemically primitive: the parsimony page concedes as much at L83 ("This is a genuine explanatory cost"), which the optimistic review calls "the dualist mirror of the cost argument". The cost argument favours D, E and F alike, so it gives Tenets 2 and 3 nothing.
- Independent support for dualism. By Chalmers's own equivalence, "no strong necessities" *is* CP-, so in [P-D1](/positions/arguments-for-dualism/#p-d1) terms the strong-necessity cost belongs to the conceivability cluster. The identity formulation reaches the same dispute by a different premise (the law-mark claim), which makes it a second route to one disputed point, not a second piece of evidence.
- That identities need explaining in the ontological sense. Chalmers & Jackson grant "Identities are ontologically primitive".
- Anything empirical.

## Corpus Seams Found

1. **`concepts/zombie-master-argument` L102 misstates the key premise.** It says the coincidence of primary and secondary intensions for phenomenal concepts "is the load-bearing premise" and that the argument's force "is conditional on the coincidence holding", and that the phenomenal-concepts strategy denies it. Chalmers says the opposite twice: 1999 §3.1, "while I accept this observation, it is inessential to the argument"; 2003 §6, "(This claim is not required for the argument to go through …)". The premise type-B must deny is thesis (ii), conceivability implies verification by some world, equivalent to "no strong necessities". And Loar's version of the strategy *grants* coincidence (his clause (b), per Chalmers 1999), so "the phenomenal concepts strategy denies" it is wrong at least for Loar. 3,042 words, 457 of headroom. Candidate refine-draft (not minted here).
2. **Routing row mislink.** `concepts/type-a-type-b-and-type-c-physicalism` L90 routes "Two-dimensional argument" to `kripke-a-posteriori-necessity-argument`, which contains no two-dimensional material. Repoint to the new page (zero words), or to `zombie-master-argument#Two-Dimensional Semantics and the Master Argument`.
3. **Three parallel hosts with three counters**: parsimony L75 ("Whether called an identity or a law, this is a brute addition"), relocation L84 (Chalmers–Jackson a priori entailment), type-identity L71 (Kripke's appearance/reality point). These are compatible, and the new page should present them as three layers: Kripke's reason why "pain" lacks a contingent mode of presentation, Chalmers–Jackson's epistemic/ontological distinction, and the law-mark premise.
4. **The optimistic review's planned pipe** (parsimony L75, "unexplained" → `the-relocation-objection#rival-readings`) should target the new page instead once it exists, since the parsimony page has 75 words of headroom and a zero-word pipe is its only option.
5. **Two "master arguments" in Map vocabulary**: `zombie-master-argument` uses "master argument" for the conceivability argument as a whole, while the routing page and `phenomenal-concepts-strategy` use it for Chalmers's 2007 dilemma against the phenomenal-concepts strategy. The new page should always say "Chalmers's (2007) master argument against the phenomenal-concepts strategy".
6. **Papineau year.** The relocation page cites Papineau (2002) for "identities need no explanation"; verified loci are 1993 p. 180, 1998 p. 379 and 2011 p. 9 (2002 is metadata-only here). Not an error; give the article a verified locus.

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1959 | Smart, "Sensations and Brain Processes" | Identity theory; the "dual property" objection Chalmers later formalises |
| 1971/1980 | Kripke, *Naming and Necessity* | Necessary a posteriori; argues the psychophysical case is unlike water/H₂O |
| 1983 | Levine, "Materialism and Qualia: The Explanatory Gap" | Names the explanatory gap |
| 1990 | Loar, "Phenomenal States" (rev. 1997) | Phenomenal concepts as recognitional; psychophysical necessity sui generis |
| 1993 | Papineau, "Physicalism, Consciousness and the Antipathetic Fallacy" | "There's an end on it": the identity needs no explanation |
| 1996 | Chalmers, *The Conscious Mind* | "Strong metaphysical necessity" (p. 136, per Chalmers 1999 and Levine 2001) |
| 1997 | Hill, "Imaginability, Conceivability, Possibility and the Mind-Body Problem" | Cognitive explanation of zombie conceivability |
| 1998 | Papineau, "Mind the Gap" | §6 "Identities Need no Explaining" |
| 1999 | Block & Stalnaker; PPR symposium; Chalmers, "Materialism and the Metaphysics of Modality" | Non-exceptionalism; "strong necessities" named; modal dualism charge |
| 2001 | Chalmers & Jackson; Levine, *Purple Haze*; Horgan & Tienson vs McLaughlin | PQTI entailment; ontological vs epistemic primitiveness; "gappy identity"; "new wave materialism" |
| 2002/2003 | Chalmers, "Consciousness and its Place in Nature" | Verdict: "primitive identities or strong necessities" |
| 2007 | Chalmers, "Phenomenal Concepts and the Explanatory Gap"; Papineau on Kripke | Master argument against concept-based explanations of uniqueness |
| 2009/2010 | Chalmers, "The Two-Dimensional Argument Against Materialism" | CP- equivalent to no strong necessities; fifteen-candidate audit |
| 2011 | Goff, AJP; Papineau, *Philosophia* | Phenomenal transparency against a posteriori physicalism; "Identities need no explanation" restated |
| 2013/2014 | Goff & Papineau, "What's Wrong with Strong Necessities?" | Stress-free modal dualism; modality not grounded in conceivability |
| 2017 | Schaffer, "The Ground Between the Gaps" | Gaps pervasive; ground physicalism |

## Potential Article Angles

**Recommended target**: `concepts/primitive-identities-and-strong-necessities.md` (slug free in `obsidian/`, `archive/` and `hugo/content/` at 08:55Z). Concepts 342/360. Concepts thresholds 2,500 soft / 3,500 hard (gate `>=`); `analyze_length` counts the reference list, so keep the total at or below ~3,200 (prose ~2,300–2,700 plus ~14 references).

1. **Angle 1 (recommended): "Two kinds of primitiveness."** Lead with the result: Chalmers's cost is real and Type-B concedes most of it on the explanation side; the dispute is whether an epistemically primitive bridge is an identity or a law; the Map's tier stays *compatible*. Suggested shape:
   - Lede: the verdict quote, one-sentence definitions of both costs, the tier result, and a "not the primitive identity of subjects" disambiguation pointing to `topics/consciousness-and-the-metaphysics-of-individuation`.
   - *Ontological and epistemic primitiveness*: the Papineau / Block–Stalnaker rejoinder with verified loci, the Chalmers–Jackson distinction, Levine's gappy identity.
   - *A law under another name*: the law-mark premise, parity, and Type-B's concessions.
   - *Strong necessities*: weak vs strong in one paragraph, the SEP derivation/non-derivation gloss, CP- equivalence, and the warning that the coincidence of intensions is inessential. Point to `zombie-master-argument` for the argument itself.
   - *Is there any other case?*: the table above, compressed, and the predicted-uniqueness reply.
   - *Where the dispute bottoms out*: concept-based explanations versus the 2007 master argument; modal rationalism versus Papineau and Goff.
   - *What the cost buys the Map*: parity, the symmetric Tenet 5, the not-shown list.
   - Relation to Site Perspective: Tenet 1 (commitment, not result); Tenet 5 (cuts both ways, including against modal monism); Tenets 2–3 (the dualist law is equally primitive; closure-denial answers the productiveness half).
2. **Angle 2 (alternative): "Is there any other case?"**, organised around the candidate audit. More concrete, but it buries the ontological/epistemic distinction, which is the Map's real gain.
3. **Declined angle**: a general survey of strong necessities in modal metaphysics (mathematics, God, laws). An LLM reader can get this elsewhere, and it moves away from consciousness.

When writing, follow `obsidian/project/writing-style.md` (front-load the result, named-anchor forward references, a "Relation to Site Perspective" section, no "This is not X. It is Y." constructions).

### Articles that should later cite it (lengths measured 2026-10-03, `analyze_length`)

| Page | Words | Headroom (hard − 1 − count) | Suggested link |
|---|---|---|---|
| `concepts/type-a-type-b-and-type-c-physicalism` | 2,803 | 696 | Routing rows "A primitive identity is a law under another name" and "Two-dimensional argument" → new page |
| `concepts/the-relocation-objection` | 2,487 | 1,012 | L84 pointer: the counter in full |
| `concepts/type-identity-theory` | 2,322 | 1,177 | L71 pointer |
| `topics/parsimony-case-for-interactionist-dualism` | 3,924 | 75 | Zero-word pipe on L75 only |
| `concepts/kripke-a-posteriori-necessity-argument` | 2,227 | 1,272 | L61, conceivability-to-possibility reply: name strong necessity |
| `concepts/conceivability-possibility-inference` | 2,271 | 1,228 | L92–94 pointer |
| `concepts/zombie-master-argument` | 3,042 | 457 | With the L102 correction |
| `concepts/phenomenal-concepts-strategy` | 3,448 | 51 | Zero-word pipe only |
| `concepts/explanatory-gap` | 3,495 | 4 | Zero-word pipe on L135 "epistemically primitive" only |

## Gaps in Research

- **Papineau 2002** (*Thinking about Consciousness*, ch. 5): metadata only. The claim is verified in his 1993, 1998 and 2011 papers.
- **Loar 1990/1997, Hill 1997, Hill & McLaughlin 1999, Loar 1999, Yablo 1999**: own texts not fetched. Their positions are reported through Chalmers 1999 (full text) and the SEP (secondary).
- **Goff & Papineau** read in the January 2013 author draft; published wording unchecked.
- **Chalmers 2010** read in the consc.net pre-publication version; printed-chapter wording and page numbers unchecked.
- **Schaffer 2017**: abstract only (site blocked).
- **Levine 2001**: snippet access. The p. 91 sentence is truncated at "the whole"; p. 84's sentence begins mid-clause. Do not quote beyond the verified spans.
- **Kripke's own stance on strong necessities** is read in opposite ways by Chalmers 2003 and by Goff & Papineau (citing Papineau 2007). Not adjudicated here; the Map's Kripke page should not be cited for either reading without a check.
- **Earliest use of "gappy identity"**: Levine 1998 (*Noûs* 32) not checked.
- **No survey of post-2017 literature** was possible without search (for example responses to Schaffer, or recent work on grounding and the explanatory gap). A literature-drift check would need a search budget.

## Citations

1. Block, N., & Stalnaker, R. (1999). Conceptual analysis, dualism, and the explanatory gap. *Philosophical Review*, 108(1), 1–46. https://doi.org/10.2307/2998259 (full text, JSTOR scan via archived author copy)
2. Chalmers, D. J. (1999). Materialism and the metaphysics of modality. *Philosophy and Phenomenological Research*, 59(2), 473–493. https://doi.org/10.2307/2653685 (full text, author's version; pages per the author's header, Crossref records first page 473 only)
3. Chalmers, D. J. (2003). Consciousness and its place in nature. In S. P. Stich & T. A. Warfield (Eds.), *The Blackwell Guide to Philosophy of Mind* (pp. 102–142). Blackwell. https://doi.org/10.1002/9780470998762.ch5 (full text, author's version)
4. Chalmers, D. J. (2010). The two-dimensional argument against materialism. In *The Character of Consciousness* (pp. 141–206). Oxford University Press. https://doi.org/10.1093/acprof:oso/9780195311105.003.0006 (full text of pre-publication version)
5. Chalmers, D. J., & Jackson, F. (2001). Conceptual analysis and reductive explanation. *Philosophical Review*, 110(3), 315–360. https://doi.org/10.1215/00318108-110-3-315 (full text, author's version)
6. Díaz-León, E. (2014). Do a posteriori physicalists get our phenomenal concepts wrong? *Ratio*, 27(1), 1–16. https://doi.org/10.1111/rati.12018 (abstract; online 2013)
7. Goff, P. (2011). A posteriori physicalists get our phenomenal concepts wrong. *Australasian Journal of Philosophy*, 89(2), 191–209. https://doi.org/10.1080/00048401003649617 (abstract)
8. Goff, P., & Papineau, D. (2014). What's wrong with strong necessities? *Philosophical Studies*, 167(3), 749–762. https://doi.org/10.1007/s11098-013-0195-6 (full text of author's draft)
9. Hill, C. S. (1997). Imaginability, conceivability, possibility and the mind-body problem. *Philosophical Studies*, 87(1), 61–85. https://doi.org/10.1023/A:1017911200883 (metadata only)
10. Hill, C. S., & McLaughlin, B. P. (1999). There are fewer things in reality than are dreamt of in Chalmers's philosophy. *Philosophy and Phenomenological Research*, 59(2), 445–. https://doi.org/10.2307/2653682 (metadata; quoted via SEP)
11. Horgan, T., & Tienson, J. (2001). Deconstructing new wave materialism. In C. Gillett & B. Loewer (Eds.), *Physicalism and Its Discontents* (pp. 307–318). Cambridge University Press. https://doi.org/10.1017/CBO9780511570797.016 (opening text)
12. Kirk, R. (2023 revision). Zombies. *Stanford Encyclopedia of Philosophy*. https://plato.stanford.edu/entries/zombies/ (full text)
13. Levine, J. (2001). *Purple Haze: The Puzzle of Consciousness*. Oxford University Press. https://doi.org/10.1093/0195132351.001.0001 (snippet access)
14. Loar, B. (1990). Phenomenal states. *Philosophical Perspectives*, 4, 81–108. https://doi.org/10.2307/2214188 (metadata; revised 1997)
15. McLaughlin, B. P. (2001). In defense of new wave materialism: A response to Horgan and Tienson. In C. Gillett & B. Loewer (Eds.), *Physicalism and Its Discontents* (pp. 319–330). Cambridge University Press. https://doi.org/10.1017/CBO9780511570797.017 (opening text)
16. Papineau, D. (1993). Physicalism, consciousness and the antipathetic fallacy. *Australasian Journal of Philosophy*, 71(2), 169–183. https://doi.org/10.1080/00048409312345182 (full text)
17. Papineau, D. (1998). Mind the gap. *Philosophical Perspectives*, 12, 373–388. https://doi.org/10.1111/0029-4624.32.s12.16 (full text)
18. Papineau, D. (2002). *Thinking about Consciousness*, ch. 5 "The Explanatory Gap" (pp. 141–160). Oxford University Press. https://doi.org/10.1093/0199243824.003.0006 (metadata only)
19. Papineau, D. (2007). Kripke's proof is ad hominem not two-dimensional. *Philosophical Perspectives*, 21, 475–494. https://doi.org/10.1111/j.1520-8583.2007.00133.x (full text fetched; thesis only)
20. Papineau, D. (2011). What exactly is the explanatory gap? *Philosophia*, 39(1), 5–19. https://doi.org/10.1007/s11406-010-9273-6 (full text)
21. Schaffer, J. (2017). The ground between the gaps. *Philosophers' Imprint*, 17(11). http://hdl.handle.net/2027/spo.3521354.0017.011 (abstract only)
22. Stoljar, D. (2026 revision). Physicalism. *Stanford Encyclopedia of Philosophy*. https://plato.stanford.edu/entries/physicalism/ (full text)
23. Weisberg, J. (n.d.). Hard problem of consciousness. *Internet Encyclopedia of Philosophy*. https://iep.utm.edu/hard-problem-of-conciousness/ (full text)