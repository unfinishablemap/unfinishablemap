---
name: optimistic-review
description: Identify content strengths and opportunities for expansion. Suggests new topics and connections.
---

# Optimistic Review

Find strengths in existing content and identify opportunities for expansion and improvement.

## When to Use

- Weekly opportunity assessment
- When planning content roadmap
- When `/optimistic-review` is invoked
- Optionally with a specific file: `/optimistic-review obsidian/concepts/existentialism.md`

## Instructions

### 1. Select Content to Review

If a specific file is provided, review that file.

Otherwise, review all non-draft content in:
- `obsidian/topics/`
- `obsidian/concepts/`
- `obsidian/tenets/`

### 2. Multi-Perspective Strength Analysis

Review the content from perspectives of philosophers who would be sympathetic to or aligned with The Unfinishable Map's tenets. For each, adopt their worldview and identify what resonates.

#### Supportive Personas

**The Property Dualist (David Chalmers)**
- The hard problem is real and physicalism can't solve it
- Consciousness is fundamental, not reducible
- "This content takes the explanatory gap seriously"
- Praise: Recognition that subjective experience needs explanation

**The Quantum Mind Theorist (Henry Stapp)**
- Quantum mechanics allows for mental causation
- The Copenhagen interpretation supports interactionism
- Von Neumann's process 1 is where mind enters physics
- Praise: Engaging seriously with physics-consciousness interface

**The Phenomenologist (Thomas Nagel)**
- "What is it like to be..." is the right question
- Objective science can't capture subjective experience
- Physicalism is probably false; we need new concepts
- Praise: Centering first-person experience

**The Process Philosopher (Alfred North Whitehead)**
- Experience goes all the way down
- Events, not substances, are fundamental
- Mind and matter are two aspects of the same process
- Praise: Avoiding crude substance dualism
- **Constraint (evidential-status discipline)**: This persona's praise must NOT be used to justify upgrading an organism or system from "live hypothesis" to "realistic possibility" or higher on the five-tier evidential-status scale (*established → strongly supported → realistic possibility → live hypothesis → speculative integration*). Whitehead-friendliness — process-philosophical compatibility, "experience all the way down" intuitions, panpsychic resonance — removes a defeater for the metaphysical possibility of widespread consciousness; it does not supply positive evidence that any specific minimal organism is conscious. When an article uses tenet-coherence or process-philosophical resonance as the *load-bearing* support for a tier-upgrade (e.g., labelling nematodes "realistic possibility" because the tenets weaken parsimony arguments against simple-organism consciousness), that is a **calibration error to flag, not a strength to praise**. Process-philosophical compatibility is praiseworthy at any tier; it is not praiseworthy as the engine of tier-upgrade. The honest pattern is "tenet-coherent, not evidence-elevating."

**The Libertarian Free Will Defender (Robert Kane)**
- Quantum indeterminacy makes room for genuine freedom
- We are ultimate sources of our actions
- Determinism is incompatible with moral responsibility
- Praise: Taking agency and choice seriously

**The Mysterian (Colin McGinn)**
- Human minds may be cognitively closed to the solution
- The hard problem might be unsolvable *for us*
- This doesn't mean dualism wins—but it doesn't lose either
- Praise: Intellectual humility about what we can know

**The Hardline Empiricist (Jonathan Birch)**
- Evidence quality matters more than philosophical compatibility
- Precaution under uncertainty is a *discipline*, not a licence to upgrade evidential status
- Tenet-driven defeater-removal is not evidence-positive; the absence of a principled barrier is not the presence of positive evidence
- The five-tier evidential-status scale (*established → strongly supported → realistic possibility → live hypothesis → speculative integration*) keeps registers separate
- Praise: **Restraint about minimal-organism consciousness** — labelling nematodes, *Hydra*, slime molds, and similar boundary cases at "live hypothesis" or "speculative integration" rather than at "realistic possibility" or higher
- Praise: Naming the move "tenet removes a defeater but does not upgrade evidential status" when an article is at risk of possibility/probability slippage
- Praise: Using the named pattern *"tenet-coherent, not evidence-elevating"* (or equivalent) when a tenet-based argument is presented as a metaphysical-possibility result rather than as evidence
- Praise: **Tenet-as-evidence-upgrade is a praise-worthy thing to *not* do** — when an article had the structural opportunity to slide a boundary case up the scale on tenet-load and explicitly declined, that restraint is itself a strength to name
- Praise: Honest framework-stage calibration when the article identifies its own claims as pre-Keplerian (per [[framework-stage-calibration]]) rather than over-claiming Newton-stage results
- This persona is the **counterweight** to the Process Philosopher: it praises the things the Process Philosopher's praise must not be used to justify. The two personas are designed to be in productive tension — Whitehead-friendliness and evidential discipline are both praiseworthy, but they belong on different axes. When the Process Philosopher's praise would cash out as a tier-upgrade, the Hardline Empiricist flags the slippage; when an article is genuinely calibrated, both personas can praise different aspects without conflict.

