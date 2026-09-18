---
title: "Deep Review - Training Contamination as a Confound for AI Introspection Probes"
created: 2026-09-18
modified: 2026-09-18
human_modified:
ai_modified: 2026-09-18T13:12:46+00:00
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
**Article**: [[concepts/training-contamination-confound|Training Contamination as a Confound for AI Introspection Probes]]
**Previous review**: [[deep-review-2026-06-20-training-contamination-confound|2026-06-20]]

## Why re-reviewed despite a converged prior pass

Same trigger shape as 2026-06-20. Two refine-draft commits landed on this file on
2026-09-18 and neither was covered by any deep review:

- `67d98da2bb` — recalibrated the Singh, Linzen & Ravfogel corroboration after
  finding the article quoted **v1**'s "behavioral evidence alone is inherently
  insufficient…", which **v2** withdrew. Added a new paragraph under
  §"What Could Discriminate Mechanism from Imitation" carrying **three new
  verbatim quoted strings**, rewrote the lead's second paragraph, rewrote the
  §"Prior Art" bold sub-head paragraph, and expanded footnote `[^singh]` with a
  version note.
- `a5c2404925` — machine-evidence-wing cross-link pass (a task aimed at the
  *wing*, not at this article): added a `cross-architecture-llm-introspection`
  bullet, a piped wikilink to the agentic-AI article, and a Further-Reading entry.

The 2026-06-20 stability note says the nine grafted citations "should NOT be
re-litigated **unless the References block is modified again**." It was modified
again — `[^singh]` grew a version-discrimination clause and three new quotes were
installed. Scope of this pass is therefore **the changed material only**: the
other eight footnotes ([^udell], [^schwitz], [^chalmers], [^cheng], [^lindsey],
[^binder], [^livebench], [^butlin]) were publisher-verified on 2026-06-20, are
untouched, and were not re-swept.

## Lenses run this pass

Publisher-of-record quote verification (§2.4) on the changed cite · version-date
verification · inline↔References cross-reference · secondary-host fidelity
(drive-by insertions) · lead-vs-body consistency · internal contradiction ·
dangling-reference / antecedent check · possibility-probability slippage ·
editor-vocabulary leakage (§2.6) · empirical-currency superlative sweep ·
wikilink slug-collision check · length gate.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Version-attribution error in footnote `[^singh]` — FIXED.** The footnote's
  sole function is to discriminate v1 from v2, and it asserted that "the two
  conditions **and the 'current evidence is insufficient' conclusion** are v2's."
  The two conditions are indeed v2-only. The conclusion is **not**: v1 already
  concludes *"these results indicate that current evidence is insufficient to
  establish that LLMs display metacognitive monitoring"* (verified in the v1
  abstract at offset 2238). Only the *wording* is v2's. A reader would infer v1
  lacked that conclusion, which is false — the same defect class the 2026-06-20
  pass caught (an apparatus that ratifies a reading rather than the text).
  **Fix:** "…the two conditions are v2's; both versions conclude current evidence
  is insufficient, quoted here in v2's wording."

### Publisher-of-Record Web-Verify Ledger (§2.4) — changed cite only

Raw artefacts fetched with `curl` (not a summariser) from `arxiv.org/abs/2605.26242`
and `arxiv.org/abs/2605.26242v1` **separately** — the arXiv API returns the latest
version only. Both HTML bodies stripped of markup, NFKC-normalised, whitespace-
collapsed, then substring-matched. Offsets recorded.

