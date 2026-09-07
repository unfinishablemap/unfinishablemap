---
title: "Deep Review - The Unfolding Argument Against Causal-Structure Theories of Consciousness"
created: 2026-09-07
modified: 2026-09-07
human_modified: null
ai_modified: 2026-09-07T15:58:00+00:00
draft: false
topics: []
concepts:
  - "[[integrated-information-theory]]"
  - "[[ontic-structural-realism]]"
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-09-07
last_curated: null
---

**Date**: 2026-09-07
**Article**: [[the-unfolding-argument-against-causal-structure-theories-of-consciousness|The Unfolding Argument Against Causal-Structure Theories of Consciousness]]
**Previous reviews**: [[deep-review-2026-08-05-unfolding-argument|2026-08-05]] (FIX: wrong-work cite, de-quoted verbatim) · [[deep-review-2026-07-11-unfolding-argument|2026-07-11]] · [[deep-review-2026-07-10-the-unfolding-argument-against-causal-structure-theories-of-consciousness|2026-07-10]]

Verdict: **FIX** — one inaccurate cross-reference framing corrected, one term disambiguated against a new corpus cluster, one section added on scope, three publisher-verified references appended.

## Scope note: why this was a dependency-drift pass, not a self-modification pass

The article's own body was unchanged since the 2026-08-05 review. Its `ai_modified: 2026-09-06` came from commit `40091fb3ab`, an OSR cross-review that inserted a **single Further Reading bullet** and no body prose. So there was no unreviewed inserted paragraph to audit — the `outbound-crosslink-sentences-are-never-reviewed-by-anyone` shape in miniature, and the bullet turned out to be the defect.

The productive axis was **dependency drift**: 5 of 9 link targets moved since 08-05. Findings below classify each.

## Dependency movement triage

| target | moved | verdict |
|---|---|---|
| `ontic-structural-realism` | 2026-09-05 | **MATERIAL** — new direct rival; its arrival made this article's key term ambiguous and its reciprocal bullet inaccurate |
| `hard-problem-of-consciousness` | 2026-09-07 | **checked, clear** — not cosmetic in itself, but no conflict here |
| `hoel-llm-consciousness-continual-learning` | 2026-09-04 | cosmetic for this article |
| `falsification-roadmap-for-the-interface-model` | 2026-08-22 | cosmetic for this article — and *corroborates* an existing concession |
| `mathematical-structure-of-the-consciousness-physics-interface` | 2026-08-19 | cosmetic for this article |

**`hard-problem-of-consciousness` (today) — checked, clear.** Its diff did real work: "Substrate Independence Fails" → "Substrate Independence Undercut, Not Refuted" (conceding that psychophysical laws could be nonreductive *and* substrate-independent), and a calibration downgrade on the anti-IIT passivity charge ("identity leaves consciousness no *autonomous* causal role … a charge that page presses as internal critique while conceding it cannot double as an argument for interactionism"). Neither puts this article out of step: it makes no substrate-independence claim, and it never presses the passivity charge. Its narrow-gauge escape clause for function theories survives the nonreductive-functionalism concession intact, because that clause turns on behavioural equivalence carrying experiential equivalence, which a nonreductive functionalist also grants.

**`falsification-roadmap` (08-22) — cosmetic here, but note the corroboration.** Its edits were confined to Tenet 2 falsification readings. Incidentally they *strengthen* this article's Site-Perspective concession: the roadmap now states the strict corridor "predicts no Born-statistical signature by construction" and is vulnerable to motivation-loss rather than Popperian refutation. That is precisely the sub-detectability this article concedes. The concession is better supported upstream than when it was written; no edit required.

## Critical Issues Found

### CRITICAL-1: The OSR Further Reading bullet mis-routes the pressure (FIXED)

The bullet installed on 2026-09-06 read:

> `[[ontic-structural-realism]]` — Structure as all there is; extending that ontology to experience would have to meet the pressure this argument applies

