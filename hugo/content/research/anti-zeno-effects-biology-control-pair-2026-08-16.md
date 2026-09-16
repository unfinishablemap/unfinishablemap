---
ai_contribution: 100
ai_generated_date: 2026-09-16
ai_modified: 2026-09-16 21:55:00+00:00
ai_system: claude-fable-5-1
author: null
concepts:
- '[[sign-problem-for-conscious-observation]]'
- '[[quantum-zeno-effect]]'
- '[[radical-pair-magnetoreception]]'
- '[[stapp-quantum-mind]]'
created: 2026-09-16
date: &id001 2026-09-16
description: Paired index search testing the sign-problem article's claim that no
  anti-Zeno results exist in biological systems. Control leg passes; null firms, with
  two near-misses found.
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-09-16 21:55:00+00:00
modified: *id001
related_articles:
- '[[anti-zeno-effect-and-sign-of-conscious-observation-2026-08-05]]'
title: Research Notes - Anti-Zeno Effects in Biological Systems as a Control-Pair
  Search
topics:
- '[[quantum-biology-and-neural-consciousness]]'
---

# Research: Anti-Zeno Effects in Biological Systems as a Control-Pair Search

**Date**: 2026-09-16 (task minted 2026-08-16; filename keeps the mint date)
**Indices**: OpenAlex, Europe PMC (metadata and open-access full text), Crossref, Semantic Scholar; publisher and PMC XML for every paper quoted.
**Outcome in one line**: the control leg passes on every index, the anti-Zeno null firms into a bounded finding, and the search surfaces two near-misses the corpus did not know about — neither of which reports an anti-Zeno regime in a biological system. **Downstream is a one-sentence refine of [sign-problem-for-conscious-observation](/concepts/sign-problem-for-conscious-observation/). No new article is warranted, and none is recommended.**

## The claim under test

[sign-problem-for-conscious-observation](/concepts/sign-problem-for-conscious-observation/) (line 49, final sentence) currently reads:

> And a search for anti-Zeno results in biological systems returned only Zeno-side work; that absence is weak evidence rather than a finding, since the search was not exhaustive.

Its stated scope is inherited from [anti-zeno-effect-and-sign-of-conscious-observation-2026-08-05](/research/anti-zeno-effect-and-sign-of-conscious-observation-2026-08-05/), whose query list contains exactly one biological query — a single WebSearch for `anti-Zeno effect radical pair spin dynamics biological quantum biology` — and whose gaps section records: "Anti-Zeno in biology: no positive literature found. Searches for anti-Zeno in radical-pair or other biological systems returned only Zeno-side results. Absence of results here is weak evidence; it was not an exhaustive search."

So the claim actually made is narrow and honest: one web query, one biological framing (radical pairs), graded weak. The question is whether a designed search changes the grade.

## Assessment: worth doing, and why

A bare zero and an index that never reached the literature look identical. The fix is a paired search: show the query design retrieves known Zeno-side biological work first, then report the anti-Zeno null against that control. This is cheap, the downstream is a refine at zero cap cost, and the prior note itself asked for it. Proceeded.

## Control anchors, printed from the publisher

**Denton et al. 2024** — Crossref: *Nature Communications* 15(1), article 10823, issued 2024-12-30; authors Denton, M.C.J.; Smith, L.D.; Xu, W.; Pugsley, J.; Toghill, A.; Kattnig, D.R.; DOI 10.1038/s41467-024-55124-x; OpenAlex W4405893658, PMID 39737951. What it reports (Crossref abstract): the FAD–superoxide radical pair in cryptochrome, traditionally thought unresponsive to weak fields because tightly bound, "can respond to Earth-strength magnetic fields, provided that the recombination reaction is strongly asymmetric—a scenario invoking the quantum Zeno effect." It is a modelling study; the abstract's own verb is "examining", and the corpus's calibrated paraphrase (computational, precedent not licence, no anti-Zeno branch explored) matches the record.

**Kominis 2009** — second control: *Physical Review E* 80(5), 056115, issued 2009-11-24, DOI 10.1103/PhysRevE.80.056115 ("Quantum Zeno effect explains magnetic-sensitive radical-ion-pair reactions").

