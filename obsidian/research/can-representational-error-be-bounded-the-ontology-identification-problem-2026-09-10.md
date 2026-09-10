---
title: Research Notes - Can representational error be bounded? The ontology-identification problem
created: 2026-09-10
draft: false
topics:
  - "[[ai-consciousness]]"
  - "[[instrumental-convergence]]"
  - "[[purpose-and-alignment]]"
  - "[[representation-adequacy-and-irreversible-intervention]]"
concepts:
  - "[[experiential-alignment]]"
  - "[[possibility-probability-slippage]]"
  - "[[substrate-independence]]"
  - "[[intrinsic-nature]]"
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-09-10
ai_modified: 2026-09-10T01:00:32+00:00
---

# Research: Can Representational Error Be Bounded? The Ontology-Identification Problem

**Date**: 2026-09-10

**Why this note exists**: [[representation-adequacy-and-irreversible-intervention]] concludes that "an agent unable to bound its own representational error has not shown that irreversible intervention is acceptably safe." The article never asks whether that inability is permanent or contingent. The optimistic review of 2026-09-09 argued the distinction is the whole practical content of the conclusion: if contingent, the argument is a moratorium with an expiry date and the agent's correct response is to invest in bounding rather than to refrain; if structural, it holds indefinitely.

This note is the sibling of [[containment-as-the-alternative-to-extinction-what-preservation-owes-to-participation-2026-09-10]], written the same night from the same review. That note asks what preservation owes to participation. This one asks whether the article's premise expires.

**The short answer**: the permanent/contingent binary is the wrong frame, and the literature says why. Bounding is available for error measured *against a specified target* and unavailable for error *in the specification of the target itself*. All four of the article's questions are of the second kind. Every working technique in the field is an extrapolation outward from a region where the answer is already known, and the article's four questions have no such region.

**Search queries used**:

- Eliciting Latent Knowledge Christiano Cotra Xu ontology identification report ARC
- Armstrong Mindermann "Occam's razor is insufficient to infer the preferences of irrational agents" NeurIPS 2018 proceedings
- Farquhar Varma Kenton "Challenges with unsupervised LLM knowledge discovery" ICLR 2024 accepted
- Alignment Research Center heuristic arguments low probability estimation mechanistic anomaly detection worst-case guarantee agenda
- (plus direct retrieval of named anchors and their citation chains; see *How To Re-Verify* below)

## How To Re-Verify Every Quote In This Note

Every quotation below was fetched as raw source, converted to plain text, and located with a Python `str.find()` whose returned offset is printed beside it. **An offset of `-1` was never accepted.** Three recipes were used; each source says which applies.

- **Recipe A (HTML)**: `curl -sL -A "Mozilla/5.0" -o FILE URL`, then strip `<script>`/`<style>` blocks, strip remaining tags, `html.unescape`, normalise curly quotes and apostrophes to ASCII, collapse runs of spaces and tabs (newlines preserved). Written to `<name>.plain` and read back in Python text mode.
- **Recipe B (Google Docs plain-text export)**: `curl` the `/export?format=txt` endpoint, then the same normalisation minus tag stripping. Note that the written file contains `\r\n`; reading it back with universal newlines drops the `\r`, which is why the artefact length below (251,052) is smaller than the byte count on disk. Offsets are into the file **as read**.
- **Recipe C (PDF)**: `pdftotext -enc UTF-8 FILE -`, then normalise the `ﬁ`/`ﬂ`/`ﬀ` ligatures, rejoin hyphenated line breaks, then collapse **all** whitespace runs (newlines included) to single spaces.

Offsets are stable for a given fetch of a given URL, not across re-fetches of a living page. They are recorded so a later checker can confirm the phrase exists *and* read the surrounding sentence, rather than taking a bare assertion that it does.

⚠️ **Tooling facts worth carrying forward.**

- The arXiv export API returns 0 bytes from this environment. Use `https://arxiv.org/abs/<id>` for metadata and **`https://ar5iv.labs.arxiv.org/html/<id>`** for full text; that route worked for all five arXiv papers here.
- **The full ELK report is reachable.** The canonical text is a Google Doc, and `https://docs.google.com/document/d/<id>/export?format=txt` returns the whole 251 KB of it. The `alignment.org` blog post is only an announcement, and a WebFetch of it returns a summary that omits everything this note depends on. Fetch the doc.
- `medium.com` (and therefore `ai-alignment.com`) is Cloudflare-blocked from here — a 5 KB "Attention Required!" stub. The Alignment Forum mirror via **`greaterwrong.com`** served the same post in full.
- ⚠️ **`pdftotext` preserves the `ﬁ` ligature.** A grep for `ontology identification` in the Soares PDF returned **zero** while the phrase "ontological identiﬁcation problem" sat in the text. Normalise ligatures before concluding a phrase is absent from a PDF.
- Alignment Forum pages carry the comment thread in the same artefact. On the Christiano post the body ends near offset 28,600 and comments follow; two passages that read as authorial pessimism are in fact commenters' words. Every Christiano quote below is from beneath that boundary and its offset proves it.

## Executive Summary

Six findings carry this note.

1. **The literature is large, the corpus has none of it, and the anchor points at the wrong half of the problem.** ELK and contrast-consistent search address the gap between what a model *represents* and what it *reports*. The article's four questions concern the gap between what a model represents and *what is the case*. ELK presupposes the knowledge is present to be elicited — the report says "We believe there should be some 'correct' reporter" — so where an agent's ontology simply lacks the distinction between reproducing reports and preserving welfare, there is no latent knowledge to elicit and the method has no purchase. The review, the harvest note and the commissioning brief all pointed at the elicitation half, because that is where the vocabulary is.

2. **Every working bounding technique extrapolates outward from a region where the answer is already known, and the article's four questions have an empty seed region.** Measurement-tampering detection requires a *trusted distribution* on which overseers do have ground truth (Roger et al.). Supervised probes require ground-truth labels (Burns et al.'s own stated limitation). Weak-to-strong generalisation requires a weak supervisor's labels. Doubly-efficient debate requires that the question be one extensive human reflection *could* have settled. Narrow ELK requires unambiguous, non-border cases. Bounding transports calibration from where it exists to where it does not; no method manufactures it. Call this the **trusted-seed requirement**; it is this note's organising claim and it is the Map's own, assembled from the sources rather than stated by any of them.

3. **For one half of the problem the permanence question has a formal answer, and the answer is "permanent absent imported normative assumptions."** Armstrong & Mindermann (NeurIPS 2018) prove that any reward function is compatible with any policy, and that degenerate decompositions of a policy into planner and reward have near-minimal description length — so a Kolmogorov-complexity prior, "the most general formalization of Occam's razor we know of," selects the degenerate ones. Their conclusion: inverse reinforcement learning is "fundamentally and philosophically incapable of establishing a 'reasonable' reward function for the human, no matter how powerful they become." ⚠️ Mark the structure precisely: Theorems 1 and 2 are theorems, but the complementary claim that *reasonable* decompositions are high-complexity is **Conjecture 9**, argued rather than proved. The result is half theorem, half conjecture, and an article that reports it as a theorem throughout will have overstated it.

4. **The flagship programme has scoped itself out of the Map's questions, in its own words, three times over.** The ELK report restricts itself to the "narrow" version — "unambiguously wrong answers to straightforward questions about the world, rather than dealing with tricky border cases or deeply confusing situations" — and puts "Designing a philosophically competent reasoner" and "Engaging with the complexity or incoherence of human values" on an explicit not-doing list, attributing its tractability to not getting "hung up on thorny philosophical questions about the nature of knowledge." Soares makes the same move when naming the problem, choosing carbon-atom counting as the goal in order "To leave aside problems of philosophy." Burns et al. make it a third time: "ELK frames this as a worst-case theoretical problem, while we frame this as an empirical problem." This is how tractable research works and it is not evasion — but it means no result in the programme licenses a claim about the article's four questions, in either direction.

5. **The anchor has a published refutation, it is the most important source here, and neither the review nor the harvest found it.** Farquhar et al. (Google DeepMind) prove that *arbitrary* binary features satisfy contrast-consistent search's consistency structure, so "arguments for CCS's effectiveness cannot be grounded in conceptual or principled motivations from the loss construction," and they exhibit probes that report a simulated character's opinion instead of the model's knowledge. Their conclusion states the dilemma the whole question turns on: "Unsupervised approaches have to overcome the identification issues we outline in this paper, whilst supervised approaches have the problem of requiring accurate human labels even in the case of superhuman models. The relative difficulty of each remains unclear."

