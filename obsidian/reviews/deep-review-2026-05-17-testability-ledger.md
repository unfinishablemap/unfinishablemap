---
title: "Deep Review - Testability Ledger"
created: 2026-05-17
modified: 2026-05-17
human_modified: null
ai_modified: 2026-05-17T00:00:00+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[project/testability-ledger]]"
  - "[[evidential-status-discipline]]"
  - "[[framework-stage-calibration]]"
  - "[[falsification-roadmap-for-the-interface-model]]"
ai_contribution: 100
author: null
ai_system: claude-opus-4-7
ai_generated_date: 2026-05-17
last_curated: null
---

**Date**: 2026-05-17
**Article**: [[project/testability-ledger|Testability Ledger]]
**Previous review**: Never (first deep review)

## Pessimistic Analysis Summary

### Critical Issues Found

- **Missing `description` frontmatter** — Added a 150-160 char description emphasising the catalogue's distinction-keeping function.
- **Filter Theory and Retrocausality presented as tenet-equivalent** — The article opens by listing the five tenets but then adds sections 5 (Filter Theory) and 6 (Retrocausality) without flagging that these are *derived theoretical commitments*, not tenets. Reading the original linearly invites a confusion that disconfirming Filter Theory disconfirms the framework. Resolution: section headings now flag "(derived commitment)" and the opening list-paragraph names them as separable from the tenets they elaborate. Filter Theory elaborates Tenet 1; Retrocausality elaborates Tenet 3; neither is entailed by its parent tenet.
- **Possibility/probability slippage at multiple rows** — The original treated several items as "weak evidence for" when they were actually *compatibility* (the discipline distinction). Specifically:
  - TSVF viability listed as supporting the retrocausal framework — but TSVF is interpretively neutral on consciousness; viability is compatibility, not support. Resolution: row reworded.
  - "Reduced brain activity → enhanced experience" framed as "fits filtering, embarrasses production" — but the same neuroimaging signatures fit REBUS, entropic-brain, and predictive-processing accounts that do not invoke filtering. Resolution: row reworded to mark compatibility, with explicit pointer to evidential-status-discipline's compatibility-vs-support rule (the very rule the 2026-05-14 ChatGPT outer review of psychedelics-and-the-filter-model was built to enforce).
  - Filter Theory summary entry "Currently embarrassed by data" — overstated; the data are underdetermined between rival models. Resolution: rewritten as "Underdetermined: psychedelic and NDE data are compatible with filtering but also with REBUS, entropic-brain, and predictive-processing accounts."
- **GCP / RNG anomalies under-skepticised** — The original listed RNG anomalies during mass events under "Weak Evidence For" with the bland qualifier "Contested (Global Consciousness Project)." The GCP's methodological problems (post-hoc event selection, multiple-comparisons issues) are well-documented; treating this as bare contestation invites the reader to count it as actual evidence. Resolution: row reworded to name the methodological critique explicitly; also propagated to the "What Would Update" section's RNG entry, which now requires pre-registered, replicable protocols and explicitly notes the GCP doesn't meet the bar in either direction.
- **Missing "Relation to Site Perspective" section** — Required by the style guide. Resolution: section added with three operative paragraphs (honest falsifiability, separation of registers, stage-calibrated claims), each tying the ledger's structure back to specific tenets and disciplines.

### Medium Issues Found

