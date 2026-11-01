---
title: "Deep Review - Consciousness and Integrated Information"
created: 2026-11-01
modified: 2026-11-01
human_modified: null
ai_modified: 2026-11-01T13:50:29+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-01
last_curated: null
---

**Date**: 2026-11-01
**Article**: [[consciousness-and-integrated-information|Consciousness and Integrated Information]]
**Previous review**: [[deep-review-2026-07-20-consciousness-and-integrated-information|2026-07-20]]
**Context**: Seventh deep review. Selected as the highest-ranked `deep_review.py candidates` entry (score 74) that was neither on the driver's exclusion list nor named as File or Secondary by any open task above `## Completed Tasks` (the two "integrated-information" hits there are agentic-social topic-dedup notes, not tasks on this file). Higher-ranked candidates were skipped: `forward-in-time-vs-time-symmetric-selection` (excluded), `philosophy-of-action-under-dualism` (File of the open P3 Davidson task), `arguments/functionalism-argument` (File of the NEEDS-HUMAN Tallis task), `arguments/many-worlds-argument` (File of the NEEDS-HUMAN length task). Four commits touched the article since 2026-07-20 (07-22 improper-mixture terminology, 07-29 epiphenomenalism calibration, 09-30 classical-menu propagation, 10-27 Tegmark targets). Every page it relies on (tenets, quantum-biology, cognitive-distinctiveness, phenomenal-value-realism, universal-coupling-response, the-binding-problem) has changed since then.

**Length**: 3999 → 3996 (topics soft 3000 / hard 4000, gate `>=`). The article started at zero headroom, so this pass was strictly length-negative: every addition was paid for in the same pass.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Attribution error: "Tononi accepts [panpsychism]"** (What IIT Gets Right). Tononi & Koch (2015) say IIT "vindicates some intuitions often associated with panpsychism" but that "unlike panpsychism, IIT implies that not everything is conscious, for example aggregates such as heaps of sand, a group of individuals or feed forward networks" (arXiv 1405.7089 preprint text, grep-verified; the published abstract carries the same contrast). The 2026-03-19 and 2026-06-02 reviews certified the line against Aaronson's blog, not Tononi's own text. **Fixed**: "Rather than retreating from [[panpsychism]], Tononi accepts it." → "Tononi accepts IIT's [[panpsychism|panpsychist-leaning]] consequences rather than retreating from them, while holding that not everything is conscious (Tononi & Koch, 2015)." Reference added.
2. **Misrepresented source: Lopez & Montemayor (2025)**. The article said IIT "cannot explain the informational differences between experiences that share a phi-structure but differ in what is attended." The paper's §3, "The Problem of Informational Differences" (Erkenntnis 91, pp. 1426–1428; grep of the version-of-record PDF), is about *kinds* of experience. Perception is more informative than dreaming or imagery, yet IIT counts only information intrinsic to the PSC. The authors even suggest that "differences in structure between different kinds of experiences seem to be the most promising way to go". The paper contains no shared-Φ-structure, differently-attended case. **Fixed**: "...press exactly this gap: ... experiences that share a phi-structure but differ in what is attended." → "...press a related gap: ... cannot explain why perception is more informative than dreaming when only information intrinsic to the system counts." The following sentence, that the critique is internal to IIT's commitments, still stands: the authors argue "in purely intrinsic terms, according to their own desiderata".
3. **Result-direction error: Corcoran et al. (2026)**. The article said the review "found the theories make genuinely contrasting predictions that current evidence does not adjudicate." The PubMed abstract (PMID 42114729) shows the review compares *three* theories (IIT, Neurorepresentationalism, Active Inference) and "outline[s] the key hypotheses to be tested across a series of multi-site experiments" for "the empirical work to come". It reports no evidential finding. **Fixed**: "compared IIT against active-inference and predictive-processing accounts and found the theories make genuinely contrasting predictions that current evidence does not adjudicate" → "compared IIT with Active Inference and Neurorepresentationalism and set out contrasting predictions for multi-site experiments still to be run". The calibration sentence after it was kept in substance and tightened ("This is an intra-physicalist exchange that does nothing to vindicate... not a settled consensus," → "The exchange does nothing to vindicate... remain rival characterisations...").
4. **Factual error: "as all interpretations except superdeterminism hold"** (L84). Bohmian mechanics and Everettian quantum mechanics are both deterministic, so the parenthesis was false. **Fixed** → "(as collapse and other indeterministic interpretations hold)". No other live page carries the phrase.
5. **Attributed figure understated: Fisher (2015) "might survive for hours"**. Fisher's own estimate is "tcoh ≃ frot²/fdip ∼ 10⁵ s ∼ 1 day. Actual coherence times could well be even longer..." (Annals of Physics 362, grep of the arXiv v2 PDF). The abstract gives no number ("on very long times"). **Fixed** → "might survive for about a day".
6. **Tenet-repair propagation miss: unscoped indistinguishability** (L78, L82). Tenets.md now scopes empirical indistinguishability to "any *unconditioned aggregate* test", adding that "a deviation *conditioned* on intention, task or subject would test the corridor itself" (P-Q3). The 2026-09-30 propagation sweep keyed on "indistinguishable from chance". This article words the same claim as "no experiment measuring frequencies could detect", so the sweep missed it. **Fixed**: L78 "no experiment measuring frequencies could detect consciousness's influence." → "no unconditioned frequency test could detect consciousness's influence (intention-conditioned tests remain open)."; L82 "That someone measuring frequencies wouldn't detect this influence" → "That unconditioned frequency counts wouldn't detect this influence".
7. **Stale Map-internal description: "two-paths framing developed in the quantum-biology article"**. The linked section (`#why-this-matters-for-consciousness`) has not held a two-paths framing since 3e23c92ff1 (2026-05-23). It now hands off to "Tenet 2's three sub-readings", which `## The Calibration Table` allocates. **Fixed**: link retargeted to `#the-calibration-table` with label "quantum-biology article's calibration table". The two clauses that follow (pre-decoherence mechanisms vs post-decoherence selection) map onto two of that table's three columns.

