---
ai_contribution: 100
ai_generated_date: 2026-09-08
ai_modified: 2026-09-08 10:26:12+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-08
date: &id001 2026-09-08
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-08 10:26:12+00:00
modified: *id001
related_articles: []
title: Deep Review - Quantum Immortality and the Quantum-Suicide Survival Argument
topics: []
---

**Date**: 2026-09-08
**Article**: [Quantum Immortality and the Quantum-Suicide Survival Argument](/topics/quantum-immortality-and-the-quantum-suicide-survival-argument/)
**Previous review**: [2026-07-26](/reviews/deep-review-2026-07-26-quantum-immortality-and-the-quantum-suicide-survival-argument/) (fourth pass; also 2026-07-19, 2026-07-08)

## Scope and Budget

Length-constrained pass. Measured before editing: **3903 words** against topics soft 3000 / hard 4000 — 97 words of headroom, with a 792-word (20%) reference apparatus and 3111 words of body prose. This is the apparatus-capped case: prose genuinely just above soft *and* the article near hard, simultaneously. Every addition was funded inside the same edit; final **3904 words** (net **+1**), 96 words of headroom, status `soft_warning`.

The 2026-07-26 review's stability notes were honoured: the Map-vs-Wilson-QMR bedrock disagreement was not re-flagged, and the multiple "not proprietary to collapse" statements were left as the section's cumulative argument via distinct routes.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. The Map's collapse described as "consciousness-caused", grounding a false empirical-immunity claim (L74). FIXED.**

The article read: *"Those are spontaneous-localization models, and the Map's collapse is not among them: it is consciousness-caused and minimal (Tenet 2), so the underground bounds that have tightened around GRW/CSL and ruled out the Diósi–Penrose model (Donadi et al. 2021) constrain spontaneous localization, not the Map's interaction-triggered reduction."*

This is wrong on the Map's own terms, and the error is load-bearing: it converts a tenet-level distinction ("minimal", "modulation") into exemption from an empirical bound. Confirmed against four independent loci, each stating the opposite:

- `topics/philosophical-stakes-of-spontaneous-collapse.md:48` — *"**Consciousness-modulated collapse** (the Map's position): A baseline physical mechanism—GRW stochasticity, CSL noise, or gravitational self-energy—collapses wave functions universally… The key distinction from consciousness-caused collapse: remove all minds from the universe and physics still produces definite outcomes."*
- `concepts/prebiotic-collapse.md:40` — *"consciousness doesn't cause collapse universally—it interfaces with collapse in neural systems. Objective reduction provides the baseline."* Its falsifier #1 is *"All objective collapse theories are ruled out experimentally… definitive exclusion of GRW, CSL and Penrose together would force revision"* — i.e. those bounds bear on the Map.
- `tenets/tenets.md:125` — the Map's resolution is *"objective reduction with consciousness modulation. Physical mechanisms (gravitational collapse, **spontaneous localization**, or unknown processes) provide baseline collapse."* The tenets page names spontaneous localization as a candidate for the Map's own baseline.
- `project/mqi-empirical-fragility.md:56` — *"The Map's existing relation to these theories is to embrace the baseline collapse mechanism… while preserving a modulation channel,"* and it treats the 2021 Gran Sasso falsification as bearing on the Map's fragility.

Also an *internal* contradiction inside the single paragraph: the immunity claim sat two sentences above the paragraph's own conclusion that single-outcome theories keep "their own probability, ontology, tails, and subject-continuity questions." The fix resolves the paragraph in favour of its conclusion.

Replacement (word-neutral, 60 → 60 before a further 3-word tightening): *"The Map does not stand outside those models: its baseline **is** [objective reduction](/concepts/prebiotic-collapse/)—gravitational self-energy, GRW, or CSL—with consciousness modulating outcomes at neural sites only (Tenet 2). The underground bounds that have tightened around GRW/CSL and ruled out the Diósi–Penrose model (Donadi et al. 2021) therefore constrain that baseline too, narrowing its parameter space rather than exempting it."*

Classification: calibration error, not bedrock disagreement — a reviewer who fully accepts the Map's tenets would still flag it, because the Map's own tenet page and positions register decline the exemption the article claimed. It is the mirror of over-concession: an over-claim running *for* the Map that four prior reviews ratified.

