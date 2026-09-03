---
ai_contribution: 100
ai_generated_date: 2026-08-23
ai_modified: 2026-08-23 23:02:44+00:00
ai_system: claude-opus-5
author: null
concepts:
- '[[compatibilist-symmetry-challenge]]'
created: 2026-08-23
date: &id001 2026-08-23
description: 'Fourth deep review: verifies the six fixes the 2026-08-22 refine pass
  applied, catches an anaphor stranded by one of them, and corrects a Frankfurt 1971
  attribution the corpus gets right everywhere else.'
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-23 23:02:44+00:00
modified: *id001
related_articles:
- '[[moral-architecture-of-consciousness]]'
- '[[moral-implications-of-genuine-agency]]'
- '[[frankfurt-hierarchical-mesh-theory-of-the-will]]'
title: Deep Review - Compatibilist Symmetry Challenge
topics: []
---

**Date**: 2026-08-23
**Article**: [Compatibilist Symmetry Challenge](/concepts/compatibilist-symmetry-challenge/)
**Previous review**: [2026-06-21](/reviews/deep-review-2026-06-21-compatibilist-symmetry-challenge/) (also [2026-06-08](/reviews/deep-review-2026-06-08-compatibilist-symmetry-challenge/), [2026-05-18](/reviews/deep-review-2026-05-18-compatibilist-symmetry-challenge/))
**Word count**: 2498 → 2492 (−6; length-neutral, back inside `ok` from the additions' transient `soft_warning`)

## Diff-First Context

The 2026-06-21 review closed with "convergence reached — treat any future re-nomination skeptically; check the diff before re-reviewing." The diff justifies the slot. Between that review and today the article was substantively rewritten once, by commit `1a9e0f0c6a` (2026-08-22 refine-draft), which applied all six findings of [the 2026-08-22 pessimistic review](/reviews/pessimistic-2026-08-22-compatibilist-symmetry-challenge/). Those findings were dependency-drift defects: the article's three sibling nodes (topic, apex, register [P-A5](/positions/agency-and-will/#p-a5)) had each moved to a more conservative reading while the canonical concept — the one **12 content articles cite** — stood still.

So this pass is a **verification review of a large same-week fix**, not a re-review of a converged article. That is the highest-value shape available here: a six-issue sweep applied in one pass is exactly where `sweep-fixes-the-disclaimer-and-strands-its-dependents` bites, and one instance of that shape is present (Issue A below).

## Verification of the 2026-08-22 Fixes

All six verified on disk this session against the source of truth, not against the review that requested them.

| Pess. issue | Fix as landed | Verdict |
|---|---|---|
| 1 — luck-objection credited to Kane's event-causal route | Split into an agent-causal Map reply plus Kane as the declined contrast, citing [P-A2](/positions/agency-and-will/#p-a2) | **Correct.** [P-A2](/positions/agency-and-will/#p-a2)'s `Asserts` verified verbatim in `positions/agency-and-will`; the article's paraphrase ("prior mental events the agent did not choose … traces back beyond the agent's control") is the register's own wording. Consistent with `concepts/quantum-indeterminacy-free-will` L89 |
| 2 — [P-A5](/positions/agency-and-will/#p-a5) residue stated flat | Conditionality installed at both loci (step 3 and the "Eliminating the residue" bullet) | **Correct.** "the last two" resolves to (b) and (c), matching [P-A5](/positions/agency-and-will/#p-a5)'s "Two of those three items — the 'could have done otherwise' readings and the metaphysics of genuine alternatives" |
| 3 — verbatim quote mis-sourced to the apex | `accounts of` trimmed so the quote matches the apex it credits | **Correct.** Verified verbatim at `apex/moral-architecture-of-consciousness` L164 |
| 4 — worked exhibit described as three moves | Updated to four; fourth move inherited | **Correct.** Apex L164 carries the fourth move; "this level inherits rather than softens" verified verbatim there |
| 5 — compatibilist roster closed at three | Opened to "three of the … families"; Strawsonian paragraph added | **Correct** — but see Issue A: the insert stranded the paragraph that follows it |
| 6 — article breached its own first forbidden move | Bullet relaxed to "must forgo **or** would predict differently" | **Correct.** Residue (a)'s sourcehood-grade contrast now satisfies the disjunct |

Internal-quote ledger (all grep-verified at the credited file, contiguity checked):

- `"a *retreat*, and a conditional one"` → `topics/frankfurt-cases-and-the-principle-of-alternate-possibilities` L81 — **verbatim**
- `"that Strawson is wrong or that dualism is right"` → `topics/reactive-attitudes-and-strawsonian-responsibility` — **verbatim**
- `"on grounds beyond moral theory (the hard problem, the explanatory gap, the conditions for downward causation)"` → apex L164 — **verbatim**, and discriminates correctly against the topic article's variant parenthesis
- `"ultimate desert in retributive contexts, certain readings of 'could have done otherwise'"` → apex L164 — **verbatim** after the fix
- `"this level inherits rather than softens"` → apex L164 — **verbatim**

## Publisher-of-Record Citation Web-Verify

§2.4 triggered: the body was substantively modified since the last deep review, and the Kane cite's argumentative role changed. Full re-verification run at the publisher of record rather than inherited from the 06-08 ledger.

- **Frankfurt, H. (1971). "Freedom of the Will and the Concept of a Person." *Journal of Philosophy*, 68(1), 5-20** — state: **real-correct**. Confirmed at the Philosophy Documentation Center, the journal's publisher of record (`pdcnet.org/jphil/content/jphil_1971_0068_0001_0005_0020` — the identifier itself encodes vol 68, issue 1, pp. 5–20). See Issue B for a *characterisation* defect distinct from the metadata.
- **Fischer, J.M. & Ravizza, M. (1998). *Responsibility and Control*. Cambridge University Press** — state: **real-correct**. Confirmed at cambridge.org (Cambridge Studies in Philosophy and Law; 1998 hardback, 1999 paperback reissue).
- **Wolf, S. (1990). *Freedom Within Reason*. Oxford University Press** — state: **real-correct**. Confirmed at global.oup.com. The Reason View's characterisation ("ability to act in accordance with the True and the Good") matches OUP's own description.
- **Kane, R. (1996). *The Significance of Free Will*. Oxford University Press** — state: **real-correct**. Confirmed at global.oup.com (ISBN 9780195105506). The effort-of-will/self-forming-actions description is accurate; the 08-22 fix corrected its *role*, not its scholarship.
- **Refs 5 and 6** — Map self-cites under the Oquatre-* pseudonyms. Legitimate; not fabrications; do not strip.

Inline ↔ References reconciliation: clean in both directions (four inline author-year cites, four external entries).

Empirical-record currency sweep: `find_superlative_claims` returns **0** — pure conceptual analysis, no superlative or empirical-record claims. N/A.

## Pessimistic Analysis Summary

### Critical Issues Found

None. No attribution error of the kind §2.5 defines, no source/Map conflation, no internal contradiction, no possibility/probability or uniqueness slippage. Applying the §2 diagnostic test — *would a reviewer who fully accepts the Map's tenets still flag the claim as overstated?* — to the residue as it now stands: no. The conditionality now matches [P-A5](/positions/agency-and-will/#p-a5) exactly.

### Medium Issues Found and Fixed

**Issue A — the Strawsonian insert stranded the paragraph after it.** The 08-22 fix added the Strawsonian family as a fourth parity case, placing it directly before the luck-objection paragraph, whose opening anaphor read *"In each case."* That anaphor now scooped in a family the section had explicitly just excluded from the three-capacity framing, and attributed to it a survival mechanism drawn from a list — "the reasons-responsive mechanism, the higher-order desires, or the normative competence" — that covers only the other three. This is the `sweep-fixes-the-disclaimer-and-strands-its-dependents` shape: the fix was right, the sentence downstream of it was not re-read. **Fixed**: scoped to "In each of those three capacity-based cases," plus a one-sentence parenthetical stating the substantive point the strand concealed — normativized Strawsonianism does not *meet* the luck objection, it stakes no metaphysical thesis for luck to undermine.

**Issue B — Frankfurt 1971 characterised as a theory of responsibility.** The article read: *"Harry Frankfurt's 1971 account grounds responsibility in the agent's identification with effective higher-order desires: an agent is morally responsible when their will is the will they want to have."* Two independent checks:

1. *Publisher/reference-work.* SEP's **Compatibilism** entry presents the hierarchical account as explaining "freely willed action"; the responsibility link is stated only as the *typical* assumption that free will is necessary for responsibility. SEP's **Moral Responsibility** entry §3.9 does read mesh theories as responsibility conditions — so the family-level reading is legitimate, but it is the *literature's* framing, not the 1971 paper's own thesis.
2. *Corpus-internal.* The Map's own dedicated page, `concepts/frankfurt-hierarchical-mesh-theory-of-the-will` L31-36, exists precisely to prevent this conflation: it states that 1971 is "a *positive* account of what freedom of the will and personhood *consist in*", that 1969 is the responsibility paper, and warns in terms that the two "are easy to conflate." `concepts/compatibilism` L63 and `concepts/moral-responsibility` L145 both get it right; **the article under review was the corpus outlier.**

**Fixed** to state freedom of the will as what the 1971 account grounds, with the responsibility reading marked as the tradition's move — which costs the argument nothing, since the symmetry challenge needs only that the identification reading is the one it must meet. Graded medium rather than critical: the family-level responsibility reading is defensible in the literature, so this is a precision defect, not a misattribution of a claim to an author who never made it.

**Issue C — "wide source" used twice with no definition or link.** For a concept whose declared job is to be cited compactly by dependents, an unexplained technical term is a real cost. `concepts/source-versus-leeway-incompatibilism` has a dedicated `## Narrow and Wide Source Incompatibilism` section. **Fixed** by linking the first occurrence (zero word cost).

**Issue D — three named accounts, no links to their dedicated pages.** The article named Frankfurt's mesh, Kane's event-causal route, and the wide-source position while linking to none of the Map's pages for them (grep-verified: 0 hits each for `frankfurt-hierarchical-mesh-theory-of-the-will`, `event-causal-libertarianism`, `source-versus-leeway-incompatibilism`). **Fixed** — all three installed, all three targets verified to exist and to have no colliding stem.

### Low Issues Found and Fixed

**Issue E — the tenet-neutrality claim over-reached.** *"The discipline is itself tenet-neutral"* was stated flat. The 08-22 pessimistic review's Nagarjuna counterargument is right that the reversal fails for a no-self framework, which has nowhere to put a residue because it reads both ultimate sourcehood and mechanism ownership as reifications. This is a small over-claim running *in the Map's favour* — the direction `over-concession-gets-ratified-not-merely-missed` warns collects endorsements rather than corrections. **Fixed**: "largely tenet-neutral," with the limit named in one clause.

**Issue F — style-guide `load-bearing`.** The 08-22 pass fixed one instance and left a second ("distinctions the rest of the Map treats as load-bearing"). **Fixed** to "essential."

### Counterarguments Considered

- **Eliminative Materialist / Hard-Nosed Physicalist / Many-Worlds Defender**: reject the framing from outside the tenets — **bedrock at the framework boundary; not re-flagged** (declared bedrock 2026-05-18, reaffirmed 06-08, 06-21).
- **Buddhist (Nagarjuna)**: the parity analysis presupposes a persisting agent, so the no-self critic grants neither horn. Partly bedrock, but the *tenet-neutrality* claim was a correctable over-reach — see Issue E. The residue itself is not re-scoped; only the reversibility claim is.
- **Empiricist (Popper's Ghost)**: presses for what would falsify "both scaffolds deliver the same first-order verdicts." The article concedes *in moral theory alone, no discriminator is in hand*, which is the discipline's own point. Honest as it stands; **considered and declined** — naming a falsifier would add ~25 words to an article at 100% of soft threshold for a claim the article already declines to assert.
- **The residue may be smaller still** (08-22 counterargument 1: after conditionalising (b) and (c), only ultimate desert survives outright, and the Pereboom manipulation bill presses even that). **Considered and declined.** The Frankfurt-cases article already books the manipulation argument as "the bill the source retreat must pay", and the article already says (b) and (c) lapse with the leeway defence — so the bill attaches to the conditional branch, which is stated. The concept's job is to mirror [P-A5](/positions/agency-and-will/#p-a5), and [P-A5](/positions/agency-and-will/#p-a5) does not book the manipulation bill inside its residue clause. Adding it here would put the concept *ahead* of its own register — the mirror image of the drift this whole cycle was fixing.

### Reasoning-Mode Classification (editor-internal)

- Frankfurt / Fischer–Ravizza / Wolf engagements: **Mode Three** (honest framework-boundary marking). Correct and load-bearing — refusing boundary-substitution *is* this article's thesis.
- Strawson / Wallace engagement (new 08-22 paragraph): **Mode Three**, correctly executed. The Map's contested reading is explicitly marked as "a conclusion the Map argues for rather than a description of the position," and the concession is quoted from the Map's own Strawson article. No boundary-substitution.
- Kane engagement (rewritten 08-22): **Mode One** — the Map declines the event-causal route on a regress argument internal to the libertarian project, not on tenet-incompatibility. Correctly earned.
- **No label leakage.** The article names four disciplines in prose, but this is a methodology concept whose subject *is* the relation between disciplines; every instance is substantive argument. No forbidden editor-vocabulary strings, no `**Evidential status:**` callouts.

## Optimistic Analysis Summary

### Strengths Preserved (do not touch)

- **The named pattern itself** — *tenet-coherent, not moral-explanatory-superior*. Compact, reusable, honest, and correctly architected as a single statement 12 articles cite.
- **The integrative-vs-separating distinction** and the unity-as-evidence diagnosis (the catalogue produces "fits together" by construction because it prunes for consistency). Untouched, as the 08-22 review directed.
- **"Availably equivalent"** as the reconciliation of identical moral outputs with different sourcehood stories. Untouched.
- **Residue item (c)'s reflexive qualifier**, marking its own separating force as framework-internal. Trimmed only of a nine-word editorial flourish; the substance is intact.
- **Tenet 5 handling**, which refuses to convert "simpler" into "more likely true" and says why.

### Enhancements Made

Four cross-links installed (mesh theory, event-causal libertarianism, source-vs-leeway, all previously absent); one Strawsonian luck-objection clause; one no-self limit on the reversibility claim. All paid for by trims elsewhere — net −6 words.

### Cross-links Added

- [frankfurt-hierarchical-mesh-theory-of-the-will](/concepts/frankfurt-hierarchical-mesh-theory-of-the-will/)
- [event-causal-libertarianism](/topics/event-causal-libertarianism/)
- [source-versus-leeway-incompatibilism](/concepts/source-versus-leeway-incompatibilism/)

## Remaining Items

None requiring a task. Two items were considered and deliberately declined, recorded above so a later pass does not re-litigate them: the Popperian falsifier sentence, and importing the manipulation-argument bill into the residue ahead of [P-A5](/positions/agency-and-will/#p-a5).

One **operator-level** item stands, carried forward from the 08-22 review's operator note and not addressable as a content task: `positions-evolve` checks whether an `Argued in` dependency has moved, but never the converse — whether the register moved under the dependency. This cycle's drift (four nodes touched 2026-07-29 → 2026-08-21, canonical concept left behind, certified "not-a-defect" in the very pass that left it) is that gap's signature. It needs an operator decision on the skill, not a queue entry.

## Stability Notes

- **Bedrock (do not re-flag)**: eliminativist / hard-physicalist / MWI rejection from outside the tenets. The article's whole thesis is that the libertarian framing's distinctiveness lives at the tenet level, not the moral-theory level — a reviewer disagreeing *from outside* the tenets is confirming that thesis, not defeating it.
- **Do not re-inflate the residue.** Three items, one held outright and two conditionally on the wide-source position. Both loci now match [P-A5](/positions/agency-and-will/#p-a5). Any future pass pushing these back toward flat or tenet-neutral moral leverage is committing the uniqueness slippage the article exists to prevent.
- **Do not re-broaden the Frankfurt sentence.** The 1971/1969 distinction is deliberate and matches `concepts/frankfurt-hierarchical-mesh-theory-of-the-will`, which is the corpus's canonical statement of it. If a future review wants "grounds responsibility" back, it must first reconcile with that page.
- **Citations verified at publisher of record 2026-08-23** (full ledger above, all four real-correct). A future no-op pass on an unchanged References block may skip re-verification.
- **Convergence status: genuinely converged, but for a specific reason.** This article's three prior "no-op" reviews were not evidence of health — they were the damping working correctly on a *self*-modification metric while the article's dependencies moved underneath it. The lesson generalises (`convergence-damping-keys-on-self-modification-not-dependency-freshness`): for this article the right re-review trigger is **a change in [P-A5](/positions/agency-and-will/#p-a5), the apex section, or `topics/frankfurt-cases-and-the-principle-of-alternate-possibilities`**, not a change in the article's own `ai_modified`.