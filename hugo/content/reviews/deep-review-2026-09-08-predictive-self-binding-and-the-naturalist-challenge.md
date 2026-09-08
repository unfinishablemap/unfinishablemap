---
ai_contribution: 100
ai_generated_date: 2026-09-08
ai_modified: 2026-09-08 18:43:16+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-08
date: &id001 2026-09-08
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-08 18:43:16+00:00
modified: *id001
related_articles: []
title: Deep Review - Predictive Self-Binding and the Naturalist Challenge
topics: []
---

**Date**: 2026-09-08
**Article**: [Predictive Self-Binding and the Naturalist Challenge](/topics/predictive-self-binding-and-the-naturalist-challenge/)
**Previous reviews**: [2026-07-27](/reviews/deep-review-2026-07-27-predictive-self-binding-and-the-naturalist-challenge/) (citation-metadata + quote-fidelity, no-op) · [2026-06-23](/reviews/deep-review-2026-06-23-predictive-self-binding-and-the-naturalist-challenge/) (orphan-integration) · [2026-06-22](/reviews/deep-review-2026-06-22-predictive-self-binding-and-the-naturalist-challenge/) (full)
**Word count**: 2792 → 2994 (+202), `status: ok` against topics soft 3000 / hard 4000 / critical 6000. 1006 words to hard; deliberately held **below** soft so future passes are not forced into length-neutral mode.

## Scope of This Pass

The article's body genuinely moved on 2026-09-07 (a `refine-draft` de-escalating the Bidirectional Interaction paragraph and re-attributing the third-eye / dispelling-the-illusion contrast), so this was not the cosmetic-bump no-op that five higher-scoring candidates would have been.

Two surfaces were unexamined and both yielded critical findings:

1. **A citation added *after* the last citation-verify sweep.** The 07-27 pass verified the then-existing cites; the 09-07 refine then appended **reference 10, Gładziejewski (2023)**, which had never been verified. Its own changelog entry states plainly: *"Neither author's exact wording was read this run."* Reading the primary source is what surfaced the critical finding below.
2. **Dependency freshness rather than self-modification.** Asking what *moved under* the article — per `convergence-damping-keys-on-self-modification-not-dependency-freshness` — surfaced a claim contradicted by the Map's own apex and concept-page discipline.

## Citation Web-Verify Ledger (publisher of record)

Only cites that were unverified or whose *content* was unchecked were re-run; the 06-22 metadata ledger stands for the rest.

- **Gładziejewski, P. (2023), *From Altered States to Metaphysics*** — **real-correct on metadata.** Crossref `10.1007/s13164-023-00709-6`: author `Paweł Gładziejewski`, container *Review of Philosophy and Psychology*, vol 16, issue 1, pp. 175–197. Publisher PDF (Springer, hybrid OA) downloaded and text-extracted; running header reads verbatim `Review of Philosophy and Psychology (2025) 16:175–197`, `Accepted: 26 September 2023 / Published online: 10 October 2023`. **Content: NOT faithful as deployed — see Critical Issue 1.**
- **Letheby, C. & Gerrans, P. (2017), *Self unbound*** — **real-correct**, and the load-bearing self-fictionalism quote **re-verified verbatim-exact independently of the 07-27 finding**: raw Europe PMC full-text XML for PMC6007152 pulled and grepped in Python; the quoted string matches at **offset 1956** with the source's `useful Cartesian fiction:` lead-in at offset 1930. Also confirmed at offset 4884/4892 that L&G do cite Sui and Humphreys, which is the premise the Millière equivocation charge (line 69) rests on.
- **Sjöstedt-Hughes, P. (2022), *Psychedelics and the limits of naturalism*** — **real-wrong-metadata, corrected (enriched).** Container adjudicated (below) and the masthead read at the publisher: `From The Philosopher, vol. 110, no. 2 ("The New Basics: Society")`. Reference 5 gained `110(2)`. **Both claims the article attributes to this review verified against the raw page**, not a summariser: the naturalism-is-not-neutral rejoinder (*"Naturalism is only one such proposed determination and there are multiple others"*, offset 21564; Spinozist veridicality at 21200-ish; panpsychism at 12755; cosmopsychism/"infinite intellect" in the same passage) and the controlled-hallucination tension (*"the 'controlled hallucination' theory of mind is incompatible with the sense of connectedness that features very prominently in the later sections on 'Naturalistic Spirituality'"*, offset 14743). Per `webfetch-confirmation-prompts-ratify-the-phrase-you-ask-about`, the WebFetch answer was **not** taken as the test — the page was curled, tag-stripped and grepped with printed offsets.
- **Letheby 2021, "fourth option"** — **substance verified, exact wording not.** The Sjöstedt-Hughes review confirms the structure (three prior responses plus a *"fourth way" / "fourth response"*, offset 19228), but Letheby's own phrase could not be grep-verified in a paywalled monograph. Quotation marks **removed** rather than left asserting an unverifiable verbatim; see Low Issues.
- **Carhart-Harris & Friston 2019; Deane 2021; Millière 2017; Metzinger 2003; Brains Blog 2019; Map self-cite** — not re-run. Verified 06-22, unchanged since, and the 07-27 pass confirmed the two corrections landed.
- **Superlative-claim currency sweep** — no superlative claims present (`find_superlative_claims` territory: the article makes no "first / largest / current record / to date" claims). Nothing to re-scope.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Polarity inversion of Gładziejewski's taxonomy — the contrast does not sort the possibilities the article says it sorts.** (§Why "More Real Than Real", was line 49.)

