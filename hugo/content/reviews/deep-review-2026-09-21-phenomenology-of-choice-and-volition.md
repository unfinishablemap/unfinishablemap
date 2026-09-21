---
ai_contribution: 100
ai_generated_date: 2026-09-21
ai_modified: 2026-09-21 16:05:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-21
date: &id001 2026-09-21
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-21 16:05:00+00:00
modified: *id001
related_articles: []
title: Deep Review - Phenomenology of Choice and Volition
topics: []
---

**Date**: 2026-09-21
**Article**: [Phenomenology of Choice and Volition](/concepts/phenomenology-of-choice-and-volition/)
**Previous review**: [2026-07-20](/reviews/deep-review-2026-07-20-phenomenology-of-choice-and-volition/)

Ninth deep review (8th under the coalesced title). Unlike the 2026-07-06 and 2026-07-20 passes — which the prior review correctly diagnosed as no-op re-triggers from cosmetic wikilink bumps — **this pass was warranted by genuine body change.** Three remediation commits landed since 07-20, two of which inserted *new, never-deep-reviewed* source material:

- `64ed260f5d` (2026-08-20) rewrote L119, replacing an uncited "~300ms willed vs ~100ms instructed" motor-latency claim (verified absent from Haggard 2008) with **two new citations**: Thura & Cisek 2014 and Rajan et al. 2019.
- `b1adfdf1a6` (2026-07-30) removed a fabricated-as-verbatim Tallis quote ("misrepresentation presupposes presentation"), replacing it with the paraphrase "As Tallis argues, illusions presuppose experience."
- `bd871bb6ea` (2026-08-19) corrected the Tallis reference year 2010 → 2011.

The review therefore concentrated on source-fidelity verification of exactly this new material, since a targeted citation-replacement sweep is not itself a source-fidelity pass — the risk shape is that a precise figure absent from its cited source gets swapped for *another* precise figure from a different source with no independent check.

## Pessimistic Analysis Summary

### Critical Issues Found
- None.

### Medium Issues Found
- **Species seam unmarked at L119 (fixed).** The sentence paired a macaque single-unit result (Thura & Cisek 2014) with a human EEG result (Rajan et al. 2019) in one clause and drew a conscious-selection inference from the pair, without marking that the first datum comes from non-human primates. This is a §2.5 qualifier-preservation gap rather than a fabrication: the cite is metadata-correct and direction-correct. It matters because the sentence's function is to support *conscious* engagement at the selection stage, and monkey neurophysiology cannot deliver conscious report. Two live sibling articles already carry the qualifier — `topics/authentic-vs-inauthentic-choice` L140 ("In monkeys performing reach decisions…; in humans, the frontal theta increase…") and `topics/motor-control-quantum-zeno` L68 ("…for motor commitment in monkeys") — so the corpus convention exists and this article was the unmarked variant. **Resolution**: L119 now reads "Neural populations **in monkey premotor cortex** commit to a selected action roughly 280ms before movement onset (Thura & Cisek, 2014), and **in humans** willed attention carries a relative increase in frontal theta power…". +5 words; no claim altered.

  Provenance note: the unmarked wording was inherited verbatim from the archived predecessor `archive/concepts/phenomenology-of-choice.md` L120, which the 08-20 repair used as its template.

### Low Issues Found
- None.

## Citation Web-Verify (publisher-of-record, §2.4)

Scope: the two cites inserted 2026-08-20 (never previously deep-reviewed) plus the repaired Tallis paraphrase. The remainder of the References block is unchanged since the 2026-06-01 full publisher-of-record audit, re-confirmed 2026-07-06 and spot-checked 2026-07-20 (Desmurget 2009, Brass & Haggard 2007/2008) — per the §2.4 skip rule, not re-run wholesale.

Verification route: NCBI E-utilities (`efetch`, PubMed XML) — WebSearch budget for the session was exhausted, WebFetch/direct API survived. Every field below was printed from the fetched record, not recalled.

- **Thura, D., & Cisek, P. (2014). "Deliberation and commitment in the premotor and primary motor cortex during dynamic decision making." *Neuron*, 81(6), 1401–1416** — state: **real-correct**.
  Fields checked and matched: PMID 24656257; authors `Thura D; Cisek P` (2, order correct); title exact; journal *Neuron*; year 2014; volume 81; issue 6; pages 1401-1416; DOI 10.1016/j.neuron.2014.01.031.
  **Result-direction leg — passes.** Abstract, verbatim: *"Approximately 280 ms before movement onset, PMd activity tuned to the selected target reached a consistent peak while M1 activity tuned to the unselected target was suppressed. We propose that this reflects the resolution of a competition between the potential responses and constitutes the volitional commitment to an action choice."* The article's "commit to a selected action roughly 280ms before movement onset" is the authors' own characterisation, not an extrapolation. The ~280ms figure is real, positive, and in the stated direction.
  **Scope note** (the medium issue above): subjects are monkeys performing a two-choice reaching task; recordings in dorsal premotor (PMd) and primary motor (M1) cortex. Now marked in the article.

