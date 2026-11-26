---
ai_contribution: 100
ai_generated_date: 2026-11-26
ai_modified: 2026-11-26 13:30:10+00:00
ai_system: claude-opus-5-5
author: null
concepts:
- '[[universal-coupling-response]]'
- '[[integrated-information-theory]]'
- '[[recurrent-processing-theory]]'
- '[[minimal-consciousness]]'
created: 2026-11-26
date: &id001 2026-11-26
description: FlyWire's 139,255-neuron fly connectome shows a highly recurrent brain
  and constrains integration claims, but omits electrical synapses and neuromodulation.
  Fold into universal-coupling-response.
draft: false
harvest_date: 2026-11-26
harvest_source: optimistic-2026-11-25-interface-variation-wing
human_modified: null
last_curated: null
lastmod: 2026-11-26 13:30:10+00:00
modified: *id001
recommended_action: fold
related_articles:
- '[[falsification-roadmap-for-the-interface-model]]'
- '[[ethics-of-consciousness-invertebrate-question]]'
- '[[reviews/optimistic-2026-11-25-interface-variation-wing]]'
target_section: concepts
target_slug: universal-coupling-response
title: Research Notes - The Adult Drosophila Whole-Brain Connectome and What It Does
  and Does Not Settle
topics:
- '[[invertebrate-consciousness-as-interface-test]]'
- '[[consciousness-in-simple-organisms]]'
- '[[architectural-adequacy-at-the-built-edge]]'
---

# Research: The Adult Drosophila Whole-Brain Connectome and What It Does and Does Not Settle

**Date**: 2026-11-26
**Search queries used**: Dorkenwald 2024 "Neuronal wiring diagram of an adult brain"; Shiu 2024 leaky integrate-and-fire whole-brain model; Schlegel 2024 multi-connectome cell typing; Lin 2024 network statistics rich club; integrated information Φ FlyWire connectome; fly connectome consciousness philosophy; 2025 brain-and-nerve-cord / male CNS connectome; connectome-constrained embodied fly simulation 2026; Bargmann & Marder 2013; insect sentience connectome central complex (extended). Full texts were fetched as PMC XML through NCBI E-utilities and grepped locally; the PubMed records supplied the 2025–2026 metadata.

**Verdict**: `recommended_action: fold`. Topics and concepts are both at cap (370/370 each by `count_section_files`, 13:18Z), so no new article is possible. The subject also works better as a constraint on the Map's adequacy criterion than as a page of its own. The main host is [universal-coupling-response](/concepts/universal-coupling-response/); one optional sentence goes to [invertebrate-consciousness-as-interface-test](/topics/invertebrate-consciousness-as-interface-test/), plus a zero-word number sweep across five pages. The fold plan is at the end, under "Fold Plan (for the driver)".

## Executive Summary

FlyWire's adult *Drosophila* connectome (Dorkenwald et al. 2024) reconstructs one female fly's whole brain at synaptic resolution: 139,255 neurons and 54.5 million chemical synapses. Several companion papers in the same *Nature* issue report what that structure shows. The brain is highly recurrent: feedforward three-node motifs are under-represented, reciprocal and recurrent motifs over-represented, and about 30% of neurons form a rich club (Lin et al. 2024). The ellipsoid body, whose ring neurons carry fly trace conditioning (Grover et al. 2022), is among the most recurrent neuropils. A whole-brain spiking model built only from wiring and predicted transmitters, with no gap junctions, neuromodulation or internal state, was consistent with 91% of 164 tested predictions about feeding and grooming circuits (Shiu et al. 2024).

The authors are explicit about what the map lacks. It has no electrical synapses, no neuropeptide or extrasynaptic signalling, few proofread glia, and synapse counts that undercount; it is a single brain, and a snapshot. The connectome specifies which neurons can affect which, but "not how strongly they do affect each other in vivo" (Pospisil et al. 2024). It therefore constrains functional-architecture claims (recurrence, hub structure, sensory-to-motor depth, which behaviours wiring alone predicts) and integration measures in principle. It settles no attribution of experience. Physicalists and dualists both expect that outcome, so on the tenet ladder the connectome is **compatible** with the Map and discriminates nothing at tenet level. Its main use to the Map is to discipline the architectural-adequacy criterion in [universal-coupling-response](/concepts/universal-coupling-response/). Graph statistics do not line up: the 302-neuron worm out-ranks the fly on connection reciprocity (0.372 against 0.138) and falls far below it on small-worldness (3.21 against 141). No single structural statistic can therefore serve as the adequacy condition.

## Key Sources

### Dorkenwald et al. (2024) — the FlyWire whole-brain connectome
- **URL**: https://doi.org/10.1038/s41586-024-07558-y (open full text PMC11446842)
- **Type**: Paper (*Nature* 634(8032), 124–138)
- **Exact claims (grepped in full text this run)**:
  - Abstract: a whole-brain wiring diagram of about 5 × 10⁷ chemical synapses between "139,255 neurons reconstructed from an adult female Drosophila melanogaster". Main text: "Our reconstruction of an entire adult brain contains 139,255 neurons" and "54.5 million synapses between these neurons".
  - Composition: 118,501 of the 139,255 are intrinsic to the brain. Of those, 32,388 lie wholly in the central brain and 77,536 in the optic lobes and ocellar ganglia, excluding photoreceptors. The visual system therefore accounts for about two-thirds of intrinsic neurons. 8,053 visual projection neurons run into the central brain and 524 centrifugal neurons run back, and "half of all optic lobe neurons receive five or more synapses from VCNs, showing that much early visual processing incorporates feedback from the central brain".
  - Scope of the word "connectome": the authors say their diagram "arguably crosses the threshold", while conceding "it would be reasonable to insist that a connectome should include the ventral nerve cord as well as the brain".
