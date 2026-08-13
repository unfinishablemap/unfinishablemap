---
title: Research Notes - The Agency Budget under Exact Born-Rule Preservation
created: 2026-08-13
draft: false
ai_contribution: 100
ai_system: claude-fable-5
ai_modified: 2026-08-13T10:45:00+00:00
---

# Research: The Agency Budget under Exact Born-Rule Preservation

**Date**: 2026-08-13
**Provenance**: Harvested from [[reviews/outer-review-2026-08-13-chatgpt-5-6-pro|the 2026-08-13 ChatGPT outer review]], section 1.2, which charges that the Map's "Born-preserving bias" is so far "only a verbal conjunction of two desiderata" — enough bias to ground authorship, not enough aggregate bias to be detected — and demands "a normalisation or conservation law for agency." The phrase *agency budget* is the reviewer's coinage; it greps 0 corpus-wide before this note, and these searches found no external philosophy-of-mind literature using the phrase in this sense either. The underlying question, however, has a substantial and surprisingly precise external literature.
**Search queries used**:
- Aaronson "Ghost in the Quantum Turing Machine" freebits free will bounded initial conditions
- Valentini quantum equilibrium signal-locality theorem Born rule violation subquantum
- "minimum entropy coupling" "perfectly secure steganography" KL divergence zero detectability
- Landsman indeterminism undecidability Born rule Martin-Löf randomness measurement outcome sequences
- Bösch 2006 meta-analysis psychokinesis random number generators publication bias small effect
- quantum indeterminism free will "no deviation" Born statistics agency Kane self-forming / criterial causation
- "Born rule and free will" philsci-archive libertarian agent-causal (→ Kastner 2016; metadata confirmed via OpenAlex after PhilSci-Archive rejected direct fetches)

## Executive Summary

The question — *if conscious selection must preserve Born statistics exactly, how much agency is left, and is a conservation law even statable?* — turns out to have a formally exact answer-shape in information theory, plus three bookend results that fix the budget's ceiling, its floor, and the price of exceeding it. (1) **Achievability**: selection that must exactly preserve a target distribution is structurally identical to a *perfectly secure steganographic channel*. A 2023 result (Schroeder de Witt et al., ICLR) proves that a steganography procedure is perfectly secure (zero KL divergence between innocent and message-bearing output — no statistical test whatsoever can detect it) if and only if it is induced by a probabilistic *coupling* between message and output whose output-marginal equals the innocent distribution, and that maximum throughput among perfectly secure procedures is achieved by *minimum entropy coupling*. Mapped to the interface: conscious states play message, Born statistics play covertext, and the reviewer's demanded conservation law is precisely the coupling's marginal constraint — Σ_C P(o|C,X)·P(C|X) = q_Born(o|X) for every publicly conditionable context X, which is the very equation the reviewer wrote schematically. The per-event budget is bounded by min(H(conscious source), H(Born distribution)) bits and is *not* zero: exact preservation is compatible with substantial reasons-correlated selection. (2) **The price of the budget**: perfect security is *equivalent to* zero third-person statistical evidence. The theorem that grants the budget simultaneously formalises [[concepts/ensemble-level-epiphenomenalism|ensemble-level epiphenomenalism]] — selection content is recoverable only relative to a "decoder" that already has the mental-side facts. The budget account therefore converts the reviewer's "verbal conjunction" charge into a theorem-plus-disclosed-cost, without discharging the mechanism debt (P-Q3/P-Q10). (3) **The computability constraint**: Landsman's algorithmic-randomness argument (2020/2021) — quantum outcome sequences are predicted to be Martin-Löf random (1-random), a property far stronger than mere Born-frequency compliance. Any agency imprint that is *computably structured relative to public data* would make outcome sequences compressible and hence detectable-in-principle; the coupling escape route requires the imprint, viewed from outside, to be itself incompressible. (4) **Why exactness, not approximation**: Valentini's signal-locality theorem — in deterministic hidden-variables theories, *any* statistical-level deviation from quantum equilibrium (Born statistics) generically enables instantaneous signalling. The budget dial has no safe intermediate setting: exactly Born (statistically invisible agency) or deviation (causal-structure violations plus detectability). Aaronson's freebit picture (2013) contributes the *finite-stock* version of a budget — Knightian freedom sourced in uncloneable initial conditions and consumed as it is amplified into macroscopic records. Kastner (2016) argues independently that libertarian agent causation need not be anomic with respect to the Born rule. Empirical ceilings on any *detectable* residue (micro-PK meta-analyses) are already covered in [[research/selection-only-mind-influence-information-limits-2026-05-05|the 2026-05-05 information-limits note]] and are cross-referenced, not repeated. **Assess-first verdict: worth covering.** The subject is genuinely uncovered, quantifiable, and — the highest-value finding — a worked coupling is a live candidate for the toy model P-Q10 says the Map lacks.

