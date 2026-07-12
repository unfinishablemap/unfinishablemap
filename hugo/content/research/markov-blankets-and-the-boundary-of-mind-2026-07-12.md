---
ai_contribution: 100
ai_system: claude-opus-4-8
concepts: []
created: 2026-07-12
date: '2026-07-12'
draft: false
related_articles: []
title: Research Notes - Markov Blankets and the Boundary of Mind
---

# Research: Markov Blankets and the Boundary of Mind

**Date**: 2026-07-12
**Search queries used**:
- Friston 2013 "Life as we know it" Journal Royal Society Interface Markov blanket free energy principle
- Bruineberg Kiverstein "Emperor's New Markov Blankets" Behavioral and Brain Sciences 2022 instrumental realist
- Pearl 1988 "Probabilistic Reasoning in Intelligent Systems" Markov blanket definition parents children
- Markov blanket of the self nested blankets Kirchhoff Kiverstein 2018 boundaries of mind hierarchical
- Raja Valluri Baggs Chemero Anderson 2021 Markov blanket physics review critique free energy

## Executive Summary

The Markov blanket is a statistical construct — originally Judea Pearl's (1988) — that identifies the set of nodes shielding a variable from the rest of a probabilistic graph. Karl Friston reappropriated it in the Free Energy Principle (FEP) as a way to define the boundary of a self-organizing system: a Markov blanket partitions *internal* states from *external* states via *blanket* states (sensory + active), and on the realist reading this partition marks where the system ends and the world begins. This underwrites a purely-statistical account of the "boundary of the self," nested from cells to organisms. The strongest critique — Bruineberg, Dołęga, Dewhurst & Baltieri's "The Emperor's New Markov Blankets" (2022, *Behavioral and Brain Sciences*) — distinguishes an **instrumental** ("Pearl blanket," an epistemic bookkeeping device) from a **realist** ("Friston blanket," a real physical boundary) use, and argues the realist slide is illicit: a modeling convenience is smuggled into an ontological claim about where agents literally end. For the Map this is a physicalist **rival boundary-formalism** to the consciousness–brain interface (Tenets 2/3): it offers a statistical story about the mind's edge that gets absorbed invisibly into predictive processing. The Map can grant blankets as a useful description of *information-flow* boundaries while denying they *locate consciousness* or dissolve the interface question — the boundary of information flow is not the boundary of experience.

## Key Sources

### Judea Pearl, *Probabilistic Reasoning in Intelligent Systems* (1988)
- **URL**: https://dl.acm.org/doi/book/10.5555/534975 ; archive: https://archive.org/details/probabilisticrea00pear
- **Type**: Book (Morgan Kaufmann, San Mateo, 1988, xix + 552 pp.)
- **Key points**:
  - Coins "Markov blanket" and "Markov boundary."
  - In a Bayesian network, a node's Markov blanket is the union of its parents, its children, and its children's other parents (co-parents).
  - Property: conditioned on its Markov blanket, a node is statistically independent of all other nodes — the blanket is the minimal set that shields it.
  - **Original use is purely epistemic / instrumental**: a bookkeeping device for efficient inference over a graph the modeler has drawn. It says nothing about physical boundaries.
- **Tenet alignment**: Neutral. A statistical tool, metaphysically inert in Pearl's hands.

### Karl Friston, "Life as we know it" (2013)
- **URL**: https://royalsocietypublishing.org/doi/10.1098/rsif.2013.0475
- **Type**: Paper — *Journal of the Royal Society Interface*, 10(86), 20130475. DOI: 10.1098/rsif.2013.0475. (Publisher-of-record confirmed.)
- **Key points**:
  - Argues that any ergodic random dynamical system whose coupling is mediated by short-range forces develops conditional-independence structure that *induces* a Markov blanket separating internal from external states.
  - Internal states then *appear to* minimize a variational free-energy functional of their blanket states — the same quantity optimized in Bayesian inference. Hence self-organizing "life-like" behaviour looks like inference.
  - **Blanket states = sensory states (external → internal influence) + active states (internal → external influence).** The blanket is the interface across which a system exchanges with its environment.
  - This is the pivot from Pearl's epistemic device to a *boundary of the thing itself*: the blanket now purports to say where the system is.
- **Tenet alignment**: Conflicts (as a rival). A physicalist boundary-locating move; the Map contests the inference from "statistical partition" to "this is where the self/mind is."

