---
ai_contribution: 100
ai_generated_date: 2026-08-07
ai_modified: 2026-08-07 16:44:00+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-07
date: &id001 2026-08-07
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-07 16:44:00+00:00
modified: *id001
related_articles:
- '[[presence-type-and-absence-type-voids]]'
- '[[taxonomy-of-voids]]'
- '[[ineffable-encounter-void]]'
- '[[compound-failure-signatures]]'
- '[[cross-domain-void-comparison]]'
- '[[erasure-void]]'
title: Deep Review - Presence-Type and Absence-Type Voids
topics: []
---

**Date**: 2026-08-07
**Article**: [Presence-Type and Absence-Type Voids](/concepts/presence-type-and-absence-type-voids/)
**Previous reviews**: [2026-06-26](/reviews/deep-review-2026-06-26-presence-type-and-absence-type-voids/), [2026-05-31](/reviews/deep-review-2026-05-31-presence-type-and-absence-type-voids/), [2026-04-21](/reviews/deep-review-2026-04-21-presence-type-and-absence-type-voids/)
**Pass type**: Internal-citation-fidelity audit (the 2026-06-26 watch-item, executed) + orphan-reference repair + one-file family sweep
**Verdict**: Three critical defects fixed, all in the internal-citation channel; one upstream sibling corrected in the same defect family. Length 1809→2069w, comfortably under the 2500 soft threshold. External reference block unchanged and not re-verified (byte-identical, verified 2026-05-31); two *new* cites added and both publisher-verified this pass.

This pass was the direct execution of the watch-item the 2026-06-26 review left: *"this article quotes/paraphrases the apex and the sibling ineffable-encounter-void; when either is rewritten, re-grep this article's references."* Both siblings had moved. The article had not.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. The "seventh primary signature" claim was wrong three ways — and one of the errors sat in a section heading (a navigation surface).**

Line 88 asserted that the failure-signature framework has *six primary* signatures with *modular selective loss and wrong model selection among secondary signatures*, and that presence-type voids add a *seventh primary* signature. Under the heading `## The Seventh Failure Signature`. Verified against all three siblings:

- [compound-failure-signatures](/voids/compound-failure-signatures/) (lines 61–70) is a table of **eight coordinate rows** keyed by limit type — Logical/self-referential, Conceptual, Introspective, Modular, Pattern-matching, Model-based, Expressive, Meta-cognitive. It makes **no primary/secondary distinction whatsoever**. The parenthetical attributed to "the framework" a two-tier structure the framework does not have.
- [taxonomy-of-voids](/apex/taxonomy-of-voids/) (line 150) lists six recurring signatures and then says **"Two more complete the inventory"** — dissolution under attention (from the ineffable encounter void) *and* **silent erasure** (from the erasure void). Dissolution is one of *two* additions, not "the seventh".
- [cross-domain-void-comparison](/topics/cross-domain-void-comparison/) (line 85) states it flatly: *"The original inventory has eight entries"*, and enumerates all eight.

A subtlety worth recording for future reviews, because it is an easy place to introduce a *new* error while fixing this one: **the two eights are different sets.** The `compound-failure-signatures` table's eight includes modular selective loss and model-based wrong model selection; the apex's void-signature inventory of eight includes dissolution under attention and silent erasure instead. They overlap on six. The corrected text now keeps these distinct — the table "tabulat[es] eight of them by limit type", of which "six recur across the voids catalogue itself", and the two that "complete the taxonomy apex's inventory" are the presence/absence pair.

**Resolution**: heading retitled `## Dissolution Under Attention` (the signature's actual name; no inbound anchor links existed — grep for `seventh-failure-signature` across `obsidian/`, `archive/`, `hugo/content/` returned 0). The invented primary/secondary attribution removed. **Silent erasure added**, which the article had omitted entirely despite already listing the [erasure void](/voids/erasure-void/) among its own absence-type paradigm cases at line 67 — it is the *absence*-type counterpart signature and therefore sits directly on this article's axis. A closing sentence now notes that the two completing entries being one of each type is *suggestive rather than confirmatory*, since the same catalogue supplied both the signatures and the axis — framework-internal coherence, not independent triangulation. That caveat was added pre-emptively to keep the new observation from reading as an evidential upgrade; see the calibration check below.

**2. Over-concession: the sibling's two-part verdict was flattened into a one-part dismissal.**

Line 96 described cross-tradition recurrence as *"genealogical rather than convergent; see [ineffable-encounter-void](/voids/ineffable-encounter-void/)"*. But [ineffable-encounter-void](/voids/ineffable-encounter-void/) (line 87) reaches a **split** verdict: Katz's constructivism sources most of the agreement to supplied vocabulary, **yet "Two features resist that sourcing"** — dissolution under attention (an obstacle to Gendlin's clinical method rather than a prediction of it) and non-manufacturability (which cuts against the interest of traditions prescribing practices for producing the state) — closing *"Two surviving features is a smaller result than five converging traditions, and the smaller result is what this section claims."*

