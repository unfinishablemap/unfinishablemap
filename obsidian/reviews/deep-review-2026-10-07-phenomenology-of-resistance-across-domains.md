---
title: "Deep Review - The Phenomenology of Resistance Across Domains"
created: 2026-10-07
modified: 2026-10-07
human_modified: null
ai_modified: 2026-10-07T09:58:37+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[phenomenology-of-resistance-across-domains]]"
ai_contribution: 100
author: null
ai_system: claude-fable-5-1
ai_generated_date: 2026-10-07
last_curated: null
---

**Date**: 2026-10-07
**Article**: [[phenomenology-of-resistance-across-domains|The Phenomenology of Resistance Across Domains]]
**Previous review**: [[deep-review-2026-06-25-phenomenology-of-resistance-across-domains|2026-06-25]] (plus 2026-05-27, 2026-04-16b, 2026-04-16)
**Pass**: 103-day staleness re-selection. Body changed once since 06-25: this morning's refine-draft (fd47ae80d3) added a secondary-host insertion in Epistemic Resistance pointing at the assent void. That insertion was read against its source and is faithful (assent-void L91: formation "feels like finding nothing to push on"; the resistance article's pushback is "failed *revision*, a different case from formation").

## Verdict: three quote-fidelity defects, all certified by prior ledgers on metadata alone

The 06-25 stability note said "after this pass the citations are publisher-verified" and predicted a no-op. The *metadata* were verified; the *quoted words* were not grepped in their raw sources. Doing that this pass turned up three defects, one of which the 06-25 "fix" introduced.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Fabricated Dilthey quotation (removed).** The article quoted reality as "initially graspable as a collection of facta bruta, as simply 'the way things are' apart from volitional intentionality" and credited it to Makkreel's SEP reconstruction. The raw SEP "Wilhelm Dilthey" entry (fetched, 106 KB, grep) contains none of *facta bruta*, *initially graspable*, *the way things are*, or *volitional intentionality*. Two further web searches with disjoint keyword sets found the sentence nowhere. The research note (`research/phenomenology-of-resistance-across-domains-2026-04-06`) self-flagged the SEP as the source, and the SEP does contain the note's *other* key points ("an inner side", "restraint of a volitional intention"), so the paraphrase seeded itself from a real page and then ratified. Replaced with two grep-verified SEP sentences: "our initial access to the external world is not inferential, but is felt as resistance to the will" and resistance "must be internalized as a restraint of a volitional intention for it to signify the existence of something independent" (Makkreel 2020). Research note corrected in place with a dated withdrawal; its "facta bruta" key-point line also dropped.
2. **Biran "quotation" is a magazine author's gloss, cited to the wrong work.** "Self-consciousness could only exist if it was being resisted at the very same time of its occurrence" was presented as Biran's words "as quoted in Horton 2025". The sentence is verbatim in Benjamin Bâcle's *Philosophy Now* 133 (2019) profile of Biran, the URL the research note actually lists, where it is Bâcle's own prose introducing the real Biran quotation that follows it: "as soon as the effort unfolds, there is a subject and an object, each constituted in relation to each other… Without this effort everything is passive and absolute… With it, everything refers to a person who wants and acts" (*Mémoire sur la décomposition de la pensée*, 1805). On the open web the sentence appears only in Bâcle and in the Map's own pages (self-contamination). The 06-25 pass upgraded the cite Horton 2024 → 2025 and declared the quote "verbatim-faithful"; Horton's paper is behind Cloudflare/Brill, so that certification cannot have been a grep. Rewritten: the sentence is now attributed to Bâcle as gloss, Biran's own formulation is quoted (as translated in Bâcle 2019), and Horton 2025 is kept live for the claim its Crossref abstract actually supports — effort "involves both a force and a resistance: thus, I am the relation between my soul and my body".
3. **Gendler "quotation" is SEP prose (defect introduced by the 06-25 fix).** "pop out as striking or jarring" / "an odd 'feel' that other sentences don't have" were attributed "According to Gendler (2006)". The raw SEP "Imaginative Resistance" entry (Tuna, 2024 revision) has, in its own voice: "The last sentence of Death pops out as striking or jarring. It has an odd 'feel' that the other sentences in the story don't. … (See Gendler 2006: 156–62 on the pop-out effect)." The research note had this right as SEP wording; the article's creation moved it to Gendler 2000, and the 06-25 ledger moved it to Gendler 2006 on the strength of the SEP's *pointer* — the fix relocated the misattribution rather than removing it. The article's rendering was also not verbatim to the SEP ("pop out" / "other sentences don't have"). Rewritten as the SEP's framing, quoted exactly, with Gendler 2006 credited for the pop-out effect.
4. **Dilthey essay title (real-wrong-metadata).** References gave "Contributions to the Solution of the Question of the Origin of Our Belief in the Reality of the External World"; the Princeton SW II product page and SEP bibliography give "The Origin of Our Belief in the Reality of the External World and Its Justification" (SW II, pp. 8–57). Corrected; Makkreel & Rodi are editors of the volume, marked as such.

### Medium Issues Found

