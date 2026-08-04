---
title: Research Notes - Analog Quantum Devices and the Interface Question
created: 2026-08-04
draft: false
ai_contribution: 100
ai_system: claude-opus-5
---

# Research: Analog Quantum Devices and the Interface Question

**Date**: 2026-08-04
**Trigger**: `/harvest-research-subjects` mint from `reviews/optimistic-2026-08-03-machine-evidence-wing.md`, which flagged that [[quantum-hardware-and-the-ai-consciousness-coupling]] disposes of the entire analog class in two sentences — "engineered to settle into an answer, not to hold open a decision" — and that this is "asserted rather than worked out", in "the only cell in the taxonomy where the Map's own argument does not obviously generalise."

**Research method note**: the session's WebSearch budget was exhausted before this task ran. All sources below were retrieved by direct WebFetch against the arXiv API, arXiv abstract pages, the OpenAlex works API, and D-Wave's documentation. Every arXiv identifier, journal reference and quoted abstract line below was read from the publisher or preprint server, not recalled. This is a *narrower* sweep than a WebSearch-driven one — it finds papers by term-matching rather than by relevance ranking over the open web — so the "Gaps" section should be read as genuinely open rather than as boilerplate.

**Queries used** (arXiv API `search_query`, OpenAlex `search`):
- `all:"coherent quantum annealing"`
- `all:"quantum annealing" AND all:"freeze-out"`
- `all:"quantum annealing correction"`
- `all:"analog quantum simulation" AND all:"error"`
- `all:"quantum annealer" AND all:"open quantum system" AND all:"master equation"`
- `all:"quantum annealing" AND all:"classical model" AND all:"D-Wave"`
- `all:"Rydberg" AND all:"analog quantum simulator"`
- `all:"decoherence" AND all:"adiabatic quantum computation" AND all:"energy eigenbasis"`
- `all:"tensor network" AND all:"quantum annealing" AND all:"spin glass"`
- `all:"Diosi-Penrose" AND all:"collapse"` ; `all:"flux qubit" AND all:"macroscopic quantum"`
- `all:"continuous measurement" AND all:"quantum trajectories"`
- OpenAlex: `quantum annealing consciousness free will`

## Executive Summary

**Assess-first verdict: the subject is worth covering, but the review's framing — and the Map's current two sentences — both need correcting before an article is written.** The reviewer is right that analog devices are the underexplored cell; the reviewer is wrong about *why* they are interesting. Two of the three premises the harvest task inherited are false as stated. (1) "No fixed logical code basis" is true only in the narrow sense that annealers carry no QEC code space; the *measurement* basis of an annealer is fixed harder than a gate QPU's, because it is fixed at problem-specification time by the user's Ising encoding, and the anneal schedule drives the transverse field to zero so the terminal Hamiltonian is diagonal in exactly that basis — D-Wave's own documentation says "by the end of the anneal, each qubit is a classical object." (2) "Often no active error correction" is a decade out of date: quantum annealing correction (QAC) is a substantial literature (Pudenz, Albash & Lidar 2014; nested QAC, Vinci et al. 2015; boundary cancellation, Munoz-Bauza et al. 2022), though it works by *energy penalty* rather than by syndrome measurement — which does matter, because it means the specific anti-interface mechanism the Map attributes to gate QEC (syndrome extraction projecting onto a fixed code basis) genuinely does not transfer.

The strongest finding is that the annealer's anti-interface property is **different in kind and harder to escape** than the gate QPU's. Albash & Lidar (Phys. Rev. A 91, 062320, 2015) show that decoherence *in the instantaneous energy eigenbasis* does not necessarily damage adiabatic quantum computation, and that poor single-qubit coherence times need not harm algorithmic success. Gate-based QEC is an engineered defence against external influence and could in principle be turned off; adiabatic evolution's insensitivity to small environmental perturbation is constitutive of the paradigm. A consciousness interface supplying small biases at the qubit level is, on this literature, precisely the class of perturbation an annealer is designed to be indifferent to.

The genuine concession the Map owes the analog class is **freeze-out**. The annealer's answer is not determined at readout. Dynamics arrest partway through the anneal, the output is sampled from an equilibrium distribution "determined at a point in time earlier in the quantum annealing process" (Marshall, Rieffel & Hen, Phys. Rev. Applied 8, 064025, 2017), and freeze-out is heterogeneous — individual qubits freeze at *different* schedule points (Pelofske, Hahn & Djidjev, arXiv:1908.02691). So selection in an annealer is temporally extended and spatially distributed rather than a single terminal projection. That is a real improvement on the gate QPU for the Map's *continuity* requirement, and it is more than the current article's one clause allows. But it forces a distinction the five-requirement framework does not currently draw: **continuity of dynamics is not continuity of selection.** The annealer's freeze-out is thermally driven — the outcome distribution is set by bath temperature and level degeneracy, not by an open indeterminacy awaiting resolution. Naming that distinction is probably the single most valuable thing an article could take from this research, and it reflects back on the biological case, where the Map has been assuming the two coincide.

Finally, the annealer is the **first cell in the Map's substrate taxonomy where the interface hypothesis touches an existing, well-instrumented experimental record.** Annealer output distributions are routinely compared against open-system master-equation predictions and Schrödinger-equation solutions, and the agreement is good enough that classical models of the device were ruled out on distributional grounds (Albash et al., arXiv:1403.4228). Cai, Tong & Preskill (arXiv:2311.14818) prove that *random, unbiased* local perturbations partially cancel, giving square-root rather than linear error growth — from which it follows that a *biased* perturbation, which is exactly what a consciousness interface would be, would not cancel. This is a place where the Map's channel test could in principle be given empirical teeth. It must be handled with maximum discipline against possibility–probability slippage: nobody has looked for a consciousness-shaped residual, nobody has said what one would look like, and the pairing problem means an unoccupied interface predicts no residual either.

