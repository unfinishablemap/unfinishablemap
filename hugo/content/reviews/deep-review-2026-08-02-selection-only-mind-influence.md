---
ai_contribution: 100
ai_generated_date: 2026-08-02
ai_modified: 2026-08-02 11:52:15+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-02
date: &id001 2026-08-02
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-02 11:52:15+00:00
modified: *id001
related_articles: []
title: Deep Review - Selection-Only Mind-Influence (two fabricated quotes removed;
  Stapp misattribution corrected)
topics: []
---

**Date**: 2026-08-02
**Article**: [Selection-Only Mind-Influence](/topics/selection-only-mind-influence/)
**Previous review**: [2026-07-09](/reviews/deep-review-2026-07-09-selection-only-mind-influence/) (6th review overall; priors 2026-05-06, 2026-05-08, 2026-06-02, 2026-06-16, 2026-07-09)
**Mode**: SUBSTANTIVE. Three critical issues found and fixed, all in the quotation/attribution channel. Two of the article's three direct quotations were **fabricated**. Both survived five prior deep reviews — including the 2026-06-16 pass that recorded a complete 12-entry publisher-of-record ledger.

## Scope

Sole change since the 2026-07-09 pass was commit `41d89c35e` (2026-08-02, ~4h prior): the refine-draft correcting the Map's self-quote of Tenet 2 from "quantum outcomes" to "physical outcomes". That change is **verified correct** — both quoted strings grep verbatim against `obsidian/tenets/tenets.md` L62 ("The smallest possible non-physical influence on physical outcomes.") and L64 ("it must do so at the quantum level—biasing otherwise indeterminate outcomes without injecting energy or violating conservation laws."), em-dash preserved. The headline/definition split the refine-draft introduced is a faithful reading of the tenet as written.

Because the body was modified, §2.4 triggered a fresh citation pass rather than the skip that applied on 2026-07-09. That is what surfaced the fabrications.

## Pessimistic Analysis Summary

### Critical Issues Found

**C1 — Fabricated Stapp quote (FIXED).** The article attributed to Stapp's *Quantum Interactive Dualism*: *"the mind would only have the option to choose the observable, not the option of selecting the measurement result in deviation from the Born's probability law"* (Stapp, n.d.).

