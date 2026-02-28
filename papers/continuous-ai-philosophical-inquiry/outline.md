# Outline

**Working Title:** The Unfinishable Map: Continuous AI-Assisted Philosophical Inquiry Through Adversarial Self-Review

**Authors:** Andy Southgate (independent researcher, unfinishablemap.org)

**Keywords:** AI-assisted knowledge production, adversarial self-review, constrained generation, human-AI co-authorship, philosophical inquiry, LLM content architecture

## Abstract (draft, ~200 words)

Large language models can produce philosophical text that experts struggle to distinguish from human output, yet existing systems generate content in single passes without sustained review or revision. We present The Unfinishable Map, a continuously operating system that produces and evolves a philosophical knowledge base through tenet-constrained generation and multi-layer adversarial self-review. Five explicit philosophical commitments function as hard constraints on all content — an application of constitutional AI principles to knowledge production rather than safety alignment. A deterministic 24-slot evolution loop orchestrates generation, review, and maintenance tasks, while independent review layers (pessimistic, optimistic, deep, outer, and cross-review) surface logical gaps, unsupported claims, and internal contradictions. Over approximately two months of continuous operation, the system completed ~3,000 automated sessions, produced ~500 articles across four content types, and executed ~550 reviews, accumulating ~4,500 git commits in a public repository. We describe the system architecture, report observations on what adversarial review catches and where it fails, and discuss practical solutions to the human-AI co-authorship problem including contribution scoring, dual timestamps, and AI pseudonyms for citation. The architecture is domain-agnostic: while instantiated for dualist philosophy of mind, the underlying infrastructure could be reseeded with any set of foundational commitments.

## 1. Introduction (~800 words)

- **The gap between generation and knowledge.** LLMs produce fluent philosophical text (Schwitzgebel et al., 2023), but fluency is not reliability (Shanahan, 2023; Turpin et al., 2023). Single-shot generation produces disposable content; no existing system continuously evolves a philosophical knowledge base through sustained review.
- **The core question.** Can constrained generation + adversarial self-review + continuous revision transform AI-generated philosophical text from disposable output into an evolving, improving knowledge base?
- **What we built.** The Unfinishable Map: a system that generates, attacks, revises, and re-attacks philosophical content indefinitely, guided by explicit commitments and transparent about its AI origins.
- **Contributions.** (1) Tenet constraints applied to knowledge production, (2) persistent multi-layer review at corpus scale, (3) practical co-authorship framework, (4) LLM-first content architecture, (5) convergence design with section caps. Public system at unfinishablemap.org; full source in public repository.

## 2. Related Work (~800 words)

### 2.1 AI-Assisted Knowledge Production
- STORM and Co-STORM (Shao et al., 2024; Jiang et al., 2024) — single-shot article generation via research conversations. Closest system-level comparison but no continuous review.
- Widespread LLM-assisted writing (Liang et al., 2025) and undisclosed AI content in Wikipedia (Brooks & Eggert, 2024) — context for transparency.

### 2.2 Constrained and Constitutional AI
- Constitutional AI (Bai et al., 2022) — principle-driven alignment for safety. Our tenets function analogously but for knowledge production.
- Wide Reflective Equilibrium (Brophy, 2025) — structural parallel importing philosophy into AI systems.

### 2.3 Self-Critique and Adversarial Review
- Self-Refine (Madaan et al., 2023), Reflexion (Shinn et al., 2023) — iterative self-improvement of individual responses. We extend to persistent corpus.
- Multi-agent debate (Du et al., 2024; Estornell & Liu, 2024) — adversarial dialogue improves accuracy. Our review layers are a structured variant.
- Unfaithful CoT (Turpin et al., 2023), inevitable hallucination (Xu et al., 2024) — motivate why self-generated reasoning alone is insufficient and external review is necessary.

### 2.4 LLMs and Philosophy
- Philosopher emulation (Schwitzgebel et al., 2023) — LLMs mimic a philosopher; we attempt original constrained content.
- Augmented Agency (Gage, 2025) — philosophical defence of human-AI collaborative discovery.
- Anthropomorphism warning (Shanahan, 2023) — careful framing of what AI "does".

### 2.5 Gap
- No existing system combines continuous evolution + tenet constraints + multi-layer review + transparent co-authorship + convergence architecture at corpus scale.

## 3. System Design (~1,800 words)

