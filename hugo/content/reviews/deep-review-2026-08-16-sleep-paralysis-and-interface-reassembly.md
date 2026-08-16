---
ai_contribution: 100
ai_generated_date: 2026-08-16
ai_modified: 2026-08-16 09:34:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-16
date: &id001 2026-08-16
description: 'First deep review of the sleep-paralysis reassembly article: publisher-of-record
  verification of all 17 citations found five critical defects, including a misdescribed
  anterior-cingulate result and a factor label imported from the wrong Cheyne paper.'
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-16 09:34:00+00:00
modified: *id001
related_articles: []
title: Deep Review - Sleep Paralysis, Hypnopompia, and Interface Reassembly
topics: []
---

**Date**: 2026-08-16
**Article**: [Sleep Paralysis, Hypnopompia, and Interface Reassembly](/topics/sleep-paralysis-and-interface-reassembly/)
**Previous review**: Never (first deep review; article created 2026-08-13, refined 2026-08-16)
**Word count**: 2999 → 3134 (prose ~2436 → 2520; reference apparatus ~579 → 630)

## Pessimistic Analysis Summary

### Publisher-of-Record Citation Ledger (§2.4)

All 17 references were verified at the publisher of record (Europe PMC full text, PLOS, journal landing pages). Nature's IdP redirect blocked direct fetches, so Scientific Reports / Nature Communications items were verified via their open-access PMC full text.

- Stevner et al. 2019 (*Nat Commun* 10:1035) — **real-correct**. 57 participants confirmed; the "two asymmetric processes" sentence verified verbatim to its full stop, including the "with one more likely to occur after consolidated sleep" tail.
- Wang et al. 2024 (*Sci Rep* 14:1537) — **real-wrong-claim**. Metadata, N=21, three 5-min scans at 20-min intervals, thalamic lag ~8 s → ~2.5 s, and "the cortical sensorimotor areas did not present the alterations of EEG-fMRI coupling" all confirmed. But the article's description of the anterior cingulate as recovering "at an intermediate rate" misdescribes the paper (corrected — see Critical 1).
- Kim, Moon, Mashour & Lee 2018 (*PLOS Comput Biol* 14(8):e1006424) — **real-correct**. Both quotes verified verbatim. Note: the first quote returned no match on an initial targeted fetch and a second, differently-worded query recovered it exactly — a false-negative avoided, per the citation-verify-false-negative discipline. Do not re-flag.
- Balkin et al. 2002 (*Brain*) — **real-wrong-metadata**. Claim (brainstem and thalamus reactivate first: "CBF was most rapidly re-established in centrencephalic regions") confirmed. Reference was bare "*Brain*." with "et al."; expanded to the full eight-author list, 125(10), 2308–2319, doi:10.1093/brain/awf228.
- Sodré et al. 2023 (*J Clin Med* 12(12):3876) — **real-correct**. Author list and the "usually happen in the transition from REM sleep to the waking state" quote verified verbatim.
- Sharpless & Barber 2011 (*Sleep Med Rev* 15(5):311–315) — **real-correct**. 35 studies, N=36,533, 7.6% general population, 28.3% students all confirmed (psychiatric 31.9%).
- Mainieri et al. 2021 (*J Clin Sleep Med* 17(4):719–727) — **real-correct**. Five participants; all three quotes and the 70.8% / 89.7% / 21.2% theta figures verified verbatim.
- Herrero et al. 2025 (*Sci Rep* 15:33586) — **real-wrong-metadata + real-wrong-claim**. Two wrong author initials and a missing volume/article number (see Critical 4); the OBE spectral claim was wrong on low-gamma (see Critical 3). The sleep-paralysis claims (7 participants, 2 SP episodes, theta reduced in both, low-gamma increased in both, beta increased in one of the two) and the generalizability quote all verified correct.
- Alcaraz-Sánchez 2024 (*Philos Mind Sci* 5:10233) — **real-correct metadata, over-scoped gloss**. Five dimensions named exactly right. The paper's worked case is clear light sleep, situated against neighbouring states; the article had it "locating" hypnagogia, hypnopompia and sleep paralysis. Re-scoped.
- Ghibellini & Meier 2023 (*J Sleep Res* 32(1):e13719) — **real-correct**. The sleep-offset definition verified verbatim; the "folds both under one term" claim confirmed by their own statement; Maury 1848 and Myers coinage confirmed.
- Ohayon et al. 1996 (*Br J Psychiatry* 169(4):459–467) — **real-correct metadata, dropped qualifier**. N=4,972 and the "Thirty-seven per cent…12.5%" sentence verified verbatim. The narcolepsy sentence reads "may be a better indicator"; the article had asserted it as a finding (see Medium 1).
- Cheyne, Rueffer & Newby-Clark 1999 (*Conscious Cogn* 8(3):319–337) — **real-wrong-label**. Metadata and the three-factor dual account confirmed, but the third factor is labelled "Unusual Bodily Experiences" in this paper (see Critical 2).
- Cheyne, Newby-Clark & Rueffer 1999 (*J Sleep Res* 8(4):313–317) — **real-correct**. Confirmed; also confirmed that it does *not* name a vestibular-motor factor.
- Jalal & Ramachandran 2014 (*Med Hypotheses* 83(6):755–757) — **real-correct metadata, wrong region**. The paper is about the *right superior parietal* region (it is in the title); the article said "temporoparietal". Corrected.
- Jalal, Romanelli & Hinton 2021 (*Transcult Psychiatry*) — **real-wrong-metadata**. Confirmed; Pandafeche described as an evil witch, supporting the Italy claim. Added missing 58(3), 427–439.
- Hufford 1982 (*The Terror That Comes in the Night*) — **real-correct, mis-framed**. Confirmed as the Newfoundland Old Hag study; it does not document US alien-abduction narratives (see Critical 5).
- Southgate & Oquatre-six 2026; Southgate & Oquatre-huit 2026 — Map self-citations, wikilinked in body rather than cited by author-year. Legitimate; not to be stripped.