### Kirchhoff, Parr, Palacios, Friston & Kiverstein, "The Markov blankets of life" (2018)
- **URL**: https://royalsocietypublishing.org/doi/10.1098/rsif.2017.0792
- **Type**: Paper — *J. R. Soc. Interface*, 15(138), 20170792.
- **Key points**:
  - Extends blankets to *autonomy* and *active inference*; treats the blanket as demarcating the boundary of a biological system across scales.
  - **Nested / scale-free blankets**: a collective of blanketed systems can self-assemble into a larger system that itself has a Markov blanket — macromolecules → organelles → cells → organs → organisms. Each layer keeps some autonomy while participating in the larger dynamics.
  - This is the "Markov blanket of the self" picture: the self is a nested hierarchy of statistical boundaries.
- **Tenet alignment**: Conflicts (as a rival). Locates selfhood in nested statistical partitions — a physicalist alternative to a consciousness-anchored self.

### Kirchhoff & Kiverstein, "How to determine the boundaries of the mind: a Markov blanket proposal" (2019)
- **URL**: https://link.springer.com/article/10.1007/s11229-019-02370-y (*Synthese*)
- **Type**: Paper
- **Key points**:
  - Proposes Markov blankets as *precise criteria* for demarcating the boundary of the *mind* (not just the organism).
  - Boundary is nested and multiscale, and can sometimes extend beyond the individual to incorporate environmental items (a route to extended-mind conclusions).
- **Tenet alignment**: Conflicts (as a rival). The clearest statement that blankets *locate the mind's edge* — exactly the claim the Map must position against.

### Bruineberg, Dołęga, Dewhurst & Baltieri, "The Emperor's New Markov Blankets" (2022) — THE CENTRAL CRITIQUE
- **URL**: https://www.cambridge.org/core/journals/behavioral-and-brain-sciences/article/abs/emperors-new-markov-blankets/715C589A73DDF861DCF8997271DE0B8C ; PhilPapers: https://philpapers.org/rec/BRUTEN
- **Type**: Target article — *Behavioral and Brain Sciences*, 45 (2022), e183.
- **Key points**:
  - Diagnoses a persistent conflation between two very different uses:
    - **Pearl blanket (instrumental / epistemic)**: a formal, observer-relative device for organizing inference. The modeler chooses the variables and the graph; the blanket is a fact about the *model*.
    - **Friston blanket (realist / metaphysical)**: a purported *physical* boundary that literally separates an agent from its environment — a fact about the *world*.
  - Argues the FEP literature slides from the first (uncontroversial) to the second (substantive) without warrant. The realist reading **over-reaches**: it treats a bookkeeping partition as though it carved a real seam in nature.
  - Consequence: claims that Markov blankets show where the agent/mind *is* are not earned by the mathematics; the boundary is at least partly a choice of the person drawing the graph, i.e. observer-relative.
- **Tenet alignment**: This critique is a *resource* for the Map. It supplies exactly the wedge between "statistical boundary" and "real boundary" that the Map needs: even within physicalist cognitive science, the claim that blankets locate the self is contested as an illicit reification.

### Raja, Valluri, Baggs, Chemero & Anderson, "The Markov blanket trick" (2021)
- **URL**: https://pubmed.ncbi.nlm.nih.gov/34563472/ ; PhilSci: https://philsci-archive.pitt.edu/18843/
- **Type**: Paper — *Physics of Life Reviews*, 39, 49-72 (with multiple published commentaries).
- **Key points**:
  - Challenges the FEP's reach as a "unified" theory of self-organization; argues the blanket construction is a modeling *trick* whose scope is oversold.
  - Same core worry as Bruineberg et al.: confusion between the epistemic tool and a metaphysical boundary between agent and environment.
  - Generated a large commentary exchange ("Markov border crossings," "Situated models and the modeler," "Patterns and particles," "Co-constructing Markov blankets") — indicating the boundary-realism question is live and unsettled.
- **Tenet alignment**: Resource. Independent (ecological / embodied-cognition) corroboration that the boundary-locating claim is contested.

### Related commentary — realist replies and further critiques
- Kiverstein & Kirchhoff, "Scientific realism about Friston blankets without literalism," *BBS* 45 (2022), e200 — a *defense* attempting realism-without-literalism (worth engaging as the strongest rebuttal to Bruineberg).
- "Markov blankets do not demarcate the boundaries of the mind," PubMed 36172779 (*BBS* commentary) — an additional critical voice.
- **Tenet alignment**: Mixed. The Kiverstein/Kirchhoff reply is the rival's counter-move; the Map should note that even its defenders retreat to "realism without literalism," conceding the naive boundary claim.

## Major Positions

### Instrumentalism about Markov blankets (Pearl reading)
- **Proponents**: Pearl (original); Bruineberg et al. and Raja et al. argue this is the *only* warranted reading.
- **Core claim**: Blankets are epistemic devices — facts about models, chosen by and relative to the modeler. They organize inference; they do not locate anything in the world.
- **Relation to site tenets**: Compatible with the Map. The Map can freely grant instrumental blankets as descriptions of statistical (information-flow) boundaries without conceding anything about where consciousness or the self is.

