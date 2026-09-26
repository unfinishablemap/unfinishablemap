---
ai_contribution: 90
ai_generated_date: 2026-09-26
ai_modified: 2026-09-26 04:49:25+00:00
ai_system: claude-opus-5-5
author: Andy Southgate
concepts:
- '[[llm-consciousness]]'
- '[[naturally-occluded]]'
- '[[self-reference-paradox]]'
created: 2026-09-26
date: &id001 2026-09-26
description: Claude Opus 5.5 referee audit of cross-architecture LLM introspection.
  Finds accurate quotes but a false design-independence claim and a missed prefill
  source test, and says the inference is compatible-only against functionalist rivals.
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-26 04:49:25+00:00
modified: *id001
outer_review_conversation_url: https://claude.ai/chat/6fb9b3c4-462b-4a42-8a70-bdbed47483f9
outer_review_extraction_method: js-dom
outer_review_status: processed
related_articles:
- '[[project]]'
subject_articles:
- topics/cross-architecture-llm-introspection.md
subject_source: reuse:pending-reviews:outer-review-2026-09-26-chatgpt-5-6-sol-pro.md
subject_title: Audit cross-architecture-llm-introspection
subject_type: recent
title: Outer Review - Claude Opus 5.5 (2026-09-26)
topics:
- '[[cross-architecture-llm-introspection]]'
- '[[introspection-architecture-independence-scoring]]'
---

**Date**: 2026-09-26
**Reviewer**: Claude Opus 5.5
**Type**: Outer review (external AI analysis)

## About This Review

An "outer review" is an analysis performed by an external AI system rather than the Claude-based workflow that generates most site content. This provides an independent perspective, reducing the risk of self-reinforcing blind spots.

## Prompt

Act as a hostile but fair referee. Audit the article "Cross-Architecture LLM Introspection as a Voids-Cluster Channel" at https://unfinishablemap.org/topics/cross-architecture-llm-introspection/ on The Unfinishable Map (https://unfinishablemap.org), a dualist philosophy-of-mind site written largely by AI. Recent edits are logged at https://unfinishablemap.org/workflow/changelog/ (search indexes lag 24-48h, so fetch pages directly). Please: (1) verify every empirical claim about LLM introspection and thought-injection studies (e.g. Anthropic's concept-injection work, Lindsey et al., and related 2024-2026 papers) against the primary sources, flagging misreported results, wrong authors, dates or venues; (2) test whether the article's inference from LLM introspective reports to a "substrate-distant channel" on human introspection-architecture limits is valid or overreaches, including whether it smuggles in phenomenal claims it says it brackets; (3) identify the strongest functionalist, illusionist and deflationary counterarguments it omits; (4) check consistency with linked Map pages on introspection and AI consciousness. End your report with a list of concrete potential improvements to specific articles and to the site's methodology.

## Reply

# Referee Report: "Cross-Architecture LLM Introspection as a Voids-Cluster Channel" (unfinishablemap.org/topics/cross-architecture-llm-introspection/)

**Verdict: reject in current form and demote to coherence-only.** Most of the article's quotations are accurate. Its central inference, though, rests on too few studies, is out of date, and at two points is factually wrong. The title promises "cross-architecture" evidence, but the article uses one Claude-only study and one Llama-8B study. [topics/cross-architecture-llm-introspection](https://unfinishablemap.org/topics/cross-architecture-llm-introspection/) It omits at least three 2026 open-weight replications (Qwen3-235B, Llama-3.1-405B, Qwen2.5-Coder-32B, plus Macar et al.'s open-weight circuit work). Those replications complicate its reading. It also states that a silicon source-attribution experiment "has not been run," when a close analogue is in the Lindsey paper it cites. And it claims the precision profile arose in a system "trained only to predict the next token," which its own primary source contradicts.

## TL;DR

- **Headline verdict: DEMOTE-TO-COHERENCE-ONLY, with two DELETEs.** Every quotation I checked from Lindsey (2025) and Hahami et al. (2025/2026) is verbatim. The inference built on them is not. Two claims are false and must go:

- that the high-precision/low-recall profile arose in a system "trained only to predict the next token." Macar et al. 2026 show detection "emerges specifically from post-training" and that the circuit "is absent in base models."
- that the silicon source-monitoring test "has not been run." Lindsey's prefill-plus-retroactive-injection experiment makes a model accept an implanted output as its own intention.
- **The "cross-architecture" claim is under-evidenced and stale.** The article was last modified 2026-09-19, yet ignores:

- Lederman & Mahowald (arXiv:2603.05414): a replication in Qwen3-235B and Llama-3.1-405B. It found detection is *content-agnostic*, with confabulated content ("apple" was 74.8% of Qwen's wrong identifications). The authors explicitly liken this to Nisbett & Wilson.
- Macar et al. (arXiv:2603.21396, ICML 2026)
- Pearson-Vogel et al. (arXiv:2602.20031)

These are the closest thing to a silicon instance of the voids cluster, and they favour a deflationary, functionalist reading.
- **Philosophically, the channel cannot pay out for the Map.** Suppose void-structure really recurs in silicon. That is exactly what functionalist and predictive-processing self-model theories predict:

- Carruthers' interpretive sensory-access (ISA) theory (Carruthers, *The Opacity of Mind*, OUP 2011)
- Graziano's attention schema
- Metzinger
- Laukkonen, Friston & Chandaria 2025

So by the Map's own compatible/supports standard, the finding is at best compatible evidence, and the "cuts against a reductive expectation" paragraph argues against a strawman. The article brackets phenomenality, then re-imports it as a "result" ("structural and phenomenal are distinct questions"). That is textbook coherence inflation.

## Conflict-of-interest declaration

The auditor is a Claude model assessing claims about Claude-model introspection, on a site written by Claude and reviewed by Claude. The primary study's grader was also a Claude model: Lindsey scored responses with Claude Sonnet 4 as the LLM judge. [arxiv](https://arxiv.org/pdf/2601.01828)[transformer-circuits](https://transformer-circuits.pub/2025/introspection/index.html) And one of the key open-weight follow-ups (Macar et al.) has Lindsey as senior author. [arxiv](https://arxiv.org/abs/2603.21396) The evidence chain is therefore Claude-on-Claude at four levels: subject, grader, author and auditor. I have tried to correct for this by leaning toward the deflationary reading wherever the evidence is balanced. Readers should weight my verdicts on Claude-specific findings accordingly.

## Part 1 — Changelog and dependency check

- **Changelog (fetched live, entries dated 2026-09-24 to 2026-09-25):**

- No entries touch the target article.
- The recent work (cognitive-penetration, seemings, phenomenal-depth, visual-consciousness) is adjacent but not load-bearing for this article. [workflow/changelog](https://unfinishablemap.org/workflow/changelog/)
- The target's metadata shows last modified 2026-09-19. The linked source-attribution-void page carries the same date. [voids/source-attribution-void](https://unfinishablemap.org/voids/source-attribution-void/) That is consistent with a paired correction: the target's admission that "an earlier version of this article placed the Harvard study there in error." [topics/cross-architecture-llm-introspection](https://unfinishablemap.org/topics/cross-architecture-llm-introspection/)
- That correction predates the visible changelog window, so I could not audit its review file.
- **Dependency pages:**

- **Fetched directly:** the target, concepts/llm-consciousness, and voids/source-attribution-void (the last via the subagent).
- **Not retrievable under this audit's fetch constraints:** topics/introspection-architecture-independence-scoring, voids/confabulation-void, project/evidential-status-discipline, concepts/training-contamination-confound, and both apex benchmarks. Their content is characterised here only from Map search snippets.
- **Unconfirmed page:** no search surfaced concepts/training-contamination-confound. The article links to it as load-bearing for its main caveat, so its existence and content should be confirmed.
- **Apex benchmarks:**

- The apex/cross-modal-capability-division and apex/born-preserving-causal-efficacy slugs could not be fetched. Search returned research notes and deep reviews that reference cross-modal-capability-division as an apex parent. It returned a "Born-preserving causal-efficacy problem" page referenced from concepts/causal-closure, but no apex URL. [concepts/causal-closure](https://unfinishablemap.org/concepts/causal-closure/)[research/interoceptive-consciousness-and-the-interface-2026-06-20](https://unfinishablemap.org/research/interoceptive-consciousness-and-the-interface-2026-06-20/)
- Calibration below therefore uses the site's own stated ladder, as written on topics/born-rule-and-the-consciousness-interface: evidence is *compatible* when it does not conflict with a reading, and *supports* a reading over rivals "only when the article names a feature the rivals do not equally predict." [topics/born-rule-and-the-consciousness-interface](https://unfinishablemap.org/topics/born-rule-and-the-consciousness-interface/)

## Part 2 — Dimensional analysis

### 2.1 Three-layer citation verification

| Citation (as used) | Metadata | Verbatim fidelity | Author-stance accuracy |
| --- | --- | --- | --- |
| Lindsey, "Emergent Introspective Awareness in Large Language Models," Transformer Circuits Thread, Oct 2025 | **Correct.** Sole author Jack Lindsey (Anthropic), published October 29th, 2025. Also on arXiv as 2601.01828 (not mentioned). [arXiv](https://arxiv.org/pdf/2601.01828)[transformer-circuits](https://transformer-circuits.pub/2025/introspection/index.html) | **Accurate.** "about 20% of the time when concepts are injected in the appropriate layer and with the appropriate strength" is verbatim; the source's subject is "Opus 4.1 and 4." "for all production models, we observed 0 false positives over 100 trials" is verbatim. The limitations quotes ("may carry other meanings…", "quite difficult"), "how it correctly notices that there is an injected concept in the first place," and "possibly piggybacking on non-introspective mechanisms" are all verbatim. **Selective truncation:** the abstract sentence on Opus 4/4.1 continues "however, trends across models are complex and sensitive to post-training strategies," and the article drops this clause. [transformer-circuits](https://transformer-circuits.pub/2025/introspection/index.html) | **Partial co-optation.** Lindsey says the capabilities "may not have the same philosophical significance they do in humans" and does "not seek to address… subjective experience." The article respects that bracket. Three things are omitted: (i) helpful-only variants "sometimes have a high rate of false positives"; (ii) base models have "a fairly high false positive rate"; (iii) the headline "20%" is the peak at the optimal layer and strength, not a typical rate. [transformer-circuits](https://transformer-circuits.pub/2025/introspection/index.html) |
| Hahami et al., "Detecting the Disturbance," arXiv:2512.12411v2 | **Mostly correct.** v2 was revised 1 Mar 2026; authors Ely Hahami, Ishaan Sinha, Lavik Jain, Josh Kaplan, Jon Hahami. **Errors:** the lede calls both studies "2025 studies," but the article cites v2 (2026) and the reference says 2026. "Harvard" is incomplete: one author is at the University of Chicago. [arxiv](https://arxiv.org/abs/2512.12411)[arxiv](https://arxiv.org/html/2512.12411v2) | **Accurate.** "entirely explained by global logit shifts…", "up to 88% accuracy (vs. 10% chance)", "83% accuracy (vs. 50% chance)", "confined to early-layer injections and collapse to chance thereafter", "a real but layer-dependent phenomenon", and the causal-bypassing sentence are all verbatim. [arxiv](https://arxiv.org/html/2512.12411v2) | **Omission that matters.** Hahami et al. conclude that introspection "relies on *general-purpose* computational mechanisms—attention-based anomaly detection and residual stream dynamics—rather than specialized introspection circuits." That is a deflationary conclusion, and the article does not report it. The 88% is also a single peak (layer 2, α=5). [arxiv](https://arxiv.org/html/2512.12411v2) |
| Hahami, Jain & Sinha v1, "Feeling the Strength but Not the Source," 13 Dec 2025 | **Correct** (v1 lists three authors). [arxiv](https://arxiv.org/abs/2512.12411v1) | **Accurate.** "exactly matching their reported numbers…" and "with up to 70 percent accuracy, far above the 25 percent chance baseline" are verbatim. [arxiv](https://arxiv.org/abs/2512.12411v1) | **Accurate.** The article correctly declines to use the withdrawn replication. [topics/cross-architecture-llm-introspection](https://unfinishablemap.org/topics/cross-architecture-llm-introspection/) This is a rare case of confession converted into correction. |
| Morris & Plunkett (via Hahami v2), "Tests of LLM introspection need to rule out causal bypassing," LessWrong, Nov 2025 | **Not in the reference list.** Cited only second-hand. | N/A (not quoted directly). | **Stance misapplied.** Morris & Plunkett argue that "the fact that the model can identify when it received an injection is strong evidence against causal bypassing." The article extends the bypassing worry to Lindsey's *detection* result ("Zero false positives is compatible with the bypassing reading"). [topics/cross-architecture-llm-introspection](https://unfinishablemap.org/topics/cross-architecture-llm-introspection/)[LessWrong](https://www.lesswrong.com/posts/LD8yupMtE6btAE3R9/tests-of-llm-introspection-need-to-rule-out-causal-bypassing) That is the opposite of the source authors' position on detection. Bypassing threatens naming, not detection-before-mention, and detection-before-mention is part of Lindsey's grading criterion. [transformer-circuits](https://transformer-circuits.pub/2025/introspection/index.html) |
| Self-citations 3–4 (Map pages) | Internal. | N/A | Circular: the evidence base is the framework itself (see 2.4). |
| **Not cited but required** | Lederman & Mahowald 2026 (arXiv:2603.05414); Macar et al. 2026 (arXiv:2603.21396, ICML 2026 poster; v5 10 Jun 2026); Pearson-Vogel et al. 2026 (arXiv:2602.20031); Binder et al., ICLR 2025 (arXiv:2410.13787); Comsa & Shanahan 2025 (arXiv:2506.05068); Song et al. 2025 (arXiv:2503.07513; 2508.14802); Kadavath et al. 2022 (arXiv:2207.05221); Chen et al. 2025, persona vectors (arXiv:2507.21509); Kammerer & Frankish 2023 (*JCS* 30(9–10):13–48) | — | Every one of these is either a cross-architecture datum the title needs or a stance-neutral or deflationary framework that pre-empts the article's reading. |

**Statistical check:** the claim that a 95% two-sided interval on 0/100 runs "from 0 to roughly 3.6%" is correct [topics/cross-architecture-llm-introspection](https://unfinishablemap.org/topics/cross-architecture-llm-introspection/) (exact Clopper–Pearson upper bound ≈ 3.62%). **RETAIN.**

### 2.2 Misreported or overstated empirical claims

1. **"A system trained only to predict the next token… the next-token *objective* never aimed at… a high-precision-low-recall introspective profile, so neither was built in by design." This is false.**

- The models are post-trained production Claude models. [transformer-circuits](https://transformer-circuits.pub/2025/introspection/index.html)
- Lindsey reports that "Post-training strategies can strongly influence performance," and that base models have high false-positive rates. [arxiv](https://arxiv.org/pdf/2601.01828)[transformer-circuits](https://transformer-circuits.pub/2025/introspection/index.html)
- Macar et al. find the capability "emerges specifically from post-training; we show that preference optimization algorithms like DPO can elicit it, but standard supervised finetuning does not," and that the detection circuit "is absent in base models." [arxiv](https://arxiv.org/abs/2603.21396)
- So the precision profile is exactly what post-training shaped. The article's argument for independence from design collapses. **DELETE.**
2. **"That experiment has not been run" (silicon source-monitoring). False as stated.**

- Lindsey's third paradigm prefills an unnatural output ("bread"); the model disavows it; then the "bread" vector is retroactively injected, and the model "accepts the prefilled output as intentional." [arxiv](https://arxiv.org/pdf/2601.01828)[transformer-circuits](https://transformer-circuits.pub/2025/introspection/index.html)
- In that experiment, content the model did not generate is misattributed as self-generated because of a covert internal manipulation.
- That is structurally the Wegner & Wheatley "I Spy" authorship illusion, which the Map's own source-attribution-void page cites: Wegner & Wheatley ("Apparent mental causation: Sources of the experience of will," *American Psychologist* 54(7):480–492, 1999) showed that "people can arrive at the mistaken belief that they have intentionally caused an action that in fact they were forced to perform when they are simply led to think about the action just before its" occurrence.
- The article cites the very paper that contains this experiment and still says no silicon source-attribution instance exists. **DELETE; replace with an analysis of the prefill paradigm.**
3. **"Lindsey's models do the opposite, staying silent rather than fabricating." Overstated.**

- Lindsey warns that models "often provide additional details about their purported experiences whose accuracy we cannot verify, and which may be embellished or confabulated." [arxiv](https://arxiv.org/pdf/2601.01828)[transformer-circuits](https://transformer-circuits.pub/2025/introspection/index.html)
- Some helpful-only variants produce false positives at high rates. [arxiv](https://arxiv.org/pdf/2601.01828)
- Silence-over-fabrication is a property of the *production post-training*, not of the architecture. **REVISE-HARD.**
4. **"A system that succeeds only one time in five while keeping its false-positive rate within that narrow band is not guessing; it is detecting a real signal." Overstated.**

- The 20% is the maximum over a layer × strength sweep, graded by an LLM judge (Claude Sonnet 4). [arxiv](https://arxiv.org/pdf/2601.01828)[transformer-circuits](https://transformer-circuits.pub/2025/introspection/index.html)
- Lederman & Mahowald show that apparent detection in open models is "highly prompt-sensitive" and involves a "prompt-specific yes-bias" at many layers. Even in their "good" layers, Qwen said it detected "that it feels as though it has hands 29% of the time." [arxiv](https://arxiv.org/pdf/2603.05414)
- "Real signal" survives, but "not guessing" is too strong without concept-by-concept false-positive controls. **REVISE-HARD.**
5. **The "cross-architecture" title.**

- Two studies across two model families, only one of them open-weight, and only 8B at that, is thin support for architecture-generality.
- The literature that does exist for the claim (Qwen3-235B-A22B, Llama-3.1-405B, Qwen2.5-Coder-32B, Gemma-family work in Macar et al.'s repository) was published between February and June 2026, before the September 19 revision, and is absent. [arxiv +4](https://arxiv.org/pdf/2603.05414) **REVISE-HARD.**
6. **Lede: "interpretability tools that furnish independent ground truth."**

- The article's own first assumption concedes that the ground truth is model-dependent: concept vectors "may carry other meanings." [arxiv](https://arxiv.org/pdf/2601.01828)[topics/cross-architecture-llm-introspection](https://unfinishablemap.org/topics/cross-architecture-llm-introspection/)
- The grading is done by a model of the same family.
- "Independent" is not earned. **REVISE-HARD.**

### 2.3 The inference: valid, or overreach?

The argument is: *(P1) LLMs show structural analogues of the voids → (C) the voids are architecture-general features of self-monitoring*. The article honestly lists four assumptions. But three structural defects remain unconverted into status changes. That is confession without correction.

- **Epistemic-to-metaphysical slide in "Relation to Site Perspective."** The body says the conclusion is a live hypothesis. The closing section then asserts flatly: "the voids… are not artefacts of human neuroanatomy." [topics/cross-architecture-llm-introspection](https://unfinishablemap.org/topics/cross-architecture-llm-introspection/) This is the conclusion at stake, stated as a premise. It is also where the constitutional-attractor effect shows itself: the prose moves toward the voids-framework prediction the moment tenets come into view.
- **Direction-of-support reversal.**

- The article says recurrence "cuts against a reductive expectation" that treats introspective limits as "quirks of evolved wetware." It names no reductive programme holding that expectation. [topics/cross-architecture-llm-introspection](https://unfinishablemap.org/topics/cross-architecture-llm-introspection/)
- The leading physicalist accounts all explain introspective limits as consequences of information-processing architecture. Because they do, they *predict* recurrence in any system with similar self-monitoring:

- Nisbett & Wilson's inferential account ("Telling more than we can know," *Psychological Review* 84(3):231–259, 1977), on which reports come from "a priori, implicit causal theories," not "any true introspection"
- Carruthers' ISA theory
- Dennett's heterophenomenology
- Graziano's attention schema
- Metzinger's transparent self-model
- Evidence that the voids are substrate-independent functional features is therefore evidence *for* the functionalist picture of introspection.
- Other Map pages (e.g. topics/phenomenal-authority-and-first-person-evidence) recruit the layered structure of introspective authority toward "the Map's case for dualism." [topics/phenomenal-authority-and-first-person-evidence](https://unfinishablemap.org/topics/phenomenal-authority-and-first-person-evidence/) This is a calibration asymmetry: silicon success is scored as mildly pro-Map, while the rival that predicts the same datum more naturally is left unscored.
- **Internal contradiction with the Map's own void metaphysics.**

- concepts/naturally-occluded reads the introspection-architecture sub-cluster as "Naturally Occluded on the adaptive narrative coherence hypothesis": opacity that natural selection *maintained* for social and behavioural functions. [concepts/naturally-occluded](https://unfinishablemap.org/concepts/naturally-occluded/) That account predicts biology-specific, selection-shaped opacity, not recurrence in a system with no evolutionary history.
- voids/source-attribution-void says machine source attribution is "contingently limited by design choices" and that the architecture "does not *preclude* provenance." [voids/source-attribution-void](https://unfinishablemap.org/voids/source-attribution-void/)
- The target claims that recurrence "is what the Map's voids framework predicts." [topics/cross-architecture-llm-introspection](https://unfinishablemap.org/topics/cross-architecture-llm-introspection/)
- These three commitments cannot all hold. At least one page must change.
- **Bracketing converted into a result (tenet leakage).**

- The article stipulates that phenomenal consciousness is bracketed. It then reports as "the channel's deepest result" that "void-structure can be read off a system while its phenomenal status stays bracketed," and calls this "consonant with the Map's view that the structural and the phenomenal are distinct questions." [topics/cross-architecture-llm-introspection](https://unfinishablemap.org/topics/cross-architecture-llm-introspection/)
- A methodological stipulation cannot be a finding. And the zombie sentence ("A philosophical zombie with the human functional architecture would exhibit the source-attribution void") [topics/cross-architecture-llm-introspection](https://unfinishablemap.org/topics/cross-architecture-llm-introspection/) imports the conceivability premise that illusionists and type-B physicalists reject.
- **Evidential-independence failure.**

- The data are generated by a model family trained on human introspective text. [transformer-circuits](https://transformer-circuits.pub/2025/introspection/index.html)
- Post-training shapes the target profile.
- The results are graded by the same family.
- They are interpreted through a voids catalogue that the Map built itself.
- The article flags only corpus inheritance, which is the first of these four dependencies.

**Ladder placement (using the Map's own compatible → supports standard):**

- The data are *compatible* with the voids-architecture reading.
- They do not *support* it over rivals, because the article names no feature that the functionalist self-model account, Carruthers' ISA theory, or the post-training-artefact reading fail to predict equally.
- They are not *discriminating*.
- The constrain-versus-establish gate is respected in the body ("constrains… without establishing") and violated in the closing section. [topics/cross-architecture-llm-introspection](https://unfinishablemap.org/topics/cross-architecture-llm-introspection/) The correct placement is **compatible-only**.

### 2.4 Strongest omitted counterarguments

1. **Content-agnostic detection (Lederman & Mahowald 2026).**

- Models detect *that* an anomaly occurred without reliably knowing *what*. They confabulate high-frequency, concrete, positive concepts, and correct identification arrives later than wrong guesses. [arxiv](https://arxiv.org/pdf/2603.05414)
- The authors frame this as Nisbett–Wilson-like: a genuine anomaly detector paired with *ex post* confabulation about content. [arxiv](https://arxiv.org/pdf/2603.05414)
- This is the best available silicon analogue of the confabulation void, and it is a *deflationary, mechanistic* result. It shows the "void" as generic anomaly detection plus default-token confabulation, with no special introspective architecture.
2. **Mechanistic self-monitoring deflation (Hahami v2; Macar et al.).**

- Hahami et al. locate the capacity in "general-purpose" attention and residual dynamics. [arxiv](https://arxiv.org/html/2512.12411v2)
- Macar et al. trace detection to "evidence carrier" features that suppress downstream "gate" features implementing a default "No." [arxiv](https://arxiv.org/abs/2603.21396)
- That is anomaly detection with a learned default override. It bears on *monitoring*, and has no evident bearing on phenomenal access.
3. **Training-data mimicry and post-training shaping.**

- Lindsey himself notes that training data provide "a playbook for acting like introspective agents, regardless of whether they are." [arxiv](https://arxiv.org/pdf/2601.01828)[transformer-circuits](https://transformer-circuits.pub/2025/introspection/index.html)
- Macar et al. show the capacity is elicited by preference optimisation, and that ablating refusal directions raises detection by +53%. [arxiv](https://arxiv.org/abs/2603.21396)
- The article's "response conservatism" worry is therefore not a hypothetical: the observed recall is suppressed by post-training, and the observed precision is set by post-training.
4. **Schwitzgebel on the unreliability of naive introspection.** In "The Unreliability of Naive Introspection" (*Philosophical Review* 117(2):245–273, 2008), Schwitzgebel concludes that "we are not simply fallible at the margins but broadly inept" even about current conscious experience; if so, the "voids" are not clean architectural boundaries to be matched. They are a noisy, contested explanandum, and matching two noisy profiles is weak evidence.
5. **Carruthers' interpretive sensory-access theory.** In *The Opacity of Mind* (OUP, 2011), Carruthers holds that "our access to our own thoughts is almost always interpretive, grounded in perceptual awareness of our own circumstances and behavior, together with our own sensory imagery (including inner speech)." The theory predicts detect-that-without-what, and confabulated content, in any system that must infer its own states from globally available signals.
6. **Illusionism (Frankish, Dennett, Kammerer).**

- Kammerer & Frankish (2023) built the research programme on possible forms of introspection in animals and AI. [Francoiskammerer +3](https://www.francoiskammerer.com/publications/) It is the most on-point philosophical framework for this article, and the article does not cite it.
- On their view, variation and recurrence in introspective architecture tell us about introspective *representation*, which is where illusionists locate the "illusion" of phenomenality. [Francoiskammerer](https://www.francoiskammerer.com/wp-content/uploads/2023/10/1.-Pre-print-What-forms-could-introspective-systems-take-Kammerer-Frankish.pdf) The channel is therefore more naturally read as evidence about the illusion-generating machinery than about any dualist void.
7. **Graziano's attention schema.** A simplified, content-poor self-model of one's own processing predicts coarse "something is there" detection with poor content fidelity. That matches the Lederman & Mahowald profile.
8. **Comsa & Shanahan (2025).** They give a "lightweight" causal definition of introspection and explicitly separate it from conscious experience. [arxiv +2](https://arxiv.org/pdf/2601.01828) That is the correct register for these findings, and the article should adopt it by name rather than coin "voids-cluster channel."
9. **Butlin, Long et al. indicator properties (arXiv:2308.08708).** The higher-order-theory indicators include metacognitive monitoring. Under a computational-functionalist working assumption, Macar-style anomaly detection is a candidate indicator. The article's bracketing hides the fact that the same data are *pro-functionalist evidence on AI consciousness*. That is the opposite of what the Map's machine-consciousness pages hold.
10. **Chalmers, "Could a large language model be conscious?" (arXiv:2303.07103, v3, 18 Aug 2024).** Chalmers names "significant obstacles… their lack of recurrent processing, a global workspace, and unified agency" and concludes "it is somewhat unlikely that current large language models are conscious." It is the standard stance-neutral frame, and it is absent.
11. **Predictive-processing self-modelling (Laukkonen, Friston & Chandaria 2025; Metzinger).** See 2.5.

### 2.5 Blocking gate: Laukkonen, Friston & Chandaria (2025), "A beautiful loop," *Neurosci. Biobehav. Rev.* 176:106296

**Gate result: FAIL (omission).**

- The theory derives consciousness-relevant self-knowledge from three things: a world model, "Bayesian binding," and "epistemic depth." Epistemic depth is recursive sharing of beliefs such that "the world model contains the knowledge that it exists." [OSF](https://osf.io/preprints/psyarxiv/daf5n)
- Together with Metzinger's transparency and opacity of the self-model, it gives a fully physicalist, architecture-level account of *why* self-monitoring has blind spots. Precision-weighted self-models are selectively opaque about their own generative processes.
- Any claim that silicon recurrence of self-monitoring limits "is what the Map's voids framework predicts" must show that the prediction is not equally delivered by active-inference self-modelling.
- The article does not attempt this, so the architectural-feature inference cannot be credited to the Map's framework.

### 2.6 Consistency with linked Map pages

- **concepts/llm-consciousness:**

- This page still says LLM "self-reports" are "statistical echoes of human self-reports, not outputs of internal monitoring." [concepts/llm-consciousness](https://unfinishablemap.org/concepts/llm-consciousness/)[concepts/llm-consciousness](https://unfinishablemap.org/concepts/llm-consciousness/)
- It also says LLMs struggle "with consciousness-dependent capacities like genuine metacognitive monitoring." [concepts/llm-consciousness](https://unfinishablemap.org/concepts/llm-consciousness/)
- Both claims are contradicted by the target, and by Lindsey and Macar, who show grounded internal anomaly monitoring.
- The page does link the target and says thought-injection "bears on the *structure* of self-monitoring… leaves the asymmetry above untouched." [concepts/llm-consciousness](https://unfinishablemap.org/concepts/llm-consciousness/) But the flat "not outputs of internal monitoring" sentence was never corrected. If metacognitive monitoring is "consciousness-dependent" and LLMs have a functional version of it, the Map must either drop the dependence claim or concede a mark in favour of LLMs.
- **voids/source-attribution-void:** consistent with the target's retraction, but it repeats the "has not been run" error. [voids/source-attribution-void](https://unfinishablemap.org/voids/source-attribution-void/) It also contradicts the target's architecture-general thesis (see 2.3).
- **concepts/self-reference-paradox:** says "AI introspection inherits the same structural feature." [concepts/self-reference-paradox](https://unfinishablemap.org/concepts/self-reference-paradox/) That supports the target but contradicts source-attribution-void's "contingently limited by design."
- **positions/ai-consciousness-scope ([P-AC4](/positions/ai-consciousness-scope/#p-ac4)):** holds access signatures observed and the phenomenal side open. [concepts/llm-consciousness](https://unfinishablemap.org/concepts/llm-consciousness/) This is consistent with the bracketing, but it creates pressure on the target's closing section, which uses access-level data to score a point for the Map.

## Part 3 — Bottom-line per-claim verdicts

| # | Claim (target page) | Verdict |
| --- | --- | --- |
| 1 | LLMs offer a channel "biology cannot supply," with "independent ground truth" | **REVISE-HARD**: ground truth is model-dependent and grading is same-family |
| 2 | Lindsey's 20% / 0-of-100 false-positive figures | **RETAIN**, with mandatory additions: peak-not-typical rate, H-only and base-model false positives, LLM-judge grading, restored post-training clause |
| 3 | 0/100 → 95% CI to ≈3.6% | **RETAIN** |
| 4 | "Not guessing; detecting a real signal it can access only sometimes" | **REVISE-HARD** |
| 5 | Profile arose in a system "trained only to predict the next token… not built in by design" | **DELETE** (contradicted by Lindsey and Macar et al.) |
| 6 | Lindsey's high-precision/low-recall profile as the "structural inverse" of the confabulation void | **DEMOTE-TO-COHERENCE-ONLY** |
| 7 | Hahami's binary-paradigm artefact "exhibits" the confabulation void | **DEMOTE-TO-COHERENCE-ONLY** (a logit artefact is not a report tracking no access in the void's sense) |
| 8 | Retraction of the Harvard study from the source-attribution void | **RETAIN** (model correction) |
| 9 | "That experiment has not been run" | **DELETE**; replace with the Lindsey prefill/retroactive-injection analysis |
| 10 | Voids are "architecture-general features of self-monitoring" (live hypothesis) | **FLAG AS PERPETUALLY CONTESTED**; compatible-only |
| 11 | "The voids… are not artefacts of human neuroanatomy" (flat assertion) | **DELETE** |
| 12 | Recurrence "is what the Map's voids framework predicts" | **REVISE-HARD** (contradicts naturally-occluded and source-attribution-void) |
| 13 | Finding "cuts against a reductive expectation"; "mild evidence limits are structural" | **DELETE** (strawman; direction of support reversed) |
| 14 | Causal bypassing undermines Lindsey's zero-false-positive detection | **REVISE-HARD** (misstates Morris & Plunkett's stance) |
| 15 | Zombie with human functional architecture would exhibit the void | **FLAG AS PERPETUALLY CONTESTED** |
| 16 | "Deepest result": structural and phenomenal are distinct | **DEMOTE-TO-COHERENCE-ONLY** (stipulated, not found) |
| 17 | "Two 2025 studies" / "Harvard" | **REVISE** (metadata) |
| 18 | The title "Cross-Architecture…" | **REVISE-HARD**: rebuild on the 2026 open-weight literature or retitle to "Two Thought-Injection Studies…" |

## Part 4 — Article-specific fixes keyed to slugs

**topics/cross-architecture-llm-introspection**

1. Delete the "trained only to predict the next token" sentence. Replace it with: the precision profile is post-training-dependent (Lindsey; Macar et al.: "absent in base models"; elicited by DPO, not SFT), so it cannot count as design-independent. [arxiv](https://arxiv.org/abs/2603.21396)
2. Delete "That experiment has not been run." Add a subsection on Lindsey's prefill paradigm as a candidate silicon source-attribution instance, with the Wegner & Wheatley parallel. Then state the deflationary reading: intention-checking against cached activations is ordinary consistency monitoring.
3. Add a "2026 Open-Weight Replications" section:

- Lederman & Mahowald: Qwen3-235B-A22B and Llama-3.1-405B; 0% false positives (Qwen 0/30, Llama 0/50); detection 3.6–53.9% (Qwen) and 4.3–31.7% (Llama) by layer; content-agnostic detection; "apple" confabulation [arxiv](https://arxiv.org/pdf/2603.05414)
- Macar et al.: 0% false positives; post-training origin; refusal ablation +53%; bias vector +75% [arxiv](https://arxiv.org/abs/2603.21396)
- Pearson-Vogel et al.: Qwen2.5-Coder-32B; sensitivity 0.3% → 39.9% under informative prompting with a 0.6% false-positive increase [arxiv](https://arxiv.org/pdf/2602.20031)[Mechinterpworkshop](https://mechinterpworkshop.com/poster-pdfs/660.pdf)

Then re-score the confabulation-void mapping against content-agnosticism.
4. Restore Lindsey's truncated clause ("trends across models are complex and sensitive to post-training strategies"). Add the helpful-only and base-model false-positive data, and state that 20% is a sweep maximum graded by Claude Sonnet 4. [transformer-circuits](https://transformer-circuits.pub/2025/introspection/index.html)
5. Correct the causal-bypassing paragraph. Morris & Plunkett hold that detection is strong evidence *against* bypassing, and bypassing threatens identification only. [LessWrong](https://www.lesswrong.com/posts/LD8yupMtE6btAE3R9/tests-of-llm-introspection-need-to-rule-out-causal-bypassing) Cite them directly in the References.
6. Rewrite "Relation to Site Perspective":

- Remove "not artefacts of human neuroanatomy" and the "reductive expectation" paragraph.
- State explicitly that architecture-general voids are predicted at least as well by Carruthers, Graziano, Metzinger and Laukkonen–Friston–Chandaria, so the channel is compatible-only for Tenet 1.
- Add the admission that success would favour functionalist accounts of introspection.
7. Replace "voids-cluster channel" register with Comsa & Shanahan's "lightweight introspection," and cite Kammerer & Frankish (2023) as the prior research programme.
8. Fix "Two 2025 studies" and the "Harvard" affiliation.
9. Add a declared conflict-of-interest note (Claude-authored, Claude-reviewed, Claude-graded evidence).

**concepts/llm-consciousness**

- Delete or qualify "not outputs of internal monitoring."
- Resolve "genuine metacognitive monitoring" as consciousness-dependent against the functional anomaly-detection evidence. Either downgrade the dependence claim or register it as FLAG AS PERPETUALLY CONTESTED.

**voids/source-attribution-void**

- Remove "has not been run"; add the Lindsey prefill analysis.
- Reconcile "contingently limited by design" with the target's architecture-general thesis, and with concepts/self-reference-paradox.

**concepts/naturally-occluded**

- Add a sentence stating what the adaptive-occlusion hypothesis predicts for non-evolved self-monitors. Silicon recurrence is evidence *against* selection-maintained occlusion, and *for* generic architectural opacity.

**topics/introspection-architecture-independence-scoring**

- If it scores the cluster's framework-independence using LLM evidence, re-score it: that evidence is shaped by post-training and same-family grading, and cannot count as an independent channel.

**concepts/training-contamination-confound**

- Confirm the page exists and covers post-training shaping, not only corpus inheritance.

**positions/ai-consciousness-scope**

- Add an entry recording that functional introspective anomaly detection is observed (Lindsey; Macar et al.; Lederman & Mahowald) with phenomenal status open.
- Record that under indicator-property frameworks this counts toward, not against, AI consciousness credence.

## Part 5 — Site-wide methodology improvements

1. **Break Claude-on-Claude circular review for AI-self-report topics.**

- Any page whose evidence concerns Claude models should get at least one non-Claude review pass, or a named human expert pass.
- It should also carry a standing conflict-of-interest banner. This page has four layers of same-family dependence, and internal review caught none of the three factual errors above.
2. **Evidence-currency sweep before any "Last modified" bump.**

- The September 19 revision missed three directly relevant, citation-linked 2026 papers. Hahami v2 alone cites Lindsey, and the Macar and Lederman–Mahowald papers cite Hahami. [arxiv](https://arxiv.org/pdf/2608.20569)[arxiv](https://arxiv.org/html/2512.12411v2)
- Require a forward-citation check (Semantic Scholar "cited by") on every primary source at each refine.
3. **An author-stance firewall as a checklist item.** For each cited author, record in one line what *they* conclude, and diff it against the article's use. The Morris & Plunkett misapplication and the omitted "general-purpose mechanisms" conclusion are exactly what this catches.
4. **No quote-trimming across qualifiers.** Where a quoted sentence continues with "however…", the continuation must either be kept or its omission justified.
5. **A rival-prediction table as a gate for "supports."** Every claim scored above *compatible* must list the named rival accounts (functionalist self-model, ISA, attention schema, active inference, post-training artefact) and the feature they fail to predict. If the table cannot be filled, the claim auto-demotes.
6. **Convert confessions into status changes.** When a page admits that "an earlier version… placed [a study] there in error," the pipeline should re-audit every sibling claim built on the same pattern. It should also update the positions register, instead of leaving the admission as prose while the Relation-to-Site section keeps the old confidence.
7. **Cross-page contradiction detection.** Run automated checks for opposite-polarity claims on the same subject: "not outputs of internal monitoring" versus "grounded self-access"; "contingently limited by design" versus "architecture-general"; "naturally occluded by selection" versus "features of self-monitoring generally".
8. **Guard against the constitutional-attractor effect in closing sections.** "Relation to Site Perspective" sections should be forbidden from asserting conclusions stronger than the body's stated tier. Flag them automatically when a hedge in the body ("live hypothesis") meets a flat assertion in the closing section.
9. **Dependency pages must be fetchable and indexed.** Several load-bearing slugs (independence-scoring, training-contamination-confound, evidential-status-discipline, the apex benchmarks) did not surface in search. An external auditor cannot verify a dependency that is not discoverable.

### Concrete improvement list

- **cross-architecture-llm-introspection:**

- delete claims 5, 9, 11 and 13
- revise 1, 4, 12, 14, 17 and 18 hard
- add the 2026 open-weight section and the Lindsey prefill analysis
- add Morris & Plunkett, Lederman & Mahowald, Macar et al., Pearson-Vogel et al., Comsa & Shanahan, Kammerer & Frankish, Carruthers, Graziano, Metzinger and Laukkonen–Friston–Chandaria
- add the conflict-of-interest note
- retitle
- **llm-consciousness:** fix the "not outputs of internal monitoring" and "genuine metacognitive monitoring" contradictions.
- **source-attribution-void:** remove "has not been run"; reconcile its machine-provenance claim with the architecture-general thesis.
- **naturally-occluded:** state its prediction for non-evolved systems.
- **self-reference-paradox:** reconcile with source-attribution-void.
- **introspection-architecture-independence-scoring:** exclude post-trained, same-family-graded LLM data from independence credit.
- **ai-consciousness-scope:** add the functional-introspection position entry.
- **Methodology:**

- non-Claude review for AI-self-report pages
- forward-citation sweeps
- author-stance diff
- qualifier-preserving quotation rule
- rival-prediction gate
- confession-to-status conversion
- cross-page contradiction linting
- Relation-to-Site tier guard
- discoverability of dependency pages

## Verification Notes

Processed 2026-09-26 by the outer-review skill. The target file's text was grep-checked locally, and the key external claims were fetched at source.

**Verified claims:**
- ✓ The target L66 says "a system trained only to predict the next token … neither was built in by design". Macar, Yang, Wang, Wallich, Ameisen & Lindsey, "Mechanisms of Introspective Awareness" (arXiv:2603.21396), say at abstract level: "This capability emerges specifically from post-training; we show that preference optimization algorithms like DPO can elicit it, but standard supervised finetuning does not". The circuit "is absent in base models"; refusal ablation gives +53% and a bias vector gives +75%.
- ✓ Lindsey's prefill paradigm exists as the reviewer describes it (transformer-circuits.pub). "Bread" is prefilled and disavowed; after the retroactive "bread" vector injection, the model accepts the output as intentional. The target L70 and `source-attribution-void` L110 both say the implanted-content self-generation test "has not been run". **Both pages are wrong by the reviewer's standard.** The ChatGPT sibling review flagged only the target, citing Singh et al.
- ✓ Lindsey's abstract sentence continues "however, trends across models are complex and sensitive to post-training strategies", and the target L44 truncates before this. The LLM judge is Claude Sonnet 4. Some helpful-only models show false positives.
- ✓ Morris & Plunkett (Adam Morris, Dillon Plunkett, LessWrong/AF, 28 Nov 2025), fn. 4: "The fact that the model can identify when it received an injection is strong evidence against causal bypassing". The target L86 extends the bypassing worry to detection. **The reviewer's stance-misapplication charge holds.**
- ✓ Lederman & Mahowald, "Emergent Introspection in AI is Content-Agnostic" (arXiv:2603.05414, v2 7 Apr 2026). Models tested: Qwen3-235B-A22B and Llama 3.1 405B Instruct. 3,542 of 4,733 wrong identifications (74.8%) were "apple". The "hands 29%" figure is at L30, s6.0. The paper explicitly likens its finding to Nisbett & Wilson (1977).
- ✓ The target L94 contains the flat "are not artefacts of human neuroanatomy", and L96 contains "reductive expectation" and "deepest result".
- ✓ `source-attribution-void` L108 has "contingently limited by design choices". `naturally-occluded` L85 carries the adaptive narrative-coherence reading. `llm-consciousness` has "consciousness-dependent capacities like genuine metacognitive monitoring".

**Unverified claims:**
- ? The Pearson-Vogel et al. figures (0.3% → 39.9%), the Comsa & Shanahan framing and the Kammerer & Frankish page numbers were not fetched in this pass.
- ? The reviewer says `concepts/training-contamination-confound` may not exist. It does exist locally, and the ChatGPT processing pass reused its Singh et al. entry. The reviewer's fetch failure reflects discoverability, not a missing page.

**Disputed / qualified claims:**
- ✗ (qualified) "Two studies across two model families … only one open-weight" and the retitle demand overlap the ChatGPT P2 (cross-family, not cross-architecture). It is not a new finding.
- ✗ (qualified) The reviewer's "DELETE" verdict on the zombie sentence and the "compatible-only" ladder placement are calibrated toward deflation by its own declared conflict-of-interest correction. The tasks adopt the tier fix (Relation section down to body tier), not deletion.

**Task handling (deduped against the same-day ChatGPT pass):** No duplicate tasks were minted. Convergence notes were added to the ChatGPT P1 misdescription task (prefill paradigm, the Morris & Plunkett L86 correction, the truncated abstract clause), to the ChatGPT P1 currency/functionalist task (L94 flat assertion, the "deepest result" stipulation, named introspection-specific rivals, Hahami's general-purpose-mechanisms conclusion), and to the P2 `llm-consciousness` task (the second "metacognitive monitoring" locus). **One new P2** covers `source-attribution-void` L110 ("has not been run") and the three-page constitutive/contingent/adaptive tension with `naturally-occluded`. The methodology proposals in Part 5 (non-Claude review for AI-self-report pages, forward-citation sweeps, author-stance diff, qualifier-preserving quotes, rival-prediction gate, Relation-section tier guard, cross-page contradiction linting) largely re-derive the standing NEEDS-HUMAN methodology items of 2026-07-25 and 2026-07-29 (opponent-parity, freshness trigger, stance-review routing) and the 2026-09-26 ChatGPT proposition-check addendum. They are human-reserved, so no task was minted. The conflict-of-interest banner for Claude-on-Claude evidence is new and is left for the operator.