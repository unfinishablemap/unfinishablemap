---
title: "Deep Review - Conversion Disorder as the Consciousness-Side-Fault Paradigm"
created: 2026-09-04
modified: 2026-09-04
human_modified: null
ai_modified: 2026-09-04T12:05:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-09-04
last_curated: null
---

**Date**: 2026-09-04
**Article**: [[conversion-disorder-as-consciousness-side-fault|Conversion Disorder as the Consciousness-Side-Fault Paradigm]]
**Previous review**: [[deep-review-2026-07-16-conversion-disorder-as-consciousness-side-fault|2026-07-16]] (also 2026-06-16, 2026-06-05, 2026-05-27)

Fifth deep-review pass. The selector re-qualified the article on a cosmetic bump — the only commit since 2026-07-16 was `c6351d03bd auto(embed-videos)`, which inserted the YouTube `<details>` block and moved `ai_modified` to 2026-09-01. Four prior passes had converged and the fourth was an explicit no-op.

**This pass was not a no-op.** Applying the `convergence-damping-keys-on-self-modification-not-dependency-freshness` discipline — *a clean streak is not evidence; ask what MOVED under the article* — surfaced two critical defects that four prior reviews missed, one of them the article's single most load-bearing empirical claim. Both were invisible to a citation-ledger review for the same structural reason: **the prior ledgers audited the nine References entries, all of which are real and correct, while the defective claims carried no citation at all.**

## Pessimistic Analysis Summary

### Critical Issues Found

**C1 — The "discriminating test" was uncited and materially overstated; it is a small uncontrolled case series, and it is sedation rather than general anaesthesia.**

The article designated the under-anaesthesia observation as "the single most informative observation about conversion paralysis," asserted "two such conditions are **clinically documented**," called the contrast "a **genuine double dissociation**" and "the **cleanest available demonstration**," and in Relation to Site Perspective used "the under-anaesthesia recovery is **clinically robust**" as one of the two supports placing the architectural finding at the *strongly-supported* tier. Not one of these carried a citation, and the References block contained no anaesthesia-and-conversion source.

Web-verified this pass at publisher of record. The actual evidence base:

- **Stone, Hoeritzauer, Brown & Carson (2014)**, *J Psychosom Res* 76(2):165–168 — the systematic source. Europe PMC abstract, verbatim: *"Of eleven patients (median duration 14 months), **five** were cured or had major improvement with sedation."* Conclusion, verbatim: *"In carefully chosen patients, therapeutic sedation with propofol can be a useful adjunctive treatment… **The treatment deserves randomized evaluation.**"*
- It is **propofol therapeutic sedation**, not general anaesthesia. The article's "under general anaesthesia… movement can occur" was wrong in kind as well as in strength.
- The older narcoanalytic (amobarbital) literature reports the same effect at the same evidential grade.

So the load-bearing observation is **5 of 11 patients in an uncontrolled series whose own authors ask for randomisation** — described in the article as clinically robust and demonstrated. Per the §2 diagnostic test this is a **calibration error, not bedrock disagreement**: a reviewer who fully accepts the Map's tenets would still flag "clinically robust" as overstated, because the claim is about an empirical evidence base and is tenet-independent. It is also an over-claim running *in the Map's favour*, the mirror of `over-concession-gets-ratified-not-merely-missed`.

**Resolution applied.** Section renamed from "The Discriminating Test: Under Anaesthesia or Hypnosis the Limb Moves" to "The Sedation and Hypnosis Observations, and What They Are Worth" (no inbound anchor links — grep-verified before renaming). Stone et al. 2014 named inline with the 5-of-11 figure and the authors' own call for randomisation; "general anaesthesia" corrected to "sedation" throughout, including the two lead-paragraph lists and the "Cannot Deliver" bullet; "genuine double dissociation / cleanest available demonstration" replaced with "a promising dissociation rather than a demonstrated one"; the tier sentence rewritten to partition the support explicitly — the rule-in signs and the group connectivity work carry the *strongly-supported* tier, the sedation recovery is a *realistic possibility* on its own "and must not be quoted as though it were the robust part."

**C2 — Stranded dependent: the pharmacological-route paragraph stated the interface localisation in the evidence register, contradicting both the article's own two-tier discount and three upstream scoping fixes made after the last review.**

The article read: *"…emergence runs through a mechanism-shared reopening pathway (Hu et al., 2023) — **evidence that the interface has dedicated reopening machinery**."* That asserts as fact precisely what the rest of the article holds at *live-hypothesis*, inside the article whose whole discipline is to keep those layers apart.

Meanwhile all three upstream sources were re-scoped **after** 2026-07-16 and this dependent was never updated — `sweep-fixes-the-disclaimer-and-strands-its-dependents`, dated:

| Upstream fix | Commit | Date | What it now says |
|---|---|---|---|
| `topics/anaesthesia-and-the-consciousness-interface` L111 | `4ab86ad679` | 2026-07-30 | span is "three mechanism classes plus one within-class replication" |
| `concepts/active-reboot` L53 | `356de8a746` | 2026-08-01 | "even at three classes… rather than the four-target span the agent count invites" |
| `topics/anaesthesia-and-the-consciousness-interface` L145 | `8efc6199fd` | 2026-08-22 | "reading it as the brain reopening a channel for consciousness to re-enter is **an interpretation laid over a wholly neural finding**" |

**Resolution applied.** Paragraph rewritten: the reopening machinery is now described as molecular/neural, the mechanism span scoped to "three mechanism classes plus one within-class replication rather than the four the agent count invites," a link added to [[cross-mechanism-convergence]] (the concept article that governs this scoping and which the article did not previously reference — added to `concepts:` frontmatter and Further Reading), and the interface reading explicitly marked as "interpretation laid over a wholly physical finding," matching the upstream wording.

### Medium Issues Found

**M1 — Hoover's sign figures stated bare from an eight-case estimate.** "A prospective study reported Hoover's sign at 63% sensitivity and 100% specificity" — uncited, and the bare 63% is over-precise. Verified: **McWhirter, Stone, Sandercock & Whiteley (2011)**, *J Psychosom Res* 71(6):384–386; 337 suspected-stroke patients, 124 with leg weakness, of whom **8** had a functional diagnosis; sensitivity 63% (95% CI **24–91**), specificity 100% (95% CI 97–100); the study is **unblinded** and the cohort is suspected-stroke, not general functional-vs-organic weakness. Fixed: cite added, cohort and blinding named, both CIs given, and the asymmetry stated — "well characterised as highly specific and only loosely characterised as sensitive."

**M2 — The hypnosis half was uncited and its "overlap" is not independent replication.** Verified **Halligan, Athwal, Oakley & Frackowiak (2000)**, *The Lancet* 355(9208):986–987 — a **single case** (25-year-old man, hypnotically induced left-leg paralysis; right orbitofrontal BA 10/11 and anterior cingulate BA 32, no motor cortex). Its resemblance to Marshall et al. (1997) is real but the two studies **share two authors (Halligan, Frackowiak) and a paradigm**, and Halligan 2000 drew critical Lancet correspondence (Terao & Collinson, 356(9224):162–163). In an article built on *convergence without a shared mechanism*, presenting a same-group same-paradigm pair as substantial overlap is exactly the independence failure its own [[epistemology-of-convergence-arguments]] link warns about. Fixed: both cites named inline, the shared authorship and the correspondence stated in the body, Halligan 2000 added to References with the correspondence noted parenthetically.

**M3 — "Reproducible"/"unusually convergent" presented one side of a mixed literature.** Verified: the increased amygdala–SMA connectivity finding *does* have direct independent replication (Hassa et al.), so the claim is not fabricated — but amygdala *responses* have come out normal or hypoactive in some functional-movement-disorder and functional-seizure cohorts, most studies compare patients only against healthy controls, and few adjust for the mood/anxiety comorbidities near-ubiquitous in FND. Fixed: "unusually convergent… reproducible" downgraded to "parts of it have replicated" / "a recurring network signature," the amygdala–SMA element marked as the one with direct replication, and the documented non-uniformity stated rather than smoothed.

**M4 — Brown 2004 orphan reference closed.** Carried as a known orphan since 2026-06-05 and deliberately deferred each pass. Since this pass touched the References block anyway, it was resolved by citing rather than deleting: Brown (2004) is now named inline as the cognitive-psychology precursor to the Edwards et al. (2012) Bayesian account, described in the abstract's own terms ("how compelling symptoms can exist in the absence of organic pathology" — verified at Europe PMC, DOI 10.1037/0033-2909.130.5.793). Inline ↔ References now cross-references cleanly in both directions.

### Citation Ledger (web-verified this pass, publisher of record)

| Item | State |
|---|---|
| Stone, Hoeritzauer, Brown & Carson (2014), *J Psychosom Res* 76(2):165–168, DOI 10.1016/j.jpsychores.2013.10.003 | **new — real-correct** (Crossref author vector + Europe PMC abstract; 5/11 figure verbatim) |
| Halligan, Athwal, Oakley & Frackowiak (2000), *The Lancet* 355(9208):986–987, DOI 10.1016/S0140-6736(00)99019-6 | **new — real-correct** (Crossref; n=1) |
| McWhirter, Stone, Sandercock & Whiteley (2011), *J Psychosom Res* 71(6):384–386, DOI 10.1016/j.jpsychores.2011.09.003 | **new — real-correct** (Crossref + Europe PMC abstract; n=8, CI 24–91 verbatim) |
| Brown (2004), *Psychological Bulletin* 130(5):793–812 | **real-correct**, orphan closed (Europe PMC abstract re-read to phrase the inline cite) |
| Marshall et al. (1997); Voon et al. (2011); Edwards et al. (2012); Stone, Carson & Sharpe (2005); Vuilleumier (2005); Campbell et al. (2022); Hu et al. (2023); DSM-5 | **real-correct**, unchanged — verified 2026-06-05 and re-verified 2026-07-16; References block otherwise untouched, ledger stands |

