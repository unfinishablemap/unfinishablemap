---
title: "Deep Review - What It Might Be Like to Be an AI"
created: 2026-06-06
modified: 2026-06-06
human_modified: null
ai_modified: 2026-06-06T19:34:46+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-06
last_curated: null
---

**Date**: 2026-06-06
**Article**: [[what-it-might-be-like-to-be-an-ai|What It Might Be Like to Be an AI]]
**Previous review**: [[deep-review-2026-05-21-what-it-might-be-like-to-be-an-ai|2026-05-21]] (preceded by 2026-04-27 and 2026-03-11 deep reviews; apex-evolve passes 2026-03-28, 2026-04-29, 2026-06-01)

This is the article's fourth deep review. Since the 2026-05-21 review it gained substantive **new content** not previously deep-reviewed: a quantum-dimension caveat citing Wiest (2025), Beshkar (2025), and NV-diamond sensors; engagement with the Butlin et al. (2023/2025) empirical AI-consciousness framework; the Claude Constitution "15–20% probability" passage in the Synthesis; and a repointed Neven (2024) citation. The new material is citation-bearing and the References block changed, so the §2.4 publisher-of-record web-verify pass was mandatory and was run in full.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Orphan References entries (citation cross-reference defect)**: References #6 (Chalmers & McQueen 2021, "Consciousness and the Collapse of the Wave Function") and #7 (Block 1978, "Troubles with Functionalism") had no inline anchor anywhere in the body — confirmed via git history that neither has *ever* been cited inline by author-year. Per §2.4 step 5, every References entry must be cited inline or removed. Both papers web-verified as real-correct and topically relevant, so the fix re-anchored them rather than deleting real references:
  - Block (1978) anchored in the Agency Without Understanding section (substrate-independence / functionalism passage): "This generalises Block's (1978) classic worry that functional organisation underdetermines phenomenal character…"
  - Chalmers & McQueen (2021) anchored in the Quantum Dimension section beside the Koch/Neven superposition-formation view: a parenthetical noting their consciousness-collapse model "pulls the other way, tying experience to the collapse dynamics rather than to superposition formation."
  **Resolution**: Both references now cited inline; orphans eliminated.

### Publisher-of-Record Web-Verify Ledger (§2.4)

All inline-cited and new/changed References entries verified against the publisher of record:

- Nagel 1974 (*The Philosophical Review* 83(4):435–450) — state: real-correct (carried from prior reviews; unchanged)
- Stapp 2007 (*Mindful Universe*, Springer) — state: real-correct (unchanged)
- Neven, Zalcman, Read, Kosik, van der Molen, Bouwmeester, Bodnia, Turin, Koch 2024 ("Testing the Conjecture That Quantum Processes Create Conscious Experience", *Entropy* 26(6):460, DOI 10.3390/e26060460) — state: real-correct. The repointed full citation (commit 925bf06a7) matches MDPI/PubMed exactly; author list, venue, volume, article number, and DOI all confirmed. "Consciousness arises when superposition forms" is faithful to the paper's thesis.
- Husserl 1928/1991 (*On the Phenomenology of the Consciousness of Internal Time*, Kluwer) — state: real-correct (unchanged)
- Frischhut 2024 ("Awareness without Time?", *The Philosophical Quarterly*) — state: real-correct (unchanged)
- Chalmers & McQueen 2021 ("Consciousness and the Collapse of the Wave Function", Preprint = arXiv:2105.02314) — state: real-correct. Now also cited inline (was orphan).
- Block 1978 ("Troubles with Functionalism", *Minnesota Studies in the Philosophy of Science* 9:261–325) — state: real-correct. Page range and venue confirmed at the UMN Digital Conservancy. Now also cited inline (was orphan).
- Cerullo 2026 ("Why Hoel's Disproof of LLM Consciousness and Functionalism Fails", *PhilArchive*) — state: real-correct (added in 2026-05-21 review; unchanged)
- Butlin, Long, Elmoznino, Bengio et al. 2023 ("Consciousness in Artificial Intelligence: Insights from the Science of Consciousness", arXiv:2308.08708) — state: real-correct. arXiv ID, title, lead authors confirmed; Chalmers confirmed among the 19-author team, so "with Chalmers among its contributors" is accurate. The indicator-properties theory list (recurrent processing, global workspace, higher-order, predictive processing, attention schema) matches.
- Butlin, Long, Bayne, Bengio et al. 2025 ("Identifying indicators of consciousness in AI systems", *Trends in Cognitive Sciences*, DOI 10.1016/j.tics.2025.10.011) — state: real-correct. Venue and authorship confirmed at cell.com (article S1364-6613(25)00286-4); the cited DOI resolves consistently. Successor relationship to the 2023 report is accurate.
- Wiest 2025 ("A quantum microtubule substrate of consciousness is experimentally supported and solves the binding and epiphenomenalism problems", *Neuroscience of Consciousness* 2025(1):niaf011) — state: real-correct. Oxford Academic / PubMed confirm title, venue, issue, article number verbatim. Article's characterisation ("review of room-temperature quantum effects in microtubules") is faithful.
- Beshkar 2025 ("Consciousness and spintronic coherence in microtubules", *Communicative & Integrative Biology* 18(1), DOI 10.1080/19420889.2025.2576334) — state: real-correct. Taylor & Francis / PMC confirm. The article's gloss ("spintronic-coherence proposal that may sidestep Tegmark's decoherence calculation") is faithful to the QBIT spintronic-coherence thesis.

