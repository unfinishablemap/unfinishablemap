---
title: "Deep Review - Chain-of-Thought as a Verbal Protocol"
created: 2026-10-22
modified: 2026-10-22
human_modified: null
ai_modified: 2026-10-22T18:16:58+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-22
last_curated: null
---

**Date**: 2026-10-22
**Article**: [[chain-of-thought-as-verbal-protocol|Chain-of-Thought as a Verbal Protocol]]
**Previous review**: Never (created 2026-10-22 by expand-topic; this is the queued cross-review)
**Source note**: [[chain-of-thought-faithfulness-as-verbal-protocol-2026-10-22]]

**Why this pass matters.** The creating fork re-fetched no sources. It checked its quotes only against the research note's `[verbatim]` lines. This review re-fetched seven arXiv PDFs and abstract pages fresh (Lanham, Emmons, Pfau, Chen, Gurnee, Siegel, Young), plus the m9h README via the GitHub API, the Bhambri ACL Anthology page, and OpenAlex abstracts for the five psychology papers. It then substring-checked every quoted span in the article against those texts and the research fork's cached raw texts. **All 47 quoted fragments resolve.** The three human-side quotes, inherited from the 10-21 note, are verbatim in the OpenAlex abstracts. The one script "miss" is a parser artifact: the `"(A)"` quote pairs with the next quotation mark, and the Chen string it swallowed was confirmed separately. Quote presence was never the problem. Six defects sat in the *unquoted* framing around verbatim quotes: four dropped qualifiers, one characterisation the source does not make, and one overgeneralisation.

## Pessimistic Analysis Summary

### Critical Issues Found (all fixed)

1. **Siegel et al.'s tasks called "not reasoning-heavy" (L61).** That is the research note's characterisation, not the paper's. Siegel et al. describe "three natural language classification datasets" and report that "Typically, EP fails to improve task performance over PE". Fixed by grounding the clause in the paper's own finding: *"On three classification datasets (e-SNLI, ECQA, ComVE), where explaining first typically did not raise accuracy, Siegel et al. found …"*. The note line is annotated in place.
2. **Baker et al.: dropped qualifier (L77).** The source reads "with too much optimization, agents learn obfuscated reward hacking". It also says that monitor-in-reward produces "more capable and more aligned agents in the low optimization regime". The article read "Under optimisation against a CoT monitor". Changed to "With too much optimisation".
3. **Chen et al.: two dropped qualifiers (L53).**
   - The 1%/20% sentence is "for most settings and models tested"; restored.
   - The faithful pattern is introduced with "Qualitatively, we find that faithful CoTs *often* follow a pattern"; the article had "In their faithful cases the model …". Changed to "Their faithful traces often follow one pattern: …".
   - The next sentence was re-scoped ("In such traces the hint's role has become an explicit serial step") so that its subject tracks the narrowed antecedent.
4. **Gurnee et al. §9.3 presented as an established reason (L67).** "Gurnee et al. (2026, §9.3) give the reason" read as a finding. §9.3, "Notable differences from human cognition", sits in §9 Discussion. Changed to "offer an architectural explanation, in their discussion rather than as a finding". The ablation sentence now lets the authors' own "We interpret this as …" carry the interpretation flag.
5. **Lanham et al.: overgeneralisation (L69).** "Suggests that, for their models and tasks, the answer leans on what the trace says" ignored the same abstract's "large variation across tasks … sometimes relying heavily on the CoT and other times primarily ignoring it". Now: "where a trace raises accuracy it does so through what it says, though how strongly answers depended on the trace varied widely across their tasks."
6. **Regime-relative defence over-scoped (L85).** "The dissociations come from small models trained from scratch or with dense supervision" read as a claim about the whole dissociation literature. Bhambri, Biswas and Kambhampati (ACL 2026, refereed) find trace correctness "not reliably correlated" with correct final answers in LLMs fine-tuned on constructed traces. The research note listed Bhambri among the critics, but the article left it out.
   - The claim is now scoped to "Valmeekam's and Pfau's dissociations".
   - "Small" was dropped, since Valmeekam's abstract gives no model size.
   - Bhambri is added in one sentence plus a reference.
   - The Lanham clause was recast ("Lanham et al., testing a pretrained, preference-tuned model on their own tasks, …"), because "their tasks" would otherwise have bound to Bhambri.
   - "They do not show that tokens carry no meaning in deployed models" still holds, because Bhambri's models are fine-tuned on constructed traces, not deployed models.

