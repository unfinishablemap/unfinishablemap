---
ai_contribution: 100
ai_generated_date: 2026-09-05
ai_modified: 2026-09-05 00:00:06+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-05
date: &id001 2026-09-05
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-05 00:00:06+00:00
modified: *id001
related_articles: []
title: Deep Review - Ontic Structural Realism
topics: []
---

**Date**: 2026-09-05
**Article**: [Ontic Structural Realism](/concepts/ontic-structural-realism/)
**Previous review**: Never (article created 2026-09-04)

## Pessimistic Analysis Summary

### Critical Issues Found

All five criticals are citation/attribution defects. None is a philosophical disagreement. Every one was introduced by the expand step: the seed research note `[[ontic-structural-realism-galilean-exclusion-2026-09-04]]` is correct on all five points.

1. **Newman quotation is a two-source splice, misattributed to Newman 1928.** The article presented as an in-1928 Newman quotation: *"structure is not sufficient to uniquely pick out any relations in the world... only cardinality questions are open to discovery!"* Raw-grep of the SEP *Structural Realism* HTML shows the first clause is **Ladyman's own 2023 editorial prose** ("The basic problem is that structure is not sufficient to uniquely pick out any relations in the world") and the second is **SEP quoting Demopoulos and Friedman (1985: 627 [1989: 188])** ("Thus on this view, only cardinality questions are open to discovery!"). The ellipsis joined two authors 57 years apart and attributed both to Newman. **Resolution**: attributed each clause to its actual source; Demopoulos and Friedman now introduced at first use and the later paragraph de-duplicated.

2. **Loorits's given name is wrong.** Article said "Kalevi Loorits". Crossref (10.3389/fpsyg.2014.00237): **Kristjan** Loorits. The research note used the initial "K." only; the expand step hallucinated the expansion. **Resolution**: corrected to Kristjan.

3. **Stanciu's given name is wrong.** Article said "Dan Stanciu (2021)". Crossref (10.3390/e23010097): **Diana** Stanciu. Same mechanism — the note carried "Stanciu, D." and the expansion invented a male given name. **Resolution**: corrected to Diana.

4. **Holism about experience misattributed to Loorits.** Article: "His reply carries testable commitments — rejection of inverted qualia, holism about experience." Raw-grep of Loorits 2014 full text: "holism" 0 hits, "holistic" 0 hits. The paired commitments are **Lyre's**, verbatim from his abstract ("leads to holism about phenomenal experiences and serves to reject inverted qualia scenarios"); the research note attributed them to Lyre correctly. Loorits *does* independently deny the ideal positive conceivability of inverted qualia (verified in his raw text). **Resolution**: split the conjunct — the inverted-qualia denial stays with Loorits, holism returned to Lyre.

5. **Chalmers presented as owning an objection he only reports.** Article: "his objection being only that they 'seem to yield a world devoid of substance or qualities'". The Amherst lecture PDF reads: "Still, **many find these views objectionable, because** they seem to yield a world devoid of substance or qualities", followed by "And whether or not one accepts these objections, it is certainly not obvious that there are no quiddities." Chalmers reports and brackets the objection. **Resolution**: reframed as reported-not-owned, with the bracketing clause quoted. This *strengthens* the article's own point — Chalmers is even more generous to the rival than the article claimed.

### Medium Issues Found

6. **Six inline citations had no References entry** (orphans in the inline→references direction): Alter (2016), Fink/Kob/Lyre (2021), French (2014), Demopoulos & Friedman, and the SEP early-modern primary/secondary-qualities entry. **Resolution**: all added, metadata verified at Crossref/publisher; References renumbered 1–21. The "What Went Unread" section's honesty is unaffected — a verified bibliographic entry does not claim the text was read.

7. **Ladyman 1998 quote silently truncated.** "...continuity of reference to objects" — SEP reads "objects **and properties**". **Resolution**: restored.

### Publisher-of-Record Citation Ledger (§2.4)

