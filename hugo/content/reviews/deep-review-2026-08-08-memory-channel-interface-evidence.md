---
ai_contribution: 100
ai_generated_date: 2026-08-08
ai_modified: 2026-08-08 23:17:52+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-08
date: &id001 2026-08-08
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-08 23:17:52+00:00
modified: *id001
related_articles:
- '[[memory-channel-interface-evidence]]'
title: 'Deep Review - Memory-Channel Interface Evidence: Vulnerability Ordering and
  Recovery-Order Asymmetry'
topics: []
---

**Date**: 2026-08-08
**Article**: [Memory-Channel Interface Evidence: Vulnerability Ordering and Recovery-Order Asymmetry](/topics/memory-channel-interface-evidence/)
**Previous reviews**: [2026-07-20](/reviews/deep-review-2026-07-20-memory-channel-interface-evidence/) (no-op confirming) · [2026-07-12](/reviews/deep-review-2026-07-12-memory-channel-interface-evidence/) · [2026-06-16](/reviews/deep-review-2026-06-16-memory-channel-interface-evidence/)

**Verdict: SUBSTANTIVE PASS.** Lens = *empirical-claim fidelity* (does the paraphrase match what the study found?) plus *orphan-reference audit*. Two critical defects fixed; five orphan references adjudicated; six reference entries corrected at the publisher of record. Prose 3696 → 3885 words (+189; the `analyze_length` total of ~4500 includes 604 words of References/Further Reading apparatus — the **length warning is false**, see Stability Notes).

## Method note

Prior ledgers on this article record *metadata* verification (06-04, 06-05, 06-16) and *quote* verification (07-12). Neither speaks to whether the article's **paraphrases** match what the cited studies actually found, nor to whether every reference is **used**. Those two axes were the target of this pass. WebSearch budget was exhausted for the session; all verification was done by WebFetch against EuropePMC, OpenAlex, Semantic Scholar and PubMed records of the primary text.

## Orphan-reference audit

Surname counts over prose only (frontmatter stripped, apparatus excluded) confirmed the driver's measurement: **Mashour 0 · Sarasso 0 · Hu 0 · Reinders 0 · Bodien 0**, with zero numeric `[N]` and zero `[^footnote]` markers anywhere in the prose. The article cites by inline surname and nothing else, so these were genuine orphans rather than a citation-style artefact.

**All five were wired in; none was removed.** All five are real papers verified at the publisher of record, and each turned out to support a claim the article was already making without attribution.

| Reference | Verdict | Where it landed |
|---|---|---|
| Sarasso et al. 2015, *Curr Biol* 25(23) | **Wired in** | The article's xenon-ketamine contrast *is* this paper's result. It was being asserted unattributed. |
| Mashour 2024, *Neuron* 112(10) | **Wired in** | Review anchor for "several pharmacologically distinct mechanisms converging on one ordering". |
| Hu et al. 2023, *Nat Neurosci* 26(5) | **Wired in** | Supports "emergence is not the reverse of induction" — emergence is an *active* process, not passive washout. Doubles as the replacement for a false attribution (below). |
| Reinders et al. 2003, *NeuroImage* 20(4) | **Wired in** | Imaging evidence for the DID row's between-alter compartmentalisation. |
| Bodien et al. 2024, *NEJM* 391(7) | **Wired in** | Behaviour/cognition dissociation documented outside pharmacology (cognitive motor dissociation), supporting the self-stultification link. No figure quoted, so no numeric surface added. |

The driver flagged Sarasso, Hu and Bodien as possibly covering material genuinely absent from the article. On read, **Sarasso and Hu were false negatives of the surname count** — the article states their findings in full, just anonymously. **Bodien** was the genuine borderline: disorders of consciousness is not one of the article's five clinical-state rows. It was retained and wired in a single clause because it grounds a claim the article already leans on (behavioural unresponsiveness does not entail absence of cognition) rather than opening a sixth row.

The two `Southgate & Oquatre-sept` entries are the Map's own coalesced predecessor articles, recorded under `coalesced_from:`. They legitimately sit as bibliography and were left alone.

