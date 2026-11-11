---
ai_contribution: 100
ai_generated_date: 2026-11-11
ai_modified: 2026-11-11 20:20:49+00:00
ai_system: claude-fable-5-2
author: null
concepts: []
created: 2026-11-11
date: &id001 2026-11-11
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-11 20:20:49+00:00
modified: *id001
related_articles: []
title: 'Deep Review - Japanese Philosophy of Mind: The Kyoto School'
topics: []
---

**Date**: 2026-11-11
**Article**: [Japanese Philosophy of Mind: The Kyoto School](/topics/japanese-philosophy-of-mind-kyoto-school/)
**Previous review**: [2026-09-11](/reviews/deep-review-2026-09-11-japanese-philosophy-of-mind-kyoto-school/)
**Word count**: 2599 → 2624 (+25), `ok` (topics soft 3000 / hard 4000)
**Mode**: post-modification review. Two refine-draft commits on 2026-10-14 (`915d6673da`,
`0020a49bf0`) changed L32, L48 and L80 after the 09-11 pass; those three passages had never
been deep-reviewed.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Unverifiable quotation attributed to Watsuji (L60). FIXED by de-quoting.**
The article put *ethics is "that which takes place between humans."* in quotation marks inside
a sentence about *Rinrigaku*. Provenance: the phrase originates as a "Key points" gloss in the
research note (`research/kyoto-school-pure-experience-absolute-nothingness-2026-07-10` L74) and
was never grepped against a raw source. Two web searches on the exact phrase return no hit; it
is absent (count 0) from the SEP Watsuji entry and the SEP Kyoto School entry; the Yamamoto &
Carter text is lending-only on archive.org and could not be searched. The 07-10 and 09-11
ledgers certified the *book metadata* only. The idea is uncontroversially Watsuji's
(*aidagara*, ethics as the study of *ningen*), so the claim stays and the quotation marks go:
"ethics, on this account, is located in what takes place between persons."

**2. L82 asserted categorically that a basin edge adds weight to the convergence argument. FIXED.**
L82 opened "Crucially, the Kyoto case only **strengthens rather than confirms** the convergence
argument" and closed "the Kyoto data point adds weight to the pattern." Since the 10-14 edit,
the immediately preceding paragraph (L80) says the Kyoto case *qualifies* the convergence
inference, and L80 defines a basin edge as a tradition that does *not* land on the Map's
reading; L84 then says the case cannot be entered unqualified in a convergence tally. An
unconditional "adds weight" sat between two paragraphs that withhold it. A tenet-accepting
reviewer would flag this, so it is a calibration error, not bedrock disagreement. The
common-cause caveat itself (fenced by 07-10 and 09-11) is preserved verbatim; only its scope is
made conditional, on the model of the Nahua sibling's "its agreement … where it exists, would
*strengthen rather than confirm*":

- **After (opening)**: "Where the Kyoto School does agree with the convergent traditions—that
  experience is not captured by third-person, object-side description—the agreement at most
  **strengthens rather than confirms** the convergence argument…"
- **After (closing)**: "So the Kyoto data point, so far as it agrees, adds weight to the pattern
  without closing the question…"

The 09-11 "tally vs census are complements" stability note is not contradicted: that note
explains why the *ordinals* are harmless; this fix concerns a sentence that did enter Kyoto on
the convergence side without condition.

### Citation Web-Verify (§2.4) — per-cite ledger

Quotations were grepped against raw fetched text this pass (SEP pages via curl, OpenAlex
abstract), not carried forward.