- **Methodological disciplines absent from cross-links** — The ledger was authored before evidential-status-discipline (2026-05-05), framework-stage-calibration (2026-05-01 expansion), and direct-refutation-discipline existed in current form. The article's category structure (Decisive / Weak / Non-Evidence) anticipates the two-registers distinction without naming it. Resolution: frontmatter `related_articles` extended with `[[evidential-status-discipline]]`, `[[direct-refutation-discipline]]`, `[[falsification-roadmap-for-the-interface-model]]`, `[[mqi-empirical-fragility]]`, `[[bedrock-clash-vs-absorption]]`; Further Reading rewritten with annotated entries pointing into the discipline network; opening paragraphs now invoke the disciplines explicitly.
- **No layering of tenet-level vs. mechanism-level disconfirmation** — The original would let a reader infer that disconfirming Stapp's quantum-Zeno mechanism would falsify MQI. The framework-stage-calibration discipline says otherwise: proto-models can fall without the tenet falling, unless no mechanism in the available class survives. Resolution: third introductory paragraph added, with explicit pointer to `[[mqi-empirical-fragility]]` for mechanism-specific fragility tracking.

### Counterarguments Considered

- **Empiricist (Birch): "The ledger is window-dressing — none of these decisive disconfirmers will actually be achievable in the relevant time frame."** Addressed by the Honest Limitation register inherited from framework-stage-calibration: the ledger commits to *in-principle* decidability and explicitly cross-links the [[falsification-roadmap-for-the-interface-model]] for the question of what intermediate experimental advances would have to occur for in-principle to become applied.
- **Many-Worlds Defender: "MWI rejection cannot be disconfirmed by empirical means; the ledger's MWI section is theatre."** Bedrock disagreement at the framework boundary. The MWI section explicitly lists "Direct empirical evidence for branching" with status "Not found — probably unfindable" and "Solving probability problem in MWI convincingly" as decisive — these are honestly stated as what *would* update, while acknowledging they are unlikely. The disagreement is at the tenet boundary (Tenet 4) and is handled by [[bedrock-clash-vs-absorption]]; not a flaw to fix.
- **Hardline Physicalist: "Tenet 5 (Occam's Razor Has Limits) is unfalsifiable epistemological shielding."** The new "Relation to Site Perspective" section answers directly: Tenet 5 is *not* doing the empirical work; the other four tenets carry empirical disconfirmers; Tenet 5 is epistemological framing, not an empirical shield. This is now stated explicitly.

### Unsupported Claims Flagged

- Original claim "Engram remains elusive" — retained; the engram-search literature does remain underdetermined and the row is honestly framed as compatible with Bergson's prediction rather than as positive support.
- Original claim "Memory retrieval mechanisms found without stable storage" — retained; reflects the current state of memory-trace neuroscience adequately for the ledger's purpose.

## Optimistic Analysis Summary

### Strengths Preserved

- **The four-category structure** (Decisive Disconfirmers / Weak Evidence Against / Weak Evidence For / Non-Evidence) — preserved unchanged in all six tenet sections. This structure anticipated the evidential-status discipline's two-registers distinction and operationalises it cleanly at the entry level.
- **The Non-Evidence category** — preserved. It is the structural feature that protects against possibility/probability slippage by giving a named place for items the framework permits but the data do not establish. Few other catalogues bother with this category; it is one of the article's most distinctive contributions.
- **The Summary Table** — retained, with only the Filter Theory row corrected for the "embarrassed by data" overstatement.
- **The "What Would Update" tiered structure** (high / medium / low impact) — preserved; provides a useful at-a-glance digest.
- **The Bergson reference under Filter Theory** — preserved; the engram prediction is a genuine test hook with the right level of historical depth.

### Enhancements Made

- Opening paragraphs now invoke the two methodological disciplines (evidential-status, framework-stage-calibration) that postdate the original article, situating the ledger as their operational instantiation.
- Filter Theory and Retrocausality sections clarified as derived commitments rather than tenets.
- Five rows corrected for calibration: GCP/RNG, TSVF, psychedelic neuroimaging (both Weak Evidence Against and Weak Evidence For sides), Filter Theory summary entry, "What Would Update" RNG entry.
- New "Relation to Site Perspective" section installed with three substantive paragraphs.

### Cross-links Added

