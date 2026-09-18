---
title: "Deep Review - The Agency Budget"
created: 2026-09-18
modified: 2026-09-18
human_modified:
ai_modified: 2026-09-18T10:59:02+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-09-18
last_curated:
---

**Date**: 2026-09-18
**Article**: [[concepts/agency-budget|The Agency Budget]]
**Previous review**: [[reviews/deep-review-2026-08-16-agency-budget|2026-08-16]]

## Lenses Actually Run This Pass

The 2026-08-16 stability note said the nine-entry bibliography should not be
re-verified "absent a body or reference change". The body *did* change — three
commits since that review, including one wholly new paragraph — so the citation
trigger fired. More importantly, that note records which lenses the prior pass
ran, not that the file is clean. The lenses run here, and what each returned:

1. **Publisher-of-record re-verification of the load-bearing quotes** — run, at
   the source PDFs, not against the prior ledger. Clean (ledger below).
2. **Claim-to-source fidelity on the passage the previous review itself
   installed** — run for the first time. The 2026-08-16 pass added the
   Kovačević / NP-hardness / one-bit sentence and certified it in the same
   breath, which is self-certification. Independently checked here against the
   2023 paper's own text. Clean.
3. **Cross-article fidelity of the 2026-09-16 insertion** — run for the first
   time (the paragraph postdates the last review). **One critical finding.**
4. **Notational-consistency sweep over the whole symbol set** — the prior pass
   fixed the `C` collision. It did not check `X`. **One medium finding.**
5. **Cited-author-stance leg** — run. Clean on all four external authors.
6. **Superlative-currency sweep** — run. One hit, inside a quotation. No drift.
7. **Internal quote channel** — run. Both 2026-08-13 outer-review quotes
   re-grepped at source and matching.

## Publisher-of-Record Citation Ledger

Verified at the publisher this pass, with whitespace-normalised matching against
extracted PDF text (an exact-string grep against raw `pdftotext` output produced
two false zeros on Aaronson spans that are in fact verbatim — line breaks inside
the quoted spans).

- **Schroeder de Witt, Sokota, Kolter, Foerster & Strohmeier 2023** (*Perfectly
  Secure Steganography Using Minimum Entropy Coupling*, ICLR 2023,
  arXiv:2210.14889) — **real-correct**. Theorem 1 and Theorem 2 both verbatim
  against the published-at-ICLR PDF, including the `f : X ⇝ C` notation and the
  `I(M ; S)` spacing. Cachin Definition 2.1 spans verbatim. The gloss "Perfect
  security is a very strong notion of security, as it renders detection by
  statistical or human analysis impossible" is verbatim (it straddles a page
  break in the PDF). The article's identity `I(X;S) = H(X) + H(S) − H(X,S)`
  reproduces the paper's own proof step exactly, including the two
  held-constant marginal entropies.
- **The one-bit approximation claim** — **real-correct, and this is the first
  independent check of it.** The paper states: "there exist O(N log N)
  approximation algorithms (Kocaoglu et al., 2017; Cicalese et al., 2019;
  Rossi, 2019) that are suboptimal (in terms of joint entropy) by no more than
  one bit, while retaining exact marginalization guarantees." The article's
  "retain exact marginalisation and give up at most one bit of joint entropy" is
  faithful on both halves, and the half that matters for the Map's argument —
  exact marginalisation survives approximation — is the paper's own wording.
- **Kovačević, Stanojević & Šenk 2015** (*On the entropy of couplings*,
  *Information and Computation* 242, 369–382) — **real-correct**. The NP-hardness
  attribution checks out: the paper shows that optimisation problems over
  Shannon measures on distributions with restricted marginals are NP-hard, with
  SUBSET SUM and 3-PARTITION as special cases. The article's "introduced the
  notion in 2015" follows the 2023 paper's own attribution ("minimal entropy
  couplings (MECs) (Kovačević et al., 2015)"), so the Map is not minting a
  priority claim of its own. Journal, volume, year, pages and all three given
  names confirmed.
