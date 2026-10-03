"""Generators for printable games: word search, bingo, memory and flash cards."""
from __future__ import annotations

import string
from random import Random

from . import icons
from .model import Block, Box, Heading, PageBreak, Para, Spacer, Table

# right, down, down-right: easy enough for Grade 3 pupils
DIRECTIONS = [(0, 1), (1, 0), (1, 1)]


def _count(grid: list[list[str]], word: str) -> int:
    n = len(grid)
    total = 0
    for r in range(n):
        for c in range(n):
            for dr, dc in DIRECTIONS:
                er, ec = r + dr * (len(word) - 1), c + dc * (len(word) - 1)
                if er >= n or ec >= n:
                    continue
                if all(grid[r + dr * i][c + dc * i] == ch for i, ch in enumerate(word)):
                    total += 1
    return total


def make_wordsearch(words: list[str], size: int = 10, seed: int = 1
                    ) -> tuple[list[list[str]], dict[str, list[tuple[int, int]]]]:
    """Return ``(grid, placements)``; every word occurs exactly once in the grid."""
    clean = sorted({w.upper().replace(" ", "") for w in words}, key=len, reverse=True)
    if not clean or max(len(w) for w in clean) > size:
        raise ValueError(f"words do not fit a {size}x{size} grid: {clean}")
    for a in clean:
        for b in clean:
            if a != b and a in b:
                raise ValueError(f"word search: '{a.lower()}' is part of '{b.lower()}' — "
                                 "pupils could not tell which one to circle; remove one of them")
    for attempt in range(200):
        rng = Random(seed * 1000 + attempt)
        grid: list[list[str | None]] = [[None] * size for _ in range(size)]
        placed: dict[str, list[tuple[int, int]]] = {}
        ok = True
        for w in clean:
            spots = []
            for dr, dc in DIRECTIONS:
                for r in range(size):
                    for c in range(size):
                        er, ec = r + dr * (len(w) - 1), c + dc * (len(w) - 1)
                        if er >= size or ec >= size:
                            continue
                        cells = [(r + dr * i, c + dc * i) for i in range(len(w))]
                        if all(grid[a][b] in (None, w[i]) for i, (a, b) in enumerate(cells)):
                            overlap = sum(grid[a][b] is not None for a, b in cells)
                            spots.append((overlap, cells))
            if not spots:
                ok = False
                break
            rng.shuffle(spots)
            spots.sort(key=lambda s: s[0])          # prefer few overlaps, stay deterministic
            cells = spots[rng.randrange(min(3, len(spots)))][1]
            for i, (a, b) in enumerate(cells):
                grid[a][b] = w[i]
            placed[w] = cells
        if not ok:
            continue
        for r in range(size):
            for c in range(size):
                if grid[r][c] is None:
                    grid[r][c] = rng.choice(string.ascii_uppercase)
        final = [[str(ch) for ch in row] for row in grid]
        if all(_count(final, w) == 1 for w in clean):
            return final, placed
    raise RuntimeError(f"could not build an unambiguous word search for {clean}")


def wordsearch_table(grid: list[list[str]], placements: dict[str, list[tuple[int, int]]] | None = None
                     ) -> Table:
    n = len(grid)
    bg: list[list[str | None]] | None = None
    rows = [[f"**{ch}**" for ch in row] for row in grid]
    if placements:
        hit = {cell for cells in placements.values() for cell in cells}
        bg = [["FFE8B0" if (r, c) in hit else None for c in range(n)] for r in range(n)]
    return Table(rows, widths=[1] * n, style="grid", align="center", size=13, row_height=8.6,
                 width_mm=8.6 * n, bg=bg)


# ---------------------------------------------------------------- bingo --------
def bingo_cards(words: list[str], n_cards: int = 8, grid: int = 3, seed: int = 7) -> list[list[list[str]]]:
    need = grid * grid
    if len(words) < need:
        raise ValueError(f"need at least {need} words for bingo, got {len(words)}")
    rng = Random(seed)
    cards: list[list[list[str]]] = []
    seen: set[tuple[str, ...]] = set()
    guard = 0
    while len(cards) < n_cards and guard < 5000:
        guard += 1
        pick = rng.sample(words, need)
        key = tuple(sorted(pick))
        if key in seen:
            continue
        seen.add(key)
        cards.append([pick[r * grid:(r + 1) * grid] for r in range(grid)])
        if len(words) == need and len(cards) == 1:
            break
    return cards


