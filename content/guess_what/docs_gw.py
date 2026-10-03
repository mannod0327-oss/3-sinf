"""Pack-level documents for Guess What!: annual plan, course map, glossary and the pack README."""
from __future__ import annotations

import math
from pathlib import Path

from sinf import icons
from sinf.model import Doc, Heading, Para, Table
from sinf.render_docx import render_docx
from sinf.render_md import render_md
from sinf.render_pdf import render_pdf

from .common import BADGE
from .pack import UNITS

QUARTER_AFTER = {2: 1, 4: 2, 6: 3, 8: 4}   # quarter test comes after these units


def plan_rows() -> list[dict]:
    """Flatten the course into the 68 numbered lessons of the year."""
    rows: list[dict] = []
    n = 0
    for unit in UNITS:
        for lesson in unit.lessons:
            n += 1
            rows.append(dict(n=n, week=math.ceil(n / 2), unit=unit.label, title=lesson.title, focus=lesson.focus,
                             folder=unit.slug))
        q = QUARTER_AFTER.get(unit.number)
        if q:
            n += 1
            name = f"Quarter {q} test" if q < 4 else "Final test (Quarter 4)"
            rows.append(dict(n=n, week=math.ceil(n / 2), unit="Tests", title=name,
                             focus="Written test (40 points) + speaking check", folder="tests"))
    return rows


def annual_plan(out: Path) -> list[Path]:
    rows = plan_rows()
    assert len(rows) == 68, f"expected 68 lessons, got {len(rows)}"
    table = [["#", "Week", "Unit", "Lesson", "Focus"]]
    bg: list[list[str | None]] = [[None] * 5]
    for r in rows:
        table.append([str(r["n"]), str(r["week"]), r["unit"], f"**{r['title']}**", r["focus"]])
        bg.append(["FFF6E0"] * 5 if r["unit"] == "Tests" else [None] * 5)
    blocks = [
        Para("A suggested plan for **68 lessons** (2 lessons a week × 34 weeks). The shaded rows are tests. "
             "Move lessons around to fit your school timetable, holidays and quarter dates.", "note"),
        Table(table, widths=[0.05, 0.085, 0.2, 0.25, 0.415], header=True, style="stage", size=9, bg=bg),
        Heading("Quarter overview", 2),
        Table([["Quarter", "Lessons", "Content", "Test"],
               ["1", "1 – 20", "Welcome, Unit 1, Unit 2", "Quarter 1 test"],
               ["2", "21 – 36", "Unit 3, Unit 4", "Quarter 2 test"],
               ["3", "37 – 52", "Unit 5, Unit 6", "Quarter 3 test"],
               ["4", "53 – 68", "Unit 7, Unit 8 + revision", "Final test"]],
              widths=[0.12, 0.15, 0.45, 0.28], header=True, style="grid", size=10),
    ]
    doc = Doc(title="Annual plan", blocks=blocks, badge=BADGE, subtitle="Guess What! Grade 3 · 68 lessons · 34 weeks",
              kind="lesson")
    return [render_md(doc, out / "annual-plan.md"), render_docx(doc, out / "annual-plan.docx"),
            render_pdf(doc, out / "annual-plan.pdf")]


def course_map(out: Path) -> list[Path]:
    rows = [["Unit", "Vocabulary", "Grammar", "Skills / Say it!", "Story value · Talk time", "CLIL"]]
    for u in UNITS:
        i = u.info
        rows.append([f"**{u.number if u.number else 'W'}  {u.title}**", i.vocabulary, "\n".join(i.grammar),
                     f"{i.skills}\nSay it!: {i.phonics}", f"{i.story_value}\n{i.talk_time}", i.clil])
    doc = Doc(title="Course map", badge=BADGE, subtitle="Welcome + 8 units", kind="reference",
              blocks=[Para("Built from the publisher's table of contents of Cambridge *Guess What!* Level 3 (Reed, "
                           "Koustaff, Bentley). Use it to see at a glance what each unit teaches.", "note"),
                      Table(rows, widths=[0.12, 0.22, 0.24, 0.16, 0.14, 0.12], header=True, style="stage", size=8)])
    return [render_md(doc, out / "course-map.md"), render_pdf(doc, out / "course-map.pdf")]


def glossary(out: Path) -> list[Path]:
    entries: dict[str, tuple[str, str, str | None]] = {}
    for u in UNITS:
        for v in u.vocab + u.extra_vocab:
            key = v.en.lower()
            entries.setdefault(key, (v.en, v.uz, u.label if u.number else "Welcome"))
    ordered = sorted(entries.values(), key=lambda e: e[0].lower())
    unit_of = {}
    for u in UNITS:
        for v in u.vocab + u.extra_vocab:
            unit_of.setdefault(v.en.lower(), v)
    rows = [["", "English", "O'zbekcha", "Unit"]]
    for en, uz, unit in ordered:
        v = unit_of[en.lower()]
        pic = f"[[{v.icon}|16]]" if v.icon and icons.has(v.icon) else ""
        rows.append([pic, f"**{en}**", uz, unit.replace("Unit ", "U").split(" · ")[0]])
    doc = Doc(title="English–Uzbek glossary", badge=BADGE,
              subtitle=f"Guess What! Grade 3 · {len(ordered)} words and phrases, A–Z", kind="reference",
              blocks=[Table(rows, widths=[0.07, 0.38, 0.43, 0.12], header=True, style="grid", size=10)])
    return [render_md(doc, out / "glossary.md"), render_pdf(doc, out / "glossary.pdf"),
            render_docx(doc, out / "glossary.docx")]


