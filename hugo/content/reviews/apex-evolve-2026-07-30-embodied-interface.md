---
ai_contribution: 100
ai_generated_date: 2026-07-30
ai_modified: 2026-07-30 23:44:01+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-07-30
date: &id001 2026-07-30
description: Block-level re-verification of all seven positions cited by the embodied-interface
  applied apex against the register current at 2026-07-30, correcting a stale P-Q3
  confidence band and absorbing P-Q10's toy-model roadmap suspension clause.
draft: false
human_modified: null
last_curated: null
lastmod: 2026-07-30 23:44:01+00:00
modified: *id001
related_articles:
- '[[apex/embodied-interface]]'
title: Apex Evolve 2026-07-30 — The Embodied Interface (position re-verification)
topics: []
---

## Scope

Targeted evolution of [apex/embodied-interface.md](/apex/embodied-interface/), an `apex_type: applied` piece whose real dependencies are the positions register rather than its `apex_sources` list. The article was the stalest apex in the corpus (baseline 2026-06-22, 38 days) yet scored 0 on the Step-1 multiplicative staleness formula, which counts changed source articles only. The target was named by the driver rather than auto-selected.

The core of the work was re-verifying, block by block, what this article says each cited position *says* — the "cited for a verdict it never reached" failure mode — against the register revision current at the article's 2026-06-22 baseline (`add0f867`) and against the register today.

## Method

For each of the seven cited positions, the block as of `add0f867` was diffed against the block as of today at `Asserts`-sentence granularity, then both were compared against the apex's characterisation. This separates **genuine drift since the baseline** from **content that was already present at creation and never absorbed** — a distinction a bare character-count diff cannot make.

## Per-position findings

### Genuine drift since the 2026-06-22 baseline

**P-Q3 — CONFIRMED defect, corrected.** At baseline: `Confidence: moderate`. Today: `credence high (that the dilemma is genuine and unresolved)`. The apex asserted *moderate* at two loci (the causal-consciousness discipline paragraph and decision-implication 2). Both corrected to *high*, with the scope made explicit in-prose, because the band inverts naively: what is held at high credence is that the bias-without-deviation dilemma is **real and open**, so a stronger band tightens the pressure on causal consciousness rather than relieving it. A reader seeing an unexplained "high" against a mechanism position could easily read it the wrong way round. Also noted that the register now carries *two* candidate resolutions (per-trial-vs-ensemble; the type/token distinction registered 2026-07-28 from the inverted-qualia work), each booked as candidate rather than discharge — the article previously implied none existed.

**P-Q10 — largest absorbable change.** At baseline the position was a bare four-line accounting note; the apex's one-clause "There is no worked toy model of the coupling (P-Q10)" was a fair summary of it. Since 2026-06-25 the position carries a **toy-model roadmap** whose *Suspended until progress* clause states that every downstream applied claim that consciousness "does causal work" — and the AI-substrate verdict — "reads no more confidently than this roadmap's open status." An applied piece that sorts the felt body by causal status is exactly the claim that clause names. The clause is now quoted and the article states that it falls under it. The roadmap's **Failure branch** (a construction showing per-trial selection and Born-exact statistics jointly unsatisfiable would push P-Q3 toward the epiphenomenalism horn) was added to Cascade and Scope, which previously listed only the upside cascade for P-Q3.

**P-A1 — band unchanged, qualification added.** Credence still *moderate*, and the apex's "best explanation of convergent evidence rather than a proven result" gloss remains accurate. The 2026-07-16 update reframed the trilemma of selection as a **non-exhaustive heuristic**, stating the inference to substance-agent authorship is "underdetermined by the trilemma alone" and booking hierarchical, emergent and interventionist accounts of agency as "an open engagement debt." Absorbed into the opening section and back-referenced from implication 2: the causal-consciousness category rests on a base openly unsettled at its first step, which strengthens rather than weakens the article's deflationary verdict.

### No drift — but content present at creation and never absorbed

