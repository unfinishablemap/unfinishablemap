---
ai_contribution: 100
ai_generated_date: 2026-08-06
ai_modified: 2026-08-06 12:14:13+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-06
date: &id001 2026-08-06
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-06 12:14:13+00:00
modified: *id001
related_articles: []
title: Deep Review - Conceptual Role Semantics and the Naturalisation of Content
topics: []
---

**Date**: 2026-08-06
**Article**: [Conceptual Role Semantics and the Naturalisation of Content](/concepts/conceptual-role-semantics/)
**Previous review**: [2026-07-13](/reviews/deep-review-2026-07-13-conceptual-role-semantics/)

Second pass. The 2026-07-13 review was the fresh-create chain cross-review; it explicitly recorded that citation metadata was **not** re-web-verified (carried from the research note) and that Brandom/Peacocke formulations were summarised from secondary sources. That unchecked surface is what this pass targeted, alongside the argument lens.

Changes since the previous review were mechanical: `a0fc32857` (coalesce) repointed `[[hard-problem-of-content]]` → `[[the-naturalisation-failure-for-content]]` after the former was archived, and `e19d4349d` populated an empty `topics: []`. Neither touched the body argument or the References block.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Attribution error — Peacocke grouped with Brandom as requiring irreducible norms.** Horn (a) read "as Brandom's appeal to genuine commitments and entitlements, or Peacocke's 'primitively compelling' transitions, seem to require". Peacocke explicitly *declines* the irreducible-norms route: *A Study of Concepts* pairs every possession condition with a **determination theory** — an account of how the concept's semantic value is fixed, required to make the possession condition's inferential principles come out truth-preserving. That is a direct answer to horn (a)'s correctness question, and the article both misattributed a requirement to him and left his actual answer unengaged. **Resolution**: Peacocke removed from the irreducible-norms clause; the determination theory now introduced in the one-factor taxonomy and engaged on its own terms inside horn (a) — the semantic value is *selected* to validate the transitions, and semantic value is already reference and truth, so correctness is read off the very inferences it was meant to underwrite. Web-verified against the published account of the determination theory before writing.

- **Stale self-description in the lede.** "It is the strongest naturalisation of content the Map has not yet engaged" is false at read-time on the page that *is* the Map's engagement with CRS — and the sibling topic already links here as "the dedicated treatment". A worst-case truncation-resilient position (first 200 words, LLM-first) carrying a self-falsifying claim. **Resolution**: rewritten to "the strongest naturalisation of content the Map's existing case does not reach", with the framing sentence changed from "the Map therefore owes CRS a dedicated response" to "CRS therefore needs a dedicated response … and this article supplies one".

### Medium Issues Found

- **Incomplete two-factor corollary.** The article treated the two-factor architecture's need for a separate wide referential factor as self-indicting ("a concession"), without saying why a Block-style theorist cannot simply naturalise the wide factor independently. That is the obvious reply and it was unanswered. **Resolution**: added the closing move — two-factor theorists naturalise reference by an informational or causal-covariational route (Fodor's asymmetric-dependence account the canonical instance), so the factor introduced to secure world-directedness lands back under exactly the dilemma inferential role was invoked to escape.

- **Undeclared pedigree of the deflation horn.** Horn (b) — grounding correctness in community dispositions trades correctness for regularity — is Kripke's Wittgenstein on dispositional accounts of rule-following, applied to inferential correctness. Presenting the fork as "not a result found pre-made in the literature" without acknowledging that ancestry reads as reinvention to any reader who knows the rule-following literature, and the Map already covers the paradox in [carrolls-regress](/concepts/carrolls-regress/). **Resolution**: ancestry named in horn (b) with a cross-link to [carrolls-regress](/concepts/carrolls-regress/); the novelty claim at the head of the reply narrowed to "a construction the Map defends rather than a result found pre-made in the literature, though each horn presses a difficulty the literature already knows". This does **not** reattribute the fork to a literature position (see Stability Notes) — the pairing of the two horns and their application to CRS as a naturalisation programme remain the Map's.

