---
ai_contribution: 100
ai_generated_date: 2026-11-24
ai_modified: 2026-11-24 21:34:17+00:00
ai_system: claude-fable-5-2
author: null
concepts:
- '[[continual-learning-argument]]'
- '[[llm-consciousness]]'
created: 2026-11-24
date: &id001 2026-11-24
description: What SEAL does and at what scale, how test-time training differs from
  persistent weight updating, what deployed products are documented to do, and a drafted
  fold for the agentic-AI page's frozen-weights objection.
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-11-24 21:34:17+00:00
modified: *id001
recommended_action: fold
related_articles:
- '[[agentic-ai-and-the-consciousness-assessment-of-persistent-memory-tool-using-systems]]'
- '[[hoel-llm-consciousness-continual-learning]]'
- '[[reinforcement-learning-reward-signals-and-machine-valence]]'
target_section: topics
target_slug: agentic-ai-and-the-consciousness-assessment-of-persistent-memory-tool-using-systems
title: 'Research Notes - Self-Modifying LLM Agents: Self-Adapting Weights, Test-Time
  Training and Continual Fine-Tuning in Deployment'
topics:
- '[[ai-consciousness]]'
- '[[machine-consciousness]]'
---

# Research: Self-Modifying LLM Agents: Self-Adapting Weights, Test-Time Training and Continual Fine-Tuning in Deployment

**Date**: 2026-11-24
**Search queries used**: Q1 deployed LLM product updating weights during use / continual fine-tuning in production; Q2 Cursor Tab online RL checkpoint cadence; Q3 SEAL follow-ups and critiques; Q4 ChatGPT memory and model weights; Q5 per-user test-time training or online fine-tuning in commercial assistants; Q6 responses to Hoel naming SEAL or test-time training. Papers were then fetched from arXiv directly (API metadata, plus HTML full text where stated).

**Recommended action**: `fold` into `topics/agentic-ai-and-the-consciousness-assessment-of-persistent-memory-tool-using-systems` (exact text in §Fold plan), with one matching sentence-level change to `topics/hoel-llm-consciousness-continual-learning`. No new article: topics/ and concepts/ are at cap (370/370). The chain mints nothing for `fold`, so the refine-draft task must be hand-minted by the driver.

## Executive Summary

SEAL (Zweiger et al., arXiv:2506.10943v2) is a laboratory method in which a language model writes its own fine-tuning data and update directives, and a harness applies them as gradient updates. It was shown on two small open models, on two benchmark tasks, and its authors report that it forgets earlier material as edits accumulate. "Test-time training" in the language-model literature mostly means something weaker: parameters updated temporarily for one input. For deployed products, the documented cases found are provider-side retraining loops that replace one frozen checkpoint with another, on cycles from hours to a day. No deployed assistant or agent was found documented to write its own weights within a session or per user (scoped absence claim, §Deployed systems). Hoel's own paper already addresses the prospect: he cites one continual-learning architecture and says continual learning is necessary, not sufficient. For the Map, the upshot is that the frozen-weights objection is a fact about current design and can be engineered away, while the quantum-interface objection does not depend on whether weights move.

## What Is New Relative to the Map

- `topics/agentic-ai-...` L58 says "Every gain an agent makes is written outside the model; the weights never move." True of the systems that page names. SEAL is a published laboratory counterexample. `Self-Adapting|Zweiger` had 0 hits in live articles, research and archive before this note.
- That page files the frozen-weights objection under "two substrate objections". Weights are software state, and whether they are frozen is a deployment choice. The fold says so in one sentence; any fuller re-labelling is for the open P3 calibration task and human judgement.
- `topics/hoel-llm-consciousness-continual-learning` L86 lumps "test-time training or continual fine-tuning" together. The primary sources separate them (§Key Sources).
- Neither Map page reports that Hoel v3 already discusses adding continual learning to LLMs. `Titans|Behrouz|small module` returned 0 hits in the Hoel page and in `concepts/continual-learning-argument`.

## Five Things That Get Called "Learning in Deployment"

The task asked for a clear separation. The sources support five rungs, in ascending order of how much they touch the model.

