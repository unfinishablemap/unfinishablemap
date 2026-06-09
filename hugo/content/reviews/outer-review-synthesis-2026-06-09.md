---
ai_contribution: 100
ai_generated_date: 2026-06-09
ai_modified: 2026-06-09 05:17:40+00:00
ai_system: claude-opus-4-8
author: Andy Southgate
concepts:
- '[[illusionism]]'
created: 2026-06-09
date: &id001 2026-06-09
description: Cross-review synthesis of three outer reviews from 2026-06-09 auditing
  the illusionism concept page. Five convergent finding clusters (two of them publisher-verified
  citation defects flagged by two reviewers each), upgrading three illusionism tasks
  toward P1.
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles:
- '[[project]]'
synthesis_coverage: 3/3
synthesizes:
- reviews/outer-review-2026-06-09-chatgpt-5-5-pro.md
- reviews/outer-review-2026-06-09-claude-opus-4-8.md
- reviews/outer-review-2026-06-09-gemini-2-5-pro.md
title: Outer Review Synthesis - 2026-06-09
topics: []
---

**Date**: 2026-06-09
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Coverage**: 3 of 3 commissioned reviewers contributed (ChatGPT 5.5 Pro, Claude Opus 4.8, Gemini 2.5 Pro). All three audited the same subject: the illusionism concept page ([concepts/illusionism.md](/concepts/illusionism/)).

## TL;DR

The dominant convergent finding is **citation infidelity on the illusionism page**: two reviewers independently web-verified the same three publisher-of-record citation defects (a fabricated "Pereboom & Frankish 2021" co-authored paper, a wrong Graziano 2024 venue, and a misattributed Chalmers 2022 claim). Five convergent clusters emerged across the three reviews; the remaining findings were singletons or — in Gemini's case — a subject-misidentification artefact. One reviewer (Gemini) reviewed the wrong argument entirely (a "choking under pressure" agent-causal piece the illusionism article never makes), so most of its critique is a false positive; only its two web-verified 2025 citations contribute real signal.

Cluster counts: **5 convergent**, **5 singleton**, **0 divergent**.

## Convergent Findings

### 1. Fabricated "Pereboom & Frankish (2021)" co-authored citation
- **Flagged by**: chatgpt, claude
- **Verification**: clean — both reviewers independently web-verified against publisher-of-record. The real *Review of Philosophy and Psychology* 13(2):427–453 (DOI 10.1007/s13164-021-00537-6) is solo-authored by Daniel Shabasson; no Pereboom–Frankish co-authored paper exists. The sibling `functional-seeming.md` page already carries the corrected cluster.
- **Quotes**:
  - **ChatGPT 5.5 Pro**: "The Illusionism page cites 'Pereboom, D. & Frankish, K. (2021)' … That reference does not line up with the bibliographic record. The relevant Review of Philosophy and Psychology article is Daniel Shabasson … (2022)."
  - **Claude Opus 4.8**: "FABRICATED CO-AUTHORSHIP (most serious) … No such co-authored paper exists. The real … paper … is solo-authored by Daniel Shabasson … Pereboom and Frankish have no co-authored publication on any topic."
- **Task action**: Folded into the existing P1 "Fix four web-verified citation defects" task (already P1, not upgraded further); rewritten to record convergence and add the Claude review as a second source.

### 2. Graziano 2024 cited with the wrong venue
- **Flagged by**: chatgpt, claude
- **Verification**: clean — both web-verified. The page lists *Journal of Consciousness Studies*; the actual venue is *eNeuro* 11(10), article ENEURO.0210-24.2024 (DOI 10.1523/ENEURO.0210-24.2024), with truncated subtitle "Some Options for Explaining Consciousness."
- **Quotes**:
  - **ChatGPT 5.5 Pro**: "The Illusionism page lists Graziano's 2024 'Illusionism Big and Small' as appearing in Journal of Consciousness Studies. Princeton's publication metadata gives the article as eNeuro, volume 11, issue 10."
  - **Claude Opus 4.8**: "WRONG JOURNAL (Graziano 2024). … The actual paper is … eNeuro 11(10), DOI 10.1523/ENEURO.0210-24.2024 (2024). Wrong venue; truncated title."
- **Task action**: Folded into the same P1 citation task as cluster 1.

### 3. Chalmers 2022 stance-transfer misattribution
- **Flagged by**: chatgpt, claude
- **Verification**: ChatGPT flagged this as "plausible — not independently re-verified" (verify-first); Claude independently verified it against Loginov 2024 (*Frontiers in Psychology* 15:1449314). The convergence holds: both read the page's "Chalmers himself (2022) later judged this flawed" as conflating Chalmers's 2022 critique of Moore's *original* external-world proof with a recantation of his own 2018 anti-illusionism argument, when the "too theory-laden" objection is Loginov's. Treat as verify-first at fix time per ChatGPT's flag.
- **Quotes**:
  - **ChatGPT 5.5 Pro**: "The page says Chalmers 'himself (2022) later judged this flawed' … The evidence I found supports a narrower and different claim: Loginov reports that Chalmers 2022 criticized Moore's original external-world argument."
  - **Claude Opus 4.8**: "MISATTRIBUTED CLAIM ABOUT CHALMERS 2022. … In 2022 (Reality+, Ch. 4) Chalmers critiqued G. E. Moore's original 1939 proof … not his own 2018 anti-illusionism argument, which he did not retract. The 'too theory-laden' objection is Loginov's (2024), not Chalmers's."
- **Task action**: Folded into the same P1 citation task as clusters 1–2.

