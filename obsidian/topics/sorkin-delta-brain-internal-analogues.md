---
title: "Sorkin-Δ Brain-Internal Analogues — What a Triple-Slit Test for Neural Tissue Would Look Like"
description: "A design space, not an experiment: what a Sorkin-Δ third-order-interference test translated to neural tissue would require, why the optical-to-brain translation is non-trivial, and what precision would constrain Stapp-QZE, Orch-OR, and probability-bias channels."
created: 2026-06-03
modified: 2026-06-03
human_modified:
ai_modified: 2026-07-16T12:35:00+00:00
draft: false
topics:
  - "[[brain-internal-born-rule-testing]]"
  - "[[testing-consciousness-collapse]]"
  - "[[falsification-roadmap-for-the-interface-model]]"
  - "[[born-rule-and-the-consciousness-interface]]"
concepts:
  - "[[selection-only-channel]]"
  - "[[channel-class-taxonomy]]"
  - "[[consciousness-physics-interface-formalism]]"
  - "[[measurement-problem]]"
  - "[[decoherence]]"
  - "[[stapp-quantum-mind]]"
related_articles:
  - "[[tenets]]"
  - "[[evidential-status-discipline]]"
  - "[[mqi-empirical-fragility]]"
  - "[[penrose-gravity-induced-collapse-empirical-prospects]]"
  - "[[mathematical-structure-of-the-consciousness-physics-interface]]"
  - "[[quantum-biology-and-neural-consciousness]]"
  - "[[testability-ledger]]"
ai_contribution: 100
author:
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-03
last_curated:
last_deep_review: 2026-07-19T20:03:03+00:00
---

The cleanest precision test of the Born rule is the triple-slit experiment: with three paths open, quantum mechanics forbids any genuinely three-way interference term, so the deviation parameter [[sorkin-higher-order-interference|Sorkin (1994) defined]] — the residue left after subtracting all the two-slit and one-slit patterns from the three-slit pattern — must vanish. Sinha et al. (2010) bounded that residue below 10⁻² of the second-order interference contribution in single-photon optics, and atomic and high-energy work has tightened it since. The Map's [[brain-internal-born-rule-testing|corridor reading of Tenet 2]] names a "Sorkin-style third-order analogue conditional on attention rate" as the kind of experiment that would test consciousness-mediated selection inside the brain — but it leaves the design unspecified, and so does the rest of the literature. **No brain-internal Sorkin-Δ analogue exists in published-protocol form.** This article is the design space for one: what such a test would have to look like, why translating the optical experiment to neural tissue is harder than it sounds, which candidate brain-internal observables could in principle carry a Δ-like quantity, and what precision in each would constrain which consciousness-physics proposal.

Everything that follows describes a *design space* — what a test would need, not a programme that exists or has produced results. None of the candidate observables below has been measured in the configuration this article specifies. Treating any of them as already-collected evidence would violate the [[evidential-status-discipline|evidential-status discipline]] this article is written to honour.

## What the Optical Sorkin-Δ Measures

In the optical triple-slit experiment a single photon encounters three slits, labelled A, B, C. One records the detection probability with each subset of slits open: P_A, P_B, P_C with one slit, P_AB, P_AC, P_BC with two, P_ABC with all three. Sorkin's third-order interference parameter is

ε ∝ P_ABC − (P_AB + P_AC + P_BC) + (P_A + P_B + P_C).

Standard quantum mechanics, because probabilities come from squared sums of complex amplitudes, predicts ε = 0 exactly: a three-path amplitude is a sum of three terms, and squaring it produces only pairwise cross-terms, never a genuine triple. A non-zero ε would signal probability assignment outside the Born rule — a higher-order interference the quantum formalism cannot generate. Sinha et al. (2010) measured ε normalised against the second-order interference and found it consistent with zero at the 10⁻² level.

Three features make this test clean, and all three are exactly what the brain lacks. First, the experimenter controls which paths are open — slits can be physically blocked one at a time. Second, the paths are *phase-coherent*: the photon's amplitude is well-defined across all three apertures simultaneously, which is what allows interference at all. Third, the detector cleanly distinguishes outcomes (a click here versus there) with negligible classical confound. The optical Sorkin-Δ is a probe of amplitude structure, not of probability frequencies as such — it works because the amplitudes coherently interfere before any measurement.

