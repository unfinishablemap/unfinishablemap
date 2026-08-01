---
ai_contribution: 100
ai_generated_date: 2026-07-30
ai_modified: 2026-07-30 21:59:29+00:00
ai_system: claude-opus-5
author: null
concepts:
- '[[substance-property-dualism]]'
created: 2026-07-30
date: &id001 2026-07-30
draft: false
human_modified: null
last_curated: null
lastmod: 2026-07-30 21:59:29+00:00
modified: *id001
related_articles: []
title: Deep Review - Substance Dualism vs Property Dualism
topics: []
---

**Date**: 2026-07-30
**Article**: [Substance Dualism vs Property Dualism](/concepts/substance-property-dualism/)
**Previous review**: [2026-07-07](/reviews/deep-review-2026-07-07-substance-property-dualism/) (ninth pass; this is the tenth)

## Scope of This Pass

Targeted citation audit, run as a **domain test**. The session closed four misattribution families in the quantum-coherence cluster, all sharing one shape: *a real paper's name attached to a claim belonging to a different real paper*, invisible to metadata checking. This article was selected because it **imports three references from that cluster** (Tegmark 2000, Hagan et al. 2002, Luo et al. 2025) into a metaphysics context — the sharpest available test of whether the defect family is cluster-specific or corpus-wide.

