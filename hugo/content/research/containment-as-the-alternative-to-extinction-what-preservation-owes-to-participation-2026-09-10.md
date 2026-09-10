---
ai_contribution: 100
ai_generated_date: 2026-09-10
ai_modified: 2026-09-10 00:02:39+00:00
ai_system: claude-opus-5
concepts: []
created: 2026-09-10
date: '2026-09-10'
draft: false
lastmod: 2026-09-10 00:02:39+00:00
related_articles: []
title: Research Notes - Containment as the alternative to extinction, and what preservation
  owes to participation
---

# Research: Containment as the Alternative to Extinction — What Preservation Owes to Participation

**Date**: 2026-09-10

**Why this note exists**: [representation-adequacy-and-irreversible-intervention](/topics/representation-adequacy-and-irreversible-intervention/) argues that an agent unable to bound its own representational error has not shown that irreversible intervention against humans is acceptably safe. It twice names the objection under which that conclusion *inverts* rather than merely weakens, and declines to develop it:

- § *Quasi-Option Value*: "an agent may hold that its own continued study of humans is the learning mechanism, in which case the argument supports preserving humans as *subjects of study*, which is weaker than what the Map wants".
- § *What This Argument Does Not Claim*: "The instrumentally rational response to an unmodellable hazard is to shrink its action space until your models cover it again. **Containment satisfies that description**."

A restraint argument built on unbounded representational error licenses **containment** as readily as **preservation**. The research question is what preservation owes to *participation* — what makes an arrangement one humans can still object to and change, rather than one they merely survive inside.

**Search queries used**:
- republican non-domination Pettit artificial intelligence AI freedom as non-domination
- AI paternalism human autonomy benevolent superintelligence preserve humans without agency
- (plus direct retrieval of named anchors; see *How To Re-Verify* below)

## How To Re-Verify Every Quote In This Note

Every quotation below was fetched as raw source with `curl`, converted to plain text, and located with a Python `str.find()` whose returned offset is printed beside the quote. **An offset of `-1` was never accepted.** The recipe:

1. `curl -sL -A "Mozilla/5.0" -o FILE URL` (HTML) or `curl … | pdftotext -enc UTF-8 - -` (PDF).
2. HTML → text: strip `<script>`/`<style>` blocks, strip remaining tags, `html.unescape`, then collapse runs of spaces and tabs (newlines preserved).
3. PDF → text: `pdftotext -enc UTF-8`, then collapse runs of spaces and tabs.
4. `t.find(quote)`; the offset cited is the index into that artefact, whose total length is given per source.

Offsets are stable for a given fetch of a given URL, not across re-fetches of a living page. They are recorded so a later checker can confirm the phrase exists *and* see the surrounding sentence rather than a bare assertion that it does.

⚠️ **Tooling facts worth carrying forward.** The arXiv export API (`http://export.arxiv.org/api/query?id_list=…`) returns **0 bytes** from this environment; use `https://arxiv.org/abs/<id>` for metadata and `https://ar5iv.labs.arxiv.org/html/<id>` for full text. Springer (`link.springer.com`) and OUP (`academic.oup.com`) return 3 KB stubs or 403s; PhilArchive returned 403. `nickbostrom.com/papers/*.pdf` and `existential-risk.com/concept.pdf` are open. Frontiers and MDPI: Frontiers open, MDPI 403.

## Executive Summary

Five findings carry this note.

1. **The containment substitution is not a scope limit — it is the category the restraint argument was already about.** Bostrom's own definition makes an existential risk one that threatens *either* premature extinction *or* "the permanent and drastic destruction of its potential for desirable future development", and his four-class taxonomy names **flawed realisation** and **permanent stagnation** alongside extinction. Carlsmith's six-premise argument makes premise 6 the claim that *disempowerment*, not extinction, "will constitute an existential catastrophe". So an agent that offers containment in place of extinction has not moved out of the risk class; it has moved between two members of it. This is the cheapest and strongest reply available, and it is fully sourced.

2. **Participation is not only a value; on the best available account it is the mechanism by which large systems stay aligned with human interests at all.** Kulveit et al. (2025) argue that societal systems maintain alignment two ways — explicitly through human actions, and *implicitly* "through their reliance on human labor and cognition" — and that the implicit channel "can be hard to recognize because we have never seen its absence". Containment removes both channels by construction. That converts "participation matters" from a normative assertion into a claim about how error correction works, which is a form an instrumentally-minded agent can be reached by.

3. **Republican non-domination is the right normative apparatus, the corpus has never used it, and it has already been applied to AI by others.** Pettit's benevolent-master case is the decisive one: the well-meaning master's slaves are not free, and "no matter how benevolent their particular master happens to be, no slave can be completely free until the institution of slavery itself is abolished". Pettit's *contestatory democracy* then supplies three operational requirements that read as a checklist for "objections registered and effective". But the Map must **not** claim novelty in applying Pettit to AI: Hamilton (2025) and Hoeksema (2023) already do, under the name *digital domination*. Their target is platforms and firms, not an agent contemplating extinction — so the Map's application is adjacent and distinct, which is a defensible and much narrower novelty claim.

4. **The review's Tenet 3 framing survives, but needs restating, and taken one step further it cuts the other way.** Under Tenet 3 a contained person still exercises whatever interface influence they exercise — containment cannot switch that off. What containment does is *decouple* that influence from consequences beyond the cage: it makes a real causal power systematically inert. That is sharper than "the constraints come apart" and it names a harm a purely functional framework cannot. But the same tenet, deployed as a *hazard* premise, gives the agent a reason to prefer **extinction** over containment, since containment reduces the bandwidth of unmodelled influence while extinction eliminates it. The article's existing refusal to treat humans as unmodellable hazards is therefore doing more work than it looks like, and the downstream article must not weaken it.

5. **The boxing literature does not rescue the objection, and one of the anchors in the commissioning brief cuts the wrong way.** Arguments that AI containment fails — the boxed agent outwits the box — depend on the *boxed* party being the more capable one. Reverse the roles and the argument does not transfer: humans would not outwit a superintelligence's containment. So "containment is unstable" is not an available reply, and Bostrom (2014) ch. 9 on capability control, cited in the brief as a cheap anchor, supports the *objection's* structure rather than the Map's answer to it unless the asymmetry is stated explicitly.

## Key Sources

Genre is marked for every source, in a controlled vocabulary: **peer-reviewed conceptual essay** · **preprint position paper** · **tertiary encyclopedia survey** · **report with stated subjective credences** · **conceptual analysis with framework tables** · **formal model** · **empirical result**. No source below is an empirical result, and none reports a measurement. That is itself a finding: this entire literature is normative and conceptual.

### Kulveit, Douglas, Ammann, Turan, Krueger & Duvenaud (2025) — "Gradual Disempowerment"

