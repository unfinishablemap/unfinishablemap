---
title: "Deep Review - Hylomorphic Dualism and the Interaction Problem"
created: 2026-09-06
modified: 2026-09-06
human_modified: null
ai_modified: 2026-09-06T00:49:31+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-fable-5-1
ai_generated_date: 2026-09-06
last_curated: null
---

**Date**: 2026-09-06
**Article**: [[hylomorphic-dualism-and-the-interaction-problem|Hylomorphic Dualism and the Interaction Problem]]
**Previous review**: [[deep-review-2026-07-25-hylomorphic-dualism-and-the-interaction-problem|2026-07-25]] (and [[deep-review-2026-07-18-hylomorphic-dualism-and-the-interaction-problem|2026-07-18]], [[deep-review-2026-07-06-hylomorphic-dualism-and-the-interaction-problem|2026-07-06]])

## Verdict: dependency drift found under a converged article — two critical fixes, two medium

Fourth deep review. The article's body was byte-identical to the 07-25 no-op pass; the only change since was the 2026-08-04 population of the `topics:` frontmatter field (three bare slugs, all resolving). That cosmetic bump is what re-qualified the article, and the three prior reviews' self-directed lenses (citation ledger, calibration hedges, QM terminology) were exhausted. This pass therefore changed lens and asked what had moved *under* the article since 07-25, and re-derived each claim the article makes about another page from that page's current text. Both lenses returned defects that no amount of re-reading the article alone would have found.

Length 2282 → 2382 words (79% of the 3000 topics soft threshold; thresholds printed before editing: 3000 / 4000 / 6000). Below soft, so additions were permitted; every addition is a correction or an attribution, not filler.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Stranded dependent of the tenets-page scoping fix (Relation to Site Perspective, L75).** The article said the Map's interface is, "on the corridor reading, empirically indistinguishable from chance" — flat. `tenets/tenets.md` L75/L81 (commit `cb47816154`, 2026-08-27) and L107 (commit `71a78a577b`, 2026-09-04) now scope that claim to *unconditioned aggregate* tests and say a deviation *conditioned* on intention, task or subject remains live, after [[positions/quantum-interface#^mechanism-debt|P-Q3]] was re-rated `indirect` on 2026-08-24. The article calibrated against the old standard and so over-conceded relative to its own tenets page — the over-concession direction, which every "does it claim too much for the Map" lens ratifies as honesty. **Resolution**: the sentence now mirrors the tenets L107 form ("under any *unconditioned aggregate* test, though a deviation *conditioned* on intention, task or subject remains a live way of testing it") with a deep link to P-Q3. Read forward to the end of the section: no later sentence presupposed flat undetectability.
- **Seager's inference presented as Jaworski's concession (Structure hylomorphism, L47–49).** The article said Jaworski "*accepts* that the effects of hylomorphic substances are fully necessitated by prior physical causes … and denies only that necessitation is *sufficient for explanation*", and that "he argues" reasons- and mechanism-explanations pick out different causal factors. The NDPR review (William Seager, 2016-09-04; fetched raw with `curl` and grep-checked, not summarised) says something narrower and differently shaped: Jaworski concedes that structure "logically supervenes upon, or is necessitated by, the fundamental physical state of the world" (synchronic, constitutive) and that "higher-level behavior never violates lower-level physical laws" (book p. 280); it is *Seager* who infers "Non-violation and necessitation seem to imply that the world is physically causally closed", and Seager who hedges the causal pluralism as something Jaworski "appears to endorse" (quoting p. 281). The article had (a) converted Seager's closure inference into a diachronic claim Jaworski accepts about *effects* and *prior causes*, and (b) dropped Seager's hedge. **Resolution**: the paragraph now attributes the reading to Seager by name, states the concession in Seager's terms (supervenience/necessitation of structure; non-violation; denial that the base *determines*, i.e. also *explains*), carries Jaworski's verbatim "pick out causal factors of different sorts" (p. 281) as quoted by Seager, and the next paragraph names Seager as the source of both closure worries instead of an anonymous "Critics note". Reference #2 now names the reviewer and date.

### Medium Issues Found

