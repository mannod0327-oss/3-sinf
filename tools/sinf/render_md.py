"""Markdown renderer — GitHub-friendly pages (icons become native emoji)."""
from __future__ import annotations

from pathlib import Path

from . import icons
from .markup import tokenize
from .model import (
    Block, Box, Bullets, Doc, Group, Heading, Lines, PageBreak, Para, Rule, Spacer, Table,
)


def md_text(text: str, cell: bool = False) -> str:
    out: list[str] = []
    for tok in tokenize(text):
        if tok.kind == "text":
            out.append(tok.value.replace("|", "\\|") if cell else tok.value)
        elif tok.kind in ("bold", "ans"):
            out.append(f"**{tok.value}**")
        elif tok.kind == "br":
            out.append("<br>" if cell else "  \n")
        elif tok.kind == "icon":
            out.append(icons.char(tok.value))
    return "".join(out)


def _blocks(blocks: list[Block]) -> list[str]:
    lines: list[str] = []
    for b in blocks:
        chunk = _block(b)
        if chunk:
            lines.extend(chunk)
            lines.append("")
    return lines


def _block(b: Block) -> list[str]:
    if isinstance(b, Heading):
        return [f"{'#' * min(b.level + 1, 6)} {md_text(b.text)}"]
    if isinstance(b, Para):
        text = md_text(b.text)
        if b.style == "instruction":
            text = f"**{text}**" if not text.startswith("**") else text
        elif b.style == "note":
            text = f"_{text}_"
        elif b.style == "small":
            text = f"<sub>{text}</sub>"
        return [text]
    if isinstance(b, Bullets):
        return [(f"{i}. " if b.ordered else "- ") + md_text(it) for i, it in enumerate(b.items, 1)]
    if isinstance(b, Spacer):
        return []
    if isinstance(b, (PageBreak, Rule)):
        return ["---"]
    if isinstance(b, Lines):
        return ["_" * 48] * b.n
    if isinstance(b, Group):
        return _blocks(b.blocks)
    if isinstance(b, Box):
        inner = _blocks(b.blocks)
        head = [f"**{md_text(b.title)}**", ""] if b.title else []
        return [f"> {ln}" if ln else ">" for ln in head + inner]
    if isinstance(b, Table):
        ncols = max(len(r) for r in b.rows)
        rows = [[md_text(c, cell=True) for c in r] + [""] * (ncols - len(r)) for r in b.rows]
        head = rows[0] if b.header else [""] * ncols
        body = rows[1:] if b.header else rows
        out = ["| " + " | ".join(head) + " |", "|" + "|".join(["---"] * ncols) + "|"]
        out += ["| " + " | ".join(r) + " |" for r in body]
        return out
    raise TypeError(f"unknown block {type(b)!r}")


def render_md(doc: Doc, path: str | Path, front: str = "") -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    head = [f"# {md_text(doc.title)}", ""]
    if doc.subtitle or doc.badge:
        head += [f"*{' · '.join(x for x in (doc.subtitle, doc.badge) if x)}*", ""]
    if front:
        head += [front, ""]
    body = _blocks(doc.blocks)
    path.write_text("\n".join(head + body).rstrip() + "\n", encoding="utf-8")
    return path
