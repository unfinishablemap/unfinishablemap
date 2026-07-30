---
title: "Deep Review - Bidirectional Interaction"
created: 2026-07-30
modified: 2026-07-30
human_modified: null
ai_modified: 2026-07-30T21:01:20+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-4-5-20251101
ai_generated_date: 2026-07-30
last_curated: null
---

**Date**: 2026-07-30
**Article**: [[bidirectional-interaction|Bidirectional Interaction]]
**Previous review**: [[deep-review-2026-07-14-bidirectional-interaction|2026-07-14]]

## Scope Note — Paraphrase Fidelity, Not Metadata Re-verify

The 2026-06-05 pass did a thorough per-cite *metadata* verification and caught a fabricated-author chimera. This pass ran the orthogonal axis the prior ledgers did not: **does the article's paraphrase match what each study actually found?** Every metadata verdict below came back clean; **three of the four post-2019 empirical citations turned out to be enrolled for claims their sources do not make.** Metadata-clean and paraphrase-clean are independent properties, and the ledger format used by reviews 1–7 recorded only the first.

Verification via Crossref REST, OpenAlex, DOI resolution and publisher fetch (WebSearch quota exhausted). Never by corpus grep.

## Per-Reference Ledger

| # | Entry | Checked | Metadata verdict | Paraphrase verdict | Source used |
|---|---|---|---|---|---|
| 1 | Seymour, J. & Mathers, N. (2024), *Front. Psychiatry* 14:1301143 | yes | **real-correct** (Jeremy Seymour, Nigel Mathers; vol 14, art. 1301143, pub. 2024-01-10) | **MISATTRIBUTED — fixed** | Crossref `10.3389/fpsyt.2023.1301143` + Frontiers full text |
| 2 | Streicher, J., Meyen, S., Franz, V. H. & Stein, T. (2025), *Neurosci. Conscious.* 2025(1) niaf042 | yes | **real-correct** (all four authors, venue, issue, article no. exact) | **MISATTRIBUTED — fixed** | Crossref `10.1093/nc/niaf042` (abstract) |
| 3 | Yuan, S. et al. (2022), *Front. Psychol.* 13:853804 | yes | **real-correct** (all ten authors, venue, volume, article no. exact) | **over-read — fixed** | Crossref `10.3389/fpsyg.2022.853804` (full structured abstract) |
| 4 | Tomasello, M. (2019), *Becoming Human* | yes | **real-correct** (Harvard UP, 2019, DOI `10.4159/9780674988651`) | real-correct | Crossref + OpenAlex |
| 5 | Frankish, K. (2016), "Illusionism as a theory of consciousness", *JCS* 23(11-12) | yes | real-correct (JCS not Crossref-indexed for this issue; OpenAlex confirms the 2016 JCS vol. 23 illusionism symposium) | **MIS-ENROLLED — fixed** (was cited for the phenomenal-concept strategy) | OpenAlex + standard attestation |
| 6 | Papineau, D. (2002), *Thinking about Consciousness* | yes | real-correct (OUP 2002, DOI `10.1093/0199243824.001.0001`) | real-correct | Crossref |
| 7 | Balog, K. (2012) — **newly added this pass** | yes | real-correct (*PPR* 84(1), 1-23) | real-correct | Crossref |
| 8 | Dehaene, S., Lau, H. & Kouider, S. (2017), *Science* 358(6362), 486-492 | yes | real-correct (exact) | real-correct | Crossref |
| 9 | Tegmark, M. (2000), *Phys. Rev. E* 61(4), 4194-4206 | yes | real-correct (exact) | real-correct | Crossref |
| 10 | Schwartz, J. M. (1998), *BJP* 173(Suppl. 35), 38-44 | yes | real-correct (exact) | real-correct (replication caveats already in body) | Crossref |
| 11 | Tomasello, M. (2014), *A Natural History of Human Thinking* | yes | real-correct (2014) | real-correct | Crossref |
| 12 | Kim, J. (2005), *Physicalism, or Something Near Enough* | yes | real-correct (Princeton UP; Crossref date 2007 = ebook reissue, print 2005) | real-correct (four-premise exclusion argument accurate) | Crossref |
| 13 | Stapp, H. P. (2007), *Mindful Universe* | yes | real-correct (Springer; Crossref 2011 = 2nd edn, 1st edn 2007) | real-correct | Crossref |
| 14 | Dennett, D. C. (1991), *Consciousness Explained* | **no** | not re-checked — stable monograph, verified 2026-06-05, bare-name inline use only | — | (carried) |

Superlative/currency sweep: `find_superlative_claims` returned **no matches**. No currency drift.

Inline ↔ References cross-check: no orphans in either direction. Balog 2012 added with an inline cite; Frankish 2016 retained and now backs *only* the illusionism paragraph.

