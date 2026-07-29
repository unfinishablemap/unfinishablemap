---
title: "Deep Review - Cetacean and Corvid Consciousness as Amplification Test Cases"
created: 2026-07-29
modified: 2026-07-29
human_modified: null
ai_modified: 2026-07-29T18:07:34+00:00
draft: false
description: "Publisher-of-record verification of the five citations added by the 2026-07-28 literature-drift audit; two defects fixed — a mis-framed Taylor & Jelbert cite and an overstated Vanhooland finding."
topics: []
concepts: []
related_articles:
  - "[[cetacean-and-corvid-consciousness]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-07-29
last_curated: null
---

**Date**: 2026-07-29
**Article**: [[cetacean-and-corvid-consciousness|Cetacean and Corvid Consciousness as Amplification Test Cases]]
**Previous review**: [[deep-review-2026-07-11-cetacean-and-corvid-consciousness|2026-07-11]] (orthogonal-lens settle pass, clean)
**Prior reviews total**: 8

## Purpose of this pass

The 2026-07-11 stability note said: *"Do NOT re-run the full publisher-of-record sweep absent newly-added citations."* Citations **were** newly added. The 2026-07-28 literature-drift audit (commit `02bc0ec6c`) rewrote the Mirror Self-Recognition section and added **five** references — Boeckle et al. 2020, Connor et al. 2022, Soler et al. 2020, Taylor & Jelbert 2020, Vanhooland et al. 2023 — none of which had been checked by any review. That newly-added citation surface is the entire scope of this pass, and it is exactly the re-open condition the previous review named.

The eighteen pre-existing citations were **not** re-swept: they were publisher-of-record verified 2026-06-02, and two currency-sensitive ones independently re-verified 2026-07-11. Re-sweeping them would be the oscillation the convergence discipline forbids.

## Publisher-of-Record Citation Ledger (§2.4) — five new cites

Verification route: DOI resolution confirmed at the registrar for all five, then metadata and abstracts retrieved via Europe PMC's publisher-deposited records (the publishers' own sites returned 403 to automated fetch). Gutfreund re-verified at the Frontiers full text directly. No verification was taken from an aggregator, from a prior Map review, or from any search result surfacing unfinishablemap.org.

- **Boeckle, M., Schiestl, M., Frohnwieser, A., Gruber, R., Miller, R., Suddendorf, T., Gray, R.D., Taylor, A.H. & Clayton, N.S. (2020). New Caledonian crows plan for specific future tool use. *Proc. R. Soc. B* 287(1938), 20201490** — state: **real-correct**. Author list, order, volume, issue and article number all match exactly. *Empirical fidelity*: the article's paraphrase ("shown a baited apparatus and then offered a choice of objects selected the tool required for that specific future task, passing over tools that had been useful previously") matches the abstract's "the crows chose the right tool for the right future task, while ignoring previously useful tools and a low-value food item." Clean.
- **Connor, R.C., Krützen, M., Allen, S.J., Sherwin, W.B. & King, S.L. (2022). Strategic intergroup alliances increase access to a contested resource in male bottlenose dolphins. *PNAS* 119(36), e2121723119** — state: **real-correct**. *Empirical fidelity*: three claims checked, all supported, one only by going to the full text. (a) "three-tiered alliance network" — abstract: "form three alliance levels, or 'orders'." (b) "cooperative relationships *between* second-order alliances, rather than alliance size, predict access to contested females" — the **abstract alone** says connectedness with third-order allies matters "independently of the effect of their second-order alliance connections," which reads as a connections-vs-connections contrast and made "rather than alliance size" look like a substitution error. The **full text settles it in the article's favour**: "second-order alliance size did not significantly predict consortship rate…or consortship duration," "third-order alliance size did not significantly predict…," and "alliance size had no effect on either response variable." The article's gloss is correct; the apparent defect was an artefact of reading the abstract only. (c) "on the authors' reading a plausible selection pressure for enhanced social cognition" — supported: the paper states "Increasing the number of alliance levels will also increase the cognitive demands of alliance formation" and invokes "the 'social brain' hypothesis for the evolution of large brains and intelligence." (d) Superlative check: article says "the largest known multilevel alliance network outside humans"; source says "the largest nonhuman alliance network known" — the article's form is if anything narrower. No currency drift. Clean.
- **Soler, M., Colmenero, J.M., Pérez-Contreras, T. & Peralta-Sánchez, J.M. (2020). Replication of the mirror mark test experiment in the magpie (*Pica pica*) does not provide evidence of self-recognition. *J. Comp. Psychol.* 134(4), 363–371** — state: **real-correct**. *Empirical fidelity*: the article's striking detail — "during the mark test, self-directed behaviour proved *more* frequent in front of the cardboard control than in front of the mirror" — is a near-verbatim rendering of the source's own sentence ("self-directed behavior proved more frequent in front of the cardboard than in the mirror"). Larger sample: confirmed. Authors' conclusion that further replication is needed: confirmed. Clean. *Noted, not changed*: the source also found more social and self-directed behaviour before mirrors than cardboard during the **exposure** phase; the article's sentence is explicitly scoped to the mark test, so no correction is owed.
- **Taylor, A.H. & Jelbert, S. (2020). The crow in the room: New Caledonian crows offer insight into the necessary and sufficient conditions for cumulative cultural evolution. *Behavioral and Brain Sciences* 43, e178** — state: **real-correct metadata, MIS-FRAMED in body (fixed)**. See Critical Issue 1.
- **Vanhooland, L.-C., Szabó, A., Bugnyar, T. & Massen, J.J.M. (2023). A comparative study of mirror self-recognition in three corvid species. *Animal Cognition* 26(1), 229–248** — state: **real-correct metadata, empirical claim OVERSTATED (fixed)**. See Critical Issue 2.

