---
title: "Deep Review - Essential vs. Contingent Consciousness of the Non-Physical Aspect"
created: 2026-08-08
modified: 2026-08-08
human_modified:
ai_modified: 2026-08-08T12:48:11+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-08-08
last_curated:
---

**Date**: 2026-08-08
**Article**: [[essential-vs-contingent-consciousness|Essential vs. Contingent Consciousness of the Non-Physical Aspect]]
**Previous reviews**: [[deep-review-2026-07-16-essential-vs-contingent-consciousness|2026-07-16]], [[deep-review-2026-06-06-essential-vs-contingent-consciousness|2026-06-06]], [[deep-review-2026-05-27-essential-vs-contingent-consciousness|2026-05-27]]

## Selection Rationale and Lens Choice

Staleness pick: 23 days since `last_deep_review` (2026-07-16), three prior reviews. `ai_modified` read 2026-08-05, but that commit was a two-line citation fix propagated from a *different* article's review; the argumentative body was 23 days stable. A changed-since-review delta pass would have inspected one reference line and no-opped.

The 07-16 review closed with "**Citation ledger complete (2026-07-16)** — all eight external references real-correct at the publisher of record. Future reviews may skip the full §2.4 pass unless the References block or body citations are modified." That permission was taken up. **Re-running the metadata ledger was deliberately declined as the one pass guaranteed to find nothing.** This review ran three lenses the prior three passes did not:

1. **Classical-source fidelity** — do the glosses of Sanskrit primary texts say what those texts say?
2. **Verbatim quote attribution** — is each quoted span actually in the work it is attributed to?
3. **Citation framing accuracy** — are real, correctly-cited authors framed as holding what they hold?

All three found defects. The metadata ledger would have found none, and worse: the 05-27 ledger had **explicitly certified the largest defect as correct**.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. `Mandukya Upanishad` misdescribed — wrong number of states, and *prajna* misidentified as the continuous witness. FIXED.**

The article read: "The *Mandukya Upanishad*'s analysis of the **three** states — waking, dream, dreamless sleep — places a continuous witnessing consciousness (***prajna***) beneath all three."

Two errors in one sentence. The Mandukya analyses **four** quarters (*padas*), not three. And *prajna* is the name of the self **in the third quarter, the deep-sleep state** — it is not the witness beneath all three. The witnessing consciousness said to underlie the other three is ***turiya***, the fourth.

This was not a subtle reading. **Two sibling articles in the Map already state it correctly**, which makes the error an internal inconsistency as well as a source error:

- `topics/contentless-awareness-evidence.md` L39: "The *Mandukya Upanishad* analyses consciousness into **four**: waking, dream, dreamless sleep (*sushupti*), and *turiya*, the witnessing awareness said to underlie all three."
- `voids/sleep-consciousness-void.md` L93: "Turiya is not a fourth state alongside the others but the witnessing background underlying all three. The Mandukya Upanishad identifies this **fourth** state."

Verified externally against the Mandukya's own division of quarters (Vaishvanara / waking; Taijasa / dream; **Prajna / deep sleep**; **Turiya / the fourth, underlying and transcending the three**), corroborated by the IEP *Advaita Vedanta* entry, which describes the three states "pointing to *turiya*, pure consciousness … the fourth nameless state."

**The 2026-05-27 review ledger listed this exact clause as verified correct**: "*prajna*, *Mandukya Upanishad* three-states analysis … — correct." A metadata-shaped attribution check ratified it; only reading the gloss against the primary text's own structure caught it. This is the orthogonal-lens pattern in its clearest form.

Fixed to: "The *Mandukya Upanishad* analyses four states: waking, dream, dreamless sleep — in which the self is called *prajna* — and *turiya*, the fourth, the witnessing consciousness said to underlie the other three."

Note the article's argument is *unharmed* and slightly strengthened — it already invoked *turiya* correctly two sections later ("Contemplative claims to have 'witnessed' deep sleep (the *turiya* tradition)"). The article was inconsistent with itself.

**2. `"zero-person perspective"` presented as a Metzinger quotation; it is not in the cited work. FIXED.**