### Medium Issues Found

- **Calibration and internal consistency in Relation to Site Perspective (MQI paragraph)**. "the selected pattern is the integrated experience" identified experience with a physical pattern, which is the move the article attacks in IIT and which contradicts the Dualism paragraph ("the physical systems provide the substrate, consciousness the integrative act"). "This also handles the temporal gap: if consciousness involves collapse processes, each collapse has duration" asserted an unsupported physical claim and said it "handles" the gap. A tenet-accepting reviewer would flag both. **Fixed** → "and that selection is the integrating act. It may also bear on the temporal gap, if each act of selection has duration rather than occurring at an instant—a conjecture the Map has not established."
- **Passivity sentence vs tenets.md ^tenet-3-epiphenomenalism**. "The theory cannot explain why we reliably track phenomenal facts if phenomenal facts have no causal role" contradicted the article's own L60/L64, which grant that phenomenal facts carry causal powers through their physical constitution. It also outran the tenet page, which concedes that the phenomenal-concept strategy answers the bare self-stultification charge. **Fixed** → "The theory owes an account of why we reliably track phenomenal facts that have no autonomous causal role." ("autonomous" is the article's own L64 term).
- **Kim mischaracterised**: "compete with physical causation at the same level". Kim's exclusion argument pits a higher-level cause against its lower-level base. **Fixed** → "for the same effect".
- **"predates IIT by nearly a century"**: *Process and Reality* is 1929 and IIT is 2004, so 75 years. **Fixed** → "by some seventy-five years".
- **"vanishes in femtoseconds"**: Tegmark's range of 10⁻¹³ to 10⁻²⁰ s is mostly sub-femtosecond. **Fixed** → "vanishes that fast".
- **"The Templeton adversarial collaboration and COGITATE study"** read as two separate things, though COGITATE is one of the TWCF-funded collaborations (Corcoran et al. is another, INTREPID). **Fixed** → "The Templeton-funded adversarial collaborations, COGITATE among them, are serious attempts".

### Low Issues / Trims (to fund the above)
- Cut "—a distinction with deep roots in philosophy of mind" (filler), "and must be stated honestly", "Three responses deserve consideration." (First/Second/Third still read cleanly after the question), "If anything,". Removed the Relation-to-Site Dualism line "The identity thesis also leaves the [[explanatory-gap]] unilluminated, for the reason given above." because it duplicated L68, which already links explanatory-gap.