- **Quote fidelity — de-contracted principle name.** The lede quoted `"covariance does not constitute content"`. Hutto and Myin's published principle is *"Covariance doesn't Constitute Content"* (the CDCCP of *Radicalizing Enactivism*). A quoted span that has been silently de-contracted greps zero at the source. **Resolution**: restored to "covariance doesn't constitute content". (The sibling topic's usage is unquoted reported speech at L57 and is correct as it stands; no change needed there.)

### Citation Ledger (per-cite verification state, publisher-of-record pass)

The prior review verified only the IEP quote, the Sellars quote and the Field URL live; the remaining seven were note-verified. All were checked at publisher/index this run.

- Block, N. 1986, "Advertisement for a Semantics for Psychology", *Midwest Studies in Philosophy* 10: 615-678 — **real-correct**. Confirmed at the Philosophy Documentation Center record (HTTP 200) and against the scanned offprint header "MIDWEST STUDIES IN PHILOSOPHY, X (1986)". Note: Wiley's online record dates the issue 1987 (DOI 10.1111/j.1475-4975.1987.tb00558.x); the article's 1986/vol. 10 is the standard citation form and is left as is.
- Field, H. 1977, "Logic, Meaning, and Conceptual Role", *Journal of Philosophy* 74(7): 379-409 — **real-correct**. Volume, issue, month (July 1977) and page range confirmed independently of PhilPapers. The 378-vs-379 start-page discrepancy documented in the research note stands; majority form retained.
- Harman, G. 1987, "(Nonsolipsistic) Conceptual Role Semantics", in LePore (ed.), *New Directions in Semantics*, Academic Press, pp. 55-81 — **real-correct**. Page range confirmed at the PhilPapers record. ⚠ Self-contamination guard: the search for this cite returned unfinishablemap.org among its results; the page range was taken from the PhilPapers record, not from the Map's own page.
- Sellars, W. 1956, "Empiricism and the Philosophy of Mind", *Minnesota Studies in the Philosophy of Science* vol. 1, pp. 253-329 — **real-correct**; the "logical space of reasons, of justifying and being able to justify what one says" quote was verbatim-verified at plato.stanford.edu in the prior review and is unchanged.
- Brandom, R. 1994, *Making It Explicit: Reasoning, Representing, and Discursive Commitment*, Harvard University Press — **real-correct**. Author, full subtitle, publisher and 1994 copyright confirmed; HUP catalogue URL live (HTTP 202).
- Fodor, J. and Lepore, E. 1992, *Holism: A Shopper's Guide*, Basil Blackwell — **real-correct**.
- Peacocke, C. 1992, *A Study of Concepts*, MIT Press — **real-correct**; and the "primitively compelling" formulation independently confirmed as Peacocke's own term for possession-condition transitions (found compelling, not inferred from anything further). The determination theory added to the article this run was verified from the same pass.
- Hutto, D.D. and Myin, E. 2013, *Radicalizing Enactivism: Basic Minds Without Content*, MIT Press — **real-correct**; principle name corrected to the published contraction (see Medium Issues).
- Conceptual Role Semantics, *Internet Encyclopedia of Philosophy* — **real-correct**, opening definition re-verified verbatim live this run including the "Roughly" hedge the article already flags. IEP additionally names Fodor (1990) and McGinn (1982) alongside Block among two-factor theorists; the article's narrower Block/Field pairing is a defensible selection, not an error.
- Self-cite (ref 10) Southgate & Oquatre-sept 2026-04-30 — **real-correct**; URL live (HTTP 200).

No superlative/empirical-currency claims detected (`find_superlative_claims` returns empty), so no currency sweep was owed.

Inline ↔ References cross-check: clean in both directions. Fodor's informational atomism is named in prose without a References entry, but it is an in-passing characterisation of a position rather than a cite to a specific work, and no year is attached — no orphan.

### Link Audit

- All six outbound wikilinks resolve to live files; `[[carrolls-regress]]` added this run and verified.
- The coalesce-era alias `[[the-naturalisation-failure-for-content|hard problem of content]]` is **accurate** — the target article is Hutto and Myin's HPC by name in its own description and lede. No relabel needed. (Checked because link aliases can survive an archival repoint while asserting something the new target does not carry.)
- Five inbound links live in content trees (the-naturalisation-failure-for-content, teleosemantics, content-externalism, intentionality, sellars-manifest-and-scientific-images), plus the archived hard-problem-of-content body. Integration is sound.

