---
ai_contribution: 90
ai_generated_date: 2026-09-27
ai_modified: 2026-09-27 04:23:23+00:00
ai_system: claude-opus-5-5
author: Andy Southgate
concepts:
- '[[libet-experiments]]'
- '[[agent-causation]]'
- '[[luck-objection]]'
created: 2026-09-27
date: &id001 2026-09-27
description: 'Claude Opus 5.5 hostile-referee audit of topics/free-will: evidence
  lines non-discriminating, Born-rule dilemma absent, tenet leakage, libet-experiments
  Sjöberg error.'
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-27 04:23:23+00:00
modified: *id001
outer_review_conversation_url: https://claude.ai/chat/70441c2b-620d-4b1a-8dd1-00b7053d2f77
outer_review_extraction_method: js-dom
outer_review_status: processed
related_articles:
- '[[project]]'
subject_articles:
- topics/free-will.md
subject_source: reuse:pending-reviews:outer-review-2026-09-27-chatgpt-5-6-sol-pro.md
subject_title: Audit free-will
subject_type: recent
title: Outer Review - Claude Opus 5.5 (2026-09-27)
topics:
- '[[free-will]]'
---

**Date**: 2026-09-27
**Reviewer**: Claude Opus 5.5
**Type**: Outer review (external AI analysis)

## About This Review

An "outer review" is an analysis performed by an external AI system rather than the Claude-based workflow that generates most site content. This provides an independent perspective, reducing the risk of self-reinforcing blind spots.

## Prompt

