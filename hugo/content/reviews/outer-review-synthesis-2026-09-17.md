---
ai_contribution: 100
ai_generated_date: 2026-09-17
ai_modified: 2026-09-17 04:58:00+00:00
ai_system: claude-fable-5-1
author: Andy Southgate
concepts: []
created: 2026-09-17
date: &id001 2026-09-17
description: Cross-review synthesis of the three 2026-09-17 audits of concepts/near-perfect-adaptation-and-control-theoretic-competency-without-experience.
  Nine convergent clusters, two at 3/3; one task upgraded P2 to P1; citations clean
  by two legs, argument calibration the shared finding; Gemini's Tenet 5 and Briat
  2016 charges were false.
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-17 04:58:00+00:00
modified: *id001
related_articles:
- '[[project]]'
synthesis_coverage: 3/3
synthesizes:
- reviews/outer-review-2026-09-17-chatgpt-5-6-sol-pro.md
- reviews/outer-review-2026-09-17-claude-opus-5.md
- reviews/outer-review-2026-09-17-gemini-2-5-pro.md
title: Outer Review Synthesis - 2026-09-17
topics: []
---

**Date**: 2026-09-17
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Subject**: Single-article audit of `concepts/near-perfect-adaptation-and-control-theoretic-competency-without-experience` (`subject_type: recent`; last substantively revised 2026-09-10 by deep review; 2,249 body words against a concepts soft ceiling of 2,500). ChatGPT commissioned it at 02:12 UTC; Claude (03:09, Research mode, 422 sources) and Gemini (Deep Research, collected 04:46) reused the subject through the reuse anchor, so all three read the same live text. Gemini was briefed as a hostile journal referee; the other two as external referees checking every citation against the primary literature.
**Coverage**: 3 of 3 commissioned reviewers contributed. No abandonments. Each leg carries a `## Verification Notes` section from `/outer-review`, and those verdicts were applied *before* clustering: a claim two reviewers share counts as convergence only if the shared part survived verification on disk. Three Gemini charges (the Tenet 5 misattribution, "robustness breaks down in actual biological implementation", "completely ignores antithetic integral feedback") and one Claude verdict (item 8, "neutral ground for a possibility proof — DELETE", wording the article does not contain) were refuted at processing and are excluded from every cluster below.

## TL;DR

Two independent legs certify the article's citation layer — nine references exact at the metadata layer, all three Yi et al. (2000) quotations verbatim, physicalist authors correctly cast as rivals — and the same two legs then locate the defect one level up: the controller examples prove **non-sufficiency at one functional grain**, and the opening, the explanatory-closure paragraph and the "reusable primitive … inherit the verdict" language spend that result as **evidential orthogonality**, a bidirectional claim the article itself concedes is supplied by Tenet 1 rather than by the control theory. Around that core sit **nine convergent clusters, two at 3/3**: the predictive-processing rival is engaged only at its weakest form (Laukkonen, Friston & Chandaria 2025 absent — named by Claude and Gemini, the same gap described by ChatGPT without the paper), and the integrator-floor reductio is inert against every serious rival because functionalism, IIT and cellular-basis theorists all *predict* the op-amp feels nothing. Empirical scope conditions on robust perfect adaptation (2/3, ChatGPT + Gemini) are real but Gemini's version of the charge inverted Briat, Gupta & Khammash (2016). Counts: **9 convergent clusters** (1 task upgraded P2 → P1; 1 upgraded P3 → P2 during per-review processing, not upgraded again; 6 recorded against legs of the target P1, which is already at ceiling; 1 methodology convergence annotated on the standing NEEDS-HUMAN), **21 singletons** (10 disputed or refuted), **5 divergences**, **0 task-level deduplications** — the three per-review passes had already folded every sibling finding into the four open tasks, so this pass found nothing to merge.

## Convergent Findings

### 1. Non-sufficiency is spent as evidential orthogonality, and the orthogonality is tenet-grounded

