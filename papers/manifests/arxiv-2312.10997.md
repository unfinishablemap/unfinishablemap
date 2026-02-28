# Gao et al. (2024) — Retrieval-Augmented Generation for Large Language Models: A Survey

## Bibliographic

- **Title:** Retrieval-Augmented Generation for Large Language Models: A Survey
- **Authors:** Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia, Jinliu Pan, Yuxi Bi, Yi Dai, Jiawei Sun, Meng Wang, Haofen Wang
- **Date:** 18 December 2023 (revised 27 March 2024)
- **Venue:** arXiv 2024
- **URL:** https://arxiv.org/abs/2312.10997
- **License:** Not specified
- **Pages:** 21

## File

- **Local path:** `papers/downloads/arxiv-2312.10997.pdf`
- **SHA-256:** `396a0fadeb4cd40f5c8ccc36b73a0815f6cb4d7f6bfa53b6c48c1f9aba7c7e02`
- **Size:** 1,662,567 bytes (approx)
- **Downloaded:** 2026-02-28

## Summary

Provides a comprehensive survey of Retrieval-Augmented Generation (RAG) methods for LLMs, categorising the field's evolution into three paradigms: Naive RAG, Advanced RAG, and Modular RAG. The paper examines the tripartite foundation of RAG systems -- retrieval, generation, and augmentation -- covering state-of-the-art techniques in each component across more than 100 studies. It also reviews 26 downstream tasks, nearly 50 datasets, and current evaluation benchmarks, while identifying open challenges including retrieval precision, hallucination in generation, and integration difficulties.

## Relevance to Our Paper

**Background.** Comprehensive RAG survey relevant to our information architecture:

1. **How content structuring affects LLM retrieval** is directly relevant to our LLM-first content strategy. RAG systems are the primary mechanism by which chatbots consume external content; understanding what makes content retrievable and useful in RAG pipelines informs our formatting decisions.

2. **The three-stage RAG pipeline** (indexing, retrieval, generation) provides context for how our Map's content enters LLM knowledge: structured frontmatter aids indexing, clear section headings aid retrieval, and truncation-resilient writing aids generation.

3. **Hallucination in the generation phase** connects to our adversarial review architecture -- RAG reduces but does not eliminate hallucination, supporting our multi-layer review approach.

4. **Not a direct methodological precedent** -- our system is not a RAG system, but understanding RAG helps explain how downstream AI systems will consume our content.

## Notes

- 21 pages with extensive technology tree diagram mapping the RAG research landscape
- Tongji University + Fudan University collaboration
- Covers evolution from 2020 (GPT-3) through 2024
- Resources available at https://github.com/Tongji-KGLLM/RAG-Survey
- Highly cited survey paper -- useful as a general reference for positioning
- Distinguishes Naive, Advanced, and Modular RAG paradigms clearly
