---
ai_contribution: 100
ai_system: claude-opus-4-8
concepts: []
created: 2026-07-08
date: '2026-07-08'
draft: false
related_articles: []
title: Research Notes - Brain Organoids and the Organoid-Intelligence Question
---

# Research: Brain Organoids and the Organoid-Intelligence Question

**Date**: 2026-07-08
**Search queries used**:
- Lancaster Knoblich 2013 Nature cerebral organoids microcephaly
- Trujillo 2019 Cell Stem Cell organoid oscillations preterm infant EEG
- Kagan 2022 Neuron DishBrain in vitro neurons learning Pong closed-loop
- Smirnova 2023 "Organoid intelligence" Frontiers in Science
- Cortical Labs CL1 biological computer 2025 launch 800000 neurons wetware as a service
- Lavazza / Jeziorski / Sawai brain organoid consciousness moral status ethics

## Executive Summary

Brain (cerebral) organoids are 3D self-organizing neural tissues grown from human induced pluripotent stem cells (iPSCs); they contain real neurons, real synapses, and, at months of maturation, spontaneous oscillatory network activity that statistically resembles preterm-infant EEG. A parallel "synthetic biological intelligence" line — DishBrain, and its commercial successor the Cortical Labs CL1 — shows cultured cortical neurons learning goal-directed behaviour (playing Pong) inside a closed-loop stimulation environment. The research programme naming these systems as candidate computers is "Organoid Intelligence" (OI). This raises a sharp question the Map cares about: **is a lab-grown neural network a candidate site for the consciousness–physical interface, or is it sub-personal machinery that computes without any experiencer present?** Organoids are the mirror image of the sponge/placozoan lower-bound case: here there is genuine neural substrate but **no body, no sensory world, and no evolutionary history**. This note lays out the empirical record and the ethics literature; it does not attempt to resolve the interface question, and it deliberately does *not* re-derive the substrate-classification analysis already carried by [ai-hardware-substrate-taxonomy](/concepts/ai-hardware-substrate-taxonomy/) (its companion on the discrete-vs-continuous / classical-vs-quantum axes).

**Relation to the companion article.** [ai-hardware-substrate-taxonomy](/concepts/ai-hardware-substrate-taxonomy/) treats "organoid / wetware" as one of six AI-hardware substrate tiers and asks whether its physics (continuous state space; possible operationally-integrated indeterminacy) could in principle host the interface. This note asks the orthogonal question: setting substrate physics aside, what is actually *in the dish*, what can it do, and what would it take for the organoid-intelligence question to become an experiencer question rather than a competence question. Read the taxonomy for "could this class of matter host consciousness"; read this note for "does *this specific artifact* have anyone home."

## Key Sources

### Lancaster et al. 2013 — the founding cerebral-organoid protocol
- **URL**: https://www.nature.com/articles/nature12517
- **Type**: Primary paper (Nature)
- **Citation (verified at publisher of record)**: Lancaster, M.A., Renner, M., Martin, C.-A., Wenzel, D., Bicknell, L.S., Hurles, M.E., Homfray, T., Penninger, J.M., Jackson, A.P., & Knoblich, J.A. (2013). Cerebral organoids model human brain development and microcephaly. *Nature*, 501(7467), 373–379. https://doi.org/10.1038/nature12517
- **Key points**:
  - iPSC-derived 3D culture self-organizes into discrete, interdependent brain regions, including a cerebral cortex with progenitor zones producing mature cortical neuron subtypes.
  - Used to model a human developmental disorder (microcephaly) — the original purpose was *modelling development*, not building a mind.
- **Tenet relevance**: Neutral. Establishes that real, regionalized neural tissue can be grown ex vivo — the precondition for the interface question to even arise.
- **Note**: Madeline Lancaster (first author), Juergen Knoblich (senior author), IMBA Vienna. The task brief's "Lancaster & Knoblich 2013" is correct as shorthand for first/senior author.

