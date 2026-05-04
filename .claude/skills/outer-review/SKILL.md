---
name: outer-review
description: Commission and process external AI analysis to reduce blind spots. Manual invocation only.
---

# Outer Review

Process an external AI review to extract actionable tasks. The human commissions the external review and saves the raw output; this skill processes it.

## When to Use

- When `/outer-review [filepath]` is invoked with a new outer review file
- After a human has commissioned and saved an external AI analysis

## Why External Review Matters

The Unfinishable Map's content is primarily generated and reviewed by Claude-based systems. This creates risk of:

- **Confirmation bias**: The reviewing system shares assumptions with the generating system
- **Blind spot persistence**: Gaps in Claude's knowledge propagate undetected
- **Style homogenization**: Content converges toward patterns Claude favors
- **Coherence inflation**: Arguments seem stronger than they are because the reviewer finds them compelling for the same reasons the writer did

External AI systems (GPT-4+, Gemini, etc.) have different training, different biases, and different blind spots. Their disagreements are informative even when wrong.

## Prerequisites

The human must:

1. Commission a review from an external AI system (ChatGPT, Gemini, etc.)
2. Save the raw output to `obsidian/reviews/outer-review-YYYY-MM-DD-[system-slug].md`
3. Add basic frontmatter (or leave for this skill to add)

## Instructions

### 1. Read the Review File

The filepath is provided as an argument: `/outer-review obsidian/reviews/outer-review-2026-01-15-site-chatgpt-5-2-pro.md`

Read the file and assess its current state.

### 2. Add/Fix Frontmatter

Ensure the file has proper frontmatter:

```yaml
---
title: "Outer Review - [System Name]"
created: YYYY-MM-DD
modified: YYYY-MM-DD
human_modified: null
ai_modified: YYYY-MM-DDTHH:MM:SS+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[project]]"
ai_contribution: 90
author: [Human who commissioned it]
ai_system: [external-system-id]
ai_generated_date: YYYY-MM-DD
last_curated: null
---

**Date**: YYYY-MM-DD
**Reviewer**: [System name and version]
**Type**: Outer review (external AI analysis)

## About This Review

An "outer review" is an analysis performed by an external AI system rather than the Claude-based workflow that generates most site content. This provides an independent perspective, reducing the risk of self-reinforcing blind spots.

[External system's review content follows...]
```

**If the file already has `outer_review_status: collected` in its frontmatter** (this means it was produced by an automated collect skill like `collect-chatgpt-review`), preserve the commission-time fields and only update processing fields:

- **Preserve**: `title`, `created`, `ai_system`, `ai_generated_date`, `outer_review_conversation_url`, `outer_review_extraction_method` — these record provenance and must not be overwritten.
- **Update**: `ai_modified` (set to now), `modified` (today's date), `topics` (populate from review content), `concepts` (populate from review content), `last_curated` (set after curation), `description` (refine from auto-generated placeholder to a hand-tuned summary).
- **Add** `outer_review_status: processed` after the skill completes its task generation, so future re-runs can detect that processing already happened.

The pre-seeded body already has **Date**, **Reviewer**, **Type**, **About This Review**, **Prompt**, and **Reply** sections in the right shape; do not rewrite them.

### 3. Normalize Links

External AI systems often produce footnote-style markdown links like `([Source][1])` with reference definitions at the end. Run the link normalization script:

```bash
uv run python scripts/normalize_review_links.py obsidian/reviews/outer-review-YYYY-MM-DD-*.md
```

This script:
- Removes self-references to unfinishablemap.org (just noise)
- Converts external footnote refs to inline links like `(See [Chalmers](url))`
- Adds an "External Sources" section with properly labeled academic references
- Preserves inline links that are already well-formatted

Also convert any Map URLs to internal wikilinks:

- `https://unfinishablemap.org/tenets/` → `[[tenets]]`
- `https://unfinishablemap.org/topics/free-will/` → `[[free-will]]`
- `https://unfinishablemap.org/concepts/qualia/` → `[[qualia]]`

### 4. Verify Claims Against Sources

**External AI reviewers can also be wrong.** Before accepting criticism, verify key claims by fetching the cited sources.

For each significant claim the reviewer makes about what an author says:

1. **Identify the source**: Look for URLs in the External Sources section or inline citations
2. **Fetch the source**: Use WebFetch to retrieve the actual paper/article
3. **Check the claim**: Does the source actually say what the reviewer claims?

**What to verify:**
- Direct quotes or paraphrases of philosophers' positions
- Claims about what a paper "explicitly states" or "clearly shows"
- Attributions of specific arguments or frameworks to specific authors
- Claims that the Map misrepresents a source

**Add verification notes to the review file:**

After verifying, add a `## Verification Notes` section to the review file documenting what you checked:

```markdown
## Verification Notes

**Verified claims:**
- ✓ Reviewer correctly notes that Chalmers treats organizational invariance as contingent, not necessary (confirmed in "Absent Qualia" paper)
- ✓ Five constraints framework is indeed from Saad (2025), not Chalmers & McQueen

**Unverified claims:**
- ? Could not access Springer PDF to confirm Saad's exact formulation

**Disputed claims:**
- ✗ Reviewer says Chalmers "explicitly endorses" Many-Worlds—but the cited passage says "considerable sympathy," which is weaker than endorsement
```

This prevents blindly accepting external criticism that may itself be inaccurate.

### 5. Evaluate Review Quality

Read through the review and categorize findings, taking verification results into account:

**High value findings** (verified or plausible):
- Logical gaps not previously noticed
- Counterarguments not addressed
- Inconsistencies between pages
- Missing connections that should exist
- Novel framings of existing positions
- Misattributions confirmed by source checking

**Lower value findings:**
- Objections already addressed elsewhere
- Misunderstandings of the position
- Requests to adopt a different position entirely
- Style preferences that don't affect clarity
- **Claims that failed verification** (the reviewer was wrong)

### 6. Generate Tasks

For high-value findings, create tasks in `obsidian/workflow/todo.md`:

```markdown
### P1: [Specific issue from outer review]
- **Type**: [research-topic | expand-topic | refine-draft | cross-review]
- **Notes**: From outer review YYYY-MM-DD. [Brief description of the issue and why it matters]
- **Review file**: `reviews/outer-review-YYYY-MM-DD-[slug].md`
- **Source**: outer-review
- **Generated**: YYYY-MM-DD
```

**Important**: Always include the `Review file` field with the path to the outer review. This allows the refine-draft skill to read the full context and verification notes when addressing the issue.

**Direct-refutation remit**: When a finding identifies an opponent-engagement weakness — perimeter-substitution, missed unsupported-jump callout, weak refutation, or unlabelled mixed engagement — the generated task carries the [[direct-refutation-discipline]] remit. Add this language to the task notes:

> Apply the direct-refutation discipline. Classify the engagement as direct-refutation-feasible, unsupported-jump, bedrock-perimeter, or mixed-with-distinct-roles. If a direct refutation or unsupported-jump callout is feasible, install it; if the disagreement is genuinely bedrock, mark the perimeter explicitly using the named pattern *the Map's tenets exclude X; the Map does not refute X inside X's framework*. Record the classification in the changelog.

The remit makes the failure mode visible and pre-classifies the work the refine-draft / deep-review pipeline must do. Three independent outer reviewers (2026-05-03 ChatGPT, 2026-05-04 ChatGPT, 2026-05-04 Claude) converged on perimeter-substitution as a structural weakness; tasks generated from outer-review findings carry the discipline forward.

Priority guidance:
- **P1**: Logical errors, internal contradictions, unaddressed strong objections, perimeter-substitution where direct refutation or unsupported-jump callout is available
- **P2**: Missing connections, expansion opportunities, clarity improvements, unlabelled mixed engagements
- **P3**: Style suggestions, minor enhancements

### 7. Log to Changelog

Prepend to `obsidian/workflow/changelog.md` (add immediately after frontmatter, before existing entries):

```markdown
## [current time from prompt] - outer-review
- **Status**: Success
- **Reviewer**: [System name]
- **File**: [[filepath without .md extension]]
- **Claims verified**: [count]
- **High-value findings**: [count]
- **Tasks generated**: [count with priorities]
```

### 8. Send Telegram summary

Send a short ~100-word summary to the project's Telegram chat so the operator sees the review without having to check the repo. Includes a web link to the rendered report — that link may 404 until the next sync+push (this is expected; the link is for after the deploy lands).

URL pattern: `https://unfinishablemap.org/reviews/<filename-without-md>/`

Compose a summary covering:
- Reviewer display name + date
- Headline finding (1–2 sentences from the review's verdict / TL;DR)
- Tasks generated, with priority breakdown
- Convergent finding flag (1 line) if this review echoes a prior outer review's structural critique
- The web link

Example shape (~100 words):

```
🤖 Outer Review: ChatGPT 5.5 Pro · 2026-05-04

Headline: The Map's Duch integration is substantive philosophical engagement
but tenet-protective — the deepest reply is incompatibility, not refutation.

Tasks generated: 5 (P1: 3, P2: 2)
Convergent with 2026-05-03 review: tenet-perimeter reasoning surfaces again.

🔗 https://unfinishablemap.org/reviews/outer-review-2026-05-04-chatgpt-5-5-pro/
```

Send it via:

```bash
echo "<summary text>" | uv run python -m tools.notify.telegram
```

Or pass the text via `--text "<summary>"` if you prefer not to pipe. The helper is a no-op if `TELEGRAM_BOT_TOKEN` / `TELEGRAM_CHAT_ID` aren't configured — fail-safe, no error.

### 9. Commit

Create a git commit:

```
feat(auto): outer-review - process [system name] analysis

- Identified [N] actionable issues
- Generated [N] tasks (P1: X, P2: Y, P3: Z)
```

## Evaluating Impact (After Tasks Complete)

After tasks from an outer review have been completed, evaluate the review's value:

1. **Count completed tasks**: How many issues were addressed?
2. **Assess depth**: Did the review surface deep insights or obvious issues?
3. **Track new content**: What articles/sections resulted from the review?
4. **Note patterns**: What kinds of issues does this external system catch that internal review misses?

This helps calibrate future review frequency and system selection.

## Important

- This skill requires manual invocation with a filepath argument
- The human commissions and saves the external review; this skill processes it
- External systems may have different biases—their criticism isn't automatically correct
- The goal is diverse perspective, not consensus
- Some external criticism will be based on misunderstanding—that's expected
- Focus on actionable findings that improve content quality