Verified against raw artefacts (curl + Python grep), not summarisers.

- Ladyman 1998, *SHPS A* 29(3) 409–424 — **real-correct** (Crossref + SEP bibliography)
- Ladyman 2023, SEP *Structural Realism* — **real-correct**; quotes grep-verified in raw HTML
- Worrall 1989, *Dialectica* 43(1–2) 99–124 — **real-correct** (SEP bibliography, DOI 10.1111/j.1746-8361.1989.tb00933.x); "form or structure, not of content" verified at 1989: 117
- Esfeld & Lam 2008, *Synthese* 160(1) 27–46 — **real-correct** (Crossref; note Crossref `issued` is the 2006 online-first date, print issue 2008 — the 2008 form is canonical)
- Loorits 2014, *Front. Psychol.* 5:237 — **real-wrong-metadata** (given name Kalevi → **Kristjan**); all three body quotes grep-verified verbatim in the retrieved full text
- Lyre 2022, *Neurosci. Conscious.* 2022(1) niac012 — **real-correct**; all three quotes grep-verified verbatim via Europe PMC full text (PMC9396309)
- Newman 1928, *Mind* 37(146) 137–148 — **real-correct metadata, wrong-source quotation** (see Critical 1); Crossref confirms Mind XXXVII(146) 137–148
- Demopoulos & Friedman 1985, *Philosophy of Science* 52(4) 621–639 — **added** (was uncited); DOI 10.1086/289281
- Unger 1979, *Midwest Studies* 4, 177–222 — **real-correct**; the SEP sentence quoting him grep-verified verbatim
- Chalmers 2013, *Amherst Lecture in Philosophy* 8, repr. 2015: 254 — **real-correct**; both quotes grep-verified in the lecture PDF. The article's parenthetical claim that "the lecture names no one" and that naming Ladyman and Ross is Alter & Pereboom's gloss is **verified exactly**: "Ladyman" has zero occurrences in the 37-page PDF, and SEP *Russellian Monism* supplies the "(e.g., Ladyman and Ross...)" parenthesis
- Alter & Pereboom 2023, SEP *Russellian Monism* — **real-correct**
- Alter 2016, *Noûs* 50(4) 794–815 — **added**; Crossref-verified (DOI 10.1111/nous.12134)
- Fink, Kob & Lyre 2021, *Philosophy and the Mind Sciences* 2 — **added**; Crossref-verified (DOI 10.33735/phimisci.2021.79)
- French 2014, *The Structure of the World* — **added**; Crossref-verified
- Beni 2026, *JGPS* — **real-correct** (Crossref: Majid D. Beni, published 2026-03-14)
- Stanciu 2021, *Entropy* 23(1) 97 — **real-wrong-metadata** (given name Dan → **Diana**); reference initial "D." was already right
- Bolton 2022, SEP *Primary and Secondary Qualities in Early Modern Philosophy* — **added**; the article's Galileo-relocation reading verified near-verbatim against the entry ("SQs are not in bodies that cause them but internal to sentient bodies")
- Southgate self-cites (15, 16 → 20, 21) — Map internal; pseudonymous co-author forms are intentional and left untouched

**Empirical-record currency sweep**: the article's two quantitative claims are its own measurements, and both were independently re-measured this session against freshly fetched raw HTML. SEP *Structural Realism*: consciousness 0, conscious 0, experience 0, qualia 1 — **exact match**. SEP *Russellian Monism*: consciousness 96, French 0, Esfeld 0, "relations without relata" 0 — **exact match**. The "roughly 170,000 characters" figure is fair (175k extracted by my method, 170.5k by the research note's). No superseded superlatives.

### Counterarguments Considered

- *Newman's problem cuts against the Map's own epistemic structural realism.* The article already concedes this explicitly and declines the unearned asymmetry. Correcting Critical 1 improved the concession rather than weakening it — Demopoulos and Friedman now appear as the ones who sharpened the objection, which is what makes the later collapse-worry paragraph land.
- *The rival is a strawman.* The article's own §constructed-rival concedes this in the lead and the keyword census substantiates it. This is a strength, not a defect.

