---
title: "Deep Review - Delegation Meets Quantum Selection"
created: 2026-09-30
modified: 2026-09-30
human_modified: null
ai_modified: 2026-09-30T13:56:53+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-fable-5-1
ai_generated_date: 2026-09-30
last_curated: null
---

**Date**: 2026-09-30
**Article**: [[delegation-meets-quantum-selection|Delegation Meets Quantum Selection]]
**Previous review**: [[deep-review-2026-07-15-delegation-meets-quantum-selection|2026-07-15]] (seventh review overall)
**Word count**: 2769 → 3096 (article started below the 3000 soft threshold; hard limit 4000)

## Pessimistic Analysis Summary

### Critical Issues Found

- **Misattributed term (attribution error).** L46 scare-quoted a "general interaction problem" and said it "is acknowledged as open" by Saad's theory. The phrase occurs nowhere in Saad (2025); it is the Map's own wording from `topics/delegatory-dualism` L184. Saad's actual stance is the reverse: he treats "the interaction problem of explaining the possibility of phenomenal-physical causal relations" as one dualists *can* answer "by appealing to virtually any of the available theories of causation", in contrast to the Upward Systematicity challenge his paper targets. **Resolution**: rewritten to quote Saad's own description of the interaction problem verbatim, state his stance, and mark the mechanism gap as the Map's framing of what the paper leaves unaddressed rather than a concession Saad makes.
- **Spliced quotation.** L42 presented one quotation joined by an ellipsis that was in fact assembled from two separate paragraphs of `topics/delegatory-dualism` (L202 and L204). **Resolution**: split into two verbatim spans, each grep-verified against the source.
- **Internal contradiction / calibration.** L104 (Dualism tenet) asserted the bridge "strengthens the dualist case by *showing* these are ... two faces of one causal event", while L92 (installed 2026-07-15) holds the single-event identification open as a candidate identity. **Resolution**: conditionalised — "if the identification proposed above holds" — with an explicit pointer to the structural non-identity.
- **Empirical overclaim (family-resolution sub-finding).** L60 called the Born rule "the most precisely confirmed regularity in physics". The Map's own `concepts/sorkin-higher-order-interference` records the direct tests as bounds on third-order interference near 10⁻⁴ (Kauten et al. 2017), and `topics/born-rule-and-the-consciousness-interface` L100 notes every precision test ran in regimes unlike brain tissue; the QED-level precision the superlative evokes belongs to expectation values derived within the framework, not to direct tests of the rule. Two prior reviews of the sibling (`deep-review-2026-06-22-delegatory-causation`, `-07-18-`) certified the phrase as "accurate" without checking it against the Sorkin page. **Resolution**: reworded to "among the most thoroughly confirmed regularities" with the 10⁻⁴ bound and a link; the identical sentence in `concepts/delegatory-causation` L146 was corrected in the same form (length-neutral there: 3493 → 3490 words, hard limit 3500). `decoherence-and-macroscopic-superposition` L123 already uses the hedged "among the most precisely confirmed" and was left alone.
- **Contradiction with Saad on the default profile.** L60 called the default "a measurable probability distribution" while L52 (correctly) says the profile is never directly observed in conscious systems. **Resolution**: "derivable in principle from the neural quantum state, even though ... never directly observed".

### Propagation lens (tenets.md as it now reads)

- **Observational-closure convergence vs. tenets L75/L81/L107 unconditioned-aggregate scoping.** L62 claimed Born-respecting selection "is therefore observationally closed in the sense Saad defines". Saad's Observational Closure ranges over any experiment "within the realm of nomic possibility", not merely aggregate ones, and Saad explicitly classifies quantum interactionist dualism as *violating* it (already recorded at `concepts/observational-closure` L72). The tenets page now scopes Born preservation to the unconditioned marginal and keeps an intention-conditioned deviation live (P-Q3). On that branch the bridge would violate Saad's constraint. **Resolution**: convergence made conditional on the strict selection-only reading, with the conditioned branch and its consequence stated; Further Reading gloss on `[[observational-closure]]` rescoped from "no empirical trace" to "no trace in unconditioned aggregate statistics"; L106 "creating no statistical anomalies" rescoped likewise.
- **Improper-mixture form (tenets L71/L105).** L70 already used "improper mixture" but the surrounding "options"/"possibilities" language admitted the classical-menu reading the tenets page now disclaims. **Resolution**: one sentence added stating that what is selected is a component of the improper reduced-state mixture awaiting actualisation — an additional actualisation postulate, not a pick from a pre-existing classical menu.
- **Tenet 3 standing note (tenets L95) and PCS roster (L103).** L108 asserted reports "are genuinely caused by conscious experience, avoiding epiphenomenalism's self-undermining implications" — exactly the "genuine causal work" register the standing note says inherits rather than discharges the debt, and a self-stultification framing the tenets page now says does not refute epiphenomenalism from inside the phenomenal-concept strategy. **Resolution**: rewritten to "could be caused", linked to `tenets#^tenet-3-standing`, with the PCS limit stated.
- **Minimality as necessity claim (method/history calibration rule).** L106 "delegation within Born-rule probabilities *is* the minimal possible intervention" — label: *framework-conditional implication*. Transition check: the tenets page (L69) marks minimality as an empirical constraint, not truth-tracking; no separate premise carries "smallest the framework specifies" to "minimal possible". **Resolution**: relabelled as a framework-conditional implication, not a demonstrated minimum.
- No Many Worlds (L110) and Occam (L112) paragraphs already carry their conditionality (posit-dependent; "remains a philosophical commitment") — no change.

### Publisher-of-record citation ledger (§2.4 — triggered: References block changed 2026-09-08)

