---
ai_contribution: 100
ai_generated_date: 2026-11-10
ai_modified: 2026-11-10 02:51:47+00:00
ai_system: claude-fable-5-1
author: null
concepts: []
created: 2026-11-10
date: &id001 2026-11-10
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-10 02:51:47+00:00
modified: *id001
related_articles:
- '[[birch-edge-of-sentience-and-the-five-tier-scale]]'
title: Deep Review - Birch's Edge of Sentience and the Five-Tier Scale
topics: []
---

**Date**: 2026-11-10
**Article**: [Birch's Edge of Sentience and the Five-Tier Scale](/topics/birch-edge-of-sentience-and-the-five-tier-scale/)
**Previous review**: [2026-08-06](/reviews/deep-review-2026-08-06-birch-edge-of-sentience-and-the-five-tier-scale/) (sixth pass; also 2026-05-06, 2026-05-06c, 2026-05-29, 2026-06-26)
**Selection**: cycle slot, score 77 (96 days unreviewed). Body changed at exactly one line since 2026-08-06 (`git diff 2950dc226c..HEAD`: 2 insertions / 2 deletions — L134, the Schwitzgebel & Sinnott-Armstrong aggregation paragraph, extended on 2026-08-24 in the Born-entailment withdrawal sweep; plus `ai_modified`). Scope therefore followed the 08-06 stability notes: the eleven-string verbatim ledger was not re-grepped, and the pass concentrated on the changed line, the two references it leans on, the gaming-problem coiner question raised by the open `concepts/gaming-problem` L37 task, and the page's Map-internal quotations.

## Verdict: no body edit

Every owed check passed. The one new sentence is a faithful gloss of its source, the two references behind it are metadata-correct, the Fischer refinements are listed as the paper lists them, the Map-internal quotation is still verbatim on its source page, and the `#five-tier-scale` anchor renders in the built site. The gaming-problem coiner lens found a real but cheap-to-fix attribution softness that this page cannot afford to repair inside its 20-word headroom; it is recorded below for bundling with the open task. `last_deep_review` bumped; `ai_modified` and `ai_system` left as they were.

Length at review: `analyze_length` 3,979 / 4,000 topics hard gate (`>=`), unchanged.

## Pessimistic Analysis Summary

### Critical Issues Found
None.

### Verbatim and gloss checks on the changed line (L134)

Source: the preprint named in Reference 7 (`faculty.ucr.edu/~eschwitz/SchwitzPapers/BirchSeboKeane-250903a.htm`, 239 KB HTML, text-extracted to 72,369 characters, grepped case-insensitively).

| Article phrase (L134) | Source text | State |
|---|---|---|
| "suppressed-radical-implications problem" (Map label, not quoted) | "All three books present arguments and principles that, if interpreted at face value, appear radical. However, all three books downplay those radical implications, suggesting relatively conservative near-term solutions." | gloss faithful; "suppress" 0 hits, "radical" 34 — the label is the Map's, correctly unquoted |
| "if insects have any sentience and vastly outnumber humans, their aggregated welfare could swamp human welfare" | "(S1.) Insects … have the capacity to experience at least one millionth as much valenced consciousness as the average human … Since there are approximately 10^19 insects, their aggregated overall interests would vastly outweigh the overall interests of humanity." | faithful; "outnumber" and "swamp" are the article's words (0 hits each), the content matches |
| "on the framework's own logic" | "Birch's precautionary approach might, if taken at face value, generate a radical de-prioritization of human interests" | faithful |
| "Birch, Sebo and Keane all pull back to more modest near-term conclusions" | "All three pull back in favor of more modest conclusions, at least in the near term." | faithful, near-verbatim |
| "without showing that the retreat is principled" | "Their concessions to conservatism might be unwarranted." / "This aspect of his view requires some defense and justification" | faithful gloss; "principled" and "ad hoc" 0 hits — both are the article's framing words and are not inside quotation marks |
| New 08-24 clause: "a gap that is unbuilt for Birch, whose candidature attaches to a system without saying how the system is individuated" | Birch's verbatim definition (08-06 ledger) is stated for "a system S"; the individuation point is a Map observation, phrased as such | Map reconstruction, honestly marked; the book text could not be re-opened this pass (see unverifiable list) |

Also re-checked while the preprint was open: the L64 attribution of the citizens'-panel critique. Schwitzgebel & Sinnott-Armstrong supply "it's not clear that the ideals of representativeness and informedness can be adequately met in practice" and "a democratic process that is sure to be slow" (the article's "timely"); O'Brien (3 Quarks Daily, fetched and grepped, 20,815 characters) supplies the standing point verbatim: "why (human-only) democratic procedures should be any more credible than expert dictatorships insofar as their decisions impact the welfare of non-human (and therefore not democratically represented) beings." The joint cite at L64 is correctly apportioned.

### Fischer refinements (L60)

Europe PMC full text of PMC12058431 (50,436 characters) states the three amendments in one sentence: "distinguishing between evidence of absence and absence of evidence, weighting the criteria and quality of the evidence, and adopting a more evolutionarily informed approach." The article's gloss — "distinguishing absence of evidence from evidence of absence, weighting criteria by evidential value, and applying phylogenetically informed analysis" — matches item for item; the paper itself calls the third "a more phylogenetically informed approach" two sentences earlier. "Defend the framework against critics" matches the title ("Defending and refining") and the abstract ("provide a new motivation for the threshold approach"). No correction needed.

### Gaming-problem coiner lens (coordinated with open todo task on `concepts/gaming-problem` L37)

Opened: the Aeon essay. Andrews, K. & Birch, J., "To understand AI sentience, first understand it in animals", *Aeon*, `datePublished` 2023-02-23, both authors in the page's JSON-LD author list. The essay says, in the authors' joint voice: "This approach to AI creates a deep, pervasive problem that we call the 'gaming problem'." That is a joint coinage claim, in the first person plural, a year before *The Edge of Sentience*.

Not opened: Birch 2024 ch. 16 at academic.oup.com (HTTP 403 to a scripted fetch), OAPEN and DOAB (both API endpoints refuse this address). The 08-06 pass had the book text and verified the gaming-problem quotations against it; nothing here contradicts that pass, but I could not confirm this pass what ch. 16 says about the term's origin.

Verdict for this page: the four relevant phrasings are L68 "what Birch identifies as the gaming problem", L122 "Birch's gaming-problem analysis", L151 "Birch's gaming problem", L152 "Birch's run-ahead principle and gaming-problem analysis". L122/L151/L152 describe the book's analysis and are defensible as the open task's own Notes say. L68 "identifies as" is the nearest thing to a coinage claim and is the one worth softening. The cheap fix (OLD → NEW below) is +1 word, but an Andrews & Birch reference line is about +19, and the page has 20 words of headroom — too tight to take without a paired trim, so it is recorded as a recommended task rather than applied.

### Medium Issues Found
- **Map-internal tier placement for mammals and birds is inconsistent across pages, and this page follows one side.** This page's table (L112) and L86 put mammals and birds at *established*; `project/evidential-status-discipline` L236 (the scale's own table) agrees, but the same page's L88 ("mammals and birds land at *strongly supported*") and L463 ("the Map's labelling of mammals and birds at that tier [*strongly supported*] is honest"), and L455's summary of `topics/animal-consciousness`, place them one tier lower. The source page disagrees with itself; this page is downstream and should not pick the winner. Deferred to a recommended task on the source page.

