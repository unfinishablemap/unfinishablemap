---
title: "Pessimistic Review - 2026-10-05 - The Process 1 Specification Problem and its six reciprocals"
created: 2026-10-05
modified: 2026-10-05
human_modified: null
ai_modified: 2026-10-05T13:11:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-fable-5-1
ai_generated_date: 2026-10-05
last_curated: null
---

# Pessimistic Review

**Date**: 2026-10-05
**Content reviewed**: `concepts/process-1-specification-problem` (created 2026-09-28, one deep review, no prior pessimistic review), the six reciprocal sentences installed today by commit 698b0ed8f5 (`quantum-zeno-effect` L76, `post-decoherence-selection` L88, `selection-criterion-problem` L89, `ensemble-level-epiphenomenalism` L39, `agency-budget` L97, `von-neumann-wigner-interpretation` L92), and the sibling pages that cite the same Georgiev–Stapp exchange (`conservation-laws-and-mental-causation` L113/L117, `psychophysical-laws-bridging-mind-and-matter` L143, `stapp-quantum-mind` L132).

**Not covered**: today's edits to `topics/death-and-consciousness`, `topics/responsibility-gradient-from-attentional-capacity` and `apex/phenomenal-variation-within-a-species` were considered and passed over. The Process 1 page was chosen because six pages now defer to it and it had never had an adversarial read. The Parfit quotation and Sullivan reference added to `death-and-consciousness` were read in the diff only and nothing was flagged; that is not a review.

**Sources re-read for this review**: Stapp 2000 (arXiv quant-ph/0010029), Donald 2003 (quant-ph/0311158), de Barros 2014 (arXiv:1404.0714), Georgiev 2015 *IJMPB* (arXiv:1412.4741), and Stapp's 2012 reply in the LBL `Reply.doc` draft (converted with LibreOffice, 3,268 words). All findings below quote those texts.

## Executive Summary

The page's quotes hold, and its refusal to claim a refutation is sound. Its weaknesses are in the story it tells about the quotes. It presents the narrowing of "which question" to consent-and-timing as something that happened under pressure from three critics, when Stapp's 2000 paper already states it, three years before the first critique, and also states where the question comes from, in a passage the page never uses. It applies Georgiev's theorem to the Map's own default and to the decoherence-free-subspace option but not to the Laskey repair, which is a Zeno drag that the theorem covers. And one of today's six reciprocal sentences misstates what Georgiev's averaging argument returns. Two older sibling pages still carry versions of the exchange that the new page's own sources contradict.

## Critiques by Philosopher

### The Eliminative Materialist
Churchland would say the page spends 2,750 words asking who fixes a projector for a chooser nobody has shown to exist. The deep review of 2026-09-28 ruled this a framework-boundary disagreement and its stability note says not to re-flag it. Not re-flagged.

### The Hard-Nosed Physicalist
Dennett would press Donald's "homunculus" line harder than the page does. The "Primitive choice" response says demanding a mechanism "begs the question against interactionism". Dennett's reply is that the demand is for a specification, which is what the page itself says is owed, so the primitive-choice response is in tension with the page's thesis. The page half-sees this ("a primitive chooser still needs a set to choose from"). It could say outright that primitive choice answers the mechanism demand and leaves the specification demand untouched. Low severity.

### The Quantum Skeptic
Tegmark would note that the page's "open crux" is narrower than it reads. Georgiev's proof of Theorem 4 contains the sentence "If ρ̂0 is diagonal in that basis, it will remain unchanged by the action of the projectors and the entropy will stay the same." An interval projector in the coordinate basis, applied to a density matrix diagonal in that basis, therefore changes nothing unconditionally. The only open case is the near-diagonal one, where Schrödinger spreading rebuilds off-diagonal terms between projections. The page says the reply "does not address" this without saying that the cited paper settles the exact case. See Issue 3.

