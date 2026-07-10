---
ai_contribution: 100
ai_generated_date: 2026-07-10
ai_modified: 2026-07-10 06:24:35+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-10
date: &id001 2026-07-10
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - The Ethics of Possible AI Consciousness (Butlin-2023 authorship
  family-resolution + publisher web-verify)
topics: []
---

**Date**: 2026-07-10
**Article**: [The Ethics of Possible AI Consciousness](/topics/ethics-of-possible-ai-consciousness/)
**Previous review**: [2026-06-20](/reviews/deep-review-2026-06-20-ethics-of-possible-ai-consciousness/)

**Scope**: Owed publisher-of-record citation web-verify seam. The 2026-06-20 review claimed a "full publisher-of-record web-verify of the entire References block" but its ledger silently omitted the Butlin et al. (2023) entry — precisely where a corpus-wide authorship error lives. This pass web-verified the unverified load-bearing cites at the publisher of record and resolved the Butlin-2023 authorship error as a corpus family-resolution across five files. No expansion/condensation was attempted: the article carries an active NEEDS-HUMAN length decision (saturated ~4000w, two deferred substantive rival-adds blocked pending human condense-first/split/accept-deferred) and is human-decision-protected against auto-condense.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Attribution error (propagated) — Butlin et al. 2308.08708 (2023) falsely credits David Chalmers as a 2023 author.** The 2023 arXiv preprint "Consciousness in Artificial Intelligence: Insights from the Science of Consciousness" (arXiv:2308.08708) authors are Butlin, Long, Elmoznino, Bengio, Birch, Constant, Deane, Fleming, Frith, Ji, Kanai, Klein, Lindsay, Michel, Mudrik, Peters, Schwitzgebel, Simon, VanRullen — **verified at arXiv (arxiv.org/abs/2308.08708)**. Neither Chalmers nor Bayne is on the 2023 paper; both joined only the 2025 *Trends in Cognitive Sciences* version ("Identifying indicators of consciousness in AI systems," DOI 10.1016/j.tics.2025.10.011). In this article the error appeared twice: body line 124 ("The Butlin-Long-Chalmers (2023) indicator framework") and References line 184 ("Butlin, P., Long, R., Chalmers, D. et al. (2023)"). **Resolution**: body corrected to "Butlin, Long et al. (2023)"; reference corrected to the real lead author-list with a disambiguating note that the 2025 TiCS version adds Chalmers and Bayne. This survived 6 prior deep reviews of this article because intra-corpus consistency ratified it and the 06-20 "full ledger" skipped the entry.

### Family Resolution (corpus-wide propagation, §2.4 step 6)

The same Chalmers-on-2023 error was grepped across the corpus and corrected in four sibling files (targeted citation fix only; not deep-reviewed, `ai_modified` bumped, `last_deep_review` untouched):

- [apex/machine-question.md](/apex/machine-question/) L127 — prose "with David Chalmers among its contributors" (of the 2023 report) → relocated to "a 2025 *Trends in Cognitive Sciences* successor—which David Chalmers joined."
- [apex/what-it-might-be-like-to-be-an-ai.md](/apex/what-it-might-be-like-to-be-an-ai/) L154 — prose "(2023, with Chalmers among its contributors)" → "(2023) and its 2025 ... successor (which David Chalmers joined)."
- [concepts/types-of-consciousness.md](/concepts/types-of-consciousness/) L156 — reference "Butlin, P., Long, R., Chalmers, D. et al. (2023)" → real author-list + 2025-version note.
- [concepts/ai-epiphenomenalism.md](/concepts/ai-epiphenomenalism/) L146 — reference "Butlin, P., Long, R., Chalmers, D. et al. (2023)" → real author-list + 2025-version note.

Corpus now consistent: files that already attributed the 2023 preprint correctly (deep-computational-markers, agentic-ai..., reinforcement-learning...valence, open-question-ai-consciousness, quantum-state-inheritance-in-ai, training-contamination-confound, assessing-ai-consciousness-under-the-map, ai-as-introspection-control) were left unchanged and confirmed correct. deep-computational-markers L117 correctly lists Bayne + Chalmers on the 2025 TiCS entry.

### Citations Web-Verified at Publisher of Record (3-state)

