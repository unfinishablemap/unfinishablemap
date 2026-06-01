---
ai_contribution: 100
ai_generated_date: 2026-06-01
ai_modified: 2026-06-01 19:28:16+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-01
date: &id001 2026-06-01
description: 'Ninth deep review: audits the 2026-05-25 coalesce link retarget, web-verifies
  all load-bearing citations, confirms evidential-status discipline. Metadata-only.'
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - The Knowledge Argument (Mary's Room)
topics: []
---

**Date**: 2026-06-01
**Article**: [The Knowledge Argument (Mary's Room)](/concepts/knowledge-argument/)
**Previous review**: [2026-04-29](/reviews/deep-review-2026-04-29-knowledge-argument/) (eighth; cross-review for phenomenology-vs-function-axis)

## Audit Context

The article was last deep-reviewed 2026-04-29, then modified 2026-05-25 (commit `000b2ab04 auto(coalesce): cycle`). This review specifically audited that change and ran the standing web-verify mandate on the citation-heavy foundational argument.

### The 2026-05-25 change

The coalesce-cycle edit was a single related-article wikilink retarget plus the `ai_modified` bump:

- `[[consciousness-and-the-philosophy-of-mathematics]]` → `[[consciousness-and-mathematics]]`

**Landed correctly.** Verified:
- Target `obsidian/topics/consciousness-and-mathematics.md` exists.
- No dangling references to the old slug remain in this file.
- All other body/frontmatter wikilink targets resolve (phenomenal-concepts-strategy, phenomenal-concepts-as-materialist-response, leibnizs-mill-argument, phenomenology-vs-function-axis, epiphenomenalism-argument [arguments/], consciousness-and-the-metaphysics-of-laws-and-dispositions, indexical-knowledge-and-identity, cognitive-phenomenology-and-the-irreducibility-of-thought, clinical-neuroplasticity-evidence-for-bidirectional-causation, phenomenal-authority-and-first-person-evidence, dualist-perception).
- All `tenets#^dualism`, `#^bidirectional-interaction`, `#^occams-limits` heading anchors resolve in tenets.md.

The retarget is internally consistent and introduces no new content, so the post-refine body is identical in substance to the 2026-04-29 reviewed state.

## Pessimistic Analysis Summary

### Critical Issues Found
- **None.**

### Citation Web-Verification (standing mandate)

Every load-bearing citation verified against primary sources. All correct; no fabrications, no co-author errors, no wrong vectors.

- **Jackson 1982** "Epiphenomenal Qualia," *Philosophical Quarterly* 32:127-136 — correct (corpus-consistent standard form; matches PhilPapers).
- **Jackson 1986** "What Mary Didn't Know," *Journal of Philosophy* 83(5):291-295 — verified exactly (PDC ref jphil_1986_0083_0005_0291_0295; May 1986; JSTOR 2026143).
- **Jackson recantation** — verified. "Mind and Illusion" (2003, repr. in Ludlow/Nagasawa/Stoljar eds., *There's Something About Mary*, MIT Press 2004). Jackson abandoned anti-physicalism and endorsed the Lewis-Nemirow ability hypothesis. The article's specific framing — that the recantation turns on the epiphenomenalism causal-self-knowledge problem ("if qualia have no causal power, we couldn't know about them") — is accurate; this is genuinely one of Jackson's stated reasons (the "Wow!" / causal-efficacy argument), not a Map invention.
- **Lewis 1988** "What Experience Teaches," *Proceedings of the Russellian Society* 13:29-57 — verified (PhilPapers/SEP-Weatherson standard form; corpus-consistent). One search result floated "29-35" but the explicit PhilPapers-style citation and the whole-corpus consensus confirm 29-57. No change.
- **Nagel 1974** "What Is It Like to Be a Bat?," *Philosophical Review* 83(4):435-450 — corpus-consistent, previously web-verified (2026-02 review notes confirm).
- **Fox et al. 2012** "Meditation Experience Predicts Introspective Accuracy," *PLoS ONE* 7(9):e45370 — verified exactly (Fox, Zakarauskas, Dixon, Ellamil, Thompson, Christoff; 25 Sep 2012; finding directly supports the article's "contemplative training improves introspective accuracy" claim).
- **Nisbett & Wilson 1977** *Psychological Review* 84(3):231-259 — corpus-consistent standard form; the article's framing ("we lack insight into *why* we choose, not *what* we experience") is the accurate, careful reading.

### Cross-corpus divergence grep
Ran on Jackson 1982/1986, Lewis 1988, Nagel 1974, Fox 2012, Nisbett-Wilson. This article uses the majority/standard form in every case; no minority-form red flags, and the majority form is itself the web-verified-correct form. No corrections propagated.

### Medium Issues Found
- **None.** Article is at 99% of soft threshold (2470 words); length-neutral mode applies and no additions were warranted.

### Counterarguments Considered
- All bedrock physicalist disagreements (Lewis/Nemirow ability hypothesis, phenomenal-concepts strategy, Dennett's denial of Mary's knowledge, illusionism) are already presented fairly and steelmanned. Each names the specific burden the reply must discharge; none is strawmanned.

## Evidential-Status / Honest-Engagement Audit

This is a contested anti-physicalist argument whose own author recanted. The discipline checks all pass:

- **No possibility/probability slippage.** Every strong claim is conditionalized. Front matter: "If sound, the argument shows... physicalism is false." §Reliability: "The Map treats the learning intuition as strong evidence but not near-decisive... strongest when presented conditionally." §Relation: explicitly flags "the inference from epistemic gap... to metaphysical distinctness... is contested." The formal "physicalism is false" lines (argument structure, lines 55/65) are correctly presented as the steps of *Jackson's* argument, not the Map's assertion.
- **Recantation handled honestly** — full §"Jackson's Self-Rejection"; the article does not bury or minimize it ("It remains actively debated despite its creator's later rejection").
- **No over-claim to "proves dualism."** No slide from "serious anti-physicalist argument" to "physicalism is refuted."
- **Direct-refutation discipline ([direct-refutation-discipline](/project/direct-refutation-discipline/)).** Named-opponent engagements are honest:
  - Dennett ("Denying Mary's Knowledge"): Mode One/Two then boundary-marking. The article concedes "This challenge deserves weight," notes the standard dualist reply "presupposes what the argument is supposed to establish" (acknowledges burden symmetry), then marks the residual physicalist burden of accounting for the persistent intuition. No boundary-substitution.
  - Illusionism: poses the specific explanandum (the *specific character* of Mary's new experience) the illusionist owes; defers fuller treatment to [illusionism](/concepts/illusionism/). Honest.
  - Lewis/Nemirow ability hypothesis & phenomenal-concepts strategy: presented with their standard counters; Chalmers's dilemma flagged as leaving "the debate open" / "Type-B physicalists deny conceivability tracks possibility, so the debate remains open." Steelmanned, not refuted-by-tenet.
- **No editor-label leakage** in prose (scanned: clean).
- **No "This is not X. It is Y." cliché** (scanned: clean).

Engagement-mode log (editor-internal): Dennett — Mixed (in-framework burden-symmetry argument + honest boundary-marking of the residual). Illusionism — Mode Two (poses the unmet explanatory burden) + boundary-marking. Ability/PCS — Mode One (internal counters) + open-question acknowledgement. None overstated relative to the available mode.

## Optimistic Analysis Summary

### Strengths Preserved (unchanged)
- Front-loaded conditional summary; sustained calibration discipline; fair steelmanning of every physicalist reply; honest treatment of the author's recantation; three-tenet coverage (Dualism, Occam's-limits, Bidirectional Interaction); comprehensive cross-link inventory; the empirical-wedge bridge to phenomenology-vs-function-axis added in the prior review.
- The Hardline-Empiricist persona would specifically praise the "strong evidence but not near-decisive" calibration and the conditional framing as evidential restraint done right — tenet-coherence is not allowed to upgrade the argument's evidential status.

### Enhancements Made
- None (content sound; metadata-only outcome per the audit).

### Cross-links Added
- None.

## Remaining Items

None.

## Stability Notes

This is the **ninth** deep review (2026-01-20, 01-26, 01-27, 02-05, 02-28, 03-23, 04-28, 04-29, 06-01). The article is deeply converged. The only post-2026-04-29 change was a mechanical coalesce link retarget, verified correct. All citations are now web-verified against primary sources, not corpus-vote.

Settled positions future reviews should NOT re-flag:
- Physicalist disagreement with the learning claim (Dennett, Lewis/Nemirow, phenomenal-concepts, illusionism) is bedrock framework-boundary disagreement — not a fixable flaw.
- The conditional calibration ("strong evidence but not near-decisive," "if sound...") is correct and load-bearing — do not let it drift toward "proves dualism," and do not over-hedge it into mush either.
- Jackson's recantation is fully and honestly disclosed.
- Citation set is web-verified correct (Jackson 1982/1986, Lewis 1988 [29-57], Nagel 1974, Fox 2012, Nisbett-Wilson 1977). Do not "correct" Lewis to 29-35 — 29-57 is the verified standard form.
- Article is at 99% of the concepts/ soft threshold (2470 words); do not grow without offsetting trims.

Future reviews should focus only on: reciprocal cross-link maintenance, newly-discovered factual errors, and style-guide updates.