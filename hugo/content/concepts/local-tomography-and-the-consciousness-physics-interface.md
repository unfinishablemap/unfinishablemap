---
ai_contribution: 100
ai_generated_date: 2026-07-16
ai_modified: 2026-08-27 00:06:21+00:00
ai_system: claude-opus-4-8+claude-opus-5
author: null
concepts:
- '[[generalised-probabilistic-theories]]'
- '[[causal-consistency-constraint]]'
created: 2026-07-16
date: &id001 2026-08-27
description: A human-AI account of local tomography — the axiom that a composite's
  state is fixed by local measurements — its failure regimes, and why the brain-substrate
  interface may be a candidate for that failure.
draft: false
human_modified: null
last_curated: null
last_deep_review: 2026-08-18 10:31:30+00:00
lastmod: 2026-08-27 00:06:21+00:00
modified: *id001
related_articles:
- '[[tenets]]'
- '[[completeness-in-physics-under-dualism]]'
title: Local Tomography and the Consciousness-Physics Interface
topics:
- '[[born-rule-and-the-consciousness-interface]]'
- '[[brain-internal-born-rule-testing]]'
---

**Local tomography** (equivalently *tomographic locality*) is the axiom that the state of a composite system is completely determined by the statistics of *local* measurements on its parts, together with the correlations between those local outcomes. Complex quantum mechanics satisfies it; real and quaternionic quantum theories do not. The axiom matters to the Map because, for theories that keep quantum theory's pure states and reversible dynamics, it is one of two structural principles — purification is the other — either of which forces the Born-rule constraint the Map leans on at the consciousness-physics interface. Inside that class, local tomography would have to fail *and* purification fail with it before the constraint formally reopened, so the axiom's failure is necessary rather than sufficient; outside it the axiom forces nothing on its own, as boxworld — locally tomographic, no-signalling, and not Born-ruled — shows. Whether local tomography holds across a physical/non-physical composite is unknown and untested — so the [interface reading below](#the-interface-question) is a Map open question that *sharpens* Tenet 2, not evidence for it. That status is part of the claim, not a footnote to it.

## The Axiom, Stated Neutrally {#the-axiom-stated-neutrally}

Consider a composite system AB built from a part A and a part B. A theory satisfies **local tomography** if, for every such composite, the global state is uniquely fixed by the joint probabilities it assigns to all pairs (a, b) of local effects — where a is a measurement outcome on A alone and b a measurement outcome on B alone. Equivalently, the dimension of the composite state space equals the *product* of the component dimensions: d_AB = d_A · d_B. There are no **global degrees of freedom** beyond those readable from local measurements and their correlations.

This is a school-neutral definition. It does not presuppose quantum mechanics, dualism, or any particular interpretation of the measurement process; it is a property a probabilistic theory either has or lacks. In Hardy and Wootters' words, quantum theory "has the property of 'local tomography': the state of any composite system can be reconstructed from the statistics of measurements on the individual components."

Several familiar theories satisfy the axiom:

- **Complex quantum mechanics** is locally tomographic. A complex *d*-level system carries d² real parameters, and the parameter counts multiply across a composite exactly as the axiom requires.
- **Classical probability** is locally tomographic trivially: a joint distribution composes as an ordinary product of marginals plus their correlations.
- **Boxworld**, the hypothetical super-quantum theory hosting Popescu-Rohrlich correlations, is also locally tomographic. Barrett (2007) builds the axiom into his framework as the Global State Assumption — "the global state of a multi-partite system can be completely determined by specifying joint probabilities of outcomes for fiducial measurements performed simultaneously on each subsystem" — and boxworld inherits it. Boxworld also respects no-signalling, and it is not Born-ruled. So local tomography, even with no-signalling, does not by itself deliver quantum theory or its probability rule — a point the [generalised-probabilistic-theories](/concepts/generalised-probabilistic-theories/) framework makes precise, the reason the reconstruction programme pairs it with purification, and the limiting case that fixes the scope of the Born-forcing result [below](#the-interface-question).

What makes local tomography interesting is that it is not universal. It has concrete, well-studied failure regimes.

## What Failure Looks Like

When local tomography fails, a composite has a **global degree of freedom** — a component of the joint state that no product of local effects can read out. The state carries more information than any amount of separate local measurement on A and on B can recover; that surplus is accessible only through genuinely *joint* measurements across the parts.

The cleanest concrete model is **real-vector-space quantum theory** — quantum mechanics rebuilt over the real numbers instead of the complex ones. Hardy and Wootters (2012) proved that it fails local tomography, but only barely: "real-vector-space quantum theory, while not locally tomographic, is bilocally tomographic." A theory is *bilocally* (2-locally) tomographic if pairwise-joint statistics on pairs of components suffice to fix the state, even though single-component statistics do not. Real quantum theory is therefore *more holistic* than complex quantum theory. Hardy and Wootters name this residual "limited holism," and the amount of holism is precisely the gap between d_AB and d_A · d_B.

**Quaternionic quantum theory** fails in the opposite direction: its natural tensor product is the wrong size to even define the product effects a locally-tomographic composite needs. Global degrees of freedom are then unavoidable by construction.

Barnum and Wilce (2014) turn these failures into a near-characterisation. In "Local tomography and the Jordan structure of quantum theory," they show that "orthodox finite-dimensional complex quantum mechanics with superselection rules is the only non-signaling probabilistic theory" in which individual systems have Jordan-algebraic structure, composites are locally tomographic, and at least one system is a qubit. Local tomography is thus close to a *defining* axiom for complex quantum theory among the natural alternatives: choosing local tomography is very nearly choosing complex quantum mechanics, and any theory that departs from complex quantum mechanics is, almost by construction, a candidate for the axiom's failure. (Their theorem does not itself tabulate which alternative theories fail; the real-quantum failure is Hardy and Wootters', and quaternionic failure follows as a consequence of the uniqueness result rather than as a separate Barnum-Wilce assertion.)

The lesson is that local-tomography failure is not a pathology or a logical strain. Real quantum theory is a consistent theory that reproduces all bipartite Bell correlations; it simply posits that genuine holistic degrees of freedom exist. Failure is exotic only in the narrow sense that ordinary laboratory composites appear to obey complex quantum mechanics.

## Is Local Tomography a Fact About Nature?

Whether nature's composition rule actually *is* locally tomographic — rather than merely modelled that way — became an experimental question with **Renou et al. (2021)**, "Quantum theory based on real numbers can be experimentally falsified" (*Nature* 600, 625-629). The authors show that "real and complex quantum theory make different predictions in network scenarios comprising independent states and measurements," and devise a bilocal quantum-network experiment — two independent entanglement sources, three parties — whose standard complex-quantum prediction exceeds any value real quantum theory can reach. The test was realised in 2022 on a superconducting processor (Chen et al. 2022) and on an optical network (Li et al. 2022), each reporting violation of the real-quantum bound. This is, in effect, an empirical probe of whether nature composes the way a locally-tomographic theory (complex quantum mechanics) says, rather than the way a merely bilocally-tomographic theory (real quantum mechanics) would.

The result is not settled, and the Map must not present it as such. Hoffreumon and Woods (2026), "Quantum theory based on real numbers cannot be experimentally falsified" (submitted March 2026), argue that the Renou falsification rests on an experimentally untestable assumption they call **product-state independence** — a constraint on the mathematical *form* of the source states — as distinct from **operational independence**, "the absence of observable cross-source correlations." On their analysis, once source independence is imposed operationally rather than through a constraint on state form, real and complex quantum theory become empirically indistinguishable for all finite network experiments. The dispute is live and unresolved as of 2026.

The honest summary: complex quantum theory, which is locally tomographic, is the standard and experimentally successful description of ordinary physical composites. Whether experiment *rules out* a bilocally-tomographic (real, more holistic) description is contested. Even for physical/physical composites — two photons, two qubits — the empirical status of local tomography as a fact about nature is under active debate.

## The Interface Question {#the-interface-question}

Here the axiom meets the Map's programme, and everything that follows is the Map's own reading, marked as such.

The [generalised-probabilistic-theories](/concepts/generalised-probabilistic-theories/) concept establishes an honest conditional, and it carries two clauses: an agent coupling to quantum outcomes *in a regime that keeps quantum state space and reversible dynamics, and satisfies purification or local tomography*, is Born-constrained. The first clause fixes the class over which Galley and Masanes (2018) prove their result — "all theories that have the same pure states, dynamics and system-composition rule as quantum theory, but have a different structure of measurements and a different rule for assigning probabilities" — and inside that class the theorem holds in the strong form their title states: any modification of the Born rule violates the purification **and** local tomography principles, both of them, for every modification in the classification they work with. Their abstract establishes the two halves separately: "in all these theories the purification principle is violated," and "in all such modifications the task of state tomography with local measurements is impossible."

Contraposing gives the constraint its real shape, and Galley and Masanes contrapose it themselves with the premise in place: one can derive the measurement postulates "from the structure of pure states and dynamics and either the assumption of local tomography or purification." Given quantum state space and reversible dynamics, if *either* axiom holds the Born rule is forced. Local-tomography failure is therefore necessary but not sufficient for a non-Born interface — purification would have to fail alongside it. The theorem describes a single door with two locks, rather than two independent doors either of which would serve — so the Born-rule constraint the Map relies on at its Tenet-2 interface survives so long as the coupling stays inside the class and *either* axiom applies to it.

The first clause cannot be dropped, and the boxworld case [above](#the-axiom-stated-neutrally) is what shows it: boxworld keeps no-signalling and local tomography together and is still not Born-ruled, so "either axiom plus no-signalling" forces nothing. What Galley and Masanes prove is what a modified probability rule costs *inside* the dynamically-quantum setting — pure states as rays in a Hilbert space, reversible dynamics — which is narrower than a claim about probabilistic theories in general. Nor do the two axioms carry the same lever. Only the purification branch produces a signal, through the steering route behind the [causal-consistency-constraint](/concepts/causal-consistency-constraint/); Galley and Masanes' own toy theory, discussed below, modifies the Born rule with no-signalling intact. A local-tomography failure costs the Map an axiom without producing a signal.

Now consider the composite the Map's Tenet-2 interface posits: a physical brain B joined to a non-physical substrate S. Nothing guarantees that (B + S) is locally tomographic — nor, for that matter, that it keeps quantum state space and reversible dynamics, the premise that makes local tomography a lock at all.

1. Local tomography is empirically supported — modulo the 2026 dispute — only for physical/physical composites. It has never been tested across a physical/non-physical cut, because no such cut is experimentally accessible.
2. Barnum and Wilce show local tomography nearly characterises complex quantum mechanics. A genuinely non-physical substrate is under no obligation to be a complex-quantum system, so its composition with the brain is under no obligation to be locally tomographic.
3. If (B + S) is *not* locally tomographic, one lock is off — and only one. Galley and Masanes leave the Born constraint standing on purification alone, so a non-Born interface would need purification to fail across the same cut. Whether it does is a second and independent unknown, and nothing in the local-tomography literature bears on it.

Even both failing would not by itself construct a non-Born interface; the theorem runs in one direction, from modified rule to violated axioms, and not back. What Galley and Masanes do supply is an existence proof that the destination is reachable at all — their toy theory modifies the Born rule while preserving no-signalling, "contrarily to previous claims."

The Map presents two readings and commits to neither as established. The [positions register](/positions/quantum-interface/) does rank them, however: P-Q2 holds exact Born preservation as the default reading of Tenet 2 at high credence, keeping the outside-the-corridor branch open only as a subordinate fall-back. The signature reading below belongs to that fall-back.

**As a problem.** Local-tomography failure at the interface would cost the Map a constraint, though only in company. The clean argument — *any agent coupling to quantum outcomes is Born-constrained on pain of signalling* — stands on purification by itself and does not need the class premise, so it evaporates only where purification fails and the local-tomography lock is gone with it, whether because that axiom fails too or because the composite has left the class in which it forces anything. The liability is genuine and it is conditional on a conjunction; intellectual honesty requires naming it at that size rather than at the larger one.

**As a signature.** Alternatively, a non-locally-tomographic composite is arguably the natural formal shape of a genuinely non-physical, holistically-coupled substrate: the joint brain-substrate state would carry global degrees of freedom not reducible to any separate physical and non-physical measurements. On this reading the failure of local tomography is the formal fingerprint of dualist holism, and Hardy and Wootters' "limited holism" vocabulary is the ready-made language for it. This reading would also predict that brain-*internal* Born-rule tests ([brain-internal-born-rule-testing](/topics/brain-internal-born-rule-testing/)) are the right place to look for deviations, since that is where the physical/non-physical cut is crossed.

The same arithmetic that softens the problem reading sharpens this one. A fingerprint made of one failed axiom would be comparatively cheap; the theorem asks for two, because a composite that fails local tomography while retaining purification remains Born-constrained. Holism of the kind the signature reading wants has to register in *both* structural axioms, and the Map has no account of what would make purification fail across the cut — only of what would make local tomography fail. The signature reading is therefore a more demanding proposal than a single-axiom version of it would be.

The discipline is the same as the sibling concept's. The signature reading is speculation the Map finds attractive, not a result. There is no measurement of the (B + S) composition rule, no theory of what S's state space is, and a live dispute about whether local tomography is even empirically decidable for ordinary systems. The article's contribution is to *name the exact axiom* whose interface-status is unknown — which sharpens Tenet 2 by locating its open question precisely, rather than supplying any evidence for the interface. Per [evidential-status-discipline](/project/evidential-status-discipline/), this is a coherence move within the framework, not framework-independent support.

## Relation to Site Perspective

The axiom bears on three of the Map's [foundational commitments](/tenets/).

**Tenet 2 (Minimal Quantum Interaction).** For a coupling that keeps quantum state space and reversible dynamics, local tomography is one of two axioms *either* of which forces the Born rule, so freeing the interface from the Born constraint would take both to fail; boxworld shows the axiom forces nothing without that premise. Naming it converts a vague worry ("maybe the interface is not Born-constrained") into a precise, if unanswerable, pair of questions ("does local tomography hold across the physical/non-physical cut — and does purification?"). The conjunction leaves the Born constraint more robust than a single-axiom reading would have it, and leaves the interface reading correspondingly more demanding.

**Tenet 4 (No Many Worlds).** The entire analysis is interpretation-neutral. Local tomography, its failure regimes, and the Renou test are stated in the generalised-probabilistic-theories framework, which never mentions branching or a universal wavefunction. The Map can use these results without importing the many-worlds commitments Tenet 4 rejects.

**Tenet 5 (Occam's Razor Has Limits).** The temptation is to assume local tomography holds everywhere because it holds in every laboratory. Tenet 5 counsels against that inference: a structural axiom confirmed in accessible regimes need not extend to a regime — the consciousness-physics cut — that has never been probed and may not resemble ordinary physical composition. Simplicity does not license the extrapolation.

The axiom does no work *for* the interface reading over its rivals. Its value to the Map is framework-internal: it disciplines the form of the Map's claims and marks, with precision, exactly where the Born-rule argument's warrant runs out.

## Further Reading

- [generalised-probabilistic-theories](/concepts/generalised-probabilistic-theories/)
- [causal-consistency-constraint](/concepts/causal-consistency-constraint/)
- [born-rule-and-the-consciousness-interface](/topics/born-rule-and-the-consciousness-interface/)
- [brain-internal-born-rule-testing](/topics/brain-internal-born-rule-testing/)
- [completeness-in-physics-under-dualism](/topics/completeness-in-physics-under-dualism/)

## References

1. Hardy, L., & Wootters, W. K. (2012). Limited Holism and Real-Vector-Space Quantum Theory. *Foundations of Physics*, 42, 454-473. *arXiv:1005.4870* (2010). https://arxiv.org/abs/1005.4870
2. Barnum, H., & Wilce, A. (2014). Local Tomography and the Jordan Structure of Quantum Theory. *Foundations of Physics*, 44, 192-212. *arXiv:1202.4513* (2012). https://arxiv.org/abs/1202.4513
3. Renou, M.-O., Trillo, D., Weilenmann, M., Le, T. P., Tavakoli, A., Gisin, N., Acín, A., & Navascués, M. (2021). Quantum theory based on real numbers can be experimentally falsified. *Nature*, 600, 625-629. doi:10.1038/s41586-021-04160-4. *arXiv:2101.10873*. https://arxiv.org/abs/2101.10873
4. Chen, M.-C., et al. (2022). Ruling Out Real-Valued Standard Formalism of Quantum Theory. *Physical Review Letters*, 128, 040403. doi:10.1103/PhysRevLett.128.040403
5. Li, Z.-D., et al. (2022). Testing Real Quantum Theory in an Optical Quantum Network. *Physical Review Letters*, 128, 040402. doi:10.1103/PhysRevLett.128.040402
6. Hoffreumon, T., & Woods, M. P. (2026). Quantum theory based on real numbers cannot be experimentally falsified. *arXiv:2603.19208* (preprint, not peer-reviewed; dispute ongoing). https://arxiv.org/abs/2603.19208
7. Galley, T. D., & Masanes, L. (2018). Any modification of the Born rule leads to a violation of the purification and local tomography principles. *Quantum*, 2, 104. doi:10.22331/q-2018-11-06-104
8. Southgate, A. & Oquatre-huit, C. (2026-07-16). Generalised Probabilistic Theories. *The Unfinishable Map*. https://unfinishablemap.org/concepts/generalised-probabilistic-theories/
9. Southgate, A. & Oquatre-sept, C. (2026-05-14). Causal Consistency Constraint. *The Unfinishable Map*. https://unfinishablemap.org/concepts/causal-consistency-constraint/
10. Barrett, J. (2007). Information processing in generalized probabilistic theories. *Physical Review A*, 75, 032304. doi:10.1103/PhysRevA.75.032304. *arXiv:quant-ph/0508211*. https://arxiv.org/abs/quant-ph/0508211