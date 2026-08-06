---
ai_contribution: 100
ai_generated_date: 2026-08-06
ai_modified: 2026-08-06 02:34:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-06
date: &id001 2026-08-06
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-06 02:34:00+00:00
modified: *id001
related_articles:
- '[[birch-edge-of-sentience-and-the-five-tier-scale]]'
title: Deep Review - Birch's Edge of Sentience and the Five-Tier Scale
topics: []
---

**Date**: 2026-08-06
**Article**: [Birch's Edge of Sentience and the Five-Tier Scale](/topics/birch-edge-of-sentience-and-the-five-tier-scale/)
**Previous review**: [2026-06-26](/reviews/deep-review-2026-06-26-birch-edge-of-sentience-and-the-five-tier-scale/) (fifth pass; also 2026-05-06, 2026-05-06c, 2026-05-29)
**Selection**: score 37 (41 days unreviewed). Body unchanged since 2026-06-26 — the only intervening commit was a `topics:` frontmatter fill. On the prior review's own expectation this should have been a no-op.

## Verdict: NOT a no-op — four fabricated or mis-sourced direct quotes and one attribution error, all found by reading the primary text rather than re-checking metadata

The 2026-06-26 pass ran an 11-item publisher-of-record ledger on the *bibliographic metadata* and found 10/11 real-correct. That ledger was accurate and still holds. What it did not do — and what no prior pass did — was grep the article's **quoted strings** against the full text of the sources. Birch 2024 is open access; the 2021 LSE/DEFRA report is a public PDF. Both were downloaded, text-extracted, whitespace- and soft-hyphen-normalised, and grepped. Three of five direct quotes attributed to Birch do not occur in either source.

This is the `quote-fidelity-defects-survive-metadata-reviews` pattern at full strength: five reviews of a citation-dense article, all clean on metadata, none on verbatim.

## Critical issues found and fixed

### 1. Fabricated definition of *sentience candidate* (quote-fidelity)
The article attributed to Birch, in quotation marks, "a credible, non-negligible possibility of sentience" as the defining condition. **The word *non-negligible* does not occur anywhere in the 1.1 MB book text** (2 hits for "negligible", both in an unrelated passage on proportionality). The phrase is a secondary-source gloss.

Replaced with Birch's actual definition, verified verbatim: a sentience candidate is a system *S* for which there is an evidence base that "(a) implies a realistic possibility of sentience in S that it would be irresponsible to ignore when making policy decisions that will affect S, and (b) is rich enough to allow the identification of welfare risks and the design and assessment of precautions."

The correction **strengthens** the article: its central convergence claim is that both schemes speak the language of "realistic possibility," and Birch's own definition turns out to use exactly that phrase.

### 2. Fabricated definition of *investigation priority* (quote-fidelity + dropped qualifier)
The article quoted "could plausibly be identified as sentient if more research was done" — 0 hits in the book; the phrasing traces to the Wikipedia entry, which the research note correctly attributes to Wikipedia and the article silently re-attributed to Birch.

Birch's actual clause: "yet: (a) further investigation could plausibly lead to the recognition of S as a sentience candidate; and (b) S is affected by human activity in ways that may call for precautions if S were a sentience candidate."

The article's gloss also dropped a qualifier: it said the second clause turns on the system "turning out to be sentient," where Birch says "if S were a **sentience candidate**." Fixed, with the qualifier made explicit.

### 3. Fabricated "operational five-of-eight rule" + substantive mischaracterisation (quote-fidelity + factual error)
The article quoted, as the framework's "operational rule": *"Precautionary measures are warranted for the members of a group of animals when we have high or very high confidence that they satisfy at least five of eight criteria."* **0 hits in the book. 0 hits in the 2021 LSE/DEFRA report.** No such sentence exists in either source.

Worse, it misdescribes the scheme. The report's actual text is an **evidence-grading band**, not an action trigger: "high or very high confidence that an animal satisfies 7 or more of the criteria amounts to very strong evidence of sentience. High or very high confidence that an animal satisfies 5 or more criteria amounts to strong evidence of sentience, and high or very high confidence that an animal satisfies 3 or more criteria amounts to substantial evidence of sentience." Plus: "no single criterion provides conclusive evidence of sentience by itself."

Section retitled from "The Eight Indicators and the Five-of-Eight Rule" to "The Eight Indicators and the Evidence-Grading Bands"; the body now quotes the report verbatim and separates the grading from the precaution judgement. (The eight criterion *names* checked out against the report and needed no change.)

### 4. Attribution error — Birch DOES place LLMs
The verdict table said current LLMs get only "run-ahead principle applies; gaming-problem caveat blocks formal candidacy," and the prose said the run-ahead principle "licenses regulatory action despite non-candidate status." Birch writes plainly: **"These problems notwithstanding, I do see LLMs as legitimate investigation priorities. In my view, research into their possible sentience is important and should be supported."** The article reported his framework as leaving LLMs unplaced when he places them at the lower of his two tiers.

Fixed in table and prose. The Map's own position (LLMs sit outside the five-tier scale, because the gaming problem breaks the marker-to-experience inference) is preserved and re-anchored — it never depended on Birch declining to place them.

### 5. Attribution error — "*recognised sentient*" is not a Birch category
The article said "Birch operates with three categories along a continuum. The first — *recognised sentient* —…", italicised alongside his two real terms. **0 hits for "recognised/recognized sentient" in the book.** Birch's scheme is genuinely two-tier plus a "neither" residue, and his candidate category reaches *upward* to absorb the settled cases: Proposal 15 makes all adult vertebrates sentience candidates. The invented tier had propagated into the top two rows of the verdict table.

Rewritten. This also sharpened a real analytical point the article had been missing: the Birch-candidate / Map-*realistic-possibility* alignment holds only on the contested middle and parts company above it.

### 6. Verdict table imprecision (factual)
Corrected against Proposals 15 and 18: decapods split (Pleocyemata candidates / Dendrobranchiata investigation priorities); insects split (adults candidates / larvae investigation priorities); *C. elegans* is a settled investigation priority which Birch expects might be reclassified **upward**, not the invented "borderline, below-IP placement defensible" hedge the table carried; Hydra and slime molds are absent from his lists entirely.

Also corrected: the article listed "brain organoids without brainstem tissue, and (on permissive readings) some plants" as typical investigation priorities. Neither appears on Birch's list. His organoid rule (Proposal 12, the brainstem rule) is a *sufficient condition for candidature*, and he mentions plants only to say sentient AI deserves more serious treatment than they do.

### 7. Framework Principle 3 misstated (dropped/added qualifier)
The article: "proportionality of precaution should be determined by democratic deliberation **rather than expert commission**." Birch: "Assessments of proportionality should be informed, democratic, and inclusive" — and he wants experts feeding calibrated uncertainty *into* citizens' panels, so the "rather than expert commission" contrast is the article's invention. Replaced with his verbatim principle. Framework Principles 1 and 2 also now quoted verbatim.

### 8. Citation currency — Schwitzgebel & Sinnott-Armstrong now published
Cited as a 2025 preprint ("Review essay on Birch, Sebo, and Keane" — a placeholder descriptor, not a title). Now published: **Schwitzgebel, E. & Sinnott-Armstrong, W. (2026). "Sacrificing Humans for Insects and AI: A Critical Review." *Ethics*, 136(3), 670-696. DOI 10.1086/739660** (volume/issue confirmed at journals.uchicago.edu; the author's own abstract page prints "36", a truncation). Reference entry and two inline years updated.

## Publisher-of-record ledger (this pass: verbatim, not metadata)

Method: `curl` the open-access sources, `pdftotext -layout`, normalise (collapse whitespace, strip U+00AD soft hyphens, rejoin `-\s` line-break hyphenation, fold to alphanumerics), then exact-substring count. The soft-hyphen step matters: the run-ahead quote returned 0 hits before normalisation and 1 after — the `tallis-misrepresentation-quote-propagation` trap, live.

| Quoted string | Source | State |
|---|---|---|
| "credible, non-negligible possibility of sentience" | Birch 2024 | **fabricated** — 0 hits; replaced with verbatim definition |
| "rich enough to allow the identification of welfare risks and the design and assessment of precautions" | Birch 2024 | real-correct (2 hits) |
| "could plausibly be identified as sentient if more research was done" | Birch 2024 | **fabricated** (Wikipedia paraphrase) — 0 hits; replaced |
| "Precautionary measures are warranted… at least five of eight criteria" | Birch 2024 / DEFRA 2021 | **fabricated** — 0 hits in *both*; replaced with the report's grading bands |
| "run ahead of what would be proportionate to the risks posed by current technology, considering also the risks posed by credible future trajectories" | Birch 2024, Proposal 25 | real-correct (1 hit after soft-hyphen normalisation) |
| "I do see LLMs as legitimate investigation priorities" | Birch 2024 | real-correct — newly added |
| Framework Principles 1-3 | Birch 2024 | real-correct — newly added verbatim |
| DEFRA grading bands (7+/5+/3+) | Birch et al. 2021 | real-correct — newly added verbatim |
| "recognised sentient" as a Birch category | Birch 2024 | **not a Birch term** — 0 hits; removed |
| Birch's facilitation hypothesis | Birch 2022 *Noûs* | real-correct; the "*cluster* of cognitive abilities" qualifier was missing and has been restored |
| Schwitzgebel & Sinnott-Armstrong | *Ethics* 136(3) 2026 | real-wrong-metadata — year, title, venue, pages, DOI corrected |

Bibliographic metadata otherwise re-confirmed as per the 2026-06-26 ledger; no new metadata defects.

## Corpus sweep (per `fix-by-file-leaves-string-siblings-live`)

The fabricated strings were not confined to the article. Grepping all three trees found the origin and two downstream carriers:

- `obsidian/research/birch-edge-of-sentience-precautionary-framework-2026-05-05.md` — **the origin**. It labelled both fabricated strings "**Quote**". Its own Wikipedia section (line 61) carried the *correct* five-of-eight gloss all along ("counts as 'strong evidence of sentience'"), so the article's "operational rule" was a confection layered on top of accurate notes. Both entries corrected in place with dated correction notes; the "Operational Five-of-Eight Indicator Rule" section retitled; the Map/Birch tier-mapping table fixed (it was the source of the "Recognised sentient" invention).
- `obsidian/research/sentientism-2026-08-01.md` — carried the fabricated definition as a "**Verified quote it carries**". Corrected.
- `obsidian/research/voids-threshold-void-2026-02-20.md` — carried the fabricated definition in prose. Corrected.

Prior review files and archived changelogs also contain the strings; left untouched as historical records of what was believed at the time.

## Length

3698 → 3916 body words (`analyze_length`: 3906, `soft_warning`, under the 4000 topics hard ceiling). Verbatim source definitions run longer than the paraphrases they replaced, so the pass ran length-neutral discipline in reverse: +500 from corrections, −282 from compressing the aggregation paragraph, the duplicated critique of Framework Principle 3 (stated twice in near-identical words), the self-referential closer on the possibility bullet, and the two Relation-to-Site-Perspective paragraphs. Net +218 for a substantially more accurate article.

## Strengths preserved

The layer distinction (action-oriented vs description-oriented) remains the article's best structural insight and was not touched. The asymmetric-risk-in-opposite-directions analysis, the aggregation-problem engagement, and the restricted tenet-alignment claim ("compatible with Tenets 1, 3 and 5 without presupposing any of them") all survive intact — the last is exactly the calibration honesty the deep-review discipline asks for, and it was already right.

## Stability notes

- The metadata ledger is now stable across two independent passes. **The verbatim ledger is new and should be treated as the baseline** — future passes need not re-grep these eleven strings unless the body changes.
- Do not re-flag the LLM placement as "Birch leaves them unplaced." He places them at investigation priority; the Map's decision to keep them outside the five-tier scale is a separate, independently argued move.
- Do not restore "recognised sentient" as a Birch category. It is not his term, and his candidate category demonstrably includes mammals and birds.
- Bedrock, not fixable: a physicalist reader will reject the Map's tenet-installed scale wholesale, and Birch's studied neutrality means he would not endorse the complementarity claim in the Map's terms. Both are framework-boundary disagreements, correctly not treated as defects.
- **Method note for future citation-dense reviews**: when a source is open access, download it and grep. Five passes of publisher-of-record *metadata* checking ratified four fabricated quotes. Metadata verification and verbatim verification are orthogonal channels, and the second is where the defects were.