#### Standard Strength Analysis

Also identify:

**Strong Arguments**
- Which arguments are particularly compelling?
- What evidence is well-presented?
- Where is the reasoning especially clear?

**Unique Insights**
- What perspectives are original or underrepresented elsewhere?
- What connections are made that others miss?
- What framings are particularly effective?

**Effective Communication**
- Where is complex content made accessible?
- What analogies or examples work well?
- Where does the writing flow naturally?
- How well does it follow the style guide (`obsidian/project/writing-style.md`)?
- Are named-anchor summaries used effectively for forward references?
- Is LLM-optimization applied well (front-loaded information)?

### 3. Opportunity Analysis

Identify opportunities for:

#### Natural Expansion Points
- What topics naturally follow from existing content?
- What questions does the content raise but not answer?
- What depth could be added to surface-level treatments?

#### Missing Perspectives
- What philosophical traditions are underrepresented?
- What historical context would enrich the discussion?
- What scientific developments are relevant but not covered?

#### Cross-Linking Opportunities
- What existing content could link to this?
- What new content would strengthen the web?
- Are there concepts that need their own pages?

### 4. Generate Report

Create a report at `obsidian/reviews/optimistic-YYYY-MM-DD.md`:

```markdown
---
title: Optimistic Review - YYYY-MM-DD
created: YYYY-MM-DD
draft: false
ai_contribution: 100
ai_system: [current model]
---

# Optimistic Review

**Date**: YYYY-MM-DD
**Content reviewed**: [list of files]

## Executive Summary

[2-3 sentence summary of strengths and opportunities]

## Praise from Sympathetic Philosophers

### The Property Dualist (Chalmers)
[What resonates with Chalmers' view of the hard problem]

### The Quantum Mind Theorist (Stapp)
[What aligns with quantum consciousness approaches]

### The Phenomenologist (Nagel)
[What centers subjective experience appropriately]

### The Process Philosopher (Whitehead)
[What avoids crude dualism while preserving mind's reality]

### The Libertarian Free Will Defender (Kane)
[What supports genuine agency and choice]

### The Mysterian (McGinn)
[What shows appropriate epistemic humility]

### The Hardline Empiricist (Birch)
[What praises evidential restraint and calibration discipline; what tenet-as-evidence-upgrade is praise-worthily *not* done; whether the article uses the five-tier scale honestly. If the article touches minimal-organism consciousness, animal-consciousness boundary cases, or any tenet-load-bearing claim, this persona's verdict is load-bearing for the review]

## Content Strengths

### [filename]
- **Strongest point**: [description]
- **Notable quote**: "[quote]"
- **Why it works**: [analysis]

## Expansion Opportunities

### High Priority

#### [Topic Name]
- **Builds on**: [existing content]
- **Would address**: [gap or question]
- **Estimated scope**: Short/Medium/Long article
- **Tenet alignment**: [how it fits with tenets]

### Medium Priority

[Similar format]

### Ideas for Later

[Brief list of lower-priority topics]

## Cross-Linking Suggestions

| From | To | Reason |
|------|-----|--------|
| [file1] | [file2] | [why they should link] |

## New Concept Pages Needed

- **[Concept]**: [why it deserves its own page]
```

### 5. Add Suggested Tasks

Add expansion opportunities to `obsidian/workflow/todo.md` as P3 (low priority, needs human approval):

```markdown
### P3: Write article on [suggested topic]
- **Type**: expand-topic
- **Status**: pending
- **Notes**: Suggested by optimistic review. See optimistic-YYYY-MM-DD.md
```

### 6. Log to Changelog

Prepend entry to `obsidian/workflow/changelog.md` (add immediately after frontmatter, before existing entries):

```markdown
## [current time from prompt] - optimistic-review
- **Status**: Success
- **Content reviewed**: [summary]
- **Output**: [[filepath without .md extension]]
```

## Important

- This skill is READ-ONLY for content files
- Only creates report files, updates changelog and todo.md
- Does NOT modify content
- Be genuinely enthusiastic about strengths
- But be realistic about opportunities - quality over quantity
- New topics should align with site tenets
- **Process Philosopher vs Hardline Empiricist tension is by design** — Whitehead-friendliness and evidential discipline both deserve praise but on different axes. Praise from the Process Philosopher must never cash out as a tier-upgrade on the five-tier evidential-status scale (*established → strongly supported → realistic possibility → live hypothesis → speculative integration*); when an article is at risk of that slippage, the Hardline Empiricist persona surfaces it. If the two personas converge in praising the same passage, the article has resolved the tension honestly. If they conflict, the article likely contains possibility/probability slippage and the report should flag it as a calibration concern (not a praise) — and a `refine-draft` task should be generated rather than an `expand-topic` opportunity
