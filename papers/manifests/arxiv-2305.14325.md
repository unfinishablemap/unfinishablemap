# Du et al. (2024) — Improving Factuality and Reasoning in Language Models through Multiagent Debate

## Bibliographic

- **Title:** Improving Factuality and Reasoning in Language Models through Multiagent Debate
- **Authors:** Yilun Du, Shuang Li, Antonio Torralba, Joshua B. Tenenbaum, Igor Mordatch
- **Date:** 23 May 2023 (revised 23 May 2023)
- **Venue:** ICML 2024
- **URL:** https://arxiv.org/abs/2305.14325
- **License:** Not specified
- **Pages:** 18

## File

- **Local path:** `papers/downloads/arxiv-2305.14325.pdf`
- **SHA-256:** `b302ff15202dc3cda03f40ea1ac92b29e1519978540b345af92991f6d3e619b4`
- **Size:** 1,700,000 bytes (approx)
- **Downloaded:** 2026-02-28

## Summary

This paper proposes a multiagent debate framework where multiple LLM instances independently generate responses, then read and critique each other's answers over several rounds to converge on a common final answer. The approach improves both factual accuracy and mathematical/strategic reasoning across six benchmarks, outperforming single-model baselines such as chain-of-thought and self-reflection. Notably, the debate process can correct cases where all models initially produce wrong answers, not merely amplifying a correct minority.

## Relevance to Our Paper

**Medium-high.** Multiagent debate is the closest analogue to the Map's adversarial review layers:

1. **Structured adversarial roles mirror our review architecture** — Du et al.'s multiple debating agents map directly to our pessimistic and optimistic review layers, which function as a structured form of adversarial debate over philosophical content rather than individual factual questions.

2. **Convergence through disagreement** — the paper shows that models converge to more accurate answers through iterative debate. Our system pursues a similar dynamic: content evolves through cycles of generation, pessimistic challenge, and revision, driving toward more defensible philosophical positions.

3. **Different-model debate improves outcomes** — the paper investigates mixing model types (ChatGPT and Bard), finding value in heterogeneous agents. This supports our outer-review approach of using different AI systems to avoid shared blind spots.

4. **Consensus can be wrong** — the finding that similar models converge to shared misconceptions motivates our use of explicit tenet constraints and human curation to prevent consensus drift.

## Notes

- Authors from MIT CSAIL and Google Brain
- Tested on Biographies, MMLU, Chess, Arithmetic, Grade School Math benchmarks
- Requires only black-box API access — no model internals needed
- Published at ICML 2024
- Extended by Estornell & Liu (2024, Ref #29) with a more rigorous mathematical framework for multi-LLM debate
