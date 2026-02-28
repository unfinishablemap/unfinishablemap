# Aggarwal et al. (2024) — GEO: Generative Engine Optimization

## Bibliographic

- **Title:** GEO: Generative Engine Optimization
- **Authors:** Pranjal Aggarwal, Vishvak Murahari, Tanmay Rajpurohit, Ashwin Kalyan, Karthik Narasimhan, Ameet Deshpande
- **Date:** 16 November 2023 (revised 28 June 2024)
- **Venue:** KDD 2024
- **URL:** https://arxiv.org/abs/2311.09735
- **License:** Not specified
- **Pages:** 12

## File

- **Local path:** `papers/downloads/arxiv-2311.09735.pdf`
- **SHA-256:** `beb95332fcbc6f32078c98cd37d0b8ea44f91968d11262344cf452beecf41f41`
- **Size:** 1,416,018 bytes (approx)
- **Downloaded:** 2026-02-28

## Summary

Introduces Generative Engine Optimization (GEO), the first framework for optimizing web content visibility in AI-powered search engines (generative engines) that synthesize responses from multiple sources rather than returning ranked links. The paper formalises generative engines mathematically, defines new visibility metrics tailored to this paradigm, and proposes a benchmark (GEO-bench) of 10,000 queries across diverse domains. Key finding: including citations, quotations from relevant sources, and statistics can boost source visibility by over 40% in generative engine responses, though optimal strategies vary by domain.

## Relevance to Our Paper

**Key paper.** First academic work defining optimization for AI-generated search responses:

1. **Establishes the field our content strategy operates in.** GEO defines the problem of being cited by AI systems; our Map's LLM-first content strategy is a related but distinct approach -- we optimize for chatbot *consumption* of philosophical content rather than search *visibility* per se.

2. **Their finding that citations and statistics boost visibility by 40%** provides empirical justification for our content formatting decisions (structured frontmatter, explicit cross-references, named anchors).

3. **Useful contrast:** GEO treats content creators as optimizing for inclusion in AI responses; our approach treats AI as both producer and consumer of the content, with humans as the architectural directors.

4. **Domain variation** finding is relevant -- philosophical content may respond differently to GEO strategies than commercial or factual content.

## Notes

- Published at KDD 2024 (top data-mining venue) -- lends credibility to this emerging research direction
- 12 pages in ACM format
- Princeton + IIT Delhi collaboration
- Code and data available at https://generative-engines.com/GEO/
- Tested on Perplexity.ai as a real-world generative engine, showing up to 37% visibility improvement
- The GEO-bench benchmark could potentially be useful for evaluating our own content's discoverability