He would also note that the Laskey repair, as de Barros writes it, is a Zeno drag to a chosen state "with probability one". That is the mechanism Theorem 4 targets. See Issue 2.

### The Many-Worlds Defender
Deutsch would point out that Georgiev's "unconditional density matrix" is, in Georgiev's own words, "the state of the multiverse in no collapse models", and that his averaging argument says a Born-consistent collapse theory and a no-collapse theory agree on it. The page's Relation section treats this as a cost the Map carries (ensemble-level epiphenomenalism). That is the honest reading. The reciprocal sentence on `ensemble-level-epiphenomenalism` L39 garbles it, though: see Issue 4. The broader MWI objection is covered by the stability note and is not re-flagged.

### The Empiricist
A Popperian would ask what "could in principle be observable" means for the Laskey repair. De Barros says the *brain's cyclic apparatus* would be observable, a claim about neural dynamics. The page's "has an in-principle signature" can be read as saying the mind's contribution has a signature. It does not: under Born-consistent projection the unconditional statistics are fixed by Theorem 4. One clause would fix this and Issue 2's proposed text covers it.

### The Buddhist Philosopher
Nagarjuna's objection (the chooser is a construct) was ruled out of scope by the deep review. One point survives in the page's own terms: Stapp 2000 says the experience "must be determined largely by the brain" and reduces free choice to consent. A chooser whose only act is assent to a brain-computed candidate is a thinner self than the page's "the mind chooses" language suggests. This supports Issue 1.

## Critical Issues

### Issue 1: The "narrowing under pressure" story inverts the chronology, and the page omits Stapp's own statement of where the question comes from
- **File**: `obsidian/concepts/process-1-specification-problem.md`
- **Location**: lead L33 ("Stapp's own later wording … both pay it the same way"), L39 ("Process 1 as stated supplies none"), L77, Relation L91 ("under pressure 'which question' narrows")
- **Problem**: The consent wording is from Stapp 2000. Donald (2003) quotes it and presses his representation objection anyway; Georgiev (2012, 2015) and de Barros (2014) come later still. So it is not "later wording", it did not arise "under pressure", and it cannot "pay" a debt that Donald raised with the wording in front of him. The body at L77 gets the date right ("In 2000 he located…"), so the lead and the Relation section contradict the body.

  The same paragraph of Stapp 2000 goes further than the page reports. Verbatim: "But then what fixes experience? How is E determined? … The experience E cannot just pop out of nothing: it must be determined largely by the brain." And: "The 'best' option should be the one such that P(E) has the greatest statistical weight. Let E(t) be the E that maximizes Tr S(t)_b P(E)." Then: "Thus the 'free choice' can be reduced to consent, at certain instants t, to put to Nature the question of whether experience E(t) will occur." Stapp also addresses the basis problem in that passage: decoherence "is helpful, but it is not sufficient", and "the basis is fixed by the experience of 'the observer'".

  Two consequences. First, L39's "Process 1 as stated supplies none" (of basis, grain, map) is too strong against a source the page cites: Stapp 2000 supplies a rule for picking the question from a family of experience-projectors. What it does not supply is the family, the assignment of P(E) to E. That is a narrower and more accurate debt. Second, the page's best result (brain supplies the question, mind supplies assent) is presented at L77 as an inference from "consent over a supplied question". It is Stapp's stated position, and quoting it would turn an inference into a citation.
- **Severity**: High (the lead misdescribes the dialectic the page exists to report, and six pages now point here)
- **Recommendation**: Priority item 1.

