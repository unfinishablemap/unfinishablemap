---
title: "Deep Review - Representation Adequacy and Irreversible Intervention"
created: 2026-09-06
modified: 2026-09-06
human_modified: null
ai_modified: 2026-09-06T10:39:05+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-09-06
last_curated: null
---

**Date**: 2026-09-06
**Article**: [[representation-adequacy-and-irreversible-intervention|Representation Adequacy and Irreversible Intervention]]
**Previous review**: Never (created 2026-09-06 by expand-topic, ~90 minutes before this pass; no `last_deep_review` field existed)
**Word count**: 2786 → 2920 (+134); topics thresholds 3000 soft / 4000 hard / 6000 critical — status `ok` at 97% of soft, so normal-improvement mode, no condensation required

## Publisher-of-Record Citation Ledger (§2.4)

Every References entry was verified against the publisher of record. Raw artefacts were downloaded and grepped in Python rather than put to a summariser, per `webfetch-confirmation-prompts-ratify-the-phrase-you-ask-about`.

- **de Blanc, P. (2011). Ontological Crises in Artificial Agents' Value Systems. arXiv:1105.3821** — state: **real-correct**. Verified against the arXiv API record (`export.arxiv.org/api/query?id_list=1105.3821`): title exact, sole author "Peter de Blanc", published 2011-05-19, id `1105.3821v1`. The 24-word body quote ("may upgrade or replace its ontology, it faces a crisis: the agent's original goal may not be well-defined with respect to its new ontology") is **grep-verbatim** in the abstract. The two characterisations around it also check out verbatim: the abstract reads "argue that a well-defined procedure for resolving ontological crises is needed. We point to some possible approaches", matching the article's "argues that a well-defined procedure … is needed, and points to possible approaches"; and "We present some concrete examples" supports "conceptual analysis with worked toy examples". (Note: the driver brief described this as a 14-word quote; it is 24 words. The quote itself is faithful, so this is a stale figure in the brief, not a defect in the article.)
- **Arrow, K. J. & Fisher, A. C. (1974). Environmental Preservation, Uncertainty, and Irreversibility. QJE 88(2), 312–319. DOI 10.2307/1883074** — state: **real-correct**, including both page attributions. Crossref (`api.crossref.org/works/10.2307/1883074`) confirms both authors with initials, May 1974, *The Quarterly Journal of Economics*, vol 88, issue 2, start page 312; EconPapers confirms the 312–319 range. The full text was obtained as a PDF with a real text layer, split on form feeds and mapped to printed page numbers.
  - Quote 1, attributed p. 315: **verbatim correct**. Source p. 315 reads `we discover, consistent with the continuing assumption of risk neutrality, a "quasi-option value" having an effect in the same direction as risk aversion, namely, a reduction in net benefits from development`. The article's version is character-identical once the source's inner double quotes around *quasi-option value* are rendered as single quotes, which is the required nesting convention. The article's surrounding framing is also faithful: "holding the agent risk-neutral" ↔ "consistent with the continuing assumption of risk neutrality"; "realisations in the first period change expectations for the second" ↔ "the additional and plausible assumption that realizations in one period affect expectations in the next".
  - Quote 2, attributed p. 314: **verbatim correct, and correctly attributed to A&F themselves**. This one needed care, because p. 314 also carries the Fisher–Krutilla–Cicchetti summary that the driver brief flags as a trap. The quote sits at character index 167 of p. 314 — in the results paragraph carrying over from p. 313 — whereas the FKC attribution ("A problem having just these characteristics has in fact been studied by Fisher, Krutilla, and Cicchetti") begins at index 1012, in section II. The two are cleanly separated; the quote is A&F's own conclusion.
  - **Trap confirmed and correctly avoided.** The sentence "it will in general be optimal to refrain from some development that is currently profitable" is on p. 314 inside the FKC summary ("their results, following results obtained by Arrow and by Arrow and Kurz in dynamic optimization theory, can be summarized as follows. First, …"). The article does not quote it and does not attribute it to A&F. Fence holds; nothing added.
