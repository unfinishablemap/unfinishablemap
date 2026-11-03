---
title: "Research Notes - Zeno Confinement to a Spatial Region under Position Decoherence"
created: 2026-11-03
modified: 2026-11-03
human_modified: null
ai_modified: 2026-11-03T13:08:13+00:00
draft: false
description: "A published model of Zeno confinement to an interval under position decoherence (Bedingham & Halliwell 2014), and the first full read of Stapp's 2015 reply. The brain number stays uncomputed."
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-03
last_curated: null
recommended_action: fold
target_section: concepts
target_slug: zeno-dynamics-on-a-decohered-mixture
---

# Research: Zeno Confinement to a Spatial Region under Position Decoherence

**Date**: 2026-11-03
**Question**: Has anyone computed the window (coherence length ℓ, crossing time) that decides the Stapp–Georgiev question, for Zeno confinement to a spatial interval while position decoherence acts at the same time?

**Search queries used** (WebSearch): "Maniscalco Piilo Suominen 'Zeno and anti-Zeno effects for quantum Brownian motion' arXiv"; "'quantum Zeno dynamics' 'position decoherence' hard-wall Lindblad spatial region"; "Stapp 2015 'Reply to Georgiev' 'No-Go for Georgiev's No-Go Theorem' NeuroQuantology pdf"; "Stapp 'Georgiev' reply 'environmental decoherence does not nullify the quantum Zeno effect'"; "'quantum Zeno' brain decoherence 'coherence length' ion 'projection' timescale Stapp model calculation window"; "'quantum Zeno' brain Stapp decoherence 'Bedingham' OR 'Halliwell' spatial region escape"; "'quantum Zeno' 'dephasing' 'continuum' position measurement 'Zeno dynamics' Lindblad hard wall Dirichlet decoherence"; "quantum Zeno effect neurons ion channel decoherence time projection rate calculation Stapp Schwartz Beauregard critique numerical estimate". **OpenAlex** full-text search: "quantum Zeno brain decoherence"; "Zeno effect spatial region decoherence escape"; "quantum Zeno spatial region environmental decoherence"; "quantum Zeno spatial region decoherence neuron"; "quantum Zeno coordinate space interval brain decoherence"; "Zeno effect ion channel position decoherence projection interval". **OpenAlex citation lists**: every work citing Bedingham & Halliwell 2014 (5), Georgiev 2015 *IJMPB* (11) and Stapp 2015 (1); J.J. Halliwell's works since 2013 matching "zeno" (5). **Full texts** downloaded and converted with `pdftotext`: arXiv 1402.4365, 1306.3377, quant-ph/0602133, quant-ph/0403205, 0911.5675, 1706.06943, 1412.4741, 2012.07836; *Sci. Rep.* 8, 14887 (publisher PDF); Stapp 2015 (publisher PDF, Internet Archive capture of 2018-07-21, `neuroquantology.com/index.php/journal/article/download/851/705`). Crossref metadata checked for every DOI in the Citations list.

**Relation to prior notes.** This continues the research note `zeno-dynamics-on-a-decohered-mixture-2026-10-05`, whose "Gaps" list ends: "No source found that treats Zeno confinement to a spatial interval under simultaneous position decoherence (hard walls plus a Joos–Zeh master equation)." The page [[zeno-dynamics-on-a-decohered-mixture]] lists it as gap 1 in §What Remains Open and gives the note's scaling argument in §Coordinate Space and the Strip Width. That note's toy model, its Stapp 2000/2012 and Georgiev readings, and its Kiefer–Joos and Facchi–Pascazio material are not repeated here.

**Verification status.** Quotations marked *verbatim* were grepped, with a count of 1, in the line-joined `pdftotext` output of the file named. In the Bedingham–Halliwell and Stapp texts the extraction writes ℏ as `~` and ε as `ǫ`; quotations below restore the symbols and change nothing else. Bedingham & Halliwell 2014 is quoted from arXiv v1, the only arXiv version; its published abstract (via OpenAlex) differs in wording ("suppresses" for "kills"), so the body may differ slightly from the published version too. Caves & Milburn 1987 and Joos 1984 are **abstract only**. Sections marked *note's reading* are this note's inferences, not findings of any source.

## Executive Summary

**Yes for the form of the window, no for the brain number.** Bedingham and Halliwell (2014, *PRA* 89, 042116) treat exactly the case the Map's gap names. A particle in one dimension is projected repeatedly onto an interval while a position-decoherence (quantum Brownian motion) master equation acts, with a Lindblad operator proportional to x̂. Environment and projector therefore share the position basis. They derive the window and its timescales analytically and check them numerically, in units ℏ = m = L = 1. They never mention brains, Stapp or Georgiev, and they set no parameters for any physical system. No source found inserts brain parameters. **The brain number remains uncomputed**, which keeps the page's deliberate endpoint intact.

What their result gives the page:

1. **The window.** The hold appears as reflection from the region's edge. It "arises when the projections are sufficiently rapid that ε < ℏ/E", where E is the kinetic energy. The condition is a projection interval against the energy time.
2. **How the environment closes it.** Position decoherence closes the window by pumping up momentum fluctuations; B&H show this is the same thing as diagonalisation, seen from the other side. The Zeno effect is killed after τ = mℏ/Dε. That is the decoherence time over the "effective spatial grid size" (ℏε/m)^½ laid down by the projections.
3. **Three regimes.**
   - If ε ≫ t_loc = (mℏ/D)^½, the system is "completely classicalized before the next projection happens".
   - If ε ≪ t_loc, the hold survives for about τ ≫ t_loc.
   - In the stationary regime it persists only if ε ≪ t_fE = ℏm^⅓/(LD)^⅔.
4. **Support and correction for the page.** The short-range coherences the hold needs decohere slowly: "The corresponding decoherence time for this process is therefore very long." That supports the page's strip-width reading. Two parts of the page's own scaling argument need correcting. The relevant length is fixed by ε and m, not by the environment's ℓ. The interval length L enters t_fE, so "the interval's grain does not" matter is not borne out.

**Stapp 2015 body read for the first time on the Map.** It closes the page's gap 2. Stapp evolves brain and environment together "via the unitary Schrödinger process in the full space", shows that the first-order term in t vanishes, and concludes that the second-order term "is the dominant term for change for sufficiently small t". This answers the "environment during the interval" point in form. It states the quadratic window without giving its size. The reply also says that Georgiev's Monte Carlo supports the Zeno effect "in a context with environmental decoherence". In the arXiv preprint, however, the sentence Stapp quotes belongs to Georgiev's simulation **without** decoherence.

