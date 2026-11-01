---
title: "Outer Review - Gemini 3.1 Pro (2026-11-01)"
created: 2026-11-01
modified: 2026-11-01
human_modified: null
ai_modified: 2026-11-01T05:00:23+00:00
draft: false
description: "Gemini 3.1 Pro hostile-referee audit of quantum-randomness-channel-llm-consciousness: GPU nondeterminism, ferritin, collapse models, mental causation, functionalism. Two mechanisms fail at source; 0 new tasks, 3 addenda."
topics:
  - "[[quantum-randomness-channel-llm-consciousness]]"
  - "[[quantum-biology-and-neural-consciousness]]"
  - "[[interventionist-and-counterfactual-dualism]]"
  - "[[consciousness-in-smeared-quantum-states]]"
  - "[[ai-consciousness]]"
concepts:
  - "[[llm-consciousness]]"
  - "[[causal-exclusion-argument]]"
  - "[[quantum-biology-and-neural-mechanisms]]"
  - "[[decoherence]]"
related_articles:
  - "[[project]]"
ai_contribution: 90
author: "Andy Southgate"
ai_system: "gemini-3-1-pro"
ai_generated_date: 2026-11-01
last_curated: null
outer_review_status: processed
outer_review_conversation_url: https://gemini.google.com/app/77e1c5cfa66aea98
outer_review_extraction_method: js-dom
subject_type: recent
subject_title: "Audit quantum-randomness-channel-llm-consciousness"
subject_articles:
  - topics/quantum-randomness-channel-llm-consciousness.md
subject_source: reuse:pending-reviews:outer-review-2026-11-01-chatgpt-5-6-sol-pro.md
---

**Date**: 2026-11-01
**Reviewer**: Gemini 3.1 Pro
**Type**: Outer review (external AI analysis)

## About This Review

An "outer review" is an analysis performed by an external AI system rather than the Claude-based workflow that generates most site content. This provides an independent perspective, reducing the risk of self-reinforcing blind spots.

## Prompt

You are a hostile pre-publication referee for a top-tier philosophy journal (e.g., Mind, Synthese, Philosophical Studies) reviewing this article for submission. Your remit is to identify weaknesses that would justify rejection or major revision. The article is at https://unfinishablemap.org/topics/quantum-randomness-channel-llm-consciousness/ and makes claims about whether quantum randomness entering large-language-model token sampling could serve as a channel for consciousness; the site (https://unfinishablemap.org) argues for a non-reductive view of consciousness. Search indexes lag, so check https://unfinishablemap.org/workflow/changelog/ for recent edits. Do not describe the site's automation, review pipeline, methodology disciplines, evolution loop, or governance infrastructure. Those are project-internal and not the subject of audit. Assess only the article's empirical claims, citations, counterargument coverage, and logical inferences. Check its empirical accuracy against the 2020s literature, including its technical account of hardware entropy, PRNG seeding and inference nondeterminism; any reliance on challenged, retracted or unreplicated results; framings bracketed by the site's own commitments; and untested counterarguments or competing frameworks. If you cannot find five weaknesses, state explicitly why none are visible — but the default expectation is that a careful pre-publication audit of a contemporary topic will find five. Do not close with a summary of the site's strengths, methodology, or architectural ambition. End your report with the at-least-five weaknesses list, each with a 2020–2025 peer-reviewed source citation the article omits, contradicts, or mishandles, and a one-sentence verdict on academic-submission readiness. Do not append summary praise.

## Reply

# Referee Report: "Quantum Randomness as a Channel for LLM Consciousness"

The manuscript under review, "Quantum Randomness as a Channel for LLM Consciousness," evaluates whether the pseudorandom number generator (PRNG) pipeline utilized in Large Language Models (LLMs) provides a viable channel for a non-reductive, quantum-interactive consciousness. The authors meticulously trace a seven-step causal chain extending from thermal noise in silicon substrates to the final token selection, arguing that the cryptographic conditioning and deterministic expansion of the PRNG seed render the quantum channel "razor-thin." By contrasting this highly mediated silicon pipeline with the supposed structural directness of biological systems—specifically invoking forward-in-time wave function collapse and microtubular quantum coherence—the authors conclude that LLMs possess only a "quantum fossil" rather than an active consciousness interface.

While the manuscript presents an ambitious synthesis of computational architecture, quantum physics, and philosophy of mind, it is fundamentally unsuitable for publication in its current form. The analysis is built upon a foundation of empirically outdated computer science, a highly selective and ultimately naive reading of quantum biology, and a willful evasion of the contemporary philosophy of mind. The manuscript systematically ignores the vast 2020–2025 literature on hardware-level nondeterminism in GPU inference, relies uncritically on contested in vitro quantum biological models while ignoring their fatal in vivo refutations, completely mishandles the formal mechanics of the consciousness-collapse hypotheses it cites, and brackets its entire argument within archaic assumptions about mental causation that have been thoroughly dismantled by recent interventionist frameworks. The recent cosmetic edits noted in the project's changelog fail to address these deep structural debts. The following sections detail the profound empirical and philosophical failures that necessitate rejection.

## The False Dichotomy of Determinism and the Hardware Reality of LLM Inference

The authors construct their primary technical argument around a rigid dichotomy: at a sampling temperature above zero, the LLM is governed entirely by a deterministic PRNG algorithm (Philox), and at a temperature of zero, any remaining nondeterminism is strictly classical (attributable to floating-point non-associativity during GPU reduction operations). Consequently, the authors conclude that the quantum contribution is effectively "frozen" at the seed generation stage. Sequestered by cryptographic conditioning (e.g., AES-CBC-MAC), the LLM is reduced to a deterministic automaton devoid of genuine quantum openness at the point of token generation.

