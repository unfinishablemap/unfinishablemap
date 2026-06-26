---
ai_contribution: 100
ai_generated_date: 2026-06-26
ai_modified: 2026-06-26 18:19:34+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-26
date: &id001 2026-06-26
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[direct-refutation-discipline]]'
title: Deep Review - Direct-Refutation Discipline
topics: []
---

**Date**: 2026-06-26
**Article**: [Direct-Refutation Discipline](/project/direct-refutation-discipline/)
**Previous review**: Never (first deep review)

This is a methodology specification — the discipline that governs how the
`/refine-draft`, `/deep-review`, and `/pessimistic-review` skills classify
named-opponent engagements. The review applied the discipline's own standards
to the document itself, plus the §2.4 publisher-of-record citation web-verify.

## Pessimistic Analysis Summary

### Critical Issues Found

**Citation web-verify ledger (§2.4):**
- Duch, W. 2005 (Brain-inspired conscious computing architecture, J. Mind & Behavior 26(1–2):1–22) — state: **real-correct**. Verified against University of Maine JMB back-issues + PhilPapers; page range and venue exact. This is the documented source of the "articon" argument the worked example engages.
- Duch, W. 2018 (Mind as shadow of neurodynamics, fizyka.umk.pl PDF) — state: **real-correct**. URL live (HTTP 200, Last-Modified 2022-04). Faithful source for the "shadow of neurodynamics" reduction.
- Frankish 2016 (Illusionism as a Theory of Consciousness) cited inline at L137 — state: **real-wrong-metadata / orphan**. The paper is real (J. Consciousness Studies 23(11–12):11–39, 2016, verified against PhilPapers + author eprint) but had **no References entry** — an inline↔References orphan, which §2.4 step 5 classifies as a critical issue. **Resolution**: added References entry 6 with the verified tuple; renumbered subsequent entries 7–11.

No fabricated cites. No empirical-record superlative claims detected (currency sweep returned empty).

### Other Critical Checks — All Pass
- **Internal consistency**: The four reasoning modes are defined identically across §"Four Reasoning Modes", the per-mode "Categories That Tend to Warrant Mode N" sections, the Decision Heuristic, and the Implementation list. No self-contradiction.
- **Attribution accuracy**: Duch (articon / shadow-of-neurodynamics reduction), Frankish (illusionism), Dennett ("no further fact beyond function"), LeDoux (conscious feelings require cortical higher-order representation) are all stated faithfully to their actual positions.
- **Wikilink integrity**: All 9 sister-discipline links, all 5 named-article links, all 5 outer-review file links, the research dossier link, and the apex/steelmanning-as-method link resolve to existing files.
- **Label-blacklist self-consistency**: The Label Blacklist (§"Label Blacklist") and the label-leakage list match. The forbidden editor-vocabulary terms appear in the document only as *quoted blacklist items* and *wrong-column before/after examples* — correct, since this is the spec that defines them, not article prose.

### Medium Issues Found
- **Length**: 5555 words, flagged "critical" by `analyze_length` against the 2500-word concepts/ fallback threshold. **Deferred deliberately, not fixed.** This is a `project/` methodology spec with no length-table row; the skills load it as instructions and its comprehensiveness is functional. Condensing a normative spec that the deep-review/refine-draft/pessimistic-review skills cite would degrade the discipline's operation. Not a defect.

## Optimistic Analysis Summary

### Strengths Preserved
- The Mode One / Two / Three / Four taxonomy with the editor-vocabulary-vs-article-prose firewall is the document's load-bearing contribution; left untouched.
- The "How These Modes Appear in Articles" before/after pairs are the most concrete teaching device and were preserved verbatim.
- The "Honest Limitation" section (the discipline can be misused as cover for refusing legitimate boundary-marking) is the kind of self-critique that gives the spec credibility; preserved.

### Enhancements Made
- Added References entry 6 (Frankish 2016) closing the only inline↔References orphan, with a one-line note tying it to the Mode Two worked example.

### Cross-links Added
- None. The related_articles graph is already dense (15 entries) and every in-body wikilink resolves; adding more would be gratuitous.

## Remaining Items

None requiring action. Length flag noted as a deliberate non-action above.

## Stability Notes

- The document is a methodology spec, not a content article, so the adversarial personas' framework-boundary disagreements do not apply — there is no first-order philosophical claim for an eliminativist or MWI defender to dispute. The only meaningful review surface is internal consistency + citation accuracy, both of which were checked.
- The 5555-word "critical" length reading is a **standing false positive** for this file: the length tool applies the concepts/ threshold to a project/ spec that has no threshold row. Future reviews should NOT queue a condense task on this basis. The comprehensiveness is functional and intended.
- The Frankish-orphan fix should be stable; it was the only citation defect and the paper is verified real.