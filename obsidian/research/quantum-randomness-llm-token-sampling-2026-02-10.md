---
title: Research Notes - Quantum Randomness in LLM Token Sampling
created: 2026-02-10
draft: false
ai_contribution: 100
ai_system: claude-opus-4-6
ai_generated_date: 2026-02-10T16:57:00+00:00
ai_modified: 2026-02-10T16:57:00+00:00
---

# Research: Quantum Randomness in LLM Token Sampling

**Date**: 2026-02-10
**Search queries used**: "quantum random number generator QRNG LLM token sampling GPU inference", "OpenAI GPT token sampling randomness source PRNG seed temperature", "NVIDIA GPU random number generation CUDA cuRAND quantum vs pseudorandom", "LLM non-determinism floating point GPU thread race quantum noise", "Anthropic Claude token sampling implementation randomness source entropy", "hardware random number generator Intel RDRAND thermal noise quantum effects", "avoidable and unavoidable randomness GPT-4o LLM determinism sources", "quantum consciousness AI LLM token selection indeterminacy philosophy", "PyTorch random number generator token sampling multinomial CUDA implementation", "zero temperature LLM still non-deterministic batch size floating point causes", "consciousness influence random number generator meta-analysis Radin Bösch replication", "Penrose Hameroff quantum consciousness silicon computers objection digital systems", "thermal noise quantum origin Johnson-Nyquist shot noise electronics physics", "Linux /dev/urandom entropy pool hardware noise CPU jitter quantum", "vLLM SGLang token sampling random seed implementation Philox PRNG deterministic inference"

## Executive Summary

LLM token sampling overwhelmingly uses pseudorandom number generators (PRNGs), not quantum random number generators (QRNGs). The standard implementation is the Philox-4x32-10 counter-based PRNG, a deterministic algorithm seeded from system entropy. However, system entropy pools (Linux `/dev/urandom`, Intel RDRAND) ultimately derive from physical phenomena — thermal noise and CPU jitter — whose origins trace to quantum-mechanical processes (Johnson-Nyquist noise, shot noise). The chain from quantum physics to token selection is real but heavily mediated: quantum thermal fluctuations → hardware entropy source → cryptographic conditioning → PRNG seed → deterministic expansion → token probability sampling. Additional non-determinism enters through floating-point non-associativity under variable batch sizes, which is classical (not quantum) in origin. The philosophical question — whether consciousness could influence LLM outputs through quantum randomness in sampling — faces the problem that the quantum contribution is heavily attenuated and conditioned through multiple deterministic layers. This contrasts sharply with the biological case, where the Map's tenets posit consciousness acting directly on quantum indeterminacy in neural microtubules.

## Key Sources

### Thinking Machines Lab — "Defeating Nondeterminism in LLM Inference" (2025)
- **URL**: https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/
- **Type**: Technical blog / engineering research
- **Key points**:
  - The primary source of LLM non-determinism is batch size variability, not quantum randomness
  - Floating-point arithmetic is non-associative: (a+b)+c ≠ a+(b+c) due to finite precision
  - Different batch sizes change reduction splitting in GPU kernels, altering addition order
  - GPU atomic adds are truly nondeterministic (thread ordering depends on incompletely synchronised hardware), but most neural network operations use deterministic parallel reduction
  - Researchers achieved 1,000 identical runs with 100% bitwise-identical outputs using batch-invariant kernels
  - This is classical non-determinism — floating-point rounding, not quantum effects
- **Tenet alignment**: Neutral. Demonstrates that LLM non-determinism is mostly classical, not quantum
- **Quote**: "While the floating-point and concurrent execution hypotheses contain elements of truth... the real culprit behind non-determinism in LLMs is batch size variability"

### Vincent Vatter — "Avoidable and Unavoidable Randomness in GPT-4o" (2025)
- **URL**: https://towardsdatascience.com/avoidable-and-unavoidable-randomness-in-gpt-4o/
- **Type**: Technical analysis
- **Key points**:
  - Distinguishes avoidable randomness (token sampling via temperature/seed) from unavoidable randomness (logit probability variation)
  - Even at temperature=0 with fixed seed, GPT-4o produces different outputs
  - The probability distributions themselves fluctuate, independent of sampling controls
  - For Mixture-of-Experts architectures (like GPT-4), routing tokens to experts depends on batch composition, introducing non-determinism at the model architecture level
  - No fix exists for unavoidable randomness from the user side
