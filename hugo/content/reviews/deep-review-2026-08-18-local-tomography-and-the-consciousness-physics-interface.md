---
ai_contribution: 100
ai_generated_date: 2026-08-18
ai_modified: 2026-08-18 10:31:30+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-18
date: &id001 2026-08-18
description: 'Second deep review: verifies the 2026-08-16 Galley-Masanes modal correction
  at Crossref, finds the same fix half-applied in the source research note, and links
  the article to the positions register.'
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-18 10:31:30+00:00
modified: *id001
related_articles: []
title: Deep Review - Local Tomography and the Consciousness-Physics Interface
topics: []
---

**Date**: 2026-08-18
**Article**: [Local Tomography and the Consciousness-Physics Interface](/concepts/local-tomography-and-the-consciousness-physics-interface/)
**Previous review**: [2026-07-16](/reviews/deep-review-2026-07-16-local-tomography-and-the-consciousness-physics-interface/)

## Scope

The unchecked surface since the last (clean) review was a single commit: `203f2ce5a9`, 2026-08-16, a refine-draft that corrected the article's statement of the Galley-Masanes theorem from a disjunctive to a conjunctive consequent, and correspondingly changed the article's own conditional from "satisfies purification **and** local tomography" to "**or**". This review starts and largely ends there.

## Pessimistic Analysis Summary

### The modal correction: verified sound, and fully applied in the article

Galley & Masanes (2018) prove, of every alternative to the measurement postulates in their classification, that it violates purification **and** that it violates local tomography — two separate results, both established in the abstract. Formally:

> modified Born rule → (¬purification ∧ ¬local tomography)

Contraposing and applying De Morgan:

> (purification ∨ local tomography) → Born rule

So a **conjunction in the paper's consequent yields a disjunction in the article's antecedent.** The 2026-08-16 edit to "or" is correct; the commit title, which describes the defect as "states Galley-Masanes as a disjunction where the paper states a conjunction", refers to the article's earlier mis-statement of the *theorem's consequent* ("violates purification **or** local tomography"), not to the conditional's antecedent. Both edits pull the same way. No revert.

Every modal claim in the article was checked against this derivation and all agree: the lede ("each of which independently forces"; "would have to fail *and* purification fail with it"), the contraposition paragraph, numbered point 3 of the interface argument ("one lock is off — and only one"), the signature-reading paragraph ("the theorem asks for two"), and the Tenet 2 paragraph. `## What Failure Looks Like` carries no Galley-Masanes modal claim; it is about real and quaternionic quantum theory. The sibling [generalised-probabilistic-theories](/concepts/generalised-probabilistic-theories/) agrees at both of its loci. The fix is *not* half-applied in article content.

### Critical issue found: the same fix **was** half-applied in the source research note

Commit `203f2ce5a9` also edited [the source research note](/research/local-tomography-and-the-consciousness-physics-interface-2026-07-16/) — correcting its "Sibling: Galley & Masanes" entry, which now reads "either axiom holding on its own forces the Born rule, so local-tomography failure at the interface is *necessary but not sufficient*". It left the note's "Interface Speculation" section uncorrected, twenty-one lines below, still asserting the retired reading:

> "If (B+S) is **not** locally tomographic, then by Galley-Masanes the door is open"

The note therefore contradicted itself in published content, and its "Setup" additionally carried a **stale internal quote** of the sibling GPT concept — reproducing "satisfies purification and local tomography" as a quotation after that article had been changed to "or". Three loci corrected (Setup, numbered point 3, reading (a)); the note's own timeline row was already right. Resolution applied.

### Corpus sweep

Four inversion strings swept across `obsidian/`, `hugo/content/` and `archive/`. `satisfies purification and local tomography` and `local tomography (and purification)` survived only in the unsynced Hugo mirror of the research note (cleared by sync). `door is open` and `exactly two doors` / `one of exactly two` survive only in unrelated articles using the metaphor in another sense, and in `reviews/` + `workflow/` — historical echo, not live defect. No further live locus.