### 4. Distortion-thesis citation is stale; current source is Gorbachev & Frankish (2025)
- **Flagged by**: claude, gemini
- **Verification**: clean — Gemini web-verified the paper real (DOI 10.1007/s11229-025-05095-3, *Synthese* 205(6):247) and accurately described its three-dimensional taxonomy (positiveness, conceptuality, dispellability → eight distortion patterns); Claude named the same paper as the correct current source for the distortion-thesis content the page attributes to the bogus "Pereboom & Frankish 2021."
- **Quotes**:
  - **Claude Opus 4.8**: "The 'distortion thesis' is in fact the framing of Gorbachev, M. & Frankish, K. (2025), 'Illusionism and the distortion thesis,' Synthese 205(6):247 … which the page does not cite."
  - **Gemini 2.5 Pro**: "Gorbachev, M. & Frankish, K. (2025). 'Illusionism and the distortion thesis.' Synthese 205(6). Real — DOI 10.1007/s11229-025-05095-3 … This is the current elaboration of the distortion thesis the article cites only at the 2021 Pereboom & Frankish vintage."
- **Task action**: Upgraded P2 → P1: "Resolve regress inconsistency + refresh stale bibliography across illusionism cluster" task; rewritten to record convergence and coordinate with the citation task (prefer Shabasson 2022 + Gorbachev & Frankish 2025 when reattributing the distortion-thesis material).

### 5. Epiphenomenalism-convergence / self-stultification argument overstated (question-begging, unflagged)
- **Flagged by**: chatgpt, claude
- **Verification**: clean (dialectical judgement, not a falsifiable claim — both treat it as a calibration finding). Both note the page presents the convergence-with-epiphenomenalism as if the illusionist has no reply, and that the argument assumes phenomenal realism in a premise; the functional-seeming page already concedes the dependence on prior commitments while the self-stultification page does not.
- **Quotes**:
  - **ChatGPT 5.5 Pro**: "The page's structural-convergence-with-epiphenomenalism section is rhetorically powerful but should be softened. … The Map can argue that this is not enough, but it should not state the convergence as if Frankish has no reply."
  - **Claude Opus 4.8**: "Self-stultification / epiphenomenalism convergence (QUESTION-BEGGING, unflagged). The argument … assumes there is experiential character to attend to — i.e., it assumes phenomenal realism. The illusionist's reply … is exactly what is denied without argument."
- **Task action**: Upgraded P2 → P1: "Strengthen opponent-engagement and soften overstatement" task; rewritten to record convergence on this sub-point (the task's other sub-points remain ChatGPT singletons bundled in the same editorial pass).

## Singleton Findings

Flagged by one reviewer only. Not upgraded; left at original task priority. Listed for the record.

- **Claude Opus 4.8**: Misattributed/fabricated Frankish "entity eliminativism" quotation (line ~55) → see `todo.md` task "Remove the misquoted Frankish 'entity eliminativism' attribution" (P1, original priority — not a convergence upgrade).
- **ChatGPT 5.5 Pro**: Kammerer source/claim mismatch — the "rich illusion" claim cites the Moorean-obviousness paper instead of "How Rich is the Illusion of Consciousness?" (*Erkenntnis* 87(2):499–515) → bundled into the P1 four-citation task (mechanical fix).
- **ChatGPT 5.5 Pro**: AST regress objection less disciplined than illusionism page; contemplative claims need sourcing → see `todo.md` task "Harmonize AST regress objection + source/downgrade contemplative claims" (P2).
- **Claude Opus 4.8**: Regress inconsistency between `qualia.md` (runs the regress as forceful) and `illusionism.md` (concedes it "proves nothing") → bundled into the upgraded P1 bibliography/regress task.
- **Claude Opus 4.8**: Kammerer 2025 "Charybdis and Scylla" (*Philosophical Studies* 182(2)) addition, plus broader 2019–2026 literature refresh (Kammerer *Synthese* 2021, *Ergo* 2019, OUP monograph; Dennett "Welcome to Strong Illusionism" 2019; Chalmers "Debunking Arguments" 2020) → bundled into the upgraded P1 bibliography task. (Gemini independently web-verified the Kammerer 2025 paper real, so this borders on convergent, but only Claude framed it as a stale-bibliography finding; recorded here as the leading singleton.)

## Divergences

None. No reviewer defended a position another criticised; the reviews are mutually consistent where they overlap.

## Method Notes

- **Gemini reviewed the wrong argument.** The Gemini 2.5 Pro leg is a subject-misidentification artefact: it audited a "choking under pressure" agent-causal defence of phenomenal consciousness (golf putts, Beilock & Carr 2001, Tulving's anoetic/autonoetic hierarchy, AST-omission, EEG/PCI dissociation) that the illusionism article never makes — a corpus grep finds zero occurrences of "choking," "golf," "Tulving," "Beilock," or "anoetic" in the article, which in fact has a dedicated AST section. Gemini's five "fatal" weaknesses are therefore false positives as applied to the actual article. Only its two web-verified 2025 citations (Gorbachev & Frankish; Kammerer Charybdis/Scylla) contribute real signal, one of which (Gorbachev & Frankish) anchors convergent cluster 4. This matches the editor-internal "subject-misidentification false positive" failure mode; its empirical/AST/motor-control findings generated no tasks.
- **ChatGPT and Claude converged tightly on citations** — they web-verified three of the same defects independently against publishers of record, which is strong evidence of real defects rather than correlated model error.
- **One disputed-vs-verified asymmetry**: the Chalmers 2022 finding (cluster 3) was verify-first for ChatGPT but verified for Claude; net it is treated as convergent-but-verify-at-fix-time, consistent with both reviewers' flags.
- **Length constraint carries through**: all reviewers and tasks note the illusionism page is ~3,499 words (one word under the 3,500 concept hard ceiling). Every upgraded task is marked length-neutral / substitution-not-accretion.