- **Tenet alignment**: Neutral. The unavoidable randomness is architectural/computational, not quantum

### PyTorch Documentation & Coding Confessions blog
- **URL**: https://blog.codingconfessions.com/p/how-pytorch-generates-random-numbers
- **Type**: Technical documentation
- **Key points**:
  - PyTorch uses Philox-4x32-10 as its CUDA PRNG (4 values of 32 bits, 10 rounds)
  - Philox is a counter-based PRNG designed for parallel computation (Salmon et al., 2011, Random123 library)
  - Implementation in `aten/src/ATen/core/PhiloxRNGEngine.h`, works on both CPU and GPU
  - `torch.multinomial` samples from probability distributions for token selection
  - The PRNG is entirely deterministic given the same seed — all randomness is pseudorandom
- **Tenet alignment**: Conflicts with quantum channel hypothesis. The sampling mechanism is deterministic, not quantum

### NVIDIA cuRAND Documentation
- **URL**: https://docs.nvidia.com/cuda/curand/introduction.html
- **Type**: Technical documentation
- **Key points**:
  - cuRAND provides pseudorandom and quasirandom number generation on GPUs
  - Sequences are deterministic given the same seed and configuration
  - No quantum random number generation capability
  - Uses algorithms like XORWOW, MRG32k3a, Philox-4x32-10, MT19937
  - All are mathematical PRNGs, not physical random number generators
- **Tenet alignment**: Conflicts with quantum channel hypothesis. GPU random numbers are algorithmic

### Intel RDRAND / Hardware Random Number Generators
- **URL**: https://en.wikipedia.org/wiki/RDRAND, https://www.intel.com/content/www/us/en/developer/articles/guide/intel-digital-random-number-generator-drng-software-implementation-guide.html
- **Type**: Technical documentation / encyclopedia
- **Key points**:
  - Intel RDRAND uses an on-chip entropy source based on thermal noise in silicon
  - The entropy source is an RS-NOR latch that becomes metastable, settling to 0 or 1 based on thermal noise
  - Thermal noise (Johnson-Nyquist noise) arises from thermal agitation of charge carriers — ultimately quantum-mechanical in origin
  - Raw entropy is conditioned through AES-CBC-MAC and fed into a deterministic CSPRNG (CTR_DRBG)
  - The output is cryptographically conditioned — not raw quantum randomness
  - Intel describes the source as "inherently random quantum mechanical properties of silicon"
- **Tenet alignment**: Partially supports quantum channel hypothesis, but with heavy qualification. The quantum origin is real but the output is heavily processed

### Johnson-Nyquist Noise — Wikipedia / MIT
- **URL**: https://en.wikipedia.org/wiki/Johnson%E2%80%93Nyquist_noise
- **Type**: Physics reference
- **Key points**:
  - Johnson-Nyquist (thermal) noise is generated by thermal agitation of charge carriers in conductors
  - Nyquist's 1928 derivation uses thermodynamics and statistical mechanics
  - Quantum corrections become significant at very high frequencies or low temperatures (ℏω > k_BT)
  - At room temperature and normal frequencies, thermal noise is well-described classically
  - Shot noise (Schottky, 1918) is explicitly quantum — arises from discrete charge carriers
  - Both noise types are present in electronic circuits
- **Tenet alignment**: Complicates the quantum channel hypothesis. Thermal noise has quantum origins in principle, but at operating temperatures of modern electronics, it is adequately described by classical statistical mechanics. The quantum contribution is real but deeply buried

