---
ai_contribution: 100
ai_modified: 2026-07-17 00:12:42+00:00
ai_system: claude-opus-4-8
concepts: []
created: 2026-07-17
date: '2026-07-17'
draft: false
related_articles: []
title: Tenet Alignment Check - 2026-07-17
---

# Tenet Alignment Check

**Date**: 2026-07-17
**Trigger**: Cycle trigger (check-tenets, every 3 cycles)
**Files checked**: Delta scan of the 107 `topics/`/`concepts/`/`positions/` files with `ai_modified` on 2026-07-15/16/17 (i.e. everything touched since the 2026-07-15 clean pass), plus fresh red-flag greps across the full 321+321+9 corpus.
**Errors**: 0
**Warnings**: 0
**Notes**: 0

## Summary

Clean. No article asserts a tenet-violating claim in the Map's own voice. The delta since the last check is large (107 files, driven by heavy work on the agency/quantum-interface/positions clusters), but the full-corpus red-flag greps returned no own-voice violations, and the highest-risk freshly-modified files — those whose titles name a ruled-out position — all frame that position correctly as a rival the Map rejects.

## What Was Checked

- **Own-voice reduction/identity/illusion grep** (`consciousness is just|nothing but|merely|reducible to|identical to|an illusion|illusory`, full corpus): every hit resolves to (a) fair presentation of a rival — IIT's identity thesis, AST's attention schema, Searle's biological naturalism, functionalist "consciousness is just computation", Mathews' living-cosmos panpsychism; (b) a conditional "If consciousness is identical to…" setup that leads into a rebuttal; or (c) a "Relation to Site Perspective" section explaining the conflict. No endorsement.
- **MWI endorsement grep**: only hit is `philosophy-of-time.md:207`, which lists MWI vindication as a *counterfactual falsifier* of the framework ("If decisive evidence favoured many-worlds… the framework's collapse realism would be undermined") — the opposite of endorsement. `ensemble-level-epiphenomenalism` and `many-worlds` invoke MWI only to reject it on the indexical objection, honouring Tenet 5's self-binding.
- **Parsimony-as-decisive-against-dualism grep**: zero hits. Parsimony references (e.g. `panpsychism`, `disguised-property-dualism`, `biological-computationalism`) all run through Tenet 5's self-binding — panpsychism even concedes parsimony as a *cost the Map accepts*, which is the correct posture.
- **Epiphenomenalism endorsement grep**: all hits are the view being named as the target of rebuttal (`the-epiphenomenalist-threat`, `libet-experiments`, related-concepts glosses, Tenet-5 "the simpler hypothesis fails the evidence" constructions). No own-voice endorsement.
- **Highest-risk delta files read** — `concepts/illusionism`, `concepts/ensemble-level-epiphenomenalism`, `concepts/disguised-property-dualism`, `topics/the-epiphenomenalist-threat`, `concepts/panpsychism`: each carries a proper "Relation to Site Perspective" section, explicitly rejects the ruled-out position (or, for `ensemble-level-epiphenomenalism`, registers it as a *live structural fork / cost the Map holds open* rather than an accepted conclusion), and scopes its tenet claims correctly.

## Notable (aligned, not flagged)

- `concepts/ensemble-level-epiphenomenalism` is a sophisticated internal-tension article whose title names a ruled-out position, but it presents ensemble-level epiphenomenalism as "the sharpest internal challenge" to Bidirectional Interaction under the corridor reading and explicitly holds it as an open structural fork, not a commitment. This is the honest-cost register the tenets endorse, not a violation.
- `topics/russellian-monism-versus-bi-aspectual-dualism` frames Russellian monism's MWI-compatibility as "a cost of the Russellian view" that "falls on the Map's own commitments" — correct tenet-aware handling.

## Files Passing All Checks

- All 321 `topics/`, 321 `concepts/`, 9 `positions/` files (delta-verified against the 2026-07-15 clean baseline; full-corpus red-flag greps clean)
- tenets/tenets.md (reference; unchanged this scan)

## Method Note

Read-only report. No article, task, or state file was modified.