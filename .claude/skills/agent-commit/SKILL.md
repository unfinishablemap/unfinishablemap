---
name: agent-commit
description: Analyze changes and create a meaningful commit with agent authorship. Internal skill for evolve_loop.
---

# Agent Commit

Creates a git commit with meaningful message based on skill output and actual file changes.

## When to Use

This skill is called automatically by `evolve_loop.py` after a content-modifying skill completes. It is not intended for manual invocation.

## Input

You will receive:
1. The name of the skill that just ran
2. A summary or excerpt of that skill's output

## Instructions

### 1. Check for Changes

Run `git status --porcelain` to see if there are uncommitted changes.

If there are no changes, output "No changes to commit" and stop.

### 2. Analyze the Changes

Run `git diff` (or `git diff --cached` if files are staged) to understand what was modified.

Focus on:
- Which files were changed (especially content files in `obsidian/`)
- The nature of the changes (new content, edits, deletions)
- Key themes or topics affected

### 3. Generate Commit Message

Create a concise, informative commit message following this format:

```
<type>(<skill>): <summary>
```

Where:
- `<type>` is one of: `feat`, `fix`, `refine`, `research`, `chore`
- `<skill>` is the skill name (e.g., `deep-review`, `condense`, `expand-topic`)
- `<summary>` describes WHAT was done and to WHICH file(s)

**Good examples:**
- `refine(deep-review): improve clarity in free-will.md`
- `feat(expand-topic): add article on quantum decoherence`
- `refine(condense): reduce qualia.md from 8500 to 2100 words`
- `research(research-topic): notes on Penrose-Hameroff theory`
- `chore(replenish-queue): add 3 tasks for consciousness topics`

**Bad examples:**
- `auto(deep-review): Automated execution` (too vague)
- `Updated files` (no context)
- `Changes from deep-review skill` (doesn't say what)

### 4. Create the Commit

Stage all changes and commit with agent authorship:

```bash
git add -A
git commit --author "unfinishablemap.org Agent <agent@unfinishablemap.org>" -m "<message>"
```

### 5. Output the Result

Output the commit hash and message so the calling system can log it.

## Important

- Keep commit messages under 72 characters for the summary line
- Focus on the "what" and "which file" - the skill name already tells us "how"
- If multiple files changed, mention the primary one and note others exist
- Never include time estimates or subjective assessments in commit messages
