---
title: "Research Notes - Generalised Probabilistic Theories and the Born Rule"
created: 2026-07-16
modified: 2026-07-16
human_modified:
ai_modified: 2026-07-16T02:58:37+00:00
draft: false
description: "Research on the generalised probabilistic theories (GPT) framework, the reconstruction programme, and how the Born rule appears within the landscape of possible theories — groundwork for a concepts/ home for a framework the Map currently defines only inline."
topics:
  - "[[born-rule-and-the-consciousness-interface]]"
concepts:
  - "[[causal-consistency-constraint]]"
  - "[[completeness-in-physics-under-dualism]]"
related_articles:
  - "[[tenets]]"
  - "[[brain-internal-born-rule-testing]]"
ai_contribution: 100
author:
ai_system: claude-opus-4-8
ai_generated_date: 2026-07-16
last_curated:
last_deep_review:
---

# Research: Generalised Probabilistic Theories and the Born Rule

**Date**: 2026-07-16
**Search queries used**:
- generalised probabilistic theories GPT framework Born rule reconstruction Hardy 2001 axioms
- Chiribella D'Ariano Perinotti 2011 informational derivation of quantum theory purification axiom
- Masanes Müller 2011 derivation of quantum theory from physical requirements axioms
- Barrett 2007 information processing in generalized probabilistic theories box world
- Plávala 2023 review general probabilistic theories introduction Physics Reports
- Hardy 2001 quantum theory from five reasonable axioms continuity
- Born rule unique probability rule no-signalling steering GPT geometric non-disturbance
- (WebFetch verification of Galley-Masanes 2018 at quantum-journal.org)

## Executive Summary