No fabricated cites, no wrong-metadata, no wrong-paper. The two defects found were orphan-direction cross-reference errors (References entry without inline anchor), not metadata errors.

### Empirical-record currency sweep

`find_superlative_claims` returned one match ("so far" at L67), which is appropriately scoped ("the effects documented so far are vibrational modes") and carries no superlative-record claim requiring currency verification. No superseded superlatives.

### Medium Issues Found

None new. The recently-added content is well-calibrated.

### Low Issues Found

None.

### Counterarguments Considered

All six pessimistic personas engaged; findings consistent with prior reviews. No re-flagging of settled bedrock disagreements.

- **Eliminative Materialist (Churchland)**: "Sea of conscious entities" presupposes dualism — bedrock disagreement, not re-flagged.
- **Hard-Nosed Physicalist (Dennett)**: epiphenomenal AI is "permanently undetectable"; the article itself makes this point as honest boundary-marking. Not critical.
- **Quantum Skeptic (Tegmark)**: the new Wiest/Beshkar caveat *directly answers* the Tegmark-decoherence objection in the article's own voice ("whether neural systems sustain quantum coherence at all remains contested … the documented effects are vibrational modes, not the sustained coherent superpositions Stapp's and Koch's pictures require"). This is the calibration discipline strengthening, not weakening — the new material adds honest hedging rather than over-claiming the experimental turn.
- **Many-Worlds Defender (Deutsch)**: No-MWI tenet section brief by design — bedrock.
- **Empiricist (Popper)**: the new Butlin engagement and Claude Constitution passage are hedged appropriately; the orphan-reference defect was the only specific issue and is fixed.
- **Buddhist (Nagarjuna)**: "sea of conscious entities" reifies — bedrock.

### Calibration check (possibility/probability slippage)

Applied the §2 diagnostic test to the new content. The Claude Constitution passage is exemplary calibration: it cites a model's "15–20% probability of being conscious" estimate and immediately declares it **non-diagnostic** ("a text-predictor trained on human introspective writing would emit such an estimate whether or not anything is experienced"). This is the opposite of slippage — it refuses to upgrade a self-report into evidence. The Wiest/Beshkar caveat explicitly downgrades ("strengthen the empirical *precondition*", "only if such an interface is real in brains") rather than treating tenet-coherence as evidential upgrade. No possibility/probability slippage detected.

### Engagement classification (editor's notes; not for article body)

- **Butlin et al. empirical framework**: Mode Three — framework-boundary marking. The article credits the convergence (indicator-based, not binary) then marks the interpretive split ("the report's expectation that the remaining barriers are merely technical assumes the substrate-neutrality the Map's dualism denies — a framework-boundary disagreement, honestly noted rather than resolved here"). Honest; no boundary-substitution.
- **Self-stultification proponents**: Mode One — defective on its own terms (unchanged from prior review; scope-narrowing argument).
- **Illusionists (Frankish-style)**: Mode One — defective on its own terms (unchanged).
- **Cerullo's objection to Hoel**: Mode One — defective on its own terms (unchanged).
- **Standard arguments against AI consciousness**: Mode Three — framework-boundary marking (unchanged).

