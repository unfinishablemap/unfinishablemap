# Estornell & Liu (2024) — Multi-LLM Debate: Framework, Principals, and Interventions

## Bibliographic

- **Title:** Multi-LLM Debate: Framework, Principals, and Interventions
- **Authors:** Andrew Estornell, Yang Liu
- **Date:** 2024
- **Venue:** NeurIPS 2024
- **URL:** https://proceedings.neurips.cc/paper_files/paper/2024/hash/32e07a110c6c6acf1afbf2bf82b614ad-Abstract-Conference.html
- **License:** Not specified
- **Pages:** 14

## File

- **Local path:** `papers/downloads/arxiv-2411.18472.pdf`
- **SHA-256:** `cdfd0958df2c71fe8d3069a7fa6cad3d6a32e610a0eaf2c4a415ef28144cd0ea`
- **Size:** 1,919,488 bytes (approx)
- **Downloaded:** 2026-02-28

## Summary

Formalises multi-LLM debate as a mathematical framework, analysing what happens when multiple language models discuss a question to reach a consensus answer. The paper shows that when debating models share similar training data, they tend to converge on the majority opinion -- including shared misconceptions -- rather than reliably correcting errors. The authors propose three interventions (principal-guided mechanisms) that improve debate outcomes across BoolQ, MMLU, MathQ, and TruthfulQA benchmarks.

Re-downloaded from NeurIPS proceedings; verified as correct paper.

## Relevance to Our Paper

**Medium-high.** Extends Du et al. (#20) with a more rigorous mathematical treatment of multi-LLM debate:

1. **Convergence to shared misconceptions** is directly relevant to our architecture: it explains why using the same model for both generation and review risks reinforcing blind spots, motivating our outer-review skill that deliberately uses different AI systems.

2. **The proposed interventions** (principal-guided debate) parallel our structured adversarial review layers -- pessimistic review, optimistic review, and outer review each serve as different "principals" steering the critique process.

3. **Formal framework** provides theoretical grounding for why multi-perspective review architectures (like ours) should outperform single-model self-critique.

## Notes

- NeurIPS 2024 publication -- high venue prestige
- 14 pages including supplementary material
- Benchmarks on BoolQ, MMLU, MathQ, TruthfulQA -- standard LLM evaluation suites
- Re-downloaded from NeurIPS proceedings after initial download fetched wrong paper
