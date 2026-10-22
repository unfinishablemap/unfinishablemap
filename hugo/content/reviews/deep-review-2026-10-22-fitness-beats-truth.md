---
ai_contribution: 100
ai_generated_date: 2026-10-22
ai_modified: 2026-10-22 19:49:08+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-10-22
date: &id001 2026-10-22
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-22 19:49:08+00:00
modified: *id001
related_articles: []
title: Deep Review - Fitness-Beats-Truth Theorem
topics: []
---

**Date**: 2026-10-22
**Article**: [Fitness-Beats-Truth Theorem](/concepts/fitness-beats-truth/)
**Previous review**: [2026-07-17](/reviews/deep-review-2026-07-17-fitness-beats-truth/) (this is the 7th review file; 2026-06-21, 2026-06-04, 2026-05-19, 2026-04-01 and 2026-03-15 before that)

## Diff Scoping

The body changed substantively after the 07-17 review, so a metadata-only pass did not apply.

- 2026-09-06 (`40091fb3ab`): the OSR cross-review added a disambiguation to the structural-realism paragraph.
- 2026-09-28 (`2a3e862041`): a refine-draft rewrote L29, L31, L37 and L39 around the probabilistic statement of the theorem. It added the Berke et al. 2022 multiple-goals objection, re-tiered the §Anchoring wording, and introduced four new quotations (Hoffman et al. 2015 ×3, Prakash et al. 2021 ×2) plus references 7 and 8.
- 2026-10-12 (`13bf9853e0`): a family-resolution edit set the von Hippel–Trivers author order and queued a quote-to-work check on L85 (open P3 task "Trivers framing in two siblings", part 2).

No earlier review had grepped any quotation against raw source text. All quotations were treated as uncertified until checked.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Misquotation with a dropped qualifier (L31).** The article quoted "strict interface strategies that are tuned to fitness routinely drive naïve realist and critical realist strategies to extinction" (Hoffman et al. 2015). The source reads "naïve realist and **weak** critical realist strategies". Weak critical realism is Hoffman's term for structure-preserving (homomorphic) perception, which is exactly what the article's structural-realism objection is about, so the omission changed the claim. Restored. The same truncated quote had been copied into four other files, and "weak" was restored in each of them (see Family Resolution).
2. **Credit slip (L29 and the `description` field).** The article said the theorem was "proved by Donald Hoffman, Manish Singh, and Chetan Prakash". That is the 2015 ITP byline. The theorem is in Prakash, Stephens, Hoffman, Singh & Fields 2021, and its proof is Prakash's. L29 now reads "proved by Chetan Prakash and co-authors including Donald Hoffman and Manish Singh (Prakash et al. 2021)", and the description was re-credited to match.
3. **Internal contradiction in §Distinguishing (L51–57).** The 09-28 refine calibrated the opening, the Berke paragraph and §Anchoring, but it left this section untouched. Three of its claims contradicted the calibrated text:
   - the theorem "says the entire perceptual system was optimised for something other than truth";
   - it "establishes a formal result about what kind of perceptual system natural selection produces";
   - "organisms that perceive this way outcompete those that see truth".

   A reader who accepts the tenets would still flag these against L37 ("a lower bound on a probability"), L67 (the transfer to real perceivers is contested) and L77 (the anchor is only as strong as that transfer). All three are now scoped to "in its model", and the transfer step is marked as contested with a link to §Contestation. The section also used to say FBT is "not evolutionary debunking" while L63 describes "the evolutionary debunking Hoffman builds on the theorem". The rewrite separates the two: the theorem is a formal dominance result, and Hoffman's debunking argument is built on it and is what Bagwell targets.