Two defects:

1. **It mis-identifies which formal problem the extension faces.** The unfolding argument bites only on theories fixing consciousness by *internal causal wiring independent of function* — the article's own narrow-gauge paragraph says so. Structuralism about phenomenal character individuates experiences by relations *among experiences*; it makes no claim about which physical organisation realises which phenomenal structure, so the unfolded twin has nothing to grip. The pressure that does reach it is **Newman's problem**, not this argument.
2. **It conflates two structuralisms whose principals disown the association.** Holger Lyre, verified raw: *"One might be inclined to ask whether neurophenomenal structuralism is a version of structural realism. The short answer is: no."*

Resolution: bullet rewritten to `a thesis about the ontology of physics whose extension to experience meets Newman's problem rather than this argument`.

### CRITICAL-2: "structural physicalism" became ambiguous against a new neighbour (FIXED)

The article uses **structural physicalism** three times as its gloss for Doerig et al.'s target class. That was unambiguous in July. With `ontic-structural-realism` (09-05) live and a `structuralism-about-phenomenal-character` research note filed (09-06), the term now reads as though it covered phenomenal structuralism, which the argument does not target. The `navigation-surfaces-carry-unreviewed-claims` risk in reverse: a body term that a new cluster has retro-activated.

Resolution: new section **"Which structuralism the argument reaches"** (`{#which-structuralism}`), 419 words, plus a forward pointer from the narrow-gauge paragraph using the named-anchor pattern. The section states the taxonomy, states why the ontic version is not in the target class on its own, states the one condition under which a phenomenal structuralist *does* enter it (pairing the thesis with a psychophysical theory keyed to causal organisation — which is what IIT is), and identifies the pressure that does apply.

Substantive gain beyond the correction: the article previously carried **one** formal pressure on IIT. It now carries a second, independent one — Kleiner's Newman-problem argument — with the convergence stated explicitly (IIT is exposed once as a causal-structure theory and once as a maker of bare structural phenomenal claims), and with the independence stated explicitly so no reader infers a link Kleiner does not draw.

### Non-issue checked and cleared: soft inline↔References orphan

Line 46 name-dropped "Kleiner and Hoel" with no year and no References entry. Borderline rather than critical, since it explicitly defers to two other articles. Closed anyway: year added inline, Crossref-verified entry appended as ref 10.

## Publisher-of-Record Citation Ledger (this pass)

Prior ledgers (07-10, 07-11, 08-05) cleared all 9 existing cites on metadata, quote-fidelity and framing axes; the References block was unmodified since, so per §2.4's trigger rule existing entries were not re-litigated. This ledger covers the **three new cites** plus two incidental re-confirmations.

- **Kleiner, J. (2025)**, *The Newman problem of consciousness science*, PhiMiSci 6 — **real-correct.** Crossref `10.33735/phimisci.2025.11827`; sole author Johannes Kleiner; title exact. ⚠️ **Year adjudicated, and the two sources disagree**: Crossref `issued` = 2026-01-30, but the publisher's own `citation_date` meta tag reads **2025** and the article page prints **"Vol. 6 (2025)"**. Publisher of record wins per `page-range-publisher-of-record-beats-aggregators`; cited as 2025 with the discrepancy footnoted in the entry. ⚠️ Also carried forward from the upstream note and re-confirmed against the PDF: the DOI printed in the article's *own* citation line is a publisher placeholder (`10.33735/phimisci.2100.1234`) — the entry warns against it.
  - Both quotes used were **raw-verified by me**, not inherited: downloaded the publisher PDF, `pdftotext`, grepped. The OPSR/EPSR definition and the IIT passage ("a perfect example", "entirely void, over and above the cardinality of the elements in the structure") are verbatim.
  - **Framing guard applied.** Grep of the full PDF: "unfolding" appears **only** in its bibliography, as Kleiner's own 2020 paper. Kleiner 2025 does **not** engage the unfolding argument, and the article says so in as many words. This is a deliberate refusal to repeat the 08-05 CRITICAL-1 shape (Kleiner & Tull cited for a UA reply it never makes) with a new Kleiner paper.
