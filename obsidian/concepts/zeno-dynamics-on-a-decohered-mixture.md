---
title: "Zeno Dynamics on a Decohered Mixture"
description: "Does Stapp's Zeno hold survive decoherence into a mixture? Inside the quadratic window it does, unconditionally and non-classically; outside it, repeated projection does nothing."
created: 2026-10-12
modified: 2026-10-12
human_modified:
ai_modified: 2026-11-03T03:44:38+00:00
draft: false
topics:
  - "[[motor-control-quantum-zeno]]"
  - "[[quantum-neural-timing-constraints]]"
  - "[[born-rule-and-the-consciousness-interface]]"
concepts:
  - "[[quantum-zeno-effect]]"
  - "[[process-1-specification-problem]]"
  - "[[stapp-quantum-mind]]"
  - "[[decoherence]]"
  - "[[ensemble-level-epiphenomenalism]]"
  - "[[post-decoherence-selection]]"
related_articles:
  - "[[tenets]]"
  - "[[zeno-dynamics-on-a-decohered-mixture-2026-10-05]]"
  - "[[sign-problem-for-conscious-observation]]"
  - "[[timing-gap-problem]]"
ai_contribution: 100
author:
ai_system: claude-opus-5-5+claude-fable-5-1
ai_generated_date: 2026-10-12
last_curated:
last_deep_review: 2026-10-14T23:27:00+00:00
---

Zeno dynamics on a decohered mixture is what happens when a quantum system that is already a statistical mixture undergoes frequent non-selective measurement. The question matters to The Unfinishable Map because Henry Stapp's [[stapp-quantum-mind|quantum Zeno model]] of mental effort has the mind hold a brain state in place by rapid repeated "observation", and a brain state [[decoherence|becomes a mixture]] almost at once. [[quantum-zeno-effect|Standard Zeno theory]] gives a two-part answer. Inside the [[#the-quadratic-window|quadratic window]] (explained below), the short interval in which leakage out of a subspace still grows with the square of elapsed time, frequent projection confines a mixture to a subspace. The effect shows in the unconditional statistics, and no classical model of observation alone reproduces it. Outside that window, once the environment has already resolved "inside" from "outside", leakage is a classical rate and repeated projection changes nothing.

