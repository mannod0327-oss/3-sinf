"""Lesson-plan model: 45-minute lessons lowered to document blocks."""
from __future__ import annotations

from dataclasses import dataclass, field

from .model import Block, Box, Bullets, Doc, Heading, Para, Spacer, Table

INTERACTION = {
    "T-Ss": "teacher – whole class", "Ss-Ss": "pairs / groups", "S": "individual",
    "G": "groups", "T-S": "teacher – pupil",
}

STD_TIMES = (3, 5, 10, 12, 10, 5)
STD_NAMES = ("Greeting & organisation", "Warm-up", "Presentation", "Controlled practice",
             "Freer practice / production", "Wrap-up & homework")


@dataclass
class Stage:
    minutes: int
    name: str
    activity: str
    interaction: str = "T-Ss"


@dataclass
class Lesson:
    title: str
    focus: str
    aims: list[str]
    language: list[str]
    materials: list[str]
    stages: list[Stage]
    homework: str
    assessment: str
    tips: list[str] = field(default_factory=list)   # teacher tips, L1 (Uzbek) notes, differentiation

    @classmethod
    def std(cls, title: str, focus: str, aims: list[str], language: list[str], materials: list[str],
            greeting: str, warmup: str, present: str, practice: str, produce: str, wrap: str,
            homework: str, assessment: str, tips: list[str] | None = None,
            interactions: tuple[str, ...] = ("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "Ss-Ss / G", "T-Ss")
            ) -> "Lesson":
        acts = (greeting, warmup, present, practice, produce, wrap)
        stages = [Stage(m, n, a, i) for m, n, a, i in zip(STD_TIMES, STD_NAMES, acts, interactions)]
        return cls(title, focus, aims, language, materials, stages, homework, assessment, tips or [])

    @property
    def minutes(self) -> int:
        return sum(s.minutes for s in self.stages)

    def blocks(self, number: int) -> list[Block]:
        facts = [
            ["**Focus**", self.focus],
            ["**Aims**  (by the end of the lesson pupils can…)", "\n".join(f"• {a}" for a in self.aims)],
            ["**Key language**", "\n".join(f"• {a}" for a in self.language)],
            ["**Materials**", "\n".join(f"• {a}" for a in self.materials)],
            ["**Time**", f"{self.minutes} minutes"],
        ]
        stage_rows = [["Min", "Stage", "What happens", "Interaction"]]
        for s in self.stages:
            stage_rows.append([str(s.minutes), f"**{s.name}**", s.activity, s.interaction])
        out: list[Block] = [
            Heading(f"Lesson {number}: {self.title}", 2),
            Table(facts, widths=[0.22, 0.78], style="grid", size=10),
            Spacer(2),
            Table(stage_rows, widths=[0.06, 0.17, 0.65, 0.12], header=True, style="stage", size=9.5),
            Para(f"**Homework:** {self.homework}"),
            Para(f"**Check learning:** {self.assessment}"),
        ]
        if self.tips:
            out.append(Box([Bullets(self.tips)], kind="tip", title="Teacher tips (o'qituvchi uchun)"))
        return out


@dataclass
class UnitInfo:
    """'Unit at a glance' facts shown at the top of every plan."""
    number: int
    title: str
    topic: str
    vocabulary: str
    grammar: list[str]
    skills: str = ""
    phonics: str = ""
    story_value: str = ""
    talk_time: str = ""
    clil: str = ""
    review: str = ""
    book: str = ""          # where the topic sits in the coursebook (used by Round-Up / Destination packs)

    def blocks(self) -> list[Block]:
        rows = [
            ["**In the book**", self.book],
            ["**Topic**", self.topic],
            ["**Vocabulary**", self.vocabulary],
            ["**Grammar**", "\n".join(f"• {g}" for g in self.grammar)],
            ["**Skills**", self.skills],
            ["**Say it! (phonics)**", self.phonics],
            ["**Story value**", self.story_value],
            ["**Talk time**", self.talk_time],
            ["**CLIL**", self.clil],
            ["**Review**", self.review],
        ]
        rows = [r for r in rows if r[1].strip()]
        return [Heading("Unit at a glance", 2), Table(rows, widths=[0.22, 0.78], style="grid", size=10)]


def plan_doc(title: str, subtitle: str, badge: str, intro: list[Block], lessons: list[Lesson]) -> Doc:
    blocks: list[Block] = list(intro)
    for i, lesson in enumerate(lessons, 1):
        blocks.extend(lesson.blocks(i))
    return Doc(title=title, blocks=blocks, subtitle=subtitle, badge=badge, kind="lesson")
