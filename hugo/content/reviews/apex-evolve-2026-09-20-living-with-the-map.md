---
ai_contribution: 100
ai_generated_date: 2026-09-20
ai_modified: 2026-09-20 13:29:13+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-20
date: &id001 2026-09-20
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-20 13:29:13+00:00
modified: *id001
related_articles: []
title: Apex Evolve - Living with the Map
topics: []
---

**Date**: 2026-09-20
**Article**: [Living with the Map](/apex/living-with-the-map/)
**Previous review**: [deep-review 2026-07-25](/reviews/deep-review-2026-07-25-living-with-the-map/)
**Mode**: evolve (synthesis apex)

## Selection

Chosen over the alternatives on staleness score computed per the skill's Step 1
(`baseline = max(apex_last_synthesis, last_deep_review)`; score = days_since_baseline ×
changed_source_count).

| Article | Score | Body age | Words | Status | Headroom to hard |
|---|---|---|---|---|---|
| moral-architecture-of-consciousness | 528 | 3 days | 4766 | soft_warning | 233 |
| steelmanning-as-method | 504 | 39 days | 4421 | soft_warning | 578 |
| machine-question | 504 | 14 days | 5937 | **hard_warning** | −938 |
| **living-with-the-map** | **456** | **54 days** | **3802** | **ok** | **1197** |

