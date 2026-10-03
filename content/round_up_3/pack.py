"""Round-Up 3 pack registry and pack-level documents."""
from __future__ import annotations

import math
from pathlib import Path

from sinf.model import Doc, Heading, Para, Table
from sinf.progress import build_progress_tests
from sinf.render_docx import render_docx
from sinf.render_md import render_md
from sinf.render_pdf import render_pdf

from . import (
    unit1_plurals, unit2_be_have_can, unit3_possessives, unit4_articles, unit5_quantity, unit6_present_simple,
    unit7_present_continuous, unit8_prepositions_imperatives,
)
from .common import BADGE
from .progress_tests import TESTS

UNITS = [m.SPEC for m in (unit1_plurals, unit2_be_have_can, unit3_possessives, unit4_articles, unit5_quantity,
                          unit6_present_simple, unit7_present_continuous, unit8_prepositions_imperatives)]

# Unit order follows the contents list of the Round-Up 3 Teacher's Guide (Longman, 2003 edition).
BOOK_UNITS = [
    ("1", "Plurals of countable and uncountable nouns", "yes", "unit-1-plurals-a-an-some"),
    ("2", "Personal pronouns / 'be' / 'have got' / 'can'", "yes", "unit-2-be-have-got-can"),
    ("3", "Possessives / Demonstratives", "yes", "unit-3-possessives-this-that"),
    ("4", "Articles", "yes", "unit-4-articles"),
    ("5", "Expressing quantity", "yes", "unit-5-how-many-how-much"),
    ("6", "Indefinite pronouns (something, anyone …)", "later", "Above Grade 3 — keep for Grade 4"),
    ("7", "Present simple", "yes", "unit-6-present-simple"),
    ("8", "Present continuous", "yes", "unit-7-present-continuous"),
    ("9", "Past simple", "later", "Not in the Grade 3 syllabus — keep for Grade 4"),
    ("10", "Present perfect", "later", "Above A1"),
    ("11", "The future (will / be going to)", "later", "Above A1"),
    ("12", "Yes / no questions and Wh- questions", "partly", "Questions are practised inside every mini-unit"),
    ("13", "Prepositions of place / movement / time", "partly (place)", "unit-8-prepositions-imperatives"),
    ("14", "The imperative", "yes", "unit-8-prepositions-imperatives"),
    ("15", "Adjectives / adverbs / comparisons", "later", "Comparatives are not needed yet"),
    ("16", "Modal verbs", "partly (can)", "can / can't is in unit-2-be-have-got-can"),
    ("17", "Infinitive / -ing form / too – enough", "later", "Above A1"),
]


def _plan_doc() -> Doc:
    rows = [["#", "Week", "Mini-unit", "Lesson"]]
    n = 0
    for unit in UNITS:
        for lesson in unit.lessons:
            n += 1
            rows.append([str(n), str(math.ceil(n / 2)), f"{unit.number}. {unit.title}", f"**{lesson.title}**"])
        if unit.number in (4, 8):
            n += 1
            label = "Progress test A" if unit.number == 4 else "Progress test B"
            rows.append([str(n), str(math.ceil(n / 2)), "Tests", f"**{label}** (30 points)"])
    blocks = [Para("A suggested order for **26 lessons** (one or two per week, for example as an extra grammar lesson or "
                   "in the school's elective hour). The mini-units are independent, so you can also pick the one that "
                   "matches the Guess What! unit you are teaching — see the curriculum bridge in docs/.", "note"),
              Table(rows, widths=[0.07, 0.09, 0.4, 0.44], header=True, style="stage", size=10)]
    return Doc(title="Suggested plan", blocks=blocks, badge=BADGE, subtitle="Round-Up 3 bridge · 26 lessons", kind="lesson")


def _book_map() -> Doc:
    rows = [["Book unit", "Topic in Round-Up 3", "In this pack?", "Where / why"]]
    for num, topic, used, where in BOOK_UNITS:
        rows.append([num, topic, used, where])
    blocks = [
        Para("Round-Up 3 is an **elementary grammar practice book** for older learners (its Teacher's Guide says levels "
             "1–3 are for the early stages of learning English). Grade 3 pupils are age 8–9 and work at CEFR A1, so "
             "only the units that match A1 are used here, and they are rewritten with pictures, short texts and "
             "games. Unit numbers follow the contents list of the 2003 Longman edition; check them against your copy.",
             "note"),
        Table(rows, widths=[0.1, 0.4, 0.15, 0.35], header=True, style="grid", size=9.5),
    ]
    return Doc(title="Round-Up 3 book map", blocks=blocks, badge=BADGE, subtitle="Which units are used for Grade 3",
               kind="reference")


def build_extras(pack_root: Path) -> list[Path]:
    made: list[Path] = []
    made += build_progress_tests(pack_root / "tests", BADGE, TESTS)
    plan, bmap = _plan_doc(), _book_map()
    made += [render_md(plan, pack_root / "plan.md"), render_pdf(plan, pack_root / "plan.pdf"),
             render_docx(plan, pack_root / "plan.docx"), render_md(bmap, pack_root / "book-map.md"),
             render_pdf(bmap, pack_root / "book-map.pdf")]
    lines = [
        "# Round-Up 3 — 3-sinf (Grade 3) uchun grammatika paketi",
        "",
        "Virginia Evans, *Round-Up 3* (Longman / Pearson) grammatika kitobi asosida **original** materiallar: "
        "3-sinfga (8–9 yosh, CEFR A1) moslashtirilgan 8 ta grammatika mini-uniti. Kitobning o'z mashqlari yoki "
        "rasmlari bu yerda **yo'q**.",
        "",
        "> **Muhim:** Google Drive papkangizda Round-Up 3 fayllari topilmadi. Mini-unitlar kitobning rasmiy "
        "mundarijasi (17 unit) asosida tuzilgan va faqat A1 darajasiga mos bo'limlar olingan. "
        "Kitob nusxangiz bo'lsa — [book-map.md](book-map.md) orqali mos bo'limni toping.",
        "",
        "## Nimalar bor",
        "",
        "| Nima | Fayl |",
        "|---|---|",
        "| Tavsiya etilgan reja (26 dars) | [plan.md](plan.md) · [PDF](plan.pdf) · [Word](plan.docx) |",
        "| Kitob xaritasi (qaysi unitlar olingan va nima uchun) | [book-map.md](book-map.md) · [PDF](book-map.pdf) |",
        "| Progress test A (1–4) va B (5–8), kalitlari bilan (30 ball) | [tests/](tests/) |",
        "",
        "## Mini-unitlar",
        "",
        "Har birida: 3 ta dars rejasi, 1 sahifalik **grammatika kartasi**, 2 ta ish varag'i, quick quiz, kalitlar, "
        "flashcards, bingo va memory o'yini.",
        "",
        "| # | Mavzu | Kitobda | Ochish |",
        "|---|---|---|---|",
    ]
    for u in UNITS:
        lines.append(f"| {u.number} | {u.title} | {u.info.book} | [{u.slug}/]({u.slug}/README.md) |")
    lines += ["", "Rasmlar — Twemoji (CC-BY 4.0), shrift — Andika (SIL OFL): [../NOTICE.md](../NOTICE.md).", ""]
    path = pack_root / "README.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    made.append(path)
    return made
