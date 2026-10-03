"""Word is strict about the order of child elements; make sure every generated DOCX respects it."""
from __future__ import annotations

import sys
import zipfile
from pathlib import Path

import pytest
from lxml import etree

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
from sinf.render_docx import PPR_ORDER, TCPR_ORDER  # noqa: E402

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def docx_files() -> list[Path]:
    return sorted(ROOT.rglob("*.docx"))


def check_order(tree, tag: str, order: list[str], name: str) -> None:
    for el in tree.iter(W + tag):
        ranks = [order.index(c.tag.replace(W, "")) for c in el if c.tag.replace(W, "") in order]
        assert ranks == sorted(ranks), f"{name}: <w:{tag}> children out of schema order: " \
                                       f"{[c.tag.replace(W, '') for c in el]}"
        names = [c.tag for c in el]
        assert len(names) == len(set(names)), f"{name}: duplicate child in <w:{tag}>"


@pytest.mark.parametrize("path", docx_files() or [pytest.param(None, marks=pytest.mark.skip("no docx built"))])
def test_docx_child_order(path: Path) -> None:
    with zipfile.ZipFile(path) as z:
        tree = etree.fromstring(z.read("word/document.xml"))
    check_order(tree, "tcPr", TCPR_ORDER, path.name)
    check_order(tree, "pPr", PPR_ORDER, path.name)
