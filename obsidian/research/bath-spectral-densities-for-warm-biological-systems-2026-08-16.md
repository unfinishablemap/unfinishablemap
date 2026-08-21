---
title: "Research Notes - Bath Spectral Densities for Warm Biological Systems"
created: 2026-08-16
modified: 2026-08-16
human_modified:
ai_modified: 2026-08-21T16:45:07+00:00
draft: false
description: "Published warm-biology spectral densities are real and specific, but sit many orders of magnitude above any neural transition frequency. The analogy does not transfer."
topics:
  - "[[quantum-biology-and-neural-consciousness]]"
  - "[[motor-control-quantum-zeno]]"
concepts:
  - "[[quantum-zeno-effect]]"
  - "[[sign-problem-for-conscious-observation]]"
  - "[[stapp-quantum-mind]]"
related_articles:
  - "[[anti-zeno-effect-and-sign-of-conscious-observation-2026-08-05]]"
  - "[[timing-gap-problem]]"
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-08-16
last_curated:
last_deep_review:
---

# Research: Bath Spectral Densities for Warm Biological Systems

**Date**: 2026-08-16
**Purpose**: The article `sign-problem-for-conscious-observation` concludes that the sign question turns on the neural coupling spectral density G(ω), a quantity it says has never been characterised. This note asks what the *adjacent* literature — spectral densities extracted for photosynthetic complexes, cryptochrome radical pairs, and tubulin — actually contains, and whether any of it transfers. The operative question is the **shape** of G(ω) near the relevant transition frequency, not a bare thermal timescale.

**Search queries used**:
- FMO complex spectral density molecular dynamics reorganization energy Olbrich Kleinekathöfer
- Drude-Lorentz spectral density light-harvesting reorganization energy bath correlation time Ishizaki Fleming
- spectral density bath correlation function microtubule tubulin neuron quantum decoherence Ohmic Drude
- ion channel gating quantum bath spectral density reorganization energy neuronal membrane open quantum system
- Kofman Kurizki 2000 reservoir correlation time Zeno condition measurement interval
- Denton Smith Kattnig 2024 cryptochrome radical pair quantum Zeno recombination rate
- Chaudhry general framework quantum Zeno anti-Zeno effects Ohmicity filter function

## Executive Summary

The adjacent literature is real, quantitatively specific, and entirely uncited by the Map — but it does **not** rescue the Zeno cluster's biological analogy, and the honest finding is mostly negative.

Two results, pulling opposite ways:

