---
title: "Deep Review - Cognitive Integration and the Self"
created: 2026-09-11
modified: 2026-09-11
human_modified:
ai_modified: 2026-09-11T18:39:27+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[cognitive-integration-and-the-self]]"
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-09-11
last_curated:
last_deep_review:
---

**Date**: 2026-09-11
**Article**: [[cognitive-integration-and-the-self|Cognitive Integration and the Self]]
**Previous review**: [[deep-review-2026-06-25-cognitive-integration-and-the-self|2026-06-25]] (clean no-op); intervening [[pessimistic-2026-09-03-cognitive-integration-and-the-self|pessimistic 2026-09-03]] (5 numbered issues, all actioned by commit `8a95f7afd9`, 2026-09-11 00:30Z)
**Pass**: fresh-work tail. The 77-day `last_deep_review` staleness score was misleading — the body is 18 hours old. The adversarial lens was **not** re-run on the five freshly-fixed issues; this pass audited the new prose for defects introduced by the fix.

## Verdict: one critical fix (substituted qualifier in an attributed claim) + one zero-cost reference-ordering fix

The 2026-06-25 stability note predicted "a genuine no-op unless the body changes." The body did change, and the fresh-work tail delivered exactly one real defect — in a sentence added yesterday that cites the positions register as its authority while wording the register's reason differently.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Substituted qualifier changed an attributed claim about List (FIXED).**
The new P-I5 sentence in the No Many Worlds section read:

> against first-personally centred readings such as List's, **which build the privileged present into the ontology**, the indexical objection still engages but drops to supplementary

The load-bearing feature of List's centred-worlds ontology — the one that makes the indexical objection drop to supplementary — is **first-person privilege**, not a privileged *present*. The corpus is unanimous on this across five independent files, all using the same formula ("the first-person privilege the indexical objection demands is built into the ontology"):

- [[positions/individuation-and-subjecthood]] P-I5 — the very entry the sentence cites: *"only the **indexical** argument still engages, and it drops to supplementary, because the first-person privilege it demands is built into the ontology"*
- [[arguments/many-worlds-argument]] L85 · [[apex/one-world-wager]] L66 · [[concepts/egocentric-presentism]] L63 · [[topics/vertiginous-question]] L162

Two compounding problems. First, the substitution conflates a *feature* of List's view ("exactly one present per subject", which the corpus does state) with the *reason* the objection weakens (first-person privilege). Second, "privileged present" is a term this corpus reserves for the A-theory / philosophy-of-time cluster — it occurs in `concepts/philosophy-of-time`, `topics/consciousness-and-the-ontology-of-temporal-becoming`, `concepts/retrocausality` and `tenets/tenets`, where it means presentism about time, a different claim entirely. Importing it here makes the article assert A-theoretic temporal privilege where the register asserts perspectival privilege.

This is a dropped/substituted-qualifier error in a claim attributed to a named philosopher, not a philosophical disagreement. **Resolution**: reworded to "which build first-person privilege into the ontology" — matches the register and all four corpus siblings, and is one word shorter.

### §2.4 Publisher-of-Record Citation Ledger

The trigger condition was met (a new reference landed yesterday). All seven cites verified; **one new cite verified for *use* as well as metadata**, which was the highest-yield check available on this article.

- **Rasch, B. & Born, J. (2013). "About sleep's role in memory." *Physiological Reviews* 93(2), 681-766** — state: **real-correct, and citation-*use* faithful**. Metadata confirmed at Europe PMC (PMID 23589831, DOI 10.1152/physrev.00032.2012) and independently at Semantic Scholar — exact match to the reference as written. **Use-fidelity checked against the raw full text**, not the abstract alone: the publisher PDF and UZH green-OA copy are bot-blocked, but PMC3768102 yielded 591,907 characters of full text. Both clauses of the body sentence are borne by the source:
  - *"reactivation of recently encoded representations occurs in slow-wave sleep and transforms them for integration into long-term stores, with ensuing REM sleep proposed to stabilize what has been transformed"* — near-verbatim from Rasch & Born's own abstract: *"Consolidation originates from reactivation of recently encoded neuronal memory representations, which occur during SWS and transform respective representations for integration into long-term memory. Ensuing REM sleep may stabilize transformed memories."* The article's hedge "proposed to stabilize" correctly tracks the source's "may stabilize".
  - *"For declarative memory the phase is predominantly slow-wave sleep rather than REM"* — borne verbatim in the full text: *"substantial evidence for the dual processes hypothesis, such as hippocampus-dependent declarative memories preferentially profiting from SWS, whereas nondeclarative aspects of memory, such as procedural, implicit, and emotional, additionally profiting from REM sleep"*, and earlier *"declarative memory profits from SWS, whereas the consolidation of nondeclarative memory is supported by REM sleep."* The article's "predominantly" is a faithful rendering of the source's "preferentially" — and the hedge is load-bearing, because the source also notes *"emotional declarative memories appear to additionally benefit from REM-rich late sleep."* An unhedged "declarative memory consolidates in SWS" would have overshot; "predominantly" does not.
