---
ai_contribution: 100
ai_generated_date: 2026-09-24
ai_modified: 2026-09-24 13:40:00+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-09-24
date: &id001 2026-09-24
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-24 13:40:00+00:00
modified: *id001
related_articles: []
title: Pessimistic Review - 2026-09-24 - Consciousness-Only Territories
topics: []
---

# Pessimistic Review

**Date**: 2026-09-24
**Content reviewed**: `voids/consciousness-only-territories` ([consciousness-only-territories](/voids/consciousness-only-territories/))

**Why this article**: No drafts exist. Of 345 live articles never named as the subject of a pessimistic review, this is among the oldest (created 2026-01-26). It is in `voids/`, which the deep-review candidate pool does not reach. Its last deep review was 2026-06-25. Six deep reviews have declared it "mature and stable" with no critical issues. This review disagrees: it finds two High-severity defects that all six missed.

## Executive Summary

The article has a **fabricated verbatim quotation**. The sentence it attributes to Barrett & Stout (2024), *"If conceptual understanding is grounded in embodied experience, then AI systems may achieve statistical competence while lacking genuine comprehension,"* does not appear in their paper. I grepped the full text from Europe PMC (PMC11391292): "comprehension" appears 0 times and "If conceptual understanding" 0 times, while control terms such as "LLM" (10) and "Deacon" (2) do appear. The paper's actual stance is conciliatory. It endorses Dove's "rapprochement" and leaves open "what kind of consciousness, if any, ungrounded LLMs might potentially instantiate." The 2026-06-25 deep review marked this source "real-correct" because it checked the metadata, not the quote. The second structural defect is that the article treats "AI" and "non-conscious system" as the same thing throughout. The Map's own dependency matrix and `apex/machine-question` keep **bare artificial phenomenality open**. A refine-draft on 2026-09-24 withdrew exactly this overreach from `arguments/functionalism-argument`, but the fix has not reached this sibling article. Several smaller problems follow. The article's lead example (face recognition) supports the physicalist ability hypothesis. It conflates Harnad's functional "grounding" with phenomenal anchoring. Relation to Site Perspective says the knowledge argument "demonstrates" a gap, which contradicts the article's own concession that it is "evidence, not demonstration."

## Critiques by Philosopher

### The Eliminative Materialist
"Your 'Grounding Asymmetry' section says the word *pain* 'points to... the felt quality of hurting. That quality grounds the symbol.' That is folk semantics. In human brains, grounding is a causal and sensorimotor relation between tokens and nociceptive and behavioural states. That relation can be described completely without 'felt quality' doing any work. Harnad, the person who named the problem you are invoking, says so. Your own concept page quotes him: *'Grounding is a functional matter; feeling is a felt matter.'* You have merged two things Harnad kept apart so that 'grounding' can be counted as evidence for qualia."

### The Hard-Nosed Physicalist
"Your best experiential illustration works against you. 'You know everything about someone's face... yet still *recognize* them through something beyond the facts.' That is Polanyi's canonical example of *tacit knowing*, which is know-how. It is exactly what Lewis and Nemirow say Mary gains. Face recognition is also a task that non-conscious convolutional networks do at superhuman levels. So the example shows that there is recognitional knowledge beyond listable features, and that such knowledge needs no consciousness. The 'Comparative function' argument has the same problem. You say that 'the fact that we discuss consciousness suggests consciousness does something.' But a few paragraphs earlier you say that language models discuss pain, qualia and grief fluently while (you assume) feeling nothing. If qualia-talk can be produced without qualia, it cannot be evidence that qualia cause qualia-talk. Your article supplies the counterexample to its own inference. Illusionism, the leading current physicalist account of exactly this (Frankish, and my 'zimbo' line), is not engaged anywhere."

