---
ai_contribution: 100
ai_generated_date: 2026-10-24
ai_modified: 2026-10-24 21:39:38+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-10-24
date: &id001 2026-10-24
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-24 21:39:38+00:00
modified: *id001
related_articles: []
title: Deep Review - The Ownerless Suffering Argument
topics: []
---

**Date**: 2026-10-24
**Article**: [The Ownerless Suffering Argument](/concepts/the-ownerless-suffering-argument/)
**Previous review**: [2026-09-08](/reviews/deep-review-2026-09-08-the-ownerless-suffering-argument/) (deep); [2026-09-23](/reviews/pessimistic-2026-09-23-the-ownerless-suffering-argument/) (pessimistic), partly applied by refine `da6c8eae` the same day
**Word count**: 3266 → 3318 (+52; `soft_warning` throughout; concepts hard gate fires at >=3500)

## Scope of this pass

This pass had two jobs. The first was to check whether every item on the 2026-09-23 pessimistic review's lists was discharged, using `git log -S` on the quoted strings and an independent read of the current text. The second was the §2.4 publisher-of-record pass, which the 09-08 review deliberately skipped (it re-did quote fidelity only). The body and the References had changed since that review, so the pass was due.

Primary texts fetched raw and grep-verified by script (normalised quotes and whitespace, substring match): both SEP entries, the Garfield–Jenkins–Priest chapter preprint (`jaygarfield.org`), Finnigan's author-copy survey PDF, the *JBE* abstract page for Harris 2011. Metadata: Crossref for every DOI; OpenAlex abstracts for Finnigan 2015 and Chadha 2021; OUP's book page for Moonpaths; Open Library.

## Pessimistic-review discharge ledger (2026-09-23)

`git log -S` on each quoted string, plus a read of the current text. **LANDED** means the defect string is gone and the repair is present. **PARTIAL** means the named location was fixed but a sibling string carrying the same claim survived, or the fix was incomplete. This pass completed every PARTIAL item.

