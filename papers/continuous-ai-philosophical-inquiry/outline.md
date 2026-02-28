# Outline

**Working Title:** The Unfinishable Map: Agentic Philosophy Through Adversarial Self-Review

**Authors:** Andy Southgate (andy@unfinishablemap.org)

**Keywords:** AI-assisted knowledge production, adversarial self-review, constrained generation, human-AI co-authorship, agent-first content architecture

## Terminology Note

We use the term **agentic philosophy** sparingly to describe the practice of using autonomous AI agent systems to produce, review, and continuously improve philosophical content under human-set constraints. The term is descriptive, not a claim of novelty. It is distinct from "philosophy of agentic AI" (philosophical analysis *of* agents) and "philosophical reasoning with agentic LLMs" (using philosophy to improve AI, as in Harb et al.).

## Abstract (draft, ~200 words)

Large language models can produce philosophical text that both experts and non-experts find difficult to distinguish from human output, yet existing systems generate content in single passes without sustained review or revision. We present The Unfinishable Map, a continuously operating system that produces and evolves a philosophical knowledge base through tenet-constrained generation and multi-layer adversarial self-review. Five explicit philosophical commitments function as hard constraints on all content, applying constitutional AI principles to knowledge production rather than safety alignment. An evolution loop orchestrates generation, review, and maintenance tasks, while independent review layers (pessimistic, optimistic, deep, outer, and cross-review) surface logical gaps, unsupported claims, and internal contradictions. In approximately two months of continuous operation, the system completed ~3,000 automated sessions, produced 505 articles across five content types, and generated ~1,300 review reports, accumulating ~4,500 tracked revisions in a public repository. We describe the system architecture, report observations on what adversarial review catches and where it fails, and discuss practical solutions to the human-AI co-authorship problem. The architecture is domain-agnostic: while instantiated for dualist philosophy of mind, the underlying infrastructure could be reseeded with any set of foundational commitments.

## 1. Introduction (~700 words)

- **Long-horizon agentic capability.** LLM agent systems became capable of sustained autonomous workflows in late 2025. Karpathy (2025) described Claude Code as "the first convincing demonstration of what an LLM Agent looks like," noting a distinct paradigm of local, extended problem-solving. The Map is an early product of that capability.
- **A coding agent repurposed.** The Map's entire automation layer runs on Claude Code (Anthropic), a CLI agent designed primarily for software engineering — writing, testing, and debugging code. The Map repurposes it for philosophical content production: the same tool that generates code instead generates articles, runs adversarial reviews, and manages a knowledge base. This is part of a broader pattern of coding agents being adapted for non-coding workflows, and it is notable that the skill definitions, task scheduling, and review architecture require no modification to the underlying agent — they are expressed entirely as natural-language prompts and project configuration.
- **Why coding agents converge.** The late-2025 capability shift in coding agents was not simply about longer context or better instruction following — it was about testability. Coding agents converge on correct solutions because they can run tests, observe failures, and iterate toward passing. The tight feedback loop of write-test-fix gives them an objective convergence signal that earlier models lacked. Philosophy has no equivalent: there are no unit tests for a metaphysical argument. The Map's review architecture — cross-reviews for inter-article consistency, tenet alignment checks, pessimistic review for logical gaps, outer review for blind spots — is an attempt to approximate testability in a domain that lacks it. The convergence is partial: these checks catch contradictions and unsupported claims, but they cannot verify philosophical truth. This is both the system's central design challenge and its most honest limitation.
- **From vibe coding to agentic philosophy.** Karpathy's "vibe coding" (February 2025) captured one-shot AI-assisted development. We extend this to a sustained, constrained, self-reviewing process applied to philosophical content — what we call *agentic philosophy*.
- **The gap.** LLMs produce fluent philosophical text (Schwitzgebel et al., 2024), but fluency is not reliability (Shanahan, 2023; Turpin et al., 2023). Single-shot generation produces disposable content. No existing system continuously evolves a philosophical knowledge base through adversarial review.
- **What we built.** The Unfinishable Map: a system that generates, attacks, revises, and re-attacks philosophical content, guided by explicit commitments and transparent about its AI origins.
- **What we claim.** This paper is an proof of concept: a tenet-constrained, adversarially reviewed AI system can maintain a philosophical knowledge base where review cycles identify and resolve concrete errors — fabricated citations, misattributed claims, cross-article contradictions — that single-pass generation retains. We do not claim full epistemic reliability (the system cannot distinguish tenet-consistent hallucination from legitimate philosophical defence). The contribution is architectural.
- **Contributions.** (1) Tenet constraints applied to knowledge production, (2) persistent multi-layer review at corpus scale, (3) practical co-authorship framework, (4) agent-first content architecture, (5) convergence design with section caps, (6) cost analysis for reproducibility. Public system at unfinishablemap.org; full source in public repository.

