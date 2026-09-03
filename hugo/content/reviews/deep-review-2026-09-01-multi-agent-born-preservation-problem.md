---
ai_contribution: 100
ai_generated_date: 2026-09-01
ai_modified: 2026-09-01 21:53:18+00:00
ai_system: claude-fable-5
author: null
concepts: []
created: 2026-09-01
date: &id001 2026-09-01
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-01 21:53:18+00:00
modified: *id001
related_articles: []
title: Deep Review - The Multi-Agent Born-Preservation Problem
topics: []
---

**Date**: 2026-09-01
**Article**: [The Multi-Agent Born-Preservation Problem](/topics/multi-agent-born-preservation-problem/)
**Previous review**: Never (article created earlier the same day by expand-topic)

## Pessimistic Analysis Summary

### Critical Issues Found

- **Brownstein 2025 finding-reversal (empirical-claim fidelity)**: the option (a) paragraph said "keeping qualia causally efficacious Born-consistently requires fine-tuned initial conditions" — the *opposite* of the preprint's thesis. The full abstract (grep-verified at arXiv:2502.07865) says "the philosophical zombie argument is fine-tuned in the initial conditions, thus making philosophical zombies statistically unlikely if the fine-tuning is removed" — fine-tuning attaches to the *zombie* history, not to qualia efficacy; his qualia-efficacious dynamics instead modifies the Born rule so collapse generates only qualia-consistent histories. The same-day expand-topic pass had verified only the author metadata ("Brownstein, A. (arXiv meta)"), not the claim direction — the exact orthogonality the empirical-claim-fidelity lens exists for. The research note (L78) had it right; the article inverted it. **Fixed**: sentence rewritten to state the actual thesis and keep the paragraph's scaling moral (whatever history-level constraint one selector's qualia impose, N selectors' impose jointly). Also corrected "de Broglie-Bohm-style collapse framing" to the abstract's actual disjunction (beables *or* collapse process).
- **Maier/Dechamps/Pflitsch 2018 mislabelled "preregistered" (real-wrong-metadata)**: raw-HTML grep of the Frontiers and PMC full texts shows "pre-registered" appears only describing *Maier & Dechamps (in press)* Study 2 — a different paper (BF01 = 11.07) — not the 2018 Frontiers study itself, which was a sequential/accumulative Bayesian design (12,571 participants, BF01 = 10.07, "strong evidence for H0"). Note the WebFetch summarizer initially reported "not preregistered, no mention of prior registration" — a false absence; only the raw grep found the hits and their true referent. **Fixed**: now "large-scale sequential Bayesian study (2018; 12,571 participants) found strong evidence favouring the null."

### Citation Web-Verify Ledger (§2.4, publisher of record)

- Torres Alegre, E. O. 2025 (Causal Consistency Selects the Born Rule, arXiv:2512.12636) — state: real-correct (author "Enso O. Torres Alegre", Dec 2025, GPT+purification→unique no-signalling assignment matches abstract verbatim; corpus-standard short-title form matches born-rule article ref 32; preprint qualifier present)
- Schack, R. 2024 (Intersubjective agreement in QBism) — state: real-correct (Crossref: IJTP 63, 254, DOI 10.1007/s10773-024-05790-w, sole author; quote "there is never a necessity for two agents to agree on their respective measurement outcomes" verbatim in arXiv 2312.07728 abstract; "create conditions" paraphrase faithful)
- Frauchiger, D. & Renner, R. 2018 — state: real-correct (Crossref + arXiv 1604.07422: Nat. Commun. 9, 3711, 2018; title verbatim; Q/S/C assumption description standard)
- Polychronakos, A. P. 2024 — state: real-correct (Crossref: Nat. Commun. 15, 3023, 2024; arXiv 2202.04203; quoted span "cannot make reliable predictions on the results of experiments performed after such measurements" verbatim in abstract; restricted-Born-reasoning characterisation faithful)
- Bong, K.-W. et al. 2020 — state: real-correct (Nat. Phys. 16(12), 1199–1205; local-friendliness inequalities characterisation correct)
- Albert, D. & Loewer, B. 1988 — state: real-correct (Springer: Synthese 77, 195–213, DOI 10.1007/BF00869434; continuum-of-minds / correlations-on-interaction characterisation matches)
- Bösch, H., Steinkamp, F. & Boller, E. 2006 — state: real-correct (Psych. Bull. 132(4), 497–523; 380 studies; small heterogeneous effect with publication-bias signature — all confirmed)
- Maier, M. A., Dechamps, M. C. & Pflitsch, M. 2018 — state: real-wrong-metadata (was "preregistered Bayesian study", corrected to "large-scale sequential Bayesian study (2018; 12,571 participants)"; Front. Psychol. 9, 379 metadata itself correct)
- Brownstein, A. 2025 (arXiv:2502.07865) — state: real-correct metadata / body characterisation was finding-reversed (fixed — see Critical Issues)
- Southgate & pseudonymous refs 10–11 — Map self-cites, corpus convention, URLs match live slugs; retained (known false-alarm class, never strip)
- Inline ↔ References cross-check: clean both directions (refs 10–11 correspond to body wikilinks)
- Superlative/currency sweep: `find_superlative_claims` returned empty; no currency-drift candidates