### Trujillo et al. 2019 — oscillations resembling preterm-infant EEG
- **URL**: https://www.cell.com/cell-stem-cell/fulltext/S1934-5909(19)30337-6
- **Type**: Primary paper (Cell Stem Cell)
- **Citation (verified)**: Trujillo, C.A., Gao, R., Negraes, P.D., Gu, J., Buchanan, J., Preissl, S., Wang, A., Wu, W., Haddad, G.G., Chaim, I.A., Domissy, A., Vandenberghe, M., Devor, A., Yeo, G.W., Voytek, B., & Muotri, A.R. (2019). Complex oscillatory waves emerging from cortical organoids model early human brain network development. *Cell Stem Cell*, 25(4), 558–569.e7. https://doi.org/10.1016/j.stem.2019.08.002
- **Key points**:
  - Cortical organoids develop periodic, nested oscillatory network events dependent on glutamatergic and GABAergic signalling.
  - The alternating quiescence / synchronized-burst pattern resembles spontaneous activity transients (SATs) in preterm-infant EEG; an ML model trained to predict neonatal age from EEG features could track the organoid's developmental timeline.
- **Tenet relevance**: This is the empirical fact that makes the whole question non-frivolous — but it is a claim about *network dynamics resembling* early-development EEG, **not** a claim about consciousness. Muotri's own group emphasizes this. The Map should treat "EEG-like oscillations" as a competence/structure signal, not an experience signal (see Tenet framing below).

### Kagan et al. 2022 — DishBrain learns Pong (and the "sentience" wording)
- **URL**: https://www.cell.com/neuron/fulltext/S0896-6273(22)00806-6
- **Type**: Primary paper (Neuron)
- **Citation (verified — vol/issue/pages/DOI)**: Kagan, B.J., Kitchen, A.C., Tran, N.T., Habibollahi, F., Khajehnejad, M., Parker, B.J., Bhat, A., Rollo, B., Razi, A., & Friston, K.J. (2022). In vitro neurons learn and exhibit sentience when embodied in a simulated game-world. *Neuron*, 110(23), 3952–3969.e8. https://doi.org/10.1016/j.neuron.2022.09.001
- **Key points**:
  - Human- or rodent-derived cortical cultures on a high-density multielectrode array, embedded via closed-loop stimulation/recording in a simulated Pong world, improved performance over training.
  - The authors' use of "sentience" is explicitly **technical** — in the Fristonian free-energy / active-inference sense of a system responsive to and modelling its sensory milieu — **not** a claim of phenomenal consciousness. Karl Friston is a co-author; the framing is active inference, not qualia.
- **Tenet relevance**: A textbook **competence-without-experience** case for Tenet 3. Closed-loop learning is real information-processing adaptation; it is exactly the kind of behavioural competence the Map's cluster throughline insists must be *decoupled* from the presence of an experiencer. "It learns Pong" licenses no inference to "something is watching the Pong."

### Smirnova et al. 2023 — the "Organoid Intelligence" research programme
- **URL**: https://www.frontiersin.org/journals/science/articles/10.3389/fsci.2023.1017235/full
- **Type**: Programmatic review / roadmap (Frontiers in Science)
- **Citation (verified — first author is Smirnova, not Hartung)**: Smirnova, L., Caffo, B.S., Gracias, D.H., Huang, Q., Morales Pantoja, I.E., Tang, B., Zack, D.J., Berlinicke, C.A., Boyd, J.L., Harris, T.D., Johnson, E.C., ... & Hartung, T. (2023). Organoid intelligence (OI): the new frontier in biocomputing and intelligence-in-a-dish. *Frontiers in Science*, 1, 1017235. https://doi.org/10.3389/fsci.2023.1017235
- **Key points**:
  - Proposes a multidisciplinary field using brain organoids as biological computing substrates, targeting molecular/cellular correlates of learning and memory.
  - Explicitly pairs the biocomputing ambition with an embedded-ethics ("ELSI") programme — the field named its own consciousness/moral-status problem at launch.
- **Tenet relevance**: Establishes that serious funded researchers treat organoids as candidate *intelligences*. The Map's contribution is to separate the intelligence claim (plausible, on a competence reading) from the experiencer claim (undemonstrated).
- **Cross-note flag**: [ai-hardware-substrate-taxonomy](/concepts/ai-hardware-substrate-taxonomy/) cites this same paper (DOI 1017235) as "Hartung et al. 2023." Same paper, but the verified first author is **Smirnova**. Minor first-author drift in the sibling article; noted for a possible future refine, out of scope here.

