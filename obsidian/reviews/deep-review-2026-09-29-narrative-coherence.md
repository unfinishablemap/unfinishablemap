---
title: "Deep Review - Narrative Coherence"
created: 2026-09-29
modified: 2026-09-29
human_modified:
ai_modified: 2026-09-29T02:55:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-fable-5-1
ai_generated_date: 2026-09-29
last_curated:
---

**Date**: 2026-09-29
**Article**: [[narrative-coherence|Narrative Coherence]]
**Previous review**: [[deep-review-2026-07-13-narrative-coherence|2026-07-13]] (also 2026-06-01, 2026-04-28, 2026-03-23, 2026-02-20)

## Scope

Sixth review. The only change since 2026-07-13 is the 2026-09-28 refine-draft (commit 5a31bb0246), which added the "Absence Without Pathology" section, two Strawson references, one verbatim quote, and re-scoped three overclaims (L35, L73, L81). This pass reviewed that delta in full, checked the new material for consistency with the untouched sections, and web-verified the two new citations plus the quote at the raw source. The eight references publisher-verified on 2026-07-13 were not re-verified (no divergence; stability note honoured). All prior stability notes were honoured.

## Citation Audit — Publisher-of-Record Web-Verify Ledger

- Strawson 2004 ("Against Narrativity") — **state: real-correct**. Crossref record for DOI 10.1111/j.1467-9329.2004.00264.x: *Ratio* 17(4), 428–452, issued 2004-11-17. Matches the References entry exactly. Wiley landing page returned 403 to the fetcher; Crossref is the publisher-deposited record. Corpus family check: [[diachronic-agency-and-personal-narrative]] L161, [[narrative-void]] L124 and the 2026-02-25 voids research note all carry the identical tuple — no family divergence.
- Strawson 2004 verbatim quote "I have absolutely no sense of my life as a narrative with form" — **grep-verified in the raw source** (PDF text, §"Episodic and Diachronic"): full sentence reads "And yet I have absolutely no sense of my life as a narrative with form, or indeed as a narrative without form. Absolutely none." The article's quote is a verbatim clause-boundary truncation; no fix required. The same truncated form is used in the two sibling articles; consistent and faithful.
- Strawson 2004, "counts himself among the latter" — **dropped qualifier restored**. Raw source: "since I find myself to be relatively Episodic, I'll use myself as an example." The article (and its two siblings) drop "relatively", which Strawson uses because he treats the Episodic/Diachronic distinction as a spectrum. Fixed here by quoting "relatively Episodic" in his own words. The siblings carry the same drop — see Remaining Items.
- Strawson 2004, normative prong ("denies that a life must be narrated to go well") — **result-direction confirmed**: raw source names "the normative, ethical Narrativity thesis" as the second target and argues against it; the article's characterisation is faithful.
- Strawson 2004, cited-author stance — Strawson is not a dualist and not a substantial-self theorist; the article correctly presents the engagement as concession plus framework-boundary disagreement and does not enlist him for the Map's conclusion.
- Strawson 2009 (*Selves: An Essay in Revisionary Metaphysics*) — **state: real-correct**. Crossref record for DOI 10.1093/acprof:oso/9780198250067.001.0001: Oxford University Press, issued 2009-07-30. Body use ("thin and short-lived" subjects) matches the characterisation at [[self-and-self-consciousness]] L122, which cites the same work. Seven other corpus articles cite the identical tuple.
- Ricoeur 1992, Schechtman 1996, MacIntyre 1981, Kahneman & Tversky 1973, Tversky & Kahneman 1983, Tulving 2002, Tversky & Kahneman 1971, Velleman 2005 — **not re-verified**; publisher-verified 2026-07-13 and 2026-06-01, References entries unchanged since (diff-confirmed).
- Superlative sweep (`find_superlative_claims`): empty. No currency leg required.
- Inline ↔ References cross-reference: all ten References entries are cited in the body; all inline cites have an entry. No orphans.

## Pessimistic Analysis Summary

### Critical Issues Found
- **Internal contradiction introduced by the 09-28 refine** — the Bidirectional Interaction paragraph now concedes that "a purely physical account—an interpreter module revises the story and the revised story shapes subsequent action—fits the same data", while the Occam paragraph still asserted that "the simpler account (confabulation) cannot capture the forward-looking, project-sustaining, revisable structure of lived narrative coherence." A revising interpreter whose story shapes future action captures exactly that structure. **Resolution**: Occam paragraph rewritten. It now separates narrow confabulation (post hoc explanation of individual actions, which does not capture the forward-looking structure) from the interpreter-module deflation (which does), declines to claim the latter is refuted, and locates the tenet's work correctly: the razor cannot settle whether the story is told *to* anyone, because that is exactly what third-person data leave open. Added [[confabulation-void|confabulation]] cross-link.
- **Dropped qualifier** — "relatively Episodic" (see ledger). Restored in the article's own voice by quoting Strawson's words.

