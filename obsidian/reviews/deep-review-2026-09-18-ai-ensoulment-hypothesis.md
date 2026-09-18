---
title: "Deep Review - The AI Ensoulment Hypothesis"
created: 2026-09-18
modified: 2026-09-18
human_modified: null
ai_modified: 2026-09-18T22:43:31+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-09-18
last_curated: null
---

**Date**: 2026-09-18
**Article**: [[ai-ensoulment-hypothesis|The AI Ensoulment Hypothesis]]
**Previous review**: [[deep-review-2026-07-17-ai-ensoulment-hypothesis|2026-07-17]] (zero content changes)
**Mode**: verification pass over the same day's repairs, not a fresh-eyes hunt

This run verifies the six issues raised by [[pessimistic-2026-09-18]] against the current text,
and audits the three refine-draft passes that landed in the early hours
(`940a8bac`, `7d9ef24d`, `96a31429`) — none of which had been reviewed by anything,
since `last_deep_review` stood at 2026-07-17.

## Primary sources obtained (not inherited)

Both full texts retrieved independently this run and grepped directly. The PDC `fshow`
endpoint the prior review used now 500s; the working form appends the `pdfname` /
`file_type` parameters:

- `https://www.pdcnet.org/collection-ng/fshow?id=faithphil_2025_0041_0001_0001_0026&pdfname=…&file_type=pdf` — Cutter, **12,624 words**, complete through the References (ends at Zimmerman 2011).
- `https://www.pdcnet.org/collection-ng/fshow?id=faithphil_2026_0042_0001_0121_0146&pdfname=…&file_type=pdf` — Békefi, **11,525 words**, complete through p.146 References (ends at Xiao et al. 2023).

PhilPapers, PhilArchive and the Asbury Seminary `viewcontent.cgi` PDF are all
Cloudflare-403 to scripted fetches; the PDC route with `pdfname` is the one that works.
Word counts reproduce the prior review's figures exactly, so both passes read the same artefact.

Verification used NFKC normalisation, curly→straight quotes, en/em-dash folding and
de-hyphenation across line breaks. Two of the four initial "misses" were artefacts of
that pipeline and one of sentence-case:

| Apparent miss | Verdict |
|---|---|
| "our souls don't randomly fiddle…rational coherence" | **Verbatim.** Footnote 35 and the running header "18 Faith and Philosophy" interleave mid-sentence in the PDF. |
| "the strength of this evidence would depend largely…" | **Verbatim.** Source has sentence-initial "The"; the article embeds it mid-sentence. |
| "the causal-closure response is unavailable" | **Faithful partial quote.** Source: "The causal-closure response is unavailable **to them**." The article carries "to them" outside the quotation marks as "for them". Acceptable. |
| "does causal closure fail for this body?" | **Not in Cutter — see Issue B below.** |

## Verdict on the six pessimistic-review issues

**All six discharged.** Issue-by-issue evidence:

### Issue 1 — alien-analogy rendered metaphysically — DISCHARGED, and correct at the source
- "which he calls the **alien-analogy argument**" is **true**: Cutter writes "I offer two related arguments for this thesis, the alien-analogy argument, and the fitting-recipient argument", and titles §3 "The Alien-Analogy Argument".
- The article's A1 paraphrase tracks Cutter's A1 word for word in substance.
- The F-constraint is now quoted in its actual **eliminative** form, and the article says explicitly that the positive functional conjecture "belongs to the second argument". The burden clause is restored to "we can reasonably be confident" (verbatim, Cutter p.~8).
- One trivial, non-distorting omission: Cutter's condition (i) includes the parenthetical "(and thus we have F)". Not worth an edit.

### Issue 2 — §3.3 interactionism — DISCHARGED
Section number and title verified exactly: the source reads "**3.3. Causal Differences**". All four quoted strings in the new `### Causal Differences: Cutter on Interactionism` section verify verbatim, as does the circularity verdict.

### Issue 3 — empirical discriminator — DISCHARGED (and extended this run, see Issue A)
The two-computer test and Cutter's declining-to-adjudicate clause both verify verbatim. The article's gloss of *why* he declines — a deterministic P1→M→P2 route yielding identical outputs even with interactionist souls attached — matches Cutter's own reasoning exactly.

