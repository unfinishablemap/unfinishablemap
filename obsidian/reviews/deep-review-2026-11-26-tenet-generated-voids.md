---
title: "Deep Review - Tenet-Generated Voids"
created: 2026-11-26
modified: 2026-11-26
human_modified: null
ai_modified: 2026-11-26T12:46:44+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-11-26
last_curated: null
---

**Date**: 2026-11-26
**Article**: [[tenet-generated-voids|Tenet-Generated Voids]]
**Previous review**: [[deep-review-2026-06-25-tenet-generated-voids|2026-06-25]] (deep). Also read: [[pessimistic-2026-09-04-tenet-generated-voids|2026-09-04]] (pessimistic) and the 2026-05-26 deep review.

## Context

This is the tenth deep review. The driver picked the page because void pages built from early research notes keep turning up defects. Its last deep review (06-25) declared it "fully converged" after checking metadata only. Since then the body has changed five times: 9fc2e5fb22 (09-04 stranded-dependent refine), e3e689517d (09-27 Maier/P-Q3), 7b30518bd8 (11-08 P-Q2 "biasing probabilities" sweep), 742d4fded9 and 0cc054b392 (11-18 binding-void and tenet-wording sweeps). All five were read in git before judging, and none was reverted. Each one's intent is kept, and three are carried further (see below).

**Seed note**: one, `research/voids-tenet-generated-voids-2026-01-25.md`. The creation changelog (2026-01-26 00:45) names only that note. No second seeding note exists: the 10 other `research/` files that mention this slug all postdate the page and cite it.

**Stability notes from prior reviews**: they shield the five-void mapping, the MWI framing ("do not re-flag as if MWI cannot accommodate any indexicality"), the citation metadata and the cross-tenet voids. None of the critical issues below re-flags a shielded item. Issue 6 keeps the 04-28 concession of branch-relative indexicality and changes only the *stronger claim* the paragraph attributes to the Map, which `tenets.md` has reworded since. Per the stability-note scope rule, an empirical or attributive claim attached to a framework commitment stays reviewable.

## Pessimistic Analysis Summary

The six personas engaged. The findings that landed:

- **Churchland**: the background-commitments concession (09-04) had dropped its qualifier. Only Tenet 1's *substance-leaning sub-reading* shares the root posit (Issue 4).
- **Dennett**: "required by our ability to discuss consciousness at all" says more than the tenet says (Issue 3).
- **Tegmark**: Tegmark (2000) aimed his calculation at Penrose–Hameroff, and Stapp says it was not aimed at him. The article grouped Stapp with Orch OR as "coherence-dependent" (Issue 2).
- **Deutsch**: the plurality-void sentence claimed a support the plurality void's own page withholds (Issue 1).
- **Popper's ghost**: the Detection Void said "current or foreseeable instruments" where the corridor is silent by construction, and it stated the corridor's grain at the pre-10-14 P-Q2 resolution (Issue 5).
- **Nagarjuna**: the presupposition concession already holds. Nothing new from this persona.

### Critical Issues Found (11)