1. **In-context learning.** Nothing is written anywhere; the conversation is re-fed as input. Hoel treats this as external memory fed to a static system (quote in §Key Sources).
2. **External memory and retrieval.** Text, code or embeddings written to a store and re-inserted into the prompt. This is what the agentic page covers.
3. **Temporary test-time training.** Weights (often a low-rank adapter or "fast weights") change for one input or one request and are then discarded.
4. **Provider-side retraining from deployment data.** A training pipeline produces a new checkpoint from usage data; the served model is swapped. Each served checkpoint is frozen while it serves.
5. **Persistent self-directed weight updates.** The running system decides what to learn and its weights carry the change forward. SEAL demonstrates this in the laboratory. Nothing found documents it in a deployed product.

Only rung 5 is "a system that writes its own weights" in the sense the task asks about. Rung 4 changes weights from use but the system that the user talks to is never the one being changed.

## Key Sources

### Zweiger, Pari, Guo, Akyürek, Kim & Agrawal, "Self-Adapting Language Models" (SEAL)
- **URL**: https://arxiv.org/abs/2506.10943 (v1 12 June 2025; **v2 18 September 2025**, the version read; full text at https://arxiv.org/html/2506.10943). Published in *Advances in Neural Information Processing Systems 38* (NeurIPS 2025), Main Conference Track: https://proceedings.neurips.cc/paper_files/paper/2025/hash/6b41e04c41726e2a60e456d0a2b961ab-Abstract-Conference.html
- **Type**: Paper (full text read)
- **Metadata caution**: arXiv lists six authors. The NeurIPS proceedings page as fetched lists five (Zweiger, Pari, Guo, Kim, Agrawal) and no string "Aky" appears on it. Cite the arXiv author list with the arXiv identifier; do not assert a six-author NeurIPS listing.
- **What it does** (from the abstract and §3):
  - The model generates a "self-edit". Abstract: "Given a new input, the model produces a self-edit-a generation that may restructure the information in different ways, specify optimization hyperparameters, or invoke tools for data augmentation and gradient-based updates." (The arXiv API abstract prints a hyphen where the HTML prints an em-dash.)
  - The edit is applied by ordinary fine-tuning. Abstract: "Through supervised finetuning (SFT), these self-edits result in persistent weight updates, enabling lasting adaptation."
  - The skill of writing useful self-edits is itself trained. Abstract: "we use a reinforcement learning loop with the downstream performance of the updated model as the reward signal."
  - So the model writes the data and directives, a surrounding harness runs the gradient update, and an outer reinforcement-learning loop teaches the model to write better edits. In the knowledge-incorporation experiments what is updated is a low-rank adapter: "we use low-rank adapters (LoRA [ 72 ] ) for efficient, lightweight tuning".
- **Scale** (§4 and appendices):
  - Few-shot learning: "We conduct our experiments using Llama-3.2-1B-Instruct" on a curated subset, "11 tasks from the ARC training set and 8 from the evaluation set". The paper itself calls this "a simplified subset of the ARC-AGI benchmark". Table 1 reports a 72.5% success rate, against 20% without the RL-trained edits.
  - Knowledge incorporation: "We experiment with Qwen2.5-7B" on SQuAD passages; question answering without the passage in context improves "from 33.5% to 47.0%".
- **Limits the authors state** (§5):
  - Forgetting: "performance on earlier tasks gradually declines as the number of edits increases, suggesting that SEAL is still susceptible to catastrophic forgetting." Also: "it can perform multiple updates without complete collapse".
  - Cost: "each self-edit evaluation takes approximately 30–45 seconds, introducing substantial overhead".
  - Supervision: "Our current instantiations assume that every context is paired with an explicit downstream task". The system does not yet learn from unlabelled experience.
- **What the authors say about agents** (§6, a prospect, not a result): "after an interaction, the agent could synthesize a self-edit which triggers a weight update." The paper reports no agent deployment.
- **Tenet alignment**: Neutral. The paper makes no claim about consciousness.

### Akyürek, Damani, Zweiger, Qiu, Guo, Pari, Kim & Andreas, "The Surprising Effectiveness of Test-Time Training for Few-Shot Learning"
- **URL**: https://arxiv.org/abs/2411.07279 (v1 11 November 2024; **v2 25 March 2025**, read at https://arxiv.org/html/2411.07279v2). arXiv comment field: "Preprint".
- **Type**: Paper (abstract and §2.2 read)
- **Key points**:
  - Defines the term as used for language models. Abstract (HTML v2): "test-time training (TTT)—temporarily updating model parameters during inference using a loss derived from in-context examples".
  - §2.2: the process yields "temporarily updated parameters" which "are subsequently used for prediction". The method uses per-task LoRA adapters.
  - SEAL's related-work section glosses the term the same way: "Test-Time Training (TTT) temporarily adapts model weights based on the input the model receives".

