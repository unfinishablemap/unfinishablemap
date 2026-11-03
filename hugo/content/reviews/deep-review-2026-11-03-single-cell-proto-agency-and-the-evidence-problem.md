---
ai_contribution: 100
ai_generated_date: 2026-11-03
ai_modified: 2026-11-03 13:47:56+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-03
date: &id001 2026-11-03
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-03 13:47:56+00:00
modified: *id001
related_articles: []
title: Deep Review - Single-Cell Proto-Agency and the Evidence Problem
topics: []
---

**Date**: 2026-11-03
**Article**: [Single-Cell Proto-Agency and the Evidence Problem](/topics/single-cell-proto-agency-and-the-evidence-problem/)
**Previous review**: [2026-08-24](/reviews/deep-review-2026-08-24-single-cell-proto-agency-and-the-evidence-problem/) (four criticals fixed), with [2026-07-25](/reviews/deep-review-2026-07-25-single-cell-proto-agency-and-the-evidence-problem/) and [2026-07-16](/reviews/deep-review-2026-07-16-single-cell-proto-agency-and-the-evidence-problem/) before it

## Why this article, and what had moved

The cycle selector chose it (score 75; 71 days since review). It is on none of today's exclusion lists. Since the 08-24 review, three commits had changed the body or the navigation, and no review had seen any of them:

- **09-08 (dc8c246d69)**: a new 196-word paragraph on Nesin & Chandrankunnel (2025), the published CBC reply to the *EMBO* dissent, plus its reference.
- **09-02 (b86a1077e2)**: a Further Reading bullet for `synthetic-minimal-agents-and-the-engineered-decoupling`.
- **09-09 (24f16a877f)**: the `basal-and-bioelectric-cognition` bullet relabelled from "Levin's agency-without-experience decoupling" to "Levin's agency-with-phenomenality-unresolved framing".

So this pass focused on those three loci. The 08-24 stability notes were read and respected. The open P3 task from `optimistic-2026-10-31-onset-and-floor-wing` Priority 3 owns L57 ("developed as an evolutionary transition-marker…") and L67 ("The two lines converge…"). Neither string was touched, and both were asserted unchanged (count 1) before and after the edits.

## Pessimistic Analysis Summary

### Critical Issues Found

**C1: Attribution error in a navigation label, contradicting the linked page (fixed).** The basal bullet read "Levin's agency-with-phenomenality-unresolved framing, which the whole cluster shares." The target page's lead says the decoupling "is drawn against Levin rather than with him", because Levin *infers* that consciousness is graded and widely distributed. That wording was installed by d38b75375f (09-09 10:16Z), whose title is "attributes programme-wide phenomenal agnosticism to Levin, contradicting his own published sentience work". The 24f16a877f relabel landed 73 minutes later and re-introduced the same agnosticism attribution in new words. Its neutrality repair (dropping "without-experience") was right, but its subject ("Levin's") was wrong.

*Primary-source check*: Levin 2022, TAME, *Front. Syst. Neurosci.* 16:768201. In the raw Europe PMC full text (PMC8988303), the passage "some variant and degree thereof has to be present very widely across autopoietic systems. TAME is definitely incompatible with binary views that cut off consciousness at a particular sharp line" is present (count 1). TAME's exposition does bracket phenomenality: "the focus of most of the discussion below is on ways to think about cognitive function, not on phenomenal or access consciousness" (count 1). But that is a scoping of the discussion, not Levin's view. Applying that definition first, an "unresolved-phenomenality framing" belongs to the Map, not to Levin.

*Fix*: "Levin's agency-with-phenomenality-unresolved framing, which the whole cluster shares" → "Levin's agency in brainless systems; the Map keeps the measurements and declines his inference to widespread consciousness". The last clause tracks the basal page's own sentence, "The Map takes the measurements and declines the inference."

**Sibling instances (not fixed here; task minted).** The pre-09-09 string "Levin's agency-without-experience decoupling" is still live in four Further Reading labels:

