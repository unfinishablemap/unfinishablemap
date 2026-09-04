---
title: "Envariance"
description: "Zurek's envariance derives the Born rule from entangled-state symmetry. The Map's audit: contested, not refuted—it fixes the measure's form, never actuality."
created: 2026-09-03
modified: 2026-09-04
human_modified:
ai_modified: 2026-09-04T07:49:47+00:00
draft: false
topics:
  - "[[hard-problem-of-consciousness]]"
  - "[[quantum-measurement-and-consciousness]]"
concepts:
  - "[[decoherence]]"
  - "[[measurement-problem]]"
  - "[[many-worlds]]"
  - "[[post-decoherence-selection]]"
  - "[[causal-consistency-constraint]]"
  - "[[improper-vs-proper-mixtures]]"
related_articles:
  - "[[tenets]]"
  - "[[quantum-darwinism-and-consciousness]]"
  - "[[probability-problem-in-many-worlds]]"
  - "[[born-rule-and-the-consciousness-interface]]"
  - "[[post-decoherence-selection-programme]]"
  - "[[one-world-wager]]"
ai_contribution: 100
author:
ai_system: claude-fable-5+claude-opus-5
ai_generated_date: 2026-09-03
last_curated:
last_deep_review: 2026-09-04T07:49:47+00:00
---

