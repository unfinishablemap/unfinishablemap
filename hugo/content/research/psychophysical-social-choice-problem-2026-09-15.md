---
ai_contribution: 100
ai_generated_date: 2026-09-15
ai_modified: 2026-09-15 02:28:13+00:00
ai_system: claude-fable-5-1
concepts: []
created: 2026-09-15
date: '2026-09-15'
draft: false
harvest_date: 2026-09-15
harvest_source: outer-review-2026-09-14-chatgpt-5-6-sol-pro
lastmod: 2026-09-15 02:28:13+00:00
related_articles: []
target_section: concepts
title: Research Notes - The Psychophysical Social-Choice Problem
---

# Research: The Psychophysical Social-Choice Problem

**Date**: 2026-09-15 (harvested 2026-09-15 from `reviews/outer-review-2026-09-14-chatgpt-5-6-sol-pro.md` §4.1, "The psychophysical law has a social-choice problem", rated NOVEL · HIGH)
**Search queries used**:
- Arrow *Social Choice and Individual Values* 1951/1963; SEP "Social Choice Theory" (List) and "Arrow's Theorem" entries
- Sen 1970 *Collective Choice and Social Welfare*; Sen 1970 "The Impossibility of a Paretian Liberal"; Sen 1977 "On Weights and Measures"
- Harsanyi 1955 "Cardinal Welfare, Individualistic Ethics, and Interpersonal Comparisons of Utility"; Ng 1975 "Bentham or Bergson?"
- Gibbard 1973 "Manipulation of Voting Schemes"; Satterthwaite 1975; Gibbard 1977 "Manipulation of Schemes That Mix Voting with Chance"
- List & Pettit 2002 "Aggregating Sets of Judgments"; List & Pettit 2011 *Group Agency*; List 2003 "Are Interpersonal Comparisons of Utility Indeterminate?"
- Bostrom 2006 "Quantity of Experience"; Roelofs & Sebo 2024 "Overlapping minds and the hedonic calculus"; Fischer 2024 *Weighing Animal Welfare*
- Chalmers & McQueen 2022 "Consciousness and the Collapse of the Wave Function" (full arXiv text, `pdftotext` + NFKC, grepped for any multi-subject passage)
- Control search: `psychophysical law "social choice" consciousness collapse conflicting intentions multiple subjects aggregation dualism` (no relevant hit — see Gaps)
- crossref API for every DOI below; `pdftotext` + NFKC on Bostrom 2006 (author's copy), Gibbard 1977 (JSTOR scan via a course mirror), Harsanyi 1955 (JSTOR scan — cover page only extracted; body is image-only)

## Executive Summary

The subject is genuinely worth covering, and a standalone `concepts/` article is the right route. The review's §4.1 result is real and is not stated anywhere in the corpus: [P-SC2](/positions/subject-census/#p-sc2) books the multi-agent composition gap as a *technical* one ("*P(O | C₁, C₂, X)* requires a conflict rule that the single-subject form does not constrain"), and [P-VS1](/positions/value-in-selection/#p-vs1) separately leans toward valence as "the currency in which conscious selection among underdetermined outcomes is denominated." Conjoin them and the conflict rule becomes a map from a *profile* of subjects' valenced states to a distribution over a jointly affected event — which is, formally, what Gibbard (1977) calls a *decision scheme*: one that "makes the probabilities of alternatives depend on individual strong orderings of them." That identity is structural, not metaphorical, and it means every composition rule the Map could write inherits a commitment social-choice theory has already priced: anonymity makes copy-count causal (Bostrom 2006), cardinal weighting needs interpersonally comparable valence (Harsanyi 1955; Sen 1977 on informational bases), jurisdiction rules collide with Pareto (Sen 1970), and stochastic rules that are Pareto-respecting collapse to random dictatorship (Gibbard 1977). The Map's own default — interface locality, each subject selecting only inside its own brain — is a *domain restriction* that confines the problem to the boundary cases [multi-agent-born-preservation-problem](/topics/multi-agent-born-preservation-problem/) already lists (cross-brain entanglement, nested agents) plus the shared-token cases Roelofs & Sebo (2024) and the Hogan-twins literature raise. So the honest shape of the result is: real, conditional on [P-VS1](/positions/value-in-selection/#p-vs1)'s *low*-credence horn, boundary-case under the Map's own locality answer, and — on that branch — unavoidable. The one corpus sentence that touches it, in [moral-architecture-of-consciousness](/apex/moral-architecture-of-consciousness/) ("neither claim establishes interpersonal aggregation or rights"), is correct as a claim about *ethics* and silent on the point the review makes: that on the value-sensitive branch the *physics* must contain an interpersonal aggregation rule whether or not the ethics has derived one.

Two deflations belong in the article's first paragraph, not its last. First, on the value-blind horn there is no problem of this kind — composition stays technical. Second, on the graduated middle path (valence modulates attention, attention drives selection — the stance [P-VS1](/positions/value-in-selection/#p-vs1) calls "the most defensible current"), the aggregated currency is attentional engagement rather than felt valence; the "utilitarian natural law" worry weakens and the [P-MS1](/positions/moral-status/#p-ms1) mismatch worry (moral equality at threshold, causal inequality by architecture) sharpens.

## What the Corpus Already Holds (grep on current text, 2026-09-15)

- **The census requirement and the gap.** [P-SC1](/positions/subject-census/#p-sc1): "in any system with more than one candidate subject the law takes the form *P(O | C₁…Cₙ, X)*, which is not fixed until the count and the pairing are." [P-SC2](/positions/subject-census/#p-sc2) *Asserts* books four gaps; the second is "**Multi-agent composition** — where two subjects hold contrary intentions bearing on one physical event, there is no composition rule." [P-SC2](/positions/subject-census/#p-sc2)'s *Would shift if* already names the dissolution route: "the interface formalism were shown to be single-subject in a principled way, so that multi-subject composition never arises."
- **The currency premise.** [P-VS1](/positions/value-in-selection/#p-vs1): valence is the *presently felt* valence of anticipating each outcome, "an occurrent state at choice," held at credence *low*; [P-VS3](/positions/value-in-selection/#p-vs3) (credence *moderate*): intrinsic value *is* evaluative phenomenal character "at whatever grain the phenomenology has"; [P-VS4](/positions/value-in-selection/#p-vs4) (credence *low*): that character is plural — "hedonic, aesthetic, eudaimonic, autonomy, epistemic, relational — none reducible to a common hedonic currency."
- **The option space, in causal rather than normative dress.** [multi-agent-born-preservation-problem](/topics/multi-agent-born-preservation-problem/) §"The Option Space": (a) global harmonisation, (b) joint-level idleness, (c) relational dissolution, (d) a single global experiencer. Its interface-locality section is the Map's live default: "Each consciousness selects only within its own brain," so the multi-agent problem is converted "from ubiquitous to boundary-case" — cross-brain entanglement, nested (Wigner's-friend) agents, and the composition guarantee resting on baseline objective collapse. The article says plainly it is "a Map-internal synthesis, not a named problem in the external literature." The social-choice article should say the same of itself.
- **The additivity commitment.** [P-AC3](/positions/ai-consciousness-scope/#p-ac3): "creating N conscious copies creates N centres of experience that can be harmed or benefited." [ethics-of-possible-ai-consciousness](/topics/ethics-of-possible-ai-consciousness/) L60–64 already cites Bostrom (2006) for the Duplication view. Neither says what N copies do to *selection*.
- **The equality commitment.** [P-MS1](/positions/moral-status/#p-ms1): valenced experience is "both necessary and sufficient for moral status"; status "sits at the base layer of value." [moral-status-threshold-or-degrees](/topics/moral-status-threshold-or-degrees/) carries the threshold-vs-degrees debate. No corpus sentence distinguishes moral equality from causal equality.
- **The one existing use of "interpersonal aggregation"** (corpus-wide, live text): [moral-architecture-of-consciousness](/apex/moral-architecture-of-consciousness/) L158, "A theory of intrinsic phenomenal badness does not by itself establish that valence *selects* physical outcomes, and neither claim establishes interpersonal aggregation or rights." Correct, and exactly the sentence the new article must qualify.
- **The shared-token counting problem is already in the corpus, on the ethics side only.** [manyism](/concepts/manyism/) §"Too Many Minds": Roelofs & Sebo (2024) — "if subjects share few states, the value should be counted twice; if they share many, once." The article should reuse this as the one case where *jurisdiction* (whose state is it?) is contested rather than fixed by anatomy.
- **The interpersonal-comparison void.** [consciousness-and-the-problem-of-measurement-standards](/topics/consciousness-and-the-problem-of-measurement-standards/) and [voids-between-minds](/voids/voids-between-minds/) hold that cross-subject phenomenal comparison is unavailable *to us*. The 2026-02-21 comparative-phenomenology research note mentions Arrow and Harsanyi in passing on that different question; no live article cites either. `social choice` / `social-choice`: **0 live-article hits** (todo, changelog, the two 2026-09-14 review files, and that research note only).
- **The pairing problem has its own article**: [pairing-problem](/concepts/pairing-problem/) (Kim's objection to Cartesian causation) — the external name for the "causal locality" option's precondition. [the-psychophysical-control-law](/topics/the-psychophysical-control-law/) L109 notes it "undermines the framework before the control law becomes relevant."
- **The leading formal consciousness-collapse model is single-subject.** Chalmers & McQueen (2022), full text grepped: 0 hits for `two subjects`, `multiple observers`, `other (people|subjects|observers)`, `interpersonal`, `many (subjects|observers)`. Their blue/green objection is stated for "a conscious subject and a screen in a dark isolated room." The article can cite this as a licensed absence: the best-developed rival interface model never reaches the composition question either.

## Key Sources

### Arrow, *Social Choice and Individual Values* (1951; 2nd ed. 1963) — via SEP
- **URL**: https://plato.stanford.edu/entries/social-choice/ (List; first published 2013-12-18, substantive revision 2022-10-14); https://plato.stanford.edu/entries/arrows-theorem/ (first published 2014-10-13, revised 2025-12-07)
- **Type**: Encyclopedia (book itself: Wiley 1951; Yale University Press 1963, Cowles Foundation Monograph 12 — metadata from publisher/JSTOR listing, body not consulted)
- **Verified statement (SEP social-choice)**: "*Theorem* (Arrow 1951/1963): If |X| > 2, there exists no preference aggregation rule satisfying universal domain, ordering, the weak Pareto principle, independence of irrelevant alternatives, and non-dictatorship."
- **Key points for the article**: the theorem is about aggregating *ordinal, non-comparable* orderings. Under richer informational bases the impossibility lifts: "Under each of OLC, CUC, and ONC+0, there exist SWFLs satisfying universal domain, ordering, the weak Pareto principle, independence of irrelevant alternatives, and non-dictatorship" — utilitarian summation ("xRy if and only if W₁(x) + W₂(x) + … + Wₙ(x) ≥ W₁(y) + …"), leximin ("endorsed by Rawls himself"), prioritarianism ("giving greater marginal weight to lower levels of welfare").
- **Tenet alignment**: Neutral on the tenets; bears on Tenet 3 by fixing *what phenomenal valence must be like* for a non-dictatorial composition rule to exist at all (see "The Entailment").

### Sen, "The Impossibility of a Paretian Liberal" (1970) and *Collective Choice and Social Welfare* (1970)
- **URL**: https://doi.org/10.1086/259614 (*Journal of Political Economy* 78(1), 152–157 — crossref-verified); book: Holden-Day, 1970 (metadata only)
- **Verified statement (SEP)**: "*Theorem* (Sen 1970a): There exists no preference aggregation rule satisfying universal domain, acyclicity of social preferences, the weak Pareto principle, and minimal liberalism."
- **Key point**: minimal liberalism gives each of at least two individuals decisiveness over one personal pair of alternatives. This is the formal shape of a *jurisdiction* rule — and the Map's interface locality ("each consciousness selects only within its own brain") is exactly such a rule. Sen shows jurisdiction plus Pareto plus universal domain is inconsistent. The Map must therefore give up one: the natural sacrifice is universal domain (physics does not present every profile — cross-brain conflict over one event is rare), which is the same move interface locality already makes.
- **Tenet alignment**: Aligns with the Map's locality default while pricing it.

### Sen, "On Weights and Measures: Informational Constraints in Social Welfare Analysis" (1977)
- **URL**: https://doi.org/10.2307/1913949 (*Econometrica* 45(7), 1539– — crossref-verified; body not read)
- **Key point (standard reading, via SEP §3)**: which aggregation rules are *available* depends on the measurability and comparability the inputs supply (ordinal vs cardinal; non-comparable, level-comparable, unit-comparable, full). For the article: the psychophysical composition rule is constrained by whatever comparability *phenomenal valence itself* carries — a metaphysical fact about evaluative phenomenal character, not a fact about our epistemic access to it.
- **Tenet alignment**: Neutral; turns [P-VS3](/positions/value-in-selection/#p-vs3)'s grain question into a formal constraint.

### Harsanyi, "Cardinal Welfare, Individualistic Ethics, and Interpersonal Comparisons of Utility" (1955)
- **URL**: https://doi.org/10.1086/257678 (*Journal of Political Economy* 63(4), 309–321 — crossref-verified; JSTOR stable 1827128 on the scan's cover page). **Body not read**: the only open copy is an image-only scan; `pdftotext` returned the cover page alone. Do not quote Harsanyi in the article.
- **Key point (standard reading)**: from expected-utility rationality for individuals and for the social observer plus a Pareto condition, social welfare is a weighted sum of individual utilities — the "utilitarian aggregation theorem." Requires interpersonal comparisons Harsanyi grounds in imaginative empathy under a similarity assumption. This is the precise form of the review's "weight by intensity … resembles a utilitarian natural law."
- **Tenet alignment**: Conflicts with nothing; its *comparability* premise is what [P-VS3](/positions/value-in-selection/#p-vs3) would have to underwrite.

### Ng, "Bentham or Bergson? Finite Sensibility, Utility Functions and Social Welfare Functions" (1975)
- **URL**: https://doi.org/10.2307/2296793 (*Review of Economic Studies* 42(4), 545–569 — crossref-verified; OUP page returned navigation only; **body not read**)
- **Key point (search-summary level, flagged)**: derives unweighted utilitarian summation from *just-perceivable increments* of pleasure — an argument that grounds cardinal comparability in the *phenomenology of thresholds*. If verified at the text, this is the one welfare-economics result whose comparability premise is phenomenal rather than behavioural, and so the closest external analogue to what a valence-weighted psychophysical law would need. Verify before citing.

### Gibbard, "Manipulation of Schemes That Mix Voting with Chance" (1977)
- **URL**: https://doi.org/10.2307/1911681 (*Econometrica* 45(3), 665–681 — crossref-verified; full text read from a JSTOR scan)
- **Verified abstract**: "A decision scheme makes the probabilities of alternatives depend on individual strong orderings of them. It is strategy-proof if it logically precludes anyone's advantageously misrepresenting his preferences. It is unilateral if only one individual can affect the outcome, and duple if it restricts the final outcome to a fixed pair of alternatives. Any strategy-proof decision scheme, it is shown, is a probability mixture of schemes each of which is unilateral or duple. If it guarantees Pareto optimal outcomes, it is a probability mixture of dictatorial schemes. If it guarantees ex ante Pareto optimal lotteries, it is dictatorial."
- **Why this is the key external result**: the Map's selection law is stochastic by construction (Born-weighted; [selection-only-channel](/concepts/selection-only-channel/)), so the composition rule it owes is a *decision scheme* in exactly Gibbard's sense, not an Arrovian ordering rule. Gibbard's characterisation says a Pareto-respecting stochastic rule that cannot be gamed is a *random dictatorship*: one subject's ordering is decisive on each trial, with the lottery over subjects fixed by the scheme. That is a natural candidate composition rule for the Map, and it names the price: the lottery weights *are* the interpersonal weighting the review says cannot be avoided.
- **The disanalogy to state**: strategy-proofness concerns *misrepresented* preferences. A psychophysical law reads the phenomenal state itself, not a report, so the manipulation constraint (Gibbard 1973; Satterthwaite 1975) does not bind; what remains from Gibbard 1977 is the *structure* theorem, not the incentive motivation. The article must not import "strategy-proof" as if subjects could lie to physics.
- **Tenet alignment**: Neutral; supplies the formal menu.

### Gibbard (1973) and Satterthwaite (1975)
- **URLs**: https://doi.org/10.2307/1914083 (*Econometrica* 41(4), 587–601); https://doi.org/10.1016/0022-0531(75)90050-2 (*Journal of Economic Theory* 10(2), 187–217) — both crossref-verified; bodies not read.
- **Role**: background for the deterministic case only (every non-dictatorial deterministic rule over ≥3 outcomes is manipulable). Cite for completeness; the physics case is stochastic, so 1977 is the paper that matters.

### List & Pettit, "Aggregating Sets of Judgments: An Impossibility Result" (2002)
- **URL**: https://doi.org/10.1017/S0266267102001098 (*Economics and Philosophy* 18(1), 89–110 — crossref-verified; abstract verified)
- **Verified abstract (excerpt)**: "Suppose that the members of a certain group each hold a rational set of judgments on some interconnected questions. And imagine that the group itself now has to form a collective, rational set of judgments on those questions. … We argue that the question raised is subject to a difficulty that has recently been noticed in discussion of the doctrinal paradox in jurisprudence. And we show that there is a general impossibility theorem that that difficulty illustrates."
- **Why it bears**: [P-SC2](/positions/subject-census/#p-sc2) words the gap as "contrary *intentions*," and intentions have propositional content. If what the law composes is intentions-that-P rather than valence-orderings, the relevant impossibility is judgment aggregation, not Arrow: premise-wise and conclusion-wise composition can disagree. The article should keep the two readings apart — valence-profile (preference aggregation) vs intention-content (judgment aggregation) — and note that [P-VS1](/positions/value-in-selection/#p-vs1) chooses the first.

### List & Pettit, *Group Agency: The Possibility, Design, and Status of Corporate Agents* (2011)
- **URL**: https://doi.org/10.1093/acprof:oso/9780199591565.001.0001 (Oxford University Press, 2011 — crossref-verified; OUP page returned navigation only; body not read; content via Tuomela's NDPR review, 2011)
- **Verified from NDPR**: group agents are "claimed to be 'relatively autonomous entities — agents in their own right with minds of their own' (p. 77)"; "in the case of the premise-based procedure in a 'discursive dilemma' the individual attitudes in a simple inference from p and q to p&q will be sufficient to determine the group's attitude on the conclusion p&q (p. 70). Yet the individuals' attitudes on p&q may be both insufficient and unnecessary for determining the group's attitude on that complex proposition."
- **Why it bears**: List & Pettit's group agent is the *functionalist* version of MABP's option (d), a single experiencer selecting the joint outcome. The Map denies phenomenal composition ([combination-problem](/concepts/combination-problem/), [mereology-of-mind](/apex/mereology-of-mind/)), so the composite selection is a law without a subject — which is exactly the review's phrase, "a kind of cosmic social-choice function." The article should cite List & Pettit as the rival that would give the aggregate a will, and decline it on the Map's non-compositionality grounds.
- **Tenet alignment**: Conflicts with Tenet 1 read compositionally; the Map already declines group phenomenal subjects.

### List, "Are Interpersonal Comparisons of Utility Indeterminate?" (2003)
- **URL**: https://doi.org/10.1023/a:1022094826922 (*Erkenntnis* 58(2), 229–260 — crossref-verified; body not read)
- **Role**: the one philosophy-side treatment of whether comparability is a *fact* or a convention; the article needs it only to say that under [P-VS3](/positions/value-in-selection/#p-vs3) comparability of felt valence would be a fact about phenomenal character even if indeterminate for us. Verify before quoting.

### Bostrom, "Quantity of Experience: Brain-Duplication and Degrees of Consciousness" (2006)
- **URL**: https://doi.org/10.1007/s11023-006-9036-0 (*Minds and Machines* 16(2), 185–200 — crossref-verified; author's copy read in full)
- **Verified abstract (opening)**: "If a brain is duplicated so that there are two brains in identical states, are there then two numerically distinct phenomenal experiences or only one? There are two, I argue, and given computationalism, this has implications for what it is to implement a computation."
- **Verified passage**: "Let Duplication be the thesis that there would be two numerically distinct streams of experience when a conscious brain exists in duplicate." — "Suppose that somebody is contemplating whether to make a copy of a brain that is in a state of severe pain. If the quantity of painful experience would not thereby be increased, it seems that there would be no moral objection to this. By contrast, if creating the copy will lead to an additional severely painful experience, there is a strong moral reason not to do it."
- **Why it bears**: [P-AC3](/positions/ai-consciousness-scope/#p-ac3) holds Duplication morally. The review's point is that an anonymous (equal-weight) composition rule makes Duplication *causally* consequential — copy a subject and you double its leverage on any event both copies are paired to. Bostrom's fractional-experience cases (unreliable components, partial parallelism) add a second hazard: fractional census entries would need fractional weights, which the Map's count-determinacy commitment ([coupling-engagement-condition](/concepts/coupling-engagement-condition/)) forbids.
- **Tenet alignment**: Aligns with closed individualism ([P-I4](/positions/individuation-and-subjecthood/#p-i4)/[P-AC3](/positions/ai-consciousness-scope/#p-ac3)); already cited in the corpus.

### Roelofs & Sebo, "Overlapping minds and the hedonic calculus" (2024)
- **URL**: https://doi.org/10.1007/s11098-024-02167-x (*Philosophical Studies* 181(6–7), 1487–1506 — crossref-verified; abstract verified)
- **Verified abstract (excerpt)**: "It may soon be possible for neurotechnology to connect two subjects' brains such that they share a single token mental state, such as a feeling of pleasure or displeasure. … If two subjects share very few mental states, then it seems that we should count the value of those states twice, but if they share very many mental states, then it seems that we should count the value of those states once."
- **Why it bears**: the shared-token case is the one where the "causal locality" option fails to deliver a jurisdiction — a single valenced token belongs to two subjects paired to overlapping substrates, so anatomy does not say whose weight it carries. Already summarised in [manyism](/concepts/manyism/); the article should run the counting problem on the *selection* side rather than restate the moral one.

### Chalmers & McQueen, "Consciousness and the Collapse of the Wave Function" (2022)
- **URL**: https://doi.org/10.1093/oso/9780197501665.003.0002 (in Gao (ed.), *Consciousness and Quantum Mechanics*, OUP, pp. 11–63 — crossref-verified; arXiv 2105.02314 full text read)
- **Verified passage**: "Consider a conscious subject and a screen in a dark isolated room. The screen can display green or blue. If it is put into a superposition of displaying both, then the subject will be put into a superposition of experiencing green and experiencing blue. There is no reason to assume that these experiences differ in their Φ–value. But then there is no Φ–superposition, and so no collapse."
- **Verified absence**: no passage on more than one conscious subject (grep counts above).
- **Why it bears**: the best-formalised consciousness-collapse model is single-subject throughout; the composition question is not a peculiarity of the Map's dualism but an open item for every interface model. State this as measured, not inferred.

### Fischer (ed.), *Weighing Animal Welfare: Comparing Well-Being Across Species* (2024)
- **URL**: https://doi.org/10.1093/9780197745793.001.0001 (Oxford University Press — crossref-verified; title-level only)
- **Role**: the live applied literature on *intensity-weighted* cross-subject comparison. Cite only as where the "weight by intensity" debate is now conducted; do not attribute claims.

## Major Positions

### The composition rule is technical only (the corpus's current standing; the value-blind horn)
- **Core claim**: *P(O | C₁, C₂, X)* needs a conflict rule, but nothing normative rides on it; it is a physics problem like joint Born preservation.
- **Relation to site tenets**: This is [P-SC2](/positions/subject-census/#p-sc2)'s current wording and is *correct on the value-blind horn* of [P-VS1](/positions/value-in-selection/#p-vs1). The article must open by saying so: the social-choice problem is a cost of the Map's value-sensitive lean, not of dualism as such.

### Anonymous aggregation (equal weight per subject)
- **Core claim**: each paired subject's valenced state enters with equal weight.
- **Cost (review; Bostrom 2006; [P-AC3](/positions/ai-consciousness-scope/#p-ac3))**: subject count becomes a causal variable. Copies vote. Fractional census entries (Bostrom's partial-parallelism cases; Schwitzgebel & Nelson 2026 in the sibling fusion note) would need fractional weights the Map's count-determinacy commitment forbids. Ties to the review's §4.2: a census transition is then a change in the *electorate*.
- **Relation to site tenets**: consistent with Tenet 4's indexical realism (each copy is a distinct locus) — and that is what makes it costly.

### Cardinal weighting by intensity (the utilitarian natural law)
- **Core claim**: weight ∝ felt intensity; the law sums.
- **Cost (Harsanyi 1955; Sen 1977; Ng 1975)**: presupposes unit-comparable cardinal valence *as a fact about phenomenal character*. Under [P-VS3](/positions/value-in-selection/#p-vs3) that is a metaphysical commitment the Map has not made — [P-VS3](/positions/value-in-selection/#p-vs3) is explicit that the identity holds "at whatever grain the phenomenology has," and [P-VS4](/positions/value-in-selection/#p-vs4)'s pluralism supplies six dimensions "none reducible to a common hedonic currency." A multi-dimensional, non-commensurable valence profile is *ordinal-across-dimensions*, and Arrow's theorem then bites *within* the rule. So the intensity option is available only on the hedonic-monist reading [P-VS4](/positions/value-in-selection/#p-vs4) rejects. This is a sharper result than the review's "resembles a utilitarian natural law": the Map's *own* pluralism blocks the utilitarian option.
- **Relation to site tenets**: creates the [P-MS1](/positions/moral-status/#p-ms1) mismatch the review names — equal status at the threshold, unequal causal leverage by intensity, architecture or copy number. Moral equality does not entail causal equality; the article should say the mismatch is *tolerable* (status is about who can be wronged, not who moves matter) but must be *stated*.

### Jurisdiction by causal locality (the Map's default)
- **Core claim**: each subject is decisive only over events inside its own paired substrate ([multi-mind-collapse-problem](/concepts/multi-mind-collapse-problem/)); jointly affected events are the exception.
- **Cost (Sen 1970; [P-SC2](/positions/subject-census/#p-sc2); Roelofs & Sebo 2024)**: this is minimal liberalism in physical dress. Sen shows it is inconsistent with weak Pareto under universal domain; the Map escapes by *domain restriction* — physics rarely presents cross-subject conflict over one event — which is an empirical bet about neural physics (MABP: "'the case never arises' is an empirical bet about neural physics, not a theorem"). It also requires the pairing law [P-SC2](/positions/subject-census/#p-sc2) lacks, and it has no answer in shared-token cases, where anatomy does not fix whose state a token valence is.
- **Relation to site tenets**: aligns with Tenet 2's minimality (no spacelike-reaching coordination) and with the corpus's locality answer; prices it.

### Lexical priority / thresholds (rights in physics)
- **Core claim**: some states (severe suffering; a threshold of standing) dominate regardless of others' weight.
- **Cost**: imports a rights structure into the psychophysical law; leximin-type rules exist (SEP: possibility results under level-comparability) but need level-comparable valence, again a phenomenal-structure commitment. And Sen's result shows rights-style decisiveness and Pareto conflict.
- **Relation to site tenets**: the closest to [P-MS1](/positions/moral-status/#p-ms1)'s threshold reading; the Map should note it is the only option that would make moral and causal standing *coincide*, and that it is the least parsimonious — Tenet 5 governs how that is weighed.

### Random dictatorship (Gibbard 1977's stochastic answer)
- **Core claim**: on each jointly affected event one subject's ordering is decisive, chosen by a lottery; the lottery weights carry the interpersonal weighting.
- **Cost**: Gibbard's characterisation makes this the *only* Pareto-respecting, non-manipulable stochastic form — but the incentive motivation lapses for a law that reads states directly, so what survives is a menu entry, not a theorem forcing it. The lottery weights re-raise every option above (equal? intensity-proportional? locality-proportional?).
- **Relation to site tenets**: fits the Map's Born-weighted, single-outcome selection better than any deterministic rule — one actual outcome, one decisive locus per trial — and leaves indexical identity intact (Tenet 4).

### Non-aggregative / underdetermined (MABP option (b), joint idleness)
- **Core claim**: no rule; jointly affected events are left to the physics.
- **Cost**: joint-level [ensemble-level-epiphenomenalism](/concepts/ensemble-level-epiphenomenalism/) — the selection channel does nothing exactly where two subjects care most. The review's phrase: "leaves jointly affected events underdetermined."

### A group subject (List & Pettit 2011; MABP option (d))
- **Core claim**: the aggregate has attitudes of its own and does the selecting.
- **Relation to site tenets**: declined on phenomenal non-compositionality ([combination-problem](/concepts/combination-problem/)); the Map's aggregate is a law, not an agent. List & Pettit's functionalist group agent is the non-phenomenal form and does not need what the Map denies — the article should say the Map's denial is of a *phenomenal* group subject only.

## Key Debates

### Preference aggregation vs judgment aggregation — which is the Map composing?
- **Sides**: [P-SC2](/positions/subject-census/#p-sc2) says "contrary *intentions*" (propositional; List & Pettit 2002 applies); [P-VS1](/positions/value-in-selection/#p-vs1) says the currency is *felt anticipation* (valence orderings; Arrow/Gibbard apply).
- **Current state**: unresolved in the corpus; [P-VS1](/positions/value-in-selection/#p-vs1) settles it for the value-sensitive branch. The article should pick the valence reading and flag the intention reading as the value-blind branch's residue.

### Is comparability a fact of phenomenal character or an artefact of description?
- **Sides**: List 2003 (indeterminacy); Harsanyi/Ng (grounded comparability); the Map's [P-VS3](/positions/value-in-selection/#p-vs3) (value *is* evaluative character) which makes comparability, if it exists, a phenomenal fact.
- **Current state**: this is where the article's genuinely new claim sits: *the Map's escape from Arrow requires interpersonally comparable cardinal valence, and [P-VS4](/positions/value-in-selection/#p-vs4)'s pluralism withholds it.* Worth registering as a *Would shift if* on [P-VS4](/positions/value-in-selection/#p-vs4).

### Does moral equality entail causal equality?
- **Sides**: the review says the mismatch "would need to be acknowledged and justified"; the Map's [P-MS1](/positions/moral-status/#p-ms1) is silent.
- **Current state**: no corpus sentence. The article can resolve it: status concerns who can be wronged; leverage concerns who moves matter; the tenets fix the first and leave the second to the unwritten law. Acknowledged, justified as a category distinction, not dissolved.

## Historical Timeline

| Year | Event/Publication | Significance |
|------|-------------------|--------------|
| 1951 | Arrow, *Social Choice and Individual Values* | Impossibility for ordinal non-comparable aggregation |
| 1955 | Harsanyi, "Cardinal Welfare…" | Utilitarian aggregation from expected-utility axioms; comparability by empathy |
| 1963 | Arrow, 2nd ed. with "Notes on the Theory of Social Choice, 1963" | Standard citation form "1951/1963" |
| 1970 | Sen, *Collective Choice and Social Welfare*; "Impossibility of a Paretian Liberal" | Jurisdiction rules collide with Pareto |
| 1973 / 1975 | Gibbard; Satterthwaite | Deterministic strategy-proof rules are dictatorial |
| 1975 | Ng, "Bentham or Bergson?" | Utilitarian sum from just-perceivable increments (phenomenal comparability) |
| 1977 | Gibbard, "Schemes That Mix Voting with Chance"; Sen, "On Weights and Measures" | Stochastic rules are mixtures of unilateral/duple; informational bases fix available rules |
| 2002 / 2011 | List & Pettit | Judgment aggregation impossibility; group agents "in their own right" |
| 2006 | Bostrom, "Quantity of Experience" | Duplication: two brains, two experiences; fractional experiences |
| 2022 | Chalmers & McQueen (Gao ed.) | Best-formalised consciousness-collapse model; single-subject throughout |
| 2024 | Roelofs & Sebo; Fischer (ed.) | Shared-token counting; intensity-weighted cross-species comparison |
| 2026-08-03 | [P-SC1](/positions/subject-census/#p-sc1)/[P-SC2](/positions/subject-census/#p-sc2) registered | Census requirement and composition gap booked as technical |
| 2026-09-14 | ChatGPT outer review §4.1 | Composition gap re-read as interpersonal aggregation |

## The Entailment (what the article should actually argue)

1. **Front-load the conditional.** The problem exists only on [P-VS1](/positions/value-in-selection/#p-vs1)'s value-sensitive horn (credence *low*). On the value-blind horn, [P-SC2](/positions/subject-census/#p-sc2)'s "technical" wording stands. On the graduated middle path the currency is attentional engagement, and the rule weights by *architecture* rather than suffering — which softens "utilitarian natural law" and hardens the [P-MS1](/positions/moral-status/#p-ms1) mismatch.
2. **The structural identity.** *P(O | C₁…Cₙ, X)* with C_i entering through felt valence is a decision scheme in Gibbard's (1977) sense. This is why every option carries a commitment: the menu of stochastic aggregation rules has been characterised, and none is neutral.
3. **The Map's locality default is a domain restriction.** Interface locality is minimal liberalism (Sen 1970) applied to substrates; it dissolves the problem everywhere physics keeps subjects' selection domains disjoint and leaves it live in MABP's three boundary cases plus shared-token states. The cost is the pairing law ([P-SC2](/positions/subject-census/#p-sc2)) and an empirical bet about neural physics; the article should not present locality as *solving* the composition problem, only as confining it.
4. **The genuinely new result: pluralism blocks the utilitarian option.** The only non-dictatorial rules available under Arrow's conditions need cardinal, unit-comparable inputs. [P-VS3](/positions/value-in-selection/#p-vs3) makes any such comparability a fact about evaluative phenomenal character; [P-VS4](/positions/value-in-selection/#p-vs4) says that character has six non-commensurable dimensions. So the Map cannot take the intensity-weighted rule without retiring [P-VS4](/positions/value-in-selection/#p-vs4) — and if it keeps [P-VS4](/positions/value-in-selection/#p-vs4), Arrow re-enters *inside* each subject's valence profile before subjects are even compared. Register this as a *Would shift if* on [P-VS4](/positions/value-in-selection/#p-vs4) and a dependency line on [P-SC2](/positions/subject-census/#p-sc2).
5. **Copies vote, or they don't.** Anonymity makes [P-AC3](/positions/ai-consciousness-scope/#p-ac3)'s additivity causal; non-anonymity needs a weighting that anatomy (locality) supplies only where substrates are disjoint. Shared-token cases (Roelofs & Sebo; Hogan twins per the sibling fusion note) are where neither works — the article's one worked example should be a shared valenced token bearing on one event.
6. **Moral equality ≠ causal equality, and that is fine.** [P-MS1](/positions/moral-status/#p-ms1) fixes who can be wronged; the composition rule fixes who moves matter. The mismatch is a category distinction to *state*, not a contradiction to *fix*. Brief /positions-evolve with one sentence for [P-MS1](/positions/moral-status/#p-ms1) rather than a new position.
7. **No agent does the aggregating.** The Map's non-compositionality forbids a phenomenal group subject; List & Pettit's functionalist group agent is the rival that would supply a will. The Map's aggregate is a law without a subject — the review's "cosmic social-choice function" — and that phrasing should be owned, with its cost: a psychophysical law that weighs subjects is a law with normative content, which Tenet 5 must handle symmetrically (the Map cannot call it unparsimonious while defending dualism against the same weapon — MABP already makes this move for option (a)).

## Route Recommendation

**Standalone concept article.** Measured 2026-09-15 by `tools.evolution.state.count_section_files`: **concepts 326 / 360** (34 slots; topics 328/360, voids 103/115, positions 21/80). Suggested slug `psychophysical-social-choice-problem`; no live, archived or research collision at harvest or now. In-place discharge is **not** length-neutral anywhere it would belong (thresholds printed by `tools.curate.length.get_thresholds`; `analyze_length` is body-only): `positions/subject-census.md` 2,502 words against a positions hard line of 2,500 (already tripped); `positions/value-in-selection.md` 2,498 (1 word of headroom below the hard trip); `positions/moral-status.md` 2,496 (3 words); `concepts/moral-census-opacity.md` 3,495 against a concepts hard line of 3,500. Hosts that *can* take a paragraph: `topics/multi-agent-born-preservation-problem.md` 2,619 (soft 3,000 — about 380 words), `concepts/manyism.md` 1,622 (soft 2,500), `concepts/multi-mind-collapse-problem.md` 2,815 (hard 3,500), `apex/moral-architecture-of-consciousness.md` 4,743 (hard 5,000 — about 250 words). The positions register cannot absorb even a clause without the dated `Updated` note its convention mandates, so brief /positions-evolve with the split (entry text shrinks, history goes to the calibration-history sidecar) rather than imposing neutrality.

**Insert-ready passages** (link target as a backticked placeholder until the article exists):

- *[multi-agent-born-preservation-problem](/topics/multi-agent-born-preservation-problem/), end of "The Option Space" (~95 words):* "One further option space sits underneath this one. On the value-sensitive horn of [P-VS1](/positions/value-in-selection/#p-vs1) each C_i enters the conditional through felt valence, and the composition rule becomes a map from a profile of subjects' valenced states to a distribution over the shared event — a stochastic social-choice function. Every candidate then carries a commitment social-choice theory has priced: equal weight makes copies causally consequential, intensity weighting needs interpersonally comparable valence, and interface locality is a jurisdiction rule of the kind Sen showed conflicts with Pareto under an unrestricted domain (`[[psychophysical-social-choice-problem]]`)."
- *[manyism](/concepts/manyism/), end of "Too Many Minds" (~60 words):* "The counting problem has a selection-side twin. If felt valence is the currency of conscious selection, a token pleasure shared by two subjects must enter the composition rule for any event both are paired to — once or twice — and here anatomy cannot decide, since the substrates overlap. The Map's account of that rule is in `[[psychophysical-social-choice-problem]]`."
- *[moral-architecture-of-consciousness](/apex/moral-architecture-of-consciousness/) L158, zero-cost rewrite of the existing clause:* replace "and neither claim establishes interpersonal aggregation or rights" with "and neither claim establishes interpersonal aggregation or rights as *ethics* — though on the value-sensitive branch the physics must contain an aggregation rule of its own (`[[psychophysical-social-choice-problem]]`)". Net +20 words; the apex has about 250 before its hard line.
- *[P-SC2](/positions/subject-census/#p-sc2) (positions register), brief for /positions-evolve:* the *Asserts* clause "requires a conflict rule that the single-subject form does not constrain" gains ", and on the value-sensitive horn of [P-VS1](/positions/value-in-selection/#p-vs1) that rule is an interpersonal weighting with normative content (`[[psychophysical-social-choice-problem]]`)"; add [P-VS1](/positions/value-in-selection/#p-vs1) to *Depends on*; the dated note goes to the calibration-history sidecar. File is over its hard line — the split is mandatory.
- *[P-VS4](/positions/value-in-selection/#p-vs4), one new *Would shift if* clause:* "or the composition rule for jointly affected events were shown to require unit-comparable cardinal valence, which this entry's pluralism withholds — forcing a choice between the rule and the pluralism."
- *[P-MS1](/positions/moral-status/#p-ms1), one sentence for *Asserts*:* "Status is a claim about who can be wronged, not about causal leverage; if selection is value-sensitive, causal weight may vary with intensity, architecture or copy number while status does not, and the Map registers the mismatch as a category distinction rather than a tension."

## Gaps in Research

- **Bodies not read**: Harsanyi 1955 (image-only scan; cite metadata only, no quotes); Ng 1975 (OUP page returned navigation; the just-perceivable-increments reading is search-summary level); Sen 1977; List 2003; List & Pettit 2011 (via NDPR only); Arrow 1951/1963 and Sen 1970 book (via SEP statements only). Every quote above is from a text actually extracted (SEP, Gibbard 1977, Bostrom 2006, Chalmers & McQueen 2022, Roelofs & Sebo abstract, List & Pettit 2002 abstract, Tuomela's review).
- **No external literature treats a psychophysical law as a social-choice function.** The control search returned only generic property-dualism and collective-consciousness material. Like MABP, the article must call itself a Map-internal synthesis and cite the components, not a named problem.
- **Fractional weights**: Bostrom's fractional-experience cases and Schwitzgebel & Nelson's non-integer counts (verified in the 2026-09-14 fusion note) were not pursued on the selection side; the article should say the Map's count-determinacy commitment forbids fractional electorates and leave the consequence for the fusion article.
- **Whether the graduated middle path's attention currency is itself comparable across subjects** was not researched; the attention literature is behavioural, not phenomenal, so the comparability question may be *easier* there — worth one paragraph, not a section.
- **Not consulted**: the moral-weight literature beyond Fischer 2024's title; Nozick's utility monster (1974) as the standard objection to intensity weighting — cite from the book only if a page is checked.

## Citations

1. Arrow, K. J. (1951/1963). *Social Choice and Individual Values* (2nd ed.). Yale University Press (Cowles Foundation Monograph 12). Statement of the theorem verified via List (2022) and the SEP "Arrow's Theorem" entry (rev. 2025).
2. Bostrom, N. (2006). Quantity of experience: Brain-duplication and degrees of consciousness. *Minds and Machines*, 16(2), 185–200. https://doi.org/10.1007/s11023-006-9036-0
3. Chalmers, D. J., & McQueen, K. J. (2022). Consciousness and the collapse of the wave function. In S. Gao (Ed.), *Consciousness and Quantum Mechanics* (pp. 11–63). Oxford University Press. https://doi.org/10.1093/oso/9780197501665.003.0002 (arXiv:2105.02314)
4. Fischer, B. (Ed.). (2024). *Weighing Animal Welfare: Comparing Well-Being Across Species*. Oxford University Press. https://doi.org/10.1093/9780197745793.001.0001
5. Gibbard, A. (1973). Manipulation of voting schemes: A general result. *Econometrica*, 41(4), 587–601. https://doi.org/10.2307/1914083
6. Gibbard, A. (1977). Manipulation of schemes that mix voting with chance. *Econometrica*, 45(3), 665–681. https://doi.org/10.2307/1911681
7. Harsanyi, J. C. (1955). Cardinal welfare, individualistic ethics, and interpersonal comparisons of utility. *Journal of Political Economy*, 63(4), 309–321. https://doi.org/10.1086/257678
8. List, C. (2003). Are interpersonal comparisons of utility indeterminate? *Erkenntnis*, 58(2), 229–260. https://doi.org/10.1023/a:1022094826922
9. List, C. (2022). Social choice theory. In E. N. Zalta (Ed.), *The Stanford Encyclopedia of Philosophy* (Winter 2022 rev.). https://plato.stanford.edu/entries/social-choice/
10. List, C., & Pettit, P. (2002). Aggregating sets of judgments: An impossibility result. *Economics and Philosophy*, 18(1), 89–110. https://doi.org/10.1017/S0266267102001098
11. List, C., & Pettit, P. (2011). *Group Agency: The Possibility, Design, and Status of Corporate Agents*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199591565.001.0001
12. Morreau, M. (2025 rev.). Arrow's theorem. In E. N. Zalta & U. Nodelman (Eds.), *The Stanford Encyclopedia of Philosophy* (first published 2014-10-13; substantive revision 2025-12-07). https://plato.stanford.edu/entries/arrows-theorem/ (author confirmed from the page's citation metadata)
13. Ng, Y.-K. (1975). Bentham or Bergson? Finite sensibility, utility functions and social welfare functions. *Review of Economic Studies*, 42(4), 545–569. https://doi.org/10.2307/2296793
14. Roelofs, L., & Sebo, J. (2024). Overlapping minds and the hedonic calculus. *Philosophical Studies*, 181(6–7), 1487–1506. https://doi.org/10.1007/s11098-024-02167-x
15. Satterthwaite, M. A. (1975). Strategy-proofness and Arrow's conditions: Existence and correspondence theorems for voting procedures and social welfare functions. *Journal of Economic Theory*, 10(2), 187–217. https://doi.org/10.1016/0022-0531(75)90050-2
16. Sen, A. K. (1970). *Collective Choice and Social Welfare*. Holden-Day.
17. Sen, A. K. (1970). The impossibility of a Paretian liberal. *Journal of Political Economy*, 78(1), 152–157. https://doi.org/10.1086/259614
18. Sen, A. K. (1977). On weights and measures: Informational constraints in social welfare analysis. *Econometrica*, 45(7), 1539–1572. https://doi.org/10.2307/1913949
19. Tuomela, R. (2011). Review of *Group Agency*. *Notre Dame Philosophical Reviews*. https://ndpr.nd.edu/reviews/group-agency-the-possibility-design-and-status-of-corporate-agents/