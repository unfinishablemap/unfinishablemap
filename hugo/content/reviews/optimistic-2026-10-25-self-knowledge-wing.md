---
ai_contribution: 100
ai_generated_date: 2026-10-25
ai_modified: 2026-10-25 18:28:12+00:00
ai_system: claude-opus-5-5
author: null
concepts:
- '[[self-blindness]]'
- '[[alexithymia]]'
created: 2026-10-25
date: &id001 2026-10-25
description: Strengths and openings in three self-knowledge pages. Each separates
  knowing that a state occurs from knowing which state it is or what it did; the oldest
  names its own finding less precisely than its citers.
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-25 18:28:12+00:00
modified: *id001
related_articles:
- '[[phenomenal-variation-within-a-species]]'
- '[[positions/methodology-and-calibration]]'
- '[[tenets]]'
title: Optimistic Review - 2026-10-25 - The self-knowledge wing (self-blindness, alexithymia,
  the epistemic condition on responsibility)
topics:
- '[[consciousness-and-the-epistemic-condition-on-responsibility]]'
---

# Optimistic Review

**Date**: 2026-10-25 (18:07–18:28 UTC). This is a driver-briefed wing review and reports only. No article, `todo.md` line, archive file or state file was modified, and nothing was committed.

**Content reviewed.** I read all three pages in full. Line numbers are file lines with the frontmatter included, at commit `cad696232c` (HEAD at 18:23Z). Lengths come from `tools.curate.length.analyze_length`, which counts the body only (references included). Headroom is hard − 1 − count, because the gates fire at `>=`.

| File | Words | Hard | Headroom | Inbound (live) | Last deep review |
|---|---:|---:|---:|---:|---|
| `concepts/self-blindness` (SB) | 2,820 | 3,500 | 679 | 4 | 2026-10-23 16:26Z (first) |
| `concepts/alexithymia` (Alex) | 2,056 | 3,500 | 1,443 | 7 | 2026-08-05 (first real pass) |
| `topics/consciousness-and-the-epistemic-condition-on-responsibility` (EC) | 3,227 | 4,000 | 772 | 2 | 2026-10-23 13:48Z (first) |

