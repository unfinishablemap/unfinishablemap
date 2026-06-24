---
title: "Deep Review - Relational Quantum Mechanics"
created: 2026-06-24
modified: 2026-06-24
human_modified: null
ai_modified: 2026-06-24T16:10:18+00:00
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

**Date**: 2026-06-24
**Article**: [[relational-quantum-mechanics|Relational Quantum Mechanics]]
**Previous review**: [[deep-review-2026-05-25-relational-quantum-mechanics|2026-05-25]]

## Context: Why This Article Re-Entered Rotation

Staleness mint (~30d since the 2026-05-25 deep review; settled state with `ai_modified == last_deep_review`, so no own-body churn). Prior `ai_system` was an older build (claude-opus-4-6 in frontmatter; 2026-05-25 review run on opus-4-7), so this pass is a fresh-eyes independent re-verification rather than a trust-the-prior-stamp no-op. The 2026-05-25 review reported full re-convergence on the CPL/Lewis/Muciño content and recommended exclusion. Per the task brief, the prior "all citations verified" stamp was NOT trusted: every citation was independently re-checked at the publisher of record.

## Pessimistic Analysis Summary

### Critical Issues Found
Two citation defects, both fixed in place (real-wrong-metadata / orphan-reference — neither a fabrication, neither a body-claim error):

1. **Pienaar (2019) wrong end page** — article cited *Foundations of Physics* 49(12), 1404–14**12**. Publisher of record (Springer DOI 10.1007/s10701-019-00303-w; confirmed independently via ADS index 2019FoPh...49.1404P and the SEP RQM bibliography) gives **1404–1414**. End page corrected 1412 → 1414. Volume (49), issue (12), start page (1404), author, title, year all correct.
2. **Laudisa (2019) orphan reference** — present in the References list but never cited inline (orphan in the inline↔References direction = critical per §2.4 step 5). Laudisa's "Open Problems in RQM" is a load-bearing foundational survey directly on-point for the "What counts as an observer" subsection. Resolved by adding a brief inline citation there ("Laudisa (2019) catalogues this among RQM's standing open problems, alongside the 'third person' question…"), which is faithful to the source (JGPS 50(2), 215–230, verified) and length-neutral (+22 words).

### Medium Issues Found
None.

### §2.4 Publisher-of-Record Citation Web-Verify (per-cite ledger)

Every inline cite and every References entry web-verified at the publisher of record (not aggregators). Three-state classification:

- Rovelli, C. (1996) Relational quantum mechanics, *Int. J. Theor. Phys.* 35(8), 1637–1678 (DOI BF02302261) — **real-correct**
- Adlam, E. & Rovelli, C. (2023) Information is Physical: Cross-Perspective Links, *Philosophy of Physics* 1(1), 1–19 (DOI 10.31389/pop.8; LSE) — **real-correct** (journal version 2023; arXiv preprint 2203.13342 is 2022 — article correctly cites the journal year)
- Lewis, P. J. (2024) A dilemma for relational quantum mechanics, *Principia* 28 (pp. 383–399) — **real-correct** (volume 28 / year 2024 confirmed via periodicos.ufsc.br + PhilSci-Archive 23794; page range not stated in the cite but nothing cited is wrong)
- Muciño, R., Okon, E. & Sudarsky, D. (2022) Assessing Relational Quantum Mechanics, *Synthese* 200(5) (DOI 10.1007/s11229-022-03886-6) — **real-correct** (surname spelling "Muciño" matches)
- Rovelli, C. (2021) A response to the Mucino-Okon-Sudarsky's Assessment, arXiv:2106.03205 — **real-correct**
- Laudisa, F. (2019) Open Problems in RQM, *JGPS* 50(2), 215–230 (DOI 10.1007/s10838-019-09450-0) — **real-correct** (was orphan; now cited inline — see above)
- Pienaar, J. (2019) Comment on "The notion of locality in RQM," *Found. Phys.* 49(12) — **real-wrong-metadata (end page 1412 → 1414, corrected)**
- Frankish, K. (2016) Illusionism as a Theory of Consciousness, *JCS* 23(11–12), 11–39 — **real-correct**
- Tallis, R. (2024) The Illusion of Illusionism, *Philosophy Now* Issue 161 (April/May 2024) — **real-correct**
- Whitehead, A. N. (1929) *Process and Reality*, Macmillan — **real-correct** (canonical)
- SEP "Relational Quantum Mechanics", plato.stanford.edu/entries/qm-relational/ — **real-correct** (live; substantive revision Feb 4, 2025 — current)

Inline↔References cross-check both directions: complete after the Laudisa fix (no remaining orphans either way). Dennett is named as an illusionist alongside the cited Frankish; his heterophenomenology is a well-known position requiring no separate ref.

