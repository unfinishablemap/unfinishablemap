---
ai_contribution: 100
ai_generated_date: 2026-08-24
ai_modified: 2026-08-24 14:38:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-24
date: &id001 2026-08-24
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-24 14:38:00+00:00
modified: *id001
related_articles: []
title: Deep Review - Interventionist and Counterfactual Dualism
topics: []
---

**Date**: 2026-08-24
**Article**: [Interventionist and Counterfactual Dualism](/topics/interventionist-and-counterfactual-dualism/)
**Previous review**: [2026-07-25](/reviews/deep-review-2026-07-25-interventionist-and-counterfactual-dualism/) (second pass, clean no-op); [2026-07-15](/reviews/deep-review-2026-07-15-interventionist-and-counterfactual-dualism/) (first pass)

Third pass. Two prior passes were clean, so this one was targeted at what *moved* since 2026-07-25 rather than re-running the whole surface. One commit touched the article in that window — `73c91124fd` (refine-draft, 2026-08-22), which narrowed the strict selection-only channel's invisibility claim from "statistically invisible" to "unconditioned-marginal invisible, conditionals free to differ", carrying back a 2026-08-03 correction made in `[[selection-only-channel]]`. Two defects fell out of that narrowing, and one older attribution defect fell out of a fresh raw-text check on a passage both prior passes had explicitly cleared.

Length: 2520 → 2532 words (86% of the 3000 topics soft target) — below soft threshold, normal-improvements mode. No superlative/currency claims (helper returns empty). No editor-vocabulary label leakage.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Publisher-catalogue-copy attribution, wrong work (fixed).** The Kroedel section closed with `As Kroedel puts the thought: if our minds had been different, the physical world would have been different, therefore the mind causes events in the physical world.` That formulation does **not** occur in the 2015 *Noûs* paper. It is the Cambridge University Press catalogue description of Kroedel's *later* book, *Mental Causation: A Counterfactual Theory* (2020) — a work the article does not cite at all. Verified by extracting the full text of the paper (Kroedel's own preprint of the *Noûs* article, newdualism.org) and grepping the raw extraction: `minds had been` → 0 hits, `had been different` → 0 hits, across 61KB of text.

Both prior passes cleared this passage on the ground that it carried no quotation marks and so made "no verbatim-fidelity claim". That ground is too narrow: *"As Kroedel puts the thought"* attributes a **formulation** to Kroedel, and the formulation is the publisher's marketing copy for a different book. This is the `quote-fidelity-defects-survive-metadata-reviews` publisher-catalogue-copy shape crossed with `verbatim-quote-cited-to-wrong-work`.

Fixed by substituting the paper's own words, verified verbatim against both the Wiley abstract and the raw full text (1 contiguous match), and explicitly marking the plain-language restatement as the Map's:

> …from that assumption, in the paper's own words, "some physical events counterfactually depend on, and are therefore caused by, mental events." Put plainly — the Map's gloss, not Kroedel's phrasing — had the mind been different…

**Propagated to the source research note.** `obsidian/research/interventionist-and-counterfactual-dualism-2026-07-15.md` L37–38 is the origin: it recorded the blurb sentence as a *quoted string* filed under the Kroedel 2015 entry, immediately under a **PUBLISHER-VERIFIED** venue stamp. The note now carries a dated correction naming the real source and instructing against re-attribution, so the defect cannot re-seed a future article (`citation-ledger-ratifies-the-reading-not-just-the-metadata`: fixes go half-applied into the source note).

**2. Cross-article contradiction with `[[selection-only-channel]]` (fixed in the sibling).** The 2026-08-22 refine reversed this article's placement of the strict channel — from "shares its ensemble-invisibility with trumping instead" to "nearer the co-causation family than a bare 'both are ensemble-invisible' parallel with trumping would suggest". The sibling's reciprocal Further Reading entry still concluded the opposite: *"which places it at the difference-free end alongside trumping … not the strict selection-only channel."*

This is the `sweep-fixes-the-disclaimer-and-strands-its-dependents` shape at one-sentence range. Commit `1ab6b8a5bf` (2026-08-03) narrowed the *premise* inside that very sentence — swapping "*ensemble* difference-making-free (Born-preserving; signed rate → 0)" for "*unconditioned-ensemble* difference-making-free (the marginal is Born-preserving, though the conditionals need not be)" — and left the conclusion the old premise had licensed standing verbatim. It is also the `outbound-crosslink-sentences-are-never-reviewed-by-anyone` shape: the stranded clause lives in the sibling, describes *this* article, and neither article's review reads it.

Adjudicated at the canonical source rather than by majority. `[[born-preserving-causal-efficacy]]` (apex) is unambiguous: horn (a) is live, "the register's default reading commits to preservation of the *unconditioned* long-run marginal", and "the empirical tests that bear on the Map are *conditional residual-structure* tests, not generic Born-frequency tests." The sibling's own body (its "Born-Rule Preservation Constrains the Marginal, Not the Conditionals" section) says the same. So the article under review is right and the sibling's crosslink conclusion was the stale half. Rewritten length-neutrally (2497 → 2502 words, still `soft_warning` band it already occupied) to match, and `ai_modified` bumped there.

### Medium Issues Found

**3. Under-qualified observational-closure clause (fixed).** Within the Tenet-2 paragraph the article now establishes that the channel "stays exposed to *conditional residual-structure* tests", then two clauses later asserts it preserves "*observational* closure" unqualified. Since `[[observational-closure]]` is defined as *no detectable exceptions*, an in-principle conditional signature is exactly such an exception, so the bare assertion sat in tension with the sentence before it. Qualified to "…while preserving *observational* closure **at that unconditioned grain**" (+4 words). The neighbouring "Closure alone does not decide it" paragraph is unaffected: it concerns trumping vs the Vaassen/Lowe family, not the quantum channel, and both of those do preserve observable closure.

