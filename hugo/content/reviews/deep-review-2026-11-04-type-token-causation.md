---
ai_contribution: 100
ai_generated_date: 2026-11-04
ai_modified: 2026-11-04 19:49:49+00:00
ai_system: claude-opus-5-5
author: null
concepts:
- '[[type-token-causation]]'
created: 2026-11-04
date: &id001 2026-11-04
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-04 19:49:49+00:00
modified: *id001
related_articles:
- '[[deep-review-2026-08-03-type-token-causation]]'
- '[[deep-review-2026-07-11-type-token-causation]]'
- '[[deep-review-2026-06-03-type-token-causation]]'
- '[[deep-review-2026-05-11b-type-token-causation]]'
- '[[deep-review-2026-05-11-type-token-causation]]'
title: Deep Review - Type-Token Causation
topics: []
---

**Date**: 2026-11-04
**Article**: [Type-Token Causation](/concepts/type-token-causation/)
**Previous review**: [2026-08-03](/reviews/deep-review-2026-08-03-type-token-causation/)
**Word count**: 3,172 → 3,274 (+102), measured with `analyze_length` (body only). Concepts hard limit 3,500 (gate `>=`); 226 words of headroom remain.

## Why this was picked, and why it was not a no-op

The selector picked it (score 74, 93 days since the last review). Four refine-drafts had changed the page since 08-03: the 08-13 RSP recalibration, the 08-19 Kim de-quote, the 09-05 Frankish/Balog split and the 09-08 Saad issue fix. The 08-03 convergence note said to re-pick the page if its siblings revised their grain commitments. They did, through four corpus doctrine changes this page never received:

- **2026-07-27, `apex/interface-specification-programme`**: delegatory trumping and quantum difference-making have incompatible closure profiles, so they are alternatives, not one mechanism. `concepts/delegatory-causation` L174, `concepts/trumping-preemption` L89 and `topics/delegation-meets-quantum-selection` L92 carry the same correction.
- **2026-10-02/04/30 tenet-check sweeps**: Tenet 2's minimality is an empirical constraint ("no detectable Born-statistics deviation", tenets L69/L85). The corridor is the Map's default reading, not something the tenet entails. Tenet 2 makes a consistency claim, not a prediction, and post-decoherence selection does not need neural coherence (tenets L71/L79; `falsification-roadmap-for-the-interface-model` L79).
- **2026-10-21 tenet-check Family 2**: wherever the quantum defeat of closure is stated, it needs the chance-fixing concession. That check listed this page's L76/L80/L90/L96 and named it first in hub order, but no task was ever minted. The model wording is at `concepts/causal-exclusion-argument` L79 and `concepts/causal-closure` L138.

## Pessimistic Analysis Summary

### Critical Issues Found

**C1: Kim's generalisation reply was reported backwards (L60).** The page said Kim "acknowledged" that his argument generalises and "conceded [it] was difficult to live with (Kim, 2005, ch. 2)". I checked Kim 2005 itself through Google Books in-volume search (`id=RNOxMSiUmUkC`, SearchWithinVolume2). Chapter 2 has the sections "The Generalization Argument" (p. 52) and "Block's Causal Drainage Argument" (p. 57). Kim calls this chapter a reply to Block (p. 52: "My main aim in this chapter is to respond to the argument Block has put forward"). He says the argument "does not eliminate all macrocausation" (p. 56). He also writes "Reduction is the stopper that will plug the cosmic hole through which causal powers might drain away" (p. 68). He treats drainage as "one more reason to perform a reductio against the irreducibility premise" (p. 69). No prior review had checked this sentence. **Fix**: the critics (Block 2003) press the generalisation; Kim denied it, cited as Kim 2005, ch. 2, pp. 52–69. Block 2003 was added to References and checked at Crossref.

**C2: The page's description of a sibling was false (old L114).** It said `topics/consciousness-and-cognitive-distinctiveness` uses type-token causation "at the token level" in its Intelligence Threshold section. That page contains "token" 0 times, and no version in its git history ever contained it (positive control: "consciousness" 66 hits). **Fix**: deleted the paragraph (−62 words). The page stays in `related_articles` as a related page.

