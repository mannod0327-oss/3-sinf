#!/usr/bin/env python3
"""Build every printable and Markdown file of the repository from ``content/``.

Usage::

    python tools/build.py                # everything
    python tools/build.py guess-what     # one pack
    python tools/build.py guess-what 1   # one unit of one pack
"""
from __future__ import annotations

import importlib
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "content"))

from sinf import model  # noqa: E402
from sinf.unit import build_unit  # noqa: E402

PACKS = {
    "guess-what": ("guess_what", "guess_what.pack"),
    "round-up-3": ("round_up_3", "round_up_3.pack"),
    "destination-a1": ("destination_a1", "destination_a1.pack"),
}


def load(pack: str):
    pkg, mod = PACKS[pack]
    try:
        return importlib.import_module(mod)
    except ModuleNotFoundError as exc:
        if exc.name and exc.name.startswith(pkg):
            return None
        raise


def main(argv: list[str]) -> int:
    wanted = [argv[0]] if argv else list(PACKS)
    only_unit = int(argv[1]) if len(argv) > 1 else None
    started = time.time()
    count = 0
    for name in wanted:
        module = load(name)
        if module is None:
            print(f"[skip] {name}: no content yet")
            continue
        model.WORDS.clear()
        model.WORDS.update(getattr(module, "WORDS", {"student": "pupil"}))   # British / American wording
        pack_root = ROOT / name
        for spec in module.UNITS:
            if only_unit is not None and spec.number != only_unit:
                continue
            made = build_unit(spec, pack_root)
            count += sum(len(v) for v in made.values())
            print(f"[ok] {name}/{spec.slug}: {sum(len(v) for v in made.values())} files")
        if hasattr(module, "build_extras") and only_unit is None:
            count += len(module.build_extras(pack_root))
            print(f"[ok] {name}: extras built")
    print(f"done: {count} files in {time.time() - started:.1f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