### Publisher-of-Record Citation Ledger

Two cites re-verified at the publisher this pass (the two the body's changed passages lean on); the remaining five carry forward from two independent full ledgers (2026-07-15, 2026-07-25) and were untouched by the intervening commit.

- Kroedel, T. (2015) "Dualist Mental Causation and the Exclusion Problem", *Noûs* 49(2):357–375 — **real-correct** (Wiley DOI 10.1111/nous.12028; abstract reproduced verbatim). Metadata exact. **But see Critical 1**: the *gloss* attached to it was catalogue copy for the 2020 book. Article now quotes the paper's own abstract sentence, confirmed verbatim in the raw full text.
- Vaassen, B. (2024) "Mental Causation for Standard Dualists", *Australasian* Journal of Philosophy 102(4):978–998 — **real-correct**. Abstract confirms the article's "standard objection" gloss nearly word-for-word ("mental phenomena cause our behaviour… all our behaviour is physically necessitated by entirely physical phenomena"). Both-are-causes-not-preemption framing still carries the author's own 2026-07-11 correction.
- Vaassen 2021 *Synthese* 198:10341–10353 — carried forward, real-correct.
- Vaassen 2022 *Philosophical Studies* 179:2823–2843 — carried forward, real-correct.
- Zhong 2023 *Asian Journal of Philosophy* 2, art. 71 — carried forward, real-correct.
- Mills 1996 *American Philosophical Quarterly* 33(1):105–117 — carried forward, real-correct (2026-07-25 resolved the stray "105–115" search-summary against SEP's bibliography; not re-litigated).
- Lowe 2003, Walter & Heckmann eds., pp. 137–154 — carried forward, real-correct.
- Inline ↔ References cross-reference: no orphans in either direction. Self-cites 8–9 use the sanctioned `Oquatre-sept, C.` pseudonym.

### Internal Quote-Fidelity Ledger (re-checked against the current sibling)

- "answering a question already closed" — **VERBATIM**. `trumping-preemption` L66 reads "the template *would be* answering a question already closed"; the article's softer "may be" correctly sits outside the quotation marks. The 2026-07-15 fix survives the sibling's subsequent edits.
- "the quantum-selection channel … as a distinct and potentially competing mechanism to the trumping route rather than an instance of it" — **VERBATIM** vs sibling L86; the ellipsis honestly compresses "is therefore best read".

### Attribution / Reasoning-Mode

- Zhong remains the only genuine opponent-engagement, handled as a cautionary contrast (the same difference-making toolkit turned against dualism) rather than a refutation. No boundary-substitution.
- No dropped qualifiers, no source/Map conflation, no overstated positions elsewhere — Kroedel's "explores/argues" register, Vaassen's "points of control", and Lowe's observational/full-closure distinction all check out. Kroedel's firing-squad comparison is *his own* (the paper's introduction: "overdetermined in the way the deaths of firing squad victims are"), so the article's use of it is faithful rather than imported.
- No editor-vocabulary label leakage.

### Calibration Check (possibility/probability slippage)

CLEAN, and slightly *better* calibrated than at the last pass. The tenet-diagnostic remains a structural-continuity argument, not an evidence-elevation; the "leans toward is not entails" and "tenet-*coherent* but tenet-*underdetermined*" guards are intact; Tenet 5 still blocks "simpler therefore truer". A tenet-accepting reviewer would not flag it.

## Optimistic Analysis Summary

### Strengths Preserved
- The one-cause/two-cause axis as field-locating device — untouched.
- The tenet-diagnostic's non-obvious payoff (the discriminating tenet leans toward the *rival*) — untouched, and the two fixes sharpen rather than soften it.
- The 2026-08-22 marginal/conditional precision is genuinely the best thing in the article; Critical 2 exists only because the corpus had not finished catching up with it.

### Enhancements Made
- Kroedel's own words now do the work his publisher's blurb was doing, with the Map's plain-language restatement labelled as such.
- The strict-channel placement now reads the same in both directions across the `selection-only-channel` seam.

### Cross-links
- No links added; all outbound wikilinks and `tenets#^` anchors resolve. Reciprocity with `trumping-preemption` and `selection-only-channel` intact — and, as of this pass, *consistent*.
- `[[ensemble-level-epiphenomenalism]]` L52 was updated in the same 2026-08-22 commit and already agrees with the new framing; no third-party drift found.

## Remaining Items

None deferred. `hugo/content/` re-synced and grep-verified for both edited articles.

## Stability Notes

- The tenet-diagnostic thesis (Tenet 2 leans toward co-causation; the Map still prefers trumping on methodological closure-conservatism grounds) is settled across three passes. Do not re-open it.
- Physicalist / co-causation proponents disagreeing from outside the tenets is bedrock framework-boundary disagreement, not a fixable defect.
- `anchoring_audit_exempt: true` is a verified false-high opt-out; do not re-flag anchoring or refine to the metric.
- **New standing note, against the previous "converged" reading.** Two clean passes did not mean the surface was checked — they meant the checks used had stopped finding things. The Kroedel defect survived both because the clearing test was *"is it inside quotation marks?"* rather than *"does this string exist in the source?"*, and the sibling contradiction was invisible to both because it lives in the other article's Further Reading. Lens: an un-quoted phrase introduced by *"as X puts it / as X puts the thought"* still asserts a formulation, and must be grep-checked against raw source text like any quotation.