- Maraldo 2005/2024, "Nishida Kitarō" (SEP) — **real-correct**. The quote installed 10-14 at
  L48 is verbatim in the live entry §7 ("his insistence on irreducible but inseparable terms in
  relation, explain why the holistic tendency evident in his methodology does not devolve into a
  simple monism, and why many commentators refer to his philosophy as non-dualist instead"). The
  article's "his holism" bridges outside the quote marks. Revision date Feb 21 2024 confirmed.
  "pre-individual" and "all-comprehensive" (L40, L64) are also Maraldo's words (§2.1).
- Davis 2006/2026, "The Kyoto School" (SEP) — **real-correct**. "highly contentious" verbatim
  ("the political ventures and misadventures of the Kyoto School remain a highly contentious
  subject"). Live entry now shows substantive revision Sep 14 2026; "rev. 2026" still right. The
  earlier Davis quote removed on 10-14 ("explicitly rejected simple monism…") is confirmed gone.
- Stone & Altobrando 2023, *The Philosophical Forum* 54(1–2), 43–60, doi 10.1111/phil.12333 —
  **real-correct** (OpenAlex metadata). "still no consensus about the extent to which Nishida's
  philosophy actually resembles James' work at all" verbatim in the abstract; "avenues James had
  reasons to decline" faithfully paraphrases the abstract's closing caveat.
- Nishida 1911/1990, *An Inquiry into the Good* (Abe & Ives, Yale) — **real-correct**. "the
  state of experience just as it is without the least addition of deliberative discrimination"
  confirmed against independent quotations of the Abe & Ives opening (secondary; the book itself
  is lending-only).
- Nishida 1926–1937/2012, *Place and Dialectic* (Krummel & Nagatomo, OUP) — real-correct
  (carried from 07-10; no quotation rests on it).
- Nishitani 1961/1982, *Religion and Nothingness* (Van Bragt, UC Press) — real-correct. Note: the
  unquoted sentence at L52 ("takes absolute nothingness as the fundamental notion for the rational
  articulation of the Eastern experience…") closely tracks the publisher's blurb, not Nishitani's
  own text. Left as paraphrase; do not put it in quotation marks.
- Watsuji, *Rinrigaku* (Yamamoto & Carter, SUNY 1996) — metadata real-correct; **quotation
  unverifiable, de-quoted** (critical 1).
- Heisig 2001 — real-correct; listed in References with no inline cite (general background
  entry, as since create; low, left).
- Superlative sweep: `find_superlative_claims` n = 0. No empirical cites, so the
  result-direction leg is not applicable.
- Cited-author-stance leg: Nishida, Nishitani, Tanabe, Watsuji are named as non-dualists (L78);
  James as neutral monist (L64); Maraldo's gloss is "non-dualist". No author is presented as
  endorsing the Map's conclusion.

### Attribution / Reasoning-Mode

- The 10-14 L32 rewording ("Nishida's own holism does not settle into simple monism either")
  correctly narrows a school-wide claim to what Maraldo supports about Nishida.
- Engagements unchanged from 09-11: Nishida dissolve/dodge, James/neutral monism, Tenet 5
  framework rivalry — all Mode Three, boundary stated, no refutation claimed. Label-leakage scan
  clean (0 hits).
- The 10-14 L80 addition ("all start from the mind-matter partition") is a Map-side claim inside
  the fenced Relation section and is marked as conditional on "the framework-dependence reading
  below"; it is a framework-conditional implication, correctly labelled. No action.

### Medium / Low Issues

- L44 "The two essays that articulate it were translated as *Place and Dialectic*": the second
  essay ("Logic and Life", 1936–37) is later than and broader than the basho logic. Low; left.

### Counterarguments Considered

Bedrock items from the 07-10 and 09-11 stability notes (physicalist rejection of the framing;
Nishida's non-dual reading of the same datum) were not re-flagged.

## Optimistic Analysis Summary

### Strengths Preserved

- Expound-then-interpret structure and the fence opening §Relation to Site Perspective.
- The dissolve-or-dodge spine left open in lead, section and Relation alike.
- The James bridge drawn and terminated; the symmetric Tenet 5 paragraph; the bounded politics note.
- The 10-14 Maraldo quote, which replaces an unverifiable Davis quote with a verified one.

### Enhancements Made

- L82 now agrees with L80 and L84: the Kyoto case is weighed on the convergence side only so
  far as it agrees.

### Cross-links Added

None (10+ inbound; no new target warranted).

## Remaining Items — reported, not edited

1. `chinese-philosophy-of-mind` L102 glosses this article as "the paired second basin edge:
   another non-substantialist tradition **landing near irreducibility** without dualism". This is
   the residue-presupposing phrasing the 09-11 pass removed from this article's own lead, still
   live in the outbound gloss of a sibling (and still an unqualified definite ordinal).
2. `cross-traditional-convergence-…` L173 still reads "a second basin edge" unqualified
   (reported 09-11). The 09-11 headline item is resolved: the hub table row is now `Qualified†`
   with a footnote.
3. `mesoamerican-nahua-philosophy-of-mind` L3 `description:` still "the convergence argument's
   second basin edge", unqualified (reported 09-11).
4. Research note L74 still carries the Watsuji phrase in quotation marks; any future article
   drawing on it will re-import the unverified quote.

## Stability Notes

- All 09-11 stability notes carry forward (ordinal scheme, tally-vs-census, bedrock rivalry,
  no condense).
- The common-cause caveat is conditional by design as of this pass. Do not restore the
  categorical "the Kyoto case only strengthens": a basin edge is not an unconditional entry on
  the convergence side.
- Do not re-quote the Watsuji sentence unless the wording is found in the Yamamoto & Carter text
  itself.
- All four quotations remaining in the article (Nishida, Maraldo, Stone & Altobrando, Davis) were
  grep-verified against source text on 2026-11-11. Re-verify only if they change.