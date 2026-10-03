"""Unit specification and the builder that writes every file of a unit."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

from . import games, icons
from .exercises import Exercise, Section, sheet
from .lesson import Lesson, UnitInfo, plan_doc
from .model import Block, Doc, Heading, PageBreak, Para, Table
from .render_docx import render_docx
from .render_md import render_md
from .render_pdf import render_pdf


@dataclass
class V:
    """One vocabulary item: English, Uzbek, optional picture."""
    en: str
    uz: str
    icon: str | None = None
    ws: str | None = None    # single-word form for the word search (defaults to ``en`` if one word)


@dataclass
class UnitSpec:
    number: int
    slug: str
    title: str
    info: UnitInfo
    vocab: list[V]
    lessons: list[Lesson]
    worksheet_a: list
    worksheet_b: list
    quiz: list
    badge: str
    sheet_a_name: str = "Words"
    sheet_b_name: str = "Sentences"
    quiz_minutes: int = 15
    intro_note: str = ""
    extra_vocab: list[V] = field(default_factory=list)
    card: list[Block] = field(default_factory=list)     # one-page grammar / word card (PDF)
    card_name: str = "Grammar card"
    extra: list[Block] = field(default_factory=list)

    @property
    def label(self) -> str:
        return self.title if self.number == 0 else f"Unit {self.number} · {self.title}"

    def game_vocab(self) -> list[tuple[str, str | None]]:
        return [(v.en, v.icon) for v in self.vocab + self.extra_vocab]


def vocab_table(vocab: list[V], with_icons: bool = True) -> Table:
    rows = [["", "English", "O'zbekcha"] if with_icons else ["English", "O'zbekcha"]]
    for v in vocab:
        pic = f"[[{v.icon}|18]]" if v.icon and icons.has(v.icon) else ""
        rows.append([pic, f"**{v.en}**", v.uz] if with_icons else [f"**{v.en}**", v.uz])
    widths = [0.1, 0.4, 0.5] if with_icons else [0.5, 0.5]
    return Table(rows, widths=widths, header=True, style="grid", size=10.5)


def build_unit(spec: UnitSpec, root: Path) -> dict[str, list[Path]]:
    """Write plans, worksheets, keys, games and the unit README. Returns the created paths."""
    out = root / spec.slug
    made: dict[str, list[Path]] = {"plan": [], "sheets": [], "keys": [], "games": [], "readme": []}

    # ---- lesson plans (md + docx) -------------------------------------------
    intro = spec.info.blocks() + [Heading("Vocabulary", 2), vocab_table(spec.vocab)]
    if spec.extra_vocab:
        intro += [Heading("Extra words used in the lessons", 3), vocab_table(spec.extra_vocab)]
    if spec.intro_note:
        intro.insert(0, Para(spec.intro_note, "note"))
    plan = plan_doc(f"{spec.label} — Lesson plans", f"{len(spec.lessons)} lessons × 45 minutes",
                    spec.badge, intro, spec.lessons)
    made["plan"] += [render_md(plan, out / "lesson-plans.md"), render_docx(plan, out / "lesson-plans.docx")]

    # ---- worksheets & quiz (pdf + docx), one combined key ---------------------
    sheets = [
        ("worksheet-A", f"{spec.label} — Worksheet A", f"{spec.sheet_a_name}", spec.worksheet_a, "worksheet"),
        ("worksheet-B", f"{spec.label} — Worksheet B", f"{spec.sheet_b_name}", spec.worksheet_b, "worksheet"),
        ("quiz", f"{spec.label} — Quick quiz", f"{spec.quiz_minutes} minutes", spec.quiz, "test"),
    ]
    key_blocks: list[Block] = []
    for i, (fname, title, sub, items, kind) in enumerate(sheets):
        d = sheet(title, items, subtitle=sub, badge=spec.badge, kind=kind)
        made["sheets"] += [render_pdf(d, out / "worksheets" / f"{fname}.pdf"),
                           render_docx(d, out / "worksheets" / f"{fname}.docx")]
        k = sheet(title, items, subtitle=sub, badge=spec.badge, key=True, kind=kind)
        if i:
            key_blocks.append(PageBreak())
        key_blocks.append(Heading(f"{title.split('—')[1].strip()} ({sub})", 1))
        key_blocks.extend(k.blocks)
    key_doc = Doc(title=f"{spec.label} — Answer keys", blocks=key_blocks, badge=spec.badge, key=True,
                  subtitle="Worksheet A · Worksheet B · Quiz")
    made["keys"].append(render_pdf(key_doc, out / "worksheets" / "answer-keys.pdf"))

    # ---- grammar / word card ---------------------------------------------------
    if spec.card:
        card = Doc(title=f"{spec.label} — {spec.card_name}", blocks=spec.card, badge=spec.badge,
                   subtitle="Stick it in the notebook or on the wall", kind="reference")
        made["games"].append(render_pdf(card, out / "grammar-card.pdf"))

    # ---- games ----------------------------------------------------------------
    gv = spec.game_vocab()
    fc = Doc(title=f"{spec.label} — Flashcards", blocks=games.flashcard_blocks(gv), badge=spec.badge,
             subtitle="Cut along the lines · A5 cards", footer="3-sinf · flashcards · emoji: Twemoji (CC-BY 4.0)")
    bingo = Doc(title=f"{spec.label} — Bingo", blocks=games.bingo_blocks(spec.label, gv), badge=spec.badge,
                subtitle="8 different 3×3 cards + caller sheet")
    mem = Doc(title=f"{spec.label} — Pairs (memory game)", blocks=games.memory_blocks(gv), badge=spec.badge,
              subtitle="Picture + word cards")
    for name, d in (("flashcards", fc), ("bingo", bingo), ("memory-pairs", mem)):
        made["games"].append(render_pdf(d, out / "games" / f"{name}.pdf"))

    # ---- unit README ------------------------------------------------------------
    made["readme"].append(write_unit_readme(spec, out))
    return made


def write_unit_readme(spec: UnitSpec, out: Path) -> Path:
    lines = [
        f"# {spec.label}",
        "",
        f"*{spec.badge}* — {spec.info.topic}",
        "",
        "## Files",
        "",
        "| What | Open |",
        "|---|---|",
        f"| Lesson plans ({len(spec.lessons)} × 45 min) | [lesson-plans.md](lesson-plans.md) · "
        "[Word](lesson-plans.docx) |",
        "| Worksheet A | [PDF](worksheets/worksheet-A.pdf) · [Word](worksheets/worksheet-A.docx) |",
        "| Worksheet B | [PDF](worksheets/worksheet-B.pdf) · [Word](worksheets/worksheet-B.docx) |",
        f"| Quick quiz ({spec.quiz_minutes} min) | [PDF](worksheets/quiz.pdf) · [Word](worksheets/quiz.docx) |",
        "| Answer keys (teacher only) | [PDF](worksheets/answer-keys.pdf) |",
        *([f"| {spec.card_name} (1 page) | [PDF](grammar-card.pdf) |"] if spec.card else []),
        "| Flashcards (A5) | [PDF](games/flashcards.pdf) |",
        "| Bingo (8 cards + caller sheet) | [PDF](games/bingo.pdf) |",
        "| Pairs / memory game | [PDF](games/memory-pairs.pdf) |",
        "",
        "## Unit at a glance",
        "",
    ]
    if spec.info.book:
        lines.append(f"- **In the book:** {spec.info.book}")
    lines.append(f"- **Vocabulary:** {spec.info.vocabulary}")
    lines += [f"- **Grammar:** {g}" for g in spec.info.grammar]
    for label, value in (("Skills", spec.info.skills), ("Say it!", spec.info.phonics),
                         ("Story value", spec.info.story_value), ("Talk time", spec.info.talk_time),
                         ("CLIL", spec.info.clil)):
        if value.strip():
            lines.append(f"- **{label}:** {value}")
    lines += ["", "## Lessons", ""]
    lines += [f"{i}. {l.title} — *{l.focus}*" for i, l in enumerate(spec.lessons, 1)]
    lines += ["", "## Vocabulary (English – O'zbekcha)", "", "| | English | O'zbekcha |", "|---|---|---|"]
    for v in spec.vocab:
        lines.append(f"| {icons.char(v.icon) if v.icon else ''} | **{v.en}** | {v.uz} |")
    if spec.extra_vocab:
        lines += ["", "### Extra words used in the lessons", "", "| | English | O'zbekcha |", "|---|---|---|"]
        for v in spec.extra_vocab:
            lines.append(f"| {icons.char(v.icon) if v.icon else ''} | **{v.en}** | {v.uz} |")
    path = out / "README.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return path


def picture_card(vocab: list[V], title: str, cols: int = 4, tip: str = "") -> list[Block]:
    """One-page picture dictionary (for vocabulary mini-units): icon + English word + Uzbek."""
    items = [v for v in vocab if v.icon and icons.has(v.icon)]
    cells = [f"[[{v.icon}|44]]\n**{v.en}**\n{v.uz}" for v in items]
    rows = [cells[i:i + cols] + [""] * (cols - len(cells[i:i + cols])) for i in range(0, len(cells), cols)]
    blocks: list[Block] = [Heading(title, 1),
                           Table(rows, widths=[1] * cols, style="grid", align="center", size=10.5, row_height=34)]
    if tip:
        from .model import Box
        blocks.append(Box([Para(tip)], kind="tip", title="Eslatma"))
    return blocks
