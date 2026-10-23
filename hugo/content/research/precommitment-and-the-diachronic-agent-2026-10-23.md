---
ai_contribution: 100
ai_generated_date: 2026-10-23
ai_modified: 2026-10-23 23:30:49+00:00
ai_system: claude-opus-5-5
author: null
concepts:
- '[[self-control-as-skill-and-scaffolding]]'
- '[[skill-delegation]]'
- '[[causal-relevance-of-content]]'
- '[[parfit-reductionism]]'
- '[[control-theoretic-will]]'
created: 2026-10-23
date: &id001 2026-10-23
description: 'Research notes on binding one''s future self: Strotz, Elster''s Ulysses,
  Schelling''s two selves, commitment devices, advance directives, and what precommitment
  shows about binder, bound and the Map''s selector.'
draft: false
human_modified: null
last_curated: null
lastmod: 2026-10-23 23:30:49+00:00
modified: *id001
recommended_action: article
related_articles:
- '[[tenets]]'
- '[[tenets/background-commitments]]'
- '[[cross-state-void]]'
- '[[emotion-regulation-and-the-timing-of-control]]'
target_section: topics
target_slug: precommitment-and-the-diachronic-agent
title: Research Notes - Precommitment and the Diachronic Agent
topics:
- '[[the-divided-will]]'
- '[[akrasia-and-weakness-of-will]]'
- '[[diachronic-agency-and-personal-narrative]]'
- '[[personal-identity]]'
- '[[consciousness-and-neurodegenerative-disease]]'
---

# Research: Precommitment and the Diachronic Agent

