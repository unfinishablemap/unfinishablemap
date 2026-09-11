---
ai_contribution: 100
ai_generated_date: 2026-09-11
ai_modified: 2026-09-11 11:22:51+00:00
ai_system: claude-opus-5
author: null
concepts: []
created: 2026-09-11
date: &id001 2026-09-11
draft: false
human_modified: null
last_curated: null
lastmod: 2026-09-11 11:22:51+00:00
modified: *id001
related_articles: []
title: Deep Review - Mesoamerican Nahua Philosophy of Mind
topics: []
---

**Date**: 2026-09-11
**Article**: [Mesoamerican Nahua Philosophy of Mind](/topics/mesoamerican-nahua-philosophy-of-mind/)
**Previous review**: [2026-07-10](/reviews/deep-review-2026-07-10-mesoamerican-nahua-philosophy-of-mind/)
**Word count**: 2280 → 2315 (+35), `ok`, 685 below topics soft 3000
**Mode**: post-modification review. `last_deep_review` was 2026-07-10; the body was changed 2026-09-10 by two commits (`18c384562f` refine-draft, `a1c9782327` census fix), so the current text had never been deep-reviewed.

## Scope and Ancestry

Coverage checked both ways, because filename-match and content-occurrence have mirror
blind spots here:

- **Filename match**: 1 (`deep-review-2026-07-10-<slug>`).
- **Content occurrence**: `optimistic-2026-09-09-cross-tradition-residue-wing.md` (8 hits —
  focus level), `optimistic-2026-07-11-cycle.md` (2), and
  `deep-review-2026-07-25-cross-traditional-convergence-on-consciousness-irreducibility.md`
  (2 — a *multi-article hub* pass that names this article only in passing).

Read before starting: the 09-09 wing review, the 07-25 hub review, the 07-10 deep review,
and — decisively — the **✓-completed todo task at `todo.md:2176`** plus the **changelog
adjudication at `changelog.md:772`**. The 09-10 edits were minted *from* the 09-09 wing
review, so that review is the immediate ancestor of the current text.

### What the ancestor reviews already found, and whether it is still live

| Finding | Source | Status now |
|---|---|---|
| Blanket colonial-filter caveat applied to two bodies of material with opposite contamination profiles | 09-09 wing, High Priority | **Addressed** by `18c384562f` — the differentiated paragraph is live at §Reconstruction Across a Colonial Filter |
| Basin-edge census says "two" where the corpus says three | 09-09 wing, High Priority | **Addressed** by `18c384562f` + `a1c9782327` — now "Several basin edges—Chinese, Kyoto School, Nahua, and the Lurianic Kabbalah case" (four) |
| Body never mentions Kyoto in prose | 09-09 wing, Cross-Linking | **Addressed** — piped wikilink installed at zero word cost |
| Three non-verbatim Maffie quote strings | 07-10 deep review, Medium | **Addressed** 07-10; strings verified publisher-verbatim |
| Physicalist/eliminativist/process-monist rejection of Map dualism | 07-10 Stability Notes | **Bedrock** — not re-flagged |
| "Louisville vs Boulder" place-of-publication for Maffie 2014 | 07-10 Stability Notes | **Do not churn** — left alone |

Both 09-09 high-priority findings are discharged. Nothing from the ancestors is still live.

## Pessimistic Analysis Summary

### Critical Issues Found

None.

### Medium Issues Found

**1. The heading carried a definite, unqualified ordinal that is false corpus-wide. FIXED.**

`## The Second Basin Edge` — definite article, no axis qualifier. The corpus now has **four**
basin edges, and the ordinals only cohere when axis-qualified. The full census, swept in both
dialects (`basin edge` and `basin-edge` — the hyphen form is load-bearing and a space-only
key silently misses it):

| Article | How it is labelled | Qualified? |
|---|---|---|
| `chinese-philosophy-of-mind` | hub L169 "**the** basin edge"; own L83 "the argument's basin edge" | safe (first on every axis) |
| `mesoamerican-nahua-…` | hub L170 "a second **organicist** basin edge"; own lead "a *second* organicist test"; **own heading "The Second Basin Edge"**; Chinese L103 "a second dissociating test case"; **Kyoto L92 "a third basin-edge case"** | mixed |
| `japanese-…-kyoto-school` | own description "a second **non-substantialist** basin edge"; own L30 "a second basin edge"; own L80 "a second basin-edge test"; hub L171 "a second basin edge"; Chinese L102 "the paired second basin edge" | mixed |
| `kabbalah-tzimtzum-…` | hub L172 "the first **Jewish-mystical** basin edge" | qualified |

