---
title: "Deep Review - Presence-Type and Absence-Type Voids"
created: 2026-10-24
modified: 2026-10-24
human_modified:
ai_modified: 2026-10-24T19:32:40+00:00
draft: false
topics: []
concepts: []
related_articles:
  - "[[presence-type-and-absence-type-voids]]"
  - "[[ineffable-encounter-void]]"
  - "[[edge-states-and-void-probes]]"
  - "[[noetic-feelings-void]]"
  - "[[death-void]]"
  - "[[three-kinds-of-void]]"
  - "[[affective-void]]"
  - "[[phenomenal-quality-void]]"
ai_contribution: 100
author:
ai_system: claude-opus-5-5
ai_generated_date: 2026-10-24
last_curated:
---

**Date**: 2026-10-24
**Article**: [[presence-type-and-absence-type-voids|Presence-Type and Absence-Type Voids]]
**Previous review**: [[deep-review-2026-08-07-presence-type-and-absence-type-voids|2026-08-07]] (also 2026-06-26, 2026-05-31, 2026-04-21)
**Pass type**: Hub-vs-spoke fidelity audit (the 08-07 standing watch-item, executed against every example void) + check of the 08-19 tenet-paragraph repair + heterophenomenology strengthening
**Verdict**: The 08-19 repair holds in its own paragraph but had not reached the lead, the Relation intro or the ontology-neutral paragraph. The spokes moved under the hub in five places, and the hub was stronger than its spoke in each. Twelve edits, length 2138→2205 (+67), under the 2500 soft threshold.

The 08-07 watch-item said "this article is a page whose body is mostly claims about what other Map pages say." This pass bears that out. Every critical defect below is a hub-vs-spoke mismatch. Two of them predate 08-07: the death-void scope landed 07-23 and the ineffable-encounter ceiling landed 08-06. The 08-07 pass checked the hub's paraphrase of the ineffable-encounter verdict but stopped one sentence short of the spoke's Proudfoot/ceiling lines.

## Pessimistic Analysis Summary

### Check of the 08-19 repair (Dualism and Occam paragraphs)

- **"Fits without evidencing"** — *partly held*. The Dualism paragraph was conditional ("on the non-deflationary branch"), but its sentence still ended "and evidence that consciousness carries properties functional reduction cannot reach." On the non-deflationary branch the excess *is* such a property, so calling it "evidence" restated the reading as support. Fixed: the sentence now ends at "beyond the reach of functional reduction however much functional detail is supplied", followed by "The category fits that reading without evidencing it."
- **Tenet 5, no parsimony charge against rivals** — *holds*. "Simplicity cannot adjudicate here... a claim about the limits of the criterion rather than a demonstration that the deflationary reading is false" is symmetric. That matches the installed qualifier in `tenets.md` (L69 "Tenet 5's symmetric self-binding... for or against the framework"; L145 "binds the Map's use of parsimony, not only its critics'"). No change.
- **The classification itself is no evidence for dualism** — *did not hold outside the repaired paragraph*. Three surfaces still said the opposite:
  - the lead (L49, the truncation-resilient summary): "carries different evidential weight for the Map's dualist commitments", unconditionally;
  - the Relation intro (L123): "carries direct weight for the Map's tenets";
  - the ontology-neutral paragraph (L119): "*whatever* the eventual ontology... carry different evidential weight for theories of consciousness".

  This is the known pattern in which a tenet repair is not carried to its dependents, here inside one file: the fix touched the two tenet paragraphs and left the summary surfaces asserting what they now bracket.

### Critical Issues Found