4. **Calibration slip: extending FBT from perception to simplicity judgments (L91).** The text said FBT doubts parsimony judgments "by showing that the system generating them was shaped by a process indifferent to truth". That stated the extension as settled. §Anchoring (L77) confines the theorem to perception, says extensions to other cognitive sites carry only *live hypothesis* status, and Hoffman's own reply (Objection 3 in the 2015 paper) allows that selection may favour partial accuracy in mathematics and logic. L91 now gives the in-model claim (having evolved is no warrant for accuracy) and says that carrying it over to the faculty that judges simplicity is held only as a *live hypothesis*, with a link to §Anchoring. The firewall (FBT removes a defeater and does not upgrade evidence) is untouched.
5. **Cited author enlisted for a thesis he does not hold (L81/L83).** The Convergent Support section said three lines of research "converge on the conclusion that cognitive systems are optimised for something other than truth". Todd & Gigerenzer's ecological rationality says the opposite about accuracy: heuristics "excel by exploiting the reliable patterns in the world" (OpenAlex abstract). Less-is-more effects use ignorance in the service of accuracy. L81 now names the narrower conclusion that all three lines actually share, which matches what L87 already said ("selectively ignorant"). L83 adds the stance clause and an inline citation.
6. **Dropped qualifier (L84).** Field & Bonsall show that information's reproductive value can be negative *once collecting it is costly*. Their abstract notes that, without the cost, the value had been shown to be non-negative. The qualifier is restored.
7. **Quote not verifiable in the cited work (L85; open P3 task, part 2).** "We deceive ourselves the better to deceive others" was cited to von Hippel & Trivers 2011 (*BBS*):
   - It is absent from the BBS abstract (OpenAlex).
   - The BBS full text could not be reached (Cambridge paywall and HTTP 429; the BBS preprint link redirects; the Wayback Machine was offline).
   - The wording *is* grep-verified in the publisher's blurb for Trivers's 2011 book *Deceit and Self-Deception* (Penguin UK; the US title is *The Folly of Fools*).

   Whether the phrase appears in the BBS article is unknown, not disproven. The quote was removed and replaced with a paraphrase of the abstract's thesis ("evolved to facilitate interpersonal deception", avoiding "the cues to conscious deception"). It is now attributed to both authors.

### Medium Issues Found

- **Bootstrapping reply misdescribed (L69).** The article said "Hoffman acknowledges the reflexivity but argues that mathematical proof operates in a different domain". His actual reply (Hoffman et al. 2015, Objection 3) is that the games concern perception only, that "each faculty must be examined on its own", and that "perhaps in math and logic … partial accuracy is allowed". He offers it tentatively. Rewritten to match.
- **Currency: Bagwell has been answered (L63).** Hoffman & Singh 2024 (*JCS* 31(9):29–41) reply that Bagwell's argument "relies on a false premise", namely "that the mathematical formulation of a scientific theory cannot dethrone its fundamental concepts". The reply is added, with a reference entry. The contested-not-settled framing stays.
- **Overstated verbs.** L31 "has direct consequences for" became "bears on", and its follow-on antecedent became "that bearing". L71 "neutralise" became "undercut".
- **Pronoun binding.** After the L31 verb change, "those consequences" had no antecedent; it now reads "that bearing".

### Citation Ledger (§2.4)

Raw-text sources used: Crossref, PubMed efetch, OpenAlex `abstract_inverted_index`, publisher PDF, and author manuscripts on Hoffman's UCI site. WebFetch summaries were not used as verification.

- **Hoffman, Singh & Prakash 2015** (*The Interface Theory of Perception*, PBR 22(6):1480–1506): **real-correct** (Crossref; PMID 26384988).
  - "routinely dominated by nonveridical strategies tuned to fitness": verbatim (PubMed abstract).
  - "veridical perceptions escape extinction only if fitness varies monotonically with truth": verbatim (abstract; the article lowercases the sentence-initial letter).
  - The "strict interface strategies … routinely drive" quote was missing "weak". Fixed.
  - "a fitness function depends not just on the objective world, but also on the organism, its state, and an action": the comma after "world" is restored.
  - The last two quotes were grep-verified in the author manuscript at `sites.socsci.uci.edu/~ddhoff/Interface_Theory_2`. The Springer published text sits behind a client challenge and could not be read.
  - Stance: Hoffman is a conscious realist. The manuscript says ITP "can be embedded in a mathematically rigorous theory of idealism". The article does not present him as a dualist, and L47 keeps the Map's distance from his programme.
