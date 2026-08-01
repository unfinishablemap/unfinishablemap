---
ai_contribution: 100
ai_system: claude-opus-5
concepts: []
created: 2026-07-31
date: '2026-07-31'
draft: false
lastmod: 2026-07-31 00:00:00+00:00
related_articles: []
title: 'Research Notes: Horizon Decoherence as a Unitary Rival to Objective Collapse'
---

# Research: Horizon Decoherence as a Unitary Rival to Objective Collapse

**Date**: 2026-07-31

**Method note**: the session's WebSearch budget (200 calls) was exhausted at the start of this task, so no general web searching was possible. All evidence below comes from direct fetches of the arXiv API, arXiv abstract pages, and full-text HTML (arXiv LaTeXML and ar5iv renderings) downloaded locally and searched by grep. This is the fallback the commission specified, and it is in some ways stronger than search: every quotation below was extracted from the raw source file and re-verified by a second independent grep against that file. Nothing here is sourced from an aggregator, a summary page, or the outer review that prompted the task. Where a claim is not verified, it is marked so.

## Executive Summary

The Danielson–Satishchandran–Wald (DSW) result is real, correctly cited in the Map, and more interesting than its one-line registration suggests. It shows that any Killing horizon — a black hole's, the Rindler horizon of an accelerated lab, or the cosmological horizon of de Sitter spacetime — decoheres a stationary quantum superposition in finite time, using nothing but unmodified quantum field theory on curved spacetime. No collapse postulate, no nonlinear term, no modification of the Schrödinger equation.

It does not, however, do what the Gemini outer review claimed. Two independent findings block that reading. **Conceptually**, DSW is a decoherence result in the strict technical sense: the papers frame their own question as whether a recombined superposition ends up *pure or mixed*, the phrase "measurement problem" appears zero times in either paper, and neither paper claims that a definite outcome is produced. The mixedness arises by tracing over degrees of freedom behind a causal horizon — an improper mixture, with the global state still pure and still unitary. That is precisely the structure the Map's fourth tenet objects to, not a substitute for it. **Quantitatively**, the effect is astronomically weak anywhere except within a few Schwarzschild radii of a black hole: about 10⁴³ years for an electron in a one-metre superposition at one astronomical unit from a solar-mass black hole, about 10³³ years for the same superposition in a lab accelerating at one *g*, and — decisively for the prebiotic question — a de Sitter cosmological-horizon decoherence time that DSW themselves say "will be much larger than the Hubble time" for any ordinary charge.

A third finding narrows the mechanism further. DSW's own 2024 follow-up establishes that a *static star* produces no such decoherence even though its exterior vacuum resembles a black hole's. So this is a horizon-specific effect rather than a general gravitational classicalising agent, which removes the route by which it might have made the early universe definite.

The mechanism is also under live dispute. Fahn and Pesci argue in *Physical Review D* that quantum-geometry effects suppress it to negligible values; Biggs and Trezzi argue that near-extremal black holes make the rate vanish outright. "Untested" is the right description, and the Map's existing one-sentence treatment is already well calibrated.

## Verification Status

| Claim | Status |
|---|---|
| DSW 2022 identifiers, authors, venue, abstract | **Verified** at arXiv:2205.06279 abstract page and ar5iv full text |
| DSW 2023 identifiers, authors, venue, abstract | **Verified** at arXiv:2301.00026 abstract page and arXiv HTML full text |
| Decoherence-time formulas and numerical estimates | **Verified** by grep against downloaded full text (LaTeX math recovered from alttext) |
| "measurement problem" absent from both papers | **Verified** — 0 occurrences in either full text |
| Follow-up and challenge papers (identifiers, titles, authors, venues) | **Verified** via arXiv API listing and abstract pages |
| Biggs–Trezzi and Fahn–Pesci target DSW specifically | **Verified** — both cite Danielson et al. by name in their reference lists / text |
| Citation counts, peer-review status of 2026 preprints | **Not verified** — no search budget; several 2026 items are preprints without journal refs |
| Whether any DSW author has publicly addressed the classicality-of-the-early-universe question | **Not verified** — not found in the material fetched, and not searched for directly |

## Key Sources

### Danielson, Satishchandran & Wald (2022) — "Black Holes Decohere Quantum Superpositions"

