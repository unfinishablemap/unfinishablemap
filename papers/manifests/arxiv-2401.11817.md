# Xu, Jain & Kankanhalli (2024) — Hallucination is Inevitable: An Innate Limitation of Large Language Models

## Bibliographic

- **Title:** Hallucination is Inevitable: An Innate Limitation of Large Language Models
- **Authors:** Ziwei Xu, Sanjay Jain, Mohan Kankanhalli
- **Date:** January 2024 (revised February 2025)
- **Venue:** arXiv preprint (cs.CL)
- **URL:** https://arxiv.org/abs/2401.11817
- **License:** Not specified
- **Pages:** ~30

## File

- **Local path:** `papers/downloads/arxiv-2401.11817.pdf`
- **SHA-256:** `a68efd295e8cd65e9115fca6bcc5d42829021a9602dcfae61baa70ba11e6e33d`
- **Size:** 812,032 bytes (approx)
- **Downloaded:** 2026-02-28

## Summary

Provides a formal proof that hallucination cannot be eliminated in LLMs, establishing it as a mathematical inevitability rather than an engineering problem to be solved. The authors define a formal world of computable functions, define hallucination as inconsistency between an LLM and a ground truth function, and use results from learning theory to show that no computable LLM can learn all computable functions — and therefore must inevitably hallucinate. Since the formal world is a subset of the real world, the result applies to real-world LLMs regardless of model architecture, learning algorithms, or training data.

## Relevance to Our Paper

**High.** Provides strong theoretical motivation for our architecture:

1. **Directly motivates multi-layer adversarial review** — if no single generation pass can be hallucination-free (proven, not conjectured), then systematic post-generation review is structurally required. Our pessimistic review, deep review, and outer review layers are a direct architectural response to this inevitability.

2. **Strengthens our contribution claim** — we are not just adding review for quality; we are addressing a proven limitation. This elevates our architecture from "nice to have" to "theoretically necessary."

3. **Complements Goldstein (#26)** — Goldstein shows rationality limits (incoherent probabilities, intransitive preferences), Xu et al. show factual accuracy limits (inevitable hallucination). Together they establish that both the reasoning and the factual content of single-pass LLM output are fundamentally unreliable.

## Notes

- From National University of Singapore (School of Computing)
- Uses formal learning theory (computability, training procedures) rather than empirical benchmarks
- The formal framework also allows evaluating existing hallucination mitigation methods, finding that retrieval augmentation and verification can reduce but never eliminate hallucination
- Under review as of the latest revision