- **Prakash, Stephens, Hoffman, Singh & Fields 2021** (*Acta Biotheoretica* 69(3):319–341): **real-correct** (Crossref; PMID 33231784). The following are verbatim in the authors' 2017 preprint (`sites.socsci.uci.edu/~ddhoff/FBT-7-30-17`):
  - Theorem 4: "Over all possible fitness functions and a priori measures, the probability that the Fitness-only perceptual strategy strictly dominates the Truth strategy is at least (|X| − 3)/(|X| − 1)".
  - "will never be dominated by Truth".
  - "will generally result in a lower expected-fitness payoff".

  The published text could not be reached (the Springer client challenge; OpenAlex and Unpaywall list it as closed). The published abstract is consistent with the preprint ("quantitative measure … how this dominance increases with the size of the perceptual space"). Result direction: correct. Credit corrected (Critical 2).
- **Mark, Marion & Hoffman 2010** (*J Theor Biol* 266(4):504–515): **real-correct** (Crossref; publisher PDF hosted at UCI). The abstract result is that veridical perceptions "can be driven to extinction" by utility-tuned strategies, so the direction is correct. Control: the L31 quote has 0 hits in Mark 2010, so citing it to Hoffman 2015 is right.
- **Berke, Walter-Terrill, Jara-Ettinger & Scholl 2022** (*Cognitive Science* 46(10), e13195): **real-correct** (Crossref). Both quotes are verbatim in the OpenAlex abstract. Stance: they criticise ITP and conclude that the fittest systems "may nevertheless represent the world as it is". The article presents them as objectors, which is correct.
- **Bagwell 2023** (*Synthese* 201(1), art. 25; Jeffrey N. Bagwell): **real-correct** (Crossref). The abstract is not raw-reachable (PhilPapers 403; Crossref has no abstract). The paraphrase is unchanged from the 06-04 pass that verified it at the publisher, and Hoffman & Singh's 2024 summary of the argument agrees with it. Stance: critic.
- **Hoffman & Singh 2024** (*JCS* 31(9):29–41, doi 10.53765/20512201.31.9.029): **added, real-correct** (Crossref, abstract read). Stance: defenders replying to Bagwell.
- **Todd & Gigerenzer 2012** (*Ecological Rationality*, OUP): **real-wrong-metadata**. The article had Gigerenzer & Todd; Crossref (10.1093/acprof:oso/9780195315448.001.0001) lists Todd first. Corrected and propagated. The orphaned (surname, year) cite now has an inline cite at L83. Stance: see Critical 5.
- **Field & Bonsall 2018** (*Ecology and Evolution* 8(1):71–77; online 2017-11-23): **real-correct** (Crossref; OpenAlex abstract). The qualifier is restored (Critical 6).
- **von Hippel & Trivers 2011** (*BBS* 34(1):1–16): **real-correct** metadata (Crossref; published byline von Hippel first). The quote was removed (Critical 7). Result direction: interpersonal-deception thesis, correct. Stance: the paraphrase now credits both authors.
- **Southgate & Oquatre-six 2026** (self-citation, *Biological Cognitive Closure*): `ai_system` is `claude-opus-4-6`, which maps to Oquatre-six. Correct.
- **Orphan check, both directions, keyed on (surname, year):** all 9 external references are cited inline, and every inline cite has a reference entry. Positive controls were counted before the zero checks.
- **Superlative/currency sweep:** `find_superlative_claims` returned nothing.

### Reasoning-Mode Classification (editor-internal)

- The materialist parsimony objection is handled by marking the framework boundary (Mode Three). FBT undercuts a "wins by default" claim and does not refute materialism.
- The Bagwell–Hoffman exchange is reported, not adjudicated. It is not a Map-versus-opponent reply.
- The structural-realism objection is answered with Hoffman's in-framework response (Mode One, on his side).
- Berke et al. are conceded as contesting the transfer to real perceivers.
- The symmetry objection is conceded honestly.
- Label leakage was checked with a grep and came back clean.

## Optimistic Analysis Summary

### Strengths Preserved
- The front-loaded probabilistic statement of the theorem (the 09-28 fix), now with the correct credit.
- The FBT-versus-ITP scope discipline at L47.
- The bounded-anchor tiering at L77 and the "does not *support* dualism — it removes one class of objection" firewall at L71.
- The Berke multiple-goals paragraph, whose quotes are verbatim.