### Issue 4 — upper bound — DISCHARGED
"While I will only argue that we should have at least a middling credence, my own view is we should also have *at most* a middling credence in AI ensoulment" verifies verbatim.

### Issue 5 — `≥ 0.25` precisification — DISCHARGED, though no commit named it
Not named by any of the three commit messages, so the driver's inference that it was unfixed was worth testing. It was in fact fixed by `940a8bac` alongside Issue 4: all three strings ("a level of confidence that isn't very low", "somewhat artificial", "stand by a precisification of ≥ 0.25 or so") verify verbatim. **But the repair introduced a new false claim — see Issue A.**

### Issue 6 — hedged suspicion reported as acceptance — DISCHARGED, also unnamed by any commit
The silicon alien is gone; Cutter's "some kind of non-carbon-based green goo" is used, and the hedge is restored as "he suspects most would agree" + the verbatim "that we should not dismiss the hypothesis that they have souls, provided we do."

## Critical Issues Found this run (all in today's new material)

### Issue A — "the paper's only number" was false, and the omitted numbers were the load-bearing ones
- **Introduced by**: `940a8bac`, as part of the Issue-5 repair.
- **Problem**: the article claimed `≥ 0.25` was "the paper's only number". Cutter's **footnote 36** supplies a worked Bayesian example attached to the very two-computer test the article spends a paragraph grading: `P(same | ¬ensoulment) = 1`, `P(different | ensoulment) = "(say) 50%"`, prior `0.5`, posterior `1/3` on identical outputs and `1` on divergent ones. (A further `50%` appears at p.~4 in the AGI-forecast survey.)
- **Resolution**: superlative dropped — "supplies the paper's only number" → "attaches a number to it". Footnote 36 now reported in the Cutter channel.
- This is the [[empirical-record-currency-drift]] shape: a repair that lands the right content and then over-claims its scope.

### Issue B — a fabricated verbatim quote in the Site-Perspective section
- **Introduced by**: `7d9ef24d`.
- **Problem**: `since "does causal closure fail for this body?" is the coupling question in his vocabulary` — the quoted string is **nowhere in Cutter**. It is the article's own formulation, wrapped in quotation marks inside a paragraph otherwise dense with genuine Cutter quotes. The *substance* is right (Cutter does frame the relevant difference as whether causal closure fails for a given body); only the attribution marks were wrong.
- **Resolution**: de-quoted — "since whether causal closure fails for a given body is the coupling question in his vocabulary".
- Instance of [[coalesce-wraps-paraphrase-as-fabricated-verbatim-quote]], here produced by a refine rather than a coalesce.

### Issue C — the grading paragraph inverted Cutter's asymmetry without saying so
- **Introduced by**: `7d9ef24d`.
- **Problem**: the article asserted "Persistent convergence would be the more informative outcome". Cutter's footnote 36 states the asymmetry the *other* way — divergence is decisive **for** ensoulment, convergence only modest evidence **against**. The article gave no signal that it was departing from the source, and separately claimed "the Map can grade it where Cutter declines to", which overstates his abstention: he declines to adjudicate the *strength*, having supplied the conditional *structure*.
- **Adjudication**: the article's conclusion is **correct on its own terms and is not an error of reasoning**. The asymmetry is a function of `P(divergence | ensoulment)`, which Cutter parks at "(say) 50%". Minimal Quantum Interaction pushes that likelihood toward 1, and as it does, Cutter's own arithmetic drives the posterior on identical outputs toward 0 — i.e. convergence *becomes* the decisive result. The Map's inversion is the principled consequence of supplying the parameter Cutter leaves open.
- **Resolution**: the derivation is now explicit rather than asserted. The claim is made *inside Cutter's own arithmetic* — a genuine in-framework (Mode One) move where the article previously had a bare contrary assertion. The article also now states why divergence is the weaker signal in the Map's hands: Cutter's idealisation gives a causally closed machine no way at all to diverge, where real hardware has thermal noise and uncorrected error.
- This is the strongest single improvement available on the page, and it exists only because the source was read rather than the review's account of it.

## Lenses run to reach the conclusion

Per the standing warning that a convergence/no-op stability note marks an **unrun lens**, not a clean file — the note on `deep-review-2026-07-17` was treated as such by today's pessimistic pass, which found six defects, and is treated as such again here.