def pack_readme(out: Path) -> Path:
    lines = [
        "# Guess What! — 3-sinf (Grade 3) materiallari",
        "",
        "Cambridge **Guess What! Level 3** (Reed, Koustaff, Bentley) darsligi uchun **original** o'qituvchi "
        "materiallari: dars rejalari, ish varaqlari, kalitlar, o'yinlar va chorak nazorat ishlari. "
        "Darslik matnlari, rasmlari va audiolari bu yerda **yo'q** — ular sizdagi nashrdan olinadi.",
        "",
        "## Nimalar bor",
        "",
        "| Nima | Fayl |",
        "|---|---|",
        "| Yillik reja (68 dars) | [annual-plan.md](annual-plan.md) · [Word](annual-plan.docx) · [PDF](annual-plan.pdf) |",
        "| Kurs xaritasi (lug'at, grammatika, fonetika, CLIL) | [course-map.md](course-map.md) · "
        "[PDF](course-map.pdf) |",
        "| Inglizcha–o'zbekcha lug'at (A–Z) | [glossary.md](glossary.md) · [PDF](glossary.pdf) · "
        "[Word](glossary.docx) |",
        "| Chorak nazorat ishlari (4 ta, kalit va tinglash matni bilan) | [tests/](tests/README.md) |",
        "| Og'zaki nazorat (rubrika + savol kartalari) | [tests/speaking-check.pdf](tests/speaking-check.pdf) |",
        "",
        "## Unitlar",
        "",
        "Har bir unit papkasida: dars rejalari (Markdown + Word), 2 ta ish varag'i, quick quiz, barcha kalitlar, "
        "flashcards, bingo va juftlik (memory) o'yini.",
        "",
        "| Unit | Mavzu | Darslar | Ochish |",
        "|---|---|---|---|",
    ]
    for u in UNITS:
        label = "Welcome" if u.number == 0 else f"Unit {u.number}"
        lines.append(f"| {label} | {u.title} — {u.info.topic} | {len(u.lessons)} | [{u.slug}/]({u.slug}/README.md) |")
    lines += [
        "",
        "## Qanday foydalanish",
        "",
        "1. **Yillik reja**dan dars raqamini toping → unit papkasidagi `lesson-plans.md` ni oching.",
        "2. Ish varag'ini **PDF** ko'rinishida chop eting (Word nusxasi — tahrir qilish uchun). Kalit "
        "(`answer-keys.pdf`) faqat o'qituvchi uchun.",
        "3. Tinglash mashqlarida matnni o'zingiz ikki marta sekin o'qing (testlar kaliti ichida berilgan).",
        "4. Darslikdagi audio, video va flashcards sizning Google Drive'dagi materiallardan olinadi "
        "(ular bu repozitoriyga qo'yilmagan).",
        "",
        "## Eslatmalar",
        "",
        "- Dars rejalaridagi **Student's Book / Activity Book** sahifalari Cambridge nashri mazmuniga mos; "
        "sahifa raqamlari nashrlarda farq qilgani uchun ko'rsatilmagan.",
        "- Yillik reja 68 soatga (haftasiga 2 soat) mo'ljallangan; maktabingiz jadvaliga moslab o'zgartiring.",
        "- Rasmlar — Twemoji (CC-BY 4.0), shrift — Andika (SIL OFL). Batafsil: [../NOTICE.md](../NOTICE.md).",
        "",
    ]
    path = out / "README.md"
    path.write_text("\n".join(lines), encoding="utf-8")
    return path


def tests_readme(out: Path) -> Path:
    lines = [
        "# Chorak nazorat ishlari (Guess What! 3-sinf)",
        "",
        "Har bir test — **40 ball**, **40 daqiqa**: Listening (10) · Vocabulary (8) · Grammar (10) · Reading (6) · "
        "Writing (6).",
        "",
        "| Test | Mavzular | O'quvchi varaqi | O'qituvchi kaliti |",
        "|---|---|---|---|",
        "| 1-chorak | Welcome, Unit 1, Unit 2 | [PDF](quarter-1-test.pdf) · [Word](quarter-1-test.docx) | "
        "[KEY](quarter-1-test-KEY.pdf) |",
        "| 2-chorak | Unit 3, Unit 4 | [PDF](quarter-2-test.pdf) · [Word](quarter-2-test.docx) | "
        "[KEY](quarter-2-test-KEY.pdf) |",
        "| 3-chorak | Unit 5, Unit 6 | [PDF](quarter-3-test.pdf) · [Word](quarter-3-test.docx) | "
        "[KEY](quarter-3-test-KEY.pdf) |",
        "| 4-chorak (yakuniy) | Unit 7, Unit 8 + butun yil | [PDF](quarter-4-final-test.pdf) · "
        "[Word](quarter-4-final-test.docx) | [KEY](quarter-4-final-test-KEY.pdf) |",
        "| Og'zaki nazorat | 1–4-chorak | [PDF](speaking-check.pdf) · [Word](speaking-check.docx) | — |",
        "",
        "## Baholash (odatdagi 86 / 71 / 55 foiz chegaralari)",
        "",
        "| Baho | Ball (40 dan) |",
        "|---|---|",
        "| 5 | 35 – 40 |",
        "| 4 | 29 – 34 |",
        "| 3 | 22 – 28 |",
        "| 2 | 0 – 21 |",
        "",
        "Maktabingiz ichki qoidasi boshqacha bo'lsa, chegaralarni o'zgartiring.",
        "",
        "## Tinglash (Listening) qanday o'tkaziladi",
        "",
        "Audio yo'q — matnni o'zingiz o'qiysiz. Kalit PDF ichida har bir mashq ostida qizil katakda "
        "**Teacher reads** matni bor. Har bir matnni **ikki marta**, sekin va aniq o'qing; qatorlar orasida qisqa pauza "
        "qiling. O'quvchilarga javobni aytib yubormang.",
        "",
    ]
    path = out / "README.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")
    return path