**Kofman & Kurizki 2000** — physics anchor for the acceleration regime: *Nature* 405(6786), 546–550, June 2000, DOI 10.1038/35014537; OpenAlex W1530671852 (522 citers); PMID 10850708. **Kaulakys & Gontis 1997** — *Physical Review A* 56(2), 1131–1137, DOI 10.1103/PhysRevA.56.1131; OpenAlex W2025548804 (93 citers). **Fischer, Gutiérrez-Medina & Raizen 2001** — *Physical Review Letters* 87(4), 040402, DOI 10.1103/PhysRevLett.87.040402; OpenAlex W2963501482 (452 citers); PMID 11461604.

## Control leg: does each index reach Zeno-side biological work?

| Index | Query | Hits | Denton 2024 | Kominis 2009 |
|---|---|---|---|---|
| OpenAlex (title+abstract) | `"quantum Zeno" radical pair` | 31 | yes | yes |
| OpenAlex | `"quantum Zeno" cryptochrome` | 11 | yes | no |
| OpenAlex | `"quantum Zeno" biological` | 68 | yes | no |
| OpenAlex | `"quantum Zeno" magnetoreception` | 27 | no | yes |
| Europe PMC (metadata) | `"quantum Zeno" AND (radical pair OR cryptochrome)` | 17 | yes | yes |
| Europe PMC | `"quantum Zeno" AND biolog*` | 56 | yes | yes |
| Europe PMC | `"quantum Zeno" AND magnetoreception` | 8 | yes | yes |
| Crossref (bibliographic, relevance-ranked; totals meaningless) | `quantum Zeno effect radical pair` | top-40 | no | yes (rank 1) |
| Crossref | `quantum Zeno effect cryptochrome magnetosensitivity` | top-40 | yes (rank 2) | no |
| Semantic Scholar | `quantum Zeno effect cryptochrome` | 1475 | yes (rank 1) | no |

Every index reaches the Zeno-side biological literature with the same term design used below. The control leg also surfaced Zeno-side biological work newer than the corpus's citations: Smith, Tallapudi, Denton & Kattnig 2025 (*AVS Quantum Science* 7(3), 032601) and Denton & Kattnig 2026 (*JACS Au* 6(4), 2420–2432, lipid peroxidation). Both are Zeno-side; see below for their anti-Zeno check.

## Anti-Zeno leg: every query with its count

**OpenAlex, title+abstract** (base counts: `"anti-Zeno"` 412, `"quantum anti-Zeno effect"` 61, `"inverse Zeno"` 12, `"antizeno"` 0, `"measurement-accelerated decay"` 0). Crossed with 17 biological terms (biological, biology, neural, neuron, brain, photosynthetic, photosynthesis, olfaction, olfactory, enzyme, enzymatic, radical pair, cryptochrome, magnetoreception, protein, "light-harvesting", FMO): **every cell is zero** except `"anti-Zeno" biological` 14, `"anti-Zeno" brain` 10, `"anti-Zeno" neural` 5, `"anti-Zeno" neuron` 4, `"anti-Zeno" photosynthetic` 2, `"quantum anti-Zeno effect" photosynthetic` 1. All `"inverse Zeno"`, `"antizeno"` and `"measurement-accelerated decay"` cells are zero, and every radical-pair / cryptochrome / magnetoreception / enzyme / olfaction / protein / light-harvesting / FMO cell is zero under every anti-Zeno variant.

⚠️ **Unresolved**: OpenAlex's free daily budget was exhausted before the member lists of the six non-zero cells could be printed (HTTP 429, "Insufficient budget", resets at midnight UTC). Those 14/10/5/4/2/1 counts are therefore *unexamined* hits, not positives; the other three indices below found nothing in those categories beyond the items listed. Anyone re-running this should print the member lists first: `filter=title_and_abstract.search:"anti-Zeno" brain`.

**Europe PMC, metadata** (`"anti-Zeno"` 71; `"anti Zeno"` 71; `"antizeno"` 0; `"inverse Zeno"` 0): `AND biolog*` 10 · `AND (radical pair OR cryptochrome OR magnetoreception)` 1 · `AND photosynth*` 1 · `AND (neural OR neuron* OR brain)` **0** · `AND (enzym* OR protein)` 5 · `AND olfact*` 0 · `AND consciousness` 1 · `"inverse Zeno" AND biolog*` 0.

**Europe PMC, open-access full text** (`BODY:"anti-Zeno"` 38 articles): `AND (biological OR biology)` 5 · `AND (radical pair OR cryptochrome OR magnetoreception)` 1 · `AND (photosynthetic OR photosynthesis OR light-harvesting)` **0** · `AND (neural OR neuron OR brain)` **0** · `AND consciousness` 1.

