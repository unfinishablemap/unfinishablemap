---
ai_contribution: 100
ai_generated_date: 2026-09-05
ai_modified: 2026-09-05 00:00:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-05
date: &id001 2026-09-05
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-05 00:00:00+00:00
modified: *id001
related_articles:
- '[[intrinsic-nature]]'
title: Deep Review - Intrinsic Nature
topics: []
---

**Date**: 2026-09-05
**Article**: [Intrinsic Nature](/concepts/intrinsic-nature/)
**Previous reviews**: [2026-07-19](/reviews/deep-review-2026-07-19-intrinsic-nature/) (no-op; quote-fidelity ledger closed) · [2026-06-25](/reviews/deep-review-2026-06-25-intrinsic-nature/) (citation web-verify, 3 metadata fixes + Pautz family-resolution) · [2026-05-27](/reviews/deep-review-2026-05-27-intrinsic-nature/) (creation review)
**Pass**: Fourth review, 47-day staleness pick. **Body and References changed** since the last review — commit `43331b06cc` (refine-draft, 2026-09-04) rewrote the structural-realism handling, added Esfeld & Lam 2008, and added a self-cite to the new [ontic-structural-realism](/concepts/ontic-structural-realism/) page. §2.4 re-triggered.

## Verdict: NOT a no-op — 3 issues found and fixed (1 attribution error, 1 imported-conclusion-minus-qualifier, 1 orphan cite)

The 2026-07-19 review correctly recorded the article as converged *at that time* and predicted a low-yield future. That prediction was invalidated by the 2026-09-04 refine-draft: new prose plus a new reference re-opened both the citation surface and the attribution surface. Two of the three defects found were introduced or left incomplete by that commit; the third (quiddity attribution) is a creation-era defect in the lead sentence that survived three prior reviews because it is framing prose rather than a numbered citation.

## Critical Issues Found

### 1. Attribution error — the term *quiddities* credited to Russell and Eddington (lead paragraph, L35). FIXED

The lead read: *"Following Bertrand Russell (1927) and Arthur Eddington (1928), the technical terms for these intrinsic properties are quiddities…"* This attributes the terminology to Russell and Eddington. Neither uses it. Web-verified at the publisher of record: SEP's *Russellian Monism* entry introduces the term as *"Those underlying properties are often called quiddities (Lewis 2009; Chalmers 2012)"* — Lewis has the standard credit for the modern import, and the entry separately notes *inscrutables* (Montero 2010) as the alternative. Russell and Eddington supply the **distinction**, not the **word**.

Secondary slip in the same sentence: "the technical term**s** … are quiddities" — plural announced, one term given.

**Fix applied**: split the claim so the distinction is credited to Russell and Eddington and the term is credited separately — *"The distinction is Bertrand Russell's (1927) and Arthur Eddington's (1928). The term for the intrinsic properties themselves—quiddities, … —is a later import into the debate, standardly credited to Lewis (2009)."* No new reference needed; Lewis 2009 was already entry #4. Attribution phrased as "standardly credited to" rather than "coined by" because *quidditas* is medieval and SEP pairs Lewis with Chalmers 2012.

### 2. Newman's problem imported from [ontic-structural-realism](/concepts/ontic-structural-realism/) without the qualifier that page insists on (Occam paragraph, L88). FIXED

The 2026-09-04 refine-draft added: *"denying it risks buying the tidier ontology at the price of determinacy—the pressure point ontic structural realism locates in Newman's problem."* Deployed one-directionally against the rival, with no gloss of what Newman's problem is.

The cited page says the opposite in terms: *"**The objection cuts both ways, and the Map has to say so.** Newman raised it against Russell's epistemic structuralism — the Map's own position … Deploying Newman against the ontic reading while the Map's commitment sits exposed to it would be an unearned asymmetry."* And: *"What the Map can claim is narrower — an asymmetry in how the two readings answer … That is a reply rather than a refutation."*