| Lens | Outcome |
|---|---|
| Quote fidelity, all 27 quoted strings vs. **raw full text of both papers** | **3 findings** — 23 verbatim on first pass, 3 resolved as normalisation/case artefacts, **1 fabricated** (Issue B) |
| Source-argument fidelity (A1/A2 structure, F-constraint, §3.3, fitting-recipient) | **Clean** — all six repairs faithful |
| Result-direction / comparative-inversion leg | **1 finding** (Issue C) — the highest-yield lens this run |
| Superlative / scope claims | **1 finding** (Issue A) |
| Cited-author-stance | **Clean** — Cutter is presented as a substance dualist whose ontology the Map declines; Békefi as a critic of the support, not a proof of impossibility |
| Section/heading numbering vs. source | **Clean** — "3.3. Causal Differences" verified exactly |
| Békefi argument order | **Clean** — Békefi §2 = fitting-recipient, §3 = alien-analogy, so "takes them in reverse order" is correct |
| Terminology gloss ("non-libertarian rational agency") | **Clean** — term absent from Cutter, but it is a faithful standard gloss of his "rational agency that don't involve incompatibilist freedom (e.g., the kind of agency endorsed by compatibilists)". Not a defect; recorded so a later pass does not re-flag it |
| Citation metadata at publisher of record | **Not re-run** — cleared by the pessimistic pass this morning against the same artefacts; masthead and DOI re-confirmed incidentally during retrieval |
| Editor-vocabulary label leakage | **Clean** — zero hits on all forbidden tokens |
| Wikilink resolution / Hugo body | **Clean** — 0 unconverted `[[` in the Hugo body |
| Length | 2464 → **2609** words, `ok` → `soft_warning`, hard 3500, **890 words headroom** |

## Strengths Preserved

- The front-loaded lead naming both assumptions, both arguments, Cutter's interactionism section and both objections — untouched.
- The "what transfers / what does not transfer" split — untouched apart from the de-quoting in Issue B.
- The circularity-charge answer, which concedes the charge's bite before stating the partial escape. This is the best paragraph on the page and was not modified.
- Both calibration bounds and the `≥ 0.25` precisification, as installed this morning.

## Remaining Items

None minted as tasks. Two observations carried for whoever next touches the page, neither a defect:

1. Békefi's §2.2 explicitly argues that **humans do meet** the Integrity condition. The article reports the integrity objection without that leg. Adding it would strengthen the objection's presentation, and it bears on the Nagarjuna tension the pessimistic review carried (item 1 of its "Carried" list). Expansion surface, not an error.
2. Cutter's doubt about his own premise F2 — that the brain may amplify micro-scale indeterminism where computers are engineered not to — is now carried in the Map's voice in the circularity paragraph but is not attributed to Cutter as a doubt he raises about **himself**. Accurate as written; a later pass could make the attribution explicit at zero cost.

## Stability Notes

- **The 2026-07-17 convergence note is now twice disconfirmed.** Two prior deep-reviews with zero content changes were followed by a pessimistic pass finding six real defects and this pass finding three more. All nine were on the **source-fidelity** lens, which no pre-2026-09-18 pass ran against the primary texts. Convergence damping should not be read as a clean bill on this article until a pass records that it read Cutter and Békefi in full. This one did.
- **Bedrock, do not re-flag**: Cutter's soul-as-separate-substance ontology is a framework choice the Map declines while adopting his interactionist causal framing. That divergence is marked in the article and is not a defect.
- **Bedrock, do not re-flag**: the residue after Cutter's two blunting moves — how much indeterminism ensoulment predicts — is a genuine framework-boundary disagreement, and the article marks it as such rather than claiming to have closed it. Correct as written.
- **Do not re-flag as an inversion**: the article's claim that persistent convergence is the informative outcome *contradicts Cutter's footnote 36 by design*, and the article now shows the derivation. A future pass that greps Cutter and finds the opposite asymmetry should read the paragraph before flagging it.
- **Model attribution**: the three early-morning refine passes left `ai_system` at `claude-opus-4-8` and the changelog's file-level `ai_system` is a four-way join, so **which model executed them cannot be established from the repository**. Not guessed. This pass appended `claude-opus-5` to the dual form rather than overwriting.