1. **The plurality void used as support for Tenet 4, which contradicts the page's own L89, the plurality-void page and P-V3.** The old L147 read: "Consciousness's constitutive singularity—its inability to be plural—reinforces this commitment: what cannot branch cannot split across worlds." But `voids/plurality-void` L103 says the void "does not refute that answer, because branching so described yields multiple singularities rather than a plural subject". P-V3 adds that "as a catalogue entry a void adds no weight to any tenet". `reviews/tenet-check-2026-09-28` L170 flagged this exact string ("against its own L89") and nothing was ever minted for it. *Fixed*: the sentence now says the plurality void adds nothing to the tenet, gives the multiple-singularities reason, and links P-V3. Seed: none. The sentence came from the 2026-02-24 deep review ("No connection to plurality void").
2. **Stapp's Zeno approach misclassified as coherence-dependent.** The old text read: "the coherence-dependent proposals (Orch OR, Stapp's quantum Zeno approach) are demoted". Stapp (2000, arXiv:quant-ph/0010029, checked in the PDF text) says the opposite: "the Quantum Zeno Effect described above is not destroyed by the fact that S(t)b is a mixture: that makes no difference at all". He also says "Tegmark … did not direct his remarks about decoherence at my theory." The Map's own `quantum-consciousness` L122 and `comparing-quantum-consciousness-mechanisms` L82/L161 record Stapp's dissent ("Neither claims to need sustained coherence"). *Fixed*: Orch OR is named as the proposal that needs coherence, and Stapp is demoted per P-Q4 "though Stapp (2000) holds that his effect survives decoherence, so the timing objection there is contested". Stapp 2000 and Tegmark 2000 were added to the References. Introduced by 9fc2e5fb22, which inherited the label from `tenets.md` L71.
3. **Tenet 3 stated past its wording** (the 0cc054b392 sweep class). The old text read: "is required by our ability to discuss consciousness at all". `tenets.md` L93 and L101 hold the tenet "as *a metaphysical commitment supported by self-stultification and indirect evidence*" and call the self-stultification point "the deepest difficulty for epiphenomenalism rather than its refutation". *Fixed*: the sentence now uses that wording, links `^tenet-3-epiphenomenalism` and says "something the Map holds to be causally real". Seed: none, present since creation.
4. **A dropped qualifier on the background-commitments concession.** `background-commitments` L36 and `tenets.md` L184 name "Tenet 1 (the substance-leaning sub-reading)". The article said "Tenets 1, 3 and 4" and called the three voids "one root's shadow cast three times". Bare Tenet 1 is neutral between substance and property dualism, and the Nature Void comes from bare irreducibility. *Fixed* in two places (L47 and Relation to Site Perspective): the qualifier is back, "one root's shadow" is dropped, and the sentence now reads "not three independent findings". Introduced by 9fc2e5fb22.
5. **The Detection Void grain was stale against P-Q2 (2026-10-14), and silence by construction was misstated as an instrument limit.** The old text read: "under any *unconditioned aggregate* test current or foreseeable instruments could run, though a deviation *conditioned* … remains live". `tenets.md` L75 says "*by construction, not by any sensitivity limit*". P-Q2 now names the grain: "outcome frequencies stay Born-exact in every publicly conditionable context", and a deviation conditioned on a public label is "the minimum-outside-the-corridor fallback … not a corridor prediction". *Fixed*: the new text gives the public-context grain "by construction rather than through any limit of instruments" with a P-Q2 link, then keeps the P-Q3 sentence in `tenets.md` L75's wording ("would test the corridor itself"). The matching phrases in "The Nature of These Limits" and the hiddenness paragraph were aligned the same way. Introduced by 9fc2e5fb22, which copied `tenets.md` L107.
6. **Tenet 4 rationale paraphrase was stale.** The old text said the Map's rejection rests on MWI's "needed cross-branch personal-identity relation (for Born-rule recovery via decision theory)". The current `tenets.md` L115 primary rationale reads differently: MWI's resources ("branch-relative identity, self-locating credence, decision-theoretic Born rules") "presuppose the very centred subject the question asks after". It is also scoped "decisive against branch-egalitarian readings" but not against "first-personally centred variants such as List's (2023)". The "needed" claim is also contestable as a description of Wallace's programme, since Saunders & Wallace's diverging view denies cross-branch identity. That was not checked at source this pass; `concepts/many-worlds` L73–82 still asserts it. *Fixed*: the text now follows `tenets.md` wording and scope. The 04-28 concession that branch-relative indexicality secures felt singularity is kept unchanged.
7. **Tenet 4 "What the tenet says" went past the tenet.** The old text read: "quantum measurements yield single outcomes". `tenets.md` L113 says only "The many-worlds interpretation of quantum mechanics is rejected". Single-outcome actualisation is the *unstated* posit (2) in `background-commitments` and `tenets.md` L184. *Fixed*: the line now states that the single-outcome claim is a further posit the tenets leave unstated, with a link. Seed: L174 ("quantum measurements yield single outcomes").
8. **Dualism stated as compulsory.** The old text read: "cannot be abandoned without denying the hard problem". McGinn, Russellian monists and panpsychists keep the hard problem without the Map's dualism, and the article's own Comparative Context lists panpsychism's void. `tenets.md` L55 calls Tenet 1 "a commitment the Map owns, not a result it reports". *Fixed*: the line now reads "a contested judgement about the explanatory gap rather than a result; rivals that keep the hard problem pay with voids of their own". Seed: none.
9. **Gödel stated without its hypotheses and applied to an informal framework.** The old text read: "Gödelian considerations suggest sufficiently rich systems contain undecidable propositions. The Map's consistency may be such a proposition—… impossible to determine from inside." Gödel II applies to consistent, effectively axiomatised systems containing enough arithmetic, and it says such a system cannot *prove* its own consistency. That is weaker than calling consistency undecidable. *Fixed*: the theorem is stated with its hypotheses, followed by "does not apply to an informal framework, so it offers only an analogy". This matches today's `interface-formalization-void` repair. Seed: L196 and L220 ("Gödelian evidence").
10. **Persistence read as evidence of structure, inside an unclosed parenthesis.** The old text read: "(though the dissolution problem cautions … since Princess Elisabeth posed it to Descartes in 1643, suggesting structural difficulty rather than insufficient effort." The parenthesis never closes (a merge artefact from 9fc2e5fb22), and the inference contradicts the dissolution caution in the same sentence. *Fixed*: the parenthesis is removed. The record is now called "consistent with a structural difficulty without favouring it over no interaction, a misframed question, or concepts not yet built", the wording of the sibling `causal-interface` repair (changelog L12466). "Posed it" became "pressed at least since … put it to". SEP *Mental Causation* (Reference 1) says "Descartes was well aware of the difficulty. Princess Elisabeth … puts it forcefully to him in a 1643 letter". Seed: L218 ("This persistence suggests structural difficulty").
11. **Mechanism Void "refuses to fill because" stated as fact.** The same sentence was repaired in `causal-interface` (changelog L12466), where "The placeholder refuses to fill because…" became "One diagnosis is…". *Fixed* the same way here, with the non-discrimination clause added. Seed: L158/L160.

