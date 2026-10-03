"""Tiny inline-markup tokenizer shared by the three renderers."""
from __future__ import annotations

import re
from typing import NamedTuple

_TOKEN = re.compile(r"(\*\*.+?\*\*|~~.+?~~|\[\[[^\]]+\]\]|\n)", re.S)


class Tok(NamedTuple):
    kind: str            # text | bold | ans | icon | br
    value: str
    size: float | None = None


def tokenize(text: str) -> list[Tok]:
    out: list[Tok] = []
    for part in _TOKEN.split(text):
        if not part:
            continue
        if part == "\n":
            out.append(Tok("br", ""))
        elif part.startswith("**") and part.endswith("**") and len(part) > 4:
            out.append(Tok("bold", part[2:-2]))
        elif part.startswith("~~") and part.endswith("~~") and len(part) > 4:
            out.append(Tok("ans", part[2:-2]))
        elif part.startswith("[[") and part.endswith("]]"):
            body = part[2:-2]
            name, _, size = body.partition("|")
            out.append(Tok("icon", name.strip(), float(size) if size else None))
        else:
            out.append(Tok("text", part))
    return out


def strip(text: str) -> str:
    """Plain text without markup (icons become nothing)."""
    return "".join(t.value for t in tokenize(text) if t.kind in ("text", "bold", "ans")).replace("\n", " ")
