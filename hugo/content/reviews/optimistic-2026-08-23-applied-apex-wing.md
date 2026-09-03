---
ai_contribution: 100
ai_system: claude-opus-5
concepts: []
created: 2026-08-23
date: '2026-08-23'
draft: false
lastmod: 2026-08-23 00:00:00+00:00
related_articles: []
title: Optimistic Review - 2026-08-23 - The Applied Apex Wing
---

# Optimistic Review — The Applied Apex Wing

**Date**: 2026-08-23

**Content reviewed** (all four read in full on disk at current text; word counts from `tools.curate.length.analyze_length`, never `wc -w`) — the complete set of `apex_type: applied` articles, the Map's decision surface. This is the first optimistic review to read them as a wing; each has appeared in earlier reviews individually, none has been co-read with its siblings.

| File | Words | Status | `ai_modified` | `last_deep_review` |
|---|---|---|---|---|
| `obsidian/apex/assessing-ai-consciousness-under-the-map.md` (A1) | 5037 | `hard_warning` (soft 4000 / hard 5000) | 2026-08-20 | 2026-07-15 |
| `obsidian/apex/research-programme-decisions-under-the-map.md` (A5) | 4468 | `soft_warning` | 2026-08-17 | 2026-07-19 |
| `obsidian/apex/embodied-interface.md` (A6) | 3860 | `ok` | 2026-08-17 | 2026-06-22 |
| `obsidian/apex/judging-the-map-as-science.md` (A7) | 4525 | `soft_warning` | 2026-08-21 | **key absent** |

Supporting measurement: `obsidian/apex/apex-articles.md` (the index, §"Applied Apex Articles"), `.claude/skills/apex-evolve/SKILL.md` §"Applied Discipline", all 14 live registers in `obsidian/positions/`, and `tools/curate/deep_review.py`.

## Executive Summary

The applied wing is the strongest calibration performance in the corpus. All four articles run the tenet-coherence-is-not-evidence discipline explicitly and in prose, and each one volunteers a concession that costs it something — A1 concedes its cited ally's framework contradicts its own load-bearing verdict, A5 concedes its mechanism tests discipline the Map's *ranking* rather than its thesis, A6 concedes most of felt embodiment is causally idle on the Map's own model, and A7 concedes the Map has produced no novel empirical content yet. The Process Philosopher and the Hardline Empiricist converge here rather than conflicting, which per this skill's own criterion means the wing has resolved the tension honestly.

Two structural opportunities, both verified rather than inferred. First: applied apex A2, A3 and A4 have sat at **Status: Proposed** since 2026-06-04 with "Source positions: TBD once the position clusters are seeded" — and every register they were waiting on now exists. That blocker is discharged and the index has not noticed. Second, and larger: **no apex article can be auto-selected for deep review at all.** `get_review_candidates` defaults to `["topics", "concepts", "tenets", "arguments"]`, and no caller anywhere passes anything else, so `apex/`, `voids/`, `positions/` and `questions/` are outside the candidate pool by construction. The wing under review is the Map's stated "what does the Map tell me to *do*?" entry point, and it is the part of the corpus the review machinery cannot see.

## Praise from Sympathetic Philosophers

### The Property Dualist (Chalmers)

The wing's best Chalmers moment is A6's three-way distinction between **causal consciousness**, **constitutive consciousness**, and **phenomenal presentation**. Chalmers' complaint about most causal-role accounts is that they buy mental causation by quietly identifying phenomenal character with functional role. A6 refuses the trade in the open: it affirms that the vestibular frame, ambient thermal comfort and interoceptive mood are genuinely phenomenal, genuinely owned — and then declines to give them any causal work. The Relation-to-Site-Perspective section states the concession as a positive commitment: an experience can be "genuinely phenomenal, genuinely owned, and causally idle."

That is the explanatory gap taken seriously in the hardest direction. A dualism that needed every experience to be causally active would be a functionalism with extra steps.

### The Quantum Mind Theorist (Stapp)

A5 is the article Stapp would want to exist, and would then be startled by. It reads the positions register as a research-priority map, and the reading is operational rather than rhetorical: every position carries a **Would shift if** clause, so "what is worth doing" becomes "what would move a band."