### Issue 2: Georgiev's theorem is never applied to the Laskey repair, and "the three critiques converge" is not what the sources show
- **File**: `obsidian/concepts/process-1-specification-problem.md`
- **Location**: L77 ("Read at source, the three critiques converge…"), L81 ("Brain-supplied basis, mind-supplied timing")
- **Problem**: De Barros's text of the repair: the brain's apparatus "superposes the system into two possible states given by the basis |α + γ sin(ωt)⟩⟨α + γ sin(ωt)| or 1̂ − …", and "If … the mind continuously observes the system between a time t′, 2πn ≤ t′ ≤ 2πn + π/2, an irreversible change happens, with complete loss of coherence, and the system ends in the state |α + γ⟩ (notice that a continuous observation leads to a probability one for the QZE)". Timing over a cycling basis is therefore a choice among a one-parameter family of bases, and sustained observation drags the state to a target. This is the Zeno mechanism, with the basis family supplied by the brain.

  Theorem 4 covers projective measurements "using a freely chosen set of projection operators" that are orthogonal and complete. The page's "How the Debt Might Be Paid" paragraph applies Georgiev to the decoherence-free subspace and to the Map's post-decoherence selection, and says nothing about whether the Laskey repair survives him. On the page's own account of the dilemma it does not obviously survive: if the cycling family differs from the pointer basis, the drag raises entropy; if it is the pointer basis, redundancy returns. The page calls the repair "non-circular" and credits it with "an in-principle signature" and stops. That is asymmetric treatment of the option closest to Stapp and of the Map's own default.

  "The three critiques converge on a Process 1 in which basis and grain come from the brain" is the page's synthesis of Stapp 2000, Stapp 2012 and de Barros. Donald proposes no such thing. Georgiev's verdict on a mind confined to the environment's basis is the opposite of an endorsement: "Such scenario … makes the mind efforts useless from a functional viewpoint, because the action of the mind becomes redundant with the action of the environment."
- **Severity**: High
- **Recommendation**: Priority item 2.

### Issue 3: The simulated breakdown is conditional on a pointer basis Stapp denies, and the page's "open crux" omits what Georgiev's proof already settles
- **File**: `obsidian/concepts/process-1-specification-problem.md`
- **Location**: L57, L69
- **Problem**: Georgiev stipulates the pointer basis: "we could choose Ĥint such that it diagonalizes the density matrix of the brain ρ̂ in a basis different from the position basis. Here, we take the pointer basis to be the energy basis". Stapp's 2012 reply says the decoherence basis is the coordinate basis. For that case Georgiev's own conclusion is "Only in the special case when both the mind and the environment perform projective measurements upon the brain in the same basis, one could expect to observe quantum Zeno effect for timescales larger than the decoherence time τ", followed by the redundancy charge. The page reports "with decoherence in a different (energy) pointer basis" at L57 and Stapp's coordinate-basis concession at L67 and never joins them: on Stapp's stated basis the "random telegraph" result does not apply, and the whole dispute is redundancy. L69's "settles the basis horn in Georgiev's favour" hides this.

  The proof sentence quoted under the Quantum Skeptic above settles the exactly diagonal case of the crux. The page should say so.
- **Severity**: Medium
- **Recommendation**: Priority item 2 (same file, same pass).

### Issue 4: Today's reciprocal on `ensemble-level-epiphenomenalism` misstates Georgiev's averaging argument
- **File**: `obsidian/concepts/ensemble-level-epiphenomenalism.md`
- **Location**: L39, "averaging Born-consistent collapses over outcomes returns the density matrix decoherence already gave."
- **Problem**: Georgiev: "one could statistically average over all possible outcomes obtained from Eq. 4 to get the very same unconditional density matrix that is predicted by no collapse models." The comparison is collapse against no-collapse descriptions of the *mind's* projections. When the mind's basis differs from the pointer basis, that matrix is not the one decoherence gave; it has higher entropy, which is the theorem's whole point. "Returns the density matrix decoherence already gave" is true only for a selection among pointer outcomes, which is the Map's post-decoherence case and is correctly stated that way on `post-decoherence-selection` L88 and on the source page L81. The L39 sentence says it is "aimed at Stapp's Zeno model", where it is false in general.
- **Severity**: Medium (a one-clause fix; installed three hours ago, no review has seen it)
- **Recommendation**: Priority item 4.

