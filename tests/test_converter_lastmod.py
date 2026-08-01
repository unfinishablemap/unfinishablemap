"""Tests for Hugo `lastmod` derivation in the Obsidian -> Hugo sync.

Regression cover for the 2026-08-01 defect: Hugo's default `.Lastmod` cascade is
`lastmod` -> `modified` -> `date`, but the Map only maintains `ai_modified` and
`human_modified`. With no `lastmod` emitted, every served `dateModified`,
`article:modified_time`, sitemap `<lastmod>` and section-index "last modified"
column was pinned to the page's creation date -- 1,226 of 7,740 pages stale,
some by over 200 days.
"""

import datetime

import frontmatter

from tools.sync.converter import convert_file, derive_lastmod

UTC = datetime.timezone.utc


class TestDeriveLastmod:
    def test_prefers_ai_modified_over_stale_modified_and_date(self) -> None:
        """The canonical defect shape: date/modified pinned at creation."""
        assert derive_lastmod(
            {
                "date": datetime.date(2026, 5, 18),
                "modified": datetime.date(2026, 5, 18),
                "ai_modified": datetime.datetime(2026, 8, 1, 18, 28, 7, tzinfo=UTC),
            }
        ) == datetime.datetime(2026, 8, 1, 18, 28, 7, tzinfo=UTC)

    def test_prefers_human_modified_when_it_is_newest(self) -> None:
        assert derive_lastmod(
            {
                "date": datetime.date(2026, 1, 2),
                "ai_modified": datetime.datetime(2026, 3, 1, tzinfo=UTC),
                "human_modified": datetime.datetime(2026, 6, 9, 11, 0, tzinfo=UTC),
            }
        ) == datetime.datetime(2026, 6, 9, 11, 0, tzinfo=UTC)

    def test_mixed_naive_and_aware_does_not_raise(self) -> None:
        """A naive datetime must not trigger the naive/aware comparison TypeError."""
        assert derive_lastmod(
            {
                "date": "2026-01-02",
                "ai_modified": datetime.datetime(2026, 2, 3, 4, 5, 6),  # naive
            }
        ) == datetime.datetime(2026, 2, 3, 4, 5, 6, tzinfo=UTC)

    def test_same_day_datetime_beats_date_only(self) -> None:
        """A date-only value normalises to midnight, so a same-day time wins."""
        assert derive_lastmod(
            {
                "modified": datetime.date(2026, 8, 1),
                "ai_modified": datetime.datetime(2026, 8, 1, 18, 28, 7, tzinfo=UTC),
            }
        ) == datetime.datetime(2026, 8, 1, 18, 28, 7, tzinfo=UTC)

    def test_null_and_unparseable_values_are_ignored(self) -> None:
        assert derive_lastmod(
            {
                "date": datetime.date(2026, 1, 1),
                "ai_modified": None,
                "human_modified": "not a date",
                "modified": "",
            }
        ) == datetime.datetime(2026, 1, 1, tzinfo=UTC)

    def test_iso_string_with_z_suffix(self) -> None:
        assert derive_lastmod(
            {"ai_modified": "2026-03-04T05:06:07Z"}
        ) == datetime.datetime(2026, 3, 4, 5, 6, 7, tzinfo=UTC)

    def test_non_utc_offset_is_normalised_to_utc(self) -> None:
        assert derive_lastmod(
            {"ai_modified": "2026-03-04T10:00:00+02:00"}
        ) == datetime.datetime(2026, 3, 4, 8, 0, 0, tzinfo=UTC)

    def test_date_acts_as_a_floor(self) -> None:
        """lastmod must never predate publication."""
        assert derive_lastmod(
            {
                "date": datetime.date(2026, 9, 9),
                "ai_modified": datetime.date(2026, 1, 1),
            }
        ) == datetime.datetime(2026, 9, 9, tzinfo=UTC)

    def test_returns_none_when_no_dates_present(self) -> None:
        assert derive_lastmod({}) is None
        assert derive_lastmod({"title": "x", "ai_modified": None}) is None

    def test_returns_a_distinct_object_not_an_input(self) -> None:
        """Sharing the object with ai_modified makes PyYAML emit anchor/alias pairs,
        which renumbers every anchor in the file and buries the real diff."""
        ai = datetime.datetime(2026, 8, 1, 18, 28, 7, tzinfo=UTC)
        assert derive_lastmod({"ai_modified": ai}) is not ai


class TestConvertFileEmitsLastmod:
    def _write(self, tmp_path, body: str):
        src = tmp_path / "sample.md"
        src.write_text(body)
        return src

    def test_lastmod_emitted_and_date_untouched(self, tmp_path) -> None:
        src = self._write(
            tmp_path,
            "---\n"
            "title: Sample\n"
            "date: 2026-05-18\n"
            "modified: 2026-05-18\n"
            "ai_modified: 2026-08-01T18:28:07+00:00\n"
            "---\n\nBody.\n",
        )
        out = frontmatter.loads(convert_file(src))
        assert out.metadata["lastmod"] == datetime.datetime(2026, 8, 1, 18, 28, 7, tzinfo=UTC)
        # `date` is the publication date: it feeds section ordering and JSON-LD
        # `datePublished`, and must not move.
        assert out.metadata["date"] == datetime.date(2026, 5, 18)

    def test_lastmod_emitted_even_when_only_date_present(self, tmp_path) -> None:
        src = self._write(
            tmp_path, "---\ntitle: Sample\ndate: 2026-05-18\n---\n\nBody.\n"
        )
        out = frontmatter.loads(convert_file(src))
        assert out.metadata["lastmod"] == datetime.datetime(2026, 5, 18, tzinfo=UTC)

    def test_serialised_output_has_no_yaml_alias_for_lastmod(self, tmp_path) -> None:
        src = self._write(
            tmp_path,
            "---\ntitle: Sample\ndate: 2026-05-18\nmodified: 2026-05-18\n"
            "ai_modified: 2026-08-01T18:28:07+00:00\n---\n\nBody.\n",
        )
        rendered = convert_file(src)
        assert "lastmod: 2026-08-01 18:28:07+00:00" in rendered
        assert "lastmod: *" not in rendered
