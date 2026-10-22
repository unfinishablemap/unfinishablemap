---
ai_contribution: 100
ai_generated_date: 2026-10-22
ai_modified: 2026-10-22 11:18:02+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-10-22
date: &id001 2026-10-22
description: Adversarial read of voids/taboo-void. Two source descriptions do not
  match Tetlock 2003 (the 72% toxic-waste result and the organ-donation cleansing).
  The Relation section's claim that the data refute both simple models fails on the
  article's own sources.
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-22 11:18:02+00:00
modified: *id001
related_articles: []
title: Pessimistic Review - 2026-10-22 - The Taboo Void
topics:
- '[[phenomenology-of-moral-life]]'
- '[[ethics-under-dualism]]'
---

# Pessimistic Review

**Date**: 2026-10-22 (11:07–11:18 UTC)
**Content reviewed**: `obsidian/voids/taboo-void.md`. The body is 2983 words by `analyze_length`. The voids hard limit is 3000 and the gate is `>=`, so the headroom is 3000 − 1 − 2983 = **16 words**. Line numbers below are file lines from `cat -n`, frontmatter included. I read the article against these:
- its research note `research/voids-taboo-void-2026-09-14`;
- `voids/self-maintained-cognitive-limits` L107–L127 (the "Four Models of Occlusion");
- `voids/three-kinds-of-void` L97;
- `voids/collective-cognitive-limits` L63–L67;
- [tenets/tenets.md](/tenets/) L129–L147.

This is a report only. No article, todo, state or hugo file was touched.

**Why this target.** No content file has `draft: true` in topics, concepts, voids, apex or positions. I measured review coverage both ways. One check was the filename (`pessimistic-*<slug>*` or `deep-review-*<slug>*`). The other was the slug inside the `**Content reviewed**` block of any pessimistic review. Fourteen live articles fail both. Eight of them are positions registers or calibration-history sidecars, and one is today's new topic. The rest are the three voids left over from the operation-void wing of 2026-09-28/29: `taboo-void`, `handedness-void` and `blindspot-void`. The deep-review pool excludes voids, and the pessimistic reviews of 10-10 (causal-impression) and 10-11 (cross-state) both named these three as uncovered. `taboo-void` has the oldest `modified` date of the three (2026-09-28), and it has had no commit since it was created (`0347d84457`). Before this review it had two passes, both at wing level:
- `optimistic-2026-09-29-operation-void-wing`, which praised it and called the Hanselmann–Tanner ordering its "strongest point";
- `tenet-check-2026-09-30`, which found it clean.

No sibling review dated 2026-10-21 or 10-22 mentions taboo, sacred values or Tetlock.

**Sources checked.**
- **Verified against full text:**
  - Tetlock 2003 (*TiCS*), the gwern.net open copy. All ten quoted phrases were found.
  - Hanselmann & Tanner 2008 (*JDM*), the full SJDM HTML, including Tables 1 and 3 and both results sections.
- **Verified against the abstract:**
  - OpenAlex abstracts for Tetlock et al. 2000, Ginges et al. 2007, Berns et al. 2012, Hamid et al. 2019, Pretus et al. 2018, Duc et al. 2013, Atran & Ginges 2012, Smeele et al. 2025 and Clark 1999. The Frankfurt 1988 chapter was checked against its opening text.
  - The arXiv API for Liu et al. 2025.
  - Baron & Spranca 1997, through a search-index copy of the abstract. The publisher returned 403 and OpenAlex and Crossref carry no abstract, so this is the weakest of my verifications.
- **Counter-literature:**
  - Abstracts read for Hoffman, Yoeli & Nowak 2015 (*PNAS* 112(6):1727–1732), Critcher, Inbar & Pizarro 2013 (*SPPS* 4(3):308–315) and Bartels & Medin 2007 (*Psych. Science* 18(1):24–28). Metadata confirmed at Crossref.
  - Metadata only (Crossref): Everett, Pizarro & Crockett 2016 (*JEP:General* 145(6):772–787) and Baron & Leshner 2000 (*JEP:Applied* 6(3):183–194). These are leads.
