---
title: "Deep Review (References Hygiene + Physics-Cite Web-Verify) - Dualism as AI Risk Mitigation"
created: 2026-06-24
modified: 2026-06-24
human_modified: null
ai_modified: 2026-06-24T14:17:24+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-06-24
last_curated: null
---

**Date**: 2026-06-24 (14:17 UTC)
**Article**: [[dualism-as-ai-risk-mitigation|Dualism as AI Risk Mitigation]]
**Previous review**: [[deep-review-2026-06-02-dualism-as-ai-risk-mitigation|2026-06-02 (10:42 UTC)]] (sixth prior review; heavily converged article — score 16 after convergence damping from 6 priors)
**Pass type**: References-hygiene + physics-cite web-verify. Body content unchanged since 2026-06-02; the References block carried a malformed-numbering artifact left by that review's Mørch removal, and the four §10 physics cites plus two §7 vacuum-decay cites had never been web-verified (the 2026-06-02 pass verified only the six AI-risk/consciousness *specialist* cites).

## Critical Issues Found (all fixed)

1. **Reference numbering gap (16 → 18, missing 17)** — the References list was non-consecutive: it ran 1–16 then jumped to 18–23. This is a residual artifact of the 2026-06-02 review's removal of the misattributed Mørch citation (old #16) without renumbering the tail. A malformed reference list is a structural defect. **Fixed**: renumbered the entire block consecutively to 1–21.

