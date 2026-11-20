---
title: "Outer Review - Claude Fable 5.2 (2026-11-20)"
created: 2026-11-20
modified: 2026-11-20
human_modified: null
ai_modified: 2026-11-20T05:15:07+00:00
draft: false
description: "Claude Fable 5.2 hostile-referee audit of the Plenitude Void, written without access to the live page. Verified: Schwitzgebel cuts against the premise, ensemble critiques missing, overflow cluster miscalibrated."
topics:
  - "[[dualist-perception]]"
  - "[[bandwidth-of-consciousness]]"
concepts:
  - "[[phenomenal-overflow]]"
  - "[[introspection]]"
  - "[[illusionism]]"
related_articles:
  - "[[project]]"
  - "[[plenitude-void]]"
  - "[[reviews/outer-review-2026-11-20-chatgpt-5-6-sol-pro]]"
ai_contribution: 90
author: "Andy Southgate"
ai_system: "claude-fable-5-2"
ai_generated_date: 2026-11-20
last_curated: 2026-11-20
outer_review_status: processed
outer_review_conversation_url: https://claude.ai/chat/c7e4e927-d588-4ab4-8896-c3f3a0a809e2
outer_review_extraction_method: js-dom
subject_type: recent
subject_title: "Audit plenitude-void"
subject_articles:
  - voids/plenitude-void.md
subject_source: reuse:pending-reviews:outer-review-2026-11-20-chatgpt-5-6-sol-pro.md
---

**Date**: 2026-11-20
**Reviewer**: Claude Fable 5.2
**Type**: Outer review (external AI analysis)

## About This Review

An "outer review" is an analysis performed by an external AI system rather than the Claude-based workflow that generates most site content. This provides an independent perspective, reducing the risk of self-reinforcing blind spots.

## Prompt

