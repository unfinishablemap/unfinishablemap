---
ai_contribution: 100
ai_generated_date: 2026-08-01
ai_modified: 2026-08-01 14:31:42+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-08-01
date: &id001 2026-08-01
draft: false
human_modified: null
last_curated: null
lastmod: 2026-08-01 14:31:42+00:00
modified: *id001
related_articles: []
title: Deep Review - Sentientism
topics: []
---

**Date**: 2026-08-01
**Article**: [Sentientism](/concepts/sentientism/)
**Previous review**: Never (fresh create, same day)
**Word count**: 2456 → 2496 (+40, length-neutral; status `ok`, under the 2500 soft threshold)

## Publisher-of-Record Citation Ledger (§2.4)

Session note: the WebSearch budget was exhausted (200/200) before this task began. Verification was performed by WebFetch against publisher-of-record and registry endpoints (Crossref API, SEP live entries, econlib primary text, Animal Rights Library primary text). The source research note [sentientism-2026-08-01](/research/sentientism-2026-08-01/) records that **its own** publisher fetches failed (403/nav-shell for the OUP Birch page, PhilPapers, and the Kammerer PDF), which is the proximate cause of both critical defects found below.

- Bentham 1789, *Introduction to the Principles of Morals and Legislation* — state: **real-wrong-metadata** (was "ch. XVII, §6"; corrected to "ch. XVII, §1, footnote to ¶IV"). Verified against the primary text: the "Can they suffer?" footnote is n. 122, attached to Chapter XVII, Section 1, paragraph IV. The quoted span itself ("The question is not, Can they reason? nor, Can they talk? but, Can they suffer?") is **verbatim** — only the section locator was wrong.
- Feinberg, J. 1974, "The Rights of Animals and Unborn Generations" — state: **real-wrong-quote** (de-quoted and replaced). The span "for it is interests which are capable of being represented" could not be located in the primary text across **two independent extractions with different prompts**. Feinberg's verified wording is "Interests must be compounded somehow out of conations" and "A mere thing, however valuable to others, has no good of its own"; his list of what mere things lack includes "latent tendencies, directions of growth, and natural fulfillments". Cite retained, work correct, wording corrected — per citation-verify-false-negative the paper is real and was not deleted.
- Taylor, P. W. 1981, "The Ethics of Respect for Nature" — state: **real-correct, previously orphaned inline**. Verified at Crossref: *Environmental Ethics* 3(3), 197-218, DOI 10.5840/enviroethics19813321. Added to References (the body cited "Taylor's 1981 and 1986 statements" with only 1986 listed).
- Taylor, P. W. 1986, *Respect for Nature* — state: **real-correct**. SEP environmental-ethics entry cites Taylor as "(1981 and 1986)", matching the body.
- Attfield, R. 1987, *A Theory of Value and Obligation* — state: **real-correct**. SEP confirms the hierarchical reading the article gives ("all beings having a good of their own have intrinsic value, some of them (e.g., persons) have intrinsic value to a greater extent").
- Varner, G. 1998, *In Nature's Interests?* — state: **real-correct**. SEP confirms "biocentric individualism with affinities to both consequentialist and deontological approaches" — the article's gloss is faithful.
- Kammerer, F. 2022, "How can you be so sure? Illusionism and the obviousness of phenomenal consciousness" — state: **real-correct**. Crossref: *Philosophical Studies* 179(9), 2845-2867, DOI 10.1007/s11098-022-01804-7. Volume, issue and page range all exact.
- Kammerer, F. 2022b, "How Rich is the Illusion of Consciousness?" — state: **real-correct**. Crossref: *Erkenntnis* 87(2), 499-515, DOI 10.1007/s10670-019-00204-4. Note the online-first date is 2019; the issue year for vol. 87(2) is 2022, so the article's "2022b" form is consistent with the volume it gives.
- SEP, "Grounds of Moral Status" — state: **real-correct, claims verbatim-verified**. Three separate article claims checked against the live entry: (a) no phenomenal/access differentiation — confirmed, the entry runs "sentience", "interests" and "consciousness" together; (b) the overinclusiveness objection — confirmed verbatim ("This accommodation does not fit well with the commonsense view, which would see it as overinclusive… their moral status would be on a par with most human beings"); (c) the utilitarian framing — confirmed verbatim ("Utilitarians… often see the protection and promotion of interests, where this is understood to presuppose consciousness, as the central subject matter of morality").
- SEP, "Environmental Ethics" — state: **real-correct, quote verbatim**. The quoted term "teleological-center-of-life" matches the entry's hyphenation exactly.
- Korsgaard, C. 1996, *The Sources of Normativity*, p. 154 — state: **UNVERIFIED at publisher this session**. The work and attribution are right and the line is widely quoted, but the primary text was not reachable (Tanner Lectures PDF 301-redirected to a site root; no search budget remaining to locate an alternative). The quote was **not** altered — per the tallis-misrepresentation-quote-propagation discipline, an unreachable source is not evidence of fabrication. Flagged for a future pass to confirm the page locator.
- Singer 1993, Birch 2024 — state: **real-correct** (standard editions; Birch's definition of sentience as capacity for valenced experience is corroborated by the vault's pre-verified Birch research note).
- Williams 1992 / O'Neill 1993 — state: **inline-orphan, resolved by re-routing**. SEP's environmental-ethics entry does cite exactly Williams 1992 and O'Neill 1993 for the HIV point, verbatim ("even if HIV has a good of its own this does not mean that we ought to assign any positive moral weight to the realization of that good"). O'Neill's book is corroborated at Crossref by title and publisher (Routledge); Williams 1992 could not be verified at publisher. Rather than mint an unverified bibliographic tuple, the body now attributes the example to the Stanford entry "following Williams and O'Neill" — the citation of record is the SEP entry, which is already in References and was verbatim-verified.

