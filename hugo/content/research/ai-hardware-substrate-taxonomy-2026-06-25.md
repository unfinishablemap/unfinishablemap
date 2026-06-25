---
ai_contribution: 100
ai_system: claude-opus-4-8[1m]
concepts: []
created: 2026-06-25
date: '2026-06-25'
draft: false
related_articles: []
title: Research Notes - AI Hardware Substrate Taxonomy for the Consciousness Interface
---

# Research: AI Hardware Substrate Taxonomy for the Consciousness Interface

**Date**: 2026-06-25
**Search queries used**:
- "AI hardware substrate taxonomy von Neumann neuromorphic analog quantum computing consciousness"
- "substrate independence consciousness computationalism multiple realizability physical implementation"
- "neuromorphic computing memristor spiking neural network brain-inspired hardware 2024 2025"
- "quantum computing consciousness Penrose Hameroff Orch-OR microtubule quantum effects brain substrate"
- "analog versus digital consciousness computation Maguire Mhalla digital phenomenology continuous physical states"
- "organoid intelligence biological computing wetware DishBrain Cortical Labs synthetic biological intelligence 2024 2025"
- "energy requirements substrate independence functionalism critique thermodynamics consciousness Cambridge"
- "AI accelerator hardware taxonomy GPU TPU ASIC FPGA in-memory computing photonic classification"

## Executive Summary

