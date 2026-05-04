"""HTML → markdown extraction for ChatGPT assistant responses.

The collect skill captures the raw innerHTML of the last assistant message's
.markdown element via JS, then pipes it to this module to produce clean
markdown. ChatGPT's rendered HTML is well-structured (paragraphs, headings,
lists, inline links, tables, blockquotes, code) so a focused converter using
only html.parser from the stdlib is sufficient.
"""

import html
import re
from html.parser import HTMLParser
from typing import Optional


class _Markdownifier(HTMLParser):
    """Convert ChatGPT's rendered markdown HTML back to markdown."""

    BLOCK_TAGS = {
        "p", "h1", "h2", "h3", "h4", "h5", "h6",
        "ul", "ol", "li", "blockquote", "pre",
        "table", "thead", "tbody", "tr", "th", "td",
        "div", "hr",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.list_stack: list[tuple[str, int]] = []  # (type, counter)
        self.in_pre = False
        self.in_code = False
        self.link_href: Optional[str] = None
        self.link_text_buf: list[str] = []
        self.collecting_link_text = False
        # Table state
        self.in_table = False
        self.current_row: list[str] = []
        self.current_cell: list[str] = []
        self.in_cell = False
        self.is_header_row = False
        self.table_rows: list[list[str]] = []
        self.table_header: list[str] = []
        self.in_blockquote = False

    # ----- Helpers ---------------------------------------------------------
    def _emit(self, s: str) -> None:
        if self.collecting_link_text:
            self.link_text_buf.append(s)
        elif self.in_cell:
            self.current_cell.append(s)
        else:
            self.parts.append(s)

    def _ensure_blank_line(self) -> None:
        text = "".join(self.parts)
        if text.endswith("\n\n") or text == "":
            return
        if text.endswith("\n"):
            self.parts.append("\n")
        else:
            self.parts.append("\n\n")

    def _ensure_newline(self) -> None:
        text = "".join(self.parts)
        if text == "" or text.endswith("\n"):
            return
        self.parts.append("\n")

    # ----- Tag handlers ----------------------------------------------------
    def handle_starttag(self, tag: str, attrs: list[tuple[str, Optional[str]]]) -> None:
        attr_dict = dict(attrs)

        if tag in {"strong", "b"}:
            self._emit("**")
        elif tag in {"em", "i"}:
            self._emit("*")
        elif tag == "code" and not self.in_pre:
            self.in_code = True
            self._emit("`")
        elif tag == "pre":
            self.in_pre = True
            self._ensure_blank_line()
            self.parts.append("```\n")
        elif tag == "br":
            self._emit("  \n")
        elif tag == "hr":
            self._ensure_blank_line()
            self.parts.append("---\n\n")
        elif tag.startswith("h") and len(tag) == 2 and tag[1].isdigit():
            level = int(tag[1])
            self._ensure_blank_line()
            self.parts.append("#" * level + " ")
        elif tag == "p":
            self._ensure_blank_line()
        elif tag == "ul":
            self.list_stack.append(("ul", 0))
            self._ensure_newline()
        elif tag == "ol":
            self.list_stack.append(("ol", 0))
            self._ensure_newline()
        elif tag == "li":
            if self.list_stack:
                kind, counter = self.list_stack[-1]
                indent = "  " * (len(self.list_stack) - 1)
                if kind == "ul":
                    self.parts.append(f"{indent}- ")
                else:
                    self.list_stack[-1] = (kind, counter + 1)
                    self.parts.append(f"{indent}{counter + 1}. ")
        elif tag == "blockquote":
            self.in_blockquote = True
            self._ensure_blank_line()
        elif tag == "a":
            self.link_href = attr_dict.get("href")
            self.collecting_link_text = True
            self.link_text_buf = []
        elif tag == "table":
            self.in_table = True
            self.table_rows = []
            self.table_header = []
            self._ensure_blank_line()
        elif tag == "tr":
            self.current_row = []
            self.is_header_row = False
        elif tag in {"th", "td"}:
            self.in_cell = True
            self.current_cell = []
            if tag == "th":
                self.is_header_row = True

    def handle_endtag(self, tag: str) -> None:
        if tag in {"strong", "b"}:
            self._emit("**")
        elif tag in {"em", "i"}:
            self._emit("*")
        elif tag == "code" and not self.in_pre:
            self._emit("`")
            self.in_code = False
        elif tag == "pre":
            self._ensure_newline()
            self.parts.append("```\n\n")
            self.in_pre = False
        elif tag.startswith("h") and len(tag) == 2 and tag[1].isdigit():
            self.parts.append("\n\n")
        elif tag == "p":
            self.parts.append("\n\n")
        elif tag in {"ul", "ol"}:
            if self.list_stack:
                self.list_stack.pop()
            if not self.list_stack:
                self.parts.append("\n")
        elif tag == "li":
            self._ensure_newline()
        elif tag == "blockquote":
            self.in_blockquote = False
            self.parts.append("\n")
        elif tag == "a":
            text = "".join(self.link_text_buf).strip()
            href = self.link_href or ""
            self.collecting_link_text = False
            self.link_href = None
            if text and href:
                self._emit(f"[{text}]({href})")
            else:
                self._emit(text)
        elif tag in {"th", "td"}:
            self.in_cell = False
            cell = "".join(self.current_cell).strip()
            cell = cell.replace("|", r"\|").replace("\n", " ")
            self.current_row.append(cell)
        elif tag == "tr":
            if self.is_header_row and not self.table_header:
                self.table_header = self.current_row
            else:
                self.table_rows.append(self.current_row)
            self.current_row = []
        elif tag == "table":
            self._render_table()
            self.in_table = False
            self.table_rows = []
            self.table_header = []

    def handle_data(self, data: str) -> None:
        if self.in_pre:
            self.parts.append(data)
            return
        if self.collecting_link_text:
            self.link_text_buf.append(data)
            return
        if self.in_cell:
            self.current_cell.append(data)
            return
        # Outside pre/code, collapse interior newlines but preserve content
        if not data.strip():
            # Whitespace between blocks — preserve a single space
            text = "".join(self.parts)
            if text and not text.endswith((" ", "\n")):
                self.parts.append(" ")
            return
        self.parts.append(data)

    # ----- Tables ----------------------------------------------------------
    def _render_table(self) -> None:
        if not self.table_header and self.table_rows:
            # No header detected; promote first row to header
            self.table_header = self.table_rows[0]
            self.table_rows = self.table_rows[1:]
        if not self.table_header:
            return
        cols = len(self.table_header)
        sep = ["---"] * cols
        lines = [
            "| " + " | ".join(self.table_header) + " |",
            "| " + " | ".join(sep) + " |",
        ]
        for row in self.table_rows:
            # Pad short rows
            while len(row) < cols:
                row.append("")
            lines.append("| " + " | ".join(row[:cols]) + " |")
        self.parts.append("\n".join(lines) + "\n\n")

    # ----- Result ----------------------------------------------------------
    def result(self) -> str:
        text = "".join(self.parts)
        # Decode any remaining entities defensively
        text = html.unescape(text)
        # Normalize whitespace: collapse runs of >=3 newlines to 2
        text = re.sub(r"\n{3,}", "\n\n", text)
        # Strip trailing whitespace per line
        text = "\n".join(line.rstrip() for line in text.splitlines())
        return text.strip() + "\n"


def html_to_markdown(html_text: str) -> str:
    """Convert ChatGPT-rendered markdown HTML back to markdown source."""
    parser = _Markdownifier()
    parser.feed(html_text)
    parser.close()
    return parser.result()
