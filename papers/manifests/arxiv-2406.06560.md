# Findeis et al. (2024) — Inverse Constitutional AI: Compressing Preferences into Principles

## Bibliographic

- **Title:** Inverse Constitutional AI: Compressing Preferences into Principles
- **Authors:** Arduin Findeis, Timo Kaufmann, Eyke Hullermeier, Samuel Albanie, Robert Mullins
- **Date:** 21 April 2025 (revised; originally June 2024)
- **Venue:** ICLR 2025
- **URL:** https://arxiv.org/abs/2406.06560
- **License:** Not specified
- **Pages:** 32

## File

- **Local path:** `papers/downloads/arxiv-2406.06560.pdf`
- **SHA-256:** `8788cb9cec5ca02033d3502a58d1c058b17f6b38cc753437a0d662906fdd5ef5`
- **Size:** 1,782,579 bytes (approx)
- **Downloaded:** 2026-02-28

## Summary

Formulates the Inverse Constitutional AI (ICAI) problem: given a dataset of pairwise text preferences (human or AI feedback), extract a compact set of natural-language principles (a "constitution") that best explains those preferences. The algorithm proceeds through five steps — principle generation, clustering, subsampling, testing, and filtering — to produce interpretable constitutions. Validated on synthetic data, AlpacaEval, Chatbot Arena, and PRISM datasets, the method can detect annotator biases and generate personalized constitutions from preference data.

## Relevance to Our Paper

**Medium.** Key connections:

1. **Inverse of our approach** — we start with explicit principles (tenets) and generate content constrained by them; ICAI starts with preference data and reverse-engineers the implicit principles. This is a clean conceptual contrast that illuminates the design space.

2. **Validates that principles and preferences are interconvertible** — if preferences can be compressed into principles, then our tenet-first approach is a legitimate alternative entry point into the same design space.

3. **Bias detection application** — ICAI's ability to surface hidden biases in preference data is relevant to our concern about AI blind spots (addressed via our outer-review mechanism).

## Notes

- Published at ICLR 2025 (the paper header confirms this, though the references.md listed it as arXiv 2024)
- Code released at https://github.com/rdnfn/icai
- The constitutions are described as "lossy, non-unique" compressions — acknowledges that multiple principle sets could explain the same preferences
- University of Cambridge and LMU Munich collaboration