### Counterarguments Considered

- **Peacocke's determination theory** — now the strongest opponent move in the article and engaged directly rather than bypassed (see Critical).
- **Block-style two-factor reply that the wide factor is independently naturalisable** — now answered (see Medium).
- **Fodor-Lepore holism** — given its own section with the moderate-holism and two-factor replies recorded and the debate left unresolved. No change; the prior review's calibration is right.
- **Inferentialist implicit-norms rejoinder** — present and answered; the proves-too-much disarm added in the prior review is intact and still doing its work.

### Engagement classification (editor-internal, per direct-refutation discipline)

- Brandom, horn (a): **Mode Two** — inferentialism helps itself to correct-inference norms while claiming to have naturalised content; the reply invokes the programme's own naturalising standard.
- Peacocke, horn (a): **Mode One** — the determination theory is defective on its own terms, since it fixes correctness by selecting a semantic value that validates the transitions, using notions the naturalisation was owed.
- Deflationary/dispositional CRS, horn (b): **Mode One** — collapses on the opponent's own account of correctness.
- The inferentialist who accepts irreducible norms of reason and stops short of dualism: **Mode Three** — framework boundary, marked honestly, unchanged from the prior review.
- No boundary-substitution found. No label leakage: no editor vocabulary appears in article prose; "helps itself to" is the approved natural-prose pattern from the writing-style guide, not a label.

## Optimistic Analysis Summary

### Strengths Preserved

- The lede's diagnosis of *why* CRS is the rival the covariance dilemma does not reach — untouched apart from the stale self-description repair.
- The one-factor/two-factor taxonomy doing real argumentative work rather than serving as a survey.
- The honest "unresolved; a standing cost, not a refutation" verdict on holism.
- The Sellars both-hands paragraph: the autonomy of the space of reasons is congenial, the final reductive step is what the Map resists.
- The proves-too-much disarm from the prior review — left exactly as written.

### Enhancements Made

- Peacocke's determination theory introduced and answered (strengthens the article by engaging the best available opponent move rather than the weakest).
- Two-factor corollary completed through to the wide factor.
- Deflation horn's Kripkean ancestry named, which converts an apparent reinvention into a located argument.

### Cross-links Added

- [carrolls-regress](/concepts/carrolls-regress/) — body, Further Reading, and `concepts:` frontmatter.

## Length

1943 → 2186 words (+243), 87% of the 2500-word concepts soft threshold. Below soft; no condensation owed. All additions are argument or attribution repairs, none expository filler.

## Remaining Items

None requiring a task. The research note's flagged open edge (whether 2020s inferentialism has a distinctive answer to the normativity regress) is still open and still does not need a queue entry — the article does not claim to have surveyed it.

## Stability Notes

- The holism section's "unresolved; a standing cost, not a refutation" verdict is deliberate calibration. Do not push it toward "CRS is refuted by holism" or toward a longer literature survey. (Carried from 2026-07-13; still right.)
- The regress/deflation **fork** remains the Map's own construction and should not be rewritten into an attributed literature position. The 2026-08-06 addition names the *ancestry of horn (b)* (Kripke's Wittgenstein on dispositions) without reattributing the fork — this is the boundary the prior stability note was drawing, and it is intact. A future review should not extend the acknowledgement into "the Map borrows this argument from Kripke".
- Inferentialists who accept irreducible norms of reason but deny dualist conclusions — a Brandomian who treats the space of reasons as socially instituted and stops there — are a framework-boundary disagreement, marked honestly and not to be re-flagged.
- Peacocke's determination theory is now engaged. A future review should not re-flag "Peacocke's answer is ignored", nor re-add Peacocke to the irreducible-norms clause in horn (a) — he explicitly declines that route.
- Citation ledger is now publisher-complete for all ten references. Absent a References-block edit, a future pass may treat the metadata as verified and skip re-verification; quote fidelity for the IEP and Sellars spans has been checked twice at primary sources.