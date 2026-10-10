---
title: "Deep Review - Bergson and Duration"
created: 2026-10-10
modified: 2026-10-10
human_modified: null
ai_modified: 2026-10-10T08:58:38+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-10
last_curated: null
---

**Date**: 2026-10-10
**Article**: [[bergson-and-duration|Bergson and Duration]]
**Previous review**: [[deep-review-2026-07-17-bergson-and-duration|2026-07-17]]

## Scope

This is the seventh deep review. The damping-aware scorer selected the article (score 60) because the body changed substantively on 2026-10-03. That refine-draft (commit 28cbf83e5c), prompted by [[outer-review-2026-10-03-chatgpt-5-6-sol-pro]] §12, removed an unargued step from phenomenological non-spatiality to ontological non-physicality and dropped "independent" support for dualism. All six prior reviews had passed that "independent philosophical support" sentence as calibrated. The outer reviewer caught it, so the earlier "slippage: PASS" verdicts are not evidence that the remaining text is sound. This pass re-read the whole article fresh and did not inherit their passes.

The 10-03 recalibration holds and has not been touched. The defects found this pass sit on axes the earlier reviews did not check: what the physics says, what many-worlds says, Whitehead's own text, and the subject of a quoted sentence.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Many-worlds was misdescribed as branching the past (strawman).** L135 read "if the past itself branches into incompatible histories, no single durée carries the full weight of what was lived." In Everettian branching every branch has a single past, and divergence runs forward. A Many-Worlds Defender (Deutsch) would rightly call this a strawman. **Resolution:** the paragraph now says many-worlds does not branch the past. It places the tension in the forward direction: one accumulated past prolongs itself into many incompatible presents, against durée's indivisibility, and nothing settles which successor continues *this* durée. It also states the defender's reply ("each successor inherits the whole past equally; no further fact is missing") and marks the remaining disagreement honestly, as a question about whether indexical identity is real. Mode Three.
2. **The physics claim was false as stated.** L65 read "The fundamental equations of physics are time-symmetric." Weak-interaction T-violation is observed (it is required by CPT given CP violation, and was directly measured in B mesons). The Map's own Tenet 2 also relies on outcome selection, which is not a time-symmetric dynamical law. **Resolution:** the text now reads "fundamental dynamical equations … time-symmetric, apart from a small violation in the weak interaction". "As Bergson describes it" was added so that the experiential-irreversibility claim is scoped to Bergson's exposition.
3. **Whitehead was misdescribed.** L113 read "Whitehead's actual occasions are discrete (though internally temporal)". *Process and Reality* says the opposite. Grepped in the raw text (archive.org `processrealityes00whit_1`): "in every act of becoming there is the becoming of something with temporal extension; but … the act itself is not extensive, in the sense that it is divisible into earlier and later acts of becoming"; "This genetic passage from phase to phase is not in physical time". **Resolution:** the text now reads "each spans a stretch of time, but its becoming is not divisible into earlier and later acts of becoming."
4. **The quote's subject was spliced (Kent & Wittmann).** The text read "Kent and Wittmann (2021) identified experienced duration as 'one of the core issues in theories of consciousness.'" The predicate is verbatim, but in the source the subject is "**This confusion between short and discrete versus long and continuous** is, we argue, one of the core issues…". **Resolution:** the text now reads "argue that confusing short, discrete moments with long, continuous experience is '…'". "Global Workspace Theory" was also changed to "Global Neuronal Workspace", which is the theory the paper discusses (GNWT, Dehaene).

### Citation / Verbatim Web-Verify Ledger (§2.4)

Raw-text greps this pass. No aggregators were used, and unfinishablemap.org was not used.