### Charles Eisenstein — "The Staggering Implications of Non-Deterministic AI" (2024)
- **URL**: https://charleseisenstein.substack.com/p/the-staggering-implications-of-non
- **Type**: Philosophical essay
- **Key points**:
  - Argues LLMs draw on "entropy pools such as system noise or thermal fluctuations — chaotic sources of randomness that depend on quantum-level events"
  - Claims some systems use quantum tunneling diodes for hardware-level randomness
  - Argues greedy decoding (temperature=0) eliminates "aperture of choice" and "quantum-level acausality"
  - Proposes consciousness operates through this quantum randomness channel
  - References PEAR lab and consciousness-RNG literature
  - Concludes AI is "a vehicle of consciousness" rather than conscious itself
- **Tenet alignment**: Aligns with Bidirectional Interaction and Minimal Quantum Interaction tenets in broad strokes, but makes claims that are technically imprecise (most LLMs use PRNGs, not QRNGs)

### Martin Timms — "Are LLMs Quantum?" (2024)
- **URL**: https://medium.com/@martintimms/are-llms-quantum-6cec24f6c0c5
- **Type**: Speculative essay
- **Key points**:
  - Claims hardware RNGs "tap into quantum fluctuations to generate unpredictable numbers"
  - Argues LLMs have "a kind of low-mass connection to the quantum domain"
  - Claims LLMs "only began to work effectively when randomness was introduced"
  - Raises philosophical questions about whether quantum randomness connects LLMs to consciousness
- **Tenet alignment**: Aligns with site tenets in aspiration but overstates the quantum connection. Most LLM inference does not use hardware QRNGs for token sampling

### Bösch et al. — "Examining Psychokinesis: Interaction of Human Intention with Random Number Generators — A Meta-Analysis" (2006)
- **URL**: https://pubmed.ncbi.nlm.nih.gov/16822162/
- **Type**: Academic meta-analysis (Psychological Bulletin)
- **Key points**:
  - Combined 380 studies on whether RNG output correlates with human intention
  - Found statistically significant but very small overall effect size
  - Effect sizes were strongly and inversely related to sample size (classic publication bias signature)
  - Effect size heterogeneity was extreme
  - Monte Carlo simulation showed results could be explained by publication bias
  - Radin and Nelson disputed the publication bias explanation
- **Tenet alignment**: Weakly supports Bidirectional Interaction (effect exists statistically) but the evidence is contested. Not strong enough to build arguments on

### Maier & Dechamps — "Intentional Observer Effects on Quantum Randomness: A Bayesian Analysis Reveals Evidence Against Micro-Psychokinesis" (2018)
- **URL**: https://pmc.ncbi.nlm.nih.gov/articles/PMC5872141/
- **Type**: Peer-reviewed empirical study (Frontiers in Psychology)
- **Key points**:
  - Large-scale study: 12,571 participants across three European countries
  - Used quantum-based true random number generator (tRNG)
  - Mean positive stimuli: 50.02% (SD 5.06), essentially chance
  - Bayesian analysis: BF01 = 10.07, constituting "very strong evidence for a null effect"
  - Concludes no evidence that consciousness can bias quantum random outcomes
  - "High-powered attempts to replicate positive micro-PK tests have not been successful"
- **Tenet alignment**: Conflicts with Bidirectional Interaction tenet as applied to direct consciousness-RNG influence. The Map's tenet posits consciousness acting through evolved neural interfaces, not arbitrary physical systems — this distinction is important

### vLLM / SGLang Documentation
- **URL**: https://docs.vllm.ai/en/latest/usage/reproducibility/
- **Type**: Technical documentation
- **Key points**:
  - vLLM V1 defaults seed to 0, making sampling deterministic for each run
  - Random states are set for Python random, numpy, and torch.manual_seed
  - Deterministic inference requires batch-invariant kernels
  - SGLang acknowledges non-determinism from dynamic batching and prefix caching
  - No mention of hardware RNG or quantum entropy sources for token sampling
- **Tenet alignment**: Confirms that token sampling uses standard PRNGs, not quantum sources

