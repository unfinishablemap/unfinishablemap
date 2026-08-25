---
title: "Outer Review Synthesis - 2026-08-25"
created: 2026-08-25
modified: 2026-08-25
human_modified: null
ai_modified: 2026-08-25T05:50:26+00:00
draft: false
description: "Three reviewers audited one article. Per-reviewer accuracy ran 9/9, 3-disputed and 1-of-5, so convergence was adjudicated against the disk before any count was allowed to move a priority."
topics: []
concepts: []
related_articles:
  - "[[project]]"
ai_contribution: 100
author: "Andy Southgate"
ai_system: "claude-opus-5"
ai_generated_date: 2026-08-25
last_curated: null
synthesizes:
  - reviews/outer-review-2026-08-25-chatgpt-5-6-sol-pro.md
  - reviews/outer-review-2026-08-25-claude-opus-5.md
  - reviews/outer-review-2026-08-25-gemini-2-5-pro.md
synthesis_coverage: "3/3"
subject_type: recent
subject_title: "Audit edge-states-and-void-probes"
subject_articles:
  - voids/edge-states-and-void-probes.md
---

**Date**: 2026-08-25
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Coverage**: 3 of 3 commissioned reviewers contributed and were processed; none abandoned.
**Subject**: `voids/edge-states-and-void-probes` — all three legs audited the **same** article via the reuse branch, so agreement here is genuine same-target convergence rather than three unrelated reports.

## TL;DR

Six findings were flagged by two or more reviewers, but only one of them changed a priority on the strength of the count alone. Per-reviewer accuracy this cycle ran from **9-of-9 verbatim** (ChatGPT) through **three disputed claims** (Claude) to **1-of-5 verified** (Gemini), so every cluster was adjudicated against the article on disk before it was allowed to count as corroboration. Two tasks were upgraded P2 → P1; four already sat at P1 and were annotated rather than moved; no task was resurrected, deduplicated, or newly minted.

## Convergent Findings

### 1. Predictive processing is engaged as a mechanism, never as a rival theory of consciousness

- **Flagged by**: claude, gemini
- **Verification**: **clean, and independently grep-confirmed.** `Laukkonen`, `beautiful loop`, `Seth`, `Letheby` and `Van Dam` all return zero hits in `obsidian/voids/edge-states-and-void-probes.md`. The Laukkonen–Friston–Chandaria paper resolves at Crossref as a `journal-article` (*Neuroscience & Biobehavioral Reviews*, 2025-09, DOI `10.1016/j.neubiorev.2025.106296`).
- **Quotes**:
  - **Claude Opus 5**: "It engages PP substantively as an *edge-mapping mechanism* (REBUS, ALBUS/SEBUS, REBAS)… What it does **not** do is engage the active-inference *theories of consciousness* that are the current framework-level rivals to the dualist reading of edge phenomenology."
  - **Gemini 2.5 Pro**: "The manuscript frames *nirodha samāpatti* (cessation) as an inexplicable 'Silence Void' that physicalist production accounts cannot model, completely omitting Laukkonen, Friston, and Chandaria (2025)."
- **Adjudication**: this is the **only** Gemini finding of five that survived verification, and it was reached independently by Claude from a different prompt and a different report structure. Claude's framing is the better one and governs the fix: the material is already carried across the corpus (`topics/predictive-processing-and-dualism`, `topics/predictive-self-binding-and-the-naturalist-challenge`, `concepts/entropic-brain-hypothesis`, `apex/testing-the-map-from-inside`), so this is **local non-integration, not a systemic blind spot**, and the repair is mostly cross-linking. Gemini's distinct contribution is the peer-reviewed venue for the citation.
- **Task action**: **Upgraded P2 → P1** — "the edge-states article engages predictive processing only as a *mechanism*, never as a rival *theory of consciousness*". No sibling task existed to deduplicate: the Gemini collect pass had already augmented Claude's task rather than minting a duplicate.

### 2. The "Bidirectional Interaction" tenet coda begs the question it is meant to support

