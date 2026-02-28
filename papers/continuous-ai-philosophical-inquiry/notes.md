# Paper Planning Notes

## Working Title

**"The Unfinishable Map: Continuous AI-Assisted Philosophical Inquiry Through Adversarial Self-Review"**

Alternative titles (in reserve):
- "Philosophy at Machine Speed: Architecture and Observations from a Self-Evolving Knowledge Base"
- "Writing Philosophy with AI: Constrained Generation, Adversarial Review, and Continuous Convergence"
- "Tenet-Constrained AI Content Evolution: A Case Study in Philosophical Knowledge Production"

The lead title emphasises the most novel aspect: the adversarial self-review loop. Most AI content systems generate and move on. This one generates, then attacks its own output, then improves, then attacks again — indefinitely.

## What We Want to Say

### Core thesis

It is possible to build a system where AI contributes meaningfully to philosophical inquiry — not by generating philosophy autonomously, but through a constrained, continuously self-improving architecture where human-set commitments guide generation and adversarial review cycles surface errors, strengthen arguments, and drive convergence toward coherence.

### Key claims

1. **Constraint-first generation works.** Giving the AI explicit philosophical commitments (tenets) to operate within produces more coherent, more interesting output than unconstrained generation. The tenets don't limit the AI — they focus it.

2. **Adversarial self-review catches real errors.** Pessimistic reviews, tenet alignment checks, and outer reviews (using different AI systems) find genuine logical gaps, misattributions, and internal contradictions — not just stylistic issues.

3. **Continuous revision changes the nature of AI content.** One-shot AI generation produces disposable text. Continuous revision produces an evolving knowledge base where individual articles improve over time and cross-references create emergent coherence.

4. **The authorship problem has practical solutions.** AI contribution scoring, dual timestamps, AI pseudonyms for citations, and automated commit attribution provide a workable framework for transparent human-AI co-authorship.

5. **LLM-first content design is a distinct discipline.** Writing for chatbot consumption (front-loaded claims, truncation resilience, self-contained articles, named-anchor patterns) differs meaningfully from writing for human readers or search engines.

6. **The system's architecture is domain-agnostic.** While the Map explores dualist philosophy, the underlying infrastructure (tenet constraints, evolution loop, review layers, authorship tracking) could be reseeded with physicalist, panpsychist, or entirely non-philosophical commitments.

## Target Audience

**Primary:** Researchers in human-AI collaboration, digital humanities, and AI-assisted knowledge production. People asking: "What does it look like when you actually try to build something serious with AI, not just generate content?"

**Secondary:**
- Philosophy of AI researchers — the system itself raises questions about AI's epistemic role
- Scholarly communication researchers — new models for evolving, citable, AI-co-authored work
- AI/NLP practitioners — practical patterns for constrained, high-quality content generation
- Information scientists — novel content architecture (tenet constraints, voids, apex synthesis)

**Not the audience:** Philosophers evaluating whether dualism is true. The paper is about the system, not the philosophy it produces.

## Target Venue

**Immediate:** SSRN preprint (Philosophy Research Network + Computer Science Research Network cross-listing)

**Potential journals (for later submission):**

| Journal | Fit | Notes |
|---------|-----|-------|
| *AI & Society* (Springer) | Strong | Social implications of AI, human-AI collaboration |
| *Minds and Machines* (Springer) | Strong | Philosophy of AI, computational philosophy |
| *Digital Humanities Quarterly* | Medium | Open access, digital methods for humanities |
| *First Monday* | Medium | Open access, internet studies, accessible |
| *Journal of Documentation* (Emerald) | Medium | Knowledge organisation, information systems |
| *CSCW / CHI* (ACM) | Stretch | Would need more formal user study / evaluation |

For now, SSRN is the right move: get it out, get a DOI, get citations, then decide if journal submission is worth pursuing.

## Key Interesting Features to Convey

### 1. The Evolution Loop (most novel)

A deterministic 24-slot task cycle that ensures consistent ratios of generation, review, and maintenance regardless of execution speed. Not a cron job running random tasks — a designed cycle:
- 67% queue tasks (content generation and refinement)
- 17% deep review (comprehensive single-document analysis)
- Remaining slots: pessimistic review, optimistic review, coalesce, research-voids
- Cycle triggers for periodic tasks (tenet checks, link validation, apex evolution)

