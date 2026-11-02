---
ai_contribution: 100
ai_generated_date: 2026-11-02
ai_modified: 2026-11-02 14:36:07+00:00
ai_system: claude-opus-5-5
author: null
concepts: []
created: 2026-11-02
date: &id001 2026-11-02
draft: false
human_modified: null
last_curated: null
lastmod: 2026-11-02 14:36:07+00:00
modified: *id001
related_articles: []
title: Deep Review - Against Functionalism
topics: []
---

**Date**: 2026-11-02
**Article**: [Against Functionalism](/arguments/functionalism-argument/)
**Previous review**: [2026-09-21](/reviews/deep-review-2026-09-21-functionalism-argument/) (no-op; it did not bump `last_deep_review`, so the frontmatter still read 2026-07-18). Intervening substantive passes: refine-drafts `ed8bb35cca` (09-21, two bibliography entries), `f419ae21e3` (09-24, L199 impossibility claim narrowed), `8b2d0344fa` (10-23, strong-Revelation water-analogy reply rewritten to weak Revelation).

## Budget

`analyze_length`: **3527 → 3496** (−31). Section `arguments/`, soft 2500 / hard 3500, gate `>=`. The article entered this review at `hard_warning` (over since the 09-21 bibliography repair) and leaves at `soft_warning` with 3 words of headroom. Per the 09-21 stability note, the over-length was answered mainly from the apparatus and by fixes that happened to delete words, not by cutting reviewed argument.

## Pessimistic Analysis Summary

### Critical Issues Found

