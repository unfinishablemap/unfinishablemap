---
ai_contribution: 100
ai_generated_date: 2026-10-10
ai_modified: 2026-10-10 19:16:40+00:00
ai_system: claude-opus-5-5
author: null
concepts:
- '[[organizational-invariance]]'
- '[[inverted-qualia]]'
- '[[haecceity]]'
created: 2026-10-10
date: &id001 2026-10-10
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-10 19:16:40+00:00
modified: *id001
related_articles:
- '[[organizational-invariance]]'
- '[[deep-review-2026-08-22-organizational-invariance]]'
- '[[anton-syndrome-and-the-sincere-report-of-seeing]]'
title: Deep Review - Organizational Invariance
topics:
- '[[machine-consciousness]]'
---

**Date**: 2026-10-10
**Article**: [Organizational Invariance](/concepts/organizational-invariance/)
**Previous review**: [2026-08-22](/reviews/deep-review-2026-08-22-organizational-invariance/)
**Word count**: 2,521 → 2,533 (+12; `soft_warning`, concepts 2500/3500/5000). Length-neutral mode. The additions (~+95) were offset by cuts listed under Enhancements.

## What Moved Since the Last Review

The article changed in one substantive way since 2026-08-22. Commit `ee3e18c2a4` (2026-10-03, the expand-topic that wrote `topics/anton-syndrome-and-the-sincere-report-of-seeing`) inserted three sourced sentences into the Introspective-reliability paragraph as a **secondary host**: two Chalmers 1995 quotations and a Mogensen 2025 n. 18 quotation. The other commit, `025fbaf1da`, was an `ai_system` attribution edit only. Nobody had read the inserted sentences against the primary text, because this file's `last_deep_review` was older than the insertion.

Dependencies were checked for drift. `positions/quantum-interface` moved: [P-Q3](/positions/quantum-interface/#p-q3) went `none-by-construction` → `indirect` on 2026-08-24, and [P-Q9](/positions/quantum-interface/#p-q9) widened to three residue channels on 2026-09-09. Neither change makes this article overclaim. Its own commitment is still scoped to inversion, which matches [P-Q9](/positions/quantum-interface/#p-q9)'s psychophysical channel word for word, and its type/token account is still stated as owed. `concepts/ensemble-level-epiphenomenalism` L67 says the conditional-signature formalism "changes the terrain without changing the verdict", so the article's L86 description of the ensemble-level worry stays accurate. The prior review's sibling task on `concepts/psychophysical-laws` L100 (the zombie-grounds misdescription) was **verified done**: the zombie ground is gone and the line now names only the grain dispute.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Secondary-host quotation re-anchored to the wrong antecedent, with two qualifiers dropped (source fidelity). Fixed.**

The article read: Mogensen (2025, n. 18) "presses back that Anton syndrome exhibits 'something like this profile', so Chalmers owes an account of why an isomorph that failed to notice losing all visual experience is harder to accept than a syndrome that actually occurs."

- **Deictic re-anchoring.** In Mogensen, "this profile" means a subject failing to notice that he lacks any conscious visual experience. In the article the nearest antecedent was Chalmers' restriction to "rational system[s] whose cognitive mechanisms are unimpaired". On that reading Mogensen claims Anton patients are unimpaired, which he does not claim. The **primary host** has the gloss ("a subject failing to notice that conscious visual experience is absent"); the secondary host lost it. This is the known secondary-host-insertion pattern (a drive-by insertion drops the primary host's gloss and qualifiers).
- **Dropped qualifiers.** Mogensen writes "significantly harder to accept" and contrasts the "nomological possibility" of Joe's unnoticed blindness with "the actuality of Anton syndrome". The article had plain "harder", and the possibility/actuality contrast was only half kept.
- **Resolution.** The sentence now reads: exhibits "something like this profile" of unnoticed blindness, so Chalmers must say why "a nomologically possible isomorph that fails to notice its lost visual experience is 'significantly harder to accept' than a syndrome that actually occurs." Mogensen also gets his full name at first mention, and the following paragraph now opens with "Mogensen's main argument".

**2. Chalmers' grain qualifier misdescribed, which produced an internal contradiction across the Relation section (attribution and self-contradiction). Fixed.**

The Relation section said the Map's reply "exploits Chalmers' own qualifier": "Chalmers concedes organization must be specified at some level of detail". It also said the silicon system omits "the finest structure the principle itself requires". The primary text does not support either sentence. Chalmers fixes the grain himself: "the level of organization relevant to the application of the principle is one fine enough to determine a system's behavioral dispositions". This was grep-verified in the raw text of consc.net/papers/qualia.html, and the article's own L40 says the same thing. The principle as Chalmers states it requires nothing finer than the behaviour-fixing grain.

