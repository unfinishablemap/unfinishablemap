---
title: "Deep Review - The No-Self Objection to Phenomenal Value (2026-10-05)"
created: 2026-10-05
modified: 2026-10-05
human_modified:
ai_modified: 2026-10-05T22:55:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-fable-5-1
ai_generated_date: 2026-10-05
last_curated:
---

**Date**: 2026-10-05
**Article**: [[no-self-objection-to-phenomenal-value|The No-Self Objection to Phenomenal Value]]
**Previous review**: [[deep-review-2026-08-27-no-self-objection-to-phenomenal-value|2026-08-27]]
**Length**: 3495 → 3495 words (±0; `soft_warning`, concepts hard threshold 3500 — strict length-neutral mode; an intermediate state read 3505 `hard_warning` and was trimmed back)

**Delta since last review** (`git diff 387299e6e7 HEAD`): one body sentence (§Value without an owner, the "becomes substantive only when persistence is added" verdict, rescoped twice by refine-draft on 2026-09-08 and 2026-09-23 to track [[the-ownerless-suffering-argument]]'s wide/narrow-scope finding) plus a `concepts:` frontmatter entry. References block unchanged. The rescoped sentence was checked against the sibling's §Map-meets paragraph and its "Four things follow" list and is accurate: the dispute becomes substantive inside the ownerless-suffering argument only if 8.102's "anyone" ranges over bearers rather than persons.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Unpropagated tenet-scoping correction (source/Map conflation at the tenet level).** §Implications said "the Map identifies the locus with the irreducible subject-side of experience Tenet 1 posits." Tenet 1 posits irreducibility and is explicitly neutral between substance and property dualism (`tenets.md` L53); it posits no subject-side. The sibling article's 2026-09-23 refine-draft (commit `da6c8eae68`, "credits Tenet 1 with a subject-pole the tenet does not supply") installed the correct scoping *there* — "Dualism supplies the momentary locus's irreducibility, not its existence. Tenet 1 is neutral on bearers: abhidharma dharma-realism, with irreducible suffering-moments and no owner, satisfies it too" — but this page, which the sibling calls its source for the locus, kept the over-credit. This is the `tenet-repairs-are-not-propagated-to-their-dependents` pattern. **Resolution**: the clause now reads that Tenet 1 "supplies the locus's irreducibility, not its existence: an abhidharma inventory of irreducible, ownerless suffering-moments satisfies the tenet too, so identifying the locus with the subject-side of experience is the Map's commitment rather than the tenet's", with a pointer to the sibling. §The Map's Reply (L92, "That is a commitment, not a discovery") and §Relation to Site Perspective ("What the tenet adds is that the locus is not a brain-built model") were already correctly scoped and are unchanged.

### Citation web-verify ledger (publisher of record)

References block unchanged since the 2026-08-27 full ledger (16 external DOIs, all `real-correct`). This pass re-verified the quotation-bearing entries against raw source text rather than re-running every DOI, and closed the one item the prior review left open. Superlative sweep (`find_superlative_claims`): empty.

- Coseru 2012 (Mind in Indian Buddhist Philosophy, SEP) — state: real-correct, re-verified. Raw HTML fetched; after stripping tags and collapsing whitespace all five quoted phrases grep verbatim ("reducible to the physical and psychological constituents", "nothing but a conventional designation that applies to the five aggregates", "do not endure for more than a moment", "precisely in order to avoid the metaphysical implications of the traditional notion of self", "overriding soteriological (or even therapeutic) concern"). Note for future passes: a plain `grep -F` on the unstripped HTML returns 0 for three of the five because of line breaks — strip first (`narrow-grep-zero-is-not-proof-of-absence`).
- Metzinger 2020 (Minimal phenomenal experience, *PhiMiSci* 1(I), 1–44) — state: real-correct, re-verified. DOI landing page `citation_pdf_url` resolved to `article/download/8960/8538` (the `download/46/26` path the prior review's PDF came from now 404s); `pdftotext` output greps all four quoted phrases verbatim ("necessary conditions for phenomenality", "MPE is non-egoic self-modelling", "atemporal, selfless, and not tied to an individual first-person perspective", "really is the content of a predictive model, namely, a Bayesian representation of tonic alertness"). Landing-page metadata: vol 1, issue I, pp. 1–44, matching the entry.
- Zahavi 2011 (The experiential self: Objections and clarifications, *Self, No Self?* pp. 56–78) — state: real-correct; **prior open item closed**. Crossref record carries no abstract and OUP/PhilPapers still 403, but the chapter abstract is mirrored at the MPG EVA literature base: the chapter "critically engages with various objections that have recently been raised against this view by Albahari and Dreyfus" and closes "with some reflections regarding the relation between self and diachronic unity." The article's gloss "his defence of it against no-self readings (2011) turns on exactly this thinness" was therefore right in substance but unspecific; it now names Albahari's and Dreyfus's objections. (Cited-author-stance note: the same Albahari the article borrows the two-tier structure from is one of the objectors Zahavi answers — consistent with the article's "disagree about almost everything else" framing.)
- All other entries (Parfit 1984; Siderits 1997, 2015, 2016; Hidalgo 2024; Zahavi 2005, 2014; Alweiss 2022; Albahari 2006, 2011; Strawson 2003, 2009, 2017; Metzinger 2003) — state: real-correct per the 2026-08-27 ledger; no inline or References change since, so not re-fetched.
- Southgate & Oquatre-cinq 2026-02-02; Southgate & Oquatre-sept 2026-01-14 — Map self-cites; not web-verified.

Inline ↔ References: unchanged and matched both ways. Result-direction leg: no empirical result is cited in a direction (the page's cites are doctrinal/positional); Hidalgo 2024's gloss (Buddhist reductionism survives objections Parfit's cannot) was abstract-verified last pass. Cited-author-stance leg: Strawson marked physicalist, Zahavi's minimal self marked phenomenological not dualist, Albahari's unconditioned-awareness claim marked not inherited, Metzinger marked rival — all present at L86 and L102.

### Medium Issues Found

- **"Writing from within Buddhism" (Albahari).** Albahari's *Analytical Buddhism* is an analytic reconstruction from Pāli sources, not a confessional work; "working from Buddhist sources" is the safer description. Changed.
- **Repetition paying for the critical fix.** Trimmed, all restatements of points made earlier in the same article: the ownership-void clause in §Dualism (already at L92); the "whose persons-in-dependence-on-the-aggregates the mainstream rejected" tail on the *Pudgalavādin* sentence; the §Reply restatement of the *vedanā* foothold (now an "explained above" pointer to §Sources); "nothing decisive has come in, and"; "is worth drawing out"; "and is registered as such"; "traces where the commitment enters" → "traces the entry point". Net ±0 words.
- Intra-corpus attributions re-checked where the body changed: [[the-ownerless-suffering-argument]] (wide/narrow scope of "anyone", Tenet 1 neutral on bearers, "Dualism supplies irreducibility, not existence") — accurate. Tenets page L121 ("What the indexical objection presupposes") still supports §No Many Worlds as written.

### Counterarguments Considered

- *Eliminativist / physicalist*: the locus is a user-illusion. Bedrock; booked in the prior Stability Notes; not re-flagged.
- *Nāgārjuna*: the momentary locus is empty. Bedrock; routed to the Mādhyamaka section of [[self-and-self-consciousness]]; not re-flagged. One sharpening this pass makes available to him: the article now concedes in its own voice that Tenet 1 is satisfied by an ownerless dharma inventory, so the existence of a bearer is carried entirely by the borrowed minimal-self structure. That is the honest position and the article says so.
- *Empiricist*: the first falsifier is near-unsatisfiable. Already in the article via the reporter-problem cross-reference.
- *Quantum skeptic / MWI defender*: nothing to engage; cascade isolation from Tenets 2 and 4 is intact.
- *Calibration check*: no possibility/probability slippage. The one calibration defect found was the reverse direction — a tenet credited with more than it supplies — and is fixed. The close remains "unrefuted and contested, not tested."

### Reasoning-mode classification (editor-internal)

Unchanged from 2026-08-27: Metzinger/MPE Mixed (Mode One on "non-egoic self-modelling", then Mode Three); Parfit Mode Three; Siderits/Hidalgo conventionalism Mode One with the near-terminological residue now scope-qualified via the sibling; Alweiss Mode Three; diachronic-welfare objector Mode Three with concession. Forbidden-label and "load-bearing" grep: zero hits.

## Optimistic Analysis Summary

### Strengths Preserved

- All seven strengths listed on 2026-08-27 (neutral four-premise statement; "a locus, not a career"; structure-not-metaphysics borrowing; valenced-MPE test; cascade isolation; three-state falsifier; costs paid in the open) are intact.
- The 2026-09 rescoping of the "close to terminological" verdict is a genuine improvement: the page now says exactly where a distinction idle within a metaphysics becomes live inside an argument.

### Enhancements Made

- Tenet 1 correctly scoped as supplying irreducibility, not existence, in the one place the page over-credited it; the bearer commitment now sits visibly on the Map rather than the tenet.
- Zahavi 2011 gloss made specific (Albahari and Dreyfus), closing the prior review's open verification item.
- Albahari's standpoint described accurately.

### Cross-links Added

- [[the-ownerless-suffering-argument]] — second body link, at the Tenet 1 scoping (the first, installed 2026-09-08, stays at the terminological verdict)
- `[explained above](#sources)` — internal anchor replacing a restatement

## Remaining Items

- **Diachronic mattering** remains the least-developed part of the reply (prudential-concern and time-bias literature unengaged). As before: an expansion opportunity, not a defect, and there is no length headroom — any treatment must trim first. No task minted.
- The article is at 3495/3500. It cannot absorb another cross-link install without a paid trim; a future cosmetic bump that pushes it over will trigger a condense task that the content does not need. Future editors should pay for insertions inline, as this pass did.

## Stability Notes

- Carry forward all 2026-08-27 stability notes: the physicalist user-illusion reading, Nāgārjuna's emptiness of the locus, Metzinger's for-no-one reading, the positive-characterisation debt, the unengaged diachronic layer, and the two remaining "marked as the Map's" hedges are not to be re-flagged as critical.
- **New**: "Tenet 1 is neutral on bearers; the locus's existence is a Map commitment" is now stated in §Implications and matches the sibling article and `tenets.md`. Do not re-flag the page for "resting the locus on a commitment" — that is the correct and now explicit position. Do re-flag any future edit that reintroduces "the subject-side Tenet 1 posits" or equivalent.
- Zahavi 2011's "thinness" gloss is now verified against the chapter abstract (via the MPG mirror); do not list it again as unverified unless the article's claim about the chapter changes.