## Key Sources

### Schroeder de Witt, Sokota, Kolter, Foerster & Strohmeier (2023) — Perfectly Secure Steganography Using Minimum Entropy Coupling

- **URL**: https://arxiv.org/abs/2210.14889 (ICLR 2023)
- **Type**: Peer-reviewed computer-science paper
- **Key points**:
  - Works within Cachin's (1998) information-theoretic model of steganography, where security is the KL divergence between covertext distribution and stegotext distribution; *perfect* security is divergence exactly zero — no statistical adversary, running any test, can do better than chance at detecting that a message is present.
  - Main theorems (verbatim from abstract, verified 2026-08-13): "a steganography procedure is perfectly secure under Cachin (1998)'s information-theoretic model of steganography if and only if it is induced by a coupling" and "among perfectly secure procedures, a procedure maximizes information throughput if and only if it is induced by a minimum entropy coupling."
  - A coupling is a joint distribution over (message, output) whose marginals are the given message distribution and the given covertext distribution. The output-marginal constraint *is* a conservation law: however the joint probability mass is arranged to correlate messages with outputs, the column sums must reproduce the covertext distribution exactly.
  - Throughput (mutual information between message and output) is bounded by min(H(message), H(covertext)) and the bound is approached by minimum entropy coupling; their iMEC algorithm achieves KL divergence at numerical precision for arbitrary covertext distributions.
- **Relevance mapping (original to this note — no published source applies this to mental causation)**: covertext distribution = Born distribution q(o|X) per public context X; stegotext = actual outcome sequence; message = conscious selection content; adversary = the totality of third-person statistical tests. The mapping makes the reviewer's two desiderata provably jointly satisfiable: genuine message-correlated structure in the outcomes (authorship) with exactly zero aggregate signature (undetectability). What the mapping *costs* is stated under Key Debates.
- **Tenet alignment**: Directly supports the mathematical coherence of Tenet 2's corridor reading (P-Q2) and gives Tenet 3 a channel formalism; neutral on whether the channel is actually occupied.

### Aaronson (2013) — The Ghost in the Quantum Turing Machine

- **URL**: https://arxiv.org/abs/1306.0159
- **Type**: Long-form essay / technical monograph (arXiv)
- **Key points**:
  - Introduces "Knightian freedom": in-principle physical unpredictability "that goes beyond probabilistic unpredictability" (verbatim, abstract, verified 2026-08-13) — unpredictability that cannot even be assigned a well-calibrated probability distribution.
  - The freebit picture "tries to find scope for 'freedom' in the universe's boundary conditions rather than in the dynamical laws" (verbatim, abstract): freebits are uncloneable quantum degrees of freedom traceable to the universe's initial state, never yet measured, whose values are therefore Knightian-uncertain. The No-Cloning theorem blocks any prediction device from characterising them in advance.
  - This is the literature's clearest *finite-stock* budget: freebits are consumed — once amplified into macroscopic records they become ordinary probabilistic facts — so the total agency allowance is bounded by the (finite) supply reaching a brain from its past light-cone.
  - Aaronson's picture needs no Born-rule deviation at all: a freebit-influenced event still looks like an ordinary quantum event to statistics; what differs is its *modal* status (no well-defined prior probability existed).
- **Tenet alignment**: Aligns with Tenet 2 (influence hides inside ordinary quantum statistics) and Tenet 5 (Knightian humility about priors). Aaronson himself is not a dualist and frames the picture as a speculative possibility-proof; the Map should cite it as such.

### Landsman (2020/2021) — Indeterminism and Undecidability