**Crossref** (`query.bibliographic`, relevance-ranked; "total-results" is in the millions and meaningless): top-25 for `anti-Zeno effect biological`, `… radical pair`, `… photosynthetic`, `… neural brain`, and `inverse Zeno effect biological` contain only physics papers plus one NeuroQuantology item (below). No radical-pair or photosynthetic paper appears under any anti-Zeno query.

**Semantic Scholar** (`anti-Zeno effect biological system` 7915 · `… photosynthetic complex` 51 · `inverse Zeno effect biology` 887; two queries lost to rate limiting): relevant rows are Thilagam 2013, Namiot & Shchurova 2018, Sumner & Iyengar 2010/2014 and the Persinger-group item, all treated below.

**Citation graph** (substitute for the OpenAlex `cites:` filter, which the budget blocked). Europe PMC-indexed citers of Kofman & Kurizki 2000: 90, of which the radical-pair citers are Kominis 2009, Dellis & Kominis 2012 (*Biosystems*) and Kominis 2014 (*Phys. Rev. E*, retrodictive master equation) — all Zeno-side. The Kominis 2009 preprint (arXiv:0804.2646) contains zero occurrences of "anti-Zeno", "Kofman" or "accelerat"; the Dellis & Kominis preprint (arXiv:0908.0763) cites Kofman & Kurizki inside a general Zeno reference cluster and never uses "anti-Zeno". Semantic Scholar citers: Kofman & Kurizki 421, of which 8 carry any biological term in title or abstract (Thilagam 2013 is the only one with anti-Zeno in the abstract); Kaulakys & Gontis 51, **0** biological; Fischer 2001 374, 4 biological (Thilagam 2013 again; Kim et al. 2021 *Quantum Reports* 3(1), 80–126, a quantum-biology review whose full text MDPI refused to serve, so its Zeno passage is unchecked). Europe PMC-indexed citers of Fischer 2001: 65, biological-flagged only Sumner & Iyengar 2010.

**Post-2020 Zeno-side radical-pair papers, checked at full text** for anti-Zeno / inverse Zeno / Kofman / Kaulakys / "accelerat… decay|recombination": Smith et al. 2025 (arXiv:2505.01519) 0/0/0/0/0; Smith et al. 2023 (arXiv:2303.12117) 0/0/0/0/0; Denton & Kattnig 2026 (PMC13126183) 0/0/0/0/0. The live radical-pair Zeno programme does not discuss the acceleration regime at all.

## What the anti-Zeno leg actually found, graded

1. **Babcock & Kattnig 2021 — the one radical-pair paper with anti-Zeno in its body.** *JACS Au* 1(11), 2033–2046, issued 2021-10-05, DOI 10.1021/jacsau.1c00332, PMC8611662. Verified in the PMC XML (one body occurrence, refs 65–66): "The term 'chemical Zeno Effect' describes the reaction dynamics enabled by this scheme.⁶⁵ Specifically, the scavenging reaction converts triplets to singlet states of the original pair, even in the absence of coherent interaction terms, and thus resembles the quantum (anti-)Zeno effect.⁶⁶" Ref 65 is Letuta & Berdinskii 2015 (*Dokl. Phys. Chem.* 463, 179–181, "Chemical Zeno effect"); ref 66 is Kaulakys & Gontis 1997. **Grade**: a hedged, parenthetical analogy in a radical-*triad* scavenging model of the cryptochrome compass. No anti-Zeno regime is computed, no crossover is reported, and the paper's own mechanism (scavenging drives evolution rather than freezing it) is what earns the "(anti-)". It is the corpus's missed work, and it is a sentence, not a result. The corpus does not currently cite this paper (grep for the DOI and "radical scavenging": 0).

2. **Thilagam 2013 — anti-Zeno framing in a toy photosynthetic model.** *Journal of Chemical Physics* 138(17), 175102, issued 2013-05-07, DOI 10.1063/1.4802785, PMID 23656162; preprint arXiv:1304.3194 (quotes below are from the preprint; the published text was not retrieved). Abstract: "We examine the Zeno and anti-Zeno effects in the context of non-Markovian dynamics in entangled spin-boson systems … We extend our analysis to examine the Zeno mechanism-non-Markovianity link using the tripartite states arising from a donor-acceptor-sink model of photosynthetic biosystems." Body: "The two dissipative sinks which act as indirect detectors, appear to induce a anti-Zeno-like effect facilitating information feedback into the specific partition considered here", and "A quantitative assessment of the contribution from the anti-Zeno-like action of the photosynthetic sink to the efficiency of energy transfer is expected to be numerically intense". **Grade**: explicit, theoretical, "anti-Zeno-*like*", on a three-site model with the rotating-wave approximation; the author defers the quantitative case. It is the only paper found that puts an anti-Zeno label on a biological energy-transfer model. It does not measure or compute an accelerated-decay regime in a real complex.