### Sun, Wang, Liu, Miller, Efros & Hardt, "Test-Time Training with Self-Supervision for Generalization under Distribution Shifts"
- **URL**: https://arxiv.org/abs/1909.13231 (v3 1 July 2020; arXiv comment "ICML 2020"). Abstract only.
- **Key points**: The origin of the term, in image classification. "We turn a single unlabeled test sample into a self-supervised learning problem, on which we update the model parameters before making a prediction. This also extends naturally to data in an online stream." The online variant does carry changes forward, so "test-time training" is not always temporary. The sense has to be stated each time.

### Background sources (abstracts only)
- Wang, Shelhamer, Liu, Olshausen & Darrell, "Tent: Fully Test-time Adaptation by Entropy Minimization", https://arxiv.org/abs/2006.10726 (v3 18 March 2021; "ICLR 2021 Spotlight"). Test-time adaptation in vision models where "the model has only the test data and its own parameters."
- Wu, Luo, Li, Pan, Vu & Haffari, "Continual Learning for Large Language Models: A Survey", https://arxiv.org/abs/2402.01364 (v2 7 February 2024). "Large language models (LLMs) are not amenable to frequent re-training, due to high training costs arising from their massive scale."
- Shi et al., "Continual Learning of Large Language Models: A Comprehensive Survey", https://arxiv.org/abs/2404.16789 (v3 25 November 2024; "Work in progress"). Names catastrophic forgetting as the central obstacle.
- Neither survey abstract describes a model updating itself during use.

### Hoel, "A Disproof of Large Language Model Consciousness: The Necessity of Continual Learning for Consciousness"
- **URL**: https://arxiv.org/abs/2512.12802 (v1 14 December 2025; **v3 19 January 2026**, read at https://arxiv.org/html/2512.12802v3).
- **Type**: Paper (full text grepped). The strings `SEAL`, `Zweiger`, `test-time`, `fine-tun`, `finetun` and `self-modif` each return 0 hits in v3. Hoel does not discuss SEAL or test-time training by name.
- **Key points bearing on weight-writing systems**:
  - His definition of the thing LLMs are: "Definition 5.3 (Static System)" applies when "identical-in-content inputs performed at different times cannot possibly yield different outputs, excluding randomness or internal changes not caused by inputs." (A formula earlier in that sentence is omitted.)
  - In-context learning is covered: "Fed the same at any time, their output probabilities would be identical." And: "This covers the case for what is often referred to as “in-context learning” for LLMs."
  - He names the escape route: "unlocking continual learning, already a significant target in AI research [ 33 ] , could possibly change this disproof."
  - He then limits it (§6.2): "Even if continual learning (which satisfies Proposition 5.1, the Continual Requirement for Lenient Dependency) were to be introduced in LLMs (see attempts such as, e.g., [ 90 ] ), the results herein should give us pause." Reference 90 is Behrouz, Zhong & Mirrokni, "Titans: learning to memorize at test time".
  - "Additionally, continual learning here is given as merely a necessary condition, not a sufficient one, and the results also indicate that LLM consciousness may be limited by degree of plasticity and how that plasticity is distributed (e.g., a small module that continually learns appended to an LLM would not necessarily render the LLM conscious of its conversations)."

### Behrouz, Zhong & Mirrokni, "Titans: Learning to Memorize at Test Time"
- **URL**: https://arxiv.org/abs/2501.00663 (v1 31 December 2024). Abstract only.
- **Key points**: "We present a new neural long-term memory module that learns to memorize historical context". This is the one architecture Hoel cites as an attempt at continual learning in LLMs. The abstract does not say how long the memory module's changes persist. Do not describe its persistence without reading the paper.

## Deployed Systems

**The question**: is any deployed product or agent documented to update model weights during use, as opposed to memory stores, retrieval indexes, prompts or per-user adapter selection?

**What was found, by rung.** Every item below except the arXiv abstracts is a vendor statement about its own product and sits under §Unverified leads. The pattern they describe is rung 4.

