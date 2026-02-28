# Bai et al. (2022) — Constitutional AI: Harmlessness from AI Feedback

## Bibliographic

- **Title:** Constitutional AI: Harmlessness from AI Feedback
- **Authors:** Yuntao Bai, Saurav Kadavath, Sandipan Kundu, Amanda Askell, Jackson Kernion, Andy Jones, Anna Chen, Anna Goldie, Azalia Mirhoseini, Cameron McKinnon, Carol Chen, Catherine Olsson, Christopher Olah, Danny Hernandez, Dawn Drain, Deep Ganguli, Dustin Li, Eli Tran-Johnson, Ethan Perez, Jamie Kerr, Jared Mueller, Jeffrey Ladish, Joshua Landau, Kamal Ndousse, Kamile Lukosuite, Liane Lovitt, Michael Sellitto, Nelson Elhage, Nicholas Schiefer, Noemi Mercado, Nova DasSarma, Robert Lasenby, Robin Larson, Sam Ringer, Scott Johnston, Shauna Kravec, Sheer El Showk, Stanislav Fort, Tamera Lanham, Timothy Telleen-Lawton, Tom Conerly, Tom Henighan, Tristan Hume, Samuel R. Bowman, Zac Hatfield-Dodds, Ben Mann, Dario Amodei, Nicholas Joseph, Sam McCandlish, Tom Brown, Jared Kaplan
- **Date:** 15 December 2022
- **Venue:** arXiv (Anthropic)
- **URL:** https://arxiv.org/abs/2212.08073
- **License:** Not specified

## File

- **Local path:** `papers/downloads/arxiv-2212.08073.pdf`
- **SHA-256:** `9a456a07ad346e3372f9867d346f69f5b0f68b4c65f060aca0b8a13fa9d98e83`
- **Size:** 2,000,000 bytes (approx)
- **Downloaded:** 2026-02-28

## Summary

Introduces Constitutional AI (CAI), a method for training a harmless AI assistant through self-improvement guided by a set of natural-language principles (a "constitution"), without requiring human feedback labels for harms. The approach has two phases: a supervised learning phase where the model generates self-critiques and revisions based on constitutional principles, and a reinforcement learning phase (RLAIF — RL from AI Feedback) where a preference model trained on AI-generated evaluations replaces human harmlessness labels.

The resulting RL-CAI model achieves a Pareto improvement over standard RLHF — it is both more helpful and more harmless, and is preferred by crowdworkers. The method demonstrates that about ten simple natural-language principles can effectively steer AI behavior, making the governance of AI systems more transparent and less dependent on large-scale human annotation.

## Relevance to Our Paper

**Seminal.** Key conceptual precedent for the Map's architecture. Core connections:

1. **The constitutional constraint paradigm:** CAI shows that natural-language principles can effectively govern AI behavior. Our tenets function analogously — five explicit philosophical commitments that constrain generation and guide self-review. We extend the paradigm from safety alignment to knowledge production.

2. **Self-critique and revision:** CAI's supervised phase (generate → critique → revise) is structurally parallel to our review layers (generate → pessimistic review → deep review → refine). Both use the same model family to evaluate and improve its own outputs against explicit principles.

3. **The key difference is domain and persistence:** CAI trains a model once using principles; the Map continuously applies principles to an evolving knowledge base. CAI's constitution constrains individual responses; our tenets constrain an entire philosophical corpus over time.

4. **Scaling supervision:** CAI's insight that a small number of principles can replace large-scale human oversight resonates with our architecture — human-directed tenets guide autonomous AI content production.

## Notes

- From Anthropic, with a large author list (50+ contributors)
- The paper's discussion of principle selection acknowledges these were chosen ad hoc and should be refined with broader stakeholder input — a tension the Map addresses by grounding tenets in explicit philosophical commitments
- Both SL and RL phases leverage chain-of-thought reasoning for transparency — related to our use of structured review outputs
- This is one of the most-cited AI alignment papers; establishing the connection strengthens our paper's positioning