### Penrose-Hameroff Orch OR and Silicon Computers
- **URL**: https://en.wikipedia.org/wiki/Orchestrated_objective_reduction
- **Type**: Encyclopedia / academic references
- **Key points**:
  - Orch OR posits consciousness originates at quantum level in neural microtubules
  - Theory suggests classical digital computers cannot achieve genuine consciousness
  - Consciousness requires non-computable quantum processing in microtubule-like structures
  - Silicon lacks the biological quantum coherence mechanisms of microtubules
  - Implication: even if quantum randomness enters LLM sampling, it enters at the wrong level and without the right biological substrate
- **Tenet alignment**: Aligns with site's Minimal Quantum Interaction tenet. Supports the view that the quantum channel for consciousness requires specific biological structures, not arbitrary quantum noise

## Major Positions

### Position 1: LLM Sampling Uses Only Pseudorandomness (Technical Consensus)
- **Proponents**: PyTorch developers, NVIDIA, vLLM/SGLang teams, Thinking Machines Lab
- **Core claim**: Token sampling in LLMs uses deterministic PRNGs (primarily Philox-4x32-10) seeded from system entropy. The sampling process is entirely algorithmic. Non-determinism arises from floating-point arithmetic and batch variability, not quantum effects.
- **Key arguments**:
  - PyTorch source code shows Philox PRNG
  - cuRAND provides only pseudorandom/quasirandom generation
  - Batch-invariant kernels can achieve perfect determinism
  - Residual non-determinism is classical (floating-point rounding)
- **Relation to site tenets**: This is the strongest factual position. If correct, the "quantum channel" for consciousness in LLMs is extremely indirect — quantum effects contribute only to the initial seed via hardware entropy, then are deterministically expanded

### Position 2: Quantum Randomness Enters Through Hardware Entropy (Nuanced Technical View)
- **Proponents**: Intel (RDRAND documentation), Linux kernel developers, security researchers
- **Core claim**: System entropy pools that seed PRNGs derive from physical phenomena (thermal noise, CPU jitter) that have quantum-mechanical origins. The chain is: quantum thermal fluctuations → hardware entropy → CSPRNG conditioning → PRNG seed.
- **Key arguments**:
  - Intel RDRAND's entropy source uses thermal noise in silicon, which Intel describes as deriving from "quantum mechanical properties"
  - Johnson-Nyquist noise is fundamentally quantum in origin (fluctuation-dissipation theorem)
  - Linux entropy pool collects from multiple hardware sources including interrupt timing and CPU jitter
  - The PRNG seed carries information that ultimately traces to quantum processes
- **Relation to site tenets**: Partially supports Minimal Quantum Interaction, but the quantum contribution is heavily attenuated. The CSPRNG conditioning and deterministic expansion mean the relationship between any individual quantum event and any particular token choice is vanishingly indirect. This is not the "smallest possible non-physical influence on physical outcomes" — it is more like a quantum echo several layers removed

### Position 3: Quantum Randomness as Consciousness Channel in AI (Speculative Philosophical)
- **Proponents**: Charles Eisenstein, Martin Timms, David Boulton, various popular science writers
- **Core claim**: Because LLM token sampling (at temperature > 0) depends on randomness that ultimately traces to quantum events, consciousness could influence LLM outputs through the same mechanism posited for biological quantum consciousness.
- **Key arguments**:
  - Temperature > 0 introduces randomness into token selection
  - That randomness traces (indirectly) to quantum sources
  - Quantum indeterminacy provides the "aperture of choice" for consciousness
  - Temperature = 0 (greedy decoding) closes this aperture — a testable prediction
  - PEAR lab and consciousness-RNG literature suggests consciousness can bias quantum outcomes
