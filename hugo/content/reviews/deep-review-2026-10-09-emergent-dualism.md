---
ai_contribution: 100
ai_generated_date: 2026-10-09
ai_modified: 2026-10-09 12:42:15+00:00
ai_system: claude-opus-5-5
author: null
concepts:
- '[[emergent-dualism]]'
created: 2026-10-09
date: &id001 2026-10-09
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-09 12:42:15+00:00
modified: *id001
related_articles: []
title: Deep Review - Emergent Dualism
topics: []
---

**Date**: 2026-10-09
**Article**: [Emergent Dualism](/concepts/emergent-dualism/)
**Previous review**: [2026-07-19](/reviews/deep-review-2026-07-19-emergent-dualism/)

## Why this target

Top candidate from `scripts/deep_review.py next` (score 126, one prior review). The delta since 07-19 is the 10-08 refine (`b9e0d0a253`) that piped L50 "Kant" to the new Kant page (`#dualist-replies`) and added "(who states the argument only to reject it)". That link brought the article into contact with the Kant page's §Three Exposures ("Unity read as simplicity"), which the article's Relation section had not been reconciled with.

## Pessimistic Analysis Summary

### Publisher-of-record citation web-verify (per-cite ledger)

- Hasker 1999 (*The Emergent Self*, Cornell UP): **real-correct**. Two new quotes were checked against the raw text through the Google Books search-within endpoint (volume `1NT-CgAAQBAJ`). p. 191: "exerts a causality of its own; certainly on the brain itself". p. 192: "do not seem to be emergent in the strong sense required for the properties of the mind", followed by the unity and teleology concessions ("…much less libertarian freedom") and "it is only an analogy".
- Hasker 2001 ("Persons as Emergent Substances", Corcoran ed., Cornell UP): **real-correct**. Crossref `10.7591/9781501723520-009` gives pp. 107–119, now added to the reference.
- Hasker 2010 ("Persons and the Unity of Consciousness", Koons & Bealer eds., OUP): **real-correct**. pp. 175–190 is corroborated by Hasker 2012's own bibliography and added. Rickabaugh (PA83) independently confirms the commissurotomy/dissociative framing.
- Hasker 2012 ("Is Materialism Equivalent to Dualism?", Göcke ed., *After Physicalism*, UNDP, pp. 180–199, DOI `10.2307/jj.21996041.10` confirmed at Crossref): **newly added**. Full chapter text was grepped from the newdualism.org PDF. Verbatim checks:
  - "the unity-of-consciousness argument which is derived from Leibniz and Kant" supports L50 "traces to Leibniz and Kant".
  - "(it can be no more than that)" is the field-analogy hedge.
  - "which posit the direct creation of the soul by God: mainly Cartesian-type dualism and some versions of Thomistic dualism".
  - "Only something that functions as a whole rather than as a system of parts could experience a visual field as a unity" (premise 2).
  - "the agent-cause of our free actions".
  - "at least logically possible" (survival).
