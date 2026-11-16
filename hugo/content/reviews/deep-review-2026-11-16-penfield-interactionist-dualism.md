---
ai_contribution: 100
ai_generated_date: 2026-11-16
ai_modified: 2026-11-16 00:41:10+00:00
ai_system: claude-fable-5-2
author: null
concepts:
- interactionist-dualism
- bidirectional-interaction
created: 2026-11-16
date: &id001 2026-11-16
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-16 00:41:10+00:00
modified: *id001
related_articles: []
title: Deep Review - Wilder Penfield's Interactionist Dualism (2026-11-16)
topics: []
---

**Date**: 2026-11-16
**Article**: [Wilder Penfield's Interactionist Dualism](/concepts/penfield-interactionist-dualism/)
**Previous review**: [2026-09-04](/reviews/deep-review-2026-09-04-penfield-interactionist-dualism/)

## Scope of this pass

Fourth deep review. Since 2026-09-04 four commits changed the body: the section "The inverse case: authorship without movement" was added with two new citations (Evans et al. 2015; Serino et al. 2022), the Sherrington sentence was reworded against the 1940 text, the Popper/Eccles paragraph gained a link, and one Further Reading line was retargeted after a coalesce. The new section had never been reviewed, so the source checks concentrated there. Two critical issues were found in it, both fixed; one reference had a missing co-author.

## Pessimistic Analysis Summary

### Citation ledger (checked this pass)

- Evans, Gale, Schurger & Blanke 2015 (*PLoS ONE* 10(6), e0130019) — metadata real-correct (OpenAlex record). Result leg: **description was incomplete and the inference drawn from it misstated the model** (critical issue 1). Checked against the abstract and the publisher's full-text XML, read by grep.
- Serino, Bockbrader, Bertoni et al. 2022 (*Nature Human Behaviour* 6(4), 565–578) — metadata real-correct (OpenAlex, Europe PMC). Result leg: **scope overstated** (critical issue 2). Checked against the Europe PMC abstract only; full text not read.
- Robinson 2025, SEP "Dualism" — real-wrong-metadata: the live entry's copyright line reads "Howard Robinson, Ralph Weir". Corrected to Robinson, H., & Weir, R. (2025). The quoted sentence ("some distinguished neuroscientists … continued to defend dualism throughout the second half of the twentieth century") was grep-matched against the live page: verbatim. Revision date "Fri Oct 17, 2025" confirmed.
- Beck & Eccles 1992 (*PNAS* 89(23), 11357–11361) — real-correct; the body's "momentarily raises the probability of emission in the thousands of synapses on each pyramidal cell" follows the abstract ("momentary increases of the probability of vesicular emission in the thousands of synapses on each pyramidal cell").
- Eccles 1990 (*Proc. R. Soc. B* 240(1299), 433–451) — real-correct; "laminae V and III-II", "as described by Fleischhauer and Peters" and the dendron/psychon pairing all match the abstract.
- Blakemore, Wolpert & Frith 2002 (*TiCS* 6(6), 237–242) and Synofzik, Vosgerau & Newen 2008 (*Consciousness and Cognition* 17(1), 219–239) — real-correct at Crossref.
- Not re-checked, carried from the 2026-07-13, 2026-07-29 and 2026-09-04 ledgers: Penfield 1975, Penfield & Rasmussen 1950, Penfield & Jasper 1954, Popper & Eccles 1977, Eccles 1994, Bachmann/Suzuki/Aru 2020 (quote grep-verified 09-04), Suzuki & Larkum 2020, Dykstra et al. 2026.
- In-text ↔ References, by (surname, year), both directions: every in-text citation has an entry. Entries with no in-text (author, year) cite: Robinson & Weir (cited in the body by work title), Blakemore et al. 2002 and Synofzik et al. 2008 (cited by name with a year range and "in 2008"), the three Penfield books (cited by title and year), and the two Map self-citations. None is an orphan in substance.
- Superlatives: none needing a currency check.

### Critical Issues Found

1. **Evans et al. 2015 half-reported, and the comparator model misstated (fixed).** The section said Evans "found visual feedback dominating agency judgements", then argued that on the comparator model a decoded command "dispatches an efference copy, and should therefore arrive with agency attached", so that agency following the display marks a point where "the model owes a further account". Three problems. (a) The comparator model does not attach agency to the efference copy; it attaches it to a match between prediction and feedback, as the article's own earlier section says. (b) Evans report the comparator-consistent result first: discrepancies between decoded activity and feedback "are associated with a decrease in the SOA, similar to SOA mechanisms proposed for bodily actions". The anomaly is narrower: where the discrepancy corrects a poorly controlled action, the sense of agency "can be high and can increase with increasing discrepancy". (c) The "further account" is not owed; the paper supplies it, concluding that "cognitive, postdictive agency theories rather than predictive best account" for the data, or else multifactorial theories — citing Synofzik, Vosgerau & Newen 2008, which this article already cites. The paragraph now states both results, the study's design (healthy volunteers, EEG, imagined hand movement), and the authors' own conclusion, and says plainly that both kinds of account are physical. This strengthens the section's existing verdict that the dualist inference gains nothing here.
2. **Serino et al. 2022 overstated (fixed).** "Located the agency-monitoring signal … in primary motor cortex" read as a localisation finding. The abstract reports a single tetraplegic participant and says the authors "provide evidence that primary motor cortex processes sensory feedback, sensorimotor conflicts and subjective states of actions". Recording was from primary motor cortex, so the study cannot place the signal there as against elsewhere. Reworded to "working with one tetraplegic participant, reported evidence that primary motor cortex carries agency-related signals".

### Medium Issues Found

- SEP entry co-author missing (fixed; see ledger).
- "even where overt movement and proprioception are absent" presented the absence as an a fortiori circumstance; in the source it is the condition under which visual feedback dominates. Folded into the rewrite of issue 1.

### Checks run clean

- Map-internal glosses re-read against the pages as they stand today: [sherrington-dualist-lineage](/topics/sherrington-dualist-lineage/) ("agnostic pole", hedged, mechanism refused, mind's contact with brain not suspended), [filter-vs-interface-distinction](/concepts/filter-vs-interface-distinction/) (filter as inbound leg), the locked-in article (input arm dissociated from output). All agree.
- Editor-vocabulary leakage: none. "This is not X. It is Y." construct: none. "load-bearing": none.
- Calibration: no claim is graded above "suggestive"; the Relation to Site Perspective section keeps the endorsement framework-relative. Engagement with the comparator account: boundary-marking with an honest concession that the physical account fits the data (unchanged since 2026-07-13). No necessity vocabulary in the historical claims.
- Cited-author stance: Evans, Serino, Blakemore, Synofzik, Bachmann, Suzuki, Larkum and Dykstra are all presented as physicalist researchers drawing no dualist conclusion; the rewrite makes that explicit for the Evans result.

### Not verified at source

- Penfield's primary texts. An attempt to read *The Mystery of the Mind* on archive.org failed (the full-text files did not download). So the claims that Penfield "explicitly declined to specify the interaction mechanism", framed his case "primarily as a negative one", and used the programmer/computer analogy rest on earlier reviews and secondary carriage. One lead worth a check when the text is available: Penfield is often reported as speculating that the mind draws on a distinct form of energy, which would sit awkwardly beside "declined to specify"; this is recalled, not sourced, and nothing was changed on it.
- Popper & Eccles 1977 ("open cortical modules in the dominant hemisphere") and Eccles 1994: not re-read.
- Serino et al. 2022 full text.

## Optimistic Analysis Summary

### Strengths Preserved

- The lead's "suggestive rather than decisive" verdict and its front-loading.
- The refusal to reproduce variant patient quotations.
- "It cuts both ways, and the second edge is the sharper" in the dendron section, untouched.
- The inverse-case section's framing sentence (movement without authorship; authorship without movement) and its closing link to the outbound arm.

### Enhancements Made

- The inverse-case paragraph now reports what the study did and what its authors concluded, which ties it to the Synofzik account already named in the physicalist-reply section.

### Cross-links Added

- None.

## Length

concepts thresholds 2500 / 3500 / 5000. 2637 → 2636 words by analyze_length (soft_warning; length-neutral mode). The rewrite added about 55 words, funded by removing two restating sentences ("Between them they occupy the two halves of the interactionist case…", which repeated the paragraph's opening claim that the two are complementary; "Over-reading it as the latter is a standing risk", which repeated the sentence before it) and three small tightenings. No qualifier, objection-answering sentence, cited fact or reference was cut.

## Remaining Items

- topics/brain-computer-interfaces-and-the-interface-boundary L137 carries the same two descriptions this pass corrected here (Evans without the comparator-consistent half; Serino "found agency-monitoring signals … processed in primary motor cortex" without the single-participant scope).
- topics/sherrington-dualist-lineage L120 and voids/anesthesia-void L185 cite the SEP entry to Robinson alone.

## Stability Notes

The bedrock disagreement recorded on 2026-07-13 stands: physicalists read Penfield's data as a fact about agency machinery, and the article concedes it. Do not re-flag the underdetermination. The inverse-case section's verdict (the constraint bears on both readings; no support for the dualist inference) is a calibration the article has chosen and should not be strengthened. The Penfield primary-text claims remain uncertified at source; a future pass with access to the 1975 book should check them rather than treat them as settled.