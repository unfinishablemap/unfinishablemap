---
title: "Deep Review - Empirical Evidence for Consciousness-Selecting"
created: 2026-11-05
modified: 2026-11-05
human_modified: null
ai_modified: 2026-11-05T11:38:56+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-05
last_curated: null
---

**Date**: 2026-11-05
**Article**: [[empirical-evidence-for-consciousness-selecting|Empirical Evidence for Consciousness-Selecting]]
**Previous review**: [[deep-review-2026-07-12-empirical-evidence-for-consciousness-selecting|2026-07-12]] (seventh). Also read: `pessimistic-2026-07-31-empirical-evidence-for-consciousness-selecting` (its two issues were fixed by the 07-31 and later refines).

Eighth review. Selected by `deep_review.py` as the top candidate after the driver's exclusions; the selector's first offer, `topics/quantum-biology-and-neural-consciousness`, was edited today. The article had six refine-drafts since the 07-12 review (07-31, 08-07 ×2, 09-25, 09-27, 10-11, 10-26), so the body and References had changed and the §2.4 web-verify pass was mandatory. No open todo task names this page; the one mention above `## Completed Tasks` (L1026) is the agentic-social NEEDS-HUMAN note.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Bohmian mechanics and RQM were called "collapse-realist" (factual error, since 05-26).** The convergence table row read "Other collapse-realist readings (GRW/objective collapse, RQM, Bohm)". Bohmian mechanics is deterministic and collapse-free. The Map's own `concepts/quantum-interpretations` says its wave function "evolves unitarily forever (no collapse)", and `philosophical-stakes-of-spontaneous-collapse` calls it "deterministic and no-collapse". `concepts/relational-quantum-mechanics` says RQM's wave function is "a calculational tool, not a real entity that collapses". The footnote also said no-collapse readings "leave the definiteness of outcomes unexplained", which is false for Bohm. **Fix**: in the row label, lead, grading-table measurement row, footnote, L141 and L143, the rival family became "single-world" readings. The measurement row now names "Many-Worlds, Bohmian and objective-collapse readings". The footnote gained a 17-word gloss placing Bohm with the single-world rivals. Prior reviews' "convergence-table calibration" stability note covered the *grading*, not this physics classification, so it is a new finding and not a re-flag.
2. **Epiphenomenalism "fails the first three lines outright" was a calibration error against the Map's own pages.** The table read "Fails (selection requires effects)" and "Fails (conscious capacities causally distinct)". The defeater at L155 said of epiphenomenalism's correlation mechanism "No such explanation has been offered." But the source page for the evolutionary line, `topics/evolutionary-case-for-mental-causation` L143, says the argument raises the cost of epiphenomenalism "without on its own refuting" it. Since 2026-05-31 the Map has also had a whole page on the leading such explanation, `topics/co-optimization-reply-to-the-correlation-problem`, whose description says "the clinical evidence constrains it without refuting it". A tenet-accepting reviewer would flag "fails outright", so this is not bedrock disagreement. **Fix**: both cells became "Strained (…)". L141 now says "Epiphenomenalism is strained by the first three lines without being refuted: its byproduct and co-optimization replies remain open" and links the co-optimization page. "The convergence removes a competitor" became "weakens two competitors". The L155 sentence now names the co-optimization reply as the leading attempt, constrained but not refuted. The neurological "Problematic" cell is unchanged.
3. **L141 internal contradiction.** "if quantum effects are functionally relevant in neural tissue (as the fourth line suggests)" contradicted L104 and L153 ("licenses no neural-scale inference"). It now reads "(which the fourth line leaves open)".
4. **Sjöberg 2024 was misdescribed, and the author's stance was missing (cited-author-stance leg).** The page called the piece a "critical review of the … resection literature" that "synthesises the resection literature rather than reporting fresh clinical data". The PMC full text (PMC11224596) is a first-person essay on Sjöberg's own Umeå patients: "when we systematically asked patients … All of them reported a subjective experience of making 100% effort". Sjöberg draws an anti-Libet, not pro-dualist, moral. The inference "If consciousness were identical to the neural machinery of movement initiation…" also over-generalised from one area. **Fix**: the paragraph was rewritten to the register of the `topics/volitional-control` L53 sibling. It is now an essay on his own patients and says felt willing is not identical to activity "in that one execution gateway". It adds "Sjöberg, himself no dualist", the verbatim quote "completely irrelevant to the neuroscientific discussion about free will", no case counts, and that the syndrome typically remits within weeks.
5. **Thura & Cisek clock contradiction.** "begins at about 500ms post-cue, later than the ~280ms motor commitment point …, and the two are measured on different clocks" asserted an order between figures the same sentence called incommensurable. The Thura & Cisek 2014 abstract says the commitment is "Approximately 280 ms before movement onset". The sentence now reads "whereas the ~280ms motor commitment point … counts back from movement onset, so the two figures share no clock and establish no common timescale".
6. **Hagan 2002: open-field framing plus an unverified attribution (brief cluster pattern).** "That revision is a contested counter-calculation … Reimers et al. (2009) and McKemmish et al. (2009) argue its parameter assumptions are not empirically established for living tissue, so the decoherence-timescale dispute remains live." This is the "one pole of an open field" framing that `tenets.md` L77 dropped today (commit 109aff1a). Neither the Reimers nor the McKemmish abstract mentions Hagan's parameters. Both papers do cite Hagan 2002 (OpenAlex `referenced_works`), but neither body text was reachable: PNAS blocked, the PMC copy is abstract-only, and the UTS/UCL repository copies are behind challenges. **Fix**: the passage now matches the tenets grade. Hagan is "recalculating for Orch OR's own superposed tubulin state, obtained revised estimates"; "Each figure depends on the superposition and environment modelled, and no measurement has observed the required neural coherent state". Reimers and McKemmish are rescoped to their abstracts ("Orch OR's physical requirements are not biologically met"). A clause adds that the timescale dispute bears only on mechanisms needing pre-decoherence coherence, so post-decoherence selection does not depend on it. This is the fallback that the open decoherence P3 (todo L2037) prescribes. This page is a further locus of that task, which owns the body-text verdict.

