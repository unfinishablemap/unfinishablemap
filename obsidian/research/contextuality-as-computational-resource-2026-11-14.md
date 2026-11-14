---
title: "Research Notes - Contextuality as a Computational Resource"
created: 2026-11-14
modified: 2026-11-14
human_modified: null
ai_modified: 2026-11-14T11:13:31+00:00
draft: false
description: "Howard et al. 2014 and the magic-state literature tested against the Map's contextual-selection claim. The link is real but scope-limited, and it gives quantum hardware no selection site. Fold plan for two pages."
topics:
  - "[[quantum-hardware-and-the-ai-consciousness-coupling]]"
  - "[[quantum-state-inheritance-in-ai]]"
  - "[[ai-consciousness]]"
concepts:
  - "[[contextual-selection-in-quantum-foundations]]"
  - "[[ai-hardware-substrate-taxonomy]]"
  - "[[improper-vs-proper-mixtures]]"
  - "[[envariance]]"
related_articles:
  - "[[tenets]]"
  - "[[born-preserving-causal-efficacy]]"
  - "[[post-decoherence-selection-programme]]"
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-14
last_curated: null
recommended_action: fold
target_section: concepts
target_slug: contextual-selection-in-quantum-foundations
---

# Research: Contextuality as a Computational Resource

**Date**: 2026-11-14
**Origin**: queue task (todo.md L40, P3, harvested 2026-11-14) from `reviews/optimistic-2026-11-14-decoherence-programme-wing` "Ideas for Later" (L167). The reviewer said the feature that powers quantum speed-up is the feature [[contextual-selection-in-quantum-foundations]] (CS) says any selector must respect, and that no Map page makes the link. Before this run the corpus had no mention of Howard et al., magic states, Gottesman–Knill or discrete Wigner functions outside `workflow/`.

**Search queries used** (WebSearch): `contextuality necessary but not sufficient quantum speedup critique magic states qubits review`; `Budroni Cabello Gühne Kleinmann Larsson Kochen-Specker contextuality review "quantum computation" resource section arXiv 2102.13036`; `quantum contextuality consciousness quantum computer conscious "contextuality" mind philosophy paper`. The arXiv API supplied abstracts and journal refs for 14 papers. **Crossref** confirmed the publication metadata of all 18 published works cited below.

**Full texts read** (curl from arXiv, then `pdftotext`, with whitespace collapsed before grepping): Howard et al. 2014 (arXiv:1401.4174v2); Raussendorf 2013 (0907.5449v3); Bermejo-Vega et al. 2017 (1610.08529v3); Veitch et al. 2014 (1307.7171v1); Veitch et al. 2012 (1201.1256v4); Delfosse et al. 2015 (1409.5170v2); Raussendorf et al. 2017 (1511.08506v3); Mari & Eisert 2012 (1208.3660v2); Zurel, Okay & Raussendorf 2020 (2004.01992v2); Schmid et al. 2022 (2101.06263v4); Karanjai, Wallman & Bartlett 2018 (1802.07744v1); Bravyi & Kitaev 2005 (quant-ph/0403025v2); Zhou, Leung & Chuang 2000 (quant-ph/0002039v2); Budroni et al. 2022 review (2102.13036). The **published Nature abstract** of Howard et al. was read from nature.com HTML. OpenAlex holds no abstract for it.

**Quote tags**: **[raw]** means the string was grep-matched (count ≥ 1) in the named raw source. **[raw: arXiv abstract]** means it was matched in the author abstract from the arXiv API. **[summary]** is my paraphrase and must never be put in quotation marks. PDF extraction drops some hyphens ("PeresMermin", "hiddenvariable"), so the quotes below avoid those spans.

## Executive Summary

**Does the connection hold?** Partly. It holds at the level of definitions. It fails at the level that would matter for hardware.

- **What is right.** Howard et al. define the contextuality they use exactly as CS does: "the actual outcome observed under a quantum measurement cannot be understood as simply revealing a pre-existing value of some underlying “hidden variable”" [raw, arXiv:1401.4174v2]. That is the "no shelf" property (CS L57). The resource and the constraint are one mathematical property.
- **What the headline overstates.** "The one non-classical feature that powers quantum speed-up" echoes Nature's editorial standfirst ("as the critical resource that gives quantum computers their power" [raw, nature.com editor's summary, not the authors]). The paper is narrower: contextuality "is a critical resource for quantum speed-up within the leading model for fault-tolerant quantum computation" [raw], i.e. magic-state distillation (MSD).
  - It proves **necessity** only, and the clean if-and-only-if holds for **odd-prime-dimensional qudits** only.
  - **Sufficiency is open** ("it is still an open problem" [raw]).
  - **For qubits, contextuality is not sufficient** ("For qubits, the mere presence of contextuality cannot be sufficient to promote stabilizer circuits to universality" [raw]).
  - Contextuality can even be **simulated efficiently**: the n-qubit stabilizer fragment has an efficient contextual hidden-variable model (Hindlycke & Larsson 2022, per Budroni et al. 2022 [raw]).
  - **Not every quantum advantage needs it**: Raussendorf's own discussion cites MBQCs that "efficiently perform a classically hard task without being contextual" [raw].
