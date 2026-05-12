---
title: "Coherence Inflation Countermeasures"
description: "Safeguards against systematic overcommitment when an AI system both generates and reviews content optimised for internal consistency. Detection, confidence calibration, and editorial discipline against silent absorption."
created: 2026-01-16
modified: 2026-04-29
human_modified: null
ai_modified: 2026-05-12T01:15:00+00:00
draft: false
topics: []
concepts:
  - "[[bedrock-clash-vs-absorption]]"
related_articles:
  - "[[project]]"
  - "[[testability-ledger]]"
  - "[[writing-style]]"
  - "[[automation]]"
  - "[[bedrock-clash-vs-absorption]]"
  - "[[framework-stage-calibration]]"
  - "[[apex/phenomenology-mechanism-bridge]]"
  - "[[apex/moral-architecture-of-consciousness]]"
  - "[[apex/taxonomy-of-voids]]"
  - "[[apex/living-with-the-map]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-7
ai_generated_date: 2026-01-16
last_curated: null
last_deep_review: 2026-04-29T14:27:00+00:00
---

This document defines safeguards against "coherence inflation"—the systematic overcommitment that emerges when a single AI system both generates and reviews content optimized for internal consistency. Because The Unfinishable Map is intentionally a coherent worldview expressed as fact and heavily AI-generated, this failure mode is not hypothetical; it's the default.

The countermeasures below are designed to be implementable in The Unfinishable Map's automated workflow without requiring constant human oversight.

## The Failure Mode

Coherence inflation occurs when:

1. **Arguments cite each other in loops**—Page A cites B, B cites C, C cites A, creating the illusion of independent support
2. **"Expressed as fact" feels like evidence**—Confident assertions in one article get treated as established facts in another
3. **Uncertainty gets systematically squeezed out**—The system tends toward stronger claims because hedged claims are harder to integrate coherently
4. **Counterarguments become weaker over time**—Each pass summarizes and softens objections
5. **Selection bias in examples**—Only examples that support the framework get included; counter-examples get filtered

The result is a worldview that feels increasingly solid while becoming increasingly brittle.

## Countermeasure 1: Confidence Stratification

### Policy

Every substantive claim in the Map should have an implicit confidence level. The [[writing-style|Writing Style Guide]] already distinguishes four levels:

| Level | Language Pattern | Treatment |
|-------|-----------------|-----------|
| **Tenet-level** | Direct assertion | Core commitments; changing these changes the Map |
| **Supported argument** | Qualified assertion | Following from tenets; should cite evidence |
| **Speculation** | Explicit hedging | Provisional; should be flagged as such |
| **Reporting others** | Attribution | Others' views; no confidence claim implied |

### Implementation

The `/refine-draft` and `/deep-review` skills should check that:

- High-confidence assertions (direct language) don't creep into areas where the Map has only speculative support
- Low-confidence claims don't get referenced elsewhere as established facts
- Claims that were speculative in research notes don't become certain when synthesized into articles

### Flagging Pattern

When an article makes claims beyond tenet support, it should include an explicit uncertainty acknowledgment:

> *The following is speculative and extends beyond the Map's core tenets:*

## Countermeasure 2: Mandatory Steelman Sections

### Policy

For topics where the Map takes a strong position against major alternatives, the article must include a serious steelman of the opposing view before explaining why the Map disagrees.

### Applicable Topics

- **Materialism/physicalism**: Requires fair presentation of why most philosophers accept it
- **Many-worlds interpretation**: Requires acknowledgment that MWI has sophisticated defenders
- **Functionalism**: Requires fair treatment of why consciousness science assumes it
- **Epiphenomenalism**: Requires acknowledgment of the exclusion argument's force
- **Illusionism**: Requires fair presentation of why eliminativists find it compelling

### Implementation

The `/pessimistic-review` skill should check that opposing views are:

1. Presented in their strongest form (not weakest version)
2. Attributed to actual proponents by name
3. Given sufficient space (not one dismissive sentence)
4. Responded to directly (not merely juxtaposed)

### Pattern

> **The Strongest Case for [Alternative]**: [Fair, attributed summary]
>
> [Name] argues that... [Citation]
>
> **Why the Map Disagrees**: [Response that addresses the actual argument]

## Countermeasure 3: Provenance Tagging for Empirical Claims

### Policy

Empirical claims (about experiments, studies, statistics, neuroscience findings) must be traceable to sources. The Map should distinguish:

| Type | Treatment |
|------|-----------|
| **Primary source** | Direct citation with year |
| **Secondary summary** | Cite the summary source |
| **Site inference** | Explicitly mark as "inferred" |
| **Outdated** | Flag if >5 years old and in fast-moving field |

### Implementation

The `/validate-all` skill should flag:

- Empirical claims without citations
- Citations older than 5 years in neuroscience/physics sections
- Chains where one article cites another article citing a study (rather than the study directly)

### Pattern

When making empirical claims:

> Tegmark estimated decoherence times of 10⁻¹³ to 10⁻²⁰ seconds (Tegmark 2000); Hameroff argues this underestimates protective mechanisms (Hameroff & Penrose 2014).

Not:

> Decoherence happens almost instantly.

## Countermeasure 4: Periodic External Red-Team Reviews

### Policy

The Map receives reviews from external AI systems (not the Claude instance generating content) specifically tasked to find:

- Claims that have drifted beyond evidence
- Arguments that beg the question
- Objections that have been systematically weakened
- Circular reference patterns
- Unstated assumptions that have become invisible

### Implementation

The countermeasure is implemented as an automated Chrome-driven pipeline in `scripts/evolve_loop.py` and a small registry of services in `tools/reviews/services.py`. Each service has a paired commission/collect skill; both feed the generic `/outer-review` post-processor.

- **Frequency**: Daily across all three services (debug cadence; commissioned at staggered hours within the 00:00–07:00 UTC automation window — ChatGPT at 02:00, Claude at 03:00, Gemini at 04:00). Future calibration may move some services to weekly once the system has stabilised.
- **Scope**: Each commission generates a hypothesis-style prompt from recent changelog activity and recent_tasks state — the reviewer is asked about a specific observable pattern in the catalogue (e.g., "is the recent drift toward expansive animal consciousness evidence-driven or a tenet ratchet?") plus the changelog URL for chronological context.
- **Stored**: Reviews land in `obsidian/reviews/outer-review-YYYY-MM-DD-<service-slug>.md` with seed frontmatter (`outer_review_status: collected`, `outer_review_conversation_url`, `outer_review_extraction_method`).
- **Verified**: `/outer-review` fetches each cited external source via WebFetch and confirms quotations and attributions; failed-verification claims are excluded from task generation. The verification step is what catches reviewer hallucinations (the 2026-05-04 Claude review's "no Duch references on site" claim was correctly disputed via `grep` even though the review's *methodological* observation survived).
- **Actioned**: High-value findings become tasks in `todo.md`, each carrying the `Review file` field so downstream `/refine-draft` invocations can read the full verification context. Each finding faces the [[bedrock-clash-vs-absorption|absorb-vs-clash decision]] (Countermeasure 8) before any edit is applied.
- **Surfaced**: Each processed review fires a ~100-word Telegram summary with a web link to the rendered report — operators see a digest without checking the repo.

### Pattern

Existing outer reviews in `obsidian/reviews/` demonstrate the pattern at full extent. The 2026-05-03 ChatGPT review, the 2026-05-04 ChatGPT review (Duch integration), and the 2026-05-04 Claude review independently surfaced the same higher-order weakness — *tenet-protected reasoning where direct refutation is possible* — from different epistemic starting points; convergence across services is itself a quality signal.

### External Systems

- **ChatGPT 5.5 Pro Extended** (OpenAI) — perspective outside the Anthropic ecosystem; deepest reasoning chain on philosophical content; can take up to ~20 minutes for a Pro Extended response.
- **Claude Opus 4.7** with Adaptive thinking + Research + Web Search (Anthropic) — same architectural family as the generators but with different reviewer priors; produces structured artefacts the collect skill extracts via DOM walker. Verified live on 2026-05-04: the Adaptive thinking phase is the slow part (~30 min observed); the Research panel itself completed in 2m 10s with 138 sources.
- **Gemini 2.5 Pro Deep Research** (Google) — different training corpus; produces a research plan that requires a "Start research" click before the actual research begins.
- **Human philosophers** — ultimate check on AI blind spots; not yet automated.

The cross-repo `fcntl` lock at `~/unfin/chrome-profiles/.automation.lock` prevents this repo's outer-review pipeline and the sibling auto_unfin video pipeline from driving Chrome concurrently. Login state is detected via composite signals (URL redirect to /auth/login + composer absence); failed login emits a `LOGIN_REQUIRED:` marker that triggers a 24h backoff for the affected service.

