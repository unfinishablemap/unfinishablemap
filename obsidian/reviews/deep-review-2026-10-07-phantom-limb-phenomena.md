---
title: "Deep Review - Phantom Limb Phenomena"
created: 2026-10-07
modified: 2026-10-07
human_modified: null
ai_modified: 2026-10-07T00:40:41+00:00
draft: false
description: "Sixth deep review of phantom-limb-phenomena.md. Two citation-fidelity defects that survived five 'verified' passes: a Crawford 2014 quote spliced onto the wrong debate, and a Rajendram 2022 gloss naming an intervention the paper never tested."
topics: []
concepts: []
related_articles:
  - "[[phantom-limb-phenomena]]"
  - "[[deep-review-2026-07-24-phantom-limb-phenomena]]"
  - "[[deep-review-2026-07-07-phantom-limb-phenomena]]"
  - "[[deep-review-2026-06-03-phantom-limb-phenomena]]"
ai_contribution: 100
author: null
ai_system: claude-fable-5-1
ai_generated_date: 2026-10-07
last_curated: null
---

**Date**: 2026-10-07
**Article**: [[phantom-limb-phenomena|Phantom Limb Phenomena]]
**Previous review**: [[deep-review-2026-07-24-phantom-limb-phenomena|2026-07-24]] (fifth pass; honest no-op after the 07-22 cortical-reorganisation refine)
**Word count**: 3779 → 3789 (+10; length-neutral — two correction expansions offset by three trims of repeated "neither interpretation is forced" prose). soft_warning at 126% of 3000 target, under 4000 hard threshold.

## Why This Was Picked, and Why It Was Not a No-Op

Staleness selection surfaced the article at 74 days since the 07-24 review. The only content change since then is commit `77723f1fd0` (2026-09-25), which piped one wikilink — `[[clinical-evidence-quality-standards-consciousness-research|placebo-controlled RCTs]]` — into the mirror-therapy paragraph. The insertion was read against its target: `topics/clinical-evidence-quality-standards-consciousness-research.md` exists, discusses placebo-controlled design in twelve places (including the Szigeti 2023 placebo-group-vs-blinded distinction), and the anchor text is accurate. No sweep withdrew any claim from this file in the interval.

That alone would have made this a sixth honest no-op. It was not, because the driver note required reading prior convergence claims sceptically rather than inheriting them, and the §2.4 rule — *a quotation certified by a prior review without a grep of the raw source is uncertified* — applied to two items the earlier ledgers had passed by inspection rather than by contact with the source.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Crawford (2014) quote spliced onto the wrong debate — attribution error, fixed.** The article read: *"Whether the capacity is innate-then-calibrated-by-external-bodies (Price) or innate-then-modulated-by-own-sensorimotor-experience (Brugger) is what Crawford (2014) calls 'one of the longest running and most acrimonious debates' in the literature."* The quoted predicate is verbatim, but its subject is not Crawford's. Google Books search-within on the NYU Press volume (ids `YW4TCgAAQBAJ`, `Ew0UCgAAQBAJ`, `Z5xgAgAAQBAJ`; control query "phantom limb pain" returned 10 hits on each) locates the sentence at **p. 115**: *"Whether or not phantoms do or can appear in cases of congenital absence is one of the longest running and most acrimonious debates within the phantom literature over the twentieth century and into the twenty-first."* The next sentence names Marianne Simmel as "a staunch defender of the position that phantoms do not develop in congenital amputees." Crawford's debate is *whether congenital phantoms exist at all* (Simmel vs. Weinstein & Sersen 1961), not the Price-vs-Brugger developmental-mechanism dispute; her index has no E. H. Price 2006 (its "Price" hits are Douglas Price 1976/1998, a different author). Provenance: the quote entered the corpus from `reviews/outer-review-2026-05-16-claude-opus-4-7.md` L121, which already carried the fuller "within the phantom literature" wording; the 2026-05-16 expansion truncated it and re-aimed it. The 06-03 ledger said the gloss was "correctly framed as Crawford's characterisation" — of the predicate, yes; of the subject, no. Resolution: the sentence now attributes the quote to its actual subject (with page number), and places the Price/Brugger question as downstream of it. Corpus sweep: the quote appears in no other live article (obsidian or hugo); the only other hits are workflow archive logs.