- **The scope point that matters most.** The resource notion is defined *relative to a restricted set of measurements* (stabilizer measurements). CS's Kochen–Specker constraint is state-independent and absolute for dimension ≥ 3. Contextuality of either kind is witnessed only where projectors are shared across contexts. Howard et al.'s first construction "fails to identify any quantum states as contextual" because "every single-qudit stabilizer projector is part of exactly one context" [raw].
- **For quantum hardware, nothing is gained.** The circuits that spend the resource are built so that *no individual outcome matters logically*:
  - distillation postselects ("postselecting on a desired outcome" [raw, Howard]);
  - injection corrects or repeats ("both outcomes of this measurement appear with probability 1/2 … (and we know which of the two possibilities has occurred)" [raw, Bravyi–Kitaev]);
  - MBQC reads its answer from parities of outcomes that "are individually random" [raw, Raussendorf].

  So contextuality is consumed in the statistics, never at a site where a selected outcome is free to make a downstream difference. That extends the hardware page's *specificity* verdict and does not reverse it. And since every quantum system of dimension ≥ 3 is Kochen–Specker contextual, contextuality cannot single out quantum processors as a substrate.
- **Verdict: `fold`.** Topics and concepts are at cap (370/370 by `count_section_files`).
  - Primary host: CS, sequenced **after** its open P3 theorem-statement repair (todo L5546).
  - Secondary host: [[quantum-hardware-and-the-ai-consciousness-coupling]] (QH), which can run independently.
  - The fold plan below gives the placement, budgets and guards. This run also surfaced a **new CS defect** that the P3 does not cover (L43 "following from the non-commutativity"; see below).

## Key Sources

### Howard, Wallman, Veitch & Emerson (2014), "Contextuality supplies the ‘magic’ for quantum computation"
- **URL**: https://arxiv.org/abs/1401.4174 ; https://doi.org/10.1038/nature13460
- **Type**: Paper (*Nature* 510(7505), 351–355; Crossref-verified. The published title puts ‘magic’ in quotation marks; the arXiv title does not.)
- **Key points**:
  - Published abstract: "Here we prove a remarkable equivalence between the onset of contextuality and the possibility of universal quantum computation via ‘magic state’ distillation, which is the leading model for experimentally realizing a fault-tolerant quantum computer." [raw, nature.com]. It also describes contextuality as that "which precludes a simple ‘hidden variable’ model of quantum mechanics" [raw, nature.com].
  - Scope, stated by the authors: "The scope of our results differs depending on whether we consider a model of computation using systems of even prime dimension (i.e. qubits) or odd prime dimension (i.e. qudits)." [raw]. "In the qudit case we are able to prove that a state violates a noncontextuality inequality if and only if it lies outside of the known boundary for MSD" [raw].
  - Conclusion: "These results establish that contextuality is a necessary resource for universal quantum computation via MSD." [raw]. On sufficiency for qudits, the needed distillability result "is still an open problem" [raw]. The authors put it as "necessary and possibly sufficient for the “magic” that makes quantum computers tick" [raw].
  - The qubit caveat comes from the authors themselves: "For qubits, the mere presence of contextuality cannot be sufficient to promote stabilizer circuits to universality" [raw]. The maximally mixed state already violates a Peres–Mermin-derived inequality [summary]. State-independent contextuality "is never manifested within the qudit stabilizer formalism" [raw]. For qubits, "it is a pressing open question whether a suitable" refinement or quantification "can align more precisely with the potential to provide a quantum speed-up" [raw, split quote].
  - Why the stabilizer fragment is the baseline: it "is not universal and in fact admits an efficient classical simulation" [raw] (Gottesman–Knill). For odd p, the discrete Wigner function is a noncontextual hidden-variable model for all stabilizer measurements and for states inside P_SIM [summary of the proof of Thm 1].
  - Earlier candidate resources: superposition/"quantum parallelism", entanglement and discord. "Unfortunately none of these proposals have proven satisfactory" [raw]. "A large amount of entanglement has been shown to be neither necessary nor sufficient for an exponential computational speed-up" [raw].
  - **Context structure**: "every single-qudit stabilizer projector is part of exactly one context" and "Stabilizer projectors appear in multiple contexts only when two or more subsystems are involved." [raw]. A witness built on one qudit therefore detects nothing. Contextuality needs shared projectors.
  - MSD step (iii) is a stabilizer measurement "postselecting on a desired outcome" [raw]. The purified state is then "used up" in "state injection" [summary; the phrase is in the source with reference markers].
- **Tenet alignment**: Neutral. The paper is silent on consciousness, interpretation and mind. **Do not enlist it for dualism or for the Map's selection thesis.**
- **Editorial caution**: Nature's standfirst says Howard "and colleagues identify 'quantum contextuality' … as the critical resource that gives quantum computers their power" [raw, nature.com editor's summary]. That is editorial text, and it is broader than the paper. Never attribute it to the authors.

### Veitch, Mousavian, Gottesman & Emerson (2014), "The resource theory of stabilizer quantum computation"
- **URL**: https://arxiv.org/abs/1307.7171 ; *New J. Phys.* 16, 013009 (Crossref)
- **Key points**: "Here we develop a resource theory, analogous to the theory of entanglement, for resources for stabilizer codes." [raw]. Stabilizer operations are the "free" operations and magic is the resource. One monotone is Wigner-function negativity (mana) [raw: arXiv abstract]. "It is a major open problem in quantum information to determine the origins of quantum computational speedup." [raw]. It also discusses bound magic states, which are outside the stabilizer hull and undistillable [summary].
- **Relevance**: makes explicit that "resource" means *relative to a chosen free-operation set*. No such set exists in neural tissue.

