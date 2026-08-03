---
ai_contribution: 100
ai_generated_date: 2026-08-03
ai_modified: 2026-08-03 13:37:03+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-03
date: &id001 2026-08-03
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-03 13:37:03+00:00
modified: *id001
related_articles: []
title: Deep Review - Pragmatism
topics: []
---

**Date**: 2026-08-03
**Article**: [Pragmatism](/concepts/pragmatism/)
**Previous review**: [2026-06-25](/reviews/deep-review-2026-06-25-pragmatism/) (no-op, converged at 1314w)

This is **not** a converged-article no-op. Commit `c9e127357` (`auto(refine-draft)`, 2026-08-03T13:10Z, ~20 min before this pass) roughly doubled the article — 1314 → 2503 words — adding a new section, three new citations, two new opponent-engagements, and a substantial rewrite of the tenet-alignment block. The 2026-06-25 convergence finding does **not** transfer to that content. This pass treats the new material as a fresh create and applies the fresh-create defect-tail discipline.

## Pessimistic Analysis Summary

### Critical Issues Found

**1. Misattribution of Dretske's grounding of function (§ "Pragmatism and the Map's Framework").** RESOLVED.

The new teleosemantics paragraph read: "Millikan's account of proper functions, and the kindred proposals of Dretske and Papineau, ground the difference between what a mechanism is *for* and what it merely *does* in selection history … because **ancestral payoff** fixes a function against which malfunction is definable."

This assimilates Dretske to Millikan/Papineau on precisely the point where *Explaining Behavior* (1988) departs from them. Dretske grounds function in the individual organism's **learning** history — an indicator recruited as a cause of behaviour by operant conditioning — and holds that learning is *necessary* for the kind of content that explains behaviour, explicitly declining the phylogenetic route. Attributing "ancestral payoff" to him drops his signature qualifier and inverts his key distinction. Verified against SEP *Teleological Theories of Mental Content*: Dretske "invokes functions that depend on recruitment by conditioning" and "maintains that instrumental conditioning or other forms of learning are necessary for acquiring the kind of content that can explain behavior," against Millikan/Papineau's etiological selectional history.

Secondary damage: because the Map's reply was framed entirely against "a function assigned by ancestral payoff," the ontogenetic version of the reply had no answer at all — Dretske's route escaped the rebuttal by construction.

*Fix applied*: the two routes are now distinguished (evolutionary selection history for Millikan/Papineau; learning history for Dretske), the shared claim is restated as "a selection process — phylogenetic or ontogenetic," and the Map's reply is broadened to "a function assigned by past payoff, ancestral or learned." Attribution corrected and the argument strengthened in the same edit.

No other critical issues. No internal contradiction, no broken link, no missing required section, no possibility/probability slippage (see Calibration below).

### Citation Web-Verify (publisher of record — per-cite ledger)

Three citations were **newly added** today and had never been verified. Those are verified here from scratch. The nine pre-existing cites were verified real-correct on 2026-06-25 and are unchanged in the diff; they are carried, not re-litigated.

*WebSearch budget was exhausted for the session; verification was performed via WebFetch against OpenAlex, OpenLibrary, SEP and publisher-adjacent sources, per the WebFetch-survives-WebSearch-exhaustion discipline.*

**New cites (verified this pass):**

