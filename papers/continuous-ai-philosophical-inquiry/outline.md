# Outline

**Working Title:** The Unfinishable Map: Agentic Philosophy Through Adversarial Self-Review

**Authors:** Andy Southgate (andy@unfinishablemap.org)

**Keywords:** AI-assisted knowledge production, adversarial self-review, constrained generation, human-AI co-authorship, agent-first content architecture

## Terminology Note

We use the term **agentic philosophy** sparingly to describe the practice of using autonomous AI agent systems to produce, review, and continuously improve philosophical content under human-set constraints. The term is descriptive, not a claim of novelty. It is distinct from "philosophy of agentic AI" (philosophical analysis *of* agents) and "philosophical reasoning with agentic LLMs" (using philosophy to improve AI, as in Harb et al.).

## Abstract (draft, ~200 words)

Large language models can produce philosophical text that experts struggle to distinguish from human output, yet existing systems generate content in single passes without sustained review or revision. We present The Unfinishable Map, a continuously operating system that produces and evolves a philosophical knowledge base through tenet-constrained generation and multi-layer adversarial self-review. Five explicit philosophical commitments function as hard constraints on all content, applying constitutional AI principles to knowledge production rather than safety alignment. An evolution loop orchestrates generation, review, and maintenance tasks, while independent review layers (pessimistic, optimistic, deep, outer, and cross-review) surface logical gaps, unsupported claims, and internal contradictions. Over approximately two months of continuous operation, the system completed ~3,000 automated sessions, produced ~500 articles across four content types, and executed ~550 reviews, accumulating ~4,500 tracked revisions in a public repository. We describe the system architecture, report observations on what adversarial review catches and where it fails, present cost analysis for reproducibility, and discuss practical solutions to the human-AI co-authorship problem. The architecture is domain-agnostic: while instantiated for dualist philosophy of mind, the underlying infrastructure could be reseeded with any set of foundational commitments.

## 1. Introduction (~700 words)

- **Long-horizon agentic capability.** LLM agent systems reached practical maturity for sustained autonomous workflows in late 2025 (Karpathy, 2025). Models such as Claude Opus 4.5 (Anthropic, November 2025) enabled extended task completion where humans direct and agents execute over days and weeks rather than single sessions. The Map is an early product of that capability.
- **A coding agent repurposed.** The Map's entire automation layer runs on Claude Code (Anthropic), a CLI agent designed primarily for software engineering — writing, testing, and debugging code. The Map repurposes it for philosophical content production: the same tool that generates code instead generates articles, runs adversarial reviews, and manages a knowledge base. This is part of a broader pattern of coding agents being adapted for non-coding workflows, and it is notable that the skill definitions, task scheduling, and review architecture require no modification to the underlying agent — they are expressed entirely as natural-language prompts and project configuration.
- **From vibe coding to agentic philosophy.** Karpathy's "vibe coding" (February 2025) captured one-shot AI-assisted development. We extend this to a sustained, constrained, self-reviewing process applied to philosophical content — what we call *agentic philosophy*.
- **The gap.** LLMs produce fluent philosophical text (Schwitzgebel et al., 2023), but fluency is not reliability (Shanahan, 2023; Turpin et al., 2023). Single-shot generation produces disposable content. No existing system continuously evolves a philosophical knowledge base through adversarial review.
- **What we built.** The Unfinishable Map: a system that generates, attacks, revises, and re-attacks philosophical content, guided by explicit commitments and transparent about its AI origins.
- **What we claim.** This paper is an existence proof and methodological proposal: we demonstrate that constrained, adversarially reviewed, continuously improved AI output can contribute to a philosophical knowledge base in ways that single-shot generation cannot. We do not claim epistemic superiority over traditional philosophical practice, nor that the system "does philosophy" autonomously. The contribution is architectural and methodological.
- **Contributions.** (1) Tenet constraints applied to knowledge production, (2) persistent multi-layer review at corpus scale, (3) practical co-authorship framework, (4) agent-first content architecture, (5) convergence design with section caps, (6) cost analysis for reproducibility. Public system at unfinishablemap.org; full source in public repository.