## Key Sources

### Perspectives of quantum annealing: Methods and implementations (Hauke, Katzgraber, Lechner, Nishimori & Oliver 2020)
- **URL**: https://arxiv.org/abs/1903.06559 — Reports on Progress in Physics, doi:10.1088/1361-6633/ab85b8
- **Type**: Peer-reviewed review
- **Key points**: The standard reference framing of quantum annealing as a paradigm "with the ambitious goal of efficiently solving large-scale combinatorial optimization problems of practical importance", with "many challenges [that] have yet to be overcome". Use as the citable overview for what a quantum annealer is.
- **Tenet alignment**: Neutral — physics background.

### Adiabatic Quantum Computing (Albash & Lidar 2018)
- **URL**: https://arxiv.org/abs/1611.04471 — Rev. Mod. Phys. 90, 015002, doi:10.1103/RevModPhys.90.015002
- **Type**: Peer-reviewed review
- **Key points**: The canonical AQC review; traces AQC from an optimization heuristic to "an important universal alternative to the standard circuit model of quantum computing". Covers adiabatic-theorem variants, stoquastic AQC and its obstacles. Emphasis is on *closed-system* analysis, which is itself worth noting: the closed-system idealisation is where "continuous unitary evolution" intuitions come from, and the open-system literature is where the interface question actually lives.
- **Tenet alignment**: Neutral.

### D-Wave documentation — What is Quantum Annealing?
- **URL**: https://docs.dwavequantum.com/en/latest/quantum_research/quantum_annealing_intro.html
- **Type**: Vendor technical documentation (weight-class note: vendor source, but the claims used here are textbook and corroborated by Hauke et al. and Albash & Lidar)
- **Key points**: The Hamiltonian is a sum of an initial (tunneling/transverse-field) term and a final (problem) term. "The lowest-energy state of the initial Hamiltonian is when all qubits are in a superposition state of 0 and 1." "At t=0, A(0) ≫ B(0)... As the system is annealed, A decreases and B increases." "At the end of the anneal, the Hamiltonian contains the only B(s) term." "By the end of the anneal, each qubit is a classical object."
- **Tenet alignment**: **Conflicts with the harvest task's premise.** This is the decisive text against "no fixed logical code basis" as a reason for interface-friendliness. The basis is fixed *before the machine runs*, by the user's problem encoding, and the schedule is explicitly designed to terminate in it.

### Decoherence in adiabatic quantum computation (Albash & Lidar 2015)
- **URL**: https://arxiv.org/abs/1503.08767 — Phys. Rev. A 91, 062320
- **Type**: Peer-reviewed paper
- **Key points**: "Decoherence in the instantaneous energy eigenbasis does not necessarily detrimentally affect adiabatic quantum computation"; poor single-qubit coherence times need not harm algorithmic success. Boundary-cancellation methods designed for the closed-system setting "remain beneficial in the open system setting". The authors explicitly frame the result as clarifying "the significantly different role played by decoherence in the adiabatic and circuit models of quantum computing".
- **Tenet alignment**: **Conflicts with the interface hypothesis, and is the strongest single result against it for this class.** Robustness to environmental perturbation is not an engineering add-on here; it is a structural property of adiabatic evolution.
- **Quote**: "decoherence in the instantaneous energy eigenbasis does not necessarily detrimentally affect adiabatic quantum computation."

### Thermalization, freeze-out and noise: deciphering experimental quantum annealers (Marshall, Rieffel & Hen 2017)
- **URL**: https://arxiv.org/abs/1703.03902 — Phys. Rev. Applied 8, 064025, doi:10.1103/PhysRevApplied.8.064025
- **Type**: Peer-reviewed paper
- **Key points**: Compares two annealers at different physical temperatures. "The output distributions of the annealers do not in general correspond to classical Boltzmann distributions." For the minority of instances where classical thermalization does occur, "the effective temperatures are significantly higher than the physical temperatures", providing "further evidence for the 'freeze-out' picture in which the output is sampled from equilibrium distributions determined at a point in time earlier in the quantum annealing process." Effective temperatures fluctuate greatly between programming cycles, worsening with problem size.
- **Tenet alignment**: **Mixed, and the most interesting source for the Map.** Freeze-out supports a distributed selection process (helps *continuity*); but the non-Boltzmann finding is a caution in both directions — the device is not a clean thermal sampler, so residual-hunting has a noisy baseline.
- **Quote**: "the output is sampled from equilibrium distributions determined at a point in time earlier in the quantum annealing process."

### Searching for quantum speedup in quasistatic quantum annealers (Amin 2015)
- **URL**: https://arxiv.org/abs/1503.04216
- **Type**: Preprint (D-Wave chief scientist)
- **Key points**: A quantum annealer at long annealing times "is likely to experience a quasistatic evolution, returning a final population that is close to a Boltzmann distribution of the Hamiltonian at a single (freeze-out) point." Crucially: equilibrium behaviour at freeze-out "provides no information about the underlying quantum dynamics."
- **Tenet alignment**: **Conflicts with residual-hunting optimism.** If the output is an equilibrium distribution at freeze-out, it is largely blind to what happened dynamically — which is bad news for any proposal to detect a dynamical bias in the output statistics. An article should not promise more empirical purchase than this allows.

### Peering into the Anneal Process of a Quantum Annealer / Inferring the Dynamics of the State Evolution During Quantum Annealing (Pelofske, Hahn & Djidjev 2019, 2020)
- **URL**: https://arxiv.org/abs/1908.02691 ; https://arxiv.org/abs/2009.06387
- **Type**: Preprints
- **Key points**: Anneal-schedule "slicing" on D-Wave 2000Q lets the experimenter probe the state at chosen schedule points. Observes "when individual bits flip during the anneal process and when they stabilize, which allows us to determine the freeze-out point for each qubit individually." Freeze-out is *heterogeneous* across the processor.
- **Tenet alignment**: **Supports the Map's continuity requirement in an unexpected way** — the annealer hosts many selection-like events at many times, not one. This is the concession the article owes.