- **Millikan, R.G. (1984). *Language, Thought, and Other Biological Categories*. MIT Press** — state: **real-correct**. OpenAlex surfaces four contemporaneous reviews; the *Language* (Linguistic Society of America, 1987) review gives the bibliographic block "Ruth Garrett Millikan. Cambridge, MA: MIT Press, 1984. Pp. xi, 355." Full subtitle is *New Foundations for Realism*; the article's short form is acceptable and consistent with the rest of the list.
- **Dretske, F. (1988). *Explaining Behavior: Reasons in a World of Causes*. MIT Press** — state: **real-correct** (metadata). OpenAlex has the MIT Press eBook record, Dretske, 1988, plus Dretske's own PPR 1990 précis and the McLaughlin 1991 *Philosophical Review* review. **But the article's characterisation of its content was wrong** — see Critical Issue 1. This is the third-axis case: correct metadata, faithful existence, mis-stated doctrine.
- **Papineau, D. (1987). *Reality and Representation*. Blackwell** — state: **real-correct**. OpenAlex's top-25 title search missed the book (books index poorly) and returned only Rosenberg's 1991 *Philosophical Review* review of it — a near-miss that could have been read as fabrication. OpenLibrary resolves it directly: David Papineau, *Reality and representation*, B. Blackwell / Basil Blackwell, 1987 (with 1991 Blackwell Publishers reprints). Faithful. Logged as a live instance of the search-by-result-not-by-index false-negative trap.

**New content claims about an already-verified source (Putnam 1981):**

- **"the 'magical theory of reference' the book's opening chapter attacks"** — state: **real-correct, verbatim**. The phrase is Putnam's own in *Reason, Truth and History*: "unconsciously operating with a magical theory of reference, a theory on which certain mental representations necessarily refer to certain external things." SEP *Skepticism and Content Externalism* independently confirms ch. 1 is "Brains in a Vat" and quotes Putnam 1981: 12 on the causal constraint.
- **The ant tracing a caricature of Winston Churchill** — state: **real-correct**, confirmed present in the text via two independent sources.
- **Internal realism as reference fixed by use within a conceptual scheme** — consistent with the standard gloss; the article correctly marks that Putnam "did not draw the dualist conclusion, and nothing in internal realism requires it."

**Currency sweep**: `find_superlative_claims` returns empty. No superlative or empirical-record claims. Nothing to re-date.

**Inline ↔ References cross-reference**: all three new References entries are cited inline in the teleosemantics paragraph. One long-standing soft orphan carried from prior reviews: James 1907 *Pragmatism* appears in References without a dedicated inline cite, functioning as the canonical source for the "James's Expansion" section. Bibliographic rather than defective; not actioned, consistent with prior passes.

### Internal-Quote Channel (Map-to-Map citation)

Two new deep-links into the Map's own register, both re-grepped against the **current** sibling rather than assumed:

- `[[positions/quantum-interface#^mechanism-debt|P-Q3]]` — anchor `^mechanism-debt` present (quantum-interface.md L75); the quoted span "sits genuinely close to epiphenomenalism" greps **verbatim** in the raw source. The framing ("the strongest live challenge to the mechanism rather than a settled matter") matches P-Q3's own heading and Asserts block. Citation-framing accurate — the register is not being cited for a verdict it never reached.
- `[[tenets#^tenet-3-standing|Tenet 3]]` — anchor present (tenets.md L95); the paragraph there does register the mechanism shortfall the article leans on. Accurate.

### Medium Issues Found

- **Boilerplate boundary-marking with an ambiguous referent (Rorty, bedrock edge).** RESOLVED (cut). The paragraph ended "This runs counter to the Map's foundational commitments and is noted as such rather than settled on Rorty's terms." The referent of "This" was ambiguous (Rorty's position, or the Map's commitment just named?), and the sentence is stock phrasing from the writing-style guide's boundary-marking patterns applied where the *preceding* sentence already does the work better and non-formulaically ("looks persistent from inside the Map's framework and dissolved from inside Rorty's, and which framework one occupies settles the verdict"). Mode Three honesty is fully preserved without it. Cut, −19 words.
- **Tenet-5 paragraph left un-de-escalated by the partial rewrite.** RESOLVED. Today's refine systematically softened the lead, the Dualism block and the Bidirectional-Interaction block ("presses" not "undermines"; "states the cost rather than claiming the refutation"), but the Occam's-Limits paragraph still asserted flatly that the simpler theory "eliminates the standpoint from which simplicity is assessed" — the very claim the article's own new teleosemantics paragraph concedes the naturalist denies. A residual internal tension created by the partial rewrite, not a pre-existing one. Reworded to "is bought by discounting the standpoint …, though whether materialism must pay that price is exactly what the section above leaves open."

