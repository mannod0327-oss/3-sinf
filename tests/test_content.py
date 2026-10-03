"""Content sanity checks: every answer key, picture, point total and lesson timing is validated."""
from __future__ import annotations

import importlib
import re

import pytest

from sinf import icons
from sinf.exercises import (
    BRACE, Circle, Exercise, Fill, Gaps, Match, Order, OddOne, PicLabel, Reading, Section, TrueFalse,
    Unscramble, WordSearch, WriteAbout, total_points,
)
from sinf.games import make_wordsearch

PACKS = ["guess_what.pack", "round_up_3.pack", "destination_a1.pack"]


def all_units():
    units = []
    for mod in PACKS:
        try:
            units.extend((mod.split(".")[0], u) for u in importlib.import_module(mod).UNITS)
        except ModuleNotFoundError as exc:
            if not (exc.name or "").startswith(mod.split(".")[0]):
                raise
    return units


UNITS = all_units()
IDS = [f"{p}:{u.slug}" for p, u in UNITS]


def exercises_of(items):
    for it in items:
        if isinstance(it, Section):
            yield from it.exercises
        elif isinstance(it, Exercise):
            yield it


def every_string(obj):
    """Yield every string reachable inside an exercise (for icon-token checks)."""
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, (list, tuple)):
        for x in obj:
            yield from every_string(x)
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from every_string(k)
            yield from every_string(v)
    elif hasattr(obj, "__dict__"):
        for v in vars(obj).values():
            yield from every_string(v)


@pytest.mark.parametrize("pack,unit", UNITS, ids=IDS)
def test_vocabulary_has_translation_and_icon(pack, unit):
    assert unit.vocab, "unit has no vocabulary"
    for v in unit.vocab + unit.extra_vocab:
        assert v.en.strip() and v.uz.strip(), f"missing text for {v}"
        if v.icon:
            assert icons.has(v.icon), f"icon '{v.icon}' for '{v.en}' is missing"


@pytest.mark.parametrize("pack,unit", UNITS, ids=IDS)
def test_icon_tokens_resolve(pack, unit):
    for items in (unit.worksheet_a, unit.worksheet_b, unit.quiz):
        for text in every_string(list(exercises_of(items))):
            for name in re.findall(r"\[\[([^\]|]+)", text):
                assert icons.has(name.strip()), f"unknown icon [[{name}]] in: {text[:60]}"


@pytest.mark.parametrize("pack,unit", UNITS, ids=IDS)
def test_exercise_answers_are_well_formed(pack, unit):
    for items in (unit.worksheet_a, unit.worksheet_b, unit.quiz):
        for ex in exercises_of(items):
            if isinstance(ex, Circle):
                for t in ex.items:
                    groups = BRACE.findall(t)
                    assert groups, f"Circle item without options: {t}"
                    for g in groups:
                        opts = g.split("|")
                        assert len(opts) >= 2, f"need two options: {t}"
                        assert sum(o.startswith("*") for o in opts) == 1, f"exactly one * per group: {t}"
            elif isinstance(ex, Fill):
                for t in ex.items:
                    assert BRACE.findall(t), f"Fill item without blank: {t}"
                    assert all(b.strip() for b in BRACE.findall(t))
            elif isinstance(ex, Match):
                lefts = [a for a, _ in ex.pairs]
                rights = [b for _, b in ex.pairs]
                assert len(set(lefts)) == len(lefts) and len(set(rights)) == len(rights), "duplicate in Match"
                assert len(ex.pairs) <= 12
            elif isinstance(ex, Unscramble):
                for s in ex.items:
                    assert len(s.split()) >= 2, s
                    assert s[0].isupper() and s[-1] in ".?!", f"sentence style: {s}"
            elif isinstance(ex, Reading):
                assert ex.text.strip() and ex.questions
                for q, a in ex.questions:
                    assert q.strip().endswith("?") and a.strip()
            elif isinstance(ex, PicLabel):
                for icon, ans in ex.items:
                    assert icons.has(icon), f"PicLabel icon {icon}"
                assert len({a for _, a in ex.items}) == len(ex.items), "duplicate PicLabel answers"
            elif isinstance(ex, Gaps):
                for icon, word in ex.items:
                    assert icons.has(icon), f"Gaps icon {icon}"
                    assert Gaps.hide(word) != word and Gaps.hide(word).count("_") >= 1, f"nothing hidden in {word}"
            elif isinstance(ex, OddOne):
                for words, odd in ex.rows:
                    assert odd in words and len(set(words)) == len(words)
            elif isinstance(ex, Order):
                assert len(set(ex.items)) == len(ex.items)
            elif isinstance(ex, TrueFalse):
                assert ex.items
            elif isinstance(ex, WordSearch):
                grid, placed = make_wordsearch(ex.words, ex.size, ex.seed)
                assert len(placed) == len({w.upper() for w in ex.words})
            elif isinstance(ex, WriteAbout):
                assert ex.model and ex.marks > 0


@pytest.mark.parametrize("pack,unit", UNITS, ids=IDS)
def test_quiz_is_twenty_points(pack, unit):
    assert total_points(unit.quiz) == 20, f"quiz has {total_points(unit.quiz)} points"


@pytest.mark.parametrize("pack,unit", UNITS, ids=IDS)
def test_lessons_fill_45_minutes(pack, unit):
    assert unit.lessons
    for i, lesson in enumerate(unit.lessons, 1):
        assert lesson.minutes == 45, f"lesson {i} '{lesson.title}' is {lesson.minutes} minutes"
        assert lesson.aims and lesson.language and lesson.materials
        assert lesson.homework.strip() and lesson.assessment.strip()
        assert len(lesson.stages) >= 5