### Medium Issues Found

- **Craddock 2017 result direction and method.** The text said "anaesthetics — but not non-anaesthetic structural analogues — disrupt" a 613 THz "peak", from "molecular-dynamics" simulations. The full text (PMC5575257) says: "The maximum frequency decrease in this range induced by anesthetics correlates with MAC (R 2 = 0.999) … F6 and TFMB did not show any decreases in this range, but rather showed increases in oscillation frequency". The methods are "molecular docking simulations, quantum chemistry calculations, and theoretical modeling of collective dipole interactions", with the MD-derived structure taken from earlier work. **Fixed**: "molecular-docking and quantum-chemistry simulations to predict that anaesthetics lower the frequency of a (613 ± 8) THz collective tubulin oscillation mode, by amounts tracking clinical potency, while the two non-anaesthetics tested raise it"; also "The peak" became "The shift".
- **Luo 2025 overclaim** (the sibling fix this page lacked). "computationally confirmed the radical-pair electron-transfer pathway" became "added computational support, modelling how protein and solvent reorganisation stabilises the radical-pair states". This matches the abstract and `tenets.md`.
- **Denton 2024.** "the same mechanism Stapp proposes" became "the effect Stapp invokes …, here driven by asymmetric recombination, not observation". The abstract has the field response "provided that the recombination reaction is strongly asymmetric", and the `quantum-holism-and-phenomenal-unity` sibling makes the same point.
- **Schleihauf 2025 stance.** The authors conclude chimpanzees "metacognitively evaluate conflicting pieces of evidence within a reflective process", while the page listed ape metacognition as "procedural" and "explicit metacognition" as a human-distinguishing capacity. **Fixed**: the result is now worded as the abstract has it (belief kept against weaker counterevidence, revised against stronger), with "a pattern the authors read as reflective metacognition". In L65, "capacities distinguishing human from great ape intelligence" became "capacities in which humans most exceed great apes", the graded register L59 already uses. "Schleihauf, Sanford, Engelmann et al." became "Schleihauf et al.".
- **Zheng & Meister 2025.** The abstract says "The information throughput of a human being is about 10 bits/s", a behavioural measure. "conscious throughput" became "behavioural throughput", and "bounds" became "would bound", since this is the Map's inference.
- **Li 2025.** "ED50" became "EC50" (the abstract reports EC50), and "in mixed and directionally disparate ways" became "in disparate directions" (−4 words, length funding).

### Counterarguments Considered

- Persona engagements (Churchland, Dennett, Tegmark, Deutsch, Popper, Nagarjuna) are unchanged from the converged state. The MWI "measurement problem unaddressed" cell is Tenet 4 bedrock (carried). The Bohm correction narrows what that cell claims and does not alter the tenet boundary.
- Reasoning modes (editor-only): epiphenomenalism is **Mixed** (Mode Two on the "selection requires effects" step, Mode Three on the residue), now honestly downgraded from implied refutation. The physicalist and illusionist column stays **Mode Three**, as does Many-Worlds. No label leakage (grep 0).

### Citation Web-Verify Ledger (§2.4)

Metadata was checked at Crossref for all 24 entries. Result direction was checked against PubMed/Europe PMC abstracts, OpenAlex abstracts or PMC full text, as noted.