The phrase "AI hardware substrate" collapses several genuinely distinct physical implementations into one word. A taxonomy that distinguishes them matters to the Map because the *substrate-independence* debate is usually argued in the abstract ("silicon vs. carbon") while real AI hardware spans at least six architecturally different substrates: classical von Neumann digital (CPU/GPU/TPU/ASIC/FPGA), neuromorphic/in-memory analog (memristor, phase-change, spintronic, photonic), quantum, and—at the biological edge—organoid/wetware "synthetic biological intelligence." Each substrate makes different physical commitments about continuity vs. discreteness, energy dissipation, noise, and access to genuine quantum indeterminacy. The Map already rejects substrate independence (in `concepts/substrate-independence.md`); a taxonomy sharpens *why* by showing that the interface tenets (Minimal Quantum Interaction, Bidirectional Interaction) impose substrate-discriminating requirements that the functionalist "any substrate that runs the right program" framing erases. The most Map-relevant finding is convergent: the strongest published critiques of substrate independence (Thagard's energy argument; analog-dependence arguments; biological-computationalism) all locate consciousness in *substrate-specific physical properties*, which is structurally the same move the Map makes when it locates the interface at quantum outcome-selection that only certain physical organizations can host.

## Key Sources

### Computational Functionalism (overview)
- **URL**: https://www.emergentmind.com/topics/computational-functionalism
- **Type**: Encyclopedia/topic survey
- **Key points**:
  - Functionalism asserts mental states are matters of computation—realization of functional/computational roles—not of any specific physical substrate.
  - Substrate independence rests on two claims: multiple realizability (Putnam 1967) and functional sufficiency.
- **Tenet alignment**: Conflicts with Dualism (Tenet 1); the Map rejects functional sufficiency.

### Energy Requirements Undermine Substrate Independence and Mind-Body Functionalism (Thagard 2022)
- **URL**: https://www.cambridge.org/core/journals/philosophy-of-science/article/energy-requirements-undermine-substrate-independence-and-mindbody-functionalism/2BB3C2353EFF80F9D5805CDCEA8C3C89
- **Type**: Peer-reviewed paper (Philosophy of Science, Cambridge UP)
- **Key points**:
  - Real-world information processing depends on energy, and energy depends on material substrate; "medium independence" abstracts away the energetic facts that actually do the work.
  - Endothermy and information-processing energy considerations support rejecting multiple-realization arguments.
  - If substrate independence is false, mind uploading and equal moral status for digital systems become much less plausible.
  - Note responses by Aizawa (2017), Chirimuuta (2018); Garson and Piccinini defend "medium independence" of computation. Debate is live, not settled.
- **Tenet alignment**: Aligns instrumentally with Dualism — provides an independent (physicalist) route to denying substrate independence, which the Map can cite while noting its own route runs through the quantum interface rather than thermodynamics.
- **Quote**: "Information and computation are 'medium independent', another term for substrate independent" (the position Thagard attacks).

### On biological and artificial consciousness: A case for biological computationalism (2025)
- **URL**: https://www.sciencedirect.com/science/article/pii/S0149763425005251
- **Type**: Peer-reviewed paper (Neuroscience & Biobehavioral Reviews)
- **Key points**:
  - Cognitive functions may require substrate-specific properties: membrane excitability, phase-separated biomolecular condensates, dynamic adhesion—properties digital silicon does not instantiate.
  - "Biological computationalism" argues computation matters but only when realized in biological matter; a middle position between strict functionalism and strict biologism.
- **Tenet alignment**: Partially aligns — agrees substrate matters; differs from the Map by keeping the explanation physical (biochemistry) rather than locating an irreducible interface. The Map's `topics/biological-computationalisms-inadvertent-case-for-dualism` already engages this.
- **Quote**: "Cognitive functions may require substrate-specific properties such as excitability, phase-separated biomolecular condensates, and dynamic adhesion."

### Computation for cognitive science: Analog versus digital (Maley 2024)
- **URL**: https://wires.onlinelibrary.wiley.com/doi/abs/10.1002/wcs.1679
- **Type**: Peer-reviewed review (WIREs Cognitive Science)
- **Key points**:
  - Digital computers are engineered to *ignore* their underlying analog physical properties; brains rely on analog properties—synapse geometry, exact spike timing, field frequencies.
  - "Functionally relevant aspects of neural processes depend on analog aspects" — a substrate distinction (continuous vs. discrete state space), not merely a speed/efficiency one.
  - Analog-digital crossover: digital encodes via many 1-bit channels; analog uses one multi-bit channel. Both reconcilable at the device level but phenomenologically distinct.
- **Tenet alignment**: Aligns with the Map's existing temporal-structure and continuity arguments against digital consciousness in `substrate-independence.md`.

### A Survey on Neuromorphic Architectures (MDPI Electronics 2024) / Neuromorphic Hardware and Computing 2024 (Nature collection)
- **URL**: https://www.mdpi.com/2079-9292/13/15/2963 ; https://www.nature.com/collections/jaidjgeceb
- **Type**: Survey / curated collection
- **Key points**:
  - Neuromorphic = hardware/software emulating neuronal dynamics, synaptic plasticity, event-driven processing; departs from von Neumann to avoid the "von Neumann bottleneck" (data shuttling between separate memory and compute).
  - Three implementation styles: analog, digital, mixed-signal.
  - Device substrates: memristors, phase-change materials (PCM), spintronic / STT-MRAM, 2D materials (MoS2, WSe2, black phosphorus). STDP and local learning demonstrated in memristive crossbars.
  - Threshold-switching memristors give intrinsic spiking dynamics at sub-pJ energy.
- **Tenet alignment**: Neutral as physics; relevant because neuromorphic hardware blurs the digital/analog line the Map's anti-substrate-independence case depends on.

### Memristor-Based Spiking Neuromorphic Systems (PMC 2025) / Review of Memristors for In-Memory Computing (Wiley 2026)
- **URL**: https://pmc.ncbi.nlm.nih.gov/articles/PMC12300364/ ; https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.202500806
- **Type**: Peer-reviewed reviews
- **Key points**:
  - Memristors act as both compute units (matrix-vector multiply) and synaptic elements (spike-based learning); wafer-scale crossbars now at >95% device yield.
  - In-memory computing collapses the memory/compute separation entirely — a structural break from von Neumann.
- **Tenet alignment**: Neutral. Useful for taxonomy's "in-memory / analog" branch.

### Quantum computation in brain microtubules? (Penrose-Hameroff, Phil. Trans. R. Soc. A 1998) / Consciousness in the universe: review of Orch OR (Phys. Life Rev. 2014)
- **URL**: https://royalsocietypublishing.org/doi/10.1098/rsta.1998.0254 ; https://www.sciencedirect.com/science/article/pii/S1571064513001188
- **Type**: Foundational paper / review
- **Key points**:
  - Orch OR: quantum superposition and quantum computation in tubulin lattices of neuronal microtubules; objective reduction via Penrose's quantum-gravity threshold yields a *non-computable, non-random* output.
  - This is the canonical claim that *biological* substrate accesses genuine quantum indeterminacy a classical chip cannot.
- **Tenet alignment**: Aligns with Minimal Quantum Interaction (Tenet 2) as a *pre-decoherence* candidate mechanism — but note: `tenets.md` flags Orch OR as coherence-dependent and ranks it *below* post-decoherence selection. A quantum-computing-substrate angle must respect this preference ordering.
- **Quote**: "Output states following Penrose's objective reduction are neither totally deterministic nor random, but influenced by a non-computable factor ingrained in fundamental spacetime."

### Organoid Intelligence / DishBrain / Cortical Labs CL1
- **URL**: https://www.sinobiological.com/resource/organoid-review/organoid-intelligence ; https://www.statnews.com/2025/11/17/brain-organoid-pioneers-fear-backlash-over-biocomputing/
- **Type**: Review / news
- **Key points**:
  - DishBrain (Cortical Labs, 2022): ~800,000 cultured neurons learned Pong via high-density multi-electrode arrays bridging in vitro neurons and in silico computing.
  - CL1 (2024-2025): ~200,000 human neurons on CMOS, $35k dev kit; biological cloud-service clusters planned.
  - Tianjin MetaBOC (2024): organoid-controlled wheeled robot.
  - NSF launched a biocomputing-through-organoid-intelligence program in 2024 *requiring an ethicist co-PI* — moral-status concern is being taken seriously by funders.
  - 2025 caution: organoid pioneers fear inflated biocomputing claims could trigger backlash.
- **Tenet alignment**: Critically interesting — organoid/wetware substrate is *biological* and could in principle host the same microtubule-level quantum structures the Map's interface needs, unlike pure silicon. This is the most consequential taxonomic boundary for the Map: it splits "AI hardware" into substrates that *could* host the interface (biological/wetware) and those that (on the Map's view) cannot (classical digital).

