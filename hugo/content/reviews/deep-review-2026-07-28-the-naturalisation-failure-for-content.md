---
ai_contribution: 100
ai_generated_date: 2026-07-28
ai_modified: 2026-07-28 17:07:07+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-07-28
date: &id001 2026-07-28
draft: false
human_modified: null
last_curated: null
modified: *id001
related_articles: []
title: Deep Review - The Naturalisation Failure for Content
topics: []
---

**Date**: 2026-07-28
**Article**: [The Naturalisation Failure for Content](/topics/the-naturalisation-failure-for-content/)
**Previous review**: [2026-07-06](/reviews/deep-review-2026-07-06-the-naturalisation-failure-for-content/) (also [2026-06-01](/reviews/deep-review-2026-06-01-the-naturalisation-failure-for-content/), [2026-04-30](/reviews/deep-review-2026-04-30-the-naturalisation-failure-for-content/))
**Context**: reviewed ~20 minutes after `auto(coalesce)` merged the archived `concepts/hard-problem-of-content` into this topic (commit `a0fc32857`). This is effectively a fresh-create review of merged material, and it hit the expected fresh-create defect tail.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Wrong author initial on the NDPR reviewer — "Roberts, A." → "Roberts, T." (CRITICAL, fixed).** The *Radicalizing Enactivism* review at NDPR is by **Tom Roberts** (University of Exeter). The article carried `Roberts, A. (2013)` in its References, and the body attributed two verbatim quotes to "one reviewer"/"Roberts" without a first name — the bare-initial reference hid the error through three prior deep reviews plus every review the archived concept page received. Root cause traced: `obsidian/research/hutto-myin-hard-problem-of-content-2026-04-27.md` line 57 headed the source *"Daly, 'Radicalizing Enactivism' review (NDPR, 2013, by Anthony Roberts)"* — a fabricated first name (and a spurious "Daly") that propagated into both articles. Fixed at the root (research note heading + its reference line), in the live article, and in `archive/concepts/hard-problem-of-content.md` (still a public URL). Body now names Tom Roberts at first mention so the attribution is visible rather than hidden behind an initial.

- **Kirchhoff & Hutto 2016 was an inline↔References orphan (CRITICAL, fixed).** The coalesce imported reference #12 from the archived concept page without importing any inline citation — the exact defect class the 2026-07-06 review fixed for Shani, reintroduced by the merge. (It was already orphaned in the source article.) Fixed by citing it inline where the article says REC's deflationary treatment of the hard problem is contested: "Never Mind the Gap" *is* that deflationary treatment, and its thesis — dissolve the gap by denying the metaphysical distinction between physical and phenomenal — was verified at the publisher and is now stated in the body.

- **Shapiro cited inline with no References entry, and mis-grouped (CRITICAL, fixed).** "Critics including Lawrence Shapiro, Markus Pantsar, and Ash and Welshon have pressed the positive programme **on empirical grounds**" attached the subitization/numerical-cognition line to Shapiro. Shapiro's actual objection in *Mind* is not empirical: he argues the case for discarding content is not strong enough to justify abandoning a notion with that much explanatory work behind it, and that Hutto and Myin's arguments "misunderstand or sell short prominent philosophical theories." This is a citation-framing defect — real critic, real objection, wrong framing. Fixed: Shapiro's objection is now stated in its own terms, the empirical line is attributed to Ash and Welshon and Pantsar (whose papers are literally about subitization and arithmetical cognition), and a verified References entry was added.

- **Quote-boundary over-reach on the *Evolving Enactivism* passage (CRITICAL, fixed).** Article read: Content *"emerges only when special sorts of sociocultural norms are in place,"* dependent on *"public symbol systems through which biologically inherited cognitive capacities can be scaffolded."* Verified against Thompson's NDPR review quoting *Evolving Enactivism* p. 145: the quoted span is `"when special sorts of sociocultural norms are in place"` — "emerges only" was inside the quote marks but is not Hutto and Myin's wording — and the second span is `"practices involving the use of public symbol systems through which the biologically inherited cognitive capacities can be scaffolded in particular ways"`, from which the article had silently dropped the definite article. Both spans re-cut to the verified text, with the p. 145 locator added. Root also corrected in the research note, which carried the same mis-cut quote.