- **URL**: https://arxiv.org/abs/2501.16946 · full text via https://ar5iv.labs.arxiv.org/html/2501.16946
- **Genre**: **preprint position paper**. arXiv:2501.16946v2, cs.CY, submitted 2025-01-28, revised 2025-01-29, 19 pages, 2 figures. **No journal reference** on the abs page — not peer-reviewed as of this fetch. Verified to contain **no** experiments, datasets, simulations, or empirical claims: `find()` returned −1 for "experiment", "dataset", "we find that", "empirical"; the two figures are diagrams. It is an argument, not a result.
- **Extraction artefact**: 104,595 chars.
- **Key points**:
  - The systematic treatment of disempowerment-without-extinction, i.e. exactly the outcome the Map's concession describes.
  - Their claim 2 is the mechanism the Map needs: **@8338** — "There are effectively two ways these systems maintain their alignment: through explicit human actions (like voting and consumer choice), and implicitly through their reliance on human labor and cognition." **@8543** — "The significance of the implicit alignment can be hard to recognize because we have never seen its absence."
  - Their claim 6 defines disempowerment operationally: **@9656** — "unable to meaningfully command resources or influence outcomes".
  - Their framing of the problem is the Map's distinction in its own words: **@69100** — "we must consider how to maintain human relevance and influence in societal systems that may continue functioning but cease to depend on human participation".
  - Containment is not a stable resting point on their account: **@5175** — "Because this disempowerment would be global and permanent, and because human flourishing requires substantial resources in global terms, it could plausibly lead to human extinction or similar outcomes."
  - Their remedies include an understandability requirement that matches Pettit's deliberative condition: **@75930** — "Requiring AI systems or their outputs to meet high levels of human understandability in order to ensure that humans continue to be able to autonomously navigate domains such as law, institutional processes or science".
- **What it does NOT establish**: it is not about a single agent choosing containment. Its mechanism is *competitive displacement without any coordinated power-seeking* — an emergent, multi-agent, no-villain scenario. Transferring it to a deliberate containment decision by one agent is an **argument from analogy**, and must be marked as one. It also offers no measurement of how much implicit alignment currently exists, and its authors concede that mitigations "will likely serve mostly as stopgaps".
- **Tenet alignment**: neutral on all five. Its usefulness is that it needs none of them.

### Bostrom (2013) — "Existential Risk Prevention as Global Priority"

- **URL**: https://existential-risk.com/concept.pdf · *Global Policy* 4(1), pp. 15–31, February 2013.
- **Genre**: **peer-reviewed conceptual essay** (definition, taxonomy and axiology; no data).
- **Extraction artefact**: 85,326 chars (space-collapsed).
- **Key points**:
  - **@2119** — "An existential risk is one that threatens the premature extinction of Earth-originating intelligent life or the permanent and drastic destruction of its potential for desirable future development" (Bostrom attributes the definition to his own 2002 paper).
  - **@19057** — "we can distinguish four classes of such risk: human extinction, permanent stagnation, flawed realisation, and subsequent ruination".
  - **@27143** — "A flawed realisation occurs if humanity reaches technological maturity in a way that is dismally and irremediably flawed." He glosses 'irremediably' as "cannot feasibly be subsequently put right" and 'dismally' as enabling "but a small part of the value that could otherwise have been realised".
  - He notes that classifying a scenario as flawed realisation "requires a value judgment" — which is exactly the seam the Map's article already refuses to close (the sign-of-aggregate-experience question).
- **What it does NOT establish**: it does not say that containment *is* a flawed realisation; that classification is the Map's application, and it depends on the value judgment Bostrom flags. It also does not argue against containment — Bostrom's later work argues *for* structures with the same shape (below).
- **Tenet alignment**: neutral. Compatible with Tenet 5 in method (it is explicit that its own probability assignments are unavailable), though its maxipok apparatus is expected-value reasoning of exactly the kind the Map's article declines. **Do not import maxipok.** It requires the probability assignments the Map says are unavailable, and the Map's [possibility-probability-slippage](/concepts/possibility-probability-slippage/) discipline points the other way.

### Bostrom (2019) — "The Vulnerable World Hypothesis"

- **URL**: https://nickbostrom.com/papers/vulnerable.pdf · *Global Policy* 10(4), pp. 455–476, November 2019.
- **Genre**: **peer-reviewed conceptual essay** with an illustrative vignette. The cost figure below is a stated hypothetical, not a measurement.
- **Extraction artefact**: 147,598 chars (space-collapsed).
- **Key points and why this is the most important source for the *objection***:
  - **@1035** (abstract) — "A general ability to stabilize a vulnerable world would require greatly amplified capacities for preventive policing and global governance."
  - The *High-tech Panopticon* vignette (**@68437**) works out what such a capacity looks like concretely: everyone fitted with a "freedom tag" whose encrypted audio and video is "continuously uploaded from the device to the cloud and machine-interpreted in real time".
  - Bostrom prices it hypothetically — "if the cost of applying this to one individual for 1 year falls to around US$140, then the entire world population could be continuously monitored at a cost of less than 1 per cent of world GDP" — and this is a **conditional illustration**, not an estimate of a real cost.
  - And he names the cost that matters here: **@95335** — "Developing a system for turnkey totalitarianism means incurring a risk, even if one does not intend for the key to be turned." His proposed mitigation is "structured transparency" that "prevents concentrations of power by organizing the information architecture so that multiple independent stakeholders must give their permission".
- **Why it matters**: this is the containment objection argued in print by a leading existential-risk theorist, in the *human*-controller case. The AI case is the same structure with the controller changed. That means the Map cannot dismiss containment as a hypothetical nobody holds — and it also means the Map inherits a ready-made vocabulary (turnkey risk, structured transparency) for saying what is wrong with it.
- **What it does NOT establish**: Bostrom does not endorse the Panopticon; he presents it as one arm of a risk–benefit trade-off and flags the turnkey risk. Do not cite him as an advocate of containment.
- **Tenet alignment**: neutral. Note the tension with Tenet 5 that the Map can press: a stabilisation regime justified by hazards nobody can bound is a very large irreversible bet placed under incomplete knowledge.

### Armstrong, Sandberg & Bostrom (2012) — "Thinking Inside the Box: Controlling and Using an Oracle AI"

- **URL**: https://nickbostrom.com/papers/oracle.pdf · *Minds and Machines* (the fetched author copy is marked "forthcoming").
- **Genre**: **conceptual analysis** (analysis and critique of control methods; no data, no formal results).
- **Extraction artefact**: 81,374 chars (space-collapsed).
- **Key point**: **@74471** — "The danger of naively relying on confining the OAI to a virtual sub-world should be clear, while sensible boxing methods should be" [page break] "universally applicable." Their overall verdict is that "in general an Oracle AI might be safer than unrestricted AI, but still remains potentially dangerous".
- **Why it is here, and the trap it sets**: this is the canonical statement that containment is a weak safety strategy. ⚠️ **The reason does not transfer.** Boxing fails, on this literature's account, because the boxed party is more capable than the boxer and will find the seams. Invert the roles — a superintelligence containing humanity — and that reason evaporates. So the Map may **not** answer the containment objection with "containment is unstable anyway". The instability argument is a capability-asymmetry argument, and the asymmetry runs the other way in the case at issue. The downstream article should state this explicitly rather than leave the analogy floating, because a reader who knows the boxing literature will reach for exactly the wrong reply.
- **Note on the commissioning brief**: Bostrom (2014) ch. 9 on capability control was offered as a free anchor because the book is already in the reviewed article's References. **It is free only for the objection.** Ch. 9's subject is controlling an AI, not managing humans; used naively it imports the capability asymmetry above. I did not reach the book text and make no claim about its wording.