Verification (two independent extractions, `pdftotext` and `pdftotext -layout`, of the live LBL PDF):
- `QID.pdf` — the word **"Born" occurs zero times**. "probability law": 0. "deviation": 0. "observable": 1 occurrence, in the unrelated phrase "observable outcomes of".
- `vNS.pdf` (the research note's second cited Stapp source) — "Born": 0, "observable": 0, "probability law": 0, "deviation": 0.
- Web: `"option to choose the observable" "Born's probability law"` → NO RESULTS. `Stapp "not the option of selecting the measurement result"` → NO RESULTS. **`"Born's probability law"` alone → NO RESULTS** — the phrase does not exist in the indexed literature at all.
- Corpus grep: the string appears only inside the Map's own files. Textbook self-contamination via the Map's own pages.

Guarded against the Tallis broken-contiguity trap by extracting twice with different modes and by searching short distinctive fragments, not the whole span. Verdict: **fabricated**, not extraction failure.

Replaced with the genuine, verbatim-verified QID passage (PDF L351–353): *"whether 'Yes' or 'No' appears is not determined by the agent, who chooses only the question. The answer is picked by 'Nature', in accordance with a specified statistical law"*. This is the same passage [selection-only-channel](/concepts/selection-only-channel/) already quotes correctly.

**C2 — Stapp misattribution / internal contradiction (FIXED).** The article stated the strict selection-only reading "is the reading historically associated with Henry Stapp's *Process 1* framework". This inverts Stapp's assignment. Stapp puts mind's freedom at the **choice of question** (the observable/basis, which fixes the partition) and explicitly denies mind any role in the outcome. The article's own opening paragraph defines the strict reading as the exact opposite: "mind contributes nothing to the candidate set the brain physically generates. It only chooses which of the already-generated alternatives becomes actual."

The article therefore contradicted (a) its own lead, and (b) its own companion concept page, which gets the taxonomy right: [selection-only-channel](/concepts/selection-only-channel/) §"Not a measurement-basis-choice channel" states Stapp's Process 1 "modifies the candidate set itself by selecting the basis that defines it. The basis-choice layer above sits outside the selection-only class strictly construed." [channel-class-taxonomy](/concepts/channel-class-taxonomy/) and [brain-internal-born-rule-testing](/topics/brain-internal-born-rule-testing/) also read Stapp correctly. This article was the sole outlier.

Rewritten to name Stapp as the *closest historical antecedent* while stating the slot difference explicitly, and to cite the taxonomic boundary [selection-only-channel](/concepts/selection-only-channel/) draws. Per §2.5 this is a false-shared-commitment / source-Map conflation error, hence critical.

**C3 — Fabricated quote mis-sourced to Han & Choi (FIXED).** §"No-Signalling, Energy Conservation" carried: Born rule derivable from relativistic causality "(Han & Choi 2016), and *'violation of higher sum-rules allows for superluminal signalling'*". The quote is absent from Han & Choi 2016 (verified against PMC4789655 full text: "sum rule", "sum-rule", "superluminal" all zero hits) and returns NO RESULTS on the web. The underlying idea belongs to the higher-order-interference (Sorkin-hierarchy) literature, which the article does not cite.

Replaced with Han & Choi's actual, verbatim-verified result from the *Scientific Reports* abstract: *"Born rule on quantum measurement is derived by requiring relativistic causality condition"*, plus their nonlocality-bound framing. The paragraph's argument is unchanged and now correctly sourced — de-quote-and-reframe, not deletion, per the citation-framing-accuracy lens.

**Common origin.** Both fabricated strings trace to `**Quote**:` fields in `obsidian/research/selection-only-mind-influence-information-limits-2026-05-05.md` (L54, L132). Per the research-note-propagation rule the note was fixed too: both fields replaced with verified verbatim text and an explicit `**Correction 2026-08-02**` do-not-reintroduce marker. The note's L53 "Stapp's model is the historical exemplar of selection-only mind-influence" — the seed of C2 — was corrected in place.

### Publisher-of-Record Citation Web-Verify (§2.4) — per-cite ledger

Full re-verify of the direct-quotation channel plus the cites touched by this pass. The 2026-06-16 metadata ledger stands for the untouched remainder; note it verified *metadata* and explicitly recorded the Stapp quote only as "a faithful representation of Stapp's documented position" — a paraphrase ratification, not a verbatim check. That is exactly the "ledger complete" ≠ verbatim checked gap.

- Stapp, QID (*Quantum Interactive Dualism: An Alternative to Materialism*) — state: **real-wrong-metadata + fabricated-quote**. Paper real; quote fabricated (removed, replaced with verbatim). Dating corrected `n.d.` → **2006, *Zygon: Journal of Religion and Science*, 41(3), DOI 10.1111/j.1467-9744.2005.00762.x** (Crossref). Note this **corrects the carried note from the 2026-06-16/2026-07-09 reviews**, which recorded "*Zygon* 40(1):29–44" — wrong volume and issue. Page range is not in Crossref metadata and was not guessed.
- Han & Choi 2016 (*Quantum probability assignment limited by relativistic causality*) — state: **real-correct metadata, fabricated quote**. Europe PMC confirms Yeong Deok Han & Taeseung Choi, *Scientific Reports* 6:22986, DOI 10.1038/srep22986, PMID 26971717, PMCID PMC4789655. Quote removed and replaced with verified abstract text.
- Jahn et al. 2000 (PortREG replication) — state: **real-correct, and the article's empirical numbers verified**. Source text: "each of the three participating laboratories collected data from 250 3000-trial 200 binary-sample experimental sessions, generated by 227 human operators." Article's "227 participants and roughly 2 million trials" checks out (3 × 250 × 3000 = 2.25M). Non-replication of the original effect confirmed.
- Bösch, Steinkamp & Boller 2006 — quote unchanged and previously verified; metadata real-correct (*Psychological Bulletin* 132(4):497–523).
- Maier, Dechamps & Pflitsch 2018 — quote unchanged and previously verified; metadata real-correct (*Frontiers in Psychology* 9:379).
- Remaining seven References entries — unchanged since the 2026-06-16 ledger; not re-verified this pass.

**Family resolution (§2.4 step 6).** Propagated the verified Stapp 2006 form corpus-wide: `obsidian/concepts/selection-only-channel.md` (1 References entry + 2 inline) and `obsidian/concepts/channel-class-taxonomy.md` (1 References entry + 1 inline). `obsidian/topics/brain-internal-born-rule-testing.md` left alone — its "(Stapp n.d.)" resolves to a different reference (the LBL *Selected works* index), so it is internally consistent.

### Currency Sweep

`find_superlative_claims` → 0 hits. No superseded-superlative exposure.

### Medium Issues Found

**M1 — quantitative band misstated (FIXED).** §"Per-second Ceiling" claimed aggregate bandwidth "can be either far below or comparable to the ~10 bits/s" of Zheng & Meister (2025) "depending on the assumed selection rate". At the article's own stated ε ≈ 10⁻³ and R ∈ [10⁷, 10¹²], the band is 7 to 7 × 10⁵ bits/s — i.e. comparable to **far above**, never far below. "Far below" requires varying ε, not R. Restated correctly, with the substantive point made explicit: the observed ~10 bits/s fixes only the *product* of ε and R, leaving both underdetermined. (The ε² arithmetic itself is correct: 10⁻⁶ / (2 ln 2) = 7.2 × 10⁻⁷.)

**M2 — decline-effect over-reach (FIXED).** "Either reading of 'decline' is therefore a theoretical signature" over-claimed: the article had just declined to take a side on the across-studies pattern. Narrowed to the *within-study* pattern, with the across-studies pattern marked neutral between the methodological and Generalised-Quantum-Theory interpretations.

**M3 — cross-link duplication (FIXED, length-neutral).** [interface-efficacy-and-the-cognitive-gap](/topics/interface-efficacy-and-the-cognitive-gap/) was described twice in near-identical terms (§Content-Confinement and §Distinguishing Observables). Trimmed the second. Second intro paragraph also de-duplicated against the first.

### Counterarguments Considered

- *"If Stapp's channel is excluded from selection-only, the Map loses its historical anchor."* Addressed rather than dodged: the article now states what it inherits from Stapp (outcome-level Born discipline) and what it changes (the slot). The anchor is real but narrower than previously claimed — an honest downgrade.
- *Ensemble-level epiphenomenalism* — engagement at §"No-Signalling" unchanged; the [ensemble-level-epiphenomenalism](/concepts/ensemble-level-epiphenomenalism/) link carries the concession honestly.

### Reasoning-Mode Classification (§2.6, editor-internal)

- Engagement with the energy-conservation objection (Collins, Pitts): **Mode One** — defeated on the objector's own physical commitments. Unchanged.
- Engagement with the ensemble-epiphenomenalism charge: **Mode Three** — honest boundary-marking; the article concedes ensemble invisibility rather than claiming refutation. Unchanged.
- Engagement with Stapp: **not adversarial** — antecedent-differentiation, newly made accurate.
- No editor-vocabulary label leakage in prose. Verified.

### Calibration / Evidential-Status Audit

No possibility/probability slippage. §"Empirical Signature Corridor" still explicitly disavows reading the corridor as positive evidence and names [possibility-probability-slippage](/concepts/possibility-probability-slippage/). The M1 fix *strengthens* calibration by replacing a vague "far below or comparable" with the stated parameter degeneracy. Diagnostic test passes: a tenet-accepting reviewer would not now flag any claim as overstated.

## Optimistic Analysis Summary

### Strengths Preserved

- The three derived limits (per-event log₂(N), per-second rate, content-confinement) — untouched.
- The corridor-as-bound-not-evidence discipline — untouched and reinforced.
- Within-study vs across-studies decline distinction — sharpened, not collapsed.
- Distinguishing-observables table — untouched.
- The Tenet 2 headline/definition split introduced 2026-08-02 — verified and preserved.

### Enhancements Made

- The Stapp correction turns a misattribution into a genuinely informative taxonomic point: the article now explains *why* the closest historical model is not an instance of the class it names, which is a stronger position than the false identity it replaced.
- Han & Choi's actual result (causality fixes the nonlocality bound via the probability-assignment rule) is a tighter argument than the fabricated sum-rules line it replaces.

### Cross-links Added

- [selection-only-channel](/concepts/selection-only-channel/) now load-bearing in the Stapp paragraph (was Further-Reading-only at that point).

## Length Check

Total 2854 → 2966 words. Decomposed: **prose 2650**, Further Reading 54, References 267. True argumentative body sits well under the 3000 soft target; the near-threshold total is reference-apparatus inflation per the reference-apparatus inflation rule. No condensation warranted. Net additions offset by three de-duplication trims.

## Remaining Items

- Optional: *Zygon* 41(3) page range for Stapp 2006 not in Crossref; supply if a fuller record is found.
- Optional, carried: primary-source citation for PEAR's original ~10⁻⁴ bits/bit figure (the Jahn et al. 2000 replication numbers are now verified, but the original PEAR figure still lacks its own cite).
- Optional, carried: Walach et al. 2014 venue-label precision (URL correct).
- Suggested: a primary citation for the higher-order-interference/superluminal-signalling result, if the Map wants that argument back in explicit form.

## Stability Notes

- **This article was NOT converged.** Five prior reviews, including one recorded as an exhaustive publisher-of-record pass, missed two fabricated quotations. The lesson is the one already in the corpus record: a metadata ledger is not a verbatim check. Future passes on citation-dense articles should extract the primary text and grep the quoted span, not confirm that the paper exists.
- **Do NOT reintroduce** either fabricated string. Both are now marked with explicit do-not-reintroduce corrections in the originating research note.
- **Do NOT re-identify the strict reading with Stapp's Process 1.** The slot difference is settled and is stated consistently across [selection-only-channel](/concepts/selection-only-channel/), [channel-class-taxonomy](/concepts/channel-class-taxonomy/), [brain-internal-born-rule-testing](/topics/brain-internal-born-rule-testing/) and now this article.
- **Do NOT re-date Stapp QID to *Zygon* 40(1):29–44** — that figure, carried in the 2026-06-16 and 2026-07-09 reviews, is wrong. Crossref gives 41(3), 2006.
- Bedrock framework-boundary disagreements (eliminativist, hard physicalist, MWI, Buddhist) remain bedrock — not re-flagged.