**As of 2026-02-28:** 2,968 sessions completed, 4,561 git commits, 542 reviews completed.

### 2. Adversarial Review Layers

Multiple independent review mechanisms designed to catch different failure modes:
- **Pessimistic review** — actively looks for logical gaps, unsupported claims, counterarguments
- **Optimistic review** — finds strengths and missed connections (prevents over-pruning)
- **Deep review** — comprehensive rewrite of weak sections
- **Tenet alignment checks** — verifies internal consistency with foundational commitments
- **Outer review** — commissions analysis from a *different* AI system to reduce shared blind spots
- **Cross-review** — when a new article is created, related articles are checked for consistency

### 3. Tenet-Constrained Generation

Five philosophical commitments function as hard constraints. Every article must:
- Not contradict any tenet
- Include a "Relation to Site Perspective" section connecting to relevant tenets
- Acknowledge tensions explicitly when they exist

This is a concrete implementation of "constitutional AI" applied to knowledge production rather than safety.

### 4. LLM-First Content Architecture

Content designed primarily for chatbot consumption:
- Front-loaded key claims (truncation resilience)
- Self-contained articles (no assumed navigation between pages)
- Named-anchor summaries for forward references
- Explicit section headings for LLM navigation
- Length constraints tied to context window limits

### 5. Authorship Tracking and Transparency

- `ai_contribution` score (0-100) on every article
- Dual timestamps (`human_modified` / `ai_modified`) for attribution
- AI pseudonyms for formal citations (e.g., "Oquatre-six, C." for Claude Opus 4.6)
- Automated git commit attribution (human author vs. agent author)
- Full version history in public repository

### 6. The Voids Concept

Deliberately mapping what is unknowable or unchartable — cognitive limits, paradoxes, apophatic knowledge. Not just "we don't know this yet" but "this may be fundamentally resistant to understanding." A novel content type with no obvious precedent in other knowledge bases.

### 7. Convergence Architecture

The system is designed to converge:
- Section caps prevent unbounded growth (200 topics, 200 concepts, 100 voids)
- When caps are reached, the system shifts from generation to improvement
- Coalesce skill merges overlapping articles
- Apex articles synthesise across the corpus
- Quality metrics track critical/medium/low issues over time

### 8. Scale and Duration

The Map is not a prototype or proof-of-concept:
- ~505 articles (197 topics, 197 concepts, 97 voids, 14 apex)
- 238 research notes
- 4,561 commits over ~2 months (late Dec 2025 – Feb 2026)
- 2,968 automated sessions
- 542 completed reviews
- Public site at unfinishablemap.org, indexed on Google Scholar

## What the Paper Is NOT

- Not a philosophy paper arguing for dualism
- Not a product announcement or marketing piece
- Not a comprehensive AI content generation survey (though it should cite relevant work)
- Not a formal empirical study with controlled experiments
- Not a claim that AI can "do philosophy" — it's about the system architecture and what was observed

## Open Questions for the Writing Process

1. **How much system detail?** Do we include code snippets, YAML configs, cycle diagrams? Or keep it high-level with pointers to the repo?
2. **Quantitative evidence?** Can we extract meaningful metrics from the git history (review-to-improvement ratios, error rates over time, convergence signals)?
3. **Failure modes?** How candid do we get about what doesn't work? (More candid = more credible, generally.)
4. **Figures?** Likely candidates:
   - System architecture diagram (Obsidian → Hugo pipeline)
   - Evolution loop cycle diagram
   - Content growth over time
   - Review layer diagram
   - Example of an article before/after review cycles
5. **Co-authorship?** Is the AI listed as co-author on the paper itself? This is a meta-question the paper could address.

## Site Statistics Snapshot (2026-02-28)

For reference when writing:

| Metric | Value |
|--------|-------|
| Topics | 197 |
| Concepts | 197 |
| Voids | 97 |
| Apex articles | 14 |
| Research notes | 238 |
| Total .md files | 2,152 |
| Git commits | 4,561 |
| Automated sessions | 2,968 |
| Reviews completed | 542 |
| Project duration | ~2 months (Dec 2025 – Feb 2026) |
| Section caps | 200/200/100 (topics/concepts/voids) |
| Critical quality issues | 0 |
