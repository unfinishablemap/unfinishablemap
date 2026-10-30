---
ai_contribution: 100
ai_generated_date: 2026-10-30
ai_modified: 2026-10-30 10:06:57+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-10-30
date: &id001 2026-10-30
description: 'What a selecting agent who knows her own intention should believe about
  the outcome, if only conditionals on the conscious state are free: Lewis''s Principal
  Principle with the conscious state as admissible history, against Sebens-Carroll,
  QBism and Healey.'
draft: false
fold_target: concepts/quantum-probability-consciousness
human_modified: null
lastmod: 2026-10-30 10:06:57+00:00
modified: *id001
recommended_action: fold
related_articles: []
title: Research Notes - The Selecting Agent's First-Person Credence Rule
---

# Research: The Selecting Agent's First-Person Credence Rule

**Date**: 2026-10-30

**Task**: if consciousness tilts the token outcome while only conditionals on the conscious state are free ([P-Q2](/positions/quantum-interface/#p-q2)), what credence should the agent assign to an outcome given her own intention, and what replaces Everettian decision theory (Sebens & Carroll 2018) on the Map's one-world reading? Source review: `reviews/outer-review-2026-10-28-claude-fable-5-1.md`, inference 3.

**Search queries used**: Lewis "A Subjectivist's Guide to Objective Chance" admissible historical information; Crossref bibliographic queries for Kent 2015, Price 2012, Maudlin 2014, Saunders 2010, Albert 2010, Thau 1994, Spohn 1977, Dawid & Thébault 2015, Healey 2017, Hájek 2016, List & Pivato 2015, Bacciagaluppi & Ismael 2015, Ismael 2011, McQueen & Vaidman 2019, Brown & Ben Porath 2020, Lewis 1979, Wallace 2010; Dawid Thébault "Many worlds: decoherent or incoherent?" abstract; Maudlin 2014 critical study of *The Emergent Multiverse*; Brown Ben Porath "Everettian probabilities, the Deutsch-Wallace theorem and the Principal Principle"; Lewis 1981 causal decision theory dependency hypothesis.

**Raw artefacts read this run**: `pdftotext` of arXiv:1405.7577 (Sebens & Carroll, the accepted BJPS version dated 29 May 2015), arXiv:1408.1944v3 (Kent), arXiv:0906.2718v1 (Wallace, the preliminary version of "How to Prove the Born Rule"), arXiv:1301.3274v1 (Fuchs & Schack), arXiv:quant-ph/9609006 (Vaidman 1998); an OCR scan of Lewis (1980) as printed in the Jeffrey volume; the publisher PDF of Dawid & Thébault (2015); the Bacciagaluppi & Ismael (2015) essay review; the arXiv API abstract of Brown & Ben Porath (2020, arXiv:2010.11591); SEP HTML for "Quantum-Bayesian and Pragmatist Views of Quantum Theory" (Healey; revised 8 Sep 2026), "Many-Worlds Interpretation of Quantum Mechanics" (Vaidman; revised 17 Jun 2026) and "Causal Decision Theory" (revised 24 Oct 2024); Crossref JSON (with abstracts where deposited) for every DOI listed under Citations.

**Verification discipline.** Quotation marks are used only on wording matched as a literal substring in one of those artefacts after Unicode NFC normalisation and whitespace collapse; each is marked **[verified: source]**. Two extraction artefacts were hit and are recorded. (1) The Lewis scan is OCR'd with stray inter-letter spaces ("o u r", "t o", "a s", "o n"); quotations from it are given with those spaces closed, and nothing else altered. (2) `pdftotext` de-hyphenation joins line-broken compounds ("selflocating", "Bornrule", "quantummechanical"); quotes are cut before such a join or the join is flagged. (3) Curly and straight apostrophes and quotation marks are treated as equivalent. Everything not in quotation marks is paraphrase, and the source it was read in is named.

## Executive Summary

**The rule.** The Map does not need a new decision theory for the selecting agent. In a one-world chancy theory credence is tied to chance by Lewis's Principal Principle (Lewis 1980), and Lewis's own criterion counts historical information as admissible, history that matches "atom for atom, field for field, even spirit for spirit (if such there be)" **[verified: Lewis 1980 scan]**. If the conscious state is part of that history, then once an intention C has formed, the chance of a neural outcome O is the conditional P(O | do(C), X) that [the Born-preservation apex](/apex/born-preserving-causal-efficacy/) already writes down. An agent who knows C should set her credence in O to her expectation of that post-intention chance. The Born weight is the right credence for anyone who lacks C. It is also the chance *before* C forms, but only if forming an intention has a propensity distribution of its own. Born weights are single-case chances at the right *time*, then. They are not the chance at the moment of selection unless horn (b) holds.

**Horn (a) or horn (b)?** Horn (a), for any agent who accepts the Map's tenets. Tenet 3 defines Bidirectional Interaction as "consciousness biasing quantum indeterminacy in the brain toward patterns that express its content" **[verified: `tenets/tenets.md` L91]**. An agent who gives that definition any credence must expect content-expressing outcomes to be favoured given her intention, so her credence leaves the Born value in the direction of what she intends. An agent who is agnostic about the direction of the tilt can rationally hold Born-valued credence. That does not concede horn (b), because horn (b) is a claim about the *chances* and her credence is only her expectation over them. "Credal Born" and "chance Born" come apart.

**Verdict: mostly shared debt, plus one cost that belongs to the Map's chance ontology and not to its decision theory.** The part every one-world objective-chance view owes is the justification of the chance–credence link itself. Wallace says the Principal Principle "is postulated, not derived" in non-Everettian probability **[verified: arXiv:0906.2718]**. His and Saunders's claim that Everett does better by proving it is denied by Brown & Ben Porath (2020) **[verified: arXiv abstract]**. On that link the Map owes exactly what GRW or Copenhagen owes. What it owes beyond them comes in two parts. (i) Its chances move with no physical change: forming an intention changes the chance of O while the physical history is fixed. That is Tenets 1 and 3 restated in chance terms, and it is the real content of the reviewer's "non-standard decision theory". The decision theory itself is standard. (ii) If the Born weight is to be a chance at *any* time, the formation of conscious states needs propensities, which grants van Inwagen's rollback premise at that grain. Without them the Born match is Pereboom's wild coincidence, which [rollback-argument-against-agent-causation](/concepts/rollback-argument-against-agent-causation/) already records as one unwritten law.

**Recommended action: `fold`** into [quantum-probability-consciousness](/concepts/quantum-probability-consciousness/) §"The Missing Piece: First-Person Probability" (3,014 words, hard limit 3,500, gate `>=`, so 485 words of headroom; measured 2026-10-30 with `tools.curate.length.analyze_length`). A drafted ~230-word fold paragraph with three references is given below under "Drafted Fold Paragraph". The candidate rule is also drafted as toy-model desideratum 7 for [born-preserving-causal-efficacy](/apex/born-preserving-causal-efficacy/), which cannot take it until the open NEEDS-HUMAN length decision is made. Not `article`: see "Why Not a Topics Article".

## What the Corpus Already Has (not re-run here)

- The Everettian derivations and their critics (Deutsch–Wallace, Sebens–Carroll, Zurek; Albert, Kent, Price, Baker, Lewis 2007, Dawid & Friederich 2022) are surveyed in the `probability-decision-theory-against-many-worlds-2026-03-04` and `born-rule-derivation-attempts-2026-03-14` research notes and in [probability-problem-in-many-worlds](/topics/probability-problem-in-many-worlds/). The `mad-dog-everettianism-and-the-austere-hilbert-space-ontology-2026-09-11` note records that Carroll & Singh defer probability to exactly those two routes. This note adds only what bears on a *one-world agent-relative* rule.
- The rollback argument and the propensity fork are worked in [rollback-argument-against-agent-causation](/concepts/rollback-argument-against-agent-causation/) §"The Map's Reading: One Debt": if the conditionals are objective propensities the Map grants van Inwagen's premise; if not, it meets Pereboom's wild coincidences. This note supplies the credence side of that fork.
- O'Connor's "structured propensities" and their mapping onto the free conditionals are in [agent-causation-and-acting-for-reasons](/topics/agent-causation-and-acting-for-reasons/) (L52, L89).
- QBism and Healey are covered as the agent-centred family in [pragmatist-quantum-foundations-and-the-agent](/topics/pragmatist-quantum-foundations-and-the-agent/) and [qbism](/concepts/qbism/). Neither page states a chance–credence rule.
- The Principal Principle appears once in the live corpus, as Wilson's "Everettian Principal Principle" in [diverging-worlds-everettianism](/concepts/diverging-worlds-everettianism/) (L44). No page states Lewis's admissibility clause or applies it to the conscious state.
- **Originator correction for the task brief.** The brief says "Pereboom's rollback argument". The rollback argument is van Inwagen's (2000), as the corpus article states. Pereboom's argument is the wild-coincidences objection (Pereboom 2001, ch. 3; 2014). This note keeps them apart.

## Key Sources

### Lewis (1980), "A Subjectivist's Guide to Objective Chance"
- **Type**: book chapter, in R. C. Jeffrey (ed.), *Studies in Inductive Logic and Probability*, vol. II, University of California Press, pp. 263–293 (Crossref lists 263–294). Reprinted with postscripts in *Philosophical Papers* vol. II (1986).
- **Originator status**: Lewis names the principle and states the admissibility clause. He points to "a relative of the Principal Principle" discussed in Jeffrey's 1970 review of articles by David Miller et al. **[verified: scan]**, so the chance–credence link has precursors. Neither the name nor the admissibility clause predates him on this evidence.
- **Key points** (all **[verified: scan]**):
  - The name: "Since this principle seems to me to capture all we know about chance, I call it The Principal Principle."
  - Admissibility is defined by role: "Admissible propositions are the sort of information whose impact on credence about outcomes comes entirely by way of credence about the chances of those outcomes."
  - It has no definition: "I have no definition of admissibility to offer, but must be content to suggest sufficient (or almost sufficient) conditions for admissibility."
  - Historical information: "If a proposition is entirely about matters of particular fact at times no later than t, then as a rule that proposition is admissible at t." The example list includes "every detail" of "the structure of the coin, the tosser, other parts of the setup".
  - History is not restricted to the physical. A proposition is about history up to noon if it cannot tell apart two worlds alike "atom for atom, field for field, even spirit for spirit (if such there be)" up to then.
  - "Time-dependent chance and time-dependent admissibility go together." The labyrinth example has chance shifting as the walker's history unfolds.
  - The qualifier "as a rule" covers the case where "the past contains seers with foreknowledge of what chance will bring" so that "patches of the past are enough tainted with futurity".
- **Bearing**: this is where "conditionals on the conscious state are free" finds a home. An intention formed before the outcome is a particular fact no later than t. It is also a *cause* of the outcome, like the tosser, not a record of it, so it is not tainted with futurity the way a seer's report would be. On Lewis's criterion it is admissible.
- **Tenet alignment**: neutral. Lewis was a physicalist. The "(if such there be)" clause is a formal allowance, not an endorsement, and this note does not enlist him.

### Wallace (2010), "How to Prove the Born Rule"
- **Type**: chapter in Saunders, Barrett, Kent & Wallace (eds.), *Many Worlds?*, OUP, pp. 227–263. Read in its arXiv preliminary version (arXiv:0906.2718v1, titled "A formal proof of the Born rule from decision-theoretic assumptions").
- **Key points** (**[verified: arXiv:0906.2718]**):
  - On non-Everettian probability, "the majority just take it as a bare postulate that an agent should conform his subjective probabilities to the objective probabilities". A footnote adds: "the Principal Principle is postulated, not derived."
  - "if classical probability can give no justification of its probability rule, why ask the Everettian for such a justification?" He then claims that in Everett one can "prove and not merely postulate the link".
  - Behavioural equivalence: "An Everettian agent who adopted the Born-rule strategy would make exactly the same choices between bets as would a non-Everettian who adopted the Principal Principle" with respect to the Born weights.
  - The personal-identity premise is explicit: "There is (I assume!) no indivisible, immaterial soul which passes through my life and magically makes me a single being".
- **Bearing**: (i) Wallace concedes the shared one-world debt in exactly the form this note's verdict needs. (ii) Everettian decision theory is not neutral ground the Map could borrow, since its derivation runs on a reductionist premise about the self that the Map denies. This is a remark about Wallace's premise. It is not an argument for dualism.
- **Tenet alignment**: conflicts with No Many Worlds.

### Brown & Ben Porath (2020), "Everettian Probabilities, the Deutsch-Wallace Theorem and the Principal Principle"
- **Type**: chapter in Hemmo & Shenker (eds.), *Quantum, Probability, Logic: Itamar Pitowsky's Work and Influence*, Springer, pp. 165–198 (arXiv:2010.11591).
- **Key points**: their main argument is that "the DW theorem does not provide a justification of the Principal Principle, contrary to claims by Wallace and Simon Saunders" **[verified: arXiv abstract]**. The abstract also says the existence of objective "chances" is questioned in the paper. Body not read.
- **Bearing**: removes Everett's claimed advantage on the chance–credence link, so the debt is shared by all parties, not just one-world parties. Do not describe the authors' wider interpretive allegiances from this note.

### Sebens & Carroll (2018), "Self-Locating Uncertainty and the Origin of Probability in Everettian Quantum Mechanics"
- **Type**: *BJPS* 69(1): 25–74, DOI 10.1093/bjps/axw004.
- **Key points** (**[verified: arXiv:1405.7577]**):
  - Their principle is that "predictions made by local agents should be independent of their environment".
  - ESP-QM: the credence agent A ought to assign to the detector's having registered an outcome, given the universal wave function, "only depends on the reduced density matrix of A and D".
  - Alice "is uncertain about where she is in the quantum multiverse", and the authors credit Vaidman (1998, 2011, 2014a, 2014b) for the point and cite Lewis (1979) and Bostrom (2002) for self-locating uncertainty as a notion. The opening sentence of the abstract is "Following Vaidman, we note that observers are in a position of self-locating uncertainty" (pdftotext joins "self-locating" across a line break here).
- **Originator of the Everettian self-location idea**: Vaidman (1998), who called it an "ignorance-type" probability, using the neutron that takes a sleeping pill **[verified: arXiv:quant-ph/9609006]**. That text has zero hits for "self-locat", so on this evidence the *label* "self-locating uncertainty" is not Vaidman's 1998 wording. Lewis (1979) is the source for *de se* attitude vocabulary. This note does not claim to know who first wrote "self-locating uncertainty" in the Everett context.
- **Bearing**: ESP-QM is in effect an admissibility rule. It declares everything outside the local reduced state epistemically irrelevant. The Map's rule differs from it by exactly one item: the agent's conscious state, which appears in no reduced density matrix, is added to what credence may depend on. The Map cannot "beat" Sebens and Carroll at deriving Born credence, and it should not try. On its own reading the informed agent's credence is *not* Born.
- **Tenet alignment**: conflicts with No Many Worlds.

### Kent (2015), "Does it Make Sense to Speak of Self-Locating Uncertainty in the Universal Wave Function? Remarks on Sebens and Carroll"
- **Type**: *Foundations of Physics* 45(2): 211–217, DOI 10.1007/s10701-014-9862-5 (online December 2014).
- **Key points** (**[verified: arXiv:1408.1944v3]**): Kent asks whether there is any objective fact for a pre-observation observer to be uncertain about, given that branch decompositions are an arbitrary choice and the post-measurement state can be read as one observer as easily as two. He judges the problems "likely sufficient to doom their attempt to make sense of many-worlds probabilities via self-locating uncertainty" while adding "we do not give a logical proof that no ideas along these lines can ever work".
- **Bearing**: in a one-world reading there is a fact to be uncertain about, namely which outcome will occur. The Map's rule needs no self-location at all.

### Dawid & Thébault (2015), "Many worlds: decoherent or incoherent?"
- **Type**: *Synthese* 192(5): 1559–1580, DOI 10.1007/s11229-014-0650-8.
- **Key points**: "We claim that, as it stands, the Deutsch–Wallace–Everett approach to quantum theory is conceptually incoherent" **[verified: publisher PDF]**. The charge is that the approach's decoherence arguments rest on probabilistic reasoning its own precepts disallow, so its "robust" emergent structures lack the empirical grounding they need. Franklin (2023, *Philosophy of Science* 91(2): 288–309) replies.
- **Note**: this is the paper the brief names. It is distinct from Dawid & Friederich (2022), the ESP critique carried by the earlier notes.

### Maudlin, Albert and McQueen & Vaidman
- **Maudlin (2014)**, critical study of *The Emergent Multiverse*, *Noûs* 48(4): 794–808, DOI 10.1111/nous.12072. Metadata verified; body **not read**. Bacciagaluppi & Ismael (2015) describe Maudlin as the most vocal critic "of the ontological picture proposed by Wallace" and group the probability critics as "David Albert, Kent, and Huw Price" **[verified: B&I review]**. The SEP many-worlds entry reports Maudlin (2010) arguing that the universal wave function is the wrong type of object to be the whole ontology. **Do not attribute a probability-derivation argument to Maudlin on this note's evidence.** His single-world reply is ontological.
- **Albert (2010)**, "Probability in the Everett Picture", *Many Worlds?* pp. 355–368 (reprinted in *After Physics*, 2015). Metadata verified; body not read this run. The SEP entry lists him among critics of the decision-theoretic assumptions. For his "fatness" argument rely on the 2026-03-04 note, which read secondary summaries.
- **McQueen & Vaidman (2019)**, "In defence of the self-location uncertainty account of probability in the many-worlds interpretation", *SHPMP B* 66: 14–23. Per the SEP entry (whose author is Vaidman), Kent (2015) and McQueen & Vaidman (2019) argue that the Sebens–Carroll proof "fails because it starts with a meaningless question" **[verified: SEP HTML]**, while the 2019 paper defends self-location uncertainty as such. Body not read.

### Price (2012), "Causation, Chance, and the Rational Significance of Supernatural Evidence"
- **Type**: *Philosophical Review* 121(4): 483–538, DOI 10.1215/00318108-1630912.
- **Key points** (**[verified: Crossref abstract]**): Price frames a conflict "between decision rules based on credences guided solely by chances, and rules based on credences guided by other sorts of probabilistic evidence", and notes that "Far from excluding cases of the latter kind, Lewis's Principal Principle explicitly allows for them, in the form of the caveat that credences should follow beliefs about chances only in the absence of “inadmissible evidence.”" His remedy has causal and evidential decision theory "being objective and subjective faces of the same practical coin". Body not read.
- **Bearing**: the reviewer calls what the Map owes an "evidential-chance" rule. The Map's conditional is interventional, P(O | do(C), X), so for the agent's own intention evidential and causal decision theory agree unless C and O share a common cause outside the selection. The rule is a causal-chance rule. Price's paper is the place to look if the Map ever needs the case where they diverge.

### Fuchs & Schack (2013), "Quantum-Bayesian Coherence"
- **Type**: *Reviews of Modern Physics* 85(4): 1693–1715, DOI 10.1103/RevModPhys.85.1693. Read as arXiv:1301.3274v1, titled "Quantum-Bayesian Coherence: The No-Nonsense Version".
- **Key points** (**[verified: arXiv:1301.3274]**): in QBism "the Born Rule cannot be interpreted as a rule for setting measurement-outcome probabilities from an objective quantum state". It is "a normative rule in addition to usual Dutch-book coherence" for "how one should assign probabilities to the consequences of various intended measurements on a physical system". The authors set out the reading philosophers give, the Born rule as "a healthy serving of Principal Principle" with the quantum state in the role of chance, and reject it: "the Quantum-Bayesian view cannot sanction this".
- **Bearing**: this is the nearest rival that already has a first-person rule. QBism's rule is first-person and not chance-based. The Map's candidate is chance-based, and first-person only in what counts as admissible. The two disagree at exactly the step QBism refuses, the "quantum Principal Principle". QBism's "intended" also attaches to the choice of *measurement*. The Map's intention attaches to the *outcome*.

### Healey: the pragmatist view (SEP, rev. 2026; Healey 2012, 2017)
- **Type**: SEP entry "Quantum-Bayesian and Pragmatist Views of Quantum Theory" (Healey; substantive revision 8 Sep 2026); Healey (2012), *BJPS* 63(4): 729–771; Healey (2017), *The Quantum Revolution in Philosophy*, OUP.
- **Key points** (**[verified: SEP HTML]**): the advice is "tailored to meet the needs of physically situated, and hence informationally-deprived, agents like us". "Setting credences equal to Born probabilities derived from the correct quantum state for anyone in that physical situation is a wise epistemic policy for an agent in a world like ours." "Born probabilities are equally objective even when they differ more radically from Lewis's (1986) chances because they are based on more (physically) limited information." The entry reports Healey's newer label for the view as "desert pragmatism" (DP).
- **Bearing**: Healey already relativises the evidence base of an objective chance to the agent's *physical* situation. The Map's rule has the same form with the situation widened to the *psychophysical* situation. Healey does not make that widening, and per [pragmatist-quantum-foundations-and-the-agent](/topics/pragmatist-quantum-foundations-and-the-agent/) his agents need not be conscious.

### List & Pivato (2015), "Emergent Chance"; Ismael (2011), "A Modest Proposal about Chance"
- **List & Pivato**: *Philosophical Review* 124(1): 119–152. Their abstract argues that "objective chance at a higher level can coexist with its absence at a lower level", with "higher-level properties supervening on lower-level ones" **[verified: Crossref abstract]**. Kinney (2021, *Journal of Philosophical Logic* 50(5): 1057–1077) contests the argument (metadata only).
- **Ismael (2011)**: *Journal of Philosophy* 108(8): 416–442. Not read. Bacciagaluppi & Ismael describe chances of the Principal-Principle kind as "single-case probabilities extracted from general probabilities by conditionalizing on everything we generally think knowable about a system", pointing to Ismael (2011) for the proposal **[verified: B&I review]**.
- **Bearing**: both give formal precedent for chance relative to a level or to an information base. Neither fits the Map exactly. List & Pivato's levels supervene, whereas the Map's C does not supervene on the physical. Ismael's "generally knowable" base is the formal twin of [P-Q2](/positions/quantum-interface/#p-q2)'s "publicly conditionable" quantifier, which is itself awaiting a human decision (see Key Debates).

### Deliberation and self-prediction: Spohn, Levi, Hájek (2016)
- **Hájek (2016)**, "Deliberation Welcomes Prediction", *Episteme* 13(4): 507–528. His abstract states the target thesis: "while deliberating about what you'll do, you cannot rationally have credences for what you'll do". It names "Spohn, Levi, Gilboa, Price, Louise, and others" as its defenders, and Hájek rebuts their arguments **[verified: Crossref abstract]**. Vavova (2016, same issue, pp. 529–538) replies that the puzzle is "complicated". Spohn is among the defenders Hájek names. Spohn (1977, *Erkenntnis* 11: 113–134) is listed below as a probable locus, but its link to the thesis was not checked (metadata verified; body not read). The `voids-self-prediction-void-2026-10-14` research note covers Levi and Rabinowicz.
- **Bearing**: this fixes the rule's scope. It applies once the intention C has formed: the credence is about the outcome *given* C, which is the ordinary act-to-outcome credence any decision theory needs. If the Map identifies the selection with the choice itself, the agent's credence about her own selection *while selecting* falls into the contested credence gap, and the rule says nothing there.

### Lewis (1981), "Causal Decision Theory", and the agent-causal sources
- **Lewis (1981)**: *Australasian Journal of Philosophy* 59(1): 5–30. Not read. Per the SEP entry, "A dependency hypothesis for an agent at a time is a maximally specific proposition about how the things the agent cares about do and do not depend causally on his present acts" **[verified: SEP HTML]**. The candidate rule's mixture over selector-law hypotheses has the shape of a partition into dependency hypotheses. That is this note's construction, not Lewis's claim.
- **O'Connor (2000)**: via [agent-causation-and-acting-for-reasons](/topics/agent-causation-and-acting-for-reasons/) (L52), which quotes the chapter abstract's "a causal notion of 'structured propensities'" and paraphrases its job as explaining why some undetermined actions are likelier than others. On the Map's mapping these are the free conditionals, and the post-intention chance the rule applies to is such a propensity.
- **Pereboom (2001; 2014)** and the wild coincidences; **van Inwagen (2000)** and the rollback: via [rollback-argument-against-agent-causation](/concepts/rollback-argument-against-agent-causation/) and [the-manipulation-argument-and-hard-incompatibilism](/topics/the-manipulation-argument-and-hard-incompatibilism/). Not re-read.

## Major Positions

### Everettian decision theory and self-location (Deutsch, Wallace; Vaidman, Sebens & Carroll)
- **Core claim**: rationality constraints, or self-locating credence with ESP-QM, force Born-valued credences on every branching agent.
- **Relation to site tenets**: conflicts with Tenet 4. On the question asked here it gives the agent's intention no role: in ESP-QM credence depends on the local reduced state alone. A theory where the agent's intention shifts the chance has no counterpart in it.

### One-world objective chance with the Principal Principle (Lewis; the GRW/Copenhagen default)
- **Core claim**: credence should follow chance given admissible evidence. The link is postulated (Wallace's concession) or justified by a separate argument (the debate Brown & Ben Porath join).
- **Relation to site tenets**: the Map's natural home. It needs one thing GRW does not, namely that the history fixing the chance includes a non-physical fact.

### QBism (Fuchs, Schack)
- **Core claim**: the Born rule is a personalist coherence norm for an agent's expectations about the consequences of her intended measurements. There are no objective chances to defer to.
- **Relation to site tenets**: it has the rule the Map lacks, but buys it by denying the objective chance Tenet 4 needs. [qbism](/concepts/qbism/) treats QBism as an under-specified relative of the Map; on credence the two part ways at the quantum Principal Principle.

### Situated pragmatism (Healey)
- **Core claim**: Born probabilities are objective advice relative to the agent's physical situation.
- **Relation to site tenets**: the formal template for the Map's rule, minus the conscious state.

## Key Debates

### Is the agent's own intention admissible evidence?
- **Three readings**:
  1. **Lewisian-historical (recommended).** C is a particular fact before the outcome and a cause of it, so it is admissible. The chance at any time after C forms conditions on C. The Born weight is then the chance only *before* C forms, and only if C's formation is chancy.
  2. **Born-as-the-chance.** If the Born weight is *the* chance at the moment of selection, C is *inadmissible*: it bears on O other than through that chance. The Principal Principle then says nothing to the informed agent, and "free" means unconstrained. The agent is left without a rule. This is the literal reading of [P-Q2](/positions/quantum-interface/#p-q2)'s "only conditionals on the conscious state itself are free".
  3. **Relativised (Healey / Ismael form).** Chance is indexed to an evidence base. The public base excludes C and yields Born, while the agent's base includes C. This is a notational variant of reading 1 that avoids saying which chance is "the" chance.
- **Is the rule compatibilist-shaped?** In form, yes. It treats C as one more item of admissible history, exactly as a physicalist treats the neural correlate of an intention, so the agent's freedom does no work in the credence norm. In content, no. The rule is silent on how C came about, and the libertarian commitment sits at C's formation. There the rollback fork bites: propensities over intention-formation are what make the Born weight a chance at any time, and they grant van Inwagen's premise. The reviewer's separate inference 2 (psychophysical superselection as a population-level, compatibilist-shaped constraint) is a different claim and is not settled here.

### Does the rule cost the Map anything the other one-world views do not pay?
- **Shared**: the justification of the Principal Principle. Wallace concedes that non-Everettian views postulate it; Brown & Ben Porath deny that Everett proves it.
- **Map-specific**: (i) chance changes without physical change; (ii) the propensity-or-coincidence fork at intention-formation; (iii) a credal commitment to horn (a) for its own adherents via Tenet 3's wording. Item (iii) has a corollary: if neural outcomes were ever recorded (cf. [brain-internal-born-rule-testing](/topics/brain-internal-born-rule-testing/)), an adherent's non-Born credences would be a bettable claim. That is the conditional signature of horn (a) seen from the inside.
- **Current state**: no source in the literature addresses a dualist admissible history. Lewis's "(if such there be)" is the only explicit allowance found.

### The rule depends on the open [P-Q2](/positions/quantum-interface/#p-q2) quantifier decision
- [P-Q2](/positions/quantum-interface/#p-q2) now reads "outcome frequencies stay Born-exact in every publicly conditionable context" **[verified: `positions/quantum-interface.md` L68]**. A P1 HUMAN DECISION in `workflow/todo.md` (blocked since 2026-10-14) asks whether to own horn (b) at every public grain (option a) or to scope the quantifier to entangled-remote contexts (option b).
- **Effect on the rule**: Tenet 3's report-reliability makes intentions reportable and instructable, which makes them publicly conditionable. Under option (a), the agent's tilted credence survives only for conscious states that are never labelled, and the rule's horn-(a) credence contradicts the register at every reported grain. Under option (b), the tilted credence predicts conditional residuals that could in principle be tested publicly. The rule does not choose between the options, but it adds a consideration: option (a) makes the Map's own adherents hold credences their register says are miscalibrated whenever they report an intention. Do **not** propagate the 2026-10-14 reading in any fold. The todo task forbids it until decided.

## The Candidate Rule

Let X be the public physical context, C the agent's conscious state (an intention), O a neural outcome, q(O | X) the Born weight, and h a hypothesis about the selector law, with every admissible h satisfying the apex's averaging identity Σ_C P_h(O | C, X) · P_h(C | X) = q(O | X).

- **(R1) Time-indexed chance.** Before C forms, the chance of O is q(O | X), provided C's formation has chances P(C | X). After C forms and before O, the chance of O is P(O | do(C), X).
- **(R2) First-person credence.** An agent who knows C, with otherwise admissible evidence, sets Cr(O | C, X) = Σ_h Cr(h) · P_h(O | do(C), X). Anyone lacking C sets Cr(O | X) = q(O | X).
- **(R3) Tenet-3 direction.** Given positive credence in Tenet 3's definition, the expectation in R2 exceeds q for content-expressing O. The size of the excess is the agent's credence in the tenet times the expected tilt. Born-valued credence for the informed agent is permitted only if she is agnostic about the direction of the tilt, and it does not entail horn (b).
- **(R4) Limit case.** If selection is complete, P(O | do(C), X) = 1 for the intended O. The agent's credence is then near 1, and Born-exactness moves entirely onto the distribution of intentions, P(C | X) = q(O | X). This is the apex's "Born-random seed wearing an agency label" rider (desideratum 5) seen from the credence side: the more confident the agent rightly is in her selection, the more the Born statistics must be carried by how often she intends.

### Toy-model desideratum 7, drafted for `apex/born-preserving-causal-efficacy` (~95 words)

> 7. **A first-person chance–credence link.** The model must state the chance of each outcome once the conscious state is fixed, P(O | do(C), X), and the moment at which chance passes from the Born marginal to that conditional. Lewis's Principal Principle, with the agent's own conscious state counted as admissible history, then fixes what a selecting agent who knows C should believe. The model must also say whether the Born weight is a chance before C forms, which needs propensities over conscious states, or only a marginal over settlings, which meets the wild-coincidences objection.

The apex is over its hard ceiling with installs blocked behind a NEEDS-HUMAN length decision (per the 2026-10-28 review). Install this only once that decision is made.

## Drafted Fold Paragraph

**Target**: [quantum-probability-consciousness](/concepts/quantum-probability-consciousness/), appended to §"The Missing Piece: First-Person Probability" after L92 ("...yet it appears in none of these accounts."). Alternative placement: the end of §"The Indexical Reading", after L132. **Size**: about 230 words of prose plus three reference entries (about 75 words), about 305 words in total against 485 of headroom. Re-measure before installing, since `analyze_length` counts the reference list.

> **A candidate rule.** Filling the gap does not need a new decision theory. In a one-world chancy theory credence follows chance by Lewis's (1980) Principal Principle, and Lewis counts historical information as admissible: history that matches "atom for atom, field for field, even spirit for spirit (if such there be)". If the conscious state belongs to that history, then once an intention C has formed, the chance of a neural outcome O is the conditional P(O | do(C), X) of [the Born-preservation trilemma](/apex/born-preserving-causal-efficacy/), and a selecting agent who knows C should set her credence to her expectation of that conditional. The Born weight stays the right credence for anyone who lacks C. It is also the chance *before* C forms, but only if forming an intention has propensities of its own; otherwise the Born match is the unexplained conformity the [rollback analysis](/concepts/rollback-argument-against-agent-causation/) records. Two consequences follow. The Map's own agent should not hold Born credence about content-expressing outcomes, because [Bidirectional Interaction](/tenets/#bidirectional-interaction) has consciousness "biasing quantum indeterminacy in the brain toward patterns that express its content". And the chance–credence link is no special debt. Wallace (2010) notes that non-Everettian accounts take the Principal Principle as a bare postulate, and Brown and Ben Porath (2020) deny that the Deutsch–Wallace theorem justifies it for the Everettian either. What belongs to the Map alone is a chance that changes with no physical change.

**Quotation status in the fold**: "atom for atom, field for field, even spirit for spirit (if such there be)" is verified against the OCR scan of Lewis (1980) and is clean in OCR. "biasing quantum indeterminacy in the brain toward patterns that express its content" is verified against `tenets/tenets.md` L91 (Map-internal; re-grep before install, since Map-internal quotations go stale). Wallace is paraphrased from arXiv:0906.2718 ("take it as a bare postulate" there reads "just take it as a bare postulate"; the fold does not quote it). Brown & Ben Porath is paraphrased from the arXiv abstract.

**References to append** (numbered to follow the target's list):

- Lewis, D. (1980). "A Subjectivist's Guide to Objective Chance." In R. C. Jeffrey (Ed.), *Studies in Inductive Logic and Probability*, Vol. II (pp. 263–293). University of California Press.
- Wallace, D. (2010). "How to Prove the Born Rule." In S. Saunders, J. Barrett, A. Kent & D. Wallace (Eds.), *Many Worlds? Everett, Quantum Theory, and Reality* (pp. 227–263). Oxford University Press.
- Brown, H. R. & Ben Porath, G. (2020). "Everettian Probabilities, the Deutsch-Wallace Theorem and the Principal Principle." In M. Hemmo & O. Shenker (Eds.), *Quantum, Probability, Logic* (pp. 165–198). Springer. arXiv:2010.11591.

**Guards for the writer**: do not enlist Lewis, Wallace, Healey, List, Ismael or O'Connor for dualism. Lewis's "(if such there be)" is a formal allowance by a physicalist. Do not say the Map *derives* any credence; the rule *applies* the Principal Principle. Do not import the [P-Q2](/positions/quantum-interface/#p-q2) "publicly conditionable" quantifier. Keep "horn (a)" as the *credal* consequence of Tenet 3's wording, not a claim that conditional deviations exist.

## Where Else This Lands (no edits made)

- [born-preserving-causal-efficacy](/apex/born-preserving-causal-efficacy/): desideratum 7 above, blocked behind the open length decision.
- [rollback-argument-against-agent-causation](/concepts/rollback-argument-against-agent-causation/) §"One Debt": one sentence could add that on the propensity branch the Born weight is the pre-intention Lewisian chance and the informed agent's credence is the post-intention one. Check that article's length before minting.
- `positions/quantum-interface` [P-Q2](/positions/quantum-interface/#p-q2) human decision: the consideration under "The rule depends on the open [P-Q2](/positions/quantum-interface/#p-q2) quantifier decision" belongs in that task's notes.

## Why Not a Topics Article

Topics stands at 367 of 370 (`count_section_files`, 2026-10-30). The literature found would support a page, since the Principal Principle has no corpus treatment. But the result itself is compact: one rule, one time-index, one verdict. Most of the surrounding material is already held by [probability-problem-in-many-worlds](/topics/probability-problem-in-many-worlds/), [pragmatist-quantum-foundations-and-the-agent](/topics/pragmatist-quantum-foundations-and-the-agent/), [rollback-argument-against-agent-causation](/concepts/rollback-argument-against-agent-causation/) and [born-preserving-causal-efficacy](/apex/born-preserving-causal-efficacy/). A standalone page would mostly restate those for one paragraph of new content. If a human later wants the page, the slug `principal-principle-and-the-selecting-agent` is the obvious one (not checked with `check_slug`), with sections built from "Key Debates" above.

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1977 | Spohn, *Erkenntnis* | Spohn is a named defender of "deliberation crowds out prediction" (Hájek 2016); this paper's role unverified |
| 1979 | Lewis, "Attitudes De Dicto and De Se" | *De se* attitudes; cited by Sebens & Carroll for self-location |
| 1980 | Lewis, "A Subjectivist's Guide" | Names the Principal Principle; admissibility clause; history "spirit for spirit (if such there be)" |
| 1981 | Lewis, "Causal Decision Theory" | Dependency-hypothesis partitions |
| 1998 | Vaidman, *ISPS* 12(3) | "Ignorance-type" probability for branching observers |
| 1999 | Deutsch, *Proc. R. Soc. A* 455 | Decision-theoretic Born rule |
| 2000 | van Inwagen | Rollback argument |
| 2001 | Pereboom, *Living Without Free Will* | Wild coincidences |
| 2010 | Wallace, "How to Prove the Born Rule" | Concedes the PP is postulated in one-world views; claims Everett proves it |
| 2012 | Price, *Phil. Review* 121(4) | Inadmissible evidence and CDT/EDT as chance and credence |
| 2013 | Fuchs & Schack, *RMP* 85(4) | QBist Born rule as coherence norm; rejects the "quantum Principal Principle" |
| 2015 | Kent, *Found. Phys.* 45(2) | Self-locating uncertainty may lack an object |
| 2015 | Dawid & Thébault, *Synthese* 192(5) | DWE approach "conceptually incoherent" |
| 2015 | List & Pivato, *Phil. Review* 124(1) | Level-specific chance |
| 2016 | Hájek, *Episteme* 13(4) | Rebuts "deliberation crowds out prediction" |
| 2017 | Healey, *Quantum Revolution in Philosophy* | Born probabilities as situated objective advice |
| 2018 | Sebens & Carroll, *BJPS* 69(1) | ESP-QM self-location derivation |
| 2020 | Brown & Ben Porath | DW theorem does not justify the PP |

## Potential Article Angles

1. **The fold** (recommended): the candidate rule and the verdict in about 230 words in [quantum-probability-consciousness](/concepts/quantum-probability-consciousness/), answering that page's own "missing piece".
2. **Desideratum 7** in [born-preserving-causal-efficacy](/apex/born-preserving-causal-efficacy/), once length allows.
3. **A topics page** (not recommended now): "The Principal Principle and the Selecting Agent". Lewis's admissibility applied to a dualist history; the three readings; Sebens–Carroll's ESP as an admissibility rule; QBism and Healey as the rule's neighbours; the deliberation scope limit.

When writing, follow `obsidian/project/writing-style.md`: front-load the rule, use named anchors for forward references, and give the tenet connection explicitly.

## Gaps in Research

- **Lewis (1994) "Humean Supervenience Debugged"** (*Mind* 103(412): 473–490; Crossref's title field for that DOI reads "Symposium: Chance and Credence"), **Hall (1994)** (*Mind* 103(412): 505–518) and **Thau (1994)** (*Mind* 103(412): 491–504): metadata verified, not read. If the Map's corridor chances are Humean, the undermining problem and the "New Principle" may apply. If they are primitive propensities they may not. Unsettled here.
- **Hall (2004)** "Two Mistakes About Credence and Chance" (*AJP* 82(1): 93–111) on whether admissibility can be defined: not read.
- **Lewis (1981)** body not read; the dependency-hypothesis description comes from the SEP. Whether Lewis's own dependency hypotheses are built from chance counterfactuals was not verified, and the note does not assert it.
- **Price (2012)**, **Ismael (2011)**, **Healey (2017)**, **Maudlin (2014)**, **Albert (2010)**, **McQueen & Vaidman (2019)**, **Saunders (2010)**, **Kinney (2021)**, **Spohn (1977)**: bodies not read. Each claim above is scoped to the abstract or carrier named.
- No source was found that discusses the Principal Principle with a non-physical admissible history beyond Lewis's parenthesis. The application is the Map's own construction.
- The size of the Tenet-3 tilt is unconstrained here. [selection-only-channel](/concepts/selection-only-channel/) bounds a pure selector to log₂(N) bits per event, which may bound how far R2 can depart from Born. Not worked.
- Multi-agent case: whether two agents with private C's can each hold tilted credences consistent with joint Born statistics is the [multi-agent-born-preservation-problem](/topics/multi-agent-born-preservation-problem/). Not addressed.

## Citations

- Albert, D. Z. (2010). Probability in the Everett Picture. In S. Saunders, J. Barrett, A. Kent & D. Wallace (Eds.), *Many Worlds?* (pp. 355–368). Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199560561.003.0013
- Bacciagaluppi, G. & Ismael, J. (2015). Essay Review: *The Emergent Multiverse*. *Philosophy of Science*, 82(1), 129–148. https://doi.org/10.1086/679037
- Brown, H. R. & Ben Porath, G. (2020). Everettian Probabilities, the Deutsch-Wallace Theorem and the Principal Principle. In M. Hemmo & O. Shenker (Eds.), *Quantum, Probability, Logic: Itamar Pitowsky's Work and Influence* (pp. 165–198). Springer. https://doi.org/10.1007/978-3-030-34316-3_7 ; arXiv:2010.11591
- Dawid, R. & Thébault, K. P. Y. (2015). Many worlds: decoherent or incoherent? *Synthese*, 192(5), 1559–1580. https://doi.org/10.1007/s11229-014-0650-8
- Deutsch, D. (1999). Quantum theory of probability and decisions. *Proceedings of the Royal Society A*, 455(1988), 3129–3137. https://doi.org/10.1098/rspa.1999.0443
- Franklin, A. (2023). Incoherent? No, Just Decoherent: How Quantum Many Worlds Emerge. *Philosophy of Science*, 91(2), 288–309. https://doi.org/10.1017/psa.2023.155 (metadata only)
- Fuchs, C. A. & Schack, R. (2013). Quantum-Bayesian coherence. *Reviews of Modern Physics*, 85(4), 1693–1715. https://doi.org/10.1103/RevModPhys.85.1693 ; arXiv:1301.3274
- Hájek, A. (2016). Deliberation Welcomes Prediction. *Episteme*, 13(4), 507–528. https://doi.org/10.1017/epi.2016.27
- Hall, N. (1994). Correcting the Guide to Objective Chance. *Mind*, 103(412), 505–518. https://doi.org/10.1093/mind/103.412.505 (metadata only)
- Hall, N. (2004). Two Mistakes About Credence and Chance. *Australasian Journal of Philosophy*, 82(1), 93–111. https://doi.org/10.1080/713659806 (metadata only)
- Healey, R. (2012). Quantum Theory: A Pragmatist Approach. *BJPS*, 63(4), 729–771. https://doi.org/10.1093/bjps/axr054 (metadata only)
- Healey, R. (2017). *The Quantum Revolution in Philosophy*. Oxford University Press. https://doi.org/10.1093/oso/9780198714057.001.0001
- Healey, R. (2016; substantive revision 2026-09-08). Quantum-Bayesian and Pragmatist Views of Quantum Theory. *Stanford Encyclopedia of Philosophy*. https://plato.stanford.edu/entries/quantum-bayesian/
- Ismael, J. (2011). A Modest Proposal about Chance. *Journal of Philosophy*, 108(8), 416–442. https://doi.org/10.5840/jphil2011108822 (metadata only)
- Kent, A. (2015). Does it Make Sense to Speak of Self-Locating Uncertainty in the Universal Wave Function? Remarks on Sebens and Carroll. *Foundations of Physics*, 45(2), 211–217. https://doi.org/10.1007/s10701-014-9862-5 ; arXiv:1408.1944
- Kinney, D. (2021). Blocking an Argument for Emergent Chance. *Journal of Philosophical Logic*, 50(5), 1057–1077. https://doi.org/10.1007/s10992-020-09590-5 (metadata only)
- Lewis, D. (1979). Attitudes De Dicto and De Se. *Philosophical Review*, 88(4), 513–543 (Crossref gives the first page only; end page unverified). https://doi.org/10.2307/2184843 (metadata only)
- Lewis, D. (1980). A Subjectivist's Guide to Objective Chance. In R. C. Jeffrey (Ed.), *Studies in Inductive Logic and Probability*, Vol. II (pp. 263–293). University of California Press. https://doi.org/10.1525/9780520318328-009
- Lewis, D. (1981). Causal Decision Theory. *Australasian Journal of Philosophy*, 59(1), 5–30. https://doi.org/10.1080/00048408112340011
- Lewis, D. (1994). Humean Supervenience Debugged. *Mind*, 103(412), 473–490. https://doi.org/10.1093/mind/103.412.473 (metadata only)
- List, C. & Pivato, M. (2015). Emergent Chance. *Philosophical Review*, 124(1), 119–152. https://doi.org/10.1215/00318108-2812670
- Maudlin, T. (2014). Critical Study: David Wallace, *The Emergent Multiverse*. *Noûs*, 48(4), 794–808. https://doi.org/10.1111/nous.12072 (metadata only)
- McQueen, K. J. & Vaidman, L. (2019). In defence of the self-location uncertainty account of probability in the many-worlds interpretation. *Studies in History and Philosophy of Modern Physics*, 66, 14–23. https://doi.org/10.1016/j.shpsb.2018.10.003 (metadata only)
- Pereboom, D. (2001). *Living Without Free Will*. Cambridge University Press. https://doi.org/10.1017/CBO9780511498824
- Price, H. (2012). Causation, Chance, and the Rational Significance of Supernatural Evidence. *Philosophical Review*, 121(4), 483–538. https://doi.org/10.1215/00318108-1630912
- Saunders, S. (2010). Chance in the Everett Interpretation. In *Many Worlds?* (pp. 181–205). Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199560561.003.0008 (metadata only)
- Sebens, C. T. & Carroll, S. M. (2018). Self-locating Uncertainty and the Origin of Probability in Everettian Quantum Mechanics. *BJPS*, 69(1), 25–74. https://doi.org/10.1093/bjps/axw004 ; arXiv:1405.7577
- Spohn, W. (1977). Where Luce and Krantz do really generalize Savage's decision model. *Erkenntnis*, 11(1), 113–134. https://doi.org/10.1007/BF00169847 (metadata only)
- Thau, M. (1994). Undermining and Admissibility. *Mind*, 103(412), 491–504. https://doi.org/10.1093/mind/103.412.491 (metadata only)
- Vaidman, L. (1998). On schizophrenic experiences of the neutron or why we should believe in the many-worlds interpretation of quantum theory. *International Studies in the Philosophy of Science*, 12(3), 245–261. https://doi.org/10.1080/02698599808573600 ; arXiv:quant-ph/9609006
- Vavova, K. (2016). Deliberation and Prediction: It's Complicated. *Episteme*, 13(4), 529–538. https://doi.org/10.1017/epi.2016.28 (metadata only)
- Wallace, D. (2010). How to Prove the Born Rule. In *Many Worlds?* (pp. 227–263). Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199560561.003.0010 ; preliminary version arXiv:0906.2718
- Wallace, D. (2012). *The Emergent Multiverse*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199546961.001.0001 (metadata only)