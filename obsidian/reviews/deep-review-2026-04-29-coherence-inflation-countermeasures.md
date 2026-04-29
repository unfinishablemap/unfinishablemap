---
title: "Deep Review - Coherence Inflation Countermeasures"
created: 2026-04-29
modified: 2026-04-29
human_modified: null
ai_modified: 2026-04-29T14:27:00+00:00
draft: false
topics: []
concepts:
  - "[[bedrock-clash-vs-absorption]]"
related_articles:
  - "[[coherence-inflation-countermeasures]]"
  - "[[bedrock-clash-vs-absorption]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-7
ai_generated_date: 2026-04-29
last_curated: null
---

**Date**: 2026-04-29
**Article**: [[coherence-inflation-countermeasures|Coherence Inflation Countermeasures]]
**Previous review**: Never (first deep review)
**Cross-review context**: Considering [[bedrock-clash-vs-absorption]] insights

## Pessimistic Analysis Summary

### Critical Issues Found

- **Missing `description` frontmatter**: Required per writing-style guide. Resolution: Added a 160-character description emphasising detection, confidence calibration, and editorial discipline.
- **Missing engagement with bedrock-clash discipline**: The [[bedrock-clash-vs-absorption]] article explicitly designates itself as feeding back into coherence-inflation countermeasures ("silently absorbed objections compound coherence inflation; explicitly preserved clashes resist it"). The article had no countermeasure for the editorial-level absorption-by-default vector. Resolution: Added Countermeasure 8: Absorb-vs-Clash Discipline at the Article Level.

### Medium Issues Found

- **Countermeasure 4 (external reviews) had no link to absorb-vs-clash decision**: External findings face the same absorption pressure as internal findings. Resolution: Added inline cross-reference in C4 noting findings face the absorb-vs-clash decision before any edit.
- **No cross-link to bedrock-clash-vs-absorption** in Further Reading or related_articles. Resolution: Added to both.
- **Metric table didn't track absorb-vs-clash discipline adherence**. Resolution: Added a new metric row.

### Counterarguments Considered

- **Eliminative materialist (Churchland)**: Would reject the evidence/coherence distinction as folk-epistemology. **Bedrock disagreement** — the article correctly assumes a non-eliminativist epistemic frame; absorbing this would require dropping the article's premise.
- **Hard-nosed physicalist (Dennett)**: Coherence is necessary for understanding; "coherence inflation" framing risks treating coherence per se as bad. Article already addresses this implicitly ("simplicity and coherence are not sufficient for truth"); not a critical flaw, but a clarification opportunity. **Deferred** — the lead and "Relation to Site Perspective" already make the necessary distinction.
- **Popper (Empiricist)**: Why these specific freshness thresholds (3 years for neuroscience, 10 for philosophy)? They are stipulative rather than empirically derived. **Acknowledged but deferred** — the article presents them as policy choices, not empirical findings; tightening would require external evidence on field velocities that is itself a research task.
- **Madhyamaka (Nagarjuna)**: The article reifies its own categories (evidence/speculation, primary/secondary). **Bedrock disagreement** — the article-level Madhyamaka response is the same as in voids work: the operational-fiction frame is the recognised non-reification.

### Unsupported Claims

- The freshness thresholds in Countermeasure 6 (3 years for neuroscience, 10 for philosophy) are stipulative. The article does not claim empirical support for these specific numbers; they are presented as policy. Acceptable as policy thresholds with the existing framing.

## Optimistic Analysis Summary

### Strengths Preserved

- **Front-loaded LLM-first lead**: "Because The Unfinishable Map is intentionally a coherent worldview... this failure mode is not hypothetical; it's the default." Preserved verbatim.
- **Seven-countermeasure structure** with consistent policy/implementation/pattern format. Preserved; new Countermeasure 8 follows the same template.
- **Concrete Tegmark/Hameroff example** in Countermeasure 3. Preserved.
- **Metric table format** with target/warning columns. Preserved and extended with new row.
- **"Relation to Site Perspective"** explicitly invokes Tenet 5 (Occam's Razor Has Limits) — the same tenet anchor as bedrock-clash-vs-absorption, so the new countermeasure integrates cleanly.

### Enhancements Made

- **Added Countermeasure 8: Absorb-vs-Clash Discipline at the Article Level** — operationalises the bedrock-clash discipline as a system-level requirement on `/refine-draft` and `/deep-review`. Includes:
  - Why default-absorb is the silent inflation vector other countermeasures cannot catch.
  - The single decision heuristic (would absorbing improve or falsify the argument?).
  - Implementation requirements (classify before editing, defer when unclear, four-element bar for clash subsections, changelog recording).
  - Closure statement: how Countermeasure 8 closes the loop Countermeasure 4 leaves open.
- **Inline reference in Countermeasure 4** to the absorb-vs-clash decision.
- **New metric row**: "Pessimistic-review findings with explicit absorb-vs-clash classification" with 100% target.

### Cross-links Added

- [[bedrock-clash-vs-absorption]] — concepts/related_articles frontmatter, Countermeasure 8 body, Further Reading.
- [[closed-loop-opportunity-execution]] — added to Further Reading as cycle-level methodological cousin.

## Remaining Items

- The article does not currently provide empirical evidence for its freshness thresholds. This is not a defect of *this* article — those thresholds are policy choices. A separate research task to investigate field velocities would supersede the policy with empirics, but no current pessimistic finding requires that work.
- Countermeasure 8's implementation requirements (changelog records of absorb-vs-clash classification) are not yet enforced in the actual `/refine-draft` skill code. This is a follow-up implementation task, not a content gap.

## Stability Notes

- **Eliminative materialism rejecting the evidence/coherence distinction is a bedrock disagreement, not a critical issue.** Future reviews should not re-flag this. The article presupposes a non-eliminativist epistemic frame; absorbing the eliminativist objection would require dropping the article's premise and is therefore a clash, not an absorption — but the clash sits at the meta-level of the entire Map, not inside this specific article.
- **Madhyamaka self-reification critiques of the article's categories are also bedrock**, addressed at the operational-fiction frame level; not a flaw inside this article.
- **The freshness thresholds are stipulative policy, not empirical claims.** Future reviews should not re-flag the absence of empirical support for the specific numbers.
- **The bedrock-clash discipline now has an explicit home in Countermeasure 8.** Future cross-reviews should not re-add the discipline as a missing item; if the discipline needs strengthening, that strengthening should refine Countermeasure 8 rather than introducing parallel countermeasures.