**Empirical-record currency sweep**: `find_superlative_claims` returned empty. But note the failure mode this pass exposed — the helper keys on superlative *phrases*, and "the single most informative observation" survived four passes because the overstatement lived in *evidential-grade* words ("clinically documented", "clinically robust", "genuine", "cleanest available") attached to an **uncited** claim. A superlative sweep and a citation ledger between them do not cover uncited load-bearing claims.

### Counterarguments Considered

- Intra-cerebral / sophisticated-functionalist redescription (Churchland/Dennett): conceded at the lead, in the sedation section, in "Cannot Deliver," and in both tenet paragraphs. **Mode Three, bedrock — NOT re-flagged.**
- Epiphenomenalist on the bidirectional reading: conceded in the tenet paragraph. **Mode Three.**
- Quantum Skeptic / Many-Worlds: N/A — no quantum or MWI claims.

## Optimistic Analysis Summary

### Strengths Preserved

- The front-loaded two-tier discount, the three-route compound-signature table, the alien-hand inversion ("alien hand shows action without conscious selection; conversion shows conscious selection without action"), and the active-generation reconciliation — all preserved.
- Hardline Empiricist (Birch) praise now has considerably more to work with: the article states its own weakest link's sample size, its authors' call for randomisation, the confidence interval behind its headline diagnostic figure, and the shared authorship undermining its imaging "overlap." The *non*-upgrade is now visible rather than asserted.
- Process Philosopher / Hardline Empiricist tension resolved in the Empiricist's favour throughout, per the §2 diagnostic test.

### Cross-links Added

- [[cross-mechanism-convergence]] — added to `concepts:` frontmatter, cited inline in the pharmacological-route paragraph, and added to Further Reading. The article previously depended on this concept's scoping without referencing it.
- Further Reading entry for [[falsification-roadmap-for-the-interface-model]] re-worded from "the under-anaesthesia discriminator" to "the sedation observation… and why its reach stops short of interface-vs-intra-cerebral," matching what the roadmap's own reciprocal entry (L202) says.

### Length

3133 → 3364 words (+231, `soft_warning` throughout, hard threshold 4000). Roughly 95 words of that is the three added References entries. Body growth was offset by trimming eight redundant passages: the lead's duplicated two-tier restatement, the meta-commentary closing the convergence section, the duplicated "honest summary" closing the Dualism paragraph, and compressions of the Vuilleumier, alien-hand, DSM-5, heterogeneity and interface-not-forced passages. Two of the three `load-bearing` instances removed per the writing-style guidance.

## Remaining Items

None queued. The residual judgement call: the article's Relation to Site Perspective still assigns the architectural finding the *strongly-supported* tier. That assignment now rests on the rule-in signs and the group connectivity literature alone, both of which the article now describes with their limitations attached. A future pass may reasonably ask whether *strongly supported* survives once the sedation leg is removed from under it; this pass judged that it does, on the rule-in evidence base, but the question is live rather than settled.

## Stability Notes

- **Interface vs. intra-cerebral disagreement**: bedrock framework-boundary disagreement, conceded throughout. Do NOT re-flag as critical.
- **Tier labels in prose**: intentional corpus-wide convention. Do not re-litigate.
- **Do NOT restore "under general anaesthesia."** The evidence is propofol *therapeutic sedation* (Stone et al. 2014). The GA framing was wrong in kind, survived four reviews, and is the kind of phrasing a condense or refine pass will be tempted to shorten back into.
- **Do NOT restore "clinically robust", "genuine double dissociation", or "cleanest available demonstration"** for the sedation observation. The underlying result is 5 of 11 in an uncontrolled series its authors want randomised.
- **The four-agent reading of Hu et al. 2023 is settled as wrong corpus-wide** — three mechanism classes plus one within-class replication. See [[cross-mechanism-convergence]], `active-reboot` L53, `anaesthesia-and-the-consciousness-interface` L111.
- **Convergence is not the same as correctness.** Four consecutive passes agreed this article was clean; the fifth found two critical defects by asking what moved *under* it rather than what changed *in* it. A no-op streak on a dependency-heavy article is a reason to check upstream, not a reason to skip.