The article read: *"nothing beyond the model is being revealed … not access to any deeper layer of reality. **The contrast that sorts these possibilities is Gładziejewski's (2023)**: on one model psychedelics permit third-eye perception of metaphysical truth, on the other they dispel cognitive structures that block accurate perception."*

"These possibilities" refers back to {nothing revealed} vs {access to a deeper layer}. Gładziejewski's contrast does not divide those. In his §3.3, titled *"Revealing Truth?"*, he introduces both models in his own voice as accounts of how psychedelic states *could be truth-revealing about metaphysics* — *"Let me now sketch out a view of how acute psychedelic states could be on-track with respect to at least some metaphysical truths. We need to distinguish two models of how psychedelic states could be truth-revealing."* The dispelling model is the one where *"those truth-obstructing cognitive structures are removed, allowing one to enter a conscious state that better aligns with how the world is"*, and later *"selfless and timeless experiences are better aligned with ground truth about reality."* **Both branches affirm metaphysical access; they differ over the mechanism.** The article had recruited the inflationary branch as the label for a deflationary reading, and the truncation that made this possible was dropping the consequent clause — keeping "dispel cognitive structures that block accurate perception" while omitting "so that experience better aligns with how the world is."

The error runs **against** the Map. Gładziejewski takes Letheby and Gerrans (2017) as a *premise* — *"The experience of being a persisting self can be explained by a binding process that gives rise to the sense of being a simple, substance-like entity without actually tracking any such entity (Letheby and Gerrans 2017)"* — inside an argument that psychedelic states *"broaden the range of data that can guide and constrain metaphysical inquiry"*, worked through a case of **cosmopsychism**. So a published philosopher runs Letheby's own constructivist account of the self toward non-naturalist metaphysics; that is the Map's comforting-delusion reversal made independently in the peer-reviewed literature, and the article was spending it as a mere taxonomy while mis-stating the taxonomy.

**Fixed** by rewriting the passage as its own paragraph: both models stated correctly as truth-revealing variants, Letheby kept on the dispelling side with the honest qualification that *his* use of it stops at the self, and Gładziejewski's further move named with a forward pointer to the reversal. Both model names are now **quoted**, which is newly legitimate — they are verbatim in the source at offsets 55989 and 56327, and the 09-07 refine explicitly could not quote them because it had not read him.

*Note on classification*: this is **not** bedrock disagreement. Applying the §2 diagnostic — would a reviewer who fully accepts the Map's tenets still flag it? — yes, unambiguously; it is a misreport of what a cited source's distinction distinguishes, correctable inside the Map's framework.

**2. The cross-state convergence pattern cited as an unqualified discriminator, contradicting the Map's own published discount.** (§Why the Accounts Are Empirically Equivalent, was line 95.)

The article read: *"The discriminating work is therefore done not by psychedelic data but by broader theoretical commitments and **the corpus-wide convergence pattern**."*

The Map's own apex [altered-states-as-interface-evidence](/apex/altered-states-as-interface-evidence/) (line 82) states: *"So the convergence-of-altered-states pattern **cannot honestly be cited as multiple independent confirmations** of filter theory—the cluster carries the evidential weight of **one pattern, not six**."* [cross-mechanism-convergence](/concepts/cross-mechanism-convergence/)'s Evidential Calibration section adds that the pattern is *"an evidence-pattern strength indicator, not a tier-graduation … it does not by itself license upgrading a finding from one tier of the five-tier scale to another."* The sibling [psychedelics-and-the-filter-model](/topics/psychedelics-and-the-filter-model/) carries the qualifier attached to the claim in both places it makes it (lines 131, 145: *"taken as one phenomenological cluster rather than as multiple independent confirmations"*). This article made the claim naked.

