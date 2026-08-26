---
ai_contribution: 100
ai_generated_date: 2026-08-26
ai_modified: 2026-08-26 21:23:03+00:00
ai_system: claude-fable-5
author: null
concepts: []
created: 2026-08-26
date: &id001 2026-08-26
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-26 21:23:03+00:00
modified: *id001
related_articles: []
title: Deep Review - Akrasia and Weakness of Will (2026-08-26)
topics: []
---

**Date**: 2026-08-26
**Article**: [Akrasia and Weakness of Will](/topics/akrasia-and-weakness-of-will/)
**Previous review**: [2026-07-09](/reviews/deep-review-2026-07-09-akrasia-and-weakness-of-will/) (verification-only, same-session as create)
**Trigger**: candidate selector (score 74; `ai_modified` bumped 2026-08-26 by embed-videos). Changes since the previous review were cosmetic only — `topics:` slug normalisation (2026-08-02), `anchoring_audit_exempt` key (2026-07-16), YouTube embed (2026-08-26). Body and References were untouched between the two reviews.

## Pessimistic Analysis Summary

### Critical Issues Found
None. The 2026-07-09 calibration verdict holds: the lead and the Relation to Site Perspective section both state that akrasia is "not a proof of dualism" and that "a physicalist can accept every word" of the exposition. No possibility/probability slippage; no label leakage (grep for the forbidden editor-vocabulary terms returned nothing).

### Medium Issues Found (all fixed this pass)
- **Hare's position under-reported (attribution fidelity).** The article rendered Hare's prescriptivist reply as "failing to do y shows the judgement was not really held", dropping his other disjunct. SEP's live text: "any apparent case of akrasia must in fact be one in which the agent is actually unable to do *a*, or one in which the agent does not genuinely evaluate…". Fixed: the sentence now carries both disjuncts (inability, or an "ought" that has shed its prescriptive force), the qualifier "when one could have done it", and a locator to *Freedom and Reason* ch. 5 "Backsliding". Hare 1963 added to References (it was an inline attribution with no bibliographic entry).
- **Empirical-record currency on Holton's willpower evidence.** The article said Holton "draws on empirical self-control research" and that willpower is "empirically studied", with no note that the ego-depletion strand of that research collapsed under preregistration (Hagger et al. 2016, 23 labs, N=2,141, d=0.04). The current SEP entry itself records that "the older 'ego depletion' model of willpower has increasingly come under question". Fixed: one calibrating passage added to the Holton section, naming Mischel and Baumeister as the sources Holton draws on, citing Hagger 2016 in the corpus-canonical form already used by [mental-effort](/concepts/mental-effort/) and [attention-as-causal-bridge](/apex/attention-as-causal-bridge/), and stating what survives (Holton's structural claim about resolutions and a distinct, trainable capacity) versus what weakened (the limited-resource model of what that capacity consumes). Cross-link to [mental-effort](/concepts/mental-effort/) added.
- **"demonstrably" overstated the datum** (RTSP: "akrasia is the case where it demonstrably does not [track evaluations]"). The article's own Socratic section says the datum's reality is contested, so "demonstrably" was an internal tension a tenet-accepting reader would flag. Softened to "by the agent's own report".
- **References claimed Bekker numbering but none appeared inline.** Added "(VII.3, 1147a)" at the sleeper/drunk passage, the one place a locator does work.
- **Description was 173 characters** (schema: 150–160). Trimmed to 159 without losing the calibration clause.