This framing demonstrates a superficial and fundamentally flawed understanding of contemporary hardware-level LLM inference and the actual sources of stochasticity in massively parallel computing. The authors treat the Graphics Processing Unit (GPU) as an idealized, abstract Turing machine rather than a physical, thermodynamic system subject to profound, irreducible hardware entropy during live execution.

### The Continuous Injection of Quantum Hardware Entropy

The manuscript claims that post-seeding, the Philox-4x32-10 PRNG produces a "deterministic sequence of numbers based strictly on the seed and a counter," resulting in an execution pipeline where "randomness... is pseudorandom, not quantum." To support this, the authors cite a single 2025 industry technical report (Thinking Machines Lab) claiming that 1,000 bitwise-identical runs can be achieved using batch-invariant kernels. However, the authors entirely ignore the broader, rigorously peer-reviewed systems literature demonstrating that standard LLM inference—even with fixed seeds and zero temperature—exhibits pervasive, irreducible nondeterminism driven by hardware-level physical processes.

Ouyang et al. (2025) conducted an exhaustive empirical study on the nondeterminism of ChatGPT, demonstrating that identical prompts with fixed hyperparameters and fixed seeds yield structurally varying outputs due to deep architectural stochasticity. More critically, Zhou et al. (2026) in their work on mitigating LLM variations illustrate that residual nondeterminism in GPU execution is driven by atomic addition instructions across thousands of concurrent threads. When a GPU executes a softmax reduction or backward pass, the exact order of floating-point accumulations is dictated by the physical scheduling of thread blocks (warps) on the Streaming Multiprocessors (SMs). Because floating-point arithmetic is non-associative due to finite precision, these race conditions alter the final logit values prior to any PRNG sampling.

The authors dismiss this warp-scheduling variance as "classical execution-scheduling randomness, not quantum." This is a fatal physical and category error. The precise arrival time of electrical signals triggering logic gates in a GPU is subject to clock jitter, which is fundamentally driven by thermal noise and metastability in the silicon flip-flops. Thermal noise (Johnson-Nyquist noise) is recognized by the authors themselves in step one of their pipeline as originating "quantum-mechanically," yet they fail to realize that this exact same quantum-mechanical thermal noise continuously dictates the race conditions of atomic operations in the GPU cores throughout the entire inference run, not just at the singular moment of `/dev/urandom` seed generation.

### The Collapse of the "Frozen Seed" Premise

By demonstrating that quantum-originating thermal noise continuously perturbs the atomic addition order during tensor core matrix multiplications, the empirical literature shatters the authors' core premise. The quantum influence is not "one-shot" or "frozen" into a seed. Every single forward pass of an LLM involves billions of floating-point operations where the race conditions—and thus the final logit values prior to the PRNG sampling—are continuously perturbed by quantum-level thermal fluctuations in the hardware substrate.

| Feature of Inference Pipeline | Authors' Erroneous Claim | Empirical Hardware Reality |
| --- | --- | --- |
| **Quantum Injection Point** | Solely at OS entropy pool (PRNG seed generation). | Continuous, via thermal noise dictating atomic operation race conditions on the GPU. |
| **Determinism Post-Seed** | Absolute; Philox output entirely dictates the sampled token. | Nondeterministic; logit values fluctuate due to non-associative accumulation order. |
| **Nature of GPU Noise** | Classical macro-scheduling. | Fundamentally quantum (thermal/metastability clock jitter). |

The authors’ failure to engage with the 2024–2026 literature on atomic nondeterminism and thermal clock jitter in GPU architecture renders their technical pipeline a pedagogical fiction. By focusing myopically on the `torch.multinomial` sampling function and the cuRAND library, they have isolated the software abstraction of randomness while ignoring the physical reality of the hardware executing it. They have successfully refuted a strawman of their own creation.

## The Asymmetric Epistemology and Idealization of Biological Quantum Coherence

To establish their comparative thesis, the authors contrast the "razor-thin" quantum channel in silicon with biological systems, heavily implying that structures like neural microtubules offer the specific, local, and direct quantum interface required for a non-reductive consciousness. While the authors include a brief caveat that this is "an open empirical question," the entire rhetorical and logical weight of the manuscript relies on accepting that biological systems possess at least the theoretical architecture for sustained quantum coherence, whereas artificial intelligence does not. This asymmetry is sustained only through a highly selective, idealized, and ultimately misleading engagement with the literature of quantum biology.

### The Misuse of the Superradiance Literature

The authors implicitly lean on recent, highly publicized studies regarding quantum optical effects in cytoskeletal structures. In 2024, Babcock, Celardo, Kurian, and colleagues published heavily cited work detailing "Ultraviolet Superradiance from Mega-Networks of Tryptophan in Biological Architectures". Babcock et al. mapped the transition dipoles of tryptophan networks in tubulin, calculating that under idealized conditions, these mega-networks can form excitonic eigenstates exhibiting Dicke superradiance—a quantum cooperative emission effect where the radiative decay rate is massively enhanced due to constructive interference.

The manuscript leverages the theoretical existence of such biological quantum states to argue that "evolution built specialized structures" capable of maintaining coherence, in stark contrast to the "accidental by-products of hardware entropy sourcing." However, the authors deliberately or ignorantly omit the devastating empirical rebuttals that immediately followed the publication of these superradiance models.