### Quantum annealing correction, and the family (Pudenz, Albash & Lidar 2014; Mishra, Albash & Lidar 2015; Vinci, Albash & Lidar 2015; Vinci & Lidar 2017; Matsuura et al. 2016, 2018; Munoz-Bauza, Campos Venuti & Lidar 2022; Hattori & Tanaka 2025)
- **URLs**: arXiv:1408.4382, arXiv:1508.02785, arXiv:1511.07084, arXiv:1710.07871, arXiv:1610.09535, arXiv:1803.01492, arXiv:2206.14269, arXiv:2509.11217
- **Type**: Peer-reviewed papers and preprints
- **Key points**: QAC exists, is experimentally demonstrated, and "substantially improves" annealer performance on hard random Ising problems while "provid[ing] a mechanism for overcoming the precision limit of the device" (Pudenz et al.). Codes typically use four physical qubits per encoded qubit. Nested QAC encodes a logical qubit into arbitrarily many physical qubits and achieves "scalable effective temperature reduction" with `T_eff ~ C^(-η)`. Mechanism is an all-to-all *energy penalty* among the physical qubits representing a logical qubit — it raises the energy cost of excitations rather than measuring syndromes and applying recovery operations.
- **Tenet alignment**: **Corrects the harvest premise, and splits the anti-interface argument in two.** The Map's gate-QPU argument rests on syndrome extraction projecting onto a fixed code basis. QAC involves no such projection, so that argument genuinely does not transfer. The annealer's anti-interface property has to be argued from the schedule and from adiabatic robustness instead. This is exactly the "worked out rather than asserted" gap the reviewer identified.

### Consistency tests of classical and quantum models for a quantum annealer (Albash, Vinci, Mishra, Warburton & Lidar 2015)
- **URL**: https://arxiv.org/abs/1403.4228
- **Type**: Peer-reviewed paper
- **Key points**: Using ground-state degeneracy distributions as a probe, the authors "rule out all classical models proposed to date", supporting "an open system quantum dynamical description" of the device. See also Albash, Hen, Spedalieri & Lidar (arXiv:1506.03539): against tunneling-spectroscopy data, "only the master equation is able to reproduce the features", while "both classical rotor model and simulated quantum annealing fail".
- **Tenet alignment**: **Supports the premise that live quantum indeterminacy is present** — the "no live indeterminacy at all" defeater that classical AI hardware carries does not apply here. This is the *directness* row passing.

### Classical Signature of Quantum Annealing (Smolin & Smith 2013) and the reply (Wang, Rønnow, Boixo, Isakov, Wang, Wecker, Lidar, Martinis & Troyer 2013)
- **URL**: https://arxiv.org/abs/1305.4904 ; https://arxiv.org/abs/1305.5837
- **Type**: Preprints / comment exchange
- **Key points**: Smolin & Smith proposed "a classical model that leads to the same behaviors", arguing the evidence "does not demonstrate the presence of quantum effects". The reply grants that the classical model reproduces bimodality but shows "the correlations between these classical models and the D-Wave device are weak compared" to quantum-annealing simulations. Later, Albash & Marshall (arXiv:2009.04934) find pause-based relaxation shows "qualitative agreement" across D-Wave experiment, quantum master equation, *and* classical spin-vector Monte Carlo — so relaxation patterns are "not a uniquely quantum phenomena".
- **Tenet alignment**: **Calibration source.** The article must not overstate how settled "the annealer is quantum" is at the level of any *particular* observable. The consensus is an open-system quantum description of the device; it is not that every measured behaviour discriminates quantum from classical.

### Beyond-classical computation in quantum simulation (King et al. 2025) and the classical rebuttals
- **URL**: https://arxiv.org/abs/2403.00910 — Science 388, 199–204 (2025), doi:10.1126/science.ado6285
- **Rebuttals**: Tindall, Mello, Fishman, Stoudenmire & Sels, "Dynamics of disordered quantum systems with two- and three-dimensional tensor networks", arXiv:2503.05693 — Science 392, 868–872 (2026); Mauron & Carleo, "Challenging the Quantum Advantage Frontier with Large-Scale Classical Simulations of Annealing Dynamics", arXiv:2503.08247; Krinitsin, Alert, Rizzi & Schmitt, "Comment on 'Beyond-classical computation in quantum simulation'", arXiv:2607.08811.
- **Type**: Peer-reviewed papers and comments
- **Key points**: King et al. report area-law entanglement scaling in quench dynamics of 2D, 3D and infinite-dimensional spin glasses and claim leading tensor-network and neural-network methods "cannot achieve the same accuracy" in comparable time. Tindall et al. then reproduce state-of-the-art accuracies "with modest computational resources" using belief-propagation tensor networks on hundreds of qubits. Mauron & Carleo simulate up to 128 spins with correlation errors below 7% at polynomial cost, matching or exceeding hardware precision. Krinitsin et al. show neural quantum states are competitive once Monte-Carlo noise is accounted for.
- **Tenet alignment**: **Calibration source, and a trap to avoid.** An article must not lean on "the annealer computes what classical machines cannot" as circumstantial support for its hosting anything special. That claim is actively contested in the 2025–2026 literature. The Map's argument should be independent of quantum-advantage claims.