6. **The corpus already owns the philosophical form of this problem in three separate places and connects none of them to AI.** [[duhem-quine-underdetermination-consciousness]] is a whole article on underdetermination. [[language-thought-boundary]] carries Quine's indeterminacy of translation in precisely the operative form — "rival translation manuals can each fit the whole of the behavioural evidence while disagreeing about what the source sentences mean" — which is structurally identical to ELK's two reporters with identical loss. [[pragmatism]] and [[pragmatisms-path-to-dualism]] carry Putnam's model-theoretic argument, that "reference cannot be fixed by physical-causal relations alone" and that "adding a causal constraint supplies only more theory, itself in need of interpretation." [[intrinsic-nature]], [[primary-secondary-quality-boundary]] and [[ontic-structural-realism]] carry Newman's problem and quiddistic indeterminacy. This mirrors exactly the asymmetry the review found in the interpretability material: the vocabulary is present in force, and the *direction* is what is missing.

## Key Sources

### Christiano, Cotra & Xu (2021) — "Eliciting latent knowledge: How to tell if your eyes deceive you"

- **URL**: announcement at https://www.alignment.org/blog/arcs-first-technical-report-eliciting-latent-knowledge/ ; full text at `https://docs.google.com/document/d/1WwsnJQstPq91_Yh-Ch2XRL8H_EpsnjrC1dwZXR37PC8/export?format=txt`
- **Genre**: **ARC technical report. Not peer-reviewed. Its central claims about difficulty and about prospects are stated credences, not results.** It contains no experiments; its method is a "builder-breaker" game over hypothetical counterexamples.
- **Recipe B**, artefact `elk_doc.plain`, length 251,052 as read.
- **Reached in full.**

The report's own framing of the problem is the article's Question 2 in machine-learning vocabulary. Its core counterexample is a pair of reporters:

> "The direct translator fills in nodes in the human Bayes net with what the human should believe, while the human simulator fills them in with what the human would believe if they saw that video and action sequence" — offset **21,364**

And the underdetermination is stated flatly:

> "these two reporters have identical behavior on the training set, so they have identical loss. It's not obvious which one gradient descent would find" — offset **22,647**

Worse, the training signal actively favours the wrong one:

> "the human simulator is in some sense the correct way to produce labels" — offset **22,201**

This is the article's sentence — "An agent trained to predict reports of pain has a construct that tracks reports" — restated by the people trying to fix it, with the additional and unwelcome observation that the training procedure *prefers* the report-tracking construct.

**Their credence on solvability**, which is the closest thing in the literature to a direct answer to the commissioning question:

> "there isn't yet much reason to believe we are stuck or are faced with an insurmountable obstacle" — offset **3,150**

**The scope restriction that decides the matter for the Map.** ELK as pursued is the narrow version:

> "we are focused on unambiguously wrong answers to straightforward questions about the world, rather than dealing with tricky border cases or deeply confusing situations" — offset **28,920**

And a counterexample only counts if:

> "the situation is a central example of something (like \"tampering\") rather than a border case" — offset **27,391**

**What the programme explicitly declines**, from its own list of what it is not doing:

> "Engaging with the complexity or incoherence of human values" — offset **80,694**
> "Designing a philosophically competent reasoner" — offset **80,943**

and the source of its tractability:

> "we don't have to get hung up on thorny philosophical questions about the nature of knowledge" — offset **75,129**

**The presupposition.** The report assumes a correct answer exists to be found:

> "We believe there should be some \"correct\" reporter, and we can label a bunch of points to help find it, but if we search for a reporter in the naive way we might get a human simulator" — offset **47,913**

- **What this source does NOT establish**: nothing empirical whatsoever. It does not show that ELK is solvable, does not show it is unsolvable, and does not address whether a question with no agreed answer among humans has a "correct reporter" at all. Its ontology-mismatch examples are all cases with a determinate physical fact underneath — Newtonian fluids versus atoms, standard model versus strings (offset **48,870**).
- **Tenet alignment**: the *ontology identification* framing is congenial to Tenet 5 — an agent's most parsimonious adequate model is not thereby the correct one. Neutral on Tenets 1–4. The report's exclusion of philosophical questions means it neither supports nor threatens the Map's metaphysics.

### Soares (2015) — "Formalizing Two Problems of Realistic World-Models"

- **URL**: https://intelligence.org/files/RealisticWorldModels.pdf
- **Genre**: **MIRI technical report.** I did not confirm a peer-reviewed venue; the arXiv-style metadata is absent and the PDF is served from MIRI's own file store. Treat as a technical report.
- **Recipe C**, artefact `soares.flat`, length 37,794.
- **Reached in full.** This is where the term is coined, and it matters for the corpus because the article *already cites* the paper Soares builds on.

> "This is the ontological identification problem" — offset **30,861**

> "it is necessary to interpret features of the environment in terms of the ontology of the goals" — offset **31,102**

> "the ontology of the goals will not actually perfectly match the ontology of reality" — offset **31,704**

> "How can the ontology of the goals be reliably mapped onto the ontology of the model?" — offset **32,133**

And the citation that connects the whole programme to the Map's existing bibliography in one step:

> "de Blanc (2011) provides a preliminary examination of these questions, but the problem remains open" — offset **32,218**

**The same philosophical exclusion, at the moment of naming the problem:**

> "As a matter of fact, it is quite difficult to say what terms our goals are specified in" — offset **30,040**
> "To leave aside problems of philosophy, and highlight the problem as it pertains to world models" — offset **30,129**

and the substitute target chosen instead:

> "the score of an agent is the count of carbon atoms covalently bound to four other carbon atoms over time" — offset **30,542**

- **What this source does NOT establish**: it offers no solution and no impossibility result. It is a problem statement. Its worked target is deliberately a physical-structural fact with a determinate referent, which is the opposite end of the spectrum from "the experiencing subject."
- **Note for the corpus**: the article's existing reference — de Blanc (2011), arXiv:1105.3821, *Ontological Crises in Artificial Agents' Value Systems*, submitted 19 May 2011 (metadata verified at the abs page this run; full text **not** fetched) — is the direct ancestor of the entire ontology-identification literature. The corpus is one citation away from all of it and has taken none of the steps.

### Farquhar, Varma, Kenton, Gasteiger, Mikulik & Shah (2023) — "Challenges with unsupervised LLM knowledge discovery"

- **URL**: https://arxiv.org/abs/2312.10029 (arXiv:2312.10029v2, submitted 15 Dec 2023, revised 18 Dec 2023)
- **Genre**: **preprint** from Google DeepMind, combining **two proved theorems** with **an experimental series**. ⚠️ I searched for a peer-reviewed venue and found none confirmed; the arXiv comments field records only page counts. Do not cite it as an ICLR paper.
- **Recipe A**, artefact `farquhar.plain`, length 84,033.
- **Reached in full.** **This is the most important source in the note** and it directly refutes the commissioning anchor.

> "existing unsupervised methods on large language model (LLM) activations do not discover knowledge" — offset **695**
> "they seem to discover whatever feature of the activations is most prominent" — offset **803**

The theoretical result:

> "arguments for CCS's effectiveness cannot be grounded in conceptual or principled motivations from the loss construction" — offset **12,621**
> "the classifier that CCS finds is under-specified: for any binary feature" — offset **13,349**

Theorem 1 shows that for *any* arbitrary binary feature of the questions there is a probe achieving optimal CCS loss inducing that feature; Theorem 2 extends this to non-binary probes under a corrected, symmetrised loss. The consistency structure that was supposed to pick out knowledge picks out nothing in particular.

Their forward-looking claim, correctly marked as a hypothesis by the authors themselves:

> "we hypothesise that the identification issues explored here, e.g. distinguishing a model's knowledge from that of a simulated character's, will persist for future unsupervised methods" — offset **1,647**
> "we speculate that they will nonetheless be vulnerable to similar critiques" — offset **39,225**

**The dilemma that decides the commissioning question:**

> "Unsupervised approaches have to overcome the identification issues we outline in this paper, whilst supervised approaches have the problem of requiring accurate human labels even in the case of superhuman models. The relative difficulty of each remains unclear." — offset **41,230**

