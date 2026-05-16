---
name: pessimistic-review
description: Critically analyze content for logical gaps, unsupported claims, and potential counterarguments. Does not modify content.
context: fork
agent: general-purpose
---

# Pessimistic Review

Adversarial analysis to find weaknesses in site content. Acts as a critical reviewer looking for flaws.

## When to Use

- Weekly quality review
- Before publishing important content
- When `/pessimistic-review` is invoked
- Optionally with a specific file: `/pessimistic-review obsidian/topics/meaning-of-life.md`

## Instructions

### 1. Select Content to Review

If a specific file is provided, review that file.

Otherwise, select content using this priority:
1. Files with `draft: true` (drafts need review before publishing)
2. Files not yet reviewed (check `obsidian/reviews/` for existing reviews)
3. Oldest content by `modified` date

### 2. Multi-Perspective Critical Analysis

Review the content from multiple philosophical perspectives. For each critic, adopt their worldview and argue as they would.

#### Critic Personas

**The Eliminative Materialist (Patricia Churchland)**
- Consciousness talk is folk psychology destined for elimination
- Neuroscience will replace mental vocabulary entirely
- "What you call 'qualia' is just neural activity you don't understand yet"
- Attack: Dualism is pre-scientific; the explanatory gap will close

**The Hard-Nosed Physicalist (Daniel Dennett)**
- Consciousness is real but not what we think it is
- Introspection is unreliable; we're "zimbos" who think we have qualia
- The hard problem is a confusion, not a discovery
- Attack: You're inflating intuitions into metaphysics

**The Quantum Skeptic (Max Tegmark)**
- Decoherence destroys quantum effects in warm brains in femtoseconds
- There's no time for consciousness to "choose" anything
- Quantum consciousness is wishful thinking dressed in physics
- Attack: The math doesn't work; you haven't done the calculations

**The Many-Worlds Defender (David Deutsch)**
- MWI is the simplest interpretation—it's just the Schrödinger equation
- Indexical questions are confused; there's no "me" to ask "why this branch"
- Your rejection of MWI is anthropocentric bias
- Attack: You're letting intuition override mathematical elegance

