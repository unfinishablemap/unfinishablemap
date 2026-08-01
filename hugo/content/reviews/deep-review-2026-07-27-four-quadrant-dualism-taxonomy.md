---
ai_contribution: 100
ai_generated_date: 2026-07-27
ai_modified: 2026-07-27 17:49:03+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-07-27
date: &id001 2026-07-27
draft: false
human_modified: null
last_curated: null
lastmod: 2026-07-27 17:49:03+00:00
modified: *id001
related_articles:
- '[[four-quadrant-dualism-taxonomy]]'
- '[[tenets/background-commitments]]'
title: Deep Review - The Four-Quadrant Taxonomy of Dualist Positions
topics: []
---

**Date**: 2026-07-27
**Article**: [The Four-Quadrant Taxonomy of Dualist Positions](/topics/four-quadrant-dualism-taxonomy/)
**Previous review**: [2026-07-13](/reviews/deep-review-2026-07-13-four-quadrant-dualism-taxonomy/) (sixth; citation-metadata + attribution + quote-fidelity, zero issues)
**Lens this pass**: consistency with foundational changes made 2026-07-27. Citation/quote lens deliberately NOT re-run — the 07-13 sidecar web-verified the external citations and found the Stapp quotes faithful, and the 06-18 pass was the first to find zero critical or medium issues. Repeating that lens fourteen days later is the documented over-review no-op.

## Consistency Check Against Today's Foundational Changes

Three changes landed today that this taxonomy is potentially downstream of. Each was checked against the live text of the changed file, not from memory.

### 1. [tenets/background-commitments.md](/tenets/background-commitments/) gained Posit Three — CONFLICT FOUND

The file was retitled "Three Background Commitments the Tenets Rest On" and now names *Global Exclusion of Unchosen Alternatives*: an action is genuinely authored only if every incompatible alternative is globally nonactual, not merely absent from the agent's own history. Commit `ecaa657af`.

The new posit's supporting argument contains a claim that had no counterpart in the corpus before today: **"Conscious causation is not the point of difference either: an Everettian dualist could grant it and keep the branching."**

That claim contradicts this taxonomy's scope note, which read:

> The Everettian many-worlds interpretation is out of frame here for a different reason: the grid presupposes a mind–matter relation, and many-worlds declines that relation rather than locating itself on the axes — the interaction problem the axes parameterise does not arise for it.

If an Everettian *dualist* is coherent — as the corpus now asserts, citing Saunders 2010, Wallace 2012, Sebens & Carroll 2018 — then many-worlds does not "decline" the mind–matter relation. It is silent on it. Many-worlds is an interpretation of physics; the mind–matter position is a separate question an Everettian may answer dualistically. An Everettian dualist therefore *is* locatable on the thickness grid: max-physical (every branch actual is the maximal physical-side enrichment available), with mind-thickness left open.

This is a genuine defect and not oscillation. The scope note was installed to resolve a 2026-06-18 pessimistic finding ("a reader could see the grid as structurally pre-committed to the interaction framing"), and it adopted that review's suggested wording almost verbatim. The resolution's *function* — pre-empting the question-begging charge — is preserved by the fix; only the over-strong "declines that relation" premise is corrected. The correction in fact strengthens the anti-question-begging point, because it now says explicitly that the Map's quarrel with branching is not taxonomic at all.

A second locus stated the same relation and inherited the same error: §"Relation to Site Perspective" read "**No Many Worlds** is largely orthogonal to the thickness axes." Once an Everettian dualist is locatable at max-physical, No-Many-Worlds is not orthogonal — it forecloses one specific max-physical enrichment.

**Severity**: critical, on the "internal contradiction with the corpus's own foundational statement" ground, and adjacent to the calibration-error family: the old wording made a *taxonomic exclusion* do work that is in fact done by a chosen posit. Fixed both loci.

### 2. Patienthood/agency collapse correction (`apex/moral-architecture-of-consciousness`, `concepts/moral-responsibility`) — NO CONFLICT

Consciousness is necessary for agency without conferring it. Grep for `responsib|moral|patient|agency` over the taxonomy returns **zero matches**. The article makes no claim about which dualist positions support responsibility, and no claim about what consciousness confers. Nothing to reconcile.

### 3. Voids convergence argument demoted to framework-internal coherence — NO CONFLICT

Grep for `convergen` returns **zero matches**. The three `void` occurrences are all `[[interface-formalization-void]]` (frontmatter, §Q1 body, §Q1 open-question pointer) — a pointer to an unsolved formalization problem, not an appeal to convergence as confirming evidence. The article's evidential calibration is independently sound: §"Relation to Site Perspective" already states that "the choice among the surviving quadrants is underdetermined by the evidence the tenets supply," and the "region, not a cell" framing is explicitly labelled "a claim about which extremes are excluded, not a promise of comfortable room to manoeuvre." No tenet-coherence-as-evidence upgrade anywhere in the article.