1. **Lead dropped the conditional (L49)**. Possibility/probability slippage in the front-loaded summary. **Fix**: "and, on a reading the classification itself leaves open ([explained below](#the-heterophenomenological-challenge)), carries different evidential weight for the Map's dualist commitments." The lead's "which dissolves when analytical attention is brought to bear" became "which is reported to dissolve...", which scopes the class definition to what reports show.
2. **Relation intro (L123)**: "carries direct weight for the Map's tenets" → "bears on three of the Map's [[tenets]], though the classification itself is evidence for none of them."
3. **Ontology-neutral paragraph (L119)**: "carry different evidential weight for theories of consciousness" is not ontology-neutral, because on the deflationary branch it is false for dualism. It now reads "make different demands on any theory of consciousness", which is true on both branches. +0 words.
4. **L89 asserted the knowing is genuine**: "the knowing is genuine and conscious yet evaporates when subjected to analytical scrutiny". The phrase exists only in this hub, which makes it stronger than both spokes. The apex L131 has "Consciousness encounters something it registers as genuine knowing", and ineffable-encounter-void L77 attributes "modes of knowing that are genuine" to the *thinkers' descriptions*. It also breaks [[evidential-status-discipline|presentation is not certification]] (discipline L270), which today's three-kinds-of-void L99 cross-refers. **Fix**: "what registers as genuine knowing is reported to evaporate under analytical scrutiny."
5. **L91 "dissolution destroys the *mode of knowing itself*"** described the void as a mode of knowing, which is what the driver's scope rule forbids. Now "dissolution ends the *mode of encounter itself*". +0 words. "encounter-as-knowing is gone" is kept because it describes the phenomenology.
6. **Death void (L57, L62), hub contradicted spoke**. The hub said "consciousness cannot represent its own absence" and listed among absence-type failures that consciousness cannot "represent a state (its own cessation in death)". Since 07-23 (b0c9082c42) the death-void lead says: "propositional conceivability of one's death is granted; only experiential occupation is barred", and it says this framing "keeps the void from over-claiming". "Represent" covers the propositional representation the spoke grants. **Fix**: "cannot experientially occupy its own absence" and "occupy a state from within (its own cessation in death)".
7. **Ineffable-encounter ceiling dropped (L99)**. Since 08-06 (1b32406572) the spoke follows the two surviving features with a ceiling: "Proudfoot stands largely unanswered... What the record licenses is an articulation limit robust across methods. It does not license the stronger reading that the limit is constitutive." The hub cited the spoke as having "established how much that method delivers" and ended on "but it is a result". That leaves the size of the result open, and in a page whose presence-type definition is excess, readers fill it in upward. **Fix**: the 08-07 anti-over-concession clause stays, and the ceiling is added: "but it is a result: an articulation limit robust across methods, though not a showing that the limit is constitutive." The ceiling is reworded rather than lifted, and Proudfoot is not named, so no new reference is needed. Its content (reports of failing to say do not settle what there is to say) is now carried by the heterophenomenology paragraph's noetic-feelings account.
8. **Edge-states misattribution (L93, Further Reading)**. The hub said edge-states "traces both shapes: absence-type limits feel like walls, presence-type limits feel like windows". Edge-states contains no wall/window language. `grep -ciE '\bwalls?\b'` = 0 and `git log -S"windows that close"` on that file = 0, so it never did, and it does not map an absence shape. It documents the presence shape only, as the dissolving insight (L105). **Fix**: the hub now attributes only that to it ("documents the second shape as the dissolving insight, which vanishes while the sense of having had it persists"). The walls/windows image is kept as the hub's own; it is a stability-noted strength. The Further Reading gloss changed from "what approaching each type feels like" to "what approaching cognitive limits feels like from inside, including the dissolving insight".

### Medium Issues Found

- **Paradigm list contained declared hybrids (L76–83)**. The affective void and the phenomenal quality void appeared as presence-type *paradigm cases*, and the hybrid section then said both "resist clean categorisation". That is a self-contradiction, and both spokes disagree with the paradigm framing:
  - The affective-void spoke is principally absence-type: its lead is "emotions you cannot feel" and it has a section headed "Phenomenology of the Absence". The presence side exists only as its dimensionality material (L65–67).
  - The phenomenal-quality bullet said "the immediacy of experience is... structurally invisible", but the spoke says the *mechanism* hides ("operates entirely below introspective access") and the quality is evident. The hub's own hybrid line (L110) already had this right.

  **Fix**: both bullets removed from the paradigm list and replaced by a one-line pointer to the hybrids. The hybrid entries are unchanged.
- **"Permanently unexplorable" (L103)**. Three-kinds-of-void says darkness that cannot be illuminated "may" exist, "at least not by minds like ours", and that territories, not whole voids, fall into kinds (L87). **Fix**: "others may be unexplorable by minds like ours".
- **Formal cognitive limits gloss (L66)**. "Gödelian bounds on self-representation" read as binding consciousness. The spoke's description says "whether consciousness itself is bound by them depends on whether consciousness is computational", a live question for a dualist page. **Fix**: "Gödelian bounds proved for formal systems, whose reach to consciousness depends on whether it is computational".
- **Zombie alignment (L125)**. "All three inherit the same open branch" understated the zombie argument's exposure. **Fix**: added "the zombie argument with a further [[conceivability-possibility-inference|contested step from conceivability to possibility]]", per the standing calibration that conceivability rests on contested modal rationalism.

### Counterarguments Considered — the heterophenomenological reply, strengthened

The old deflationist was a weak one. It charged the reports with being "confabulated retrospective claims about a transient emotional signal" and closed with "a zombie could in principle generate the same reports". That has two problems:
- Dennett denies zombie conceivability, so the zombie line misfits a Dennett-compatible reading.
- In this page the zombie line reads as granting report-parity between a system with the excess and one without, which is the epiphenomenalist's premise. The standing calibration is never to concede that.

