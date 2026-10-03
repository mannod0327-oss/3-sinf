"""Destination A1 pack registry and pack-level documents."""
from __future__ import annotations

import math
from pathlib import Path

from sinf.model import Doc, Para, Table
from sinf.progress import build_progress_tests
from sinf.render_docx import render_docx
from sinf.render_md import render_md
from sinf.render_pdf import render_pdf

from . import (
    unit1_be_there, unit2_present_simple_jobs, unit3_my_home, unit4_present_continuous, unit5_hobbies,
    unit6_school_life, unit7_food_shopping, unit8_weather_seasons, unit9_clothes,
)
from .common import BADGE
from .progress_tests import TESTS

UNITS = [m.SPEC for m in (unit1_be_there, unit2_present_simple_jobs, unit3_my_home, unit4_present_continuous,
                          unit5_hobbies, unit6_school_life, unit7_food_shopping, unit8_weather_seasons, unit9_clothes)]

# Unit order follows the contents list of Destination A1 Plus (Macmillan Education, 2017, 42 units).
BOOK_UNITS = [
    ("1", "Grammar: to be; there is / there are; it's; this / these / that / those", "yes", "unit-1-be-there-is-this-that"),
    ("2", "Grammar: Present simple 1", "yes", "unit-2-present-simple-jobs"),
    ("3", "Vocabulary: My home", "yes", "unit-3-my-home"),
    ("4", "Grammar: Present simple 2", "yes", "unit-2-present-simple-jobs (negatives and questions)"),
    ("5", "Grammar: Present continuous", "yes", "unit-4-present-continuous-park"),
    ("6", "Vocabulary: Hobbies and pastimes", "yes", "unit-5-hobbies-pastimes"),
    ("7", "Grammar: Present simple and present continuous", "partly", "Both tenses are practised in mini-units 2, 4 and 5; "
                                                                       "the contrast itself is for Grade 4"),
    ("8", "Grammar: Past simple 1", "later", "Not in the Grade 3 syllabus — keep for Grade 4"),
    ("9", "Vocabulary: School life", "yes", "unit-6-school-life"),
    ("10", "Grammar: Past simple 2", "later", "Above A1 for Grade 3"),
    ("11", "Grammar: Past continuous", "later", "Above A1 for Grade 3"),
    ("12", "Vocabulary: Making friends and getting to know people", "later",
     "Names, age and questions are revised in Guess What! Unit 0 (Welcome)"),
    ("13", "Grammar: Present perfect 1", "later", "Above A1"),
    ("14", "Grammar: Present perfect 2", "later", "Above A1"),
    ("15", "Vocabulary: Travel", "later", "Keep for Grade 4"),
    ("16", "Grammar: Present perfect and past simple", "later", "Above A1"),
    ("17", "Grammar: will and be going to", "later", "Above A1"),
    ("18", "Vocabulary: Sports and healthy lifestyle", "later", "Sports words are in unit-5-hobbies-pastimes"),
    ("19", "Grammar: Modal verbs 1", "later", "can / can't is in Round-Up 3 mini-unit 2"),
    ("20", "Grammar: Modal verbs 2", "later", "Above A1"),
    ("21", "Vocabulary: Rules", "later", "Keep for Grade 4"),
    ("22", "Grammar: Plurals, countable and uncountable nouns 1", "yes", "unit-7-food-shopping"),
    ("23", "Grammar: Countable and uncountable nouns 2", "yes", "unit-7-food-shopping"),
    ("24", "Vocabulary: Food and shopping", "yes", "unit-7-food-shopping"),
    ("25", "Grammar: have and have got, some and any", "partly", "some / any in mini-unit 7, has got in mini-unit 9"),
    ("26", "Grammar: Wh-questions and question tags", "partly", "Wh-questions appear in every mini-unit; "
                                                                 "question tags are for later"),
    ("27", "Vocabulary: Character and appearance", "yes", "unit-9-clothes-appearance"),
    ("28", "Grammar: Articles", "partly", "Round-Up 3 mini-unit 4 (articles)"),
    ("29", "Grammar: Numerals", "partly", "Numbers and prices in mini-unit 7; more numbers in Guess What! Unit 7 (At the market)"),
    ("30", "Vocabulary: Weather and seasons, nature and ecology", "yes", "unit-8-weather-seasons"),
    ("31", "Grammar: Possessive 's, Whose …?", "partly", "Round-Up 3 mini-unit 3 (possessives)"),
    ("32", "Grammar: Pronouns and possessive determiners", "partly", "Round-Up 3 mini-units 2 and 3"),
    ("33", "Vocabulary: Clothes and fashion", "yes", "unit-9-clothes-appearance"),
    ("34", "Grammar: Relative pronouns and adverbs, relative clauses", "later", "Above A1"),
    ("35", "Grammar: First conditional", "later", "Above A1"),
    ("36", "Vocabulary: Jobs and professions", "yes", "unit-2-present-simple-jobs"),
    ("37", "Grammar: Comparatives, as … as", "later", "Keep for Grade 4"),
    ("38", "Grammar: Superlatives", "later", "Keep for Grade 4"),
    ("39", "Vocabulary: Famous people and places", "later", "Keep for Grade 4"),
    ("40", "Grammar: Imperative, infinitive, -ing form, I'd like …", "partly",
     "Imperatives in Round-Up 3 mini-unit 8, -ing after like in mini-unit 5, I'd like in mini-unit 7"),
    ("41", "Grammar: Prepositions of place, movement and time", "partly",
     "Place: mini-unit 3 and Round-Up 3 mini-unit 8; time (at seven o'clock): Guess What! Unit 4 (My day)"),
    ("42", "Vocabulary: Communication and technology", "later", "Computer words start in mini-unit 1"),
]


