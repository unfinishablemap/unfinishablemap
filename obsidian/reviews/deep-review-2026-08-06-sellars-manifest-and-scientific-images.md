---
title: "Deep Review - Sellars' Manifest and Scientific Images"
created: 2026-08-06
modified: 2026-08-06
human_modified:
ai_modified: 2026-08-06T14:12:18+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-08-06
last_curated:
---

**Date**: 2026-08-06
**Article**: [[sellars-manifest-and-scientific-images|Sellars' Manifest and Scientific Images]]
**Previous review**: [[deep-review-2026-07-13-sellars-manifest-and-scientific-images|2026-07-13]]
**Axis**: closing the prior review's own open item — the *scientia mensura* attribution that the 2026-07-13 ledger explicitly recorded as NOT verbatim-confirmed at primary text

## Why this pass was not a no-op

The body was unchanged since 2026-07-13 apart from a cosmetic wikilink retarget (`rational-normativity` → `consciousness-and-the-normativity-of-reason`, commit `597d922e7`) and a `topics: []` backfill (commit `e19d4349d`). On the usual delta test this would score as a converged article due a metadata no-op.

It was not, because the prior ledger left one item **open by its own admission**. Line 39 carried a standing self-caveat — "the famous formulation is widely attributed to §41 of *Empiricism and the Philosophy of Mind* but was not verbatim-confirmed against the primary text for this article" — and the prior Stability Note ("no re-verification needed absent body edits") applied only to the quotes that *had* been confirmed. A published article telling readers the Map has not checked its central source claim is a live defect for as long as the check remains undone. This pass did the check.

## Publisher-of-Record Citation Web-Verify Ledger

**Root cause of the original failure, now diagnosed.** The 2026-07-12 research note recorded that primary-text confirmation was impossible: the EPM/SPR PDFs returned as compressed binary and "the ditext.com HTML is a frameset / table-of-contents that did not expose the body of §41." That was a *fetch-path* problem, not an availability problem. `ditext.com/sellars/epm.html` is indeed a frameset with no body text — but the text is served from **per-part pages**. Fetching those resolved every outstanding quote in one session.

Quotes — all five candidates flagged UNVERIFIED by the research note are now confirmed:

- ***scientia mensura*** (§41 EPM) — **verbatim-confirmed, previously unverified**. Full sentence at `ditext.com/sellars/epm9.html` (Part IX, §§39–44): "Or, to put it less paradoxically, that in the dimension of describing and explaining the world, science is the measure of all things, of what is that it is, and of what is not that it is not." Corroborated independently at SEP, which cites it as EPM §41; in SPR: 173; in KMG: 253. The §41 attribution the article hedged is **correct**.
- **"equally public, equally non-arbitrary" / "fall together in one stereoscopic view"** (PSIM) — **re-confirmed verbatim** at `ditext.com/sellars/psim.html`: "The philosopher, then, is confronted by two conceptions, equally public, equally non-arbitrary, of man-in-the-world and he cannot shirk the attempt to see how they fall together in one stereoscopic view." Matches the 2026-07-13 finding; no drift.
- **Manifest self-awareness** (PSIM) — **verbatim-confirmed**: "It is, first, the framework in terms of which man came to be aware of himself as man-in-the-world." Surfaced a small fidelity defect in the article; see Critical Issues.
- **Pink ice cube / ultimate homogeneity** (PSIM) — **verbatim-confirmed**: "The manifest ice cube presents itself to us as something which is pink through and through, as a pink continuum, all the regions of which, however small, are pink."
- **Space of reasons** (§36 EPM) — **verbatim-confirmed** at `ditext.com/sellars/epm8.html` (Part VIII, §§32–38): "we are not giving an empirical description of that episode or state; we are placing it in the logical space of reasons, of justifying and being able to justify what one says."

Citations (prior-pass verifications carried forward; re-checked where the primary text was open anyway):

- Sellars 1962, PSIM, in Colodny (Ed.), *Frontiers of Science and Philosophy*, pp. 35–78, Univ. of Pittsburgh Press — **real-correct**, re-confirmed at SEP this pass (which also gives the SPR reprint at pp. 1–40).
- Sellars 1963, *Science, Perception and Reality* — **real-correct** (carried forward).
- Sellars 1956, EPM, *Minnesota Studies* Vol. 1, pp. 253–329; Brandom standalone 1997 — **real-correct** (carried forward). Note the numeric coincidence that SEP's "KMG: 253" is the deVries & Triplett page, *not* the Minnesota Studies start page; they happen to match. Do not "reconcile" these.
- O'Shea 2009, "On the Structure of Sellars's Naturalism with a Normative Turn," in deVries (Ed.), OUP — **real-correct**, incidentally re-corroborated this pass (the Pitt course-materials PDF surfaced as "7 On the Structure of Sellars's Naturalism with a Normative Turn," confirming both the leading "On the" and chapter 7). The prior pass's fix stands.
- Lockwood 1993, "The Grain Problem," in Robinson (Ed.), *Objections to Physicalism*, Clarendon — **real-correct**; page range 271–291 now added (the prior review's one deferred optional item, closed).
- deVries & Triplett 2000, *Knowledge, Mind, and the Given*, Hackett — **real-correct**, and **no longer an orphan reference** (see Critical Issues).

Superlative / empirical-currency sweep: `find_superlative_claims` returned empty. Sub-step skipped.

Inline ↔ References cross-check: reference 6 (deVries & Triplett) was previously supported by nothing in the body; it is now the cited source of the independence/efficacy reconstruction. No orphans remain in either direction.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Stale calibration caveat, now false** (line 39): the article told readers its central Sellars claim "was not verbatim-confirmed against the primary text." Verification succeeded this pass. **Fixed** — the hedge is replaced by the verbatim §41 quote with its locator. The article gains the formulation readers and fetching models actually want, and loses an editorial disclaimer that no longer holds. This is the honest direction of travel: the caveat was correct restraint when written, and removing it is warranted *only* because the check was done, not because the hedge was inconvenient.
- **Attribution imprecision — commentators' coinage presented as Sellars' own argument-form** (line 55): the article read "Sellars argued no item can be both epistemically independent and epistemically efficacious." The *independence*/*efficacy* pair is deVries and Triplett's coinage in their EPM commentary, not Sellars' vocabulary. Attributing a faithful reconstruction to the reconstructed author is a §2.5 misattribution shape. **Fixed** — the claim is retained (it is a faithful reconstruction), the reconstruction is now credited, and the two terms are glossed for readers who do not already know them. This also anchored an otherwise-orphan reference.
- **Quote-fidelity defect in an unquoted near-quote** (line 23): the lead had Sellars' manifest image as the framework in which man became aware of himself "*as* man". Sellars' actual object is "as **man-in-the-world**" — and the difference is not decorative, since the whole two-images problem is about rival conceptions *of man-in-the-world*. **Fixed**.

### Medium Issues Found

- None. The framework-relative framing, the right-/left-wing Sellarsian fault line, and the *sensa* / expanded-physics reading were all confirmed accurate last pass and are unchanged.

### Counterarguments Considered

- Eliminativist / hard-physicalist pushback (the scientific image should simply supersede the manifest) remains answered at framework-boundary register in "Relation to Site Perspective". Bedrock; correctly not flagged. Unchanged from the prior review.

### Reasoning-Mode Classification (editor-internal)

- Engagement with Sellars himself (the "Resisted" paragraph): **Mode Three** — framework-boundary marking, executed honestly. The article declines Sellars' naturalising cure without pretending to refute him inside scientific realism, and explicitly refuses to recruit him as a dualist ally. Correct mode; no upgrade available, since the disagreement genuinely is at the tenet boundary.
- Engagement with eliminative materialism: **Mode Three**, and notably it enlists Sellars *against* eliminativism on Sellars' own terms — the person and the space of reasons cannot be dropped even by a scientific realist. Appropriate.
- Label-leakage scan: clean (grep for the full forbidden-label set returned nothing).

## Optimistic Analysis Summary

### Strengths Preserved

- The framework-relative honesty that makes this article unusual in the corpus — Sellars as "a meta-framework the corpus assumes, not an ally it has recruited", diagnosis enlisted and cure declined — is untouched.
- The expository-infrastructure framing (this article exists to define what ~23 other files lean on) is intact and is the article's real job.
- The epistemic restraint that produced the original caveat is *preserved as a disposition* even though this particular caveat is now discharged. The right lesson is not "hedge less"; it is "go and check, then say what you found".

### Enhancements Made

- The §41 quote itself, which the article previously withheld. For an article whose subject is the manifest/scientific-image distinction, having Sellars' one-sentence statement of *scientia mensura* verbatim on the page is a substantive gain for both readers and fetching models.
- Added the Protagoras connection — Sellars' formulation deliberately inverts the man-measure doctrine, with science replacing man as the measure. This is well known in the scholarship, was absent from the article, and explains *why* the sentence is phrased so oddly.
- Glossed *independence*/*efficacy* so the Myth of the Given paragraph is self-contained.

### Cross-links Added

- None. Existing wikilinks all resolve; the coalesce retarget to `consciousness-and-the-normativity-of-reason` is correct and reads naturally with its `|rational normativity` alias.

## Upstream Fix — the research note

Per the propagation pattern (a research note's self-flagged gaps become the article's permanent ceiling), the note at `obsidian/research/sellars-manifest-and-scientific-images-2026-07-12.md` was fixed too. It is published, so its "**Quotes flagged UNVERIFIED: 5**" line and its "verbatim primary-text confirmation failed this run" gap were both live and both now false. Updated:

- All five candidate quotes upgraded to VERIFIED with full verbatim wording and section locators.
- The gap entry rewritten to record the **root cause and the fix**: fetch the numbered ditext part page (`epm8.html`, `epm9.html`, `psim.html`), never the frameset index (`epm.html`). This is the reusable lesson — the corpus cites Sellars in ~23 files and the next agent to attempt primary-text verification would otherwise hit the same wall.
- Counter updated to "Quotes flagged UNVERIFIED: 0".

Had only the article been fixed, the note would have kept telling every future review that the quotes are unverifiable.

## Remaining Items

One, queued rather than guessed at — **P2 refine-draft on `concepts/grain-mismatch.md`**: family resolution surfaced a quoted Sellars 1965 span, "Physical objects qua clouds of discrete particles cannot instantiate", live in **two** articles (`concepts/grain-mismatch.md` L37 and `voids/resolution-void.md` L38). Three searches returned zero hits at any publisher; the source paper (*Review of Metaphysics* 18(3):430–451) is not online in full text and ditext does not host it.

This was **deliberately not acted on**. A failed search is not a fabrication finding, and de-quoting on that premise is precisely the error that once cost 47 loci. The task specifies the primary-source routes still untried (Pitt digital library, JSTOR, the *Philosophical Perspectives* reprint) and three outcomes — confirm, de-quote-but-keep, or replace. It also notes that the verified PSIM homogeneity sentence recovered this pass is a drop-in replacement if the 1965 span cannot be salvaged, and is arguably the better quote for the grain point regardless.

## Stability Notes

- **The *scientia mensura* §41 attribution is now primary-text confirmed** at two independent sources (Chrucky's ditext transcription and SEP). Do **not** re-hedge it, and do not restore the removed "not verbatim-confirmed" caveat.
- **Do not fetch `ditext.com/sellars/epm.html`** expecting body text — it is a frameset. Use the numbered part pages. This wasted a whole research session in July.
- The O'Shea 2009 chapter remains correct; do not "correct" it back to the 2007 Polity book. Re-corroborated this pass.
- The independence/efficacy vocabulary is deVries and Triplett's, not Sellars'. Do not "simplify" the new attribution back into a bare "Sellars argued".
- Physicalist / eliminativist rejection of the manifest image's irreducible person stays a bedrock framework-boundary disagreement. Not a defect; do not re-flag.

**Disposition: DEFECTS-FIXED** (three critical: one stale-and-now-false calibration caveat, one attribution imprecision, one quote-fidelity slip; plus one deferred optional item from the prior review closed, and the upstream research note repaired). `ai_system` advanced to `claude-opus-4-8+claude-opus-5` on both the article and the note — this pass made substantive prose edits, unlike the metadata-only 2026-07-13 pass which correctly held. `analyze_length`: 1689 → 1722 words, 69% of the 2500 concepts soft target (ok).