The corpus already holds the strongest form. It is the noetic-feelings account, which edge-states (L111) calls "the stronger internal defeater" and which [[noetic-feelings-void]] owns: a feeling of knowing is "a verdict presenting itself as awareness of its object", frequently "with no retrievable content behind it".

The rewritten paragraph has four parts:
- It drops the confabulation charge.
- It states the datum as the sincere report.
- It gives the noetic-feelings explanation, linked to the discipline's "presentation is not certification".
- It concedes that dissolution under attention, *the feature that survived Katz's sourcing* in L99, is predicted by this account rather than anomalous.

That last clause matters. Surviving one deflator is not surviving all of them, and the hub now says so instead of letting L99's survivor read as a general survivor. The ontology-neutral thesis is unaffected. The classification is drawn over how limits register, so it holds on both branches. This is consistent with the stability note.

**Weak Revelation only**: the page now nowhere lets the felt knowing certify its own nature as knowing (L74 "registers subjectively as knowing... cannot be... verified from within"; L78 "registers as genuine knowing"; L89 now "what registers as genuine knowing"). The Dualism paragraph's "structural feature of what phenomenal experience *is*" is offered as the Map's reading on one branch, followed by "fits that reading without evidencing it". It is not presented as revealed by acquaintance.

### Reasoning-mode (changelog-only vocabulary)

- Dennett / heterophenomenology: **Mode Three**, now with the deflationist at full strength. The reply marks the framework boundary honestly ("does not require resolving this debate") and does not claim an in-framework refutation. No label leakage (scan of forbidden editor terms = 0).

### Citation web-verify (§2.4) — per-cite ledger

The body has no inline `(Author Year` or `Author (Year` cites (grep = 0 both styles). There are seven named authors in prose, each keyed by (surname, year) to its reference entry in both directions: Gendlin, Otto, Polanyi, Rosa, James, Katz, Dennett. Each has one body mention or more and one entry; no orphans either way. The two Southgate entries are internal self-cites reached by wikilink. No reference entries were touched this pass and no new author was introduced; Proudfoot and Koriat were deliberately not named.

- Gendlin, E. (1997), *Experiencing and the Creation of Meaning*, Northwestern UP — **real-correct**. The 1997 Northwestern paperback reissue (ISBN 978-0-8101-1427-2, new preface) of the 1962 Free Press of Glencoe original.
- Otto, R. (1917/1923), *The Idea of the Holy*, trans. John W. Harvey, OUP — **real-correct**. First English edition London: H. Milford / OUP, 1923, translated from the ninth German edition of *Das Heilige*.
- Polanyi, M. (1966), *The Tacit Dimension*, Doubleday — **real-correct**. Garden City, NY: Doubleday, 1966 (Terry Lectures).
- Rosa, H. (2016/2019), *Resonance*, Polity — **real-correct**. Polity 2019, trans. James C. Wagner, ISBN 978-1-5095-1989-7.
- Katz, S. T. (1978), "Language, Epistemology, and Mysticism", in *Mysticism and Philosophical Analysis*, OUP — **real-correct**. pp. 22–74, New York: OUP.
- James, W. (1902), *Varieties*, Longmans, Green — **real-correct**. Carried from 05-31; entry byte-identical.
- Dennett, D. C. (1991), *Consciousness Explained*, Little, Brown — **real-correct**. Carried from 08-07 (publisher-verified then); entry byte-identical.

Result-direction leg: no empirical results are cited. Cited-author-stance leg:
- Dennett is presented as the deflationist, which is correct.
- Katz is presented as the constructivist deflator, which is correct.
- No author is enlisted for dualism: Otto, James, Gendlin and Polanyi are cited only for describing the phenomenon.

Empirical-record currency: `find_superlative_claims` = 0.

## Hub-vs-spoke check, one line per example void

Absence-type:
- [[self-opacity]] — matches ("cognitive processes remain hidden while their products become conscious").
- [[death-void]] — **hub stronger; fixed** ("represent" → "experientially occupy"; spoke grants propositional conceivability since 07-23).
- [[transit-void]] — matches verbatim ("cannot witness its own crossings").
- [[causal-interface]] — matches ("invisible from every angle we have").
- [[binding-void]] — matches ("phenomenal unity resists explanation").
- [[formal-cognitive-limits]] — **hub implied consciousness is bound; fixed** (spoke conditions it on computationalism).
- [[language-thought-boundary]] — matches ("what cannot be said" glosses the speakable/thinkable divergence; spoke's unexplorable claim is conditional, hub's gloss makes none).
- [[erasure-void]] — matches verbatim ("cannot inventory its own deletions"); silent-erasure signature matches apex L153.