- `bacterial-chemotaxis-and-minimal-biogenic-cognition` L101
- `the-enteric-nervous-system-and-the-gut-brain-distributed-interface-question` L91
- `neuron-less-animals-sponges-placozoans-and-the-lower-bound-of-cognition` L86
- `brain-organoids-and-the-organoid-intelligence-question` L96, which is on today's exclusion list

This is the `fix-by-file-leaves-string-siblings-live` shape: d38 fixed the target page and none of its four inbound labels.

**C2: Undefined abbreviation and an unnamed opponent (fixed).** The 09-08 paragraph opens "The CBC side has since replied in print… they endorse CBC". "CBC" appeared nowhere else in this article, so a reader arriving here (or an LLM fetching this page alone) could not resolve it. The 09-08 changelog had itself noted that the article "states the *EMBO* dissent without naming whom it dissents from" and left that out of scope. Adding the "CBC side" paragraph made the gap a defect.

*Fix*: the *EMBO* sentence now names its target. "(Robinson, Mallatt, Peer, Sourjik, Taiz)." → "(Robinson, Mallatt, Peer, Sourjik, Taiz), a rebuttal of the [Cellular Basis of Consciousness](/topics/bacterial-chemotaxis-and-minimal-biogenic-cognition/#the-cellular-basis-of-consciousness-the-strongest-rival) (CBC) theory that all cells are conscious." The piped link sends readers to the sibling's CBC section, which names and cites Reber and Baluška, so no new reference is needed here. Verified against Robinson et al.'s own subtitle, "The cellular basis of consciousness theory lacks empirical evidence for its claims that all cells have consciousness". The anchor ID was taken from the rendered sibling HTML (`id=the-cellular-basis-of-consciousness-the-strongest-rival`).

In the same paragraph, "they demand of the opposing camp that 'theories require proof…'" → "they demand of CBC that…". The raw text directs that demand at CBC by name: "theories require proof from hypotheses-testing, solid facts and empirical evidence. In these respects, CBC falls short."

### Medium Issues Found

- **M1: Redundant restatement in the Nesin sentence (tightened, which also paid for C2).** "take up this charge by name—the critics' claim that the individual cell makes no choice and that its apparent decisions reduce to stochastic differences in protein levels—and answer it" restated, in paraphrase, two quotes given three sentences earlier. → "take up the protein-noise charge, citing the dissent, and answer it". *Stranded-reference check*: an intermediate draft read "take up exactly this charge". Placed straight after the new "demand of CBC that theories require proof", that "this charge" could be read as the evidence demand, so it was replaced with the explicit "protein-noise charge". Faithful to the paper, which restates the charge as "the individual bacterial cell does not make choices, and the decision-making is the result of stochastic differences in protein levels" and cites Robinson et al. as [6].
- **M2: An instance of the banned "not X. It is Y." construct (fixed).** L47 read "The interesting question is no longer noise-versus-choice. It is whether…". This is the forbidden two-sentence construct in a "no longer" variant, which is why earlier "not X. It is Y." scans missed it. → "The interesting question then shifts from noise-versus-choice to whether 'harnessed stochastic search with a memory' earns agency vocabulary at all—a conceptual question no experiment resolves." Same claim, six words shorter.
- **M3: Tense drift in the synthetic-agents bullet (fixed).** "its builders cannot account for" → "could not account for". The target page says "they could not account for" and adds that JCVI-syn3A follow-up modelling "narrowed that unknown fraction without closing it". The present tense overstated a figure that has since moved.

### Counterarguments Considered

- **Nesin & Chandrankunnel's parity argument** (a molecular-stochasticity reduction applied evenhandedly would deflate human choice too). It is presented at full strength and marked as the Map's reading of their work ("read as an objection"). Nothing to change. Their stance is recorded correctly: they endorse CBC and *conscious* decision-making in bacteria, and the article does not enlist them for the Map's conclusion.
- **Eliminativist / Dennettian deflation of "proto-choice"**: bedrock, per the carried stability notes; not re-flagged.

