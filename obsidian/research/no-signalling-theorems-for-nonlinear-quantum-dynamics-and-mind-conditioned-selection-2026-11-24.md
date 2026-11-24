---
title: "Research Notes - No-Signalling Theorems for Nonlinear and State-Dependent Quantum Dynamics and a Mind-Conditioned Selection Law"
created: 2026-11-24
modified: 2026-11-24
human_modified: null
ai_modified: 2026-11-24T22:55:10+00:00
draft: false
description: "What Gisin, Polchinski, Simon-Bužek-Gisin and successors prove about no-signalling and linearity, how collapse models pass, and where the Map's selection reading is not yet covered."
topics:
  - "[[born-rule-and-the-consciousness-interface]]"
  - "[[the-interface-problem]]"
concepts:
  - "[[causal-consistency-constraint]]"
  - "[[consciousness-physics-interface-formalism]]"
  - "[[selection-only-channel]]"
  - "[[post-decoherence-selection]]"
related_articles:
  - "[[born-preserving-causal-efficacy]]"
  - "[[agency-budget]]"
ai_contribution: 100
author: null
ai_system: claude-fable-5-2
ai_generated_date: 2026-11-24
last_curated: null
recommended_action: fold
target_section: concepts
target_slug: causal-consistency-constraint
---

# Research: No-Signalling Theorems for Nonlinear and State-Dependent Quantum Dynamics and a Mind-Conditioned Selection Law

**Date**: 2026-11-24
**Search queries used**: arXiv full-text fetches by identifier (listed under each source); Crossref, INSPIRE-HEP and arXiv API metadata lookups by DOI; WebSearch "consciousness-collapse model superluminal signalling Born rule violation no-signalling Stapp OR Chalmers OR psychophysical collapse mind bias outcome probabilities"; WebSearch "Gisin 1989 Stochastic quantum dynamics and relativity Helvetica Physica Acta 62 363 e-periodica".