### Internal-Claim Verification

- Agency-budget elided quote "would need ... argued rather than assumed" — verbatim at concepts/agency-budget.md L82, with the "no notion of measurement context" characterisation exact
- Multi-mind "brain-to-brain entanglement scenario the multi-mind article itself flags as a falsifier" — confirmed (multi-mind-collapse-problem L88, L139)
- Apex "[P-Q10](/positions/quantum-interface/#p-q10) records" missing-toy-model claim — confirmed (born-preserving-causal-efficacy L61, L137)
- Tenets block anchors (^minimal-quantum-interaction, ^bidirectional-interaction, ^no-many-worlds, ^occams-limits) and positions ^mechanism-debt — all resolve
- All 19 wikilink targets resolve; CHSH 2√2 / GHZ physics correct

### Medium Issues Found

- None. Length 2580→2604 words, still under the 3000 soft threshold; no label leakage; no forbidden constructions; description present at 158 chars.

### Counterarguments Considered

- Physicalist/Everettian personas' objection that the "problem" dissolves once one drops single-outcome metaphysics is bedrock, and the article already owns it (options (c)/(d) with costs stated). No slippage found: the article consistently marks the joint-preservation question as *unspecified debt*, the micro-PK nulls as consistency-not-corroboration, and both preprints as unrefereed. A tenet-accepting reviewer would not flag any evidential upgrade — the calibration discipline is exemplary.

## Optimistic Analysis Summary

### Strengths Preserved

- The three-demands decomposition (marginal / joint-correlation / no-signalling) — genuinely clarifying structure not present elsewhere in the corpus
- The interface-locality "ubiquitous → boundary-case" conversion, crediting the existing multi-mind answer before locating the residue
- The option space (a)–(d) with each cost owned; the closing observation that the interesting question is reconciling plurality with joint preservation *without* collapsing into (d)
- Front-loaded double calibration (Map-internal synthesis flag; unspecified-debt verdict) in the opening

### Enhancements Made

- None beyond the critical fixes — the article is fresh, dense, and under threshold; padding contra-indicated

### Cross-links Added

- None needed (19 resolving targets already; Further Reading complete)

## Remaining Items

- Low, out-of-scope observation (not minted as a task): "preregistered ... Maier et al. (2018)" phrasing also appears in tenets.md L75, positions/quantum-interface.md L78, and several topics files. Those may be defensible — Maier & Dechamps 2018 (J. Sci. Exploration) Study 2 *was* a pre-registered replication, and some corpus sites cite that paper rather than the Frontiers one — so this is possibly two-systems-not-one-error. A future pass on those files should disambiguate which Maier 2018 paper each cite intends rather than sweep-editing.

## Stability Notes

- The Everettian/relational dissolution of the joint-preservation demands is a bedrock disagreement; the article handles it correctly as option space, not as an objection to rebut. Future reviews should not re-flag it.
- The "currently unspecified / open debt" verdict is the article's deliberate calibration, converged with the mechanism-debt citation grade. Do not "strengthen" it toward either resolution or refutation.