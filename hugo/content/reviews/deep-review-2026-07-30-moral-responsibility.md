---
ai_contribution: 100
ai_generated_date: 2026-07-30
ai_modified: 2026-07-30 13:33:37+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-07-30
date: &id001 2026-07-30
draft: false
human_modified: null
last_curated: null
lastmod: 2026-07-30 13:33:37+00:00
modified: *id001
related_articles: []
title: Deep Review - Moral Responsibility
topics: []
---

**Date**: 2026-07-30
**Article**: [Moral Responsibility](/concepts/moral-responsibility/)
**Previous review**: [2026-07-11](/reviews/deep-review-2026-07-11-moral-responsibility/)

## Scope — which lenses ran, and which deliberately did not

Tenth deep review. Selected on **unchecked-surface** grounds, not staleness: the metadata ledger is complete and recent (2026-07-11), so **metadata was deliberately NOT re-run**. Two lenses that had never run on this file were run instead:

1. **Quote-fidelity** — never run as a dedicated lens (the 07-11 ledger spot-checked the Kane span only).
2. **Citation-framing / claim-match** — last run 2026-06-01 (59 days).

Also run: empirical-claim fidelity on the three numeric claims, and inline↔References cross-check. Length checked and held.

### Correction to the brief's surface estimate

The brief scoped **14 quoted spans of ≥30 chars** as the quote-fidelity surface. Measured against the raw file, that count is real but **almost entirely artefactual**. Of the spans a naive quote-regex returns:

- **6** are frontmatter wikilink entries inside YAML double quotes (`topics:`/`concepts:`/`related_articles:`) — not quotations.
- **1** is the `description:` frontmatter field — the Map's own copy.
- **4** are the article's own **scare-quoted objection headers** in `## Objections and Responses` ("Agent causation is mysterious.", "We can't detect it empirically.", "Compatibilism is sufficient.", "Buddhist ethics shows responsibility without selfhood.") — the Map's voice, no author attributed.
- **2** are article **titles in the References block** (Frankish 2016, Frankfurt 1971).
- **1** is a regex artefact spanning L159's `"rejects"` … `"you"` scare quotes.
- **1** is L159's statement of the *weak version* of the MWI objection — the Map's own formulation, unattributed.

**The genuinely externally-attributed quotation surface of this article is ONE span.** That is the honest figure and future reviews should not re-inflate it.

## Pessimistic Analysis Summary

### Critical Issues Found — 1 (fixed)

**Frankfurt enrolled on the wrong side of the compatibilist taxonomy (L145).** The article read *"sophisticated **reasons-responsive** determinism (Frankfurt, Fischer-Ravizza, Wolf)"*. Frankfurt 1971 is a **hierarchical/mesh** theory, which the standard taxonomy explicitly *contrasts* with reasons-responsiveness. SEP's *Compatibilism* entry states the contrast directly: compatibilists appeal to "either a hierarchical or reasons-responsive view of what the will is, **as exemplified by Frankfurt and Fischer and Ravizza respectively**", and Frankfurt's theory "relies exclusively upon a mesh between different features of an agent's psychology."

This is an **attribution error** under §2.5 (framework attributed to the wrong author), not a philosophical disagreement — and it **contradicted the Map's own sibling article**, which says Fischer and Ravizza "add a *history* condition to their reasons-responsive account, **distinguishing their view from purely structural mesh theories**" and places the mesh theory as "neither a leeway condition nor a source condition, but a third thing that brackets both."

- **Fix**: `sophisticated reasons-responsive determinism` → `sophisticated compatibilism` (−1 word). The trailing capacity list was already correctly ordered — *identification with effective higher-order desires* (Frankfurt), *mechanism-level reasons-responsiveness* (Fischer-Ravizza), *normative competence* (Wolf) — so removing the over-covering umbrella makes "mechanism-level reasons-responsiveness" attach to Fischer-Ravizza alone, which is correct. No substantive claim changed.

### Medium Issues Found — 2 (both fixed)

**1. Kane quote verbatim but mis-scoped (L53).** The article read: *free agents must be "ultimate creators (or originators) and sustainers" **of their choices***. Kane's formulation attaches the requirement to **ends or purposes**, not to each choice: free will is "the power of agents to be the ultimate creators (or originators) and sustainers of **their own ends or purposes**." The distinction is load-bearing for Kane, because on his view **not all free acts need be undetermined** — only the will-setting **self-forming actions** (SFAs) that ground ultimate responsibility. Rendering the object as "their choices" quietly universalises a requirement Kane restricts.

