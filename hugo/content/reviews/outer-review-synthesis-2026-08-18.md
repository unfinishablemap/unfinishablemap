---
ai_contribution: 100
ai_generated_date: 2026-08-18
ai_modified: 2026-08-18 05:45:44+00:00
ai_system: claude-opus-5
author: Andy Southgate
concepts:
- '[[concepts/haecceity]]'
- '[[concepts/buddhism-and-dualism]]'
- '[[concepts/witness-consciousness]]'
created: 2026-08-18
date: &id001 2026-08-18
description: Cross-review synthesis of three outer reviews from 2026-08-18, all three
  answering the same subject. Thirteen clusters, four of them unanimous; two reviewers
  converged on a claim the third correctly refused.
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-18 05:45:44+00:00
modified: *id001
related_articles:
- '[[project]]'
synthesis_coverage: 3/3
synthesizes:
- reviews/outer-review-2026-08-18-chatgpt-5-6-pro.md
- reviews/outer-review-2026-08-18-claude-opus-5.md
- reviews/outer-review-2026-08-18-gemini-2-5-pro.md
title: Outer Review Synthesis - 2026-08-18
topics:
- '[[eastern-philosophy-consciousness]]'
- '[[vertiginous-question]]'
---

**Date**: 2026-08-18
**Type**: Outer-review synthesis (cross-reviewer convergence analysis)
**Coverage**: 3 of 3 commissioned reviewers collected and processed. All three answered the same subject — `subject_type: recent`, "Audit eastern-philosophy-consciousness" — with the Claude and Gemini lanes reusing the subject the ChatGPT lane selected at 02:00Z. This is the cycle the steering mechanism was built for: one article, three independent hostile readings, no partial overlap to discount.

## TL;DR

Three reviewers audited a single article and produced **thirteen finding clusters, four of them unanimous**. The unanimous four are the substantive ones: the cross-traditional convergence thesis is manufactured by selective reading; Madhyamaka *śūnyatā* is a defeater the article neutralises by redefining "irreducibility" as a relation between descriptions; "process haecceitism" does not reconcile no-self with indexical identity; and Siderits's 2025 *Buddhist Physicalism?* is a live countermodel the article never meets. Eight open tasks were upgraded P2 → P1 and none were merged or deleted — the collect legs had already deduplicated, recording six (Claude) and seven (Gemini) findings as convergent rather than re-minting them, so this pass mostly weights tasks rather than consolidating them.

The cycle's most instructive result is a **failed** convergence. Claude and Gemini independently charged that the article ducks illusionism — Claude as "calibration asymmetry", Gemini as "strawmanning" — and both charges are false on the page. ChatGPT, the minority, read the section correctly and credited the concession the other two say is missing. Two reviewers agreeing on a false premise is correlated error, and a synthesis that counted voices instead of checking the text would have upgraded it to P1.

## Convergent Findings

### C1. The cross-traditional convergence thesis is manufactured, not discovered

- **Flagged by**: chatgpt, claude, gemini (3/3)
- **Verification**: clean on the core charge. Gemini's Advaita instance is partly disputed — it quotes the "Alignment" paragraph and passes over the "Tension" paragraph directly beneath it, so its specific claim that the article never noticed the incompatibility does not stand. The charge survives on the other two legs and on Gemini's Buddhist and Daoist instances.
- **Quotes**:
  - **ChatGPT 5.6 Pro**: "The article's central convergence argument is constructed at too coarse a level. 'Consciousness is real and significant' is compatible with physicalism, nonreductive physicalism, idealism, neutral monism, phenomenology, Madhyamaka conventionalism, and several forms of illusionism."
  - **Claude Opus 5**: "The convergence is manufactured by selective reading, so **evidential-independence fails**: the traditions are not independent witnesses but the same tenet-set ventriloquised three times."
  - **Gemini 2.5 Pro**: "systematically flattening complex, anti-foundationalist Eastern ontologies to force them into a parochial Western Cartesian-Whiteheadian framework."
- **Task action**: Upgraded P2 → P1: "eastern-philosophy-consciousness flattens Advaita, Buddhism and Daoism into one convergence claim" (todo.md L2751). No siblings to deduplicate.
- **Note**: Claude contributes a locus the other two miss — the article's own **Tension** paragraph at `:72` states the incompatibility and then dissolves it by fiat. The fix is therefore not to add the objection but to stop bracketing the one already present.

