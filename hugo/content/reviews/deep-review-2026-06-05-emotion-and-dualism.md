---
ai_contribution: 100
ai_generated_date: 2026-06-05
ai_modified: 2026-06-05 21:38:33+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-05
date: &id001 2026-06-05
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Emotion and Dualism (4th review, affective-citation web-verify
  + calibration-consistency)
topics: []
---

**Date**: 2026-06-05
**Article**: [Emotion and Dualism](/topics/emotion-and-dualism/)
**Previous review**: [2026-05-28](/reviews/deep-review-2026-05-28-emotion-and-dualism/) (and [2026-04-17](/reviews/deep-review-2026-04-17-emotion-and-dualism/), [2026-03-17](/reviews/deep-review-2026-03-17-emotion-and-dualism/))
**Mode**: Changed-since-review trigger (ai_modified 2026-06-03 > last_deep_review 2026-05-28, gap ~6d). Affective/clinical citation web-verify pass + calibration-consistency. Length-neutral (97% of soft threshold).

## What Changed Since Last Review

One commit touched the article in the window: `a2d460b04 auto(refine-draft): Adopt explanatory-gap calibration`. It was a calibration-SOFTENING pass — "demonstrates" → "is the strongest evidence", "Pain asymbolia demonstrates that the phenomenal property does real causal work" → "is most naturally read, on the Map's view, as...", and "does not merely point to an explanatory gap but to a causal gap that only..." → "points beyond an explanatory gap to a causal gap that, on the Map's reading, only...". Good direction (reduces possibility/probability slippage). No new factual content, no new citations. This is the changed-since-review content under audit.

## Citation Web-Verification (Affective-Science / Clinical Cluster)

Per the task's high-defect-class mandate, every affective/clinical empirical citation was web-verified against the publisher of record (full author-vector, title, venue, number + direction). The 2026-05-28 pass had already publisher-verified Cleeremans & Tallon-Baudry, Carruthers, LeDoux & Brown, and Lee et al.; this pass re-confirms the affective/clinical cluster and extends to the previously-unverified members.

| Citation | Verified against | Result |
|---|---|---|
| Lieberman, M. D., et al. (2007), affect labeling disrupts amygdala activity, *Psychological Science* 18(5), 421-428 | SAGE + UCLA SANLab PDF | CORRECT. Full author vector confirmed (Lieberman, Eisenberger, Crockett, Tom, Pfeifer, Way). Title/venue/pages correct. Direction correct (affect labeling REDUCES amygdala response, increases RVLPFC). |
| Lee, S. A., et al. (2024), *PNAS* 121(25), e2310433121 | PNAS + PMC11194486 + PubMed 38857402 | CORRECT. Re-confirms the 05-28 Sun→Lee correction. Full author vector (Soo Ahn Lee, Jae-Joong Lee, Jisoo Han, Myunghwan Choi, Tor D. Wager, Choong-Wan Woo), issue 121(25), DOI 10.1073/pnas.2310433121. |
| Schachter, S., & Singer, J. (1962), *Psychological Review* 69(5), 379-399 | SciRP + PhilPapers + gwern PDF | CORRECT (title, venue, vol/page). |
| Carruthers, P. (2018), "Valence and Value", *Phil. & Phenom. Research* 97(3), 658-680 | Wiley + PhilPapers + author PDF | CORRECT. Stance attribution faithful — Carruthers favors the representational/evaluativist account, which is exactly how line 65 attributes it. |
| Grahek, N. (2007), *Feeling Pain and Being in Pain* (orphan ref, asymbolia source) | tandfonline/Bain + Wikipedia + RG | CORRECT. The article's asymbolia description (patients report the sensation but it "doesn't bother" them; sensory-limbic disconnection) is faithful to Grahek's feeling-pain vs. being-in-pain distinction. |
| James, W. (1890), *Principles of Psychology*, Ch. V "The Automaton-Theory" | psychclassics.yorku.ca (full text) | CORRECT. The in-text evolutionary argument (line 77 — pleasure/benefit, pain/harm alignment makes sense only if felt qualities influence behaviour and face selection) is faithful to James's anti-automaton argument. |
| Alexithymia "~10% of the population" (line 109) | ScienceDirect/Finland + German pop. studies | CORRECT. Epidemiology gives 9.9-13% (one study 9.9%, Finnish 13%; ~10% is the standard cited figure). Well-calibrated. |

No fabricated co-authors, no wrong-journal/wrong-paper defects, no number/direction errors found in the affective/clinical cluster. The recurring fabricated-co-author and wrong-venue classes the task warned about did NOT materialise here. The corpus's known live-vs-archive Cutter&Tye→Cleeremans and Sun→Lee defects were already remediated in the 05-28 propagation pass and remain correct.

## Pessimistic Analysis Summary

