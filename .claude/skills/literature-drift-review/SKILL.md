---
name: literature-drift-review
description: Audit one topic article per run for stale citations against the live 2020s literature. Generates a refine-draft task when drift is detected.
---

# Literature-Drift Review

Audit a topic article whose empirical citations may have aged out of the live literature. One audit per invocation; one WebSearch call per run. This is Audit One of the [[project/calibration-audit-triple|calibration audit triple]] — the only audit in that triple requiring a dedicated skill, because the other two run on local content.

## When to Use

- Weekly wall-clock trigger: Tuesday at/after 05:00 UTC (gated by `state.last_runs["literature-drift-review"]` for same-day idempotency)
- When `/literature-drift-review [filepath]` is invoked manually
- When a queue task of type `literature-drift-review` is selected (the queue does not auto-generate these; manual escalation only)

The audit is **necessary** for topic articles in active-research areas where the 2020s literature has materially advanced (psychedelics, consciousness measurement, animal cognition, IIT empirical work, quantum biology). It is **advisory** for concept articles, philosophy-of-mind topic articles, and historical-survey articles where the literature is more stable. The skill refuses to audit articles outside the configured `active_research_sections` list — those use the existing `/deep-review` and `/refine-draft` channels.

## Instructions

### 1. Select Target Article

If a specific filepath is provided as argument, use it (subject to active-research-area check below).

Otherwise, read `obsidian/workflow/evolution-state.yaml` to get the `audit_triple.literature_drift.active_research_sections` list and the `recently_audited` list. Select the topic article matching one of the active-research-area patterns with the *oldest* `ai_modified` timestamp that has **not** been audited in the last 30 days.

```bash
uv run python -c "
import yaml
from pathlib import Path
from tools.curate.frontmatter import load_frontmatter

state = yaml.safe_load(Path('obsidian/workflow/evolution-state.yaml').read_text())
config = state.get('audit_triple', {}).get('literature_drift', {})
patterns = config.get('active_research_sections', [])
recently = set(config.get('recently_audited', []))

candidates = []
for path in Path('obsidian/topics').glob('*.md'):
    if path.stem in recently:
        continue
    if not any(p in path.stem for p in patterns):
        continue
    fm = load_frontmatter(path)
    candidates.append((fm.get('ai_modified') or fm.get('modified'), path))

candidates.sort()
if candidates:
    print(candidates[0][1])
else:
    print('NO_CANDIDATE')
"
```

If `NO_CANDIDATE`, log to changelog and exit successfully — every active-research article has been audited recently, which is the audit's success state.

### 2. Extract Article Metadata and Citations

Read the target article. Extract:

1. `ai_modified` (or `modified` as fallback) date from frontmatter → the audit baseline.
2. All citation years from the References section. Match against patterns `(\d{4})`, `et al\.\s+\d{4}`, `\d{4}-\d{2}-\d{2}`. Restrict to citations of empirical work — skip Map self-citations (`unfinishablemap.org`) and pre-2000 historical references that are clearly canonical (e.g., Husserl 1913, James 1890).
3. Compute the *median citation year* of the remaining empirical citations.
4. Identify the article's research-area keyword from the matched pattern in `active_research_sections` (e.g., `psychedelics`, `animal-cognition`, `iit`).

### 3. WebSearch for Recent High-Impact Papers

Use WebSearch (one call only, this is the audit's irreducible cost) to find the 3–5 most-recent (last 24 months from today's date) high-impact papers in the article's research area. Search query template:

```
{research_area_keyword} consciousness {current_year-2}..{current_year} review
```

Prefer results from:
- `nature.com`, `science.org`, `cell.com` and major neuroscience journals
- `*.harvard.edu`, `*.stanford.edu`, university lab pages with paper announcements
- `semanticscholar.org`, `pubmed.ncbi.nlm.nih.gov` listings
- Avoid: pre-prints unless very widely cited; popular-press summaries

For each result, capture: title, authors (first author + et al.), year, journal, one-sentence relevance to the article's central claim.

### 4. Compute Drift Signal

A drift signal is **raised** when both of the following hold:

1. The median citation year is more than `median_year_lag_threshold` years (default 5) behind `ai_modified` year.
2. At least `missing_citation_threshold` (default 2) of the WebSearch results are *topically appropriate* — they engage the article's central evidential frame — *and* are not cited in the article (check by author surname + year grep against the article body).

Thresholds are configurable in `evolution-state.yaml:audit_triple.literature_drift.{median_year_lag_threshold, missing_citation_threshold}`.

If the article matches the patterns but the article's evidential frame is *not* the framing the recent literature engages, this is **not** a drift signal — record the audit as `no-drift, frame-divergence` and do not generate a refine-draft task. Example: an article about psychedelics' phenomenology may legitimately not cite the 2024 Siegel paper on desynchronisation if the article's frame is qualitative-phenomenological rather than neural-correlate.

### 5. If Drift Detected: Generate refine-draft Task

Append to `obsidian/workflow/todo.md` under "Active Tasks":