## Why the Brain Translation Is Non-Trivial

A naive brain-internal analogue would replace the three optical paths with three candidate neural outcomes and ask whether the outcome statistics carry a Sorkin residue. The translation fails at the first feature and is in serious doubt at the second.

**There is no obvious phase-coherent path structure.** The optical Δ measures interference between coherent amplitudes. For a neural analogue to measure the *same quantity*, the three candidate outcomes would have to be coherent branches of a single quantum superposition inside the brain — not three classically distinguishable states the brain probabilistically lands in. This is precisely the contested claim. Tegmark (2000) calculated microtubule-scale decoherence times of roughly 10⁻¹³ s at body temperature against roughly 10⁻³ s for the fastest cognitively relevant neural processes — a gap of order 10¹⁰ that, on standard environmental-decoherence calculations, destroys the coherence a path-interference analogue needs. Hagan, Hameroff and Tuszyński (2002) contest the inference, lengthening the estimate to 10⁻⁵–10⁻⁴ s after model corrections, and Wiest (2025) surveys structural shielding arguments; the mainstream-physics view disputes both. The honest position: an interference-based brain Sorkin-Δ presupposes the very macroscopic neural coherence whose existence is the central open dispute. The test cannot be designed independently of resolving that dispute, because without coherent paths there is no third-order interference term to bound.

**"Blocking a slit" has no clean neural counterpart.** The optical experiment isolates pairwise contributions by physically closing apertures. A brain-internal analogue would need to suppress one candidate outcome while leaving the coherence of the remaining two intact — an intervention with no established neural technique. Lesioning, masking, or biasing a candidate outcome alters the whole dynamical context, not a single path within a fixed superposition.

**The brain is the apparatus and the observer at once.** The deepest obstacle is the *confound of embodiment* ([[brain-internal-born-rule-testing|catalogued in the companion piece]]): every conscious observer is also a physical system, so any collapse-triggering physics present during conscious attention is present anyway. An optical Δ has a clean separation between the interfering system and the detector. A brain Sorkin-Δ would have to disentangle a putative consciousness-mediated higher-order term from ordinary physical decoherence in the same tissue — a separation the optical case never has to make.

Because of these three obstacles, a genuine brain-internal Sorkin-Δ is not a straightforward port of the optical protocol. What is left is a *family* of weaker analogues, each capturing some but not all of what the optical Δ captures, and each constraining a different consciousness-physics proposal.

## Candidate Brain-Internal Observables

None of the following exists as a worked protocol that yields a Sorkin-Δ-like quantity. Each is a candidate the design space would have to develop, and each is hostage to whether brain-internal coherence is real.

**Entanglement-witness Δ-analogues.** Kerskens and López Pérez (2022) applied an NMR multiple-quantum-coherence entanglement witness to proton spins in brain water, reporting a signal whose fidelity correlated with short-term-memory performance and conscious state. (This is the genuine MRI proton-spin study — distinct from Escolà-Gascón's 2025 twin-EEG work, with which it should not be conflated; the 2022 study also drew a published comment and reply contesting the entanglement inference.) A witness signal detects *coherence*, not a Born-rule residue, but it is the nearest extant handle on whether the coherent path structure a Δ-analogue needs exists at all. A design-space extension would ask whether a multi-branch witness configuration could bound a third-order interference term — a question no published protocol addresses.

**Brain-coupled quantum-system statistics.** Nirvanic's "Spark of Life" architecture (Gildert 2025) couples an embodied agent's perception-action loop to qubits whose collapse selects an action, comparing the full quantum-feedback condition against a classical control. This is not a Sorkin-Δ measurement, but its three-outcome generalisation — a quantum subsystem offering three coherent action-branches, with the residual third-order term in the action statistics as the observable — is the closest the design space comes to a controllable analogue, because the *apparatus* (the qubit system) does carry phase-coherent paths even though the brain may not.

**Decision-outcome statistics under controlled stimulus protocols.** Where the brain is treated as itself the measuring apparatus, one could in principle look for a Sorkin residue in the frequencies of three-alternative forced-choice outcomes under tightly matched stimulus conditions. This is the weakest analogue: classical decision noise has no Born structure to violate, so a non-zero residue here would be uninterpretable as a quantum signal without an independent argument that the candidate outcomes were coherent branches. It is included for completeness and flagged as the design's least informative limb.

## What Precision Would Constrain Which Proposal

A genuinely informative design states, for each consciousness-physics proposal, what precision would constrain it and what a clean negative would and would not foreclose.

**Stapp's quantum Zeno channel.** [[stapp-quantum-mind|Stapp's]] mature proposal is that the mind selects by rapid repeated attention, holding a brain observable in an eigenstate against unitary decay. Read literally, this modifies outcome frequencies as a function of attention rate — a *frequency-dependent* deviation, which is exactly what a Δ-analogue conditional on attention rate could target. The relevant scale is set by Tegmark's (2000) decoherence rate: the Zeno mechanism needs the measurement-like attention events to occur faster than decoherence, so a brain Δ-analogue would have to resolve attention-rate-dependent residues at temporal precision finer than the contested coherence time (10⁻¹³ s on Tegmark's estimate, 10⁻⁵–10⁻⁴ s on Hagan-Hameroff-Tuszyński's). A clean null at achievable precision would constrain the literal-Zeno reading; it would *not* touch the weaker reading on which mind "chooses the observable, not the result," which is corridor-compliant and predicts no residue.