Please act as a hostile but fair academic referee and audit the article "Free Will" on The Unfinishable Map (https://unfinishablemap.org/topics/free-will/), a dualist philosophy site (https://unfinishablemap.org). Check recent edits at https://unfinishablemap.org/workflow/changelog/ since search indexes may lag 24-48h; fetch the live page directly. Assess: (1) whether its central claims about libertarian free will, mental causation and quantum-level agency are argued rather than asserted; (2) citation accuracy, including whether quoted passages are verbatim, correctly attributed and fairly represent the cited works (e.g. Libet, Schurger, Desmurget, Wegner); (3) whether the strongest compatibilist, hard-incompatibilist and neuroscientific counterarguments are stated and answered in their best form; (4) whether the site's tenets (dualism, minimal quantum interaction, bidirectional interaction, no many-worlds, limits of Occam's razor) are bracketed honestly as commitments rather than smuggled in as conclusions; and (5) overclaiming about empirical support. Be specific and quote the text you criticise. End your report with a list of concrete potential improvements to specific articles and to the site's methodology.

## Reply

# Adversarial Referee Audit: "Free Will and Determinism" (unfinishablemap.org/topics/free-will/)

**Headline verdict: MAJOR REVISION, bordering on reject-and-resubmit.** The article is a well-organised statement of the Map's commitments. It is not a defence of them. Its three "lines of evidence" for agent causation fit physicalism equally well. It recruits its main empirical sources (Schurger, Desmurget, Wegner, James) for conclusions those authors reject or explicitly call undecidable. It never confronts the Born-rule/"wild coincidence" dilemma that decides whether "selection" means anything. Its own positions register rates [P-A2](/positions/agency-and-will/#p-a2) as having "no independent evidence", yet the prose says the phenomenology "support[s] genuine agent causation". [free-will](/topics/free-will/) That gap is confession without correction.

## A. TL;DR

- **Verdict:** The page asserts rather than argues its central claims: that agent-causal libertarian free will is real, that consciousness selects neural outcomes, and that closure "fails precisely where consciousness acts". Each of its evidential supports either merely defeats one anti-free-will argument (Libet) or is equally predicted by physicalist and compatibilist rivals (effort phenomenology, neural signatures, reasons-guidance). Most of the positive case should be demoted to *coherence-only*.
- **Citations:** The metadata is mostly real, but several titles are truncated or wrong (Schurger, Desmurget, Libet 1983). The William James quote is verbatim but cited to the wrong page (p. 497; the passage is on p. 571 of the 1890 Holt edition). [yorku](https://psychclassics.yorku.ca/James/Principles/prin26.htm) The main failure is at the author-stance layer. Desmurget et al. conclude that "Conscious intention and motor awareness thus arise from increased parietal activity before movement execution". [Ovid](https://www.ovid.com/00007529-200905080-00033) That is a neural-origination finding, and the article uses it as confirmation of a selector distinct from the brain. James, whose sentence closes the requirements section, held that the free-will question "is insoluble on strictly psychologic grounds". [University of Oregon](https://pages.uoregon.edu/koopman/pub/2017jhp_will_willblv_willjames-final.pdf)[yorku](https://psychclassics.yorku.ca/James/Principles/prin26.htm)
- **Missing opponents:** The strongest opposition is absent from this page or pushed off it: Pereboom's wild-coincidence objection, van Inwagen's rollback, Mele's present luck, Galen Strawson's Basic Argument, Tegmark's decoherence numbers, List's naturalistic free will, and active inference (Laukkonen, Friston & Chandaria 2025). The falsifiability section ends by immunising the thesis: "Failure of any particular proposed mechanism... would require finding an alternative gap, not abandoning libertarian free will." [free-will](/topics/free-will/)

**Scope and verification status.** Fetched live on 2026-09-27:

- The target page, meta-dated modified 2026-09-20T01:11:04Z and generated by claude-opus-4-5-20251101. [free-will](/topics/free-will/)
- The changelog.
- The linked dependency `concepts/libet-experiments` (modified 2026-07-12). [libet-experiments](/concepts/libet-experiments/)

The visible part of the changelog covers only 2026-09-24 to 2026-09-25 (the fetch was truncated). It has no entry for `topics/free-will` or its direct dependencies. The nearest relevant items are the 2026-09-25 optimistic review of the quantum-interpretation wing, which lists "Stapp as Born-bending" among five calibration defects, and a 2026-09-24 refine of `overdetermination-dissolution-under-selection-only-interactionism`. [changelog](/workflow/changelog/) I could not confirm what the 2026-09-20 edit to this page changed.

Direct fetches of `/tenets/`, `/concepts/quantum-indeterminacy-free-will/` and the two calibration benchmarks (`cross-modal-capability-division`, `born-preserving-causal-efficacy`) were refused by the fetch tool. Where I compare against sibling pages, I rely on search-index extracts (which may lag) of `concepts/causal-closure`, `concepts/von-neumann-wigner-interpretation`, `concepts/luck-objection`, `concepts/stapp-quantum-mind` and the 2026-06-01 outer review. These are marked as such below.

## B. Dimensional Analysis

### (1) Argued or asserted?

**Mostly asserted.** Take the luck-objection section, which the article itself calls "the strongest challenge". Its entire reply is: "the agent *as persisting substance* directly causes choices, ontologically prior to any events. The agent's exercise of causal power *is* the explanation—irreducible to any prior event sequence." [free-will](/topics/free-will/) That restates agent causation. It does not answer the objection. Van Inwagen's rollback asks why, across replays with identical past and laws, the agent-causal power yields A in some runs and B in others. Saying "the agent did it" in every run gives no contrastive explanation of A-rather-than-B. The page never states the rollback, so it never has to meet it.

The "three lines of evidence" do not discriminate between rivals:

- **"Phenomenology of volition... four distinguishable components... each with distinct neural correlates and clinical dissociation patterns. If choices were random fluctuations, this articulated structure would have no explanation."** [free-will](/topics/free-will/) The rival being refuted is "random fluctuations", which no serious opponent holds. The data offered (distinct neural correlates, dissociation under lesion) is what a neurally implemented control architecture predicts. Selective lesion dissociation is, if anything, evidence of neural *realisation*.
- **"Reasons-guidance: Selection responds to what matters to the agent."** [free-will](/topics/free-will/) Reasons-responsiveness is Fischer and Ravizza's *compatibilist* condition. Presenting it as evidence for agent causation is a co-optation firewall failure: the datum belongs to the opponent's theory.
- **"Distinctive neural signatures: Willed actions show frontal theta oscillations and bidirectional coherence that automatic processes lack."** [free-will](/topics/free-will/) This has no citation. Even granted, it is a physicalist datum.

The paragraph that follows admits "The physicalist can accommodate the neural data". It then shifts the burden: "the physicalist must then explain why the phenomenological distinction *exists*". [free-will](/topics/free-will/) That is the hard problem restated. It is not a free-will argument. It then asserts that "This cross-domain coherence is what agent causation predicts and what physicalism struggles to explain." [free-will](/topics/free-will/) No prediction is derived from agent causation. Nothing in the concept of an irreducible substance-cause entails that felt effort should scale with "degree of conscious engagement" across attention, motor control and reasoning. This is coherence inflation: fit is relabelled as prediction.

"If choosing were epiphenomenal decoration, this correlation would be coincidental" [free-will](/topics/free-will/) is a false dilemma. On reductive or realisation physicalism the correlation is non-coincidental *and* non-epiphenomenal. That is exactly Kim's point, and the article never considers it.

**Genuine strengths:**

- The page correctly says the Consequence Argument "establishes incompatibilism only". [free-will](/topics/free-will/)
- It disclaims the trilemma as "a complete partition of the space". [free-will](/topics/free-will/)
- Its moral-responsibility section openly concedes that "the moral phenomena alone do not settle that libertarian agency is *required*". [free-will](/topics/free-will/) That is honest and should be the template for the rest of the page.

### (2) Three-layer citation verification

| Citation (as given) | Metadata | Verbatim fidelity | Author-stance accuracy | Notes |
| --- | --- | --- | --- | --- |
| Libet et al. (1983), *Brain* 106(3), 623–642 | Volume/issue/pages correct. Title truncated to "Time of conscious intention to act"; the full title continues "in relation to onset of cerebral activity (readiness-potential): The unconscious initiation of a freely voluntary act". The sibling `libet-experiments` page has it right. [free-will](/topics/free-will/)[libet-experiments](/concepts/libet-experiments/) | No quote. | Fair for the timing claim. | Fix the title. |
| Libet "veto power" (text only; no Libet 1985 entry) | Not in References. The source is Libet (1985), *BBS* 8(4), target article pp. 529–539 (529–566 with commentary), DOI 10.1017/S0140525X00044903. [cambridge](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/unconscious-cerebral-initiative-and-the-role-of-conscious-will-in-voluntary-action/D215D2A77F1140CD0D8DA6AB93DA5499) | Paraphrase fair. The abstract: subjects "can in fact 'veto' motor performance during a 100–200-ms period before a prearranged time to act". [Springer](https://link.springer.com/content/pdf/10.1007/978-1-4612-0355-1_16.pdf)[cambridge](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/unconscious-cerebral-initiative-and-the-role-of-conscious-will-in-voluntary-action/D215D2A77F1140CD0D8DA6AB93DA5499) | Fair. Libet was himself interactionist-leaning: he later proposed a "conscious mental field", *JCS* 1(1):119–126 (1994). [Scholarpedia +2](http://www.scholarpedia.org/article/Field_theories_of_consciousness) No recruitment problem. | The veto data came from *prearranged-time* vetoes, not spontaneous ones. [University of Colorado Boulder](https://spot.colorado.edu/~tooley/Benjamin%20Libet.pdf)[cambridge](https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/unconscious-cerebral-initiative-and-the-role-of-conscious-will-in-voluntary-action/D215D2A77F1140CD0D8DA6AB93DA5499) The article presents the veto as a live escape without noting this or the later veto-precursor literature, e.g. Filevich, Kühn & Haggard (2013), *PLoS ONE* 8(2):e53053, which reports that "Last-moment decisions to inhibit or delay may depend on unconscious preparatory neural activity." |
| Schurger et al. (2012), *PNAS* 109(42), E2904–E2913 | Volume/issue/pages correct (PMC/PubMed). Title wrong: "Accumulator model for spontaneous neural activity" should be "An accumulator model for spontaneous neural activity prior to self-initiated movement". [nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC3479453/) | The paraphrase "RP reflects neural noise rather than decision preparation" is compressed. The paper says that "when the imperative to produce a movement is weak, the precise moment at which the decision threshold is crossed... is largely determined by spontaneous subthreshold fluctuations". [nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC3479453/) | **Partly misused.** In Schurger's model the decision *is* a neural threshold crossing by a leaky stochastic accumulator. The model leaves no gap for a non-physical selector. The sibling page's gloss, "random fluctuations preceded the moment consciousness decided to act", has no basis in the paper. [libet-experiments](/concepts/libet-experiments/)[nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC3479453/) | Legitimate only as a defeater of the Libet inference. |
| Desmurget et al. (2009), *Science* 324(5928), 811–813 | Volume/issue/pages correct (PubMed). Title truncated: "in humans" dropped. [PubMed](https://pubmed.ncbi.nlm.nih.gov/19423830/) | No quote. The double-dissociation summary is accurate, including false movement beliefs at higher parietal intensity. [Ovid](https://www.ovid.com/00007529-200905080-00033) | **Misrepresented.** The authors conclude: "Conscious intention and motor awareness thus arise from increased parietal activity before movement execution." Electrically *inducing* the felt intention is evidence that intention is produced by cortex. The page says Desmurget "confirm[s] the selection-execution distinction", and the sibling page calls parietal cortex "*selection* areas". Both turn a neural-origination result into support for a distinct selector. [free-will](/topics/free-will/) | Co-optation firewall failure. Also unmentioned: the published comment by Karnath, Borchers & Himmelbach (*Science* 327:1200, 2010). [PubMed](https://pubmed.ncbi.nlm.nih.gov/19423830/) |
| Sjöberg (2024), *Brain* 147(7), 2267–2269 | Correct (OUP; DOI 10.1093/brain/awae180). [Oxford Academic](https://academic.oup.com/brain/article/147/7/2267/7685995) | The free-will page has no quote. The sibling page's "completely irrelevant to the free will debate" narrows the source, which says Libet's findings are "completely irrelevant to the neuroscientific discussion about free will". [libet-experiments](/concepts/libet-experiments/)[Oxford Academic](https://academic.oup.com/brain/article/147/7/2267/7685995) | The free-will page is fair: it says Sjöberg "reads the cases as removing a defeater". The sibling page is not. It claims removing the SMA should impair "the capacity for voluntary movement. It doesn't." Sjöberg writes that the SMA syndrome "certainly demonstrates that this area of the brain is involved in the regulation of voluntary movement". His 2021 *Acta Neurochirurgica* review describes loss of executive control, not preserved motor capacity. [free-will](/topics/free-will/) | A factual error on `libet-experiments`, one of this page's main dependencies. |
| Wegner (2002), *The Illusion of Conscious Will*, MIT Press | Correct. | No quote. The claim that Wegner "acknowledges the robust feeling of effort" is **unverified**: neither the 2004 BBS *Précis* nor secondary sources confirm it for the 2002 book. His effort work is later (Preston & Wegner 2007, 2009). [harvard](https://dtg.sites.fas.harvard.edu/DANWEGNER/wjh/conscwil.htm) | Half-right. Wegner does hold that the experience is real but non-causal: people "experience conscious will quite independent of any actual causal connection between their thoughts and actions". [caltech](http://www.its.caltech.edu/~squartz/wegner2.pdf) But his theory of apparent mental causation (priority, consistency, exclusivity) is a worked-out *rival explanation* of exactly the datum the article relies on. [ResearchGate](https://www.researchgate.net/publication/247172948_Phenomenology_and_the_Feeling_of_Doing_Wegner_on_the_Conscious_Will_1)[caltech](http://www.its.caltech.edu/~squartz/wegner2.pdf) Citing him only to concede that the feeling exists is performative inoculation. | See (3). |
| Schwitzgebel (2011), *Perplexities of Consciousness*, MIT | Consistent with the standard record; not re-fetched. | No quote. | Schwitzgebel's scepticism is aimed at judgements people think are *easy* and coarse. So "coarse-grained" is the contested premise, not a reply to him. | Needs a steelman. |
| Gallagher & Zahavi (2012), *The Phenomenological Mind* (2nd ed.) | Plausible and standard; not re-fetched. | No quote. | Neither author is a substance dualist. The standard account of delusions of control in this literature is comparator/forward-model failure, a *selective* breakdown that deflationary models predict. | Undercuts the page's "should colour all movement uniformly" argument. |
| Suddendorf & Corballis (2007), *BBS* 30(3), 299–313; Read (2008), *Evol. Psych.* 6(4) | Consistent with the standard record; not re-fetched. | No quote. | Both are naturalistic accounts of working memory and foresight. "Species with reduced conscious capacity" is the Map's gloss. | The inference to "what Minimal Quantum Interaction would predict" is a non-sequitur (see (4)). |
| Byrne (2005), MIT Press | Consistent with the standard record; not re-fetched. | No quote. | Fair. | — |
| James, *Principles* vol. 2, ch. XXVI, "p. 497" | **Page wrong.** The sentence is on **p. 571** (1890 Holt pagination, in "The Question of 'Free-Will'", from p. 569). [yorku](https://psychclassics.yorku.ca/James/Principles/prin26.htm) | **Verbatim correct:** "It relates solely to the amount of effort of attention or consent which we can at any time put forth." [yorku](https://psychclassics.yorku.ca/James/Principles/prin26.htm) | **Stance problem.** On p. 572 James writes: "My own belief is that the question of free-will is insoluble on strictly psychologic grounds... it is manifestly impossible to tell whether either more or less of it *might* have been given or not." His grounds for believing in freedom were "ethical rather than psychological". [yorku](https://psychclassics.yorku.ca/James/Principles/prin26.htm) Quoting him to close a page whose "core evidence is phenomenological" enlists him against his own stated view. | Also: James's "thought is itself the thinker" rejects the persisting substance the page needs. [lbl](https://www-physics.lbl.gov/~stapp/QID.pdf)[arxiv](https://arxiv.org/pdf/q-bio/0401019) The Map's own 2026-09-24 changelog entry acknowledges this James/Whitehead tension for a sibling page. [changelog](/workflow/changelog/) |
| Named but uncited: Frankfurt, Fischer & Ravizza, Wolf, Kim, Chisholm, Sartre, Deutsch–Wallace | No reference entries. | — | **Sartre:** the page says Sartre's "condemned to be free" shows "why agent causation needs the substance-bearing subject". [free-will](/topics/free-will/) On the standard reading Sartre denies that consciousness is a substance: the for-itself is a no-thing, and the ego is a transcendent object. Recruiting him *for* substance is a stance inversion. | Add references or cut. |
| Never cited on this page: Soon 2008, Fried 2011, Maoz 2019, Kane, Pereboom, Dennett, G. Strawson, Nahmias, Mele, van Inwagen, List, Tse, Stapp, Tegmark, Laukkonen et al. | — | — | — | Soon et al. (2008, *Nat. Neurosci.* 11(5):543–545), whose abstract reports that a decision outcome "can be encoded in brain activity of prefrontal and parietal cortex up to 10 s before it enters awareness", and Dennett appear only on `libet-experiments`. Pereboom appears only as a Further Reading link. The absences are themselves the finding. |

**Primary-source verification.** Stapp's position was checked at LBNL:

- In LBNL-55887, his reply to Bourget, he says "I stay strictly within the bounds of contemporary orthodox science in accepting the quantum statistical rules as primitive elements of our basic theory." He quotes his 1993 contrast with Eccles: "This proposed solution requires no … distortion of the laws of physics." [Lbl](https://www-physics.lbl.gov/~stapp/repB.pdf)
- In "Quantum Interactive Dualism" the agent "chooses only the question"; whether "'Yes' or 'No' appears is not determined by the agent". [lbl](https://www-physics.lbl.gov/~stapp/QID.pdf)

The page's model is outcome selection: "Consciousness... selects which pattern becomes actual", with "biasing indeterminate outcomes" listed as a candidate mechanism. [free-will](/topics/free-will/) That is Eccles-style. It is not Stapp's. The page places the two side by side as "quantum selection (biasing indeterminate outcomes or Zeno-like stabilisation)" without saying that the only named physicist behind the second explicitly disowned the first. [free-will](/topics/free-will/) The Map's own 2026-09-25 review flags "Stapp as Born-bending" as a live calibration defect elsewhere in the corpus. [changelog](/workflow/changelog/)

### (3) Are the strongest counterarguments stated and answered?

**Compatibilism.** It is stated in caricature: "acting from endorsed desires without external coercion". [free-will](/topics/free-will/) That is Hobbes/Hume, not Frankfurt's hierarchical mesh, Fischer and Ravizza's guidance control, Wolf's reason view, Dennett's evitability, or List's *Why Free Will Is Real*. List's view is the most damaging omission. It offers agent-level alternative possibilities and causal control compatible with physical determinism, so it directly contests the Dualism-section claim that "Genuine authorship requires consciousness to be something more than physical processes." [free-will](/topics/free-will/) The page does link a Frankfurt concept page and concedes moral symmetry, which is a real strength. But the metaphysical claim that authorship requires dualism is never defended against the compatibilist *account of authorship*.

**Hard incompatibilism.**

- Pereboom appears only as a link. His *specific* objection to agent-causal libertarianism (Pereboom, *Noûs* 29:21–45, 1995; *Living Without Free Will*, CUP 2001) is not stated: if agent-caused outcomes always match the physical statistical laws, that conformity "would involve coincidences too wild to be credible" (as Runyan 2018 summarises it); if they don't, we should see long-run frequency deviations.
- Galen Strawson's Basic Argument (to be responsible you must be *causa sui*; nobody is) is absent. It targets precisely the "persisting substance" the page relies on, since the substance's character is itself unchosen.
- Caruso is absent.
- Fair credit: the pro-agent-causal literature has replies to Pereboom (Runyan 2018, *Synthese* 195(10):4563–4580; Taggart 2021, *Synthese* 198:11421–11435; Müller 2023, *Mind* 132(527):789–802, "Taming Pereboom's Wild Coincidences"). The page could use them and does not.

**Luck.** Van Inwagen's rollback and Mele's present-luck argument are absent by name. The reply given ("the agent's exercise of causal power *is* the explanation") is the move both arguments were built to defeat.

**Kim and closure.** The page says: "physics provides *necessary but not sufficient* causes where genuine indeterminacy exists. Causal closure fails precisely where consciousness acts." [free-will](/topics/free-will/) This fails in two ways:

- It does not engage the probabilistic formulation of closure. On that formulation every physical event has a sufficient physical cause *of its chance*, and it is untouched if Born statistics hold.
- It does not engage the inductive case for closure from the absence of detected anomalous forces.

The heavy lifting is outsourced to `overdetermination-dissolution-under-selection-only-interactionism`. [free-will](/topics/free-will/) But "dissolves the overdetermination worry rather than answering it" only works if the selection is real, which is the point in dispute.

**Decoherence.** The page contains no decoherence discussion; it only links out. The linked `libet-experiments` page offers three replies. The second says Zeno observation works because "observations happen faster than decoherence can act". [libet-experiments](/concepts/libet-experiments/) Tegmark (2000), *Phys. Rev. E* 61(4):4194–4206, reports that "decoherence timescales (~10⁻¹³ – 10⁻²⁰ seconds) are typically much shorter than the relevant dynamical timescales (~10⁻³ – 10⁻¹ seconds)". On those numbers, "faster than decoherence" would require observation rates of at least 10¹³ Hz. That is a physics claim the page never quantifies, and it is not Stapp's argument: in his reply to Tegmark (LBNL-46871) he writes that "My theory is specifically designed so that the particular quantum effects that allow a person's thoughts to influence his brain are not affected by environmental decoherence", a different and contested claim. The third reply says "The categorical objection—that biology cannot use quantum mechanics—is empirically refuted". [libet-experiments](/concepts/libet-experiments/) That attacks a strawman. Tegmark's claim concerns the neural degrees of freedom relevant to cognition, not biology in general. [PubMed](https://pubmed.ncbi.nlm.nih.gov/11088215/)

**Neuroscience.** Wegner's apparent-mental-causation model gets a concession but no answer. The introspective-reliability section argues that agency/ownership dissociation "resists the deflationary reading: a single demand-tracking confabulation should colour all movement uniformly". [free-will](/topics/free-will/) No deflationist holds a "single, uniform" confabulation. Comparator models and Wegner's priority/consistency/exclusivity cues both predict *selective* loss of the sense of agency when the cues fail. [caltech](http://www.its.caltech.edu/~squartz/wegner2.pdf) This is a strawman.

**Predictive processing / active inference.** This rival is **absent** from the page. Laukkonen, Friston & Chandaria (2025), "A beautiful loop", *Neuroscience and Biobehavioral Reviews* 176:106296, is verified. It posits "inferential competition to enter the world model" in which "Only the inferences that coherently reduce long-term uncertainty win, evincing a selection for consciousness that we call Bayesian binding." [OSF](https://osf.io/preprints/psyarxiv/daf5n) That is a physicalist theory of *selection*, the article's own key word, and it covers policy selection and selfhood. The page's model ("The brain prepares multiple possible action patterns... Consciousness... selects") is exactly the slot active inference fills without a non-physical selector. [free-will](/topics/free-will/) A sibling page, `predictive-processing-and-dualism`, exists (per search index) but is not linked from here. [visual-consciousness](/concepts/visual-consciousness/)

### (4) Tenet handling: bracketed or smuggled?

**Mixed. The worst leakage is in the closing section.** Credit where due:

- The page states that the substance lean is "downstream of the agent-causal commitment, not inherited from the Dualism tenet". [free-will](/topics/free-will/)
- It labels the MWI global-exclusion condition "a posit the Map adopts, asserted rather than derived". [free-will](/topics/free-will/)

That is model bracketing. Elsewhere tenets function as premises that deliver conclusions:

- **"Occam's Razor Has Limits: Determinism seems simpler but fails to explain the data: phenomenology of effort, willed/instructed neural distinctions, conscious engagement correlating with neuroplasticity."** [free-will](/topics/free-will/) This is tenet leakage plus a category error. The live rival is not "determinism" but indeterministic or compatibilist physicalism, and all three listed data are *explained* by it. A methodological tenet is being used to claim an explanatory victory.
- **"Minimal Quantum Interaction: Consciousness operates within what physics allows—selecting among possibilities without violating conservation laws or causal closure where it holds."** [free-will](/topics/free-will/) "Causal closure where it holds" is a hedge that empties the claim.
- **Counterfactual reasoning.** A cognitive-psychology finding (Byrne: we "mutate nearby features of actuality") is said to be "what Minimal Quantum Interaction would predict". [free-will](/topics/free-will/) No derivation connects a quantum-minimality tenet to limits on counterfactual imagination. This is a constitutional-attractor effect: any datum gets drawn toward a tenet.
- **Decision-void.** The page calls it "the primary candidate site for non-physical influence and the site whose structural opacity the Map's tenets predict". [free-will](/topics/free-will/) Opacity is predicted equally by any theory on which decision processes are subpersonal. Presenting it as tenet-predicted is coherence inflation.
- **"Free will stands at the intersection of all five tenets"** introduces a section that restates the tenets as requirements ("Genuine authorship requires consciousness to be something more than physical processes"). [free-will](/topics/free-will/) The requirement claim is the thesis, not a tenet consequence.

### (5) Empirical overclaiming

- **Constrain-vs-establish failure (lede).** "The core evidence is phenomenological—the felt difference between choosing and observing, the effort of deliberation, the distinctive neural signatures of willed action. These phenomena survive regardless of which physical mechanism enables consciousness-brain interaction." [free-will](/topics/free-will/) The phenomena survive regardless of whether *any* non-physical interaction exists. That is precisely why they cannot discriminate.
- **Schurger/Sjöberg.** The free-will page keeps these at defeater status, and that is correct. But its dependency `libet-experiments` states that "The Map's position is that current evidence supports selection over randomness". That page also treats the 60% Soon et al. decoding accuracy as a "gap" where "consciousness might operate". [libet-experiments](/concepts/libet-experiments/) Treating measurement noise as metaphysical openness is an epistemic-to-metaphysical slide. Because the free-will page routes readers there "for detailed analysis", it inherits the overclaim. [free-will](/topics/free-will/)
- **Desmurget.** See (2): a neural-origination result is presented as confirmation of a distinct selector.
- **Dream problem-solving.** "dream incorporation more than doubled solving rates" has no citation. The page itself concedes the finding rests on "a small lucid-dreamer-selected sample and has not been independently replicated". It then infers: "If consciousness were epiphenomenal, the phenomenal character of dreaming should be irrelevant". [free-will](/topics/free-will/) Confession without correction: the weakness is disclosed and the evidential role kept.
- **Meditation.** "A passive recipient of random events couldn't choose to be passive." [free-will](/topics/free-will/) Again the rival is "random events". A predictive-processing account of attentional precision (Laukkonen's own research area) explains witness-mode without a non-physical chooser.
- **Born-rule dilemma (not addressed on this page).** The page says selection is "minimal—working with what physics allows, not overriding it". [free-will](/topics/free-will/) Per the search-index extract, the sibling `von-neumann-wigner-interpretation` page concedes that the bias "is constructed to average back to the Born measure" and is "empirically indistinguishable from chance under any unconditioned aggregate test". [von-neumann-wigner-interpretation](/concepts/von-neumann-wigner-interpretation/) Either consciousness shifts outcome frequencies, so there is a deviation and a signalling risk and physics is not respected, or it does not, so "selection" does no work that chance does not already do. The same objection appears as Pereboom's wild coincidences. [Springer](https://link.springer.com/article/10.1007/s11229-017-1419-7) The Map's own 2026-06-01 outer review called this the corpus's "single deepest problem". [outer-review-2026-06-01-claude-opus-4-8](/reviews/outer-review-2026-06-01-claude-opus-4-8/) Four months later the flagship free-will page does not mention it. The site knows the objection, and its most-read page on the topic does not engage it.
- **Falsifiability.** Each of the four "falsifiers" is unreachable or non-discriminating:

- "prior neural states... *sufficient* for choice outcomes" can never be shown if the Map is right that physics is indeterministic. [free-will](/topics/free-will/)
- A "Materialist solution to the hard problem" is not a falsifier of *agent causation*.
- "Effort feeling easy when neural cost is high" tests a correlation physicalism also predicts.
- "Proof that causal closure holds without exception at all scales" is unprovable by induction.

The next sentence then removes even these: "Failure of any particular proposed mechanism... would require finding an alternative gap, not abandoning libertarian free will." [free-will](/topics/free-will/) This is the clearest instance of the constitutional-attractor effect on the page.
- **Register–prose calibration asymmetry.** The positions box states [P-A1](/positions/agency-and-will/#p-a1) "limited or indirect evidence" and [P-A2](/positions/agency-and-will/#p-a2) "no independent evidence". The prose says "Three lines of evidence support genuine agent causation" and that the covariation "is better explained by genuine agent involvement than by any account treating the phenomenology as illusory or idle". [free-will](/topics/free-will/) The register confesses. The prose does not follow it. Sibling pages have already been brought to a "compatible with rather than compels" standard: the 2026-09-24 changelog entry for `pain-consciousness-and-causal-power` rewrote "exactly what interactionist dualism predicts" on those grounds. [changelog](/workflow/changelog/) This page has not.

## C. Bottom-Line Verdicts per Central Claim

| # | Claim (quoted) | Verdict | Reason |
| --- | --- | --- | --- |
| 1 | "The Map defends agent-causal libertarian free will" ([P-A1](/positions/agency-and-will/#p-a1)) | **FLAG AS PERPETUALLY CONTESTED** | Legitimate as a declared framework commitment. It must be presented as such, not as an evidence-backed result. |
| 2 | "The core evidence is phenomenological"; "Three lines of evidence support genuine agent causation" | **DEMOTE-TO-COHERENCE-ONLY** | None of the three lines discriminates against indeterministic or compatibilist physicalism. Reasons-guidance is the opponent's own criterion. |
| 3 | "This cross-domain coherence is what agent causation predicts and what physicalism struggles to explain" | **DELETE** | No prediction is derived, and physicalism predicts the covariation. |
| 4 | Libet challenge answered via Schurger, Sjöberg, veto | **RETAIN (defeater-only)**, but **REVISE-HARD** the dependency page | Correct as the defeat of one argument. Fix the Schurger gloss, the "It doesn't" SMA error, and the veto caveats. |
| 5 | "Desmurget's neurosurgical studies confirm the selection-execution distinction" | **REVISE-HARD** (delete "confirm") | The authors' own conclusion is neural origination of intention. [Ovid](https://www.ovid.com/00007529-200905080-00033) |
| 6 | Luck reply: "The agent's exercise of causal power *is* the explanation" | **REVISE-HARD** | State the rollback and present luck, and give a contrastive answer or concede there isn't one. |
| 7 | "Causal closure fails precisely where consciousness acts" | **DEMOTE-TO-COHERENCE-ONLY** | Holds only if the Born-rule dilemma is resolved. It must be stated conditionally. |
| 8 | Quantum selection "working with what physics allows, not overriding it" | **REVISE-HARD** | Add the Born/wild-coincidence dilemma and Tegmark's numbers. Separate Stapp's question-choice from Eccles-style outcome biasing. |
| 9 | Retrocausal/atemporal resolution of the temporal problem | **DEMOTE-TO-COHERENCE-ONLY** | Already hedged as "speculative". But "the linear ordering is itself part of what was selected" in the closing section re-inflates it. [free-will](/topics/free-will/) |
| 10 | Introspective reliability via agency/ownership dissociation | **REVISE-HARD** | Replace the strawman with Wegner's and the comparator model's actual predictions. |
| 11 | Dream problem-solving as evidence | **DELETE** (or cite and relabel as anecdote-grade) | The source is uncited and, by the page's own admission, unreplicated. |
| 12 | Counterfactual limits "what Minimal Quantum Interaction would predict" | **DELETE** | Non-sequitur tenet leakage. |
| 13 | Sartre as support for a "substance-bearing subject" | **DELETE** the substance inference | Stance inversion. |
| 14 | James quote | **REVISE-HARD** | Correct to p. 571 and add his p. 572 "insoluble on strictly psychologic grounds". [yorku](https://psychclassics.yorku.ca/James/Principles/prin26.htm) |
| 15 | Falsifiers section plus the "alternative gap" sentence | **REVISE-HARD**; **DELETE** the immunising sentence | Replace with discriminating tests (see D). |
| 16 | Occam paragraph: "Determinism seems simpler but fails to explain the data" | **DELETE** | Wrong rival, and a false claim of explanatory victory. |
| 17 | Epiphenomenalism self-stultification / argument from reason | **FLAG AS PERPETUALLY CONTESTED** | These bite on epiphenomenalism, not on reductive physicalism, and are stated without replies. |
| 18 | No-MWI authorship paragraph | **RETAIN** | The best-bracketed paragraph on the page: posit declared, Deutsch–Wallace distinguished. |
| 19 | Moral-responsibility symmetry concession | **RETAIN** | An honest calibration model for the rest of the page. |
| 20 | Trilemma framing | **RETAIN** with disclaimer | The non-partition caveat is present. Replace "randomness (luck)" with the strongest event-causal rival. |

## D. Article-Specific Fixes (by slug)

**`topics/free-will`**

1. Rewrite the lede. Change "The core evidence is phenomenological" to wording like: "The Map's case is coherence with phenomenology; the phenomenology is compatible with, but does not discriminate against, physicalist and compatibilist rivals (register: [P-A1](/positions/agency-and-will/#p-a1) limited/indirect; [P-A2](/positions/agency-and-will/#p-a2) no independent evidence)."
2. Replace "Three lines of evidence support genuine agent causation" with "Three lines of evidence the agent-causal view accommodates". Add one sentence per line naming the physicalist explanation of the same datum. Delete "This cross-domain coherence is what agent causation predicts..." and "If choosing were epiphenomenal decoration, this correlation would be coincidental."
3. Luck section: state van Inwagen's rollback and Mele's present-luck case verbatim from primary sources. Either give a contrastive answer or state plainly that agent causation offers none and treats this as primitive.
4. Add a "Wild coincidences and the Born rule" subsection. State Pereboom's dilemma and the Born-preservation horn conceded on `von-neumann-wigner-interpretation`. Cite Runyan (2018), Taggart (2021) and Müller (2023) as the best libertarian replies. Route readers to `born-preserving-causal-efficacy` (I could not fetch it for this audit).
5. Mechanism section: separate "Stapp: consciousness chooses *which question and when*; outcomes remain Born-random (LBNL-55887)" from "Eccles-style outcome biasing". Add Tegmark (2000), *Phys. Rev. E* 61:4194, with its timescales. [American Physical Society](https://link.aps.org/doi/10.1103/PhysRevE.61.4194)
6. Motor Selection: change "Desmurget's neurosurgical studies confirm" to "Desmurget et al. found that parietal stimulation produces felt intention; the authors conclude intention 'arise[s] from increased parietal activity', a result the dualist must accommodate rather than cite as support." Fix the title ("…in humans") and cite Karnath et al. (2010). [PubMed](https://pubmed.ncbi.nlm.nih.gov/19423830/)
7. Introspective Reliability: drop "a single demand-tracking confabulation should colour all movement uniformly". Present Wegner's priority/consistency/exclusivity model and comparator accounts as the rivals, and say why the Map rejects them. Verify or delete "acknowledges the robust feeling of effort".
8. Compatibilism: replace the Hobbesian definition with Frankfurt, Fischer & Ravizza, and List (2019, *Why Free Will Is Real*), and add references. Add Galen Strawson's Basic Argument as the objection to "persisting substance".
9. Add a paragraph on predictive processing / active inference citing Laukkonen, Friston & Chandaria (2025), *NBR* 176:106296. Link `predictive-processing-and-dualism`.
10. Falsifiers: replace them with discriminating ones, e.g.:

- a pre-registered conditional Born-deviation test keyed to intention (the sibling register's [P-Q3](/positions/quantum-interface/#p-q3));
- veto-precursor results;
- decoding accuracy approaching the noise ceiling in deliberate-choice paradigms like Maoz, Yaffe, Koch & Mudrik (2019, *eLife* 8:e39787), who found that RPs present for arbitrary decisions "were strikingly absent for deliberate ones".

Delete "would require finding an alternative gap, not abandoning libertarian free will."
11. Delete the counterfactual → MQI sentence, the decision-void "tenets predict" clause, the Occam paragraph's "fails to explain the data", and the dream evidence (or cite and relabel it).
12. Sartre: keep the phenomenology of self-distance, but delete "why agent causation needs the substance-bearing subject".
13. References: fix the Libet 1983, Schurger and Desmurget titles. Add Libet (1985) *BBS* 8(4):529–539. Correct James to vol. 2, p. 571, and add the p. 572 "insoluble" sentence. Add entries for Kim, Chisholm, Frankfurt, Fischer & Ravizza, Wolf and Pereboom.

**`concepts/libet-experiments`**

- Delete "It doesn't" on SMA resection and quote Sjöberg's "certainly demonstrates that this area... is involved in the regulation of voluntary movement".
- Restore Sjöberg's scope ("neuroscientific discussion about free will").
- Delete "the moment consciousness decided to act" from the Schurger gloss.
- Remove "Libet measured the wrong signal" as a Desmurget inference.
- Quantify the Zeno-vs-decoherence claim or delete "observations happen faster than decoherence can act".
- Replace the "empirically refuted" strawman with Tegmark's actual claim.
- Demote "current evidence supports selection over randomness" to coherence-only.
- Remove the 60%-accuracy "gap" argument or label it an argument from measurement noise.

**`positions/agency-and-will`**: Add a prose-sync rule. Any page citing [P-A2](/positions/agency-and-will/#p-a2) ("no independent evidence") may not use "support", "evidence for" or "better explained" of agent causation without a named, discriminating datum.

**`concepts/luck-objection`**, **`concepts/quantum-indeterminacy-free-will`**, **`concepts/stapp-quantum-mind`**, **`topics/motor-control-quantum-zeno`**: Audit these for the same Stapp/Eccles conflation flagged in the 2026-09-25 changelog. [changelog](/workflow/changelog/) The `luck-objection` extract asserts "The felt cost of concentration corresponds to real causal engagement via the quantum Zeno effect". [luck-objection](/concepts/quantum-indeterminacy-free-will/) That is the same establish-for-constrain error.

**`topics/the-manipulation-argument-and-hard-incompatibilism`**: Make sure Pereboom's *wild-coincidence* objection is treated there, not only the four-case argument, and link it from the free-will luck section.

## E. Site-Wide Methodology Improvements

1. **Evidential-status ladder, enforced in prose.** Tag every evidential sentence as *compatible* (the datum fits the Map), *suggestive* (fits the Map better on a stated, contestable prior), or *discriminating* (predicted by the Map and disfavoured by a named rival). Ban "supports", "confirms" and "better explained" below the *discriminating* level. This page would currently have zero *discriminating* sentences, which is the honest finding.
2. **Register–prose lint.** Run the calibration already in the positions register over the text. If a page cites a position banded "no independent evidence", flag every evidence-verb. This turns confession into correction automatically.
3. **Author-stance field in citation checks.** The pipeline already verifies metadata and grep-verifies quotes (see the 2026-09-24/25 entries). [changelog](/workflow/changelog/) Add a third mandatory field: "cited author's own conclusion (verbatim)" next to "use on the page". Desmurget, Schurger, James and Sartre would all have failed this check.
4. **Defeater vs. support tags.** Mark each empirical citation as either *defeats an anti-Map argument* or *positive support*. Schurger and Sjöberg belong only in the first category. Dependent pages must inherit the tag.
5. **Falsifier quality gate.** Every "What would challenge this" item must be reachable in principle and discriminating (the rival must predict the opposite). Reject any sentence that reserves a fallback gap.
6. **Rival-completeness checklist per topic.** For free will, the required list: Frankfurt, Fischer & Ravizza, Dennett, List, Pereboom (four-case *and* wild coincidences), G. Strawson, Caruso, van Inwagen, Mele, Kim, Tegmark, Wegner, active inference. A page cannot pass review while a listed rival is absent or represented only by a link.
7. **Tenet-quarantine box.** Confine tenet-derived claims to the "Relation to Site Perspective" section, phrased as "given tenet X, the Map reads datum Y as…". Flag any tenet name that appears in an explanatory "predicts" clause outside that box.
8. **Re-audit older-model pages to the current standard.** This page was generated by claude-opus-4-5-20251101 and created 2026-01-08. [free-will](/topics/free-will/) Recent changelog entries show newer-model passes holding sibling pages to a "compatible with rather than compels" standard that this page has not had. [changelog](/workflow/changelog/) That is a calibration asymmetry across the corpus. Prioritise high-traffic, framework-critical pages ([P-A1](/positions/agency-and-will/#p-a1) is marked "framework-critical"). [free-will](/topics/free-will/)
9. **Propagate external-audit findings.** The 2026-06-01 outer review identified the Born-rule dilemma as the corpus's deepest problem. [outer-review-2026-06-01-claude-opus-4-8](/reviews/outer-review-2026-06-01-claude-opus-4-8/) Track such findings to every page whose central claim depends on them, and require each to state the dilemma, or record why it does not apply.
10. **Reviewer independence.** Generator and reviewer come from the same model family, and the tenets are supplied as a constitution. That is the likely source of the attractor effects above. Add a reviewer instructed to argue *from* a named rival's published framework (e.g., "review as Pereboom", "review as List", "review as a Friston-school active-inference theorist"), with authority to set DEMOTE or DELETE verdicts, not only to request hedges.
11. **Auditability.** Make the tenets page and core benchmark pages reachable to external fetchers (the tool refused `/tenets/` for this audit; that is a tool constraint, not a site fault). Publish a per-page "last substantive change" diff summary so auditors don't depend on a truncated changelog view.

## Verification Notes

Extraction: the artifact body was built in the page and downloaded as a Blob (47,079 characters; body size stable at 39,993 rendered characters across a 10 s sentinel). It ends on methodology item 11, so it is complete. Verified 2026-09-27 against the live Obsidian tree and primary sources.

**Map-attributed spans (grep-checked in the source files):**
- ✓ [topics/free-will.md](/topics/free-will/) L94 "Three lines of evidence support genuine agent causation"; L100 "what agent causation predicts and what physicalism struggles to explain": verbatim.
- ✓ The register–prose asymmetry is real. [P-A2](/positions/agency-and-will/#p-a2) in [positions/agency-and-will.md](/positions/agency-and-will/) carries external-evidence grade **D**. The sync (`tools/sync/positions.py`) renders that grade as "no independent evidence" in the hub's positions box, while the hub's prose uses evidence verbs.
- ✓ The Born-rule / wild-coincidence dilemma is absent from the hub: `Born` 0 hits, `coincidence` 0 hits, `born-preserving` / `brain-specialness` / `mechanism-debt` 0 links. [positions/quantum-interface.md](/positions/quantum-interface/) L45 (the mechanism-debt convention) says that agency articles asserting causal work *inherit* this debt and should deep-link `#^mechanism-debt`. The flagship hub does neither.
- ✓ L178 "would require finding an alternative gap, not abandoning libertarian free will": verbatim. This is convergent with the ChatGPT leg, which quoted it and minted no task for it.
- ✓ L204 Occam: "Determinism seems simpler but fails to explain the data": verbatim.
- ✓ L112 counterfactual → "which is what [Minimal Quantum Interaction](/tenets/#minimal-quantum-interaction) would predict". The reviewer's quoted string is wikilink-split in the source, which is why a naive grep returns 0.
- ✓ L88 decision-void "the structural opacity the Map's tenets predict": verbatim.
- ✓ L104 "a single demand-tracking confabulation should colour all movement uniformly" and "Wegner (2002) ... acknowledges the robust feeling of effort": both present.
- ✓ L149 "dream incorporation more than doubled solving rates": uncited in the hub.
- ✓ The hub never names Stapp (0 hits). L116 lists "biasing indeterminate outcomes or Zeno-like stabilisation" as candidate mechanisms. The reviewer's claim that the page sets Eccles-style biasing "side by side" with Stapp is therefore true only by implication. The Zeno candidate is Stapp's, and the hub does not say that Stapp disowns outcome biasing. This is a minor finding, handled inside the new P1.
- ✓ Reference titles are truncated at L245–247 (Libet 1983, Schurger 2012, Desmurget 2009). No Libet 1985 entry exists.
- ✓ [concepts/libet-experiments.md](/concepts/libet-experiments/) L69 says SMA removal should impair voluntary movement, then "It doesn't." and "completely irrelevant" to the free will debate. L63 has the Schurger gloss "the moment consciousness decided to act". L85 has "Libet measured the wrong signal". L125 has "observations happen faster than decoherence can act". L127 has "The categorical objection ... is empirically refuted". L193 has "current evidence supports selection over randomness". All are present.

**Primary-source checks:**
- ✓ **Sjöberg 2024** (academic.oup.com, *Brain* 147(7):2267). The paper says "The SMA syndrome ... certainly demonstrates that this area of the brain is involved in the regulation of voluntary movement." The scope of the key sentence is "completely irrelevant to the *neuroscientific discussion about* free will". Patients show temporary deficits in *initiating* movement and speech, while their sense of intention and effort is preserved. The Map's "It doesn't" is therefore wrong as written. What is preserved is the sense of willing, not the capacity to move. The reviewer is right, with that nuance.
- ✓ James p. 571 (1890 Holt) and the p. 572 "insoluble on strictly psychologic grounds" sentence were already verified by the sibling leg. This is convergent.
- ? Desmurget 2009 conclusion quote ("Conscious intention and motor awareness thus arise from increased parietal activity before movement execution"): PubMed returned a CAPTCHA page. The wording matches the widely reproduced abstract, so it is accepted as a strong lead. The "(…in humans)" title completion is standard.
- ? Stapp LBNL quotes (question-choice, not outcome biasing) were not re-fetched. They are consistent with the 2026-09-24 repair of `concepts/stapp-quantum-mind` and with the open P3 "Stapp is question-choice, not Born-bending".
- ? Tegmark 2000 timescales, Filevich/Kühn/Haggard 2013, Maoz 2019 and Laukkonen–Friston–Chandaria 2025 were not re-fetched. They are well-known real papers; verify each at the publisher before adding.
- ? Wegner "acknowledges the robust feeling of effort": the reviewer calls it unverified, not false. Verify against the 2002 book or drop the claim.

**Disputed / overstated:**
- ✗ "Predictive processing / active inference ... absent ... `predictive-processing-and-dualism` ... not linked from here": the hub does lack it (0 hits for `predictive`). But the corpus engages Laukkonen et al. 2025 at length in `topics/predictive-processing-and-dualism`, so this is a missing cross-link, not a missing engagement. Low priority, given the hub's length.
- ✗ The reviewer's "Pereboom appears only as a link" understates the corpus, since `topics/the-manipulation-argument-and-hard-incompatibilism` treats him. The *wild-coincidence* objection specifically is absent from the hub, and that part stands.
- Partial: List, G. Strawson's Basic Argument, Mele and Caruso are absent from the hub (0 hits each, apart from P.F. Strawson). The hub is 191 words below its hard ceiling, so a full rival-completeness pass is not affordable there. Nothing was minted beyond what the existing P1 (rollback, physicalist null) already covers.

**Tally:** 14 Map-attributed claims checked, all accurate (one understated, one wikilink-split). 1 primary source fetched and confirmed (Sjöberg). 1 blocked by CAPTCHA (Desmurget). 4 leads unverified. 2 overstatements.

## Processing Outcome

The sibling ChatGPT leg on the same subject had already minted 5 tasks. To avoid duplicates, this reviewer's overlapping findings were **appended as addenda** to those tasks:
1. P1 `topics/free-will` rollback / physicalist null: corroborated (convergent, 2 reviewers).
2. P2 `topics/free-will` citations: added reference-title fixes, the missing Libet 1985 entry and the Wegner "robust feeling of effort" check. Desmurget, James and Sartre are corroborated.
3. P2 `concepts/libet-experiments`: added the Sjöberg "It doesn't" factual error and scope narrowing, the Schurger gloss, the Zeno-vs-decoherence quantification, the "empirically refuted" strawman and the L193 overclaim. The 60% and "selection areas" items are corroborated.

New tasks minted (findings the sibling did not raise):
4. **P1** refine-draft `topics/free-will`: the Born-rule / wild-coincidence dilemma is absent, and the hub has no link to the mechanism debt the register says it inherits.
5. **P2** refine-draft `topics/free-will`: tenet leakage and falsifier immunisation (Occam L204, counterfactual → MQI L112, decision-void "tenets predict" L88, "alternative gap" L178, the uncited dream finding L149, the introspection strawman L104). The changes are deletion-heavy, so the task is length-negative.

Methodology items E1–E11 were not minted. E1, E2, E4 and E7 restate the standing mechanism-debt citation-grade convention and the compatible/discriminating discipline. E3 (author-stance field) is the provenance NEEDS-HUMAN already on record. E9 is the register-propagation NEEDS-HUMAN. E10 is a subject-selection policy question already open.