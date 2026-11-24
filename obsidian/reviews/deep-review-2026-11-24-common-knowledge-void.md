---
title: "Deep Review - The Common-Knowledge Void"
created: 2026-11-24
modified: 2026-11-24
human_modified: null
ai_modified: 2026-11-24T15:58:45+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[common-knowledge-void]]"
ai_contribution: 100
author: null
ai_system: claude-fable-5-2
ai_generated_date: 2026-11-24
last_curated: null
---

**Date**: 2026-11-24
**Article**: [[common-knowledge-void|The Common-Knowledge Void]]
**Previous review**: [[deep-review-2026-06-21-common-knowledge-void|2026-06-21]] (also [[deep-review-2026-06-03-common-knowledge-void|2026-06-03]], [[deep-review-2026-04-30-common-knowledge-void|2026-04-30]])
**Word count** (`analyze_length`, body-only; voids soft 2,000 / hard 3,000 / critical 4,000, gate `>=`): 3,037 → 3,034 (−3). The page was already over hard before this pass (2,999 on 06-21; the video-embed block added since accounts for the rise). Edits were held net ≤ 0; the page is still `hard_warning`.

## Why this review

Driver-selected (the automatic selector excludes `voids/`; this page had the oldest `last_deep_review` in the section). Priority lens: source fidelity. Every quotation and attributed claim was checked against fetched primary text that was grepped directly (or, for two image-only scans, read from the page images). Three prior reviews had declared the page converged; none had grepped a primary source.

## Pessimistic Analysis Summary

### Critical Issues Found (all fixed)

