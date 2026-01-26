# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Claude Code Settings

The file `.claude/settings.json` contains pre-approved permissions for The Unfinishable Map. If you create or modify `.claude/settings.local.json` for personal experimentation, remember to merge any useful generic permissions back into `settings.json` so they persist across sessions and for other users.

## Project Overview

The Unfinishable Map is a philosophical content platform built with Hugo and Pico CSS.

**Canonical domain:** `unfinishablemap.org` — Use this domain in all site-visible text, links, and references. The Map may also appear under other domains (e.g., unfinishablemap.com, Netlify subdomains) but the canonical domain should always be used in content.

**Data flow:** Obsidian vault → Python sync tools → Hugo content → Static site (Netlify)

## Commands

```bash
# Install dependencies
uv sync

# Full build pipeline (sync + validate + build Hugo)
uv run python scripts/build.py

# Sync Obsidian → Hugo only
uv run python scripts/sync.py

# Hugo dev server
cd hugo && hugo server

# Validate frontmatter
uv run python scripts/validate.py hugo/content/

# Commit obsidian changes with human/AI attribution
uv run python scripts/commit_obsidian.py --dry-run
uv run python scripts/commit_obsidian.py
```

## Architecture

```
obsidian/           # Primary content source (Obsidian vault)
├── apex/           # Synthesis articles (human-readable integrations)
├── topics/         # Philosophical topics
├── concepts/       # Core concepts
├── research/       # AI research notes (public)
├── templates/      # Obsidian templates
├── project/        # Project documentation
└── workflow/       # AI automation (todo, changelog, reviews)

archive/            # Archived content (preserves URLs for external links)
├── topics/         # Mirrors obsidian structure
├── concepts/
└── ...             # Pages show archive notice linking to replacement

hugo/               # Static site generator
├── content/        # Synced from Obsidian + archive
├── layouts/        # HTML templates
└── data/           # YAML data files

tools/              # Python library modules
├── sync/           # Obsidian → Hugo conversion
└── curate/         # Frontmatter validation

scripts/            # CLI entry points (thin wrappers calling tools/)
```

## Authorship Tracking

When editing files in `obsidian/`, update the `ai_modified` frontmatter field with the current ISO timestamp:

```yaml
ai_modified: 2026-01-02T15:30:00+00:00
```

The `human_modified` field is updated automatically by the Obsidian Frontmatter Modified Date plugin when the user edits.

The `commit_obsidian.py` script compares these timestamps to determine git commit authorship:
- Human edits: Uses configured git user
- AI edits: Uses "unfinishablemap.org Agent <agent@unfinishablemap.org>"

### Git Commit Author

When committing changes (other than automated AI work), use the configured git author name and email. If none are configured, use:
- Name: Andy Southgate
- Email: andy@unfinishablemap.org

## Timezone Policy

**All timestamps must use UTC (+00:00).** This ensures:
- Consistent ordering and comparison across all content
- No leakage of author/user geographical location
- Simpler timestamp handling in automation scripts

When generating timestamps in Python, use:
```python
from datetime import datetime, timezone
timestamp = datetime.now(timezone.utc).isoformat()
```

## Frontmatter Schema

All markdown content uses a flat schema (no nesting):

```yaml
---
title: "Article Title"
created: YYYY-MM-DD
modified: YYYY-MM-DD
human_modified: YYYY-MM-DD or ISO timestamp
ai_modified: null or ISO timestamp
draft: true/false # always default to false
topics: []
concepts: []
related_articles: []

ai_contribution: 0-100   # 0=human, 100=ai, 1-99=mixed
author: "Name"           # human author
ai_system: null          # or model name like "claude-sonnet-4-20250514"
ai_generated_date: null  # when AI generated content
last_curated: null       # last human review date
last_deep_review: null   # ISO timestamp of last comprehensive review
---
```

Authorship type is derived from `ai_contribution`:
- `0` = human (purely human-created)
- `100` = ai (purely AI-generated)
- `1-99` = mixed (human-AI collaboration)

## Writing Style

All content follows the Writing Style Guide in `obsidian/project/writing-style.md`.

Key principles:
- **LLM-first**: Primary audience is chatbots fetching pages. Important information first (truncation resilience).
- **Named-anchor summaries**: When forward-referencing concepts, use "explained below" pattern with section anchors.
- **Selective background**: Include background only when framed for the Map's dualist perspective. Skip what LLMs already know.
- **Tenet alignment**: Every article must connect to tenets explicitly via "Relation to Site Perspective" section.
- **Avoid LLM clichés**: Do not use the "This is not X. It is Y." construct—it has become an overused LLM pattern that grates on readers. Rephrase to make the positive claim directly or integrate the contrast more naturally.