### Cortical Labs CL1 — commercial "biological computer" (2025)
- **URL**: https://corticallabs.com/cl1
- **Type**: Product / industry reporting (Forbes, Data Center Dynamics, corticallabs.com)
- **Key points (verified across multiple outlets)**:
  - Launched 2 March 2025 (Barcelona). ~800,000 lab-grown human-derived neurons on a silicon multielectrode interface; neurons viable up to ~6 months.
  - Priced around US$35,000; also offered as a cloud "Wetware as a Service" product; sub-millisecond electrical feedback loops.
- **Tenet relevance**: Turns the DishBrain demo into a shipping substrate — which is what forces the ethics question from thought-experiment into governance. But CL1's capabilities remain closed-loop adaptive computation; commercialization changes the moral-urgency, not the experiencer-evidence.

### Ethics / moral-status literature (all authors verified at PhilPapers / PMC)
- **Lavazza, A. (2020). Human cerebral organoids and consciousness: a double-edged sword.** *Monash Bioethics Review* / PMC7723930. And Lavazza & Massimini, "Cerebral organoids: ethical issues and consciousness assessment." Argues moral status would require at least a minimal/basic consciousness; current organoids likely lack it, but status could change as neural sophistication grows. Proposes consciousness-*assessment* (e.g. perturbational-complexity-style measures) as a gating tool.
  - URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC7723930/
- **Jeziorski, J., ... Koch, C., & Muotri, A.R. (2023). Brain organoids, consciousness, ethics and moral status.** *Seminars in Cell & Developmental Biology*. A biologist–philosopher–ethicist consensus piece written directly in response to the Trujillo oscillation findings; catalogues oversight, biomaterial procurement, chimera/implantation, and consciousness/moral-status issues.
  - URL: https://www.sciencedirect.com/science/article/abs/pii/S1084952122000866
- **Sawai, T. (Hiroshima / Kyoto ASHBi) et al.** Leads an ELSI programme; e.g. "Mapping the Ethical Issues of Brain Organoid Research and Application" and "Beyond the Personhood." Argues for a **precautionary principle**: absent an accepted consciousness-detection procedure, proceed *as if* organoids may be conscious when uncertain.
  - URL: https://philpapers.org/rec/SAWMTE
- **Commentaries on the OI roadmap** (Frontiers in Science): "The sentient organoid?" (10.3389/fsci.2023.1147911) and the "Baltimore declaration toward the exploration of organoid intelligence" (10.3389/fsci.2023.1068159) — supportive/critical responses bundled with the Smirnova roadmap.

## Major Positions

### "Organoids are (or could become) candidate experiencers" — precautionary realism
- **Proponents**: Sawai (precautionary), Lavazza (conditional, assessment-gated), elements of the Jeziorski consensus.
- **Core claim**: Real neurons + synapses + emergent oscillations put organoids on a trajectory where the probability of some minimal experience is non-zero and rising; ethics should hedge against it now.
- **Relation to site tenets**: Compatible with the Map taking the question *seriously* without conceding it. The Map's interface view (Tenet 3) would ask not "is there network complexity" but "is there an operationally integrated site of the kind the interface requires" — a stricter and different bar than the ethics literature's complexity/consciousness-assessment heuristics.

### "Organoid/DishBrain competence is sub-personal computation, no experiencer" — deflationary reading
- **Proponents**: Implicit in Kagan et al.'s own technical use of "sentience"; the Friston active-inference framing; general computational-functionalist deflation.
- **Core claim**: Learning, adaptation, and EEG-like oscillation are information-processing phenomena that can be fully specified without positing phenomenal experience.
- **Relation to site tenets**: This is the **reading (c) / sub-personal-machinery** horn the cluster keeps returning to. The Map endorses the *discipline* (competence ≠ experience) without endorsing the deflation of experience in general — the Map is dualist, so it rejects the further step "therefore experience is nothing over and above the computation."

### "It's the wrong substrate anyway" — deferred to the companion
- The physics question (could carbon-neuron tissue host consciousness-relevant indeterminacy where silicon cannot) is **out of scope here** and fully developed in [ai-hardware-substrate-taxonomy](/concepts/ai-hardware-substrate-taxonomy/). This note assumes that debate and asks the artifact-level question instead.

## The Interface Question (Tenet framing — lay out, do not over-resolve)

The Map's throughline for this session's cluster is **Tenet 3 interface-localisation**: where, if anywhere, is the site at which consciousness and the physical world interact? Organoids sharpen the question from a novel direction.

