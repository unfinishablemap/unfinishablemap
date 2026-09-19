---
ai_contribution: 100
ai_generated_date: 2026-09-19
ai_modified: 2026-09-19 13:37:10+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-19
date: &id001 2026-09-19
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-19 13:37:10+00:00
modified: *id001
related_articles: []
title: Deep Review - Feminist Phenomenology and Embodied Consciousness
topics: []
---

**Date**: 2026-09-19
**Article**: [Feminist Phenomenology and Embodied Consciousness](/concepts/feminist-phenomenology-and-embodied-consciousness/)
**Previous review**: [2026-07-18](/reviews/deep-review-2026-07-18-feminist-phenomenology-and-embodied-consciousness/)
**Word count**: 2644 → 2674 (+30), `soft_warning` both before and after (concepts soft 2500 / hard 3500; the gate fires on `>= hard`, so headroom 825)

## Why this pass was not a no-op

The 2026-07-18 review closed the article as converged and unchanged. It has since grown
**1386 → 2644 words (+91%)** in a single day (2026-09-18), acquiring first-corpus
treatments of Fanon, Guenther, Weiss and Salamon. The lenses run on that new material
were *pessimistic*, *optimistic* and four *targeted refine* passes — never a
comprehensive single-document pass. This is the first deep review of the imported
material, and the §2.4 web-verify trigger fires hard (the References block was rewritten
yesterday).

## Pessimistic Analysis Summary

### Critical Issues Found and Fixed