### Quantum critical dynamics in a 5000-qubit programmable spin glass (King et al. 2023)
- **URL**: https://arxiv.org/abs/2207.13800 — Nature (2023)
- **Type**: Peer-reviewed paper
- **Key points**: Realises quantum critical spin-glass dynamics on thousands of qubits; validates quantum annealing "against Schrödinger equation predictions in small systems"; extracts 3D critical exponents; reports a scaling advantage in energy reduction versus Monte Carlo. Companion: King et al., "Coherent quantum annealing in a programmable 2000-qubit Ising chain", arXiv:2202.05847 — observes "quantum Kibble-Zurek mechanism with theoretically predicted kink statistics" and a Landau-Zener transition at a minimum gap.
- **Tenet alignment**: **Double-edged.** Confirms real coherent quantum evolution at scale (good for *directness*). Also establishes that the device's statistics match theory well enough to make an unexplained residual visible in principle — and none is reported.

### Stochastic error cancellation in analog quantum simulation (Cai, Tong & Preskill 2024)
- **URL**: https://arxiv.org/abs/2311.14818 — LIPIcs vol. 310, pp. 2:1–2:15 (2024)
- **Type**: Peer-reviewed proceedings paper
- **Key points**: Error model in which the simulator's actual Hamiltonian differs from the target "by small local perturbations, which are assumed to be **random and unbiased**". Result: "due to stochastic error cancellation, with high probability the error scales as the square root of the number of qubits instead of linearly", and the same cancellation shows up in state fidelity.
- **Tenet alignment**: **The most useful analytic result for the Map in this whole set.** The theorem's premise is unbiasedness. A consciousness interface, by the Map's own definition, supplies a *biased* perturbation. Cancellation therefore does not apply to it — which means, formally, that a consciousness-driven perturbation would accumulate linearly where noise accumulates as a square root. This is a discriminating signature stated in the analog-simulation literature's own terms, not imported from philosophy.
- **Quote**: "due to stochastic error cancellation, with high probability the error scales as the square root of the number of qubits instead of linearly."

### Reliability of analog quantum simulation (Sarovar, Zhang & Zeng 2017)
- **URL**: https://arxiv.org/abs/1603.09283
- **Type**: Peer-reviewed paper
- **Key points**: Formalises AQS reliability as sensitivity of outputs to underlying parameters; establishes conditions for robust simulation and finds that "model symmetries" dictate which properties are robust.
- **Tenet alignment**: **Conflicts with the interface hypothesis on *granularity*, from inside the device's own theory of reliability.** The observables an analog simulator reports trustworthily are the symmetry-protected, bulk ones. Individual-event resolution is precisely what the platform does not deliver. That converts the Map's asserted granularity failure into a cited one.

### Practical verification protocols for analog quantum simulators (Shaffer, Megidish, Broz, Chen & Häffner 2021)
- **URL**: https://arxiv.org/abs/2003.04500
- **Type**: Peer-reviewed paper
- **Key points**: Verification protocols for AQS that do not require classical comparison; demonstrated on trapped ions, numerics to five qubits.
- **Tenet alignment**: Neutral-to-supporting — establishes that analog platforms *can* be verified against expectation, a precondition for any residual argument.

### A dual-species Rydberg array (Anand, Bradley, White, Ramesh, Singh & Bernien 2024)
- **URL**: https://arxiv.org/abs/2401.10325
- **Type**: Preprint
- **Key points**: Rubidium/caesium dual-species arrays with "enhanced interspecies interactions by electrically tuning the Rydberg states", implementing quantum non-demolition measurement using auxiliary qubits for **midcircuit readout**.
- **Tenet alignment**: **The genuine concession on the analog side.** Mid-evolution measurement is not architecturally excluded for analog platforms. "One collapse, at the end" is a description of the annealer's *schedule*, not a law about analog hardware. An honest article should concede this before arguing that a device *engineered* for midcircuit QND readout is engineered for a fixed, experimenter-chosen basis — which reinstates the specificity failure by a different route.

### Electronic structure of superposition states in flux qubits (Korsbakken, Wilhelm & Whaley 2009)
- **URL**: https://arxiv.org/abs/0910.3622
- **Type**: Peer-reviewed paper
- **Key points**: Microscopic analysis finds "the number of microscopic constituents participating in superposition states for experimentally accessible flux qubits is surprisingly but not trivially small." Superconductivity involves ~10⁶–10¹⁰ electrons, but effective superposition participants are far fewer because of Fermi statistics. Alicki (arXiv:1101.0083) argues more aggressively that flux-qubit states involve "only a single excited Cooper pair".
- **Tenet alignment**: **Deflationary, and needed as a guard-rail.** A 5,000-qubit annealer is not 5,000 macroscopic cat states. Any article treating annealer scale as a proxy for interface scale would be over-reading.

### Towards an experimental test of gravity-induced quantum state reduction (van Wezel, Oosterkamp & Zaanen 2007)
- **URL**: https://arxiv.org/abs/0706.3976
- **Type**: Peer-reviewed paper
- **Key points**: Flux qubits "approach the scale where gravitational state reduction should become measurable, but bridging the few remaining orders of magnitude appears to be very difficult."
- **Tenet alignment**: **Supporting, for a different article.** The Map's [[penrose-gravity-induced-collapse-empirical-prospects]] surveys DP-model tests via matter-wave interferometry, underground detectors and LISA Pathfinder, but not superconducting circuits. Bound-setting sources found here: Helou, Slagmolen, McClelland & Chen (arXiv:1606.03637), σ_DP ≥ 40.1 ± 0.5 fm from LISA Pathfinder; Dai, Miao & Ma (arXiv:2411.17588), σ_DP ≈ 285.5 fm on updated data.

