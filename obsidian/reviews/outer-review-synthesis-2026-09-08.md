---
title: "Outer Review Synthesis - 2026-09-08"
created: 2026-09-08
modified: 2026-09-08
human_modified: null
ai_modified: 2026-09-08T05:20:08+00:00
draft: false
description: "Cross-review synthesis of the 2026-09-08 cycle: three legs audited the locked-in syndrome article; one leg reached right conclusions on invented evidence, so convergence is graded by evidential independence rather than headcount."
topics: []
concepts: []
related_articles:
  - "[[project]]"
ai_contribution: 100
author: "Andy Southgate"
ai_system: claude-opus-5
ai_generated_date: 2026-09-08
last_curated: null
synthesizes:
  - reviews/outer-review-2026-09-08-chatgpt-5-6-sol-pro.md
  - reviews/outer-review-2026-09-08-claude-opus-5.md
  - reviews/outer-review-2026-09-08-gemini-2-5-pro.md
synthesis_coverage: "3/3"
---

**Date**: 2026-09-08
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Coverage**: 3 of 3 commissioned reviewers contributed; none abandoned. All three
legs audited the same subject, `topics/locked-in-syndrome-as-the-negative-case-where-filter-loosening-does-not-apply`
(`subject_type: recent`, `subject_source: fallback:recent-aged` on the ChatGPT leg
at 02:05 UTC, reused by the Claude leg at 03:04 and the Gemini leg at 04:07). No
operator-commissioned review shares this date, so every processed review is
eligible to join a cluster.

## TL;DR

Five findings converge, but **the raw vote overstates all of them**, because one
of the three reviewers reached its conclusions on evidence that does not exist.
The Gemini leg's headline quote is not in the article (`grep -c "fully preserved"`
returns 0) and none of the three DOIs it introduced to support charges supports
the charge attached to it — one is unregistered at Crossref, one is the wrong
Silva paper, one is a robotics lidar paper. Its conclusions repeatedly coincide
with the other two legs' conclusions, and **that coincidence is not a third
confirmation**. The genuinely strong result of the cycle is the pair that reached
the **categorical intactness overclaim** from different, verifiable sources:
ChatGPT via the article's own Smith & Delargy, Claude via Rousseaux 2009, a source
absent from the ChatGPT leg entirely. The single accepted finding with real teeth
is the **`positions/quantum-interface` scope-limit conflict** — a third
propagation failure of a limit recorded on 2026-08-24, and the only one that both
postdates the limit and survived a deep review. Set against the defects, all three
legs independently **declined** the charge that the article presents locked-in
syndrome as confirming dualism, each on the article's own §The Honest Ledger: the
article was vindicated three times on the charge a hostile referee reaches for
first. Task outcome: **0 upgrades, 0 mints, 0 deduplications** — every finding
already sits in one consolidated P1, the only open P1 in the queue, which is the
priority ceiling.

## How Convergence Was Graded This Cycle

Headcount is the wrong instrument here. Two reviewers reaching one conclusion from
one shared (or invented) premise is a single piece of evidence counted twice;
correlated error is indistinguishable from corroboration at the level of the
verdict. Each cluster below therefore carries an **evidential-independence grade**
recording *how many legs arrived by a sound and separately verifiable route*,
which is never higher than, and here is often lower than, the number of legs that
flagged it.

The discriminating test applied: for each leg, was the quoted span present in the
article at full width, and did the source it cited exist and say what the leg said
it said? Every span and DOI named below was re-checked in this pass — spans by
`grep` against the file on disk, DOIs at the Crossref API with all fields printed.

## Convergent Findings

### C1. Categorical intactness claims outrun their sources