**Date**: 2026-10-23
**Origin**: P3 task harvested from `reviews/optimistic-2026-10-22-location-wing.md`, New-Territory Candidate 3 ("Precommitment and the diachronic agent"; "Builds on" line at that review's L225).
**Search queries used**: two WebSearch calls (Bryan, Karlan & Nelson definition; Strotz "strategy of precommitment"), one more on the Ariely & Wertenbroch retraction, and one on Holton's "Rational Resolve". Everything else was fetched directly: Crossref and OpenAlex metadata and abstracts; the archive.org full-text-search index for Elster 1979 and Elster 2000; publisher or author PDFs of Strotz (1955–56), Bryan, Karlan & Nelson (2010 and the 2009 working paper) and Schelling (1980); raw SEP HTML for "Weakness of Will" (rev. 18 Sep 2025) and "Personal Identity and Ethics" (Dufner, first published 30 Jun 2025); Retraction Watch.

**Verification tags**: **[V-raw]** quoted wording greps in a PDF text layer or raw HTML of the source named. **[V-ocr]** wording greps in archive.org's full-text-search OCR of the book; that index gives no page numbers, so pages are unverified unless stated. **[V-abs]** abstract only (Crossref or OpenAlex). **[V-xref]** bibliographic metadata at Crossref only. **[V-sec]** through a named secondary source. **[Lead]** not verified.

## Executive Summary

Precommitment is acting at one time so as to change what one will do at a later time, through a causal route that runs outside the agent. Strotz (1955–56) named "the strategy of precommitment", and Elster (1979) made Ulysses at the mast its emblem. Elster's own definition requires "some causal process in the external world", and it explicitly excludes Ainslie's "private side bets" (internal personal rules). That makes precommitment the one scaffolding strategy built to **remove or price the agent's later override**, where if-then plans, Holton's resolutions and skill delegation all keep it.

The diachronic question has three answers in the literature: two agents (Strotz's "different person", Schelling's "as if they had two selves", Parfit's Russian nobleman), one imperfectly rational agent (Elster: "being weak and knowing it"), or sub-personal interests bargaining (Ainslie, already on the Map). The two-agent vocabulary is mostly a modelling posture. Where it is pressed as an identity claim (the nobleman), the speaker is the agent in the case, not Parfit.

The practical debates (advance directives in dementia, self-binding directives in bipolar disorder) mostly locate the binder's **authority** in capacity or critical interests, not in **numerical identity**. The SEP's 2025 survey says few have argued "that it is identity as such that matters here". The Map's persisting subject therefore settles a question the authority debate mostly treats as not decisive.

The field record on commitment devices is mixed. Take-up is low (11% and 28% in two flagship trials). Effects are real but modest. Many binders mis-size their own binding: 55% defaulted in one trial, and in another, take-up showed "little association" with measured time inconsistency.

**Verdict: `article`**, topics, slug `precommitment-and-the-diachronic-agent` (free per `check_slug.py`). The article turns on binder/bound authority, override removal and where a conscious contribution would sit. It does not survey commitment-device economics. [Reasoning below](#verdict).

**One retraction the writer must know about.** Ariely & Wertenbroch (2002), the standard citation for self-imposed deadlines as precommitment, was **retracted on 2 September 2026** after a failed replication and a data-forensics review ([details](#not-to-lean-on)). Bryan, Karlan & Nelson (2010) rely on it at pp. 680–681.

## Verdict: article, not fold {#verdict}

**Against fold** (host: `concepts/self-control-as-skill-and-scaffolding`):
- **Headroom.** Measured by `analyze_length`, the host is 3,029 words: prose before Further Reading 2,400, Further Reading 91, References 563. The concepts hard threshold is 3,500 and the gate is `>=`, so headroom is 3,500 − 1 − 3,029 = **470**.
- **Fit.** A fold that carried the identity/authority material, Elster's definition and the field record would need about 350–450 words of prose plus 5–7 references (about 150 words). It would not fit.
- **Subject drift.** It would also turn a page about strategy and skill into one about personal identity.
- **The open question the host leaves.** Its L108 leaves the persistence question explicitly open: "the literature does not force the persisting reading, and the tension stays open". The right move is a pointer clause there, plus a page that takes the question up.

**No other host can absorb it**:
- `personal-identity`: 4,033 words, already past topics hard (4,000).
- `cross-state-void`: 2,952 of voids hard 3,000, so 47 words of headroom.
- `diachronic-agency-and-personal-narrative`: about narrative and coordination, not binding.
- `parfit-reductionism`: a concepts page on Parfit's metaphysics. The nobleman fits there as one sentence, not as a treatment.

**Against `none`.** Live coverage is zero for "precommit", "Elster", "Strotz", "commitment device", "Dworkin" and "Dresser" ([Coverage](#coverage)). The Map's self-control page names the tension as open, and the subject gives the self-control wing its one case where the override is removed by design rather than retained.

**Section room.** `count_section_files('topics')` = 364 of cap 370, so 6 slots. CLAUDE.md records that the function over-counts topics by one sidecar.

**Duplication risk, and the guard against it.** The article must not re-survey:
- situation selection and implementation intentions (`self-control` §evidence);
- Ainslie's four tactics or the organ-model test (`self-control` L66, `the-divided-will`);
- Holton's resolutions (`akrasia` L76–82);
- Bratman's plans (`diachronic-agency` L81).

Link those instead. What is new is the binding relation itself.

## Coverage on the Map (scoped) {#coverage}

Method: `grep -rliF` (case-insensitive, fixed string) over live `topics/ concepts/ apex/ voids/ positions/`, sidecars excluded, then over `research/`, run 2026-10-23 about 23:10Z. These are file counts. Each nonzero live hit was read in context.

| String | Live | Research | Live hits, read |
|---|---|---|---|
| "precommit" | 0 | 3 | — (research: self-prediction, impairment and cross-state void notes) |
| "pre-commit" | 2 | 1 | Both in `apex/` (`research-programme-decisions-under-the-map`, `apex-articles`), in the **pre-registration** sense. Different subject. |
| "Ulysses" | 1 | 1 | `cross-state-void` L75, one sentence (see [Side-findings](#side-findings) item 3) |
| "Odysseus" | 1 | 1 | `akrasia` L64, Aristotle on impetuosity. Not precommitment. |
| "Elster" | 0 | 4 | — (research hits are *The Multiple Self* as Davidson's venue) |
| "Strotz" | 0 | — | — |
| "commitment device" | 0 | 1 | — |
| "advance directive" | 1 | 1 | `cross-state-void` L75 |
| "Dworkin" / "Dresser" / "critical interests" | 0 / 0 / 0 | — | — |
| "Jaworska" | 1 | — | `moral-status-threshold-or-degrees`, a different question |
| "Schelling" | 1 | 3 | `common-knowledge-void`, *Strategy of Conflict* (1960), on coordination. Different work. |
| "Laibson" | 1 | 2 | `the-divided-will` L155, a reference (McClure, Laibson et al. 2004) |
| "Kavka" / "McClennen" / "resolute choice" | 0 / 0 / 0 | — | — |
| "self-binding" | 22 | 7 | Sampled: all in the **Tenet 5** sense ("symmetric self-binding" of parsimony). Term trap. |
| **Positive control** "Ainslie" | 3 | 6 | `self-control`, `the-divided-will`, `akrasia` |
| **Positive control** "Holton" | 3 | 8 | `akrasia` L40, L76–82 and refs; `phenomenology-of-trust` (Holton 1994, on trust); `self-control` L118 |
| **Positive control** "Bratman" | 4 | 6 | `diachronic-agency` L81; `consciousness-and-collective-phenomena`; `akrasia` (1979 paper); `wholeheartedness-void` |

The closest live neighbours, and what each already holds:
- **`self-control-as-skill-and-scaffolding`**:
  - L66: Ainslie's "extrapsychic commitment (p. 74)", one of four tactics.
  - L68: Ainslie 2021 on resolve. The driver's spot-check passes: "as a test case for a broader set of future choices" is present verbatim.
  - L86: moments of policy, plus the Dretske structuring-cause reading of if-then plans ("unless the selector exercises its retained override").
  - L106: the Tenet 2 correction.
  - L108: the persistence question left open.
- **`the-divided-will`**:
  - L59: Ainslie's bargaining is "recursive self-prediction rather than negotiation between literal future selves (p. 93)".
  - L61: Thaler and Shefrin's planner–doer model.
  - L107: Steward (2012) on weakness of will as "essential to the very existence of such an agent" (p. 161). The page glosses the reason in its own words: "a settler of matters at the time of action must be able not to act on an intention already formed". **That clause is the Map's paraphrase, not Steward's wording.**
- **`akrasia-and-weakness-of-will`** L76–82: Holton's resolutions, "an intention formed precisely to insulate the agent against contrary inclinations they expect to feel when the time comes".
- **`diachronic-agency-and-personal-narrative`** L81: Bratman's plans and policies "coordinate an agent with their own future self".
- **`consciousness-and-neurodegenerative-disease`** L135: the calibrated Tenet 4 register for the demented patient's identity (see [calibration rule 5](#calibration)).
- **`emotion-regulation-and-the-timing-of-control`** (created today): policy moments for emotion (L90). No binding devices.

## Key Sources {#key-sources}

### A. The founding texts

**Strotz, R. H. (1955–56). "Myopia and Inconsistency in Dynamic Utility Maximization." *Review of Economic Studies* 23(3), 165–180. doi:10.2307/2295722.**
- **Tags.** [V-xref]: Crossref dates the issue 1955, and Bryan et al. cite it as 1956. [V-raw]: JSTOR-stamped PDF hosted at ceremade.dauphine.fr.
- **Epigraph** (p. 165), from the Odyssey: "but you must bind me hard and fast, so that I cannot stir from the spot where you will stand me . . . and if I beg you to release me, you must tighten and add to my bonds."
- **The first statement** (p. 165): the agent who recognises his inconsistency "may " precommit" his future behaviour by precluding future options so that it will conform to his present desire as to what it should be". The scare quotes around "precommit" are in the original.
- **§VI**, p. 173:
  - (1) "This we call the strategy of precommitment."
  - (2) "This we call the strategy of consistent planning."
  - On why it is rational to jettison yesterday's plan: "because to-day he is a different person with a new discount function-the old one shifted forward in time". The dash is a PDF rendering of a dash.
  - "regretting either course later on (at least for the moment) is to be expected, for otherwise precommitment would have had no purpose."
  - "What needs to be explained is not that people do precommit their future actions, but that the practice is not still more wide-spread." Strotz's answer is "risk and uncertainty, both as to future tastes and future opportunities".
- **Stance.** Economist with a formal model. His "different person" is defined by a shifted discount function. It is a figure for time-inconsistent preference, not a thesis about personal identity.

**Elster, J. (1979). *Ulysses and the Sirens: Studies in Rationality and Irrationality*. Cambridge University Press.**
- **Metadata.** No Crossref DOI resolves for the monograph. Its metadata ("Cambridge: Cambridge University Press 1979. Pp. ix + 193") is confirmed through Gauthier's review, *Canadian Journal of Philosophy* 13(1), 1983, 133–140, doi:10.1080/00455091.1983.10715839 [V-xref]. The 1977 article of the same title is *Social Science Information* 16(5), 469–526, doi:10.1177/053901847701600501 [V-xref]. Text is from archive.org item `ulyssessirensstu0000elst` (CUP 1979, ISBN 0521223881) [V-ocr].
- **Chapter II** is "IMPERFECT RATIONALITY: ULYSSES AND THE SIRENS". The contents list it at **p. 36**, and §II.1 opens it:
  - "Ulysses was not fully rational, for a rational creature would not have to resort to this device; nor was he simply the passive and irrational vehicle for his changing wants and desires, for he was capable of achieving by indirect means the same end as a rational person could have realised in a direct manner. His predicament — being weak and knowing it — points to the need for a theory of imperfect rationality that has been all but neglected by philosophers and social scientists."
  - The spelling is British ("realised").
- **Thesis:** "binding oneself is a privileged way of resolving the problem of weakness of will; the main technique for achieving rationality by indirect means."
- **The definition** is "tentative" and "a first approximation":
  - "(i) To bind oneself is to carry out a certain decision at time t1 in order to increase the probability that one will carry out another decision at time t2." The OCR renders the subscripts as "t;" and "ty". Check t1/t2 against a print copy if the subscripts are quoted.
  - A criterion on the feasible set: an act "does not count as binding oneself if the new feasible set includes the old one".
  - "(iii) The effect of carrying out the decision at t1 must be to set up some causal process in the external world."
  - "(iii) also excludes what Ainslie calls 'private side bets'", that is, internal personal rules.
  - "(v) The act of binding oneself must be an act of commission, not of omission."
  - Condition (iv) was not retrieved.
- **Pages** other than ch. II's opening are unverified.
- **Stance.** Rational-choice theorist and methodological individualist. No dualism. "Imperfect rationality" is a one-agent reading.

**Elster, J. (2000). *Ulysses Unbound: Studies in Rationality, Precommitment, and Constraints*. Cambridge University Press. doi:10.1017/cbo9780511625008.**
- **Tags.** [V-xref]. Text from archive.org item `ulyssesunboundst0000elst` [V-ocr].
- **Contents pages:**
  - Preface and Acknowledgments p. ix.
  - Ch. I, "Ulysses Revisited: How and Why People Bind Themselves", p. 1.
  - §I.6 "Variations on a Russian Nobleman" p. 57.
  - §I.7 "Addiction and Precommitment" p. 63.
- **Self-description:** "not simply a new edition of the earlier book, though". It develops the "sometimes programmatic and sketchy arguments of the earlier book".
- **Coiner trap, binding.** The famous line is **Jens Arup Seip's**, quoted by Elster: "In politics, people never try to bind themselves, only to bind others." It comes from "a critical comment on Ulysses and the Sirens by my friend and mentor, the late Norwegian historian Jens Arup Seip". Elster's own verdict follows: "Although that statement is too stark, I now think it closer to the truth than the view that self-binding is the essence of constitution-making".
- **A second retraction, in a note:** having "with others, used marriage as a standard case of precommitment, I now believe this to be a mistake, or at least misleading". Strotz (p. 173) had listed "marriage for the sake of " settling down."" as a precommitment device.
- **The organising idea** is "a distinction between reasons for precommitment and devices for precommitment".
  - Table I.1's reasons include "Overcome passion and interest", "Overcome hyperbolic discounting" and "Overcome strategic time-inconsistency", plus preference change (neutralise or prevent).
  - The table's OCR is jumbled, so paraphrase the table. Do not quote it as a list.
- **The Russian nobleman, as quoted by Elster from Parfit** (Elster's note cites "Parfit (1973), p. 145; cited in Elster (1984), p. 109"). Elster recalls that in *Ulysses and the Sirens* he "cited the following passage from an article by Derek Parfit". Parfit's passage opens: "Let us take a nineteenth-century Russian who, in several years, should inherit vast estates. Because he has socialist ideals, he intends, now, to give the land to the peasants. But he knows that in time his ideals may fade." The nobleman "signs a legal document which will automatically give away" the land. He asks his wife to promise "that you will not consent" to revoke. Then:
  - "He might add, 'I regard my ideals as essential to me. If I lose these ideals, I want you to think that I cease to exist. I want you to regard your husband, then, not as me, the man who asks you for this promise, but only as his later self. Promise me that you would not do what he asks.'"
  - The OCR reads "1 cease" for "I cease".
  - **The identity-disowning clause is introduced by "He might add".** It is the nobleman's self-interpretation inside Parfit's example.
- **Elster's gloss:** "He intends to neutralize the effect of a preference change, not to prevent it." Akeel Bilgrami's reading of the same passage follows in Elster [Lead; not read].
- **Stance.** As above. Elster also discusses "Multiple Selves and Successive Generations" as an alternative idiom (section heading, [V-ocr]).

**Schelling, T. C. (1980). "The Intimate Contest for Self-Command." *The Public Interest*, Summer 1980, pp. 94–118.**
- **Tags.** [V-raw]: the PDF linked from nationalaffairs.com. The issue number was not checked.
- **pp. 95–96:** "People behave sometimes as if they had two selves, one who wants clean lungs and long life and another who adores tobacco … The two are in continual contest for control."
- **p. 96:** the blanket case. "That decision to go to bed minus one blanket was made by a warm boy. Another boy awoke cold in the night, too cold to retrieve the blanket, cursing the boy who had removed the blanket".
- **pp. 103–104** (between the running heads for 103 and 105), on deciding in advance to die after a disabling stroke: "We confront that question, which is the authentic 'I'? There are two of me, one who was in command when I made the arrangements, gave the instructions, and warned you not to heed that other one who might surface and speak with my voice when it was time to die. How do we tell-how do you tell-whether this is the moment of truth or the moment of derangement? This is the problem of authenticity".
  - The OCR renders 'I' as "'T'". Restore it and say so in a note, or quote around it.
- **Stance.** Game theorist. "As if" marks the two selves as a descriptive posture. He poses the authenticity question and does not answer it metaphysically.
- **Schelling 1984** ("Self-command in practice, in policy, and in a theory of rational choice", *AER* 74(2), 1–11) is metadata only. Bryan et al.'s reference list gives "Am. Econ. Rev. 74:1–11" [V-raw in Bryan et al.]. A reprint is in *Strategies of Commitment and Other Essays* (Harvard UP), pp. 63–81, doi:10.2307/j.ctv1dv0tg9.8 [V-xref]. Body not read.

### B. Commitment devices: definition and field record

**Bryan, G., Karlan, D., & Nelson, S. (2010). "Commitment Devices." *Annual Review of Economics* 2, 671–698. doi:10.1146/annurev.economics.102308.124324.**
- **Tags.** [V-xref]. [V-raw]: the published PDF, mirrored at pdf.stafforini.com; pages assigned from page-by-page extraction.
- **p. 672:** "This review is concerned with self-commitment devices—the arrangements people make to formalize and facilitate their goals. Broadly, a commitment device is an arrangement entered into by an individual with the aim of helping fulfill a plan for future behavior that would otherwise be difficult owing to intrapersonal conflict stemming from, for example, a lack of self-control."
- **p. 673,** the formal definition: "We define a commitment device as an arrangement entered into by an agent who restricts his or her future choice set by making certain choices more expensive, perhaps infinitely expensive, while also satisfying two conditions: (a) The agent would, on the margin, pay something in the present to make those choices more expensive, even if he or she received no other benefit for the payment, and (b) the arrangement does not have a strategic purpose with respect to others."
- **Wording trap.** The 2009 Yale working paper ("Commitment Contracts", Economic Growth Center DP 980) words both definitions differently: "due to personal conflict"; condition (a) as "primarily aimed at helping the agent fulfill plans … where they themselves are the source of the risk". **Quote only the 2010 wording above, and attribute it to the 2010 article.**
- **Field results as reported by the review:**
  - SEED savings "nevertheless had a high (28%) take-up" (p. 684).
  - CARES smoking "was taken up by 11% of smokers offered the account", and those offered were "3 percentage points more likely to pass the six-month test" (p. 685).
  - On over-enrolment: "some agents signed up, deposited money, and still failed the nicotine test" (p. 693).
- **pp. 680–681 lean on Ariely & Wertenbroch (2002), now retracted.** Do not import that paragraph.
- **Stance.** Development and behavioural economists. Physical or agnostic.

**Primary field studies (abstracts) [V-abs]:**
- **Ashraf, Karlan & Yin (2006).** "Tying Odysseus to the Mast: Evidence From a Commitment Savings Product in the Philippines." *QJE* 121(2), 635–672, doi:10.1162/qjec.2006.121.2.635. "202 (28.4 percent) accepted the offer"; "average savings balances increased by 81 percentage points" at twelve months.
- **Giné, Karlan & Zinman (2010).** "Put Your Money Where Your Butt Is." *AEJ: Applied* 2(4), 213–235, doi:10.1257/app.2.4.213. "11 percent took up"; "3 percentage points more likely to pass"; the effect "persisted in surprise tests at 12 months".
- **John (2020).** "When Commitment Fails: Evidence from a Field Experiment." *Management Science* 66(2), 503–529, doi:10.1287/mnsc.2018.3236.
  - "A majority appears to choose a harmful contract: While the average effect on bank savings is large, 55% of clients default and incur monetary losses."
  - The pattern is "consistent with theoretical predictions that partial sophisticates adopt weak commitments and then default".
- **Carrera, Royer, Stehr, Sydnor & Taubinsky (2022; online 2021).** "Who Chooses Commitment? Evidence and Welfare Implications." *Review of Economic Studies* 89(3), 1205–1244, doi:10.1093/restud/rdab056. Gym attendance, N = 1,248.
  - "Approximately half of the people who take up commitment contracts for higher gym attendance also take up commitment contracts for lower gym attendance."
  - "There is little association between commitment contract take-up and reduced-form and structural estimates of actual or perceived time inconsistency."
  - Offering the contracts "lowers consumer surplus".
- **Laibson (2015).** "Why Don't Present-Biased Agents Make Commitments?" *AER: P&P* 105(5), 267–272, doi:10.1257/aer.p20151084. "Commitment is a problematic prediction, since we see so little of it." "Demand for commitment is a special case rather than the general case."
- **Laibson (1997).** "Golden Eggs and Hyperbolic Discounting." *QJE* 112(2), 443–478, doi:10.1162/003355397555253. Hyperbolic discounting implies "a motive for consumers to constrain their own future choices"; an illiquid asset is "an imperfect commitment technology". **The body's "selves" idiom was not read.** Do not quote it.

### C. Identity, authority and advance binding

**Dufner, A. (2025). "Personal Identity and Ethics." *Stanford Encyclopedia of Philosophy*, first published 30 June 2025.** https://plato.stanford.edu/entries/identity-ethics/
- **Tags.** [V-raw]: raw HTML.
- **On the nobleman** (citing Parfit 1984: 325f): "If psychological continuity is relevant here, she would still have to be seen as bound by her commitment. If connectedness is relevant, she might not be."
- **On advance directives:** "not a lot of people have explicitly argued that it is identity as such that matters here (for an exception see Dresser 1986). One can argue that numerical identity is not decisive for the validity of an advance directive, and that other aspects are more important."
- **Dworkin** "argu[es] that dementia patients cannot form or revise what he calls critical interests (Dworkin 1993: 201f …)". **Jaworska** holds that "what matters is her remaining 'capacity to value' (Jaworska 1999: 109)".
- **Bibliography,** [V-raw in SEP]:
  - Dresser, R. 1986, "Life, Death, and Incompetent Patients: Conceptual Infirmities and Hidden Values in the Law", *Arizona Law Review* 28(3): 373–405.
  - Dworkin, R. 1993, *Life's Dominion*, New York: Knopf.
  - Parfit, D. 1973, "Later Selves and Moral Principles", in A. Montefiore (ed.), *Philosophy and Personal Relations*, London: Routledge, 137–169. Also [V-xref], doi:10.1515/9780773593435-009.
- Further metadata: Jaworska (1999), *Philosophy & Public Affairs* 28(2), 105–138, doi:10.1111/j.1088-4963.1999.00105.x [V-xref]. Dresser (1995), "Dworkin on Dementia: Elegant Theory, Questionable Policy", *Hastings Center Report* 25(6), 32–38, doi:10.2307/3527839 [V-xref].
- **Dworkin, Dresser and Jaworska bodies were not read.** Report their views only as the SEP reports them.

**Self-binding directives in bipolar disorder [V-abs]:**
- **Gergel & Owen (2015).** "Fluctuating capacity and advance decision-making in Bipolar Affective Disorder — Self-binding directives and self-determination." *International Journal of Law and Psychiatry* 40, 92–101, doi:10.1016/j.ijlp.2015.04.004. A corrigendum is at 41, 105.
  - An SBD is one "by which they commit themselves to treatment during future episodes of mania, even if unwilling". It "can seem the most rational way to deal with an imperfect predicament".
  - "Effectively, the autonomy and rights of people with bipolar are being 'protected' through being denied an opportunity to protect themselves."
- **Gergel, Das, Owen et al. (2021).** "Reasons for endorsing or rejecting self-binding directives in bipolar disorder: a qualitative study of survey responses from UK service users." *Lancet Psychiatry* 8(7), 599–609, doi:10.1016/S2215-0366(21)00115-2.
  - "463 (82%) of the 565 participants endorsed self-binding directives, of whom 411 (89%) describing a determinate shift to distorted thinking and decision making when unwell as their key justification."
  - **Sample:** the Bipolar UK mailing list, self-reported diagnosis, "predominantly white British". These are not population rates.
- **Spellecy (2003).** "Reviving Ulysses Contracts." *Kennedy Institute of Ethics Journal* 13(4), 373–392, doi:10.1353/ken.2004.0010. The contracts "are designed to override a present request from a legally competent patient in favor of a past request made by that patient". The paternalism charge "can be answered" by "a proper understanding of the future-directed planning embodied in Ulysses contracts", justifying some enforcement "under the rubric of weak paternalism".
- **Stephenson et al. (2023).** "Self-binding directives in psychiatric practice: a systematic review of reasons." *Lancet Psychiatry* 10(11), 887–895, doi:10.1016/S2215-0366(23)00221-3 [V-xref; no abstract retrieved].

### D. Philosophy of resolution, planning and the toxin (metadata or leads)

- **Holton.** *Willing, Wanting, Waiting* (OUP 2009), doi:10.1093/acprof:oso/9780199214570.001.0001 [V-xref]. Chapters [V-xref]: "Weakness of Will" pp. 70–96, "Temptation" 97–111, "Strength of Will" 112–136, "Rationality" 137–166. Also "Rational Resolve", *Philosophical Review* 113(4), 2004, 507–535, doi:10.1215/00318108-113-4-507 [V-xref; body closed, not read]. **Use the akrasia page's existing Holton account. No new Holton quotations.**
- **Bratman.**
  - "Toxin, Temptation, and the Stability of Intention", in Coleman & Morris (eds), *Rational Commitment and Social Justice* (CUP 1998), 59–83, doi:10.1017/cbo9780511527364.006 [V-xref].
  - "Temptation Revisited", *Structures of Agency* (OUP 2007), 256–282 [V-xref].
  - *Planning, Time, and Self-Governance* (OUP 2018), including "Temptation and the Agent's Standpoint" [V-xref; closed].
  - Précis, *Inquiry* 64(9), 2021 (online 2019), 883–891 [V-xref; closed].
  - **No Bratman claim beyond `diachronic-agency` L81's.**
- **Kavka (1983).** "The toxin puzzle", *Analysis* 43(1), 33–36, doi:10.1093/analys/43.1.33 [V-xref]. Gauthier's "Rethinking the Toxin Puzzle" and Harman's "The Toxin Puzzle" are in the 1998 Coleman & Morris volume [V-xref]. Lead for the "can one rationally intend what one will have reason not to do?" strand.
- **McClennen (1990).** *Rationality and Dynamic Choice* (CUP), doi:10.1017/cbo9780511983979 [V-xref]. "Resolute choice", a lead. Not read.
- **O'Donoghue & Rabin (1999).** "Doing It Now or Later", *AER* 89(1), 103–124, doi:10.1257/aer.89.1.103 [V-xref]. Origin of the sophisticate/naif terminology the John and Carrera abstracts use.
- **Ainslie (1992).** *Picoeconomics* (CUP), xvi + 440 pp. Metadata via reviews by Kavka (*Economics and Philosophy* 10(2), 1994, doi:10.1017/s0266267100004806) and Bloch (*Dialogue* 34(3), 1995) [V-xref]. Not read. The Map's Ainslie claims rest on the 2001 and 2021 texts.
- **Thaler & Shefrin (1981).** *JPE* 89(2), 392–406, doi:10.1086/260971 [V-xref]. Already quoted at `the-divided-will` L61.
- **Liberman (2016).** "Reconsidering Resolutions", *Journal of Ethics and Social Philosophy*, argues against Holton [Lead, via search summary only].

### E. The retracted study (flag only)

- **Ariely, D., & Wertenbroch, K. (2002).** "Procrastination, Deadlines, and Performance: Self-Control by Precommitment." *Psychological Science* 13(3), 219–224, doi:10.1111/1467-9280.00441.
  - Crossref now titles it "RETRACTED: …". It carries an `updated-by` retraction record, doi:10.1177/09567976261488042, dated 2026-09-02, *Psych Sci* 37(9), 665 [V-xref].
- **Hyndman, K., & Bisin, A. (2026).** "Replication of 'Procrastination, Deadlines, and Performance: Self-Control by Precommitment'." *Psychological Science* 37(8), 557–571, doi:10.1177/09567976261460772 [V-abs]: "We show that our results do not replicate those of the original article."
- **Retraction Watch** (3 Sep 2026) [V-sec]:
  - The notice says the replication "raised questions about the underlying data in the original study", and the Data Colada posts "called into question the veracity of the overall findings".
  - Wertenbroch "requested the retraction on July 23", according to the editor.
- **Map exposure:** 0 hits for "Wertenbroch" in `obsidian/`, `hugo/content/` and `archive/`.

## Major Positions {#positions}

### Two agents: the binder governs another (Strotz, Schelling, the nobleman, planner–doer)
- **Core claim.** Time-inconsistent preference is modelled as a game between temporal selves. Binding is one self constraining another.
- **Status of the selves.**
  - Strotz: a figure for a shifted discount function.
  - Schelling: "as if".
  - Thaler & Shefrin: a "planner" and a "doer" (`the-divided-will` L61).
  - The nobleman: an identity claim, but the agent's own ("He might add").
- **Relation to the Map.** Compatible as modelling. Incompatible only if pressed as a claim that numerically distinct subjects are involved. That would contradict [Posit One](/tenets/background-commitments/)'s diachronic subject persistence. None of the economists presses it.

### One imperfectly rational agent (Elster 1979; Bryan et al.'s "intrapersonal conflict")
- **Core claim.** One agent, "being weak and knowing it", achieves "by indirect means" what a fully rational agent would do directly.
- **Relation to the Map.** The natural fit for a persisting subject. But the fit is not evidence: the same reading suits a single physical planner.

### Interests, not selves (Ainslie)
- **Core claim.** A population of hyperbolically discounting interests bargains by recursive self-prediction (p. 93, per `the-divided-will` L59).
- **Note.** Elster 1979's condition (iii) **excludes Ainslie's private side bets from "binding oneself"**, so the Elster/Ainslie line is a definitional boundary, not a disagreement about cases.
- **Relation to the Map.** Already on the Map as a rival with no selector.

### Planning agency and resolution (Bratman; Holton; Spellecy's "future-directed planning")
- **Core claim.** Diachronic self-governance runs through intentions and resolutions that resist reconsideration. External binding is a fallback, not the paradigm.
- **Relation to the Map.** These keep the later override, so they belong with the self-control page's moments of policy. Precommitment proper is the contrast case.

### Authority without identity (Dworkin; Jaworska; the SBD literature)
- **Core claim.** Whether the earlier directive binds turns on critical interests, capacity to value, or distorted decision-making, not on whether the later patient is numerically the same person.
- **Exception.** Dresser (1986), per the SEP.
- **Relation to the Map.** The Map's posit answers "same subject?" (yes) and leaves "whose verdict governs?" open.

## Key Debates {#debates}

1. **Is the bound self another person?**
   - Sides: Strotz's and Schelling's two-self idiom; the nobleman's own words; Elster's one agent; Ainslie's interests.
   - Current state: the economic models need no fact about identity, and the philosophical uses of the case (Parfit, Dufner) ask whether continuity or connectedness matters, not whether there are two subjects.
2. **Who has authority, binder or bound?**
   - Schelling's "moment of truth or the moment of derangement?"
   - Dworkin's critical interests against Jaworska's capacity to value.
   - SBD respondents' "determinate shift to distorted thinking".
   - Spellecy's weak paternalism.
   - Open.
3. **Why so little commitment?**
   - Strotz (1955–56) already: "not still more wide-spread".
   - Laibson (2015): "a special case".
   - Carrera et al.: take-up barely tracks measured time inconsistency.
   - Open, with the field record mixed.
4. **Is a resolution a precommitment?**
   - Elster 1979 says no for internal rules (condition iii).
   - Ainslie and Holton treat internal resolve as the main tool.
   - A definitional difference that the article must state before using the word.

## Historical Timeline

| Year | Event | Significance |
|---|---|---|
| c. 8th c. BCE | *Odyssey* XII, the Sirens | The emblem. Strotz's epigraph quotes it. |
| 1955–56 | Strotz, "Myopia and Inconsistency" | Names "the strategy of precommitment" and "consistent planning" (p. 173) |
| 1973 | Parfit, "Later Selves and Moral Principles" | The Russian nobleman (p. 145 per Elster 2000) |
| 1977 / 1979 | Elster, *SSI* article / *Ulysses and the Sirens* | Imperfect rationality. The definition of binding oneself. |
| 1980 | Schelling, "The Intimate Contest for Self-Command" | Two selves "as if". The authenticity question. |
| 1983 | Kavka, "The toxin puzzle" | Intending against later reasons |
| 1986 | Dresser, *Arizona Law Review* | Identity-based challenge to advance directives (per SEP) |
| 1990 | McClennen, *Rationality and Dynamic Choice* | Resolute choice [lead] |
| 1993 | Dworkin, *Life's Dominion* | Critical interests and the Margo case (per SEP) |
| 1997 | Laibson, "Golden Eggs" | Illiquid assets as commitment technology |
| 1999 | Jaworska; O'Donoghue & Rabin | Capacity to value; sophisticates and naifs |
| 2000 | Elster, *Ulysses Unbound* | Seip's "bind others"; marriage dropped as standard case |
| 2002 | Ariely & Wertenbroch | Self-imposed deadlines (**retracted 2026**) |
| 2006 / 2010 | Ashraf et al.; Giné et al. | Field commitment devices: 28% and 11% take-up |
| 2010 | Bryan, Karlan & Nelson | The definition and review |
| 2015 | Laibson; Gergel & Owen | "Missing" commitment; self-binding directives |
| 2020 / 2021–22 | John; Carrera et al.; Gergel et al. | Harmful mis-sized commitments; mistargeted take-up; 82% SBD endorsement in a self-selected sample |
| 2025 | Dufner, SEP "Personal Identity and Ethics" | Identity is mostly not taken as decisive for advance directives |
| 2026 | Hyndman & Bisin replication; retraction of Ariely & Wertenbroch | The deadlines result fails |

## The Map's Question: Where a Conscious Contribution Would Sit {#maps-question}

This section is the Map's interpretation. No source above argues for it.

1. **At the binding, and only there for the bound matter.**
   - Precommitment is an "act of commission" (Elster's v) at t1. Its effect routes through "some causal process in the external world" (iii).
   - If a selector contributes, its contribution to the t2 outcome is the t1 selection.
   - At t2 the device has removed options or raised their price. On the bound matter there may be nothing left to select, or only a costlier menu.
   - In the self-control page's terms, this is a moment of policy with **no retained override**, the limit case that page does not discuss.
2. **The structuring reading fits loosely, and its cost carries over.**
   - The self-control page reads an if-then plan as what Dretske calls a structuring cause, "the cause of the cue's later causing it" (L86).
   - A binding device mostly removes or prices options rather than recruiting a state to cause a movement, so it structures which effects the later trigger *can* have. That is an analogy to Dretske's learning-history notion, not an instance of it.
   - The cost carries over unchanged. In [the causal-relevance article](/concepts/causal-relevance-of-content/#causal-history-reply)'s words, history "defeats the idleness inference but establishes no efficacy".
3. **The bound self is not epiphenomenal.**
   - Ulysses at the mast hears, wants, and orders his release. His t2 will moves his voice and his limbs. The device, built at t1, blocks only its downstream route to the helm.
   - Strotz's "regretting … is to be expected" is the same point: the later self's preferences are live, and the binding is designed to overrule them.
   - So the case is no image of idle consciousness. Nor does the externalising of the binding show that the t1 decision was idle.
4. **Steward's settler, traded away on purpose.**
   - [The divided-will article](/topics/the-divided-will/#luck-objection) reports Steward's argument that weakness of will may be "essential to the very existence of such an agent" (p. 161). It explains why in its own words: a settler "must be able not to act on an intention already formed". **Quote that clause as the divided-will article's gloss, never as Steward's.**
   - Precommitment is an agent using its t1 settling to suspend its t2 settling on one matter.
   - That fits a settler view and a physical planner equally. It discriminates nothing.
   - It also leaves the luck objection where `self-control` L90 left it: the contrastive question moves to t1.
5. **Identity is necessary for *self*-binding, not sufficient for authority.**
   - If binder and bound are one persisting subject, as Posit One holds, precommitment is self-government. Otherwise it is paternalism over another.
   - The authority literature mostly does not rest the directive's force on identity (Dufner), so the Map's posit settles a prior question and leaves the live one open. That is a finding about scope, not a weakness.
   - The neurodegenerative page's L135 register is the model.
6. **The binder's model of the bound is poor.**
   - Carrera et al.'s mistargeted take-up and John's 55% default show binders mis-sizing commitments to their own future selves.
   - This bears on Bermúdez's point (`self-control` L56) that synchronic control supplies "the self-knowledge required to anticipate motivational conflicts", and on the unpublished self-prediction void ([voids-self-prediction-void-2026-10-14](/research/voids-self-prediction-void-2026-10-14/) L188, which already names precommitment as a seam).
   - It fits a "candidate-relative, low-bandwidth and fallible" selector (`self-control` L104), and a fallible physical planner equally.

## Potential Article Angles {#angles}

1. **Recommended spine: "Who binds whom?"**
   - **Lead:** Elster's definition, then the three readings. Front-load the Map's answers: the literature does not force two agents; the posit answers identity, not authority; precommitment is the scaffolding strategy that removes the override, so any contribution sits at the binding; fit, not evidence.
   - **Sections:**
     - What precommitment is and is not (Strotz, Elster's (i)/(iii)/(v), Bryan et al.; resolutions and plans as contrast).
     - Three readings of binder and bound.
     - The override removed (Ulysses at the mast; the self-control and skill-delegation contrast; Steward; Dretske loosely).
     - Identity and authority (nobleman, Schelling's authenticity question, advance directives via the SEP, SBDs).
     - The binder's poor self-model (the field record, stated as mixed).
     - Relation to Site Perspective.
2. **Alternative: a narrower page on authority across time** (Schelling's question as the frame). This is weaker for the Map, because it drifts into bioethics where the Map has no distinctive contribution beyond Posit One.
3. **Not recommended:** a commitment-device survey, or a page arguing that precommitment evidences a non-physical selector.

When writing the article, follow `obsidian/project/writing-style.md` for the named-anchor forward references, background vs. novelty decisions, tenet alignment and LLM-first ordering.

## Guards for the Article Writer (Binding) {#guards}

### Author stances

- **Strotz; Laibson; O'Donoghue & Rabin; Bryan, Karlan & Nelson; Ashraf, Karlan & Yin; Giné, Karlan & Zinman; John; Carrera et al.**
  - Economists working with quasi-hyperbolic or time-inconsistent preference models.
  - Physical or agnostic. Strotz's "different person" is a discount-function figure.
  - **Cite as describing the phenomenon, never as allies.**
- **Elster.** Rational-choice theorist. One agent with imperfect rationality. No metaphysics of the self. He revised himself twice in 2000 (constitutions; marriage). Do not cite 1979 views as his settled ones without noting the revision.
- **Schelling.** Game theorist. "As if they had two selves". He poses the authenticity question and does not answer it.
- **Parfit.** Reductionist about identity, which the Map rejects ([parfit-reductionism](/concepts/parfit-reductionism/)). The nobleman's "I cease to exist" is spoken by the nobleman ("He might add"). **Do not attribute it to Parfit as his view, and do not use it as the Map's.**
- **Ainslie.** Naturalist. Interests, not selves. On the Map already as a rival with no selector.
- **Holton; Bratman; Kavka; McClennen; Spellecy.**
  - Analytic philosophers of action and practical reason, working in a naturalist frame. None engages dualism.
  - Holton's willpower is "empirically studied, ordinary self-management" (`akrasia` L82).
- **Dworkin; Dresser; Jaworska; Dufner.** Ethicists and legal theorists. None engages dualism. Report their views through the SEP only.
- **Gergel; Owen; Stephenson et al.** Clinical ethics and psychiatry. Their case is clinical and rights-based.
- **No author in this note argues for dualism or a non-physical selector.** Write the selector placement as the Map's interpretation, in its own voice, with the self-control page's disclaimer pattern ("none of the authors above argues for it", L82).

### The calibration rule (binding) {#calibration}

1. **Fit, not evidence (Tenet 3).**
   - Precommitment is a scaffolding strategy that a physical planner uses equally well: Strotz's and Laibson's consumers are physical planners. Placing a conscious contribution at the binding is coherence inside the Map's framework only. It is neither support nor challenge.
   - Match `self-control` L88: "The fit discriminates nothing".
   - Do not write that precommitment "shows", "reveals" or "requires" a selector.
2. **The Dretske tie, without overclaiming.**
   - Link `self-control` L86 and `causal-relevance-of-content#response-families`.
   - Say that binding devices fit Dretske's structuring/triggering distinction only by analogy: they price or remove options rather than recruit a state through learning.
   - Carry the cost: the relevance is past-tense, and history "establishes no efficacy" (`causal-relevance-of-content` L78).
   - The self-control page's own verb is "would then be". Keep it conditional.
3. **Never concede epiphenomenalism.**
   - That the binding is externalised does not show that the conscious decision to bind is idle.
   - The bound self's will is causally live: it moves voice and limbs, and the device blocks its route to the outcome.
   - Equally, do not argue the converse ("binding is deliberate and felt, so consciousness does it"). The cost-signal reading (`self-control` §effort-as-evidence) and [P-A4](/positions/agency-and-will/#p-a4)'s verification limit apply.
4. **Tenet 2 is empirical-constraint minimality, not fewness.**
   - "One choice now governs many later" is fewness of interventions.
   - Tenets L69: "*empirical-constraint* minimality, fixed by the Rules-out clause".
   - `self-control` L106 already says the economy of policy moments "is not the empirical-constraint minimality the tenet names, and it suits a physical controller equally, so it is no evidence". Match it.
   - Note: `diachronic-agency` L131 reads Tenet 2 partly as "sustained sequences of minimal selections". **Do not copy that framing** ([Side-findings](#side-findings) item 5).
5. **Tenet 4 and indexical identity.**
   - The persisting subject comes from [Posit One](/tenets/background-commitments/) ("Diachronic subject persistence"), not from rejecting many-worlds.
   - Use `consciousness-and-neurodegenerative-disease` L135 as the model: "rejecting many-worlds secures only indexical identity—a single bearer of *this* experience—and branch-relative accounts deliver determinate continuity facts too".
   - Hold the non-deflationary "I" as a **commitment, not a finding**. Tenets L121 says the Map concedes that "the indexical question is meaningful" is "itself a posited claim".
   - If the "future self as another person" framing appears (Strotz, Schelling, the nobleman), state that the Map's posit denies two subjects. Then say that this settles self-binding versus paternalism and does not settle authority.
   - Madhyamaka-style deflation (an aggregate with no further fact) stays a **bedrock disagreement** (tenets L121), not a refuted rival.
   - Do not present precommitment as evidence for persistence. The economic models run on any account of identity.
6. **Do not borrow the speculative temporal framework.** Do not connect binding to `time-collapse-and-agency` or to consciousness shaping time (`diachronic-agency` L101 flags that as speculative). Precommitment involves ordinary causal processes.
7. **Absence claims scoped** (see [Absence and Exclusivity Claims](#absence)).
8. **Psychiatric material.**
   - The SBD literature treats the ill and well person as one rights-holder with fluctuating capacity.
   - Do not describe the manic self as "not the person", and do not let "derangement" (Schelling's word) stand as the Map's.
   - The respondents' justification is distorted decision-making.

### Quote status {#quote-status}

**Cleared to quote** (raw-text grep, at the tag and page shown in [Key Sources](#key-sources)):
- **Strotz** (pp. 165, 173).
- **Bryan, Karlan & Nelson 2010** (pp. 672, 673, 684, 685, 693). The **2010 wording only**: "owing to intrapersonal conflict", not the working paper's "due to personal conflict".
- **Schelling 1980** (pp. 95–96, 96, 103–104). Restore the OCR's "'T'" to "'I'".
- **Dufner 2025 (SEP)** sentences.
- **Stroud & Svirsky 2025 (SEP)** for the absence count only.

**Cleared, page unverified** ([V-ocr]; cite chapter or section, not page, except ch. II's opening at p. 36):
- **Elster 1979:** the Ulysses passage, the "privileged way" thesis, conditions (i), (iii), (v), and the side-bets exclusion.
- **Elster 2000:** "not simply a new edition"; "Although that statement is too stark…"; the marriage retraction (in a note); "He intends to neutralize the effect of a preference change, not to prevent it."

**Quote only "as quoted in":**
- **Seip:** "In politics, people never try to bind themselves, only to bind others." **As quoted in Elster 2000, Preface.** Never attribute it to Elster.
- **Parfit's nobleman:** as quoted in Elster 2000, §I.6, citing Parfit (1973), p. 145. If the article quotes "I want you to think that I cease to exist", it must keep "He might add" or say that the nobleman says it.
- **Dworkin; Jaworska:** through Dufner 2025 only.
- **Steward 2012:** only the fragment `the-divided-will` L107 quotes ("essential to the very existence of such an agent", p. 161). The "must be able not to act on an intention already formed" clause is that page's gloss.

**Abstract wording only** ([V-abs]): Ashraf et al. 2006; Giné et al. 2010; John 2020; Carrera et al. 2022; Laibson 1997, 2015; Gergel & Owen 2015; Gergel et al. 2021; Spellecy 2003; Hyndman & Bisin 2026.

**Do not quote:**
- Holton 2004 or 2009 (bodies not read);
- Bratman 1998, 2007, 2018;
- Kavka 1983; McClennen 1990; Ainslie 1992;
- Laibson 1997's body ("selves");
- Dresser 1986 or 1995; Dworkin 1993; Jaworska 1999;
- Schelling 1984 (*AER*);
- Elster's list of precommitment devices (not retrieved as a list) or Table I.1 as a list;
- anything from Ariely & Wertenbroch 2002.

### Coiner and populariser

- **"Precommitment":** Strotz *named* "the strategy of precommitment" (p. 173) and put "precommit" in quotation marks at p. 165. **Whether he coined the word is unverified.** Write "Strotz named the strategy", not "Strotz coined the term". (A search summary credited him with the term. That is not evidence.)
- **The Ulysses emblem:** in this literature it predates Elster. Strotz's epigraph (1955–56) is the earliest found here, but this is **not established as the earliest overall**. Elster popularised it across philosophy and social science. Ashraf et al.'s 2006 title ("Tying Odysseus to the Mast") reuses it.
- **"Bind others, not themselves":** Seip (via Elster 2000).
- **The Russian nobleman:** Parfit (1973), not Elster. It reappears in Parfit 1984 around p. 325 (per Dufner).
- **"Commitment device," formal definition:** Bryan, Karlan & Nelson 2010, p. 673. They say a one-line definition "proved to be a difficult but enlightening task" (p. 673). Do not present any one-line gloss as theirs except p. 672's "Broadly…".
- **"Ulysses contract"** (psychiatry): no coiner verified. Dresser 1982, "Ulysses and the Psychiatrists", is a lead only.

### Term traps

- **"Self-binding"** on the Map already means Tenet 5's symmetric discipline (22 live files). In the article, prefer "binding oneself" or "precommitment". If "self-binding" is used, gloss it on first use (Elster's sense; SBDs).
- **"Pre-commit"** in `apex/` means pre-registering predictions. Do not link those pages as related.
- **"Commitment"** in Bratman and Holton (an intention as a commitment) is not a "commitment device" (a priced or removed option).
- **"Diachronic"** has three senses on the Map: Kennett's diachronic control (`self-control` L38), Strawson's "diachronic" people (`narrative-void`), and Bratman-style diachronic agency. Say which.
- **"Sophisticated" / "naive"** are O'Donoghue–Rabin technical terms for beliefs about one's own future preferences. Gloss them if used.
- **"Resolve"** is Ainslie 2021's, a resolution is Holton's, and precommitment is Elster's. They are distinct by Elster's condition (iii).

### Evidence not to lean on {#not-to-lean-on}

- **Ariely & Wertenbroch 2002: retracted.**
  - Do not cite it, even as "early evidence", except to note the retraction.
  - Do not import it through Bryan et al. 2010, pp. 680–681.
  - If the article wants a deadlines example, there is none verified here. Leave it out.
- **Commitment-device field effects.**
  - Real but modest (CARES +3 pp; SEED +81 pp in balances), with low take-up (11%, 28%).
  - Strong failure modes: John's 55% default; Carrera et al.'s mistargeting and lowered consumer surplus.
  - **No meta-analysis was consulted.** Write "mixed", with the specific figures, and no pooled effect.
- **SBD endorsement (82%)** comes from a self-selected charity sample with self-reported diagnosis. Do not generalise it.
- **Ego depletion.** Do not explain why binding helps by resource depletion. If it comes up, flag it in one clause and link [mental-effort](/concepts/mental-effort/).
- **The broad nudge literature** (SMarT, defaults). Its effect sizes are contested, and Bryan et al. treat SMarT as a soft commitment. Leave it out.

### Integration passages for the cross-review {#integration}

Headroom = hard − 1 − `analyze_length` total, measured 2026-10-23 about 23:15Z. Re-measure before editing.

| Host | Line | Total / hard → headroom | Suggested edit |
|---|---|---|---|
| `concepts/self-control-as-skill-and-scaffolding` | L108 (No Many Worlds) | 3,029 / 3,500 → **470** | One pointer clause after "the tension stays open": the article takes it up for binding devices (+~15 words). Optionally a piped link at zero cost on L66's "extrapsychic commitment". |
| `topics/akrasia-and-weakness-of-will` | L80 (Holton's resolutions) | 3,622 / 4,000 → **377** | One sentence contrasting a resolution (override retained, so it can be abandoned) with precommitment (override removed by an external device) (+~25) |
| `topics/diachronic-agency-and-personal-narrative` | L81 (Bratman's plans) | 3,442 / 4,000 → **557** | A clause after the plans-and-policies sentence: external binding as the fallback when plans alone will not hold (+~20) |
| `topics/the-divided-will` | L107 (Steward's settler) | 3,074 / 4,000 → **925** | Optional: precommitment as the settler suspending its own later settling (+~25) |
| `concepts/skill-delegation` | §"Phase 3: Retained Override Capacity" (L58) | 2,437 / 3,500 → **1,062** | Optional Further Reading entry: precommitment as the deliberate removal of override (+~15) |
| `topics/consciousness-and-neurodegenerative-disease` | L135 | 3,220 / 4,000 → **779** | Optional: advance directives as the practical form of the identity question (+~20) |
| `concepts/parfit-reductionism` | §"Parfit's Core Claims" (L37–47) | 2,532 / 3,500 → **967** | Optional: one sentence on the nobleman, with "He might add" kept (+~30) |
| `voids/cross-state-void` | L75 | 2,952 / 3,000 → **47** | **Zero-cost piped link only** on "Ulysses contracts". See also side-finding 3 (a possible direction slip in the same sentence). |
| `topics/personal-identity` | — | 4,033 / 4,000 → **past hard** | **No edit.** |
| `topics/emotion-regulation-and-the-timing-of-control` | Further Reading | 2,699 / 4,000 → 1,300 | Optional Further Reading entry. Created today, so leave body edits to its own cross-review. |

### Length

- Topics thresholds: soft 3,000, hard 4,000. The total counts the reference apparatus.
- Aim for **≤ 3,000 total**, roughly 2,300–2,500 prose plus 15–20 references.
- If the total passes 3,000, split prose from apparatus before any condense decision.

### Prose

- Avoid the "This is not X. It is Y." construct and the default intensifier "load-bearing" (CLAUDE.md).
- Lead with the Map's three answers (truncation resilience).
- Put the Map's interpretation under a sentence such as "This section gives the Map's interpretation; none of the authors above argues for it", as `self-control` L82 does.

## Absence and Exclusivity Claims (Scoped) {#absence}

1. **On the Map.** "precommit", "Elster", "Strotz", "commitment device", "Dworkin", "Dresser", "Kavka" and "McClennen" have **0 live hits**. "Ulysses" has one, a single sentence at `cross-state-void` L75. Positive controls: "Ainslie" 3, "Holton" 3, "Bratman" 4. Scope: live `topics/ concepts/ apex/ voids/ positions/`, 2026-10-23.
2. **SEP "Weakness of Will"** (Stroud & Svirsky, rev. 18 Sep 2025, raw HTML). Counts: "precommit" 0, "Ulysses" 0, "Elster" 0, against positive controls "Holton" 14, "Bratman" 9, "Ainslie" 7. **Scope:** this one entry. It does discuss "diachronic regulation and external scaffolding". Do not generalise this into "philosophers of weakness of will neglect precommitment".
3. **SEP "Personal Identity and Ethics"** (Dufner 2025, raw HTML). Counts: "Ulysses" 0, "precommit" 0, "Elster" 0. Controls: "advance directive" 11, "Parfit" 21, "nobleman" 1. **Scope:** this one entry.
4. **"Identity is not decisive" is Dufner's assessment**, scoped to the advance-directive debate ("not a lot of people have explicitly argued…"). It is not a literature-wide census. Attribute it to her.
5. **No "consensus" claim** is licensed about commitment-device efficacy or about the binder's authority.
6. **Strotz's priority** is scoped: the earliest economic use of the Ulysses image *found here*.
7. **The Map's distinctiveness claim** ("the one scaffolding strategy that removes the override") is scoped to the strategies the Map discusses: if-then plans, situation selection, Ainslie's four tactics, Holton's resolutions and skill delegation. It is a definitional consequence of Elster's (iii), not an empirical finding.

## Gaps in Research {#gaps}

- **Elster pages.** archive.org FTS gives wording without pages. Google Books gave no hits for these volumes even on the positive control "Ulysses", so those zeros mean nothing. Pages beyond ch. II's opening (1979) and the contents (2000) are unverified.
- **Parfit 1973 and 1984** were not read directly. The nobleman is as quoted in Elster 2000. Parfit's own conclusion about the wife's obligation was not read (Dufner's summary only).
- **Holton and Bratman** bodies are closed. The resolution/precommitment contrast rests on the akrasia page's existing account and Elster's definition.
- **Dworkin 1993, Dresser 1986/1995 and Jaworska 1999**: only as the SEP summarises them.
- **No meta-analysis of commitment devices** was consulted. John 2020 and Carrera et al. 2022 are abstracts only.
- **Kavka's toxin puzzle and McClennen's resolute choice** are leads. They would sharpen the "can one rationally intend against later reasons?" strand if the article wants it.
- **Ainslie (1992)** and Elster (ed.) 1986's Schelling and Ainslie chapters were not read.
- **Stephenson et al. 2023** (systematic review of SBD reasons): no abstract retrieved.
- **Dresser (1982)**, "Ulysses and the Psychiatrists": not verified.
- **Procrastination** (Andreou) is a separate later candidate (the review's "Ideas for Later"). It is not covered here.

## Side-Findings (leads only) {#side-findings}

1. **Retraction, no Map exposure.**
   - Ariely & Wertenbroch 2002 was retracted 2026-09-02, and the Map has 0 citations.
   - `voids/preference-void` leans on Ariely, Loewenstein & Prelec (2003, *QJE*) for coherent arbitrariness. That paper is not retracted as far as checked here.
   - Maniadis, Tufano & List (2014), "One Swallow Doesn't Make a Summer: New Evidence on Anchoring Effects", *AER* 104(1), 277–290, doi:10.1257/aer.104.1.277 [V-xref; abstract: it "explores the strength of certain anchoring results"], is a replication-and-caution paper that the void does not cite (0 hits).
   - **Lead for a literature-drift check of the void's single-study dependence. Do not assert a result.**
2. **Bryan et al. 2010 pp. 680–681** report the retracted study as lab evidence of demand for commitment. Any future Map citation of the review for "lab evidence" should skip that paragraph.
3. **`cross-state-void` L75: a possible direction slip.**
   - The sentence: "Ulysses contracts, advance directives and notes written during craving for the cold self transmit the hot self's *verdicts* without its weight".
   - Ulysses contracts and advance directives are drafted in the cold or well state to bind the hot one. Gergel & Owen's SBD is one "by which they commit themselves to treatment during future episodes of mania, even if unwilling". So these carry the **cold** self's verdict into the hot state. Only the craving notes carry the hot self's verdict out.
   - The same lumping is in [voids-cross-state-void-2026-09-24](/research/voids-cross-state-void-2026-09-24/) L178.
   - A possible fix (+~10 words, inside the 47-word headroom): "Ulysses contracts and advance directives carry the cold self's verdict into the hot state, and notes written during craving carry the hot self's out".
   - **Verify against the void's intent before editing.** The void may mean that the cold self encodes what it knows of past hot states.
4. **The self-control page's L108 cites Ainslie p. 93** through `the-divided-will` for "recursive self-prediction without literal future selves". That is consistent with Elster 1979's exclusion of private side bets, so the two pages need no reconciliation.
5. **`diachronic-agency-and-personal-narrative` L131 (Tenet 2):** "The impressive temporal coherence of diachronic agency emerges not from massive interventions but from sustained sequences of minimal selections". This leans on smallness and fewness. Compare tenets L69 (empirical-constraint minimality) and `self-control` L106's correction. **Low-priority lead.** The tenet's headline wording ("smallest possible") may license part of it. Read before tasking.
6. **Holton (2017),** "We don't torture: moral resolutions, temptation, and the doctrine of double effect", *Journal of the British Academy* 5. Possibly relevant to `akrasia` or moral-agency pages [Lead; search summary only].

## Citations {#citations}

1. Ainslie, G. (1992). *Picoeconomics: The Strategic Interaction of Successive Motivational States within the Person*. Cambridge University Press. [metadata via reviews]
2. Ainslie, G. (2001). *Breakdown of Will*. Cambridge University Press. https://doi.org/10.1017/CBO9781139164191
3. Ariely, D., & Wertenbroch, K. (2002). Procrastination, deadlines, and performance: Self-control by precommitment. *Psychological Science*, 13(3), 219–224. https://doi.org/10.1111/1467-9280.00441 — **RETRACTED** (2026), https://doi.org/10.1177/09567976261488042
4. Ashraf, N., Karlan, D., & Yin, W. (2006). Tying Odysseus to the mast: Evidence from a commitment savings product in the Philippines. *Quarterly Journal of Economics*, 121(2), 635–672. https://doi.org/10.1162/qjec.2006.121.2.635
5. Bratman, M. E. (1998). Toxin, temptation, and the stability of intention. In J. L. Coleman & C. W. Morris (Eds.), *Rational Commitment and Social Justice* (pp. 59–83). Cambridge University Press. https://doi.org/10.1017/cbo9780511527364.006
6. Bratman, M. E. (2018). *Planning, Time, and Self-Governance*. Oxford University Press. https://doi.org/10.1093/oso/9780190867850.001.0001
7. Bryan, G., Karlan, D., & Nelson, S. (2010). Commitment devices. *Annual Review of Economics*, 2, 671–698. https://doi.org/10.1146/annurev.economics.102308.124324
8. Carrera, M., Royer, H., Stehr, M., Sydnor, J., & Taubinsky, D. (2022). Who chooses commitment? Evidence and welfare implications. *Review of Economic Studies*, 89(3), 1205–1244. https://doi.org/10.1093/restud/rdab056
9. Dresser, R. (1986). Life, death, and incompetent patients: Conceptual infirmities and hidden values in the law. *Arizona Law Review*, 28(3), 373–405. [via SEP]
10. Dresser, R. (1995). Dworkin on dementia: Elegant theory, questionable policy. *Hastings Center Report*, 25(6), 32–38. https://doi.org/10.2307/3527839
11. Dufner, A. (2025). Personal identity and ethics. *Stanford Encyclopedia of Philosophy* (first published 30 June 2025). https://plato.stanford.edu/entries/identity-ethics/
12. Dworkin, R. (1993). *Life's Dominion: An Argument about Abortion, Euthanasia, and Individual Freedom*. New York: Knopf. [via SEP]
13. Elster, J. (1977). Ulysses and the Sirens: A theory of imperfect rationality. *Social Science Information*, 16(5), 469–526. https://doi.org/10.1177/053901847701600501
14. Elster, J. (1979). *Ulysses and the Sirens: Studies in Rationality and Irrationality*. Cambridge University Press. (Rev. ed. 1984.)
15. Elster, J. (2000). *Ulysses Unbound: Studies in Rationality, Precommitment, and Constraints*. Cambridge University Press. https://doi.org/10.1017/cbo9780511625008
16. Gergel, T., & Owen, G. S. (2015). Fluctuating capacity and advance decision-making in Bipolar Affective Disorder — Self-binding directives and self-determination. *International Journal of Law and Psychiatry*, 40, 92–101. https://doi.org/10.1016/j.ijlp.2015.04.004
17. Gergel, T., Das, P., Owen, G., Stephenson, L., Rifkin, L., Hindley, G., Dawson, J., & Ruck Keene, A. (2021). Reasons for endorsing or rejecting self-binding directives in bipolar disorder: A qualitative study of survey responses from UK service users. *Lancet Psychiatry*, 8(7), 599–609. https://doi.org/10.1016/S2215-0366(21)00115-2
18. Giné, X., Karlan, D., & Zinman, J. (2010). Put your money where your butt is: A commitment contract for smoking cessation. *American Economic Journal: Applied Economics*, 2(4), 213–235. https://doi.org/10.1257/app.2.4.213
19. Holton, R. (2004). Rational resolve. *Philosophical Review*, 113(4), 507–535. https://doi.org/10.1215/00318108-113-4-507
20. Holton, R. (2009). *Willing, Wanting, Waiting*. Oxford University Press. https://doi.org/10.1093/acprof:oso/9780199214570.001.0001
21. Hyndman, K., & Bisin, A. (2026). Replication of "Procrastination, Deadlines, and Performance: Self-Control by Precommitment". *Psychological Science*, 37(8), 557–571. https://doi.org/10.1177/09567976261460772
22. Jaworska, A. (1999). Respecting the margins of agency: Alzheimer's patients and the capacity to value. *Philosophy & Public Affairs*, 28(2), 105–138. https://doi.org/10.1111/j.1088-4963.1999.00105.x
23. John, A. (2020). When commitment fails: Evidence from a field experiment. *Management Science*, 66(2), 503–529. https://doi.org/10.1287/mnsc.2018.3236
24. Kavka, G. S. (1983). The toxin puzzle. *Analysis*, 43(1), 33–36. https://doi.org/10.1093/analys/43.1.33
25. Laibson, D. (1997). Golden eggs and hyperbolic discounting. *Quarterly Journal of Economics*, 112(2), 443–478. https://doi.org/10.1162/003355397555253
26. Laibson, D. (2015). Why don't present-biased agents make commitments? *American Economic Review*, 105(5), 267–272. https://doi.org/10.1257/aer.p20151084
27. Maniadis, Z., Tufano, F., & List, J. A. (2014). One swallow doesn't make a summer: New evidence on anchoring effects. *American Economic Review*, 104(1), 277–290. https://doi.org/10.1257/aer.104.1.277 [side-finding only]
28. McClennen, E. F. (1990). *Rationality and Dynamic Choice: Foundational Explorations*. Cambridge University Press. https://doi.org/10.1017/cbo9780511983979
29. O'Donoghue, T., & Rabin, M. (1999). Doing it now or later. *American Economic Review*, 89(1), 103–124. https://doi.org/10.1257/aer.89.1.103
30. Parfit, D. (1973). Later selves and moral principles. In A. Montefiore (Ed.), *Philosophy and Personal Relations* (pp. 137–169). London: Routledge & Kegan Paul. https://doi.org/10.1515/9780773593435-009
31. Schelling, T. C. (1980). The intimate contest for self-command. *The Public Interest*, Summer 1980, 94–118.
32. Schelling, T. C. (1984). Self-command in practice, in policy, and in a theory of rational choice. *American Economic Review*, 74(2), 1–11. [metadata via Bryan et al.; body not read]
33. Spellecy, R. (2003). Reviving Ulysses contracts. *Kennedy Institute of Ethics Journal*, 13(4), 373–392. https://doi.org/10.1353/ken.2004.0010
34. Stephenson, L., Gieselmann, A., Gergel, T., Owen, G., Gather, J., & Scholten, M. (2023). Self-binding directives in psychiatric practice: A systematic review of reasons. *Lancet Psychiatry*, 10(11), 887–895. https://doi.org/10.1016/S2215-0366(23)00221-3
35. Strotz, R. H. (1955–56). Myopia and inconsistency in dynamic utility maximization. *Review of Economic Studies*, 23(3), 165–180. https://doi.org/10.2307/2295722
36. Stroud, S., & Svirsky, L. (2025). Weakness of will. *Stanford Encyclopedia of Philosophy* (revision of 18 September 2025). https://plato.stanford.edu/entries/weakness-will/
37. Thaler, R. H., & Shefrin, H. M. (1981). An economic theory of self-control. *Journal of Political Economy*, 89(2), 392–406. https://doi.org/10.1086/260971