### Enhancements Made
- Hoffman & Singh 2024 added, which brings the self-defeat debate up to date.
- §Distinguishing realigned with the calibrated core (Critical 3).
- The structural-realism paragraph now benefits from the restored "weak critical realist" wording: the L31 simulations already pit fitness-tuned strategies against exactly the structure-preserving perceivers the objection appeals to.

### Cross-links
No new cross-links. The new in-page anchor links (`#contestation-and-limits`, `#anchoring-the-naturally-occluded-category`) point at headings that exist in this file.

## Family Resolution

- **Todd & Gigerenzer order** propagated to the following, with `ai_modified` bumped and `ai_system` unchanged on these one-token fixes:
  - `voids/biological-cognitive-closure` ref 3;
  - `archive/voids/adaptive-cognitive-limits` ref 1;
  - `archive/voids/evolved-cognitive-limits` ref 3;
  - the inline cite in `archive/concepts/adaptive-cognitive-limits` L51, whose reference list already had Todd first.

  `concepts/naturally-occluded` was already correct. The research note `research/voids-adaptive-cognitive-limits-2026-02-08` was left as a historical record.
- **"weak critical realist" restored** in the Hoffman 2015 quote in `concepts/naturally-occluded` L63, `voids/biological-cognitive-closure` L87, and the three archive copies. Each fix is one token inside quotation marks.

## Length

Concepts thresholds: soft 2500 / hard 3500 / critical 5000; the gate is `>=`. Status is `soft_warning` before and after, with hard not reached.

| | Prose | Further Reading | References | Total (`analyze_length`) |
|---|---|---|---|---|
| Before | 2208 | 170 | 195 | 2576 |
| After | 2251 | 163 | 219 | 2635 |

The net change is +59: +43 prose, −7 Further Reading, +24 References (the new Hoffman & Singh entry). The additions were partly offset by tightening the OSR disambiguation, the L45 sentence and one Further Reading gloss, and by removing a duplicate Hoffman clause at L91.

## Remaining Items

- `concepts/naturally-occluded` L73 has the same unverified "we deceive ourselves the better to deceive others" quote cited to von Hippel & Trivers 2011. So do archive copies in `archive/voids/adaptive-cognitive-limits` L52, `archive/concepts/adaptive-cognitive-limits` L53, `archive/voids/evolved-cognitive-limits` L97 and `archive/voids/complicity-void` L76. `voids/self-maintained-cognitive-limits` L85 cites it to *The Folly of Fools*, which the publisher blurb supports.
- `voids/biological-cognitive-closure` L87 still credits the theorem to "Hoffman, Singh, and Prakash", the same slip as Critical 2. Its L139 Trivers overreach is part 1 of the open P3 task and was not touched here.
- `concepts/naturally-occluded` L71 quotes "systematically ignoring part of the available information leads to more accurate inferences" (Todd & Gigerenzer 2012). It was not grep-verified in this pass.

## Stability Notes

- The 07-17 note about the "strictly dominates" / "equal or higher expected fitness" pairing is **obsolete**. The 09-28 refine replaced the "equal or higher" wording. The current pairing is the probability lower bound plus the authors' own "will never be dominated by Truth", and both are verbatim in the preprint.
- The extension from perceptual FBT to the faculty that issues simplicity verdicts is held at *live hypothesis* (L91, matching L77). Future passes should not restore an unconditional "FBT shows the system … was shaped by a process indifferent to truth".
- Every quotation in the article is now grep-verified in raw text: abstract, publisher PDF, or author manuscript or preprint, as recorded in the ledger. The Prakash 2021 and Hoffman 2015 body quotes rest on author versions because the Springer texts were unreachable. A future pass that can open the published PDFs should confirm them there and should not re-flag them otherwise.
- The anchoring-ratio flag against mysterianism remains a known false positive for this demonstrated-formal-result article.
- Physicalist compatibility with FBT, and the symmetry objection, remain bedrock disagreements at the framework boundary.