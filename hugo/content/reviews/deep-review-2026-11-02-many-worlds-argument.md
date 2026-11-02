---
ai_contribution: 100
ai_generated_date: 2026-11-02
ai_modified: 2026-11-02 18:49:22+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-02
date: &id001 2026-11-02
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-02 18:49:22+00:00
modified: *id001
related_articles:
- '[[arguments/many-worlds-argument]]'
- '[[deep-review-2026-07-19-many-worlds-argument]]'
- '[[concepts/diverging-worlds-everettianism]]'
title: Deep Review - The Map's Case for One-World Actuality
topics: []
---

**Date**: 2026-11-02
**Article**: [The Map's Case for One-World Actuality](/arguments/many-worlds-argument/)
**Previous review**: [2026-07-19](/reviews/deep-review-2026-07-19-many-worlds-argument/) (7th review)

This is the 8th deep review. The skill's selector picked it (score 76; last reviewed 106 days ago). The page was not edited today, and no open P1 or P2 task names it. Three open entries do: the blocked NEEDS-HUMAN length decision, the P3 Tallis repoint (this page is a secondary file), and the P3 `arguments/arguments` description task. The page is over its hard limit and under the NEEDS-HUMAN "do not auto-condense" bar, so this pass was **length-neutral**: **3872 → 3871**. By analyze_length the split is prose ~3374 and Further Reading + References ~498. The prose alone is under the 3500 hard limit, so the breach is reference apparatus.

## A Discrepancy in the 07-19 Review

The 07-19 archive reports a condensation of 3695 → 3498. It also says the `### The Decision-Theoretic Response` subsection was removed and lists a set of dedups. **None of that is in the file.** Commit `9f53bd9331` changed only `last_deep_review`, and the subsection is still present (`git log -S` shows it has stood since February). So the open NEEDS-HUMAN length entry is accurate, and the 07-19 claim that the length was resolved is false. The 07-19 citation ledger is also unreliable: it rated Everett 1957 "real-correct" when the title and issue were wrong, and it never checked how Tappenden and Mandolesi were described. Every citation was re-verified this pass.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Tappenden misattribution (L77)**: the article said Tappenden (2008, 2017) "extends the picture with a self-locating-beliefs account: pre-measurement uncertainty is uncertainty about *which* post-measurement observer I will be". That is the Saunders–Wallace position. Tappenden 2008 is a *reply* to it: per the Crossref/OpenAlex abstract, "I argue that a central assumption of this seductive idea is questionable". Tappenden 2017 (arXiv 1702.02140 abstract) treats self-location uncertainty for "a post-measurement, pre-observation subject" through a mind-body account that "leads to a fission, rather than divergence, interpretation". **Fixed**: the paragraph now says Tappenden questions the pre-branching case (2008) and turns to post-measurement credences grounded in his mind-body account (2017). The Map's reply is kept and is now marked as the Map's: the centred subject comes from that account, not from branching alone.
- **Mandolesi attached to the wrong derivation (L79)**: the article had "Mandolesi (2018) formalises the circularity" in Vaidman's caring-measure derivation. Mandolesi analyses *Wallace's* decision-theoretic proof. The arXiv 1504.05259 abstract says "Some problems have been identified, and we suggest possible corrections". The paper does not formalise a circularity, and it does not discuss Vaidman. **Fixed**: the clause was removed from the Vaidman paragraph and moved to the Decision-Theoretic Response as "Mandolesi (2018) finds formal problems in Wallace's proof". The reference title was missing its subtitle; it now reads "…: Formal Aspects" (Crossref `10.1007/s10701-018-0179-7`).
- **Everett 1957 metadata**: corrected to `"'Relative State' Formulation of Quantum Mechanics"`, *Rev. Mod. Phys.* 29(3), 454–462 (Crossref `10.1103/RevModPhys.29.454`). This discharges the NEEDS-HUMAN entry's 2026-08-25 rider. It is a zero-word fix.
- **Tallis cited to the wrong work**: the body wording "illusions presuppose experience" comes from the 2024 *Philosophy Now* article, not from *Aping Mankind* (2011). This is the same finding as [reviews/deep-review-2026-11-01-experiential-alignment.md](/reviews/deep-review-2026-11-01-experiential-alignment/) L54, and the open P3 Tallis task lists this page. **Fixed**: the reference was repointed to Tallis (2024), and "(2024)" was added inline.
- **Diverging-worlds concession missing (calibration and cross-page consistency)**: on 2026-10-05, `tenets/background-commitments` L52 and `apex/one-world-wager` L54 conceded that the fission-shaped indexical argument does not reach diverging-worlds Everettianism. `concepts/diverging-worlds-everettianism` concedes the same. The apex points readers to "the arguments article", yet this page stated the fission premise without qualification. Its Conclusion called the case "decisive against branch-egalitarian Everettianism", and the diverging reading is branch-egalitarian. A reviewer who accepts the tenets would still flag that. **Fixed**: L61 now scopes the metaphysical problem to "this fission picture" and installs the concession, citing Saunders 2010 (arXiv 1609.04720 has "no good reason to think EQM is really a theory of overlapping worlds") and Wilson 2020. It names what survives at the boundary: haecceity, and the posit that unchosen outcomes occur nowhere. The Conclusion now reads "read as fission". The three later "decisive against branch-egalitarian…" loci (table, Cumulative Case, Relation-to-Site) now read "fission readings". The redundant L59 restatement of the fission premise was removed; L57 already states it.
- **Dropped qualifier**: the 07-11 compression turned "not *merely* epistemic" into "not epistemic". On the diverging reading the question *is* epistemic. "Merely" is restored.

### Medium Issues Found

- **Non-deflationary dependency not propagated**: since 06-03, `tenets.md` has said the indexical objection "is as strong as the non-deflationary 'I' it presupposes, and no stronger". **Fixed** in the Parfit section's closing conditional. The same edit removed "cannot accommodate the apparent fact", which belongs to the "cannot accommodate" family the 09-07 sweep scoped.
- **Vaidman terminology**: "caring measure" is Greaves's term. Vaidman 2014 (arXiv PDF, grep) uses "measure of existence" ×13 and justifies betting "in proportion to the measure of existence" by symmetry. **Fixed** at zero words. The circularity question is now stated precisely: does equating that measure with squared amplitude presuppose the Born rule?
- **"…that many-worlds cannot provide" (L109)**: scoped to "that branching does not supply".
- **Argument 4 overclaim**: "No theory that fragments subjects across branches explains the unity of experience" contradicted the article's own L73 (branch-local singularity, not refuted on its own terms) and L87 (Many-Minds preserves unity along each trajectory). The rhetorical question before it repeated Argument 1; the 07-19 review flagged that dedup but never applied it. **Fixed**: the passage now points to Premise 3's question of unity within a branch.
- **Illusionist engagement**: "The *seeming* … is itself phenomenal" asserted the premise illusionists deny. `arguments/functionalism-argument` L175 concedes that the regress, "taken bare", proves nothing. **Fixed**: the premise is now a conditional, "as the Map holds and illusionists deny".
- **Contemplative-convergence overclaim**: "favors genuine singularity of awareness, not confabulated impression" read metaphysics off phenomenology. `concepts/witness-consciousness` L60 says traditions converge on the phenomenology "while diverging on its metaphysical status", and anattā is the counterexample. **Fixed**: the sentence now says what the convergence covers and what it leaves open.
- **Orphan reference**: Barrett (1999) was never cited inline. Removed.
- **Style**: three uses of "load-bearing" were removed (L129, L149, L171). The L149 sentence was redundant with L155. The banned pair "tenet is not arbitrary. It follows…" (Relation to Site) now reads "tenet follows…".

### Counterarguments Considered

- **Deutsch / diverging worlds**: conceded. The article now names it as a framework boundary.
- **Dennett, Churchland**: the illusionist and physicalist challenges remain bedrock (07-19 stability notes). This pass corrected only how the article presents its own premise.
- **Nagarjuna**: the deflationary route is now stated as the condition under which the objection loses its grip.
- **Tegmark**: Argument 3's einselection caveat is unchanged and remains correct.
- **Popper**: the "What Would Challenge This View?" list is unchanged.

### Reasoning-Mode Classification (editor-internal)

- **Tappenden**: Mode Two, recast honestly. The subject is supplied by an extra mind-body account, and the Map presses that dependence without claiming Tappenden concedes it.
- **Diverging worlds**: Mode Three, an explicit boundary.
- **Illusionism**: Mixed. Tallis's regress is supplied as intuition, and the boundary is now declared.
- Grep finds no label leakage.

## Citation Web-Verify Ledger (§2.4)

- Albert & Loewer 1988, *Synthese* 77(2) 195–213 — real-correct (Crossref `10.1007/BF00869434`)
- Carroll 2019, *Something Deeply Hidden*, Dutton — real-correct (Open Library)
- Everett 1957 — real-wrong-metadata (title lacked the scare quotes and the issue was missing; now `"'Relative State' Formulation…"`, 29(3))
- Kent 2010, "One World Versus Many", in *Many Worlds?* — real-correct, short title (Crossref `10.1093/acprof:oso/9780199560561.003.0012`)
- List 2023, *Noûs* 57(2) 316–340 — real-correct (Crossref; published online 2022)
- Lockwood 1989, *Mind, Brain and the Quantum*, Blackwell — real-correct (Open Library)
- Lockwood 1996, *BJPS* 47(2) 159–188 — real-correct (Crossref `10.1093/bjps/47.2.159`)
- Mandolesi 2018, *Found. Phys.* 48(7) 751–782 — real-wrong-metadata (subtitle "Formal Aspects" added) **and** misattached (moved from Vaidman to Wallace's proof; "formalises the circularity" overstated the abstract)
- Saunders 2010, "Chance in the Everett Interpretation", *Many Worlds?* pp. 181–205 — real-correct (Crossref `…003.0008`); divergence thesis grep-verified in arXiv 1609.04720
- Saunders, Barrett, Kent & Wallace (eds.) 2010, *Many Worlds?*, OUP — real-correct
- Sebens & Carroll 2018, *BJPS* 69(1) 25–74 — real-correct (Crossref `10.1093/bjps/axw004`)
- Tallis 2011, *Aping Mankind* — real, but the wrong work for the wording; **replaced**
- Tallis 2024, "The Illusion of Illusionism", *Philosophy Now* 161 — real-correct. The raw publisher HTML was fetched with `curl` and stripped two ways. Tag-to-nothing: "all illusions presuppose experience" ×1. Tag-to-space: same ×1, and "misrepresentation presupposes presentation" 0, reproducing the known split-word artifact. JSON-LD datePublished is 2024-04-08. Page range omitted, per the P3 task.
- Tappenden 2008, *BJPS* 59(3) 307–314 — real-correct metadata (Crossref `10.1093/bjps/axn019`), **body misdescribed it; fixed**
- Tappenden 2017, *SHPMP* 57, 8–16 — real-correct metadata (Crossref `10.1016/j.shpsb.2017.01.007`), **body misdescribed it; fixed**
- Vaidman 1998, *Int. Stud. Phil. Sci.* 12(3) 245–261 — real-correct (Crossref)
- Vaidman 2014, *Quantum Stud.* 1(1-2) 5–38 — real-correct (Crossref); the term "caring measure" was corrected to "measure of existence"
- Wallace 2012, *The Emergent Multiverse*, OUP — real-correct (Crossref book DOI)
- Whitehead 1929, *Process and Reality*, Macmillan — real-correct
- Wilson 2020, *The Nature of Contingency*, OUP — real-correct (Crossref `10.1093/oso/9780198846215.001.0001`)
- Barrett 1999 — orphan, removed

**Inline ↔ References**: after the Barrett removal, every reference has an inline cite. Albert, Price, DeWitt and Deutsch are named at L105 without their own entries. Price 2010 and Albert's probability chapter sit inside the cited *Many Worlds?* volume; see Remaining Items. **Result direction**: no empirical results are cited. **Cited-author stance**: every Everettian named is presented as an opponent. Tallis is an anti-physicalist critic of illusionism and is not presented as a dualist. Mandolesi is a critic of the proof only. Whitehead is used in the Map's own application. **Superlative helper**: empty. **Map-internal quotations**: none in the body.

## Optimistic Analysis Summary

### Strengths Preserved
- The seven-engagement Branch-Relative Identity Programme, the List paragraph, and the symmetric-burden paragraph (07-16) are untouched.
- Argument 3's einselection self-application and the three-not-four argument count are untouched.
- The Parfit convergence (now with its condition stated) and the Whiteheadian exclusion passage are kept.

### Enhancements Made
- The diverging-worlds concession brings this page into line with the apex, the background-commitments page and the concept page.
- The Tappenden paragraph now carries a sharper and accurate point: his account needs a separate mind-body theory to supply the subject.

### Cross-links Added
- [diverging-worlds-everettianism](/concepts/diverging-worlds-everettianism/) (body and `related_articles`)

## Remaining Items

- `tenets.md` L117 and [arguments/arguments.md](/arguments/) L52 still say "decisive against branch-egalitarian readings/versions" without the fission scoping now used here. Per [reviews/optimistic-2026-10-05-today-changed-pages-wing.md](/reviews/optimistic-2026-10-05-today-changed-pages-wing/) L39, the tenets locus belongs to an existing NEEDS-HUMAN entry. The arguments index is covered by the open P3 description task on that page. No task minted.
- Low: L105 names Albert and Price as critics, but the only Albert entry is the 1988 many-minds paper. Adding Albert 2010 and Price 2010 would cost about 30 words, which waits on the length decision.
- The length breach persists (3871 vs 3500), as reference apparatus. The NEEDS-HUMAN decision stands.

## Stability Notes

- Carried forward: the 07-19 notes (illusionist, eliminativist, branch-relative, Wilson and Many-Minds as bedrock; Argument 3 not independent; the symmetric burden).
- New: the diverging-worlds reading is **conceded**. Do not reinstate an unqualified fission premise or an unscoped "decisive against branch-egalitarian" claim.
- New: the Tappenden paragraph now matches both abstracts. Do not revert it to "extends the picture".
- New: Mandolesi belongs to Wallace's proof, not to Vaidman.