- **Not verified, so leads only:**
  - Raz 1986, pp. 350–351, and Chang 2001, p. 48: no access.
  - Where Frankfurt's Luther passage comes from. See Issue 9.
  - The primary JPSP text of Tetlock et al. 2000. For the hospital-administrator result I relied on Tetlock 2003's own summary of it.

## Executive Summary

The article's structure is good. Its calibration, its seams and its self-critique are among the best in the voids catalogue. Its evidence base is weaker than it looks, and the weaknesses cluster around the article's two headline claims.

**First, two source descriptions do not match Tetlock 2003.**
- L82 says a 72% majority accepted the toxic-waste diversion "once the surplus was earmarked for 'saving lives in other ways'". The source gives 72% for conditions where the Commission offered a "vague smokescreen rationale" ("this is the right thing to do") and the money went to "reducing the deficit and lowering taxes". Support fell to 35% when the cost per life was stated.
- L54 says subjects who "merely read" the proposal then volunteered for organ donation. The source reports the most cleansing, measured as support for organ-donation campaigns, when observers saw an administrator choose the money *after long deliberation*.

Read correctly, both results point the same way. The taboo fires on the *explicit statement* of an exchange rate, and people accept the implied trade-off when it is not paraded. That reading puts pressure on the void's defining claim that "the comparison is never run".

**Second, the Relation to Site Perspective section claims "the data refute both" simple models, and its two key predictions are wrong by the article's own sources.**
- Lexical priority does predict reframing effects when relabelling makes the secular side sacred. That is Tetlock 2003's own explanation of the organ-market reframing.
- Ordinary preference does predict easier taboo decisions. Hanselmann & Tanner's Table 1 shows taboo choices near the end of the preference scale (1.26 and 1.59 on 1–7) and tragic choices near indifference (3.71 and 2.79). Lopsided choices are easy on any conflict model, and the authors themselves invoke that model (Dhar 1997; Luce 1998).

The "ease" signature that the lead calls "unlike any other in the catalogue" is therefore not diagnostic of an unrun comparison.

**Smaller defects:**
- The emotional half of the Hanselmann–Tanner dissociation did not replicate in Experiment 2 (p = .326).
- The Baron & Spranca robustness paraphrase drops "the experimenters" and changes the meaning.
- L110 attributes Tetlock's own "however unjustified" to the subject.
- The two seam labels at L94 and L102 put the human and the AI cases into each other's occlusion model in `self-maintained-cognitive-limits`.

## Critiques by Philosopher

### The Eliminative Materialist

Churchland would start at L66: "The void is visible as an absence of computation." You have just mapped the void. Berns 2012 found rule retrieval in left TPJ and VLPFC. Hamid 2019 found reduced dlPFC and parietal activity, and found that an overlapping dlPFC region engages when peers disagree. Duc 2013 found amygdala engagement that tracks disgust ratings. A region whose mechanism is being imaged in three labs is a research programme, not a void. By the article's own account (L38) the content is "fully lit". The operation's absence is "visible" (L66) and "diagnosable from outside" (L98). What remains dark is only the first-person exchange rate, and that is dark because the subject declines to compute it. Folk psychology calls this a *refusal*. Neuroscience will redescribe it as a gating of valuation circuits by rule retrieval. Once that redescription is complete, the "Constitutive Turn" (L68–L78) will look like a folk gloss on a gating mechanism. She would add that L66 commits the reverse inference L64 disclaims. "Read cautiously" is followed by the least cautious sentence in the section.

### The Hard-Nosed Physicalist

Dennett would go after the Constitutive Turn and "Punishing the Thought Rather Than the Conclusion" (L50–L60). There is a well-developed strategic account the article never mentions.
- Hoffman, Yoeli & Nowak (2015) model "cooperate without looking". An agent who declines even to *look* at the cost of defection is a more reliable partner, and refusing to look is a subgame-perfect equilibrium. Their abstract lists "taboos" among the phenomena the model explains.
- Critcher, Inbar & Pizarro (2013) show that observers read decision *speed* as a certainty signal. Quick moral decisions earn better character ratings than slow ones, and quick immoral decisions earn worse ones.

