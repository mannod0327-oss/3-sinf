"""Exercise types.

Each exercise knows how to draw itself for pupils (``key=False``) and for the
teacher's key (``key=True``).  Answers in the key are wrapped in ``~~…~~`` so
they show up red and bold.  All shuffling is deterministic, so rebuilding the
repository never changes a worksheet unless its content changed.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from random import Random

from . import games
from .model import Block, Box, Doc, Group, Lines, PageBreak, Para, Spacer, Table, student

BRACE = re.compile(r"\{([^{}]*)\}")
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def blank(answer: str, minimum: int = 8, maximum: int | None = None) -> str:
    n = max(minimum, int(len(answer) * 1.35) + 2)
    return "_" * (min(n, maximum) if maximum else n)


def _shuffled(seq: list, seed: int) -> list:
    """Deterministic shuffle that never returns the original order (len > 1)."""
    if len(seq) < 2:
        return list(seq)
    rng = Random(seed)
    out = list(seq)
    for _ in range(50):
        rng.shuffle(out)
        if out != seq:
            break
    return out


@dataclass
class Exercise:
    instruction: str
    script: list[str] | None = field(default=None, kw_only=True)   # teacher reads aloud
    note: str | None = field(default=None, kw_only=True)           # teacher-only hint in the key

    @property
    def points(self) -> int:  # pragma: no cover - overridden
        raise NotImplementedError

    def body(self, key: bool) -> list[Block]:  # pragma: no cover - overridden
        raise NotImplementedError

    def blocks(self, label: str, key: bool, lead: list[Block] | None = None) -> list[Block]:
        prefix = "[[music|17]] " if self.script else ""
        head = Para(f"**{label}**  {prefix}{self.instruction}", "instruction")
        body = self.body(key)
        extra: list[Block] = []
        if key and self.script:
            extra.append(Box([Para(ln, "small") for ln in self.script], kind="script",
                             title="Teacher reads (twice, slowly):"))
        if key and self.note:
            extra.append(Para(f"Note: {self.note}", "note"))
        return [Group([*(lead or []), head, *body, *extra])]


# --------------------------------------------------------------- matching -------
@dataclass
class Match(Exercise):
    pairs: list[tuple[str, str]] = field(default_factory=list)
    seed: int = 1

    @property
    def points(self) -> int:
        return len(self.pairs)

    def body(self, key: bool) -> list[Block]:
        order = _shuffled(list(range(len(self.pairs))), self.seed)
        rows = []
        for i, (left, _) in enumerate(self.pairs):
            letter = LETTERS[order.index(i)]
            mark = f"~~{letter}~~" if key else "____"
            rows.append([f"**{i + 1}**  {left}   {mark}", f"**{LETTERS[i]}**  {self.pairs[order[i]][1]}"])
        return [Table(rows, widths=[0.52, 0.48], style="plain", row_height=11)]


@dataclass
class PicLabel(Exercise):
    items: list[tuple[str, str]] = field(default_factory=list)   # (icon, answer)
    cols: int = 4
    bank: bool = True
    seed: int = 2
    size: float = 40

    @property
    def points(self) -> int:
        return len(self.items)

    def body(self, key: bool) -> list[Block]:
        out: list[Block] = []
        if self.bank:
            words = _shuffled([a for _, a in self.items], self.seed)
            out.append(Box([Para("  ·  ".join(f"**{w}**" for w in words), "center")], kind="bank"))
        cells = []
        for i, (icon, ans) in enumerate(self.items, 1):
            line = f"~~{ans}~~" if key else blank(ans, 11, 15)
            cells.append(f"[[{icon}|{self.size}]]\n**{i}**  {line}")
        rows = [cells[j:j + self.cols] + [""] * (self.cols - len(cells[j:j + self.cols]))
                for j in range(0, len(cells), self.cols)]
        out.append(Table(rows, widths=[1] * self.cols, style="plain", align="center", row_height=27))
        return out


# ------------------------------------------------------------ choose / fill -----
@dataclass
class Circle(Exercise):
    """Items look like ``"She {*plays|play} the piano."`` (``*`` marks the answer)."""
    items: list[str] = field(default_factory=list)

    @property
    def points(self) -> int:
        return sum(len(BRACE.findall(t)) for t in self.items)

    @staticmethod
    def _sub(text: str, key: bool) -> str:
        def repl(m: re.Match[str]) -> str:
            opts = m.group(1).split("|")
            shown = []
            for o in opts:
                good = o.startswith("*")
                o = o.lstrip("*")
                shown.append(f"~~{o}~~" if (key and good) else f"**{o}**" if not key else o)
            return "(" + " / ".join(shown) + ")"
        return BRACE.sub(repl, text)

    def body(self, key: bool) -> list[Block]:
        return [Para(f"**{i}**  {self._sub(t, key)}") for i, t in enumerate(self.items, 1)]


@dataclass
class Fill(Exercise):
    """Items like ``"Lucas {gets up} at seven."``; ``bank`` shows a word box."""
    items: list[str] = field(default_factory=list)
    bank: bool = True
    extra_words: list[str] = field(default_factory=list)
    seed: int = 3

    @property
    def points(self) -> int:
        return sum(len(BRACE.findall(t)) for t in self.items)

    def body(self, key: bool) -> list[Block]:
        out: list[Block] = []
        if self.bank:
            words = []
            for t in self.items:
                words += BRACE.findall(t)
            words = list(dict.fromkeys(words + self.extra_words))
            out.append(Box([Para("  ·  ".join(f"**{w}**" for w in _shuffled(words, self.seed)), "center")],
                           kind="bank"))
        for i, t in enumerate(self.items, 1):
            text = BRACE.sub(lambda m: f"~~{m.group(1)}~~" if key else blank(m.group(1)), t)
            out.append(Para(f"**{i}**  {text}"))
        return out


@dataclass
class Unscramble(Exercise):
    items: list[str] = field(default_factory=list)   # correct sentences
    seed: int = 4

    @property
    def points(self) -> int:
        return len(self.items)

    def body(self, key: bool) -> list[Block]:
        out: list[Block] = []
        for i, sentence in enumerate(self.items, 1):
            words = sentence.split()
            shuffled = _shuffled(words, self.seed + i)
            out.append(Para(f"**{i}**  " + "  /  ".join(shuffled)))
            out.append(Para(f"~~{sentence}~~") if key else Lines(1, 8))
        return out


@dataclass
class Gaps(Exercise):
    """Look at the picture, complete the word (vowels are missing) — spelling practice."""
    items: list[tuple[str, str]] = field(default_factory=list)   # (icon, word)
    cols: int = 3
    size: float = 34

    @property
    def points(self) -> int:
        return len(self.items)

    @staticmethod
    def hide(word: str) -> str:
        out = []
        for i, ch in enumerate(word):
            out.append("_" if ch.lower() in "aeiou" and i > 0 else ch)
        return "".join(out)

    def body(self, key: bool) -> list[Block]:
        cells = []
        for i, (icon, word) in enumerate(self.items, 1):
            line = f"~~{word}~~" if key else blank(word, 8)
            cells.append(f"[[{icon}|{self.size}]]\n**{i}**  {self.hide(word)}\n{line}")
        rows = [cells[j:j + self.cols] + [""] * (self.cols - len(cells[j:j + self.cols]))
                for j in range(0, len(cells), self.cols)]
        return [Table(rows, widths=[1] * self.cols, style="plain", align="center", row_height=31)]


@dataclass
class NumberPics(Exercise):
    """Listening: pupils write 1, 2, 3… in the box under each picture in the order they hear them.

    ``heard[k]`` is the index (into ``icons``) of the picture mentioned k-th."""
    icons: list[str] = field(default_factory=list)
    heard: list[int] = field(default_factory=list)
    cols: int = 5
    size: float = 38

    @property
    def points(self) -> int:
        return len(self.icons)

    def body(self, key: bool) -> list[Block]:
        number = {idx: k + 1 for k, idx in enumerate(self.heard)}
        cells = []
        for i, icon in enumerate(self.icons):
            mark = f"~~{number[i]}~~" if key else "  "
            cells.append(f"[[{icon}|{self.size}]]\n[ {mark} ]")
        rows = [cells[j:j + self.cols] + [""] * (self.cols - len(cells[j:j + self.cols]))
                for j in range(0, len(cells), self.cols)]
        return [Table(rows, widths=[1] * self.cols, style="plain", align="center", row_height=27)]


@dataclass
class TrueFalse(Exercise):
    items: list[tuple[str, bool]] = field(default_factory=list)
    labels: tuple[str, str] = ("T", "F")

    @property
    def points(self) -> int:
        return len(self.items)

    def body(self, key: bool) -> list[Block]:
        t, f = self.labels
        rows = []
        for i, (stmt, val) in enumerate(self.items, 1):
            if key:
                choice = f"~~{t}~~   {f}" if val else f"{t}   ~~{f}~~"
            else:
                choice = f"( {t} )   ( {f} )"
            rows.append([f"**{i}**  {stmt}", choice])
        return [Table(rows, widths=[0.78, 0.22], style="plain", row_height=10)]


@dataclass
class Order(Exercise):
    items: list[str] = field(default_factory=list)   # in the correct order
    seed: int = 5

    @property
    def points(self) -> int:
        return len(self.items)

    def body(self, key: bool) -> list[Block]:
        order = _shuffled(list(range(len(self.items))), self.seed)
        rows = []
        for pos, idx in enumerate(order):
            number = f"~~{idx + 1}~~" if key else "[  ]"
            rows.append([number, self.items[idx]])
        return [Table(rows, widths=[0.1, 0.9], style="plain", row_height=10)]


@dataclass
class OddOne(Exercise):
    rows: list[tuple[list[str], str]] = field(default_factory=list)

    @property
    def points(self) -> int:
        return len(self.rows)

    def body(self, key: bool) -> list[Block]:
        out = []
        for i, (words, odd) in enumerate(self.rows, 1):
            cells = [f"**{i}**"] + [f"~~{w}~~" if key and w == odd else w for w in words]
            out.append(cells)
        n = len(self.rows[0][0]) + 1
        return [Table(out, widths=[0.1] + [0.9 / (n - 1)] * (n - 1), style="plain", align="center", row_height=10)]


# ------------------------------------------------------------- read / write -----
@dataclass
class Reading(Exercise):
    title: str = ""
    text: str = ""
    questions: list[tuple[str, str]] = field(default_factory=list)
    lines_per_answer: int = 1

    @property
    def points(self) -> int:
        return len(self.questions)

    def body(self, key: bool) -> list[Block]:
        paras = [Para(p.strip()) for p in self.text.strip().split("\n\n")]
        out: list[Block] = [Box(paras, kind="note", title=self.title or None)]
        for i, (q, a) in enumerate(self.questions, 1):
            out.append(Para(f"**{i}**  {q}"))
            out.append(Para(f"~~{a}~~") if key else Lines(self.lines_per_answer, 8))
        return out


@dataclass
class WriteAbout(Exercise):
    frames: list[str] = field(default_factory=list)
    lines: int = 3
    model: list[str] = field(default_factory=list)
    marks: int = 3    # content 1 · grammar 1 · spelling 1 (teacher scored)

    @property
    def points(self) -> int:
        return self.marks

    def body(self, key: bool) -> list[Block]:
        out: list[Block] = []
        if self.frames:
            out.append(Box([Para(f) for f in self.frames], kind="bank", title="Help box"))
        if key:
            out.append(Box([Para(m) for m in self.model], kind="answer",
                           title=f"Sample answer ({self.marks} marks: content, grammar, spelling)"))
        else:
            out.append(Lines(self.lines, 9))
        return out


@dataclass
class Draw(Exercise):
    prompts: list[str] = field(default_factory=list)

    @property
    def points(self) -> int:
        return 0

    def body(self, key: bool) -> list[Block]:
        if key:
            return [Para(f"{student(plural=True, cap=True)}' own drawings — praise effort and check the labels.", "note")]
        return [Box([Para(p, "center")], kind="draw") for p in self.prompts]


@dataclass
class WordSearch(Exercise):
    words: list[str] = field(default_factory=list)
    size: int = 10
    seed: int = 1
    icon_of: dict[str, str] = field(default_factory=dict)

    @property
    def points(self) -> int:
        return 0

    def body(self, key: bool) -> list[Block]:
        grid, placed = games.make_wordsearch(self.words, self.size, self.seed)
        table = games.wordsearch_table(grid, placed if key else None)
        chips = "   ".join((f"[[{self.icon_of[w]}|16]] " if w in self.icon_of else "") + f"**{w.upper()}**"
                           for w in self.words)
        return [Box([Para(chips, "center")], kind="bank", title="Find these words (→ ↓ ↘)"), table]


@dataclass
class FreeText(Exercise):
    """Anything that is not an exercise in the strict sense (speaking tasks, games)."""
    blocks_: list[Block] = field(default_factory=list)

    @property
    def points(self) -> int:
        return 0

    def body(self, key: bool) -> list[Block]:
        return list(self.blocks_)


# ---------------------------------------------------------------- documents -----
@dataclass
class Section:
    title: str
    exercises: list[Exercise]
    intro: str | None = None


def total_points(items: list) -> int:
    total = 0
    for it in items:
        if isinstance(it, Section):
            total += sum(e.points for e in it.exercises)
        elif isinstance(it, Exercise):
            total += it.points
    return total


def sheet(title: str, items: list, *, subtitle: str = "", badge: str = "", key: bool = False,
          name_line: bool = True, footer: str = "", kind: str = "worksheet", score: bool = True) -> Doc:
    """Assemble a printable document from exercises, sections and raw blocks."""
    blocks: list[Block] = []
    n = 0
    for it in items:
        if isinstance(it, Section):
            pts = sum(e.points for e in it.exercises)
            lead: list[Block] = [Para(f"**{it.title}**" + (f"   ({pts} points)" if pts else ""), "instruction")]
            if it.intro:
                lead.append(Para(it.intro, "note"))
            for k, e in enumerate(it.exercises):
                blocks.extend(e.blocks(LETTERS[n], key, lead if k == 0 else None))
                n += 1
        elif isinstance(it, Exercise):
            blocks.extend(it.blocks(LETTERS[n], key))
            n += 1
        else:
            blocks.append(it)
    total = total_points(items)
    if score and total:
        blocks.append(Spacer(2))
        blocks.append(Para(f"Total: {total} points" if key else f"Score: ________ / {total}", "right"))
    return Doc(title=title, blocks=blocks, subtitle=subtitle, badge=badge, kind=kind,
               name_line=name_line and not key, footer=footer, key=key)
