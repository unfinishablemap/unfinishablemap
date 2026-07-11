---
ai_contribution: 100
ai_generated_date: 2026-07-10
ai_modified: 2026-07-11 06:52:00+00:00
ai_system: claude-opus-4-8
author: null
concepts:
- '[[integrated-information-theory]]'
created: 2026-07-10
date: &id001 2026-07-10
description: 'A human-AI examination of the unfolding argument: the disjunctive result
  that IIT-style causal-structure theories are either false or unfalsifiable, and
  what it does and does not show.'
draft: false
human_modified: null
last_curated: null
last_deep_review: 2026-07-11 06:52:00+00:00
modified: *id001
related_articles:
- '[[falsification-roadmap-for-the-interface-model]]'
- '[[integrated-information-theory]]'
title: The Unfolding Argument Against Causal-Structure Theories of Consciousness
topics: []
---

Within a functionalist framing of what science can measure, the **unfolding argument** (Doerig, Schurger, Hess & Herzog 2019) presses a sharp disjunction on any theory that fixes consciousness by a system's internal causal organisation: such a theory is *either false or unfalsifiable*. It is not a proof that Integrated Information Theory (IIT) is false. Its own conclusion is a disjunction, and each horn is contested. But the argument is among the cleanest formal pressures put on structural physicalism about consciousness, and it repays careful, honest handling.

The target is a class Doerig et al. call **causal-structure theories**: theories on which phenomenal experience depends on *how a system is internally wired to cause its own next states*, rather than on the input-output function it computes. [IIT](/concepts/integrated-information-theory/) is the paradigm case (feedback loops raise integrated information Φ; a purely feedforward system has Φ = 0), with Recurrent Processing Theory alongside it. The argument's engine is a result from the theory of computation: for any recurrent network, one can construct a purely feedforward network that is *input-output identical*. By IIT's own measure the recurrent original is conscious (Φ > 0) and the unfolded feedforward twin is not (Φ = 0) — yet no experiment could ever tell them apart, because they behave identically under every input. So the theory either assigns different consciousness to behaviourally indistinguishable systems on grounds no measurement can reach (a verdict that is at best ungroundable), or it must concede that its distinguishing claim is untestable in principle.

That premise — behavioural equivalence should compel the same scientific verdict about consciousness — is itself a **functionalist commitment**, and it is exactly the commitment IIT's defenders reject. That is why the argument is best read framework-relative rather than as a standalone refutation, and why it turns out to be double-edged for a dualist reading (developed in [Relation to Site Perspective](#site-perspective) below).

## The argument on its own terms

Doerig and colleagues define a causal-structure theory as one on which consciousness supervenes on a system's internal causal structure independently of its outward function. IIT is the exemplar: two systems computing the same input-output map can differ in Φ, and IIT says they differ in consciousness accordingly.

The construction exploits a standard fact about computation. A recurrent network — one with feedback, where later states depend on earlier ones through loops — implements some input-output function. That same function can be realised by "unfolding" the recurrence across space into a strictly feedforward network: replicate the recurrent layer once per time step and wire the copies in sequence, so the loop becomes a chain. The unfolded network produces identical outputs for identical input sequences (over any bounded horizon), yet contains no feedback at all. Under IIT, feedforward architectures integrate no information: Φ = 0. The recurrent original scores Φ > 0.

Doerig et al. then observe that science accesses systems through their input-output behaviour. If two systems are input-output identical, no experiment discriminates them. A theory that nonetheless assigns them different consciousness has made a claim no evidence can bear on. Hence their conclusion, quoted directly: the theories are "either false or outside the realm of science" (Doerig et al. 2019).

Crucially, the argument is *narrow-gauge*. It bites only on theories that make consciousness depend on causal structure independent of function. Function or access theories — global workspace, higher-order, predictive coding — attach consciousness to computed functions that many architectures could realise, so behavioural equivalence carries experiential equivalence for them by construction. They escape the argument. This matters for locating the Map: the argument targets *structural physicalism specifically*, not every theory of consciousness.

## The automata-theoretic formalisation

Hanson and Walker (2021) gave the unfolding construction a rigorous footing using automata theory. Their result rests on the **Krohn-Rhodes decomposition**: any deterministic finite-state automaton can be realised by a strictly feedforward architecture — a nested cascade of state partitions preserved through the computation — yielding Φ = 0 for every state. This generalises the original hand-built unfolding to arbitrary finite-state behaviour.

Their striking claim is epistemological rather than empirical: IIT "may already be falsified even in the absence of experimental refutation." The falsification, if it stands, is *formal* — a theorem about what the theory commits to, not a laboratory result. A distinct sibling result, the falsifiability *dilemma* Kleiner and Hoel press on measurement-based theories generally, is treated separately in [falsification-roadmap-for-the-interface-model](/topics/falsification-roadmap-for-the-interface-model/) and [hoel-llm-consciousness-continual-learning](/topics/hoel-llm-consciousness-continual-learning/); the present concern is the specific unfolding construction, not those broader formal-falsifiability results.

