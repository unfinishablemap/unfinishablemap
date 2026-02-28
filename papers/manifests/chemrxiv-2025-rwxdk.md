# Harb et al. (2025) — Socratic Method for Scientific Assistance

## Bibliographic

- **Title:** Towards Philosophical Reasoning with Agentic LLMs: Socratic Method for Scientific Assistance
- **Authors:** Hassan Harb, Yunkai Sun, Mustafa Unal, Abhishek Aggarwal, Chiara Bissolotti, Işıksu Büyüker, Sungil Hong, Luke Johnson, Lateef Jolaoso, Bratin Sengupta, Michael Stuhr, Zhenzhen Yang, Brian Ingram, Rajeev Surendran Assary
- **Date:** 7 July 2025
- **Venue:** ChemRxiv preprint (published in Machine Learning: Science and Technology)
- **DOI:** https://doi.org/10.26434/chemrxiv-2025-rwxdk
- **Landing page:** https://chemrxiv.org/engage/chemrxiv/article-details/68655830c1cb1ecda0b4d2e9
- **License:** CC-BY-NC 4.0
- **Pages:** 27 (including supplementary)
- **Views/Downloads:** 1,802 / 1,002

## File

- **Local path:** `papers/downloads/chemrxiv-2025-rwxdk.pdf`
- **SHA-256:** `9059acb71f0ff9d3976b6962de109eea38719a9c45886dc79cb2c6c17101cb80`
- **Size:** 582,426 bytes
- **Downloaded:** 2026-02-28

## Summary

Introduces a "Socratic Method Agent" (SM Agent) — a single-agent system that uses a structured system prompt encoding ten classical Socratic principles (definition, generalization, induction, elenchus, hypothesis elimination, dialectic, maieutic, recollection, irony, analogy) to improve LLM scientific reasoning. Built on GPT-4o via Argonne National Lab's internal ChatGPT interface. No fine-tuning or external tools.

The agent follows a 4-step pipeline: (1) select relevant Socratic principles, (2) reformulate the user's question as a Socratic inquiry, (3) self-query and answer, (4) generate follow-up questions. The authors call this "Chain-of-Reasoning" (CoR) — distinct from Chain-of-Thought in that it emphasises epistemic structure and iterative refinement rather than step-by-step problem decomposition.

Evaluated on 12 domain-specific tasks across chemistry, materials science, and physics, plus the ARC Challenge dataset where it achieved 97.15% accuracy (SOTA at time of publication, surpassing GPT-4o+CoT at 94.88%).

## Relevance to Our Paper

**Low-medium.** This paper uses philosophical methods to structure LLM prompting for *scientific* reasoning. Our work uses LLMs to produce *philosophical* content. The connection is inverted:

- **Harb et al.:** Philosophy → LLM prompting strategy → better science outputs
- **Our work:** LLM system → philosophical content production → continuous self-improvement

**Citable as:** Evidence that philosophical principles can meaningfully structure AI reasoning (supports our claim that tenet constraints improve output quality). Also relevant as a contrast — their system is single-agent, single-prompt, single-session; ours is multi-skill, multi-review-layer, continuous over months.

**Key difference:** Their "agent" is really a prompt engineering technique applied per-session. Our system is an autonomous evolution loop running thousands of sessions with persistent state, task queues, and adversarial review layers. They improve individual responses; we improve an entire knowledge base over time.

## Notes

- The term "agentic" in their title is used loosely — the agent is a system prompt, not a tool-using autonomous agent in the modern sense. It autonomously selects Socratic principles and generates follow-ups, but doesn't use tools, access external data, or maintain state.
- The paper is well-structured and uses a format we should note: title page with abstract + keywords, numbered sections, figures with captions, comparison tables, bar chart for benchmark results, substantial discussion section.
- 27 pages is on the longer end for a preprint; includes extensive case-study tables.
- Published on ChemRxiv (chemistry preprint server) rather than arXiv CS or SSRN — disciplinary venue choice matters.