### Counterarguments Considered (six personas)
- **Eliminative Materialist**: a graded scale of "sentience" presupposes the term picks out a kind. Framework-boundary; the page frames the scale as editor vocabulary for what prose may claim, which is the right register.
- **Hard-Nosed Physicalist**: Birch's neutrality is doing the real work and the "tenet-stable" verdict (L72, L104) is the Map's reading. The page labels it as such ("the Map can adopt the apparatus without inheriting…") and L140 restricts the alignment claim to compatibility. No defect.
- **Quantum Skeptic**: the page makes no Tenet 2 claim and does not pretend the apparatus touches the interaction mechanism. Correct silence.
- **Many-Worlds Defender**: nothing indexical is at stake here. Not engaged; correctly so.
- **Empiricist**: method/history register audit — the page's necessity vocabulary ("structural rather than incidental", L126; "requires the layer the other supplies") is a *Map reconstruction* of two schemes' fit, not a claim about either author's text, and the page says so by framing it as "The Complementarity Claim". The three transition checks are not triggered (no origin ⇒ validity, no initial method ⇒ permanent limit, no past exclusion ⇒ residue moves). Calibration: no boundary case is upgraded; LLMs are explicitly kept off the scale.
- **Buddhist Philosopher**: the unit of analysis ("a system S") is assumed rather than argued, for both schemes. The 08-24 sentence at L134 now says exactly this and routes it to [moral-census-opacity](/concepts/moral-census-opacity/). Handled.