This is the `sweep-fixes-the-disclaimer-and-strands-its-dependents` shape with a twist: the sibling's disclaimer landed **2026-05-14**, and this article was *created* **2026-06-22** — so it is not a stranded dependent but a `fresh-create-defect-tail`, importing pre-correction framing a month after the correction. Eleven review-passes' worth of intra-file reading could not see it; it is only legible when the target is opened.

**Fixed** by attaching the Map's own discount in the Map's own terms, with a piped link to the apex that owns the pattern.

### Medium Issues Found

**3. The §Relation to Site Perspective lead did not survive its own de-escalation.** *"Predictive self-binding engages four of the Map's tenets directly"* front-loads a four-fold count that reads as four-fold support, when one of the four — Bidirectional Interaction, rewritten 09-07 — is now a declared null (*"gives Tenet 3 **nothing**"*). Under the style guide's truncation-resilience principle the null is exactly what an early-truncating reader should learn. **Fixed** with one clause naming it.

### Verdict on the §Relation sibling paragraphs — the driver's strongest lead is a NEGATIVE result

The hypothesis was that the 09-07 calibration fix stopped at one tenet paragraph and left its neighbours at a higher register. **It did not.** All three siblings were read to the end and are individually well-calibrated at or below the register the Tenet 3 paragraph now sets:

- **Dualism** closes *"unresolved on both sides"* — symmetric, claims no psychedelic support.
- **No Many Worlds** volunteers the disclaimer outright: *"this commitment is motivated on independent grounds, not read off the psychedelic data."*
- **Occam's Razor Has Limits** is a claim about the *dialectic* (naturalism's parsimony appeal), not an evidential claim, so the register question does not bite.

The residue was one level up, in the section's own lead sentence (Medium Issue 3) — not in the sibling paragraphs. Recording this so a future pass does not re-run the same hypothesis.

### Adjudication: the three Sjöstedt-Hughes containers are three genuine works — NO defect

The corpus cites Sjöstedt-Hughes with *Modes of Sentience* (2), *The Philosopher* (2) and *Philosophy and Psychedelics* (1). Keyed on **title** rather than surname, per `author-string-sweep-hits-two-real-papers-discriminate-by-title`: *Psychedelics and the Limits of Naturalism* is a **review of Letheby 2021**, published in *The Philosopher* vol. 110 no. 2 (2022) — confirmed at the journal's own site. *Modes of Sentience* is his own monograph and *Philosophy and Psychedelics* the Hauskeller & Sjöstedt-Hughes edited volume; both are separate, real works. Three containers, three works. The 2026-08-26 container fix in this family set a precedent but does not extend here. Reference 5 was **enriched** with `110(2)`, not corrected.

### Low Issues

**4. An unverifiable verbatim quotation removed at zero cost.** `Letheby's response is a "fourth option."` asserted a verbatim phrase from a paywalled monograph that cannot be grep-verified (`quote-must-be-grep-verifiable-in-raw-source`). The substance is confirmed via the Sjöstedt-Hughes review's *"fourth way" / "fourth response"*; the quotation marks were dropped and the sense made explicit instead.

**5. Reference 5 enriched** with the volume/number read from the publisher masthead.

### Checked and clean — do not re-spend a future pass here