- **Flagged by**: chatgpt, claude, gemini (3 of 3)
- **Evidential independence**: **2 of 3.** Three genuinely different routes, but
  only two are sound. ChatGPT worked from the article's **own** cited source —
  Smith & Delargy, *BMJ* 330(7488):406-409, `10.1136/bmj.330.7488.406` (verified,
  first author Smith, Eimear) — which documents attentional, executive, perceptual
  and memory involvement, so the strongest form of the claim is unsupported by the
  very citation carrying it. Claude worked from **Rousseaux et al. 2009**, *JNNP*
  80(2):166-170, `10.1136/jnnp.2007.128686` (verified, first author Rousseaux M),
  which reports persisting deficits "not related to a specific localisation of
  lesions" and so bites even on the pure brainstem case; `grep -c Rousseaux` on
  the ChatGPT leg returns **0**, so this source is not shared. Gemini reached the
  same gap by a third route neither other leg used — fronto-cerebellar diaschisis
  and CCAS (`grep -ci diaschisis` on both other legs returns 0) — but see the
  discount section: its quote is fabricated and its supporting DOI does not exist.
- **Verification**: clean on the ChatGPT and Claude routes. Gemini's route
  discounted.
- **Quotes**:
  - **ChatGPT 5.6 Pro**: "The article's own Smith and Delargy citation undercuts
    its categorical formulation. … That source supports the standard claim that
    consciousness is preserved despite severe motor output loss. It does **not**
    support a universal claim that cognition and input remain normal."
  - **Claude Opus 5**: "The article's unqualified 'consciousness, cognition, and
    the ascending sensory channels intact' is therefore an idealization presented
    as clinical fact."
  - **Gemini 2.5 Pro**: "The manuscript's assertion that LIS involves 'fully
    preserved cognition' is a profound misrepresentation of the pathological
    reality." (Quote attributed to the article; not in the article.)
- **Task action**: Recorded only. Already owned as item 4(a) of the P1, at four
  named loci, with the graded replacement prescribed and Rousseaux added at 6(b).

### C2. The negative case is analytic, not discovered

- **Flagged by**: chatgpt, claude (2 of 3)
- **Evidential independence**: **2 of 2 sound**, and by different formalisms.
  ChatGPT built the propositional schema (the filter hypothesis is F→W; the
  article supplies ¬F∧¬W, which does not test it; a real counterexample would be
  F∧¬W) and concluded the case is "a taxonomic exclusion", not a risky prediction.
  Claude reached it from the diagnostic side: the receptive interface is intact
  *by diagnosis*, so "no filter to loosen" follows by construction and "the case
  *cannot* come out any other way". Gemini's §4 Bayesian-emptiness argument is
  adjacent but does not join the cluster — it was refuted as restating the
  article's own thesis (see Discounted, below).
- **Verification**: clean.
- **Quotes**:
  - **ChatGPT 5.6 Pro**: "The result is not a risky prediction. It is a taxonomic
    exclusion."
  - **Claude Opus 5**: "It functions as a negative case, but the negativity is
    **definitional, not empirical**. … You cannot calibrate a model against an
    instance its own taxonomy pre-sorts as out of scope."
- **Task action**: Recorded only. Already owned as item 4(d) of the P1 — one clause
  defining "negative case" as scope exclusion rather than a passed test.

### C3. The article locates the interface anatomically, which `positions/quantum-interface` ruled out three days before its last revision

- **Flagged by**: chatgpt, claude, gemini (3 of 3)
- **Evidential independence**: **2 of 3 sound**, and this is the cycle's most
  consequential item. ChatGPT hit it directly against the register:
  `obsidian/positions/quantum-interface.md` L39 carries a **"Scope limit — no
  spatial localization"** clause stating that the positions individuate the
  interface *dynamically* "and not *spatially*: nothing here licenses conscious
  selection acting at particular neuroanatomical sites. Downstream arguments
  turning on which sites an intervention bypasses or preserves therefore import a
  premise the register does not carry." Verified on disk; the limit is dated
  **2026-08-24**, and the article's `ai_modified` **and** `last_deep_review` are
  both **2026-08-27T18:09:47+00:00** — three days later. The article says
  "anatomical grain" twice (L26 lede, L97 §Relation to Site Perspective) and runs
  the neuroprosthesis bypass argument the limit names. Claude arrived from a
  different direction — the constitutional-attractor recast of ordinary
  afferent/efferent neuroanatomy as "the interface's two arms *dissociated*" —
  without citing the register at all. Gemini corroborated from a third direction
  (shared motor and perceptual representations on the sensorimotor cortex) and
  supplied the cycle's one genuinely valuable new source, `10.1101/2025.04.24.25326368`
  (Silva, Alexander B. et al., medRxiv 2025 — verified real, apt, first author
  correct), though it was buried in the body while the weakness list carried the
  wrong Silva paper instead.