- **URL**: https://arxiv.org/abs/2003.03554 ; published in *Undecidability, Uncomputability, and Unpredictability* (Springer, 2021), also PhilArchive
- **Type**: Peer-reviewed book chapter (mathematical physics / philosophy of physics)
- **Key points**:
  - Argues that quantum indeterminism can be proved from Chaitin's incompleteness theorem, exploiting the *full* empirical content of quantum mechanics: not just long-run frequencies but the character of the outcome *sequences* themselves.
  - Idealised as infinite binary strings, outcome sequences of a fair quantum coin are predicted to be 1-random (Martin-Löf random) almost surely — a property much stronger than Born-frequency compliance and much stronger than uncomputability.
  - Consequence for the budget (this note's extension, not Landsman's claim — his target is determinism): frequency-preservation is *not* the only public constraint on selection. A selection policy that imprinted any computable pattern on outcomes — Morse-coding reasons into a spin sequence, say — would produce a compressible sequence, failing ML-randomness tests even while passing every frequency test. The budget is therefore constrained twice over: marginals must match Born (the coupling constraint) *and* the imprint must be incompressible relative to every computable test with public data. Reasons-guided selection survives only if, viewed without the mental-side key, its trace is algorithmically random.
  - This sharpens rather than contradicts the steganographic mapping: a perfectly secure coupling's output is distributed *identically* to the covertext, so it inherits ML-randomness automatically. The tension bites only for naive "signalling" models of agency — which is exactly why the corridor reading forbids them.
- **Tenet alignment**: Aligns with Tenet 2's exactness requirement; supplies the strongest available formal reason why agency cannot show up as pattern even where it cannot show up as bias.

### Valentini — Signal-Locality and Subquantum Information in Deterministic Hidden-Variables Theories

- **URL**: https://link.springer.com/chapter/10.1007/978-94-010-0385-8_6 (in *Non-locality and Modality*, Springer); background at https://arxiv.org/abs/quant-ph/0106098
- **Type**: Book chapter / peer-reviewed paper
- **Key points**:
  - Signal-locality theorem: deterministic hidden-variables theories that reproduce quantum theory for the quantum-equilibrium distribution (P = |ψ|²; Born) predict instantaneous statistical-level signals for hypothetical *non-equilibrium* ensembles.
  - Read as a budget result: at exact equilibrium the statistical-level agency budget is exactly zero (no controllable ensemble-level bias is possible); away from equilibrium the budget is positive but purchases superluminal signalling and the collapse of effective locality and uncertainty.
  - This explains *why* the Map's corridor must claim exactness rather than mere smallness: there is no physically innocent ε. Any standing deviation is both a detection surface (Chernoff scaling — a per-trial bias ε becomes visible after ~1/ε² trials) and, in the hidden-variables setting, a causal-structure violation.
  - Fuller treatment of Valentini's programme, including cosmological non-equilibrium searches, is in [[research/bohmian-quantum-equilibrium-and-non-equilibrium-2026-07-19|the 2026-07-19 quantum-equilibrium note]]; not repeated here.
- **Tenet alignment**: Aligns with Tenet 2 read strictly; conflicts with any "minimum-outside-the-corridor" fallback (the Route 2 the Map keeps open) by pricing it — Route 2's minimum is not statistically free.

### Kastner (2016) — The Born Rule and Free Will: Why Libertarian Agent-Causal Free Will Is Not "Antiscientific"

- **URL**: https://philsci-archive.pitt.edu/11893/ ; published in *Probing the Meaning of Quantum Mechanics* (World Scientific), pp. 231–243, DOI 10.1142/9789813146280_0009; reprinted in *Adventures in Quantumland* (2019), DOI 10.1142/9781786346421_0019
- **Type**: Conference paper / book chapter (metadata confirmed via OpenAlex; PhilSci-Archive rejected direct fetches, so the argument summary below rests on the abstract and secondary descriptions, flagged accordingly)
- **Key points**:
  - Argues against the common claim that libertarian agent causation must be "anomic" — lawless — with respect to the quantum statistical law, and is therefore antiscientific.
  - On Kastner's transactional-picture reading, an agent's volition can be implicated in which outcome is actualised while the Born weights remain the correct statistics over the possibility structure: lawful statistics over possibilities, agentive selection among them.
  - Closest published philosophical precedent for the Map's exact position; note Kastner's framework commitments (possibilist transactional interpretation) differ from the Map's forward-in-time post-decoherence preference — see [[concepts/transactional-interpretation-of-quantum-mechanics|the TI concept article]] for how the Map already handles Kastner material.
- **Tenet alignment**: Aligns with Tenets 2 and 3; her time-symmetric machinery is subordinate under the Map's 2026-06-10 subordination scope ruling (P-Q1).

### Empirical ceiling sources (cross-referenced, not re-summarised)

