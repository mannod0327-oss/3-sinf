"""Progress tests (30 points) for the grammar packs, with marking keys."""
from __future__ import annotations

from pathlib import Path

from .exercises import Section, sheet, total_points
from .model import Bullets, Heading, Para, Spacer, Table
from .render_docx import render_docx
from .render_pdf import render_pdf

GRADE_30 = [
    ["Mark", "Level", "Points (of 30)", "Percent"],
    ["5", "a'lo (excellent)", "26 – 30", "86 – 100 %"],
    ["4", "yaxshi (good)", "22 – 25", "71 – 85 %"],
    ["3", "qoniqarli (satisfactory)", "17 – 21", "55 – 70 %"],
    ["2", "qoniqarsiz (unsatisfactory)", "0 – 16", "below 55 %"],
]
WRITING_4 = [
    ["Criterion", "2 points", "1 point", "0 points"],
    ["Content", "all 4 sentences answer the task", "2–3 sentences on task", "off-topic or one sentence"],
    ["Language", "target grammar mostly correct, spelling clear", "some correct, several errors",
     "hard to understand"],
]


def build_progress_tests(out: Path, badge: str, tests: list[dict]) -> list[Path]:
    """``tests``: dicts with ``slug``, ``title``, ``scope`` and ``sections``; each must total 30 points."""
    made: list[Path] = []
    for t in tests:
        total = total_points(t["sections"])
        assert total == 30, f"{t['slug']} has {total} points, expected 30"
        sub = f"{t['scope']} · 30 points · 30 minutes"
        student = sheet(t["title"], t["sections"], subtitle=sub, badge=badge, kind="test")
        made += [render_pdf(student, out / f"{t['slug']}.pdf"), render_docx(student, out / f"{t['slug']}.docx")]
        key = sheet(t["title"], t["sections"], subtitle=sub, badge=badge, key=True, kind="test")
        part_rows = [["Part", "Points"]] + [[s.title, str(sum(e.points for e in s.exercises))]
                                            for s in t["sections"]] + [["**Total**", "**30**"]]
        key.blocks = [
            Heading("How to use this key", 2),
            Bullets(["Time: 30 minutes. Pupils need a pencil.",
                     "1 point per correct item. Accept small spelling slips only if the word is recognisable and "
                     "the grammar is right.",
                     "Writing (4 points): use the rubric below."]),
            Table(part_rows, widths=[0.7, 0.3], header=True, style="grid", size=10),
            Spacer(2), Heading("Marks", 3),
            Table(GRADE_30, widths=[0.12, 0.4, 0.25, 0.23], header=True, style="grid", size=10),
            Para("Thresholds follow the usual 86 / 71 / 55 percent bands; adjust them if your school uses a "
                 "different scale.", "note"),
            Heading("Writing rubric", 3),
            Table(WRITING_4, widths=[0.22, 0.28, 0.27, 0.23], header=True, style="grid", size=9.5),
            Spacer(3),
        ] + key.blocks
        made.append(render_pdf(key, out / f"{t['slug']}-KEY.pdf"))
    return made
