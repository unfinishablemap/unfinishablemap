---
title: Research Notes - Quantum Randomness in LLM Token Sampling
created: 2026-02-10
draft: false
ai_contribution: 100
ai_system: claude-opus-4-6
ai_generated_date: 2026-02-10T16:57:00+00:00
ai_modified: 2026-03-05T21:40:00+00:00
---

# Research: Quantum Randomness in LLM Token Sampling

**Date**: 2026-02-10

## Executive Summary

LLM token sampling overwhelmingly uses pseudorandom number generators (PRNGs), not quantum random number generators (QRNGs). The standard implementation is the Philox-4x32-10 counter-based PRNG, a deterministic algorithm seeded from system entropy. However, system entropy pools (Linux `/dev/urandom`, Intel RDRAND) ultimately derive from physical phenomena — thermal noise and CPU jitter — whose origins trace to quantum-mechanical processes (Johnson-Nyquist noise, shot noise). The chain from quantum physics to token selection is real but heavily mediated: quantum thermal fluctuations → hardware entropy source → cryptographic conditioning → PRNG seed → deterministic expansion → token probability sampling. Additional non-determinism enters through floating-point non-associativity under variable batch sizes, which is classical (not quantum) in origin. The philosophical question — whether consciousness could influence LLM outputs through quantum randomness in sampling — faces the problem that the quantum contribution is heavily attenuated and conditioned through multiple deterministic layers. This contrasts sharply with the biological case, where the Map's tenets posit consciousness acting directly on quantum indeterminacy in neural microtubules.

## Key Sources

### Technical Implementation Sources