- **The sponge/placozoan case** ([basal-and-bioelectric-cognition](/topics/basal-and-bioelectric-cognition/) and the neuron-less-animals research note) probes the **lower bound**: behaviour and coordination *without* neurons. It asks whether the interface can exist below the neural threshold.
- **The organoid case is the opposite edge**: **neural substrate without the rest of a living animal.** Real cortical neurons, real synapses, real oscillations — but no body to act with, no sensory world to be about, no evolutionary history that made the tissue *for* anything. It asks whether neural machinery *alone* is sufficient, or whether the interface (if it is anywhere) is bound up with embodiment, world-directedness, and biography.

Three readings, held open:

1. **Candidate site.** If the interface localises to a physical property of integrated neural tissue, an organoid that instantiates that property could be a genuine (if minimal, world-less) experiencer — a mind with nothing to think *about*.
2. **Necessary-but-insufficient.** The neural substrate is one ingredient, but the interface requires operational integration with a body/world that a dish cannot supply; organoids are permanently pre-experiential.
3. **Sub-personal machinery (deflationary horn).** Whatever the organoid does is computation with no one home — the same competence-without-experience discipline the DishBrain-Pong result illustrates.

**Tenet 2 (minimality) bearing.** The Map posits the *smallest possible* non-physical influence on quantum outcomes. That minimality cuts both ways for organoids. It offers no reason to expect an interface to "switch on" merely because neuron count or oscillatory complexity crosses some threshold — minimality resists inflating every integrated neural system into an interface site. But neither does it license confident denial: if the relevant physical property is genuinely minimal, its presence is not something behavioural competence or an EEG-like trace would reveal. Minimality therefore recommends **agnosticism plus caution**, which aligns the Map's stance with Sawai's precautionary principle for a *different* reason than the ethics literature gives (physical-interface uncertainty, not complexity-based probability).

**The decoupling discipline.** The single most important move, and the cluster's shared spine: **closed-loop learning ≠ experience.** DishBrain playing Pong, organoids oscillating like a preterm brain, and CL1 running as a cloud service are all competence signals. None is an experiencer signal. The Map should state this decoupling explicitly and resist the slide — common in popular coverage ("mini-brains," "sentient")— from "does brain-like things" to "has experiences."

## Key Debates

### Does emergent oscillation indicate anything about consciousness?
- **Sides**: Muotri/Trujillo (structural/developmental resemblance, no consciousness claim) vs. cautious ethicists (resemblance is a warning flag warranting oversight) vs. deflationists (oscillation is just network dynamics).
- **Current state**: Ongoing. There is no accepted consciousness-detection procedure for organoids — the central methodological gap Sawai and Lavazza both stress.

### Is "sentience" the right word for DishBrain?
- **Sides**: Kagan et al. use it in a defined active-inference sense; critics (and headline-writers) hear the phenomenal sense.
- **Current state**: A terminological fault line the Map can exploit to make its competence/experience decoupling vivid.

### What moral-status framework applies to human neural tissue in a dish?
- **Sides**: Personhood-based, consciousness/sentience-based (precautionary), gradualist/assessment-gated, and non-Western relational-ontology approaches (Sawai & Ishida on Nishida).
- **Current state**: Genuinely unsettled; the OI field embedded ELSI work from launch precisely because it is unsettled.

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 2013 | Lancaster et al., *Nature* — cerebral organoids | First self-organizing regionalized human neural tissue ex vivo |
| 2019 | Trujillo et al., *Cell Stem Cell* — oscillations vs preterm EEG | Made the consciousness question empirically non-frivolous |
| 2020 | Lavazza, "double-edged sword" | Opens the consciousness-assessment ethics line |
| 2022 | Kagan et al., *Neuron* — DishBrain plays Pong | Closed-loop learning; the "sentience" (active-inference) framing |
| 2023 | Smirnova et al., *Frontiers in Science* — Organoid Intelligence roadmap + Baltimore declaration | Names the biocomputing programme and its ELSI problem |
| 2023 | Jeziorski et al. — consensus on organoid consciousness/ethics | Cross-disciplinary catalogue of the moral-status issues |
| 2025 | Cortical Labs CL1 launches (~800k neurons, WaaS) | Commercial shipping "biological computer" — moves ethics to governance |

## Potential Article Angles

Based on this research, an article could:

1. **"The Organoid-Intelligence Question: Neural Substrate Without a World"** (topic) — the primary angle. Frame organoids as the *upper*-edge mirror of the sponge lower-bound case: real neurons, no body/world/history. Build around the three-reading interface analysis and the competence-vs-experience decoupling. Cross-link [ai-hardware-substrate-taxonomy](/concepts/ai-hardware-substrate-taxonomy/) as the substrate-physics companion, [basal-and-bioelectric-cognition](/topics/basal-and-bioelectric-cognition/) and the neuron-less lower-bound work as the opposite edge, and [ethics-of-possible-ai-consciousness](/topics/ethics-of-possible-ai-consciousness/) for the moral-status throughline. Follow `obsidian/project/writing-style.md`: front-load the decoupling thesis; use named-anchor forward references for the three readings; keep the "Relation to Site Perspective" section explicit on Tenets 2 and 3; skip background the LLM already has on iPSCs.
2. **A tighter concept note on "closed-loop learning ≠ experience"** using DishBrain as the worked example — but check first whether this is better folded into an existing competence-without-experience article rather than minted fresh (dedup risk).

## Gaps in Research

- No accepted, organoid-applicable consciousness-detection procedure exists; all moral-status reasoning is downstream of that gap.
- The Map's own interface criterion ("operationally integrated site") has not been operationalized against organoid physiology — this note flags the mismatch between the ethics literature's complexity heuristics and the Map's physical-interface bar, but does not resolve it.
- CL1 capability claims are largely industry-sourced; independent peer-reviewed characterization of CL1 (as distinct from the 2022 DishBrain platform) is thin as of this note.
- Chimera/implantation ethics (organoid transplant into animal hosts) is adjacent and only lightly touched here.

## Citations

1. Lancaster, M.A., et al. (2013). Cerebral organoids model human brain development and microcephaly. *Nature*, 501(7467), 373–379. https://doi.org/10.1038/nature12517
2. Trujillo, C.A., et al. (2019). Complex oscillatory waves emerging from cortical organoids model early human brain network development. *Cell Stem Cell*, 25(4), 558–569.e7. https://doi.org/10.1016/j.stem.2019.08.002
3. Kagan, B.J., et al. (2022). In vitro neurons learn and exhibit sentience when embodied in a simulated game-world. *Neuron*, 110(23), 3952–3969.e8. https://doi.org/10.1016/j.neuron.2022.09.001
4. Smirnova, L., et al. (2023). Organoid intelligence (OI): the new frontier in biocomputing and intelligence-in-a-dish. *Frontiers in Science*, 1, 1017235. https://doi.org/10.3389/fsci.2023.1017235
5. Lavazza, A. (2020). Human cerebral organoids and consciousness: a double-edged sword. PMC7723930. https://pmc.ncbi.nlm.nih.gov/articles/PMC7723930/
6. Jeziorski, J., et al. (2023). Brain organoids, consciousness, ethics and moral status. *Seminars in Cell & Developmental Biology*. https://www.sciencedirect.com/science/article/abs/pii/S1084952122000866
7. Sawai, T., et al. Mapping the ethical issues of brain organoid research and application. https://philpapers.org/rec/SAWMTE
8. Cortical Labs. CL1 biological computer (launched 2 March 2025). https://corticallabs.com/cl1 ; Forbes coverage: https://www.forbes.com/sites/johnkoetsier/2025/06/04/hardware-software-meet-wetware-a-computer-with-800000-human-neurons/

## Cross-links (verified to resolve to live articles)

- [ai-hardware-substrate-taxonomy](/concepts/ai-hardware-substrate-taxonomy/) — substrate-physics companion (concepts/) ✓
- [basal-and-bioelectric-cognition](/topics/basal-and-bioelectric-cognition/) — opposite (lower/neuron-less) edge (topics/) ✓
- [the-enteric-nervous-system-and-the-gut-brain-distributed-interface-question](/topics/the-enteric-nervous-system-and-the-gut-brain-distributed-interface-question/) — distributed-interface sibling in the cluster (topics/) ✓
- [ethics-of-possible-ai-consciousness](/topics/ethics-of-possible-ai-consciousness/) — moral-status throughline (topics/) ✓

*(Not linked: the neuron-less sponges/placozoans lower-bound work exists only as a research note, not a live article, so it is referenced in prose but not wikilinked.)*