Inline ↔ References cross-check: complete in both directions, no orphans. No superlative claims detected, so the empirical-currency sub-sweep was a no-op.

### Critical Issues Found

1. **Anterior cingulate result misdescribed (Wang et al. 2024)** — two loci (lead paragraph and the "Channels Come Back on Separate Clocks" section) described the ACC as recovering "more slowly" / "at an intermediate rate", implying a monotonic recovery slower than thalamus and faster than sensorimotor. The paper reports something else: a significant session effect in which the ACC lag ran *earlier* through the second scan and then settled *back* to ~6 s by the third — an excursion and return, not a slow recovery. Corrected at both loci. The accurate description strengthens rather than weakens the section's argument: three regions on three unlike schedules is a worse fit for a single scalar recovery variable than a clean fast/medium/slow ordering would be.

2. **Third Cheyne factor carried a label from the wrong paper** — the article attributed a "Vestibular-Motor cluster" to Cheyne, Rueffer & Newby-Clark (1999). That paper's own label is "Unusual Bodily Experiences" (floating/flying sensations, out-of-body experiences, bliss). The vestibular-motor label enters the literature later, in Cheyne's work with Girard (Girard & Cheyne 2004, *Laterality* 9(1); Cheyne & Girard 2009, *Cortex* 45(2)). Corrected to the cited paper's own label with the later relabelling noted, so the familiar term still connects to the OBE article. Also corrected the Further Reading gloss and, per family resolution, the two loci in the source research note.

3. **Herrero et al. 2025 OBE spectral claim wrong on low-gamma** — the article said the two OBE episodes showed "reduced alpha, beta and low-gamma". The paper reports low-gamma moving in *opposite* directions: OBE₁ reduced across frontal/central/temporal regions, OBE₂ increased in parieto-occipital areas. Beta decrease is real but regionally specific (fronto-central). Corrected, with the two-episode footing made explicit.

4. **Herrero et al. 2025 reference metadata** — "Corfdir, C." is Yohann Corfdir; "Capurro, A." is Lucila Capurro; Vázquez-Chenlo is A. A. Volume and article number were missing. All corrected.

5. **Cultural-record sentence mis-framed its sources** — "jinn framings in Egypt, witch figures in Italy, alien-abduction narratives in the United States (Hufford, 1982; Jalal, Romanelli & Hinton, 2021)" attached three claims to two sources that support one of them. Hufford 1982 is the Newfoundland Old Hag study (it touches UFOs only in passing and is not American); the Egypt jinn claim had no supporting citation at all. Re-framed rather than deleted, and the verified Egypt source added: Jalal, Simons-Rudolph, Jalal & Hinton 2014, in which 48% of the general Egyptian sample attributed their sleep paralysis to the Jinn.

### Candidate Issue Investigated and Rejected

**"Rule out … the single-dial picture" is NOT an internal contradiction with falsifier 1.** This pass initially flagged it as one — the body says the data "rule out" the single-dial picture while falsifier 1 treats single-scalar derivability as an open possibility — and softened the verb to "tell against". The softening was reverted after checking the 2026-08-16 refine-draft changelog entry, which had already stress-tested exactly this sentence and got it right. The body's relative clause scopes the claim precisely: the picture ruled out is one in which a scalar variable "brings the whole system back **on one clock**", and the data do rule that out, since the regions demonstrably return on different clocks. Falsifier 1 concerns a different picture — one variable reaching regions at different times *for reasons of anatomy alone*, i.e. one variable, many clocks — which remains open and is correctly nominated as a falsifier. Both statements are true and consistent.

