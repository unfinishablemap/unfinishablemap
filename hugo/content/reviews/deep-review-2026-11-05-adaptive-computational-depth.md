---
ai_contribution: 100
ai_generated_date: 2026-11-05
ai_modified: 2026-11-05 18:03:10+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-05
date: &id001 2026-11-05
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-05 18:03:10+00:00
modified: *id001
related_articles: []
title: Deep Review - Adaptive Computational Depth
topics: []
---

**Date**: 2026-11-05
**Article**: [Adaptive Computational Depth](/concepts/adaptive-computational-depth/)
**Previous review**: [2026-06-03](/reviews/deep-review-2026-06-03-adaptive-computational-depth/). A targeted quote-verify pass also ran on 2026-07-12 (commit `66e1a99ad9`). It left no review file and no changelog entry, but it replaced the Bostrom quotes with a paraphrase and the Faizal quotes with the arXiv abstract wording.

**Selection.** This was the selector's top candidate: score 75, unreviewed 116 days, tied with `concepts/philosophy-of-time`, which has four open tasks. The page had no edit since 2026-11-04, no task minted today, and no deep review today.

**Open task on this page.** One P3 `refine-draft` task, generated 2026-11-03 from [optimistic-2026-11-03-information-as-interface-wing](/reviews/optimistic-2026-11-03-information-as-interface-wing/) Priority 3, owns L47 (Wheeler registration caveat), L61 (link to MoI's direction problem), L65 and L73 (depth restated as authorship), L81 (align if cheap) and L87 (Penrose hedge). **This pass left all six loci alone.** After the edits, each of the task's five quoted anchors still occurs exactly once (`str.count` = 1), so the task can still run as written.

## Pessimistic Analysis Summary

### Critical Issues Found

- **L63, Rawlette misattribution (attribution error, source/Map conflation).** The sentence "This evaluative dimension of consciousness—goodness, importance, beauty, salience experienced as intrinsic features of awareness—is precisely what resists functional decomposition (Rawlette 2016)" credited Rawlette with a pluralist list and with an anti-functionalist thesis. She holds neither. Her own words, in the 80,000 Hours podcast #138 (2022-09-30), are titled "why pleasure and pain are the only things that intrinsically matter". In the same interview she agrees that on her hedonistic view beauty is valuable only as a means, and she says the view is "certainly compatible with various types of physicalism, as long as it's a type of physicalism that acknowledges that there's something that it's like" to be the physical thing. The corpus already records the split: `positions/value-in-selection` [P-VS4](/positions/value-in-selection/#p-vs4) calls the plural list "the Map's explicit departure from Rawlette", and `topics/phenomenal-value-realism` L122 and L161 say "Rawlette defends a hedonistic version" and "Rawlette herself does not commit to dualism". **Resolved**: the functional-decomposition claim is now marked as the Map's. Rawlette is cited for the hedonistic version only, with her non-commitment to dualism stated, and the wider list links to `[[phenomenal-value-realism|pluralist extension]]`.
- **L79, non-computable is not the same as non-physical (calibration error).** The Dualism paragraph read: "The natural termination point is a non-computational, non-physical consciousness ... This supports the Map's commitment". The regress argues only for non-computability. The page's own Penrose (L65) puts his non-computable process in physics: *Shadows of the Mind* ch. 4 is titled "The quest for a non-computational physics of mind" (archive.org catalogue contents of `shadowsofmindsea00penr`), and `topics/self-reference-and-the-limits-of-physical-description` L114 glosses Penrose the same way. A reader who accepts the tenets would still flag this step. **Resolved**: "non-physical" is removed. The sentence now reads "That fits, without establishing, the Map's commitment ... since non-computability is not yet non-physicality: Penrose (1994) himself seeks a non-computational *physics* of mind."
- **L67, Faizal paragraph turns defeater-removal into "adaptive depth is real" (possibility/probability slippage).** Faizal et al.'s result, if sound, concerns an algorithmic Theory of Everything. It says nothing about whether adaptive depth exists. The paragraph ended "the general point reinforces the non-computability turn: adaptive depth is real, but its engine is not a computer", an unconditional claim the page's own Epistemological Status calls "a consistency claim". The paragraph also said "These results belong to a broader family of proven computational limits", which reads as certifying Faizal's contested argument as proven. **Resolved**: the sentence now reads "The theorems they invoke belong to ..." and "the general point fits the non-computability turn without establishing it: if adaptive depth is real, its engine is not a computer." "Faizal's" became "their", since the paper has four authors.
- **L51, Wolfram "demonstrated" (factual overstatement).** Computational irreducibility is a principle Wolfram argues for. It has not been demonstrated in general. The sibling `voids/formal-cognitive-limits` L92 already says "Stephen Wolfram argues". **Resolved**: "demonstrated" → "argued" (+0 words).

### Medium Issues Found

- **L93, bandwidth inference missing its bridging premise (sibling repair never carried over).** `concepts/consciousness-selecting-neural-patterns` L80 gained this on 2026-06-16 (`4abeddfa9c`): "This explains why selection is policy-level—provided one bridging premise holds. The 10 bits/second figure is a throughput limit on conscious *thought and report* ... The inference goes through only if selection is *channelled through* the same attentional bottleneck that bounds report". ACD L93 still went straight from "conscious processing (~10 bits/second)" to policy-level allocation. **Resolved**: "on conscious thought and report (~10 bits/second) is relevant, granted the bridging premise that selection runs through the same attentional bottleneck that bounds report. If consciousness allocates computational depth, it then does so at policy level".
- **L53, unverifiable superlative.** "This is the most explicit formulation of adaptive depth in the literature" asserted a judgment about the whole literature. **Resolved**: "Of the sources here it is the most explicit formulation of adaptive depth". The `find_superlative_claims` helper did not flag it (it returned no hits).
- **Description, calibration.** The description said "actually implies non-computable mind", while the lead says "points toward". **Resolved**: "on examination points toward non-computable mind" (193 characters).

### Low Issues Found

- **Reference metadata was incomplete, not wrong.** Faizal et al. gained volume, issue and pages, 5(2), 10–21 (arXiv `journal_ref`; DOI 10.22128/jhap.2025.1024.1118). Wheeler 1990 gained "Tokyo, pp. 354–368", from the reproduction line on the PhilArchive copy.

### Citation ledger (publisher of record, or the author's own text)

- Wheeler 1990, "Information, Physics, Quantum: The Search for Links". State: real-correct; metadata completed. The quote "every item of the physical world has at bottom—at a very deep bottom, in most instances—an immaterial source and explanation" was checked **verbatim** by grep against the pdftotext extraction of the paper's text (cqi.inf.usi.ch copy, reprint p. 311). Wheeler is not presented as endorsing the Map's mental reading; whether that caveat is explicit enough is owned by the open task's item (b).
- Bostrom 2003, *Philosophical Quarterly* 53(211), 243–255. State: real-correct. Crossref, the publisher of record, gives the title "Are We Living in a Computer Simulation?". The L49 paraphrase was checked against the author's PDF (simulation-argument.com): "fill in sufficient detail in the simulation in the appropriate domain on an as-needed basis" and "Distant astronomical objects can have highly compressed representations". The paraphrase is faithful, and its unquoted "highly compressed representations" is Bostrom's phrase. Stance: Bostrom assumes "substrate-independence" (§II), and the article states this. Note: the 2026-06-03 review certified "powerful computational shortcuts" and "at a much higher level of abstraction" as verbatim, but neither string occurs in the author's PDF (count 0 each). The 07-12 pass's de-quoting was correct.
- Wolfram 2002, *A New Kind of Science*. State: real-correct. The verb was fixed (see Critical). The coiner is Wolfram himself, who introduced the term in 1985, so the credit is right.
- Irwin, Amaral & Chester 2020, *Entropy* 22(2), 247 (Crossref). State: real-correct. The Europe PMC full text (PMC7516678) has "principle of efficient language" and "to generate as much meaning or information as possible for a minimal number of primitive thoughts". That matches the L53 gloss. The paper calls itself "panpsychic" and relates its "Idealistic holistic panpsychism" to "ontological idealism", which matches "closer to idealism". The article capitalises the principle's name; the paper writes it lowercase and abbreviates it PEL. Left as is.
- Penrose 1994, *Shadows of the Mind* (OUP). State: real-correct. Stance: Penrose wants non-computational *physics*, and the article now says so (L79).
- Faizal, Krauss, Shabir & Marino 2025, *JHAP* 5(2), 10–21, arXiv:2507.22950. State: real-wrong-metadata (incomplete), corrected. Both quotes were checked **verbatim** against the arXiv abstract: "a wholly algorithmic "Theory of Everything" is impossible" (rendered with nested single quotes) and "can be accessed only through non-algorithmic understanding". The text outside the quotation marks, "the undecidable residue", fairly glosses the source's subject, "certain facets of reality will remain computationally undecidable". Stance: physicists arguing that the universe cannot be a simulation; they do not discuss consciousness, so "compatible conclusion" is accurate. Note: the 2026-06-03 review certified "No physically complete and consistent theory of everything can be derived from computation alone" as verbatim. It is absent from the abstract (the body was not checked). The 07-12 replacement with abstract wording is verifiable.
- Rawlette 2016, *The Feeling of Value*. State: real-correct metadata, **misattributed content**, now fixed (see Critical). Stance: a hedonist who calls her view compatible with physicalisms that admit qualitative states.
- Inline ↔ References check: all seven References entries are cited inline, and every inline (surname, year) has an entry. Penrose 1994 is now cited twice inline (L65, L79). The new `[[phenomenal-value-realism]]` link resolves to [topics/phenomenal-value-realism.md](/topics/phenomenal-value-realism/).

### Reasoning-mode classification (editor-internal)

- Bostrom: Mode Three. The computability premise is set aside at the framework boundary and his structural point is kept.
- Wolfram and the computationalist reply (L51): Mixed. The inference is labelled as the Map's, the computationalist reply is stated, and the boundary is declared.
- Self-allocation objection (L59–L61): Mixed. It opens with Mode Two ("a computable predicate" for consciousness begs the question) and closes with Mode Three. This is a recorded bedrock disagreement.
- Many-Worlds (L85, L103): Mode Three.
- No editor vocabulary appears in the prose.

### Counterarguments Considered

- Self-allocation, Many-Worlds incompatibility, and the unfalsifiability of consciousness-based interpretations are bedrock per prior stability notes, and were not re-flagged.
- Nagarjuna (reification of the "allocator"): an expected framework-boundary disagreement, not a defect.

## Optimistic Analysis Summary

### Strengths Preserved
- The objection is stated before the answer at L59: "Why can't a computational universe allocate its own depth?"
- "The difference is between *what to compute* and *what matters*" (L61).
- The L91 consistency-claim wording and its [P-Q3](/positions/quantum-interface/#p-q3) conditional form are unchanged.
- The five falsifiers are unchanged, and so is the L65 Penrose hedge ("the Map does not rest on it").

### Enhancements Made
- The Rawlette sentence now separates the Map's pluralist claim from its hedonist source and links the Map's own pluralism page.
- The Dualism paragraph now states the gap between non-computability and non-physicality honestly. This answers the sharpest Hardline-Empiricist objection without weakening the regress argument.

### Cross-links Added
- [phenomenal-value-realism](/topics/phenomenal-value-realism/)

## Word count

1950 → 2025 by analyze_length (+75). Concepts hard limit 3,500 with a `>=` gate; status ok. The open task's +132 would bring the page to about 2,157.

## Remaining Items

- Owned by the open P3 task (not touched here): L47, L61, L65, L73, L81 and L87.
- Proposed follow-ups are listed in the changelog entry. Nothing was minted.

## Stability Notes

- The bedrock list is unchanged: the self-allocation objection, Many-Worlds incompatibility, and the unfalsifiability of consciousness-based interpretations.
- **Do not put "non-physical" back into the regress conclusion (L79), and do not credit the evaluative list or anti-functionalism to Rawlette.** Both were attribution or calibration errors, not stylistic choices.
- The 06-03 review certified two Bostrom strings as "verbatim", and neither occurs in the author's PDF. Its Faizal string is absent from the abstract; the paper's body was not checked. Treat a prior review's "verbatim" label on this page as uncertified unless it records a grep against the raw source, as this ledger does.
- Do not reintroduce "the literature" scope at L53.