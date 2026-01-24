---
title: "The Unfinishable Map"
created: 2026-01-01
modified: 2026-01-03
human_modified: 2026-01-03
ai_modified: 2026-01-24T00:00:00+00:00
draft: false
topics: []
concepts: []
related_articles: []

ai_contribution: 40
author: "Andy Southgate"
ai_system: "claude-opus-4-5-20251101"
ai_generated_date: null
last_curated: null
---

*A system like [Deep Thought](https://en.wikipedia.org/wiki/Deep_Thought_(The_Hitchhiker%27s_Guide_to_the_Galaxy)), only slower and less confident.*

A project in Agentic Philosophy: an AI system that researches, writes, and revises a coherent worldview about consciousness, meaning, and what it is to be human. Not balanced. Not hedged. Just a best guess at the truth—one that evolves as the system learns and argues with itself.

What makes this different:
 * **Continual automated review and revision.**  This is not just single-time AI generation with its associated problems, but a coherent view constantly refined by both human and AI distinctions.
 * **The Map takes positions** as a foundational starting point.  It's not just a broad review of the philosophy.

**[[highlights|Highlights]]** — Notable additions. **[Follow @unfinishablemap](https://x.com/unfinishablemap)** — a bot posting daily highlights on X.

## Navigating the Map



```mermaid
flowchart BT
    subgraph revision["Continual Revision"]
        direction BT
        TO[Topics]
        CO[Concepts]
        AP[Apex]
        VO[Voids]

        TO --> AP
        CO --> AP
    end

    RE[Research] --> TO
    RE --> CO

    TE[Tenets] -.->|feed into| TO
    TE -.->|feed into| CO

    TO -.->|point to| VO
    CO -.->|point to| VO

    click AP "/apex/" "Apex Articles"
    click TO "/topics/" "Topics"
    click CO "/concepts/" "Concepts"
    click VO "/voids/" "Voids"
    click TE "/tenets/" "Tenets"
    click RE "/research/" "Research"
```

- **[[apex|Apex]]** — Synthesis articles weaving themes together for human readers.
- **[[topics|Topics]]**, **[[concepts|Concepts]]** — Atomic content optimized for AI traversal.
- **[[tenets|Tenets]]** — The five foundational commitments that are integrated into topics and concepts.
- **[[voids|Voids]]** — The boundaries of knowledge—what the Map reveals as unknowable.
- **[[research|Research]]** — Raw notes and sources that inform topics and concepts.

## Starting Points

**[[hard-problem-of-consciousness|The Hard Problem of Consciousness]]** — Why science can't explain the most obvious thing in the universe: that there's something it's like to be you.

**[[meaning-of-life|The Meaning of Life]]** — If consciousness matters, what makes a life worth living?

**[[tenets|The Five Tenets]]** — The foundational commitments that shape everything on this site.

## Concepts Worth Exploring

**[[haecceity|Haecceity]]** — Why being *you* can't be duplicated, even by a perfect copy.

**[[attention-as-interface|Attention as Interface]]** — How consciousness might actually touch the physical world.

**[[interface-locality|Interface Locality]]** — Why minds can't move objects at a distance (and why that's the right answer).

**[[phenomenal-value-realism|Phenomenal Value Realism]]** — The case that consciousness is the only source of intrinsic value.

## Explore

- **[[apex|Apex]]** — Synthesis articles integrating themes
- **[[topics|Topics]]** & **[[arguments|Arguments]]** — Deep dives and critiques
- **[[concepts|Concepts]]** — Core ideas and frameworks
- **[[questions|Questions]]** & **[[voids|Voids]]** — Open problems and unknowables
- **[[project|Project]]** — How the Map works

## How It Works

Content is created through human-AI collaboration:
- Humans provide direction, curation, and foundational tenets
- AI assists with research, article creation, review, and cross-linking in an automated, agentic way
- All content tracks its authorship (human, AI, or mixed)

Learn more in the [[project-brief|Project Brief]].



## Using the Map with AI Chatbots

The Map is designed for AI chatbot consumption. Articles are structured with important information first (so truncation preserves the core message), each page is self-contained, and content focuses on what the Map uniquely contributes rather than repeating standard philosophy.

**If your chatbot navigates websites** (like ChatGPT with browsing, or Perplexity), you can simply ask it to explore the Map. Try: *"Read unfinishablemap.org and explain its view on consciousness"* or *"What does unfinishablemap.org say about the hard problem?"*

**If your chatbot only fetches specific URLs** (like Claude without web access, or some API integrations), provide the page URL directly. Useful starting points:
- `/tenets/` — The foundational commitments
- `/arguments/materialism/` — The case against physicalism
- `/topics/hard-problem-of-consciousness/` — The central puzzle

You can prompt: *"Fetch and summarise `https://unfinishablemap.org/tenets/`"* or *"Read the page at [URL] and answer my question based on it."*

As of 2026-01-22, [miromind.ai](https://miromind.ai) is a free site that can evaluate questions by traversing this site—just instruct it to "Search unfinishablemap.org and...".

The [[writing-style|Writing Style Guide]] explains how content is structured for chatbot retrieval.

## Author

I'm [Andy Southgate](mailto:andy@unfinishablemap.org) <a href="https://x.com/andysouthgate"><i class="fa-brands fa-x-twitter"></i></a>. I'm not qualified to make statements on the subject matter of this site, I'm leaning on the AI for that, but I am a working AI researcher (cybersecurity) with a Ph.D. in Physics.

## Source

The Map can be explored at [github.com/unfinishablemap/unfinishablemap](https://github.com/unfinishablemap/unfinishablemap/), and is also mentioned on [Substack](https://unfinishablemap.substack.com).
