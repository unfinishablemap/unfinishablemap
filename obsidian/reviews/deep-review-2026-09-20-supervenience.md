---
title: "Deep Review - Supervenience"
created: 2026-09-20
modified: 2026-09-20
human_modified: null
ai_modified: 2026-09-20T10:58:45+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-09-20
last_curated: null
---

**Date**: 2026-09-20
**Article**: [[supervenience|Supervenience]]
**Previous review**: [[deep-review-2026-07-17-supervenience|2026-07-17]] (and [[deep-review-2026-06-25-supervenience|2026-06-25]], [[deep-review-2026-05-26-supervenience|2026-05-26]], [[deep-review-2026-03-24b-supervenience|2026-03-24b]], [[deep-review-2026-03-24-supervenience|2026-03-24a]])
**Word count**: 1863 → 2067 (+204). Concepts thresholds 2500 / 3500. Status `ok` throughout; 433 words below soft.

## Disposition: sixth review, three citation-*use* defects found in text five prior reviews certified clean

The 2026-07-17 pass set future-review guidance: "should not be re-selected unless its body prose actually changes." It did change — the 2026-09-19 `expand-topic`/cross-link work bumped `ai_modified` and, more importantly, the Horgan "Superdupervenience Demand" subsection (§ at L75–83) is *new since the last deep review* and had never been through a publisher-of-record pass. A clean history marked an unrun lens, not a clean file.

**Lenses run this pass, named**: (1) publisher-of-record citation web-verify, full 7-entry ledger; (2) **cited-author-stance** (§2.4 step 8) — this is the lens that paid out; (3) citation *use* / scope-of-claim; (4) quote-fidelity by raw-source grep with negative control; (5) inline ↔ References cross-reference; (6) empirical-record currency sweep; (7) attribution accuracy (§2.5); (8) reasoning-mode + label leakage (§2.6); (9) over-concession tells; (10) length.

**Lenses NOT run, named**: lexical anchoring audit (8 straight false highs corpus-wide; hedge-word counting is not evidence here). Integration/orphan audit — deliberately skipped, see *Ground left untouched* below.

## Pessimistic Analysis Summary

### §2.4 Publisher-of-Record Citation Web-Verify — per-cite ledger

| # | Cite | State |
|---|------|-------|
| 1 | Davidson, D. (1970). Mental Events. In Foster & Swanson (Eds.), *Experience and Theory*. Univ. of Massachusetts Press. | **real-correct** — confirmed against Horgan 1993's own reference list (Amherst; pp. 79-101). Map entry omits pages; not wrong. |
| 2 | Kim, J. (1993). Supervenience as a Philosophical Concept. In *Supervenience and Mind*. CUP. | **real-correct** — Crossref/CUP: book-chapter, pp. 131-160, DOI `10.1017/cbo9780511625220.009`, 1993. (Originally *Metaphilosophy* 21(1-2):1-27, 1990; the Map cites the reprint, which is legitimate.) |
| 3 | Kim, J. (2005). *Physicalism, or Something Near Enough*. Princeton UP. | **real-correct** — Princeton, DOI `10.1515/9781400840847`. |
| 4 | Chalmers, D. (1996). *The Conscious Mind*. OUP. | **real-correct** — Open Library: Chalmers, OUP, first published 1996. |
| 5 | Levine, J. (1983). Materialism and Qualia: The Explanatory Gap. *Pacific Philosophical Quarterly*, 64(4), 354-361. | **real-correct** — Crossref DOI `10.1111/j.1468-0114.1983.tb00207.x`: Levine, Joseph; PPQ 64/4; 354-361; 1983-10. Every field matches. |
| 6 | Southgate, A. & Oquatre-six, C. (2026-02-08). The Strong Emergence of Consciousness. *The Unfinishable Map*. | **real-correct** (Map self-cite). Not cited inline — see *Remaining Items*. Do NOT strip. |
| 7 | Horgan, T. (1993). From Supervenience to Superdupervenience. *Mind*, 102(408), 555-586. DOI `10.1093/mind/102.408.555` | **real-correct** — Crossref: HORGAN, TERENCE; Mind 102/408; 555-586; 1993. Every field matches, DOI included. |