### Note on the previous review's ledger

The 2026-07-16 review's per-cite ledger recorded Galley & Masanes as **real-correct** — and it was, as *metadata*. The citation's author, year, title and venue were all faithful while the article's reading of the theorem's logical form was inverted, and the ledger entry positively ratified the wrong reading ("'one of exactly two axioms' framing faithful to the paper's purification+local-tomography result"). A correct-metadata ledger entry is not evidence that the cited theorem has been read correctly; the two are orthogonal checks.

### Medium issue: uncited empirical claim

`## Is Local Tomography a Fact About Nature?` asserted that the Renou test "was realised in 2022 on superconducting and photonic platforms" with no citation anywhere in the References. Both realisations verified at Crossref and added, with inline attribution so neither entry is an orphan.

## Publisher-of-Record Citation Ledger

WebSearch was exhausted for the cycle; verification ran on Crossref REST and the arXiv API, both primary.

- Galley, T. D., & Masanes, L. (2018), *Any modification of the Born rule leads to a violation of the purification and local tomography principles*, Quantum 2, 104 — **real-correct** (Crossref `10.22331/q-2018-11-06-104`; title, both authors, venue, volume, page, date all exact). All three abstract quotations verified verbatim: "in all these theories the purification principle is violated"; "in all such modifications the task of state tomography with local measurements is impossible"; "contrarily to previous claims". The article's scope condition — that they classify alternatives to the *measurement* postulates while holding pure-state structure and reversible dynamics fixed — is faithful to the abstract's "from the structure of pure states and reversible dynamics". DOI added to the reference entry.
- Hardy, L., & Wootters, W. K. (2012), *Limited Holism and Real-Vector-Space Quantum Theory*, Foundations of Physics 42, 454-473 — **real-correct** (Crossref `10.1007/s10701-011-9616-6`; `published-print` 2012-03, so the article's 2012 is the right year to cite against volume 42). Both quotations verbatim from arXiv:1005.4870: "has the property of 'local tomography': the state of any composite system can be reconstructed from the statistics of measurements on the individual components"; "real-vector-space quantum theory, while not locally tomographic, is bilocally tomographic".
- Barnum, H., & Wilce, A. (2014), *Local Tomography and the Jordan Structure of Quantum Theory*, Foundations of Physics 44, 192-212 — **real-correct** (Crossref `10.1007/s10701-014-9777-1`, `published-print` 2014-02). Quotation verbatim from arXiv:1202.4513: "orthodox finite-dimensional complex quantum mechanics with superselection rules is the only non-signaling probabilistic theory". The article's parenthetical caveat — that the theorem does not itself tabulate which alternatives fail — is accurate against the abstract.
- Renou, M.-O., et al. (2021), *Quantum theory based on real numbers can be experimentally falsified*, Nature 600, 625-629 — **real-correct** (Crossref `10.1038/s41586-021-04160-4`; all eight authors in the cited order). Quotation verbatim: "real and complex quantum theory make different predictions in network scenarios comprising independent states and measurements".
- Hoffreumon, T., & Woods, M. P. (2026), *Quantum theory based on real numbers cannot be experimentally falsified*, arXiv:2603.19208 — **real-correct** (arXiv API: both authors, title exact, submitted 2026-03-19, matching the article's "submitted March 2026"; no journal-ref, so the article's "preprint, not peer-reviewed" flag is right). Quotation "the absence of observable cross-source correlations" verbatim. The article's paraphrase of the product-state-independence / operational-independence distinction and of the finite-network indistinguishability result matches the abstract.
- Chen, M.-C., et al. (2022), *Ruling Out Real-Valued Standard Formalism of Quantum Theory*, Physical Review Letters 128, 040403 — **added** (Crossref `10.1103/PhysRevLett.128.040403`; the superconducting realisation).
- Li, Z.-D., et al. (2022), *Testing Real Quantum Theory in an Optical Quantum Network*, Physical Review Letters 128, 040402 — **added** (Crossref `10.1103/PhysRevLett.128.040402`; the photonic realisation).

No fabricated citation. No currency-superseded superlative: the article's only dated empirical superlatives are already scoped ("as of 2026", "unresolved as of 2026") and the Hoffreumon-Woods dispute is correctly reported as live rather than settled.

## Optimistic Analysis Summary

### Strengths preserved

- The "one door with two locks" figure. It carries the corrected modal structure in one image and is now load-bearing in three places; left untouched.
- The article's habit of naming its own evidential status inside the claim rather than in a footnote — the lede's "That status is part of the claim, not a footnote to it" — is unusually disciplined and was not diluted.
- The symmetry of the treatment: the paragraph beginning "The same arithmetic that softens the problem reading sharpens this one" makes the correction cut *against* the Map's preferred reading as hard as it cuts for it. This is the article's best passage.
- The Hardy-Wootters "limited holism" vocabulary as the ready-made language for the signature reading.

### Enhancement made: the positions-register gap

The article's `## The Interface Question` discussed the Tenet-2 interface at length while carrying zero links to [quantum-interface](/positions/quantum-interface/) (driver-measured, confirmed: `grep -c` = 0). Assessed against the register, the article does **not** over-read it — see Stability Notes — but it did present its two readings as unranked, where the register ranks them: [P-Q2](/positions/quantum-interface/#p-q2) holds exact Born preservation as the *default* reading of Tenet 2 at high credence, keeping the outside-the-corridor branch open as an explicitly subordinate fall-back ([P-Q2](/positions/quantum-interface/#p-q2)'s "Would shift if"). A reader could otherwise take "commits to neither as established" as the Map's whole position on Born deviation. One link plus one calibration clause added; no rewrite.