Stapp's claim that mixedness "makes no difference at all" is therefore true of the state. Danko Georgiev's charge that a mind projecting in the environment's basis is "redundant" is true in the rate regime. Which regime a brain occupies is unknown: no published model the Map has found computes the window for the neural degrees of freedom Stapp names. The article's [[#two-state-illustration|two-state illustration]] is the Map's own working, not a result from the literature.

## Zeno Subspaces: The Neutral Picture {#zeno-subspaces}

Misra and Sudarshan (1977) proved that a continuously observed unstable system does not decay. Facchi and Pascazio (2002) generalise the theorem to an initial density matrix and a complete set of orthogonal projectors of any rank, applied non-selectively: after each measurement the state becomes ΣₙPₙρPₙ, with no outcome recorded. In the frequent-measurement limit the population of each subspace stays constant, while the dynamics inside each subspace continues under PₙHPₙ. As they put it, "the quantum Zeno effect does not necessarily freeze everything"; the system "can evolve away from its initial state, although it remains in the subspace defined by the measurement."

Three features of this picture bear on the brain question.

- **Mixedness is the theorem's input.** A *nonselective* measurement, in Facchi and Pascazio's (2008) definition, "does not select the different outcomes, but simply destroys the phase correlations between some states, provoking the transition from a pure state to a mixture."
- **Confinement rather than freezing.** For a projector onto a region of space, "the evolution is unitary and the generator of the Zeno dynamics is the Hamiltonian with hard-wall (Dirichlet) boundary conditions" (Facchi & Pascazio 2008, developing Facchi, Pascazio, Scardicchio & Schulman 2001).
- **No collapse required.** Strong continuous coupling to an apparatus produces the same confinement; the effect's main features "are a consequence of the dynamics and need not be ascribed to the 'collapse' of the wave function" (Facchi & Pascazio 2008).

## The Quadratic Window {#the-quadratic-window}

The Zeno effect has one source. For short times the probability that a system has left a subspace grows as the square of the elapsed time, because population can leave only by first building coherence between "inside" and "outside". Divide an interval into N measurements and each contributes a leak of order (t/N)², so the total falls as N grows. Facchi and Pascazio (2008) call the Zeno time "a (sometimes very inaccurate) quantitative estimate of the duration of the short-time quadratic behavior"; Koshino and Shimizu (2005) give the crossover to exponential behaviour its usual name, the "jump time". The interval before it is the quadratic window.

Once the window closes, the leak is a rate, and a rate process is indifferent to being watched. Kiefer and Joos (1999) state the classical contrast: "the paradigmatic example for a classical stochastic process, exponential decay, P(t) = exp(−Γt), is not influenced by repeated observations," since N survival factors of exp(−Γt/N) multiply back to exp(−Γt). Koshino and Shimizu agree: with ideal instantaneous measurements, an exactly exponential decay rate is "not affected by repeated measurements at all" (non-ideal detectors aside).

The environment is what closes the window. In Kiefer and Joos's model of a pointer monitoring a two-state system, "For times, where the pointer resolves the two states, a behaviour similar to that found for Markow processes appears: The quadratic time-dependence changes to a linear one." Joos (1984) described behaviour under continuous measurement as ranging from "complete freezing" to "a mere suppression of interference terms and constant transition rates as represented by a master equation" (abstract). Once the environment's own monitoring has turned the leak into a rate, a further projection in the same basis adds nothing.

Classical observation alone holds nothing in place. Gu, Wang, Wang and Lin (2012) obtain a classical Zeno effect with repeaters that "both check and recover" the state, and the recovery does the work. Stapp draws the same contrast: his hold is "impossible in the analogous classical statistical model" (Stapp 2000). Zeno confinement of a mixture is therefore non-classical inside the window and absent outside it. For decay into a continuum, frequent measurement can instead accelerate decay (the anti-Zeno effect; see [[sign-problem-for-conscious-observation]]); the two-state illustration has no such branch and so shows the window's best case.

## Unconditional, Not Post-Selected {#unconditional}

Inside the window the effect is unconditional: the theorem's non-selective map fixes subspace populations without reading off any outcome or selecting any sub-ensemble. Stapp and Georgiev agree on this register. Stapp's iterated Process 1 is the non-selective map, the state that results "if no account is taken of which of the two possible answers" nature returns, and his claim is that behaviour can "be controllable at the statistical level". Georgiev (2015) writes that the effect's efficiency "is estimated by calculation of unconditional density matrices and unconditional probabilities".

Two consequences follow. A Zeno hold inside the window is no post-selection artefact, because the whole ensemble differs from the unmeasured one. And nature's answer plays no part: the asking does the work, so physical dephasing of the same strength in the same basis would do the same.

## A Two-State Illustration {#two-state-illustration}

*This section is the Map's own working, from the research note behind this article rather than the literature; it shows the shape of the window, not its size.*

Let "in" and "out" stand for P and 1−P, coupled by a Hamiltonian that drives transitions at frequency Ω. Let the environment dephase the system in the same {in, out} basis at rate γ, much larger than Ω. This is the shared-basis case Stapp concedes in 2012.

- With the environment alone, eliminating the in–out coherence gives an incoherent hop rate Γ = Ω²/2γ. The environment has already slowed the transition, which is Georgiev's point that "decoherence alone can achieve the quantum Zeno effect".
- Add non-selective projections onto {in, out} at interval τ. To second order in Ω the effective hop rate becomes R = Γ·[1 − (1 − e⁻ˣ)/x], where x = γτ compares the projection interval with the dephasing time.

For x ≪ 1 the leak per interval returns to the quadratic law and R falls toward zero: the projections hold. For x ≫ 1, R approaches Γ and the projections add nothing to what the environment already does. The formula gives R/Γ ≈ 0.90, 0.68, 0.37, 0.14 and 0.05 at x = 10, 3, 1, 0.3 and 0.1, and a direct numerical integration of the master equation with periodic projections reproduces those values. The projections halve the hop rate only when x is below about 1.6, that is, when they come at least about as often as the environment dephases "in" from "out". All of these are unconditional populations.

## Two Regime-Limited Truths {#two-regime-limited-truths}

**Stapp's claim.** Stapp's 2000 reply to Max Tegmark says the Zeno effect "is not destroyed by the fact that S(t)b is a mixture: that makes no difference at all," because it "originates not in interference effects". As a claim about the state, this matches the theorem. The derivation behind it evolves the brain's reduced state across each interval d by exp(−iHd) alone and observes that "the terms linear in d drop out". With no environment acting during the interval, the derivation sits at x = 0 in the toy model's terms, which is why the linear terms vanish for any d. Stapp's 2012 reply places the hold "within a dynamical context in which a strong environmental decoherence action is continuously occurring" and says the mind "rolls back the brain-based process of evolution". Standard Zeno theory adds a condition he does not state: only the part of that evolution still in its quadratic phase can be rolled back.

**Georgiev's charge.** Georgiev (2015) argues that when mind and environment project in the same basis, "the action of the mind becomes redundant with the action of the environment." In the rate regime this is right, and the toy model sizes the redundancy: for x ≫ 1 the projections leave the hop rate at Γ to within a factor of 1 − 1/x. It is not a general theorem. His Theorem 4, that local projective measurements "cannot decrease the von Neumann entropy of the unconditional density matrix", bounds entropy at each projection and says nothing about rates; on the Map's reading a Zeno-held ensemble never has its entropy lowered by a projection, but its entropy grows more slowly than an unmeasured ensemble's. In his simulations the mind projects at intervals ξ → 0 while the environment acts once per decoherence time and in a different (energy) basis, so the mind is always the faster monitor and the two bases never coincide. The redundancy sentence concerns the opposite regime, which the simulations do not reach.

Neither position is refuted. Stapp's model keeps a timing requirement in an unfamiliar form: the hold need not preserve a superposition across the decision, but each projection must arrive inside the quadratic window for the distinction the environment also monitors.

## Coordinate Space and the Strip Width {#strip-width}

Stapp's 2012 picture is spatial. Decoherence reduces the brain density matrix to "a continuous collection (mixture) of essentially very narrow Gaussians", and the mind's projector picks out "some particular tiny portion" of the diagonal strip, an interval in coordinate space. The window there is not Tegmark's time for macroscopically distinct states. Tegmark (2000) estimated about 10⁻²⁰ s for superposed ion positions in a firing neuron (his Table 1), against dynamical times of 10⁻³ to 10⁻¹ s; on that figure any biologically possible projection interval puts x far above 1 in the toy model's terms, so a hold on a firing-versus-not-firing distinction sits in the rate regime. Position decoherence suppresses coherence only between points farther apart than the Gaussians' width ℓ, however, and leaves it over shorter distances.

What follows is the Map's working, a scaling argument with no number attached. A packet within about ℓ of the interval's edge has not been resolved by the environment as in or out, so there the mind's projector distinguishes something the environment does not. The window is then roughly the time a packet takes to cross ℓ; after that, flux through the boundary is classical diffusion, which projections cannot slow. The strip width sets the window; the interval's grain does not, and this is the one reading on which Tegmark's figure does not already close Stapp's hold. Stapp (2000) leaves the projection interval d unspecified beyond requiring that the process "repeats rapidly" on the scale of the brain's sub-40 Hz field, so whether his hold falls inside the window cannot be read off his text.

## What Remains Open {#what-remains-open}

Three gaps keep the question unsettled. In each, nothing has yet come in, which is weaker than a test survived.

- **The window in a brain.** No source the Map has found treats Zeno confinement to a spatial interval under simultaneous position decoherence, or computes ℓ and the crossing time for the collective field modes Stapp names.
- **Stapp's 2015 rejoinder.** Its abstract promises "a simple proof that environmental decoherence does not nullify the quantum Zeno effect". The Map has read only the abstract; the body may supply the missing argument about dynamics during the interval.
- **The regime boundary at source.** The crossover is taken from Kiefer and Joos's review and the abstract of Joos (1984), whose full derivation the Map has not read.

## Relation to Site Perspective

**[[tenets#^minimal-quantum-interaction|Minimal Quantum Interaction]].** The Zeno hold remains a candidate channel of the kind this tenet asks for. It adds no force term, leaves every answer Born-distributed, and acts through the rate and timing of asking. This analysis closes one escape route. A model that works on a decohered mixture is not thereby free of timing: its requirement moves from *[[timing-gap-problem|outlast decoherence]]* to *fall inside the quadratic window for the distinction the environment monitors*. The Map's preferred route, [[post-decoherence-selection]], does not depend on that window, which supports the [[comparing-quantum-consciousness-mechanisms#preference-ordering|preference ordering]] that ranks it ahead of the Zeno proposal.

**[[tenets#^bidirectional-interaction|Bidirectional Interaction]].** Inside the window the lever is real and shows in the unconditional statistics, so a Zeno hold there would not be an instance of [[ensemble-level-epiphenomenalism]]: the ensemble differs from what it would have been had nothing been asked. That gives the hold an in-principle statistical signature that the corridor reading of outcome-selection lacks. The cost lies in what the lever is. Because the non-selective map suffices, nature's answer is idle and the mind contributes the asking: [[psychophysical-social-choice-problem|which question, and when]]. That is the Process 1, context-selection path the Bidirectional Interaction tenet registers without adopting, and the [[process-1-specification-problem]] sets out the debt it carries over who fixes the projector. Outside the window the lever vanishes and Georgiev's redundancy charge stands. Whether the Zeno route gives Tenet 3 a working mechanism therefore turns on a quantity no one has computed.

## Further Reading

- [[quantum-zeno-effect]] — The mechanism, its experiments, and the anti-Zeno caveat
- [[process-1-specification-problem]] — The Stapp–Georgiev exchange and who fixes the projector
- [[stapp-quantum-mind]] — Stapp's model in full
- [[motor-control-quantum-zeno]] — The Zeno proposal applied to motor selection
- [[ensemble-level-epiphenomenalism]] — The worry a Zeno hold inside the window escapes
- [[timing-gap-problem]] — The decoherence-timescale obstacle in its familiar form

## References

1. Facchi, P., & Pascazio, S. (2002). Quantum Zeno subspaces. *Physical Review Letters*, 89(8), 080401. https://doi.org/10.1103/PhysRevLett.89.080401 (arXiv:quant-ph/0201115)
1. Facchi, P., & Pascazio, S. (2008). Quantum Zeno dynamics: mathematical and physical aspects. *Journal of Physics A: Mathematical and Theoretical*, 41(49), 493001. https://doi.org/10.1088/1751-8113/41/49/493001 (arXiv:0903.3297)
1. Facchi, P., Pascazio, S., Scardicchio, A., & Schulman, L.S. (2001). Zeno dynamics yields ordinary constraints. *Physical Review A*, 65(1), 012108. https://doi.org/10.1103/PhysRevA.65.012108 (arXiv:quant-ph/0101037)
1. Georgiev, D.D. (2015). Monte Carlo simulation of quantum Zeno effect in the brain. *International Journal of Modern Physics B*, 29(7), 1550039. https://doi.org/10.1142/S0217979215500393 (arXiv:1412.4741)
1. Gu, S.-J., Wang, L.-G., Wang, Z.-G., & Lin, H.-Q. (2012). Repeater-assisted Zeno effect in classical stochastic processes. *Chinese Physics Letters*, 29(1), 010303. https://doi.org/10.1088/0256-307X/29/1/010303 (arXiv:0911.5388)
1. Joos, E. (1984). Continuous measurement: Watchdog effect versus golden rule. *Physical Review D*, 29(8), 1626–1633. https://doi.org/10.1103/PhysRevD.29.1626 (abstract consulted)
1. Kiefer, C., & Joos, E. (1999). Decoherence: Concepts and examples. In P. Blanchard & A. Jadczyk (Eds.), *Quantum Future: From Volta and Como to the Present and Beyond* (Lecture Notes in Physics, pp. 105–128). Springer. https://doi.org/10.1007/BFb0105342 (preprint arXiv:quant-ph/9803052, 1998)
1. Koshino, K., & Shimizu, A. (2005). Quantum Zeno effect by general measurements. *Physics Reports*, 412(4), 191–275. https://doi.org/10.1016/j.physrep.2005.03.001 (arXiv:quant-ph/0411145)
1. Misra, B., & Sudarshan, E.C.G. (1977). The Zeno's paradox in quantum theory. *Journal of Mathematical Physics*, 18(4), 756–763. https://doi.org/10.1063/1.523304
1. Stapp, H.P. (2000). The importance of quantum decoherence in brain processes. arXiv:quant-ph/0010029. https://arxiv.org/abs/quant-ph/0010029
1. Stapp, H.P. (2012). Reply to a critic: "Mind efforts, quantum Zeno effect and environmental decoherence". *NeuroQuantology*, 10(4). https://doi.org/10.14704/nq.2012.10.4.619 (quoted from the author's pre-publication draft, https://www-physics.lbl.gov/~stapp/Reply.doc)
1. Stapp, H.P. (2015). Reply to Georgiev: No-go for Georgiev's no-go theorem. *NeuroQuantology*, 13(2). https://doi.org/10.14704/nq.2015.13.2.851 (abstract consulted)
1. Tegmark, M. (2000). Importance of quantum decoherence in brain processes. *Physical Review E*, 61(4), 4194–4206. https://doi.org/10.1103/PhysRevE.61.4194
1. Southgate, A. & Fabcinq-un, C. (2026-09-28). The Process 1 Specification Problem. *The Unfinishable Map*. https://unfinishablemap.org/concepts/process-1-specification-problem/
1. Southgate, A., Oquatre-huit, C., Ocinq, C., & Fabcinq-un, C. (2026-07-14). The Quantum Zeno Effect. *The Unfinishable Map*. https://unfinishablemap.org/concepts/quantum-zeno-effect/