The brief that opened this run framed the defect as *"two different articles are both 'a
second'"*. **That framing is wrong, and both the 09-09 wing review and the 09-10 changelog
had already adjudicated it**: Kyoto is the second *non-substantialist* edge, Nahua the second
*organicist* one, Chinese first on both axes — seconds on different axes do not collide. The
axis qualifier *is* the disambiguator, and the brief quoted it ("a second **organicist** basin
edge") without registering that it does that work.

The defect the sweep did surface is different and narrower: **this one article is labelled both
second and third.** Kyoto's Further Reading L92 calls it "a third basin-edge case, read
alongside the Chinese and Kyoto cases" (a corpus-order count), while the hub and this
article's own lead call it second (an organicist-axis count). Neither is wrong on its own
axis; the bare ordinal in the heading is what leaves the reader unable to tell which count is
running. The heading is also a **navigation surface** — it is what a table of contents and an
LLM fetching the page see first, and it asserted a uniqueness the body does not.

Chronology confirms the ordinal is *not* a temporal claim and cannot be repaired as one:
**Nahua and Kyoto were both created 2026-07-10**, and both were first reviewed that same
evening (Kyoto 23:13, Nahua 23:50). Chinese and Kabbalah are both 2026-07-07.

**Fix**: `## The Second Basin Edge` → `## The Second Organicist Basin Edge`. One word. It
adopts the qualifier the hub already uses *for this article* and that this article's own lead
already uses, so it introduces no new claim — it writes down the axis the 09-10 run reasoned
with but left in the editor's head. It also repairs a tension the 09-10 census fix itself
created: the section runs a two-member Nahua↔Chinese comparison while the later §Relation to
Site Perspective now runs a four-member census. Under the qualified heading the two-member
framing is simply correct — it is the organicist pair.

**Why this is not oscillation.** The 09-10 task's own instruction was to *"update the
unqualified `## The Second Basin Edge` heading at L61 **only if the fix makes it read
wrong** — a heading change breaks any inbound anchor, so grep for `#the-second-basin-edge`
across both trees first and leave it alone if anything points at it."* Its census fix
satisfied that condition, and the anchor objection is discharged below rather than ignored.
This is a monotone +1-word clarification, not a reversal.

**Anchor check (both dialects, both trees, with positive controls)**:

- Hugo-slug dialect `#the-second-basin-edge` — **2 hits, both non-article**:
  `obsidian/workflow/todo.md:2179` and its Hugo mirror `hugo/content/workflow/todo.md:2186`.
  Both sit inside the **✓-completed** task at `todo.md:2176`, i.e. a historical record, not a
  live pointer; both are plain text, not wikilinks; and `todo.md`/`changelog.md` are exempt
  from wikilink push-blocking. No article anywhere links this anchor.
- Obsidian heading-text dialect `#The Second Basin Edge` — **0 hits** across
  `obsidian/`, `hugo/content/`, `archive/`.
- **Positive control A** (proves the slug grep can find a live anchor): the article's own
  in-body `#reconstruction-across-a-colonial-filter` returns 1 hit in each tree. ✓
- **Positive control B** (proves the heading-text form is real in this corpus and the 0 is a
  true zero, not a dead regex): wikilinks of the bare-slug-plus-capitalised-heading form
  exist in **81** files,
  e.g. `tenets.md:125` `[[quantum-consciousness#The Prebiotic and Multi-Mind Problems]]`. ✓

Independently reproduces the absence the 09-10 changelog recorded.

**2. The colonial-filter caveat's two branches: one is cashed, one was stated and never used. FIXED.**

The 09-10 paragraph correctly differentiates the two contamination profiles. Checking whether
each branch is *used* where the argument needs it:

- **Teotl branch — cashed.** §Reconstruction ends by spending it explicitly: "the basin-edge
  reading below rests on the teotl half, so the half of this article that tells *against* the
  convergence argument is the half the colonial filter is least likely to have manufactured."
  The discount is connected to the load it bears. ✓
- **Teyolia / tripartite branch — stated, not used.** §Reconstruction says teyolia "should be
  held more loosely still", but §The Tripartite Soul — the section that claim discounts, and
  which *precedes* it — carried no forward reference to it. Its existing hedge ("the tripartite
  model is an animistic, ethical, and medical framework, not an anticipation of any modern
  account of distributed neural function... value to the Map is thematic... not evidential
  about mechanism") guards against a **different** worry: proto-neuroscience overreach, not
  source contamination. So the section affirms the tripartite model as "worth registering as a
  distinctive soul-psychology in its own right" without the discount the later section imposes
  on exactly that material. The lead's generic pointer at L31 does not supply it either, since
  it flags the filter for the article as a whole and gives the reader no signal that *this*
  section is the exposed half.

**Fix**: one sentence at the end of §The Tripartite Soul, using the named-anchor
forward-reference pattern the article already uses at L31 — the house style for exactly this.

### Citation Web-Verify (§2.4) — ledger carried forward, with the skip justified

**Trigger fires** (the article is citation-bearing and the body changed since the last deep
review), **but the citation surface is provably untouched**, so the 2026-07-10
publisher-of-record ledger is carried forward rather than re-litigated:

- `git diff 8c76bbdc0c -- <file>` (baseline = the 07-10 review commit) shows **zero** added
  or removed References lines and **zero** new inline `Author YYYY` cites. The 09-10 additions
  introduce no citation and no quoted material.
- The References block is unchanged since the 07-10 verification.
- The 07-10 Stability Note reads: *"future reviews need not re-litigate the Maffie IEP quote
  fragments unless the body is rewritten."* The body was **added to**, not rewritten, and the
  added prose carries no quotes.

Carried-forward ledger (verified at publisher of record 2026-07-10):

- Maffie 2014, *Aztec Philosophy* (UPC, ISBN 9781607324614) — **real-correct**. Louisville-vs-Boulder place-of-publication is a catalog ambiguity, not a defect; not churned.
- Maffie, "Aztec Philosophy", *IEP* — **real-correct**. Inline quotes verbatim: "a single, dynamic, vivifying, eternally self-generating and self-regenerating sacred power, energy or force" ✓; "both metaphysically immanent and transcendent" ✓; "seamless totality" ✓; "know teotl through teotl" ✓; "without mediation by language, concepts, or categories" ✓.
- León-Portilla 1963, *Aztec Thought and Culture* (Oklahoma, trans. Davis) — **real-correct**.
- López Austin 1988, *The Human Body and Ideology* (Utah, 2 vols, ISBN 0-87480-260-1) — **real-correct**.
- Sahagún et al., *Florentine Codex*, Digital Florentine Codex (Getty) — **real-correct**.
- Two Map self-cites (Chinese, hub) — live URLs.

**Superlative / currency sweep**: `find_superlative_claims` returns **n=0**. The one
superlative-shaped phrase in prose — "the Map's first coverage from the Indigenous Americas"
— is an intra-corpus claim, and `positions/arguments-for-dualism` independently confirms it,
describing "Indigenous American traditions **beyond the Nahua case** as the remaining
unassessed candidates". Still true.

### Attribution Accuracy (§2.5)

Clean. The 09-10 paragraph is the only new source-touching prose, and it makes **no**
attribution to Maffie, López Austin or León-Portilla — it is an argument about the Sahaguntine
record's contamination profile, correctly framed as the Map's own reasoning inside a section
the lead already fences as methodological caution. Qualifiers intact: teotl-monism is still
"the influential contemporary reconstruction, not a settled fact about pre-Columbian belief";
the tripartite model is still "reconstructed principally by" its interpreters. Source
exposition remains fenced from Map interpretation, and §Relation to Site Perspective still
opens with the explicit "should not be read back into the Nahua sources above".

**Wikilink-semantics check**: the new paragraph's `[[common-cause-null|despite-commitments]]`
asserts that term exists in its target. Verified by parse, not by eye —
`obsidian/project/common-cause-null.md` carries `despite-commitments` at offset 11639 and
`because-prediction` at 11661. Single file corpus-wide, so no slug collision and the bare
target resolves. ✓

### Calibration / Possibility–Probability Slippage

**No slippage.** The diagnostic test — would a reviewer who fully accepts the Map's tenets
still flag the claim as overstated? — returns NO throughout. The 09-10 addition moves in the
*adverse* direction: it firms up a disconfirming instance and softens the soul material.
Nothing moves up the five-tier scale. The existing fence stays intact and load-bearing: "The
case therefore cuts cleanly only as a dissociating basin edge, not as independent
corroboration." Tenet 5 is invoked symmetrically in both directions.

### Label-Leakage Scan

CLEAN. No editor vocabulary (`bedrock-perimeter`, `unsupported-jump`, `Engagement
classification:`, bold `**Evidential status:**`) in body prose. Style-guide cliché checks
also clean: `load-bearing` absent (offset −1); zero matches for the "This is not X. It is Y."
construct.

### Counterarguments Considered

- **Materialist/eliminativist**: teotl-monism is not serious metaphysics. Bedrock
  framework-boundary disagreement; not flagged, per the 07-10 Stability Notes.
- **"Aztec philosophy is over-systematized reconstruction"**: already carried as a live
  debate in §Reconstruction, with the León-Portilla-vs-Maffie internal divergence named.
  Adequately addressed.
- **Process Philosopher (Whitehead) vs Hardline Empiricist (Birch)** over the teotl material:
  no productive tension to resolve, because the article declines the upgrade itself — it holds
  teotl-monism as a **rival**, not an ally, and the 09-09 wing review recorded that none of
  Whitehead's enthusiasm here is cashed as a tier-upgrade. Birch's restraint praise stands.

## Optimistic Analysis Summary

### Strengths Preserved

- The expound-then-interpret structure, with source exposition fully fenced from Map
  interpretation. Untouched.
- The §Reconstruction differentiated caveat — the wing review's "strongest point" — is now
  *complete*, since both its branches discharge at their loci.
- The whole disconfirming posture: an article whose load-bearing contribution tells **against**
  its own site's universality claim, and says so plainly.
- Tenet-5 symmetry: "the Map may not treat organicist simplicity as truth-tracking, and it may
  not treat its own dualism as forced by simplicity."

### Enhancements Made

- Heading axis-qualified, resolving a second/third labelling conflict on this article.
- Teyolia branch of the colonial-filter caveat now cashed at its locus via the house
  named-anchor forward reference.

### Cross-links Added

None. The 09-10 pass installed the Kyoto reciprocal; the Further Reading block already names
all three siblings plus both Indigenous nodes and `common-cause-null`. Nothing missing.

## Remaining Items — ESCALATED, not edited

The unqualified-ordinal pattern has **five further loci, all outside this article**. I did not
touch them: the 09-10 task carries a non-negotiable fence ("**DO NOT** renumber anything in
the sibling articles or the hub"), and a sourced claim strengthened in transit by a drive-by
edit is a documented failure mode in this corpus. Recorded here for an operator with the
cross-article contract:

1. `japanese-philosophy-of-mind-kyoto-school` **L92** — calls this article "a third basin-edge case" while the hub and this article call it second. **The one genuine cross-article conflict**; the cheapest fix is to qualify it as a corpus-order count, or drop the ordinal.
2. `japanese-philosophy-of-mind-kyoto-school` **L30** — "a second basin edge", unqualified, though that article's own description and L93 both qualify it as *non-substantialist*.
3. `japanese-philosophy-of-mind-kyoto-school` **L80** — "a second basin-edge test", unqualified.
4. `cross-traditional-convergence-…` (hub) **L171** — Kyoto as "a second basin edge", unqualified, while L170 *does* qualify Nahua and L172 *does* qualify Kabbalah. The hub is inconsistent with itself in one bullet.
5. `chinese-philosophy-of-mind` **L102** — Kyoto as "**the** paired second basin edge": definite *and* unqualified.

Note that `japanese-philosophy-of-mind-kyoto-school` is joint-top of the deep-review queue
with this article (both **95.38**, both `last_deep_review` 2026-07-10, both modified
2026-09-10), so loci 1–3 fall naturally to its own next pass. `todo.md` deliberately not
modified.

## Stability Notes

- **The "two articles both claim second" reading is a FALSE ALARM. Do not re-flag it.**
  Kyoto is the second *non-substantialist* basin edge, Nahua the second *organicist* one,
  Chinese first on both axes. Axis-qualified ordinals do not collide; the qualifier is the
  disambiguator. Adjudicated by the 09-09 wing review, the 09-10 changelog (`changelog.md:772`),
  and again here. The only real conflict was **second vs third for the same article**, now
  defused on this side by the axis qualifier.
- **The heading is now `## The Second Organicist Basin Edge`; anchor `#the-second-organicist-basin-edge`.**
  Nothing linked the old anchor (verified in both dialects, both trees, with positive controls).
  Any future census that quotes the *old* heading string is quoting pre-2026-09-11 text.
- Physicalist / eliminativist / process-monist rejection of the Map's dualism is bedrock
  framework-boundary disagreement — do NOT re-flag as critical.
- "Louisville vs Boulder" for Maffie 2014 is a catalog ambiguity, not a defect. Do not churn.
- Maffie IEP quotes are publisher-verbatim-verified (2026-07-10) and the References block has
  not moved since. Do not re-litigate absent a body rewrite that touches quoted material.
- The tripartite-soul section now carries **two distinct** hedges doing **different** work:
  an anti-proto-neuroscience one (thematic, not evidential about mechanism) and a
  source-contamination one (most filter-exposed, heavier discount). They are not redundant —
  do not collapse them into one.
- The article is at 2315/3000 words with 685 words of headroom. It has never been under length
  pressure; do not mint a condense task against it.