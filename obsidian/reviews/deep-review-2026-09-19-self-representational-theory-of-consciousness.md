---
title: "Deep Review - The Self-Representational Theory of Consciousness"
created: 2026-09-19
modified: 2026-09-19
human_modified:
ai_modified: 2026-09-19T18:15:00+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-09-19
last_curated:
---

**Date**: 2026-09-19
**Article**: [[self-representational-theory-of-consciousness|The Self-Representational Theory of Consciousness]]
**Previous reviews**: [[deep-review-2026-07-26-self-representational-theory-of-consciousness|2026-07-26 (deep)]]; [[deep-review-2026-07-20-self-representational-theory-of-consciousness|2026-07-20 (deep)]]; [[deep-review-2026-07-13-self-representational-theory-of-consciousness|2026-07-13 (deep)]]; [[pessimistic-2026-07-14-self-representational-theory|2026-07-14 (pessimistic)]]

**Delta since last review**: one paragraph, installed 2026-09-18 by a `refine-draft` pass (the possibility/probability-slippage guard closing §The Drift Toward Acquaintance). References block unchanged since 2026-07-20.

**Lens run this pass**: source-fidelity against raw text. The 2026-07-20 ledger verified every citation's *metadata* at the publisher of record and the 2026-07-26 pass skipped §2.4 by trigger. Neither pass opened the cited sources to check whether they say what the article reports. That is the lens run here, and it found the article's single most-repeated attribution to be unsupported by its own cited source.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Levine does not gesture toward acquaintance in the cited review — the word never occurs in it.**

- **Locus (was)**: §The Standard Objections — "In the review Levine gestures toward **acquaintance** rather than representation as the relevant primitive, though the piece is a review of Kriegel rather than a statement of Levine's own constructive metaphysics."
- **Method**: fetched `ndpr.nd.edu/reviews/subjective-consciousness-a-self-representational-theory/` raw, stripped tags, NFKC-normalised, de-hyphenated (35,324 chars — the full review through its reference list and footnotes). `acquaint` / `Acquaint`: **0 occurrences**. Positive controls in the same extraction: `subjective character` 22, `Trinity` 3, `awareness relation` 1. The zero is a real absence, not a truncated read.
- **Provenance**: this sentence was installed by commit `994be1e42e` (refine-draft, 2026-07-14) in response to pessimistic-2026-07-14 Issue 5a, which had correctly flagged the stronger form ("Levine's own preferred primitive is acquaintance") as going beyond the review. The recommended repair was to *soften* to "gestures toward." The softening changed the claim's strength but left its content false, and the 2026-07-20 deep review recorded Issue 5a as **"Resolved."** The 2026-07-20 ledger verified that the NDPR URL is live — metadata, not reading. This is [[citation-ledger-ratifies-the-reading-not-just-the-metadata]] exactly: three subsequent passes ratified a claim none of them checked against the text.
- **Resolution applied**: replaced with Levine's actual argument and two verbatim quotations from the review — his rejection of the machinery ("neither the appeal to cross-order integration nor to indirect representation works," offset 23811/25611 region) and his conclusion ("the awareness relation involved in conscious experience cannot be explicated in terms of representational states, at least not reductively, as one must either sacrifice the phenomenology or sacrifice the representation relation," offset ~32925). Bullet retitled **The unity dilemma (Levine)**. The new text states explicitly that Levine names no replacement primitive.

**2. The conceivability framing of Levine's objection is also absent from the review.**

- **Locus (was)**: "A state that represented itself non-derivatively, specifically, and essentially yet had no felt character seems conceivable; if so, self-representation is not sufficient for phenomenality."
- **Method**: same extraction. `conceiv`: **0**; `zombie`: **0**. The review *does* contain Kriegel's (SR) formula with "non-derivatively, specifically, and essentially" (offset ~9820) — so the vocabulary is Levine's, but the conceivability argument built from it is not. Levine's three declared lines of attack are the argument for abandoning two-state theory, the account of qualitative character, and the ontological structure of conscious states; none is a conceivability argument.
- **Resolution applied**: removed; the bullet now reports the dilemma Levine actually runs.
- **Dependent repaired**: §The Standard Objections opening sentence read "Levine's gap rests on a conceivability intuition" — a calibration concession installed by the 2026-07-14 pessimistic pass (Issue 1, downgrading "jointly decisive"). Cutting the conceivability framing would have stranded it. The concession is preserved on a true basis: "Levine's verdict rests on his own judgement that no representational relation could supply the unity conscious awareness exhibits." Defeasibility retained, source-fidelity restored.

### Medium Issues Found

**3. Williford was listed among the objections while his cited paper answers them.**