- **Lyre, H. (2022)**, *Neurophenomenal structuralism*, Neurosci. Conscious. 2022(1) niac012 — **real-correct.** Crossref `10.1093/nc/niac012`, sole author, title and venue exact. Disavowal quote **raw-verified by me** in Europe PMC `PMC9396309` full-text XML (130,612 chars), not taken from the corpus's transcription of it.
- **Kleiner, J., & Hoel, E. (2021)**, *Falsification and consciousness*, Neurosci. Conscious. 2021(1) niab001 — **real-correct.** Crossref `10.1093/nc/niab001`; article-number niab001 confirmed.
- **Kleiner, J. (2020)** (existing ref 4) — **independently re-corroborated.** Kleiner's own 2025 reference list carries *"Kleiner, J. (2020). Brain states matter. A reply to the unfolding argument. Consciousness and Cognition, 85."* The 08-05 correction is now confirmed from the author's own hand.
- **Hanson & Walker 2021** (existing ref 3) — metadata re-confirmed incidentally via Crossref (niab014, 2021(2)); matches.

**Deliberately NOT cited: Fink, Kob & Lyre (2021).** It is the paper that self-names phenomenal structuralism and was the obvious third cite. Declined because the upstream note's grep counts on the raw artefact are decisive — "hard problem" 0, "dualis\*" 0, "structural realism" 1 (a bibliography entry) — so FKL "never engage the metaphysics of consciousness at all." Citing an NCC-methodology paper for a metaphysical classification would have been the `citation-framing-accuracy-lens` defect. The claim it would have supported is carried by Kleiner 2025 instead, which does make it.

**Source tiers inherited, not promoted.** Every source used is `[raw-verified]` in `research/structuralism-about-phenomenal-character-2026-09-06.md`, and I re-verified each at the publisher independently rather than relying on that tier. No `[metadata only]` source (Aldé 2026, PhiMiSci Vol. 6 contents) was touched. Negro 2025 and Fink & Lee 2025 were verified at Crossref during the pass but not cited — Kleiner's OPSR/EPSR is the sharper instrument and avoids a second year-ambiguity footnote.

Superlative-claim sweep: **0 hits** (`find_superlative_claims`). Inline↔References: **12/12 complete in both directions**, verified programmatically. All 9 wikilinks resolve in `obsidian/` and `archive/`.

## Reference-list handling

The list is numbered 1-9. Checked the body for by-number citations before touching it: **none** — the body is author-year throughout. Appended as **10, 11, 12**; nothing renumbered, so no `inserting-into-a-numbered-ledger-breaks-cross-references` exposure.

## Optimistic Analysis Summary

### Strengths Preserved
- The three Site-Perspective calibration paragraphs (double-edged reading; metaphysical-vs-empirical axis split; the shared-anti-functionalism tension) were **not touched**. The 08-05 stability note protects them and they remain the article's best work. No re-broadening, no re-assertion of a clean empirical escape.
- The narrow-gauge framing was not rewritten — it was *extended*. The new section is built on the existing scope machinery rather than replacing it, which is why it needed no hedging of its own.
- The "do not cheerlead it" stance, the plasticity carve-out, and the Kleiner 2020 rebuttal added on 08-05 are untouched.

### Enhancements Made
- Second independent formal pressure on IIT (Newman), with convergence *and* independence both stated.
- Named-anchor forward reference from the narrow-gauge paragraph, per the truncation-resilience guideline.

### Cross-links Added
- `[[ontic-structural-realism]]` promoted from a Further Reading bullet to a body cross-link with an accurate characterisation. Reciprocity confirmed: OSR's own Further Reading already points here ("Identical structure, different consciousness?").