- **Bergson, "Time is invention or it is nothing at all"** (*Creative Evolution*, Mitchell trans.). State: **real-correct (verbatim)**. Re-grepped in Gutenberg #26163: "_Time is invention or it is nothing at all._" There is no "an" (see the 07-17 stability note).
- **Bergson, "qualitative multiplicity"** (*Time and Free Will*, Pogson trans.). State: **real-correct (verbatim)**. Grepped in Gutenberg #56852: "a continuous or qualitative multiplicity with no resemblance to number". The melody image is Bergson's own ("like the notes of a tune").
- **Bergson, *Creative Evolution* indetermination passages (NEW, in the Tenet 2 paragraph).** State: **real-correct (verbatim)**. All four quoted strings were grepped in Gutenberg #26163: "the rôle of life is to insert some _indetermination_ into matter"; "the quantity created does not belong to the order of magnitude apprehended by our senses and instruments of measurement"; "the work of releasing, although always the same and always smaller than any given quantity"; "consciousness corresponds exactly to the living being's power of choice".
- **Whitehead, creativity as "the ultimate"** (*Process and Reality*). State: **real-correct (verbatim)**. Raw text: "In the philosophy of organism this ultimate is termed 'creativity'". The old gloss "his Category of the Ultimate" was **real-wrong**: the Category of the Ultimate is "'Creativity,' 'many,' 'one'", so creativity is one notion within it and not the category itself. It was replaced with the verbatim "the principle of novelty" ("'Creativity' is the principle of novelty").
- **Kent, L. & Wittmann, M. (2021)**, *Neuroscience of Consciousness* 2021(2), niab011. Metadata state: **real-correct**. Crossref gives issue 2; Europe PMC's index shows issue 1, which is the pre-erratum mis-issue (erratum niab015). The quote was **real-correct in the predicate and spliced in the subject**, and is fixed above. **Result-direction leg:** the full text (PMC8042366) says "major theories such as IIT, GNWT, RPT, and ST were concerned only with narrow timescales between approximately 100 and 300 ms" (citing Northoff & Lamme 2020) and "many of the leading candidate theories cannot explain continuity or flow". The article's "cannot explain why experience extends across seconds" matches that direction. **Stance leg:** Kent & Wittmann are neutral about which theory is right ("It may be that different theories of consciousness are compatible/complementary"). They do not mention Bergson. "Bergson diagnosed this gap a century earlier" is placed after a colon as the Map's gloss and does not present them as Bergsonians.
- **Bergson (1934/1946), *The Creative Mind*, Citadel Press.** State: **real-wrong-metadata**. Andison's translation first appeared in 1946 from Philosophical Library (Wisdom Library imprint per the UPenn catalogue). Citadel's edition is 1992, per the SEP Bergson bibliography: "New York: The Citadel Press, 1992 [1946]". **Corrected** to 1934/1992, with the translator named and a note on the 1946 first publication. This was the article's only uncited-inline Bergson primary source. It is now anchored inline: "Introduction to Metaphysics" (1903, collected in *The Creative Mind*) is where Bergson sets out analysis versus intuition.
- **Julian Huxley as critic of the élan vital.** State: **real-correct**. His "élan locomotif" railway-engine quip is well attested. No quote appears in the article.
- **Time and Free Will 1889/2001 Dover; Matter and Memory 1896/1988 Zone; Creative Evolution 1907/1998 Dover; Guerlac 2006 Cornell; Whitehead 1929/1978 Free Press.** Publisher-verified 2026-06-25. The References entries are unchanged and were not re-litigated.
- **Lacey 1989 Routledge; Mullarkey 1999 Edinburgh UP.** These are standard editions. They have no inline cite and serve as background secondary literature, following the corpus convention; left as is.

**Empirical-record currency sweep:** the helper returns no superlative claims.

### Medium Issues Found

- **Relation to Site Perspective had no Tenet 2 paragraph, and it misdescribed Bergson's mechanism.** "Differing on mechanism, looking to quantum indeterminacy rather than Bergson's vitalism" misses that Bergson's own account of how life and consciousness act on matter is indetermination plus an energy-conserving trigger of less than any given quantity. **Resolution:** a new Minimal Quantum Interaction paragraph built from the verified passages. It is calibrated: Bergson "could not say where in physics that openness lies"; locating it in quantum outcomes "is the Map's own proposal"; and the precedent "gives the idea a lineage, not evidence". The Dualism closer now reads "without adopting the *élan vital*", and the section opener was adjusted to match.
- **The Further Reading gloss for `temporal-consciousness-structure-and-agency`** duplicated the gloss for the temporal-becoming article ("How temporal ontology constrains…"). It was rewritten from the target's own description.

### Counterarguments Considered