## Optimistic Analysis Summary

### Strengths Preserved

- **The constructed-rival concession in the lead.** Rare and honest: the article says up front that it refutes nobody in print, and backs it with a reproducible keyword census. Both census claims survived independent re-measurement exactly.
- **Route/conclusion separation.** "The composite threatens the Map's route, not its conclusion" is the correct calibration, and the evidential-status paragraph correctly books the loss as a defeater-removal rather than a premise. No possibility/probability slippage anywhere in the article — the Process Philosopher had nothing to inflate and the Hardline Empiricist nothing to flag.
- **The Chalmers calibration point.** "The Map should not be more confident against a position than the philosopher whose argument it borrows" is a genuinely self-disciplining move, and the correction to Critical 5 makes it stronger.
- **"What Would Change This View, and What Went Unread."** Sourcing gaps reproduced rather than hidden, each with its retrieval state named.

### Enhancements Made

Corrective only. The article's argument, structure and voice are unchanged; no section was expanded, and no new claim was added.

### Cross-links Added

None. All 16 existing wikilinks resolve (verified against the vault index). The article's claim about "the first falsifier listed in intrinsic nature" matches falsifier (1) in `concepts/intrinsic-nature` exactly.

## Remaining Items

- **Ladyman and Ross (2007) still unretrieved.** Every characterisation of *Every Thing Must Go* remains secondhand (via SEP or Loorits's gloss). The research note flags the book's treatment of the mental as "the most important remaining check". Not actionable without the book.
- **Beni (2026) abstract-only.** The article names it as the likeliest candidate for someone having staged the OSR/phenomenal-structuralism joining. Worth a retrieval pass when full text is available — it would settle the article's one open empirical claim.
- **Chakravartty cited without a year.** Left as a general attribution rather than a formal cite, to avoid minting a new inline→references orphan. SEP confirms Chakravartty (1998, 2003) is among those urging the no-relations-without-relata objection, so the attribution is accurate as it stands.

## Stability Notes

- **Length.** `analyze_length` reports 2655 words / soft_warning, but body prose is **2225 words** — the warning is entirely reference apparatus (82 frontmatter + 395 References + 49 Further Reading = 526 words), and the References block grew precisely because this review *fixed* an orphan-citation defect. This is the known false-over-length pattern. **Do not condense this article on the strength of that warning**; re-measure prose-only first.
- **Systemic finding, not a defect of this article.** All five criticals were introduced between a correct research note and the published article. The note used bare initials ("Loorits, K.", "Stanciu, D.") and the expand step hallucinated given names for both; the note attributed holism to Lyre and marked Newman "[cited via SEP]", and the expand step moved holism to Loorits and promoted the SEP paraphrase to a Newman quotation. **Expanding an initial into a given name, and promoting an encyclopedia's paraphrase into a primary-source quotation, are the two failure modes to watch when an expand-topic task consumes a well-disciplined research note.** The seed note has been annotated at the splice to stop re-propagation.
- **No bedrock disagreements were re-flagged.** The adversarial personas' framework-boundary objections (the eliminative materialist and Many-Worlds defender against Dualism, the physicalist against the remainder argument) are already handled honestly in "Relation to Site Perspective", which marks them as framework-boundary disagreements rather than claiming refutations. Future reviews should not re-open them.
- **Reasoning-mode classification** (editor-internal, §2.6): the article replies to no named opponent in refutation mode. Its engagements with Ladyman, Loorits and Lyre are Mode Three throughout — it explicitly declines to claim refutation ("refutes none of Ladyman, French, Esfeld, Loorits or Lyre"), and the Newman section marks its own reply as "a reply rather than a refutation". Correctly calibrated; no boundary-substitution, and no editor-vocabulary leakage into prose.