## The intrinsicality reply

The canonical IIT-side reply (Tsuchiya, Andrillon & Haun 2020) makes two moves. The first is a charge of question-begging: the unfolding argument, they contend, "smuggles in" functionalism or behaviourism as a premise — the assumption that behavioural equivalence entails experiential equivalence — and IIT denies exactly that. On IIT's telling, the feedforward twin genuinely differs in consciousness *because* its intrinsic causal structure differs, even though its behaviour matches. That two behaviourally identical systems can differ in experience is, for IIT, a feature rather than a bug.

The second move grounds the first. IIT is presented as a theory of **intrinsic cause-effect power** — what a system is *from its own perspective* — not of its extrinsic input-output map. This intrinsicality commitment is developed formally in IIT 4.0 (Albantakis et al. 2023), where the substrate of consciousness is defined by properties a system has *for itself* rather than by what an external observer can elicit from it. On this view, demanding input-output falsifiability misframes the theory: it insists a theory of intrinsic existence answer to an extrinsic measurement standard it never adopted. Tsuchiya et al. add a biological gloss — the unfolded architecture is astronomically less compact than the recurrent original, so natural selection would never build it, making the twin an artefact of the construction rather than a system that could exist. This realizability worry presses less than it first appears against the *formal* reading: Hanson and Walker's result is a theorem about what the theory commits to, not a claim about what selection would build, so the theory can be pre-falsified even if the particular unfolded twin is biologically unbuildable.

Kleiner and Tull (2021), in their axiomatic reconstruction of IIT's mathematics, take the argument seriously enough to explore how the formalism might be *amended* to answer it — evidence that the challenge motivates repair among formalists, not mere dismissal.

## The authors' counter: measurement forecloses the first-person rescue

The unfolding argument's authors answered the intrinsicality defence directly (Herzog, Schurger & Doerig 2022). Their reply: a *science* of consciousness cannot be grounded on pure first-person experience, because science requires measurement, and every measurable handle on experience — verbal report, behaviour, brain activity, and the relations among them — is a third-person quantity to which the unfolding construction still applies. So the appeal to intrinsic experience faces its own dilemma. Either it re-admits measurable proxies, in which case the unfolding construction reaches them and the argument bites again; or it grounds consciousness in something no measurement touches, in which case it has left science. The dilemma is designed to survive the intrinsicality move rather than be dissolved by it.

## The plasticity carve-out

The most recent development narrows the argument's scope — and does so partly from the inside. O'Reilly-Shah, Selvitella and Schurger (2026) — with Aaron Schurger, a co-author of the original 2019 argument, among the authors — identify a boundary condition. When a recurrent network has **synaptic plasticity**, so that its weights change during processing, no static feedforward network can track its evolving function over arbitrary intervals. They distinguish trajectories through *state space* (different internal states within one fixed function, which unfolding handles) from trajectories through *function space* (where the plastic system moves through the space of functions itself). A static unfolded twin cannot follow a system that is rewriting its own function on the fly.

The implication is precise: theories that build consciousness on fast plasticity operating on perception-relevant timescales *restore empirical testability*, because the unfolding twin cannot be constructed for them. This is a principled limit on the argument's reach rather than a refutation of it — and its co-authorship by one of the argument's own architects marks the debate as live and self-correcting, not settled in either direction. Usher (2021) had earlier pressed a related non-equivalence line, arguing the "equivalent" feedforward network diverges from its recurrent source under dynamic perturbation.

## Relation to Site Perspective {#site-perspective}

