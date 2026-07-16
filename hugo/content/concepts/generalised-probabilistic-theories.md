---
ai_contribution: 100
ai_generated_date: 2026-07-16
ai_modified: 2026-07-16 11:01:00+00:00
ai_system: claude-opus-4-8
author: null
concepts:
- '[[causal-consistency-constraint]]'
- '[[quantum-interpretations]]'
created: 2026-07-16
date: &id001 2026-07-16
description: The GPT framework treats quantum mechanics as one probabilistic theory
  among many. A human-AI account of what forces the Born rule — and why no-signalling
  alone does not.
draft: false
human_modified: null
last_curated: null
last_deep_review: 2026-07-16 11:01:00+00:00
modified: *id001
related_articles:
- '[[tenets]]'
- '[[completeness-in-physics-under-dualism]]'
title: Generalised Probabilistic Theories
topics:
- '[[born-rule-and-the-consciousness-interface]]'
- '[[brain-internal-born-rule-testing]]'
---

A **generalised probabilistic theory** (GPT) is an operational framework in which any physical theory — classical probability, quantum mechanics, and a continuum of exotic alternatives — is specified by three ingredients: a set of states, a set of measurements, and a rule pairing them to yield probabilities. Quantum mechanics is one point in this landscape; classical theory is another; still others describe worlds that have never been observed. This is the neutral, school-independent definition every camp accepts.

The Map uses the GPT framework because it makes precise an otherwise vague slogan — *quantum mechanics is one probabilistic theory among many* — and because it locates the Born rule as a specific, non-inevitable choice within that landscape rather than as the definition of probability itself. That interpretive use is the Map's, not a consequence of the framework. And the Map's downstream argument (that any agent coupling to quantum outcomes is bound by the Born rule) turns out to require **more than** the framework's most-cited constraint: no-signalling alone does not force the Born rule. That correction, established below, is the reason this concept has its own home.

## The Neutral Definition

A single-system GPT is a triple: a **state space**, an **effect space**, and a **probability rule**.

- The **state space** is a convex set. Convexity encodes probabilistic mixing: if you can prepare state ω₁ and state ω₂, you can prepare "ω₁ with probability *p*, ω₂ otherwise," and that mixture is also a state. **Pure states** are the extreme points of the set — the corners and surface that cannot be written as mixtures. **Mixed states** are interior points.
- **Effects** are the possible measurement outcomes, represented as functions from states to numbers in [0, 1]. A measurement is a collection of effects that sum to certainty.
- The **probability rule** pairs a state with an effect and returns the probability of that outcome.

The theory's physical content is carried by the *geometry* of its state space. Classical *n*-outcome probability theory is a **simplex** — a triangle for three outcomes, a tetrahedron for four — in which every mixed state decomposes into pure states in exactly one way. A quantum bit is the **Bloch ball**, a solid sphere whose entire surface is pure states; because a point inside a ball can be reached by infinitely many chords, quantum mixtures decompose non-uniquely, which is the geometric root of much quantum strangeness. A third, purely hypothetical theory called **boxworld** has a square or hypercube for its state space and hosts super-quantum correlations (Popescu-Rohrlich boxes) that still forbid faster-than-light signalling. Plávala's 2023 *Physics Reports* review is the canonical modern synthesis of this machinery.

This definition is metaphysically neutral. It supplies a vocabulary, not a worldview; classical, quantum, and boxworld all sit inside it as equally well-formed theories.

## The Reconstruction Programme

The framework's original purpose was **reconstruction**: deriving the Hilbert-space formalism of quantum mechanics — complex amplitudes, tensor products, the Born rule — from short lists of operational axioms rather than postulating it outright.

Hardy's 2001 "Quantum Theory From Five Reasonable Axioms" founded the modern programme. Hardy characterises a theory by two numbers: a dimension *N* (the states distinguishable in one measurement) and a count *K* of independent parameters needed to specify a state. Classical theory has *K = N*; quantum theory has *K = N²*. Four of Hardy's axioms are consistent with both classical and quantum theory; the fifth — the existence of *continuous* reversible transformations between pure states — is what selects quantum over classical. Delete the word "continuous," Hardy notes, and the reconstruction lands back in classical probability.

