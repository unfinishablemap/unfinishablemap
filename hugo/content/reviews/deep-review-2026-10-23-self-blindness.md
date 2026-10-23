---
ai_contribution: 100
ai_generated_date: 2026-10-23
ai_modified: 2026-10-23 16:26:38+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-10-23
date: &id001 2026-10-23
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-23 16:26:38+00:00
modified: *id001
related_articles: []
title: Deep Review - Self-Blindness
topics: []
---

**Date**: 2026-10-23
**Article**: [Self-Blindness](/concepts/self-blindness/)
**Previous review**: Never. The page was created 2026-10-23 at about 01:05Z by expand-topic from [self-blindness-and-partial-introspective-failure-2026-10-10](/research/self-blindness-and-partial-introspective-failure-2026-10-10/).
**Word count** (`analyze_length`): 2,816 → 2,820 (+4). Concepts soft is 2,500 and hard is 3,500, so the pass ran length-neutral.

## Verdict

The page is sound. Its calibration is honest: the five-condition test is labelled as the Map's construction, Shoemaker is firewalled from the Map's dualism, and Tenet 1 is "fits without evidencing". The citation base is real. Every Shoemaker quote checked against the 1996 book's OCR is verbatim. The defects were qualifier-level. The lead overcounted the conditions each case fails. One quotation dropped Shoemaker's own conditional. One SEP gloss dropped "entirely". Several clauses stated Map readings or secondary reports a notch more strongly than their sources. All were fixed in place.

## Quote Verification (Mandatory Check 1)

**Route.** The Google Books search-within endpoint (`jscmd=SearchWithinVolume2`) was dead today. The volume id `uwfIt6gxZzgC` returned `searchable: true` with zero hits for the control "perspective". A cross-book control on the Hirsch volume `iPRqtcjeHPsC`, live on 2026-09-16, also returned zero. So the zeros reflect an endpoint failure, not absence.

The working route was **archive.org full-text search** (`services/search/beta/page_production/?service_backend=fts`) on the OCR of item `firstpersonpersp0000shoe` (CUP 1996, ISBN 9780521568715). Its controls:
- Positive: "self-blind creature could frame" gives 1 hit, in this book.
- Negative: a nonsense phrase gives 0.

The OCR breaks words at line ends ("self-blind- ness", "know- ing", "over- step"), so zeros were re-probed on spans that avoid broken words.

**Limit.** The FTS returns text, not page numbers (`page_num` is always 1). So the wording of every span below is verified, but the page locators still rest on the 2026-10-10 Google Books snippets. The one exception is p. 224, where the folio "224" appears inline in the OCR inside the independence-condition sentence.

