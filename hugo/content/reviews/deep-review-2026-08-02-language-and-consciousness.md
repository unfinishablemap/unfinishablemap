---
ai_contribution: 100
ai_generated_date: 2026-08-02
ai_modified: 2026-08-02 03:25:11+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-02
date: &id001 2026-08-02
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-02 03:25:11+00:00
modified: *id001
related_articles: []
title: Deep Review - Philosophy of Language and Consciousness
topics: []
---

**Date**: 2026-08-02
**Article**: [Philosophy of Language and Consciousness](/concepts/language-and-consciousness/)
**Previous review**: [2026-06-20](/reviews/deep-review-2026-06-20-language-and-consciousness/)
**Review number**: 8

This pass was triggered by a References-block change: the 03:04Z refine-draft (commit `ef3ba9200`) settled the long-running corpus split over the Chalmers "Phenomenal Concepts and the Explanatory Gap" year and propagated a canonical entry across nine live loci. The 7th review's stability note explicitly scoped re-verification to "unless the References block changes," so the changed entry was re-verified at the publisher of record.

The pass then found three attribution defects in the body that seven prior reviews had not caught. All three sit in the citation-framing-accuracy lens: the sources are real, the metadata is correct, and the framing misstates what the source says. This is the expected failure mode for a converged article — intra-corpus consistency ratifies a misframing rather than catching it.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Misattribution — Searle's "connection principle" named for a different doctrine.** The article glossed the connection principle as "all intentionality... is either conscious or derivable from conscious states," then illustrated it with the thermostat. Both halves misdescribe the principle. Searle's Connection Principle — introduced in "Consciousness, explanatory inversion, and cognitive science" (*Behavioral and Brain Sciences* 13(4), 1990, 585–596; developed at book length in *The Rediscovery of the Mind*, 1992) — states that **all unconscious intentionality must be accessible in principle to consciousness**. It is a thesis about the potential accessibility of *unconscious* intentional states, not about derivability. What the article actually described, and what the thermostat case illustrates, is Searle's separate **intrinsic vs. derived (observer-relative / as-if) intentionality** distinction. Right author, right pair of doctrines, wrong label attached to the wrong one.
**Resolution**: rewrote the paragraph to state the connection principle correctly and to present the intrinsic/derived distinction as the separate thesis it is, with the thermostat attached to the latter. The downstream inference ("If Grice and Searle are right, meaning cannot exist without consciousness") is unchanged and now rests on the premise that actually supports it — derived intentionality is precisely what makes the LLM case in the next paragraph go through.

**2. Attribution imprecision — Grice's 1957 analysandum inverted.** The article read "A sentence means what the speaker intends the audience to recognise they intend." Grice 1957 analyses **utterer's occasion-meaning**, not sentence meaning; separating the two is what the paper is known for, and he later analysed sentence meaning as a persistent pattern in speaker meaning rather than reducing it directly to intention. Attributing a *sentence*-meaning analysis to the reflexive-intention account inverts the distinction.
**Resolution**: restated the analysis as covering what a speaker means on an occasion (belief-intention + recognition-intention + reason-giving clause), then noted Grice's separation of utterer's meaning from sentence meaning and the pattern-based treatment of the latter. Verified against SEP's Grice entry. No new reference needed — the claim is scoped to what the existing Grice 1957 entry supports plus the standard reading of his later position, without asserting a specific later work.

**3. Factual/historical error and cross-article contradiction — "the decline of functionalist... approaches."** The article stated that logical behaviourism's failure "marked the decline of [functionalist](/concepts/functionalism/) and behaviourist approaches to consciousness vocabulary." This gets the chronology backwards: functionalism was the *successor* to behaviourism, arising from its collapse, not a co-casualty of it. It also contradicts the Map's own linked article — `obsidian/concepts/functionalism.md` opens "Functionalism is the leading account of the nature of mental states in contemporary philosophy of mind." The sentence declared functionalism declined while the same paragraph went on to deploy the zombie argument against it as a live position, and while the wikilink it used pointed at a page asserting the opposite.
**Resolution**: removed the false claim and added a paragraph that gets the succession right — functionalism took over the project, swapping behavioural dispositions for causal roles, buys real ground against the suppressed/faked/paralysed-behaviour objections, but inherits rather than dissolves the difficulty. The engagement is expressed in the same register the functionalism article already uses (the sufficiency claim is asserted without an account of why the role should feel like anything), and hands off to the phenomenal-concepts dilemma stated earlier in the article. This corrects an over-claim that ran *in the Map's favour* — the kind that collects ratification rather than challenge.