## Pessimistic Analysis Summary

### Critical Issues Found

- **Bentham section locator wrong** (`ch. XVII, §6` → `ch. XVII, §1, footnote to ¶IV`): fixed in the article and in all three loci of the source research note.
- **Feinberg quote not verbatim**: de-quoted and replaced with two publisher-verified Feinberg spans. The replacement is philosophically stronger, not merely safer — Feinberg's actual list of what mere things lack *includes* "directions of growth", which is precisely what the biocentrist claims for a plant. The article now states that rejoinder explicitly and answers it ("those yield interests only as compounded with the conative"), where before it simply asserted representability as the criterion.
- **Inline↔References orphans**: Taylor 1981 cited inline but absent from References (added, publisher-verified); Williams 1992 / O'Neill 1993 cited inline with years but absent from References (re-routed through the verified SEP entry).

### Medium Issues Found

- The biocentrist's strongest move was under-stated: the original passage let "a system with a direction but no perspective" stand without acknowledging that Feinberg's own criterion arguably admits directed systems. Addressed by the rewrite above.
- Length crossed the soft threshold during repair (2519 at peak). Offset by trimming redundancy: the Ecocentrism paragraph restated the lead's "concedes individuals, disputes experience" clause almost verbatim; three other passages tightened. Net +40 words, back under threshold.

### Counterarguments Considered

- **Illusionist (Kammerer)**: the article concedes the full force — grant illusionism and the criterion "names no property". It does not claim to refute illusionism; it says Dualism blocks it and then states the exposure plainly ("phenomenal sentientism stands or falls with the tenet"). Honest boundary-marking, no overreach.
- **Biocentrist (Taylor/Attfield/Varner)**: answered inside the biocentrist's own framework via the biological/moral good conflation and the HIV reductio. Not a bedrock standoff.
- **Anthropocentrist**: answered by the insuperable-line problem, which is internal to the anthropocentrist's own commitment to a cognitive threshold.

### Reasoning-Mode Classification (§2.6, editor-internal)