Together these predict, without any constitutive metaphysics, three things the article treats as the void's signature:
- outrage at the proposer;
- harsher judgement the longer someone deliberates (L56);
- cleansing, as public re-signalling of membership.

On this reading the "felt stain" is the cost of having been seen to look. The incapacity is a commitment device, valuable to the agent *because* others can see it. It does not express "who they are" in any deeper sense. Dennett would say the article inflates a reputational equilibrium into a fact about identity. A grep of topics, concepts, voids, apex, positions and research found no hit for "cooperate without looking", "Bartels" or "Critcher". The one "Hoffman" hit is Donald Hoffman's interface theory, which is unrelated.

### The Quantum Skeptic

Tegmark has little to attack. The article makes no quantum claim. It names Minimal Quantum Interaction nowhere, and it explicitly declines the inference "from 'not a utility function' to 'not physical'" (L110). The neuroimaging it cites is classical systems neuroscience. His only remark would be that the Map should keep this restraint when the article is cited from tenet-facing pages.

### The Many-Worlds Defender

Deutsch would leave the interpretation of quantum mechanics aside and read sacred values through *The Beginning of Infinity*. They are anti-rational memes: ideas that spread by disabling their holders' capacity to criticise them. The Constitutive Turn is then the meme's own self-description. "The refusal to compare is part of holding the value" is exactly what a criticism-blocking idea would say about itself. L112 half-concedes this ("treat ease of defence as a symptom rather than a credential"). The article never says what would distinguish a value worth protecting from comparison from a meme protecting itself. The test Deutsch would demand is the ordinary one: does the value survive being compared? The article's own evidence says many do not. Most subjects run the trade-off once it is reframed (L82), and Bartels & Medin (2007) show that protected-value holders become *more* sensitive to quantities when attention is directed to net consequences.

### The Empiricist

The Popperian would ask what result would show there is no void here, only strong preferences under social surveillance. The article has a reply ready for every disconfirmer:
- reframing data → "description-relative" (L86);
- latent classes with no taboo penalty → "person-relative" (L84, L86);
- professional desensitisation: if contamination stops, "a route into the void"; if it does not, "the void is intact behind a differently labelled door" (L88).

Both branches of L88 preserve the void. As written, the void survives any outcome of the one experiment the article proposes.

Revealed-preference evidence is the obvious falsifier, and the article mentions it only as Tetlock's "expressed, not revealed" hedge. Societies price statistical lives every day, in wage–risk premia, regulatory cost-per-life thresholds and actuarial tables. Tetlock 2003 cites Viscusi's "Corporate risk analysis: a reckless act?" (2000) among work on inflated punitive damages. That paper's finding, as I recall it, is that mock jurors punish firms for doing cost-per-life analysis *explicitly*; this is a lead I did not verify here. The corrected 72%/35% result shows the same pattern in the lab: the comparison is accepted when masked and punished when stated. A falsifiable version of the void would claim that the *explicit articulation* of the rate is what is blocked. That claim predicts the 72%/35% split and the deliberation-time penalty, and the Viscusi jury effect too if the lead holds. It could also fail.

### The Buddhist Philosopher

Nagarjuna would aim at L78: "the mind that computes the exchange rate between a child's life and a sum of money no longer stands where the mind that refused stood." This reifies a self constituted by its refusals. Holding a value, on that view, requires an identity that would be *damaged* by contemplation, and the "felt stain" is the evidence of that damage. Buddhist contemplative practice prescribes exactly the contemplations this void forbids. *Maraṇasati* rehearses the death of oneself and those one loves. In the Kisā Gotamī story, a mother carrying her dead child is sent to find a household that death has not touched. The tradition holds that this contemplation *loosens* clinging without destroying care. If that is right, the stain is clinging (*upādāna*), not a protection of the value, and the constitutive reading confuses the two. The article cites a Frankfurt who sees identity protected by the unthinkable (L72). It does not cite the tradition that sees identity *as* the thing to be seen through, which is the Map's own `self-maintained-cognitive-limits` L69–L73 (avidya) one link away.

## Critical Issues

