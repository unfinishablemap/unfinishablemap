---
ai_contribution: 100
ai_generated_date: 2026-06-20
ai_modified: 2026-06-20 00:00:00+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-20
date: &id001 2026-06-20
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[stapp-quantum-mind]]'
title: Deep Review - Stapp's Quantum Mind Model
topics: []
---

**Date**: 2026-06-20
**Article**: [Stapp's Quantum Mind Model](/concepts/stapp-quantum-mind/)
**Previous review**: [2026-05-31](/reviews/deep-review-2026-05-31-stapp-quantum-mind/) (deep, 8th pass)
**Context**: GENUINE-DRIFT verification pass. `last_deep_review` 2026-05-31; `ai_modified` 2026-06-18 (drift commit `9f15ad12d` "Decoherence-timescale brain-side pass" rewrote the Monte Carlo critique paragraph with NEW specific claims AND added a brand-new References entry). Citation-defect-prone article (defect history: 2026-05-27 overclaims/orphan-refs fix; Denton article-number fix; once-fabricated "Meister 2024 PNAS" orphan). Mandate: web-verify the new Georgiev 2015 cite FIRST at publisher of record, then every external cite + full inline↔References integrity, the rewritten Monte Carlo paragraph's calibration, and currency.

## Citation Web-Verify Ledger (§2.4, publisher of record)

Per-cite verification ledger. The drift commit's new claims and the article's defect history warranted re-verifying the whole external set, not just the new entry.

- **Georgiev, D.D. (2015). Monte Carlo simulation of quantum Zeno effect in the brain. *Int. J. Mod. Phys. B* 29(7), 1550039. arXiv:1412.4741** — **state: real-correct.** PRIMARY VERDICT (task item a). Verified against arXiv journal-ref ("International Journal of Modern Physics B 2015; 29 (7): 1550039"), DOI 10.1142/S0217979215500393, and the World Scientific / ADS records. Author (Danko D. Georgiev), title, journal, vol 29, issue 7, article-number 1550039, year 2015, and arXiv id 1412.4741 ALL exact. The "2014" appearing in some aggregator summaries is the arXiv submission date (11 Dec 2014), not the publication year. **The decoherence-free-subspace argument attributed to it is FAITHFUL**: the publisher abstract confirms verbatim that Georgiev (i) modeled "quantum tunneling of an electron in a multiple-well structure such as the voltage sensor in neuronal ion channels," (ii) found "the quantum Zeno effect breaks down for timescales greater than the brain decoherence time," and (iii) "leaves a door open for future development of quantum mind theories provided the brain has a decoherence-free subspace." All three article claims are accurate. (Corroborated by a prior corpus web-verify on quantum-state-inheritance-in-ai, changelog L460.)

- **Georgiev, D. (~~2014~~ → 2012). Mind efforts, quantum Zeno effect and environmental decoherence. *NeuroQuantology* ~~12(3)~~ → 10(3), 552** — **state: real-wrong-metadata (CORRECTED).** The paper is real and the projection-operators-without-wavefunction formal-inconsistency objection attributed to it (article L121) is faithful. But the article had **wrong year (2014→2012) AND wrong volume (12→10)** — a "+2 on both year and volume" drift. Decisive evidence: the canonical DOI `10.14704/nq.2012.10.3.552` (NeuroQuantology DOIs encode `nq.YEAR.VOLUME.ISSUE.PAGE`) resolves 302 → the live article page; ProQuest record confirms vol 10, issue 3, 2012, page 552. Corrected in-body (L121: "Georgiev (2012)") and in References to "Georgiev, D. (2012). … *NeuroQuantology*, 10(3), 552." **Family-resolution (§2.4)**: the same wrong metadata lived in the source research note [research/stapp-mental-effort-mind-matter-2026-01-14.md](/research/stapp-mental-effort-mind-matter-2026-01-14/) (section header + reference line) — propagated the canonical 2012/10(3)/552 form there too.

- **Schwartz, J.M., Stoessel, P.W., Baxter, L.R., Martin, K.M., & Phelps, M.E. (1996). Systematic changes in cerebral glucose metabolic rate after successful behavior modification treatment of OCD. *Archives of General Psychiatry* 53(2), 109-113** — **state: real-correct, INLINE-ORPHAN FIXED.** Article L77 cited "(Schwartz et al., 1996)" for the PET-caudate result but the References list had NO Schwartz-1996 entry (only Schwartz & Begley 2002 and Schwartz/Stapp/Beauregard 2005). The 2026-05-31 orphan sweep checked References→inline; this is the inline→References direction it missed. Paper verified real and faithfully described (PET, caudate glucose-metabolism change after behavior therapy for OCD). Added the missing References entry.

- **Georgiev, D. (2014). [the NeuroQuantology entry] — see above (corrected to 2012).**
- **Hagan, S., Hameroff, S., & Tuszynski, J. (2002). Quantum computation in brain microtubules. *Phys. Rev. E* 65, 061901** — **state: real-correct.** Verified (PubMed PMID 12188753, ADS 2002PhRvE..65f1901H). The ordered-water / counter-ion Debye-layer screening argument at L113 is faithful.
- **Denton, M.C.J., et al. (2024). *Nature Communications* 15, 10823** — real-correct (re-confirmed 2026-05-31; unchanged). Cited descriptively at L113 ("in 2024, Nature Communications published evidence…") rather than by surname — anchored, acceptable.
- **Rajan et al. (2019) *Cerebral Cortex* 29(7), 2832-2843; Garrison et al. (2013) *Front. Hum. Neurosci.* 7, 440; Zheng & Meister (2025) *Neuron* 113(2), 192-204; Schwartz, Stapp & Beauregard (2005) *Phil. Trans. R. Soc. B* 360(1458), 1309-1327** — real-correct, all web-verified exact on 2026-05-31, unchanged since; not re-litigated.
- **In-body-only cites with no References entry by design** (acceptable — classics / descriptive): Tegmark (2000, 10⁻¹³ s figure, L111), James (1890, has entry), Rizzolatti PMTA (L87), Kane self-forming-actions (L101), Kral et al. (2022, L79), Schwartz et al. 1996 (now has entry). Tegmark has no entry here but is the canonical 10⁻¹³ s reference and cited only for that figure in-body; corpus canonical form is *Phys. Rev. E* 61(4), 4194-4206 — no defect, just not listed.

**Inline↔References integrity**: now COMPLETE in both directions. One inline-orphan (Schwartz 1996) found and fixed; no References-orphans (every list entry is cited in-body, Denton descriptively). No fabrications. No same-paper-divergent-metadata across the corpus after the NeuroQuantology fix.

## Calibration / Evidential-Status Pass (Tenet 2/3) — rewritten Monte Carlo paragraph (task item c)

The rewritten paragraph (L115) is **honestly calibrated; no possibility→probability slippage.** It reports Georgiev's breakdown conclusion faithfully, then accurately describes the decoherence-free-subspace escape hatch as "the narrower and still-open empirical question of whether neural tissue supplies such a protected subspace" and "unconfirmed." It treats Stapp's mechanism as a contested live hypothesis throughout, not as established. The DFS qualifier it leans on is genuinely in Georgiev's paper.

One honest-scoping note (NOT a defect): the paragraph omits the *stronger* half of Georgiev's result — the von Neumann-entropy no-go theorem (local projections cannot decrease the unconditional brain density matrix's entropy), which Georgiev uses to call Stapp's model "physically implausible." Omitting it **understates the critique's force against Stapp** rather than overclaiming for the Map, so it is a defensible scoping choice, not a calibration error. Left as-is. (A future optimistic/pessimistic pass could add the no-go theorem for completeness, but it is not required and would cost length on a soft-warning article.)