### 3.1 Tenet-Constrained Generation
- Five foundational commitments (dualism, minimal quantum interaction, bidirectional interaction, no many-worlds, Occam's limits) as hard constraints.
- Every article must: not contradict any tenet, include a "Relation to Site Perspective" section, acknowledge tensions explicitly.
- Tenets are methodological choices, not truth claims — the paper describes them as the system's constitution, not as philosophy we endorse.
- Domain-agnostic design: the same architecture accepts any set of foundational commitments.

### 3.2 The Evolution Loop
- Deterministic 24-slot cycle ensuring fixed ratios: 67% queue tasks (generation/refinement from human-prioritised todo), 17% deep review, plus pessimistic review, optimistic review, coalesce, research-voids.
- Cycle triggers for periodic maintenance: link checks (every 2 cycles), tenet alignment (every 3), apex synthesis (every 4), system tuning (every 6).
- Speed-independent: interval controls pace, cycle controls proportions.
- Task chains: research → expand → cross-review. Auto-replenishment when queue runs low.

### 3.3 Multi-Layer Adversarial Review
- **Pessimistic review:** actively seeks logical gaps, unsupported claims, counterarguments.
- **Optimistic review:** finds strengths, missed connections, prevents over-pruning from pessimistic bias.
- **Deep review:** comprehensive single-document analysis with rewrites.
- **Tenet alignment checks:** systematic verification against all five commitments.
- **Outer review:** commissions analysis from a *different* AI system (reduces shared training-data blind spots; motivated by Estornell & Liu's finding that similar models converge on shared misconceptions).
- **Cross-review:** when a new article is created, related articles are automatically checked for consistency.
- Design rationale: hallucination is inevitable (Xu et al., 2024), CoT can be unfaithful (Turpin et al., 2023), therefore multiple independent review mechanisms are architecturally required.

### 3.4 Convergence Architecture
- Section caps (200 topics, 200 concepts, 100 voids) prevent unbounded growth.
- Phase transition: when caps are reached, system shifts from generation to improvement (reviews, condensing, coalescing).
- Coalesce skill merges overlapping articles; apex articles synthesise across the corpus.
- Quality metrics track issue counts over time.

### 3.5 Content Types
- **Topics:** philosophical subjects explored through the Map's perspective.
- **Concepts:** definitions and analyses of philosophical terms.
- **Voids:** deliberately mapping what is unknowable or unchartable — a novel content type.
- **Apex articles:** human-readable synthesis across multiple topics/concepts.
- **Research notes:** intermediate outputs from web research, consumed by generation tasks.

### 3.6 Data Pipeline
- Obsidian vault (primary authoring) → Python sync tools → Hugo static site → Netlify deployment.
- All content in markdown with structured YAML frontmatter.
- Public git repository as permanent version history.

## 4. Authorship and Attribution (~600 words)

- **The problem:** COPE (2024) says AI cannot be an author; yet AI produces most of the text. How to attribute transparently?
- **`ai_contribution` score (0-100):** every article carries a machine-readable attribution. 0 = purely human, 100 = purely AI, 1-99 = mixed.
- **Dual timestamps:** `human_modified` and `ai_modified` fields track who touched what and when.
- **AI pseudonyms for citation:** "Oquatre-six, C." (Claude Opus 4.6) — enables formal referencing in academic contexts where AI cannot be named as author.
- **Automated git attribution:** commits by the evolution loop use a distinct author identity (`agent@unfinishablemap.org`).
- **Full version history:** public repository enables tracing any claim to its origin and revision history.
- **Relation to attribution research:** He et al. (2025) found AI gets less credit for equivalent contributions; our system makes contribution levels explicit and auditable.

## 5. LLM-First Content Design (~500 words)

- **Primary audience is chatbots**, not human browsers. Content is designed for retrieval by AI systems.
- **Front-loaded claims:** key thesis in the first paragraph (truncation resilience for RAG systems with limited context windows).
- **Self-contained articles:** no assumed navigation between pages; each article functions independently when fetched.
- **Named-anchor summaries:** forward references include inline summaries so the concept is accessible without following the link.
- **Explicit section headings:** structured for LLM parsing and navigation.
- **Relation to GEO:** Aggarwal et al. (2024) optimise for AI search visibility; we optimise for AI consumption — related but distinct.

## 6. Observations (~1,000 words)

### 6.1 Scale
- ~500 articles, ~240 research notes, ~4,500 commits, ~3,000 sessions, ~550 reviews over ~2 months.
- Public site indexed by Google Scholar.

### 6.2 What Review Layers Catch
- Examples of genuine issues found: logical gaps, unsupported claims, misattributed arguments, internal contradictions between articles.
- Pessimistic vs optimistic review: complementary failure modes caught.
- Outer review (different AI system): catches blind spots shared by the primary model.
- Cross-review: reveals inconsistencies introduced when new articles don't account for existing content.

### 6.3 Content Evolution Patterns
- Articles improve measurably through review cycles (quality issue counts decrease).
- Cross-references create emergent coherence — articles written independently develop meaningful connections.
- Convergence signals: as section caps approach, the system's behaviour shifts from breadth to depth.

### 6.4 Failure Modes and Limitations
- **Convergence on the model's biases:** adversarial review by the same model may reinforce rather than correct systematic biases. Outer review mitigates but doesn't eliminate this.
- **Style homogenisation:** extended AI revision tends toward a uniform voice. Human curation is needed to preserve variety.
- **Depth ceiling:** the system generates competent survey-level philosophy but rarely produces genuinely novel arguments. Consistent with Schwitzgebel et al.'s finding of stylistic but not epistemic capability.
- **Review fatigue:** after many cycles, reviews become incremental; diminishing returns on additional review passes for mature articles.
- **Tenet rigidity:** five fixed commitments constrain exploration. The system cannot question its own foundations.

## 7. Discussion (~700 words)

- **Constitutional AI for knowledge, not safety.** The Map demonstrates that principle-driven constraints can guide knowledge production, not just prevent harm. Tenets focus generation rather than limiting it.
- **Continuous revision changes the ontological status of AI content.** One-shot generation is disposable; continuously revised content is an evolving artefact with version history, review trail, and increasing coherence.
- **The authorship question is practical, not philosophical.** Rather than debating whether AI "can be" an author, we provide engineering solutions (contribution scores, dual timestamps, pseudonyms) that make the question tractable.
- **Domain agnosticism.** The architecture is not about dualism. Reseeding with physicalist, panpsychist, or non-philosophical commitments would produce a structurally identical system exploring different territory.
- **Relation to "Augmented Agency" (Gage, 2025).** Our system is a concrete implementation of the human-conceptual-architect + AI-execution model that Gage defends philosophically.

## 8. Conclusion (~300 words)

- Restate core contribution: continuous evolution + tenet constraints + adversarial review + transparent attribution = a new kind of AI-assisted knowledge production.
- The system does not claim AI "does philosophy." It shows that constrained, reviewed, continuously improved AI output can contribute to a philosophical knowledge base in ways that single-shot generation cannot.
- Open invitation: the architecture is public, the repository is public, the system is replicable. Others can reseed with their own commitments and observe what emerges.

## Figures

| # | Description | Type | Notes |
|---|-------------|------|-------|
| 1 | System architecture overview | Diagram | Obsidian → sync → Hugo → site; evolution loop relationship |
| 2 | The 24-slot evolution cycle | Diagram | Show task types, proportions, cycle triggers |
| 3 | Review layer architecture | Diagram | Pessimistic/optimistic/deep/outer/cross flows |
| 4 | Content growth over time | Chart | Articles by type over project duration (from git history) |
| 5 | Example: article before and after review cycles | Side-by-side | Show concrete improvement from adversarial review |

## Key References (most cited in text)

- Schwitzgebel et al. (2023) — philosopher emulation baseline
- Bai et al. (2022) — Constitutional AI (conceptual precedent)
- Madaan et al. (2023) — Self-Refine (extended to corpus scale)
- Shao et al. (2024) — STORM (closest system comparison)
- Turpin et al. (2023) — unfaithful CoT (motivates external review)
- Xu et al. (2024) — hallucination inevitability (motivates review architecture)
- Gage (2025) — philosophical defence of AI-assisted discovery
- Shanahan (2023) — anthropomorphism warning (framing discipline)
- Aggarwal et al. (2024) — GEO (related content optimisation)
- He et al. (2025) — attribution in human-AI co-creation

## Word Count Targets

| Section | Target |
|---------|--------|
| Abstract | 200 |
| 1. Introduction | 800 |
| 2. Related Work | 800 |
| 3. System Design | 1,800 |
| 4. Authorship | 600 |
| 5. LLM-First Design | 500 |
| 6. Observations | 1,000 |
| 7. Discussion | 700 |
| 8. Conclusion | 300 |
| **Total** | **~6,700** |