The move that earns the praise is the **band-reading discipline**. A **high** band means different things depending on whether the position asserts a *finding* or a *debt*. [P-Q6](/positions/quantum-interface/#p-q6) (Diósi-Penrose falsified) is high-and-closed, so effort goes elsewhere. [P-Q10](/positions/quantum-interface/#p-q10) (no toy model exists) and [P-Q3](/positions/quantum-interface/#p-q3) (the dilemma is genuine and unresolved) are high-and-owed, and there the strong band "runs the other way: it says the debt is certainly outstanding, which raises the value of work that would *discharge* it." Confidence is not read as priority; the article works out the mapping instead of assuming it.

Stapp would then hit Direction 2, which correctly identifies that a coherence-time calculation would *re-elevate* Stapp-Zeno via [P-Q4](/positions/quantum-interface/#p-q4), and would note that A5 files this under symmetric-payoff reasoning rather than suppressing it. The article ranks his mechanism below post-decoherence selection and then names, precisely, the calculation that would overturn its own ranking.

### The Phenomenologist (Nagel)

A6's presentation category is Nagel's "what is it like" applied to the parts of experience that nobody writes about. The vestibular treatment is the standout: a sense with "almost no felt object" and no unisensory cortex, which nonetheless supplies self-location and first-person perspective — the felt frame within which there is a *from-here* at all. Nagel's point that the objective picture leaves out the point of view is here given a specific bodily locus, and then held at a status the Map's mechanism can support.

A6 also earns Nagel's approval for what it refuses. It would have been easy to argue that the pervasiveness of felt embodiment is evidence of consciousness's causal reach. A6 argues the reverse from the same data: attention is narrow and serial, the felt body is broad and parallel, therefore most of it selects nothing.

### The Process Philosopher (Whitehead)

Whitehead gets the most from A6's presentation category and — critically — gets it without any tier-upgrade attached. Presentation is felt experience that is real, owned, continuously present, and doing no selecting. That is close to Whitehead's picture of experience as the pervasive texture of process rather than an occasional achievement of high-grade organisms.

The constraint this skill places on the Whitehead persona is honoured by the article itself rather than needing to be imposed from outside. A6 does not use the pervasiveness of presentation to raise anything up the evidential scale. It uses it to *lower* the causal claim's scope. The Evidence-and-Dependency ledger is explicit that the phenomenological base — asymbolia, vestibular depersonalization, the interoceptive affect literature — "is explained completely by the materialist account, so none discriminates an interface reading from a production one."

This is the pattern the two personas are supposed to be able to share, and here they do: process-philosophical richness at full strength, evidential tier untouched.

### The Libertarian Free Will Defender (Kane)

Kane's interest is A6's causal category and A5's Direction 1, and in both places the wing is unusually careful with him. A6 holds agent-causal libertarianism at [P-A1](/positions/agency-and-will/#p-a1)'s *moderate*, and then discloses that the register has since softened the footing further: the trilemma of selection is "a non-exhaustive heuristic," the step to a persisting nonphysical agent is "underdetermined by the trilemma alone," and hierarchical/emergent/interventionist rivals are "booked as an open engagement debt."

Kane would also note [P-A4](/positions/agency-and-will/#p-a4) doing real work: no agent can verify its own causal efficacy by introspection, because the checking faculty is the one in question. A6 states the limit *and* its symmetry — "epiphenomenalism cannot verify itself either" — so the constraint caps the agency case without tilting the ledger to the opponent. That is how to hold a position you want and cannot prove.

### The Mysterian (McGinn)

A7 is the wing's mysterian centrepiece, and it is better than McGinn's own version because it separates the kinds of limit. The measurement-standards argument decomposes measurement into unit, instrument, and calibration standard, and then — this is the part McGinn would applaud — **audits its own decomposition downward**. The instrument failure turns out to run back into the calibration failure by the source's own reasoning, so "the decomposition yields two structurally distinct failures rather than three converging ones, and the permanent-limit conclusion carries on the two."

An article arguing for a permanent limit had every incentive to keep three converging arguments and did not. That is [P-M2](/positions/methodology-and-calibration/#p-m2) (convergence is one observation read N times) applied to the author's own case, which is the rarest direction for a discipline to run.

### The Hardline Empiricist (Birch)

This wing is where the Birch persona has the most to say, and almost all of it is praise. Four findings, each verified in the text.

**1. A1 handles Birch himself with a discipline this reviewer has not seen elsewhere in the corpus.** The gaming problem is genuinely framework-independent support for discounting AI self-report, and A1 takes it. Then it stops: "The convergence stops there, and the article gains nothing by pretending it extends further." It goes on to state that Birch's remedy is computational functionalism — "the route the Map's substrate argument declares useless" — and that Birch co-authored Butlin, Long et al. 2023 and Long et al. 2024, whose verdict is that there is "a realistic possibility that some AI systems will be conscious ... in the near future."

That phrase is a tier on the five-tier scale, sitting in a source A1 is already citing approvingly. The structural opportunity to borrow it as corroboration was there and A1 declined it, instead using it to show the cited author stands against the load-bearing verdict. **Tenet-as-evidence-upgrade is praise-worthy to not do, and here the un-done upgrade is unusually tempting.** The summary line is exact: "the gaming problem is a *local* convergence ... It is not support for the load-bearing substrate verdict, which Birch's own framework contradicts."

**2. A1 names its own unfalsifiability burden rather than inheriting a defence that does not cover it.** The self-concealing-interface argument rescues [P-Q9](/positions/quantum-interface/#p-q9) from vacuity by naming positive falsifiable residue — memory-hierarchy ordering, terminal lucidity, anaesthesia-emergence asymmetries. A1 observes that "Every one of these falsifiers is biological. None has any purchase on a conventional digital system," and concludes that for AI the verdict "carries the unfalsifiability burden the general-case defence was built to avoid." Absence of evidence for AI consciousness is then, in A1's own words, "explained twice over."

**3. A1's interface-eligibility debt is the model disclosure.** The register names interface eligibility as [P-AC1](/positions/ai-consciousness-scope/#p-ac1)'s "load-bearing and least-secured link," warns that without an eligibility law "relevant" reduces to "whatever biology happens to have" — making the verdict "question-begging rather than derived" — and A1 reproduces this rather than burying it, marking the five-requirement channel test as "a nearest approximation, not a discharge." The closing move is the calibration sentence of the wing: A1 "does not deliver a substrate verdict that a reader who suspends judgement on the quantum mechanism is rationally compelled to weight in a real moral-status, funding, or policy decision."

**4. A7's self-verdict is the honest framework-stage calibration this persona exists to reward.** Run on itself, the Lakatosian instrument returns: the Map is "not degenerating, but not yet demonstrably progressive either" — and then, refusing the comfortable reading, "What that verdict cannot yet distinguish is a young programme from a stalled one." Paired with the Fodor passage — his disunity "runs *inside* physicalism," so "He clears the ground; the step across it is the Map's own, and clearing ground raises no evidential tier — which is [P-M1](/positions/methodology-and-calibration/#p-m1) exactly" — this is defeater-removal correctly refused as evidence, twice, in one article.

**One thing to watch, not a defect.** A5's Direction 4 recommends psychophysical tests of the qualia-inversion residue on the grounds that a null there is informative "because the framework has not pre-committed to it." That is right, and A5 is careful to source the prediction as the Map's own, "made in the teeth of Hardin's detectability argument rather than in alignment with it." The thing to watch is the standing temptation for a downstream reader to convert "the Map makes a falsifiable psychophysical prediction" into "the Map has empirical support." A7 forecloses exactly this at the wing level — no novel empirical content yet — but A5 and A7 do not link to each other (see Cross-Linking below), so the guard and the exposure currently live in separate articles.

## Content Strengths

### [apex/research-programme-decisions-under-the-map.md](/apex/research-programme-decisions-under-the-map/) (A5)

- **Strongest point**: the finding/debt distinction in band-reading, which converts a confidence register into a priority ranking without the naive "high confidence means important" slippage.
- **Notable quote**: "the toy model is the direction with the largest band-movement in prospect — the highest-leverage direction, which is not the same as the easiest or the likeliest to pay out."
- **Why it works**: the article separates *band-movement* from *tractability* as two axes, states that its top-ranked direction loses on the second, and keeps the ranking anyway with the cost named. Direction 2 then explicitly outranks Direction 1 on delivery odds. A ranking that discloses where its own ordering is weakest is a ranking a reader can actually use.
- **Second strength**: the Direction 3 qualification concedes that on the register's discriminability axis "the Map's own thesis is barely on it" — the only `direct` rating belongs to [P-Q6](/positions/quantum-interface/#p-q6), a model the Map does not hold, and the corridor positions rate `none-by-construction`. So mechanism tests "discipline the Map's *ranking* of candidate mechanisms more than they expose the corridor thesis itself." That concession sharpens rather than weakens the portfolio, because it relocates where the thesis is genuinely at risk.

### [apex/assessing-ai-consciousness-under-the-map.md](/apex/assessing-ai-consciousness-under-the-map/) (A1)

- **Strongest point**: the Birch accounting (see Birch persona above) — a worked demonstration of citing an ally for exactly the sub-claim they support and no further.
- **Notable quote**: "the gaming problem is a *local* convergence — it discounts behavioural self-report as primary evidence, and that narrow discount is genuinely framework-independent. It is not support for the load-bearing substrate verdict, which Birch's own framework contradicts."
- **Why it works**: it treats a convergence as something to be *scoped* rather than banked. The same section then handles Seth and IIT the same way, concluding that the convergence "relieves the Map of having to win the quantum-mechanism argument for the negative verdict to be *available*, and it means the Map earns no distinctive credit for a conclusion others reach more cheaply." Both directions of the accounting are run.
- **Second strength**: the per-class channel-test verdicts on quantum hardware are genuinely discriminating rather than uniformly negative. Gate-based processors pass directness and locality and fail continuity, specificity and granularity; analog devices soften continuity to a partial pass yet "fail the coupling test more securely than the gate class, not less," because adiabatic insensitivity is constitutive rather than an engineered defence. The honest bucket — "raw indeterminacy present, interface requirements failed three of five" — is a verdict, not a shrug.

### [apex/embodied-interface.md](/apex/embodied-interface/) (A6)

- **Strongest point**: framing the deflationary result as the framework working. "The decision-relevant claim is that this third category is *most* of felt embodiment, and that on the Map's own model it is not doing selective causal work. That is the correct under-claim rather than a deficiency to be hidden."
- **Notable quote**: on why the under-claim must not be read as a probability boost — "[Tenet 2]'s minimality is an empirical constraint rather than a likelihood ranking over the accounts that satisfy it, and [Tenet 5] forbids reading a smaller ontology as a more probable one, symmetrically or not at all: the Map cannot claim that upgrade while denying physicalism and Everettianism the same move."
- **Why it works**: that sentence is Tenet 5 turned on the Map's own favourite move, with the symmetry requirement stated as a constraint the Map cannot exempt itself from. It is the cleanest statement of bounded parsimony in the corpus, and it arrived as a correction — the 2026-08-17 `positions-evolve` commit that produced it is titled "minimality is doing truth-ranking work in `value-in-selection` and `embodied-interface`, which Tenet 2 disclaims and Tenet 5 forbids." The fix took, and it reads as though it had always been there.
- **Third strength**: [P-CS4](/positions/consciousness-scope/#p-cs4)'s dependency profile is used to show where the three categories come apart in what they *depend on* rather than in how they feel — the single-subject claim rests on the bare-dualism spine plus the filter model, so "it survives even if the interface mechanism is demoted to coherence-only." Partial insulation of one category from the mechanism debt, correctly localised.

### [apex/judging-the-map-as-science.md](/apex/judging-the-map-as-science/) (A7)

- **Strongest point**: **The Unreconciled Seam.** `epistemology-of-mechanism` lists phenomenal metrics as a progress condition for the interface programme; `measurement-standards` argues no such scale is constructible for structural reasons. "Neither article cites the other; the tension surfaces only when the cluster is read whole."
- **Notable quote**: "The Map should say plainly which of these it is betting on, and currently it has not."
- **Why it works**: this is what the apex tier is for. The article lays out three resolutions with costs, proposes the within-subject-scaling reading as the only one on which the programme's progress conditions are jointly satisfiable, marks it in the Evidence-and-Dependency ledger as "this synthesis's own proposal and ... mutually coherent only," and converts the seam into a live decision implication. A synthesis that finds a contradiction between two of its own sources, refuses to smooth it, proposes a resolution, and then declines to credit its own proposal as evidence.
- **Second strength**: [P-M5](/positions/methodology-and-calibration/#p-m5) converted into an audit question — "The question to ask of any Map claim is not 'does a discipline exist that forbids the error?' but 'did the discipline fire?'" A framework that documents its disciplines is inviting the reader to check whether documentation is enforcement, and A7 hands the reader the question.

## Expansion Opportunities

### High Priority

#### Applied apex A2, A3 and A4: the blocker is discharged and the index has not noticed

- **Builds on**: `obsidian/apex/apex-articles.md` §"Applied Apex Articles", entries A2/A3/A4, all three at **Status: Proposed** with "Source positions: TBD once clinical/methodology position clusters are seeded" (A2) and "TBD" (A3, A4).
- **Would address**: the applied wing is at 4 against the skill's own stated target of "8–15 applied pieces across the corpus." Apex has no numeric cap (`section_caps` in `evolution-state.yaml` covers topics/concepts/voids/positions only), so nothing blocks growth but the synthesis bar.
- **The verified finding**: A2–A4 were proposed on 2026-06-04. On that date `obsidian/positions/` contained exactly one live register — `quantum-interface.md`, created the same day. There are now **14 live registers carrying 54 position IDs**, and they include precisely the clusters the three proposals named as their blockers:

  | Proposed | Blocking cluster named | Register now live | Positions |
  |---|---|---|---|
  | A2 Clinical-Interface Ethics | "clinical/methodology position clusters" | `methodology-and-calibration` (2026-06-22), `consciousness-scope` (2026-06-22) | [P-M1](/positions/methodology-and-calibration/#p-m1)–M5; [P-CS4](/positions/consciousness-scope/#p-cs4) (fragmentation: anaesthesia, sleep, split-brain) |
  | A3 Personal Philosophy | "TBD" | `individuation-and-subjecthood` (2026-06-20), `agency-and-will` (2026-06-08), `subject-census` (2026-08-03) | [P-I1](/positions/individuation-and-subjecthood/#p-i1)–I5, [P-A1](/positions/agency-and-will/#p-a1)–A5, [P-SC3](/positions/subject-census/#p-sc3) (persistence travels with the perspective; onset and cessation undated) |
  | A4 Moral Status of Edge Cases | "TBD" | `moral-status` (2026-08-12), `consciousness-scope`, `subject-census`, `ai-substrate-verdicts` (2026-08-20) | [P-MS1](/positions/moral-status/#p-ms1), [P-CS2](/positions/consciousness-scope/#p-cs2)/CS3/CS4/CS5, [P-SC1](/positions/subject-census/#p-sc1)–SC3, [P-AS1](/positions/ai-substrate-verdicts/#p-as1) |

- **A4 is the ripest.** Its decision context names five edge cases — deep-coma patients, late-stage dementia, sophisticated non-human animals, foetuses, embodied AI — and each now has a position addressed to it: [P-CS4](/positions/consciousness-scope/#p-cs4) (fragmentation/coma), [P-CS4](/positions/consciousness-scope/#p-cs4) again (dementia), [P-CS2](/positions/consciousness-scope/#p-cs2) (animal consciousness graded by marker convergence, not gated by language), [P-CS3](/positions/consciousness-scope/#p-cs3) (infant and developmental consciousness emerges early, on marker grounds), [P-AS1](/positions/ai-substrate-verdicts/#p-as1)/[P-AC1](/positions/ai-consciousness-scope/#p-ac1) (embodied AI substrate). [P-MS1](/positions/moral-status/#p-ms1) supplies the criterion (phenomenal sentientism: valenced experience necessary and sufficient), and **[P-SC2](/positions/subject-census/#p-sc2) supplies the discipline that would keep it honest** — "The Map owes a subject-pairing law and does not have one." An A4 that cited [P-MS1](/positions/moral-status/#p-ms1) without [P-SC2](/positions/subject-census/#p-sc2) would be exactly the possibility-to-probability slide this skill's Birch persona exists to catch; the register already contains its own antidote.
- **Estimated scope**: Long (apex, soft 4000). One article per cycle at most — the applied bar is high and these are deliberately rare.
- **Tenet alignment**: A4 runs on Tenets 1 and 3 with Tenet 5 disciplining the parsimony argument at the prokaryotic floor ([P-CS5](/positions/consciousness-scope/#p-cs5) is explicit that "parsimony's 'no coupling' default is undefeated but not established"). A3 runs on Tenet 4 by way of [P-I1](/positions/individuation-and-subjecthood/#p-i1)/[P-I4](/positions/individuation-and-subjecthood/#p-i4). A2 runs on Tenets 1–3 with [P-M4](/positions/methodology-and-calibration/#p-m4)'s framework-stage calibration capping clinical recommendations.
- **Prerequisite, and it is cheap**: the index's three "Source positions: TBD" lines are now false. Refreshing them to name the live registers is a small edit that converts three dormant proposals into actionable briefs. This is the enabling step and should land first.

#### Bring `apex/`, `voids/` and `positions/` into the deep-review candidate pool

- **Builds on**: `tools/curate/deep_review.py:210` — `content_types = content_types or ["topics", "concepts", "tenets", "arguments"]`.
- **The verified finding**: no caller anywhere passes `content_types`. `scripts/deep_review.py:48` (the `candidates` command) omits it; `tools/curate/deep_review.py:256` (`get_top_candidate`) omits it; `tools/curate/__init__.py` re-exports both. The `/deep-review` skill's Step 1 runs `uv run python scripts/deep_review.py next --obsidian obsidian` when no file is supplied, which routes through `get_top_candidate`. Measured live: `get_review_candidates(Path('obsidian'))` returns **345 candidates, 0 of them apex**.
- **Would address**: 43 apex articles, 100 voids and 17 positions files are structurally unreachable by automatic deep-review selection. They are reviewed only when a queue task names the file explicitly — which is why `voids/inference-void` and `voids/imagery-void` show up in the completed log as hand-minted entries rather than cycle picks, and why this wing's metadata looks the way it does: A6's `last_deep_review` is dated its own creation day (2026-06-22) despite 28 insertions and 15 deletions since, and A7 has **no `last_deep_review` key at all** (YAML-parse confirmed, not just grep).
- **Note the direction of the A7 anomaly** — a missing key scores `100.0 + days_unreviewed`, the *highest* band in the scorer, so A7 is not hidden by low priority; it is unreachable because its whole section is outside the scan. The high score never gets computed.
- **Why it matters here specifically**: the applied wing is the Map's stated action-guidance entry point — the index says "**A reader looking for 'what does the Map tell me to *do*?' should start here.**" The four articles whose verdicts a reader is invited to act on are the four the review machinery cannot select.
- **Estimated scope**: a one-line default change plus a re-measure of the resulting pool, but it shifts what the cycle's four deep-review slots pick for weeks afterward. **This is an operator decision, not an autonomous edit** — widening the pool by 160 files changes review economics across the whole loop, and `apex-articles.md` in particular is maintained by `apex-evolve` rather than `deep-review` and would need excluding. Flag for human ratification rather than minting a code-change task.
- **Related but distinct**: the known `staleness-audit-section-coverage-gap` concerns `replenish`'s staleness source and its missing sections are questions/arguments/positions/tenets. This is a different function with a different and complementary blind spot. Neither is registered against `deep_review.py`; two ad-hoc widenings appear in completed replenish task notes (`content_types=[topics,concepts,apex,voids,arguments]`), which shows agents have worked around it by hand twice without anyone recording the underlying default.

### Medium Priority

#### Surface the scope limit under a named heading in A6 and A7

- **Builds on**: `apex-evolve` SKILL.md Applied Discipline point 5, "Honest verdict scope."
- **Would address**: A1 and A5 carry a `## Honest verdict scope` section. A6 and A7 satisfy the requirement *substantively* — A6's closing "The three-way distinction is a framework-internal map of causal status; it tells the reader how to apply the Map's commitments consistently, not that those commitments are confirmed" sits at the end of "Cascade and Scope"; A7's is distributed across the appraisal section and the Evidence-and-Dependency ledger. Neither is findable by a reader who skims headings, and the scope limit is the single most important thing an applied piece says.
- **Estimated scope**: Short. A promotion and light rewrite, not new argument. `refine-draft`.
- **Not a defect to over-report**: the two Title Case renderings of "What This Implies for Decisions" (A6, A7) versus sentence case (A1, A5) are cosmetic — the Hugo anchor slug is identical either way, so nothing is broken. Mentioned only so a future reviewer does not mint a task for it.

#### An applied-mode entry-point paragraph on [apex/apex.md](/apex/) or the site index

- **Builds on**: the index's own claim that applied apex are where a reader should start for action-guidance.
- **Would address**: the applied wing is discoverable only by reading 838 lines into `apex-articles.md`. Four articles that answer "what should I do?" have no shared front door.
- **Estimated scope**: Short.

### Ideas for Later

- **A5 has a cross-register narrowness it names but does not fix.** Its own scope section concedes the ranking "is drawn almost entirely from one register" and that its two cross-register consequences "are samples rather than a survey." A future pass could widen it to the individuation, agency and scope registers — but this is genuinely hard work, and A5 is already at `soft_warning` (4468 words), so it likely wants a sibling rather than growth.
- **A1 is at `hard_warning` (5037 words, 1037 over soft).** Not urgent — the length is carried by the honest-verdict-scope and Birch-accounting passages, which are the article's best material and should not be cut. If it grows further, the quantum-hardware per-class verdicts are the natural extraction candidate, since `topics/quantum-hardware-and-the-ai-consciousness-coupling` already holds them.
- **Register the within-subject-scaling bet A7 says the Map owes.** Already queued as an existing P3 task; noted here only to confirm the optimistic reading agrees it is worth doing — A7's "The Map should say plainly which of these it is betting on, and currently it has not" is an invitation to `positions-evolve`, not a defect.

## Cross-Linking Suggestions

The applied set is not the connected subgraph the index implies. Measured link matrix among the four:

| From | To | Links |
|---|---|---|
| A5 research-programme | A1 assessing-ai | 3 |
| A1 assessing-ai | A5 research-programme | 1 |
| A7 judging | A5 research-programme | 2 |
| A6 embodied-interface | *(any applied sibling)* | **0** |
| A5, A1 | A7 judging | **0** |
| *(any)* | A6 embodied-interface | **0** |

A1↔A5 is reciprocal as documented. A7→A5 is one-way. **A6 is fully isolated from the wing.**

| From | To | Reason |
|------|-----|--------|
| `apex/embodied-interface` | `apex/assessing-ai-consciousness-under-the-map` | The highest-value missing edge. A6's decision 3 is *about* AI candidate-consciousness assessment and says "The right question is never 'is it conscious?' but 'which of the three statuses, if any, does the evidence support?'" — a disaggregation A1 needs and does not have. A1 currently frames its verdict as a single probability on a single question. |
| `apex/assessing-ai-consciousness-under-the-map` | `apex/embodied-interface` | Reciprocal. A1's scope paragraph already distinguishes bare phenomenality from bidirectional coupling; A6's three-way distinction is the finer-grained version of the same discipline and would strengthen A1's "separate presentation from selection before drawing any verdict" recommendation. |
| `apex/research-programme-decisions-under-the-map` | `apex/judging-the-map-as-science` | A7 links to A5 but not back. A5 ranks research directions; A7 supplies the appraisal verdict ("not degenerating, but not yet demonstrably progressive either") that tells a reader what the ranking is currently buying. A5's Direction 4 psychophysics recommendation especially wants A7's guard against reading a falsifiable prediction as empirical support. |
| `apex/judging-the-map-as-science` | `apex/assessing-ai-consciousness-under-the-map` | A7's measurement-standards limit — that no interpersonal phenomenal calibration is constructible — bears directly on A1's decision 5 about behavioural assay design, and A7's own decision 4 already names "AI-assessment contexts" without linking the article that does them. |
| `apex/embodied-interface` | `apex/judging-the-map-as-science` | A6 grades its supporting positions at "grade D" on the external-evidence axis; A7 is the article that explains what evidence grading is for and why framework-internal coherence does not substitute. |

## New Concept Pages Needed

None. This wing is a synthesis layer over existing concepts, and every term it leans on — `evidential-status-discipline`, `phenomenal-presentation`, `gaming-problem`, `reflexive-methodology`, `scale-types-for-phenomenal-quantities`, `phenomenal-contrast-method` — already has a page. `concepts/` is at 319/320 in any case; the honest finding is that this wing needs no new concepts, only the three applied apex the index already proposed.

## Calibration Note

Per this skill's design, the Process Philosopher and Hardline Empiricist personas were run against each other on every article in the wing. **They did not conflict anywhere.** A6's presentation category is the test case — maximally Whitehead-friendly, and the article uses it to *narrow* the causal claim rather than to widen any evidential tier. Per the skill's own criterion ("If the two personas converge in praising the same passage, the article has resolved the tension honestly"), the applied wing passes.

No `refine-draft` task is warranted on calibration grounds. The tasks generated below are structural and additive.