---
title: "Deep Review - Arguments"
created: 2026-06-18
modified: 2026-06-18
human_modified: null
ai_modified: 2026-06-18T13:18:44+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-18
last_curated: null
---

**Date**: 2026-06-18
**Article**: [[arguments|Arguments]] (section index)
**Previous review**: [[deep-review-2026-05-17-arguments|2026-05-17]]

## Context

Changed-since-review verification of the section index. The 2026-06-01 refine-draft (commit c9e61d424, "Calibrate epiphenomenalism-argument + arguments index to match the softened tenets-page treatment") bumped `ai_modified` past `last_deep_review` (32d gap). That refine softened only two lines — the §"Against Epiphenomenalism" summary and the Bidirectional-Interaction tenet line — but was never deep-review-verified for index-wide propagation. This pass audits whether the calibration discipline reached the *other three* argument summaries and confirms summaries still track their (separately refined/reviewed) children.

Pre-confirmed landed (not re-litigated): the Epiphenomenalism summary now reads "pressuring epiphenomenalism toward self-stultification... the sophisticated phenomenal-concept version relocates the dispute rather than ending it"; the Bidirectional-Interaction tenet line now reads "presses hard toward... a relocation of the dispute rather than a closed result." Both verified calibrated against the current tenets-page treatment (tenets.md lines 90–98).

## Pessimistic Analysis Summary

### Critical Issues Found

