---
ai_contribution: 100
ai_generated_date: 2026-07-18
ai_modified: 2026-07-18 00:35:17+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-18
date: &id001 2026-07-18
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - The Parsimony Case for Interactionist Dualism
topics: []
---

**Date**: 2026-07-18
**Article**: [The Parsimony Case for Interactionist Dualism](/topics/parsimony-case-for-interactionist-dualism/)
**Previous review**: [2026-06-20](/reviews/deep-review-2026-06-20-parsimony-case-for-interactionist-dualism/) (ninth pass; this is the tenth)

## Focus of This Pass — refine→cross-review verification (Lycan quote fix)

This pass verifies that the 2026-07-16 refine (commit db22e5c21) corrected the Lycan
(2009) word-inside-quote defect onto the TRUE verbatim wording — guarding against the
"fix that corrupts" pattern where a refine introduces a new error while fixing the old.
The refine changed the quoted line from:

- BEFORE: `admits that "there is no evidence against dualism; it only offends parsimony"`
- AFTER: `admits of dualism that "there is no evidence against that view; it only offends parsimony"`

i.e. it moved the paraphrased antecedent ("dualism") OUTSIDE the quotation marks and
restored the verbatim quoted form "that view".

## §2.4 Publisher-of-Record Citation Web-Verify — targeted (changed line only)

Only the Lycan line changed since the 06-20 full-corpus web-verify ledger; the rest of
the References block is unchanged and carries the 06-20 verified states forward. The two
quotes touched by the refine were re-verified INDEPENDENTLY at the primary source
(newdualism.org hosting of the AJP text + buffalo.edu PDF), NOT at unfinishablemap.org
(circular) or aggregators (corruption risk).

- **Lycan 2009 (Giving Dualism its Due, AJP 87(4), 551–563) — real-correct; refine CONFIRMED.**
  The exact verbatim string `As before, there is no evidence against that view; it only
  offends parsimony.` appears in the paper (twice — in the Lewis-Armstrong and Papineau
  passages, identical wording each time). "That view" is the dualist causal-overdetermination
  view. The refine's move — de-quoting the paraphrased antecedent "dualism" and restoring the
  verbatim "that view" — is exactly right; it landed on Lycan's true words and introduced NO
  new corruption. The 06-20 ledger had accepted the prior "against dualism" form as a "faithful"
  antecedent substitution; the refine upgraded it to strict verbatim. Good.
- **Lycan "a very posterior reason" — real-correct (verbatim).** Primary text: "But it is a
  very posterior reason. That is, not only does it always carry the qualification 'other
  things being equal,' but many, nearly all, other things must be equal before parsimony is
  called in to break the tie." The quoted substring "a very posterior reason" is faithful.
- **Smart 1959 "severely criticized" — real-correct (unchanged; general characterisation).**
  Not a Lycan verbatim quote; functions as scare-quotes describing the historical reception of
  Smart's identity-theory / parsimony argument (historically accurate). Classified real-correct
  across the prior ledger; left unchanged to avoid churn on a converged article. Minor
  observation only: the quotation marks read as attribution but the phrase is a paraphrase —
  a de-quote is defensible but is a stylistic micro-edit, not a defect.
- **Churchland 1984 (Matter and Consciousness) — real-correct (unchanged).** The 06-20 review
  corrected a false-verbatim "inconclusive regarding duality" quote to the documented
  no-single-argument-is-conclusive concession (no quote marks). The current body carries that
  corrected form; verified still-corrected this pass.
- All other cites (Anderson, Chalmers, Frankish, Hubbard, Huemer, Koksvik, Masi, Zanotti,
  Southgate & Oquatre-six) — carried forward real-correct from the 06-20 full ledger; body
  text for each unchanged since. NEVER-STRIP Map self-cite pseudonym (Oquatre-six) intact.

Inline ↔ References cross-check: unchanged since 06-20 (all matched). Empirical-record
currency sweep: no superlative claims (helper empty at 06-20; body unchanged). No banned
constructions ("This is not X. It is Y."; gratuitous "load-bearing") introduced.

## Pessimistic Analysis Summary

### Critical Issues Found
None. The one changed line since last review (Lycan quote) is verified verbatim-correct.

### Medium Issues Found
None new. Calibration guard from prior passes holds: the article makes the *dialectical*
reversal (turning the objector's parsimony commitment against them) without a first-person
Map endorsement of parsimony-as-truth-tracker — Tenet 5 self-binding preserved. No
possibility/probability slippage.

### Counterarguments Considered
Bedrock framework-boundary disagreements (physicalist / MWI / eliminativist rejection of the
tenets) remain expected and are NOT re-flagged, per convergence discipline.

## Optimistic Analysis Summary

### Strengths Preserved
- Hostile-witness framing (Smart, Lycan, Churchland) — now resting on strict-verbatim Lycan
  quotes, which strengthens the rhetorical force.
- Dimensional-reversal and modesty-ledger symmetry arguments — intact.
- Self-qualifying honesty in the proliferation section ("suggestive rather than dispositive").

### Enhancements Made
None — genuine no-op after real scrutiny (the refine already did the substantive fix).

### Cross-links Added
None.

## Remaining Items

- P3 (carried from 06-20): [topics/arguments-against-materialism.md](/topics/arguments-against-materialism/) line 99 presents
  Churchland's concession in quote marks ("qualifies it as 'not conclusive'") — family-resolution
  polish, still deferred.
- Optional micro-edit: de-quote Smart "severely criticized" (paraphrase-in-quotes). Not a
  defect; not worth a churn commit on its own.

## Stability Notes

Tenth pass; the article is at stable convergence. The refine→cross-review chain is CLEAN:
the Lycan word-inside-quote fix landed on the true verbatim wording with no new corruption —
the "fix that corrupts" pattern did NOT occur here. Content unchanged this pass; only
`last_deep_review` bumped (ai_modified held at the refine's HEAD value, ai_system held).

Do NOT re-inflate the dialectical conclusion to "the Map concludes dualism is more
parsimonious / truer" (Tenet 5 forbids), and do NOT re-introduce the false-verbatim
Churchland "inconclusive regarding duality" quote (Map paraphrase, not Churchland's words).