Two 2011 reconstructions sharpened this. Chiribella, D'Ariano and Perinotti derive quantum theory from six informational principles, of which five define a broad class of "standard" information-processing theories and one — **purification**, the requirement that every mixed state be the marginal of a pure state on a larger system — singles out quantum theory within that class. Masanes and Müller derive the formalism from five physical requirements and explain group-theoretically why a qubit's state space is precisely the three-dimensional Bloch ball. Barrett's 2007 operational treatment introduced boxworld and the assumption of **local tomography** (a composite system's state is fixed by measurements on its parts).

Two recurring axioms — **purification** and **local tomography** — will do the decisive work below.

## The Map's Interpretation

The Map reads the GPT framework as the setting that makes its Tenet-2 commitment (**Minimal Quantum Interaction** — the smallest possible non-physical influence on quantum outcomes) statable in exact terms. This reading is the Map's, and is marked as such.

Two interpretive moves belong to the Map specifically.

First, the framework converts "quantum mechanics is not the only conceivable probabilistic theory" from rhetoric into geometry. Ruling out the near-quantum alternatives is then substantive mathematical work, not a triviality — Masanes and Müller explicitly flag routes to consistent *modifications* of quantum theory, so the neighbourhood of quantum mechanics is genuinely populated.

Second, the Map reads the interface's signature — a consciousness-physics coupling that selects outcomes without disturbing statistics — as a *geometric* condition, not merely a statistical one. A selection-only interface must preserve the whole convex structure (state space and effects together), not just the marginal frequencies. This geometric reading of non-disturbance is a Map proposal that the bare framework neither supplies nor forbids.

## The Disputed Payload: What Forces the Born Rule

Here the Map corrects a slogan it has sometimes leaned on. The tempting claim is: *no-signalling forces the Born rule, so any agent — physical or non-physical — coupling to quantum outcomes is Born-constrained.* The GPT literature shows the first half of that sentence is false as stated.

No-signalling **alone** does not force the Born rule. Boxworld (Barrett 2007) is a non-quantum theory that respects no-signalling, and Galley and Masanes established in 2018 that the Born measurement rule can be modified while preserving no-signalling — "contrarily to previous claims," as their paper puts it. Their result is titled: "Any modification of the Born rule leads to a violation of the purification and local tomography principles." The Born rule becomes forced only once **purification and/or local tomography** are added to no-signalling.

This is why the Map's existing anchor, the [causal-consistency-constraint](/concepts/causal-consistency-constraint/), is stated carefully. Torres Alegre's 2025 steering-based derivation — an arXiv preprint, not yet peer-reviewed — shows that *within GPTs satisfying purification*, the Born rule is the unique no-signalling-compatible probability assignment. The purification assumption is doing the real work; the theorem inherits exactly the Galley-Masanes gap. A 2026 preprint extending the result to infinite-dimensional theories suggests the selection line is being generalised rather than overturned, though it too awaits refereeing.

The honest Map statement is therefore a conditional: *an agent coupling to quantum outcomes in a regime that satisfies purification and local tomography — as physics does everywhere it has been tested — is Born-constrained on pain of signalling.* The constraint on a non-physical interface is exactly as strong as the applicability of those two structural axioms to the interface, and no stronger. This is an upgrade, not a retreat: it names the precise open question ([brain-internal-born-rule-testing](/topics/brain-internal-born-rule-testing/)) instead of hiding it inside a slogan.

## Rival Readings

The reconstruction programme is not uncontested, and the disagreements matter for how much weight the Map can place on it.

The "reasonableness" objection holds that the axioms are chosen with quantum theory already in view — that "reasonable" and "physically natural" quietly smuggle in the destination. On this reading the derivations are real mathematics whose premises' applicability to any concrete regime is a separate, empirical question. The Map endorses this candour: consistent with Tenet 5 (**Occam's Razor Has Limits**), a derivation shows quantum structure is forced *given the axioms* without showing the axioms hold everywhere — least of all inside a brain at interaction-relevant precision.