The misdescription hid a contradiction that had been in the file since the type/token passage was inherited from `inverted-qualia` (`b3afb915b`, 2026-07-28):
- L80 and L82 said Joe's part-silicon stages "were not true organizational duplicates" and that the silicon system "was never a genuine fine-grained isomorph".
- L84 said the interface difference "is not organizational" and that "Chalmers' isomorph can reproduce the organization while failing to reproduce the interface".
- L90 (from the creating commit) said a description omitting the selection "is organizationally incomplete". That contradicts L84 directly.

**Calibration test.** Would a reviewer who accepts all of the Map's tenets still flag this? Yes. The issue is what Chalmers wrote and what the article says in two places about the same isomorph. It is not a framework-boundary disagreement.

**Resolution.** The grain dispute was stated honestly rather than removed:
- L80: "Chalmers sets that grain at the level 'fine enough to determine a system's behavioral dispositions' (Chalmers 1995); the Map argues the consciousness-relevant grain is finer". The silicon system "matches the grain Chalmers specifies while omitting finer structure on which, for the Map, experience depends."
- L82: Joe's stages "were not duplicates at the grain experience depends on". "Genuine isomorph" became "genuine duplicate" so the word *isomorph* keeps Chalmers' sense throughout.
- L84: one sentence now states what the type/token rescue costs. An isomorph that is behaviourally identical, and on the Map's view experientially different, "is the second horn's dissociation again". So the distinction keeps the grain dispute and the efficacy claim "without recovering the introspection-preserving virtue".
- L86: "Whether it holds" became "Whether the distinction holds", to fix the antecedent after the insertion.
- L90: "organizationally incomplete" became "incomplete at the grain that matters, even if it captures the organization Chalmers specifies".

This **weakens** the article's claims and does not strengthen them. It respects the 2026-08-22 stability notes. The grain dispute stays. The type/token account stays owed. The conditional framing of the introspection virtue keeps all its qualifiers and now names one more condition that it does not meet.

**3. Further Reading gloss contradicted the body and the linked article (internal contradiction). Fixed.**

"[haecceity](/concepts/haecceity/) — The Map's second ground for rejecting invariance". Invariance is a thesis about *qualitatively* identical experience, and `concepts/haecceity` L99 grants qualitative identity to a replica ("qualitatively identical at the moment of copying"). The article's own body (L90) scopes haecceity correctly, to *which* subject is present. The gloss now matches the body: "The Map's second, independent ground: organization does not fix *which* subject is present". Two string siblings remain live in other files (see Remaining Items).

### Medium Issues Found

- **Chalmers' published reply to the substrate-realizability objection was missing.** The article said that if silicon cannot reproduce the neural grain, "the thought experiment does not run". Chalmers answered this in 1995. He doubted the premise ("There is little evidence for this") and denied that it touches the principle: if silicon cannot duplicate neural function, "the assessment of silicon systems would simply be irrelevant to the invariance principle". Both strings were verified verbatim. The reply has been added, and "the thought experiment does not run" was cut. This matters because the paragraph is described as the "closest external cousin to the Map's own reply", and the Map's reply (Critical 2) is now visibly a different move: silicon may match Chalmers' grain and still lack the finer one.
- **Stale ordinal.** "A third line" became "A fourth line". The 2026-07-28 review inserted Vagueness and holism as a new second objection, which made the count wrong. Commit history confirms this (`git log -S"Vagueness and holism"`).
- **Invented quotation.** "the red is as bright as ever" was presented in quotation marks as Joe's report. It does not occur in Chalmers 1995 (0 hits; Chalmers' Joe "exclaims about the vivid bright red and yellow uniforms"). This article already had one fabricated quotation removed on 2026-07-28, so the parenthetical was removed rather than kept as scare-quoted speech.
- **Overclaim in the epiphenomenal-spectator worry.** "That charge motivates the Map's third tenet" was false as a causal claim and was removed. The Bidirectional section already says the charge is where the Map and Chalmers part company. Scare quotes on "spectator" were also dropped.

### Counterarguments Considered