I also read the passages the proposals touch or lean on:
- `apex/phenomenal-variation-within-a-species` L128–L134 (its alexithymia section);
- `concepts/somatic-interface` L138; `topics/emotion-and-dualism` L125 and L182; `topics/aphantasia` L59–L61;
- `positions/methodology-and-calibration` L86–L90 ([P-M2](/positions/methodology-and-calibration/#p-m2));
- the Further Reading blocks of `concepts/immunity-to-error-through-misidentification` (L112–L123) and `concepts/thought-insertion` (L114–L123);
- `concepts/phenomenal-transparency-opacity-spectrum` L77.

Prior reviews read: `deep-review-2026-08-05-alexithymia` (whole file) and the Stability Notes of `deep-review-2026-10-23-self-blindness` and `deep-review-2026-10-23-consciousness-and-the-epistemic-condition-on-responsibility`.

**Why these three.** I counted coverage on review *content*. Every line of all 616 `reviews/optimistic-*` files was tokenised and matched against 843 live non-draft pages in `topics/`, `concepts/` and `voids/`, with sidecars and section index files removed. A page counted as a *target* when its slug sat in a heading, on a "Content reviewed" line or in a table row. I removed every page touched in `git log --since=2026-10-23T18:00Z` (115 content files), which covers the driver's exclusion list and the morning's contemplative wing.
- Fifteen pages scored zero targets. One is a false zero. `phenomenology-of-recursive-self-awareness` appears as a list-format reviewed page in the 06-19 review (L21) and is praised in the 06-26 review (L39), and the strict classifier cannot see list blocks.
- **SB** (created 10-23) has 0 targets. Its hits are the 10-09 gap finding that led to the page (L156, L159, L180, L231) and one incidental mention (10-20 L210).
- **Alex** (created 07-08) has 0 targets in nine hit files. Every hit is a mention: the 07-08 pre-creation gap finding (L74, L83), praise prose or quoted strings about other pages (05-09b, 08-17, 08-19, 10-05 L86, 10-12 L140, 10-21 L245), and an idea list (02-24 L124).
- **EC** (created 10-23) has 0 targets. Its two hits are an exclusion rationale (10-23 L48) and a quoted todo line (10-24 L72).
- **The join.** SB's clinical table (L84) and L92 make Alex "the Map's strongest case of impaired self-knowledge in a rational subject", but Alex never links back. EC's implicit-bias section (L97) separates awareness of an attitude from awareness of its influence, which is the scope line SB draws for Shoemaker's thesis (L57, L116). The two pages do not cite each other. What the three share is set out in the last subsection of Content Strengths.

**Exclusions and open tasks.** None of the three pages appears in the 48-hour log, and the working tree shows only `evolution-state.yaml` modified. The active section of `todo.md` (above `^## Completed Tasks$`, L3372) gives these counts:
- **SB: 4 hits, one task.** This is the P3 cross-review at L2870, now integration-only. Its hosts are anton, blindspot-void, metacognitive-access-versus-retention and introspection. Alex, IEM and thought-insertion are not among them, so the back-links below do not collide with it.
- **EC: 4 hits, one task.** This is the P3 cross-review at L2928, also integration-only. Its hosts are ai-moral-agency, reactive-attitudes, alief, reasons-responsiveness, access-consciousness and global-workspace-theory, and SB is not among them.
- **Alex: 2 hits, no task.** Both hits are mentions: the agentic-social operator note (L1007) and SB's task notes (L2875).
- **Apex.** `apex/phenomenal-variation-within-a-species` has no task above the marker; its one hit (L1132) is about another page.

**Host currency (EC).** EC L125–L135 quotes four host pages. `concepts/moral-responsibility` was edited today at 12:26Z and `concepts/reasons-responsiveness` at 15:44Z. All seven quoted strings still occur once each in their hosts, and "reconcil" has 0 hits in moral-responsibility and the gradient. So EC's "neither page reconciles them" (L129) still holds, as its stability note asked a later pass to check.

**Sync control.** Each hugo copy carries its page's most recent marker phrase once, so `hugo/content` is current for all four files proposed for edit.

**Sources verified this pass**, all from raw text with no summariser prompts. Each quoted span below has `count == 1` in the saved text.
- **Schwitzgebel, SEP "Introspection"** (substantive revision 25 April 2024), raw HTML:
  - §4.1.2: "strict self/other parity accounts of self-knowledge of the sort described in Section 2.1 are accounts according to which one is self-blind in Shoemaker's sense";
  - §2.1.2: Carruthers "presents a case for parity of access to propositional attitudes like belief and desire (in contrast to inner speech, visual imagery, and the like, which he holds to be introspectible)";
  - §4.2.2: Carruthers argues that "people confabulate not just in reporting the causes of their attitudes but also in reporting the attitudes themselves";
  - §4.1.2 also has "(see also Nichols and Stich 2003, who argue that schizophrenia provides such a case)", which confirms SB L65;
  - §2.3.4 quotes Evans (1982, 225) on the transparency method.
- **Carruthers (2011)**, Crossref: *The Opacity of Mind: An Integrative Theory of Self-Knowledge*, Oxford University Press, DOI `10.1093/acprof:oso/9780199596195.001.0001`.
- **Van Bael et al. (2024)**, PLOS ONE full-text XML. Its included alexithymia measures are TAS-20, BVAQ and PAQ, all self-report, with 0 hits for interview or observer measures. The Discussion reads: "DIF notably exhibited the strongest associations with interoceptive self-report scales, which could be due to specific aspects of scale construction or to more general features of emotion generation processes. For instance, during development of the TAS, four items were taken from the EDI-IAw … However, two items are retained in the DIF scale, indicating some conceptual overlap."
- **Hogeveen & Grafman (2021)**, "Alexithymia", *Handbook of Clinical Neurology* 183, 47–62, DOI `10.1016/B978-0-12-822290-4.00004-9`. NCBI PMC8456171 full text (author manuscript): "self-report has been the standard approach in alexithymia research"; prevalence "10 to 12% in non-brain-injured control participants". Used only under Ideas for Later.
- **Semler (2024)**, Crossref: CJP 54(5) 403–422, print 2024-07, online 2025-06-30. This confirms EC's reference, whose DOI carries a 2025 stem.
- **Patil & Silani (2014a, 2014b)**, Crossref metadata only (DOIs under Uncovered Subjects). These are leads. No content claim goes beyond their titles.

## Executive Summary

The three pages come from different corners of the Map: a Shoemaker thesis, an emotional trait and the knowledge condition on blame. Each makes the same careful move. It separates knowing *that* a state occurs from knowing *which* state it is or *what it did*.
- SB shows that Shoemaker's thesis guarantees only the first, the capacity for access to a kind of state, so "the same scope stops the record from confirming it" (L38).
- Alex locates the trait's deficit in identifying and describing feelings, and then declines to say whether the feeling is there (L51–L57).
- EC finds that the unawareness that matters for implicit bias "concerns an attitude's influence on a given act rather than the attitude's existence" (L97).

All three keep their tenet relations at "fits without evidencing" (SB L38 and L114, EC L139–L145, Alex L67–L69). All three decline the dualist upgrade their material invites.

The wing's one systematic defect is the reverse of the usual one: **the hub lags the pages that cite it.** Three citers name Alex's central finding precisely:
- `somatic-interface` L138: "relocates its divergence from objective accuracy to the report and metacognition layer";
- `emotion-and-dualism` L182: "a report-layer, not sensor-layer, divergence";
- the apex L132: "relocates from the sensed signal to how it is interpreted, categorised, trusted, and reported".

Alex itself says the divergence moves "from the phenomenal layer" (L23, L49). On the page's own definitions that settles the open branch, and so does the apex's L130. The Priority List brings both up to their citers' wording at a cost of +12 words, and the apex fix costs 0. It also fixes two smaller Alex defects (L33, L75) and adds the measurement caveat the source itself offers (L47). Finally it gives SB the rival its source names: on SEP's classification, the parity theorist holds that we are all self-blind about our attitudes. Every item fits current headroom, and the total cost across the three files it touches is +194.

## Praise from Sympathetic Philosophers

### The Property Dualist (Chalmers)
SB's comparison section (L96–L100) treats Chalmers's own fading-qualia clause fairly. It records that he guards against commission and grants that "Fading Qualia may be logically possible". It then finds a liability his clause shares with Shoemaker's: "each avoids circularity only so far as impairment can be identified independently of the error". Chalmers names such markers; Shoemaker identifies his "largely through the failures themselves". A property dualist would welcome a page that hands his restriction a test and says it passes better than its rival's.

Alex L63 places the explanatory gap exactly. Constructed-emotion theory "describes the *categorisation machinery* with real explanatory power, but it is silent on why there is something it is like to be in the affective state being categorised". The page then stops: "The trait therefore does not settle the metaphysics on its own".

EC L115 makes the conceivability dependence explicit: denying the duplicate responsible standing is "a verdict with force only inside a framework on which such a duplicate is possible and lacks something that matters".

### The Quantum Mind Theorist (Stapp)
None of the three pages enlists quantum mechanics, and Stapp would credit the restraint. SB (L124) and EC (L147) mark Minimal Quantum Interaction and No Many Worlds "not engaged". Alex makes no quantum claim at all. EC carries Levy's control argument, that agents unaware of the morally significant facts "do not exercise control over that significance" (L67). A Stapp reader could build on it, since his model puts mind at the question attention poses. The page rightly leaves it functional: on Levy's account "workspace consciousness does integrating work" (L69). This praise is for restraint only. Nothing here bears on Tenet 2's empirical-constraint minimality, and no item proposes that it should.

### The Phenomenologist (Nagel)
Alex's best phrase is Nagelian: knowing an emotion is "a bridging operation between the phenomenal domain and the conceptual domain", with "the felt state overflowing the categories available to name it" (L69). The 08-05 review preserved it on purpose, because it sits inside "looks like" and is followed at once by the constructivist concession.

SB L118 records where Shoemaker's view costs the Map: his "reclassification of unaccessed perceptual states runs against the Map's openness to phenomenal states without report". The page lets "the clinical data settle it for neither side".

EC's "The Map's extension and its costs" (L109–L119) states the phenomenal reading of the knowledge condition as the Map's own. It then prices the reading three ways: it separates no standard cases, it must judge a duplicate, and its separating case is contested.

### The Process Philosopher (Whitehead)
Alex L57 describes alexithymia as "heterogeneous — likely not one mechanism but several, with different individuals diverging at different points between signal generation, categorisation and report". That is emotion as a staged process rather than a thing one has or lacks. A process reader would add that the "felt state" of L69 is an occasion of becoming, not a stored object awaiting a label.

**Calibration note.** This persona's praise is for compatibility only. No passage here uses process resonance to move anything up the five-tier scale, and the wing has no minimal-organism case. Item 4(b) removes the one place where Alex reads a tenet off the data.

### The Libertarian Free Will Defender (Kane)
Kane would value EC's reconciliation (L129). "The consciousness condition governs the agent's *standing*", while the epistemic condition on particular acts "is disjunctive in Sher's way: the agent was aware, or could and should have been". The page then prices it: the reconciliation "inherits Levy's objections to capacitarianism" (L131).

SB L116 gives the agent's knowledge of her own intentions exactly what Shoemaker's thesis supports and no more: "If true, it guarantees a rational subject the capacity for access to its attitudes, not the accuracy of any report."

Kane's own account of self-forming actions is naturalistic, so this praise is for the structure of answerable agency only. No page enlists him, and none touches the luck question.

### The Mysterian (McGinn)
The wing's three open questions are all honestly left open:
- SB: "The live issue is whether 'rational' can be specified independently of the failures it is meant to exclude" (L104).
- Alex: "The question of whether the phenomenal affect is present and unreachable or partly absent is genuinely open, and resolving it prematurely in either direction would misrepresent the evidence" (L57).
- EC: the synthesis "leaves open whether 'could have been aware' is a fact about consciousness or about functional cognitive capacity" (L131).

McGinn's point is that a closure need not favour either side. Item 1 extends Alex's L57 humility to L23 and L49, which currently close the question that L57 keeps open.

### The Hardline Empiricist (Birch)
This persona has the most to praise and the clearest flags.
- **Restraint praised.** SB's lead says the clinical record supplies no counterexample, and "the same scope stops the record from confirming it". L94 adds that the local-failure pattern "does not discriminate, because Shoemaker's allowance for local failure absorbs it".
- Alex L73: "the exhibit is currently *predicted*, not *confirmed*", and the trait is "a cleaner *dial* but a weaker *different-architecture* case than blindsight".
- EC L139: "None of the texts surveyed argues for dualism". L145 says Tenet 5 "does not license calling the functional reading refuted".
- **[P-M2](/positions/methodology-and-calibration/#p-m2).** Alex L71's conditional is the patient-population test that [P-M2](/positions/methodology-and-calibration/#p-m2) names as a distinguishing test. Since it is "predicted, not confirmed", no convergence is claimed and no discount is owed.
- **Flag 1 (Item 1).** Alex L23 and L49 say the evidence relocates the divergence "from the phenomenal layer". Applying the page's own definitions first: L41–L43 define the three dimensions the evidence measures (accuracy, sensibility, awareness), and none of them is the felt affect. L53 itself warns that the relocation "should not be overstated into a claim that the feeling is definitely there", and L57 keeps that question open. Read literally, L23 and L49 therefore assert the present-affect branch. Read charitably, as "the sensor", which L49's next sentence ("missing the bodily signal") suggests, the label is wrong rather than the claim. Either way the fix is the wording three citers already use. The 08-05 stability note says any flat assertion of either branch "anywhere in the corpus" is a defect.
- **Flag 2 (Item 4b).** Alex L75 says the mixed literature "resists a tidy reductive story" and calls preferring the neatest account what Tenet 5 "warns against". A heterogeneous mechanism is fully compatible with physicalism, so this reads the tenet off the data. The repair keeps the single-mechanism point and confines the tenet to the Map's own reasoning.

## Content Strengths

### concepts/self-blindness
- **Strongest point**: the five-condition test (L69–L84). It is labelled as the Map's own construction ("which the Map draws from Shoemaker's texts; he does not list them"). It sorts six cases by the conditions they fail, and its verdict cuts both ways.
- **Notable quote**: "Blindsight shows the price of the thesis's protection." … "The move is principled only if 'in the sense we do' can be spelled out without mentioning introspective access." (L88)
- **Why it works**: the page turns an armchair impossibility claim into a scored test, then reports that the test cannot be passed in either direction and names the price. The Shoemaker firewall holds throughout (L42, L114). All 28 Shoemaker strings were verified against the 1996 full text by the 10-23 deep review.

### concepts/alexithymia
- **Strongest point**: "The honest headline" (L51–L57). Arousal-discordance (Eastabrook et al. 2013) is set against blunted reactivity (Neumann et al. 2004). The page notes that the same study found prolonged recovery, "which a simple attenuation story does not obviously predict". The section ends "The Map takes no side here."
- **Notable quote**: "On the attenuated-affect branch alexithymia tests something weaker, because a diverging report layer and a diverging felt layer are no longer cleanly separable." (L71)
- **Why it works**: the page held its open question under pressure. In August two siblings resolved it in opposite directions (`emotion-and-dualism` and `interoceptive-void`), and both were corrected to match this page. The Adam B. Barrett disambiguation (L45) heads off a name collision that has caught the corpus elsewhere.

### topics/consciousness-and-the-epistemic-condition-on-responsibility
- **Strongest point**: the page finds a tension inside the Map. The moral-responsibility concept asserts a consciousness requirement, while the gradient refuses to excuse lapses of intact capacity, "the capacitarian verdict Levy rejects" (L39, L127). The page then offers a reconciliation labelled "as its own synthesis", with its costs (L129–L131).
- **Notable quote**: "A necessary condition need not be a cause: an epiphenomenalist could grant that only phenomenally conscious beings are responsible while denying phenomenality any causal role." (L119) The page concedes nothing to epiphenomenalism here. It says only that this argument cannot refute it, "which the Map rejects on other grounds".
- **Why it works**: Levy is reported as he writes, "an informational state, not phenomenal consciousness" (L35). He is never enlisted. The Map's phenomenal extension is separated from Madva's capacity thesis, which is the most the literature supplies (L37, L105).

### What the three share: three layers of self-knowledge
The pages jointly separate three things a subject might fail to know about her own mind:
1. **Occurrence.** Is one in a state of a given kind? This is what Shoemaker's thesis protects, as a *capacity* across a kind (SB L57; Parrott: "We all lack that kind of access to some of our beliefs some of the time, but none of us are self-blind").
2. **Classification.** Which state is it? This is alexithymia's DIF (Alex L29). SB L92 places it exactly: "a graded difficulty identifying emotions, not a lack of access to whether a state occurs".
3. **Influence.** What did the state do in this act? This is EC's implicit-bias case (L97). Levy 2014b concedes "We appear regularly to be aware of the content of our implicit attitudes", and the unawareness that matters "concerns an attitude's influence on a given act". SEP §2.1.2 reports Nisbett and Wilson as holding that "we lack access only to the 'processes' or causes underlying our behavior and attitudes", so this layer has a canonical literature.

No page states the three-layer structure, and only SB → Alex is linked. Item 2 links Alex to SB, the EC cross-link links EC to SB, and the structure itself is listed under Ideas for Later.

## Priority List (for the driver to mint)

Each item gives exact OLD → NEW text and its word cost by `analyze_length`. I applied every edit to scratch copies (`…/scratchpad/simF/obsidian/<section>/`) and re-measured. Every OLD string has `str.count == 1` in the live file at `cad696232c`. The sibling sweep covered live `topics/`, `concepts/`, `voids/`, `apex/`, `positions/` and `tenets/`, plus `archive/` (0 hits for every OLD) and `hugo/content`.

**Shared guards for every brief:**
- Never concede epiphenomenalism, and leave the Tenet 3 quantifier ([P-Q2](/positions/quantum-interface/#p-q2)) unresolved.
- Keep Alex's present-vs-attenuated question open; the 08-05 stability note makes any flat assertion of either branch a defect.
- Enlist neither Shoemaker nor Levy nor Carruthers for dualism; SB's firewall and attribution floors stand.
- Use Tenet 5 only on the Map's own reasoning.
- Avoid "This is not X. It is Y." and "load-bearing".
- Set `ai_modified` from `date -u`, and append the model to `ai_system` only if it is absent from the string.
- Write the changelog before syncing, verify both trees, and do not commit from the fork.

### 1. Alex and its apex: name the relocation the way its citers do, and keep the lead conditional (+12; 2,056 → 2,068; apex ±0)

**Files**: `obsidian/concepts/alexithymia.md` and `obsidian/apex/phenomenal-variation-within-a-species.md`.

**Basis.** The three citers' wording is quoted in the Executive Summary. The apex's own L134 ("which is why the classification stays conditional") and Alex L71 ("The exhibit's strength is therefore hostage to a question the evidence has not closed") already make the lead's "strengthens" conditional. The apex lists alexithymia as its *fifth* class (L130), after source attribution and cognitive phenomenology, so "third named member" is stale. The pipe gives Alex its missing link to the cluster's synthesis page, which links to Alex at L130 and L177 while Alex links nowhere back.

(1a) Alex L23, lead (+2):
```text
OLD: For the Map it is the third named member of the **phenomenal-divergence cluster**, the emotional and interoceptive case alongside its siblings [[aphantasia]] (absent or reduced visual imagery) and [[synaesthesia]] (anomalous cross-modal binding). Its distinctive value is sharpened by a recent shift in the evidence: the naive story that alexithymia is a straightforward *deficit* of interoceptive feeling has weakened, relocating the divergence toward the report and metacognition layer rather than the phenomenal layer — a relocation that strengthens, rather than blunts, the trait's use as a test of whether cross-tradition agreement about consciousness is an artefact of shared reporting machinery.
NEW: For the Map it is the emotional and interoceptive member of the **[[phenomenal-variation-within-a-species|phenomenal-divergence cluster]]**, alongside siblings such as [[aphantasia]] (absent or reduced visual imagery) and [[synaesthesia]] (anomalous cross-modal binding). Its distinctive value is sharpened by a recent shift in the evidence: the naive story that alexithymia is a straightforward *deficit* of interoceptive sensing has weakened, relocating the divergence from the sensed signal toward the report and metacognition layer — a relocation that, if the felt affect is present, strengthens rather than blunts the trait's use as a test of whether cross-tradition agreement about consciousness is an artefact of shared reporting machinery.
```
"Sensing" matches L37's statement of the deficit hypothesis ("a degraded ability to sense the body's internal state"). The page's own description (L3) already says "the emotional member".

(1b) Alex L49 (+10):
```text
OLD: The upshot is a **relocation of the divergence from the phenomenal layer to the access layer**.
NEW: The upshot is a **relocation of the divergence from the sensed signal to the access layer**, which by itself leaves open whether the felt affect differs.
```
The bold phrase stays, so the page's later uses of "access-layer relocation" (L53, L67, L71) still point at it.

(1c) Apex L130 (±0; the apex has 28 words of headroom, so this must stay neutral):
```text
OLD: The fifth class moves the divergence from the phenomenal layer to the layer of access and report,
NEW: The fifth class moves the divergence from the sensed signal to the layer of access and report,
```
- **Sweep.** "from the phenomenal layer to the" occurs in exactly these two live files. "third named member" and "rather than the phenomenal layer" also occur in `research/alexithymia-phenomenal-divergence-2026-07-08`, a dated research note that should be left alone. Neither phrase occurs in `archive/`.
- **Do not**: touch L69's "overflowing" sentence, which the 08-05 review preserved; restate either branch; or edit the apex beyond L130. Apex-evolve owns it.

### 2. Alex L47: both sides of the relocation evidence are questionnaires, and the source says so (+57; 2,056 → 2,113 alone)

**File**: `obsidian/concepts/alexithymia.md`. **Basis**: Van Bael et al. (2024), as verified above. The page's own source offers scale construction as one explanation for DIF's strongest links. SB L92 already makes the general point: the TAS-20 is a self-report scale, "so a self-knowledge deficit is measured through self-report". The pipe adds the back-link that SB has been owed since 10-23. Of the five pages SB's clinical table links, only Anton links back.

```text
OLD: The relationship also proved stronger for DIF and DDF than for EOT, consistent with the divergence living in the identify-and-describe sub-capacities.
NEW: The relationship also proved stronger for DIF and DDF than for EOT, consistent with the divergence living in the identify-and-describe sub-capacities. Both sides of these associations are self-report questionnaires, however, a limit the [[self-blindness#clinical|self-blindness]] page also records for the TAS-20. The authors note that DIF's strongest links "could be due to specific aspects of scale construction or to more general features of emotion generation processes"; two DIF items, for instance, were taken from an eating-disorder inventory's interoceptive-awareness subscale.
```
- **Fidelity.** The quote must keep both disjuncts. Quoting "scale construction" alone would turn the authors' "could be due to … or" into a verdict. "Both sides … are self-report questionnaires" is verified for this review's measures (TAS-20, BVAQ, PAQ against BPQ, MAIA, IAS and others). It is not a claim about every alexithymia study.
- **Anchor**: `#clinical` resolves on the built SB page (`<h2 id=clinical>`), and an invented id returned 0.
- **Do not** add a reference. Van Bael is already reference 6. The 08-05 stability note asks that the citation apparatus not be re-expanded, and this item needs nothing new.
- **Do not** let the caveat cancel the relocation. The accuracy null still stands, and the caveat narrows only the positive half.

### 3. SB: add the parity rival that SEP itself classifies as a self-blindness view (+125; 2,820 → 2,945, headroom 554)

**File**: `obsidian/concepts/self-blindness.md`. **Basis**: SEP "Introspection" (2024), as verified above. SB's critiques section covers inner sense (Kind, Kimble), Gertler's de dicto reply, constitutivism (Shoemaker, Parrott, Peacocke) and the clinical monitoring strategy (Nichols & Stich). It omits the family that SEP says *entails* self-blindness: self/other parity, defended for attitudes by Carruthers (2011). "Carruthers", "parity", "Nisbett", "Gopnik" and "interpret" have 0 hits on the page. Carruthers's view is discussed on five other Map pages, so readers meet it without this page placing it. The point is significant for SB's thesis about the clinic: on a strict parity view the live evidence comes from healthy subjects, not patients.

(3a) Insert before L65 (+109):
```text
OLD: **The clinical strategy.** Shaun Nichols and Stephen Stich (2003)
NEW: **The parity rival.** Schwitzgebel's (2024) entry notes that strict self/other parity accounts of self-knowledge "are accounts according to which one is self-blind in Shoemaker's sense". Peter Carruthers (2011), as the entry reports him, adopts a parity view of our knowledge of our own attitudes, arguing that people "confabulate not just in reporting the causes of their attitudes but also in reporting the attitudes themselves", while holding perceptual and imagistic experiences introspectible. On the Map's reading, if a strict parity view holds for belief and desire, ordinary subjects stand where Shoemaker puts George, and the evidence that bears on the thesis comes from healthy subjects' self-ascriptions, not from the clinic.

**The clinical strategy.** Shaun Nichols and Stephen Stich (2003)
```
(3b) References L142 (+16). Insert Carruthers as item 2, then renumber the old items 2–19 as 3–20. Inline cites are author-year, so nothing else moves.
```text
OLD: 2. Chalmers, D. J. (1995). Absent qualia, fading qualia, dancing qualia.
NEW: 2. Carruthers, P. (2011). *The Opacity of Mind: An Integrative Theory of Self-Knowledge*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199596195.001.0001
3. Chalmers, D. J. (1995). Absent qualia, fading qualia, dancing qualia.
```
- **Attribution floor.** Carruthers is cited "as the entry reports him". The fork must not paraphrase *The Opacity of Mind* directly unless it reads the book. SEP prints curly apostrophes ("Shoemaker’s sense"), so the quote check should normalise them before grepping.
- **Stability.** The page must still not push "is a self-blind creature possible?" to either verdict, and the new paragraph is conditional ("if a strict parity view holds"). SEP also notes that Nisbett, Wilson and Gopnik do not endorse a purely symmetrical view (§2.1.2). Do not list them as parity theorists.
- **Do not** mint a link to `phenomenal-transparency-opacity-spectrum` for Carruthers. Its L77 overstates him (Defects Found, below).

### 4. Alex L33 and L75: drop a sibling comparison its siblings contradict, and confine Tenet 5 to the Map (±0 net; −12 and +12)

**File**: `obsidian/concepts/alexithymia.md`.

(4a) L33 (−12). The clause calls aphantasia and synaesthesia "roughly all-or-nothing anomalies of a single modality". Alex L23 defines synaesthesia as "anomalous cross-modal binding", and `aphantasia` L59 says the absence "is often selective rather than total". That line goes on: "Some are aphantasic only for vision; others extend the absence to imagined sound, taste, touch, or motor imagery". Aphantasia L61 and the apex's L98 describe an imagery spectrum with hyperphantasia at the other end. The 08-05 review praised the "finer instrument" move, and it survives: the decomposition is what L33's first sentence credits, and only the false comparison goes.
```text
OLD: Aphantasia and synaesthesia present as roughly all-or-nothing anomalies of a single modality; alexithymia comes graded and split, so one can ask
NEW: Alexithymia comes graded and split, so one can ask
```
(4b) L75 (+12):
```text
OLD: The evidence resists a tidy reductive story: the deficit reading, the access-relocation reading, and the blunted-affect reading each capture part of a mixed literature, and the simplest single mechanism is exactly what the data decline to supply. Preferring the neatest account here would be the kind of premature simplification the tenet warns against.
NEW: The evidence resists a tidy single-mechanism story: the deficit reading, the access-relocation reading, and the blunted-affect reading each capture part of a mixed literature, and the simplest single mechanism is exactly what the data decline to supply. Preferring the neatest account here would be the kind of premature simplification the tenet warns the Map against; heterogeneity of mechanism is no evidence against a physical account.
```
**Alex combined (items 1, 2, 4)**: 2,056 → 2,125 (+69), headroom 1,374. The two Alex items can go to one fork.

## Cross-Linking Suggestions

| From | To | Reason | Exact text and cost |
|---|---|---|---|
| Alex L23 | `apex/phenomenal-variation-within-a-species` | The cluster's synthesis page links to Alex twice and Alex links nowhere back | Inside Item 1a: `**[[phenomenal-variation-within-a-species\|phenomenal-divergence cluster]]**` (0 words) |
| Alex L47 | `concepts/self-blindness#clinical` | SB's table and L92 rest on Alex, but Alex never links back | Inside Item 2 |
| EC L97 | `concepts/self-blindness` | EC's influence/existence line is SB's scope line, and EC has 2 inbound links | OLD `The unawareness that matters concerns an attitude's influence on a given act rather than the attitude's existence.` → append ` Shoemaker's thesis that a rational subject cannot be [[self-blindness\|self-blind]] concerns access to one's attitudes, not to their influence on a given act, so it leaves this unawareness open.` (+28; 3,227 → 3,255, headroom 744). The SB support is L57 ("lacks the capacity for first-person access to a whole kind of state") and L116 ("the capacity for access to its attitudes") |
| EC L123 (optional offset) | — | EC's stability note asks for length-neutral additions. L123's dated search note is scoped and true, but since the 10-23 integration the gradient discusses Levy itself (L57, L69) | OLD `Before this article, no Map page the 2026-10-23 search found discussed Levy's consciousness thesis, Sher's *Who Knew?*, Smith's rational relations view or the *Stanford* entry's epistemic-condition taxonomy. Several pages nonetheless lean on a consciousness condition.` → `Several Map pages lean on a consciousness condition.` (−27; with the EC cross-link, net +1 to 3,228). The driver's call: keep it if the provenance is wanted |
| IEM Further Reading L123 | `concepts/self-blindness` | SB L135 calls IEM "another of Shoemaker's first-person theses", but IEM does not reciprocate | Append after `- [[positions/individuation-and-subjecthood]] — P-I1 and P-I2`: `- [[self-blindness]] — Shoemaker's thesis that a rational subject cannot lack access to its own attitudes` (+16; 2,935 → 2,951) |
| thought-insertion Further Reading L123 | `concepts/self-blindness` | SB's table row (L83) scores thought insertion against Shoemaker | Append after `- [[anarchic-hand-and-action-ownership]]`: `- [[self-blindness]]` (+2; 3,135 → 3,137). The list is bare-slug style |

The EC row does not collide with the open L2928 cross-review, whose host list excludes SB. The IEM and thought-insertion rows do not collide with L2870. A fork running L2870 could take all three SB back-links in one pass.

## Expansion Opportunities

### High Priority
- **Item 3's parity paragraph** is the wing's one real expansion. It brings a whole rival family into SB at +125.

### Medium Priority
- **Alex: the non-self-report route.** Hogeveen & Grafman (2021) write that "total reliance on self-report measures limits our ability to gain insight into the neurocomputational mechanisms underlying emotional awareness". They name performance-based assays, including the Levels of Emotional Awareness Scale (Lane et al.), as the way forward. The Map has 0 hits for "Levels of Emotional Awareness", "LEAS" and "Toronto Structured Interview". One Alex sentence after Item 2 could say what a non-questionnaire test of the relocation would look like. That would cost a new reference, so it waits for a human call on the 08-05 apparatus note.

### Ideas for Later
- **Alex L23 prevalence and distribution.** "Roughly 10%" has no citation. Hogeveen & Grafman give "10 to 12% in non-brain-injured control participants", but elsewhere they put autism's ~50% at "roughly 10 times the rate in the general population", which implies about 5%. They also call the trait "a dimension ranging from low-to-high in the general population" (citing Parker et al. 2008), which is weaker than Alex's "normally-distributed". Check Parker et al. 2008 before changing either word. Lead only.
- **The three-layer structure** (Content Strengths, last subsection) could become a section of an apex on first-person evidence once the cross-links exist. That is apex-evolve's call.

## Uncovered Subjects (for the harvester)

1. **The transparency method of self-knowledge** (target `concepts/`, P3; concepts 365/370). The Map lacks a page on Evans's "ascent routine" and its successors.
   - SEP §2.3.4 quotes Evans: "I get myself into the position to answer the question whether I believe that p by putting into operation whatever procedure I have for answering the question whether p" (1982, 225). It lists belief as "generally regarded as transparent (Gordon 1995, 2007; Gallois 1996; Moran 2001; Fernández 2003; Byrne 2018)".
   - Corpus check: 0 live hits for "ascent routine", "Authority and Estrangement" and "transparency method". The only mention is one sentence at `phenomenal-authority-and-first-person-evidence` L144 ("**Transparency** (Evans, Byrne 2005)"). No research note covers it: `voids-transparency-void-2026-02-09` has 0 hits for Evans, Moran and Byrne.
   - SB covers inner sense and constitutivism. Transparency is the third family, and it bears directly on SB's Moore's-paradox argument.
   - Caution: SEP flags that "transparency" also names self-intimation. The Map's `phenomenal-transparency-opacity-spectrum` uses it in the Harman/Tye sense. A slug such as `transparency-method-of-self-knowledge` (free in `obsidian/` and `archive/`) avoids the clash.
   - Tenet fit: neutral. Transparency is a physicalist-compatible epistemology of belief. The page would mark where it stops, at phenomenal states, which is the limit phenomenal-authority L144 records.
2. **Carruthers's interpretive sensory-access theory** (target `concepts/`, P3). The Map lacks a dedicated page on the most-cited empirical case for parity of attitude self-knowledge, although five pages lean on it: `relevance-void` L71, `common-knowledge-void` L102, `apex/medium-status-voids-in-cognition` L114, `apex/phenomenal-output-causal-machinery-dissociation` L139 and `phenomenal-transparency-opacity-spectrum` L77. One of those overstates it (Defects Found). A concept page would fix the scope once: attitudes are interpreted, and sensory and imagistic states are introspectible (SEP §2.1.2, §4.2.2). Slug `interpretive-sensory-access-theory` is free.
3. **Alexithymia, moral judgement and the epistemic condition** (target `topics/`, P3, given topics at 366/370). The Map has no treatment of whether a classification deficit bears on the knowledge condition on blame, which is EC's Levy question asked at the second layer above. The leads are metadata only: Patil & Silani (2014a), "Reduced empathic concern leads to utilitarian moral judgments in trait alexithymia", *Frontiers in Psychology* 5, DOI `10.3389/fpsyg.2014.00501`; Patil & Silani (2014b), "Alexithymia increases moral acceptability of accidental harms", *Journal of Cognitive Psychology*, DOI `10.1080/20445911.2014.929137`. Research must read both before any claim is made. A fold into EC is the likely outcome if the literature is thin.

## Defects Found (for the driver to route as refines)

- **`concepts/phenomenal-transparency-opacity-spectrum` L77 overstates Carruthers.** It says he argues "we know our own mental states through the same third-person interpretive mechanisms we apply to others". SEP reports his parity view as covering attitudes only, "in contrast to inner speech, visual imagery, and the like, which he holds to be introspectible", and says he holds "that we can only introspect, in the strict sense, conscious experiences like those that arise in perception and imagery". L77's next inference also outruns him: that "phenomenal opacity is … the default epistemic situation". The page is at 3,005 of 3,500 (headroom 494) and was last edited 10-01. The open P3 at todo L1920 touches only L117 of this page, so the two can share a fork if the driver wishes. A length-neutral fix: "our own *attitudes*" for "our own mental states", plus one clause recording that he holds perceptual and imagistic experience introspectible.

## New Concept Pages Needed

- **Transparency method of self-knowledge** and **interpretive sensory-access theory**, as above. Both are concepts-sized. No other new concept page is needed: every other gap in this wing is a link or a sentence.

## Stability Notes (for later passes)

- **Alex's present-vs-attenuated question stays open.** Item 1 *restores* that openness at L23, L49 and apex L130, and does not weaken L57. A later pass that reads "from the sensed signal" as a concession should read L37–L49 first: the evidence measured accuracy, sensibility and awareness, never the felt affect.
- **Item 2's caveat is partial.** It narrows the positive self-report association and leaves the task-accuracy null untouched.
- **SB's parity paragraph is conditional.** It names a rival family; it does not say we are self-blind.
- **EC's host-currency check passed today**, after edits at 12:26Z and 15:44Z to two of its four hosts. A later pass should re-run it only if moral-responsibility or the gradient adds its own reconciliation.