## Reasoning-Mode Discipline Check

- **Forbidden label leakage**: NONE (grep PASS). No "not X but Y" banned construct.
- Engagement classifications (editor-internal, unchanged from 2026-05-31): Epiphenomenalist — Mode One; Illusionist — Mode Two; MWI — Mode Three (framework-boundary, "the debate remains open"). The Georgiev formalism/Monte-Carlo critiques are honestly reported objections with open-debate framing, not boundary-substitution.

## Currency Sweep

`find_superlative_claims` returned EMPTY — no "current record/largest/latest/to date" claims to currency-check. Decoherence-timescale figures (Tegmark 10⁻¹³ s, revised 10⁻⁵ s, cryptochrome µs) internally consistent and current.

## Length

3008 words (120% of 2500 soft; soft_warning), 492 words below the 3500 hard threshold. Net change from this pass ≈ +25 words (one short References entry; metadata edits are number-swaps). Length-neutral satisfied; comfortably under hard.

## Pessimistic Summary

Two real citation defects caught this pass (Georgiev-NeuroQuantology wrong year+volume; Schwartz-1996 inline-orphan) — both correctable, both fixed. The drift commit's headline new content (Georgiev 2015 cite + DFS claim) is **fully verified clean and faithful** — the GENUINE-DRIFT verification confirms the drift was a legitimate, accurate improvement, not a fabrication or overclaim.

## Optimistic Summary

### Strengths preserved
- Front-loaded LLM-resilient lede; honest Schwartz-OCD evidence handling (small N, no independent replication, no ERP comparison); seven quantified falsifiable predictions with explicit attention-layer-vs-quantum-layer demarcation; cryptochrome "proof-of-concept, not precedent" reframe (settled-correct calibration — do not re-escalate).
- The newly-developed Georgiev-2015 DFS paragraph is a genuine improvement: it converts the decoherence objection from a blanket impossibility into a sharply-stated open empirical question, which is both more accurate and more useful.

### Enhancements made
- Citation-integrity hardening: corrected NeuroQuantology metadata corpus-wide; closed the Schwartz-1996 inline-orphan.

### Cross-links
None needed; densely linked already.

## Remaining Items

None requiring a follow-on. Optional future nicety: add Georgiev's von Neumann-entropy no-go theorem to the Monte Carlo paragraph for completeness (not required; would cost length).

## Stability Notes

Future reviews should NOT re-flag:
- **MWI singular-determination disagreement** — bedrock, framework-boundary.
- **Heterophenomenological symmetry of the effort-calibration argument** — already conceded in-text (~L127).
- **Corridor-vs-minimum-outside-corridor Born-rule fork** — held as a live fork by design.
- **Cryptochrome "proof-of-concept, not precedent for neural states"** — settled-correct calibration.
- **Georgiev 2015 (IJMPB 29(7) 1550039, arXiv:1412.4741)** — web-verified real-correct AND its DFS attribution faithful as of 2026-06-20; do not re-flag.
- **Georgiev 2012 NeuroQuantology 10(3) 552** — corrected from 2014/12(3) this pass; web-verified canonical via DOI 10.14704/nq.2012.10.3.552. Do not let it drift back to 2014/12(3).
- **The fabricated "Meister 2024 PNAS"** — gone for good; correct bandwidth cite is Zheng & Meister 2025, *Neuron* 113(2), 192-204.