### Publisher-of-Record Citation Web-Verify Ledger

Scope: the one entry changed since the 7th review's full-corpus ledger. The other eight entries were verified real-correct on 2026-06-20 and are unchanged on disk; that ledger stands.

- Chalmers, D. (2007). "Phenomenal Concepts and the Explanatory Gap." In T. Alter & S. Walter (eds.), *Phenomenal Concepts and Phenomenal Knowledge: New Essays on Consciousness and Physicalism* (pp. 167–194). Oxford University Press. DOI `10.1093/acprof:oso/9780195171655.003.0009` — state: **real-correct**. Crossref chapter record confirms author David J. Chalmers, container *Phenomenal Concepts and Phenomenal Knowledge*, OUP New York, pp. 167–194, published-print 2007-01-01. Crossref book record `...001.0001` confirms the subtitle *New Essays on Consciousness and Physicalism*, editors Torin Alter and Sven Walter, ISBN 9780195171655. OpenAlex independently returns 2007, pp. 167–194. DOI resolves to `academic.oup.com/book/36049/chapter/313126380`.

**The new convention parenthetical is factually accurate and is retained.** Its two assertions were checked separately, since it is now serving to readers in nine live articles:
- *"released 2006"* — **confirmed**. OpenLibrary records ISBN 9780195171655 as published 20 November 2006, Oxford University Press USA, 359 pp. Independently corroborated by Chalmers's own preprint header at `consc.net/papers/pceg.html`, which reads "Forthcoming in... Oxford University Press, 2006."
- *"the 2007 OUP imprint year of record, which the DOI resolves to"* — **confirmed**. Crossref gives published-print and published-online both as 2007-01-01 for chapter and book alike.

The 2006/2007 split that divided prior reviewers is therefore a genuine hardback-ships-before-imprint-year case, not a reviewer error on either side. Both earlier verdicts were reasoning from real evidence; neither had both halves.

### Family Resolution (cross-corpus)

The 03:04Z propagation was verified rather than trusted. The canonical entry is present exactly once in each of all **ten** live loci, in both trees: `concepts/phenomenal-concepts-strategy`, `concepts/phenomenal-consciousness`, `concepts/phenomenal-acquaintance`, `concepts/qualia`, `concepts/language-and-consciousness`, `concepts/disguised-property-dualism`, `topics/duhem-quine-underdetermination-consciousness`, `topics/modal-structure-of-phenomenal-properties`, `voids/what-voids-reveal`, `voids/acquaintance-void`. The `hugo/` mirror agrees on all ten — already synced, no obsidian-only-fix gap.

A methodological note worth carrying forward: the first sweep of this family returned only nine loci and appeared to show `concepts/disguised-property-dualism` unpatched, because that file titles the chapter in sentence case ("Phenomenal concepts and the explanatory gap") and the grep used the canonical form's capitalisation. The tenth locus was in fact patched correctly. This is the "a narrow grep returning zero is not proof of absence" failure exactly — the search was written in the words of the fix rather than the words the file uses. Family sweeps over citation strings should be case-insensitive by default.

One locus outside the sweep: `archive/topics/phenomenal-concepts-as-materialist-response.md:177` retains the short pre-canonical form (no pages, no DOI, no subtitle). It is **not defective** — it gives 2007, the correct year — merely abbreviated, and it sits in the archive tree where bodies are frozen historical records. Recorded here so a future sweep does not read the mismatch as an unresolved split.

### Empirical-Record Currency Sweep
`find_superlative_claims` returned zero superlative claims. One near-superlative was introduced by this pass — "remains the leading account of mental states in contemporary philosophy of mind" — sourced to the Map's own [concepts/functionalism.md](/concepts/functionalism/) lead and uncontroversial in the 2020s literature. No currency risk.

### Medium Issues Found
None outstanding.

