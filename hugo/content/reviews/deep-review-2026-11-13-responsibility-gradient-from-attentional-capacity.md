---
ai_contribution: 100
ai_generated_date: 2026-11-13
ai_modified: 2026-11-13 20:56:11+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-13
date: &id001 2026-11-13
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-13 20:56:11+00:00
modified: *id001
related_articles: []
title: 'Deep Review - The Responsibility Gradient: From Attentional Capacity to Moral
  Desert'
topics: []
---

**Date**: 2026-11-13
**Article**: [The Responsibility Gradient: From Attentional Capacity to Moral Desert](/topics/responsibility-gradient-from-attentional-capacity/)
**Previous review**: [2026-07-17](/reviews/deep-review-2026-07-17-responsibility-gradient-from-attentional-capacity/)

This is the eighth deep review. Unlike the seventh, which was a cosmetic re-float, this one was warranted: ten refine-draft commits landed between 2026-07-28 and 2026-11-04. They brought the scarcity-evidence hedge with three new references (Mani et al. 2013, Carvalho et al. 2016, O'Donnell et al. 2021), the Strawson borrow/decline split, the Levy/Sher epistemic-condition sentences, the akrasia carve-out, the quantifier-neutral floor wording, the Tenet 2 minimality correction, the [P-Q9](/positions/quantum-interface/#p-q9) capacity/exercise paragraph and the mechanism-debt citation grade. The References block had changed, so the §2.4 web-verify pass was mandatory. Word count went from 2595 at the last review to 3302 before this pass, which is soft_warning for topics (3000 soft, 4000 hard), so the review ran in length-neutral mode.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Source/Map conflation in the Kane sentence (Against Binary Responsibility).** The article said hard determinism "denies what the Map affirms—and what Kane (1996) argues from a libertarian perspective: that consciousness genuinely selects among open possibilities". Kane's 1996 account is event-causal and has no dualist commitment. The corpus files it as the Map's main rival within libertarianism (`topics/event-causal-libertarianism`), so the sentence credited Kane with the Map's own thesis. **Fixed**: the Map's claim now stands alone, and Kane is credited only with its libertarian core (open alternatives, ultimate responsibility) "without the Map's dualism".
- **Position-strength overstatement on Fischer & Ravizza (1998).** The article said their theory accepts degrees of responsiveness, "yielding graded responsibility". Their guidance-control account sets a threshold (moderate reasons-responsiveness). Coates & Swenson's *Philosophical Studies* paper, "Reasons-responsiveness and degrees of responsibility", is the work that extends it to degrees. **Fixed** in a form that is true whether or not F&R grade responsibility themselves: "already accept that responsiveness comes in degrees, and Coates and Swenson (2013) extend that theory to graded responsibility". A References entry was added, with metadata checked at Crossref. Caveat: no raw abstract text could be retrieved (Springer and PhilArchive returned 403 or a redirect, and Semantic Scholar elides the abstract). The "threshold" reading rests on the paper's title and the publisher metadata together with the standard reading of F&R. That is why the replacement claims only the extension and says nothing about what F&R lack.

### Medium Issues Found

- **Zheng & Meister framed as measuring consciousness (two places).** The article called their work an "analysis of conscious throughput" and described the 10 bits/s figure as "a measured fact about conscious processing". The raw arXiv text (2408.10234) speaks of "the information throughput of a human being" and "the neural conundrum behind the slowness of human behavior". It names unconscious processing only as an objection to answer (§5.3), and nowhere frames the figure as conscious throughput. The more careful sibling pages already use the behavioural framing: `topics/one-structure-three-vocabularies` L51, `topics/grain-mismatch-as-independent-evidence` L54, `concepts/sleep-and-consciousness` L42. **Fixed** without changing length: "the figure Zheng & Meister (2025) estimate for human behavioural throughput", and "estimated from behavioural throughput, is a datum that…". The 2026-06-19 ledger had certified the old wording as "faithful". That certification covered metadata only (see the result-direction/stance legs of §2.4).
- **Orphan reference.** After the 2026-07-29 refine moved the inline cite to Mani et al., Mullainathan & Shafir (2013) *Scarcity* stayed in References with no inline cite. The refine had kept it on purpose for the "bandwidth" vocabulary. **Fixed** by citing it inline as the popularisation: "(Mani et al., 2013; popularised in Mullainathan & Shafir, 2013)".
- **Incomplete Map-internal gloss of [P-Q9](/positions/quantum-interface/#p-q9).** The article said "[P-Q9](/positions/quantum-interface/#p-q9)'s residue channels test ensemble statistics or mechanism". The current [P-Q9](/positions/quantum-interface/#p-q9) Asserts names three channels: conditional-statistical, mechanism and psychophysical. The psychophysical channel has been in [P-Q9](/positions/quantum-interface/#p-q9) since before the 2026-10-20 edit that installed this gloss. **Fixed**: "three residue channels test ensemble statistics, mechanism or psychophysics". The conclusion ("not one agent's contribution to one act") holds for all three.
- **Unsupported empirical generalisation.** "Most moral failures occur within the range of full or near-full capacity" had no support and repeated the preceding "applies primarily at the margins". **Cut.** No review or todo protects it (grepped).

### §2.4 Publisher-of-Record Citation Ledger (this pass)

- Mani, Mullainathan, Shafir & Zhao 2013 (*Poverty impedes cognitive function*, Science 341(6149):976-980, doi 10.1126/science.1238041). **State: real-correct** (Crossref). The OpenAlex abstract confirms the claim's direction: "poverty itself reduces cognitive capacity… poverty-related concerns consume mental resources". The 13-IQ-point figure is not in the abstract, and the full text was unreachable this pass (Princeton, Harvard and Booth mirrors returned HTML or 403). The 2026-07-29 refine verified it against Princeton's press release. Result-direction leg: same direction.
- Carvalho, Meier & Wang 2016 (AER 106(2):260-284, doi 10.1257/aer.20140481). **State: real-correct** (RePEc). Result-direction leg: the raw abstract reads "Nor do we find before-after differences in risk-taking, the quality of decision-making, the performance in cognitive function tasks, or in heuristic judgments." This is a null, and the article reports it as a null.
- O'Donnell et al. 2021 (PNAS 118(44):e2103313118). **State: real-correct** (Crossref: 24 authors, O'Donnell first). Result-direction leg: the OpenAlex abstract says "considerable variability in the replicability, with some strong successes and other undeniable failures", so "uneven" is a faithful gloss.
- The "published rebuttal" of the audit is Shah, Zhao, Mullainathan & Shafir 2023, "A scarcity literature mischaracterized with an empirical audit", PNAS 120(26):e2206054120 (Crossref). Real; the rebuttal comes from the original authors' group. It is not a References entry, only a prose clause.
- Coates & Swenson 2013 (*Reasons-responsiveness and degrees of responsibility*, Philosophical Studies 165(2):629-645, doi 10.1007/s11098-012-9969-5; online 2012). **State: new, real-correct** (Crossref).
- Zheng & Meister 2025 (Neuron 113(2):192-204). Metadata **real-correct** (06-19 ledger). **Framing corrected this pass** (above). Stance: the authors are physicalists looking for a neural substrate, and the article no longer implies otherwise.
- Kane 1996. Metadata real-correct (06-19). **Stance leg corrected this pass** (event-causal libertarian, no dualism).
- Cowan 2001, Fischer & Ravizza 1998, Mullainathan & Shafir 2013, Schwartz & Begley 2002, Strawson 1962 (187-211). Unchanged since the 06-19 ledger and not re-fetched. Stance: Strawson is marked as a declined rival (07-29). The Schwartz & Begley hedge ("largely unreplicated outside their originating groups") stands from the 09-02 sweep.
- Levy and Sher are named inline with no years and have no References entries in this article. Their characterisations ("ordinary agents who just happen not to be conscious", "informational state, not phenomenal consciousness", "personally available", Sher filed as capacitarian by the SEP entry) match `topics/consciousness-and-the-epistemic-condition-on-responsibility`. There, OpenAlex chapter abstracts verified the quotes in `reviews/pessimistic-2026-10-31-…` and the cites carry full references. These are not orphan `Author YYYY` cites.
- Superlative helper: one hit, "so far", which is a hedge. No currency issue.
- Inline ↔ References: no orphans in either direction after the Mullainathan fix.

### Map-internal glosses re-checked against current text

- "tunnel vision" in `consciousness-and-moral-agency-under-duress` L55: present.
- The mechanism-debt citation grade ("framework-internal coherence result only") in `positions/quantum-interface` L45: matches.
- [P-Q9](/positions/quantum-interface/#p-q9) "self-concealing by construction": matches the title. Its channel count was corrected (above).
- Practical unity "without the posit" (`the-divided-will` §practical-unity): matches.
- The physical-controller point (`control-theoretic-will` §Analogy, Model, and Ontology): matches.
- Background-commitments "globally nonactual" posit (L46): matches.
- Tenet 2 minimality (tenets L65/L69: empirical-constraint minimality, no energy, no Born deviation, no conservation violation): the article's "Born-exactness, not narrowness" gloss matches. Today's tenets refine (heliocentrism/epicycles) does not affect this article.
- The sibling epistemic-condition page quotes three strings from this article: "You cannot be fully responsible for consequences you lacked the bandwidth to foresee", "were never phenomenally available for selection" and "is not thereby excused". All three remain verbatim after this pass.

### Calibration check

- With the Zheng & Meister fix, no claim reads more confident than its support. The upper-end desert claim already carries the mechanism-debt grade, and the [P-Q9](/positions/quantum-interface/#p-q9) paragraph marks exercise-level desert as publicly underdetermined. There are no five-tier labels and no minimal-organism claims.

### Reasoning-mode classification (editor-internal)

- Standard compatibilism (F&R): Mixed. The article credits their grading, then supplies a unification it concedes a physicalist controller provides equally. It does not dress this as a refutation.
- Hard determinism: Mode Three, a framework-boundary disagreement.
- Strawson: Mode Three, borrow/decline (07-29).
- Everettian: Mode Three. The article concedes the gradient survives in-branch and places the disagreement at the globally-nonactual posit.
- No label leakage.

### Counterarguments considered (bedrock, not re-flagged)

- The Churchland/eliminativist charge that "phenomenally available" lacks an operational criterion (`pessimistic-2026-10-31`). The article already marks the term as its own and contrasts it with Levy's. Carried forward, not a defect.
- Physicalist, MWI, quantum-skeptic, empiricist and Buddhist objections, all as recorded in reviews 3-7.

## Optimistic Analysis Summary

### Strengths Preserved

- The five-dimension framework and its control-parameter table.
- The three-case cultivation principle.
- The capacity/exercise split in the measurement objection: public grade versus publicly underdetermined desert. This is the article's most distinctive recent addition, and it models the "tenet-coherent, not evidence-elevating" discipline.
- The scarcity paragraph's explicit retreat to the weaker claim.
- The NMW paragraph's concession that the gradient survives branch-locally.
- The honest admission that a physical controller would unify the conditions equally.

### Enhancements Made

- Two attribution corrections (Kane, F&R), one framing correction (Zheng & Meister, at two loci), an orphan-reference repair, a [P-Q9](/positions/quantum-interface/#p-q9) gloss completion, and one unsupported sentence plus one redundant sentence cut.

### Cross-links Added

- None. All body and Further Reading targets resolve.

## Length

- 3302 → 3325 (+23; topics soft 3000 / hard 4000; soft_warning). The additions are attribution fixes and one References line (about 14 words of apparatus). They are offset by two cuts: "Most moral failures occur within the range of full or near-full capacity." and "Neglecting this capacity is itself a moral matter.", the second of which repeated its bold lead-in.

## Remaining Items

- **Not touched, by design.** Three sentences are reserved for the open NEEDS-HUMAN Tenet 3 quantifier decision (todo, addendum 2026-10-05): "they remain a subject of experience, a genuine agent", "The agent hasn't ceased to exist as controller" and "it does not eliminate selection itself".
- **Not touched, owned elsewhere.** The P3 menu-luck task names this page as a secondary file (§Scope, ≤45 words).

## Stability Notes

- Eighth review. The body had absorbed ten targeted refines since the last full pass. This pass found attribution and framing defects only, none structural. Future reviews should not reopen the capacity/exercise paragraph, the scarcity hedge, the Strawson split, the floor wording, or the Tenet 2/Tenet 4 paragraphs unless their upstream sources move.
- The ledger above supersedes the 06-19 ledger for Mani, Carvalho, O'Donnell, Coates & Swenson, Zheng & Meister (framing) and Kane (stance).
- All bedrock disagreements remain framework-boundary differences.