Two related calibration items were fixed alongside these:
- **Productive failure**: "the shape of the voids constrains what consciousness … might be" was read as evidence against P-V2 ("Tenet-generated voids are entries naming the price the framework pays"). It now reads "cartographic information, though about the framework first … bears on what consciousness might be only through whatever independent support those commitments have".
- **Hiddenness paragraph**: "provides a principled answer (the interaction is *exactly* minimal) … fine-tuning cries out" did not match `tenets.md` L69, where Tenet 2's minimality is "empirical-constraint minimality … only that no larger interaction is empirically tenable". It now says the constraint is read off the record. It also names the deflationary reply (the tenet was fitted to the null record) that the framework cannot tell apart from a fact about the interface.

### Citation Web-Verify Ledger (publisher of record)

- Maier, Dechamps & Pflitsch 2018, *Frontiers in Psychology* 9:379 — **real-correct** metadata (Crossref 10.3389/fpsyg.2018.00379; PMC5872141 full text via efetch). **Result leg**: there was one online experiment, with N = 12,571, a Quantis quantum RNG and an implicit (uninstructed, goal-dependent) intention manipulation. It found "strong evidence for H 0 (BF 01 = 10.07)". There is an exploratory caveat: the temporal change "seemed to suggest a non-random oscillative structure". *Fixed* the plural "nulls" (the Study 2 null belongs to Maier & Dechamps, in press, a different paper) and added the sample, the RNG and the direction. Stance: the authors are parapsychologists running a test for micro-PK, and the article does not present them as supporting the Map.
- McGinn 1989, *Mind* 98(391):349–366 — **real-correct** (Crossref 10.1093/mind/XCVIII.391.349). This was an **orphan** reference: it had no inline cite. It is now cited in Comparative Context, with the paraphrase checked in the full text: "(i) there exists some property of the brain that accounts naturalistically for consciousness; (ii) we are cognitively closed with respect to that property" (p. 352). Stance: McGinn is a naturalist who files Cartesian dualism among "supernatural" solutions. The article presents him as rejecting the first tenet.
- Stapp 2000, arXiv:quant-ph/0010029, "The importance of quantum decoherence in brain processes" — **real-correct** (arXiv API and the PDF text; submitted to Phys. Rev. E). Added. The quoted claim was grepped in the PDF (see Issue 2). Stance: Stapp is an interactionist. He is cited only for his own claim about his own model.
- Tegmark 2000, *Physical Review E* 61(4):4194–4206 — **real-correct** (Crossref 10.1103/PhysRevE.61.4194). Added. Before this pass Tegmark was named inline with no reference. Stance: Tegmark is a physicalist critic, and the article cites him only for his estimates of decoherence timescales.
- Byers 2011, *The Blind Spot* (Princeton UP) — real, but an **orphan** with no inline cite. **Removed**. The publisher page sits behind a Cloudflare 403, so the book's content claims could not be checked, and nothing in the body depends on it.
- SEP *Mental Causation*, SEP *Quantum Approaches to Consciousness*, IEP *Mind and the Causal Exclusion Problem*, IEP *Hard Problem of Consciousness* (the IEP URL's misspelling "conciousness" is IEP's own), SEP *Hiddenness of God* — every URL returns 200 with a matching title. These are general reference entries, and each topic is named in the body. SEP *Mental Causation* also supports the 1643 claim.
- Not cited: List 2023 (*Noûs* 57(2):316–340, Crossref 10.1111/nous.12408). It was checked only because the seed note and `tenets.md` L115 cite it. The article now mentions "first-personally centred variants" without naming List.
- **Superlative sweep**: `find_superlative_claims` returned nothing.
- **Inline ↔ References**: Maier, McGinn, Stapp and Tegmark now match both ways.