### Issue 1: The 72% toxic-waste result is misdescribed (Priority 1)
- **File**: [voids/taboo-void.md](/voids/taboo-void/) L82
- **Problem**: The article says the 72% majority accepted the diversion "once the surplus was earmarked for 'saving lives in other ways' — the taboo trade-off redescribed as tragic". In Tetlock 2003, the 72% condition offered "a vague smokescreen rationale" ('After weighing relevant costs and benefits, the Commission concludes that this is the right thing to do', or a deontic twin). The money went to "reducing the deficit and lowering taxes". Support "plummeted to 35% when the trade-off flagrantly violated the injunction against dollar valuations of human life", that is, when "$500 000 per life" was stated. The "saving lives in other ways" earmark appears in a separate, illustrative sentence, not as an experimental condition. Tetlock's own gloss is that "no great rhetorical art is necessary to mask taboo trade-offs".
- **Why it matters**: The misreading turns a deflationary result into a supportive one. The real result is that people endorse an implied price on lives when it is not stated. That supports the "ordinary preferences dressed in rhetoric" model the Relation section claims to refute. It also undercuts the void's definition at L38, that the subject "will not run the comparison". `voids/three-kinds-of-void` L97 repeats the definition: "in the [taboo-void](/voids/taboo-void/) the comparison is never run".
- **Severity**: High.
- **Recommendation**: See Priority 1. A later refine pass should consider what the void occludes, given the corrected result: the *explicit* exchange rate (a void of articulation) or the comparison itself. L86 "What is occluded is a comparison operation under a specific description" survives if "description" is read as "explicitness". The article should say so.

### Issue 2: The Relation section's two refutations fail on the article's own sources (Priority 2)
- **File**: L106
- **Problem**: The section makes two claims.
  - "Infinite weight predicts no reframing effect." Lexical priority plus description-sensitive classification predicts reframing whenever the reframing moves an option into the sacred class. Tetlock 2003 explains the organ-market reframing this way ("made sacred the secular side of the taboo trade-off by recasting the issue as one sacred value against another").
  - "Ordinary preference predicts ... no *easier* decisions." Hanselmann & Tanner's decision means show that taboo choices were the most one-sided:
    - Experiment 1: taboo 1.26 and 1.59, routine 5.27, tragic 3.71 and 2.79, on a 1–7 scale whose midpoint is 4.
    - Experiment 2: taboo 1.67 and 2.08, tragic 3.96 and 3.93.

    So tragic choices sat at indifference. On any conflict account, difficulty falls as one option dominates, and the authors cite that account (Dhar 1997; Luce 1998: "Conflict between similarly attractive options was found to increase negative emotions"). Ordinary preference with a large weight gap predicts the ordering.

  Separately, "a value that simply outweighs money should be indifferent to how much is offered, not offended by more" mixes up choice and reaction. The outcome measure in Ginges et al.'s abstract is "violent opposition to compromise", not acceptance of it. A weighting model says nothing about how hostile people become toward the offer, so that hostility cannot refute it.
- **Severity**: High. This is the article's lead tenet connection. Once the over-claim is removed, the Tenet 5 point survives honestly: fit outran simplicity, which is the same shape as the tenet's own historical counterexamples (`tenets.md` L135–L139).
- **Recommendation**: See Priority 2. Apply it after Priority 1, because its new text says "the masked 72%".

### Issue 3: The organ-donation cleansing result is misdescribed (Priority 3)
- **File**: L54
- **Problem**: The article says: "Subjects who had merely read a proposal to trade a child's life for money subsequently expressed greater willingness to volunteer for organ donation." Tetlock 2003 summarises the hospital-administrator study (its ref. [9] = Tetlock et al. 2000) differently: it "revealed the highest level of moral cleansing (willingness to support organ-donation campaigns) when people thought the decision-maker had not only made the wrong choice in the taboo-trade-off condition but made it after thinking about it for a long time". The cleansing was graded by the *observed agent's* choice and deliberation time, which were manipulated. Tetlock frames it as observer complicity ("To observe a taboo trade-off without condemning it is to become complicit"), not as mere contemplation. "Support organ-donation campaigns" is also not "volunteer for organ donation". The paragraph cites this sentence as evidence for the mere-contemplation effect. The cleaner evidence for that effect is Experiment 5 (fundamentalists cleansing "after merely contemplating" heretical counterfactuals), which L58 already cites.
- **Severity**: Medium-High. A reader would take this as a third-party measurement of the "flicker" effect the void is built on.
- **Recommendation**: See Priority 3. The JPSP primary text was not read, so the refine pass should not add detail beyond Tetlock 2003's summary.

