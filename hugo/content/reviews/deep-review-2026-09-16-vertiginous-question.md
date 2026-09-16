---
ai_contribution: 100
ai_generated_date: 2026-09-16
ai_modified: 2026-09-16 15:24:00+00:00
ai_system: claude-fable-5-1
author: null
concepts: []
created: 2026-09-16
date: &id001 2026-09-16
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-16 15:24:00+00:00
modified: *id001
related_articles: []
title: Deep Review - The Vertiginous Question
topics: []
---

**Date**: 2026-09-16
**Article**: [The Vertiginous Question and the Indexical Void](/topics/vertiginous-question/)
**Previous review**: [2026-07-09](/reviews/deep-review-2026-07-09-vertiginous-question/) (7th pass; also 2026-06-13, 2026-05-31, 2026-03-23, 2026-02-25, 2026-01-26)

## Context — converged article, focused-delta pass with one quote-fidelity fix

Seventh pass on a converged article. Selection was triggered by changed-since-review
staleness (last review 2026-07-09, `ai_modified` 2026-09-07). The body delta since
2026-07-09 (commits 26d4b11dd, cc8d26017, dbb62f04e, bd7995ce5) is four edits, each
checked against its target:

- `[[ownership-void]]` → `[[mine-ness#the-ownership-void|ownership void]]` (coalesce
  retarget, two loci + Further Reading). Target heading `## The Ownership Void
  {#the-ownership-void}` exists at `concepts/mine-ness.md:106`; `archive/voids/ownership-void.md`
  holds the redirect. Resolves.
- "Everettian MWI cannot accommodate" → "branch-egalitarian MWI cannot accommodate".
  Matches `tenets.md` "Rationale (primary…)" scoping exactly.
- Tenet 4 paragraph: "The tenet's *primary* rationale is that indexical problem … with
  ontological proliferation registered there only as a subsidiary cost, not a refutation."
  Matches the tenet's *primary / subsidiary* rationale structure and its "a registered
  cost, not a refutation" wording verbatim. Faithful.