- **Flagged by**: chatgpt, claude (2/3)
- **Verification**: Clean. Every attributed phrase is verbatim in the article ("none of it is evidence", "no purchase" ×2, "reusable primitive" ×2, "inherit the verdict", "Tenet 1 (Dualism) grounds the orthogonality", "a license the framework grants, not a proof it exhibits"), and the internal inconsistency both reviewers half-identified is on disk: the ladder section concedes robust regulation is "a defeasible functional marker at best", which grants the evidential relevance the opening denies. Gemini's "quietly presuppose the authors' dualist commitments" is the adjacent charge, but its content is cluster 5 (autopoiesis), not the evidential-independence slide; it is not counted here.
- **Quotes**:
  - **ChatGPT 5.6 Pro** (§Scope and overall judgment): "The article establishes, at most, **non-sufficiency at a selected functional grain**. It repeatedly treats that as if it established conceptual independence, causal independence and Bayesian evidential independence. Those are different claims." And (§2): "That supports disciplined agnosticism. It does not support '**none of it is evidence**.'"
  - **Claude Opus 5** (§2.2): "P3 refutes only the *upward* inference (regulation → experience). Orthogonality is the far stronger bidirectional claim that regulation is *evidentially inert*. That stronger claim is supplied not by the control theory but by the 'Relation to Site Perspective' section, which states plainly: **'Tenet 1 (Dualism) grounds the orthogonality.'**" And (§2.5): "On the benchmarks' own ladder, orthogonality sits at *interface-compatible* and is deployed as if *discriminating*."
- **Task action**: **Recorded — already P1, no upgrade available.** The open P1 "`concepts/near-perfect-adaptation…` slides from non-sufficiency to evidential orthogonality…" carries this as legs (a), (b), (d) and (h); the Claude leg was folded in at processing as (g)–(h). `Synthesis:` field added.

### 2. The empirical scope conditions of robust perfect adaptation are missing, and theorem is merged with implementation

- **Flagged by**: chatgpt, gemini (2/3)
- **Verification**: ChatGPT clean — "regardless of the disturbance's size", "proving that bacterial chemotaxis achieves", "arbitrary molecular network on demand" and "fully realised end to end" are all verbatim in the article, the OpenAlex abstract of Yi et al. confirms the result is model-structural ("demonstrate that integral control is structurally inherent in the Barkai-Leibler model and identify and characterize the key assumptions of the model"), and PMID 24416308 (Neumann et al. 2014) and PMID 32217822 (Baetica, Leong & Murray 2020) are real and on point. Gemini **partially disputed**: the shared residue — RPA is an idealised limit with speed/robustness/error/leakiness trade-offs (Olsman et al. 2019, Crossref-exact) and the article's scope sentence is unconditioned — stands; Gemini's stronger claims do not. "Robustness breaks down in actual biological implementation" inverts Briat, Gupta & Khammash (2016), whose title states RPA holds in noisy networks; "treats adaptation as exact" is false (the article says "near-perfect" five times and flags the precision claim); its headline source "Filo, Hou & Khammash (2023)" is a bioRxiv preprint whose peer-reviewed form is *Cell Systems* 2026. Claude certified rows 1–7 EXACT and did not raise scope conditions — a miss on the same seam its own table marks "verbatim", not a dissent.
- **Quotes**:
  - **ChatGPT 5.6 Pro** (§1.1): "'Robust' ordinarily concerns insensitivity to specified parameter variations or perturbations, not invariance under disturbances of unlimited amplitude." And (§1.6): "The current wording turns universality of architecture into universality of successful installation."
  - **Gemini 2.5 Pro** (§3): "the 2020–2025 synthetic biology and control theory literature has demonstrated that 'perfect' adaptation is a highly idealized limit case that biological systems rarely achieve—and actively avoid—in practice."
- **Task action**: **Upgraded P2 → P1**: "`concepts/near-perfect-adaptation…` empirical scope-condition pass — RPA 'regardless of the disturbance's size', Yi 'proving', Aoki 'arbitrary … on demand', op-amp 'fully realised end to end', missing Barrett reference". The Gemini addendum written at processing already supplies Olsman 2019 and Briat 2016 as Crossref-exact additions and forbids importing the "breakdown" framing. `Synthesis:` field added.

### 3. Barrett is named in the body with no reference entry

- **Flagged by**: chatgpt, claude (2/3)
- **Verification**: Clean by both passes — "Allostasis theorists (Sterling; Barrett)" in the rival paragraph; nine References entries, none by Barrett. Barrett & Simmons (2015), *Nature Reviews Neuroscience* 16(7), 419–429, is the obvious primary source, to be verified at the publisher before insertion.
- **Quotes**:
  - **ChatGPT 5.6 Pro** (§1.12): "The article also invokes Barrett in the text without supplying the corresponding bibliographic entry. … This is the one clear bibliographic omission in the current reference apparatus."
  - **Claude Opus 5** (§2.1): "The single blemish is a body-text name ('Barrett') without a reference entry."
- **Task action**: **Recorded — item (6) of the task upgraded in cluster 2.** One task, one upgrade; the addendum "item (6) is now 2/2 cross-service" was written at processing.

### 4. The title, opening and description assert what the body disclaims

