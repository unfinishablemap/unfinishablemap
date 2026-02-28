# Qu et al. (2024) — Recursive Introspection: Teaching Language Model Agents How to Self-Improve (RISE)

## Bibliographic

- **Title:** Recursive Introspection: Teaching Language Model Agents How to Self-Improve
- **Authors:** Yuxiao Qu, Tianjun Zhang, Naman Garg, Aviral Kumar
- **Date:** 25 July 2024 (revised 26 July 2024)
- **Venue:** NeurIPS 2024
- **URL:** https://arxiv.org/abs/2407.18219
- **License:** Not specified
- **Pages:** 28

## File

- **Local path:** `papers/downloads/arxiv-2407.18219.pdf`
- **SHA-256:** `21870776f1d07c49d6a52a5af0b27e7161473517dc7ede7f17ec66ae1aa0d690`
- **Size:** 4,500,000 bytes (approx)
- **Downloaded:** 2026-02-28

## Summary

RISE (Recursive IntroSpEction) introduces a fine-tuning approach that teaches LLMs to iteratively self-improve their responses over multiple turns. The method frames single-turn prompting as a multi-turn Markov decision process, using on-policy data collection and reward-weighted regression to train models that can recursively detect and correct their own mistakes. RISE achieves a 17.7% improvement for LLaMA2-7B over five turns of introspection on GSM8K, and scales well with more capable models, demonstrating that self-improvement capability can be trained into models that otherwise fail to improve across sequential attempts.

## Relevance to Our Paper

**Medium.** RISE demonstrates that iterative self-improvement yields compounding gains, supporting the Map's deep-review cycles:

1. **Iterative improvement yields compounding returns** — RISE shows that models improve monotonically over multiple turns of self-correction. Our deep-review cycles operate on a similar principle: each review pass over an article can find and fix issues that previous passes missed, with quality improving through iteration.

2. **Self-improvement requires architectural support** — a key finding is that off-the-shelf LLMs cannot self-improve even when told their mistakes; the capability must be structurally enabled. This parallels our design choice to build explicit review infrastructure (scheduled review cycles, distinct review modes, evolution state tracking) rather than relying on ad-hoc self-correction.

3. **Training-based vs. prompt-based self-improvement** — RISE uses fine-tuning to instil self-improvement capability, whereas our system achieves iterative improvement through prompt-based review layers and persistent state. The contrast is useful for positioning our approach as complementary.

## Notes

- Work done at Carnegie Mellon University, UC Berkeley, and MultiOn
- Tested on LLaMA2, LLaMA3, and Mistral models on GSM8K and MATH benchmarks
- GPT-3.5 only improves 4.6% over five turns vs. RISE's 17.7% — showing the gap between prompting and training for self-improvement
- Published at NeurIPS 2024
- Distinguishes itself from GLoRE and Self-Correct by training over more than two turns
