# Shinn et al. (2023) — Reflexion: Language Agents with Verbal Reinforcement Learning

## Bibliographic

- **Title:** Reflexion: Language Agents with Verbal Reinforcement Learning
- **Authors:** Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao
- **Date:** 20 March 2023 (revised 10 October 2023)
- **Venue:** NeurIPS 2023
- **URL:** https://arxiv.org/abs/2303.11366
- **License:** Not specified
- **Pages:** 21

## File

- **Local path:** `papers/downloads/arxiv-2303.11366.pdf`
- **SHA-256:** `6059b6f89fea9959bd3dab553fbb97756a3dfb1b15e3cbab2fbf3ab6664333bd`
- **Size:** 578,000 bytes (approx)
- **Downloaded:** 2026-02-28

## Summary

Reflexion introduces a framework for reinforcing language agents through verbal self-reflection rather than weight updates. Agents convert binary or scalar task feedback into natural-language reflective summaries stored in an episodic memory buffer, which are then used as context in subsequent trials to improve decision-making. The approach achieves significant improvements across decision-making (AlfWorld), reasoning (HotPotQA), and programming (HumanEval) benchmarks, reaching 91% pass@1 on HumanEval.

## Relevance to Our Paper

**Medium-high.** Reflexion's verbal reflection mechanism is an important precedent for the Map's system-level self-improvement:

1. **Episodic memory parallels our changelog and evolution state** — Reflexion agents maintain natural-language experience summaries that persist across trials, analogous to how the Map's changelog and evolution-state.yaml track prior actions, outcomes, and lessons learned at the system level.

2. **Verbal reinforcement vs. tenet-constrained review** — Reflexion converts environment feedback into self-reflective text that guides future behaviour. Our review layers (pessimistic, optimistic, deep) serve a similar function but operate over a persistent knowledge base rather than individual task episodes, and are constrained by explicit tenets rather than task-specific feedback signals.

3. **Supports the broader argument** that LLMs can improve through structured self-critique without retraining, which is a core assumption of our continuous evolution architecture.

## Notes

- Six authors across Northeastern University, MIT, and Princeton
- Achieves 91% pass@1 on HumanEval, surpassing GPT-4's 80% at the time
- Modular architecture with separate Actor, Evaluator, and Self-Reflection models
- Published at NeurIPS 2023; widely cited in the self-improvement literature
- Shares co-author (Shunyu Yao) with Tree of Thoughts — both explore structured LLM reasoning