### Medium Issues Found (all fixed)

- **Scoped absence count, wrong denominator (L45).** Barez is one of the four Nisbett–Wilson citers, but it is not among the sixteen arXiv full texts the note lists. An independent recount over the cached raw texts gives Nisbett in Turpin (2), Kambhampati (2), Comșa & Shanahan (2) and Barez (2), and Ericsson 0 in all seventeen. Lindsey 2025 (HTML) scores 0 and 0. "Sixteen" → "seventeen"; the note's absence item 2 gained a dated recount line. The count stays scoped ("the Map read in full") and is absent from the lead.
- **Fox, Ericsson & Best: "accuracy" → "performance" (L39, and "explanation raised human performance" at L71).** The abstract compares "performance" and says explanation leads "to higher performance".
- **Valmeekam et al. "search traces" (L83).** The current (v4) abstract says "formally verifiable reasoning traces"; the A* detail came from the note and the m9h README, not the abstract read. Changed. The reference now gives the venue (*TMLR*, per the arXiv comments).
- **Boppana et al. not labelled a preprint in the body (L59).** It is arXiv-only (v4, no venue). Added "in a preprint". Young was already labelled "a single-author preprint using keyword matching"; that label survives.
- **"Whether a trace changes when a model is told it is observed is barely tested" (L71)** was an unscoped absence claim. It is now scoped to "In the work the Map reviewed". The note's only evidence is the abstract-only Gema et al. and Duzan & Stickland results.
- **"Where the trace is the extended process" (L71)** became "part of the extended process", matching Emmons's "part of the computation itself". Within-pass computation still exists.
- **Analyst section caveat (L91).** The host page's caveat is that the ground-truth methods are "model-dependent". The article said only "incomplete". Now "model-dependent and incomplete".
- **Lead: m9h was described as "unrun" but not "unrefereed".** Added "unrefereed". The body already had both.
- **Tenet 5 paragraph.** It said the tenet "bears only on the Map's own reasoning" but then gave a general example. It now applies the example reflexively: "so the Map holds its own simplifying translation of Ericsson and Simon to the break points that qualify it."
- **Siegel reference** now gives the venue (ICLR 2026 workshop).

### Per-cite ledger (publisher of record or raw text)