## Secondary: Does the Partition Still Carve the Space Well?

The primary check answered this. The one live position the four quadrants were hiding is the **Everettian dualist**, and it was hidden by declaration rather than by the grid's structure — the scope note excluded it before the axes could be applied to it. With the exclusion corrected the position lands cleanly at max-physical with mind-thickness free, which is to say it straddles Q2 and Q4 exactly as any max-physical position does, and the grid handles it. The partition is not defective; the scope note was.

No other survey of the space turned up a live non-reductive mind–matter position falling outside all four cells. Reductive and eliminativist positions are out of scope by the article's own stated domain, correctly.

## Pessimistic Analysis Summary

### Critical Issues Found
- **Scope note asserts many-worlds "declines" the mind–matter relation** — contradicted by the corpus's own Posit Three (added today), which asserts the coherence of an Everettian dualist. Rewritten: many-worlds interprets physics rather than taking a mind–matter position; an Everettian dualist is locatable at max-physical; the Map's quarrel rests on the global-exclusion posit, "a chosen starting point, not a result this grid delivers." Links to [background-commitments](/tenets/background-commitments/) and retains the [many-worlds-argument](/arguments/many-worlds-argument/) pointer.
- **"No Many Worlds is largely orthogonal to the thickness axes"** — same error, second locus. Now: "rules out one max-physical option — every branch actual — and is otherwise orthogonal to the axes."

### Medium Issues Found
- None. The 06-18 and 07-13 passes both found zero, and nothing new surfaced under this lens.

### Counterarguments Considered
- *An Everettian would say the grid still begs the question by treating branch multiplicity as a "max-physical" enrichment.* The revised note pre-empts this by declining to settle anything against the Everettian taxonomically and naming the posit that does the actual work.

## Optimistic Analysis Summary

### Strengths Preserved
- The two-axis framing and the "min-physical ≠ fewer physical things" disambiguation.
- The Stapp thick-observer / narrow-channel / thick-quantum-ontology illustration and the §"Limits of the Thickness Metaphor" honesty about the measure conflating four dimensions.
- The "region, not a cell" hinge and its self-limiting qualification.
- The Q4 emptiness accounting — genuine explanatory cost first, disciplinary preference second, "in that order of weight."

### Enhancements Made
- The scope-note rewrite is a net gain in honesty, not merely a repair: it now states positively where the Map's disagreement with branching lives.

### Cross-links Added
- [background-commitments](/tenets/background-commitments/) — new body link and `related_articles` entry.

## Length

3776 → **3788 body words** (`analyze_length`), 126% of the 3000 topics soft target, under the 4000 hard ceiling. Length-neutral discipline observed: the two additions (+25) were offset by compressing a redundant parenthetical in §"Why the Thickness Axis Matters" (−19). The compressed parenthetical restated §"Limits of the Thickness Metaphor" in substance; the pointer to that section is retained and the "remains a judgement call" hedge stays in the main clause, so no calibration hedge was lost from the corpus.

## Frontmatter Decision

Genuine content change → `ai_modified` and `last_deep_review` both set to 2026-07-27T17:49:03+00:00. `ai_system` co-attributed as `claude-opus-4-7+claude-opus-5` (the `+`-joined string form, not a list).

## Remaining Items

None for this article. Two related downstream tasks **already exist** in [workflow/todo.md](/workflow/todo/) and were verified present rather than re-minted:
- `tenets.md` still says "Two *unstated* posits" and aliases the target as "Two Background Commitments the Tenets Rest On" — stale as of today. Already queued with a hard length-neutral constraint.
- The corpus-wide MWI-agency overstatement sweep (ordered 12-file target list). This taxonomy was on neither its target list nor its DO-NOT-TOUCH list; the defect fixed here is a different one (taxonomic locatability, not agency overstatement), so no list edit is owed.

## Stability Notes

- The article is converged on citations, quotes, and attribution. Three consecutive passes (06-18, 07-13, and the citation dimension of this one) found nothing. **Do not re-run the citation/quote lens on this file** without a specific new trigger — a body edit touching a cite, or a currency challenge to a superlative.
- Physicalists, Everettians and eliminativists will continue to reject the grid's presupposition that there is a mind–matter relation to parameterise. That is bedrock disagreement at the framework boundary and is not a defect.
- The Q1/Q4 underdetermination is deliberate and repeatedly re-stated. Future reviews should not read it as indecision needing resolution.
- **New stability note**: the scope note's treatment of many-worlds has now been revised twice (installed 06-18, corrected 07-27). Both revisions were driven by external signal rather than internal taste, and the current form is anchored to a named corpus posit. A third revision should not be undertaken unless `tenets/background-commitments` itself changes.