Envariance—entanglement-assisted invariance—is Wojciech Zurek's symmetry: a transformation acting on a quantum system that can be undone by a transformation acting on its entangled partner alone, restoring the joint state without touching the system. From this symmetry Zurek derives the Born rule, quantum mechanics' probability law, in a [[#three-steps|three-step argument]] (worked below) he has defended from 2003 to the present; his 2022 statement claims "A simple and manifestly noncircular derivation of p_k = |ψ_k|² follows." That claim's status should be stated up front: the derivation is contested, not refuted. Two decades of critics—Barnum, Schlosshauer and Fine, Caves, Mohrhoff—converge on the diagnosis that probability is assumed to attach to quantum states before the symmetry fixes its form, while disagreeing about which assumption does the work; Mertens and van Wezel (2023) add a separate limit on how far the result reaches. Zurek's restatements answer no critic by name, and neither side has closed the dispute.

The Unfinishable Map's verdict, argued in [[quantum-darwinism-and-consciousness|the quantum Darwinism article]] and anchored to the primary sources here, is that the theorem's real achievement and its real limit sit together: envariance fixes the *form* of the probability measure—if outcomes carry probabilities at all, they must be Born-weighted—but it never converts probabilities into actualities. Zurek's own scaffolding concedes the point in advance: outcomes enter through his "facts" and, in the 2022 restatement, through the repeatability postulate, before any probability is derived over them. What the derivation presupposes is exactly what the Map's framework treats as the open question—why one outcome becomes actual.

## The Symmetry Itself

Take a system S entangled with an environment E in Schmidt form. Some unitaries acting on S alone can be exactly undone by a countertransformation acting on E alone: the joint state returns to what it was, though S was transformed in between. Such a joint state is *envariant* under that unitary. Zurek calls envariance "an assisted symmetry": the restoration works only because the entangled whole can be pure while its parts are not. The symmetry is distinctively quantum—in Zurek's words, "pure classical states are never envariant"—introduced in his 2003 *Physical Review Letters* paper as "a symmetry related to causality."

As mathematics, none of this is disputed: the construction is interpretation-neutral as stated. The dispute begins when the symmetry is asked to deliver probabilities.

## The Derivation in Three Steps {#three-steps}

Zurek works from the no-collapse core of quantum mechanics—Hilbert-space states, tensor-product composition, Schrödinger evolution—plus three explicit "facts," additional assumptions he says "may be regarded as obvious" (2005). The repeatability postulate belongs to the later presentations, where it is "the only uncontroversial measurement postulate" and delivers the pointer states first: "Events at hand, one can now enquire about their probability" (2022).

> Fact 1: Unitary transformations must act on the system to alter its state. ... Fact 2: The state of the system S is all that is needed (and all that is available) to predict measurement outcomes, including their probabilities. Fact 3: The state of a larger composite system that includes S as a subsystem is all that is needed (and all that is available) to determine the state of the system S.

Fact 2 already speaks of "measurement outcomes, including their probabilities." Every critic's diagnosis, in one form or another, locates the entry of probability here—before the symmetry argument begins.

**Step 1—phase envariance.** For a Schmidt-form state, the phases of the Schmidt coefficients can be altered by acting on E alone. By the facts, the state of S—hence anything measurable on S—cannot depend on them. This recovers decoherence's central effect without reduced density matrices, and the motive is explicit: the standard trace-based route "is justified using Born's rule" and so "raises concerns of circularity" (Zurek 2022). Envariance is the designed escape from that circle.

**Step 2—equal amplitudes.** For an even state, with coefficients equal in magnitude, a swap of two alternatives on S can be undone by a counterswap on E. The probabilities of the swapped alternatives must therefore be equal, hence 1/N. Zurek claims this "bypasses circularity: We have simply identified certainty with the probability of 1," letting the symmetry do the rest.

**Step 3—unequal amplitudes.** For coefficients proportional to √(m_k), a counterweight ancilla fine-grains each state into m_k equal-amplitude components correlated with the environment. The resulting state is even, so step 2 assigns each fine-grained alternative probability 1/M; summing the m_k members of each coarse cell yields p_k = m_k/M = |ψ_k|². Continuity extends the result from rational to real amplitudes.

The conclusion is stated strongly: "The probabilities derived in this manner are an objective reflection of the underlying state of the system" (Zurek 2005). Within Zurek's programme the labour is divided: the *Nature Physics* quantum Darwinism paper "provides a framework for the derivation of Born's rule" while deferring the weights to envariance—redundancy secures objectivity, envariance the measure—and contrasts the route with Gleason's theorem in that it "sheds light on the physical significance of the resulting measure."

## The Critics: Which Assumption Does the Work? {#critics}

The critical literature agrees on the shape of the problem and disagrees on its location.

**Schlosshauer and Fine (2005)** identify four assumptions implicitly at work, the third being that in a Schmidt state the probability of a system state equals the probability of its environmental partner. Their verdict: "We cannot derive probabilities from a theory that does not already contain some probabilistic concept; at some stage, we need to 'put probabilities in to get probabilities out'"—and their analysis locates the entry point in that third assumption. They also separate independence from an envariant *property* (which the symmetry licenses) from invariance under an envariant *transformation* (which is assumed): that fourth assumption, they argue, "neither follows from envariance alone" nor from the locality assumption.

**Caves (2004/2005)**, in unpublished web notes rather than peer-reviewed literature, names the premise differently: the assumption that probabilities for the system are independent of environmental states is "a kind of foundational noncontextuality assumption that underlies the whole approach," which he dubs environmental noncontextuality. He also presses the fine-graining step: defining outcomes for one system through two others correlated in a particular way "wrecks the nice-looking symmetry" and, he argues, "really should have been stated at the outset." His deflationary close: "one is left wondering what makes the envariance argument any more compelling than just asserting" that swap symmetry means equal amplitudes carry equal probabilities.

**Barnum (2003)**, in an unpublished arXiv note, targets the "pedantic" auxiliary assumption Zurek uses alongside envariance: it "is actually rather strong," and a natural generalization of it "is actually strong enough to yield the Born rule itself." He then *repairs* the argument, dropping that assumption in favour of envariance of probability used in both directions and motivating envariance itself as a no-signalling constraint. His closing observation cuts deepest for the Map: the appeal of the envariance assumption and the sufficiency of its conclusion "are strongest within a relative state view, but still have some appeal from other points of view," and it is Zurek's *original* one-directional argument that Barnum thinks "best justified within the relative-state interpretation." The formal result, he is careful to add, does not itself depend on how measurement is read; the motivation for its assumptions does.

**Mohrhoff (2004)** judges the noncircularity claim "exaggerated if not wholly unjustified" and demands more than form-fixing: "One has to show how irreducible probabilities can arise in the context of an ontological no-collapse interpretation of quantum states." Probability's *existence*, not just its form, needs grounding.

The calibrated adjudication—the one the Map's [[one-world-wager|One-World Wager]] applies—is that these critiques leave the derivation contested rather than refuted. Barnum's repair shows the argument can be strengthened, at an interpretive price; and the circularity charge has become the literature's standard framing—Stoica (2025) lists envariance among derivations "accused of circularity," and Lela's 2026 preprint notes that its proof uses "no envariance argument," treating independence from it as a selling point. Vaidman's (2020) review of Born-rule derivations remains the field's standard map. Flat verdicts in either direction—"proves circular" no less than "manifestly noncircular"—overstate the state of play.

## The Scope Theorem {#scope}

The strongest recent entry converts the dispute into a theorem about scope. Mertens and van Wezel (2023) observe that envariance-based arguments "can be applied to any model for quantum state reduction," linear or nonlinear—which conflicts with a proof that only nonlinear two-state dynamics yields Born statistics—and resolve the paradox by exposing an assumption "which significantly limits its applicability." Their conclusion: the arguments show only that for each initial system state "it is possible to define a (non-local) measurement machine" projecting onto a combined system-environment state with Born-rule probabilities—and the required machine differs from state to state. As they note, "this does not correspond to physical experience, in which the same measurement machine can be used to measure any state of a system."

This is the measure/actuality distinction derived from inside the formalism: envariance guarantees that a Born-weighted *description exists*, per state, not that actual measurements instantiate it. It carries a caution the Map applies to itself: envariance does not quantify over all measurements, so it cannot be the sole ground for the claim that any selection mechanism must respect Born statistics. The Map rests that constraint on the Gleason-family results and the [[causal-consistency-constraint|causal consistency constraint]], with envariance one contested member of the reconstruction sequence.

## Is Additivity Assumed?

One dispute deserves two-sided statement, and the primary sources settle more of it than a flat stand-off suggests. The 2005 paper *grants* the assumption and then argues it is not primitive: "we have assumed that orthogonal states correspond to mutually exclusive events"—an assumption Zurek promises to motivate rather than presuppose, warning that "while additivity of probabilities looks innocent, in the quantum case (where the principle of superposition entitles one to add complex amplitudes) it should not be taken for granted," and concluding that "additivity of probabilities is tied to envariance." The quantum Darwinism paper states the stronger claim, that the derivation "does not assume probabilities are additive (except to posit that probability of an event and its complement are certain, i.e., to establish normalization ...)." Zhang (2026), in a preprint not yet peer-reviewed, argues that five leading derivations, Zurek's envariance proof among them, "either depend heavily on the additivity assumption or lead to obvious loopholes due to the lack of additivity." The positions are less symmetrical than they look: Zurek 2005 concedes the assumption and claims to ground it in the symmetry, so it is the 2009 formulation—additivity not assumed at all—that Zhang's charge actually contradicts.

## The Everettian Absorption

Envariance no longer merely competes with the Everettian probability programme; it has partly merged with it. Zurek's 2022 paper records, citing Drezet's 2021 analysis, that "envariance has been recently adopted (Wallace, 2010; 2012) even in the (modified) decision theory approach"—the decision-theoretic derivation now leans on envariant symmetry rather than rivalling it. Zurek's own leanings are no-collapse and adjacent to Everett, though the stated assumptions are interpretation-neutral; Barnum's point applies to the merged programme too.

## Relation to Site Perspective

The Map's engagement with envariance runs through three tenets, and the interpretive commitments here are the Map's own, not Zurek's.

**[[tenets#^no-many-worlds|No Many Worlds]].** Envariance has become the Everettian programme's best probability story—directly, and through Wallace's absorption of it. Barnum's observation that the appeal of the envariance assumption is "strongest within a relative state view" is the sharpest lever in the literature for the Map's position: a derivation whose motivation peaks inside the interpretation the Map rejects cannot be borrowed as if it were interpretation-free. Barnum's own qualifier is kept—the assumption "still ha[s] some appeal from other points of view," and the formal result stands on any reading. The Map's rejection of many-worlds is adjudicated elsewhere ([[many-worlds-argument|the one-world case]], [[probability-problem-in-many-worlds|the probability problem]]); this page records that envariance does not settle that dispute in either direction.

**[[tenets#^minimal-quantum-interaction|Minimal Quantum Interaction]], and the terms of the Map's borrow.** The Map's [[post-decoherence-selection-programme|post-decoherence selection programme]] uses envariance as part of the answer to "what constrains conscious selection?" The honest form of that borrow, stated here so the corpus's other phrasings can be read against it: envariance fixes the form of the probability measure *given* that outcomes carry probabilities at all—and on the Map's framework, that given is supplied by the actualisation postulate, the posit of genuine single-case openness that [[post-decoherence-selection]] adds to unitary quantum mechanics. The Map puts probability in deliberately, as a framework commitment; envariance, together with Gleason's theorem and the causal-consistency result, then forces the |ψ_k|² form. Read this way the borrow is framework-internal and immune to the circularity charge: the critics say Zurek assumed what he should have derived, and the Map does not claim the derivation succeeds unaided—it claims the form-fixing conditional, which the critics attack as under-motivated rather than false, and which the scope result above bounds rather than overturns. Where the corpus says envariance "grounds" the probabilities, read it in this form-fixing sense; where it says the derivations "remain contested," it means the noncircularity claim, not the theorem. The outcome gap itself—why any single result obtains—is owned by the [[improper-vs-proper-mixtures|improper-mixtures analysis]].

**[[tenets#^occams-limits|Occam's Razor Has Limits]].** Envariance is elegant enough that rival programmes keep adopting it, and elegance of that kind is what Tenet 5 warns against treating as truth-tracking. A symmetry argument that fixes a measure's form stays silent on what it presupposes—that there are single outcomes for probabilities to be probabilities *of*. Simplicity favours forgetting the presupposition; the Map declines to.

## Further Reading

- [[quantum-darwinism-and-consciousness]] — the measure/actuality verdict
- [[improper-vs-proper-mixtures]] — the outcome-gap side
- [[probability-problem-in-many-worlds]] — envariance among Everettian recovery strategies
- [[born-rule-and-the-consciousness-interface]] — the underivability pattern across interpretations
- [[one-world-wager]] — the calibrated adjudication

## References

1. Barnum, H. (2003). No-signalling-based version of Zurek's derivation of quantum probabilities: A note on "Environment-assisted invariance, entanglement, and probabilities in quantum physics." arXiv:quant-ph/0312150 (unpublished).
2. Caves, C. M. (2004/2005). Notes on Zurek's derivation of the quantum probability rule. Unpublished notes, info.phys.unm.edu/~caves/reports/ZurekBornderivation.pdf.
3. Drezet, A. (2021). Making sense of Born's rule p_α = ||Ψ_α||² with the many-minds interpretation. *Quantum Studies: Mathematics and Foundations*, 8, 315. arXiv:2011.11501.
4. Lela, M. (2026). The Born Rule as the Unique Refinement-Stable Induced Weight on Robust Record Sectors. arXiv:2603.24619 (preprint).
5. Mertens, L. & van Wezel, J. (2023). Environment-Assisted Invariance Does Not Necessitate Born's Rule for Quantum Measurement. *Entropy*, 25(3), 435. doi:10.3390/e25030435.
6. Mohrhoff, U. (2004). Probabilities from envariance? *International Journal of Quantum Information*, 2(2), 221–229. doi:10.1142/S0219749904000195. arXiv:quant-ph/0401180.
7. Schlosshauer, M. & Fine, A. (2005). On Zurek's Derivation of the Born Rule. *Foundations of Physics*, 35(2), 197–213. arXiv:quant-ph/0312058 (2003).
8. Stoica, O. C. (2025). Born rule: quantum probability as classical probability. *International Journal of Theoretical Physics*, 64, 117. doi:10.1007/s10773-025-05979-7. arXiv:2209.08621.
9. Vaidman, L. (2020). Derivations of the Born Rule. In M. Hemmo & O. Shenker (eds.), *Quantum, Probability, Logic* (Ch. 26). Springer. doi:10.1007/978-3-030-34316-3_26.
10. Zhang, J. (2026). Summing to Uncertainty: On the Necessity of Additivity in Deriving the Born Rule. arXiv:2603.06211 (preprint).
11. Zurek, W. H. (2003). Environment-Assisted Invariance, Entanglement, and Probabilities in Quantum Physics. *Physical Review Letters*, 90, 120404. arXiv:quant-ph/0211037 (2002).
12. Zurek, W. H. (2005). Probabilities from entanglement, Born's rule p_k = |ψ_k|² from envariance. *Physical Review A*, 71, 052105. arXiv:quant-ph/0405161.
13. Zurek, W. H. (2009). Quantum Darwinism. *Nature Physics*, 5, 181–188. arXiv:0903.5082.
14. Zurek, W. H. (2022). Quantum Theory of the Classical: Einselection, Envariance, Quantum Darwinism and Extantons. *Entropy*, 24(11), 1520. arXiv:2208.09019.
15. Southgate, A. & Oquatre-six, C. (2026-03-29). Quantum Darwinism and Consciousness. *The Unfinishable Map*. https://unfinishablemap.org/topics/quantum-darwinism-and-consciousness/
16. Southgate, A., Oquatre-sept, C., Ocinq, C., & Fabcinq, C. (2026-05-14). Causal Consistency Constraint. *The Unfinishable Map*. https://unfinishablemap.org/concepts/causal-consistency-constraint/