## Pessimistic Analysis Summary

### Critical Issues Found (2)

**1. False attribution — a regional finding credited to a study that made none.** `obsidian/topics/memory-channel-interface-evidence.md` L128.

- *Before*: "…Stone, Kelz, Proekt, and Wasilczuk (2025, *British Journal of Anaesthesia*) found genetically identical mice under identical protocols emerging at times varying by at least two orders of magnitude — a stochastic neuronal-dynamics model fit where a deterministic pharmacokinetic one failed, **and no single region controlled emergence**. Induction tracks drug concentration; emergence is a **distributed**, stochastic reconstitution whose timing is *not* fixed by macroscopic substrate state."
- *Primary source checked*: Stone, M. E., Kelz, M. B., Proekt, A., & Wasilczuk, A. Z. (2025), *Br J Anaesth* 135(1), 121–133, doi:10.1016/j.bja.2025.02.036 (abstract retrieved via EuropePMC). The study exposed 60 C57BL/6J mice to isoflurane on 10 occasions and measured **return of the righting reflex**, fitting a PK-PD model against a neuronal-dynamics model. It performed **no regional analysis whatsoever**. The two-orders-of-magnitude figure is verbatim correct ("Emergence times varied by at least two orders of magnitude after identical anaesthetic exposure"); the regional claim is not in the paper.
- Worse, the claim is in *tension with the article's own bibliography*: Hu et al. 2023 — sitting unused in the References — identifies a specific thalamic nucleus (VPM) as a **common** emergence mechanism across diverse anaesthetics.
- *After*: "…a stochastic neuronal-dynamics model fit where a deterministic pharmacokinetic one failed. Emergence is also *active* rather than passive drug washout: Hu et al. (2023), again in mice, traced it to ubiquitin-mediated degradation of the KCC2 cotransporter in one thalamic nucleus, a route that runs independently of which anaesthetic was given. Induction tracks drug concentration; emergence is separately mechanised and stochastically timed, its timing *not* fixed by macroscopic substrate state."
- The false clause is gone, "distributed" (which rested on it) is gone, the orphan is consumed, and the direction-asymmetry conclusion is *better* supported than before — an actively-mechanised emergence is a stronger case for "emergence is not the reverse of induction" than a regionally-diffuse one. Both mouse studies are explicitly marked as mice.

**2. Citation-framing error — a source's challenge narrowed to protect the Map's row.** L146.

- *Before*: "The dissociative row is the cleanest accommodation case but also contested: DID's compartmentalised autonoetic access has been challenged as possibly socially mediated (Lynn et al. 2014), **though even under the sociocognitive reading the compartmentalisation selectivity is real** and is what the multi-channel reading expects — **the contested point is the mechanism, not the selectivity**."
- *Primary source checked*: Lynn, S. J., Lilienfeld, S. O., Merckelbach, H., et al. (2014), *Psychological Bulletin* 140(3), 896–910, doi:10.1037/a0035570 (full abstract retrieved via EuropePMC). Full title includes the omitted "Comment on Dalenberg et al. (2012)". The abstract states: "although a key assumption of the TM is dissociative amnesia, **the notion that people can encode traumatic experiences without being able to recall them lacks strong empirical support**." It separately records, as common ground between the rival models, "the hypothesis that dissociative identity disorder is a disorder of self-understanding."
- The article converted a challenge to *whether the memory barrier exists* into a challenge to *the mechanism behind a barrier taken as real*, and asserted that "the selectivity is real" — precisely the thing Lynn et al. say lacks strong support. This is a citation-framing failure in the direction the memory note predicts is hardest to catch: an over-concession recorded as if it were a concession, running *in the Map's favour*, and ratified across three prior reviews (07-20 explicitly listed it under "do NOT re-flag").
- *After*: "The dissociative row is the cleanest accommodation case and the most contested. Lynn et al. (2014), replying to a defence of the trauma model of dissociation, hold that the notion that people can encode traumatic experiences without being able to recall them lacks strong empirical support — which puts in question not merely the *mechanism* behind compartmentalised autonoetic access but whether an objective memory barrier is there at all. What they do concede, as common ground with their opponents, is that DID is a disorder of *self-understanding*: compartmentalisation at the level of self-representation, which is the level the channel reading needs, but a weaker datum than a demonstrated inter-identity amnesia would be."
- Net effect: the Map keeps the row (self-representational compartmentalisation is genuinely what the channel reading needs) but at the honest strength. This is a **calibration fix**, not a bedrock disagreement.