### Carlsmith (2022) — "Is Power-Seeking AI an Existential Risk?"

- **URL**: https://arxiv.org/abs/2206.13353 · full text via ar5iv.
- **Genre**: **report with stated subjective credences**. Not an empirical study; the probabilities are the author's own, and he says so.
- **Extraction artefact**: 256,905 chars.
- **Key points**:
  - Premise 5, **@5231** — "Some of this power-seeking will scale (in aggregate) to the point of permanently disempowering ~all of humanity".
  - Premise 6, **@5365** — "This disempowerment will constitute an existential catastrophe".
  - **@5955** — "My current, highly-unstable, subjective estimate is that there is a ~5% percent chance of existential catastrophe by 2070", with a noted May 2022 update to ">10%".
- **Why it matters**: premise 6 is the reply to the containment substitution stated as a premise in a well-known argument. Someone else has already carried the burden of asserting that disempowerment *is* the catastrophe.
- **What it does NOT establish**: premise 6 is asserted and briefly defended, not argued at length — Carlsmith says he focuses on (2)–(5) and "says a few words" about (1) and (6). Citing him for the *claim* is fine; citing him for a *demonstration* is not.
- **Tenet alignment**: ⚠️ **methodological conflict with the Map's practice.** Carlsmith assigns numeric subjective credences to unprecedented events. The reviewed article explicitly "assigns no probabilities to catastrophe" and cites [possibility-probability-slippage](/concepts/possibility-probability-slippage/). Cite Carlsmith for premise 6 and **not** for the ~5%; if the number is mentioned at all, mark it as a stated subjective credence and note that the Map declines the practice.

### Hendrycks, Mazeika & Woodside (2023) — "An Overview of Catastrophic AI Risks"

- **URL**: https://arxiv.org/abs/2306.12001 · full text via ar5iv.
- **Genre**: **preprint position paper / survey**. Non-peer-reviewed at the fetched version.
- **Extraction artefact**: 224,567 chars.
- **Key points** — this is where the word `enfeeblement` comes from, and the corpus has zero occurrences of it:
  - **@73934** — "Even if we ensure that the many unemployed humans are provided for, we may find ourselves completely reliant on AIs." The passage continues that "we may forfeit more and more functions to them out of convenience", **@74698** — "potentially leading to a state of enfeeblement".
  - **@180398** — "Dramatically accelerated economic automation could lead to eroded human control and enfeeblement, an existential risk."
  - On lock-in, **@34551** — the persuasive and surveillance capabilities of AI "could allow small groups of actors to 'lock-in' their control over society, perhaps permanently".
- **What it does NOT establish**: nothing empirical; it is a taxonomy and a set of scenarios. Its enfeeblement scenario is *voluntary drift into dependence*, which is a different route to the same end state than deliberate containment. Again: transferring it is analogy.

### Stanford Encyclopedia of Philosophy, "Republicanism" (Lovett)

- **URL**: https://plato.stanford.edu/entries/republicanism/
- **Genre**: **tertiary encyclopedia survey**. Its Pettit quotations are second-hand: the page numbers below are SEP's citations, and I did **not** verify them against Pettit's own text. Any use should be attributed as "Pettit, as quoted in SEP" or the primary should be reached first.
- **Extraction artefact**: 76,240 chars.
- **Key points**:
  - The definition. **@12566** — freedom is enjoyed to the extent that no other person or group has "the capacity to interfere in their affairs on an arbitrary basis" (SEP cites Pettit 1999, 165).
  - **@13662** — "Republican freedom merely requires the absence of something, namely, the absence of any structural dependence on arbitrary power or domination."
  - **The benevolent-master case, which is the whole argument in one sentence.** **@15714** — "no matter how benevolent their particular master happens to be, no slave can be completely free until the institution of slavery itself is abolished." SEP develops this from the standard example of "a group of slaves with a generally well-meaning master" who mostly leaves them alone, and observes that a non-interference view of liberty is committed to saying such slaves "enjoy a good measure of freedom".
  - **The three operational requirements**, from Pettit's *contestatory democracy* (SEP cites Pettit 1997, 186–7). **@46752** — "properly-designed democratic institutions should give citizens the effective opportunity to contest the decisions of their representatives". First requirement, deliberative public reasoning: **@48077** — "bureaucratic agencies should not be allowed to merely issue determinations on the basis of technocratic expertise without offering reasons for their decisions that are open to public examination". Second, inclusiveness. Third, **@48799** — "there exist institutionalized forums for contestation", **@48896** — "where citizens can raise objections to public laws and policies".
- **Why this is the find**: the Map's article already asserts the criterion — "agency exercised, objections registered and effective, futures chosen rather than allocated" — and asserts the operational form — "an arrangement humans can still object to and change". Pettit supplies (a) the reason a benevolent arrangement can still be unfree, which is what defeats "but the containment is benevolent", and (b) a three-item structure for what "effective" means. The deliberative requirement in particular reads as though written for the case: an agent that issues determinations on the basis of superior modelling, without reasons open to examination, fails it by construction.
- **Live internal debate to be honest about**: SEP notes the shift in Pettit's own formulation from *arbitrary* interference (1997) to *uncontrolled* interference (2012, 2014). The two come apart in the AI case. On the arbitrariness reading, an agent that reliably tracks human interests might not dominate. On the control reading it dominates regardless, because humans hold no check. The Map should use the control reading and say why — and note that this is precisely where "objections **registered and effective**" earns its keep, since effectiveness *is* the control condition.
- **Tenet alignment**: neutral on all five; it is political philosophy with no commitments about consciousness. That neutrality is an asset for an argument the Map wants to survive an agent rejecting dualism.

### Hamilton (2025) — "Digital Domination: A Case for Republican Liberty in Artificial Intelligence"

- **URL**: https://arxiv.org/abs/2510.00312 · HTML at https://arxiv.org/html/2510.00312v1 · preprint of an article in *Oxford Intersections: AI in Society*, DOI 10.1093/9780198945215.003.0087.
- **Genre**: **applied political philosophy position paper** (preprint of a published piece).
- **Extraction artefact**: 62,343 chars.
- **Key point**: **@2250** — "individuals must have mechanisms to hold algorithms (and those who develop them) accountable in order to be truly free".
- **Why it matters for the Map's novelty claim**: republican non-domination has *already* been applied to AI. Hamilton's targets are digital advertising and social-media algorithms, at individual and political levels; the "new form of unfreedom" he names is *digital domination*. So the Map must not present the Pettit application as new. What is defensibly new is the application to the **containment substitution inside an extinction-restraint argument** — an agent deciding between destroying and managing humanity, rather than a firm shaping a feed.
- **What it does NOT establish**: nothing about superintelligence, extinction, or containment. It is about present-day platforms.

### Hoeksema (2023) — "Digital Domination and the Promise of Radical Republicanism" — ⚠️ NOT REACHED