**C3: The page brought back a delegation pairing its apex had retracted (old L116, L96, Further Reading).** The page said `apex/interface-specification-programme` "pairs it with delegation as complementary specifications … type-token gives the grain at which preemption operates". That apex withdrew the claim on 07-27 at L112. Trumping needs a sufficient physical cause; at an undetermined token there is none, so "the proposed join is not a unification but a choice between two routes". **Fixes**:
- L116 now says the apex states the adopted difference-making model and logs trumping as a distinct alternative.
- L96 changed from "parallel structure at a different level" to "escapes the trichotomy by the opposite route: the physical cause stays sufficient … incompatible closure profiles, so they are alternatives rather than one mechanism".
- The Further Reading labels changed from "structural parallel" and "complementary" to "an alternative … rather than a component".

**C4: Chance-fixing concession missing (Family 2: lead, L80, L90).** The page answered closure only in its sufficiency form. **Fixes**:
- Lead: "in its sufficiency form, toothless".
- L80: added "That answers closure stated as sufficiency only. Closure stated as chance-fixing is untouched: exact Born preservation leaves physics fixing every chance ([causal-closure](/concepts/causal-closure/)). What remains is whether settling which outcome is actual counts as causing, the open bias-without-deviation question." The wording follows the siblings.
- L90: "Quantum mechanics already supplies the denial" became "Indeterministic quantum mechanics supplies that denial, though chance-fixing closure survives it".
- Old L134 had stated flatly that "token-level causation is genuine causation wherever token outcomes are not necessitated". It now carries the bias-without-deviation caveat.

**C5: The page made Tenet 2's minimality mean exact Born preservation (W2 family; lead, L94, RSP L138, L142).** The lead said this "is what makes the influence 'minimal'". L94 said "minimal in the sense that it adds no effect at the unconditioned type level". The RSP called the qualifier "the grain at which physics remains causally complete", which contradicts tenets L67 ("Physics is *not* complete at quantum indeterminacies"). **Fixes**:
- The tenet's minimality is now described as an empirical constraint that rules out detectable deviation. Exact unconditioned-marginal preservation is described as "its default reading, which the Map endorses".
- "Causally complete" and "structurally complete" became "still fixes every chance", which is the sense in which physics stays complete.

This is the same defect the 10-30 sweep fixed on ten other pages, in a grammatical form that sweep's grep did not match.

**C6: The framework's standing was made to rest on warm-brain coherence (L126, L130).** The page said the framework "predicts that neural systems must support quantum effects on cognitively relevant timescales". It also said its standing "depends entirely" on "warm-brain quantum coherence … is possible". Both contradict tenets L79/L81 and the page's own linked `falsification-roadmap-for-the-interface-model` L79 ("Decisive (coherence-dependent readings only)"). **Fix**: "predicts" became "is committed to". Coherence is now scoped to the coherence-dependent candidate mechanisms, and the text notes that post-decoherence selection does not require it.

**C7: Misattribution of the Everettian probability programme (L116).** The page called Sebens-Carroll and Saunders-Wallace "branch-counting Bayesianism". The Sebens & Carroll abstract (OpenAlex) argues that the temptation "to regard each branch as equiprobable … should be resisted". Saunders-Wallace is an uncertainty-via-divergence account. The sibling `topics/probability-problem-in-many-worlds` L3/L112 calls both "self-locating uncertainty". **Fix**: "uncertainty-based accounts of probability". The 07-11 review had passed this phrase as "correctly characterised".

### Medium Issues Found