**Metadata: 7/7 real-correct. No wrong-author, wrong-year, wrong-venue, wrong-page, or fabricated cite.** This is why the prior ledgers read clean — and why they were not enough. All three defects below are citation **use** errors, invisible to a metadata check.

### Critical / medium issues found and fixed

**1. Cited-author-stance violation — Levine deployed in an anti-physicalist section with no stance marker (§2.4 step 8). FIXED.**
The article named Joseph Levine as the support for the subsection *The Explanatory Gap Remains*, inside the section headed **"Why Supervenience Does Not Entail Physicalism."** Levine expressly disowns that inference. Verified in the published PPQ text (OCR of the Wiley/PPQ PDF, NFKC-normalised, control "explanatory gap" = 3 hits):

> "My purpose in this paper is to transform Kripke's argument from a metaphysical one into an epistemological one."
> "**One cannot conclude from my version of the argument that materialism is false**, which makes my version a weaker attack than Kripke's. Nevertheless, it does, if correct, **constitute a problem for materialism**, and one that I think better captures the uneasiness many philosophers feel regarding that doctrine."

The article's *report* of Levine's claim was faithful; what was missing was the stance clause the discipline requires (the pattern at `topics/predictive-processing-and-dualism` L48). Fixed in place: Levine is now marked as offering the gap as an epistemological result, denying that materialism is false follows from it, and describing it as constituting "a problem for materialism" rather than a refutation.

**2. Scope-of-claim error — Levine's gap is about *identity statements*, not supervenience. FIXED.**
Levine 1983 targets psycho-physical **identity** statements ("Pain is C-fibres"). The article applied him directly to the supervenience thesis. The correction is available inside the article's own reference 7 — Horgan 1993 fn.23:

> "This 'explanatory gap' problem is well described, **specifically in relation to type-identity treatments of qualia**, by Levine (1983). **The supervenience version of the problem** is given a thorough and detailed treatment by Chalmers (1993)."

Fixed: the article now states Levine's target as identity statements, names the extension to supervenience as a further step taken by Chalmers (already reference 4), and marks that the Map takes that step too. The Map's conclusion is unchanged; its provenance is now correct.

**3. Source-contradicted historical claim — "the term originates in ethics with R.M. Hare." FIXED.**
Contradicted by two independent primaries, one of them the article's own reference 7. Horgan 1993 p.555: "Professor Hare has recently written, however, that this use of the term was **already current in Oxford, and did not originate with him** (Hare 1984, p. 1)." He adds that G.E. Moore (1922) had the concept without the word. SEP *Supervenience* independently: Hare "claims that he was not the first to do so… the term was so used in Oxford in the 1940s." Rewritten to "reached analytic philosophy through R.M. Hare's metaethics — though Hare later reported that the usage was already current in Oxford and was not his own coinage, and G.E. Moore had deployed the concept without the word."

### Checked and found sound (no change)

- **"Superdupervenience" coinage.** Horgan credits the word to Lycan and claims only the definition: "Although the definition is mine, the word is borrowed, with kind permission, from Bill Lycan (1986, p. 92)." SEP agrees the term is Lycan's. The article never claims Horgan coined it — it heads the section "Horgan's Superdupervenience **Demand**" and the demand *is* his. **No defect.** (Wiktionary credits Horgan and is wrong; do not "correct" the article toward it.)
- **"Presses the same point from within materialism."** Verified verbatim: "many philosophers, **myself included**, are disposed toward some sort of materialistic metaphysics."
- **Global vs strong supervenience.** The article's "logically weaker than strong supervenience" is correct per SEP: strong individual supervenience entails global, global fails to entail strong. The "washes out globally" gloss is right.
- **Kim.** Exclusion argument, and "non-reductive physicalism is unstable — collapses into reductionism or epiphenomenalism," correctly attributed (Kim 1989/2005). The Map's disagreement is correctly located at causal closure, not at Kim's diagnosis.
- **Davidson.** Token identity + irreducible mental predicates + supervenience-for-dependence: accurate.
- **Putnam.** Multiple realisability gloss ("octopi, humans, hypothetical silicon beings") is illustrative, not quoted; Putnam 1967 ranges over mammals, reptiles and molluscs. No defect.