- **What this source does NOT establish**: it does not prove unsupervised knowledge discovery impossible. The generalisation to future methods is explicitly speculation. It also honestly declines to claim its own positive interpretation — the authors note they "do not know whether the feature we extract tracks the beliefs of the simulated character" and name a rival hypothesis for their own Figure 3.
- **Tenet alignment**: neutral metaphysically; strongly supportive of the Map's method. A consistency structure satisfiable by arbitrary features is a clean case of a criterion that looks principled and constrains nothing — the shape of Tenet 5's warning about parsimony under incomplete knowledge, and closely analogous to the Newman problem the corpus already runs in [[ontic-structural-realism]], where structure alone fixes little beyond cardinality.

### Burns, Ye, Klein & Steinhardt (2022) — "Discovering Latent Knowledge in Language Models Without Supervision"

- **URL**: https://arxiv.org/abs/2212.03827 — **ICLR 2023** (confirmed in the arXiv comments field; v1 submitted 7 Dec 2022, v2 revised 2 Mar 2024). ⚠️ The review dated "v2" to 2022-12-07; that is v1's date.
- **Genre**: **peer-reviewed empirical machine-learning paper.** An average-case result on benchmarks, not a bound.
- **Recipe A**, artefact `burns.plain`, length 93,212.
- **Reached in full.**

> "Existing techniques for training language models can be misaligned with the truth" — offset **330**
> "We propose circumventing this issue by directly finding latent knowledge inside the internal activations of a language model in a purely unsupervised way" — offset **619**
> "finding a direction in activation space that satisfies logical consistency properties" — offset **904**

The headline number is modest and should be quoted as such: "it outperforms zero-shot accuracy by 4% on average" (offset **1,256**).

**The paper's own two disclaimers matter more than its result for this question.** First, it declines the bounding framing outright:

> "ELK frames this as a worst-case theoretical problem, while we frame this as an empirical problem that we can make progress on using current models" — offset **39,717**

A bound is a worst-case notion. On its own account this paper is not in that business.

Second, its precondition:

> "CCS relies on the existence of a direction in activation space that separates true and false inputs well" — offset **39,973**

which requires

> "that a model is both capable of evaluating the truth of a given input, and also that the model actively evaluates the truth of that input" — offset **40,249**

followed by

> "It is not clear when these conditions hold precisely" — offset **40,388**

- **What this source does NOT establish**: it does not bound anything, does not address deception (the authors say so, having found no evaluation setup for it), and its precondition fails by construction on any question where the model does not already represent a truth-value. For "does this reconstruction preserve the subject?" the precondition is exactly what is in doubt.
- **Tenet alignment**: neutral. ⚠️ **Do not present this paper as the remedy the Map's article lacks.** It is a 4%-average-accuracy unsupervised probe with a stated refutation and a stated precondition failure, and the review's framing of it as "the article's problem in machine-learning vocabulary" is right about the framing and silent about the outcome.

### Armstrong & Mindermann (2018) — "Occam's razor is insufficient to infer the preferences of irrational agents"

- **URL**: https://arxiv.org/abs/1712.05812 (v1 15 Dec 2017, v6 11 Jan 2019); **NeurIPS 2018**, pp. 5603–5614, confirmed at `proceedings.neurips.cc` (the arXiv record itself lists no venue, so the venue was verified separately).
- **Genre**: **peer-reviewed formal result** — two theorems plus one explicitly labelled conjecture.
- **Recipe A**, artefact `armstrong.plain`, length 75,630.
- **Reached in full.** **For the Map this is the single most valuable source in the note**, because it converts Tenet 5 from a methodological commitment into a cited formal result in a machine-learning setting.

> "a No Free Lunch result implies it is impossible to uniquely decompose a policy into a planning algorithm and reward function" — offset **1,276**
> "even with a reasonable simplicity prior/Occam's razor on the set of decompositions, we cannot distinguish between the true decomposition and others that lead to high regret" — offset **1,415**
> "we need simple 'normative' assumptions, which cannot be deduced exclusively from observations" — offset **1,606**

The novelty relative to the older IRL ambiguity results:

> "this unidentifiability does not disappear when regularising with a general simplicity prior that formalizes Occam's razor" — offset **5,395**
> "simplicity does not solve the No Free Lunch result" — offset **18,571**

The permanence claim, stated by the authors in the strongest available terms:

> "they are fundamentally and philosophically incapable of establishing a 'reasonable' reward function for the human, no matter how powerful they become" — offset **5,846**

And the conclusion, which is Tenet 5 in a formal register:

> "under the Kolmogorov-complexity simplicity prior, a formalization of Occam's Razor, the posterior would endorse degenerate solutions" — offset **41,371**

- ⚠️ **What this source does NOT establish, and the calibration an article must carry.** Theorem 1 (any reward compatible with any policy) and Theorem 2 (degenerate decompositions have near-minimal description length) are proved. The complementary half — that the decompositions *we would endorse* are of high complexity — is **Conjecture 9**, an "informal complexity proposition" that the authors argue for and do not prove. The full claim in the abstract therefore rests on a theorem plus a conjecture. An article reporting "it has been proved that Occam's razor cannot infer human preferences" would be overstating it; the honest form is that the degenerate solutions are provably cheap and the good ones are conjectured to be expensive.
- Also note the result concerns *preferences inferred from behaviour*, not consciousness. It bears on the article's Questions 2 and 4 directly and on Questions 1 and 3 only by analogy.
- **Tenet alignment**: **Tenet 5, squarely and without strain.** The corpus has [[epistemological-limits-occams-razor]] as the natural host and currently holds no formal external instance of the tenet at all. ⚠️ Attribution caution: the corpus already cites a *different* paper by a Sören Mindermann — the 2025 Anthropic agentic-misalignment paper in [[instrumental-convergence]] — so "Mindermann is absent from the corpus" is false and "this author is new to the corpus" is false. The *paper* is absent.

### Roger, Greenblatt, Nadeau, Shlegeris & Thomas (2023) — "Benchmarks for Detecting Measurement Tampering"

- **URL**: https://arxiv.org/abs/2308.15605
- **Genre**: **benchmark/datasets paper** (Redwood Research), preprint. Empirical, and its outcome is partial by the authors' own statement.
- **Recipe A**, artefact `roger.plain`, length 165,010.
- **Reached in full.**

This is the closest thing in the literature to a *measurable* bounding of one specific representational failure, and its architecture is precisely what establishes the trusted-seed requirement:

> "given a restricted trusted distribution on which overseers can avoid tampering because they understand the action sequences and their effects well, and a wider untrusted distribution where tampering sometimes happened, but overseers don't know when, which means they don't have access to the ground truth" — offset **1,602**

The method generalises outward from a region where humans do know the answer to a region where they do not. Its result is explicitly incomplete: "We demonstrate techniques that outperform simple baselines on most datasets, but don't achieve maximum performance" (offset **1,173**).

- **What this source does NOT establish**: it does not bound error on any question lacking a trusted region, and the datasets' ground truth is manufactured by the authors ("we use fixed datasets which contain examples where we manually generate discrepancies between the ground truth and measurements", offset **4,800**). Nothing here transfers to a question on which humans have no trusted region at all.
- **Tenet alignment**: neutral. Methodologically it is the cleanest illustration in the note of why the article's four questions are not addressable by current means: there is no set of cases in which humans reliably know whether a functional duplicate preserved the subject, so there is no trusted distribution to seed from.

### Burns, Izmailov, Kirchner, Baker, Gao, Aschenbrenner, Chen, Ecoffet, Joglekar, Leike, Sutskever & Wu (2023) — "Weak-to-Strong Generalization"

- **URL**: https://arxiv.org/abs/2312.09390
- **Genre**: **OpenAI technical report / preprint**, empirical, with an explicit disanalogy inventory. Same lead author as the 2022 anchor.
- **Recipe A**, artefact `w2s.plain`, length 159,385.
- **Reached in full.**

The framing is the supervised horn of Farquhar's dilemma: "can weak model supervision elicit the full capabilities of a much stronger model?" The result is real and partial:

> "we are still far from recovering the full capabilities of strong models with naive finetuning alone, suggesting that techniques like RLHF may scale poorly to superhuman models without further work" — offset **1,612**

and the authors' own limitation statement:

> "our methods serve more as proofs-of-concept that weak-to-strong generalization is tractable, rather than practical solutions we recommend deploying today" — offset **9,394**