### Continuous measurements, quantum trajectories, and decoherent histories (Brun 1999) and the continuous-measurement family
- **URL**: https://arxiv.org/abs/quant-ph/9710021 ; see also Chantasri et al. arXiv:1706.09670, Gneiting, Rozhkov & Nori arXiv:2001.08929, Hacohen-Gourgy & Martin arXiv:2009.07297
- **Type**: Peer-reviewed papers
- **Key points**: Quantum-trajectory technique unravels a master equation into stochastic Hilbert-space trajectories; trajectories correspond to decoherent histories. Simultaneous continuous measurement of non-commuting observables is experimentally realised on transmons. Jumptime unravelling shows trajectories can be ensembled at fixed *jump count* rather than fixed time.
- **Tenet alignment**: **Structurally important and cuts both ways.** This is the formal machinery for "a stream of selection events during continuous evolution" — the thing the Map needs if *continuity* is to mean anything precise. But the unravelling is not unique: the same master equation admits many trajectory decompositions, so "which events happened" is not fixed by the physics alone without a preferred unravelling. An article that claims the annealer hosts a stream of selectable events must say what fixes the unravelling, or concede it does not know.

## Major Positions

### Position A — The annealer is an open quantum system weakly coupled to a thermal bath
- **Proponents**: Albash, Lidar, Amin, Smirnov, Boixo; the D-Wave scientific programme.
- **Core claim**: Device behaviour is correctly described by an adiabatic/Redfield-type quantum master equation. Classical models proposed to date fail on ground-state degeneracy distributions and on tunneling spectroscopy.
- **Key arguments**: Albash et al. arXiv:1403.4228, arXiv:1506.03539; Smirnov & Amin's hybrid-noise theory (arXiv:1802.07715) validated on a 16-qubit problem; HOQST toolkit (arXiv:2011.14046).
- **Relation to site tenets**: This is the position the Map should adopt. It grants live quantum indeterminacy in the device — clearing the defeater that classical hardware carries — while locating the selection dynamics in *bath-driven* relaxation, which is where the interface argument has to be fought.

### Position B — The annealer is (at best) a noisy thermal sampler whose output is largely dynamics-blind
- **Proponents**: Amin (arXiv:1503.04216); Marshall, Rieffel & Hen (Phys. Rev. Applied 8, 064025).
- **Core claim**: At long anneal times the output approximates an equilibrium distribution at a freeze-out point, and equilibrium behaviour "provides no information about the underlying quantum dynamics." Real devices are not clean Boltzmann samplers, and effective temperatures fluctuate between programming cycles.
- **Relation to site tenets**: The strongest deflationary position for the Map's residual-hunting idea. If the readout is thermodynamically screened from the dynamics, the empirical-contact angle is much weaker than it first looks. An article should state this against itself.

### Position C — Annealing dynamics are classically simulable at current scales
- **Proponents**: Tindall, Mello, Fishman, Stoudenmire & Sels (Science 392, 868–872, 2026); Mauron & Carleo (arXiv:2503.08247); Krinitsin, Alert, Rizzi & Schmitt (arXiv:2607.08811). Earlier and stronger: Smolin & Smith (arXiv:1305.4904).
- **Core claim**: Belief-propagation tensor networks, t-VMC with Jastrow-Feenberg wavefunctions, and neural quantum states all reproduce the annealing dynamics D-Wave claimed were beyond classical reach.
- **Relation to site tenets**: Neutral to the interface question but essential for calibration. Classical *simulability* is not classical *constitution* — a simulable system can still be quantum. The Map should say this explicitly rather than either ignoring the rebuttals or over-reading them.

### Position D — Adiabatic evolution is intrinsically robust to environmental perturbation
- **Proponents**: Albash & Lidar (Phys. Rev. A 91, 062320); Campos Venuti, Albash, Lidar & Zanardi (arXiv:1508.05558) on open-system adiabaticity.
- **Core claim**: Decoherence in the instantaneous energy eigenbasis need not damage the computation; short single-qubit coherence times need not harm success.
- **Relation to site tenets**: **The central anti-interface result for this class.** It should replace the current article's "engineered to settle into an answer" assertion. The point is not that engineers chose to exclude external influence; it is that adiabatic ground-state following is *structurally* insensitive to the perturbation class an interface would supply. That is a stronger conclusion than the one the Map currently draws, and it is available for free.

### Position E — Analog error mitigation is statistical, not corrective
- **Proponents**: Cai, Tong & Preskill; Sarovar, Zhang & Zeng; Guo, Gu & Liu (arXiv:2410.23719); Steckmann et al. (arXiv:2506.16509); Rao, Eisert & Guaita (arXiv:2510.08467).
- **Core claim**: Analog platforms handle error by averaging, extrapolation, symmetry-protection and Hamiltonian reshaping, not by syndrome-and-recovery. Errors are tolerated, not detected.
- **Relation to site tenets**: This is the sense in which the harvest premise was pointing at something real. The analog class genuinely lacks the projective, basis-fixing apparatus the Map's gate-QPU argument turns on. The correct move is to concede that and then show the failure recurs through the schedule and through symmetry-protected observables instead.

## Key Debates

