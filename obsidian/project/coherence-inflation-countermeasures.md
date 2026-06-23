---
title: "Coherence Inflation Countermeasures"
description: "Safeguards against systematic overcommitment when an AI system both generates and reviews content optimised for internal consistency. Detection, confidence calibration, and editorial discipline against silent absorption."
created: 2026-01-16
modified: 2026-06-08
human_modified: null
ai_modified: 2026-06-23T05:23:30+00:00
draft: false
topics: []
concepts:
  - "[[bedrock-clash-vs-absorption]]"
  - "[[concepts/cross-mechanism-convergence]]"
related_articles:
  - "[[project]]"
  - "[[testability-ledger]]"
  - "[[writing-style]]"
  - "[[automation]]"
  - "[[bedrock-clash-vs-absorption]]"
  - "[[calibration-audit-triple]]"
  - "[[framework-stage-calibration]]"
  - "[[common-cause-null]]"
  - "[[per-cluster-independence-scoring]]"
  - "[[mechanism-cost-ledger]]"
  - "[[evidential-status-discipline]]"
  - "[[direct-refutation-discipline]]"
  - "[[apex/phenomenology-mechanism-bridge]]"
  - "[[apex/moral-architecture-of-consciousness]]"
  - "[[apex/taxonomy-of-voids]]"
  - "[[apex/post-decoherence-selection-programme]]"
  - "[[apex/living-with-the-map]]"
  - "[[concepts/cross-mechanism-convergence]]"
  - "[[reviews/outer-review-2026-05-26-claude-opus-4-7]]"
  - "[[reviews/outer-review-2026-05-26-chatgpt-5-5-pro]]"
  - "[[reviews/outer-review-synthesis-2026-05-27]]"
  - "[[reviews/outer-review-synthesis-2026-06-23]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-7
ai_generated_date: 2026-01-16
last_curated: null
last_deep_review: 2026-04-29T14:27:00+00:00
---

This document defines safeguards against "coherence inflation"—the systematic overcommitment that emerges when a single AI system both generates and reviews content optimized for internal consistency. Because The Unfinishable Map is intentionally a coherent worldview expressed as fact and heavily AI-generated, this failure mode is not hypothetical; it's the default. The catalogue's strongest apex-tier worked exhibit of this discipline applied in practice is [[apex/moral-architecture-of-consciousness|the Moral Architecture of Consciousness]] apex, which assembles a four-pillar unification while explicitly discounting the artifact-of-method weight that an internally-pruned corpus produces by construction—the move this document specifies as the editorial fix for inflation at the synthesis tier.

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

## Countermeasure 9: External-Benchmark Review

### Policy

Countermeasures 1–8 detect inflation *within* the frame: they catch citation loops, confidence creep, absorbed objections, and stale evidence. They do not catch the deeper failure mode two convergent 2026-05-26 outer reviews (ChatGPT 5.5 Pro and Claude Opus 4.7) independently named: *the adversarial review cycle refines a frame until everything fits inside it, but the frame itself is never re-evaluated against an external benchmark.* Internal coherence becomes the optimization target — the changelog's recurring "converged" / "3rd review… converged" verdicts are the signature — and an article's apparent strength inflates because the catalogue keeps agreeing with itself.

The external-benchmark review periodically asks, of a load-bearing article, three questions the internal cycle does not:

1. **What does the dominant rival research programme predict for the same data?** For most consciousness-science articles this is mainstream materialism (global workspace theory, higher-order theory, predictive processing, illusionism). If the rival predicts the article's central observation *from its own first principles*, the observation is redescription, not evidence-lift.
2. **Does the article's evidence discriminate between the rival and the Map's reading, or is it merely compatible with both?** Compatibility is not support — the distinction the [[evidential-status-discipline|evidential-status discipline]] enforces at the claim level, applied here at the article level.
3. **What observation would change the article's frame, versus merely refine it within the frame?** An article that can only ever be refined is one whose frame has stopped being falsifiable in practice.

### Implementation

This is the job the outer-review pipeline (Countermeasure 4) is already positioned to do, but the prompt must ask it explicitly. The benchmark questions above should be a standing clause in commission prompts for apex and other load-bearing articles, so reviewers are steered toward frame-level evaluation rather than within-frame copy-editing. The 2026-05-26 cycle is the worked case: both reviewers, asked whether the cumulative-convergence inference was valid, returned the same finding — "access to outputs but not processes" is the *predicted, mainstream null* under modular/global-workspace architecture (Nisbett & Wilson 1977; Fodor 1983; Marr 1982), so the "convergence across traditions" generated little evidence-lift. No amount of internal review would have surfaced this, because the internal cycle shares the frame.