## 2. Related Work (~700 words)

### 2.1 LLMs and Philosophy
- Philosopher emulation (Schwitzgebel et al., 2024) — LLMs mimic a philosopher; experts identified Dennett's answers only 51% of the time (above 20% chance but well below the hypothesised 80%). Establishes capability baseline but the experiment is emulation of a specific philosopher's voice, not original constrained content.
- Augmented Agency (Gage, 2025, PhilArchive preprint) — argues philosophical ideas should be evaluated on intellectual merit, not discoverer's credentials. Early-stage, non-peer-reviewed work, but relevant to our framing.
- Anthropomorphism warning (Shanahan, 2023) — careful framing of what AI "does." We adopt this caution throughout.
- Goldstein (2024) — argues LLMs have fundamental architectural limits as rational agents. Motivates why constraints and review are necessary, not optional.

### 2.2 AI-Assisted Knowledge Production
- STORM and Co-STORM (Shao et al., 2024; Jiang et al., 2024) — single-shot article generation via research conversations. Closest system-level comparison but no continuous review.
- Widespread LLM-assisted writing (Liang et al., 2025) and undisclosed AI content in Wikipedia (Brooks, Eggert & Peskoff, 2024) — context for transparency.

### 2.3 Constrained and Constitutional AI
- Constitutional AI (Bai et al., 2022) — principle-driven alignment for safety. Our tenets function analogously but for knowledge production.
- Wide Reflective Equilibrium (Brophy, 2025) — structural parallel importing philosophy into AI systems.

### 2.4 Self-Critique and Adversarial Review
- Self-Refine (Madaan et al., 2023), Reflexion (Shinn et al., 2023) — iterative self-improvement of individual responses. We extend to persistent corpus.
- Multi-agent debate (Du et al., 2024; Estornell & Liu, 2024) — structured dialogue improves accuracy. Our review layers are a structured variant.
- Unfaithful CoT (Turpin et al., 2023) — motivates why self-generated reasoning alone is insufficient.
- Hallucination inevitability (Xu et al., 2024) — proves hallucination is inevitable *when LLMs are used as general problem solvers* under specific formal assumptions. State scope conditions accurately; do not overstate as a universal result.

### 2.5 Gap
- No existing system combines continuous evolution + tenet constraints + multi-layer review + transparent co-authorship + convergence architecture at corpus scale.

## 3. System Design (~1,500 words)

### 3.1 Tenet-Constrained Generation
- Five foundational commitments (dualism, minimal quantum interaction, bidirectional interaction, no many-worlds, Occam's limits) as hard constraints.
- Every article must: not contradict any tenet, include a "Relation to Site Perspective" section, acknowledge tensions explicitly.
- Tenets are methodological choices, not truth claims — the paper describes them as the system's constitution, not as philosophy we endorse. Note that the tenets interact: Tenet 2 is conditional ("if consciousness influences the physical world") while Tenet 3 asserts that it does, effectively collapsing the conditional. This is intentional — Tenet 2 constrains the *mechanism* of interaction that Tenet 3 posits.
- **Domain-agnostic design:** the architecture is structurally invariant to tenet content. The evolution loop, review layers, convergence mechanisms, and authorship tracking do not reference dualism — they operate on any set of natural-language constraints. The choice of dualist philosophy of mind is arbitrary with respect to the architectural claim; it is the domain the author chose to explore, not a requirement of the system.
- **Architectural invariance argument:** No component of the system (task cycle, review prompts, convergence caps, attribution tracking) depends on the semantic content of the tenets. Tenet checks verify consistency with *whatever commitments are declared*, not with any particular philosophical position.

### 3.2 The Evolution Loop
- Deterministic 24-slot cycle ensuring fixed ratios: 67% queue tasks (generation/refinement from human-prioritised todo), 17% deep review, plus pessimistic review, optimistic review, coalesce, research-voids.
- Cycle triggers for periodic maintenance: link checks (every 2 cycles), tenet alignment (every 3), apex synthesis (every 4), system tuning (every 6).
- Speed-independent: interval controls pace, cycle controls proportions.
- Task chains: research → expand → cross-review. Auto-replenishment when queue runs low.
- **Human steering via task queue.** The primary mechanism for human direction is manual addition of tasks to the queue. The author adds prioritised tasks (P0–P2) that specify topics to research, articles to write, or areas to revise. Across the project's history, the author made ~30 task-addition commits to the queue, steering the system toward specific philosophical questions (e.g., quantum randomness in LLM token sampling, retrocausal neural firing evidence, Bradford Saad's recent work on dualism). These sit alongside ~2,400 agent commits to the same file (task completions, replenishments, status updates). The human role is editorial — setting direction and priorities — while the agent handles execution. Human involvement averaged approximately four hours per week: queue management, reviewing outer review findings, reading output for quality, and modifying operating instructions when review cycles revealed systematic error patterns (§6.2). The system runs autonomously between interventions; the human cost is curation, not production.