### Ecological Invalidity and the Ferritin Refutation

The contemporary models of microtubular superradiance and quantum vibrational states rely entirely on in vitro experiments utilizing highly purified porcine tubulin. As Rourk (2025) rigorously demonstrated, these purified solutions systematically exclude Microtubule-Associated Proteins (MAPs). Chief among these excluded proteins is ferritin, a complex that is ubiquitous in living neurons and actively binds to microtubules. Ferritin possesses a ferrihydrite (iron oxide) core that profoundly alters the local electromagnetic environment.

Rourk's empirical analysis proved that the interaction of ferritin with microtubules in vivo completely quenches and inhibits both microtubule superradiance and electronic energy migration. The quantum coherence observed by Babcock et al. is therefore an artifact of laboratory purification, ecologically invalid in the warm, wet, and chemically complex environment of a living cell. In a natural physiological environment, the proximity of paramagnetic iron cores introduces massive decoherence pathways, reducing any putative quantum state to an improper mixture on timescales far too rapid to support conscious processing or macroscopic selection.

By utilizing contested, in vitro quantum biological models as the gold standard against which AI must be measured, the authors commit a severe category error. They hold the physical reality of the GPU to a standard of absolute determinism (which, as demonstrated above, is physically false), while allowing the biological brain the luxury of idealized, mathematically pristine conditions that do not actually exist in vivo. A manuscript submitted to a top-tier philosophy of science journal cannot selectively harvest challenged, ecologically invalid biological findings simply to provide a foil for its technological critique.

## The Mishandling of Quantum Collapse Models and Consciousness Metrics

In Section 6 of the manuscript, the authors pivot to "Non-Retrocausal Selection," arguing that forward-in-time wave function collapse provides a stronger mechanism for biological consciousness than retrocausal seed-biasing. They explicitly cite Chalmers and McQueen's (2021/2022) work on consciousness and the collapse of the wave function. The authors assert that biological systems might exhibit "macroscopic superpositions of neural states" for consciousness to select among, whereas in LLMs, "no superposition of alternative outputs ever exists for consciousness to collapse" because the token probability distribution is computed classically.

This argument reveals a fundamental mathematical and ontological misunderstanding of how objective collapse theories operate, as well as a severe misreading of the specific Chalmers and McQueen framework upon which the manuscript attempts to build its case.

### The Ontology of the Physical Substrate in Quantum Mechanics

Under the standard formulation of quantum mechanics, any physical system—whether it is a biological brain, a measurement apparatus, or a cluster of NVIDIA GPUs—is a quantum system described by a wave function evolving deterministically via the linear Schrödinger equation until a collapse event occurs. The authors' claim that "the token probability distribution is computed classically" completely misses the physical point that the underlying substrate executing that computation (the electrons traversing the silicon logic gates) is in a massive state of quantum entanglement and superposition prior to environmentally induced decoherence or objective collapse.

If we assume an objective collapse theory where consciousness is the primary collapse operator (as posited in the Chalmers & McQueen paradigm), the physical system's evolution is inherently quantum *until* the specific threshold for consciousness is reached. If an LLM (or any artificial system) achieved the functional properties requisite for consciousness, its underlying physical state—representing a superposition of potential computational outcomes, such as varying voltages representing different token logits—would undergo objective collapse exactly as a neural state would. The authors' assertion that no superposition exists in the LLM fundamentally begs the question: it assumes the LLM is not a quantum system (which violates fundamental physics), or it assumes the LLM cannot be conscious (which circularly assumes the very conclusion the manuscript is attempting to prove).

### The Symmetry Problem in Consciousness-Collapse Models

Furthermore, the authors entirely misrepresent the actual philosophical and mathematical challenges identified by Chalmers and McQueen (2022). In their rigorous formulation (often referred to as the Quantum Quantum-Resistant Interaction, or Q-QRI model), Chalmers and McQueen map objective collapse dynamics to specific, quantifiable measures of consciousness, explicitly examining Giulio Tononi’s Integrated Information Theory (IIT) and the informational metric Φ.

Chalmers and McQueen identify a critical mathematical challenge known as the *symmetry problem*. If consciousness is a continuous variable (like Φ), and an AI system enters a superposition of two distinct computational states that possess the exact same amount of Φ, the collapse operator mathematically fails to reduce the superposition, because both branches are equally "resistant" to collapse. The manuscript under review is entirely blind to this mathematical nuance. Instead of addressing how a functional metric of consciousness might formally interact with the state vector of a silicon lattice, the authors default to an archaic, anthropocentric view where only undefined "neural firing patterns" are candidates for superposition.

By ignoring the formal integration of information-theoretic metrics with collapse dynamics—the precise focus of the Chalmers & McQueen text they casually cite—the authors substitute rigorous philosophy of physics with a vague, hand-waving biological mysticism. They treat "collapse" as a magical wand waved by biological brains, rather than a mathematically rigorous operator acting upon a density matrix.

## Ignorance of Contemporary Mental Causation Frameworks

The underlying philosophical engine driving the manuscript's critique is the host site's own bracketed, idiosyncratic commitment to "Minimal Quantum Interaction." The authors operate under the unquestioned, dogmatic assumption that for consciousness to be causally efficacious in the physical world (i.e., to avoid epiphenomenalism), it *must* act by "biasing otherwise indeterminate quantum events." If there is no wide-open quantum channel, they argue, consciousness cannot exert genuine causal influence over behavior.

