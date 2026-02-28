# Shao et al. (2024) — STORM: Assisting in Writing Wikipedia-like Articles

## Bibliographic

- **Title:** Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models
- **Authors:** Yijia Shao, Yucheng Jiang, Theodore A. Kanell, Peter Xu, Omar Khattab, Monica S. Lam
- **Date:** 22 February 2024 (revised 8 April 2024)
- **Venue:** NAACL 2024
- **URL:** https://arxiv.org/abs/2402.14207
- **License:** Not specified

## File

- **Local path:** `papers/downloads/arxiv-2402.14207.pdf`
- **SHA-256:** `dae3d662c85488ce41f3fbae8f66224431acb8ab6a5a5fb3ae3bb5c84b0d0f0b`
- **Size:** 1,300,000 bytes (approx)
- **Downloaded:** 2026-02-28

## Summary

Proposes STORM (Synthesis of Topic Outlines through Retrieval and Multi-perspective Question Asking), a system that automates the pre-writing stage of generating Wikipedia-like articles from scratch. STORM discovers diverse perspectives on a topic, simulates multi-turn conversations where perspective-carrying writers pose questions to a topic expert grounded on Internet sources, then curates the collected information into a structured outline that can be expanded into a full-length article.

Evaluated using FreshWiki, a curated dataset of recent high-quality Wikipedia articles, plus expert feedback from experienced Wikipedia editors. Editors found STORM articles more organized (25% absolute increase) and broader in coverage (10% increase) compared to an outline-driven RAG baseline, while also identifying challenges such as source bias and fabricated connections between unrelated facts.

## Relevance to Our Paper

**High.** Closest system-level comparison to the Map. Key connections:

1. **Both systems generate long-form knowledge articles from scratch using LLMs.** STORM produces single-shot Wikipedia-style articles; the Map continuously evolves a philosophical knowledge base through adversarial self-review.

2. **The contrast is instructive:** STORM is single-pass generation (research → outline → article), while the Map adds persistent state, multi-layer review, tenet constraints, and continuous improvement over months. STORM generates individual articles; the Map manages an entire evolving corpus.

3. **STORM's identified limitations motivate our architecture:** source bias and fabricated connections are exactly the problems our pessimistic review and outer review layers are designed to catch over time.

## Notes

- From Stanford's OVAL lab; code and data released at https://github.com/stanford-oval/storm
- The FreshWiki dataset mitigates data leakage by using articles created/edited after LLM training cutoffs
- Extended by Co-STORM (Jiang et al., EMNLP 2024), which adds human-AI collaborative curation — also in our bibliography
