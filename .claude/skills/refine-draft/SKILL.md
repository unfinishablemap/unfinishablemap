---
name: refine-draft
description: Improve the quality of draft content. Runs review and applies improvements while preserving voice.
---

# Refine Draft

Improve existing draft content through review and targeted improvements.

## When to Use

- When a todo item is type `refine-draft`
- When `/refine-draft [filepath]` is invoked
- Weekly draft refinement runs

## Instructions

### 1. Select Draft to Refine

If a specific file is provided, use it.

Otherwise, select using this priority:
1. Drafts flagged for refinement in todo.md
2. Oldest draft by `created` date
3. Drafts with lowest quality scores (if reviewed)

### 2. Check for Review Context

If the task context includes a `Review file` field (e.g., from an outer review):

1. Read the referenced review file (e.g., `reviews/outer-review-2026-01-28-*.md`)
2. Find the specific issue being addressed in the task notes
3. Check the Verification Notes section to understand what was confirmed
4. Use the reviewer's specific guidance for the fix

This provides crucial context for targeted fixes rather than general refinement.

### 3. Run Quality Review

Use the existing review tool:
```bash
uv run python scripts/curate.py review [filepath]
```

This provides:
- Overall quality score (1-10)
- Strengths list
- Improvements list with priorities
- Missing concepts

### 3.5 Attribution Accuracy Check (Required for Source-Based Articles)

If the article is based on a specific source (research paper, philosopher's work), run this checklist:

#### Misattribution Check
- [ ] Are all claims attributed to the source actually in the source?
- [ ] Did we attribute framework/constraints to the right author? (e.g., "five constraints" are Saad's, not Chalmers')
- [ ] Did we claim the author discusses something they don't? (e.g., "Many-Worlds" when they don't mention it)

#### Qualifier Preservation Check
- [ ] Are crucial qualifiers preserved? ("default causal profile" not just "causal profile")
- [ ] Did we change "X or at least Y" to just "X"?
- [ ] Did we change "some" to "all" or "wherever"?

#### Position Strength Check
- [ ] Did we present exploratory positions as commitments?
- [ ] Did we claim shared commitments that aren't shared? (e.g., "shares our rejection of MWI" when author expresses "sympathy for MWI")
- [ ] Did we use "solves" or "answers" when source uses "addresses" or "explores"?

#### Source/Map Separation Check
- [ ] Is source exposition clearly separated from Map interpretation?
- [ ] Are Map-specific arguments (tenets, quantum interactionism) clearly labeled as such?
- [ ] Did we inject Map arguments as if they came from the source?

#### Self-Contradiction Check
- [ ] Did we claim something is "not required" but also "required" in different sections?
- [ ] Are claims about the theory's commitments consistent throughout?

**If any check fails, fix the issue before proceeding to other improvements.**

### 3.6 Reasoning-Mode Classification (Required for Articles That Reply to Named Opponents)

When the article replies to a named opponent (Duch, Frankish, Dennett, Chalmers, the materialist, the functionalist, etc.), classify the reply by reasoning mode before editing. See [[direct-refutation-discipline]] for the full discipline. **The classification is editor-internal — it goes in the changelog, not in the article body.** The article must engage the opponent in natural journal-quality prose.