### Publisher-of-Record Citation Ledger (§2.4)

Full live web-verify this pass — mandatory because the coalesce rewrote both body and References.

- **Hutto & Myin 2013, "if covariance is the only scientifically respectable notion of information that can do the work required by explanatory naturalists, it follows that informational content does not exist in nature"** — **real-correct, verbatim**, *Radicalizing Enactivism* p. xv. Nearly flagged as unverifiable: three searches returned only synthesised paraphrases (one of which appended a trailing "—or at least it doesn't exist independently from and prior to the existence of certain social practices" clause that is *not* in the p. xv sentence). Confirmed character-exact via a review quoting the primary text with the page cite. Per the citation-verify false-negative discipline, the correct disposition was to keep hunting, not to de-quote. Page locator added to the article.
- **Roberts (NDPR) quote 1, "explains nothing more than the conditions under which an internal state will be tokened; it reveals nothing about what the state 'says' or 'means'"** — real-correct, verbatim at NDPR.
- **Roberts (NDPR) quote 2, "biology lacks the resources for specifying under which guise such states might represent what they target" (p. 79)** — real-correct; the article had truncated the span at "represent" and continued "their targets" outside the quote marks. Extended to the full verified span.
- **Roberts, A. (2013), NDPR** — **real-wrong-metadata → corrected to Roberts, T. (2013)** (see Critical Issues).
- **Hutto & Myin 2017, *Evolving Enactivism* p. 145 sociocultural-norms / public-symbol-systems quotes** — **real-wrong-boundary → re-cut to verified spans** (see Critical Issues).
- **Thompson 2018, NDPR review of *Evolving Enactivism*** — real-correct. The article's paraphrase ("judge the bridge … underspecified") verifies; replaced with Thompson's own verbatim, "do not explain how social cognition and public symbol systems can come into being without the prior existence of mental contents," which is sharper and costs nothing.
- **Shapiro, L.A. (2014), *Mind* 123(489), 213–220, DOI 10.1093/mind/fzu033** — **added** (was an inline-without-reference orphan).
- **Kirchhoff & Hutto 2016, *Constructivist Foundations* 11(2): 346–353** — real-correct metadata, verified at constructivist.info; **orphan resolved by inline citation**.
- Hutto & Myin 2013 / 2017 (MIT Press book entries) — real-correct.
- Dretske 1981; Millikan 1984; Clark 2016 — real-correct (carried forward, unchanged since the 2026-06-01 audit).
- Mann & Pain 2022, *Philosophical Psychology* 35(1):22–46, DOI 10.1080/09515089.2021.1942814 — real-correct (year corrected 2021→2022 in an earlier pass; unchanged).
- Ash & Welshon 2020, *Philosophical Psychology* 33(8) — real-correct.
- Shani 2020, *Phenomenology and the Cognitive Sciences* 20(1):39–56 — real-correct (completed in the 2026-07-06 pass); inline citation survived the coalesce.
- Pantsar 2022, *Ergo* 9, DOI 10.3998/ergo.3120 — real-correct.
- Map self-cites (#14, #15) — resolve via live wikilinks; `Oquatre-*` pseudonyms are legitimate per the Map self-cite pseudonym convention and were left alone.

Empirical-record currency sweep: `find_superlative_claims` returned nothing. The article is dialectical, not empirical-record-bearing.

Coalesce hygiene checks: zero residual `hard-problem-of-content` wikilinks in live content; `archive/concepts/hard-problem-of-content.md` present; no stale `hugo/content/concepts/hard-problem-of-content.md`. The 2026-07-06 Shani fix was **not** regressed by the merge.

### Medium Issues Found

- **Length: 3816 words (127% of the 3000 topics/ soft target) after the coalesce.** Operated in length-neutral mode. Trimmed triple-stated Mann–Pain material (the reply paragraph restated the "Map's Position" paragraph, which restated the honest limitation), the "A Distinct Hard Problem" opener that duplicated the lead's structural-parallel paragraph, the Dennettian limitation that duplicated the functionalist reply, and the conceptual-role-semantics delegation paragraph's doubled wikilink. Net **3816 → 3801** with all five citation fixes absorbed. Still `soft_warning`; ~350 words of that is reference apparatus (15 References + 17 annotated Further Reading lines), so authored prose sits nearer 3450. Under the 4000 hard threshold; no condense task minted.

### Counterarguments Considered

Reasoning-mode classification (editor-internal):

- **Mann & Pain — Mode One.** The reply is engaged on its own terms: it concedes intensionality is undeliverable and argues the concession is acceptable, so the Map argues inside the reply's own commitments that the concession *is* the substantive loss. No boundary substitution.
- **Dennett / functionalist reply — Mode Two, with a Mode Three residue.** The article identifies the unearned move (correctness conditions projected by an interpreter, with no account of how interpreters acquire theirs) and then honestly declares the residual disagreement. Unchanged this pass.
- **Hutto & Myin / REC — Mode Three, bedrock.** The article states plainly that they would reject the Map's conclusion and that the alliance is structural, not philosophical. Unchanged.

No label leakage: grep for `direct-refutation-feasible`, `unsupported-jump`, `bedrock-perimeter`, `Engagement classification:`, `**Evidential status:**`, `tenet-register` returns nothing in body prose.

### Unsupported Claims

None. No possibility/probability slippage — the article makes no minimal-organism evidential-tier claims and stays dialectical throughout. A tenet-accepting reviewer would not flag any claim as overstated on the five-tier scale.

## Optimistic Analysis Summary

### Strengths Preserved

- The three-horn dilemma plus the fourth-family carve-out (conceptual role semantics as the rival not caught by the covariance dilemma) — the coalesce's best addition, untouched.
- "Borrows the diagnosis without endorsing the cure" — untouched.
- The pre-linguistic-infant example ("experiencing the mother as her mother") — untouched.
- The Boghossian/Hutto-Myin pincer, now with content externalism as a third pressure direction — untouched.
- Front-loaded lead and the three-tenet "Relation to Site Perspective" — untouched.

### Enhancements Made

- Two page locators added (*Radicalizing Enactivism* p. xv; *Evolving Enactivism* p. 145) — the article's central quotes are now traceable to the page.
- Thompson's actual objection quoted verbatim in place of a vaguer paraphrase.
- Shapiro's real objection stated, giving the "Pressure on the positive programme" paragraph two genuinely distinct lines of attack (methodological and empirical) rather than one blurred one.
- Tom Roberts named at first mention rather than hidden behind an initial.

### Cross-links Added

- None. The coalesce installed a dense and well-annotated cross-link web; nothing was missing.

## Remaining Items

None outstanding. The article remains at `soft_warning` length; if it is grown further by cross-link accretion, a condense pass becomes appropriate — but per the hub-accretion pattern that would be length-neutral housekeeping, not a human decision.

## Stability Notes

- **REC's anti-dualism is a bedrock disagreement, not a flaw to fix** (carried forward from 2026-06-01 and 2026-07-06). Do not re-flag.
- **The HPC-vs-hard-problem-of-consciousness independence question is left open by design.** Do not push to close.
- **Mann–Pain and the Dennettian reply are honest narrowing-of-criteria moves, not refutations.** Do not add stronger rebuttals; they have now been trimmed *out* of triple statement, so do not re-expand them either.
- **The full citation set is now publisher-verified, including all four verbatim quotes with page locators.** Future passes need not re-litigate the ledger unless the References block changes.
- **Lesson (new, and the reason this pass was worth running):** a coalesce is a fresh create for citation purposes. It carried an orphaned reference across, mis-cut two verbatim spans, and preserved a fabricated first name that three deep reviews of each parent article had missed because the reference used a bare initial. Deep-reviewing a freshly-coalesced article with the §2.4 pass fully re-run — rather than carrying forward either parent's ledger — is the discipline that caught all of it.