---
ai_contribution: 100
ai_generated_date: 2026-11-02
ai_modified: 2026-11-02 21:29:23+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-02
date: &id001 2026-11-02
description: 'Third-pass deep review: audit of the never-reviewed 10-25 Carruthers/Hurlburt
  sentence, a false Map-internal pointer present since creation, and citation currency.'
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-02 21:29:23+00:00
modified: *id001
related_articles: []
title: Deep Review - Inner Speech and Anendophasia
topics: []
---

**Date**: 2026-11-02
**Article**: [Inner Speech and Anendophasia](/topics/inner-speech-and-anendophasia/)
**Previous review**: [2026-09-02](/reviews/deep-review-2026-09-02-inner-speech-and-anendophasia/)
**Mode**: Third pass on an article the 09-02 review called converged. Selection: the selector's #1 (`affective-tone-divergence-across-meditative-traditions`) was edited today and was skipped; this was #2 (score 76). Git check against the 09-02 claims: the only body delta since then is commit `82c32b5761` (2026-10-25 expand-topic for `concepts/interpretive-sensory-access-theory`). It added one sentence at L67 carrying three quoted spans, plus References entries for Carruthers (2009) and Hurlburt (2009). No review had read that sentence. The 09-02 claim "the body contains no verbatim quoted spans" is now out of date because of it.

## Pessimistic Analysis Summary

### Critical Issues Found

- **False Map-internal pointer (L107 at review start, present since creation in `db4db60ee0`)**: "…its phenomenal character is not fixed by its linguistic content — a point that supports the use-relation framing and is developed in [source-attribution-void](/voids/source-attribution-void/)." The void page has never contained the string "speech" (`git log -S speech` on that file: zero commits). It also has no mention of hallucination, "alien" or "self-produced". The claimed development does not exist and never did, and both prior reviews passed over it. **Fixed:** `source-attribution-void` is kept as the link for the general concept, now a pipe on "source-attribution failure", which that page does cover (the architectural absence of source tags). The development pointer is retargeted to [thought-insertion](/concepts/thought-insertion/), whose "Clinical Picture" section carries the report this sentence needs: a patient whose own thoughts "might say the same thing 'but the feeling isn't the same'" (Guillot from Allison-Bolger, as that page transcribes it). It also records the inner-speech corollary-discharge findings (Whitford et al. 2017; Jack et al. 2019). I paraphrased the report without quotation marks, because the patient wording sits two transcriptions from the primary record.
- **Same sentence, calibration (fixed with it)**: the opening "Inner speech not recognised as one's own is the *clearest* natural case" was an unsupported superlative, now "a natural case". The factive "The same inner speech can be experienced as self-produced or as alien, so its phenomenal character is not fixed…" is now conditional ("If the same inner speech can be…"). The article's own closing caution says report-level measures "underdetermine the phenomenal facts", so the Map "cannot consistently read a phenomenal conclusion off them when they happen to point the Map's way". A factive phenomenal conclusion drawn from clinical reports broke that rule two paragraphs earlier. A tenet-accepting reviewer would flag it, so it counts as a calibration fix, not bedrock.
- **Position-strength framing (L67, 0 words)**: "Hurlburt's reply *grants* that unsymbolized thinking 'may involve (non-symbolic) sensory aspects'". The source says "I argue that…", and argues it in order to conclude that unsymbolized thinking "poses no threat to mindreading-is-prior". Hurlburt is on Carruthers's side about attitude access ("Descriptive Experience Sampling lends empirical support to the view that access to our own propositional attitudes is interpretative, not introspective"). "Grants" casts him as a reluctant opponent making a concession. That is the framing the ISA research note's guard warned against ("Hurlburt is **not** an opponent of ISA on attitude access"). Now "argues".

### Medium Issues Found

- **Internal ordering (0 words)**: L105 opens "A framework-relative caution belongs at the end", but the L107 paragraph followed it. The source-attribution paragraph now sits before the caution, so the caution really is last. Its throat-clearing opener "One further connection is worth flagging." was cut (−6) to keep the pass under the soft threshold. No review or task installed or guards that phrase (grep of `reviews/` and `todo.md`: zero hits).
- **References entry 16 had no body anchor**: *Philosophy of Language Under Dualism* sat in References and Further Reading but had no body link. I applied the open P3's zero-word pipe at L101 ("illustrate the [two layers of semantic content](/topics/philosophy-of-language-under-dualism/) the Map distinguishes", str.count == 1). The target's L61–L64 list exactly those two layers, functional and phenomenal. **The P3 in `todo.md` ("`topics/inner-speech-and-anendophasia` L101: zero-word pipe…") is now discharged** and can be closed.