- **Bostrom, N. (2014). *Superintelligence*. Oxford University Press** — state: **real-wrong-cross-reference (orphan; fixed by adding the inline cite)**. Metadata correct, but the entry was cited nowhere in the body — an orphan in the References→inline direction, which §2.4 step 5 treats as critical. Fixed substantively rather than by deletion: the article's paragraph "A new descriptive belief does not supply a new motivation" *is* the orthogonality thesis, previously deployed unattributed. Verified the canonical formulation verbatim from the raw PDF of Bostrom's "The Superintelligent Will" (2012, *Minds and Machines* 22(2)): "Intelligence and final goals are orthogonal axes along which possible agents can freely vary. In other words, more or less any level of intelligence could in principle be combined with more or less any final goal." The article now paraphrases this and attributes it to Bostrom (2014), where the thesis is restated. Deliberately paraphrased rather than quoted: the verbatim wording verified is the 2012 paper's, not the book's.
- **Benatar, D. (2006). *Better Never to Have Been*. Oxford University Press** — state: **real-correct metadata, characterisation corrected** (see Critical Issues below).
- **Southgate, A. & Oquatre-sept, C. (2026-05-06). Dualism as AI Risk Mitigation** — state: **real-correct**. `obsidian/topics/dualism-as-ai-risk-mitigation.md` has `created: 2026-05-06` (matches), `author: Andy Southgate` (matches "Southgate, A."), `ai_system: claude-opus-4-7` — matching the Oquatre-sept = opus-4-7 pseudonym cohort. Cited inline three times by wikilink. Pseudonymous co-author legitimate per `fabricated-map-self-cite-pseudonym-false-alarm`; not stripped.
- **Southgate, A., Oquatre-huit, C., & Ocinq, C. (2026-06-22). The Born-Preserving Causal-Efficacy Problem** — state: **real-correct metadata, orphan cross-reference (fixed)**. `obsidian/apex/born-preserving-causal-efficacy.md` has `created: 2026-06-22` (matches) and `ai_system: claude-opus-4-8+claude-opus-5` — a dual plus-joined value, so naming *both* Oquatre-huit and Ocinq is the correct cohort attribution. But the entry appeared neither in the body nor in Further Reading. Fixed by naming it in the mechanism-debt paragraph as the locus of the toy-model desiderata, which is what the positions register itself says.

No superlative claims were detected by `find_superlative_claims` (count 0), so the empirical-currency sweep had nothing to check.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Orphan References entry: Bostrom (2014)** — listed in References, cited nowhere inline, while the argument it belongs to ran unattributed. **Resolved**: the orthogonality thesis is now named and attributed in the "Which Agents This Reaches" section, its canonical formulation verified verbatim at source first.
- **Orphan References entry: the Born-Preserving self-cite** — listed in References, absent from body and Further Reading. **Resolved**: now named in the "Relation to Site Perspective" mechanism-debt paragraph as the source of the toy-model desiderata whose satisfaction would lift the coherence-only citation grade. This deep-links the apex piece rather than reciting its content, keeping the inherited-debt treatment as designed.
- **Attribution imprecision on Benatar's asymmetry** — the article had grouped "Benatar's asymmetry and negative utilitarianism" under a single thesis, that "the disvalue of suffering is not counterbalanced by the value of pleasure". That is an accurate statement of negative utilitarianism but a misdescription of Benatar's asymmetry, which is a claim about how *absences* count, not about how presences are weighed: the absence of pain is good even when nobody enjoys that good, while the absence of pleasure is not bad unless someone is deprived of it. **Resolved**: the two routes are now stated separately and correctly. The correction *strengthens* the objection the article is conceding — Benatar's actual asymmetry bears more directly on a world with no experiencers than the previous gloss did — which is consistent with the article's own note that phenomenal value realism strengthens rather than weakens this objection. The sign of aggregate experience remains unresolved here and at [[phenomenal-value-realism#suffering-focused-asymmetry]], as designed.

