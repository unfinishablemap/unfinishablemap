# Huang et al. (2024) — Collective Constitutional AI: Aligning a Language Model with Public Input

## Bibliographic

- **Title:** Collective Constitutional AI: Aligning a Language Model with Public Input
- **Authors:** Saffron Huang, Divya Siddarth, Liane Lovitt, Thomas I. Liao, Esin Durmus, Alex Tamkin, Deep Ganguli
- **Date:** 12 June 2024
- **Venue:** ACM Conference on Fairness, Accountability, and Transparency (FAccT 2024)
- **URL:** https://arxiv.org/abs/2406.07814
- **License:** Not specified
- **Pages:** 23

## File

- **Local path:** `papers/downloads/arxiv-2406.07814.pdf`
- **SHA-256:** `bf59c3f9a5c569b7c29063a24803128f7c3c8228790fa451e838cd1536cf9d15`
- **Size:** 2,831,155 bytes (approx)
- **Downloaded:** 2026-02-28

## Summary

Presents Collective Constitutional AI (CCAI), a multi-stage framework for sourcing constitutional principles from public input rather than developer fiat. A representative sample of ~1,000 U.S. adults contributed principles via the Polis deliberation platform, which were then used to fine-tune a Claude model. The publicly-sourced model showed lower bias across nine social dimensions compared to Anthropic's standard constitution model, while maintaining equivalent performance on language, math, and helpfulness benchmarks.

## Relevance to Our Paper

**Medium-high.** Key connections:

1. **Extends Constitutional AI to democratic input** — while our tenets are author-defined philosophical commitments, CCAI demonstrates the broader principle that natural-language constitutions can come from diverse sources and meaningfully shape model behavior.

2. **Validates the tenet-as-constraint paradigm** — CCAI shows that explicit principles sourced externally (from the public; in our case, from a philosophical framework) can guide generation without degrading capability. This supports our claim that tenet-constrained content production is viable.

3. **Useful contrast in constraint purpose:** CCAI constrains for safety/bias reduction; we constrain for philosophical coherence. Both use natural-language principles as the mechanism.

## Notes

- Published at FAccT 2024 (Rio de Janeiro), a top venue for AI ethics and fairness
- Joint work between the Collective Intelligence Project and Anthropic
- Includes open data: anonymized public input and the Jupyter notebook used to create the constitution
- 23 pages including appendices with the full public constitution