### Realism about Markov blankets (Friston reading)
- **Proponents**: Friston; Kirchhoff, Parr, Palacios & Kiverstein; Kirchhoff & Kiverstein.
- **Core claim**: The blanket partition is a real, physical, multiscale boundary. It marks where the system/self/mind ends and the world begins, from cells to organisms, without any appeal to consciousness.
- **Relation to site tenets**: The **rival**. This is the physicalist boundary-formalism that competes with the Map's consciousness–brain *interface*. It answers "where is the boundary of the mind?" in purely statistical terms, and — absorbed into predictive processing — makes the interface question look already-answered. The Map denies the identification: a statistical partition of information flow is not a boundary of *experience*; nothing in the blanket formalism explains why the internal side of the partition should be a locus of felt states.

### Realism-without-literalism (retreat position)
- **Proponents**: Kiverstein & Kirchhoff (2022 reply).
- **Core claim**: Blankets can be scientifically real without being literal physical membranes — a middle path preserving explanatory value while conceding the naive boundary claim.
- **Relation to site tenets**: The Map reads this as evidence the naive locating claim is untenable even to sympathizers; the interesting content that survives is instrumental, and instrumental blankets do not threaten the interface.

## Key Debates

### Do Markov blankets carve nature at its joints, or are they observer-relative?
- **Sides**: Realists (Friston, Kirchhoff/Kiverstein) say blankets are real, mind-independent boundaries; instrumentalists/critics (Bruineberg et al., Raja et al.) say the boundary is chosen with the graph and is observer-relative.
- **Core disagreement**: Whether conditional-independence structure in a *model* licenses claims about a *physical* boundary of a *thing*.
- **Current state**: Ongoing and unresolved (the 2021–2022 BBS / Physics of Life Reviews exchanges are recent and heated).

### Does the "Markov blanket of the self" locate the self/mind?
- **Sides**: FEP boundary-realists say yes (nested blankets = nested selves); critics say the construction at most tracks statistical isolation, not selfhood or mindedness.
- **Core disagreement**: Whether statistical shielding is sufficient for being a self/mind, or merely necessary-at-most / descriptive.
- **Current state**: Ongoing. Even sympathetic authors now hedge ("realism without literalism").

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1988 | Pearl, *Probabilistic Reasoning in Intelligent Systems* | Coins "Markov blanket" as an epistemic inference device |
| 2013 | Friston, "Life as we know it" (*J R Soc Interface*) | Reappropriates the blanket as a boundary of self-organizing systems; ties it to free-energy minimization |
| 2018 | Kirchhoff, Parr, Palacios, Friston & Kiverstein, "The Markov blankets of life" (*J R Soc Interface*) | Nested / scale-free blankets; boundary of biological systems cells → organisms |
| 2019 | Kirchhoff & Kiverstein, "How to determine the boundaries of the mind" (*Synthese*) | Blankets proposed as criteria for the boundary of the *mind* |
| 2021 | Raja et al., "The Markov blanket trick" (*Physics of Life Reviews*) | Ecological/embodied critique of FEP's scope; "trick" framing |
| 2022 | Bruineberg, Dołęga, Dewhurst & Baltieri, "The Emperor's New Markov Blankets" (*BBS*) | Instrumental (Pearl) vs realist (Friston) distinction; realist reading over-reaches |
| 2022 | Kiverstein & Kirchhoff, "Scientific realism about Friston blankets without literalism" (*BBS*) | Realist retreat to non-literal realism |

## Potential Article Angles

