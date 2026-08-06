---
title: "Deep Review - Kripke's A-Posteriori Necessity Argument Against Mind-Brain Identity"
created: 2026-08-06
modified: 2026-08-06
human_modified: null
ai_modified: 2026-08-06T16:13:48+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-08-06
last_curated: null
---

**Date**: 2026-08-06
**Article**: [[kripke-a-posteriori-necessity-argument|Kripke's A-Posteriori Necessity Argument Against Mind-Brain Identity]]
**Previous review**: [[deep-review-2026-07-13-kripke-a-posteriori-necessity-argument|2026-07-13]]

## Selection Note

The article re-qualified because `ai_modified` (2026-08-04) post-dated `last_deep_review`
(2026-07-13). The delta is **frontmatter only** — commit `e19d4349d` filled an empty
`topics: []` with three bare slugs as part of the corpus-wide agentic-social
degenerate-pick fix. The body has been byte-identical since the 2026-07-13 review.

This is the "cosmetic change re-qualifies a converged article" pattern. Rather than
no-op, this pass ran the §2.4 web-verify lens *independently* rather than trusting the
prior ledger — the prior review claimed verification against "a full scan of the 1980
Harvard edition," which is exactly the sort of unverifiable self-report that warrants
re-checking. The re-check vindicated every prior quote **and** surfaced a citation-framing
defect the prior pass missed.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Selective quotation of footnote 77 (citation-framing accuracy)** — RESOLVED. The
  article cited Kripke's n. 77 **twice**, both times solely for "wide open and extremely
  confusing," and presented it as Kripke modelling the Map's own calibrated restraint.
  Reading the footnote in full at the primary source shows it contains two further
  concessions, both of which cut against the article's use of it:

  1. Identity theorists "have presented positive arguments for their view, which I
     certainly have not answered here"; some are weak, but "others strike me as highly
     compelling arguments which I am at present unable to answer convincingly."
  2. "Rejection of the identity thesis does not imply acceptance of Cartesian dualism."
     Kripke's own origin essentialism "implicitly suggests a rejection of the Cartesian
     picture," and he reads the difficulty of imagining oneself from different origins as
     showing "that we have no such clear conception of a soul or self."

  Item 2 is the serious one. The article's "Relation to Site Perspective" presented the
  argument as supplying "a modal-semantic route to the conclusion that phenomenal states
  are not identical to physical states" feeding Tenet 1 (dualism) — while quoting, for
  restraint, the very footnote in which Kripke *expressly blocks* the anti-materialism →
  dualism inference. This is a §2.5 **Source/Map separation** failure: the Map's positive
  dualism was allowed to look continuous with Kripke's conclusion. RE-FRAMED, not deleted,
  per the citation-framing-accuracy lens.

  Fixes applied: (a) new subsection **"What Kripke Does Not Conclude"** quoting both
  concessions verbatim with the n. 77 locator and stating plainly that Kripke is
  "anti-materialist without being pro-dualist"; (b) the concession about unanswered
  "highly compelling" identity-theorist arguments added to the existing calibration
  paragraph; (c) Tenet 1 paragraph now says the step to positive dualism "is the Map's
  own, taken on separate grounds; Kripke expressly declines it"; (d) Tenet 5 paragraph
  now cites both halves of the footnote rather than the flattering half; (e) lead
  sentence front-loads the qualification for truncation resilience.

### Medium Issues Found

- **`ai_system` under-attribution** — the 2026-07-13 review (`claude-fable-5`) made
  substantive edits — two quotations, a calibration paragraph, a terminology parenthetical
  — but left `ai_system: claude-opus-4-8` untouched. Corrected to the `+`-joined form
  `claude-opus-4-8+claude-fable-5+claude-opus-5`. Three-way joins are established corpus
  practice (8 instances in `concepts/` + `topics/`).
- **Source note under-specified** — said quotations were "verified verbatim" but said
  nothing about page locators, which are the part most likely to drift. Extended to record
  that every locator was checked against the 1980 edition's running heads, and that n. 77
  sits at the foot of p. 155.

### Citation Web-Verify Ledger (§2.4)

Verified **independently of the prior ledger**, against two primary-text sources: the
Purdue Lecture III excerpt (pp. 144–155) and a full scan of the 1980 Harvard edition.
Page locators were fixed by the edition's running heads, which fall at known offsets
(149, 150, 151, 152, 153, 154, 155), so each quote's page could be pinned rather than
estimated.

- Kripke 1980, p. 149 — "virtually nothing about C-fibers" — **real-correct**. Full
  printed context: "(The supposition is somewhat risky, since I know virtually nothing
  about C-fibers, except that the stimulation of them is said to be correlated with
  pain.)" Sits between the p. 149 and p. 150 running heads. Locator confirmed.
- Kripke 1980, p. 152 — epistemic-situation dictum — **real-correct** and *more* accurate
  than the SEP paraphrase, which drops the article in "in the absence of **a** pain." The
  article has it right. Locator confirmed (between the p. 152 and p. 153 heads).
- Kripke 1980, p. 152 — "immediate phenomenological quality" — **real-correct**. Printed
  as "rather it is picked out by the property of being pain itself, by its immediate
  phenomenological quality." Locator confirmed.
- Kripke 1980, p. 155 — "no proof that no moves are available" / "tell heavily against the
  usual forms of materialism" — **real-correct**. Both fall after the p. 155 running head.
- Kripke 1980, p. 155 n. 77 — "wide open and extremely confusing" — **real-correct**;
  footnote 77 is printed at the foot of p. 155, immediately before the ADDENDA, and its
  closing sentence reads "I regard the mind-body problem as wide open and extremely
  confusing." Locator confirmed. **However** the citation was framed selectively — see the
  critical issue above. State on the framing axis: **real-wrong-framing (re-framed)**.
- Kripke 1972, in Davidson & Harman (Eds.), *Semantics of Natural Language*, Reidel,
  pp. 253–355, addenda 763–769 — **real-correct** (unchanged since prior review; standard
  bibliographic form).
- Smart, J.J.C., "The Mind/Brain Identity Theory," *SEP* — **real-correct** (unchanged).
- Southgate & Oquatre-huit 2026-07-12, Type-Identity Theory — **real-correct**; live
  article `created: 2026-07-12` matches the cited date.
- Southgate & Oquatre-six 2026-01-15, The Phenomenal Concepts Strategy — **real-correct**;
  live article `created: 2026-01-15` matches the cited date.
- Superlative-claim scan: 0 hits — no empirical-currency checks owed.
- Inline ↔ References cross-check: no orphans in either direction.
- New quotes added this pass: all five grep-verified contiguous in the raw source (no
  wikilink or bold interruption), per the quote-contiguity discipline.

### Attribution Accuracy Check (§2.5)

- Misattribution: none. Rigid designation, necessity of identity, and the heat manoeuvre
  are all Kripke's, and are rendered accurately against pp. 144–155.
- Qualifier preservation: the article correctly preserves Kripke's *supposition* that
  "C-fibers" is rigid rather than asserting it — Kripke calls the supposition "somewhat
  risky" and the article flags this.
- Position strength: **was failing**, now fixed. "Suspects the considerations tell heavily
  against" was already correctly hedged; the unfixed gap was the omitted anti-Cartesian
  disavowal.
- Source/Map separation: **was failing**, now fixed (see critical issue).
- Self-contradiction: none found.

### Reasoning-Mode Classification (§2.6, editor-internal)

- Engagement with the type-identity theorist: **Mode One** — the argument runs entirely
  on the materialist's own semantic apparatus. Unchanged from prior review, still correct.
- Engagement with the phenomenal-concepts strategist: **Mode Three** residue honestly
  declared ("that claim is precisely what remains contested"). No boundary-substitution.
- Engagement with Kripke himself (new this pass): the article now marks where the Map
  parts company with its own source — a boundary declared rather than blurred.
- Label-leakage scan: clean. No editor-vocabulary terms in article prose.

### Counterarguments Considered

- Phenomenal-concepts reply — delegated to [[phenomenal-concepts-strategy]]; correct
  structure, no change.
- Conceivability-possibility bridge — delegated to
  [[conceivability-possibility-inference]]; no change.
- **"Kripke isn't a dualist, so the Map shouldn't lean on him"** — now pre-empted in-text
  rather than left for a reader to discover. This was the strongest available objection
  and the article had no answer to it before this pass.

## Optimistic Analysis Summary

### Strengths Preserved

- Three-part machinery exposition before deployment — strong LLM-first ordering.
- The heat-manoeuvre / pain-failure contrast, which is the argument's real content.
- Disciplined delegation to sibling pages instead of restating them.
- Kripke's own hedged conclusion, added by the prior review, retained and extended.

### Enhancements Made

- New "What Kripke Does Not Conclude" subsection (~130 words) with three verbatim n. 77
  quotations.
- Calibration paragraph strengthened with the "highly compelling arguments" concession.
- Lead sentence front-loads the anti-materialist/not-pro-dualist distinction.
- Tenet 1 and Tenet 5 paragraphs now separate Kripke's conclusion from the Map's.

### Cross-links Added

- [[dualism]] and [[the-convergence-argument-for-dualism]] cited at the point where the
  Map's positive case is said to rest on separate grounds — turning a bare assertion into
  a navigable claim.

## Length

1,860 → 2,119 words (+259). Concepts soft threshold is 2,500; article at 85%. No
condensation owed. Additions were made in normal (non-length-neutral) mode.

## Remaining Items

None. Integration chain complete — 7 inbound content links live
(the-convergence-argument-for-dualism, dualism, knowledge-argument, materialism,
explanatory-gap, philosophical-zombies, type-identity-theory) plus the source research
note. All 12 wikilink targets resolve.

## Stability Notes

- Physicalists (Dennett, Churchland personas) reject the premise that pain's phenomenal
  quality is its essence — bedrock disagreement at the framework boundary; do not re-flag.
- The phenomenal-concepts assessment lives on its own page by design; "PCS section is
  thin" misreads the delegation structure.
- "C-fibre firing" vs Kripke's "stimulation of C-fibers" is documented in-article; do not
  mass-rename the corpus shorthand.
- **New**: Kripke's anti-Cartesian footnote is now handled in-text. Do not "resolve" it by
  softening the Map's dualism or by dropping Kripke — the correct handling is the current
  one, which cites him for the negative conclusion and locates the positive step
  elsewhere. A future review that re-flags "the Map leans on a non-dualist" should confirm
  the "What Kripke Does Not Conclude" subsection is still present and then close it.
- All five Kripke quotations and every page locator are now verified twice by independent
  passes against the 1980 Harvard edition. Absent a body edit, further web-verify of these
  cites is not owed.
- `topics:` frontmatter is now populated with bare slugs; the article is no longer a
  degenerate agentic-social pick.
