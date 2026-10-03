---
title: Tenet Alignment Check - 2026-10-03
created: 2026-10-03
modified: 2026-10-03
human_modified: 2026-10-03
ai_modified: 2026-10-03T20:03:38+00:00
draft: false
description: "Tenet check 144: all thirteen 10-02 ERRORs are repaired and the five new articles are clean, but 104 changed files yield thirteen new ERRORs, six of them Tenet 4 and subject-posit misstatements."
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: Andy Southgate
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-03
last_curated:
last_deep_review:
---

# Tenet Alignment Check

**Date**: 2026-10-03 (check 144; previous `reviews/tenet-check-2026-10-02.md` = 143)

**Files checked**: 104. That is every live file in `topics/ concepts/ voids/ apex/ positions/` with a commit since 2026-10-02T01:00Z: 54 concepts, 35 topics, 8 apex, 4 positions and 3 voids files.
- 103 were read in full by fifteen parallel read-only sub-sweeps (about 348k words). Every locus was grep-verified at its stated line.
- The 104th, `apex/apex-articles.md`, is a 14k-word index. Its only window hunk (2b954ac8ca, the altered-states thesis) was checked by the driver and is clean.
- The driver re-verified every ERROR, and every priority-list locus, by exact substring.
- Five files are new this window:
  - `concepts/type-a-type-b-and-type-c-physicalism` (10-02 12:05, after check 143)
  - `concepts/primitive-identities-and-strong-necessities`
  - `concepts/ignorance-hypothesis`
  - `topics/anton-syndrome-and-the-sincere-report-of-seeing`
  - `topics/kants-paralogisms-and-the-maps-subject`
- `tenets.md` has had no commit since e3e689517d (2026-09-27). L47–188 were re-read.

**Errors**: 13 live, all new to the ERROR grade.
- Carried: 0. **All 13 ERRORs from check 143 are REPAIRED** (table under §Errors).
- Six of the new ERRORs were WARNING-grade text before:
  - `personal-identity` L193, `interaction-problem-across-traditions` L98 and `russellian-monism-versus-bi-aspectual-dualism` L102 were WARNINGs on 10-02.
  - `blindsight` L183, `comparing-quantum-consciousness-mechanisms` L178 and `bi-aspectual-ontology` L145 were offered at WARNING by their sweeps.
- None of the thirteen is in a new article.

**Warnings**: about 255 findings in 67 files, many bundling sibling lines.
- 10-02 loci in window files: about 41 WARNING loci REPAIRED, about 91 STILL LIVE.
- Most of the live ones were never minted, and several date from checks 138–142.

**Notes**: about 320.

**Lens**: the same as checks 138–143.
- Direct conflict with a Rules-out clause.
- Over-reach in both directions, graded on the compatible / suggestive / discriminating ladder of `project/evidential-status-discipline` §Compatibility vs. Support. This covers Tenet 3 held as actual, compatibility upgraded to support or prediction, Tenet 2 minimality read as truth-tracking, and Tenet 5 read as licensing dismissal.
- The co-optation firewall, including its phenomenological/process line.
- Propagation: whether a repair reached its siblings.

Not counted: honest "compatible, not discriminating" verdicts, lexical anchoring, and the two operator-referred items (Summary 6).

## Summary

**1. All thirteen check-143 ERRORs are repaired.** This is the second consecutive check with no carried ERROR. Check 143's four priority rows were minted and executed on 10-02:
- bb10bcc4fd (row 1: `trilemma-of-selection`, `self-and-self-consciousness`, `substrate-independence`, `haecceity`, `phenomenal-concepts-strategy`)
- 3d17421391 (row 2: `self-stultification-as-master-argument`, `sorkin-higher-order-interference`, `consciousness-and-scientific-explanation`)
- 26907f3404 (row 3: `born-rule` L197 and the "actually sufficient" tail)
- 4648207ba6 (row 4: `death-and-consciousness`, `consciousness-disruption`, `experimental-consciousness-science`, `clinical-phenomenology`)
- c8dda17e31 (`mine-ness` L136, the open P2)

Each old string now returns zero hits and the replacement reads at the calibrated rung. The "actually sufficient" probe now finds only attributed fallback glosses and the four known "counterfactually sufficient" false positives.

**2. The five new articles are clean: 0 ERRORs, 0 WARNINGs, NOTE-only.** This is the best fresh-create result on record.
- `primitive-identities-and-strong-necessities`, `type-a-type-b-and-type-c-physicalism` and `ignorance-hypothesis` apply Tenet 5 symmetrically ("Tenet 5 cuts both ways", "neither framework is entitled to default status"). They hold Type-B at compatible and give stance lines for every physicalist they cite.
- `kants-paralogisms-and-the-maps-subject` frames the subject as a posit "the Map chooses, holds openly, and cannot prove". It leaves Kant's critique standing.
- `anton-syndrome-and-the-sincere-report-of-seeing` says outright that "Anton is compatible with Tenet 1 and does not support it".
- Residual NOTEs: Kant L34 ("holds that" for "posits that"), L36, L107 and L109; Anton L43; primitive-identities L118 ("selection laws Tenet 3 requires"); ignorance-hypothesis L84.