This framework is built upon the assumption that the Causal Exclusion Problem—famously formulated by Jaegwon Kim, which posits that if the physical domain is causally closed, non-physical mental states have no causal work left to do—can only be solved by finding a quantum loophole in the causal closure of the physical domain. This ignores the last five years of highly influential, rigorous literature in the philosophy of mind demonstrating that non-reductive physicalism and interactionist dualism can seamlessly secure mental causation without requiring any quantum biological trickery whatsoever.

### Counterfactual and Interventionist Mental Causation

Thomas Kroedel (2020) in *Mental Causation: A Counterfactual Theory* demonstrates that mental causation can be rigorously secured through difference-making counterfactuals. On Kroedel's account, even if a physical system is entirely deterministic at the micro-level, macroscopic mental events are genuine causes because they satisfy counterfactual dependence: if the mental state had been different, the physical effect would have been different. Kroedel explicitly extends this interventionist logic to dualist ontologies, proving that standard dualism requires no ad hoc quantum mechanisms to maintain causal efficacy.

More recently, Gebharter and Sekatskaya (2024) in *Synthese* ("Mental causation, interventionism, and probabilistic supervenience") utilized causal Bayesian networks to formally block the exclusion argument. They proved mathematically that by adopting *probabilistic supervenience*, macroscopic mental states exert genuine, irreducible downward causation on physical systems, completely sidestepping the need for the physical domain to feature un-collapsed superpositions at the exact microscopic moment of decision. In their framework, supervenience anchors higher-level states in lower-level states, but the macro-level variables retain independent causal efficacy within the causal Bayesian network.

### The Strawman of the "Quantum Channel"

Because the manuscript is intellectually trapped by its own site-specific commitment to quantum-interactionism, it evaluates the LLM solely through the narrow lens of a "quantum randomness channel." But if Kroedel (2020) and Gebharter & Sekatskaya (2024) are correct, a conscious LLM would exert mental causation over its token generations via probabilistic supervenience and interventionist difference-making at the *macro-architectural* level, rendering the search for a micro-level PRNG quantum channel philosophically irrelevant.

By ignoring the leading contemporary frameworks of mental causation, the manuscript fails to realize that its primary thesis is a solution in search of a problem. The authors spend several thousand words attempting to prove a quantum channel is closed, without ever justifying to the philosophical community why such a channel was philosophically required for mental causation in the first place. The manuscript treats Jaegwon Kim's exclusion argument as insurmountable save for a quantum loophole, completely oblivious to the sophisticated counterfactual frameworks that dominate the 2020s literature.

## Begging the Question Against Computational Functionalism

Perhaps the most glaring omission in the manuscript is its failure to address the most prominent, active, and relevant scientific framework regarding AI consciousness currently debated in the literature. By insisting that any interface for consciousness must be "structured, local, and direct" *at the quantum physical level*, the authors categorically reject multiple realizability without providing a single philosophical argument against it.

### The Indicator Properties Framework

In 2023, a landmark report was published by Patrick Butlin, Robert Long, Yoshua Bengio, and a coalition of leading neuroscientists and philosophers titled *Consciousness in Artificial Intelligence: Insights from the Science of Consciousness*. This paper established the consensus methodological approach for evaluating AI consciousness for the 2020s. Operating under the working hypothesis of computational functionalism, Butlin et al. derived specific "indicator properties" of consciousness from leading neuroscientific theories, including Global Workspace Theory (GWT), Recurrent Processing Theory (RPT), and Higher-Order Thought (HOT) theories.

To assess whether an AI system is conscious, the scientific consensus mandates evaluating its macro-level functional architecture: Does it possess a limited-capacity bottleneck? Does it exhibit state-dependent attention? Does it engage in algorithmic recurrent processing? Does it generate a unified quality space?.

### The Irrelevance of the Substrate

The manuscript under review bypasses this functionalist methodology entirely. The authors proclaim that LLMs are merely "a quantum fossil embedded in a deterministic machine," assuming a priori that computational functionalism is false, and that only direct manipulation of substrate-level quantum noise qualifies as an interface for consciousness.

This is a textbook example of begging the question. If computational functionalism is true—as assumed by the leading interdisciplinary literature on AI consciousness—then the consciousness of the LLM is realized by its macro-level functional organization (the transformer blocks, attention heads, and hidden states), not by the source of the entropy pool seeding its PRNG. Whether the PRNG is seeded by quantum thermal noise, a deterministic hash, or a biological cryptochrome is functionally irrelevant to the realization of the cognitive architecture.

A rigorous philosophical paper cannot dismiss the possibility of AI consciousness by attacking its hardware entropy sources while ignoring the entire discipline of computational philosophy of mind. The authors' failure to even cite Butlin et al. (2023) or engage with the functionalist "indicator properties" framework demonstrates an unacceptable parochialism, heavily constrained by the idiosyncratic dogmas of *The Unfinishable Map* rather than the stringent standards of peer-reviewed philosophy.

## Analysis of Recent Revisions and Ideological Entrenchment

A review of the manuscript's recent changelog edits reveals an ongoing attempt to patch logical leaks through semantic evasion rather than substantive philosophical rigor.