The article read: "Thomas Metzinger's contrasting position — that for-me-ness is a contingent feature, in principle absent in "minimal phenomenal experience" with a **"zero-person perspective"** — is the contingentist rival."

Two quoted coinages in one clause, attributed to Metzinger. The article's only Metzinger reference is Metzinger (2020), *Philosophy and the Mind Sciences* 1(I), 1–44.

Downloaded the publisher PDF (DOI 10.33735/phimisci.2020.I.46 → `philosophymindscience.org/index.php/phimisci/article/download/8960/8538/6263`, 22,514 words) and grepped it:

- **"zero-person" / "0-person": 0 occurrences.** The only instance of the string `zero` in the entire paper is "Zero brightness means zero phenomenal experience."
- **"for-me-ness" / "mineness": 0 occurrences in the body.** The single match is a bibliography entry — Kriegel's chapter in an edited volume *titled* *The sense of mineness*.
- **"Zahavi": appears only twice, both as a volume *editor* in bibliography entries.** Metzinger does not engage Zahavi in this paper.

Guarded against the false-absence traps before concluding: re-ran case-insensitively, re-ran on a whitespace-collapsed and de-hyphenated whole-document stream (to defeat line-break hyphenation), and re-extracted with a second engine (`pdftotext -layout`). All four passes agree.

**Where the phrase actually comes from:** the earliest published locus found is **Shigeru Taguchi (2019), "Extreme obviousness and the 'zero-person' perspective," *Metodo: International Studies in Phenomenology and Philosophy*** (DOI 10.19079/metodo.s1.3.15) — a phenomenologist, not Metzinger. An OpenAlex full-text query restricted to Metzinger's author record returns exactly one "zero-person" hit, and that record is a **book review** of *The Elephant and the Blind* published in *Perspectives on Science and Christian Faith*, not Metzinger's own text.

**What I could not verify:** I did not obtain the full text of Metzinger's *The Elephant and the Blind* (MIT Press, 2024) — both the MIT Press OA preview and the PhilPapers archive copy returned Cloudflare interstitials rather than PDFs. **I therefore cannot say the phrase is absent from Metzinger's corpus**, only that it is verifiably absent from the work this article cites. Per the citation-verify-false-negative discipline the phrase was **not deleted corpus-wide**; see Remaining Items.

Fixed by replacing the unverifiable quotation with Metzinger's own grep-verified 2020 vocabulary — "minimal phenomenal experience", "pure awareness", *selfless*, *aperspectival*, *epistemic agent model*, *tonic alertness* — every one of which was confirmed present in the downloaded PDF before use.

**3. Metzinger recruited as "the contingentist rival" against his own conclusion. FIXED.**

This is the framing defect: the citation is real and correctly formatted, and the author is nonetheless made to underwrite a position he does not hold. It is the fourth confirmed instance of the Map recruiting a physicalist as an anti-physicalist (or here, cross-framework) witness.

Two distinct slips:

- **Scope slip.** The article defines contingent consciousness as "a substance or bearer that *has* consciousness when conditions are met and lacks it otherwise" — a claim about *consciousness*. Metzinger's contingency claim is about *selfhood*: MPE is a **phenomenal state throughout**. Nothing in his account describes an unconscious bearer persisting across a gap. Calling him "the contingentist rival" without qualification maps for-me-ness-contingency onto consciousness-contingency.
- **Direction slip, producing an internal inconsistency.** Because MPE is contentless awareness that persists when self and content are stripped, Metzinger's programme is, if anything, evidence in the *essentialist's* direction. The article already used it that way two sections later — "including Metzinger's minimal-phenomenal-experience program alongside the *turiya* reports" as candidate evidence for contentless awareness. So the same author was the contingentist rival in one section and essentialist-side evidence in another.

Also unstated: Metzinger's naturalism. The 2020 paper says outright (§ preamble) that "the MPE approach as sketched out here operates under naturalistic background assumptions," and its abstract concludes that pure awareness "really is the content of a predictive model, namely, a Bayesian representation of tonic alertness."

