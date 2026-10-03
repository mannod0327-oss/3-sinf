"""Round-Up 3 · mini-unit 5 — expressing quantity (Round-Up Unit 5)."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, PicLabel, Reading, Section, Unscramble, WordSearch, WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.model import Box, Heading, Para, Table
from sinf.unit import UnitSpec, V

from .common import BADGE, GRADE_TIP_20

VOCAB = [
    V("eggs", "tuxumlar", "egg"), V("apples", "olmalar", "apple"), V("tomatoes", "pomidorlar", "tomato"),
    V("bananas", "bananlar", "banana"), V("milk", "sut", "milk"), V("water", "suv", "water"),
    V("bread", "non", "bread"), V("rice", "guruch", "rice"), V("cheese", "pishloq", "cheese"),
    V("honey", "asal", "honey"),
]
EXTRA = [
    V("some", "bir necha, ozgina", None), V("any", "biron, hech qanday", None), V("a lot of", "ko'p", None),
    V("many", "ko'p (sanaladigan)", None), V("much", "ko'p (sanalmaydigan)", None),
    V("a few", "bir nechta", None), V("a little", "ozgina", None),
]

INFO = UnitInfo(
    number=5, title="How many? How much?", topic="Countable and uncountable food; some, any, many, much, a lot of",
    book="Round-Up 3, Unit 5 — Expressing quantity",
    vocabulary="eggs, apples, tomatoes, bananas, milk, water, bread, rice, cheese, honey",
    grammar=["some (+) and any (− ?): There are some eggs. There isn't any milk. Is there any bread?",
             "How many + plural / How much + uncountable",
             "a lot of, many, much, a few, a little"],
)

CARD = [
    Heading("How many? How much?", 1),
    Table([["", "countable (eggs, apples)", "uncountable (milk, bread)"],
           ["+", "There are **some** eggs.\nThere are **a lot of** eggs.", "There is **some** milk.\nThere is **a lot of** milk."],
           ["−", "There aren't **any** eggs.\nI haven't got **many** eggs.", "There isn't **any** milk.\nI haven't got **much** milk."],
           ["?", "Are there **any** eggs?\n**How many** eggs are there?", "Is there **any** milk?\n**How much** milk is there?"],
           ["small", "**a few** eggs", "**a little** milk"]],
          widths=[0.1, 0.45, 0.45], header=True, style="grid", size=10.5),
    Box([Para("Count it? → **many**, **a few**, **How many**. Can't count it (milk, water, bread, rice)? → **much**, "
              "**a little**, **How much**.")], kind="grammar", title="Rule of thumb"),
    Box([Para("'Non', 'sut', 'guruch', 'suv' — sanab bo'lmaydi: 'two breads' emas, 'two pieces of bread'. "
              "Sanaladigan: 'tuxum', 'olma' → eggs, apples.")], kind="tip", title="Eslatma"),
]

LESSONS = [
    Lesson.std(
        title="some and any",
        focus="Countable and uncountable nouns; some (+), any (− ?)",
        aims=["say if a noun can be counted", "use some in positive and any in negative sentences and questions"],
        language=["There are some eggs. · There is some milk.", "There aren't any apples. · Is there any bread?"],
        materials=["Food picture cards (egg, apple, milk, bread)", "a picture of a fridge with some items",
                   "Grammar card"],
        greeting="Open a picture of a fridge: 'What is there in the fridge?'",
        warmup="**Count it!** Show cards; pupils say 'We can count it: one egg, two eggs' or 'We can't: milk'.",
        present="Sort the cards into countable / uncountable. Write the positive / negative / question pattern and "
                "underline some and any. Use the fridge picture for examples.",
        practice="Worksheet A exercises A (label), D (complete the words) and E (word search); Worksheet B exercise A "
                 "(circle some / any).",
        produce="**Spot the fridge**: pairs have two fridge pictures and ask 'Is there any milk?' to find the differences.",
        wrap="Quick-fire: show a card; pupils make a full sentence with some or any. Homework.",
        homework="Write five sentences about your kitchen with some and any.",
        assessment="Listen for some / any in the fridge game.",
        tips=["O'zbek tilida 'sanaladigan / sanalmaydigan' farq bor (non, sut). Xuddi shuni inglizchaga bog'lang.",
              "'some' ijobiy, 'any' inkor va so'roq. Istisno: taklif ('Would you like some tea?') — hozircha o'rgatmang.",
              "Support: colour-code countable (blue) and uncountable (green)."],
    ),
    Lesson.std(
        title="How many? How much?",
        focus="How many + plural, How much + uncountable; many / much",
        aims=["ask and answer: How many eggs are there? How much milk is there?", "choose many or much"],
        language=["How many (eggs) are there? — There are six. · How much (milk) is there? — A lot."],
        materials=["Real or picture items in bags", "Worksheet A exercises B, C; Worksheet B exercise B"],
        greeting="Ask 'How many pupils are there in our class?' and 'How much water is in this bottle?'",
        warmup="**Bag questions**: pupils ask 'How many apples are in the bag?' and guess; you show the answer.",
        present="Write the two question patterns side by side with examples. Stress: How many + plural noun, How much + "
                "uncountable noun.",
        practice="Worksheet A exercises B (match questions and answers) and C (circle many or much), Worksheet B exercise B.",
        produce="**Kitchen survey**: pupils ask 'How many eggs have you got at home?' 'How much bread?' and report.",
        wrap="Class chant: 'How many apples? How much milk?' with gestures. Homework.",
        homework="Workbook: write six questions with How many / How much and answer them.",
        assessment="Check pupils do not say 'How much eggs'.",
        tips=["'How much eggs' — keng tarqalgan xato, chunki o'zbekchada 'qancha' bitta. Ikkita so'zni (many / much) "
              "kartalarda ranglang.",
              "Pul uchun ham 'How much is it?' — keyingi bo'limlarda takrorlanadi.",
              "Support: sentence frames. Extension: add 'a lot of'."],
    ),
    Lesson.std(
        title="a lot of, a few, a little",
        focus="Quantities: a lot of, a few, a little — at the bazaar",
        aims=["use a lot of, a few and a little correctly", "role-play buying food at the bazaar"],
        language=["There is a lot of bread. · I have a few apples. · I want a little honey."],
        materials=["Play money and food picture cards", "Worksheet B exercises C–E"],
        greeting="Put several cards on the table: 'There are a lot of apples. There are a few bananas.'",
        warmup="**Lots or few?** Show a card with many or few items; pupils say 'a lot of' or 'a few'.",
        present="Show the small-quantity words: a few (countable), a little (uncountable). Compare with a lot of. "
                "Write three examples.",
        practice="Worksheet B exercises C (unscramble), D (reading at the bazaar) and E (writing).",
        produce="**At the bazaar**: shopkeepers and customers: 'Can I have a few apples and a little honey, please?' — "
                "'Here you are.'",
        wrap="Report: 'I bought …' Homework.",
        homework="Write a short shopping dialogue.",
        assessment="Observe correct a few / a little use in the role-play.",
        tips=["'a few' (bir nechta — sanaladigan), 'a little' (ozgina — sanalmaydigan). Juftlik qilib yodlating.",
              "Bozor kontekstidan foydalaning: 'Chorsu bozori' — bolalar uchun tanish vaziyat.",
              "Support: model dialogue on the board. Extension: add prices (How much is it? — 5,000 sum)."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "Ss-Ss", "T-Ss"),
    ),
]

A = [
    PicLabel("Look and write the words.", items=[
        ("egg", "eggs"), ("apple", "apples"), ("tomato", "tomatoes"), ("banana", "bananas"), ("milk", "milk"),
        ("water", "water"), ("bread", "bread"), ("rice", "rice")], cols=4),
    Match("Match the questions to the answers.", pairs=[
        ("How many eggs are there?", "There are six."), ("How much milk is there?", "There is a lot."),
        ("Are there any apples?", "No, there aren't any."), ("Is there any bread?", "Yes, there is some.")], seed=341),
    Circle("Circle many or much.", items=[
        "How {*many|much} eggs are there?", "How {many|*much} milk is there?", "How {*many|much} apples have you got?",
        "How {many|*much} water is there?", "How {*many|much} bananas are there?", "How {many|*much} rice is there?"]),
    Gaps("Look and complete the words.", items=[
        ("tomato", "tomatoes"), ("apple", "apples"), ("banana", "bananas"), ("cheese", "cheese"), ("honey", "honey"),
        ("rice", "rice")]),
    WordSearch("Find eight food words.", words=["eggs", "apples", "tomatoes", "bananas", "milk", "water", "bread",
                                                "rice"], size=10, seed=25),
    Draw("Draw your fridge with some food. Write: There are some ___ . There is some ___ .", prompts=["My fridge"]),
]

B = [
    Circle("Circle some or any.", items=[
        "There are {*some|any} eggs.", "There aren't {some|*any} apples.", "Is there {some|*any} milk?",
        "We've got {*some|any} bread.", "Are there {some|*any} tomatoes?", "There isn't {some|*any} cheese."]),
    Fill("Complete the sentences.", items=[
        "{How many} eggs are there? — There are six.", "{How much} milk is there? — A lot.",
        "We haven't got {much} water.", "I have {a few} apples.", "There is {a little} honey."], bank=True),
    Unscramble("Put the words in the right order.", items=[
        "Are there any apples?", "There isn't any milk.", "How much bread is there?", "We have a lot of rice."]),
    Reading("Read and answer.", title="At the bazaar", text=(
        "Dilnoza and her mum are at the bazaar. There are lots of tomatoes and apples, but there aren't any bananas "
        "today.\n\n"
        "There is a lot of bread, but there isn't much cheese. Mum buys six eggs and a little honey."), questions=[
        ("Are there any bananas?", "No, there aren't."), ("Is there much cheese?", "No, there isn't."),
        ("How many eggs does Mum buy?", "Six.")]),
    WriteAbout("Write about your fridge (real or imaginary).", frames=[
        "There are some ___ .", "There isn't any ___ .", "There is a lot of ___ ."], lines=3,
        model=["There are some eggs. There isn't any cheese. There is a lot of milk."]),
]

QUIZ = [
    Section("Part 1 · Food words", [
        PicLabel("Look and write the words.", items=[
            ("egg", "eggs"), ("apple", "apples"), ("milk", "milk"), ("bread", "bread"), ("rice", "rice"),
            ("cheese", "cheese")], bank=False, cols=3, size=34)]),
    Section("Part 2 · Grammar", [
        Circle("Circle the correct word.", items=[
            "There are {*some|any} bananas.", "Is there {some|*any} milk?", "How {*many|much} apples are there?",
            "We haven't got {*much|many} water."]),
        Fill("Complete the sentences.", items=[
            "There aren't {any} eggs.", "{How much} bread is there?", "I have {a few} tomatoes.",
            "There is {a lot of} rice."], extra_words=["some"])]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="Bobur's kitchen", text=(
            "There are six eggs in Bobur's kitchen. There is a lot of bread, but there isn't any cheese. "
            "There are a few apples."), questions=[
            ("How many eggs are there?", "Six."), ("Is there any cheese?", "No, there isn't."),
            ("Is there a lot of bread?", "Yes, there is.")]),
        Unscramble("Put the words in the right order.", items=[
            "Is there any water?", "There are some apples.", "How many eggs are there?"])]),
]

SPEC = UnitSpec(number=5, slug="unit-5-how-many-how-much", title="How many? How much?", info=INFO, vocab=VOCAB,
                extra_vocab=EXTRA, lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="Countable and uncountable food", sheet_b_name="some / any, How many / much, reading",
                card=CARD,
                intro_note="Adapted for Grade 3 (age 8–9, CEFR A1): the ideas come from the Round-Up 3 unit; all "
                           "exercises and texts are new.")