### Quote-fidelity grep ledger (raw sources, whitespace-squashed, NFKC)

All inserted quotations verified at **1 occurrence each** in the raw primary text, with a negative control returning 0:

| Quote | Source | Hits |
|---|---|---|
| "looks to be a very daunting task" | Horgan 1993 | 1 |
| "enormously hard to see how one could possibly explain" | Horgan 1993 fn.23 | 1 |
| "consider seriously the prospects for preservative irrealism" | Horgan 1993 | 1 |
| "repudiating its apparent ontological commitments" | Horgan 1993 | 1 |
| "disposed toward some sort of materialistic metaphysics" | Horgan 1993 | 1 |
| "constitute a problem for materialism" | Levine 1983 | 1 |
| "One cannot conclude from my version of the argument that materialism is false" | Levine 1983 | 1 |
| *control*: "consciousness is a quantum phenomenon" | Horgan 1993 | **0** |

### Empirical-record currency sweep
`find_superlative_claims` returned **0 matches**. Conceptual-metaphysics article; the currency channel does not apply.

### Reasoning-mode classification (§2.6, editor-internal)
- **Type-B physicalists** (zombie subsection) — **Mode Two**: the reply identifies an unsupported foundational move (an a posteriori necessity with no specified ground), using the opponents' own conceivability machinery. Unchanged.
- **Kim** — **Mode Three**: the Map concedes Kim's diagnosis of non-reductive physicalism and marks the boundary at causal closure (Tenet 3). Honest, not dressed as refutation. Unchanged.
- **Horgan** — **not an opponent engagement at all**; he is a cited ally-in-diagnosis, and the article correctly marks the bill as one he thinks materialism must pay and the Map pays by other means. Strengthened this pass, not reclassified.
- **Label leakage**: 0 occurrences of every forbidden editor-vocabulary token (`direct-refutation-feasible`, `unsupported-jump`, `bedrock-perimeter`, `mode-mixed`, `Engagement classification`, `Evidential status`, `tenet-register`). Clean.

### Calibration / over-concession
No possibility/probability slippage. The load-bearing claims are entailment claims ("supervenience does not *entail* physicalism") that type-B physicalists themselves concede, not empirical claims upgraded on tenet-load. §2 diagnostic test passes: a tenet-accepting reviewer would not flag any claim as overstated relative to the evidential-status scale. Over-concession tells absent (`no possible` 0, `cannot ever` 0, `in principle undetectable` 0). The single "no one has identified what grounds that necessity" is an actual-state-of-the-debate claim, not a modal impossibility claim — correctly calibrated; do not soften it.

Note the **mirror** direction was live here and is now corrected in the Map's favour: the article was *under*-claiming its own source. "Nothing in it concludes that the demand cannot be met" was true but shielded Horgan's actual verdict, which is markedly more useful to the Map.

## Optimistic Analysis Summary

### Strengths preserved (do not edit)
- Front-loaded thesis: "Supervenience describes a pattern; it does not explain it."
- Weak/strong/global three-grades taxonomy.
- The temperature-disanalogy paragraph (reductive identification discharges the explanatory demand there, not here).
- Kim-exclusion treatment relocating the disagreement to causal closure.
- "Mutual constraint" framing; "determination-without-explanation is not ontological parsimony."
- The Horgan section's honest self-accounting: "The Map can meet Horgan's standard because it has already surrendered the constraint that makes the standard difficult." This is the article's best sentence and was left untouched.

