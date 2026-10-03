#!/usr/bin/env python3
"""Render the Twemoji icons used by ``sinf.icons`` to PNG.

The PNGs are committed to the repository, so this script only needs to be run
when new icons are added to ``sinf/icons.py``.

Usage::

    npm i @twemoji/svg@15.0.0          # anywhere
    python tools/build_assets.py /path/to/node_modules/@twemoji/svg
"""
from __future__ import annotations

import sys
from pathlib import Path

import cairosvg

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sinf import icons  # noqa: E402


def candidates(stem: str) -> list[str]:
    parts = stem.split("-")
    with_fe0f = "-".join([parts[0], "fe0f", *parts[1:]])
    return [stem, with_fe0f]


def main(svg_dir: str) -> int:
    src = Path(svg_dir)
    icons.ASSET_DIR.mkdir(parents=True, exist_ok=True)
    missing: list[str] = []
    done: set[str] = set()
    for name, stem in sorted(icons.EMOJI.items()):
        if stem in done:
            continue
        svg = next((src / f"{c}.svg" for c in candidates(stem) if (src / f"{c}.svg").exists()), None)
        if svg is None:
            missing.append(f"{name} ({stem})")
            continue
        cairosvg.svg2png(url=str(svg), write_to=str(icons.ASSET_DIR / f"{stem}.png"),
                         output_width=256, output_height=256)
        done.add(stem)
    print(f"rendered {len(done)} icons into {icons.ASSET_DIR}")
    if missing:
        print("MISSING in Twemoji set:", ", ".join(missing))
        return 1
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1]))
