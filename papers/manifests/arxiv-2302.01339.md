# Schwitzgebel et al. (2023) — Creating a Large Language Model of a Philosopher

## Bibliographic

- **Title:** Creating a Large Language Model of a Philosopher
- **Authors:** Eric Schwitzgebel, David Schwitzgebel, Anna Strasser
- **Date:** 2 February 2023 (revised 9 May 2023)
- **Venue:** arXiv preprint (cs.CL, cs.AI)
- **URL:** https://arxiv.org/abs/2302.01339
- **License:** Not specified
- **Pages:** 36

## File

- **Local path:** `papers/downloads/arxiv-2302.01339.pdf`
- **SHA-256:** `d10ff1992ff1c95b380eff31ca684f581cc4af0412ecdd6756cc447290b59d85`
- **Size:** 673,600 bytes (approx)
- **Downloaded:** 2026-02-28

## Summary

Fine-tuned GPT-3 on Daniel Dennett's published philosophical works, then ran a discrimination study (N=425) where participants tried to distinguish Dennett's actual answers to philosophical questions from the model's outputs. Experts identified Dennett at 51% (above 20% chance but far below expectations). Ordinary participants were near chance. The model occasionally produced answers experts preferred over Dennett's own.

Key finding: LLMs can produce paragraph-length philosophical text that even domain experts struggle to distinguish from a professional philosopher's output — without cherry-picking.

## Relevance to Our Paper

**High.** This is one of the closest precedents to our work. Key connections:

1. **Establishes that LLMs can produce credible philosophical text** — our paper can cite this as prior evidence, then extend it: Schwitzgebel showed LLMs can mimic one philosopher; we show they can contribute to an evolving philosophical knowledge base.

2. **Their approach vs. ours is a useful contrast:**
   - Schwitzgebel: fine-tune on one philosopher's corpus → generate in that philosopher's voice → evaluate via Turing-style discrimination
   - Our approach: constrain via explicit tenets (not training data) → generate original content → evaluate via adversarial multi-layer review → iterate continuously

3. **They acknowledge the limitation:** their model mimics Dennett, it doesn't do original philosophy. Our system attempts something more ambitious — original philosophical content that evolves through review.

4. **The "no cherry-picking" principle** resonates with our transparency approach (ai_contribution scores, public version history).

## Notes

- APA-style formatting (unusual for CS papers — reflects philosophy venue expectations)
- 36 pages including extensive appendices with actual Q&A examples
- Published 2023, before GPT-4 — results would likely be even more striking with current models
- Schwitzgebel is a major figure in philosophy of mind — his involvement lends credibility to this research direction
- The paper's framing ("how safe is philosophy from AI?") is complementary to ours ("how can AI contribute to philosophy?")