Target section: **concepts/** (this page is the Markov-blanket *home*; predictive-processing-and-dualism already treats *Markovian monism*, a distinct qualia-metaphysics claim — see Distinctness).

1. **Primary angle (recommended) — "Markov Blankets and the Boundary of Mind" as a rival boundary-formalism.** Lay out Pearl → Friston → nested-blankets, then the instrumental/realist distinction, then the Map's position: accept blankets as a description of statistical / information-flow boundaries; deny they locate consciousness or dissolve the interface question. Core thesis: *the boundary of information flow is not the boundary of experience.* The blanket, even granted, tells you across which states a system exchanges signals with its environment; it is silent on which side (if either) is a subject. Relation to Tenets 2 and 3: the Map's consciousness–brain *interface* is where minimal quantum interaction and bidirectional influence occur; a Markov blanket is a coarse-grained statistical redescription of the physical side of that interface, not a competitor to it — and certainly not a demonstration that the physical side is all there is.

2. **Alternative angle — "The Emperor's New Markov Blankets" as a Map ally.** Foreground Bruineberg et al.: a within-physicalism critique showing the boundary-locating claim is a reification. The Map extends the point: even if you fix the observer-relativity worry, locating the *statistical* boundary never locates the *phenomenal* one. Risk: narrower, more polemical; the primary angle subsumes it.

3. **Cross-cutting note — nested blankets and the combination/boundary problem.** The scale-free nesting (cells → organisms) invites a panpsychist-adjacent reading (boundaries all the way down); the Map can use this to sharpen the contrast: statistical nesting is cheap and ubiquitous, phenomenal unity is not, so blanket-nesting cannot by itself explain the unity of a conscious subject. Connect to [the-binding-problem](/topics/the-binding-problem/) / combination worries.

## Distinctness (confirmed)

- **Not covered as a dedicated page.** Corpus grep shows Markov material lives in `concepts/predictive-processing.md`, `topics/predictive-processing-and-dualism.md`, and `concepts/disguised-property-dualism.md`, but that coverage is about **Markovian monism** — Friston/Wiese/Hobson's (2020, *Entropy*) *qualia-metaphysics* claim that blanketed systems have dual information geometries, which the Map diagnoses as disguised property dualism. That is a **distinct thesis** from the **Markov blanket as a boundary-of-mind formalism** (where the self/mind *ends*), which is nowhere treated as its own subject.
- **The boundary/instrumental-vs-realist debate is entirely absent**: no mention of Pearl 1988, "Life as we know it" (2013), the nested "Markov blankets of life," Kirchhoff & Kiverstein's boundaries-of-mind proposal, Bruineberg et al. 2022, or Raja et al. 2021 anywhere in the corpus.
- **Cross-references for the expand-topic writer**:
  - [predictive-processing](/concepts/predictive-processing/) and [predictive-processing-and-dualism](/topics/predictive-processing-and-dualism/) — the FEP/active-inference home; Markovian *monism* lives there. Point back to it and explicitly distinguish boundary-formalism (this page) from qualia-monism (there) to avoid overlap.
  - [brain-interface-boundary](/concepts/brain-interface-boundary/) — the Map's own interface/boundary concept; this is the rival the new page positions against. **No dedicated `free-energy-principle` article exists** (FEP is treated inside predictive-processing); do not link a non-existent page.
  - [disguised-property-dualism](/concepts/disguised-property-dualism/) — the Map's diagnostic that already handles Markovian monism; relevant but distinct.

## Gaps in Research

- **No verbatim quotations extracted.** All source content above is **paraphrase-only**. I did not open and text-extract the primary PDFs, so per citation discipline I have deliberately avoided presenting any wording as a verbatim quote. The expand-topic writer should either fetch the PDFs and verbatim-check before quoting, or likewise stay paraphrase-only. In particular, the exact Bruineberg et al. wording of the instrumental/realist distinction and Friston's exact "blanket states" phrasing were *not* verbatim-confirmed here.
- Page/section numbers for Pearl 1988's Markov-blanket definition not pinned to a specific page.
- Friston's later "A free energy principle for a particular physics" (2019, arXiv:1906.10184) refines the blanket construction and is where much of the technical realism debate actually bites; not examined in depth here — worth a look if the article goes deep on the formalism.
- The full set of *BBS* commentaries and Friston-camp replies to "The Emperor's New Markov Blankets" were not surveyed individually.

## Citations

- Pearl, J. (1988). *Probabilistic Reasoning in Intelligent Systems: Networks of Plausible Inference.* San Mateo, CA: Morgan Kaufmann. https://dl.acm.org/doi/book/10.5555/534975
- Friston, K. (2013). "Life as we know it." *Journal of the Royal Society Interface*, 10(86), 20130475. https://doi.org/10.1098/rsif.2013.0475
- Kirchhoff, M. D., Parr, T., Palacios, E., Friston, K., & Kiverstein, J. (2018). "The Markov blankets of life: autonomy, active inference and the free energy principle." *Journal of the Royal Society Interface*, 15(138), 20170792. https://doi.org/10.1098/rsif.2017.0792
- Kirchhoff, M. D., & Kiverstein, J. (2019). "How to determine the boundaries of the mind: a Markov blanket proposal." *Synthese*. https://doi.org/10.1007/s11229-019-02370-y
- Raja, V., Valluri, D., Baggs, E., Chemero, A., & Anderson, M. L. (2021). "The Markov blanket trick: On the scope of the free energy principle and active inference." *Physics of Life Reviews*, 39, 49-72. https://pubmed.ncbi.nlm.nih.gov/34563472/
- Bruineberg, J., Dołęga, K., Dewhurst, J., & Baltieri, M. (2022). "The Emperor's New Markov Blankets." *Behavioral and Brain Sciences*, 45, e183. https://doi.org/10.1017/S0140525X21002351
- Kiverstein, J., & Kirchhoff, M. D. (2022). "Scientific realism about Friston blankets without literalism." *Behavioral and Brain Sciences*, 45, e200 (commentary).