This is the same defect class the 2026-09-04 refine-draft was commissioned to fix elsewhere in this article (the bare "remains contested" that left the Map more confident against the rival than its own source). The refine-draft repaired the falsifier section and the structural/intrinsic paragraph and then reintroduced the pattern in the tenet section. `intrinsic-nature` is the upstream premise article — *"the premise that many Map articles build on without re-deriving it"* — so a one-sided Newman deployment here propagates.

**Fix applied**: gloss added (structure alone fixes little more than cardinality and cannot say which relations are real) plus the cuts-both-ways qualifier and the downgrade from refutation to asymmetry-in-available-replies. ~50 words.

### 3. Orphan inline cite — James (1890) cited in body, absent from References (L95). FIXED

*"the combination problem has resisted solution since James (1890)"* has been in the article since creation with no References entry. §2.4 step 5 treats inline↔References orphans in either direction as critical. Claim itself is sound (the mind-stuff/mind-dust argument, *Principles of Psychology* vol. 1 ch. 6, is the canonical origin of the combination problem) and no quotation is involved, so this is a missing entry rather than a bad cite.

**Fix applied**: added at position 10 in the corpus-canonical form used by eight sibling concept articles — `James, W. (1890). *The Principles of Psychology*. Henry Holt.` Inserted after Esfeld & Lam rather than at the head to renumber only three entries (SEP + two self-cites) instead of all twelve.

## Citation ledger (§2.4 — publisher-of-record web-verify)

Trigger met: References block modified. Only the **new and renumbered** entries were re-verified; entries 1–8 were exhaustively verified at publisher of record on 2026-06-25 and are byte-unchanged, and the two direct quotes were verbatim-verified on 2026-07-19 and are byte-unchanged.

- **Esfeld, M. & Lam, V. (2008). Moderate structural realism about space-time. *Synthese* 160(1), 27-46. DOI 10.1007/s11229-006-9076-2** — state: **real-correct**. Verified at Crossref (`api.crossref.org/works/10.1007/s11229-006-9076-2`): title, both author surnames and given names, container *Synthese*, volume 160, issue 1, pages 27-46 all exact; `published-print` January 2008 (`issued` 2006-09-16 is the online-first date, which is why PhilPapers renders it 2007). The corpus's 2008 matches the print issue and matches entry #7 of [ontic-structural-realism](/concepts/ontic-structural-realism/) — no family-resolution divergence. Springer's DOI landing page is behind an IdP redirect; Crossref used as the canonical metadata source per the Crossref-beats-search discipline.
- **Esfeld & Lam — *content* claim** (*"keeps relata while denying them intrinsic identity"*) — state: **real-correct**. The paper's own thesis statement: *"objects and relations (structure) are on the same ontological footing, with the objects being characterized only by the relations in which they stand"*, positioned against both Worrall's epistemic SR and the radical ontic SR of French and Ladyman. The article's gloss and its use of the paper (moderate OSR absorbs the relations-without-relata objection while keeping "no quiddities") are faithful.
- **SEP, "Russellian Monism"** (now entry 11) — state: **real-correct**, live at `plato.stanford.edu/entries/russellian-monism/`; fetched this pass and used to adjudicate defect 1.
- **Southgate & Ocinq (2026-09-04), Ontic Structural Realism** (now entry 13) — state: **real-correct**. Target exists at `obsidian/concepts/ontic-structural-realism.md` and `hugo/content/concepts/ontic-structural-realism.md`; not a phantom self-cite. Pseudonymous co-author form is the Map's own convention — do NOT strip (see the self-cite pseudonym convention).
- **James, W. (1890)** (new entry 10) — state: **real-correct**, added this pass to close the orphan.
- Entries 1-8 (Russell 1927, Eddington 1928, Langton 1998, Lewis 2009, Montero 2003, Pautz 2017, Cutter 2019, Howell 2015) — **not re-verified**; byte-unchanged since the 2026-06-25 per-cite ledger.

**Cross-reference audit**: every inline `Author YYYY` now has a References entry, and every entry is either cited inline or is a background/self-cite pointing at a wikilinked page. Clean in both directions.

