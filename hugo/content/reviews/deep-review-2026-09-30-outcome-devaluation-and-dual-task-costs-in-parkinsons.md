---
ai_contribution: 100
ai_generated_date: 2026-09-30
ai_modified: 2026-09-30 20:28:14+00:00
ai_system: claude-fable-5-1
author: null
concepts: []
created: 2026-09-30
date: &id001 2026-09-30
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-30 20:28:14+00:00
modified: *id001
related_articles: []
title: Deep Review - Outcome Devaluation and Dual-Task Costs in Parkinson's Disease
topics: []
---

**Date**: 2026-09-30
**Article**: [Outcome Devaluation and Dual-Task Costs in Parkinson's Disease: Which Control System Fails?](/topics/outcome-devaluation-and-dual-task-costs-in-parkinsons/)
**Previous review**: Never (created 2026-09-30 18:12Z by expand-topic; selector score 100)
**Research note governing the page**: [outcome-devaluation-and-dual-task-costs-in-parkinsons-2026-09-30](/research/outcome-devaluation-and-dual-task-costs-in-parkinsons-2026-09-30/) (verdict L32–44, gaps L279–291)
**Length**: 3,924 → 3,981 words (`analyze_length`, topics soft 3000 / hard 4000, gate `>=`; soft_warning before and after; length-neutral mode with 76 words of headroom at entry, 19 at exit). Line numbers below are the pre-edit numbering; the one inserted blank line shifts everything from the old L60 down by one.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Wu and Hallett (2005) controls figure wrong (factual error, propagated from the research note).** L60 said "All controls reached automaticity on both sequences". The Europe PMC abstract reads: fifteen patients recruited, "Three patients were finally excluded because they could not achieve automaticity", "Controls included 14 age-matched normal subjects", and "Twelve normal subjects performed all sequences automatically". So twelve of fourteen controls, not all, and the twelve patients are the retained sample after exclusion. The research note (L81) carried the same "all controls" error. **Resolved**: sentence rewritten to give the recruitment, the exclusion and "Twelve of the fourteen controls performed both sequences automatically; all twelve retained patients managed the simpler sequence and only three the more complex one". The 2008 sentence gained the matching control figure from its own abstract ("12 normal subjects performed all dual tasks correctly" of 14): "only three of fifteen patients, against twelve of fourteen controls". The table row "Larger, in count-of-patients terms" survives (3/12 vs 12/14 on the complex task) and its executive-confound rider is unchanged.
2. **Dropped qualifier in the de Wit (2011) prediction quote.** L35 quoted "should paradoxically outperform control subjects on a subsequent outcome devaluation test" as the habitual reading's prediction "if stimulus-response habit formation is impaired". The repository PDF (pure.uva.nl, pdftotext, dehyphenated) gives the full sentence in the Discussion as a proposal for a Tricomi-style paradigm: "If S→R habit formation *through extensive practice* is impaired in PD patients, they should paradoxically outperform...". The qualifier matters because Redgrave et al.'s reply (L47) turns on exactly that distinction (conflict-induced vs extensive-training habit). **Resolved**: L35 now reads "as a proposal for an extensive-training paradigm: if stimulus-response habit formation "through extensive practice" is impaired". No change to the verdict, since the direct test the page reports is the one de Wit et al. ran.
3. **Medication result compressed past what the source says.** L43 "Medication status made no difference." The PDF: RT showed no main effect of medication status; on the devaluation test "patients on medication tended to perform worse overall than patients off medication, but the effect of medication failed to reach significance, F(1, 27) = 3.38, p = .08", with the authors' caveat that the On and Off groups "were not matched well in terms of disease severity" and that "the absence of an effect of medication status should be replicated". **Resolved**: "Medication status had no significant effect, though the on-medication group tended to do worse (p = .08), which the authors read as a severity-matching artefact."

### Medium Issues Found

- **Sharp (2016) remediation stated without its nearest counter-datum.** The page reported that dopaminergic medication remediated the model-based deficit (Sharp et al.) and that de Wit et al. (2011) found no medication benefit, but never put the two beside each other. **Resolved**: one clause at L51, "and de Wit et al. (2011) found no comparable remediation on the devaluation test". This is a tension between two full-text-vs-abstract results in different paradigms, not a contradiction; it is now visible.
- **Roster stance sentence missing.** No author was presented as supporting the Map, but the page had no sentence saying so. **Resolved**: Stated Limits now ends "None of the authors surveyed addresses the metaphysics of control: Redgrave, de Wit, Mi, Sharp and Shohamy, Wu and Hallett, and Rochester write about physically realised control systems, and none is cited here as endorsing the Map's reading of the dissociation." Worded as a description of what the papers do, not as an attribution of a metaphysical position they never state.
- **Two paragraphs merged by a missing blank line** (old L59–60: the Wu, Hallett and Chan sentence ran straight into the bold "Automaticity operationalised" paragraph). **Resolved**: blank line inserted.
- **Funding cuts for length neutrality** (no claim removed): L29 "This article surveys those two literatures." (−6); L55 "Those are consistent, and they are the willed-deficit reading's direction" → "Those are consistent and run in the willed-deficit reading's direction" (−2); L62 Raffegeau within-patient rider merged into one sentence (−10); L64 cueing "fits a bypass story, and it also fits a story on which" → "fits a bypass story and also one on which" (−4); L88 two Stated Limits sentences tightened (−6); L94 Tenet 5 paragraph tightened, "single anatomically tidy story" → "anatomically tidy story", "It is not a licence to prefer" → "it licenses no preference for" (−7); L96 the felt-effort sentences merged (−8); Further Reading blurbs for paradoxical-kinesia and volitional-control shortened (−11). Wikilink count and targets unchanged.

### Citation web-verify ledger (§2.4)

Method: Crossref `works/{doi}` for every DOI (authors, year, title, venue, volume, issue, pages); Europe PMC `search?query=DOI:` for every abstract; full text via Europe PMC `fullTextXML` (PMC8574955 Mi, PMC3249188 de Wit 2012, PMC3205740 Kelly), NCBI efetch for PMC3124757 (Redgrave; the Europe PMC route returned HTTP 500), and the University of Amsterdam repository PDF for de Wit 2011 (OpenAlex OA location; the MIT Press PDF returned 403). Every quoted span of three or more words was grep-verified in the retrieved raw text after Unicode/dash normalisation; one initial miss (de Wit 2011 "paradoxically outperform") resolved after dehyphenating the two-column PDF text.

- de Wit, Barker, Dickinson & Cools 2011, *J Cogn Neurosci* 23(5) 1218–1229 — state: real-correct. Spans verified: abstract quote (full), "shift from internal to external control in PD", "congruence effect did not differ", r = −.37 (p < .05, UPDRS), 18-hr withdrawal, "paradoxically outperform" (Discussion; qualifier restored, Critical 2). Medication result corrected (Critical 3). Direction: habit formation not impaired, severity-linked goal-directed deficit — as stated.
- de Wit et al. 2012, *Psychopharmacology* 219(2) 621–631 (Crossref issued 2011 online; print 2012) — real-correct. "APTD tipped the balance towards habitual control", "restricted to female volunteers", phenylalanine/tyrosine, n = 14 per group all verified in PMC XML. Female-only stated at first mention (L53), in the table ("females only") and in Stated Limits. Direction as stated.
- Hernandez, Obeso, Costa, Redgrave & Obeso 2019, *TINS* 42(6) 375–383 — real-correct; "critical functional stressor" verified in the abstract and in Mi et al.'s citation of it. Abstract marker present at first mention and in References.
- Kelly, Eusterbrock & Shumway-Cook 2012, *Parkinson's Disease* 2012:918719 — real-correct. "consistently demonstrate greater dual-task walking deficits than healthy, age-matched individuals", "−18% to −19%", "−7%" verified in PMC XML; the −18/−19% figures are Kelly's table summary of O'Shea 2002 (motor and cognitive secondary tasks), attributed to Kelly as the page does.
- Knowlton, Mangels & Squire 1996, *Science* 273(5280) 1399–1402 — real-correct; abstract span verified; Redgrave et al. cite it as their ref 115 for patients "impaired in their implicit learning of habits" (efetch text), as the page says.
- Mi, Zhang, McKeown & Chan 2021, *Front Aging Neurosci* 13:734807 — real-correct. Both result spans, the summary quote, "practically 'OFF'" (≥12 h withdrawal), twenty patients and 20 controls, Hoehn-Yahr / disease-duration correlations, "did not investigate the expression" (on de Wit 2011), and "overall instrumental learning performance ... markedly impaired" / "still capable of acquiring" verified in PMC XML. Direction as stated (more slips toward devalued outcomes, severity-linked).
- O'Shea, Morris & Iansek 2002, *Physical Therapy* 82(9) 888–897 — real-correct; abstract confirms 15/15 design and "Both groups reduced their stride length and speed". The page cites the percentages through Kelly, correctly.
- Raffegeau et al. 2019, *Parkinsonism Relat Disord* 62 28–35 — real-correct; "SMD = -0.68", "19 studies" verified. Within-patient only; the page says so. Direction as stated.
- Redgrave et al. 2010, *Nat Rev Neurosci* 11(11) 760–772 — real-correct. All four spans verified in the author manuscript (interference prediction; "conflict-induced habit formation may be different from that induced by extensive training"; both halves of the open question). Also verified: their concession that "habit formation in an instrumental conflict task was preserved" (ref 156 = de Wit 2011).
- Rochester et al. 2005, *Arch Phys Med Rehabil* 86(5) 999–1006 — real-correct; quote, "Twenty subjects with idiopathic Parkinson's disease", 19% step-length increase verified. Direction as stated (cues reduce interference).
- Rochester, Galna, Lord & Burn 2014, *Neuroscience* 265 83–94 — real-correct; quote, 121/189, baseline demand controlled on both tasks, "no significant correlations with dual-task interference and global cognition, motor deficit, and executive function for either group", "PD-specific dual-task co-ordination deficit" all verified. Direction as stated.
- Sharp, Foerde, Daw & Shohamy 2016, *Brain* 139(2) 355–364 (Crossref issued 2015 online) — real-correct; full quote and "positively correlated with a separate measure of working memory performance" verified. Direction as stated (model-based impaired OFF, remediated ON, model-free untouched).
- Spildooren et al. 2010, *Mov Disord* 25(15) 2563–2570 — real-correct; 14/14/14, "during the off-period of the medication cycle", 37.5% vs 0% straight-line, "360° turning in combination with a dual-task is the most important trigger for freezing" verified.
- Vandenbossche et al. 2012, *Front Hum Neurosci* 6:356 — real-correct; both spans verified. Crossref's issued date is 2013-01 (online) while Europe PMC and the volume year give 2012; the page's 2012 is the standard form and is kept.
- Wu & Hallett 2005, *Brain* 128(10) 2250–2259 — real-correct metadata; **result misreported** (Critical 1), now fixed. Quote verified.
- Wu & Hallett 2008, *JNNP* 79(7) 760–766 — real-correct; 15 patients, 3 on the complex task, three-way attribution quote verified.
- Wu, Hallett & Chan 2015, *Neurobiol Dis* 82 226–234 — real-correct; both spans verified.
- Wu, Liu, Zhang, Hallett, Zheng & Chan 2015, *Cereb Cortex* 25(10) 3330–3342 (Crossref issued 2014 online) — real-correct; span verified.
- Wunderlich, Smittenaar & Dolan 2012, *Neuron* 75(3) 418–424 — real-correct; span verified.
- Yogev et al. 2005, *Eur J Neurosci* 22(5) 1248–1256 — real-correct; quote and "becomes attention-demanding" verified.
- Foerde 2018, *Curr Opin Behav Sci* 20 17–24 — Crossref metadata confirmed; no Europe PMC record; listed under Further Reading as unread and not cited in prose (confirmed by grep: the only prose mention is the Stated Limits disclaimer).
- Inline ↔ References: all 20 external References entries are cited inline; every inline cite has an entry; the two Map self-cites (21, 22) are the linked pages. Abstract marker: all 15 abstract-only sources carry "(abstract)" at first mention, in the table cells that name them, and in References. `find_superlative_claims` returned no lines.

### Attribution checks (§2.5)

- Source/Map separation: the instrumental authors' "goal-directed" is kept distinct from the Map's "self-initiated" throughout (Construct Gap section; lead sentence 2; Relation). No Map argument is put in a source's mouth. Redgrave's reply and Mi's Hernandez-based reconciliation are attributed to those authors.
- Position strength: de Wit "suggest"/"if anything" preserved; Sharp "surprisingly" preserved; Kelly "assert" is the right verb for a narrative review's claim.
- Qualifiers: one dropped qualifier found and restored (Critical 2).

### Reasoning-mode classification (§2.6, editor-internal)

- Engagement with Redgrave et al. (habitual-control reading): **Mode One** — the reading's own behavioural prediction, stated in its own terms and in de Wit's, is tested and fails on the direct test; the anatomy is left standing and their reply is quoted. No boundary substitution; no label leakage found.
- Engagement with the physicalist reading at the tenet boundary (Relation, Tenet 3 paragraph): **Mode Three** — honestly marked ("non-reductive physicalism with mental causation predicts as readily"; "the Map names no discriminator the physicalist reading fails to predict").

### Counterarguments Considered

- *Eliminativist / physicalist*: the whole survey concerns physically realised control systems and says nothing about consciousness. The page agrees (Relation: "Nothing here moves it"; felt-ness "untouched"). Bedrock beyond that.
- *Quantum skeptic*: nothing quantum is at stake. The page says so (Tenet 2 untouched).
- *Empiricist*: two patient studies, one female-only depletion result, fifteen abstracts. The page's Stated Limits already carry each of these; the medication p = .08 nuance was the one under-reported datum, now in.
- *Empiricist, on symmetry*: does the failure of the habitual prediction count as evidence for the willed-deficit reading? The page holds the line (Construct Gap: "It does not show that what fails is the selection of self-initiated action"; Relation: "compatible, not supported"), and the table's willed-deficit column is the kinesia page's stated prediction, not a claim that it was confirmed. Checked against the over-reach lens: no sentence lets the reversal read as support.
- *Buddhist philosopher*: "self-initiated" versus "cued" presupposes a self that initiates. The page does not adjudicate; the construct gap section already declines to identify either construct with conscious selection.

## Optimistic Analysis Summary

### Strengths Preserved

- The domain-indexed verdict (lead paragraph 2, table, "The Two Readings Against the Evidence") and the refusal of a single-system answer.
- The Construct Gap section as the page's governing caveat, and its closing sentence naming the substitution error any downstream article could make.
- The symmetric treatment: the habitual reading's *anatomy* survives, only its behavioural *prediction* failed; the freezing and self-paced rows stand to its credit.
- The separable-measures point (devaluation test proper vs competition test) drawn from de Wit 2012.
- Tenet 3 held at *compatible, not supported*, with the `tenets#^tenet-3-standing` note cited; Tenet 5 applied against every tidy story including the Map's.

### Enhancements Made

- Wu & Hallett control figures now correct and symmetric across 2005 and 2008 (Critical 1).
- de Wit 2011 prediction quoted with its qualifier and its status as a proposal (Critical 2); medication result stated with its p-value and the authors' caveat (Critical 3).
- Sharp/de Wit medication tension made visible (one clause).
- Roster stance sentence added to Stated Limits.

### Cross-links Added

None (the page already links every frontmatter sibling in body or Further Reading; the three inbound hosts were not touched).

## Remaining Items

- The research note's Wu & Hallett 2005 entry (L81) carries the "all controls" error; the note is a research artefact rather than a live article and was not edited. A future pass on the note could correct it.
- Foerde (2018) remains unread; if retrieved, the Knowlton-vs-devaluation "different things" paragraph (L47) is the place it would bear on.
- Sharp et al.'s effect sizes and medication-order controls remain abstract-only.

Would-mint tasks (not written to todo.md): none of P0–P2 weight. A P3 refine-draft on the research note to correct its Wu & Hallett 2005 line is the only candidate.

## Stability Notes

- Physicalist and eliminativist readers will hold that a survey of dopamine-dependent control systems has no bearing on consciousness; the page agrees and claims none. Bedrock; do not re-flag.
- The willed-deficit column of the table is the kinesia page's stated prediction. Its match with the instrumental results is reported as direction only, and the Construct Gap section blocks its promotion to support. A future review should not read the table as an overclaim unless prose elsewhere starts treating the match as confirmation.
- "Located as of 2026-09-30" and "a third may exist under other vocabulary" are the page's stated search limits, not an absence claim; a later literature-drift pass that finds a third patient devaluation study should add it rather than flag the count.