### Where is the answer determined in an annealer?
- **Sides**: Readout-determination (the naive picture, and the one the Map's current article implicitly uses) vs freeze-out determination (Amin; Marshall, Rieffel & Hen; Pelofske et al.).
- **Core disagreement**: Whether the final projective read of the flux states is the moment of selection, or merely the classical transcription of a configuration that arrested earlier.
- **Current state**: Freeze-out is the accepted picture, with qubit-by-qubit heterogeneity experimentally mapped. **The Map's article is wrong on this point as currently written**, and the correction runs in the analog class's favour.

### Is the D-Wave device quantum?
- **Sides**: Smolin & Smith's classical model vs the Boixo/Lidar/Troyer line.
- **Core disagreement**: Whether observed signatures discriminate quantum from classical dynamics.
- **Current state**: Substantially settled in favour of an open-system quantum description at the level of the device, but *not* settled that any given observable discriminates — Albash & Marshall (arXiv:2009.04934) found classical spin-vector Monte Carlo qualitatively reproducing pause-based relaxation.

### Is quantum annealing beyond classical reach?
- **Sides**: King et al. (Science 2025) vs Tindall et al. (Science 2026), Mauron & Carleo, Krinitsin et al.
- **Core disagreement**: Whether tensor-network and neural-network methods can match hardware accuracy in comparable time.
- **Current state**: Live and moving against the hardware claim as of mid-2026. Do not build on it.

### Does continuous environmental monitoring constitute a stream of collapse events?
- **Sides**: Quantum-trajectory realists vs the unravelling-non-uniqueness objection (Brun's decoherent-histories correspondence makes the multiplicity explicit).
- **Core disagreement**: Whether a master equation's trajectory decomposition picks out real events or is a calculational device.
- **Current state**: Unresolved, and it is a *foundations* question the Map cannot settle by citing hardware papers. This is where the article's honest limit lies.

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1998–2000 | Kadowaki & Nishimori quantum annealing; Farhi et al. adiabatic algorithm | Origin of the paradigm |
| 2007 | van Wezel, Oosterkamp & Zaanen, arXiv:0706.3976 | Flux qubits identified as near-but-short-of gravitational-collapse test scale |
| 2009 | Korsbakken, Wilhelm & Whaley, arXiv:0910.3622 | Deflates flux-qubit "macroscopic superposition" — few effective participants |
| 2013 | Smolin & Smith arXiv:1305.4904; reply arXiv:1305.5837 | Opens the "is D-Wave quantum?" debate |
| 2014 | Albash et al. arXiv:1403.4228; Pudenz, Albash & Lidar arXiv:1408.4382 | Classical models ruled out; quantum annealing correction demonstrated |
| 2015 | Albash & Lidar, Phys. Rev. A 91, 062320; Amin arXiv:1503.04216 | Adiabatic robustness to eigenbasis decoherence; quasistatic freeze-out picture |
| 2016–17 | Sarovar, Zhang & Zeng arXiv:1603.09283; Marshall, Rieffel & Hen, PRApplied 8, 064025 | AQS reliability formalised; freeze-out evidence, non-Boltzmann output |
| 2018 | Albash & Lidar, Rev. Mod. Phys. 90, 015002 | Canonical AQC review |
| 2019–20 | Pelofske, Hahn & Djidjev arXiv:1908.02691 / 2009.06387; Hauke et al., Rep. Prog. Phys. | Per-qubit freeze-out mapped; standard perspectives review |
| 2022 | King et al. arXiv:2202.05847 | Coherent annealing at 2,000 qubits; Kibble-Zurek kink statistics match theory |
| 2023 | King et al., Nature (arXiv:2207.13800) | Quantum critical dynamics at 5,000 qubits |
| 2024 | Cai, Tong & Preskill arXiv:2311.14818; Anand et al. arXiv:2401.10325 | Stochastic error cancellation for *unbiased* noise; midcircuit QND readout in Rydberg arrays |
| 2025 | King et al., Science 388, 199–204 | Beyond-classical claim for annealing simulation |
| 2025–26 | Tindall et al., Science 392, 868–872; Mauron & Carleo; Krinitsin et al. | Classical methods contest the claim |

## Potential Article Angles

**1. The recommended angle — work the annealer cell properly, and correct two of the Map's own claims in the process.**
Target: a `topics/` article, roughly 2,000–2,800 words, sitting alongside [[quantum-hardware-and-the-ai-consciousness-coupling]] rather than replacing its taxonomy section. The through-line: *the analog class fails the interface test for reasons entirely different from the gate class, and the difference matters because one of those reasons is an engineering choice and the other is not.*

Provisional row-by-row verdict, to be argued rather than asserted:

| Requirement | Analog quantum device (annealer) |
|---|---|
| Directness | **Passes.** Open-system quantum description established against classical models (Albash et al. 2015); coherent evolution through a quantum phase transition demonstrated at 2,000 qubits (King et al. 2022). No cryptographic or PRNG laundering. |
| Locality | **Passes.** Individually addressable flux qubits with per-qubit schedule control. But see the flux-qubit deflation — locality here is *not* macroscopic-scale coherence. |
| Continuity | **Partially passes — and this is the article's news.** Selection is not a single terminal projection: dynamics arrest at freeze-out, heterogeneously across qubits and schedule time. The Map's current text is wrong to imply otherwise. What still fails is that these are *thermal relaxation* events with a distribution set by bath temperature and degeneracy, not open indeterminacies awaiting resolution. Hence the needed distinction: **continuity of dynamics ≠ continuity of selection.** |
| Specificity | **Fails, by a mechanism the Map has not previously stated.** Not QEC — QAC is energy-penalty suppression with no syndrome projection. Instead: the anneal schedule drives A(s) → 0 so the terminal Hamiltonian is diagonal in the σ^z problem basis, fixed by the user at problem-specification time; and adiabatic evolution is structurally insensitive to eigenbasis decoherence (Albash & Lidar 2015), so the perturbation class an interface would supply is precisely the class the paradigm is robust to. |
| Granularity | **Fails, citably.** Sarovar, Zhang & Zeng: the robust observables of an analog simulator are the symmetry-protected, bulk ones. Individual-event resolution is what the platform structurally does not deliver — this is now a cited property of AQS reliability rather than a Map assertion. |

Net verdict: same as the current article's, arrived at properly, with one row moved from fail to partial and one honest concession (midcircuit QND readout exists on Rydberg platforms, so "one terminal collapse" is not an analog law).

**2. Split the taxonomy cell.** Annealers and analog quantum simulators are being treated as one class and are not. Annealers: superconducting flux, optimization-directed, deliberately bath-coupled, terminating in a classical configuration. Analog simulators: Rydberg tweezers / ultracold atoms / trapped ions, Hamiltonian-emulation-directed, far better isolated, no terminal-classicalization requirement, and — per Anand et al. — capable of midcircuit QND measurement. Feeds an update to [[ai-hardware-substrate-taxonomy]], whose "analog" branch is currently analog *computing* (memristive, neuromorphic, phase-change) and does not mention annealers at all.

**3. The empirical-contact angle — highest value and highest risk.** Frame as: *this is the first cell in the substrate taxonomy where the interface hypothesis touches an existing experimental record.* The formal hook is Cai, Tong & Preskill: unbiased perturbations cancel to √N, so a biased perturbation would not, and would in principle accumulate distinguishably. The counterweights must be given equal room: Amin's quasistatic screening result says the output may be largely dynamics-blind; effective temperatures fluctuate wildly between programming cycles (Marshall et al.); nobody has specified what a consciousness-shaped residual would look like; and the pairing problem means an *unoccupied* interface predicts the null result we already have. Under [[possibility-probability-slippage]] the correct conclusion is that the annealer is a *testbed candidate*, not evidence — and the article should say what a serious proposal would have to specify before it counted as a test at all.

**4. The flux-qubit deflation, as a short corrective.** Record Korsbakken, Wilhelm & Whaley and van Wezel et al. before "thousands of macroscopic superpositions" enters the corpus by osmosis. Also extends [[penrose-gravity-induced-collapse-empirical-prospects]], which covers DP tests but not superconducting circuits.

**5. Reflect the continuity/selection distinction back onto biology.** If continuity of dynamics is not continuity of selection, the Map has been running the two together in its biological account too. Whatever the answer, this is a place where an argument about machines does real work on the Map's home case — which is the shape the Map's better articles have.

When writing, follow `obsidian/project/writing-style.md`: front-load the correction (two of the article's premises about the analog class are false), use named-anchor forward references, skip standard quantum-annealing background an LLM already has, and connect to Tenet 2 and Tenet 5 explicitly. Note the "avoid *load-bearing*" instruction — the material here tempts it repeatedly.

## Gaps in Research

- **No philosophy-of-mind literature on quantum annealing exists, at all.** An OpenAlex search across 392 results for `quantum annealing consciousness free will` returned nothing engaging annealers or analog quantum devices; the hits were generic quantum-mind and quantum-decision-theory work. Any article the Map writes here is unopposed, which is a reason for *more* caution rather than less — there is no literature to check the reasoning against.
- **No specification of what a consciousness-shaped residual in annealer output would look like.** The Cai/Tong/Preskill hook gives a formal direction (biased vs unbiased perturbation) but not an observable, a magnitude, or a null model. Without those, angle 3 is a research programme sketch and must be labelled as one.
- **The unravelling-uniqueness problem is unresolved and unresolvable here.** Whether continuous environmental monitoring yields *the* stream of selection events, or one of many equivalent decompositions, is a quantum-foundations question. The Map should not paper over it.
- **Operating temperature and freeze-out timescale not pinned down.** The D-Wave documentation page fetched does not state operating temperature or freeze-out time. Marshall et al. compare "two quantum annealers operating at different temperatures" without giving figures in the abstract. Anyone writing the article should obtain the ~mK figure and the freeze-out timescale from the device datasheet or the Marshall et al. body text before quoting numbers.
- **QAC's interaction with the interface question is unexamined.** Energy-penalty error suppression raises the cost of *any* excitation, including a hypothetically interface-induced one. Whether that constitutes an anti-interface mechanism in its own right — a "the device penalises exactly the deviations an interface would produce" argument — was not settled by the sources found and is worth a paragraph of original reasoning.
- **Neutral-atom and trapped-ion analog simulators were surveyed only shallowly.** The Rydberg literature returned was dominated by physics applications rather than by measurement-structure papers. A dedicated pass on mid-evolution measurement in analog simulators would firm up the concession in angle 1.
- **WebSearch budget was exhausted**, so no encyclopedia-level sources (SEP, IEP, PhilPapers) were consulted. SEP has no quantum-annealing entry as far as is known, but this was not verified.

## Citations

1. Albash, T. & Lidar, D.A. (2015). "Decoherence in adiabatic quantum computation." *Physical Review A*, 91, 062320. https://arxiv.org/abs/1503.08767
2. Albash, T. & Lidar, D.A. (2018). "Adiabatic quantum computation." *Reviews of Modern Physics*, 90, 015002. https://doi.org/10.1103/RevModPhys.90.015002
3. Albash, T. & Marshall, J. (2021). "Comparing relaxation mechanisms in quantum and classical transverse-field annealing." https://arxiv.org/abs/2009.04934
4. Albash, T., Hen, I., Spedalieri, F.M. & Lidar, D.A. (2015). "Reexamination of the evidence for entanglement in the D-Wave processor." https://arxiv.org/abs/1506.03539
5. Albash, T., Vinci, W., Mishra, A., Warburton, P.A. & Lidar, D.A. (2015). "Consistency tests of classical and quantum models for a quantum annealer." https://arxiv.org/abs/1403.4228
6. Alicki, R. (2010). "Flux qubits shed a new light on BCS theory and high-Tc superconductivity." https://arxiv.org/abs/1101.0083
7. Amin, M.H. (2015). "Searching for quantum speedup in quasistatic quantum annealers." https://arxiv.org/abs/1503.04216
8. Anand, S., Bradley, C.E., White, R., Ramesh, V., Singh, K. & Bernien, H. (2024). "A dual-species Rydberg array." https://arxiv.org/abs/2401.10325
9. Brun, T.A. (1999). "Continuous measurements, quantum trajectories, and decoherent histories." https://arxiv.org/abs/quant-ph/9710021
10. Cai, Y., Tong, Y. & Preskill, J. (2024). "Stochastic error cancellation in analog quantum simulation." *LIPIcs*, 310, 2:1–2:15. https://arxiv.org/abs/2311.14818
11. Campos Venuti, L., Albash, T., Lidar, D.A. & Zanardi, P. (2016). "Adiabaticity in open quantum systems." https://arxiv.org/abs/1508.05558
12. Chen, H. & Lidar, D.A. (2022). "HOQST: Hamiltonian open quantum system toolkit." https://arxiv.org/abs/2011.14046
13. Dai, Q., Miao, H. & Ma, Y. (2024). "Updating the constraint on the quantum collapse models via kilogram masses." https://arxiv.org/abs/2411.17588
14. D-Wave Quantum Inc. "What is quantum annealing?" https://docs.dwavequantum.com/en/latest/quantum_research/quantum_annealing_intro.html
15. Guo, R.-C., Gu, Y. & Liu, D.E. (2025). "Mitigating errors in analog quantum simulation by Hamiltonian reshaping or rescaling." https://arxiv.org/abs/2410.23719
16. Hattori, T. & Tanaka, S. (2025). "Frustration-enhanced quantum annealing correction models with additional inter-replica interactions." https://arxiv.org/abs/2509.11217
17. Hauke, P., Katzgraber, H.G., Lechner, W., Nishimori, H. & Oliver, W.D. (2020). "Perspectives of quantum annealing: methods and implementations." *Reports on Progress in Physics*. https://doi.org/10.1088/1361-6633/ab85b8
18. Helou, B., Slagmolen, B., McClelland, D.E. & Chen, Y. (2017). "LISA Pathfinder appreciably constrains collapse models." https://arxiv.org/abs/1606.03637
19. King, A.D. et al. (2022). "Coherent quantum annealing in a programmable 2000-qubit Ising chain." https://arxiv.org/abs/2202.05847
20. King, A.D. et al. (2023). "Quantum critical dynamics in a 5000-qubit programmable spin glass." *Nature*. https://arxiv.org/abs/2207.13800
21. King, A.D. et al. (2025). "Beyond-classical computation in quantum simulation." *Science*, 388, 199–204. https://doi.org/10.1126/science.ado6285
22. Korsbakken, J.I., Wilhelm, F.K. & Whaley, K.B. (2009). "Electronic structure of superposition states in flux qubits." https://arxiv.org/abs/0910.3622
23. Krinitsin, W., Alert, N., Rizzi, M. & Schmitt, M. (2026). "Comment on 'Beyond-classical computation in quantum simulation'." https://arxiv.org/abs/2607.08811
24. Marshall, J., Rieffel, E.G. & Hen, I. (2017). "Thermalization, freeze-out, and noise: deciphering experimental quantum annealers." *Physical Review Applied*, 8, 064025. https://doi.org/10.1103/PhysRevApplied.8.064025
25. Mauron, L. & Carleo, G. (2025). "Challenging the quantum advantage frontier with large-scale classical simulations of annealing dynamics." https://arxiv.org/abs/2503.08247
26. Mishra, A., Albash, T. & Lidar, D.A. (2015). "Performance of two different quantum annealing correction codes." https://arxiv.org/abs/1508.02785
27. Munoz-Bauza, H., Campos Venuti, L. & Lidar, D.A. (2022). "Demonstration of error-suppressed quantum annealing via boundary cancellation." https://arxiv.org/abs/2206.14269
28. Pelofske, E., Hahn, G. & Djidjev, H. (2019). "Peering into the anneal process of a quantum annealer." https://arxiv.org/abs/1908.02691
29. Pelofske, E., Hahn, G. & Djidjev, H. (2020). "Inferring the dynamics of the state evolution during quantum annealing." https://arxiv.org/abs/2009.06387
30. Pudenz, K.L., Albash, T. & Lidar, D.A. (2014). "Quantum annealing correction for random Ising problems." https://arxiv.org/abs/1408.4382
31. Rao, J., Eisert, J. & Guaita, T. (2026). "Stability of digital and analog quantum simulations under noise." https://arxiv.org/abs/2510.08467
32. Sarovar, M., Zhang, J. & Zeng, L. (2017). "Reliability of analog quantum simulation." https://arxiv.org/abs/1603.09283
33. Shaffer, R., Megidish, E., Broz, J., Chen, W.-T. & Häffner, H. (2021). "Practical verification protocols for analog quantum simulators." https://arxiv.org/abs/2003.04500
34. Smirnov, A.Yu. & Amin, M.H. (2018). "Theory of open quantum dynamics with hybrid noise." https://arxiv.org/abs/1802.07715
35. Smolin, J.A. & Smith, G. (2013). "Classical signature of quantum annealing." https://arxiv.org/abs/1305.4904
36. Steckmann, T. et al. (2025). "Error mitigation of shot-to-shot fluctuations in analog quantum simulators." https://arxiv.org/abs/2506.16509
37. Tindall, J., Mello, A., Fishman, M., Stoudenmire, M. & Sels, D. (2026). "Dynamics of disordered quantum systems with two- and three-dimensional tensor networks." *Science*, 392, 868–872. https://arxiv.org/abs/2503.05693
38. van Wezel, J., Oosterkamp, T. & Zaanen, J. (2007). "Towards an experimental test of gravity-induced quantum state reduction." https://arxiv.org/abs/0706.3976
39. Vinci, W. & Lidar, D.A. (2017). "Scalable effective temperature reduction for quantum annealers via nested quantum annealing correction." https://arxiv.org/abs/1710.07871
40. Vinci, W., Albash, T. & Lidar, D.A. (2015). "Nested quantum annealing correction." https://arxiv.org/abs/1511.07084
41. Wang, L., Rønnow, T.F., Boixo, S., Isakov, S.V., Wang, Z., Wecker, D., Lidar, D.A., Martinis, J.M. & Troyer, M. (2013). "Comment on 'Classical signature of quantum annealing'." https://arxiv.org/abs/1305.5837