### Map-Internal Quotation and Gloss Re-grep

- "objective reduction with consciousness modulation": matches `tenets.md` L125 verbatim (italic there).
- "Five *stated* commitments" … "is not": matches `background-commitments` L36 verbatim.
- "on minimum-outside-corridor readings the effects are in principle detectable" (link text): the source is `judging-the-map-as-science` L144 ("the effects are in principle detectable on minimum-outside-corridor readings"). The words are reordered inside link text rather than quoted. Faithful.
- Taxonomy gloss: it said the tenet-generated voids were "the category where the framework's commitments shape what counts as a void in the first place", which is **not** in `taxonomy-of-voids`. Replaced with the verbatim L181 text, "entries naming the price the framework pays, not evidence for the tenets".
- Binding-void gloss: it said the rival analyses "each presuppose phenomenal unity". `binding-void` L131 says "each reach for something already unified", and only Dainton takes unity as primitive. Aligned.
- The reverse direction: `taxonomy-of-voids` L171 quotes this page's "one signature, though, not five". That string is kept verbatim.
- Five tenet paraphrases checked against the current `tenets.md`: Dualism (L53) is faithful. MQI (L63/L65) is faithful. BI changed from "physical outcomes" to L89's "the physical world". NMW is Issue 7. Occam (L131) is verbatim. The Meta-Void line "provides no alternative criterion" was sharpened: L131 names the failure condition ("when we lack the concepts or data") but gives no test for it.
- Position IDs: P-Q1 ("relocates rather than resolves"), P-Q2 (grain), P-Q3 (`^mechanism-debt`, Maier update 09-27), P-Q4 (two gates), P-Q10 (no toy model) and P-V3 ("a void adds no weight to any tenet") were all read in full. The block anchors `^p-q2`, `^p-q4`, `^p-v3` and `^tenet-3-epiphenomenalism`, and the heading `quantum-consciousness#Quantum Zeno Effect (Stapp)`, all resolve.
- Voids index terminology: the territory-axis **Occluded** means "blocked *on purpose*" (`voids/voids` L79), and the index warns against conflating it with the reason axis. The article's Occluded paragraph is about self-blocking inquiry, so it now says "blocked rather than out of reach, where what blocks is the inquiry itself rather than any outside agent".

### Calibration Grades (evidential-status discipline)

The page makes no claim above *compatible*. The voids are presented as costs (P-V2) and add no weight (P-V3). The McGinn sentence shows that the Mechanism Void does not discriminate, since it also arises without Tenet 1. The persistence of the interaction problem is graded *compatible*, not *suggestive*. The Detection Void's conditioned signature is unmeasured, and the one large external-RNG null does not bear on the corridor, so nothing here is *discriminating*.

### Reasoning-Mode Classification (changelog only)

- MWI: Mode Three, unchanged. The tenet's own branch-egalitarian scope now marks the boundary.
- Madhyamaka no-self: Mode Three, unchanged.
- Epiphenomenalism (Relation section): newly Mode Three: "deepest difficulty … not a refutation".
- Tegmark and Stapp: not replies. They are cited for what each claims.
- McGinn: comparative, not opposed.
- No label leakage.

### Medium Issues Found

- Meta-Void "no alternative criterion" sharpened (see above).
- Duplicate Further Reading entry for `meta-epistemology-of-limits` removed: the same page was listed twice.

## Optimistic Analysis Summary

The seven personas engaged. Strengths preserved:
- the "What the tenet says / What it cannot answer" format
- the Epistemic Privilege Void
- the Completeness Void's partial-boundary concession
- the "Gaps documented rather than defended" heading (09-04)
- "What Would Challenge This Analysis?"
- the reflexive Meta-Void

The Hardline Empiricist persona credits the new McGinn sentence and the deflationary "fitted to the null record" reply as restraint that names an alternative and does not upgrade the evidence. The Process Philosopher's praise of the cross-tenet structure justifies no grade change.