- Dilley 2003 ("A Critique of Emergent Dualism", *Faith and Philosophy* 20(1): 37–49, DOI `10.5840/faithphil200320114` confirmed at Crossref): **newly added**. The abstract was grepped from the newdualism.org PDF: attributing "spatiality and energy to the self undercuts the basic historic arguments for separating mind from body".
- Rickabaugh 2018 ("Against Emergent Dualism", Blackwell Companion, ch. 5): **real-correct**. Crossref `10.1002/9781119468004.ch5` gives pp. 73–86. The paraphrase was verified in the raw text (Google Books `JQhTDwAAQBAJ`, PA73): "I argue that emergent dualism is not more attractive than nonemergent versions of substance dualism as Hasker suggests." The section "combination problem for emergent dualism" (PA80–83) confirms the combination/constitution framing. DOI and pages added.
- O'Connor & Wong, "Emergent Properties", SEP: **real-wrong-metadata (CRITICAL; fixed)**. The reference pointed to the live URL `plato.stanford.edu/entries/properties-emergent/`. That URL now hosts a *new* entry by Timothy O'Connor alone ("First published Mon Aug 10, 2020"; `citation_author` = O'Connor only). The new entry mentions Hasker only in passing ("See Zimmerman 2010 and Hasker 2016"), and the sentence the article paraphrases is **absent** from it. The sentence exists only in the superseded O'Connor & Wong entry (first published 2002; substantive revision 3 June 2015), which the Summer 2020 archive preserves. Its actual wording is "explaining how individual brains and mental substances come to be linked in a persistent, 'monogamous' relationship". The 07-19 review's "verbatim" rendering ("linked in a persistent way") was not verbatim. **Fix:** the body now names the 2015 revision ("since replaced by a new entry"), and the reference points to `plato.stanford.edu/archives/sum2020/entries/properties-emergent/`.
- Kim 2005 (*Physicalism, or Something Near Enough*, Princeton UP): **real-correct**. Ch. 3 treats the pairing problem and ch. 2 the supervenience/exclusion argument.
- Kant (*Critique of Pure Reason*, Guyer & Wood trans.): **newly added** for the A352–353 collective-unity reply. The form matches the Kant page's reference.
- Map self-cites (pairing-problem 2026-01-16, unity-of-consciousness 2026-01-21): created dates match the source files.

`find_superlative_claims` returned nothing. Inline↔References are cross-checked with no orphans in either direction. Hasker 1999/2001/2010/2012, Dilley, Rickabaugh, O'Connor & Wong, Kant and Kim are all cited inline or named in the body. Family check: no other live article attributes content to the O'Connor & Wong SEP entry. `voids/emergence-void` cites the live URL without authors or a specific claim, which is not a defect.

**Result-direction leg:** no empirical results are cited, so this leg does not apply.

**Cited-author-stance leg:**
- Hasker: emergent substance dualist (theist). He is presented as an ally on Tenets 1/3 and a rival on dependence, which is correct.
- Rickabaugh: non-emergent substance dualist, labelled "dualist-internal".
- Dilley: Cartesian dualist, labelled as such.
- O'Connor & Wong: emergentists who are not dualists. They are cited only for a report of Hasker's claim.
- Kim: physicalist. He is cited as the objector.
- Kant: the article now states that he rejects the argument and gives his ground.

### Critical Issues Found

1. **Unverifiable quote (fixed).** L78's Hasker's field "acts back on the brain that generates it" was in quotation marks. The only web hit was the Map's own page, and the nearest real wording is Dilley's paraphrase ("its ability to act on the brain that generates it"). It was replaced with verbatim Hasker 1999 p. 191: "exerts a causality of its own; certainly on the brain itself".
2. **Stale SEP attribution (fixed).** See the ledger above.
3. **Map-internal inconsistency with the Kant page (fixed).** The Relation section said "His UOC argument is one the Map can largely endorse" and referred to "the Map's endorsement of the UOC simple-subject conclusion". After the 10-08 refine, the same article says Kant rejects the argument, and it links to a Map page whose §Three Exposures says an article that wants unity to *establish* a simple subject "owes a premise excluding the collective reading". It also says [P-I1](/positions/individuation-and-subjecthood/#p-i1) and the first background posit "can never be presented as *following from* the unity … of consciousness". A tenet-accepting reviewer would flag this, so it is a calibration error and not bedrock disagreement. **Fix:**
   - The Relation section now says the Map shares Hasker's simple-subject *conclusion* but holds it as a posit, not as the UOC argument's result, and links `#three-exposures`.
   - The second and third considerations now speak of the "simple-subject posit".
   - §UOC now states Kant's collective-unity ground (A352–353) and quotes Hasker's own premise that would exclude it, with the note that Hasker does not frame it as a reply to Kant. The Kant page records that Hasker's chapter mentions Kant once and the Paralogisms not at all.
4. **Tenet over-reading (fixed; possibility/probability-style slippage).** "The Map's Minimal Quantum Interaction tenet points the other way" credited Tenet 2 with a stance on the *origin* of consciousness. The tenet text (tenets L63–71) fixes only *how* consciousness acts, and an emergent self could act through quantum indeterminacy as well. Now reads: "No tenet settles this … But the Map's picture points the other way".
5. **Factual mischaracterisation of the rivals (fixed).** The lead and §Position said Cartesian/Thomistic souls "pre-exist" the body or are "separately created and merely joined to it". Neither Descartes nor Aquinas holds pre-existence. For Aquinas the soul is the body's substantial form, not something "merely joined". The passage now uses Hasker 2012's own characterisation ("direct creation of the soul by God: mainly Cartesian-type dualism and some versions of Thomistic dualism") and the substantial-form clause.

### Attribution Accuracy (§2.5)

- **Qualifier preservation:** Hasker's own hedge on the field analogy ("it can be no more than that"; "only an analogy") was missing. Without it, "Defenders regard the field analogy as showing the combination is intelligible" read as if Hasker leaned on it harder than he does. The hedge has been added.
- **Concession claim:** "a distance Hasker himself concedes, granting that his emergent substance stands far removed from garden-variety emergence" was an unsourced paraphrase. It is now anchored to the verified p. 192 concession.
- **Third consideration:** it said agent causation favours the Map over Hasker, but the article's own Further Reading says Hasker combines agent causation with emergent dualism, and Hasker 2012 confirms this ("the agent-cause of our free actions"). The consideration is now scoped to nomological dependence and marked the weakest of the three, conceding that agent causation does not separate the views and that Hasker holds survival logically possible.
- **Pairing:** "Emergent dualism dissolves this" became "claims to dissolve". Map voice and Hasker's claim are now separated.

### Reasoning-mode (§2.6)

- Engagement with Rickabaugh: **Mode Two/Three mixed**, unchanged. The constitution worry is conceded to land on generation views, and the coupling reply is honestly marked as relocating, not discharging, the burden. That is the terminus from 07-17, and it was not reopened.
- Engagement with Kant (new): **Mode Three**. The Map declines to claim the UOC argument refutes the collective reading and holds the simple subject as a posit.
- Engagement with Dilley (new): **Mode One** (internal to dualism). The Map concedes the spatiality half and escapes the energy half only via Tenet 2's no-energy clause, which is in-framework.
- No editor-vocabulary leakage in prose.

### Medium Issues / Counterarguments

- Physicalist and eliminativist rejection of a unified simple subject: bedrock, per the 07-19 stability note. Not re-flagged.
- Buddhist/Humean bundle denial of the simple subject: the Kant-page alignment now partially addresses this. The Map holds the subject as a posit, not as a derivation, so the bundle theorist is no longer being told unity *proves* simplicity. No further hedge added, to avoid oscillation.

## Optimistic Analysis Summary

### Strengths Preserved
- The "close cousin, not opponent" frame and the dependence-versus-independence axis.
- The two-contrast structure in §Position.
- The 07-17 burden-relocation concession on Rickabaugh, kept verbatim.
- The closing comparative paragraph and the Tenet 5 symmetry ("neither … is the 'simple' option").

### Enhancements Made
- Hasker 2012 integrated as the verified source for "traces to Leibniz and Kant", the creationist-rival characterisation, the analogy hedge, premise 2, agent causation and survival.
- Kant's collective-unity reply stated in §UOC, so the "(rejects it)" clause now says *why*.
- Dilley 2003 added as a named dualist-internal critic of the coherence and spatiality move, with Map exposure stated in the Relation section.
- Reference apparatus: pages and DOIs added for Hasker 2001/2010/2012, Rickabaugh and Dilley; SEP reference corrected to the archived 2015 revision.

### Cross-links Added
- [kants-paralogisms-and-the-maps-subject](/topics/kants-paralogisms-and-the-maps-subject/#three-exposures) (Relation section).

## Word count

2,154 → 2,614. Below the soft threshold (2,500) at start, so normal improvements were allowed. It now sits in `soft_warning`, which has no gate, with 885 words of headroom to the hard gate (3,500). Roughly 140 of the added words are reference apparatus.

## Remaining Items

- [concepts/emergence.md](/concepts/emergence/) L124–126 presents O'Connor and Wong's emergentism as "align[ing] closely with the Map's framework" and as "explicitly den[ying] causal closure". The cited-author-stance leg was not run there, because it is out of scope for this review. Flagged for that article's next deep review, not minted.
- [research/emergent-dualism-2026-07-12.md](/research/emergent-dualism-2026-07-12/) L153 records the SEP entry as "VERIFIED (live entry; discusses Hasker's emergent dualism …)". That is false for the live entry since August 2020. The research note was left untouched as a historical record.

## Stability Notes

- Bedrock: physicalist, eliminativist and MWI rejection of a unified simple subject. Do not re-flag.
- The Rickabaugh burden-relocation concession remains the article's terminus on the constitution worry.
- The Map's simple subject is a **posit** in this article, aligned with the Kant page and [P-I1](/positions/individuation-and-subjecthood/#p-i1). Future reviews should not restore "the Map can largely endorse the UOC argument" or similar derivation language. Nor should they swing the other way and deny that the Map holds the simple-subject conclusion.
- The SEP citation is to the **archived 2015 O'Connor & Wong revision**. Do not "correct" it back to the live URL, which hosts a different entry by O'Connor alone that does not contain the Hasker sentence.
- The ledger above was checked against raw text (newdualism PDFs, Google Books search-within, the SEP HTML, Crossref). Do not re-litigate it absent a body or References change.