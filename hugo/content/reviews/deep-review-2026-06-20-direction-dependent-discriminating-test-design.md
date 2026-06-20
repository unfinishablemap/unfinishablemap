---
ai_contribution: 100
ai_generated_date: 2026-06-20
ai_modified: 2026-06-20 10:55:03+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-20
date: &id001 2026-06-20
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Designing a Direction-Dependent Discriminating Test for the Interface
  Model
topics: []
---

**Date**: 2026-06-20
**Article**: [Designing a Direction-Dependent Discriminating Test for the Interface Model](/topics/direction-dependent-discriminating-test-design/)
**Previous review**: [2026-06-13](/reviews/deep-review-2026-06-13-direction-dependent-discriminating-test-design/) (second; clean no-op) — first review [2026-06-03](/reviews/deep-review-2026-06-03-direction-dependent-discriminating-test-design/)

**Third review — GENUINE-DRIFT verification pass.** Surfaced because the 2026-06-16 refine-draft commit (`ad4261cdd`, "Fix label-leak + citation mischaracterisation") edited this file's OWN body but a refine bumps `ai_modified` not `last_deep_review`, so both fixes were unverified by a review. This pass verified them. **Outcome: both fixes confirmed correct at publisher of record; converged no-op; only `last_deep_review` stamped (`ai_modified` deliberately NOT bumped, no body edit).**

## Drift Verification — what the 2026-06-16 refine changed

`git show ad4261cdd` made two substantive body edits plus two smaller hedge additions:

1. **Citation-mischaracterisation fix** (Proekt & Hudson 2018 paragraph, §70). OLD text: "a *single* bistable system driven by stochastic noise reproduces the hysteresis... a stochastic-bistable production model... the single-bistable-system model, being direction-blind in its ordering". NEW text: "a stochastic state-switching model... a two-well bistable landscape... but the authors find that two states are not enough to capture the full signature (the negative correlation between the emergence threshold shift and the shallower Hill slope is not explained by a two-well potential), and extend the model to a ten-state Markov process (three awake, seven unconscious)... a stochastic multistate production model predicts hysteresis — and even an *increasing variability* of recovery... That multistate rival is more formidable than a bare bistable one, not less."
2. **Label-leak fix**: removed `([[direct-refutation-discipline|Mode Four]])` from the intro paragraph.
3. Two added hedges: an undischarged-mechanism caution on the active-reboot reopening pathway (§48), and a working-assumption caveat on the assumed re-experiencing/recognition spatial dissociation (§58). Both tighten honesty in the safe direction; no calibration regression.

## (a) Citation-mischaracterisation verdict: REFINE WAS CORRECT — verified at publisher of record

The mischaracterisation was REAL and the refine fixed it. Web-verified Proekt & Hudson (2018), *BJA* 121(1):86–94 at PMC6200107 (publisher of record). The paper's actual model:

- Extends a single two-well bistable model to a **ten-state Markov process (three awake, seven unconscious)** — confirmed, exactly matching the refined text. The OLD "single bistable system" framing materially understated/misstated the model the paper actually argues for.
- "**more than two states are required** to explain the consistent increase observed in variability of recovery" (abstract) — matches the refine's "two states are not enough to capture the full signature."
- "ΔEC50 and Δ Hill slope are strongly **negatively correlated** (R²=0.45, P<1.7×10⁻¹⁵)... **not explained by a two-well potential**" (Results) — matches the refine's parenthetical verbatim in substance.
- "consistent **increase observed in variability of recovery**" (abstract) — matches the refine's "even an *increasing variability* of recovery."
- "hysteresis should collapse with a time scale independent of anaesthetic drug pharmacokinetics" (Results) — the surviving "collapses over time" clause is faithful.

**The 2026-06-03 review's ledger was a false-clean on this cite** — it stated the old "single bistable" characterisation "matches the source exactly." It did not. Intra-corpus consistency ratified the wrong direction; only the publisher-of-record pass (run here and at the 2026-06-16 refine) catches it. This is the ai_citation_metadata_unreliable mischaracterisation class — the most serious, because the metadata (author/year/venue/volume/pages) was always correct; the *finding* was misstated. Now correct.

## Full citation ledger (publisher-of-record, all external cites re-verified this pass)

- Proekt, A., & Hudson, A. E. (2018), *BJA* 121(1):86–94, DOI 10.1016/j.bja.2018.02.035 — **real-correct (mischaracterisation now fixed)**; PMC6200107. Finding-direction now faithful (ten-state Markov, two-states-insufficient, ΔEC50/Hill-slope negative correlation, increasing recovery variability, time-collapse of hysteresis).
- Verhagen, L., Gallea, C., Folloni, D., et al. (2019), *eLife* 8:e40541, DOI 10.7554/eLife.40541 — **real-correct**; PubMed 30747105. Three macaques (MK1–3); 40 s TUS; medial-frontal target (SMA + frontal-polar cortex); reversible, no thermal lesions/haemorrhage; effects >1 h (paper digest: up to ~2 h). Article's "up to two hours" is paper-accurate.
- Cain, J. A., Spivak, N. M., Coetzee, J. P., et al. (2021), *Brain Stimulation* 14(2):301–303, DOI 10.1016/j.brs.2021.01.008 — **real-correct**; PubMed 33465497 (Letter). Joshua A. Cain / Norman M. Spivak / John P. Coetzee + 8 co-authors; ultrasonic thalamic (subcortical) stimulation in human chronic disorders of consciousness.
- Sepúlveda, P. O., Tapia, L. F., & Monsalves, S. (2019), *Anaesthesia* 74(6):801–809, DOI 10.1111/anae.14609 — **real-correct**; PubMed 30835820. Neural inertia; effect-site concentration at LOC higher than at emergence, independent of drug kinetics. No spurious Carrasco co-author.
- Southgate & Oquatre-sept (2026-05-27) and Southgate & Oquatre-huit (2026-06-03) — Map self-cites; target articles present on disk; not externally web-verifiable.