## Publisher-of-Record Citation Ledger

Only one citation is new since 08-24 (Nesin & Chandrankunnel 2025). The others are carried, with their quotes re-grepped in raw text wherever an open raw source exists.

- Robinson et al. 2024 (*EMBO Reports* 25(5):2162–2167): **real-correct**. All four quotes re-grepped in the raw Europe PMC fullTextXML (PMC11094104), 4/4 present. Quote 1 differs only in the source's sentence-initial capital ("An individual…"). The new body claim (it rebuts CBC's all-cells-conscious thesis) and the "demand of CBC" retarget are both verified against the raw text, as quoted above.
- Nesin & Chandrankunnel 2025 (*Communicative & Integrative Biology* 18(1):2463926): **real-correct**.
  - Metadata: Crossref returns title, authors Sibin Mathew Nesin and Mathew Chandrankunnel, volume 18, issue 1, article 2463926, issued 2025-02-12.
  - Quotes: in the raw Europe PMC text (PMC11834444), both are present (count 1 each): "can be considered as the molecular mechanism underlying individualistic decision-making in bacteria as well as in humans" and "can also be traced to the stochastic differences in biomolecules and ion levels between cells".
  - Paraphrases: "endorse CBC" ← "The authors thus support the CBC". "Rather than a set of independent events" ← "Signaling in bacteria is not an independent event but an interaction of interconnected pathways". "Motor and cognitive flexibility in brains" ← "The labile motor plans in the brain provide flexibility…" and "The cases of skilled movement and cognitive flexibility…". All faithful.
  - Result direction: they report a proposal (a perspective piece), not data, and the article calls it a "reading" and an "account". Correct.
- Levin 2022 (TAME): **not cited in this article**. Relied on for C1 and verified in raw text as above. No reference added.
- Sneddon, Pontius & Emonet 2012: carried. The "enhanced performance on shallow gradients by up to 73%" quote was re-grepped in the PMC HTML (PMC3271881), count 1.
- Birch, Ginsburg & Jablonka 2020: carried. The "can tell us which animals are conscious, but it does not aspire to tell us which are not" quote was re-grepped in the raw text (PMC7116763), count 1.
- Ginsburg & Jablonka 2021: carried. The "Learning by habituation and sensitization has been found in bacteria" span was re-grepped in the PMC HTML (PMC7935133), count 1. Europe PMC's fullTextXML endpoint returned a 150-byte stub for this paper and for Sneddon, so a zero there was not a real absence; the HTML was used instead.
- Lyon 2015: carried. The "Habituation and sensitization have both been demonstrated in bacterial" span was re-grepped in the raw text (PMC4396460), count 1.
- MacDermott et al. 2024: carried. The quote is present in the arXiv PDF (2412.04758) as "a continuous measure of goaldirectedness rather than a binary notion of agency". The missing hyphen is a pdftotext line-break artefact, so the quote is verbatim.
- Colombo & Palacios 2021 and Brancazio, Segundo-Ortin & McGivern 2020: carried from the 08-24 and 07-16 ledgers. There is no open raw text (Europe PMC has no record of the former; the latter is behind a SAGE paywall), so they were **not re-grepped this pass**. These passages were not touched.
- Sourjik & Berg 2002, Keegstra et al. 2017, He et al. 2016, Yi et al. 2000, Watson 2023, Lyon 2020: carried from the 08-24 and 07-16 ledgers. The body claims anchored to them are byte-identical since 08-24.
- Superlative scan (`find_superlative_claims`): 0 hits.
- Inline ↔ References: no reference added or removed, and no orphans either way.

## Map-Internal Quotation Re-grep