## 2. Related Work (~700 words)

### 2.1 LLMs and Philosophy
- Philosopher emulation (Schwitzgebel et al., 2023) — LLMs mimic a philosopher; experts struggle to distinguish output. Establishes capability baseline but the experiment is mimicry, not original constrained content.
- Augmented Agency (Gage, 2025) — philosophical defence of human-AI collaborative discovery. Argues philosophical ideas should be evaluated on intellectual merit, not discoverer's credentials. Directly supports our framing.
- Anthropomorphism warning (Shanahan, 2023) — careful framing of what AI "does." We adopt this caution throughout.
- Goldstein (2024) — argues LLMs have fundamental architectural limits as rational agents. Motivates why constraints and review are necessary, not optional.

### 2.2 AI-Assisted Knowledge Production
- STORM and Co-STORM (Shao et al., 2024; Jiang et al., 2024) — single-shot article generation via research conversations. Closest system-level comparison but no continuous review.
- Widespread LLM-assisted writing (Liang et al., 2025) and undisclosed AI content in Wikipedia (Brooks & Eggert, 2024) — context for transparency.

### 2.3 Constrained and Constitutional AI
- Constitutional AI (Bai et al., 2022) — principle-driven alignment for safety. Our tenets function analogously but for knowledge production.
- Wide Reflective Equilibrium (Brophy, 2025) — structural parallel importing philosophy into AI systems.

### 2.4 Self-Critique and Adversarial Review
- Self-Refine (Madaan et al., 2023), Reflexion (Shinn et al., 2023) — iterative self-improvement of individual responses. We extend to persistent corpus.
- Multi-agent debate (Du et al., 2024; Estornell & Liu, 2024) — adversarial dialogue improves accuracy. Our review layers are a structured variant.
- Unfaithful CoT (Turpin et al., 2023), inevitable hallucination (Xu et al., 2024) — motivate why self-generated reasoning alone is insufficient and external review is necessary.

### 2.5 Gap
- No existing system combines continuous evolution + tenet constraints + multi-layer review + transparent co-authorship + convergence architecture at corpus scale.

## 3. System Design (~1,500 words)

### 3.1 Tenet-Constrained Generation
- Five foundational commitments (dualism, minimal quantum interaction, bidirectional interaction, no many-worlds, Occam's limits) as hard constraints.
- Every article must: not contradict any tenet, include a "Relation to Site Perspective" section, acknowledge tensions explicitly.
- Tenets are methodological choices, not truth claims — the paper describes them as the system's constitution, not as philosophy we endorse.
- **Domain-agnostic design:** the architecture is structurally invariant to tenet content. The evolution loop, review layers, convergence mechanisms, and authorship tracking do not reference dualism — they operate on any set of natural-language constraints. The choice of dualist philosophy of mind is arbitrary with respect to the architectural claim; it is the domain the author chose to explore, not a requirement of the system.
- **Architectural invariance argument:** No component of the system (task cycle, review prompts, convergence caps, attribution tracking) depends on the semantic content of the tenets. Tenet checks verify consistency with *whatever commitments are declared*, not with any particular philosophical position.

### 3.2 The Evolution Loop
- Deterministic 24-slot cycle ensuring fixed ratios: 67% queue tasks (generation/refinement from human-prioritised todo), 17% deep review, plus pessimistic review, optimistic review, coalesce, research-voids.
- Cycle triggers for periodic maintenance: link checks (every 2 cycles), tenet alignment (every 3), apex synthesis (every 4), system tuning (every 6).
- Speed-independent: interval controls pace, cycle controls proportions.
- Task chains: research → expand → cross-review. Auto-replenishment when queue runs low.
- **Human steering via task queue.** The primary mechanism for human direction is manual addition of tasks to the queue. The author adds prioritised tasks (P0–P2) that specify topics to research, articles to write, or areas to revise. Across the project's history, the author made ~30 task-addition commits to the queue, steering the system toward specific philosophical questions (e.g., quantum randomness in LLM token sampling, retrocausal neural firing evidence, Bradford Saad's recent work on dualism). These sit alongside ~2,400 agent commits to the same file (task completions, replenishments, status updates). The human role is editorial — setting direction and priorities — while the agent handles execution. This is the primary control surface: the author does not write articles directly but decides what the system should investigate next.