2. **Orphan reference — Coleman & De Luccia (1980)** (old #9, "Gravitational effects on and of vacuum decay," *Physical Review D* 21(12), 3305–3315) — a real, canonical paper (the CDL instanton) but **never cited inline**. The body's §7 electroweak-vacuum example cites only Coleman 1977 (which IS cited inline at line 106, "Coleman 1977; Buttazzo et al. 2013"). Per §2.4 step 5 (every References entry must be cited inline or removed), the uncited Coleman & De Luccia entry was **removed** — it is redundant with the cited Coleman 1977 on the same vacuum-decay point, so no body claim loses support. Net −20 words.

## Citation Web-Verify Results (physics cites — newly verified this pass)

The 2026-06-02 review web-verified six specialist cites (Cutter, Békefi, Townsend, Ziesche/Yampolskiy, Mørch [removed], Asphaug [→ Arvan & Maley]). It did NOT verify the physics references. Those four §10 decoherence cites + two §7 vacuum-decay cites were added at commit 3127bd911 (predating the 2026-06-02 pass) and had never been checked at the publisher of record. Verified this pass:

- Tegmark, M. (2000). Importance of quantum decoherence in brain processes. *Physical Review E* 61(4), 4194–4206 — **state: real-correct** (PubMed 11088215; APS DOI 10.1103/PhysRevE.61.4194).
- Hagan, S., Hameroff, S. R., & Tuszyński, J. A. (2002). Quantum computation in brain microtubules. *Physical Review E* 65(6), 061901 — **state: real-correct** (PubMed 12188753; ADS 2002PhRvE..65f1901H).
- McKemmish, L. K., Reimers, J. R., McKenzie, R. H., Mark, A. E., & Hush, N. S. (2009). Penrose-Hameroff orchestrated objective-reduction proposal… not biologically feasible. *Physical Review E* 80(2), 021912 — **state: real-correct** (UCL Discovery; PhilPapers MCKPOO; APS DOI 10.1103/PhysRevE.80.021912).
- Reimers, J. R., McKemmish, L. K., McKenzie, R. H., Mark, A. E., & Hush, N. S. (2009). Weak, strong, and coherent regimes of Fröhlich condensation… *PNAS* 106(11), 4219–4224 — **state: real-correct** (PubMed 19251667; PMC2657444; ADS 2009PNAS..106.4219R).
- Coleman, S. (1977). Fate of the false vacuum: Semiclassical theory. *Physical Review D* 15(10), 2929–2936 — **state: real-correct** (canonical; erratum PRD 16, 1248).
- Buttazzo, D., et al. (2013). Investigating the near-criticality of the Higgs boson. *JHEP* 2013(12), 89 — **state: real-correct** (Springer DOI 10.1007/JHEP12(2013)089; seven-author list matches).

The six AI-risk/consciousness specialist cites remain web-verified as of 2026-06-02 (Cutter clean; Békefi/Townsend/Ziesche-Yampolskiy metadata-corrected; Asphaug→Arvan & Maley corrected; Mørch removed). Not re-verified — no material change since.

Foundational AI-risk cites (Bostrom 2009/2012/2014, Hubinger et al. 2019, Russell 2019, Leike & Hutter 2018, Knight 1921, AI Impacts 2018) are canonical textbook-level references present through all six prior reviews; treated as established.

**Inline ↔ References cross-check (both directions): clean** after the Coleman & De Luccia removal. Every inline `Author YYYY` resolves to a References entry; every References entry is cited inline. (Knight 1921 is cited only via the eponymous adjective "Knightian uncertainty" at lines 68/148 — a legitimate eponymous-source inclusion for a named concept the body uses; retained, not flagged as an orphan.)

**Empirical-record currency sweep**: `find_superlative_claims` returns empty — no superlative empirical claims to re-verify against the live literature.

## Low Issues Found (fixed)

- **"Tuszynski" diacritic inconsistency** (§10, line 138): body used "Tuszynski" while reference 10 and the verified Polish spelling use "Tuszyński". **Fixed** body to "Tuszyński" for consistency.

## Possibility/Probability-Slippage Calibration Check

**Clean.** The central claim is conditional throughout ("*if* dualism is true, *then* the standard expected-utility argument for AI takeover loses force" — lines 40, 42, 140), anchored to the [[possibility-probability-slippage]] discipline. The §7 unbounded-impact and active-protection claims are honestly tagged "speculative-integration-tier" (line 110). The protective effect is sourced to a *structural* property (indeterminability / non-derivable arbitrary powers), not asserted as positive evidence. Diagnostic test (would a tenet-accepting reviewer still flag any claim as overstated relative to the five-tier scale?) returns no hits. The §6 plurality option stays self-undercutting (does not spin dualism as uniquely protective); the epistemic-vs-tactical asymmetry remains explicit (§6, §10 instrumentalism). No body content changed this pass, so the modal register is unchanged from 2026-06-02.

## Reasoning-Mode / Editor-Vocabulary Check

- **No editor-vocabulary leakage in body prose** (re-verified): zero hits for "Mode One/Two/Three", `direct-refutation-feasible`, `unsupported-jump`, `bedrock-perimeter`, `Engagement classification`, `Evidential status:` callouts. `direct-refutation-discipline` appears only in `related_articles` frontmatter (line 31), not as body meta-commentary. The 2026-05-11 line-134 leak fix holds.
- No new named-opponent engagements added. All §2/§5/§7/§9/§10 mode classifications from the 2026-05-11 and 2026-06-02 reviews carry forward (Bostrom convergence §2: Mode Two+Three; Bostrom Pascal's Mugging §7: Mode One; Russell §5: Mode Three/absorption; Cutter §9: Mode One+Three; §10 coercion-substitution: Mode One; §10 MQI fragility: Mixed; §10 instrumentalism: Mode One). No boundary-substitution.

## Optimistic Analysis Summary

### Strengths Preserved
All strengths from prior reviews hold. The Cutter/Békefi ensoulment engagement (§9), the conditional-structure-as-slippage-discipline self-defence (§10 instrumentalism), and the "shield narrows… does not dissolve" framing remain effective and untouched. The §10 physics-debate paragraph (Tegmark / Reimers / McKemmish / Hagan-Hameroff-Tuszyński / Born-rule programme) is now fully and correctly referenced and verified clean — the Hardline Empiricist (Birch) praise from 2026-05-11 stands: the article concedes empirical magnitude-exposure honestly rather than upgrading the dualism to absorb it.

### Enhancements Made
Reference list integrity restored (consecutive numbering; orphan removed). Six physics cites web-verified clean and recorded in the ledger. Diacritic consistency fixed. No prose-quality or expansion changes (length-neutral / net-reducing, hygiene-focused pass).

## Cross-links Added
None this pass. Cross-link density is appropriate; the article is at 124% of soft threshold (length-neutral mode).

## Remaining Items

None actionable. (Prior review's §6 "second panpsychism citation for the plurality list" note remains low-priority and optional; the plurality argument does not depend on citation count — do NOT restore a Mørch cite without confirming an actual Mørch paper on the point.)

## Stability Notes

- **Reference list is now consecutively numbered (1–21) and fully cross-checked** as of 2026-06-24. Future reviews should not re-introduce the orphan Coleman & De Luccia (1980) cite — Coleman 1977 already carries the §7 vacuum-decay point.
- **All six physics cites are now web-verified clean** (Tegmark 2000, Hagan/Hameroff/Tuszyński 2002, McKemmish et al. 2009, Reimers et al. 2009, Coleman 1977, Buttazzo et al. 2013). Do not re-verify unless the article is materially modified.
- **All bedrock disagreements carry forward, do NOT re-flag**: eliminative-materialist / hard-nosed-physicalist / MWI-defender disagreements at the framework boundary; the uncomputable-vs-intractable distinction depending on interactionist dualism; §9 ensoulment scope-contraction (partial-survival); §10's three counterarguments as honest in-framework (Mode-One) replies; §7 speculative-integration-tier examples (Higgs vacuum, prayer-equivalent effects, responsive arena dynamics).
- **Do NOT restore "Asphaug" or the Mørch N&BR cite** (confirmed fabricated/misattributed 2026-06-02).
- Article is highly converged (now seven reviews). Convergence damping plus the 14-day exclusion should keep it out of routine selection; this pass found no critical *content* issues, only References-hygiene artifacts and an outstanding physics-cite web-verify debt — both now cleared.

## What This Pass Did NOT Do

- Did not grow the article (3732 → 3712 words; net −20 from orphan-ref removal; well under 4000 hard).
- Did not re-flag any bedrock disagreement or §7/§9/§10 framing.
- Did not modify body argument content (References-block + one diacritic only).
- Did not commit (cycle_post / agent-commit handles it).