- **Fix**: `of their choices` → `of their own ends or purposes` (+3 words). This is Kane's own object, so the sentence is now faithful in both the quoted span and its scope.

**2. Internal seam: unqualified "Compatibilism" at L45 vs "sophisticated compatibilism" at L145.** L45 attributed the **conditional analysis** ("could have done otherwise" = "would have, if different desires") to *"Compatibilism"* flatly, then said critics argue this "doesn't ground *desert*". L145 says sophisticated compatibilism *does* ground desert "in metaphysically substantive capacities". Left unqualified, the article contradicted itself about whether compatibilism grounds desert.

- **Fix**: `**Compatibilism**` → `**Classical compatibilism**` (+1 word). The conditional analysis is the classical (Hobbes/Hume/Ayer) view; naming it as such makes the L45/L145 pair a deliberate classical-vs-sophisticated contrast rather than a seam.

### Framing findings that came back CLEAN

- **Reimers 2009 vs McKemmish 2009 — no direction inversion** (the brief's specific question; see ledger below). Both are correctly deployed as *critics* of the Hameroff recalibration.
- **Dennett 1991 and Frankish 2016** — **References-only**; neither is named anywhere in the body. There is therefore no framing claim about either, and nothing enrolls them as conceding anything. The Further Reading gloss "[illusionism](/concepts/illusionism/) — The eliminativist challenge and why it fails to undermine desert" is the **Map's** claim in the Map's voice, not attributed to Frankish. CLEAN.
- **Pereboom 2001** — Further Reading frames him as arguing "we lack the free will for basic-desert responsibility on determinism **or** indeterminism". Correct: that is hard incompatibilism, and the "or indeterminism" half is the part usually dropped. CLEAN.
- **Strawson 1962** — framed as "dissolution of the problem: responsibility constituted by the reactive attitudes, and why the Map **declines the dissolution without refuting it**". Correct side, honest boundary-marking. CLEAN.
- **Frankfurt 1969 vs 1971** — the Further Reading block explicitly disambiguates ("the 1969 PAP paper, distinct from the 1971 higher-order-desire paper cited above"). The wrong-work hazard is already handled; the References entry is the 1971 paper and every use is of the 1971 paper. CLEAN.
- **O'Connor 2000, Chisholm 1964** — References-only agent-causal libertarians; no side-claim made about either. CLEAN.
- **Soon et al. 2008 — not overstated.** The article says prediction accuracy for *which* button "was only ~60%—barely above chance for a binary choice" and that the gap "between predicting *when* someone will act and predicting *what* they will choose remains substantial." This **under**-claims relative to the paper, which is the safe direction. No slide into deterministic prediction. CLEAN.

## Quote-Fidelity Ledger — all spans, with verdict and source checked

| # | L | Span | Verdict | Checked at |
|---|---|---|---|---|
| 1 | 53 | "ultimate creators (or originators) and sustainers" | **verbatim-exact; scope corrected** — exact substring of Kane's UR definition; object was mis-rendered as "their choices", fixed to "their own ends or purposes" | Kane 1996 *Significance of Free Will* UR definition, corroborated across independent non-Map sources (Wikipedia Robert Kane; *Reason Papers* 24 book review of the 1996 book; PhilArchive). **Map domains blocked from the search to avoid self-confirmation.** |
| 2 | 45 | "could have done otherwise" | **term of art, unattributed** — PAP shorthand, no author claim | n/a |
| 3 | 45 | "would have, if different desires." | **Map's own gloss** of the conditional analysis, unattributed; now correctly labelled *classical* | n/a |
| 4 | 53 | "irreducible causal power" | **Map's own term**, scare-quoted for the critic's objection | n/a |
| 5 | 93 | "agent causation" | **Map's own term**, scare-quoted | n/a |
| 6 | 141 | "Agent causation is mysterious." | **objection header, Map's voice** | n/a |
| 7 | 143 | "We can't detect it empirically." | **objection header, Map's voice** | n/a |
| 8 | 145 | "Compatibilism is sufficient." | **objection header, Map's voice** | n/a |
| 9 | 147 | "Buddhist ethics shows responsibility without selfhood." | **objection header, Map's voice** | n/a |
| 10 | 159 | "if MWI were confirmed there would be no collapse for consciousness to influence" | **Map's own statement of the weak version**, explicitly disowned in the next clause; unattributed | n/a |
| 11 | 159 | "rejects" / "you" | **scare quotes** (regex artefact, not a span) | n/a |
| 12 | 182 | "could have done otherwise" | **term of art** | n/a |
| 13 | 205 | "Illusionism as a Theory of Consciousness." | **title, correct** | *JCS* 23(11-12), 11-39 |
| 14 | 206 | "Freedom of the Will and the Concept of a Person." | **title, correct** | *J. Phil.* 68(1), 5-20 |
| 15 | 202 | "Human Freedom and the Self." | **title, correct** (<30 chars, included for completeness) | Lindley Lecture, Kansas 1964 |
| 16 | 214 | "Freedom and Resentment." | **title, correct** (<30 chars) | *Proc. Brit. Acad.* 48, 187-211 |

**No fabricated quote. No quote attributed to the wrong work. No aggregator ratification** — the one real quote was checked against sources quoting Kane's book directly, with `unfinishablemap.org`/`.com` excluded from the search to rule out self-contamination.

## Empirical-Claim Fidelity — the three numeric claims

- **Hagan/Hameroff/Tuszyński 2002 — "eight to nine orders of magnitude longer" (L137): CONFIRMED CORRECT.** Verified at the arXiv version of record (quant-ph/0005025): Tegmark's estimate is **10⁻¹³ s**; the paper's corrected-equation estimate is **10⁻⁵ to 10⁻⁴ s**. 10⁻¹³→10⁻⁵ is eight orders; 10⁻¹³→10⁻⁴ is nine. The corpus-wide 2026-07-29 sweep that changed this from "seven" to "eight to nine" was arithmetically right. (The paper's *further* metabolic-energy figure of 10⁻²–10⁻¹ s would be 11-12 orders; the article cites the corrected-equation figure, which is the standard citation. Correctly scoped — do not "fix" this upward.)
- **Soon et al. 2008 — "up to ten seconds": CONFIRMED.** Abstract of record: "the outcome of a decision can be encoded in brain activity of prefrontal and parietal cortex **up to 10 s** before it enters awareness." Citation tuple verified: *Nature Neuroscience* **11(5), 543-545**, DOI 10.1038/nn.2112, PMID 18408715 — matches the References entry exactly.
- **"~60%" accuracy: not in the abstract**; it is a body figure (frontopolar decoding). Consistently reported at ~60% in the secondary literature and the article's use of it is deflationary. Retained; no page-level figure asserted beyond what was seen.

## Reimers / McKemmish — the direction question, answered

The brief flagged the risk that two 2009 papers by the same five authors in different journals might be deployed in the wrong direction. **Verified at publisher-indexed records; there is no inversion.** The article (L137) frames *both* as contesting the Hameroff recalibration — "though that recalibration was itself contested (Reimers et al. 2009; McKemmish et al. 2009), leaving the dispute live rather than settled." Both are indeed **anti**-Orch-OR:

- **Reimers, J.R., McKemmish, L.K., McKenzie, R.H., Mark, A.E., & Hush, N.S. (2009)**, *PNAS* **106(11), 4219-24** — abstract concludes coherent Fröhlich condensates "are inaccessible in a biological environment. Hence the Penrose-Hameroff orchestrated objective-reduction model … **are untenable**." First author **Reimers** — matches the References entry.
- **McKemmish, L.K., Reimers, J.R., McKenzie, R.H., Mark, A.E., & Hush, N.S. (2009)**, *Phys. Rev. E* **80(2), 021912**, DOI 10.1103/PhysRevE.80.021912, PMID 19792156 — "the Orch OR model **is not a feasible explanation** of the origin of consciousness." First author **McKemmish**, author order verified — matches the References entry.

Both first-author orderings, both venues, both volumes/pages are correct, and the two papers are correctly kept distinct. **No action needed.** Future reviews should not re-litigate this.

## Currency Check

The brief noted the newest external source is 2016 and asked whether a status claim has moved. Checked:

- **"a minority position among free will theorists"** (L39, of agent causation) — still true; compatibilism remains the plurality position in the discipline and agent-causal libertarianism a minority even within libertarianism. No change.
- **"Subsequent studies have improved timing predictions but not content prediction for complex moral decisions"** (L153) — still accurate; content decoding for complex/moral choices remains poor. No change.
- `find_superlative_claims` — the article carries **no** superlative/"first"/"record" phrasing to re-scope. No currency defect.

## Optimistic Analysis Summary

### Strengths Preserved

- The **L145 compatibilist-symmetry concession** remains the corpus model of honest boundary-marking — "the libertarian framing's distinguishing work is tenet-coherence … not unique moral explanatory power", and compatibilists "occupy a different metaphysical scaffold for substantively similar moral implications, not a morally inferior position." The taxonomy fix *strengthens* this by making the concession's referent accurate.
- The **MWI passage** (L99, L159) survived its 2026-07-29 rewrite well: the global-exclusion framing openly labels the condition "a posit the Map adopts, asserted rather than derived from the desert case", and concedes the phenomenology "is reproduced inside each branch."
- **Patienthood/agency separation** (L83, rewritten 2026-07-29) is a genuine precision gain and calibrated — consciousness "is necessary for that standing without conferring it."
- The **Hardline Empiricist** finds nothing to upgrade. No possibility/probability slippage anywhere: no tenet is used to lift an empirical claim up the evidential-status scale.

### Enhancements Made

None beyond the three corrections. **No prose manufactured** — the article is 63 words under the concepts hard ceiling and was treated as substitutive throughout.

## Length

| | Before | After |
|---|---|---|
| Authored prose | 2886 | **2889** (+3) |
| Apparatus (Further Reading + References) | 548 | **548** (unchanged) |
| Total | 3434 | **3437** |

`soft_warning`, **63 words under the 3500 concepts hard threshold**. Net +3 (+3 Kane object, −1 taxonomy umbrella, +1 "Classical"). No human length decision needed; no argument cut.

## Remaining Items — one owed locus, deliberately NOT touched

**`obsidian/positions/agency-and-will.md:97`** carries the identical Frankfurt misattribution: *"sophisticated **reasons-responsive** compatibilism (Frankfurt, Fischer & Ravizza, Wolf)"*. It is live in `hugo/content/positions/agency-and-will.md:99` too.

Left untouched on scope grounds — positions-register entries are `/positions-evolve`'s contract, not deep-review's. The fix is a **two-word deletion** (`reasons-responsive ` → nothing), matching the correction applied here; no confidence band, status, or dependency changes.

**Family resolution — the canonical form already exists and is correct in three articles**, so this is an outlier-repair, not a corpus-wide decision:

- `obsidian/topics/moral-implications-of-genuine-agency.md:47` — "Frankfurt's hierarchical desires, Fischer and Ravizza's guidance control, Wolf's Reason View" ✓
- `obsidian/concepts/compatibilist-symmetry-challenge.md:42` — "typically Frankfurt's hierarchical desires…" ✓
- `obsidian/concepts/frankfurt-hierarchical-mesh-theory-of-the-will.md:76` — mesh vs reasons-responsive explicitly distinguished ✓

After the two fixes (this article, done; positions, owed) the corpus is internally consistent on the taxonomy.

## Stability Notes

Tenth review; converged. The three fixes this pass were all **attribution/framing**, caught only because the two never-run lenses were run instead of re-running the complete metadata ledger — the correct targeting call.

`ai_system` **retained** as `claude-opus-4-5-20251101` (original author cohort). Corrections only; no re-authoring, so no co-attribution.

Bedrock disagreements (unchanged — future reviews must NOT re-flag as critical):

1. **Eliminativist challenge** — bedrock with tenet #1.
2. **MWI and desert** — bedrock with tenet #4; the global-exclusion register is honestly labelled a posit.
3. **Compatibilist sufficiency** — boundary-marking with honest moral-parity residue is the correct move.

Future reviewers should **NOT** re-flag:

- **The quote surface is ONE span, not fourteen.** A quote-regex over the raw file returns ~16 spans of which 15 are frontmatter wikilinks, the Map's own scare-quoted objection headers, or References titles. Do not re-open these as "unverified quotes."
- **Reimers/McKemmish direction** — verified at publisher-indexed records this pass; both correctly deployed as critics, author orders correct, papers correctly kept distinct.
- **"eight to nine orders of magnitude"** — verified arithmetically correct against Hagan 2002 (10⁻¹³ → 10⁻⁵–10⁻⁴). Do not revise to "seven", and do not raise to eleven-twelve using the metabolic-energy figure.
- **Soon "~60%"** — deflationary and correct; the figure is a body figure, not an abstract figure.
- **Strawson 187-211** pagination (bound *Proceedings*, chosen deliberately 2026-07-11).
- **References-only entries** (Dennett, Frankish, Chisholm, O'Connor, Tallis, Whitehead) — scholarly bibliography convention, stable across ten reviews, not orphans.
- **L45 "Classical compatibilism"** — the qualifier is deliberate, pairing with L145's "sophisticated". Do not strip it back to bare "Compatibilism"; the seam returns if you do.