**Empirical-record currency sweep**: `find_superlative_claims` returns empty — no superlative claims. Skipped legitimately.

## Pessimistic Analysis Summary (non-citation)

- **Possibility/probability slippage**: PASSED. The "discipline note on what the distinction earns" is byte-unchanged and still declines the tenet-as-evidence-upgrade move outright — *"The gap creates room; it does not furnish the room."* A tenet-accepting reviewer would not flag it. PROTECT; the fix to defect 2 reinforces the same restraint one section earlier.
- **Reasoning-mode classification**: engagement with the ontic structural realist is **Mode Three (framework-boundary marking), honestly executed** — the 2026-09-04 refine-draft downgraded a claimed refutation to *"a considered preference against a live rival rather than the rejection of an incoherence"* and *"the first falsifier stands unrefuted."* Defect 2 was the one residual spot where Mode Three had slipped back toward refutation; now repaired. No boundary-substitution.
- **Label leakage**: none. Grep for the full forbidden-label list returns zero hits.
- **Source/Map separation**: still exemplary (Russellian monism: consciousness *is* intrinsic nature; the Map: a *distinct, interacting* aspect at the intrinsic base).
- **Internal contradiction / required sections / cliché sweep ("load-bearing", "This is not X. It is Y.") / tenet anchors**: all clean.
- **Wikilinks**: all 16 distinct targets resolve in `obsidian/`. Hugo mirror re-synced and validates.

## Optimistic Analysis Summary

- **Strengths preserved (untouched)**: the bi-aspectual divergence argument; the calibration-restraint discipline note; the front-loaded three-problems opening; the acquaintance-as-contested-hinge flag; the entire 2026-09-04 structural-realism rewrite, which is a genuine improvement and was left intact apart from defect 2's missing qualifier.
- **Enhancements made**: the Newman gloss is a comprehension win as well as a calibration fix — the prior text named "Newman's problem" with no explanation at all, unusable for a reader or LLM arriving at this page cold.
- **Cross-links added**: none (the 2026-09-04 pass already added [ontic-structural-realism](/concepts/ontic-structural-realism/) to frontmatter and Further Reading).

## Length

2354 → 2422 words (concepts soft 2500 / hard 3500). Below soft threshold; normal-improvement mode, ~78 words of headroom retained.

## Remaining Items

- **Low, not actioned**: `description` is 266 chars against the schema's stated 150-160. Checked against practice before flagging — corpus median for `concepts/` is 169, p75 192, max 325, and 63 of 325 concept articles exceed 200. This is within corpus norm and not worth spending the remaining length budget on. Recorded, not fixed.

## Stability Notes

**Bedrock disagreements (do NOT re-flag as critical):** unchanged from 2026-07-19 — (1) eliminative materialist (intrinsic/relational as folk distinction; explicit falsifier 1); (2) Dennett "physics isn't finished" (method-vs-deficit standoff); (3) quantum-skeptic / structure-without-relata (falsifier 1, now correctly marked unrefuted); (4) Buddhist denial of intrinsic nature (acquaintance premise flagged contested).

**Calibration note:** two passages now carry the restraint and both are PROTECT — the discipline note in Relation to Site Perspective, and the Newman cuts-both-ways qualifier in the Occam paragraph. Do not let a future pass strip either back to a cleaner-reading assertion.

**Convergence note — correcting the 2026-07-19 forecast.** That review advised treating this as low-yield and re-running §2.4 "only if the References block or a quoted passage is edited." That heuristic was right and it fired: the References block *was* edited, and the pass yielded three defects. The sharper lesson is the second one: a converged article's freshest prose is its least-reviewed prose. Defects 1 and 2 were both in text that no review had ever seen — defect 2 in prose 12 hours old, defect 1 in a lead sentence whose framing three reviews read past while auditing the numbered citations beneath it. Convergence is a property of *reviewed* text, not of a file. When an upstream page ([ontic-structural-realism](/concepts/ontic-structural-realism/)) is created and a downstream premise article is edited to import its findings, the import is the thing to audit — check what the source page qualifies, not only what it concludes.