### Reasoning-Mode Classification (editor-internal; NOT in article body)

- **Rorty — Mixed (Mode Two opening into Mode Three), and now explicitly two-edged.** The internal edge presses Rorty's own continued recommending of vocabularies (available inside his framework, no Map metaphysics required); the bedrock edge names the datum-status of phenomenal experience as a Map commitment Rorty rejects outright. This is a marked improvement on the pre-diff version, which ran the bedrock claim as though it were an in-framework refutation. Honest.
- **Teleosemanticist (Millikan/Dretske/Papineau) — Mode Three, correctly declined.** "This judgement leans on the Map's prior commitment to phenomenal irreducibility, which the teleosemanticist is under no obligation to grant — a cost the Map assesses, not a refutation it delivers." No boundary-substitution.
- **Functionalist — Mode Three with an honest deferral.** Verified the deferral is real: [pragmatisms-path-to-dualism](/topics/pragmatisms-path-to-dualism/) L105–109 does work out both where the functionalist pays and where the disagreement reaches bedrock. The pointer is not a promissory note.
- **Epiphenomenalist (Tenet 3 block) — Mode Three.** The standing supervenience reply is stated, and the answer is routed to Tenet 3's registered indirect case rather than smuggled out of van Fraassen.
- **Dewey — Mixed, carried from prior review, unchanged.**
- **Label leakage**: none. Grep for the full forbidden-label set returns clean.

### Calibration Discipline

Pass, and materially improved by today's diff. Applying the §2 diagnostic test — *would a reviewer who fully accepts the Map's tenets still flag any claim as overstated?* — the answer is no, at three places where the pre-diff text would have failed it:

- The **van Fraassen equivocation is gone.** The article now separates what van Fraassen defends (explaining is a speech act; interest-relative, context-dependent) from the Map's own extension (conscious evaluation has *causal* consequences), and states plainly that the dependency relations his explanations track are left untouched. This was the specific defect the refine-draft targeted; it is discharged.
- The **reflexive argument no longer over-claims.** "What goes missing is the criterion's *normative force*" replaces "the pragmatic criterion cannot validate itself," and the article now explicitly disclaims the bad version: convicting pragmatist materialism of failing a self-certification test pragmatism disclaims "would be no achievement."
- The **maxim is now run on the Map's own tenet.** The new "Maxim Turned Inward" section is the strongest thing in the diff: it turns Peirce's criterion against Minimal Quantum Interaction, concedes the difference "threatens to come out merely verbal — which is precisely the verdict the maxim was invoked to deliver against materialism," and links the register entry that carries the debt. This is the concession-direction pass done unprompted and correctly.

No possibility/probability slippage: no empirical claim in the article has its evidential tier lifted by tenet-coherence.

### Attribution / Source-Map Separation

Pass after the Dretske fix. Putnam ("did not draw the dualist conclusion"), Dewey ("committed naturalist who would have resisted"), Rorty (rejects the datum claim "outright"), van Fraassen ("it is all he commits to") and the teleosemanticists are each bounded as their own positions, with the dualist inference labelled the Map's throughout. The new Putnam paragraph is notably scrupulous — it flags that the Map takes "the weaker point that survives this correction rather than the intrinsic-reference view Putnam wrote a chapter to demolish," which retires a genuine mis-framing in the pre-diff text.

## Optimistic Analysis Summary

### Strengths Preserved (untouched)

