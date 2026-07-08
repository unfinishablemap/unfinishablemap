---
title: "Deep Review - Research Programme Decisions Under the Map"
created: 2026-07-08
modified: 2026-07-08
human_modified: null
ai_modified: 2026-07-08T09:13:51+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-8
ai_generated_date: 2026-07-08
last_curated: null
---

**Date**: 2026-07-08
**Article**: [[apex/research-programme-decisions-under-the-map|Research Programme Decisions Under the Map]]
**Previous review**: Never (this is the first genuine deep-review; `last_deep_review` was set to 2026-06-16 by apex-evolve at creation, but no review file existed — phantom review-debt of the kind noted in the coalesce/refine review-debt pattern)

## Selection Rationale

Selected as a genuinely unverified target: **0 prior deep-review files** despite a `last_deep_review` timestamp, 12-line References/citation load, applied-apex on the quantum-interface research directions (Tenet 2 / Tenet 3 load-bearing), and 6.3 days of unverified drift since the phantom review date. Fresh, citation-heavy, never-genuinely-reviewed content is exactly where a defect tail is expected (per the fresh-create-defect-tail pattern), and the review found one: a cluster of citation cross-reference orphans plus a corpus-propagated misattribution.

## Pessimistic Analysis Summary

### Critical Issues Found

**Citation cross-reference orphans (§2.4 step 5)** — the article's single defect cluster:

- **Orphan inline cite** `Babcock-Hameroff (2025)` (Direction 2) — cited inline, no References entry. **Also a misattribution**: there is no joint "Babcock-Hameroff 2025" paper. The genuine contestant of Tegmark's microtubule-decoherence calculation is **Hagan, Hameroff & Tuszynski (2002)** (*Phys. Rev. E* 65:061901); the real Babcock lead paper is the **2024** tryptophan-superradiance work (*J. Phys. Chem. B* 128(17):4035-4046). The corpus changelog already documents "Babcock-Hameroff (2025)" as a famous-name-substitution defect (elsewhere resolved to Wiest 2025 in the born-rule context). **Fix**: removed the misleading bare author-year and routed the citation through the [[falsification-roadmap-for-the-interface-model|falsification roadmap]] link (an apex properly defers detailed cites to its source articles).
- **Four orphan References** (in the References list, never cited inline):
  - **Torres Alegre (2025)**, arXiv:2512.12636 — real-correct, and sharply relevant. It underwrites the no-signalling↔Born-preservation constraint that is load-bearing for the toy-model direction (this is the same result P-Q7 of the quantum-interface register cites). **Fix**: wired inline in Direction 1, grounded exactly as the register uses it.
  - **Chalmers & McQueen (2022)**, Gao (Ed.) *Consciousness and Quantum Mechanics*, OUP — real, but tangential to this applied prioritisation piece and its page range (11-63) could not be confirmed at publisher of record this pass. **Fix**: removed (still cited in sibling articles; no corpus loss).
  - **Zheng & Meister (2025)**, *Neuron* 113(2):192-204 — real-correct, but off-topic residue (10-bits/s cognitive throughput has no home in a research-prioritisation piece). **Fix**: removed.
  - **Schurger, Sitt & Dehaene (2012)**, *PNAS* 109(42):E2904-E2913 — real-correct, but off-topic residue (readiness-potential accumulator model, no inline home). **Fix**: removed.

### Publisher-of-Record Citation Ledger (§2.4)

Every reference and inline cite web-verified at publisher of record this pass:

- Donadi, S. et al. (2021), *Nature Physics* 17, 74-78 — **real-correct** (ADS 2021NatPh..17...74D; arXiv:2111.13490). Cited inline (Direction 3, Decision 4).
- Tegmark, M. (2000), *Phys. Rev. E* 61(4), 4194-4206 — **real-correct** (APS DOI 10.1103/PhysRevE.61.4194). Cited inline (Direction 2).
- Maier, M. A., Dechamps, M. C. & Pflitsch, M. (2018), *Frontiers in Psychology* 9, 379 — **real-correct** (DOI 10.3389/fpsyg.2018.00379; PubMed 29619001). Cited inline (Direction 2, Decision 4).
- Torres Alegre, E. O. (2025), arXiv:2512.12636, "Causal Consistency Selects the Born Rule…" — **real-correct** (arXiv PDF confirmed). Was orphan → now cited inline (Direction 1).
- Chalmers, D. J. & McQueen, K. J. (2022), in Gao (Ed.), OUP — **real-correct on author/year/title/venue** (OUP DOI 10.1093/oso/9780197501665.003.0002; PhilPapers CHACAT-24); page range 11-63 unconfirmed at publisher this pass. **orphan → removed**.
- Zheng, J. & Meister, M. (2025), *Neuron* 113(2), 192-204 — **real-correct** (Cell S0896-6273(24)00808-0). **orphan → removed**.
- Schurger, A., Sitt, J. D. & Dehaene, S. (2012), *PNAS* 109(42), E2904-E2913 — **real-correct** (PNAS DOI 10.1073/pnas.1210467109; PMID 22869750). **orphan → removed**.
- `Babcock-Hameroff (2025)` inline — **no such paper (misattribution)**; correct works are Hagan-Hameroff-Tuszynski (2002) [Tegmark rebuttal] and Babcock et al. (2024) [superradiance]. **orphan inline → removed / rerouted**.