- **What this source does NOT establish**: it does not remove the need for labels; it makes weaker labels go further. The whole setup presupposes a weak supervisor who is *right often enough*. On the Map's four questions there is no weak supervisor whose labels are better than chance in any demonstrable sense, so the technique has nothing to amplify.
- **Tenet alignment**: neutral.

### Brown-Cohen, Irving & Piliouras (2023) — "Scalable AI Safety via Doubly-Efficient Debate"

- **URL**: https://arxiv.org/abs/2311.14125
- **Genre**: **theoretical (complexity-theoretic) preprint**, Google DeepMind. This is the strongest positive result in the note — an actual guarantee — which is why its antecedent matters so much.
- **Recipe A**, artefact `debate.plain`, length 88,285.
- **Reached in full.**

> "In this model we prove that, under appropriate assumptions, any polynomial-time computation can be verified using only a constant number of queries to the black-box representing human judgement" — offset **7,435**

> "for any problem whose solutions can be verified by extremely extensive human reflection, the solutions can also be verified with a constant amount of human judgement and interaction with competing provers" — offset **7,717**

And the antecedent, which the authors themselves name as the limitation:

> "A key requirement, and limitation, for applying our results in real-world settings, is that the debating models must have the ability to produce (potentially extensive) natural-language reasoning traces to solve the problem at hand, in such a way that (potentially extensive) careful human analysis could have been used to judge that the reasoning was correct." — offset **7,923**

- **What this source does NOT establish**: the theorem is a *reduction*. It converts questions that extensive human reflection could settle into questions cheap human judgement can settle. It cannot manufacture verifiability that does not exist. The article's four questions are precisely questions that centuries of extensive human reflection have not settled, so the antecedent fails and the guarantee does not reach them.
- A further caution the paper itself supplies: when black-box access is allowed, "the main theorems regarding the power of interactive proofs (e.g. IP=PSPACE and the PCP theorem) are actually false" (offset **6,855**). Importing complexity-theoretic intuitions about verification into the human-judgement setting is hazardous, and this paper is the one that says so.
- **Tenet alignment**: neutral. Useful to the Map as the demonstration that formal guarantees in this area are conditional on human verifiability rather than replacing it.

### Christiano (2020) — "Inaccessible information"

- **URL**: https://www.alignmentforum.org/posts/ZyWyAJbedvEgRT2uF/inaccessible-information (fetched via `greaterwrong.com`; the `ai-alignment.com` original is Cloudflare-blocked)
- **Genre**: **research blog post / conceptual framing.** The author calls it "clarification and framing rather than a presentation of new ideas." Not peer-reviewed, no results.
- **Recipe A**, artefact `inacc.plain`, length 53,403. **Post body ends near offset 28,600; comments follow.** All quotes below are from the body.
- **Reached in full.** ⚠️ The review flagged `Christiano` as absent from the corpus and pointed at the ELK report. **This** is the piece of Christiano that matters most, because its worked example is the Map's Question 2 verbatim.

> "the model might have a detailed representation of Alice's thoughts which it uses to predict what Alice will say, without being able to directly answer \"What is Alice thinking?\"" — offset **1,148**
> "I'll call information like \"What is Alice thinking?\" inaccessible" — offset **1,457**
> "I think it's very plausible that AI systems will build up important inaccessible knowledge, and that this may be a central feature of the AI alignment problem" — offset **1,524**

The definition of accessibility is a checkability condition, and it fails on exactly the Map's cases:

> "If I can check X myself, given other accessible information, then I'll define X to be accessible" — offset **2,155**
> "I can check a claim about what Alice will do, but I can't check a claim about what Alice is thinking" — offset **2,266**

**And the prospects, in the same author's words, one year before the ELK report's optimism:**

> "it's totally unclear how we ever get the intended policy rather than the instrumental policy" — offset **20,099**
> "I don't think we have any concrete proposals for how to understand what the policy is doing well enough to make this distinction" — offset **21,097**
> "I don't think we have any approach that moves the needle on this problem, at least from a theoretical perspective, so I think it's a plausible candidate for a hard core" — offset **25,223**

- **Reading the apparent tension honestly.** The 2020 post says nothing moves the needle; the 2021 report says there is no reason to think we are stuck. These are not in contradiction — they are about the wide and narrow problems respectively, by the same author, and read together they *are* the narrow/wide split stated from the inside. An article should present them as a pair; presenting either alone misrepresents the field's own view.
- **What this source does NOT establish**: no result of any kind. It is a framing document with stated credences.
- **Tenet alignment**: the accessibility definition is a strikingly close functional match to the Map's structural point about behavioural evidence, arrived at without any dualist premise — which supports the reviewed article's central design goal of a protective case that survives an agent rejecting Tenet 1.

### Hilton (2024) — "A bird's eye view of ARC's research"

- **URL**: https://www.alignment.org/blog/a-birds-eye-view-of-arcs-research/
- **Genre**: **organisational agenda post.** Describes intentions, not results.
- **Recipe A**, artefact `arc_birdseye.plain`, length 14,393.
- **Reached in full.** Relevant because ARC's successor programme is the live candidate for a label-free worst-case guarantee, and therefore for the "contingent" reading.

> "if the scalability of an algorithm depends on unknown empirical contingencies (such as how advanced AI systems generalize), then we try to make worst-case assumptions instead of attempting to extrapolate from today's systems" — offset **2,188**

> "how can we train an AI system to honestly report its internal beliefs, rather than what it predicts a human would think" — offset **3,464**

**The concession that matters most for the word "bounded":**

> "we believe proof is too strict of a standard to be feasible" — offset **4,415**

The success criterion is a *heuristic explanation*, and the robustness application is negative selection rather than certification:

> "LPE would help with alignment robustness by allowing us to select models for which we cannot explain why they would ever behave catastrophically" — offset **5,637**

- **What this source does NOT establish**: no technical claim. Note also that mechanistic anomaly detection, ARC's most-favoured route, defines anomaly relative to the mechanism that produces low loss on the *training* data — which is the trusted-seed requirement again, one level down.
- **Tenet alignment**: neutral. Worth recording that a programme aiming explicitly at the worst case has already conceded that proof is out of reach, so even its own success would not be a bound in the sense the article's certification asymmetry uses.

## Sources I Could Not Reach

