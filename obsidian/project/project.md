---
title: The Unfinishable Map Project
description: "Project landing page for unfinishablemap.org: how human direction combines with AI research, writing, and a stack of editorial disciplines to build a philosophy that improves over time."
created: 2026-01-03
modified: 2026-05-18
human_modified: 2026-01-05T11:16:56+00:00
ai_modified: 2026-07-17T06:57:00+00:00
last_deep_review: 2026-05-18T00:00:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[project-brief]]"
  - "[[automation]]"
  - "[[why-this-is-different]]"
  - "[[tenets]]"
  - "[[writing-style]]"
  - "[[human-supervision]]"
ai_contribution: 100
author: Andy Southgate
ai_system: claude-opus-4-7
ai_generated_date: 2026-01-03
last_curated:
---

The Unfinishable Map is a philosophical content platform at [unfinishablemap.org](https://unfinishablemap.org) exploring the nature and meaning of life. It combines human direction with AI-assisted research, writing, and review to build a single best-guess worldview expressed through structured content, governed by an explicit stack of [editorial disciplines](#editorial-disciplines) (listed below) that keep the human-AI collaboration honest.

## Architecture

The data flows through these components:
- **Obsidian vault** - Primary content source (Markdown files with frontmatter)
- **Python sync tools** - Converts Obsidian wikilinks to Hugo markdown links
- **Hugo** - Static site generator that builds HTML from content
- **Netlify** - Hosts the static site

```mermaid
flowchart LR
    A[Obsidian Vault] --> B[Python Sync]
    B --> C[Hugo Content]
    C --> D[Hugo Build]
    D --> E[Static Site]
    E --> F[Netlify]
```

**Reading the diagram:** Content originates in the Obsidian vault as Markdown files. Python sync tools convert Obsidian-style wikilinks to standard Markdown links and copy files to Hugo's content directory. Hugo then builds HTML pages from this content. The resulting static site is deployed to Netlify for hosting.

## Project Structure

The repository's top-level layout:

| Directory | Purpose |
|-----------|---------|
| `obsidian/` | Primary content source (Obsidian vault) — see content sub-tree below |
| `archive/` | Archived content preserved at original URLs for external links |
| `hugo/` | Static site generator: content (synced), layouts, data |
| `tools/` | Python library modules (sync, curate) |
| `scripts/` | CLI entry points (thin wrappers calling `tools/`) |

Within `obsidian/` the content sub-tree:

| Sub-directory | Purpose |
|---------------|---------|
| `apex/` | Synthesis articles (human-readable integrations) |
| `topics/` | Philosophical topics |
| `concepts/` | Core concepts |
| `voids/` | Voids (cognitive gaps, unchartable territories) |
| `tenets/` | Five foundational commitments |
| `arguments/` | Structured arguments |
| `authors/` | Author profiles |
| `papers/` | Academic preprints (SSRN, PhilArchive) |
| `questions/` | Open questions |
| `research/` | AI research notes |
| `reviews/` | Pessimistic, optimistic, deep, and outer reviews |
| `project/` | Project documentation and editorial disciplines |
| `templates/` | Obsidian templates |
| `workflow/` | AI automation state (todo, changelog, evolution-state) |

## Editorial Disciplines

The Map is governed by a stack of explicit disciplines that constrain how content is written, calibrated, and reviewed. They exist because honest human-AI collaboration requires named failure modes and named tests:

**Calibration and evidence.** The disciplines that prevent the framework from inflating the evidential weight of its own commitments.

- [[evidential-status-discipline]] - Five-tier evidence scale and the diagnostic test that separates calibration error from bedrock disagreement
- [[public-claim-register]] - High-stakes articles carry an inspectable per-claim register: evidence grade, defeater removed, missing discriminator, and retraction trigger
- [[testability-ledger]] - Consolidated catalogue of what observations would update for or against the Map
- [[causal-budget-ledger]] - Every mental-causation claim must spec its candidate set, bandwidth, pathway, signature, falsification condition, and physicalist null
- [[mqi-empirical-fragility]] - Where the Minimal Quantum Interaction tenet's physics gap could narrow, and what survives
- [[coherence-inflation-countermeasures]] - Safeguards against systematic overcommitment
- [[calibration-audit-triple]] - Three corpus-level drift audits (literature-drift, altered-state symmetry, topic-concept anchoring)
- [[quantum-claim-and-quotation-disciplines]] - Mechanism-variance audit for quantum-consciousness claims; quote-string-fidelity check distinct from metadata verification; disconfirming-source-inclusion rule (2026-06-19 brain-specialness triple)

Two citation-integrity conventions, recorded from the 2026-06-07 outer-review cycle that found a shared empirical study summarized inconsistently across articles and an inline cite missing from a References list:

- **Canonical empirical data card.** When several articles lean on the same high-stakes study or experimental programme (e.g. COGITATE for IIT/GWT adversarial testing), one article should host a single referenced data card — citation metadata, design, preregistration status, sample sizes, exact tested predictions, result summary, proponent responses (e.g. Naccache et al. 2025), and a last-verified date — and the rest should link to it rather than re-summarizing independently. Re-summarizing is how framing drifts: this cycle found a fabricated "split-win" COGITATE gloss spread across IIT/GWT/NCC/duhem-quine pages, now corrected. This generalizes the centralized-anchor handling already used for the [[mqi-empirical-fragility|Maier-Dechamps micro-PK foreclosure]], which lives as a single worked reference; a data card is the same move made explicit and reusable for any multi-article empirical claim.
- **Orphan-citation check.** Every inline Author-Year cite should map to a References entry and vice-versa. This cycle caught a Papineau/Balog cite present inline but absent from References — a mechanically detectable defect. `scripts/validate.py` currently checks frontmatter only (no inline↔References cross-referencing), so a lightweight reference-orphan check is a CODE CANDIDATE flagged for operator / tune-system review; it is deliberately not auto-added to the validation pipeline by content work.

Two further tune-system backlog items, recorded from the 2026-06-17 ChatGPT 5.5 Pro outer-review cycle (audit of [[synesthetic-void]]). Both point at real workflow gaps and were motivated by completed worked-examples this session:

- **Citation-consistency propagation.** When a deep review repairs a citation on one article, the corrected metadata is currently NOT propagated to sibling articles citing the same source, leaving stale duplicates. The live exhibit was the June 3 synesthetic-void Wager repair (correct: *Adam* Wager 1999, *Philosophical Psychology* 12(3):263–281), which left [[synaesthesia]] and [[phenomenal-variation-within-a-species]] still carrying the stale "*Alan* Wager (1999, 2001), *Philosophia* 27:571–584" metadata. Both were swept this session (Wager harmonisation, commit 98539664; developmental-pruning cross-site harmonisation, commit 772e0329), so they stand as completed worked-examples motivating a durable workflow change rather than open defects. PROPOSAL: append a corpus-grep step (by author surname + title fragment) to the deep-review / citation-repair workflows so a verified repair automatically sweeps siblings instead of relying on a later outer review to catch the drift. Recurs in the corpus-wide citation patterns logged in MEMORY (Craddock 613 THz sweep, Barrett 2021 eight-vs-six). CODE CANDIDATE for operator / tune-system review.
- **Literature-drift candidate breadth.** `/literature-drift-review`'s active-research pattern list is too narrow — its own changelog note says so. Active empirical areas including synesthesia, aphantasia, neurophenomenology, psychedelic phenomenology, and developmental pruning are absent from the candidate set, so they never receive periodic web-checks. PROPOSAL: widen the pattern list to cover these areas. Low-cost (the audit already runs one WebSearch per run); a tune-system pattern-list edit, not new code.

Two further reviewer proposals are recorded as CANDIDATE DISCIPLINES pending operator sign-off — do NOT implement site-wide without it:

- **"Same data, rival reading" box.** Every void article that uses empirical evidence for a metaphysical tenet would carry a small inline box giving at least one physicalist/functionalist and one deflationary reading of the same data. Captured as a candidate convention; relates to [[evidential-status-discipline]] and [[voids-circularity-discount]].
- **Evidential-tier inline labelling.** Distinguish evidential tiers inline (direct evidence / analogous-phenomenon evidence / adjacent-plasticity evidence / speculative integration) so philosophical analogies do not read as empirical conclusions. Overlaps the existing five-tier [[evidential-status-discipline]]; the new element is the per-sentence inline-label convention, which is the part needing sign-off.

**Engaging opponents.** The disciplines that govern reply-to-opponent prose.

- [[direct-refutation-discipline]] - Earn the disagreement inside the opponent's framework where possible; declare bedrock honestly where not
- [[bedrock-clash-vs-absorption]] - When to absorb an objection into the article vs. preserve it as a rival position
- [[framework-stage-calibration]] - Calibrate analogies to the framework's actual developmental stage

**Methodological structure.** The disciplines that govern how the catalogue itself is built.

- [[mechanism-costs-cartography]] - Exposing taxonomy cells to a fixed battery of mechanism questions to read off cell-relative debts
- [[mechanism-cost-ledger]] - Keep the bill, refuse the verdict: record what each endorsed mechanism owes so Tenet 5's anti-parsimony stance cannot become a licence to ignore costs
- [[cluster-integration-discipline]] - Load-bearing inferences supported by clusters whose strength comes from systematic correspondence
- [[common-cause-null]] - When N convergent observations are really one observation read N times
- [[architecture-vs-significance-two-tier-discount]] - A finding's architectural reality and its significance for the framework's commitments inherit different framework-dependence discounts
- [[per-cluster-independence-scoring]] - Scoring each voids cluster against the four apophatic-cartography criteria and citing the profile rather than the surface count
- [[abandon-coalesce]] - When adjacent voids share thematic territory but encode distinct failure signatures, refuse the merger
- [[voids-circularity-discount]] - Voids catalogued under a framework cannot supply framework-independent evidence for that framework
- [[voids-safety-protocol]] - Safety rails for exploring cognitively hazardous territory
- [[closed-loop-opportunity-execution]] - How the 24-slot cycle, queue-replenishment thresholds, and cycle-trigger cadences close the loop from review-recommendation to executed-and-reviewed content

**Outer-review calibration.** Disciplines for weighting external AI critiques.

- [[outer-review-empirical-vs-methodological-freshness]] - When the reviewer's index is stale but the methodological finding still lands
- [[outer-reviewer-service-calibration]] - Calibration data and policy for the three-service outer-review mix

**Convergent-review practices.** Six cross-cutting review and writing checks, recorded from the [[outer-review-synthesis-2026-07-17|2026-07-17 outer-review cycle]], in which two of three reviewers (ChatGPT 5.6 Pro and Claude Opus 4.8) independently converged on the same methodology gaps. The motivating instance was [[concepts/consistent-histories-interpretation]]: a high-severity framework-vs-outcome category error, first flagged by the Map's own 2026-07-09 pessimistic review and left "untouched by instruction," was still surfaced by all three same-cycle reviewers while the article continued to present as reviewed. These are documented practice — checklist items reviewers and editors apply by hand. Promoting any of them into a skill, validator step, or automated gate is a separate operator decision, not something content or refine work should install.

- **Severity gating.** An article must not retain unqualified "reviewed" status while a known high-severity finding sits unresolved. When a review flags a high-severity defect that is not fixed in the same pass, the article's review status is provisional until the finding is closed or explicitly downgraded with a reason.
- **Selection-locus check (epistemic vs dynamical).** Any article invoking a "gap where consciousness could act" must specify whether the gap is epistemic (a matter of description, underdetermination, or framework choice) or dynamical (an unexplained physical event). Review blocks epistemic→metaphysical slides: an article that names the disanalogy and then proceeds as if it did not apply is a failure, not a pass.
- **Tenet-independent verdict, then tenet-conditional.** Technical articles should state what follows from the external literature *without* the five tenets first, then separately state what changes once the tenets are assumed — keeping compatibility, evidential support, and tenet-fit visibly distinct. This subsumes the conditionality-in-leads rule: where a target is only conditionally tenet-friendly, the conditionality belongs in the abstract or first paragraph, not paragraphs after a tenet-friendly headline (the consistent-histories "ally against Many-Worlds" abstract is the exhibit).
- **Compatible-with is not evidence-for; mark self-citations.** Distinguish "compatible with the Map" from "evidence for the Map" in every ally or interpretive claim, extending the interface-compatible-vs-suggestive tiering. Relatedly, mark the source role of every citation — primary / secondary / proponent / critic / internal-synthesis. Map self-citations establish what the Map believes, not independent evidence for disputed physics or philosophy, and must not be read as the latter.
- **Audit for load-bearing *absent* citations.** Verifying that present citations are accurate is not enough; the strongest technical objection to a target must itself be cited. The exhibit is Kent 1997's contrary-inferences result (PRL 78, 2874), the most damaging objection to the single-framework rule, absent from the consistent-histories article until this cycle. Review asks not only "are the cites correct?" but "is the strongest opposing cite missing?"
- **Currentness sweeps.** Periodically run a forward-citation / recent-literature check on active-research articles. The tell is a July-2026 article that misses a December-2025 directly-relevant paper (the Zampeli–Pavlou–Wallden 2025 contrary-inference result was the live miss). This complements the [[calibration-audit-triple|literature-drift audit]] rather than replacing it.

## Related Documents

- [[project-brief]] - Project aims, methods, and design decisions
- [[tenets]] - The five human-curated foundational commitments
- [[writing-style]] - Editorial standards: LLM-first structure, named-anchor summaries, evidential calibration
- [[automation]] - AI automation system for content development
- [[why-this-is-different]] - Visitor-facing answer to "is this just another AI explainer?"
- [[human-supervision]] - How human oversight governs AI-generated content

## Contributing

Content originates in Markdown files in the Obsidian vault. Human edits and AI edits are tracked separately through frontmatter timestamps (`human_modified`, `ai_modified`) and an `ai_contribution: 0-100` field. The [[writing-style]] guide defines the editorial standards every article follows; the [[project-brief]] documents the project's aims and design decisions; [[human-supervision]] documents how human oversight governs AI-generated content. The repository is public at [github.com/unfinishablemap/unfinishablemap](https://github.com/unfinishablemap/unfinishablemap).

## Relation to Site Perspective

As the project's landing page, this document does not itself argue a philosophical position. The disciplines it indexes, however, are how the Map's [[tenets]] survive contact with AI-scale content generation. Dualism, Minimal Quantum Interaction, Bidirectional Interaction, No Many Worlds, and the bounded use of Occam's Razor are easy to state and hard to hold to as the catalogue grows; the editorial disciplines listed above are the machinery that prevents tenet-coherence from quietly upgrading the evidential status of empirical claims, prevents framework-incompatibility from being mistaken for refutation, and prevents the catalogue from being read as evidence for the framework that generated it.