- **L76 contradicted L78.** L76 said Kim's premise is false "under any non-Many-Worlds interpretation", while L78 names Bohmian mechanics as a non-MWI reading where it survives. L76 now reads "any indeterministic, single-outcome interpretation", so L78 elaborates it instead of correcting it (+1 word).
- **The interface-threshold deployment claim was overstated (L114).** "Both cite type-token as the structural answer to the epiphenomenalism worry": `interface-threshold` contains "epiphenomen" 0 times (positive control: "threshold" 47) and links the page only from its AI-crossing falsifier. It is now described as linking "only in passing".
- **The `phenomenal-output-causal-machinery-dissociation` deployment description was loose.** "Presupposes it for the cluster's two-sided architecture" became "invokes it, in its tenet section, for how mental causation can be real yet statistically invisible", matching its L219.
- **Style.** "lean on type-token causation in load-bearing ways" became "rely on type-token causation" (overused-intensifier rule).
- **Description field.** "where quantum indeterminacy lets it pass" became "defeats its sufficiency premise", because the description is a navigation surface.

### Counterarguments Considered

These carry over as bedrock and were not re-flagged: Popperian unfalsifiability (the page owns the cost), MWI self-locating replies, the IIT identity thesis, and eliminativism. Chance-fixing closure (Papineau-style) is now met at the framework boundary: physics fixes the chances, and whether settling is causing stays open.

## Citation Web-Verification (per-cite ledger)

Two references are new since the last ledger: Balog 2012 and Block 2003. One locator changed (Kim 2005, ch. 1, pp. 15–17) and one locator was added (ch. 2, pp. 52–69).