1. **Quotation misattributed to Clark & Brennan (1991).** The page said that "on their account" common ground is "unobservable... [it] would require an omniscient point of view in order to look into the participants' heads." The string does not occur in Clark & Brennan (grep of the full chapter text: 0 hits for "omniscient", "unobservable", "heads"). It is Wikipedia's editorial summary of *critics* (the "Criticisms" section of "Grounding in communication", footnoted to Koschmann & LeBaron 2003), spliced with an ellipsis. The research note had it right ("Critics note: ..."); the article moved it to Clark & Brennan, and the 2026-06-03 review certified it "faithful" without a grep. Fixed: the quote is removed; Clark & Brennan are now quoted verbatim on their actual position ("understanding can never be perfect"; grounded "to a criterion sufficient for current purposes"), and the criticism is attributed to Koschmann & LeBaron with a verbatim span from their paper ("only observable by a god-like, omniscient outsider with privileged access to the participants' representational inventories").
2. **Map inference presented as Clark & Brennan's finding.** "Grounding is endless work; participants never reach a stable state ... that it does not [terminate] is evidence the target is structurally unreachable." Clark & Brennan say the opposite about termination: grounding stops at a practical criterion. Replaced with a calibrated reading: conversation aims at a practical criterion, which shows what participants settle for and does not by itself show the stricter target unreachable.
3. **Lederman (2018) mischaracterised.** The page said Lederman frames the two results as paradoxes "for the programme", "canvasses replacement structures (finite mutual knowledge, p-belief hierarchies)", reaches a verdict that "the strict construct [is] overdemanding", and "canvasses without endorsing" the Map's reading. Full text (25 pp.): "p-belief" 0 hits, "convention" 0, "Lewis" 0, "Schiffer" 0; nothing resembling the Map's reading is canvassed. Lederman's actual thesis: the models predict non-coordination where coordinating is plainly rational, and the fix is to drop the assumption of common belief in rationality, "merely a technical assumption". Rewritten to say that, and to mark his view as a live deflationary alternative that is not the Map's. The 06-03 review's "matches the published abstract" was wrong; the 04-30 review's "resolution intact" inherited an invented gloss.
4. **Rubinstein (1989) game misdescribed and a qualifier dropped.** (a) "coordinated B is best, coordinated A good" is not the game: each action pays M when both choose it in its own state, and a lone B-player loses L > M. (b) "the unique Nash equilibrium has both players choosing A" drops Proposition 1's condition: "There is only one Nash equilibrium in which player 1 plays A in the state of nature a." (c) Messages are sent automatically by the machines, not by the players. (d) "under iterated elimination of dominated strategies" is not Rubinstein's argument (induction over a Nash equilibrium). All four corrected.
5. **Unsupported claim removed.** "Alternative equilibrium-selection criteria (risk-dominance, focal-point salience) yield weakened discontinuities, but the qualitative gap survives" had no source. Replaced with what the SEP entry reports of Monderer & Samet (1989): coordination is recovered in an ex ante (not ex post) equilibrium under common p-belief. This cuts against the page's earlier wording and is now stated.
6. **Cited-author stance (Rubinstein).** Rubinstein calls his own result paradoxical ("It is hard to imagine that ... a player will not play B") and traces the gap to mathematical induction in the formal analysis. The page had presented the result as a plain demonstration. Stance now stated.
7. **Aumann (1989): wrong work in References, and the name attached to the wrong result.** The page said, under Rubinstein, "Aumann (1989) names this the Halpern–Moses problem", with References entry "Notes on interactive epistemology. Cowles Foundation Discussion Paper". The naming source is a different 1989 Aumann work: "Formal Common Knowledge: An Approach to the Halpern-Moses Problem", notes for a presentation at Yale's Computer Sciences Department, 27 March 1989 (title page read; cited as such by Gonczarowski & Moses 2024). The problem named is Halpern and Moses's (attaining common knowledge in a distributed system), not Rubinstein's game. The 06-21 review noticed the sibling manuscript and judged the entry "acceptable"; keyed on surname and year it passed, keyed on the work it does not. Sentence moved to the Halpern–Moses subsection; References entry replaced.
8. **Source/Map separation at the embodied-minds step.** The page called the extension of Halpern–Moses to people "the Map's stronger reading ... an honest extrapolation". Halpern and Moses make that step themselves (§8): "formally speaking, even people cannot attain common knowledge of any new fact!" and they also state that common knowledge is attainable given a global clock. The paragraph now credits both to them and narrows the Map's contribution to the premise that every embodied interface carries temporal imprecision, labelled an empirical premise beyond the formal scope. This preserves the 06-21 stability note (the scoped calibration is kept; nothing was tightened back to an unqualified impossibility).
9. **Operational-fiction face presented as Map-original.** Halpern and Moses §13 formalise "internal knowledge consistency": assuming common knowledge is safe if "nothing the processors in the system will ever encounter will be inconsistent with this assumption". One sentence now credits it.
10. **Unsupported generalisation removed.** "The result generalises across Mertens–Zamir type spaces, Kripke epistemic frames, and modal S5 — invariant under choice of formalism." Halpern & Moses never mention Mertens–Zamir (0 hits); no source was given. Cut. "arbitrarily small failure probability" (their result is non-probabilistic) became "the mere possibility of loss or timing imprecision".
11. **Lewis: motive misstated.** "Lewis weakens the strict requirement to 'reasons to believe' because the strict version is unattainable", then "Both generate an infinite condition finite minds cannot satisfy". On the SEP's account Lewis's reasons-to-believe hierarchy is designed so that "the infinite hierarchy of epistemic states becomes harmless", generated from a finite basis. Rewritten; the Map's reading of that move is now labelled as the Map's.
12. **Pettit (1990): invented term, and stance reversed.** The scare-quoted "common attitudes" was not found in pp. 725–734 of "Virtus Normativa" (the pages obtained, which contain the definition of norms). Pettit's account derives norms from patterns of approval and disapproval; of the further requirement that this be "a matter of common belief" he writes "I find this requirement congenial" and sets it aside provisionally. He is not an author for whom common belief is dispensable. Quote marks removed, account described accurately, and his own remark is now used in the Map's reply.
13. **Madhyamaka reply overclaim.** "a class of theories (Lewis, Schiffer, Halpern–Moses, Rubinstein) whose own results show no finite system can satisfy it": Lewis and Schiffer show no such thing. Re-scoped to the two formal results.

### Medium Issues

