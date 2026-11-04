---
ai_contribution: 100
ai_generated_date: 2026-11-04
ai_modified: 2026-11-04 21:35:53+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-04
date: &id001 2026-11-04
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-04 21:35:53+00:00
modified: *id001
related_articles: []
title: Deep Review - The Von Neumann–Wigner Interpretation
topics: []
---

**Date**: 2026-11-04
**Article**: [The Von Neumann–Wigner Interpretation](/concepts/von-neumann-wigner-interpretation/)
**Previous review**: [2026-07-23](/reviews/deep-review-2026-07-23-von-neumann-wigner-interpretation/) (sixth deep review; six prior no-critical-issues verdicts)

## Summary

Seventh deep review. Three changes have landed since 07-23: the 09-04 unconditioned-aggregate scoping (L102), the 10-05 Process 1 reciprocal (L92), and the 11-03 Zeno-timing satellite fix (L84/L96). All three were re-read and left as they are.

This pass broke the convergence streak on three critical defects. None of them came from the recent edits; all three had stood since creation or since early reviews. The first two were found by grepping primary sources, which the six prior reviews never did. The third was found by reading the sibling pages, which already carry the corrected form.

1. **Misquotation of Wigner (L56).** The article quoted Wigner as saying "It **is** not possible to formulate…". The 1961 text reads "it **was** not possible to formulate the laws of quantum mechanics in a fully consistent way without reference to the consciousness." The prior reviews of 03-20, 04-27 and 06-01 all certified the quote "authentic" without grepping the source.
2. **Misattributed reasons for Wigner's retreat (L58).** The article said "Two pressures drove it", naming solipsism and the multi-observer specification problem, and that "Wigner found these problems substantial enough to walk back the strong reading". The documented record differs in three ways:
   - It names Zeh's 1970 argument that macroscopic systems are never closed. The article omitted this.
   - It also names solipsism. The article had this one right.
   - The multi-observer objection comes from Wigner's critics, notably Shimony (1963), not from Wigner. The 06-01 review saw this gloss and passed it as "exposition", but it never found the Zeh driver, so its resolution was incomplete.
3. **Frauchiger–Renner misread, and a contradiction with sibling pages (L60).** The article said "F–R puts pressure on V-N-W rather than supporting it" and that the Map's response "runs through interface locality and indexical identity".
   - Frauchiger and Renner's own text says Assumption (Q) "is manifestly violated by theories that postulate a modification of standard quantum mechanics, such as spontaneous… and gravity-induced… collapse models". V-N-W therefore takes the drop-universality exit by construction, and so does the Map's objective-collapse baseline.
   - `concepts/post-decoherence-selection` §"Absolute Outcomes and the Local Friendliness Theorem" states that the Map's actual answer is that "a laboratory containing a conscious observer cannot afterwards be recohered by an experimenter outside it".
   - `topics/multi-agent-born-preservation-problem` L64 says that in Wigner's-friend scenarios "interface locality cannot help".
   - `testing-consciousness-collapse` L175 and `self-reference-and-the-limits-of-physical-description` L134 agree. This page was the outlier.

Word count: 2894 → 2987 (+93). Concepts soft is 2500 and hard is 3500 (gate `>=`), leaving 513 words of headroom. The two substantive corrections cost about +160 and were partly offset by about −67 of trims (see below).

## Open-Task Overlap (honoured)

- **P3 refine-draft (tenet-check 2026-11-03 W2)** owns L112 ("Stapp's quantum Zeno mechanism that specifies *how* consciousness acts") and optionally L114 (note 8). **Not touched.** That task's OLD string still occurs exactly once.
- **P3 NEEDS-HUMAN on `positions/quantum-interface`** lists an unminted lead from the 10-05 corridor review: L58's "(consciousness modulates collapse statistics rather than constituting collapse itself)". That wording belongs to a pending "modulat-" terminology sweep, recorded as a watch item in tenet-check 2026-10-03. The L58 rewrite keeps that parenthetical **verbatim**, so the sweep is not pre-empted.
- The 11-03 L84/L96 satellite fix is left as it is, per the P3 task's note.

## Publisher-of-Record Citation Web-Verify (§2.4)

Per-cite ledger (this pass):