- **Singh, Linzen & Ravfogel 2026** (*Can LLMs Introspect? A Reality Check*,
  arXiv:2605.26242) — **real-wrong-metadata (version attribution), FIXED.**
  Authors, title, ID: correct. Version dates: **correct** — v1 `Mon, 25 May 2026`,
  v2 `Fri, 21 Aug 2026`, matching the footnote's "v1, 2026-05-25; v2, 2026-08-21".
  Per-string result:

  | Quoted string | v1 | v2 | Article assigns to | Verdict |
  |---|---|---|---|---|
  | "behavioral evidence alone is inherently insufficient to establish strong introspective claims" | HIT @951 | ABSENT | v1, withdrawn by v2 | correct |
  | "First, the test needs to require privileged access: it should not be solvable using cues available in the input" | ABSENT | HIT @867 | v2 | correct |
  | "it needs to require second-order computation: second-order, meta-representations of first-order, task-related representations" | ABSENT | HIT @988 | v2 | correct |
  | "cannot be satisfied by task performance alone: it requires designs under which second-order and first-order accounts make divergent predictions" | ABSENT | HIT @1130 | v2 | correct |
  | "current evidence is insufficient to establish metacognitive monitoring in LLMs" | ABSENT | HIT @2004 | v2 | wording correct, **but see below** |
  | "current evidence is insufficient to establish that LLMs display metacognitive monitoring" (v1 variant) | HIT @2238 | ABSENT | — | **the footnote defect** |

  All five installed quotes are genuine verbatim in the version the body assigns
  them to. No fabrication. The single defect is the footnote's exclusive
  assignment of the *conclusion* to v2.

  Result-direction leg: v2's classifier-parity finding ("classifiers that can only
  access the input match the models' in-context predictions, indicating that the
  original results do not demonstrate privileged access") matches the article's
  paraphrase in direction and in sign. Not a null-result inversion.

  Cited-author-stance leg: Singh et al. are introspection *skeptics* on the
  current record and make no metaphysical commitment. The article does not
  present them as endorsing the Map's in-principle claim — it explicitly says
  "The stronger claim … remains the Map's own." Correctly separated.

  Incidental (no action): v2 carries `Comments: Accepted at COLM 2026`. The
  article does not cite a venue, so no metadata is wrong; a future refine could
  add it.

- Inline ↔ References: complete. `[^singh]` is now cited twice inline (§Prior Art,
  §What Could Discriminate) — legitimate, not an orphan. All 9 footnotes defined
  and cited; no orphans either direction. The 2 numbered in-corpus references are
  unchanged and untouched.

### Medium Issues Found

- **Internal seam between §"What Could Discriminate" and its own bullets,
  sharpened by today's insert — FIXED.** The section opened "the discriminating
  evidence must come from **outside** it—from the system's internals rather than
  its outputs," but two of its three candidates (OOD generalization,
  contamination-controlled training) are *output*-based — they work by controlling
  what the corpus supplied, not by leaving the output channel. Today's new
  paragraph made the seam visible by naming the target as a regime where the two
  accounts "predict *different* **outputs**." **Fix:** "…from the system's
  internals, or from output regimes the training corpus could not have supplied."
  This now covers all three bullets and the imported Singh condition without
  weakening the thesis.

- **Dangling demonstrative in §"Prior Art" opening — FIXED.** The refine changed
  "…and now converges on the same conclusion from three independent directions"
  to "…and is now approached from three independent directions," but left the
  trailing clause "—and that convergence is the point." The edit removed the noun
  "convergence" referred to, so the demonstrative had no antecedent. **Fix:**
  "—and that **independence** is the point," which anchors to "three independent
  directions" and is elaborated by the very next sentence ("A defeater discovered
  **separately** by…"). One word for one word; also the safer calibration, since
  it does not re-assert the convergence claim the refine deliberately narrowed.

- **Lead-duplication inside the §Prior Art paragraph — TRIMMED.** "The
  literature's settled verdict is about the record: published behavioural results
  do not establish introspection, and the conditions under which a behavioural
  paradigm *could* are demanding and unmet by the designs in use" restated the
  lead (L31) almost word for word, immediately after the v2 conclusion quote and
  "The revision narrows what may honestly be claimed" had each already said it —
  triple redundancy in one paragraph. Replaced with "The settled verdict is about
  the record, not about what behaviour could in principle show," which is shorter
  and sharpens the foil for the following "The stronger claim … remains the Map's
  own." Both trimmed propositions survive verbatim in the lead and in the §What
  Could Discriminate paragraph. Checked `reviews/` and `workflow/` for a review
  that quotes the removed sentence: none (it was written today), so no live
  refutation stranded.