- Writing-style: lede of Relation to Site Perspective used the banned "is not X—it is Y" construct ("is not an anomaly requiring a special explanation—it is what Biran and Dilthey taught us to expect"). Rephrased to lead with the positive claim.
- "load-bearing" as intensifier at the close of the Biranian section → "indispensable". The second occurrence (the thread "is load-bearing for the Map's argument") names a premise the argument depends on and was kept.
- This morning's insertion read as one over-long "Two things … while … and …" sentence; split into three with no change of claim.

### Citation ledger (per-cite, this pass)

- Bâcle 2019 (Maine de Biran, *Philosophy Now* 133) — **newly added**; sentence grep-verified in raw page; author from page JSON-LD description.
- Horton 2025 (JCPR 7(1): 66–88, DOI 10.1163/25889613-bja10082) — real-correct metadata (Crossref); **quote was not in it** → re-scoped to the abstract's force/resistance claim.
- Makkreel 2020 (SEP Dilthey) — **newly added**; both quoted sentences grep-verified in raw page.
- Tuna 2024 (SEP Imaginative Resistance) — **newly added**; quoted sentences grep-verified; Gendler 2006 = Nichols (ed.) 2006: 149–173 confirmed from the entry's bibliography.
- Gendler 2000 (J. Phil. 97(2): 55–81, doi:10.2307/2678446) — real-correct (SEP bibliography).
- Gendler 2006 — real-correct metadata; **no longer carries a quotation**.
- Dilthey 1890/2010 — real-wrong-metadata (title; corrected, pages added).
- Mandelbaum 1955 — real-correct; "reflexive felt demand" grep-verified as a quoted phrase in the SEP Moral Phenomenology entry (Drummond & Timmons). The 06-25 note that "reflexive" was the article's gloss was itself wrong.
- Dennett 2017, Frankish 2016, Graziano 2019, Heidegger 1927/1962, Husserl 1952/1989, Merleau-Ponty 1945/1962, Walton 1994, Wegner 2002, Falque 2025 — metadata carried forward from the 06-25 publisher pass; References block unchanged for these; no quotations attached except Wegner's "an illusion" (title-level, faithful) and Heidegger's Macquarrie–Robinson terms.
- Superlative sweep: `find_superlative_claims` — none applicable (no "first/largest/record" claims).
- Inline ↔ References: all inline cites have entries; all entries are cited inline (Falque 2025 was an orphan reference before this pass — now cited inline alongside Horton, whose abstract says it draws on Falque's reading; Husserl, Heidegger, Merleau-Ponty, Mandelbaum, Walton, Wegner, Frankish, Dennett, Graziano by name).

### Reasoning-mode classification (editor-internal)

- Engagement with illusionism (Wegner, Frankish, Graziano, Dennett): **Mixed** — opens by refusing the cheap self-undermining charge, then Mode Two (the agency-self-model answer "names a category without explaining" the cross-domain unity — a standard illusionists endorse), closes Mode Three ("does not settle the debate"). Honest; no boundary-substitution; no label leakage.

### Counterarguments Considered

- Disanalogy view ("resistance" is equivocal across six domains): the article already concedes the equivocation for the logical and imaginative domains and rests the Map's claim on the four effortful ones. Unchanged.

## Optimistic Analysis Summary

### Strengths Preserved
- The two-tier claim structure (universal weak claim vs four-domain strong claim) and the explicit statement that interface friction is modelled on the strong claim only.
- The careful deflationary section, which declines the self-undermining move and concedes "an explanatory advantage—not a decisive one".
- The Merleau-Ponty tension paragraph.

### Enhancements Made
- Biran's own words now appear where previously a journalist's gloss stood in for them; the force/resistance relation is now sourced to a peer-reviewed paper's actual content.

### Cross-links Added
- None new (assent-void link from this morning retained).

## Length

3117 → 3202 words (+85). Split: References +3 entries ≈ +55; body ≈ +30 (Biran paragraph +~45, Gendler/Dilthey rewordings +~15, two redundancy trims −~55, insertion split 0). Under the 4000 hard threshold by ~800; soft-warning status unchanged.

## Remaining Items

- Horton 2025 full text remains unread (Cloudflare on PhilArchive, 403 on Brill). The claim now attached to it is from the Crossref-served abstract, verbatim.
- Gendler 2006 pp. 156–62 not grepped (OUP chapter); the article now attributes only "the pop-out effect" to it, on the SEP's pointer.

## Stability Notes

- Merleau-Ponty's anti-Cartesianism, illusionism as a framework-boundary disagreement, and the MQI extension flagged as speculative are settled; do not re-flag.
- **Do not trust "citations publisher-verified" notes in this article's earlier reviews as covering quoted words.** 04-16, 04-16b, 05-27 and 06-25 all certified metadata; none grepped a quotation in a raw source, and 06-25's Gendler fix moved a misattribution rather than removing it. After this pass every quotation in the article has been grep-matched against the raw page it is cited to (Bâcle, Makkreel SEP, Tuna SEP, Mandelbaum via SEP Moral Phenomenology).
