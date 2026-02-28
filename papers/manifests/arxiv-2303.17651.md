# Madaan, Tandon et al. (2023) — Self-Refine: Iterative Refinement with Self-Feedback

## Bibliographic

- **Title:** Self-Refine: Iterative Refinement with Self-Feedback
- **Authors:** Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon, Nouha Dziri, Shrimai Prabhumoye, Yiming Yang, Shashank Gupta, Bodhisattwa Prasad Majumder, Katherine Hermann, Sean Welleck, Amir Yazdanbakhsh, Peter Clark
- **Date:** March 2023 (revised May 2023)
- **Venue:** NeurIPS 2023
- **URL:** https://arxiv.org/abs/2303.17651
- **License:** Not specified
- **Pages:** ~30

## File

- **Local path:** `papers/downloads/arxiv-2303.17651.pdf`
- **SHA-256:** `81e44592314d80218ad108d3490cd0b84ba5962fefd5c84819987afd77a57087`
- **Size:** 2,097,152 bytes (approx)
- **Downloaded:** 2026-02-28

## Summary

Introduces Self-Refine, an approach where the same LLM generates an initial output, provides feedback on that output, and then refines it iteratively — without any supervised training data, additional training, or reinforcement learning. Evaluated across 7 diverse tasks (dialogue, code optimisation, mathematical reasoning, etc.) using GPT-3.5 and GPT-4, Self-Refine improves outputs by approximately 20% absolute over single-pass generation on average, as measured by both human preference and automatic metrics. The key insight is that LLMs can be effective critics of their own work at test time.

## Relevance to Our Paper

**High (seminal).** One of the foundational papers for our review architecture:

1. **Establishes the core principle we extend** — Self-Refine shows a single LLM can generate, critique, and improve its own output. Our review layers (pessimistic, optimistic, deep review) extend this principle from individual responses to a persistent, evolving knowledge base.

2. **Key contrast in scope** — Self-Refine operates on single outputs in a single session; our system operates on a corpus of ~300 articles over months, with review history persisted in changelogs and evolution state. We extend self-refinement from episodic to continuous.

3. **Validates the feedback-then-refine loop** — our deep-review skill follows essentially the same generate-feedback-refine pattern, but applied to existing articles rather than fresh generations.

4. **Limitation we address** — Self-Refine uses the same model for all three roles (generator, critic, refiner). Our outer-review skill uses a different AI system for cross-validation, addressing the shared-blindspot problem.

## Notes

- Multi-institutional collaboration: CMU, Allen AI, University of Washington, NVIDIA, UC San Diego, Google Research
- Published at NeurIPS 2023, one of the top ML venues — high credibility
- Code and data available at https://selfrefine.info/
- The ~20% improvement figure is a useful benchmark when discussing the value of iterative review
- Pre-dates more sophisticated multi-agent debate approaches but establishes the foundational single-agent self-critique pattern
