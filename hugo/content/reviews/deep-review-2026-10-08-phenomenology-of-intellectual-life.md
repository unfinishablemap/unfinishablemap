---
ai_contribution: 100
ai_generated_date: 2026-10-08
ai_modified: 2026-10-08 13:12:14+00:00
ai_system: claude-fable-5-1
author: null
concepts: []
created: 2026-10-08
date: &id001 2026-10-08
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-08 13:12:14+00:00
modified: *id001
related_articles: []
title: Deep Review - The Phenomenology of Intellectual Life
topics: []
---

**Date**: 2026-10-08
**Article**: [The Phenomenology of Intellectual Life](/topics/phenomenology-of-intellectual-life/)
**Previous review**: [2026-07-17](/reviews/deep-review-2026-07-17-phenomenology-of-intellectual-life/) (seventh deep review)
**Bucket**: MODIFIED since last review — three unreviewed strands, plus two source-fidelity defects that six prior ledgers had certified

## Diff Scoping

`git diff 0c48cbd650` (the 2026-07-17 review commit) shows three body changes no review has read:

1. **Tallis de-quote (2026-07-30 corpus sweep)** — `As Raymond Tallis sharpens: "Misrepresentation presupposes presentation."` → `Raymond Tallis sharpens the point: illusions presuppose experience.` Paraphrase, attributed as paraphrase; the 07-17 review's sole open item (verbatim-confirm the five-word string) is thereby discharged. No further action.
2. **Correlationism graft (2026-09-29 expand-topic secondary host)** — one clause appended to the "Constitution vs reliable correlation" paragraph plus a `related_articles` entry. Defective; fixed below.
3. **`structure-of-attention` Further Reading entry (2026-09-29)** — slug resolves; the gloss "willed/instructed/exogenous" matches that article's own vocabulary (38/16/10 occurrences). No action.

The lenses the driver asked for first (quote fidelity against the raw source; attribution keyed on surname+year) were then run over the whole article, not only the diff, because the prior ledgers certified metadata only.

## Web-Verify Ledger (raw-source greps, not metadata)

