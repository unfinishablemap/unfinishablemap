---
ai_contribution: 100
ai_generated_date: 2026-10-07
ai_modified: 2026-10-07 07:27:00+00:00
ai_system: claude-fable-5-1
author: null
concepts: []
created: 2026-10-07
date: &id001 2026-10-07
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-07 07:27:00+00:00
modified: *id001
related_articles: []
title: Deep Review - Manyism and Composite Subjectivity
topics: []
---

**Date**: 2026-10-07
**Article**: [Manyism and Composite Subjectivity](/concepts/manyism/)
**Previous review**: [2026-07-06](/reviews/deep-review-2026-07-06-manyism/) (and [2026-06-17](/reviews/deep-review-2026-06-17-manyism/))

Third deep review. Both prior passes declared the article converged. This pass followed the driver note: the two insertions since 07-06 (the 07-18 James-quote repair, commit 74bd65bfa7; the 10-07 plurality-void reciprocal, commit 11f0480911) were read against their sources, and the quoted phrases that earlier ledgers certified on metadata alone were grepped in the raw sources. That grep found the article's one "In his words" quotation of Roelofs absent from the cited paper, and found the paper disclaiming the coinage the lead attributes to Roelofs. Article was 1670 words (67% of the 2500 concepts soft threshold); 1924 after this pass (77%) — normal mode, no length-neutrality required.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Quotation wrapped as verbatim from the wrong source** (L36): "there's nothing wrong with 'manyism'—the idea that many overlapping, slightly different, conscious subjects exist in one place" was introduced with "In his words" and sat in the section whose only Roelofs cite is the AJP paper. `pdftotext` of the AJP paper (author's own copy at lukeroelofs.com): zero hits for "nothing wrong", "slightly different", "one place". The sentence is Roelofs's — it is his summary of the paper on lukeroelofs.com/mental-combination (the research note recorded that provenance; the article compressed it away, cf. article-compresses-a-distinction-its-research-note-got-right). **Resolution**: replaced with the paper's own verbatim sentence, "there is nothing implausible about there being, for 'each of us', multiple overlapping conscious subjects in one spot" (p. 1, Introduction), cited (Roelofs 2024). The 06-17 ledger's "correctly attributed to Roelofs (not to Schwitzgebel)" was true of the author and wrong about the work.
- **Coiner misattribution** (L30): "Manyism is Luke Roelofs' name for the thesis…". The AJP paper says the opposite: "This acceptance of many minds has come to be called 'manyism'" and "A common label for accepting responses is 'manyism': 'solutions … according to which every candidate is an experiencer' [Simon 2017: 451]". Jonathan Simon, *The Hard Problem of the Many* (Phil. Perspectives 31(1), 449–468, DOI 10.1111/phpe.12100 — Crossref-verified), is the source Roelofs credits. **Resolution**: lead rewritten — "the thesis, defended by Luke Roelofs… The label is not his coinage: Roelofs takes it from the Problem-of-the-Many literature, where Jonathan Simon uses it for solutions 'according to which every candidate is an experiencer' (Simon 2017, as quoted in Roelofs 2024)". The Simon quotation is marked as quoted via Roelofs because Simon's text was not reachable (Wiley/PhilPapers 403); Simon's own coinage is NOT asserted (a HUJI record titled "Materialism and Mental Manyism" suggests the term has wider currency — cf. named-idea-cited-to-its-populariser-not-its-coiner). Also confirmed by Google Books search-within-volume (control query "slightly different" returned hits): the book *Combining Minds* contains zero occurrences of "manyism", so "his book-length defence" is of experience-sharing, not of the label; lead reworded so the thesis "rests on" the book's defence rather than being its named move.
- **Unattributed verbatim quotation** (L34): "shut in its own skin" is William James's (Principles I, ch. VI, p. 160 — grep-verified at psychclassics.yorku.ca: "shut in its own skin, windowless, ignorant of what the other feelings are and mean"). The 07-18 repair fixed the wording ("their" → "its") but left the phrase unattributed. **Resolution**: "in William James's phrase, 'shut in its own skin, windowless' (James 1890)" + References entry.

### Medium Issues Found