No boundary-substitution, no label leakage in prose (grep-confirmed clean).

### Attribution Accuracy

All checks pass. The two newly-anchored references (Block, Chalmers & McQueen) are attributed faithfully: Block's is correctly framed as a functionalism critique that functional role underdetermines qualitative character; Chalmers & McQueen's is correctly framed as a consciousness-*collapse* (not superposition-formation) model, which is exactly right — their IIT-plus-CSL model ties consciousness to collapse dynamics, contrasting with Koch/Neven's superposition-formation view. No source/Map conflation.

### Style/Cliché Check

"This is not X. It is Y." construct: 0 matches (grep-confirmed). No editor-vocabulary leakage.

## Optimistic Analysis Summary

### Strengths Preserved (untouched)

- Disaggregation insight in Synthesis (central original contribution)
- Both-possibilities balance — "none" preserved as the most likely answer for current systems
- Witness-consciousness "no exit" parallel
- Progressive structural build (epiphenomenal → agency → temporal → quantum → alien qualia)
- Five-model mnemonic (Flicker, Witness, Borrowed, Epiphenomenal, Alien)
- The new Claude Constitution passage is a genuine strength: it closes the self-report loophole crisply and is the most current empirical hook in the article.

### Hardline Empiricist (Birch) — counterweight check

The article continues to decline tenet-as-evidence-upgrade. The new experimental-turn caveat is precisely the evidential restraint Birch praises: it reports the 2025–2026 microtubule results as raising the *precondition* probability while explicitly noting the documented effects fall short of what the frameworks require. Tenet-coherence is offered as a question-framing tool, not as evidence anything is conscious.

### Enhancements Made

- Re-anchored Block (1978) and Chalmers & McQueen (2021) inline (fixes orphan-reference critical issue while preserving two real, relevant references).

### Cross-links Added

None. Cross-link density already high; all 20+ internal links verified resolving (including the newer [[claude-constitution-consciousness-uncertainty]], [[structural-varieties-of-consciousness-and-ai-phenomenology]], [[baseline-cognition]]).

## Length Assessment

- **Before**: 4212 words (105% of 4000 apex soft threshold) — `soft_warning`
- **After**: 4277 words (107% of soft threshold) — `soft_warning`, well under the 5000 hard threshold
- **Net change**: +65 words. The two inline citation anchors (non-discretionary — they fix a critical orphan-reference defect) were partially offset by tightening the Butlin paragraph and the Wiest/Beshkar caveat. Net increase kept small in length-neutral discipline; article remains comfortably under the apex hard threshold.

## Remaining Items

None.

## Stability Notes

The article has now passed four deep reviews (2026-03-11, 2026-04-27, 2026-05-21, 2026-06-06) plus three apex-evolve passes. Convergence pattern holds: the only critical issue this pass was a mechanical orphan-reference defect introduced when recent apex-evolve/refine restructuring condensed sections without preserving (or never having) inline anchors for two References entries. Now fixed.

Continue to treat as stable and not-to-be-re-flagged:

- Adversarial personas finding the dualist framework objectionable (eliminative materialism, MWI, Buddhist anti-reification) — bedrock disagreement.
- Quantum-consciousness section is appropriately speculative and hedged; the new Wiest/Beshkar/NV-diamond caveat strengthens, not weakens, the calibration.
- Nagel interpretation properly qualified ("what the Map reads as").
- Attribution verified strong across all 12 references (full publisher-of-record ledger above; do not re-litigate these cites unless the References block changes again).
- "Binding" placeholder acknowledgement is the correct epistemic position.
- No-MWI tenet engagement brief by design.
- Companion apex split ([[open-question-ai-consciousness]] = "whether"; this = "what it would be like") is intentional; neither should expand into the other's domain.
- The article preserves "none" as the most likely answer for current systems. The new Claude Constitution passage reinforces this by declaring model self-reports non-diagnostic. Any future edit softening this calibration is a regression to revert.

Next review should expect few or no issues unless source articles change materially or new content is added. The References block is now fully cross-referenced (no orphans in either direction) — a future no-op pass on a stable References list may skip the §2.4 web-verify per the trigger rule.