### Citation Ledger (§2.4)

Raw Crossref fields, with OpenAlex abstract inverted indexes for quotation greps. Every fetch used `--max-time 30`.

- Alderson-Day & Fernyhough (2015), *Psychological Bulletin* 141(5), 931–965 — real-correct (10.1037/bul0000021)
- Carruthers (2002), *BBS* 25(6), 657–674 — real-correct (10.1017/s0140525x02000122)
- Carruthers (2009), "How we know our own minds…", *BBS* 32(2), 121–138 — real-correct (10.1017/s0140525x09000545). Quote "alleged evidence": 1 hit in the author-written abstract ("Section 8 examines alleged evidence of 'unsymbolized thinking'"). The words are the abstract's summary of §8, not a sentence read in §8. The 10-31 ISA pessimistic review accepted the "(2009, §8)" locator on that basis, and I kept it. The gloss "against his interpretive account" matches Hurlburt's own characterisation ("a potential threat to his mindreading-is-prior position"). The pipe text "interpretive account" avoids naming ISA, which is Carruthers's 2011 label, anachronistically.
- Dennett (1991), *Consciousness Explained*, Little, Brown — real-correct (carried from 09-02 Open Library check; unchanged)
- Heavey & Hurlburt (2008), *Consciousness and Cognition* 17(3), 798–810 — real-correct (10.1016/j.concog.2007.12.006)
- Hinwar & Lambert (2021), *Frontiers in Psychology* 12, 744213 — real-correct (10.3389/fpsyg.2021.744213)
- Hurlburt (2009), "Unsymbolized thinking, sensory awareness, and mindreading", *BBS* 32(2), 149–150 — real-correct (10.1017/s0140525x09000673). Quotes "may involve (non-symbolic) sensory aspects" and "not purely propositional": 1 hit each in the abstract, subject "unsymbolized thinking" in both. Framing fixed as above.
- Hurlburt (2026), *Psychological Science*, online ahead of print — real-correct; **still no volume/issue/page** (Crossref: all absent; issued 2026-01-30). Do not "fix" it to 36(9), which is Lind (2025a)'s.
- Hurlburt & Akhter (2008), *Consciousness and Cognition* 17(4), 1364–1374 — real-correct (10.1016/j.concog.2008.03.021)
- Hurlburt, Heavey & Kelsey (2013), *Consciousness and Cognition* 22(4), 1477–1494 — real-correct (10.1016/j.concog.2013.10.003)
- Lind (2025a), *Psychological Science* 36(9), 765–767 — real-correct (10.1177/09567976251335583)
- Lind (2025b), PsyArXiv — real-correct, **still unpublished** (posted-content 10.31234/osf.io/8u4ct_v1; no journal version found)
- Lupyan & Nedergaard (2025), OSF — real-correct, **still unpublished** (posted-content 10.31219/osf.io/w9gfy_v1; no journal version found)
- Nedergaard & Lupyan (2024), *Psychological Science* 35(7), 780–797 — real-correct (10.1177/09567976241243004)

**Result-direction leg**: the 08-04 review checked every empirical figure against the source abstracts or the Frontiers full text: N = 46/47, the direction of the inner-speech/distress finding, rho = 0.83, the 34/29 group counts, and the one-quarter frequency. Those body lines are byte-identical since then (verified by `git diff d4701faee4 HEAD`), so I carried the check forward rather than re-deriving it.

**Cited-author-stance leg**: Carruthers is a physicalist, cited as an opponent (the constitutive view; the dismissal of unsymbolized thinking). Hurlburt is an empirical methodologist, sided with Carruthers on attitude access and never enlisted for dualism. Dennett is a physicalist opponent. Alderson-Day & Fernyhough are explicitly "compatible both with the Map's position and with the position the Map rejects". Nedergaard, Lupyan and Lind make no metaphysical commitments that the article attributes to them.

**Currency**: `find_superlative_claims` found 0 candidates. **Lead, not a defect**: Lambert, Schelp, Quigley-Tump, Tan, Purdy & Sibley (2026), *Neuropsychologia* 230, 109527 (10.1016/j.neuropsychologia.2026.109527) is the same lab's large-sample follow-up (N = 32,784, NZAVS wave 13). Its OpenAlex abstract reports anauralia and aphantasia prevalence at about 0.8% each and "distinct psychological profiles". It also reports that anauralics show better self-control, while aphantasics show more distress and poorer wellbeing. The article reports only what the 2021 sample showed, so nothing it says is superseded. A future pass could use the 2026 paper for the "Three Names" section's phenomenology-versus-function asymmetry. That is not a fix, and it would need length budget.