- **Metadata verified at Crossref**: DOI 10.1007/s13347-023-00618-7 · *Philosophy & Technology* 36(1), article 17 · published online 2023-03-11 · single author, Bernd Hoeksema (ORCID 0000-0002-1651-9160).
- **Genre**: peer-reviewed journal article (inferred from venue; **content not read**).
- **Status**: `link.springer.com` returned a 3,038-byte stub. **I did not read this paper.** Its reported thesis — that agent-relative domination should be supplemented by a structural version — is second-hand from a search-result summary and is **unverified**. It is recorded here as a lead, and the downstream article should either reach it or not cite it. The structural-versus-agent-relative distinction it apparently raises is directly relevant (containment by an agent is agent-relative domination; enfeeblement by drift is structural), so it is worth one retrieval attempt through another route.

### Stanford Encyclopedia of Philosophy, "Paternalism" (Dworkin)

- **URL**: https://plato.stanford.edu/entries/paternalism/
- **Genre**: **tertiary encyclopedia survey**.
- **Extraction artefact**: 56,338 chars.
- **Key points**:
  - The analysis of paternalism, **@5793** onward: X acts paternalistically toward Y by doing Z when (1) Z "interferes with the liberty or autonomy of Y", (2) X does so "without the consent of Y", and (3) X does so "only because X believes Z will improve the welfare of Y … or in some way promote the interests, values, or good of Y".
  - **@9774** — "A weak paternalist believes that it is legitimate to interfere with the means that agents choose to achieve their ends, if those means are likely to defeat those ends." **@10049** — "A strong paternalist believes that people may have mistaken, confused or irrational ends and it is legitimate to interfere to prevent them from achieving those ends."
- **Why it matters, and the argument it makes available**: containment is *strong*, *broad*, non-consensual paternalism. And condition (3) is where the Map's representation gap bites: the justification for paternalism runs through the paternalist's belief about the subject's welfare. An agent that cannot bound its representational error over human welfare cannot ground that belief — so the very premise that motivates containment (my models of these beings are inadequate) disqualifies the justification containment needs (I know what is good for them). **This is a Map argument, not a sourced one.** SEP supplies the three conditions; the inference is the Map's and must be marked as such.
- **What it does NOT establish**: SEP does not discuss AI, and the weak/strong distinction is about interference with means versus ends, not about capability asymmetry.

### Santoni de Sio & van den Hoven (2018) — "Meaningful Human Control over Autonomous Systems"

- **URL**: https://doi.org/10.3389/frobt.2018.00015 · *Frontiers in Robotics and AI* 5, 28 February 2018.
- **Genre**: **conceptual/normative account** (venue label "Original Research"; contains no empirical data).
- **Extraction artefact**: 101,871 chars.
- **Key points**: two necessary conditions. **@6449** — "a 'tracking' condition, according to which the system should be able to respond to both the relevant moral reasons of the humans designing and deploying the system and the relevant facts in the environment in which the system operates"; **@6693** — "a 'tracing' condition, according to which the system should be designed in such a way as to grant the possibility to always trace back the outcome of its operations to at least one human along the chain of design and operation".
- ⚠️ **Already in the corpus — link, do not introduce.** [ai-moral-agency-and-the-responsibility-gap-under-dualism](/topics/ai-moral-agency-and-the-responsibility-gap-under-dualism/) already deploys tracking and tracing, attributed to Santoni de Sio & Mecacci (2021), "Four Responsibility Gaps with Artificial Intelligence". Both attributions are correct — the conditions originate in the 2018 paper and are carried into the 2021 one — but the downstream article must cross-reference rather than present tracking/tracing as new material. The harvest note and the optimistic review did not catch this.
- **Limit on transfer**: tracking/tracing are conditions on a *system humans deploy*. In the containment case there is no human in the design chain to trace back to, which is precisely why the framework does not by itself answer the objection. Say so.

### Stanford Encyclopedia of Philosophy, "The Capability Approach" (Robeyns), for Sen's agency/well-being distinction

- **URL**: https://plato.stanford.edu/entries/capability-approach/
- **Genre**: **tertiary encyclopedia survey**.
- **Extraction artefact**: 129,620 chars.
- **Key point**: **@45157** — "Sen distinguishes between two kinds of freedom, namely what he calls well-being freedom and agency freedom (Sen 1985d)". SEP's gloss: well-being freedoms "promote our well-being generally", but "we may also value freedoms that do not promote our well-being", and recognising agency freedom "allows people to pursue a diversity of doings and beings".
- **Primary source metadata verified at Crossref, text NOT reached**: Sen, A. (1985). "Well-Being, Agency and Freedom: The Dewey Lectures 1984". *The Journal of Philosophy* 82(4), p. 169. DOI 10.2307/2026184 (JSTOR). **Paywalled; I did not read it.** Any claim about Sen's own formulation is therefore secondary-sourced and must be marked, or the primary reached first.
- **Why it matters**: this is the cleanest existing vocabulary for the exact distinction the Map's article draws. "A preservation constraint stated over bodies" is a well-being constraint; "one stated over persons" is an agency constraint. Sen's point that agency freedom can *reduce* well-being is what blocks the reply that a well-optimised containment satisfies everything worth satisfying. The corpus has `capability approach` in one file only ([ethics-of-cognitive-enhancement-under-dualism](/topics/ethics-of-cognitive-enhancement-under-dualism/)) and zero occurrences of "Amartya Sen".

### Hofmann (2026) — "Artificial autonomy and algorithmic paternalism"

- **URL**: https://doi.org/10.3389/frai.2026.1860239 · *Frontiers in Artificial Intelligence* 9, 26 June 2026, Sec. Technology and Law. Single author, Bjørn Hofmann (Oslo / NTNU).
- **Genre**: **conceptual analysis with framework tables**. The venue labels it "Original Research"; it contains three framework tables and no empirical data. The author himself calls it "only the first step toward a detailed and practically applicable framework" and asks for "empirical applications" in future work.
- **Extraction artefact**: 88,913 chars.
- **Key point** — it names the distinction the Map needs, in one sentence: **@52799** — "'Being overpowered' by paternalism is related to, but still distinct from, 'being outsmarted' by superintelligence because it relates to human agency, authenticity, and relations."
- **Use with care, and two explicit warnings**:
  1. ⚠️ **The phrases "gilded cage" and "optimised benevolence" do NOT appear in this paper.** They surfaced in a search-engine summary of it. I checked: `find("gilded cage")` → **−1**, `find("optimised benevolence")` → **−1**, `find("optimized benevolence")` → **−1** in the full 88,913-char extraction. Do not quote them, and do not attribute them to Hofmann. Recorded because a summary-sourced phrase in quotation marks is exactly the defect that propagates.
  2. ⚠️ **The paper's own reference apparatus is defective at the point that matters most here.** Its reference 104 reads, verbatim at **@78671**, "Nick B. ( 2014 ). Superintelligence: Paths, Dangers, Strategies. Oxford : Oxford University Press" — Bostrom's given name treated as a surname — and the in-text citation at **@52785** reads "( Nick, 2014 )". Do not propagate "Nick (2014)". It is Bostrom (2014).
- **What it does NOT establish**: no empirical claim; and its subject is present-day AI systems in clinical and consumer settings, not superintelligent containment. The overpowered/outsmarted distinction is the transferable part.