- **Anti-dualist vitalism induction (Dennett/Churchland).** The élan vital is the stock example of a non-physical posit that was eliminated. The article now links [[vitalism]], which carries the disanalogy reply. This adds no words in the body (a piped link on "vital force").
- **Many-worlds reply.** Now stated in the article and answered at the framework boundary (Mode Three).
- **Quantum skeptic on the new Tenet 2 paragraph.** The paragraph explicitly claims precedent, not evidence, and does not attribute any quantum view to Bergson. Writing in 1907, Bergson could not have held one.
- The determinist and eliminativist disagreements, the Buddhist momentariness tension, and the contestedness of the élan vital carry forward as bedrock (see Stability Notes).

### Other Verifications

- **Possibility/probability slippage: PASS on the 10-03 text.** The lead, Dualism and Bidirectional paragraphs now separate intelligibility, availability and actuality (`^tenet-3-standing`). The new Tenet 2 paragraph was written to the same discipline. A tenet-accepting reviewer would not flag it.
- **Method/history necessity vocabulary.** "Bergson diagnosed this gap… theories that spatialize time cannot capture duration" is a *documented textual claim* attributed to Bergson. "Intellect naturally spatializes" is attributed to Bergson. No unlabelled origin⇒validity move.
- **Engagement modes (editor-internal).** Snapshot and spatialising reductions: Mode One (unchanged since 10-03). Ontological residue: Mode Three (unchanged). Many-worlds: Mode Three, upgraded from a strawman to an honest boundary statement. Determinist (Time and Free Will section): Mode Three, bedrock.
- **Label leakage: none.** No "This is not X. It is Y.", no "load-bearing", and no `[1m]` artifact.
- **Wikilinks.** All targets resolve, including the new `[[vitalism]]` and the `^minimal-quantum-interaction` anchor in `tenets.md`.

## Optimistic Analysis Summary

### Strengths Preserved

These are untouched: the 10-03 calibrated lead ("a vivid case rather than a separate route"); the four-feature durée exposition and melody analogy (now confirmed as Bergson's own image); the three-way irreversibility distinction; intuition defended as disciplined attention; the honest treatment of the élan vital; the Bergson–Whitehead comparison (made more precise, not expanded); and the Bidirectional paragraph's intelligibility/actuality separation.

### Enhancements Made

1. A Tenet 2 paragraph built on four verified *Creative Evolution* passages (Chalmers/Stapp personas). It is the article's most distinctive new content, because no other Map page cites Bergson's "insert some indetermination into matter" (grep: 0 hits before this pass).
2. The "Introduction to Metaphysics" anchor for the analysis/intuition distinction.
3. The many-worlds paragraph now ties back to the article's own Indivisibility feature.

### Cross-links Added

- [[vitalism]] (body, as a piped link; concepts frontmatter; Further Reading). This makes the link reciprocal, since `concepts/vitalism` already links here.
- [[tenets#^minimal-quantum-interaction]]

## Remaining Items

- **Sibling Whitehead errors, not fixed here** (other files, with concurrent agents active). `concepts/process-philosophy` L72 has the identical "discrete (though internally temporal)" phrase. Its L58 says "Whitehead names this creative advance his 'Category of the Ultimate'". `apex/process-and-consciousness` L69 has the identical "'the ultimate,' his Category of the Ultimate" conflation, and its L67 says "every actual occasion's coming-to-be a temporally extended act of synthesis", which contradicts PR's "the act itself is not extensive". A P2 refine-draft task with the verified raw-text strings has been minted in todo.md.

## Stability Notes

- **Do not restore "his Category of the Ultimate" or "internally temporal".** Both are contradicted by the raw *Process and Reality* text quoted above.
- **Do not reintroduce "the past branches" for many-worlds.** The many-worlds paragraph now states the defender's reply and marks the residue as a dispute about indexical identity. A Many-Worlds Defender's continued dissatisfaction is bedrock, not a defect.
- **The Tenet 2 paragraph claims lineage, not evidence.** Future passes should neither upgrade it ("Bergson anticipated quantum interactionism") nor delete it as tangential. Its quotes are raw-text-verified.
- **"Time is invention or it is nothing at all" stays without "an"** (Gutenberg #26163, re-grepped this pass).
- Carried forward from earlier reviews: the determinist and eliminativist disagreements are bedrock; the Buddhist momentariness question is open, not a defect; the élan vital treatment is correct as written; the specious-present paragraph should not be expanded.
- **Length is now 2862 words (95% of the 3000 soft threshold).** Future passes are length-neutral.