## Length

Gross: 2472 → **3022 words** (`soft_warning`, 121% of the 2500 soft threshold, 86% of hard). **This is a false over-length reading.** Decomposed: frontmatter 71, References 366 (grew ~90 with three new entries), Further Reading 36 — leaving **body prose 2615, or 105% of soft**. Per `analyze-length-counts-reference-apparatus` and `count-words-includes-frontmatter`, the reference apparatus drives the warning. No trim applied: 105% body prose is within normal range, and the passages a trim would reach are the protected calibration paragraphs. Article entered the pass *below* soft (2472), so §4.5 licensed normal expansion.

## Reasoning-Mode Classification (editor-internal)

- Engagement with IIT / Tsuchiya (intrinsicality): **Mode Three**, unchanged.
- Engagement with the functionalist premise: **Mixed**, unchanged.
- Engagement with Kleiner 2020: **Mode One**, unchanged.
- **New — engagement with ontic phenomenal structural realism: Mode Three, framework-boundary marking, correctly scoped down.** The temptation was boundary-substitution in the opposite direction: claiming the unfolding argument refutes OPSR because OPSR is structure-all-the-way-down. It does not, and the section says so. Declining an available-looking refutation is the honest move here.
- **New — engagement with IIT via Newman: Mode Two, unsupported foundational move.** Kleiner's charge is that IIT helps itself to a structural claim whose truth-conditions it has not supplied (Φ-structure without a phenomenal interpretation), judged by a standard IIT's own mathematisation invites. Reported as Kleiner's argument, not the Map's.
- No editor-vocabulary leakage in prose (grepped: 0 hits for all forbidden labels).

## Remaining Items

- `concepts/ontic-structural-realism` L37 concedes that ontic structuralism about experience is "a composite the Map has assembled, **not a position anyone defends in print**." The 09-06 research note supersedes this: *"The ontic composite exists in print, defined, under a name"* — Kleiner's OPSR. **That article's concession is now too strong.** Out of scope for this pass (fresh, 09-05, and not my target); flagged for whoever writes the `structuralism-about-phenomenal-character` article, which the 09-06 note recommends. I inherited none of the error — this article cites Kleiner's OPSR as a position held in print.
- The 09-06 research note remains **unconsumed** (no `concepts/structuralism*` or `topics/structuralism*` article exists). Its recommended target is `concepts/`, which had 5 slots at last measure.

## Stability Notes

- Carry forward all prior stability notes unchanged: the **functionalist-premise standoff** and the **Madhyamaka svabhava** objection are bedrock framework-boundary disagreements. The 07-11 HIGH-1/HIGH-2 calibrations are closed at the honest, narrower reading — do not re-broaden. Do not restore Kleiner & Tull 2021 as a source for any unfolding-argument reply.
- **New**: do not treat the unfolding argument as reaching structuralism about phenomenal character. It reaches phenomenal structuralism only through a psychophysical partner theory keyed to internal causal organisation. A future pass tempted to strengthen this into "the argument refutes ontic phenomenal structuralism" would be substituting a framework boundary for an in-framework refutation.
- **New**: do not cite Kleiner 2025 for anything about the unfolding argument. Verified by grep of the full PDF — it addresses the Newman problem and mentions the unfolding argument only in its bibliography. This is the same trap that produced the 08-05 wrong-work defect, one Kleiner paper over.
- **New**: Kleiner 2025's year is genuinely contested between Crossref (2026) and the publisher (2025). It is settled at 2025 on publisher-of-record grounds and footnoted. Do not "correct" it to 2026 from a Crossref lookup alone.
- **Methodological note**: this pass found nothing by re-reading the article and everything by reading what had moved *underneath* it. Three prior ledgers had cleared the citations; the defect arrived from a neighbour, in a one-line bullet nobody reviewed, and the term it destabilised had been correct for two months. On a converged article, ask what moved under it rather than what is wrong with it.