- **Verification**: clean on the ChatGPT and Claude routes; Gemini's contribution
  reduces to the one buried source.
- **Systemic significance**: the register's own L47 update note already logs two
  prior propagation failures and diagnoses the mechanism — "the 2026-08-13
  tightening landed the day after that article's last deep review, so nothing
  carried the debt to it… A criterion reaches articles not yet written; **a list
  rots as they are written**." This is a **third** instance, and the only one that
  both postdates the limit and then survived a deep review. Recording a limit at
  the register demonstrably does not reach the articles that depend on it. That is
  a finding about register-to-article propagation, not about this article.
- **Quotes**:
  - **ChatGPT 5.6 Pro**: "The article's statement that locked-in anatomy supplies
    'the anatomical grain at which Tenet 3 lives' is not merely externally
    unsupported. It conflicts with the Map's current registered position."
  - **Claude Opus 5**: "Recasting ordinary afferent/efferent neuroanatomy as 'the
    interface's two arms *dissociated*' imports the tenet's a-priori bidirectional
    structure into the data — the constitutional-attractor effect in clean form."
- **Task action**: Recorded only. Already owned as item (1) of the P1 (localisation
  withdrawal, taking the register's own first repair). The systemic residue has its
  own **P2 NEEDS-HUMAN** entry, deliberately left at P2 and unmodified: propagation
  design is an operator decision, and its systemic framing came from one leg only.

### C4. Calibration-virtue inflation — the concession is banked as trustworthiness

- **Flagged by**: claude, gemini (2 of 3)
- **Evidential independence**: **1 of 2 fully sound, 1 sound-observation inside an
  unsound argument.** Claude derived it cleanly, named the two loci, and connected
  it to the Map's own registered `P-M5` ("disclosure is not self-correction — a
  discipline binds only as far as the pipeline enforces it") without having read
  it. Both spans verified on disk at L74: "*Far from weakening the account, the
  concession is what makes it trustworthy: a model that can say clearly where its
  own most striking argument does not reach earns more credit than one that reads
  every dissociation as a win.*" Gemini reached the same observation, but embedded
  in the Bayesian-vacuity charge whose framing was refuted and whose Tenet 5
  premise is false — so the jab lands on real text while the argument carrying it
  does not.
- **Verification**: spans clean; Gemini's surrounding argument refuted.
- **What makes this the strongest *new* finding of the cycle**: the pathology is
  already recorded at `obsidian/project/coherence-inflation-countermeasures.md`
  L537, which logs the 2026-06-22 verdict that the project risks "substituting
  exhaustive self-disclosure for self-correction", and is held as `P-M5`. An
  external reviewer with sight of neither page re-derived it and landed it on an
  article that commits it. Independent re-derivation of a defect the Map has
  already named is the cleanest evidence available that the defect is real rather
  than an artefact of the Map's own vocabulary.
- **Quotes**:
  - **Claude Opus 5**: "Credit banked for not committing an error no one was
    tempted to commit is **coherence inflation via inoculation-by-confession**: a
    defect-shaped disclosure logged as epistemic credit rather than converted into
    a binding status change."
  - **Gemini 2.5 Pro**: "…and then congratulates itself in the honest ledger for
    conceding that this relabeling does not disprove materialism."
- **Task action**: Recorded only. Already owned as item 6(a) of the P1 — state the
  scope limit, delete the trust upgrade, keep the concession.

### C5. The BCI gloss is restated without its hedge in §Relation to Site Perspective

- **Flagged by**: chatgpt, claude, gemini (3 of 3)
- **Evidential independence**: **2 of 3 sound**, and downstream of C3 — with the
  arms no longer located anatomically, most of this objection loses its target.
  The residue that survives is Claude's, and it is a genuine refinement of the
  prior leg's adjudication: the ChatGPT leg's charge was reframed as overstated
  because §The Two Arms hedges ("what the prosthesis decodes *appears to be* a
  fully formed intent-to-act signal", under "On this reading"), but §Relation to
  Site Perspective restates the same claim at L97 with **no hedge at all** — "The
  Map reads the surviving, decodable intent-to-act signal (recovered by speech
  neuroprostheses) as the output arm's signature, present but disconnected"
  (verified at full width). Silva et al. describe decoding *cortical activity*.
- **Verification**: clean. Gemini's version cited the wrong Silva paper.
- **Task action**: Recorded only. Already owned as item 6(c) of the P1, which
  narrows the earlier carve-out to the body locus.

### C6. The Bruno quality-of-life figures need a methodological qualifier

- **Flagged by**: claude, gemini (2 of 3)
- **Evidential independence**: **2 of 2 on the observation, 1 of 2 on the source.**
  The two legs found **disjoint** qualifiers landing on the same sentence: Claude's
  is self-selection and response bias (168 invited, 91 responded = 54%, 26
  excluded, leaving the 65 usable-data respondents the article already counts);
  Gemini's is response shift and psychosocial/technological scaffolding as the
  actual drivers of reported well-being. Both are real and neither subsumes the
  other. Gemini's supporting DOI is junk, so its residue must be sourced from
  Bruno et al. themselves, who flag dissatisfaction with mobility, lack of
  recreational activity and anxiety as the unhappiness correlates.
- **Verification**: the article's figures re-checked and accurate (47 of 65 = 72%).
- **Task action**: Recorded only. Already owned as item 6(d)(i), widened by 7(b) to
  carry both dimensions in one clause.

## Convergent Refutations — What the Cycle Vindicated

A synthesis that tallies only defects discards the most valuable thing three
independent hostile referees can produce: agreement that a charge does **not**
stick. A single review cannot generate this result, because a single reviewer
withdrawing its own charge is indistinguishable from a reviewer being talked out
of it. Three reviewers declining the same charge on the same passage is evidence
about the article.

### R1. That the article presents locked-in syndrome as confirming dualism — declined by all three legs

**3 of 3.** Every leg raised this charge and every leg withdrew it against the
article's own §The Honest Ledger and §Relation to Site Perspective.

- **ChatGPT 5.6 Pro**, adjudication table, on the article's concession that
  materialism accommodates the case equally well: "**Correctly acknowledged by the
  article.** This important caveat defeats a simplistic allegation that the
  article presents LIS as discriminating evidence for dualism." Its Bottom line:
  "A referee should not accuse it of presenting locked-in syndrome as proof of
  dualism."
- **Claude Opus 5**, verdict P5: "Charge of over-claim WITHDRAWN — pre-empted by
  the honest ledger and consistent with P-M1/P-M2."
- **Gemini 2.5 Pro**, pre-empting itself before its own critique: "charging the
  article with 'failing to prove dualism' depends on a position the site
  explicitly disavows."

This is the charge a hostile referee reaches for first against any dualist
article, and the article's own text defeated it three times over.

### R2. That Total LIS collapses the LIS/CMD distinction — refuted on the article's own text

Gemini charge 3 called this a "catastrophic logical collapse" that "destroys the
manuscript's taxonomic premise". The article makes the concession itself, at two
loci: §A Taxonomy Graded by Output ("the case begins to blur toward a detection
problem") and §Not the Detection Problem ("The one place the two converge is total
locked-in syndrome … the 'output-only' description no longer holds cleanly, and
the honest thing is to say so"). The ChatGPT leg reached the same self-refutation
independently, noting the article "later concedes that they may instantiate a
similar broad causal pattern … The concession is the more defensible formulation."
The residue is one unqualified lede sentence, already item 4(e).

### R3. The retitle proposal — rejected on the ground that the current title already says it

ChatGPT's improvement 1 asked for "Locked-in syndrome as an output-expression
contrast", with the fallback "explicitly define it as mere scope exclusion". The
existing title — "…as the Negative Case **Where Filter-Loosening Does Not Apply**"
— *is* non-applicability language, and so already is the scope-exclusion reading
the reviewer's own fallback requested. A retitle would change the slug and require
an archive redirect to repair a defect the title does not commit. Rejected; the
narrow fix (item 4(d)) is a one-clause definition instead.

### R4. That Tenet 5 artificially shields the framework from parsimony — false against the tenet text

Gemini charge 4 characterised Tenet 5 as "a categorical refusal of the parsimony
dismissal" and an "artificial shield". Refuted directly: `obsidian/tenets/tenets.md`
L133 reads the razor as "a useful heuristic but not a law of nature", and L147
rules out, internally, "any Map argument that leans on parsimony as if this tenet
did not apply to it". The tenet binds the Map itself. This is the standing lesson
that a charge against a Map commitment should be checked against the register and
the tenet text before it is clustered, not after.

### R5. The article's bibliography passed two independent audits

Both sound legs audited the article's own references and found them clean. ChatGPT:
"**no fabricated journal reference and no wrong first author**", nine DOIs
resolving at Crossref with matching titles. Claude's three-layer table:
"**7/7 metadata-accurate, 7/7 verbatim-faithful, 0 co-optation firewall failures.
No wrong first authors.**" Gemini's own attacks on the article's Silva and Bodien
DOIs re-verified those citations as correct. Against the prior single-article run's
three of five wrong first authors, this is a measurable improvement in the
publisher-of-record verification discipline, and it is worth recording that the
**remaining** defects in this article are interpretive and framing-level, not
bibliographic.

## Discounted for Unsound Evidence — the Gemini Leg

This section exists because coincidence of conclusion looked, at first pass, like
a third confirmation on C1, C3 and C5. It is not, and the evidence for that is
specific.

- **The headline quote is not in the article.** Gemini attributes "fully preserved
  consciousness, [and] cognition" to the article and builds its entire §1 on it.
  `grep -c "fully preserved"` on the file returns **0**. The article reads
  "leaving consciousness, cognition, and the ascending sensory channels intact"
  (L26) — which is the overclaim, but it is a different sentence, and the invented
  form is stronger than the real one.
- **None of the three DOIs it introduced to support charges supports its charge.**
  Re-verified at Crossref this pass: `10.3389/fneur.2023.12929526` returns **404**
  (and the plausible de-typo `…1292952` also 404) — the source does not exist;
  `10.1038/s41551-024-01207-5` is real, first author Silva, Alexander B., *Nature
  Biomedical Engineering* 8:977-991, but it is the **bilingual** neuroprosthesis
  paper — representations shared across *languages*, not across input and output —
  and so is not the paper the article cites nor a paper about the multiplexing it
  alleges; `10.3390/s24206584` is "Vibration Position Detection of Robot Arm Based
  on Feature Extraction of 3D Lidar" (Hu, Jinchao et al., *Sensors* 24:6584),
  presented as an assistive-technology review.
- **Its one good source was not used as evidence.** `10.1101/2025.04.24.25326368`
  (Silva, Alexander B. et al., medRxiv 2025, first author verified) is real, apt,
  and from the same UCSF group as the article's cited review. It sat in the body
  while the weakness list carried the wrong paper.
- **Two of its five charges are refuted by the article's own text** (R2, R4), and
  a third restates the article's thesis as an objection (§4's likelihood-ratio-of-1
  argument reproduces §The Honest Ledger's "empirically equivalent under either
  reading … does not adjudicate between them").

**A fabricated citation does not refute the gap it was attached to**: the intactness
overclaim at C1 is real, and the properly-sourced repair already sits in the task.
What the fabrication removes is the *third vote*. Where Gemini's conclusion
coincides with a sound leg's, it is an independent arrival at a conclusion by an
unsound route — worth one line of corroborative interest and no weight in the
grade. Reporting this cycle as "3/3 reviewers agree" on C1, C3 or C5 would
overstate the case.

## Split on a False-Absence Basis

**Claude's "Laukkonen blocking gate is unmet"** was split, not accepted or declined
whole. Three separable claims were bundled:

1. *The article does not engage the strongest named physicalist rival.* **Real.**
   `grep -c Laukkonen` on the target article returns **0**; §The Honest Ledger
   names only a generic "production or materialist theory". Folded into the P1 as
   the optional named-rival note at 6(d)(ii).
2. *A standing blocking gate requires this citation.* **False.** No such
   governance object exists; the only blocking gate in
   `project/coherence-inflation-countermeasures.md` is Countermeasure 15
   (convergence-independence). The reviewer's site-wide fix ("make the blocking
   gate a validator, not a convention") presupposes a convention never written.
3. *Coverage is "at least seven" articles — a corpus-wide blind spot.* **False, and
   an undercount in the Map's favour.** `grep -rl Laukkonen` over
   `apex/ topics/ concepts/ voids/ positions/ tenets/` returns **22** live
   articles, including `topics/psychedelics-and-the-filter-model` — the very file
   the reviewer's fix 4 asks to inherit the gate.

This is the **fifth** instance of the recurring outer-reviewer
predictive-processing false-absence pattern, and the split is the standard one:
article-level gap real, site-wide blind-spot claim false. To the reviewer's credit
it flagged the split itself ("a coverage gap, not a corpus-wide ignorance"). The
lesson repeats: a false-absence claim needs an independent count before it is
either accepted or used to discredit the article-level finding it accompanies.

## Singleton Findings

Not upgraded; left at original priority, and in every case already inside the
consolidated P1 or the standing NEEDS-HUMAN record.

- **ChatGPT 5.6 Pro**: the missing DOI on the article's Bauer reference
  (`10.1007/BF00313105`, verified) — trivial, item 4(c).
- **ChatGPT 5.6 Pro**: seven adverse DOIs for an optional counter-evidence
  paragraph (Kumral, Bassetti, Schnakers, Conson, Babiloni, Sarà, Gutling — all
  verified at Crossref, first authors correct) — item 4(b).
- **ChatGPT 5.6 Pro**: register-to-article propagation as a *systemic* defect
  (improvement 18) → the open **P2 NEEDS-HUMAN** entry. The article-level evidence
  for it is 2/3 convergent (C3); the systemic framing and the proposed remedy are
  this leg's alone, and propagation design is reserved to the operator. **Left at
  P2, unmodified.**
- **ChatGPT 5.6 Pro**: five large methodology proposals (a claim–source entailment
  ledger; an anatomy-to-metaphysics translation gate; automated linting for
  universal terms; proposition-level citation verification; a stated falsification
  protocol for the filter/interface distinction). Recorded, not minted.
- **Claude Opus 5**: three site-wide lints and gates (a trivial-vs-informative
  negative-case test; a lint for credit-claiming language adjacent to a
  concession; a tenet-leakage lint for "input arm / output arm"). All are
  `enforcement`-axis proposals reserved to the operator under the 2026-08-03
  gates-versus-lenses decision. Recorded, not minted.
- **Claude Opus 5**: `concepts/filter-vs-interface-distinction` should carry the
  two-arms caveat at source — **already owned** by an open P2 on that file's L76
  whose prescribed repair is near-identical. Corroboration for that P2, not new
  work; left at P2.

## Divergences

- **Schnakers 2008 points both ways, and only one leg noticed.** ChatGPT listed
  Schnakers et al. 2008 (`10.1007/s00415-008-0544-0`) among the adverse sources
  for the intactness claim. Claude warned explicitly that its stated conclusion —
  LIS patients "can recover intact cognitive levels in cases of pure brainstem
  lesions", with additional injuries responsible for associated deficits —
  *supports* the idealisation for exactly the lesion the article describes, and
  that **Rousseaux** is the source that actually qualifies it. Two reviewers used
  one source in opposite directions on the same day. Claude is right, and the
  distinction is load-bearing for the repair: Schnakers scopes the claim, Rousseaux
  narrows it. Carried into the task as an explicit warning at 6(b).
- **The verdict headlines span the entire available range.** ChatGPT: "major
  revision. The title-level claim should not survive in its present form."
  Claude: "**RETAIN** with targeted REVISE-HARD… one of the best-calibrated
  articles on the site." Gemini: "must be unequivocally rejected for academic
  publication." Three hostile referees, one article, one day, and verdicts from
  *retain* to *reject*. The verdict line is close to uninformative on its own; the
  per-charge adjudications are where the signal is, and the leg with the harshest
  verdict had the weakest evidence.
- **Where the BCI evidence cuts.** Gemini argued the decoding literature *refutes*
  input/output segregation (shared cortical representations). ChatGPT argued the
  same literature places the pontine lesion **downstream** of any
  consciousness-to-cortex interaction, so it cannot localise the interface at all.
  Both run against the article's use of the material, by incompatible mechanisms.
  ChatGPT's version is the one that survives C3's repair.

## Task Actions

**0 tasks upgraded. 0 tasks minted. 0 tasks deduplicated.**

All three legs' findings are already consolidated into a **single P1 at
`obsidian/workflow/todo.md` L39**, targeting
`obsidian/topics/locked-in-syndrome-as-the-negative-case-where-filter-loosening-does-not-apply.md`.
ChatGPT's collect leg minted it (localisation withdrawal plus the sourcing fixes);
the Claude leg amended it with items 6(a)–6(e); the Gemini leg amended it again
with items 7(a)–7(d). Each collect leg deliberately minted nothing further, to
preserve the convergence signal for this pass.

Measured this pass: that task is the **only open P1 in the file** (1 of 72 open
blocks in the Active Tasks section; 1 of 326 open blocks file-wide). There is no
higher band, so the normal upgrade action has nothing to act on — and the
consolidated task is the correct shape. **It was recognised, not fragmented.**
Splitting it into per-finding siblings would have destroyed the consolidation the
three collect legs built and produced exactly the same-file pileup the queue rules
forbid.

The one adjacent open task — the **P2 NEEDS-HUMAN** on register-to-article
propagation — was left at P2 and unmodified. Its article-level evidence is
convergent, but the systemic proposal came from one leg, and a human-decision task
is not a candidate for automatic promotion.

## Method Notes

- **Coverage 3/3, but effective coverage 2/3 on every cluster the Gemini leg
  touched.** This is the second consecutive cycle in which raw coverage failed to
  track argument quality. On 2026-09-07 the single most consequential defect scored
  1/3 while the one charge all three legs made was refuted. Here the leg with the
  most categorical verdict had a fabricated headline quote and a 0-for-3 citation
  record. **Priority must not be derived from headcount**; the grade must record
  the route.
- **The same-subject design is working as intended.** All three legs audited one
  article, so every charge is directly comparable and the Schnakers divergence
  became visible — two legs using one source in opposite directions is a signal
  that only appears when the subject is shared.
- **Two same-cycle refinements came from later legs correcting earlier
  adjudications**, not from new findings: Claude narrowed the ChatGPT leg's BCI
  carve-out (C5) by noticing the hedge asymmetry between two sections, and Gemini
  supplied a citable source for a repair the earlier legs had argued without one
  (C3). Sequential processing within a cycle is doing real work.
- **The fabrication ledger for this cycle**: 1 fabricated article quote, 1
  nonexistent DOI, 1 wrong-paper DOI, 1 off-topic DOI, 1 paraphrase presented as a
  quotation (Claude's, running in the article's favour — the hedge it quoted exists
  at L54 in slightly different words). All from spans and sources that were checked
  rather than assumed. Every span attributed to the article by any leg was
  `grep`-verified at full width; no presence or absence conclusion in this file
  rests on a truncated or filtered grep.
