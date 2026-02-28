# Yao et al. (2023) — Tree of Thoughts: Deliberate Problem Solving with Large Language Models

## Bibliographic

- **Title:** Tree of Thoughts: Deliberate Problem Solving with Large Language Models
- **Authors:** Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan
- **Date:** 17 May 2023 (revised 3 December 2023)
- **Venue:** NeurIPS 2023
- **URL:** https://arxiv.org/abs/2305.10601
- **License:** Not specified
- **Pages:** 14

## File

- **Local path:** `papers/downloads/arxiv-2305.10601.pdf`
- **SHA-256:** `79c5237e3f63953a73f2b0d6894327702ee1f7e981450c251bb1b5cb4f8d7b8f`
- **Size:** 781,000 bytes (approx)
- **Downloaded:** 2026-02-28

## Summary

Tree of Thoughts (ToT) generalises chain-of-thought prompting into a framework where LLMs explore multiple reasoning paths structured as a tree. Each node represents a coherent intermediate thought, and the LLM self-evaluates the progress of different branches, using search algorithms (BFS or DFS) to decide which paths to pursue and when to backtrack. On tasks requiring planning and search — Game of 24, Creative Writing, and Mini Crosswords — ToT dramatically outperforms standard prompting; for instance, GPT-4 with chain-of-thought solved only 4% of Game of 24 tasks while ToT achieved 74%.

## Relevance to Our Paper

**Medium.** ToT is foundational for self-evaluating reasoning systems and provides conceptual grounding for our review architecture:

1. **Self-evaluation as a search heuristic** — ToT's core innovation is using the LLM itself to evaluate which reasoning paths are promising. Our pessimistic and optimistic review layers perform an analogous function at the content level: evaluating which claims, arguments, and articles are worth preserving or revising.

2. **Deliberate exploration vs. greedy generation** — ToT argues that LLMs benefit from exploring alternatives rather than committing to a single left-to-right generation. Our system applies this principle at corpus scale: rather than generating articles once, we systematically revisit and revise content through scheduled review cycles.

3. **Backtracking and the coalesce skill** — ToT's ability to abandon unpromising paths and try alternatives is conceptually similar to our coalesce and archive skills, which consolidate or retire content that isn't serving the knowledge base well.

## Notes

- Authors from Princeton University, Google DeepMind
- Published at NeurIPS 2023
- Inspired by dual-process theory (Kahneman's System 1/System 2) and classical AI planning (Newell, Shaw, Simon)
- Shares co-authors (Yao, Narasimhan) with Reflexion — both from Princeton NLP group
- Code at https://github.com/princeton-nlp/tree-of-thought-llm
- Highly cited; foundational reference for structured LLM reasoning