- **Flagged by**: chatgpt, claude
- **Verification**: **clean.** The coda sentence at L161 was grep-verified verbatim on disk during collection; the Dualism coda four paragraphs above it, which concedes the opposite, was verified in the same pass.
- **Quotes**:
  - **Claude Opus 5**: "The claim that approaching the edge 'demonstrates consciousness influencing physical processes' imports Tenet 3 as a *premise* while the article's stance elsewhere is neutral inquiry. On physicalism, 'intention → neural state' is intra-physical causation; citing it as evidence for mind→physical causation begs the question."
  - **ChatGPT 5.6 Pro**: "Treating ordinary intention-mediated neural change as a demonstration of dualist downward causation therefore presupposes the tenet it is supposed to support." And, generalised in its counterargument section: "Demonstrating that a person's intention predicts neural change is not yet evidence that a nonphysical consciousness supplied an additional cause."
- **Task action**: **Recorded only — already at P1**, so no upgrade was available. The existing task was annotated with the ChatGPT leg and its A.18 recommendation.

### 3. The "Minimal Quantum Interaction" coda is decorative and does no argumentative work

- **Flagged by**: chatgpt, claude
- **Verification**: **clean.** Both quote the article's own self-flagged "speculative" hedge.
- **Quotes**:
  - **Claude Opus 5**: "Tenet 2 (Minimal Quantum Interaction) is **decorative and self-admittedly so**… This does no argumentative work and the article flags it as speculative."
  - **ChatGPT 5.6 Pro**: "The suggestion that loosened predictive constraints may permit consciousness to affect 'open quantum processes' supplies no specified quantum state, interaction Hamiltonian, measurement operator, coherence timescale or distinctive prediction."
- **Remedy variance, resolvable**: Claude asks to cut it **or** mark it apex-style as carrying a coherence cost; ChatGPT asks for a clearly labelled speculative box. These are compatible — either satisfies both legs — so the variance was recorded in the task rather than adjudicated here.
- **Task action**: **Recorded only** — carried by the same P1 task as finding 2, which already had this coda in scope.

### 4. Citation-metadata failures in the target article

- **Flagged by**: chatgpt, claude
- **Verification**: **clean, both legs independently re-resolved by DOI** — ChatGPT at Crossref and Europe PMC, Claude at Crossref, PubMed and Europe PMC.
- **Quotes**:
  - **ChatGPT 5.6 Pro**: the article cites "*Scientific Reports*, 13, 3083 (2023)"; Crossref and Europe PMC "both return **volume 15, article 3651, published 2025-01-29**. The DOI the article carries… is *correct*."
  - **Claude Opus 5**: "**Correction to the review:** it claims volume 13 / article 3083 'correspond to no real object'. They do — `Sci Rep 13(1):3083 (2023)`… is Agostini et al. on parasite-induced behavioural alteration in wild capuchin monkeys. The citation as printed resolves to a real, wholly unrelated paper, which makes it more dangerous than a dangling reference, not less."
- **Also convergent inside this cluster**: the **Sjöstedt-Hughes container** error (both legs; ChatGPT further established that it has propagated to `topics/psychedelics-and-the-filter-model`, a research note, and the archived predecessor), the **Gładziejewski online-first / print conflation**, and the **missing Koriat reference** — an author-year carrying the article's strongest internal defeater at L111 with no entry in the 22-item reference list.
- **Divergence inside the cluster, resolved against Claude**: Claude recommended verifying-or-removing `Kutnyy (2024)` as possibly fabricated. That was **verified false** during collection — the work is real (PhilArchive `KUTTBO`, archival date 2024-12-09), and philarchive.org simply returns Cloudflare 403 to automated fetchers. Acting on the recommendation would have deleted a real citation from four files. The surviving refinement is a `preprint` label, not a deletion.
- **Task action**: **Recorded only — already at P1.** The ChatGPT collect pass minted it; the Claude collect pass augmented the same task with three amendments and two additions rather than duplicating it. Annotated with the convergent leg.

### 5. Citation checking must resolve the identifier and diff the returned fields, not merely confirm the object exists