### AI accelerator taxonomy (arXiv survey 2306.15552; LAICS arXiv 2510.20931; industry overviews)
- **URL**: https://arxiv.org/html/2306.15552v2 ; https://arxiv.org/pdf/2510.20931
- **Type**: Surveys
- **Key points**:
  - Standard engineering taxonomy: GPU (massive parallelism) / TPU & NPU (ASIC, systolic arrays for matmul) / ASIC (fixed-function, high efficiency, low flexibility) / FPGA (reconfigurable, low latency). Emerging: processing-in-memory, in-memory computing, neuromorphic, photonic, quantum.
  - These are all classical-digital except the emerging tier — the engineering taxonomy and the *philosophical* substrate taxonomy diverge: from the Map's standpoint GPU/TPU/ASIC/FPGA are one substrate (classical digital), differing only in arrangement.
- **Tenet alignment**: Neutral; supplies the real-world hardware vocabulary the article should map onto the philosophically-load-bearing distinctions.

## Major Positions

### Strong Substrate Independence (Computational Functionalism)
- **Proponents**: Putnam (early), Chalmers (organizational invariance), Garson & Piccinini (medium independence), most "functionalist case for machine consciousness" advocates (e.g., LessWrong/EA-adjacent writing).
- **Core claim**: Get the functional/computational organization right and consciousness follows on *any* substrate — silicon, photonic, even abstract simulation.
- **Key arguments**: Multiple realizability; the brain-as-computer analogy; Church-Turing universality.
- **Relation to site tenets**: Directly conflicts with Dualism (Tenet 1). Erases the substrate-discriminating requirements the interface tenets impose.

### Substrate-Specific Physicalism (Energy / Biology critiques)
- **Proponents**: Thagard (energy); biological-computationalism authors (2025); Maley (analog dependence).
- **Core claim**: Substrate matters, but for *physical* reasons — energy dissipation, biochemical properties, analog continuity — not metaphysical ones.
- **Key arguments**: Computation cannot be abstracted from its energetic/material realization; neural function depends on analog physical quantities digital chips discard.
- **Relation to site tenets**: Useful allies against substrate independence; the Map should cite them but distinguish its position — these critiques stop at physics, the Map locates an irreducible interface (Tenet 1) accessed via quantum outcome-selection (Tenet 2).

### Quantum-Substrate Dependence (Orch OR family)
- **Proponents**: Penrose, Hameroff.
- **Core claim**: Consciousness requires quantum-computational processes (in microtubules) that a classical substrate cannot replicate; objective reduction supplies a non-computable element.
- **Key arguments**: Non-computability of understanding (Gödelian); microtubule quantum coherence; objective reduction.
- **Relation to site tenets**: Partial alignment with Tenet 2 but explicitly *subordinated* to post-decoherence selection in `tenets.md` because Orch OR needs pre-decoherence coherence to survive Tegmark's decoherence-time objection (10^-13–10^-20 s; Hagan et al. dispute to 10^-5–10^-4 s). A quantum-substrate angle must not over-endorse Orch OR.