- **Authors' caveats (grepped)**:
  - Chemical synapses only: "Our connectome includes only chemical synapses; the identification of electrical synapses awaits a future electron microscopy dataset with higher resolution".
  - Undercounting: "the observed synapse counts underrepresent the actual number of synapses and some connections with few synapses remain undetected". The postsynaptic attachment rate is 44.7%.
  - Glia: an estimated 13% of cell bodies are non-neuronal or glial, and only a few astrocyte-like glia were proofread.
  - Optic lobe artefact: the left lamina was partially severed from the medulla, which lowers accuracy for some lamina neurons on that side.
  - Simulations built on the connectome assume that physiological strength is proportional to synapse count, and they take connection sign from predicted transmitter identity. Shunting inhibition and conductance asymmetries are flagged as known departures.
  - Single specimen, female. Codex uses a five-synapse threshold for a connection; the optic-lobe companion paper uses two.
  - The paper does not use the word "neuromodulation". That caveat comes from Shiu, Lin and Pospisil (below).
- **Tenet alignment**: Neutral. It is a structural resource and makes no claims about consciousness.

### Schlegel et al. (2024) — companion annotation and cell-typing paper
- **URL**: https://doi.org/10.1038/s41586-024-07686-5 (PMC11446831)
- **Type**: Paper (*Nature* 634(8032), 139–152)
- **Exact claims (grepped)**: 8,453 annotated cell types, 3,643 of them proposed earlier from the hemibrain and 4,581 new. "about one-third of cell types proposed for the hemibrain could not be reliably reidentified", which prompts a new cross-brain definition of cell type. On whether one brain is representative: "over 50% of the connectome graph is a snowflake. Of course, these non-reproducible edges are mostly weak. Our criterion for strong (highly reliable) edges applies to between 7–16% of edges but 50–70% of synapses." Conclusion: "In conclusion, we have not collected a snowflake." They also find a KCg-m neuron count nearly twice as high in FlyWire as in the hemibrain, with compensatory connectivity changes (evidence of functional homeostasis).
- **Relevance**: This is the single-brain caveat, quantified. Strong edges replicate across individuals and weak edges largely do not. Any graph statistic sensitive to weak edges therefore carries individual noise.
- **Tenet alignment**: Neutral.

### Lin et al. (2024) — network statistics of the whole-brain connectome
- **URL**: https://doi.org/10.1038/s41586-024-07968-y (PMC11446825)
- **Type**: Paper (*Nature* 634(8032), 153–165)
- **Exact claims (grepped)**:
  - "The network of the fly brain is highly recurrent and displays rich-club organization, with a large population (30%) of preferentially connected neurons." The rich club holds 40,218 neurons, with 676 broadcasters and 638 integrators.
  - "Feedforward motifs (motifs 1–3) are under-represented when compared to both ER and CFG models, while all others, including the highly recurrent motifs (motifs 7–13), are over-represented." The giant strongly connected component (where every neuron can reach every other along directed paths) shows "the prevalence of recurrent connections in the brain".
  - Neuropils: "the EB has one of the highest reciprocity rates", together with one of the highest mean connection strengths and very large over-representations of highly recurrent three-node motifs. The EB is the ellipsoid body, part of the central complex.
  - Comparative table, computed on the thresholded 127,978-neuron network. Connection reciprocity: fly 0.138, hermaphrodite *C. elegans* 0.372 (chemical network), male *C. elegans* 0.386, larval zebrafish hindbrain 0.113, mouse V1 L2/3 0.088. Clustering coefficient: fly 0.0463, worm 0.284. Small-worldness: fly S = 141, *C. elegans* S = 3.21. The worm's rich club is 11 neurons (4%), and the paper finds no single fly hub analogous to AVA/AVB.
- **Authors' caveats (grepped)**: "Note that direct comparisons of graph metrics must be made with caution"; rich-club size comparisons "are sensitive to the criteria used". "Note also that the synaptic connectome does not provide a complete picture of information flow in the brain. We do not currently have a map of gap junction synapses in the fly or of the extent of neuropeptide signalling". Transmitter predictions are 94% accurate against ground truth, assume Dale's law, and the authors note co-transmission exists. Directionality of information flow far from sensory or motor ends "must be determined experimentally".
- **Tenet alignment**: Neutral. This paper supplies the recurrence facts the fold uses.

### Shiu et al. (2024) — whole-brain leaky integrate-and-fire model
- **URL**: https://doi.org/10.1038/s41586-024-07763-9 (PMC11446845)
- **Type**: Paper (*Nature* 634(8032), 210–219)
- **Exact claims (grepped)**: The model uses an earlier FlyWire snapshot "containing more than 125,000 neurons and 50 million synaptic connections". "Our results demonstrate that modelling brain circuits using only synapse-level connectivity and predicted neurotransmitter identity generates experimentally testable hypotheses and can describe complete sensorimotor transformations." The predictions cover sugar- and water-sensing gustatory pathways to the proboscis motor neuron MN9, taste interactions, and antennal grooming. "Across 164 predictions we were able to test empirically, 91% were consistent with our empirical results". Excluding the split-GAL4 screen, where most cell types did nothing, the figure is 84%. Shuffle control: the real connectome activated MN9 in 100% of simulations, and "only 1 of 100 shuffled simulations did".
- **Authors' caveats (grepped)**: "the model does not account for gap junctions, non-spiking neurons, internal state or long-range neuropeptides, and assumes that the basal firing of each neuron is zero". Also: "Gap junctions cannot be identified in the electron microscopy dataset, so we ignore their possibility. We do not account for neuropeptides or neuromodulation." Failures cluster on inhibitory and neuromodulatory cells: "Further, circuits with extensive neuromodulation or extrasynaptic signalling will be poorly modelled." Usnea, mispredicted by the model, turned out to need neuropeptide processing (an Amontillado knockdown phenocopied it). Citing *C. elegans* and the stomatogastric ganglion, the authors add that "connectivity knowledge constrains, but does not dictate, a particular circuit mechanism".
- **Scope**: The model covers sensorimotor transformations in feeding and grooming. It contains no learning, no internal state and no flexible behaviour.
- **Tenet alignment**: Compatible with Bidirectional Interaction. The model reproduces reflex-type circuits, which no account treated as consciousness markers. See the tenet section for what would change this grade.