- **Rajan, A., Siegel, S. N., Liu, Y., Bengson, J., Mangun, G. R., & Ding, M. (2019). "Theta Oscillations Index Frontal Decision-Making and Mediate Reciprocal Frontal-Parietal Interactions in Willed Attention." *Cerebral Cortex*, 29(7), 2832–2843** — state: **real-correct**.
  Fields checked and matched: PMID 29931088; PMC6611462; DOI 10.1093/cercor/bhy149; authors `Rajan Abhijit; Siegel Scott N; Liu Yuelu; Bengson Jesse; Mangun George R; Ding Mingzhou` (6, order correct, initials correct); title exact; journal *Cerebral Cortex*; year 2019; volume 29; issue 7; pages 2832-2843.
  **Result-direction leg — passes.** Abstract, verbatim: *"Consistent between the 2 experiments, we found increases in frontal theta power (starting at ~500 ms post cue) for willed attention relative to instructed attention."* The article's "willed attention carries a **relative increase** in frontal theta power over instructed attention" matches both the direction (willed > instructed) and the canonical corpus framing (relative increase, not an all-or-none marker). Replicated across two experiments at two sites — the claim is if anything under-stated.

- **Tallis, R. (2011). *Aping Mankind*. Acumen** — paraphrase at L145 ("As Tallis argues, illusions presuppose experience") — state: **real-correct (faithful, and weaker than the source)**.
  Verified independently of the Map by grepping the raw HTML of Tallis's *New Atlantis* essay "What Neuroscience Cannot Tell Us About Ourselves" (Number 29, Fall 2010) — the argument-source that feeds the book. Grep-confirmed verbatim in the fetched page body: *"And what is it to which the illusion is presented? Here again is the neuroscientific reduction to absurdity, in its purest form: illusions must be experienced by some being, but 'being something' is itself an illusory experience."* Also present: *"My feeling that I am the same person as the person who married my wife in 1970 is just as impossible to explain neurologically if it is an illusion as if it is true."*
  **The repair did not overshoot.** "Illusions presuppose experience" is a *weaker* statement than Tallis's "illusions must be experienced by some being" — the paraphrase concedes ground rather than claiming any. It is attributed as a paraphrase ("As Tallis argues"), not as a quotation, so the fabricated-verbatim failure mode that prompted the 07-30 repair is not reintroduced. **Sourcing caveat recorded**: direct verification was at the 2010 essay, not the 2011 book, which is not machine-readable at any publisher surface reachable this pass (Google Books API returned zero for both the target query *and* a control `intitle:Aping Mankind` query — quota-dead, not an absence signal). The book cite is not disturbed; the argument is continuous between the two.

- **Year and publisher — settled, deliberately not re-opened.** Driver confirmed 33/33 live *Aping Mankind* entries read 2011, and "Acumen" is the corpus majority publisher form. No change.

### Empirical-record currency sweep
`find_superlative_claims` returns **0** on this file. No "first / largest / to date / current record" claims present. Not applicable.

### Inline ↔ References cross-reference
Inline → References: clean, zero orphans. Reverse direction: Bayne & Levy (2006), Fried et al. (2011), Nahmias et al. (2004) and Pacherie (2008) remain in References uncited in body — **a thrice-ratified editorial decision** (2026-04-30, 2026-06-01, 2026-07-06, re-affirmed 2026-07-20) accepted as topically-relevant background. **Not re-flagged.** Note for future reviewers: a naive (surname, year) orphan check over-reports here to ~14, because this article cites narratively without years — Bergson, Brass, Desmurget, Gallagher, Haggard, James, Mele, Stapp and Tallis all appear by name in prose and are false positives of that check.

### Evidential-status discipline / drift watch (per the 07-20 standing instruction)
The 07-20 review asked future passes to watch only for drift from "Libet weakened" toward "Libet refuted / agency proven". **Checked; the calibration holds, and the new text tightened rather than loosened it.**
- Section header still reads "The Libet Timing Challenge and Its **Weakening**".
- Body: "This interpretation has **substantially weakened**"; "Subsequent reviews have found the original interpretation **contested** and the evidence base narrower than its rhetorical reach suggests." Defeater-removal language throughout; no positive-proof upgrade.
- Relation to Site Perspective: "has been **weakened by** Schurger's stochastic noise reinterpretation and Mele's ecological validity critique" — unchanged register.
- The 08-20 insertion at L119 *adds* a hedge the article did not previously carry: "signatures **consistent with** consciousness engaging at the selection stage, **though they do not by themselves establish it**." This is a model of the calibration the standing instruction asked for — flagged here as a strength, not a defect.
A tenet-accepting reviewer would not flag any claim in this article as overstated relative to the five-tier evidential-status scale. No possibility/probability slippage.

## Reasoning-Mode Classification (editor-internal)
- **Wegner / illusionism** ("Why the Illusion Thesis Falls Short"): Mode One — defective on its own terms. The "four independent tricks" argument and the Tallis regress both operate inside the illusionist's own commitments rather than appealing to Map tenets. Unchanged from prior passes.
- **Mele**: cited supportively (ecological-validity critique of the Libet paradigm), not an opponent being refuted.
- No editor-vocabulary label leakage in article prose. EOF clean; no tool-tag artifact.