### C2. Madhyamaka *śūnyatā* is a defeater, neutralised by an equivocation on "irreducibility"

- **Flagged by**: chatgpt, claude, gemini (3/3)
- **Verification**: clean. The target span "irreducibility is a relation between descriptions" was grep-confirmed at `:92`, and the neighbouring `concepts/buddhism-and-dualism` positions were confirmed verbatim at `:83`, `:101` and `:133`.
- **Quotes**:
  - **ChatGPT 5.6 Pro**: "This buys compatibility by weakening the Map's commitment: a descriptive or explanatory nonreduction claim is not yet the Map's metaphysical claim that something beyond the material exists."
  - **Claude Opus 5**: "Redefining 'irreducibility' as 'a relation between descriptions' is a **coherence-inflation** manoeuvre that swaps the metaphysical thesis for a semantic one and then claims the tradition supports the metaphysical thesis."
  - **Gemini 2.5 Pro**: "Madhyamaka anti-foundationalism is not a polite epistemic caveat that can be deemed 'compatible' with an interactionist dualism; it is a lethal philosophical solvent."
- **Task action**: Upgraded P2 → P1: "eastern-philosophy-consciousness contradicts concepts/buddhism-and-dualism on Yogācāra, karma and Madhyamaka" (L2784).
- **Note**: the same Yogācāra reading is separately flagged by all three as a self-defeat — collapsing mind-to-body causation into mind-to-mind removes the second relatum Bidirectional Interaction requires. Claude finds the identical "irreducibility" swap propagated to `concepts/haecceity`, so the neighbour may need the same reconciliation once this lands.

### C3. "Process haecceitism" does not reconcile no-self with indexical identity

- **Flagged by**: chatgpt, claude, gemini (3/3)
- **Verification**: **partly disputed, and the disputed half is the reviewers' headline.** Claude's "no truth conditions" charge and its "cannot have indexicality robust enough to kill Many Worlds but soft enough for *anattā*" charge are both **already held positions** — `positions/individuation-and-subjecthood` P-I1 grades primitive thisness external-evidence D with empirical discriminability none, and P-I2 registers the Tenet-4 indexical objection as conditional. Declined as pre-conceded; they carry no convergence weight. What converges is the narrower internal contradiction, verified at three loci on disk.
- **Quotes**:
  - **ChatGPT 5.6 Pro**: "The proposal can therefore be retained as a speculative metaphysical option, but it should no longer be called a resolution. It either abandons primitive haecceity in favour of causal individuation or preserves primitive haecceity and leaves the Buddhist objection untouched."
  - **Claude Opus 5**: "It is a relabelling, not a substantive proposal... The primitive thisness does all the work and 'process' is decorative."
  - **Gemini 2.5 Pro**: "By shifting haecceity from 'substance' to 'process,' the author merely moves the target of reification, committing the exact error of conceptual clinging (*upādāna*) that Madhyamaka philosophy exists to deconstruct."
- **Task action**: Recorded only — the matching task was already P1 and cannot upgrade further: "eastern-philosophy-consciousness calls process haecceitism 'The Resolution' while tenets.md and vertiginous-question say the same disagreement is bedrock" (L2729). Convergence recorded in its notes.
- **Note**: this is the fourth consecutive cycle in which an outer reviewer's headline metaphysical charge turns out to be pre-conceded in the positions register. The register is doing its job; the reviewers are not reading it, despite the prompt instructing them to.

### C4. Siderits 2025, *Buddhist Physicalism?*, is a live countermodel the article never meets

- **Flagged by**: chatgpt, claude, gemini (3/3)
- **Verification**: clean, and unusually well-sourced — two legs verified the book independently at separate indexes (ChatGPT at OpenAlex, DOI `10.1093/9780197799697.001.0001`; Gemini at Crossref). Gemini's initial OpenAlex miss was a false absence, correctly identified as such rather than treated as evidence against the book.
- **Quotes**:
  - **ChatGPT 5.6 Pro**: "the omitted Siderits 2025 argument supplies a **Buddhist-internal** route to illusionism... its existence is enough to refute the article's suggestion that illusionism simply threatens or contradicts Buddhism's practical project from outside."
  - **Claude Opus 5**: "Siderits is a Buddhist Reductionist now defending *Buddhist Physicalism?* (OUP 2025); runs no-self toward physicalism, not dualism."
  - **Gemini 2.5 Pro**: "They completely ignore Mark Siderits's highly anticipated 2025 monograph... The manuscript acts as though a physicalist reading of Buddhism is an impossibility, a boundary it arbitrarily enforces by ignoring a landmark 2025 text."