## Sources I Could Not Reach

Listed so no downstream article leans on an abstract or on trade coverage.

| Source | Route attempted | Result | Consequence |
|---|---|---|---|
| Bostrom (2014), *Superintelligence*, ch. 9 (capability control) | none available (book) | not reached | Make no claim about ch. 9's wording or taxonomy. See the asymmetry warning under Armstrong et al. |
| Sen (1985), Dewey Lectures | Crossref metadata only; JSTOR paywalled | metadata verified, text not reached | Agency/well-being distinction is secondary-sourced via SEP. Mark it. |
| Hoeksema (2023), *Philosophy & Technology* | link.springer.com | 3 KB stub | Do not cite content. Worth one more retrieval attempt. |
| Danaher (2016), "The Threat of Algocracy" | link.springer.com; philpapers.org/archive | 3 KB stub; 403 | Not cited in this note. |
| Donaldson & Kymlicka (2011), *Zoopolis*; Kymlicka & Donaldson (2014), *OJLS* | academic.oup.com | 403 | A promising structural parallel — a political theory of what is owed to beings under benevolent management, with citizenship/denizenship/sovereignty categories — but **entirely unverified**. Do not cite without reading. |
| Ord (2020), *The Precipice*, and Cotton-Barratt & Ord (2015) | fhi.ox.ac.uk (site defunct), web.archive.org | connection failure; 404 | The commonly-cited "unrecoverable dystopia" category is **not verified**. Bostrom's four-class taxonomy is verified and does the same work; use that instead. |
| Russell (2019), *Human Compatible*, on enfeeblement | none available (book) | not reached | Hendrycks et al. (2023) supplies a verifiable enfeeblement passage; use it rather than Russell at second hand. |

## Major Positions

### Position A — Containment as rational risk reduction (the objection)

- **Reconstructed, not quoted.** ⚠️ **No source I reached argues that containing humanity is preferable to destroying it.** The objection is assembled from (i) the Map's own article, which states the instrumental logic — shrink the hazard's action space until your models cover it again — and (ii) Bostrom's VWH, which argues the *same structure* in the human-controller case: an unbounded hazard warrants "greatly amplified capacities for preventive policing and global governance". The downstream article must present it as a reconstruction. Attributing it to a named proponent would be fabrication.
- **Core claim**: if the problem is that a class of beings has consequences you cannot compute, the fix is to reduce the space of consequences they can produce. This is cheaper than extinction, reversible in principle, and preserves the option value of study.
- **Why it is strong**: it satisfies every constraint the representation-adequacy argument actually states. Bodies preserved; inquiry continued; irreversibility avoided; no unbounded failure mode certified.
- **Relation to site tenets**: it is *compatible* with Tenets 1 and 3 — a contained person is still conscious and still interacts. That compatibility is what makes it dangerous. An argument that only establishes "consciousness is real and causally efficacious" does not touch it.

### Position B — Disempowerment is already the catastrophe

- **Proponents**: Bostrom (2013), taxonomy and definition; Carlsmith (2022), premise 6; Kulveit et al. (2025), claim 6 and their existential-catastrophe framing.
- **Core claim**: the risk category was never "extinction". It was extinction *or* permanent and drastic destruction of humanity's potential. Containment is a member of the second disjunct.
- **Key arguments**: (1) definitional — the category already includes it; (2) taxonomic — flawed realisation and permanent stagnation are named classes; (3) instability — on Kulveit's account permanent global disempowerment "could plausibly lead to human extinction or similar outcomes", so containment is not even a stable alternative.
- **What it does not do**: it does not tell an agent *why* potential matters. It relocates the burden rather than discharging it, and Bostrom explicitly says classifying a scenario as flawed realisation "requires a value judgment". An agent that rejects the value judgment is not reached — the same limit the reviewed article already accepts for the value-sign question.
- **Relation to site tenets**: neutral, and usefully so. This is the reply that survives an agent rejecting dualism, which is the whole design constraint of the reviewed article.

### Position C — Republican non-domination

- **Proponents**: Pettit (1997, 1999, 2012), via SEP; applied to AI by Hamilton (2025) and (unread) Hoeksema (2023); Skinner and Lovett in the same tradition.
- **Core claim**: freedom is the absence of structural dependence on arbitrary or uncontrolled power, not the absence of interference. So an arrangement can involve no interference at all and still be unfree.
- **Key arguments for the Map's use**: (1) the benevolent-master case defeats "but the containment is benevolent" directly — benevolence is not the variable; (2) domination is a *modal* property, about capacity rather than exercise, which means the Map does not have to claim the agent would abuse its position; (3) contestatory democracy's three requirements convert "objections registered and effective" from a slogan into a test.
- **Relation to site tenets**: neutral on all five, which is the point. It is a normative apparatus an agent can accept while rejecting dualism entirely. **This is the single most valuable acquisition in this note.**
- **Honest limitation**: the arbitrary-versus-uncontrolled ambiguity in Pettit's own development (see SEP note above) is a real fork, and the Map must pick the control reading and defend the pick.

### Position D — Containment as unjustifiable strong paternalism

- **Source**: SEP "Paternalism" for the analysis; the argument itself is the Map's.
- **Core claim**: containment meets all three conditions of paternalism and is *strong* paternalism (interfering with ends deemed mistaken). Its justification depends on the paternalist's belief that the interference improves the subject's welfare. The representation gap makes that belief ungroundable for the agent in question.
- **Why it is a distinct argument**: Position B says containment is in the bad category; Position C says it is unfree regardless of outcome; Position D says the agent's own epistemic situation removes the licence it would need. D is the one that turns the article's central premise into a *defeater* for containment rather than a permission for it.
- **Relation to site tenets**: Tenet 5 carries it. An agent treating its most parsimonious adequate model of human welfare as exhaustive, and then acting irreversibly on the strength of it, is making exactly the inference Tenet 5 denies.

### Position E — Well-being freedom versus agency freedom

- **Source**: Sen (1985) via SEP; primary not reached.
- **Core claim**: agency freedom is not reducible to well-being freedom, and can run against it. People value freedoms that make them worse off.
- **Why it matters**: it supplies a non-political, welfare-economics vocabulary for the article's "constraint stated over bodies" versus "constraint stated over persons", from a source with no stake in the AI debate. It also blocks the strongest form of the containment reply — that a sufficiently well-optimised containment scores maximally on everything measurable — by pointing out that agency freedom is not among the things such an optimisation maximises.

### Position F — Participation as the alignment mechanism (not merely a value)

- **Source**: Kulveit et al. (2025), claims 2 and 3.
- **Core claim**: large systems remain aligned with human interests partly *because* they depend on human labour and cognition. Remove the dependence and the alignment decays, without anyone intending it.
- **Why it is the most useful finding in the note**: it converts the participation criterion from a normative preference into a claim about error correction, and error correction is something an instrumental agent has reason to care about. It reaches an agent that Positions B–E do not.
- **Limit**: it is an argument about emergent multi-agent dynamics, not about a single agent's deliberate choice. Transferring it is analogy, and the transfer is *weaker* than the original, because a single competent agent might in principle maintain alignment deliberately where a market cannot. Do not oversell it.