**Result: all 28 distinct quoted Shoemaker strings on the page verified verbatim, 0 failed**, including those on pp. 24, 31, 71 and 80. Four context spans were also checked: on p. 225, "equally damaging", the blindsight listing and the Nisbett and Wilson citation; on p. 24, the sentence's continuation.
- p. 31, the definition: "self-blind creature could frame and understand ascrip- tions to itself of various mental states, but would be incapable of know- ing by self-acquaintance whether such self-ascriptions were true". All three segments hit.
- p. 31: "would it be appropriate to think of the capacity for self-acquaintance as a quasi-perceptual capacity".
- p. 224: "caused by those mental states, via a reliable belief-producing mecha- nism"; "is independent of their being known in this way, and 224 even of there existing" (inline folio).
- p. 225: "Although I am equally opposed to Cartesianism and the broad per- ceptual model"; "equally damaging to the Cartesian conception"; "One of the most striking is 'blindsight.'"; "confabulation" (see Nisbett and Wilson 1977).
- p. 39: "self-blind man who has human intelligence and conceptual capacity".
- p. 237: "the logical impropriety of affirming something while denying that one believes it".
- p. 36: "give away the fact that he lacks self-acquaintance".
- p. 228: "take away a lot else". p. 229: "self-blindness with respect to pain seems to be an impossibility".
- p. 231: "perceptual experiences in the sense we do"; "states that play some of the functional role of perceptual experiences". The form without "that" is confirmed, against the `06Shoe` handout.
- p. 234: "blindness is not self-blind- ness, and not introspective blindness"; "the occupants of the body"; "If anything would make it reasonable to say that the agent and the agnostic are one and the same"; "beliefs and desire that can independently be ascribed to the agnostic".
- p. 25: "at least for the sake of discussion"; "logically possible for a person to be mistaken about his own mental states, of whatever kind".
- p. 71: "Failures of rationality, such as those in- volved in self-deception, can bring with them failures in access"; "the rule rather than the exception, we over- step the bounds of intelligibility"; "is less than perfect because our rationality is less than perfect".
- p. 80: "lots of the beliefs that one can be said to have at a time are not available to one at that time".
- p. 93: "in some conceptually central class of cases, ones blessed with more rationality than is usual in human affairs".
- p. 49: "puts a rather heavy burden on the concept of rationality".
- p. 24: "Although I think that there are lots of good reasons for rejecting Cartesian dualism, I do not think that the truth of the Humean denial is one of them". The continuation was read so that the stance clause is not spliced. Shoemaker does hold the reasons for rejection to be good.
- p. 207: "There is no organ of introspection that the self directs ei- ther to itself".
- p. 242: "what I call the core realization of it and what I call the total realization".

**Subject-splice check.** Each quotation's grammatical subject sits outside the quotation marks and matches the source. There was one fidelity defect, the conditional at p. 234, fixed under critical issue 2 below.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Lead overcounted the conditions failed (internal contradiction / universal without scope).**
   - Before: the five clinical cases "each fall outside the thesis on at least two of five conditions". The table's Anton row reads "1, 4" with "usually impaired on independent markers".
   - The Anton page L84 names pressure cases with preserved cognition: Swartz and Brust's "otherwise mentally normal" patient and Harpaste. For those, only C1 is a definite failure.
   - The DID row also listed C5 as "failed" while its Why cell says "contested".
   - After: the lead reads "on at least one of five conditions ..., most on two or more". The table cells read "1 (4 usually)" and "2, 3 (5 contested)".
   - The verdict does not move, because one failed condition suffices. The overcount came from the research note's headline (a), whose own table never marks Anton's C4 as "Fails".
2. **Dropped conditional in the agent/agnostic quote (qualifier preservation).**
   - Before: "What would make it reasonable to call them one person is that ...".
   - Source (verified): "If anything would make it reasonable to say that the agent and the agnostic are one and the same person, it would be the fact that ...".
   - After: "'If anything would make it reasonable' to call them one person, it would be that ...". Shoemaker does not assert that anything does.
3. **SEP gloss dropped "entirely".**
   - Before: Schwitzgebel's entry "cites them as arguing that schizophrenia shows introspection breaking down, the possibility inner-sense views imply and Shoemaker denies".
   - SEP (verified): the detection faculty could "break down entirely ... (see also Nichols and Stich 2003, who argue that schizophrenia provides such a case)".
   - Shoemaker allows local breakdown, so the unqualified version attributed to him a denial he does not make.
   - After: "breaking down entirely".

### Medium Issues Found

4. **DID irrationality clause overclaimed circularity.**
   - Before: "the only irrationality Shoemaker can cite is the motivated non-search, identified through the very failure it is meant to explain."
   - The research note (L288) says it is "diagnosed through the access failure plus a motive". Parrott (n. 25) also names dissociation or alienation as a distinct irrationality, so "the only" was too strong.
   - After: "the irrationality Shoemaker would most plausibly cite ..., identified largely through ...". This matches the Chalmers section's own "largely". It is an over-concession to the critique, now corrected.
5. **Alexithymia conclusion dropped its conditional.**
   - The paragraph says presence of the affect is unresolved, then ended "Alexithymia shows that rationality does not guarantee accurate self-classification."
   - After: "At most, alexithymia shows ...".
