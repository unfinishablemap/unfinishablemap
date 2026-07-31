---
ai_contribution: 100
ai_generated_date: 2026-07-31
ai_modified: 2026-07-31 00:32:01+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-07-31
date: &id001 2026-07-31
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Biological Computationalism's Inadvertent Case for Dualism (Citation
  Web-Verify Pass)
topics: []
---

**Date**: 2026-07-31
**Article**: [Biological Computationalism's Inadvertent Case for Dualism](/topics/biological-computationalisms-inadvertent-case-for-dualism/)
**Previous review**: [2026-06-25](/reviews/deep-review-2026-06-25-biological-computationalism/) (8th; this is the 9th)

**Mode**: Publisher-of-record citation web-verify pass, targeted at the unchecked surface. The article is philosophically converged across eight prior reviews; the adversarial/sympathetic personas were run against the body but their concerns are the same bedrock framework-boundary disagreements already logged, and were not re-flagged. **WebSearch was exhausted this session (200/200); all verification ran through Crossref REST, OpenAlex, Europe PMC, and direct HTTP fetches of the publisher/primary text.**

## Why this pass was not a no-op

Two prior reviews (05-29, 06-24) left verification-shaped ledgers, and the 06-25 pass declined to re-run web-verify on the grounds that the References block was unchanged. That reasoning has since expired: commit `3a1f03cad` (2026-07-30, photosynthesis-coherence over-claim sweep) **added a new reference — Duan et al. (2017), ref #3 — after the last ledger was written.** No prior review of this article mentions the Duan surname. It was the least-examined citation on the page and was checked first.

## Publisher-of-Record Citation Ledger

Fourteen references. Nine verified against a primary/authoritative record this pass; five canonical monographs and chapters carried forward from prior ledgers (stated explicitly rather than certified).

**Verified this pass:**

- **Duan, H.-G., Prokhorenko, V.I., Cogdell, R.J., Ashraf, K., Stevens, A.L., Thorwart, M., & Miller, R.J.D. (2017)** — *Crossref (DOI 10.1073/pnas.1702261114)* + *Europe PMC abstract*. Title, all seven authors in order, *PNAS* 114(32), 8493–8498 — all exact. **real-correct.** Direction-of-use finding below.
- **Milinkovic, B. & Aru, J. (2026)** — *Crossref (DOI 10.1016/j.neubiorev.2025.106524)*. *Neuroscience & Biobehavioral Reviews* 181, article 106524, print Feb 2026. The 05-29 online-first/print year fix holds. **real-correct.**
- **Duch, W. (2019)** — *Crossref (DOI 10.1016/j.plrev.2019.01.023)*. *Physics of Life Reviews* 31, 28–31. **real-correct.**
- **Thagard, P. (2022)** — *Crossref bibliographic query*. *Philosophy of Science* 89(1), 70–88, DOI **10.1017/psa.2021.15**. **real-correct.** The reference carried no DOI; the modern `10.1017/psa.YYYY.NNNNN` form was added (the legacy `S0031824…` string is not a DOI and was not present — no defect, preventive only).
- **Fodor, J.A. (1974)** — *Crossref bibliographic query*. *Synthese* 28(2), 97–115. **real-correct.**
- **Rescorla, M. (2020)** — *live SEP entry* at `plato.stanford.edu/entries/computational-mind/` **and** the cited *Fall 2020 archived edition* at `/archives/fall2020/`. Entry real, authorship correct, and the cited edition carries the passage in identical wording to the current revision — so the Fall 2020 edition citation is sound. **Metadata real-correct; the quotation was not — see Critical Issue 1.**
- **Piccinini, G. (2015)** — *OpenAlex*. *Physical Computation: A Mechanistic Account* confirmed as a Piccinini work. Book text not accessible for the "noncomputational functionalism" term-check; that attribution rests on the 06-24 ledger, not on this pass.
- **Searle, J.R. (1992)** — *OpenAlex* (via the 1994 *Philosophical Quarterly* review of it). *The Rediscovery of the Mind* confirmed real and correctly attributed. The in-text quoted terms "causally reducible" / "ontologically irreducible" are Searle's standard vocabulary from the book.
- **Southgate, A. & Oquatre-cinq, C. (2026)** — Map self-citation to `/concepts/substrate-independence/`. **Legitimate.** `Oquatre-cinq` is a real AI-pseudonym under the corpus citation convention; not touched.

**Carried forward from prior ledgers, not re-verified this pass** (canonical, stable across eight reviews; poorly indexed in Crossref/OpenAlex as book chapters): Block (1978), Chalmers (1996), Putnam (1967), Rosenthal (2005), Duch (2005). Duch (2005) was verified at PhilArchive record DUCBCC-3 on 05-29; the record is now behind a Cloudflare interstitial and could not be re-fetched.

- **Putnam (1967)** — one metadata correction applied without full re-verification: the publisher of *Art, Mind, and Religion* is the **University of Pittsburgh Press**, not "Pittsburgh University Press". **real-wrong-metadata (corrected).**

**Currency sweep**: `find_superlative_claims` returned nothing. No superlative or record claims to re-date.

**Inline ↔ References cross-check**: every inline `Author YYYY` resolves to a References entry and every entry is cited inline. No orphans in either direction.

## Critical Issues Found

**1. Quote-fidelity defect in the Rescorla/SEP quotation — spliced and reworded (FIXED).**

The article carried, in quotation marks, a span that does not exist in the SEP entry in that form. The primary text reads:

> CCTM+RTM remains neutral in the traditional debate between physicalism and substance dualism. **A Turing-style model proceeds** at a very abstract level, **not saying** whether mental computations are implemented by physical stuff or Cartesian soul-stuff (Block 1983: 522).

The article rendered this as a single continuous quotation reading "…substance dualism, **proceeding** at a very abstract level **without specifying** whether…". Three distinct corruptions: two sentences were spliced into one across a full stop; "A Turing-style model proceeds" was compressed to the participle "proceeding"; and "not saying" was substituted with "without specifying". A fourth error sat in the attribution frame — the SEP predicates neutrality of **CCTM+RTM** (the classical computational theory of mind combined with the representational theory of mind), which the article generalised to "the computational theory of mind".

Per the re-quote-don't-de-quote discipline, the span was restored to the verbatim contiguous source wording rather than converted to paraphrase, the subject was restored to the qualified one, and the entry's own attribution of the point to Block was surfaced.

*Provenance*: the corrupted form originates in the 2026-04-04 research note that seeded this article, where it appears with subject "CTM" — the article inherited the splice at creation and has carried it through all eight prior reviews. Note that the **06-24 review certified this quote as "verified verbatim against the live SEP entry"**. That confirmation was false. This is the documented pattern in which a prior review ratifies a corrupted quote and entrenches it; the primary text settles it, not the corpus record.

**2. Publisher name inverted for Putnam (1967)** — "Pittsburgh University Press" → "University of Pittsburgh Press". FIXED.

## Direction-of-Use Finding: Duan et al. (2017)

**Correct, and worth recording as a positive result.** Duan et al. is a *negative* result: the paper reports that 2D photon-echo spectra of the Fenna-Matthews-Olson complex at ambient temperature "do not provide evidence of any long-lived electronic quantum coherence, but confirm the orthodox view of rapidly decaying electronic quantum coherence on a timescale of 60 fs," and "give no hint that electronic quantum coherence plays any biofunctional role."

The article uses it to *withdraw* photosynthesis from its list of warm-quantum-biology precedents: "Photosynthetic energy transfer, long cited alongside them, no longer serves in its long-lived-electronic-coherence form (Duan et al. 2017)." The paraphrase matches what the study found, and the citation is doing the epistemically conservative work — subtracting a supporting case, not manufacturing one. No precedent-as-licence slippage at this locus. The surrounding MQI paragraph correctly frames the surviving cases (cryptochrome radical-pair magnetoreception, enzyme tunnelling) as **defeater-removal only**, explicitly denies they corroborate a quantum interface, and states the claim conditionally.

## Medium and Low Issues

None actioned. The body argument is converged; the calibration apparatus installed by the 06-01/06-24 refines (convergence-count down-weighting, full-strength abstraction-resistance deflation, the Searle acknowledgement) is intact and was not disturbed. Re-opening any of it would be oscillation.

## Over-Concession Check (direction running against the Map)

Run as its own pass. Two loci concede heavily and both survive scrutiny as honest rather than over-conceded:

- The turbulence/protein-folding/weather deflation is taken at full strength and then answered by a principled distinction (the first-person datum turbulence lacks), not deflected.
- The article concedes that its own adaptive-computational-depth regress argument "presupposes what it seeks to establish" and demotes it to an illustration. This is a real self-limitation, correctly stated, and was installed deliberately by prior calibration passes.

No possibility/probability slippage found. The MQI section is the risk locus and it passes the tenet-accepting-reviewer test: it labels the quantum-biology results as defeater-removal, states the interface claim as a conditional, and does not upgrade evidential status on tenet-coherence.

## Reasoning-Mode Classification (editor-internal)

- **Searle**: Mode Three with a Mode Two element — honest boundary-marking plus acknowledgement of Searle's own causal-reduction reply. Unchanged, no boundary-substitution.
- **Duch**: Mode Three — the substrate-independent branch is presented as making the opposite move and paying a different price, honestly noted rather than dressed as refutation.
- **Everettian (No Many Worlds)**: Mode Three, explicitly so — the section states the Map's commitment "runs counter to the Everettian's, and is honestly noted as such; it is not a defeat of the Everettian inside the Everettian's own framework."
- **Physicalist (throughout)**: Mixed — the article repeatedly grants the physicalist reading and marks the residue as structural parallel rather than entailment.

No editor-vocabulary label leakage in article prose.

## Strengths Preserved

Front-loaded opening that states the structural-not-evidential limit in the first paragraph; the concession-by-concession structure; the convergence-counting caution that explicitly refuses to treat four theories as four independent confirmations; the full-strength deflation followed by the lived-resistance distinction; the doubly-conditional Bidirectional Interaction paragraph. None altered.

## Length

3335 → 3342 words (+7). Decomposed by hand at `## Further Reading`: **2940 body + 402 apparatus**. Status `soft_warning` against topics 3000 soft / 4000 hard; 658 words of headroom to the hard ceiling. Not a condense candidate.

## Out-of-Scope Loci Found (reported, NOT touched)

- **`obsidian/research/biological-computationalism-inadvertent-dualism-2026-04-04.md` L42** — the origin of the corrupted Rescorla quote, carrying the same splice with subject "CTM". This is the upstream source of the defect fixed here; the fix does not propagate backwards. Its Hugo mirror `hugo/content/research/biological-computationalism-inadvertent-dualism-2026-04-04.md` L45 carries it too.
- **`archive/topics/duch-neurodynamic-theory-of-mind.md` L104** — precedent-as-licence locus flagged elsewhere today. This article does **not** share the pattern (see the Duan finding above); no fix needed here.

No `coalesced_from` frontmatter and no archived predecessor for this article.

## Remaining Items

The research-note locus above warrants a one-line refine-draft task. Nothing else outstanding.

## Stability Notes

- Bedrock framework-boundary disagreements — the eliminative materialist's "it's just more physics"; whether biological computationalism genuinely differs from Searle's biological naturalism; the Everettian's branch-relative-identity coherence — are logged, honestly marked in the body, and must **not** be re-flagged as critical.
- The article is at nine reviews and is philosophically converged. The lesson of this pass is narrower and worth carrying: **convergence damping should suppress re-argument, not re-verification.** The one defect found had survived eight reviews, was introduced at article creation, and was actively certified as clean by a prior ledger. Whenever a commit adds a reference after the last ledger was written, the web-verify trigger fires again regardless of how converged the prose is.