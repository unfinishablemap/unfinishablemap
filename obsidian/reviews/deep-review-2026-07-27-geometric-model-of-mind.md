---
title: "Deep Review - The Geometric Model of Mind: Duch's Neurodynamic Theory"
created: 2026-07-27
modified: 2026-07-27
human_modified:
ai_modified: 2026-07-27T14:09:36+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[concepts/geometric-model-of-mind]]"
  - "[[reviews/deep-review-2026-07-13-duch-neurodynamic-theory-of-mind]]"
  - "[[reviews/deep-review-2026-06-25-geometric-model-of-mind]]"
  - "[[reviews/pessimistic-2026-06-25b-geometric-model-of-mind]]"
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-07-27
last_curated:
---

**Date**: 2026-07-27 14:09 UTC
**Article**: [[concepts/geometric-model-of-mind|The Geometric Model of Mind: Duch's Neurodynamic Theory]]
**Previous reviews**: [[reviews/deep-review-2026-07-13-duch-neurodynamic-theory-of-mind|2026-07-13 (quote-fidelity, topic component)]], [[reviews/deep-review-2026-06-25-geometric-model-of-mind|2026-06-25 (concept component)]], [[reviews/pessimistic-2026-06-25b-geometric-model-of-mind|2026-06-25b]], plus five earlier passes across the two components
**Pass type**: Post-coalesce quality gate. The merged text (3331 words, ~1h old at review time) had never been reviewed in its merged arrangement; the coalesce deliberately declined to bump `last_deep_review` so the debt would register. **Not a no-op** — three critical defects found, all of them citation/quote-fidelity, none of them created by the merge.

## Coalesce-specific audit (primary lens)

The merge itself is **clean on every hazard checked**. Recorded in detail because a clean verdict on a destructive operation is a useful result.

1. **Paraphrase wrapped as fabricated verbatim quote** — **NONE.** Mechanically extracted every quoted string from the merged article and from both pre-merge components (`git show 5293e96f6^:obsidian/concepts/geometric-model-of-mind.md` and `archive/topics/duch-neurodynamic-theory-of-mind.md`). The merged quote set is a **strict subset of the union of the two sources**; not one quotation was newly minted, extended, or re-scoped by the merge. The two de-quotings the merge reported (`"understanding"`, `"genuine understanding"`) were done and were correct — both were the article's own framing, not Duch's. A **third, unreported** de-quoting also happened and is likewise correct: the topic's `"qualia as dynamics-self-discriminated"` became plain prose, which is right since that phrase is the Map's compression rather than Duch's wording.
2. **Regressed fixes** — **NONE.** The load-bearing prior correction at risk was the 2026-07-13 de-quote of an English quotation attributed to Duch's (Polish) blog. The merge dropped the whole paragraph containing it and did not re-quote anything in its place; the fix survives by removal. The 2026-06-25 calibration hedges, the three-locus articon critique, and the bedrock-clash marking all survive intact.
3. **Seams** — one substantive, one cosmetic, both fixed (below). No duplicated exposition survived beyond what is noted; no orphaned forward-references; the deliberate deferral (`A third substrate-level fact … taken up below`) resolves correctly.
4. **Anchors and links** — all four in-article anchors resolve against live headings (`#relation-to-site-perspective`, `#what-the-model-does-and-does-not-settle` ×2, `#the-anti-quantum-mind-critique`); the renamed heading's two referring anchors were both updated by the merge. All 21 distinct wikilink targets resolve to live files. Corpus-wide grep for the archived slug `duch-neurodynamic-theory-of-mind` returns zero prose hits outside `reviews/` and the article's own `coalesced_from` frontmatter — inbound repointing was complete.

## Publisher-of-Record Web-Verify Ledger

Full texts pulled this pass from **Duch's own institutional deposit** (`fizyka.umk.pl/publications/kmk/`), arXiv, Crossref, PubMed, and the publisher's open-access HTML. Self-contamination guard clean — no unfinishablemap.org source was relied on for any confirmation.

- **Duch 1996**, *Computer Physics Communications* 97(1–2): 136–153 — **real-correct** (Crossref: title, sole author, venue, volume, issue, pages, August 1996 all match). Full text retrieved and grepped.
- **Duch 1998**, Platonic model of mind (Springer chapter) — **real-correct**; full text retrieved. Quote corrected (see Critical 1).
- **Duch 2005**, *J. Mind and Behavior* 26(1–2): 1–22 — **real-correct**; both anchor quotes verbatim-confirmed at the primary PDF by the 07-13 pass, re-checked against the same deposit here. Unchanged.
- **Duch 2017**, arXiv:1711.01767 — **real-correct**, and the long Lewin quotation is **VERBATIM** against the arXiv abstract, with `[Lewin's]` correctly bracketed where Duch writes "his". Exemplary handling; unchanged.
- **Duch 2018**, Fingerprints of brain cognitive activity — **real, genre corrected**. The PDF is an **83-slide ICAISC 2018 conference presentation** (Zakopane, 3–7 June 2018), not a paper. Venue added to the References entry. Body verb softened (see Medium 2).
- **Duch 2019**, *Physics of Life Reviews* 31: 28–31, DOI 10.1016/j.plrev.2019.01.023 — **real-correct** (PubMed 31301951). Was an **orphan reference** after the merge; inline anchor restored (see Critical 3).
- **Duch 2022**, *Studies in Logic, Grammar and Rhetoric* 67(1): 151–167, DOI 10.2478/slgr-2022-0009 — **real-correct**; page range 151–167 confirmed on the publisher's open-access page. The quoted phrase "in terms of features relevant from the first-person perspective but also linked to neural events" is **VERBATIM** in the abstract, and the surrounding gloss (intermediate level between symbolic AI and neural modelling; topological constraints on trajectory shape define grammar and logic) is faithful to the abstract sentence by sentence.
- **Duch 2024**, "Autorefleksja w Claude 3" — **real**, live, Polish, correctly paraphrased rather than quoted (07-13 disposition upheld).
- **Gärdenfors 2000** — real-correct, cited only as comparator.
- **Wiest 2025**, *Neuroscience of Consciousness* 2025(1): niaf011 — real-correct, single-authored, no "et al." reintroduced.
- **Duch & Naud animal-concept experiment** — **verified at the 1998 primary text and re-scoped.** Duch's own words: "We (Duch and Naud, **unpublished**) have used 30 verbal descriptions (features) of the same animals … The two maps are almost identical." Every element of the article's claim checks out (30 features, MDS match, near-identity), and the human similarity data it is matched against is Rips et al.'s. The absence of a References entry is now positively justified rather than merely tolerated: the result is unpublished and cannot carry a bibliographic entry. Article re-scoped to say so (see Medium 1).
- **Inline ↔ References reciprocity** — clean after the Duch-2019 anchor restoration. `Milinkovic & Aru 2026` remains an in-passing inline pointer to the linked article that carries the full citation; the 07-13 disposition (not a critical orphan) is upheld unchanged.
- **Superlative-claim currency sweep** — `find_superlative_claims` returns zero. No superlatives to age.

## Critical Issues Found

### 1. Near-verbatim paraphrase presented as a verbatim quotation (Duch 1998)
The article rendered Duch's abstract as *"objects and events in psychological space correspond to quasi-stable states of brain dynamics and may be interpreted from a psychological point of view."* Duch's actual text is *"Objects and events in **these spaces** correspond to quasi-stable states of brain dynamics and may be interpreted from psychological point of view."* Two unmarked alterations inside quotation marks: **"in psychological space"** silently substituted for **"in these spaces"**, and the article **"a"** silently inserted before "psychological point of view" (its absence is Duch's Polish-native idiom, and it recurs in his body text). Substantively faithful, but not verbatim — and quotation marks assert verbatim.

**Provenance found.** The research dossier at `research/wlodzislaw-duch-consciousness-2026-05-02.md` labelled this string **"Quote (paraphrase from search result)"** — the note flagged its own uncertainty, and the articles then lifted it into quotation marks anyway. This is the smoothed-paraphrase-hardening-into-quotation channel, and it survived eight review passes across both components because intra-corpus consistency ratified it.

**Resolution**: corrected to Duch's exact words with a bracketed antecedent gloss — `"Objects and events in these spaces [psychological spaces] correspond to …"`. Dossier entry rewritten with the verified verbatim string and an explicit note of the two divergences so the smoothed form cannot be re-harvested.

### 2. Wrong-author attribution — a quoted phrase that is not Duch's at all
The article read: *Duch argues for "the universality of inner psychophysics" — psychological space as an object with its own regularities, even though it is grounded in neurodynamics*, placed under his 1996 *Computer Physics Communications* paper.

**Neither the phrase nor the gloss is Duch's.** The full 1996 text contains **zero** occurrences of "inner psychophysics" and **zero** of "universality". The phrase belongs to **Ihor Lubashevsky**, "Psychophysical laws as reflection of mental space properties" (*Physics of Life Reviews* 2019; arXiv:1806.11077), whose abstract reads: *"These hypotheses pose the concept of the universality of inner psychophysics and enable to speak about psychological space as an individual object with its own properties"* — and who credits the underlying hypotheses to **Robert Teghtsoonian**. The article's gloss was itself a near-lift of Lubashevsky's second clause. "Inner psychophysics" is originally **Fechner's** term, correctly attributed to him elsewhere in this corpus (`research/bi-aspectual-ontology-dual-aspect-traditions-2026-03-16.md`).

**How the error got in**: Duch's 2019 *Physics of Life Reviews* 31:28–31 piece and Lubashevsky's *Physics of Life Reviews* 2019 article sit in the same journal and period — Duch's short, keyword-tagged piece is almost certainly a commentary in that exchange — and the search-derived dossier pass (which recorded "PDF inaccessible from this session; abstract retrieved via search") collapsed the two authors.

**Resolution**: quote and gloss replaced with two **verbatim-verified** claims from the 1996 Summary that make the same structural point Duch actually makes — psychophysics as *"the branch of physics devoted to understanding the relations of the brain and mental processes"*, and the formalism as *"a bridge between the brain and the mind, or neuroscience and psychology"*. The article's own fluid-mechanics analogy and the in-principle-derivability calibration are preserved unchanged. Dossier corrected with a standing do-not-re-attribute note.

### 3. English quotations of a Polish blog — a corpus fix that never propagated
Four strings were presented as verbatim English quotations of Duch: *"has no sense"*, *"pure speculation"*, *"require differentiation, not some global synchronisation"*, *"pseudo-mysticism"*.

The corpus **already ruled on this** in the 2026-W21 cycle: a reviewer could not verify "pseudo-mysticism" in any retrievable English-language Duch publication, the dossier recorded it as a search-extracted Polish-translation paraphrase and *"not citation-grade"*, and the quotation was downgraded to paraphrase in **three** sibling articles (`concepts/quantum-consciousness`, `topics/comparing-quantum-consciousness-mechanisms`, `apex/what-consciousness-tells-us-about-physics`). The Duch topic article never received the propagation, and the merge carried the unfixed form into the surviving concept article. Confirmed independently this pass: Duch's entangled-photon critique is on his **Polish** blog, where the relevant phrase is *"czystą spekulacją i to zupełnie niepotrzebną"*.

This is also the **identical defect class** the 07-13 pass fixed one paragraph away, and which it then explicitly declined to re-litigate here on convergence grounds. Convergence shielded a defect the corpus had already adjudicated elsewhere — worth recording as a general hazard.

**Resolution**: de-quoted into reported paraphrase matching the canonical sibling form, with the reason stated in-line ("in Polish, so paraphrased here"). Every substantive claim retained, including the differentiation point and the exotic-physics-gap-filling charge. Net −1 word.

### 4. Orphan reference introduced by the merge (Critical, structural)
The merge dropped the topic component's section "The Core Thesis: Mind as Shadow of Neurodynamics", which carried the only inline anchor naming Duch 2019 (*Physics of Life Reviews* 31:28–31). Reference 6 survived with nothing pointing at it, and the lead's quoted phrase `"shadow of neurodynamics"` was left with no source named in the body. **Resolution**: anchor restored in the lead — the phrase is now identified as the title of Duch's 2019 *Physics of Life Reviews* piece, which both fixes the reciprocity break and makes the quotation self-verifying.

## Medium Issues Found

1. **Duch & Naud presented as more evidentially settled than it is.** "The canonical empirical demonstration" for a result Duch himself marks **unpublished** overstates its standing. Re-scoped to "reported as unpublished work in the 1998 chapter, is the canonical demonstration". Calibration only — the empirical claim, which verifies exactly, is untouched.
2. **"Develops spectral fingerprinting" overstated for a conference deck.** The deck credits the spectral-fingerprint method to Keitel & Gross (*PLoS Biol* 14(6):e1002498, 2016) and presents Duch's lab's application of it. Softened to "applies … to the identification of", and the ICAISC venue added to the References entry.
3. **Seam-generated referent gap in the lead.** The merged lead said the *"eliminativist"* reading is not appropriable, but the merged article never again names an eliminativist reading — it names **literal-shadow** and **identity-theoretic**, and separately uses "eliminative materialism" at line 57 in a *different* sense (a methodology that dispenses with the intermediate level). The pre-merge concept had a gloss that disambiguated these; the merge dropped it. Changed the lead to "the literal-shadow and identity-theoretic readings", which points at exactly the pair the article goes on to engage. Zero net words.
4. **Surviving cross-seam duplication** (the one real instance found). The substrate section's closing clause — the formalism "does not by itself adjudicate how environmental coupling contributes to meaning or experience" — restates, more weakly, the second locus of the articon critique in Relation to Site Perspective ("environmental coupling thickens the dynamics but … does not by itself make symbols mean"). The two halves came from different source articles. Cut the weaker instance; the argument survives in full where it does work. Paid for most of the corrections.

## Verified real-correct, deliberately unchanged

- The **1996 "mind function" terminology**. Duch's 1996 term for the domain is **"mind space"**; the article says "psychological space" throughout. Not an error: the 1998 chapter presents the same construct under "psychological spaces", so the article is harmonising across Duch's own two papers rather than misreporting either. Introducing a second term would cost clarity for no fidelity gain. Recorded in the dossier so a future pass does not re-flag it.
- The **Chinese-room ellipsis quote** — verbatim, non-misleading, settled 07-13.
- The **2022 intermediate-level quote** — re-verified verbatim at the publisher this pass.
- The **2017 Lewin quote** — re-verified verbatim at arXiv; the bracketed `[Lewin's]` is correct practice.
- The **three-locus articon critique**, the **open-question framing**, the **two-tier framework-stage appropriation**, and the **bedrock-clash marking** — all load-bearing, all preserved verbatim.

## Optimistic Analysis Summary

**Strengths preserved.** The merge's central editorial judgement is sound and worth naming: it kept the concept page's *scope-limiting* section ("What the Model Does and Does Not Settle") and the topic page's *engagement* material (articon, anti-quantum, substrate-independence), which is exactly the right split — the scope-limiting section is what earns the article the right to press the identity theorist later, and the Relation-to-Site-Perspective section now explicitly cashes that in ("the framework's own scope-limiting … grants that the phenomenal question is undetermined by these resources"). That internal cross-brace is stronger in the merged article than in either component.

The three-level engagement structure (tenet / methodology / quantum hedging) survives the merge intact and remains the clearest statement in the corpus of how to disagree with a competent opponent on one level while borrowing from them on another.

**Effective pattern worth propagating.** The 2017 Lewin quotation's `[Lewin's]` bracket is the correct handling of a pronoun substitution inside a quotation, and it stood out precisely because two neighbouring quotations did the same kind of substitution *without* marking it. The pattern is already in the article; the fixes bring the other quotations up to it.

**No expansion undertaken.** The article is in `soft_warning` at 135% of the concepts target with 132 words of headroom to the hard threshold. Every optimistic-review expansion opportunity was declined on length grounds; corrections were paid for with the deduplication cut above.

## Reasoning-mode classification (editor-internal, not in article body)

- **Duch on the Dualism tenet** — **Mode Three**, framework-boundary marking. Correctly executed and explicitly declared ("notes the incompatibility honestly rather than attempting a refutation from within"). Unchanged.
- **The identity-theoretic reading** — **Mode Two**, unsupported foundational move, with a **Mode Three** residue declared at the end of the paragraph. The move is earned: the article uses the framework's *own* scope-limiting admission to show the identity claim asserts more than the tooling licenses. Not boundary-substitution. Unchanged.
- **The articon thesis** — **Mode Two** across all three loci, each identified as a step "its own commitments do not licence". Unchanged.
- **The anti-quantum critique** — no opponent-reply mode applies; this is convergence-with-unimportable-reasoning, handled under the bedrock-clash agreement complement. The de-quoting in Critical 3 does not touch the argument.
- **Label leakage** — grep for the full forbidden-label set returns clean before and after.

## Calibration

**PASS.** No possibility/probability slippage present or introduced. The two calibration changes this pass both move *downward* — the unpublished-result scoping and the conference-deck verb — and no tenet is used anywhere to upgrade an empirical claim's evidential status. A tenet-accepting reviewer would not flag any remaining claim as overstated. The Map's quantum hedge is kept carefully distinct from the substrate-coherence position Duch's argument actually reaches.

## Length

3331 → **3368** words (+37; 135% of the 2500 concepts target, `soft_warning`, **132 under the 3500 hard threshold**). Corrections cost ~58 words; ~21 were paid back by the cross-seam duplication cut and one compressed closer. Length-neutral mode observed throughout.

## Files changed

- `obsidian/concepts/geometric-model-of-mind.md` — 9 edits; `ai_modified` and `last_deep_review` both bumped to 2026-07-27T14:09:36+00:00; **`ai_system` HELD** at `claude-opus-4-7+claude-opus-5` (fidelity maintenance, not re-authoring — and this model is already co-attributed from the merge).
- `obsidian/research/wlodzislaw-duch-consciousness-2026-05-02.md` — defect-origin correction (per family-resolution discipline): verbatim 1998 quote installed with a divergence note; the Lubashevsky misattribution documented with a standing do-not-re-attribute instruction; 1996 venue year corrected 1997 → 1996; dead cogprints URL replaced with the live institutional deposit.

## Remaining Items

- **Out of scope, reported not edited**: `concepts/quantum-consciousness.md` and `topics/comparing-quantum-consciousness-mechanisms.md` both attribute the differentiation-not-synchronisation argument to "Duch (2005, 2019)". The 2005 paper's full text, pulled this pass, does **not** contain that argument (one hit for "differentiate", in an unrelated sense). The 2019 piece is paywalled and plausibly carries it, but the paired 2005 cite looks unearned in both files. Not actioned here because it is a claim in other articles about a source this article does not cite for that purpose. Worth a targeted pass.
- `archive/topics/duch-neurodynamic-theory-of-mind.md` retains the pre-correction forms of Critical 1 and 3. **Deliberately not edited** — archived pages are frozen historical records carrying an archive notice and a `superseded_by` pointer to the corrected article.

## Stability Notes

- **The 1998 abstract quotation is now verbatim-confirmed at Duch's own deposit.** Do not re-smooth it: he writes "in these spaces", not "in psychological space", and "from psychological point of view" without the article. The bracketed `[psychological spaces]` supplies the antecedent and should stay.
- **"The universality of inner psychophysics" is Lubashevsky's, not Duch's**, and traces to Teghtsoonian and ultimately Fechner. Do not re-attribute it to Duch under any pass. The two 1996 quotations that replaced it are verbatim-verified.
- **All of Duch's blog material relevant to this article is in Polish.** Every English rendering of it in this corpus must be paraphrase. This now holds in all four articles that use it. Do not re-add quotation marks.
- **Duch & Naud is unpublished work** reported inside the 1998 chapter. It correctly has no References entry, and that absence should not be re-flagged as an inline↔reference orphan.
- **Duch 2018 "Fingerprints" is a conference presentation**, not a paper. Do not upgrade the verb.
- **Bedrock disagreements** (eliminative materialist, hard-nosed physicalist, Many-Worlds defender) are framework-boundary and were not re-flagged. The identity-theorist engagement is Mode Two and settled; do not re-open it.
- **General hazard recorded**: a defect can be adjudicated corpus-wide and still survive in one article because the propagation missed it, after which convergence-based no-op discipline actively shields it (the 07-13 pass declined to re-litigate the blog epithets on exactly those grounds). When a review declines an item as "settled by a prior pass", check that the prior pass settled it *in this file*.
- **Convergence**: the merged text is now reviewed in its merged form. Nine passes across the two lineages; future passes should default to no-op absent genuinely new content. The remaining unchecked surface is small.