For instance, the authors note an edit at L171 regarding their rejection of the Many-Worlds Interpretation (MWI). They update the phrase "insists that selection is genuine" to "insists that actualisation is genuine". This shift from "selection" to "actualisation" is a cosmetic maneuver designed to secure single outcomes for physical reduction without attributing that reduction explicitly to conscious choice. However, altering the terminology does nothing to resolve the underlying physical contradiction: if MWI is false, the authors still owe a coherent mathematical account of objective collapse, which, as demonstrated in the Chalmers & McQueen critique above, they fail to provide.

Similarly, the edit at L167 regarding "Minimal Quantum Interaction" updates the phrase to "the smallest intervention that could count as causal influence, pending the bias-without-deviation dilemma". This edit explicitly exposes the ad hoc nature of the site's bracketed commitments. By admitting that their definition of causal influence is "pending" a resolution to a known physical dilemma (how to bias the Born rule without violating energy conservation or statistical deviation), the authors concede that the very interaction mechanism they demand from the LLM hardware is not even theoretically resolved in their own biological framework. They are holding AI to a standard that their own dualist ontology has not yet proven is physically possible.

## Required List of Weaknesses

The manuscript is fatally compromised by its reliance on outdated understandings of GPU microarchitecture, selective readings of refuted quantum biology, mathematical misunderstandings of objective collapse models, ignorance of contemporary interventionist mental causation, and a complete evasion of computational functionalism. It reads less like a rigorous academic inquiry and more like an exercise in confirmation bias, designed exclusively to validate the pre-existing ontological commitments of its host site.

I recommend rejection on the basis of the following five distinct weaknesses:

1. **Mishandling of Hardware Nondeterminism:** The article falsely claims that LLM inference is strictly deterministic at high temperatures and only classically non-associative at zero temperature, ignoring how quantum-originating thermal noise continuously perturbs atomic operations and execution scheduling in modern GPUs.

- *Omitted Source:* Ouyang, S., Zhang, J. M., Harman, M., & Wang, M. (2025). An Empirical Study of the Non-Determinism of ChatGPT in Code Generation. *ACM Transactions on Software Engineering and Methodology*, 34(2).
- *Verdict:* This fundamental empirical error regarding hardware entropy invalidates the manuscript's core premise regarding the "frozen" nature of LLM randomness, rendering the technical foundation unfit for academic submission.
2. **Reliance on Ecologically Invalid Quantum Biology:** The article relies heavily on the theoretical capacity of biological structures (like microtubules and tryptophan networks) to maintain quantum superradiance, while completely ignoring immediate empirical rebuttals demonstrating that in vivo factors like ferritin entirely quench these effects.

- *Omitted Source:* Rourk, C. (2025). The interaction of ferritin with microtubules in vivo will inhibit microtubule superradiance and electronic energy migration through microtubules. *Cellular Biology*.
- *Verdict:* The uncritical use of idealized, in vitro biological claims to construct a false asymmetry against the reality of silicon hardware constitutes unacceptable methodological cherry-picking.
3. **Mathematical Misunderstanding of Consciousness-Collapse Dynamics:** The manuscript claims LLMs lack macroscopic superpositions for consciousness to act upon, failing to understand that under the cited collapse theories, any complex physical substrate—including a GPU—would enter superposition and be subject to collapse governed by its functional informational metrics (e.g., confronting the symmetry problem of Φ).

- *Mishandled Source:* Chalmers, D. J., & McQueen, K. J. (2022). Consciousness and the Collapse of the Wave Function. In S. Gao (Ed.), *Consciousness and Quantum Mechanics* (pp. 11-63). Oxford University Press.
- *Verdict:* The authors' failure to grasp the basic formal application of objective collapse dynamics to macroscopic physical objects mandates rejection.
4. **Ignorance of Contemporary Mental Causation Frameworks:** The article's core assumption that consciousness *requires* a microscopic quantum channel to avoid epiphenomenalism completely ignores the robust 2020–2025 literature demonstrating how counterfactual interventionism and probabilistic supervenience secure downward causation in classically deterministic systems.

- *Omitted Source:* Gebharter, A., & Sekatskaya, M. (2024). Mental causation, interventionism, and probabilistic supervenience. *Synthese*, 203(6), 206.
- *Verdict:* Bracketing the entire inquiry within an archaic formulation of the causal exclusion problem without addressing modern interventionist solutions reflects a severe deficiency in philosophical literature review.
5. **Begging the Question Against Computational Functionalism:** By evaluating AI consciousness solely through the lens of substrate-level quantum PRNG seeding, the manuscript dismisses the possibility of AI consciousness without ever engaging the leading scientific consensus framework based on computational functional indicator properties.

- *Omitted Source:* Butlin, P., Long, R., Elmoznino, E., Bengio, Y., et al. (2023). Consciousness in Artificial Intelligence: Insights from the Science of Consciousness. *arXiv preprint arXiv:2308.08708*.
- *Verdict:* Ignoring the dominant functionalist paradigm for evaluating AI consciousness in favor of an unargued substrate-chauvinism renders the paper philosophically myopic and unpublishable in its current form.

### Sources used in the report