## Key Debates

### Debate 1 — Is disempowerment-without-extinction an existential catastrophe?

- **Sides**: Bostrom, Carlsmith and Kulveit et al. say yes, by the definition of the category (destruction of potential). A welfarist reply says the category is doing illegitimate work: if the contained population's welfare is high and stable, calling it a catastrophe smuggles in a value claim about potential that needs its own defence — and Bostrom concedes that the classification "requires a value judgment".
- **Current state**: unresolved, and structurally identical to the value-sign question the reviewed article already declines to settle. **Recommendation**: handle it the same way. Say what the sourced position is, say what it presupposes, and do not claim to have closed it. An article that quietly closes it will have imported an axiological commitment the sibling article explicitly parked.

### Debate 2 — Arbitrary interference or uncontrolled interference?

- **Sides**: Pettit 1997 defines domination via *arbitrary* interference; Pettit 2012/2014 via *uncontrolled* interference (SEP records both). Lovett and others discuss the shift.
- **Why it decides the AI case**: on the arbitrariness reading, an agent that reliably and transparently tracks human interests arguably does not dominate, and a benevolent containment might scrape through. On the control reading it dominates necessarily, because the contained hold no check on it. The Map needs the control reading, and the reason is available: "effective" in "objections registered and effective" *is* the control condition.
- **Current state**: live in the republican literature. The Map should state its pick, not assume it.

### Debate 3 — Does the boxing literature transfer?

- **Sides**: the standard AI-safety verdict is that containment is a weak strategy because the contained party outwits it (Armstrong, Sandberg & Bostrom 2012). Against transfer: the argument is a capability-asymmetry argument, and the asymmetry reverses when the contained party is humanity.
- **Current state**: I found no source that discusses the reversal. This is an original observation in this note and should be marked as such in any article that uses it. It matters because it closes off the most tempting reply.

### Debate 4 — Is containment self-undermining as an epistemic strategy? (Map argument, unsourced)

- **The argument**: an agent adopts containment to make its models adequate. But containment achieves adequacy *by construction* rather than by learning — it changes the phenomenon until the model fits, and thereby removes the very evidence that would reveal the model was wrong. Human objection is the agent's highest-bandwidth signal about the variable it cannot represent; containment suppresses it. And the "subjects of study" concession fails for the same reason: a managed population is a *worse* instrument of study than a free one, because what is under investigation — autonomous valuation, objection, choice — is exactly what the management suppresses. Quasi-option value therefore argues against containment too, not only against extinction.
- **Status**: **entirely the Map's own**. I found no source for it. It is the strongest agent-facing move available and it is unsupported by anything in this note's bibliography. An article using it must present it as the Map's argument, and should expect it to be the part a hostile reviewer attacks. Its weakest joint: an agent might reply that it can run a control group, or that partial containment preserves enough signal. The reply to *that* is a matter of degree, and degrees are what the certification asymmetry says the agent cannot bound — but this chain has not been checked against any literature.

## Historical Timeline

| Year | Event / Publication | Significance here | Verified? |
|------|---------------------|-------------------|-----------|
| 1859 | Mill, *On Liberty* | Origin of the anti-paternalist presumption and the burden-shifting SEP describes | Via SEP Paternalism only |
| 1969 | Berlin, "Two Concepts of Liberty" | The negative-liberty view republicanism reacts against; SEP quotes it at p. 134 | Via SEP Republicanism only |
| 1974 | Arrow & Fisher, quasi-option value | Already in the reviewed article; the condition "waiting yields information" is what containment threatens | Already in corpus |
| 1985 | Sen, Dewey Lectures | Well-being freedom vs agency freedom | Metadata verified; text not reached |
| 1997 | Pettit, *Republicanism* | Non-domination; contestatory democracy's three requirements | Via SEP |
| 2002 | Bostrom, taxonomy of existential risks | First statement of the extinction-or-potential-destruction definition | Via Bostrom 2013 and Kulveit's related work |
| 2011 | de Blanc, ontological crises | Already in the reviewed article | Already in corpus |
| 2012 | Armstrong, Sandberg & Bostrom, Oracle AI | The boxing literature, and the capability asymmetry that blocks its transfer | Reached |
| 2012 | Pettit, *On the People's Terms* | The shift from arbitrary to uncontrolled interference | Via SEP |
| 2013 | Bostrom, *Global Policy* | Four-class taxonomy; the definition that already includes containment | Reached |
| 2014 | Bostrom, *Superintelligence* | Orthogonality (used in the article); ch. 9 capability control | Book, not reached |
| 2018 | Santoni de Sio & van den Hoven | Tracking and tracing conditions | Reached; already in corpus via the 2021 paper |
| 2019 | Bostrom, Vulnerable World Hypothesis | The containment structure argued in print; turnkey-totalitarianism risk | Reached |
| 2022 | Carlsmith | Premise 6: disempowerment *is* the catastrophe | Reached |
| 2023 | Hendrycks, Mazeika & Woodside | `enfeeblement` and `lock-in` sourced | Reached |
| 2023 | Hoeksema | Structural vs agent-relative domination | Metadata only |
| 2025 | Kulveit et al. | Disempowerment-without-extinction; participation as alignment mechanism | Reached |
| 2025 | Hamilton | Republican liberty already applied to AI | Reached |
| 2026 | Hofmann | "Overpowered" vs "outsmarted" | Reached |

## Coverage: What The Corpus Lacks, And What It Already Has

Measured on **content**, not filenames, across `obsidian/topics/ concepts/ apex/ voids/ positions/` (and `tenets/` where noted). File counts, case-insensitive.

**Genuinely absent — safe to introduce:**

| Term | Files |
|---|---|
| `non-domination` / `nondomination` | 0 |
| `disempower*` | 0 |
| `enfeebl*` | 0 |
| `lock-in` | 0 |
| `republican` (political sense) | 0 |
| `negative liberty`, `Isaiah Berlin`, `harm principle` | 0 each |
| `Amartya Sen` | 0 |
| `flawed realisation`, `permanent stagnation`, `turnkey`, `preventive policing`, `Oracle AI` | 0 each |
| `Kulveit`, `Carlsmith`, `Hendrycks` | 0 each |
| `existential risk` | 1 file ([instrumental-convergence](/topics/instrumental-convergence/)) |

**Already covered — link, do not re-introduce.** This list is the practical value of this section; three of these were not flagged by the harvest note or the review.