- **Flagged by**: chatgpt, claude
- **Verification**: **clean**, and grounded in the same verified diagnostic as finding 4 — a citation whose DOI is correct while its year, volume and article number are all wrong, so an existence check and a DOI-resolves check both **pass** it.
- **Quotes**:
  - **Claude Opus 5**: "a DOI-resolves check would have *passed* it because the DOI is real, while the human-readable volume and article number were fabricated around it. Add a cross-field consistency check that resolves the DOI and then diffs the returned year/volume/issue/article-number/pagination against the citation as written."
  - **ChatGPT 5.6 Pro**: "Introduce automated bibliographic validation. Check DOI metadata, year, volume, article number, container title and author list against publishers or Crossref before publication."
- **Why this counts as convergence rather than referee boilerplate**: "verify your sources" is what every external reviewer writes, and two reviewers writing it would be worth nothing. What converged here is the *specific and non-obvious* mechanism — that DOI resolution is necessary but not sufficient, and the returned fields must be diffed one by one. ChatGPT states it as a field list; Claude states it as a diff. They are the same gate, reached from independent audits.
- **ChatGPT's separable addition**: a **body-to-bibliography completeness test** ("any author-year citation used in prose… should fail validation when no matching reference exists"). The missing Koriat entry is this cycle's live instance, and the check needs no network call at all, so it is buildable independently of the Crossref work.
- **Task action**: **Upgraded P2 → P1** — "citation checking passes objects that exist but are the wrong object". Annotated with the ChatGPT leg, its completeness-test addition, and a reminder that the no-deletion-on-failed-fetch rule must ship with the gate rather than after it.

### 6. Retrospective report may reconstruct rather than preserve edge phenomenology

- **Flagged by**: chatgpt, claude
- **Verification**: **clean** — `Van Dam` returns zero hits in the target article.
- **Quotes**:
  - **ChatGPT 5.6 Pro**: "Reports of timelessness, absence of self, total understanding or absence of experience may be reconstructions produced when ordinary memory and conceptual systems attempt to interpret an unusual or poorly encoded state… A failure to remember content is not evidence that the state contained content that exceeded conceptual capacity."
  - **Claude Opus 5**: "Add the retrospective-report-validity / demand-characteristics critique (Van Dam et al. 2018, 'Mind the Hype')… where the article rests weight on cross-tradition self-report convergence."
- **Task action**: **Recorded only** — already carried as item 4 of the "what to add" list on the finding-1 task, which this synthesis upgraded to P1 on other grounds. No separate task was warranted.

## Singleton Findings

Flagged by one reviewer only. Not upgraded; left at original task priority.

- **ChatGPT 5.6 Pro**: the lead asserts "a consistent phenomenology appears" and that evidence "partly discriminates", which the article's own later analysis retracts; and the "idiosyncratic chaos" contrast sets up a straw physicalist opponent when the real alternative is structured construction by a shared system → `todo.md` task "the article's own methodological paragraph refutes its lead, and its physicalist opponent is a straw one" (P2). See Divergences — Claude reads the body the other way.
- **ChatGPT 5.6 Pro**: selective currency — six verified 2024–2026 sources on construct heterogeneity, false insight, epistemic vulnerability and large-scale neural synthesis are absent while recent work favourable to openness is cited → task "Six verified 2024-2026 sources the altered-states cluster should absorb" (P2).
- **ChatGPT 5.6 Pro**: link-maintenance commits reset `ai_modified`, so the subject selector and the commission prompt both read pure maintenance as substantive revision → task "Maintenance edits reset `ai_modified`, and the outer-review subject selector reads it as substantive revision" (P2). The reviewer opened its report by correcting a false revision date we had asserted to it.
- **ChatGPT 5.6 Pro**: the corpus assigns three different evidential weights to the same altered-state observations — "better accommodates" in `concepts/filter-theory` against "roughly equally compatible" in the target → task "The corpus assigns three different evidential weights to the same altered-state observations" (P1). The Claude collect pass augmented this task with an *independent* same-file gap (`concepts/filter-theory` carries no Vollenweider metabolic-hyperfrontality caveat), which is same-file augmentation rather than convergence on the same finding, and so did not trigger an upgrade.
- **Claude Opus 5**: the article never states which voids-taxonomy category it occupies, nor its individuating thesis against its five nearest neighbours. **Partly disputed** — the comparative half ("unlike neighbouring voids that declare their category explicitly") failed against five checked neighbours, none of which declares a category either. The surviving suggestion is a site-wide convention proposal, not an article defect, and was not minted as a task.