- Saad 2025 (A dualist theory of experience) — state: **real-correct**. Crossref: *Philosophical Studies* 182(3-4), 939-967, doi 10.1007/s11098-025-02290-3, published 2025-02-18, sole author Bradford Saad. Reading checked against the open-access full text: "default causal profile", "Subset Law*", "Delegatory Law", the major/sergeant analogy and "Observational Closure" (defined over nomically possible experiments) all present and used as the article uses them; "general interaction problem" absent (corrected above). Stance leg: Saad is a closure-*preserving* dualist who classes quantum interactionist dualism as Observational-Closure-violating and "not the project of this paper" — the article now says so rather than presenting him as party to the bridge.
- Torres Alegre 2025 (Causal Consistency Selects the Born Rule) — state: **real-correct**, with one reading correction. arXiv:2512.12636, submitted 2025-12-14, author Enso O. Torres Alegre, preprint flag intact. Abstract: "in any GPT satisfying purification, and therefore admitting steering, the only such relationship consistent with no-signaling is the identity"; "any strictly convex or concave deviation from linearity enables superluminal signaling". The article's "any nonlinear deviation" over-generalised the abstract's scope — corrected to the abstract's wording. Result-direction leg: reports the result in the direction the article states (form of the rule fixed, not its existence — already hedged).
- Southgate & Oquatre-six (2026-02-15) Delegatory Causation; Southgate & Oquatre-cinq (2026-01-29) Delegatory Dualism — Map self-cites at live URLs; pseudonymous co-author form is the established convention (not a fabrication signal).
- Inline ↔ References orphan check, both directions on (surname, year): inline Saad 2025 ↔ ref 1; inline Torres Alegre 2025 ↔ ref 2; refs 3–4 are the two Map articles quoted inline. No orphans either way. `find_superlative_claims`: no hits (the "most precisely confirmed" overclaim above uses a form the helper does not match — caught by hand).
- Internal quotations grep-verified against raw sibling sources: delegatory-dualism L202/L204 (now two spans), L194 ("combining two speculative frameworks multiplies assumptions rather than reducing them"), trumping-preemption L87 ("a distinct and potentially competing mechanism ... rather than an instance of"), delegatory-causation L174 (carries the same note). Trilemma "working heuristic rather than a complete partition" matches `trilemma-of-selection` L40/L82. Bandwidth ~10 bits/s matches `consciousness-bandwidth-architecture` L43/L55.
- All 25 wikilink targets resolve to exactly one live file; the five `tenets#^…` anchors and `^tenet-3-standing`, `positions/quantum-interface#^mechanism-debt` exist.

### Medium Issues Found

- "not a philosopher's thought experiment but a measurable probability distribution" was both an overclaim and the "not X but Y" construct the style guide flags — removed with the L60 rewrite.

### Reasoning-mode classification (editor-internal)

- Engagement with Saad (closure-preserving delegatory dualist): Mode Three, now honestly marked — the article presents the bridge as a Map proposal Saad would classify as Observational-Closure-violating on the conditioned branch, rather than as something his framework licenses.
- Engagement with Everett (L110): Mode Three, posit-dependent, unchanged.

### Counterarguments Considered

- *Quantum Skeptic*: "the Born rule's precision is irrelevant if the brain's relevant states are not quantum-indeterminate" — already carried at L96 ("if quantum effects in the brain prove negligible, the bridge has no physical foundation").
- *Hard-Nosed Physicalist*: "delegation is empirically invisible by design and quantum selection is invisible in aggregate by construction; the bridge is unfalsifiable" — bedrock at the framework boundary, but the conditioned-deviation branch now named at L62 is the article's honest statement of where a test would bite.

## Optimistic Analysis Summary

### Strengths Preserved

- The candidate-identification register of the lead and the four-item "What the Bridge Does Not Resolve" section (including the 07-15 structural non-identity item) — untouched.
- The bandwidth-as-delegation-scope section and the skill-delegation inverse — untouched; the Hardline Empiricist persona notes it as the article's most concrete, least tenet-loaded contribution.
- Saad's terminology is now used with the paper's own scope, which the Property Dualist persona reads as strengthening rather than weakening the bridge.

### Enhancements Made

- Six body passages calibrated (listed above); one sibling sentence propagated.

### Cross-links Added

- [[sorkin-higher-order-interference]] (target and sibling)
- [[tenets#^tenet-3-standing]], [[positions/quantum-interface#^mechanism-debt]]

## Remaining Items

- The article now sits at 3096 words (soft warning, hard 4000). No condensation debt, but the next review should not expand further.
- `topics/delegatory-dualism` L184 still uses "the general interaction problem for dualism" as the Map's own phrase (unquoted, not attributed to Saad) — acceptable as Map vocabulary; not changed.

## Stability Notes

- Carried forward from 2026-07-15: the delegation↔quantum-selection identification is a candidate unification the Map proposes; do not re-flag "single event" as critical now that both the structural non-identity (L92) and the Dualism-tenet paragraph (L104) are conditionalised.
- The observational-closure convergence is now explicitly *conditional on the strict selection-only branch*. A future review should not re-flag "the bridge violates Saad's Observational Closure on the conditioned branch" — the article says so.
- "The Born rule is the most precisely confirmed regularity in physics" was certified accurate by two sibling reviews (06-22, 07-18); this review overrode that on the strength of the Map's own Sorkin page. Do not restore the superlative without a publisher-of-record source that gives a direct Born-rule test at better than the QED level.
- Physicalist/Everettian objections to the bridge's existence are bedrock; the persona disagreements at L96/L110 are not correctable defects.