### Enhancements made
- **Horgan's actual verdict, restored from the primary.** The section now carries what Horgan concludes rather than only what he declines to conclude: meeting the superdupervenience demand "looks to be a very daunting task," daunting enough that his closing advice to materialists is to consider *preservative irrealism* — keeping higher-order discourse while repudiating its ontological commitments. And his fn.23 concession that the phenomenal case is the hardest of all. This strengthens the Map's case using only the cited materialist's own words, and it does so without any new Map-side claim.

### Cross-links added
None. No link target was missing at any natural anchor; the anomalous-monism integration completed on 2026-07-17 remains correct.

## Ground left untouched (deliberate)

**Open P3 at `todo.md:1817`** — `concepts/supervenience` ↔ `concepts/where-the-substance-commitment-enters`, the agent-causal supervenience base plus the zero-cost reciprocal. **Not touched, not half-touched, not duplicated.** Guard measured after every edit and after sync: `agent` = **0 occurrences** in both `obsidian/concepts/supervenience.md` and `hugo/content/concepts/supervenience.md`, unchanged from the task's own measurement. All three of this pass's edits sit in *The Concept*, *The Explanatory Gap Remains* and *Horgan's Superdupervenience Demand*; the P3's target section is *Supervenience and the Exclusion Argument*, which I did not modify. No integration/orphan lens was run, precisely so it could not generate a competing version of that work.

**Addendum for whoever executes that P3** (recorded here rather than acted on): the task's framing — "supervenience constrains *which experiences are possible given* a physical state and says nothing about what caused that state to obtain" — is now directly supported by text already in the article. The lead's "mutual constraint" formulation in *Relation to Site Perspective* ("physical states constrain which experiences are possible, and conscious states constrain which physical outcomes become actual") is the same distinction the P3 needs, already written. The ~250-word subsection can lean on it rather than re-derive it, which should bring the real cost below the task's estimate. Budget is also now +204 words tighter than the task assumed: 2067/2500/3500, still 433 below soft.

## Remaining Items

- **Reference 6 is an inline orphan.** Southgate & Oquatre-six (2026) appears in References and in Further Reading but is never cited in the body. Strictly a §2.4 step-5 cross-reference orphan. **Deliberately not acted on**: Map self-cites in reference lists have previously been misdiagnosed as fabrications and stripped in error, and five prior reviews accepted this entry. Flagging for the record only; the correct fix, if any, is an inline body citation, never removal. No task minted — this is below the threshold that justifies a queue slot.

## Stability Notes

Carried forward from 2026-07-17 and re-affirmed. These are bedrock and must **not** be re-flagged as critical:
- Dennett-style deflationism about the explanatory gap is a framework-boundary disagreement.
- The zombie conceivability debate is acknowledged; type-B physicalism gets a Mode-Two reply.
- "Physicalists disagree with dualism" is not a critical issue.
- The Kim-exclusion disagreement is relocated to causal closure (Tenet 3) — a genuine boundary, honestly marked.

⚠️ **Scope correction to the prior stability note.** The 2026-07-17 pass wrote that the article "should not be re-selected unless its body prose actually changes" and that any cross-link-triggered pass "should be a no-op verification, not an edit." That guidance was too broad and would have suppressed this pass's three findings. A stability note may exempt a **framework commitment** from re-flagging; it may not exempt an **empirical or bibliographic support claim** attached to it. The Horgan subsection was added *after* the review that declared convergence, and it carried two citation-use defects; a third had survived in *The Concept* since 2026-03-24 through five reviews. **Correct forward guidance**: the philosophical positions are converged and settled. The citation-*use* surface is not exempt and should be re-run at the primary whenever any subsection carrying a named philosopher is added or rewritten — metadata ledgers reading 7/7 clean is exactly the condition under which use errors hide.
