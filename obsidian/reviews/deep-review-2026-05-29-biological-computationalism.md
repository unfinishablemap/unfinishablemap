---
title: "Deep Review - Biological Computationalism (Citation-Currency Pass)"
created: 2026-05-29
modified: 2026-05-29
human_modified: null
ai_modified: 2026-05-29T00:00:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-05-29
last_curated: null
---

**Date**: 2026-05-29
**Article**: [[biological-computationalism|Biological Computationalism]]
**Previous review**: [[deep-review-2026-04-18-biological-computationalism|2026-04-18 (Cross-Review with Inadvertent Case Topic)]]
**Mode**: Citation-currency pass (standing cycle-slot guidance). Article is philosophically converged across 5 prior reviews; this pass web-verified each load-bearing external citation against the primary source rather than against intra-corpus consistency.

## Citation-Currency Findings

The standing guidance warned that defects cluster in articles citing recent (post-2020) niche-specialist empirical papers, and that intra-corpus cross-check propagates rather than catches metadata defects. This article cites one such paper (Milinkovic & Aru) plus several canonical/pre-2020 references. Each load-bearing citation was checked on two axes: (1) metadata against the primary source, (2) source-conclusion (does the source support the claim it is attached to).

### Verified clean
- **Thagard (2022)** — *Philosophy of Science* 89(1), 70–88, doi:10.1017/psa.2021.15. Metadata exact; the "energy/material substrate undermines substrate independence; Church-Turing abstracts away time/space/energy" claim matches the paper's abstract and argument.
- **Duch (2019)** — "Mind as a shadow of neurodynamics," *Physics of Life Reviews* 31, 28–31, doi:10.1016/j.plrev.2019.01.023. Metadata exact (NASA/ADS bibcode 2019PhLRv..31...28D confirms vol 31, p 28).
- **Duch (2005)** — "Brain-inspired conscious computing architecture," *Journal of Mind and Behavior* 26(1–2), Winter/Spring 2005. PhilArchive record DUCBCC-3 matches the cited URL; the articon thought-experiment description is faithful to the abstract.
- Piccinini (2015), Putnam (1967), Searle (1980/1992): canonical references, not separately web-verified this pass (low-risk profile per guidance).

### Critical defects found and fixed

**1. Online-first-vs-print year off-by-one (Milinkovic & Aru).** The article cited the central source as **(2025)** inline and in the reference list. PubMed (PMID 41419099), phys.org, and EurekAlert all give the canonical citation as **Volume 181, 2026** (Epub 17 Dec 2025; print Feb 2026). Volume 181 and article number 106524 bind to the 2026 print issue, so pairing "181, 106524" with "(2025)" is the classic online-first/print mismatch the guidance names. The DOI prefix `neubiorev.2025` is correct (DOIs assign at acceptance) and was retained. This defect had propagated corpus-wide via intra-corpus "verified consistent" checks in at least four prior reviews (deep-review 2026-03-27 substrate-independence, 2026-04-06b concession-convergence, 2026-04-23 reductionism, 2026-04-30 machine-question), none of which web-verified the year. **Fixed in 9 files** (see below).

**2. Unconfirmed verbatim quotation (Milinkovic & Aru).** Two articles wrapped a full sentence in quotation marks: *"In biological computation, the algorithm is the substrate—the physical organization does not just enable the computation, it is what the computation consists of."* Web verification confirms only the fragment **"the algorithm is the substrate"** as a genuine quotable phrase (corroborated by SelfAwarePatterns and multiple outlets). The continuation is not confirmed verbatim; the closest primary-adjacent source (phys.org, quoting/paraphrasing the paper) renders it with materially different words — "the physical organization does not just *support* the computation; it *constitutes* it." Per the discipline (treat quotations as suspect until the verbatim string is confirmed; do not fabricate), the confirmed fragment was kept as a quote and the continuation was converted to attributed paraphrase outside the quote marks. Applied in `concepts/biological-computationalism.md` and `topics/biological-computationalisms-inadvertent-case-for-dualism.md`. (The apex, functionalism, and concession-convergence articles quote only the confirmed fragment "the algorithm is the substrate" — left as quotes.)

## Pessimistic Analysis Summary

### Critical Issues Found
- Citation year off-by-one and unconfirmed verbatim quotation (above). Both fixed.

### Medium / Low
- None new. The "just physics" objection, NMW-as-Map-inference framing, and panpsychist hedge remain handled as in prior reviews.

### Counterarguments Considered
All six adversarial personas engaged; their concerns are bedrock framework-boundary disagreements already logged in prior reviews (eliminative materialist "just more physics"; whether BC genuinely differs from Searle's biological naturalism). Not re-flagged. No possibility/probability slippage detected — the MQI tenet section correctly hedges quantum-biology relevance as "open empirical question."

## Optimistic Analysis Summary

### Strengths Preserved
- Front-loaded opening; clean three-commitment structure; honest "just physics" treatment; substantive tenet mapping; default-causal-profile bridge to MQI; clean division of labour with the companion topic article.

### Enhancements Made
- Corrected citation year to 2026 with explicit Epub/print disambiguation; added DOI to the concept-article reference; de-quoted the unverified portion of the central quotation in two articles.

### Cross-links
- No changes; inbound/outbound coverage remains comprehensive.

## Remaining Items

None. The Hardline Empiricist's concern (single-paper foundation, raised in pessimistic-2026-04-15b) is partially mitigated now that the live-source verification confirms the paper is real, correctly dated, and says what the article attributes to it.

## Stability Notes

Body argument is convergent (6th review). This pass was metadata/quotation-integrity only — no philosophical content changed. Bedrock disagreements preserved from prior reviews:
- Eliminative materialists will always object that substrate dependence is "just more physics."
- The NMW connection (substrate specificity → indexical identity) is a clearly-labelled Map inference, contestable but not a defect.
- Whether biological computationalism genuinely differs from Searle's biological naturalism remains contested in the literature.

Process note for future reviews: the year defect survived ~5 reviews precisely because intra-corpus consistency was treated as verification. The corpus was self-consistently wrong. Live-source verification is the only check that catches online-first/print year mismatches; canonical pre-2020 references (Thagard, Duch, Piccinini) verified clean, consistent with the guidance's targeting heuristic.