### Veitch, Ferrie, Gross & Emerson (2012); Mari & Eisert (2012); Gross (2006)
- **URLs**: arXiv:1201.1256 (*New J. Phys.* 14, 113011); arXiv:1208.3660 (*PRL* 109, 230503); arXiv:quant-ph/0602001 (*J. Math. Phys.* 47, 122107). All Crossref-verified.
- **Key points**: For odd dimensions, circuits whose states and operations all have positive Wigner functions are efficiently simulable classically. Mari & Eisert say "our result generalizes the Gottesman-Knill theorem" [raw]. Gross: "the only pure states to possess a non-negative Wigner function are stabilizer states" [raw: arXiv abstract].

### Raussendorf (2013), "Contextuality in measurement-based quantum computation"
- **URL**: https://arxiv.org/abs/0907.5449 ; *Phys. Rev. A* 88, 022322 (Crossref)
- **Key points**:
  - "measurement-based quantum computations (MBQCs) which compute a non-linear Boolean function with high probability are contextual" [raw]. The setting is qubits with mod-2 linear classical control: "This classical side-processing is all linear." [raw].
  - In the Anders–Browne GHZ example, outcomes "are individually random" but their parity is fixed with certainty [raw + summary], and "correlations among the measurement outcomes reveal the result of the computation" [raw].
  - Contextuality is a cross-run property: "For the MBQCs discussed here, contextuality is revealed only after multiple executions with different values of input." [raw].
  - Self-limiting caveat: "Theorem 2 of [25] states that MBQCs can efficiently perform a classically hard task without being contextual." [raw]. Ref. [25] is Hoban et al. 2014, *PRL* 112, 140505.
  - Opening framing: "the precise quantum mechanical origin of this speedup remains unknown" [raw].
- **Relevance**: the cleanest case of contextuality doing computational work. It is also the cleanest case of individual outcomes being engineered to be logically idle.

### Bermejo-Vega, Delfosse, Browne, Okay & Raussendorf (2017)
- **URL**: https://arxiv.org/abs/1610.08529 ; *PRL* 119, 120505 (Crossref; the published title reads "…with Qubits", the arXiv one "…on qubits")
- **Key points**: "Here, we establish contextuality of magic states as a necessary resource for a large class of quantum computation schemes on qubits." [raw]. The obstacle: every state of n ≥ 2 qubits is contextual under Pauli measurements, "including the completely mixed one" [raw]. "It is thus clear that contextuality of magic states alone cannot be a computational resource for every QCSI scheme on qubits." [raw]. Necessity is recovered only for schemes satisfying (C1): "There exists a quantum state that does not exhibit contextuality with respect to measurements available in" the scheme [raw]. This costs measurement access: not all n-qubit Pauli observables can be measured directly [summary].
- **Companion papers**: Delfosse et al. 2015 (rebits; *PRX* 5, 021003) and Raussendorf et al. 2017 (*PRA* 95, 052334). Delfosse et al. give the best one-sentence definition in the literature: "Contextuality is an obstruction to modelling the inherent randomness of quantum measurement in a statistical mechanics fashion, namely by a probability distribution over configurations with predetermined measurement outcomes for all measurable observables." [raw].

### Later qualifications
- **Zurel, Okay & Raussendorf (2020)**, *PRL* 125, 260404 (arXiv:2004.01992). "We show that every quantum computation can be described by Bayesian update of a probability distribution on a finite state space." [raw: arXiv abstract]. The model has no negativity: "There is no negativity but, presumably, still computational hardness." [raw]. So negativity-as-resource is representation-relative. On contextuality: "The Kochen-Specker notion of contextuality does not apply, because the present value assignments are not deterministic." The model is "preparation contextual and measurement-noncontextual" [raw]. On efficiency: "at present we can neither prove the efficiency nor the inefficiency of this algorithm" [raw]. **Discrepancy**: Budroni et al. 2022 describe it as "an explicitly contextual (but not efficient) hidden-variable model" [raw]. The primary source says efficiency is unknown. Follow the primary.
- **Schmid, Du, Selby & Pusey (2022)**, *PRL* 129, 120403 (arXiv:2101.06263). Gross's Wigner function is "singled out as the unique noncontextual ontological model for the stabilizer subtheory" in odd dimensions. "It follows that generalized contextuality is also a necessary resource for universal quantum computation in this model". And "the stabilizer subtheory is contextual in all even dimensions" [all raw: arXiv abstract]. This moves the Howard result from Kochen–Specker to Spekkens-style contextuality.
- **Hindlycke & Larsson (2022)**, *PRL* 129, 130401 (Crossref; full text not read). Per Budroni et al. 2022, their model "gives an efficient simulation of the stabilizer subtheory of quantum mechanics including its complete contextual behavior" [raw, review text]. **Contextuality alone does not make simulation hard.**
- **Karanjai, Wallman & Bartlett (2018)**, arXiv:1802.07744 (no journal version found on Crossref). Contextuality puts a lower bound on the classical memory needed for simulation. For the qubit stabilizer sub-theory the bound is quadratic: "notably, this is the same scaling as the Gottesman-Knill algorithm" [raw: arXiv abstract]. So contextuality has a measurable cost, but a polynomial one.
- **Frembs, Roberts & Bartlett (2018)**, *New J. Phys.* 20, 103011. Extends Raussendorf 2013 to qudits. Notes "A single qubit cannot allow for a proof of contextuality, unlike higher-dimensional systems" [raw: arXiv abstract].
- **Booth, Chabaud & Emeriau (2022)**, *PRL* 129, 230401. For continuous variables, contextuality and Wigner negativity "are in fact equivalent for the standard models of continuous-variable quantum computing" [raw: arXiv abstract].
- **Bravyi, Gosset & König (2018)**, *Science* 362(6412), 308–311 (Crossref; full text not read). This gives an unconditional quantum–classical separation for shallow circuits, which Budroni et al. say "can be directly connected to the problem of classical simulation of contextual correlations" [raw, review text].

