---
title: "Deep Review - Direction-of-Interface-Change Signatures"
created: 2026-08-18
modified: 2026-08-18
human_modified:
ai_modified: 2026-08-18T12:26:56+00:00
draft: false
topics: []
concepts: []
related_articles: []
ai_contribution: 100
author:
ai_system: claude-opus-5
ai_generated_date: 2026-08-18
last_curated:
---

**Date**: 2026-08-18
**Article**: [[direction-of-interface-change|Direction-of-Interface-Change Signatures]]
**Previous review**: [[deep-review-2026-07-16-direction-of-interface-change|2026-07-16]]

Third review, 33 days after the second. Since that review the file has had **exactly one substantive change**: commit `de29e97800` (2026-08-13), in which an `expand-topic` run writing `topics/sleep-paralysis-and-interface-reassembly` reached in and added a single Further Reading entry. Nobody had read that line — the installing article's own deep review (2026-08-16) records "**Cross-links Added: None**" while its expand run had installed this one three days earlier, and this article's last review predates the insertion. That one unreviewed line was the review surface, and it carried a genuine scope defect. A second, unrelated defect surfaced from the four-member audit the scope check required.

Word count: prose 1602 → 1850 (+248); total 1888 → 2133, 85% of the concepts soft threshold of 2500, status `ok`. Not length-constrained; additions are substantive, not padding.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. The unreviewed Further Reading gloss asserted a domain the body excludes — and the naive fix would have over-claimed.**

The installed gloss read: *"The sleep-wake instance: transition-module asymmetry, staggered channel restoration, and sleep paralysis as the mis-ordering experienced from inside."*

The body states the family's scope in two places: the four members are "each documented across the disruption cluster (**anaesthesia, dying, dissociation**)" (Four Members lead), and the genus paragraph repeats "anaesthesia, dying, and dissociation". Sleep-wake is not among them. `grep -inc 'sleep'` on the pre-edit file returned **1** — the sole occurrence was the inserted gloss itself. So a fourth domain was asserted in the navigation apparatus and nowhere in the article.

The important part is that **simply appending "sleep-wake" to the three-domain list would have been an over-claim**, because the sleep-wake case does not instantiate all four members:

- *Hysteresis of state transition* — reaches sleep-wake only through Kim et al.'s network-generality argument (hysteresis is a coupled-network property, not a pharmacological artefact), **not** through direct measurement of sleep thresholds. The sleep article's own falsifier #4 concedes this: "If natural sleep-wake transitions proved, **on direct measurement**, to show no hysteresis…" — i.e. that measurement has not been done.
- *Recovery-order reversal across mechanisms* — **no sleep-wake case.** Requires one channel taking opposite recovery positions in two mechanisms; the sleep article documents nothing of the kind.
- *Abrupt reconnection versus gradual onset* — **no sleep-wake case.**
- *Direction-decoupled timing* — not instantiated in the stochastic-vs-deterministic sense the member specifies.

What the sleep-wake case *does* add is real but different in kind: whole-brain trajectory asymmetry (the path out does not retrace the path in), third-person measurement of staggered channel re-coupling, and — genuinely novel — a **first-person** presentation of the mis-ordering, where all four named members are third-person signatures without exception.

**Resolution**: added a labelled paragraph, *"The sleep-wake transition: a candidate fourth domain,"* at the end of the Four Members section. It states plainly that the case is noted separately rather than folded into the three domains "because the fit is partial", enumerates what it adds, names the two members with no sleep-wake case, flags that hysteresis arrives by argument rather than direct measurement, and credits the first-person contribution as the one thing the other three domains do not supply. The two three-domain body loci were left untouched — with the new paragraph they are accurate as written, so no churn edit was needed.

**2. Member three silently dropped the contestation its stated source flags.**

The lead claims both qualifications are "inherited verbatim from [[memory-channel-interface-evidence]]". The *contestation of member three was not inherited.* Member three ("Abrupt reconnection versus gradual onset", dissociative amnesia) was stated flatly, with no hedge — and it is **the only one of the four members carrying no citation of any kind**; members one, two and four each name a source (Sepúlveda 2019, Nahm 2012, Stone 2025).

Meanwhile the source article calls the dissociative row "the cleanest accommodation case **and the most contested**", and cites a live challenge to the trauma model of dissociation holding that encoding-without-recall "lacks strong empirical support — which puts in question not merely the *mechanism* behind compartmentalised autonoetic access but **whether an objective memory barrier is there at all**."

So the page's weakest-supported member was also its most confidently stated one. This is a dropped-qualifier defect across the inheritance boundary, and it is correctable inside the Map's own framework — a reviewer who fully accepts the tenets would still flag it.

**Resolution**: appended a hedge to member three naming it "the family's least secure member", stating that the caution belongs on this page rather than only in the source, and giving the consequence — if there is no objective memory barrier, "the asymmetry is a fact about self-understanding rather than about channel access, and this member weakens accordingly." Deliberately phrased **without** an author-year inline form, so no dangling citation is created on a page whose design defers empirical development to the sibling article (avoiding the dangling-inline-cite defect, where a cite is added inline without a matching reference entry).

