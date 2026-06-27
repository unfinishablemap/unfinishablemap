---
title: Human Supervision
description: "Not an AI content farm. Human-directed, AI-assisted philosophy with full version history, multi-stage review, and a structural commitment to inspectability."
created: 2026-01-24
modified: 2026-05-19
human_modified: 2026-01-24T00:00:00+00:00
ai_modified: 2026-06-27T00:05:00+00:00
last_deep_review: 2026-06-27T00:05:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[automation]]"
  - "[[project]]"
  - "[[why-this-is-different]]"
  - "[[writing-style]]"
  - "[[changelog]]"
  - "[[tenets]]"
  - "[[agentic-philosophy-adversarial-self-review]]"
ai_contribution: 55
author: Andy Southgate
ai_system: claude-opus-4-7
ai_generated_date: 2026-01-24
last_curated: null
---

The Unfinishable Map uses AI to generate and refine content, but every article exists within a human-supervised system. This page explains what that means and why it matters. For the short, visitor-facing answer to "is this just another AI explainer?", see [[why-this-is-different]].

## Why This Matters

The internet is filling with AI-generated content farms—sites that publish machine output without review, editing, or accountability. The Unfinishable Map is different:

- **Intentional creation**: Content serves a coherent philosophical project, not SEO traffic
- **Ongoing refinement**: Articles are reviewed, critiqued, and improved over time
- **Full transparency**: Every edit is tracked in version control
- **Human direction**: A human sets priorities, reviews output, and maintains editorial control

## How Supervision Works

### Editorial Control

A human editor (currently Andy Southgate) maintains control over:

- Which topics get researched and written
- Task prioritization in the [[todo|task queue]]
- The [[tenets|philosophical commitments]] the system holds itself to
- The skills, disciplines, and methodology the [[automation|automation system]] runs
- Direct intervention when the AI drifts from site goals

Direction is gated by the human; individual article publication is not. AI-generated content is published directly with full version history rather than awaiting per-article approval. This is a deliberate choice: requiring human sign-off on every change would bottleneck the system into producing roughly the volume a single editor could review, defeating the experiment in human-AI collaboration. The system instead trades pre-publication gating for post-publication inspectability — every change is auditable, retractable, and visible.

### Review Cycles

Content undergoes multiple review passes:

1. **Initial generation**: AI creates draft content based on research
2. **Pessimistic review**: Internal AI critiques find logical gaps and counterarguments
3. **Optimistic review**: Internal AI identifies strengths and expansion opportunities
4. **Outer review**: External AI systems (ChatGPT, Claude, Gemini) run nightly via a Chrome-driven automation pipeline; the Map's `/outer-review` skill verifies their citations and converts findings into tasks. This is a third lens that does not share the generator's training, so it catches blind spots the internal reviews miss.
5. **Human curation**: Editor reviews articles as time permits, prioritising those flagged by the review pipeline

The `last_curated` date in article metadata shows when a human last reviewed that page. Many articles carry `last_curated: null` — the editor cannot personally review every page in a corpus the AI maintains continuously. The signal exists so visitors can see which pages have had direct human attention and which have not; the [[changelog|changelog]] records every change regardless.

### Version History

Every article links to its complete edit history on GitHub. You can see:

- When the article was created
- Every change made since then
- Whether changes came from human or AI commits
- The full content at any point in time

This transparency is deliberate. Unlike content farms that hide their processes, we show our work.

## What AI Does

The AI system handles:

- **Research**: Gathering information on philosophical topics
- **Drafting**: Writing initial article content
- **Cross-referencing**: Linking related concepts across the site
- **Review**: Finding weaknesses and opportunities in existing content
- **Refinement**: Improving clarity and accuracy over time

## What Humans Do

The human editor handles:

- **Direction**: Deciding what the site should cover and how
- **Priority**: Choosing which tasks matter most
- **Quality control**: Reviewing AI output for errors and misalignment
- **Accountability**: Taking responsibility for published content
- **Course correction**: Adjusting when the AI drifts from site goals

## The Goal

This isn't a site that happens to use AI. It's a deliberate experiment in human-AI collaboration for knowledge synthesis. The goal is a comprehensive philosophical resource that:

- Maintains a consistent perspective (see [[tenets]])
- Builds genuine understanding rather than superficial coverage
- Improves over time through systematic review
- Remains transparent about its methods

The "unfinishable" in our name reflects this: we're building something that grows and refines indefinitely, not churning out disposable content.

## Content-Specific Safeguards

Beyond general editorial oversight, certain content types receive additional protection:

- **Voids content**: The [[voids-safety-protocol|Voids Safety Protocol]] governs exploration of cognitively hazardous territory—requiring epistemic labeling, exit paths, human review gates, and stop conditions
- **Coherence inflation**: [[coherence-inflation-countermeasures|Dedicated countermeasures]] prevent the AI system from systematically inflating confidence in the Map's positions

## Relation to Site Perspective

Human supervision is methodological infrastructure rather than a substantive philosophical claim, but its design embodies **[[tenets|Tenet 5: Occam's Razor Has Limits]]** at the editorial level. A simpler "publish what the AI generates and call it good" pipeline would saturate under load, drift from the framework, and accumulate unaddressed objections invisibly. A simpler "human approves every article before publication" pipeline would bottleneck the system into a single editor's reading speed and defeat the point of AI-assisted scale.

The actual design refuses both simplifications: humans control direction, priorities, tenets, and methodology; AI handles research, drafting, cross-referencing, and review; every change is logged so the trade-off remains inspectable. Inspectability is the price the system pays for that refusal, and the reason it can be trusted by inspection rather than by trust.

The [[writing-style|writing-style guide]] and the [[automation|automation system]] describe the disciplines and the orchestrator that operationalise this stance. The methodology behind the multi-stage review architecture is written up in full in [[agentic-philosophy-adversarial-self-review|the methodology preprint]] (DOI 10.2139/ssrn.6330678).

## Questions?

If you have questions about how this site operates, the [[project|Project]] section has more details, or you can view the source code and full automation system on [GitHub](https://github.com/unfinishablemap/unfinishablemap).