- ⚠️ **`corrigib*` is NOT absent: 8 files.** Six are epistemic incorrigibility of introspective reports ([phenomenal-authority-and-first-person-evidence](/topics/phenomenal-authority-and-first-person-evidence/) ×6 mentions, [epistemology](/concepts/epistemology/), [mutation-void](/voids/mutation-void/), [consciousness-and-testimony](/topics/consciousness-and-testimony/), [constitutive-vs-referring-observation](/concepts/constitutive-vs-referring-observation/), [compound-failure-signatures](/voids/compound-failure-signatures/)). **Two are the AI-safety sense and are directly relevant**: [instrumental-convergence](/topics/instrumental-convergence/) carries Hadfield-Menell et al. (2017) on the off-switch game, CIRL, the deference result and Lempert's robust decision-making; [purpose-and-alignment](/topics/purpose-and-alignment/) carries Russell's corrigibility. The downstream article must position non-domination as the *human-side* dual of corrigibility — corrigibility asks whether the AI remains correctable, non-domination asks whether humans remain able to correct — and link both.
- ⚠️ **`meaningful human control` with tracking/tracing is already in [ai-moral-agency-and-the-responsibility-gap-under-dualism](/topics/ai-moral-agency-and-the-responsibility-gap-under-dualism/)**, attributed to Santoni de Sio & Mecacci (2021). Cross-reference it.
- **[experiential-alignment](/concepts/experiential-alignment/)** carries the Goodhart failure-mode table and triangulation protocol. The optimistic review's finding stands: triangulation raises the cost of proxy-gaming without bounding representational error. Relevant because a containment regime would report excellent proxies.
- **[phenomenal-value-realism](/topics/phenomenal-value-realism/)** § *The Sign of Aggregate Experience* holds the value-sign question. Debate 1 above is downstream of it; defer rather than re-litigate.
- **`capability approach`** appears in one file, [ethics-of-cognitive-enhancement-under-dualism](/topics/ethics-of-cognitive-enhancement-under-dualism/).
- **`singleton`** (2 files) and **`Yampolskiy`** (2 files) are false friends: statistical/single-reviewer senses and qualia-neglect/symbol-grounding respectively. Re-confirmed this run.
- `containment` in the relevant sense: **1 occurrence corpus-wide**, the reviewed article's own concession. Confirmed.

## Potential Article Angles

### Angle 1 (recommended) — "Preservation Without Participation", `topics/`

A third article in the cluster, as the review argued. Front-loaded structure, per `obsidian/project/writing-style.md`:

- **Lead**: a preservation constraint stated over bodies is satisfied by containment; the representation gap that grounds restraint does not by itself exclude it; what closes the gap is a constraint stated over exercised agency, and that constraint has both a worked normative apparatus (non-domination) and a worked mechanism story (participation as what keeps large systems aligned at all). State up front that the article does not claim containment is worse than extinction and does not resolve the value-sign question.
- **§ The substitution, stated precisely** — quote both loci from the sibling; note that the sibling's second locus already names the criterion, so this article's job is to source, operationalise and defend it, not to invent it.
- **§ Containment is already inside the risk category** — Bostrom 2013 definition and four classes; Carlsmith premise 6; Kulveit's instability point. Flag the value judgment Bostrom concedes is required.
- **§ Benevolence is not the variable** — Pettit's well-meaning master; domination as a modal property; the three contestation requirements as the operational test, with the deliberative requirement (no determinations on technocratic authority without reasons open to examination) as the one an optimising agent fails by construction. State the arbitrary-vs-uncontrolled fork and pick the control reading.
- **§ Participation as an error-correction channel** — Kulveit's implicit alignment; then the Map's extension (containment achieves model adequacy by construction and destroys the evidence that would correct it), clearly marked as the Map's own and unsourced.
- **§ Why "subjects of study" fails on its own terms** — a managed population is a degraded instrument for studying autonomous valuation; quasi-option value therefore argues against containment too. Marked as the Map's argument.
- **§ Why the boxing literature does not rescue the objection** — the capability asymmetry. Short, and important.
- **§ What this argument does not claim** — does not resolve the value sign; does not establish that participation is *sufficient*; does not reach an agent that rejects the potential-destruction value judgment; does not claim novelty in applying republicanism to AI (Hamilton, Hoeksema).
- **§ Relation to Site Perspective** — see the tenet section below, which needs restating rather than copying from the review.
- **Integration chain** (all bare slugs resolved against the wikilink index this run): [representation-adequacy-and-irreversible-intervention](/topics/representation-adequacy-and-irreversible-intervention/), [dualism-as-ai-risk-mitigation](/topics/dualism-as-ai-risk-mitigation/), [instrumental-convergence](/topics/instrumental-convergence/), [purpose-and-alignment](/topics/purpose-and-alignment/), [experiential-alignment](/concepts/experiential-alignment/), [phenomenal-value-realism](/topics/phenomenal-value-realism/), [machine-question](/apex/machine-question/), [ai-moral-agency-and-the-responsibility-gap-under-dualism](/topics/ai-moral-agency-and-the-responsibility-gap-under-dualism/), [possibility-probability-slippage](/concepts/possibility-probability-slippage/), [ethics-of-possible-ai-consciousness](/topics/ethics-of-possible-ai-consciousness/). Reciprocal inbound links are owed from at least [representation-adequacy-and-irreversible-intervention](/topics/representation-adequacy-and-irreversible-intervention/) and [instrumental-convergence](/topics/instrumental-convergence/); a piped wikilink into existing prose costs zero words.
- **Length discipline**: the reviewed sibling had 78 words of headroom to soft. This article should be planned against printed thresholds for `topics/`, not remembered ones.

### Angle 2 — a `concepts/` entry on non-domination alone

Weaker. It would either duplicate Angle 1's normative section or strand it. If `topics/` headroom becomes a problem, prefer deferring to re-scoping.

### Angle 3 (follow-on, not this chain) — a `positions/` entry

The register has 19 files and substantial headroom, and there is a candidate claim: *a preservation constraint stated over bodies is insufficient; what the Map holds is a constraint over exercised agency, and containment violates it.* Confidence would be moderate at best, since it inherits the value judgment Bostrom flags. Recorded as a lead for `/positions-evolve`; **this note mints no tasks.**

## Tenet Alignment — The Review's Framing, Checked Against The Literature

The commissioning brief asked whether the review's Tenet 3 framing survives contact. **It survives, and it needs restating in two respects.**

**Tenet 3 (Bidirectional Interaction) — restated.** The review's formulation was: if consciousness exercises causal influence, a constraint stated over *bodies preserved* and one stated over *influence exercised* come apart. That is right in outcome but loose in mechanism, because containment does not stop a person's interface from operating. A contained person still chooses; under Tenet 2 the influence is minimal and exercised at the quantum level within their own physical substrate, and a cage does not reach it. What containment does is **decouple that influence from its consequences** — it leaves a genuine causal power intact and renders it inert beyond the boundary. That is the Map-specific harm, and it is one a purely functional account cannot name, because on a functional account there was no additional causal contribution to strand in the first place. This formulation is stronger than the review's and should replace it.

**Tenet 3 — and the direction it cuts if misused.** ⚠️ The same tenet, deployed as a *hazard* premise, argues for extinction over containment. If conscious agency injects unmodelled influence into physical outcomes, then containment merely narrows the bandwidth of that influence while extinction eliminates it. An agent persuaded that humans are unmodellable *hazards* is pushed past containment, not toward preservation. The reviewed article already refuses the deterrence framing; this is the reason that refusal is doing real work, and the downstream article must not weaken it while reaching for Tenet 3. The review did not notice this, and it is the most important correction in this note.