6. **Coiner: the Toronto Alexithymia Scale was credited to its 1994 revision.**
   - Bagby, Parker & Taylor 1994 created the twenty-item TAS. The original 26-item TAS is Taylor, Ryan & Bagby 1985.
   - After: "the self-report twenty-item Toronto Alexithymia Scale (Bagby, Parker & Taylor 1994)", at +1 word and with no new reference.
7. **Peacocke attribution strength.**
   - Before: Peacocke "derives the impossibility from" concept possession.
   - Speaks's notes say Peacocke "suggests that we can answer it via a theory of the nature of possession of the concept of belief" and "promises an explanation".
   - After: "explains the impossibility through", which is Speaks's own register.
8. **Parrott's stance upgraded.**
   - "Parrott accepts the thesis" at L105 against "tends to agree" at L56, the source wording on Parrott p. 6, verified.
   - After: "Parrott inclines to the thesis".
9. **"Only Shoemaker's constitutive explanation adds" read as an absence claim** about rival explanations such as Peacocke's.
   - After: "Shoemaker's constitutive explanation, not the thesis, adds", which is the contrast the paragraph intends.
10. **"the dilemma for all rationalist accounts".**
    - SEP §3.6 (verified) says "Rationalist accounts face two related challenges" and "The success of rationalist accounts ... depends on". It has no universal quantifier.
    - "all" was removed.
11. **Bidirectional paragraph misattributed one clause to the tenets.**
    - "confined to unimpaired systems" is the Anton article's restriction (Anton L46, L113), not tenets.md. tenets.md L101 supplies the "difficulty, not refutation" grade.
    - After: "where the tenets and the Anton article place it".
12. **Blindsight paragraph presented the Map's application as Shoemaker's.**
    - Shoemaker lists blindsight at p. 225 against Cartesianism, but the p. 231 reclassification is argued for a hypothetical case.
    - After: "His perceptual-experience move would absorb it".
13. **Redundant, slightly overstated sentence cut (−18 words).**
    - Cut: "The Map's Anton article meets the same question for Chalmers's clause and answers it with markers independent of the error."
    - It repeated L85 and L99. Anton L84 itself says "mostly it can", not that it answers the question.
    - The next sentence's "it" was then repointed to "the issue" to avoid a stranded pronoun.

### Checks Passed

- **Author-stance firewall (check 2).** Shoemaker is enlisted for the Map nowhere. L37 and L113 firewall him explicitly: "rejects Cartesian dualism"; "lends no support to the subject the Map posits, to its dualism, or to the near-incorrigibility". The p. 24 sentence was read to its end.
- **Forbidden words (check 3).** A grep for `refut|counterexample|counter-example|tests? shoemaker` finds:
  - L37 "supplies no counterexample", the allowed use;
  - L87 "counter-evidence", in "shields the thesis from clinical counter-evidence", a structural claim that names no case as a refutation.

  There is no "refute" and no "tests Shoemaker".
- **Five-condition test labelled (check 4).** L37 says "that the Map draws from Shoemaker's texts". L68 says "which the Map draws from Shoemaker's texts; he does not list them."
- **Attribution strength (check 5).** Each is now at the strength its source supports:
  - Kind: "On the evidence of her abstract"; matches the OpenAlex abstract.
  - Kimble: "also known here by abstract"; matches the Hrčak abstract.
  - Gertler 2011: "as her own encyclopedia entry reports"; SEP verbatim.
  - Peacocke: "as Jeff Speaks's teaching notes report him"; Speaks verbatim, see issue 7.