## Pessimistic Analysis Summary

### Critical Issues Found (all fixed)

**1. Frankish 2016 cited as a source for the phenomenal-concept strategy — misattribution *and* internal contradiction.** The 2026-07-22 refine-draft commit (`ae1a2bd87`) introduced "the phenomenal-concept strategy (Frankish 2016, Papineau 2002)". Frankish 2016 is the *illusionism* paper; Frankish is not a PCS proponent. Worse, the same article three paragraphs later contrasts the two: "Where the phenomenal-concept strategy above keeps phenomenality and relocates the dispute, illusionism dissolves it by giving phenomenality up." The article cited Frankish for a position it then said Frankish rejects. The corpus sibling [[phenomenal-concepts-strategy]] attributes PCS to Loar, Papineau and Balog, and files Dennett/Frankish under [[illusionism]] — so the target article also contradicted the very page it wikilinks to. A secondary conflation: PCS was called "the strongest **epiphenomenalist** reply", but Papineau and Balog are physicalists.
- *Fixed*: cite corrected to **(Papineau 2002; Balog 2012)**; framing changed to "the strongest reply available to the epiphenomenalist borrows the phenomenal-concept strategy … a physicalist programme rather than an epiphenomenalist one, though its machinery transfers". Balog 2012 added to References. Frankish 2016 retained for the illusionism paragraph.

**2. Seymour & Mathers (2024) enrolled against its own thesis, and as empirical when it presents no new data.** Article claimed the paper showed "different beliefs about different conditions generating different neural signatures" and called this "a paradigmatic case of content-specific mental causation". The paper is a Frontiers **Hypothesis and Theory** article that states outright "This article presents no new data in support of the Neuroplasticity Placebo Theory", and its thesis is the *converse* structural claim — "Neuroplasticity is the **common denominator**, exerting **similar** measurable neurobiological activity in fronto-limbic areas". A unifying-mechanism proposal was being cited for condition-specific differentiation, inside a section headed "Empirical Support" describing "three converging **empirical** streams". The opioid/dopamine material is in the paper but cited by its authors from prior literature.
- *Fixed*: rewritten to state what the paper proposes, that it is a theoretical synthesis with no new data, and that its common-denominator thesis supports the weaker claim (belief states have identifiable neural consequences) rather than the stronger one (meaning selects among them). Section intro re-scoped to "three converging strands—two empirical, one a proposed mechanism". Note: the sibling [[clinical-neuroplasticity-evidence-for-bidirectional-causation]] already characterised this source correctly ("A 2024 paper *proposes*…"); the over-read was local to this article.

**3. Streicher et al. (2025) — a fabricated causal diagnosis replaced the paper's actual one.** Article said "most purported demonstrations of 'unconscious cognition' reflect **weak stimuli or brief exposure**, not genuine bypassing of consciousness". The paper's diagnosis is **statistical**, not substantive: the standard design never directly compares the sensitivity of the awareness measure against that of the processing measure, "a fundamental statistical fallacy". Nothing in the paper attributes the overestimate to stimulus weakness or exposure duration. The paper is also a **reanalysis**, not a meta-analysis (the wikilink alias asserted "meta-analysis" too — a nav-surface instance).
- *Fixed*: alias and body corrected to "reanalysis"; the true 8-of-80 figure given directly; the sensitivity-comparison diagnosis stated in the paper's own terms. Corpus check: this false diagnosis appears **only** in this article — [[access-consciousness]] states the sensitivity-comparison mechanism correctly, and the other five loci carry the 10% figure without a false diagnosis (a loose "meta-analysis" label persists in three; not swept this pass).

**4. Yuan et al. (2022) — anatomical over-read.** Article said the meta-analysis "found consistent **fronto-limbic** activation changes". The paper's own conclusion names "the altered activation in the **prefrontal cortex and precuneus**"; the precuneus is parietal/DMN, not limbic. The findings were consistent *decreases*, and the **emotion-task subanalysis found no regions surviving** — which directly undercuts a limbic reading. "Fronto-limbic" appears to have drifted onto Yuan from the Seymour & Mathers paraphrase in the adjacent bullet.
- *Fixed*: restated as "consistent *decreases* in prefrontal and precuneus activation … though its emotion-task subanalysis found no regions surviving", with the study count (13) added.