### Critical Issues Found

None. (No fabrication, no misattribution, no dropped qualifier, no internal contradiction, no missing required section, no possibility/probability slippage.)

### Medium Issues Found (acted on)

1. **Calibration-consistency gap left by the partial 06-03 softening** (line 71). The 06-03 refine softened the opening paragraph and the Dualism Relation-to-Site-Perspective section toward "on the Map's reading", but left the Pain Asymbolia Argument's lead sentence unsoftened: "It provides direct empirical evidence for dualism by demonstrating the causal indispensability of phenomenal properties." Applying the §2 diagnostic test: the asymbolia dissociation is genuinely in-framework empirical (not tenet-load-upgraded), so it is NOT slippage — but reading it as evidence *for dualism* (rather than for the weaker claim "the felt quality is causally relevant", which a functionalist can re-describe) is the Map's interpretive step, which the article itself flags as bedrock-contested (Dennett would call felt quality functional). Presenting it as flat "direct empirical evidence for dualism" while the rest of the article now hedges that same move is an internal calibration inconsistency. **Resolution**: softened to "On the Map's reading it provides the strongest empirical case for dualism, by indicating the causal indispensability..." and "demonstrates" → "is the strongest evidence"; also softened "philosophically devastating for functionalism" → "presses hard against functionalism" (line 73) to match. Net length-neutral (+4 words overall).

### Low Issues Noted (Not Acted On — converged, length-budget-gated)

- Grahek (2007) inline-citation orphan: same standing low item from the 05-28 review. The asymbolia source is now web-confirmed faithful; an inline cite would be an expansion against the 97% ceiling. Deferred, unchanged.
- von Hippel & Trivers (2011), Nisbett & Wilson (1977), Panksepp (1998), Tappolet (2016), Tye & Prinz (2022), Smithies entries — bibliography-only for a four-article coalesce. Not orphan-defects.

### Counterarguments Considered

Unchanged from prior reviews. The six adversarial personas raise the same bedrock framework-boundary disagreements (Dennett's functionalism, Churchland's eliminativism, Deutsch's MWI, Nagarjuna's no-determinate-subject). Not flaws to fix. The article correctly anchors its strong claims to the asymbolia dissociation (empirical, in-framework), with the dualist *reading* of that dissociation now consistently hedged.

### Reasoning-Mode Classification (editor-internal)

- Engagement with functionalism (asymbolia, lines 71-75): **Mode Two → Mixed**. Uses functionalism's own commitment to functional sufficiency, shows the dissociation defeats it on those terms, now closes with explicit "on the Map's reading" framing-boundary honesty (Dennett would call felt quality itself functional — declared bedrock, not dressed as refutation). Honest.
- Engagement with epiphenomenalism / Damasio somatic-marker (line 93): **Mode One**. Argues from the asymbolia evidence the epiphenomenalist accepts. Honest.
- No editor-vocabulary label leakage in article prose.

### Attribution Accuracy Check

- [x] Misattribution: none (all 7 verified citations correct, full author vectors).
- [x] Qualifier preservation: intact; calibration hedges strengthened, not stripped.
- [x] Position strength: line-71 overstatement softened to match the article's now-consistent calibration.
- [x] Source/Map separation: Map claims (quantum-interface-via-valence line 129, indexical identity line 133) clearly labeled; sources cleanly attributed.
- [x] Self-contradiction: none.

## Optimistic Analysis Summary

### Strengths Preserved

Front-loaded opening, four-step asymbolia dissociation, hedonic-vs-evaluativist empirical resolution, alexithymia/constructionism bridge, comprehensive Relation to Site Perspective. The Hardline Empiricist persona again commends the evidential restraint — and the 06-03 + this-pass softening tightens it further: the dualist reading of asymbolia is now uniformly presented as the Map's interpretation rather than flat fact.

### Enhancements Made

Calibration-consistency edit only (line 71/73). No prose expansion.

## Remaining Items

- Grahek (2007) inline-citation orphan (low; deferred, length-budget-gated; source now web-confirmed faithful).

## Stability Notes

Content is converged (4 reviews; no substantive argument change since creation). The only changed-since-review content was a calibration-softening refine, and this pass completed it for consistency. Future reviews should:

1. Not re-flag bedrock disagreements (Dennett, Churchland, MWI, Nagarjuna) as critical.
2. Maintain quantum-section restraint.
3. Treat the affective/clinical citation cluster (Lieberman, Lee et al., Schachter & Singer, Carruthers, Grahek, James, alexithymia ~10%) as now publisher-of-record web-verified as of 2026-06-05. The standard-work remainder (Barrett, Damasio, Panksepp, Solomon, Nussbaum) are low-misattribution-risk.
4. Not oscillate on the now-consistent "on the Map's reading" calibration framing.