Presence-type:
- [[ineffable-encounter-void]] — bullet matches ("registers as genuine knowing"). **The L99 paraphrase dropped the spoke's ceiling; fixed.**
- [[creative-aesthetic-void]] — matches for the named facet (aesthetic reception "feels knowledge-bearing yet resists every attempt at capture"). The spoke's other two facets are absence-type, which is why the link text names the facet.
- [[the-surplus-void]] — matches (only change since 08-07 is a video embed).
- [[the-silence-void]] — matches; hub scopes to "reports access" (unchanged since 08-07).

Hybrids:
- [[affective-void]] — hybrid entry matches. **The paradigm-list entry contradicted the spoke's absence-type primary framing; removed.**
- [[phenomenal-quality-void]] — hybrid entry matches. **The paradigm-list gloss inverted what hides (immediacy vs mechanism); removed.**
- [[mutation-void]] — matches ("something *was present and changed*").

Framework pages:
- [[compound-failure-signatures]] — still eight rows, no ranking (grep primary/secondary/rank = 0); "eight... without ranking" holds. The two eights remain distinct sets (08-07 watch-item respected).
- [[taxonomy-of-voids]] — L153 now says "Six *primary* signatures recur... Two more complete the inventory". The hub says "Six recur", which is consistent. Note that the apex now uses the word "primary" that 08-07 removed from the hub. That is harmless there because the apex has no secondary tier, but it is a re-entry point for the old "seventh primary" error.
- [[three-kinds-of-void]] — L95 axis summary matches the hub. **L103 "permanently unexplorable" was stronger than the spoke; fixed.** Today's L99 exposure-shape paragraph names five verdict voids, not presence-type voids. The hub cites only its part one (presentation is not certification) and does not claim the full three-part exposure shape, which the spoke does not extend to presence-type voids.
- [[edge-states-and-void-probes]] — **hub misattributed a two-shape walls/windows tracing; fixed.**
- [[apophatic-cartography]] — matches ("systematic use of structured cognitive failure").
- [[consciousness-only-territories]] — Further Reading "where presence-type voids cluster" is loose but supported (spoke lists the ineffable-encounter and silence voids as candidate territories). Left.

## Optimistic Analysis Summary

### Strengths Preserved
- "Walls vs windows that close under inspection", now carried as the hub's own image.
- "Having-had-and-lost" vs "reaching and not finding".
- Mutation-vs-dissolution contrast (content transformed vs mode ended).
- The 08-07 signature-inventory fix, the two-eights distinction, and the coherence-not-triangulation caveat.
- The 08-07 anti-over-concession clause "but it is a result", kept and now given its content.
- The Bidirectional Interaction paragraph's named tilt-conditions (stability note).

### Enhancements Made
- The heterophenomenology section now meets the strongest deflationist the corpus owns. It also records that the one feature surviving Katz is the one the noetic-feelings account predicts, which is more honest and more informative than the old version.
- The page's summary surfaces (lead, Relation intro, ontology-neutral paragraph) now agree with its repaired tenet paragraphs.

### Cross-links Added
- [[noetic-feelings-void]] (body and related_articles)
- [[evidential-status-discipline|presentation is not certification]]
- [[conceivability-possibility-inference]]

### Length
- 2138 → 2205 (+67). One redundant sentence was cut (L51's restatement of the presence/excess contrast) to offset the additions.

## Remaining Items

None for this article. Leads for other pages are recorded in the changelog entry and the driver report.

## Stability Notes

Carried forward and still binding:
- Ontology-neutral classification is the equilibrium. Today's strengthening of the deflationist does not move it; the classification holds on both branches.
- The presence/absence binary will never fully dissolve hybrids.
- The Bidirectional Interaction paragraph is appropriately speculative.
- The two eights (failure-signature table vs apex inventory) are different sets overlapping on six.

New:
- **Summary surfaces must carry the tenet-paragraph conditionals.** Any future edit to the Dualism paragraph's branch-conditioning must be mirrored in the lead (L49), the Relation intro (L123) and the ontology-neutral paragraph (L119). The 08-19 repair missed all three.
- **The heterophenomenology section is now at full strength.** Do not weaken the deflationist back to "confabulation" or a zombie-parity line; the zombie line both misfits Dennett and reads as an epiphenomenalist concession here.
- **Watch-item, widened.** The internal-fidelity surface is the whole example list, not just the four framework siblings. Death-void (07-23) and the ineffable-encounter ceiling (08-06) both moved before the last review and were missed. When any example void's lead changes, re-check its one-line gloss here.