- **DID (check 6).** There is no dedicated DID page. The live DID host is [metacognitive-access-versus-retention](/concepts/metacognitive-access-versus-retention/), plus [clinical-dissociation-as-systematic-evidence](/topics/clinical-dissociation-as-systematic-evidence/); the old `dissociative-states-as-intact-substrate-interface-evidence` is archived.
  - The stability notes of [deep-review-2026-10-09-metacognitive-access-versus-retention](/reviews/deep-review-2026-10-09-metacognitive-access-versus-retention/) require two things. The transfer claim stays scoped to feigning-resistant tests. The Beker 2024 → Donath 2025 → Beker 2025 dispute stays open.
  - The page's "perform like healthy controls on feigning-resistant tests (Huntjens et al. 2003), though the meta-analytic picture is disputed" complies on both points.
  - Huntjens 2003 is interference-paradigm evidence, which Donath #2 classes as feigning-resistant (per that review, L40).
- **Presentation rule (calibration).** The rule is attributed to [evidential-status-discipline](/project/evidential-status-discipline/), and it is there (L270, "presentation is not certification"). The page adds no new row, matching the research note §certification L333–346.
- **Epiphenomenalism.** It is never conceded. L119 reads: "does not show experience to be causally idle".
- **Label leakage.** None found. A grep for the forbidden editor labels, "load-bearing" and "This is not" returns zero.

### Counterarguments Considered

- **Popper's ghost:** the thesis is shielded from clinical refutation, so is it empirically idle? The page already concedes this in the blindsight paragraph and in "What the record shows". Its open question, whether "rational" can be specified independently, is the honest residue. No change.
- **Churchland:** the folk categories that Shoemaker's thesis presupposes may not survive. This is bedrock. The page's Dualism verdict, compatible with physicalism either way, does not depend on it.
- **Dennett:** the debate is entirely about report systems. The page grants it ("the monitoring mechanism is a physical detector").
- **Tegmark, Deutsch:** not engaged. The page says Minimal Quantum Interaction and No Many Worlds are not engaged.
- **Nagarjuna:** "the subject the Map posits" is denied any support from Shoemaker. No overreach.

### Reasoning-Mode Classification (editor-internal)

- Shoemaker's reclassification at p. 231: Mode Two. The move is principled only if "in the sense we do" can be specified without mentioning access. That is a standard Shoemaker's own anti-circularity commitments endorse.
- Shoemaker on DID: Mode One. His own agent/agnostic dilemma is applied, and both horns are drawn from his texts.
- Shoemaker's p. 231 reclassification against the Map's phenomenal states without report: Mode Three. It is honestly recorded as a framework-boundary tension, with "the clinical data settle it for neither side".
- Parsimony (Occam paragraph): Mode Three, applied symmetrically.

## Citation Ledger (§2.4)

- Bagby, Parker & Taylor 1994 (TAS-20, *J Psychosom Res* 38(1):23–32, doi 10.1016/0022-3999(94)90005-1): real-correct (Crossref). Coiner wording fixed in the body (issue 6).
- Chalmers 1995 ("Absent qualia, fading qualia, dancing qualia", in Metzinger ed., *Conscious Experience*, Imprint Academic): real-correct (consc.net header). Quotes verbatim: "whose cognitive mechanisms are unimpaired can be so mistaken"; "Fading Qualia may be logically possible"; "any systematic psychiatric disorder", in a list of impairment markers Joe lacks. "judge that he has all these complex experiences that he in fact lacks" supports the commission gloss.
- Gertler 2011 (*Self-Knowledge*, Routledge, doi 10.4324/9780203835678): real-correct. Crossref online date 2010-11-25; print 2011. Ch. 5 content is carried only at SEP-summary strength.
- Gertler 2021 (SEP "Self-Knowledge", substantive revision Tue Nov 9, 2021): real-correct. These are verbatim:
  - the §3.6 quote;
  - the de dicto/de re summary;
  - "in rational creatures, the causal role defining a mental state are also sufficient for belief that one is in that mental state";
  - the §3.6 heading "Rationalist Accounts".