1. **Chalmers's master-argument dilemma was misrendered, and horn 2 did not follow (L167).** The article read: *"if they are inconceivable, zombies have C too—same concepts, same apparent gap—so C cannot explain why we find consciousness puzzling."* Chalmers's own horn 2 (2007, §3.2, verified from the author's PDF at consc.net/papers/pceg.pdf by text extraction and grep) runs: (4) if P&~C is not conceivable, zombies satisfy C; (5) **zombies do not share our epistemic situation**; (6) so C cannot explain our epistemic situation. He defines an epistemic situation as "the truth-values of their beliefs and the epistemic status of their beliefs", and says that "the real work in this argument is done by premise (5)". The intuition he gives is that a zombie twin's corresponding beliefs are false, "or at least... less justified than my beliefs". The article's version dropped premise (5). It gave zombies "the same apparent gap", which on its own makes the inference to "C cannot explain why we find consciousness puzzling" a non sequitur. It also echoes the reply Carruthers and Veillet make to Chalmers. **Fixed:** horn 2 now reads *"zombies have C too, yet their beliefs about consciousness are false or less justified, so C cannot explain our epistemic situation."* The next sentence, "Carruthers and Veillet (2007) dispute the explanandum it turns on", now has a stated explanandum. (+6 words.)
2. **Leftover strong Revelation (old L161).** The 10-23 refine rewrote the water-analogy reply to weak Revelation and conceded that the result depends on contested modal rationalism. It left the next line in place: *"The conceivability of zombies reflects our positive grasp of phenomenal consciousness, not ignorance of it."* The "not ignorance" clause is the strong-Revelation conclusion that `concepts/revelation-thesis` L38 rules out ("it contradicts the Map's own claims that consciousness is partly opaque to itself"). It also restates the dualist verdict straight after the paragraph has conceded it. A grep of `obsidian/` finds this the only locus. **Fixed:** the sentence is deleted (−15). It was original February text, and no review installed it (`git log -S` → `bb89a12042`, a sync fix; zero hits in `reviews/` and `todo.md`).
3. **The two legs were said to share "no premise" (L229).** The same paragraph and table row 5 call Argument 5 "Argument 1's observation without the possibility claim … not a separate confirmation". `positions/arguments-for-dualism` [P-D1](/positions/arguments-for-dualism/#p-d1), which the article links twice, says the explanatory gap and the zombie argument "press the same gap" and "fail together" if that common starting point fails. A reviewer who accepts the tenets would flag "sharing no premise" as overstating independence. **Fixed:** *"two legs sharing only the gap observation"* (+2). The optimistic reviews of 08-03 and 08-08 praised the dependency accounting as a strength. This edit tightens that accounting and does not reverse it.
4. **Tenet 3 stated as actual in the Relation to Site Perspective section (Bidirectional, old 4th sentence).** *"Consciousness adds something—selection among quantum possibilities—that the functional story misses."* `tenet-check-2026-09-25` Family S listed this verbatim against `tenets.md` `^tenet-3-standing`, and nobody acted on it. The 10-29 tenet repair ("that is where the Map holds consciousness acts") had not reached this paragraph either. The sentence repeated sentence 2, which already says "the Map holds". **Fixed:** deleted (−13). The paragraph still ends on the tenet's requirement.

### Medium Issues Found

- **Argument 3's lead overstated Searle's target (L101).** It said the Chinese Room "directly targets functionalism's implications for AI consciousness", while L107 (the 07-31 Issue 3 repair) says Searle's target is intentionality and "no premise above concerns what a state is like". Earlier fixes had already repaired L107. **Fixed:** "targets functionalism's implications for [machine understanding](/topics/ai-consciousness/)" (−1).
- **The phenomenal concepts strategy was conflated with the Type-A reply (L165).** "explains why zombies *seem* conceivable" reads as the "zombies aren't really conceivable" objection the article answers separately. Chalmers notes that conceivability is "an assumption that type-B materialists typically grant". **Fixed:** "seem" → "are" (0).
- **No Many Worlds section (L211).** It asserted "Consciousness involves selection of a particular outcome" outside the "the Map insists" scope (the same Tenet-3 family as item 4), and closed with "exactly what functionalism cannot capture". **Fixed** by moving the one-outcome claim inside the Map's insistence and dropping the intensifier (−6).
- **Navigation labels.** `[[ai-consciousness]]` "Why computers probably aren't conscious" covered every computer, while the destination's lede scopes to current AI and says "not proof that artificial consciousness is impossible in principle". The label is now "Principled obstacles facing current AI". `[[haecceity]]` "Why functional equivalence doesn't ensure experiential equivalence" described a page that explicitly separates the phenomenal difference from the haecceity question (its L75). The label is now "What makes a subject *this* one". `[[continual-learning-argument]]` "fail consciousness criteria" now reads "Why frozen-weight LLMs likely lack consciousness", matching the destination's "very likely lack". `[[concepts/functionalism]]` was shortened.
- **Inline/reference apparatus.** "Chalmers presses a dilemma" carried no year, and the only Chalmers entry was 1996, which does not contain the 2007 master argument. **Fixed:** "Chalmers (2007)" with a bibliography entry, metadata verified at Crossref (DOI 10.1093/acprof:oso/9780195171655.003.0009: Chalmers, D. J., "Phenomenal Concepts and the Explanatory Gap", *Phenomenal Concepts and Phenomenal Knowledge*, OUP 2007, pp. 167-194; editors Alter & Walter per the corpus canonical form). **Funded by removing the Hoel (2026) entry.** The 09-21 review recorded Hoel as the article's reverse orphan, never named in the body, and the body reaches it through `[[continual-learning-argument]]`, whose lede names Hoel's paper. The 09-21 review rated that orphan "defensible" when the article had headroom. With the article over the gate, the swap keeps a cite the body depends on and drops one it does not.
- **Unsourced empirical sentence (L89, "local factors rather than one global factor").** The claim is faithful: the Emery, Volbrecht, Peterzell & Webster (2023) *PNAS* abstract, via OpenAlex, reads "multiple independent factors limited to different local regions of color space". Its source sits in `concepts/inverted-qualia` §Twenty-First-Century Colour Science. **Fixed at zero word cost** with a piped link to that section. No inline cite was added, given the budget.

### Citation Ledger (§2.4)

- Block, N. (1978) "Troubles with Functionalism", *Minnesota Studies* 9, 261-325: **real-correct** (SEP cites the 1980 reprint; the original venue and pages are standard).
- Chalmers, D. (1996) *The Conscious Mind*: **real-correct** (carried).
- Chalmers, D. (2007) "Phenomenal Concepts and the Explanatory Gap": **real-correct, newly added**; Crossref-verified. **The paraphrase was wrong** (critical item 1) and is fixed.
- Searle, J. (1980) *BBS* 3(3), 417-424: **real-correct** (SEP gives 417–457, which includes the commentaries; 417–424 is the target article).
- Jackson, F. (1982) *Phil. Quarterly* 32(127), 127-136: **real-correct** (SEP bibliography).
- Carruthers & Veillet (2007) *JCS* 14(9-10), 212-236: **real-correct** (carried from the 09-21 OpenAlex check). The clause "dispute the explanandum it turns on" matches `concepts/phenomenal-concepts-strategy` L97 (their equivocation charge: zombie and twin share the epistemic situation).
- Hardin (1988): **real-correct** (carried).
- Tallis (2024) *Philosophy Now* 161, 58-59: **real-correct**. Left untouched, per the 09-21 note on its equilibrium.
- Frankish (2016) *JCS* 23(11-12), 11-39: **real-correct** (carried).
- Graziano (2024) *eNeuro* 11(10): **real-correct** (carried from the 09-21 raw-source grep).
- Hoel (2026) arXiv:2512.12802: **real-correct** (arXiv: v1 submitted 14 Dec 2025, v3 19 Jan 2026, so 2026 is the current version's year). **Removed from this article's apparatus** as a reverse orphan (see Medium).
- Emery et al. (2023) *PNAS* 120(4): result direction verified (local factors). Reached through the inverted-qualia link and not cited here.
- `find_superlative_claims`: 0 hits.
- Result-direction leg: horn 2 was the one paraphrase whose logical direction failed, and it is fixed. Chalmers's horn 1 ("C is not physically explicable … these features will generate a gap of their own") is faithful.
- Cited-author stance: Chalmers is a property dualist, correctly presented as pressing a dilemma that "has not closed the debate". Frankish and Graziano are illusionists presented on their own terms. Carruthers & Veillet are physicalists, cited as opponents.

### Map-internal claims re-checked

- `revelation-thesis` L36: weak Revelation means "the existence of a quality and part of its character". It matches L159's "an experiential quality exists and part of its character".
- `positions/arguments-for-dualism` `^p-d1` exists and supports "one dependency, not two". It drove critical item 3.
- `decoherence` L167 ("the live status of the … dispute") and `quantum-biology-and-neural-mechanisms` ("leading but unsettled model") support "Neither treats it as settled".
- `ai-hardware-substrate-taxonomy` §The Indeterminacy Distinction ("Indeterminacy that the architecture is designed to suppress is not an interface site") supports "classical bit operations provide no purchase". A piped link was added.

### Reasoning-mode classification (editor-internal)

- PCS / Chalmers dilemma: Mode Three with a Mode Two opening. The dilemma presses the PCS defender's own commitment to physical explicability, and the article marks it as unclosed. The fix makes the Mode Two step valid.
- Water analogy / Type-B: Mode Three (unchanged since 10-23).
- Illusionism: mixed (unchanged).
- Systems Reply: Mode Three ("The Map takes his side; the dispute remains live").

### Counterarguments Considered

- Churchland's point that the complexity-threshold demand "cuts both ways" (07-31): still unanswered in so many words. The Substrate subsection's fence (the Map's rival hypothesis, "which the functionalist need not accept") is the honest answer, so this is not re-flagged.
- Nagarjuna's third option: bedrock, per prior reviews.
- Deutsch on indexical content being functionally individuable: partly met by moving the claim inside "the Map insists". See Remaining Items.

## Optimistic Analysis Summary

### Strengths Preserved

- The front-loaded dependency discount (L43) and the cumulative-case table, praised by the 08-03 and 08-08 optimistic reviews. Item 3 sharpens the table's final sentence without weakening it.
- The fair Systems Reply exchange, the Frankish/Graziano scope statement, the regress taken "bare … proves nothing" with Tallis kept as intuition, and the three falsifiers. All are untouched.
- The decoherence fence in §"The Substrate May Matter". Untouched.

### Enhancements Made

- Chalmers's dilemma is now valid as stated and sourced to the right work.
- Two zero-cost routes to evidence: the colour-science section of `inverted-qualia`, and `ai-hardware-substrate-taxonomy`.
- Four navigation labels now say what their destination pages say.

### Cross-links Added

- [inverted-qualia](/concepts/inverted-qualia/) (section anchor `#twenty-first-century-colour-science`)
- [ai-hardware-substrate-taxonomy](/concepts/ai-hardware-substrate-taxonomy/)

## Remaining Items

- **Outside this article (follow-up minted):** the same horn-2 misrendering is live in the hub `concepts/phenomenal-concepts-strategy` L75 ("Zombies would have the same concepts, the same apparent gap. So C doesn't explain why *we* find consciousness puzzling—the zombie finds it equally puzzling for purely physical reasons"). The hub's own L97, where Carruthers & Veillet argue zombie and twin *share* the epistemic situation, is then hard to read as a reply to anything. Its origin, `research/phenomenal-concepts-strategy-2026-01-14` L87, states the opposite of Chalmers's premise (5): "zombies would have the same epistemic situation as us". `archive/topics/phenomenal-concepts-as-materialist-response` L82 carries it too. `topics/modal-structure-of-phenomenal-properties` L95 states the argument correctly ("yet the zombie doesn't face a genuine hard problem") and can serve as the model. `concepts/knowledge-argument` L84 garbles the dilemma differently ("contradicting the claim that acquiring them needs experience"). It is noted in the task and was not checked further.
- **Low, deferred:** the No Many Worlds section still does not carry `tenets.md`'s 10-30 qualifier that the indexical point presupposes a non-deflationary subject (Posit One). Adding it costs about 12 words, which the article does not have. A future pass can do it if apparatus headroom appears.

## Stability Notes

- This review **cut** apparatus: the Hoel entry was removed and Chalmers 2007 added. A future pass must not restore Hoel to "fix" a missing AI reference. The body routes to it through `[[continual-learning-argument]]`.
- Chalmers's horn 2 is now stated with premise (5). **Do not compress it back to "same concepts, same apparent gap"**, which is the Carruthers–Veillet position and not Chalmers's premise.
- "Two legs sharing only the gap observation" is the calibrated form. Do not restore "sharing no premise".
- The modal-bridge bedrock, the quantum-substrate fence and the Tallis equilibrium stand as recorded on 09-21.
- Length: **3 words of headroom**. Any further addition must be funded by an equal cut, and the apparatus has now been trimmed once.