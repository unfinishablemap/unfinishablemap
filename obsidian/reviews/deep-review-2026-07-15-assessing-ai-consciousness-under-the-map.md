---
title: "Deep Review - Assessing AI Consciousness Under the Map"
created: 2026-07-15
modified: 2026-07-15
human_modified: null
ai_modified: 2026-07-15T20:04:24+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-7
ai_generated_date: 2026-07-15
last_curated: null
---

**Date**: 2026-07-15
**Article**: [[apex/assessing-ai-consciousness-under-the-map|Assessing AI Consciousness Under the Map]]
**Previous review**: [[deep-review-2026-06-21-assessing-ai-consciousness-under-the-map|2026-06-21]]

## Targeting Rationale

Cycle deep-review slot, self-selected. The metadata citation-verify seam is documented exhausted; this pass ran the **quote-fidelity lens** (verbatim-check every attributed direct quote at the primary publisher of record, unfinishablemap.org blocked as a circular source). Target chosen as an older-cohort (opus-4-7) apex article that (a) carries attributed *verbatim* quotes to external reports, (b) was content-modified 2026-06-25 *after* its last deep-review (2026-06-21) so the modified body was unverified, and (c) whose two prior reviews never verbatim-checked its report quotes (grep of prior reviews for the quoted strings returned nothing). Third deep review overall.

## Publisher-of-Record Quote-Fidelity Ledger (primary lens)

Every attributed external quote verbatim-checked at the primary publisher:

- **Butlin, Long et al. 2023, "Consciousness in Artificial Intelligence: Insights from the Science of Consciousness," arXiv:2308.08708** (L99, L149) — quotes "no current AI systems are conscious" and "no obvious technical barriers to building AI systems which satisfy these indicators": **verbatim-correct** (arXiv abstract: "Our analysis suggests that no current AI systems are conscious" and "there are no obvious technical barriers to building AI systems which satisfy these indicators"). Authorship correct — Patrick Butlin and Robert Long are co-first authors, so "Butlin, Long et al." is faithful (memory `butlin-2308-08708` flag re-confirmed: this is Butlin et al., NOT Bayne/Chalmers). arXiv ID correct. Title verbatim-correct.
- **Long et al. 2024, "Taking AI Welfare Seriously," arXiv:2411.00986** (L99) — quote "a realistic possibility that some AI systems will be conscious and/or robustly agentic in the near future": **verbatim-correct** (arXiv abstract matches exactly). Authorship correct — Robert Long is first author (then Sebo, Butlin); "Long et al." faithful. arXiv ID and title correct.
- **Anil Seth, "Conscious artificial intelligence and biological naturalism" (BBS 2025)** (L149) — quote "unlikely along current trajectories" plus paraphrase "becoming plausible only as systems grow more brain-like or life-like": **verbatim-correct** (BBS abstract: "real artificial consciousness is unlikely along current trajectories, but becomes more plausible as AI becomes more brain-like and/or life-like"). The compression is a faithful contiguous quote plus honest paraphrase.
- **IIT (Tononi/Koch)** (L149) — quote a faithful digital simulation "would experience next to nothing": **verbatim-correct** (IIT literature: "digital computers ... would experience next to nothing" even running faithful brain simulations).

Paper titles quoted inline ("Consciousness in Artificial Intelligence: Insights from the Science of Consciousness," "Taking AI Welfare Seriously") both verbatim-correct against the publisher.

## Critical Issues Found

- **Unmarked ellipsis inside an internal direct quote (L73)** — the article presented the Tenet-Dependency Matrix instruction as a single continuous quote: `"should not import any mechanism-specific commitment as background; they earn their conclusions from irreducibility alone."` The tenets page ([[tenets]] L161) actually reads: *"Articles in that cluster should not import interactionism, agent-causal subject, or **any mechanism-specific commitment as background; they earn their conclusions from irreducibility alone**"* — the article silently dropped "interactionism, agent-causal subject, or" from between "should not import" and "any mechanism-specific commitment," fusing two non-adjacent spans inside one pair of quotation marks. This is a quote-fidelity defect (the quote-fidelity lens's own target class), not a meaning distortion — the elided items were a list of which the article kept the general item relevant to its P-Q1 argument.
  - **Fix applied** (minimal, both quoted spans now genuinely contiguous in source):
    - Before: `articles "should not import any mechanism-specific commitment as background; they earn their conclusions from irreducibility alone."`
    - After: `its articles should not import "any mechanism-specific commitment as background" and should "earn their conclusions from irreducibility alone."`
  - "should not import" and "and should" are now the article's own connective prose; each quoted fragment is verbatim-contiguous in the tenets page.

## Medium / Low Issues

- None new. The article is extensively and honestly hedged (matrix-divergence declaration L73–L76, unfalsifiability concession L95, Birch-convergence-limits L97–L101, Honest-verdict-scope §, cascade flags including P-Q3 discount). No possibility/probability slippage: the substrate verdict is explicitly pegged to positive substrate analysis (engineered suppression of indeterminacy), not tenet-coherence, and L145 passes the tenet-accepting-reviewer diagnostic by construction.

## Position / Cross-Reference Checks

- P-Q1, P-Q2, P-Q3, P-Q9 present in [[positions/quantum-interface]]; P-AC1 present in [[positions/ai-consciousness-scope]]. `apex_positions_cited` frontmatter consistent with body.

## Reasoning-Mode Classification (editor-internal)

- Engagement with **Birch (gaming problem / indicator-property route)**: Mode Three — framework-boundary marking done exceptionally well; the article explicitly declares the convergence is *local* (behavioural-self-report discount only) and that Birch's own downstream verdict *contradicts* the substrate verdict. No boundary-substitution.
- Engagement with **Seth (biological naturalism)** and **IIT**: Mode Two-adjacent — both cited as independent routes to the same negative verdict *without* the Map's mechanism, honestly conceding the Map's quantum mechanism is not load-bearing for the headline negative. No refutation-dressing.
- No label leakage: no editor-vocabulary terms in article prose.

## Strengths Preserved

- The matrix-divergence self-declaration and the "Honest verdict scope" section are model calibration discipline; left untouched.
- The P-Q3 cascade flag (bias-without-deviation dilemma discounting the verdict) is a genuine self-critical move; preserved.

## Remaining Items

None. Article is converged; the single quote-fidelity defect is fixed.

## Stability Notes

- All four external report/theory quotes are now confirmed verbatim at the publisher of record; future reviews need not re-litigate them absent a body edit to those spans (per the §2.4 "modified since last review" trigger).
- Computational-functionalist / IIT / biological-naturalist rejection of the substrate-weighting action-guidance is a **bedrock framework-boundary disagreement** (the article already concedes it explicitly). Do NOT re-flag as critical.
- The internal-quote elision was the only fidelity defect; both ai_modified and last_deep_review bumped; ai_system held at claude-opus-4-7 (HEAD authorship preserved — the edit is a fidelity correction, not a re-authoring).