1. **The timescale transfers; this is a genuine upgrade.** Published bath correlation times for warm biomolecular environments cluster at **13–50 fs** (Ishizaki & Fleming's Drude fit for FMO at 300 K uses τ_c = 50 fs; a 2026 tubulin preprint reports a protein-bath baseline near 13 fs). The Map's illustrative ħ/k_BT ≈ 25 fs at 310 K sits inside that range. That figure can stop being flagged as *only* the Map's own arithmetic — the order of magnitude is now externally corroborated, though still not by a neural measurement.

2. **The shape does not transfer, and this is the real finding.** Every published biological spectral density characterises G(ω) around a *molecular* transition — an optical/vibrational one for light-harvesting complexes, a spin transition for radical pairs. The structure that carries the coupling weight sits at **1600–2000 cm⁻¹** for photosynthetic complexes and at **MHz–GHz** for cryptochrome. A neural selection event, on any reading the Map has offered, would occur at Hz–kHz. Taking that as 1 Hz to 1 kHz, the gap is **roughly 11 to 14 orders of magnitude for the photosynthetic spectra, and 3 to 9 orders for the radical-pair case**. Since Kofman and Kurizki's criterion is precisely a statement about G(ω)'s shape *near the transition frequency*, a spectrum characterised that far up constrains nothing about the neural case.

A third result is worth more than either: the one paper that attempts a genuinely *neural* bath — Naskar and Joarder on microtubule decoherence — assumes an Ohmic spectral density and then leaves its amplitude explicitly undetermined, deferring it as future work. The Map's claim that the quantity "has never been characterised" can therefore be cited rather than merely asserted.

**Recommendation: fold into the two existing articles; do not mint a new one.** Details in "Downstream" below.

## The Frequency Ladder

This is the note's central object. Figures marked *(sourced)* are quoted from the papers; those marked *(conversion)* are arithmetic performed for the Map from a sourced figure, using 1 cm⁻¹ ≈ 29.98 GHz.

| System / quantity | Frequency scale | In cm⁻¹ | Source |
|---|---|---|---|
| FMO vibrational coupling band | 1600–2000 cm⁻¹ *(sourced)* | 1600–2000 | Huh et al. 2013 |
| BChl vibrational modes | ~1600 cm⁻¹ *(sourced)* | ~1600 | Olbrich et al. 2011 |
| Low-frequency band governing transfer | `< 500 cm⁻¹` *(sourced)* | `< 500` | Huh et al. 2013 |
| Drude cutoff γ from τ_c = 50 fs | 2×10¹³ rad s⁻¹ *(conversion)* | ≈106 | Ishizaki & Fleming 2009 |
| Reorganisation energy λ (Drude fit) | 35 cm⁻¹ *(sourced)* | 35 | Ishizaki & Fleming 2009 |
| Cryptochrome inter-radical coupling | up to −1.7 GHz *(sourced)* | ≈5.7×10⁻² *(conversion)* | Denton et al. 2024 |
| Cryptochrome N5 hyperfine `A∥/(2π)` | 49.2 MHz *(sourced)* | ≈1.6×10⁻³ *(conversion)* | Denton et al. 2024 |
| Geomagnetic Larmor precession | 1.4 MHz *(sourced)* | ≈4.7×10⁻⁵ *(conversion)* | Denton et al. 2024 |
| Neural gamma-band rhythm, 40 Hz | 40 Hz | ≈1.3×10⁻⁹ *(conversion)* | — |

The published spectra live in the top half of this ladder. The neural case lives at the bottom. Nothing in the literature bridges it.

## Key Sources

### Ishizaki & Fleming (2009), *PNAS* — the canonical warm-biology bath parameters

- **URL**: https://doi.org/10.1073/pnas.0908989106
- **Type**: Paper (PNAS), open access via PMC
- **Key points**:
  - The spectral density is the overdamped Brownian oscillator (Drude-Lorentz) form, `J(ω) = 2λγω/(ω² + γ²)`.
  - Reorganisation energy λ = 35 cm⁻¹; bath relaxation time τ_c = γ⁻¹ = 50 fs; T = 300 K.
  - Robustness was also checked at τ_c = 166 fs and τ_c = 35 fs.
- **Why it matters here**: this is the single most-cited parameter set for a warm biological bath, and it supplies the correlation-time figure that corroborates the Map's 25 fs arithmetic. It is also the source of the *functional form* whose low-frequency behaviour is analysed below.
- **Tenet alignment**: Neutral. A modelling choice in photosynthesis, with no bearing on dualism either way.

### Huh, Saikin, Brookes, Valleau, Fujita & Aspuru-Guzik (2013) — where the coupling weight actually sits

- **URL**: https://arxiv.org/abs/1307.0886
- **Type**: Paper (arXiv preprint; later published)
- **Key points**:
  - On the exciton transfer matrix at 300 K: "The strong white diagonal band corresponds to the strong exciton-phonon coupling at 1600–2000 cm−1 ... which leads to the rapid energy dissipation of the localized IS within the roll."
  - The appendix plots spectral densities on a wavenumber axis running to 4000 cm⁻¹, and identifies the "low frequency region" governing inter-unit transfer as below 500 cm⁻¹.
  - Spectral densities were taken from prior QM/MM and TDDFT work rather than recomputed.
- **Why it matters here**: this is the clearest published statement of *where in frequency* a warm biological spectral density carries its structure. It is the paper that makes the mismatch quantitative.
- **Tenet alignment**: Neutral.

### Olbrich, Strümpfer, Schulten & Kleinekathöfer (2011), *J. Phys. Chem. Lett.* — MD-derived spectral densities

- **URL**: https://doi.org/10.1021/jz2007676
- **Type**: Paper, open access via PMC
- **Key points**:
  - Spectral densities were obtained from temporal autocorrelation of the ground-to-excited-state energy gap along MD trajectories.
  - "it is well known that BChl molecules have vibrational modes in the region of 1600 cm⁻¹ which are strongly present in Figure 5."
  - Spectral densities are presented in eV, extending to roughly 0.2 eV.
- **Why it matters here**: establishes that the MD-extraction method the review nomination had in mind is real and produces highly structured spectra — sharp vibrational peaks rather than the smooth Drude curve. Shape information exists; it is simply shape information about the wrong frequency decade.
- **Tenet alignment**: Neutral.

### Naskar & Joarder (2023) — the closest thing to a neural bath, and its own admission

- **URL**: https://arxiv.org/abs/2304.06518
- **Type**: Paper (arXiv preprint), "Quantum decoherence in Microtubules"
- **Key points**:
  - Treats a tubulin dimer superposition (the αβ state) coupled to a bosonic environment with an **assumed** Ohmic spectral density with upper cutoff Ω.
  - Derives a decoherence time τ_d = 1.60485×10⁻²¹ C₀ seconds, where C₀ absorbs the coupling strength and the spectral density amplitude.
  - The paper then states plainly: "Now to find the exact value of τd finding the proper value of C0 for the particular environment inside the nerve cells is important as well as difficult. Finding the proper value of C0 is our future proposed work."
  - Repeated in the conclusions: "Finding the explicit value of C0 for real environment inside neuron is very important for finding the actual time of decoherence. This is our proposed future work."
- **Why it matters here**: **this is the most valuable single find in the note.** It converts the Map's assertion of absence into a citable admission by the authors of the nearest relevant work. The spectral density inside a neuron is not merely uncomputed by the Map; it is flagged as unknown and deferred by the people who needed it.
- **Tenet alignment**: Neutral on the tenets, but it *supports* the Map's epistemic caution rather than undercutting it.

### Firmenich, Firmenich & Firmenich (2026), bioRxiv preprint — an external version of the Map's own worry

- **URL**: https://doi.org/10.64898/2026.05.10.724047
- **Type**: Preprint (bioRxiv, posted 2026-05-13) — **not peer reviewed**
- **Key points** (from the record's abstract; see Gaps):
  - Framing quote: "Quantum effects in biology are unavoidable at the molecular scale; the unresolved question is whether they can remain functionally relevant across the timescale gap between femtosecond molecular dynamics and microsecond-to-millisecond biological function."
  - Compares secular Lindblad, Redfield and HEOM treatments of tubulin; reports equilibrium dephasing of roughly 1 fs at body temperature and a protein-bath baseline near 13 fs; a 30 ps HEOM trajectory with terminal purity 0.210 and stretched-exponential exponent near 0.44.
  - Reports a thermodynamic-uncertainty argument that neural-scale cascade amplification would require about five orders of magnitude more power than the local microtubule GTP budget allows.
- **Why it matters here**: an independent group is now posing exactly the Map's question — whether femtosecond bath physics can carry anything to millisecond neural function — and answering it with an energetic bound. The 13 fs protein-bath figure is a second corroboration of the correlation-time scale.
- **Tenet alignment**: **Conflicts** with the corpus's more optimistic quantum-interface readings. If the amplification bound holds, it constrains any mechanism that needs molecular-scale quantum structure to reach behaviour. It does not touch Tenet 1 directly — a dualist interface need not run through microtubules — but it is bad news for microtubule-mediated routes specifically.

### Chaudhry (2016), *Scientific Reports* — the shape criterion, stated generally

- **URL**: https://doi.org/10.1038/srep29497
- **Type**: Paper, open access via PMC
- **Key points**:
  - "the effective decay rate can be written as an overlap integral of the spectral density of the environment J(ω) and a generalized 'filter function' Q(ω, τ)".
  - The spectral density is parameterised as `J(ω) = Gω^s e^(−ω/ω_c)`, where "the parameter s characterizes the Ohmicity of the environment. Namely, s = 1 corresponds to an Ohmic environment, s > 1 gives a super-Ohmic environment, while s < 1 corresponds to a sub-Ohmic environment."
  - The paper demonstrates the QZE/AZE crossover through worked spin-boson examples rather than stating a closed-form universal criterion in terms of s and ω_c.
- **Why it matters here**: confirms that the sign is fixed by an overlap between J(ω) and a measurement-set filter function, and gives the standard parameterisation in which "shape" is a definite question (the exponent s and the cutoff ω_c). It also confirms that no general rule reduces the sign to Ohmicity alone — the answer depends on where the transition frequency sits relative to the cutoff.
- **Tenet alignment**: Neutral.

### Denton, Smith, Xu, Pugsley, Toghill & Kattnig (2024), *Nature Communications* — the biological Zeno precedent, at its own scale

- **URL**: https://doi.org/10.1038/s41467-024-55124-x
- **Type**: Paper, open access via PMC
- **Key points**:
  - Recombination rates: "k_S and k_T in the range of 10−3 μs−1 to 106 μs−1, formally corresponding to lifetimes between 1 ms and 1 ps."
  - Hyperfine: "N5 nucleus with A⊥/(2π) = − 2.6 MHz, A∥/(2π) = 49.2 MHz"; inter-radical couplings up to −1.7 GHz; Larmor precession in the geomagnetic field of 1.4 MHz at 50 μT.
  - The Zeno mechanism is driven by the spin-selective recombination reaction, not by an observer.
- **Why it matters here**: the Map already cites this as its one warm-biology Zeno precedent. The numbers show the precedent operates on *spin* transitions at MHz–GHz, with the "measurement" being a chemical decay channel whose rate range spans nine orders of magnitude. Nothing about the neural case is licensed by it.
- **Tenet alignment**: Neutral as physics; the Map already reads it as illustrating an observation-concept Stapp's proposal cannot use.

## The Shape Question, Answered as Far as It Can Be

The nomination asked for shape rather than timescale. Here is what can be said, with the epistemic status of each step marked.

**Sourced.** The sign is set by the overlap of J(ω) with a measurement-broadened filter function (Chaudhry 2016; Kofman & Kurizki 2000, already cited in the corpus). "Shape near the transition frequency" is therefore the right object.

**Sourced.** Every biological J(ω) in the literature is characterised around a molecular transition: 1600–2000 cm⁻¹ vibrational structure for light-harvesting complexes, MHz–GHz spin structure for radical pairs.

**Map's inference, not published.** For the Drude-Lorentz form used throughout this literature, `J(ω) = 2λγω/(ω² + γ²)`, the low-frequency limit is linear: as ω → 0, `J(ω) → 2λω/γ`. A neural transition frequency is roughly nine to twelve orders of magnitude below the 106 cm⁻¹ cutoff, so on this functional form a neural process would sit on the extreme *rising* low-frequency flank of the bath spectrum, where the coupling weight is near zero and monotonically increasing. Broadening a filter function outward from a transition sitting on a monotonically rising flank that starts near zero can only sample *more* spectral weight, not less — which is the acceleration (anti-Zeno) side. **This is an inference from a published functional form, not a published result, and the functional form was fitted for a system nothing like a neuron.** It should be stated in the corpus with exactly that hedge, because it points the same way as Horn 1 and would be easy to over-sell.

**Honest negative.** I did not find any published spectral density, reorganisation energy, or bath correlation function computed for a neural degree of freedom — an ion channel gating coordinate, a membrane potential mode, or a synaptic vesicle event. Searches on ion-channel MD and open-quantum-system treatments of membrane proteins returned classical conformational-dynamics work and proton-transport modelling, not bath characterisation. This is a search result, not a proof of absence; but it is consistent with Naskar and Joarder having to defer the same quantity.

## Major Positions

### "Warm biological quantum effects are established, so neural ones are plausible"
- **Proponents**: the general quantum-biology argument the Map's Zeno cluster leans on.
- **Core claim**: FMO and cryptochrome show that quantum coherence survives in warm, wet biology; a neural analogue is therefore not absurd.
- **Relation to site tenets**: this note **weakens** the argument as applied to the sign question. The established cases are established *at their own frequencies*. Coherence surviving at 1600 cm⁻¹ in a pigment-protein complex says nothing about G(ω) at 40 Hz in tissue. The Map should keep the plausibility argument for coherence-in-warm-biology in general, and stop letting it do work on the sign question specifically.

### "The timescale gap is the binding constraint"
- **Proponents**: Firmenich et al. 2026 (preprint); implicitly Georgiev, already cited in the corpus.
- **Core claim**: the gap between femtosecond bath physics and millisecond function is the thing to explain, and energetic bounds may close it off.
- **Relation to site tenets**: **conflicts** with microtubule-mediated interface routes. Consistent with the Map's own [[timing-gap-problem]] worry. The Map should note that an external group has independently reached the framing, which slightly raises confidence that the worry is well-posed.

## Downstream: Refine, Do Not Create

**This note licenses `refine-draft` work on two existing articles and nominates no new article.** `topics/` is at 320/320 and `concepts/` has a single unclaimed slot that a sibling research note has recommended leaving unspent. The material folds cleanly, because both target articles already contain the exact sentences it refines — this is correction and citation of existing claims, not new territory.

### For `sign-problem-for-conscious-observation`

1. **Split the absence claim.** The article says of the 25 fs figure that it is "not a measured or published neural parameter, and no such parameter exists in the literature." The first half is correct and should stand. The second half is too strong as written: published *warm-biomolecular* bath correlation times do exist, at 13–50 fs. Recommend rewording to distinguish "no neural parameter" (true, and now citable) from "no warm-biology parameter" (false).
2. **Upgrade the 25 fs caveat rather than remove it.** Keep the flag that it is the Map's arithmetic; add that it lands inside the 13–50 fs range published for warm biomolecular baths, so the order of magnitude is externally corroborated. This *strengthens* the article's argument — the timescale demand it derives is not an artefact of a back-of-envelope calculation.
3. **Cite the deferral.** In "What Would Settle It", replace the bare assertion that nobody has computed G(ω) with the Naskar and Joarder citation, which assumes an Ohmic form and explicitly defers the neural amplitude to future work.
4. **Sharpen what needs measuring.** "Characterisation of the neural coupling spectrum G(ω)" should become characterisation *at neural transition frequencies*, noting that existing biological characterisations sit 11–14 orders of magnitude higher (photosynthetic) or 3–9 orders higher (radical-pair). This is the note's main contribution to that section.
5. **Add the scale mismatch to the Denton paragraph.** The cryptochrome precedent operates on MHz–GHz spin transitions. The article currently distinguishes it from Stapp's model on the *concept of measurement*; the frequency mismatch is a second, independent reason it does not transfer.
6. **Optionally add the low-frequency-flank inference** as a hedged paragraph, with the caveat above. It supplies a reason to expect Horn 1 generically that is better than "the sign is unknown", while remaining explicitly an inference.

### For `quantum-zeno-effect`

1. **Same refinement at the "nobody has characterised" sentence** (currently in the anti-Zeno caveat paragraph): keep the claim, attach the Naskar and Joarder citation, and specify that the uncharacterised quantity is the spectrum *at neural frequencies*.
2. **Name the adjacent literature in the biological-precedent section.** The article discusses biological Zeno precedents without mentioning that a mature literature exists on extracting spectral densities from MD for warm biomolecules. One or two sentences with the Ishizaki-Fleming parameters and the 1600–2000 cm⁻¹ band would let a reader see both that the technique exists and why it has not been applied here.

### Cap-aware note on not creating

A "Bath Spectral Densities in Warm Biology" article would be a survey of physical chemistry with a single paragraph of Map-relevant payload, and that payload is a *negative* result about an analogy the Map already treats cautiously. It belongs inside the two articles that make the claims it corrects. Spending the last `concepts/` slot on it would be poor value even if the slot were free.

## Calibration

The result here is **net negative for the Zeno mechanism and net positive for the Map's honesty about it**, and nothing in this note should upgrade the sign-problem article's coherence-grade status.

- The biological spectral densities that exist are for molecular transitions at energies wholly unlike anything a neural selection event would involve. **The analogy the Zeno cluster leans on does not transfer.** That is a real constraint on the Map's own mechanism and should be stated as one.
- The one genuine gain — external corroboration of the 25 fs order of magnitude — makes the article's *objection* stronger, not its mechanism. It firms up the timescale demand that the discrete-observation move was meant to escape.
- No applicability should be manufactured. The correct summary sentence for the corpus is that the warm-biology literature constrains G(ω) in a frequency window that has no overlap with the neural case, and that the nearest neural attempt defers the quantity as unknown.

## Gaps in Research

Flagged as binding for downstream work:

- **Firmenich et al. 2026 figures come from the record's abstract, not the paper body.** The bioRxiv full-text page returned HTTP 403 on two attempts; the abstract was retrieved through the bioRxiv details API. The 1 fs, 13 fs, 30 ps, 0.210 purity, 0.44 exponent and "five orders of magnitude" figures are therefore **abstract-level and not verified against the paper body**. It is additionally a **preprint and not peer reviewed**, and the author list (three authors sharing a surname) is unusual enough to warrant a second look before the corpus leans on it. Treat as suggestive, cite with the preprint flag, and do not build an argument on the amplification bound without retrieving the body.
- **Quotes from Ishizaki & Fleming, Olbrich et al., Chaudhry, and Denton et al. were extracted via WebFetch from PMC/publisher pages rather than read by me in full.** The Huh et al. and Naskar & Joarder quotes are the strongest in this note: those were extracted from the raw PDFs locally and are grep-verifiable. Prefer the latter two where a verbatim quote is going into an article.
- **Olbrich et al. report reorganisation energies in eV, not cm⁻¹.** I did not obtain a numeric cm⁻¹ reorganisation energy from that paper. The MD-derived reorganisation energies are widely said to exceed experimental fits, but I did not verify a specific pair of numbers at source, so no such comparison should be written into an article on the strength of this note.
- **The FMO electronic transition wavenumber is deliberately omitted.** A figure near 12,500 cm⁻¹ for the BChl Qy band is standard, but I did not verify it at a primary source, so the frequency ladder above stops at the vibrational structure.
- **Unit conversions in the ladder are the Map's arithmetic**, using 1 cm⁻¹ ≈ 29.98 GHz. The sourced figures are marked separately. The 106 cm⁻¹ Drude cutoff in particular is a conversion from the sourced 50 fs, not a number appearing in Ishizaki & Fleming.
- **The low-frequency-flank argument is unpublished inference.** No paper was found that works out Zeno/anti-Zeno for a transition frequency nine to twelve orders of magnitude below the bath cutoff. If the corpus uses it, the hedge must travel with it.
- **Absence of a neural spectral density is a search result, not a proof.** I did not find one; I did not exhaust the literature.
- **Kofman & Kurizki 2000 was not re-fetched.** The quotes in the corpus were verified in prior work and I relied on that, adding only the shape framing from Chaudhry 2016.

## Citations

1. Ishizaki, A., & Fleming, G.R. (2009). Theoretical examination of quantum coherence in a photosynthetic system at physiological temperature. *PNAS*, 106(41), 17255–17260. https://doi.org/10.1073/pnas.0908989106
1. Huh, J., Saikin, S.K., Brookes, J.C., Valleau, S., Fujita, T., & Aspuru-Guzik, A. (2014). Atomistic study of energy funneling in the light-harvesting complex of green sulfur bacteria. *Journal of the American Chemical Society*, 136(5), 2048–2057. https://doi.org/10.1021/ja412035q. Preprint: arXiv:1307.0886 (quotes above verified against **v2**, which carries the Appendix; **v1 lacks it** and reads "red diagonal band" where v2 reads "white").
1. Olbrich, C., Strümpfer, J., Schulten, K., & Kleinekathöfer, U. (2011). Theory and simulation of the environmental effects on FMO electronic transitions. *J. Phys. Chem. Lett.*, 2(14), 1771–1776. https://doi.org/10.1021/jz2007676
1. Naskar, K., & Joarder, P. (2023). Quantum decoherence in Microtubules. arXiv:2304.06518. https://arxiv.org/abs/2304.06518
1. Firmenich, F., Firmenich, P., & Firmenich, L. (2026). Beyond Redfield: Thermodynamic bounds and non-perturbative quantum dynamics in tubulin networks. bioRxiv preprint, posted 2026-05-13. https://doi.org/10.64898/2026.05.10.724047 — **preprint, not peer reviewed**
1. Chaudhry, A.Z. (2016). A general framework for the quantum Zeno and anti-Zeno effects. *Scientific Reports*, 6, 29497. https://doi.org/10.1038/srep29497
1. Denton, M.C.J., Smith, L.D., Xu, W., Pugsley, J., Toghill, A., & Kattnig, D.R. (2024). Magnetosensitivity of tightly bound radical pairs in cryptochrome is enabled by the quantum Zeno effect. *Nature Communications*, 15, 10823. https://doi.org/10.1038/s41467-024-55124-x
1. Kofman, A.G., & Kurizki, G. (2000). Acceleration of quantum decay processes by frequent observations. *Nature*, 405(6786), 546–550. https://doi.org/10.1038/35014537 — cited from prior corpus verification, not re-fetched for this note
