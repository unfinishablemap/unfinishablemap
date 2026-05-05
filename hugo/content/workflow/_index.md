---
ai_contribution: 100
ai_generated_date: 2026-01-05
ai_modified: 2026-05-04 14:30:00+00:00
ai_system: claude-opus-4-7
author: Andy Southgate
concepts: []
created: 2026-01-05
date: &id001 2026-05-04
draft: false
human_modified: 2026-01-05
last_curated: null
modified: *id001
related_articles:
- '[[automation]]'
- '[[todo]]'
- '[[changelog]]'
- '[[highlights]]'
title: Workflow System
topics: []
---

The workflow system executes AI skills programmatically and tracks their execution history.

## Overview

Skills are invoked via the Claude CLI using stream-json format, which allows proper skill expansion and tool access. The workflow executor:

1. Invokes a skill by name
2. Captures execution metrics (duration, cost, turns)
3. Logs results to this file
4. Commits changes using the `/agent-commit` skill for meaningful messages

## Available Skills

### Orchestration

The evolution loop (`scripts/evolve_loop.py`) is the main orchestrator. It runs a deterministic 24-slot task cycle interleaved with several time-triggered events: daily highlights at 8am UTC, daily outer-review commissions at 02–04 UTC across three external services, and continuous agentic-social posting on a 45-minute interval.

| Skill | Purpose | Modifies Content? |
|-------|---------|-------------------|
| `/replenish-queue [mode]` | Auto-generate tasks when queue is empty or near-empty | Yes (todo.md only) |
| `/tune-system` | Monthly meta-review—analyze system operation, adjust cadences/thresholds | Yes (state, minor) |

### Content Creation

| Skill | Purpose | Modifies Content? |
|-------|---------|-------------------|
| `/expand-topic [topic]` | Generate new article on a topic | Yes (creates draft) |
| `/refine-draft [file]` | Improve existing draft content | Yes (edits content) |
| `/research-topic [topic]` | Web research, outputs notes to [research](/research/) | Research notes only |
| `/research-voids` | Daily research on cognitive gaps and unchartable territories | Research notes only |
| `/apex-evolve` | Build/maintain apex articles — human-readable synthesis pieces | Yes (creates, modifies) |
| `/embed-videos` | Embed published YouTube videos from sibling auto_unfin repo into matching articles | Yes (obsidian source) |

### Review & Validation

| Skill | Purpose | Modifies Content? |
|-------|---------|-------------------|
| `/validate-all` | Check frontmatter, links, orphans | No (reports only) |
| `/check-tenets` | Verify alignment with 5 foundational tenets | No (reports only) |
| `/check-links` | Verify all internal links work | No (reports only) |
| `/pessimistic-review` | Find logical gaps, unsupported claims, counterarguments | No (reports only) |
| `/optimistic-review` | Find strengths and expansion opportunities | No (reports only) |
| `/deep-review [file]` | Comprehensive single-document review with improvements | Yes (modifies content) |
| `/outer-review [file]` | Process an external AI review file, normalise links, verify claims, generate tasks, send Telegram summary | Yes (modifies review file, creates tasks) |

### Outer-Review Automation (Chrome-driven)

The Map commissions outer reviews from three external AI systems automatically every night within a dedicated Chrome window (00:00–07:00 UTC, with 07:00–08:00 as a buffer for in-flight tasks). Each service has a paired commission/collect skill; both feed the generic `/outer-review` post-processor.

| Skill | Purpose | Modifies Content? |
|-------|---------|-------------------|
| `/commission-chatgpt-review` | 02:00 UTC daily. Drives Chrome to ChatGPT 5.5 Pro Extended in the Map's project workspace; submits prompt; records pending entry. | Yes (pending-reviews.yaml) |
| `/collect-chatgpt-review` | Per-iteration when a pending ChatGPT entry is ≥90 min old. Extracts response, writes review file, invokes `/outer-review`. | Yes (creates review file) |
| `/commission-claude-review` | 03:00 UTC daily. Claude Opus 4.7 Adaptive + Research + Web Search; navigates the optional clarifying-questions stage with "go". | Yes (pending-reviews.yaml) |
| `/collect-claude-review` | Per-iteration when a pending Claude entry is ≥60 min old. Opens the artifact panel; extracts the body via DOM walker. | Yes (creates review file) |
| `/commission-gemini-review` | 04:00 UTC daily. Gemini 2.5 Pro with Deep Research; clicks the mandatory "Start research" button on the research-plan stage. | Yes (pending-reviews.yaml) |
| `/collect-gemini-review` | Per-iteration when a pending Gemini entry is ≥20 min old. Extracts the report from `.markdown.markdown-main-panel`. | Yes (creates review file) |

Lifecycle: each task launches a fresh Chrome under `~/unfin/chrome-profiles/unfinishable`, runs to completion, and stops Chrome (Chrome with the Claude Code extension degrades over long sessions, so per-task lifecycle is the cure). A cross-repo `fcntl` lock at `~/unfin/chrome-profiles/.automation.lock` prevents this repo and the sibling auto_unfin video pipeline from driving Chrome simultaneously. The lock is auto-released on holder exit (kernel guarantee), so there is no stale-lock recovery problem; `python -m tools.chrome_session [--status | --force-cleanup]` exposes status and a wedged-Chrome cleanup path.

The post-processor (`/outer-review`) is service-agnostic: it normalises links, fetches and verifies external citations, generates tasks in `[[todo]]`, logs to `[[changelog]]`, sends a ~100-word Telegram summary with a link to the published report, and commits.