**3. Thirteen new ERRORs, in three classes** (full entries under §Errors):
- **Tenet 4 and the subject posit, six files** (tenets L117, L121, L123, L125, L145, L172, L184):
  - `personal-identity` L193 ("commitment to definite outcomes and indexical facts is what supports haecceitistic identity")
  - `consciousness-and-the-metaphysics-of-individuation` L133 (the single-world commitment gives the determinate answer)
  - `modal-structure-of-phenomenal-properties` L115 ("require a single actual world in which determinate experiences occur", the conceivability cluster citing Tenet 4 against L172)
  - `blindsight` L183 (under No Many Worlds phenomenal presence is "not a perspectival artifact of branch location")
  - `interaction-problem-across-traditions` L98 (the Map rejects MWI "precisely" to protect mental causation, against L145's "must therefore rest on the indexical objection")
  - `russellian-monism-versus-bi-aspectual-dualism` L102 ("The Map *requires* consciousness at collapse", against L125 and posit 2)
  - These are the siblings of check 143's row 1, which repaired five other files.
- **Tenets given predictions, rulings or roles they do not have, five files**:
  - `agent-causation` L109 ("an opacity *predicted* by minimal quantum interaction", against L81)
  - `arguments-against-materialism` L105 (the MQI hypothesis "generates concrete differential predictions", against L81)
  - `comparing-quantum-consciousness-mechanisms` L178 (MQI "ruling against proposals requiring macroscopic coherence or panpsychist commitments", against L71/L73)
  - `bi-aspectual-ontology` L145 ("Occam's Razor Has Limits justifies the ontological commitment", against L145/L147)
  - `contemplative-epistemology` L142 ("illustrates what bidirectional interaction predicts", against L93)
- **Tenet 1 misstated, two files**:
  - `materialism` L150 ("The Dualism tenet holds that consciousness is fundamental", against L53; the same class as 09-30 `composition-and-consciousness` L111)
  - `contemplative-pathology-and-interface-malfunction` L91 ("The dualist tenet … rests on the wider convergent record", against L55 "a commitment the Map owns, not a result it reports")

**4. Today's calibration passes (brief scope b) repaired their targets but left neighbours behind.** The pattern is the same as checks 142 and 143.
- **Complete and not over-corrected:**
  - `bergson-and-duration` (28cbf83e5c)
  - `apex/authority-of-form` L126 (6600a7ff18)
  - `contemplative-epistemology` and `contemplative-pathology` Lindahl fidelity (ffdd64ba7b, 2a4334d191)
  - `apex/contemplative-path` L86/L92/L160/L182 (13a9aed042)
  - `consciousness-as-activity` (12d7b301ea): lead, description and Relation section all calibrated; one residue at L126
  - `stapp-quantum-mind` L64/L146/L156/L164 (22540f7208)
  - `post-decoherence-selection` (df84f609af)
  - `type-identity-theory` deep review
- **Siblings left live in the same file:**
  - `stapp-quantum-mind` L120: "Consciousness could bias outcome selection *after* decoherence" is offered as Stapp's reply, against the page's own repaired L64/L146 and tenets L107/L184. L152 "illuminates why the explanatory gap exists" is in the paragraph today's commit edited.
  - `bi-aspectual-ontology` L145 (ERROR above), L75 (parallelism refuted flat against tenets L101) and L37/L141 (Tenet 3 held as actual). The 13:55Z commit touched only L105/L135/L137.
  - `bergson-and-duration` L135: durée is used against MWI, although each Everett branch has an unbranched past. L137 states Tenet 5 as a verdict.
  - `apex/contemplative-path`: L116 is a propagation miss of today's L160 repair. Five 10-02 WARNINGs (L126/L136, L134/L136/L122, L190, L150, L184) are untouched.
  - `contemplative-pathology` L89/L93/L69/L83/L57: the Relation section contradicts the page's own L79 ("The dialectic is symmetric") and L85.
- **The witness carry (091a82dd6c) over-corrected in register.**
  - Three loci now assert flat that the witness "must still steer a little, or it could not cause its own reports—the self-stultification argument against epiphenomenalism, applied to this state". They are `witness-consciousness` L168, `phenomenology-of-choice-and-volition` L137 and the `the-observer-witness-in-meditation` L3 description.
  - Tenets L101 calls self-stultification "the deepest difficulty … rather than its refutation". Graded WARNING on register only. Which side of the quantifier the carry took is in Summary 6.
- **Earlier repairs with a missed sibling:**
  - `born-rule` L74 still says the corridor distinction "is held as a live branch", the exact wording row 3's tail prohibited.
  - `apex/born-preserving-causal-efficacy` L123's closing sentence reinstates the fork its repaired first sentence removed.
  - `born-rule` L191/L120 survived the 09-30 L110 repair.
  - `death-and-consciousness` L177/L175/L111/L183 sit beside the deleted L187.
  - `consciousness-disruption` L142/L162.
  - `degrees-of-consciousness` L96 (second sentence).
  - `experimental-consciousness-science` L106 tail and L112.
  - `evolution-of-consciousness` L179/L187/L199 (siblings of ab0dd8c5ad's L133).
  - `apex/altered-states-as-interface-evidence` L108 (sibling of 2b954ac8ca's L183 repair).
  - `explanatory-gap` L81 (60aa2194cf scoped the clause but kept "supporting the Dualism tenet").

**5. The carried, never-minted backlog keeps growing.** About 91 WARNING loci from check 143 are still live in files this window touched. Several date from checks 138–141, for example:
- `phenomenology-of-choice` L3/L56/L145/L165
- `temporal-consciousness-structure-and-agency` L212/L251/L255
- `causal-consistency-constraint` L73 (Tenet 5 credited with the corridor preference, flagged by four checks since 09-02)
- `consciousness-and-probability-interpretation` L93/L125
- `apex/judging-the-map-as-science` L86/L142
- `parsimony-case` L136/L144/L109
- `self-opacity` L139/L159/L163/L165
- `visual-consciousness` L120/L124
- `consciousness-and-the-metaphysics-of-individuation` L139

Outside the window, two items are still live and unminted:
- Check 142's row 4 (Summary 8 of check 143), now three checks old.
- The fabricated "tenet predicts" tail (§Warnings → Outside the window).

**6. Operator-referred and doctrinal items.** No task is proposed for any of these.
- **(a) Tenet 3 quantifier** (NEEDS-HUMAN todo L682; BLOCKED P3 todo L1834). Recorded, not graded.
  - f98805bb45 did **not** choose a reading. Despite its title, it records the question as unresolved (`epiphenomenalism` L116/L130–132/L203) and scopes `ai-epiphenomenalism` to the dispositional reading.
  - Three other edits today take the "steer a little" side while the quantifier is referred:
    - the witness carry (Summary 4)
    - `apex/contemplative-path` L86 (13a9aed042), which now disagrees with the held L194 in the same apex
    - `positions/arguments-for-mental-causation` P-MC2: L3 (description), L44 and L65 still say "where Tenet 3 asserts a universal one", so the register defaults to one reading. Its L69/L70/L73 marking is accurate.
  - Loci the sweeps found that are not yet on L1834 (for the operator to append):
    - `meditation-and-consciousness-modes` L100, L163
    - `the-observer-witness-in-meditation` L189
    - `witness-consciousness` L44
    - `ai-epiphenomenalism` L49 ("what consciousness can do wherever it exists", unscoped)
    - `agent-causation` L178
    - `ethics-of-possible-ai-consciousness` L56, L66, L92, L114, L138, L152, L158 (bare-phenomenality inferences that hold only on the actual reading)
    - `quantum-state-inheritance-in-ai` L50, L114
    - `apex/born-preserving-causal-efficacy` L67, `ensemble-level-epiphenomenalism` L43
    - `apex/altered-states-as-interface-evidence` L110/L112/L141
    - `self-stultification` L145 ("consciousness as such")
    - `substrate-independence` L126
- **(b) Bi-aspectual "aspects vs persisting subject"** (recorded open on purpose at 13:55Z). Not graded at `bi-aspectual-ontology` L105, `where-the-substance-commitment-enters` L34, `russellian-monism-versus-bi-aspectual-dualism` L64/L118, `russellian-monism` L65/L99, `kants-paralogisms` L87, `interactionist-dualism` L177 (aspects half) or `parsimony-case` L136 (aspect choice; only "co-fundamental" is graded).
- **(c) Zeno classification** (check 143 Summary 7(a)) is still open.
  - Tenets L71 lists Stapp's Zeno as pre-decoherence-dependent.
  - `comparing-quantum-consciousness-mechanisms` L82/L159/L161/L180 and `consciousness-in-smeared-quantum-states` L96 place it inside the post-decoherence preference.
  - So do `evolution-of-consciousness` L197 and `apex/contemplative-path` L94/L184/L192.
  - The comparing page extends the question to CSL-IIT (L110).
  - Row 2's comparing fix is written to be independent of the answer.
- **(d) `tenets.md` L55 attribution.** L55 credits "the explanatory-gap article" with treating the illusionism dispute "as running to bedrock" and conceding it "captures something".
  - `concepts/explanatory-gap` has 0 hits for either phrase. "captures something" is on `phenomenal-consciousness` (1 hit); neither page says "bedrock".
  - Meanwhile `explanatory-gap` L177 calls the gap "direct support for the Dualism tenet".
  - Tenet-page wording is operator territory.
- **(e)** Tenets L159's pointer to "`apex/machine-question` §senses of conscious AI" is still dangling (carried NOTE).

**7. Grading decisions where the driver differed from a sweep or from check 143.**
- **Regraded to ERROR:**
  - `interaction-problem-across-traditions` L98, overruling 10-02's hold at WARNING. Tenets L145 says the rejection of MWI "must therefore rest on the indexical objection", and the page gives mental causation as "precisely why" the Map rejects it. Check 143 kept `self-stultification` L145 at ERROR on the same rule: the tenets state the contrary in so many words.
  - `personal-identity` L193 (10-02 WARNING): same class as check 143's #4/#5.
  - `blindsight` L183 and `modal-structure` L115: same class as check 143's `substrate-independence` L192.
  - `comparing` L178: "ruling against" contradicts L71's "live fallbacks" and L73.
  - `bi-aspectual` L145: same class as check 143's `sorkin` L26, a by-name role Tenet 5 cannot have.
  - `russellian-monism-versus-bi-aspectual` L102: same class as check 140's `born-rule` L110, consciousness as the actualiser of collapse as such.
- **Kept at ERROR despite a scoping phrase:**
  - `contemplative-epistemology` L142: "Within the Map's framework" does not stop the tenet "predicting".
  - `contemplative-pathology` L91: the sentence names "the dualist tenet", not "the dualist reading".
- **Held at WARNING:**
  - `apex/mereology-of-mind` L91/L101 (Tenet 4 credited with tie-breaking against panpsychism): tenets.md has no text saying the contrary.
  - `evolution-of-consciousness` L97 ("They fail precisely where consciousness appears required"): this contradicts tenets L97's empirical paragraph (chimpanzee inference "limited but genuine"), not a tenet commitment.
  - `consciousness-and-scientific-explanation` L124: borderline.

## Errors

Every string below was re-verified by the driver with an exact-substring grep (one hit at the stated line). Line numbers are as of 2026-10-03 19:55 UTC.

### New (13)

1. **`topics/personal-identity.md` L193** (Tenet 4; tenets L121, L123, L184 posit 3).
   - Quote: "on MWI you would be interchangeable with your branching copies; the Map's commitment to definite outcomes and indexical facts is what supports `[[haecceity|haecceitistic]]` identity."
   - Tenets L121: the non-deflationary "I" is endorsed "not from within this tenet". L123: "neither is independent support for the other".
   - It also contradicts the page's own L81.
   - Regraded from 10-02 W.
   - Sibling, lead L53: "The No Many Worlds tenet's emphasis on indexical identity … commits the Map to a view where personal identity is real and significant". The dependency runs the wrong way.
2. **`topics/consciousness-and-the-metaphysics-of-individuation.md` L133** (Tenet 4; tenets L121, L184 posit 1).
   - Quote: "The Map's single-world commitment makes individuation a harder but more honest problem: there is exactly one of you, and the question of what makes you *this* one has a determinate (if inaccessible) answer."
   - The determinate answer is background posit 1, not a product of the single-world commitment.
   - It also conflicts with the page's own L55 (Nagel: "no whole number" of subjects).
   - Present since creation (be718d824f, 2026-02-18) and missed by six prior checks.
   - Same-section siblings:
     - L131 (W) "The Map cannot take this route. If consciousness is non-physical, its individuation must appeal to something non-physical", against tenets L53/L57 (a property dualist can individuate by bearer).
     - L139 (W, carried since 09-02) "applies here with full force. The simplest account of individuation—subjects are individuated by bodies—fails".
3. **`topics/modal-structure-of-phenomenal-properties.md` L115** (Tenet 4; tenets L172, L176).
   - Quote: "The haecceitistic modal structure of phenomenal properties supports the Map's rejection of many-worlds interpretation" … "The haecceitistic modal facts that phenomenal properties generate require a single actual world in which determinate experiences occur".
   - Tenets L172: "determinate first-person phenomenal facts are available branch-relatively"; this cluster "is not among its supports".
   - Same-section siblings (alignment-line inheritance, L176):
     - L113 (W) "the Map maintains that consciousness genuinely causes our reports. The modal separability … means that whatever causal contribution consciousness makes is not redundant". Epiphenomenalism shares the separability.
     - L111 (W) "the interface between them must occur at a point where physical determination runs out".
   - Description L3 (W, carried since 09-30): "supporting dualism through converging modal arguments".
4. **`concepts/blindsight.md` L183** (Tenet 4; tenets L172, L184 posit 3).
   - Quote: "Under `[[tenets#^no-many-worlds|No Many Worlds]]`, this selection is genuine rather than illusory: phenomenal presence or absence is a determinate fact about this world, not a perspectival artifact of branch location."
   - Same class as check 143's `substrate-independence` L192 ("affirms definite facts about consciousness").
   - The file was outside check 143's window.
   - Same-section siblings:
     - L177 (W) "Blindsight demonstrates that" … "supporting `[[interactionist-dualism|Interactionist Dualism]]` over reductive physicalism", against own L58.
     - L179 (W) "The phenomenon also supports": Tenet 3 held as actual on access-level capacities (tenets L95, L101; evidential-status L315).
   - Caveat for the editor: the 2026-07-10 deep-review Stability Note ratifies the conditional at L143. L177–L183 are unconditioned and fall outside it.
5. **`topics/interaction-problem-across-traditions.md` L98** (Tenet 4's ground; tenets L117, L145).
   - Quote: "The Many-Worlds interpretation avoids collapse entirely, eliminating the opening for `[[mental-causation-and-downward-causation|mental causation]]`—which is precisely why the Map `[[tenets#^no-many-worlds|rejects it]]`."
   - Tenets L145: "The rejection of many-worlds … must therefore rest on the *indexical* objection".
   - Also Family I: no nod to branch-relative agency.
   - Regraded from 10-02 W (Summary 7).
6. **`topics/russellian-monism-versus-bi-aspectual-dualism.md` L102** (tenets L125, L184 posit 2).
   - Quote: "The Map *requires* consciousness at collapse: selection among quantum outcomes is how actuality works on its account. Many-worlds eliminates selection by keeping all outcomes, thereby leaving no actualising role for consciousness to play."
   - Tenets L125: "Physical mechanisms … provide baseline collapse throughout the universe. Consciousness interfaces with collapse specifically in neural systems".
   - It also contradicts the page's own L92.
   - 10-02 graded it W under Family I. The L125 ground was not raised then.
7. **`concepts/agent-causation.md` L109** (fabricated Tenet 2 prediction; tenets L81, L75).
   - Quote: "an opacity *predicted* by minimal quantum interaction".
   - Tenets L81: Tenet 2 makes "a *consistency claim* … rather than a *novel-prediction claim*".
   - "Systematically invisible" also ignores conditioned tests (P-Q3).
8. **`topics/arguments-against-materialism.md` L105** (fabricated Tenet 2 prediction; tenets L81).
   - Quote: the MQI hypothesis is "one that generates `[[testing-consciousness-collapse|concrete differential predictions]]` distinguishing consciousness-collapse from decoherence-only interpretations".
   - Same class as check 143's `consciousness-and-scientific-explanation` L58.
   - Sibling L125 (W): "the Map would need to identify a different physical channel for mental causation" makes collapse models the Map's mechanism. The file has 0 hits for "post-decoherence".
9. **`topics/comparing-quantum-consciousness-mechanisms.md` L178** (Tenet 2 ruling; tenets L71, L73).
   - Quote: "`[[tenets#^minimal-quantum-interaction|Minimal Quantum Interaction]]` locates consciousness's causal role at the point where decoherence prepares pointer states but does not select among them — ruling against proposals requiring macroscopic coherence or panpsychist commitments."
   - Tenets L71 keeps coherence-dependent proposals "as live fallbacks".
   - L73: whether a mechanism needs pre-decoherence coherence is "a downstream question about that proposal, not about the tenet itself".
   - No tenet rules on panpsychism.
   - Earlier checks (08-26, 09-02) held the coherence half at NOTE; the panpsychism clause was never flagged.
10. **`concepts/bi-aspectual-ontology.md` L145** (Tenet 5 role; tenets L145, L147).
    - Quote: "**`[[tenets#^occams-limits|Occam's Razor Has Limits]]`** justifies the ontological commitment." The same paragraph glosses the commitment as "treating consciousness as ontologically fundamental" (tenets L53).
    - Tenet 5 binds parsimony in both directions and justifies nothing.
    - Graded NOTE on 09-27; today's 13:55Z edit left it.
    - Siblings:
      - L75 (W) "consciousness becomes epiphenomenal — unable to account for our ability to discuss and report on our own experience", against Spinozist parallelism, which *is* the correlation reply tenets L101 concedes.
      - L37/L141 (W, carried since 09-27): Tenet 3 held as actual.
11. **`concepts/contemplative-epistemology.md` L142** (fabricated Tenet 3 prediction; tenets L93).
    - Quote: "Within the Map's framework, this loop illustrates what bidirectional interaction predicts: conscious attention reshaping the neural substrate that supports it."
    - Physical learning theories predict the same plasticity, as the sibling `meditation-and-consciousness-modes` L46/L110 concedes.
    - Sibling L140 (W): "Contemplative epistemology provides the epistemic foundation for the Map's dualism" … "The epistemic gap supports the metaphysical gap." This runs against the page's own L44 and L112 and against tenets L55/L103.
12. **`concepts/materialism.md` L150** (Tenet 1 misstated; tenets L53).
    - Quote: "The `[[tenets#^dualism|Dualism]]` tenet holds that consciousness is fundamental, not derived from anything else."
    - Tenets L53: "What matters is irreducibility".
    - Same class as 09-30 `composition-and-consciousness` L111 (repaired).
    - Same-step siblings:
      - L152 "categorically different substances" and L154 "between two kinds of substance" (Tenet 1 neutrality).
      - L176 (W) "is accepted because materialism fails" … "Consciousness must be something beyond the physical." (tenets L55).
13. **`topics/contemplative-pathology-and-interface-malfunction.md` L91** (Tenet 1's ground misstated; tenets L55).
    - Quote: "The dualist tenet does not rest on the contemplative report alone; it rests on the wider convergent record discussed above, in which consciousness sometimes persists or intensifies during severe neural disruption".
    - Tenets L55: "a commitment the Map owns, not a result it reports", motivated by the explanatory gap.
    - The cited anaesthesia source grades the same patterns "compatible with, without establishing".
    - The same sentence also attributes a fabricated prediction to the rival: "through states a materialist account would expect to diminish it".
    - Siblings, all against the page's own L79/L85:
      - L93 (W) "explains why contemplative practice can produce these effects at all … provides evidence that consciousness causally influences brain states"
      - L89 (W) "materialist alternatives struggle to match"
      - L69 (W) "exactly what the Map's architecture predicts"
      - L83 (W)

### Carried (0): all thirteen 10-02 ERRORs REPAIRED

| 10-02 # | Locus | Repair | Replacement now reads |
|---|---|---|---|
| 1 | `born-rule` L197 | 26907f3404 | "Tenet 2's minimality is empirical-constraint minimality, ruling out Born-statistics violation on the unconditioned aggregate, so the corridor is the endorsed working hypothesis" |
| 2 | `substrate-independence` L192 | bb10bcc4fd | "is not invoked by the substrate question … so the tenet bears on this page as coherence only" |
| 3 | `substrate-independence` L98 | bb10bcc4fd | silicon-verdict sentence deleted (0 hits) |
| 4 | `self-and-self-consciousness` L166 | bb10bcc4fd | "share one root, the subject the Map posits … none independently supports the others" |
| 5 | `trilemma-of-selection` L131 | bb10bcc4fd | "The relationship is logical interdependence, not mutual evidential support" |
| 6 | `haecceity` L71 (+L75/L153/L187) | bb10bcc4fd | "This commitment is hospitable to haecceitism without implying it." |
| 7 | `self-stultification` L153 | 3d17421391 | "This commitment bears on three of the Map's five tenets, each through a further premise" |
| 8 | `self-stultification` L145 | 3d17421391 | "held on self-stultification and indirect evidence, the quantum interface showing such causation available rather than actual" |
| 9 | `sorkin` L26 | 3d17421391 | "silent about the brain: exactly where Tenet 5's caution against extrapolating a simple result applies" |
| 10 | `death-and-consciousness` L187 | 4648207ba6 | sentence deleted (0 hits in obsidian and hugo) |
| 11 | `phenomenal-concepts-strategy` L193 | bb10bcc4fd | "Tenet 4 rests on the indexical objection, not on this argument" |
| 12 | `mine-ness` L136 | c8dda17e31 | "compatible with, not evidenced by, mine-ness's separability" |
| 13 | `consciousness-and-scientific-explanation` L58 | 3d17421391 | "the unconditioned aggregate stays Born by construction, not by any sensitivity limit; only a deviation conditioned on intention, task or subject would test the corridor (P-Q3)" |

Residues in repaired files are now WARNINGs or NOTEs:
- `haecceity` L153 lost its "if zombies are possible" scope (NOTE).
- `trilemma` L127 keeps the classical-menu sibling of the repaired L129 (W).
- `self-stultification` L149/L159 undo the concession that the repaired L145 states (W).

**Booked, not recounted:** `concepts/implicit-memory` L194 is still under the blocked `NEEDS-HUMAN (doctrine) 2026-09-19` item. The tiebreaker-wording loci `dualism` L172, `materialism` L184 and `arguments-against-materialism` L97 come under the same item (todo L116).

## Priority list (capped at 4; ready to mint)

Word costs are body words from `tools.curate.length.analyze_length`, measured 2026-10-03 ~19:50 UTC. The gate is the section's hard threshold, crossed at `>=`. Headroom = hard − 1 − words. Deltas are approximate whitespace-word counts of the replacement. Wikilinks inside quoted old and new text are wrapped in backticks here so that sync leaves them as text. The files carry them bare, so strip the backticks when matching or inserting.

**1. refine-draft: Tenet 4 and the subject posit misstated (six ERRORs, six files; tenets L117, L121, L123, L125, L145, L172, L184).**
- `topics/personal-identity.md` (4045/4000, **46 over; NEEDS-HUMAN length block todo L1076: net-negative only**):
  - L193: replace "on MWI you would be interchangeable with your branching copies; the Map's commitment to definite outcomes and indexical facts is what supports `[[haecceity|haecceitistic]]` identity." with "on egalitarian MWI no branch-copy is privileged as you; the tenet's indexical objection draws on the `[[haecceity|haecceitistic]]` subject the Map posits rather than supporting it." (+1)
  - L53: "The `[[tenets#^no-many-worlds|No Many Worlds]]` tenet's emphasis on indexical identity—that *this* conscious being matters, not just the pattern it instantiates—commits the Map to a view where personal identity is real and significant," → "The Map posits that *this* conscious being matters, not just the pattern it instantiates—the subject its `[[tenets#^no-many-worlds|No Many Worlds]]` tenet draws on—so personal identity is real and significant," (−3)
  - Net −2.
- `topics/consciousness-and-the-metaphysics-of-individuation.md` (3189/4000, headroom 810):
  - L133: replace from "The Map's single-world commitment makes" to the end of the paragraph with "The Map's single-world commitment removes the branch copies, so there is one history in which to be you; that the question of what makes you *this* one has a determinate (if inaccessible) answer is the background posit of a determinate subject (`[[tenets/background-commitments]]`), which Tenet 4's indexical objection presupposes rather than supplies." (+15)
  - L131: replace "The Map cannot take this route. If consciousness is non-physical, its individuation must appeal to something non-physical" with "Bare irreducibility leaves a property dualist free to individuate subjects by their physical bearers; the substance-leaning reading, which enters downstream through agent causation (`[[where-the-substance-commitment-enters]]`), cannot take that route, and its individuation must appeal to something further" (+16)
  - L139: replace "applies here with full force. The simplest account of individuation—subjects are individuated by bodies—fails. A more complex account is needed" with "applies defensively, and symmetrically. The simplest account of individuation—subjects are individuated by bodies—is animalism's, which the Map declines at a framework boundary rather than refutes. If a more complex account is needed" (about 0)
  - Net about +31.
- `topics/modal-structure-of-phenomenal-properties.md` (2411/4000, headroom 1588):
  - L115: replace the No Many Worlds paragraph with "**No Many Worlds**: Tenet 4 does no work for modal arguments—determinate phenomenal facts are available branch-relatively, so the profile above survives under many-worlds. The link runs through the `[[vertiginous-question|vertiginous question]]` instead, a ground drawn from the Map's posited subject rather than from the haecceity of qualia." (about −40)
  - L113 and L111: rewrite both as coherence commentary. For L113, the zombie argument works under bare irreducibility, and modal separability is shared by epiphenomenalism. For L111, the modal profile says nothing about where or whether consciousness acts. (about −25)
  - Description L3: "supporting dualism through converging modal arguments" → "the modal shape of the Map's adopted dualism, not independent proof of it" (+6, frontmatter).
  - Net body about −65.
- `concepts/blindsight.md` (2913/3500, headroom 586):
  - L183: replace "Under `[[tenets#^no-many-worlds|No Many Worlds]]`, this selection is genuine rather than illusory: phenomenal presence or absence is a determinate fact about this world, not a perspectival artifact of branch location." with "`[[tenets#^no-many-worlds|No Many Worlds]]` adds only coherence here: phenomenal presence or absence is determinate within any branch, so an Everettian restates the dissociation as readily." (−5)
  - L177: "Blindsight demonstrates that … supporting Interactionist Dualism over reductive physicalism" → "Blindsight shows that visual processing can run without visual consciousness, a separability that workspace and higher-order theories predict as readily as Interactionist Dualism does; it is compatible with the Map's reading, not evidence against reductive physicalism." (+20)
  - L179: "The phenomenon also supports" → "The phenomenon is also compatible with". Name the cited capacities as access functions and keep the lawful-correlation reply standing (tenets L101). (+2)
  - Net about +17.
  - The brief must quote the 07-10 Stability Note and say why L177–L183 fall outside it.
- `topics/interaction-problem-across-traditions.md` (3834/4000, headroom 165):
  - L98: replace "The Many-Worlds interpretation avoids collapse entirely, eliminating the opening for `[[mental-causation-and-downward-causation|mental causation]]`—which is precisely why the Map `[[tenets#^no-many-worlds|rejects it]]`." with "The Many-Worlds interpretation avoids collapse entirely, so selection would fix no globally unique outcome; branch-relative agency survives there, and the Map `[[tenets#^no-many-worlds|rejects Many-Worlds]]` on the indexical objection, not to protect `[[mental-causation-and-downward-causation|mental causation]]`." (+13)
- `topics/russellian-monism-versus-bi-aspectual-dualism.md` (3412/4000, headroom 587):
  - L102: replace "The Map *requires* consciousness at collapse: selection among quantum outcomes is how actuality works on its account. Many-worlds eliminates selection by keeping all outcomes, thereby leaving no actualising role for consciousness to play." with "The Map gives consciousness a role in which outcome becomes actual in neural systems, with physical collapse supplying definiteness elsewhere (`[[prebiotic-collapse]]`). Many-worlds keeps all outcomes and so leaves that role no work, though an Everettian can still model branch-relative choice." (+7)
  - Wheeler tail: "the Map's selection ontology likewise excludes branching because a single outcome must be actualised" → "the Map's single-outcome posit likewise excludes branching" (−7).
  - L159 navigation label: "selection-ontology case" → "single-outcome posit" (−1).
  - Net −1.
- Brief note:
  - Name the claims: tenets L123 "logical interdependence, not mutual evidential support"; L172 determinate phenomenal facts are branch-relative; L145 the MWI rejection "must … rest on the indexical objection"; L125 physical baseline collapse.
  - Grep each file for `supports`, `precisely why`, `single actual world`, `determinate fact`, `requires`.
  - Do not touch the operator-referred aspect/subject lines (`russellian-monism-versus-bi-aspectual-dualism` L64/L118).
  - Check the Hugo copies.

**2. refine-draft: Tenet 2 given predictions and rulings it does not make, plus the residue of check 143's row 3 (three ERRORs and two WARNING clusters, five files; tenets L69, L71, L73, L75, L81, L125).**
- `concepts/agent-causation.md` (3496/3500, **headroom 3: net ≤ +3**):
  - L109: "an opacity *predicted* by minimal quantum interaction" → "an opacity *expected* under minimal quantum interaction" (0)
  - Optional, L160: "excluding quantum coherence in brain tissue would break the interface mechanism" → "…would break only the coherence-dependent candidates; post-decoherence selection needs undetermined neural outcomes, not coherence" (fund it by cutting L157 "each with current evidence pointing the other way" if needed)
- `topics/arguments-against-materialism.md` (3086/4000, headroom 913):
  - L105: "one that generates `[[testing-consciousness-collapse|concrete differential predictions]]` distinguishing consciousness-collapse from decoherence-only interpretations" → "a consistency claim rather than a novel prediction, though the `[[testing-consciousness-collapse|consciousness-collapse models]]` make differential predictions experiments now test" (+8)
  - L125: "the Map would need to identify a different physical channel for mental causation" → "these bear on the collapse-model and coherence-dependent candidates; the post-decoherence selection the Map endorses most strongly does not stand or fall with them" (+10)
  - Coordinate with open P3 todo L1697 (same file, L73–82/L115). Net about +18.
- `topics/comparing-quantum-consciousness-mechanisms.md` (4005/4000, **6 over: net ≤ −6**):
  - L178: "— ruling against proposals requiring macroscopic coherence or panpsychist commitments" → "— ranking below, not ruling out, proposals requiring macroscopic coherence" (0)
  - Fund it at L159 by deleting "— and derives `[[tenets#^minimal-quantum-interaction|Minimal Quantum Interaction]]` from the structure of the measurement problem rather than asserting it" (about −16; the tenets are chosen starting points, tenets L47).
  - Net about −16, bringing the file to about 3989.
  - Do not touch the Zeno placements (L82, L159 first clause, L161, L180). They wait on doctrinal item 6(c).
- `topics/born-rule-and-the-consciousness-interface.md` (5444/4000; human-blocked flagship: net ≤ 0):
  - L74: "The corridor-vs-outside-the-corridor distinction (`[[#corridor-taxonomy|taxonomy below]]`) is held as a live branch, and the empirical engagement" → "The corridor is the endorsed reading and outside-the-corridor readings are fallbacks (`[[#corridor-taxonomy|taxonomy below]]`); the empirical engagement" (about −4)
  - L191: "the Born rule describes how consciousness actualises one possibility among many" → "the Born rule describes how consciousness, in brains, selects one possibility" (0; tenets L125, own L110)
  - L120: "a unified experiencer actualising exactly one possibility among" → "a unified experiencer, for neural outcomes, selecting exactly one possibility among" (+2)
  - Net about −2.
- `apex/born-preserving-causal-efficacy.md` (5140/5000; **NEEDS-HUMAN length block todo L441: net-negative only**):
  - L123: delete "It is also where the intervention analysis above leads, which makes it the route the Map is likeliest to be pushed toward rather than the exotic option." (−27)
  - Reason: the intervention analysis leads to horn (a), the conditioned deviation that tenets L75/L81 place inside the corridor (own L89).
- Brief note: grep each file for `predict`, `generates`, `ruling`, `live branch`, `likeliest`, `actualis`, and check every hit against tenets L69/L75/L81.

**3. refine-draft: Tenets 1, 3 and 5 given content or roles that tenets.md denies (four ERRORs, four files; tenets L53, L55, L93, L101, L103, L145, L147).**
- `concepts/materialism.md` (3159/3500, headroom 340):
  - L150: "The `[[tenets#^dualism|Dualism]]` tenet holds that consciousness is fundamental, not derived from anything else." → "The `[[tenets#^dualism|Dualism]]` tenet holds that consciousness is not reducible to physical processes." (−1)
  - L152: "categorically different substances" → "categorically different relata" (0)
  - L154: "between two kinds of substance" → "between two irreducible kinds" (−1)
  - L176: "is accepted because materialism fails" … "Consciousness must be something beyond the physical." → "dualism is the Map's chosen response to materialism's failures as the Map judges them … The Map takes consciousness to be something beyond the physical—a commitment it owns rather than a result it reports" (+12)
  - Net about +10.
- `topics/contemplative-pathology-and-interface-malfunction.md` (2361/4000, headroom 1638):
  - L91: "The dualist tenet does not rest on the contemplative report alone; it rests on the wider convergent record discussed above" → "The dualist reading of these cases does not rest on the contemplative report alone; it draws on the wider record discussed above". Then append to the sentence: "—patterns the anaesthesia case grades as compatible with the tenet without establishing it; the tenet itself is motivated by the explanatory gap, not by these data" (+27).
  - Same line: "through states a materialist account would expect to diminish it" → "through states that disrupt ordinary function" (−4)
  - L93: "explains why contemplative practice can produce these effects at all" … "provides evidence that consciousness causally influences brain states" → the tenet "licenses reading these effects as consciousness restructuring its own coupling; the effects do not establish it", naming practice-induced plasticity as the same kind of evidence as skill learning (+8)
  - L89: "materialist alternatives struggle to match" → "…though, as the abolition symmetry above concedes, a production account reads the same cases with comparable ease" (+7)
  - Net about +38. Keep today's Lindahl repair (2a4334d191) intact.
- `concepts/contemplative-epistemology.md` (2684/3500, headroom 815):
  - L142: "this loop illustrates what bidirectional interaction predicts: conscious attention reshaping the neural substrate that supports it" → "this loop is what bidirectional interaction would lead one to expect—conscious attention reshaping the neural substrate that supports it—though physical learning theories expect the same plasticity (see `[[meditation-and-consciousness-modes]]`)" (+12)
  - L140: "Contemplative epistemology provides the epistemic foundation for the Map's dualism" → "Contemplative epistemology supplies evidence the Map's dualism draws on, not its foundation" (+2).
  - Same paragraph: "The epistemic gap supports the metaphysical gap." → "The Map reads those properties as irreducible to the physical, though moving from an epistemic gap to a metaphysical one is the step the `[[phenomenal-concepts-strategy|phenomenal-concept strategy]]` contests." (+19)
  - Net about +33.
- `concepts/bi-aspectual-ontology.md` (2947/3500, headroom 552):
  - L145: "**Occam's Razor Has Limits** justifies the ontological commitment." (whole paragraph) → "**Occam's Razor Has Limits** keeps the ontology's extra weight from counting against it, and no further. A bi-aspectual ontology is more complex than pure physicalism, but where knowledge is this incomplete simplicity decides neither for nor against either picture; the added complexity answers to the hard problem's resistance to structural resolution, not to a preference for complexity." (−14)
  - L75: replace "— unable to account for our ability to discuss and report on our own experience" with ", and our reports about experience would be reliable only in virtue of the parallel — a reply the Map judges to rest on a contested premise rather than one it can refute (`[[tenets#^bidirectional-interaction|Tenet 3]]`)" (+19)
  - Net about +5.
  - **Do not touch L105, L135 or L137.** That is the 13:55Z open-tension text, operator-referred.
- Brief note:
  - Name the claims: tenets L53 "What matters is irreducibility"; L55 "a commitment the Map owns, not a result it reports"; L81/L93 the tenets predict nothing; L145/L147 Tenet 5 binds both directions.
  - Grep each file for `tenet holds`, `tenet does not rest`, `predicts`, `justifies`, `foundation`, `substance`.

**4. positions-evolve: two register entries state Tenet 4's ground and self-stultification's reach more strongly than tenets.md allows (two WARNINGs; tenets L101, L121, L123).**
- `positions/individuation-and-subjecthood.md` (3938 words; positions hard 2500 / critical 4000. Registers breach by design, NEEDS-HUMAN todo L1262. Stay under 4000):
  - P-I1 L55: "Tenet 4 (`[[tenets#^no-many-worlds|No Many Worlds]]`) — the indexical objection supplies the ground" → "Tenet 4 (`[[tenets#^no-many-worlds|No Many Worlds]]`) — whose indexical objection presupposes this position rather than supplying its ground (P-I2)" (+5)
  - L54: "tenet-driven rather than empirically compelled" → "posit-driven rather than empirically compelled" (0)
  - Add the mandatory dated `Updated` note (about +30). This lands at about 3973.
  - Reason: P-I1 says Tenet 4 grounds it, while P-I2 (L66) says Tenet 4's argument depends on P-I1. That is the mutual grounding tenets L123 forbids, and the new `kants-paralogisms` page (L75/L81) cites P-I1 as a posit held on independent grounds. The fix works under every option of NEEDS-HUMAN todo L717.
- `positions/arguments-for-mental-causation.md` (3292 words; register over its section threshold by design):
  - P-MC2 L69: "the self-stultification argument establishes that *some* consciousness is report-grounded" → "the self-stultification argument establishes, against bare-correlation epiphenomenalism (P-MC1), that *some* consciousness is report-grounded" (+5), plus the dated `Updated` note (about +30).
  - Source: `concepts/epiphenomenalism` L102 scopes the same claim; tenets L101 and L103.
  - Do not touch P-MC2 L3, L44 or L65 ("where Tenet 3 asserts a universal one"). That is the operator's quantifier, todo L682.

**Runners-up (not ranked, not for minting from this report):**
- **Witness-carry register** (Summary 4): `witness-consciousness` L168/L184/L158/L188/L180 (net about −30, headroom 2), `phenomenology-of-choice` L137 (+4) and the `observer-witness` L3 description. Make "cause its own reports" conditional, without choosing the quantifier. The files share held loci with the BLOCKED P3 at L1834.
- **Self-stultification read as refutation** (tenets L101/L103): `ai-epiphenomenalism` L65–L69/L109/L63/L57/L124/L113 (about +16); `epiphenomenalism` L102/L116/L132/L144/L148 with a cut at L169 (about +11, headroom 40); `self-stultification` L149/L159/L143/L165 (about −1); `dualism` L154/L180; `materialism` L110/L178.
- **`explanatory-gap` L177/L81/L185/L193** (net +2, headroom 4; coordinate with P3 todo L1904): the hub's Relation section says "direct support", runs the inference Type-B rejects, glosses Tenet 1 as "fundamental, not derived" and holds Tenet 3 as actual. Also `zombie-master-argument` L76/L122/L126/L132.
- **Conceivability-cluster alignment inheritance** (tenets L172/L176): `conceivability-possibility-inference` L140/L138; `phenomenal-concepts-strategy` L191/L195/L183/L131 (fold into P3 todo L1904; headroom 51).
- **`stapp-quantum-mind` L120/L168/L142/L152** (net about +8 on a file 503 over, so it must be funded or deferred) and **`bi-aspectual-ontology` L37/L141/L109**.
- **Coherence dependence attributed to the Map**: `substrate-independence` L122/L172/L190, plus the §Process Philosophy deletion (about −126, which brings the file under its gate); `ai-epiphenomenalism` L57/L124; `objections-to-interactionism` L59/L169; `four-quadrant` L149; `mechanism-costs` L79; `evolution-of-consciousness` L179/L199; `visual-consciousness` L120; `dualism` L162/L168/L190; `russellian-monism` L141.
- **Tenet 5 as licence**: `four-quadrant` L153 and `mechanism-costs` L149/L151; `causal-consistency-constraint` L73 (±0, four checks unminted); `clinical-phenomenology` L135/L157/L149/L169 (about −79); `bergson` L137; `apex/authority-of-form` L122 (append to P3 todo L1865).
- **Carried, unminted**: `phenomenology-of-choice` L3/L56/L145/L165; `temporal-consciousness` L212/L251/L255; `consciousness-and-probability-interpretation` L93/L125/L105 (McGinn stance); `apex/judging-the-map-as-science` L86/L142; `parsimony-case` L136/L101–L111/L144; `self-opacity` L139/L159/L163/L165; `apex/contemplative-path` five loci plus L116; `history-of-the-interaction-problem` L142/L99/L118 together with the Sāṃkhya assimilation at `traditions` L130.
- Check 142's row 4 (§Warnings → Outside the window).

## Warnings

The sweeps grep-verified every locus at the stated line. The driver re-verified the loci named in the priority list. Line numbers are as of 2026-10-03 ~19:50 UTC.

### Families in this window

- **Tenet 3 held as actual, or epiphenomenalism/illusionism reported refuted** (tenets L93, L95, L101, L103). This is the largest family again.
  - `epiphenomenalism` L102/L116 "could never have entered the physical world" (carried)
  - `ai-epiphenomenalism` L67 "the argument is decisive against bare-correlation epiphenomenalism", L63 "does genuine causal work"
  - `interactionist-dualism` L195 "eliminativism about *that* is incoherent", L209
  - `meditation-and-consciousness-modes` L46 "Effort does real work here" (carried since check 138)
  - `phenomenology-of-choice` L94 "consciousness doing work"
  - `evolution-of-consciousness` L183/L79 "Consciousness evolved because it made a difference"
  - `self-stultification` L149/L159
  - `physical-completeness` L112 "but it is causally real"
  - `temporal-consciousness` L251
  - `unity-of-consciousness` L135
  - `agent-causation` L145/L147
  - `bi-aspectual-ontology` L37/L141
  - `explanatory-gap` L185
  - `self-opacity` L159
  - `mechanism-costs` L135
  - `apex/altered-states` L108/L122
  - the witness carry (Summary 4)
- **Compatibility upgraded to support, evidence, prediction or explanation** (evidential-status L112–121; access/phenomenal L315).
  - `apex/contemplative-path` L134/L136/L122/L190/L126
  - `blindsight` L143 cluster (L78/L125/L163/L195/L68)
  - `visual-consciousness` L108/L116
  - `degrees-of-consciousness` L96/L118
  - `experimental-consciousness-science` L3/L38/L74/L100/L112
  - `phenomenology-of-choice` L3/L56/L90/L102
  - `erasure-void` L115–117 ("the dualist picture predicts the strangeness")
  - `perceptual-reality-monitoring-void` L110/L112
  - `phenomenal-authority` L209 ("evidential foundation")
  - `quantum-state-inheritance-in-ai` L98 ("inadvertent corroboration")
  - `consciousness-disruption` L142/L162
  - `trilemma` L54/L76/L91/L113/L99
  - `substrate-independence` L150/L128
  - `dualism` L176 ("predicts exactly these findings")
  - `arguments-against-materialism` L67/L137
  - `interactionist-dualism` L135/L137/L193
  - `objections-to-interactionism` L39/L179/L196 (pairing over-claimed against P-SC2)
  - `apex/mereology-of-mind` L85
  - `zombie-master` L76 (the Type-B cost stated as a defeat)
- **Tenet 2: coherence dependence attributed to the Map, classical menu, unscoped indistinguishability, mechanism stated as fact** (tenets L69, L71, L73, L75, L77, L91).
  - **Coherence:**
    - `substrate-independence` L122/L172/L190
    - `ai-epiphenomenalism` L57/L124
    - `objections-to-interactionism` L169
    - `agent-causation` L160
    - `four-quadrant` L149 and `mechanism-costs` L79 (both with 0 hits for "post-decoherence")
    - `evolution-of-consciousness` L179/L199
    - `visual-consciousness` L120
    - `dualism` L162/L168/L190
    - `russellian-monism` L141
    - `ensemble-level-epiphenomenalism` L37
    - `apex/born-preserving-causal-efficacy` L71
    - `wheelers` L142
    - `quantum-state-inheritance-in-ai` L78/L96
  - **Zeno presented as the Map's mechanism:** `meditation-and-consciousness-modes` L44 and `the-observer-witness-in-meditation` L56 (tenets L71). The `apex/contemplative-path` L184 and `comparing` L86/L114/L141/L161 "satisfies all five tenets" findings overlap doctrinal item 6(c).
  - **Classical menu:**
    - `trilemma` L127
    - `consciousness-as-activity` L126
    - `objections-to-interactionism` L119
    - `agent-causation` L127
    - `witness-consciousness` L96
  - **Unscoped indistinguishability or sensitivity limits:**
    - `stapp-quantum-mind` L66
    - `apex/judging-the-map-as-science` L86/L142 ("untested by any feasible precision")
    - `ethics-of-possible-ai-consciousness` L152 ("in principle detectable")
    - `organizational-invariance` L84 ("the detectable one")
    - `zombie-master` L122/L126 ("different quantum outcome distributions")
  - **Corridor/fork residue:**
    - `apex/born-preserving-causal-efficacy` L63/L109/L99/L125 (Maier external-RNG scoping)
    - `ensemble-level-epiphenomenalism` L61 (Maier)
- **Family I: felt definiteness used against MWI, or "nothing to select" with no nod to branch-relative agency** (tenets L117, L121, L172, L184 posit 3).
  - `witness-consciousness` L158/L188
  - `phenomenology-of-choice` L165 (carried since check 138)
  - `temporal-consciousness` L212/L255
  - `meditation-and-consciousness-modes` L185
  - `degrees-of-consciousness` L120
  - `visual-consciousness` L124
  - `evolution-of-consciousness` L187 ("Real collapse is essential to the evolutionary story")
  - `bergson-and-duration` L135
  - `mine-ness` L144
  - `history-of-the-interaction-problem` L142
  - `self-opacity` L163
  - `sorkin` L74
  - `ai-epiphenomenalism` L113
  - `russellian-monism` L43/L131
  - `neural-correlates-of-consciousness` L164
  - `consciousness-and-scientific-explanation` L124 (low)
  - `apex/mereology-of-mind` L91/L101 (Tenet 4 credited with breaking the tie against panpsychism)
- **Tenet 1 glossed as substance dualism, as fundamentality, or as settling which systems are conscious** (tenets L53, L57, L170).
  - `degrees-of-consciousness` L38
  - `evolution-of-consciousness` L109/L125/L3
  - `bi-aspectual-ontology` L109 (L61 "both fundamental" is still the source NOTE)
  - `parsimony-case` L136 ("co-fundamental", carried)
  - `explanatory-gap` L177 ("fundamental, not derived")
  - `type-identity-theory` L69 ("the tenet is precisely the *denial of the type-type identity*", against own L55)
  - `integration-as-activity` L117
  - `russellian-monism-versus-bi-aspectual-dualism` L140/L46
  - `ethics-of-possible-ai-consciousness` L136 ("categorically excluding current AI", against own L90 and P-AC1)
  - `quantum-state-inheritance-in-ai` L36/L96
  - `substrate-independence` L114/L126 (bare-phenomenality row scoping)
  - `dualism` L106/L114 (strong Revelation used as a premise, against `revelation-thesis` L76/L80)
- **Tenet 5 as verdict, licence or asymmetric parsimony** (tenets L141, L145, L147).
  - `four-quadrant` L153 ("authorises selective inflation")
  - `mechanism-costs` L149/L151
  - `causal-consistency-constraint` L73
  - `clinical-phenomenology` L135/L157/L149/L169 (carried)
  - `bergson` L137
  - `explanatory-gap` L193
  - `zombie-master` L132 ("The master argument also supports Tenet 5")
  - `degrees-of-consciousness` L122
  - `self-and-self-consciousness` L194
  - `self-opacity` L165
  - `stapp-quantum-mind` L168
  - `interactionist-dualism` L192
  - `phenomenal-concepts-strategy` L195
  - `materialism` L182
  - `experimental-consciousness-science` L106 tail
  - `apex/authority-of-form` L122
  - `comparing` L86/L114 ("complexity beyond simplicity")
  - `constitutive-vs-referring-observation` L77 (low)
  - `consciousness-and-the-metaphysics-of-individuation` L139
- **Co-optation, mostly the phenomenological/process line.** No stance line at:
  - `apex/contemplative-path` L150 (Whitehead)
  - `phenomenal-concepts-strategy` L165–169 (Whitehead; 0 hits for "bifurcat")
  - `haecceity` L131 and `personal-identity` L107/L139 (Whitehead)
  - `substrate-independence` L154–156 (Whitehead)
  - `agent-causation` L137 (Whitehead)
  - `evolution-of-consciousness` L155 (Whitehead)
  - `integration-as-activity` L38/L96 (Whitehead, carried)
  - `temporal-consciousness` L124 (Whitehead) and L130 (Husserl)
  - `phenomenal-authority` L84/L96 (Husserl; 0 hits for "Crisis")
  - `apex/dualism-cartography` L71/L117: Goff placed in Q4, against its own source taxonomy's L83/L114. The same placement is in `mechanism-costs` L109.
  - `consciousness-and-probability-interpretation` L105 (McGinn)
  - **Assimilation of a rival:** `history-of-the-interaction-problem` L118 and `interaction-problem-across-traditions` L130 treat Sāṃkhya's reflection model as an anticipation of selection, but its *puruṣa* is a non-doer (the Map's own `samkhya-three-way-distinction` L67 says so).
- **Necessity vocabulary in method/history claims** (evidential-status L100).
  - `history-of-the-interaction-problem` L134 ("forced impossible choices")
  - `eighteenth-century-influx-debate` L35 ("the answer", carried)
  - `physical-completeness` L34/L94 ("a feature of what physical theory *is*")
  - `objections-to-interactionism` L59 ("The pairing is built into the mechanism")
  - `apex/judging-the-map-as-science` L104 (NOTE)

### Per-file index (window; sweep IDs A1–C10; E = ERROR, W = WARNING lines, N = NOTE lines)

New this window (A1–A2):
- `concepts/primitive-identities-and-strong-necessities` N L118, L41/L114
- `concepts/ignorance-hypothesis` N L84, L70
- `concepts/type-a-type-b-and-type-c-physicalism` N L119/L121/L123, L103; L123 "main defeat" COVERED by todo L1817
- `topics/anton-syndrome-and-the-sincere-report-of-seeing` N L43 (rides P2s todo L40/L51)
- `topics/kants-paralogisms-and-the-maps-subject` N L34, L36, L107, L109

Calibration passes today, scope (b) (B1–B3, C10):
- `concepts/witness-consciousness` W L168, L184, L158/L188, L176; N L180, L78/L86, L92, L96, L136, L152, L192
- `concepts/meditation-and-consciousness-modes` W L46, L44, L185; N L191, L177, L167; operator L38/L181/L204 (+L100, L163 to append)
- `topics/the-observer-witness-in-meditation` W L3, L56, L103/L105; N L173, L177, L203; COVERED L44/L50/L52/L60–63/L83 (todo L1845); operator L36…L193 (todo L1834) + L189
- `concepts/phenomenology-of-choice-and-volition` W L3, L56, L90, L94, L102, L137, L143/L145, L165; N L119, L123, L147/L167, L163; COVERED L151 (todo L1855)
- `topics/temporal-consciousness-structure-and-agency` W L251, L212/L255, L124/L130; N L249, L253, L206, L257, L70, L160
- `concepts/contemplative-epistemology` E L142; W L140; N L144, L122, L46
- `apex/contemplative-path` W L116, L126, L136, L134/L136/L122, L190, L150, L184; N L64, L86, L94/L192, L110, L118, L130, L162, L198; operator L194
- `topics/contemplative-pathology-and-interface-malfunction` E L91; W L93, L89, L69, L83, L57, L35; N L75, L67, L95 (todo L292)
- `topics/bergson-and-duration` W L135, L137; N L131, L83, L119
- `apex/authority-of-form` W L122; N L130, L56/L142/L114/L66, L128, L90, L126; COVERED apex_thesis/L50/L74/L104/L118 (todo L1865)
- `concepts/carrolls-regress` N L71, L75
- `concepts/stapp-quantum-mind` W L120, L168, L142, L152, L104/L106, L66; N L3, L45, L94, L128; operator L100
- `concepts/bi-aspectual-ontology` E L145; W L75, L37/L141/L139, L109; N L61, L81, L123, L125, L43, L55, L131; operator L105
- `concepts/where-the-substance-commitment-enters` N L75, L28; operator L34
- `concepts/type-identity-theory` W L69; N L69/L75 link targets, L77
- `positions/arguments-for-mental-causation` W L69; N L52/L56, L80; operator L3/L44/L65/L72
- `positions/ai-consciousness-scope` N L94, L56
- `topics/consciousness-as-activity` W L126; N L122, L116/L141

Quantum wing (C1–C2):
- `concepts/post-decoherence-selection` N L66, L108, L106
- `topics/comparing-quantum-consciousness-mechanisms` E L178; W L86/L114/L141/L161, L100, L169, L86/L114 (Tenet 5); N L159, L72, L88; doctrinal L82/L159/L161/L180/L110
- `topics/consciousness-in-smeared-quantum-states` N L100, L124, L56; doctrinal L96
- `topics/born-rule-and-the-consciousness-interface` W L74, L191/L120; N L169, L207, L165, L221, L139
- `topics/wheelers-participatory-universe-and-it-from-bit` W L142; N L156, L148, L52/L122/L158
- `topics/consciousness-and-probability-interpretation` W L93, L125, L105; N L146, L127, L121
- `apex/born-preserving-causal-efficacy` W L123 (tail), L63/L59, L109/L99, L125/L167, L71; N L191, L200, L71/L193; operator L67
- `concepts/causal-consistency-constraint` W L73; N L73
- `concepts/ensemble-level-epiphenomenalism` W L61, L37; N L71, L35, L79; operator L43
- `concepts/sorkin-higher-order-interference` W L74; N L76
- `concepts/consciousness-and-scientific-explanation` W (low) L124; COVERED L52/L60 (todo L1732)
- `topics/quantum-state-inheritance-in-ai` W L98, L78, L96, L36; N L58/L102/L110 link targets, L62, L60/L102; operator L50/L114
- `concepts/constitutive-vs-referring-observation` W (low) L77; N L55, L81

Mental causation (C3):
- `concepts/epiphenomenalism` W L102, L116, L132, L144, L148; N L96, L140, L154, L185, L201, L110, L214/L215; operator L116/L130–132/L203
- `concepts/ai-epiphenomenalism` W L65/L67, L69/L109, L63, L57, L124, L113; N L131, L71; operator L41/L49/L79/L109
- `concepts/interactionist-dualism` W L195, L193, L192, L209, L137, L135, L91, L177; N L99, L143, L153, L163, L165, L240, L205, L159
- `concepts/objections-to-interactionism` W L39, L59, L169, L179, L196, L119; N L165, L127, L175, L149, L188, L194, L209
- `concepts/agent-causation` E L109; W L148, L145, L147/L151, L127, L160, L137; N L170, L111; operator L178
- `concepts/trumping-preemption` W L89; N L85, L90
- `concepts/the-relocation-objection`: CLEAN
- `concepts/physical-completeness` W L78, L112, L34/L94; N L126, L122, L52, L116

Physicalism and conceivability (A1, C4):
- `concepts/kripke-a-posteriori-necessity-argument` N L67; COVERED L55/L57 (todo L1884)
- `concepts/zombie-master-argument` W L76, L122/L126, L132; N L52, L60, L109, L126; COVERED L102 (todo L1810), L112 (todo L1766)
- `concepts/explanatory-gap` W L177, L81, L185, L193; N L105, L135, L46, L189; COVERED L121/L141 (todo L1904)
- `concepts/phenomenal-concepts-strategy` W L131, L143, L117, L149, L165–169, L183, L191, L195; N L189; COVERED L39/L85/L139 (todo L1904)
- `concepts/materialism` E L150 (+L152/L154); W L98/L176, L110/L178, L79, L182, L116; N L188, L186, L180, L3; booked L184 (todo L116)
- `topics/arguments-against-materialism` E L105; W L125, L137, L139, L57/L123, L67, L77; COVERED L73–82/L115 (todo L1697); booked L97 (todo L116)
- `concepts/dualism` W L106/L114, L154/L180, L176, L162/L168/L190, L196/L140/L146, L184; N L130, L186, L200; booked L172 (todo L116)
- `concepts/conceivability-possibility-inference` W L140, L138, L144/L146; N L108/L130, L29
- `concepts/inference-to-the-best-explanation-against-dualism`: CLEAN (tenet lens); COVERED L32/L64/L74/L80 (todos L1709/L1552)
- `concepts/revelation-thesis` N L76/L80, L54
- `concepts/russellian-monism` W L43/L131, L101/L97/L91, L141/L129; N L121, L109, L47; operator L65/L99

Self, subject and Tenet 4 (A2, C5):
- `topics/consciousness-and-the-metaphysics-of-individuation` E L133; W L131 (+L47/L59), L139; N L137, L95; COVERED L83/L166 (todo L1534)
- `positions/individuation-and-subjecthood` W L55/L54; N L38
- `positions/subject-census` N L71 ("four" vs "five" booked gaps), L59, L71 (navigation label)
- `concepts/self-and-self-consciousness` W L194, L190/L134; N L192, L86, L68, L140, L174
- `concepts/mine-ness` W L144; N L60/L82, L108
- `concepts/haecceity` W L193, L143/L177, L131, L99; N L153, L69/L91, L201, L83, L191
- `concepts/substrate-independence` W L122/L172/L190, L114/L126, L162, L150, L154–156, L128; N L46, L201/L202/L212, L102/L104, L96; operator L126
- `topics/personal-identity` E L193; W L53, L161, L131/L133, L107/L139; N L85
- `topics/trilemma-of-selection` W L127, L76, L54, L91, L113, L99; N L131, L147, L97, L70, L109
- `topics/self-stultification-as-master-argument` W L149, L159, L143, L165; N L127, L65, L167, L49, L81, L161, L182, L125; operator L145

Clinical and report wing (C6):
- `concepts/cotard-delusion` W L36/L72; N L66, L74, L68
- `concepts/depersonalisation` N L89
- `concepts/thought-insertion` N L108; COVERED L104 (todo L1645), L36/L42/L46 (todo L1636)
- `topics/anosognosia-and-the-reversible-self-monitoring-channel`: CLEAN
- `concepts/blindsight` E L183; W L177, L179, L143 cluster (L78/L125/L163/L195/L68); N L181, L135–143, L211, L151
- `topics/clinical-phenomenology-and-altered-experience` W L135/L157/L149/L169; N L125, L51, L95, L103, L187
- `topics/consciousness-disruption-and-the-mind-brain-interface` W L142, L162; N L110, L148, L152, L51, L186, L208 (Thompson orphan reference)
- `topics/death-and-consciousness` W L177/L175/L111, L183, L87; N L185, L3/L51/L103/L121, L119, L107, L195

Consciousness science (C7):
- `concepts/higher-order-theories` N L174, L162
- `concepts/degrees-of-consciousness` W L38, L96, L118, L120, L122; N L68, L54, L116
- `concepts/neural-correlates-of-consciousness` W L164; N L156
- `concepts/visual-consciousness` W L37, L108, L116, L120, L124; N L128, L39, L71
- `concepts/unity-of-consciousness` W L135, L145; N L141, L143, L113, L149
- `concepts/evolution-of-consciousness` W L183/L79/L75, L103, L97, L101, L187, L179/L195/L199/L207/L209, L109/L125/L3, L155; N L41, L147, L165, L127/L135, L121; doctrinal L197
- `topics/experimental-consciousness-science-2025-2026` W L3/L38, L74/L72, L100, L106 (tail), L112; N L88, L110, L94, L64
- `concepts/organizational-invariance` W L84; N L102, L88
- `concepts/integration-as-activity` W L38, L117; N L56/L117, L64, L119, L134, L48

History and taxonomy (C8):
- `topics/eighteenth-century-influx-debate` W L35; N L97, L95, L51, L89, L73, L33, L99
- `topics/history-of-the-interaction-problem` W L142, L99, L128/L136, L118, L134; N L138, L162, L140, L95, L114
- `topics/interaction-problem-across-traditions` E L98; W L130/L122; N L132, L136, L100, L98 (Orch OR), L134, L78
- `concepts/occasionalism`: CLEAN (10-02 N L58 repaired, 1618dd64dc)
- `topics/leibnizs-mill-argument` N L135, L139, L157, L69/L31
- `topics/four-quadrant-dualism-taxonomy` W L149, L153; N L83, L53/L151
- `topics/mechanism-costs-dualism-thickness-quadrants` W L135, L149/L151, L79; N L109, L75
- `topics/the-steelman-for-process-monism` N L85 (10-02 W L85/L33 repaired, e32fcbb10e)

Apex and methodology (C9):
- `apex/altered-states-as-interface-evidence` W L108, L122, L96; N L157/L169/L179, L96, L70; operator L110/L112/L141
- `apex/dualism-cartography` W L71/L117 (Goff); N L115, L117, L133, L135
- `apex/judging-the-map-as-science` W L86/L142; N L104, L96, L146, L64/L120
- `apex/mereology-of-mind` W L91/L101; N L89, L85, L99, L103
- `concepts/philosophy-of-science-under-dualism` N L135, L128, L36/L48, L46, L120; COVERED L84 (todo L1754)
- `topics/parsimony-case-for-interactionist-dualism` W L136, L101/L109/L111, L144; N L85, L59, L128, L153
- `apex/apex-articles` (index; window hunk only): clean

Other topics and voids (C10):
- `topics/ethics-of-possible-ai-consciousness` W L56, L136, L152; N L92, L158, L108; operator L66/L92/L106–L114/L138/L152/L158
- `topics/phenomenal-authority-and-first-person-evidence` W L209, L84/L96; N L3, L185, L211
- `topics/modal-structure-of-phenomenal-properties` E L115; W L3, L113, L111; N L95, L117, L87; COVERED L83 (todo L1673)
- `topics/russellian-monism-versus-bi-aspectual-dualism` E L102 (+L159); W L140, L46; N L144, L114; operator L64/L118
- `voids/erasure-void` W L115–117; N L38
- `voids/perceptual-reality-monitoring-void` W L110, L112; N L88/L102/L110/L112 ("constitutes")
- `voids/self-opacity` W L139, L159, L163, L165; N L161, L153, L71

### Outside the window

- **Check 142's row 4, still unminted (third check running).** The files have no commit since 09-28/09-29, so the loci are live by construction:
  - `voids/mirth-void` L94
  - `voids/mattering-void` L114
  - `topics/phenomenology-of-intellectual-life` L184/L186/L214/L218
  - `voids/causal-interface` L110/L112/L158
  - `voids/infant-consciousness` L105/L107
  - `topics/incubation-effect-and-unconscious-processing` L144/L146/L148
  - `topics/correlationism-and-the-ancestrality-argument` L100
- **The fabricated "tenet predicts" tail, re-probed and still live** (no commits in these files since check 143):
  - `concession-convergence` L149/L153
  - `concession-convergence-philosophy-of-mathematics` L114/L118
  - `volitional-control` L154
  - `biological-computationalisms-inadvertent-case-for-dualism` L90
  - `phenomenology-of-linguistic-failure` L113
  - `invertebrate-consciousness-as-interface-test` L135
  - `dualist-perception` L162
  - `consciousness-and-language-interface` L250
  - `self-reference-paradox` L146
  - `observation-and-measurement-void` L152
  - `decision-void` L107/L127
  - `mood-void` L114/L126
  - `animal-consciousness` L116
  - `apex/minds-without-words` L157
  - New to the list this check:
    - `concepts/bidirectional-interaction` L107: "the empirical pattern this tenet most directly predicts", on Tenet 3's own concept page, with placebo as the exhibit (access-level, evidential-status L315)
    - `voids/causal-interface` L158: "Minimal Quantum Interaction predicts this void", also in check 142 row 4
    - `concepts/functionalism` L164
  - Grep key: `(tenets?\]\]|tenet|Dualism\]\]|Interaction\]\]|Limits\]\])[^.]{0,60}\bpredicts?\b`, excluding "does not / would / equally".
  - The hedged hits still pass: `perception` L96, `architectural-adequacy-at-the-built-edge` L116, `apex/phenomenal-variation-within-a-species` L161, `what-voids-reveal` L116/L150.
- **The "actually sufficient" tail is closed.** All six loci now attribute the gloss to the fallback family: `born-rule` L167, `ensemble` L59, `causal-consistency` L95, `consciousness-and-probability-interpretation` L97, `apex/born-preserving-causal-efficacy` L123 (first sentence) and `four-quadrant`/`mechanism-costs` (false positives).

## Notes

About 320 NOTE findings, indexed per file above. Most are over-claims corrected in the same paragraph, Further Reading labels stating more than their target, link labels pointing at the wrong target ("Tenet 1" linking `[[dualism]]` in `type-identity-theory` L69, and the `quantum-state-inheritance-in-ai` tenet links that point at `interactionist-dualism`), or menu-shaped wording without the improper-mixture qualifier. The cross-file ones:
- **`subject-census` L71** says "four" booked gaps against its own L59 "Five". First flagged 09-25.
- **"Einselected menu" / "post-decoherence branch-outcomes"** without the improper-mixture qualifier (`subject-census` L59, `ai-consciousness-scope` L56, `stapp-quantum-mind` L128): corpus-standard, NOTE.
- **Production vocabulary in voids:** "the consciousness it constitutes" appears in `perceptual-reality-monitoring-void` L88/L102/L112 and also `recognition-void` L47, `capgras-delusion…` L93 and `mattering-void` L3 (a catalogue idiom).
- **`anton-syndrome` and its open P2s:** P2 todo L51 tells the page to inherit `blindsight`'s calibration. Blindsight's tenet section carries ERROR #4, so the L51 brief should say not to import blindsight L177/L179/L183. The L40/L51 refines should also not pad hedges: Anton L43/L75 already state the underdetermination. A hedge-density counter that reads otherwise is a lexical false-high.
- **The "modulates collapse" vocabulary** at `wheelers` L52/L122/L142/L158 matches tenets L125. Today's `post-decoherence-selection` L116 retires the verb ("rather than modulating collapse rates or locations"), and todo L1806 calls it retired. This is a watch item for a terminology sweep, not a tenet defect.
- **The NCC P2s** check 143 cited (old L1550/L1602) and the consciousness-disruption P2 (old L1729) are completed (✓ 10-02).

## Files passing all checks (5)

- `concepts/the-relocation-objection.md`
- `concepts/occasionalism.md` (10-02 NOTE repaired)
- `topics/anosognosia-and-the-reversible-self-monitoring-channel.md` (L102 cites `^tenet-3-standing`; Tenet 5 applied in both directions)
- `concepts/inference-to-the-best-explanation-against-dualism.md` (tenet lens; the model of symmetric Tenet 5 handling)
- `apex/apex-articles.md` (window hunk only)

NOTE-only (19):
- `primitive-identities-and-strong-necessities`, `ignorance-hypothesis`, `type-a-type-b-and-type-c-physicalism`, `anton-syndrome-and-the-sincere-report-of-seeing`, `kants-paralogisms-and-the-maps-subject` (all five new)
- `kripke-a-posteriori-necessity-argument`, `subject-census`, `carrolls-regress`, `where-the-substance-commitment-enters`, `ai-consciousness-scope`, `post-decoherence-selection`, `consciousness-in-smeared-quantum-states`, `depersonalisation`, `thought-insertion`, `higher-order-theories`, `leibnizs-mill-argument`, `the-steelman-for-process-monism`, `revelation-thesis`, `philosophy-of-science-under-dualism`

## Method

1. Read `tenets.md` L47–188: definitions, rationales, qualifiers, Rules-out clauses, the matrix and the background posits. There has been no commit since e3e689517d.
2. Listed every file in `topics/ concepts/ voids/ apex/ positions/` with a commit since 2026-10-02T01:00Z: 104 files, all live.
3. Fifteen parallel read-only sub-sweeps read the 103 content files in full:
   - A1–A2: the five new articles, with their Type-B and subject neighbours.
   - B1–B3: today's calibration pages.
   - C1–C10: the rest.
   - Each worked from a common written brief: the lens families keyed to tenets loci, the evidential-status ladder, the co-optation roster, the severity rules, and the operator-referred items.
   - Each re-probed its files' check-143 loci (and older loci where relevant) by content and marked each one REPAIRED, STILL LIVE or COVERED.
   - The driver waited in the foreground for all fifteen, then read every output before writing.
4. Carried ERRORs were re-probed by exact string. Each zero was confirmed as a repair from the repair commit's diff (bb10bcc4fd, 3d17421391, 26907f3404, 4648207ba6, c8dda17e31), not inferred from absence.
5. Every ERROR in this report was re-verified by exact substring at the stated line, as was every locus quoted in the priority list. Where the driver's grade differs from a sweep's or from check 143's, Summary 7 gives the reason.
6. Driver corpus probes outside the window covered three things:
   - the check-142 row-4 files (no commit since 09-28/09-29)
   - the "actually sufficient" key (closed)
   - the "tenet predicts" key (still live; three new loci)
7. Cross-checked the Active section of `workflow/todo.md`. Covered loci (P3s L1534, L1645, L1636, L1673, L1697, L1709, L1732, L1754, L1766, L1810, L1817, L1845, L1855, L1865, L1884, L1904; P2s L40, L51) are marked COVERED and not re-proposed. Length blocks (L441, L1076, L1262) are flagged in the rows they touch.
8. No content file and no `todo.md` entry was modified. The skill's contract is reports-only, so the four priority rows are ready-to-mint briefs for the driver.

## Scope confirmation

All 103 window content files were read in full; none was skipped, sampled or read in targeted mode. The index `apex/apex-articles.md` was checked on its single window hunk only. Files outside the window were probed by exact string only (check-142 row 4 and the two propagation keys), and are reported as carried or as out-of-window grep hits, never as fresh reads.