### Medium Issues Found
- Intro overclaim surviving the 09-28 re-scope: "it makes [[moral-responsibility]] over time intelligible" implies responsibility over time is unintelligible without narrative coherence, which the new Strawson section (and Strawson's own §"Can Episodics be properly moral beings?") denies. **Fixed**: "helps make".
- Self-undercutting sentence in the new section: "plays a smaller part … than the earlier sections might suggest" told the reader the article's own earlier sections overstate. Since the 09-28 refine already re-scoped the intro, the hedge was stale. **Fixed**: now states the bounded role directly.
- Navigation surface carrying the pre-refine claim: Further Reading labelled the diachronic-agency link "How narrative coherence grounds extended agency" and the moral-responsibility link "How coherence enables responsibility across time" — both stronger than the body now says. **Fixed**: "one route to extended agency, alongside non-narrative routes"; "supports responsibility across time".

### Counterarguments Considered
- Eliminative materialist / hard-nosed physicalist: the interpreter-module account explains the data without a subject. Now conceded explicitly in two places (Bidirectional, Occam) and marked as undetermined by the data rather than refuted — Mode Three, honestly declared.
- Buddhist no-self: attachment to narrative as suffering. Prior stability note; the 09-28 reformulation ("the narrative is *someone's*" rather than "someone must be doing the constructing") already softened the reply to the defensible form. Not re-flagged.
- Empiricist: the breakdown cases do not establish causal efficacy. Already conceded at L73 in the 09-28 refine; verified the concession survives and is consistent with the Bidirectional paragraph.
- Strawson (episodic lives): fully conceded; framework-boundary residue (transience thesis) marked honestly.

### Reasoning-mode classification (editor-internal)
- Engagement with Parfit: Mode Two — the article claims Parfit's element-cataloguing framework lacks the resources for a relational property; it does not claim to refute reductionism.
- Engagement with Velleman / constructionism: Mixed — concedes the interpreter-module picture, then marks the residue (a subject for whom coherence is lived) as the Map's commitment, not a refutation.
- Engagement with Strawson: Mode Three, explicitly declared in the prose ("a disagreement at the framework boundary … nothing here refutes the transience thesis from inside Strawson's own commitments").
- Label leakage check: none of the forbidden editor-vocabulary terms appear in the article.

## Optimistic Analysis Summary

### Strengths Preserved
- The clinical triad (depression / dissociation / amnesia) with the temporal-unity vs narrative-coherence distinction — untouched.
- The 09-28 reformulation of the constructionist reply ("the narrative is *someone's*" … "pattern without perspective does not supply one") — untouched; this is the article's best passage and the Hardline Empiricist persona would praise it as the tenet-coherent-not-evidence-elevating pattern done right.
- The Strawson section's concession ("The concession costs the Map less than it might appear") — preserved; only the stale self-hedge was tightened.

### Enhancements Made
- Occam paragraph now does real tenet work (razor cannot adjudicate under missing knowledge) instead of asserting a claim the article elsewhere concedes.
- Strawson's own qualifier restored.

### Cross-links Added
- [[confabulation-void]]

## Length Check
2352 → 2422 words (+70). 97% of the 2500 concepts soft threshold; below soft, so normal mode, but the article is now within ~80 words of the threshold — future passes should operate length-neutrally.

## Remaining Items
- [[diachronic-agency-and-personal-narrative]] L76 and [[narrative-void]] L82 carry the same dropped "relatively" qualifier on Strawson's self-description. Low severity (the truncated quote itself is verbatim). Not fixed here — out of this review's file scope; left for those articles' next passes rather than minted as a task.

## Stability Notes

All prior stability notes remain in effect (2026-07-13 ledger: eight references publisher-verified; Velleman 2005/2006 dual-route citation deliberate; MacIntyre "narrative unity" deliberately unquoted; T&K 1983 author order verified). New notes:
- **Strawson 2004 and 2009 publisher-verified as of 2026-09-29**; the "absolutely no sense of my life as a narrative with form" quote is grep-verified verbatim in the raw source as a clause-boundary truncation of a longer sentence. Do not add an ellipsis or "correct" it — the truncation is faithful. Do not extend it in this article alone without updating the two siblings.
- **The Occam paragraph deliberately concedes the interpreter-module deflation** and rests the tenet's work on underdetermination, not on confabulation failing to capture forward-looking structure. Do not restore the "cannot capture" claim — it contradicted the Bidirectional paragraph's concession.
- **Narrative coherence is deliberately scoped as "one route" / "helps make" / "bounded part"** throughout (intro, Absence section, Further Reading). Reviewers reading the intro as under-selling the concept should check the Strawson section before re-strengthening it.
- Strawson's transience thesis (2009) is a bedrock disagreement at the framework boundary and is declared as such in the prose. Do not re-flag as an unanswered counterargument.