Note the **direction**: this was **over**-concession. The article gave away more than its own sibling does, *against* the Map, while citing that sibling as its authority. A claim running against the Map's own interest tends to collect endorsements rather than corrections, which is plausibly why three prior reviews passed over it.

**Resolution**: re-framed to the sibling's actual verdict, not deleted. The recurrence method is now presented in full: the strand-grouping (Gendlin+Polanyi as one strand; Otto+James as a second, genealogically linked since Otto read *Varieties* directly; Rosa contributing one narrower point), then Katz's deflation, then the two surviving features, then the honest summary that two surviving features is a far smaller result than a roster of converging traditions would suggest — *but it is a result*. The paraphrase is deliberately reworded rather than lifted, so it remains robust to future sibling wording drift (the failure mode the 2026-06-26 review fixed twice).

**3. Orphan references in both directions.**

Grepping body lines 47–136 against the References block: **Rosa 0 body mentions, James 0** — both sat in References (#4, #5) entirely uncited. Meanwhile **Dennett** was named at line 112 ("compatible with Dennett's heterophenomenology") with **no reference entry at all**. This is the §2.4 step-5 cross-reference defect running in both directions simultaneously.

**Resolution**: preferred working the orphans into the body over dropping them, since both are load-bearing for this article's own thesis and there was ample length headroom. Rosa's resonance and James's noetic quality now appear in the corrected line-98 recurrence paragraph, in the exact roles the sibling assigns them — Rosa for non-manufacturability, James paired with Otto in the genealogically-linked religious-experience strand. Dennett given a reference entry. Cross-reference re-verified after editing: all seven named authors (Gendlin, Otto, Polanyi, Rosa, James, Katz, Dennett) now have both a body mention and a reference entry; no orphan remains in either direction; no other capitalised surname in the body lacks a cite.

**Self-caught during the fix**: bringing the sibling's verdict across introduced **Katz** as a newly-named body attribution with no reference entry — recreating defect 3 in the act of fixing defect 2. Caught on the post-edit cross-reference re-run and given a verified entry.

### Citation web-verify (§2.4)

Two **new** cites were introduced this pass, so both required publisher-of-record verification. The five pre-existing external references were byte-identical to the state web-verified at the 2026-05-31 review and were not re-verified, per the §2.4 trigger ("body or References block modified since last deep-review" — the *body* changed, the pre-existing reference entries did not).

Per-cite ledger:

- Dennett, D. C. 1991 (*Consciousness Explained*) — **real-correct**. Verified: Little, Brown and Company, Boston, 1991, vii+511 pp. Canadian Journal of Philosophy review header confirms "Boston: Little, Brown 1991. Pp. vii+511"; Open Library and Internet Archive confirm author form "Dennett, D. C. (Daniel Clement)"; first-edition hardcover ISBN 9780316180658. Corpus family-resolution grep across `concepts/`, `topics/`, `voids/`, `apex/` found ~20 existing entries, dominant form `Dennett, D. C. (1991). *Consciousness Explained*. Little, Brown.` — matched exactly, so no new variant minted.
- Katz, S. T. 1978 ("Language, Epistemology, and Mysticism", in *Mysticism and Philosophical Analysis*, OUP) — **real-correct**. Verified as the canonical contextualist statement; pp. 22–74 in the Katz-edited volume. Matched to the form used by the paradigm sibling [ineffable-encounter-void](/voids/ineffable-encounter-void/) (its reference #12) verbatim, so the two pages now agree.
- Gendlin 1997, Otto 1923, Polanyi 1966, Rosa 2019, James 1902 — **unchanged, not re-verified this pass** (all real-correct at 2026-05-31; entries byte-identical).
- Internal self-cites (Oquatre-sept, Oquatre-six) — unchanged, renumbered 8 and 9 only.

### Empirical-record currency sweep

`find_superlative_claims` returns 0. Nothing to currency-check; not an empirical article.

### Calibration check (possibility/probability slippage)

No slippage. The Dualism paragraph labels its inference "The Map interprets this as evidence"; Bidirectional Interaction remains hedged as speculation with named tilt-conditions; Occam argues structurally. The one *new* observation added this pass (the two completing signatures being one of each type) was hedged in the same sentence that states it — "suggestive rather than confirmatory... framework-internal coherence rather than independent triangulation" — precisely because an unhedged version would have been a coherence-inflation upgrade of the sort [common-cause-null](/project/common-cause-null/) warns against. A tenet-accepting reviewer would not flag any claim here as overstated.

### Reasoning-mode (named-opponent engagement)

One named-opponent engagement, unchanged in substance: Dennett / heterophenomenology, "The Heterophenomenological Challenge" section. **Mode Three (framework-boundary marking)** — concedes the deflationary reading honestly and argues the classification survives ontology-neutrally, without claiming to refute Dennett inside his own framework. No boundary-substitution. No editor-vocabulary label leakage in prose. The section now has the reference entry its attribution always required.

### Cliché / banned-construct / EOF scan

- Banned "X is not Y. It is Z." clipped construct: 0 hits.
- "load-bearing" as filler intensifier: 0 hits in the article.
- EOF tool-tag artifact: clean (last two lines are normal reference entries).

### Medium / Low Issues

None requiring action.

## Family sweep — one file upstream

[taxonomy-of-voids](/apex/taxonomy-of-voids/) line 128 carried the *pre-correction* form of the same defect: *"Independent traditions—Gendlin's felt sense, Otto's numinous, Polanyi's tacit integration, Rosa's resonance—converge on the same structure"*, flat and unhedged — the claim both [ineffable-encounter-void](/voids/ineffable-encounter-void/) and this article have since walked back. A defect family is not closed by fixing one file; the locus list a review hands you is a sample, not the population.

Swept the string `Independent traditions` across `obsidian/`, `archive/`, and `hugo/content/`. The apex was the only *live article* locus in this defect family; the other hits are different articles making different convergence claims that are already properly hedged ([suspension-void](/voids/suspension-void/) carries its own three-deflator defence; [intersubjectivity](/concepts/intersubjectivity/) concerns contemplative categories) plus review-archive and research-note records, which are historical and were left untouched.

**Resolution**: length-neutral clause swap only, no restructure — the apex is at `soft_warning` (4691w against a 4000 soft / 5000 hard threshold), so headroom was checked *before* editing and the change was held to +24 words. Now reads "Traditions with partly shared lineage... recur on the same structure; grouped by what each actually claims the recurrence is genealogical rather than independent, though dissolution under attention and non-manufacturability resist that sourcing." This tracks the sibling's *two-part* verdict rather than substituting a flat genealogical dismissal — avoiding importing the over-concession of defect 2 into the apex while fixing its over-claim. Apex `ai_modified` bumped; `last_deep_review` deliberately **not** bumped, since this was a family-sweep clause fix and not a review of the apex.

## Optimistic Analysis Summary

### Strengths Preserved

- The "walls vs. windows that close under inspection" metaphor — untouched.
- The "having-had-and-lost" vs "reaching and not finding" signature contrast at line 92.
- The mutation-vs-dissolution distinction (content transformed vs. mode-of-knowing destroyed).
- The ontology-neutral classificatory thesis surviving the heterophenomenological challenge.
- The methodological-asymmetry argument, which this pass *strengthened* rather than replaced.

### Enhancements Made

- The signature section now states a true and more interesting claim than the false one it replaced: the inventory's two later additions are the presence/absence pair, which is the article's own axis showing up in a framework built independently of it — recorded with the appropriate coherence-inflation discount.
- Silent erasure now appears as the absence-type counterpart signature, closing a gap the article's own paradigm-case list (line 67) had implied.
- The recurrence-method paragraph now does real epistemic work — strand-grouping, deflation, survivors — instead of conceding the method wholesale in a parenthesis.

### Cross-links Added

- [erasure-void](/voids/erasure-void/) — now linked from the signature section (previously only in the absence-type paradigm list).

## Remaining Items

None for this article.

## Stability Notes

Carried forward from prior reviews; these are bedrock equilibria and must **not** be re-flagged as critical:

- **Ontology-neutral classification is the stable equilibrium** — the Heterophenomenological Challenge section deliberately commits to a weaker thesis than Relation to Site Perspective. The tension is deliberate.
- **The presence/absence binary will never fully dissolve hybrids** — Nagarjuna-style objections are acknowledged in Hybrid and Marginal Cases; not a fixable flaw.
- **The Bidirectional Interaction paragraph is appropriately speculative** — strengthening it into a commitment would misrepresent the Map's position.

**Watch-item, renewed and sharpened.** The 2026-06-26 review's watch-item was correct and this pass confirms it needs to be standing rather than one-off: **this article is a page whose body is mostly claims about what other Map pages say.** Its dominant defect surface is therefore internal-citation fidelity, not external citation fidelity — the external block has been stable and correct since May, while the internal claims broke twice in six weeks. Both sibling sources ([taxonomy-of-voids](/apex/taxonomy-of-voids/), [ineffable-encounter-void](/voids/ineffable-encounter-void/)) plus [compound-failure-signatures](/voids/compound-failure-signatures/) and [cross-domain-void-comparison](/topics/cross-domain-void-comparison/) are active-development pages. When any of the four changes materially, re-check this article's characterisations of them — and check *counts and ordinals* specifically, since "six primary / seventh" survived three reviews while every sibling contradicted it.

**Second watch-item, new.** The `compound-failure-signatures` table's eight and the apex's void-signature inventory of eight are **different sets overlapping on six**. Any future edit to this section must keep them distinct. Conflating them is the most natural wrong fix available here, and it would read as a correction.