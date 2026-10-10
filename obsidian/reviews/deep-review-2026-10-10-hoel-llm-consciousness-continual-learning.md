---
title: "Deep Review - Hoel's Disproof of LLM Consciousness"
created: 2026-10-10
modified: 2026-10-10
human_modified: null
ai_modified: 2026-10-10T10:59:39+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-10
last_curated: null
---

**Date**: 2026-10-10
**Article**: [[hoel-llm-consciousness-continual-learning|Hoel's Disproof of LLM Consciousness]]
**Previous review**: [[deep-review-2026-07-18-hoel-llm-consciousness-continual-learning|2026-07-18]] (seventh deep review overall). Also read: [[pessimistic-2026-09-27-hoel-llm-consciousness-continual-learning]] and the 2026-09-27 refine-draft that acted on it (commit 6e0144ab01).

## Scope of This Pass

The 07-18 review called the article a strong convergence-damping candidate and named "substantive new body content" as a re-review trigger. The 09-27 refine-draft rewrote about a third of the body (non-triviality definition, IIT horn, the Corollary 5.5 reply, the open-flank paragraph, the tautology reply, a new amnesia paragraph, the Dualism and Bidirectional paragraphs). This pass audits that rewrite against the primary source. The arXiv HTML of 2512.12802v3 was downloaded and converted to plain text, and every Hoel claim was grepped in the raw text. The research note and the pessimistic review were not used to verify anything. The full paper was then read for anything material the article leaves out.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Horn mapping reversed (L66)**. The article said continual learning gives lenient dependency "(avoiding unfalsifiability)" and that substitutions fail "because lookup tables cannot learn (ensuring non-triviality)". In Hoel, invalid static substitutes (Corollary 5.5) protect a learning theory against **a priori falsification**. Non-triviality comes from Proposition 5.6 (latent learning and multiple realisability let predictions come apart from inferences). **Resolution**: rewritten so each horn has the right mechanism, scoped to "a priori falsification by static substitution". Hoel says outright: "This is not to say that the results herein currently show that all universal substitutions for learning systems are impossible."
2. **Omission that weakens the alignment claim: Hoel's verdict on substance dualism**. In §4.1 item 3, Hoel lists metaphysical theories that are "scientifically trivial per Definition 4.1" and names "potential candidates include theories like substance dualism [Descartes] or analytic idealism". The article said the Map "finds Hoel's framework largely aligned with its commitments" and never mentioned that his framework puts the Map's own foundational commitment in the trivial bin. A reviewer who accepts the tenets would still flag this: the article presented a source as an ally while leaving out the source's direct pressure on the tenet. **Resolution**: the Relation opener now reads "verdict on current LLMs largely aligned … his framework also presses on dualism itself". The Dualism paragraph reports Hoel's classification and gives the Map's reply: interactionist dualism ties consciousness to a causal interface rather than to behaviour, so its predictions need not be fixed by behavioural data. It then says plainly that whether those predictions could actually come apart from the data "is open".
3. **Dropped qualifier on Definition 4.2**. Hoel's "non-conscious" label depends on an assumption he states openly: "I assume that trivial theories of consciousness must be false … all the conclusions would still hold but with this sort of replacement language". The article gave Definition 4.2 without it. **Resolution**: one sentence added giving the assumption and the weaker reading that applies without it.
4. **Proximity-argument summary covered only one horn (L58)**. The old text said no theory could attribute consciousness to LLMs "without also attributing it to such equivalents". That is the triviality horn alone. Hoel's Constraint Theorem (Theorem 4.6) and Proposition 4.8 close both horns: properties lost along the chain vary while inferences stay fixed (a priori falsification), and input-output grounding is trivial. **Resolution**: the paragraph is rewritten around Theorem 4.6 and Proposition 4.8, with the same length.
5. **Unverifiable Cerullo quote**. "nearly tautological" entered the article at creation (2026-02-22, opus-4-6 cohort) and had no research-note source. The 03-19 and 04-23 reviews "verified" it against intra-corpus text, and the 06-26 web-verify checked only the other two quotes. A raw-source grep was impossible because PhilArchive and PhilPapers record pages are Cloudflare-blocked (HTTP 403 and challenge pages to curl, WebFetch and a reader proxy). Cerullo's current abstract, read through the PhilPapers browse listing, says the criterion is "tautological, ad hoc, and inconsistently applied". **Resolution**: the quote marks and "nearly" are removed, and the charge is paraphrased from the current abstract. The weight-versus-context framing is now the article's own development of the inconsistency charge ("The inconsistency charge is sharpest for…"). It is no longer attributed to Cerullo, because that attribution could not be checked against his body text.
6. **Factual error (MQI paragraph)**. The article said Hoel's framework "does not engage with quantum processes". Hoel lists "quantum processes in the brain" as one factor that might make universal substitutes for humans ill-defined. **Resolution**: corrected. The Map now treats that aside as a point of contact rather than a conflict.

### Medium Issues Found

- **Reference orphans**: Tononi 2008, Baars 1988 and Chalmers 1996 were in References with no inline cite. The 06-26 review counted them as "underpinning" discussions, and one of those discussions (zombies) is no longer in the body. **Resolution**: inline cites added at IIT, global workspaces and the hard problem (+6 words). Kleiner and Hoel 2021, the source of the dilemma the article names, is now cited and referenced.
- **Training-time scope**: Hoel says the disproof "does not rule out LLM consciousness during their training … nor does it guarantee their consciousness in any way". The article left this out. **Resolution**: added to "What the Paper Does Not Claim", together with the static-substitutes-only concession.
- **Clive Wearing "memory span of seconds to minutes"**: the standard account is seconds (roughly 7–30 s). Narrowed to "seconds".
- **Map speculation inside exposition (L64 expertise void)**: the old wording "illuminates what continual learning actually does to consciousness" sat inside the Hoel exposition and said more than the evidence supports. Compressed and marked "On the Map's reading".
- **Duplicate paragraph**: the "same holds more broadly" Cerullo paragraph repeated the framework-boundary point made just before it. Removed; its job is now done by the Cerullo sentence in the Dualism paragraph.

### §2.4 Citation Ledger (publisher of record, this pass)

- Hoel 2026 (arXiv:2512.12802), state: **real-correct**. Abstract page: v1 14 Dec 2025, v2 12 Jan 2026, v3 19 Jan 2026, matching "first posted December 2025, revised January 2026". Raw-text grep of v3 confirms these verbatim: "strict dependency between its predictions and inferences" (Definition 4.1); Definition 4.2 wording; "Kleiner-Hoel dilemma"; "lenient dependency" (Definition 4.11); "thus, IIT would say that LLMs are not conscious"; "theater" plus global workspaces [Baars 1997]; quantum processes, computational irreducibility and the no-cloning theorem; the transformer→RNN→single-hidden-layer FNN→lookup-table chain; Corollary 5.5 (a) external memory and (b) experimentally derivative/monitoring; "baseline LLMs mimic learning via external memory"; identical output probabilities; latent learning and "multiple-realizability of learning" (Proposition 5.6); "requires no opinion on whether qualia is causally relevant or epiphenomenal" (the article paraphrases "qualia" as "consciousness", unquoted, acceptable); "substitution space" (Hoel's own scare-quoted term); "merely a necessary condition, not a sufficient one"; the abstract's "If continual learning is linked…" quote is verbatim.
- Result-direction leg (Hoel): the IIT verdict (LLMs not conscious, Φ=0) is the right direction; "necessary not sufficient" is the right direction. Hoel even says a continually learning module appended to an LLM "would not necessarily render the LLM conscious", which is consistent with the article's "reassessed case by case".
- Cerullo 2026 (PhilArchive CERWHD), state: **real-correct metadata; quote fidelity partially verified**. The title matches (WebSearch index and PhilPapers browse listing). "conflates two distinct targets of consciousness science", "the normal operation of a science that takes third-person consciousness as its subject matter" and "speculative escape hatches—quantum processes, computational irreducibility[, or unspecified non-computational properties]" are corroborated by the search index's text of the PhilArchive record, which looks like an earlier abstract version. The current abstract on PhilPapers words these points differently ("a conflation of first-person and third-person consciousness"; "Blocking this symmetry requires a positive commitment, whether substance dualism, Penrose-style non-computability, or biological naturalism"; "tautological, ad hoc, and inconsistently applied"). That text was read through the WebFetch summariser only, not a raw grep, so the confidence is medium. "nearly tautological" is **unverified in any version** and has been de-quoted. If raw access to PhilArchive becomes possible, re-grep the two retained quotes against the current version.
- Kleiner & Hoel 2021, "Falsification and consciousness", *Neuroscience of Consciousness* 2021(1) niab001, state: **real-correct** (Crossref 10.1093/nc/niab001; it is Hoel's ref [18] for the dilemma). Newly added.
- Corkin 2002, "What's new with the amnesic patient H.M.?", *Nat Rev Neurosci* 3(2):153–160, state: **real-correct** (Crossref 10.1038/nrn726). Result direction: H.M.'s preserved nondeclarative and motor-skill learning, mirror tracing included, is the right direction.
- Tononi 2008, *Biological Bulletin* 215(3):216–242, state: **real-correct** (Crossref 10.2307/25470707).
- Baars 1988 and Chalmers 1996: standard monographs, metadata unchanged from the 06-26 verification, state: **real-correct**.
- Superlative helper: zero candidates.
- Cited-author-stance leg: Hoel calls his argument "philosophically neutral" and lists substance dualism as a candidate trivial theory. The article now says he does not endorse the Map's conclusion and that his framework presses on dualism. Cerullo is a functionalist critic and is presented as one.

### Counterarguments Considered

- The Many-Worlds Defender, the eliminativist and the empiricist objections are bedrock or were already addressed (the 09-27 analogy-not-entailment wording is preserved; the amnesia paragraph is in place).
- Cerullo's symmetry objection ("the proof proves too much"), which is new in his current abstract, is now engaged in the Dualism paragraph as framework-boundary marking. The Map accepts the positive commitment Cerullo says is needed, and the article states that for the Map the brain–LLM asymmetry therefore *follows from* its tenets and is *not independent evidence for* them.

## Reasoning-Mode Classification (editor-internal)

- Cerullo, first-/third-person conflation: Mode Three (unchanged; boundary marked at the end of the tautology paragraph).
- Cerullo, tautology: Mode Two→Three mixed (unchanged from 09-27: in-framework non-circularity, then boundary on phenomenology).
- Cerullo, inconsistency (context vs weights): Hoel's in-framework reply (Corollary 5.5) plus the open flank, unchanged.
- Cerullo, symmetry / positive-commitment (new): Mode Three. The Map holds the commitment, says so, and declines to count it as evidence.
- Hoel, substance dualism as candidate-trivial (new): Mixed. The Map's reply is made on Hoel's own terms (interface-grounded predictions are not strictly dependent on behavioural data), and the residue (whether they can actually diverge) is marked open. No label leakage (grep clean).

## Calibration Check

Pass after fixes. The new Dualism material lowers the article's evidential claims: it concedes that Hoel classes substance dualism as possibly trivial, leaves the Map's escape route open, and refuses to count the asymmetry as evidence for the tenets. No tenet is used to raise any empirical claim. The MQI paragraph keeps "speculatively".

## Optimistic Analysis Summary

### Strengths Preserved

- "Frozen target rather than a moving one"; "What the Paper Does Not Claim"; the open-flank paragraph; the amnesia test case with its "rescue has a cost" turn; the quantum-randomness-channel convergence (07-18 fix); the Bidirectional paragraph's coherent version (09-27 fix); burden-of-proof reframing.

### Enhancements Made

- The Dualism paragraph now joins Hoel's verdict on dualism and Cerullo's positive-commitment objection into one honest account of the Map's position. Hoel thinks dualism may be scientifically trivial, and Cerullo thinks only something like dualism blocks the symmetry. The Map sits where the two meet and says so. This is the most useful thing the article does that the sibling articles do not.
- The proximity argument now states Hoel's actual two-horn closure (Theorem 4.6, Proposition 4.8).

### Cross-links Added

None. The article is well linked; the change was in how existing links are framed.

## Length

3123 → 3122 words (analyze_length total; about 2,850 prose and 275 apparatus). The article was at soft_warning on entry, so the pass ran in length-neutral mode: each addition was paired with a cut (duplicate Cerullo paragraph, the expertise-void sentence, a repeated IIT exposure sentence, the MQI "complementary" sentence, Further Reading annotations).

## Remaining Items

- **Sibling carry-forward (task minted, P2 refine-draft)**: `concepts/continual-learning-argument` L50 and `topics/ai-consciousness` L115 still carry the "systems that clearly lack it" misstatement of non-triviality that the 09-27 refine fixed here, and continual-learning-argument L158 still reads Hoel as support for anti-functionalism.
- **Cerullo raw-text verification**: blocked by Cloudflare. If a raw copy becomes reachable, grep the two retained quotes against the current version, and check whether the paper's body ties "inconsistently applied" to context-based versus weight-based encoding.
- `ai_system` left at `claude-opus-4-6`. The 09-27 refine (opus-5-5) and this pass together re-authored perhaps 35–40% of the body, so a `claude-opus-4-6+claude-opus-5-5` co-attribution is defensible. It was not applied unilaterally; flagged for the operator.

## Stability Notes

- Seventh deep review. The bedrock list from 06-26 and 07-18 stands.
- **Re-verify against the raw arXiv text, not the research note.** The research note still has the original misstatement (annotated in its 09-27 correction block), and intra-corpus checks will clear defects that the primary source exposes.
- The substance-dualism disclosure and the "follows from its tenets, not independent evidence for them" sentence are deliberate calibration and should not be trimmed in later condense or length passes. Removing them would bring back the false-ally framing.
- "Escapes a priori falsification *by static substitution*" is scoped on purpose. Do not widen it to "escapes a priori falsification".
- Re-review triggers: (a) a frontier model shipped with production continual learning (re-check "frozen weights"); (b) a Hoel reply to Cerullo, or a v4 of 2512.12802; (c) raw access to Cerullo's text.