- **Bortolan, A. (2020)** — state: real-correct (publisher-verified 2026-06-25; reference block unchanged since).
- **Crick, F. & Koch, C. (1990)**, *Seminars in the Neurosciences* — state: real-correct. **Fence respected, not disturbed** — journal title left correctly **plural**.
- **Gallagher, S. (2000)** — state: real-correct.
- **Gazzaniga, M. S. (2005)** — state: real-correct.
- **Gallagher, S. & Zahavi, D. (2012)**, 2nd ed., Routledge — state: real-correct. **Fence respected** — the 2021 3rd ed. was **not** substituted.
- **Zahavi, D. (2005)**, MIT Press — state: real-correct. **Fence respected** — year left at **2005**, not "corrected" to the aggregator's 2006.

**Inline ↔ References cross-reference**: 7 distinct inline cites, 7 reference entries, exact bijection. No orphans in either direction.

**Empirical-record currency sweep**: no superlative claims ("current record", "largest", "first to demonstrate", "to date") in the body. Skipped correctly.

### Medium / Low Issues Found

- **Reference list was mis-alphabetised (FIXED, zero word cost).** Gazzaniga (2005) sat between Gallagher (2000) and Gallagher & Zahavi (2012); "Gallagher, S. & Zahavi, D." sorts before "Gazzaniga, M. S." Pre-existing, not introduced yesterday — yesterday's insertion of Rasch & Born was correctly placed. Moved, not renumbered (the list is unnumbered, so no cross-references break).
- **Uncited empirical premise (DEFERRED, length-constrained).** "the best-supported consolidation window is the one from which dream reports are sparsest" rests on an uncited claim that dream recall is sparser from SWS than from REM. The claim is correct and textbook-level, and the Map's LLM-first style permits omitting background an LLM already holds — but it is the pivot of the "That profile weakens an inference" move, so it is doing argumentative work uncited. Adding a citation costs words the article does not have (4 below soft). Left as-is; recorded here so a future review need not re-derive the judgement.
- **Missing trailing newline at EOF.** Pre-existing, harmless. Checked for an end-of-file tool-tag artifact — the file ends cleanly at "MIT Press.", no artifact. No change.

### Checks Run That Found Nothing (recorded so they are not re-run)

- **Composition/ownership consistency — holds.** `constitutes indexical identity` → 0 (withdrawn claim fully gone); `composition` ×2, `ownership` ×4. All four ownership loci are consistent: the Integration and Indexical Identity section installs the distinction, the Dreamless Sleep section applies it correctly ("Neither alternative bears on the ownership question"), the No Many Worlds section turns on it ("What such a reading cannot supply is the ownership fact"), and the Further Reading gloss states it explicitly ("integration fixes which experiences compose a stream, not whose stream it is"). **No surviving passage leans on integration to settle ownership.**
- **`for-me-ness` ×2 — both correct, neither is an Issue-5 survivor.** Offsets 4104 and 4622, both in the Minimal Self section, both untouched by yesterday's commit. These are *definitional* uses of Zahavi's term ("what Zahavi calls 'for-me-ness'"; "for-me-ness is not added to consciousness but is its very form"), not assertions of unverifiable first-person facts about third parties. The Issue-5 locus was in Dissociative Disorders and is fixed there: "each alter **reports** experience in the first-personal mode. The evidence is report-based."
- **Hedging does not over-correct — it is register-mandated.** Checked the conditionals installed by Issue 3's fix against [[positions/quantum-interface]] first, since outer reviewers recurrently attack mechanisms the Map already disclaims. The register's mechanism-debt convention states: *"Any downstream article that asserts consciousness 'does causal work' and builds a practical or normative conclusion on it inherits this debt rather than discharging it, and should not read more confident than the register does upstream"*, and the 2026-08-13 convergence tightened this into an explicit citation grade — *"citable downstream as a framework-internal coherence result only, never as established mental causation."* The article's "inherits the Map's mechanism debt rather than discharging it" and "the self-forming picture is a framework-internal consequence" are near-paraphrases of that convention. The conditionals are correctly aimed at the **open** question (whether token-level selection can be causal while exactly Born-preserving — P-Q3/P-Q10), not at Tenet 3's assertion that consciousness influences the physical, which the article never conditionalises. No "would" undercuts a tenet the Map asserts outright.
- **P-I1 citation — holds, though the heading alone would suggest otherwise.** The article cites P-I1 for "the Map treats that [ownership] fact as primitive rather than constructed", and P-I1's heading is about subject *boundaries* (a composition notion) in an article that has just said boundaries do not supply ownership. Checked the entry body: the register glosses P-I1 as the determinate-subjecthood claim underwriting *"a non-deflationary fact about which subject is **this** one"*, and notes that retiring it "leaves Tenet 4's indexical objection with nothing to discriminate among." The citation is correct on the register's body; it is the heading that reads narrower than the position. Flagged here because a future review reading only the heading would plausibly mis-flag this.
- **P-I5 characterisation otherwise faithful.** "drops to supplementary", "the case there rests on a separate rejection of modal realism" — both match P-I5 verbatim in substance ("one supplementary argument plus a separate commitment: the rejection of the modal realism on which every subject's centred world is a real world").
- **All 21 wikilinks resolve.** Zero bare unresolved against a 2011-entry `build_content_index` (zero collisions). Yesterday's new bare target `clinical-dissociation-as-systematic-evidence` exists at `obsidian/topics/`. The caret anchors added yesterday all resolve: `tenets#^no-many-worlds`, `tenets#^minimal-quantum-interaction`, `tenets#^occams-limits` all present in `tenets/tenets.md`; the path-qualified `positions/quantum-interface#^mechanism-debt` resolves to the P-Q3 framing. The same-page `{#no-many-worlds}` anchor added yesterday matches its `[[#no-many-worlds]]` referrer. Bare position ids `P-I1` and `P-I5` both exist in `positions/individuation-and-subjecthood.md` and autolink correctly.
- **§2.6 reasoning-mode leakage — clean.** Zero occurrences of every forbidden editor-vocabulary label. The No Many Worlds section's "is honestly noted as such, not a refutation of many-worlds on its own terms" is the recommended natural-prose pattern, not a leaked label.
- **Style — clean.** Zero "load-bearing", zero "This is not X" construct.