### Citation Web-Verification Ledger (publisher of record)

Crossref API for every DOI, with title, container, volume, issue, pages and full author list printed untruncated. Quotes and figures were grepped in the raw text where it was obtainable.

- Tononi 2008 (*Biol Bull* 215(3), 216-242, DOI 10.2307/25470707) — state: real-correct.
- Albantakis et al. 2023 (IIT 4.0, *PLOS Comput Biol* 19(10), e1011465) — state: real-correct (subtitle omitted; acceptable).
- Tononi & Koch 2015 (*Phil Trans R Soc B* 370(1668), 20140167) — state: real-correct; NEW, added to support the corrected panpsychism line.
- Aaronson 2014 (scottaaronson.blog/?p=1799, 2014-05-21) — state: real-correct; quote re-grepped verbatim: "they can be unboundedly _more_ conscious than humans are." "Tononi accepts this" (expander) is supported by Aaronson's follow-up post, 2014-05-30 (?p=1823: "He affirms that, yes, according to IIT, a large network of XOR gates arranged in a simple expander graph is conscious"), which reports Tononi's reply ("Why Scott should stare at a blank wall and reconsider (or, the conscious grid)"). That reply is not the cited post; see Remaining Items.
- COGITATE Consortium 2025 (*Nature* 642(8066), 133-142, DOI 10.1038/s41586-025-08888-1) — state: real-correct (Crossref lists "Cogitate Consortium" first, so the Melloni first-author trap is avoided).
- Fleming et al. 2023 (PsyArXiv) — state: real-correct as a preprint citation. Date and count (15 Sept 2023, 124 signatories) are corroborated only by a secondary source (Wikipedia summary); the OSF record would not render. Currency: published in revised form as "What makes a theory of consciousness unscientific?", *Nature Neuroscience* 28(4), 689–693 (2025; byline led by "IIT-Concerned"), with Tononi et al.'s reply at pp. 694–702. See Remaining Items.
- Merker, Williford & Rudrauf 2022 (*BBS* 45, e41, DOI 10.1017/S0140525X21000881; online 2021-05-19) — state: real-correct. Abstract verbatim: "IIT's identification of consciousness with the causal efficacy with which differentiated networks accomplish global information transfer (which is what Φ in fact measures) is mistaken". The article's paraphrase is faithful.
- Corcoran et al. 2026 (*Neurosci Biobehav Rev* 187, 106742, DOI 10.1016/j.neubiorev.2026.106742; PMID 42114729) — state: real-correct metadata. Result-direction was WRONG and is fixed (Critical 3).
- Lopez & Montemayor 2025 (*Erkenntnis*) — state: real-wrong-metadata (incomplete). Version of record is "The Integrated Information Theory Needs Attention", *Erkenntnis* (2026) 91(3), 1419–1443, published online 2025-04-03. Corrected to "Needs" and added 91(3), 1419–1443; the year was kept at 2025 (online-first). Paraphrase was WRONG and is fixed (Critical 2).
- Lamme 2006 (*TiCS* 10(11), 494-501) — state: real-correct.
- Baars 1988 (*A Cognitive Theory of Consciousness*, CUP) — state: real-correct (standard).
- Dehaene & Changeux 2011 (*Neuron* 70(2), 200-227) — state: real-correct.
- Friston 2010 (*Nat Rev Neurosci* 11(2), 127-138) — state: real-correct.
- Whitehead 1929 (*Process and Reality*, Macmillan) — state: real-correct (standard).
- Kim 2005 (*Physicalism, or Something Near Enough*, Princeton UP) — state: real-correct (standard); the paraphrase is fixed (Medium).
- Tegmark 2000 (*Phys Rev E* 61(4), 4194-4206) — state: real-correct. Abstract verbatim: "~10^{-13}-10^{-20} seconds ... both for regular neuron firing and for kink-like polarization excitations in microtubules", which matches the 10-27 wording.
- Fisher 2015 (*Ann Phys* 362, 593-602) — state: real-correct metadata. The attributed figure was WRONG and is fixed (Critical 5).
- Coslett & Saffran 1991 (*Brain* 114(4), 1523-1545) — state: real-correct.

