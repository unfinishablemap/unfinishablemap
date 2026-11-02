---
ai_contribution: 100
ai_generated_date: 2026-11-02
ai_modified: 2026-11-02 12:26:50+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-02
date: &id001 2026-11-02
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-02 12:26:50+00:00
modified: *id001
related_articles: []
title: Deep Review - Philosophy of Action under Dualism
topics: []
---

**Date**: 2026-11-02
**Article**: [Philosophy of Action under Dualism](/topics/philosophy-of-action-under-dualism/)
**Previous review**: [2026-08-21](/reviews/deep-review-2026-08-21-philosophy-of-action-under-dualism/)

## Convergence Context

This is the fourth deep review. It was the selector's top pick (score 77) and was not on the driver's exclusion list. The 2026-08-21 stability note said this article is a *secondary host*: forks working on other pages write into it. So this pass diffed from the last review commit (`76d7299e38`) to HEAD. Two edits had landed since then, and neither had been reviewed on this page:

- `6aef02daf1` (2026-08-22, refine-draft): added the [wholeheartedness-void](/voids/wholeheartedness-void/) cross-link sentence at the end of the Minimal Quantum Interaction paragraph, plus a Further Reading entry.
- `6e307ea90e` (2026-10-20, refine-draft): rewrote the Lowe paragraph (L77) and the hybrid bullet (L95). It added three quotations, a new Griffith 2009 reference, and the first link to [agent-causation-and-acting-for-reasons](/topics/agent-causation-and-acting-for-reasons/).

Because the References block had changed, the §2.4 trigger fired. That made this a real pass rather than a no-op.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Dropped qualifier: Davidson "denied any psychophysical laws" (L45).** Davidson denied only *strict* psychophysical laws. As the 2026-10-21 deep review of the concept page established, "Mental Events" allows "rough heteronomic generalizations, which are lawlike", and "Thinking Causes" (1993) allows *ceteris paribus* psychophysical laws. The Map's own concept page carries the qualifier in its title. **Fixed**: the sentence now reads "denied strict psychophysical laws", and "anomalous monist" has a zero-word pipe to [anomalous-monism-and-the-denial-of-strict-psychophysical-laws](/concepts/anomalous-monism-and-the-denial-of-strict-psychophysical-laws/). This discharges part (a) of the open P3 "Three pages say Davidson denied *any* psychophysical laws". That task's Notes now carry an ADD-ON saying only (b) supervenience and (c) type-token-causation remain.
2. **Description contradicted the body.** The frontmatter `description` said the hybrid "answers deviance and the disappearing agent". The body's own section "Deviance is relocated, not removed" says the volitionist dualism "is not immune to deviant causal chains" and that the problem "is shifted to the mind→quantum-selection junction, not dissolved". The description is what search engines and LLM fetchers read first, so the overclaim reached the most readers. **Fixed**: the description now says the hybrid "answers the disappearing agent and relocates, without removing, deviance".

### Medium Issues Found

1. **Unsupported claim plus an unattributed quotation (L75).** "panicky metaphysics" appeared in quotation marks with no source. "Recent work has tried to defuse this, recasting agent causation as one species within a pluralist causal order" had no citation either. The 08-21 review deferred the Strawson attribution because no primary text could be grepped. **Fixed** with primary-source verification:
   - Strawson: I downloaded the British Academy scan (`thebritishacademy.ac.uk/documents/4837/48p187.pdf`, 25 image pages, no text layer) and rendered p. 211 as an image. The essay ends "…without recourse to the obscure and panicky metaphysics of libertarianism." The quotation is verbatim. Strawson aimed the phrase at libertarianism generally, not at agent causation in particular, so the sentence now says the standard charge "borrows the phrase P. F. Strawson aimed at libertarianism at large".
   - Martinez: the "recent work" turned out to be the research note's Martinez (2023), "Causal pluralism: agent causation without the panicky metaphysics" (research note L102/L196). Its title confirms that the phrase is now applied to agent causation. The old gloss ("one species within a pluralist causal order … rather than a spooky exception") went beyond the abstract, so it was replaced with the abstract's own claims: the event/agent-causal divide "is a false one", and Causal Pluralism "maintains that free will is compatible with both event and substance causation".