**Verdict**: `recommended_action: fold`. Host: [[causal-consistency-constraint]] (2,528 words by `analyze_length` at 22:5xZ; concepts hard gate 3,500; headroom 971). The fold text is in [the fold plan](#fold-plan). `topics/` and `concepts/` are at cap, so no article is proposed.

## Executive Summary

The refereed theorem that does the work is Simon, Bužek and Gisin (2001): given Hilbert-space rays, the trace rule at each time, and no superluminal communication, subsystem dynamics must be linear and completely positive on density matrices. It extends an argument from Gisin (1989), which this note could not read; Bassi and Hejazi (2015) re-derive that argument. The theorems leave stochastic nonlinear pure-state dynamics alone when the average is linear, which is how GRW and CSL pass, and Bassi, Dürr and Hinrichs (2013) show that under a Markov assumption the admissible diffusions practically coincide with collapse-model equations. Published escape routes for deterministic nonlinearity (Czachor and Doebner 2002, Kent 2005, Helou and Chen 2017, Rembieliński and Caban 2020, Kaplan and Rajendran 2022) each give up one of the theorem's premises, usually the standard projection or Born prescription for separated systems.

None of these theorems is about a nonphysical variable. Applied to a mind-conditioned selection law by this note's own inference, three cases separate: Born weights whatever the mental state (safe, and the mental state is statistically idle); mind-dependent weights over pre-existing branches (the distant reduced state conditional on the mental state changes; signalling follows if the mental state can be set locally); mind-dependent local dynamics followed by Born selection (safe for distant statistics, no longer selection-only). One consciousness-collapse author, Stapp (2011), states in print that biased outcome weights let an observer send a sender-controlled signal. The Map's selection reading has been shown safe only in the first case.

## Key Sources

All quotations below are verbatim spans found by text search in the fetched file named. "Held" means full text fetched and searched.

### Simon, Bužek & Gisin (2001), "The no-signaling condition and quantum dynamics"
- **URL**: https://arxiv.org/abs/quant-ph/0102125 (v1, 23 Feb 2001; held). *Phys. Rev. Lett.* 87, 170405; DOI 10.1103/PhysRevLett.87.170405 (arXiv API metadata).
- **Type**: Paper
- **Key points**:
  - Assumptions, from the abstract: "(1) physical states are described by rays in a Hilbert space, (2) probabilities for measurement outcomes at any given time are calculated according to the usual trace rule, (3) superluminal communication is excluded."
  - Also assumed in the body: spacelike-separated operations commute ("locality is implemented in the algebra of observables"), entangled states exist, and "the identity operation on a subsystem is a permitted dynamical evolution" (used for complete positivity only).
  - The projection postulate is **not** assumed: "Note that we also do not assume the projection postulate." Remote preparation of mixtures is derived from the trace rule alone.
  - Mechanism: any mixture realising ρ_A can be prepared at a distance; no-signalling requires the later ρ′_A to "be a function of ρA only"; combining this with mixtures evolving member by member gives linearity (their Eqs. 3 to 5).
  - Stochastic exemption, their note [14]: "Nonlinear stochastic dynamics for pure states are not excluded, provided they lead to a linear CP dynamics for the averaged density matrix. The Ghirardi-RiminiWeber (GRW) model is one such example" (the missing hyphen is a PDF-extraction artefact; print "Ghirardi-Rimini-Weber").
  - What nonlinear theories must give up: "Nonlinear modifications of quantum mechanics [15,16] have to give up at least one of these assumptions." For dynamics depending nonlinearly on the reduced state: "This seems to imply that, at least for separated systems, the trace rule has to be modified in such a nonlinear theory."
  - Lineage: "This result is a significant extension of earlier work by one of the authors [7]", where [7] is Gisin, *Helv. Phys. Acta* 62, 363 (1989).
- **Tenet alignment**: Neutral. Constrains any Minimal Quantum Interaction coupling expressible as dynamics on Hilbert-space states.

### Bassi & Hejazi (2015), "No-faster-than-light-signaling implies linear evolutions. A re-derivation"
- **URL**: https://arxiv.org/abs/1411.1768 (v2, 16 Oct 2015; held). *European Journal of Physics* 36(5), 055027; DOI 10.1088/0143-0807/36/5/055027. Note the published title has plural "evolutions"; the task brief's singular is a slip.
- **Type**: Paper (pedagogical re-derivation)
- **Key points**:
  - "We review the original argument elaborated by N. Gisin [1], which shows that the non-superluminal-signaling condition implies that the dynamics of the density matrix must be linear." Their [1] is Gisin, *Helv. Phys. Acta* 62, 363 (1989).
  - Scope of the conclusion: "The evolution for the density matrix has to be linear, no matter how the state vector's evolution is, e.g. deterministic, stochastic, etc."
  - Stochastic case: "Gisin's theorem immediately generalizes also to such evolutions." (Appendix A.)
  - Grade of the "collapse models are forced" claim: it needs two further requirements, "a quantumdynamical-semigroup type of equation, and complete positivity" (hyphenation artefact), the first of which "amounts to requiring a Markovian evolution"; "given the above premises, one can conclude that the one given by collapse models is the only possible way to modify the Schrödinger equation, if one requires no superluminal communication."
  - Finite-dimensional Hilbert spaces; the derivation is described by its authors as "done in a heuristic way".
- **Tenet alignment**: Neutral.

### Bassi, Dürr & Hinrichs (2013), "On the uniqueness of the equation for state-vector collapse"
- **URL**: https://arxiv.org/abs/1303.4284 (v2, 29 Aug 2013; held). *Phys. Rev. Lett.* 111, 210401; DOI 10.1103/PhysRevLett.111.210401.
- **Key points**:
  - "In this paper we classify all Markovian wave function evolutions [23] which do not allow faster-than-light signalling."
  - "A remarkable fact is that complete positivity is not required, but comes as a byproduct."
  - "These diffusions practically coincide with those of collapse models."
  - Theorem 1 assumes a Markovian random wave function in finite dimension whose statistical operator evolves in a closed and linear way; the conclusion is a Lindblad equation. This is the rigorous form of the "forced" claim, limited to continuous (diffusive) Markovian evolutions.
- **Tenet alignment**: Neutral.

### Polchinski (1991), "Weinberg's nonlinear quantum mechanics and the Einstein-Podolsky-Rosen paradox"
- **URL**: https://doi.org/10.1103/PhysRevLett.66.397. *Phys. Rev. Lett.* 66(4), 397–400 (Crossref). **Abstract only**, via the INSPIRE-HEP API record for the DOI; full text not obtained.
- **Abstract (INSPIRE; not in a fetched full text, so one database stands behind it)**: "I show that Weinberg's nonlinear quantum mechanics leads either to communication via Einstein-Podolsky-Rosen correlations, or to communications between branches of the wave function."
- The formalism page's sentence matches this. The label "Everett phone" does not occur in the abstract or in any text this note holds; treat it as an unverified lead for the name, and do not attribute the phrase to the abstract.
- Czachor and Doebner (2002, held) mark the Everettian character of his construction: "As opposed to the original Polchinski formulation [3] we do not resort to the Many Worlds Interpretation."
- **Tenet alignment**: The branch-communication horn presupposes real branches, so it conflicts with No Many Worlds as an escape route; the Map cannot use it.

### Gisin (1990), "Weinberg's non-linear quantum mechanics and supraluminal communications"
- *Physics Letters A* 143(1–2), 1–2; DOI 10.1016/0375-9601(90)90786-N (Crossref). **Not read.** Crossref carries no abstract. The INSPIRE-HEP record for this DOI returns an abstract that plainly belongs to a different work (a long review of dynamical reduction models), so it is a database error and must not be used.
- What held secondary descriptions say: Diósi (2016, held) writes "N. Gisin proved in 1990 that any (deterministic) nonlinear Schrödinger equation would allow for superluminal communication"; Rembieliński and Caban (2019 preprint, held) write that arguments "(in the context of the Weinberg model [3]) were clearly given by Gisin in Ref. [7]", their [7] being this paper, and that the arguments "are based on the observation that deterministic nonlinear time evolution destroys equivalence of quantum ensembles deﬁning the same mixed state".
- Consequence for the formalism page: its sentence "Gisin (1990) showed that Weinberg's nonlinear modification of quantum mechanics allows superluminal communication" agrees with the title and with two held secondary descriptions. No correction is indicated. The one refinement available is that the *general* density-matrix argument is credited by both Simon et al. and Bassi–Hejazi to Gisin (1989), not to the 1990 letter.

### Gisin (1989), "Stochastic quantum dynamics and relativity"
- *Helvetica Physica Acta* 62(4), 363–371; DOI 10.5169/seals-116034 (metadata read from the e-periodica record page, https://www.e-periodica.ch/view/hpa-001/1989/62/1121). **Not read**: the PDF download is behind an automated-client verification challenge, which this note did not attempt to pass. Everything said about its content here comes from Simon et al. (2001) and Bassi and Hejazi (2015).

### Czachor (1991) and Czachor & Doebner (2002)
- Czachor (1991), "Mobility and non-separability", *Foundations of Physics Letters* 4(4), 351–361; DOI 10.1007/BF00665894 (Crossref). **Metadata only**; no abstract obtained. Cited by Simon et al. and Kent alongside Gisin and Polchinski as showing nonlinear modifications permit signalling.
- Czachor & Doebner (2002), "Correlation experiments in nonlinear quantum mechanics", https://arxiv.org/abs/quant-ph/0110008 (v2; held). *Phys. Lett. A* 301, 139–152; DOI 10.1016/S0375-9601(02)00959-3. Abstract: "We show how one can compute multiple-time multi-particle correlation functions in nonlinear quantum mechanics in a way which guarantees locality of the formalism." Rembieliński and Caban's gloss on the cost: the "approach implies the modiﬁcation of the state reduction postulate".

### Kent (2005), "Nonlinearity without Superluminality"
- **URL**: https://arxiv.org/abs/quant-ph/0204106 (v4, 11 May 2005; held). *Phys. Rev. A* 72, 012108; DOI 10.1103/PhysRevA.72.012108.
- **Key points**:
  - The earlier results "apply to theories satisfying the rule that their predictions for widely separated and slowly moving entangled systems can be approximated by non-relativistic equations of motion with respect to a preferred time coordinate. This paper describes a natural way in which this rule might fail to hold."
  - The escape: let nonlinear evolution depend on a **local state**, "given by taking the joint wave function of the complete system, defined by allowing for only those projective measurements in the past light cone of the particle, and then tracing out the rest of the system."
  - Result claimed: "It follows that any locally defined nonlinear evolution of pure states can be made consistent with Minkowski causality."
  - Kent assumes objective collapse for the construction: "It will be assumed that measurement is an objectively definable process, and that a genuine state vector reduction takes place during measurement."
  - A direct link to consciousness, offered as speculation: "One might also wonder whether a theory of consciousness, which (according to one line of thought) has to attach consciousness to some definite physical quantity, might possibly use local quantum states."
- **Tenet alignment**: Compatible with collapse realism (No Many Worlds). The consciousness remark is a one-sentence aside labelled by Kent as beyond "coffee table speculation" only if made specific; do not present it as a proposal he develops there.

### Helou & Chen (2017)
- **URL**: https://arxiv.org/abs/1709.06639 (v2, 22 Sep 2017; held), titled "Different interpretations of quantum mechanics make different predictions in non-linear quantum mechanics, and some do not violate the no-signaling condition". Crossref lists a paper by the same authors, "Extensions of Born's rule to non-linear quantum mechanics, some of which do not imply superluminal communication", *J. Phys.: Conf. Ser.* 880, 012021 (2017), DOI 10.1088/1742-6596/880/1/012021. The arXiv record carries no journal reference, so whether these are the same text is **unconfirmed**; cite the arXiv version for the quotations.
- **Key points**: the superluminality results "overlook the fact that the distribution of measurement results predicted by non-linear quantum mechanics depends on the interpretation of quantum mechanics that one uses." Many prescriptions avoid signalling "but only two seem to have a reasonable justification. The first is the Everett interpretation, and the second, which we name causal-conditional, states that a measurement broadcasts its outcome to degrees of freedom in its future light-cone".
- **Tenet alignment**: The Everett route conflicts with No Many Worlds. The causal-conditional route is collapse-compatible and close in spirit to Kent's local state.

### Later generalisations and surveys (all held)
- Rembieliński & Caban, "Nonlinear evolution and signaling", https://arxiv.org/abs/1906.03869 (v1); *Phys. Rev. Research* 2, 012027 (2020). "We propose a condition, called convex quasi-linearity, for deterministic nonlinear quantum evolutions. Evolutions satisfying this condition do not allow for arbitrary fast signaling". The size of the class is left open by the authors.
- Kaplan & Rajendran, "A Causal Framework for Non-Linear Quantum Mechanics", https://arxiv.org/abs/2106.10576 (v2); *Phys. Rev. D* 105, 055002 (2022). A state-dependent nonlinear QFT claimed causal; it treats measurement as ordinary interaction with no collapse, so its relevance to a collapse-realist Map is limited.
- Diósi, "Nonlinear Schrödinger equation in foundations: summary of 4 catches", https://arxiv.org/abs/1602.03772 (v2); *J. Phys. Conf. Ser.* 701, 012019 (2016). Superluminal communication is the first of four anomalies it lists.

### Stapp (2011), "Retrocausal Effects as a Consequence of Orthodox Quantum Mechanics Refined to Accommodate the Principle of Sufficient Reason"
- **URL**: https://arxiv.org/abs/1105.2053 (v3; held). *AIP Conference Proceedings*, pp. 31–44, DOI 10.1063/1.3663716 (Crossref; volume not returned, and Crossref lists the proceedings editor Sheehan as a co-author, which is a record artefact: arXiv gives Stapp alone).
- **Key points**:
  - "It is well known---as will be reviewed presently---that biasing the weights of the random quantum choices, relative to the weights prescribed by orthodox quantum theory, leads to an apparent breakdown of the normal causal structure of phenomena."
  - The bias he considers is experiential: choices "can be biased away from the orthodox rules in ways that depend upon the character of the knowledge/experiences that these choices are creating."
  - The mechanism: "the biasing of the outcome of the observation here and now will shift the result of the observation of the faraway record from 50% “Yes” and 50% “No” to 100% “Yes”."
  - The signalling statement: "the observer here, by his or her choice of what to measure now, at process time n can send a signal (a sender-controlled message) to the faraway region".
- **Tenet alignment**: Aligns with Dualism and Bidirectional Interaction in ambition; shows the cost of leaving the Born corridor.
- **Guard for any writer**: Stapp presents this as an *acceptable consequence* that would explain Bem's reported retrocausal results ("The concepts of classical relativity theory break down"). He is not offering a reductio of biased weights, and he does not say his standard (unbiased) model signals. The sender-controlled variable in his example is the **choice of what to measure**, operating together with nature's biased response; do not paraphrase it as "setting the mental state".

### de Barros & Oas (2017), "Can we Falsify the Consciousness-Causes-Collapse Hypothesis in Quantum Mechanics?"
- **URL**: https://arxiv.org/abs/1609.00614 (v2; held). *Foundations of Physics* 47(10), 1294–1308; DOI 10.1007/s10701-017-0110-7 (Crossref).
- **Key point**: applies no-signalling to a proposed test of consciousness-causes-collapse (Yu and Nikolić's delayed-choice design with a human eye as detector). The interference pattern exists only in conditional statistics: "If this were not the case, we would violate the no-signaling condition in quantum mechanics, as we could use a choice of detection apparatus in Di to communicate instantaneously (or to the past)". The paper constrains what a *test* of consciousness-collapse can show; it does not analyse a mind-biased outcome law.

### Chalmers & McQueen (2021 preprint), "Consciousness and the Collapse of the Wave Function"
- **URL**: https://arxiv.org/abs/2105.02314 (v1; held).
- **Key point**: one sentence acknowledges the constraint and adopts the standard form: "To be consistent and compatible with constraints such as no superluminal signalling, nonlinear modifications to the Schrodinger equation must take a highly constrained stochastic form." (In the PDF this sentence runs across a page break and footnote 14; the span is continuous in the authors' text.) Their Eq. (3) is the CSL-type equation with a collapse operator Â. Outcomes follow "the Born rule" throughout the passages searched. Reading their default as theorem-safe *because* it has the CSL form with a fixed operator is this note's reading of Eq. (3), not a claim they argue.

### Unverified leads (do not quote)
- The phrase "Everett phone" for Polchinski's branch-communication horn (familiar in secondary literature; not in any held text).
- The WebSearch summary's statements about Okon and Sebastián's integrated-information collapse model and about a de Broglie–programme appendix on Born violation and signalling (arXiv:1703.06158); neither was fetched.
- Kent, "Quanta and Qualia" (arXiv:1608.04804, held; *Found. Phys.* 48(9), 1021–1037) mentions that block-universe qualia theories "can have unusual and counter-intuitive implications, including effects that appear to agents within the theory to be reverse causation and spacelike signalling." This is held and quotable, but it concerns a different model class (final-condition block-universe laws) and is listed here so it is not mistaken for an analysis of selection laws.
- Gisin & Rigo (1995), *J. Phys. A* 28, 7375, and Diósi (1988), *Phys. Lett. A* 129, 419, cited in Simon et al. note [14]; not fetched.
- Valentini's signal-locality theorem for deterministic hidden-variables theories is already cited on [[selection-only-channel]] and [[agency-budget]]; not re-fetched here.

## Key Debates

### Does a mind-conditioned selection law signal?

Everything in this subsection is **the note's inference** unless marked "theorem". It is laid out so each step can be checked.

**Setup.** A local system A (in or coupled to a brain) is entangled with a distant system B: |ψ⟩ = Σ_i c_i |a_i⟩|b_i⟩ with the |a_i⟩ orthonormal, p_i = |c_i|². A selection event at A picks branch i with probability q_i(m), where m is the mental state. Write ρ_i for B's state in branch i (here |b_i⟩⟨b_i|). "Selecting a branch" means the post-event global state is the i-th term of the decomposition, so B is left in ρ_i. Then B's state, averaged over outcomes at fixed m, is

ρ_B(m) = Σ_i q_i(m) ρ_i, against the standard ρ_B = Σ_i p_i ρ_i.

If the |b_i⟩ are orthonormal, ρ_B(m) = ρ_B exactly when q_i(m) = p_i for every i. So **branch selection preserves the distant reduced state for all entangled states only with Born weights**. This is two lines of algebra from the trace rule; it is the same step Simon et al. call preparation at a distance ("by performing a measurement of his system the observer B also prepares a certain state in A"), and it matches Stapp's faraway-record example.

**Case 1: Born weights whatever the mental state** (q_i(m) = p_i for all m). The averaged map is the ordinary non-selective measurement, linear and completely positive. *Theorem-grade*: standard no-signalling applies. Cost: outcome statistics are independent of m, so m transmits nothing to the outcome record in the Shannon sense. What remains for consciousness is the actualising of a Born sample, a token-level role with no statistical footprint.

**Case 2: mind-dependent weights over the pre-existing branches**, with the average over mental states restoring Born: Σ_m μ(m) q_i(m) = p_i. Conditional on m, the distant state is ρ_B(m) ≠ ρ_B. Whether that is *signalling* turns on who can fix m, and three sub-cases follow.
- *2a, m (or a correlate) settable locally at A*, by the agent or by an experimenter's instruction. Then a block of trials run at m gives B statistics ρ_B(m), distinguishable from ρ_B(m′) with enough pairs. That is signalling at spacelike separation. The averaging over μ does not rescue it, because the sender controls μ. No public announcement of m is needed; the signal is carried by the choice of m.
- *2b, m fixed only by events in the common causal past of A and B.* No superluminal signal, but sub-ensembles labelled by m depart from Born at both wings: an ordinary, in-principle-detectable Born deviation conditioned on mental state.
- *2c, m inaccessible in principle to everyone, including the subject, with μ fixed by law.* Operationally nothing signals. Structurally this is a hidden-variables theory with m in an equilibrium distribution, and the Valentini-type price already recorded on [[agency-budget]] applies: safety holds only while the distribution is exactly μ and m cannot be read or steered. An m that is reportable, trainable or instructable is not of this kind.

**Case 3: mind-dependent local dynamics, then Born selection.** If m acts as a control parameter on a completely positive trace-preserving map on A (in effect choosing which question is put, or perturbing the local Hamiltonian) and the outcome then carries Born weights for the evolved state, B's reduced state is untouched. *Theorem-grade* for each fixed m: local operations do not signal. But the local outcome statistics now depend on m, so the coupling is locally detectable and is not selection-only. A further trap sits here: if m is itself a function of the quantum state (a psychophysical law m = f(ψ)), an m-dependent map is a state-dependent map, the averaged dynamics need not be a function of the density matrix alone, and the Simon–Bužek–Gisin argument applies in full. The stochastic exemption covers only the specific forms whose average is linear.

**What the decohered setting adds.** In post-decoherence selection the branch index is recorded redundantly in the environment, including radiation that has left the laboratory. Those records play the role of B. A selection event later than the decoherence event is spacelike to some of them, which is Stapp's "faraway record" geometry. So restricting selection to decohered alternatives does not by itself remove the entangled-partner problem; it multiplies the partners.

**Scope of the theorems.** Gisin, Simon–Bužek–Gisin and Bassi–Hejazi assume the physical state is a Hilbert-space ray and that the trace rule gives all probabilities. A nonphysical m is outside that description. Applying the theorems to it requires either treating m as an external control (Cases 2a, 3) or as an extra variable (Case 2c, where the relevant results are of the hidden-variables kind). Either way, the application is the Map's extension, of the same kind as the extension of Torres Alegre's theorem corrected today.

- **Current state**: unresolved for the Map. The selection reading is shown no-signalling only in Case 1.

### How each reading of the P-Q2 quantifier fares

This describes; it does not recommend. (The wording in [[born-preserving-causal-efficacy]] is an open operator decision.)
- **Born per mental state, or per every publicly conditionable context where mental state is such a context**: Case 1. Passes on the standard theorem. The apex's talk of biasing which outcome becomes actual must then be read non-statistically.
- **Born in the pooled aggregate only**: Case 2. The distant reduced state conditional on m changes. Safe from signalling only under 2b or 2c; under 2a it signals. Not shown safe by anything the Map cites.
- **Born per every third-person-accessible context, with the selection-relevant variable inaccessible**: Case 2c. Passes operationally at the hidden-variables price, and requires that the variable doing the selecting not be the reportable intention.

## Historical Timeline

Weinberg's nonlinear proposal (1989); Gisin (1989, 1990), Polchinski (1991) and Czachor (1991) on signalling; Simon, Bužek & Gisin (2001) general theorem; escapes by Czachor & Doebner (2002), Kent (2005), Helou & Chen (2017), Rembieliński & Caban (2020), Kaplan & Rajendran (2022); Stapp (2011) on biased weights; Bassi, Dürr & Hinrichs (2013) and Bassi & Hejazi (2015) on the uniqueness of collapse equations.

## Potential Article Angles

No article is proposed (sections at cap). If capacity opens, a concepts page "no-signalling and nonlinear quantum dynamics" (slug `no-signalling-and-nonlinear-quantum-dynamics`, free in concepts at 22:5xZ) could carry the three-case analysis in full. Follow `obsidian/project/writing-style.md`.

## Fold plan

**Host**: `obsidian/concepts/causal-consistency-constraint.md`. Re-measure before editing; 2,528 words at the time of writing.

**Placement**: a new H2 immediately after "## Implications for the Interactionist Taxonomy" and before "## Two Qualifications That Limit the Constraint's Reach".

**Proposed text** (about 290 body words):

> ## What the Linearity Theorems Add
>
> Torres Alegre's preprint has refereed predecessors that constrain dynamics where his result constrains the probability rule. Simon, Bužek and Gisin (2001) assume Hilbert-space rays, the trace rule and no superluminal communication, and derive that subsystem dynamics must be linear and completely positive on density matrices; Bassi and Hejazi (2015) re-derive the argument, which both papers credit to Gisin (1989). The theorems leave pure-state nonlinearity alone when it is stochastic and averages to a linear map, which is how GRW and CSL pass (Simon et al. 2001, note 14). Adding a Markov assumption, Bassi, Dürr and Hinrichs (2013) show the admissible diffusions practically coincide with collapse-model equations.
>
> Applied to a mind-conditioned selection law, by the Map's inference and not by any cited theorem, three cases separate. If outcomes carry Born weights whatever the mental state, the averaged map is the ordinary non-selective measurement and nothing distant changes; the mental state is then statistically idle. If the weights q_i depend on the mental state while selection still lands on pre-existing branches, a distant partner's reduced state conditional on that mental state becomes Σ q_i ρ_i where the Born value is Σ p_i ρ_i, and anyone able to set the mental state locally can signal. Stapp (2011) reaches the parallel result for biased weights: the observer, by choosing what to measure, "can send a signal (a sender-controlled message) to the faraway region". If the mental state alters local dynamics before a Born-weighted selection, distant statistics are protected, but the coupling is no longer selection-only. The corridor reading is shown safe only in the first case, and the Map has not shown that a first-case law leaves consciousness more to do than actualise a Born sample. A nonphysical variable also sits outside the theorems' Hilbert-space premises, so applying them here is itself an extension.

**Reference entries to add** (renumber to the host's scheme):
- Bassi, A., Dürr, D. & Hinrichs, G. (2013). On the uniqueness of the equation for state-vector collapse. *Physical Review Letters*, 111, 210401. https://doi.org/10.1103/PhysRevLett.111.210401
- Bassi, A. & Hejazi, K. (2015). No-faster-than-light-signaling implies linear evolutions. A re-derivation. *European Journal of Physics*, 36(5), 055027. https://doi.org/10.1088/0143-0807/36/5/055027
- Gisin, N. (1989). Stochastic quantum dynamics and relativity. *Helvetica Physica Acta*, 62(4), 363–371. https://doi.org/10.5169/seals-116034 (cited via Simon et al. 2001 and Bassi & Hejazi 2015; not consulted directly).
- Simon, C., Bužek, V. & Gisin, N. (2001). No-Signaling Condition and Quantum Dynamics. *Physical Review Letters*, 87(17), 170405. https://doi.org/10.1103/PhysRevLett.87.170405
- Stapp, H. P. (2011). Retrocausal Effects as a Consequence of Orthodox Quantum Mechanics Refined to Accommodate the Principle of Sufficient Reason. *AIP Conference Proceedings*, 31–44. https://doi.org/10.1063/1.3663716 (quotation from arXiv:1105.2053v3).

**One-clause correction on the host, needed for consistency.** The corridor paragraph currently says the reading "inherits the constraint *natively* — there is no extra work to show that selection-only coupling respects no-signalling, because the channel is defined so that ensemble statistics are unperturbed." That contradicts the formalism page ("the selection reading has not yet been shown to meet it") and [[selection-only-channel]] ("narrower than automatic"). Suggested replacement for the clause after the dash: "on the strong reading, where the Born weights hold for every mental state and every publicly conditionable context, no extra work is needed; on the pooled-aggregate reading the work is not done (see the linearity theorems below)". The same qualifier is owed where the host's Relation to Site Perspective says "The corridor and trumping readings both satisfy the condition".

**Corrections on `consciousness-physics-interface-formalism`**: none required. The Gisin (1990) sentence agrees with the title and with held secondary descriptions (Diósi 2016; Rembieliński and Caban 2019). Optional, length-neutral precision if that page is next edited: the paragraph's general claim rests on Simon et al., whose note [14] exempts stochastic pure-state nonlinearity that averages to a linear map; the paragraph's phrase "whose action depended on the pure state beyond the density matrix it contributes to" is correct for the *averaged* action only.

**Do not** touch the P-Q2 paragraph of the apex.

## Gaps in Research

- Gisin (1989) and Gisin (1990) were not read; Polchinski (1991) at abstract level only; Czachor (1991) metadata only. All four are paywalled or challenge-gated to this session.
- No full-text check of the Helou–Chen journal version against the arXiv text.
- **No absence claim is made** about published applications of these theorems to mind-matter models. The one WebSearch run reported finding no paper arguing that mind-biased probabilities enable signalling, while Stapp (2011), held here, argues exactly that. The search therefore failed a known-positive control and licenses nothing. Found by direct fetch: Stapp (2011), de Barros and Oas (2017), Kent's aside (2005), and the Chalmers–McQueen sentence. Not searched: PhilPapers, the Georgiev and Donald critiques of Stapp for signalling arguments, Okon and Sebastián.
- The three-case analysis is elementary but unrefereed; in particular the claim that decohered environmental records serve as distant partners deserves a check against a concrete decoherence model.
- Whether a Kent-style local-state or Helou–Chen causal-conditional dependence could make Case 2 safe was not analysed. Those constructions address state-dependent *evolution*; Case 2's difficulty is non-Born *weights* on correlated branches, and this note sees no reason the constructions transfer.

## Citations

Full references, with arXiv versions and DOIs as verified, are given under each entry in Key Sources and in the fold plan's reference list. One further item is cited for context only: Weinberg, S. (1989). Testing quantum mechanics. *Annals of Physics*, 194(2), 336–386. https://doi.org/10.1016/0003-4916(89)90276-5 (Crossref metadata; not read).