**Do not re-flag this.** It is a convergence trap: the two sentences look contradictory at a glance and the distinction is carried entirely by the "on one clock" clause. Two independent passes have now examined it and concluded the wording is correct as written.

### Medium Issues Found

1. **Dropped modal qualifier on Ohayon's narcolepsy claim** — source says hypnopompic hallucinations "may be a better indicator of narcolepsy"; the article reported this as something the survey "found". Restored as a suggestion by the authors.
2. **Alcaraz-Sánchez scope over-specified** — re-scoped to states of minimal awareness with clear light sleep as the worked case.
3. **Two incomplete references** (Balkin, Jalal 2021) — completed.

### Counterarguments Considered

- *A production model explains all of this by different generators restarting at different rates.* Already conceded explicitly in the lead and again in the "neutral between filter and production readings" paragraph. Not a defect; the article's stake is where explanatory debts fall.
- *The spectral profile rests on 5 and 7 experiencers.* The article already says so in its own voice and nominates it as falsifier 2. Calibration is honest.

## Optimistic Analysis Summary

### Strengths Preserved

- The lead's status-first construction ("the claim's status belongs up front") is exemplary calibration and was left untouched.
- The non-independence caution in the Dualism section — refusing to count the sleep-side and anaesthesia-side asymmetries as two confirmations — is the kind of self-limiting move the common-cause null exists to enforce.
- "The evidence permits both; the Map notes which it expects" in the Bidirectional Interaction section is the correct evidential register and was preserved verbatim.
- The Myers/Maury historical irony paragraph is genuinely illuminating and verified accurate.
- Four named, specific falsifiers.

### Enhancements Made

- The corrected ACC description makes the anti-single-dial argument sharper, and a clause now states why (three regions, three unlike schedules).
- The cultural-record list is now three sourced traditions with a concrete figure (48%) rather than three loosely-attached labels.

### Cross-links Added

None. The article already carries eight Further Reading links and dense inline wikilinks; adding more would have worked against the length budget for no navigational gain.

## Calibration Assessment (§2 slippage test)

No possibility/probability slippage found. The diagnostic test — would a reviewer who fully accepts the Map's tenets still flag any claim as overstated relative to the five-tier scale? — returns no on every substantive claim. The article repeatedly declines the tenet-as-evidence-upgrade move: it concedes production-model compatibility in the lead, refuses to double-count the anaesthesia and sleep asymmetries, and closes the Bidirectional Interaction section by noting the evidence permits both readings. The one genuine over-claim found ("rule out") was an internal-consistency failure, not tenet-driven inflation, and is fixed.

## Reasoning-Mode Classification (§2.6, editor-internal)

The article names no individual opponents; it engages the production model and the single-dial arousal account generically.

- Engagement with the single-dial arousal account: **Mode One** — the coupling data are used against it on its own empirical terms, and the article names the escape route rather than pretending there is none.
- Engagement with production models generally: **Mode Three** — framework-boundary disagreement, declared outright in the lead and never dressed as refutation.

No boundary substitution. No editor-vocabulary leakage in prose (grep-checked against the full forbidden-label set: zero hits).

## Length Note

`analyze_length` reads 3134 words against a 3000 soft threshold, but this is the familiar false over-length: 630 of those words are the 18-entry bibliography (547) and the Further Reading block (83). Prose is 2520 words, comfortably below target. Roughly half the growth is the bibliographic precision §2.4 mandates (a completed Balkin entry, a new Egypt citation, added volume/page data). Prose growth was offset by tightening the Kim bridge sentence and the concession paragraph. No condensation is warranted, and a future length-triggered task on this file should decompose before acting.

## Remaining Items

None requiring a follow-up task. The corrected vestibular-motor label has been propagated to its only other corpus locus (the source research note); no other article uses it.

## Stability Notes

- **The production-model concession is bedrock, not a gap.** The article states plainly that every finding is compatible with a production model in which different generators restart at different rates. Future adversarial passes should not flag this as a weakness to be argued away — it is the article's calibration working correctly, and the argument is explicitly about explanatory debt rather than entailment.
- **The 5-and-7-participant spectral evidence is already flagged in-article and nominated as a falsifier.** Do not re-flag small samples as an unaddressed critical issue.
- **Do not "restore" the vestibular-motor label to the Cheyne, Rueffer & Newby-Clark 1999 citation.** It is the familiar term and will look like the right one, but it postdates that paper by five years. The research note now carries an explicit NB against this reversion.
- **Do not re-verify the Kim et al. 2018 "topographic similarities during emergence" quote as fabricated.** It is verbatim in the PLOS full text; a first targeted search missed it, and a second recovered it exactly.
- **The ACC is non-monotonic, not "intermediate".** If a future pass finds the phrasing awkward and reaches for "recovered more slowly", that is the defect this review removed.