**5. Calibration error — "direct empirical evidence" for a non-discriminating pattern.** The Content-Specificity section opened "provides **direct empirical evidence for bidirectional interaction**". Content-specificity (belief content determines which physiological cascade follows) is fully predicted by physicalism, on which belief content is encoded in the brain states carrying it. By the skill's diagnostic test, a reviewer who *fully accepts the Map's tenets* would still flag this as overstated — the load-bearing support is tenet-coherence, not discriminating evidence. This is possibility/probability slippage, not bedrock disagreement.
- *Fixed*: reframed as "the empirical pattern this tenet most directly predicts", with the rival reading named explicitly and the residual positive claim preserved ("any adequate account must make meaning causally relevant somewhere; which account it favours turns on the arguments above rather than on the pattern itself"). Every other strand in this section already named its materialist reinterpretation; this one alone did not.

### Medium Issues Found
- The "convergence across three independent research programmes" summary asserted the dual-process asymmetry is "difficult to accommodate" for physicalism, while the asymmetry itself is attributed only to "the treatment-mechanism literature" with no citation and an "If robust" hedge two paragraphs earlier. Re-calibrated to say plainly that the asymmetry is a characterisation of the literature rather than a result any cited study establishes.
- The uncited dual-process asymmetry claim remains uncited (deliberately vague since the 2026-06-05 fabricated-detail removal). Now honestly labelled rather than silently load-bearing. Not escalated.

### Counterarguments Considered
- Physicalist re-description of every clinical result as brain-on-brain: already conceded per-strand; now conceded for content-specificity too, which was the one gap.
- Over-concession check (run as its own pass, per discipline): the 2026-07-22 self-stultification hedging is strong but was a convergent outer-review fix ratified by two reviewers on 07-20. It concedes the *conditionality* of the argument, not the tenet. Not reverted — reverting would oscillate.

## Optimistic Analysis Summary

### Strengths Preserved
- The 2026-07-22 self-stultification recalibration — genuinely good work, untouched except for the citation correction.
- The three-mechanism quantum interface exposition (Zeno / Orch OR / spontaneous collapse) with coupling-modes cross-link.
- "What Bidirectional Interaction Is Not", including the explicit "Not proven".
- Per-strand materialist counter-explanations in the clinical section — the model the content-specificity fix was made to match.

### Enhancements Made
- Five citation-fidelity fixes above; one reference added (Balog 2012).
- Hardline Empiricist counterweight satisfied twice over: fixes 2 and 5 both *decline* an evidence-upgrade the article had helped itself to.

### Cross-links Added
None — apparatus already extensive; all targets resolve.

## Tenet-Strength Assessment

**Does it distinguish what the tenet asserts from what evidence establishes?** Yes, and well, at the structural level: "a foundational tenet, not a derived conclusion", "The Map takes this as a starting commitment", "Not proven". No change needed.

**Does it over-read the empirical material into the tenet?** It did, in three places — all now fixed. The pattern was consistent: the *framing* sentences were honest while the *citation-level* claims quietly ran ahead of their sources. This is why seven prior reviews passed it: the hedges are all present and correct, so a calibration lens reading the prose finds nothing, while the over-claim sits one level down in what each paper is said to have found.

**Over-concession direction**: checked, none found beyond the already-ratified self-stultification hedging.

## Length

| | Prose (start → `## Further Reading`) | Apparatus (`## Further Reading` → EOF) | Total |
|---|---|---|---|
| Before | 2258 | 530 | 2788 |
| After | 2544 | 547 | 3091 |

Split computed by hand at the `## Further Reading` boundary (`analyze_length` returns one total and does no heading decomposition). Status remains `soft_warning`; **409 words to hard (3500)**. The growth is calibrated prose replacing bare assertion — the expected cost. No condense attempted.

## Remaining Items

1. **Loose "meta-analysis" label for Streicher et al. (2025)** in [[apex/minds-without-words]], [[global-workspace-theory]] and [[baseline-cognition]] — the paper is a reanalysis. Cosmetic, not false (none of the three carries the fabricated "weak stimuli" diagnosis). Not swept.
2. The Content-Specificity examples (painkiller/stimulant) remain uncited in this article; citations live in the sibling [[content-specificity-of-mental-causation]]. Site convention, deferred.

## Stability Notes

Seven prior reviews certified this article's citations, four of them with explicit verification sections, and all four verified **metadata only**. The 2026-06-05 review's ledger format — "author / venue / year / key numbers / stance" — is precisely the format that cannot catch a correctly-cited paper enrolled for a result it does not report. Future passes on citation-dense articles should treat *paraphrase fidelity* as a separate column, as this review's ledger does.

Bedrock disagreements (do **NOT** re-flag as critical): eliminativist (consciousness not a natural kind), illusionist (opposite starting intuitions), MWI-defender (all outcomes actualise), timing-skeptic (live research question). All framework-boundary standoffs.

The content-specificity calibration (fix 5) should **not** be re-expanded by a future optimistic pass into "direct evidence" — the pattern is predicted by physicalism too, and the article now says so.