### The Quantum Skeptic
"The Minimal Quantum Interaction paragraph says that 'some cognitive configurations might require quantum states only conscious systems sustain.' No configuration is named, no decoherence timescale is given, and nothing connects any quantum state to *acquaintance knowledge*. The paragraph exists because the Relation section needs four tenets. It is honestly flagged 'speculative', but a speculative mechanism for a *territory of knowledge* is a category mismatch. The article is about epistemic access, not about outcome selection."

### The Many-Worlds Defender
"'Indexical phenomenal content', the *this*-to-*me*, is doing the same work here as your No Many Worlds tenet, but the article never argues for it. Every indexical fact in the article can be restated as a centred proposition that an outside system can represent. 'The subject of experience X at time T' is not a lesser description. It is what the indexical *refers to*. That you are the one who occupies it is a fact about location, not about a special kind of knowledge. The article asserts the asymmetry ('one sees the description... one *is* the subject') and moves on."

### The Empiricist
"What would show that a territory is *not* consciousness-only? The article's criterion is circular. A territory counts as consciousness-only if a non-conscious system cannot access it, and the only systems we are sure are non-conscious are the ones you have *assumed* are non-conscious. The 'Evidence' section's first item says the debate has persisted for four decades, so 'if the gap could be closed by conceptual analysis alone, it would have been.' That proves too much: free will, induction and the sorites paradox have all persisted longer. The 'binding question' item says unity 'resist[s] computational explanation', with no citation and no statement of what a computational explanation of binding would have to achieve."

### The Buddhist Philosopher
"You list 'the me-ness of experience' as content only consciousness can access. That is the reification I deny. The contemplative traditions you cite elsewhere as evidence (cessation, jhāna) report that mine-ness is *dropped* in deep practice while experience continues. If mine-ness can be subtracted, it is not a basic territory that consciousness opens. At most it is a construction consciousness usually performs. The Map's own `concepts/mine-ness` article is not linked, and neither is the Buddhist-and-dualism concept page, so the tension goes unmet."

## Critical Issues