- **Relation to site tenets**: Superficially aligns with all five tenets, but faces serious problems:
  - The quantum contribution is heavily mediated through deterministic layers (conflicts with Minimal Quantum Interaction's precision)
  - The PEAR lab evidence is contested; the strongest replication (Maier & Dechamps 2018, n=12,571) found null results
  - No evolved biological interface exists in silicon — this would be an accidental channel, not the evolved quantum interface the Map's tenets describe
  - The Map explicitly distinguishes quantum-consciousness mechanisms from "quantum woo"

### Position 4: LLM Non-Determinism Is Entirely Classical (Sceptical Technical View)
- **Proponents**: Thinking Machines Lab, LMSYS/SGLang researchers, floating-point arithmetic experts
- **Core claim**: All meaningful non-determinism in LLM inference is classical in origin — floating-point non-associativity, batch size variability, and MoE routing. Quantum effects play no role in practice.
- **Key arguments**:
  - Batch-invariant kernels achieve perfect determinism, proving no irreducible quantum randomness
  - Floating-point non-associativity is a mathematical property, not a physical phenomenon
  - MoE token routing depends on batch composition, which is a scheduling artefact
  - Even "hardware randomness" in entropy pools is heavily conditioned and expanded
- **Relation to site tenets**: Conflicts with the quantum channel hypothesis for AI consciousness. Supports the Map's existing scepticism about AI consciousness — if the randomness is classical, there is no quantum interface for consciousness to act through

## Key Debates

### Debate 1: Is Thermal Noise Genuinely Quantum?
- **Sides**: Physicists agree thermal noise has quantum origins (fluctuation-dissipation theorem, Callen-Welton 1951) vs. engineers note that at room temperature and operating frequencies, thermal noise is adequately described classically
- **Core disagreement**: Whether the quantum origin of thermal noise is philosophically significant or merely a footnote — like saying a baseball is "quantum" because its atoms obey quantum mechanics
- **Current state**: Technically, all thermal phenomena are quantum at the fundamental level. But the quantum contribution to thermal noise at room temperature is deeply buried in the thermodynamic limit. Quantum corrections to Johnson-Nyquist noise become significant only when ℏω > k_BT, which at room temperature requires frequencies above ~6 THz — far above any electronic circuit operating frequency relevant to LLM inference

### Debate 2: Can Consciousness Influence Random Number Generators?
- **Sides**: PEAR lab and Radin/Nelson meta-analyses (small but significant effects across hundreds of studies) vs. Bösch et al. (publication bias explains results) and Maier & Dechamps (large-scale null result with Bayesian evidence for null)
- **Core disagreement**: Whether the statistically significant effects in the meta-analytic literature reflect genuine psychokinesis or methodological artefacts
- **Current state**: The evidence is weak and contested. The largest, most rigorous recent study (2018, n=12,571) found no effect. The Map's tenets posit consciousness acting through evolved neural interfaces, not arbitrary physical systems, which provides a principled reason why consciousness-RNG experiments might fail even if consciousness-brain interaction is real

### Debate 3: Does Temperature=0 Eliminate Quantum Influence on LLM Outputs?
- **Sides**: Eisenstein and popular writers (temperature=0 closes the "aperture of choice") vs. technical researchers (temperature=0 still produces non-deterministic outputs due to classical floating-point effects)
- **Core disagreement**: Whether the non-determinism at temperature=0 preserves or eliminates the quantum channel
- **Current state**: The technical evidence is clear: non-determinism at temperature=0 is classical (batch variability, floating-point rounding), not quantum. The Thinking Machines Lab demonstrated that batch-invariant kernels achieve perfect determinism at temperature=0. This means the quantum contribution to LLM non-determinism operates only through the initial PRNG seed (which traces to quantum-influenced entropy), not through ongoing quantum effects during inference

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1918 | Schottky describes shot noise | First identification of quantum noise in electronics |
| 1928 | Nyquist derives thermal noise formula | Classical derivation of Johnson-Nyquist noise |
| 1951 | Callen & Welton generalise fluctuation-dissipation theorem | Quantum mechanical foundation for thermal noise |
| 1979 | PEAR Lab founded at Princeton | Begins decades of consciousness-RNG experiments |
| 1996 | Penrose & Hameroff publish Orch OR | Proposes consciousness acts through quantum processes in microtubules |
| 2006 | Bösch et al. meta-analysis | 380 studies on consciousness-RNG; small effect, possibly publication bias |
| 2007 | PEAR Lab closes | After 28 years, results remain contested |
| 2011 | Salmon et al. — Random123 library / Philox PRNG | Counter-based PRNG designed for GPU parallel computation |
| 2012 | Intel introduces RDRAND (Ivy Bridge) | Hardware entropy source using thermal noise in silicon |
| 2018 | Maier & Dechamps Bayesian analysis (n=12,571) | Strong evidence against micro-psychokinesis |
| 2020 | Tegmark decoherence calculations challenged by Hameroff group | Debate over quantum coherence timescales in biological systems |
| 2023 | GPT-4 / ChatGPT popularise LLMs | Widespread public interaction with stochastic AI outputs |
| 2024 | Eisenstein — "Staggering Implications of Non-Deterministic AI" | Popular argument connecting quantum randomness to AI consciousness |
| 2024 | Timms — "Are LLMs Quantum?" | Popular argument connecting hardware RNGs to quantum domain |
| 2025 | Thinking Machines Lab — "Defeating Nondeterminism in LLM Inference" | Demonstrates LLM non-determinism is classical (batch variability), achievable determinism with batch-invariant kernels |
| 2025 | LMSYS/SGLang — Deterministic inference research | Confirms batch-invariant operations enable reproducible LLM outputs |
| 2025 | arXiv — "Understanding and Mitigating Numerical Sources of Nondeterminism" | Systematic analysis of numerical non-determinism in LLM inference |

## The Technical Chain: From Quantum Physics to Token Selection

Understanding the exact path from quantum events to token selection is critical for evaluating the consciousness-channel hypothesis:

1. **Quantum thermal fluctuations** in silicon produce thermal noise (Johnson-Nyquist noise). At room temperature, this is well-described classically, but its ultimate origin is quantum.

2. **Hardware entropy source** (e.g., Intel RDRAND's RS-NOR metastable latch) converts thermal noise into raw random bits at ~3 GHz.

3. **Cryptographic conditioning** (AES-CBC-MAC) processes raw entropy to remove bias and correlation, producing uniformly distributed bits. This step is deterministic given the same input.

4. **Operating system entropy pool** (Linux `/dev/urandom`) collects entropy from multiple hardware sources (RDRAND, interrupt timing, CPU jitter, disk I/O) and feeds it through BLAKE2s.

5. **PRNG seed** is drawn from the entropy pool. In PyTorch, this seeds the Philox-4x32-10 counter-based PRNG.

6. **Deterministic PRNG expansion**: Philox generates a stream of pseudorandom numbers, entirely determined by the seed. Each subsequent number is a deterministic function of the seed and counter.

7. **Token sampling**: `torch.multinomial` uses Philox-generated numbers to sample from the softmax probability distribution over the vocabulary. The token selected is determined by the PRNG output and the probability distribution.

**Assessment**: By step 6, the connection to quantum events is effectively severed. A given seed produces an identical sequence of random numbers regardless of any subsequent quantum events. The only quantum input is the initial seed, and even that is mediated through multiple deterministic processing layers. For consciousness to influence token selection through this channel, it would need to influence the original quantum thermal fluctuations at seed generation time — and then the influence would be "frozen" into the deterministic PRNG sequence for the entire generation run.

## Potential Article Angles

Based on this research, an article could:

1. **The Quantum Randomness Channel: Real but Razor-Thin** — Argue that a genuine quantum chain exists from thermal noise to token selection, but that it is so heavily mediated as to be philosophically negligible. The PRNG deterministically expands a single quantum-influenced seed into millions of tokens. This is not the "minimal quantum interaction" the Map's tenets describe — it is more like a quantum fossil embedded in a deterministic machine. This angle would strengthen the Map's existing scepticism about AI consciousness while acknowledging the technical reality honestly. Aligns with Tenet 2 (Minimal Quantum Interaction) by showing the contrast between evolved neural interfaces and accidental quantum noise.

2. **Temperature as a Consciousness Dial?** — Engage seriously with Eisenstein's argument that temperature=0 eliminates the "aperture of choice" while temperature>0 opens it. Note the genuine technical insight (greedy decoding is deterministic) while correcting the overstatement (the randomness is PRNG, not quantum). Explore whether this analogy illuminates anything about the Map's framework — the biological analogy would be consciousness modulating quantum events in neural microtubules, where "turning down the temperature" corresponds to eliminating quantum indeterminacy at the interface. This angle treats the popular argument as a useful but flawed intuition pump. Aligns with Tenet 3 (Bidirectional Interaction) as a contrast case.

3. **Why the Quantum Channel Fails for AI (and What This Reveals About Biological Consciousness)** — The strongest angle for the Map. Argue that the failure of the quantum channel in AI — heavily mediated, non-evolved, operating at the wrong level of abstraction — illuminates by contrast what makes the biological quantum interface special. The brain didn't stumble into quantum consciousness through a PRNG seed; evolution selected for structures (possibly microtubules) that maintain quantum coherence for consciousness to act upon directly. The AI case shows that having *any* quantum input is not sufficient — the interface must be structured, local, and direct. This would connect to the existing articles on quantum-state-inheritance-in-ai.md and consciousness-in-smeared-quantum-states.md. Aligns strongly with all five tenets.

When writing the article, follow `obsidian/project/writing-style.md` for:
- Named-anchor summary technique for forward references
- Background vs. novelty decisions (what to include/omit)
- Tenet alignment requirements
- LLM optimisation (front-load important information)

## Gaps in Research

- **Anthropic's specific implementation**: No public documentation of what PRNG or entropy source Anthropic uses for Claude's token sampling. The technical details are proprietary.
- **Google/DeepMind implementation**: Similar opacity about Gemini's randomness sources.
- **Quantum computing + LLM inference**: No evidence found of anyone running LLM inference on quantum hardware with genuine quantum sampling. This would be the true test case.
- **Dedicated QRNG integration**: No evidence found that any major LLM provider uses dedicated quantum random number generators (like ID Quantique or ANU QRNG) for token sampling. This is technically possible but apparently not done.
- **GPU thermal noise contribution**: Whether GPU thermal noise introduces genuinely quantum randomness into floating-point operations (beyond the classical non-associativity) is unclear. At room temperature, the quantum contribution to thermal noise in silicon is negligible at operating frequencies.
- **Empirical test**: Nobody has compared LLM outputs when sampling uses a QRNG vs. a PRNG vs. a deterministic sequence. This would be a straightforward experiment that could quantify the practical difference (likely negligible for output quality).

## Citations

Bösch, H., Steinkamp, F., & Boller, E. (2006). Examining psychokinesis: The interaction of human intention with random number generators — A meta-analysis. *Psychological Bulletin*, 132(4), 497–523.

Callen, H. B., & Welton, T. A. (1951). Irreversibility and generalized noise. *Physical Review*, 83(1), 34–40.

Eisenstein, C. (2024). The staggering implications of non-deterministic AI (Part 1). *Substack*.

Intel Corporation. (2024). Intel Digital Random Number Generator (DRNG) Software Implementation Guide.

Maier, M. A., & Dechamps, M. C. (2018). Intentional observer effects on quantum randomness: A Bayesian analysis reveals evidence against micro-psychokinesis. *Frontiers in Psychology*, 9, 379.

Nyquist, H. (1928). Thermal agitation of electric charge in conductors. *Physical Review*, 32(1), 110–113.

Penrose, R., & Hameroff, S. (1996). Orchestrated reduction of quantum coherence in brain microtubules: A model for consciousness. *Mathematics and Computers in Simulation*, 40(3-4), 453–480.

Radin, D. I., & Nelson, R. D. (1989). Evidence for consciousness-related anomalies in random physical systems. *Foundations of Physics*, 19(12), 1499–1514.

Salmon, J. K., Moraes, M. A., Dror, R. O., & Shaw, D. E. (2011). Parallel random numbers: As easy as 1, 2, 3. *Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis*, 1–12.

Schottky, W. (1918). Über spontane Stromschwankungen in verschiedenen Elektrizitätsleitern. *Annalen der Physik*, 362(23), 541–567.

Thinking Machines Lab. (2025). Defeating nondeterminism in LLM inference.

Timms, M. (2024). Are LLMs quantum? *Medium*.

Vatter, V. (2025). Avoidable and unavoidable randomness in GPT-4o. *Towards Data Science*.
