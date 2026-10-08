---
title: "Deep Review - Multiple Drafts Model and the Cartesian Theater"
created: 2026-10-08
modified: 2026-10-08
human_modified: null
ai_modified: 2026-10-08T09:54:29+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-fable-5-1
ai_generated_date: 2026-10-08
last_curated: null
---

**Date**: 2026-10-08
**Article**: [[multiple-drafts-model|Multiple Drafts Model and the Cartesian Theater]]
**Previous review**: [[deep-review-2026-08-21-multiple-drafts-model|2026-08-21]], preceded by [[deep-review-2026-07-26-multiple-drafts-model|2026-07-26]] and [[pessimistic-2026-07-25-multiple-drafts-model|pessimistic 2026-07-25]].

**Change since last review**: one line. The 2026-10-04 expand-topic for `topics/the-divided-will` grafted a Further Reading entry (`[[the-divided-will]] — Partitioned and distributed models of the will, which explain choice with no single selector`) and bumped `ai_modified`; the body argument and the References block were otherwise byte-identical to the 2026-08-21 state. A cosmetic requalification, so the pass was spent on the lenses the two prior ledgers never ran: both certified citation *metadata* only, and neither grepped a quoted phrase or a theory statement against the raw text of Dennett 2001 or Dennett & Kinsbourne 1992. This review did, and also re-read the 2026-08-21 repair paragraph (§Relation, the register-anchored concession) against the register's current state.

## Pessimistic Analysis Summary

### Critical Issues Found

None. Specifically ruled out this pass:

- **Quote fidelity (raw-source grep).** Every quoted phrase in the article was located verbatim in the source text. Dennett & Kinsbourne 1992 (full text, Wayback copy of the Tufts-hosted final draft): "it all comes together" (abstract and §1.1, twice more), "presented" (abstract), "no fact of the matter" (endnote 12, "our contention that there is no fact of the matter"). Dennett 2001 (full text, Wayback copy of `cognition.fin`): "fame in the brain" (6 hits), "cerebral celebrity" (2 hits — "a more useful guiding metaphor: 'fame in the brain' or 'cerebral celebrity' (Dennett, 1994, 1996, 1998)"). The 2026-08-21 rewording of the priority claim ("Across his later work … stating it compactly in 2001") is confirmed correct by Dennett's own 1994/1996/1998 self-citation for the metaphor.
- **Theory statements against the publisher of record.** The Cartesian-materialism definition at L33 matches D&K §1.1 ("the view one arrives at when one discards Descartes' dualism but fails to discard the associated imagery of a central (but material) Theater"). The straw-man reply at L35 matches D&K §1.1 ("Whether or not anyone explicitly endorses Cartesian materialism, some ubiquitous assumptions of current theorizing presuppose this dubious view"). The Orwellian/Stalinesque etymologies at L45 match D&K §2.2 exactly (Ministry of Truth rewriting history; show trials with "bogus confessions"). Colour-phi at L41 matches D&K's "the color of the moving spot switch in mid-trajectory from red to green". The cutaneous-rabbit gloss at L41 matches D&K's abstract ("an illusion of evenly spaced series of 'hops' produced by two or more widely spaced series of taps") and Geldard & Sherrick's own abstract (Europe PMC 5076909: "widely separated bodily points … trains of taps … 'phantom' impressions connecting the points actually touched").
- **Dennett's on-record answer to "for whom?" (L69).** Confirmed in Dennett 2001 §3 ("it seems to be leaving out the most important element — the Subject! … The mistake behind this misbegotten objection is not noticing that the First Person has in fact already been incorporated into the multifarious further effects"). The article's claim that the cerebral-celebrity gloss *is* Dennett's answer to the narrator premise is accurate and is stated on his terms before the Map replies.
- **GNW welcome (L51).** Dennett 2001 §1: "Dehaene and Naccache … see convergence coming from quite different quarters on a version of the global neuronal workspace model … I agree, and will attempt to re-articulate this emerging view in slightly different terms." Direction and strength of the attribution are right.
- **Register anchoring of the 2026-08-21 repair (L67).** `positions/quantum-interface` P-Q1 (last reviewed 2026-07-27, entry edited 2026-09-27 for P-Q3's Maier null) still carries horn (a) — P(O | do(C), X) ≠ q(O | X) — as specifiable and still states that exclusive Route-1 commitment "falls to *low* credence". The article's wording ("open dilemma with one horn still specifiable, and foreclosing it counts there as a demotion") remains faithful. The 09-27 register change (external-RNG nulls no longer count as a conditioned corridor test) does not touch anything the article says.
- **Reasoning-mode discipline.** Unchanged from 2026-07-26: verificationism lever is Mode Two (stated as "a standard Dennett's own account must meet"); narrator argument is Mode Three and marked as such; no editor-vocabulary leakage (grep for the forbidden labels: 0 hits). No "This is not X. It is Y." and no "load-bearing".

### Medium Issues Found

- **Dangling self-reference at L45 — a fresh-create defect that survived three reviews.** "The timing illusions generate MDM's sharpest argument, forward-referenced above." Nothing above forward-references the Orwellian/Stalinesque argument: the lead's only forward reference ("developed below") points at the Map's response, and §The Positive Editorial Picture ends on postdiction without announcing the argument. `git log -S` traces the phrase to the 2026-07-12 creation commit (ac6defc3fd) unchanged. **Fixed** — "forward-referenced above" deleted; the sentence now reads "The timing illusions generate MDM's sharpest argument." (−3 words).
- **Originator axis — the two illusions were unattributed.** L41 correctly said Dennett and Kinsbourne "drew this from timing illusions" (so no misattribution to Dennett), but named no discoverer, and the Map had no entry for either paper anywhere in the corpus (`grep -ri "Kolers\|Geldard" obsidian/` outside `reviews/`: 0 hits). **Fixed** — inline cites added: "(Kolers and von Grünau 1976)" and "(Geldard and Sherrick 1972)", plus "two earlier timing illusions" so the lineage is explicit; two References entries added, both verified at Crossref (ledger below).

### Counterarguments Considered

- All three carried-forward standoffs (subject-realism bedrock; Dennett's rejection of the objection split; Popperian unfalsifiability of the residue) are answered in the text per the 2026-07-26 and 2026-08-21 reviews and were not re-flagged.
- **Historical quibble on L51 "successor to MDM" (Empiricist persona)**: Baars's global workspace (1988) predates MDM (1991), so GWT is not a chronological successor. The article scopes the claim with "On this lineage" — Dennett's own 2001 narrative, in which MDM "did not provide … a sufficiently vivid antidote" and the GNW consensus is where his view lands — and names GNW (Dehaene & Naccache 2001), which does postdate MDM. Not a defect; noted so a future pass does not re-litigate it.

## Citation Web-Verify Ledger (§2.4)

Trigger met this pass only because the review added two entries; the four Dennett entries were re-verified against raw text anyway, since the prior ledgers certified metadata only.

- Dennett 1991 (*Consciousness Explained*, Little, Brown, Boston) — state: real-correct (carried from 2026-07-26; "coined the term Cartesian Theater" is consistent with D&K 1992 citing Dennett 1991 as the origin of the Multiple Drafts / Cartesian Theater contrast).
- Dennett & Kinsbourne 1992 (Time and the observer: The where and when of consciousness in the brain, *BBS* 15(2), 183–201, doi:10.1017/S0140525X00068229) — state: real-correct; **raw text grepped** (Wayback `ase.tufts.edu/cogstud/papers/time&obs.htm`); every quoted phrase and every theory gloss located (see Critical Issues). Result direction: the paper argues *for* "no fact of the matter" between Orwellian and Stalinesque revisions (endnote 12 confirms this is the authors' contention against Harnad) — direction matches the article.
- Dennett 1988 (Quining Qualia, in Marcel & Bisiach eds., *Consciousness in Contemporary Science*, OUP) — state: real-correct (carried from 2026-07-26; Dennett 2001 §4 self-cites "my warnings (1988, 1991, 1994b)" against the term *qualia*, consistent with the article's "denying the datum" gloss of the critics' charge).
- Dennett 2001 (Are we explaining consciousness yet?, *Cognition* 79(1–2), 221–237) — state: real-correct; Europe PMC PMID 11164029, doi:10.1016/S0010-0277(00)00130-X, pages 221–237 confirmed; **raw text grepped** (Wayback `cognition.fin.htm`, header "FINAL DRAFT [cognition.fin] for Cognition, August 27, 2000"). DOI appended to the References entry this pass. Cited-author stance: Dennett is anti-dualist and the article presents him as such throughout.
- **Kolers & von Grünau 1976** (Shape and color in apparent motion, *Vision Research* 16(4), 329–335, doi:10.1016/0042-6989(76)90192-9) — state: real-correct, **added this pass**; Crossref record matches authors, title, venue, volume, issue, pages, year. Result direction: colour change perceived mid-trajectory — as the article and D&K state.
- **Geldard & Sherrick 1972** (The cutaneous "rabbit": A perceptual illusion, *Science* 178(4057), 178–179, doi:10.1126/science.178.4057.178) — state: real-correct, **added this pass**; Crossref and Europe PMC (PMID 5076909) match; abstract confirms "widely separated bodily points … trains of taps … 'phantom' impressions connecting the points" — direction matches.
- Southgate & Oquatre-six 2026-01-21 (Unity of Consciousness) — state: real-correct (Map self-cite; target exists, `created: 2026-01-21` matches).
- Southgate & Sonquatre-cinq 2026-01-23 (Heterophenomenology) — state: real-correct (target exists, `created: 2026-01-23` matches).

Cross-reference: every inline cite (1991, 1992, 1988, 2001, 1976, 1972) has a References entry and vice versa; the two self-cites correspond to body wikilinks. No References orphans. Superlative-claim scan (`find_superlative_claims`): not re-run — no superlative vocabulary in the body (grep for "first to", "largest", "to date", "current record": 0 hits).

## Optimistic Analysis Summary

### Strengths Preserved

- The spine (narrator argument honestly marked as Mode Three; verificationism as the one in-framework lever; register-anchored concession) is untouched.
- The timing-illusion exposition is now not only accurate against D&K but sourced to its discoverers — the Hardline Empiricist's praise point this pass: the article's empirical floor is now traceable to two 1970s psychophysics papers rather than resting on Dennett's retelling.
- Dennett's reply to "for whom?" is stated on his terms before the Map answers; confirmed verbatim in Dennett 2001 §3.

### Enhancements Made

- L41: originators named inline for both illusions; "two earlier timing illusions" makes the lineage explicit (+~12 words).
- L45: dangling "forward-referenced above" removed (−3 words).
- References: DOI appended to Dennett 2001; Kolers & von Grünau 1976 and Geldard & Sherrick 1972 added (+~37 words).

### Cross-links Added

None — no new Map page is relevant that is not already linked. The 2026-10-04 `[[the-divided-will]]` graft was checked: the target lists this page in `related_articles` only (no body mention of Dennett), so the reciprocal is frontmatter-only on that side; the gloss here ("no single selector") is apt and was left as is.

## Remaining Items

None for this article. One optional follow-up for the sibling page, not minted as a task: `obsidian/topics/the-divided-will.md` carries `[[multiple-drafts-model]]` in `related_articles` but its body never mentions Dennett or the Multiple Drafts Model, so the link this page's Further Reading now makes is one-directional in body text (frontmatter membership is not a link). A future pass on that page could pipe a body link where it discusses distributed selection with no central selector.

## Stability Notes

- **Carried forward and still binding**: subject-realism bedrock; Dennett's rejection of the objection split (answered in text); Popperian unfalsifiability (conceded and owned); the register-anchored concession must not drift back to "no probe could register the difference" (read P-Q1 before "strengthening the honesty").
- **New**: the quoted phrases and theory glosses in §§Negative Core, Positive Editorial Picture, Orwellian/Stalinesque and Cerebral Celebrity have now been grepped against the raw text of both Dennett sources. Future reviews may treat them as raw-source-certified unless the body text changes; a metadata-only ledger would not have certified them.
- **"Successor to MDM" (L51)** is Dennett's 2001 lineage claim, scoped by "On this lineage", not a chronological claim about Baars 1988. Do not re-flag.
- Word count 1944 → 1990 (+46), well under the 2500 concepts/ soft threshold.