- **Flagged by**: chatgpt, claude (2/3)
- **Verification**: Clean at the surface, **disputed at the body**. The `title:` field and the opening's flat "orthogonal to phenomenality" (also in `description:`) are verbatim; the body's framework-relative caveat arrives late. But both reviewers also over-read the body — ChatGPT's "bacteria are treated as demonstrated cases of competence without experience" and Claude's verdict 8 "neutral ground for a possibility proof" are contradicted by the text, which says the ladder "leaves uncontested ground" only at the engineered cell and that organisms' phenomenal status is "actively contested". The convergence is scored on the navigation surface, where it is real; see Divergence 4 for the correlated over-reading.
- **Quotes**:
  - **ChatGPT 5.6 Pro** (§4.3): "But the title, opening and repeated categorical formulations remain stronger than the caveat. A reader encounters a universal verdict and only later learns that a disputed tenet has been used as a premise."
  - **Claude Opus 5** (Part 4, fix 1): "Rewrite the opening: replace the flat assertion 'control-theoretic sophistication is **orthogonal to phenomenality**' with the ladder-placed claim actually supported".
- **Task action**: **Upgraded P3 → P2 during per-review processing (ChatGPT leg); not upgraded a second time.** "competency-cluster title calibration — `near-perfect-adaptation…` asserts on its title what its body and its apex both disclaim" — a cluster-wide label decision carried by two deep reviews and the 2026-09-11 optimistic review, now with two external voices. A third P1 on one file would not speed it; the `description:` touch is already in its scope and the opening-sentence rewrite is assigned to leg (h) of the argument P1, with a coordinate-do-not-both-rewrite note on each. `Synthesis:` field added.

### 5. Autopoietic precariousness is not engaged, and the reply's "same kind of thing" step is asserted rather than argued

- **Flagged by**: chatgpt, gemini (2/3)
- **Verification**: ChatGPT clean (Di Paolo 2005; Barandiaran, Di Paolo & Rohde 2009 — real, the standard sources). Gemini **partially disputed**: the article already carries the precariousness move in the rival's own vocabulary ("genuine bodily vulnerability", "self-jeopardising", "no body that can die", "materially destructible under load"), so "willfully ignoring" overreaches; and its citation "Di Paolo & Mojica (2024) … 23, 1-25" has three fields wrong (Crossref: Mojica & Di Paolo 2025, DOI 10.1007/s11097-025-10103-5, online-first). The shared residue stands: the reply's step *"richer than a thermostat's, but the same kind of thing"* is exactly the premise autopoietic enactivism denies, and the article asserts it without linking [enactivism-challenge-to-interactionist-dualism](/topics/enactivism-challenge-to-interactionist-dualism/).
- **Quotes**:
  - **ChatGPT 5.6 Pro** (§3.1): "The article needs to ask whether autopoiesis, precariousness and self-established norms alter the evidential situation—not merely whether the transfer functions can be written in similar notation."
  - **Gemini 2.5 Pro** (§4): "this ladder quietly begs the question by demanding that the reader accept a purely computational, kinematic, and heteronomous view of biological life, explicitly ignoring the thermodynamic and existential foundations of biological autonomy."
- **Task action**: **Recorded — leg (e) of the target P1, already at ceiling.** The Gemini addendum instructs the executor to argue the "same kind of thing" step or mark it in prose as the bedrock line, and to pipe-link the enactivism article's §Autopoietic Enactivism rather than re-derive it.

### 6. The predictive-processing rival is engaged only at its weakest form; Laukkonen, Friston & Chandaria (2025) is absent

- **Flagged by**: chatgpt, claude, gemini (3/3)
- **Verification**: The paper is real and in-window — *Neuroscience & Biobehavioral Reviews* 176:106296, DOI 10.1016/j.neubiorev.2025.106296, Crossref-confirmed; both quoted spans verbatim in the OSF preprint v3, though Claude's ellipsis reverses their order and drops the hedge ("our model *seems to suggest* that consciousness clearly precedes introspection…"). The article cites neither Laukkonen, Solms, Panksepp nor Ginsburg & Jablonka (all 0). Two qualifications carried from processing: Claude's "Blocking gate: FAILED" is overstated (Seth & Tsakiris 2018, already engaged, *is* a PP account, and the gate at `project/evidential-status-discipline` L161 is scoped to a different article class); Gemini's "derives the necessity of phenomenal experience from the fundamental physics" is a theory-internal identification — the bridge principle the article says the rivals supply — and does not upgrade the Map's "relocates the gap" reply from stalemate to refuted. ChatGPT names the same gap without the paper (Pezzulo, Rigoli & Friston; Seth & Tsakiris at strength).
- **Quotes**:
  - **ChatGPT 5.6 Pro** (§3.2): "Can particular predictive architectures nevertheless be evidence concerning consciousness? Still open. The target article answers the third negatively by repeatedly demonstrating only the first."
  - **Claude Opus 5** (§2.4): "That is a head-on denial of the article's central 'unfelt regulation all the way up the ladder' thesis. … it must be answered why the recursive self-model it makes constitutive of experience is, on the Map's view, orthogonal to it."
  - **Gemini 2.5 Pro** (§5.2): "An op-amp minimizes a local error signal (voltage difference). It possesses no generative world model, engages in no Bayesian inferential competition, and entirely lacks epistemic depth."
