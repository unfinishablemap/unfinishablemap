# Large Language Models Cannot Self-Correct Reasoning Yet

## Bibliographic
- **Title:** Large Language Models Cannot Self-Correct Reasoning Yet
- **Authors:** Jie Huang, Xinyun Chen, Swaroop Mishra, Huaixiu Steven Zheng, Adams Wei Yu, Xinying Song, Denny Zhou
- **Date:** 2024 (arXiv v2: 14 Mar 2024; originally submitted Oct 2023)
- **Venue:** Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)
- **URL:** https://arxiv.org/abs/2310.01798

## File
- **Local path:** papers/downloads/arxiv-2310.01798.pdf
- **SHA-256:** 15e1731e255ec6b217792a1e077926807da77e8e46b69e6c57dda30d67794761
- **Size:** 385585
- **Downloaded:** 2026-03-01

## Summary
Critically examines the concept of "intrinsic self-correction" in LLMs — where a model attempts to correct its own responses without external feedback. Finds that LLMs struggle to self-correct reasoning in this setting, and performance often degrades after self-correction attempts. Argues that positive results in the literature often rely on external feedback (ground-truth labels, tool outputs) smuggled into the correction step.

## Relevance to Our Paper
High relevance. This is the key counterpoint to our adversarial self-review architecture. We cite it in §2.4 to acknowledge the self-correction limitation and explain how the Map's approach differs from pure intrinsic self-correction (external source verification via web search, cross-model outer review, corpus-level consistency checking rather than single-output correction).

## Notes
Google DeepMind paper. Authors from Google DeepMind and University of Illinois at Urbana-Champaign. The paper specifically defines "intrinsic self-correction" as a setting without external feedback — our system's use of web search verification and cross-model review places it partially outside this definition, which is the distinction we draw in the draft.