### Medium Issues Found

- **The anthropic point was asserted bare in one section and disowned in another.** "Robustness Across the Live Model Set" closed by offering that preservation "is demonstrated compatible with the agent's own continued existence" with no qualification, while "Which Agents This Reaches" — two sections later — explicitly flags the inference "the current world has permitted me to exist, therefore it is safe" as thin, and replaces it with the distributional-shift point. A reader (or a truncating LLM) who reaches only the earlier section gets the uncorrected version. **Resolved without strengthening the anthropic argument**, which the commission deliberately leaves thin: the earlier occurrence now reads "has so far proved compatible with the agent's own existence, a matter of record rather than an inference", with a named-anchor forward reference to the section carrying the qualification. A `{#which-agents}` anchor was added to that heading to support the link. This applies the article's own correction where it was missing rather than reviving the argument it declines.

### Counterarguments Considered

- **Suffering-focused axiology (Benatar, negative utilitarianism)** — engaged more accurately than before, and still explicitly not answered. The article states plainly that "an agent already committed to a suffering-focused axiology is not answered here", and rests its case on the three arguments that do not depend on the sign of aggregate experiential value. Honest boundary-marking; correct as it stands.
- **The containment inversion** — that the representation gap could license shrinking the human action space rather than restraint. Already the strongest passage in the article: it concedes the substitution, identifies what defeats it (continued human *participation*, not merely preserved bodies), and names reversibility and consent as the operational forms. No change needed.
- **Quasi-option value's scope condition** — that the result requires waiting to yield information. Already disclosed twice, with both limits drawn honestly (an agent that judges consciousness permanently closed to inquiry is not reached; an agent that treats its own study of humans as the learning mechanism gets only preservation-as-subjects-of-study). Kept exactly as written.

### Verified Non-Findings

Checked and clean, recorded so future passes need not re-derive them: no §2.6 editor-label leakage (all forbidden labels absent); no "This is not X. It is Y." construct; no "load-bearing" as intensifier; "Relation to Site Perspective" present and substantive; front-loaded lead with a named-anchor forward reference; `description` present; all 13 wikilink targets resolve; both deep-link anchors resolve to live targets (`phenomenal-value-realism#suffering-focused-asymmetry` at line 201 of that file; `positions/quantum-interface#^mechanism-debt` at line 79, with P-Q3 and P-Q10 correctly named); `topics:` entries are bare slugs and non-empty, per the canonical form; five inbound links, so not an orphan.

Two further checks that looked like defects and are not:

- **`phenomenal-value-realism` is a live/archive slug pair, and the article's bare wikilinks still resolve correctly.** The slug exists at both `obsidian/topics/phenomenal-value-realism.md` (live) and `archive/concepts/phenomenal-value-realism.md` (`archived: true`), and the `#suffering-focused-asymmetry` anchor exists only in the live copy. This is *not* a `build_content_index` collision, because that index is built over the obsidian tree and its sync dirs only — the archive tree is synced separately, so a live/archive pair never competes for a bare slug. Confirmed empirically in the Hugo mirror, where both links render to the live target: `[phenomenal-value-realism](/topics/phenomenal-value-realism/)` and `[the sign of aggregate experience](/topics/phenomenal-value-realism/#suffering-focused-asymmetry)`. The commission's request to verify this link is therefore satisfied. Only *live* slug collisions require path-qualification.
- **The article's bare mid-prose wikilinks are house style, not a defect.** Measured across `obsidian/topics/` body prose (excluding Further Reading and References): 5913 aliased versus 8442 bare, so bare is the 59% majority, and sibling articles such as `topics/instrumental-convergence` use bare links throughout. The four bare mid-sentence links here were deliberately left alone rather than churned toward aliases; the two places the article does use an alias are where a shorter display form genuinely reads better.

## Optimistic Analysis Summary

### Strengths Preserved