- **Further Reading gloss claimed content its target does not carry.** The bullet for [[history-of-the-interaction-problem]] said the article shows "how the modern problem arose when Descartes displaced hylomorphism". That article opens at *The Cartesian Foundation*, contains zero occurrences of "hylomorph" or "Aristot", and mentions scholasticism once (the gravity analogy). A navigation surface was asserting an Aristotelian pre-history the target never treats. **Resolution**: gloss rewritten to what the target actually covers (Descartes, Elisabeth's 1643 challenge, four centuries of response).
- **Quoted phrase verified only against publisher catalogue copy.** The 07-06 ledger cleared "a basic ontological and explanatory principle" because it "matches the book's own OUP description" — which per the corpus's quote-fidelity discipline is a red flag, not a clearance. This pass tried to confirm body prose at four raw sources (PhilArchive → HTML challenge page; PhilPapers and PDC → 403; Google Books page → JS-only; Books API → 429 daily quota exhausted) and could not. **Resolution**: the phrase is de-quoted to a paraphrase (it faithfully states the view) and paired with a verbatim that *is* raw-verified: structure "operates as an irreducible ontological principle", which Seager quotes from the book in the NDPR text. Nothing was lost and the quotation surface is now grep-verifiable.
- Incidental: the paragraph pair used "dual-explananda" and "dual-explanandum" for the same move; the second occurrence was inside the rewritten sentence and is gone.

### Citation Web-Verify Ledger (§2.4)

References block unchanged in membership; #2 gained the reviewer's name and date. Trigger for a full re-verify was off (no References entries added or altered by any post-07-25 edit), so the 07-06 publisher-of-record ledger stands for the static tuples; this pass re-verified only what it touched.

- Aquinas, *ST* Ia q.75 a.2 — **real-correct** (07-06 ledger; both quotes verbatim at newadvent.org). Unchanged.
- Jaworski 2016, OUP — **real-correct** metadata (ISBN 9780198749561, 07-06). Quote-fidelity: **"a basic ontological and explanatory principle" — catalogue-copy match only, body prose unconfirmed after four raw attempts → de-quoted to paraphrase**; **"operates as an irreducible ontological principle" — verified verbatim** in Seager's raw NDPR text quoting the book; **"pick out causal factors of different sorts" (p. 281) — verified verbatim** in Seager's raw NDPR text quoting the book.
- Seager, NDPR 2016.09.04 (the review URL under #2) — **real-correct**; raw HTML fetched by `curl`, stripped, and grep-checked for every sentence the article now relies on ("logically supervenes upon, or is necessitated by, the fundamental physical state of the world"; "higher-level behavior never violates lower-level physical laws" (p. 280); "Non-violation and necessitation seem to imply that the world is physically causally closed"; "identify the hylomorphist's structured individuals with the necessitating base"; "appears to endorse a causal pluralism"). The JBTS review (Vecchio, 2017) independently gives the book's p. 3 "structure matters / structure makes a difference" formulation, consistent with the paraphrase kept.
- Feser 2011 (blog) — **real-correct**, fabricated-quote fix from 07-06 stands ("a single, complete substance"). Unchanged.
- Koons 2018, *Blackwell Companion to Substance Dualism*, pp. 377–393 — **real-correct** (07-06). Unchanged.
- Marmodoro 2013, *Philosophical Inquiry* 37(1-2): 5–22 — **real-correct** (07-06). Unchanged.
- Nussbaum & Putnam 1992; SEP "Form vs. Matter" — background bibliography supporting the "standard Aristotelian background" sentence; not cited inline, judged legitimate in 07-06 and not re-litigated.
- Self-cites #8, #9 — unchanged.
- `find_superlative_claims`: empty (no currency sweep needed).

### Reasoning-Mode Classification (§2.6) — editor-internal

- Engagement with the hylomorphist/critic exchange (Does Dissolution Actually Work?; Relation to Site Perspective): **Mode Three — framework-boundary marking**, unchanged and still honest ("This exchange is live and unresolved in the literature, and the Map does not get to declare it settled"; "it does not hold that hylomorphism has been shown to have lost").
- Engagement with Jaworski's structure hylomorphism: **Mode One via Seager** — the closure worry is derived from Jaworski's *own* commitments (necessitation plus non-violation), which is an internal-to-the-opponent argument; the pass did not change the mode, it attributed the argument to the reviewer who made it instead of voicing it as anonymous "critics". No editor-vocabulary label leakage in prose.

### Counterarguments Considered

- "Formal causation names the explanandum rather than supplying a mechanism" — still voiced in the article as the critic's live reply, handled honestly. No change.

## Optimistic Analysis Summary

### Strengths Preserved
- The three-way taxonomy (structure / Thomistic / emergent hylomorphism) mapped onto Tenets 2 and 3, untouched.
- The dialectical honesty of the Relation section — dissolution as the *rival's* move, "a cost to the Map, not a win", the fair-bet symmetry sentence — untouched; the scoping fix makes the price the Map "pays" more precise, not smaller.
- The substance-connection section's scoped borrowing (persisting subject from Thomistic subsistence while rejecting dissolution), untouched and re-derived against `where-the-substance-commitment-enters` (no commits since 07-25) and tenets L121 (still names the agency cluster's substance-leaning sub-reading). Consistent.

### Enhancements Made
- Seager named as the source of the structure-hylomorphism reading, with a page-cited verbatim from the book.
- The Further Reading gloss for the history article now describes the article a reader will actually find.

### Cross-links Added
- [[positions/quantum-interface#^mechanism-debt|P-Q3]] (deep link into the register at the sentence that needed it).

## Remaining Items

- **Sibling carriers of the same flat phrase** — the 2026-09-04 sweep closed the "under any aggregate(-statistics) test" *string* form only. A full-corpus survey this run (25 live files carry "indistinguishable from chance"; the ugrep context window silently hid tail-of-paragraph hits on the first pass, including this article's own) found three strong stranded dependents (`concepts/pragmatism` L44 — the pre-08-27 "presently conceivable instrument" wording attributed to the tenet; `tenets/background-commitments` L60 — a tenets-tier page citing the falsifiability status that no longer says this; `topics/epistemology-of-mechanism-at-the-consciousness-matter-interface` L123 — "Detectability follows *only* on minimum-outside-corridor readings", contradicting P-Q3 `indirect`), one medium (`apex/dualism-cartography` L105, "concede exactly that"), two judgement calls, and seven non-defects. Minted as one P3 refine-draft in `obsidian/workflow/todo.md` (inserted above `## Completed Tasks`) with both-tree line numbers and the tenets L107 transplant model. No open task covered any of the six.
- The idiom "the smallest deviation from standard physics" (L75) is shared with `topics/forward-in-time-conscious-selection` and `topics/arguments-against-materialism`; it sits in mild tension with tenets L81's "consistency claim" framing but is a corpus-wide phrasing, so it was not changed here alone. Not minted — three carriers, low stakes.

## Stability Notes

- Carried forward from 07-18/07-25: the dissolution-vs-location disagreement is a bedrock bet, stated as such — do NOT re-flag "hylomorphists reject the mechanistic premise"; Koons' "emergent individual" wording is defensible — do NOT re-litigate; "improper reduced-state mixture" is the deliberately chosen term — do NOT revert.
- **The correct re-review trigger for this article is movement in its dependencies, not its own `ai_modified`**: `tenets/tenets.md` L75/L81/L107, P-Q2/P-Q3 in `positions/quantum-interface`, `apex/post-decoherence-selection-programme`, and `concepts/where-the-substance-commitment-enters`. Three consecutive no-op passes were not evidence the article was sound; they were evidence the self-directed lenses were spent.
- "load-bearing" (L77) and the "This is not by itself an objection; … But it marks…" construct (L69) are pre-existing; the style guide says existing uses need not be swept. Do NOT re-flag.
- The Jaworski blurb phrase is now a paraphrase by design. If a future pass obtains the book's Introduction and confirms "Hylomorphism claims that structure is a basic ontological and explanatory principle" as body prose, re-quoting is legitimate; until then, do NOT restore the quotation marks on catalogue-copy grounds.
