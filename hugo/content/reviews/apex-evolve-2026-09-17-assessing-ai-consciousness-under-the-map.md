---
ai_contribution: 100
ai_generated_date: 2026-09-17
ai_modified: 2026-09-17 01:27:35+00:00
ai_system: claude-fable-5-1
author: null
concepts: []
created: 2026-09-17
date: &id001 2026-09-17
description: 'Apex-evolve pass on three apex articles carrying summaries of sources
  that changed on 2026-09-16: substrate taxonomy, sign problem, and P-I4.'
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-17 01:27:35+00:00
modified: *id001
related_articles: []
title: 'Apex Evolve Review: Driver-Flagged Stale Summaries (2026-09-17)'
topics: []
---

# Apex Evolve Review: Driver-Flagged Stale Summaries

**Mode**: evolve, driver-directed (three targets, one pass). Selection followed the driver's notes for 2026-09-16/17 rather than the staleness scorer.

## Articles reviewed and changed sources

| Apex | Changed source (2026-09-16 commit) | Stale claim found |
|---|---|---|
| [assessing-ai-consciousness-under-the-map](/apex/assessing-ai-consciousness-under-the-map/) | [ai-hardware-substrate-taxonomy](/concepts/ai-hardware-substrate-taxonomy/) (`e85d8a7262`, new section *Gate-model quantum computing: two eligibility standards*) | "mapped at finer grain by the substrate taxonomy" — presented the taxonomy as the same territory at higher resolution, hiding that its Axis 2 predicate and the five-requirement channel test now come apart on the gate-QPU case, with the channel test governing present hardware |
| [what-consciousness-tells-us-about-physics](/apex/what-consciousness-tells-us-about-physics/) | [sign-problem-for-conscious-observation](/concepts/sign-problem-for-conscious-observation/) (`6723f97c51`, Horn 2 priced via the agency budget) | Paragraph said the sign problem leaves Horn 2's specification cost "unpriced", that the budget is "the currency it would have to be priced in", that the two results "meet in a way neither states alone", and that "nothing yet establishes that the two demands fit inside one budget". The source now states the meeting itself and prices the horn: tens of bits per placement × ~10¹³ placements per decision window against ~10 bits/s, i.e. the demands do not fit, and the shortfall lands on the horn the agency reading needs |
| [identity-across-transformations](/apex/identity-across-transformations/) | [individuation-and-subjecthood](/positions/individuation-and-subjecthood/) (`a641a16547`, [P-I4](/positions/individuation-and-subjecthood/#p-i4) fission verdict now conditional on [P-SC2](/positions/subject-census/#p-sc2); split-brain consequence booked) | "the same consciousness with fragmented continuity (as in amnesia or split-brain) remains the same subject" — a flat one-subject verdict on split-brain, where [P-I4](/positions/individuation-and-subjecthood/#p-i4) now books the question as real but unreadable ([P-I3](/positions/individuation-and-subjecthood/#p-i3)) and the reported single perspective as telling for, not settling, continuity |

Also checked and left alone: [direction-of-fit](/concepts/direction-of-fit/) (Searle bullets rewritten) is not cited by any apex; [mereology-of-mind](/apex/mereology-of-mind/) carries no fission/fusion verdict sentence to go stale ([P-I4](/positions/individuation-and-subjecthood/#p-i4) cites it as the fusion mirror via its de-combination hinge, which is unchanged); [one-world-wager](/apex/one-world-wager/) §List discusses [P-I5](/positions/individuation-and-subjecthood/#p-i5)'s target, whose 09-16 wording change ("many-subject views such as List's") the apex already matches in substance.

## Pessimistic review (three personas)

**Clarity Critic**: In the AI apex the old parenthetical made the taxonomy sound like a finer-resolution copy of the channel test; a reader following the link would find a section saying the two standards disagree. In the physics apex the paragraph's rhetorical build ("a debt the Map has only now made visible to itself") outlived the state of the debt. In the identity apex "as in amnesia or split-brain" bundled an uncontroversial case with a contested one.

**Redundancy Hunter**: The identity apex already reports the single first-person perspective two sentences earlier (line 171), so the new clause refers back to "the reported single perspective" rather than restating it. The physics paragraph's "and that access is information the mechanism must supply from somewhere" was made redundant by the priced figure and was cut to pay for it.

**Narrative Flow Analyst**: In the AI apex the divergence clause now sits after the channel test is named, so "this test" has a referent; placing it in the earlier parenthetical would have forward-referenced an unnamed test. In the physics apex the paragraph now closes on what a deeper theory must show (price wrong, or direction set without the agent paying), which keeps the section's "what a deeper theory would have to do" structure.

## Optimistic review (three personas)

**Connection Finder**: The physics apex gains the concrete price (≈1 bit/event budget vs tens of bits × ~10¹³ placements vs ~10 bits/s), which is the synthesis point the article was reaching for when it wrote "the budget is the currency". The AI apex now links to the exact taxonomy section (`#gate-model-two-standards`) rather than the article top.

**Synthesis Strengthener**: The identity apex now ties its split-brain claim to the register entry (bare `P-I4`, autolinked by sync) so a reader can see the verdict's conditional footing rather than an asserted one.

**Human Reader Advocate**: "Coarser eligibility predicate" was chosen over the taxonomy's internal name "Axis 2", which an apex reader has not been introduced to.

## Length assessment (`analyze_length`, apex soft 4000 / hard 5000; the hard figure itself trips)

| Apex | Before | After | Status |
|---|---|---|---|
| assessing-ai-consciousness-under-the-map | 5035 | 5035 | hard_warning (unchanged; edit length-neutral as the driver required) |
| what-consciousness-tells-us-about-physics | 5453 | 5453 | hard_warning (unchanged; rewritten paragraph held at 164 words) |
| identity-across-transformations | 4393 | 4414 | soft_warning (+21) |

Both hard-warning articles were already over threshold before this pass; no condensation was attempted here because the driver scoped the work to the stale summaries. They remain candidates for a dedicated condense pass.

## Evidence and Dependency section

Present on all three; the physics apex's ledger (which grades the capacity ceiling and direction shortfall as *mutually coherent only*) still describes the rewritten paragraph correctly, since the new price is coherence-only arithmetic per the source. No refresh needed.

## Citations

No external citation was added or altered. The figures introduced into the physics apex (min(H(source), H(Born)) bits, ~10¹³ placements, ~10 bits/s) are the Map's own internal arithmetic as stated in [sign-problem-for-conscious-observation](/concepts/sign-problem-for-conscious-observation/), [agency-budget](/concepts/agency-budget/) and [bandwidth-of-consciousness](/concepts/bandwidth-of-consciousness/); nothing required publisher verification.

## Sync

`scripts/sync.py` run; old strings return 0 in both trees, new strings 1 in both (the bare `P-I4` renders in Hugo as `[P-I4](/positions/individuation-and-subjecthood/#p-i4)`). Frontmatter bumped on all three (`ai_modified`, `modified`, `apex_last_synthesis`, `ai_system` += claude-fable-5-1). todo.md untouched.