**Noted and deliberately declined**: the convention parenthetical is written in the imperative and addressed to a future editor ("cite the 2007 OUP imprint year of record"), which is editor-directed register appearing in reader-facing content. A purely reader-facing phrasing would be "hardback released November 2006; 2007 is the OUP imprint year of record." This was **not changed**, for three reasons: the imperative was a deliberate design choice recorded in the changelog (the convention is placed "where the next reviewer will hit it, not only in a review file nobody greps before editing"); rewriting it in one file would re-split the family that was just unified; and rewriting it in nine files fifteen minutes after installation is exactly the churn the convergence discipline exists to prevent. Future reviewers should leave it alone unless the operator wants the register changed corpus-wide as a deliberate call.

### Counterarguments Considered
All prior stability notes respected. Not re-flagged: inferentialist/Brandom engagement depth, absent Minimal Quantum Interaction / No Many Worlds connections, Dennett heterophenomenology and eliminative-materialist critiques.

### Possibility/Probability Slippage Check
None. The article makes no five-tier evidential-status claims. The lead's "These anomalies are evidence that consciousness involves something beyond the reach of linguistic analysis" is honestly scoped as evidence rather than proof, and the tenets section argues from expectation ("exactly what we would expect if") rather than asserting an upgrade. Applying the diagnostic test — would a tenet-accepting reviewer flag anything as overstated relative to the evidential scale? — the answer for the article as it now stands is no. It *was* yes for the "decline of functionalism" claim, which overstated the Map's dialectical position; that is fixed above.

### Reasoning-Mode Classification (editor-internal)
- Phenomenal concepts strategy: **Mode One** — the dilemma shows the strategy defective on its own terms. Unchanged.
- Logical positivism / behaviourism: **Mode One** — the programme failed by its own reductive standards. Unchanged.
- Functionalism (new engagement this pass): **Mode Two** — functionalism asserts role-occupancy suffices for experience without supplying an account of why, a standard its own explanatory commitments endorse. Credits the genuine ground the move buys before pressing the debt.
- Inferentialism: **Mixed**. Unchanged.
- Eliminative materialism / hard-nosed physicalism: **Mode Three**. Unchanged.

No editor-vocabulary leakage in article prose (grep-confirmed clean after edits). No boundary-substitution.

## Optimistic Analysis Summary

### Strengths Preserved
- Cumulative architecture (Meaning → Private Language → Reference → Expressibility)
- Phenomenal concepts dilemma paragraph
- Tripartite analysis ("describe partially, refer problematically, express lossily")
- Gricean → bidirectional-interaction argument, the article's distinctive contribution
- Front-loaded opening summary
- Comprehensive inbound link network

### Enhancements Made
- Grice paragraph now carries the full three-clause reflexive-intention analysis rather than a one-line gloss, which strengthens the "conscious intentions reflexively grasped" claim that immediately follows it.
- Searle paragraph now presents two distinct theses instead of one conflated one, giving the LLM/symbol-grounding paragraph a premise that actually supports it.
- New functionalism paragraph closes a real gap: the article previously jumped from behaviourism's failure to the Map's conclusion without acknowledging the successor position that occupies the field.

### Cross-links Added
- [phenomenal-concepts-strategy](/concepts/phenomenal-concepts-strategy/) gains a second in-body link from the new functionalism paragraph, tying the Expressibility section back to the Reference section's dilemma.
- [functionalism](/concepts/functionalism/) link retained and its surrounding claim corrected, so the link no longer points at a page contradicting the sentence containing it.

## Length Check
1868 → 2109 words (+241). 84% of the 2500 soft threshold — status ok. Below threshold, so expansion was permitted; no compensating cuts required.

## Remaining Items
None.

## Stability Notes
- Eight reviews complete. This pass is evidence that "converged" is not the same as "verified": three attribution defects survived seven passes because each was internally consistent and matched sibling articles. The lens that caught all three was citation-framing accuracy — checking what the source *says* against what the article says it says, at the publisher, rather than checking metadata or cross-corpus agreement.
- The Chalmers 2006/2007 question is **settled and should not be reopened**. Both dates are real: hardback 20 Nov 2006 (OpenLibrary), OUP imprint and DOI year 2007 (Crossref). The corpus cites 2007 with the discrepancy noted inline. Any future reviewer finding "2006" in an external source has found the hardback ship date, not an error.
- The convention parenthetical's editor-directed register is a known, deliberate trade-off. Do not rewrite it in a single file.
- Framework-boundary disagreements (eliminativism, hard-nosed physicalism, MWI, quantum skepticism) are not deficiencies and must not be re-flagged.
- The article should be excluded from review until substantively modified or the References block changes again.