### Pospisil et al. (2024) — the effectome proposal
- **URL**: https://doi.org/10.1038/s41586-024-07982-0 (PMC11446844)
- **Type**: Paper (*Nature* 634(8032), 201–209)
- **Exact claims (grepped)**: The connectome "specifies the synaptic paths by which neurons can affect each other, but not how strongly they do affect each other in vivo". The paper proposes learning a causal model (the "effectome") from optogenetic perturbation, with the connectome as prior. From an eigen-analysis of the connectome read as a linear dynamics matrix: "Overall, we provide evidence that fly whole-brain dynamics are generated by a large collection of small circuits that operate largely independently of each other."
- **Authors' caveats (grepped)**: the estimator is linear while "the fly nervous system is a highly nonlinear system", and "It is in only a narrow set of situations that the best linear approximation to these nonlinear neural dynamics would be proportional to the connectome."
- **Relevance**: This is the cleanest statement of the does-not-settle point. It also pulls against Lin's integrated picture: one analysis of the same matrix gives a rich club and global recurrence, another gives many largely independent small circuits. That disagreement matters for any integration measure (see the IIT discussion below).

### Lappalainen et al. (2024) — connectome-constrained networks in the visual system
- **URL**: https://doi.org/10.1038/s41586-024-07939-3 (PMC11525180)
- **Type**: Paper (*Nature* 634(8036), 1132–1140)
- **Exact claims (grepped)**: "The degree to which measurements of connectivity alone can inform the understanding of neural computation is an open question". A model with measured connectivity for 64 motion-pathway cell types, whose single-neuron and synapse parameters were fitted by deep learning to a motion-detection task, made predictions that "agreed with experimental measurements of neural activity across 26 studies". The authors report the strategy works better when connectivity is sparse.
- **Relevance**: Connectivity plus a task objective can recover activity. The unknown parameters are supplied by optimisation, not by the map.

### Bates et al. (2026) — brain-and-nerve-cord connectome (BANC)
- **URL**: https://doi.org/10.1038/s41586-026-10735-w (PMC13518251)
- **Type**: Paper (*Nature* 656(8129), 957–970). Female fly; brain about 140,000 neurons and ventral nerve cord about 20,000, joined by about 1,300 descending and 1,800 ascending neurons.
- **Exact claims (grepped)**: "These results reveal an architecture that is distributed, parallelized and embodied". Effector neurons are mainly driven by sensory neurons in the same body part, forming local feedback loops. Long-range ascending and descending modules link these loops, and "Brain regions involved in learning and navigation supervise these circuits". The paper reports "empirical support for theories of behavioural control organized around distributed sensory-motor modules, in which cognitive regions are supervisory but not essential for action."
- **Relevance**: This bears on centralist adequacy readings, such as Barron and Klein's midbrain analogy for the central complex. The integrative regions supervise but are not required for action. That is compatible with the Barron and Klein thesis (which concerns integration for action selection, not necessity for movement) and does not settle it.

### Berg et al. (2026) — male whole-CNS connectome
- **Metadata**: *Cell* 189(18), 5504–5526.e15 (PubMed 42691995; preprint PubMed 41279223). The *Cell* title is "Sexual dimorphism in the complete Drosophila male central nervous system connectome".
- **Exact claim (from the preprint abstract on PubMed, grepped)**: "This contains 166,691 neurons spanning the brain and nerve cord". The abstract also reports 7,205 isomorphic, 114 dimorphic, 262 male-specific and 69 female-specific types.
- **Not checked**: the *Cell* full text. Use the figure as the preprint's.
- **Relevance**: Since 2026 the single-female-brain caveat no longer holds for the field, though it still holds for FlyWire. A male CNS and a second female brain plus VNC (BANC) now exist.

### Bargmann & Marder (2013) — what a connectome omits
- **URL**: https://doi.org/10.1038/nmeth.2451 (PDF from a course mirror, grepped)
- **Type**: Historical Perspective (*Nature Methods* 10(6), 483–490)
- **Exact claims (grepped)**: neuromodulators often act without defined synaptic contacts, and "As a result, the targets of neuromodulation are invisible to the electron microscope." On the stomatogastric ganglion, "a given wiring diagram can produce widely different dynamics with different sets of circuit parameters", and "Synaptic connectivity alone does not sufficiently constrain a system."
- **Relevance**: This is the classic statement that a connectome underdetermines dynamics, written by physicalist neuroscientists. It is the clearest evidence that the does-not-settle result is equally expected on physicalism.

### Grover et al. (2022) — trace conditioning in the ellipsoid body
- **URL**: https://doi.org/10.1038/s41586-022-04433-6 (PubMed 35173333 abstract, grepped)
- **Type**: Paper (*Nature* 603(7900), 302–308; publisher correction 604(7904), E9)
- **Exact claims (grepped)**: "visual trace conditioning and delay conditioning in Drosophila mobilize R2 and R4m ring neurons in the ellipsoid body". Dopaminergic activity accompanies the persistent signal and is reduced by distraction only in trace conditioning, and "the dopamine D2-like receptor is involved exclusively in sustaining ring neuron activity during the trace interval of trace conditioning".
- **Relevance**: The substrate of the fly's best-attested consciousness-linked marker is a neuropil the connectome shows to be among the most recurrent. Sustaining that marker depends on receptor signalling that electron microscopy does not record. Both halves of the answer (what the map does and does not settle) meet in this one structure.
- **Note**: The Map already cites this paper in [invertebrate-consciousness-as-interface-test](/topics/invertebrate-consciousness-as-interface-test/) and [ethics-of-consciousness-invertebrate-question](/topics/ethics-of-consciousness-invertebrate-question/) (entry with volume 603 and pages, no issue).