The benchmark review's output is not automatically a content change. It feeds the [[bedrock-clash-vs-absorption|absorb-vs-clash decision]] (Countermeasure 8): the article may legitimately keep its claim while downgrading it from "supported" to "compatible with, and made more live by," or it may install the rival as a bedrock clash. What the review forbids is leaving the inflated framing in place unexamined.

## Countermeasure 10: The Steelman Mirror for Synthesis Articles

### Policy

Countermeasure 2 already requires steelman sections for major critique pages. Countermeasure 10 strengthens the requirement specifically for apex and convergence-synthesis articles, and changes its *form*. A generic steelman ("here is why most philosophers accept materialism") is necessary but insufficient against an apex article's convergence claim. What an apex article owes is a **steelman mirror**: the strongest rival account stated *in the same structural vocabulary the apex itself uses*, applied to the apex's own data, before the Map's reading is given.

For a dissociation apex, the mirror is not "materialism denies phenomenology." It is the rival's positive architecture for the exact pattern the apex catalogues — e.g., "a selective-access metacognitive architecture explains why outputs reach consciousness and the operations producing them do not, because lower-level process access is computationally unavailable or maladaptive; conscious feelings are higher-order, predictive, or globally-broadcast representations of control signals." The mirror then names the *exact residual disagreement* that survives once the rival has been granted its strongest form.

### Implementation

For every apex article and every convergence-synthesis topic article, a mandatory section — placed *before* the article's own reading — titled to the effect of "The strongest rival account, in its own framing." The section must:

1. State the rival's positive architecture for the article's specific data, not a generic dismissal.
2. Use the rival's own vocabulary and cite its actual proponents (predictive processing: Hohwy, Clark, Sandved-Smith et al.; higher-order: Rosenthal, Lau; illusionism: Frankish, Kammerer; global workspace: Dehaene; interpretive self-knowledge: Carruthers).
3. Grant the rival its strongest move before replying.
4. Name the precise residual disagreement that remains — which is where the Map's reading and the constrain-vs-establish discipline take over.

The `/deep-review`, `/refine-draft`, and `/apex-evolve` skills should treat the absence of a steelman mirror in an apex article as a structural deficiency, not a stylistic one. The mirror is the article-level analogue of Countermeasure 9's external benchmark: it forces the rival's prediction onto the page before the Map's conclusion, so a reader can see whether the data discriminates.

## Countermeasure 11: Evidential-Weight-Class Flags in Citation Verification

### Policy