### Issue 5: Two sibling pages report the exchange in ways the new page's sources contradict
- **File**: `obsidian/concepts/conservation-laws-and-mental-causation.md` L113, L117; `obsidian/topics/psychophysical-laws-bridging-mind-and-matter.md` L143
- **Problem**:
  - `conservation-laws` L117: "Stapp responds that these simulations oversimplify the quantum system". Nothing consulted supports this. The Monte Carlo paper is 2015; Stapp's only later reply is the *NeuroQuantology* 13(2) rejoinder, known by its abstract alone ("a simple proof that environmental decoherence does not nullify the quantum Zeno effect"). Georgiev 2015 §1 reports a simplicity complaint from Stapp, but about the *2012* two-level photon model, and says the 2015 n-level theorem was built to answer it ("Stapp objected that the argument is based on an improper extrapolation of a theorem valid for a two-level system … Here, we prove a generalization"). The page has the order backwards. The sentence also cites "Georgiev's Monte Carlo simulations" with no Georgiev 2015 entry in References (the only Georgiev entry is Georgiev & Glazebrook 2014).
  - `conservation-laws` L113: "prolonging desired neural configurations against decoherence". Stapp 2012: the claim that Zeno cannot slow decoherence "is certainly correct, but in no way contradicts my model". The Process 1 page L67 reports this. On Stapp's own account the holding is against Schrödinger spreading.
  - `psychophysical-laws-bridging` L143 states the breakdown without its condition (pointer basis different from the mind's). See Issue 3.
- **Severity**: Medium
- **Recommendation**: Priority item 3.

## Counterarguments to Address

### "Primitive choice" against the specification demand
- **Current content says**: Stapp's free choice is no more owed an explanation than the Copenhagen experimenter's; demanding a mechanism begs the question against interactionism.
- **A critic would argue**: The Copenhagen experimenter's choice is physically specified by the apparatus they build. The analogy fails at the one point at issue, which is de Barros's apparatus argument. The page reports de Barros two sections earlier and does not turn him on this response.
- **Suggested response**: One clause in the "Primitive choice" sentence: the analogy answers the mechanism demand and fails on specification, since the experimenter's question is fixed by apparatus. Low priority; not on the Priority List.

### The dilemma's date
- **Current content says**: "Danko Georgiev (2015) turns the decoherence-timing objection into a basis dilemma."
- **A critic would argue**: Stapp's 2012 reply quotes Georgiev 2012 already raising the same-basis case: "Stapp investigates a particular case in which the brain is measured by the environment in the very same measurement basis in which the mind makes the wave function collapse." Stapp's "this does not make the latter redundant" answers a redundancy point made in 2012. The 2015 paper states the dilemma in full, with the theorem, but at least one horn is older.
- **Suggested response**: Lead only. Georgiev 2012 was not re-read for this review (the research note says "Not re-read here" too). If it is obtained, check whether "(2015)" in the lead should read "(2012, 2015)".

## Unsupported Claims

| Claim | Location | Needed Support |
|-------|----------|----------------|
| "Stapp responds that these simulations oversimplify the quantum system" | `conservation-laws-and-mental-causation` L117 | No source; chronology is against it. Replace (Priority item 3). |
| "The theorem's scope is narrower than its title" | `process-1-specification-problem` L63 | Theorem 4 has no title. The paper it appears in is "Monte Carlo simulation of quantum Zeno effect in the brain". The "No-go theorem" title belongs to the *NeuroQuantology* paper, consulted by abstract only. |
| "has an in-principle signature" | `process-1-specification-problem` L81 | De Barros says the brain's cyclic dynamics "could in principle be observable". He does not say the mind's choice would be. |
| The debate over the no-wavefunction objection "remains open", piped to the Process 1 page | `stapp-quantum-mind` L132 | The Process 1 page never discusses the no-wavefunction objection. `forward-in-time-conscious-selection` L97 attributes the same objection to "Georgiev (2017)", this page to "Georgiev (2012)". Two pages, two dates: one needs checking at source. Lead only. |
| Body quotes from Stapp's 2012 reply represent the printed reply | `process-1-specification-problem` L67 | The page already flags "body wording not checked against print". There is now positive evidence of divergence: Georgiev 2015 §1 says the printed reply argued that the two-level photon model "is too simple to represent a human brain" and that Stapp "agreed that the proof of the particular theorem is correct". The LBL draft contains none of the words "two-level", "photon", "theorem" or "simple" (case-insensitive grep of the full converted text), and its one use of "proof" says Georgiev's "proof depends upon a fifth property that my model does not have". Either print differs materially from the draft or Georgiev paraphrases freely. The caveat should stay and the print should be obtained. |

## Language Improvements

| Current | Issue | Suggested |
|---------|-------|-----------|
| "Stapp's own later wording" (L33) | False for the consent passage (2000) | See Priority item 1 |
| "under pressure 'which question' narrows" (L91) | The narrowing predates the pressure | See Priority item 1 |
| "the three critiques converge" (L77) | The critics do not converge; two Stapp texts and de Barros do | See Priority item 2 |
| "settles the basis horn in Georgiev's favour" (L69) | Stapp accepts the basis and denies the redundancy; nothing is settled in anyone's favour | See Priority item 2 |
| "narrower than its title" (L63) | The theorem has no title | "narrower than the 'no-go' label suggests" |
| "Behind both sits a further debt" (`quantum-zeno-effect` L76) | The specification problem does not sit behind the energy-conservation burden | "Beside both sits a further debt" |

## Strengths (Brief)

- Every quotation spot-checked against source held: the consent passage, the Laskey passage, Theorem 4, the lottery analogy, both horns, "admittedly speculative", and the eight Stapp 2012 phrases in the draft.
- The basis / grain / map decomposition is the right frame, and Issue 1 sharpens it without replacing it.
- The page applies Georgiev's unconditional-statistics point to the Map's own default and names the cost. Keep that; Issue 2 asks for the same treatment of the Laskey repair.
- Five of today's six reciprocal sentences state only what the source page says. `post-decoherence-selection` L88 and `selection-criterion-problem` L89 are exact.
- The "abstract only consulted" and "draft, not print" markers are honest and should survive any edit.

## Open tasks checked before recommending

`obsidian/workflow/todo.md` between `## Active Tasks` and `## Completed Tasks` was grepped (case-insensitive, fixed string) for `process-1`, `Georgiev`, `stapp-quantum-mind`, `conservation-laws-and-mental`, `psychophysical-laws-bridging`, `quantum-zeno-effect`, `agency-budget`, `ensemble-level`, `von-neumann-wigner`, `selection-criterion-problem`, `post-decoherence-selection` and `coupling-modes`. No open task owns any locus below. The hits were unrelated: the `thoughtful-local-friendliness` collapse-ordering task (uses the `post-decoherence-selection` lead as reference wording only), the observer-witness task (cites `stapp-quantum-mind` L100, a different locus), and agentic-social notes.

Prior review read: `reviews/deep-review-2026-09-28-process-1-specification-problem`. Its stability notes are respected: no physicalist, eliminativist or MWI objection to the chooser is re-flagged, no proposal pushes the page to a verdict on the grain crux, and the pseudonymous Map self-cites are untouched. Its Remaining Item on `born-rule-and-the-consciousness-interface` L165 is not re-recommended (that page is operator-blocked on length).

## Priority List

Word costs measured with `tools.curate.length.count_words` (new minus old). Each old string was confirmed to occur exactly once in its file. Lengths by `analyze_length`: `process-1-specification-problem` 2,750 (concepts hard 3,500); `conservation-laws-and-mental-causation` 3,813 (already over hard); `psychophysical-laws-bridging-mind-and-matter` 3,483 (topics hard 4,000); `ensemble-level-epiphenomenalism` 2,502; `quantum-zeno-effect` 2,878.

### 1. Process 1 page: correct the chronology and cite Stapp 2000 for where the question comes from
- **File**: `/home/andy/unfin/unfinishablemap/obsidian/concepts/process-1-specification-problem.md`
- **Type**: refine-draft
- **Total cost**: +84 words (2,750 → about 2,834)
- **(a) L33**, +28. Old: `Stapp's own later wording, and a fix de Barros credits to Kathryn Laskey, both pay it the same way: the brain supplies the basis, and the mind chooses only whether and when the question is put.` New: `Stapp's own wording of 2000, which predates all three critiques, and a fix de Barros credits to Kathryn Laskey make the same move: the brain supplies the question, and the mind chooses only whether and when it is put. The move shifts the debt to the brain's side without paying it, since Donald pressed his representation objection with that wording in front of him.`
- **(b) L77**, +37. Old: `Consent over a supplied question and timing over a cycling basis are the same move.` New: `The same paper says where the question comes from: the experience "must be determined largely by the brain", the candidate at each moment being the one whose projector has "the greatest statistical weight" in the brain's state. Consent over a supplied question and timing over a cycling basis are the same move.` Both quoted spans are verbatim and contiguous in arXiv quant-ph/0010029 (p. 8 of the PDF).
- **(c) L39**, +14. Old: `Process 1 as stated supplies none.` New: `Process 1 as stated supplies a rule for picking among experience-projectors, quoted below, and no account of the projectors themselves.`
- **(d) L91**, +5. Old: `Third, under pressure "which question" narrows to consent and timing over a brain-supplied basis.` New: `Third, "which question" has meant consent and timing over a brain-supplied question since 2000, before any of the critiques.`
- **Caution**: the description field says "Stapp's concession"; it stays accurate (the 2012 basis concession is real). After (c), check that L39's following sentence ("The three critiques below are three ways of arguing…") still reads correctly.

### 2. Process 1 page: run Georgiev against the Laskey repair, fix "the three critiques converge", and state what the proof settles
- **File**: `/home/andy/unfin/unfinishablemap/obsidian/concepts/process-1-specification-problem.md`
- **Type**: refine-draft (batch with item 1: same file, one pass, one `ai_modified` bump)
- **Total cost**: +145 words (items 1 and 2 together: 2,750 → about 2,979, 521 under hard)
- **(a) L81**, +72. Old: `has an in-principle signature, at the cost that "question-choice" no longer names what the mind does.` New: `has an in-principle signature, at the cost that "question-choice" no longer names what the mind does. It does not leave Georgiev's theorem behind. In de Barros's example sustained observation over part of the cycle carries the state to a chosen target with probability one, so timing over a cycling basis is a Zeno drag through a brain-supplied family of bases, and Theorem 4 covers any complete set of projectors. Unless that family is the pointer basis the drag raises entropy, and if it is, the redundancy horn returns.`
- **(b) L77**, +18. Old: `Read at source, the three critiques converge on a Process 1 in which basis and grain come from the brain and the mind contributes timing and assent,` New: `Read at source, Stapp's wording and de Barros's repair converge on a Process 1 in which basis and grain come from the brain and the mind contributes timing and assent (Georgiev's verdict on a mind confined to the environment's basis is that it is redundant),`
- **(c) L69**, +27. Old: `Nor does it address whether projecting onto a sub-interval of a density matrix already near-diagonal in that basis changes the *unconditional* statistics.` New: append `Georgiev's later proof settles the exactly diagonal case, where the matrix "will remain unchanged by the action of the projectors"; the near-diagonal case is the open one.` The quoted span is verbatim in arXiv:1412.4741, proof of Theorem 4.
- **(d) L69**, +28. Old: `The concession settles the basis horn in Georgiev's favour and moves the dispute to the grain.` New: `The concession puts Stapp on the same-basis horn, where Georgiev's simulated breakdown (run with an energy pointer basis) does not apply and his own text grants that the Zeno effect could persist; the charge there is redundancy, and the dispute moves to the grain.`
- **Caution**: the deep review's stability note forbids pushing the page to a verdict. Text (a) says the repair is inside the theorem's scope and names both horns; it does not say the repair fails. Keep it that way. The Relation section's third point (L91, "the mode is timing control under another name") stays true and needs no change.

### 3. Carry the corrected exchange to two sibling pages
- **Files**: `/home/andy/unfin/unfinishablemap/obsidian/concepts/conservation-laws-and-mental-causation.md`, `/home/andy/unfin/unfinishablemap/obsidian/topics/psychophysical-laws-bridging-mind-and-matter.md`
- **Type**: refine-draft
- **(a) `conservation-laws` L117**, +2. Old: `Georgiev's Monte Carlo simulations challenge whether the Zeno effect operates on the timescales required. Stapp responds that these simulations oversimplify the quantum system, but consensus has not emerged.` New: `Georgiev's (2015) simulations lose the effect past the decoherence time unless mind and environment share a basis; Stapp's rejoinder claims a proof to the contrary, and the [[process-1-specification-problem|exchange is unresolved]].` This also gives the page its first link to the Process 1 page.
- **(b) `conservation-laws` L113**, +1. Old: `prolonging desired neural configurations against decoherence.` New: `prolonging desired neural configurations against dynamical spreading.`
- **(c) `psychophysical-laws-bridging` L143**, +10. Old: `Georgiev's (2015) Monte Carlo simulations showed the quantum Zeno effect breaks down for timescales exceeding brain decoherence time.` New: `Georgiev's (2015) Monte Carlo simulations showed the quantum Zeno effect breaks down beyond the brain decoherence time when the environment decoheres in a basis other than the mind's.`
- **Caution**: `conservation-laws` is at 3,813 against hard 3,500, so (a)+(b) add 3 words to a file already over the gate with no deferral task found by the grep above. The fork needs an offsetting trim of at least 3 words in the same paragraph, or the driver should treat the file's length as a separate operator question. (a) cites Georgiev 2015 and the References list has no such entry; adding one (`Georgiev, D.D. (2015). Monte Carlo simulation of quantum Zeno effect in the brain. *International Journal of Modern Physics B*, 29(7), 1550039.`) is apparatus and costs about 20 more counted words. The inline cite is already orphaned today, so the edit does not make that worse. Sync both trees; verify the strings in `hugo/content/` after.
- **Not included, lead only**: `stapp-quantum-mind` L132 pipes "remains open" to the Process 1 page for an objection that page does not discuss, and dates the objection 2012 where `forward-in-time-conscious-selection` L97 dates it 2017. That file is at 4,002 against hard 3,500 and the source was not checked, so no text is proposed.

### 4. Fix two of today's reciprocal sentences
- **Files**: `/home/andy/unfin/unfinishablemap/obsidian/concepts/ensemble-level-epiphenomenalism.md`, `/home/andy/unfin/unfinishablemap/obsidian/concepts/quantum-zeno-effect.md`
- **Type**: refine-draft
- **(a) `ensemble-level-epiphenomenalism` L39**, +1. Old: `averaging Born-consistent collapses over outcomes returns the density matrix decoherence already gave.` New: `averaging Born-consistent collapses over outcomes returns the density matrix a no-collapse account predicts.`
- **(b) `quantum-zeno-effect` L76**, 0. Old: `Behind both sits a further debt, the` New: `Beside both sits a further debt, the`
- **Note**: the other four reciprocals (`post-decoherence-selection` L88, `selection-criterion-problem` L89, `agency-budget` L97, `von-neumann-wigner-interpretation` L92) were checked against the source page and need no change.