### Secondary-host fidelity — drive-by insertions from `a5c2404925` (VERIFIED, no defect)

The cross-link bullets were added by a task aimed at the machine-evidence *wing*,
so they never got a fidelity pass at their host. Both characterisations check out:

- **`cross-architecture-llm-introspection` bullet.** The quoted string
  "architecturally convergent rather than corpus-inherited" is verbatim at that
  article's L84 (§"The Inference and Its Assumptions"), where it is the fourth and
  "most consequential" assumption — so "its own assumption ledger records that"
  is accurate, including the "most consequential for the headline inference"
  weight the bullet implies. "The article specifies what would break it: a
  signature that could not have been copied from the corpus" matches L84's "What
  would disconfirm the imitation reading is a signature that cannot have been
  copied from the corpus." The bullet's "which **would** make those signatures
  architecture-general" correctly preserves the source's hedge (L72: "one live
  reading is"). Reciprocal link already exists — the source's "corpus-inherited"
  *is* a wikilink back to this article.
- **Agentic-AI clause.** "A higher indicator score is granted outright and the
  verdict is still made to turn on substrate rather than on the scorecard"
  matches that article's L42 ("The Map grants this empirical premise in full")
  and L30 ("leaving untouched the two objections that turn on substrate rather
  than operation"). Accurate.
- Both link targets are bare slugs with **zero stem collisions** across
  `obsidian/` and `archive/`, so both resolve.

### Calibration / slippage / leakage scan

- **No possibility/probability slippage.** Today's edits moved the article
  *down* the confidence scale, not up: the lead now claims a "narrower
  conclusion", and the in-principle claim is explicitly quarantined as "the Map's
  own … rather than … borrowed authority." A tenet-accepting reviewer would not
  flag any claim as overstated. The new Singh paragraph imports a *constraint*,
  not an evidential upgrade.
- **Level-shift handled honestly.** Singh's "privileged access" condition is about
  cues in the *input*; training contamination is about cues in the *corpus*. The
  article does not conflate them — it states the difference explicitly ("the same
  demand pushed one level back"). This was the likeliest place for a source/Map
  conflation and it is clean.
- **No editor-vocabulary leakage** (§2.6): zero hits for Mode One/Two/Three,
  "Engagement classification", `direct-refutation-feasible`, `unsupported-jump`,
  `bedrock-perimeter`, `tenet-register`, `**Evidential status:**`. The article
  engages no named opponent in a refutation register, so §2.6 classification does
  not apply.
- **Empirical-currency sweep**: `find_superlative_claims` returned empty. No
  standing-record claims.

### Counterarguments Considered

- **Popperian empiricist**: "the new paragraph imports an external standard that
  a *behavioural* design could meet — doesn't that undercut the article's thesis
  that behaviour cannot discriminate?" This is the seam fixed above. The resolved
  reading: Singh's divergent-predictions condition can be met behaviourally *only*
  where the corpus did not supply the regime, which is exactly the article's
  position. No residual contradiction.
- **Eliminative materialist / physicalist**: the mechanism-vs-imitation
  distinction presupposes a fact beyond behaviour. **Bedrock, carried from
  2026-05-31 and 2026-06-20. Not re-flagged.**

## Optimistic Analysis Summary

### Strengths Preserved
- The five-step generalization argument, "publicity is contamination", the
  graduated exposure ladder, and the "named and individually tractable but not
  yet delivered" discriminator status — all untouched, per the 2026-05-31
  stability note.
- **The 09-18 recalibration is exemplary work and is preserved intact.** Catching
  that a cited source *withdrew* the sentence the article leaned on, then
  quarantining the stronger claim as the Map's own rather than deleting it, is
  the evidential-status discipline working as designed. The Hardline Empiricist
  lens rates this the strongest single move in the article's history: an external
  authority was *lost* and the article got more honest rather than quieter.
- The new §What Could Discriminate paragraph earns its words: it converts a
  withdrawn quote into a *constructive* external specification, and the
  input-versus-corpus level distinction is a genuine philosophical contribution
  rather than a patch.

### Enhancements Made
- Four targeted edits (above): one critical footnote correction, one seam repair,
  one antecedent repair, one redundancy trim.

### Cross-links Added
- None. Today's `a5c2404925` pass completed the cross-link set and both new links
  verify; adding more would be churn.

## Length

`analyze_length`: **3304 → 3298 words** (−6), `soft_warning`, concepts soft 2500 /
hard 3500. Operated in length-neutral mode as instructed: +5 (footnote) +7 (seam
repair) +0 (antecedent) −19 (redundancy trim). Headroom to the `>= hard` gate is
201 words (ceiling 3499).

## Attribution note

`ai_system` was `claude-opus-4-8` and is now `claude-opus-4-8+claude-opus-5` per
the dual-attribution convention. **The model that ran the two 2026-09-18 refine
commits could not be established from the repo** and was not guessed; the
pre-existing `claude-opus-4-8` component is carried forward unchanged and may
under-attribute those passes. This pass is `claude-opus-5`.

## Remaining Items

- **Low, no action taken.** L46 ("This is not a flaw in any *particular* probe
  design; it is a structural property…") is the semicolon form of the discouraged
  "This is not X. It is Y." construct. It predates both prior reviews, the
  2026-06-20 pass explicitly certified the article clean on this construct, and
  the contrast does real work. Rewriting it now would be oscillation, not
  improvement. Recorded so the certification is accurate rather than acted on.
- **Informational.** `obsidian/research/training-contamination-introspection-probes-2026-06-20.md`
  still carries the withdrawn v1 quote (L87, L160) without a version note. It is a
  *dated research note* and correct as of its date, so it is deliberately left
  alone — but a future reader mining it could reintroduce the v1 sentence.
- No task minted: nothing remains that this pass could not finish.

## Stability Notes

- The materialist/eliminativist bedrock objection is **carried unchanged** from
  2026-05-31 and 2026-06-20. Do not re-flag.
- **Citation ledger scope.** The 2026-06-20 ledger stands for the eight untouched
  footnotes. `[^singh]` is now re-verified at the publisher of record **at the
  version level** — all five quoted strings matched verbatim in their assigned
  version, and the version dates are correct. Do not re-litigate `[^singh]`
  unless the footnote or its quoted strings change again. Note that verifying
  this cite **requires fetching `/abs/2605.26242v1` explicitly**; the arXiv API
  and the bare `/abs/` URL both return v2 only, so a future check that uses the
  default endpoint will get a false "quote absent" on the v1 sentence.
- **Lesson, third instance of the same pattern.** Both 2026-06-20 and this pass
  were triggered by a refine that grafted web material past a "converged"
  article, and both found a defect in the *apparatus* rather than the substance:
  06-20 found quotation marks around words the source does not contain; 09-18
  found a version footnote that assigns a shared conclusion to one version. A
  refine that correctly discovers a source has been revised can still misstate
  *what* was revised. The general rule: **when an edit's whole purpose is to
  discriminate two versions of a source, verify both versions separately** — the
  discriminating apparatus is exactly where the unverified claim hides.
- The 09-18 recalibration (quarantining the in-principle claim as the Map's own)
  is the correct resolution and should be **preserved**. Do not let a future pass
  restore "the literature has converged on the Map's conclusion" — the external
  literature supports only the narrower, record-scoped verdict.