### Cross-links Added
- [[positions/quantum-interface#^p-q2|P-Q2]], [[positions/quantum-interface#^p-q4|P-Q4]], [[positions/voids-as-evidence#^p-v3|P-V3]]
- [[tenets#^tenet-3-epiphenomenalism]], [[tenets#^minimal-quantum-interaction|Tenet 2]]
- [[quantum-consciousness#Quantum Zeno Effect (Stapp)]]

## Length Management

- **Before**: 2,500 words (`analyze_length`; voids soft 2,000, hard 3,000)
- **After**: 2,820 words (+320). That leaves 179 words of headroom below the hard gate (`>=` 3,000).
- **Mode**: length-neutral where possible. About 110 words were trimmed to offset additions:
  - the Gödel sentence
  - the hiddenness tail
  - the Relation lines
  - the "Intellectual honesty" bullet, which repeated the lead
  - "Dynamic evolution"
  - a duplicate Further Reading entry
  - "Three of the five tenets …", which repeated L47
- The remaining growth comes from the eleven critical fixes and two added references.

## Remaining Items (for the driver to mint)

1. **`tenets.md` L71 and P-Q1 (`positions/quantum-interface` L55)** class Stapp's Zeno approach as pre-decoherence or coherence-dependent ("Other proposals depend on pre-decoherence coherence … Stapp's quantum Zeno approach"; "pressed against pre-decoherence proposals (Stapp-Zeno, Orch-OR)"). This contradicts Stapp (2000) and the Map's own `quantum-consciousness` L122.
2. **`tenets.md` L107** says "under any *unconditioned aggregate* test current or foreseeable instruments could run", which contradicts its own L75 ("by construction, not by any sensitivity limit") and P-Q2. The same instrument-limit phrase appears in `concepts/pragmatism` L44, `concepts/von-neumann-wigner-interpretation` L102 and `concepts/quantum-completeness` L82. `grep -rlF "current or foreseeable instruments" obsidian` returns 4 live files outside reviews/workflow.
3. **Maier et al. 2018 "nulls" (plural)** appears in 11 live loci, among them `tenets.md` L75, P-Q3 L78, P-Q9 L146, `parapsychology-firewall` L51, `amplification-void` L63 and `research-programme-decisions-under-the-map` L86/L124 (`grep -rnF "intention-to-RNG nulls"`). The paper reports one experiment, so the plural is unsupported by it.
4. **Seed note `research/voids-tenet-generated-voids-2026-01-25.md`** needs a Correction line for:
   - L166 "simultaneously real and undetectable"
   - L174 "quantum measurements yield single outcomes"
   - L196/L220 Gödel without hypotheses
   - L218 persistence as evidence
   - L158/L160 "refuses to fill" stated as fact
   - L79 an unverified attribution to Wallace ("'I' can make sense only if confined to a single branch")
   - L92 an unverified Byers quotation, probably jacket copy
5. **`concepts/many-worlds` L73–82** asserts that the Deutsch–Wallace derivation *requires* a cross-branch personal-identity relation. This needs source-checking against Wallace (2012) and Saunders & Wallace (2008, diverging view), and alignment with the scoped `tenets.md` L115.
6. **`tenet-check-2026-09-28` L170 Tenet-4 list**: this page's item is now discharged, but the 13 sibling loci listed there were not checked this pass.
7. **P-Q2 vs P-Q9/`tenets.md` L75 grain tension**: P-Q2 (10-14) says public-label conditioned deviations are the minimum-outside-corridor fallback, while P-Q9 (09-09) and `tenets.md` L75 describe them as testing "the corridor itself". The two can be read consistently, but P-Q2's own note says `apex/born-preserving-causal-efficacy` "owes a wording fix".

**Could not verify**: the Byers book content (Cloudflare 403), and whether Gassendi's Fifth Objections (1641) first raised the problem. The article no longer makes an originator claim.

## Stability Notes

- The bedrock items from prior reviews stand: the eliminativist "self-inflicted voids" objection, MWI one-branch metaphysics, Madhyamaka no-self, and the divine-hiddenness parallel as analogy.
- **New**: future reviews should **not** restore any of the following:
  - the plurality void as support for Tenet 4
  - Stapp as "coherence-dependent"
  - the "Tenets 1, 3 and 4" root posit without the sub-reading qualifier
  - the "current or foreseeable instruments" wording
  - the "Gödelian undecidability" of the Map's consistency
  - "No amount of further effort closes it"
  
  Each was a correctable calibration or attribution error, not a philosophical disagreement.
- Convergence on this page should key on upstream changes (`tenets.md`, `positions/quantum-interface`, `positions/voids-as-evidence`, `background-commitments`, `plurality-void`, `binding-void`, `taxonomy-of-voids`), not on the page's own stability. The 06-25 "fully converged" verdict missed six of the eleven defects, which were already on the page (1, 3, 7, 8, 9, 11; all but 1 present since creation, 1 since 2026-02-24). Four more (2, 4, 5, 6) were introduced by later refines or stranded by upstream rewording, and 10 is mixed (the inference since creation, the unclosed parenthesis from 9fc2e5fb22).