- **Locus (was)**: "Kenneth Williford — himself a defender — catalogues three regress arguments the self-awareness thesis faces."
- **Problem**: the bullet sat inside a list the article calls "jointly sufficient to decline the reduction." Williford 2019 raises the three regresses *in order to dissolve them* via a self-acquaintance postulate. Crediting him with an objection he answers is the pattern flagged in this session's driver notes.
- **Resolution applied**: the bullet now says he raises them to answer them, and identifies what Kriegel actually inherits — "not an unanswerable regress but an answer that costs him the representational thesis." This is both accurate to Williford and *stronger* for the Map, since it makes the acquaintance drift the immediate consequence of the regress answer rather than a separate observation.
- Also corrected: the third regress is Williford's "Fichte-Henrich-Shoemaker Regress of **de se belief**," not "of first-person reference."

**4. Kriegel's synchrony speculation was reported as his strategy, making the Map's reservation over-fire.**

- **Locus (was)**: §The Core Thesis — components "integrated into a single state by synchronous firing"; §Relation to Site Perspective — "Kriegel's naturalisation **leans on** binding-by-synchrony … a theory whose reduction is **hostage to** a contested integration mechanism."
- **Method**: Levine's review describes the actual commitment at offset ~24185: Kriegel "proposes that just this sort of integration occurs between the first-order and the second-order representations … (hence he calls this 'cross order integration'), and **he speculates that synchronous firing could be the mechanism** that implements the integration."
- **Problem**: the article promoted a named speculation into the load of the naturalisation, which inflated the Map's own empirical reservation. A tenet-accepting reviewer would still flag it.
- **Resolution applied**: §Core Thesis now names cross-order integration as the commitment and synchrony as what "he speculates … might implement" it. §Relation to Site Perspective keeps the reservation but re-bases it honestly: integration needs *some* mechanism, synchrony is the only candidate offered, and "a reduction whose only proposed integration mechanism is contested inherits that fragility." The reservation survives without the overstatement.

**5. The Zahavi critique had no source in References that contains it.**

- **Problem**: the body attributes to Zahavi the claim that pre-reflective self-awareness is "not representational at all," pressed *against* Kriegel. The only Zahavi entry in References was Zahavi & Kriegel (2015), "For-me-ness: What it is and what it is not" — a **jointly authored** chapter in which the two agree that for-me-ness is constitutive of conscious mentality. A reader following the reference finds agreement, not the critique.
- **Resolution applied**: body now cites *Subjectivity and Selfhood* (2005) inline; added as References entry 13 (MIT Press, DOI 10.7551/mitpress/6541.001.0001, verified at Crossref). The 2015 chapter is retained — it is correctly used elsewhere for the for-me-ness framing.

### Low Issues Found

**6. Publisher-summary quotation reshaped its own punctuation.** The article quoted conscious states as ones that "always represent themselves, whereas unconscious ones do not" — but OUP's description reads "whatever else they may represent, conscious mental states always represent themselves **(**whereas unconscious ones do not, at least not in the right way**)**." The article had converted an opening parenthesis into a comma inside the quotation marks and moved the closing qualifier outside as editorial gloss. Meaning preserved, punctuation not. Now quoted verbatim in full, with "The parenthetical qualifier matters" as the bridge.

### Citation Web-Verify Ledger (§2.4)

Reading-level verification (leg 7 result-direction and leg 8 cited-author-stance). Metadata was fully ledgered on 2026-07-20 and the References block has not changed; what follows re-verifies what the sources *say*.

