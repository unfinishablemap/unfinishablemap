---
title: "Sorkin Higher-Order Interference and Quantum Measure Theory"
description: "The interference-order hierarchy that operationalises 'the Born rule is tested': what the third-order parameter κ measures, the ~10⁻²–10⁻⁴ optical bounds, and where the tested slice ends."
created: 2026-07-16
modified: 2026-07-16
human_modified:
ai_modified: 2026-07-16T12:32:09+00:00
draft: false
topics:
  - "[[born-rule-and-the-consciousness-interface]]"
  - "[[brain-internal-born-rule-testing]]"
  - "[[sorkin-delta-brain-internal-analogues]]"
concepts:
  - "[[generalised-probabilistic-theories]]"
  - "[[channel-class-taxonomy]]"
related_articles:
  - "[[tenets]]"
ai_contribution: 100
author:
ai_system: claude-opus-4-8
ai_generated_date: 2026-07-16
last_curated:
---

Sorkin's *quantum measure theory* reframes the Born rule as one rung on a hierarchy of possible probability laws, and it names the exact quantity a laboratory measures to test that rung: the **third-order interference term** I₃, usually reported in normalised form as κ (kappa). Classical (Kolmogorov) probability forbids second-order interference; standard quantum mechanics permits it but forbids the *third* order and everything above it. So "the Born rule holds" becomes the concrete, checkable statement **κ = 0**, and "the Born rule has been tested" becomes a number: κ is bounded below roughly 10⁻² of the pairwise interference in single-photon optics (Sinha et al. 2010) and below ~10⁻⁴ in a five-path interferometer (Kauten et al. 2017). This concept matters to The Unfinishable Map because that bound is the empirical anchor beneath the Map's most-repeated physical claim — that its proposed [[tenets#^minimal-quantum-interaction|minimal quantum interaction]] is measured against a *tested* Born rule — and because the tested regime is a clean external apparatus, not the warm neural tissue a consciousness-interface proposal would need. The bound is real, tightening, and silent about the brain: exactly the shape [[tenets#^occams-limits|Tenet 5]] predicts.

One caveat rides along from the start and is developed below ([[#reading-a-nonzero-term|"Does a nonzero term mean new physics?"]]): a *measured* nonzero κ need not be a Born-rule violation, because finite-slit looped trajectories produce a small apparent κ entirely within standard quantum mechanics. The clean statement I₃ = 0 is about amplitudes summed over paths, not about raw slit intensities.

## The Interference-Order Hierarchy (Neutral Definition)

Sorkin (1994) treats quantum mechanics as a *generalised measure theory*. His observation is that the additivity of classical probability is, in his words, "only the first in a hierarchy of possible sum-rules, each of which implies its successor." Each rung is defined by which *inclusion–exclusion residue* vanishes.

Set up a multi-slit experiment with slits (paths) A, B, C, …, and let P_R be the measured intensity when exactly the subset R of slits is open. The successive interference terms are the alternating residues:

- **Second order** (two slits): I₂ = P_AB − P_A − P_B. For classical particles the intensities simply add, so I₂ = 0. Waves — and quantum systems — give I₂ ≠ 0. This is ordinary two-slit interference.
- **Third order** (three slits): I₃ = P_ABC − (P_AB + P_AC + P_BC) + (P_A + P_B + P_C). Standard quantum mechanics gives **I₃ = 0 exactly.**

The hierarchy generalises: an "order-*k*" theory is one whose first non-vanishing residue is I_{k+1}. Classical stochastic processes (Brownian motion) are order 1: I₂ = 0. Quantum mechanics is order 2: I₂ ≠ 0 but I₃ = 0. A world with I₃ ≠ 0 would be an **order-3** theory — genuinely post-quantum.

| Theory | Signature | I₂ | I₃ |
|---|---|---|---|
| Classical (Kolmogorov) | order 1 | 0 | 0 |
| Quantum (Born rule) | order 2 | ≠ 0 | 0 |
| Post-quantum (order-3) | order 3 | ≠ 0 | ≠ 0 |

### Why the Born rule forces I₃ = 0

The reason is a one-line fact about the quadratic form of the Born rule. A three-path state is a *sum* of amplitudes, ψ = ψ_A + ψ_B + ψ_C. Its Born probability is the modulus squared:

|ψ|² = |ψ_A|² + |ψ_B|² + |ψ_C|² + 2 Re(ψ_A*ψ_B + ψ_A*ψ_C + ψ_B*ψ_C).

Squaring a sum produces only *self-terms* and *pairwise* cross-terms — never a genuine three-way term. The inclusion–exclusion residue in I₃ is built precisely to cancel the self-terms and the pairwise terms, so it leaves zero. Every higher order vanishes for the same reason: |·|² is quadratic, so nothing beyond pairwise ever appears. That quadratic-form fact is the entire content of "the Born rule forbids higher-order interference." Its theoretical ancestor is Gleason's theorem (1957), which fixes the quadratic measure from the Hilbert-space structure in dimension ≥ 3.

Sorkin's point is that nothing *a priori* privileges order 2. That quantum mechanics sits exactly one rung above the classical is an empirical fact, to be measured — which is what makes κ interesting.

## The Operational Parameter κ

I₃ (also written as the Sorkin parameter ε) is the measured value of the third-order residue. Because a raw residue carries units and scale, experiments report a **normalised** form: κ ≡ I₃ divided by a reference such as the maximum pairwise interference or the central-maximum intensity, so that "how close to zero" is scale-free. When comparing published bounds, the normalisation matters and should be stated explicitly — a figure quoted as a *bound relative to pairwise interference* is a different quantity from the *statistical uncertainty on κ*, and the two can differ by an order of magnitude even for the same experiment.

"The Born rule is tested" then means, concretely, **κ has been bounded near zero:**

- **Sinha, Couteau, Jennewein, Laflamme & Weihs (2010, *Science*)** ran a single-photon triple-slit experiment and, in the words of their abstract, "bounded the magnitude of three path interference to less than 10⁻² of the expected two-path interference." This is the landmark number and the cleanest to explain.
- **Kauten, Keil, Kaufmann, Pressl, Brukner & Weihs (2017, *New J. Phys.*)** used a five-path optical interferometer to tighten the bound to more than four orders of magnitude below the expected pairwise interference — roughly κ ~ 10⁻⁴ — refining the earlier optical bound by about two orders of magnitude.

An article or claim invoking this evidence should replace any vague "the Born rule is well-tested" with the precise version: κ ≲ 10⁻² (Sinha) to ~10⁻⁴ (Kauten) *in the optical regime*.

## Relation to Site Perspective

The Map reads κ as the measured coordinate beneath three of its tenets, and marks that reading as its own — the physics above is school-neutral; what follows is the Map's interpretation.

**Tenet 2 (Minimal Quantum Interaction) — the measured quantity.** The Map's [[tenets#^minimal-quantum-interaction|second tenet]] proposes the smallest possible non-physical influence on quantum outcomes, and insists that influence respect the empirical record: no detectable Born-statistics violation. κ is *what "respect the Born statistics" means numerically*. The [[born-rule-and-the-consciousness-interface|corridor reading]] the Map endorses biases which single outcome is realised while leaving the ensemble Born measure — and so the Hilbert-space geometry Gleason's theorem fixes — intact. That construction is designed to leave κ untouched, which is why the Map treats its interaction as empirically indistinguishable from chance rather than as a predicted κ ≠ 0. The Sorkin parameter is the instrument against which "minimal" is checked.

**Tenet 4 (No Many Worlds) — what makes κ well-defined.** κ is a statement about *one* actual intensity pattern accumulating on a screen. It presupposes single-outcome actualisation: definite counts, one world's worth of clicks. The Map's [[tenets#^no-many-worlds|single-outcome ontology]] is the setting in which the third-order residue is a measured number rather than a branch-relative bookkeeping quantity, so κ and the No-Many-Worlds tenet share the same background posit of objective actualisation.

**Tenet 5 (Occam's Razor Has Limits) — the tested slice.** Every κ bound lives in a clean external apparatus: photons, cold atoms, molecules, collider particles. None is brain-internal, warm, wet, or on the coherence timescale a consciousness-interface proposal would need. The tested κ constrains post-quantum probability *in the tested regime* and is silent on a brain-internal deviation — precisely the [[sorkin-delta-brain-internal-analogues|Sorkin-Δ analogue]] argument that no clean neural counterpart of "blocking a slit" exists. This is the concrete, quantity-level form of Tenet 5's warning that a result's authority does not automatically extend past the slice in which it was earned. The slice is real and expanding (Sinha → Kauten, and proposals reaching toward collider timescales); it is never the whole space.

## Does a Nonzero Term Mean New Physics? {#reading-a-nonzero-term}

A naive reading treats any measured κ ≠ 0 as a Born-rule violation. The corrected reading, now settled in the literature, is that finite-size slits generate *non-classical looped trajectories* — Sawant, Samuel, Sinha, Sinha & Sinha (2014, *Phys. Rev. Lett.*) and the "exotic looped trajectories" work (Magaña-Loaiza et al., *Nature Communications*, 2016) — which add a small **apparent** κ that sits entirely within standard quantum mechanics once the paths are summed correctly. Published triple-slit anomalies have been attributed to these near-field effects, not to post-quantum probability. Any use of the Sorkin bound must carry this caveat or it will overstate the cleanliness of the test: I₃ = 0 is a claim about amplitudes summed over paths, and slit-geometry corrections must be modelled out before a residual counts as new physics. (Genuine higher-order interference *can* be engineered — Namdar et al. (2023, *Phys. Rev. A*) generate it in a nonlinear triple slit — but there the source is optical nonlinearity, not post-quantum probability, a boundary case worth keeping distinct.)

A second distinction guards against conflating operationalisations. Valentini & Varma (2025, *Phys. Rev. D*) is a **proposal**, not a completed measurement, and it targets a **different observable**: Born-rule linearity in spin/polarization *expectation values* at collider timescales (~10⁻²⁵ s), not the third-order interference term I₃. It reports no new numerical bound, and its author, Antony Valentini, is a pilot-wave theorist whose programme actively seeks Born-rule violations. Both lines test "Born-rule linearity," but via different quantities; a claim about the tested regime must state the observable, not merely a headline number. Extending the tested slice toward the shortest accessible timescales sharpens the Tenet-5 point rather than closing it.

## What a Nonzero I₃ Would Mean

A confirmed κ ≠ 0 would falsify standard quantum mechanics and place physics in a [[generalised-probabilistic-theories|generalised probabilistic theory]] beyond quantum mechanics — the post-quantum landscape the GPT framework maps. Sorkin's measure hierarchy is one concrete axis through that landscape: order 2 is quantum mechanics, order 3 is the nearest post-quantum neighbour along this particular direction. The two concepts interlock. Generalised probabilistic theories supply the *space of alternatives* and the reconstruction story for why quantum mechanics sits where it does; the Sorkin hierarchy supplies the *single measured coordinate* whose non-vanishing would eject physics from quantum mechanics along one specified direction. The theoretical result that no-signalling alone does not force the Born rule and the experimental result that κ ≈ 0 are complementary reasons — one structural, one empirical — that the Born rule holds in the tested regime.

For the Map, this is why κ is worth naming rather than leaving as a slogan. It converts "the Born rule is well-tested" into a quantity, a number, and a regime — and it marks the exact edge past which the brain-internal extrapolation the Map proposes departs from anything a laboratory has yet constrained.

## Further Reading

- [[born-rule-and-the-consciousness-interface]] — how corridor dualism biases which outcome is realised while leaving the Born measure intact
- [[brain-internal-born-rule-testing]] — what would make the corridor empirically superfluous
- [[sorkin-delta-brain-internal-analogues]] — translating the optical triple-slit test into neural tissue
- [[generalised-probabilistic-theories]] — the space of post-quantum theories a nonzero κ would enter
- [[tenets]] — the five foundational commitments

## References

1. Sorkin, R. D. (1994). Quantum Mechanics as Quantum Measure Theory. *Modern Physics Letters A*, 9(33), 3119–3127. arXiv:gr-qc/9401003. https://arxiv.org/abs/gr-qc/9401003
2. Sinha, U., Couteau, C., Jennewein, T., Laflamme, R., & Weihs, G. (2010). Ruling Out Multi-Order Interference in Quantum Mechanics. *Science*, 329(5990), 418–421. arXiv:1007.4193. https://arxiv.org/abs/1007.4193
3. Kauten, T., Keil, R., Kaufmann, T., Pressl, B., Brukner, Č., & Weihs, G. (2017). Obtaining tight bounds on higher-order interferences with a 5-path interferometer. *New Journal of Physics*, 19, 033017. arXiv:1508.03253. https://arxiv.org/abs/1508.03253
4. Sawant, R., Samuel, J., Sinha, A., Sinha, S., & Sinha, U. (2014). Nonclassical Paths in Quantum Interference Experiments. *Physical Review Letters*, 113, 120406.
5. Magaña-Loaiza, O. S., et al. (2016). Exotic looped trajectories of photons in three-slit interference. *Nature Communications*, 7, 13987.
6. Namdar, P., Jenke, P. K., Alonso Calafell, I., Trenti, A., Radonjić, M., Dakić, B., Walther, P., & Rozema, L. A. (2023). Experimental higher-order interference in a nonlinear triple slit. *Physical Review A*, 107, 032211. arXiv:2112.06965.
7. Valentini, A., & Varma, M. (2025). Towards a test of the Born rule in high-energy collisions. *Physical Review D*, 112, 112024. arXiv:2505.07510. https://arxiv.org/abs/2505.07510
8. Gleason, A. M. (1957). Measures on the Closed Subspaces of a Hilbert Space. *Journal of Mathematics and Mechanics*, 6(6), 885–893.
9. Southgate, A. & Oquatre-huit, C. (2026-03-15). The Born Rule and the Consciousness-Physics Interface. *The Unfinishable Map*. https://unfinishablemap.org/topics/born-rule-and-the-consciousness-interface/
10. Southgate, A. & Oquatre-huit, C. (2026-06-03). Sorkin-Δ Brain-Internal Analogues. *The Unfinishable Map*. https://unfinishablemap.org/topics/sorkin-delta-brain-internal-analogues/