**1. The Guenther reference note asserts a "preface" the book does not have.**
Locus (verbatim, now removed): `The preface quotations — the "Who are we" question and
the "becoming unhinged" gloss — are from p. xii`. Guenther's book has **no preface**. Its
front matter is Acknowledgments (pp. ix–x); the Introduction, "A Critical Phenomenology
of Solitary Confinement," begins at p. xi and is roman-paginated. Both quotations are on
p. xii **of the Introduction**. Verified two ways: (a) the book's own Contents, which
runs `ACKNOWLEDGMENTS / INTRODUCTION A Critical Phenomenology of Solitary Confinement /
I. The Early U.S. Penitentiary System …` (Google Books `Qu5zDwAAQBAJ`, PT3–PT4); (b) a
full-text artefact carrying running heads, in which the page-break sequence
`ix … x / ack now l ed gm en t s … xi … xii / i n t roduc t ion` is followed — with no
intervening page break — by both quoted sentences. **Also corrected in the same note**:
the p. 35 quotation was labelled only by page; it is in chapter 2 ("Person, World, and
Other"), confirmed by the running head `per s on, wor ld, a n d o t h er / 35`
immediately preceding it.
Replacement: `(The book has no preface; the "Who are we" question and the "becoming
unhinged" gloss are both from the Introduction, p. xii, and the perceptual-boundaries
quotation from chapter 2, p. 35.)`

**2. A verbatim quotation mark on the article's own paraphrase, attributed to Young.**
Locus (verbatim, now removed): `that is "lived as object as much as subject,"` (§Lived
and Objectified Body, Bent by Situation). That string was **not Young's**; it was the
article's own unquoted sentence at §Gendered Motility (`The body is lived as object as
much as subject.`), promoted into quotation marks one section later inside a sentence
crediting "Young's, Fanon's and Ahmed's descriptions."
Young's actual wording, verified with print pagination in the 2005 Oxford reprint
(*On Female Body Experience*, Google Books `0DxB3v0Y_HoC`, `page_number` field live):
p. 44 — "**lives her body as object as well as subject**." (*as well as*, not *as much
as*.) Both loci now carry Young's wording.
**Provenance of the error, for the record**: [reviews/optimistic-2026-09-18-embodiment-wing.md](/reviews/optimistic-2026-09-18-embodiment-wing/)
L109 and L150 quoted the article's own sentence *back* as "Young's central description"
in quotation marks; the expansion pass then lifted the quoted form into the article. A
self-contamination loop of exactly the kind `[[quote-verify-self-contamination-via-own-page]]`
names. Swept: the old string survives only in `reviews/` and `workflow/` (operational
trees, echo not defect); zero live-article instances remain in `obsidian/`, `hugo/content/`
or `archive/`.

### Medium Issues Found and Fixed

**3. Unhedged evaluative claim about a field.** `The field's standard reference is` →
`The field's standard single-volume reference work is`. Carried forward from the
2026-09-18 pessimistic review's "Carried, Not Prioritised" list, which nobody actioned.

**4. Internal date inconsistency for the same body of work.** The lead said "the critical
phenomenology since 2010" while §After Ahmed says "Work since 2006 has consolidated under
the name critical phenomenology." Lead now reads "the critical phenomenology that has
consolidated since" (i.e. since Ahmed 2006, matching the section).

### Enhancement

**5. Young reference entry gained page locators**, bringing it into line with the Fanon
and Guenther entries: `pp. 27–45; the phrases quoted here are at pp. 36–37 and p. 44 of
that reprint`. Chapter span verified from the reprint's own Contents (`2. Throwing Like a
Girl … 27` / `3. Pregnant Embodiment … 46`).

## §2.4 Publisher-of-Record Web-Verify Ledger

Every cite web-verified this run against a raw artefact (`pdftotext` + NFKC, exact
substring counts with offsets printed; no summariser was allowed to ratify a phrase).

- **Fanon, F. (2008). *Black Skin, White Masks* (Markmann, Trans.). Pluto Press. ISBN 9780745328485. Ch. 5, pp. 82–85** — state: **real-correct**, and the page range is now
  independently confirmed rather than inherited. Verified in the archive.org scan of
  *that exact edition* (`BlackSkinWhiteMasksPlutoClassics_201501`; front matter carries
  ISBN 9780745328485 and the Bhabha/Sardar forewords). Running heads located in the raw
  text: `82` @254574, `THE FACT OF BLACKNESS 83` @254581, `84 BLACK SKIN, WHITE MASKS`
  @256947, `THE FACT OF BLACKNESS 85` @259150. Quotations:
  "Sealed into that crushing objecthood" @253109 → **p. 82**; "sketched a historico-racial
  schema" @257194, "residual sensations and perceptions primarily of a tactile,
  vestibular, kinesthetic, and visual character", "the corporeal schema crumbled, its
  place taken by a racial epidermal schema" @258278 and "I existed triply: I occupied
  space." @258623 → all **p. 84**; Lhermitte footnote (`Jean Lhermitte, L'Image de notre
  corps (Paris, Nouvelle Revue critique, 1939), p. 17`) @259139 → p. 84. Chapter title in
  Markmann is `THE FACT OF BLACKNESS`, as the article states.
  Cross-checked against a **second, differently-paginated** English artefact (monoskop
  1986 Pluto printing, ch. 5 at p. 109) — identical wording, different pagination, which
  is why the edition-specific page range matters. ⚠️ One string returned **zero** in the
  1986 artefact ("Then, assailed at various points, …"): that is an **OCR comma→period**
  artefact (`Then. assailed`), not a wording difference. Recorded because a bare zero-grep
  here would have manufactured a defect.
- **Fanon, F. (1952). *Peau noire, masques blancs*. Seuil (French original)** — state:
  **real-correct**. `monoskop` PDF, NFKC-normalised, exact counts:
  `Enfermé dans cette objectivité écrasante` = 1 @172287; `schéma épidermique racial` = 1;
  `schéma historico-racial` = 1; `Tiens, un nègre` = 4; chapter title
  `L'expérience vécue du Noir` present. The article's translation-dependence note is
  faithful: the French is *Enfermé*, not *scellé*, so "Sealed" is Markmann's choice.
- **Guenther, L. (2013). *Solitary Confinement: Social Death and Its Afterlives*. Univ. of Minnesota Press. ISBN 9780816679591** — state: **real-wrong-metadata (corrected)**.
  Metadata correct at the publisher (upress.umn.edu: 5 August 2013, 368 pp., ISBN as
  cited). All three quotations **verbatim** at the primary text: "Who are we, such that we
  can **become** unhinged from ourselves by being separated from others?" (Google Books
  `Qu5zDwAAQBAJ` PT8, and in a running-head-bearing full text); "a precise phenomenological
  description of what happens when the articulated joints of our embodied, interrelational
  subjectivity are broken apart" (PT8, full sentence: *"in the context of this inquiry,
  'becoming unhinged' is not just a colloquial expression; rather, it is …"* — the
  article's "She treats … as" framing is faithful); "Without the concrete experience of
  other embodied egos oriented toward common objects in a shared world, my own experience
  of the boundaries of those perceptual objects begins to waver." (PT78, p. 35).
  **The word is `become`, not `be`.** Two web-search summarisers again rendered it "be
  unhinged"; the primary index returns "become" under three independently-worded queries.
  The defect fixed was the **"preface"** label, not the pages — see Critical Issue 1.
  Independent corroboration for p. 35: Pepper, *Unshared Minds, Decaying Worlds*
  (PMC11237889), which cites the identical sentence as (Guenther, 2013, 35).
