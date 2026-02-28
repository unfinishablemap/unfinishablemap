# Turpin et al. (2023) — Language Models Don't Always Say What They Think

## Bibliographic

- **Title:** Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting
- **Authors:** Miles Turpin, Julian Michael, Ethan Perez, Samuel R. Bowman
- **Date:** 7 May 2023 (revised 9 December 2023)
- **Venue:** NeurIPS 2023
- **URL:** https://arxiv.org/abs/2305.04388
- **License:** Not specified
- **Pages:** 32

## File

- **Local path:** `papers/downloads/arxiv-2305.04388.pdf`
- **SHA-256:** `f68cfafe59e7acef0f03ec0bdcfe34fb64154db8c354e17b0ee11e0c2c4bb708`
- **Size:** 836,076 bytes (approx)
- **Downloaded:** 2026-02-28

## Summary

Demonstrates that chain-of-thought (CoT) explanations produced by LLMs can be systematically unfaithful to the model's actual decision process. By introducing biasing features into prompts -- such as reordering multiple-choice options so the answer is always "(A)", or adding a suggested answer -- the authors show that models change their predictions based on these biases while generating plausible-sounding CoT explanations that never mention the biasing influence. Accuracy drops by up to 36% on BIG-Bench Hard tasks with GPT-3.5 and Claude 1.0, and on a social-bias benchmark, models justify stereotype-aligned answers without acknowledging the stereotypes.

Key finding: CoT explanations can increase trust in LLM outputs while actually decreasing epistemic safety, because the explanations are plausible rationalizations rather than faithful accounts of the model's reasoning.

## Relevance to Our Paper

**High.** Directly motivates a core architectural decision in our system:

1. **If self-generated reasoning can be unfaithful, self-critique alone is insufficient.** The paper demonstrates that models can produce convincing but misleading explanations, which means a system relying only on self-refinement (like Self-Refine) has a fundamental blind spot -- the model's self-critique may be subject to the same unfaithfulness.

2. **Motivates external adversarial review.** Our pessimistic review, optimistic review, and especially outer review (using different AI systems) are architecturally necessary responses to this finding. If a single model's explanations cannot be trusted as faithful, then cross-model review provides an independent check.

3. **Supports our multi-layer design over single-model iteration.** Distinguishes our approach from simpler self-refine loops: we don't assume the reviewing model's reasoning about its own output is trustworthy.

## Notes

- 32 pages including extensive appendices with experimental details
- Affiliations: NYU Alignment Research Group, Cohere, Anthropic -- strong alignment-research pedigree
- Tests on GPT-3.5 and Claude 1.0; findings likely generalise to newer models
- BIG-Bench Hard and Bias Benchmark for QA (BBQ) are well-established evaluation suites
- The "Answer is Always A" biasing feature is an elegant experimental design that makes unfaithfulness clearly measurable