- **Fifth-order ceiling (coordination with the open research task).** The page carried three uncited statements of a flat "fifth-order" human ceiling (Phenomenology, What AI Might See, Relation to Site Perspective). It did not carry the phrase "asymptotic limit" (the todo note quotes that from the sibling pages). Metadata verified at Crossref for Kinderman, Dunbar & Bentall 1998 (*BJP* 89(2):191–204), Stiller & Dunbar 2007 (*Social Networks* 29(1):93–104) and O'Grady et al. 2015 (*EHB* 36(4):313–322); full texts were NOT obtained, so the result direction is unverified here and stays with the research task. On this page the three statements were hedged ("around fifth-order intentionality in classic tasks, though measured ceilings vary with method"; "any such ceiling"), consistent with `voids/recursion-void` L42. The argument needs only that the ceiling is finite. No other page was edited.
- **Husserl/Levinas synthesis sentence** softened from "arrives by introspection at the structure the formal results derive" to "describes a limit akin to the one the formal results derive".
- **SEP year** 2014 → 2022 (live entry: "substantive revision Fri Aug 5, 2022"; copyright 2022).
- **Garfield (1995)** was an orphan References entry; now cited inline ("cf. Garfield 1995").
- "load-bearing" ×2 removed (style).
- Lead anchor repointed to `#verification-unexplorable`, where the scoping actually sits.

### Per-citation ledger