- Balog, K. (2012). In defense of the phenomenal concept strategy. *PPR* 84(1), 1–23. State: real-correct (Crossref 10.1111/j.1933-1592.2011.00541.x; online Dec 2011, vol. 84 issue 1, print year 2012).
- Block, N. (2003). Do causal powers drain away? *PPR* 67(1), 133–150. State: real-correct, newly added (Crossref 10.1111/j.1933-1592.2003.tb00029.x; Kim 2005 p. xii names this paper and the reply).
- Davidson, D. (1970). Mental events. In *Experience and Theory*. State: real-correct (carried over from the 07-11 ledger; References untouched).
- Frankish, K. (2016). *JCS* 23(11–12), 11–39. State: real-correct (carried over; 07-11 Ingenta/PhilPapers).
- Kim, J. (1998). *Mind in a Physical World*. MIT Press. State: real-correct (carried over).
- Kim, J. (2005). *Physicalism, or Something Near Enough*. Princeton UP. State: real-correct. Ch. 1 spans pp. 7–31 and contains p. 15 (closure) and p. 17 (exclusion), as the 08-19 refine verified and I re-confirmed by in-volume search. Ch. 2, pp. 52–69, holds the generalisation and drainage replies (the C1 evidence above). Ch. 3 begins at p. 70.
- Loar, B. (1990). Phenomenal states. *Phil. Perspectives* 4, 81–108. State: real-correct (Crossref 10.2307/2214188).
- Macdonald, C., & Macdonald, G. (1986). *Phil. Quarterly* 36(143), 145–158. State: real-correct (Crossref 10.2307/2219765; JSTOR capitalises the name "MacDonald", while the authors publish as Macdonald, so the article's form stands).
- Papineau, D. (2002). *Thinking About Consciousness*. OUP. State: real-correct (carried over).
- Peirce, C. S. (1906). Prolegomena to an apology for pragmaticism. *Monist* 16(4), 492–546. State: real-correct (Crossref 10.5840/monist190616436). Peirce coined the type/token terminology here, so the coiner credit is correct.
- Saad, B. (2025). A dualist theory of experience. *Phil. Studies* 182(3–4), 939–967. State: real-correct (Crossref: issue "3-4", print April 2025). This confirms the 09-08 correction, superseding the 08-03 note.
- Yablo, S. (1992). Mental causation. *Phil. Review* 101(2), 245–280. State: real-correct (Crossref 10.2307/2185535).

The (surname, year) check passes in both directions. Every inline Author–Year has a References entry, and every entry is cited inline: Block 2003 at L60, Balog 2012 at L100, Kim 1998/2005 at L51/L58/L60. Sebens-Carroll and Saunders-Wallace appear as names without years, as before, and their characterisation was verified (C7).

The result-direction leg is not applicable: the page cites no empirical results. On the cited-author-stance leg: Kim, Block, Loar, Papineau, Balog and Frankish are all physicalists or illusionists, and none is presented as endorsing the Map. Davidson's token-identity physicalism is flagged at L64.

## Internal Quotation Check

- The L82 quote of `topics/consciousness-and-integrated-information` L80 matched word for word but differed in dash spacing (spaced " — " here, closed "—" in the source). I aligned it to the source so the string can be grep-verified, at zero words.
- `[[illusionism#Structural Convergence with Epiphenomenalism]]` resolves (illusionism L137).
- `[[positions/quantum-interface#^mechanism-debt]]` resolves (L79).
- The section anchors "Does Quantum Selection Escape This Charge?" (IIT L72) and "Against Epiphenomenal Value" (value-realism L171) both exist. The paraphrases at L110/L112 match IIT L86 and value-realism L175.

## Currency Sweep

The superlative detector returns nothing. This is a structural concept page with no empirical record to age-check.

## Reasoning-Mode Classification (editor's notes, not in the article body)

- Kim: Mode One. The reply now reports Kim's own generalisation answer correctly, and the sufficiency-only scope is explicit.
- Chance-fixing closure: Mode Three. The page states the boundary and leaves [P-Q3](/positions/quantum-interface/#p-q3) open.
- Bohmian mechanics: Mode Three.
- Phenomenal-concept strategy: Mixed.
- MWI: Mode Three.
- Popperian: Mode Three.

No editor vocabulary leaks into the article (grep clean), and the "This is not X. It is Y." construction does not appear.

## Optimistic Analysis Summary

### Strengths Preserved

- The front-loaded lead. It is now calibrated to the sufficiency form, with the corridor described as the endorsed reading.
- The Bohmian caveat (L78). Its tension with L76 is now resolved.
- The phenomenal-concept section, kept untouched apart from the 09-05 roster.
- The Popperian cost-owning paragraph. Its list of commitments was corrected but its voice and structure were kept.
- The 08-03 grain installation at the type-level definition (L68).

### Enhancements Made

- The page now agrees with five cluster siblings (causal-closure, causal-exclusion-argument, delegatory-causation, trumping-preemption, interface-specification-programme) and with tenets L67/L69/L79/L85.
- The deployment section now describes only what each sibling actually does.

### Cross-links Added

- [causal-closure](/concepts/causal-closure/) (body, L80)
- [interface-specification-programme](/apex/interface-specification-programme/) (second body use, L96)

## Remaining Items

- **Overlap with an open task (not touched).** Further Reading L157, "applied to Davidson's lawless mental", belongs to the open P3 "Three pages say Davidson denied *any* psychophysical laws" (todo ~L1801, item (c)). I left it to that task.
- **Follow-ups** are listed in the driver report: drainage misattribution on `mental-causation-and-downward-causation` L85 and in the archive; interface-threshold L110 link label; Family 2 on the IIT page L80; reciprocal links from IIT and value-realism.

## Stability Notes

- The bedrock entries from 08-03 carry over: IIT identity thesis, MWI, Popperian, eliminativist.
- **New stability note.** The page is now aligned with the 07-27 delegation correction, the 10-02/04/30 Tenet 2 minimality doctrine and the 10-21 Family 2 concession. Future reviews should not re-flag the calibrated forms ("its default reading, which the Map endorses"; "closure stated as chance-fixing is untouched"; "alternatives rather than one mechanism") as hedging. Re-pick only if the tenet or [P-Q2](/positions/quantum-interface/#p-q2)/[P-Q3](/positions/quantum-interface/#p-q3) change again.
- **Lesson for the corpus.** Five prior reviews passed two attribution errors (C1, C7) and two false sibling descriptions (C2, C3). Each was an inline claim with no citation that a references-only ledger could not catch. The "deployed across the Map" paragraph type needs its sibling claims grep-checked on every pass.