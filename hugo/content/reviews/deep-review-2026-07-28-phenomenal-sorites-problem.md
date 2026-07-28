---
ai_contribution: 100
ai_generated_date: 2026-07-28
ai_modified: 2026-07-28 11:36:56+00:00
ai_system: claude-opus-5
author: null
concepts:
- '[[phenomenal-sorites-problem]]'
created: 2026-07-28
date: &id001 2026-07-28
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - The Phenomenal-Sorites Problem
topics: []
---

**Date**: 2026-07-28
**Article**: [The Phenomenal-Sorites Problem](/concepts/phenomenal-sorites-problem/)
**Previous review**: [2026-07-19](/reviews/deep-review-2026-07-19-phenomenal-sorites-problem/)
**Lens**: Citation web-verify (existence/metadata, quote fidelity, empirical-claim fidelity) on the coalesce-introduced reference block.
**Word count**: 3417 → 3439 (+22; concepts soft 2500 / hard 3500 — 61 words of margin retained)

## Verdict: FIX — wrong-work attribution and a reversed author position, both introduced by the 2026-07-27 coalesce and never verified

## Why this pass found what two prior reviews did not

The 2026-07-19 review recorded "Citation Web-Verify — **skipped** per §2.4 skip rule: References block unmodified since the 2026-07-11 review." That was true when written. Then commit `7d434ab86 auto(coalesce)` merged [epistemicism-about-consciousness](/concepts/phenomenal-sorites-problem/) into this article and **grew the reference list from 8 entries to 15**. The 07-11 ledger covered only the original 8 (Schwitzgebel ×2, Simon, Hall, Antony ×2, Tye, Papineau). The seven entries the coalesce carried in — Williamson 1994, Sorensen 1988, Sorensen 2001, Jago 2012, SEP Sorites, and two Map self-cites — had **never been verified in any pass**. Both real defects below live in that unverified block.

This is the owed-web-verify seam in its coalesce variant: a complete-looking ledger inherited forward stops covering the current reference list the moment content is merged in from another article. **A coalesce should be treated as invalidating an inherited citation ledger outright.**

## Critical Issues Found

### 1. Wrong-work attribution — "absolute borderline cases" cited to *Blindspots* (1988)

The article read: *"Sorensen reached a version of the view independently in* Blindspots *(1988) … introducing 'absolute borderline cases'."*

"Absolute Borderline Cases" is a **chapter of *Vagueness and Contradiction* (OUP, 2001)** — verified at the Oxford Academic chapter landing page and corroborated by the NDPR review, which places the absolute/relative distinction at Ch. 1.2 and the truthmaker treatment at Ch. 1.11. Both books are real and both are correctly in the reference list; the term was simply pinned to the wrong one. This is the verbatim-quote-cited-to-wrong-work pattern applied to a technical term rather than a quotation: right author, right view, **wrong work**. Re-attributed, not deleted.

The article's *gloss* of the term was independently correct and was preserved: absolute borderline cases are those where ignorance is not relative to any cognitive system, hence insurmountable in principle.

### 2. Reversed author position — Sorensen given Williamson's word-not-world grounding

The same sentence described Sorensen as *"treating the sorites as a paradox about the* word *rather than the world."* This is backwards. Per SEP §3.2 and Weatherson's review of *Vagueness and Contradiction*, grounding sharp boundaries in speakers' use is **Williamson's** signature move, and **Sorensen explicitly rejects it** — he objects that it makes definiteness "only defined relative to a discriminator," which is precisely why he requires *absolute* borderline cases.

Three compounding problems, all now resolved:

- **Internal contradiction.** Four sentences earlier the article says Sorensen holds that "vagueness pervades the way the world is divided" — the direct opposite of "a paradox about the word rather than the world," with both attributed to Sorensen in adjacent paragraphs.
- **Self-undercutting.** The article's own Fact-Maker Problem section correctly identifies Sorensen's route as **truthmaker-gap** — the sharp fact has *no* truth-maker at all. A theorist who grounds boundaries in use-facts is not a theorist who denies truth-makers. The misattribution contradicted the article's own downstream argument.
- **False harmonization.** "Both authors share the core" flattened a divergence Sorensen himself presses against Williamson.

Fixed by re-attributing the term to the 2001 book, deleting the word-not-world clause, keeping the genuine shared core (determinate fact, hidden location, classical logic preserved), and naming the divergence explicitly with a forward pointer to where it does work.

### 3. Over-generalized premise in the Fact-Maker Problem

"…a truth-maker that **generic epistemicism** got for free from use" → "…that **Williamson's version** got for free from use." Generic epistemicism did *not* get it for free from use: Sorensen, the other founder named in the same article, denies truth-makers outright — as the very next paragraph says. The narrower claim is the true one and is what the argument actually needs.

## Medium Issues Found

### 4. Jago's objection under-specified (empirical-claim fidelity)

"Mark Jago (2012) argues this is unstable" was directionally right but uninformative. Jago's actual argument, per the published abstract: truthmaker-gap epistemicism **is incompatible with higher-order vagueness**, which Sorensen is "adamant" exists — so the view is in an uncomfortable position *by Sorensen's own lights*. Sharpened to name the objection. This strengthens the Map's stated reason for declining the truthmaker-gap route: the objection is internal to Sorensen, not imported.

## Citation Web-Verify Ledger (publisher of record)

Newly-verified block (coalesce-introduced; never previously checked):