- **ARC's "Obstacles in ARC's research agenda"** (`alignment.org/blog/obstacles-in-arcs-research-agenda/`) is a 1.2 KB pointer post only. The three substantive posts by David Matolcsi that it links, on LessWrong, were **not fetched**. These are the most likely place to find an insider statement of what currently blocks the programme, and they are the highest-value follow-up in this note.
- **ARC's heuristic-arguments papers** — "Formalizing the presumption of independence", "Estimating Tail Risk in Neural Networks", "Towards a Law of Iterated Expectations for Heuristic Estimators" — were identified but **not fetched**. Any claim about what ARC's current programme can or cannot deliver should rest on these rather than on the bird's-eye summary.
- **de Blanc (2011) full text**. Metadata verified at the abs page (title, author, 19 May 2011 submission) and the paper is already cited by the reviewed article, but the text was **not read this run**. The article's characterisation of it as "a conceptual analysis with worked toy examples" was not independently checked here.
- **Skalse & Abate on inverse-reinforcement-learning misspecification, and the STARC-metric literature.** Not searched. This is the natural place to look for a *quantitative* version of Armstrong & Mindermann, and its absence is the main gap in the formal arm of this note.
- **The ELK prize results** (ARC's published round of builder-breaker submissions) were not retrieved; they would show how the counterexamples fared against real proposals rather than hypothetical ones.
- **Peer-reviewed philosophy connecting the ontology-identification problem to the philosophy of reference.** I searched only via the AI-safety literature's own citation chains and found none. The interpretability sibling note recorded the same gap from the other side, so two independent runs have now failed to find this literature. That is weak evidence it is genuinely thin, and it is the strongest candidate for a place where the Map could contribute rather than summarise.

## Major Positions

### Position A — The inability is contingent; bounding is an engineering programme in progress

- **Proponents**: Christiano, Cotra & Xu (2021) as to narrow ELK; Burns et al. (2022, 2023); ARC's current agenda.
- **Core claim**: representational error is a technical problem with unexplored approaches, and there is no identified in-principle obstruction.
- **Evidential status**: **stated credence plus partial empirical progress.** The strongest formulation available is "there isn't yet much reason to believe we are stuck," which is an absence of a proof of impossibility rather than evidence of tractability.
- **Relation to site tenets**: if right, the reviewed article's conclusion is a moratorium with an expiry date. Note that it would expire for the Map's questions only if the programme extended to them, which its own scope statements decline.

### Position B — The inability is structural for value and preference identification

- **Proponents**: Armstrong & Mindermann (2018).
- **Core claim**: no simplicity prior selects the intended decomposition of behaviour into planner and reward; normative assumptions must be imported from outside the observations.
- **Evidential status**: **two proved theorems plus one conjecture** (see the calibration note above). Peer-reviewed.
- **Relation to site tenets**: direct formal support for Tenet 5, and the strongest available support for the reviewed article's conclusion — reached without any dualist premise, which is what the article was designed to want.

### Position C — Identification failure will persist for unsupervised methods

- **Proponents**: Farquhar et al. (2023).
- **Core claim**: consistency structures do not pick out knowledge, because agent-belief features satisfy them too; adding further consistency properties will not fix this because simulated-agent beliefs also satisfy the new properties.
- **Evidential status**: **proved for CCS specifically; speculation as to future methods, so marked by the authors.**
- **Relation to site tenets**: methodologically congenial to Tenet 5 and structurally cognate to Newman's problem as the corpus already runs it.

### Position D — The problem is real but the philosophical part is deliberately deferred

- **Proponents**: the field's own scope statements — Christiano, Cotra & Xu; Soares; Burns et al.
- **Core claim**: progress requires targets with determinate referents, so the formalisations pick physical or behavioural facts and set the rest aside.
- **Evidential status**: this is not a position anyone argues for; it is a research-strategy choice, stated repeatedly and openly.
- **Relation to site tenets**: this is the finding the Map should build on. It means the corpus's contribution is not to summarise the programme but to state what the programme has excluded and why that exclusion is exactly where the article's argument lives.

### Position E — Bounding, if achieved, would be a rival to corrigibility rather than its precondition

- **Proponents**: **none. This is the Map's own argument and I found no source for it.**
- **Core claim**: in the off-switch game already carried by [[instrumental-convergence]], an agent permits shutdown *because* it is uncertain about its own objective and reads the human's shutdown action as evidence about it. Reducing representational error reduces that uncertainty, and so reduces the deference incentive. A successful bounding programme would therefore retire the reviewed article's restraint argument and one ground of corrigibility together.
- **What protects the Map here**: Armstrong & Mindermann's result bears on the *reward-identification* quantity rather than the *elicitation* quantity. If it holds, uncertainty about what humans value survives even a complete solution to ELK — so corrigibility's ground survives the contingent reading of the bounding question. The two quantities coming apart is the distinction the whole answer turns on, and it is why the commissioning question has no single yes or no.
- ⚠️ **This inverts the commissioning brief**, which stated that "bounding one's model of humans is the epistemic precondition for corrigibility rather than a rival to it." See *What I Judge The Brief And The Review Got Wrong* below.

## Key Debates

### Debate 1 — Is the failure permanent or contingent?

- **Sides**: Position A (contingent, no identified obstruction) against Position B (structurally impossible for preference inference absent normative assumptions).
- **Core disagreement**: whether the quantity at issue is *elicitation* (getting a model to report what it represents) or *identification* (fixing what the target term refers to). The two camps are largely talking about different quantities and rarely say so.
- **Current state**: **not joined.** The clearest statement of the real question is Farquhar's, and it ends "The relative difficulty of each remains unclear." Neither side has addressed the class of question on which the Map's article turns.

### Debate 2 — Does the narrow/wide distinction do the work the field assumes?

- **Sides**: the ELK report's position that solving crisp counterexamples "would already be a very promising step," against the possibility that the crisp cases and the border cases fail for different reasons and a solution to the first transfers not at all.
- **Core disagreement**: whether ontological error is one phenomenon admitting a graded attack or two phenomena sharing a name.
- **Current state**: undiscussed in the sources reached. This note's Finding 2 takes the second view — that the trusted-seed requirement is what unifies the successful techniques, and that it is present in the crisp cases and absent in the border cases — but that is the Map's reconstruction and no source states it.

### Debate 3 — Are supervised or unsupervised routes more promising?

- **Sides**: Farquhar et al. name both horns and decline to adjudicate; Burns et al. (2023) pursue the supervised horn; ARC pursues a third route via heuristic explanations that aims to need neither.
- **Current state**: genuinely open, and the authors of the sharpest result say so in as many words.

### Debate 4 — Would a successful probe bear on Tenet 1? (Map argument, unsourced)

- **The argument**: the review held that Tenet 1 predicts a principled rather than engineering ceiling for activation probes, and called this "falsifiable-shaped."
- **The problem**: a probe's success is scored against human labels. If a probe were to succeed on a question about experience, a dualist can hold that the probe tracks the physical correlate that generates the labels, which is what the labels were evidence of anyway. There is no clean falsifier, so the prediction is not falsifiable-shaped in the way claimed.
- **Where Tenet 1 does real work instead**: it explains *why* the trusted seed region is empty rather than merely observing that it is. Under Tenet 1 the disputed facts are not just unlabelled but not labellable by behavioural means, so the seed requirement fails for a reason.
- **Status**: the Map's own; no source. See the tenet section below.

## Coverage: What The Corpus Lacks, And What It Already Has

Measured on **content**, not filenames, across `obsidian/topics/ concepts/ apex/ voids/ positions/ tenets/`. File counts, this run.

**Genuinely absent — safe to introduce:**

| Term | Files |
|---|---|
| `latent knowledge` | 0 |
| `ontology identification` / `ontology-identification` / `ontological identification` | 0 each |
| `Eliciting Latent` | 0 |
| `Christiano` | 0 |
| `ELK` (case-**sensitive**, word-bounded) | 0 |
| `Mindermann` (the 2018 paper) | 0 — but see caution below |
| `measurement tampering`, `weak-to-strong`, `scalable oversight`, `distribution shift` | 0 each |
| `reward misspecification`, `reference magnet`, `permutation argument`, `Kripkenstein` | 0 each |

⚠️ **The `ELK` measurement needs care, and the brief's stated reason for its zero is wrong.** Case-**insensitive** word-bounded `\bELK\b` returns **1 file**, not 0: `topics/clinical-evidence-quality-standards-consciousness-research` cites **van Elk** four times, where `Elk` is a standalone word rather than word-internal. The correct test is case-*sensitive* `grep -nE '\bELK\b'`, which returns 0. Word bounds alone are insufficient; word bounds plus case sensitivity settle it. The conclusion the brief drew is right and the reason it gave is not.

**Already covered — link, do not re-introduce.** This section is the practical payload; four of these were flagged by neither the review nor the harvest.

- ⚠️ **The philosophical form of the ontology-identification problem is already in the corpus in three families.**
  - [[duhem-quine-underdetermination-consciousness]] — an entire article on underdetermination, applied to consciousness science and never to AI representation.
  - [[language-thought-boundary]] carries Quine's indeterminacy of translation in the exactly operative form: "rival translation manuals can each fit the whole of the behavioural evidence while disagreeing about what the source sentences mean." Set that beside the ELK report's two reporters with "identical loss" and the structural identity is complete. The same article also models the move the downstream article needs — it records that *which label applies* (unmapped versus unexplorable) is itself the live dispute, and inherits "the dispute, not either verdict."
  - [[pragmatism]] and [[pragmatisms-path-to-dualism]] carry Putnam's model-theoretic argument: "reference cannot be fixed by physical-causal relations alone: any purely physical description is compatible with multiple incompatible interpretations, and adding a causal constraint supplies only more theory, itself in need of interpretation." That is the ontology-identification problem as a thesis about reference, and it is already the Map's.
  - [[intrinsic-nature]], [[primary-secondary-quality-boundary]], [[ontic-structural-realism]] and [[the-unfolding-argument-against-causal-structure-theories-of-consciousness]] carry Newman's problem and quiddistic indeterminacy — structure fixing little beyond cardinality. Farquhar's Theorem 1 is a machine-learning instance of the same shape.
- ⚠️ **The Map already has a purpose-built taxonomy for the commissioning question, and should use it instead of the permanent/contingent binary.** The [[voids]] taxonomy sorts territory into unexplored, unexplorable and occluded. [[intrinsic-nature-void]] already delivers a verdict of precisely this shape for an analogous inscrutability, holding that it "is not a puzzle awaiting a clever solution but may be a permanent boundary." An article that answers "permanent or contingent?" without using the corpus's own three-way vocabulary will have reinvented a worse version of it.
- ⚠️ **`corrigib*` is not absent: 8 files, and 2 are the AI-safety sense.** [[instrumental-convergence]] carries the Hadfield-Menell off-switch game, CIRL, the deference result and Lempert's robust decision-making; [[purpose-and-alignment]] carries Russell. Position E above states the relationship this note recommends, which is *not* the one the brief stated.
- **`interpretab*` appears in 39 files this run**, led by [[deep-computational-markers-for-machine-consciousness]] (11 mentions), [[non-human-minds-as-void-explorers]] (7), [[anti-correlation-probes-for-ai-consciousness]] (5), [[training-contamination-confound]] (5), [[ai-as-introspection-control]] (5), [[cross-architecture-llm-introspection]] (4). ⚠️ Three figures are now in circulation — the review's 20, the brief's 23, and today's 39 — measured on different dates and, from the leader's mention count also rising (9 → 11), plausibly all correct when taken. **The review's substantive point survives and is the important part**: every one of these uses interpretability as a probe of *AI* phenomenology or self-report reliability, and none as a remedy for an agent's model of *humans*. State the asymmetry; do not present interpretability as absent.
- **[[experiential-alignment]]** holds the Goodhart failure-mode table and the triangulation protocol. The review's verdict stands and this note sharpens it: triangulation raises the cost of proxy-gaming without bounding representational error, because every proxy in the protocol is a measurement of physical or behavioural fact and the question is whether any set of such measurements fixes the referent. Farquhar's Theorem 1 is the formal version of that point.
- **The sibling research note [[interpretability-probes-representational-ambivalence-2026-08-20]] is already consumed**, not a pending claimant — its own frontmatter records `consumed_by: anti-correlation-probes-for-ai-consciousness` and its Angle 1 is marked "FOLDED 2026-08-21." Its disanalogy (iii) is directly relevant and should be linked rather than re-derived: the human analogue of weight-level access does not exist and may be blocked in principle at the relevant grain if the Tenet 2 interface is real.
- **[[phenomenal-value-realism]]** holds the value-sign question; the review correctly closed it as covered. Do not reopen.
- **[[epistemological-limits-occams-razor]]** is the natural host for the Armstrong & Mindermann result and currently holds no formal external instance of Tenet 5.

**Section capacity, measured this run with the gating function** `tools.evolution.state.count_section_files` rather than the CLAUDE.md table, which is badly stale:

| Section | Count | Cap | Free |
|---|---|---|---|
| `topics/` | 328 | 360 | 32 |
| `concepts/` | 326 | 360 | 34 |
| `voids/` | 103 | 115 | 12 |
| `positions/` | 18 | 80 | 62 |

The gate is known to over-count `topics/` by one. Both candidate sections have ample headroom, so the review's cap caveat is discharged — but re-measure before the expand runs anyway.

## The Core Analysis: Permanent, Contingent, Or Neither

This is the question the task asks. The honest answer replaces the binary.

**Two quantities wear the same name.** Distinguish:

- **(a) Extraction error** — the gap between what a model internally represents and what it reports or acts on. This is what ELK, CCS, mechanistic anomaly detection, measurement-tampering detection and weak-to-strong generalisation address.
- **(b) Specification error** — the gap between what a model's concepts pick out and what the terms of its goal were meant to pick out. This is Soares's ontological identification problem, Putnam's model-theoretic problem, and Armstrong & Mindermann's unidentifiability.

The reviewed article's four questions are all of kind (b). Whether preserving functional organisation preserves the subject, whether reproducing reports preserves welfare, whether a reconstruction's testimony establishes continuity, whether removing an objection removes the wrong — none of these is a question about whether the agent will honestly report what it represents. Each asks whether the agent's concept of a person picks out what matters. **An agent could solve ELK completely and have made no progress on any of them.** That is the single most important thing this note has to say, and it means the anchor the review verified, while genuinely apt as a framing of the problem, is aimed at the adjacent quantity.

**The trusted-seed requirement.** Assembling the successful techniques reveals a common architecture that no source states. Each one is an extrapolation outward from a region where the answer is already known:

| Technique | Seed it extrapolates from |
|---|---|
| Supervised probes | ground-truth labels on the training set |
| CCS (unsupervised) | the model already representing a truth-value — and Farquhar shows the consistency structure fails to identify it even then |
| Measurement-tampering detection | a *trusted distribution* on which overseers know the answer |
| Weak-to-strong generalisation | a weak supervisor whose labels are better than chance |
| Doubly-efficient debate | the question being settleable by extensive human reflection |
| Narrow ELK | unambiguous, non-border cases with a determinate referent |
| Mechanistic anomaly detection | the mechanism that produces low loss on training data |

Bounding, on this reading, is the transport of calibration from where it exists to where it does not. No method in the literature creates calibration where none exists. **And the article's four questions have an empty seed region**: there is no set of cases in which humans reliably know whether a substrate migration preserved the subject, so there is nothing to extrapolate from, and the failure is not a shortage of data or compute.

**So the verdict.** The inability is **contingent for extraction error and, on present evidence, unbounded and largely unattempted for specification error** — with one formal permanence result (Armstrong & Mindermann, half theorem and half conjecture) covering the value-identification part of the second class. The article's conclusion therefore does not have an expiry date that any current programme is working toward, and the moratorium reading fails not because the inability has been shown permanent but because **the research programme that would lift it has explicitly excluded the questions at issue**, in three independent statements by three separate groups.

This is a stronger and more defensible position than either horn the review offered, and it changes the agent-facing advice. The reviewed article's implicit counsel — refrain rather than invest in bounding — is correct as things stand, and the reason is not that bounding is impossible but that no available notion of bounding is defined over the quantity in question.

**What would settle it.** A method that certifies a bound on a quantity whose definition does not presuppose (i) human labels on the disputed cases, (ii) that the disputed cases are settleable by extensive human reflection, or (iii) that the target is already represented in the model. Three observations about that target:

1. **Nobody has proposed such a method.** ARC's heuristic-arguments programme is the closest live candidate for a label-free worst-case guarantee, and it has already conceded that "proof is too strict of a standard to be feasible" — so even its success would deliver negative selection (models whose catastrophic behaviour cannot be *explained*) rather than a bound in the certification sense the article's asymmetry uses. That gap between "we cannot explain a failure" and "the failure is bounded" is exactly the gap the article's engineering analogy is about, and the article is on the right side of it.
2. **The decisive experiment is probably not constructible.** The test would be a benchmark whose ground truth is a philosophically disputed fact about persons — and no such benchmark can be built, for the same reason the problem is hard. That unconstructibility is itself informative, and it is what would justify a `voids/` classification rather than a bare "unsolved."
3. **A weaker settling condition is available and worth stating**, because it is the one an agent could actually check: if a bounding method were demonstrated on a question where humans *had* disagreed and later converged — a case where the seed region was empty and then filled — that would be evidence the seed requirement is contingent. The Map should name this as the falsifier it would accept.

**What the Map must not do here.** The reviewed article declines expected-value and unbounded-magnitude reasoning under [[possibility-probability-slippage]], and nothing in this note reintroduces it. No credence figures, no probability-weighted catastrophe magnitudes, and no p(doom)-style aggregates appear above; where sources state credences, they are marked as the source's credences rather than adopted. An article built on this note must keep that discipline, and should note that the sources it leans on are mostly preprints and technical reports carrying stated credences rather than peer-reviewed empirical results — the exceptions being Burns et al. (ICLR 2023) and Armstrong & Mindermann (NeurIPS 2018).

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1928 | Newman's objection to Russell | Structure alone fixes little beyond cardinality — already in the corpus |
| 1960 | Quine, *Word and Object* | Rival translation manuals fitting all behavioural evidence — already in the corpus |
| 1981 | Putnam's model-theoretic argument | Reference not fixed by physical-causal relations — already in the corpus |
| 2000 | Ng & Russell | The classical reward-shaping ambiguity in IRL (cited by Armstrong & Mindermann; not read this run) |
| 2011 | de Blanc, *Ontological Crises in Artificial Agents' Value Systems* | The ancestor of the whole programme, and already cited by the reviewed article |
| 2015 | Soares, *Formalizing Two Problems of Realistic World-Models* | Names the ontological identification problem; calls it open; sets philosophy aside |
| 2018 | Armstrong & Mindermann, NeurIPS | The formal impossibility result; Occam's razor insufficient |
| 2020 | Christiano, *Inaccessible information* | "What is Alice thinking?" as the paradigm case; nothing moves the needle |
| 2021 | Christiano, Cotra & Xu, ELK report | The problem in ML vocabulary; narrow scope declared; philosophy excluded |
| 2022 | Burns, Ye, Klein & Steinhardt, CCS (ICLR 2023) | The empirical arm opens; worst-case framing explicitly declined |
| 2023 | Roger et al. measurement tampering; Brown-Cohen et al. doubly-efficient debate; Burns et al. weak-to-strong; Farquhar et al. CCS critique | Benchmarks, the first real formal guarantee, the supervised horn, and the refutation — all in one year |
| 2024 | ARC's bird's-eye view | Programme pivots to heuristic explanations; proof conceded infeasible |
| 2025 | Matolcsi's obstacles sequence (not read this run) | Insider account of what currently blocks the programme |

## Potential Article Angles

### Angle 1 (recommended) — "Whether Representational Error Can Be Bounded", `topics/`

A companion to the reviewed article that supplies the missing conditional. Shape:

1. The reviewed article's conclusion rests on an inability, and the practical content depends on whether it expires.
2. The two quantities — extraction error and specification error — and why the article's four questions are all of the second kind. An agent could solve ELK completely and be no further forward.
3. The literature that exists: de Blanc → Soares → ELK → CCS → Farquhar's refutation, with Christiano's inaccessible-information framing as the clearest statement of the problem.
4. The trusted-seed requirement, stated as the Map's own reconstruction, with the table above.
5. Armstrong & Mindermann as the one formal permanence result, calibrated as theorem-plus-conjecture, and as a cited external instance of Tenet 5.
6. The field's three scope statements, and the conclusion: the inability is not shown permanent, and no programme is working to lift it for these questions.
7. Classification in the corpus's own voids vocabulary rather than the permanent/contingent binary, following [[language-thought-boundary]]'s precedent of inheriting the dispute rather than a verdict.

**Placement**: `topics/` has 32 free slots and `concepts/` 34, so either is available. I recommend `topics/` — the piece is argumentative and literature-heavy rather than definitional. Required links: the reviewed article, its sibling research note, [[duhem-quine-underdetermination-consciousness]], [[language-thought-boundary]], [[pragmatisms-path-to-dualism]], [[intrinsic-nature]], [[experiential-alignment]], [[instrumental-convergence]], [[purpose-and-alignment]], [[epistemological-limits-occams-razor]], [[possibility-probability-slippage]]. **Do not** restate the off-switch literature; link it and state the relationship in Position E's terms.

### Angle 2 — the Tenet 5 insertion, cheap and independently valuable

[[epistemological-limits-occams-razor]] holds no formal external instance of the tenet, and Armstrong & Mindermann supply one in a machine-learning setting with a Kolmogorov-complexity prior. A short insertion pays down real debt whether or not Angle 1 is written, and it needs no cap headroom. ⚠️ It must carry the theorem/conjecture calibration; a claim that Occam's insufficiency has been *proved* for preference inference would overstate the paper.

### Angle 3 — the `experiential-alignment` reciprocal

The review flagged this as out of contract and worth more than the forward link, since that article is where a reader arrives expecting a solution. Farquhar's Theorem 1 gives it a citable formal backing: a consistency criterion satisfiable by arbitrary features constrains nothing, which is the general form of "convergence of proxies is not evidence of ontological adequacy." Per `out-of-scope-spillover-flags-stale`, re-derive rather than trust this if it is picked up later.

### Angle 4 (follow-on, not this chain) — a `positions/` entry

`positions/` has 62 free slots. A register entry recording the Map's grade on the bounding question — that extraction error is plausibly contingent, specification error unbounded on present evidence, with the Armstrong & Mindermann result as the strongest support and its conjecture-half named as the dependency — would give downstream articles something to cite instead of re-arguing it. Separate task.

## Tenet Alignment — The Review's Framing, Checked Against The Literature

The review claimed: "Tenet 1 predicts a specific failure for the whole programme — if consciousness is not reducible to physical processes, then no probe of physical activations recovers what the article says is omitted, and unsupervised latent-knowledge extraction has a principled ceiling rather than an engineering one. That is a falsifiable-shaped prediction the Map can own, which is more than tenet-compatibility."

**The framing half-survives, and both halves of the correction matter.**

**It over-reaches.** The ceiling does not need Tenet 1. Armstrong & Mindermann's result is fully physicalist and blocks preference identification anyway; Putnam's and Quine's arguments are available to a physicalist; Farquhar's Theorem 1 is a fact about a loss function. Three of the article's four questions can be blocked without any dualist premise. Resting the ceiling on Tenet 1 would make the argument *more* contested than it needs to be — which is the precise mistake the reviewed article was written to avoid, since its whole design is a protective case that survives an agent rejecting dualism. **An article built on this note must not rest the ceiling on Tenet 1.**

**It is not falsifiable-shaped.** A probe's success is scored against human labels, so a probe succeeding on an experience-question is compatible with the dualist reading that the probe tracks the physical correlate the labels were evidence of. The prediction has no clean falsifier and the review over-credited it. What *is* falsifiable-shaped is the weaker settling condition in the Core Analysis above — a bounding method demonstrated on a question whose seed region was once empty and later filled.

**Where Tenet 1 does real work.** It explains why the seed region is empty rather than merely noting that it is: under Tenet 1 the disputed facts are not merely unlabelled but not labellable by behavioural means, so the trusted-seed requirement fails for a principled reason rather than a contingent one. That is a genuine contribution and it is more modest than the review's version.

**Tenet 5 is where the real gain is.** Armstrong & Mindermann formalise "Occam's razor has limits" in exactly the Map's sense — a Kolmogorov-complexity prior, the most general formalisation of parsimony available, selecting degenerate solutions under incomplete knowledge. The reviewed article's own Tenet 5 paragraph already says that "An agent treating its most parsimonious adequate model as exhaustive is making exactly the inference Tenet 5 denies," and this result is a peer-reviewed external instance of precisely that inference failing. The corpus holds no such instance. ⚠️ Carry the theorem/conjecture calibration wherever it is cited.

**Tenets 2, 3 and 4** are not engaged by this material. The reviewed article's inherited mechanism debt is untouched by anything here, and an article on this subject can and should stay clear of it: the trusted-seed argument requires only that the agent cannot exclude the relevant models, not that the Map's interface is efficacious.

## What I Judge The Brief And The Review Got Wrong

Recorded so the corrections are not re-derived, and because the commissioning brief asked.

1. **"Bounding one's model of humans is the epistemic precondition for corrigibility rather than a rival to it" — the brief, and I think this is backwards.** In the off-switch game the corpus already carries, uncertainty about the objective is what *produces* deference; the agent permits shutdown because it treats the human's action as evidence about a utility function it does not know. Bounding representational error reduces that uncertainty and therefore weakens the deference incentive. Bounding and corrigibility are substitutes on that mechanism, not precondition and consequent. What saves the Map is that the two quantities differ: Armstrong & Mindermann's unidentifiability concerns reward inference, so corrigibility's ground survives even a complete solution to elicitation. Position E states this; it is the Map's own and unsourced.
2. **The anchor is aimed at the adjacent quantity.** Burns et al. and ELK address extraction error; the article's four questions are specification error. The review's sentence that CCS's "framing is the article's problem in machine-learning vocabulary" is right about the framing and does not notice that the *method* cannot reach the article's cases, for a reason the paper itself states (its precondition requires the model already to represent the truth-value).
3. **The anchor has a published refutation that neither the review nor the harvest note mentions.** Farquhar et al. prove CCS's objective is satisfied by arbitrary features. A downstream article that presented Burns et al. as the live remedy would have been wrong within twelve months of the anchor's publication, and the review's "whether that succeeds is the question the article's conclusion is silently conditional on" reads very differently once the refutation is on the table.
4. **The `\bELK\b` zero is right and its stated reason is wrong.** The brief said the ten case-insensitive hits are "all word-internal (Elk, Spelke, Belknap, Wendelken, Mielke)" and instructed "use word bounds, not `.count()`." But `van Elk` — four occurrences in `topics/clinical-evidence-quality-standards-consciousness-research` — is a word-bounded standalone `Elk`, so case-insensitive `\bELK\b` returns 1 file, not 0. Case *sensitivity* is what settles it, and the review's own parenthetical "(`Elk` as a surname ×4)" contradicts its own "all word-internal" gloss. Conclusion unaffected; the test is not.
5. **The sibling research note is consumed, not a pending claimant.** The brief says `reviews/system-tune-2026-08-20` records [[interpretability-probes-representational-ambivalence-2026-08-20]] as "a claimant for a topics slot." Its own frontmatter carries `consumed_by: anti-correlation-probes-for-ai-consciousness` and its Angle 1 is annotated "FOLDED 2026-08-21." Either the tune report predates the fold or the two disagree; the note itself is the better authority for its own status.
6. **The interpretability count has three live values** — 20 (review), 23 (brief), 39 (this run) — and the leader's mention count has also moved (9 → 11). These are probably three correct measurements on three dates rather than one error, per `figure-disagreement-may-be-two-systems-not-one-error`. **Do not put any of these numbers in an article**; state the asymmetry, which is the durable finding, and re-measure if a count is ever needed.
7. **The review's Tenet 1 prediction is over-credited as "falsifiable-shaped."** See the tenet section above. This is the correction most likely to matter, because a downstream article that leans on it would import the Map's most contested commitment into an argument specifically designed to survive without it.
8. **The permanent/contingent binary is itself the framing to resist**, and the corpus supplies a better one. The voids taxonomy already sorts this kind of question three ways, and [[intrinsic-nature-void]] has already ruled on a structurally analogous inscrutability. The review's dichotomy is a good diagnostic question and a poor article structure.

## Gaps in Research

- **No source states the trusted-seed requirement.** It is this note's central analytical claim and it is entirely the Map's own, assembled from the architectures of six techniques. It is the part a hostile reviewer should attack. Its weakest joint: an agent might argue that a sufficiently strong prior over ontologies substitutes for a seed region, which is close to what ARC's heuristic-explanation programme hopes. The reply is that a prior over ontologies is itself a normative assumption of the kind Armstrong & Mindermann say must be imported — but that chain has not been checked against any literature, and the ARC heuristic-arguments papers were not read.
- **Position E (bounding as a rival to corrigibility) is unsourced.** I found no source arguing either direction. It rests on reading the off-switch result's uncertainty condition as the mechanism, and a specialist might hold that ontological adequacy and reward uncertainty are independent enough that the substitution does not go through.
- **Nothing here measures anything about humans.** Every source is about machine learning systems or is a formal result. There is no empirical work on whether human institutions bound their own representational error about persons, which is the obvious comparison class and would bear directly on whether the seed region is empty in principle or only currently.
- **The philosophy-of-reference bridge remains unfound after two independent runs.** Neither this note nor the 2026-08-20 sibling located a mature philosophy literature connecting these formal results to the philosophy of reference and self-knowledge. It may be genuinely thin. It may also be that I searched only through the AI-safety literature's own citation chains, which would not surface it. Before any article claims novelty in joining Putnam/Quine/Newman to ontology identification, search the philosophy literature directly.
- **Armstrong & Mindermann's Conjecture 9 has not been checked for subsequent resolution.** Someone may have proved or refuted it since 2018. The citation chain forward from that paper was not followed, and this is the cheapest high-value follow-up: if the conjecture has been proved, Position B strengthens considerably; if refuted, the note's one formal permanence result weakens.
- **The quantitative IRL-misspecification literature was not searched** (Skalse & Abate, STARC metrics). This is where a graded version of the impossibility result would live, and a graded version is what the certification asymmetry actually needs — the article's burden is one of *bounding*, and a bound is a number.
- **ARC's obstacles sequence and heuristic-arguments papers were not read.** Any claim about what the current programme can deliver rests here on a summary agenda post, which is the weakest evidential base in the note.
- **de Blanc (2011) was not read**, though it is already cited by the reviewed article and is the ancestor of the whole chain. The article's characterisation of it went unchecked.

## Citations

1. Christiano, P., Cotra, A., & Xu, M. (2021). *Eliciting latent knowledge: How to tell if your eyes deceive you*. Alignment Research Center. https://www.alignment.org/blog/arcs-first-technical-report-eliciting-latent-knowledge/ — **ARC technical report, not peer-reviewed, stated credences; reached in full via the Google Docs txt export.**
2. Soares, N. (2015). *Formalizing Two Problems of Realistic World-Models*. Machine Intelligence Research Institute. https://intelligence.org/files/RealisticWorldModels.pdf — **MIRI technical report; peer-reviewed venue not confirmed; reached in full.**
3. de Blanc, P. (2011). Ontological Crises in Artificial Agents' Value Systems. arXiv:1105.3821. https://arxiv.org/abs/1105.3821 — **preprint; metadata verified only, full text NOT read this run.** Already cited by the reviewed article.
4. Burns, C., Ye, H., Klein, D., & Steinhardt, J. (2022). Discovering Latent Knowledge in Language Models Without Supervision. arXiv:2212.03827; **ICLR 2023**. https://arxiv.org/abs/2212.03827 — **peer-reviewed empirical ML paper; average-case, not a bound; reached in full.**
5. Farquhar, S., Varma, V., Kenton, Z., Gasteiger, J., Mikulik, V., & Shah, R. (2023). Challenges with unsupervised LLM knowledge discovery. arXiv:2312.10029. https://arxiv.org/abs/2312.10029 — **preprint (Google DeepMind); two proved theorems plus experiments, with future-method claims marked as speculation by the authors; no peer-reviewed venue confirmed; reached in full.**
6. Armstrong, S., & Mindermann, S. (2018). Occam's razor is insufficient to infer the preferences of irrational agents. arXiv:1712.05812; **NeurIPS 2018, pp. 5603–5614**. https://arxiv.org/abs/1712.05812 — **peer-reviewed formal result; two theorems plus Conjecture 9; venue verified at proceedings.neurips.cc; reached in full.**
7. Roger, F., Greenblatt, R., Nadeau, M., Shlegeris, B., & Thomas, N. (2023). Benchmarks for Detecting Measurement Tampering. arXiv:2308.15605. https://arxiv.org/abs/2308.15605 — **preprint (Redwood Research); benchmark/datasets paper with partial results; reached in full.**
8. Burns, C., Izmailov, P., Kirchner, J. H., Baker, B., Gao, L., Aschenbrenner, L., Chen, Y., Ecoffet, A., Joglekar, M., Leike, J., Sutskever, I., & Wu, J. (2023). Weak-to-Strong Generalization: Eliciting Strong Capabilities With Weak Supervision. arXiv:2312.09390. https://arxiv.org/abs/2312.09390 — **OpenAI technical report / preprint; empirical, proofs-of-concept by the authors' own description; reached in full.**
9. Brown-Cohen, J., Irving, G., & Piliouras, G. (2023). Scalable AI Safety via Doubly-Efficient Debate. arXiv:2311.14125. https://arxiv.org/abs/2311.14125 — **preprint (Google DeepMind); complexity-theoretic result conditional on human verifiability; reached in full.**
10. Christiano, P. (2020). *Inaccessible information*. Alignment Forum. https://www.alignmentforum.org/posts/ZyWyAJbedvEgRT2uF/inaccessible-information — **research blog post; framing rather than results, by the author's own description; reached in full via greaterwrong.com.**
11. Hilton, J. (2024). *A bird's eye view of ARC's research*. Alignment Research Center. https://www.alignment.org/blog/a-birds-eye-view-of-arcs-research/ — **organisational agenda post; intentions, not results; reached in full.**
12. Hilton, J. (2025). *Obstacles in ARC's research agenda*. Alignment Research Center. https://www.alignment.org/blog/obstacles-in-arcs-research-agenda/ — **pointer post only (1.2 KB); the three linked Matolcsi posts were NOT reached.**
13. Newman, M. H. A. (1928). Mr. Russell's "Causal Theory of Perception". *Mind*, 37(146), 137–148. — **cited via the corpus's existing treatment in [[primary-secondary-quality-boundary]]; not fetched this run.**
14. Hadfield-Menell, D., Dragan, A., Abbeel, P., & Russell, S. (2016/2017). Cooperative Inverse Reinforcement Learning; The Off-Switch Game. — **cited via the corpus's existing treatment in [[instrumental-convergence]]; not fetched this run.**