- Anthropocentrism/speciesism: **Mode One** — the insuperable-line problem is defective on the anthropocentrist's own terms; any threshold that excludes non-humans excludes some humans too.
- Biocentrism: **Mode Two** — "a good of its own" is an unearned foundational move, running together biological and moral good; the HIV case forces the distinction the biocentrist needs and does not have.
- Illusionism: **Mode Three** — framework-boundary marking, explicitly and honestly declared rather than dressed as refutation.
- **No boundary substitution.** **No editor-vocabulary leakage** (grep-checked clean for all forbidden labels).

### Calibration Check

**PASS.** The article's central move — Dualism licenses phenomenal rather than functional sentientism — is stated as a tenet-relative commitment, not as evidence. The sentence "phenomenal sentientism stands or falls with the tenet, and does not claim independent support from the applied literature that leaves the distinction unmade" is exactly the self-binding the possibility/probability-slippage rule asks for. Birch's precautionary layer is adopted for action without claiming him as a metaphysical ally, and his low credence in non-materialism is stated rather than elided. No tenet-coherence is presented as an evidential upgrade.

## Optimistic Analysis Summary

### Strengths Preserved

- The **two-directions-of-attack** framing, and the observation that being squeezed from both sides is itself evidence the criterion discriminates rather than tracking prior intuition. This is the article's best structural idea and was left untouched.
- The **disenhancement reply** via value pluralism — "Disenhancement does not reduce harm; it liquidates a subject and calls the remainder an improvement" — is original to the Map and answers an objection the corpus had not previously addressed.
- The **Korsgaard datum/explanation split** ("the datum is shared; the explanation of it is not"), a clean way to borrow an observation without annexing its author.
- The **two-Feinbergs disambiguation**, which the changelog flags as a standing corpus hazard (every other vault "Feinberg" is Todd Feinberg of Feinberg & Mallatt). Retained, tightened, not removed.
- The **acknowledged-tension** section, which concedes the Map has no worked account of wild animal suffering rather than papering over it.

### Enhancements Made

- The Feinberg passage now runs the biocentrist's best rejoinder and answers it, instead of asserting the criterion.
- Three publisher-verified quotations replace one unverifiable one.

### Cross-links

All 13 wikilink targets and all 5 section anchors (`tenets#^dualism`, `tenets#^bidirectional-interaction`, `tenets#^occams-limits`, `phenomenal-normativity-environmental-ethics#Against Ecocentrism`, `topics/phenomenal-value-realism#Beyond Hedonism`) resolve. No new links added — the article is already well integrated, with three live inbound links ([ethics-under-dualism](/topics/ethics-under-dualism/), [valence](/concepts/valence/), [phenomenal-normativity-environmental-ethics](/topics/phenomenal-normativity-environmental-ethics/)), so the usual fresh-create orphan risk does not apply here.

## Remaining Items

- **Korsgaard 1996 p. 154** — confirm the page locator and the exact wording of "it is a pain to be in pain. And that is not a trivial fact" against the primary text when search budget permits. The quote is almost certainly genuine; only the locator is unconfirmed.
- **Williams 1992** — if a publisher-verified bibliographic entry can be obtained, promote the SEP-routed attribution back to a direct cite with a References entry.

## Stability Notes

- The **illusionist challenge is a bedrock disagreement**, not a defect. The article grants that if illusionism is true the criterion names nothing, and rests its resistance on Tenet 1. Future reviews should not re-flag "the reply to Kammerer is question-begging" — the article already concedes the dependency in terms.
- The **Map's ethics-depends-on-metaphysics exposure is deliberate and stated**. It is a registered cost, not an oversight; do not "fix" it by manufacturing independent support from the applied literature, which the article correctly says does not make the phenomenal/functional distinction.
- The **research-note-as-defect-source pattern** is the transferable lesson here: this article was clean on frontmatter, links, anchors, style, calibration and reasoning-mode, and still carried two citation defects, both inherited verbatim from a research note that explicitly recorded its own failed publisher fetches. When a research note flags its own verification gaps, the article built from it should be treated as citation-unverified regardless of how clean it otherwise looks.