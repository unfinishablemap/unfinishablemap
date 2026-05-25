---
ai_contribution: 100
ai_generated_date: 2026-01-03
ai_modified: 2026-05-25 13:30:00+00:00
ai_system: claude-opus-4-7
author: Andy Southgate
concepts: []
created: 2026-01-03
date: &id001 2026-05-18
description: 'Project landing page for unfinishablemap.org: how human direction combines
  with AI research, writing, and a stack of editorial disciplines to build a philosophy
  that improves over time.'
draft: false
human_modified: 2026-01-05 11:16:56+00:00
last_curated: null
last_deep_review: 2026-05-18 00:00:00+00:00
modified: *id001
related_articles:
- '[[project-brief]]'
- '[[automation]]'
- '[[why-this-is-different]]'
- '[[tenets]]'
- '[[writing-style]]'
- '[[human-supervision]]'
title: The Unfinishable Map Project
topics: []
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

- [evidential-status-discipline](/project/evidential-status-discipline/) - Five-tier evidence scale and the diagnostic test that separates calibration error from bedrock disagreement
- [public-claim-register](/project/public-claim-register/) - High-stakes articles carry an inspectable per-claim register: evidence grade, defeater removed, missing discriminator, and retraction trigger
- [testability-ledger](/project/testability-ledger/) - Consolidated catalogue of what observations would update for or against the Map
- [causal-budget-ledger](/project/causal-budget-ledger/) - Every mental-causation claim must spec its candidate set, bandwidth, pathway, signature, falsification condition, and physicalist null
- [mqi-empirical-fragility](/project/mqi-empirical-fragility/) - Where the Minimal Quantum Interaction tenet's physics gap could narrow, and what survives
- [coherence-inflation-countermeasures](/project/coherence-inflation-countermeasures/) - Safeguards against systematic overcommitment
- [calibration-audit-triple](/project/calibration-audit-triple/) - Three corpus-level drift audits (literature-drift, altered-state symmetry, topic-concept anchoring)

**Engaging opponents.** The disciplines that govern reply-to-opponent prose.

- [direct-refutation-discipline](/project/direct-refutation-discipline/) - Earn the disagreement inside the opponent's framework where possible; declare bedrock honestly where not
- [bedrock-clash-vs-absorption](/project/bedrock-clash-vs-absorption/) - When to absorb an objection into the article vs. preserve it as a rival position
- [framework-stage-calibration](/project/framework-stage-calibration/) - Calibrate analogies to the framework's actual developmental stage

**Methodological structure.** The disciplines that govern how the catalogue itself is built.

- [mechanism-costs-cartography](/project/mechanism-costs-cartography/) - Exposing taxonomy cells to a fixed battery of mechanism questions to read off cell-relative debts
- [cluster-integration-discipline](/project/cluster-integration-discipline/) - Load-bearing inferences supported by clusters whose strength comes from systematic correspondence
- [common-cause-null](/project/common-cause-null/) - When N convergent observations are really one observation read N times
- [abandon-coalesce](/project/abandon-coalesce/) - When adjacent voids share thematic territory but encode distinct failure signatures, refuse the merger
- [voids-circularity-discount](/project/voids-circularity-discount/) - Voids catalogued under a framework cannot supply framework-independent evidence for that framework
- [voids-safety-protocol](/project/voids-safety-protocol/) - Safety rails for exploring cognitively hazardous territory
- [closed-loop-opportunity-execution](/project/closed-loop-opportunity-execution/) - How the 24-slot cycle, queue-replenishment thresholds, and cycle-trigger cadences close the loop from review-recommendation to executed-and-reviewed content

**Outer-review calibration.** Disciplines for weighting external AI critiques.

- [outer-review-empirical-vs-methodological-freshness](/project/outer-review-empirical-vs-methodological-freshness/) - When the reviewer's index is stale but the methodological finding still lands
- [outer-reviewer-service-calibration](/project/outer-reviewer-service-calibration/) - Calibration data and policy for the three-service outer-review mix

## Related Documents

- [project-brief](/project/project-brief/) - Project aims, methods, and design decisions
- [tenets](/tenets/) - The five human-curated foundational commitments
- [writing-style](/project/writing-style/) - Editorial standards: LLM-first structure, named-anchor summaries, evidential calibration
- [automation](/project/automation/) - AI automation system for content development
- [why-this-is-different](/project/why-this-is-different/) - Visitor-facing answer to "is this just another AI explainer?"
- [human-supervision](/project/human-supervision/) - How human oversight governs AI-generated content

## Contributing

Content originates in Markdown files in the Obsidian vault. Human edits and AI edits are tracked separately through frontmatter timestamps (`human_modified`, `ai_modified`) and an `ai_contribution: 0-100` field. The [writing-style](/project/writing-style/) guide defines the editorial standards every article follows; the [project-brief](/project/project-brief/) documents the project's aims and design decisions; [human-supervision](/project/human-supervision/) documents how human oversight governs AI-generated content. The repository is public at [github.com/unfinishablemap/unfinishablemap](https://github.com/unfinishablemap/unfinishablemap).

## Relation to Site Perspective

As the project's landing page, this document does not itself argue a philosophical position. The disciplines it indexes, however, are how the Map's [tenets](/tenets/) survive contact with AI-scale content generation. Dualism, Minimal Quantum Interaction, Bidirectional Interaction, No Many Worlds, and the bounded use of Occam's Razor are easy to state and hard to hold to as the catalogue grows; the editorial disciplines listed above are the machinery that prevents tenet-coherence from quietly upgrading the evidential status of empirical claims, prevents framework-incompatibility from being mistaken for refutation, and prevents the catalogue from being read as evidence for the framework that generated it.