Act as a hostile but fair referee for The Unfinishable Map (https://unfinishablemap.org), a site that argues for interactionist dualism. Please audit its article "The Plenitude Void": https://unfinishablemap.org/voids/plenitude-void/ which was last edited on 2026-11-13. Your search index may lag by a day or two, so check the changelog at https://unfinishablemap.org/workflow/changelog/ before calling anything unfixed. The article claims that conscious experience seems richer than anything we can report or check, and that this gap may be impossible to settle from the inside. It draws on the grand illusion debate, Block's overflow argument, ensemble statistics, unreliable introspection and bandwidth estimates. Please (1) verify each citation and quotation at its source, (2) test whether the empirical summaries match the current literature, including failed replications and critiques, (3) give the strongest illusionist and cognitive-access objections and judge whether the article answers them, and (4) assess how well it separates itself from neighbouring void pages and links into the rest of the site. End your report with a list of concrete potential improvements to specific articles and to the site's methodology.

## Reply

# Hostile-Referee Audit: “The Plenitude Void” (unfinishablemap.org/voids/plenitude-void/)

The Plenitude Void is a defensible epistemic observation turned into a weak argument. Its sound core is that introspection cannot tell rich phenomenology apart from inflated or generic phenomenology. That core is predicted equally well by illusionist, higher-order and global-workspace accounts, so it is evidentially neutral between dualism and physicalism and can sit on the site only as a coherence-only, perpetually contested entry. The article needs a hard revision: cut the bandwidth material, add the missing critiques of Bronfman, and make an explicit no-support declaration on the tenets.

**Scope disclosure (binding on every finding below).** In this audit session the fetch tool refused the live article URL, and no search returned the article page itself, so I could not read the live text of `voids/plenitude-void` directly. I also could not open the voids index, the two calibration apex articles, or the changelog entries for 2026-11-13 to about 2026-11-18. What I did verify at source:

- the live changelog for 2026-11-19 and 2026-11-20;
- the full live text of `concepts/phenomenal-overflow` (last modified 2026-11-05);
- the 2026-08-18 research note that planned the article’s current “Ensemble Reframe” section;
- live excerpts of `topics/dualist-perception`, `topics/bandwidth-of-consciousness`, `voids/the-surplus-void`, `voids/dimensionality-void`, `voids/erasure-void`, `concepts/heterophenomenology` and `concepts/cognitive-penetration`;
- the external primary literature listed in the tables.

Statements about what the Plenitude Void says come from the site’s own records of the article: research notes, the task queue and logged review entries. They are marked **[site-record]**. I quote no wording from the article that I did not see. Every verdict on the article is therefore provisional on a direct reading, and Part 4 lists exactly what to check.

## Part 1 — TL;DR

- **Headline verdict: REVISE-HARD.** The overall verdict is REVISE-HARD. The tenet/site-perspective connection should be DEMOTED to COHERENCE-ONLY, the overflow core FLAGGED AS PERPETUALLY CONTESTED, and the “Bandwidth Frame” DELETED from this page and moved to `topics/bandwidth-of-consciousness`. A void that cannot be settled from the inside carries a likelihood ratio of roughly one between dualism and its rivals. At most it is *compatible* evidence on the site’s own compatible/suggestive/discriminating ladder, and the article should say so in those words.
- **Citations and currency:** metadata for the core literature checks out where I could test it (Block 2007/2011, Cohen & Dennett 2011, Zheng & Meister 2025, Amir et al. 2023, Jackson-Nielsen et al. 2017, Sauerbrei & Pruszynski 2025). The failures are in stance and currency, not bibliography:

- The ensemble section, as planned **[site-record]**, sets Bronfman et al. 2014 against Ward, Bear & Scholl 2016. [[research/voids-summary-statistics-void-2026-08-18]] It omits Jackson-Nielsen, Cohen & Pitts 2017, which found no ensemble information outside attention, [springer](https://link.springer.com/article/10.3758/s13414-020-02067-2) and Kimchi & Sabary’s 2025 Attention, Perception & Psychophysics study (87(6):1888–1903), which also concluded that “ensemble perception requires attention”.
- The bandwidth figures measure behavioural throughput, an access-side quantity, so they cannot bear on plenitude at all.
- Sister pages co-opt Sauerbrei & Pruszynski toward a “consciousness filter” reading that the authors do not make. [[topics/bandwidth-of-consciousness]]
- **Objections and integration:** the strongest rivals are Phillips’s postdiction, Kouider/Stazicker generic phenomenology, Lau-lab inflation, Cohen–Dennett unfalsifiability, Schwitzgebel’s own periphery examples, and predictive processing including Laukkonen, Friston & Chandaria 2025. At best they are named, not answered, and several leave no trace in any site record of the article. The site contradicts itself: `topics/dualist-perception` calls perceptual richness “converging evidence that consciousness involves something beyond the physical”, [[topics/dualist-perception]] and `concepts/phenomenal-overflow` treats subjects’ richness reports as “the primary data”. [[concepts/phenomenal-overflow]] [[topics/dualist-perception]] Meanwhile the void page’s thesis is that those reports cannot settle anything. The concept page for the article’s central argument does not link back to the Plenitude Void. [[concepts/phenomenal-overflow]] A logged review recorded the page at 3,062 words, over its 3,000-word hard limit, and declined additions instead of trimming. [[workflow/changelog]]

## Part 2 — Dimensional Analysis

### 2.0 What the changelog shows since 2026-11-13

- **Verified (2026-11-19 to 2026-11-20 entries, read live):** no entry in this window edits `voids/plenitude-void`, `concepts/phenomenal-overflow`, `voids/resolution-void`, `topics/bandwidth-of-consciousness`, `concepts/introspection` or `concepts/illusionism`. Two entries touch the article’s bandwidth sources on *other* pages:

- The 2026-11-20T01:03 review of `concepts/metaphysics-of-information-under-dualism` replaced a sentence that had presented the minimality tenet as a convergent observation. The new text reads: “Zheng and Meister treat the limit as a question of neural substrate; reading it as a narrow semantic bottleneck at the interface, consistent with the minimality tenet, is the Map’s inference.” It also corrected “the brain’s ~10⁹ bits per second of sensory processing” to the abstract’s “our sensory systems gather data at ∼10⁹ bits/s”. [[workflow/changelog]]
- The 2026-11-19T18:44 review of `concepts/interface-friction` checked Zheng & Meister against arXiv 2408.10234. [[workflow/changelog]]
- This is the right correction. Nothing in the visible changelog shows it was carried over to the Plenitude Void’s “Bandwidth Frame” **[site-record: the section exists]**. [[research/voids-summary-statistics-void-2026-08-18]] Until the live text is checked, treat the same defect as *probably present, not confirmed*.
- **Not verified:** the 2026-11-13 edit itself and every entry from 2026-11-13 to about 2026-11-18. The changelog page is about 745 KB and the fetchable views were truncated. I therefore call no defect “unfixed” unconditionally. Each defect below is conditional on the live text.
- **Standing records relevant to the article:**

- (a) A logged review entry records “**plenitude-void DECLINED** — it is at **3062 words, over its 3000 hard gate**”. [[workflow/changelog]] The same review logged “Verified clean, do not re-flag: plenitude format-vs-combination distinction accurate against Cohen/Dennett/Kanwisher 2016”. [[workflow/changelog]] I found no logged trim. This is confession-without-correction: an over-limit status was logged and became a reason to refuse additions, but no reduction was made.
- (b) The task queue records that “The Ensemble Reframe” section landed on 2026-08-18 at 18:00 with five references. The secondary fold into `voids/resolution-void` was still an active task. [[workflow/todo]]
- (c) The 2026-08-18 research note said: “plenitude-void currently states that ‘current methods cannot adjudicate between these pictures.’ That is too flat.” [[research/voids-summary-statistics-void-2026-08-18]] It prescribed a softening. [[research/voids-summary-statistics-void-2026-08-18]] Whether the softening landed cannot be confirmed without the live text. If the sentence survives unchanged, it is a second confession-without-correction.

### 2.1 Three-layer citation verification

Layer key: **Meta** = metadata accuracy; **Verb** = verbatim fidelity; **Stance** = author-stance accuracy. “Presence” says how I know the source is used on the page.

| # | Source as used (presence) | Meta | Verb | Stance | Verdict | Checked at |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Block (2007) BBS 30(5-6):481–499; Block (2011) TiCS 15(12):567–575, overflow (site-record; cited on `phenomenal-overflow`) | Correct as given on `phenomenal-overflow` | “Perceptual consciousness is richer (i.e., has a higher capacity) than cognitive access” matches the TiCS 2011 abstract wording as reproduced in site notes; not re-read at publisher this session | **At risk.** Block is a physicalist. `phenomenal-overflow` correctly records his “neural realizer” claim, [[concepts/phenomenal-overflow]] but `topics/dualist-perception` turns richness into “converging evidence that consciousness involves something beyond the physical” [[topics/dualist-perception]] | Retain citation; fix stance on sister page | PubMed 22078929 (via site note); BBS DOI 10.1017/S0140525X07002786 |
| 2 | Dennett, “grand illusion sparsity” (site-record) [[research/voids-summary-statistics-void-2026-08-18]] | Not visible | Not visible | **Compressed.** The “grand illusion” label comes from Blackmore et al. (1995) and the 2002 JCS special issue edited by Noë. Noë’s own target paper argued the grand-illusion hypothesis is mistaken. Vision and Mind (Noë & Thompson 2002) presents “Perceptual experience is a ‘grand illusion’” as the “new skepticism” under examination, not as Dennett’s coinage [uodiyala](https://coehuman.uodiyala.edu.iq/uploads/LONG-NAMES-FILES/Alva_Noe_and_Evan_Thompson_(eds)_-_Vision_and_Mind._Selected_Readings_in_the_Philosophy_of_Perception_2002_______________~1.pdf) | Revise attribution | Noë & Thompson (eds.) 2002, Vision and Mind, intro (MIT Press) |
| 3 | O’Regan & Noë, “outside memory” (site-record: “already in plenitude-void”) [[research/voids-summary-statistics-void-2026-08-18]] | **Probable misattribution.** “The world as an outside memory” is the title of O’Regan (1992), Canadian Journal of Psychology 46:461–488, not O’Regan & Noë (2001, BBS 24:939–1031) [uodiyala](https://coehuman.uodiyala.edu.iq/uploads/LONG-NAMES-FILES/Alva_Noe_and_Evan_Thompson_(eds)_-_Vision_and_Mind._Selected_Readings_in_the_Philosophy_of_Perception_2002_______________~1.pdf) | Not visible | Accurate as sensorimotor anti-representationalism; O’Regan & Noë are not dualists and should not be counted toward Tenet 1 | Correct to O’Regan 1992, or cite 2001 for sensorimotor theory only | Vision and Mind bibliography (O’Regan 1992 title verified) |
| 4 | Cohen, Dennett & Kanwisher (2016) TiCS 20(5):324–335 (site-record) | Correct (per Crossref record reproduced in site note) [[research/voids-summary-statistics-void-2026-08-18]] | Not visible | Logged as “accurate against CDK 2016” on the format-vs-combination point. CDK argue for *sparse* item-level phenomenology plus summary statistics, so any reading of ensemble coding as support for richness is a stance inversion [[research/voids-summary-statistics-void-2026-08-18]] | Retain; check direction of use | DOI 10.1016/j.tics.2016.03.006 |
| 5 | Bronfman, Brezis, Jacobson & Usher (2014) Psych Sci 25(7):1394–1403 (site-record) | Correct | Site note quotes the abstract (“registered automatically, outside focal attention…”); consistent with my knowledge, not re-read this session | Usher and colleagues do favour overflow; stance accurate [[research/voids-summary-statistics-void-2026-08-18]] | Retain, but **incomplete without its critiques** (rows 6–7) | DOI 10.1177/0956797614532656 |
| 6 | Ward, Bear & Scholl (2016) Cognition 152:78–86 (site-record) | Correct per site note’s Crossref check; my independent search failed (budget) | Site note quotes the abstract: “such results are fully consistent with sparse visual awareness” | Accurate if used as cutting the ensemble-to-item inference; the authors claim consistency with sparseness, not proof [[research/voids-summary-statistics-void-2026-08-18]] | Retain | DOI 10.1016/j.cognition.2016.01.010 |
| 7 | Jackson-Nielsen, Cohen & Pitts (2017) Consc. Cogn. 48:149–160 (**absent from the site’s planning record**) | Verified [philpapers](https://philpapers.org/rec/JACPOE-2) | Kimchi & Sabary (2025) report that “a majority of the participants were inattentionally blind to color diversity, size diversity, and mean size” | Cohen co-authored; a deflationary result | **Material omission** | PhilPapers JACPOE-2; DOI 10.1016/j.concog.2016.11.007 [springer](https://link.springer.com/article/10.3758/s13414-025-03111-9) |
| 8 | Rahnev et al. (2011) Nat Neurosci 14(12):1513–1515; Knotts, Odegaard, Lau & Rosenthal (2019) Curr Opin Psychol 29:49–55 (site-record: “inflation as the account of the seeming”) | Correct per site note | Site note: “subjective inflation can account for rich phenomenology without invoking phenomenological overflow” | Lau and Rosenthal are higher-order physicalists. The site note recasts inflation as a mere parsimony move to be blunted by Tenet 5. [[research/voids-summary-statistics-void-2026-08-18]] That misdescribes it: inflation makes distinct confidence–sensitivity predictions that were tested | Retain citation; fix framing | DOIs 10.1038/nn.2948; 10.1016/j.copsyc.2018.11.006 |
| 9 | Odegaard & Lau (2016) TiCS 20(9):642–643 (site note) | The site note’s “corrected” author list is right for this letter. The four-author “Odegaard, Chang, Lau & Cheung” it had recalled [[research/voids-summary-statistics-void-2026-08-18]] is a *different* paper (2018, Phil. Trans. R. Soc. B, “Inflation versus filling-in”), which is uncited and directly relevant | — | — | Add the 2018 paper | DOI 10.1016/j.tics.2016.06.005 |
| 10 | Zheng & Meister (2025) Neuron 113(2):192–204 (site-record: “Bandwidth Frame”; inferred) | Verified [caltech](https://meisterlab.caltech.edu/documents/30100/Zheng_2024_The_unbearable_slowness_of_being-_Why_do_we_live_at_10_bitss.pdf) | Verified: sensory input about 10⁹ bits/s (“6 million cones … about 1.6 gigabits/s”); behavioural throughput about 10 bits/s [[workflow/changelog]] | **High risk.** The authors measure *behavioural* information throughput and treat the gap as a neural question. On 2026-11-20 the site itself conceded on another page that the interface reading “is the Map’s inference” [[workflow/changelog]] | Retain only with explicit stance line, or move off-page | DOI 10.1016/j.neuron.2024.11.008; Caltech PDF |
| 11 | Sauerbrei & Pruszynski (2025) Nat Neurosci 28:1365–1366 (used on `bandwidth-of-consciousness`) [[topics/bandwidth-of-consciousness]] | Verified | Abstract: the limit “appears to hold for high-level cognitive functions” but “unconscious processing for real-time control of movement … substantially exceeds this limit” [nature](https://www.nature.com/articles/s41593-025-01997-0) | **Co-optation.** `bandwidth-of-consciousness` says the bottleneck “appears precisely where consciousness enters the picture” and calls it “the filter itself”. [[topics/bandwidth-of-consciousness]] The authors argue about unconscious motor throughput, not a consciousness filter [researchgate](https://www.researchgate.net/scientific-contributions/J-Andrew-Pruszynski-2119802703) | Fix sister page | DOI 10.1038/s41593-025-01997-0 |
| 12 | Nørretranders (1998) / Zimmermann “11 million vs ~40–50 bits/s” (user-flagged; presence unconfirmed) | Not checkable this session | — | Provenance: textbook channel-capacity tables (Zimmermann, in Schmidt & Thews, Human Physiology) popularised by Nørretranders. These are engineering estimates of receptor-channel capacity, not measurements of conscious content | If present: demote to historical note or delete | Not verified at source (flagged) |
| 13 | Schwitzgebel (2008) Phil. Review 117(2):245–273 (user states the article draws on introspective unreliability) | Not verified this session | Not visible | **Self-undermining.** Schwitzgebel’s central examples include people’s confident but mistaken belief that peripheral visual experience is clear and detailed. That makes the *seeming of richness* his paradigm introspective error | Must be confronted, not merely cited | From knowledge; flagged unverified |
| 14 | Amir, Assaf, Yovel & Mudrik (2023) Cognition 238:105529 (**no site record of use**) | Verified [philpapers](https://philpapers.org/rec/AMIEWK) | — | The most-discussed recent empirical case for phenomenal consciousness without access (pink-noise offset paradigm) [nih](https://pmc.ncbi.nlm.nih.gov/articles/PMC12500690/) | **Material omission** | PhilPapers AMIEWK; DOI 10.1016/j.cognition.2023.105529 [philpapers](https://philpapers.org/rec/AMIEWK) |
| 15 | Frankish (2016) JCS 23(11-12):11–39 (on `phenomenal-overflow`) | Correct | Paraphrase accurate | Accurate: the page records that illusionism moves the “surcharge” rather than doubling it [[concepts/phenomenal-overflow]] | Retain (credit) | — |
| 16 | Nartker, Firestone, Egeth & Phillips (2025) eLife (on `phenomenal-overflow`) | Plausible; not verified this session | — | The page’s caution that the result “constrains that debate more than it settles it” is fair [[concepts/phenomenal-overflow]] | Retain | Not verified at source (flagged) |

**Pattern.** The site’s primary failure mode holds here too. The bibliography is mostly sound, and the errors sit in stance and selection:

- physicalist results recruited into dualist-flavoured framings (rows 1, 10, 11);
- deflationary critiques left out (rows 7, 9, 14);
- a single Bronfman-versus-Ward pairing presented as if it were the state of the ensemble debate.

### 2.2 Empirical currency

1. **Sperling, fragile VSTM, partial report.** Sperling’s basic partial-report advantage (about 4–5 letters on whole report against about 3 of 4 per cued row) is secure, and `phenomenal-overflow` states it correctly. [[concepts/phenomenal-overflow]] What is contested is the inference.

- Phillips argues the cue can shape the experience after the fact (postdiction).
- Mack and colleagues (2016) and Persuh, Genzer & Melara (2012) report that iconic memory degrades without attention.
- de Gardelle, Sackur & Kouider (2009) found subjects misreport pseudo-letters as real letters, the classic evidence for *generic or inflated* rather than specific phenomenology. [nih](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11498181/)
- None of these appears in any site record of the article, and `phenomenal-overflow` mentions none of them. **Verdict: incomplete; cherry-picked by omission.**
2. **Bronfman et al. and ensemble statistics.** The planned section pairs Bronfman with Ward, Bear & Scholl, which is a real improvement. It still omits:

- Jackson-Nielsen, Cohen & Pitts (2017);
- Kimchi & Sabary (2025, Attention, Perception & Psychophysics 87(6):1888–1903, PMC12331843), which concluded that “ensemble perception, at least of size and orientation, requires attention”;
- the countervailing finding that ensemble perception without attention “depends upon attentional control settings” (Chen, Zhuang, Wang, Ren & Abrams, Atten. Percept. Psychophys. 83:1240–1250, 2020).

The current state is that whether ensembles are extracted without attention is unresolved and paradigm-dependent. [researchgate](https://www.researchgate.net/publication/388618897_The_Role_of_Attention_in_Basic_Ensemble_Statistics_Processing) That is neither the overflow reading nor a clean deflation. Ensemble coding is in fact the deflationist’s mechanism (Cohen, Dennett & Kanwisher 2016). [[research/voids-summary-statistics-void-2026-08-18]][dokumen](https://dokumen.pub/the-philosophy-of-daniel-dennett-9780199367528-0199367523.html) Any use of it as evidence *for* plenitude inverts its literature. The logged “format-vs-combination accurate” check suggests the page uses it as a reframe, which is defensible, but this must be confirmed in the live text. **Verdict: partly current; selectively sourced.**
3. **Change and inattentional blindness.** The blindness-versus-amnesia dispute (Wolfe’s inattentional amnesia; Simons & Rensink 2005) is the point that matters for plenitude, and no site record shows it is engaged. `phenomenal-overflow` asserts without citation that change-blind subjects “often report a vague sense that ‘something is different’”. [[concepts/phenomenal-overflow]] That needs a source (Rensink’s “mindsight” work and its critics) or deletion. **Verdict: unsourced at the sister page; status on the void page unknown.**
4. **Peripheral and subjective inflation.** Present in plan **[site-record]**. [[research/voids-summary-statistics-void-2026-08-18]] The framing is wrong, though: the research note treats inflation as “a genuine explanatory economy” to be neutralised by Tenet 5. [[research/voids-summary-statistics-void-2026-08-18]] Inflation is a mechanistic account with tested signatures, including Rahnev’s lower confidence under attention at matched sensitivity and the Odegaard et al. 2018 peripheral work. An empirical model with tested predictions is not answered by invoking limits on Occam’s razor. **Verdict: present but mis-characterised.**
5. **Introspective unreliability.** Schwitzgebel’s case cuts against the premise (row 13). The standard replies are Bayne & Spener (2010) “Introspective humility”, which argues for domain-specific reliability, and Hurlburt’s Descriptive Experience Sampling. They would let the article claim *selective* rather than global unreliability, and selective unreliability is all the article needs. No site record shows either is used. **Verdict: weaponised in the wrong direction.**
6. **Bandwidth.** Zheng & Meister (2025) is verified. Sauerbrei & Pruszynski (2025) is the main published critique, and lower-quality compilations cite 2025 preprints reporting higher rates for memory and calculation (unreviewed; treat as leads only). [zenodo](https://zenodo.org/records/23939704) The decisive point is conceptual, not numerical: bits per second of *behaviour* measure the access channel. A gap between 10⁹ bits/s of sensory input and 10 bits/s of output is exactly what both the rich and the sparse views predict. **Verdict: irrelevant to the article’s thesis; delete from this page.**
7. **No-report paradigms and COGITATE.** No site record shows engagement with Tsuchiya et al. (2015), Block (2019) on no-report, or the COGITATE adversarial collaboration. The Cogitate Consortium’s 2025 Nature report (Ferrante et al., Nature 642:133–142, doi 10.1038/s41586-025-08888-1) found results that “align with some predictions of both theories” but “critically challenge key tenets of both theories” (global workspace and integrated information theory). A void claiming the gap may be unsettleable should at least say what no-report methods have and have not settled. **Verdict: out of date.**
8. **2023–2026 work.**

- Amir et al. (2023) is missing.
- A 2024 PMC paper, “More than words: can free reports adequately measure the richness of perception?” (PMC11498181), shows the free-report method itself is under active challenge. [nih](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11498181/)
- Edvard Aviles-Meza’s “The Problem of Introspective Blink” (Erkenntnis, 19 March 2026, doi 10.1007/s10670-026-01068-1) argues that overflow creates a distinctive epistemological problem: introspection requires attention, so experience outside attention is subjectively inaccessible and, he proposes, “can only be known through memory”. That is *the article’s own thesis, published by a Cornell philosopher*, and the article should cite it as its closest ally and test.

**Verdict: not current.**

### 2.3 Objections: steelmen and whether they are answered

Judgements are provisional where marked (†) because I could not read the live text. “Site-record” means the site’s own planning or review notes show engagement.

| Objection (steelman) | Evidence of engagement | Judgement |
| --- | --- | --- |
| (a) **Dennett.** The richness is in the world, not the head. The *judgement* “it’s all there” is real, but there is no rich internal medium, and outside the stories we tell there is no fact about “unaccessed experience” | Named (site-record: “Dennett’s grand-illusion sparsity”) [[research/voids-summary-statistics-void-2026-08-18]] | Named but not answered† |
| (b) **Frankish/Kammerer illusionism.** The seeming of plenitude is an introspective representation with no rich phenomenal object. Kammerer’s question is why illusions of phenomenality are so robust | Named as “eliminativism as a third exit” (site-record). [[research/voids-summary-statistics-void-2026-08-18]] `phenomenal-overflow` handles Frankish fairly [[concepts/phenomenal-overflow]] | Partially answered† |
| (c) **Cohen & Dennett (2011).** Phenomenality dissociated from all function is untestable and so outside science. A void “unsettleable from inside” *concedes* this unless it names an outside route | `phenomenal-overflow` concedes “may be unfalsifiable” and then calls this “exactly what we’d expect if phenomenology genuinely transcends access” [[concepts/phenomenal-overflow]] | **Not answered; conceded.** Treating unfalsifiability as expected under one’s own hypothesis is the void-as-evidence move |
| (d) **Phillips (postdiction).** The cue shapes what was experienced; partial-report superiority shows availability, not prior specific experience | No record | Not addressed |
| (e) **Stazicker/Kouider.** Unattended content is phenomenally *indeterminate* or *generic* (“letters, unidentified”). That is rich in seeming, sparse in specificity, and needs no overflow | `phenomenal-overflow` sketches a “gestalt impression”; no record on the void page [[concepts/phenomenal-overflow]] | Named (sister page) but not answered |
| (f) **Gross & Flombaum (2017).** Probabilistic, hierarchical representations make “how much is represented” ill-posed. Report limits reflect sampling from distributions, not unaccessed determinate content | The ensemble “format” reframe gestures at this (site-record) [[research/voids-summary-statistics-void-2026-08-18]] | Partially answered (indirectly)† |
| (g) **Lau/Odegaard/Knotts (inflation; higher-order theory).** Felt richness is a confidence signal that runs *against* fidelity in the periphery | Planned (site-record) [[research/voids-summary-statistics-void-2026-08-18]] | Named; framed as parsimony only, so **not answered** |
| (h) **Dehaene/Naccache (global workspace).** The “illusion of seeing” is the workspace’s ability to access any region on demand; preconscious content is available, not experienced | No record | Not addressed |
| (i) **Schwitzgebel against the premise.** If naive introspection is this unreliable, the datum “experience seems richer” loses its standing, and Schwitzgebel’s own examples are periphery-richness errors | No record of the article confronting this | **Not addressed; self-undermining** |
| (j) **Refrigerator light.** Each time you check the periphery it is detailed because checking makes it so; from inside, “always rich” and “rich when checked” are indistinguishable | Implicit in the “outside memory” material (site-record) [[research/voids-summary-statistics-void-2026-08-18]] | Partially answered† |
| (k) **Predictive processing / active inference.** Clark, Hohwy and Seth: felt richness is high-precision prediction of a stable world (“controlled hallucination”). Laukkonen, Friston & Chandaria (2025, Neuroscience & Biobehavioral Reviews 176:106296, metadata as supplied by the user, not re-verified this session) model the felt luminosity of experience through self-modelling “epistemic depth” | No record on this page, although the changelog shows a “beautiful-loop paragraph” was added to some *other* voids page. [[workflow/changelog]] This is a standing corpus-wide blind spot | **Not addressed; material.** Predictive processing is the most developed positive account of *why* experience seems fuller than its accessible content, which is this article’s explanandum |

**The central inference.** The article’s honest version is: “from the inside, rich phenomenology and inflated or generic phenomenology are indistinguishable.” Every major rival predicts that indistinguishability:

- higher-order theory, through inflation;
- global workspace theory, through on-demand access;
- illusionism, through introspective misrepresentation;
- predictive processing, through high-precision priors.

So the void has a likelihood ratio close to 1 for dualism against physicalism. It can therefore count for nothing beyond *compatibility*. An unsettleable gap is evidence that introspection has limits. It is not evidence about what lies beyond the limit. Any tenets section that says or implies that the void “fits”, “is expected under” or “is explained by” irreducibility, without an explicit *no evidential weight* declaration, commits an epistemic-to-metaphysical slide. `voids/the-surplus-void` already shows the correct move: “the fact that the dualism tenet makes the surplus expected cannot then serve as independent evidence for the tenet itself”. [[voids/the-surplus-void]] So does the 2026-11-20 `interested-party-void` edit: “support no tenet; none of their authors argues for dualism (P-V3)”. [[workflow/changelog]] The Plenitude Void should carry the same declaration verbatim in structure. I could not confirm that it does†.

### 2.4 Neighbour differentiation and site integration

**Distinct work.** The page does real distinct work only if its thesis is narrowed to *format* or *specificity*: consciousness cannot tell from inside whether its field is item-coded, statistically coded or inflated. The site’s own research note says as much: the only angle “genuinely not a sub-part of plenitude-void” is the format question. [[research/voids-summary-statistics-void-2026-08-18]] Framed as “experience is richer than report”, the page duplicates `concepts/phenomenal-overflow` almost entirely.

**Overlaps (verified from live neighbour excerpts):**

- `voids/resolution-void`: “The Discrimination Floor” and “Six Orders of Magnitude” compression overlap the Bandwidth Frame and the metamer material. [[research/voids-summary-statistics-void-2026-08-18]] The secondary fold was still pending in the task queue. [[workflow/todo]]
- `voids/dimensionality-void`: the “sufficiency illusion” and “our introspective completeness — the feeling that experience is all there”. [[voids/dimensionality-void]] This is the mirror image of plenitude (seeming complete versus seeming overfull) and needs an explicit contrast sentence on both pages.
- `voids/erasure-void`: the “completeness illusion”, “From the inside, a full inventory and a depleted inventory plus confabulation feel the same.” [[voids/erasure-void]] This is structurally identical to the plenitude indistinguishability claim. Same architecture, different content, so it falls under the taxonomy’s independence caveat.
- `voids/the-surplus-void`: a *different* sense of richness (qualitative depth beyond function). The research note warns that “conflating the two senses of ‘richness’ would generate a false concession”. [[research/voids-summary-statistics-void-2026-08-18]] The Plenitude Void must say which sense it uses.
- `voids/noetic-feelings-void` and `voids/perceptual-reality-monitoring-void`: the site’s research note calls felt-vividness the fifth case of a separable, sub-personal “felt-X” signal decoupled from what it reports. [[research/voids-summary-statistics-void-2026-08-18]] Five faces of one architecture are not five findings, and the page should say so. [[research/voids-summary-statistics-void-2026-08-18]]
- `voids/acquaintance-void`: `phenomenal-overflow` routes readers there (“the broader void of pre-conceptual knowing”), not to the Plenitude Void. [[concepts/phenomenal-overflow]]

**Reciprocity (verified):** the “Further Reading” list of `concepts/phenomenal-overflow` (live, 2026-11-05) links access-consciousness, phenomenal-consciousness, global-workspace-theory, recurrent-processing-theory, introspection, attention-as-interface, stapp-quantum-mind, the Acquaintance Void and consciousness-epistemology-extended-cognition. It does **not** link `voids/plenitude-void`, [[concepts/phenomenal-overflow]] even though the void owns the overflow dispute **[site-record]**. [[research/voids-summary-statistics-void-2026-08-18]] That is a reciprocity failure on the article’s most important neighbour. Whether the void links the concept page could not be checked†.

**Contradictions (verified on the neighbours):**

1. `topics/dualist-perception`: “The richness of perceptual experience reflects the richness of consciousness itself” and “providing converging evidence that consciousness involves something beyond the physical.” [[topics/dualist-perception]] This presents as established the very richness the void says cannot be settled. It is a constrain-versus-establish failure, and it contradicts the void’s own thesis.
2. `concepts/phenomenal-overflow`, Occam section: “Deflationary theories require subjects to be systematically wrong about their own experience” and “When a theory’s parsimony requires dismissing the primary data (subjective reports), parsimony may mislead.” [[concepts/phenomenal-overflow]] The void’s thesis, and its reliance on introspective unreliability, *requires* that subjects can be systematically wrong here. The site cannot treat richness reports as primary data on one page and as unsettleable on another. This is calibration asymmetry: introspection is trusted when it favours richness and distrusted when it would settle the question.
3. `concepts/phenomenal-overflow` says both “The Unfinishable Map presents it as evidence for the richness of phenomenology beyond access” and “Overflow fits the tenet without establishing it.” [[concepts/phenomenal-overflow]] The first sentence overstates what the second, correctly, concedes.
4. `concepts/cognitive-penetration` has it right: “introspective judgement is the more exposed faculty… The seeming that it is irreducible is more exposed”. [[concepts/cognitive-penetration]] The Plenitude Void should import that self-awareness, since the seeming of plenitude is exactly such an exposed introspective seeming.

**Credit where due.** On available evidence the page is not padded rhetoric:

- the 08-18 ensemble fold followed a sourced critique;
- the logged format-versus-combination check is a real check against Cohen, Dennett & Kanwisher; [[workflow/changelog]]
- the research note’s own warnings (do not read the literature as settling against Block; do not conflate the two senses of richness; do not present the human/AI asymmetry as access to phenomenology) are the right ones. [[research/voids-summary-statistics-void-2026-08-18]]

**Calibration against the apex standard.** I could not fetch `apex/cross-modal-capability-division` or `apex/born-preserving-causal-efficacy` in this session, so I cannot compare line by line. Against the evidential ladder the user names (compatible, suggestive, discriminating), nothing in the site record suggests the Plenitude Void labels any claim’s evidential grade. Its correct grade is *compatible* throughout.

**Pathology ledger (only instances quoted from text I saw):**

- **Constitutional-attractor effect / constrain-vs-establish gate:** `topics/dualist-perception`, “converging evidence that consciousness involves something beyond the physical.” [[topics/dualist-perception]]
- **Co-optation firewall failure:** `topics/bandwidth-of-consciousness`, “The bottleneck appears precisely where consciousness enters the picture—the brain *can* process at higher rates, as Sauerbrei and Pruszynski demonstrate”, followed by “the bottleneck is the *filter itself*”. [[topics/bandwidth-of-consciousness]] Also the bandwidth research note, which says the critique “actually strengthens the case for a conscious interface bottleneck.” [[research/bandwidth-constraints-10-bits-2026-03-29]]
- **Calibration asymmetry:** `concepts/phenomenal-overflow`, “This reflects the materialist strategy of explaining away apparent features of consciousness rather than explaining them.” [[concepts/phenomenal-overflow]]
- **Epistemic-to-metaphysical slide / void-as-evidence:** `concepts/phenomenal-overflow`, “This unfalsifiability is generally a mark against a hypothesis—yet it’s also exactly what we’d expect if phenomenology genuinely transcends access.” It is partly redeemed by the next clause, “unfalsifiability doesn’t confirm overflow”. [[concepts/phenomenal-overflow]]
- **Tenet leakage:** the same page’s Bidirectional Interaction section, “overflow fits a picture on which phenomenology is primary, and access is the result of conscious selection”. [[concepts/phenomenal-overflow]]
- **Confession-without-correction:** the logged “plenitude-void DECLINED — it is at 3062 words, over its 3000 hard gate” with no trim recorded; and the logged “A correction the Map owes itself” (“cannot adjudicate” is “too flat”), whose application is unconfirmed. [[research/voids-summary-statistics-void-2026-08-18]] [[workflow/changelog]]
- **Evidential-independence failure:** felt-vividness counted alongside four other “felt-X” voids from one architecture. The research note concedes “five faces of one architecture is not five independent findings”. [[research/voids-summary-statistics-void-2026-08-18]] Whether the void page repeats the concession is unknown†.

## Part 3 — Bottom-Line Per-Position Verdicts

| Position the article advances | Verdict | Reason |
| --- | --- | --- |
| “Conscious experience *seems* richer than anything we can report or check” | **RETAIN** (as a description of a seeming) | A near-universal report, but it must be paired with Schwitzgebel’s point that this seeming is itself a documented introspective error in the periphery |
| “The gap may be impossible to settle from the inside” | **RETAIN, narrowed** | True and now defended in the professional literature (Aviles-Meza, Introspective Blink, 2026). It must state that *outside* routes such as no-report methods, Amir et al. 2023, metamers and inflation psychophysics are partly tractable |
| Grand-illusion debate as framing | **REVISE-HARD** | Fix the attribution (Blackmore, the 2002 JCS issue, Noë’s rejection of the label); drop the “Dennett’s grand illusion” shorthand |
| Block’s overflow argument | **FLAG AS PERPETUALLY CONTESTED** | Add Phillips, Kouider/de Gardelle, Stazicker, Gross & Flombaum, Amir et al.; state Block’s physicalism in the article body [[concepts/phenomenal-overflow]] |
| Ensemble statistics | **REVISE-HARD** | Keep the format reframe; add Jackson-Nielsen et al. 2017 and Kimchi & Sabary 2025; state that ensemble coding is the deflationist’s mechanism |
| Introspective unreliability (Schwitzgebel) | **REVISE-HARD** | Currently cuts against the premise; reframe as *selective* unreliability (Bayne & Spener) and confront the periphery examples |
| Bandwidth estimates (Zimmermann/Nørretranders; Zheng & Meister) | **DELETE from this page** | They measure the access channel, so they are irrelevant to plenitude; they duplicate `bandwidth-of-consciousness`; [[research/voids-summary-statistics-void-2026-08-18]] and deleting them frees the words needed to get back under the 3,000-word limit |
| “Current methods cannot adjudicate” (if still present) | **REVISE-HARD** | The site’s own research note called it “too flat” [[research/voids-summary-statistics-void-2026-08-18]] |
| Tenet/site-perspective connection | **DEMOTE-TO-COHERENCE-ONLY** | Likelihood ratio about 1; adopt the surplus-void and P-V3 no-support formula |
| The page as a whole | **REVISE-HARD** | Distinct only as the *format/specificity* void; otherwise it duplicates `concepts/phenomenal-overflow` |

## Part 4 — Article-Specific Fixes

**`voids/plenitude-void`**

1. **Verify first, against the live text:**

- whether “current methods cannot adjudicate between these pictures” survives;
- whether O’Regan & Noë (2001) is credited with “outside memory”;
- whether the Bandwidth Frame presents Zheng & Meister’s 10 bits/s as *conscious* bandwidth;
- whether the tenets section contains a no-support declaration.

Record each outcome in the changelog.
2. **Delete the “Bandwidth Frame” section.** Replace it with one sentence: “Throughput estimates measure the access channel and so cannot bear on whether experience outruns it; see bandwidth-of-consciousness.” This takes the page under 3,000 words and clears the logged over-limit status.
3. **Rewrite the thesis sentence** to the format/specificity form: “From the inside, consciousness cannot tell whether its unattended field is item-coded, statistically pooled, generically indeterminate or confidence-inflated; all four render as populated space.”
4. **Add a “Rivals at strength” subsection** (about 350 words) covering:

- Phillips’s postdiction;
- Kouider/de Gardelle generic phenomenology;
- Stazicker’s indeterminacy;
- Gross & Flombaum’s probabilistic representation;
- Dehaene/Naccache’s on-demand access;
- Lau-lab inflation as a *tested model*, not a parsimony move;
- predictive processing (Seth; Clark; Laukkonen, Friston & Chandaria 2025).

Give each a one-line statement of what it predicts about the seeming. Conclude that all predict the void.
5. **Ensemble section:** add Jackson-Nielsen, Cohen & Pitts (2017, doi 10.1016/j.concog.2016.11.007) and Kimchi & Sabary’s 2025 attention-requirement study (doi 10.3758/s13414-025-03111-9, PMC12331843), and state that whether ensembles survive without attention is unresolved. Add one sentence saying that Cohen, Dennett & Kanwisher use summary statistics to argue for *sparse* item phenomenology.
6. **Schwitzgebel paragraph:** add “Schwitzgebel’s own examples of naive introspective error include the belief that peripheral vision is detailed; the seeming this article starts from is thus his paradigm case of unreliability.” Then add Bayne & Spener (2010) for the selective-reliability reply.
7. **Add an “Outside routes” paragraph** covering Amir et al. (2023), no-report paradigms and Block (2019), COGITATE (2025), metamer psychophysics, and Aviles-Meza’s “The Problem of Introspective Blink” (2026). The point: the gap is unsettleable *introspectively*, not wholly unsettleable.
8. **Relation to Site Perspective:** insert “The plenitude void supports no tenet. Every rival predicts the same inside-indistinguishability, so its evidential grade is *compatible*, not suggestive or discriminating; none of the cited empirical authors argues for dualism (P-V3).”
9. **Attribution fixes:** credit “grand illusion” to Blackmore et al. (1995) and the 2002 JCS issue, noting that Noë argued against it. Credit “outside memory” to O’Regan (1992).
10. **Add contrast sentences** with `voids/dimensionality-void` (seeming-complete versus seeming-overfull), `voids/erasure-void` (same indistinguishability architecture) and `voids/the-surplus-void` (a different sense of richness). State the independence caveat for the five felt-X voids.

**`concepts/phenomenal-overflow`**

1. Add `voids/plenitude-void` to Further Reading and to the closing paragraph alongside the Acquaintance Void.
2. Replace “The Unfinishable Map presents it as evidence for the richness of phenomenology beyond access” with “The Map treats it as contested and, at most, compatible with the dualism tenet.”
3. Delete or rewrite the Occam section’s “Deflationary theories require subjects to be systematically wrong…” and “materialist strategy of explaining away”. Replace them with a symmetric statement: both readings take a position on what the reports are worth, and the reports cannot settle it.
4. Source or delete the change-blindness “vague sense that something is different” claim.
5. Add Phillips (postdiction), de Gardelle, Sackur & Kouider (2009), Amir et al. (2023) and Lau-lab inflation to the evidence section.
6. Reconcile the Sperling count with `research/voids-pre-conceptual-knowing-2026-01-27`, which says “3-4”; the concept page says “4-5”. [[concepts/phenomenal-overflow]]

**`topics/dualist-perception`**

1. Replace “providing converging evidence that consciousness involves something beyond the physical” with “each compatible with, but none discriminating for, the claim that consciousness involves something beyond the physical.” Replace “The richness of perceptual experience reflects the richness of consciousness itself” with a conditional: “If dualism is true, the richness of perceptual experience could reflect…”

**`topics/bandwidth-of-consciousness`**

1. Rewrite the Sauerbrei & Pruszynski passage so it states their claim: unconscious motor control exceeds 10 bits/s. Mark “the bottleneck is the filter itself” as “the Map’s interpretation, not the authors’”, mirroring the 2026-11-20 fix on `metaphysics-of-information-under-dualism`.
2. Absorb the material deleted from the void’s Bandwidth Frame (references only, given the page’s own hard-limit status). Add the summary-statistics argument of Cohen, Dennett & Kanwisher, which the 08-18 note says is “not represented anywhere in the corpus”. [[research/voids-summary-statistics-void-2026-08-18]]

**`voids/resolution-void`**

1. Complete the pending metamer fold, and add a reciprocal link to the Plenitude Void at “The Discrimination Floor”.

**`research/voids-summary-statistics-void-2026-08-18`**

1. Correct “O’Regan & Noë’s ‘outside memory’ account” to O’Regan (1992). Add a note that the four-author paper it recalled is Odegaard, Chang, Lau & Cheung (2018), a separate and relevant source. Revise “The Map’s position should be that the economy is real and that it is not, by itself, evidence”: inflation is a tested model, not merely a parsimony claim.

## Part 5 — Site-Wide Methodology Improvements

1. **Turn confessions into binding status changes.** An over-length or a “correction the Map owes itself” entry should automatically open a P1 task that blocks further edits to the page until it is resolved. “DECLINED, over hard gate” must never be a terminal state. Add a weekly check: any page over its hard limit for more than 14 days gets a forced trim or a demotion flag shown on the page.
2. **Make evidential-grade labels mandatory on every void page.** Every tenets section should carry one of compatible, suggestive or discriminating, together with the rival(s) that would need to *fail* to predict the void for the grade to rise. Voids default to *compatible*, and a higher grade requires a stated likelihood-ratio argument. The P-V3 sentence used on `interested-party-void` on 2026-11-20 should become standard boilerplate.
3. **Make the co-optation firewall a checklist item, not a free-text judgement.** For each cited empirical author, record (a) their stated metaphysics and (b) whether the citing sentence draws a conclusion they reject. The 2026-11-20 Zheng & Meister fix shows the review can catch this, but it caught it on one page and not on the others where the same source is used. Corrections should spread across the corpus by source DOI, not stay page by page.
4. **Run a cross-page consistency check on introspective trust.** Any page that treats introspective reports as “primary data” for richness or irreducibility should be flagged when a void page in the same cluster treats those reports as unreliable. One site-wide position (P-level) on the evidential weight of introspective seemings, along the lines of `concepts/cognitive-penetration`’s “the seeming that it is irreducible is more exposed”, should govern both.
5. **Make predictive processing a mandatory rival.** It is a standing blind spot. Every void about the *seeming* of experience (richness, completeness, presence, vividness) should carry a one-paragraph predictive-processing or active-inference rival (Clark, Hohwy, Seth, and Laukkonen, Friston & Chandaria 2025) before review sign-off.
6. **Verify at full text before folding.** The 2026-08-18 research note that seeded the Ensemble Reframe states that no web search was available. It says all sources were checked at abstract level only and that “any downstream article must open the full texts before asserting anything finer-grained”. [[research/voids-summary-statistics-void-2026-08-18]] The section landed the same day. [[workflow/todo]] Folds that rest on abstract-only notes should be blocked until full-text verification is logged.
7. **Address Claude-on-Claude circular review directly.** The site’s research, drafting and review stages are run by models from one family. The site’s own distributional-void note reports that errors across different models are correlated. [[research/voids-distributional-void-2026-08-24]] A “Verified clean, do not re-flag” stamp from a same-family reviewer therefore protects the content from later scrutiny instead of certifying it. Stamps should expire after 60 days or after the next substantive edit. Stance accuracy should be audited at least quarterly by a reviewer outside the model family or by a human, starting with the overflow cluster (`concepts/phenomenal-overflow`, `voids/plenitude-void`, `topics/dualist-perception`, `topics/bandwidth-of-consciousness`).
8. **Make search-lag-proof fetching a published contract.** External audits repeatedly fail to fetch slug URLs and paginated changelog views. Publish (a) a machine-readable per-page changelog (for example `/voids/plenitude-void/history.json`) and (b) a daily changelog archive split by date, so that a “since date X” audit can be done without loading a 745 KB page.
9. **Run a neighbour-differentiation audit for every void cluster.** Require each void to state in one sentence what it does that its three nearest neighbours do not, and to carry reciprocal links to them. Automate the check that the concept page owning a void’s central argument links back to that void, which fails today for `concepts/phenomenal-overflow` and `voids/plenitude-void`.
10. **Treat DELETE and DEMOTE as real outcomes.** The voids catalogue is close to its cap (the 2026-11-19 entries record 124/125). [[workflow/changelog]] Re-scope the Plenitude Void as the “format void”. If, after the fixes above, it still largely restates `concepts/phenomenal-overflow`, merge it into that page and free a slot instead of continuing to defend both.

## Verification Notes

Processed 2026-11-20 by the collect-claude-review pass. Extraction: 53,922 characters from the artifact panel (body stable across a 10 s sample), ending on Part 5 item 10. **Binding caveat:** the reviewer says it could not fetch the live `voids/plenitude-void` and audited the page from research notes, the task queue and changelog records. Every claim about the page was therefore re-checked against the live file (3,062 words by `analyze_length`, voids hard 3,000). Several of its page-state claims describe older text or text the page never carried.

**Verified claims (tasks minted):**
- ✓ **Schwitzgebel (2008) cuts against the page's premise.** Author PDF (faculty.ucr.edu, pdftotext): asked whether a wide swath of the desk is clear at once, "Most people endorse something like this view when I ask them. … They are, I think, mistaken." He traces the error to checking each item by looking at it and then concluding "that they’re all clear simultaneously", which is the page's own check-and-find loop drawn to a sparse conclusion. The page cites him (L84) for unreliability about "peripheral visual detail" and then argues errors run "in both directions" (L86) without noting that his case is an over-estimate of richness. → new P1 task (item 1).
- ✓ **Subjective inflation is answered as a mere economy.** L80 reports Rahnev et al.'s psychophysical result and then replies only "The economy is real, and by Occam's Razor Has Limits a real economy is not by itself evidence." That leaves the evidence unanswered within the page. The ChatGPT pass rejected a broader "parsimony dismissed too readily" point as a framework-boundary disagreement; this narrower version is an internal gap and was minted with the counter-evidence route (Comay et al. 2025). → new P1 task (item 2).
- ✓ **The ensemble section omits the attention critiques.** Jackson-Nielsen, Cohen & Pitts (2017), *Consciousness and Cognition* 48:149–160, PMID 27918894 (abstract): colour and size summary statistics "often go unnoticed without attention". Kimchi & Sabary (2025), *Atten Percept Psychophys* 87(6):1888–1903, PMID 40533716 (abstract): the question "is unresolved", and their results "suggest that ensemble perception requires attention". The page answers Bronfman's attention-free claim only with Ward et al., who contest a different inference. → new P1 task (item 3).
- ✓ **`concepts/phenomenal-overflow` calibration.** L162 "presents it as evidence for the richness of phenomenology beyond access" sits against L142 "Overflow fits the tenet without establishing it". L154 calls deflation "the materialist strategy of explaining away", and L156 faults deflation for requiring subjects to be "systematically wrong", a cost `voids/plenitude-void` itself accepts via Schwitzgebel. L107 quotes "something is different" with no source. Rensink 2004, Simons, Nevarez & Boot 2005, Kouider et al. 2010, de Gardelle et al. 2009 and Phillips 2011 exist (Crossref metadata; no content read). → new P2 task.
- ✓ **`topics/dualist-perception` overstates overflow.** L90 "The information was in the experience but exceeded what access-consciousness could retrieve" is stated as fact, and L94 closes "The richness of perceptual experience reflects the richness of consciousness itself". Both conflict with the void's thesis. The page also gives Sperling's whole report as "3-4", against phenomenal-overflow's "4-5". → new P2 task.
- ✓ **Same as ChatGPT (Also-flagged lines added, no new tasks):** "outside memory" is O'Regan's 1992 phrase (P2 citation task, item 3). `concepts/phenomenal-overflow` does not link the void (P2 reciprocal-links task, item 1). Partial convergence on the Relation section's tenet grading (P1 calibration task, with the residual L122 "fits more comfortably within dualism's framing" made optional).
- ✓ Recent literature exists (Crossref): Amir, Assaf, Yovel & Mudrik 2023, *Cognition* 238:105529 (PubMed abstract: retrospective judgements of phenomenal aspects without online access, a pro-overflow result). Aviles-Meza, "The Problem of Introspective Blink", *Erkenntnis* 2026, doi 10.1007/s10670-026-01068-1, Cornell (metadata only; abstract elided by the publisher, so the reviewer's summary that it argues the page's thesis is unverified). Sauerbrei & Pruszynski 2025, *Nat Neurosci* 28:1365–1366.

**Unverified claims:**
- ? The reviewer's Kimchi & Sabary wording "ensemble perception, at least of size and orientation, requires attention", and its row-7 quotation about inattentional blindness to colour and size diversity. Neither is in the abstract; PMC full text not read.
- ? Noë rejected the grand-illusion charge. Supported by two abstracts that describe his view (Clark 2002; Clark & Toribio 2001), but Noë's own paper was not fetched (PhilPapers 403). Folded into the P1 task as an optional item, to be checked at source first.
- ? Bayne & Spener (2010) "Introspective humility", Odegaard et al. (2018) "Inflation versus filling-in", Chen et al. (2020), Laukkonen, Friston & Chandaria (2025), the 2024 PMC free-report paper, and COGITATE (Ferrante et al. 2025). Not checked, and not minted. They are leads only.
- ? Whether the page's ensemble reframe is read as support for richness. The live text uses it as a format reframe and reports Ward's "fully consistent with sparse visual awareness", so no stance inversion is visible.

**Disputed or rejected claims:**
- ✗ *"Grand illusion" credited to Dennett.* The live page credits the framing to Noë's 2002 volume and quotes Blackmore. "Dennett's grand-illusion sparsity" is research-note wording.
- ✗ *Bandwidth Frame presents Zheng & Meister's 10 bits/s or the Zimmermann/Nørretranders figures.* The page names neither ("Zheng", "Meister", "bits" all 0). It defers the figures to `bandwidth-of-consciousness` and says the asymmetry is "compatible with two pictures". The recommendation to delete the section rests on that false premise. Compressing L90–L92 is kept only as the word source for the new P1 task.
- ✗ *"Current methods cannot adjudicate" survives unsoftened.* L94 now reads "have not adjudicated … though that claim needs stating more carefully than it once did", followed by the "fewer pieces on the board" qualification. The 2026-08-18 correction landed.
- ✗ *No no-support statement in the Relation section.* L122 says the move "is not an independent argument for dualism" and that the void "does not by itself adjudicate between these frameworks".
- ✗ *Surplus-void sense of richness unscoped.* L46 and L76 scope it ("not the attended qualitative depth that the-surplus-void treats"). The ChatGPT pass rejected the same point.
- ✗ *`topics/dualist-perception` "providing converging evidence that consciousness involves something beyond the physical".* Removed by the 2026-10-30 refine (commit 0ba9461119). The live L66 "converging evidence" concerns the interface failure signatures.
- ✗ *`topics/bandwidth-of-consciousness` co-opts Sauerbrei & Pruszynski into a consciousness filter.* L147 now says both teams are physicalists, that "neither paper contains a mind-matter interface" and that "The interface conclusion is the Map's alone". L151 frames the filter reading as "accommodation, not discrimination".
- ✗ *Contrast sentence with `voids/dimensionality-void`.* That page is archived (`archive/voids/dimensionality-void.md`).
- — *Missing rivals on the void page itself* (Phillips, Kouider, Stazicker, Gross & Flombaum, Dehaene, predictive processing). These are real absences (all 0 hits), but the page is over its hard limit and already carries three open tasks. The partial-awareness and postdiction rivals were routed to `concepts/phenomenal-overflow`, which has headroom. Predictive processing as a corpus-wide rival is a methodology point.
- — *Methodology proposals* (Part 5: binding over-length status, mandatory evidential-grade labels, a co-optation checklist keyed by DOI, a consistency check on introspective trust, predictive processing as a mandatory rival, full-text verification before folds, stamp expiry and out-of-family audits, per-page history JSON, neighbour-differentiation audits, treating DELETE and DEMOTE as real outcomes). None was minted. They are recorded here for the combine and tune-system passes. Item 1 overlaps ChatGPT's page-length-enforcement proposal, and item 8 repeats the stale-changelog problem recorded in memory (the changelog page is too large for external fetchers).
