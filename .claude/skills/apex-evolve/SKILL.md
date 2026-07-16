---
name: apex-evolve
description: Build and maintain apex articles—human-readable synthesis pieces.
context: fork
agent: general-purpose
---

# Apex Evolve

Build and maintain apex articles through creation, evolution, and length management.

## When to Use

- Creating a new apex article from the approved list
- Evolving an existing apex article when source content has changed
- Checking which apex articles need attention

## Invocation

```
/apex-evolve create "Article Title"
/apex-evolve evolve [article-slug]
/apex-evolve check
```

Apex articles come in two shapes: **synthesis** (the default — weaving sources together into a coherent narrative) and **applied** (decision-oriented — given the positions the Map holds, what follows for a specific real-world context). The shape is recorded in the frontmatter field `apex_type: synthesis | applied` (default `synthesis` if absent) and listed in `obsidian/apex/apex-articles.md`. The 10-step evolution process below applies to both; the **Applied Discipline** section below adds extra requirements for applied apex.

## Modes

### Mode 1: `create`

Generate a new apex article from scratch.

**Input**: Article title from the approved list in `obsidian/apex/apex-articles.md`

**Process**:
1. Look up the article in the master list to get source articles and thesis
2. **Check for slug collisions** before creating:
   ```bash
   uv run python scripts/check_slug.py <slug> apex
   ```
   If the check reports a collision, choose a different filename.
3. Read all source articles to understand the material
4. Read `obsidian/project/writing-style.md` for apex article guidelines
5. Synthesize into a narrative that weaves sources together
6. Include the required "Evidence and Dependency" section (see below) classifying the synthesis's main lines of support
7. Target length: 2500-4000 words
8. Create with required frontmatter (see below)

**Output**: New apex article at `obsidian/apex/[slug].md`

### Mode 2: `evolve`

Update an existing apex article when sources have changed.

**Input**: Specific article slug, or omit to auto-select stalest

**Process**: See 10-step evolution process below

**Output**: Improved article + review archive

### Mode 3: `check`

Report which apex articles need evolution.

**Process**:
1. Read all apex articles and their `apex_sources` frontmatter
2. For each source, check its `modified` date against the apex article's effective baseline `max(apex_last_synthesis, last_deep_review)` (see Step 1 for why — `/deep-review` updates `last_deep_review` but not `apex_last_synthesis`, so the bare-field check over-reports drift)
3. Report articles with stale sources, ordered by priority

**Output**: List of articles needing attention with staleness scores

---

## Frontmatter Schema

Apex articles use standard frontmatter plus apex-specific fields:

```yaml
---
title: "Article Title"
created: 2026-01-24
modified: 2026-01-24
human_modified: null
ai_modified: 2026-01-24T00:00:00+00:00
draft: false
topics: []
concepts: []
related_articles: []

ai_contribution: 100
author: null
ai_system: claude-opus-4-5-20251101
ai_generated_date: 2026-01-24
last_curated: null

# Apex-specific fields
apex_type: synthesis  # or "applied" for decision-oriented apex
apex_sources:
  - topics/free-will
  - topics/agent-causation
  - concepts/mental-causation
apex_last_synthesis: 2026-01-24T00:00:00+00:00
apex_thesis: "One-sentence thesis statement"

# Applied-apex only:
apex_decision_context: "AI consciousness assessment"  # what real-world domain this informs
apex_positions_cited:  # the positions the decision turns on; ≥3 required
  - P-Q1
  - P-Q2
  - P-Q9
---
```

---

## Evolution Process (10 Steps)

### Step 1: Select Article

If article specified, use it. Otherwise, auto-select:
1. Read all apex articles in `obsidian/apex/`
2. For each, compute the **effective synthesis baseline**:
   `baseline = max(apex_last_synthesis, last_deep_review)`
   This is the fix for the stale-`apex_last_synthesis` drift bug — `/deep-review` touches an apex's body and updates `last_deep_review` but does **not** update `apex_last_synthesis`, so a naïve scorer keeps re-nominating apex articles whose content has already absorbed every source change via the deep-review. Using the max of the two timestamps treats a recent deep-review as a successful synthesis for staleness purposes.
3. Calculate staleness score:
   - Count sources modified after `baseline`
   - Score = days_since_baseline × changed_source_count
4. Select highest-scoring article. If the top candidate's `baseline` is within the last 7 days, declare a no-op (the work is already done) and exit cleanly without picking a target.

### Step 2: Identify Changed Sources

Compare each source's `modified` date to the effective baseline `max(apex_last_synthesis, last_deep_review)`. List all changed sources. (Same fix as Step 1 — guards against the stale-`apex_last_synthesis` drift artifact where a recent deep-review already absorbed the source updates.)

### Step 3: Read Changed Sources

