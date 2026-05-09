---
name: combine-outer-reviews
description: Synthesize all outer reviews from a single UTC cycle into one convergence report; upgrade priority of tasks flagged by ≥2 reviewers.
---

# Combine Outer Reviews

After all three external reviewers (ChatGPT, Claude, Gemini) have been collected and processed for the same UTC date, this skill reads the per-review files, identifies convergent findings, writes a synthesis report, and rewrites the matching `todo.md` tasks so issues flagged by multiple reviewers carry elevated priority.

## When to Use

- The evolve loop fires this automatically when `tools.reviews.synthesis.cycle_dates_to_synthesize()` returns a ready cycle date.
- Manual invocation: `/combine-outer-reviews YYYY-MM-DD` (the cycle date).

## Why Synthesis Matters

Each `/outer-review` pass treats one external review in isolation. A finding that all three reviewers independently flag is much stronger evidence of a real defect than the same finding from one reviewer — but per-review processing cannot see across reviews, so convergent findings end up at the same priority as singleton noise. This skill is the curation pass: it weights tasks by how many independent reviewers flagged them.

## Prerequisites

- ≥2 review files at `obsidian/reviews/outer-review-{date}-*.md` exist with `outer_review_status: processed` in their frontmatter (i.e., `/outer-review` already ran on each).
- No synthesis file at `obsidian/reviews/outer-review-synthesis-{date}.md` yet (idempotence).

The trigger helper enforces both checks before this skill is invoked, but the skill should re-validate them and refuse with a clear message if violated.

## Instructions

### 1. Parse the cycle date

The cycle date is the single argument: `YYYY-MM-DD`. Validate the format. If missing, refuse and exit.

### 2. Locate processed review files

Use the helper to confirm the cycle is ready:

```python
from tools.reviews.synthesis import (
    cycle_dates_to_synthesize,
    count_processed_reviews_for,
    synthesis_path_for,
)
```

If `synthesis_path_for(date).exists()` already, refuse — synthesis has already run for this cycle.

Glob `obsidian/reviews/outer-review-{date}-*.md`, exclude any file starting with `outer-review-synthesis-`, and keep only those whose frontmatter has `outer_review_status: processed`. Refuse if fewer than 2 remain.

### 3. Read each review

For every processed review file, capture:

