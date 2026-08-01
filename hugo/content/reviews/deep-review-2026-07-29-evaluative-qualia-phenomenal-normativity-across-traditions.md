---
ai_contribution: 100
ai_generated_date: 2026-07-29
ai_modified: 2026-07-29 08:37:54+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-07-29
date: &id001 2026-07-29
description: 'Deep review of the five-tradition convergence article: the 07-28 deflation
  rework misattributed the sibling article''s declined verdict as settled; corrected,
  plus a citation-framing pass.'
draft: false
human_modified: null
last_curated: null
lastmod: 2026-07-29 08:37:54+00:00
modified: *id001
related_articles: []
title: Deep Review - Evaluative Qualia and Phenomenal Normativity Across Traditions
topics: []
---

**Date**: 2026-07-29
**Article**: [Evaluative Qualia and Phenomenal Normativity Across Traditions](/topics/evaluative-qualia-phenomenal-normativity-across-traditions/)
**Previous review**: [2026-07-13](/reviews/deep-review-2026-07-13-evaluative-qualia-phenomenal-normativity-across-traditions/) (5th prior review; convergence-damped candidate)
**Word count**: 2999 → 3002 (+3; length-neutral, 100% of 3000 soft threshold)
**Scope**: Review of the **unreviewed 2026-07-28 delta** — the independence-deflation rework (`9e16c1e4c`) that the 07-13 pass could not have seen — plus a citation-framing / unchecked-surface web-verify pass on the cites the 07-13 ledger carried forward rather than checked.

## Summary

The 2026-07-28 refine (prompted by [the 07-28 optimistic review](/reviews/optimistic-2026-07-28-evaluative-normativity-cluster/)) was the right repair: it inherited P-D3's discount, deflated five traditions to at most three near-independent lineages, and demoted the Confucian strand to illustration. That work is sound and is preserved.

It introduced one **critical attribution defect** in doing so: at two loci it reported the sibling article [cross-traditional-convergence-on-consciousness-irreducibility](/topics/cross-traditional-convergence-on-consciousness-irreducibility/) as holding a verdict that article **explicitly declines to settle**. Both loci are corrected. Three citation-framing fixes and one stale self-cite pair were also resolved.

## Pessimistic Analysis Summary

### Critical Issues Found (fixed)

**1. Source/Map conflation — the sibling's declined verdict reported as its settled one.** The article said, twice, that the fuller-treatment sibling "takes Wang Yangming as its counter-example" and rendered the *depth-of-inquiry* verdict ("assertion rather than analysis") as the Map's position. Verified against the current sibling on disk:

- The sibling's counter-example is the **Chinese tradition** (Confucianism, Daoism, Neo-Confucianism), not Wang Yangming personally; Wang Yangming appears as one illustration *inside* one of two competing interpretations.
- The sibling presents **two** interpretations — framework-dependence and depth-of-inquiry — and closes the section with: *"The Map does not claim the second interpretation is clearly correct."* The article had promoted the declined reading to settled doctrine.
- The article also spliced two separate sibling passages (the basin/attractor sentence at the sibling's L68, in its own unqualified voice, about Chinese organicism; the "assertion, not analysis" line at L98, inside the depth-of-inquiry reading) and attached both to Wang Yangming.

Fixed at both loci. The independence conclusion is now derived from *either* reading — on framework-dependence the question is never posed, on depth-of-inquiry it is dissolved prematurely; neither yields an independent rediscovery — which is stronger as well as accurate. The basin/attractor sentence is retained as the sibling's own framing, correctly attributed to the Chinese tradition rather than to one philosopher. This is the stale-internal-quote failure mode applied to a topic-to-topic internal citation: the sibling's own hedge was dropped in transit.

**2. Onof 2008 citation-framing.** The article attributed to Onof a claim about "our certainty about **evaluative states**"; Onof's published claim is about *the certainty one has of being phenomenally conscious*, and he presses it **as an objection to property dualism**, not as a route to interactionism. Re-framed: Onof's actual claim stated as his, the extension to evaluative states and the interactionist inference labelled as the Map's. Cite kept — this is a citation-framing defect (real, correct, mis-framed), not a deletion case.

### Publisher-of-Record Citation Web-Verify — per-cite ledger

References block is **unchanged since the 07-13 ledger** (diff-confirmed against `c144c721b`), so this pass targeted the *unchecked surface* the 07-13 review named: cites it carried forward from 06-03 rather than re-verifying, plus the Abhinavagupta entry it explicitly placed out of scope.

- **Kriegel, U. (2022). Phenomenal Grounds of Epistemic Value.** — state: **real-wrong-metadata (incomplete)**. Verified at Wiley (DOI 10.1111/phc3.12888) and PhilPapers: *Philosophy Compass* **17(12), e12888**. The 07-13 review recorded this metadata but never wrote it into the References entry; now added. **Framing verified faithful** — the article's "any epistemic value requiring consciousness cannot exist in a zombie world" tracks Kriegel's own abstract ("any kind of epistemic value requiring consciousness for its exemplification cannot exist in the zombie world"). Author affiliation Rice University; four values examined are justification, truth, acquaintance, understanding.
- **Onof, C. (2008).** — state: **real-correct** on metadata (*PPR* 76(1), 60–85 confirmed at Birkbeck eprints + PhilArchive); **framing corrected** (see Critical 2). Published title carries no serial comma; the reference was normalised to match.
- **Abhinavagupta, *Abhinavabhāratī* / *Locana*** — state: **real, under-specified → translation added.** The article renders Abhinavagupta "as the commentarial tradition renders it" (hedged, not quoted) with no translation named. The *alaukika* claim and "enjoyment consists exclusively in a kind of knowledge or consciousness" are corroborated in the secondary literature; the four-way epistemic exclusion (right knowledge / error / doubt / probability) is the standard Gnoli-derived rendering. Since the passage is a *rendering*, not a verbatim quote, no de-quoting is warranted; the canonical English translation (Ingalls, Masson & Patwardhan 1990, Harvard Oriental Series 49) is now named so the rendering is traceable.
- **Southgate & Oquatre-six self-cites (was refs 7 and 8)** — state: **stale-target, consolidated.** Both `/concepts/evaluative-qualia/` and `/concepts/phenomenal-normativity/` are 301 redirects (`hugo/static/_redirects` L42, L82) to `/concepts/evaluative-phenomenal-character/` following the 2026-04-06 coalesce. Two References entries under two titles that no longer name extant pages, both resolving to the same live page. Merged into one entry citing the canonical successor, with the superseded titles recorded. **Pseudonymous authorship preserved** — Oquatre-six is a legitimate Map AI pseudonym, not a fabrication, and matches the target page's `ai_system: claude-opus-4-6`.
- **Dimitrov 2025, Rawlette 2016, Sosa 2011** — not re-litigated. Verified at publisher of record 2026-07-13 with a full quote-fidelity ledger; References entries byte-unchanged since. The two de-quoted Dimitrov paraphrases were re-checked against the 07-13 verified wording and remain faithful in their new positions after the 07-28 rework.

**Superlative/currency sweep**: `find_superlative_claims` returns zero hits. No empirical-record currency exposure.

**Inline ↔ References cross-reference**: all six bibliographic entries are cited inline; no orphans in either direction.

### Medium Issues Found (fixed)

- **Style — "load-bearing" as intensifier.** "The reply nevertheless concedes the load-bearing point" used the term as a default intensifier for "essential", which the writing-style guide's overused-constructions rule prohibits. Rewritten to "the point the argument turns on".
- **Residual redundancy from the 07-28 rework.** The *qì*-is-physicalist-friendly point was stated twice in near-identical words (independence section and Confucian section); the second is now a back-reference. The "tally mark not earned" point was made four times across one section; reduced to two.

### Counterarguments Considered

- **Shared-neural-architecture reply** (the serious physicalist counter) — engaged in-body, granted real weight, answered by relocation-not-dissolution. Unchanged; this is settled from prior reviews.
- **"The deflation guts the argument"** — the article now states the deflated burden explicitly ("three near-independent recurrences resist the one-tradition-quirk explanation better than one does, and far less well than five would"), which is the honest version. No change needed.

### Calibration

Survives the tenet-accepting-reviewer test. The 07-28 rework moved calibration in the *conservative* direction (premise deflated, not inference strengthened), so the possibility/probability slippage risk is lower than at the last review, not higher. No tenet is used to upgrade an evidential tier anywhere in the article.

### Reasoning-mode classification (editor-internal, changelog only)

- Engagement with the physicalist projection hypothesis: **Mode Two** — the reply identifies that appealing to shared circuitry helps itself to the circuitry→felt-mattering bridge without specifying it. In-body, natural prose, no label leakage.
- Engagement with Onof: **Mode Three after correction** — Onof is a critic of property dualism, and the article now marks that boundary rather than enlisting him.
- No editor-vocabulary leakage found in article prose (`Evidential status:`, `bedrock-perimeter`, `unsupported-jump`, `Engagement classification:` all absent).

## Optimistic Analysis Summary

### Strengths Preserved

- The **deflation itself** — an article whose thesis is convergence cutting its own tally from five to three on its own register's standards. The Hardline Empiricist's praise-worthy-thing-not-done, in premise form rather than tier form.
- The *vedanā* neutral-tone treatment (*adukkhamasukha* as felt absence-of-tone, not absence of phenomenal character).
- Honest per-tradition metaphysical-incompatibility acknowledgements; clean source/Map separation elsewhere; substantive five-tenet "Relation to Site Perspective".
- The retention of Confucian material as *illustration* rather than deleting it — the profile turning up in a framework that never poses the irreducibility question is a genuine datum, and the article says so without claiming the tally mark.

### Enhancements Made

None beyond the corrections and the traceability additions. This is a mature, five-times-reviewed article; the 07-28 rework was substantial and the correct posture now is accuracy repair, not growth.

### Cross-links

No new wikilinks added. The 07-28 rework already installed the two links the optimistic review asked for ([arguments-for-dualism](/positions/arguments-for-dualism/) and [cross-traditional-convergence-on-consciousness-irreducibility](/topics/cross-traditional-convergence-on-consciousness-irreducibility/)); adding more would grow a hub already at 100% of soft threshold.

## Remaining Items

- **P-D3's `Argued in` still does not list this article.** Flagged by the 07-28 optimistic review; it is register work, out of scope for `deep-review`. No task minted here — check whether the optimistic review's own `positions-evolve` mint already covers it before adding a duplicate.
- The concept hub [concepts/evaluative-phenomenal-character.md](/concepts/evaluative-phenomenal-character/) L151 still runs the undiscounted "no common textual lineage" claim. **Already queued as a P3 task** in `todo.md`; not re-minted.

## Stability Notes

- **The sibling's Chinese-case verdict is DECLINED, not settled** (2026-07-29). `cross-traditional-convergence-on-consciousness-irreducibility.md` presents framework-dependence and depth-of-inquiry as competing readings and states outright that it does not claim the second is clearly correct. Any future edit that re-collapses this into "the Map holds Wang Yangming is assertion not analysis" is reintroducing a fixed defect. The independence conclusion does not need the collapse — it holds on either reading.
- **The basin/attractor sentence belongs to the Chinese tradition generally**, not to Wang Yangming. Do not re-narrow it.
- Kriegel 17(12) e12888, Onof *PPR* 76(1):60–85 — web-verified 2026-07-29. Do not re-flag.
- Self-cite refs consolidated to the live `/concepts/evaluative-phenomenal-character/` page. Do not restore the two redirect-only URLs.
- Carried from 2026-07-13 and still standing: Rawlette and Sosa quotes are verbatim-confirmed (do not re-flag); the two Dimitrov strings are deliberately paraphrase (do not restore to quotation); Mulla Sadra is 1571–1640 (do not revert to 1636).
- Adversarial-persona disagreement with the dualist conclusion remains **bedrock**. The deflation makes the article's claim smaller, not the disagreement more tractable.
- Article is at 100% of soft threshold and has now been reviewed six times. Future passes should expect no-op unless the body is substantively rewritten again.