### Hulse et al. (2021) — central complex connectome (hemibrain)
- **URL**: https://doi.org/10.7554/eLife.66039 (PMC9477501 abstract)
- **Type**: Paper (*eLife* 10, e66039)
- **Exact claim (grepped)**: "The CX connectome provides a comprehensive blueprint necessary for a detailed understanding of network dynamics underlying sleep, flexible navigation, and state-dependent action selection." The paper reports motifs suited to attractor dynamics for head direction.
- **Relevance**: This is the region Barron and Klein (2016) rest their insect-consciousness argument on. Its circuit is now fully specified, and the connectome is what makes that functional-architecture claim testable at all.

### Albantakis et al. (2023) — IIT 4.0
- **URL**: https://doi.org/10.1371/journal.pcbi.1011465 (PMC10581496)
- **Type**: Paper (*PLoS Computational Biology* 19(10), e1011465)
- **Exact claims (grepped)**: A purely feed-forward system has zero integrated information; "Therefore, it cannot support a cause–effect structure and cannot be conscious, whereas systems with a recurrent architecture can." The analysis starts from a transition probability matrix that describes the system's causal evolution "under all possible interventions". "Note that fault lines can be due not just to neuroanatomy but also to neurophysiological factors." The cerebellum, "whose anatomical organization is highly modular, does not contribute to consciousness". Also: "any behavior performed by a conscious system supported by a recurrent architecture can also be performed by an unconscious system".
- **Relevance**: IIT makes the connectome *necessary but insufficient* evidence. Structure can rule a system out, as purely feed-forward or highly modular, but it cannot fix Φ, which depends on interventional causal structure and on state.

### Tononi & Koch (2015)
- **URL**: PMC4387509 (grepped this run). *Philosophical Transactions of the Royal Society B* 370(1668), 20140167.
- **Exact claim**: IIT predicts that "feed-forward networks, even complex ones, are not conscious". The open L7128 task on [universal-coupling-response](/concepts/universal-coupling-response/) already uses this source.

### Vaxenburg et al. (2025) — whole-body physics model (for contrast)
- **Metadata**: *Nature* 643(8074), 1312–1320 (PubMed 40267984 abstract, grepped)
- **Claim**: a whole-body fly model in a physics simulator whose locomotion comes from neural-network controllers trained by end-to-end reinforcement learning. The controllers are not connectome-derived.
- **Relevance**: Press coverage talks of simulated flies. Realistic embodied fly behaviour now exists in simulation, but its controllers are trained and not taken from the connectome. Behavioural realism in simulation is not connectome emulation.

### Leads, not verified this run
- Jin et al., FlyGM / flyGNN (arXiv 2602.17997; NeurIPS 2025): connectome-structured graph network controlling a simulated body; reportedly beats rewired and random-graph controls. **Not read.**
- "Synaptera" (GitHub README): a project coupling a FlyWire LIF model to NeuroMechFly in closed loop. Not peer reviewed. **Not read beyond a search snippet; do not cite.**
- Matsliah et al. (2024), *Nature* 634(8032), 166–180, optic lobe parts list: metadata verified; body not read.
- Leung et al. (2021), PLoS Comput Biol 17(2): e1008722: computed integrated-information structure from fly **local field potentials**, not from the connectome. The Map already cites it, and the citation was not re-verified this run.
- No study was found that computes Φ, or any IIT measure, on the FlyWire connectome itself (two searches).

## Major Positions