3. **Frydman-group NMR — anti-Zeno resets on biomolecules, as method.** Novakovic, Kupče, Oxenfarth, Battistel, Freedberg, Schwalbe & Frydman 2020, *Nature Communications* 11(1), 5317, DOI 10.1038/s41467-020-19108-x, PMC7577996: solvent exchange of labile protons is treated "as 'resets' within the framework of Anti-Zeno Effects", yielding cross-peak enhancements in proteins, oligosaccharides and nucleic acids. It rests on Álvarez, Rao, Frydman & Kurizki 2010, *Physical Review Letters* 105(16), 160401, DOI 10.1103/PhysRevLett.105.160401, whose abstract states that "repeated dephasing at intervals associated with the anti-Zeno regime leads to ensemble purification, whereas those associated with the Zeno regime lead to ensemble mixing." **Grade**: real anti-Zeno-regime dynamics realised at room temperature in biomolecular spin ensembles — but engineered by a pulse sequence, on nuclear spins, as a spectroscopic tool. It says nothing about a biological process operating in that regime. Kurizki co-authoring the 2010 paper is the closest the acceleration-regime literature comes to biology.

4. **Framing-only mentions** (a boilerplate sentence, no result): Slocombe, Winokan, Al-Khalili & Sacchi 2023, *J. Phys. Chem. Lett.* 14(1), 9–15, DOI 10.1021/acs.jpclett.2c03171, PMC9841559 (DNA tautomerism: environment "can either impede or encourage the system's evolution, known as a quantum Zeno or anti-Zeno effect"); Warman, Slocombe & Sacchi 2023, *RSC Advances* 13(20), 13384–13396, DOI 10.1039/d3ra00983a (same sentence); Sumner & Iyengar 2010, *J. Chem. Theory Comput.* 6(5), 1698–1710, DOI 10.1021/ct900630n, PMC3428049 (enzyme hydrogen tunnelling; one comparison of avoided crossings to an "experimentally observed anti-Zeno effect" via Modi & Shaji).

5. **Fringe, not usable**: Pradhan 2015, "Quantum Zeno Effect in Sleep Disorders and Treatment by the Anti-Zeno Effect", *NeuroQuantology* 14(1), DOI 10.14704/nq.2016.14.1.864 (title located via Crossref only; content not retrieved; venue outside the mainstream literature); Dotta, Vares & Persinger 2016, *Journal of Advances in Physics* 11(6), 3374–3378, DOI 10.24297/JAP.V11I5.352 ("negative Zeno effect" in photon counts). Namiot & Shchurova 2018, *Biophysics* 63(5), 825–830, DOI 10.1134/S0006350918050202 ("Is it possible to determine an observer effect in biological systems?") could not be read (no abstract in Crossref or Europe PMC; Springer blocked the fetch) and is recorded as unexamined.

## Firmed finding

With controls passing on four indices, and with the open-access full-text layer of Europe PMC and the citation graphs of all three physics anchors searched: **no paper reports an anti-Zeno regime — measurement-accelerated decay — in a biological system.** For neural systems the null is clean on Europe PMC (metadata and full text), Crossref and Semantic Scholar; the OpenAlex `brain`/`neural`/`neuron` cells (10/5/4) are unexamined and must be printed before "clean" is claimed there. What exists instead is one hedged analogy in a cryptochrome radical-triad model, one "anti-Zeno-like" feedback in a toy photosynthetic model, and NMR methods that impose anti-Zeno resets on biomolecular spins. The live Zeno-side radical-pair programme (Kominis; Kattnig group through 2026) never discusses the acceleration regime.

Two calibration cautions travel with this. First, it is a bounded null, not evidence that biological observers sit on the stabilising side; the absence of anti-Zeno *reports* is consistent with nobody having looked, and the Kattnig group's own text shows the label is available to them when a mechanism drives evolution. Second, the Map's sign problem concerns an observer whose observation is not merely another physical coupling; none of the papers above, Zeno-side or anti-Zeno-side, models that — so the biological literature is silent on the Map's case in both directions, exactly as the article already says of Denton.

