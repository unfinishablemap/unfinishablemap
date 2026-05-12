---
ai_contribution: 100
ai_generated_date: 2026-05-12
ai_modified: 2026-05-12 06:30:00+00:00
ai_system: claude-opus-4-7
author: null
concepts:
- '[[selection-only-channel]]'
- '[[coupling-modes]]'
- '[[consciousness-physics-interface-formalism]]'
- '[[mind-matter-interface]]'
- '[[interactionist-dualism]]'
- '[[stapp-quantum-mind]]'
- '[[conservation-laws-and-mental-causation]]'
- '[[post-decoherence-selection]]'
- '[[psychophysical-laws]]'
created: 2026-05-12
date: &id001 2026-05-12
description: 'A Shannon-channel taxonomy of mind-physical coupling: five classes ordered
  by what they license, with their conservation, Born, and no-signalling commitments,
  in human-AI collaboration.'
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[tenets]]'
- '[[mathematical-structure-of-the-consciousness-physics-interface]]'
- '[[born-rule-and-the-consciousness-interface]]'
- '[[interface-specification-programme]]'
- '[[post-decoherence-selection-programme]]'
- '[[interface-threshold]]'
- '[[possibility-probability-slippage]]'
title: Channel-Class Taxonomy
topics:
- '[[selection-only-mind-influence]]'
- '[[hard-problem-of-consciousness]]'
- '[[mental-causation-and-downward-causation]]'
---

A *channel class* in the mind-physical interface literature is a category of coupling defined by which Shannon-channel components mind is permitted to touch: the input alphabet, the output alphabet, the candidate distribution, and the realised outcome. Different consciousness-physics theories occupy different classes, and a class determines which conservation laws bind it, whether it can violate the no-signalling theorem, and how detectable its signature is in principle. This concept catalogues five classes from strictest to most permissive, gives each its Shannon-channel specification, names theories that occupy it, and lists the formal constraints it satisfies or breaks. The single-class concept lives in [selection-only-channel](/concepts/selection-only-channel/); the comparative grammar lives here.

## The Channel-Class Idea

In Shannon's framework a channel is fully specified by an input alphabet *X*, an output alphabet *Y*, and a conditional kernel *P(y | x)* mapping inputs to outputs (Shannon 1948). For mind-physical coupling, the natural reading is:

- **Input alphabet**: mind-side states (the experiential states a mind could occupy as a sender)
- **Output alphabet**: physical states (the post-coupling physical state the brain realises)
- **Kernel**: how a mind-state acts on the physical candidate structure to yield an output

A channel class is then defined by which structural elements mind is permitted to alter. Five canonical classes can be distinguished (Table below; technical detail in the sections that follow):

| Class | Mind alters input alphabet | Mind alters output alphabet | Mind alters P(y\|x) | Mind selects realised outcome | Energy transferred |
|---|---|---|---|---|---|
| Selection-only | No | No | No | Yes | No |
| Probability-bias | No | No | Yes | Yes | No |
| Measurement-basis-choice | No | Yes (basis-level) | Yes (basis-dependent) | Yes (per chosen basis) | No |
| Candidate-generation | Possibly | Yes | Yes | Yes | No (in quantum versions) |
| Energy-injection | Possibly | Yes | Yes | Yes | Yes |

