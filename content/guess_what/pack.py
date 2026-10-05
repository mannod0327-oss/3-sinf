"""Pack registry: unit modules in course order, plus the pack-level documents."""
from pathlib import Path

from . import (
    unit0_welcome, unit1_garden, unit2_school, unit3_days, unit4_my_day, unit5_home, unit6_hobbies,
    unit7_market, unit8_beach,
)

# Guess What! is the American edition: teacher-facing templates say "students" (the grammar packs say "pupils").
WORDS = {"student": "student"}

UNITS = [m.SPEC for m in (unit0_welcome, unit1_garden, unit2_school, unit3_days, unit4_my_day, unit5_home,
                          unit6_hobbies, unit7_market, unit8_beach)]


def build_extras(pack_root: Path) -> list[Path]:
    from . import docs_gw, quarter_tests
    made: list[Path] = []
    made += quarter_tests.build_tests(pack_root)
    made.append(docs_gw.tests_readme(pack_root / "tests"))
    made += docs_gw.annual_plan(pack_root)
    made += docs_gw.course_map(pack_root)
    made += docs_gw.glossary(pack_root)
    made.append(docs_gw.pack_readme(pack_root))
    return made