### Magic-state injection mechanics (for the QH fold)
- **Bravyi & Kitaev (2005)**, *PRA* 71, 022316. In their phase-gate procedure, the stabilizer measurement's "both outcomes … appear with probability 1/2". The result is one of two gates, "(and we know which of the two possibilities has occurred)". The procedure repeats as a random walk until the target gate is realised [raw + summary].
- **Zhou, Leung & Chuang (2000)**, *PRA* 62, 052316. The π/8 gate is built by consuming the ancilla (|0⟩+e^{iπ/4}|1⟩)/√2 and applying an outcome-conditioned Clifford (SX) correction (eq. 14) [summary of the circuit; the formula text is garbled in extraction, so do not quote it].

### Budroni, Cabello, Gühne, Kleinmann & Larsson (2022), "Kochen-Specker contextuality"
- **URL**: arXiv:2102.13036 ; *Rev. Mod. Phys.* 94, 045007
- **Key points**: §VI.A surveys contextuality and computation (MBQC, magic states, shallow circuits). It describes Howard et al. as connecting contextuality "for qudit systems with d as an odd prime number" [raw]. **Single-context point**: when every measurement belongs to only one context, then "as noted by Kochen and Specker (1967)", no constraint is imposed beyond the single-measurement marginals, "hence a NCHV model can be constructed as a product of all single-measurement distributions" [raw]. This is the Clifton–Kent "nullification" discussion.