**Inline ↔ References**: complete both ways after adding Tononi & Koch 2015. Levine is named inline ("what Levine called the explanatory gap") with no References entry. It is a named-idea attribution, not an `Author YYYY` cite; see Remaining Items.
**Superlatives**: none in the body that need a currency check. "the most mathematically sophisticated theory of consciousness available" in the lead is evaluative, not empirical.

### Cited-author stance
Merker/Williford/Rudrauf: naturalistic; the abstract calls IIT's panpsychist drift a "departure from science as we know it", so the article's "remain within a physicalist frame" is fair. Lopez & Montemayor: no metaphysical commitment stated; the critique is internal to IIT. Corcoran et al.: theory proponents (Tononi, Friston, Pennartz), presented as not vindicating the Map. Tononi & Koch: IIT proponents who distinguish IIT from panpsychism, now stated as such.

### Reasoning-mode classification (editor-internal)
- Passivity objection vs IIT's identity thesis: Mixed. The opening is a Mode Two foundational-move identification (the identity is asserted without the transparency water = H₂O enjoys). The L66 circularity concession is Mode Three boundary-marking. After the L62 calibration, the epistemic charge is phrased as a debt IIT owes, not a refutation.
- Merker/Williford/Rudrauf: Mode Three (convergence on the negative point only). Corcoran: Mode Three. Lopez & Montemayor: Mode One (an argument internal to IIT's own commitments; the Map's extension is labelled as the Map's).
- Kim: Mode One/Mixed (the exclusion premise "every physical event already has a sufficient physical cause" is denied at token indeterminacies).
- No label leakage (editor-vocabulary grep clean); no boundary-substitution.

## Optimistic Analysis Summary

### Strengths Preserved
- Front-loaded lead with the identity/activity thesis stated in the first paragraph.
- Three-part critique (passivity, expander graph, temporal gap).
- Self-critical "Does Quantum Selection Escape This Charge?" section with the circularity acknowledgement. The heading is kept because `topics/phenomenal-value-realism` links to its anchor.
- The type/token distinction, now aligned with the tenet's scoped-indistinguishability wording.
- Walled-off treatment of intra-physicalist sources ("tenet-coherent, not evidence-elevating").
- Symphony and simultanagnosia anchors; the "What IIT Gets Right" section, now accurate about what Tononi accepts.

### Enhancements Made
- Seven critical corrections and six medium corrections (above), plus four trims, all within a net −3 words.

### Cross-links Added
- Retargeted [[topics/quantum-biology-and-neural-consciousness#the-calibration-table]]. The duplicate [[explanatory-gap]] link was removed (L68 still carries it).

## Remaining Items
- **Uncited Tononi acceptance (expander)**: "Tononi accepts this: a large expander graph would be conscious" rests on Tononi's 2014 reply as reported in Aaronson's 2014-05-30 post, not the cited 2014-05-21 post. Adding the reply as a reference costs about 20 words the article does not have.
- **Fleming et al. currency**: the 2023 preprint's revised publication, *Nature Neuroscience* 28(4), 689–693 (2025), could be added alongside or instead. Cost: about 20 words.
- **Levine** named inline without a References entry (about 15 words).
- All three need headroom. The article sits 3 words under the gate, so this is a human-length-budget decision. No condense queued, per the 2026-07-20 length note.

## Stability Notes
- Bedrock disagreements carried forward unchanged (eliminativist, Buddhist no-self, MWI, quantum-skeptic unfalsifiability, "activity is not simpler"). Do not re-flag them.
- **The "verified" ledger of 2026-07-20 was partial**: it directly verified 4 of 14 cites, and three defects sat in the unverified remainder or in paraphrases of verified cites (Lopez & Montemayor gloss, Corcoran finding, Fisher figure). Every cite now has a publisher or Crossref check, and the paraphrased claims were checked against raw text where it was obtainable. Future passes should re-verify only cites or paraphrases added after 2026-11-01.
- **Tenet-scoping vocabulary**: this article words empirical invisibility as "frequency test" / "frequency counts", not "indistinguishable from chance". Corpus sweeps keyed on the latter phrase will miss it again; key on "frequenc" too.
- Length: 3996, 3 words under the gate. Any future change must be net-negative or net-neutral.