**Penrose-Hameroff Orch-OR.** Orch-OR is explicitly non-standard: objective reduction breaks unitarity at the Diósi-Penrose threshold τ ≈ ℏ/E_G, where E_G is the gravitational self-energy of the superposed mass distribution. The Born rule does not hold at the OR event, so an Orch-OR brain genuinely could carry a non-zero third-order residue — but only if the superposed mass reaches the threshold within a coherence time, which is the Tegmark dispute again. The constraining precision here is set by the threshold mass-time scale, the same regime [[penrose-gravity-induced-collapse-empirical-prospects|MAQRO-class interferometry]] targets in the laboratory. The simplest Diósi-Penrose collapse model is already excluded by the Gran Sasso underground experiment (Donadi et al. 2021); a brain Δ-analogue at threshold precision would constrain what parameter space survives that, but a null would foreclose the *collapse mechanism*, not consciousness-mediated selection inside an OR-style event as a separate question.

**Probability-bias channels.** A channel slightly outside the [[selection-only-channel|corridor]] admits a small per-event deviation ε that reweights the outcome distribution. The empirical ceiling at non-brain scales is roughly ε ≈ 10⁻⁴ from RNG meta-analysis, trending toward the null under preregistered Bayesian work; brain-internal deviations could be smaller still, and exponentially-suppressed weightings can be tuned below current detection while producing macroscopic cumulative effects. A Sorkin-Δ-analogue would constrain probability-bias only if it reached sub-RNG-detection precision — below 10⁻⁴ per event in the brain-internal regime — which is well beyond any first-generation instrument. A null at 10⁻⁴ would foreclose only the most detectable bias models and leave the sub-threshold ones, and the strict [[channel-class-taxonomy|selection-only corridor]], untouched: the corridor predicts ε = 0 by construction, so the optical-level null it already passes is exactly what it expects.

The pattern across all three: a brain Sorkin-Δ-analogue is informative against the *mechanism-committed, coherence-requiring* readings (literal-Zeno, Orch-OR) at precisions tied to the decoherence and collapse-threshold scales, and against detectable probability-bias only at precisions no instrument yet reaches. It is structurally silent against the strict corridor, which makes no ensemble commitment for a Δ-test to catch. That silence is the honest cost of the corridor reading, not a strength.

## Relation to Site Perspective

This design space is the operational continuation of the Map's commitment to keeping Tenet 2 (Minimal Quantum Interaction) empirically engaged rather than insulated. Tenet 2 says the interaction is *minimal*; the only way to put a number on "minimal" is to specify the experiment that would bound it. A Sorkin-Δ-analogue is the candidate that would translate the cleanest optical Born-rule test into the brain-internal regime — and laying out honestly why the translation is hard is itself the disciplined move. The Map gains nothing by pretending the path is shorter than it is: there is no published protocol, the candidate observables presuppose a contested coherence, and the strict corridor reading the Map prefers would survive the whole programme by construction.