- Huntjens et al. 2003 (*J Abnorm Psychol* 112(2):290–297, doi 10.1037/0021-843X.112.2.290, PMID 12784839): real-correct. Result direction confirmed: 21 of 31 patients reported complete one-way amnesia, yet "neither recall nor recognition scores of patients were different from those of normal controls". The OpenAlex `mag` id is 1987352305, so the record cannot have been seeded by Map text.
- Kimble 2013 (*Synthesis philosophica* 28(1–2):245–262, hrcak 120145): real-correct. Abstract: "a broad perceptual model of introspection can successfully circumvent the central problems he raises".
- Kind 2003 (*Phil Quarterly* 53(210):39–48, doi 10.1111/1467-9213.00294): real-correct. The OpenAlex abstract (`mag` 2075191886) matches the body's gloss.
- Nichols & Stich 2003 (*Mindreading*, OUP, doi 10.1093/0198236107.001.0001): real-correct. The ch. 4 Crossref record (`.003.0004`) confirms "Reading One's Own Mind", pp. 150–199.
- Parrott 2017 (*Philosophers' Imprint* 17(16):1–22, ORA PDF): real-correct. Four quotes verified in the PDF text:
  - p. 6: "We all lack that kind of access ... none of us are self-blind";
  - p. 6: "I tend to agree with Shoemaker that it is not";
  - p. 1, abstract: "wholly distinct from her beliefs about them";
  - p. 1, abstract: "better placed to explain our fallibility and ignorance".
- Peacocke 1998 (in *Knowing Our Own Minds*, pp. 63–98, doi 10.1093/0199241406.003.0004): real-correct. Crossref OSO date 2000; print 1998. Content is cited only via Speaks and not quoted.
- Schwitzgebel 2024 (SEP "Introspection", substantive revision Thu Apr 25, 2024): real-correct. The "break down entirely ... Nichols and Stich 2003" passage is verbatim (issue 3).
- Shoemaker 1988 (*Phil Perspectives* 2:183ff, doi 10.2307/2214074): real-correct. Crossref gives the first page only; 183–209 is the standard range.
- Shoemaker 1990 (*Phil Perspectives* 4:187ff, doi 10.2307/2214192): real-correct. The open-ended "187ff" is honest; the end page was not checked at the publisher.
- Shoemaker 1994 (PPR 54(2), Lecture I from p. 249, doi 10.2307/2108488; Lecture II from p. 271, doi 10.2307/2108489): real-correct. "Royce lectures" is confirmed by the archive.org catalogue description.
- Shoemaker 1995 (*Phil Studies* 77(2–3):211–228, doi 10.1007/BF00989570): real-correct.
- Shoemaker 1996 (*The First-Person Perspective and Other Essays*, CUP, doi 10.1017/CBO9780511624674): real-correct. Its quotes are verified as listed above.
- Speaks 2004 (McGill course notes, dated "March 16, 2004", nd.edu PDF): real-correct. The Peacocke gloss matches ("Peacocke suggests that we can answer it via a theory of the nature of possession of the concept of belief").
- Southgate & Ocinq-cinq 2026 (Anton; metacognitive access): internal. The author string matches the corpus's 21 existing uses.

**Inline ↔ References.** Every inline cite has an entry and every entry is cited. Speaks is cited by name without a year, which is acceptable for teaching notes. No orphans in either direction, checked on (surname, year) pairs.

**Empirical currency.** The only superlative is "the Map's strongest case" (alexithymia), an internal ranking with no literature claim. There is no "first", "largest" or "to date".

**Named-idea coiners.**
- self-blindness, the broad perceptual model, and core/total realization: Shoemaker, who coined each. Correct.
- The Monitoring Mechanism: Nichols & Stich. Correct.
- TAS: fixed (issue 6).
- "Inner sense", "overflow" and "blindsight": no coiner is credited, and none needs to be.

## Optimistic Analysis Summary

### Strengths Preserved

- **The front-loaded verdict and its guard shape.** The page blocks two errors at once: reading the clinical record as a refutation of first-person access, and recruiting Shoemaker for dualism. Chalmers (property dualist) and Birch (hardline empiricist) would both praise the "same scope that protects the thesis stops the record from confirming it" symmetry.
- **The scope section.** Its four verified quotes (pp. 25, 71, 80, 93) plus Parrott p. 6 make the thesis's permissions explicit, and that disarms the most tempting misreading.
- **The Chalmers comparison.** It distinguishes direction (commission versus omission), modality (plausibility versus conceptual) and object (experience versus attitudes), and identifies the one shared liability, independent markers. This is the page's most original contribution.
- **The "tension, recorded" paragraph.** It names the p. 231 reclassification's conflict with the Map's openness to unreported phenomenal states, and declines to adjudicate it. Nagel (phenomenologist) and McGinn (mysterian) would praise the restraint.
- **The alexithymia measurement point.** A self-knowledge deficit measured by self-report is an honest methodological caveat most treatments omit.
- **The Bidirectional paragraph.** Shoemaker's account gives the correlation reply a mechanism for attitudes, but nothing about experience; the paragraph concedes no epiphenomenalism. Stapp (quantum mind) and Kane (libertarian) would find nothing given away.

### Enhancements Made

None beyond the fixes. The page is above soft, so no expansion was made.

### Expansion Opportunities (not taken; page above soft)

- Doyle (2024) on alienated belief is the likeliest bridge to DID's report profile. It is unread, so it stays a research lead.
- Frith & Happé (1999) on autism as impaired self-reflection is a candidate pressure case the Map does not hold, and it conflicts with Nichols & Stich's intact-monitoring reading. It is held in the research note's gaps.

### Cross-links Added

None. The existing links cover the wing.

## Host-Side Findings (not edited; reported only)

- The four integration sentences are consistent with this page's verdict. None says "Anton tests Shoemaker" or calls a case a counterexample.
  - `topics/anton-syndrome-and-the-sincere-report-of-seeing` L84
  - `voids/blindspot-void` L57
  - `concepts/metacognitive-access-versus-retention` L130
  - `concepts/introspection` L125
- `topics/clinical-dissociation-as-systematic-evidence` L74 and L82 still over-read Marsh et al. 2021: "objective tests show transfer (Marsh et al., below)"; "only a trend toward loss on free recall". This is already tracked: the NEEDS-HUMAN length-budget item (todo ~L1541) has the 2026-10-21 driver add-on, and the split-brain task records it as a sibling locus. Not a new finding.

## Remaining Items

None for this page.

## Stability Notes

- **Bedrock, not defects.** Physicalist personas will say both live accounts of self-blindness are physicalist. The page grants this; it is its Dualism verdict, compatible either way. Do not re-flag it.
- **Whether a self-blind creature is possible is contested** (Kind, Gertler, Kimble against; Parrott inclines to impossibility). The page reports the contest. It must not be pushed to either verdict.
- **Calibration to hold.**
  - The clinical cases "fall outside" the thesis, with at least one failed condition each and most failing two or more. They are not counterexamples, and the record neither confirms nor refutes the thesis.
  - Do not restore "each ... at least two". Anton's C4 is "usually", and DID's C5 is "contested".
- **Shoemaker firewall.** He is a functionalist who holds that "there are lots of good reasons for rejecting Cartesian dualism" (p. 24; the sentence was read to its end). Never enlist him for the subject, the Map's dualism, or Layer 1.
- **Attribution floors.** Do not raise any of these beyond the source tier:
  - Kind and Kimble: abstract strength.
  - Gertler 2011 ch. 5: via her SEP entry.
  - Peacocke: via Speaks, unquoted.
  - Parrott: "tends to agree" / "inclines to".
- **Quotes.** Every Shoemaker span on the page is now grep-verified against the 1996 OCR (archive.org FTS, 2026-10-23). The page locators rest on the 2026-10-10 Google Books snippets, except p. 224, which is confirmed by an inline folio. A future review should not re-litigate the wording. Re-verifying the pages is optional, since the Google Books search-within endpoint was down this pass.
- **DID wording.** Keep "feigning-resistant tests" and "the meta-analytic picture is disputed", per the metacognitive page's stability notes.