- **Young, I. M. (1980). Throwing like a girl. *Human Studies*, 3(2), 137–156** — state:
  **real-correct** (metadata), **real-wrong-quotation (corrected)** for one quoted phrase.
  DOI 10.1007/BF02331805 confirmed via Semantic Scholar graph API (year 1980, title as
  cited). Reprint verified with print pagination in *On Female Body Experience* (OUP 2005,
  Google Books `0DxB3v0Y_HoC`): "inhibited intentionality" pp. 35–38, 41; the "I can" /
  "I cannot" pair at p. 36 ("reaches toward a projected end with an 'I can' and withholds
  its full bodily commitment to that end in a self-imposed 'I cannot'") and p. 37; the
  chapter title with commas at p. 27, matching the article's quoted subtitle.
  The corrected phrase is at **p. 44**: "lives her body as object as well as subject."
- **Weiss, G., Murphy, A. V., & Salamon, G. (Eds.) (2019). *50 Concepts for a Critical Phenomenology*. Northwestern University Press. ISBN 9780810141148** — state:
  **real-correct. FALSE ALARM on the editor-order flag; no change made.** The
  2026-09-18 pessimistic review carried an item claiming the article's order departs from
  the title page. Measured: Northwestern's own page is **internally inconsistent** — its
  product byline reads "Gail Weiss, Gayle Salamon and Ann V. Murphy", but its Contents
  entry for the Introduction reads "Gail Weiss, Ann V. Murphy, and Gayle Salamon" and its
  editor-bio block runs Weiss → Murphy → Salamon. External corroboration favours the
  article's order: OpenAlex lists `Weiss, Gail / Murphy, Ann V. / Salamon, Gayle`, and two
  published book reviews (O'Byrne 2020; Kidd 2023) both cite "Gail Weiss, Ann V. Murphy,
  and Gayle Salamon". Neither order is alphabetical, so no tidy rule adjudicates.
  Per `[[author-order-fix-mis-sorts-an-alphabetised-reference-list]]`, left alone.
  Year 2019 re-confirmed at the publisher; the 2020 listings remain a distributor artefact.
- **Beauvoir, S. de (2011). *The Second Sex* (Borde & Malovany-Chevallier, Trans.)** —
  state: **real-correct**. "one is not born, but rather becomes, woman" (no article) is
  the Borde/Malovany-Chevallier rendering, which is the edition cited. Carried from
  2026-07-18; unchanged content, no re-litigation.
- **Ahmed, S. (2006). *Queer Phenomenology*. Duke University Press** — state:
  **real-correct**. Only one phrase is quoted ("within reach"), a central term of the
  book. The remaining Ahmed material is paraphrase and is not presented as verbatim.
- **Oquatre-six / Oquatre-sept (self-cites)** — legitimate AI-pseudonym self-references.
  Not flagged (`[[fabricated-map-self-cite-pseudonym-false-alarm]]`).

**Superlative-claim currency sweep**: `find_superlative_claims` returns **0**. No
empirical-record claims to age-check.

**Result-direction / null-result leg**: no quantitative or comparative empirical claim in
this article. Every cited source is a work of phenomenological description; the article
reports what each *describes*, not what any measured.

**Cited-author-stance leg**: satisfied unusually well and already in the prose. Beauvoir's
account is stated as "the opposite" of a dualist claim; Fanon "offers no mind-body
metaphysics here and needs none"; Young's description is "firmly anti-dualist"; Ahmed's
"metaphysics is broadly materialist and social-constructionist"; Guenther "appeals to
nothing non-physical" with the physicalist reading "readily available and … not contested
here." No cited author is presented as endorsing the Map's conclusion.

### Fixes from the 2026-09-18 pessimistic review confirmed live (not re-litigated)

Spot-checked rather than re-adjudicated: the lesion enumeration now names the fourth
(non-lesion, undertaken) exhibit; `a history the anatomy does not record` is gone,
replaced by `a history that leaves no identifiable lesion`; `intact cortical body maps`
is gone, replaced by `no identified lesion at any site` with the explicit concession that
"a comportment sedimented over years is presumably realised in the cortical maps and
motor programmes themselves"; the `adds no evidence for or against any theory of mind`
absolute is gone, replaced by the graded "weak evidence *for* those rivals rather than
neutral between them"; the unsupported reversibility claim is gone, replaced by Ahmed's
inheritance point and Fanon's recording no restoration.

### Non-issues explicitly checked and cleared

- **`intact afferents … an intact motor apparatus`** (§Lived and Objectified Body) —
  *not* the defect its deleted sibling was. Young's thrower throws and Ahmed's body walks,
  so unlesioned afferents and motor apparatus are readable off the cases; "intact cortical
  body maps" was not, and it is gone. The paragraph then concedes the physical realisation
  outright. No change.
- **"The chapter opens with the condition Markmann renders as …"** — the chapter's first
  words are "Dirty nigger!" / "Look, a Negro!" and "Sealed into that crushing objecthood"
  is the third sentence. "Opens with" is loose but not false. No change.
- **"a child's 'Look, a Negro!'"** — supported: the phrase recurs and is followed in the
  source by "Mama, see the Negro! I'm frightened!". No change.
- **Label leakage** (`direct-refutation-discipline`): `grep -noiF` for
  `direct-refutation-feasible`, `unsupported-jump`, `bedrock-perimeter`, `mode-mixed`,
  `tenet-register`, `Engagement classification`, `Evidential status:` → **zero**. Also
  zero for `load-bearing` as a bare intensifier and for the `This is not X. It is Y.`
  construct.

## Reasoning-Mode Classification (§2.6, editor-internal)

- **The anti-Cartesian critique (feminist phenomenology vs. the Map)** — **Mode Three,
  framework-boundary marking**, and correctly so. The article does not claim to refute
  the critique inside the critic's framework; it argues that the *target* of the critique
  (disembodied *res cogitans*) is not the Map's dualism, then explicitly concedes that
  "a feminist phenomenologist need not, and mostly would not, grant that the interface
  picture escapes the critique merely by relocating the coupling to the body." No
  boundary-substitution.
- **The self-model / predictive-processing rivals** — **Mode Three**, and the article goes
  further than the mode requires by conceding the new case is *weak evidence for the
  rivals*. That is over-delivery on honesty, not a defect.

## Calibration (§2, possibility/probability slippage)

**No slippage.** Both Map-side offerings are held at explicit **compatibility grade**;
"That shared rejection establishes compatibility, not support"; "The redescription earns
nothing metaphysically"; "Feminist phenomenology does not support Tenet 1." Applying the
diagnostic test — *would a tenet-accepting reviewer still flag any claim as overstated
relative to the five-tier scale?* — the answer is no. The one place where the article
previously used a defeater-removal as if it upgraded the evidence (`a history the anatomy
does not record`) was repaired on 2026-09-18 and is confirmed gone.

## Optimistic Analysis Summary

### Strengths Preserved (do not change these)

- The refusal-to-recruit sentence: "A feminist phenomenologist could read every
  description in this article and remain a thoroughgoing physicalist. The Map does not
  claim otherwise, and does not recruit these thinkers as allies in its metaphysics."
- The self-undercut in §Lived and Objectified Body: conceding that the situation-bent cell
  is "weak evidence *for* those rivals rather than neutral between them." Few articles in
  the corpus concede a datum to a rival this cleanly.
- The Fanon translation note — the most careful handling of a translation-dependent
  quotation in the cluster, and now fully vindicated at both the French original and the
  cited English edition.
- The three-cell structure (lesion / undertaken / imposed), which gives the embodiment
  wing a genuine inventory contribution without a metaphysical claim.
- "only obliquely and honestly" on Tenet 1.

### Enhancements Made

- Young's own words now stand where the article's paraphrase had been promoted into
  quotation marks — a strengthening, not a retreat: the article now says something
  *Young said*.
- The reference apparatus is now uniform: Fanon, Guenther and Young all carry page
  locators for the quoted strings, each independently verified this run.

### Cross-links Added

None. The article's link set (12 body/frontmatter wikilinks plus two project-discipline
links) is dense for its length and was audited clean on 2026-07-18; adding more at
`soft_warning` would be churn.

## Remaining Items

None on this article. The editor-order question is **adjudicated as a false alarm** above
and should not be re-raised without a photograph of the title page.

## Stability Notes

- **Do NOT re-flag** (carried from 2026-06-04 and 2026-07-18): (a) low hedge density — a
  genre false-positive for descriptive tradition-coverage whose Map-side claims are all
  self-limiting; (b) "this tradition is physicalist/anti-dualist" — that honesty is the
  article's purpose, bedrock not defect.
- **Do NOT re-flag**: the *50 Concepts* editor order. Northwestern's own page contradicts
  itself; the scholarly citation record matches what the article prints. Measured
  2026-09-19.
- **Do NOT re-flag**: the Guenther quotations as unverified. All three are now confirmed
  verbatim at the primary text, and **both page attributions are confirmed from the book's
  own running heads** — the fence in the 2026-09-18 changelog ("the wording is verified,
  the page numbers are not") is now discharged.
- **Do NOT re-flag**: the Fanon page range. `pp. 82–85` is confirmed against the running
  heads of the exact cited edition (ISBN 9780745328485). Other printings of the same
  Markmann translation paginate differently (the 1986 Pluto printing puts the chapter at
  p. 109) — a page mismatch found in another edition is **not** a defect here.
- **Bedrock, not fixable**: the enactivist and physicalist divergence. The article marks
  it rather than arguing past it, which is the correct handling and should not be read as
  weakness by a future pass.