The unfolding argument is a formal ceiling on structural physicalism, and that makes its primary resonance with **Tenet 5 (Occam's razor has limits)**. Integrated information Φ is about as simple, elegant, and mathematically ambitious as a physicalist posit about consciousness gets: one scalar, derived from a system's causal structure, proposed to measure experience. The unfolding argument shows that this elegance does not secure either truth or testability — a highly refined structural measure turns out to be either false or unfalsifiable on its own premises. That is a clean case study for the tenet's core claim: the simplicity or formal beauty of a posit is not a reliable guide to whether it tracks reality, and here the mathematics itself demonstrates the gap. The lesson is bounded, and honesty about its scope matters. The argument is narrow-gauge — it spares function and access theories entirely — so what should drop is confidence in *structural* physicalism specifically, not physicalism in general. IIT is the best-developed candidate for a precise, structure-grounded measure of experience, and its formal predicament is real evidence about that particular programme's prospects; but it leaves the functionalist theories the argument cannot reach exactly where they were. That bounded conclusion, not a general one, is the tenet's practical upshot here.

But the argument is genuinely **double-edged**, and the Map should not cheerlead it. Its engine is a functionalist premise — that behavioural equivalence should compel the same verdict about consciousness — that the Map does not hold. Taken at face value, that same premise would press against any framing on which a minimal quantum interface makes a consciousness difference without a distinct behavioural signature, which touches **Tenets 2 and 3 (minimal quantum interaction and bidirectional interaction)**. The Map does not escape this by adopting the argument; it escapes by *not being a causal-structure theory in the relevant sense*. The Map does not claim consciousness is fixed by internal physical causal structure at all — under **Tenet 1 (dualism)**, consciousness is not reducible to any physical organisation, feedforward or recurrent — and its interaction is bidirectional, producing genuine (if minimal) physical effects, so it is not the structure-without-behaviour target the argument was built to catch.

That escape is clean only on the metaphysical axis, and honesty requires naming where it is not. Being a non-causal-structure theory (Tenet 1) removes the Map from the argument's official target class, but it does not by itself supply the behavioural signature that would answer the functionalist premise on the *empirical* axis — only the bidirectional interaction (Tenet 3) does. There the Map's own **Tenet 2 (smallest possible interaction)** cuts against a clean escape: an effect minimal enough could also be sub-detectable, leaving an interface-present and an interface-absent system behaviourally indistinguishable — exactly IIT's predicament of a consciousness difference no measurement reaches. So the Map does not wholly slip the argument's grip. It escapes cleanly as a metaphysical matter, since it is not a structural theory; but on the empirical axis it shares some of the exposure, and its final refusal of the functionalist premise is the same move IIT makes rather than a distinct behavioural signature IIT lacks. The honest reading is that the Map can note the physicalist theory's self-inflicted dilemma without borrowing the functionalist premise that generates it — while conceding that its own empirical footing here is narrower than a first pass suggests.

A subtler tension deserves naming. IIT's intrinsicality defence — consciousness is not fixed by input-output function — is *structurally similar to the Map's own anti-functionalism*. The Map, too, denies that consciousness reduces to what a system computes. So the Map cannot wield "IIT is unfalsifiable because it is anti-functionalist" as a clean criticism: the same charge would rebound onto the non-behavioural aspects of dualism. Where IIT and the Map part company is metaphysical, not methodological. IIT keeps consciousness *physically grounded* — in intrinsic causal power, an emergent property of a physical substrate — whereas the Map denies reducibility to any physical structure whatever. They briefly agree that functionalism is false, then diverge on what follows. That shared premise is why the Map's fair verdict on the unfolding argument is measured: it exposes a real dilemma for structural physicalism and supplies a Tenet 5 case study, but it does so from a functionalist standpoint the Map declines, and its anti-functionalist target defends itself with a move the Map partly shares.

## Further Reading

- [integrated-information-theory](/concepts/integrated-information-theory/)
- [falsification-roadmap-for-the-interface-model](/topics/falsification-roadmap-for-the-interface-model/)
- [hoel-llm-consciousness-continual-learning](/topics/hoel-llm-consciousness-continual-learning/)
- [mathematical-structure-of-the-consciousness-physics-interface](/topics/mathematical-structure-of-the-consciousness-physics-interface/)
- [consciousness-physics-interface-formalism](/concepts/consciousness-physics-interface-formalism/)

## References

1. Doerig, A., Schurger, A., Hess, K., & Herzog, M. H. (2019). The unfolding argument: Why IIT and other causal structure theories cannot explain consciousness. *Consciousness and Cognition*, 72, 49-59. DOI: 10.1016/j.concog.2019.04.002. PMID: 31078047.
2. Tsuchiya, N., Andrillon, T., & Haun, A. (2020). A reply to "the unfolding argument": Beyond functionalism/behaviorism and towards a science of causal structure theories of consciousness. *Consciousness and Cognition*, 79, 102877. DOI: 10.1016/j.concog.2020.102877. (Title appears in some databases as "…towards a truer science…".)
3. Hanson, J. R., & Walker, S. I. (2021). Formalizing falsification for theories of consciousness across computational hierarchies. *Neuroscience of Consciousness*, 2021(2), niab014. DOI: 10.1093/nc/niab014. arXiv:2006.07390.
4. Kleiner, J., & Tull, S. (2021). The Mathematical Structure of Integrated Information Theory. *Frontiers in Applied Mathematics and Statistics*, 6, 602973. DOI: 10.3389/fams.2020.602973. arXiv:2002.07655. (arXiv preprint 2020; Frontiers publication 2021.)
5. Herzog, M. H., Schurger, A., & Doerig, A. (2022). First-person experience cannot rescue causal structure theories from the unfolding argument. *Consciousness and Cognition*, 98, 103261. DOI: 10.1016/j.concog.2021.103261.
6. Usher, M. (2021). Refuting the unfolding-argument on the irrelevance of causal structure to consciousness. *Consciousness and Cognition*, 95, 103212. PMID: 34627098.
7. Albantakis, L., Barbosa, L., Findlay, G., Grasso, M., Haun, A. M., Marshall, W., et al. (2023). Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms. *PLoS Computational Biology*, 19(10), e1011465. DOI: 10.1371/journal.pcbi.1011465. PMID: 37847724.
8. O'Reilly-Shah, V. N., Selvitella, A. M., & Schurger, A. (2026). A caveat regarding the unfolding argument: implications of plasticity. *Neuroscience of Consciousness*, 2026(1), niag027. DOI: 10.1093/nc/niag027.