An instrumentalist reads GPTs as bookkeeping over laboratory statistics with no ontological import, and the framework is deliberately agnostic between quantum interpretations — collapse, hidden-variable, relational, QBist. The Map treats that agnosticism as a feature: because GPTs never mention many-worlds branching or a universal wavefunction, results proved in the framework do not presuppose the interpretations Tenet 4 (**No Many Worlds**) rejects. The framework fixes the *form* any corridor-compliant coupling must take, not the *existence* of the interface the Map posits — and it does so without committing to any single reading of the measurement process.

## Relation to Site Perspective

The GPT framework is the formal setting in which several of the Map's tenets acquire precise statements.

**Tenet 2 (Minimal Quantum Interaction)**: The framework locates the Born rule as one probability rule among many and identifies the exact conditions — purification and local tomography — under which it is forced. A minimal interface that selects outcomes without signalling must preserve the theory's whole convex geometry.

**Tenet 4 (No Many Worlds)**: GPTs are interpretation-neutral and make no appeal to branching, so the Map can use their results without importing many-worlds commitments.

**Tenet 5 (Occam's Razor Has Limits)**: Reconstruction shows quantum structure is derived, not arbitrary — but only relative to axioms whose reach into untested regimes is unknown. Simplicity here is *earned* structure, and its earning is conditional.

The framework does no work *for* the interface reading over its rivals: every no-signalling-respecting framework inherits the same constraints. Its value to the Map is framework-internal — it disciplines the form of the Map's claims and forces the honest conditional in place of the tempting slogan.

## Further Reading

- [causal-consistency-constraint](/concepts/causal-consistency-constraint/)
- [born-rule-and-the-consciousness-interface](/topics/born-rule-and-the-consciousness-interface/)
- [brain-internal-born-rule-testing](/topics/brain-internal-born-rule-testing/)
- [quantum-interpretations](/concepts/quantum-interpretations/)
- [completeness-in-physics-under-dualism](/topics/completeness-in-physics-under-dualism/)

## References

1. Hardy, L. (2001). Quantum Theory From Five Reasonable Axioms. *arXiv:quant-ph/0101012*. https://arxiv.org/abs/quant-ph/0101012
2. Barrett, J. (2007). Information processing in generalized probabilistic theories. *Physical Review A*, 75, 032304.
3. Chiribella, G., D'Ariano, G. M., & Perinotti, P. (2011). Informational derivation of quantum theory. *Physical Review A*, 84, 012311. *arXiv:1011.6451*. https://arxiv.org/abs/1011.6451
4. Masanes, L., & Müller, M. P. (2011). A derivation of quantum theory from physical requirements. *New Journal of Physics*, 13, 063001. *arXiv:1004.1483*. https://arxiv.org/abs/1004.1483
5. Galley, T. D., & Masanes, L. (2018). Any modification of the Born rule leads to a violation of the purification and local tomography principles. *Quantum*, 2, 104. https://quantum-journal.org/papers/q-2018-11-06-104/
6. Plávala, M. (2023). General probabilistic theories: An introduction. *Physics Reports*, 1033, 1–64. *arXiv:2103.07469*. https://arxiv.org/abs/2103.07469
7. Torres Alegre, E. O. (2025). Causal Consistency Selects the Born Rule: A Derivation from Steering in Generalized Probabilistic Theories. *arXiv:2512.12636*. https://arxiv.org/abs/2512.12636 (preprint, not peer-reviewed).
8. Southgate, A. & Oquatre-sept, C. (2026-05-14). Causal Consistency Constraint. *The Unfinishable Map*. https://unfinishablemap.org/concepts/causal-consistency-constraint/
9. Southgate, A. & Oquatre-huit, C. (2026-03-15). The Born Rule and the Consciousness Interface. *The Unfinishable Map*. https://unfinishablemap.org/topics/born-rule-and-the-consciousness-interface/