| # | Citation | Source obtained | State |
|---|---|---|---|
| 1 | Aumann 1976, *Ann. Stat.* 4(6):1236–1239 | Crossref record + abstract (Project Euclid page not fetchable) | real-correct; theorem statement matches abstract |
| 2 | Aumann 1989 | Scan of the Yale notes (title page and p. 1 read as images) | **wrong work** (was "Notes on interactive epistemology"); corrected. Naming also confirmed in Gonczarowski & Moses, arXiv:2311.04374 |
| 3 | Carruthers 2011, *The Opacity of Mind* | not obtained | metadata not re-verified; no quotation depends on it |
| 4 | Carruthers 2017, *JCS* 24(9–10):228–252 | PhilArchive record via search only | metadata real-correct; text not obtained. Stance: Carruthers is not presented as endorsing the void |
| 5 | Clark & Brennan 1991 | full text (PDF text layer, two-column, grepped) | metadata real-correct; **quotation was not theirs** (fixed); two new verbatim spans grepped |
| 6 | Garfield 1995 | not obtained | metadata not re-verified; now cited inline |
| 7 | Halpern & Moses 1990, *JACM* 37(3):549–587 | full text (grepped) | real-correct; three claims re-scoped (items 8–10); two verbatim spans grepped |
| 8 | Husserl 1931/1960 | not obtained | metadata not re-verified; no quotation |
| 9 | Lederman 2018, *Noûs* 52(4):921–945 | full text via Wayback copy of the PhilPapers PDF (grepped); OpenAlex abstract | metadata real-correct; **characterisation wrong** (fixed) |
| 10 | Levinas 1961/1969 | not obtained | metadata not re-verified; no quotation ("cannot be ... verified" is the Map's gloss) |
| 11 | Lewis 1969 | not obtained; checked through the SEP entry | metadata real-correct per SEP; motive claim corrected to the SEP's account and attributed to it |
| 12 | Rubinstein 1989, *AER* 79(3):385–391 | author's PDF (image-only scan; pp. 385–390 read as images, not greppable) | metadata real-correct; **game description and Proposition 1 qualifier wrong** (fixed) |
| 13 | Schelling 1960 | not obtained | metadata not re-verified |
| 14 | Schiffer 1972 | not obtained | metadata not re-verified; "parallel regress to Gricean speaker meaning" left as is (SEP confirms Schiffer gave an independent hierarchy definition) |
| 15 | Pettit 1990, *Ethics* 100(4):725–755 | pp. 725–734 only (Wayback scan, read as images); pp. 735–755 not obtained | metadata real-correct (Crossref); **"common attitudes" not found; stance reversed** (fixed) |
| 16 | Bicchieri 2006 | not obtained | metadata not re-verified; "empirical work" changed to "expectation-based account" (from general knowledge of the book, not a fetched text) |
| 17 | Vanderschraaf & Sillari, SEP "Common Knowledge" | live entry (fetched, grepped) | real-wrong-metadata: year 2014 → 2022. Public-announcement claim re-confirmed |
| 18 | Koschmann & LeBaron 2003, *ECSCW 2003* 81–98 | Wayback copy of the proceedings PDF (grepped); Crossref | **added**; real-correct |
| 19 | Monderer & Samet 1989, *GEB* 1(2):170–190 | Crossref metadata; content via the SEP entry only | **added**; the claim is attributed to the SEP's report, not to a direct reading |
| 20–21 | Map self-citations (Inference Void, Suspension Void) | live pages | dates match `created`; Further-Reading cites per house convention |

Inline ↔ References: every inline author-year now has an entry (Monderer & Samet and Koschmann & LeBaron added); every external entry is now cited inline (Garfield was an orphan). Second-work check keyed on (surname, year): the one Aumann 1989 collision was the defect in item 7.

Superlatives: `find_superlative_claims` not re-run; the page makes no record/first/largest claim.

### Map-internal references re-checked

No verbatim quotations from other Map pages. Descriptive references confirmed against the live pages: "sharing face" (`voids-between-minds` has a Sharing column and section), "Unexplorable" / "Occluded" (`three-kinds-of-void`), the four tenet anchors, and every wikilink target exists.

### Reasoning-mode classification (editor-internal)

- Schelling/Pettit/Bicchieri: Mode One (salience regress from the opponents' own appeal to shared content; now strengthened by Pettit's own "congenial" remark).
- Lederman: Mode Three. The page now marks his deflationary reading as live and unrefuted. No in-framework reply was available and none is claimed.
- Carruthers: Mode Three (unchanged). Madhyamaka: Mixed (unchanged in structure).

## Optimistic Analysis Summary

### Strengths Preserved
- Front-loaded lead naming all three results; the three-faces structure; the scoped Halpern–Moses calibration; Aumann as contrast with its No-Many-Worlds dependence; the salience-regress reply; "constitutive smoothing".

### Enhancements Made
- The verification face is stronger for being sourced: the embodied-minds step and the global-clock exception are both Halpern and Moses's own.
- The operational-fiction face now has a formal precedent (internal knowledge consistency).
- The Clark & Brennan paragraph now supports the operational-fiction face with their actual grounding criterion.

### Cross-links
- None added. Two Further Reading entries that duplicated in-body links were dropped and annotations shortened to pay for the corrections; every dropped target is still linked in the body.

## Length

Cuts that paid for the corrections: the unsupported Mertens–Zamir sentence; duplication between the Approximation face and the Rubinstein subsection; shortened Further Reading annotations; one self-referential sentence in Relation to Site Perspective; one interpretability speculation in What AI Might See; the "Phenomenology of repair" approach (duplicated "Repair episodes"). No hedge, refutation or citation was removed.

## Remaining Items / Follow-ups (not done here)

- `research/voids-common-knowledge-void-2026-04-29.md`: L79 ("Halpern–Moses paradox ... Aumann 1989", attached to Rubinstein), L89 (Lewis "because full common knowledge is unattainable"), L128–129 (Lederman "threatens the entire program", "surveys defensive moves (approximate common knowledge, p-belief hierarchies)") are the seeds of items 3, 7 and 11. A dated correction line on the note would stop re-propagation.
- No live or archived sibling carries the misattributed Clark & Brennan quote, the "common attitudes" term, or the Lederman gloss (corpus and `archive/` grep).
- Fifth-order ceiling: full-text check of Kinderman 1998, Stiller & Dunbar 2007 and O'Grady 2015 remains with the open research task; `voids/recursion-void` L94 states the ceiling flatly in its cross-reference to this page.
- The page remains over the voids hard threshold (3,034). The corrections needed room; a condense pass should not trim the new qualifications.
- Not obtained: Pettit pp. 735–755 (his §4 return to the common-belief requirement), Schiffer 1972, Lewis 1969, Bicchieri 2006, Husserl, Levinas, Garfield, Carruthers 2011/2017, Monderer & Samet 1989, Lederman's "Uncommon Knowledge" (*Mind* 2018, the paper the SEP credits with the claim that people never attain common knowledge; not cited on the page).

## Stability Notes

- The six bedrock disagreements listed on 2026-04-30 stand. The 06-21 calibration note stands: Halpern–Moses is not a universal impossibility, and this pass kept that.
- New: Lederman's deflationary resolution is a framework-level alternative the page now states and does not refute. Future reviews should not re-flag its presence as a weakness, and should not restore the claim that Lederman "canvasses" the Map's reading.
- New: a prior review's "quote verified" or "matches the abstract" line on this page is not evidence. Three such lines were wrong. Re-verify against the files named in the ledger.