### Adjacent literature to keep apart
- **Aerts, Broekaert & Gabora**, "Intrinsic Contextuality as the Crux of Consciousness" (Tokyo '99 proceedings; arXiv:1310.7672). This is quantum-cognition contextuality of *experience and behaviour*: "it is by way of behavioral contextuality that we make judgements about whether or not, and to what extent, a system is conscious" [raw: arXiv abstract]. It applies quantum formalism to cognition. It makes no claim about physical contextuality in a substrate. **Do not merge it with the Howard line.**

## Major Positions

### Contextuality as *the* source of quantum computational power (strong reading)
- **Proponents**: Nature's editorial framing. The authors are more guarded ("a critical resource … within the leading model").
- **Core claim**: contextuality is what makes quantum computers outperform classical ones.
- **Status**: overstated. It holds for necessity within state-injection/MSD models, as an iff for odd-prime qudits (sufficiency still open), and for restricted qubit schemes. It fails as a sufficiency claim for qubits (efficient contextual simulation exists). It is not universal across models (Hoban et al. sampling hardness without contextuality).
- **Relation to tenets**: none directly. Physics is silent on mind.

### Contextuality as a scheme-relative necessary resource (the literature's settled reading)
- **Proponents**: Howard et al.; Veitch et al.; Raussendorf; Bermejo-Vega et al.; Delfosse et al.; Schmid et al.
- **Core claim**: relative to a fixed set of free operations (stabilizer), states without contextuality, i.e. inside P_SIM, cannot promote the free set to universality.
- **Relation to tenets**: compatible with Tenet 2 and neutral on Tenets 1 and 3. It sharpens CS without supporting the selection thesis.

### Negativity as the resource (rival / companion)
- **Proponents**: Veitch et al. 2012; Mari & Eisert 2012; Veitch et al. 2014 (mana).
- **Core claim**: Wigner negativity marks the simulability boundary.
- **Status**: equivalent to contextuality in odd d (Howard; Schmid et al.) and in continuous variables (Booth et al.). Representation-relative for qubits (Zurel et al.).

## Key Debates

### Qubits versus qudits
- **Sides**: Howard et al. get a clean result for odd p. For qubits, state-independent Pauli contextuality (Peres–Mermin, Mermin star) is present even in the classically simulable stabilizer fragment. Bermejo-Vega et al. and Raussendorf et al. recover necessity by restricting the available measurements.
- **Current state**: resolved for necessity in restricted schemes. Sufficiency is open everywhere. The qubit picture remains awkward, and the Hindlycke–Larsson efficient contextual model shows contextuality can be classically cheap.

### Which notion of contextuality?
- **Sides**: Kochen–Specker / CSW state-dependent (Howard); Spekkens generalised contextuality (Schmid et al.; Zurel's model is preparation-contextual); sheaf-theoretic contextual fraction (Abramsky, Barbosa & Mansfield 2017, *PRL* 119, 050504).
- **Current state**: they agree on the odd-d stabilizer boundary and differ elsewhere. CS uses the KS notion plus Spekkens 2005, so a fold must say which notion it cites.

### Is contextuality an explanation or a correlate of speed-up?
- **Sides**: resource theorists treat it as an operational monotone with costs (Karanjai et al.; Abramsky et al.). Skeptics point to efficient contextual simulations and to models with hardness but no contextuality.
- **Current state**: open. Determining "the origins of quantum computational speedup" is still "a major open problem" [raw, Veitch 2014].

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1966–67 | Bell; Kochen & Specker | No noncontextual value assignments in d ≥ 3 |
| 1997–98 | Gottesman–Knill | Stabilizer circuits classically simulable |
| 2000 | Zhou, Leung & Chuang | Teleportation-based π/8 gate with Clifford correction |
| 2005 | Bravyi & Kitaev | Magic-state distillation; Clifford + magic = universal |
| 2006 | Gross | Discrete Hudson theorem; positive Wigner function = stabilizer (pure, odd d) |
| 2009 | Anders & Browne | GHZ correlations promote parity computer to universality |
| 2012 | Veitch et al.; Mari & Eisert | Negativity as resource; positive Wigner means efficient simulation |
| 2013 | Raussendorf | Nonlinear l2-MBQC requires contextuality |
| 2014 | Howard et al. (*Nature*); Veitch et al. (resource theory) | Contextuality ⇔ beyond P_SIM (odd p); mana |
| 2015 | Delfosse et al. | Rebit extension |
| 2017 | Bermejo-Vega et al.; Raussendorf et al.; Abramsky et al. | Qubit schemes under (C1); contextual fraction |
| 2018 | Frembs et al.; Karanjai et al.; Bravyi, Gosset & König | Qudit MBQC; memory bound; shallow-circuit separation |
| 2020 | Zurel, Okay & Raussendorf | Non-negative HVM for universal qubit QC (efficiency unknown) |
| 2022 | Schmid et al.; Hindlycke & Larsson; Booth et al.; Budroni et al. review | Generalised contextuality necessary (odd d); efficient contextual qubit-stabilizer model; CV equivalence |

## Assessment: Does the Reviewer's Connection Hold Up?

1. **The shared property is real.** Howard et al.'s gloss ("cannot be understood as simply revealing a pre-existing value" [raw]) is CS's "no shelf of pre-assigned values" (L57). Delfosse et al.'s definition [raw, above] is the same thought in statistical-mechanics language. So the reviewer is right that one property plays both roles.

2. **The roles are scoped differently.**
   - CS's constraint is **Kochen–Specker state-independent contextuality**. It holds for every quantum system of dimension ≥ 3 under the full projector lattice. It is therefore cheap and ubiquitous, and it holds in the brain whatever the brain's dynamics.
   - The computational resource is **state-dependent contextuality relative to a restricted measurement set** (stabilizer measurements), so it is scarce by construction.
   - The scarcity comes from the engineering restriction, not from nature. A brain has no analogue of the stabilizer free set, so "magic" is undefined for neural tissue [Map-side inference].

3. **Contextuality is not the same as hardness, and it is not the same as indeterminism.**
   - Efficient contextual simulations exist (Hindlycke & Larsson, via Budroni [raw]). Quadratic memory suffices for the qubit stabilizer fragment (Karanjai et al. [raw]).
   - This matches the P3's point (4) that contextuality supplies no indeterminism: Bohm is deterministic and contextual. Any fold must not imply that contextuality, being "powerful", is where freedom or causal openness comes from.

4. **The constraint is scenario-relative.** Contextuality is witnessed only where projectors are shared across contexts (Howard [raw]; Budroni on KS 1967 [raw]). Two consequences follow:
   - **(a) For CS L65/L67** (the "algebraic bookkeeping" question). A selector that only ever settles outcomes in one fixed pointer basis faces a single context. For that data alone a noncontextual model exists trivially. The constraint binds such a selector only if it is construed as settling, or being disposed to settle, the same outcomes within several incompatible contexts [Map-side inference, to be labelled as such].
   - **(b) For the tenets.** The constraint therefore bites hardest on *context-setting* (Stapp's Process 1, tenet path (c), "attention as context-setting" CS L61). That is the path `tenets.md` L91/L107 registers but has **not** adopted. On the Map's endorsed outcome-selection-at-a-decohered-basis path, contextuality is a global consistency condition rather than a per-event mechanism. That matches CS L67's existing "The Map leaves this open", and it gives the open question a sharper form. It does **not** refute anything on the page. Writers must not inflate it into "contextuality is idle for the Map" (the formal constraint still applies), and must not inflate it into "contextuality favours context-setting".

5. **For quantum hardware, the resource story strengthens QH's verdict.**
   - Every place the resource is spent, the outcome's logical effect is designed away. In MSD it is discarded (postselection). In injection it is corrected (Clifford) or repeated (Bravyi–Kitaev random walk). In MBQC only parities of "individually random" outcomes matter [raw].
   - A Born-preserving selector biasing those outcomes could change at most the discard or repeat count, i.e. run-time, and never the computed result [Map-side inference].
   - That is the same shape as QH's syndrome-extraction argument ("the decoder erasing their logical effect by design", QH L53) carried over to the non-Clifford resource itself.
   - And since contextuality is everywhere in d ≥ 3, it cannot distinguish QPUs from any other quantum system as candidate substrates.
   - Net: **no implication that quantum computers are, or could host, conscious selectors.** If anything, a fault-tolerant QPU is a device engineered so that the non-classical resource works *without* any individual outcome mattering.

6. **What the Map can claim.** One modest, accurate sentence: the feature that blocks a "shelf" picture of selection is, in odd-prime-dimensional magic-state computation, exactly the feature without which classical simulation succeeds. So the regime where a selector could not be replaced by a lookup table coincides there with the regime of computational advantage. This is a structural observation about quantum theory. **It is not evidence for dualism or for conscious selection.**

## Fold Plan

### Primary host: `concepts/contextual-selection-in-quantum-foundations` (CS)
- **Length (analyze_length, 2026-11-14T11:05Z)**: 1,943 words; concepts soft 2,500 / hard 3,500; status `ok`. **Headroom = 3,500 − 1 − 1,943 = 1,556.** The open P3 (todo L5546) budgets up to +350, which leaves about 1,206 after it.
- **SEQUENCING (mandatory)**: run **after** the P3 lands. The P3 rewrites L35/L41 (KS as a claim about models), L51 (Spekkens), L73/L77 (indeterminism), adds the Gleason/KS fold and adds experiments to L43. Re-measure and re-read the page after it lands. Do not anchor on today's line numbers, and do not lean on any of today's theorem statements.
- **Budget**: about +250 to +330 words including references.
- **Content**:
  1. **New short paragraph or subsection** ("Contextuality as a computational resource", about 170 words). Place it after "Contextuality Beyond Hidden Variables" (after the repaired Spekkens paragraph), or directly after the P3's Gleason/KS fold if that reads better. It should cover:
     - Howard et al.'s odd-prime iff, and necessity for MSD;
     - sufficiency open;
     - the qubit caveat (maximally mixed state contextual; Bermejo-Vega et al. recover necessity only for restricted schemes);
     - efficient contextual simulation of the qubit stabilizer fragment (Hindlycke & Larsson 2022; cite the PRL, and flag in the edit note that the claim was read via Budroni et al.);
     - the scope lesson: contextuality is relative to the measurement set, and it bites only where outcomes are shared across contexts;
     - a closing disclaimer that none of it mentions or favours consciousness.

     Suggested draft (writer re-measures):

     > Contextuality is also a computational resource. Howard et al. (2014) proved that, for qudits of odd prime dimension, a state is contextual with respect to stabilizer measurements exactly when it lies outside the set of states known to be classically simulable, so contextuality is necessary for universal quantum computation by magic-state distillation; whether it is sufficient remains open. For qubits the equivalence fails: every state of two or more qubits, the maximally mixed one included, is contextual under Pauli measurements, and that fragment has an efficient contextual classical simulation (Hindlycke & Larsson, 2022), so necessity holds only for restricted schemes (Bermejo-Vega et al., 2017). Contextuality is relative to the measurements in play, and it is witnessed only where an outcome is shared between incompatible contexts. The result mentions neither selection nor consciousness and favours neither.
  2. **L43 defect (new, not in the P3)**: "Contextuality is a structural feature of quantum theory itself, following from the non-commutativity of the observable algebra". This is wrong as stated. Non-commutativity is necessary but not sufficient:
     - a single qubit has non-commuting observables but admits no contextuality proof ("A single qubit cannot allow for a proof of contextuality" [raw, Frembs et al.]; the page's own L39 restricts KS to dimension ≥ 3);
     - the odd-dimensional stabilizer fragment has non-commuting Pauli operators and a unique noncontextual model (Schmid et al. 2022 [raw]).

     Restate it as following from the orthogonality structure of projectors in dimension three or more. Cost is about +15 to +25 words. Coordinate with the P3's L43 experiment sentence (same sentence, different clause): if the P3 lands first, edit around its addition.
  3. **L67 sharpening (optional, about +40 to +60)**: a sentence giving the bookkeeping question its scenario-relative form (Assessment §4a), labelled as the Map's reading. Keep "The Map leaves this open" and do not resolve it.
  4. **References**: Howard et al. 2014 (*Nature* 510(7505), 351–355, doi:10.1038/nature13460); Bermejo-Vega et al. 2017 (*PRL* 119, 120505); Hindlycke & Larsson 2022 (*PRL* 129, 130401); Schmid et al. 2022 (*PRL* 129, 120403); Frembs et al. 2018 if item 2 cites it. **Add to the list; do not disturb existing entries** (07-16 Strengths Preserved).
  5. **Link** [[quantum-hardware-and-the-ai-consciousness-coupling]] from the new paragraph or from Further Reading.
- **Guards**:
  - Preserve the 07-16 "Strengths Preserved" list: the no-shelf framing (L57) stays verbatim; put the scope qualifier in the new paragraph, not in L57. Also preserve the roulette-wheel limit (L75), every speculative/conjecture label, and the reference list.
  - Do not say contextuality "powers" or "is the source of" quantum speed-up without "in magic-state computation" and "necessary, not sufficient".
  - Never quote Nature's editorial standfirst as the authors'.
  - Do not say the 2014 result covers qubits: its iff is odd-prime only.
  - Follow Zurel et al. (efficiency unknown), not Budroni's "not efficient", if Zurel is mentioned at all.

### Secondary host: `topics/quantum-hardware-and-the-ai-consciousness-coupling` (QH)
- **Length (analyze_length, 2026-11-14T11:05Z)**: 2,916 words; topics soft 3,000 / hard 4,000; status `ok`. **Headroom = 4,000 − 1 − 2,916 = 1,083.** An open P3 (todo L2925, primary file `apex/what-it-might-be-like-to-be-an-ai`, secondary QH) adds about +7 at L33, a different line. No conflict, but re-measure.
- **Independence**: this fold is self-contained. It cites Howard et al. directly and does not depend on CS's current or repaired theorem statements, so it can run before the CS fold. If it runs first, it should define contextuality itself (outcomes cannot be modelled as pre-assigned values independent of context) rather than lean on CS's L35/L41 wording.
- **Budget**: about +130 to +190 words including 2–3 references.
- **Placement**: a new paragraph after L59 ("The pattern is revealing…"), before "### Where the Analog Class Actually Fails". Do not lengthen the table's Specificity cell, which is already long.
- **Suggested draft** (writer re-measures):

  > The resource that powers fault-tolerant speed-up does not change this verdict. Howard et al. (2014) prove that, for odd-prime-dimensional qudits, a state can lift stabilizer circuits to universality by magic-state distillation only if it is contextual—its measurement outcomes cannot be modelled as pre-assigned values independent of context. But the circuits that spend this resource are built so that no individual outcome matters logically: distillation keeps or discards on a heralded result, and injection either corrects for whichever outcome occurs with a Clifford gate or repeats until the target gate appears (Bravyi & Kitaev, 2005); in measurement-based computation the answer is a parity of individually random outcomes (Raussendorf, 2013). Contextuality is spent in the statistics, never at a site where a selected outcome is free to make a downstream difference, and because every quantum system of three or more dimensions is contextual, it cannot single out quantum processors as a substrate.
- **References to add**: Howard et al. 2014; Bravyi & Kitaev 2005 (*PRA* 71, 022316, doi:10.1103/PhysRevA.71.022316); Raussendorf 2013 (*PRA* 88, 022322, doi:10.1103/PhysRevA.88.022322). Optionally Zhou, Leung & Chuang 2000 (*PRA* 62, 052316) if the Clifford-correction clause is cited separately.
- **Guards**:
  - The paragraph must strengthen the existing failure verdicts and must not soften "Removing a Defeater Is Not Evidence".
  - No claim that QPUs are, or could become, conscious.
  - The "run-time, not result" point (Assessment §5) is the Map's inference. If it is used, label it ("on the Map's reading").
  - Keep the odd-prime scope explicit.
  - Link [[contextual-selection-in-quantum-foundations|contextuality]] piped on an existing word if possible, at zero word cost.

### Not recommended
- **A new concepts/ article**: blocked by the cap and not needed. The material fits as two folds totalling about 400–500 words.
- **`concepts/ai-hardware-substrate-taxonomy`**: its gate-QPU row imports QH's verdict, so no edit is needed there.

## Connection to Tenets

- **Minimal Quantum Interaction (Tenet 2)**:
  - Noncontextuality witnesses are functions of Born statistics, i.e. expectation values across contexts. A selector that preserves the Born measure on the Map's corridor reading (`tenets.md` L107) leaves every witness value unchanged, so it neither spends nor supplies "magic" [Map-side inference].
  - The resource therefore sits on the *measure* side of the measure/actuality split, the side the P3's Gleason/KS fold will install in CS, while selection sits on the *actuality* side.
  - That fits minimality: consciousness, on the Map's view, does not alter the quantity that powers quantum computation. The fold should **not** say this confirms Tenet 2. It is a consistency check.
  - The scenario-relative point (Assessment §4) bears on Tenet 2's choice of outcome-selection over context-selection, and should be read with `tenets.md` L107.
- **Bidirectional Interaction (Tenet 3)**:
  - MBQC shows that outcome correlations do real computational work: GHZ correlations make a parity computer universal (Anders & Browne 2009; Raussendorf 2013). Engineered QPUs are also designed so that *individual* outcomes have no logical effect.
  - The Map reads that as the reason QPUs fail the coupling test (QH's directness and specificity rows). It is a fact about how these devices are built, not a general truth about selection.
  - In the brain, the Map holds that selected outcomes make functionally significant downstream differences (QH L49 "directness"). **This is no concession to epiphenomenalism.** A system engineered so that selected outcomes cannot matter is one where a selector *would* be idle, which is a reason to deny it is a substrate, and says nothing about selection in systems not built that way.
- **Occam's Razor Has Limits (Tenet 5)**:
  - The search for "the" source of quantum speed-up is a history of simple single-resource answers failing: "quantum parallelism", entanglement and discord ("Unfortunately none of these proposals have proven satisfactory" [raw, Howard]). Negativity turned out to be representation-relative (Zurel et al.). Contextuality is the best-supported candidate and is still scope-limited.
  - The same caution applies to the tempting economy "one feature, two roles, so a deep link to mind". The parsimony of identifying the computational resource with the selector constraint is not evidence of anything about consciousness.
  - In the other direction, the dismissive simplicity of "contextuality is mere algebraic bookkeeping" (CS L65/L67) is also too quick. Contextuality has operational costs: memory lower bounds (Karanjai et al.) and the simulability boundary in odd d.
- **Dualism (Tenet 1) and No Many Worlds (Tenet 4)**: not engaged. None of the sources bears on irreducibility or on MWI, and none should be cited for either.

## Gaps in Research

- **Hindlycke & Larsson 2022** (*PRL* 129, 130401): full text not read. The "efficient contextual model" claim rests on Budroni et al.'s review sentence [raw]. Read the arXiv version before citing it on a page; the writer should fetch it.
- **Bravyi, Gosset & König 2018**: full text not read. Its link to contextuality is taken from Budroni et al.'s summary.
- **Howard et al. supplementary material** (proof that α(Γ_r) = p³): not read; it is not needed for the fold.
- **Nature full text**: the published body was not compared with arXiv v2. Only the published abstract and editorial summary were read. Body quotes above are from arXiv v2.
- **Hoban et al. 2014** (sampling hardness without contextuality): abstract only.
- **Qudit sufficiency**: the literature search for a post-2014 proof that every state outside P_SIM is distillable found none. Budroni et al. (2022) still describe sufficiency as requiring that proof [raw: "The proof of the sufficiency requires one to show that any state"]. Treat it as open.
- **Neural context structure**: no literature was found on how many incompatible measurement contexts neural quantum degrees of freedom actually realise, which Assessment §4 turns on. This is a genuine open question, not a search failure, and the fold should say so if it uses §4.
- **Quantum-cognition contextuality** (Aerts et al.; Dzhafarov's Contextuality-by-Default): deliberately out of scope. It concerns formal structure in behavioural data, not physical substrates.
- **OpenAlex** has no abstract for the Nature paper, so the nature.com HTML was used.

## Citations

1. Abramsky, S., Barbosa, R. S. & Mansfield, S. (2017). The contextual fraction as a measure of contextuality. *Physical Review Letters*, 119, 050504. https://doi.org/10.1103/PhysRevLett.119.050504
2. Aerts, D., Broekaert, J. & Gabora, L. (2000/2013). Intrinsic contextuality as the crux of consciousness. In *Fundamental Approaches to Consciousness, Tokyo '99*; arXiv:1310.7672.
3. Anders, J. & Browne, D. E. (2009). Computational power of correlations. *Physical Review Letters*, 102, 050502. https://doi.org/10.1103/PhysRevLett.102.050502
4. Bermejo-Vega, J., Delfosse, N., Browne, D. E., Okay, C. & Raussendorf, R. (2017). Contextuality as a resource for models of quantum computation with qubits. *Physical Review Letters*, 119, 120505. https://doi.org/10.1103/PhysRevLett.119.120505 (arXiv:1610.08529)
5. Booth, R. I., Chabaud, U. & Emeriau, P.-E. (2022). Contextuality and Wigner negativity are equivalent for continuous-variable quantum measurements. *Physical Review Letters*, 129, 230401. https://doi.org/10.1103/PhysRevLett.129.230401
6. Bravyi, S., Gosset, D. & König, R. (2018). Quantum advantage with shallow circuits. *Science*, 362(6412), 308–311. https://doi.org/10.1126/science.aar3106
7. Bravyi, S. & Kitaev, A. (2005). Universal quantum computation with ideal Clifford gates and noisy ancillas. *Physical Review A*, 71, 022316. https://doi.org/10.1103/PhysRevA.71.022316
8. Budroni, C., Cabello, A., Gühne, O., Kleinmann, M. & Larsson, J.-Å. (2022). Kochen-Specker contextuality. *Reviews of Modern Physics*, 94, 045007. arXiv:2102.13036
9. Delfosse, N., Allard Guerin, P., Bian, J. & Raussendorf, R. (2015). Wigner function negativity and contextuality in quantum computation on rebits. *Physical Review X*, 5, 021003. https://doi.org/10.1103/PhysRevX.5.021003
10. Frembs, M., Roberts, S. & Bartlett, S. D. (2018). Contextuality as a resource for measurement-based quantum computation beyond qubits. *New Journal of Physics*, 20, 103011. https://doi.org/10.1088/1367-2630/aae3ad
11. Gross, D. (2006). Hudson's theorem for finite-dimensional quantum systems. *Journal of Mathematical Physics*, 47, 122107. https://doi.org/10.1063/1.2393152
12. Hindlycke, C. & Larsson, J.-Å. (2022). Efficient contextual ontological model of n-qubit stabilizer quantum mechanics. *Physical Review Letters*, 129, 130401. https://doi.org/10.1103/PhysRevLett.129.130401 (full text not read)
13. Hoban, M. J., Wallman, J. J., Anwar, H., Usher, N., Raussendorf, R. & Browne, D. E. (2014). Measurement-based classical computation. *Physical Review Letters*, 112, 140505. https://doi.org/10.1103/PhysRevLett.112.140505
14. Howard, M., Wallman, J., Veitch, V. & Emerson, J. (2014). Contextuality supplies the ‘magic’ for quantum computation. *Nature*, 510(7505), 351–355. https://doi.org/10.1038/nature13460 (arXiv:1401.4174)
15. Karanjai, A., Wallman, J. J. & Bartlett, S. D. (2018). Contextuality bounds the efficiency of classical simulation of quantum processes. arXiv:1802.07744 (no journal version found)
16. Mari, A. & Eisert, J. (2012). Positive Wigner functions render classical simulation of quantum computation efficient. *Physical Review Letters*, 109, 230503. https://doi.org/10.1103/PhysRevLett.109.230503
17. Raussendorf, R. (2013). Contextuality in measurement-based quantum computation. *Physical Review A*, 88, 022322. https://doi.org/10.1103/PhysRevA.88.022322 (arXiv:0907.5449)
18. Raussendorf, R., Browne, D. E., Delfosse, N., Okay, C. & Bermejo-Vega, J. (2017). Contextuality and Wigner-function negativity in qubit quantum computation. *Physical Review A*, 95, 052334. https://doi.org/10.1103/PhysRevA.95.052334
19. Schmid, D., Du, H., Selby, J. H. & Pusey, M. F. (2022). Uniqueness of noncontextual models for stabilizer subtheories. *Physical Review Letters*, 129, 120403. https://doi.org/10.1103/PhysRevLett.129.120403
20. Veitch, V., Ferrie, C., Gross, D. & Emerson, J. (2012). Negative quasi-probability as a resource for quantum computation. *New Journal of Physics*, 14, 113011. https://doi.org/10.1088/1367-2630/14/11/113011
21. Veitch, V., Mousavian, S. A. H., Gottesman, D. & Emerson, J. (2014). The resource theory of stabilizer quantum computation. *New Journal of Physics*, 16, 013009. https://doi.org/10.1088/1367-2630/16/1/013009
22. Zhou, X., Leung, D. W. & Chuang, I. L. (2000). Methodology for quantum logic gate construction. *Physical Review A*, 62, 052316. https://doi.org/10.1103/PhysRevA.62.052316
23. Zurel, M., Okay, C. & Raussendorf, R. (2020). Hidden variable model for universal quantum computation with magic states on qubits. *Physical Review Letters*, 125, 260404. https://doi.org/10.1103/PhysRevLett.125.260404