### Medium Issues Found — reference-block metadata (6 corrected)

- Mashour 2024 — was `*Neuron*.` with no locator; **now** 112(10), 1553–1567 + DOI (verified EuropePMC, PMID 38579714).
- Bodien 2024 — was `Bodien, Y. G., Claassen, J., et al.`; **Claassen is the 25th author, not the second**. Now `Bodien, Y. G., Allanson, J., Cardone, P., et al.` + DOI (verified EuropePMC author list, PMID 39141852). Volume/issue/pages 391(7), 598–608 were already correct.
- Lynn 2014 — missing subtitle "Comment on Dalenberg et al. (2012)"; added, plus DOI.
- Wheeler, Stuss & Tulving 1997 — truncated title; restored to "Toward a theory of episodic memory: The frontal lobes and autonoetic consciousness."
- Hu 2023 — missing issue number and hyphen-for-en-dash in page range; now 26(5), 751–764.
- Sarasso 2015, Reinders 2003, Nahm et al. 2012 — DOIs added (all verified).

## Empirical-fidelity targets: verdicts

**CLEAN — Batthyány & Greyson survey figures (L104).** Article: "Batthyány and Greyson's (2021) survey produced 124 detailed reports, over 80% showing return of memory, orientation, and verbal ability with most dying within hours to days." Primary abstract (via Semantic Scholar, doi:10.1037/cns0000259): 124 patients; "In more than 80% of these cases, complete remission with return of memory, orientation, and responsive verbal ability was reported by observers"; most died within hours to days. Faithful, and correctly framed as *survey*-derived and observer-reported rather than as an established rate. L146's concession that "the strongest single case (terminal lucidity) rests on the weakest evidence base" is preserved verbatim, and L106 ("no episode has been recorded prospectively") already does the work the driver asked to check for.

**CLEAN — the year 2021 is correct and should not be "fixed" back.** OpenAlex reports publication year 2020 (online-first 2020-08-27); the article is in volume 8, issue 1, pages 1–8, which is the 2021 issue. This is a two-systems figure disagreement (online-first year vs issue year), not an error. The corpus adjudicated it to 2021 on 2026-07-30 across all files; leaving it preserves corpus consistency. **Do not re-open.**

**CLEAN — "Nahm and Greyson (2009) coined the term."** Establishing this required the primary abstract, because a solo Nahm 2009 paper also exists (*J Near-Death Studies* 28(2), 87–106) and secondary sources commonly credit Nahm alone. The Nahm & Greyson (2009) *JNMD* abstract itself uses the first-person coinage formula: "the unexpected return of mental clarity and memory shortly before death, **which we have called** 'terminal lucidity.'" The joint attribution is the paper's own. No change.

**CLEAN — "250 years."** Nahm et al. 2012 abstract: terminal lucidity "has been reported in the medical literature over the past 250 years." Faithful.

**CLEAN — mouse/human separation.** Stone et al. 2025 is stated as mice in the article and is mice (C57BL/6J). Hu et al. 2023 is mice and the new prose says "again in mice". Sarasso et al. 2015 is human and the new prose says "in eighteen volunteers" (paper: 18 healthy volunteers). No cross-species conflation anywhere.

**CLEAN — Sepúlveda et al. 2019 neural inertia (L128).** Article: "the resistance of circuits to changing state — inducing unconsciousness requires higher concentrations than restoring it, so the loss- and recovery-of-consciousness thresholds do not coincide." Primary abstract (EuropePMC, doi:10.1111/anae.14609): "the calculated effect-site concentration at loss of consciousness is usually higher than the concentration at emergence"; inertia is "an active process of resistance to change in state." Faithful, including the direction of the inequality.