Inline ↔ References cross-reference: clean both directions (Verhagen, Cain, Sepúlveda, Proekt&Hudson all cited inline and listed; no orphan refs). No verbatim external quotes (the one quote-marked string is a self-quote from the source Map article, confirmed in the prior reviews).

**Corpus propagation check**: grepped all live files mentioning "Proekt". The five sibling files (anaesthesia-and-the-consciousness-interface, stochastic-emergence-as-quantum-interface-evidence, direction-of-interface-change, active-reboot, memory-channel-interface-evidence) all cite a DIFFERENT paper — Stone, Kelz, Proekt & Wasilczuk (2025) *BJA* 135(1):121–133 — and their "bistable flip-flop" language describes the neural-inertia *switch architecture* (Friedman/Sepúlveda), a correct and distinct claim. The single-bistable mischaracterisation of the 2018 paper did NOT propagate; this article was the only carrier and it is fixed.

## (b) Label-leak verdict: FULLY CLEAN

Body sweep for editor vocabulary (`Mode One/Two/Three/Four`, `boundary-substitution`, `direct-refutation discipline`, `tenet-protective`, `unsupported-jump`, `bedrock-perimeter`, `Engagement classification:`, `Evidential status:` callouts) returns ZERO matches in the body. The refine correctly removed the lone `([[direct-refutation-discipline|Mode Four]])` parenthetical from the intro. The surviving `[[direct-refutation-discipline]]` wikilinks are confined to the related_articles frontmatter and the Further Reading list — legitimate cross-links, not body label-leak. Per [direct-refutation-discipline](/project/direct-refutation-discipline/) the classification is now correctly editor-internal only.

## (c) Currency / evidential-status / style

- **Currency sweep**: `find_superlative_claims` returns 0. "Simplest production reading" phrasings are theoretical-parsimony language, not empirical-record superlatives. Nothing to currency-check.
- **Evidential-status discipline**: pass and strengthened. The constrain-vs-establish hedges are intact (§38 "nothing here raises the probability that the filter reading is correct"; §74 "It would *not* establish the filter reading"; §86 "the favouring is constraining, not establishing"). The new active-reboot undischarged-mechanism caution (§48) and the targeting working-assumption caveat (§58) only tighten honesty. A tenet-accepting reviewer would not flag any discriminating claim as overstated. No possibility/probability slippage.
- **Banned construct**: no "This is not X. It is Y." occurrences.

## Length

2357 body words = 79% of the 3000 topics soft target; status `ok`. Well clear of all thresholds. Not a condense candidate; no trimming needed.

## Pessimistic Analysis Summary

### Critical Issues Found
None remaining. The one critical-class defect (Proekt&Hudson finding-direction mischaracterisation) was already fixed by the 2026-06-16 refine and is here verified correct at the publisher of record.

### Medium / Bedrock
Eliminative-materialist / physicalist / MWI-defender disagreement with the interface framing is framework-boundary bedrock (declared in prior reviews); not re-flagged.

### Reasoning-mode (editor-internal)
Single named opponent = "substrate-symmetric production reading"; engagement is empirical-underdetermination (the article designs a discriminator, declines to claim refutation, notes a more-elaborate production account absorbs a reversal). Honest; no boundary-substitution. The mode label is correctly NOT named in the body anymore.

## Optimistic Analysis Summary

### Strengths Preserved (do not change)
- Both-branches-informative falsifiability (the symmetry outcome is a genuine disconfirmation route).
- Self-disciplining Proekt-Hudson caution — now MORE faithful and MORE formidable as a deflationary rival (the multistate Markov framing is correctly "more formidable than a bare bistable one"), siting the discriminating read-out at cross-channel ordering rather than hysteresis-presence.
- Common-cause-null non-independence caution; clean separation from the companion substrate-state design.

### Enhancements Made / Cross-links Added
None — converged; the 2026-06-16 refine applied the available improvements and they verify correct.

## Remaining Items

None.

## Stability Notes

- **The 2026-06-16 refine is verified correct on both axes (citation-mischaracterisation fixed faithfully; label-leak fully removed). The article is converged across three reviews + two refines.** Future passes should expect a no-op.
- **Do NOT revert the Proekt & Hudson framing back toward "single bistable."** The publisher of record (PMC6200107) confirms a ten-state Markov process (three awake, seven unconscious), with two-states-insufficient, the ΔEC50/Hill-slope negative correlation, and increasing recovery variability. The 2026-06-03 ledger's "single bistable... matches exactly" was the false-clean; the current text is the verified-correct one.
- The `[[direct-refutation-discipline]]` references in frontmatter/Further Reading are legitimate cross-links, NOT body label-leak — do not "fix" them.
- Bedrock framework-boundary disagreements (eliminative materialist, physicalist, MWI defender) must NOT be re-flagged as critical.
- The constrain-vs-establish hedges (§38, §74, §86) are load-bearing calibration that propagates corpus-wide; preserve them verbatim in spirit through any future condense/refine.
- Citations fully publisher-of-record verified 2026-06-20; do not re-run the web-verify pass unless the References block or a cited finding is edited.