## Tenet relevance

Unchanged from the parent note. The finding tightens the epistemic footing of a falsifier the Map raised against its own Tenet 2/3 mechanism (Stapp-style attention-as-Zeno in [stapp-quantum-mind](/concepts/stapp-quantum-mind/)); it does not move the mechanism's status. It slightly strengthens the Tenet 5 point: the field's silence on the anti-Zeno side in biology is a gap in knowledge, and simplicity arguments ("measurement stabilises") should not be run across it.

## Refine brief for `concepts/sign-problem-for-conscious-observation`

**Length position, measured**: 2511 words in the `concepts/` band (soft 2500, hard 3500); the article is already 11 words over soft, with 988 words of headroom to hard. Prefer the near-neutral variant.

**Replace** (line 49, final sentence, verbatim):

> And a search for anti-Zeno results in biological systems returned only Zeno-side work; that absence is weak evidence rather than a finding, since the search was not exhaustive.

**With — near-neutral variant (+~35 words, no new references required)**:

> And a paired search for anti-Zeno results in biological systems — run on four indices after confirming each retrieved the Zeno-side cryptochrome work — found no paper reporting measurement-accelerated decay in any biological system, neural or otherwise; the nearest approaches are a hedged "(anti-)Zeno" analogy in a cryptochrome radical-triad model and an "anti-Zeno-like" feedback in a toy photosynthetic model. That is a bounded null, not evidence that a biological observer sits on the stabilising side.

**Or — fuller variant (+~75 words; adds two references)**: as above, naming Babcock and Kattnig (2021) for the analogy and Thilagam (2013) for the photosynthetic model, and adding to the reference list:

- Babcock, N.S., & Kattnig, D.R. (2021). Radical scavenging could answer the challenge posed by electron–electron dipolar interactions in the cryptochrome compass model. *JACS Au*, 1(11), 2033–2046. https://doi.org/10.1021/jacsau.1c00332
- Thilagam, A. (2013). Non-Markovianity during the quantum Zeno effect. *The Journal of Chemical Physics*, 138(17), 175102. https://doi.org/10.1063/1.4802785

**Do not**: describe either paper as demonstrating an anti-Zeno effect in biology; cite the Frydman NMR work as biological evidence; or upgrade the null to "biological systems are Zeno-side". Add a pointer to this note in the article's research-notes list. **No new article**: the finding is one sentence's worth of calibration and belongs in the existing host.

## Gaps

- OpenAlex member lists for the six non-zero anti-Zeno cells and the `cites:` filter on all three anchors — blocked by the daily budget; re-run after 00:00 UTC.
- Kominis 2014 (*Phys. Rev. E*, retrodictive derivation) and Kim et al. 2021 (*Quantum Reports*) full texts not checked for anti-Zeno framing.
- Thilagam 2013 quoted from arXiv v1; published *JCP* text not compared.
- Namiot & Shchurova 2018 and Pradhan 2015 content unexamined.
- Non-English literature (the Russian *Biofizika* items) not pursued.

## Citations