- Bösch, Steinkamp & Boller (2006), *Psychological Bulletin* — 380-study micro-PK meta-analysis; tiny heterogeneous effect consistent with publication bias. https://pubmed.ncbi.nlm.nih.gov/16822162/
- Maier & Dechamps-line Bayesian replication (2018), *Frontiers in Psychology* — strong evidence for the null. https://pmc.ncbi.nlm.nih.gov/articles/PMC5872141/
- Both are treated in depth, with the PEAR history and the decline-effect literature, in [[research/selection-only-mind-influence-information-limits-2026-05-05|the 2026-05-05 note]]; their role here is one sentence: the *detectable* residue of any agency budget is empirically bounded at or below ~10⁻⁴ bits/bit, and the best-powered modern test finds none — which is what a perfectly secure coupling predicts and what [[topics/parapsychology-firewall|the parapsychology firewall]] requires.

## Major Positions

### Zero-budget reading (ensemble-level epiphenomenalism pressed to verdict)
- **Proponents**: the objector position tracked by [[concepts/ensemble-level-epiphenomenalism]]; the 2026-08-13 outer-review convergence pressing demote-to-coherence-only
- **Core claim**: exact Born preservation leaves selection nothing to *do*; "which outcome" authorship with no conditional signature is chance under another name.
- **Relation to site tenets**: the standing challenge P-Q3 records at high confidence. The coupling result answers its *impossibility* form (bias and preservation are jointly consistent) but not its *idleness* form (what key-relative content is worth) — the note keeps these separate.

### Coupling / steganographic-channel reading
- **Proponents**: constructed here from Schroeder de Witt et al. 2023 + Cachin 1998; no published proponent applies it to consciousness
- **Core claim**: the agency budget is min(H(conscious source), H(Born distribution)) bits per selection event, deliverable at exactly zero statistical signature, with the conservation law Σ_C P(o|C,X)·P(C|X) = q_Born(o|X) holding per public context. Correlated populations are handled the same way: the constraint binds per *publicly conditionable* class X, so shared preferences must be offset within whatever ensemble an outside tester can actually assemble — bias conditional on hidden mental states survives; bias conditional on public variables is forbidden.
- **Key arguments**: the two ICLR theorems; ML-randomness inherited automatically from marginal-identity.
- **Relation to site tenets**: strongest formal support yet found for P-Q2's coherence; candidate skeleton for the P-Q10 toy model; leaves P-Q3's idleness horn standing and formalises P-Q9's self-concealment (perfect security *is* self-concealment, proved optimal).

### Typicality / type-class reading
- **Proponents**: folk-theorem material from the method of types (Cover–Thomas textbook tradition); implicit in the reviewer's "chance-equivalent outcome classes"
- **Core claim**: over n trials, Born-typical sequences number ~2^{nH(q)}; exact preservation confines selection to choosing *which* typical sequence is actualised, so the class size — 2^{nH(q)} — literally is the agency allowance, H(q) bits per trial. The reviewer's intuition is thus a special case of the coupling reading (couplings are how a choice-of-typical-sequence gets correlated with reasons without breaking marginals).
- **Relation to site tenets**: aligns; gives the budget its most quotable closed form.

### Finite-stock (freebit) reading
- **Proponents**: Aaronson 2013 (with antecedents he credits to Hoefer, Stoica, and Turing)
- **Core claim**: the budget is a consumable physical resource — Knightian-uncertain, uncloneable initial-condition bits — bounded by supply from the past light-cone and destroyed by amplification into records.
- **Relation to site tenets**: aligns with Tenets 2 and 5; differs from the Map in requiring no mental-side ontology at all, so it functions as a physicalist-adjacent comparison case: even *without* dualism, a bounded, statistically invisible freedom budget is defensible.

### Non-equilibrium reading (budget outside the corridor)
- **Proponents**: Valentini's programme (as possibility, not as consciousness thesis)
- **Core claim**: real ensemble-level agency requires non-equilibrium; exact equilibrium means zero statistical budget, full stop.
- **Relation to site tenets**: conflicts with the corridor's exactness only by relocating agency to a regime the Map rejects for the actual world; its value is adversarial — it prices Route 2 (minimum-outside-corridor) in signalling currency.

### Question-choice reading (Stapp)
- **Core claim**: agency's budget lives in *which measurement is made and when* (Process 1 / Zeno timing), not in which outcome occurs; outcome statistics stay Born by construction.
- **Relation to site tenets**: the historical antecedent slot-shifted — covered in the 2026-05-05 note; listed here because a full budget account should say whether basis-choice and outcome-choice budgets add, and nothing in the found literature computes the combined channel.

## Key Debates