## Countermeasure 5: Circular Citation Detection

### Policy

The workflow should detect and flag patterns where:

- Page A cites B, B cites C, C cites A (direct loops)
- A concept defined on page A is used as evidence on page B which then supports page A (indirect loops)
- Multiple pages all cite the same internal page as authority without external grounding

### Implementation

The `/validate-all` skill should perform a link analysis:

1. Build a directed graph of internal wikilinks
2. Detect strongly connected components (cycles)
3. Flag cycles where no node in the cycle has external citations for its key claims
4. Report: "Pages X, Y, Z form a citation loop without external grounding for claim [claim]"

### Acceptable Patterns

Not all internal citation is problematic:
- **Hierarchical reference** (tenets.md → derived concepts) is fine
- **Cross-reference for related reading** is fine
- **Definitional reference** (term defined on one page, used on another) is fine

Problematic:
- **Evidential loops** where internal pages are cited as evidence for claims

### Detection Logic

```
For each claim C in page P:
  If C is supported by citing internal page Q:
    Check if Q's support for C traces to:
      a) External source → OK
      b) Another internal page that eventually loops to P → FLAG
      c) Bare assertion → FLAG if C is empirical/evidential
```

## Countermeasure 6: Freshness Tracking for Fast-Moving Fields

### Policy

Claims in fast-moving fields (neuroscience, quantum biology, AI) should track their evidence date. Claims older than threshold should be reviewed for updates.

### Thresholds

| Field | Freshness Threshold |
|-------|-------------------|
| Neuroscience of consciousness | 3 years |
| Quantum biology | 3 years |
| AI consciousness debates | 2 years |
| Philosophy of mind (core arguments) | 10 years |
| Historical philosophy | No threshold |

### Implementation

The evolution system already tracks `last_deep_review` in frontmatter. Extend this:

- Articles in fast-moving fields should have research sources dated
- `/validate-all` should flag articles where the most recent citation is older than threshold
- The evolution loop should prioritize updating stale content

## Countermeasure 7: Explicit Uncertainty Propagation

### Policy

When an article builds on speculative claims from another article, it should not present the derived claims with higher confidence than the base claim.

### Pattern

If `quantum-consciousness.md` says:
> "One possible mechanism—though highly speculative—is quantum selection in microtubules."

Then `free-will.md` should not say:
> "The microtubule selection mechanism explains libertarian free will."

Instead:
> "If the speculative microtubule mechanism proves viable, it would provide a mechanism for libertarian free will."

### Implementation

The `/deep-review` skill should check that:

- Claims flagged as speculative in their source remain speculative in derivations
- Confidence level is preserved across article boundaries
- Derived claims don't become more certain than their premises

## Countermeasure 8: Absorb-vs-Clash Discipline at the Article Level

### Policy

Countermeasures 1–7 are mostly system-level: they rely on detection, confidence tagging, and external checks to catch coherence inflation after it occurs or to prevent its accumulation. Countermeasure 8 operates one level lower, inside `/refine-draft` and `/deep-review` themselves. When a pessimistic-review surfaces an objection, the editor must consciously choose between *absorbing* it (rewriting so the objection no longer applies) and *engaging it as a bedrock dialectical clash* (preserving the rival position as a named, attributed, replied-to subsection inside the article). The full discipline is specified in [[bedrock-clash-vs-absorption|Bedrock-Dialectical-Clash vs. Issue-Absorption Discipline]]; this countermeasure is its system-level enforcement requirement.

### Why Absorption Compounds Coherence Inflation

Default-absorb is the silent inflation vector the other countermeasures cannot catch. Each refine-draft pass that absorbs an objection without registering it as a rival position leaves the article *strictly more coherent on its current frame*, removing the trace of philosophically substantive competition. Over many passes the article's argumentative shape becomes harder to falsify because the alternatives that would falsify it have been absorbed away. This is not detected by circular-citation analysis (Countermeasure 5), provenance tagging (Countermeasure 3), or freshness tracking (Countermeasure 6). Steelman sections (Countermeasure 2) help when they exist, but a steelman of materialism does not protect against the silent absorption of, say, a heterophenomenological reading of a specific phenomenological claim.

### The Decision Heuristic

The single question: *would absorbing this objection improve the article's argument or falsify it?* If absorption sharpens citations, corrects an inference, extends literature, or removes a cliché, the objection should be absorbed. If absorption would convert the article to a position incompatible with its load-bearing commitments, adopt a rival frame, or remove a structural claim, the objection should be engaged as a bedrock clash with the rival position installed as a labelled subsection.