- Levine, J. (2010), NDPR review — **real-wrong-reading (corrected)**. Metadata correct, URL live. Two claims attributed to the review are absent from it (`acquaint` 0/35,324; `conceiv` 0). Body rewritten against the raw text; two verbatim quotations substituted. Author stance: Levine's conclusion is anti-reductionist about the awareness relation, which the article may cite — he does not endorse acquaintance in this piece.
- Kriegel, U. (2009), *Subjective Consciousness* — **real-correct**; publisher summary now quoted verbatim (issue 6). The (SR) formula "non-derivatively, specifically, and essentially self-representing" confirmed against Levine's review at offset ~9820.
- Kriegel, U. (2009), synchrony claim — **real-wrong-reading (corrected)**: a speculation reported as the strategy (issue 4).
- Kriegel & Williford (eds.) (2006), *Self-Representational Approaches to Consciousness*, MIT Press — **real-correct**. Publisher description presents the view "as an alternative to the two dominant reductive theories … the representational theory of consciousness and the higher-order monitoring theory," which is exactly the article's "distinct *third* camp, standing against both first-order representationalism and higher-order monitoring."
- Gennaro, R. J. (2012), *The Consciousness Paradox* — **real-correct**, and the quoted phrase is now verbatim-sourced. IEP's "Higher-Order Theories of Consciousness" (entry authored by Gennaro himself) reads: the wide intrinsicality view "which he takes to be **a version of HOT theory**" (offset 47353, `iep.utm.edu`, 75,395-char extraction). The same passage confirms the article's contrast: for Gennaro "the **(unconscious)** HOT is … intrinsic to the target state."
- Weisberg, J. (2008), *Synthese* 160(2):161-181, DOI 10.1007/s11229-006-9106-0 — **real-correct**, direction confirmed: Weisberg "argues that despite appearances, the same-order theory fails to avoid this objection and also has troubles with intimacy." Matches the article's rendering and the "cuts both ways" dilemma.
- Williford, K. (2019), *ProtoSociology* 36:368-412 — **real-correct metadata, stance corrected** (issue 3). Abstract: the three regresses "can all be resolved by a self-acquaintance postulate," entailing that consciousness has an "irreducibly circular **structure**" and that self-acquaintance is "a realized relation-instance relating to itself as well as to something other than itself." The article had compressed these into a single quoted noun phrase, an "irreducibly circular" *relation-instance*; §The Drift now renders both parts as the source has them. Publisher-of-record page (pdcnet.org) is paywalled behind an SSO redirect; abstract verified via the publisher's indexed listing.
- Giustina, A. (2022), *Philosophical Studies* 179(12):3831-3863 — **real-correct**. Crossref DOI 10.1007/s11098-022-01868-5, single author Anna Giustina, 2022-09-23. (A separate Crossref record, 10.1007/s11098-022-01891-6, is the published correction at 179(12):3865 — noted, not cited.)
- Kriegel, U. (2024), "Knowledge-by-Acquaintance First", *PPR* 109(2):458-477 — **newly added, real-correct**. Replaces the article's unsourced "Kriegel's own recent work engages increasingly with acquaintance." ⚠️ A WebSearch summary asserted this paper is co-authored with Anna Giustina. **Both** Crossref (DOI 10.1111/phpr.13051) and OpenAlex list a **single author, Uriah Kriegel**. The search summary's co-author was not propagated.
- Zahavi, D., & Kriegel, U. (2015) — **real-correct but mis-tasked** (issue 5); Zahavi (2005) added.
- Brentano, F. (1874/1995) — **real-correct**, unchanged; the article's own "standardly claimed, not held" caution already guards the lineage.
- Shadlen & Movshon (1999), *Neuron* 24(1):67-77 — **real-correct**, unchanged.
- Aristotle, *De Anima* — "we perceive that we see and hear" verbatim-verified in the 2026-07-13 and 2026-07-20 passes; text unchanged, not re-litigated.

**Empirical-record currency sweep**: `find_superlative_claims` returned **0** claims. Nothing to age-check.

**Inline ↔ References cross-check**: clean. Every named cite resolves; entries 13 and 14 are both cited inline (Zahavi 2005 in §The Standard Objections, Kriegel 2024 in §The Drift Toward Acquaintance).

**Wikilink resolution**: all ten targets resolve to live files, including `possibility-probability-slippage` from the 2026-09-18 insertion. No push-blocker.

### False alarms — checked and cleared