- **Calibration drift / summary-tracks-child failure — Many-Worlds Key claims (line 52)**. The index led the Many-Worlds "Key claims" with *"Ontological extravagance: mathematical simplicity purchased with metaphysical inflation"* — unqualified, in first position, framed as a lead objection. Both the recalibrated child page (`many-worlds-argument.md`, §"A Non-Decisive Cost: Ontological Extravagance", lines 140–164 + Cumulative Case table) and the tenets page (tenets.md line 114, "subsidiary — a registered cost, not a refutation"; line 198) now explicitly demote ontological extravagance to a **non-decisive cost the Map cannot press**, because Tenet 5 (Occam's Razor Has Limits) binds the Map not to wield parsimony as decisive having disowned it. The load-bearing argument on both child and tenets page is the **indexical problem** ("This is the Map's central objection" / "This is the load-bearing argument"), which the index buried in second place.

  **Diagnostic test applied**: would a reviewer who fully accepts the Map's tenets still flag this? **Yes** — Tenet 5 is itself a Map tenet and the tenets page makes the discipline symmetric ("parsimony cannot decide for or against a framework", line 140; "Rules out... internally, any Map argument that leans on parsimony as if this tenet did not apply to it", line 142). A tenet-accepting reviewer flags the index for leading with the very parsimony-style objection the Map disowns. This is a calibration error correctable inside the framework, not a bedrock disagreement.

  **Resolution**: reordered the Key claims so the indexical problem leads (marked "load-bearing"), probability and consciousness-role follow, and ontological extravagance moves last, rewritten to *"a registered cost, not a decisive objection—having disowned parsimony under [[tenets#^occams-limits|Tenet 5]], the Map cannot wield ontological economy as a knockdown argument."* This now mirrors the child's Cumulative Case table exactly and preserves the partisan framing (the section still argues against MWI). +18 body words; still 33% of soft threshold.

### Medium Issues Found

None. The other three summaries' overclaim verbs were checked and found faithful (see below) — no false-balance neutering applied.

### Surviving-Overclaim Scan (task a) — the other three summaries

Scanned §"Against Materialism", §"Against Functionalism", §"Against Many-Worlds" (and Occam) for overclaim verbs (shows/establishes/proves/decisive/demonstrates/refutes) inconsistent with the softened tenets-page register. Verdict per summary:

- **Against Materialism** ("zombie argument *shows* consciousness is not entailed by physical facts") — CLEAN. Standard conditional output of the zombie argument; the child page's Relation section explicitly states "None of this proves dualism" and frames dualism as a working hypothesis. The index claims non-entailment, not refutation of materialism. A tenet-accepting reviewer would not flag it.
- **Against Functionalism** ("five arguments *showing* functional organization is insufficient"; "*showing* function doesn't guarantee consciousness") — CLEAN. The child page's Conclusion (lines 204–212) uses the identical "shows" register ("Zombies show that functional organization doesn't guarantee consciousness"). Index faithfully tracks child. Functionalism rejection runs on bare Tenet 1; calibrated correctly.
- **Against Many-Worlds (Relation line)** ("arguments against many-worlds *show* why the Map requires collapse to be real") — CLEAN. A claim about the Map's *internal* requirement, not a claim that MWI is refuted.
- **Occam's Razor** ("History repeatedly *shows* parsimony pointing away from truth") — CLEAN. Matches tenets.md line 128 verbatim in register.

The single surviving overclaim was the Many-Worlds Key-claims ordering/framing (critical, fixed above). The "shows" verbs elsewhere are faithful to their recalibrated children; softening them would impose false balance the prompt explicitly warns against on this by-design partisan index.

### Summary-Tracks-Child (task b)

- Materialism summary ↔ `materialism-argument.md` (deep-reviewed 2026-06-15): faithful. Key claims (explanatory gap not merely epistemic; zombie non-entailment; quantum not causally closed) all present and correctly scoped in the child.
- Functionalism summary ↔ `functionalism-argument.md` (deep-reviewed 2026-05-22): faithful. Five Key claims mirror the five numbered arguments + Conclusion.
- Many-Worlds summary ↔ `many-worlds-argument.md` (deep-reviewed 2026-06-03): drifted on ontological-extravagance framing (fixed); after fix, the four Key claims now mirror the child's Cumulative Case table in both content and the non-decisive marking.
- Epiphenomenalism summary ↔ `epiphenomenalism-argument.md` (refined 2026-06-01): pre-confirmed calibrated; consistent with the four numbered arguments and the relocation register.

### Links (task c)

All intra-page wikilinks resolve: materialism-argument, functionalism-argument, many-worlds-argument, epiphenomenalism-argument, epistemological-limits-of-occams-razor (arguments/), parsimony-case-for-interactionist-dualism (topics/), epistemological-limits-occams-razor (voids/), interactionist-dualism (concepts/), and the three concept pages (concepts/materialism, concepts/many-worlds, concepts/functionalism). All five tenet anchors used (^dualism, ^bidirectional-interaction, ^minimal-quantum-interaction, ^no-many-worlds, ^occams-limits) are defined in tenets.md.

### Date sanity (task d)

No in-body dates present. No date-sanity issue.

### Citations

This index carries no bibliographic citations (pure routing/summary page). §2.4 web-verify pass not applicable.

### Attribution Accuracy Check

- "Seven arguments" (Interactionist Dualism), "four arguments" (Epiphenomenalism), "five arguments" (Functionalism): unchanged since the 2026-05-17 review verified them; no detail-page count changes detected this pass. No misattribution, no dropped qualifiers, no source/Map conflation, no self-contradiction.

### Reasoning-Mode Classification (editor-internal)

Index/landing page — points to detail pages that engage named opponents; does not itself conduct argumentative dialogue. The opening "openly partisan" paragraph is Mode Three boundary-marking for the section as a whole. No label leakage; no editor-vocabulary in prose.

## Optimistic Analysis Summary

### Strengths Preserved

- The "openly partisan" opening framing (do NOT re-flag — established as the page's distinctive stance in prior reviews).
- The "Key claims" + "Discussion" structure (LLM truncation resilience).
- The cumulative-case paragraph in Relation to Site Perspective ("rejecting materialism motivates dualism; rejecting epiphenomenalism requires interaction; the mechanism for interaction requires collapse interpretations that reject many-worlds") — preserved unchanged; the index's most distinctive contribution.
- Full five-anchor tenet coverage.

### Enhancements Made

- Reordered + recalibrated the Many-Worlds Key claims so the load-bearing indexical argument leads and ontological extravagance is marked non-decisive (Tenet 5 binding), bringing the index into line with both the recalibrated child page and the tenets page.

### Cross-links Added

- None new; added an inline [[tenets#^occams-limits|Tenet 5]] anchor within the recalibrated Many-Worlds extravagance bullet (reuses an already-present anchor target).

## Remaining Items

None.

## Stability Notes

- The 2026-06-01 calibration *did* propagate to the epiphenomenalism summary and tenet line but had NOT reached the Many-Worlds Key claims, which still led with unqualified ontological extravagance. That gap is now closed; the index, the No-Many-Worlds tenet treatment, and the many-worlds-argument child page are mutually consistent on extravagance-as-non-decisive-cost.
- **Future reviews should NOT re-flag** the "shows" verbs in the Materialism / Functionalism / Occam summaries: they faithfully track their (separately reviewed) children's calibrated register and are conditional in-framework claims, not overclaims. Softening them would impose false balance on a by-design partisan index.
- **Future reviews should NOT re-flag** the openly-partisan opening or the "Quantum mechanics is not causally closed" Key claim (index summary pointing to a detail page that defends it — category mistake to treat the index as load-bearing).
- **Bedrock disagreements** (do NOT re-flag): MWI defenders reject the indexical bullet; eliminativists reject the explanatory-gap bullet; functionalists reject the absent-qualia bullet. Framework-boundary, not flaws.
- Word count: 803 → 821 (+18). 33% of soft threshold; length-neutral.
- This index should fire again only on: new argument sections; detail-page renames breaking wikilinks; argument-count changes on children; or a further calibration shift on a child/tenet that the summary must track.