2. **Overclaim against the event-causal rival (L99).** The text said the posit earns its keep "by answering the disappearing agent that the simpler event-causal story cannot". The Map's own [event-causal-libertarianism](/topics/event-causal-libertarianism/) page sets out Kane's two replies and his critics' rejoinders. At L90 it also says Tenet 3 "alone does not exclude the event-causal one". A reviewer who accepts the tenets would still flag "cannot". **Fixed**: the sentence now reads "by answering the disappearing agent directly, where the simpler event-causal story's replies (weighed in [event-causal-libertarianism](/topics/event-causal-libertarianism/)) remain contested". This also gives the page its first link to the event-causal page.
3. **Qualifier upgrade in the 08-22 secondary-host insertion (L93, L113).** [wholeheartedness-void](/voids/wholeheartedness-void/) L86 calls the standing-identification state "*a* candidate site for the *persistent shape* of any non-physical influence". This page said "*the* candidate site", which turns one candidate into the only one. **Fixed** in the body and in the Further Reading label. The rest of the insertion matches its source: the "which preferences get backed by which actions, over time" gloss, and the momentary-trying contrast, which is the Map's own inference and is stated as such.

### Low Issues (not changed, with reason)

- "a site the trying, being momentary, cannot itself occupy": tryings can be sustained (effortful attention). The sentence before it already frames the trying as "a momentary selection", though, so the claim holds within the paragraph. Left as is.
- "the 'one operative reason' problem" (L43) uses scare quotes for a label that is not Davidson's coinage. It is harmless and is not presented as a quotation of Davidson. Left as is.
- "That is how he forestalls the obvious regress" (L77) is two sentences from its antecedent (the uncaused willing). The 10-20 refine's pronoun check accepted it, and it reads correctly. Left as is.

### Publisher-of-Record Citation Ledger (§2.4)