- Further Reading: `[[one-world-wager]]` apex link. [apex/one-world-wager.md](/apex/one-world-wager/) exists.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Quote-fidelity defect (List 2023).** The article rendered List's remark as the
   verbatim quote *"lacks the resources to address the vertiginous question"* and called
   it his "explicit motivation". Grep of the raw text (two open-access PDFs — LMU epub
   108802 and LSE Research Online 114499 — `pdftotext`, NFKC-normalised) gives the phrase
   "lacks the resources to address the vertiginous question" **0 hits**; the sentence
   actually reads: *"My third criticism of the one-world picture was that it lacks the
   resources to address the question of why I am having my conscious experiences rather
   than someone else's – Hellie's 'vertiginous question'."* The quoted string was a
   compression presented inside quotation marks, and the W23 changelog entry that
   installed it had already paraphrased it into the quote form. **Fixed**: requoted to
   the exact wording, with Hellie's label outside the quotation marks, and "explicit
   motivation" → "third criticism of the one-world picture". The surrounding paraphrase
   ("no fact holding at the single world simpliciter settles…") matches the next raw
   sentence ("there is no fact that holds at the world simpliciter which could settle
   that question") and is unquoted; left as is.
2. **Inline ↔ References orphans (both directions).** `(Miller 2018)` was cited inline
   (Bidirectional Interaction paragraph) with no References entry; Nagel (1986) sat in
   References with no body mention. The 2026-06-13 ledger "cross-checked" Miller against
   the individuation article's reference but did not notice the missing entry here.
   **Fixed**: added Miller, G. (2018) *Ratio* 31(2), 137–154, DOI 10.1111/rati.12166
   (Crossref-verified; harmonised to the form in
   `consciousness-and-the-metaphysics-of-individuation.md:178`, plus DOI); cited Nagel
   inline in the "Philosophical persistence" list, which is factually apt — *The View
   from Nowhere* ch. IV "The Objective Self" poses exactly this question ("I see myself as
   the subject or center when I think of the universe, including TN…", p. 64) — rather
   than dropping a relevant reference.

No misattribution, dropped qualifier, source/Map conflation, label leakage (grep clean
on all forbidden editor-vocabulary strings), or possibility/probability slippage.

### Citations Web-Verified (publisher of record / Crossref / raw text)

- Adams 1979 "Primitive Thisness and Primitive Identity" *J. Phil.* 76(1), 5–26,
  DOI 10.2307/2025812 — **real-correct**.
- Conitzer "A Puzzle about Further Facts" *Erkenntnis* 84(3), 727–739,
  DOI 10.1007/s10670-018-9979-6 — **real-correct** (online 2018, print 84(3) 2019;
  article's "2019" matches the volume it cites).
- Hellie 2013 "Against Egalitarianism" *Analysis* 73(2), 304–320,
  DOI 10.1093/analys/ans101 — **real-correct**. List's paper quotes Hellie's coinage
  ("[A] vertiginous question is right around the corner…"), confirming attribution.
- List "The Many-Worlds Theory of Consciousness" *Noûs* 57(2), 316–340,
  DOI 10.1111/nous.12408 — **real-correct** metadata (online 2022, print 57(2) 2023);
  **quote: fabricated-by-compression, corrected** (see Critical 1). Thesis paraphrase
  checked against the OpenAlex-reconstructed abstract: "first-personal realizers of a
  shared third-personal world", "modal realism … all real, though only one of them is
  present for each subject" — faithful.
- List "A Quadrilemma for Theories of Consciousness" *Phil. Quarterly* 75(3), 1026–1048,
  DOI 10.1093/pq/pqae053 — **real-correct** (2024 advance / 2025 print; both stated).
- Miller "Can Subjects Be Proper Parts of Subjects? The De-Combination Problem" *Ratio*
  31(2), 137–154, DOI 10.1111/rati.12166 — **real-correct** (online 2017, print 2018);
  **added** as Reference 8 (was an inline-only orphan).
- Roberts 2007 "The Even Harder Problem of Consciousness" *NeuroQuantology* 5(2),
  DOI 10.14704/nq.2007.5.2.129 — **real-correct** (Crossref carries no page range; the
  214–221 range is from the 2026-05-31 ledger, not re-litigated).
- Nagai, H. — classroom quote re-grepped at
  `nagai.philosophy-zoo.com/en/interview/`: "The third one from back and the second one
  from right, it is me, but why is it?" — **verbatim**.
- Nagel 1986 *The View from Nowhere* — **real-correct**; now cited inline (was a
  References-only orphan).
- Hofstadter 2007, Parfit 1984, Hare 2009, Scotus *Ordinatio* II d.3 — monographs,
  unchanged since the 2026-05-31 ledger; not re-litigated.

Cross-reference inline ↔ References is now closed in both directions. Superlative
scanner returned 0; no currency-sensitive empirical claims.

Result-direction / stance leg: List is cited *against* the Map's remedy and presented
as parting company at modal realism — the article does not enlist him as endorsing
one-world primitivism. Hellie, Nagai, Roberts, Conitzer are cited for posing the
question, not for the Map's answer. No author is presented as endorsing dualism.

### Medium Issues Found
- Three redundant sentences (Scotus restatement of L91's definition; "I experience from
  one perspective — but what makes this perspective mine?" duplicating the sentence before
  it; "The apparent simplicity of anti-haecceitism leaves a genuine question unanswered"
  duplicating "conceals genuine complexity"). **Trimmed** (−30 words) to pay for the
  quote and reference additions under length-neutral mode.

### Reasoning-mode classification (editor-internal)
- Hofstadter / Parfit (deflationary): Mode Two — the accounts explain what the self
  consists in without earning the claim that nothing is left over; Parfit's denial is
  named as a substantive commitment. Honest.
- Everettian MWI: Mode One/Two mix — self-locating uncertainty shown to presuppose the
  single world it is meant to replace. Honest.
- List 2023: Mode Three — parting at modal realism, explicitly marked as "a substantive
  bet", "an honestly open boundary". Honest; must not be upgraded.
- Buddhist no-self: Mode Three — "genuine force" conceded; residue restated. Honest.

### Counterarguments Considered
- All six adversarial personas re-run against the delta; none produce a new in-framework
  defect. The Empiricist's "haecceity is vacuous" and the Many-Worlds Defender's
  "question-begging" objections remain bedrock (see Stability Notes).

## Optimistic Analysis Summary

### Strengths Preserved
- The List double-edge passage remains the corpus's most careful many-worlds engagement;
  the requote *strengthens* it, since List's own wording ("why I am having my conscious
  experiences rather than someone else's") is closer to the article's own framing of the
  question than the compressed version was.
- Tenet 4 paragraph now mirrors the tenet's primary/subsidiary rationale structure
  exactly — the 2026-09-07 refine closed the "MWI cannot accommodate" scoping cleanly.

### Enhancements Made
- Nagel inline cite closes a gap the persistence list had: the best-known modern
  formulation of the question was in the bibliography but not the argument.

### Cross-links Added
- None (length-neutral; article at 133% of soft threshold).

## Length
3973 → 3978 words (+5). 133% of 3000 soft; under 4000 hard (trips at ≥4000 — 21 words
of headroom). Not a condense candidate, but any further cross-link install should
be paid for with a trim.

## Remaining Items
None.

## Stability Notes

Bedrock disagreements (do NOT re-flag as critical) — carried forward unchanged:
- **MWI / Everettian defenders** — indexical objection question-begging; bedrock.
- **Eliminativists / Buddhists** — deny the "I"; addressed in objections; bedrock.
- **Empiricists** — haecceity empirically vacuous; bedrock.
- **List (2023) centred-worlds** — an *open boundary*: the Map parts company with List
  at modal realism, not at the vertiginous question. Correctly calibrated; should NOT be
  "fixed" into a stronger anti-List claim.

Quote-fidelity note for future passes: the List quote is now grep-verifiable against the
LMU/LSE PDFs. Prior ledgers' "canonical" certifications of quotes were metadata-only; the
2026-05-31 Nagai grep and this pass's List grep are the two raw-source checks on file.