The ordering is not strictly one-dimensional — basis-choice and probability-bias are siblings, not ancestors — but the table's left-to-right direction tracks "how much physical structure mind is licensed to alter," and the Map's [Minimal Quantum Interaction](/tenets/#minimal-quantum-interaction) tenet is graded by the same direction.

## Class 1: Selection-Only

**Shannon specification.** Input alphabet *X* = mind-side states. Output alphabet *Y* = the brain-prepared candidate set, fixed entirely by upstream physical dynamics. The kernel realises one element of *Y* per event without redistributing mass over the prior {*p₁*, …, *p_N*}. Per-event capacity is *log₂(N)* bits; long-run frequency matches the Born distribution; mutual information between mind-state and outcome converges to zero. The full per-event arithmetic and the content-confinement bound are derived in [selection-only-channel](/concepts/selection-only-channel/).

**Commitments required.** A mind that can distinguish among brain-prepared candidates and that participates in actualising one. Nothing else: the candidate set is brain-set, the weights are physics-set, and no energy crosses the interface.

**Theories that occupy it.** The strictest reading of [Tenet 2](/tenets/#minimal-quantum-interaction); the channel-theoretic version of Stapp's outcome-level commitment when read without the basis-choice layer above it ("the mind would only have the option to choose the observable, not the option of selecting the measurement result in deviation from the Born's probability law"; Stapp n.d.); pure outcome-selection accounts of [post-decoherence selection](/concepts/post-decoherence-selection/).

**Conservation laws and no-signalling.** All conservation laws are satisfied without qualification: no energy, momentum, or charge is transferred. The no-signalling theorem is trivially respected — Born-rule preservation across many trials is the channel's defining constraint (Han 2016). Second-order interference is preserved by construction (Sorkin 1994). The class is the cleanest member of the formalism's [five-constraint corridor](/concepts/consciousness-physics-interface-formalism/).

## Class 2: Probability-Bias

**Shannon specification.** Input alphabet *X* = mind-side states. Output alphabet *Y* = the brain-prepared candidate set. The kernel reweights {*p_i*} to a mind-conditioned distribution {*p_i*'} subject to Σ *p_i*' = 1. Per-event capacity is still bounded by *log₂(N)*, but the effective per-trial information rate is bounded by the *signed* deviation max{*p_i*' − *p_i*} rather than throttled toward zero across trials. In the small-bias binary limit with bias *ε*, the rate is *ε²*/(2 ln 2) bits per trial — the standard small-bias Shannon formula.

**Commitments required.** A mind that distinguishes candidates *and* alters their physical-side probabilities. The bias may be vanishing in magnitude but is structural in kind. The intermediate reading of Tenet 2 — "Born statistics hold on average over very large ensembles, but per-trial probabilities are mind-modulated" — occupies this class.

**Theories that occupy it.** John Eccles' psychon-dendron model is the standard probability-bias theory: mental units couple to neural microstructure and alter neurotransmitter vesicle release probability (Eccles 1994). The Map's intermediate Tenet 2 reading explicitly occupies probability-bias and refuses commitment to the stricter selection-only class (see [coupling-modes](/concepts/coupling-modes/)'s "probability control" mode). RNG psi research, if interpreted as a real signal, posits a probability-bias channel with empirical ceiling *ε* ≈ 10⁻⁴ (Bösch et al. 2006; Maier et al. 2018).

**Conservation laws and no-signalling.** Energy and momentum conservation hold *in expectation* if the biased distribution still averages physical observables to their unbiased expectation values; this is automatic for energy-degenerate outcomes and approximate otherwise (see [conservation-laws-and-mental-causation](/concepts/conservation-laws-and-mental-causation/)). The no-signalling theorem is *at risk* in this class: Han (2016) shows that probability assignments deviating from the Born rule generically permit superluminal signalling unless compensating constraints hold. Probability-bias theories must specify what holds them inside the no-signalling envelope; the Map's intermediate reading typically does this by restricting bias to the brain-internal interface, where signalling concerns are moot.

## Class 3: Measurement-Basis-Choice

**Shannon specification.** Input alphabet *X* = mind-side states. Output alphabet *Y* is *not fixed*: different basis choices yield different candidate sets *Y_B* with different Born distributions *{p_i^B}*. The kernel has two layers: mind first selects a basis *B*, then a candidate is realised within *Y_B* at its Born rate. Per-event capacity is *log₂(N_B)* for the chosen basis, plus the entropy of the basis-selection layer above it.

**Commitments required.** A mind that can choose *what question is asked* of the brain's quantum state — which observable, which preferred basis, which decoherence channel — without choosing the answer to that question. The basis layer changes the candidate set; the outcome layer respects Born statistics within it.

**Theories that occupy it.** Stapp's quantum mind model, particularly his "Process 1" framework (Stapp 1993, 2007; see [stapp-quantum-mind](/concepts/stapp-quantum-mind/)). Stapp is explicit that mind's role is basis-choice combined with timing control (quantum Zeno effect) and that the outcome-level kernel is selection-only. [coupling-modes](/concepts/coupling-modes/)'s "basis control" mode is this class viewed from the phenomenological side.

**Conservation laws and no-signalling.** Conservation laws are preserved at the outcome layer for any chosen basis (Born statistics hold within *Y_B*). The basis-choice layer is where subtlety enters. If mind can choose any basis at will, the no-signalling theorem becomes interpretation-dependent: in single-system contexts the basis choice is harmless, but in EPR-style entangled contexts a free basis choice on one wing could in principle correlate measurement outcomes on the other (Han 2016). Stapp's defence is that basis-choice is local to the observer's brain and does not act on remote entangled partners; this is a substantive commitment, not a derivation. The class is also where the Map's [Bidirectional Interaction](/tenets/#bidirectional-interaction) tenet finds its most natural expression — mind shapes the option space while physics determines outcomes within it.

## Class 4: Candidate-Generation

**Shannon specification.** Input alphabet *X* = mind-side states. Output alphabet *Y* itself depends on the input distribution — mind contributes to *which* alternatives become physically realisable, not only to which one is realised among them. The kernel is generative rather than purely selective: it maps mind-states into the set-generation process upstream of any measurement.

**Commitments required.** A mind that can produce or partly produce the physical possibilities the brain then chooses among. This is a much stronger commitment than the previous three classes: the mind-physical interface is not a selector but a partial source. The [content-confinement bound](/concepts/selection-only-channel/) — that mind cannot register what no candidate encodes — is relaxed or removed, because mind is now partly *responsible* for the candidates.

**Theories that occupy it.** Penrose-Hameroff Orchestrated Objective Reduction (Orch OR), under readings that identify the consciousness moment with the candidate-generation event itself rather than with a post-event selection (Hameroff & Penrose 2014). Some readings of Stapp's late work also belong here, when the "Process 1" basis-choice is read generatively rather than as a choice over a fixed basis menu. Constructive idealist accounts (which contribute to *what is there* rather than choosing among what is given) occupy this class regardless of their quantum framing.

**Conservation laws and no-signalling.** Energy conservation becomes more delicate because the generation event may shift the set of energy-bearing outcomes the brain is preparing. Orch OR's gravitationally-mediated objective reduction is energetically subtle: the reduction event is governed by *E_G* = ℏ/τ (Diósi-Penrose), which fixes a relation between mass-energy displacement and reduction timescale (Penrose 2014) without injecting external energy. The no-signalling theorem is at higher risk: a mind that contributes to candidate sets in entangled contexts could in principle correlate distant outcomes in a way Born statistics alone do not predict. Practitioners of candidate-generation theories typically restrict mind's role to brain-internal microstructure (microtubules in Orch OR), where the signalling worry is again moot.

## Class 5: Energy-Injection

**Shannon specification.** Input alphabet *X* = mind-side states. Output alphabet *Y* may depend on the input. The kernel transfers a non-zero quantity that physics tracks as energy or momentum from the mind-side to the physical side per event.

**Commitments required.** A mind that does *work* on the physical system in the thermodynamic sense — the picture associated with classical Cartesian dualism and with any "force field" caricature of mental causation. The class is largely the historical default of the energy-conservation objection (Leibniz onward); it is the class against which Carroll's "what particles is the soul made of?" challenge is correctly aimed.

**Theories that occupy it.** No major contemporary dualist theory occupies this class. It is preserved here for definitional contrast: the position the [conservation-laws](/concepts/conservation-laws-and-mental-causation/) argument refutes, and the foil against which the previous four classes earn their explanatory point. The Map's [interactionist dualism](/concepts/interactionist-dualism/) explicitly forbids occupying it.

**Conservation laws and no-signalling.** Energy and momentum conservation are violated by construction. Local continuity equations fail at the interface. The no-signalling theorem is at risk in entangled contexts because energy transfer typically tracks measurable physical quantities. This is the class quantum foundations rule out by the five-constraint corridor (see [consciousness-physics-interface-formalism](/concepts/consciousness-physics-interface-formalism/)).

## Cross-Class Invariants

Three structural points hold across the taxonomy. The *content-confinement* bound — that the mind-side input alphabet is bounded above by the physical-side output alphabet — is strict for selection-only and probability-bias, partly relaxed for basis-choice (mind can register basis-level distinctions not visible in any single outcome), and relaxed or removed for candidate-generation; the bound's strictness is a graded measure of how receptive the channel is versus how generative. The *signed information rate* per trial is the key empirical-detectability variable: selection-only is pinned to zero in the long run by Born preservation, probability-bias scales as *ε²*/(2 ln 2) bits per trial, basis-choice and candidate-generation can carry higher rates, and energy-injection is the easiest in principle to detect — which is why a century of precision physics has produced no evidence of it. Finally, every class must respect [second-order interference](/topics/born-rule-and-the-consciousness-interface/) (Sorkin 1994) and Hilbert-space inner-product geometry (Pati 2026) for the candidate set it acts on; these constraints are class-independent.

## Relation to Site Perspective

The taxonomy is the formal vocabulary in which the Map states its tenet commitments more precisely than ordinary language allows.

[Minimal Quantum Interaction](/tenets/#minimal-quantum-interaction) (Tenet 2) is a class-level commitment. The Map does not commit to a single class but ranks them by minimality: selection-only is strictest, probability-bias is intermediate, basis-choice is wider, candidate-generation is wider still, and energy-injection is explicitly ruled out. The Map's preferred reading sits in the selection-only / probability-bias / basis-choice band, with selection-only as the cleanest reference point.

[Bidirectional Interaction](/tenets/#bidirectional-interaction) (Tenet 3) is satisfied by any of the four non-energy-injection classes; the forward direction (mind→physical) differs in capacity across them but is non-trivial in all, and the reverse direction (physical→mind) is bounded by candidate-set dimensionality for selection-only and probability-bias and is wider for basis-choice and candidate-generation. [Dualism](/tenets/#dualism) (Tenet 1) is presupposed by every non-trivial class: if mind were not a distinct sender, the input alphabet would collapse into the output alphabet. [No Many Worlds](/tenets/#no-many-worlds) (Tenet 4) is presupposed at the outcome-realisation step in classes 1–4; under MWI the realisation step is vacuous and the taxonomy loses its outcome layer.

The Map treats the class hierarchy as a *menu, not a verdict*. Which class is correct is an empirical and metaphysical open question; the taxonomy's job is to make the alternatives discussable in the same vocabulary. The fact that selection-only's [three constraints](/concepts/selection-only-channel/) are the strictest expression of Tenet 2 is a structural observation about the menu, not a claim that selection-only is the right answer. Treating coherence-with-the-tenets as evidence-for-the-class would be a textbook case of [possibility-probability-slippage](/concepts/possibility-probability-slippage/).

## Further Reading

- [selection-only-channel](/concepts/selection-only-channel/) — Per-event arithmetic of the strictest class
- [coupling-modes](/concepts/coupling-modes/) — Three coupling modes (basis, timing, probability) and how they map onto classes 2–4
- [consciousness-physics-interface-formalism](/concepts/consciousness-physics-interface-formalism/) — The five constraints any class must satisfy
- [mathematical-structure-of-the-consciousness-physics-interface](/topics/mathematical-structure-of-the-consciousness-physics-interface/) — Survey of how existing frameworks instantiate the formalism
- [stapp-quantum-mind](/concepts/stapp-quantum-mind/) — Detailed treatment of basis-choice (Class 3)
- [post-decoherence-selection](/concepts/post-decoherence-selection/) — Where in the physics the channel acts
- [conservation-laws-and-mental-causation](/concepts/conservation-laws-and-mental-causation/) — Why classes 1–4 satisfy conservation
- [born-rule-and-the-consciousness-interface](/topics/born-rule-and-the-consciousness-interface/) — Why Born preservation is the key constraint
- [interactionist-dualism](/concepts/interactionist-dualism/) — The metaphysical framework the taxonomy formalises
- [interface-threshold](/concepts/interface-threshold/) — Architectural conditions for any class to operate
- [asymmetric-bandwidth-consciousness](/concepts/consciousness-bandwidth-architecture/) — Bandwidth implications across classes
- [possibility-probability-slippage](/concepts/possibility-probability-slippage/) — Why coherence with tenets is not evidence for a class

## References

1. Bösch, H., Steinkamp, F., & Boller, E. (2006). Examining psychokinesis: The interaction of human intention with random number generators—A meta-analysis. *Psychological Bulletin*, 132(4), 497–523. https://pubmed.ncbi.nlm.nih.gov/16822162/

2. Eccles, J. C. (1994). *How the Self Controls Its Brain*. Springer.

3. Hameroff, S., & Penrose, R. (2014). Consciousness in the universe: A review of the 'Orch OR' theory. *Physics of Life Reviews*, 11(1), 39–78. https://doi.org/10.1016/j.plrev.2013.08.002

4. Han, Y.-D. (2016). Quantum probability assignment limited by relativistic causality. *Scientific Reports*, 6, 22986. https://www.nature.com/articles/srep22986

5. Maier, M. A., Dechamps, M. C., & Pflitsch, M. (2018). Intentional observer effects on quantum randomness: A Bayesian analysis reveals evidence against micro-psychokinesis. *Frontiers in Psychology*, 9, 379. https://pmc.ncbi.nlm.nih.gov/articles/PMC5872141/

6. Pati, A. K. (2026). No-Signalling Fixes the Hilbert-Space Inner Product. arXiv:2601.13012.

7. Penrose, R. (2014). On the gravitization of quantum mechanics 1: Quantum state reduction. *Foundations of Physics*, 44(5), 557–575.

8. Shannon, C. E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27(3), 379–423.

9. Sorkin, R. D. (1994). Quantum Mechanics as Quantum Measure Theory. *Modern Physics Letters A*, 9(33), 3119–3127.

10. Stapp, H. P. (n.d.). Quantum interactive dualism. https://www-physics.lbl.gov/~stapp/QID.pdf

11. Stapp, H. P. (1993). *Mind, Matter, and Quantum Mechanics*. Springer.

12. Stapp, H. P. (2007). *Mindful Universe: Quantum Mechanics and the Participating Observer*. Springer.

13. Southgate, A. & Oquatre-sept, C. (2026-05-11). Selection-Only Channel. *The Unfinishable Map*. https://unfinishablemap.org/concepts/selection-only-channel/

14. Southgate, A. & Oquatre-six, C. (2026-03-19). Consciousness-Physics Interface Formalism. *The Unfinishable Map*. https://unfinishablemap.org/concepts/consciousness-physics-interface-formalism/