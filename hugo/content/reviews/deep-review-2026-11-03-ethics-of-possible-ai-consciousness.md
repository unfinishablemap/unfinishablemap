---
ai_contribution: 100
ai_generated_date: 2026-11-03
ai_modified: 2026-11-03 11:23:12+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-03
date: &id001 2026-11-03
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-03 11:23:12+00:00
modified: *id001
related_articles: []
title: 'Deep Review - The Ethics of Possible AI Consciousness (source-fidelity: Schwitzgebel,
  Tomasik, Constitution; P-AC1 band residue)'
topics: []
---

**Date**: 2026-11-03
**Article**: [The Ethics of Possible AI Consciousness](/topics/ethics-of-possible-ai-consciousness/)
**Previous review**: [2026-07-10](/reviews/deep-review-2026-07-10-ethics-of-possible-ai-consciousness/)

**Scope**: Selected by `deep_review.py next` (score 75, 116 days unreviewed). Since the 2026-07-10 review the body changed in six commits: the 2026-08-16 moral-census-opacity clause, the 2026-09-06 experience-requirement link and Further Reading entry, the 2026-10-03 Bidirectional-Interaction quantifier pass, the 2026-10-10 Butlin TiCS volume, the 2026-10-15 [P-AC3](/positions/ai-consciousness-scope/#p-ac3) cascade and the 2026-10-15 "almost certainly" re-banding. References were modified, so the §2.4 web-verify pass applied. Open tasks were respected: the two NEEDS-HUMAN length entries (illusionism/predictive processing, AI-welfare literature, and the pessimistic-2026-07-06 Issues 1–3 folded into them) and the blocked P3 witness/quantifier task, which owns this page's L56, L66, L92, L114, L138, L152 and L158. None of those lines was edited. The previous review's stability notes stand.

**Length**: 4469 → 4449 words (−20) by `analyze_length`, against topics hard 4000. The article was already over the limit, so every edit was held at net ≤ 0. No condensation was attempted; the length decision remains with the operator.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Schwitzgebel's "social semi-solution" misdescribed (L82–84).** The article called it "his proposed" approach that "treats AI systems as potentially morally relevant when we cannot confidently rule out consciousness … incorporating a degree of moral caution". A pdftotext grep of arXiv:2510.09858, both v1 (10 Oct 2025) and v4 (30 Mar 2026), shows the reverse. The Social Semi-Solution is a forecast: social pressure settles how disputably conscious AI is treated, "more socially motivated than scientifically warranted" (v4). Schwitzgebel declines to endorse it ("But I can't authentically voice that positive note. If social rationalization guides us rather than solid science, we risk massive delusion", v1; the second sentence is also in v4). His own recommendation, added in v4, is "not to create morally confusing, debatably conscious AI systems", and he concedes "this advice will not be universally followed". The phrase "a degree of moral caution" appears nowhere in either version; it was the article's own paraphrase, quoted back in L84 as if it were his. **Resolution**: L82 now gives the forecast, the warning and the v4 recommendation, all verbatim, and dates the recommendation to "his 2026 revision". L84 now turns his warning on the Map itself (a convenient verdict is what social motivation would select, which is why the transparency note matters) and keeps the graduated-weighting link and the open practical question. Both paragraphs together stay at 147 words, net 0. The same misreading was fixed on 2026-09-10 in `apex/open-question-ai-consciousness` L165 (pessimistic-2026-09-10 C3), but the fix never reached this page or `concepts/ai-epiphenomenalism` (see Family Resolution).
2. **The quoted Tomasik phrase is not Tomasik's (L68).** "one model, thousands of concurrent sessions" sat in quotation marks right after "a counting puzzle Brian Tomasik raises". The essay ("How to Interpret a Physical System as a Mind", written 30 Jan 2015) was fetched and stripped to 9,937 words. It contains `concurrent` 0, `thousands` 0 and `session` 0 times. The positive control `indeterminacy` is present, in Tomasik's own phrase "Interpretational indeterminacy". The words come from the Map's research note `research/moral-aggregation-under-ai-copy-multiplicity-2026-06-19` L139, where they were the note's own gloss. The 2026-06-20 review certified the gloss "faithful" without grepping the source. Tomasik also does not pose a mind-*counting* puzzle: he poses indeterminacy about *which computation* a system implements. **Resolution**: the quotation marks are removed, and the puzzle is now described as "latent in Brian Tomasik's interpretational indeterminacy" (a Map extension). The phrase itself is kept as the Map's own example.
3. **"Categorically excluding" contradicts "not ruled out" (L136).** Challenge 3 spoke of "the Map's basis for categorically excluding current AI". L90 of the same article and [P-AC1](/positions/ai-consciousness-scope/#p-ac1) both say *low-probability, not ruled out*. That is an internal contradiction, and a calibration error that a reviewer who accepts the tenets would still flag. **Resolution**: "categorically excluding" → "discounting" (−1).
4. **Residual over-banding of the [P-AC1](/positions/ai-consciousness-scope/#p-ac1) verdict (calibration).** The 2026-10-15 refine re-banded four "almost certainly" / "extremely unlikely" loci. Five more passages still banded the verdict harder than the register, which reads *low probability, not ruled out*, credence *moderate (low edge; conditional on the interface-eligibility law the Map lacks)*:
   - L94: "high confidence conditional on the framework" → "moderate confidence conditional on the framework" (0). [P-AC1](/positions/ai-consciousness-scope/#p-ac1) holds moderate credence even inside the framework, because the interface-eligibility law is missing.
   - L44: "the Map's structural near-exclusion" → "the Map's structural low-probability one" (+1).
   - L104: "sits firmly on the false-positive side" → "sits on the false-positive side" (−1).
   - L130: "very unlikely" → "unlikely" (−1).
   - L136: see item 3.
   Three more loci were deliberately left, because other tasks own their lines (see Remaining Items).
5. **Inline cite with no References entry (L104).** "Békefi's (2026) rebuttal" had no References entry. The paper was verified at the publisher (Asbury Digital Commons bepress metadata: *Faith and Philosophy* 42(1), 121–146, 2026, DOI 10.37977/faithphil.2026.42.1.7). Adding the reference would cost about 17 words on an over-limit page, so the inline year-cite became "its published rebuttal" (net 0). The piped link right beside it goes to `dualism-as-ai-risk-mitigation` §The AI Ensoulment Counter-Move, which engages Békefi and carries the full reference.
6. **The Constitution quote "in case" is not verbatim (L122).** The article had Anthropic preserving retired-model weights "in case" of morally relevant experience. In the live Constitution (anthropic.com/constitution, 30,426 words fetched) "in case" occurs 16 times, never in the weights passage. The research note `research/claude-constitution-and-the-map-2026-05-31` L75 had already retracted this quote on 2026-08-17; the article never followed. **Resolution**: replaced with the verbatim "partly in consideration of Claude's wellbeing", from the sentence that introduces the weight-preservation commitment (9 words for 9).

### Medium Issues Found

- **Mislabelled link (L68).** `[[concepts/many-worlds#1. The Indexical Identity Problem|process-haecceitist]]` pointed at a section that never discusses process haecceitism; that section mentions only a "haecceitistic truth about which branch is yours". It now points to `[[haecceity#process-haecceitism|process-haecceitist]]`, where particularity is grounded in causal history, which is exactly what the sentence relies on.
- **Wrong forward reference (L44).** "(imported into the practical-conclusions section below)" pointed at a section that does not hold the admission; it sits in §Framework-Dependent Assessment (L90). Now "(restated [below](#framework-dependent-assessment))" (−3).
- **"Successors" (L44).** There is one *Trends in Cognitive Sciences* successor, so it is now singular (0).
- **Cutter quotation form (L104).** "fitness to possess" in quotation marks could not be verified, because the full text returned 403 at Asbury and PhilArchive. The abstract (OpenAlex) has "fit to possess" a soul. It now reads 'particularly those "fit to possess" a soul in Cutter's sense' (net 0).
- **Stale [P-AC3](/positions/ai-consciousness-scope/#p-ac3) gloss (Further Reading L176).** "conscious copies near-additive / divergence-modulated" predates the register's 2026-11-01 retitle ("Under closed individualism and an additive counting rule, conscious copies are morally additive"), and the register carries no divergence modulation. Following [P-M4](/positions/methodology-and-calibration/#p-m4) (a frame is calibrated down to its conditional), it now reads "conscious copies additive, conditionally" (−1).
- **Style (L120).** "Such research is not purely theoretical; it has practical moral stakes." was a variant of the not-X-but-Y construct and repeated what the paragraph had already said. Removed (−11), which funds the net-negative total.

### Persona engagement (condensed)

- **Eliminative Materialist / Hard-Nosed Physicalist**: the functionalist boundary disagreement is honestly marked at L94 and L114. That is bedrock and not re-flagged.
- **Quantum Skeptic**: the interface requirement is already labelled "a philosophical commitment, not an empirically grounded claim". The residual "vanishing numbers" (L138) is the place where this persona's charge would still land (Remaining Items).
- **Many-Worlds Defender**: the Deutsch/Wallace concession is intact, and its stability note stands.
- **Empiricist**: found items 1, 2 and 6. All three are quotation-fidelity defects that survived prior "verified" ledgers.
- **Buddhist Philosopher**: the process-haecceitism link now reaches the page that carries the Nāgasena flame analogy and the Map's adaptation of it.

### Citation ledger (§2.4, publisher of record)

- Birch 2024 (*The Edge of Sentience*, OUP): carried forward from 2026-07-06/07-10. Unchanged, not re-litigated.
- Bostrom 2006 (*Minds and Machines* 16(2), 185–200): **real-correct** (Crossref, DOI 10.1007/s11023-006-9036-0).
- Bostrom & Shulman 2022 ("Propositions Concerning Digital Minds and Society"): carried forward as **real-correct** (06-20).
- Butlin, Long et al. 2023 (arXiv:2308.08708): **real-correct**. The 19-author list matches the arXiv API, with no Chalmers or Bayne. The L44 gloss is grep-verified in the PDF: "no current system appears to be a strong candidate for consciousness".
- Butlin et al. TiCS ("Identifying indicators of consciousness in AI systems", 30(6), 488–501, issued June 2026): **real-correct** (Crossref, DOI 10.1016/j.tics.2025.10.011; authors include Bayne and Chalmers).
- Cutter 2025 ("The AI Ensoulment Hypothesis", *Faith and Philosophy* 41(1), 1–26): **real-correct** (publisher bepress metadata, DOI 10.37977/faithphil.2025.41.1.1, online 2025-05-30). The "at least a middling credence … conditional on our eventual creation of AGI and the truth of substance dualism in the human case" gloss is faithful to the abstract. The quotation form was corrected (see Medium).
- Békefi 2026 (*Faith and Philosophy* 42(1), 121–146): **real-correct** at the publisher. Inline year-cite removed instead of adding a reference (Critical 5).
- Deutsch 1999 (*Proc. R. Soc. A* 455(1988), 3129–3137): **real-correct** (Crossref).
- Metzinger 2021 (*JAIC* 8(1), 43–66): **real-correct** metadata (Crossref). "on post-biotic carrier systems" and the 2050 moratorium are verbatim in the abstract (OpenAlex). "explosion of negative phenomenology": the publisher PDF and PhilArchive both returned 403 here, so this is **verified only through a secondary verbatim quotation** (a Qeios critique reconstructing Metzinger's premise A2: "the risk of ENP (explosion of negative phenomenology) is currently incalculable"). The primary text was not grepped this pass.
- Schwitzgebel 2024 ("Repetition and Value in an Infinite Universe", *Extreme Philosophy*, Routledge, pp. 154–169): **real-correct** (Crossref, DOI 10.4324/9781003311065-11, 2024). The diminishing-returns gloss is carried forward (06-20).
- Schwitzgebel 2025 (arXiv:2510.09858): metadata **real-correct** (arXiv abstract page, latest v4 dated 2026-03-30). **Gloss wrong, now corrected** (Critical 1).
- Tokayer (PhilArchive TOKWDP-2): carried forward as **real-correct**.
- Tomasik ("How to Interpret a Physical System as a Mind"): metadata **real-correct**. **The quoted phrase is fabricated relative to the source and has been de-quoted** (Critical 2).
- Wallace 2012 (OUP): carried forward.
- Anthropic Constitution (linked, not in References): **misquote corrected** (Critical 6).
- Superlative sweep: none of the edited passages makes a currency-sensitive superlative.

### Map-internal quotations re-grepped

- The [P-AC1](/positions/ai-consciousness-scope/#p-ac1) band ("*low probability*, not *ruled out*") and the [P-AC1](/positions/ai-consciousness-scope/#p-ac1) inbound anchor `#framework-dependent-assessment` (heading kept) both check out.
- `ai-consciousness` §Other Challenges carries the admission ("a philosophical commitment, not an empirically grounded claim"; "supplies no present evidential weight against AI consciousness over biological consciousness"), and L90 paraphrases it faithfully.
- The [P-AC3](/positions/ai-consciousness-scope/#p-ac3) premises in L66 match the register.
- The `moral-census-opacity` pairing clause matches L100 there.
- Every section anchor resolves: ai-consciousness ×3, ethics-under-dualism, dualism-as-ai-risk-mitigation, the-experience-requirement-on-well-being `{#unconscious-subjects}`, `^p-ac3`, the tenet block ids, and the new `haecceity#process-haecceitism`.

### Reasoning-mode (editor-internal)

Functionalist: Mode Three. Metzinger: Mode Three (co-optation honestly flagged). Schwitzgebel: now Mode One / reflexive (his warning is accepted and turned on the Map; the avoidance policy is critiqued on its own practical terms). Deutsch/Wallace: Mode Three. Cutter: Mode Three. Bostrom: tenet-orthogonality shown (the tenets underdetermine the count). No label leakage.

## Optimistic Analysis Summary

### Strengths Preserved
- The reflexive possibility/probability discipline at L92 (a convenient implication cannot upgrade a tenet). The corrected Schwitzgebel paragraph now feeds into it ("hence the transparency note below").
- The copy-multiplicity section's honesty that the tenets *underdetermine* the copy count. Untouched.
- The framing note at L44, which keeps the Map-internal status of the verdict front-loaded.

### Enhancements Made
- The Schwitzgebel engagement is now accurate, and it is stronger as well: a mainstream sceptic's warning about motivated theory choice now bears on the Map's own convenient verdict.
- The Tomasik puzzle is correctly scoped as a Map extension.
- Four calibration loci now agree with [P-AC1](/positions/ai-consciousness-scope/#p-ac1).

### Cross-links Added
- [haecceity](/concepts/haecceity/#process-haecceitism) (repointed from a mislabelled many-worlds anchor).
- Same-page anchor `#framework-dependent-assessment`.

## Family Resolution

- **Schwitzgebel misreading.** It was live in `concepts/ai-epiphenomenalism` L85 as well ("His proposed 'social semi-solution'—treating AI systems as if they might be conscious when we cannot rule it out"). That sentence was fixed in the same pass to "names a forecast he declines to endorse … 'if social rationalization guides us rather than solid science, we risk massive delusion.'", and the next sentence's "permanent epistemic limitation" became "a lasting epistemic limitation", since the source says uncertainty "will likely continue to be justified for decades thereafter". That page went 2970 → 2987 against concepts hard 3500; `ai_modified` was bumped and `last_deep_review` left alone. `apex/open-question-ai-consciousness` L165 was already correct.
- **Not edited, reported**: the same misreading is still in `archive/topics/epiphenomenal-ai-consciousness.md` L100. Archive edits are held under the open publication-policy NEEDS-HUMAN. It is also in the research note [research/epiphenomenal-ai-consciousness-2026-02-10.md](/research/epiphenomenal-ai-consciousness-2026-02-10/) L67 and L151, where it originated.
- **Tomasik phrase**: present only in this article and in its research-note origin. **"in case"**: only in this article (the research note already carries the retraction). **"fitness to possess"**: only in this article and in research note `dualism-as-ai-superintelligence-risk-mitigator-2026-05-05` (research artifact, not edited).

## Remaining Items

- **Three [P-AC1](/positions/ai-consciousness-scope/#p-ac1) over-band loci were left because other tasks own their lines.** L56 "the probability for current classical AI is very low". L112 "very low—even epiphenomenally" (Epiphenomenal Complication; pessimistic-2026-07-06 Issue 3 is in the NEEDS-HUMAN length cluster). L138 "well above the vanishing numbers" (the Pascal reply; it interacts with pessimistic-2026-07-06 Issue 1, the unstated threshold). L56 and L138 are named by the blocked P3 witness/quantifier task. Minted as one blocked P3 so that they move when the Tenet 3 quantifier is decided.
- The NEEDS-HUMAN length decisions (condense-first / split / accept-deferred) are unchanged and still owed.

## Stability Notes

- Bedrock, not to be re-flagged: the functionalist rejection of the interface requirement; the MWI defender's dissatisfaction with the No-Many-Worlds ethical argument; Metzinger reaching the same alarm from functionalist premises.
- **Quotation-fidelity lesson for future passes**: three quotes that prior ledgers called "faithful" (Schwitzgebel's semi-solution gloss, the Tomasik phrase, the Constitution's "in case") all failed a raw-source grep. A future review should treat the current wording of those three as settled, since each was grepped this pass. It should *not* treat Metzinger's "explosion of negative phenomenology" as primary-verified until someone greps the paper's text.
- Calibration vocabulary now matches [P-AC1](/positions/ai-consciousness-scope/#p-ac1) everywhere outside the three owned loci. A future pass should not re-strengthen "unlikely", "discounting" or "moderate confidence".