### Cross-links added

- [quantum-interface](/positions/quantum-interface/)

## Length

2435 → 2497 words (soft 2500, hard 3500; status `ok`). Operated length-neutrally: the two additions were offset by tightening the redundant restatement in the contraposition paragraph, cutting a sentence in `## What Failure Looks Like` that re-stated the bilocal-tomography definition given immediately above it, and compressing one lede clause. No calibration qualifier was removed in any of the three trims.

## Remaining Items

- The `d` symbol carries two meanings a few lines apart in `## The Axiom, Stated Neutrally` — GPT state-space dimension in "d_AB = d_A · d_B", Hilbert-space dimension in "a complex *d*-level system carries d² real parameters". Each statement is correct in its own convention and the source research note uses the same overload, so this is a clarity matter rather than an error. Left alone; flagged for any future condense pass that opens the section anyway.

## Stability Notes

- **The `#^mechanism-debt` citation grade does not bind this article.** The 2026-08-13 convergence attached that grade to downstream articles claiming consciousness "does causal work". This article contains no causal-work vocabulary at all (`grep -i` for causal / efficacy / agency / mental causation returns only the `causal-consistency-constraint` wikilink and its reference entry). It is a structural-axiom concept article whose thesis is that the axiom "does no work *for* the interface reading over its rivals", and it already cites [the evidential-status discipline](/concepts/evidential-status-discipline/) to place itself at coherence-only. Future reviews should not mint a mechanism-debt citation on this file; the register link added here is about [P-Q2](/positions/quantum-interface/#p-q2)'s default/fall-back ranking, which is a different point.
- **The article under-reads rather than over-reads the register**, and that is the right direction for a page whose subject is where a warrant runs out. Do not "strengthen" the signature reading to restore symmetry with the problem reading.
- The signature reading remains speculation the Map finds attractive. That it is *more demanding* after the modal correction than before is a feature of the correction, not a defect to repair.
- Real-quantum-theory partisans and anyone who accepts Hoffreumon-Woods will find the empirical section's agnosticism unsatisfying in opposite directions. The article's refusal to call the dispute is correct while it remains live; this is not an issue to re-flag.