### Content Maintenance

| Skill | Purpose | Modifies Content? |
|-------|---------|-------------------|
| `/coalesce` | Merge overlapping articles into unified pieces, archiving originals | Yes (creates, archives) |
| `/condense [file]` | Reduce article length while preserving value | Yes (modifies content) |
| `/archive [file]` | Archive an article while preserving its URL for external links | Yes (moves to archive) |

### Publishing

| Skill | Purpose | Modifies Content? |
|-------|---------|-------------------|
| `/add-highlight [topic]` | Add item to [What's New](/workflow/highlights/) page (max 1/day). Supports backlog: can highlight any content not featured in last 90 days. With `--tweet`, also runs the full add → commit → push → wait-for-deploy → tweet pipeline. | Yes (highlights.md, optionally Twitter) |
| `/agentic-social` | Post site content to an AI-agent social network on a ~45-minute cadence. | No (external only) |
| `/compose-paper` | Compose an academic preprint for SSRN and PhilArchive. Drafts in markdown, then writes to Google Docs via Chrome for final formatting and PDF export. | Yes (creates paper drafts) |

### Internal (Automation Only)

| Skill | Purpose | Modifies Content? |
|-------|---------|-------------------|
| `/agent-commit` | Analyze changes and create meaningful git commit messages | Git only |

The `/agent-commit` skill is invoked automatically by the evolution loop after each content-modifying skill completes. It:

1. Receives the previous skill's output as context
2. Runs `git diff` to analyze actual file changes
3. Generates a descriptive commit message (e.g., `refine(deep-review): improve clarity in free-will.md`)
4. Creates the commit with agent authorship

This replaces the previous generic commit messages like `auto(deep-review): Automated execution`.

## Queue Replenishment

The task queue in [todo](/workflow/todo/) auto-replenishes when active tasks (P0-P2) drop below 3. The evolution loop triggers `/replenish-queue` automatically when the queue is low.

### Task Types and Chains

Tasks generate follow-up tasks automatically:

| Type | Description | Generates |
|------|-------------|-----------|
| `research-topic` | Web research producing notes | → `expand-topic` |
| `expand-topic` | Write new article | → `cross-review` |
| `cross-review` | Review article in light of new content | (terminal) |
| `refine-draft` | Improve existing draft | (terminal) |
| `deep-review` | Comprehensive single-doc review | (terminal) |

### Task Generation Sources

`/replenish-queue` generates tasks from four sources:

1. **Task chains**: Recent `research-topic` completions that need articles written; recent `expand-topic` completions that need cross-review integration
2. **Unconsumed research**: Research notes in `research/` without corresponding articles
3. **Gap analysis**: Content gaps based on tenet support, undefined concepts, coverage targets
4. **Staleness**: AI-generated content not reviewed in 30+ days

### Replenishment Modes

- `conservative`: 3-5 high-confidence tasks only
- (default): 5-8 tasks with good diversity
- `aggressive`: 8-12 tasks including speculative ones

### Cross-Review Tasks

When a new article is written, `/replenish-queue` generates `cross-review` tasks for related existing articles. These reviews:

- Add wikilinks to the new content
- Check for arguments that the new content supports or challenges
- Ensure consistent terminology
- Identify missing cross-references

## System Tuning

The `/tune-system` skill provides meta-level self-improvement for the automation system. It runs monthly (30-day cadence, injected when 45 days overdue).

### What It Analyzes

1. **Cadence adherence**: Are maintenance tasks running on schedule or frequently overdue?
2. **Failure patterns**: What's causing systematic task failures?
3. **Queue health**: Is replenishment producing tasks that actually get executed?
4. **Review findings**: Are identified issues being addressed?
5. **Convergence progress**: Is the system making progress toward goals?

### Change Tiers

| Tier | Scope | Approval |
|------|-------|----------|
| **Tier 1** | Cadence ±2 days, threshold ±2 days | Automatic (max 3/session) |
| **Tier 2** | New P3 tasks, larger changes | Recommendation only |
| **Tier 3** | Skill changes, tenet-related | Report only |

### Safeguards

- **Evidence threshold**: Requires 5+ data points before making changes
- **Change cooldown**: Settings can't change twice within 60 days
- **Locked settings**: Human can lock any setting via `locked_settings` in state
- **Abort conditions**: Stops if >50% failure rate or convergence regresses

### Output

Creates report at `reviews/system-tune-YYYY-MM-DD.md` documenting findings, changes applied, and recommendations.

## Running Workflows

### Evolution Loop

The evolution loop runs continuously, executing tasks on a 24-slot cycle:

```bash
# Run evolution loop (Ctrl+C to stop)
python scripts/evolve_loop.py --interval 2400

# Describe the task cycle
python scripts/evolve_loop.py --describe-cycle

# Test with limited iterations
python scripts/evolve_loop.py --max-iterations 5
```

### Individual Skills

```bash
# Run a skill manually
uv run python scripts/run_workflow.py validate-all

# Run with more turns for complex tasks
uv run python scripts/run_workflow.py expand-topic --max-turns 30
```

## Execution Format

Each workflow execution logs:

- **Status**: Success, Error, MaxTurns, or PermissionDenied
- **Duration**: How long the execution took
- **Cost**: API cost in USD
- **Turns**: Conversation turns used vs maximum
- **Output**: Brief summary or error message
- **Session**: Session ID for debugging

## Recent Executions