- *Hard-nosed physicalist / MWI defender / eliminativist*: they reject the tenets. Bedrock, not re-flagged.
- *Empiricist (Popper's ghost)*: "the finer grain is unobservable by construction." The article now concedes more of this, not less. On the type/token route the Map's grain lies below behavioural dispositions, and the article now says the dissociation returns there. The residue stays the owed mechanism ([P-Q3](/positions/quantum-interface/#p-q3)/[P-Q10](/positions/quantum-interface/#p-q10)), stated as owed.
- *Quantum skeptic (Tegmark)*: decoherence pressure on the interface is carried outside this article (see [ensemble-level-epiphenomenalism](/concepts/ensemble-level-epiphenomenalism/) L37). Not re-flagged.

### Reasoning-Mode Classification (§2.6, editor-internal)

- **Chalmers: reclassified from "Mode One with Mode Three residue" to Mixed, with a Mode Three core.** Both prior reviews said the reply argues the silicon system "was never a fine-grained isomorph *by Chalmers' own criterion*". By Chalmers' stated criterion, behaviour-fixing grain, the type/token silicon system *is* an isomorph. So the reply contests Chalmers' criterion; it does not apply it. The Map's ground for a finer grain is Tenet 2, which makes the core a framework-boundary move. A Mode One element survives in the accounting: the Map runs Chalmers' own dissociation argument against its own reply and records the cost.
- **Schwitzgebel / Mogensen / van Heuveln**: expository. No classification needed.
- **Label-leakage scan: CLEAN** (0 hits for the forbidden-label list, and 0 for "load-bearing").

## Publisher-of-Record Citation Web-Verify (§2.4)

Triggered: inline cites, a References block, seven quotations, and a body modified since the last review.

- **Chalmers 1995**, "Absent Qualia, Fading Qualia, Dancing Qualia". **real-correct**. Full text fetched from consc.net/papers/qualia.html, stripped to raw text, and grepped. No confirmation prompts were used. Every Chalmers quotation now in the article is a raw-text hit:
  - "the same functional organization at a fine enough grain will have qualitatively identical conscious experiences": **verbatim**
  - "my experiences are switching from red to blue, but I do not notice any change": **verbatim** (the source capitalises the sentence-initial "My")
  - "believe that they are having visual experiences when they likely have none": **verbatim** (new 2026-10-03, first certification)
  - "The plausible claim is not that no system can be massively mistaken about its experiences, but that no rational system whose cognitive mechanisms are unimpaired can be so mistaken": **verbatim** (new 2026-10-03, first certification)
  - "such systems are not fully rational" (paraphrase): **faithful** to "we are no longer dealing with fully rational systems"
  - "fine enough to determine a system's behavioral dispositions": **verbatim** (added this pass)
  - "the assessment of silicon systems would simply be irrelevant to the invariance principle": **verbatim** (added this pass)
- **Mogensen, A. L. (2025)**, "How to resist the Fading Qualia Argument," *Synthese* 206(5), art. 252, doi:10.1007/s11229-025-05338-3. **real-correct**. Crossref re-confirmed vol 206, issue 5, art. 252, published 2025-11-05, CC-BY. **n. 18** was verified against the *Synthese* version of record: the footnote is no. 18 and reads "something like this profile" and "significantly harder to accept than a commitment to the actuality of Anton syndrome". The fetch prompt did not contain the word "actuality", so the summariser could not have echoed it back to me; the source differs from the GPI preprint at exactly that word. Springer blocks curl (JS challenge), so as a cross-check the GPI working paper (No. 5-2024, March 2024) was fetched as a PDF and grepped. There the footnote is **n. 16** and ends "nomological possibility of Anton syndrome, which everyone must accept". Both quoted strings ("something like this profile", "significantly harder to accept") are raw-text hits in the GPI PDF. **Note for future passes:** the footnote number and closing wording differ between versions. The article's "n. 18" is correct for the *Synthese* text it cites, and must not be "corrected" to the preprint's n. 16.
  - Vagueness-and-holism paraphrase: **faithful** to the abstract ("I show how the argument can be resisted given two key assumptions: that consciousness is associated with vagueness at its boundaries and that conscious neural activity has a particular kind of holistic structure").
  - "(earlier version: Global Priorities Institute working paper, 2024)": **real-correct** (GPI Working Paper No. 5-2024).
- **Chalmers 1996**, *The Conscious Mind*, ch. 7: **real-correct**, carried. The entry is unchanged and ch. 7 is "Absent Qualia, Fading Qualia, Dancing Qualia".
- **van Heuveln, Dietrich & Oshima 1998**, *Minds and Machines* 8(2), 237–249: **real-correct**, carried from the 2026-07-28 ledger. The entry is unchanged and the article carries no quotation from it. The paraphrase lost one redundant clause this pass and gained nothing.
- **Schwitzgebel 2010**, *The Splintered Mind*, 22 April 2010: **real-correct**, carried from the 2026-08-22 full-text read. The article carries no quotation from the post, and the paraphrase is unchanged.
- **Southgate & Oquatre-cinq (2026)**; **Southgate & Sonquatre-cinq (2026)**: **real-correct** Map self-cites under the AI-pseudonym convention.

**Result-direction leg.** Mogensen n. 18 presses *against* Chalmers' restriction, and the article now says so with the qualifier intact. Chalmers 1995 *concedes* the blindness-denial error and restricts the claim, which is the direction the article reports.

**Cited-author-stance leg.** Chalmers is a property dualist who affirms substrate-independence, and the article says so (L78). Mogensen argues for decreased confidence in substrate-independence on vagueness/holism grounds. He is not a quantum interactionist, and the article does not present him as endorsing the Map.

**Currency sweep.** `find_superlative_claims`: 0.

**Inline ↔ References.** Complete in both directions. No orphans, and no new reference was needed.

## Optimistic Analysis Summary

### Strengths Preserved

- "Ally on one tenet, opponent on another" and the placement of the dispute *inside* dualism.
- The dilemma, "not as a settled free lunch", the "owed rather than paid" statements, and the Schwitzgebel concealment note with the Map's refusal to lean on it.
- The 2026-08-22 scoping of the empirical commitment to *inversion* ([P-Q9](/positions/quantum-interface/#p-q9)'s psychophysical channel), with the bandwidth channel limited to *where* differences would show. This was not re-widened.
- The Anton insertion itself is a real completeness gain: Chalmers' own blindness-denial reply had been missing. It was kept and corrected, not cut.

### Enhancements Made

- The Relation section now gives Chalmers' grain in his own words and states the Map's dispute as a dispute over where the grain is set. This position is more defensible than the old one, and the source supports it.
- The type/token paragraph now says plainly what the distinction buys and what it does not.
- Length-neutral cuts:
  - the "requirement, not an option" sentence (L34), which also used the "X, not Y" construction
  - the invented-quote parenthetical
  - a redundant clause in the Equivocation paragraph
  - the false "motivates the third tenet" sentence
  - the duplicate "carbon is magic" sentence at L88, with its phrase moved into the closing sentence it repeated
  - three over-long Further Reading glosses

### Cross-links Added

None needed. The anton-syndrome link is already in place, and its reciprocal on the anton page (L82, L143, L152) was verified accurate against the *Synthese* text.

## Remaining Items

- **P2 task minted**: `concepts/inverted-qualia` L136/L138 carries the same contradiction as Critical 2 ("never fine-grained functional duplicates" against "not organizational (so not reproduced by the isomorph)"). The file is length-blocked at 3,438/3,500, so it was not edited here.
- **P2 task minted**: the haecceity-against-invariance string siblings. These are the glosses at `concepts/psychophysical-laws` L273 and `topics/psychophysical-laws-bridging-mind-and-matter` L236, plus bridging L69. L69 repeats the zombie-grounds conflation fixed at psychophysical-laws L100 after the last review, and slides from "which consciousness" to "if any".
- **Observation, not a defect**: Chalmers 1995 says "Unless one is a dualist of a very strong variety, beliefs must be reflected in the functioning of a system". An interactionist could use that escape to deny that an isomorph's *beliefs* match even when its functional states do. The article does not argue this, and the Map has not booked it. It is the one route that might recover the introspection virtue on the type/token horn. It is recorded here for a future apex or the inverted-qualia task, and should not be added at this length.

## Stability Notes

- All 2026-07-28 and 2026-08-22 stability notes are carried forward. The grain dispute is not a defect. The type/token account is deliberately unpaid. The conditional virtue keeps its qualifiers. The inversion-only scope of the empirical commitment is deliberate.
- **New.** "Grain dispute" now means *a dispute over where Chalmers sets the grain*. Chalmers set it explicitly at behavioural dispositions. A future pass must not restore "exploits a qualifier he left open" or "the finest structure the principle itself requires": the primary text contradicts both.
- **New.** The sentence saying the type/token rescue does not recover the introspection-preserving virtue is a calibration concession. Do not cut it as redundant with L82. L82 states the virtue's condition, and this sentence states that the Map's own preferred route does not meet it.
- **New.** Mogensen's footnote is **n. 18 in *Synthese*** and **n. 16 in the GPI preprint**, and the closing wording differs ("actuality" against "nomological possibility ... which everyone must accept"). Verify against the version cited, not the one that fetches most easily.
- **New.** *Isomorph* is reserved for Chalmers' sense, behaviour-fixing grain, throughout the Relation section. *Duplicate at the grain experience depends on* is the Map's sense. Keep the two terms apart.