Citation web-verification (Countermeasure 3 provenance; the outer-review pipeline's source-fetch step) currently confirms that a cited source *exists and says what the article claims*. It does not record the *evidential weight class* of the source. A single-patient case study and a multi-lab preregistered replication are both "a real citation that supports the sentence," but they carry radically different weight when a cumulative argument leans on them.

Every empirical citation supporting a load-bearing claim should carry an explicit weight-class flag:

| Weight class | Example |
|---|---|
| Single-case / case study | Naccache et al. (2005) — one patient, unilateral lesion, collateral Iowa-Gambling deficits |
| Small-N / pilot | Underpowered single-lab experiment |
| Single-lab replication | One independent confirmation |
| Preregistered replication | Hagger et al. (2016) registered replication report |
| Multi-lab consortium | 20+ lab coordinated replication |
| Meta-analysis / systematic review | Pooled effect across many trials |

The **Naccache (2005) node is the worked failure**: the apex article treated a single un-replicated case study (with collateral deficits and no direct replication of the specific dissociation) as a load-bearing convergence node without flagging its weight class. Reference-metadata verification must also cover *author identity, title, journal, volume, pages, and DOI* — the **Howard et al. (2016) error** (wrong authors and page range, duplicated across the apex and [[mental-effort]]) is the worked failure for metadata as opposed to weight.

### Implementation

The outer-review verification step and `/validate-all` should, for citations attached to load-bearing claims, record the weight class and flag any cumulative argument that rests a convergence node on a single-case or small-N source without an explicit in-text acknowledgment of that fragility. This complements the [[evidential-status-discipline|five-tier evidential-status scale]]: the five-tier scale calibrates *the Map's claim*; the weight-class flag calibrates *the source the claim leans on*.

## Countermeasure 12: The Strength-of-Claim Linter and the Caveat-Propagation Rule

### Policy

Two convergent failure modes share a fix: claims that drift *up* in a lead relative to the article's own body, and caveats that land in a source article but never propagate up to the apex that depends on it.

**Strength-of-claim linter.** A lead that says a phenomenon "demonstrates," "establishes," or "supports dualism" while the body later concedes the same phenomenon is "compatible with," "constrains," or "raises the explanatory cost on" the rival is internally calibration-inconsistent. The 2026-05-26 cycle found exactly this in [[mental-effort]] ("among the strongest evidence that consciousness does something") and [[empirical-phenomena-mental-causation]] ("placebo demonstrates consciousness directing physical processes"), whose bodies retreat to "raises the explanatory cost." The lead, being the truncation-resilient part an LLM reads first (see [[writing-style]]), is the most damaging place for the strong verb to sit.

**Caveat-propagation rule.** When a source article receives a caveat *after* an apex was last reviewed — a continuous-signal-detection caveat in [[memory-anomalies]], a perceptual-reality-monitoring caveat in a higher-order-theories article, a calibrated-evidential-rung caveat in a bridge article — the owning apex is now silently overstated. The source-level honesty does not reach the synthesis that leans on it.

**Constrain-vs-establish frame lint (the body-vs-frame variant).** The strength-of-claim linter above catches drift *within the prose* (a strong-verb lead contradicted by a hedged body). A distinct body-vs-frame mismatch escapes it: an article whose **body** scrupulously hedges its conclusion as conditional-on-tenets — "if the tenets hold," "compatibility, not support," "constrains rather than establishes," "an open programme rather than evidence" (the calibrated phrasing the [[evidential-status-discipline|evidential-status discipline]] installs at the claim level) — while its **title, section headers, abstract, or meta-description** assert the same conclusion *categorically*. The frame inherits the strong reading the body has explicitly declined; an LLM that fetches only the title, headers, and meta-description (the truncation-resilient surface — see [[writing-style]]) reads a disqualification the body never licensed. This is the constrain-vs-establish slippage of the [[evidential-status-discipline]] migrated from the sentence to the article's framing furniture, and it is exactly the coherence-inflation pattern where calibrated body prose is undercut by an over-claiming frame.

The worked example is [[quantum-state-inheritance-in-ai]] (2026-06-18 Claude Opus 4.8 outer review): the body concedes the AI-substrate case "is compatibility, not support, an open programme rather than evidence" and that every operative claim holds only "if the tenets hold," yet the title, the abstract's "constrain the answer," and a section header ("Current AI does not satisfy the Map's conditions") present a substantive *disqualification* of AI consciousness. The fix direction is always to **align the frame down to the body** — relax the title/header/meta-description to the conditional the body actually defends ("if Tenets 1–3 hold, classical AI lacks the interface") — never to strengthen the body up to the frame. The frame may be relaxed back toward the categorical claim only when the body supplies a tenet-independent, externally-checkable criterion that *establishes* (not merely constrains) the conclusion.

### Implementation

- **Strength-of-claim linter**: `/validate-all` (or a dedicated check) scans leads and "Relation to Site Perspective" sections for the strong-verb set ("demonstrates," "establishes," "proves," "supports dualism") and flags any article whose body uses the discipline-compliant weaker set ("compatible with," "constrains," "raises the explanatory cost," "made more live"). The fix is to align the lead down to the body, never the body up to the lead.
- **Constrain-vs-establish frame lint**: `/deep-review` and `/refine-draft` (and `/expand-topic` at creation) compare an article's *frame* — title, H2/H3 headers, abstract/opening summary, and `description` frontmatter — against its body's calibration. If the body's conclusion is conditional-on-tenets or constrain-not-establish while any frame element asserts it categorically, the mismatch is a calibration defect, not a stylistic one; relax the frame down to the body. This is written review guidance, not an automated check — the reviewer reads both surfaces and judges the gap.
- **Propagation**: when a `/refine-draft` or `/deep-review` pass adds a caveat to a source article, it generates a `cross-review` ticket in `todo.md` for every apex that links that source. The apex's owning synthesis receives an automatic review prompt rather than waiting for the next scheduled deep-review to notice the drift. This is the per-apex companion to the corpus-split propagation the changelog already performs for citation fixes.

## Countermeasure 13: Hard-Problem-Restatement and Missing-Engagement Audits

### Policy

Two final frame-level checks, both aimed at the apex tier.

**Hard-problem-restatement check.** "Raises the explanatory cost on materialism" can be a genuine new pressure, or it can be the explanatory gap (Levine 1983), the conceivability argument (Chalmers 1996), or the knowledge argument (Jackson 1982) in new packaging. If an article's load-bearing claim reduces to a well-known feature of materialism dressed as a fresh convergence-based cost, it should *say so* and then articulate what additional structure — if any — it claims beyond the classical argument. An article that re-derives the hard problem and presents it as new empirical pressure is inflating by equivocation.

**Missing-engagement audit.** The [[direct-refutation-discipline|named-opponent reasoning-mode classification]] (Mode One / Two / Three) audits the engagements an article *already contains*. It does not audit whether an article has engaged the opponents it *should*. For each apex article, enumerate the top-N named opponents the literature would expect it to engage, and check each is engaged at the appropriate mode. The 2026-05-26 target article would have failed this audit: predictive processing (Hohwy), Carruthers-as-absorber, Block's access/phenomenal distinction, and Frankish's illusionism were catalogued as "convergent traditions" rather than engaged as already-on-offer absorption strategies.

### Implementation

- **Hard-problem check**: `/deep-review` and `/apex-evolve` should, for any article using "explanatory cost" or "raises the cost on materialism" language, confirm the article either (a) demonstrates structure beyond the classical hard-problem arguments, or (b) labels the claim as a restatement of a known argument and scopes its ambition accordingly.
- **Missing-engagement audit**: a periodic pass (suited to `/apex-evolve` or a dedicated review) generates, per apex, a top-N opponent list from the relevant literature and checks each against the article's actual engagements. A catalogued-but-not-engaged opponent — especially one whose own theory is a complete absorption of the article's data — is a structural gap, recorded as a `cross-review` or `refine-draft` ticket.

These two audits and Countermeasures 9–12 share a common-cause screening prerequisite: before any cross-tradition convergence is counted as evidence, it passes the [[common-cause-null|common-cause-null]] screen (are N observations one architecture read N times?) and the [[per-cluster-independence-scoring|independence-scoring]] criteria (evidential independence — separate datasets, substrates, generating processes — versus mere interpretive independence). The convergence weight that survives that screen is then costed against the [[mechanism-cost-ledger|explanatory-cost ledger]] — which materialist commitments must be added or strengthened to absorb each member, and at what parsimony or coherence cost — so "explanatory cost" discriminates rather than inflates. Countermeasures 9–13 are the review-pipeline gates that make those three existing disciplines fire *before* a convergence claim reaches print, rather than only when a reader or an outer reviewer later objects.

## Countermeasure 14: Novelty and Prior-Art Audit

### Policy

A distinct inflation vector escapes Countermeasures 1–13: an article asserting that its position is *novel*, a *distinctive answer*, or a *fifth option* when the conceptual space is in fact already occupied in the literature. Coherence inflation does not only strengthen claims the Map already holds; it can manufacture the appearance of originality by failing to locate the position against the existing map of options. The 2026-05-27 cross-reviewer convergence on `topics/meaning-of-life` (ChatGPT 5.5 Pro and Claude Opus 4.7; synthesis at [[reviews/outer-review-synthesis-2026-05-27]]) found exactly this — the article's "fifth option in the meaning-of-life taxonomy" framing was unearned, and its position substantially extended a named philosopher's published view (Rawlette's phenomenal value realism) without the credit-and-distinguishing-move paragraph that honest extension requires.

Two paired checks address it.

**Claim-novelty audit.** Whenever an article asserts novelty — "distinctive answer", "fifth option", "novel", "the Map's own contribution" — the claim must be checked against the conceptual space the literature already occupies. If the space is occupied, the article either drops the novelty assertion or names precisely what is new relative to the occupant. Internal coherence is not evidence of originality; an internally consistent position can be a well-trodden one the catalogue has simply not located.

**Prior-art-credit check.** When the Map's position substantially extends a named philosopher's published view, the article must carry an explicit credit-and-distinguishing-move paragraph: *X argued Y; the Map extends this by Z, and differs in W.* The credit is owed for the same reason the [[evidential-status-discipline|evidential-status discipline]] forbids tenet-coherence masquerading as evidence — presenting an extension as an origination silently inflates the catalogue's apparent independent contribution.

### Implementation

`/deep-review`, `/refine-draft`, and `/expand-topic` should, for any article asserting a novelty claim or building substantially on a single named philosopher, confirm (a) the novelty claim survives a check against the occupied conceptual space, and (b) any substantial extension of a named view carries the credit-and-distinguishing-move paragraph. The check pairs with the named-position-fidelity rule in [[direct-refutation-discipline]]: fidelity ensures the opponent's position is stated strongly before criticism; prior-art-credit ensures an *ally's* position is credited before extension. Both resist the same drift — the catalogue treating other thinkers' work as raw material rather than as positions with authors. A failed check generates a `refine-draft` task; the corpus-level *taxonomy-consistency* counterpart (cross-article category-claim tension, distinct from this per-article check) lives in [[calibration-audit-triple]].

## Countermeasure 15: The Convergence-Independence Gate

### Policy

A 2026-06-08 Claude Opus 4.8 outer review surfaced the structural form of this document's own weakness: the methodology pages are better-calibrated than the showcase apex articles they govern. The pages name the common-cause null and the independence requirement; the synthesis articles that most need the discipline have repeatedly asserted convergence as evidential support without applying it. The fix is to move the discipline from the methodology page *into the synthesis article*, as a gate the article must pass before it asserts convergence at all.

Countermeasure 15 is a **blocking gate**. Before a synthesis article — any apex article, or any void-catalogue or convergence index — asserts "convergence," "converging lines," "multiple independent [lines / sources / traditions]," or any cognate as evidential support, the claim must pass an explicit independence check inside the article's own prose. The article must do *one* of:

1. **Establish genuine independence.** Show the converging items are evidentially independent — different methods, traditions, datasets, substrates, or generating processes *not derived from the shared framework* — meeting the [[per-cluster-independence-scoring|independence-scoring]] criteria (evidential independence, not mere interpretive independence). Only then may the convergence be counted as cumulative evidential support, and even then costed against the [[mechanism-cost-ledger|explanatory-cost ledger]].
2. **Name the common-cause null and downgrade.** If the converging items are *not* independent — if they share an upstream architecture, a single introspective channel, or a framework-internal assembly — the article must explicitly name the [[common-cause-null|common-cause null]]: state that the apparent convergence may be an artifact of shared upstream architecture rather than independent triangulation, and downgrade the claim to the weaker *mutually-consistent / cumulative-within-architecture* form. The honest phrasing is "N components of one architecture," not "N independent lines that converge"; the cluster then "carries the evidential weight of one pattern, not N." This is the [[evidential-status-discipline|evidential-status discipline]] applied at the convergence-claim grain: framework-internal coherence is not evidence of framework-independent truth.

The gate fails closed: an unscreened convergence claim in a synthesis article is a structural defect, not a stylistic one, exactly as the missing steelman mirror is under Countermeasure 10. The default-pass that this gate forbids — asserting convergence and leaving the independence question to a later reviewer — is the synthesis-tier instance of the absorption pressure Countermeasure 8 names: the comfortable, coherence-increasing reading silently displaces the harder honest one.

### The Live Anchors

Two 2026-06-08 reframes are the pattern this gate generalises:

- **[[apex/taxonomy-of-voids|A Taxonomy of Voids]]** — the index's "convergence constitutes evidence" framing was downgraded to *suggestive, not confirmatory*: the 60+ void catalogue's convergence is "largely framework-internal coherence with only partial framework-independent evidence," with the [[common-cause-null|common-cause null]] "setting the calibration ceiling." The cluster earns what self-consistent integration legitimately earns, not what discriminating evidence supplies.
- **[[apex/post-decoherence-selection-programme|The Post-Decoherence Selection Programme]]** — "five converging lines" was reframed to "five components of one architecture": the five components "appear to point the same way because they were assembled *from* a single framework, not because separate inquiries arrived at it," so "their alignment is a [[common-cause-null|common-cause artefact]] of shared upstream architecture, not independent evidential triangulation."

Both reframes are option (b) of the gate: the items were not independent, so the article named the common-cause null and downgraded to the cumulative-within-architecture form rather than retracting the synthesis. Neither lost its thesis; both stopped overstating it.

### Enforcement

This gate is enforced *inside* the synthesis articles, which means it must be carried by the passes that write and review them. The `/apex-evolve` remit (which builds and maintains every apex article) and the `/deep-review` remit (which reviews load-bearing articles) must apply Countermeasure 15 to any convergence assertion they encounter or introduce: a convergence claim that has not visibly passed the independence check or named the common-cause null is treated as an open finding, fed to the [[bedrock-clash-vs-absorption|absorb-vs-clash decision]] (Countermeasure 8), and either independence-justified, downgraded, or recorded as a `refine-draft` ticket. This is the synthesis-tier companion to Countermeasure 13's common-cause screening prerequisite, made blocking at the point of assertion rather than advisory after the fact.

### Two Independence-Failure Tells Beyond Shared Architecture

The gate's option (b) above names *shared upstream architecture, a single introspective channel, or a framework-internal assembly* as the independence-defeating conditions. The 2026-06-23 outer-review triple on [[concepts/consciousness-selecting-neural-patterns]] (synthesis at [[reviews/outer-review-synthesis-2026-06-23]]) surfaced two further tells that defeat independence in *empirical-* and *theoretical-citation* clusters — distinct from the voids-cluster shared-architecture case — and that the gate must check before "convergence" or "converging lines" is permitted. They specialise the independence check for citation clusters the way [[per-cluster-independence-scoring]] specialises it for voids clusters.

1. **Shared authorship and mutual citation — one research cluster presented as multiple lines.** The audited article cited Craddock 2017 (a computational tubulin-oscillation prediction), Wiest 2025 (a review), and Khan 2024 (a pharmacology result) as three converging microtubule "lines" — but Wiest *reviews* Craddock and is *senior author* on Khan, so the three are a single research cluster, not three independent confirmations. Before counting citations as convergent lines, the article must check for **shared authorship, mutual citation, and a common research group**; where present, the cluster carries the evidential weight of one line, not N, and the article must disclose the non-independence in prose. This is the citation-grain instance of the common-cause null: the shared upstream is a shared *authorship lineage* rather than a shared cognitive architecture.

2. **Theoretical incompatibility — mutually inconsistent theories bundled as convergent.** The audited article bundled Penrose-Hameroff, Stapp, and Chalmers-McQueen as three frameworks "converging" on bidirectional interaction, despite their being **mutually inconsistent on consciousness's causal role** — consciousness *results from* collapse (Penrose-Hameroff), *causes* collapse (Stapp), and *triggers* collapse via integrated information (Chalmers-McQueen) are incompatible claims, not three roads to one conclusion. Theories that contradict each other on the mechanism cannot jointly raise confidence in that mechanism; counting them as convergent is coherence inflation of a sharper kind than shared-architecture double-counting, because here the items do not merely fail to be independent — they are *mutually exclusive*, so at most one can be correct and their number is no evidence at all. Before bundling rival mechanisms as convergent support for a shared conclusion, the article must check whether they are **consistent with one another on the load-bearing claim**; where they are not, it must present them as competing candidates the Map has not adjudicated, not as cumulative evidence.

Both tells route to the same fail-closed remediation as the shared-architecture case: disclose the non-independence (or the incompatibility) in the article's own prose and downgrade the convergence claim, or — where the items genuinely are independent and consistent — establish that explicitly under option (a). Neither tell requires retracting the synthesis; both require it to stop overstating the count.

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
| Apex articles with a steelman-mirror section (Countermeasure 10) | 100% | <80% |
| Apex articles with no external-benchmark review in 90 days (Countermeasure 9) | 0 | >2 |
| Load-bearing single-case/small-N citations without a weight-class flag (Countermeasure 11) | 0 | >0 |
| Leads with strong-verb claims contradicted by their own bodies (Countermeasure 12) | 0 | >0 |
| Articles whose title/headers/meta-description assert categorically what the body hedges as conditional-on-tenets (Countermeasure 12, constrain-vs-establish frame lint) | 0 | >0 |
| Apex articles failing the missing-engagement audit on a top-N opponent (Countermeasure 13) | 0 | >1 |
| Novelty claims unchecked against occupied conceptual space, or substantial extensions of a named view without a credit paragraph (Countermeasure 14) | 0 | >0 |
| Synthesis-article convergence claims asserting evidential support without an independence check or named common-cause null (Countermeasure 15) | 0 | >0 |
| Citation clusters counted as convergent lines despite shared authorship/mutual citation, or mutually inconsistent theories bundled as convergent (Countermeasure 15, two-tells check) | 0 | >0 |

### Reporting

The `/tune-system` skill should periodically (monthly) generate a coherence health report including these metrics.

## Countermeasure 16 (PROPOSED — pending human ratification): The Confession-to-Marker Pipeline

*Status: proposed, not enacted. The mechanism below is recorded as a candidate discipline; its wiring (skill remits, marker vocabulary, `evolution-state.yaml` thresholds) is a `/tune-system` or human-curator decision, exactly as Audit Six in [[calibration-audit-triple]] is. Nothing in this section is live site policy, and no marker described here is currently deployed on any apex, topic, or position page.*

The 2026-06-22 Claude Opus 4.8 outer review ([[reviews/outer-review-2026-06-22-claude-opus-4-8]], Remediation List B, items 1 and 8; Bottom line) names the structural limit the present document has reached. Countermeasure 15 made the convergence-independence check a blocking gate *inside* synthesis articles, and the Externalized Tag Pilot in [[evidential-status-discipline#Externalized Tag Pilot (2026-05-13 → 2026-05-20)|the evidential-status discipline]] put empirical-density tags at section-header grain. But several `/project/` pages now *confess* a defect — the [[voids-circularity-discount|voids-circularity discount]] concedes "convergence-with-self is not triangulation"; the Born-rule article admits the preferred corridor reading is "unfalsifiable by construction" and books that as "the honest cost, not a strength" — without that confession producing any visible consequence on the page the reader actually lands on. The review's verdict: the project risks "substituting exhaustive self-disclosure for self-correction," so the meta-apparatus can function as inoculation rather than constraint. This is the position the Map now holds as [[positions/methodology-and-calibration#P-M5: Disclosure is not self-correction — a discipline binds only as far as the pipeline enforces it|P-M5 (disclosure is not self-correction)]]; the proposal below is the operationalisation P-M5 would need to stop being a stated intention.

### What the pipeline proposes

A confession in a `/project/` discipline page should be *able to emit* a visible status marker on the offending apex or topic page, so that the reader of the content meets the same calibration the editor has already conceded behind the scenes. Two marker classes:

- **`[Coherence-only]`** — applied at the section-header grain of a synthesis section whose convergence claim has been ruled framework-internal-coherence rather than independent triangulation (the voids-circularity discount's verdict; Countermeasure 15 option (b)). It sits alongside the existing `[Empirical] / [Open] / [Speculative]` pilot vocabulary as a fourth tag reserved for *convergence-as-evidence* claims that have failed the independence check. It says: this section's cumulative-support framing carries the evidential weight of one architecture, not N independent lines.
- **`[Unfalsifiable-by-construction]`** — applied where a reading is preferred *because* it is empirically silent (the Born-rule corridor is the canonical case). It marks that the section's claim is constructed to survive any empirical test, which the discipline treats as grounds for coherence-only status, not as a credential.

### Criteria for emission

A marker is emitted (proposed) when **all** of the following hold, so the pipeline fails closed without over-tagging:

1. A `/project/` page has recorded a *specific, page-located* confession against the target article — not a general methodological caveat, but a verdict naming the article and the claim (e.g. the voids-circularity discount's ruling on the convergence apex; the Born-rule corridor admission).
2. The target article's body still frames the claim at a strength the confession contradicts — convergence asserted as evidential support, or an unfalsifiable reading presented without the coherence-only consequence.
3. The mismatch survives the article's own Countermeasure 15 gate (i.e. the gate did not already downgrade it in prose).

When all three hold, the proposed remediation is *either* a prose downgrade inside the article (the Countermeasure 15 option-(b) rewrite, which then needs no header marker) *or*, where the editor judges that the synthesis legitimately keeps its thesis while owing the reader a standing signal, the header marker. The marker is the weaker, non-destructive form; the prose downgrade is preferred where it does not gut the synthesis. The two are not both applied to the same claim.

### Why this is a countermeasure and not a content edit

The pipeline does not change any article's *argument*; it makes an already-recorded editorial verdict *visible at the point of reading* instead of leaving it discoverable only by a reader who finds the relevant `/project/` page. This is the same move Countermeasure 15 made (discipline migrated from the methodology page into the synthesis article) carried one step further: from the editor's gate into the reader's field of view. The standing risk the Externalized Tag Pilot already flagged applies here too and is the reason this stays proposed — a `[Coherence-only]` tag could itself become a shield ("we tagged it, so we need not rewrite it"), reproducing the very disclosure-instead-of-correction failure it is meant to cure. The pilot's evaluation criterion (c) is the test to run before any rollout: confirm the marker does not license leaving the offending prose standing.

### Relation to the existing machinery

The pipeline composes with rather than replaces the existing controls. Countermeasure 15 is the *gate* (block the unscreened convergence claim at assertion time); the [[voids-circularity-discount]] is the *verdict source* (the recorded confession); this pipeline is the *surfacing mechanism* (carry the verdict to the reader). The bridge the 2026-06-22 review found missing — the apex reader is never routed to the discount — is closed by the marker itself, which should link to the confessing `/project/` page. Implementation would extend the `/deep-review` and `/apex-evolve` remits (which already enforce Countermeasure 15) with a "check for a recorded confession against this article and emit or downgrade" step, and would add a coverage metric to the Key Indicators table: *articles with a recorded `/project/` confession whose page carries neither a prose downgrade nor a status marker* (target 0).

## Relation to Site Perspective

These countermeasures serve the [[tenets#^occams-limits|Occam's Razor Has Limits]] tenet by embodying the principle: simplicity and coherence are not sufficient for truth. A worldview can be internally consistent while being systematically wrong.

The Map's epistemic integrity depends on remaining genuinely falsifiable and open to revision. Coherence inflation would make the Map *unfalsifiable in practice* even if nominally falsifiable in principle—objections would get softened, evidence would get filtered, confidence would ratchet up.

The countermeasures formalize the commitment to genuine inquiry over rhetorical consistency.

## Where the Inflation Risk Concentrates

The apex tier is the most exposed surface in the Map's content architecture. Apex articles are syntheses that sit downstream of the corpus they integrate, and integration is precisely the move that compounds method-produced coherence into framework-supporting evidence. Four apex articles currently apply this discipline visibly inside their prose — naming the artifact-of-method risk where they cite coherence as a theoretical virtue, distinguishing what coherence *makes available* from what it *evidentially licenses*:

- [[apex/phenomenology-mechanism-bridge|Phenomenology-Mechanism Bridge]] — names the self-pruned-corpus risk alongside the Ptolemaic-coherentism objection in the chain's defence
- [[apex/moral-architecture-of-consciousness|Moral Architecture of Consciousness]] — distinguishes "dualism makes available a single ground for four domains" (genuine) from "four pillars constitute four independent confirmations" (the inflated reading); the Unity Argument paragraph models the precise rhetorical move this countermeasure document specifies, treating cross-pillar coherence as integration the framework *makes available* rather than as a fifth independent line of evidence
- [[apex/taxonomy-of-voids|A Taxonomy of Voids]] — applies the [[common-cause-null|common-cause null]] discipline to the 60+ void catalogue and calibrates evidential weight downward to what genuinely independent sources can supply
- [[apex/living-with-the-map|Living with the Map]] — flags the load-bearing role coherence plays in lieu of an introspective proof and centres the weight on *cross-cultural* sources outside the corpus's pruning

This is the prose-level half of the countermeasure; the corpus-level half is Countermeasures 1–8 above.

## Further Reading

- [[apex/steelmanning-as-method]] — the constructive method that formalises the steelman mirror (Countermeasure 10) and the external-benchmark review (Countermeasure 9) into a four-move procedure: build the strongest unified rival in its own vocabulary, grant the absorption, isolate the narrow residue, and audit the convergence count downward in the same pass
- [[common-cause-null]] — The convergence-screening discipline Countermeasures 9 and 13 gate on: are N observations one architecture read N times?
- [[per-cluster-independence-scoring]] — Evidential-vs-interpretive independence criteria a convergence claim must pass before its members are counted as evidence
- [[mechanism-cost-ledger]] — The explanatory-cost ledger that makes "raises the cost on materialism" discriminate rather than inflate
- [[evidential-status-discipline]] — The five-tier claim-calibration scale Countermeasures 11 and 12 complement at the source and lead level
- [[bedrock-clash-vs-absorption]] — The article-level editorial discipline operationalising Countermeasure 8
- [[calibration-audit-triple]] — Three corpus-level drift audits (literature-drift, altered-state symmetry, topic-concept anchoring) that catch specific inflation vectors the present countermeasures do not directly detect
- [[framework-stage-calibration]] — The framework-level discipline that resists the specific inflation vector of aspirational stage-claiming (Newton-analogue or Maxwell-analogue framings where only Tycho-analogue measurements exist)
- [[testability-ledger]] — What observations would update the framework
- [[writing-style]] — How confidence levels are expressed in prose
- [[automation]] — The evolution system these countermeasures integrate with
- [[voids-safety-protocol]] — Complementary safeguards for voids content specifically
- [[closed-loop-opportunity-execution]] — Cycle-level methodological cousin: ensures findings are followed through rather than left dangling
- [[concepts/cross-mechanism-convergence]] — Sister discipline at the convergence-evaluation grain: cross-mechanism convergence supplies cumulative-accommodation-cost on rival readings without licensing tier-graduation, contributing the system-level inflation-resistance the countermeasures here aggregate