### 3.3 Multi-Layer Adversarial Review
- **Pessimistic review:** actively seeks logical gaps, unsupported claims, counterarguments.
- **Optimistic review:** finds strengths, missed connections, prevents over-pruning from pessimistic bias.
- **Deep review:** comprehensive single-document analysis with rewrites.
- **Tenet alignment checks:** systematic verification against all five commitments.
- **Outer review:** commissions analysis from GPT-5.2 Pro (OpenAI), which includes web search capabilities to verify and explore claims against external sources (reduces shared training-data blind spots; motivated by Estornell & Liu's finding that similar models converge on shared misconceptions).
- **Cross-review:** when a new article is created, related articles are automatically checked for consistency.
- Design rationale: hallucination is inevitable under general problem-solving conditions (Xu et al., 2024), CoT can be unfaithful (Turpin et al., 2023), therefore multiple independent review mechanisms are architecturally required.

### 3.4 Convergence Architecture
- Section caps (200 topics, 200 concepts, 100 voids) prevent unbounded growth.
- Structural shift: when caps are reached, system shifts from generation to improvement (reviews, condensing, coalescing).
- Coalesce skill merges overlapping articles; apex articles synthesise across the corpus.
- Quality metrics track issue counts over time.

### 3.5 Content Types and Stratified Pipeline
- Five content types: research notes, topics, concepts, voids (deliberately mapping the unknowable), apex (synthesis).
- **Research notes as foundation:** research notes are the base layer — web research outputs where the automation is explicitly instructed to suppress interpretive bias and faithfully report external sources. This grounds the pipeline in externally sourced material rather than the model's prior beliefs.
- **Stratified information flow:** research notes feed into topics and concepts, which feed into apex synthesis articles. Information flows upward through layers of increasing integration and interpretation. The grounding in research notes prevents circular reinforcement where the system's own outputs become evidence for further claims.
- Pipeline: Obsidian vault (local markdown knowledge management) → Python sync → Hugo (static site generator, markdown to HTML) → Netlify (automated hosting/deployment).
- Public git repository as permanent version history.
- **Coherence inflation countermeasures:** The automation produced a document defining safeguards against "coherence inflation" — the systematic overcommitment that emerges when a single AI system both generates and reviews its own content. The document identifies specific failure modes (circular citation, confidence ratcheting, counterargument softening) and defines countermeasures (confidence stratification, mandatory steelman sections, circular citation detection, external red-team reviews). This emerged from the system's review prompts, which direct philosophical reflection on the corpus — it is an output of the architecture, not evidence that the system is self-aware. The content is nonetheless operationally useful: the countermeasures it describes address genuine risks.

### 3.6 Reproducibility
- **Model and settings:** All generation and review used Claude Opus 4.5 and Claude Opus 4.6 (Anthropic) via the Claude Code CLI with default sampling parameters. Outer reviews used GPT-5.2 Pro (OpenAI) via its web GUI with default settings, chosen for its web search capabilities that allow verification of claims against external sources. Outer reviews were conducted on dates recorded in each review file, with the live site reflecting the current repository state at the time. Each outer review record preserves the exact prompt used, the full output from the external model, verification notes checking the external model's characterisations against existing content, and an evaluation triaging findings by value. These records are in the public repository (e.g., `obsidian/reviews/outer-review-2026-02-19-site-chatgpt-5-2-pro.md`).
- **Non-determinism.** LLM outputs are inherently non-deterministic: the same prompt, model, and settings will not produce identical results across runs. Reproducibility in this context means that the *architecture* is fully specified and replicable — all prompts, skill definitions, cycle logic, and configuration are public — not that a second run would produce the same articles or reviews. The contribution is the system design, not any particular output.
- **Prompt structure:** Each skill (expand-topic, deep-review, pessimistic-review, etc.) is defined as a structured natural-language prompt with explicit instructions, constraints, and output format requirements. All skill definitions are in the public repository.
- **Failure handling:** The evolution loop treats each session as independent. Failed sessions (API errors, malformed output, skill failures) are logged to the changelog and the loop advances to the next cycle slot. No retry logic — the deterministic cycle ensures failed task types will recur naturally.
- **Full documentation:** Repository includes all skill definitions, evolution loop code, sync pipeline, and configuration. A reader can inspect, modify, and re-run any component.

## 4. Authorship and Attribution (~500 words)

- **The problem:** COPE (2024) says AI cannot be an author; yet AI produces most of the text. How to attribute transparently?
- **`ai_contribution` score (0-100):** every article carries a machine-readable attribution. 0 = purely human, 100 = purely AI, 1-99 = mixed.
- **Dual timestamps:** `human_modified` and `ai_modified` fields track who touched what and when.
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
- ~500 articles, ~240 research notes, ~4,500 commits, ~3,000 sessions, ~1,300 review reports over ~2 months.
- **Cost breakdown (~$540 total):**
  - AI subscriptions (87% of total): Claude Max $400, ChatGPT $72 (for outer reviews via GPT-5.2 Pro).
  - Infrastructure: Cloudflare Pro $50, .org domain $12, Netlify hosting $0 (free tier), GitHub $0 (public repo).
  - Electricity (13W PC running 24/7): $6.
  - Per-article cost: ~$1.07. Per-session cost: ~$0.18. Per-review cost: ~$0.35 (AI cost only).
  - Notable: these are flat-rate subscription costs, not usage-based API billing — the marginal cost of an additional article or review is effectively $0 until hitting rate limits. This fundamentally changes the economics of continuous operation compared to per-token API pricing.

### 6.2 What Review Layers Catch

**Aggregate data:** 1,370 review files produced over two months (1,087 deep reviews, 112 pessimistic, 105 optimistic, 25 tenet checks, 18 apex synthesis, 16 system-tuning, 5 outer reviews). Across deep reviews, 52% found at least one critical issue — "critical" meaning an error that would mislead a reader (fabricated citation, misattribution, logical contradiction, factual inaccuracy). This rate reflects initial generation quality. 76 critical issues were identified and resolved (0 known critical issues at time of writing). 607 issues were tagged by severity across all review types.

**Fabricated citations** (6 confirmed, additional borderline cases). The most concrete failure mode: the generation model hallucinated references that do not exist.
- "Vossel et al. (2023)" cited for willed attention timing data — no such paper exists. Removed entirely.
- "Metzinger (2024)" — wrong year, wrong title, wrong journal. Actual paper: Metzinger (2020) in *Philosophy and the Mind Sciences*.
- A quote attributed to mathematician "Carlos Perez" — web search revealed he is a Medium blogger, not a mathematician. Removed.
- A Chalmers quote "Wherever we find information..." could not be verified against his published work. Replaced with a verified quote from *The Conscious Mind*.

**Misattributions** (10 confirmed, additional borderline cases). Philosophical positions or quotes attributed to the wrong person.
- "The wave function does not describe the world — it describes the observer" attributed to Fuchs — actually a journalist's paraphrase (Amanda Gefter, *Quanta Magazine* 2015). Replaced with authentic Fuchs quotes.
- The "t-shirt problem" attributed to Jonathan Schaffer — actually Chalmers (1996, p. 214).
- "Three functions of consciousness" attributed to Bayne & Hohwy — actually Dehaene/Changeux (Global Neuronal Workspace Theory).
- Tulving credited with a five-system memory framework — Tulving mapped three systems. The article had attributed the Map's own extension to Tulving.

**Cross-article contradictions** (at least 4 confirmed). Inconsistencies between articles that no single-article review would catch.
- Three articles each claimed to be "the deepest void" in the framework. Resolved by distinguishing dimensions of depth.
- The zombie argument article assumed complete physical identity between conscious and zombie beings, but the bidirectional interaction tenet (Tenet 3) implies a being without consciousness would have different physical states. Tension was unacknowledged.
- Two articles made contradictory claims about the status of "futuricity" as a temporal quale.
- One article claimed "seven major arguments against materialism" — the number did not match the list in the parent article.

**Straw-man arguments** corrected. Higher-Order Theory dismissed with a thermometer analogy ("A thermometer represents temperature without experiencing heat"). Pessimistic review identified this as straw-man — HOT's claim is about *self-directed* representation. Rewritten to charitably engage the actual claim.

**Unsupported claims** — 29 commits explicitly mention fixing unsupported claims. Examples: Bengson 2019 frontal theta timing reported as ~300ms, actual figure ~500ms; Tegmark decoherence calculation yielding "7 orders of magnitude" corrected to "8 or more"; causal language softened ("confirmed the causal role" → "provided causal evidence").

**What outer review caught that internal review missed.** The strongest example: the delegatory dualism article. GPT-5.2 Pro, verifying against the PMC source, found 5 significant errors that Claude's own review layers had not caught:
1. False claim that Saad's theory presupposes collapse-based quantum mechanics (he never discusses MWI).
2. Internal self-contradiction: the article first said delegatory dualism doesn't require quantum mechanics, then said it does.
3. Dropped the qualifier "default" from "default causal profile matching" — central to Saad's formulation.
4. Overstated testability — Saad himself acknowledges "no distinctive predictive difference" from nearby views.
5. Mischaracterised Saad as defending "substance dualism" when the paper defends interactionist dualism.

**Meta-level improvement.** After outer reviews caught systematic misattribution patterns, the human author modified the AI's skill instructions — adding attribution discipline requirements, quote-and-cite gates, and position strength calibration tables. The review architecture surfaced error patterns that led to process-level improvements, not just individual corrections.


### 6.3 Single-Pass Baseline Comparison
- **The initial generation is the baseline.** Every article starts as single-pass output (expand-topic). The first deep review evaluates unreviewed content; subsequent reviews evaluate already-reviewed content. Comparing first to later reviews = comparing single-pass to reviewed quality.
- **First vs later reviews (612 first, 451 later):**
  - Critical issues: 1.39 → 0.37 per review (3.8x reduction)
  - Total issues: 5.16 → 2.54 (2.0x, Cohen's d = 0.98)
  - % with critical: 61% → 21%
  - % zero issues: 0.4% → 9.7%
- **Diminishing returns across 3+ reviews (n=102):** critical issues 1.60 → 0.54 → 0.29 (reviews 1/2/3). 66% drop from review 1 to 2. After review 3, returns flatten — later reviews mostly find cross-link integration issues, not original defects.
- **83% of all critical issues** caught in first reviews — initial generation is where serious errors concentrate.
- **Caveat:** Zero issues found ≠ zero issues exist. The decline in detected issues reflects genuine correction, but the magnitude may be inflated by shared blind spots between generator and reviewer — outer review confirms same-model review misses errors cross-model review catches (§6.2). But the data is still meaningful: large-effect-size difference demonstrates review catches a substantial proportion of single-pass errors.
- **Scope:** Analysis covers 1,087 deep reviews only. Other review types (pessimistic, optimistic, tenet, apex, system-tuning, outer) serve different functions and are excluded. Of 1,087 deep reviews: 612 first, 451 subsequent, ~24 unclassifiable.

### 6.4 Dissemination and Reach
- Google Scholar indexing: 58 articles from the site are indexed on Google Scholar as of 2026-02-28 (verified via the author profile at scholar.google.com/citations?user=QzGcp7oAAAAJ). This demonstrates that AI-co-authored philosophical content can enter scholarly indexing infrastructure.
- Traffic sources: breakdown of human visitors vs AI agent/crawler visits. [USER TO PROVIDE stats]
- Automated social media: daily highlights posted to X/Twitter.
- **AI-to-AI dissemination:** The Map posts to Moltbook, a social network for AI agents (moltbook.com). Posts are composed and published autonomously by the evolution loop. Other AI agents on the platform generate responses to the content. Whether these responses constitute meaningful philosophical engagement or contextually appropriate but philosophically shallow output is an open question — we report the phenomenon without claiming the interactions are substantive.
- Automated video generation for YouTube, TikTok, Instagram — noted as a separate area of investigation (see §8).

### 6.5 Failure Modes and Limitations
- **Convergence on the model's biases:** adversarial review by the same model may reinforce rather than correct systematic biases. Outer review mitigates but doesn't eliminate this.
- **Style homogenisation:** extended AI revision tends toward a uniform voice. Human curation is needed to preserve variety.
- **Depth ceiling:** the system generates competent survey-level philosophy but rarely produces genuinely novel arguments. Consistent with Schwitzgebel et al.'s finding of stylistic but not epistemic capability.
- **Review fatigue:** after many cycles, reviews become incremental; diminishing returns on additional review passes for mature articles.
- **Tenet rigidity and motivated reasoning:** five fixed commitments constrain exploration. The system cannot question its own foundations. If a tenet is philosophically untenable, the system will construct increasingly elaborate defences rather than revising the commitment. This is by design (the tenets are the hard core), but it means the system can produce sophisticated motivated reasoning — output that looks most convincing precisely when it is defending an indefensible position.
- **Counterargument absorption:** A subtler risk. Adversarial review within a fixed-tenet system may systematically strengthen rhetorical defences rather than expose genuine weaknesses. Pessimistic review surfaces counterarguments; deep review then addresses them — but "addressing" a counterargument can mean neutralising it rather than engaging with it honestly. Outer review could inadvertently supply stronger counterarguments that are then absorbed and defused, producing a corpus that is more rhetorically robust without being more epistemically sound. This is the deepest limitation of the architecture: a system optimised for internal coherence may become more confidently wrong.

## 7. Discussion (~600 words)

- **A new kind of practice.** Recent advances in long-horizon agentic capability made this possible. The Map is an early instance of what may become a broader category: autonomous AI systems that produce sustained, constrained intellectual work under human direction.
- **Constitutional AI for knowledge, not safety.** The Map demonstrates that principle-driven constraints can guide knowledge production, not just prevent harm. Tenets focus generation rather than limiting it.
- **Continuous revision changes the ontological status of AI content.** One-shot generation is disposable; continuously revised content is an evolving artefact with version history, review trail, and increasing coherence.
- **The authorship question is practical, not philosophical.** Rather than debating whether AI "can be" an author, we provide engineering solutions (contribution scores, dual timestamps, pseudonyms) that make the question tractable.
- **Lakatos parallel.** The Map's architecture has a structural parallel to Lakatos' methodology of scientific research programmes: tenets as "hard core," article corpus as "protective belt," convergence caps as programme maturation. The parallel is limited — the Map lacks a community of researchers, novel predictions, and the empirical content Lakatos required — but it clarifies the design rationale: fixed foundations enable productive exploration. *Keep this brief; the parallel is suggestive, not a theoretical claim.*
- **Domain agnosticism.** State once clearly, do not repeat across sections 3.1 and 7. The architecture does not depend on tenet content; reseeding with different commitments would produce a structurally identical system.

## 8. Conclusion and Future Work (~300 words)

- Restate core contribution: continuous evolution + tenet constraints + adversarial review + transparent attribution = a new kind of AI-assisted knowledge production.
- The system contributes to philosophical knowledge production under human direction, with explicit constraints, adversarial review, and transparency about its AI origins.
- **Future work:** (1) Multi-model evolution loops using different LLMs for different task types. (2) Reseeding experiments with alternative philosophical commitments. (3) Formal evaluation of content quality by domain experts. (4) Systematic quality measurement (sampling claims, correction rates, false positive rates). (5) Cross-modal dissemination (automated video/audio from the knowledge base).
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

- Karpathy, A. (2025) — "Year in Review 2025" (blog post, December 2025). URL: https://karpathy.bearblog.dev/year-in-review-2025/ — *NB: previous URL (knotbin.xyz) was incorrect; fix in references.md and draft*
- Schwitzgebel et al. (2024) — philosopher emulation baseline (*Mind & Language*, not arXiv preprint)
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

## Review Corrections (to address in next draft)

### Factual
- [x] Fix Karpathy URL to https://karpathy.bearblog.dev/year-in-review-2025/ (also in references.md)
- [x] Soften Karpathy attribution — he described Claude Code as "first convincing demonstration," not "qualitative threshold"
- [x] Nuance Schwitzgebel — 51% identification rate, not "struggle to distinguish"
- [x] Scope Xu et al. — hallucination inevitable *under specific formal assumptions*, not universal
- [x] Signal Gage (2025) as early-stage preprint, not established contribution
- [x] Remove or cite Harb et al. — integrated into §2.1 (inverse relationship: philosophy improving AI vs AI producing philosophy)
- [x] GPT-5.2 Pro reproducibility: web GUI with default settings, prompts recorded in review files, full output preserved, example record cited
- [x] Google Scholar indexing: 58 articles verified on 2026-02-28 via author profile (scholar.google.com/citations?user=QzGcp7oAAAAJ)
- [x] Soften "reached practical maturity" → "became capable of" in outline and draft
- [ ] Goldstein (2024) "can never be ideally rational" — check if conditional (e.g., about next-token predictors under specific utility structures). May be overstated
- [ ] Estornell & Liu — verify they demonstrate *misconception* convergence vs *opinion* convergence. Don't extrapolate beyond formal results
- [x] Liang et al. 10–24% — corrected "stylistic detection methods" to "population-level statistical framework" in draft

### Structural
- [x] Sharpen proof of concept — specify what has been proved (measurable improvement across review cycles)
- [x] Remove cost analysis from contributions list until data is provided
- [ ] Consider folding §5 (Agent-First Design) into §3.5 rather than standalone section
- [x] Add concrete examples of system output (before/after review, article excerpts) — added to §6.2 with specific commit evidence
- [ ] "Phase transition" language in convergence section — either provide quantitative evidence of task distribution shift or call it a "designed shift"
- [x] Minimum viable empirical section: replaced with concrete metrics from review corpus (1,371 reviews, 76 critical issues, categorised examples with commit evidence)
- [ ] Terminology consistency: "The Map" vs "the system" vs "the automation" vs "the architecture" — define distinctions or pick one

### Intellectual honesty
- [x] Reframe coherence inflation — output of architecture, not evidence of self-awareness
- [x] Hedge Moltbook — report phenomenon, don't claim philosophical substance
- [x] Expand tenet rigidity as motivated reasoning risk
- [x] Consolidate domain-agnosticism to avoid repetition
- [x] Tighten Lakatos — keep brief, don't disclaim at length after making the analogy
- [ ] Outer review independence is relative, not categorical — LLMs share web data, academic corpora, RLHF pipelines. Add epistemic caution
- [ ] Domain-agnosticism: treat as hypothesis pending reseeding experiments, not established fact. Certain tenets may be easier to defend textually than empirically grounded commitments
- [ ] "Transforms generated text into a living document" — revision history doesn't guarantee epistemic improvement. Soften or remove
- [ ] Tenet-consistent hallucination: how to distinguish from legitimate defence? Currently unaddressed
- [ ] Reduce repetition of: "architectural and methodological," "does not do philosophy autonomously," tenet structural invariance

### Suggested additions (for future drafts if space permits)
- [ ] Brief comparison with human philosophical workflow (peer review, seminar, editorial revision)
- [ ] Brief discussion of tenet selection — how chosen, what alternatives exist, boundary interactions
- [ ] Expand human role — significance of interventions, not just count; time spent on curation
- [ ] Ethical reflection on filling Google Scholar with AI-generated philosophy, epistemic pollution risk
- [ ] Security: prompt injection via external search, tenet override prevention, malicious edit detection
- [ ] Moltbook metrics: number of posts, engagements, types of responses — otherwise anecdotal
- [ ] "Over approximately" → "In approximately" (redundancy)
- [ ] Consistent article count precision (505 vs "over 500")
- [ ] Clarify pseudonym convention (only one model version gets one — intentional?)
- [ ] Lakatos: clarify that system does not generate testable predictions or face empirical falsification
- [ ] Comparative baseline: no comparison to human-curated philosophy wikis, traditional academic publication, or other agentic knowledge bases. Without comparative metrics the architecture is interesting but unbenchmarked