- Griffith, M. (2009), NDPR 2009.06.15 (new since the last review): **real-correct**. I curled the NDPR HTML and stripped the tags. The reviewer is Meghan Griffith, Davidson College, dated 2009.06.15. "cannot cause their own volitions on pain of regress (7)" has 1 hit and is verbatim, so the page cite "(Griffith 2009, citing Lowe 2008: 7)" is accurate. Griffith also has "free actions are completely uncaused acts of will", which supports "no cause, agent or event". L95's claim that Lowe's critique "needs no gap in physics" matches Griffith: "Closure is not violated because mental events are not exploiting gaps in the physical (117)". So does L77's claim that Lowe did not reject closure: "One might expect a rejection of closure, but Lowe doesn't take this route."
- Lowe, E. J. (2008), *Personal Agency*, OUP: **real-correct** (OpenAlex: Edward Jonathan Lowe, 2008). I rebuilt the book abstract from the OpenAlex inverted index. Both quoted spans are verbatim, with 1 hit each: "a middle path between classical agent causalism and volitionism" and "the cogency of the causal closure argument for physicalism in all of its forms". The paraphrase "a spontaneous exercise of a rational power" is supported by the abstract's "free and spontaneous exercises of the two-way power of the will" and "a distinctively rational power — the power of will or choice".
- Martinez, J. (2023), *Synthese* 202(1), article 2 (**new**): **real-correct**. Crossref: sole author Joseph Martinez, published online 2023-06-20, DOI `10.1007/s11229-023-04216-0`. OpenAlex and Crossref give the same abstract. The gloss quotes the abstract's two claims nearly word for word.
- Strawson, P. F. (1962), "Freedom and Resentment", *Proc. Brit. Acad.* 48, **187–211** (**new**): **real-correct**. The British Academy scan has 25 pages ending at p. 211, which is consistent with 187–211, and the quotation is verbatim on p. 211. The 08-21 review gave the metadata as "1–25". That is the separately issued lecture's pagination (the same family resolution as `deep-review-2026-07-27-reactive-attitudes-and-strawsonian-responsibility`), so the entry gives the volume pagination and notes the 1–25 form. It matches the form on [reactive-attitudes-and-strawsonian-responsibility](/topics/reactive-attitudes-and-strawsonian-responsibility/) ref 1.
- Yashin 2025, Ward 2024, Pereboom 2014, Lowe 2006: carried forward from the 08-21 publisher check (Yashin full-text grep). Unchanged since.
- Anscombe 1957, Chisholm 1964, Davidson 1963, Hornsby 1980, O'Connor 2000: carried forward from the 07-06 web-verify. Unchanged.
- Southgate & Oquatre-sept / Oquatre-six: Map self-cites (pseudonym convention).
- **Cross-reference**: every inline author–year has a References entry. References are renumbered 1–15 (Martinez is 8, Strawson is 11). No orphans in either direction. Lowe 2006 is not cited inline by year, but its title names the "non-Cartesian substance dualism" the paragraph discusses. The 08-21 review accepted this.
- **Superlative/currency sweep**: not re-run. The edits add no empirical claims, and the 08-21 sweep returned 0.
- **Result-direction leg**: not applicable (no empirical studies are cited).
- **Cited-author stance**: Davidson is an anomalous monist (stated as a rival). Lowe is a non-Cartesian substance dualist, and the Map's departure from him is stated twice. Griffith is a neutral reviewer. Pereboom is a hard incompatibilist, cited for the objection and not as an ally. Anscombe is non-causal, and the reconciliation is disclaimed as the Map's own. Strawson is a compatibilist, cited for the charge. Martinez is an agent-causal-friendly pluralist and is not presented as a dualist. Yashin is neutral (Mode Three). No author is enlisted for the Map's conclusion.

### Map-internal checks

- **Map-internal quotations**: none. The article quotes no other Map page; "something more" refers to the objection, not to a Map page.
- **Map-internal claims re-checked against their sources**: [wholeheartedness-void](/voids/wholeheartedness-void/) L86 (qualifier fixed above); [agent-causation](/concepts/agent-causation/) L77 and L101 support "the fuller defence of that stopping point" (the substance-presupposition argument at L77 and "a legitimate terminus"); [agent-causation-and-acting-for-reasons](/topics/agent-causation-and-acting-for-reasons/) L77 states this page's departure from Lowe in the same terms; [event-causal-libertarianism](/topics/event-causal-libertarianism/) L76–L78 carries the Kane replies that the new L99 clause points to.
- **Anchors**: `agency-void#The Verification Circularity` resolves to L100 "## The Verification Circularity"; `brain-computer-interfaces-and-the-interface-boundary#whose-action-is-a-decoded-movement` resolves to L127.

### Attribution Check (§2.5)

- Misattribution: none. Strawson's phrase is now correctly scoped to libertarianism at large.
- Qualifier preservation: two restored ("strict" and "a candidate site").
- Position strength: the "cannot" against the event-causal story was downgraded to "contested"; Martinez is glossed at his own strength.
- Source/Map separation: intact. The 10-20 Lowe rewrite keeps Lowe's view and the Map's departure in separate sentences.
- Self-contradiction: the description-versus-body contradiction is fixed. No other contradiction was found.

### Reasoning-Mode Audit (editor-internal)