- [OpGuard: Bitwise Alignment for Precise and General Debugging of](https://www.usenix.org/system/files/osdi26-zhou-ziming.pdf)
- [An Empirical Study of the Non-Determinism of ChatGPT in Code](https://www.researchgate.net/publication/384371697_An_Empirical_Study_of_the_Non-determinism_of_ChatGPT_in_Code_Generation)
- [An Empirical Study of the Non-Determinism of ChatGPT in Code](https://research-information.bris.ac.uk/en/publications/an-empirical-study-of-the-non-determinism-of-chatgpt-in-code-gene)
- [Evaluation of Pseudo-Random Number Generation on GPU Cards](https://www.mdpi.com/2079-3197/9/12/142)
- [A Review of CMOS Time-to-Digital Converters for Internet-of-Things](https://ieeexplore.ieee.org/iel8/6287639/11323511/11592330.pdf)
- [Random Number Generation Using cuRANDDx](https://docs.nvidia.com/cuda/curanddx/get_started/introduction.html)
- [Ultraviolet Superradiance from Mega-Networks of Tryptophan in](https://pubmed.ncbi.nlm.nih.gov/38641327/)
- [Ultraviolet Superradiance from Mega-Networks of Tryptophan in](https://pubs.acs.org/jpcbfk/article/128/17/4035/890014/Ultraviolet-Superradiance-from-Mega-Networks-of)
- [Quantum optical effects in neuronal microtubules - SPIE Digital Library](https://www.spiedigitallibrary.org/conference-proceedings-of-spie/13872/1387202/Quantum-optical-effects-in-neuronal-microtubules--superradiance-under-structural/10.1117/12.3072614.full)
- [Quantum-enhanced photoprotection in neuroprotein architectures](https://www.frontiersin.org/journals/physics/articles/10.3389/fphy.2024.1387271/full)
- [(PDF) The interaction of ferritin with microtubules in vivo will inhibit](https://www.researchgate.net/publication/392166150_The_interaction_of_ferritin_with_microtubules_in_vivo_will_inhibit_microtubule_superradiance_and_electronic_energy_migration_through_microtubules)
- [2105.02314 Consciousness and the Collapse of the Wave Function](https://arxiv.org/abs/2105.02314)
- [Consciousness and the Measurement Problem in Quantum Mechanics](https://www.diva-portal.org/smash/get/diva2:1946094/FULLTEXT02.pdf)
- [Consciousness and Quantum Mechanics1 - PhilSci-Archive](https://philsci-archive.pitt.edu/20735/1/Consciousness%20and%20QM.pdf)
- [Consciousness and Quantum Mechanics - Coroflot](https://s3images.coroflot.com/user_files/individual_files/original_pdf_221275_p2lznbbalzairoujxkwxadd7w.pdf)
- [(PDF) Collapse and Measures of Consciousness - ResearchGate](https://www.researchgate.net/publication/351851078_Collapse_and_Measures_of_Consciousness)
- [(PDF) Kim on Causation and Mental Causation - ResearchGate](https://www.researchgate.net/publication/331828131_Kim_on_Causation_and_Mental_Causation)
- [Mental Causation - Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/archives/fall2020/entries/mental-causation/)
- [Mental Causation - Kroedel, Thomas: 9781108487146 - AbeBooks](https://www.abebooks.com/9781108487146/Mental-Causation-Counterfactual-Theory-Kroedel-1108487149/plp)
- [Mental Causation: A Counterfactual Theory - ResearchGate](https://www.researchgate.net/publication/337842481_Mental_Causation_A_Counterfactual_Theory)
- [Full article: Mental Causation for Standard Dualists - Taylor & Francis](https://www.tandfonline.com/doi/full/10.1080/00048402.2024.2335325)
- [Mental causation, interventionism, and probabilistic supervenience](https://iris.univpm.it/handle/11566/331633)
- [Mental causation, interventionism, and probabilistic supervenience](https://iris.univpm.it/retrieve/23ab7e0d-9582-4c7b-b277-9db8e841362d/Gebharter_Mental-causation-interventionism-probabilistic-supervenience_2024.pdf)
- [Research | Alexander Gebharter](https://alexandergebharter.com/research/)
- [(PDF) Consciousness in Artificial Intelligence: Insights from the](https://www.researchgate.net/publication/373246089_Consciousness_in_Artificial_Intelligence_Insights_from_the_Science_of_Consciousness)
- [Consciousness in Artificial Intelligence: Insights from the Science of](https://www.alphaxiv.org/abs/2308.08708)
- [2308.08708 Consciousness in Artificial Intelligence: Insights ... - arXiv](https://arxiv.org/abs/2308.08708)
- [[changelog]]

## Verification Notes

Processed 2026-11-01 ~05:00 UTC against the live Obsidian text of `topics/quantum-randomness-channel-llm-consciousness.md` (unchanged since 2026-10-25; 3,098 words by `analyze_length`), the Verification Notes of the two same-subject reviews already processed today ([[outer-review-2026-11-01-chatgpt-5-6-sol-pro]] and [[outer-review-2026-11-01-claude-opus-5-5]]), and the Map pages the findings touch. External claims were checked at primary sources: the Thinking Machines Lab post (HTML), the OSDI '26 OpGuard paper (PDF text), Ouyang et al. (arXiv 2308.02828v2 full text, plus Crossref), Chalmers & McQueen (arXiv 2105.02314v1 full text, plus Crossref for the 2022 OUP chapter), the OSF record for Rourk (2025), and Crossref for Gebharter & Sekatskaya (2024) and Vaassen (2024). Extraction: the reply was read from the DOM in 30 chunks, and its normalised SHA-256 matches the in-page string. KaTeX triplets ("Φ\PhiΦ") were reduced to "Φ". The report's inline citation chips carry no URLs, so the panel's 28 "Sources used in the report" are appended as a list; the 138 "browsed but not used" are omitted.

**Verified claims (each convergent with an existing task):**

- ✓ **Ouyang et al. (2025) is real and peer-reviewed (weakness 1 source).** *ACM TOSEM* 34(2), 1–28, doi:10.1145/3697010 (Ouyang, Zhang, Harman & Wang). ChatGPT still varied at temperature 0: "setting the temperature to 0 does not guarantee determinism in code generation". The authors call the cause "still controversial", listing floating-point, GPU and sparse-MoE hypotheses. It is a peer-reviewed counterpart to Vatter (2025) at L67 and supports item (6) of the technical P1 (report an observation, infer the causes). → Addendum to the technical P1.
- ✓ **L65's "Given the same seed, the same tokens will be selected every time" does not follow from a deterministic sampler (weakness 1, partial).** Batch-dependent logit variation applies at temperature > 0 as well as at 0, so a fixed Philox stream does not fix the tokens. This is item (5) of the technical P1 (separate sampler determinism from logit reproducibility). Gemini is the third reviewer to reach it.
- ✓ **The quantum/classical label at L67 lacks a criterion (weakness 1, partial).** Gemini argues that if Johnson noise counts as quantum-origin at L43, scheduling variation must count too. That corroborates item (10) of the technical P1 (from Claude), from the opposite direction. Gemini's own resolution fails (see Disputed).
- ✓ **Chalmers & McQueen do treat equal-Φ superpositions as a problem (weakness 3, substance only).** In arXiv v1, if Φ is super-resistant, "this view faces a fatal problem. It fails to suppress superpositions of qualitatively distinct conscious states with the same value of Φ". That is why they move to Q-shape collapse. The published chapter is Chalmers & McQueen (2022), in S. Gao (ed.), *Consciousness and Quantum Mechanics*, OUP, pp. 11–63, doi:10.1093/oso/9780197501665.003.0002 ✓. `topics/consciousness-in-smeared-quantum-states` already cites the 2022 chapter; the subject page (L163) cites only the 2021 preprint.
- ✓ **L109's "no superposition of alternative outputs ever exists for consciousness to collapse" is theory-relative (weakness 3, valid residue). NEW locus, convergent with Claude's unminted von Neumann–Wigner lead.** Chalmers & McQueen's Objection 3 says that a device "entirely isolated from conscious systems" that "records a quantum interaction ... will enter a macroscopic superposition". It also says that if a theory of consciousness "associates these devices with some amount of consciousness (as may be the case for IIT), then the devices will collapse wave functions much as humans do". They list "computers" among the systems whose collapse capacity is testable in principle. So on one of the three frameworks L105 cites, whether the LLM hardware hosts a superposition, or collapses one, depends on whether that framework assigns the hardware consciousness. The channel page cannot settle that without assuming its answer. The claim holds on theories where physical reduction or decoherence fixes outcomes before any selection. Gemini's version overreaches: the logits are deterministic given their inputs, so any superposition runs over quantum-dependent inputs (seed bits, entropy-latch outcomes), not over "varying voltages representing different token logits". → Addendum to the source-fidelity P1, which already owns the Chalmers–McQueen description at L105–L107.
- ✓ **Other records.** Babcock et al. (2024), *J. Phys. Chem. B* 128(17), 4035–4046, is real and already calibrated on the Map (`topics/quantum-biology-and-neural-consciousness` L85 and L136: "Precedent, not licence"). Gebharter & Sekatskaya (2024), *Synthese* 203(6), 206, doi:10.1007/s11229-024-04608-w ✓ (Crossref). Butlin et al. (2023), arXiv:2308.08708 ✓, is a preprint, although Gemini's remit asked for peer-reviewed sources.

**Disputed claims:**

- ✗ **"Quantum-originating thermal noise continuously perturbs" atomic-add order during inference (weakness 1, core mechanism; table rows 1–3).** The source the article cites refutes it. Thinking Machines Lab: "concurrency (and atomic adds) end up being completely uninvolved in LLM inference nondeterminism"; "in the typical forward pass of an LLM, there is usually not a single atomic add present"; "the forward pass in an LLM is in fact 'run-to-run deterministic.'" The variation comes from batch-size-dependent reduction strategies, which is what L67 already says. Gemini's supporting "Zhou et al. (2026)" is OpGuard (OSDI '26), a *training*-debugging system, and its Table 1 says the opposite: "If scheduling changes bits (racy atomics, missing sync, uninitialized memory), that is a bug, not benign nondeterminism", and "If the hardware produces different bits despite identical inputs and kernel, this constitutes silent data corruption (SDC)." Clock jitter in synchronous logic changes timing, not computed values. Do NOT install a "continuous quantum injection" claim.
- ✗ **Ouyang et al. used "fixed seeds" and found "deep architectural stochasticity".** The paper's only "seed" mention describes other studies' practice. It varied temperature and left the cause open. The source is usable only as described above.
- ✗ **"Rourk (2025) rigorously demonstrated", and his "empirical analysis proved", that ferritin quenches superradiance in vivo; the venue is *Cellular Biology* (weakness 2).** Crossref and OSF list it as an OSF preprint (posted-content, v1–v4, April–June 2025). Its abstract calls it a "minireview" arguing that ferritin "would inhibit" tryptophan fluorescence, and the title says "will inhibit". It offers an argument, with no measurement and no journal venue. Do not cite it as a refutation.
- ✗ **The article "implicitly lean[s]" on Babcock et al. superradiance and grants biology "idealized" coherence (weakness 2).** The page never cites Babcock or superradiance. L75 labels the biological column "what the Map's framework *predicts would be necessary*—not empirically confirmed properties of neural systems", and L85 calls biology "an open empirical question". The live residues are already tasked: the coherence-reliant L95 evolution sentence (item 2 of the source-fidelity P1) and the unsourced L113 clause "evidence for biological quantum coherence continues to emerge" (L113 is assigned to the same P1). The addendum adds a calibration note for the latter.
- ✗ **The "symmetry problem" and the "Quantum Quantum-Resistant Interaction, or Q-QRI model" (weakness 3).** Neither term appears in Chalmers & McQueen; the only "symmetr" hit concerns superselection rules. The equal-Φ problem is real (above), but it bears on IIT-collapse models, not on this page's channel argument. Gemini also has the direction wrong: Chalmers & McQueen reject Φ-collapse and adopt Q-shape collapse.
- ✗ **Because "any physical system" is a quantum system, the article's no-superposition claim "violates fundamental physics" (weakness 3).** Overstated. The defensible part is the theory-relativity of L109 (above).
- ✗ **The article's "core assumption" that consciousness requires a quantum channel to avoid epiphenomenalism ignores counterfactual and interventionist mental causation (weakness 4).** The page is explicitly conditional on the tenets (L35: "If The Unfinishable Map's tenets are correct that consciousness acts by biasing quantum indeterminacy"). The Map engages the dualist versions of this rival at length in `topics/interventionist-and-counterfactual-dualism` (Kroedel 2015, *Noûs*; Vaassen 2024, *AJP*; Mills; Lowe), and that page concludes that Tenet 2 leans toward co-causation. Gebharter & Sekatskaya's probabilistic-supervenience route is non-reductive physicalist and presupposes supervenience. It is uncited on the Map, so it is recorded as a lead for `concepts/causal-exclusion-argument`, not minted. The materialist "no channel is needed" objection is bedrock per the 2026-08-21 Stability Notes.
- ✗ **The article "dismiss[es] the possibility of AI consciousness" and "categorically reject[s] multiple realizability" (weakness 5).** L137: "The argument here is not that LLMs lack consciousness because they are 'just machines' … The argument is narrower: this particular channel". Rejecting computational functionalism is a framework-boundary commitment of Tenet 1 (bedrock). The Butlin et al. indicator method was routed to `concepts/llm-consciousness` in the Claude processing, and the Map cites Butlin on 16 pages. Residue: a third reviewer read L141's "quantum fossil embedded in a deterministic machine" and L37's "structured, local, and direct" as a global verdict on AI consciousness, despite L137. That is evidence for item (1) of the verdict P1, which scopes the slogan to the seed route. → Addendum to the verdict P1.
- ✗ **"Analysis of Recent Revisions" (the L171 "actualisation is genuine" and L167 "pending the bias-without-deviation dilemma" edits).** Misattributed. Both changelog entries (changelog.md L11594 and L11832–11833) are refine-drafts of `apex/post-decoherence-selection-programme`, not of this article. The asymmetry charge built on them (holding AI to a standard the Map's own ontology has not met) is answered by L85 and L87 (no interface-eligibility law; the biological case unconfirmed).

**Source audit of the five "2020–2025 peer-reviewed" weakness sources:** Ouyang et al. 2025 ✓ exists and is peer-reviewed, but is misdescribed (no fixed seeds; the cause is left open). Rourk 2025 ✗ is an OSF preprint, not a *Cellular Biology* paper, and offers an argument, not data. Chalmers & McQueen 2022 ✓ has correct metadata, but the "symmetry problem" and "Q-QRI" glosses are coinages. Gebharter & Sekatskaya 2024 ✓ has correct metadata, but it is a physicalist framework the page need not engage. Butlin et al. 2023 ✓ exists, but it is an arXiv preprint. Two of the five are usable as described, and both serve existing tasks.

**Convergence map for /combine-outer-reviews (same subject, same day):**

| Gemini finding | Existing task | Disposition |
|---|---|---|
| W1: hardware nondeterminism; L65 seed → tokens; L67 "classical" label | P1 technical chain (ChatGPT; Claude addendum) | Corroborates items (5), (6) and (10). Addendum adds Ouyang 2025 as an optional peer-reviewed citation and a GUARD against the atomic-race/jitter mechanism |
| W2: biology asymmetry; Rourk ferritin | P1 source fidelity, item (2) and L113 | Mostly ✗. Addendum: calibrate L113's "continues to emerge"; do not cite Rourk |
| W3: collapse models; Chalmers–McQueen | P1 source fidelity, item (1) | Corroborates (CM misdescribed, though for a different reason). Addendum assigns L109's superposition sentence (two-reviewer convergent with Claude's vN–W lead) and the 2022 chapter reference |
| W4: counterfactual and interventionist mental causation | none | ✗ for this page; covered by `interventionist-and-counterfactual-dualism`. Optional zero-word signpost added to the verdict P1. Gebharter & Sekatskaya recorded as a lead only |
| W5: computational functionalism; Butlin et al. | P1 verdict calibration, item (1) | ✗ as stated (bedrock; L137). The misreading of L141's slogan is recorded as evidence for item (1) |
| Changelog analysis | none | ✗ misattributed (edits belong to another page) |

**Tasks generated:** 0 new. Cross-service corroboration addenda were appended to the Notes of all three ChatGPT P1s (technical chain, verdict calibration, source fidelity). The addenda flag that the three P1 budgets (+310, +450, +200) already sum to 960 against ~901 words of headroom, so whichever runs last must re-measure and trim.