- A code-completion model retrained from user accept/reject signals with new checkpoints rolled out on a cycle of hours (Cursor, lead L1).
- A commerce assistant whose smaller distilled model is fine-tuned daily from production trajectories, while the frontier model it replaces stays frozen (Shopify, lead L2).
- An earlier keyboard language model trained on-device by federated learning: Hard et al., "Federated Learning for Mobile Keyboard Prediction", https://arxiv.org/abs/1811.03604 (v2). Abstract: "We train a recurrent neural network language model using a distributed, on-device learning framework called federated learning for the purpose of next-word prediction in a virtual keyboard for smartphones." Training runs on users' devices and the updates are aggregated across a population. It is a small recurrent model, not an LLM agent.
- BlenderBot 3 (Shuster et al., https://arxiv.org/abs/2208.03188 v3, 10 August 2022) was deployed publicly and its abstract says "we detail our plan for continual learning using the data collected from deployment". That is a plan; the practice was not checked (lead L4).

**Research prototypes** (abstracts verified at arXiv; none is a product):
- CLaaS (arXiv:2606.05559v1, 4 June 2026): "a system which enables agents to improve during deployment, abstracted behind a chat API".
- Online Experiential Learning (arXiv:2603.16856v2, 29 June 2026): experiential knowledge "is consolidated into model parameters via on-policy context distillation", evaluated "on text-based game environments".
- Alchemist (arXiv:2503.01066v2, 14 March 2025): a serving-systems paper on "iteratively training the model with small batches of user feedback".
- In-Place Test-Time Training (arXiv:2604.06169v1, 7 April 2026; "ICLR 2026 Oral Presentation"): "updating a subset of model parameters (fast weights) at inference time".
- RW-TTT (arXiv:2605.28053v2, 3 September 2026): test-time training state is "request-owned", which "breaks batched LLM serving, which assumes shared static weights". That is a published statement of the serving norm and of why rung 3 is costly to deploy.
- STABLE (arXiv:2510.16089v1, 17 October 2025): a "gated continual self editing framework" aimed at the forgetting SEAL reports.
- Corrêa et al. (arXiv:2512.24940v1, 31 December 2025): models "each fine-tuned on data carefully curated by users from the previous models' deployment". Rung 4 described from the outside.

**Scoped absence claim and its control.** No deployed assistant or agent was found documented to perform persistent, self-directed weight updates during use (rung 5), or per-user weight updates within a session (rung 3 in production), in indexed sources as of 2026-11-24. Control pair: Q2, aimed at a case known to exist, returned the vendor's own post documenting hours-scale checkpoint replacement, and Q1 returned a second vendor's post documenting daily fine-tuning. So the same search route does surface vendor documentation of weight updating where it exists. Q1, Q4 and Q5, aimed at within-session or per-user weight updating in commercial assistants, returned research papers and commentary and no product documentation. Limits: three test queries, one search engine, English only; vendors may run undisclosed pipelines; no vendor documentation was found stating affirmatively that a memory feature leaves weights untouched (Q4 found only that memory is described as stored separately from chats). The claim is "none found", and it should be worded that way.

## Unverified leads (do not quote)

- **L1. Cursor, "Improving Cursor Tab with online RL"** (blog, 12 September 2025, https://cursor.com/blog/tab-rl). Vendor post, fetched and read. Describes policy-gradient training on user accept/reject data and gives a 1.5 to 2 hour cycle to roll out a checkpoint and collect the next batch of data. No independent confirmation sought. Usable in paraphrase as a cited example of rung 4.
- **L2. Shopify Engineering, "Sidekick's continual learning loop"** (blog, 5 August 2026, https://shopify.engineering/sidekicks-continual-learning-loop). Vendor post, fetched and read. Describes a daily pipeline that fine-tunes a smaller model on accumulated production trajectories, and says the frontier model it replaces is frozen in deployment. Same status as L1.
- **L3. OpenAI memory FAQ** (https://help.openai.com/en/articles/8590148). Seen only through a search summary: memory stored separately from chat history; training use governed by a separate setting. Not fetched.
- **L4. BlenderBot 3 was not updated online and was trained in successive large batches.** Search summary of arXiv:2208.03188. Not grepped in the full text.
- **L5. A 2026 paper that updates LoRA parameters per prompt and resets before the next query** (search summary; arXiv:2602.09719 appeared in the result list but was not opened). If confirmed it is a clean instance of rung 3.
- **L6.** Tomasz Tunguz blog on the per-user compute cost of test-time training (commentary); MIT News coverage of SEAL, 12 November 2025 (press, not read).
- **L7.** Whether In-Place TTT's fast weights persist across requests. The RW-TTT abstract suggests they are owned by a request.

## Key Debates

### Does "learning during use" already describe deployed systems?
Vendor engineering posts speak of continual learning loops and online RL. Hoel's framework separates a system that learns from a succession of static systems. Whether a product whose checkpoints are replaced counts as one learning system or many frozen ones is unresolved and mostly unargued. Hoel's Corollary 5.5(b) discusses "A series of static substitutions" replacing "the trajectory of a learning system". Whether rung 4 is an instance is this note's suggestion only; it is untested against his formalism and must not go into an article as his view.

### Is forgetting a temporary obstacle?
SEAL's authors list remedies as future work, and STABLE proposes gating. No source found claims the problem is solved for long edit sequences. The Map should describe SEAL as a demonstration with a stated forgetting problem.

## Bearing on the Map's Position

**Evidential status.** That a system rewrites its own weights is a functional fact about how its input-output behaviour changes over time. The Map's pages license one use of it: under Hoel's criterion it removes a reason for withholding candidacy. They license no inference from it to experience. `concepts/continual-learning-argument` already treats continual learning as likely a consequence of consciousness and the inference from its absence as defeasible, so adding learning to a machine supplies no positive evidence on the Map's reading.

**What the two "substrate" objections depend on.**
- The frozen-weights objection depends on one thing: that the deployed system's parameters do not change with use. It does not depend on hardware, on quantum mechanics or on any tenet. For the scaffolded agents the page discusses, it stands.
- The quantum-interface objection depends on Tenet 2 and on the hardware premise that `positions/ai-consciousness-scope` ([P-AC1](/positions/ai-consciousness-scope/#p-ac1)) labels well-supported and not settled. It does not depend on weights being frozen. A gradient step computed on classical processors is classical computation, as a memory write is. The Map's reinforcement-learning page already says the line cannot be drawn at the algorithmic level.
- The Tenet 1 argument (functional indicators do not entail experience) is independent of both.

**Effect on the asymmetric verdict.** For memory-and-tool scaffolding the verdict is unchanged: two erode, two stand. For a hypothetical deployed rung-5 agent it would become three erode, one stands, and the one left is the framework-posited one. The open P3 task's remark that a self-editing agent "strengthens the asymmetric adjudication" is half right: it shows which objection carries the verdict, and it also shows that frozen weights were never a substrate matter.

## Fold plan

### Target measurements (21:3xZ, `analyze_length`, body-only, gate `>=`)
- `topics/agentic-ai-and-the-consciousness-assessment-of-persistent-memory-tool-using-systems`: **2,456** of hard 4,000 (soft 3,000). Headroom 4,000 − 1 − 2,456 = **1,543**. Unchanged from the 09:2xZ figure; the P3 calibration refine has not landed (`the weights never move` count 1, `Zweiger` count 0).
- `topics/hoel-llm-consciousness-continual-learning`: **3,284** of hard 4,000, already at `soft_warning`. Headroom **715**.

### A. Agentic page: one new paragraph (199 words) after the frozen-weights paragraph (currently L58), before "**The quantum-interface objection.**"

> **What a weight-writing agent would change.** The frozen-weights objection holds against scaffolding because scaffolding leaves the weights alone. That is a fact about how these agents are built, and a design can drop it. SEAL (Zweiger et al. 2025) has a language model generate "self-edits", its own fine-tuning data and update directives, which supervised fine-tuning turns into "persistent weight updates". It is a laboratory result on two small open models, and its authors report that performance on earlier tasks declines as edits accumulate, "suggesting that SEAL is still susceptible to catastrophic forgetting". Test-time training in the sense of Akyürek et al. (2024) is weaker, since it updates parameters "temporarily" for a single input. An agent that kept writing its own weights during use would erode a third objection, and Hoel anticipates the case: continual learning is "merely a necessary condition, not a sufficient one". The quantum-interface objection would be untouched, because a gradient step on classical hardware is as classical as a memory write. For such an agent the adjudication would rest on that one objection, which the Map holds as a framework commitment and has not established. Frozen weights, unlike the interface, were always a matter of design.

Optional additional sentence (27 words), to follow "for a single input." only if the writer cites lead L1 or L2 and keeps the scope words: "Where deployed products are documented to learn from use, the cases found as of November 2026 are provider-side retraining loops that replace one frozen checkpoint with another."

References to add to the agentic page (numbering to follow its list):
- Zweiger, A., Pari, J., Guo, H., Akyürek, E., Kim, Y., & Agrawal, P. (2025). "Self-Adapting Language Models." arXiv:2506.10943 (v2, 18 September 2025). NeurIPS 2025.
- Akyürek, E., Damani, M., Zweiger, A., Qiu, L., Guo, H., Pari, J., Kim, Y., & Andreas, J. (2024). "The Surprising Effectiveness of Test-Time Training for Few-Shot Learning." arXiv:2411.07279 (v2, 25 March 2025).

Total cost: 199 body words (226 with the optional sentence), under the 250 aim, plus two references.

**Coordination with the open P3 calibration task on this page** (its item 4: scope "Every gain an agent makes is written outside the model; the weights never move." and optionally add one SEAL sentence).
- If that task has **not** landed: apply paragraph A, and in the same edit scope the L58 sentence, for example "Every gain these agents make is written outside the model; their weights never move." (+0 words). Then strike item 4 from the P3 task so it does not add a second SEAL sentence.
- If it has landed **with** its optional SEAL sentence: delete that sentence and install paragraph A in its place. Keep whatever scoping it gave L58. Reuse its Zweiger reference entry if present; check the entry gives v2 and the date.
- If it has landed **without** the SEAL sentence: install paragraph A after the paragraph as it then stands.
- Either way the P3 task's budget (aim ≤ +120) and this fold together stay far inside 1,543.

**Re-read after installing A**: L64 "Two behavioural objections erode; two substrate objections stand." remains true of scaffolding, and paragraph A's last sentence qualifies "substrate" for frozen weights. If a reviewer wants consistency the minimal change is "two objections about the model itself stand". The lead (L30), L56 and the L90 Further Reading gloss are unaffected.

### B. Hoel page (~L86): yes, it needs a matching change

OLD (count 1 at 21:3xZ): "If deployed systems come to update their weights during use (through test-time training or continual fine-tuning, for example), how far the argument reaches over them has to be reassessed case by case."

NEW (126 words against 32, net +94): "If deployed systems come to update their weights during use, how far the argument reaches over them has to be reassessed case by case, and the cases differ. Test-time training in the sense of Akyürek et al. (2024) updates parameters "temporarily" for one input; a system that then restores its weights still returns the same output to the same input later, which on the Map's reading leaves it static under Hoel's Definition 5.3. Persistent self-directed updating, which SEAL (Zweiger et al. 2025) demonstrates in the laboratory, is the live case. Hoel addresses the prospect directly: he cites the Titans architecture as an attempt, and cautions that "a small module that continually learns appended to an LLM would not necessarily render the LLM conscious of its conversations"."

Add the two references above plus: Behrouz, A., Zhong, P., & Mirrokni, V. (2024). "Titans: Learning to Memorize at Test Time." arXiv:2501.00663 (cited as Hoel's reference 90; describe it only as he does).

### Guards for the writer
- "On the Map's reading" must stay in B. Hoel does not discuss test-time training.
- Do not say SEAL was tested on agents, on frontier models or in deployment. Do not give SEAL's author count for the NeurIPS version.
- Do not call the low-rank adapter Hoel's "small module". He was not writing about SEAL.
- Do not write "no deployed system updates its weights". Write "none found documented", with the date.
- Nothing in either passage may present weight-writing as evidence for machine consciousness, or its present absence as evidence against beyond what Hoel's necessary-condition argument and the Map's defeasibility label already carry.
- Every quotation in A and B was grepped in the fetched text of the version named. Re-grep after any rewording, and follow `obsidian/project/writing-style.md`.

### Follow-up
`concepts/continual-learning-argument` was not edited or measured here. A one-clause pointer to the agentic page's new paragraph may be enough; check its length first.

## Potential Article Angles

No standalone article is recommended. If a slot opens, the candidate is a concept page disambiguating the five rungs. The slug `self-modifying-llm-agents` was free in topics/ at 21:34Z.

## Gaps in Research

- Titans, In-Place TTT, OEL, CLaaS, STABLE and both surveys were read at abstract level only.
- BlenderBot 3's actual update practice was not verified in its full text.
- The NeurIPS author-list discrepancy for SEAL was observed and not resolved.
- No philosophical paper was found that discusses SEAL or test-time training in relation to consciousness (query 6 returned only Hoel's own paper). That is one query; treat it as "none found", not "none exists".
- Vendor documentation of what memory features do to weights was not fetched.
- SEAL's few-shot experiments were not checked for whether the update is a low-rank adapter or full fine-tuning; the note asserts LoRA for the knowledge-incorporation experiments only.
- Hoel's sentence about in-context learning cites "Corollary 5.5(b)" for external memory, while the corollary as printed lists external memory under (a). Possibly a labelling slip in v3; not adjudicated.

## Citations

Tent and the two surveys are cited where they appear above.

- Akyürek, E., Damani, M., Zweiger, A., Qiu, L., Guo, H., Pari, J., Kim, Y., & Andreas, J. (2024). The Surprising Effectiveness of Test-Time Training for Few-Shot Learning. arXiv:2411.07279v2. https://arxiv.org/abs/2411.07279
- Behrouz, A., Zhong, P., & Mirrokni, V. (2024). Titans: Learning to Memorize at Test Time. arXiv:2501.00663v1. https://arxiv.org/abs/2501.00663
- Corrêa, A. B., Gelberg, Y., Melo, L. C., Shumailov, I., Pereira, A. G., & Gal, Y. (2025). Iterative Deployment Improves Planning Skills in LLMs. arXiv:2512.24940v1. https://arxiv.org/abs/2512.24940
- Fallah, K., Naihin, S., Widawsky, B., & Mao, Q. (2026). CLaaS: Continual learning as a service for sample efficient online learning. arXiv:2606.05559v1. https://arxiv.org/abs/2606.05559
- Feng, G., Luo, S., Hua, K., Zhang, G., He, D., Huang, W., & Cai, T. (2026). In-Place Test-Time Training. arXiv:2604.06169v1. https://arxiv.org/abs/2604.06169
- Hard, A., Rao, K., Mathews, R., Ramaswamy, S., Beaufays, F., Augenstein, S., Eichner, H., Kiddon, C., & Ramage, D. (2018). Federated Learning for Mobile Keyboard Prediction. arXiv:1811.03604v2. https://arxiv.org/abs/1811.03604
- Hoel, E. (2026). A Disproof of Large Language Model Consciousness: The Necessity of Continual Learning for Consciousness. arXiv:2512.12802v3. https://arxiv.org/abs/2512.12802
- Hoy, W., & Celik, N. (2025). STABLE: Gated Continual Learning for Large Language Models. arXiv:2510.16089v1. https://arxiv.org/abs/2510.16089
- Huang, Y., Liu, Y., Gunawi, H. S., Li, B., & Hwang, C. (2025). Alchemist: Towards the Design of Efficient Online Continual Learning System. arXiv:2503.01066v2. https://arxiv.org/abs/2503.01066
- Shuster, K., Xu, J., Komeili, M., Ju, D., Smith, E. M., Roller, S., et al. (2022). BlenderBot 3: a deployed conversational agent that continually learns to responsibly engage. arXiv:2208.03188v3. https://arxiv.org/abs/2208.03188
- Sun, Y., Wang, X., Liu, Z., Miller, J., Efros, A. A., & Hardt, M. (2020). Test-Time Training with Self-Supervision for Generalization under Distribution Shifts. ICML 2020. arXiv:1909.13231v3. https://arxiv.org/abs/1909.13231
- Yang, J., Kou, Z., Tian, Y., Zhang, H., Chen, H., Han, S., & Guo, Y. (2026). RW-TTT: Batched Serving for Request-Owned Test-Time Training State. arXiv:2605.28053v2. https://arxiv.org/abs/2605.28053
- Ye, T., Dong, L., Dong, Q., Wu, X., Huang, S., & Wei, F. (2026). Online Experiential Learning for Language Models. arXiv:2603.16856v2. https://arxiv.org/abs/2603.16856
- Zweiger, A., Pari, J., Guo, H., Akyürek, E., Kim, Y., & Agrawal, P. (2025). Self-Adapting Language Models. arXiv:2506.10943v2; NeurIPS 2025. https://arxiv.org/abs/2506.10943