# Gou et al. (2024) — CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing

## Bibliographic

- **Title:** CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing
- **Authors:** Zhibin Gou, Zhihong Shao, Yeyun Gong, Yelong Shen, Yujiu Yang, Nan Duan, Weizhu Chen
- **Date:** 19 May 2023 (revised 21 February 2024)
- **Venue:** ICLR 2024
- **URL:** https://arxiv.org/abs/2305.11738
- **License:** Not specified
- **Pages:** 24

## File

- **Local path:** `papers/downloads/arxiv-2305.11738.pdf`
- **SHA-256:** `ed5cbff53c8ff550b72d6abba0d7e4d83c5d214d61d0fafde10cbe4bbfc31a5b`
- **Size:** 1,600,000 bytes (approx)
- **Downloaded:** 2026-02-28

## Summary

CRITIC presents a unified framework that enables black-box LLMs to verify and correct their own outputs through interaction with external tools such as search engines, knowledge bases, and code interpreters. The system follows a verify-then-correct loop: the LLM first generates an output, then uses tools to critique specific aspects (plausibility, truthfulness, correctness), and finally revises the output based on the critiques. Evaluated across free-form QA, mathematical reasoning, and toxicity reduction tasks, CRITIC consistently improves performance while highlighting that LLM self-correction without external feedback is unreliable.

## Relevance to Our Paper

**Medium.** CRITIC's tool-interactive verification is relevant to the Map's use of external validation:

1. **External feedback is essential for reliable self-correction** — CRITIC's key finding that LLMs struggle to self-correct without external tools supports our architectural decision to include outer-review (using different AI systems) rather than relying solely on same-model self-critique.

2. **Verify-then-correct maps to our review-then-revise pattern** — CRITIC's iterative loop of generating, verifying with tools, and correcting parallels our deep-review and pessimistic-review skills, though we operate at article scale rather than individual response scale.

3. **Underscores the unreliability of pure self-evaluation** — the paper's finding that all tested LLMs are unreliable at validating their own results reinforces why our architecture uses multiple distinct review modes and external review rather than a single self-check pass.

## Notes

- Work done at Tsinghua University and Microsoft Research Asia
- Tested across ChatGPT, Text-Davinci-003, and LLaMA-2 variants (7B, 13B, 70B)
- 7.7 F1 improvement on QA, 7.0% on math, 79.2% toxicity reduction when applied to ChatGPT
- Code released at https://github.com/microsoft/ProphetNet/tree/master/CRITIC
- Published at ICLR 2024