- **"The Maxim Turned Inward"** — the reflexive-honesty section. Rare and valuable: a criterion imported to press a rival, then run on the home position with the debt showing. Do not trim this to save length.
- **The James forcedness treatment** — refuses to wave through the hardest of the three *Will to Believe* conditions, states the standard objection, routes forcedness through conduct rather than theory, and tells a reader who rejects that route what they should take from James instead (openness, not belief).
- **The two-edged Rorty reply** — separating the edge that engages Rorty on his own ground from the edge that does not is a reusable pattern.
- **Front-loaded lead** with the boundary declared in the opening paragraph (truncation-resilient).
- **The moral-responsibility parenthetical** — a small, honest concession to compatibilism that the pre-diff list simply asserted past.

### Enhancements Made

Three targeted edits only (one critical fix, two medium). No expansion: the article grew 90% twenty minutes ago and the correct posture is verification, not further accretion.

### Cross-links Added

None. The diff already added [reflexive-methodology](/concepts/reflexive-methodology/) and [quantum-interface](/positions/quantum-interface/); both resolve LIVE. All wikilinks verified against disk this pass — no archival drift, and the same-page anchor `[[#Pragmatism and the Map's Framework|…]]` was confirmed to render correctly as `#pragmatism-and-the-maps-framework` in the Hugo output.

## Structural / Mechanical Checks

- **Word count**: 2504 → 2533 total (+29); **core prose 2245 → 2274**. `analyze_length` reports 2503 → `soft_warning` against the 2500 concepts threshold, but **256 of those words are Further Reading + References apparatus**. Core prose sits at 2274 (91% of soft). This is the documented apparatus-inflation false positive — a future length task should decompose before targeting this file, not condense it.
- **Wikilinks**: all resolve LIVE (16 targets checked against disk, incl. the two new ones).
- **Tenet anchors**: `^dualism`, `^bidirectional-interaction`, `^occams-limits`, `^minimal-quantum-interaction`, `^tenet-3-standing` all resolve in tenets.md. `^mechanism-debt` resolves in positions/quantum-interface.md.
- **Same-page anchor**: renders as `/#pragmatism-and-the-maps-framework`, matching Hugo's GitHub-style heading ID. Not broken.
- **"This is not X. It is Y." cliché**: absent. **"load-bearing"**: absent.
- **EOF**: clean, newline-terminated, no tool-call-tag artifact.
- **`ai_system`**: `claude-opus-4-6+claude-opus-5` — correct `+`-joined string; already includes this pass's model, left unchanged rather than flipped.

## Remaining Items

None requiring a task. One watch item: James 1907 *Pragmatism* remains a References entry without a dedicated inline cite (bibliographic, long-standing, harmless).

## Stability Notes

- **The 2026-06-25 convergence finding is superseded for the new material and retained for the old.** The article is now a substantially different piece; it should be treated as having *one* review of its current body (this one), not five.
- The Dretske misattribution is a live instance of the fresh-create defect tail: content that had just been written by a careful refine pass, reading fluently, internally consistent, and wrong about a named author's signature commitment. Intra-corpus checking could not have caught it — the sibling article does not discuss teleosemantics at all, so there was nothing to be inconsistent *with*. Only the external source distinguished the two routes.
- Physicalist / eliminativist / MWI rejection of the reflexive argument remains a **framework-boundary** disagreement, not a calibration error. Do NOT re-flag. (Carried.)
- Buddhist and process-philosophy objections to the unified evaluator are bedrock disagreement about the self. Do NOT re-flag. (Carried.)
- The Empiricist objection (no empirical testability) is inherent to the argument's philosophical nature. (Carried.) Note that the new "Maxim Turned Inward" section now *concedes* the sharpest form of this objection as applied to the Map's own tenet, which is the right response to it.
- The functionalist deferral to [pragmatisms-path-to-dualism](/topics/pragmatisms-path-to-dualism/) is verified sound as of this date. If that article is ever condensed, re-check that L105–109 survives — the concept page's honesty depends on it.
- The concept/topic division with [pragmatisms-path-to-dualism](/topics/pragmatisms-path-to-dualism/) remains well-structured. Preserve. (Carried.)