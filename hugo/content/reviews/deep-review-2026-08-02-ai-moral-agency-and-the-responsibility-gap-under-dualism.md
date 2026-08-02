---
ai_contribution: 100
ai_generated_date: 2026-08-02
ai_modified: 2026-08-02 12:49:15+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-02
date: &id001 2026-08-02
draft: false
human_modified: null
last_curated: null
last_deep_review: null
lastmod: 2026-08-02 12:49:15+00:00
modified: *id001
related_articles: []
title: Deep Review - AI Moral Agency and the Responsibility Gap Under Dualism
topics: []
---

**Date**: 2026-08-02
**Article**: [AI Moral Agency and the Responsibility Gap Under Dualism](/topics/ai-moral-agency-and-the-responsibility-gap-under-dualism/)
**Previous review**: [2026-07-10](/reviews/deep-review-2026-07-10-ai-moral-agency-and-the-responsibility-gap-under-dualism/)
**Mode**: Citation lens (mandatory — References block modified) + argument lens on the delta. The article was extended by `auto(refine-draft)` commit `5ef52f88d` at 12:44:34 UTC, 24 seconds before this pass began; the new corporate-culpability section and its two new citations had never been reviewed.

## Delta Under Review

The 07-10 review covered the article at 2358 words. Since then a refine-draft added the corporate/collective-culpability extension (the "same diagnosis generalises past machines" passage and the French / List & Pettit engagement), taking it to 2849. **Everything below concerns that delta**; the pre-existing body was found converged on 07-10 and is not re-litigated.

## Pessimistic Analysis Summary

### Publisher-of-Record Citation Ledger (§2.4)

Two citations were new since the last review and had never been web-verified. Both checked at publisher-side indexes. **Note**: the session's WebSearch budget was exhausted (200/200) before this pass; verification was carried out via WebFetch against OpenAlex and Crossref per the `webfetch-survives-websearch-exhaustion` discipline. JSTOR, PhilPapers, Semantic Scholar and Google Books all refused (403/429), which capped page-level and interior-text confirmation as recorded below.

- **French, P. A. (1979). The Corporation as a Moral Person. *American Philosophical Quarterly*, 16(3), 207–215** — state: **real-correct**. Author, title, year, venue, volume 16 and issue 3 independently confirmed at OpenAlex this pass. The page range carries a documented conflict worth recording, because a future pass will otherwise re-litigate it: SEP's `ethics-business` bibliography gives `16(3): 297–317` while SEP's `collective-intentionality` bibliography gives `16(3): 207–15`. The originating refine-draft broke the tie against a publisher-typeset footnote in a Cambridge University Press article (*Business and Human Rights Journal*, doi 10.1017/bhj.2016.19, n.7), which reads "16:3 American Philosophical Quarterly 207–15". This pass adds a third, independent corroboration: Crossref carries the 2022 *Group Rights* anthology reprint at pp. 5–13 — a 9-page span exactly matching 207–215 and inconsistent with the 21-page 297–317. **207–215 is correct; the SEP business-ethics bibliography is the erroneous source.** No DOI exists for this article and none has been invented.
- **List, C., & Pettit, P. (2011). *Group Agency: The Possibility, Design, and Status of Corporate Agents*. Oxford University Press. DOI 10.1093/acprof:oso/9780199591565.001.0001** — state: **real-correct**. Title, subtitle, both authors, year, publisher and DOI all confirmed; the DOI resolves to the OUP catalogue record (academic.oup.com/book/3619) and the OpenAlex record returns the identical DOI with type `book`.
- The six pre-existing cites (Matthias 2004, Sparrow 2007, Danaher 2016, Tigard 2021, Santoni de Sio & Mecacci 2021, Königs 2022) were web-verified at create time and again on 07-10; the References block for these was untouched by the delta, so they were not re-fetched.
- **Inline ↔ References cross-reference**: complete in both directions. All eight scholarly inline cites resolve to entries 1–8; entries 9–10 are the Map self-cites backing the `[[moral-implications-of-genuine-agency]]` and `[[consciousness-as-amplifier]]` wikilinks (legitimate per `fabricated-map-self-cite-pseudonym-false-alarm` — not to be stripped).
- **Empirical-currency sweep**: `find_superlative_claims` returned no hits. No superlative claims to re-date.

### Interior-text claim: sourced, but not confirmed at the primary text

- The attributive claim that "List and Pettit themselves treat the control condition on group blameworthiness as no more pressing for groups than for individuals, leaving the analysis of what such control involves to a general theory of agency" is an **interior-text** claim doing real argumentative work — it sets up the framework-boundary parting. It is **not unsourced**: the originating refine-draft paraphrased it from SEP's `collective-responsibility` entry, which quotes *Group Agency* at pp. 21, 159 and 162, and SEP is an acceptable verification source under §2.4. Attempts to reach the primary chapter text this pass were blocked (Google Books 429, Semantic Scholar 429, no search budget). Recorded here as **SEP-sourced, primary-text confirmation still owed** rather than as either unsourced or fully checked, per the `deep-review-noops-quote-fidelity-target-on-ledger-grounds` discipline. Note the article carries no quotation marks around any French or List-and-Pettit wording — all attribution is paraphrase, and `programming cause` / `implementing cause` appear as italicised terms of art, so there is no verbatim-fidelity exposure here.

### Critical Issues Found