- **arXiv**: 2205.06279 [hep-th], submitted 12 May 2022, revised 28 Nov 2022
- **Journal**: *International Journal of Modern Physics D* **31**(14), 2241003 (2022); DOI 10.1142/S0218271822410036
- **Note**: third prize, 2022 Gravity Research Foundation Essay Competition — an essay, not a full technical paper. The technical treatment is the 2023 *PRD* paper.
- **Key points**:
  - A massive or charged body in spatial superposition sources a long-range field; the black hole horizon registers that field differently for each branch, acquiring which-path information via soft gravitons or photons.
  - Decoherence time for the electromagnetic case: `T_D ~ ε₀ħc⁶b⁶ / (G³M³q²d²)`, where *b* is the distance from the hole, *d* the superposition separation.
  - Numerically: "if our Sun were a black hole and if one separated an electron into two components one meter apart in a laboratory experiment on Earth, it would not be possible to maintain the coherence of the electron for more than 10⁴³ years. On the other hand, if this experiment were done at b=6GM/c², then T_D ~ 5 minutes."
- **Verified quote** (abstract): "We believe that the fact that a black hole will eventually decohere any quantum superposition may be of fundamental significance for our understanding of the nature of black holes in a quantum theory of gravity."
- **Significance of that quote**: the authors state their own stakes as *black holes and quantum gravity*. They do not claim significance for the measurement problem, for the classical limit, or for cosmology.
- **Tenet relation**: neutral-to-adverse on **No Many Worlds** — supplies mind-independent loss of interference but no branch selection.

### Danielson, Satishchandran & Wald (2023) — "Killing Horizons Decohere Quantum Superpositions"

- **arXiv**: 2301.00026 [hep-th], submitted 30 Dec 2022, revised 15 Jun 2023
- **Journal**: *Physical Review D* **108**, 025007 (2023); DOI 10.1103/PhysRevD.108.025007
- **Key points**:
  - Generalises from black holes to *any* Killing horizon, explicitly including the Rindler horizon of a uniformly accelerating lab and the de Sitter cosmological horizon.
  - The mechanism is a flux of soft horizon gravitons/photons; from the inertial perspective the same physics appears as radiation of high-frequency gravitons/photons to null infinity.
  - The effect is distinct from, and larger than, decoherence due to Unruh radiation.
  - Number of entangling photons grows *linearly* with the time T the superposition is held stationary: `⟨N⟩ ~ q²d²T/R_H³` (de Sitter, EM) and `⟨N⟩ ~ m²d⁴T/R_H⁵` (de Sitter, GR). Decoherence requires `⟨N⟩ ≳ 1`.
  - Analysis is for d=4 but applies to any d ≥ 4.
- **Verified quote** (abstract): "The Killing horizon thereby harvests \"which path\" information of quantum superpositions and will decohere any quantum superposition in a finite time."
  - This is the one span the Gemini review quoted, and it **is** verbatim. Confirmed by grep against the raw HTML.