A generalised probabilistic theory (GPT) is an operational, convex-geometric framework in which *any* physical theory — classical probability, quantum mechanics, and a continuum of exotic alternatives — is specified by three ingredients: a convex state space, a set of measurement effects, and a probability rule pairing states with effects. Quantum mechanics is one point in this landscape; classical theory is another (a simplex); "boxworld" with Popescu-Rohrlich boxes is a third. The GPT framework is the setting for the *reconstruction programme* (Hardy 2001; Chiribella-D'Ariano-Perinotti 2011; Masanes-Müller 2011), which recovers the Hilbert-space formalism from short lists of operational axioms rather than postulating it. The Born rule enters this landscape as the specific probability rule quantum mechanics uses, and a subline of the programme asks what forces *that* rule rather than an alternative. The crucial and non-obvious finding for the Map: no-signalling *alone* does **not** force the Born rule (Galley-Masanes 2018 explicitly construct no-signalling-preserving modifications); the Born rule is forced only once **purification and/or local tomography** are added (Galley-Masanes 2018; Torres Alegre 2025 via steering). This sharpens — and slightly corrects the folk version of — the Map's "the Born rule binds any agent via relativistic causality" move: relativistic causality is necessary but not sufficient, and the eventual concepts/ article should carry that distinction as its spine.

## Distinctness from Existing Coverage

The Map currently defines GPTs **only inline** in [[causal-consistency-constraint]] ("A GPT specifies a state space, a set of measurement effects, and a probability function mapping state-effect pairs to numbers in [0, 1]") and references the framework across ≥5 files. That article is about **one theorem** (Torres Alegre's steering-based no-signalling result) and its use for the interface reading. It is not about the GPT framework as a framework: it does not cover convex-geometric structure, the state-space-as-convex-body picture, the reconstruction programme's history and axiom lists, boxworld / PR boxes, tomographic locality, or — most importantly — the *comparative* result that no-signalling is insufficient without purification. A concepts/ article on GPTs would be the heading-level home the framework currently lacks (every sibling formal apparatus the Map uses — categorical QM, Hilbert-space structure, SIC-POVMs — already has one). **Verdict: genuinely distinct and worth covering.** Confidence on worth-covering: high. Confidence it clears the cap contest (concepts at 318/320, competing with 2 sibling harvested subjects for ~2 slots): medium — see "Cap-Contest Note" below.

## Key Sources

### Plávala (2023) — the canonical modern review
- **URL**: https://arxiv.org/abs/2103.07469 (arXiv); published *Physics Reports* 1033 (2023), pp. 1–64, doi:10.1016/j.physrep.2023.09.001
- **Type**: Review article (Physics Reports)
- **Key points**:
  - Self-contained introduction to GPTs; tools are convex geometry, diagrammatic notation, and equations-as-diagrams.
  - GPTs generalise *both* finite-dimensional classical and quantum theory, and include exotic theories such as boxworld (containing PR boxes).
  - Frames the original motivation as answering "what is a physical theory?" in the context of axiomatising quantum theory; notes current research has shifted toward operational properties (what structure is needed to realise a given protocol).
- **Tenet alignment**: Neutral (a framework, not a metaphysics). Supplies the vocabulary the Map's Tenet-2 claims are stated in.
- **Provenance**: title/venue/pages verified via search; detailed claims from the search summary of the abstract/intro, not a full read.

### Hardy (2001) — the founding reconstruction
- **URL**: https://arxiv.org/abs/quant-ph/0101012
- **Type**: arXiv paper (foundational)
- **Key points**:
  - "Quantum Theory From Five Reasonable Axioms." Introduces GPTs in their modern operational form to re-axiomatise QM.
  - Two operational primitives: **dimension** N (max number of states distinguishable in a single-shot measurement) and **number of degrees of freedom** K. Quantum theory is characterised by K = N² (classical probability: K = N).
  - Axioms 1–4 are consistent with *both* classical and quantum theory; **Axiom 5** (existence of *continuous* reversible transformations between pure states) is what selects quantum over classical. Drop the word "continuous" and you land back in classical probability theory.
- **Tenet alignment**: Neutral. Shows QM is not an arbitrary formalism but a near-unique fixed point of operational axioms — relevant to Tenet 5 (Occam's-razor-has-limits): simplicity here is *derived structure*, not assumed.
- **Provenance**: arXiv ID and the classical/quantum-via-continuity point verified via search; the K=N² detail is standard textbook GPT knowledge but flagged as secondary.

### Chiribella, D'Ariano & Perinotti (2011) — the purification reconstruction
- **URL**: https://arxiv.org/abs/1011.6451 ; *Phys. Rev. A* 84, 012311 (2011)
- **Type**: Peer-reviewed (Phys. Rev. A)
- **Key points**:
  - Derives QM from **six informational principles**: causality, perfect distinguishability, ideal compression, local distinguishability, pure conditioning — these define a class of "standard" information-processing theories — plus **purification**, which singles out quantum theory *within* that class.
  - Recovers core QM structure (e.g. mixed states as convex combinations of perfectly distinguishable pure states) **without** assuming Hilbert space.
  - **Purification** = every mixed state is the marginal of a pure state on a larger system. This is exactly the assumption [[causal-consistency-constraint]] leans on; CDP is its canonical source.
- **Tenet alignment**: Neutral framework; purification is the axiom that does the load-bearing work in the Map's no-signalling argument, so this is the primary citation for that assumption.
- **Provenance**: arXiv ID + journal verified; "one postulate — purification — singles out quantum theory" verified via search summary of the abstract.

### Masanes & Müller (2011) — the requirements reconstruction
- **URL**: https://arxiv.org/abs/1004.1483 ; *New J. Phys.* 13, 063001 (2011)
- **Type**: Peer-reviewed (New Journal of Physics)
- **Key points**:
  - Derives the full QM formalism from five physical requirements on preparations, transformations, and measurements.
  - Explicitly analogises to special relativity (two postulates → Minkowski structure), which is the same rhetorical move the Map makes with "the Born rule is what relativistic causality requires."
  - Gives a group-theoretic explanation of *why* the qubit state space is the 3-dimensional Bloch ball, and flags natural routes to consistent *modifications* of QM (i.e. neighbouring GPTs).
- **Tenet alignment**: Neutral. The "consistent modifications" point matters for the Map: it means the space of near-quantum alternatives is populated, so ruling them out is substantive work, not a triviality.
- **Provenance**: arXiv ID + journal verified via search.

### Barrett (2007) — information processing in GPTs / boxworld
- **URL**: *Phys. Rev. A* 75, 032304 (2007) (arXiv:quant-ph/0508211)
- **Type**: Peer-reviewed (Phys. Rev. A)
- **Key points**:
  - Seminal operational treatment of GPTs as an information-processing framework; introduces **local tomography / global-state assumption** (the joint state is fixed by local fiducial measurement statistics).
  - Studies **boxworld**: a GPT with a *larger* state space but *smaller* effect space than QM, home to super-quantum PR-box correlations that still respect no-signalling.
- **Tenet alignment**: Neutral. Boxworld is the standard witness that **no-signalling does not entail quantum theory** — directly relevant to the Map's necessary-but-not-sufficient point below.
- **Provenance**: journal reference verified; arXiv number is the standard one for this paper but flagged (search returned the PRA citation, not the arXiv ID directly).

### Galley & Masanes (2018) — no-signalling is NOT enough *(the pivotal source)*
- **URL**: https://quantum-journal.org/papers/q-2018-11-06-104/ ; *Quantum* 2, 104 (2018)
- **Type**: Peer-reviewed (Quantum) — **verified by direct WebFetch of the publisher page**
- **Key points** (verbatim-checked against the publisher abstract):
  - Title: "Any modification of the Born rule leads to a violation of the purification and local tomography principles."
  - Result: any alternative to the Born measurement postulate makes **some mixed states fail to be reductions of a pure state** (purification breaks) and makes **local-measurement state tomography impossible** (local tomography breaks).
  - **Crucially**: it is *possible* to modify the Born rule **while preserving no-signalling** — "contrary to previous assumptions." Non-quantum measurement postulates exhibit an irreducible classicality.
- **Tenet alignment**: This is the source that keeps the Map honest. It shows the "no-signalling forces the Born rule" slogan is **too strong as stated**; what forces the Born rule is no-signalling *plus purification/local tomography*.
- **Quote (from abstract, publisher-verified)**: modifications of the Born rule are possible without signalling, but they "violate the purification and local tomography principles."

### Torres Alegre (2025) — the Map's existing anchor
- **URL**: https://arxiv.org/abs/2512.12636 (arXiv preprint, **not yet peer-reviewed**)
- **Type**: arXiv preprint
- **Key points**: Within GPTs satisfying purification, the Born rule is the unique probability rule compatible with no-signalling, enforced via **steering**; any nonlinear deviation lets a remote party signal. Distinguishes **geometric transition probability** (state-space structure) from **predictive probability** (experimental prediction) and shows no-signalling forces their relationship to be the identity.
- **Tenet alignment**: Aligns with Tenet 2 (Minimal Quantum Interaction) as a *form-fixer*, per the existing [[causal-consistency-constraint]] treatment — form not existence, derivational not empirical.
- **Provenance**: already cited in the corpus; note the **purification assumption is doing the real work** and Torres Alegre inherits exactly the Galley-Masanes gap (steering/purification is the extra ingredient beyond no-signalling).

### Extension: "Causal Rigidity of Born-Type Probability Rules in Infinite-Dimensional Operational Theories" (2026)
- **URL**: https://arxiv.org/abs/2602.09056 (arXiv preprint)
- **Type**: arXiv preprint
- **Key points**: Extends the "Born rule is the only no-signalling-compatible assignment in theories admitting normal steering" result to **infinite-dimensional** operational theories. A currency check for the Map: the Torres Alegre-style result is being generalised, not overturned.
- **Provenance**: arXiv ID surfaced in search; not read in full. Flag for verification before citing in an article.

## Major Positions / Framings

### The GPT framework itself (the concept the article should own)
- **Core content**: A single-system GPT = (state space Ω, effect space E, a pairing e(ω) ∈ [0,1]).
  - **State space** is a **convex set** (compact convex body); convexity encodes probabilistic mixing (you can prepare "ω₁ with prob p, ω₂ with prob 1−p").
  - **Pure states** = extreme points of the body; **mixed states** = interior points.
  - **Effects** are affine functionals from states to [0,1]; a measurement is a set of effects summing to the unit effect.
  - **The theory's "shape" is its geometry**: classical n-outcome theory is a **simplex** (n vertices, unique decomposition of every mixed state); the qubit is the **Bloch ball** (a sphere's worth of pure states, non-unique mixture decompositions — the geometric root of quantum weirdness); boxworld is a **square/hypercube**.
- **Why the Map cares**: it makes precise the claim "quantum mechanics is one probabilistic theory among many." The Born rule is not the definition of probability; it is *this theory's* probability rule, sitting at a specific geometric point.

### The reconstruction programme
- **Proponents**: Hardy; Chiribella-D'Ariano-Perinotti; Masanes-Müller; Barrett; Dakić-Brukner; Wilce; Höhn.
- **Core claim**: The Hilbert-space formalism (complex amplitudes, tensor products, the Born rule) is **derivable** from a handful of operational/informational axioms, rather than being a brute postulate.
- **Recurring load-bearing axioms**: tomographic/local tomography, continuous reversibility, purification, subspace/ideal-compression, perfect distinguishability.
- **Relation to Map tenets**: Directly supports the Map's use of the Born rule as a *derived* constraint (not a metaphysical add-on) while respecting Tenet 5: the derivations are *conditional* on axioms whose applicability to the brain-internal regime is untested. The programme shows QM's structure is forced *given the axioms* — it does not show the axioms hold everywhere.

### The Born-rule-selection subline (the Tenet-2 payload)
- **The naive claim** (what the Map's slogan risks asserting): "no-signalling forces the Born rule, so any agent — physical or non-physical — coupling to quantum outcomes is Born-constrained."
- **The corrected claim** (what the literature actually supports):
  1. No-signalling **alone** is *insufficient* — boxworld (Barrett 2007) is a no-signalling non-quantum theory, and Galley-Masanes (2018) exhibit no-signalling-preserving Born-rule modifications.
  2. The Born rule becomes **forced** once you add **purification** (CDP-style / Torres Alegre steering) and/or **local tomography** (Galley-Masanes).
  3. Therefore the correct Map statement is: *an agent coupling to quantum outcomes in a regime satisfying purification + local tomography (as physics does everywhere it has been tested) is Born-constrained on pain of signalling.* The constraint on a non-physical interface is exactly as strong as the applicability of those two structural axioms to the interface — no stronger.
- **Why this is an upgrade, not a retreat**: it converts a slightly-overstated slogan into a precise, defensible conditional, and it names the two axioms whose brain-internal status is the actual open question (which is exactly what [[brain-internal-born-rule-testing]] is about). It also gives the corridor's "geometric-non-disturbance minimal-intervention signature" a sharper reading: a selection-only interface preserves *the whole convex geometry* (state space + effects), not merely the marginal statistics — non-disturbance is a geometric, not just a statistical, condition.

## Key Debates

### Does no-signalling select the Born rule?
- **Sides**: Torres Alegre (2025) and the causal-rigidity line say yes *within purified/steering theories*; Galley-Masanes (2018) show no *if* you only assume no-signalling.
- **Core disagreement**: whether the selecting principle is relativistic causality *simpliciter* or relativistic causality *conjoined with* purification/local tomography.
- **Current state**: Effectively resolved in favour of the conjunction. The literature is consistent once you track which axioms each result assumes; the appearance of disagreement is an artefact of loose "no-signalling forces Born" summaries. **The eventual article must state the conjunction, not the slogan.**

### Why these axioms and not others? (the "reasonableness" debate)
- **Sides**: reconstruction programme (the axioms are physically well-motivated) vs. sceptics (the axioms are chosen with the destination — QM — in view; "reasonable" is doing covert work).
- **Relevance to Map**: a candour point aligned with the Map's [[evidential-status-discipline]] — the derivations are real mathematics but their *premises'* applicability to any concrete regime (especially the interface) is a separate, empirical question.

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1957 | Gleason's theorem | Born rule from Hilbert-space measure structure (dim ≥ 3); pre-GPT ancestor. |
| 1994 | Popescu-Rohrlich boxes | Super-quantum no-signalling correlations; the seed of boxworld. |
| 2001 | Hardy, "Five Reasonable Axioms" | Founds the modern operational/GPT reconstruction programme. |
| 2007 | Barrett, GPT information processing | Operationalises GPTs; boxworld, local tomography; no-signalling ≠ quantum. |
| 2011 | Chiribella-D'Ariano-Perinotti | Purification singles out QM among informational theories. |
| 2011 | Masanes-Müller | QM from five physical requirements; Bloch ball explained. |
| 2018 | Galley-Masanes | Born-rule modifications *can* preserve no-signalling; forced only with purification + local tomography. |
| 2023 | Plávala, Physics Reports review | Canonical modern synthesis of the framework. |
| 2025 | Torres Alegre (preprint) | Steering-based no-signalling selection of the Born rule (Map's current anchor). |
| 2026 | Causal Rigidity (preprint) | Extends the selection result to infinite dimensions. |

## Potential Article Angles

1. **"Generalised Probabilistic Theories" (recommended, concepts/).** The framework as such: convex state space / effects / probability rule; QM as one point among many; the simplex-vs-Bloch-ball-vs-square picture; the reconstruction programme; then a dedicated section — "Where the Born rule sits" — that states the *conjunction* result (no-signalling + purification/local tomography) and hands the Tenet-2 payload to [[causal-consistency-constraint]] and [[born-rule-and-the-consciousness-interface]] rather than re-arguing it. This is the general concept the harvest task asked for and is cleanly distinct from the inline theorem treatment.
2. **Alternative / narrower.** "Why no-signalling is not enough to fix the Born rule" — a corrective micro-article built around Galley-Masanes vs. Torres Alegre. Higher novelty but overlaps more with the existing [[causal-consistency-constraint]]; better folded in as a *section* of angle 1 than spun out separately (avoids the same over-specific trap the harvest task warns against).

When writing, follow `obsidian/project/writing-style.md`: front-load the three-ingredient definition and the QM-as-one-point framing (truncation resilience); use named-anchor summaries for the forward reference to the Born-rule-selection section; include only the background framed for the Map's dualist reading (the convex geometry matters *because* it makes the interface's non-disturbance condition geometric); and add the required "Relation to Site Perspective" section tying to Tenets 2, 4 (indexical identity / no-MWI: GPTs are agnostic on interpretation, which is a feature), and 5.

## Cap-Contest Note (for the operator)

- **Worth covering: high confidence.** GPT is the one sibling formal framework with no heading-level home, it is load-bearing for the Map's flagship Tenet-2 argument, and this note surfaces a substantive *correction* (no-signalling alone is insufficient) that improves the accuracy of ≥5 downstream files, not merely a restatement.
- **Cap pressure: medium confidence it should win a slot.** concepts is at 318/320. If forced to rank against the two sibling harvested subjects, this one has the strongest claim because (a) it fixes a live over-statement in existing published content and (b) it is a genuine framework-hub that multiple articles already lean on inline. Recommend prioritising it over any sibling subject that is a leaf-topic rather than a hub.
- **Downstream integration:** the eventual article should add inbound links from [[causal-consistency-constraint]] (replace the inline GPT definition with a "see [[generalised-probabilistic-theories]]" pointer, keeping a one-line gloss), [[born-rule-and-the-consciousness-interface]], [[completeness-in-physics-under-dualism]], and [[brain-internal-born-rule-testing]]. Queue a cross-review after expansion.

## Gaps in Research

- **Not read in full**: every source here was assessed via search summaries plus one publisher WebFetch (Galley-Masanes). The convex-geometry specifics (Bloch ball = qubit, simplex = classical, square = boxworld) are standard GPT textbook facts but were not line-verified against a primary text in this pass; verify against Plávala (2023) §2–3 before publishing.
- **Barrett 2007 arXiv ID** (quant-ph/0508211) inferred from standard citation, not directly returned by search — verify.
- **Torres Alegre and Causal-Rigidity are preprints** — flag evidential status per [[evidential-status-discipline]]; neither is peer-reviewed.
- **Open for the article, not this note**: precisely how much of purification + local tomography a *non-physical* interface can be assumed to satisfy is the substantive interface question; this note establishes only that those are the two axioms on which the whole "any agent is Born-constrained" claim rests.

## Citations

1. Hardy, L. (2001). Quantum Theory From Five Reasonable Axioms. *arXiv:quant-ph/0101012*. https://arxiv.org/abs/quant-ph/0101012
2. Barrett, J. (2007). Information processing in generalized probabilistic theories. *Physical Review A*, 75, 032304. (arXiv:quant-ph/0508211 — verify.)
3. Chiribella, G., D'Ariano, G. M., & Perinotti, P. (2011). Informational derivation of quantum theory. *Physical Review A*, 84, 012311. *arXiv:1011.6451*. https://arxiv.org/abs/1011.6451
4. Masanes, L., & Müller, M. P. (2011). A derivation of quantum theory from physical requirements. *New Journal of Physics*, 13, 063001. *arXiv:1004.1483*. https://arxiv.org/abs/1004.1483
5. Galley, T. D., & Masanes, L. (2018). Any modification of the Born rule leads to a violation of the purification and local tomography principles. *Quantum*, 2, 104. https://quantum-journal.org/papers/q-2018-11-06-104/ (publisher-verified)
6. Plávala, M. (2023). General probabilistic theories: An introduction. *Physics Reports*, 1033, 1–64. *arXiv:2103.07469*. https://arxiv.org/abs/2103.07469
7. Torres Alegre, E. O. (2025). Causal Consistency Selects the Born Rule: A Derivation from Steering in Generalized Probabilistic Theories. *arXiv:2512.12636*. https://arxiv.org/abs/2512.12636 (preprint, not peer-reviewed).
8. Causal Rigidity of Born-Type Probability Rules in Infinite-Dimensional Operational Theories (2026). *arXiv:2602.09056*. https://arxiv.org/abs/2602.09056 (preprint — verify authorship/details before citing).
9. Gleason, A. M. (1957). Measures on the Closed Subspaces of a Hilbert Space. *Journal of Mathematics and Mechanics*, 6(6), 885–893.