- Service identity (from `ai_system` frontmatter — e.g., `chatgpt-5-5-pro`, `claude-opus-4-7`, `gemini-2-5-pro`).
- Display name (from the `**Reviewer**:` line in the body).
- The Reply section (the external system's actual analysis).
- The Verification Notes section, if present (records which reviewer claims `/outer-review` confirmed, disputed, or could not check).
- The conversation URL (from `outer_review_conversation_url` frontmatter).

Treat verification-disputed claims as **lower** weight when clustering — a disputed claim is not real convergence even if another reviewer made the same disputed claim.

### 4. Cluster findings across reviews

Identify finding clusters by **semantic match**, not exact string match. Two reviewers describing the same structural weakness in different vocabulary belong to the same cluster.

For each cluster, record:

- A short cluster description (1 sentence).
- The set of services that flagged it: a subset of `{chatgpt, claude, gemini}`.
- One verbatim quote from each flagging reviewer (so traceability survives).
- Verification status: any of the supporting claims marked disputed in `/outer-review` verification notes.

A cluster with 2+ services in its set is **convergent**. A cluster with 1 service is a **singleton**. Note any cases where reviewers explicitly contradict each other — record these as **divergences**, not convergences.

### 5. Locate existing per-review tasks in todo.md

Open `obsidian/workflow/todo.md`. Find tasks whose body contains:

- `Source: outer-review` AND
- `Review file: reviews/outer-review-{date}-*.md` (any of the cycle's reviews).

Skip tasks already marked complete (lines starting with `### ✓`). For each remaining open task, decide which cluster (if any) it corresponds to, by reading the task's notes and cross-referencing the review it cites.

### 6. Rewrite convergent tasks; leave singletons

For each **convergent cluster** (≥2 services):

- If 2+ open tasks point at the same cluster (one per reviewer), **deduplicate**: keep one task, delete the redundant siblings, and rewrite its frontmatter-style fields:
  - `Type:` — keep the most specific type from the originals (e.g., `refine-draft` beats `expand-topic` for an existing-article fix).
  - Add a new line `Review files:` (plural) listing all source review paths, comma-separated.
  - Replace the original `Review file:` line with `Review files:`.
  - Update `Notes:` to begin with `From convergent outer reviews ({date}, {N}/{cycle_size} reviewers): [{services}]`. Keep the substantive content from the strongest of the original notes; quote each flagging reviewer briefly inline.
  - Add a line: `Synthesis: reviews/outer-review-synthesis-{date}.md`.
- **Upgrade priority by one tier**: P3 → P2, P2 → P1. Do not upgrade beyond P1. If the original task was already P1, leave it.
- If only one open task exists for a convergent cluster (e.g., other siblings already completed), still rewrite its notes/fields and upgrade priority — the cluster is convergent regardless of whether per-reviewer tasks happened to land for every reviewer.

For each **singleton cluster** (1 service): leave the matching task untouched.

If a cluster's matching tasks have all already been completed, **do not resurrect them** — just record the convergence in the synthesis file (step 7); the work is done.

### 7. Write the synthesis file

Write `obsidian/reviews/outer-review-synthesis-{date}.md` with this structure:

```yaml
---
title: "Outer Review Synthesis - {date}"
created: {date}
modified: {today}
human_modified: null
ai_modified: {now-iso}
draft: false
description: "Cross-review synthesis of {N} outer reviews from {date}. Identifies findings flagged by multiple reviewers and upgrades their task priority."
topics: []
concepts: []
related_articles:
  - "[[project]]"
ai_contribution: 100
author: "Andy Southgate"
ai_system: claude-opus-4-7
ai_generated_date: {date}
last_curated: null
synthesizes:
  - reviews/outer-review-{date}-{slug-1}.md
  - reviews/outer-review-{date}-{slug-2}.md
  # … one entry per processed review in this cycle
synthesis_coverage: "{N}/{cycle_size}"  # e.g., "2/3" when one was abandoned
---

**Date**: {date}
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Coverage**: {N} of {cycle_size} commissioned reviewers contributed; {abandoned/failed list if any}.

## TL;DR

[1–3 sentences: the dominant convergent finding, plus a count of clusters by service-coverage.]

## Convergent Findings

For each convergent cluster (≥2 reviewers), one section:

### {Short cluster name}
- **Flagged by**: {service1}, {service2}{, service3}
- **Verification**: {clean | disputed by /outer-review on {service}'s claim of X}
- **Quotes**:
  - **{Service1 display name}**: "{verbatim quote}"
  - **{Service2 display name}**: "{verbatim quote}"
- **Task action**: Upgraded P{old} → P{new}: "{task title}" (was {N} sibling tasks, deduplicated to 1) | Recorded only — matching tasks already completed.

## Singleton Findings

Findings flagged by only one reviewer. Not upgraded; left at original task priority. Listed for the record.

- **{Service display name}**: {short description} → see `todo.md` task "{title}" (P{n}).

## Divergences

Cases where two reviewers explicitly contradicted each other (one defends a position the other criticises). These are interesting signal — the disagreement itself may be worth its own task — but neither view is "convergent."

- **{Service A} vs {Service B}**: {description}.

## Method Notes

- {Anything notable about the cycle: one reviewer was disputed on empirical claims; one abandoned; etc.}
```

If there are zero convergent clusters, still write the synthesis file (it documents that this cycle had no convergence). Use a clear TL;DR like "No convergent findings; all flagged issues were singletons."

### 8. Log to changelog

Prepend to `obsidian/workflow/changelog.md` (immediately after the frontmatter, before the existing entries):

```markdown
## {iso-now} - combine-outer-reviews
- **Status**: Success
- **Cycle**: {date}
- **Coverage**: {N}/{cycle_size} reviewers processed (sources: {service list})
- **Clusters**: {convergent_count} convergent, {singleton_count} singleton{, divergent_count divergent if any}
- **Tasks upgraded**: {N} (P3→P2: X, P2→P1: Y)
- **Tasks deduplicated**: {N}
- **Output**: [[reviews/outer-review-synthesis-{date}]]
```

### 9. Send Telegram summary

Compose ~80 words covering: cycle date, coverage, top 1–2 convergent findings, count of upgrades, link to the synthesis page on the deployed site (it 404s until the next sync+push — that is expected).

URL pattern: `https://unfinishablemap.org/reviews/outer-review-synthesis-{date}/`

Send via:

```bash
echo "<summary text>" | uv run python -m tools.notify.telegram
```

The helper is a no-op when Telegram credentials aren't configured — fail-safe.

### 10. Commit

```
feat(auto): combine-outer-reviews - synthesize {date} cycle

- {N}/{cycle_size} reviewers
- {convergent_count} convergent clusters, {singleton_count} singletons
- {N} tasks upgraded, {N} deduplicated
```

Use the agent author identity (the standard automation-commit identity).

## Important

- This skill **does not** invoke `/outer-review` on its own output — the synthesis is local meta-analysis, not an external review, and does not need verification of external sources.
- The trigger fires once per cycle. The synthesis file's existence is the idempotence marker; never overwrite a synthesis that already exists. Refuse with a clear message instead.
- Quorum: refuse when fewer than 2 reviews are processed for the cycle. Convergence requires ≥2 voices by definition.
- Disputed claims: a finding that `/outer-review` flagged as disputed (e.g., the reviewer's empirical claim was wrong) does not count toward convergence. Two reviewers making the same wrong empirical claim is correlated error, not convergent signal.
- Do **not** re-prioritise already-completed tasks. Tasks marked `### ✓` in todo.md are out of scope; record the convergence in the synthesis file but leave todo.md alone for them.
- Keep editor-internal vocabulary (reasoning-mode labels, direct-refutation-discipline, etc.) out of the synthesis file's prose where it would feed into article body text. The synthesis file itself is editor-internal — labels are fine in `todo.md` task notes — but if the synthesis recommends refine-draft work, follow the same labels-out-of-articles rule the per-review tasks already follow.
