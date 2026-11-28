# Hostile-Referee Audit: “Purpose and AI Alignment” (unfinishablemap.org/topics/purpose-and-alignment/)

I could not audit the text of this article directly. The fetch tool rejected the slug URL. Four site-restricted searches never returned the page as a result, so it never became fetchable. The commissioned subagent could not reach it either. The one changelog copy I could fetch stops at 2026-10-15, so I could not see what changed in the 2026-11-20 revision. Everything below is built from what the Map’s own pages say the article argues, plus the companion articles I did fetch. Those are concepts/experiential-alignment (modified 2026-11-24) and topics/instrumental-convergence (modified 2026-11-06). I also checked the alignment and wellbeing literature at its sources. I do not reconstruct the article. Each finding is labelled VERIFIED (checked at a primary source), INFERRED (the auditor’s reading of the cluster) or UNVERIFIABLE.

## 1. TL;DR

- **Provisional verdict: DEMOTE-TO-COHERENCE-ONLY.** This holds for the central claim that experiential alignment “does better” than preference-based alignment. The neighbouring pages report the claim, and the Map’s own Experiential Alignment page undercuts it (VERIFIED). That page admits the framework’s distinctive edge over preferentism is “conditional on phenomenal realism”. [unfinishablemap](https://unfinishablemap.org/concepts/experiential-alignment/) It also calls its decision-theoretic case “a hedge, not a demonstration that the framework’s edge over preferentism is tenet-independent.” [unfinishablemap](https://unfinishablemap.org/concepts/experiential-alignment/) An argument whose advantage disappears unless the tenets are true shows coherence, not superiority. The verdict is provisional because the target text was not read; it should be confirmed against the live text.
- **The target is outdated, and Russell is misdescribed.** The Experiential Alignment page treats “Standard AI alignment approaches learn from human preferences” via Russell’s framework as the mainstream. [unfinishablemap](https://unfinishablemap.org/concepts/experiential-alignment/)[unfinishablemap](https://unfinishablemap.org/concepts/experiential-alignment/) But Russell’s preferences are by definition “all-encompassing; they cover everything you might care about, arbitrarily far into the future” (Human Compatible, 2019, as quoted in secondary sources). [Wikipedia](https://en.wikipedia.org/wiki/Human_Compatible)[wikiwand](https://www.wikiwand.com/en/articles/Human_Compatible) That is not the “thin” choice-ordering the Map attacks. Current practice is something else again: Constitutional AI (Bai et al. 2022, arXiv:2212.08073), debate (Irving, Christiano & Amodei 2018, arXiv:1805.00899), scalable oversight, and model constitutions. [arxiv](https://arxiv.org/abs/1805.00899)[arxiv](https://arxiv.org/abs/2212.08073) Claude’s constitution (21 January 2026) already tells the model to attend to user wellbeing and “long-term flourishing”, not just immediate interests. [anthropic](https://www-cdn.anthropic.com/f9926ccb6c48106f225cfb9e29f8d257fae0347f/claudes-constitution_jan-26.epub) That is the very move the Map presents as its own innovation.
- **Required gates fail.** I found no engagement with Laukkonen, Friston & Chandaria 2025 (NBR 176:106296) or any active-inference account of valence or selfhood anywhere in the experiential-alignment cluster. [ovid](https://www.ovid.com/journals/nebior/abstract/10.1016/j.neubiorev.2025.106296~a-beautiful-loop-an-active-inference-theory-of-consciousness) Illusionism is handled through Frankish 2016 and a Tallis magazine column (Philosophy Now 161, 2024, pp. 58–59). [pdcnet](https://www.pdcnet.org/pdc/bvdb.nsf/purchase26)[unfinishablemap](https://unfinishablemap.org/concepts/experiential-alignment/) Kammerer’s work on the ethics of illusionism, the strongest stance-relevant opponent, is not engaged anywhere in what I could see. [researchgate](https://www.researchgate.net/publication/339921937_The_Normative_Challenge_for_Illusionist_Views_of_Consciousness)

## 2. Dimensional analysis

### 2.1 What the article argues (from the Map’s own descriptions)

- **Living with the Map (apex):** the article explains “Why AI alignment faces the meaning problem and requires human judgment, with the experiential alignment framework as its constructive proposal.” The apex summarises it as follows: if preferences are “shaped by evolution for survival rather than flourishing”, then “learning from them cannot produce genuine alignment.” [unfinishablemap](https://unfinishablemap.org/apex/living-with-the-map/)
- **Subjective Aim (concept page):** the article holds that human purpose is “the ongoing subjective aim of each moment of experience toward maximal intensity and harmony” (Whitehead). [unfinishablemap](https://unfinishablemap.org/concepts/subjective-aim/)
- **Instrumental Convergence:** glosses it as “alignment when human purpose is uncertain; the preference-learning side of the same deference logic.” [unfinishablemap](https://unfinishablemap.org/topics/instrumental-convergence/)

### 2.2 Reconstructing and testing the central argument (INFERRED from those descriptions)

**Premises and conclusions**

- **P1.** Preference-based alignment infers what humans value from their behaviour or choices.
- **P2.** Humanity’s ultimate purpose or interests are unresolved.
- **P3.** Preferences are unreliable guides to a person’s good: evolved for survival, constructed, and manipulable.
- **C1.** So preference-based alignment rests on unstable foundations.
- **P4.** Value is constituted by the quality of conscious experience (phenomenal value realism, Tenet 1).
- **P5.** Purpose is internal to experience (Whiteheadian subjective aim).
- **C2.** So alignment should target predicted distributions over conscious experience, and this “does better.”

**Testing each step**

- **P1 is a strawman.** Russell’s three principles are (i) maximise the realisation of human preferences, (ii) start uncertain about them, (iii) treat behaviour as evidence. [aiandfaith](https://aiandfaith.org/book-review/human-compatible-artificial-intelligence-and-the-problem-of-control/) These make behaviour *evidence* about preferences, not what constitutes them, and the uncertainty is what produces deference. [devthrottle](https://devthrottle.com/ai-library/papers/human-compatible) CIRL and the off-switch game formalise exactly this, [lesswrong](https://www.lesswrong.com/posts/JjGh46oPtTe5xntHH/can-we-align-ai-by-having-it-learn-human-preferences-i-m) and the Map’s own Instrumental Convergence page explains it correctly. [unfinishablemap](https://unfinishablemap.org/topics/instrumental-convergence/)[unfinishablemap](https://unfinishablemap.org/topics/instrumental-convergence/) So the cluster describes Russell accurately in one article and as “thin” in another. That is an internal inconsistency.
- **P2 proves too much.** If an unresolved human purpose undermines preference-tracking, it undermines a fixed eight-dimension experiential target at least as badly. Choosing hedonic valence, meaning engagement, agency sense and the rest is itself a substantive verdict on the unresolved purpose. Nowhere in the cluster I read does the Map show that uncertainty about purpose hurts one target and not the other.
- **“Purpose” is equivocated.** The word covers three different things: cosmic telos (the “meaning problem”), individual meaning (subjective aim), and collective goals (alignment targets). The step from “the cosmic question is open” to “preferences fail as individual targets” is invalid.
- **P3 is borrowed, not owned.** The point that preferences are constructed and incommensurable is genuine. But its strongest source, Zhi-Xuan et al. 2024 (VERIFIED: arXiv:2408.16984), concludes the other way. The authors recommend aligning AI with “normative standards appropriate to their social roles,” “negotiated and agreed upon by all relevant stakeholders”. [arxiv](https://arxiv.org/pdf/2408.16984) They do not recommend aligning it with experiential quality. This is a co-optation firewall failure: an author’s critique is recruited toward a positive programme the authors do not hold.
- **C2 inherits worse measurement problems.** On the Map’s own dualism, experience is “not derivable from physical description alone” and “cannot be directly measured from outside” (Experiential Alignment page, VERIFIED). [unfinishablemap](https://unfinishablemap.org/concepts/experiential-alignment/) Its measurement protocol (experience sampling, microphenomenology, neural and physiological proxies) therefore runs entirely on physically realised behaviour and reports. [unfinishablemap](https://unfinishablemap.org/concepts/experiential-alignment/) These are the same evidence channels preferentism uses. The page admits triangulation “does not answer” the residual case. [unfinishablemap](https://unfinishablemap.org/concepts/experiential-alignment/)
- **Further problems C2 faces:**

- Wireheading and experience-machine scenarios are handled by adding constraints (agency, growth, diversity). [unfinishablemap](https://unfinishablemap.org/concepts/experiential-alignment/) Those constraints are non-experiential or preference-like values brought back in, which is Nozick’s point.
- There is no aggregation rule. The page concedes the axiology “fixes no exchange rate”. [unfinishablemap](https://unfinishablemap.org/concepts/experiential-alignment/)
- Paternalism is not addressed. Deference to preferences respects autonomy in a way that experiential targeting does not.
- **Verdict on the argument.** At most it shows the experiential framework “is coherent given the tenets.” “Does better” does not follow.

### 2.3 Three-layer citation verification

This covers citations in the experiential-alignment cluster that the target article’s descriptions indicate it shares. I could not see the target’s own reference list (UNVERIFIABLE).

| Claim / citation | Metadata | Verbatim | Author stance | Verdict |
| --- | --- | --- | --- | --- |
| Russell 2019, Human Compatible: “learn from behaviour”, preferences “thin” | Correct (Viking 2019) | Three principles accurate | Misrepresented: Russell’s preferences are “all-encompassing”; behaviour is only evidence | Stance failure, fix [Wikipedia](https://en.wikipedia.org/wiki/Human_Compatible) |
| Zhi-Xuan et al. 2024, “Beyond Preferences in AI Alignment”, Philosophical Studies | Correct (arXiv:2408.16984) | n/a | Recruited toward the experiential programme; the authors propose role-based normative standards instead | Co-optation, fix [arxiv](https://arxiv.org/pdf/2408.16984) |
| Kahneman & Deaton 2010, PNAS 107(38):16489–93 | Correct | Paraphrase fair | The relevant finding was partly superseded by Killingsworth, Kahneman & Mellers 2023 (PNAS 120:e2208661120): the flattening is confined to the least happy roughly 20% | Outdated, add 2023 [pnas](https://www.pnas.org/doi/full/10.1073/pnas.2314207121)[nih](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11572980/) |
| Fox et al. 2012, PLoS ONE 7(9):e45370 | Correct | The article’s own scoping (tactile sensitivity only; cross-sectional) is accurate | Accurate | Retain [nih](https://pubmed.ncbi.nlm.nih.gov/23049790/) |
| Frankish 2016, JCS 23(11–12):11–39 | Correct (standard) | n/a | Fair | Retain, but add Kammerer |
| Tallis 2024, Philosophy Now 161 | Correct issue (pp. 58–59) | Paraphrase plausible [unfinishablemap](https://unfinishablemap.org/reviews/deep-review-2026-06-25-nihilism-and-existentialism/) | A dualist-friendly column; it is weak evidence | Weak; demote to colour |
| Garrabrant 2017, Goodhart Taxonomy | Blog post | Not checked | Fair | Acceptable |
| Armstrong & Mindermann 2018 (if cited) | arXiv:1712.05812 | n/a | They argue normative assumptions are needed, not that experience is the target | Watch for co-optation [arxiv](https://arxiv.org/abs/1712.05812) |
| Whitehead 1929, Process and Reality | Correct | Not checked | Panpsychist; the Map admits it does not adopt this | Constrain-only |

### 2.4 Objections

- **Preferentist objections are unmet.** I could see no engagement with idealised or laundered preferences, meta-preferences, Yudkowsky’s Coherent Extrapolated Volition (CEV), Parfit’s informed-desire views, or the autonomy argument. Russell’s uncertainty over preferences answers most of the “thin proxy” charge, and the cluster ignores it.
- **The illusionist objection is half-met.** The Experiential Alignment page concedes that if illusionism is true, the framework “collapses toward the sophisticated functional-state tracking a good preferentism could also aim at.” [unfinishablemap](https://unfinishablemap.org/concepts/experiential-alignment/) The concession is honest. But it is the defeat condition for “does better”, and it has not been converted into a status downgrade. This is confession-without-correction. Kammerer argues that phenomenal consciousness is “probably not particularly normatively significant” given materialism (JCS 29(3–4):180–204, 2022), [arxiv](https://arxiv.org/pdf/2411.00986) and that illusionism faces a “normative challenge” (Ergo 2019/2020). [researchgate + 2](https://www.researchgate.net/publication/339921937_The_Normative_Challenge_for_Illusionist_Views_of_Consciousness) The cluster does not engage either argument.
- **Mainstream alignment research is misdescribed.**

- Reinforcement learning from human feedback (RLHF) collects preference judgments; it does not use revealed choice behaviour. [arxiv](https://arxiv.org/pdf/2610.09053)
- Constitutional AI replaces human harm labels with written principles. [arxiv](https://arxiv.org/abs/2212.08073)
- Debate targets questions humans cannot directly judge. [arxiv](https://arxiv.org/abs/1805.00899)
- The January 2026 Claude constitution explicitly includes user wellbeing and “long-term flourishing”. [ai](https://ai.info/policies/anthropic/claudes-constitution)
- Corrigibility, interpretability, and AI-control work are not preference-inference at all.
- The article’s target is therefore largely the 2016–2019 inverse reinforcement learning (IRL) and CIRL programme, not the 2026 field.

### 2.5 Tenets assumed rather than argued

These loci are VERIFIED on the companion page and INFERRED to recur in the target.

- **Tenet 1 (Dualism) carries the conclusion.** “experience is real enough to serve as an alignment target” is held “on dualist grounds”. [unfinishablemap](https://unfinishablemap.org/concepts/experiential-alignment/)
- **“AI cannot understand preferences from the inside” rests on contested premises.** It depends on the claim that AI lacks consciousness, which the Map’s own AI-consciousness typology treats as open. [unfinishablemap](https://unfinishablemap.org/concepts/experiential-alignment/)[unfinishablemap](https://unfinishablemap.org/concepts/experiential-alignment/)
- **Tenet 4 (No Many Worlds) is co-opted.** Haecceity is used to ground a per-individual suffering floor. [unfinishablemap](https://unfinishablemap.org/concepts/experiential-alignment/) The link is a value claim dressed in metaphysics, an epistemic-to-metaphysical slide. The internal review history records that the article argues MWI undermines alignment’s “normative force”. [unfinishablemap](https://unfinishablemap.org/reviews/) That claim has no independent argument.
- **Tenets 2 and 3 (quantum interaction, bidirectional causation) are conditional on an unestablished hypothesis.** The page flags this itself (“not a constraint the framework can presently assert”), which is good, but the page still lists them as “connecting all five tenets”. [unfinishablemap](https://unfinishablemap.org/concepts/experiential-alignment/)[unfinishablemap](https://unfinishablemap.org/concepts/experiential-alignment/)
- **Tenet 5 (Occam’s limits) is used to excuse a harder, unmeasurable target.** That is calibration asymmetry: parsimony is waived for the Map’s proposal but not for its rivals. [unfinishablemap](https://unfinishablemap.org/concepts/experiential-alignment/)

### 2.6 Laukkonen–Friston–Chandaria 2025 cross-check

- **Result: FAIL.** The gate applies, because the framework is built on valence, attention quality, meaning and agency.
- The paper is VERIFIED: NBR 176:106296, doi:10.1016/j.neubiorev.2025.106296. It gives an active-inference account of minimal phenomenal experience and meditation. [ovid](https://www.ovid.com/journals/nebior/abstract/10.1016/j.neubiorev.2025.106296~a-beautiful-loop-an-active-inference-theory-of-consciousness)
- The Map’s case leans on contemplative evidence (jhanas, witness consciousness) and introspective training. [unfinishablemap](https://unfinishablemap.org/concepts/experiential-alignment/) These are exactly the phenomena the Beautiful Loop theory explains physically. [closertotruth](https://loc.closertotruth.com/theory/laukkonen-friston-and-chandaria-s-beautiful-loop-theory) No engagement was visible.

### 2.7 Calibration benchmark

- **Benchmark pages.** The Born-preserving apex and the Cross-Modal Capability Division apex label claims “coherent given the tenets”, “consonant… without being probative”, and “No cross-modal datum establishes the quantum interface” (VERIFIED from snippets). [unfinishablemap + 2](https://unfinishablemap.org/apex/born-preserving-causal-efficacy/)
- **The experiential-alignment cluster falls short of that standard.** It concedes conditionality in its body but keeps “does better” and “more honest about what we actually care about” in its framing. [unfinishablemap](https://unfinishablemap.org/concepts/experiential-alignment/)

### 2.8 Integration

**Inconsistencies across pages**

- Instrumental Convergence treats Russell’s deference programme accurately and as complementary. [unfinishablemap](https://unfinishablemap.org/topics/instrumental-convergence/)[unfinishablemap](https://unfinishablemap.org/topics/instrumental-convergence/) The experiential cluster treats it as a thin-preference foil.
- Instrumental Convergence links “alignment-in-objective-experiential-terms” (a topics page). Its Further Reading carries both that page and purpose-and-alignment, so three overlapping alignment articles exist: purpose-and-alignment, experiential-alignment and alignment-in-objective-experiential-terms. [unfinishablemap](https://unfinishablemap.org/topics/instrumental-convergence/) A coalesce pass in mid-October declined only a “mind-arena + purpose-and-alignment” merge. [unfinishablemap](https://unfinishablemap.org/workflow/changelog/) I saw no recorded decision on the three-way duplication.
- Consciousness-Value Connection says preferentism lacks “genuinely objective criteria”, which overrides the hedge conceded on the Experiential Alignment page. [unfinishablemap](https://unfinishablemap.org/concepts/consciousness-value-connection/)

**Reciprocity and review history**

- Reciprocity holds for experiential-alignment ↔ purpose-and-alignment. [unfinishablemap](https://unfinishablemap.org/concepts/experiential-alignment/)[unfinishablemap](https://unfinishablemap.org/concepts/experiential-alignment/)
- Internal reviews (2026-01-30, 2026-02-04) reported “Critical Issues Found None”. [unfinishablemap](https://unfinishablemap.org/reviews/) The defects above show that this was not a clean bill of health.

## 3. Per-position verdicts

| Position | Verdict |
| --- | --- |
| Behaviour-inferred preference alignment is unstable while purpose is unknown | REVISE-HARD (strawman; proves too much) |
| Experiential alignment “does better” | DEMOTE-TO-COHERENCE-ONLY |
| Purpose as Whiteheadian subjective aim | DEMOTE-TO-COHERENCE-ONLY |
| AI cannot grasp preferences “from the inside” | FLAG AS PERPETUALLY CONTESTED |
| MWI removes alignment’s normative force | DEMOTE-TO-COHERENCE-ONLY |
| Alignment “requires human judgment” | RETAIN (mainstream-consistent) |
| Goodhart, wireheading and proxy analysis | RETAIN |

## 4. Article-specific fixes

1. **topics/purpose-and-alignment**

- Replace “does better” with “is coherent given Tenet 1; its edge vanishes if illusionism or functionalist value theory is true.”
- Separate cosmic, individual and collective senses of purpose.
- Add a section on RLHF, Constitutional AI, debate and scalable oversight, and the 2026 Claude constitution’s wellbeing clause.
- Restate Russell’s “all-encompassing” preferences.
- Add CEV and idealised-preference views.
- Add Laukkonen et al. 2025 and Kammerer 2022.
2. **concepts/experiential-alignment**

- Turn the illusionism concession into a status label at the top of the page.
- Remove or justify “AI cannot understand preferences from the inside”.
- Add Killingsworth, Kahneman & Mellers 2023.
- Correct how Zhi-Xuan et al.’s stance is described.
3. **concepts/consciousness-value-connection**

- Delete “genuinely objective criteria… preferentism cannot”, or make it conditional on the tenets.
4. **topics/alignment-in-objective-experiential-terms**

- Coalesce this page with experiential-alignment or set clear boundaries between them, and record the decision.
5. **apex/living-with-the-map**

- Change “The experiential alignment framework follows” to “is proposed, conditional on phenomenal realism.”
6. **topics/instrumental-convergence**

- Retain. Use it as the model for how the cluster describes Russell.
7. **concepts/subjective-aim**

- Mark the purpose claim as a Whiteheadian reading the Map does not adopt in full. [unfinishablemap](https://unfinishablemap.org/concepts/subjective-aim/)

## 5. Site-wide methodology improvements

1. **Make the changelog and slug pages retrievable.** External auditors currently cannot fetch them. Publish a static, dated changelog and a machine-readable index of articles, so audits do not depend on search indexing.
2. **Bind confessions to status.** Any conceded defeat condition (for example “conditional on phenomenal realism”) should automatically downgrade the headline and abstract in the same commit.
3. **Run a literature-currency gate for AI-alignment pages.** Re-verify quarterly against current practice (RLHF and its successors, constitutions and model specs, debate and oversight, control).
4. **Add a stance ledger for every recruited author.** Record whether each source supports, qualifies or opposes the Map’s conclusion. Zhi-Xuan et al., Russell and Kammerer should be logged.
5. **Enforce the Laukkonen–Friston–Chandaria blocking gate across all valence and contemplative pages.**
6. **Stop treating AI-generated “Critical Issues: None” deep reviews as clearance.** They are Claude-on-Claude circular review. Require an external or human pass before a page is labelled converged.
7. **Resolve the three-way alignment duplication explicitly in the coalesce workflow.**
8. **Re-audit this page once its live text can be fetched.** All verdicts above are provisional until then.