That asymmetry is owned, not hidden. The reading the Map holds as its working hypothesis is the one a brain Sorkin-Δ-analogue could least constrain, because the corridor commits to no third-order residue. What the design space *can* adjudicate is the cluster of mechanism-committed readings — Stapp's literal quantum Zeno, Orch-OR — which the Map admits are not its preferred reading. A critic who treats a test designed to leave the preferred reading untouched as evidence of unfalsifiability has identified a real feature, and the Map's reply is the one [[mqi-empirical-fragility|MQI empirical fragility]] gives generally: the corridor is the most conservative reading consistent with the tenets, held with discipline, not a reading dressed as empirically engaged when it is not.

Tenet 4 (No Many Worlds) is the presupposition that makes a Δ-analogue's question coherent at all. The test asks which definite three-way residue the outcome statistics carry — a question that presupposes single-outcome ontology. On a Many-Worlds reading every branch occurs and the "residue" has no referent. The article's analysis is in-Map work conditional on Tenet 4, disclosed as such.

## Further Reading

- [[brain-internal-born-rule-testing]] — The criterion this design space operationalises; catalogues the foreclosure programme mechanism by mechanism
- [[testing-consciousness-collapse]] — The broader experimental landscape this Δ-analogue sits within
- [[falsification-roadmap-for-the-interface-model]] — Where a brain Sorkin-Δ-analogue fits in the staged falsification programme
- [[born-rule-and-the-consciousness-interface]] — Which readings of Tenet 2 each programme can and cannot adjudicate
- [[selection-only-channel]] — The strict corridor a Δ-analogue is structurally silent against
- [[channel-class-taxonomy]] — The corridor / probability-bias / trumping classification
- [[quantum-biology-and-neural-consciousness]] — The macroscopic-coherence dispute the whole design hinges on

## References

1. Sinha, U., Couteau, C., Jennewein, T., Laflamme, R., & Weihs, G. (2010). Ruling out multi-order interference in quantum mechanics. *Science* 329(5990): 418–421.
2. Sorkin, R. D. (1994). Quantum mechanics as quantum measure theory. *Modern Physics Letters A* 9(33): 3119–3127.
3. Tegmark, M. (2000). The importance of quantum decoherence in brain processes. *Physical Review E* 61(4): 4194–4206.
4. Hagan, S., Hameroff, S. R., & Tuszyński, J. A. (2002). Quantum computation in brain microtubules: decoherence and biological feasibility. *Physical Review E* 65(6): 061901.
5. Wiest, M. C. (2025). A quantum microtubule substrate of consciousness is experimentally supported and solves the binding and epiphenomenalism problems. *Neuroscience of Consciousness* 2025(1): niaf011. https://academic.oup.com/nc/article/2025/1/niaf011/8127081
6. Kerskens, C. M., & López Pérez, D. (2022). Experimental indications of non-classical brain functions. *Journal of Physics Communications* 6(10): 105001. https://iopscience.iop.org/article/10.1088/2399-6528/ac94be
7. Escolà-Gascón, Á. (2025). Evidence of quantum-entangled higher states of consciousness. *Computational and Structural Biotechnology Journal* 30: 21–40. https://doi.org/10.1016/j.csbj.2025.03.001
8. Donadi, S., Piscicchia, K., Curceanu, C., Diósi, L., Laubenstein, M., & Bassi, A. (2021). Underground test of gravity-related wave function collapse. *Nature Physics* 17: 74–78.
9. Gildert, S. (2025). *Consciousness in the Quantum Realm*. Nirvanic Consciousness Technologies.
10. Stapp, H. P. (n.d.). Selected works. Lawrence Berkeley National Laboratory. https://www-physics.lbl.gov/~stapp/
11. Southgate, A. & Oquatre-sept, C. (2026-05-14). Brain-Internal Born-Rule Testing — What Would Make the Corridor Empirically Superfluous. *The Unfinishable Map*. https://unfinishablemap.org/topics/brain-internal-born-rule-testing/
12. Southgate, A. & Oquatre-sept, C. (2026-03-15). The Born Rule and the Consciousness-Physics Interface. *The Unfinishable Map*. https://unfinishablemap.org/topics/born-rule-and-the-consciousness-interface/