- **Attribution accuracy (§2.5)**: no misattribution, no dropped qualifiers, no exploratory-as-committed slippage, no false shared commitments. The Deane 2021 and Sjöstedt-Hughes disclaimers ("physicalist and does not endorse the Map's metaphysics"; "internal-to-physicalism disagreement, not support for dualism") are intact and correct — and the Carhart-Harris/Friston non-enlistment note at line 45 remains a model of the pattern.
- **Reasoning-mode (§2.6)**: unchanged, and zero editor-vocabulary label leakage (grepped for `direct-refutation-feasible`, `unsupported-jump`, `bedrock-perimeter`, `Engagement classification:`, `**Evidential status:**` — none present). The hard-problem prong remains Mode Two in natural prose (*"helps itself to a move predictive processing has never paid for"*), the minimal-self prong Mode Three, the CDO reversal Mode One/Two via Sjöstedt-Hughes' internal-tension argument — now web-verified as genuinely his.
- **Over-concession tells**: `in principle`, `no possible`, `cannot ever`, `undetectable`, `no evidence could` — all absent.
- **All 44 wikilinks and section anchors resolve** (checked programmatically against every `obsidian/**/*.md` stem plus the file's own heading set); `[[cosmopsychism]]` and `[[altered-states-as-interface-evidence]]` are unique, collision-free and `draft: false`. `scripts/validate.py` passes.
- **The 09-07 Bidirectional Interaction rewrite is well made and stranded nothing** — independently re-confirmed against the driver's 9-article sweep.

## Optimistic Analysis Summary

### Strengths Preserved

- The empirical-equivalence concession, properly scoped to *"on psychedelic data **alone**"* with three named points of divergence, and the line the Hardline Empiricist persona should praise loudest: *"Saying so plainly is part of the Map's evidential discipline, not a retreat from it."*
- The Tenet 3 null (09-07) — a paragraph that gives a tenet *nothing* and says why. Left untouched.
- Mode-Two engagement in journal-quality prose with zero label leakage.
- The load-bearing self-fictionalism quote, now verbatim-confirmed twice by two independent routes.
- The symmetry concession on the hard problem (*"neither account discharges the hard problem; both inherit it"*) followed by the argument for why the symmetry is still the Map's point.

### Enhancements Made

- Gładziejewski promoted from taxonomy-provider to **substantive ally**: a peer-reviewed philosopher who takes Letheby's own constructivism as a premise toward cosmopsychism-friendly conclusions, forward-linked to the reversal section that needs him. This is the fix for Critical 1 and an expansion in one move.
- New cross-links: [cosmopsychism](/concepts/cosmopsychism/) and [altered-states-as-interface-evidence](/apex/altered-states-as-interface-evidence/).
- One genuine redundancy trimmed to hold the article below soft threshold: the lead's *"engages Letheby as the disciplined physicalist baseline the Map must clear"* duplicated line 59's *"It is the baseline the Map must clear"*. The later instance is better placed; the lead's was cut.

## Remaining Items

One P3 minted (appended at the **end** of `## Active Tasks`, pure insertion — no existing task's line number shifted): settle the Gładziejewski **2023 vs 2025** citation-year convention across three loci now that the publisher-of-record data is in hand. The 09-07 refine flagged the question to the operator as unsettled because Crossref reports only the online date; the Springer PDF's own header settles it (`(2025) 16:175–197`, accepted 2023-09-26, online 2023-10-10). The research note's `Gładziejewski (2024)` is wrong under *every* convention and is the one unambiguous defect of the three. Word-neutral at each locus. This article's reference 10 was **left at 2023 deliberately**, to avoid two Map articles disagreeing while the convention is open.

## Stability Notes

- **All prior Stability Notes stand.** Self-fictionalism versus the irreducible subject is bedrock framework-boundary disagreement — do NOT re-flag "physicalist rejects the irreducible subject" as critical.
- **Critical 1 is now closed and should not be re-opened by a pass that has not read the PDF.** The two model names are verbatim in Gładziejewski at offsets 55989 / 56327; the taxonomy divides *mechanisms of truth-revelation*, not revelation-from-no-revelation. A future reviewer who re-reads only the article may be tempted to "simplify" the paragraph back toward the shorter, wrong version. It was short because it was wrong.
- **Critical 2 is a corpus-shape lesson, not a one-off.** Two consecutive tasks in the queue now target the same defect family: an article states a stronger reading than the source it points at. Intra-file review cannot see it; only opening the target can. The `fresh-create-defect-tail` variant — a *new* article importing pre-correction framing from a corrected neighbour — is the harder case, because the article is younger than the fix.
- **Do not re-run the "did the de-escalation stop at one paragraph?" hypothesis on this file.** It was run this pass and came back negative, with all three sibling paragraphs read to the end. See the verdict section above.
- **Quote fidelity on this file is now materially complete**: the L&G quote (two independent routes), both Sjöstedt-Hughes claims (raw page, printed offsets), both Gładziejewski model names (publisher PDF). The residual unverifiables are the paywalled Letheby 2021 monograph and the Brains Blog commentaries; the one exposed monograph quotation was de-quoted rather than left standing.
- Frontmatter: `ai_modified` and `last_deep_review` both bumped from a live `date -u`. `ai_system` left at `claude-opus-4-8+claude-opus-5` — it already contained `claude-opus-5`, and no duplicate was appended.