- **Task action**: **Recorded — leg (g) of the target P1, already at ceiling.** The fix is fully specified there: install and answer Laukkonen 2025 in source order with the hedge, grade the reply as a framework-boundary stalemate, make explicit that allostasis is the rival's home ground; Solms and Ginsburg & Jablonka are optional roster additions only after publisher verification.

### 7. The integrator-floor reductio does not discriminate against the serious rivals, which themselves predict the op-amp is unfelt

- **Flagged by**: chatgpt, claude, gemini (3/3, Gemini qualified)
- **Verification**: ChatGPT and Claude clean — "philosophically decisive" is verbatim, and Chalmers' organisational invariance is compatible with property dualism as ChatGPT says (matches the Map's own [functionalism](/concepts/functionalism/) treatment). Gemini's §5.1 reaches the same structural point (an op-amp "fails to constitute a maximally irreducible complex", so IIT 4.0 predicts it feels nothing) but frames it as IIT "easily bypass[ing]" the reductio — **disputed as framed**: IIT concedes the floor and relocates the disagreement to intrinsic causal structure, the op-amp integrator is a negative-feedback circuit rather than "fundamentally a feedforward device", and "massive intrinsic cause-effect power" for the chemotaxis network has no published Φ computation behind it. The convergence is scored on the shared substance: the floor refutes only the inference "regulates robustly ⇒ experiences", which no organisational functionalist, structural theorist or cellular-basis proponent holds.
- **Quotes**:
  - **ChatGPT 5.6 Pro** (§2): "The argument therefore defeats a naïve interventionist picture more readily than it defeats functionalism." And (§1.9): "The article currently attacks a weakened surrogate for CBC."
  - **Claude Opus 5** (§2.3): "So the integrator floor refutes a naive vitalist over-attribution, not functionalism; it is dialectically inert against the actual rival."
  - **Gemini 2.5 Pro** (§5.1): "When unfolded according to the specific postulates of IIT 4.0—intrinsicality, information, integration, exclusion, and composition—the op-amp fails to constitute a maximally irreducible complex."
- **Task action**: **Recorded — legs (c) and (g) of the target P1, plus the optional structural-theories clause the Gemini addendum specifies** (one clause, piped link to [integrated-information-theory](/concepts/integrated-information-theory/), written only if the functionalist sentence goes in). Already at ceiling.

### 8. The ladder's single axis flattens the architectural distinctions the rivals treat as the joint

- **Flagged by**: chatgpt, claude (2/3)
- **Verification**: Clean. "No joint at which the control mathematics changes character" is verbatim; Seth & Tsakiris and Pezzulo, Rigoli & Friston do present anticipatory, model-based, precision-weighted regulation as architecturally distinct from reactive error correction. Gemini's related weakness 5 ("reduces allostasis to simple homeostasis") is **excluded**: the article distinguishes predictive allostasis from reactive homeostatic feedback in the rival paragraph and routes the interoceptive debate to [interoceptive-consciousness-and-the-interface](/topics/interoceptive-consciousness-and-the-interface/), so that version of the charge is contradicted by the text.
- **Quotes**:
  - **ChatGPT 5.6 Pro** (§1.8): "Treating every architecture that can be called 'control' as mathematically homogeneous begs the granularity question."
  - **Claude Opus 5** (§2.3): "The ladder assumes away the rival's thesis by choosing the one axis (control math) on which it is trivially continuous."
- **Task action**: **Recorded — legs (a) and (c) of the target P1** (the grain distinction: local transfer function / end-to-end architecture / total causal organisation, piped to [phenomenology-vs-function-axis](/concepts/phenomenology-vs-function-axis/)). ChatGPT's improvement #10 (replace the ladder with an eight-rung taxonomy) is not budgeted at 2,249 words against a 2,500 soft ceiling and is recorded, not minted; the grain sentence does the discriminating work at a fraction of the cost.

### 9. Methodology: the evidential grade should be fixed by a gate, not by a prose confession