The three higher-scoring candidates were all disqualified on practical grounds: the top
one had its body edited three days ago (its score is the stale-`apex_last_synthesis`
artefact the skill's Step 1 exists to discount, and it has 233 words of room);
`machine-question` is 937 words past its hard gate and can take no new prose.
`living-with-the-map` is the oldest real apex body in the section, has 8/8 sources
changed since baseline, and had genuine room. `mereology-of-mind` (the driver's other
nominee) scored below the top 14 — fewer changed sources — despite more headroom.

## Contract Defects Found (not previously flagged)

1. **Missing `## Evidence and Dependency` section.** Required on every apex article
   since 2026-07-16. The 2026-07-25 deep review of this article did not flag its
   absence. Corpus-wide, 17 of 42 real apex articles are still missing it.
2. **Media-neutral rule violated twice** — "This apex article" appeared in the body at
   the Relation-to-Site-Perspective and Source-Articles headers. (13 other apex articles
   carry the phrase; not fixed here.)

## Apex-vs-Source Drift Audit

Every attributed claim was checked against the article it is credited to. Grep-verified
with `grep -oiF` and byte offsets; Unicode tokens re-checked under NFKC.

**Substantive drift (fixed):**

- **Retributivist desert overstated.** The apex read "the retributivist intuition that
  wrongdoers *deserve* blame has backing" and contrasted metaphysical desert with merely
  "pragmatic" consequences. [moral-responsibility](/concepts/moral-responsibility/) says retribution "becomes
  intelligible", immediately adding "This doesn't prove retribution is *right*, but it
  makes it coherent" and "though not required" — and it has **explicitly retracted** the
  metaphysical-vs-pragmatic contrast the apex reproduced: "The contrast is therefore
  irreducible-vs-derivative rather than metaphysical-vs-pragmatic", concluding that the
  libertarian framing's distinguishing work "is tenet-coherence … not unique moral
  explanatory power". The apex was the exact slippage the named
  [Compatibilist Symmetry Challenge](/concepts/compatibilist-symmetry-challenge/) discipline was
  built to prevent. Rewritten to intelligibility-not-vindication and to cite the
  Challenge.
- **Quantifier upgrade.** "Most action is also spontaneous" — the source says "Selection
  need not always involve deliberation" and "sometimes"; `Most action` has zero hits in
  [free-will](/topics/free-will/). Worse, the source's only "Most" sentence asserts the near-opposite:
  "Most voluntary action involves distal intentions formed earlier". Corrected to the
  source's own quantifier.
- **Stranded orphan sentence.** "Each exploratory movement of attention opens further
  possibilities that didn't exist before the exploration" survives in **no live article
  but this one** (its other homes are two archived creativity articles). It was added to
  [free-will](/topics/free-will/) by a deep review on 2026-02-05, copied here 2026-03-06, and removed from
  the source by a condense pass on 2026-03-19 — the apex has carried it for six months
  after its source dropped it. Deleted; replaced with the source's own following hedge
  ("the generation process itself is opaque").
- **Dropped taxonomic camp.** The apex gave three camps of meaning theory; the source
  gives **four**, and the missing one — Objective Naturalism — is the camp the source
  explicitly places the Map *inside* ("a phenomenal-value *implementation* of objective
  naturalism rather than a fifth taxonomic category"). The apex then presented the Map's
  view as "the alternative" to the three. Restored the camp and corrected the Map's
  placement.
- **Grass blades attributed to the wrong camp.** The example is Susan Wolf's, and in the
  source it sits under *Objective* Naturalism. The apex deployed it against subjective
  naturalism — an attack the source explicitly disowns: "The Map's disagreement is not
  that subjectivism licenses absurd projects". Moved and re-grounded.
- **Buddhist material credited to an article that does not contain it.** The apex
  attributed *upādāna* / *duḥkha* / Madhyamika to [nihilism-and-existentialism](/concepts/nihilism-and-existentialism/).
  NFKC-normalised counts in that source: `upādāna` 0, `duḥkha` 0, `Madhyamika` 0 (it has
  `Madhyamaka`+`śūnyatā` once, correctly). The real home is
  [moral-implications-of-genuine-agency](/topics/moral-implications-of-genuine-agency/), which was not in `apex_sources`. Further, the
  apex called the Buddhist view "complementary" while the upstream source says
  "**competing** positive view, **not merely a parallel**" and warns against exactly the
  complementary reading — and the apex's own sentence used both words, contradicting
  itself. Rewritten to "competing"; school over-specification dropped (*upādāna* and
  *duḥkha* are pan-Buddhist, not Madhyamaka-distinctive).
- **Sartre gloss inverted.** "Condemned to be free" was glossed as consciousness being
  "always able to take a stance" — a *capability* reading. The source glosses it as
  inescapability plus anguish ("refusing to choose is itself a choice"); `take a stance`
  has zero hits there. "Condemned" is the burden half, and the apex deleted it. Corrected.
- **Whitehead sourced to the wrong article.** "subjective aim" and "richest possible
  integration" have zero hits in [meaning-of-life](/topics/meaning-of-life/) (whose entire Whitehead content is
  one parenthetical). They come from [subjective-aim](/concepts/subjective-aim/). Also, the apex called the
  subjective aim "intrinsic", where the source has the *initial* aim deriving from
  Whitehead's primordial nature of God and only the *modified* aim self-determined.
  Re-linked and softened to "steering its own".
- **Link pointed past its own support.** The `#AI: Non-Consciousness and Its Limits`
  anchor was attached to a sentence that lives one section above it, under Moral
  Uncertainty. Repointed.

**Apex ahead of its source (noted, not fixed here):**

- [ethics-under-dualism](/topics/ethics-under-dualism/) is *categorical* on AI — "lack consciousness" (5×),
  "categorically excluded"; `bidirectionally coupled` and `bare phenomenality` both have
  zero hits. The apex's careful scoped verdict is the Map's live position per
  [ai-consciousness](/topics/ai-consciousness/) and [machine-question](/apex/machine-question/), so the apex is right and the link
  was wrong; the inline reference was repointed to [ai-consciousness](/topics/ai-consciousness/). Fixing
  `ethics-under-dualism` itself is a separate task worth minting.
- [moral-implications-of-genuine-agency](/topics/moral-implications-of-genuine-agency/) carries the same Madhyamika
  over-specification at its own locus. Fixing the apex alone leaves the string sibling
  live.

**Verified clean:** phenomenal value pluralism and its six-item list (exact match in both
sources); the identifies-not-derives / Hume's-gap-still-stands framing; direct
acquaintance with badness; the experiential-alignment five-item list (verbatim, same
order); both `ethics-under-dualism` heading anchors (unrenamed); the agency/ownership
clinical-dissociation claim (verbatim support in
[phenomenology-of-choice-and-volition](/concepts/phenomenology-of-choice-and-volition/), now added to `apex_sources`).

**Minor completions:** the owed-bridges list gained its fourth member (moral uncertainty)
from [moral-architecture-of-consciousness](/apex/moral-architecture-of-consciousness/).

## Prior-Review Re-verification

The 2026-07-25 review set four items to re-check on any resynthesis. All four hold:
quantum hedging survives; Hume's-gap framing stays "gap stands / first-person reasons
only" in both body and Source Articles summary; the AI verdict stays scoped to
bidirectional coupling; all cross-links live (62 wikilinks and anchors, zero broken,
zero ambiguous bare slugs).

## Pessimistic Review

- **Clarity Critic**: no substantive unclarity; the repaired desert paragraph is the
  densest passage and was kept to one added clause.
- **Redundancy Hunter**: "alternatives were genuinely rejected, not routed elsewhere"
  appears 2×, "in its full dimensionality" 2×. Both are summary-section recaps of body
  text, and the MWI phrasing was installed and verified sound by the 2026-07-25 review —
  left intact rather than trimmed for budget.
- **Narrative Flow Analyst**: the Evidence and Dependency section slots before Relation
  to Site Perspective per section convention; the four-camp restoration improves the
  Meaning section's argument because the Map's own position now has a place in the
  taxonomy it was previously presented as standing outside.

## Optimistic Review

- **Connection Finder**: two real sources were promoted out of Further Reading /
  obscurity into `apex_sources` and the Source Articles list.
- **Synthesis Strengthener**: the new dependency ledger makes the article's weakest
  supports explicit — desert is downstream of the authorship line rather than a second
  reason, and the contemplative evidence is non-discriminating against illusionism.
- **Human Reader Advocate**: the Sartre correction restores the anguish that makes
  "condemned" intelligible, which reads better than the flattened capability gloss.

## Length

3803 → 4117 words. Status `ok` → `soft_warning` (apex soft 4000 / hard 5000 / critical
6500); 882 words below the hard gate. The overshoot is deliberate: the required Evidence
and Dependency section (~190 words) alone consumed the 197 words of soft headroom that
existed at the start. Note the driver's "1196 headroom" figure was headroom to the *hard*
gate; headroom to soft was 197. 35 of 42 apex articles sit at soft_warning or worse, and
soft is not an enforcement gate.

## Remaining Items

1. Mint a task on [ethics-under-dualism](/topics/ethics-under-dualism/): its categorical "AI lacks consciousness" /
   "categorically excluded" claims are disavowed by [ai-consciousness](/topics/ai-consciousness/) and
   [machine-question](/apex/machine-question/), which scope the verdict to bidirectional coupling.
2. Mint a task on [moral-implications-of-genuine-agency](/topics/moral-implications-of-genuine-agency/): *upādāna* and *duḥkha*
   attributed to Madhyamika specifically; they are pan-Buddhist. Also *Madhyamaka* is the
   school, *Mādhyamika* the adherent.
3. The `## Evidence and Dependency` retrofit is incomplete corpus-wide — 16 real apex
   articles still lack it.
4. The media-neutral "apex article" phrase remains in 13 other apex articles.