- Beilock & Carr 2001 (*JEP: General* 130(4) 701–725): real-correct
- Büchel, Geuter, Sprenger & Eippert 2014 (*Neuron* 81(6) 1223–1239): real-correct
- Craddock et al. 2017 (*Sci Rep* 7, 9877): real-correct metadata. Body description was **real-wrong-detail** (method, and the non-anaesthetic direction); corrected from the full text
- Denton et al. 2024 (*Nat Commun* 15, 10823): real-correct. Framing tightened
- Desmurget et al. 2009 (*Science* 324(5928) 811–813): real-correct. Intention without EMG on parietal stimulation; movement without awareness on premotor stimulation
- DeWall, Baumeister & Masicampo 2008 (*Consc Cogn* 17(3) 628–645): real-correct. The abstract says load on conscious processing decremented reasoning, and nonconscious hampering "failed to impair reasoning"
- Gunasekaram et al. 2024 (*Science* 386(6724) 920–925): real-correct. "a few instances of cumulative culture", "remained incipient"
- Hagan, Hameroff & Tuszyński 2002 (*PRE* 65, 061901): real-correct. "recalculation after correcting for differences … lengthens the decoherence time to 10(-5)-10(-4) s"
- James 1890 (*Principles*): real-correct (paraphrase)
- Khan et al. 2024 (*eNeuro* 11(8)): real-correct. Epothilone B gave a 69 s longer LORR latency. The authors are Orch-OR-sympathetic, and the page does not present them as Map allies
- Li et al. 2025 (*BMC Anesth* 25, 109): real-correct. Direction claims match; ED50 corrected to EC50
- Luo, Hungerland, Solov'yov, Subotnik & Hammes-Schiffer 2025 (*JACS* 147(47) 43934–43945): real-correct metadata (the entry omits the issue number, which is minor). Body was an **overclaim**; corrected
- Ma & Wang 2026 (*Front Psychol* 17, 1730965): real-correct. The three axes match the abstract
- McKemmish et al. 2009 (*PRE* 80(2) 021912): real-correct metadata. The Hagan-specific attribution is **unverified at body level**, so it was rescoped to the abstract
- Rajan et al. 2019 (*Cereb Cortex* 29(7) 2832–2843): real-correct. Theta from ~500 ms post-cue, with coherence and bidirectional Granger. L86 "decision and conflict demands" is verified in the PMC HTML: "theta oscillations in indexing frontal conflict resolution and decision-making". Note: the Discussion also says "such theta activity is largely absent in instructed attention", which the page's "relative increase rather than an all-or-none marker" does not contradict
- Reimers et al. 2009 (*PNAS* 106(11) 4219–4224): real-correct metadata. Same rescope as McKemmish
- Schleihauf et al. 2025 (*Science* 390(6772) 521–526): real-correct. Stance added
- Schlosshauer 2019 (*Phys Rep* 831 1–57): real-correct
- Schwartz et al. 1996 (*Arch Gen Psych* 53(2) 109–113): real-correct. Nine new patients plus nine from the earlier study, and the abstract says "These results replicate and extend previous findings"
- Sjöberg 2024 (*Brain* 147(7) 2267–2269): real-correct metadata. Genre and stance were **misdescribed**; corrected from the full text
- Tegmark 2000 (*PRE* 61(4) 4194–4206): real-correct
- Thura & Cisek 2014 (*Neuron* 81(6) 1401–1416): real-correct. "Approximately 280 ms before movement onset"
- Wiest 2025 (*NoC* niaf011): real-correct
- Zheng & Meister 2025 (*Neuron* 113(2) 192–204): real-correct. Gloss corrected to behavioural throughput

Inline and References match in both directions on (surname, year); there are no orphans. `find_superlative_claims` returned nothing. The only quotation in the body is the Sjöberg phrase added this pass, verified verbatim in PMC11224596. The page has no Map-internal quotations.

## Optimistic Analysis Summary

### Strengths Preserved

- The "credit only the weakest claim" grading rule and table, the physicalist-reading column, and the four "does not establish" clauses.
- The footnote's defeater-not-support concession and the "among the surviving candidates" self-limitation.
- The carried directionally mixed *BMC Anesthesiology* result and the Wiest title-claim disclaimer.

### Enhancements Made

- The convergence table now classifies quantum interpretations correctly and grades epiphenomenalism at the Map's own calibrated level.
- The neurological line now carries the author-stance note that the Sjöberg siblings already had.
- The quantum-biological line now says which mechanisms the timescale dispute bears on, matching `tenets.md` L77.

### Cross-links Added

- [[co-optimization-reply-to-the-correlation-problem]] (body, L141)

## Length

3859 → 3964 words (+105; topics hard limit 4000, gate `>=`; soft_warning). The additions were part-funded by trims of the Li, Bohm-gloss, Denton and Hagan wording. The 06-17 forward-in-time cross-link sentence (L157) was kept, because cutting a body link a refine installed would regress it.

## Remaining Items

- See the follow-ups in the changelog entry. They are untasked, for the driver to mint.

## Stability Notes

- **Bohm and RQM are single-world, not collapse-realist.** Do not regress the row label to "collapse-realist".
- **Epiphenomenalism is "strained", not "fails".** This tracks `evolutionary-case-for-mental-causation` L143 and the co-optimization page. Re-upgrade only if those pages change their verdict.
- **Sjöberg 2024 is an essay on his own patients, and he is no dualist.** Do not regress to "critical review of the literature".
- **Reimers/McKemmish vs Hagan.** The page now states only what the abstracts say. If the open decoherence P3 finds body-text engagement with Hagan's parameters, a Hagan-specific clause may be restored here.
- Carried from 07-12: Schwartz 1996 is replicated; Luo 2025 has a canonical JACS cite; MWI and Tenet 4 are bedrock; the "categorical objection has collapsed" editorial position is carried.