- **Verified quote** (introduction, framing the paper's own question): "Will Alice be able to maintain the coherence of these components, so that, when recombined, the final state of her particle will be pure—or will decoherence have occurred, so that the final state of her particle will be mixed?"
  - This is the crux for the Map. The paper's own statement of what is at stake is *pure versus mixed*, not *superposed versus definite*.
- **Verified quote** (de Sitter section): "the decoherence time will be much larger than the Hubble time R_H/c unless q is extremely large relative to the Planck charge"
- **Tenet relation**: as above.

### Danielson, Satishchandran & Wald (2024) — "Local Description of Decoherence of Quantum Superpositions by Black Holes and Other Bodies"

- **arXiv**: 2407.02567, submitted 2 Jul 2024; *Physical Review D* **111**, 025014 (2025)
- **Key points**:
  - The decoherence can be described entirely by the local two-point function of the field inside Alice's lab, with no direct reference to the horizon.
  - Crucially, it explains "the lack of decoherence in the spacetime of a static star even though the vacuum state outside the star is similar in many respects to the Boulware vacuum around a black hole."
  - It then asks what a material body would need in order to *mimic* the black hole's effect.
- **Why this matters to the Map**: ordinary massive bodies do not do this. The effect tracks horizons, not mass or gravity as such. Any argument of the form "gravity decohered the early universe by this mechanism" needs a horizon in the relevant causal past, and needs the superposition held stationary for the requisite time.

### Danielson, Kudler-Flam, Satishchandran & Wald (2025) — "How to Minimize the Decoherence Caused by Black Holes"

- **arXiv**: 2501.04773; *Physical Review D* **112**, 025012 (2025)
- Derives protocols that minimise the decoherence. Relevant because a mechanism whose magnitude an experimenter can *strategically reduce* is not behaving like an objective collapse law; it behaves like an environmental coupling.

### Danielson & Satishchandran (2025) — "Horizons and Soft Quantum Information"

- **arXiv**: 2512.20754 [hep-th], 23 Dec 2025. No journal ref found.
- Extends the analysis using Tomita–Takesaki theory, unambiguous state discrimination and approximate quantum error correction; concludes a horizon decoheres its environment as though its interior were full of optimal observers. **Note**: this phrasing is a summarised paraphrase from the abstract page, not a grep-verified verbatim span — treat as unverified wording.

### Satishchandran (2025) — "Black Holes, Entanglement and Decoherence"

- **arXiv**: 2508.20171. Proceedings of GR24 / Amaldi16.
- Review by one of the original authors; identifies three interrelated mechanisms: entanglement with interior degrees of freedom, absorption of emitted entangling radiation, and interaction with quantum fluctuations of the hole's multipole moments sourced by ultra-low-frequency Hawking radiation.

## The Decoherence Times — Why Magnitude Decides This

All formulas below are verified verbatim from the source full texts.

| Setting | Formula | Numerical estimate |
|---|---|---|
| Electron, 1 m separation, 1 a.u. from a solar-mass black hole | `T_D ~ ε₀ħc⁶b⁶/(G³M³q²d²)` | ~10⁴³ years |
| Same electron at b = 6GM/c² (close orbit) | same | ~5 minutes |
| Electron, 1 m separation, lab accelerating at 1 g (Rindler) | `T_D ~ ε₀ħc⁶/(a³q²d²)` | ~10³³ years |
| Charged body, de Sitter cosmological horizon | `T_D ~ ħε₀R_H³/(q²d²)` | ≫ Hubble time for ordinary charge |
| Massive body, de Sitter cosmological horizon | `T_D^GR ~ ħR_H⁵/(Gm²d⁴)` | ≫ Hubble time |

The scaling is brutal. `b⁶` in the black hole case means the effect falls away as the sixth power of distance; the 10⁴³-year figure at one astronomical unit versus five minutes at six gravitational radii spans thirty-eight orders of magnitude. The de Sitter case is the one that bears directly on the prebiotic question, since a cosmological horizon is the only Killing horizon available to generic matter in the early universe, and DSW state plainly that its decoherence time exceeds the Hubble time.

There is a further structural constraint. The whole calculation assumes Alice maintains a *stationary* superposition in an otherwise perfectly isolated lab for a time T, with all ordinary environmental decoherence stipulated away. In the actual early universe ordinary environmental decoherence — photons, collisions, the CMB — dominates this effect by an unimaginable margin. DSW's result is best read as a statement about an irreducible *floor*: coherence cannot be maintained indefinitely even in principle, even with perfect isolation. That is a genuinely interesting foundational claim about the limits of quantum control. It is not a claim about what made the early universe look classical.

## What DSW Does and Does Not Show

### Does show

1. Loss of interference is forced by horizon structure alone, within standard QM + GR, with no modification to the Schrödinger equation.
2. The effect is universal in scope: any Killing horizon, any superposed charge or mass, any spacetime dimension ≥ 4.
3. Coherence has a fundamental in-principle ceiling, independent of experimental skill.
4. Soft-mode and memory-effect physics has observable consequences for quantum information, connecting infrared structure to decoherence.

### Does not show

1. **That any outcome becomes definite.** The final state is *mixed*. Mixedness here is obtained by tracing over field degrees of freedom that have crossed the horizon and are inaccessible to the exterior observer — an improper mixture. The global state remains pure and unitarily evolving. Nothing removes a branch.
2. **That the measurement problem is addressed.** The phrase does not appear in either paper. The word "definite" appears once in each, and in the 2023 paper it refers to the *spin measurement Alice uses to detect the decoherence*, not to outcome selection.
3. **That collapse models are refuted.** DSW and objective collapse are answers to different questions. Objective reduction claims a definite outcome is produced; DSW computes a coherence budget. A universe governed by gravitational OR would also exhibit horizon decoherence.
4. **That the effect is cosmologically significant.** Its own authors' numbers put the cosmological-horizon decoherence time above the Hubble time.
5. **That it is settled physics.** See below.

## Live Contestation (2023–2026)

The mechanism is actively disputed in the peer-reviewed literature, which matters for how confidently the Map should treat it.

| Paper | Identifier / venue | Bearing |
|---|---|---|
| Gralla & Wei, "Decoherence from Horizons: General Formulation and Rotating Black Holes" | arXiv:2311.11461 | Extends to arbitrary Killing horizons and Kerr; reports the extremal electromagnetic case vanishes |
| Wilson-Gerow, Dugad & Chen, "Decoherence by warm horizons" | *Phys. Rev. D* **110**, 045002 (2024) | Recasts DSW via an Unruh–DeWitt detector and the fluctuation–dissipation theorem; a local, thermal reading |
| Li, "Decoherence of quantum superpositions by Reissner–Nordström black holes" | arXiv:2411.04734 | Effect vanishes for extremal black holes via a Meissner-like effect |
| Fahn & Pesci, "Effects of quantum geometry on the decoherence induced by black holes" | *Phys. Rev. D* **112**, L121502 (2025) | **Challenge**: minimal-length/minimal-area quantum geometry limits the horizon-induced decoherence "to negligibly small values" |
| Fahn & Pesci, "Horizon quantum geometries and decoherence" | *Phys. Rev. D* **112**, 124036 (2025) | **Challenge**: discretised horizon geometry strongly reduces or eliminates the effect |
| Biggs & Trezzi, "Not all black holes decohere quantum superpositions" | arXiv:2605.23880 (May 2026), preprint | **Challenge**: near-extremal black holes, quantum gravity effects make the decoherence rate vanish; a spin-induced energy gap in the black hole spectrum. Above the gap the rate is nonzero but still suppressed — "these quantum gravity effects always enhance the coherence of the superposition" |
| Batista, Landulfo, Mann & Matsas, "Nonperturbative Danielson–Satishchandran–Wald Decoherence with Unruh–DeWitt detectors" | arXiv:2605.00956 (May 2026), preprint | Nonperturbative test of the mechanism |
| Ireland, "Is Gravity Always Enough to Yield a Classical Universe?" | arXiv:2604.01283 (Apr 2026), Gravity Research Foundation essay | Argues gravitational and horizon decoherence are **not always sufficient** for a classical universe; non-linear perturbation dynamics may leave surviving non-classical features in observables |

One deflationary note from the Biggs–Trezzi introduction is worth recording: they observe that in the electromagnetic case the black hole's decoherence rate is comparable to that of ordinary matter, and that it is easy to find ordinary matter with the same effective "resistivity" as the hole. On that reading the horizon is not doing anything qualitatively exotic in the EM case; it behaves like a dissipative environment.

## Assessing the Outer Reviewer's Claim

The commissioning synthesis records Gemini 2.5 Pro as asserting that DSW "dissolves the prebiotic-collapse argument outright." Established independently from the primary literature, that claim does not hold, for two separable reasons — and either one alone is sufficient.

**First, the conceptual gap.** DSW yields a mixed reduced density matrix. The prebiotic-collapse argument asks what made outcomes *definite* before observers existed. Decoherence answers why branches stop interfering; it does not answer why one branch obtains. This is not the Map defending itself with a convenient distinction — it is the framing DSW themselves use ("pure ... or ... mixed"), and it is the standard reading in the decoherence literature, already recorded in the Map's own `concepts/decoherence` material and in the Stanford Encyclopedia entry on decoherence.

**Second, the quantitative gap.** Even granting a reading on which suppression of interference is all the prebiotic argument needs, the cosmological-horizon decoherence time exceeds the Hubble time by the authors' own estimate. The mechanism is too weak, by many orders of magnitude, to be the agent that classicalised the early universe.

**What is fair to concede.** The reviewer identified a genuinely under-discussed piece of physics, correctly named the authors, correctly described the mechanism (soft gravitons/photons through a horizon, which-path information, no modification to the Schrödinger equation), and quoted the 2023 abstract verbatim. The finding is real; only the strength of the conclusion is wrong. This fits the pattern the synthesis flagged — a reviewer whose sourcing is sound and whose inferential leaps are not.

## Corrections to the Commission's Premises

Two premises in the harvested task description are inaccurate, and both should be corrected before any downstream `expand-topic` task acts on them.

**1. The corpus does already engage DSW, accurately.** `obsidian/topics/penrose-gravity-induced-collapse-empirical-prospects.md` registers the mechanism in a full sentence in its "The No-Collapse Alternative" section, describes it correctly (Killing horizon, black hole or Rindler, soft gravitons and photons, which-path information, finite time, no modification to the Schrödinger equation), and states that "The effect is untested, and yields a mixed density matrix." That is precisely the calibration this research supports. The task description's "the mechanism has no treatment anywhere in the corpus" understates what is there.

**2. `concepts/prebiotic-collapse.md` does address the decoherence rival.** The task asserts that grepping it for `decoher` returns zero matches. It returns **14** matches in the body. The article carries a section headed "Decoherence Naturalization" that states the mainstream position and answers it, including a quoted 2025 review: "After the basis is chosen and quantum superpositions are suppressed, the system still remains in a mixture of possible outcomes. Decoherence does not tell how and why only one of these outcomes is measured." The words `unitary`, `no-collapse` and `rival` do indeed return zero — the vocabulary differs — but the *position* is present and answered.

The real gap is therefore much narrower than commissioned: the article addresses *environmental* decoherence as the no-collapse rival but not the *horizon* variant, and the reply it already deploys transfers to DSW without modification. This is the "narrow grep of my own words" failure mode — the probe searched for the vocabulary a new article would use rather than the vocabulary the existing article does use.

## Potential Article Angles

**Recommendation: do not create a new article.** Three considerations converge on this.

1. `topics/` is at 319/320 and `concepts/` at 318/320. Spending one of the last two slots on a mechanism whose own authors put its cosmological decoherence time above the Hubble time is poor allocation.
2. The material is paragraph-scale. Its entire bearing on the Map is a sharpening of a reply the corpus already makes.
3. A standalone article would create pressure to overstate the mechanism's significance to justify its existence — the exact failure the commission warned against, in mirror image.

**Preferred: two targeted additions to existing articles.**

- **`concepts/prebiotic-collapse.md`, in the existing "Decoherence Naturalization" section.** Add two or three sentences noting that the strongest form of the no-collapse rival is not environmental decoherence but horizon decoherence, which needs no environment at all and no collapse postulate; then note that its cosmological decoherence time exceeds the Hubble time, and that it delivers a mixed state rather than a definite outcome — so the section's existing reply covers it without alteration. This is honest engagement with the strongest version of the rival, and it *strengthens* the article rather than conceding to it.
- **`topics/penrose-gravity-induced-collapse-empirical-prospects.md`.** Optionally add the 2024 "Local Description" finding that a static star produces no such decoherence, which sharpens the existing sentence by showing the effect is horizon-specific. Length-neutral; the article is already near its threshold.

**If an article is nonetheless wanted later**, the defensible framing is *not* "horizon decoherence" as a physics explainer — the Map is not a physics site and would be competing with better sources. It would be **the distinction between interference-suppression and outcome-selection, illustrated through the strongest available case**. DSW is the ideal illustration precisely because it is the most fundamental, least hand-wavy decoherence mechanism anyone has produced — derived from horizon structure alone — and it *still* does not select an outcome. That is a genuine contribution the Map is positioned to make, and it would serve the fourth tenet directly.

## Relation to Site Tenets

- **Dualism** — neutral. DSW is silent on consciousness and does not bear on the mind-matter question either way.
- **Minimal Quantum Interaction** — mildly relevant. Horizon decoherence sets an in-principle floor on how long any superposition can be maintained, which is a constraint the interface proposal must respect. It does not close the interface, since the timescales involved are astronomically longer than any neural process.
- **Bidirectional Interaction** — neutral.
- **No Many Worlds** — this is where the action is, and where the reviewer's reading fails. DSW's mixed state is obtained by tracing over degrees of freedom behind a horizon. The global state stays pure; every branch survives; nothing is selected. Read as a complete story, horizon decoherence is *Everettian* in structure, which is what the fourth tenet rejects. So DSW does not supply what the prebiotic argument needs; it reproduces, in an unusually clean and fundamental form, exactly the gap the tenet identifies. Registering it as the strongest version of the rival and showing the standing reply still holds is a net gain for the tenet.
- **Occam's Razor Has Limits** — mildly supportive. The mainstream case against collapse leans on the claim that unitary evolution plus decoherence needs nothing further. DSW makes that case as strong as it can be made, and it still leaves outcome selection unexplained — an instance of simplicity being an unreliable guide where knowledge is incomplete.

## Gaps in Research

- **No general web search was possible.** Nothing here reflects philosophical commentary on DSW (in *Philosophy of Physics*, *Studies in HPMP*, PhilPapers, or SEP), only the physics literature reachable via arXiv. If DSW has been discussed by philosophers of physics, that discussion is unsampled and could be a better source for the Map than the primary physics.
- **Citation counts and reception were not measured.** "Landmark" was the reviewer's word; this research neither confirms nor refutes it. The follow-up volume observed on arXiv suggests real uptake, but that is an impression, not a metric.
- **Peer-review status of the 2026 preprints is unconfirmed.** Biggs–Trezzi, Batista et al. and Ireland are preprints without journal references at time of writing. The Fahn–Pesci challenges *are* published in *Physical Review D*.
- **The gravitational-case numbers are less well pinned than the electromagnetic ones.** DSW give explicit numerical estimates for the EM case and formula-only results for the GR case in the settings examined here.
- **Not investigated**: whether the near-horizon regime (five minutes at six gravitational radii) has any conceivable observational prospect. Almost certainly not, but it was not checked.
- **Not investigated**: whether the DSW authors or others have written on the classical-limit or early-universe implications directly. The Ireland essay is adjacent but was found by keyword listing rather than targeted search.

## Citations

1. Danielson, D. L., Satishchandran, G., & Wald, R. M. (2022). "Black Holes Decohere Quantum Superpositions." *International Journal of Modern Physics D*, 31(14), 2241003. arXiv:2205.06279. https://doi.org/10.1142/S0218271822410036
2. Danielson, D. L., Satishchandran, G., & Wald, R. M. (2023). "Killing Horizons Decohere Quantum Superpositions." *Physical Review D*, 108, 025007. arXiv:2301.00026. https://doi.org/10.1103/PhysRevD.108.025007
3. Danielson, D. L., Satishchandran, G., & Wald, R. M. (2025). "Local Description of Decoherence of Quantum Superpositions by Black Holes and Other Bodies." *Physical Review D*, 111, 025014. arXiv:2407.02567.
4. Danielson, D. L., Kudler-Flam, J., Satishchandran, G., & Wald, R. M. (2025). "How to Minimize the Decoherence Caused by Black Holes." *Physical Review D*, 112, 025012. arXiv:2501.04773.
5. Danielson, D. L., & Satishchandran, G. (2025). "Horizons and Soft Quantum Information." arXiv:2512.20754.
6. Satishchandran, G. (2025). "Black Holes, Entanglement and Decoherence." Proceedings of GR24 / Amaldi16. arXiv:2508.20171.
7. Danielson, D. L., Satishchandran, G., & Wald, R. M. (2022). "Gravitationally Mediated Entanglement: Newtonian Field vs. Gravitons." *Physical Review D*, 105, 086001. arXiv:2112.10798.
8. Gralla, S. E., & Wei, H. (2023). "Decoherence from Horizons: General Formulation and Rotating Black Holes." arXiv:2311.11461.
9. Wilson-Gerow, J., Dugad, A., & Chen, Y. (2024). "Decoherence by warm horizons." *Physical Review D*, 110, 045002. arXiv:2405.00804.
10. Li, R. (2024). "Decoherence of quantum superpositions by Reissner-Nordström black holes." arXiv:2411.04734.
11. Fahn, M. J., & Pesci, A. (2025). "Effects of quantum geometry on the decoherence induced by black holes." *Physical Review D*, 112, L121502. arXiv:2507.16911.
12. Fahn, M. J., & Pesci, A. (2025). "Horizon quantum geometries and decoherence." *Physical Review D*, 112, 124036. arXiv:2507.18709.
13. Biggs, A., & Trezzi, S. (2026). "Not all black holes decohere quantum superpositions." arXiv:2605.23880 (preprint).
14. Batista, L. B. N., Landulfo, A. G. S., Mann, R. B., & Matsas, G. E. A. (2026). "Nonperturbative Danielson-Satishchandran-Wald Decoherence with Unruh-DeWitt detectors." arXiv:2605.00956 (preprint).
15. Ireland, A. (2026). "Is Gravity Always Enough to Yield a Classical Universe?" Gravity Research Foundation 2026 essay. arXiv:2604.01283 (preprint).