Re-verified independently at the primary source (not from the prior review's ledger):

- **Gutfreund, Y. (2024). Neuroscience of animal consciousness: still agnostic after all. *Frontiers in Psychology* 15, 1456403** — state: **real-correct, quote faithful**. Fetched the Frontiers full text. Source sentence: *"Hence, a perceptual decision without a felt subjective experience (David et al., 2011) is a possibility that is equally consistent with the data and cannot be disregarded."* The article quotes the clause up to "…consistent with the data." — a meaning-preserving prefix ending at a clean clause boundary; the omitted continuation strengthens rather than weakens Gutfreund's point. Confirms the 2026-07-11 verdict by an independent route. The References entry was **incomplete** (no volume, no article number, no DOI, unlike every other entry) — completed as part of this pass.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Citation framing error — Taylor & Jelbert 2020 cited on the wrong side of the question they answer.** The body read: *"Whether New Caledonian crow tool traditions genuinely accumulate innovations or merely persist through social learning is the contested step—sharpened by the observation that these crows do not appear to imitate, so any ratchet would have to run through a mechanism such as mental template matching rather than copying (Taylor & Jelbert 2020)."* Two problems. **(a)** Taylor & Jelbert's actual published position is the affirmative one: their abstract states NC crow tools "show suggestive evidence of cumulative change" and "therefore, appear to be the product of cumulative technological culture (CTC)." Appending them to a clause about accumulation being doubtful reads as though the cited authors sharpen the doubt, when they are on the other side of it — the "real, verbatim, yet mis-framed" defect class. **(b)** The specific propositions attributed to them (crows "do not appear to imitate"; "mental template matching") appear nowhere in the commentary's abstract; mental template matching is the finding of a *different* paper (Jelbert et al. 2018, *Scientific Reports*), and I could not confirm either proposition in the commentary's body. **Resolution**: re-framed to state what the source actually argues — "Taylor and Jelbert (2020) read the designs as showing suggestive evidence of cumulative change and argue the crows are a useful test case for which conditions are necessary and sufficient for cumulative culture to emerge at all." Every element is verbatim-traceable to the verified abstract. The unverifiable mechanism attribution is gone. Per discipline the cite was **re-framed, not deleted**.

2. **Empirical-claim overstatement — Vanhooland et al. 2023 reported as having established what they raised as a question.** The body said the study "traced the divergent corvid results partly to methodological heterogeneity rather than phylogeny." The source does no such tracing: it says the divergence in methodologies "calls into question whether the observed differences are in fact phylogenetic or methodological," and closes by advocating "for consistent methodologies and procedures." Posing an open question is not attributing a cause. **Resolution**: rewritten to "questioned whether the divergent corvid results reflect phylogeny at all rather than the widely varying protocols used." Secondary fix in the same sentence: "found no mark-directed behaviour indicative of self-recognition" → "found no mark-test evidence of self-recognition," because the source *does* report interspecies differences in mark-test behaviour; what it denies is their evidential import ("the performances of these species in the Mark Test do not provide any evidence for their ability of self-recognition"). Species list ("common ravens, carrion crows, azure-winged magpies") verified correct.

3. **Corpus propagation — a sibling still asserted the superseded claim.** Grep of live sections for MSR claims found one downstream locus outside the target: `concepts/self-and-self-consciousness.md` L159 listed "mirror self-recognition: great apes, elephants, dolphins, some corvids" as settled comparative fact. After the magpie replication failure and three further negative corvid species, that parenthetical ratified as fact what the hub article now flags as contested. **Resolution**: calibrated in place to "and — contested since the magpie replication failure — some corvids." Minimal, non-retracting; the file's `last_deep_review` was **not** touched (it was not reviewed, only calibrated).

### Medium Issues Found

- **Table row imprecision.** "Mirror self-recognition | … | Contested (unreplicated)" understated the record: the magpie result has not merely gone unreplicated, a close replication was attempted and failed. Changed to "Contested (failed replication)," which also matches the section prose.
- **Incomplete reference entry.** Gutfreund 2024 lacked volume/article number/DOI while all eighteen other entries carry full metadata. Completed with the details verified at Frontiers.
- **Redundancy introduced by the 2026-07-28 edit.** The MSR section closed with "The replication record sharpens the existing hedge rather than removing a support," which restated the immediately preceding sentence ("Neither development costs the amplification argument a premise, which never rested on magpie MSR"). Cut — this paid for the additions above.

### Counterarguments Considered

- Bedrock disagreements carried forward from prior reviews (materialist sufficiency claim, MWI branch-relative selection, epiphenomenalist convergent-emergence) were re-checked and remain honestly marked. Not re-flagged.

## Optimistic Analysis Summary

### Strengths Preserved

- The lead's evidential calibration is unchanged and remains exemplary: cetaceans/corvids at *realistic possibility, contested*, the amplification hypothesis at *live hypothesis*, and the explicit "The Map's tenets remove a defeater … they do not, by themselves, raise evidence-grade."
- The 2026-07-28 MSR rewrite deserves credit for a hard thing done well: it downgraded a datum the article had been leaning on and then said plainly that the argument never rested on it. The Hardline Empiricist reads this as tenet-as-evidence-upgrade correctly declined.
- The Standing Agnostic Challenge section remains the article's calibration spine, explicitly scoping every species-claim.

### Enhancements Made

- Three citations now state what their sources actually found rather than what the surrounding argument wanted them to say.

### Cross-links Added

None — the article's link surface is already dense and length headroom is thin.

## Length

3782 words before, 3782 after (hard threshold 4000, `soft_warning`). Deliberately net-neutral: the three additions were paid for by cutting the redundant closing sentence. Note that this count includes ~41 lines of reference apparatus; the argument prose sits comfortably below the ceiling and this article should **not** be routed to `/condense` on the raw figure.

## Reasoning-mode classifications (editor-internal, carried forward unchanged)

- Materialist convergent-computation / Neural Architecture Challenge — Mixed (foundational-move identification of the computation→phenomenal-seeming bridge, opened with honest boundary-marking of the sufficiency claim).
- Epiphenomenalism (James 1890 convergent-emergence reply) — Mode Three; deferred to the separate evolutionary-case argument.
- MWI defender (branch-relative selection) — Mode Three; bedrock disagreement explicitly marked.

No label leakage in prose (§2.6 re-checked).

## Remaining Items

- **`research/animal-consciousness-2026-01-14.md`** (L94, L96, L211) and **`research/animal-consciousness-2024-2025-literature-2026-05-19.md`** (L103) still record magpie MSR as a clean 2008 pass. These are **dated research snapshots**, and the Map's convention is that research notes record the literature as understood at the note's date — so this is arguably correct-as-archive rather than drift. Flagged for the operator rather than edited: if research notes are meant to track current consensus, both need a one-line 2020/2023 addendum.
- Taylor & Jelbert 2020 body text was not obtainable (Cambridge Core paywalled; no preprint on the Bristol repository page). The re-framed sentence is grounded entirely in the verified abstract, so nothing now rests on the unobtainable body — but if the commentary is ever accessed, the imitation / mental-template point could be restored **with a Jelbert et al. 2018 citation of its own**.

## Stability Notes

- The 2026-07-11 note held: the article was stable, and the only thing that re-opened it was newly-added citations. That re-open condition fired exactly as designed, and it caught two real defects in day-old content. **The general lesson: freshly-added citations are the highest-risk surface in an otherwise converged article, and a settle-pass verdict does not transfer to them.**
- All five 2026-07-28 citations are now publisher-of-record verified. **Do NOT re-sweep** the eighteen older citations (verified 2026-06-02, spot re-verified 2026-07-11) or these five, absent further additions.
- The Connor et al. 2022 case is worth remembering as an **anti-pattern for premature reversion**: the abstract alone made a correct paraphrase look like a substitution error ("alliance size" vs "second-order alliance connections"), and only the full text showed the article was right. Abstract-only reading would have introduced a defect while claiming to fix one.
- Corvid MSR is now correctly registered as contested across the corpus. Do not "restore" magpie MSR as a settled datum on the strength of Prior et al. 2008 alone.
- Bedrock disagreements remain explicitly marked and must NOT be re-flagged as critical: eliminative-materialist sufficiency claim, MWI branch-relative-selection counter, epiphenomenalist convergent-emergence reply.
- `ai_system` **held** at `claude-opus-4-6+claude-opus-5`. This pass was calibration and citation re-framing, not re-authoring; per the attribution discipline the existing value stands.