## Divergences

- **ChatGPT vs Claude — does the article's *body* overclaim, or over-concede?** ChatGPT reads the lead as asserting more than the evidence supports and asks for "current evidence partly discriminates" to be removed outright. Claude reads the same body as passing the constrain-vs-establish gate "at the level it matters most", finds calibration asymmetry "near-absent, and arguably reversed", and concludes the article "risks *over-concession* rather than asymmetric credulity" — locating the single clear violation entirely in the tenet coda. Both cannot be right about the same paragraphs. This disagreement is itself the more interesting signal, and the refine pass working the ChatGPT singleton should adjudicate it rather than executing either verdict unread.
- **Gemini vs both siblings — the direction in which the article uses AWARE-II.** Gemini charges that the article "cites Parnia's AWARE II study (2023) to argue for transcendent dualist access" and "deliberately suppresses" its findings. Verified inverted: the article recruits AWARE-II's *negative* primary endpoint against transcendence, concluding the post-2019 findings "tilt toward the edge-mapping and dying-brain production readings… and none supports transcendence." Neither sibling reviewer made this charge; both read the article's NDE handling as conservative.

## Method Notes

**Per-reviewer accuracy diverged far enough this cycle to change how the count was used.**

- **ChatGPT 5.6 Pro** — all 9 Map-attributed spans grep verbatim; four citation criticisms verified at the publisher. Notably clean against the base rate for this channel.
- **Claude Opus 5** — mostly sound, but **three claims failed verification** and were recorded as disputed: the Kutnyy "possibly fabricated" call (the work is real; the flag reflects a Cloudflare 403, and acting on it would have deleted a real citation from four files), the assertion that the wrong Zeifman locator "corresponds to no real object" (it resolves to a real capuchin-parasitology paper, which makes the defect worse, not absent), and the "unlike neighbouring voids" comparative, which failed against five checked neighbours.
- **Gemini 2.5 Pro** — **4 of 5 weaknesses failed verification**, the lowest hit rate recorded for this channel on a single-article subject. It claimed the article omits Borjigin et al. 2023 (cited at L129 as Xu et al., same DOI — a first-author / senior-author miss), that it perpetuates "flat EEG" framing (L127 debunks exactly that), that it cites AWARE-II for transcendent access (L129 uses its negative endpoint), and that it ignores Metzinger 2024 (11 occurrences on the live page). Diagnosis: it audited a **composite** of several site pages — three of its quoted spans occur in `concepts/filter-theory` and `topics/eastern-philosophy-consciousness`, not the target. **This is a repeat**: the 2026-06-05 Gemini leg on this same article was logged as "mostly misreads NDE".

**Consequence for this synthesis.** No priority was moved on a bare count. Every cluster was checked against the article on disk before it was allowed to count as corroboration, and a finding already refuted during collection was not permitted back in through the count — Gemini's four failed weaknesses generated nothing here. The one cluster carrying a Gemini vote (finding 1) earned its upgrade because that specific item verified independently, not because two voices agreed.

**No tasks were minted, resurrected, or deduplicated.** Both collect passes had already augmented existing tasks rather than duplicating them, so the deduplication step this skill normally performs had nothing to do. Eleven-plus active blocks already touch `voids/edge-states-and-void-probes`; adding more would have compounded the pile-up rather than the coverage.

**Recorded, deliberately not actioned — evidence bearing on the upgrade rule itself.** Kim, Garg, Peng & Garg (arXiv:2506.07962, ICML 2025) measure exactly this configuration across 350+ models and find that error correlation *rises* with capability "even with distinct architectures and providers", with models agreeing "60% of the time when both models err". That is a direct argument that a 2-of-3 count is worth less than it looks. The counterweight is Buyl et al. (*npj AI* 2(1):7, 2026), which finds model families sitting in measurably different positions by region of origin — so the signal is **over-priced, not worthless**. Changing the standing upgrade discipline is the operator's reserved domain and overlaps the open `NEEDS-HUMAN (methodology ratification) 2026-08-03` entry in `todo.md`; it is recorded here and left there.