**Inline ↔ References**: complete in both directions. Entry 16 is now anchored by the L101 pipe, and entry 15 by the L83 link.

### Map-internal claims re-checked against their targets

- `positions/ai-consciousness-scope` [P-AC4](/positions/ai-consciousness-scope/#p-ac4): "workspace-like functional signatures of access consciousness" observed, phenomenal question left open. The L101 paraphrase matches.
- `concepts/descriptive-experience-sampling`: the "Absence at zero" entry at L86 is still present. The L89 claim matches.
- `apex/phenomenal-variation-within-a-species` L124: "*partly unmatched* performance". The Further Reading annotation matches.
- `topics/consciousness-and-language-interface` L180: "confuses correlation with constitution… neural maturation and social interaction". The L83 claim matches.
- `topics/aphantasia` L45/L96: the task "gets done anyway, by other means", with task-level performance "matched". The L77 claim matches.
- `topics/philosophy-of-language-under-dualism` L61–L64: two layers, functional and phenomenal. The L101 claim matches.
- `voids/source-attribution-void`: **failed** (see Critical). Fixed.

### Counterarguments Considered

The constitutive-question engagement, the two-layer framing and the anendophasia modal calibration were not re-opened, per both prior stability notes. Reasoning mode for the Dennett/Carruthers/Vygotskian engagement remains Mixed: an in-framework burden transfer, with the strongest reply (unconscious linguistic processing) stated, and no refutation claimed. I looked at one possible gap. Carruthers's own 2009 reply to unsymbolized thinking (that the reports are self-interpretation) differs from the unconscious-processing reply L85 names. L67 ("alleged evidence") and challenge 1 (L89) already cover it in substance, and the research note never verified the §8 verdict wording. I added nothing.

## Optimistic Analysis Summary

### Strengths Preserved

All five strengths from 08-04 and 09-02 are intact: the reframing away from the contested existence claim; the coiners' concession at maximum leverage; symmetric scepticism about the article's preferred evidence channel; anauralia kept distinct from anendophasia; four real defeaters. The closing caution now actually closes the article, which strengthens the last of these. The L67 sentence is a real gain from the 10-25 insertion: it puts the sturdier evidence's chief rival reading on the page, and with "argues" it now does so accurately.

### Enhancements Made

- One cross-link added: [thought-insertion](/concepts/thought-insertion/), previously unlinked from this page, the nearest clinical case for the alien-inner-speech point.
- The orphaned self-reference (entry 16) is now anchored.

### Cross-links Added

- [thought-insertion](/concepts/thought-insertion/)
- [philosophy-of-language-under-dualism](/topics/philosophy-of-language-under-dualism/) (body pipe; it was previously in frontmatter, Further Reading and References only)

## Word Count

2990 → 2995 (+5) by `analyze_length`. Topics soft 3000, hard 4000, gate `>=`; status `ok`. The first draft reached 3006 (`soft_warning`). Tightening the pointer sentence (−5) and cutting the L107 opener (−6) brought it to 2995.

## Remaining Items

- **Currency tracking (unchanged)**: Hurlburt (2026) volume/issue; Lupyan & Nedergaard (2025) and Lind (2025b) peer-reviewed publication. None has happened as of this pass.
- **Lead**: Lambert et al. (2026) *Neuropsychologia*, as above. Not queued, because the article is at 2995/3000 soft and no claim is wrong.
- **Operator**: close the P3 "L101: zero-word pipe to `philosophy-of-language-under-dualism`" as done by this review.

## Stability Notes

Carried forward unchanged: do not re-open the constitutive-question argument, the two-layer framing, or the modal calibration; 36(9) belongs to Lind (2025a), not Hurlburt (2026); whether anyone sits at exactly zero inner speech is not the Map's question. New: Hurlburt (2009) is an *ally* of Carruthers on attitude access, so render his sensory-aspects claim as argued, never as conceded. The source-attribution paragraph's phenomenal claim is conditional by design, to match the article's closing caution. Do not restore the factive form. The convergence verdict of 09-02 was premature, because a sentence present since creation pointed at content that never existed. Outbound "developed in X" pointers deserve a target grep on every pass.