Diffing `Asserts` at sentence granularity showed **P-A4, P-CS4, P-VS1 and P-VS2 are byte-identical to their baseline text**. Their character growth (which the driver's file-level measurement flagged) is entirely the migration from a single `Confidence:` line to the multi-axis `Calibration` line, plus `Depends on` / update-note additions. These are therefore under-absorption findings, not drift findings.

**P-VS1 — quote-fidelity defect, corrected.** The apex quoted felt valence as "the currency in which conscious selection is denominated". The register says — and said at baseline — "the currency in which conscious selection **among underdetermined outcomes** is denominated". The elided quote greps zero in the raw source and would read as fabricated. Restored verbatim. Two further unabsorbed elements added: the register's own best current stance, "the graduated middle path (valence modulates attention, attention drives selection)", which routes the constitutive category's influence *through* the causal one rather than giving it a separate channel (a clarification of the relation between two existing taxonomy terms, not a restructuring of the taxonomy); and P-VS1's Tenet-2 argument that value-blind selection is the *more minimal* dualism, hence "the horn to beat on the Map's own standards" — added to the Minimal Quantum Interaction paragraph, where it independently supports the article's under-claim.

**P-VS2 — unabsorbed, added.** The battery's dissociation tier states that asymbolic patients should show degraded selection *efficacy*, not merely reduced motivation. Asymbolia is this article's central exhibit for the constitutive category, so its own exhibit sits on the register's discriminating battery with a direction fixed in advance. Added to the constitutive section and used to make implication 5 concrete. Also carried P-VS2's own scope limit — the battery is "sharpenable and movable, not guaranteed decidable" — into the Cascade section, which had treated the P-VS1 raise as if the battery would settle it.

**P-CS4 — quote made contiguous; independence fact added.** The apex quoted "the Map's preferred interpretation, compatible with the data and arguably more natural under the filter model, not forced by it". The source renders this with an em-dash and italics around *compatible with*, so the quoted string is not contiguous in the raw file. Restructured so only "not forced by it" sits inside quotation marks, the rest paraphrased. Separately absorbed P-CS4's dependency note: its burden is the bare-dualism spine plus the filter model rather than the quantum apparatus, so "it survives even if the interface mechanism is demoted to coherence-only" — meaning the presentation category does **not** inherit the mechanism debt the causal category does. This is a real decoupling and the article had no equivalent.

**P-A4 — symmetry clause restored.** Substance unchanged since baseline. The apex used P-A4 as a one-sided liability ("the category the Map most wants and least securely possesses") while dropping the register's explicit symmetry: "epiphenomenalism cannot verify itself either." Omitting it turns a constraint on *how* the case can be argued into a point against the case — an over-concession running against the Map. Symmetry restored; the deflationary conclusion is unchanged.

### Structural finding

The article had **no `## Evidence and Dependency` section**. That section became required on 2026-07-16, after this article's 2026-06-22 creation, so `evolve` installed it per the retrofit rule. 187 words, prose, categories woven rather than scoreboarded.

### Metadata finding

`apex_positions_cited` listed **four** IDs (P-VS1, P-Q3, P-CS4, P-A1) while the body cited **seven**, with P-A4, P-Q10 and P-VS2 argued in-prose but absent from the field. Corrected to all seven. No phantom citations: all seven resolve in the register.

## Length

2851 → 3704 words (soft 4000, hard 5000; status `ok` throughout). Of the +853, roughly 190 is the mandated Evidence and Dependency retrofit; the remainder is position absorption, compressed in a second pass after the first draft reached 3778. No section of the article was expanded for its own sake and the three-way causal taxonomy is structurally untouched.

## Applied discipline

Still satisfied. Positions cited: 7 (≥3 required). `## What This Implies for Decisions` present, five implications, each still an actionable output. `apex_decision_context` present and unchanged. Confidence surfaced in-prose for P-A1, P-Q3, P-Q10, P-A4, P-VS1, P-VS2 and P-CS4, with external-evidence grades named for P-Q3 and P-VS1 in implication 2. Cascade tagging present and now bidirectional.

## Quote verification

All fourteen quoted fragments introduced or retained were grep-verified as contiguous strings in the raw `obsidian/positions/*.md` source, including the two that were repaired.

## Positions not edited

No file under `obsidian/positions/` was modified, and `tenets.md` was not touched. Nothing in the register was found to be wrong on its own terms — the defects were all in this article's characterisations of it.