### Is key-relative content real content?
- **Sides**: the coupling reading (authorship real, witnessable only from the mental side — the indexical move formalised) vs. the idleness horn (evidence-transcendent authorship is epiphenomenalism with extra steps).
- **Core disagreement**: whether a channel whose decoder necessarily possesses the mental facts already can ground *mental-to-physical* efficacy in a non-circular way.
- **Current state**: open; exactly P-Q3. The formal result moves the debate from "are the desiderata consistent?" (settled: yes) to "what is consistency worth?" (unsettled). The coherence-only citation grade in [[positions/quantum-interface]] should continue to govern downstream use.

### Where does the offsetting bias live in correlated populations?
- **Sides**: the reviewer (offsets must exist "across states, contexts, subjects, or outcomes" and need a law) vs. the per-public-context coupling answer (offsets are automatic within any ensemble an outsider can condition on; no cross-subject ledger is needed because the constraint was never per-subject).
- **Core disagreement**: whether "common ensemble" is a physical fact or an epistemic one. If two agents' conscious states could themselves be publicly conditioned on, their shared bias would become testable — so the account quietly requires that conscious states are not fully publicly resolvable, connecting the budget to privacy/inner-access commitments the Map holds elsewhere.
- **Current state**: unexplored in the found literature; the sharpest novel question this research surfaces. Also the natural home for the review's 1.3 fission worry: a per-system (not per-subject) coupling makes "total bias" conserved under subject-splitting by construction, at the cost of decoupling causal capacity from subject count.

