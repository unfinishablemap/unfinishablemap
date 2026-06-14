---
name: harvest-research-subjects
description: Mine outer/optimistic reviews for uncovered subjects and mint research-topic tasks. Wall-clock trigger, daily.
---

# Harvest Research Subjects

Convert "the corpus doesn't cover X" findings from the review corpus into
`research-topic` tasks, reviving the research→expand-topic pipeline.

## Why this exists

The loop's organic research generators dried up: replenish mints expand-topic
candidates only from gap analysis (mature corpus → nothing) and dedupes
anything it proposes against the 572-entry Vetoed bank, so new-article
generation stalled even with cap headroom. Meanwhile the outer reviews — three
frontier models independently naming what the corpus does NOT cover — were
mined only for refine-draft fixes (45 refine-draft tasks vs 0 research-topic).

This skill reads the review files that NOMINATE NEW TERRITORY (outer-review,
outer-review-synthesis, optimistic) and mints research-topic tasks, deduping
against **live articles and existing research notes — NOT the Vetoed bank**.
That last point is the whole point: a subject the operator once parked is fair
game again when an external reviewer re-raises it as a genuine gap.

## When to Use

- Automatic: wall-clock trigger, daily (`tools/evolution/time_trigger.py:check_harvest_research`).
  Daily, not cycle-based, because cycle cadence stretches to ~29h of uptime and
  drifts (see [[check-model-fallback]]'s same migration).
- Manual: `/harvest-research-subjects` to top up the research queue on demand.

## Instructions

### 1. Get the batch of unscanned reviews

```bash
uv run python scripts/harvest_research_subjects.py --list-unscanned
```

This prints the newest mine-reviews not yet scanned (default 8). If it prints
nothing, every mine-review is scanned — exit cleanly, nothing to harvest.

### 2. Read each listed review and extract uncovered-subject candidates

Read the listed files. You are looking ONLY for findings that name a subject
the corpus does not yet cover and that warrants its own article — phrased as
"omits", "no article on", "missing the literature on", "would benefit from a
dedicated treatment of", "under-explored", "the Map lacks", etc.

**Include** a candidate when the finding names a discrete, article-sized
philosophical/empirical subject that plausibly belongs in `topics/` or
`concepts/`.

**Exclude** (these are NOT research subjects — they are other task types):
- "fix / sharpen / rebalance / add a hedge to [existing article]" → refine-draft, not ours
- "add a cross-link between X and Y" → refine-draft
- "this citation is wrong / stale" → refine-draft / literature-drift
- subjects that target `voids/` (at cap; research-voids owns that lane)
- vague meta-advice ("be more rigorous", "engage opponents better")

For each kept candidate, prepare an object:
- `title`: the subject as an article-title-shaped noun phrase (no "Research"/"Write" prefix — the script adds "Research ")
- `slug`: kebab-case (omit to let the script derive it from the title)
- `target_section`: `topics` or `concepts`
- `rationale`: one or two sentences — what the reviewer said and why it's worth covering. Quote the review where useful.
- `source_review`: the review filename it came from
- `priority`: `P2` (default) or `P3`

Assess-first: only include subjects you judge genuinely worth covering. It is
correct to read 8 reviews and mint 0 if none name a real new subject.

### 3. Mint the tasks

Pipe a JSON payload to the CLI. `subjects` is your candidate list; `scanned`
is EVERY review filename you read this run (so the backlog drains, even reviews
that yielded nothing):

```bash
echo '{
  "subjects": [
    {"title": "Chemosensory qualia under dualism", "target_section": "topics",
     "rationale": "outer-review-2026-06-14-claude-fable-5 flags olfaction/gustation as having no modality home despite being load-bearing in two articles.",
     "source_review": "outer-review-2026-06-14-claude-fable-5.md", "priority": "P2"}
  ],
  "scanned": ["outer-review-2026-06-14-claude-fable-5.md", "optimistic-2026-06-14.md"]
}' | uv run python scripts/harvest_research_subjects.py --mint
```

The CLI dedupes (against live/archived articles, existing research notes, and
prior mints — NOT the Vetoed bank), mints up to the per-run cap (default 4,
P-ordered as you supply them), marks the scanned reviews, and updates state in
`../unfinishablemap_log/research-harvest-state.json` (outside cycle_post's
reach). Over-cap survivors are deferred, not lost — they re-surface only if a
future review re-raises them (they aren't re-read from the now-scanned file).

### 4. Report and stop

Summarise: how many reviews read, how many tasks minted (with slugs), how many
skipped and why. Do NOT commit — the loop's agent-commit step handles that. Do
NOT write the research notes themselves — that's the downstream research-topic
task the loop will pick from the queue.

## Important

- Dedupe is against ARTICLES + RESEARCH NOTES + prior mints, never the Vetoed
  bank — re-suppressing parked ideas would reinstate the stall this fixes.
- Only `topics`/`concepts` targets; the script rejects anything else.
- Per-run mint cap bounds queue growth; daily cadence keeps research flowing
  without flooding. Minted tasks chain research-topic → expand-topic → the new
  article lands in a section with cap headroom (caps raised to 300/300).
- If `--list-unscanned` is empty, exit cleanly — not an error.