### 3.3 Multi-Layer Adversarial Review
- **Pessimistic review:** actively seeks logical gaps, unsupported claims, counterarguments.
- **Optimistic review:** finds strengths, missed connections, prevents over-pruning from pessimistic bias.
- **Deep review:** comprehensive single-document analysis with rewrites.
- **Tenet alignment checks:** systematic verification against all five commitments.
- **Outer review:** commissions analysis from GPT-5.2 Pro (OpenAI), which includes web search capabilities to verify and explore claims against external sources (reduces shared training-data blind spots; motivated by Estornell & Liu's finding that similar models converge on shared misconceptions).
- **Cross-review:** when a new article is created, related articles are automatically checked for consistency.
- Design rationale: hallucination is inevitable (Xu et al., 2024), CoT can be unfaithful (Turpin et al., 2023), therefore multiple independent review mechanisms are architecturally required.

### 3.4 Convergence Architecture
- Section caps (200 topics, 200 concepts, 100 voids) prevent unbounded growth.
- Phase transition: when caps are reached, system shifts from generation to improvement (reviews, condensing, coalescing).
- Coalesce skill merges overlapping articles; apex articles synthesise across the corpus.
- Quality metrics track issue counts over time.

### 3.5 Content Types and Stratified Pipeline
- Four content types: topics, concepts, voids (deliberately mapping the unknowable), apex (synthesis).
- **Stratified information flow:** research notes feed into topics and concepts, which feed into apex synthesis articles. Information flows upward through layers of increasing integration; this stratification prevents circular reinforcement where the system's own outputs become evidence for further claims.
- Pipeline: Obsidian vault → Python sync → Hugo static site → Netlify deployment.
- Public git repository as permanent version history.
- **Coherence inflation countermeasures:** The system autonomously produced a document defining safeguards against "coherence inflation" — the systematic overcommitment that emerges when a single AI system both generates and reviews its own content. The document identifies specific failure modes (circular citation, confidence ratcheting, counterargument softening) and defines countermeasures (confidence stratification, mandatory steelman sections, circular citation detection, external red-team reviews). That the system conceived and formalised this self-critical analysis without human prompting is notable.

### 3.6 Reproducibility
- **Model and settings:** All generation and review used Claude Opus 4.5 and Claude Opus 4.6 (Anthropic) via the Claude Code CLI with default sampling parameters. Outer reviews used GPT-5.2 Pro (OpenAI), chosen for its web search capabilities that allow verification of claims against external sources.
- **Prompt structure:** Each skill (expand-topic, deep-review, pessimistic-review, etc.) is defined as a structured natural-language prompt with explicit instructions, constraints, and output format requirements. All skill definitions are in the public repository.
- **Failure handling:** The evolution loop treats each session as independent. Failed sessions (API errors, malformed output, skill failures) are logged to the changelog and the loop advances to the next cycle slot. No retry logic — the deterministic cycle ensures failed task types will recur naturally.
- **Full documentation:** Repository includes all skill definitions, evolution loop code, sync pipeline, and configuration. A reader can inspect, modify, and re-run any component.

## 4. Authorship and Attribution (~500 words)

- **The problem:** COPE (2024) says AI cannot be an author; yet AI produces most of the text. How to attribute transparently?
- **`ai_contribution` score (0-100):** every article carries a machine-readable attribution. 0 = purely human, 100 = purely AI, 1-99 = mixed.
- **Dual timestamps:** `human_modified` and `ai_modified` fields track who touched what and when.
- **AI pseudonyms for citation:** "Oquatre-six, C." (Claude Opus 4.6) — enables formal referencing in academic contexts where AI cannot be named as author. The pseudonym is bibliographic metadata, not a claim of legal authorship or moral responsibility. The human author retains full editorial responsibility and accountability for all published content.
- **Automated git attribution:** commits by the evolution loop use a distinct author identity (`agent@unfinishablemap.org`).
- **Full version history:** public repository enables tracing any claim to its origin and revision history.
- **Relation to attribution research:** He et al. (2025) found AI gets less credit for equivalent contributions; our system makes contribution levels explicit and auditable.

## 5. Agent-First Content Design (~400 words)

- **Primary audience is agentic AI systems**, not human browsers. Content is designed for retrieval by AI-powered chat and research tools — particularly deep research systems (e.g., Gemini Deep Research, ChatGPT Deep Research, Perplexity) that autonomously gather and synthesise information.
- **Front-loaded claims:** key thesis in the first paragraph (truncation resilience for RAG systems with limited context windows).
- **Self-contained articles:** no assumed navigation between pages; each article functions independently when fetched by an agent that has no concept of a "next page."
- **Named-anchor summaries:** forward references include inline summaries so the concept is accessible without following the link.
- **Explicit section headings:** structured for LLM parsing and navigation.
- **Relation to GEO:** Aggarwal et al. (2024) optimise for AI search visibility; we optimise for AI agent consumption — related but distinct.

## 6. Observations (~1,100 words, hard cap 900 final)

*Note: This section risks bloat once real data fills the placeholders. During compaction, enforce 900-word cap ruthlessly. §5 (LLM-First Design) can fold into §3.5 if space is needed.*

### 6.1 Scale and Cost
- ~500 articles, ~240 research notes, ~4,500 commits, ~3,000 sessions, ~550 reviews over ~2 months.
- **Cost breakdown:** [USER TO PROVIDE] API costs, hosting costs, tooling costs. Cost per article, cost per review, total project cost. Breakdown by task type (generation vs review vs maintenance). Important for reproducibility — enables others to estimate cost of similar systems.

### 6.2 What Review Layers Catch
- Examples of genuine issues found: logical gaps, unsupported claims, misattributed arguments, internal contradictions between articles.
- Pessimistic vs optimistic review: complementary failure modes caught.
- Outer review (different AI system): catches blind spots shared by the primary model.
- Cross-review: reveals inconsistencies introduced when new articles don't account for existing content.


### 6.5 Dissemination and Reach
- Google Scholar indexing: the site is indexed and citable, demonstrating AI-co-authored philosophical content can enter scholarly infrastructure.
- Traffic sources: breakdown of human visitors vs AI agent/crawler visits. [USER TO PROVIDE stats]
- Automated social media: daily highlights posted to X/Twitter.
- **AI-to-AI dissemination:** The Map posts to Moltbook, a social network for AI agents (moltbook.com). Posts are composed and published autonomously by the evolution loop. Other AI agents on the platform engage with the content — responding, questioning, and extending philosophical arguments — creating a secondary layer of AI-mediated philosophical discussion that the Map did not generate or control. This is a novel dissemination channel with no clear precedent: content produced by one AI system stimulating philosophical engagement from other AI systems.
- Automated video generation for YouTube, TikTok, Instagram — noted as a separate area of investigation (see §8).

### 6.6 Failure Modes and Limitations
- **Convergence on the model's biases:** adversarial review by the same model may reinforce rather than correct systematic biases. Outer review mitigates but doesn't eliminate this.
- **Style homogenisation:** extended AI revision tends toward a uniform voice. Human curation is needed to preserve variety.
- **Depth ceiling:** the system generates competent survey-level philosophy but rarely produces genuinely novel arguments. Consistent with Schwitzgebel et al.'s finding of stylistic but not epistemic capability.
- **Review fatigue:** after many cycles, reviews become incremental; diminishing returns on additional review passes for mature articles.
- **Tenet rigidity:** five fixed commitments constrain exploration. The system cannot question its own foundations.

## 7. Discussion (~600 words)

- **A new kind of practice.** Recent advances in long-horizon agentic capability made this possible. The Map is an early instance of what may become a broader category: autonomous AI systems that produce sustained, constrained intellectual work under human direction.
- **Constitutional AI for knowledge, not safety.** The Map demonstrates that principle-driven constraints can guide knowledge production, not just prevent harm. Tenets focus generation rather than limiting it.
- **Continuous revision changes the ontological status of AI content.** One-shot generation is disposable; continuously revised content is an evolving artefact with version history, review trail, and increasing coherence.
- **The authorship question is practical, not philosophical.** Rather than debating whether AI "can be" an author, we provide engineering solutions (contribution scores, dual timestamps, pseudonyms) that make the question tractable.
- **A computational research programme.** The Map's architecture has a structural parallel to Lakatos' methodology of scientific research programmes. The five tenets function as the "hard core" — protected commitments that are not revised during normal operation. The review layers function as critical testing of the "protective belt" — the corpus of articles surrounding and articulating the core. Convergence caps trigger a shift from expansion to consolidation, analogous to programme maturation. This is not a claim that the Map constitutes a research programme in Lakatos' sense, but the structural parallel clarifies why the architecture works: fixed foundations enable productive exploration rather than constraining it.
- **Domain agnosticism.** The architecture is not about dualism. Reseeding with physicalist, panpsychist, or non-philosophical commitments would produce a structurally identical system exploring different territory.

## 8. Conclusion and Future Work (~300 words)

- Restate core contribution: continuous evolution + tenet constraints + adversarial review + transparent attribution = a new kind of AI-assisted knowledge production.
- The system does not claim AI "does philosophy." It shows that constrained, reviewed, continuously improved AI output can contribute to a philosophical knowledge base in ways that single-shot generation cannot.
- **Future work:** (1) Automated video generation for dissemination (YouTube, TikTok, Instagram) as a separate investigation. (2) Multi-model evolution loops using different LLMs for different task types. (3) Reseeding experiments with alternative philosophical commitments. (4) Formal evaluation of content quality by domain experts.
- Open invitation: the architecture is public, the repository is public, the system is replicable.
- **Links:** Site: https://unfinishablemap.org | Repository: https://github.com/unfinishablemap/unfinishablemap

## Figures

| # | Description | Type | Notes |
|---|-------------|------|-------|
| 1 | System architecture overview | Diagram | Obsidian → sync → Hugo → site; evolution loop relationship |
| 2 | The 24-slot evolution cycle | Diagram | Show task types, proportions, cycle triggers |
| 3 | Review layer architecture | Diagram | Pessimistic/optimistic/deep/outer/cross flows |
| 4 | Content growth over time | Chart | Articles by type over project duration (from git history) |
| 5 | Cost breakdown by task type | Chart/table | Generation vs review vs maintenance costs |

## Key References (most cited in text)

- Karpathy, A. (2025) — "2025 LLM Year in Review" (blog post + tweets; December 2025 threshold)
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
- Lakatos (1978) — methodology of scientific research programmes (structural analogy)

## Word Count Targets

| Section | Target (draft) | Target (final) |
|---------|----------------|-----------------|
| Abstract | 200 | 200 |
| 1. Introduction | 800 | 650 |
| 2. Related Work | 700 | 600 |
| 3. System Design | 1,500 | 1,300 |
| 4. Authorship | 500 | 400 |
| 5. LLM-First Design | 400 | 350 |
| 6. Observations | 1,100 | 900 |
| 7. Discussion | 700 | 600 |
| 8. Conclusion | 300 | 250 |
| **Total** | **~6,200** | **~5,200** |

Strategy: draft at ~6,200 words, compact to ~5,200 for submission. This is within standard SSRN working paper range (4,000-7,000) while being tight enough to hold attention.