**Isolation check (structurally independent of the first).** Swept `obsidian/` + `archive/` for the *claim* rather than the string — `underground|Donadi|Diósi–Penrose` across both trees, ~60 loci inspected. Every other locus states the constraint correctly; [positions/quantum-interface.md](/positions/quantum-interface/) [P-Q6](/positions/quantum-interface/#p-q6) positively asserts the parameter-free DP model *has been* empirically falsified. `consciousness-caused` appears in six other live articles, all correctly describing what the Map is **not** (or a rival view). The defect was confined to this article. **No sweep task minted.**

**2. Greene 2026 cited as "forthcoming" in two places. FIXED.** Verified independently at Crossref (not taken on the driver's label): DOI `10.1080/00048402.2026.2670763`, *Australasian Journal of Philosophy*, author **Preston Greene** (ORCID 0000-0001-6439-3323, NTU), issued **2026-05-14**, online-first pp. **1–17**, no volume/issue yet. Body (L82) `forthcoming` → `2026`; reference 18 now carries year, page range and DOI in house style. The paper published two months *before* this article was created (2026-07-08), so the citation was stale at birth.

Greene's argument shape was also verified rather than assumed, since the cite is claim-bearing: the paper argues that Parfit's psychological view of personal identity combined with an infinite universe (the majority cosmological view) guarantees immortality via distant duplicates. The article's gloss — *"if identity is Parfitian and space is infinite, psychological continuity is preserved by distant duplicates even under one-branch collapse"* — is faithful.

**3. `description` 209 chars against the 150–160 schema band. FIXED.** Rewritten to **160** chars: *"A human-AI examination of quantum suicide: the immortality expectation needs branch-relative identity, which collapse never supplies — no advantage for dualism."* The demotion is preserved (the "no advantage for dualism" clause is retained, not dropped), so this does not regress commit `7956f4fa92`'s sweep against descriptions claiming dualist payoffs their bodies retract. −6 words, which part-funded the other edits.

### Medium Issues Found

**Tegmark 1998 quote: grammatical graft and altered terminal punctuation. FIXED (+3 words).** The article read *"the dedicated experimenter, he wrote, \"will experimentally convince yourself…\""* — a third-person antecedent governing a second-person quotation, and a period substituted for the source's exclamation mark. The source's own conditional (*repeated* attempts) was also dropped. Now: *"repeatedly attempt quantum suicide, he wrote, and \"you will experimentally convince yourself that the MWI is correct, but you can never convince anyone else!\""*

**O'Brien classification strengthened beyond the source. FIXED (−1 word).** "classes him as the canonical immortalist" → "classes him among the immortalists". O'Brien's abstract gives Tegmark as *an example* ("Some, e.g. Max Tegmark (immortalists)"); "canonical" was the Map's gloss presented as O'Brien's classification.

### Publisher-of-Record Citation Ledger (§2.4)

The driver had pre-resolved eight references at Crossref (7, 8, 10, 11, 15, 16, 19, 20). Per `citation-verify-false-negative` discipline, only the ones driving an edit were re-verified; the rest were not re-spent. Ledger for what this pass actually checked:

- **Greene, P. (2026) "We Will All Live Forever", *AJP*** — state: **real-wrong-metadata**. Was "(forthcoming)" in body and reference; corrected to 2026, pp. 1–17, DOI:10.1080/00048402.2026.2670763. Verified at Crossref DOI record (all fields printed, not sliced).
- **O'Brien, M. W. (2025) *Synthese* 206(5), art. 221** — state: **real-correct**. Re-resolved at Crossref: title, venue, volume 206, issue 5, article-number 221, issued 2025-10-16, author "Mark William O'Brien". Matches reference 11 exactly. The *substantive* classification claim was verified separately (below).
- **Tegmark, M. (1998), arXiv:quant-ph/9709032** — state: **real-correct**, quote **verbatim** (method below).
- **Mallah, J. (2009), arXiv:0902.0187** — state: **real-correct**, and it does reproduce the Tegmark website note it is cited for; quote **verbatim** (method below).
- **Donadi et al. (2021) *Nature Physics* 17, 74–78** — state: **real-correct** (driver-resolved; retained as "2021" for consistency with reference 20). Note [concepts/prebiotic-collapse.md](/concepts/prebiotic-collapse/) cites the same paper as "(2020)" for the online-first date; both are defensible and neither article is wrong.

References **9, 12, 13, 14, 17** and the three books (**4, 5, 6**) were **not** web-verified this pass — budget went to the L74 defect and the quote-fidelity lens. They remain an open verification seam; see Remaining Items.

Superlative-claim sweep via `tools.curate.empirical_currency.find_superlative_claims`: **0 claims detected**. No currency-drift exposure.

Inline ↔ References cross-check: all 20 references are cited inline or in the "Further Reading"/body apparatus; no orphans in either direction.

### Quote-Fidelity Lens (nobody had run it on this article)

Both verbatim quotes were checked against **raw** sources pulled and grepped locally in Python with offsets printed — not via a summariser, and not via any Map page (self-contamination avoided).

**1. Tegmark 1998.** Fetched the arXiv **LaTeX source** (`arxiv.org/e-print/quant-ph/9709032`, gunzipped to `9709032.tex`, 41,039 bytes). A naive normalized grep for the full quote returned **offset −1** — a **false negative** caused by LaTeX markup splitting the phrase: the source is `you {\it will} experimentally convince yourself`, so the italic command sits between "you" and "will". Confirmed by locating the fragments (`convince yourself` at offset 32969; `convince anyone else` at 33030) and printing 1,500 characters of surrounding context. De-LaTeXed source reads:

> …if once you feel ready to die, you repeatedly attempt quantum suicide: you *will* experimentally convince yourself that the MWI is correct, but you can never convince anyone else!

**Verdict: verbatim**, modulo the terminal `!`→`.` substitution the article had made (now restored). This is a clean instance of `my-truncated-reads-manufacture-defects-and-false-accusations`-class markup interference — the first grep would have licensed a false fabrication charge.

**2. Tegmark c.2004 website note, via Mallah 2009.** Fetched `arxiv.org/e-print/0902.0187` (PDF, 16pp), extracted with `pdftotext -layout`, normalized de-hyphenation and dash forms. Found at offset 40210:

> After all, dying isn't a binary thing where you're either dead or alive - rather, there's a whole continuum of states of progressively decreasing self-awareness.

**Verdict: verbatim**, modulo hyphen-vs-em-dash styling. Attribution also confirmed: Mallah introduces it as *"He wrote the following explanation [Tegmark 2]"*, and his reference list resolves `[Tegmark 2]` to *"Quantum resources (website) http://space.mit.edu/home/tegmark/quantum.html"* — so "c.2004 website note (reproduced in Mallah's 2009 survey)" is accurate.

**One precision note, not actioned.** Reference 2 credits the website note as source of both the quoted remark *and* "the later numbered three-condition summary". Mallah's reproduction contains the remark but **no numbered list** — he paraphrases only two conditions (genuine quantum event; death before the doomed-branch subject becomes aware). The numbered list is presumably on Tegmark's live page and in *Our Mathematical Universe*, both of which reference 2 also names, so the reference is defensible as written; but a reader going to Mallah for the list will not find it. Left alone rather than spending words on a hedge — recorded here so a future pass need not rediscover it.

### O'Brien 2025 Load-Bearing Check (driver-flagged)

O'Brien carries three claims in this article: the immortalist/mortalist split, Tegmark's classification, and the "costs of rejecting" framing. Springer, PhilPapers and PhilSci-Archive all blocked direct retrieval (403 / bot challenge); Semantic Scholar and OpenAlex both return the abstract elided. Recovered the abstract text through two independent searches that returned **stably identical** wording:

> Proponents of the Many Worlds Interpretation … are divided in their attitudes to the idea of quantum immortality. Some, e.g. Max Tegmark (immortalists), believe one should always expect to experience subjective survival in a quantum suicide thought experiment… Others, e.g. Sean Carroll, David Papineau and David Wallace (mortalists), believe that the truth of the MWI has no such consequences…

All three claims confirmed. The apparent tension the driver flagged — the article classing Papineau as a mortalist while also saying his 2004 piece "runs the other way, defending the Everettian" — is **not** a defect: a mortalist *is* an Everettian who rejects the immortality inference, and Papineau's 2004 paper defends the Everettian account of *probability* against Lewis. The two statements are consistent, and the article's reference 8 gloss already says so.

### Over-Concession Sweep (driver-flagged)

Swept for *no possible / cannot ever / in principle undetectable / never / always / impossible*: 12 hits. Eight are exposition of the opponent's own argument (L34, L36, L38, L54, L68) or restatements of a cited position — correctly attributed, not the Map's assertions.

The driver flagged the **Tenet-2 pressure test** (L84) as the place to look hardest, since *"A subject therefore cannot steer an external lethal device toward survival"* is the article's own construction. **Verdict: sound, and it is the L74 defect's mirror image — checking it is what exposed L74.** L84 rests on the trigger being *"objectively reduced before any neural processing of it begins"*, which is exactly right on the Map's actual position (objective reduction is the universal baseline). L74's "consciousness-caused" was what made L84 look suspect; with L74 corrected, L84's argument is consistent with `prebiotic-collapse` and with Tenet 2's scope limit (*"minimal in scope (brains, not cosmos)"*). Its "cannot" is earned by the scope limit, not over-claimed. **Not changed.**

L80's *"parsimony cannot do load-bearing work for or against a framework under incomplete knowledge"* is Tenet 5 stated correctly and is itself a concession against an easy Map argument. Left intact; the "load-bearing" usage here is borderline against the house style note but is doing genuine structural work.

### Reasoning-Mode Classification (§2.6)

No editor-vocabulary label leakage found in article prose (checked for `direct-refutation-feasible`, `unsupported-jump`, `bedrock-perimeter`, `Engagement classification:`, bold `**Evidential status:**` callouts): **zero hits**.

- Engagement with **Wilson (quantum modal realism)**: **Mode Three — framework-boundary marking**, correctly and explicitly declared (*"The Map meets it at that framework boundary… not with a refutation earned inside Wilson's system"*). Honest.
- Engagement with the **Everettian mortalist / caring-measure reply (Greaves, Wallace)**: **Mode Three**, and unusually generous — the article concedes the caring-measure account "defeats the immortality inference from inside MWI—without collapse and without a dualist subject." Boundary declared at the right place (whether care-distribution can substitute for a fact about which successor one *will be*).
- Engagement with **Parfit / Madhyamaka**: **Mode Three**, correctly framed as a presupposition the dissolution depends on rather than a position refuted.

No boundary-substitution found; no engagement was weaker than the available mode.

## Optimistic Analysis Summary

### Strengths Preserved
- The immortalist/mortalist division and its current sourcing (O'Brien 2025) — verified accurate this pass, and rare in the popular literature on this topic, which usually reports the argument without noting the field is split.
- The **Tenet-2 pressure test** (L84): a self-interrogation the Map specifically owes and that no cited source raises. It survived adversarial scrutiny this pass rather than merely going unexamined.
- The **demotion arc** — declining a dialectical advantage for dualism, and saying so in the lead as well as the conclusion. The Hardline Empiricist persona's praise-worthy pattern (tenet-as-evidence-upgrade declined) is present throughout, and the L74 fix extends it: the article now also declines an *empirical-immunity* upgrade.
- The conditional treatment of the measure objection ("decisive only once Born-weighted anticipation is granted") — calibrated, and consistent between lead and body.

### Enhancements Made
Four fixes and one tightening; see the pessimistic ledger. No expansion was attempted — the article is at 20% apparatus with 96 words of headroom, and expansion would have required cutting calibration content to pay for it.

### Cross-links Added
- [objective reduction](/concepts/prebiotic-collapse/) — piped onto existing text, **zero word cost**. This was also the substantively right link: it points the empirical-constraint claim at the Map's own treatment of the baseline, closing the gap that let the defect stand through three prior reviews.

## Remaining Items

- **References 9, 12, 13, 14, 17 and the books 4, 5, 6 are not publisher-verified.** Reference 4 (Squires 1986) is worth one check: this article gives the publisher as **Adam Hilger**, while Mallah's own reference list gives **Institute of Physics Publishing**. Both are defensible (Adam Hilger was IOP's imprint), so this is a disambiguation rather than a suspected error. Not urgent enough to mint a task — the next citation-lens pass on this article should start here.
- **Reference 2's numbered-list attribution** — see the precision note above. Cosmetic; do not re-litigate without new information.

## Stability Notes

- **The Map-vs-Wilson-QMR disagreement remains bedrock** (whether *which successor is me* is a counterpart-relative similarity fact or a real further fact). Do not re-flag. Unchanged from 2026-07-26.
- **The multiple "not proprietary to collapse" statements are cumulative argument via distinct routes**, not redundancy. Unchanged from 2026-07-26; do not trim further.
- **New: the Map's collapse is objective reduction with consciousness modulation, never "consciousness-caused".** The Map's baseline *is* a spontaneous-localization-class mechanism, so the GRW/CSL/Diósi–Penrose bounds constrain it and narrow its parameter space. Any future edit reasserting that those bounds do not reach the Map is reintroducing this defect. Canonical statements: `topics/philosophical-stakes-of-spontaneous-collapse.md:48`, `concepts/prebiotic-collapse.md:40`, `tenets/tenets.md:125`, `project/mqi-empirical-fragility.md:56`.
- **The convergence-damping caution is borne out here.** Three prior reviews (2026-07-08, 07-19, 07-26) and a 2026-08-07 description sweep all passed over a claim that contradicts four canonical loci, and the 07-26 pass explicitly scoped citations and recalibration out. A clean streak on this article was not evidence of correctness — the lens that had never been run (quote fidelity, and reading the Tenet-2 pressure test against the Map's own collapse ontology) is what found it. Convergence damping should not be read as licensing a no-op on the next pass.