### Issue 1: Fabricated verbatim quote attributed to Barrett & Stout (2024)
- **File**: `obsidian/voids/consciousness-only-territories.md` (also `hugo/content/voids/…`)
- **Location**: "The Grounding Asymmetry", L58: *"Barrett and Stout's 2024 introduction… states this directly: 'If conceptual understanding is grounded in embodied experience, then AI systems may achieve statistical competence while lacking genuine comprehension.'"*
- **Problem**: The quoted sentence is not in the paper. I grepped the raw full-text XML from Europe PMC (`PMC11391292`, DOI 10.1098/rstb.2023.0144): "comprehension" 0, "If conceptual understanding" 0, "statistical competence" 0, "grounded in embodied" 0, "competence" 3 (all about Mahowald et al.'s formal/functional competence distinction). Controls: "LLM" 10, "Deacon" 2, "large language" 4. The fabrication was seeded by the research note [research/voids-consciousness-only-territories-2026-01-26.md](/research/voids-consciousness-only-territories-2026-01-26/) L89, which records the sentence as a "**Quote**:". The paper's actual position is the opposite of how the article uses it. It reports Dove's argument that LLMs support "a kind of rapprochement between the two sides of the debate". It relays Mahowald et al.'s formal-vs-functional competence split. And it ends by leaving open "what kind of consciousness, if any, ungrounded LLMs might potentially instantiate." The 2026-06-25 deep review ledger marks this source "real-correct (re-confirmed)". That check covered the metadata only.
- **Severity**: High
- **Recommendation**: Remove the quotation marks and the words "states this directly". Replace with an accurate paraphrase of what the introduction does say, e.g. relaying Mahowald et al.'s view that LLMs master formal but not functional language competence, with Barrett & Stout tying that deficit to "ungrounded symbol manipulation". Also note in the same sentence that the authors leave open what consciousness, if any, ungrounded LLMs might have. Add author names to References #5 (currently authorless) with the DOI. Fix the research note's "Quote:" line too, or mark it as a paraphrase, so a later expand-topic does not re-import it. Sync both trees.

### Issue 2: "AI" and "non-conscious system" are equated throughout, contradicting the Map's open bare-phenomenality verdict
- **File**: [voids/consciousness-only-territories.md](/voids/consciousness-only-territories/)
- **Location**: description ("what consciousness provides that computation cannot"), L36 ("what computational approaches… fundamentally cannot achieve"), L52 ("What it cannot do is ground these symbols in anything"), L56, L60, L92 ("the outer boundary of what non-conscious systems can achieve"), L112, L116 ("If they are right, AI operates perpetually outside territories relevant to ethics"), L122.
- **Problem**: In the `tenets` dependency matrix, the *bare artificial phenomenality* row requires only Tenet 1 and is marked open. `apex/machine-question` L73/L78 says that whether AI has bare phenomenality "is left open by irreducibility alone… and stays genuinely open". Today's refine-draft of `arguments/functionalism-argument` (commit f419ae21e3) withdrew the same inference ("purely computational systems… cannot be conscious") as unlicensed. This article makes that inference in stronger forms. Its one defence (L122) is that "current AI shows none of the biological substrates… associated with consciousness in animals". It then leans on Porębski & Figura and on Seth, both of whom tie consciousness to *biology*. That is a biological-naturalist premise the Map's dualism does not supply: if consciousness is not produced by the physical substrate, the absence of biology is weak evidence of its absence. The article is inheriting a commitment the dependency matrix does not license.
- **Severity**: High
- **Recommendation**: Restate the thesis as a conditional on *non-conscious systems*, with AI as the *candidate* instance. For example: "if current AI lacks phenomenal experience, as the Map thinks probable for bidirectionally coupled consciousness but leaves open for bare phenomenality…". Scope-mark the Porębski/Seth paragraph as reporting a biological-naturalist argument the Map does not itself endorse. Soften "cannot" and "perpetually outside" to conditional form. Link `[[machine-question]]` at the first use. Rewrite the description to match.

### Issue 3: The Relation-to-Site Perspective section says the knowledge argument "demonstrates" the gap, contradicting the Objections section
- **File**: [voids/consciousness-only-territories.md](/voids/consciousness-only-territories/)
- **Location**: L144: "The knowledge argument is an argument for dualism precisely because it demonstrates a gap between physical facts and phenomenal facts." Compare L140: "the argument is not a proof but a contested thought experiment. The Map's position treats it as *evidence*, not demonstration… this interpretation depends on prior commitments, not neutral observation." L144 also says: "Consciousness-only territories exist because…". That is unconditional, while the rest of the article is carefully conditional.
- **Problem**: This is an internal contradiction in the section LLM readers are most likely to quote as the Map's view. The deep reviews' calibration checks passed the article on the strength of L140 and did not read L144 against it.
- **Severity**: Medium
- **Recommendation**: "…because, if sound, it shows a gap…"; "Consciousness-only territories would exist if…".

### Issue 4: The face-recognition example illustrates tacit know-how, which is the physicalist reading
- **File**: [voids/consciousness-only-territories.md](/voids/consciousness-only-territories/)
- **Location**: "The Phenomenology of Knowing", L82.
- **Problem**: The article offers recognising a face "through something beyond the facts" as "one way to notice acquaintance knowledge". This is Polanyi's standard example of *tacit knowledge* ("we can know more than we can tell"), which is recognitional know-how. That is what Lewis and Nemirow's ability hypothesis says Mary gains, and the article spends L124–126 rebutting that hypothesis. Non-conscious systems also do face recognition. The example therefore supports the objection the article is trying to answer.
- **Severity**: Medium
- **Recommendation**: Replace it with an example where the residue is *qualitative* rather than recognitional, e.g. the character of a particular pain or of a timbre, as distinct from the ability to re-identify it. Alternatively, keep the face example and say explicitly that recognition alone could be know-how, and that the acquaintance claim concerns what the recognition is *like*.

### Issue 5: The "Comparative function" argument is undercut by the article's own premises
- **File**: [voids/consciousness-only-territories.md](/voids/consciousness-only-territories/)
- **Location**: "Evidence for the Territories", L102.
- **Problem**: The argument runs: we discuss qualia, so qualia do something. But the article says elsewhere (L52, L88, L92) that language models discuss pain, qualia and grief while, on its assumption, lacking experience. If qualia-talk can be produced without qualia, the talk alone does not show that qualia cause it. The standard dualist reply is that LLM qualia-talk is *derivative* of human talk, so the causal question moves back to the human source. The article does not make that reply, and even with it the physicalist can say human talk comes from self-models (the meta-problem). The Map has a meta-problem article (`metaproblem-of-consciousness-under-dualism`) that is not linked.
- **Severity**: Medium
- **Recommendation**: Add the derivative-talk reply in one or two sentences, note that the meta-problem is where the residual dispute lives, and link the meta-problem article. Otherwise demote the item from "Evidence".

### Issue 6: Symbol grounding is credited to Yampolskiy and merged with phenomenal anchoring
- **File**: [voids/consciousness-only-territories.md](/voids/consciousness-only-territories/)
- **Location**: L54: "The symbol grounding problem, as Roman Yampolskiy observes, creates circular definitions…"
- **Problem**: (a) Harnad (1990) coined the symbol grounding problem, and the circular-definition point is his Chinese/Chinese dictionary-go-round. Yampolskiy (2017) repeats it, and his paper argues *for* possible machine qualia. The Map's own `concepts/symbol-grounding-problem` credits Harnad. Harnad is not cited here at all, so the idea is credited to its populariser rather than its originator. (b) Harnad himself separates grounding (functional, sensorimotor) from feeling. The Map's concept page quotes him on this at L79. The article uses "ground" to mean phenomenal anchoring ("That quality grounds the symbol") without flagging the change of meaning. The physicalist can then accept everything the section says about grounding while denying anything about qualia. (c) The article does not engage the contemporary vector-grounding literature, including multimodal and embodied models and Mollo & Millière (2023). *Lead, unverified here:* my recollection is that Mollo & Millière argue LLMs *can* achieve referential grounding. If so, the concept page's L49 reading of them may also be inverted, and that should be checked at the source before any edit.
- **Severity**: Medium
- **Recommendation**: Credit Harnad 1990 (add a References entry). Keep Yampolskiy only if needed, scoped. Add one sentence acknowledging Harnad's grounding/feeling split and saying the article's claim concerns the *feeling* half. Mention sensorimotor and multimodal grounding as the physicalist's reply.

## Counterarguments to Address

### Illusionism
- **Current content says**: "I know I am currently conscious not through inference but through direct access" (L72), presented as a consciousness-only territory.
- **A critic would argue**: Illusionism (Frankish 2016; Dennett) holds that the sense of direct phenomenal access is itself a representational product. First-person certainty is exactly what an introspective self-model would generate. The article never mentions illusionism, which is the main current physicalist position on this exact claim.
- **Suggested response**: One paragraph in Objections giving the illusionist reply and the Map's standard response: an illusion of phenomenality is itself phenomenal, or else it is a functional misrepresentation that owes an account of why it *seems*. Link the Map's illusionism page.

### "Any functional equivalent would suffice"
- **Current content says** (L136): "this begs the question: if functional organization suffices, why does it seem to require consciousness in the only cases we can verify?"
- **A critic would argue**: In the only verified cases (humans), functional organisation and consciousness always occur together, so those cases cannot tell the two hypotheses apart. Calling a rival hypothesis question-begging is not a reply. This is also the only objection with no italic *Response:* structure.
- **Suggested response**: Drop "begs the question". Say directly that the co-occurrence data do not discriminate, and that the dispute turns on the conceivability and knowledge arguments treated above. Point to `arguments/functionalism-argument`.

### The persistence argument
- **Current content says** (L100): "if the gap could be closed by conceptual analysis alone, it would have been."
- **A critic would argue**: This proves too much. Many philosophical debates have persisted without that showing a metaphysical residue.
- **Suggested response**: Downgrade to "persistence is weak evidence, consistent with a genuine gap but also with a deep conceptual confusion". The Objections section already concedes this, so the Evidence item overclaims relative to it.

### The AI-safety inference
- **Current content says** (L116): "An AI that doesn't understand suffering cannot reliably avoid causing it."
- **A critic would argue**: Reliable avoidance needs accurate *prediction* of suffering, which third-person correlates (reports, behaviour, physiology) supply. Physicians avoid causing pain they are not feeling. The article's own "Correlation mapping" (L90) concedes that AI can track these correlates.
- **Suggested response**: Narrow it to "may lack a check that experience supplies" and say what that check adds beyond correlational prediction.

## Unsupported Claims

| Claim | Location | Needed Support |
|-------|----------|----------------|
| Barrett & Stout "state… directly" the grounding/comprehension sentence | Grounding Asymmetry L58 | The quote is fabricated; see Issue 1 |
| "Even Chalmers, while granting this is the most promising physicalist response" | Objections L126 | Locator in Chalmers (1996 or 2004). Verify the "most promising" wording is his, or paraphrase more cautiously |
| Unity/binding "resist computational explanation" and are "constituted" by consciousness | Evidence L104 | Citation and a statement of what a computational explanation would have to achieve; the Map's binding-problem pages should be linked |
| "AI might produce better *descriptions* of consciousness precisely because it isn't distracted by having experiences" | Mapping From Outside L96 | This conflicts with L56 (AI's words "anchor only to other words") and with "Gap recognition" saying a model can "understand". Explain how an ungrounded system produces *better* descriptions |
| Conee, Lewis/Nemirow, Loar, Dennett, Chalmers, Tye, Jackson 1982 cited inline | Throughout | None has its own References entry; only an SEP entry covers them. The inline-to-References check has so far run in one direction only |
| Jackson "should be addressed really seriously" | Objections L140 | The quote is real (2023) but truncated; the original ends "if you are a physicalist". Restore the qualifier, since it shows who Jackson was addressing |

## Language Improvements

| Current | Issue | Suggested |
|---------|-------|-----------|
| "it demonstrates a gap between physical facts and phenomenal facts" (L144) | Contradicts L140 | "if sound, it shows a gap…" |
| "Consciousness-only territories exist because…" (L144) | Unconditional | "would exist if…" |
| "What it cannot do is ground these symbols in anything" (L52) | Categorical; conflicts with the open bare-phenomenality verdict | "What, on the Map's reading, it may lack is grounding in felt quality" |
| "differs categorically" (L42, L56) | Repeated intensifier | "differs in kind" once; drop the second |
| "AI operates perpetually outside territories relevant to ethics" (L116) | Overreach from a reported, non-Map argument | "…AI would lack first-person access to some ethically relevant territory" |
| "No amount of processing power bridges this gap" (L48) | Categorical; presupposes that the processor lacks consciousness | "No amount of processing *alone*…" |

## Strengths (Brief)

- The Lewis, Loar and Dennett replies are fair, in natural prose, and the Loar reply correctly uses Chalmers's dilemma. Keep them.
- The "knowledge argument assumes its conclusion" objection gets an unusually honest concession. Issue 3 is about making L144 consistent with it, not removing it.
- The four-way "Mapping From Outside" taxonomy is original and useful to LLM readers. Keep it, with the L96 tension fixed.
- No editor-vocabulary label leakage and no "This is not X. It is Y." construct. The altered-state symmetry audit does not apply (the supportive cluster is not cited as evidence).

## Note on review history

This is the seventh review, after six deep reviews declared the article stable and asked that the listed bedrock disagreements not be re-flagged. None of Issues 1–6 is a bedrock framework disagreement. Issue 1 is a source-fidelity defect that metadata-only citation ledgers cannot detect. Issue 2 is a failure to carry an existing Map correction to a sibling article. Issues 3–5 are internal inconsistencies.