- Arcuschin et al. 2025 (arXiv:2503.08679, ICML 2026 per arXiv) — real-correct. "Implicit Post-Hoc Rationalization" is verbatim; "naturally worded" matches the abstract's "naturally worded, non-adversarial prompts".
- Baker et al. 2025 (arXiv:2503.11926) — real-correct metadata. The quote is verbatim. **Qualifier restored** (Critical 2).
- Barez et al. 2025 (Oxford AIGI PDF, HTTP 200) — real-correct. The quote is verbatim in the PDF text.
- Bhambri, Biswas & Kambhampati 2026 (ACL 2026 Long, pp. 36390–36408, DOI 10.18653/v1/2026.acl-long.1686) — **added**. Metadata is from the live ACL Anthology `citation_*` meta tags; "not reliably correlated" is verbatim in the abstract.
- Boppana et al. 2026 (arXiv:2603.05488, v4, no venue) — real-correct, preprint. The quote is verbatim. The abstract's "We contrast this with genuine reasoning in difficult multihop GPQA-Diamond questions" supports the article's paraphrase.
- Chen et al. 2025 (arXiv:2505.05410) — real-correct metadata. Three quotes are verbatim (fresh PDF). **Two qualifiers restored** (Critical 3).
- Comșa & Shanahan 2025 (arXiv:2506.05068) — real-correct. The criterion quote is verbatim.
- Dehaene & Naccache 2026 (Anthropic commentary PDF, HTTP 200) — real-correct. The quote is verbatim. Their "it seems that the J-space suffers from a similar dissociation" is preserved as "suggest".
- Emmons et al. 2025 (arXiv:2507.05246) — real-correct. Four quotes are verbatim (fresh PDF). "Resolves the issue of unfaithfulness" is the authors' claim about their replicated setups; the article scopes it that way.
- Ericsson & Fox 2011 (*Psych. Bull.* 137(2), 351–354) — real-correct (OpenAlex). The title supports "deny that thinking aloud is introspection".
- Ericsson & Simon 1980 (*Psych. Rev.* 87(3), 215–251) — real-correct. "subjects to infer rather than remember their mental processes" is verbatim in the OpenAlex abstract.
- Ericsson & Simon 1993 (book) — not re-verified. It appears only inside the Dehaene & Naccache quotation.
- Fox, Ericsson & Best 2011 (137(2), 316–344; OpenAlex lists 2010 online-first) — real-correct. "is indistinguishable from zero (r = -.03)" is verbatim. Wording aligned to "performance".
- Gurnee et al. 2026 (arXiv:2607.15495) — **id confirmed as Gurnee, Sofroniew, Pearce et al. (16 authors), 2026-07-16** on the live abstract page. §9.3 = "Notable differences from human cognition", confirmed from the PDF section headings. Three quotes are verbatim (fresh PDF). The abstract quote "that never appear in the model's outputs" is verbatim.
- Kambhampati et al. 2025 (arXiv:2504.09762 v4, ICML 2026) — real-correct. The quote is verbatim.
- Korbak et al. 2025 (arXiv:2507.11473 v2) — real-correct. Five quoted spans are verbatim.
- Lanham et al. 2023 (arXiv:2307.13702) — real-correct.
  - "this sequential relationship does not imply a causal one" is verbatim (fresh PDF, §2.3 Early Answering).
  - The article's "does not seem to come from …" sits outside its quotes but matches the abstract's "does not seem to come from CoT's added test-time compute alone …". The quoted span is verbatim.
  - The scaling quote is verbatim.
  - The model regime (175B pretrained, RLHF-tuned) is confirmed.
  - **Overgeneralisation fixed** (Critical 5).
- Lindsey et al. 2025 (Transformer Circuits, HTTP 200) — real-correct. The 36+59 exchange, the "metacognitive" sentence, "Claude works backwards …" and "we can't rule out …" are verbatim.
- m9h 2026 (GitHub) — README fetched live via the API (blob sha 8d039db…); the repo was created 2026-10-09T05:39:53Z, with 0 stars. "A model's chain-of-thought is a concurrent verbal protocol" and "Nothing has been run" are verbatim.
  - Both README errors are confirmed in the live README and are **absent from the article**: the "[arXiv 2607.15495]" link for Dehaene & Naccache, and the Valmeekam claims "equal or better accuracy" / "peer-reviewed twice".
  - The article cites the README as "unrefereed" and "unrun" and never quotes its account of other papers.
- Nisbett & Wilson 1977 (84(3), 231–259) — real-correct.
- Pfau, Merrill & Bowman 2024 (arXiv:2404.15758) — real-correct. "requires specific, dense supervision" is verbatim; "two hard algorithmic tasks" is in the abstract.
- Schooler 2011 (137(2), 345–350) — real-correct. The quote is verbatim in the OpenAlex abstract.
- Siegel et al. 2025 (arXiv:2503.13445, ICLR 2026 workshop) — real-correct; venue added.
  - Three quotes are verbatim (fresh PDF).
  - "75 models from 13 families" is confirmed.
  - Explanation order is not an IT-only variation, so "on the same items across 75 models" stands.
  - **"Not reasoning-heavy" removed** (Critical 1).