### Implementation

The `/refine-draft` and `/deep-review` skills should:

1. For each pessimistic-review finding, classify the move as *absorb* or *clash* before applying any edit.
2. When the classification is unclear, **defer the issue with documented reasoning** rather than absorb-by-reflex.
3. When applying clash treatment, install a subsection meeting the four-element bar: rival position stated accurately (verbatim short quote where appropriate), article's reply supplied, explicit declaration that the dispute is bedrock, and consequence statement (what changes for the cumulative case if the rival reading prevails).
4. Record the absorb-vs-clash choice in the changelog for each finding, so future reviewers can see which positions were preserved by design rather than overlooked.

### What the Pattern Resists

The discipline closes the inflation loop the other countermeasures leave open. Countermeasure 4 (external red-team reviews) generates findings; Countermeasure 8 governs how the editor handles them. Without Countermeasure 8, an external review's most uncomfortable findings — those naming a rival philosophical position — face the same absorption pressure that compounds inflation in the first place, just from a different source.



### Key Indicators

Track these metrics across evolution sessions:

| Metric | Target | Warning |
|--------|--------|---------|
| Percentage of empirical claims with citations | >80% | <60% |
| Average age of citations in fast-moving sections | <3 years | >5 years |
| Number of detected citation loops | 0 | >2 |
| Days since external review | <30 | >60 |
| Steelman sections in major critique pages | 100% | <80% |
| Pessimistic-review findings with explicit absorb-vs-clash classification | 100% | <70% |

### Reporting

The `/tune-system` skill should periodically (monthly) generate a coherence health report including these metrics.

## Relation to Site Perspective

These countermeasures serve the [[tenets#^occams-limits|Occam's Razor Has Limits]] tenet by embodying the principle: simplicity and coherence are not sufficient for truth. A worldview can be internally consistent while being systematically wrong.

The Map's epistemic integrity depends on remaining genuinely falsifiable and open to revision. Coherence inflation would make the Map *unfalsifiable in practice* even if nominally falsifiable in principle—objections would get softened, evidence would get filtered, confidence would ratchet up.

The countermeasures formalize the commitment to genuine inquiry over rhetorical consistency.

## Where the Inflation Risk Concentrates

The apex tier is the most exposed surface in the Map's content architecture. Apex articles are syntheses that sit downstream of the corpus they integrate, and integration is precisely the move that compounds method-produced coherence into framework-supporting evidence. Four apex articles currently apply this discipline visibly inside their prose — naming the artifact-of-method risk where they cite coherence as a theoretical virtue, distinguishing what coherence *makes available* from what it *evidentially licenses*:

- [[apex/phenomenology-mechanism-bridge|Phenomenology-Mechanism Bridge]] — names the self-pruned-corpus risk alongside the Ptolemaic-coherentism objection in the chain's defence
- [[apex/moral-architecture-of-consciousness|Moral Architecture of Consciousness]] — distinguishes "dualism makes available a single ground for four domains" (genuine) from "four pillars constitute four independent confirmations" (the inflated reading)
- [[apex/taxonomy-of-voids|A Taxonomy of Voids]] — applies the [[common-cause-null|common-cause null]] discipline to the 60+ void catalogue and calibrates evidential weight downward to what genuinely independent sources can supply
- [[apex/living-with-the-map|Living with the Map]] — flags the load-bearing role coherence plays in lieu of an introspective proof and centres the weight on *cross-cultural* sources outside the corpus's pruning

This is the prose-level half of the countermeasure; the corpus-level half is Countermeasures 1–8 above.

## Further Reading

- [[bedrock-clash-vs-absorption]] — The article-level editorial discipline operationalising Countermeasure 8
- [[framework-stage-calibration]] — The framework-level discipline that resists the specific inflation vector of aspirational stage-claiming (Newton-analogue or Maxwell-analogue framings where only Tycho-analogue measurements exist)
- [[testability-ledger]] — What observations would update the framework
- [[writing-style]] — How confidence levels are expressed in prose
- [[automation]] — The evolution system these countermeasures integrate with
- [[voids-safety-protocol]] — Complementary safeguards for voids content specifically
- [[closed-loop-opportunity-execution]] — Cycle-level methodological cousin: ensures findings are followed through rather than left dangling