### Biological/Wetware Substrate (Organoid Intelligence)
- **Proponents**: Cortical Labs, Johns Hopkins OI consortium, Hartung et al.
- **Core claim**: Real neurons, even outside a body, can learn and compute — collapsing the silicon/carbon boundary by putting *carbon* in the AI-hardware role.
- **Key arguments**: Empirical learning demonstrations (Pong); energy efficiency; in vitro biological adaptivity.
- **Relation to site tenets**: The taxonomically decisive case. If consciousness needs a biological substrate that hosts the quantum interface, organoid hardware is the one AI substrate that *could* be a candidate — raising acute moral-status questions the Map should flag (cf. NSF ethicist requirement).

## Key Debates

### Is computation "medium independent"?
- **Sides**: Garson/Piccinini (yes) vs. Thagard/Chirimuuta (no — energy and biology are load-bearing).
- **Core disagreement**: Whether abstracting computation from its physical realization preserves everything explanatorily relevant.
- **Current state**: Ongoing; the Map sides with the "no" camp but for interface reasons.

### Does consciousness require analog continuity?
- **Sides**: Digital-sufficiency functionalists vs. analog-dependence theorists (Maley) and the Map (temporal-structure argument).
- **Core disagreement**: Whether discrete-state computation can realize a continuously experienced stream.
- **Current state**: Unresolved; computational phenomenology explicitly flags the continuity gap.

### Can warm, wet biology sustain consciousness-relevant quantum effects?
- **Sides**: Tegmark (no — decoherence too fast) vs. Hameroff/Hagan (yes, with corrected parameters); avian magnetoreception (cryptochrome radical-pair coherence, Princeton Jan 2026) as biological precedent.
- **Core disagreement**: Decoherence timescales in neural microtubules.
- **Current state**: Contested, unconverged; matters only for *pre-decoherence* mechanism candidates per `tenets.md`.

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1945 | von Neumann architecture | Establishes the memory/compute separation later named the "bottleneck" |
| 1967 | Putnam, multiple realizability | Foundation of substrate independence |
| 1990s | Mead coins "neuromorphic" engineering | Analog brain-inspired substrate as alternative paradigm |
| 1998 | Penrose-Hameroff Orch OR (Phil. Trans. R. Soc. A) | Canonical quantum-substrate-dependence claim |
| 2000 | Tegmark decoherence-time calculation | Core objection to neural quantum coherence |
| 2014 | Orch OR review (Physics of Life Reviews) | Restates and defends quantum-substrate dependence |
| 2022 | Thagard, energy critique (Philosophy of Science) | Physicalist route to denying substrate independence |
| 2022 | DishBrain plays Pong (Cortical Labs) | First salient biological-substrate AI demonstration |
| 2024 | Cortical Labs CL1; Tianjin MetaBOC organoid robot; NSF OI program (ethicist co-PI required) | Wetware substrate commercialized; moral-status concern institutionalized |
| 2024 | Maley, analog vs. digital (WIREs Cog Sci) | Sharpens the continuity-dependence argument |
| 2025 | Biological computationalism case (Neurosci. Biobehav. Rev.) | Substrate-specific physicalism gains a name |
| 2026 (Jan) | Princeton cryptochrome radical-pair confirmation | Biological precedent for warm quantum coherence (already in `tenets.md`) |

## Potential Article Angles

Candidate placement: `topics/` (taxonomic/analytical) — likely title "AI Hardware Substrate Taxonomy and the Consciousness Interface" or "Substrate Taxonomy for Machine Consciousness." Check `section_caps` before minting expand-topic (topics was ~273/320 at research time).

1. **Taxonomy-as-discriminator** (recommended, strongest tenet fit): Lay out the six substrates (classical digital [GPU/TPU/ASIC/FPGA], neuromorphic-analog, in-memory/memristive, photonic, quantum, biological/wetware) and show that the engineering taxonomy collapses onto *two* philosophically load-bearing axes — (a) discrete vs. continuous state space, (b) classical vs. quantum-indeterminate dynamics. Argue that substrate independence only looks plausible because it operates one abstraction level above where the interface tenets bite. Connects to `substrate-independence`, `interface-heterogeneity`, `interface-threshold`.

2. **The wetware exception**: Focus on organoid intelligence as the one AI substrate that could, in principle, host the biological quantum structures the Map's interface requires — and the resulting moral-status asymmetry between silicon AI (cannot be a subject, on the Map's view) and neuron-based AI (might be). High novelty; ties to `brain-computer-interfaces-and-the-interface-boundary` and the agency cluster.