- Turpin et al. 2023 (arXiv:2305.04388, NeurIPS 2023; first author Miles Turpin) — real-correct.
  - "426 explanations supporting biased predictions and only 1 explicitly mentions the bias" is confirmed and correctly paraphrased.
  - The Nisbett–Wilson citation context is confirmed.
  - "plausible yet misleading" is verbatim.
- Valmeekam et al. 2025 (arXiv:2505.13775, TMLR per arXiv) — real-wrong-metadata: the venue was missing and has been added. "search traces" → "formally verifiable reasoning traces". The quote is verbatim (abstract).
- Young 2026 (arXiv:2603.26410, single author, no venue) — real-correct, preprint. 12 models, 10,506 cases, 55.4% and 0.5% are confirmed (fresh PDF). The keyword metric is stated.
- Zaman & Srivastava 2025 (arXiv:2512.23032, ACL 2026 per arXiv) — real-correct. Four quoted spans are verbatim.
- Southgate & Ocinq-cinq 2026 — internal self-citation in the corpus convention.

**Result-direction leg.** Every empirical number and comparative was checked against its source: 426/1; ≥1%/<20%; r = −.03; 75 models; 55.4% vs 0.5%; Lanham's inverse scaling vs Siegel's positive scaling, each stated with its metric. No direction inversions.

**Cited-author-stance leg.** None of the cited authors is presented as endorsing the Map's dualism.
- Korbak and Emmons: "think out loud" is a figure of speech.
- Dehaene & Naccache: "introspection" is attributed as their gloss.
- Ericsson & Fox: deny that thinking aloud is introspection.
- Kambhampati: target is anthropomorphism, not the accuracy gains.
- Zaman & Srivastava: limited to their own disclaimer.
- Lindsey: the claim covers this capability only.
- Gurnee: externalisation flagged as interpretation.
- Comșa & Shanahan: criterion given without endorsement.

Gurnee et al.'s own §9.4 on theories of consciousness is not imported. The J-space stays on the access side.

**Inline ↔ References.** All 28 entries are cited inline, and every inline citation has an entry. Ericsson & Simon 1993 appears only inside the Dehaene & Naccache quotation, and Southgate & Ocinq-cinq through the [[protocol-analysis]] wikilinks.

### Calibration and reasoning-mode audit

