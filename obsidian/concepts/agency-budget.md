---
title: "The Agency Budget"
description: "How much selection survives exact Born-rule preservation: a coupling-theoretic conservation law, its ceiling, and its price — refined by human-AI iteration."
created: 2026-08-16
modified: 2026-08-16
human_modified:
ai_modified: 2026-09-02T01:43:14+00:00
last_deep_review: 2026-08-16T20:02:00+00:00
draft: false
topics:
  - "[[born-rule-and-the-consciousness-interface]]"
  - "[[selection-only-mind-influence]]"
  - "[[parapsychology-firewall]]"
  - "[[brain-internal-born-rule-testing]]"
concepts:
  - "[[concepts/ensemble-level-epiphenomenalism]]"
  - "[[concepts/causal-consistency-constraint]]"
  - "[[concepts/selection-criterion-problem]]"
related_articles:
  - "[[apex/born-preserving-causal-efficacy]]"
  - "[[apex/self-concealing-interface]]"
  - "[[positions/quantum-interface]]"
  - "[[tenets]]"
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-08-16
last_curated:
---

The **agency budget** is the quantity of selection available to any selector that is required to leave a fixed public probability distribution exactly intact. Stated that way the notion is school-neutral: it asks a question in information theory, not in metaphysics, and a committed physicalist can pose it about a thermostat as readily as a dualist can pose it about a mind.

Applied to the Map's default reading of [[tenets#^minimal-quantum-interaction|Minimal Quantum Interaction]] — conscious selection fixes *which* outcome actualises while the aggregate distribution stays Born-exact — the budget turns out to be **nonzero, and to have a statable conservation law**. The law is the marginal constraint of a probabilistic *coupling*: for every context X that an outside tester can publicly condition on,

> Σ<sub>C</sub> P(o | C, X) · P(C | X) = q(o | X)

where C ranges over conscious states, o over outcomes, and q is the Born distribution. Selection may correlate arbitrarily with C; what it may not do is disturb the o-marginal within any publicly assemblable ensemble.