- Von Neumann 1932/1955 (*Mathematical Foundations of Quantum Mechanics*, Princeton) — **real-correct**. The two-word term "abstract ego" was **not re-verified this pass**: archive.org's copies are lending-only (HTTP 401) and the Google Books API returned 429. The term is untouched and long-attested, and is carried forward from the prior ledger.
- Wigner 1961 ("Remarks on the Mind-Body Question", in I.J. Good (ed.), *The Scientist Speculates*, Heinemann) — **real-correct metadata**. The reprint's source note (Yale-hosted PDF) reads: "Reprinted by permission from The Scientist Speculates, I. J. Good, ed. (London: William Heinemann, Ltd., 1961; New York: Basic Books, Inc., 1962)", which confirms 1961 for Heinemann. **Quote: misquoted (tense), corrected** to the verbatim "it was not possible…", grep-confirmed in the raw text.
- London & Bauer 1939 (*La Théorie de l'Observation…*, Hermann) — real-correct (carried forward; untouched).
- Frauchiger & Renner 2018 ("Quantum theory cannot consistently describe the use of itself", *Nat. Commun.* 9(1), 3711; DOI 10.1038/s41467-018-05739-8) — **real-correct**, by Crossref and the publisher PDF. The **result-direction leg failed on the article's framing**: FR's own text puts collapse modifications outside the theorem's force, quoted above, so the "pressure on V-N-W" reading has been withdrawn.
- Stapp 2007 (*Mindful Universe*, Springer) — real-correct (carried forward). Cited by name in the body and never by year; this is a pre-existing pattern accepted by six reviews.
- Tegmark 2000 (*Phys. Rev. E* 61(4), 4194–4206) — **real-correct** (Crossref).
- Hagan, Hameroff & Tuszyński 2002 (*Phys. Rev. E* 65(6), 061901) — **real-correct** (Crossref).
- Wiest 2025 (*Neuroscience of Consciousness* 2025(1), niaf011; DOI 10.1093/nc/niaf011) — **real-correct** (Crossref).
- **NEW** Zeh 1970 ("On the interpretation of measurement in quantum theory", *Found. Phys.* 1(1), 69–76; DOI 10.1007/bf00708656) — **real-correct** (Crossref; also FR 2018 ref. 49). The body paraphrase was checked against the full text at the Köln mirror: "Since the interactions between macroscopic systems are effective even at astronomical distances, the only 'closed system' is the universe as a whole. The assumption of a closed system M + S is hence unrealistic on a microscopic scale."
- **NEW** Shimony 1963 ("Role of the observer in quantum theory", *Am. J. Phys.* 31(10), 755–773; DOI 10.1119/1.1969073) — **real-correct** (Crossref). The attribution was checked against the OpenAlex abstract, which says of the von Neumann/London–Bauer interpretation: "it is not supported by psychological evidence and it is difficult to reconcile with the intersubjective agreement of several independent observers."
- Southgate & Oquatre-six 2026 — a Map self-reference, unchanged.
- **Wigner's later view (historiography; no inline cite added).** Three secondary sources were used:
  - Freire Jr., "Orthodoxy and Heterodoxy… E.P. Wigner's Case" (arXiv physics/0602028): Wigner backed Zeh's paper. Freire also quotes Shimony 1997 quoting Wigner: "the validity of quantum mechanics' linear laws is limited."
  - Wikipedia "Consciousness causes collapse", citing Esfeld 1999: there was a 1982 lecture on solipsism and a 1984 statement crediting Zeh. Wikipedia also says Wigner "rejected his initial idea of treating macroscopic objects as isolated systems."
  - Thaheld 2005 (arXiv quant-ph/0509042), citing Mehra (ed.) 1995, *Collected Works* B/VI, pp. 73, 230, 593 and Esfeld 1999: Wigner changed position "in order to avoid solipsism", "considered it to be necessary to admit state reductions independently of an observer's consciousness", and suggested "an amendment of the Schrödinger equation".

  The article's new sentences paraphrase only what at least two of these sources agree on. Esfeld 1999 itself was **not** read (no accessible text), so it is not cited.
- Empirical-currency sweep: the article has no superlatives in the edited passages. The earlier sweep found none.
- Cited-author-stance leg: Shimony's 1963 position is reported as a criticism of consciousness-collapse, which it was. Zeh is reported for his closed-system argument only; the article does not present his conclusion, universal validity of quantum theory, as Wigner's. Frauchiger and Renner are not presented as favouring any interpretation.

## Pessimistic Analysis Summary

### Critical Issues Found
- **Quote fidelity (L56)**: tense changed inside quotation marks. **Fixed**: the quote is now verbatim, with the original's framing ("with the creation of quantum mechanics") outside the marks.
- **Attribution error (L58)**: reasons were attributed to Wigner that he did not give, and the documented one was omitted. **Fixed**: the passage now has two documented pressures (Zeh 1970 non-closure; solipsism) and Wigner's later acceptance of consciousness-independent state reduction. The multi-observer specification problem is now credited to critics "such as Shimony (1963) rather than by Wigner". It adds that the Map's objective-collapse baseline is "close to where Wigner himself ended", which is accurate: the Map's baseline is objective collapse with modulation added, and Wigner's later view was objective reduction alone.
- **Source misreading and cross-page contradiction (L60)**: **Fixed**. F–R "neither refutes V-N-W nor singles it out". FR class collapse modifications as manifestly violating universality, and V-N-W modifies quantum mechanics exactly at the friend's observation. The Map takes the same exit and owns the cost (no recoherence of a lab containing a conscious observer, detectable in principle), linking the canonical section. "Interface locality cannot do this work" now aligns with `multi-agent-born-preservation-problem` L64. The literature's three-exit gloss is kept verbatim.

### Calibration Check (possibility/probability slippage)
- **PASS.** No evidential tier moved. The F–R rewrite removes a weak claim (that the Map has an interface-locality answer to F–R) and replaces it with an owned cost. The Wigner retreat rewrite is historical exposition and concerns no evidence level. The genealogy transition check passes: no step runs "origin ⇒ validity". The lineage claim stays at "problem space", not "Wigner was right" (L104).

### Medium Issues
- Redundancies were trimmed to offset length:
  - The duplicate lineage sentence at L58 went; the same sentence stands in the RtSP bold lead at L104.
  - At L102, the clause "and the article's 'ancestor not final form' framing is meant to mark exactly this distinction" went.
  - The closing sentence of the L126 hub paragraph went, because it restated L118.
  - Two Further Reading entries (`measurement-problem`, `spontaneous-collapse-theories`) went, because they duplicate the "Where the Modulation Framing Appears" list immediately above. Both pages stay linked elsewhere on the page.

### Low Issues (not acted on)
- L84 (owned by the 11-03 satellite fix, left as it is): Tegmark's 10⁻²⁰ s figure is for a superposition of a neuron firing or not, so "ion-channel superpositions" is loose. "Femtoseconds" undersells 10⁻²⁰ s.
- L46: "the only element that cannot itself be placed into quantum superposition" is an interpretive gloss on von Neumann's "abstract ego". It is stable across seven reviews and not re-flagged.

### Counterarguments Considered
- The adversarial personas' objections remain the documented bedrock standoffs (eliminativism, MWI, decoherence-only physicalism). None is re-flagged.
- The Deutsch persona's earlier complaint (pessimistic 06-26c) that the F–R response was "a promissory note" is now answered on the page: the Map's response is a stated restriction with a testable cost.

## Reasoning-Mode Classification

These classifications are editor-internal; there is no label leakage in the prose.

- Frauchiger–Renner: exposition, plus an honestly owned cost. No refutation is claimed; the Map takes a named exit.
- Shimony's objection: exposition of a critic, answered by interface locality in the ordinary case.
- Tegmark/decoherence: Mode Three (unchanged).
- Many-Worlds: Mode Three (unchanged).

## Attribution Accuracy Check

- Misattribution: fixed (Wigner's reasons).
- Qualifiers: preserved. "Close to where Wigner himself ended" is hedged, and "a charge Wigner later allowed his earlier view invited" follows the sources' wording.
- Position strength: Wigner's later proposal is reported as "proposed amending the equation of motion", not as a theory he established.
- Source/Map separation: the Map's exit from F–R is marked as the Map's own ("The Map takes the same exit and owns its cost").
- Self-contradiction: the cross-page contradiction with the multi-agent page is removed.

## Optimistic Analysis Summary

### Strengths Preserved
- The front-loaded weaker-than-headline framing.
- The "problem space, not mechanism" lineage claim (L104).
- The Process-1 conservativeness passage and the "acknowledges but does not adopt" boundary (L92–L94).
- The decoherence paragraph's honesty.
- The modulation-framing hub.

### Enhancements Made
- The lineage now records that Wigner himself ended near the Map's objective-collapse baseline. This is a stronger and accurate genealogy, since the Map's mechanism inherits the late Wigner's reduction and not the early Wigner's consciousness-trigger.
- The F–R treatment now states the Map's actual exit and its empirical cost.

### Cross-links Added
- [post-decoherence-selection](/concepts/post-decoherence-selection/) (to the local-friendliness section)
- [multi-agent-born-preservation-problem](/topics/multi-agent-born-preservation-problem/)

## Remaining Items

- L112 and L114 belong to the open P3 task (tenet-check 2026-11-03 W2).
- The "modulates collapse statistics" wording (L58, L102) belongs to the pending terminology sweep.
- Sibling `concepts/quantum-probability-consciousness` L138 says Wigner abandoned the idea "after Zeh's decoherence work showed that environmental interaction suppresses interference without invoking consciousness". Zeh 1970's argument was non-closure, and Wigner's conclusion was that QM's linear laws are limited, not that decoherence explains outcomes. This is proposed as a follow-up and was not edited here.

## Stability Notes

- The quote, the retreat paragraph and the F–R paragraph are now source-verified. Future reviews should not reopen them unless the text changes. If the retreat passage is revisited, do not reintroduce "the multi-observer problem drove Wigner's retreat"; it was Shimony's objection.
- Bedrock disagreements (eliminative materialism, MWI, decoherence-only physicalism) remain expected framework-boundary standoffs and should not be re-flagged.
- **Lesson for this file**: six consecutive no-critical verdicts certified a misquote, a misattribution and a source misreading. None of the six grepped the Wigner text, read FR's discussion of collapse theories, or compared the F–R paragraph with its siblings. A convergence streak on this page is not evidence of accuracy for passages that no review checked against a primary source.