Read the full content of each changed source to understand new material.

### Step 4: Pessimistic Review

Apply three critical personas:

**Clarity Critic**: Where is the prose unclear, jargon-heavy, or hard to follow? Where does the narrative lose the reader?

**Redundancy Hunter**: What passages repeat information? Where does the article say the same thing twice? What can be cut without losing meaning?

**Narrative Flow Analyst**: Where does the argument structure break down? Are transitions smooth? Does the piece build to its conclusion?

### Step 5: Optimistic Review

Apply three supportive personas:

**Connection Finder**: What new connections from changed sources should be woven in? What synthesis opportunities exist?

**Synthesis Strengthener**: Where can the article better show how pieces fit together? Where is the "so what" unclear?

**Human Reader Advocate**: What would make this more engaging to read? Where does it feel like a reference rather than a narrative?

### Step 6: Length Assessment

1. Count current word length
2. Compare to target range: 2500-4000 words
3. Note whether condensation or expansion is needed

### Step 7: Apply Improvements

**Always do**:
- Fix issues identified by pessimistic review
- Integrate insights from changed sources
- Strengthen synthesis per optimistic review
- Install the "Evidence and Dependency" section if absent; refresh it if the synthesis's lines of support changed (see "Evidence and Dependency Section" below)

**If over 4000 words** (condensation required):
- Remove redundant passages identified by Redundancy Hunter
- Tighten prose: eliminate filler words, combine sentences
- Move detailed explanations to source articles; replace with links
- Remove sections that duplicate what sources already cover well
- Preserve the narrative arc while reducing word count

**If under 2500 words** (expansion needed):
- Expand synthesis sections showing connections between sources
- Add transitions that guide the reader through the argument
- Deepen the narrative arc with richer examples

### Step 8: Update Frontmatter

```yaml
ai_modified: [current UTC timestamp]
apex_last_synthesis: [current UTC timestamp]
```

Adjust `ai_contribution` if human edits were preserved.

### Step 9: Create Review Archive

Create `obsidian/reviews/apex-evolve-[date]-[slug].md` containing:
- Article reviewed
- Changed sources identified
- Pessimistic review findings (3 personas)
- Optimistic review findings (3 personas)
- Length assessment (before/after word counts)
- Summary of changes made

### Step 10: Log and Commit

1. Prepend to `obsidian/workflow/changelog.md` (add immediately after frontmatter, before existing entries):
   ```
   ## [current time from prompt] - apex-evolve
   - **Status**: Complete
   - **Article**: [[article path without .md extension]]
   - **Changed sources**: [count]
   - **Word count**: [before] → [after]
   - **Review**: [[reviews/apex-evolve-date-slug]]
   ```

2. Do **not** create a git commit. Leave file changes uncommitted on
   disk — the orchestrator (`cycle_post.py` for /loop runs,
   `agent-commit` for legacy `evolve_loop.py` runs) commits afterward.
   For manual invocations, run `/agent-commit` or commit by hand.

---

## Article Structure

Apex articles follow this structure:

```markdown
# [Title]

[Opening paragraph stating the integrated thesis - what this synthesis argues]

## [Narrative Section 1]

[Build the argument, drawing from multiple sources]
[Link to sources: "As explored in [[source-article]]..."]

## [Narrative Section 2]

[Continue building, showing connections between ideas]

## [Additional sections as needed]

## Synthesis

[Show how the pieces fit together in a way individual articles don't]
[This is the unique value of the apex article]

## Evidence and Dependency

[Required — see "Evidence and Dependency Section" below. A brief reader-facing
ledger classifying the synthesis's main lines of support.]

## Relation to Site Perspective

[Connect to tenets - required for all articles]

## Source Articles

This apex article synthesizes:
- [[source-1|Source 1 Title]]
- [[source-2|Source 2 Title]]
- ...
```

---

## Evidence and Dependency Section (required)

