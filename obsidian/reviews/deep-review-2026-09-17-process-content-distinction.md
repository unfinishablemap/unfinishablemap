---
title: "Deep Review - The Process/Content Distinction"
created: 2026-09-17
modified: 2026-09-17
human_modified: null
ai_modified: 2026-09-17T07:06:55+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author: null
ai_system: claude-opus-5
ai_generated_date: 2026-09-17
last_curated: null
---

**Date**: 2026-09-17
**Article**: [[process-content-distinction|The Process/Content Distinction]]
**Previous review**: [[deep-review-2026-07-25-process-content-distinction|2026-07-25]]

## Why This Article Re-Qualified

The only change since the 2026-07-25 review was refine-draft commit 9555567dd6 (2026-08-08), which found that the Nisbett & Wilson three-part unawareness "quote" was a bracketed paraphrase occurring 0 times in the paper, even though the 2026-07-10 review had marked it "verified verbatim". Because a prior review had certified a quote that was not in the source, this pass treated every earlier quote and figure certification as unverified. It checked them all by grepping the raw text of the 29-page paper (pdftotext, NFKC-normalised, line-break hyphenation removed).

## Pessimistic Analysis Summary

### Quote / figure fidelity (raw-source grep of Nisbett & Wilson 1977)

- "people often cannot report accurately on the effects of particular stimuli on higher order, inference-based responses": **verbatim** (p. 233, conclusion 1).
- The abstract's "(a)... (b)... and (c)..." sentence as installed on 08-08: **verbatim**.
- **CRITICAL: misreading of that sentence.** The 08-08 fix glossed the list as "cumulative... conjoined rather than offered as alternatives". The paper says each failure happens *sometimes*, and its body text is explicitly distributive ("sometimes... sometimes... and sometimes"). The gloss made the claim stronger than the source. **Fixed**: the article now says the three are separate forms of failure and quotes the distributive body sentence.
- **CRITICAL: stocking-study figures not in the cited source.** "approximately 40%... 12%... roughly three-to-one" does not appear in N&W 1977 (0 hits for 40% or 12%). The paper says "by a factor of almost four to one". The 07-10 review had called the 12/17/31/40 split "canonical" from memory. Those figures probably come from Wilson & Nisbett 1978 (*Social Psychology* 41(2):118-131, DOI 10.2307/3033572), which is not in the reference list and was not checked. **Fixed**: the article now uses N&W's own "almost four to one" and adds the verified "virtually all subjects denied it".
- **CRITICAL: the reasons attributed to subjects were invented.** The article gave subjects' explanations as "knit, sheerness, elasticity, workmanship". The paper has only "The knit, sheerness, and weave of nylon stockings seem representative of reasons" as an illustration of representativeness, and "elasticity" and "workmanship" appear nowhere. "Shoppers" should be "passersby". **Fixed**: the passage now says only that subjects gave quality-based reasons, without the invented list.
- Added a verbatim anchor for the distinction's name: "based not on access to process but access to content" (verified in the raw text).

### Citation ledger (§2.4)

