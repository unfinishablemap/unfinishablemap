# Brooks & Eggert (2024) — The Rise of AI-Generated Content in Wikipedia

## Bibliographic

- **Title:** The Rise of AI-Generated Content in Wikipedia
- **Authors:** Creston Brooks, Samuel Eggert
- **Date:** 10 October 2024
- **Venue:** WikiNLP 2024
- **URL:** https://arxiv.org/abs/2410.08044
- **License:** Not specified

## File

- **Local path:** `papers/downloads/arxiv-2410.08044.pdf`
- **SHA-256:** `5bfc7f25d64528f9491475c66d3c20e9c6c2e3c286e2c51f5aeb2e45b6d61b71`
- **Size:** 2,100,000 bytes (approx)
- **Downloaded:** 2026-02-28

## Summary

Uses two AI detection tools — GPTZero (proprietary) and Binoculars (open-source, based on cross-perplexity between two LLMs) — to estimate the prevalence of AI-generated content in newly created Wikipedia articles. Compares articles created in August 2024 against a pre-March 2022 baseline across English, French, German, and Italian Wikipedias.

Finds that over 5% of newly created English Wikipedia articles in August 2024 contain significant AI-generated content (with thresholds calibrated for a 1% false positive rate on pre-GPT-3.5 articles). Flagged AI-generated articles are generally lower quality: fewer footnotes per sentence and fewer outgoing wiki-links. Manual inspection of the 45 articles flagged by both detectors reveals self-promotion and partisan viewpoints as common motivations.

## Relevance to Our Paper

**Medium.** Useful for positioning the Map's transparent attribution against the backdrop of undisclosed AI content in knowledge platforms. Key connections:

1. **Documents the problem we aim to solve differently:** Wikipedia has undisclosed AI-generated content of lower quality; the Map makes AI involvement explicit and subjects it to continuous adversarial review.

2. **The quality findings support our architecture:** AI-generated Wikipedia articles are typically worse (fewer citations, less integration) — our multi-layer review system is designed to prevent exactly this quality degradation.

3. **Contrasting approaches to AI in knowledge production:** Wikipedia tries to detect and flag AI content after the fact; the Map builds AI contribution into its workflow from the start with full transparency.

## Notes

- From Princeton University; also lists Denis Peskoff as a co-author on the paper itself
- Code and data at github.com/brooksca3/wiki_collection
- Detection results represent lower bounds — actual AI content could be substantially higher given false negatives
- Short paper (7 pages) — workshop format for WikiNLP