- Williamson, T. (1994). *Vagueness*. Routledge — **real-correct**. Margin-for-error framework confirmed at SEP Sorites §3.2.
- Williamson quote, "small differences in meaning, not to small differences in the objects under discussion" (pp. 230–231) — **real-correct, verbatim**. Confirmed against Sainsbury's review "Vagueness, Ignorance, and Margin for Error," which quotes the full sentence and cites pp. 230–1. Article's fragment matches the source string exactly; page range correct.
- Sorensen, R. A. (1988). *Blindspots*. Clarendon Press — **real-correct** as a bibliographic entry; SEP §3.2 cites it as an epistemicist source. **Body claim mis-attributed to it — fixed (Critical 1 & 2).**
- Sorensen, R. A. (2001). *Vagueness and Contradiction*. OUP — **real-correct**. Truthmaker-gap epistemicism and "Absolute Borderline Cases" both confirmed as this book's content.
- Jago, M. (2012). The Problem with Truthmaker-Gap Epistemicism. *Thought: A Journal of Philosophy* — **real-wrong-metadata (incomplete)**: volume and pages were absent. Corrected to *1*, 320–329. DOI 10.1002/tht3.49 confirmed at Wiley. Thesis re-verified (Medium 4).
- SEP (2025). Sorites Paradox, §3.2 "The Epistemic Theory" — **real-correct**. Section number *and* exact title confirmed at plato.stanford.edu; entry last substantively revised Tue Aug 26, 2025; authors Raffman and Hyde.
- Southgate & Oquatre-huit (2026-03-24), Composition and Consciousness — **real-correct**; target file live. AI pseudonym is corpus convention (a known false-alarm class), retained.
- Southgate & Oquatre-sept (2026-05-11), The Interface Threshold — **real-correct**; target file live. Pseudonym retained.

Carried forward from the 2026-07-11 ledger, References block unchanged for these eight, no re-verification triggered: Schwitzgebel 2023 (real-correct), Schwitzgebel working paper (venue correctly flagged unconfirmed), Simon 2017, Hall 2023, Antony 2006 ×2, Tye 2021, Papineau 2002 — all real-correct.

**No fabricated citations.** Superlative-currency helper returned 0 candidates.

**Inline ↔ References cross-check**: all 15 entries accounted for. One near-orphan — the SEP Sorites entry is not cited by name inline, functioning as a background source for "The Epistemic Theory of Vagueness" section. Left in place as conventional; not worth churn.

## Subject-Specific Checks (per task brief)

- **Epistemic / metaphysical slippage** — clean. The three-loci taxonomy holds its distinctions throughout: the boundary is metaphysically sharp and epistemically hidden, and the article never lets "we cannot detect a difference" drift into "there is no difference." The "no external measure" passage grounds an *epistemic* conclusion in a *metaphysical* premise, but says so explicitly ("is exactly what an interactionist framework denies") rather than sliding.
- **Bracket-notation / sync hazard** — none present. No double-bracket QEC-style notation of the `[n,k,d]` family (which sync silently strips as a wikilink unless backtick-wrapped); the only bracketed tokens are the enumerations (a)–(d), which sync handles.
- **`[1m]` ANSI artifact** — absent.

## Reasoning-Mode Classification (editor-internal)

- Engagement with Schwitzgebel (quadrilemma → ontic vagueness): **Mixed, Mode Two + Mode Three** — identifies the quadrilemma's explicit naturalism assumption as the foundational move, denies it from Tenet 1, and declines to claim refutation. Unchanged from 07-19; still honest.
- Engagement with Sorensen (truthmaker-gap route): **Mode One** — the Map declines the route on grounds internal to it (Jago's higher-order-vagueness objection, which Sorensen's own commitments generate). Strengthened by Medium 4.
- No editor-vocabulary label leakage in prose.

## Calibration Check

No possibility/probability slippage. The lead frames the Map's stake as "motivation rather than as an established result"; the epistemicism section states the preference is conditional and "not a proof that consciousness has a sharp boundary"; the costs paragraph concedes the open problem (a graded physical trigger would reintroduce the sorites at the coupling's switch-on). A tenet-accepting reviewer would not flag any claim as overstated.

## Strengths Preserved

- Three-loci taxonomy (ontic / semantic / epistemic) and the conditional Tenet-4 stake.
- Careful Tye characterisation — affirms vagueness via panpsychism, resisting the common misfiling.
- Antony/Papineau disambiguation on conceptual sharpness.
- The interface-threshold / existence-fact disambiguation from 07-11 — verified still intact after the coalesce, in both body and Further Reading.
- The Fact-Maker Problem section, which is the article's strongest original contribution; Critical 3 sharpened its premise rather than touching its structure.

## Remaining Items

- The Schwitzgebel subject-counting working paper's venue remains the one item to re-check if it reaches a confirmed journal.
- SEP entry is a References-only background source (see cross-check above). Cosmetic; no task minted.

## Stability Notes

The two critical findings were **coalesce-introduced**, not drift in previously-reviewed prose — the article's original 8 citations remain clean across three passes. Do not read this FIX verdict as reopening the converged core.

Bedrock disagreements stand and should not be re-flagged: ontic-vagueness proponents (Schwitzgebel, Hall, Tye) reject the Map's framework from outside it, and epistemicism's counterintuitiveness is a declared cost, not a defect. The residual open question — why a non-physical coupling's engagement-condition would be non-graded where physical triggers are graded — remains honestly flagged in-text as the load-bearing step.

**Process note for future reviews**: the §2.4 "References unmodified since last review" skip rule is unsafe across a coalesce, which can grow the reference list while leaving inherited-ledger prose looking complete. Treat any `auto(coalesce)` commit in a file's history as invalidating the prior citation ledger and re-verify the full list.