- **Rosenthal on targetless HOTs** (the article's single Rosenthal mention, and the one the driver notes flagged as least cross-checked). The article says he "accepts that such 'targetless' higher-order thoughts still produce experience." A search summary of Rosenthal's *Analysis* 71(3):431-437 (2011) reply to Block states the reverse — that he denies one is in any conscious state in virtue of such a HOT. The Stanford Encyclopedia settles it in the article's favour: "Both Lycan (1996) and Rosenthal (2005) are sanguine in the face of this objection. Each allows that targetless higher-order representations are a possibility … and each opts to say that **the subject in such a case is phenomenally conscious**." The two are reconcilable — Rosenthal denies there is a conscious *state* (nothing exists to be conscious) while holding that what it is like for the subject is fixed by the HOT — and the article's "produce experience" tracks the second, which is the phrasing SEP uses. **No edit.** The corpus's sibling treatment at `concepts/higher-order-theories.md` L69 says the same thing and is equally sound.
- **SEP files self-representational accounts under higher-order theories** — confirmed; the entry's §6 is titled "Self-Representational and Hybrid Higher-Order Theories" and refers to "'self-representational' higher-order theories." IEP §5 does the same. **Real-correct.**
- **Parsimony / Tenet 5 guard** — `grep -iF` for `simpl`, `parsimon`, `Occam` over the article returns **0**. The article awards itself no simplicity verdict, so the corpus-standard Tenet 5 guard has nothing to attach to. No unguarded "ours is simpler" family member here.
- **Calibration register** — the 2026-09-18 slippage paragraph, the "jointly sufficient / not a single knock-down" framing, the non-representational ≠ non-physical ≠ causal-relatum ladder, and the felt/dark fork's conditionality on phenomenal realism are all intact and none was re-inflated by this pass. The Map's verdict sentence is unchanged.

### Reasoning-Mode Classification (§2.6)

- **Engagement with Kriegel: Mode One** (defective on its own terms), now better supported. The unity dilemma is Levine's internal objection, and issue 4's repair makes the empirical leg internal too — Kriegel needs an integration mechanism by his own lights, and the one he offers is contested.
- **Engagement with Levine: not an opposition** — Levine is cited in support and his stance is now stated accurately, including that he stops short of the Map's further steps.
- **Engagement with Williford and Giustina: Mode Three** (framework-boundary marking), unchanged and correct — the article states plainly that they are primitivists offering a naturalistic monism and that neither takes the Map's metaphysical steps.
- **Engagement with the reductionist on the felt/dark fork: Mode Three**, explicitly conditional on phenomenal realism. Unchanged.
- **Label leakage**: none. No editor vocabulary in the body; no "This is not X. It is Y." construct introduced; no bare "load-bearing."

## Optimistic Analysis Summary

### Strengths Preserved
- The taxonomy section's substantive question — "is the awareness-conferring component itself conscious?" — remains the best thing in the article and is now doubly sourced (IEP confirms both the Gennaro quote and the unconscious-HOT reading).
- The Brentano-lineage caution, untouched.
- The acquaintance-drift calibration ladder and the 2026-09-18 slippage paragraph, untouched.
- The closing verdict sentence, untouched.

### Enhancements Made
- Two verbatim Levine quotations replace a construction attributed to him. The article is now *more* concrete about why the reduction fails, not less.
- The Williford repair makes the regress objection and the acquaintance drift one argument instead of two adjacent observations.
- "Kriegel's own recent work engages increasingly with acquaintance" — a vague unsourced trend claim — is now a specific sourced one (PPR 2024).

### Cross-links Added
None. Existing wikilink set is dense and appropriate; frontmatter membership unchanged.

## Length

2351 → 2563 words (+212). Section thresholds concepts/ 2500 / 3500 / 5000. Status moved `ok` → `soft_warning`; 937 words below hard. The pre-improvement measurement was 2351 (`ok`), so §4.5 normal mode applied. The growth is almost entirely the two verbatim Levine quotations substituted for the unsupported paraphrase, which cannot be made shorter without losing the verification that justifies them. Four tightening passes recovered ~40 words from the new prose. A future `condense` pass should look at the lead/§Relation-to-Site-Perspective overlap on "re-sites the hard problem" rather than at the quotations.

## Remaining Items

None deferred.

## Stability Notes

Carried forward from the 2026-07-20 and 2026-07-26 notes, still valid:
- **Taxonomy handling** (third-camp vs HOT-variant) — correct, and now verbatim-sourced at IEP. Do not re-flag.
- **Weisberg** — "Josh," not "Jonathan"; title takes "representation," not the aggregator's "representational." Direction of his argument confirmed this pass.
- **Acquaintance-drift framing** — deliberately hedged to "suggestive." Do not re-inflate to concession or vindication.
- **Felt/dark fork** — a valid conditional given phenomenal realism. The residual Churchland/Dennett resistance is bedrock framework-boundary disagreement, not a correctable calibration error.
- **The Zahavi tension** — a genuine framework-boundary standoff, honestly hedged. Bedrock, not slippage.

New for this pass:
- **Levine's role is now fixed to what the review contains.** The review is a purely negative result about representation. Do not re-attribute acquaintance, a conceivability argument, or any positive primitive to it. If a future pass wants Levine on acquaintance, it must cite Levine's *own* constructive work, not the NDPR review.
- **Binding-by-synchrony is Kriegel's speculation, not his commitment.** The Map's reservation is that it is the only candidate offered, not that the reduction depends on it. Do not restore "leans on" or "hostage to."
- **Williford answers the regresses; he does not press them.** Do not restore him to the objections column.
- **Kriegel 2024 PPR "Knowledge-by-Acquaintance First" is single-authored.** A web search summary claims Giustina as co-author; Crossref and OpenAlex both disagree. Do not add her.
- ⚠️ **Method note for this article's successors.** Three prior passes marked the Levine attribution resolved without opening the review. The distinguishing move this pass made was fetching the raw text and running a `grep -F` with *positive controls* before trusting a zero. The References block being stable is a reason to skip re-verifying *metadata*, never a reason to skip verifying *readings*.