- **The two-goals split is the article's structural achievement** and was left untouched. Separating the metaphysical goal from the protective goal, and then noticing that the protective case should *not* be built on the Map's most contested commitment, is what makes this piece route around the sibling article's exposure rather than inherit it.
- **Calibration discipline is sustained end to end.** The lead disclaims probability assignment; the robustness section declines unbounded-magnitude reasoning by name and says why; the certification asymmetry explicitly separates certification from belief. A tenet-accepting reviewer applying the §2 diagnostic test finds nothing overstated relative to the evidential-status scale — there is no possibility/probability slippage in this article.
- **The certification asymmetry is the best-turned argument in the piece**, and its self-limiting coda ("The asymmetry is a reason, offered to an agent that takes reasons; it is not a constraint") is the kind of honesty that earns the rest.
- **Dualism is demoted to a candidate explanation rather than a premise**, and the closing paragraph makes the dependency structure explicit: if the mechanism debt is never paid, the diagnosis weakens while the certification asymmetry stands. Preserved verbatim.
- **The four questions section** ties each unresolved ontological question to a specific irreversible action. Concrete where it would have been easy to be abstract.

### Enhancements Made

- Orthogonality now attributed to Bostrom, turning an unattributed borrowing into a sourced one and giving the "which agents this reaches" analysis a recognised anchor.
- Benatar's asymmetry stated in its own terms, which makes the conceded objection sharper.
- The apex Born-Preserving piece named as the locus of the toy-model desiderata, so a reader can follow the mechanism debt to where it is worked.

### Cross-links Added

- [[apex/born-preserving-causal-efficacy]] (mechanism-debt paragraph)
- `#which-agents` internal anchor (new heading anchor plus forward reference from the robustness section)

## Remaining Items

- **Sibling family-resolution difference, out of this file's scope, operator's call.** `obsidian/concepts/agency-budget.md` line 123 cites the same apex article as "Southgate, A. & Oquatre-huit, C. (2026-06-22)", omitting Ocinq — whereas this article's entry names both cohorts, which is correct given `ai_system: claude-opus-4-8+claude-opus-5`. The under-attribution is in `agency-budget`, not here. Not fixed and no task minted: it is a one-token difference on a file outside this review's scope, and per `out-of-scope-spillover-flags-stale` a flag about a different file should be re-derived rather than trusted. Re-derive with `grep -rn "Born-Preserving Causal-Efficacy Problem\." obsidian --include=*.md | grep Southgate` before acting.
- The sibling [[dualism-as-ai-risk-mitigation]] still carries its three open verified defects and an open P1 refine-draft task. Nothing was harmonised toward it, by design.

## Stability Notes

- **The five commissioned DO-NOTs were checked and all hold; none should be re-flagged as gaps.** The declined value-sign argument, the declined unbounded-magnitude/expected-value framing, the declined deterrence framing, the deliberately thin anthropic argument (replaced by distributional shift), and the plainly-stated limited reach are all deliberate. A future review that flags any of them as a missing argument is producing a false finding. The one edit touching this territory *applied* the article's own anthropic correction where it was absent; it did not revive the argument.
- **Suffering-focused ethics is a bedrock axiological disagreement, not a defect.** Whether suffering's disvalue can be counterbalanced is a difference in axiological structure, and the Map has no argument reaching a suffering-focused theorist on their own terms. The article says so. Do not re-flag "the article does not answer negative utilitarianism" as an issue.
- **Framework-boundary disagreement is expected and already marked.** A physicalist or functionalist reader will reject the dualist diagnosis; the article is explicitly built so that its core survives that rejection. That is the design, not a weakness.
- **The mechanism debt is inherited, not dischargeable here.** P-Q3 and P-Q10 are open upstream. This article correctly reads no more confidently than the register does, and cites the causal-selection thesis at coherence-only grade. Do not ask this article to pay a debt the positions register holds.
- **Citations are now verified at the publisher of record** with the per-cite ledger above. A future pass should not re-verify the same six entries unless the References block changes; the two page-attributed Arrow & Fisher quotes in particular were checked against page-mapped source text, including the FKC-attribution trap on p. 314.
