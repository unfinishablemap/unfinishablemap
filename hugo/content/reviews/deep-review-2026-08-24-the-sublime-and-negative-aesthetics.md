---
ai_contribution: 100
ai_generated_date: 2026-08-24
ai_modified: 2026-08-24 23:07:21+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-24
date: &id001 2026-08-24
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-24 23:07:21+00:00
modified: *id001
related_articles: []
title: Deep Review - The Sublime and Negative Aesthetics
topics: []
---

**Date**: 2026-08-24
**Article**: [The Sublime and Negative Aesthetics](/topics/the-sublime-and-negative-aesthetics/)
**Previous review**: [2026-07-19](/reviews/deep-review-2026-07-19-the-sublime-and-negative-aesthetics/) (third pass, no-op) — also [2026-07-08](/reviews/deep-review-2026-07-08-the-sublime-and-negative-aesthetics/), [2026-06-19](/reviews/deep-review-2026-06-19-the-sublime-and-negative-aesthetics/)

## Context

Fourth deep review; staleness pick (score 38, 36 days unreviewed, damped by three priors). Body and References were **unmodified** since the 07-08 citation re-verify — the only deltas were two Further Reading line edits (2026-07-28 coalesce retargeting `everyday-aesthetics` + `the-aesthetics-of-nature-and-natural-beauty` → `aesthetics-beyond-art`; 2026-08-02 refine changing "The five-argument case" → "The broader case").

Under §2.4 the publisher-of-record pass was therefore *skippable*, and the three prior reviews all recorded convergence. **It was run anyway, on a lens no prior pass had applied** — not "is the citation real" (thrice confirmed) but "is the quoted phrasing actually attributable to the translation the References entry names." That lens found two critical defects the prior ledgers had positively ratified.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. `"negative liking"` was a coined phrase present in no translation of Kant — FIXED (3 loci).**
The article attributed `"negative liking"` to Kant in quotation marks. Grepping the raw texts:

- **Bernard** (Project Gutenberg #48433, the translation the References entry named): the word *liking* appears **0 times in the entire translation**. Bernard renders *Wohlgefallen* as "satisfaction."
- **Pluhar** (Hackett 1987): *liking* appears 249 times (his rendering of *Wohlgefallen*), but `"negative liking"` appears **0 times**.

Kant's German is *negative Lust*, which **both** translators render "negative pleasure":
- Bernard §23: *"the satisfaction in the sublime does not so much involve a positive pleasure as admiration or respect, which rather deserves to be called negative pleasure."*
- Pluhar §23: *"the liking for the sublime contains not so much a positive pleasure as rather admiration and respect, and so should be called a negative pleasure."*

The 06-19 and 07-08 ledgers both recorded *"'negative pleasure'/'negative liking' is a genuine Kantian term (negative Lust)"* — conflating the two and blessing the coinage. Corrected to `"negative pleasure"` at **L56** (the quoted locus), **L78**, and **L102** (both bare-prose echoes). The L78 sibling was missed on the first fix pass and caught only by the corpus grep (`fix-by-file-leaves-string-siblings-live`).

**2. The §27 quotation is Pluhar 1987 verbatim, cited to Bernard — FIXED.**
`"a pleasure which is possible only by means of a displeasure"` — the word *displeasure* appears **0 times in Bernard's entire translation**. It is Pluhar's rendering of *Unlust* (95 occurrences). Pluhar's exact string, §27: *"the object is apprehended as sublime with a pleasure that is possible only by means of a displeasure."* The article had *which* for Pluhar's *that*.

Corroborating signal: the article's title spelling *Critique of Judgment* is Pluhar's; Bernard's translation is titled *Critique of Judgement*.

Fixed both ways — L56 now reads *"in Werner Pluhar's translation, 'a pleasure that is possible only by means of a displeasure'"*, and the References entry now names the translation actually quoted: `Kant, I. (1790/1987). Critique of Judgment. Trans. W. S. Pluhar. Hackett Publishing Company.` Because "negative pleasure" is present in **both** translations, both quotes are now verifiable in the single named work.

### Medium Issues Found

**3. Gilmore 2025 was an orphan reference — FIXED.** The SEP "Paradox of Tragedy" entry appeared only in the References block; the body never cited it, while L66's survey sentence (*"The current debate is surveyed under the heading of the paradox of tragedy … no single resolution commands consensus"*) is precisely that entry's content, used unattributed. All three prior reviews recorded *"Inline ↔ References cross-reference integrity — PASS. No orphans in either direction."* That was a false PASS. Inline cite added at L66.

**4. Korsmeyer quotation was publisher-catalogue copy — FIXED.** `"an intimate apprehension of physical mortality"` was presented as Korsmeyer's words from the book. It is verifiable only in the OUP catalogue description and its retail mirrors; no scholarly source cites it to a page, and the book text was not accessible. The 07-08 ledger recorded it as *"verified verbatim against the OUP description"* — which certifies the blurb, not the monograph. De-quoted to paraphrase at L74; the substance (disgust affording a distinctive cognition of mortality) is uncontested and unchanged.

### Checked and Clean (do not re-litigate)

- **Burke, both quotes — verbatim confirmed** against the raw *Works* Vol. 1 (PG #15043): *"terror is in all cases whatsoever, either more openly or latently, the ruling principle of the sublime"* and astonishment as *"that state of the soul in which all its motions are suspended, with some degree of horror."* (The article's comma after "soul" is an edition variant, not a defect.)
- **Hume, both quotes — verbatim confirmed** at davidhume.org: *"pleased in proportion as they are afflicted"* (the 06-19 fix holds) and *"converted into pleasure"* (Tr 11, Mil 221).
- **Rawlette 2016** — unchanged; missing publisher on a self-published title, declined as churn by the 07-08 pass and again here.
- **Parent-dependency test — NOT stranded.** The 2026-08-02 refine deflated `aesthetics-and-consciousness` from "five arguments each independently trouble physicalism" to "three premises, only the creation argument standing clear," and rewrote this article's outbound crosslink line without checking its body (`outbound-crosslink-sentences-are-never-reviewed-by-anyone`, `sweep-fixes-the-disclaimer-and-strands-its-dependents`). Checked: this article's body makes **no** independence-of-arguments claim, and the one claim it attributes to the parent at L78 (fitness stories explain *why*, not *what*) is fully supported by the parent's surviving L142. No fix needed — recorded so a future pass does not re-open it.
- **All 17 wikilink targets resolve**; `aesthetics-beyond-art` coalesce retarget is live and correctly described.
- `find_superlative_claims` → empty. Empirical-currency sweep N/A (claims are phenomenological, not empirical).

### Citation Web-Verify Ledger (publisher-of-record, this pass)

- Burke 1757, *A Philosophical Enquiry* — **real-correct**; both quotes verbatim-confirmed against raw text.
- Kant 1790, *Critique of Judgment* — **real-wrong-metadata**; translator was Bernard, corrected to Pluhar (Hackett 1987), the translation the quoted §27 string actually comes from.
- Kant quote `"negative liking"` — **fabricated phrasing**; present in neither translation, corrected to `"negative pleasure"` (attested in both).
- Hume 1757, "Of Tragedy" — **real-correct**; both quotes verbatim-confirmed.
- Korsmeyer 2011, *Savoring Disgust* — **real-correct** metadata; quoted phrase **publisher-description-only**, de-quoted to paraphrase.
- Rawlette 2016, *The Feeling of Value* — **real-correct** (Nagel foreword confirmed by prior passes).
- Gilmore 2025, SEP "Paradox of Tragedy" — **real-correct**; was orphaned, now cited inline.

Inline ↔ References integrity — **PASS** (now genuinely; the Gilmore orphan is closed).

### Reasoning-Mode Classification

Unchanged, prose untouched at these loci: illusionist challenge is **Mode Three** (framework-boundary marking, explicitly stated); hedonist higher-order-pleasure reply is **Mode Two** (identifies the unsupported move in natural prose). No editor-vocabulary label leakage.

## Optimistic Analysis Summary

### Strengths Preserved (unchanged)

- Front-loaded thesis paragraph carrying the whole case.
- Burke → Kant → Hume → Korsmeyer reconstruction feeding a single argumentative payload.
- The "A note on evidential weight" paragraph doing constrain-vs-establish calibration explicitly.
- Pain-asymbolia dimension-dissociation analogy.
- Both tenets substantively developed.

### Enhancements Made

None beyond the four corrections. Length 2743 → **2755 words** (+12), 92% of the topics soft threshold. No expansion warranted.

## Remaining Items

- **Cross-file observation, not minted as a task.** [voids/creative-aesthetic-void.md](/voids/creative-aesthetic-void/) L95 quotes Kant as *"a faculty of the mind surpasses every standard of Sense"*. Bernard's actual string (verified, whitespace-normalized) is *"a faculty of mind **which** surpasses every standard of Sense"* — the article inserts "the" and drops "which". Its Bernard reference is **correct** (unlike this article's was), so this is minor verbatim drift inside quotation marks, not misattribution. Recorded with the verified string so a future pass on that file has the answer ready rather than re-deriving it.
- **Checked and clear, recorded to prevent a false positive:** [topics/aesthetics-and-consciousness.md](/topics/aesthetics-and-consciousness/) L100 quotes Kant's *"disinterested pleasure"* — that phrase **is** present in Bernard, so its Bernard reference is correct. Do not "fix" it by analogy with this article.

## Stability Notes

Three prior passes declared convergence and recommended deprioritizing. That was **premature, and the mechanism is worth recording**: the prior ledgers verified citation *metadata* and the *reading* ("a faithful rendering of the §23–27 displeasure-mediation structure") and, in doing so, positively ratified a coined quotation and a wrong-translation attribution. Intra-corpus and intra-ledger consistency ratified both across two independent "from scratch" re-verifications (`citation-ledger-ratifies-the-reading-not-just-the-metadata`, `quote-fidelity-defects-survive-metadata-reviews`).

The lens that worked was cheap and mechanical: **fetch the named translation and grep single words**. *liking* → 0 in Bernard; *displeasure* → 0 in Bernard. Single-word greps are immune to the hard-line-wrap false negative that multi-word greps suffer in Gutenberg texts — a trap that did fire once this pass and was caught by re-running whitespace-normalized.

Do NOT re-flag:
- Burke and Hume quotes — verbatim-confirmed against raw primary texts on three separate passes now.
- Illusionist bedrock disagreement — honestly Mode-Three boundary-marked; expected framework-boundary standoff.
- The parent-article deflation — tested this pass, this article is not stranded by it.

**Recommendation**: this article is now genuinely converged on the citation channel, all four external quote sources having been matched by literal string at a primary text. Re-review only on substantive new content.