**Recommended action: `fold`** into `concepts/zeno-dynamics-on-a-decohered-mixture` (§strip-width, §two-regime-limited-truths, §what-remains-open). Draft passages and word costs are in [[#fold-plan|Fold Plan]] below. Secondary refine targets are listed there too.

## Key Sources

### Bedingham & Halliwell (2014), "Classical limit of the quantum Zeno effect by environmental decoherence"
- **URL**: https://arxiv.org/abs/1402.4365 (*Physical Review A* 89(4), 042116; DOI 10.1103/PhysRevA.89.042116; Crossref-confirmed)
- **Type**: Paper, read in full (arXiv v1, 45 pp.)
- **Model**: a point particle in one dimension. It is projected at intervals ε onto [−L/2, L/2] with P = f_L(x̂), and between projections it evolves under ∂ρ/∂t = (iℏ/2m)(∂²ρ/∂x² − ∂²ρ/∂y²) − (D/ℏ²)(x−y)²ρ. That is the Lindblad equation with L = (D/ℏ²)^½ x̂, which B&H describe as a particle "coupled to a thermal environment (quantum Brownian motion)", citing Caldeira–Leggett among others for the propagator. There is **no friction term**: ⟨p²⟩ grows by 2Dt between projections without bound. The sharp projector is smoothed over a width a = ℏε/mL to give a momentum cut-off.
- **Key points** (*verbatim* unless stated):
  - Coherence length and decoherence time: "When the state has quantum coherence over a lengthscale ℓ, another timescale is also important, the decoherence time, td = ℏ²/Dℓ²." Then: "The reflection process entailed in the Zeno effect involves quantum coherences over very short lengthscales and it is these that we need to suppress by decoherence. The corresponding decoherence time for this process is therefore very long."
  - The window: "The Zeno effect arises when the projections are sufficiently rapid that ε < ℏ/E. States trying to escape from the region are simply reflected from the boundary under these conditions." And: "The Zeno effect therefore exists only in the low momentum regime. It will be suppressed if there is a mechanism which pushes the momenta to larger values."
  - The grid: "Reflection occurs when the wavelength ℏ/p of the incoming packet is larger than the grid size", the grid being (ℏε/m)^½. The reflection condition "remains approximately valid for a mixed state with evolution according to a master equation" (citing their 2013 paper).
  - Diagonalisation and heating are the same mechanism: their account involves "two different but, as we showed, equivalent perspectives: density matrix diagonalization, the traditional story of emergent classicality, and large momentum fluctuations required to suppress reflection."
  - The kill time, eq. (8.5)/(11.1): τ = mℏ/Dε = t_loc²/ε. "This is the timescale on which the Zeno effect is killed from a general initial state." "This may be interpreted as the decoherence time on the lengthscale" (ℏε/m)^½, "which is the effective spatial grid size associated with the projections a time ε apart."
  - The localisation time t_loc = (mℏ/D)^½ "is independent of the initial state". "The case tloc ≪ ε is somewhat trivial. It means that, after each projection, the quantum term in Eq.(8.4) becomes negligible after time ε so the system is completely classicalized before the next projection happens." For the weaker environment, ε ≪ t_loc, "it takes longer than the localization time for the Zeno effect to be suppressed".
  - The classical regime: the projections become "gates" that "simply remove probability – there is no quantum-mechanical reflection and the dynamics is not significantly changed by taking the limit ε→0 with τ = nε fixed."
  - The stationary regime, from numerics: stationary momentum p_s = (mLD)^⅓, classical decay time λ⁻¹ = (m²L²/D)^⅓, and final energy time t_fE = mℏ/p_s² = ℏm^⅓/(LD)^⅔. They state the condition as a heuristic: "We argued that there would be no Zeno effect in that regime as long as the parameters of the model are such that the final energy time satisfies tfE ≪ ε." When instead ε ≪ t_fE, "reflection is possible in this case. This means that the Wigner function has entered its stationary regime but the regime is still a quantum one." Their Fig. 1(a) run (D = 100, ε = 0.01, t_fE > ε) confirms this: "the quantum contribution cannot be neglected".
  - Two-state model (§IV.A, H = ωσx, L ∝ σx, P = |↑⟩⟨↑|), where the Lindblad operator does *not* commute with P: "But for any non-zero D, there is always a linear decay, no matter how small ε is. Hence the presence of the environment restores the expected classical decay".
  - A general argument (§II): if histories decohere, the Zeno effect is killed. Conversely, "the presence of the Zeno effect prevents decoherence of histories".
- **Not in the paper**: any mention of brains, Stapp, Georgiev, consciousness or neurons. A case-insensitive grep for `brain|stapp|conscious|neuron|mind` returns 0, against a positive control: "Zeno" is present throughout. No physical parameter values are set.
- **Tenet alignment**: Neutral. Standard physics. It is the first source the Map has found that models the Stapp 2012 geometry (an interval in coordinate space under coordinate-basis decoherence).

### Stapp (2015), "Reply to Georgiev: No-Go for Georgiev's No-Go Theorem"
- **URL**: https://doi.org/10.14704/nq.2015.13.2.851 (*NeuroQuantology* 13(2), 190–191 per the PDF header; Crossref-confirmed, no pages in Crossref). The DOI now redirects to the journal homepage. Full text read from the publisher PDF in an Internet Archive capture (2018-07-21) of `https://www.neuroquantology.com/index.php/journal/article/download/851/705`.
- **Type**: Two-page commentary, read in full. The two-column layout breaks one quoted sentence across a column; it is marked below.
- **Key points** (*verbatim*):
  - "The Monte Carlo simulation is not a simulation of my theory. Moreover, it appears to validate, not invalidate, the Quantum Zeno Effect (QZE) in the presence of environmental decoherence." He supports this by quoting Georgiev "just below his Diagram 3 ... in a context with environmental decoherence".
  - Set-up: system I is the brain subsystem holding "the neural correlates of the possible upcoming perceptions"; system II is the environment. "The condition that the mind-chosen action P acts in the perception-related subspace I, and not on the unknowable environment, is the condition that P act as the identity operator in the subspace II." The environment acts during the interval: "The evolution of Rho(t), via the unitary Schrödinger process in the full space, induces / effects in the observable “Yes” part of rho(t), due to interactions between the subspaces I and II." (Joined across the column break.)
  - Result: the first-order term is (−it)Trace[(PHP)(PRho(0)P) − (PRho(0)P)(PHP)] = 0 by cyclicity of the trace. "Hence the second-order term is the dominant term for change for sufficiently small t. But that dominance is precisely the condition that entails the quantum Zeno effects."
  - Concession and claim: "whereas it is indeed true that environmental decoherence does progressively decrease the (originally unit) probability of the initial state, and that Process 3 cannot undo the diminishing of that probability, those two facts do not undo the QZE. For the effect of the shortening of the temporal spacing Xi to zero is, by itself, sufficient to reduce to zero the rate of the diminishing of the (originally unit) probability."
- **Check of Stapp's Georgiev quotation**: in arXiv:1412.4741 (v1, the only version), the sentence reads "In the limit ξ → 0, the electron in the quantum brain stays with probability of 1 in its initial state." It sits in §4, the Fig. 3 simulation, where "Between the projective measurements the electron state evolves coherently according to the Schrödinger equation". Georgiev sums that run up as follows: "The results show that in the absence of environmental decoherence the quantum Zeno effect indeed could be achieved". His decoherence run is Fig. 4 ("Decoherence induced breakdown of quantum Zeno effect"). So, at least in the preprint, Stapp's "in a context with environmental decoherence" misplaces the sentence. Stapp's quotation also paraphrases it ("Xi goes to 0", "stays with probability 1"). Whether the published *IJMPB* text is laid out differently was not checked.
- **Note's reading**: the proof is the standard short-time expansion applied to P ⊗ 1 on the closed brain-plus-environment system, which is the Facchi–Pascazio subspace theorem. As mathematics its ε → 0 limit is not in doubt; in B&H, too, τ → ∞ as ε → 0. Georgiev's Fig. 4 breakdown at ξ → 0 comes from a different model of the environment. He writes "we take the pointer basis to be the energy basis" (*verbatim*) and applies it as an instantaneous energy-basis projection once per decoherence time τ. That is a non-commuting environment with no short-time regime of its own, the kind for which B&H's two-state model also finds a linear leak at any ε. On this reading the two sides disagree less about Zeno theory than about how the environment behaves on timescales shorter than its own correlation time. What the proof leaves open is the size of "sufficiently small". On B&H's general formula (their eqs. 1.5–1.6, p(τ) = 1 − Nε²/t_z² with t_z = ℏ/⟨H P̄ H⟩^½), the scale is the Zeno time of the full Hamiltonian, coupling included, relative to P ⊗ 1. That is this note's application of their formula, not something Stapp or B&H state. The reply does not touch Georgiev's same-basis redundancy horn or the anti-Zeno sign.
- **Tenet alignment**: Supports Bidirectional Interaction as Stapp intends it. It is consistent with the page's "Two Regime-Limited Truths": the timing requirement is restated, not removed.

### Facchi, Tasaki, Pascazio, Nakazato, Tokuse & Lidar (2005), "Control of decoherence: Analysis and comparison of three different strategies"
- **URL**: https://arxiv.org/abs/quant-ph/0403205 (*PRA* 71, 022302; DOI 10.1103/PhysRevA.71.022302; Crossref-confirmed)
- **Type**: Paper. Abstract, §VIII and the threshold passages read.
- **Key points** (*verbatim*): "Decoherence is shown to be suppressed only if the frequency N of the measurements/pulses is large enough or if the coupling K is sufficiently strong. Otherwise, if N or K are large, but not extremely large, all these control procedures accelerate decoherence." There is a transition time τ*, with suppression for τ < τ* and enhancement for τ > τ*. τ* and 2π/K* are "not simply related to the inverse bandwidth": "they can be in general (much) shorter". And: "it is not true that repeated measurements/interruptions always lead to a suppression of decoherence".
- **Relevance**: the system is a qubit coupled to a reservoir, not a spatial interval. It bears on the non-commuting case and on [[sign-problem-for-conscious-observation]], not on gap 1. The task's description of it as "the same shape as the toy's x criterion" holds for the threshold's existence. It also adds that the threshold can lie well below the reservoir's correlation time.

### Maniscalco, Piilo & Suominen (2006), "Zeno and anti-Zeno effects for quantum Brownian motion"
- **URL**: https://arxiv.org/abs/quant-ph/0602133 (*PRL* 97, 130402; DOI 10.1103/PhysRevLett.97.130402; Crossref-confirmed)
- **Type**: Paper, read in full (4 pp., v2)
- **Key points**: a damped harmonic oscillator in a Fock state |n⟩ under repeated non-selective measurements in the energy basis, with an exact non-Markovian QBM master equation. *Verbatim*: "We demonstrate that, for high reservoir temperatures, the short time behaviour of environment induced decoherence is the ultimate responsible for the occurrence of either the Zeno or the anti-Zeno effect." The crossover is set by whether the interval-averaged diffusion coefficient ∫₀^τ Δ(t)dt/τ is below or above its Markovian value.
- **Relevance**: the closest continuous-variable lead in the task, but the projector is onto an energy eigenstate, not a spatial region. It shows that for an environment that does not commute with P, the window lies in the environment's non-Markovian short-time regime. It does not answer gap 1.

### Beau, Kiukas, Egusquiza & del Campo (2017), "Nonexponential quantum decay under environmental decoherence"
- **URL**: https://arxiv.org/abs/1706.06943 (*PRL* 119, 130401; DOI 10.1103/PhysRevLett.119.130401; Crossref-confirmed). Cites B&H 2014.
- **Type**: Paper, relevant passages read.
- **Key points** (*verbatim*): short-time deviations from exponential decay "are generally suppressed by the coupling to an environment that induces the appearance of a term linear in t". And: "While it is known that the Markovian master equation fails generally at very short-times, within the realm of its validity short-time deviations are absent."
- **Relevance (note's reading)**: this reconciles Stapp 2015 with Markovian treatments such as the page's two-state illustration and B&H's §IV.A. Stapp's closed-system expansion is quadratic at short enough t. A Markovian description of an environment that does not commute with P has no quadratic regime. The window for such couplings therefore lies below the timescale on which a Markovian description holds. For couplings that commute with P, as in B&H's main model, a Markovian treatment still has a window, set by the system's own energy time.

### Majeed & Chaudhry (2018), "The quantum Zeno and anti-Zeno effects with non-selective projective measurements"
- **URL**: https://doi.org/10.1038/s41598-018-33181-9 (*Scientific Reports* 8, 14887; Crossref-confirmed; open-access PDF read)
- **Key point** (*verbatim*): "there is a difference between using non-selective projective measurements and the usual approach of considering only selective measurements only if we go beyond the weak system-environment coupling regime in models other than the usual population decay models." (In the PDF extraction the hyphen in "system-environment" is lost; the abstract has it.)
- **Relevance**: a caution. B&H compute the selective survival probability, the probability of being found inside at every check (their eqs. 1.1, 3.3). The page's §unconditional works in Stapp's non-selective register. Whether B&H's thresholds carry over unchanged to the non-selective population was not checked.

### Bedingham & Halliwell (2013), "Suppression of quantum-mechanical reflection by environmental decoherence"
- **URL**: https://arxiv.org/abs/1306.3377 (*PRA* 88, 022128; DOI 10.1103/PhysRevA.88.022128; Crossref-confirmed). Abstract read.
- **Key point** (*verbatim*, abstract): with "Lindblad operator proportional to position (the simplest version of quantum Brownian motion)", "suppression of reflection is achieved only for environmental interaction so strong that large fluctuations in momentum are generated which blurs the distinction between incoming and reflected wave packets." It is the half-line precursor. In the finite region of the 2014 paper, the fluctuations problem is said to be harmless because they "enhance the escape".

### Facchi, Graffi & Ligabò (2010), "Classical limit of the quantum Zeno effect"
- **URL**: https://arxiv.org/abs/0911.5675 (*J. Phys. A* 43(3), 032001; DOI 10.1088/1751-8113/43/3/032001; Crossref gives 2009-12-17 online). Abstract read. Shows the Zeno effect "vanishes at all orders, when the Planck constant tends to zero". B&H's §VI uses it as the ℏ → 0 limit their environment mimics.

### Abstract-only leads from the task
- **Caves & Milburn (1987)**, *PRA* 36(12), 5543–5555, DOI 10.1103/PhysRevA.36.5543 (Crossref-confirmed). **Abstract only** (OpenAlex): continuous position measurements "lead to fluctuations without systematic dissipation, and they rapidly destroy off-diagonal terms in the position basis; thus the pointer basis is position." The structure is the same as B&H's Lindblad term (momentum diffusion, no friction). No window computation appears in the abstract.
- **Joos (1984)**, *PRD* 29(8), 1626–1633, DOI 10.1103/PhysRevD.29.1626 (Crossref-confirmed). Still **abstract only**; no open copy found. The page's gap 3 stands.

### Searched and set aside (abstracts read)
- Georgiev (2020), *Prog. Biophys. Mol. Biol.* 158, 16–32, DOI 10.1016/j.pbiomolbio.2020.08.002 (Crossref-confirmed). arXiv:2012.07836 full text grepped: "Zeno" occurs once, in the reference list. No window computation.
- Zhang et al. (2026), "Quantum Zeno effect in the spatial evolution of a single atom", *Nature Communications* 17, 7464, DOI 10.1038/s41467-026-74332-1 (Crossref-confirmed). The abstract reports a direct observation of the Zeno effect in real-space motion. It describes no decoherence-window computation. It is relevant only to the 10-05 note's warning that the 2008 sentence "No experiments have been performed so far" is dated.
- Other works citing B&H 2014: del Campo group 2017 (above), Slichter et al. 2016 (circuit QED), Majeed & Chaudhry 2018 (above), Lucia 2023 (thermodynamics), Xu 2026 (generalised measurements). None treats a brain.
- Sbitnev 2016 (arXiv:1606.00258), Broka 2019, "Consciousness and the Problem of Quantum Measurement" (arXiv:1911.01823), and Ingber 2019, "Quantum Calcium-Ion Interactions with EEG" (*Sci* 1, 20), came up in brain-targeted queries. None computes a Zeno window under decoherence.

## The Answer, Structured

### What B&H compute, in the page's terms
- **Shared basis, continuum.** Their main model is Stapp's 2012 geometry: decoherence in the coordinate basis plus a projector onto an interval of that coordinate. It is also Georgiev's same-basis horn.
- **Environment alone does not confine.** Without the projections, a free particle under position decoherence spreads and diffuses. In the classical limit the projections then only "remove probability". That is the page's "flux through the boundary is classical diffusion, which projections cannot slow", now with a source.
- **When the projections do something the environment does not.** When ε ≪ t_fE, reflection persists in the stationary regime. Before the stationary regime, when ε ≪ t_loc, it persists for about τ = t_loc²/ε. *Note's reading*: in that regime a mind projecting in the environment's own basis is not redundant with it. Georgiev's redundancy sentence does not follow from a shared basis alone; it needs the environment to resolve the in/out distinction at the boundary, which position decoherence does slowly at short range. The shared basis on its own is not enough.

### How this maps onto the page's two-state illustration (note's derivation)
Coherence between points at separation s decays at rate Ds²/ℏ². Over one interval ε, the coherence at the grid scale s = (ℏε/m)^½ loses a fraction set by Dε²/(mℏ) = (ε/t_loc)². This plays the role of the toy's x = γτ. So the toy's x ≪ 1 corresponds to ε ≪ t_loc, and its x ≫ 1 corresponds to B&H's "somewhat trivial" case t_loc ≪ ε, in which the state is classical before each projection. The correspondence is heuristic and is this note's. B&H's extra ingredient, which the toy lacks, is heating: even for ε ≪ t_loc the hold dies after τ = t_loc²/ε unless ε ≪ t_fE.

### How this bears on the page's scaling argument (note's reading)
The page (§strip-width) says: the window is "roughly the time a packet takes to cross ℓ"; "The strip width sets the window; the interval's grain does not".
- **Partly matched.** t_fE = mℏ/p_s² is the time to cross ℏ/p_s at speed p_s/m. If ℓ is read as the stationary coherence length ℏ/p_s, the page's crossing-time heuristic coincides with B&H's stationary criterion.
- **Not matched.** p_s = (mLD)^⅓ depends on the interval length L, so t_fE ∝ L^−⅔ and the grain enters. The transient kill time is set by the *projection-grid* length (ℏε/m)^½, not by the environment's ℓ. Replace the heuristic with B&H's result.
- **Unchanged.** The Tegmark calibration. B&H's window is not the decoherence time for macroscopically distinct states, so the page's "this is the one reading on which Tegmark's figure does not already close Stapp's hold" still holds.

### Limits of the model (carry into any fold)
- A single free particle in one dimension. There is no friction, so ⟨p²⟩ is not capped by any temperature, and a thermalising environment is not modelled.
- Units ℏ = m = L = 1, and no physical system is parametrised. The stationary-regime threshold is a heuristic backed by numerics.
- Survival probability (selective register), not Stapp's non-selective population; see Majeed & Chaudhry.
- B&H use a smoothed projector with width a = ℏε/mL. The thresholds depend on that cut-off choice, which they fix "in a physically sensible way" by equating it with the momentum that leaves the region within ε.

## Major Positions

### Stapp: decoherence does not nullify the hold
- **What the 2015 body adds**: the environment is now inside the evolution, which the 2000 derivation lacked. The claim is the ε → 0 limit on the closed system.
- **What the literature supports**: that limit (Facchi–Pascazio; B&H's τ → ∞ as ε → 0; B&H's quantum stationary regime for ε ≪ t_fE).
- **What it does not supply**: the size of "sufficiently small t", for any brain degree of freedom.
- **Guard**: do not repeat Stapp's claim that Georgiev's simulation supports the hold "in a context with environmental decoherence". In the preprint, the sentence he quotes is from the decoherence-free run.

### Georgiev: different basis breaks it, same basis is redundant
- **Different-basis horn**: supported in Markovian form by B&H's two-state model (L ∝ σx, linear decay for any ε), which matches Georgiev's own choice to model the environment as instantaneous energy-basis projections. Beau et al. and Facchi et al. 2005 add that a non-Markovian window below the environment's correlation regime survives in principle.
- **Same-basis horn**: B&H's continuum model is a shared-basis case in which the projections are not redundant while ε is short enough (note's reading). The redundancy charge holds in B&H's classical regimes (t_loc ≪ ε, or t_fE ≪ ε in the steady state). It is not general.

### The physics default (Bedingham, Halliwell, Facchi, Pascazio, Maniscalco, del Campo)
- Zeno and its environmental suppression are regimes of one dynamics, set by comparing the measurement interval with system and environment timescales. The comparison in the spatial case is ε against the decoherence-heated energy time.

## Key Debates

### Does the 2015 proof answer the "environment during the interval" objection?
- **Sides**: the Map's page (via the 10-05 note) says Stapp 2000's derivation has no environment during the interval. Stapp 2015 includes it.
- **Current state**: answered in form; the timing requirement survives. Stapp's own conclusion is conditioned on "sufficiently small t". The page's sentence "Standard Zeno theory adds a condition he does not state" should be qualified: he states it qualitatively in 2015, without a size.

### Is the brain inside the window?
- **Current state**: open. Nobody has supplied m, D, L and ε for the collective field modes Stapp names, or for ions, and B&H's frictionless model would need a dissipative extension before thermal brain numbers could be inserted. Per the stability note in `deep-review-2026-10-14-zeno-dynamics-on-a-decohered-mixture`, the Map should not compute this itself and present it as the literature's.

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1987 | Caves & Milburn, *PRA* 36, 5543 | Continuous position measurement: momentum diffusion, position pointer basis |
| 2005 | Facchi et al., *PRA* 71, 022302 | Suppression only below a transition interval τ*; acceleration above |
| 2006 | Maniscalco, Piilo & Suominen, *PRL* 97, 130402 | QBM: short-time decoherence decides Zeno vs anti-Zeno |
| 2010 | Facchi, Graffi & Ligabò, *J. Phys. A* 43, 032001 | Zeno effect vanishes as ℏ → 0 |
| 2013 | Bedingham & Halliwell, *PRA* 88, 022128 | Decoherence and reflection from a step |
| 2014 | Bedingham & Halliwell, *PRA* 89, 042116 | Zeno confinement to an interval under position decoherence: window ε < ℏ/E, kill time mℏ/Dε |
| 2015 | Stapp, *NeuroQuantology* 13(2), 190–191 | Closed-system proof: leak second-order "for sufficiently small t" |
| 2017 | Beau et al., *PRL* 119, 130401 | Markovian master equations lack short-time deviations |
| 2018 | Majeed & Chaudhry, *Sci. Rep.* 8, 14887 | Selective vs non-selective Zeno rates can differ beyond weak coupling |

## Potential Article Angles

None as a new article: concepts/ is at cap and the material belongs on the existing page.

## Fold Plan {#fold-plan}

**Host**: `obsidian/concepts/zeno-dynamics-on-a-decohered-mixture.md`, at 2,630 words by `analyze_length` on 2026-11-03 (soft 2,500, hard 3,500). Net cost of the three passages plus references is about **+312 words** by `wc -w` (A +243, B +50, C −4, refs +23), which leaves about 557 below hard. Add the new note's slug to `related_articles` and set `ai_modified`.

**A. §Coordinate Space and the Strip Width {#strip-width}, replace the second paragraph** (the one beginning "What follows is the Map's working, a scaling argument with no number attached."), 135 → 378 words:

> Bedingham and Halliwell (2014) work this case through: a particle in one dimension, projected onto a region at intervals ε while a standard position-decoherence master equation acts. Their Lindblad operator is proportional to position, so environment and projector share a basis. The coherences the hold needs behave as the strip-width reading says: the reflection process behind the Zeno effect "involves quantum coherences over very short lengthscales", and "the corresponding decoherence time for this process is therefore very long." The hold shows as reflection from the region's edge, and it "arises when the projections are sufficiently rapid that ε < ℏ/E", E being the particle's kinetic energy. The environment closes the window by heating: in their account the diagonalisation decoherence produces is equivalently a growth of momentum fluctuations. Momentum diffusion at rate D raises E until ℏ/E falls below ε, which takes about mℏ/Dε, the decoherence time over the grid (ℏε/m)^½ that the projections lay down. If ε is much longer than the localisation time (mℏ/D)^½, the state is "completely classicalized before the next projection happens", and the projections only remove probability. In the long-run steady state, reflection survives when ε is well below a final energy time fixed by D, the mass and the region's length, and is absent when ε is well above it. They track the probability of passing every check, not the unconditional population, so carrying their thresholds over is the Map's step.
>
> The strip-width reading is still the only one on which Tegmark's figure does not already close Stapp's hold, and on the Map's reading the model refines it in two ways. The length that matters is set by the projection interval and the mass, and the region's length enters the steady-state threshold, so the interval's grain does matter. And a shared basis does not by itself make the projections redundant: position decoherence alone confines nothing, and fast enough projections still reflect. The model is a free particle without friction, and no source the Map has found sets its parameters for any neural degree of freedom. Stapp (2000) leaves the projection interval d unspecified beyond requiring that the process "repeats rapidly" on the scale of the brain's sub-40 Hz field, so whether his hold falls inside the window cannot be read off his text.

Guards for A: the subject of the first quote is B&H's "The reflection process entailed in the Zeno effect", so keep the subject outside the quotation marks as drafted. Keep "on the Map's reading" on the two consequences. Keep the Tegmark sentence, which the 10-14 deep review installed. Do not add numbers.

**B. §Two Regime-Limited Truths {#two-regime-limited-truths}, Stapp paragraph, replace its last sentence** ("Standard Zeno theory adds a condition he does not state: only the part of that evolution still in its quadratic phase can be rolled back."), 25 → 75 words:

> Standard Zeno theory adds a condition he does not state there: only the part of that evolution still in its quadratic phase can be rolled back. His 2015 reply to Georgiev comes closest. It evolves brain and environment together under one unitary, shows that the first-order term in t vanishes, and concludes that the second-order term "is the dominant term for change for sufficiently small t". That states the quadratic window without giving its size.

Guard for B: do not quote "first- order" (the PDF has a stray space); paraphrase as drafted.

**C. §What Remains Open {#what-remains-open}, replace the lead sentence and the first two bullets**, 96 → 92 words. Keep the third bullet ("The regime boundary at source") unchanged:

> Two gaps keep the question unsettled. In each, nothing has yet come in, which is weaker than a test survived.
>
> - **The window in a brain.** Bedingham and Halliwell (2014) give the window's form for a particle confined to a region under position decoherence, and Stapp's 2015 proof holds only "for sufficiently small t". No source the Map has found supplies the mass, diffusion constant, region size and projection interval for the collective field modes Stapp names, or for any other neural degree of freedom, so the window's size is still uncomputed.

**References**: add, in alphabetical position,
`1. Bedingham, D.J., & Halliwell, J.J. (2014). Classical limit of the quantum Zeno effect by environmental decoherence. *Physical Review A*, 89(4), 042116. https://doi.org/10.1103/PhysRevA.89.042116 (arXiv:1402.4365)`
and change the Stapp 2015 entry's tail from `13(2). … (abstract consulted)` to `13(2), 190–191. https://doi.org/10.14704/nq.2015.13.2.851`.

**Unchanged by this note**: the lead (L35, "no published model the Map has found computes the window for the neural degrees of freedom Stapp names") and the Tenet 3 endpoint (L100, "turns on a quantity no one has computed") both remain true.

**Secondary refine targets** (not part of this fold; the driver may mint):
1. `concepts/process-1-specification-problem` L69 (3,086 words; about 413 headroom). It reads "Stapp's 2015 rejoinder promises … only its abstract could be located" and "No worked model on either side compares the interval grain with the decoherence strip width". Update the first clause from the body, as in B. Keep the second as true of the two sides, and point it at B&H via `[[zeno-dynamics-on-a-decohered-mixture#strip-width|…]]`. L116's "(abstract only consulted)" needs the same fix.
2. `concepts/sign-problem-for-conscious-observation` L122 annotation ("neither addresses sign"). The body confirms it: the 2015 proof is the ε → 0 limit only. No change needed. Facchi et al. 2005's τ* (suppression below, acceleration above, possibly much shorter than the reservoir's inverse bandwidth) could strengthen that page if it lacks it; not checked.
3. `topics/motor-control-quantum-zeno` L115: re-read live on 2026-11-03. Its attribution ("on his account the hold works on the decohered state and need not outpace decoherence") is accurate to both the 2000 text and the 2015 body. No change needed.
4. The research note `stapp-process-1-basis-timing-critiques-2026-09-27` L163 says the Stapp 2015 full text was not found. A dated one-line pointer to this note would stop the claim propagating.

## Gaps in Research

- The published *PRA* text of B&H 2014 was not compared with arXiv v1. The abstracts differ slightly.
- Whether B&H's thresholds carry over to the non-selective population (Stapp's register) was not worked out.
- No dissipative (thermalising) version of B&H's model was searched for. It would be the next step before any brain parameters could be inserted, and only a source should insert them.
- Joos 1984 body still unread. Caves & Milburn 1987 read at abstract level only.
- The published *IJMPB* layout of Georgiev 2015 was not checked against the preprint for the sentence Stapp quotes.
- Absence claims rest on these control pairs. OpenAlex "quantum Zeno spatial region environmental decoherence" returns B&H at rank 1 (positive control). The brain-targeted variants ("… neuron", "quantum Zeno coordinate space interval brain decoherence", "Zeno effect ion channel position decoherence projection interval") return no window computation in the top results. The OpenAlex citation lists show no work citing both B&H 2014 and any of Stapp 2015, Georgiev 2015 or Georgiev 2020. Google Scholar was not used.

## Citations

1. Beau, M., Kiukas, J., Egusquiza, I.L., & del Campo, A. (2017). Nonexponential quantum decay under environmental decoherence. *Physical Review Letters*, 119(13), 130401. https://doi.org/10.1103/PhysRevLett.119.130401 (arXiv:1706.06943)
2. Bedingham, D.J., & Halliwell, J.J. (2013). Suppression of quantum-mechanical reflection by environmental decoherence. *Physical Review A*, 88(2), 022128. https://doi.org/10.1103/PhysRevA.88.022128 (arXiv:1306.3377; abstract read)
3. Bedingham, D.J., & Halliwell, J.J. (2014). Classical limit of the quantum Zeno effect by environmental decoherence. *Physical Review A*, 89(4), 042116. https://doi.org/10.1103/PhysRevA.89.042116 (arXiv:1402.4365, read in full)
4. Caves, C.M., & Milburn, G.J. (1987). Quantum-mechanical model for continuous position measurements. *Physical Review A*, 36(12), 5543–5555. https://doi.org/10.1103/PhysRevA.36.5543 (abstract only)
5. Facchi, P., Graffi, S., & Ligabò, M. (2010). Classical limit of the quantum Zeno effect. *Journal of Physics A: Mathematical and Theoretical*, 43(3), 032001. https://doi.org/10.1088/1751-8113/43/3/032001 (arXiv:0911.5675; abstract read)
6. Facchi, P., Tasaki, S., Pascazio, S., Nakazato, H., Tokuse, A., & Lidar, D.A. (2005). Control of decoherence: Analysis and comparison of three different strategies. *Physical Review A*, 71(2), 022302. https://doi.org/10.1103/PhysRevA.71.022302 (arXiv:quant-ph/0403205)
7. Georgiev, D.D. (2015). Monte Carlo simulation of quantum Zeno effect in the brain. *International Journal of Modern Physics B*, 29(7), 1550039. https://doi.org/10.1142/S0217979215500393 (arXiv:1412.4741)
8. Georgiev, D.D. (2020). Quantum information theoretic approach to the mind–brain problem. *Progress in Biophysics and Molecular Biology*, 158, 16–32. https://doi.org/10.1016/j.pbiomolbio.2020.08.002 (arXiv:2012.07836; grepped only)
9. Joos, E. (1984). Continuous measurement: Watchdog effect versus golden rule. *Physical Review D*, 29(8), 1626–1633. https://doi.org/10.1103/PhysRevD.29.1626 (abstract only)
10. Majeed, M., & Chaudhry, A.Z. (2018). The quantum Zeno and anti-Zeno effects with non-selective projective measurements. *Scientific Reports*, 8, 14887. https://doi.org/10.1038/s41598-018-33181-9
11. Maniscalco, S., Piilo, J., & Suominen, K.-A. (2006). Zeno and anti-Zeno effects for quantum Brownian motion. *Physical Review Letters*, 97(13), 130402. https://doi.org/10.1103/PhysRevLett.97.130402 (arXiv:quant-ph/0602133)
12. Stapp, H.P. (2015). Reply to Georgiev: No-Go for Georgiev's No-Go Theorem. *NeuroQuantology*, 13(2), 190–191. https://doi.org/10.14704/nq.2015.13.2.851 (publisher PDF via Internet Archive capture, 2018-07-21)
13. Zhang, Z.-Y., et al. (2026). Quantum Zeno effect in the spatial evolution of a single atom. *Nature Communications*, 17, 7464. https://doi.org/10.1038/s41467-026-74332-1 (abstract only)