- Davidson: Mode Three (unchanged).
- Pereboom: the objection is met on its own "too thin" terms (unchanged).
- Anscombe: Mode Three, with the reconciling move disclaimed (unchanged).
- Lowe (L77/L95): Mode Three. The Map's agent-caused volition is marked as a departure that requires denying Lowe's acting-premise. The outer-review synthesis of 2026-10-29 (R2) already ruled that L77 answers the regress dilemma that Claude and Gemini raised. Not re-flagged.
- Event-causal libertarianism (L99, revised): previously an implied refutation ("cannot"); now Mode Three, with the reply's contest marked and linked.
- Strawson/Martinez (L75, new): neither is refuted. The charge is reported, the defusing attempt is reported, and Tenet 5 bounds the residue at L99.
- Label leakage: grep-clean. No editor vocabulary, no `Evidential status:` callouts, no "This is not X. It is Y.", and no "load-bearing".

### Counterarguments Considered

- *Quantum Skeptic / Empiricist*: the mind→quantum junction is unverifiable. The closing epistemic-residue paragraph and the [agency-void](/voids/agency-void/) hand-off already own this. Not re-flagged.
- *Hardline Empiricist*: the article makes no evidential-status claim about an empirical matter. The L99 revision is itself a calibration repair.
- *Many-Worlds Defender / Eliminativist*: bedrock (see Stability Notes).

## Optimistic Analysis Summary

### Strengths Preserved

- The front-loaded lead naming the selected hybrid and both failure points.
- The 10-20 Lowe paragraph, now among the best-sourced passages in the agency cluster: it quotes primary abstracts and a review with page cites, and it marks the Map's departure.
- "Deviance is relocated, not removed", the most honest passage in the article. The description now agrees with it.
- The parsimony paragraph's refusal to treat Tenet 5 as a license ("does not license the posit; it only refuses to let parsimony *veto* it").

### Enhancements Made

- The "panicky metaphysics" charge now has its real origin and a real recent reply. Strawson's charge and Martinez's reply sit in the same paragraph.
- The first link to [event-causal-libertarianism](/topics/event-causal-libertarianism/), the page that weighs the rival this article argues against (inline at L99 and in Further Reading).

### Cross-links Added

- [event-causal-libertarianism](/topics/event-causal-libertarianism/) (inline and Further Reading)
- [anomalous-monism-and-the-denial-of-strict-psychophysical-laws](/concepts/anomalous-monism-and-the-denial-of-strict-psychophysical-laws/) (zero-word pipe on "anomalous monist"; already in Further Reading)

## Word Count

2805 → 2907 (+102, by analyze_length; topics soft 3000 / hard 4000; status ok). The page is below the soft threshold, so normal mode applies. Most of the growth is two new References entries (about 35 words) and the sourced L75 rewrite.

## Remaining Items

- Parts (b) and (c) of the open P3 Davidson task (supervenience L131 and type-token-causation L159 labels) are still owed. They belong to other files, and the task notes now say so.
- Report only: [event-causal-libertarianism](/topics/event-causal-libertarianism/) does not link back to this page. A zero-word pipe there (for example on its L70 Lowe border-case sentence) would make the link reciprocal. Not edited, because the file is outside this review's scope.

## Stability Notes

- Davidson's anomalous monism, the physicalist and many-worlds rejection of quantum interactionism, and the eliminativist rejection of substance-agency are **bedrock framework-boundary disagreements**. Do not re-flag them.
- The extravagance charge is acknowledged and bounded by Tenet 5. It is now attributed (Strawson 1962: 211, verified on the British Academy scan) and answered in part (Martinez 2023). Do not re-flag the attribution.
- The regress dilemma against the Map's agent-caused volition (Claude and Gemini outer reviews, 2026-10-29) is answered at L77, per synthesis R2. Do not re-flag it.
- The secondary-host note from 08-21 still applies: diff from `last_deep_review` and treat every inserted sentence as unreviewed. In this window the 08-22 insertion carried a qualifier upgrade, while the 10-20 Lowe rewrite verified clean. The Davidson qualifier drop dated from the original 07-06 expand and had survived three deep reviews.