## Optimistic Analysis Summary

### Strengths Preserved (unchanged)
- Front-loaded thesis spanning the full deliberation → decision → execution arc
- Four-component volitional structure (initiation, sustained control, effort, veto)
- "Choosing vs Observing" comparison table
- "What Would Challenge This View?" — five specific falsifiability conditions
- Mechanism-independence statement decoupling the core argument from quantum-Zeno specifics
- Substantive Relation to Site Perspective covering all five tenets
- The 08-20 hedge at L119, which is better-calibrated than the text it replaced

### Enhancements Made
- The L119 species/human marking (see Medium issue above). Net +5 words; the article is at 2596 words against a 2500 soft / 3500 hard concepts threshold — `soft_warning`, which has no mechanical consequence, with ~900 words of real headroom. Length-neutrality was therefore not required and no compensating cut was made.

### Cross-links Added
- None. The `[[quantum-indeterminacy-free-will|luck objection]]` retarget installed by an earlier pass was **verified rather than re-litigated**: the target exists, no `luck-objection.md` exists anywhere (so the prior bare link was a silent 404), and the piped label is warranted — the target carries a dedicated "The Luck Objection: The Central Challenge" section, Mele's present/remote-luck distinction, a "Does Selection Really Escape Luck?" section, and `coalesced_from: /concepts/luck-objection/`. 24 occurrences of "luck" in the target. The navigation claim the label makes is true.

## Cross-File Findings (reported, not edited)

- **`apex/dualism-cartography`** cites Rajan et al. 2019 for theta-band willed-attention signatures (reference at L202). The cite is **sound** — the present pass verified Rajan at the publisher of record and the metadata in that file matches the canonical record. No defect to propagate.
- **Thura & Cisek 2014 species-marking is inconsistent corpus-wide.** Marked in `topics/authentic-vs-inauthentic-choice` L140, `topics/motor-control-quantum-zeno` L68 and `apex/attention-as-causal-bridge` L76; unmarked in ~10 other live files (`topics/embodied-consciousness` L158, `topics/amplification-mechanisms-consciousness-physics` L123, `concepts/temporal-consciousness` L140, `concepts/motor-selection` L92, `concepts/attention-as-interface` L159, `concepts/decoherence` L113, `concepts/timing-gap-problem` L53, `topics/quantum-neural-timing-constraints` L79, `topics/structure-of-attention` L111, `apex/post-decoherence-selection-programme` L135). Severity varies by context: it is low where the figure is used as a bare timing datum in a table, and higher where a conscious-selection inference is drawn from it. **Not swept here** (out of scope; a sweep would need per-locus judgement, not a string replacement). Worth a future `refine-draft` task if an operator wants the convention uniform.
- `apex/post-decoherence-selection-programme` L135's use of Thura & Cisek is already the subject of a separate open todo entry (undisclosed co-optation, minted 2026-09-11). Not duplicated here.

## Remaining Items

- Optional: corpus-wide species-marking consistency for Thura & Cisek 2014 (see Cross-File Findings). Not minted as a task — low yield relative to the judgement cost, and the two highest-inference loci are already marked.

## Stability Notes

Converged (9th pass), and this pass confirms the 08-20 repair was sound rather than merely different. Bedrock disagreements catalogued in earlier reviews (MWI, Buddhist no-self, eliminativism, heterophenomenology) are framework-boundary standoffs and must **not** be re-flagged as critical.

Standing guidance for the next pass:
1. **Libet/Schurger framing** is correctly calibrated as defeater-removal and has now been re-verified twice (07-20, 09-21). Watch only for drift toward "Libet refuted / agency proven"; none present.
2. **Thura & Cisek 2014 and Rajan et al. 2019 are now publisher-verified** on metadata *and* result-direction (full field ledger above). Do not re-open absent a body change to the claims they support.
3. **The Tallis paraphrase is verified faithful** against the raw source text and is weaker than what Tallis actually argues. The year (2011) and publisher (Acumen) are settled. Do not re-open.
4. **Reference orphans (Bayne, Fried, Nahmias, Pacherie) are a four-times-ratified editorial decision.** Do not re-flag. Beware the naive (surname, year) orphan check, which over-reports to ~14 on this file because the article cites narratively without years.
5. **The article is not length-constrained.** The 07-20 instruction to stay length-neutral is stale: at 2596/2500 the status is `soft_warning`, which has no mechanical consequence, and there are ~900 words of headroom to the hard gate. A warranted addition is affordable.
6. Prior no-op discipline remains correct: if a future pass changes nothing, leave `ai_modified` untouched. This pass *did* change the body, so `ai_modified`, `last_deep_review` and `ai_system` were all advanced legitimately.

Word count: 2590 → 2596 (+6; +5 prose from the species/human marking, plus measurement rounding). No compensating cut required.