- **Pitt, D. (2004)** *The phenomenology of cognition, or, what is it like to think that P?* PPR 69(1):1–36 — metadata **real-correct**; content **real-wrong-attribution, corrected**. Full preprint text obtained from consc.net (`consc.net/event/neh/papers/pitt.pdf`, 52 pp.). Pitt's minimal pairs are centre-embedded, garden-path and "machine-gun" sentences — "The boy the man the girl saw chased fled", "The boat sailed down the river sank", the seven-buffalo sentence — read before and after explanation. Greps for `bank`, `riverbank`, `financial`, `ambigu*`, `homonym`, `two meanings`, `aphantas*`, `without imag*`, `no imag*` all return **zero**. Pitt's imagery passage argues only that phonological/orthographic imagery is not *identical* to the thought even if it always accompanies it. So of the three cases the article listed under "Pitt (2004) argues", only the recursion case is Pitt's; the lexical-ambiguity case and the aphantasia case were Map extensions presented as Pitt's. (The 2026-05-22 ledger's "the ambiguity and recursion cases are Pitt's ✓" was half wrong, and it was silent on the aphantasia case; "aphantasia" was coined in 2015, so Pitt 2004 could not have used it.) The article's own sentence was also not Pitt's ("The man who saw the woman who chased the dog ran" is nowhere in the paper). **Fix**: the paragraph now quotes Pitt's actual sentence and marks the other two cases as "the Map's extension rather than Pitt's"; "people with aphantasia" → "people who report no visual imagery" (the anachronistic term dropped; the claim is now Map-owned and modest).
- **Kounios, J. & Beeman, M. (2014)** *The cognitive neuroscience of insight.* Annu. Rev. Psychol. 65:71–93, DOI 10.1146/annurev-psych-010213-115154 — metadata **real-correct** (PubMed 24405359); content **real-wrong-result, corrected**. Full text obtained from the Beeman lab's hosted copy (sites.northwestern.edu). The paper's stated attributes of insight are: suddenness as a discrete all-or-none transition "with no intermediate states" (speed–accuracy decomposition, Smith & Kounios 1996), a burst of positive emotion/surprise that is explicitly "not a necessary feature", impasse-breaking restructuring (explicitly not a precondition), and substantial preceding unconscious processing (subliminal primes spark later insights). Greps for `confiden*`, `pop*`, `receiv*`, `verif*` (as a feature) return **zero**: "insight carries confidence before verification" is not in this paper — it belongs to the later accuracy literature (Salvi et al. 2016), which the article does not cite. Three prior ledgers (03-30, 04-04, 05-22) certified the "three features" without a grep. **Fix**: the three features are now the paper's own; and the cited-author-stance leg is discharged in prose — Kounios and Beeman explain the "received" quality by unconscious processing, and the Map's reading is marked as the Map's.
- **James, W. (1890)** *Principles of Psychology* — "feelings of relation": **real-correct**, 9 verbatim hits in the Gutenberg text (#57628), ch. IX.
- **James, W. (1902)** *Varieties of Religious Experience* — "self-surrender": **real-correct**, 16 hits in the Gutenberg text (#621) once the search key uses Gutenberg's U+2010 hyphen (an ASCII-hyphen grep returns zero — recorded so the next reviewer does not false-zero it). The article's gloss "in which the will stops struggling" is faithful: James (Lecture IX) writes that "the personal will must be given up" and that relief "refuses to come until the person ceases to resist, or to make an effort".
- **Strawson, G. (1994)** *Mental Reality* — foreign-language (Jacques/Jack) argument: **real-correct**; Pitt 2004 itself cites Strawson's "understanding experience" for the same point (preprint p. 40), cross-confirming the attribution.
- **Bayne, T. & Montague, M. (eds.) (2011)** *Cognitive Phenomenology*, OUP — **real-correct**; the volume contains Prinz, "The sensory basis of cognitive phenomenology" and Carruthers & Veillet, "The case against cognitive phenomenology" (publisher/catalogue contents). The body's dangling names "(Prinz, Carruthers)" now read "(Prinz, and Carruthers and Veillet, both in Bayne & Montague 2011)" — the missing co-author restored and one of the orphan References entries is now cited inline at zero cost.
- **Festinger 1957, Sosa 2007, Greco 2010, Plato *Meno* 97a–98b, Tallis 2011** — **real-correct**; standing from prior ledgers, no body change reopened them, no quoted strings involved.
- **Superlative sweep**: `find_superlative_claims` returns nothing. No currency defects.
- **References orphans** (Bergson, Chudnoff, Husserl, Nagel, Petitmengin, Schwitzgebel): retained by explicit decision in the 2026-04-04 review, confirmed 05-22. Not re-flagged as critical (recorded resolution), but see Remaining Items — the justifications given then ("Durée concept appropriately used", "introspective reliability challenge fairly represented") describe text that the coalesce removed; neither Bergson nor Schwitzgebel is mentioned in the live body.

## Pessimistic Analysis Summary

### Critical Issues Found
- **Pitt 2004 attribution** (above): two of three listed cases were not Pitt's; one used a term coined eleven years after the paper. Fixed.
- **Kounios & Beeman 2014 result** (above): one of three "features" is absent from the paper. Fixed; Map/source separation now explicit.
- **Correlationism graft contradicts its own target page.** The 09-29 clause called Meillassoux's correlationism "constitutive"; the sibling article it links (L76) says correlationism is an *access* thesis that "does not assert" a constitutive contribution (Gabriel), and reserves "constitutive" for the Map's fourth rung. Old: `"correlation" here means reliable co-variation, the opposite of the constitutive correlationism Meillassoux names.` New: `"correlation" here means reliable co-variation, a different sense from the access thesis Meillassoux names correlationism.` ("Opposite" was also wrong — the two are homonyms, not contraries.)
- **Internal tension in the AI section.** After arguing against functionalist reduction, the article said an understanding AI "must have something functionally equivalent to understanding's phenomenology" — conceding exactly the functional-equivalence reading PCT denies. Old: `It suggests that if AI genuinely understands, it must have something functionally equivalent to understanding's phenomenology — whatever the substrate.` New: `It implies that if an AI genuinely understands, it has understanding's phenomenology — whatever the substrate.`

### Medium Issues Found
- Dangling in-text names (Prinz, Carruthers) with no References entry — resolved by attaching them to the existing Bayne & Montague 2011 entry (Veillet restored).
- Three passages duplicated the lead or each other (the "work/strain/reach" triad at L116 repeats the lead verbatim; L192's coupling argument repeats L186's; L172's trailing list repeats the five-mode section). Tightened to offset the additions.

### Counterarguments Considered
- Eliminativist, Buddhist no-self, functionalist-reduction, MWI — all bedrock per the standing stability notes; not re-flagged.

## Reasoning-Mode Check
- Functionalist (Pitt): Mode One — now rests on Pitt's actual minimal pairs, which is a stronger in-framework case than the invented ones (the orthography is literally fixed while the experience changes). Deflationary replies named with correct co-authorship.
- Illusionist: Mode Two — unchanged; Tallis paraphrase.
- MWI: Mode Three — unchanged, self-marked "honest tension".
- No label leakage (grep clean).

## Calibration
Unchanged: observation and constitution claims, no five-tier slippage. The new Kounios & Beeman sentence explicitly declines to let the authors' finding carry the Map's phenomenal reading.

## Optimistic Analysis Summary

### Strengths Preserved
- The "What Would Challenge This View" section (genuine-risk vs partially-insulated split) — untouched.
- The constitution-vs-co-variation paragraph — only the final clause changed.
- Five-modes architecture and the Relation section — untouched.

### Enhancements Made
- Pitt's real sentence now does the work; the Map's extensions are owned as the Map's.
- Kounios & Beeman's own explanatory stance recorded in prose (cited-author-stance leg).

### Cross-links Added
- None new (the two 09-29 links were verified rather than added).

## Length
3317 → 3368 words (+51; topics gate 4,000, headroom 631). Additions: Pitt +41, Kounios +40; offsets: L116 −14, L172 −16, L192 −12 (approx.). Soft-band article, length-neutral mode approximated; well below the hard gate.

## Remaining Items
- **Low — orphan References (Bergson 1889, Chudnoff 2015, Husserl 1900/2001, Nagel 1986, Petitmengin 2006, Schwitzgebel 2011).** The 04-04 retention rationale cites body text that no longer exists after the 06-13 coalesce. Either cite each inline where apt (Schwitzgebel at the "Partially insulated criteria" paragraph on introspective convergence; Petitmengin at "Contemplative Evidence"; Chudnoff at "The Click of Comprehension") or remove. Not done here to avoid oscillating against a recorded decision; a human call.
- **Low — sibling-page check.** `topics/correlationism-and-the-ancestrality-argument` L124 glosses this article as "the opposite of Meillassoux's sense"; same "opposite" slip, in the other host. Live text: `- [[phenomenology-of-intellectual-life]] — Where "correlation" means reliable co-variation, the opposite of Meillassoux's sense`. Suggest "a different sense from Meillassoux's". Not edited: out of this review's file scope.
- **Low — corpus sweep.** Other pages may carry the "Kounios and Beeman … confidence before verification" or the "Pitt … aphantasia" formulation (the coalesce merged nine articles; the originals are archived). Grep `confidence before verification` and `aphantasia` near `Pitt` across `obsidian/` and `archive/` before the next cross-review.

## Stability Notes
Seventh deep review. Bedrock disagreements unchanged from the 07-17 notes (eliminativist, Buddhist no-self, functionalist reduction at framework level, MWI indexical). Add one stability note for future reviews: **the Pitt and Kounios & Beeman content attributions have now been grepped against the raw sources** (consc.net preprint; Beeman-lab PDF) — a future ledger may cite this review rather than re-fetch, unless the body text at those two loci changes.

## Word Count
- Before: 3317
- After: 3368 (+51)