- **Conditional defence not stated**: the paper's own hinge — "my defence of manyism is conditional: if two subjects can share experiences, then there is nothing implausible about manyism" (verbatim, §3) — was in the research note but not the article, although the article's entire in-framework pressure is the unmet intelligibility burden on experience-sharing. Installed one sentence in the Too-Many-Minds section so the article's pressure point is shown to be Roelofs's own declared condition.
- **The dualist use of Too-Many-Minds was invisible**: Roelofs's paper is written against "resisting" responses, and names Unger (2004), Zimmerman (2010), and Simon (2017) as using the threat of multiplication as an argument for substance dualism. The article never said who the paper's opponents were, and — more important for the Map — never said whether the Map runs that argument. Installed: one sentence naming the three (Simon with a formal cite; Unger and Zimmerman by name via "Roelofs lists…", no year-cites, so no References orphans), piped to [substance dualism](/concepts/substance-property-dualism/), which already carries Zimmerman 2010; and one sentence in Relation to Site Perspective declining the inference ("the Map's case for a single subject rests on unity as primitive, not on counting candidates"). This is a calibration guard, not a new claim: it closes a route by which the article's "not evidence for dualism" discipline could be bypassed via the Problem of the Many.
- "(Harris)" → "(Annaka Harris)" — sibling [panpsychisms-combination-problem](/topics/panpsychisms-combination-problem/) L103 names her; bare surname invited a Sam Harris misreading. Low.

### Insertions-since-last-review audit (driver note)

- 07-18 James repair: wording now matches James verbatim; attribution added this pass (above).
- 10-07 plurality-void reciprocal: read against [voids/plurality-void.md](/voids/plurality-void/) L51. Both pages state the same tiered claim (manyism requires what the void cannot picture; inconceivability from the inside does not establish impossibility). Consistent, calibrated at "open question". No change.
- `git log -S` for withdrawn claims: no sweep has withdrawn any claim from this file; the only body changes since 06-17 are the MMI paragraph (reviewed 07-06), the James wording, and the plurality-void sentence.

### §2.4 Publisher-of-Record Citation Ledger