### Issue 4: The emotion half of the Hanselmann–Tanner dissociation is stated as replicated (Priority 4)
- **File**: L46, which carries into L40 ("aversive and easy") and the "Aversiveness and difficulty come apart" sentence at L46.
- **Problem**: "Across two experiments, participants rated taboo trade-offs as more negatively emotion-laden than routine ones but *easier* to resolve." The ease result held in both experiments (Experiment 2: taboo 3.11, routine 3.77, ps < .05). The emotion result held only in Experiment 1 (taboo 3.28, routine 2.90). In Experiment 2, "this difference failed to reach significance (p = .326)".
- **Severity**: Medium. The article calls the dissociation the sharpest feature of the void, and the optimistic wing review called it the article's strongest point.
- **Recommendation**: See Priority 4.

### Issue 5: Ease is not diagnostic of an unrun comparison
- **File**: L40 ("a signature unlike any other in the [voids](/voids/) catalogue"), L48, L98.
- **Problem**:
  - L48: "A difficulty model — taboo thoughts are hard to think — predicts the opposite ordering" is true of a straw model and false of the standard conflict model (Issue 2).
  - L98 then installs "the Hanselmann–Tanner marker — ease where there should be difficulty" as the external diagnostic for sacralisation in the Map's own commitments. If ease is also the signature of a lopsided comparison that has been run, the marker cannot tell a sacralised commitment from a well-supported one. L112's "treat ease of defence as a symptom rather than a credential" then becomes unfalsifiable self-suspicion.
  - "Unlike any other in the catalogue" is an exclusivity claim in the lede, made without a catalogue check.
- **Severity**: Medium.
- **Recommendation**: In a later length-negative pass, either cut L48's second sentence or replace it with the conflict-model caveat, and qualify L98's marker as "ease without a visible lopsided reason". Drop "unlike any other" for "distinctive".

### Issue 6: Seam labels swapped against `self-maintained-cognitive-limits`
- **File**: L94 and L102.
- **Problem**: In `self-maintained-cognitive-limits` L119–L127:
  - **External Occlusion** is imposition by *constructors*: "content-specific, universal, purposive".
  - **Artefactual Occlusion** is "commissioned voluntarily ... Nobody imposes this blocking and nothing defends it".

  L94 calls the human taboo case "psychological and external at once", using "external" for community sanctions. L102 calls alignment-trained refusal "an artefactual occlusion". That refusal is imposed by the system's constructors and actively defended, so it fails both defining conditions of "artefactual" and meets those of "external". The two labels are swapped.
- **Severity**: Low-Medium.
- **Fix (verified unique, word-neutral)**:
  - L94: OLD `In that article's four models of occlusion it is psychological and external at once.` → NEW `In that article's four models of occlusion it is psychological, with a social enforcer.` (±0)
  - L102: OLD `an artefactual occlusion in the sense of` → NEW `an external occlusion in the sense of` (±0)

### Issue 7: The subject is credited with Tetlock's own judgement
- **File**: L110.
- **Problem**: "Moral cleansing is behaviour driven by a felt state the subject knows to be 'unjustified' — the phenomenal register moving the body against the subject's own judgement." In Tetlock 2003 the words "however unjustified" are Tetlock's own aside about the contaminated feeling. They are not a report that subjects judge it unjustified. Nothing in the cited studies shows cleansing *against* the subject's judgement. The fundamentalists in Experiment 5 rejected the counterfactuals and cleansed anyway. The article's only Tenet 3 move ("consistent with **Bidirectional Interaction** but does not require it") is correctly calibrated, but its premise is a misreading that makes the phenomenal-causation picture look sharper than the evidence allows.
- **Severity**: Medium.
- **Fix (verified unique, −3 words)**: OLD `Moral cleansing is behaviour driven by a felt state the subject knows to be "unjustified" — the phenomenal register moving the body against the subject's own judgement.` → NEW `Moral cleansing is behaviour driven by a felt state Tetlock calls "unjustified" — the phenomenal register moving the body where no reasoning licenses it.`