- [P-CS5](/positions/consciousness-scope/#p-cs5) in `positions/consciousness-scope`: "no coupling, nothing chosen, nothing felt", "undefeated but not positively established", "endorses it as the reading the behaviour matches" and "denying it is proven" are each present (count 1). Credence is still **moderate** (L100), so the article's "at moderate credence" stands.
- `concepts/interface-threshold` L68/L70/L100: "may well be present", "A simple organism may have minimal phenomenal experience…" and "neutral on substrate" are all still present. The article's L79 paraphrase stands.
- `voids/agency-void` L102: "every check is performed by the faculty under investigation". The article's paraphrase stands.
- `topics/synthetic-minimal-agents…` L40/L56: "roughly a third of whose essential parts they could not account for" and "Engineered agency does not entail engineer's transparency". The bullet now matches (M3).
- `tenets` ^tenet-3-standing (available-not-actual): the article's Tenet-3 paragraph states the commitment as what "the Map holds" and as a posit. It never claims "real" or "genuine causal work", so it reads no more confidently than the standing paragraph. No change.

## Optimistic Analysis Summary

### Strengths Preserved
- The reframing from "do cells choose?" to "what observation could discriminate?". Untouched.
- The Sourjik detail as corrected on 08-24 (praised again by the 10-31 optimistic review). Untouched.
- The Nesin paragraph's final sentence distinguishing their route ("displace the noise with pathway multiplicity") from the article's ("leaves the noise in place and asks what it is doing"). This is a model of source/Map separation. Untouched.
- The L79 refusal to treat Tenet 2 as grounds for denying the cell experience (praised by the 10-31 review). Untouched.

### Enhancements Made
- CBC is now defined, and the dissent is anchored to its target with a zero-reference link to the sibling's CBC section.
- Two navigation labels were brought into line with what their target pages now say.

### Cross-links Added
- [bacterial-chemotaxis-and-minimal-biogenic-cognition](/topics/bacterial-chemotaxis-and-minimal-biogenic-cognition/#the-cellular-basis-of-consciousness-the-strongest-rival). This is a section anchor into an already-linked page, the first anchor link into that section anywhere in the corpus.

## Length

3076 → 3075 words (`analyze_length`; topics soft 3000 / hard 4000; status `soft_warning` before and after). This was length-neutral mode. Per-edit whitespace-token deltas: C2 +13 (gloss +15, "the opposing camp" → "CBC" −2), M1 −18, M2 −6, C1 +9, M3 +1. Net −1, matching `analyze_length`.

## Reasoning-Mode Classification (editor-internal)

- Deflationists (Robinson et al.): Mode Three, unchanged.
- Nesin & Chandrankunnel: their parity argument is Mode One *against the deflationist* (an over-generalisation on the deflationist's own terms), reported rather than adopted. Unchanged.
- Levin (Further Reading label only): the label now marks a framework-boundary declination ("declines his inference") rather than attributing the Map's stance to him.
- No editor vocabulary in prose (scanned).

## Remaining Items

- The sibling-label task (see C1) is minted in `todo.md`.
- The 08-24 Remaining Items (apex source-list omission; cluster-wide one-directional [P-CS5](/positions/consciousness-scope/#p-cs5) linkage) are carried and untouched.

## Stability Notes (carried forward, plus new)

- All 08-24 stability notes stand. That covers bedrock physicalist disagreement; the hedged intractability wager anchored to [P-CS5](/positions/consciousness-scope/#p-cs5) moderate; the intentionally omitted Brancazio DOI; the corrected Sourjik detail; interface-threshold not being a synonym for "no interface"; FEP triviality rather than unfalsifiability (and not Andrews 2021 as a critic); the two distinct Lyon papers; and Birch et al. 2020 saying nothing about bacteria.
- **New**: do not attribute the competency/experience decoupling, or an "unresolved-phenomenality" stance, to Levin. His own TAME text is gradualist about consciousness ("present very widely across autopoietic systems"). The decoupling is the Map's, drawn against him.
- **New**: "CBC" must stay defined on first use in this article. If the *EMBO* sentence is ever condensed, keep the gloss or move it to the first "CBC" token.
- **New**: Nesin & Chandrankunnel endorse CBC and *conscious* decision-making in bacteria. Do not soften them into neutral mechanists, and do not enlist them for the Map's conclusion.