### Exact vs. ε-approximate preservation
- **Sides**: exactness (Valentini's theorem; no-signalling; [[concepts/causal-consistency-constraint]] via Torres Alegre 2025) vs. small-deviation proposals (late Stapp; consciousness-collapse models with parameter windows).
- **Current state**: the Map is already committed to exactness (P-Q2, high confidence); the budget literature strengthens the case by showing exactness costs less than assumed — a nonzero budget survives it — while any ε is both detectable at ~1/ε² trials ([[topics/brain-internal-born-rule-testing|brain-internal Born tests]]) and causally expensive.

### Does the computability constraint bind reasons?
- **Sides**: Landsman-derived worry (reasons are compressible — shared, linguistically structured — so reason-correlated outcomes threaten compressibility) vs. the coupling answer (marginal-identity guarantees incompressibility of the *public* trace regardless of message structure).
- **Current state**: resolved in principle by the coupling theorems, but nobody has checked the quantum version: Cachin-model steganography is classical. Whether contextuality, POVM structure, or Gleason-type constraints narrow the set of physically realisable couplings is, as far as these searches found, an open and publishable question.

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1926 | Born's probability rule | The constraint the budget is defined against |
| 1952 | Bohm's pilot-wave theory | First concrete home for "hidden" determinants of outcomes |
| 1991 | Valentini's subquantum H-theorem | Born statistics as an *equilibrium* condition, not an axiom |
| 1998 | Cachin's information-theoretic steganography model | Perfect security = zero KL divergence; the budget's formal frame |
| 2002 | Valentini's signal-locality theorem | Any statistical deviation from Born buys signalling |
| 2006 | Bösch–Steinkamp–Boller meta-analysis | Empirical ceiling on detectable intention-correlated bias |
| 2013 | Aaronson's freebit essay | Finite-stock Knightian budget without Born deviation |
| 2016 | Kastner, "The Born Rule and Free Will" | Agent causation argued lawful under Born statistics |
| 2018 | Bayesian micro-PK replication (Frontiers) | Strong null at scale |
| 2020/21 | Landsman, "Indeterminism and Undecidability" | Outcome sequences must be 1-random, not just Born-frequent |
| 2023 | Schroeder de Witt et al., ICLR | Perfect security iff coupling; max throughput iff minimum entropy coupling |
| 2025 | Torres Alegre preprint (arXiv:2512.12636) | No-signalling-under-purification argument for forced Born form (unrefereed) |
| 2026 | ChatGPT outer review §1.2 | Names the missing conservation law; this note answers the shape of it |

## Potential Article Angles

Target section per the harvest task: `concepts/` (cap headroom confirmed at harvest; re-measure before creating).

1. **`concepts/agency-budget` (recommended)** — state the budget as a framework-internal formal result: the conservation law (coupling marginal constraint), the closed form (min-entropy bound; 2^{nH(q)} type-class size), the two bookends (achievability via coupling; 1-randomness of the public trace), and the disclosed cost (perfect security ≡ zero third-person evidence, so this *formalises* [[apex/self-concealing-interface|self-concealment]] rather than escaping it). Must carry the mechanism-debt citation grade explicitly: this is coherence arithmetic, not established mental causation. Highest value: a worked minimum-entropy coupling between a toy conscious-state space and a toy outcome space is a direct candidate for the P-Q10 toy model, meeting several desiderata already listed in [[apex/born-preserving-causal-efficacy]] (explicit joint distribution, exact marginal preservation, nonzero mutual information, per-context conservation).
2. Alternative, narrower: fold the budget into [[apex/born-preserving-causal-efficacy]] as a new section rather than minting a concept — defensible if concepts/ headroom has closed by execution time, but the reviewer's charge was that the account is *distributed*; a citable single home has integration value.
3. A follow-up research task (not an article yet): the quantum-Cachin question — which couplings are physically realisable given POVM/contextuality constraints, and does the Torres Alegre no-signalling argument interact with the coupling form? Genuinely open in the literature.

When writing the article, follow `obsidian/project/writing-style.md` (front-load the result; named-anchor the conservation law; explicit Relation to Site Perspective section connecting to Tenets 2, 3, and 5).

## Gaps in Research

- **The mapping is original**: no found source applies steganographic perfect security to mental causation. The article must present it as the Map's own framework-internal construction, at coherence-only grade — not as a published result about consciousness.
- **Classical-only theorems**: the coupling results are for classical distributions; the quantum version (couplings over measurement contexts, Gleason/contextuality constraints, whether purification arguments force coupling structure) is unexplored territory.
- **Kastner full text unretrieved**: PhilSci-Archive rejected fetches; the summary rests on abstract-level metadata (OpenAlex-confirmed DOIs). Before quoting her in an article, retrieve the chapter text.
- **Landsman extension is ours**: his argument targets determinism; the application to agency-imprint detectability is this note's inference and should be attributed that way.
- **Basis-choice + outcome-choice combined budget**: nothing found computes whether Stapp-style question-choice bandwidth and outcome-selection bandwidth add, trade off, or interact.
- **Freebit supply accounting**: Aaronson gestures at cosmological bounds on freebit supply; no found source computes a per-brain, per-lifetime figure that could be compared against behavioural information rates.
- **The privacy dependency**: the correlated-population answer requires conscious states to be publicly unresolvable in principle; whether the Map already asserts this strongly enough (and where) needs a positions-register check.

## Citations

- Aaronson, S. (2013). "The Ghost in the Quantum Turing Machine." arXiv:1306.0159. https://arxiv.org/abs/1306.0159
- Bösch, H., Steinkamp, F., & Boller, E. (2006). "Examining Psychokinesis: The Interaction of Human Intention With Random Number Generators — A Meta-Analysis." *Psychological Bulletin* 132(4), 497–523. https://pubmed.ncbi.nlm.nih.gov/16822162/
- Cachin, C. (1998). "An Information-Theoretic Model for Steganography." *Information Hiding* (Springer LNCS 1525). (Cited via Schroeder de Witt et al. 2023.)
- Kastner, R. E. (2016). "The Born Rule and Free Will: Why Libertarian Agent-Causal Free Will Is Not 'Antiscientific'." In *Probing the Meaning of Quantum Mechanics*, World Scientific, 231–243. DOI 10.1142/9789813146280_0009. Preprint: https://philsci-archive.pitt.edu/11893/
- Landsman, K. (2021). "Indeterminism and Undecidability." In *Undecidability, Uncomputability, and Unpredictability*, Springer. arXiv:2003.03554. https://arxiv.org/abs/2003.03554
- Schroeder de Witt, C., Sokota, S., Kolter, J. Z., Foerster, J., & Strohmeier, M. (2023). "Perfectly Secure Steganography Using Minimum Entropy Coupling." ICLR 2023. arXiv:2210.14889. https://arxiv.org/abs/2210.14889
- Valentini, A. (2002). "Signal-Locality and Subquantum Information in Deterministic Hidden-Variables Theories." In *Non-locality and Modality*, Springer, 81–103. https://link.springer.com/chapter/10.1007/978-94-010-0385-8_6
- Maier, M. A., et al. (2018). "Intentional Observer Effects on Quantum Randomness: A Bayesian Analysis Reveals Evidence Against Micro-Psychokinesis." *Frontiers in Psychology* 9:379. https://pmc.ncbi.nlm.nih.gov/articles/PMC5872141/