Both axes were run **separately**: metadata (author/year/venue/volume/pages/DOI) and paraphrase fidelity (*does the article's use of the source point the same way the source does?*). A clean metadata sweep is no evidence of fidelity.

Verification used Crossref, OpenAlex, Semantic Scholar, arXiv (author preprints), plato.stanford.edu and author-hosted PDFs. **No verification was done by corpus grep** — with five families closed this session, a corpus search confirms whichever variant it happens to read.

## Domain Verdict: Cluster-Specific (with one qualification)

**The misattribution family did not cross the domain boundary.** All three imported quantum-cluster citations came back clean on the paraphrase axis:

- **Hagan et al. 2002** — the 10⁻⁵–10⁻⁴ s figure and the "eight to nine orders of magnitude" arithmetic are both correct against the primary abstract, and correctly anchored to Tegmark's 10⁻¹³ s microtubule figure.
- **Luo et al. 2025** — the article credits it with "computational support"; the paper is QM/MM and first-principles electronic structure. Exactly right. The microsecond-persistence claim is stated independently of Luo rather than enrolled onto it — the calibration hedge restored by the 2026-05-27 review is **holding**.
- **Tegmark 2000** — one defect, but of a *different and milder species* (below).

Critically, the specific cluster failure the session has been chasing — *experimentally measured* coherence times credited to papers that report no such measurement — **does not occur here**. The article says Hagan "challenged Tegmark's parameters, yielding estimates," which is honest about the recalculation's status and consistent with the corpus position at [entanglement-binding-hypothesis](/concepts/entanglement-binding-hypothesis/) that Hagan's recalculation remains untested in neural tissue.

**The qualification.** This article is not defect-free; it fails on a *different* channel. What surfaced here is (a) within-source scope drift — a real figure from the right paper attached to the wrong one of the two systems that paper modelled — and (b) reference-apparatus decay: a wrong reference-work title and two orphaned references. These are lower-severity and structurally distinct from misattribution.

So: **localise the misattribution family to the quantum-coherence cluster; do not generalise it.** But do not read that as "the rest of the corpus is clean" — this article carried three real apparatus/scoping defects through nine prior reviews. The corpus-wide channel is precision of citation *apparatus and scope*, not misattribution of claims.

**Second-order finding, and the important one.** The wrong SEP title (below) was listed as `real-correct` in prior review ledgers. A prior ledger **ratified** the error. This is the aggregator-ratification pattern operating on Map-internal reviews: a ledger entry is only as good as the check behind it, and "previously ledgered real-correct" must not be treated as verification.

## §2.4 Publisher-of-Record Web-Verify Ledger

Two axes reported separately. **A clean metadata verdict is not evidence of a clean paraphrase verdict.**

| # | Reference | Metadata | Paraphrase / framing | Source used |
|---|---|---|---|---|
| 1 | Chalmers 1996, *The Conscious Mind*, OUP | **real-correct** | **faithful** — "naturalistic dualism (Chalmers's early position)" and "Chalmersan psychophysical laws" both correct | OpenAlex (1996 Choice Reviews record) |
| 2 | Chalmers 2018, meta-problem, *JCS* 25(9-10), 6-61 | **real-correct** — venue line verified verbatim: "Journal of Consciousness Studies, 25, No. 9–10, 2018, pp. 6–61" | **was ORPHAN — now anchored.** New inline cite states only the definition, verified verbatim against p.1; no stance on illusionism attributed | consc.net author-hosted PDF (primary) |
| 3 | Descartes 1641, *Meditations* | **real-correct** (canonical primary text) | **faithful** — res cogitans/res extensa, pineal gland | canonical |
| 4 | Frankish 2016, illusionism, *JCS* 23(11-12), 11-39 | **not re-verified this pass** — ingentaconnect 403; canonical form, ledgered real-correct 2026-05-27 | **faithful** — cited for illusionism, which is what the paper is. Driver pre-tested; not re-opened | — (unverified metadata) |
| 5 | Hagan, Hameroff & Tuszyński 2002, *Phys Rev E* 65(6), 061901 | **real-correct** — DOI 10.1103/physreve.65.061901; authors, title, venue, vol/issue confirmed | **faithful** — "10⁻⁵–10⁻⁴ s" verbatim from abstract; "eight to nine orders" arithmetic correct off 10⁻¹³ | Crossref + arXiv quant-ph/0005025 abstract |
| 6 | Lowe 2006, *Erkenntnis* 65(1), 5-23 | **real-correct** — DOI 10.1007/s10670-006-9012-3; all fields confirmed twice | **faithful** — grouped under a Map-coined heading ("naturalistic substance dualism"), not attributed to Lowe as his own label | Crossref + Semantic Scholar |
| 7 | Luo et al. 2025, *JACS* 147, 43934-43945 | **real-correct** — DOI 10.1021/jacs.5c15726; five-author list, vol 147 iss 47, pages all confirmed | **faithful** — study is QM/MM computational; "computational support" is exact. Microsecond claim correctly *not* enrolled onto Luo | Crossref + PMC12673606 (full text) |
| 8 | Pautz 2015, chapter in Alter & Nagasawa (Eds.), OUP | **partially confirmed** — chapter, title, author, year confirmed. **Venue UNCONFIRMED** | **UNCONFIRMED** — verbatim quote could not be checked | OpenAlex; PhilPapers/MUSE/Google Books all blocked |
| 9 | Robinson 2020, SEP | **real-wrong-metadata → FIXED.** Title was "Substance dualism"; the entry is **"Dualism"** (citation_title metadata). No separate SEP entry by that name exists | **was ORPHAN — now anchored.** Cited as a survey of the taxonomy, which is what it is | plato.stanford.edu live entry + archive |
| 10 | Tegmark 2000, *Phys Rev E* 61(4), 4194-4206 | **real-correct** — DOI 10.1103/physreve.61.4194; all fields confirmed | **real-wrong-scope → FIXED** (see below) | Crossref + arXiv quant-ph/9907009 abstract |
| 11 | Whitehead 1929, *Process and Reality*, Macmillan | **real-correct** | **faithful** — "actual occasions" is Whitehead's term | OpenAlex (Nature 1930 review; Gifford Lectures 1927-28) |
| 12 | Zimmerman 2010, *Aristotelian Society Supp. Vol.* 84(1), 119-150 | **real-correct** — DOI 10.1111/j.1467-8349.2010.00189.x; confirmed twice | **faithful on the main enrollment** — he does argue from property dualism to substance dualism. **Spatial-location sub-claim unconfirmed** (see Remaining Items) | Crossref + Semantic Scholar + OUP abstract |

**Inline ↔ References cross-check**: after this pass, all 12 references have body anchors and every inline cite has a References entry. Two orphans existed before this pass (see below).

## Critical Issues Found

1. **Tegmark scope conflation (paraphrase defect, fixed).** The article read *"Tegmark (2000) calculated decoherence times for neural microtubules at 10⁻¹³ to 10⁻²⁰ seconds."* Tegmark's range spans **two different systems**: 10⁻¹³ s is the microtubule figure, 10⁻²⁰ s the neuron-firing figure. Tegmark's abstract gives the range "both for regular neuron firing and for kink-like polarization excitations in microtubules"; Hagan's abstract independently confirms the split ("Tegmark finds that microtubules can maintain quantum coherence for only 10⁻¹³ s"). Attaching the whole range to microtubules also left the article's own "eight to nine orders of magnitude" arithmetic — which only works off 10⁻¹³ — silently unanchored. **Fixed**, and the fix makes the article internally coherent.

2. **Wrong reference-work title (metadata defect, fixed).** SEP entry is "Dualism", not "Substance dualism". Year 2020 **retained** and is correct: 2020 archived editions exist (spr/fall/win 2020 all resolve), and in 2020 the entry was sole-authored by Robinson. Bumping to the current 2025 revision would have required adding co-author Ralph Weir — so the minimal fix is also the one that keeps authorship right.

3. **Two orphaned references (fixed).** Robinson 2020 and Chalmers 2018 had no body anchor. The driver's surname-only test caught Robinson but masked Chalmers 2018 — "Chalmers" appears twice in the body, but both occurrences refer to the 1996 position; "meta-problem" appeared zero times. Both are apt sources, so both were anchored rather than removed.

## Changes Applied

| Location | Before | After |
|---|---|---|
| Decoherence / The Objection | "decoherence times for neural microtubules at 10⁻¹³ to 10⁻²⁰ seconds" | "decoherence times of 10⁻¹³ seconds for microtubule excitations and 10⁻²⁰ seconds for neuron firing" |
| References | "Robinson, H. (2020). Substance dualism." | "Robinson, H. (2020). Dualism." |
| Comparing the Views | (no lead-in) | + "Robinson (2020) surveys the standard taxonomy; what follows picks out the differences that bear on the Map's tenets." |
| The Illusionist Challenge | (para ended at "systematically misleading.") | + "The challenge is sharpened by what Chalmers (2018) calls the meta-problem of consciousness—the problem of explaining why we think there is a problem of consciousness at all." |

## Length

`analyze_length` reports 2787w / `soft_warning`, but the tool returns **one total with no heading decomposition**. Split by hand at `## Further Reading`: **prose 2453w, apparatus 334w.** Prose alone is **below** the 2500 concepts soft threshold — the warning is entirely reference apparatus. This is the standard false-over-length pattern; **no condense performed or warranted.** (Before this pass: 2739w total, 2404w prose.)

## Strengths Preserved

- The Luo calibration hedge from 2026-05-27 (computational-vs-experimental separation) is intact and correct — it is the single best-calibrated citation in the article and was left untouched.
- The "Where the Substance-Leaning Becomes Load-Bearing" section's diagnostic (agency-cluster claims need the substance reading; irreducibility claims do not) remains the article's most valuable original contribution.
- Honest framing of the substance lean as "a philosophical preference, not a doctrinal requirement."

## Remaining Items

1. **Pautz 2015 — venue and verbatim quote UNCONFIRMED.** The quote *"Though called a physicalist view, it seems to have many of the vices of dualism"* is grep-contiguous in the raw file (`grep -c` = 1) and is the article's only substantive external quote. The chapter's existence, title, author and year are confirmed via OpenAlex. **Its presence in the Alter & Nagasawa volume could not be confirmed**: Crossref has *zero* chapter-level deposits for that volume, so its silence is not evidence of absence; PhilPapers (403/JS-wall), Project MUSE (403) and Google Books (empty) all blocked automated access. **Nothing was acted on** — per discipline, a failed search is not grounds to call a reference wrong. This is the highest-value open item and needs a session with WebSearch budget or manual access.
2. **Zimmerman spatial-location sub-claim unconfirmed.** The article enrolls Zimmerman (with Hasker) under "locating minds spatially in the brain where they interact" as a pairing-problem response. His main enrollment is verified; the OUP abstract does not address spatial location, and full text was inaccessible. Hasker's half is uncontroversial. Low risk, but unverified.
3. **Bailey, Rasmussen & Van Horn** are cited in-body without a year and are absent from References — outside the formal reference audit. Their sorting under "invoking haecceities" (rather than under option 3, denying causation requires spatial relations) was not verifiable; OpenAlex could not locate the paper. No action taken.
4. **Frankish 2016 metadata** not re-verified at publisher this pass (403). Scoping was pre-tested clean and correctly cites him for illusionism.

## Stability Notes

- The article is at its **tenth** review and body argumentation has been stable since the fifth. Do **not** re-open: the substance-vs-property lean, the illusionism regress response, or the decoherence framing. These are converged.
- **Bedrock disagreements, not defects**: illusionists will reject the regress argument; physicalists will reject the irreducibility premise; MWI defenders will reject the indexical-identity argument under No Many Worlds. All sit at the framework boundary and must not be re-flagged as critical.
- **No possibility/probability slippage found.** The decoherence section is well calibrated: Hagan is presented as a contested recalculation, not a measurement, and the cryptochrome analogy carries its own explicit limiter ("cryptochrome's specific architecture does not by itself license neural-scale coherence"). A tenet-accepting reviewer would not flag these as overstated.
- **What this pass shows about review method**: nine prior reviews, four carrying verification sections, all missed a wrong reference-work title and two orphaned references — and at least one prior ledger positively affirmed the wrong title as `real-correct`. Metadata ledgers must record *which source was consulted*, or they become ratification machinery. This review's ledger names a source for every row.