Fixed by adding two explicit qualifications — that his contingency claim concerns selfhood rather than consciousness, and that he writes under naturalistic assumptions the Map declines while drawing on the phenomenology. The Map's sibling `voids/edge-states-and-void-probes.md` L102 already models exactly this discipline ("This is a disagreement *within* Metzinger's framing, not support drawn from it"); this article now matches it.

### Medium Issues Found

**4. Same canonical report rendered two incompatible ways. FIXED.**

The classical Advaita waking report appeared twice in different English:

- L54: "I slept well; I knew nothing."
- L90 (evidence table): "I slept dreamlessly, knew nothing"

Presented as the same datum, at most one can be a faithful rendering. The Sanskrit is *sukham aham asvāpsam, na kiñcid avediṣam* — *sukham* is "happily / well", **not** "dreamlessly" (the dreamless-sleep state is *sushupti*, a separate word the article uses correctly elsewhere). The table's rendering silently translated the state-name into the verb.

Neither rendering was attributed to a translator, which is itself the finding for a formula with many published English versions. Harmonised to "I slept well; I knew nothing" — the form used at L54 and in the sibling `contentless-awareness-evidence.md` L39, so the corpus is now consistent on this quoted datum.

**5. `Nyaya Sutra` 1.1.10 glossed as an ontological claim it does not make. FIXED.**

The article read: "According to the *Nyaya Sutra* (Gautama, c. 2nd century CE, 1.1.10), the self is **the locus of** desire, aversion, effort, pleasure, pain, and cognition."

The sutra — *icchā-dveṣa-prayatna-sukha-duḥkha-jñānāni ātmano **liṅgam*** — states that these six are the **marks (*liṅga*)** of the self: the inferential signs by which its existence is established. That is an epistemological claim about how the self is *known*, not an ontological claim about what it *bears*. Nyaya does independently hold the self to be the substrate (*āśraya*) of these qualities, so the article's content is not false Nyaya — but it is not what 1.1.10 says, and the cite is pinned to that sutra.

Notably, the 2026-07-16 ledger **supplied the correct Sanskrit and the correct gloss** ("are the marks (liṅga) of the self") and then recorded the article's "locus" wording as **real-correct** — the verification found the right text and did not compare it to the sentence it was verifying.

Re-framed to "lists desire, aversion, effort, pleasure, pain, and cognition as the *marks* (*linga*) by which the self is inferred — signs that the self is present, not constituents of what it is." The argument is preserved and the original "but none of these defines it" point now follows directly from the sutra rather than around it.

**6. `Mandukya Upanishad` cited inline with no References entry. FIXED.**

§2.4 cross-reference rule: every inline citation needs a References entry. The Mandukya was load-bearing in the Advaita section and absent from the bibliography. Added, using the same Radhakrishnan (1953) *The Principal Upanishads* edition the sibling `contentless-awareness-evidence.md` L98 already cites, so the corpus resolves the text to one edition.

### Full Body Quote Ledger (9 spans, frontmatter stripped)

| Span | Attributed to | Verified against | State |
|---|---|---|---|
| "I slept well; I knew nothing." (L54) | generic waking report, Advaita | standard rendering of *sukham aham asvāpsam…*; matches sibling article | real-correct (unattributed by design — a stylised report, not a scripture quotation) |
| "I slept dreamlessly, knew nothing" (table) | same datum | *sukham* ≠ "dreamlessly" | **inconsistent-rendering — harmonised** |
| "pure consciousness" (L68) | gloss of *purusha* | standard Samkhya gloss | real-correct |
| "minimal phenomenal experience" (L80) | Metzinger 2020 | verbatim in paper title | real-correct |
| "zero-person perspective" (L80) | Metzinger 2020 | **0 occurrences in the cited PDF** (4 extraction passes) | **not-in-cited-source — removed** |
| "for-me-ness" (L80) | Zahavi | Zahavi's own term — correct as Zahavi's | real-correct as used of Zahavi; **mis-applied to Metzinger, who never uses it — re-framed** |
| "I was aware but remember nothing" (L48) | — | article's own constructed contrast | not a citation |
| "I was not aware," (L48) | — | article's own constructed contrast | not a citation |
| "where does consciousness go in dreamless sleep?" (L94) | — | article's own question | not a citation |