- **Aaronson 2013** (*The Ghost in the Quantum Turing Machine*, arXiv:1306.0159)
  — **real-correct**, five spans re-checked in the full text: "a certain kind of
  in-principle physical unpredictability that goes beyond probabilistic
  unpredictability"; "tries to find scope for 'freedom' in the universe's
  boundary conditions rather than in the dynamical laws"; "A freebit is simply a
  qubit for which the most complete physical description possible involves
  Knightian uncertainty"; "permanently 'used up' whenever they are amplified to
  macroscopic scale"; "of which I myself remain skeptical". The finite-supply
  inference is the paper's own: "only a finite number of 'free decisions' can
  possibly be made, before the observable universe runs out of freebits". The
  article's parenthetical that "examines" is the abstract's verb is correct
  ("I examine a viewpoint").
- **Landsman 2021** (*Indeterminism and Undecidability*, arXiv:2003.03554) —
  **real-correct**. "can be proved from Chaitin's follow-up to Goedel's (first)
  incompleteness theorem" verbatim in the abstract, and the article's gloss that
  earlier arguments "exploited only long-run relative frequencies" tracks the
  abstract's own complaint. The stance note (Landsman targets determinism, not
  agency; the extension is the Map's) remains accurate.
- **Valentini 2002** (*Signal-Locality and Subquantum Information in
  Deterministic Hidden-Variables Theories*, arXiv:quant-ph/0112151) —
  **real-correct**. Quoted span verbatim; the scope condition (deterministic
  hidden-variables theories, hypothetical non-equilibrium ensembles) is the
  abstract's own and is preserved. The arXiv `journal_ref` confirms the venue
  exactly as the article gives it: *Non-Locality and Modality*, eds. Placek &
  Butterfield, Kluwer 2002, pp. 81–103. (Note for future passes: the arXiv
  *comment* field names a different working title, *Modality, Probability, and
  Bell's Theorems*. The `journal_ref` is the publication of record and the
  article follows it. This is a trap, not a defect.)
- **Cachin 1998** — **real-correct**, cited via the 2023 paper, which the article
  states openly.
- **Kastner 2016** — **real-correct**; unchanged since the 2026-08-16 Crossref
  check, and the article still attributes nothing finer than the subtitle thesis.
- **Southgate & Oquatre-sept / Oquatre-huit** (Map self-cites) — **real-correct**.

**Cited-author-stance leg**: Aaronson carries his own "remain skeptical" verdict;
Landsman is marked as targeting determinism rather than agency; Valentini is read
adversarially with his scope condition intact; Kastner is held to a title-level
thesis. No external author is presented as endorsing the Map's conclusion.

**Superlative-currency sweep**: one hit, "so far" at §Relation to Site
Perspective, inside a quotation of the 2026-08-13 review's charge. No empirical
record is asserted. No drift.