No metadata errors in the surviving references; all defects were cross-reference orphans and one propagated phantom-author cite.

### Family Resolution (§2.4 step 6) — corpus-wide propagation

The `Babcock-Hameroff (2025)` phantom cite was propagated across three live files. Fixed each to its context-appropriate verified form and bumped `ai_modified` on every edited file:

- `apex/research-programme-decisions-under-the-map.md` — rerouted through the roadmap link.
- `topics/falsification-roadmap-for-the-interface-model.md` (summary table) — "contested by Babcock-Hameroff 2025" → "contested by **Hagan-Hameroff-Tuszynski 2002**" (the genuine decoherence-calc rebuttal).
- `topics/testing-consciousness-collapse.md` — "Babcock-Hameroff microtubule evidence (2025)" → "**Babcock et al. microtubule superradiance evidence (2024)**" (the real experimental paper).

### Internal-Quote / Attribution Check (§2.5)

Apex quoting the positions register — verified every quoted band and shift-condition against `positions/quantum-interface.md`:

- P-Q1 **moderate**, P-Q3 **moderate**, P-Q6 **high**, P-Q9 **moderate**, P-Q10 **high** — all match the register exactly.
- Quoted shift-conditions (P-Q10 "were a worked toy model to appear… tighten by one band"; P-Q3 mechanism-debt/bias-without-deviation wording; P-Q4/P-Q5 coherence-time shift-conditions; P-Q9 aggregate-channel self-concealment scoping) — all faithful.
- No stale internal-quote drift (apex-stale-internal-quote channel clean).
- No source/Map conflation; no overstated positions; the piece is scrupulously scoped ("internal to the Map," "licenses a *prioritisation*, not a guarantee").

### Calibration Check (possibility/probability slippage)

Clean. The article is explicitly pegged to the [[evidential-status-discipline]] and repeatedly refuses to upgrade evidential status on tenet-load: the "Honest verdict scope" section states the ranking "is not a claim about what the wider field… should prioritise" and that a tenet-rejecting researcher "has no reason to weight a toy model… above… a decoherence-only resolution." A tenet-accepting reviewer would not flag any claim as overstated relative to the five-tier scale.

## Optimistic Analysis Summary

### Strengths Preserved
- The band-movement decision principle (value tracks how much a feasible result would move a confidence band or discharge a standing debt) is a genuinely original, operational use of the positions register as a *research-priority map*.
- The symmetry argument for coherence-time calculations ("it pays whichever way it comes out") is a clean articulation of decision-relevance vs. confirmation-seeking.
- The self-concealment pruning principle (do not spend effort where the framework has pre-committed to a null) is a distinctive, correctly-scoped contribution.
- The "Cascade flags" and "Honest verdict scope" sections are model calibration hygiene and were left untouched.

### Enhancements Made
- Torres Alegre (2025) wired into Direction 1 to ground the no-signalling↔Born-preservation constraint (adds explanatory value: it explains *why* a no-signalling-respecting bias is pushed toward Born preservation).

### Cross-links
- No new cross-links needed; the apex is densely and correctly linked to its sources and the positions register.

## Length

Body 2961 → 2921 words (73% of the 4000-word apex soft threshold). Length-neutral: one inline clause added (Torres Alegre), three orphan references removed. Comfortably within ceiling.

## Remaining Items

None. The applied-apex structure is intact (5 positions cited: P-Q1/Q3/Q6/Q9/Q10; "What this implies for decisions" section present). Required "Relation to Site Perspective" section present and substantive.

## Stability Notes

- This was the first genuine deep-review; the citation cross-reference orphans were the expected fresh-create defect tail. The surviving citation set is now fully web-verified and inline↔References-consistent, so future reviews should not re-verify absent a new flag.
- The `Babcock-Hameroff (2025)` phantom author-year is a **famous-name-substitution defect** the corpus is prone to. It has now been swept from all three live-content files. Future edits should not reintroduce it: the Tegmark decoherence rebuttal is **Hagan, Hameroff & Tuszynski (2002)**; the microtubule superradiance evidence is **Babcock et al. (2024)**; the born-rule entanglement-witness quote is **Wiest (2025)** — three distinct real works, none a joint "Babcock-Hameroff 2025."
- The register-band quotes (P-Q1/Q3/Q6/Q9/Q10) are faithful as of the register's current state; if the register re-bands (especially P-Q10 on a toy-model appearance), this apex must re-read — the article flags this itself in "Cascade flags."
- Bedrock disagreement (a physicalist/decoherence-only researcher rejecting the whole prioritisation) is expected and honestly declared by the article; not a defect.