**The Empiricist (Karl Popper's Ghost)**
- Unfalsifiable claims aren't scientific
- "Minimal quantum interaction" that's undetectable is metaphysics, not physics
- What experiment could prove you wrong?
- Attack: This is not even wrong

**The Buddhist Philosopher (Nagarjuna)**
- The self you're trying to preserve is itself an illusion
- Consciousness isn't a thing that interacts—it's empty
- Your dualism reifies what should be deconstructed
- Attack: You're clinging to a permanent self that doesn't exist

#### Standard Analysis

Also check for:

**Logical Gaps**
- Are there non-sequiturs in the argument?
- Do conclusions follow from premises?
- Are there missing steps in reasoning?

**Unsupported Claims**
- Are assertions made without evidence or argument?
- Are sources cited for factual claims?
- Are philosophical positions attributed correctly?

**Internal Contradictions**
- Does the content contradict itself?
- Does it conflict with other site content?
- Does it conflict with The Unfinishable Map's tenets?

**Language Issues**
- Is language overly strong without justification? ("clearly," "obviously," "must be")
- Are there weasel words hiding weak arguments?
- Is the tone appropriately uncertain where warranted?

**Style Guide Violations** (see `obsidian/project/writing-style.md`)
- Is important information front-loaded for LLM truncation resilience?
- Are there undefined forward references without named-anchor markers?
- Is the "Relation to Site Perspective" section present and substantive?
- Is redundant background minimised (focus on what's novel)?

**Reasoning-Mode Failures** (see [[direct-refutation-discipline]])

When the article replies to a named opponent, evaluate the reply against the discipline. The classification is editor-internal — the article must engage the opponent in natural journal-quality prose, never naming the modes. Failures fall into two families:

*Substitution failures (the engagement claims a mode it cannot do):*

- **Boundary-substitution** — the article rejects the opponent by appealing to tenet incompatibility, dressed as if it refuted the opponent inside the opponent's framework. *Critical issue.* The reply must either be upgraded (find the in-framework argument or the unsupported-foundational-move identification, where one is feasible) or honestly downgraded to natural framework-boundary marking — *"this runs counter to the Map's foundational commitments and is honestly noted as such, not refuted within X's framework"*.
- **Missed unsupported-move identification** — the opponent's framework helps itself to a foundational move it has not earned by its own standards (materialism stipulating "computation produces experience" without specifying the bridge; functionalism asserting "functional pattern is what matters" without arguing why; eliminativism declaring folk-psychology terms non-referential without specifying the reduction). The article fails to name the unmet standard the opponent's own commitments demand. *Medium issue.*
- **In-framework argument that actually appeals to Map commitments** — the article presents a passage as engaging the opponent on their own terms, but the actual reasoning depends on Map-specific tenets. The reply does not earn the disagreement inside the opponent's framework. *Critical issue.*

*Label-leakage failures (editor-vocabulary in article prose):*

- **Forbidden labels in prose** — the article contains any of `direct-refutation-feasible`, `unsupported-jump callout`, `unsupported-jump`, `bedrock-perimeter` (and variants), `mode-mixed`, `mixed-with-distinct-roles`, `tenet-register move`, `Engagement classification:`, or `per [[direct-refutation-discipline]]` as meta-commentary. *Critical issue.* These are editor-vocabulary; they belong in the changelog and editor's notes, never in the article. The substance the labels were marking should remain, expressed in natural language per [[writing-style|the writing-style guide]].
- **Bold-headed `**Evidential status:**` callouts** — disrupts article flow with editor-vocabulary. *Critical issue.* Convert to inline natural-language phrasing at section close (*"the case is open but unsettled"*, *"contested but real"*).

Three independent outer reviewers (2026-05-03 ChatGPT, 2026-05-04 ChatGPT, 2026-05-04 Claude) converged on boundary-substitution as the catalogue's primary structural weakness; label leakage is the failure mode that came from over-eager early implementation of the discipline. This check catches both. The fix is always to preserve the philosophical substance and remove the editor-vocabulary or substitution dressing.

**Altered-State Symmetry** (see [[project/calibration-audit-triple]] Audit Two)

When the article frames altered-state evidence around filter / transmission theory, audit the article's handling of the altered-state cluster for *convergence double-counting*. The failure mode the 2026-05-14 outer-review surfaced on `psychedelics-and-the-filter-model.md` (and that required four refine-passes before the symmetry section was installed): the article cites a *supportive cluster* (psychedelics, near-death experiences, terminal lucidity, contemplative cessation, mystical experience, out-of-body) as multiple independent confirmations of filter framing without engaging the *disruptive cluster* (anaesthesia, slow-wave sleep, brain damage, persistent vegetative state, dementia) the framing must also accommodate. The discipline should catch this earlier than four refine-passes.

For each candidate article, run these three checks (the audit logic also lives at `tools/curate/altered_state_symmetry.py`; pessimistic-review applies it as a manual checklist, not as automation):

1. **Supportive-cluster gate.** Does the article cite ≥2 items from the supportive cluster (psychedelics / psilocybin / DMT / LSD / ego-dissolution; near-death experience / NDE; terminal lucidity / paradoxical lucidity; contemplative cessation / nirodha-samapatti / jhana; mystical experience / unitive experience; out-of-body / OBE)? If no, the audit does not apply.
2. **Disruptive-cluster engagement.** If supportive-cluster gate passes, does the article cite at least one item from the disruptive cluster (anaesthesia / propofol / ketamine / xenon; slow-wave sleep / NREM / dreamless sleep; brain damage / TBI / lesion; persistent vegetative state / PVS / minimally conscious state; dementia / Alzheimer's / neurodegeneration)? If no — *critical issue* — flag the article for a `refine-draft` pass that installs the symmetric accommodation work. The supportive cluster is being treated as *N* independent confirmations when each case contributes the same evidential move; the disruptive cluster contributes the parallel move and is missing.
3. **Symmetry-acknowledgment.** If the disruptive cluster *is* cited, does the article *explicitly name* the symmetric accommodation work both framings owe? Look for natural-language markers: *symmetric / symmetry; structurally identical; parallel accommodation / move / burden; the same move is available to production theorists; both framings / accounts / readings; one pattern, not five / many; cluster carries the evidential weight of one; cannot honestly be cited as multiple independent confirmations; double-counting*. If the disruptive items appear only as a footnote without the explicit parallel-accommodation framing — *medium issue* — flag for `refine-draft`.

The discipline is not "balance every claim with a counter-claim" — it is "present the dialectical position as a single position, not as a count of independent confirmations." A filter-framed article whose argumentative load rests on convergence-across-cases must audit that the convergence is honest: the cluster carries the evidential weight of *one* pattern, and the production framing has access to the same accommodation move applied to the disruptive cases. See `concepts/altered-states-of-consciousness.md` and `topics/anaesthesia-and-the-consciousness-interface.md` for the corpus articles that establish how the Map performs the disruptive-cluster accommodation; the audited article should inherit that accommodation rather than ignore it.

When this check fires, add a `refine-draft` task whose notes list (a) which supportive-cluster items are cited, (b) which disruptive-cluster items are missing (or under-engaged), and (c) which symmetry-acknowledgment marker is to be installed in the refine pass. The companion `refine-draft` skill's *Altered-State Symmetry Remediation* section specifies the corresponding fix.

### 3. Generate Report

Create a report at `obsidian/reviews/pessimistic-YYYY-MM-DD.md`:

```markdown
---
title: Pessimistic Review - YYYY-MM-DD
created: YYYY-MM-DD
draft: false
ai_contribution: 100
ai_system: [current model]
---

# Pessimistic Review

**Date**: YYYY-MM-DD
**Content reviewed**: [filename or list]

## Executive Summary

[2-3 sentence summary of main findings]

## Critiques by Philosopher

### The Eliminative Materialist
[What Patricia Churchland would say about this content]

### The Hard-Nosed Physicalist
[What Daniel Dennett would say]

### The Quantum Skeptic
[What Max Tegmark would say]

### The Many-Worlds Defender
[What David Deutsch would say]

### The Empiricist
[What a Popperian would say about falsifiability]

### The Buddhist Philosopher
[What Nagarjuna would say about self and emptiness]

## Critical Issues

### Issue 1: [Title]
- **File**: [filename]
- **Location**: [section or quote]
- **Problem**: [description]
- **Severity**: High/Medium/Low
- **Recommendation**: [how to address]

## Counterarguments to Address

### [Topic/Claim]
- **Current content says**: [summary]
- **A critic would argue**: [counterargument]
- **Suggested response**: [how to address]

## Unsupported Claims

| Claim | Location | Needed Support |
|-------|----------|----------------|
| [claim] | [file:section] | [what's needed] |

## Language Improvements

| Current | Issue | Suggested |
|---------|-------|-----------|
| "clearly shows" | Too strong | "suggests" |

## Strengths (Brief)

Despite criticisms, note what works well to preserve during revisions.
```

### 4. Add Actionable Items

If significant issues are found, add tasks to `obsidian/workflow/todo.md`:

```markdown
### P2: Address gaps in [filename]
- **Type**: refine-draft
- **Status**: pending
- **Notes**: Pessimistic review found [brief description]. See pessimistic-YYYY-MM-DD.md
```

### 5. Log to Changelog

Prepend entry to `obsidian/workflow/changelog.md` (add immediately after frontmatter, before existing entries):

```markdown
## [current time from prompt] - pessimistic-review
- **Status**: Success
- **Content reviewed**: [summary]
- **Output**: [[filepath without .md extension]]
```

## Important

- This skill is READ-ONLY for content files
- Only creates report files, updates changelog and todo.md
- Does NOT modify the content itself
- Be genuinely critical - the goal is to find real weaknesses
- But be constructive - always suggest how to improve