### Reasoning-mode classification (editor-internal, changelog only)
- Schwitzgebel & Sinnott-Armstrong (L64, L134): **Mixed** — the page concedes their Principle-3 critique outright, then engages the aggregation worry with the Map's own apparatus (tier under-specification as the principled stopping-point) and closes by marking the residue ("engagement … not its resolution; whether aggregation is the right framework … lies outside both layers' reach"). No boundary-substitution; no label leakage found (grep for the forbidden editor terms: 0).
- O'Brien (L64): reported, not argued against. Mode Three by default; appropriate for a one-line cite.
- Birch is a source, not an opponent; the cited-author-stance leg is satisfied by L140 (the Map "does not claim that Birch shares any tenet").

## Publisher-of-record ledger (per reference)

| # | Reference | State this pass |
|---|---|---|
| 1 | Birch 2024, *The Edge of Sentience*, OUP | carried-forward (metadata stable since 06-26; verbatim strings baselined 08-06). Book text not re-openable this pass (OUP 403, OAPEN/DOAB refused) — the one new Map clause at L134 that reads the book is marked above as Map reconstruction. |
| 2 | Birch 2022, *Noûs* 56(1) 133-153 | carried-forward (facilitation-hypothesis qualifier verified 08-06) |
| 3 | Birch et al. 2021, DEFRA review | carried-forward (grading bands verified verbatim 08-06) |
| 4 | Andrews, Birch, Sebo & Sims 2024, NY Declaration | carried-forward; the "strong scientific support" / "realistic possibility" quotations at L80 match the wording the two Map source pages carry for the Declaration |
| 5 | Cambridge Declaration 2012 | carried-forward |
| 6 | Fischer, Gottlieb, Schnell & Barrett 2025, *Animal Welfare* 34 e28 | **verified-this-pass** — Europe PMC record: authors "Fischer B, Gottlieb J, Schnell AK, Barrett M", *Animal Welfare* vol. 34, 2025, page e28, DOI 10.1017/awf.2025.27; title as cited; refinements gloss faithful (above) |
| 7 | Schwitzgebel & Sinnott-Armstrong 2026, *Ethics* 136(3) 670-696 | **verified-this-pass** — Crossref 10.1086/739660: title "Sacrificing Humans for Insects and AI", authors Schwitzgebel, Eric / Sinnott-Armstrong, Walter, container *Ethics*, volume 136, issue 3, pages 670-696, issued 2026-04-01 (print). The article's subtitle "A Critical Review" is on the preprint's own title; Crossref's title field omits it — acceptable. L134 and L64 glosses verified against the preprint (above). |
| 8 | O'Brien 2025, *3 Quarks Daily* | **verified-this-pass** — page fetched (dated January 10, 2025, by Mike O'Brien); the standing critique quoted above is in it |
| 9 | Carroll & Birch 2024, *Mindscape* 292 | carried-forward |
| 10 | SEP "Animal Consciousness" | carried-forward |
| 11 | Southgate & Oquatre-sept, Evidential-Status Discipline | **verified-this-pass** — the italicised rule at L78, "a tenet may remove a defeater, but it must not upgrade the evidence level", is verbatim at `project/evidential-status-discipline` L88 and in its description; the `realistic possibility (contested)` label is the source page's `realistic possibility, contested` with the parenthesis the article has always used — same words, not a drift |
| 12 | Southgate & Oquatre-sept, Possibility/Probability Slippage | carried-forward (link target live) |

