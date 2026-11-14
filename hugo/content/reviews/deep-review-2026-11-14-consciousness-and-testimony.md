---
ai_contribution: 100
ai_generated_date: 2026-11-14
ai_modified: 2026-11-14 17:41:44+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-14
date: &id001 2026-11-14
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-14 17:41:44+00:00
modified: *id001
related_articles: []
title: Deep Review - Consciousness and Testimony
topics: []
---

**Date**: 2026-11-14
**Article**: [Consciousness and Testimony](/topics/consciousness-and-testimony/)
**Previous review**: [2026-07-18](/reviews/deep-review-2026-07-18-consciousness-and-testimony/)

This is the **eighth** deep review. The article itself changed once since the 07-18 pass: commit `41be63f07` (2026-09-26) piped L75 "default openness" to [phenomenology-of-trust](/topics/phenomenology-of-trust/), a zero-word cosmetic edit. The defects found this pass come from two other sources. Three pages the article paraphrases moved after it was last reviewed, and the References ledger certified by the 06-26 and 07-18 reviews was wrong.

## Trigger Assessment

- Own changes since 07-18: one cosmetic piped wikilink. No argument or citation change.
- What moved underneath it:
  1. `topics/phenomenal-authority-and-first-person-evidence` (commit `531492b3b`, 2026-11-09) scoped self-presentation to "in clear cases". The Map's position there now reads "fallible judgement about presentation incorrigible in clear cases". The same page's acquaintance paragraph says "Apparent infallibilism dissolves once we distinguish *acquaintance* from *judgement*". This article's L87 still glossed that page as "direct phenomenal presentation (infallible at the level of bare awareness)". The repair had not reached this dependent.
  2. The positions register now scopes self-stultification. [P-MC1](/positions/arguments-for-mental-causation/#p-mc1) says it "decisively burdens bare-correlation epiphenomenalism; the phenomenal-concept version survives by relocating the dispute". [P-MC2](/positions/arguments-for-mental-causation/#p-mc2) (updated 2026-10-08) says the argument establishes an existential claim, not Tenet 3's universal one. `concepts/epiphenomenalism` L96/L98 uses the same bare-correlation scope. Both postdate the 07-18 review. The L145 opener "Bidirectional Interaction is presupposed by the very act of giving testimony" and the unscoped "If consciousness were epiphenomenal, testimony about it would be coincidental" claimed more than that accounting allows. They also claimed more than the paragraph's own conclusion ("genuinely part company rather than refuting supervenience on its own terms").
- The ledger certified by earlier passes was wrong (next section).

## Pessimistic Analysis Summary

### Critical Issues Found

- **Four orphan References entries, falsely certified "no orphans" twice.** Chalmers 1996, Coady 1992, Lackey 2008 and Lackey & Sosa 2006 have had **zero** body mentions since the 2026-02-21 coalesce (`git show ceb020202c` confirms none was cited inline even then). The 06-26 review said "every References entry is cited inline (Hume/Reid via the reductionist/anti-reductionist camps, all others by name)". The 07-18 review carried that forward as "no orphans either direction". Both claims were false for four entries. Resolution:
  - Chalmers 1996 is now cited at the zombie mention (L55), the work where the zombie argument is developed.
  - Coady 1992 is now cited beside Reid as the modern anti-reductionist. SEP "Epistemological Problems of Testimony" lists "Coady (1992, 1994)" among non-reductionists.
  - Lackey 2008 is now cited in a new 14-word sentence: "Hybrid views combine the two, requiring hearer-side reasons and a reliable speaker (Lackey 2008)." The sentence also corrects the bare two-camp dichotomy. SEP: "some epistemologists reject both Reductionism and Non-Reductionism in favor of various hybrid views. … See, e.g., Lackey (2008)". Faulkner's *Mind* review (2009, doi 10.1093/mind/fzp036; raw PDF text extracted with pdftotext and grepped) gives her "dualism" as "the audience satisfying an 'audience condition' and having reasons for belief, and the speaker satisfying a 'speaker condition' and being a reliable reporter". The article avoids her label "dualism" so it is not confused with the Map's.
  - Lackey & Sosa 2006 was **removed**. It is an anthology the body never drew on, and the topics page is length-bound. The skill allows "cited inline (or removed)".
- **L87 stale Map-internal gloss (dropped qualifier).** "(infallible at the level of bare awareness)" became "(incorrigible in clear cases)", matching the linked page's current Map-position wording (−3 words). A corpus grep found no other live instance of the phrase.
- **L87 overclaim against the article's own cited source.** "no third party is better positioned to correct it" became "third parties can correct it only indirectly" (−2). Schwitzgebel 2008, cited three sentences earlier, shows introspective error largely through experimenter-side tests, which correct subjects' reports. The paragraph itself also notes clinicians weighing assessment against self-report. The absolute claim contradicted both. The revision keeps the asymmetry the paragraph needs, since correction comes only through indirect evidence and never through access to the experience.
- **L145 calibration (possibility/probability slippage, tenet-accepting test).** "is presupposed by the very act" became "draws support from the very act" (0 words), consistent with the section frame "The Map's tenets find natural support". "If consciousness were epiphenomenal" became "If consciousness were a bare epiphenomenal correlate" (+3), the [P-MC1](/positions/arguments-for-mental-causation/#p-mc1) scope. This is not a re-run of the 06-26 Counterargument B, which added the physicalist common-cause engagement and is preserved verbatim. The fix aligns the paragraph's opener with the accounting the register installed after that review.
- **Description overclaim (navigation surface).** "The felt dimension … reveals consciousness as constitutive of knowledge" asserted as revealed what the body, since the 06-26 refine, holds as "a *framework commitment* rather than an established result". The new description says "The Map holds that felt assessment of the speaker is constitutive of testimony — a framework commitment that constrains materialism without settling dualism", which matches the lead's constrain-not-settle register. The description is frontmatter, so analyze_length is unaffected.

### Medium / Low Issues Found

- **L59 misquotation of the article's own L57 (Map-internal quotation).** The quoted string "checked only against further reports, each presupposing the phenomenon at issue" does not occur in L57, which reads "can only be checked against further reports — one's own or others' — each presupposing the very phenomenon at issue". The quotation marks were removed so the clause reads as a paraphrase (0 words). No other Map-internal quotation appears in the body.
- **L77 unsupported empirical gesture (deferred).** "Research on social cognition supports the observation that much credibility assessment may operate below conscious awareness" carries no citation. Its link target [consciousness-and-social-understanding](/topics/consciousness-and-social-understanding/) has never discussed credibility assessment (`git log -S "credib"` and `-S "subpersonal"` on that page return nothing). The claim is hedged and concedes ground to the opponent, so it is low severity. A real anchor exists (e.g. Willis & Todorov 2006 on 100-ms trustworthiness impressions), but a cite plus a References entry costs about 25 words against 9 words of headroom. Deferred.

### Publisher-of-Record Citation Web-Verify (per-cite ledger)

- Chalmers 1996 (*The Conscious Mind*, OUP): real-correct. Now cited inline.
- Churchland, P. M. 1981 (*J. Phil.* 78(2), 67–90): real-correct. Live-verified 06-26 at PDC. References block entry byte-identical since.
- Coady 1992 (*Testimony: A Philosophical Study*, Oxford: Clarendon Press, ISBN 0-19-824786-9): real-correct. Library catalogue records confirm. Stance confirmed as non-reductionist via SEP. Now cited inline.
- Dennett 2003 ("Who's On First? Heterophenomenology Explained", *JCS* 10(9–10), 19–30): real-correct. Confirmed this pass at PhilArchive (DENWOF-2). A Cogprints record giving "10–30" is the outlier.
- Hume 1748 (*Enquiry*, §X "Of Miracles"): real-correct, conventional dating (the 1748 first edition was titled *Philosophical Essays Concerning Human Understanding*, retitled 1758). No change.
- Jackson 1982 (*Phil. Q.* 32(127), 127–136): real-correct. Live-verified 06-26 at Oxford Academic.
- Lackey 2008 (*Learning from Words*, OUP): real-correct. Table of contents includes "A Critique of Reductionism and Non-Reductionism" and "Dualism in the Epistemology of Testimony". Now cited inline (hybrid sentence).
- Lackey & Sosa 2006 (*The Epistemology of Testimony*, OUP): real, but an orphan. **Removed** (see Critical).
- Reid 1764 (*Inquiry into the Human Mind*): real-correct.
- Schwitzgebel 2008 (*Phil. Review* 117(2), 245–273): real-correct. "Naive" qualifier preserved.
- Inline ↔ References: verified this pass by body-range `grep -c` per surname (not by carrying a prior claim). Chalmers 1, Coady 1, Lackey 1, Sosa 0 in body. Every remaining References entry has a body mention, and every inline `Author YYYY` has an entry.
- Result-direction leg: no empirically cited paper with a directional result. Schwitzgebel is cited for unreliability, which is the paper's thesis.
- Cited-author-stance leg: Lackey is cited only for the shape of the debate, not in support of a Map reading. Her statement view runs *against* the article (see Remaining Items). Dennett and Churchland are cited as opponents. Chalmers is cited only for the zombie concept.
- Empirical-record currency: `find_superlative_claims` returns empty.
- No external quotation appears in the body, so there were no raw-source greps of quotations to run.

### Named-Opponent Engagement (reasoning mode, editor-internal)

- Dennett (heterophenomenology): Mode Two. Unchanged.
- Churchland / eliminativism: Mode Two, with the debt named. Unchanged.
- Physicalist common-cause (L145): Mode Three, now with a scoped opener. The bare-correlation charge is aimed at the version it binds, and the phenomenal-concept or common-cause escape is honestly marked as the parting point.
- MWI: Mode Three. Unchanged.
- Label leakage scan (Mode One/Two/Three, Engagement classification, Evidential status, direct-refutation, unsupported-jump, bedrock-perimeter): none. No "This is not X. It is Y."; no "load-bearing".

## Optimistic Analysis Summary

### Strengths Preserved

All of the 06-26 list is preserved: the epistemic circle with the parity-with-perception defence, the thermometer analogy, "propositionally correct but phenomenally hollow", the eliminativist bind as challenge-not-refutation, transparency-to-opacity suspicion, the farmer/algorithm contrast, the knowledge-argument stratification, and the conditional LLM paragraph.

### Enhancements Made

- The two-camp framing of testimony epistemology now acknowledges hybrid views. This matters because the next paragraph argues that "the phenomenology appears to favour the anti-reductionist picture", and Lackey's audience condition (positive reasons) is the in-field position that default openness has to beat.
- The description is now calibrated to the body.

### Cross-links

No new links. All 28 unique wikilink targets resolve to live files (scripted check). All five tenet block anchors exist in `tenets.md`.

## Word Count

analyze_length 3,989 → **3,990** (+1; topics hard 4,000, gate `>=`; headroom 9). Additions: Chalmers +2, Coady +2, hybrid sentence +14, bare-correlate scope +3. Cuts: L87 −5, Lackey & Sosa entry −15.

## Remaining Items

- **Lackey's statement view is unengaged.** Faulkner glosses it: "we should not … be interested in the sincerity and competence of a speaker as believer as such, but should focus on the competence of a speaker as a producer of reliable testimony". It is the strongest in-field challenge to L65 (assessing "the consciousness behind it: … are they sincere") and to the LLM paragraph's claim that felt assessment constitutes the practice. Now that Lackey 2008 is cited, it is worth a paragraph. Engaging it needs about 60–80 words, which is not affordable at 9 words of headroom without a matching condense. Queued as a P3 refine-draft.
- The L77 citation gap (above).

## Stability Notes

- All prior stability notes stand. Do not re-flag: the Dennett parting point, MWI indexicality, the eliminativist deflated-testimony reply, Buddhist no-self, and hedge density as style.
- **Ledger lesson.** A carried-forward "no orphans" line is not a check. The 06-26 claim was a surname-level assertion that was never run, and it survived one carry-forward. Future passes should re-run the per-surname body count.
- The L145 changes scope the opener only. The common-cause engagement (06-26) is intact and should not be expanded or re-litigated. If the Tenet 3 quantifier decision (open NEEDS-HUMAN) lands, re-check "draws support from" against it.
- Length: 3,990/4,000. Future passes must stay length-neutral. Hub accretion into Further Reading remains the most likely breach.