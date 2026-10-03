"""Low-level document model.

Content is written once (see ``content/``) and lowered to this small set of
blocks.  Three renderers (PDF, DOCX, Markdown) understand exactly these blocks,
which keeps the printed worksheets, the editable Word files and the GitHub
pages consistent with each other.

Inline markup supported in every string:

``**bold**``        bold text
``~~answer~~``      answer highlight (red, bold) used in teacher keys
``[[name]]``        inline icon (see :mod:`sinf.icons`), optional size in points
``[[name|34]]``     icon drawn 34 pt high
``\\n``              line break inside a paragraph or table cell
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Union

Block = Union[
    "Heading", "Para", "Bullets", "Table", "Box", "Lines", "Spacer",
    "PageBreak", "Group", "Rule",
]


@dataclass
class Heading:
    text: str
    level: int = 1  # 1..3


@dataclass
class Para:
    text: str
    style: str = "body"  # body | small | center | right | instruction | note


@dataclass
class Bullets:
    items: list[str]
    ordered: bool = False


@dataclass
class Table:
    rows: list[list[str]]
    widths: list[float] | None = None      # fractions of the text width
    header: bool = False                   # first row is a header row
    style: str = "grid"                    # grid | plain | cards | stage
    bg: list[list[str | None]] | None = None  # per-cell background colours
    align: str = "left"                    # left | center
    size: float | None = None              # font size override (pt)
    row_height: float | None = None        # minimum row height (mm)
    width_mm: float | None = None          # fixed total width (mm), centred


@dataclass
class Box:
    blocks: list["Block"]
    kind: str = "note"  # note | bank | grammar | tip | answer | script | draw
    title: str | None = None


@dataclass
class Lines:
    n: int = 1
    height: float = 9.0  # mm per line


@dataclass
class Spacer:
    h: float = 4.0  # mm


@dataclass
class PageBreak:
    pass


@dataclass
class Rule:
    pass


@dataclass
class Group:
    """Blocks that should stay together on one page (PDF only)."""
    blocks: list["Block"]


@dataclass
class Doc:
    title: str
    blocks: list["Block"] = field(default_factory=list)
    subtitle: str = ""
    badge: str = ""              # small label in the header, e.g. "Guess What! · Grade 3"
    kind: str = "worksheet"      # worksheet | lesson | test | reference
    name_line: bool = False      # print "Name / Date / Class" under the title
    footer: str = ""
    key: bool = False            # True when this is the teacher's answer key