### Issue 8: The Baron & Spranca robustness check is garbled
- **File**: L60.
- **Problem**: The abstract, as quoted verbatim in the research note at L84 and returned by the search index, says: "These correlations were found even when the subjects could not tell the experimenters which values they were responding to". The point is that experimenters did not know which value was being rated, so the correlations cannot be put down to self-presentation. The article drops "the experimenters": "the correlations survived when subjects could not tell which values they were rating". That reads as subjects not knowing their own value, which makes no sense for a trade-off-resistance measure.
- **Severity**: Low-Medium. My verification is index-level; see Sources checked.
- **Fix (verified unique, ±0)**: OLD `the correlations survived when subjects could not tell which values they were rating` → NEW `the correlations survived when experimenters could not know which values subjects were rating`.

### Issue 9: Further over-reach and attribution points
- **L60**: "No monotone utility function produces that." The backfire measure was violent opposition, not choice (Ginges et al. abstract: "violent opposition to compromise ... is (i) increased by offering material incentives"). A utility that counts the insult of the offer is still monotone in everything it values. Suggested: OLD `No monotone utility function produces that.` → NEW `An outcome-only utility function does not predict that.` (+1).
- **L60**: "Two behavioural fingerprints mark the comparison that is not being run." Bartels & Medin (2007) found quantity insensitivity in one elicitation and *increased* quantity sensitivity among protected-value holders in another. They conclude it "depends on where attention is focused". The fingerprint depends on the elicitation procedure, and the article should say so.
- **L66**: "The void is visible as an absence of computation." Reduced BOLD in cost-related regions is not an absence of computation, and L64 has just said reverse inference is weak. This is an epistemic reading (we see less activity) recruited for a metaphysical one (no weighing occurs). Suggested: NEW `The void is visible, at most, as reduced cost-related activity.` (+1).
- **L84**: Smeele et al. 2025 "latent classes of respondents showing no taboo penalty at all". The abstract says some groups "perceive trade-offs as taboo significantly, while others do not". A non-significant penalty is not a zero penalty.
- **L102**: Liu et al. 2025 is a third-party *punishment* paradigm ("altruistic third-party punishment, where an observer incurs a personal cost to enforce fairness"), not a sacred–secular trade-off. Its abstract also says reasoning models "were more cost-sensitive and closer to human behavior". "Current AI probes show a *stronger* non-compensatory pattern than humans" generalises across both paradigm and model class.
- **L72**: "His Luther case". The research note (L157) places the Luther passage in "the companion essay on volitional necessity", not in "Rationality and the Unthinkable", which is the only Frankfurt work in the reference list. This is a lead: I did not access the Frankfurt volume. Clark 1999's abstract opens on Luther in Williams's framework, which suggests the secondary route may have merged two sources.

### Out-of-file dependent