def _plan_doc() -> Doc:
    rows = [["#", "Week", "Mini-unit", "Lesson"]]
    n = 0
    for unit in UNITS:
        for lesson in unit.lessons:
            n += 1
            rows.append([str(n), str(math.ceil(n / 2)), f"{unit.number}. {unit.title}", f"**{lesson.title}**"])
        if unit.number in (5, 9):
            n += 1
            label = "Progress test A" if unit.number == 5 else "Progress test B"
            rows.append([str(n), str(math.ceil(n / 2)), "Tests", f"**{label}** (30 points)"])
    blocks = [Para("A suggested order for **29 lessons** (27 lessons and 2 tests; one or two per week, for example as an "
                   "extra lesson or in the school's elective hour). The mini-units are independent, so you can also pick "
                   "the one that matches the Guess What! unit you are teaching — see the curriculum bridge in docs/.",
                   "note"),
              Table(rows, widths=[0.07, 0.09, 0.4, 0.44], header=True, style="stage", size=10)]
    return Doc(title="Suggested plan", blocks=blocks, badge=BADGE, subtitle="Destination A1 bridge · 29 lessons", kind="lesson")


def _book_map() -> Doc:
    rows = [["Book unit", "Topic in Destination A1", "In this pack?", "Where / why"]]
    for num, topic, used, where in BOOK_UNITS:
        rows.append([num, topic, used, where])
    blocks = [
        Para("Destination A1 (Macmillan Education) is a **vocabulary and grammar practice book** with 42 units. Grade 3 "
             "pupils are age 8–9 and work at CEFR A1, so only the units that match A1 are used here, and they are "
             "rewritten with pictures, short texts and games. Unit numbers follow the contents list of the 2017 "
             "*Destination A1 Plus* edition; check them against your copy, because other editions can differ.", "note"),
        Table(rows, widths=[0.1, 0.4, 0.15, 0.35], header=True, style="grid", size=9),
    ]
    return Doc(title="Destination A1 book map", blocks=blocks, badge=BADGE, subtitle="Which units are used for Grade 3",
               kind="reference")


def build_extras(pack_root: Path) -> list[Path]:
    made: list[Path] = []
    made += build_progress_tests(pack_root / "tests", BADGE, TESTS)
    plan, bmap = _plan_doc(), _book_map()
    made += [render_md(plan, pack_root / "plan.md"), render_pdf(plan, pack_root / "plan.pdf"),
             render_docx(plan, pack_root / "plan.docx"), render_md(bmap, pack_root / "book-map.md"),
             render_pdf(bmap, pack_root / "book-map.pdf")]
    lines = [
        "# Destination A1 — 3-sinf (Grade 3) uchun lug'at va grammatika paketi",
        "",
        "Macmillan *Destination A1* (lug'at va grammatika mashqlari kitobi) mavzulari asosida **original** materiallar: "
        "3-sinfga (8–9 yosh, CEFR A1) moslashtirilgan 9 ta mini-unit. Kitobning o'z mashqlari, matnlari yoki "
        "rasmlari bu yerda **yo'q**.",
        "",
        "> **Muhim:** Google Drive papkangizda Destination A1 fayllari topilmadi. Mini-unitlar kitobning rasmiy "
        "mundarijasi (*Destination A1 Plus*, 42 unit) asosida tuzilgan va faqat A1 darajasiga mos bo'limlar olingan. "
        "Kitob nusxangiz bo'lsa — [book-map.md](book-map.md) orqali mos bo'limni toping; nashrlar farq qilishi mumkin.",
        "",
        "## Nimalar bor",
        "",
        "| Nima | Fayl |",
        "|---|---|",
        "| Tavsiya etilgan reja (29 dars: 27 dars + 2 test) | [plan.md](plan.md) · [PDF](plan.pdf) · [Word](plan.docx) |",
        "| Kitob xaritasi (qaysi unitlar olingan va nima uchun) | [book-map.md](book-map.md) · [PDF](book-map.pdf) |",
        "| Progress test A (1–5) va B (6–9), kalitlari bilan (30 ball) | [tests/](tests/) |",
        "",
        "## Mini-unitlar",
        "",
        "Har birida: 3 ta dars rejasi, 1 sahifalik **so'z / grammatika kartasi**, 2 ta ish varag'i, quick quiz, kalitlar, "
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