Three primary modes plus a mixed sequence (editor's diagnostic vocabulary, not article vocabulary):

- **Mode One — defective on its own terms.** Internal-to-the-opponent argument is available; the reply earns the disagreement inside the opponent's framework. The opponent could in principle accept the criticism without abandoning their commitments.
- **Mode Two — unsupported foundational move.** The framework has helped itself to a foundational move it has not earned by its own standards. The reply uses the opponent's own commitments to mechanism, evidence, or argument. Examples: materialism stipulating "computation produces experience" without specifying the bridge; functionalism asserting "functional pattern is what matters" without arguing why it would generate qualia; eliminativism declaring folk-psychology terms non-referential without specifying the reduction.
- **Mode Three — framework-boundary marking.** The disagreement is at the framework boundary. The reply notes the disagreement honestly without claiming to have refuted the opponent inside their own framework.
- **Mixed.** Most full engagements warrant a sequence: foundational-move identification opens, in-framework argument deepens, boundary-marking declares the residue. The prose flows naturally between the moves.

For each named-opponent reply:

1. **Classify** the engagement as one of the modes (or which mode applies to which subsection for mixed engagements). This is for your working knowledge.
2. **Verify the mode is honest** — Mode One must derive a contradiction or empirical inadequacy from the opponent's *own* commitments; Mode Two must invoke a standard the opponent's framework actually endorses; Mode Three must explicitly note the framework-boundary disagreement rather than dressing it as refutation.
3. **Catch boundary-substitution** — if the article currently presents tenet-incompatibility as if it refuted the opponent inside the opponent's framework, this is the failure mode the discipline names. Either upgrade the engagement (find the in-framework argument or the unsupported-move identification) or downgrade the language (note the framework-boundary disagreement honestly).
4. **Apply the fix in natural prose.** Use the patterns in [[writing-style|the writing-style guide]]'s "Engaging Opponents in Journal-Quality Prose" section. Useful natural-language phrasings include *"X helps itself to Y without specifying how"*, *"this runs counter to the Map's foundational commitments and is honestly noted as such, not refuted within X's framework"*, *"X's framework cannot accommodate the measurement on its own terms"*. **Do not name the modes in the article.**
5. **Record the classification in the changelog only.** Format: *"engagement with [opponent]: Mode N; [one-sentence justification]"*. For mixed engagements, list each subsection's mode. **Never write the mode label into the article body.**

**Forbidden in article prose** (these are editor-vocabulary; if any appear in the article, remove and replace with natural prose):

- `direct-refutation-feasible`, `unsupported-jump callout`, `unsupported-jump`, `bedrock-perimeter`, `mode-mixed`, `mixed-with-distinct-roles`, `tenet-register move`, `Engagement classification:`
- The phrase `per [[direct-refutation-discipline]]` as meta-commentary in prose
- Bold-headed `**Evidential status:**` callouts (use inline natural-language phrasing instead — see [[writing-style]])

The discipline does not require every named opponent to receive in-framework refutation. Some disagreements are genuinely bedrock; saying so honestly is part of the discipline. The failure mode is *substitution* — letting boundary-marking silently stand in for an argument that was available. The other failure mode is *label leakage* — exposing the editor's diagnostic vocabulary in article prose. Both are correctable in this pass.

### 4. Apply Improvements

Based on the review, make targeted improvements following `obsidian/project/writing-style.md`.

#### Clarity
- Simplify convoluted sentences
- Define jargon on first use
- Improve paragraph flow

#### Structure
- Verify opening summary front-loads key information
- Check for undefined forward references (use named-anchor pattern)
- Ensure "Relation to Site Perspective" section exists
- Add transitions between sections

#### Style Guide Compliance
- Important information front-loaded (truncation resilience)
- Named-anchor summaries for forward references
- Standard background minimised (focus on what's novel)
- H2/H3 headers are descriptive and aid navigation

#### Tenet Alignment
- Ensure content doesn't contradict tenets
- Add explicit connections to tenets where natural
- Address obvious objections

### 5. Check for Description

If the article lacks a `description` field in frontmatter:
- Add one: 150-160 characters
- Emphasize human+AI collaboration, iterative refinement, and pursuit of truth
- Avoid generic phrases—make it distinctive to The Unfinishable Map's approach
- Example style: "AI-assisted exploration of X—continuously refined to get closer to the truth."

### 6. Preserve Voice

When refining:
- Keep the original style and approach
- Don't over-edit - targeted improvements only
- Preserve unique phrasings that work
- Maintain the original argument structure unless flawed

### 7. Update Frontmatter

After refinement:

```yaml
ai_modified: YYYY-MM-DDTHH:MM:SS+00:00  # Update timestamp
```

If the original was human-authored (`ai_contribution: 0`), update to mixed:
```yaml
ai_contribution: 20  # Or appropriate percentage based on changes
```

### 8. Document Changes

Add a comment at the end of the file (to be removed by human):

```markdown
<!-- AI REFINEMENT LOG - YYYY-MM-DD
Changes made:
- [Change 1]
- [Change 2]
- [Change 3]

Based on review scoring X/10.
Key improvements: [summary]

This log should be removed after human review.
-->
```

### 9. Update Todo

If this was a todo item, mark it complete.

If significant issues remain, create a new todo:
```markdown
### P2: Further refine [filename]
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Initial refinement done but [remaining issues]
```

### 10. Log to Changelog

Prepend to `obsidian/workflow/changelog.md` (add immediately after frontmatter, before existing entries):

```markdown
## [current time from prompt] - refine-draft
- **Status**: Success
- **File**: [[filepath without .md extension]]
- **Original score**: X/10
- **Changes**: [brief list]
- **Published**: yes
```

### 11. Commit

Create a git commit with message:
```
refine(content): Improve [filename]

Changes:
- [Change 1]
- [Change 2]

Changes applied directly.
```

## What NOT to Do

- Don't change the fundamental argument unless it's flawed
- Don't add unnecessary content to pad length
- Don't remove content without clear reason
- Don't change `draft: false` to `draft: true` on published content
- Don't make stylistic changes just for the sake of change

### Attribution Errors to Avoid

These errors have been identified in outer reviews and must be fixed when found:

- **Don't attribute framework X to author Y** when it's actually from author Z (e.g., "five constraints" are Saad's, not Chalmers')
- **Don't claim an author discusses topic X** when they don't mention it (e.g., Saad doesn't discuss Many-Worlds)
- **Don't drop crucial qualifiers** from definitions (e.g., "default causal profile" → "causal profile" loses essential meaning)
- **Don't strengthen hedged claims** (e.g., "explores" → "argues"; "sympathy for X" → "rejects alternatives to X")
- **Don't present Map interpretations as source claims** — keep Channel A (source) and Channel B (Map) separate
- **Don't claim shared commitments that aren't shared** (e.g., claiming author "shares our rejection of MWI" when they express sympathy for MWI)

## Important

- ALWAYS update `ai_modified` timestamp
- ALWAYS document changes made
- Preserve the original author's voice