```markdown
### P2: Update {article-slug} citations — {N} 2020s papers missing
- **Type**: refine-draft
- **Status**: pending
- **Notes**: From literature-drift audit {YYYY-MM-DD}. Article's empirical citations have median year {YYYY}, which is {N} years behind its last-modified date ({YYYY-MM-DD}). The 2024–{current_year} literature in the {research-area} area has materially advanced and the article does not engage the following high-impact papers, each topically appropriate to the article's central evidential frame:
  1. {Author et al. YYYY} — {one-sentence relevance}
  2. {Author et al. YYYY} — {one-sentence relevance}
  ...
  Action: integrate these citations into the article's evidence sections; reframe the central claim if the 2020s literature has shifted the dominant interpretive framing (e.g., from DMN-suppression-as-filter-loosening toward complexity-measure / predictive-processing accounts); preserve the article's existing voice and underdetermination markers. **Important**: do NOT inflate the article's evidential calibration on the basis of more citations — see [[project/evidential-status-discipline]]. If the new citations support the article's framing, this *constrains* the rivals; if they support a rival framing, the article must acknowledge that.
- **Source**: literature-drift-audit
- **Generated**: {YYYY-MM-DD}
```

If drift is **not** detected, no task is generated. Either outcome is a successful audit run.

### 6. Update audit-state tracking

Update `obsidian/workflow/evolution-state.yaml` under `audit_triple.literature_drift`:

1. Append the audited article slug to `recently_audited` (keep last 30 entries; oldest drop off).
2. Record `last_audit_date` as today (ISO date).
3. Increment `total_audits` and either `flagged_audits` or `clean_audits` depending on outcome.

These counters feed the falsification trigger documented in `project/calibration-audit-triple.md`: if `flagged_audits / total_audits` falls outside the 20–80% window over a 30-audit horizon, the thresholds need retuning at the next `/tune-system` pass.

### 7. Log to Changelog

Prepend to `obsidian/workflow/changelog.md` (after frontmatter, before existing entries):

```markdown
## [current time from prompt] - literature-drift-review
- **Status**: Success
- **Article**: [[{filepath-without-extension}]]
- **Research area**: {research-area-keyword}
- **Median citation year**: {YYYY} ({N} years behind ai_modified)
- **Recent papers found**: {count}
- **Missing topically-appropriate**: {count}
- **Outcome**: drift-flagged / no-drift / no-drift-frame-divergence
- **Task generated**: {task title or "none"}
```

## Why Wall-Clock Tuesday, Not Cycle-Trigger

The trigger is wall-clock weekly (Tuesday 05:00 UTC) rather than every-N-cycles. At the default `--interval 2400` (40 min), every 10 cycles ≈ 7 days, which would approximate weekly. But the loop's interval is user-tunable: at `--interval 14400` (4 hours), every 10 cycles is 40 days, not 7. A wall-clock trigger is cadence-stable across interval changes. The cost profile (one WebSearch call per run) is independent of speed, and the audit's purpose — keeping pace with the *external* literature cadence — is itself wall-clock-shaped, not session-shaped.

The trigger does not require Chrome and does not gate on the automation window. It runs Tuesday at/after 05:00 UTC, idempotency tracked by `state.last_runs["literature-drift-review"].date() != now.date()`. This places it after the 02–04 UTC commission cluster (which holds Chrome) and before the 08:00 UTC tweet trigger.

## What NOT to Do

- Don't audit more than one article per invocation — the cost gate is one WebSearch call.
- Don't audit articles outside the `active_research_sections` list — they use the existing review channels.
- Don't audit articles audited in the last 30 days — `recently_audited` enforces this.
- Don't generate a refine-draft task if the article's frame legitimately diverges from the recent literature's frame; record `frame-divergence` and skip.
- Don't *automatically* re-rank the refine-draft task above P2 — the task is a P2 default; human review can promote.
- Don't include pre-prints or popular-press summaries in the missing-citation list — only peer-reviewed work or widely-cited pre-prints.
- Don't run on concept articles or apex articles — both genres have different citation conventions and warrant a different audit shape.
- Don't conflate citation count with evidential weight — adding citations does not upgrade an article on the five-tier evidential-status scale (*established → strongly supported → realistic possibility → live hypothesis → speculative integration*); see [[project/evidential-status-discipline]].

## Important

- One WebSearch call per invocation (cost gate).
- Always update `recently_audited` to prevent re-auditing.
- Always log audit outcome to changelog, even when no drift is detected — the longitudinal record is the audit's own calibration data.
- The audit surfaces candidates; the subsequent `refine-draft` pass is responsible for dismissing false positives with notes recorded as audit-calibration data.
- Tenet alignment: [[tenets|Tenet 5 — Occam's Razor Has Limits]] applied at the corpus-management layer. A published article ages; the simpler editorial design ("published, therefore calibrated") lets drift accumulate silently. This audit is the operational refusal of that simpler design.
- See [[project/calibration-audit-triple]] for the wider audit family (audits two and three integrate into `/pessimistic-review` and `/refine-draft` rather than running as standalone skills).
