"""Every relative link in every Markdown file must point at a file that exists."""
from __future__ import annotations

import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
MD_FILES = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts and ".venv" not in p.parts)


@pytest.mark.parametrize("md", MD_FILES, ids=[str(p.relative_to(ROOT)) for p in MD_FILES])
def test_relative_links_resolve(md: Path):
    broken = []
    for target in LINK.findall(md.read_text(encoding="utf-8")):
        if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith("#"):
            continue   # http(s), mailto, in-page anchors
        path = (md.parent / target.split("#")[0]).resolve()
        if not path.exists():
            broken.append(target)
    assert not broken, f"{md.relative_to(ROOT)}: broken links {broken}"


def test_docs_exist():
    for name in ("README.md", "NOTICE.md", "docs/teacher-handbook.md", "docs/curriculum-bridge.md",
                 "docs/drive-inventory.md", "docs/sources.md"):
        assert (ROOT / name).exists(), name