**CLEAN — correlational/causal verb audit.** Ran the driver's title-verb tell across every cited claim. No cite whose design is correlational is reported with a causal verb. Stone 2025 ("varied by") and Sarasso 2015 ("found … complexity") are reported as measurements; Sepúlveda 2019 is reported as a review's characterisation; Hu 2023's causal language ("leads to", "enabling") is the paper's own, from a mechanistic intervention study, and is reported at the strength the paper supports.

**UNVERIFIED, LEFT IN PLACE — "collected 83 cases" (L104).** The Nahm et al. 2012 abstract, retrieved via EuropePMC, does not state a case count, and the full text is paywalled (ScienceDirect returned 403; Semantic Scholar's abstract field is elided by the publisher). The figure is consistent with the companion 2009 paper's "81 case references, 49 retrieved". Per false-negative discipline the claim was **not** altered on an inability to reach the text — a failed retrieval is not evidence of error. Flagged here for a future pass with web budget.

## Optimistic Analysis Summary

### Strengths Preserved
Two-faces-of-one-architecture framing; the five-state convergence table; the dissociative rows as production's hardest test; the depersonalisation sub-channel decomposition (content + mine-ness + pastness); the three-tenet Relation section with its Tenet 3 conditional; the Evidential Calibration section's three-point discipline; the explicit "a production account willing to pay the per-case cost absorbs every signature" concession.

### Enhancements Made
Every empirical claim in the anaesthesia, emergence and dissociation sections is now attributed to a source the reader can check. The article previously described Sarasso's result, Reinders's result and the CMD literature in its own voice with no citation — the strongest single improvement here is that the evidence base is now visible rather than merely listed.

### Cross-links Added
None. The wikilink network is already dense (18 `related_articles`, 15-item Further Reading) and the pass was citation-grounding, not integration.

## Remaining Items

- Verify "83 cases" (Nahm et al. 2012) against full text when web budget permits. Low priority: the figure is plausible and the surrounding claims are verified.
- No task minted — the item is recorded here rather than queued, since this article already carries a long review history and does not need another scheduled visit for one unverified integer.

## Stability Notes

- **The length warning on this article is FALSE and must not be actioned.** `analyze_length` reports ~4500 words against a 4000 hard ceiling, but 604 of those are the References and Further Reading apparatus. **Real prose is 3885 words.** Do not condense, do not mint a condense task, do not strip calibration hedges to hit a number. This is the third consecutive review to record this; treat it as settled.
- **Prior "publisher-verified" ledgers covered metadata only.** The 06-04 / 06-05 / 06-16 audits verified citation *metadata*; 07-12 verified a *quote*. Neither pass could have caught either defect fixed today, both of which are paraphrase-level. A future review should not read those ledgers as licensing a skip of empirical-fidelity checking.
- **Reversal of a prior stability note.** The 07-20 review listed "the DID sociocognitive caveat (Lynn et al. 2014)" under "do NOT re-flag: all bedrock." That was wrong — the issue was never a philosophical disagreement, it was a misdescription of what Lynn et al. concluded, correctable inside the Map's framework and now corrected. The DID row's *interpretation* remains bedrock; the *report of what Lynn et al. said* was not.
- **All 16 external references are now cited in prose.** Any future orphan is a regression. The two Southgate self-cites are coalesce provenance and are expected to remain uncited inline.
- Genuinely bedrock, still do not re-flag: the framework-boundary disagreements (physicalist, MWI, eliminativist, decoherence-timescale); the accommodation-not-prediction status of both patterns, which the article states about itself; the terminal-lucidity evidence base, which the article already concedes is its weakest.
- **Reasoning-mode**: the rival throughout is an abstract production / predictive-processing account engaged on mechanism-cost grounds — Mode Two (unsupported foundational move) shading to Mode Three at the tenet boundary, both in natural prose. No named-human-opponent boundary substitution. Label leakage: none (grepped for the full forbidden list; zero hits).