### Counterarguments Considered

- **Everettian (branch-relative identity)**: fully absorbed, and absorbed *correctly*. The article concedes that "branches decohere rather than interfere, so a branch-relative Everettian can grant this article's whole account of binding and continuity, indexed to a branch." That concession is physically accurate and is the right one — the retired integration-fracture argument is gone and has not crept back.
- **Phenomenology-as-evidence**: the article now polices itself here — "every branch-relative successor feels the same continuity, so treating the feeling as confirmation reads felt weight as evidential weight." No calibration slippage to flag.
- **Split-brain (against basic phenomenal unity)**: engaged honestly, unchanged from prior reviews, and consistent with P-I3's epistemic (not metaphysical) agnosticism.

## Optimistic Analysis Summary

### Strengths Preserved

- The **composition/ownership** distinction is the strongest structural move in the article's history. It replaced a claim the article's own next sentence withdrew with a distinction that does real work in four separate sections, and it cost almost nothing in length.
- The **Rasch & Born inversion** is unusually good intellectual practice: the article did not merely fix a wrong citation, it noticed that the corrected science *weakens* the argument the passage was making ("the best-supported consolidation window is the one from which dream reports are sparsest") and said so, rather than quietly retaining the conclusion.
- The **variant-relative** treatment of the anti-many-worlds case (P-I5) means the article no longer claims uniform reach for the indexical objection.

### Enhancements Made

None beyond the two fixes. The article is 4 words below its soft threshold; expansion was not available and not warranted.

### Cross-links Added

None. Yesterday's commit already added `clinical-dissociation-as-systematic-evidence` and the `positions/quantum-interface#^mechanism-debt` deep link.

## Length

**2997 → 2996 words** (−1). Section is `topics/`: soft 3000, hard 4000. The article lands **4 words below soft**, status `ok` — it did **not** cross soft. The critical fix was chosen in its shortest faithful form partly for this reason: "the privileged present" (3 words) → "first-person privilege" (2 words). The longer and arguably more faithful "the first-person privilege the objection demands" would have landed at 2999 — still under, but with one word of headroom. Length-neutral mode was in force and was respected.

## Remaining Items

- The uncited SWS-dream-recall premise (see Low Issues). Not queued as a task; it needs ~15 words the article does not have, and the claim is correct.

## Stability Notes

- **The three citation fences from 2026-06-25 stand and were re-confirmed, not disturbed**: Crick & Koch's *Seminars in the Neurosciences* is correctly **plural**; Gallagher & Zahavi is correctly the **2nd ed. (2012)**, not the 2021 3rd; Zahavi's *Subjectivity and Selfhood* is correctly **2005**, not the aggregator's 2006. A future review that "corrects" any of these is introducing a defect.
- **New fence: "first-person privilege", not "privileged present".** The corpus formula for what List's centred-worlds ontology builds in is *first-person privilege* (P-I5 and four sibling articles). "Privileged present" belongs to the A-theory/philosophy-of-time cluster and means something else. Do not re-substitute.
- **The Everettian standoff is bedrock, not a defect.** The article states this itself: "many-worlds denies there is a further fact here rather than failing to accommodate one." A reviewer finding the indexical objection unsatisfying from inside Everettianism is registering the expected framework-boundary disagreement, and P-I5 already books the variant-relativity. Do not re-flag as critical.
- **The conditionals in Prospective Integration and Bidirectional Interaction are register-mandated, not over-hedging.** They are required by the [[positions/quantum-interface]] mechanism-debt citation grade (coherence-only). A future review that upgrades them to the indicative would be regressing a 2026-08-13 three-reviewer convergence.
- **The 2026-06-25 no-op prediction was correct in kind.** Its condition ("unless the body changes") was met, and the body change produced exactly one defect, in the newest sentence. Expect a genuine no-op on the next staleness re-selection if the body is stable — and note this article now has 6 prior reviews, so convergence damping should push it well down the pool.