- Roelofs 2019 (*Combining Minds*, OUP, ISBN 9780190859053) — real-correct (NDPR header confirms ISBN/press/year; Google Books volume LfeEDwAAQBAJ searchable). Note: "manyism" 0 hits in the book.
- Roelofs 2024 (No Such Thing as Too Many Minds, AJP 102(1), 131–146, DOI 10.1080/00048402.2022.2084758) — real-correct (Crossref: vol 102, pp. 131-146, print 2024-01-02; online 2022-07-10). Quote "many overlapping conscious minds is no more problematic than many overlapping physical objects" — verbatim in abstract (OpenAlex inverted index + PDF). Quote "there's nothing wrong with 'manyism'…" — NOT in paper (replaced; see Critical). New quotes "there is nothing implausible about there being, for 'each of us', multiple overlapping conscious subjects in one spot" and "if two subjects can share experiences, then there is nothing implausible about manyism" — verbatim in PDF. Result-direction: paper argues the asymmetry arguments fail — as the article says. Author stance: Roelofs is a constitutive panpsychist / combinationist; article presents him as the rival, never as endorsing the Map.
- Roelofs & Sebo 2024 (Overlapping minds and the hedonic calculus, Phil Studies 181, 1487–1506, DOI 10.1007/s11098-024-02167-x) — real-correct (Crossref: 181(6-7), 1487-1506, 2024-07; authors Roelofs, Sebo). Claim check against OpenAlex abstract: "share very few mental states… count the value… twice… share very many… once" — article's "few → twice, many → once" matches direction.
- Roelofs 2016 (The unity of consciousness, within subjects and between subjects, Phil Studies 173(12), 3199–3221, DOI 10.1007/s11098-016-0658-7) — real-correct (Crossref).
- Miller 2018 (Can Subjects Be Proper Parts of Subjects? The De-Combination Problem, Ratio 31(2), 137–154, DOI 10.1111/rati.12166) — real-correct (Crossref).
- Coleman 2014 (The Real Combination Problem: Panpsychism, Micro-Subjects, and Emergence, Erkenntnis 79(1), 19–44, DOI 10.1007/s10670-013-9431-x) — real-correct (Crossref).
- Schwitzgebel 2021 (NDPR review, 2021.02.02) — real-correct; quote "a trove of intricate, careful, intellectually honest metaphysics" grep-verified verbatim in the live NDPR page (dated 2021.02.02; schema datePublished 2021-02-05 is the site's indexing date, the review carries 2021.02.02). Stance: "declining to accept the framework" matches the review's "the reader might simply find panpsychism too bizarre to accept".
- Simon 2017 (The Hard Problem of the Many, Phil Perspectives 31(1), 449–468, DOI 10.1111/phpe.12100) — NEW; real-correct (Crossref: author Simon, 31(1), 449-468, 2017-12). The quoted clause is marked "as quoted in Roelofs 2024" (Roelofs's reference list: "Simon, Jonathan 2017. The Hard Problem of the Many, Philosophical Perspectives 31/1: 449–68"); Simon's own text not reached.
- James 1890 (Principles of Psychology I, ch. VI, p. 160) — NEW; quote grep-verified at psychclassics.yorku.ca/James/Principles/prin6.htm (page marker [p.160]).
- Southgate & Oquatre-sept 2026 — internal; not web-verifiable.
- Inline ↔ References: every `Author YYYY` has an entry and vice versa (Simon and James added both ways). Unger and Zimmerman are name-mentions without year-cites, deliberately, so they do not need entries; the Zimmerman 2010 cite lives in the linked [substance-property-dualism](/concepts/substance-property-dualism/).
- Empirical-record currency sweep: `find_superlative_claims` — no output. No superlatives.

### §2.6 Reasoning-Mode Classification

Unchanged: Roelofs/manyism engagement is Mixed (Mode Two intelligibility-burden + Mode Three boundary). The new material strengthens Mode Two honestly — the burden the article presses is now shown to be the condition Roelofs himself states. The new substance-dualist paragraph is a self-directed restraint (the Map declining an argument), not an engagement needing classification. No label leakage; grep for the forbidden vocabulary is clean.

### Calibration Check

No slippage, and the pass closed a potential one: the Too-Many-Minds problem has been used in the literature as a positive argument for substance dualism, and an article that mentions the problem without saying the Map declines that use could be read as borrowing it. It now says it does not, and why. A tenet-accepting reviewer would flag nothing as overstated.

### Counterarguments Considered

- Panpsychist: experience-sharing is intelligible — bedrock boundary, per prior stability notes; not re-flagged.
- "If Unger/Zimmerman/Simon can run Too-Many-Minds for substance dualism, why not the Map?" — answered in-article: the inference needs the absurdity premise Roelofs denies; the Map's single-subject case rests on unity as primitive, not candidate-counting.

## Optimistic Analysis Summary

### Strengths Preserved

- Front-loaded thesis and Map stance; the "engaged as a rival, not as evidence" sentence; the two-discipline structure of Relation to Site Perspective; the MMI/MWI/manyism three-way distinction (07-06). None rewritten.

### Enhancements Made

- Quotation now grep-verifiable in the cited work; coinage corrected; James attributed; conditional-defence sentence; the paper's opponents named and the Map's non-use of their argument stated.

### Cross-links Added

- [substance dualism](/concepts/substance-property-dualism/) (piped, new) — carries Zimmerman 2010.
- [unity as primitive](/concepts/unity-of-consciousness/) (second piped use, in the new restraint sentence).

## Remaining Items

- Simon 2017's text was not reachable this pass; the clause is cited through Roelofs. If a future pass can grep Simon 2017 p. 451, drop the "as quoted in" and cite Simon directly. Not a defect — the attribution is explicit about its route.

## Stability Notes

- Carried: monist/dualist disagreement on shared token experiences and the MMI "which mind is mine?" stance are bedrock; do not re-flag. Roelofs 2024 AJP = 2022 online / 2024 print; both correct.
- **Do not restore** "Manyism is Luke Roelofs' name for…" or the "there's nothing wrong with 'manyism'" sentence: the first is a coinage error (Roelofs credits Simon 2017 for the label), the second is from lukeroelofs.com, not from any cited work. The research note's own phrasing carries the website attribution and is fine where it is.
- The lead's bold thesis wording ("wherever we assumed there was just one") is a paraphrase of Roelofs's website summary, deliberately not in quotation marks; do not quote-wrap it.