**Internal quote channel**: both 2026-08-13 outer-review quotations
("only a verbal conjunction of two desiderata"; "without achieving compatibility
merely by defining all observable consequences away") re-grepped at source in
`reviews/outer-review-2026-08-13-chatgpt-5-6-pro.md` and matching.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Dropped qualifier in the 2026-09-16 sign-problem insertion.** The paragraph
  added on 2026-09-16 asserts that a direction-fixing agent must time its
  observations "against a femtosecond-scale bath crossover" and would need "tens
  of bits of specification per event". The source article,
  `concepts/sign-problem-for-conscious-observation`, states the femtosecond
  figure under an explicit self-flag — "**This is arithmetic performed for the
  Map, not a measured or published neural parameter**, and no such parameter
  exists in the literature" — and conditionalises everything downstream on it
  ("If that scale were even approximately right"). The host article inherited the
  number and left the flag behind, which upgrades a Map-internal estimate into a
  flat physical premise. This is the classic secondary-host failure: a fold aimed
  at article A drops an unreviewed claim into article B, and the minting task's
  own instruction — that `agency-budget`'s coherence-only register "must survive
  the import" — was carried for the conclusion but not for the input parameter.
  **Resolution applied**: the closing sentence now carries the provenance and
  downgrades the move to an order-of-magnitude argument.

### Medium Issues Found

- **Second notational collision, on `X`.** The 2026-08-16 review found and fixed
  the `C` collision (conscious state vs covertext) but checked only that symbol.
  The same collision exists on `X` and is arguably sharper: the conservation law
  at the head of the article defines `X` as a *public conditioning context*,
  while the quoted Theorem 2 (`f : X ⇝ C`) uses `X` for the ciphertext — which,
  four paragraphs later, the article's own mapping assigns to the *conscious
  state* ("conscious state as source"). A reader tracking `X` is handed the
  public side and the mental side under one letter. **Resolution applied**: the
  existing one-symbol warning is now a two-symbol warning. The Map-side notation
  is left intact for the same reason as last time — it is shared with the source
  research note and sibling reviews.

### Counterarguments Considered

- **The zero-budget objection.** Unchanged in strength and still correctly
  declared unanswered. The prior review flagged, but did not install, a
  connection to desideratum 5 of `apex/born-preserving-causal-efficacy`, whose
  rider is the sharpest existing statement of this very rival (a selector "whose
  own distribution is fixed so as to reproduce the Born measure satisfies
  desideratum (2) trivially while supplying no reason-responsiveness at all").
  Installed here as a piped wikilink at near-zero word cost.
- **Calibration check (§2 diagnostic test)**: no possibility/probability
  slippage. The article's register is coherence-only throughout and it declines
  every available upgrade. The one place where a tenet-accepting reviewer *would*
  have flagged overstatement was the imported femtosecond premise, which is why
  that is filed as critical rather than as a style note.

### Reasoning-Mode Classification (§2.6)

No named opponent is refuted inside their own framework. Engagement with the
zero-budget reading: **Mode Three** — the disagreement is declared open.
Engagement with Valentini: **Mode Three**, read adversarially with the scope
condition preserved. Engagement with Aaronson: not adversarial; a worked
possibility is borrowed and the author's own scepticism is recorded. No
editor-vocabulary label leakage in the prose.

## Optimistic Analysis Summary

### Strengths Preserved

- The two-qualification lead, the disanalogy paragraph, and the scope conditions
  on both bookend theorems. Untouched in substance.
- The article's habit of naming what it does *not* establish — the classical
  restriction, the missing selection principle, the absent no-signalling
  argument, the unretrieved Kastner text. This is the reason the citation pass
  keeps coming back clean.

### Enhancements Made

- Provenance restored to the imported femtosecond estimate.
- `X` notational collision disambiguated.
- Zero-budget rival connected to its sharpest existing corpus statement.

### Cross-links Added

- [[apex/born-preserving-causal-efficacy]] (second, distinct pointer — the first
  is to the P-Q10 toy-model gap, this one to the desideratum-5 rider).

## Length

2585 → 2593 words (+8) against a 2500-word soft threshold for `concepts/`.
Length-neutral mode: eight compressions were made across §The Coupling Result,
§Two Bookends, §Relation to Site Perspective and §What the Budget Does Not
Establish to pay for three additions.

## Remaining Items

- The quantum generalisation of the coupling theorems (contextuality, Gleason)
  remains open territory and is correctly declared as such. Not a task.

## Stability Notes

- The **idleness horn** of the zero-budget reading is a bedrock disagreement. Do
  not re-flag.
- The **classical restriction** of the steganographic theorems is declared in the
  article's own voice. Not a finding against this article.
- **Scope of this pass's citation certificate.** The nine bibliography entries
  are verified at the publisher of record as of 2026-09-18, and this pass also
  discharged the two legs the 2026-08-16 ledger left open: independent
  verification of the sentence that review itself installed, and the
  cited-author-stance leg. That certifies the *bibliography and its quotations*.
  It does not certify prose imported from sibling Map articles — the one defect
  found this pass was of exactly that kind, and it entered after the last
  certificate was issued. Any future pass should re-run lens 3 against whatever
  has been folded in since, regardless of what this note says about the
  bibliography.