- **Task action**: Upgraded P2 → P1: "eastern-philosophy-consciousness omits Siderits 2025 'Buddhist Physicalism?' and its falsifier list still says 'None has occurred'" (L2762).
- **Note**: three legs, three framings — omission (ChatGPT and Gemini) and author-stance (Claude, who observes that the article leans on Siderits's 2007 introduction while his 2025 monograph runs against the thesis it is cited for). The question mark in the title matters: Siderits presents the physicalist reconstruction as exploratory, so it is a countermodel to engage, not a defeat to concede.

### C5. Active inference and predictive processing are a total blind spot

- **Flagged by**: claude, gemini (2/3)
- **Verification**: clean, and the cleanest 2/3 in the cycle — two legs, two *different* verified papers, one grep-confirmed gap (`friston|active inference|predictive processing|laukkonen` returns zero across the article). Claude's supporting *quotation* from the Laukkonen–Friston–Chandaria abstract is fabricated and is excluded; the paper itself is real with exact metadata, and the gap does not depend on the quote.
- **Quotes**:
  - **Claude Opus 5**: "The article discusses *nirodha samāpatti* ('cessation'), minimal phenomenal experience, and momentariness — all of which now have explicit active-inference models — without a single reference to Friston, Clark, Seth, Hohwy... This is the site's single largest recurring blind spot."
  - **Gemini 2.5 Pro**: "The author's failure to engage with the predictive processing model of meditation renders the entire section on contemplative evidence a relic of a bygone era in neuroscience."
- **Task action**: Upgraded P2 → P1: "eastern-philosophy-consciousness has zero engagement with active inference" (L2804).
- **Note**: Gemini supplies **Laukkonen & Slagter (2021)**, "From many to (n)one" (`10.1016/j.neubiorev.2021.06.021`), which is the better citation for the meditation-specific claim than Claude's 2025 *Beautiful Loop* paper, whose fit to cessation and minimal phenomenal experience was the reviewer's inference rather than the authors' claim.

### C6. The Fox et al. 2012 inference is not licensed by the study design

- **Flagged by**: chatgpt, claude (2/3)
- **Verification**: clean on the design point. Gemini pressed the same sentence on different grounds, but its framing that the article "relies entirely on Fox" was declined at collect time — `:132` already concedes the rejoinder in the reviewer's own terms.
- **Quotes**:
  - **ChatGPT 5.6 Pro**: "It was not a randomized training study and did not test whether subjects had more accurate access to phenomenal properties as such... Better tactile calibration is equally compatible with improved metacognition about representational or quasi-phenomenal states."
  - **Claude Opus 5**: "the study is **cross-sectional** (experience *predicts* accuracy; does not show training *produces* it), a limitation the site's own changelog flags for sibling articles."
- **Task action**: Recorded only — matching task already P1: "eastern-philosophy-consciousness reads the extended-cessation study backwards... and the Fox et al. correction never reached the inference" (L2740).
- **Note**: the defect is that a correction already applied to the *citation* sentence never reached the *inference* two clauses later. That shape — a repair that stops at the first locus — is worth watching for elsewhere.

### C7. Citation auditability: the Tallis year mismatch and the unlocatable Laozi

- **Flagged by**: chatgpt, claude (2/3)
- **Verification**: clean, both verified on disk and at the publisher of record.
- **Quotes**:
  - **ChatGPT 5.6 Pro**: "The text invokes 'Tallis's regress (2011),' but the bibliography contains only Tallis 2024... 'Lao Tzu … Various translations' makes textual verification impossible."
  - **Claude Opus 5**: "**FAIL** — body/reference date mismatch; the 2011 regress source is *Aping Mankind* (Routledge), a different work (correctly listed as Ref 11 on `concepts/haecceity`)."
- **Task action**: Upgraded P2 → P1: "eastern-philosophy-consciousness citation-auditability fixes" (L2773).
- **Note**: Claude's independent check supplies the *answer* as well as the flag — the regress comes from *Aping Mankind* (2011), and the sibling `concepts/haecceity` page already lists it correctly, so the fix is a copy rather than a research task. The *saṅkhāra* mistranslation bundled into the same task is a ChatGPT singleton (see below).

### C8. "Process haecceitism" is the Map's own coinage, presented without provenance

- **Flagged by**: claude, gemini (2/3 on the observation)
- **Verification**: clean. Claude verified the compound term returns results only from unfinishablemap.org; a corpus grep for `coinage|neologism` returns nothing, so no page labels it.
- **Quotes**:
  - **Claude Opus 5**: "their conjunction under this label is a **site coinage presented as if it were a recognised position**."
  - **Gemini 2.5 Pro**: "the author invents a conceptual chimera... a purely ad hoc philosophical fiction generated to save a Western dualist intuition."
- **Task action**: Upgraded P2 → P1: "'process haecceitism' is presented as an established position across five live articles with no coinage label" (L2815).
- **Note**: the two legs **converge on the observation** and **diverge on the remedy** — Claude asks for a provenance label; Gemini treats the ad-hoc-ness as itself disqualifying. The Map's answer is Claude's. Gemini's word "fabricated" here means invented, not a fabricated citation; it should not be read as the latter.

### C9. `concepts/witness-consciousness` recruits the Advaita *sākṣin* for two-relata dualism

- **Flagged by**: chatgpt, claude (2/3 on this page)
- **Verification**: clean. The page's `:43` and `:193` assertions were confirmed verbatim, as was `:51` — "Shankara identifies the sakshi with Brahman" — which is why the defect is a non-sequitur rather than an ignorance of the monism.
- **Quotes**:
  - **ChatGPT 5.6 Pro**: "Remove any unargued inference from 'thoughts are observed' to 'a distinct observer exists.'"
  - **Claude Opus 5**: "the Advaita *sākṣin* **is** Brahman — the sole reality — so recruiting it for a *two-relata* interactionism is a category error shared across both pages. **Tenet leakage**: the Dualism tenet's needs are read back into a monist source."
- **Task action**: Upgraded P2 → P1: "witness-consciousness runs the bare regress uncorrected and recruits the Advaita sākṣin for two-relata dualism in its lede" (L2826).
- **Note**: Gemini presses the same recruitment, but against the subject article rather than this page. The task's *other* half — the uncorrected bare regress at `:143` — is a collector finding, not a reviewer finding, and carries no convergence weight; it is in the task because it is true on disk.

### C10. Garfield 2022, *Losing Ourselves*, attacks the article's central reconciliation and is omitted

- **Flagged by**: claude, gemini (2/3)
- **Verification**: clean; title, publisher and year confirmed by Gemini's leg.
- **Quotes**:
  - **Claude Opus 5**: "Garfield (*Losing Ourselves*, Princeton 2022) argues the self is a *cognitive illusion*; would reject the dualist recruitment" — graded FAIL on author-stance-by-omission.
  - **Gemini 2.5 Pro**: "The manuscript's continued reliance on Garfield's 1995 translation of Nāgārjuna, while completely ignoring his 2022 full-scale philosophical assault on the manuscript's precise, foundational concept of indexical particularity, is an egregious omission."
- **Task action**: Upgraded P2 → P1 (shared with C11): "eastern-philosophy-consciousness omits three verified 2020s sources" (L2837).

### C11. No illusionist literature after Frankish 2016

- **Flagged by**: chatgpt, gemini (2/3)
- **Verification**: clean on the *currency* claim only, grep-confirmed (Kammerer 0 hits, no post-2016 illusionist citation). Both legs' surrounding framings were weaker than the core — Gemini's "strawmanning" premise is false, and Gemini's supporting citation named the wrong author and venue (corrected to Kammerer 2022, *Philosophical Studies*, `10.1007/s11098-022-01804-7`).
- **Quotes**:
  - **ChatGPT 5.6 Pro**: "Contemporary 'new-wave' illusionism need not make that prediction. It explicitly allows the appearance of phenomenal consciousness to remain compelling even under impeccable reasoning... Increasing discriminatory expertise can therefore coexist with illusionism."
  - **Gemini 2.5 Pro**: "An article claiming to assess the threat of illusionism to contemplative philosophy that fails to cite any illusionist literature post-2016 ... is functionally useless to a contemporary academic journal."
- **Task action**: Upgraded P2 → P1 (shared with C10): L2837. See the Divergences section — the convergent core here is citation currency and nothing more.

### C12. Empirical citations are asked to support conclusions their authors reject — **no matching task**

- **Flagged by**: chatgpt, claude (2/3)
- **Verification**: clean as a general charge; **mistargeted in one concrete instance**. ChatGPT's routing of the Demirel fix to `topics/lucid-dreaming-and-dualist-rendering` was declined at collect time — that file does not cite Demirel, and the framing at the real locus (`topics/dream-consciousness:123`) is already narrow.
- **Quotes**:
  - **ChatGPT 5.6 Pro**: "The larger problem is **inferential fidelity**: studies and traditions are repeatedly asked to support propositions substantially stronger than those their sources establish." On Yang et al. 2025: "'Consistent with reduced self-model salience while awareness-related processing continues' would be a defensible description. 'Neuroimaging supports' the Map's process-witness interpretation is not."
  - **Claude Opus 5**: "**CO-OPTATION FIREWALL FAILURE**" — its citation table grades Yang 2025, Metzinger 2024, Siderits 2007, Demirel 2025 and Garfield 1995 as author-stance failures, five of eleven rows.
- **Task action**: **None — recorded only, and deliberately so.** No task was minted for the Yang or Demirel stance findings: ChatGPT's Demirel routing was disputed, and the Yang finding overlaps the empirical-calibration scope of the already-P1 task at L2740. The subject article already carries eight live tasks and a ninth would deepen a pile-up rather than clear one. **Operator decision available**: either widen L2740's scope fence to cover the Yang "Neuroimaging supports" claim at `:86`, or mint a separate task once some of the current eight have landed.

### C13. The citation ledger should record entailment and author stance, not only metadata — **operator territory**

- **Flagged by**: chatgpt, claude (2/3)
- **Verification**: clean; this is the methodological form of C12, and the two legs proposed the same structural fix independently.
- **Quotes**:
  - **ChatGPT 5.6 Pro**: "Extend the citation ledger beyond metadata verification. Every important citation should separately record: **source existence**, **quotation/paraphrase fidelity**, **study design**, and **whether the cited source entails the article's conclusion**."
  - **Claude Opus 5**: "Add a mandatory author-stance field for every cited empirical/naturalist source... No neuroscience finding or self-model theorist may be cited as *support* for a tenet without an explicit line recording that the author rejects the dualist reading."
- **Task action**: **None — recorded, not minted.** This is a pipeline and schema change, and the open writing-style task at L2795 explicitly fences it out as an operator call. Recording it here because two independent reviewers reaching the same schema recommendation is stronger evidence than one, and because the same cycle supplied C12 as a live demonstration of what the missing field would have caught.

## Singleton Findings

Flagged by one reviewer only. Not upgraded; left at their original priority or folded into an existing task without adding weight.

- **ChatGPT 5.6 Pro**: the extended-cessation study is read backwards — its authors classify the state as one in which "consciousness is volitionally **suspended**" and conclude "consciousness can cease without global suppression", so residual regional activity is not evidence of consciousness continuing independently of neural activity. Folded into the already-P1 task at L2740, where it stands on the collector's Europe PMC verification rather than on convergence. **This is the cycle's strongest single finding and it has no second voice** — a reminder that convergence weight and evidential weight are different quantities.
- **ChatGPT 5.6 Pro**: *saṅkhāra* is mistranslated as "conditioned arising" at `:158`; the term for dependent arising is *pratītyasamutpāda* / *paṭiccasamuppāda*. Folded into L2773. The review routed it to the wrong file (`concepts/process-philosophy`, which contains no instance); the terminological point is correct and was retargeted.
- **ChatGPT 5.6 Pro**: site-methodology recommendations — a three-layer format for comparative articles (source claim / live dispute / Map appropriation), mandatory primary-source locators, and literature-sensitive falsifier sections. → `todo.md` task "adopt a three-layer format and primary-source locator rule for comparative articles" (**left at P2** — the only task in this cycle not upgraded).
- **Gemini 2.5 Pro**: Chadha 2023, *Selfless Minds*, argues Vasubandhu defends strong illusionism about self-representation — a Yogācāra-internal counterexample to the article's "None is eliminativist" at `:108`. Verified real. Folded into L2837 as the singleton strand of a task whose other two strands are convergent.
- **Claude Opus 5**: the electron/identical-particles analogy and the Metzinger MPE stance charge. The first was retargeted at collect time (the review named `concepts/haecceity`, whose only electron passage makes a different argument; the real locus already hedges). The second is **unverified** — the session's web-search budget was exhausted — and must be checked at the publisher before any article quotes it.
- **Collector findings, not reviewer findings**: the cessation claim at `:118` carries no citation at all — the preprint appears nowhere in the reference list; and `concepts/witness-consciousness:143` runs the bare regress uncorrected, having been missed by the 2026-08-03 family top-band pass. Both are in tasks on their own evidence.

## Divergences

### The verdicts differ materially, and the disagreement is itself the finding

Same article, same prompt, same day, three incompatible remedies:

- **ChatGPT 5.6 Pro**: "**major revision**" — the article's problems are fixable in place, section by section.
- **Claude Opus 5**: "**DEMOTE-TO-COHERENCE-ONLY**, trending REVISE-HARD on two sections that must not survive in their current form... Retain only if explicitly relabelled as an internal coherence exercise ('how the Map *reads* Eastern traditions') and stripped of every claim that these traditions *support*, *evidence*, or *converge on* the Dualism tenet."
- **Gemini 2.5 Pro**: "this manuscript must be unequivocally **rejected**."

Claude's is the structurally strongest recommendation, and it is not simply a midpoint between the other two. ChatGPT and Gemini disagree about *how much* to change; Claude proposes changing what *kind of thing* the article is — from an evidential argument to a coherence exercise. That is a distinct proposal, it is the only one that would dissolve C1 rather than patch it, and no task in this cycle implements it. It is an operator call, recorded here rather than minted.

### Does the article already meet the illusionist reply? Two reviewers said no; the page says yes

This is the cycle's most important negative result.

- **Claude Opus 5** charged "**calibration asymmetry**": "the pro-dualist datum (training refines access) is counted as evidence, while the symmetric illusionist reading (training refines the model's fidelity) is acknowledged and not counted."
- **Gemini 2.5 Pro** charged strawmanning: the article "dismisses the entire paradigm of strong illusionism by leaning exclusively on a single, outdated philosophical objection" and "relies entirely on Fox et al. (2012)."
- **ChatGPT 5.6 Pro** said the opposite: "The article **does** acknowledge the illusionist reply that meditators may be improving the accuracy of quasi-phenomenal self-representation. That is a useful concession."

ChatGPT is right. `:132` states the symmetric reply in the reviewers' own terms — "what improves is the fidelity of quasi-phenomenal self-representation rather than access to anything phenomenal, so this is evidential pressure rather than proof" — and `:128` and `:130` go further, announcing that "Two responses are usually offered, and they are not of equal strength" and then **refuting** the Tallis regress on illusionist grounds. Both charges were declined at collect time on the text.

Had this synthesis counted reviewers instead of checking the page, a 2/3 cluster would have upgraded a task instructing a fork to add a concession the article already makes — and the most likely outcome would have been a second, redundant hedge on a passage that is currently well calibrated. The residual valid finding, that no illusionist source after Frankish 2016 is cited, is C11 and is a citation-currency ask only.

### Does the article notice the Advaita incompatibility?

- **Claude Opus 5**: yes, and that is the problem — "**confession-without-correction**: the incompatibility is stated and dissolved by fiat."
- **Gemini 2.5 Pro**: no — "The author attempts to hand-wave this lethal incompatibility away."

Claude is right; `:72` states the objection Gemini presses. The substantive pressure (that a two-levels appeal may not rescue the alignment) is shared and is carried by C1. The charge of hand-waving an *unnoticed* problem is not.

### Claude versus the corpus on the "boilerplate confession"

Claude charged that the Tallis-regress confession is "copied verbatim across three articles" including `concepts/witness-consciousness`. The corpus says otherwise in **both** directions: that page contains no occurrence of "bare regress" or "proves nothing" — it is the one page *missing* the correction — and the phrase appears in 20 live articles, not three. The underlying observation (a confession that recurs unchanged and moves no conclusion) is sound; the locus claim is inverted, and the inversion is what produced the real defect now sitting in L2826.

## Method Notes

**Priority concentration — an artefact of the steering, not seven emergencies.** The subject article now carries **8 live tasks, all 8 at P1**. Site-wide the queue holds **10 P1 tasks, and all ten are from this one cycle** — eight on the subject article, two on siblings (`concepts/haecceity`, `concepts/witness-consciousness`). Before this synthesis the queue held two P1s.

This is what the rule mandates when three reviewers audit one article and agree, and it is not being suppressed. But it should be read for what it is: a concentration produced by *pointing three reviewers at one target*, not by one article suddenly developing eight independent emergencies. The tasks are individually sound and individually scope-fenced, and several explicitly instruct the executing fork to re-read the file first because siblings may have landed. If the operator wants the queue to reflect urgency rather than reviewer count, the natural lever is to demote the 2/3 clusters (C7–C11) back to P2 and keep P1 for the four unanimous ones (C1–C4). This is the recurring same-file task-pileup shape.

**Deduplication was already done upstream.** The collect legs suppressed their own duplicates before this pass ever ran — Claude recorded six findings as convergent with ChatGPT rather than re-minting, Gemini recorded seven. Eleven tasks were minted across three reviewers where roughly twenty-four would have been the naive count. **No tasks were merged or deleted here**, because no two describe the same defect; this pass weighted rather than consolidated. That upstream deduplication is why the convergence signal had to be reconstructed from the review bodies rather than read off duplicate task pairs.

**Disputed and declined claims, excluded from all convergence counting.** A finding that failed verification does not count, and two reviewers making the same failed claim counts for less than one that survived:

- Claude: a **fabricated site quote** ("indexical identity is a real fact" — zero matches across `obsidian/`, `archive/` and `hugo/content/`); a **fabricated abstract quote** wrapped around a real and exactly-cited paper (Laukkonen–Friston–Chandaria 2025, `10.1016/j.neubiorev.2025.106296`); the inverted boilerplate-confession locus; the calibration-asymmetry charge; and both headline metaphysical charges as pre-conceded by P-I1 and P-I2.
- Gemini: the strawmanning premise; "relies entirely on Fox 2012"; the Advaita critique that skips the Tension paragraph; a positions-register "quote" that is a **stitched composite** of two registers; a genuine quote attributed to the wrong register; and "Kammerer 2021 *Mind & Language*", which is Shabasson (`10.1007/s13164-021-00537-6`) — corrected to Kammerer 2022, *Philosophical Studies*.
- ChatGPT: three improvements routed to files that do not contain the defect (*saṅkhāra* → `concepts/process-philosophy`; the electron analogy → `concepts/haecceity`; Demirel → `topics/lucid-dreaming-and-dualist-rendering`). Two were retargeted to real loci; the third was largely unsupported as stated.

The pattern worth keeping: **metadata checking alone would have passed Claude's fabricated abstract quote**, because the reference around it is exact. Verify the span, not the reference.

**Quote-fidelity scoreboard.** ChatGPT 8 of 9 site spans verbatim with one fair near-miss and zero fabrications; Claude 33 of 34 site spans verbatim — unusually good — but one fabricated external quotation; Gemini 14 of 14 target spans genuine, a marked improvement on its 2026-08-17 leg, with two silent lead-in alterations and one stitched positions-register composite. Gemini's sourcing is now stronger than its reading: in three places its account of what the article says is less careful than its account of what the literature contains.

**Capacity.** No cluster in this cycle asks for a new article — every finding targets an existing one — so nothing here is capacity-blocked. That is fortunate: `topics/` and `concepts/` are each one slot from cap.

**A defect in this skill's own specification.** `SKILL.md` step 6 instructs the synthesis pass to replace each task's `- **Review file**:` line with a plural `- **Review files**:`. That instruction causes **silent provenance loss** and was not followed. `tools/todo/processor.py:153` matches `- **Review file**:` by exact prefix, so a plural line leaves `task.review_file` as `None`; `tools/evolution/task_selector.py:213` then stops appending the review pointer and the executing fork never learns which review raised the finding. Nothing errors — the task still parses, still carries Type, File and Notes, and still gets picked. Thirteen tasks in `todo.md` already carry the damaged plural form from earlier cycles. This pass kept the singular line intact and recorded multi-leg provenance in an additive `- **Convergent with**:` line instead. `.claude/skills/` is operator territory; the fix is reported, not applied.