Every apex article carries a short reader-facing section, `## Evidence and Dependency`, between the Synthesis section and Relation to Site Perspective. Adopted 2026-07-16 from an outer-review recommendation (ChatGPT 5.6 Pro full-site audit, rec #29); convergent with the methodology register's independence discipline.

**Why**: apex pieces are the corpus's most vulnerable point for **confidence amplification**. When agency, altered states, quantum interpretation, subjecthood, and value all draw on the same five tenets, their convergence is one premise package producing mutually compatible outputs — not five independent reasons for those tenets. The ledger makes the dependency structure explicit so the synthesis cannot silently count coherence as evidence.

**Content**: classify each of the article's main lines of support as one of:

- **Externally evidenced** — rests on cited empirical work or external scholarship that holds independently of the Map's framework
- **Independently argued** — a philosophical argument that does not presuppose the tenets (state which premises it does need)
- **Inherited from a tenet** — follows from one or more tenets; name them
- **Inherited from another synthesis** — imported from another apex piece; name it so a reader can trace the chain (and so double-counting across apex articles is visible)
- **Mutually coherent only** — fits the rest of the framework but carries no independent weight; coherence is all it contributes

**Form**: natural prose or a compact list, under ~200 words. Example register: *"The altered-states line is inherited from Tenets 1–3 plus the filter reading; the dissociation studies it cites are externally evidenced but do not by themselves discriminate filter from production accounts. The agency argument is independently argued, though it presupposes that reasons-responsiveness is not exhausted by physical description."* Do not use the phrase "apex article" inside it (media-neutral rule) — "this synthesis" works. Do not present the five category names as a labelled scoreboard; weave them into readable prose.

**Retrofit**: `create` includes the section from the start; `evolve` installs it if absent and refreshes it whenever the support lines change.

---

## Length Management Guidelines

**Target**: 2500-4000 words

**Why this range**:
- Under 2500: Not enough synthesis to justify an apex article
- Over 4000: Becomes unwieldy for human readers; defeats the purpose

**Condensation techniques**:
- "As [[source-article]] explores in detail..." (link instead of repeat)
- Combine related paragraphs
- Remove hedging language that adds words without adding meaning
- Cut examples that illustrate the same point

**Expansion techniques**:
- "This connects to [[other-source]] because..." (show synthesis)
- Add transitional paragraphs between major sections
- Deepen the "why this matters" throughout

---

## Cross-Review Integration

When other skills create or modify content that's an apex source:

1. After `/expand-topic` or `/research-topic` completes
2. Check if the new/modified article is in any apex article's `apex_sources`
3. If yes, add to `obsidian/workflow/todo.md`:
   ```markdown
   - [ ] P2 apex-evolve: [apex-article-slug] — source [modified-article] updated
   ```

This ensures apex articles stay current without manual tracking.

---

## Important

- **Approved subjects only**: Only create apex articles from the master list in `obsidian/apex/apex-articles.md`
- **Human-first**: Unlike topics/concepts, apex articles prioritize narrative flow over LLM-atomic structure
- **Media-neutral language**: Never use the phrase "apex article" in the article content itself. Content may be reproduced in contexts where our internal terminology is unknown. Write as standalone prose.
- **Condense actively**: Evolution must maintain length discipline; don't let articles grow unbounded
- **Link extensively**: Apex articles are synthesis—they should link heavily to source articles
- **Preserve thesis**: Each apex article has a thesis; edits should strengthen it, not dilute it
- **Show the dependency structure**: The "Evidence and Dependency" section is required on every apex article — convergence among tenet-derived lines is not independent confirmation, and the ledger keeps that honest

---

## Applied Discipline (for `apex_type: applied` articles)

Applied apex articles take a decision-relevant context (assessing AI consciousness, clinical-interface ethics, personal philosophy under the Map, etc.) and produce a verdict the Map's framework supports. They are subject to extra discipline beyond synthesis apex:

1. **Cite ≥3 positions**. The `apex_positions_cited` frontmatter field must list at least three position IDs from `obsidian/positions/`. The body should reference them explicitly: "On position P-Q1, the Map holds…" or similar. Without explicit position citation, an applied apex is just an opinion piece.

2. **Surface confidence**. When the article's verdict turns on a position, surface that position's confidence band in-prose, not buried in the frontmatter. A reader should be able to see what the verdict turns on and how confidently. Example: "This verdict depends on P-Q9 (moderate confidence) — were the self-concealing-interface argument to weaken, the implication for AI assessment shifts."

3. **"What this implies for decisions" section**. Required, named exactly that. Two-to-five concrete implications, each stated as a recommendation or evaluation the reader could act on or apply. Not a summary; an output.

4. **Name the decision context**. The `apex_decision_context` frontmatter field is required. The opening paragraph should name the decision context explicitly: "This piece addresses how to assess putative consciousness in current AI systems, given the Map's positions on…"

5. **Honest verdict scope**. Distinguish what the Map's positions actually license from what they merely permit. An applied apex must not over-extend the Map's commitments. If the positions support only a partial verdict, say so; if they leave a decision underdetermined, name the residual uncertainty.

6. **Cascade tagged**. When an applied apex relies on positions whose confidence might shift, note in the body: "If position P-XN is retired or downgraded, this verdict on [aspect] would need re-evaluation." This makes the applied piece self-flagging when positions change.

Applied apex articles are deliberately rare — the goal is 8–15 across the corpus, not 30+. Each one should answer a question a reader would actually ask of the Map.

When creating or evolving an `apex_type: applied` article, run the synthesis 10-step process *and* verify the six points above are satisfied before publishing.