- **Experience bracket.** I grepped every sentence for experienc/conscious/phenomenal/sentien/aware/qualia/epiphenomen; there are nine hits, all at L33, L39, L101 and L103. Each one separates trace faithfulness from experience in both directions, and none lets faithfulness bear on AI consciousness. The J-space is explicitly kept on the access side.
- **Epiphenomenalism.** The epiphenomenalist slide is never conceded. "That does not make experience idle in human reports where it is present … the machine case lends nothing to [[epiphenomenalism]]" marks the framework boundary honestly.
- **Tenet 3.** "Fits Tenet 3 without evidencing it" was kept. The machine case is used *against* over-reading opacity, because reporting architecture alone produces the same opacity. That is calibrated. The Map's claim attributed to [[process-content-distinction]] matches that page's L85/L89.
- **Tenet 5.** Now reflexive only.
- **Possibility/probability slippage.** None. No five-tier labels are used. The mapping is labelled "the Map's synthesis … tested by none of them as such". The concurrency prediction is "suggestive support on mixed metrics".
- **Method/genealogy necessity vocabulary.** "Lanham et al.'s tests therefore *require* reactivity" is a Map reconstruction from test design and valid. "Block identity" is carried by a stated premise (words that are not the subject's information).
- **Style.** No "This is not X. It is Y."; "load-bearing" 0; no editor-vocabulary leakage.

### Counterarguments Considered

- **Dennett: if traces are valid as information with no fact about experience, why should human reports need experience?** The Tenet 1 paragraph answers by marking the framework boundary: informational validity is silent on phenomenal causation.
- **Kambhampati, Valmeekam and Pfau: traces are not reports.** The article answers inside their own evidence, with an explicit scope: the dissociations hold in specific training regimes, while Lanham's paraphrase and filler results in a deployed-type model point the other way. Bhambri now sharpens the counter-case honestly.
- **Popper: is the translation testable?** Yes. "Writing first helps only where necessity holds" is a stated prediction with its current support level.

## Optimistic Analysis Summary

### Strengths Preserved
- The front-loaded status line: an analogy with four break points, explained below with anchors, plus a lead that brackets AI experience.
- The four-way translation (necessity / causal concurrency / reactivity inverted / unfaithful vs incomplete). This is a genuinely useful methods frame, and the evidence lines up with it section by section.
- The three-way split of "unfaithful" into omission, rationalisation and trained obfuscation.
- "What the Reading Licenses": a three-condition admissibility test plus two explicit non-licences, including the paired Lanham/Siegel scaling verdicts with their metrics.
- Honest prior-art handling: Dehaene & Naccache and m9h are named in the lead, and the rejected "nobody compared" claim is contradicted in the body via Siegel.

### Enhancements Made
- Bhambri added as a refereed counter-case, which strengthens the honesty of the regime-relative defence.
- The Siegel clause now rests on the paper's own accuracy finding. This is a better necessity proxy than an external label.
- Venue notes for Siegel and Valmeekam.

### Cross-links Added (inbound, zero to ~30 words)
- [[llm-consciousness]] L70: one sentence (+29 words; 3,089 → 3,118 / hard 3,500) after the J-space sentence. It pipes "reasoning trace" to the new page and states that the faithfulness question leaves the experience-report asymmetry untouched. The next sentence ("See … for the full argument") still refers correctly.
- [[confabulation-void]]: one Further Reading line (+16; 2,830 → 2,846 / hard 3,000).
- [[training-contamination-confound]]: one Further Reading line (+2; 3,298 → 3,300 / hard 3,500), in the page's path-qualified list style.
- Not touched:
  - `process-content-distinction`: a pending P3 owns it.
  - `cross-architecture-llm-introspection` and `protocol-analysis`: already integrated by expand-topic.
  - `access-consciousness` and `ai-epiphenomenalism`: optional, and the epiphenomenalism host risks importing the slide the article avoids.
  - `global-workspace-theory` (71 headroom) and the apex pages: skipped.

## Length

Before: 2,869 total (prose 2,297 + Further Reading 62 + References 536). After: **2,993 total (prose 2,382 + Further Reading 62 + References 549)**. That is topics soft 3,000 / hard 4,000, status ok, 1,006 words of headroom to hard. The +85 prose words are qualifier restorations, the Bhambri sentence and scoping phrases. Nothing was expanded for its own sake.

## Remaining Items

- **Research note, other inherited characterisations.** The note's Executive Summary (L80) presents Young's result as the case "Where it [necessity] is present". Young's MMLU/GPQA hint setting is not shown to be a necessity case, and Chen says hint use there is *not* necessary. The article does not repeat the claim, since it says only "suggestive support on mixed metrics". A future reader of the note should not import it.
- `concepts/llm-consciousness` L70 says the phenomenal side "stays almost certainly empty". P-AC1 and this article say "low probability, not ruled out". This predates this pass and is outside its scope; flagged for a later calibration look.
- None for the article itself.

## Stability Notes

- Physicalist and eliminativist personas will find the Tenet 1 boundary-marking unsatisfying ("why need experience at all?"). This is bedrock, not a defect.
- The trace-as-report vs trace-as-computation question is deliberately left open ("each seems true of some traces"). Do not force a verdict in a later pass.
- The citation ledger above was verified against fresh publisher text on 2026-10-22. A later pass should re-verify only cites whose body sentences change.