### Citation web-verify ledger (publisher of record; raw-text grep, not confirmation prompts)
- Plato, *Protagoras* 358b–c quote — **real-correct**. Grep-verified against the raw HTML of the live SEP entry: "No one," he declared, "who either knows or believes that there is another possible course of action, better than the one he is following, will ever continue on his present course" (*Protagoras* 358b–c). The article's ellipsis stands in for "he declared" — faithful.
- Davidson 1980, p. 42 quote — **real-correct**. Raw SEP text: "what is the agent's reason for doing [b] when he believes it would be better, all things considered, to do another thing, then the answer must be: for this, the agent has no reason" (p. 42). The article's `[b]` matches SEP's own bracketed substitution; its ellipsis replaces "all things considered" — faithful.
- Davidson 1980 (*Essays on Actions and Events*, Essay 2, pp. 21–42, OUP; orig. Feinberg ed. *Moral Concepts* 1969/1970) — **real-correct**, unchanged since 2026-07-09 ledger (reprint metadata confirmed then at Oxford Academic; the 1969/1970 hedge is legitimate).
- Holton 2009, *Willing, Wanting, Waiting* — **real-correct**. SEP bibliography lists it as Oxford: Clarendon Press (an OUP imprint; the article's "Oxford University Press" is not wrong). Web-verified this pass that Holton's strength-of-will argument draws on Mischel and Baumeister and that the ego-depletion capacity "has been identified with willpower by both psychologists (Baumeister & Vohs, 2007) and philosophers (Holton, 2009)" — licenses the new currency sentence as a claim about Holton's sources rather than an invented link.
- Stroud, Sarah & Svirsky, Larisa (2025), "Weakness of Will", SEP — **real-correct**. Raw page: "First published Wed May 14, 2008; substantive revision Thu Sep 18, 2025"; copyright line names both authors.
- Aristotle, *NE* VII (practical syllogism; "have and not have" as sleeper/drunk) — **real-correct**; locator VII.3, 1147a now given inline.
- **New — Hare, R. M. (1963), *Freedom and Reason*, Oxford: Clarendon Press, ch. 5 "Backsliding", pp. 67–86** — **real-correct**. SEP bibliography lists the book; Oxford Academic's chapter page confirms "Backsliding" in *Freedom and Reason* at pp. 67–86 with the psychological-incapacity / off-colour-"ought" reply the article now reports.
- **New — Hagger, M. S., Chatzisarantis, N. L. D., et al. (2016), "A Multilab Preregistered Replication of the Ego-Depletion Effect", *Perspectives on Psychological Science* 11(4), 546–573, doi:10.1177/1745691616652873** — **real-correct**. Crossref works record: title, container, 2016-07, vol. 11 iss. 4 pp. 546–573, 64 authors led by Hagger and Chatzisarantis. Family resolution: entry written in the same form the corpus already uses in [concepts/mental-effort.md](/concepts/mental-effort/) and [apex/attention-as-causal-bridge.md](/apex/attention-as-causal-bridge/), so no new variant was minted.
- Superlative/empirical-record scan (`find_superlative_claims`): empty. Currency sweep therefore ran on the one implicit empirical claim (willpower "empirically studied") rather than on a superlative; see the Holton item above.
- Inline ↔ References cross-check after edits: Aristotle, Davidson, Hagger, Hare, Holton, Plato, SEP all cited inline and listed; the two Map self-cites (Southgate & Oquatre-*) are the standing pseudonym convention, left intact. No orphans either way.

### Counterarguments Considered
- *Socratic/Harean denial that the datum exists* — bedrock at the level of philosophy of action, and the article does not try to refute it; it treats the datum as contested. Unchanged.
- *Physicalist reading of the selection language as functional description* — conceded in the article itself; bedrock. Unchanged.
- *Popperian: "empirically studied willpower" leans on a literature that partly failed replication* — the one non-bedrock objection this pass found, and the one it acted on.

## Optimistic Analysis Summary

### Strengths Preserved
- Front-loaded four-position summary; exemplary exposition-before-interpretation structure; triple-hedged RTSP that names each naturalistic escape route (Socrates, Davidson, Holton) by name.
- The Hardline Empiricist persona's reading: the article already declines to let tenet-coherence elevate an empirical claim; this pass extends that restraint to the Holton evidence base rather than adding any pro-Map weight.

### Enhancements Made
- Hare disjunct restored with locator; Bekker locator for Aristotle; ego-depletion currency note; "demonstrably" softened; description trimmed to schema length.

### Cross-links Added
- [mental-effort](/concepts/mental-effort/) (the corpus's home for the Hagger 2016 result and the felt-effort/resource dissociation).

## Reasoning-mode classification (editor-internal; not in article body)
- Socratic/Harean denial — Mode Three (framework-boundary marking): the article declines to refute the denial and records that the datum's existence is contested. Honest; no upgrade available without importing a phenomenological premise the deniers reject.
- Physicalist functional reading of the selection model — Mode Three, explicitly conceded ("a physicalist can accept every word"). Correct as written.
- Davidson and Holton are not opponents here; they are naturalistic accounts the article endorses as the shared ground.

## Word count
2170 → 2332 (+162; topics/ soft threshold 3000, status ok). Not in length-neutral mode.

## Remaining Items
None.

## Stability Notes
- Carried from 2026-07-09: physicalist/functionalist readings of the selection language are a bedrock framework-boundary matter, not a defect; and any impulse to "argue the selection model more strongly" would reintroduce the phenomenal-absence over-claim the article is built to avoid. Do not act on it.
- New: the ego-depletion caveat is deliberately scoped to *what the capacity consumes*, leaving Holton's structural claim intact. A future review that wants to expand the replication-crisis material should send it to [mental-effort](/concepts/mental-effort/), not here — this article is about the philosophy of action, and one calibrating passage is the right dose.
- The two quotes have now been grep-verified against raw SEP HTML in two independent passes. Re-verify only if the SEP entry's revision date changes from 2025-09-18.

## Sync
`scripts/sync.py` run after edits; Hugo copy at `hugo/content/topics/akrasia-and-weakness-of-will.md` carries the same body.