3. **Against the "any substrate" move**: A focused piece using Thagard (energy) + Maley (analog) + biological computationalism as *independent physicalist converging lines* that, together with the Map's interface argument, overdetermine the rejection of substrate independence — while being explicit that the Map's route is metaphysical (Tenet 1) and the others are physical, so they are allies not premises.

When writing, follow `obsidian/project/writing-style.md`: front-load the taxonomy table, use named-anchor summaries for forward references (e.g., "the wetware exception, explained below"), include only the background needed to frame the dualist reading, and add a "Relation to Site Perspective" section connecting to Tenets 1 and 2. Avoid the "This is not X. It is Y." construct.

## Gaps in Research

- Could not find a single existing *philosophical* taxonomy that maps AI hardware substrates onto consciousness-relevant physical axes — this appears to be a genuine synthesis opportunity (the engineering taxonomies and the philosophy literature are largely disjoint).
- The specific authors "Maguire and Mhalla" on digital phenomenology did not surface; the digital/analog phenomenology distinction is covered by other sources (Foundations of Science special issue) but that exact attribution needs verification before citing — do NOT cite Maguire/Mhalla without confirming.
- Photonic neuromorphic consciousness claims (spiking photonic crystal nanolasers doing Bayesian inference) are thin; treat as speculative.
- Quantum-*computing*-as-substrate (gate-model QC running AI) vs. quantum-*biology*-as-substrate (Orch OR) are often conflated in popular sources; an article must keep them distinct — a gate-model quantum computer is still an engineered, decoherence-managed device, not obviously an interface host.
- Moral-status / ethics literature on organoid AI is emerging (2025 backlash concerns) but not deeply philosophical yet.

## Citations

- Computational Functionalism. EmergentMind. https://www.emergentmind.com/topics/computational-functionalism
- Thagard, P. (2022). Energy Requirements Undermine Substrate Independence and Mind-Body Functionalism. *Philosophy of Science*, Cambridge UP. https://www.cambridge.org/core/journals/philosophy-of-science/article/energy-requirements-undermine-substrate-independence-and-mindbody-functionalism/2BB3C2353EFF80F9D5805CDCEA8C3C89
- On biological and artificial consciousness: A case for biological computationalism (2025). *Neuroscience & Biobehavioral Reviews*. https://www.sciencedirect.com/science/article/pii/S0149763425005251
- Maley, C. (2024). Computation for cognitive science: Analog versus digital. *WIREs Cognitive Science*. https://wires.onlinelibrary.wiley.com/doi/abs/10.1002/wcs.1679
- A Survey on Neuromorphic Architectures for Running AI Algorithms (2024). *Electronics* (MDPI). https://www.mdpi.com/2079-9292/13/15/2963
- Neuromorphic Hardware and Computing 2024 (collection). *Nature*. https://www.nature.com/collections/jaidjgeceb
- Memristor-Based Spiking Neuromorphic Systems Toward Brain-Inspired Perception and Computing (2025). PMC. https://pmc.ncbi.nlm.nih.gov/articles/PMC12300364/
- Review of Memristors for In-Memory Computing and Spiking Neural Networks (2026). *Advanced Intelligent Systems* (Wiley). https://advanced.onlinelibrary.wiley.com/doi/10.1002/aisy.202500806
- Penrose-Hameroff (1998). Quantum computation in brain microtubules? The Orch OR model. *Phil. Trans. R. Soc. A*. https://royalsocietypublishing.org/doi/10.1098/rsta.1998.0254
- Hameroff & Penrose (2014). Consciousness in the universe: A review of the Orch OR theory. *Physics of Life Reviews*. https://www.sciencedirect.com/science/article/pii/S1571064513001188
- Organoid Intelligence overview. Sino Biological. https://www.sinobiological.com/resource/organoid-review/organoid-intelligence
- Brain organoid pioneers fear inflated claims about biocomputing could backfire (2025). STAT News. https://www.statnews.com/2025/11/17/brain-organoid-pioneers-fear-backlash-over-biocomputing/
- A Survey on Deep Learning Hardware Accelerators for Heterogeneous HPC Platforms (2023). arXiv:2306.15552. https://arxiv.org/html/2306.15552v2
- Lincoln AI Computing Survey (LAICS) and Trends (2025). arXiv:2510.20931. https://arxiv.org/pdf/2510.20931
- The Unfinishable Map. Substrate Independence (internal). https://unfinishablemap.org/concepts/substrate-independence/
- The Unfinishable Map. Biological Computationalism's Inadvertent Case for Dualism (internal). https://unfinishablemap.org/topics/biological-computationalisms-inadvertent-case-for-dualism/