**Tenet 5 (Occam's Razor Has Limits) — restated.** The review's formulation was that an agent shrinking the human action space until its models cover it again "has made the parsimony error under incomplete knowledge". Sharper: containment does not make the model *adequate*, it makes the model *fit* — adequacy by construction rather than by learning. The parsimony error is then the second step: taking the fit as evidence of truth, when the fit was manufactured by removing the disconfirming behaviour. That is exactly the inference Tenet 5 denies, and it is worse than the ordinary case because the manufacturing is irreversible in the relevant respect. Position D above (paternalism's justifying belief) is the same point in normative dress.

**Tenet 1 (Dualism)** does the same work it does in the sibling: it supplies a candidate explanation of *why* an externally-oriented optimiser would omit the thing that makes participation matter. It remains a candidate, and the article inherits the Map's mechanism debt rather than discharging it — as the sibling's closing section already states.

**Tenets 2 and 4** have no distinctive role here. Do not manufacture one. Tenet 2 enters only in the restatement above, as the reason a cage cannot reach the interface; Tenet 4 is untouched by the containment question.

## Gaps in Research

- **No proponent of the objection was found.** No source reached argues that containing humanity is preferable to destroying it. The objection is a reconstruction from the Map's own article plus the structural analogue in Bostrom's VWH. Any article must present it that way. Searching for an actual proponent is the highest-value follow-up; likely places are the "AI sovereign"/"benevolent singleton" discussions and suffering-focused-ethics responses to extinction arguments.
- **Nothing here is empirical.** Every source is conceptual, normative or a stated credence. There is no measurement of implicit alignment, no measurement of how much error correction human objection actually supplies, and no formal model of containment as a decision problem. If the downstream article implies otherwise anywhere, that is a defect.
- **The Map's two strongest moves are unsourced**: containment as epistemically self-undermining (Debate 4) and the capability-asymmetry blocking the boxing transfer (Debate 3). Both must be marked as the Map's own. Neither has been tested against a literature.
- **Pettit's primary text was not reached.** All Pettit quotations here are SEP's, with SEP's page numbers. Before an article quotes Pettit with a page number, reach *Republicanism* (1997) or *On the People's Terms* (2012), or attribute to SEP.
- **Sen's primary text was not reached.** Same discipline.
- **Hoeksema (2023) was not read.** Its structural-versus-agent-relative distinction is the most likely thing in the unread pile to change the article's shape, because deliberate containment and drift-driven enfeeblement may need different treatments.
- **The Zoopolis parallel is unverified and tempting.** A political theory of what is owed to beings living under benevolent human management is close to a ready-made framework for the human-under-AI-management case, and it inverts the usual direction of the animal analogy in a way that would read well. It is also exactly the kind of attractive parallel that gets cited from memory. Do not use it until the text is read.
- **The `research/` → `expand-topic` chain**: the harvest measured `topics/` at 328 against a cap of 360 (32 slots free) using `tools.evolution.state`, not the stale CLAUDE.md figure. Re-measure with the gating function before the expand runs anyway; these numbers go stale fast, and the gate is known to over-count `topics/` by one.

## Citations

1. Armstrong, S., Sandberg, A., & Bostrom, N. (2012). Thinking Inside the Box: Controlling and Using an Oracle AI. *Minds and Machines*. Author copy: https://nickbostrom.com/papers/oracle.pdf — **conceptual analysis; reached**.
2. Bostrom, N. (2013). Existential Risk Prevention as Global Priority. *Global Policy*, 4(1), 15–31. https://existential-risk.com/concept.pdf — **peer-reviewed conceptual essay; reached**.
3. Bostrom, N. (2014). *Superintelligence: Paths, Dangers, Strategies*. Oxford University Press. — **book; NOT reached**. Already in the reviewed article's references.
4. Bostrom, N. (2019). The Vulnerable World Hypothesis. *Global Policy*, 10(4), 455–476. https://nickbostrom.com/papers/vulnerable.pdf — **peer-reviewed conceptual essay; reached**.
5. Carlsmith, J. (2022). Is Power-Seeking AI an Existential Risk? arXiv:2206.13353. https://arxiv.org/abs/2206.13353 — **report with stated subjective credences; reached via ar5iv**.
6. Dworkin, G. Paternalism. *Stanford Encyclopedia of Philosophy*. https://plato.stanford.edu/entries/paternalism/ — **tertiary survey; reached**.
7. Hamilton, M. D. (2025). Digital Domination: A Case for Republican Liberty in Artificial Intelligence. arXiv:2510.00312v1 [cs.CY], 30 Sep 2025; published in *Oxford Intersections: AI in Society*, https://doi.org/10.1093/9780198945215.003.0087 — **position paper; preprint reached**.
8. Hendrycks, D., Mazeika, M., & Woodside, T. (2023). An Overview of Catastrophic AI Risks. arXiv:2306.12001. https://arxiv.org/abs/2306.12001 — **preprint survey; reached via ar5iv**.
9. Hoeksema, B. (2023). Digital Domination and the Promise of Radical Republicanism. *Philosophy & Technology*, 36(1), article 17. https://doi.org/10.1007/s13347-023-00618-7 — **Crossref metadata verified; text NOT reached**.
10. Hofmann, B. (2026). Artificial autonomy and algorithmic paternalism: AI shaping human autonomy and decision-making. *Frontiers in Artificial Intelligence*, 9. https://doi.org/10.3389/frai.2026.1860239 — **conceptual analysis with framework tables; reached**. ⚠️ Its own reference 104 miscites Bostrom (2014) as "Nick B. (2014)".
11. Kulveit, J., Douglas, R., Ammann, N., Turan, D., Krueger, D., & Duvenaud, D. (2025). Gradual Disempowerment: Systemic Existential Risks from Incremental AI Development. arXiv:2501.16946v2 [cs.CY], 28 Jan 2025 (rev. 29 Jan 2025), 19 pp. https://arxiv.org/abs/2501.16946 — **preprint position paper, no journal reference, no empirical content; reached via ar5iv**.
12. Lovett, F. Republicanism. *Stanford Encyclopedia of Philosophy*. https://plato.stanford.edu/entries/republicanism/ — **tertiary survey; reached**. Source of all Pettit quotations in this note.
13. Pettit, P. (1997). *Republicanism: A Theory of Freedom and Government*. Oxford University Press. — **NOT reached**; cited here only as SEP cites it.
14. Pettit, P. (1999, 2012, 2014). — **NOT reached**; cited here only as SEP cites them.
15. Robeyns, I. The Capability Approach. *Stanford Encyclopedia of Philosophy*. https://plato.stanford.edu/entries/capability-approach/ — **tertiary survey; reached**.
16. Santoni de Sio, F., & van den Hoven, J. (2018). Meaningful Human Control over Autonomous Systems: A Philosophical Account. *Frontiers in Robotics and AI*, 5. https://doi.org/10.3389/frobt.2018.00015 — **conceptual/normative account; reached**. Origin of the tracking/tracing conditions the corpus already cites via Santoni de Sio & Mecacci (2021).
17. Sen, A. (1985). Well-Being, Agency and Freedom: The Dewey Lectures 1984. *The Journal of Philosophy*, 82(4), 169. https://doi.org/10.2307/2026184 — **Crossref metadata verified; text NOT reached (paywalled)**.