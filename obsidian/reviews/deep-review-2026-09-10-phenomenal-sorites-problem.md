---
title: "Deep Review - The Phenomenal-Sorites Problem"
created: 2026-09-10
modified: 2026-09-10
human_modified:
ai_modified: 2026-09-10T12:53:18+00:00
draft: false
topics: []
concepts:
  - "[[phenomenal-sorites-problem]]"
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-09-10
last_curated:
---

**Date**: 2026-09-10
**Article**: [[phenomenal-sorites-problem|The Phenomenal-Sorites Problem]]
**Previous review**: [[deep-review-2026-07-28-phenomenal-sorites-problem|2026-07-28]]
**Lens**: Full comprehensive pass. The delta lens was spent before this review began (two commits since 07-28, neither a substantive edit to the article's own claims), so the ground was staleness, prior-resolution verification, and a fresh publisher-of-record citation sweep.
**Word count**: 3439 → 3431 (−8; concepts soft 2500 / hard 3500 — margin *grew* from 61 to 69)

## Verdict: FIX — one critical citation defect, caught by the 07-28 review's own deferred item coming due

## Critical Issues Found

### 1. Stale "working paper" citation, missing co-author, and a now-false parenthetical claim about the publisher of record

The 07-28 review closed with one deferred item: *"The Schwitzgebel subject-counting working paper's venue remains the one item to re-check if it reaches a confirmed journal."* **It has.** Verified at the publisher of record (Crossref record for the Taylor & Francis DOI, corroborated by OpenAlex):

> Schwitzgebel, E. & Nelson, S. R. — "When counting conscious subjects, the result needn't always be a determinate whole number." *Philosophical Psychology* **39**(3), 847–867. DOI `10.1080/09515089.2025.2520364`. Online 2025-06-16; print 2026-04-03.

Three compounding defects, all now resolved:

- **Missing co-author.** Both the References entry and the body attributed the paper to Schwitzgebel alone. **Sophie R. Nelson is second author.** Body now reads "A companion paper with Sophie Nelson (2026)"; the Tenet-4 paragraph now reads "The Schwitzgebel–Nelson extension".
- **A false statement about the publisher of record.** The body carried "(That paper's final venue and year were not confirmed at the publisher of record and it should be treated as a working paper.)" That sentence was true when written and is now false in every clause — venue, year, and status are all confirmed. Deleted (−23 words), which is what paid for the rest of this pass inside a 61-word ceiling.
- **Reference entry replaced** with the full verified tuple including DOI.

**Family resolution (§2.4 step 6).** The corpus-wide sweep on `"determinate whole number"` found three live articles citing this paper. [[moral-census-opacity]] and [[coupling-engagement-condition]] **both already carried the correct published form**; `phenomenal-sorites-problem` was the sole stale outlier. This is the inverse of the usual failure — here intra-corpus consistency would have *caught* the defect had anyone compared, but nothing does compare, so the outlier sat for four days after a sibling article was created carrying the right metadata. No propagation needed; the two correct siblings were left untouched.

### 2. Naturalism qualifier restored to the counting claim (quote-fidelity / over-concession)

The counting paper's abstract restricts its argument explicitly: *"on a wide range of naturalistic views of consciousness, the processes underlying consciousness are sufficiently complex to render it implausible that conscious subjects must always arise in determinate whole numbers."* The article stated the conclusion flat, without the naturalism restriction — quoting past a qualifier the source attaches, and in the direction that **overstates a threat to the Map**, which is not a naturalist framework. Body now reads "arguing that on those same naturalistic views…", anaphoric to "Assuming mainstream naturalism about consciousness" two sentences earlier in the same paragraph. Length-neutral in effect (absorbed by the deletion above).

## Medium Issues Found

### 3. Sorensen's objection pinned to the wrong Williamsonian doctrine

The article read: *"Williamson locates it in speakers' use, **which** Sorensen rejects for making definiteness relative to a discriminator."* The antecedent of "which" is speakers' use, but per Weatherson's review (raw text grepped, not summarised) the discriminator objection targets Williamson's *indiscriminability-based definition of definiteness*, not the use-grounding as such:

> "Secondly, indiscriminability is always indiscriminability by something, so on Williamson's account definiteness is only defined relative to a discriminator. Sorensen wants there to be absolute borderline cases, and absolute indefiniteness, so he cannot rest with this definition."

Weatherson lists this as one of *four* Sorensen–Williamson disagreements. The 07-28 review's substantive finding stands — Sorensen does reject Williamson's account on this ground — but the welding of the objection onto the use-grounding clause was a compression. Widened to "and Sorensen rejects **his account** for making definiteness relative to a discriminator" (+2 words), which is what Weatherson supports.

### 4. Jago issue number (family resolution, zero-word)

`*Thought: A Journal of Philosophy*, 1, 320–329` → `1(4), 320–329`. Crossref confirms volume 1, **issue 4**. [[coupling-engagement-condition]] already carried `1(4)`; the two now agree.

## Verification of the 07-28 Review's Own Resolutions

Per the standing discipline that a prior review's recorded fixes are verification targets rather than closed questions. **All three held.**

- **"Absolute borderline cases" re-attributed from *Blindspots* (1988) to *Vagueness and Contradiction* (2001)** — **CONFIRMED at the publisher of record.** Oxford Academic registered chapter DOIs for the 2001 book with Crossref; "Absolute Borderline Cases" is `10.1093/oso/9780199241309.003.0002` (Ch. 2, directly after "Introduction" `.003.0001`). "Truthmaker Gaps" is `.003.0012` in the same book, so the article's pairing of the truthmaker-gap route with the 2001 volume is also right. The 07-28 fix was correct.
- **Sorensen rejects Williamson's grounding** — **CONFIRMED in substance**, refined for precision (Medium 3 above).
- **Jago's objection = incompatibility with higher-order vagueness** — **CONFIRMED verbatim** against the OpenAlex abstract: *"argue that the view is incompatible with higher-order vagueness … Since it is highly likely that there is higher-order vagueness, truthmaker-gap epistemicism is in an uncomfortable position."* The record's `mag` id (1782077689) predates 2022, ruling out training-contamination.

## Citation Web-Verify Ledger (publisher of record)

- **Schwitzgebel, E. & Nelson, S. R. (2026)**, counting conscious subjects — **real-wrong-metadata → corrected** (was "Schwitzgebel, E. (~2025) … Working paper (venue unconfirmed)"; now *Philosophical Psychology* 39(3), 847–867, DOI added, co-author added). Critical 1.
- **Jago, M. (2012)** — **real-wrong-metadata → corrected** (issue number added: 1(4)). Thesis re-verified independently via OpenAlex abstract.
- **Williamson, T. (1994)**, *Vagueness*, quote "small differences in meaning, not to small differences in the objects under discussion" (pp. 230–231) — **real-correct, verbatim, pages correct.** Re-verified this pass by a route independent of the 07-28 pass's summariser: the Sainsbury 1995 BJPS review PDF was downloaded and `pdftotext`-extracted, and the string located by offset in the **raw text** (offset 11858), reading *"he suggests that 'what distinguishes vagueness as a source of inexactness is that the margin for error principles to which it gives rise advert to small differences in meaning, not to small differences in the objects under discussion' (p. 230–1)."* The article's fragment and its surrounding paraphrase both track the source.
- **Sorensen, R. A. (2001)**, *Vagueness and Contradiction* — **real-correct**; chapter structure confirmed via registered chapter DOIs (see above).
- **Sorensen, R. A. (1988)**, *Blindspots* — **real-correct** as a bibliographic entry; body claim correctly no longer leans on it for the 2001 material.
- **Schwitzgebel, E. (2023)**, Borderline consciousness — **real-correct**; *Philosophical Studies* 180(12), 3415–3439 confirmed field-by-field at Crossref.
- Carried forward, References block unchanged and verified across three prior passes: **Simon 2017, Hall 2023, Antony 2006 ×2, Tye 2021, Papineau 2002, SEP Sorites §3.2, Southgate & Oquatre-huit 2026-03-24, Southgate & Oquatre-sept 2026-05-11** — all real-correct.

**No fabricated citations.** Superlative-currency helper returned **0** candidates. Inline↔References cross-check: all 15 entries have a body locus except the SEP entry, which remains the known background-source near-orphan the 07-28 review accepted; no churn.

## The `coupling-engagement-condition` Piped-Label Seam (task-brief target)

The 2026-09-06 commit that created [[coupling-engagement-condition]] reached into this article and wrapped **existing prose** in a piped link, asserting an identity: *"contrasted here with [[coupling-engagement-condition|the coupling's mere engagement]], which is what secures the on/off subject-fact."*

**The label is accurate.** The target article's own opening states the relationship in the same direction and in nearly the same words: *"[[phenomenal-sorites-problem|The phenomenal-sorites problem]] installs it as the truth-maker for the sharp on/off fact about whether a subject exists."* Both pages agree on what the construct does and which article installed it. No misdescription; no fix needed.

**Considered and declined**: the label asserts "which is what secures" flatly, where the target page disclaims having *shown* engagement to be non-graded and lists "Whether engagement is genuinely non-graded" under what it does not settle. This is not over-claiming, because the label makes a *role-assignment* claim inside the Map's framework (which construct bears the on/off fact), not an evidential one — and it mirrors the body's existing phrasing about the interface threshold verbatim ("so it is not the construct that secures the on/off fact"). Changing one and not the other would introduce an inconsistency where none exists. Left alone deliberately.

## Reasoning-Mode Classification (editor-internal)

- Engagement with **Schwitzgebel & Nelson** (quadrilemma and the counting extension): **Mixed, Mode Two + Mode Three** — names the explicit naturalism assumption as the foundational move, denies it from Tenet 1, declines to claim refutation ("the Map does not claim to have refuted ontic vagueness"). Strengthened this pass: the naturalism restriction is now stated for the counting paper too, so the Mode Two identification covers both arguments rather than only the quadrilemma.
- Engagement with **Sorensen** (truthmaker-gap route declined): **Mode One** — declined on grounds internal to Sorensen, via Jago's higher-order-vagueness objection. Re-verified against Jago's abstract this pass.
- **Antony** is a constraint the Map accepts, not an opponent; no mode applies.
- **No editor-vocabulary label leakage** in prose (scanned for all eleven forbidden tokens plus ANSI `[1m`; all absent).

## Calibration Check

No possibility/probability slippage. The lead frames the Map's stake as "motivation rather than as an established result"; the epistemicism section states the preference is conditional and "not a proof that consciousness has a sharp boundary"; the closing paragraph concedes the open trigger problem. The over-concession sweep (tells: *no possible / cannot ever / in principle undetectable*) found the candidate phrases all doing legitimate work — "cannot know *in principle*" is the definition of epistemicism, and "nothing could 'fix' a boundary we are constitutionally unable to detect" is reported as an objector's retort, not asserted. **The one over-concession found was Critical 2**, and it ran in the direction of overstating an opponent's reach rather than the Map's.

## Strengths Preserved

- The three-loci taxonomy (ontic / semantic / epistemic) and its front-loaded placement in the lead.
- The Fact-Maker Problem section, still the article's strongest original contribution — untouched structurally for a third consecutive review.
- The careful Tye characterisation (affirms vagueness *via* panpsychism), and the Antony/Papineau disambiguation on conceptual sharpness.
- The interface-threshold / existence-fact disambiguation, verified intact in both body and Further Reading.

## Remaining Items

None deferred. The 07-28 review's sole open item is now closed.

## Stability Notes

**The article's argumentative core is converged and was not touched.** Every change this pass was citation-metadata or source-fidelity; no philosophical claim was added, removed, or re-weighted. Four passes have now left the Fact-Maker Problem structure untouched.

Bedrock disagreements stand and must not be re-flagged: ontic-vagueness proponents (Schwitzgebel, Nelson, Hall, Tye) reject the Map's framework from outside it, and epistemicism's counterintuitiveness is a declared cost, not a defect. The residual open question — whether a graded physical trigger is compatible with a sharp ground — is honestly flagged in-text and is now worked out at length on its own page, [[coupling-engagement-condition]].

**Process note for future reviews.** The 07-28 pass's "re-check if it reaches a confirmed journal" line is the reason this defect was findable in one query. A deferred citation item written as a *specific, checkable condition* survives handoff between reviews; "citations verified" does not. Note also that the §2.4 skip rule would have licensed skipping this pass entirely — the References block was unmodified since 07-28 — and the skip would have missed a critical defect. **A reference block does not have to change for a citation in it to become wrong: the world moves under a "working paper" entry.** Any entry carrying a provisional marker (*working paper*, *venue unconfirmed*, *forthcoming*, *preprint*) should be treated as re-verifiable on every pass regardless of whether the block was edited.
