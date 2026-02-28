# Goldstein (2024) — LLMs Can Never Be Ideally Rational

## Bibliographic

- **Title:** LLMs Can Never Be Ideally Rational
- **Authors:** Simon Goldstein
- **Date:** 2024
- **Venue:** PhilArchive preprint
- **URL:** https://philarchive.org/rec/GOLLCN
- **License:** Not specified
- **Pages:** ~25

## File

- **Local path:** `papers/downloads/philarchive-GOLLCN.pdf`
- **SHA-256:** `4196fa38712c4e207f0b978da098e21626e02dcbcc4e47e2aff413d0490873cf`
- **Size:** 318,464 bytes (approx)
- **Downloaded:** 2026-02-28

## Summary

Demonstrates an in-principle limit to LLM agency rooted in their architecture as next-word predictors. Goldstein shows that LLMs are "Dutch bookable" — their probabilistic predictions are guaranteed to be incoherent and violate the axioms of probability calculus — and that their preferences over actions are guaranteed to be intransitive, making them exploitable via money pumps. The core argument is that selecting the most likely next token is structurally different from selecting an action that maximises expected value, so probability cannot be forced into the shape of genuine rational agency.

## Relevance to Our Paper

**High.** Provides theoretical grounding for our architectural decisions:

1. **Motivates our constraint architecture** — if raw LLM output is inherently unreliable at the level of rational coherence, then systematic constraints (tenets) and adversarial review layers are architecturally necessary, not optional quality improvements.

2. **Supports multi-layer review** — the impossibility of ideal rationality in single-pass generation justifies why we use pessimistic review, optimistic review, deep review, and outer review rather than trusting any single generation.

3. **Philosophical depth** — engages with decision theory and philosophy of mind (beliefs, desires, coherence), which positions our paper within serious philosophical discourse rather than pure engineering.

## Notes

- Uses formal decision-theoretic arguments (Dutch books, money pumps) rather than empirical benchmarks
- Complements Xu et al. (#28) on hallucination inevitability — Goldstein shows rationality limits, Xu shows factual accuracy limits
- The exploitability result has an interesting upside the author notes: it may help with AI safety by providing a mechanism to control LLM agents