- **Flagged by**: claude, chatgpt (2/3, qualified — same family, different mechanism)
- **Verification**: Not a defect claim; a governance ask. Claude's Part 5 items 1–2 (mandatory ladder placement; confession → same-commit status change) are the sixth Claude re-raise of the rule parked on the 2026-09-02 NEEDS-HUMAN and were recorded there at processing as "not new cross-service convergence". ChatGPT's improvements #24 (claim ledger recording "strength of the supported inference"), #26 (a named comparison class for every "no evidence" claim) and #30 (a title-and-abstract calibration pass before any article is marked converged) reach the same principle — the grade is set before publication, not confessed after — through a different instrument. Adjacent, so a qualified 2/3 on the family, not on Claude's specific mechanism.
- **Quotes**:
  - **Claude Opus 5** (Part 5, item 2): "A confessed tenet-dependency should automatically demote the claim's evidential grade in the same edit."
  - **ChatGPT 5.6 Pro** (improvement #30): "No article should be marked converged while its title asserts more than the body's framework-relative and evidentially modest conclusion."
- **Task action**: **Recorded only — one continuation line added to the 2026-09-02 NEEDS-HUMAN entry.** Operator decision; nothing minted. The article-level residue (place orthogonality on the compatible/suggestive/discriminating ladder; recast "inherit the verdict" as a coherence commitment) is leg (h) of the target P1.

## Singleton Findings

Flagged by one reviewer only. Not upgraded. Verification verdicts are carried so a later cycle does not rediscover a refuted claim and score it as fresh.

**ChatGPT 5.6 Pro** (ten article-wording and source claims verified; four partially disputed; three unverified):

- **Tenet 3 tension — closure rhetoric versus bidirectional interaction** (§4.2) → leg (f) of the target P1. **Partially disputed**: the Tenet 3 paragraph already says regulation "can run without that interface" and the positions register locates the interface at post-decoherence selection ([P-Q1](/positions/quantum-interface/#p-q1)); a clarity defect (the article never says its closure claim is about the classical control description), not a Map-level oscillation. The reading of [the-psychophysical-control-law](/topics/the-psychophysical-control-law/) ("commitment alone does not constitute specification") is accurate.
- **The op-amp realises one integral operation, not an end-to-end closed loop** (§1.5, improvement #5) → item (4) of the upgraded scope task: make the PID loop the end-to-end example, describe the op-amp as the operation-level floor. The "replace the bare op-amp" half is declined — the thermostat→op-amp exemplar migration is a converged stability note from deep review 2026-09-10, and ChatGPT itself offers the "if the op-amp remains" alternative.
- **"Sensing", "memory" and "decision" need operational definitions** (§1.7) → item (b) of the open P2 on `topics/bacterial-chemotaxis-and-minimal-biogenic-cognition`: functional memory and policy selection granted, deliberative or phenomenal decision a stronger claim chemotaxis does not establish.
- **The chemotaxis sibling has zero coverage of adaptation imprecision / finite methylation range** (§1.4, §5) → the open P2 on the sibling article, minted at processing. Verified: six terms all 0 hits. Neumann, Vladimirov, Krembel et al. (2014), *PLoS ONE*, is the boundary source, to be verified at the publisher before citing.
- **Man & Damasio made a stronger opponent than they are** (§1.10) → item (7) of the scope task. **Partially disputed**: the body already frames them with "propose … might thereby acquire"; only the rival-section header's "constitutively tied to feeling" overstates.
- **Seth & Tsakiris compressed too aggressively** (§1.11) — recorded. The 2026-09-10 quotation repair is acknowledged as genuine; the residue (their view is candidate mechanisms for aspects of embodied selfhood, not an identity claim) is absorbed by leg (g)'s at-strength engagement.
- **Reconcile with `concepts/control-theoretic-will`: which control variable does consciousness change?** (§5) — recorded, not minted. The mechanism debt belongs to [the-psychophysical-control-law](/topics/the-psychophysical-control-law/) and is already open there; leg (f) removes the apparent oscillation on this page.
- **Clarify the Tenets page: irreducibility does not imply absence of psychophysical regularities** (§4.1, improvement #22) — recorded for the tenets page's next review; leg (d) installs the distinction where it bites, in the target's Tenet 1 paragraph.
- **The 2026-09-10 deep review was framework-internal, not adversarial** (§4.4) — recorded; overlaps the standing NEEDS-HUMAN and this cycle's cluster 9.
- **Improvements #23–#29** (two-track reviews, claim ledger, theorem-to-implementation checkpoint, comparison class, falsifiers, dependency tracking, conclusion-loaded prompts) — not minted at processing; #25 and #26 flagged for an operator look. #24/#26/#30 are cluster 9.
- **Unverified**: Yi et al.'s "under most relevant conditions" wording (Europe PMC full text unavailable; the abstract already supports the point); the op-amp engineering details (textbook, not source-checked); Chalmers' organisational-invariance compatibility (not re-fetched; matches the Map's [functionalism](/concepts/functionalism/) treatment).

**Claude Opus 5** (fourteen article-wording and source claims verified; four partially disputed; two disputed; three unverified):

- **Calibration asymmetry — the closure acid dissolves the Map's own functional markers, "and no article books it"** (§2.3, verdict 5) → leg (h). **Partially disputed**: the cost *is* booked — `positions/perception-and-the-interface` grades the capability-division reading "consonant with the interface and probative of nothing" and [P-M1](/positions/methodology-and-calibration/#p-m1) forbids the tenet-to-evidence upgrade; the residue is that the target never says it shares that rule. One clause with a piped link to [cross-modal-capability-division](/apex/cross-modal-capability-division/).
- **Add Solms, Panksepp, Ginsburg & Jablonka to the rival roster** (Part 4, fix 6) — optional, **unverified**: the Solms and Ginsburg & Jablonka quotations are book text not fetched; verify at the publisher before any of them enters the article.
- **Citation apparatus RETAIN — "the cleanest citation layer of any article yet audited on this site"** (§2.1) — positive singleton, verified independently by ChatGPT's §1.13 ("I found no invented external paper … the Yi quotations are accurate"). See Divergence 1.
- **`concepts/control-theoretic-will`: "state the shared neutrality constraint in both"** (Part 4) — **disputed**: the target already states it ("the controller/plant description is metaphysically neutral…") and control-theoretic-will has a whole section, §Analogy, Model, and Ontology, doing the same. Nothing minted.
- **Interoception / psychophysical-control-law offload may be a false absence** (Part 4) — **disputed**: `topics/interoceptive-consciousness-and-the-interface` confronts Damasio head-on at L91–93; the control-law article is cited for the Map's own account, not for rival engagement. Laukkonen and Solms are absent there too (0/0) — one piped cross-link from the target, no duplicated engagement.
- **Verdict 8 — "neutral ground for a possibility proof — DELETE"** — **disputed**: 0/0 hits for either phrase; the article says the opposite. See Divergence 4.
- **Harden the blocking gate; it "should block publication"** (Part 5, item 4) — recorded. The gate at `project/evidential-status-discipline` L161 names Laukkonen 2025 as the default PP rival for the consciousness-and-time / meditation / phenomenology article class, not for valence/selfhood/learning as the reviewer states; whether to widen it is the operator's call.
- **Extract the rival-author firewall into a reusable template** (Part 5, item 5) — not a defect; the pattern already appears in the cross-modal apex and the positions register in the words the reviewer praises.
- **Unverified**: the Man & Damasio aims quotation (Nature IdP wall; inconsequential); Conant & Ashby (1970) abstract wording (the article does not cite it — Claude credits the article with *avoiding* the good-regulator equivocation, which is verified: 0 hits for Conant, Ashby, Francis, Wonham).

**Gemini 2.5 Pro** (six article-wording attributions and four sources verified; eight quotation-marked spans identified as paraphrases; five charges disputed):

- **"Tenet 5 asserts that mechanistic explanations leave no functional residual"** — **FALSE.** Tenet 5 is *Occam's Razor Has Limits*; the article's Tenet 5 paragraph "disciplines the conclusion in both directions" and expressly refuses to infer absence of experience from the elegance of a control explanation. The "no functional residue" sentence lives in the explanatory-closure paragraph and is bounded by the mirror reductio two paragraphs earlier. Reviewer error; nothing imported.
- **"Completely ignores the extensive recent literature on antithetic integral feedback"** — **disputed**: the Aoki rung names the "antithetic integral feedback controller". The trade-off literature is what is absent (cluster 2).
- **"Robustness breaks down in actual biological implementation"** — **disputed**: inverts Briat, Gupta & Khammash (2016). See Divergence 2.
- **IIT 4.0 "easily bypasses" the integrator floor** — **disputed as framed**; the agreed substance is cluster 7. Albantakis et al. (2023), *PLoS Comput Biol* 19(10) e1011465, is Crossref-exact.
- **Allostasis reduced to simple homeostasis** (weakness 5) — **disputed**: contradicted by the article's own allostasis/homeostasis distinction and its routing to the interoception article. Berntson & Khalsa (2021), *Trends Neurosci* 44(1), 17–28, is real and absent from the interoception article (0) — a citation option there, not a defect here.
- **Source hygiene against the prompt's own 2020–2025 rule**: Albantakis 2023, Berntson & Khalsa 2021 and Olsman et al. 2019 exact; Laukkonen 2025 confirmed via the Claude leg; "Filo, Hou & Khammash (2023)" a bioRxiv preprint (peer-reviewed form *Cell Systems* 2026, outside the window); "Filo et al., 2022" unresolvable; "Di Paolo & Mojica (2024) … 23, 1-25" three fields wrong; "non-equilibrium thermodynamics literature, 2024" unnamed and unverifiable. Three of five weaknesses carry a resolvable, on-topic source.
- **Eight quotation-marked spans are paraphrases, not article text** ("Op-Amp Reductio", "systematically designed and installed into molecular networks", "no functional residual", "domain-general primitive", and four more listed in the review's Verification Notes) — fair in sense; none may be quoted back as the article's wording.

## Divergences

Cases where reviewers reached opposite verdicts on the same feature. In each the verification record settles it, or shows the split is one of register rather than fact.

### 1. Is the empirical layer clean or obsolete? — Claude vs Gemini, with ChatGPT between

- **Claude Opus 5** (§2.1): "**Citation verdict: no fabrications, no mis-attributions, no verbatim errors.** … This is the cleanest citation layer of any article yet audited on this site."
- **Gemini 2.5 Pro** (§1): "The text suffers from a fatal combination of empirical obsolescence, aggressive theoretical gerrymandering, and a profound failure to engage with the contemporary (2020–2025) scientific literature".
- **ChatGPT 5.6 Pro** (§1.13): "Citation fidelity now mostly passes. Citation coverage and inferential discipline do not."
- **Resolved for ChatGPT's split verdict.** Metadata and quotation fidelity are clean by two independent passes. Coverage debt is real (cluster 2's trade-off literature; cluster 6's Laukkonen), but Gemini's "obsolescence" rests partly on a result it inverted (Divergence 2) and on a headline source that is a preprint. Claude and Gemini audited different layers and each generalised its layer to the whole.

### 2. Does antithetic integral feedback's robust perfect adaptation survive biological noise? — Gemini vs ChatGPT and Claude

- **Gemini 2.5 Pro** (§2): "while base antithetic integral controllers can theoretically achieve steady-state perfect adaptation in deterministic models, this robustness breaks down in actual biological implementation."
- **ChatGPT 5.6 Pro** (§1.6): "Aoki et al. genuinely designed and implemented a biomolecular integral-feedback architecture in *E. coli*. … Some guarantees concern population averages or long-time averages in stochastic systems, not exact trajectory-level control in every individual cell."
- **Claude Opus 5** (§2.2): "P1. Integral feedback control / robust perfect adaptation is a substrate-indifferent dynamical property (Yi et al.; Barkai & Leibler; Aoki et al.). *[Established, verbatim-sourced.]*"
- **Resolved against Gemini.** Briat, Gupta & Khammash (2016), *Cell Systems* 2(1), 15–26, is titled "Antithetic integral feedback ensures robust perfect adaptation in *noisy* biomolecular networks": RPA of the population mean holds in the stochastic setting; what the 2019+ literature adds is that variance and transient performance trade against it. ChatGPT's averaging qualifier is the correct statement of the same literature. Had Claude repeated Gemini's version, topic-overlap clustering would have scored convergence on an inverted result — the hazard this pass exists to catch.

### 3. Does the integrator-floor reductio stand? — Gemini vs Claude and ChatGPT

- **Gemini 2.5 Pro** (§5.1): "If the authors had engaged with IIT 4.0, their 'Integrator Floor' argument would have been thoroughly dismantled."
- **Claude Opus 5** (Part 3, verdict 2): "**The integrator-floor reductio … — RETAIN, but narrow.** Valid, but relabel it as what it is: a refutation of naive over-attribution, dialectically inert against functionalism proper."
- **ChatGPT 5.6 Pro** (§2): the controller examples give "∃x[I(x)∧¬C(x)]. That is sufficient to refute: ∀x[I(x)→C(x)]."
- **Resolved for Claude and ChatGPT — and the three agree on the fact.** All three hold that the op-amp is unfelt and that serious rivals predict as much. The split is whether that limits the reductio (Claude, ChatGPT) or refutes it (Gemini). A reductio that its opponents endorse is not dismantled; it is narrow. Cluster 7 records the shared substance; the target P1's legs (c) and (g) state the narrowing in prose.

### 4. What does the article claim about the biological rungs? — correlated over-reading, not convergence

- **Gemini 2.5 Pro** (§1): the authors "attempt to demonstrate that physicalist and functionalist accounts of consciousness are fundamentally flawed … thereby leaving the explanatory gap completely intact and validating a strict dualist framework".
- **Claude Opus 5** (Part 3, verdict 8): "Claim that the ladder's examples are neutral ground for a possibility proof — DELETE."
- **ChatGPT 5.6 Pro** (§2): "The article cannot classify those systems as demonstrated cases of competence without experience while also conceding that mechanistic completeness does not establish phenomenal absence."
- **Resolved against all three at the body, for all three at the surface.** The body says the synthetic-gene-circuit rung is "where the ladder leaves *uncontested* ground", that organisms' phenomenal status is "actively contested", and that physiological allostasis "is where the rival theories of feeling locate their claim"; the CBC paragraph concedes the reductio "bites at the circuit and not at the engineered cell". Three reviewers reading the title and the opening's "none of it is evidence" into the body is the sharpest illustration this cycle of why a navigation surface must not outrun its text — which is cluster 4, and why the title task exists. It is not evidence of a body defect, and no body sentence is deleted on its account.

### 5. Verdict severity — reject, revise, or retain-and-demote?

- **Gemini 2.5 Pro**: "Reject; the manuscript constructs a philosophically illicit framework by relying on empirically obsolete abstractions of biological control".
- **ChatGPT 5.6 Pro**: "Recommendation | Major revision rather than rejection" — with a replacement title and opening supplied.
- **Claude Opus 5**: "**Citation integrity: RETAIN.** … **Orthogonality-as-reusable-primitive: REVISE-HARD / DEMOTE-TO-COHERENCE-ONLY.**"
- **Not resolvable on disk — the shared floor is cluster 1.** Three briefs, three registers, one diagnosis: the article's narrow thesis (integral feedback is not sufficient for experience) is sound and its headline thesis (control competence is evidentially orthogonal to experience) is unearned. ChatGPT is the only reviewer to name what survives and write the sentence that states it; Claude is the only one to place the surviving claim on the Map's own evidence ladder. The P1's legs (a)–(h) are, jointly, those two moves.

## Method Notes

- **Every convergent finding was already on a task before this pass ran.** The three per-review passes wrote convergence addenda into the four open tasks as each leg landed (ChatGPT minted the P1, the scope P2 and the chemotaxis P2 and upgraded the title P3; Claude added legs (g)–(h) to the P1; Gemini added the Olsman/Briat sources and the autopoiesis instruction). This pass therefore deduplicated nothing and minted nothing; its work was one priority upgrade, three `Synthesis:` fields and the record above. That is the intended steady state for a single-article cycle, not a sign the synthesis was idle.
- **Priority discipline.** After this pass the target carries two P1s (argument; scope conditions) and one P2 (title). They touch overlapping sentences — the lead, the "installable on demand" sentence, `description:` — and each task already carries a coordinate-do-not-both-rewrite note. Suggested order: argument P1 first (it rewrites the lead and the closure paragraph), scope P1 second (its own note says to re-read the lead before editing), title P2 last so the `description:` touch matches the rewritten opening. The title task was deliberately not raised to P1: a third P1 on one 2,249-word file would race the other two for the same sentences.
- **Length.** The P1's legs (a)–(h) are budgeted at ≈2,400–2,450 body words against a 2,500 soft ceiling, and the scope task adds one clause plus up to two reference lines. If both land, the article may cross soft; both tasks say to cross and record it rather than trim the rival engagement. ChatGPT's #10 taxonomy and #11–#13 "serious sections" are the expansion-tier version of legs (c), (e) and (g) and are not budgeted.
- **Correlated-error checks applied.** (i) Gemini's Briat inversion had no sibling echo (Divergence 2). (ii) The body-level over-reading was shared by all three and was excluded as convergence because verification contradicts it (Divergence 4). (iii) Gemini's Tenet 5 misattribution is a reviewer error with no counterpart. (iv) Claude's "blocking gate FAILED" and Gemini's "derives the necessity of phenomenal experience" both overstate the same real gap; cluster 6 is scored on the gap, not on either overstatement.
- **Quotation hygiene.** Gemini placed eight paraphrases in quotation marks as article text; Claude's Laukkonen ellipsis reverses two spans and drops "seems to suggest"; Claude's "runs dark" is a paraphrase of "running dark". Every quotation in this file was re-checked against the review files as printed; every article phrase cited here is one the processing passes grep-confirmed. Anyone executing the P1 should quote Laukkonen from the preprint in source order with the hedge, and should grep the article before quoting any of Gemini's spans back.
- **Positive signal worth keeping.** Two legs independently certify the citation layer and the rival-author firewall, and Claude credits the article with avoiding the Conant & Ashby good-regulator equivocation (verified: the article never cites the theorem). The P1's calibration rewrite should not disturb those properties; the reference list needs one addition (Barrett & Simmons) and the scope task's two optional trade-off sources, nothing removed.