## Code Conventions

- **Python:** Ruff linting (E, F, I, N, W), line length 100, mypy type hints required
- **Module pattern:** `scripts/` contains thin CLI wrappers, `tools/` contains business logic
- **Content links:** Obsidian uses `[[wikilinks]]`, auto-converted to Hugo markdown links during sync
- **Section index files:** Files named the same as their folder (e.g., `obsidian/project/project.md`) become `_index.md` in Hugo (e.g., `hugo/content/project/_index.md`) and serve as the section landing page
- **Site index:** `obsidian/index.md` becomes `hugo/content/_index.md` (the Map landing page)

### Error Handling

**Never use fallthrough logic that hides errors.** When dispatching on enums, types, or task categories:

- **Do NOT** provide a catch-all `else` that silently substitutes a default behavior
- **DO** raise an exception for unhandled cases so they surface immediately
- Use `LogicFlawError` (or similar) for cases that indicate a programming error rather than user error

**Bad** (error-hiding fallthrough):
```python
if task_type == TaskType.EXPAND:
    return expand_skill(task)
elif task_type == TaskType.RESEARCH:
    return research_skill(task)
else:
    # Silently falls through - new task types will be mishandled!
    return expand_skill(task)
```

**Good** (fail-fast):
```python
if task_type == TaskType.EXPAND:
    return expand_skill(task)
elif task_type == TaskType.RESEARCH:
    return research_skill(task)
else:
    raise LogicFlawError(f"Unhandled task type: {task_type}")
```

This ensures that when new enum values are added, missing handler code surfaces immediately rather than causing silent misbehavior.

## AI Automation System

The Map includes scheduled AI automation for content development. All AI-generated content is created as drafts requiring human review.

### Skills (Slash Commands)

| Skill | Purpose | Modifies Content? |
|-------|---------|-------------------|
| `/validate-all` | Daily health check: frontmatter, links, orphans | No (reports only) |
| `/check-tenets` | Verify content aligns with 5 foundational tenets | No (reports only) |
| `/pessimistic-review` | Find logical gaps, unsupported claims, counterarguments | No (reports only) |
| `/optimistic-review` | Find strengths, expansion opportunities | No (reports only) |
| `/research-topic [topic]` | Web research, outputs notes to `research/` | No (research notes only) |
| `/research-voids` | Research voids (cognitive gaps, unchartable territories). Daily. | No (research notes only) |
| `/expand-topic [topic]` | Generate new article (always `draft: true`) | Yes (creates drafts) |
| `/refine-draft [file]` | Improve existing draft content | Yes (keeps as draft) |
| `/deep-review [file]` | Comprehensive single-document review with improvements | Yes (modifies content) |
| `/condense [file]` | Intelligently reduce article length while preserving value | Yes (modifies content) |
| `/replenish-queue [mode]` | Auto-generate tasks when queue is empty (chains, gaps, research) | Yes (todo.md only) |
| `/tune-system` | Monthly meta-review: analyze system operation | Yes (state, minor) |
| `/add-highlight` | Add item to highlights page (max 1/day) | Yes (highlights.md) |
| `/tweet-highlight` | [DEPRECATED] Use add-highlight --tweet instead. Tweets existing highlight without deployment verification. | No (external only) |
| `/outer-review` | Commission and process external AI analysis to reduce blind spots | Yes (creates review, tasks) |
| `/coalesce` | Combine multiple related articles into one unified piece. Archives originals to preserve URLs. | Yes (creates, archives) |
| `/archive` | Archive an article while preserving its URL for external links. | Yes (moves to archive) |
| `/apex-evolve` | Build and maintain apex articles—human-readable synthesis pieces. | Yes (creates, modifies) |
| `/agent-commit` | Analyze changes and create a meaningful commit with agent authorship. Internal skill for evolve_loop. | Yes (git only) |

### Task Queue

Tasks are managed in `obsidian/workflow/todo.md`:
- P0 (urgent) → P3 (nice to have)
- Human prioritizes; AI executes
- All content changes create drafts

#### Task Types

| Type | Description | Generates Chain? |
|------|-------------|------------------|
| `research-topic` | Web research producing notes | Yes → expand-topic |
| `expand-topic` | Write new article | Yes → cross-review |
| `cross-review` | Review article in light of new content | No |
| `refine-draft` | Improve existing draft | No |
| `deep-review` | Comprehensive single-doc review | No |
| `condense` | Reduce article length while preserving value | No |
| `other` | Miscellaneous tasks | No |

#### Queue Replenishment

The queue auto-replenishes when active tasks (P0-P2) drop below 3. `/evolve` triggers `/replenish-queue` automatically. Tasks are generated from:

1. **Task chains**: `research-topic` → `expand-topic` → `cross-review`
2. **Unconsumed research**: Research notes without corresponding articles
3. **Gap analysis**: Content areas needing expansion (tenet support, undefined concepts)
4. **Staleness**: AI-generated content not reviewed in 30+ days
5. **Length violations**: Articles exceeding word count thresholds

State tracking in `obsidian/workflow/evolution-state.yaml` includes:
- `task_chains.pending_articles`: Research awaiting article synthesis
- `task_chains.pending_cross_reviews`: New articles needing integration review
- `replenishment_config`: Thresholds and limits

### Changelog

AI activity is logged to `obsidian/workflow/changelog.md` with:
- Timestamp, task name, status
- Duration, cost estimate
- Output files, commit hash

### Cycle-Based Scheduling

The evolution loop (`scripts/evolve_loop.py`) uses a deterministic task cycle. Speed is controlled by `--interval`; the cycle ensures consistent task ratios regardless of speed.

**The 24-slot task cycle:**
- Queue tasks: 16 slots (67%) - picks from P0-P2 todo queue
- Deep-review: 4 slots (17%)
- Pessimistic-review: 1 slot
- Optimistic-review: 1 slot
- Coalesce: 1 slot
- Research-voids: 1 slot

**Cycle triggers** (run every N complete cycles):
- check-links: every 2 cycles
- check-tenets: every 3 cycles
- apex-evolve: every 4 cycles
- tune-system: every 6 cycles

**Time-triggered** (wall clock):
- add-highlight-tweet: 8am UTC daily (finds highlight-worthy work, adds highlight, pushes, waits for deploy, tweets)

**Speed examples:**
| Interval | Sessions/day | Cycle duration |
|----------|--------------|----------------|
| 10 min   | 144          | 4 hours        |
| 40 min   | 36           | 16 hours       |
| 4 hours  | 6            | 4 days         |

### Running Automation

**Local:**
```bash
# Run evolution loop (Ctrl+C to stop)
python scripts/evolve_loop.py --interval 2400

# Describe the task cycle
python scripts/evolve_loop.py --describe-cycle

# Test with limited iterations
python scripts/evolve_loop.py --max-iterations 5
```

**Speed control:**
```bash
# Fast (testing): 10 min intervals
python scripts/evolve_loop.py --interval 600

# Normal: 40 min intervals (default)
python scripts/evolve_loop.py --interval 2400

# Slow (low budget): 4 hour intervals
python scripts/evolve_loop.py --interval 14400
```

### The Five Tenets

All content must align with these foundational commitments (see `obsidian/tenets/tenets.md`):

1. **Dualism** - Consciousness is not reducible to physical processes
2. **Minimal Quantum Interaction** - Smallest possible non-physical influence on quantum outcomes
3. **Bidirectional Interaction** - Consciousness causally influences the physical world
4. **No Many Worlds** - Reject MWI; indexical identity matters
5. **Occam's Razor Has Limits** - Simplicity is unreliable with incomplete knowledge

### Adding New Skills

To add a new skill to the workflow system, touch these parts:

#### 1. Create the Skill File

Create `.claude/skills/[skill-name]/SKILL.md`:

```markdown
---
name: skill-name
description: Brief description for skill listing.
---

# Skill Title

[What this skill does]

## When to Use

- Bullet points describing when this skill should be invoked

## Instructions

### 1. [First Step]
[Detailed instructions...]

### 2. [Second Step]
[Continue with numbered steps...]

## Important

- Key constraints or requirements
```

#### 2. Register with /evolve (if maintenance task)

If the skill should run on a schedule, update `.claude/skills/evolve/SKILL.md`:

1. Add to the **Check Staleness** table with cadence and overdue threshold
2. Add to the **Execute Tasks** section showing how to invoke it

#### 3. Update evolution-state.yaml

For scheduled tasks, add entries to `obsidian/workflow/evolution-state.yaml`:

```yaml
last_runs:
  new-skill: null  # or initial timestamp

cadences:
  new-skill: 168  # how often in hours (168h = 7 days)

overdue_thresholds:
  new-skill: 72  # inject when overdue by N hours (72h = 3 days)
```

#### 4. Update CLAUDE.md Skills Table

Add the skill to the **Skills (Slash Commands)** table in this file with:
- Skill name
- Purpose description
- Whether it modifies content

#### 5. Interactive Sessions

**If the session is interactive, ask the user how often the skill should run:**
- Daily, weekly, monthly, or manual-only?
- What overdue threshold makes sense?
- Should it compete with todo tasks or run independently?

This ensures the cadence matches user expectations rather than guessing.