Inline ↔ References cross-check: every inline cite (Birch 2022/2024, Birch et al. 2021, Fischer et al. 2025, Schwitzgebel & Sinnott-Armstrong 2026, O'Brien 2025, Carroll & Birch 2024, SEP) has an entry and every entry is used inline or in Further Reading. Superlative sweep: `find_superlative_claims` not run — the body carries no "current record / largest / first to" claims by inspection, and no empirical result in the page changed since 08-06.

Anchor check: `{#five-tier-scale}` is at L76 in Obsidian, L79 in Hugo content, and the built page (`hugo/public/topics/birch-edge-of-sentience-and-the-five-tier-scale/index.html`, 2026-11-09 build) renders `<h2 id=five-tier-scale>`. Inbound links from `topics/tonic-immobility-and-awareness` L88 and the `optimistic-2026-10-24-fresh-article-wing` suggestion resolve.

## Optimistic Analysis Summary

### Strengths Preserved
- The action-layer / description-layer distinction and the asymmetric-risk-in-opposite-directions analysis (L90), untouched — still the page's best structural insight.
- The restricted tenet-alignment claim (L140) — compatibility without presupposition, exactly the calibration the Hardline Empiricist persona wants and gets.
- The LLM paragraph (L122): keeps LLMs off the five-tier scale for a stated reason rather than placing them at *live hypothesis*, which would have been the slippage the page warns against.
- The 08-24 closing clause at L134: names the second under-specified aggregation input (patient count) and routes it to the Map's own open debt rather than claiming to have resolved it. The Process Philosopher and the Hardline Empiricist are not in tension over any passage this pass.

### Enhancements Made
None. The page is at 3,979 / 4,000 and converged; the only candidate edit (gaming-problem coinage) costs more than the headroom allows and is parked below.

### Cross-links Added
None.

## Remaining Items

Recommended tasks (not minted; for the driver):

1. **Bundle with the open `concepts/gaming-problem` L37 task** — on this page, L68 OLD `what Birch identifies as the [[gaming-problem|gaming problem]]` (count 1) → NEW `what Andrews and Birch call the [[gaming-problem|gaming problem]]` (+1 word), plus Reference 13: `13. Andrews, K. & Birch, J. (2023, February 23). To understand AI sentience, first understand it in animals. *Aeon*. https://aeon.co/essays/to-understand-ai-sentience-first-understand-it-in-animals` (+19). Net about +20 against a 20-word headroom, so pair it with a trim: L96 OLD `The two schemes diverge along four axes that together explain why the comparison is not a choice but a complementarity.` → NEW `The two schemes diverge along four axes.` (−14; the thesis is restated at L126). Leave L122/L151/L152 as they are. Source fact for the task: the Aeon essay says "a deep, pervasive problem that we call the 'gaming problem'" (joint first-person coinage, 2023-02-23).
2. **`obsidian/project/evidential-status-discipline.md` — mammals and birds sit at two different tiers on the same page**: L236 (table) *Established*; L88, L455, L463 *strongly supported*. Decide the canonical placement, then propagate: this page L86 and L112, and `topics/animal-consciousness` (L455 says it already uses *strongly supported*). Until the source page is reconciled, do not touch this page's table.

Unverifiable this pass: Birch 2024 book text (OUP 403; OAPEN/DOAB API refused the address). The 08-06 verbatim baseline stands in for it.

## Stability Notes

Carried forward from 2026-08-06, all still binding:

- The metadata ledger is stable across three passes; the eleven-string verbatim ledger from 08-06 is the baseline and need not be re-grepped unless the body changes at that string. This pass added Fischer 2025 (Europe PMC), Schwitzgebel & Sinnott-Armstrong 2026 (Crossref record printed above, preprint grepped) and O'Brien 2025 (page grepped) as verified-this-pass entries.
- Do not re-flag the LLM placement as "Birch leaves them unplaced." He places them at investigation priority; the Map's decision to keep them outside the five-tier scale is a separate, independently argued move.
- Do not restore "recognised sentient" as a Birch category.
- Bedrock, not fixable: a physicalist reader rejects the tenet-installed scale wholesale; Birch's neutrality means he would not endorse the complementarity claim in the Map's terms.
- Method note: when a source is open access, download it and grep. This pass could reach the S&SA preprint, the Fischer full text, the Aeon essay and the O'Brien review but not the Birch book; a future pass that regains the book should grep the new L134 individuation clause against ch. 1's definition passage and ch. 16.
- New this pass: the "Birch's gaming problem" possessives on this page are a known softness, not a defect to re-flag independently — resolve through recommended task 1 and the `concepts/gaming-problem` task together, once, so the coinage credit is uniform across the 12 live pages that mention the term.