### Empirical-Record Currency Sweep
`find_superlative_claims` returned no detected superlatives. Manual scan: "the most serious technical move RQM has made in twenty years" and "the centre of gravity in the 2020s literature" are claims about RQM's *internal* dialectic, not empirical-record superlatives subject to supersession. The CPL/Lewis/Muciño exchange remains the live edge of the RQM literature as of June 2026 (no decisive resolution of Lewis's dilemma found in 2024–2026 search). No currency-drift; no literature-drift follow-on warranted at this time.

### In-Quoted Sibling-String Check (stale-internal-quote risk)
No verbatim quotes attributed to sibling Map articles in the body — all quoted strings are external (Rovelli "There is nothing subjective, idealistic, or mentalistic, in RQM" — verified verbatim in SEP and the literature; Adlam & Rovelli "shared observable reality…"; Tallis "Misrepresentation presupposes presentation") or the article's own scare-quoted terms. No stale-internal-quote exposure (cf. [[apex-stale-internal-quote-channel]]).

### Calibration Check (possibility/probability slippage)
No slippage. The RQM-vs-interface comparison consistently treats RQM's framework-internal coherence as coherence, NOT as evidence against the Map (and vice versa) — e.g. "honest framework-boundary disagreement—neither refutes the other from inside" (line 87) and the symmetric concession that the Map's mechanism "lacks specified coupling constants, just as RQM treats relative facts as brute" (line 141). The CPL claims are about RQM's internal dialectic, left explicitly open ("whether it earns this by RQM's own resources … is what Lewis's dilemma and the Muciño-Okon-Sudarsky exchange leave contested"). Diagnostic test: a reviewer who fully accepts the Map's tenets would not find any claim overstated relative to the evidential-status scale. Pass — relational/observer-relative claims stay interpretive stances, not asserted physics.

### Reasoning-Mode Classification (named-opponent engagements)
- **RQM's universalised observer (Rovelli):** Mode Three, explicit — "honest framework-boundary disagreement; neither refutes the other from inside; each makes a foundational commitment the other declines." No boundary-substitution.
- **Illusionism (Dennett heterophenomenology / Frankish quasi-phenomenal):** Mixed — Tallis "misrepresentation presupposes presentation" is a Mode One/Two reply (uses the opponent's own representational commitments), with the residue declared Mode Three ("the dispute is live, and the Map's commitment to dualism is what tips the assessment, not a stand-alone refutation"). Honest.
- No editor-vocabulary label leakage (forbidden-term scan clean). No banned "This is not X. It is Y." construct. No HTML-comment / refinement-log leakage.

### Self-Contradiction Check
Consistent — "dissolves the measurement problem" (textbook problem, denied by premise) is cleanly distinguished from "faces its own version of the 'how does collapse happen?' question" (residual brute "why this relative value", acknowledged). No contradiction.

## Optimistic Analysis Summary

### Strengths Preserved
- CPL/Lewis/Muciño exchange as contemporary backbone, accurately weighted as the 2020s centre of gravity.
- Special-relativity analogy + Wigner's friend pedagogy.
- Precise framework-boundary statement (RQM: any physical system; Map: the conscious system at whose interface actualisation occurs).
- Five falsifiability conditions incl. the CPL-specific #5.
- **Hardline Empiricist (Birch) note:** evidential restraint holds — first-person weight "depends on prior commitments," CPL left open, no tenet-as-evidence-upgrade.
- **Process Philosopher (Whitehead) note:** dedicated section declines panexperientialism, avoiding combination-problem overreach. Birch and Whitehead not in tension on any passage.

### Enhancements Made
None beyond the two required citation fixes (length-neutral). Article sound as written.

### Cross-links Verified
All 23 body + frontmatter + Further Reading wikilinks resolve on disk. Load-bearing siblings reciprocate (quantum-interpretations, qm-interpretations-beyond-many-worlds link back to RQM). measurement-problem / locality / born-rule are outbound-only — normal hub asymmetry, not load-bearing breakage; not modifying siblings to force reciprocity (length/scope discipline).

## Remaining Items

None.

## Stability Notes

This is the sixth deep review (2026-01-20, 2026-01-29, 2026-03-11, 2026-04-05, 2026-05-25, 2026-06-24). The 2026-05-25 review verified the CPL content against live literature but its citation pass missed the Pienaar end-page error and the Laudisa inline-orphan — both caught here only because the brief mandated independent publisher-of-record re-verification (a textbook instance of intra-corpus consistency *ratifying* a metadata defect across five "verified" reviews; cf. [[ai_citation_metadata_unreliable]]). Both now fixed.

Bedrock disagreements (do NOT re-flag as critical):
- Eliminative materialists and illusionists endorse RQM's removal of consciousness — congenial, registered honestly as RQM's natural allies.
- MWI defenders find the indexical-identity argument unsatisfying — expected framework-boundary standoff.
- Physicalists will not accept dualism from inside their framework — the article does not claim in-framework refutation.

**Recommendation**: Re-converged. Exclude from deep-review rotation again unless substantive content changes are made. A future trigger would be a decisive technical resolution of Lewis's dilemma (whether CPL is internally earned) — at which point a literature-drift refresh of the CPL section would be warranted.