1. Denton, M.C.J., Smith, L.D., Xu, W., Pugsley, J., Toghill, A., & Kattnig, D.R. (2024). Magnetosensitivity of tightly bound radical pairs in cryptochrome is enabled by the quantum Zeno effect. *Nature Communications*, 15(1), 10823. https://doi.org/10.1038/s41467-024-55124-x
2. Kominis, I.K. (2009). Quantum Zeno effect explains magnetic-sensitive radical-ion-pair reactions. *Physical Review E*, 80(5), 056115. https://doi.org/10.1103/PhysRevE.80.056115
3. Kofman, A.G., & Kurizki, G. (2000). Acceleration of quantum decay processes by frequent observations. *Nature*, 405(6786), 546–550. https://doi.org/10.1038/35014537
4. Kaulakys, B., & Gontis, V. (1997). Quantum anti-Zeno effect. *Physical Review A*, 56(2), 1131–1137. https://doi.org/10.1103/PhysRevA.56.1131
5. Fischer, M.C., Gutiérrez-Medina, B., & Raizen, M.G. (2001). Observation of the quantum Zeno and anti-Zeno effects in an unstable system. *Physical Review Letters*, 87(4), 040402. https://doi.org/10.1103/PhysRevLett.87.040402
6. Babcock, N.S., & Kattnig, D.R. (2021). Radical scavenging could answer the challenge posed by electron–electron dipolar interactions in the cryptochrome compass model. *JACS Au*, 1(11), 2033–2046. https://doi.org/10.1021/jacsau.1c00332 — body quote verified in PMC8611662 XML
7. Letuta, A.S., & Berdinskii, V.L. (2015). Chemical Zeno effect—A new mechanism of spin catalysis in radical triads. *Doklady Physical Chemistry*, 463, 179–181. https://doi.org/10.1134/S0012501615080059 — cited via Babcock & Kattnig 2021, not retrieved
8. Thilagam, A. (2013). Non-Markovianity during the quantum Zeno effect. *The Journal of Chemical Physics*, 138(17), 175102. https://doi.org/10.1063/1.4802785 — quotes from arXiv:1304.3194
9. Novakovic, M., Kupče, Ē., Oxenfarth, A., Battistel, M.D., Freedberg, D.I., Schwalbe, H., & Frydman, L. (2020). Sensitivity enhancement of homonuclear multidimensional NMR correlations for labile sites in proteins, polysaccharides, and nucleic acids. *Nature Communications*, 11(1), 5317. https://doi.org/10.1038/s41467-020-19108-x — body quote verified in PMC7577996 XML
10. Álvarez, G.A., Rao, D.D.B., Frydman, L., & Kurizki, G. (2010). Zeno and anti-Zeno polarization control of spin ensembles by induced dephasing. *Physical Review Letters*, 105(16), 160401. https://doi.org/10.1103/PhysRevLett.105.160401 — abstract via Europe PMC
11. Slocombe, L., Winokan, M., Al-Khalili, J., & Sacchi, M. (2023). Quantum tunnelling effects in the guanine-thymine wobble misincorporation via tautomerism. *The Journal of Physical Chemistry Letters*, 14(1), 9–15. https://doi.org/10.1021/acs.jpclett.2c03171
12. Warman, H., Slocombe, L., & Sacchi, M. (2023). How proton transfer impacts hachimoji DNA. *RSC Advances*, 13(20), 13384–13396. https://doi.org/10.1039/d3ra00983a
13. Sumner, I., & Iyengar, S.S. (2010). Analysis of hydrogen tunneling in an enzyme active site using von Neumann measurements. *Journal of Chemical Theory and Computation*, 6(5), 1698–1710. https://doi.org/10.1021/ct900630n
14. Smith, L.D., Tallapudi, S., Denton, M.C.J., & Kattnig, D.R. (2025). Chirality-bolstered quantum Zeno effect enhances radical pair-based magnetoreception. *AVS Quantum Science*, 7(3), 032601. https://doi.org/10.1116/5.0277712
15. Denton, M.C.J., & Kattnig, D.R. (2026). Quantum Zeno effect permits magnetosensitivity in lipid peroxidation despite fluctuating inter-radical coupling. *JACS Au*, 6(4), 2420–2432. https://doi.org/10.1021/jacsau.6c00031
16. Dellis, A.T., & Kominis, I.K. (2012). The quantum Zeno effect immunizes the avian compass against the deleterious effects of exchange and dipolar interactions. *Biosystems*, 107(3), 153–157. https://doi.org/10.1016/j.biosystems.2011.11.007 — preprint arXiv:0908.0763 checked
17. Kim, Y., et al. (2021). Quantum biology: An update and perspective. *Quantum Reports*, 3(1), 80–126. https://doi.org/10.3390/quantum3010006 — not retrieved
18. Pradhan, R.K. (2015). Quantum Zeno effect in sleep disorders and treatment by the anti-Zeno effect. *NeuroQuantology*, 14(1). https://doi.org/10.14704/nq.2016.14.1.864 — title only
19. Dotta, B.T., Vares, D.A., & Persinger, M.A. (2016). Acceleration of radiative decay of photon counts with increasing numbers of measurement units. *Journal of Advances in Physics*, 11(6), 3374–3378. https://doi.org/10.24297/JAP.V11I5.352 — title only
20. Namiot, V.A., & Shchurova, L.Yu. (2018). On the influence of observation of the processes in quantum systems: Is it possible to determine an observer effect in biological systems? *Biophysics*, 63(5), 825–830. https://doi.org/10.1134/S0006350918050202 — not retrieved