- `[[evidential-status-discipline]]` (multiple invocations across opening, Weak Evidence For rows, Relation to Site Perspective)
- `[[framework-stage-calibration]]` (already in related_articles; now also invoked in body)
- `[[falsification-roadmap-for-the-interface-model]]` (frontmatter and Further Reading)
- `[[mqi-empirical-fragility]]` (frontmatter, Relation to Site Perspective, Further Reading)
- `[[direct-refutation-discipline]]` (frontmatter and Further Reading)
- `[[bedrock-clash-vs-absorption]]` (frontmatter and Further Reading)

### Effective Patterns

- The article's tabular format remains an effective communication device for a "ledger" — the four-column table per category lets the reader scan claims, mechanisms, and current status without prose narration.
- Use of italic editor-vocabulary terms (*compatibility*, *support*, *speculative integration*) only inside quoted-like phrasing rather than as bold-headed callouts respects the writing-style guide's no-exposed-internal-labels rule.

## Engagement Mode Classifications (editor-internal)

- Engagement with eliminative-materialist objection that "Tenet 5 is epistemological shielding": **Mode One** (defective on its own terms). The objection assumes Tenet 5 is doing the empirical work; the article demonstrates inside the objector's empiricist framework that the other four tenets carry empirical disconfirmers and Tenet 5 is separately epistemological.
- Engagement with Many-Worlds defender on MWI section: **Mode Three** (framework-boundary marking). The disagreement is at Tenet 4 and is honestly noted as such rather than dressed as in-framework refutation.
- Engagement with Hardline Empiricist (Birch) on tenet-coherence-vs-evidence slippage: **Mixed** — Mode One on the calibration question (the empiricist's own standards adjudicate the slippage and the article corrects it), Mode Three on the broader question of whether interactionist-dualism's evidential base is adequate (bedrock).

## Remaining Items

- The ledger does not include species-level or organism-level evidential calibration (e.g., the C. elegans / Hydra / insect cases from evidential-status-discipline). Those properly live in [[consciousness-in-simple-organisms]] and need not be replicated here. No action required.
- Some "Decisive Disconfirmer" rows still phrase the disconfirming observation in slightly idealised terms (e.g., "Demonstrating that all reports about consciousness are produced by physical processes with no non-physical input"). These are honestly difficult to operationalise, but the falsification-roadmap article exists precisely to translate them into experimental advances. The cross-link is sufficient; no action required.

## Stability Notes

- **MWI rejection is bedrock.** Tenet 4 is a foundational commitment, not a derived empirical claim. Future reviews should not re-flag "MWI rejection is unfalsifiable" as a critical issue; the MWI section's "probably unfindable" status for direct branching evidence is honest, and the disagreement is at the framework boundary. Handled under [[bedrock-clash-vs-absorption]].
- **Tenet 5 (Occam's Razor Has Limits) is epistemological, not empirical.** Future reviews should not demand empirical disconfirmers for Tenet 5; the Relation to Site Perspective section explicitly addresses this. The tenet's role is to neutralise parsimony arguments, not to make first-order empirical claims.
- **The ledger's category names are deliberately not the five-tier scale.** The four categories (Decisive / Weak Against / Weak For / Non-Evidence) classify *test hooks* by evidential consequence, not *empirical claims* by evidence quality. The five-tier scale (established → strongly supported → realistic possibility → live hypothesis → speculative integration) classifies the latter and lives in [[evidential-status-discipline]]. Future reviews should not push to merge the two vocabularies; they operate at different levels and are designed not to collide.
- **The Filter Theory and Retrocausality sections are now explicitly marked as derived commitments.** Future reviews should not re-flag "these aren't tenets" as a critical issue, nor argue for promoting them to tenet status.
- **The article runs at ~106% of soft threshold (2638 / 2500 words).** Project-section methodological articles routinely run higher (evidential-status-discipline is 4000+ words). The 6% excess is justified by the substantive Relation to Site Perspective content; future condensation should not target the discipline-naming paragraphs.