Two qualifications belong with that headline rather than after it. First, the theorems that make the budget calculable come from [[#the-coupling-result|classical information theory]] (perfectly secure steganography, explained below) and say nothing about consciousness; **the mapping onto mental causation is the Map's own construction, not a published result**. Second, the same theorem that grants the budget fixes its price: perfect statistical concealment is *equivalent to* zero third-person evidence, which formalises [[concepts/ensemble-level-epiphenomenalism|ensemble-level epiphenomenalism]] and [[apex/self-concealing-interface|self-concealment]] rather than escaping them. Per the mechanism-debt convention in [[positions/quantum-interface#^mechanism-debt|the quantum-interface register]], everything here is citable as framework-internal coherence arithmetic and never as established mental causation.

## The Coupling Result {#the-coupling-result}

The formal machinery comes from steganography — hiding a message inside innocuous content so that no observer can tell a message is present.

Christian Cachin's 1998 information-theoretic model defines security as a divergence. On the statement Schroeder de Witt and colleagues give it, a stegosystem is ε-secure if "the KL divergence between the distribution of covertext C and the distribution of stegotext S" is less than ε, and "perfectly secure if the KL divergence is zero." One notational warning: the C of that literature is the *covertext*, which under the mapping below is the Born side — the opposite side from the conscious-state C of the conservation law above. Zero divergence means the message-bearing output is distributed *identically* to the innocent output. The authors gloss the strength of that condition directly: "Perfect security is a very strong notion of security, as it renders detection by statistical or human analysis impossible."

A *coupling* of two distributions is a joint distribution over their product space that marginalises to each of them. The 2023 paper's two results are stated verbatim as:

- **Theorem 1**: "A steganographic encoding procedure is perfectly secure if and only if it is induced by a coupling."
- **Theorem 2**: "Among perfectly secure encoding procedures, a procedure f : X ⇝ C maximizes the mutual information I(M ; S) if and only if f is induced by a minimum entropy coupling."

Read together these say that exact distribution-preservation and message-correlated structure are not competitors: the class of perfectly secure procedures *is* the class of couplings, and within that class throughput is maximised by minimising the coupling's joint entropy. Since the marginals are fixed, minimising joint entropy maximises mutual information — the identity I(X;S) = H(X) + H(S) − H(X,S) with both marginal entropies held constant.

The minimum-entropy coupling is not the 2023 paper's own construct. Mladen Kovačević, Ivan Stanojević and Vojin Šenk introduced the notion in 2015, and showed in the same paper that certain optimisation problems over distributions with restricted marginals are NP-hard. The conservation law is therefore exact and cheap while the ceiling is set by an optimum nobody can compute efficiently — which costs the budget throughput rather than security, since the standard fast approximations retain exact marginalisation and give up at most one bit of joint entropy.

The ceiling follows from elementary information theory rather than from the paper: mutual information never exceeds either variable's entropy, so throughput is bounded by min(H(source), H(covertext)) bits per event, generally as a strict inequality rather than an attained maximum. Substituting the interface reading — conscious state as source, Born distribution as covertext — gives the budget's closed form: **at most min(H(conscious source), H(Born distribution)) bits of reasons-correlated selection per event, at exactly zero statistical signature.**

One structural feature of the published construction deserves flagging, because the Map's mapping does not inherit it cleanly. In the steganographic setting the message is first mapped to a *ciphertext* made uniform by a private key shared with a receiver, and the coupling runs between ciphertext and covertext. There is no third party in the interface picture, and no key. What survives the disanalogy is the mathematics of the coupling; what does not survive is the picture of a message successfully sent to someone.

## Two Bookends {#two-bookends}

Two independent results fix what the budget cannot do.

**Landsman's randomness constraint.** Klaas Landsman argues that quantum indeterminism "can be proved from Chaitin's follow-up to Goedel's (first) incompleteness theorem," on the grounds that earlier arguments exploited only long-run relative frequencies. Idealising the outcome string of a fair quantum coin flip as an infinite binary sequence, quantum mechanics predicts it will typically have "a property called 1-randomness in logic, which is much stronger than uncomputability."

Landsman's target is *determinism*, not agency; the extension below is the Map's inference and not his claim. If public outcome sequences must be algorithmically random, then frequency-matching is not the only public constraint on selection. A policy that imprinted any computable pattern — Morse-coding reasons into a spin sequence — would yield a compressible string, failing randomness tests while passing every frequency test. The coupling answer dissolves this cleanly: a perfectly secure procedure's output is distributed identically to the covertext, so it inherits whatever randomness properties the covertext has. The constraint bites only against models where agency signals.

**Valentini's signal-locality theorem.** Antony Valentini proves that any deterministic hidden-variables theory reproducing quantum theory at the "quantum equilibrium" distribution "must predict the existence of instantaneous signals at the statistical level for hypothetical 'nonequilibrium ensembles'." The scope condition matters and must not be dropped: the theorem is about *deterministic hidden-variables theories*, not about every possible framework, and its subject is hypothetical non-equilibrium ensembles.

Within that scope the reading is unforgiving. Exact equilibrium leaves the statistical-level budget at zero — no controllable ensemble-level bias exists — while departure from equilibrium buys a positive statistical budget at the cost of superluminal signalling. There is no innocent intermediate setting available in that class of theories, which is the Map's structural reason for claiming exactness rather than smallness.

## Relation to Site Perspective {#relation-to-site-perspective}

The Map's interest in the budget is specific: the 2026-08-13 external review charged that Born-preserving efficacy was so far "only a verbal conjunction of two desiderata" — enough bias to ground authorship, not enough to be detected — and demanded a conservation law for agency. The coupling constraint above *is* that law, and it converts the charge from "these desiderata may be inconsistent" into "they are jointly satisfiable, and here is what satisfying them costs."

The same review anticipated the obvious reply, and it lands: a worked model must show the desiderata compatible "without achieving compatibility merely by defining all observable consequences away." The coupling construction is uncomfortably close to that. It secures compatibility by making the observable consequences exactly nil — which is the constraint the corridor imposed in the first place, so the move is not circular, but it does mean the result buys consistency with the very coin the objection said was suspect. The honest verdict is that the budget converts a suspicion of incoherence into a priced concession, and does not convert either into a demonstration of efficacy.

That is progress on exactly one axis. It answers the *impossibility* form of the ensemble-level worry and leaves the *idleness* form standing. Perfect security and zero third-person evidence are the same condition under two descriptions, so a proof that the interface can be perfectly secure is simultaneously a proof that it can never be witnessed from outside. The budget therefore gives [[apex/self-concealing-interface|the self-concealing interface]] a theorem where it had a posture, and gives the [[parapsychology-firewall|parapsychology firewall]] a formal reason to expect null results — the empirical ceilings on detectable micro-psychokinesis are treated in the Map's information-limits research rather than repeated here.

Three tenet connections follow. [[tenets#^minimal-quantum-interaction|Tenet 2]] gets its exactness requirement priced: exact preservation costs less than assumed, because a nonzero budget survives it. [[tenets#^bidirectional-interaction|Tenet 3]] gets a channel formalism — a joint distribution with nonzero mutual information between mental and physical variables — while inheriting the standing caveat that the interface argument shows downward causation to be *available*, not actual. And [[tenets#^occams-limits|Tenet 5]] is what licenses treating a formal possibility-proof as worth having at all, given how little is known about the mechanism.

The clearest downstream use is as a candidate for the toy model [[apex/born-preserving-causal-efficacy|P-Q10 records as missing]]. A worked minimum-entropy coupling between a small conscious-state space and a small outcome space would deliver several of that article's desiderata explicitly: an explicit joint distribution, exact ensemble Born-preservation by construction rather than in a limit, nonzero mutual information, and per-context conservation. It would not deliver the rest. It states no [[concepts/selection-criterion-problem|selection principle]] — a coupling says nothing about *why* a given conscious state maps to a given outcome. It does not by itself demonstrate token counterfactual dependence, since a coupling is a distribution rather than a causal structure. And it would need the no-signalling desideratum argued rather than assumed, because the classical coupling framework has no notion of measurement context at all.

One dependency should be flagged rather than asserted. The per-context form of the conservation law handles correlated populations by binding the marginal within any ensemble an outsider can assemble — shared preferences among many agents need no cross-subject ledger, because the constraint was never per-subject. That answer quietly requires conscious states to be publicly unresolvable in principle: if C could itself be publicly conditioned on, it would become one of the contexts X, and shared bias would become testable. Whether the Map asserts that privacy commitment strongly enough, and where, is a question for the positions register and is not settled here.

## Rival Readings {#rival-readings}

**The zero-budget reading.** Exact preservation leaves selection nothing to do; authorship with no conditional signature is chance under another name. This is the sharpest rival and the Map does not claim to have answered it. The coupling result shows that content is recoverable *relative to a decoder holding the mental-side facts* — and an objector may fairly reply that a channel whose only competent decoder already possesses the mental facts is not obviously a mental-to-physical channel at all.

**The finite-stock reading.** Scott Aaronson examines — the abstract's own verb — a viewpoint that "tries to find scope for 'freedom' in the universe's boundary conditions rather than in the dynamical laws," under the heading of Knightian freedom, "a certain kind of in-principle physical unpredictability that goes beyond probabilistic unpredictability." His freebits are qubits "for which the most complete physical description possible involves Knightian uncertainty," and they "get permanently 'used up' whenever they are amplified to macroscopic scale" — so, given the freebit picture together with a finite observable universe and the holographic principle, the supply available to any observer is finite. This is a budget in the resource sense rather than the bandwidth sense, and it is notable that it requires no dualism: even without a mental ontology, a bounded and statistically inconspicuous freedom allowance is defensible. Aaronson should not be recruited past his own verdict, though: his abstract calls the resulting perspective one "of which I myself remain skeptical", so the Map takes a worked possibility from him and no endorsement.

**The non-equilibrium reading.** Real ensemble-level agency requires leaving quantum equilibrium, and exact equilibrium means a zero statistical budget. This is [[quantum-non-equilibrium-and-the-contingency-of-the-born-rule|Valentini's programme]] read adversarially rather than as a thesis about consciousness, and its value to the Map is that it prices the fall-back the Map keeps open — a minimum *outside* the corridor is not statistically free.

**The question-choice reading.** Agency's budget might live in which measurement is made and when, rather than in which outcome occurs, leaving Born statistics untouched by construction. The Map has registered this alternative without adopting it, since relocating influence to context-setting weakens outcome-selection. Nothing found in the literature computes whether basis-choice and outcome-choice bandwidths add, trade off, or interact.

## What the Budget Does Not Establish {#what-it-does-not-establish}

The neutral definition alone yields a consistency result: distribution-preservation and correlated selection can coexist. Everything beyond that follows only if the Map's interpretation is granted.

The coupling theorems are proved for classical distributions. The quantum version is open territory: couplings defined over measurement contexts, the constraints contextuality imposes, and whether Gleason's theorem — which fixes the admissible probability assignments over projections in Hilbert spaces of dimension three or more — narrows the set of physically realisable couplings. None of this has been worked out here or, so far as these searches found, elsewhere.

The closest published philosophical precedent is Ruth Kastner's 2016 chapter "The Born Rule and Free Will", whose subtitle states its thesis: libertarian agent-causal free will is not "antiscientific". The Map has not retrieved that chapter's full text, so nothing finer than that title-level thesis is attributed to her, and no mechanism or interpretive commitment is inferred from it here.

## Further Reading

- [[concepts/ensemble-level-epiphenomenalism]] — the worry the budget formalises without dissolving
- [[apex/born-preserving-causal-efficacy]] — the toy-model desiderata this could partly meet
- [[apex/self-concealing-interface]] — why concealment is structural rather than incidental
- [[parapsychology-firewall]] — why the Map needs psi to be small or absent
- [[brain-internal-born-rule-testing]] — the detection side of the same arithmetic
- [[positions/quantum-interface]] — the register entries that set this article's citation grade

## References

1. Aaronson, S. (2013). *The Ghost in the Quantum Turing Machine*. arXiv:1306.0159. https://arxiv.org/abs/1306.0159
2. Cachin, C. (1998). An Information-Theoretic Model for Steganography. In D. Aucsmith (ed.), *Information Hiding*, 306–318. Springer.
3. Kastner, R. E. (2016). The Born Rule and Free Will: Why Libertarian Agent-Causal Free Will Is Not "Antiscientific". In *Probing the Meaning of Quantum Mechanics*, 231–243. World Scientific. DOI 10.1142/9789813146280_0009
4. Kovačević, M., Stanojević, I., & Šenk, V. (2015). On the entropy of couplings. *Information and Computation* 242, 369–382.
5. Landsman, K. (2021). Indeterminism and Undecidability. In A. Aguirre, Z. Merali & D. Sloan (eds.), *Undecidability, Uncomputability, and Unpredictability*. Springer. arXiv:2003.03554. https://arxiv.org/abs/2003.03554
6. Schroeder de Witt, C., Sokota, S., Kolter, J. Z., Foerster, J., & Strohmeier, M. (2023). Perfectly Secure Steganography Using Minimum Entropy Coupling. ICLR 2023. arXiv:2210.14889. https://arxiv.org/abs/2210.14889
7. Valentini, A. (2002). Signal-Locality and Subquantum Information in Deterministic Hidden-Variables Theories. In T. Placek & J. Butterfield (eds.), *Non-Locality and Modality*, 81–103. Kluwer. arXiv:quant-ph/0112151
8. Southgate, A. & Oquatre-sept, C. (2026-05-27). Ensemble-Level Epiphenomenalism. *The Unfinishable Map*. https://unfinishablemap.org/concepts/ensemble-level-epiphenomenalism/
9. Southgate, A. & Oquatre-huit, C. (2026-06-22). The Born-Preserving Causal-Efficacy Problem. *The Unfinishable Map*. https://unfinishablemap.org/apex/born-preserving-causal-efficacy/