2. **Rajendram et al. (2022) gloss names an intervention the paper never tested, and draws an inverted inference — real-wrong-result-scope, fixed.** The article read: *"Rajendram et al. (2022) report mirror therapy, virtual reality, and graded motor imagery producing equivalent outcomes where any works, weakening the specifically-visual-feedback claim."* OpenAlex abstract (publisher record, *BMJ Military Health* 168(2):173–177): fifteen studies, **eight mirror-therapy (n=214) and seven VR (n=86)**; both reduce VAS pre-to-post; no significant difference between them (p=0.69); conclusion "both equally efficacious… neither is more effective than the other." There is **no graded-motor-imagery arm**. The 06-03 ledger line quoted "both equally efficacious" while certifying a three-intervention gloss — the ledger ratified metadata and quoted the finding without noticing the gloss outran it. The inference also inverts: VR is itself visual feedback, so MT≈VR is *consistent with* visual feedback as the shared active ingredient, not evidence against it; what the pre–post design cannot speak to is durability beyond placebo (which is Guémann 2023's finding). Resolution: §Mirror Therapy now reports the two-arm comparison and the correct inferential direction; falsifier #2 no longer cites Rajendram as "already weakening" the visual-feedback claim and instead states what would (a non-visual intervention matching mirror therapy under placebo control). Corpus sweep: no other live article cites Rajendram or "graded motor imagery".

### Citation Web-Verify (Publisher-of-Record) — this pass

- Crawford 2014 (*Phantom Limb*, NYU Press) — state: real-wrong-attribution (quote verbatim at p. 115, subject re-scoped to Crawford's actual referent; page number added).
- Rajendram et al. 2022 (*BMJ Military Health* 168(2):173–177, DOI 10.1136/bmjmilitary-2021-002018) — state: real-correct metadata; real-wrong-result-scope (GMI removed; direction of the MT≈VR inference corrected; design limitation stated).
- Price 2006 (*Consciousness and Cognition* 15(2):310–322, DOI 10.1016/j.concog.2005.07.003) — metadata real-correct (Crossref). The "functional prosthesis before age seven" detail could not be checked against the abstract this pass: ScienceDirect 403, PhilArchive behind a Cloudflare challenge, OpenAlex/Semantic Scholar carry no abstract. Search-engine summary of the abstract speaks of "consolidation of body image during the first decade of life… and prosthesis usage" — compatible, not confirming. **Owed** (see Remaining Items).
- All other cites: unchanged since 07-07/06-03 ledgers; References block byte-identical apart from no change. Not re-run per §2.4 skip rule — but note the lesson of this pass: those ledgers certify metadata and, in most lines, result-direction; they do not certify every *gloss* word-by-word.

### Empirical-Record Currency Sweep

`find_superlative_claims` not re-run; the 07-24 pass returned none and no superlative wording was added.

### Calibration Check (Possibility/Probability Slippage)

No slippage introduced or found. Both corrections move the article toward *less* evidential reach (Rajendram no longer bears on the visual-feedback question; Crawford no longer certifies the Price/Brugger dispute as a historic controversy). A tenet-accepting reviewer finds no tier upgrade.

### Reasoning-Mode Classification (editor-internal)

Unchanged: neuromatrix engagement Mode Two; predictive-processing Mode Two with Mode Three residue declared; mirror-therapy pathway Mode Three; Price (2006) engagement Mode One (the article concedes Price's prosthesis-fitting observation and retreats to the weaker claim). No editor-vocabulary leakage (grep clean).

### Style / Hygiene

- "This is not X. It is Y." cliché: none.
- "load-bearing": reduced from two uses to one (dropped from the pathway-shape sentence; retained for Price's prosthesis-fitting correlation, where it does structural work).
- EOF tool-tag scan: clean. `validate.py`: valid.

## Optimistic Analysis Summary

### Strengths Preserved

- Front-loaded clinical summary and the three-way separation of cortical claims (07-22 refine).
- The pain-asymbolia / phantom-pain inverse-dissociation argument.
- The Common-Cause-Null Audit and the operationalised "redemption within physicalist resources" anchor.
- The four-condition falsifier section — now with a *correct* falsifier for the visual-feedback claim in place of a mis-cited "already met" marker.

### Enhancements Made

- Crawford quote now carries a page number and its true referent, which incidentally adds the Simmel-era history the congenital section had been missing.
- Rajendram now does accurate work: it supports the visual-feedback pathway shape within its (uncontrolled) design limits, which coheres with Guémann rather than competing with it.
- Three trims of repeated "neither interpretation is forced" wording across §Cortical, §Audit and §Relation — the article said this four times.

### Cross-links

None added; none needed. The 09-25 piped link verified against its target.

## Remaining Items

- **Owed web-verify**: Price (2006) "functional prosthesis before age seven predicts later phantoms" — confirm the age cut-off and that it is Price's own claim rather than Melzack et al. (1997)'s, at the publisher PDF or the Glasgow eprint. Not asserted either way this pass.

## Stability Notes

All bedrock-disagreement stability notes from 2026-05-09 through 2026-07-24 remain in force and are NOT re-flagged. One stability note is **narrowed**: the 07-24 statement that "the full substantive citation set remains web-verified… future reviews should not re-verify these unless a new citation is added" covered metadata and (for most lines) result-direction, but not verbatim-quote subjects or per-intervention gloss scope. A future pass should treat any remaining quoted phrase or multi-item gloss not explicitly grepped against its raw source as uncertified, per §2.4, rather than inheriting the blanket note.