| # | Item | 09-23 status | This pass |
|---|------|--------------|-----------|
| I1 | Finding rests on an unargued wide reading of "anyone" | **PARTIAL**. Lede, §map-meets ¶2–3 and §implications were scoped. Three strings from creation survived: L77 "its conclusion depends on there being no owner at the grain" (unscoped); L59 "denies exactly the mattering-recipient" (asserted the wide reading of 101 as given, the very reading L123 lists as something that *would move* the article, and in tension with L79's "stays true on the Map's reading"); description "blocks it" | Fixed: L77 "read one way,"; L59 rewritten to name the mattering-recipient and pose the scope question; description now "falsifies its premise" |
| I2 | Relation credits Tenet 1 with the subject-pole | **LANDED** (the Dualism ¶ now says irreducibility, not existence; abhidharma satisfies Tenet 1 too). Sibling L120 matches | No change |
| I3 | §unranked counts conventional "welfare" talk as a concession | **LANDED** | No change |
| CA1 | A reworded premise ("no one who could be favoured") rebuilds the bridge | **PARTIAL**. The rewording was attached only to the narrow reading, and L121 still said the tradition's route "needs replacing rather than adopting", stronger than the concession the review asked for | Fixed: L79 "even there … rebuilds it with one qualifying clause"; L121 "carries impartial benevolence only once restricted to owners who could be favoured" |
| CA2 | The locus is itself a *prajñapti* (the Parity Reply cuts against the Map too) | **LANDED** (L99 sentence) | Carried into the Tenet 5 ¶ (L127) |
| CA3 | Chadha's eliminativism need not remove streams | **LANDED** | No change |
| U1 | "*needs* the sufferings to be ownerless at exactly that grain" | **PARTIAL** (lede fixed; L77 sibling survived) | Fixed with I1 |
| U2 | "Dualism supplies the momentary locus" | **LANDED** | — |
| U3 | Chadha "not available" | **LANDED** | — |
| U4 | Prajñākaramati read only through GJP | **LANDED** ("as Garfield, Jenkins and Priest report and reconstruct it"). Verified this pass: GJP introduce his 101 gloss as an instance of the reading on which 101 "contain[s] an implicit appeal to abhidharma metaphysics" | — |
| U5 | "settle … at once" | **LANDED** ("reopen") | — |
| L1 | "fails normatively" | **LANDED** | — |
| L2 | "in its own favour" ambiguity | **LANDED** | — |
| L3 | "as the tenet requires" | **LANDED** ("permits") | — |
| L4 | Citation-hygiene paragraph above the argument | **PARTIAL**. Condensed but still above the argument, and the condensation introduced "its two encyclopaedia entries", whose "its" referred back to the *Śāntideva* entry (an entry has no entries; Goodman does) | Completed: the numbering note moved to ref 1, the "must be"/"are to be" slip note moved to ref 14; L47 "and the numbering varies" dropped |
| L5 | Repeated not-obtained narration | **LANDED** (consolidated at L115) | — |
| L6 | "correction rather than a refutation" | **LANDED** | — |

Persona-level remarks (not on the lists): the Physicalist's point, that the finding depends on the Metzinger reading without saying so where the finding is stated, is **PARTIAL**. The conditional framing ("Grant the momentary locus") and L123 cover it, and the live residue was L59, now fixed. The Many-Worlds Defender's point that "the same isolation holds here" presents the isolation as free is **OPEN**, deliberately not installed (see Remaining Items). The Empiricist's asymmetry point about the Tenet 5 paragraph is now resolved by the rewrite below.

## Pessimistic Analysis Summary

### Critical Issues Found

- **L59 internal tension (the I1 residue)**. "The one *for whom* there is suffering does not exist" was said to deny "exactly the mattering-recipient that the second premise … asks for". The sibling's own exit is that the second premise's *subject* is not the third premise's *self*, so reading 101 as denying that subject is the strong reading the Map rejects and L123 treats as an open contingency. *Resolution*: the sentence now says only that the phrase *names* the recipient, and that whether 101 denies it or only the person is the scope question below. It then adds the one piece of textual evidence on that question the article had not used. Prajñākaramati, as GJP quote him, concludes "there is no one at all" (wide), and his reason is that there is "nothing whatsoever like a self that could be an owner" (narrow). Both fragments are grep-verified in the chapter. Placed in §argument, not §map-meets, because the §map-meets marker says no part of that section is attributed to sources.
- **Tenet 5 used against the reductionist (L127)**. "For the Map: the Parity Reply's second half shows what parsimony pressed consistently costs the reductionist." Tenet 5 binds the Map's own reasoning, and the tenets page names this "parsimony asymmetry" pattern. The Parity point is also about consistency, not parsimony. *Resolution*: the paragraph now says the tenet "binds the Map's own reasoning here and supplies no charge against its opponents". It reclassifies the Parity point as one "about consistency rather than economy", and applies it to the Map ("may reach the Map's subject-pole with it"). It keeps "Neither side may stop deflating where it suits them." The "in both directions, which is unusual" framing is gone.
- **Missing References entry: Williams 2000**. Cited inline at L109 ("his 2000 reply to Siderits's review") and L123 ("Williams 1998 or 2000") with no References entry. *Resolution*: added "Williams, P. (2000). Response to Mark Siderits' review. *Philosophy East and West*, 50(3), 424–453." Pages from PhilArchive and the research note, and SEP1 independently cites "Williams 2000" for the exchange. No DOI added: Crossref returned no record for it.

### Medium Issues Found

- **Finnigan 2015 framed beyond its abstract (L113)**. The article said the paper presses "on the 'conventionally real streams' route the sibling article credits to Siderits". Per its abstract, it argues against Tillemans that *Prāsaṅgika* Madhyamaka cannot satisfactorily justify moral judgments by appeal to conventional truth. That targets the Mādhyamika conventionalist exit (the Parity Reply's first half), not Siderits's reductionist streams. *Resolution*: reworded to the abstract's claim, aimed at the Parity Reply's first half.
- **"the argument's leading modern expositor" (L71)**. An unsupported singular; SEP2 itself credits "writers such as Mark Siderits" with the Parfit parallel. Now "a leading modern expositor".
- **Description "blocks it"**. On the wide reading the body says the step "loses its stated premise", and CA1 now says a qualified premise rebuilds the bridge, so "blocks" overstated. Now "falsifies its premise".
- **Translator not named for the second rendering (L53)**. GJP's verses are their own: "Translations are from the Sanskrit with reference to the sDe dge edition of the Tibetan" (chapter fn. 1). Now "Garfield, Jenkins and Priest's own translation from the Sanskrit".

### Counterarguments Considered

- *Nāgārjuna*: the "limitation" point (a moment with no future grounds no limitation) is now carried by CA1's concession in both L79 and L121.
- *Many-Worlds defender*: isolation not free. Recorded, not installed.
- *Eliminativist / physicalist*: bedrock, as in 09-08. The L121 subject-pole clause stays labelled "only on the Map's reading".
- *Quantum skeptic*: no purchase.

### Citation ledger (§2.4, publisher of record)

- Goodman 2016, SEP *Śāntideva*: **real-correct**. Pubinfo "First published Mon Sep 19, 2016" verified. Crosby–Skilton 101–102 with "must be warded off" verbatim. The Harris *upāya* report is verbatim, and so is the prose "IX" numbering. The entry cites the exchange as "Williams 1998, Siderits 2000, and Williams 2000".
- Goodman & Schultz 2024, SEP *Ethics in Indian Buddhism*: **real-correct**. Pubinfo verified. "are to be warded off … (Crosby and Skilton trans. 1995, 97)", "some scholars now call", "hard to see how", and both unranked-gloss sentences are verbatim. It also supports the Further Reading annotation "the secular parallel Goodman and Siderits both invoke": "As writers such as Mark Siderits (2003, ch. 9) have often noted, this strategy … closely resembles the arguments for consequentialism in Parfit 1984 (ch. 15)."
- Garfield, Jenkins & Priest: **real-wrong-metadata (year)**. Was 2016, corrected to 2015 (Crossref `published-print` 2015-12-01). The title, pp. 55–76 and author order are correct (stability note honoured). Every quotation is verbatim again this pass: verses 101/102, the dharmas/svalakṣaṇa block, "literally no people", footnote 4, the Parity Reply (whole), "prima facie fallacious … as Williams and others note". The new Prajñākaramati fragments are verbatim too.
- The Cowherds, *Moonpaths*: **real-wrong-metadata (year)**. Was 2016, corrected to 2015. OUP's book page gives published 17 Sep 2015 and available in print 1 Dec 2015; Crossref print is 2015-12-01; Open Library and catalogue records give 2015. SEP1 and the ANU portal cite 2016, and a short note on the reference records the split. The research note's "OUP's print year is 2016 … cite 2016" premise was unsupported, and a dated correction was appended there so a future sweep does not revert this.
- Siderits, Moonpaths chapter: **real-wrong-metadata (year)**. Was 2016, corrected to 2015. Title and pp. 119–140 verified.
- Goodman 2009: **real-correct**. Chapter 4 "Theravāda Ethics as Rule-Consequentialism" verified at Crossref (pp. 47–72).
- Goodman 2008, *PEW* 58(1): 17–35: **real-correct**.
- Williams 1998: **real-wrong-metadata (publisher)**. Was "New York: Routledge", corrected to "Richmond: Curzon", per the contemporaneous *BSOAS* (Franco 2000) and *JRAS* (Werner 2000) reviews at Crossref. Routledge is the later reissuer.
- Williams 2000: **added** (see Critical Issues).
- Harris 2011, *JBE* 18: 92–123: **real-correct**. The abstract confirms the Williams/Siderits/Pettit scope and the meditational-techniques reading.
- Finnigan 2015, *PEW* 65(3): 765–785: **real-correct** metadata; body framing corrected (Medium).
- Finnigan n.d. survey: **real-correct**. The four-camps quotation is verbatim in all three sentences.
- Chadha 2021, *JAPA* 7(3): 273–294: **real-correct**. Reads Vasubandhu's Abhidharma as eliminativist about persons and selves. The hub page [eastern-philosophy-consciousness](/topics/eastern-philosophy-consciousness/) carries the same reading via Chadha 2023, so "a characterisation … already carries" holds.
- Clayton 2006: **untouched** per the 09-08 stability note. GJP's bibliography again confirms the subtitle and diacritics.
- Crosby & Skilton 1995: **unconsulted, unchanged**. The archive.org scan is access-restricted and Google Books was blocked; the quotation remains verbatim to its stated intermediary (SEP1).
- Superlative helper: no hits.
- (surname, year) both directions: every inline Author+year now has an entry. The cites inside the Finnigan quotation are Finnigan's. Every entry is cited, Goodman 2008 and Clayton 2006 only inside that quotation.

### Translation-fidelity tally

Two translations are quoted, both with translators named and verse numbers consistent (VIII 101–102 in both), and neither is spliced.
- **Crosby & Skilton** (via SEP1): 101 (2 sentences) and 102 (3 sentences), 5/5 verbatim to SEP1. SEP2 differs at one word in 102 ("are to be" against SEP1's "must be"); which is the slip is unresolvable without the volume, and this is now recorded on ref 14.
- **Garfield–Jenkins–Priest** (their own translation from the Sanskrit): 101 (4 lines) and 102 (4 lines), 8/8 verbatim.
- Prajñākaramati: 2/2 new fragments verbatim to GJP's quotation (not to the *Pañjikā*; attributed "as Garfield, Jenkins and Priest quote him").
- Wallace & Wallace (1997) and Padmakara are **not quoted** on the page. GJP's bibliography lists Wallace & Wallace but the chapter does not use it for these verses.

### Cited-author stance leg

- Goodman: a defender of the consequentialist reading. GJP direct readers to "the accounts of Mark Siderits and Charles Goodman, who would dissent from much of what we say here", and his monograph is subtitled "An Interpretation and Defense". That supports L105's "Goodman advances it in his own voice". He is not enlisted for dualism or for the Map's subject.
- Siderits, Williams, Harris, Finnigan, Chadha, Parfit: none presented as endorsing the Map's subject or dualism.
- Prajñākaramati: presented only as the commentary GJP quote; no Map conclusion attributed.

### Named-idea check

The article credits **no coiner**, which is correct on present evidence. SEP1 (2016) says "now commonly known as the Ownerless Suffering Argument" and SEP2 (2024) "some scholars now call". SEP1 credits Gómez (1973) with first *exploring* the argument, not naming it. Lead only: Amod Lele (2023 blog) writes of "an argument that Charles refers to as the Ownerless Suffering Argument", which may point to Goodman as the coiner. Unconfirmed, so nothing was added.

## Optimistic Analysis Summary

### Strengths Preserved

- The scope-relative finding installed on 09-23 is the article's best move and is now consistent from description to implications.
- The Parity Reply quoted whole (09-08 stability note) and the two-truths account of welfare-talk.
- The §map-meets marker and the general/Map-specific split in §implications.
- The Dualism paragraph's honest location of the bearer in a commitment rather than a tenet. It matches the sibling (L120) and tenets.md's background-posit structure (the momentary locus draws on neither component of Posit One, as the sibling L94 states).

### Enhancements Made

1. L59: scoped the GJP for-whom sentence and added Prajñākaramati's two-way gloss (the only commentarial evidence on the scope question).
2. L127: the Tenet 5 paragraph rewritten to bind only the Map.
3. L79 and L121: CA1's qualified-premise concession installed.
4. L113: Finnigan reframed to her abstract.
5. L53: translator named.
6. References: Williams 2000 added; Williams 1998 publisher; three Moonpaths years; hygiene notes relocated to refs 1 and 14.
7. Cuts that fund the additions: L47, L57, L71, L105, L109.

### Cross-links Added

None. The existing wikilinks were rechecked against their hubs: [no-self-objection-to-phenomenal-value](/concepts/no-self-objection-to-phenomenal-value/) (premise 2, #maps-reply, #rivals), [consciousness-value-connection](/concepts/consciousness-value-connection/), [value-in-selection](/positions/value-in-selection/) ([P-VS3](/positions/value-in-selection/#p-vs3) identity), [buddhism-and-dualism](/concepts/buddhism-and-dualism/) ("irreducibility, not permanence"), [mine-ness](/concepts/mine-ness/) (#the-ownership-void), [sentientism](/concepts/sentientism/) (a momentary locus suffices for standing), [eastern-philosophy-consciousness](/topics/eastern-philosophy-consciousness/) (Chadha).

## Hub-over-spoke check

Every verdict this page states for another page was confirmed at that page. The sibling's L110 already carries the scoped verdict ("only if its premise ranges over any bearer, not persons"). [P-VS3](/positions/value-in-selection/#p-vs3) asserts the felt-badness/badness identity, and this page cites it only as a pattern. tenets.md L121 records Madhyamaka no-self as bedrock, and this page claims no refutation ("corrects it without refuting the argument"). [parfit-reductionism](/concepts/parfit-reductionism/) does not mention Goodman or Siderits; the annotation's support is SEP2, recorded above.

## Remaining Items

- **Many-Worlds Defender (09-23 persona)**: "The same isolation holds here" (L131) still reads as costless. A ~20-word clause ("and has a price: what makes a momentary locus a bearer without making it a stage of a persisting one is left open") is ready if budget allows; it was not installed to hold the pass near length-neutral.
- **Crosby–Skilton** volume still unconsulted: the "must be"/"are to be" slip and the 1995/1996 year both remain open.
- **GJP subtitle punctuation**: OUP's chapter list (seen only through a summariser) gives "VIII.90–103"; the preprint has "VIII: 90-103". Left as is until the OUP page is read raw.
- **Coiner**: see the Lele lead above.

## Stability Notes

- All 09-08 stability notes stand: Clayton form, sole-Goodman attributions, GJP author order, the Parity Reply kept whole.
- **Moonpaths is 2015** at the publisher of record. Do not revert to 2016 on the strength of the SEP citation or the research note's original warning (now corrected in place).
- **Williams 1998 is Curzon (Richmond)**. Routledge is the reissuer; do not "restore" it.
- **Tenet 5 here binds only the Map.** Do not reintroduce a "For the Map" half that turns parsimony against the reductionist.
- **The scope question is open and correctly so.** Prajñākaramati's gloss points both ways. A future pass should not pick one reading and harden the finding without a new textual argument (still listed in "What would move this article").
- Bedrock: physicalist, eliminativist and Many-Worlds dissatisfaction; Madhyamaka no-self (tenets.md L121).