- Nisbett & Wilson (1977), *Psychological Review* 84(3):231-259: real-correct (29-page PDF retrieved).
- Bem (1972), Self-perception theory, *Adv. Exp. Soc. Psych.* 6:1-62: real-correct (also cited in N&W's reference list). **Framing fix**: "the post-decision rationalisation literature that Bem developed" was wrong on two counts. The paradigm described is induced compliance, and Bem reinterpreted dissonance findings rather than developing that literature. Reworded.
- Block (2007), BBS 30(5-6):481-499: real-correct (Crossref). **Framing fix**: "Block's phenomenal overflow *research*" became "overflow *argument*, drawing on Sperling-style partial-report experiments". Block did not run the experiments.
- Gazzaniga (1985), *The Social Brain*, Basic Books: real-correct (carried over from 07-10; no new claim depends on it).
- Lush (2020), *Collabra: Psychology* 6(1):22, solo author: real-correct (Crossref). **Dropped-qualifier fix**: the article said reports "reflect demand characteristics". The abstract says the illusion "may be, partially or entirely, a suggestion effect". Now quoted. **Attribution fix**: "trait phenomenal-control capacity" and "mirror-touch" findings are not in Lush 2020. They come from the separate paper below, which was added.
- Lush, Botan, Scott, Seth, Ward & Dienes (2020), Trait phenomenological control predicts experience of mirror synaesthesia and the rubber hand illusion, *Nature Communications* 11:4853: **added**. Verified via Crossref DOI 10.1038/s41467-020-18591-6.
- Petitmengin (2006): **real-wrong-metadata**. Issue was 5(3), corrected to 5(3-4). The missing subtitle "An interview method for the science of consciousness" was restored (Crossref).
- Schwitzgebel (2011), *Perplexities of Consciousness*, MIT Press: real-correct (carried over).
- Internal Map cites (Southgate & Oquatre-sept / Oquatre-cinq): real-correct (carried over).
- Result-direction leg: Lush 2020 reports that controls are confounded, which is what the article claims. N&W report the position effect and subjects' denial of it, as the article says.
- Cited-author-stance leg: Nisbett & Wilson, Bem, Lush and Block are presented only as sources of empirical and methodological claims. None is presented as endorsing dualism. The existing "materialists and dualists can both endorse the distinction" bullet covers this.
- Superlative-currency sweep: "most famous exhibit" is rhetorical. No empirical-record claim.

### Medium Issues Found
- **Description overclaimed**: "Introspection accesses the content of mental states reliably" contradicted the body ("comparatively more warranted trust", "neither side exempt from error") and ran to about 240 characters. Rewritten to a 159-character comparative form.
- **Evidential-tier calibration in Relation to Site Perspective**: "Content reports earn higher tiers (typically *strongly supported* or *established*...)" sits badly with the article's own Schwitzgebel bullet. A reviewer who accepts the tenets would still flag it. Softened to "can reach the upper tiers when they concern repeatable structural features that converge across subjects and methods."
- **Lead**: "replicated... across... split-brain work" wrongly presented independent, contemporaneous split-brain research as an extension of the N&W paradigm. Reworded as "converges with the independently obtained split-brain findings".
- **Wrong direction reference**: "Microphenomenological gains (below)" pointed back to an earlier bullet. Changed to "(above)".

### Counterarguments Considered
- Heterophenomenology: Mode Three, unchanged. Honest framework-boundary marking.
- Pessimist programme overreach: Mode One touch, unchanged.

## Optimistic Analysis Summary

### Strengths Preserved
- The asymmetric-reliability framing, and the "What the Distinction Actually Claims" and "Does Not Claim" sections, which show evidential restraint (a Hardline Empiricist strength).
- The escalation of exhibits from behavioural, to attitudinal, to neuroanatomical, to phenomenological control.
- The McGinn neutrality bullet and the microphenomenology "line is methodologically negotiable" bullet.

### Enhancements Made
- The distinction's name is now anchored with a verbatim N&W quote.
- The phenomenological-control paragraph now separates the two Lush 2020 papers and states their actual findings.

### Cross-links Added
- None needed. The link set is dense and all targets resolve.

## Word count
2258 → 2436 (concepts soft threshold 2500; status ok)

## Remaining Items
- Wilson & Nisbett (1978) is the likely source of the commonly repeated 12/17/31/40% split. It was not verified here. Do not reintroduce percentages without checking that paper directly.

## Stability Notes
- **The quote and figure certifications in the 2026-07-10 review are withdrawn.** It marked a paraphrase "verbatim" and an out-of-source percentage split "canonical". The raw-text grep on 2026-09-17 is the record of what is actually in N&W 1977.
- Do not re-add "conjoined/cumulative" readings of the (a)/(b)/(c) list. The source is distributive.
- Keep "almost four to one" (N&W's own wording) unless the 1978 paper is added and verified.
- Carry forward: Lush 2020 Collabra is solo-authored. The multi-author trait paper is a separate Nature Communications article.
- The physicalist / heterophenomenological disagreement about what the content data supports remains a bedrock framework-boundary disagreement.