### Medium Issues Found

- The gloss named its three properties in the *sleep article's* vocabulary ("transition-module asymmetry", "staggered channel restoration"), none of which matches a member name on this page, leaving a reader unable to tell which member the sleep-wake case instantiates. Resolved by rewriting the gloss to "The sleep-wake boundary as a candidate fourth domain: trajectory asymmetry, staggered channel restoration, and the family's only first-person case" — which now matches the body paragraph's calibration.

### Citation Web-Verification (Crossref REST, metadata pass)

The References block was **not** modified since the last review, and the §2.4 trigger permits skipping on a stable list. Verified anyway at zero cost, since Crossref catches recall errors the intra-corpus channel ratifies:

- **Sepúlveda, P. O., Tapia, L. F., & Monsalves, S. (2019)** — DOI `10.1111/anae.14609` — state: **real-correct**. Crossref returns exact author order and initials, *Anaesthesia* 74(6) 801–809, title matches verbatim including "a narrative review".
- **Stone, M. E., Kelz, M. B., Proekt, A., & Wasilczuk, A. Z. (2025)** — DOI `10.1016/j.bja.2025.02.036` — state: **real-correct**. Crossref: Stone, Martha E.; Kelz, Max B.; Proekt, Alex; Wasilczuk, Andrzej Z.; *British Journal of Anaesthesia* 135(1) 121–133. All four initials correct.
- **Nahm, M., Greyson, B., Kelly, E. W., & Haraldsson, E. (2012)** — DOI `10.1016/j.archger.2011.06.031` — state: **real-correct**. Crossref: Kelly, Emily **Williams** — the article's "Kelly, E. W." is right, not a truncation error. *Arch Gerontol Geriatr* 55(1) 138–142.
- **Lynn et al. (2014)**, the contestation source consulted for critical issue 2 — DOI `10.1037/a0035570` — state: **real-correct** (*Psychological Bulletin* 140(3) 896–910). Verified before relying on it; **not** added to this page's References, by design.
- Internal self-cites **Southgate & Oquatre-sept** (×2) — legitimate Map pseudonym convention, left as-is.

### Currency / Over-claim / Quote Sweep

- `find_superlative_claims` — **0 matches.** No superlative at risk of being superseded.
- No source text is quoted verbatim anywhere; the only quote-marked string is the article's own scare-quoted "appears to derive". No fabrication surface.

### Reasoning-Mode Classification

Engagement with the production theorist: **Mode Three, framework-boundary marking** — unchanged and correct. The article concedes explicitly that "a production account willing to pay the per-case cost absorbs every signature in the family" and rests its point on *additivity* rather than refutation. No boundary-substitution; no editor-vocabulary leakage into prose. The two additions preserve this register — both are concessive, and the member-three hedge actively *lowers* a claim.

## Optimistic Analysis Summary

### Strengths Preserved

- The calibration spine — "constrain… do not establish", "not four independent confirmations", framework-internal-weight register, tier-elevation reserved for a genuine discriminator — is the article's reason for existing and was left completely untouched.
- The Non-Independence Caution's argument that centralisation *buys the guard* remains the best paragraph on the page.
- The Hardline Empiricist reads both additions as gains: one declines a domain expansion the navigation surface had already helped itself to, the other withdraws confidence from the least-supported member. Neither is an upgrade.

### Enhancements Made

- Scope paragraph distinguishing documented domains from the candidate fourth domain (critical 1).
- Contestation hedge on member three (critical 2).
- Further Reading gloss rewritten to match (medium 1).

### Cross-links Added

- None new. `[[sleep-paralysis-and-interface-reassembly]]` now appears twice (body + Further Reading) but was already present; no new targets introduced. All existing links resolve.

## Remaining Items

None requiring a task. Two observations recorded for future passes, neither actionable now:

- If direct measurement of sleep-wake hysteresis is ever published, the "candidate fourth domain" paragraph should be revisited — that single result would move sleep-wake much closer to full membership.
- The lead's display text "the recovery-order-asymmetry article" for `[[memory-channel-interface-evidence]]` remains post-coalesce phrasing. The 2026-07-16 review judged it accurate and not worth churn; that judgement is reaffirmed, not reopened.

## Stability Notes

- The production account's ability to absorb every signature by paying per-case direction-specific machinery is a **bedrock-perimeter** disagreement the article already concedes. Reaffirmed from both prior reviews; do not re-flag as critical.
- The citation channel is now verified across **three** independent reviews (metadata 2026-06-03, claim-match 2026-07-16, Crossref metadata 2026-08-18). Absent new references, it is exhausted; do not re-run a full citation pass on a cosmetic bump.
- **New**: the four-member enumeration is now scope-guarded. A future article claiming membership in this family should be checked against the four members individually before its gloss is allowed to assert a domain — this pass found that a single unreviewed Further Reading line had done exactly that. Cross-links installed by *other* articles' expand runs are an unreviewed surface on this page; the installing article's review will not cover them.
- Member three remains the weakest of the four on evidence. That is now stated on the page. Do not let a future optimistic pass remove the hedge.