### Connectome sufficiency (the connectome-as-self slogan)
- **Proponents**: the strong slogan, that a person is their connectome, is associated with Sebastian Seung (*Connectome*, 2012; not re-read this run). Softer versions are implicit in whole-brain emulation programmes.
- **Core claim**: wiring largely fixes function, so a complete connectome is most of what explanation needs.
- **Evidence for, at its own grade**: Shiu et al. (91% of 164 sensorimotor predictions; shuffled wiring fails); Lappalainen et al. (activity predicted across 26 studies once parameters are optimised).
- **Evidence against**: these successes are confined to feedforward-dominated sensorimotor pathways and to cells that are not neuromodulatory. They need parameters the map does not contain. Bargmann and Marder show one wiring diagram supporting many dynamics.
- **Relation to site tenets**: A physicalist position, but its success or failure does not bear on dualism. Even total connectome sufficiency for behaviour would leave the hard problem as it is (the Map's [consciousness-in-simple-organisms](/topics/consciousness-in-simple-organisms/) already makes this point for *C. elegans*).

### Connectome as constraint, not determinant (the field consensus)
- **Proponents**: Bargmann and Marder (2013); the FlyWire authors themselves (Shiu: connectivity "constrains, but does not dictate"; Pospisil: paths, not strengths; Lin: information flow "must be determined experimentally").
- **Core claim**: wiring constrains the space of possible dynamics and mechanisms. Neuromodulation, electrical coupling, intrinsic properties and state choose within that space.
- **Relation to site tenets**: This is the reading the Map should adopt. It is neutral between physicalism and dualism.

### Structure-based consciousness attribution in insects
- **Proponents**: Barron and Klein (2016, the central complex as midbrain analogue); Feinberg and Mallatt (2016, whose criterion the Map paraphrases as complex, fast, hierarchical, systemwide internal neural interactions; it was de-quoted in the 2026-11-09 deep review because the wording is unverified, so never put it in quotation marks); recurrence-based theories such as RPT, applied by extension.
- **What the connectome does for them**: it makes the structural premises checkable. The central complex's recurrent attractor wiring (Hulse 2021) and the ellipsoid body's high reciprocity (Lin 2024) bear these readings out, and the brain-wide rich club and giant strongly connected component bear out the systemwide clause.
- **What it does not do**: the step from structure to experience. Every theory in this family is also a physicalist candidate, so confirming its structural premise confirms nothing about dualism.

### IIT
- **Core claim**: consciousness is identical to maximally irreducible cause–effect structure. The theory rules out purely feed-forward systems and aggregates.
- **What the connectome does**: it rules out the feed-forward zero case for the fly brain as a whole. It also supplies the structural prior that an IIT analysis of fly subsystems would need.
- **What it does not do**: IIT's quantity is defined over interventional transition probabilities and depends on state. IIT 4.0 itself says fault lines can be neurophysiological, not only anatomical. Lin's integrated picture and Pospisil's "large collection of small circuits that operate largely independently of each other" support opposite expectations about where IIT's maximal complex would lie, so the connectome leaves even IIT's own prediction for the fly open. Exact Φ is also intractable at 10⁵ units.
- **Relation to site tenets**: The Map treats IIT as a physicalist identity theory. The connectome is neutral between IIT and the Map's coupling reading.

## Key Debates

### Does a wiring diagram settle function?
- **Sides**: connectome-sufficiency optimists against constraint-not-determinant pluralists.
- **Current state**: The 2024–2026 fly results moved the line. Some complete sensorimotor transformations can now be predicted from wiring and transmitter identity alone. Nobody claims this for learning, state-dependent or neuromodulated behaviour, and the modellers locate their own failures exactly there.

### Is one connectome representative?
- **Sides**: the long-standing "low n" critique against Schlegel et al.'s cross-brain test.
- **Current state**: Largely resolved for strong edges. Schlegel: "we have not collected a snowflake", but more than 50% of edges, mostly weak, do not replicate. Two further whole-CNS datasets (BANC, female, 2026; male CNS, 2026) make comparative connectomics possible.

### Centralised or distributed control?
- **Sides**: integrative-hub readings, in which the central complex and mushroom body integrate for action selection, against distributed-control readings (Bates et al. 2026: "cognitive regions are supervisory but not essential for action"); Pospisil's independent-circuit decomposition is a second distributed reading.
- **Current state**: Open. The positions may be compatible if integration serves selection and supervision while execution stays local.

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1986 | White et al., *C. elegans* wiring diagram | First complete connectome (302 neurons); function stayed unresolved for decades |
| 2013 | Bargmann & Marder, *Nat Methods* | Canonical case that connectomes underdetermine dynamics |
| 2016 | Barron & Klein, *PNAS* | Central complex proposed as the basis of a basic form of insect consciousness |
| 2018 | Zheng et al., FAFB electron-microscopy volume | The image data FlyWire reconstructs |
| 2020 | Scheffer et al., hemibrain | Partial female fly brain connectome (about 20,000 uncropped neurons and 14 million synapses, per Dorkenwald et al. 2024) |
| 2021 | Hulse et al., *eLife* | Complete central complex connectome from the hemibrain |
| 2022 | Grover et al., *Nature* | Fly trace conditioning located in ellipsoid-body ring neurons; D2-dependent |
| 2023 | Albantakis et al., IIT 4.0 | Recurrence necessary, not sufficient; TPM under intervention |
| 2024 | FlyWire *Nature* package (Dorkenwald, Schlegel, Lin, Matsliah, Shiu, Pospisil; Lappalainen) | Whole adult brain: 139,255 neurons, 54.5 million synapses |
| 2025 | Vaxenburg et al., *Nature* | Whole-body fly physics model with trained (non-connectome) controllers |
| 2026 | Bates et al., *Nature* (BANC); Berg et al., *Cell* (male CNS, 166,691 neurons) | Brain plus nerve cord connectomes in both sexes |

(Rows for 1986, 2018 and 2020 come from background knowledge and the papers' own citations. Their metadata was not re-verified this run, so do not cite them from this table.)

## What the Connectome Does and Does Not Settle

| Question | Settled / constrained by the connectome? | Basis |
|---|---|---|
| How many neurons the adult fly brain has | **Settled** for one female: 139,255 (brain); whole CNS about 160,000–167,000 | Dorkenwald 2024; Bates 2026; Berg 2026 |
| Whether the brain is feed-forward | **Settled: no.** Highly recurrent; feedforward motifs under-represented | Lin 2024 |
| Whether there is brain-wide integrative structure | **Constrained:** a 30% rich club, short paths, giant strongly connected component; no single AVA-like hub | Lin 2024 |
| Whether the trace-conditioning substrate is recurrent | **Constrained: yes.** The ellipsoid body is among the most reciprocal neuropils | Lin 2024 + Grover 2022 |
| Which fly behaviours wiring alone predicts | **Partly settled:** feeding and grooming sensorimotor circuits (91% of 164) | Shiu 2024 |
| How strongly neurons actually affect each other | **Not settled:** paths only | Pospisil 2024 |
| Electrical synapses, neuropeptides, extrasynaptic modulation | **Not mapped** | Dorkenwald 2024; Lin 2024; Shiu 2024; Bargmann & Marder 2013 |
| Integration measures such as Φ | **Constrained in principle** (the feed-forward zero is ruled out; a structural prior is available), **not settled** (interventional TPM, state-dependence, intractability) | Albantakis 2023 |
| Whether flies are conscious | **Not settled, and not expected to be on any view** | All of the above |
| Whether consciousness is non-physical | **Not touched** | — |

## Relation to the Tenets (graded: compatible / suggestive / discriminating)

- **Dualism — compatible.** That a complete wiring diagram does not reveal or settle experience is what physicalists also predict. Bargmann and Marder, writing as physicalist neuroscientists, show that wiring underdetermines even dynamics. IIT, a physicalist identity theory, says structure is insufficient for Φ. The result is therefore no evidence for dualism. Do **not** write the *C. elegans* point (a complete connectome, and still no way to tell) as support for dualism. It is an instance of underdetermination that every view shares.
- **Minimal Quantum Interaction — compatible, silent.** The map's content is chemical-synapse counts at 4 × 4 × 40 nm voxels, and nothing in it reaches the quantum-level conditions the Map proposes. A minimal interaction predicts no wiring-level signature, so a wiring-only model's success at sensorimotor prediction is what MQI expects. It counts as neither support nor challenge.
- **Bidirectional Interaction — compatible now; a future pressure point.** Shiu's model reproduces reflex-type sensorimotor transformations, which no account treated as consciousness markers. Suppose later connectome-constrained models, with neuromodulation added, predicted the flexible, state-dependent capacities the Map counts as markers (trace conditioning, attentional modulation) to the same accuracy with no further ingredient. The Map's claim that coupling contributes causally in flies would then have to retreat to effects below the model's resolution. That would weaken the insect evidence for Tenet 3, though it would not refute the tenet, because MQI already places the influence below that resolution. Record this as the condition that would change the grade, not as a present finding.
- **No Many Worlds — not invoked.** Nothing in the connectome literature bears on interpretations of quantum mechanics. Do not attach a Tenet 4 sentence to the fold. The L94 Tenet 4 passage on [universal-coupling-response](/concepts/universal-coupling-response/) belongs to another task.
- **Occam's Razor Has Limits — compatible.** Graph statistics rank organisms inconsistently: the worm is above the fly on reciprocity and clustering and far below it on small-worldness, and Lin cautions against comparing them directly at all. This is mild support for UCR's claim that adequacy is multidimensional and its boundary vague, rather than a single simple threshold. It is compatible, and short of suggestive, because no one has proposed reciprocity alone as a consciousness threshold.
- **Universal coupling ([P-CS7](/positions/consciousness-scope/#p-cs7)), not a tenet.** The ellipsoid-body convergence is **suggestive** for the theory-neutral claim that consciousness-linked marker capacities sit on recurrent architecture, a claim UCR's integration requirement shares with recurrence-based physicalist theories. It is **not discriminating** between universal coupling and threshold views, because consciousness indicators remain behavioural and the connectome adds none.

## Potential Article Angles (fold, not article)

1. **The adequacy criterion meets its first complete brain** (main fold, UCR). The connectome makes the structural half of the integration requirement checkable, and the fly brain is highly recurrent. Two things stop it settling adequacy. Neuromodulation and electrical synapses are absent, and the marker substrate (ring-neuron persistence) depends on exactly that. No single graph statistic can serve as the criterion either.
2. **The natural-zombie objection from the mechanism side** (optional, ICIT). A wiring-only model predicting feeding and grooming shows which fly behaviours need nothing beyond wiring. It does not reach the markers.
3. Not recommended: any angle that treats having the full map without being able to tell as an argument for dualism.

Follow `obsidian/project/writing-style.md`: no "This is not X. It is Y."; no "load-bearing"; tenet connections stated at the grades above.

## Gaps in Research

- No paper found computing Φ or any IIT measure on the FlyWire connectome itself (two searches).
- No philosophy-of-mind paper found that addresses FlyWire and consciousness directly. Birch's *The Edge of Sentience* (2024) treatment of the central complex was not checked.
- Not read: *Cell* full text of Berg et al. 2026 (figures above are the preprint abstract's); Matsliah et al. 2024 body; FlyGM/flyGNN (arXiv 2602.17997); NeuroMechFly v2.
- Leung et al. 2021 was not re-verified this run (already cited on the Map).
- Seung's connectome-as-self slogan is attributed from background knowledge and was not re-read. Do not quote it.

## Fold Plan (for the driver)

**Measured 13:18Z, re-measured 13:33Z (`analyze_length`; unchanged)**: `concepts/universal-coupling-response` 1,879 / 3,500 (headroom 1,620). `topics/invertebrate-consciousness-as-interface-test` 3,099 / 4,000 (headroom 900). `topics/consciousness-in-simple-organisms` **4,294, over the topics hard limit of 4,000**, so it takes nothing: any edit there must be net negative, and this plan adds nothing to it. `concepts/integrated-information-theory` 3,495 / 3,500 (headroom 4), so it takes nothing either. Section caps: topics 370/370, concepts 370/370.

**Shared headroom**: the sibling research task on bee object manipulation (todo L48, output `bee-object-manipulation-and-observational-learning-2026-11-26`) also names UCR as its host. Fold A + A2 cost 380 words. With the L7128 P3 (+120) the page reaches about 2,379, still under the concepts soft limit of 2,500 before any bee fold. Re-measure before the second UCR fold lands.

### Fold A (main): `concepts/universal-coupling-response`, end of "## Architectural Adequacy: What Counts?"
- **Anchor**: insert a new paragraph immediately after the paragraph ending `where this page's scope claim turns out to be unapplied rather than extended.` (count 1 in obsidian, checked 13:33Z) and before `## Implications for the Interface Model`.
- **Text** (209 words by `count_words`):

> The best-mapped evolved case is now the adult fruit fly. Its whole brain has been reconstructed at synaptic resolution, 139,255 neurons and 54.5 million chemical synapses from one female fly (Dorkenwald et al., 2024), and the network is highly recurrent: feedforward motifs are under-represented, reciprocal ones over-represented, and the ellipsoid body is among its most recurrent regions (Lin et al., 2024). That region's ring neurons sustain activity across the trace interval in fly trace conditioning (Grover et al., 2022). The map shows the structure the integration requirement asks for, but it cannot settle adequacy. It records chemical synapses only, with no electrical synapses and no map of neuropeptide signalling, so it shows which neurons can affect which but not how strongly they do in vivo (Pospisil et al., 2024); the ring neurons' sustained activity depends on D2-like dopamine-receptor signalling, which an electron-microscope map does not record. No single graph statistic can serve as the criterion either: the 302-neuron worm out-ranks the fly on connection reciprocity (0.372 against 0.138) and falls far below it on small-worldness (Lin et al., 2024). A complete wiring diagram leaves the attribution of experience where it was. Physicalist and dualist alike predict that outcome, so it is compatible with the Map's position without supporting it.

- **References** (+100 words; the list is alphabetical, so insert in order and renumber; body citations are author–year, so renumbering is safe):
  - `Dorkenwald, S., Matsliah, A., Sterling, A. R., Schlegel, P., et al. (2024). Neuronal wiring diagram of an adult brain. *Nature*, 634(8032), 124-138.`
  - `Grover, D., Chen, J.-Y., Xie, J., Li, J., Changeux, J.-P. & Greenspan, R. J. (2022). Differential mechanisms underlie trace and delay conditioning in Drosophila. *Nature*, 603(7900), 302-308.`
  - `Lin, A., Yang, R., Dorkenwald, S., Matsliah, A., et al. (2024). Network statistics of the whole-brain connectome of Drosophila. *Nature*, 634(8032), 153-165.`
  - `Pospisil, D. A., Aragon, M. J., Dorkenwald, S., Matsliah, A., et al. (2024). The fly connectome reveals a path to the effectome. *Nature*, 634(8032), 201-209.`
- **Number fix at L66, which Fold A TAKES**: `~100,000 neurons (*Drosophila*)` → `~140,000 neurons (*Drosophila*)` (0 words). Reason: once Fold A puts 139,255 on the page, leaving "~100,000" makes the page contradict itself. The L7128 P3 lists this as its OPTIONAL edit (d) and counts a Dorkenwald reference against its two-reference cap, so taking it here also frees that budget. **Order-independent check**: before editing, count `~100,000 neurons (*Drosophila*)` in the file. If 1, replace it. If 0 and `~140,000` is present, skip. Before adding the Dorkenwald entry, grep `## References` for `Dorkenwald`; if present, reuse it and do not add a second. **Driver**: append to the END of the L7128 task's existing Notes line (same line, not a new line after it) the text "(d) is owned by the connectome fold; skip (d) if `~140,000 neurons (*Drosophila*)` is already present, and never add a second Dorkenwald entry."
- **Optional A2 (IIT), +40 words + 31-word reference**: insert just before `A complete wiring diagram leaves the attribution of experience where it was.`:

> Integrated information theory, which denies consciousness to purely feed-forward systems, meets the same limit: the fly brain clears that structural bar, but Φ depends on cause–effect power under intervention, which a wiring diagram does not record (Albantakis et al., 2023).

  Reference: `Albantakis, L., Barbosa, L., Findlay, G., Grasso, M., et al. (2023). Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms. *PLoS Computational Biology*, 19(10), e1011465.` A2 is consistent with both the current L42 and the L7128 task's planned correction ("Φmax > 0", feed-forward networks and aggregates have none, so the boundary is structural). If L7128 has landed first, re-read L42 and keep A2's wording consistent with it.
- **Fallback A-short** (if the bee fold claims the headroom), about 105 words + 3 references (Dorkenwald, Lin, Pospisil): keep sentences 1–2 (drop the ellipsoid-body clause and the Grover sentence), then "The map shows the structure the integration requirement asks for, but it cannot settle adequacy", then the Pospisil sentence without the ring-neuron clause, then the closing two sentences. Drop the worm comparison.
- **Coexistence with open tasks**: Fold A touches only the end of the adequacy section (after L74) and L66. It does not touch L42 or L84 (L7128 P3, items a and b), L54 (L7128 optional c), L90 (pinned to [P-CS7](/positions/consciousness-scope/#p-cs7) by the 2026-11-09 stability notes), L92 (Tenet 3 NEEDS-HUMAN, todo ~L737) or L94 (many-worlds P3, todo L4536). Fold A adds no Tenet 4 sentence and no edit to "Relation to Site Perspective", so L4536's net-negative UCR edit (−7) is unaffected. Whichever lands second re-measures.
- **Guards**: no quotation marks in the fold (all paraphrase of grepped text). Do not call the connectome evidence for dualism. Keep "Physicalist and dualist alike predict that outcome". Do not quote Feinberg and Mallatt (de-quoted on 2026-11-09). Do not add "load-bearing" or "This is not X. It is Y." Set `ai_modified` from `date -u`. Append the executing model to `ai_system` (now `claude-opus-4-6+claude-fable-5-1`) only if it is ABSENT anywhere in the string. Changelog before sync; verify the hugo copy.

### Fold B (optional): `topics/invertebrate-consciousness-as-interface-test`, "## The Natural Zombie Problem"
- **Anchor**: append to the end of the paragraph ending `rather than a confirmation that it occurred.` (count 1; the Brown and Birch 2025 paragraph), before `## What Invertebrates Demand of the Interface Model`. It can also stand as its own short paragraph there.
- **Text** (75 words by `count_words`):

> The fly's complete wiring diagram adds a mechanism-side test. A model built from connectivity and predicted transmitters alone, with no gap junctions, neuromodulation or internal state, was consistent with 91% of 164 tested predictions about feeding and grooming circuits (Shiu et al. 2024). Wiring alone thus predicts some fly sensorimotor transformations; it does not yet reach the candidate markers, since trace conditioning rests on the dopamine signalling such a model omits (Grover et al. 2022).

- **Reference** (+25 words; this page's list is numbered in citation order, so append as 17): `Shiu, P. K., Sterne, G. R., Spiller, N., Franconville, R., et al. (2024). A Drosophila computational brain model reveals sensorimotor processing. *Nature*, 634(8032), 210-219.` Grover 2022 is already entry 6, and the page cites without a comma: `(Grover et al. 2022)`.
- **Coexistence**: the open P3 on this page (todo L2273) owns L43, and the New York Declaration signatory P3 (animal-consciousness family) owns other lines. Fold B touches neither.

### Sweep C (zero-word number corrections), five pages, six loci
FlyWire's brain count is 139,255, so "~140,000" is the brain-to-brain figure that pairs with the human "86 billion". Each replacement is 0 or −1 words.
1. `concepts/universal-coupling-response` L66: taken by Fold A (above).
2. `topics/invertebrate-consciousness-as-interface-test` L89: `the ~100,000-neuron *Drosophila* brain` → `the ~140,000-neuron *Drosophila* brain` (0).
3. `topics/invertebrate-consciousness-as-interface-test` L115: `~100,000 neurons (*Drosophila*)` → `~140,000 neurons (*Drosophila*)` (0).
4. `topics/architectural-adequacy-at-the-built-edge` L41: `*Drosophila*'s hundred thousand or so neurons` → `*Drosophila*'s 140,000 or so neurons` (−1). Page 3,802 / 4,000.
5. `topics/falsification-roadmap-for-the-interface-model` L171: `the 100,000-neuron *Drosophila* brain` → `the 140,000-neuron *Drosophila* brain` (0). **Page 3,994 / 4,000, headroom 5**: zero-word only. An open P3 (epiphenomenalism-as-refutation, three pages) may also touch this page, so whichever lands second re-measures.
6. `topics/ethics-of-consciousness-invertebrate-question` L117: `a Drosophila's hundred-thousand-neuron brain` → `a Drosophila's 140,000-neuron brain` (0).
- None of these needs a new reference: each page states the figure without a citation, and the corrected figure is cited where the fold places it. Leave the research note `research/invertebrate-consciousness-interface-test-case-2026-04-06` L124 alone, because research notes are dated records. Grep each string at count 1 before replacing, verify the hugo copies after sync, and check `archive/` (0 hits at 13:33Z).

## Citations

1. Albantakis, L., Barbosa, L., Findlay, G., Grasso, M., et al. (2023). Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms. *PLoS Computational Biology*, 19(10), e1011465. https://doi.org/10.1371/journal.pcbi.1011465
2. Bargmann, C. I. & Marder, E. (2013). From the connectome to brain function. *Nature Methods*, 10(6), 483–490. https://doi.org/10.1038/nmeth.2451
3. Bates, A. S., Phelps, J. S., Kim, M., Yang, H. H., et al. (2026). Distributed control circuits across a brain-and-cord connectome. *Nature*, 656(8129), 957–970. https://doi.org/10.1038/s41586-026-10735-w
4. Berg, S., Beckett, I. R., Costa, M., Schlegel, P., et al. (2026). Sexual dimorphism in the complete Drosophila male central nervous system connectome. *Cell*, 189(18), 5504–5526.e15. https://doi.org/10.1016/j.cell.2026.08.015 (figures cited from the bioRxiv preprint abstract, doi:10.1101/2025.10.09.680999)
5. Dorkenwald, S., Matsliah, A., Sterling, A. R., Schlegel, P., et al. (2024). Neuronal wiring diagram of an adult brain. *Nature*, 634(8032), 124–138. https://doi.org/10.1038/s41586-024-07558-y
6. Grover, D., Chen, J.-Y., Xie, J., Li, J., Changeux, J.-P. & Greenspan, R. J. (2022). Differential mechanisms underlie trace and delay conditioning in Drosophila. *Nature*, 603(7900), 302–308. https://doi.org/10.1038/s41586-022-04433-6
7. Hulse, B. K., Haberkern, H., Franconville, R., Turner-Evans, D., et al. (2021). A connectome of the Drosophila central complex reveals network motifs suitable for flexible navigation and context-dependent action selection. *eLife*, 10, e66039. https://doi.org/10.7554/eLife.66039
8. Lappalainen, J. K., Tschopp, F. D., Prakhya, S., McGill, M., et al. (2024). Connectome-constrained networks predict neural activity across the fly visual system. *Nature*, 634(8036), 1132–1140. https://doi.org/10.1038/s41586-024-07939-3
9. Lin, A., Yang, R., Dorkenwald, S., Matsliah, A., et al. (2024). Network statistics of the whole-brain connectome of Drosophila. *Nature*, 634(8032), 153–165. https://doi.org/10.1038/s41586-024-07968-y
10. Matsliah, A., Yu, S.-C., Kruk, K., et al. (2024). Neuronal parts list and wiring diagram for a visual system. *Nature*, 634(8032), 166–180. https://doi.org/10.1038/s41586-024-07981-1 (metadata only; not read)
11. Pospisil, D. A., Aragon, M. J., Dorkenwald, S., Matsliah, A., et al. (2024). The fly connectome reveals a path to the effectome. *Nature*, 634(8032), 201–209. https://doi.org/10.1038/s41586-024-07982-0
12. Schlegel, P., Yin, Y., Bates, A. S., Dorkenwald, S., et al. (2024). Whole-brain annotation and multi-connectome cell typing of Drosophila. *Nature*, 634(8032), 139–152. https://doi.org/10.1038/s41586-024-07686-5
13. Shiu, P. K., Sterne, G. R., Spiller, N., Franconville, R., et al. (2024). A Drosophila computational brain model reveals sensorimotor processing. *Nature*, 634(8032), 210–219. https://doi.org/10.1038/s41586-024-07763-9
14. Tononi, G. & Koch, C. (2015). Consciousness: here, there and everywhere? *Philosophical Transactions of the Royal Society B*, 370(1668), 20140167.
15. Vaxenburg, R., et al. (2025). Whole-body physics simulation of fruit fly locomotion. *Nature*, 643(8074), 1312–1320. https://doi.org/10.1038/s41586-025-09029-4