### Calibration Check (§2)
Passes, unchanged. "The Map's Reading" still performs the diagnostic test in the body. No possibility/probability slippage; the essentialist lean is labelled a commitment throughout. The Metzinger fix *improves* calibration by removing an implied external ally.

### Reasoning-Mode Classification (§2.6)
- Engagement with Nyaya: **Mode Three** (framework-boundary marking) — declined "on coherence grounds rather than evidential ones." Unchanged, no boundary-substitution.
- Engagement with Metzinger: previously an implicit **boundary-substitution risk** — his naturalistic conclusion went unmentioned while his phenomenology was enlisted. Now **Mode Three explicit**: the phenomenology is drawn on, the metaphysics openly declined. No editor-vocabulary leakage in prose.

## Optimistic Analysis Summary

### Strengths Preserved
- The "Two Theses, Sharply Drawn" limiting-case framing.
- The symmetric dreamless-sleep evidence table (same datum, two readings, identical prediction) — the article's strongest structural move.
- The regress-termination contrast (Advaita → self-luminosity; Nyaya → causal apperception *anuvyavasaya*).
- The Samkhya "relocation of the question" move.
- The exemplary evidential restraint in "The Map's Reading" — tenet-as-evidence-upgrade explicitly declined as a thing *not* done.

### Enhancements Made
The Metzinger passage gained a genuine philosophical point it previously lacked: that MPE cuts toward the essentialist side, which sharpens rather than blunts the article's own dichotomy. Word count 2767 → 2932 (+165), still below the 3000 soft threshold, so the expansion needed no offsetting cut.

### Cross-links Added
None. Existing link set already resolves.

## Remaining Items

**Corpus sweep required — `"zero-person perspective"` attribution.** The phrase is attributed to Metzinger in eight further live content files (`concepts/self-and-self-consciousness` ×3, `concepts/witness-consciousness`, `voids/edge-states-and-void-probes` ×7 including a section heading, `voids/minimal-consciousness-void`, `topics/eastern-philosophy-consciousness`) plus six archive files. **This must not be mass-deleted**: the phrase is verifiably not in Metzinger (2020), but I could not obtain *The Elephant and the Blind* (2024) to check whether he adopted it there, and Taguchi (2019) is a real published locus. Task minted at P2 to (a) obtain the book text, (b) determine whether the phrase is Metzinger's, Taguchi's, or a Map coinage, and (c) propagate one canonical attribution. Until then the phrase stands elsewhere unmodified.

## Stability Notes

Three prior reviews called this article converged. It was not — but the residue was invisible to the lens those reviews used.

- **The convergence claim was lens-relative, not article-relative.** The 07-16 review's closing permission ("future reviews may skip the full §2.4 pass") was correct and should stand: the metadata ledger *is* complete and re-running it wastes a slot. The error was treating a complete metadata ledger as a complete verification. Four of this pass's six findings sat in text whose citations were all real, correctly attributed, and correctly formatted.
- **A prior ledger explicitly certified two of the defects.** 05-27 certified the *prajna* gloss "correct"; 07-16 supplied the correct Sanskrit for *Nyaya Sutra* 1.1.10 and then certified the divergent paraphrase "real-correct". Ratification by a prior review is not evidence; re-derive from the primary text.
- **Sibling-article disagreement is a high-yield signal.** Two of the six findings were detectable by grepping the corpus for the same claim: the Map's own articles already had the Mandukya right and the sleep-formula rendering consistent. A cheap cross-sibling consistency grep should precede the expensive web pass.
- Eliminative-materialist / physicalist rejection of the presupposed non-physical aspect remains a **bedrock framework-boundary disagreement**. Do not re-flag.
- The essential-vs-contingent choice remains **underdetermined by evidence** and held as a defeasible commitment. Correctly calibrated. Do not pressure it up the evidential-status scale.
- **Nyaya remains the contingent-consciousness outlier**, declined on coherence not evidential grounds. Do not recast as refutation.
- **Metzinger is now correctly positioned and should not be flipped back.** He is a naturalist whose MPE work concerns the contingency of *selfhood*, not of consciousness; he is not a contingentist in this article's sense. A future review must not re-simplify him into "the contingentist rival."
