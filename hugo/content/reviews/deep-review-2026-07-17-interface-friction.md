---
ai_contribution: 100
ai_generated_date: 2026-07-17
ai_modified: 2026-07-17 23:05:21+00:00
ai_system: claude-opus-4-8
author: null
concepts: []
created: 2026-07-17
date: &id001 2026-07-17
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - Interface Friction
topics: []
---

**Date**: 2026-07-17
**Article**: [Interface Friction](/concepts/interface-friction/)
**Previous review**: [2026-06-25](/reviews/deep-review-2026-06-25-interface-friction/) (7th deep review overall; prior passes 2026-02-20, 2026-03-19, 2026-04-16, 2026-04-17, 2026-05-28, 2026-06-25)

## Context

Highly converged article. This pass is scoped to the **one substantive delta since the 06-25 ledger**: commit `d3839143c` (2026-06-26) rewrote the choking paragraph in the "Attentional Cost" section, adding **three genuinely-new inline citations** (Beilock & Carr 2001; Gröpel & Mesagno 2019; Smoulder et al. 2024) and their References entries, and reframing the paragraph's calibration. The 06-25 ledger reviewed the *previous* form of that paragraph, which carried **zero citations** — so these three cites have NEVER been web-verified. The only other change since (commit `b2e457215`) is a cosmetic `[[philosophy-of-habit-under-dualism]]` related-article link that bumped `ai_modified` to 2026-07-07; it touched no body prose. All eight pre-existing cites carry the standing 05-28/06-25 publisher-of-record ledger and are byte-identical.

## Pessimistic Analysis Summary

### Critical Issues Found

- **None.**

### §2.4 Publisher-of-Record Web-Verify — the three new citations (first verification)

- **Beilock, S. L., & Carr, T. H. (2001). On the fragility of skilled performance: What governs choking under pressure? *J. Exp. Psychol.: General*, 130(4), 701–725** — **real-correct.** Full tuple confirmed at the APA publisher (xge-1304701.pdf header: "Journal of Experimental Psychology: General 2001. Vol. 130. No. 4. 701–725"); PubMed 11757876. Author order, year, volume, issue, pages all faithful.
- **Gröpel, P., & Mesagno, C. (2019). Choking interventions in sports: A systematic review. *Int. Rev. Sport Exerc. Psychol.*, 12(1), 176–201** — **real-correct.** Confirmed at Taylor & Francis (DOI 10.1080/1750984X.2017.1408134), vol 12 issue 1, pp. 176–201. The **"47 intervention studies" count is accurate, not fabricated**: the review synthesises 47 empirical studies (published to April 2017) and is organised around the distraction vs. self-focus models. The article's phrasing ("distraction/self-focus split confirmed across 47 intervention studies") is a defensible, mildly loose characterisation of a review structured around those two models — not a misattribution; no fix needed.
- **Smoulder, A. L., Marino, P. J., Oby, E. R., et al. (2024). A neural basis of choking under pressure. *Neuron*, 112(20), 3424–3433.e8** — **real-correct.** Confirmed at Cell Press/Neuron (S0896-6273(24)00608-1), PubMed 37090659; vol 112 issue 20, 3424–3433.e8. Authors Smoulder AL, Marino PJ, Oby ER match. **No Denton-2024-style overclaim**: the article says "a motor-cortical substrate located by Smoulder et al. 2024" — "located" faithfully describes the study's finding (motor-cortex planning signals became less distinguishable under jackpot reward). The result is a Rhesus-monkey correlational/observational finding; the article makes no "first to demonstrate" claim and does not misrepresent it as human data. Faithful.

Inline ↔ References cross-reference: all three new inline cites have References entries; no orphans in either direction.

### Empirical-Record Currency Sweep

- `find_superlative_claims` returns empty (0). No superlative empirical claims to currency-check.

### Verbatim Quote Check

- No source quotes anywhere in the article. The only quoted strings are illustrative Map phrasings ("Reach for the cup", "fire motor neuron N₄₅₆₇₈"), not attributed source text. Nothing to verbatim-check or de-quote.

### Calibration Check (evidential-status discipline) — the reframed choking paragraph

- **PASSED — the delta strengthened calibration.** The 06-25 form ended "...active interference, an empirical signature of the same finite, imperfectly coupled channel" — where "empirical signature" flirted with presenting choking as evidence *for* the dualist channel. The 06-26 rewrite corrects this: it now states explicitly that the reading "is an interpretive fit rather than an empirically distinguishable prediction," that "standard motor-control and reward-pressure models ... already predict the degradation," and that interface-friction "redescribes that established result under a dualist ontology rather than discriminating against it." No claim that interface-friction *discriminates* against standard models; no possibility/probability slippage. A tenet-accepting reviewer would not flag this as overstated.

### Reasoning-Mode Classification (§2.6)

- No extended named-opponent refutation. The physicalist is engaged generically and honestly (Mode Three boundary-marking with a Mode Two seed — the explanatory-value question is framed as the open central question, not a claimed refutation). No boundary-substitution; no editor-vocabulary leakage in prose.

### Attribution / Self-Contradiction

- Original Map concept; Map-specific moves (tenets, quantum Zeno) labelled as the Map's reading throughout. No misattribution, no source/Map conflation, no self-contradiction.

## Optimistic Analysis Summary

### Strengths Preserved

- The article's disciplined "interpretive, not predictive" self-framing is now consistently applied to the choking material as well, closing the one spot where an evidence-elevation reading could have crept in. This is the corpus's calibration discipline working as intended.
- Cross-link `[[empirical-phenomena-mental-causation|placebo and choking]]` resolves — target exists, title is literally "Empirical Phenomena of Mental Causation: Placebo and Choking." Anchor faithful.

### Enhancements Made

- None needed. All three new citations verified faithful; calibration sound; no fixes applied.

## Remaining Items

None.

## Stability Notes

- The physicalist "friction merely restates neural facts in dualist vocabulary" objection is bedrock framework-boundary disagreement — the article concedes it openly as the central open question. Do NOT re-flag as critical.
- Seven prior review files; convergence damping is heavy. This pass ran solely to first-verify the three 06-26 citations. All real-correct. Future passes should treat the References block as web-verified through 2026-07-17 unless the body/References change again.

## Frontmatter Disposition

Genuine no-op after real scrutiny: `last_deep_review` bumped to 2026-07-17T23:05:21+00:00; `ai_modified` held at HEAD (2026-07-07T22:02:24+00:00); `ai_system` held (claude-opus-4-6). No body edits.