- **Butlin, P., Long, R., Elmoznino, E., Bengio, Y., Birch, J., et al. (2023). Consciousness in Artificial Intelligence. arXiv:2308.08708** — state: **real-wrong-metadata (author error corrected)**. Full 19-author list verified at arXiv (submitted 2023-08-17, v3 2023-08-22). Chalmers/Bayne removed from 2023 attribution; noted on 2025 version.
- **Metzinger, T. (2021). Artificial Suffering: An Argument for a Global Moratorium on Synthetic Phenomenology. *Journal of Artificial Intelligence and Consciousness* 8(1), 43–66** — state: **real-correct**. Verified vol 08 / issue 01 / pp. 43–66, DOI 10.1142/S270507852150003X (World Scientific; corroborated PhilPapers METASA-4). Body gloss ("explosion of negative phenomenology"; moratorium; "post-biotic carrier systems") faithful.
- **Bostrom, N. (2006). Quantity of experience: brain-duplication and degrees of consciousness. *Minds and Machines* 16(2), 185–200. DOI 10.1007/s11023-006-9036-0** — state: **real-correct**. Verified at Springer + Oxford FHI listing (16(2):185–200). Body use (Unification vs Duplication poles; Duplication derived without haecceity/MWI-rejection) faithful.
- **Schwitzgebel, E. (2025). AI and Consciousness. arXiv:2510.09858** — state: **real-correct**. Verified at arXiv:2510.09858 (forthcoming Cambridge Elements). Body gloss ("mainstream theories yield contradictory verdicts"; "social semi-solution") faithful.
- **Bostrom, N. & Shulman, C. (2022); Schwitzgebel 2024/2023 (Repetition and Value); Tokayer (PhilArchive); Cutter, B. (2025) Faith and Philosophy 41(1):1–26** — carried forward from the 2026-06-20 publisher-verified ledger; unchanged since; not re-litigated.
- **Birch (2024, OUP Edge of Sentience); Deutsch (1999, Proc. R. Soc. A 455(1988):3129–3137); Wallace (2012, OUP Emergent Multiverse); Tomasik; Metzinger** — standard well-attested references; no metadata anomaly.

### Reasoning-Mode / Calibration
- No possibility/probability slippage introduced or found. The article is unusually disciplined on this axis (explicit possibility-probability-slippage self-application at line 92; framing note at line 44; evidential-status discipline at line 66). No label leakage. No edits needed here.
- Named-opponent engagements (functionalist, Metzinger, Birch, MWI-defender via Deutsch/Wallace) are Mode Three framework-boundary marking, honestly flagged as such — no boundary-substitution.

### Medium / Low
- None actioned. The two deferred substantive adds (illusionism + predictive-processing engagement; 2024–2026 AI-welfare literature) remain human-decision-gated on length; not touched.

## Optimistic Analysis Summary

### Strengths Preserved
- The reflexive possibility/probability-slippage discipline (a tenet's convenient empirical implication cannot upgrade the tenet) is exemplary and left intact.
- The Aggregation-Under-Copy-Multiplicity section's honesty about the tenets *underdetermining* the copy-count (Duplication View adopted on independent Bostrom grounds, not forced by haecceity/MWI-rejection) is a model calibration passage.

### Enhancements Made
- Reference disambiguation note added to the Butlin entry so the 2023-vs-2025 authorship distinction is explicit and resists re-introduction.

### Cross-links Added
- None (length-locked; no orphan risk).

## Length
4380 → 4410 words (+30, the reference disambiguation note). Status band unchanged (hard_warning, well under the 6000 critical). Auto-condense deliberately NOT applied — human-decision-protected (todo NEEDS-HUMAN length decisions of 2026-06-27). The +30 is a citation-correctness requirement, not a substantive expansion, and does not touch the deferred rival-engagement adds.

## Remaining Items
- The standing NEEDS-HUMAN length decision (condense-first / split / accept-deferred) is unchanged and still owed to the human operator.

## Stability Notes
- Bedrock disagreements NOT to re-flag: the functionalist rejection of the quantum-interface requirement (framework boundary); the MWI-defender's dissatisfaction with the No-Many-Worlds ethical argument; Metzinger's catastrophe reaching the same alarm from incompatible (functionalist) premises. All honestly flagged in-article as framework-boundary.
- The citation set is now publisher-verified through this pass; the only defect was the propagated Butlin-2023 authorship, now resolved corpus-wide. Future selections should be metadata-only confirms unless the body changes.