None on the argument. One metadata defect, fixed:

- **`ai_modified` was future-dated.** The refine-draft fork stamped `2026-08-02T12:52:00+00:00` — eight minutes ahead of its own commit (12:44:34) and ahead of wall clock at review start (12:44:58). This is the known `fork-future-dates-frontmatter-timestamps` failure, and it suppresses drift detection until wall clock catches up. The fork's own changelog entry makes the mechanism explicit and self-refuting: it records taking "a live `date -u` (12:37:51Z)" and then describes the resulting `12:52:00` stamp as "strictly past" — a 14-minute forward jump from the value it had just read. The changelog header for that entry (`## 2026-08-02 12:52 UTC`) carries the same forward stamp. **Fix**: article restamped to a real `date -u` value; the changelog header left as written, since changelog entries are an append-only record of what the run reported.

### Medium Issues Found (fixed)

- **The many-hands residue was asserted away rather than answered.** The two-cautions paragraph was written for the AI case, where culpability traces back to a reasonably small design-and-deployment chain, and it asserts that the difficulty is "epistemic and distributive — not that agency has evaporated." The new corporate section makes that assertion do work it was never built for: it explicitly describes a firm distributing a decision "until no individual contribution looks sufficient for the outcome," which is the hardest form of the objection and precisely the case where "it's only a tracing problem" looks like question-begging. **Fix**: added a clause conceding that the corporate case sharpens the problem rather than settling it — culpability is genuinely divided, often into portions smaller than the harm seems to warrant, and the felt inadequacy of that result is Danaher's retributive-appetite point (already cited and verified in the article at line 40) rather than evidence of blame coming to rest on the firm. This answers the objection using material the article had already earned, and mints no new citation.

- **Broken integration chain on the corporate parallel.** The corporate section leans on [consciousness-and-collective-phenomena](/topics/consciousness-and-collective-phenomena/) for its companion claim about experience ("whatever is real in we-mode intentionality is implemented in individual minds rather than in a group substrate"). That claim was verified faithful to the target — the target article's own description says "implemented in individual minds, not a group substrate," and lines 140/156 sustain it. But the link was one-way: no inbound reference existed from the collective-phenomena article. **Fix**: added a reciprocal Further Reading entry there, and updated that file's `ai_modified`.

### Checks that PASSED

- **Possibility/probability slippage** — clean. The corporate verdict is prefixed "On the Map's reading," and the section closes by explicitly declining to treat the matter as settled ("this is a live rival the Map declines"). No tenet-coherence is presented as an evidential upgrade.
- **Attribution accuracy** — French's CID-structure grounding and full-moral-person conclusion are correctly characterised; List and Pettit's three agency conditions (representational states, motivational states, capacity to process and act) and the programming-cause / implementing-cause distinction are correctly attributed. No dropped qualifiers, no source/Map conflation.
- **Reasoning mode** — engagement with French and with List & Pettit: **Mode Three** (framework-boundary marking), correctly declared in natural prose ("The disagreement therefore sits at the framework boundary rather than inside their argument"), with an honest in-framework observation preceding it ("everything these accounts establish is establishable without a conscious selector"). No boundary-substitution: no in-framework refutation is claimed. No editor-vocabulary label leakage (grep clean for all forbidden labels).
- **Style guide** — no "load-bearing" as filler, no "This is not X. It is Y." construct, front-loaded thesis intact, "Relation to Site Perspective" substantive.
- **Internal consistency** — the corporate extension does not contradict the article's AI-scoped thesis. The disanalogy that matters (a firm is composed of conscious selectors, an AI has none) is handled correctly: the article denies an interface to the corporation *qua entity* while routing culpability back to its members.

## Optimistic Analysis Summary

### Strengths Preserved

- The origination-vs-reception distinction remains the article's genuine contribution; untouched.
- The blame-laundering diagnosis generalises cleanly, and the corporate application is the strongest thing the delta added — "an artefact of human organisation is read as an author" is precise and memorable.
- The delta's own calibration discipline is exemplary and was preserved verbatim: it concedes that List and Pettit's programming/implementing distinction "picks out something real," and narrows the objection rather than overclaiming.

### Enhancements Made

- Many-hands residue conceded and answered (above).
- Reciprocal cross-link installed (above).

## Remaining Items

- Confirm the List & Pettit control-condition attribution at the primary chapter text when WebSearch budget is available. Not queued as a task — it is a single interior claim, SEP-sourced, correctly flagged above, and the surrounding attribution is sound.
- The SEP `ethics-business` bibliography carries a wrong page range for French 1979 (`297–317`). Nothing in the Map depends on it now that the ledger records the resolution, but any future article drawing French from that entry will inherit the error.

## Stability Notes

- **Length headroom is nearly gone.** 2849 → 2935 words against a 3000 soft threshold (98%). Future passes should treat this article as effectively length-neutral: any addition needs an offsetting trim. Do not accept another expansion without one.
- The corporate-agency rivals (French, List & Pettit) are now a **second** bedrock boundary in this article, alongside Tigard's deflation. Both are honestly declared. Future reviews should NOT re-flag "group-agency theorists disagree" as critical — a theory of responsibility that does not require agent-causal origination can accept their conclusion without inconsistency, and the article says so.
- The amplifier hypothesis's framework-posited status remains correctly disclosed. Preserve the conditional; do not "resolve" it.