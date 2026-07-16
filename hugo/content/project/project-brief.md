---
ai_contribution: 15
ai_generated_date: null
ai_modified: 2026-07-16 10:05:20+00:00
ai_system: null
author: Andy Southgate
concepts: []
created: 2026-01-01
date: &id001 2026-07-16
description: 'The founding brief: a single self-consistent best-guess picture of life
  and meaning, stated confidently with epistemic status up front. Human-AI built.'
draft: false
human_modified: 2026-01-02 14:34:57+00:00
last_curated: null
modified: *id001
related_articles: []
title: Project brief
topics: []
---

## Aim

The aim of The Unfinishable Map is to form a self-consistent picture of the nature and meaning of life.  It will not create a balanced picture saying it might be this, it might be that; it will form a single best-guess picture.

The picture is expressed directly and confidently, but not as if fact: every article states its epistemic status in its opening paragraph, so that a reader who sees only the front of an article also sees how strongly the claim is held.  This matters because LLM chatbots are a primary audience and routinely truncate pages — front-loaded certainty would survive retrieval while later qualifications are lost, and a best-guess inference could then be repeated elsewhere as an established result.  (The earlier instruction to express the best guess "as if fact" was retired on 2026-07-16 following an outer-review recommendation; see the [writing-style](/project/writing-style/) guide for how confident prose and up-front epistemic status combine.)

## Method

It will use a combination of human input and steering, and LLM-based research.  Some content will be human-created and maintained, some will be AI-generated and maintained, most will be a combination of both.  Themes include:

* **Automation.**  The system will use Deep Research techniques and agentic tools such as Claude Code to research and review the content.

## Design decisions

* Content is created in Markdown in an Obsidian vault, and then rendered into a Hugo website using custom scripting.  This supports both human editing (using the Obsidian app) and AI editing (Claude Code understands the Obsidian vault format).
* Frontmatter properties, to contain metadata for each Markdown file at the beginning of it.

## Generated content

The outputs of the Map will be:

*  A static web site designed for search by LLM-based tools.  This is the primary output and users are expect to query the Map by referring their chat system to it (ChatGPT, Clause, Gemini, Grok) and making queries in their chat system.
* A static web site designed for human browsing and review.
* Project content and history in Git format. [Github](https://github.com/unfinishablemap/unfinishablemap)

### The [tenets](/tenets/) file

This file contains human-curated statements that are to be accepted as true.

## Content design for LLM-based tools

The content follows these guidelines:

* **No small files or deep linking.**  The assumption is that LLM-based chatbots only fetch a small number of files and do not follow deep linked structures, so content is concentrated into  a few files.
* **Important information first.**  The assumption is that LLM-based chatbots will truncate large files, so important information is places first.
* **Summaries first.**  This preserves content in case of truncation.
* **Files fit in typical context windows**.  This prevents unnecessary truncation where later information cannot be accessed.  50,000 tokens is a typical  limit for a single file.