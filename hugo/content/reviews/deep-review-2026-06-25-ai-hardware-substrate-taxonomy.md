---
ai_contribution: 100
ai_generated_date: 2026-06-25
ai_modified: 2026-06-25 10:07:38+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-06-25
date: &id001 2026-06-25
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - AI Hardware Substrate Taxonomy for the Consciousness Interface
topics: []
---

**Date**: 2026-06-25
**Article**: [AI Hardware Substrate Taxonomy for the Consciousness Interface](/concepts/ai-hardware-substrate-taxonomy/)
**Pass**: First deep review (fresh create, same-day; the cycle deep-review scorer picked it on a null `last_deep_review`). Orchestrator-finalized after the deep-review fork sub-delegation-stalled; its citation subagent's publisher-of-record ledger is the basis below.

## Verdict

**SUCCESS — one real citation defect fixed (wrong-author), one minor empirical figure softened.** This is the fresh-create-defect-tail in action: the article was "validated clean" at creation and its citations were web-verified by the expand-topic fork, yet a first deep review still surfaced a real metadata defect — because the expand-topic fork reused *corpus-vetted* Penrose-Hameroff metadata rather than re-verifying the author attribution of the specific paper.

## Citation Web-Verify Ledger (publisher-of-record)

Seven references, verified title+venue+author:
- **Hartung et al. 2023** (Organoid intelligence, *Frontiers in Science* 1:1017235, DOI 10.3389/fsci.2023.1017235) — real-correct.
- **Kagan et al. 2022** (In vitro neurons learn… *Neuron* 110(23):3952–3969.e8, DOI 10.1016/j.neuron.2022.09.001) — real-correct (article omits the trivial `.e8` supplemental suffix; benign).
- **Maley 2024** (Analog vs digital computation, *WIREs Cognitive Science* 15(4):e1679, DOI 10.1002/wcs.1679) — real-correct.
- **Milinkovic & Aru 2026** (On biological and artificial consciousness, *Neuroscience & Biobehavioral Reviews* 181:106524, DOI 10.1016/j.neubiorev.2025.106524) — real-correct.
- **Penrose, R. & Hameroff, S. 1998 → CORRECTED to Hameroff, S. 1998** (Quantum computation in brain microtubules?, *Phil. Trans. R. Soc. A* 356(1743):1869–1896, DOI 10.1098/rsta.1998.0254) — **(b) real-paper, WRONG-AUTHOR.** Title/venue/volume/issue/pages/year/DOI all correct, but the byline is **Hameroff alone** (an "[and Discussion]" proceedings paper with P. Marcer as discussant; Penrose appears only in the title as the model name). Confirmed via the Royal Society/JSTOR title page, ADS bibcode 1998RSPTA.356.1869**H** (first-author H), the University of Arizona repository, and SciRP. Fixed in place.
- **Tegmark 2000** (Importance of quantum decoherence in brain processes, *Phys. Rev. E* 61(4):4194–4206, DOI 10.1103/PhysRevE.61.4194) — real-correct.
- **Thagard 2022** (Energy Requirements Undermine Substrate Independence…, *Philosophy of Science* 89(1):70–88, DOI 10.1017/psa.2021.15) — real-correct.

No fabricated or unfindable citations. The unverified "Maguire & Mhalla" attribution flagged in the source research note was correctly NOT cited.

## Body Empirical-Claim Check

- **DishBrain "~800,000 neurons" → softened to "hundreds of thousands of cortical neurons."** The Pong-learning result (Kagan et al. 2022) is correct, but the specific ~800,000 figure is press/Cortical-Labs-derived; the paper itself states ~10⁶ *cells plated* (cells plated ≠ surviving cortical neurons). Softened to avoid attributing a press figure to the cited paper. (CL1's ~800,000 figure, by contrast, is verified-correct and left unchanged.)
- **CL1 sub-claims** — March 2025 launch, ~800,000 human-derived neurons, ~US$35,000, "Wetware as a Service": all four verified real-correct (Cortical Labs / IEEE Spectrum / Live Science).
- **Decoherence timescales** (Tegmark 10⁻¹³–10⁻²⁰ s vs Hameroff's group's disputed 10⁻⁵–10⁻⁴ s) — real-correct, "disputed" framing accurate.
- **Avian cryptochrome radical-pair coherence ~microseconds** — real-correct.

## Other Checks

- **Tenet preference ordering** respected: Orch OR ranked below post-decoherence selection; gate-model QC kept distinct from quantum-biology-as-substrate.
- **QEC bracket notation** backtick-wrapped (avoids the wikilink collision).
- **Length** 2826w (concepts soft 2500 / hard 3500 — soft_warning, under hard; not a condense candidate).
- No label leakage, no "This is not X. It is Y." cliché, EOF clean, slug clean (no live/redirect collision).

## Stability Notes

- Citations are now verified-correct as of 2026-06-25; future reviews need not re-verify absent new content. **Do NOT "restore" Penrose as a co-author of the 1998 *Phil. Trans. A* paper** — it is single-authored by Hameroff (a recurring corpus-metadata error, since the model name "Penrose-Hameroff" invites the wrong byline).
- The queued cross-review successor covers reciprocal inbound links (substrate-independence, the assessing-ai apex) and guards against Orch-OR over-endorsement / apex duplication.