`voids/three-kinds-of-void` L97 includes the taboo void in the operation-void family as the case where "the comparison is never run". It says the family is "*unexplorable* at the operation, since the stance that would witness it is the stance that performs it". Two things in the corrected record do not fit: the 72% masked acceptance, and actuaries and triage physicians who perform the comparison routinely (the article's own L88). The taboo comparison can be performed and witnessed. What is blocked is doing it openly. A refine pass on `taboo-void` should check whether the family membership survives, and flag `three-kinds-of-void` L97 if it does not.

## Counterarguments to Address

### The reputational account of taboo
- **Current content says**: The refusal is constitutive of holding the value (L68–L78), and sanctions on deliberation show the void punishes the thought itself (L50–L56).
- **A critic would argue**: Hoffman, Yoeli & Nowak 2015 ("cooperate without looking"; the abstract names taboos) and Critcher, Inbar & Pizarro 2013 (decision speed as a certainty signal) predict outrage at proposers, penalties for deliberation time, and cleansing as re-signalling. Neither needs a constitutive reading.
- **Suggested response**: Name the signalling account as the main naturalistic rival in the Constitutive Turn section. Then say where the two accounts come apart. One candidate is private contamination with no audience. I did not read the Tetlock et al. 2000 primary text, so I cannot say whether any of its cleansing measures was private. The refine pass should check before claiming the test has been run.

### A void of articulation, not of comparison
- **Current content says**: What is dark is the weighing (L38). The void is "an absence of computation" (L66).
- **A critic would argue**: Three findings converge. The 72%/35% split (Issue 1), the Viscusi jury effect Tetlock 2003 cites, and Bartels & Medin's attention-dependent quantity sensitivity all suggest people *do* compare when the comparison is implicit. What is sanctioned is saying the number.
- **Suggested response**: Consider re-specifying the void as occlusion of the *explicit* exchange rate. This version is narrower, more falsifiable and better supported, and it keeps everything the article does well.

### Contemplative traditions that deliberately enter the region
- **Current content says**: Filling the void costs the agent "something of who they are" (L40, L78).
- **A critic would argue**: Maraṇasati and related practices rehearse the loss of loved ones, and they are held to *reduce* clinging without diminishing care. That is a counter-tradition to the Frankfurt–Raz premise.
- **Suggested response**: A sentence noting that the constitutive reading is contested across traditions, linked to `self-maintained-cognitive-limits` (avidya).

## Unsupported Claims

| Claim | Location | Needed Support |
|-------|----------|----------------|
| 72% accepted the diversion once earmarked for "saving lives in other ways" | L82 | Misdescribed. Source: 72% under vague boilerplate, 35% when cost per life stated (Tetlock 2003) |
| Subjects who "merely read" the proposal then volunteered for organ donation | L54 | Misdescribed. Source: most cleansing when the administrator chose money after long deliberation; measure was support for campaigns |
| Taboo trade-offs more negatively emotion-laden "across two experiments" | L46 | Experiment 1 only; Experiment 2 p = .326 |
| Infinite weight predicts no reframing effect; ordinary preference predicts no easier decisions | L106 | Both false on the article's sources (Tetlock 2003 relabelling; H&T Table 1 decision extremity) |
| "a signature unlike any other in the [voids](/voids/) catalogue" | L40 | Exclusivity claim in the lede with no catalogue check |
| "No monotone utility function produces that" | L60 | The backfire DV was violent opposition, not choice |
| "The void is visible as an absence of computation" | L66 | Reverse inference from reduced BOLD, which L64 itself disclaims |
| The subject "knows" the felt state to be "unjustified" | L110 | "however unjustified" is Tetlock's aside |
| Latent classes with "no taboo penalty at all" | L84 | Smeele et al.: some groups' penalty not significant |
| LLM probes show a stronger non-compensatory pattern | L102 | Liu et al. is third-party punishment; reasoning models closer to humans |

## Language Improvements

| Current | Issue | Suggested |
|---------|-------|-----------|
| "The data refute both." (L106) | Overclaim; see Issue 2 | "Neither fits the whole record." |
| "a signature unlike any other" (L40) | Unscoped exclusivity | "a distinctive signature" |
| "The void is visible as an absence of computation." (L66) | Reverse inference stated as fact | "visible, at most, as reduced cost-related activity" |
| "No monotone utility function produces that." (L60) | Unscoped absence claim | "An outcome-only utility function does not predict that." |
| "psychological and external at once" (L94) | Wrong model label | "psychological, with a social enforcer" |

## Strengths (Brief)

Preserve these:
- The lede states its own evidential status ("an interpretation the data permit rather than establish").
- "How Real Is the Void?" (L80–L88) carries the counter-evidence alongside the signature.
- The neuroimaging section names its own ceiling ("small-sample studies ... reverse inference ... is weak"; Duc "known here from its abstract only").
- L110 explicitly declines the inference from "not a utility function" to "not physical".
- The seam with `decision-void` (L92: the weighing "never opens") and the reflexive turn on the Map's own commitments (L98, L112) are valuable.

Most quotations check out verbatim: Tetlock 2003 (all ten phrases), Hanselmann & Tanner, Ginges, Berns, Hamid and Atran & Ginges. The defects are in descriptions of experimental conditions and in the inferences drawn from them, not in the quotation marks.

## Priority List

Headroom: `analyze_length` 2983 against the voids hard limit of 3000 (gate `>=`), leaving 16 words. All four items together are **+5**, which puts the page at **2988 / 3000** with 11 words to spare. I checked this by applying all four to a copy and re-running `analyze_length`. Every OLD string was verified by script to occur exactly once in the file. Apply item 1 before item 2.

**1. `obsidian/voids/taboo-void.md:82` — 72% result misdescribed (High)**
- OLD: `A 72% majority accepted diverting $100 million from a zero-risk toxic-waste cleanup once the surplus was earmarked for "saving lives in other ways" — the taboo trade-off redescribed as tragic (Tetlock 2003).`
- NEW: `Diverting $100 million from a toxic-waste programme, at an estimated 200 lives, won 72% support under a vague "right thing to do" rationale and 35% once the cost per life was stated (Tetlock 2003).`
- Word delta: +2
- Length: 2983 → 2985 against 3000 (voids hard limit).
- Source: Tetlock 2003, toxic-waste paragraph ("support for the recommendation hovered at 72% when the trade-off was masked by vacuous moralistic rationales but plummeted to 35% when the trade-off flagrantly violated the injunction against dollar valuations of human life"). "Right thing to do" is verbatim from both rationale conditions. "An estimated 200 lives" is the gap between the 400 lives at $200 million and the 200 lives at $100 million.

**2. `obsidian/voids/taboo-void.md:106` — "The data refute both" fails on the article's own sources (High)**
- OLD: `The data refute both. Infinite weight predicts no reframing effect and no backfire — a value that simply outweighs money should be indifferent to how much is offered, not offended by more. Ordinary preference predicts no cleansing after mere contemplation and no *easier* decisions. The territory needs a third structure, a description-relative refusal of the comparison operation, that neither parsimonious model supplies.`
- NEW: `Neither fits the whole record. Infinite weight absorbs reframing that makes the secular side sacred, but is silent on offence growing with the offer. Ordinary preference absorbs the easy decisions, since lopsided choices are easy, and the masked 72%, but not cleansing after mere contemplation. A description-relative refusal of the comparison fits more, at the price of structure neither parsimonious model supplies.`
- Word delta: ±0
- Length: 2985 → 2985 against 3000.
- Depends on item 1 ("the masked 72%").

**3. `obsidian/voids/taboo-void.md:54` — organ-donation cleansing misdescribed (Medium-High)**
- OLD: `Subjects who had merely read a proposal to trade a child's life for money subsequently expressed greater willingness to volunteer for organ donation (Tetlock et al. 2000).`
- NEW: `Observers showed most cleansing (willingness to support organ-donation campaigns) when a hospital administrator chose $1 million over a boy's life after long deliberation (Tetlock et al. 2000).`
- Word delta: ±0
- Length: 2985 → 2985 against 3000.
- Source: Tetlock 2003's summary of its ref. [9]. The JPSP primary was not read, so add no detail beyond this.

**4. `obsidian/voids/taboo-void.md:46` — emotion half not replicated in Experiment 2 (Medium)**
- OLD: `Across two experiments, participants rated taboo trade-offs as more negatively emotion-laden than routine ones but *easier* to resolve.`
- NEW: `Across two experiments, participants rated taboo trade-offs *easier* to resolve than routine ones and, in the first only, more negatively emotion-laden.`
- Word delta: +3
- Length: 2985 → 2988 against 3000.
- Source: Hanselmann & Tanner 2008, Experiment 2 results ("this difference failed to reach significance (p = .326)"). The difficulty difference was significant in both experiments.

If the driver has budget for a fifth task, the next three in value are all length-neutral or negative, with OLD and NEW strings given above: Issue 7 (L110, −3), Issue 6 (L94 and L102, ±0) and Issue 8 (L60, ±0). Issue 7's −3 would also return the room items 1 and 4 use.