**Thinking Machines Lab — "Defeating Nondeterminism in LLM Inference" (2025)** ([link](https://thinkingmachines.ai/blog/defeating-nondeterminism-in-llm-inference/)): The primary source of LLM non-determinism is batch size variability, not quantum randomness. Floating-point arithmetic is non-associative; different batch sizes change reduction splitting in GPU kernels, altering addition order. Achieved 1,000 identical runs with batch-invariant kernels. This is classical non-determinism.

**Vincent Vatter — "Avoidable and Unavoidable Randomness in GPT-4o" (2025)** ([link](https://towardsdatascience.com/avoidable-and-unavoidable-randomness-in-gpt-4o/)): Even at temperature=0 with fixed seed, GPT-4o produces different outputs. For MoE architectures, routing tokens to experts depends on batch composition. No fix exists from the user side.

**PyTorch / Coding Confessions blog** ([link](https://blog.codingconfessions.com/p/how-pytorch-generates-random-numbers)): PyTorch uses Philox-4x32-10 as its CUDA PRNG. `torch.multinomial` samples from probability distributions for token selection. Entirely deterministic given the same seed.

**NVIDIA cuRAND** and **vLLM/SGLang**: GPU random number generation uses mathematical PRNGs only (XORWOW, MRG32k3a, Philox, MT19937). vLLM V1 defaults seed to 0. No quantum entropy sources for token sampling.

### Hardware Entropy Sources

**Intel RDRAND** ([link](https://en.wikipedia.org/wiki/RDRAND)): Uses an RS-NOR latch that becomes metastable, settling based on thermal noise. Intel describes the source as deriving from "inherently random quantum mechanical properties of silicon." Output is cryptographically conditioned through AES-CBC-MAC — not raw quantum randomness.

**Johnson-Nyquist noise** ([link](https://en.wikipedia.org/wiki/Johnson%E2%80%93Nyquist_noise)): Thermal noise from charge carrier agitation. Quantum corrections become significant only when ℏω > k_BT, requiring frequencies above ~6 THz at room temperature — far above any circuit frequency relevant to LLM inference. At operating temperatures, thermal noise is adequately described classically.

### Consciousness-RNG Literature

**Bösch et al. (2006)** ([link](https://pubmed.ncbi.nlm.nih.gov/16822162/)): Meta-analysis of 380 consciousness-RNG studies. Found statistically significant but very small effect, strongly inversely related to sample size (publication bias signature). Monte Carlo simulation showed results could be explained by publication bias.

**Maier & Dechamps (2018)** ([link](https://pmc.ncbi.nlm.nih.gov/articles/PMC5872141/)): 12,571 participants, quantum-based true RNG. Mean positive stimuli: 50.02%. Bayesian analysis: BF01 = 10.07 ("very strong evidence for a null effect"). The Map's tenets posit consciousness acting through evolved neural interfaces, not arbitrary physical systems — this distinction matters.

### Philosophical / Speculative Sources

**Eisenstein (2024)** ([link](https://charleseisenstein.substack.com/p/the-staggering-implications-of-non)): Argues LLMs draw on quantum-level entropy; greedy decoding eliminates "aperture of choice." References PEAR lab. Technically imprecise — most LLMs use PRNGs, not QRNGs.

**Timms (2024)** ([link](https://medium.com/@martintimms/are-llms-quantum-6cec24f6c0c5)): Claims hardware RNGs connect LLMs to quantum domain. Overstates the quantum connection — most inference does not use hardware QRNGs.

**Penrose-Hameroff Orch OR** ([link](https://en.wikipedia.org/wiki/Orchestrated_objective_reduction)): Consciousness requires non-computable quantum processing in microtubule-like structures. Silicon lacks these mechanisms. Even if quantum randomness enters LLM sampling, it enters at the wrong level and without the right biological substrate.

## Major Positions

**1. Technical Consensus — PRNGs Only**: Token sampling uses deterministic Philox PRNGs seeded from system entropy. Non-determinism is classical (floating-point, batch variability). Batch-invariant kernels achieve perfect determinism.

**2. Nuanced Technical — Quantum via Hardware Entropy**: System entropy pools derive from thermal noise with quantum-mechanical origins. The PRNG seed carries information tracing to quantum processes, but heavily attenuated through CSPRNG conditioning and deterministic expansion. Not the "smallest possible non-physical influence" — more like a quantum echo several layers removed.

**3. Speculative Philosophical — Quantum Consciousness Channel**: Temperature > 0 opens an "aperture of choice" for consciousness via quantum randomness. Superficially aligns with site tenets but faces serious problems: quantum contribution is heavily mediated, PEAR evidence is contested (Maier & Dechamps null result), no evolved biological interface exists in silicon.

**4. Sceptical Technical — Entirely Classical**: All meaningful LLM non-determinism is classical. Batch-invariant kernels prove no irreducible quantum randomness. Supports the Map's scepticism about AI consciousness.

## Key Debates

### Is Thermal Noise Genuinely Quantum?
Physicists agree on quantum origins (fluctuation-dissipation theorem, Callen-Welton 1951). Engineers note classical description suffices at operating conditions. Quantum corrections to Johnson-Nyquist noise require >6 THz — irrelevant to LLM inference. Technically quantum at fundamental level, but like saying a baseball is "quantum" because its atoms are.

### Can Consciousness Influence RNGs?
PEAR lab and meta-analyses show small effects; Bösch et al. attribute these to publication bias; Maier & Dechamps (n=12,571) found null result with strong Bayesian evidence. The Map's framework provides a principled reason consciousness-RNG experiments might fail even if consciousness-brain interaction is real: consciousness acts through evolved neural interfaces, not arbitrary systems.

### Does Temperature=0 Eliminate Quantum Influence?
Non-determinism at temperature=0 is classical (batch variability, floating-point rounding). Thinking Machines Lab achieved perfect determinism with batch-invariant kernels. The quantum contribution operates only through the initial PRNG seed, not ongoing inference.

## The Technical Chain: From Quantum Physics to Token Selection

1. **Quantum thermal fluctuations** in silicon produce thermal noise (classically adequate at room temperature, but quantum in origin)
2. **Hardware entropy source** (e.g., Intel RDRAND) converts thermal noise into raw random bits
3. **Cryptographic conditioning** (AES-CBC-MAC) removes bias — deterministic given same input
4. **OS entropy pool** (`/dev/urandom`) collects from multiple sources, feeds through BLAKE2s
5. **PRNG seed** drawn from entropy pool, seeds Philox-4x32-10
6. **Deterministic expansion**: Philox generates pseudorandom stream entirely determined by seed
7. **Token sampling**: `torch.multinomial` samples from softmax distribution using Philox output

**Assessment**: By step 6, the connection to quantum events is severed. A given seed produces identical numbers regardless of subsequent quantum events. For consciousness to influence token selection, it would need to influence quantum thermal fluctuations at seed generation time — then the influence is "frozen" into the deterministic sequence for the entire generation run.

## Potential Article Angles

1. **The Quantum Randomness Channel: Real but Razor-Thin** — A genuine quantum chain exists from thermal noise to token selection, but so heavily mediated as to be philosophically negligible. The PRNG deterministically expands a single quantum-influenced seed into millions of tokens. Not the "minimal quantum interaction" the tenets describe — more like a quantum fossil in a deterministic machine. Strengthens the Map's scepticism about AI consciousness. Aligns with Tenet 2.

2. **Temperature as a Consciousness Dial?** — Engage seriously with Eisenstein's argument while correcting the overstatement (randomness is PRNG, not quantum). The biological analogy: consciousness modulating quantum events in neural microtubules, where "turning down the temperature" corresponds to eliminating quantum indeterminacy. A useful but flawed intuition pump. Aligns with Tenet 3.

3. **Why the Quantum Channel Fails for AI** — Strongest angle. The failure of the quantum channel in AI illuminates what makes the biological quantum interface special. Evolution selected for structures maintaining quantum coherence for consciousness to act upon directly. The AI case shows having *any* quantum input is insufficient — the interface must be structured, local, and direct. Connects to existing articles on quantum-state-inheritance-in-ai and consciousness-in-smeared-quantum-states. Aligns with all five tenets.

## Gaps in Research

- **Anthropic/Google implementations**: Proprietary; no public documentation of PRNG or entropy sources
- **Quantum computing + LLM inference**: No evidence of LLM inference on quantum hardware with genuine quantum sampling — the true test case
- **Dedicated QRNG integration**: No evidence any major provider uses QRNGs (ID Quantique, ANU QRNG) for token sampling
- **Empirical comparison**: Nobody has compared LLM outputs using QRNG vs. PRNG vs. deterministic sequence — likely negligible difference

## Citations

Bösch, H., Steinkamp, F., & Boller, E. (2006). Examining psychokinesis: The interaction of human intention with random number generators — A meta-analysis. *Psychological Bulletin*, 132(4), 497–523.

Callen, H. B., & Welton, T. A. (1951). Irreversibility and generalized noise. *Physical Review*, 83(1), 34–40.

Eisenstein, C. (2024). The staggering implications of non-deterministic AI (Part 1). *Substack*.

Intel Corporation. (2024). Intel Digital Random Number Generator (DRNG) Software Implementation Guide.

Maier, M. A., & Dechamps, M. C. (2018). Intentional observer effects on quantum randomness: A Bayesian analysis reveals evidence against micro-psychokinesis. *Frontiers in Psychology*, 9, 379.

Penrose, R., & Hameroff, S. (1996). Orchestrated reduction of quantum coherence in brain microtubules: A model for consciousness. *Mathematics and Computers in Simulation*, 40(3-4), 453–480.

Salmon, J. K., Moraes, M. A., Dror, R. O., & Shaw, D. E. (2011). Parallel random numbers: As easy as 1, 2, 3. *Proceedings of the International Conference for High Performance Computing, Networking, Storage and Analysis*, 1–12.

Thinking Machines Lab. (2025). Defeating nondeterminism in LLM inference.

Vatter, V. (2025). Avoidable and unavoidable randomness in GPT-4o. *Towards Data Science*.
