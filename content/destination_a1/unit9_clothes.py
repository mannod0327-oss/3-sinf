"""Destination A1 · mini-unit 9 — clothes and appearance (Destination Units 27 and 33)."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, OddOne, PicLabel, Reading, Section, Unscramble, WordSearch, WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.model import Box, Heading, Para, Table
from sinf.unit import UnitSpec, V

from .common import BADGE, NOTE

VOCAB = [
    V("T-shirt", "futbolka", "tshirt"), V("jeans", "jinsi", "jeans"), V("dress", "ko'ylak (qizlar uchun)", "dress"),
    V("cap", "kepka", "cap"), V("shoes", "poyabzal", "shoe"), V("socks", "paypoq", "socks"), V("coat", "palto", "coat"),
    V("scarf", "sharf", "scarf"), V("gloves", "qo'lqop", "gloves"), V("hat", "shlyapa", "hat"),
]
EXTRA = [
    V("tall", "baland bo'yli", None), V("short", "past bo'yli", None), V("long hair", "uzun soch", None),
    V("short hair", "kalta soch", None), V("brown eyes", "jigarrang ko'z", "eye"), V("young", "yosh", "young"),
    V("old", "keksa", "old man"),
]

INFO = UnitInfo(
    number=9, title="Clothes and appearance", topic="What people wear and what they look like",
    book="Destination A1, Units 27 and 33 — Vocabulary: Character and appearance; Clothes and fashion",
    vocabulary="T-shirt, jeans, dress, cap, shoes, socks, coat, scarf, gloves, hat",
    grammar=["He is wearing a blue T-shirt. · I'm wearing a coat.",
             "She has got long hair. · He has got brown eyes. · They haven't got hats.",
             "He is tall. · She is young. · Who is it?"],
)

CARD = [
    Heading("Clothes and appearance", 1),
    Table([["[[tshirt|40]]\n**T-shirt**", "[[jeans|40]]\n**jeans**", "[[dress|40]]\n**dress**", "[[cap|40]]\n**cap**",
            "[[shoe|40]]\n**shoes**"],
           ["[[socks|40]]\n**socks**", "[[coat|40]]\n**coat**", "[[scarf|40]]\n**scarf**", "[[gloves|40]]\n**gloves**",
            "[[hat|40]]\n**hat**"]],
          widths=[1] * 5, style="grid", size=10.5, align="center", row_height=32),
    Table([["is / are (what he looks like)", "has got (what he has)", "is wearing (now)"],
           ["He **is** tall.\nShe **is** young.\nThey **are** short.", "She **has got** long hair.\nHe **has got** brown eyes.\n"
            "They **haven't got** hats.", "He **is wearing** a blue cap.\nI **am wearing** a coat.\nThey **are wearing** gloves."]],
          widths=[0.33, 0.34, 0.33], header=True, style="grid", size=10.5),
    Box([Para("jeans, socks, shoes, gloves — **ko'plik**: 'These jeans are blue', 'a pair of jeans'.")], kind="grammar",
        title="Always plural"),
    Box([Para("'U baland bo'yli' = 'He **is** tall'. 'Uning uzun sochi bor' = 'She **has got** long hair'. "
              "Ikkala fe'lni (is / has got) aralashtirmang.")], kind="tip", title="Eslatma"),
]

LESSONS = [
    Lesson.std(
        title="Clothes",
        focus="Vocabulary — ten clothes words; He is wearing …",
        aims=["name ten clothes", "say what someone is wearing: He is wearing a blue cap."],
        language=["T-shirt, jeans, dress, cap, shoes, socks, coat, scarf, gloves, hat", "He / She is wearing …"],
        materials=["Flashcards (games/flashcards.pdf)", "Word card (grammar-card.pdf)", "Worksheet A exercises A, B"],
        greeting="Ask 'What are you wearing today?' and write answers on the board.",
        warmup="**Who is wearing…?** 'Stand up if you are wearing something blue.' Pupils respond with 'I'm wearing blue socks.'",
        present="Present the flashcards. Point out plural words (jeans, socks, shoes, gloves).",
        practice="Worksheet A exercises A (label), B (match clothes and where we wear them), C (complete) and D (word search).",
        produce="**Dress the doll**: pairs dress a paper figure and describe it: 'It is wearing a red hat.'",
        wrap="Teacher says a clothes word; pupils say the colour and put a counter on the matching picture. Homework.",
        homework="Learn the words; draw yourself in your favourite clothes (Worksheet A exercise F).",
        assessment="Point at cards for 5 pupils; note gaps.",
        tips=["'jeans', 'socks', 'shoes', 'gloves' — doim ko'plik: 'These jeans are …' (this jeans emas).",
              "'wear' (kiymoq, kiyib yurmoq) — 'put on' (kiyib olmoq) bilan aralashtirmang.",
              "Support: pictures only. Extension: add colours to each item."],
    ),
    Lesson.std(
        title="What does he look like?",
        focus="Appearance: is / has got + tall, short, long hair, brown eyes, young, old",
        aims=["describe a person: He is tall. He has got short hair.", "use is / has got correctly"],
        language=["He is tall. · She is young. · He has got brown eyes. · She hasn't got short hair."],
        materials=["Pictures of people", "Worksheet A exercise E; Worksheet B exercises A–C"],
        greeting="Show a picture: 'Who is this? What does he look like?'",
        warmup="**Describe and draw**: you describe a face; pupils draw it.",
        present="Show the two patterns on the board: **is** + adjective; **has got** + hair / eyes. Colour them differently.",
        practice="Worksheet B exercises A (circle), B (fill in) and C (unscramble).",
        produce="**My partner**: pupils describe their partner in three sentences and the partner says 'right' or 'wrong'.",
        wrap="Quick-fire: teacher says a description; pupils say whether it fits a given picture. Homework.",
        homework="Describe a family member in four sentences.",
        assessment="Check is vs has got.",
        tips=["'He has got long hair' — 'is' bilan emas! 'He is long hair' — keng tarqalgan xato.",
              "'short' ikki ma'noli: past bo'yli (short) va kalta (short hair).",
              "Support: sentence frames. Extension: add colours of hair and eyes."],
    ),
    Lesson.std(
        title="Guess who?",
        focus="Describe people and clothes in a guessing game and in writing",
        aims=["describe a person with clothes and appearance", "write 5 sentences about a friend"],
        language=["He is tall. He has got short hair. He is wearing a red cap and jeans. Who is he?"],
        materials=["A picture of 6 people", "Worksheet B exercises D–E"],
        greeting="Show the picture of 6 people: 'I'm thinking of one person.'",
        warmup="**Yes / no**: pupils ask 'Is it a boy? Has he got short hair?' to guess.",
        present="Read the model text (Worksheet B exercise D) and underline is / has got / is wearing.",
        practice="Worksheet B exercises D (reading) and E (writing).",
        produce="**Guess who?** In pairs: one pupil describes a classmate; the other guesses.",
        wrap="Volunteers describe a classmate and the class guesses. Homework.",
        homework="Describe a friend or family member and draw them.",
        assessment="Mark Worksheet B exercise E for is / has got / is wearing.",
        tips=["O'yin paytida bolalar ismini aytmasin — faqat tasvir. Hurmat qoidasi: tashqi ko'rinish haqida xushmuomala gapiring.",
              "Support: gapped model text. Extension: add 'but' (He is tall but she is short)."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "Ss-Ss", "T-Ss"),
    ),
]

A = [
    PicLabel("Look and write the clothes.", items=[
        ("tshirt", "T-shirt"), ("jeans", "jeans"), ("dress", "dress"), ("cap", "cap"), ("shoe", "shoes"),
        ("socks", "socks"), ("coat", "coat"), ("scarf", "scarf")], cols=4),
    Match("Match the clothes to where we wear them.", pairs=[
        ("You wear them on your feet. You take them off at the door.", "shoes"), ("You wear them on your hands.", "gloves"),
        ("You wear it round your neck.", "scarf"), ("You wear them inside your shoes.", "socks"),
        ("You wear it over your clothes when it's cold.", "coat"), ("You wear them on your legs.", "jeans")], seed=561),
    Gaps("Look and complete the words.", items=[
        ("jeans", "jeans"), ("scarf", "scarf"), ("gloves", "gloves"), ("socks", "socks"), ("dress", "dress"),
        ("coat", "coat")]),
    WordSearch("Find eight clothes words.", words=["jeans", "scarf", "gloves", "socks", "dress", "coat", "shoes",
                                                    "hat"], size=10, seed=39),
    OddOne("Circle the odd one out.", rows=[
        (["jeans", "dress", "scarf", "banana"], "banana"), (["coat", "gloves", "scarf", "window"], "window"),
        (["socks", "shoes", "cap", "tall"], "tall")]),
    Draw("Draw yourself. Colour your clothes. Write: I am wearing ___ .", prompts=["I am wearing ________ ."]),
]

B = [
    Circle("Choose the correct word (A, B or C).", items=[
        "He {*is|has|have} tall.", "She {*has|have|is} got long hair.", "I {*am|is|are} wearing a blue coat.",
        "They {*are|is|am} wearing gloves.", "She {*is|are|has} young.", "He {*has|have|is} got brown eyes."]),
    Fill("Complete the sentences.", items=[
        "She {is} wearing a red dress.", "He {has} got short hair.", "I {am} wearing a coat.",
        "They {are} wearing hats."], bank=True, extra_words=["have"]),
    Unscramble("Put the words in the right order.", items=[
        "He is wearing a red cap.", "She has got long hair.", "They are wearing gloves.", "Who is he?"]),
    Reading("Read and answer.", title="Who is it?", text=(
        "This boy is tall. He has got short black hair and brown eyes. He is wearing blue jeans, a white T-shirt and a red "
        "cap.\n\n"
        "He is wearing white socks and black shoes. Who is he? He is Bobur."), questions=[
        ("What colour is his hair?", "Black."), ("What is he wearing on his head?", "A red cap."),
        ("Is he short?", "No, he isn't. He is tall.")]),
    WriteAbout("Describe a friend or a family member.", frames=[
        "My friend is ___ .", "He / She has got ___ hair and ___ eyes.", "He / She is wearing ___ .",
        "Who is it?"], lines=4,
        model=["My friend is tall. She has got long hair and brown eyes. She is wearing a blue dress and white shoes. "
               "Who is it?"]),
]

QUIZ = [
    Section("Part 1 · Clothes", [
        PicLabel("Look and write the clothes.", items=[
            ("tshirt", "T-shirt"), ("jeans", "jeans"), ("dress", "dress"), ("coat", "coat"), ("scarf", "scarf"),
            ("gloves", "gloves")], bank=False, cols=3, size=34)]),
    Section("Part 2 · Grammar", [
        Circle("Choose the correct word.", items=[
            "He {*is|has} tall.", "She {*has|is} got long hair.", "I {*am|is} wearing a coat.",
            "They {*are|is} wearing gloves."]),
        Fill("Complete the sentences.", items=[
            "She {is} wearing a hat.", "He {has} got brown eyes.", "We {are} wearing jeans.",
            "I {am} wearing socks."], extra_words=["have"])]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="My sister", text=(
            "My sister is young. She has got long hair and blue eyes. She is wearing a yellow dress and a white hat."),
            questions=[("Is she young?", "Yes, she is."), ("What colour are her eyes?", "Blue."),
                       ("What is she wearing on her head?", "A white hat.")]),
        Unscramble("Put the words in the right order.", items=[
            "He has got short hair.", "She is wearing a coat.", "They are tall."])]),
]

SPEC = UnitSpec(number=9, slug="unit-9-clothes-appearance", title="Clothes and appearance", info=INFO, vocab=VOCAB,
                extra_vocab=EXTRA, lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="Clothes words", sheet_b_name="is / has got / is wearing, reading, writing",
                card=CARD, intro_note=NOTE)