def _cell(word: str, icon: str | None, big: float) -> str:
    pic = f"[[{icon}|{big}]]\n" if icon and icons.has(icon) else "\n"
    return f"{pic}**{word}**"


def bingo_blocks(title: str, vocab: list[tuple[str, str | None]], n_cards: int = 8, seed: int = 7
                 ) -> list[Block]:
    icon_of = dict(vocab)
    words = [w for w, _ in vocab]
    blocks: list[Block] = []
    cards = bingo_cards(words, n_cards=n_cards, seed=seed)
    for i, card in enumerate(cards):
        rows = [[_cell(w, icon_of.get(w), 40) for w in row] for row in card]
        blocks.append(Heading(f"{title} · Bingo card {i + 1}", 2))
        blocks.append(Table(rows, widths=[1, 1, 1], style="grid", align="center", size=13, row_height=36,
                            width_mm=150))
        blocks.append(Spacer(3))
        if i % 2 == 1 and i != len(cards) - 1:
            blocks.append(PageBreak())
    blocks.append(PageBreak())
    blocks.append(Heading("Teacher's caller sheet — cut up and draw from a bag", 2))
    blocks.append(Table([[_cell(w, icon_of.get(w), 26) for w in words[j:j + 4]]
                         + [""] * (4 - len(words[j:j + 4])) for j in range(0, len(words), 4)],
                        widths=[1, 1, 1, 1], style="cards", align="center", size=11, row_height=24))
    blocks.append(Para("How to play: pupils choose a card. Call a word (or say its sentence). Pupils who have it "
                       "cover it with a counter. First to cover a full line shouts **BINGO!** and reads the "
                       "words back.", "note"))
    return blocks


# -------------------------------------------------------- memory & flash -------
def memory_blocks(vocab: list[tuple[str, str | None]], per_page: int = 6) -> list[Block]:
    """Picture/word pairs for 'Pairs' — cut out, shuffle, play."""
    pics = [(w, i) for w, i in vocab if i and icons.has(i)]
    cards: list[str] = []
    for w, i in pics:
        cards.append(f"[[{i}|54]]")
        cards.append(f"**{w}**")
    blocks: list[Block] = [Para("Cut along the lines. Shuffle the cards and put them face down. Turn over two: "
                                "if picture and word match, you keep the pair!", "note")]
    cols = 4
    per = cols * 6
    for start in range(0, len(cards), per):
        chunk = cards[start:start + per]
        rows = [chunk[j:j + cols] + [""] * (cols - len(chunk[j:j + cols])) for j in range(0, len(chunk), cols)]
        blocks.append(Table(rows, widths=[1] * cols, style="cards", align="center", size=14, row_height=38))
        if start + per < len(cards):
            blocks.append(PageBreak())
    return blocks


def flashcard_blocks(vocab: list[tuple[str, str | None]]) -> list[Block]:
    """Four big cards per page (2 x 2)."""
    items = [(w, i) for w, i in vocab if i and icons.has(i)]
    blocks: list[Block] = []
    for start in range(0, len(items), 4):
        chunk = items[start:start + 4]
        cells = [f"[[{i}|96]]\n\n**{w}**" for w, i in chunk] + [""] * (4 - len(chunk))
        rows = [cells[0:2], cells[2:4]]
        blocks.append(Table(rows, widths=[1, 1], style="cards", align="center", size=26, row_height=118))
        if start + 4 < len(items):
            blocks.append(PageBreak())
    return blocks


def sentence_strips(lines: list[str]) -> list[Block]:
    """Printable strips for sentence-ordering / speaking games."""
    return [Table([[ln] for ln in lines], widths=[1], style="cards", size=14, row_height=13)]


def note(text: str) -> Box:
    return Box([Para(text, "body")], kind="tip")
