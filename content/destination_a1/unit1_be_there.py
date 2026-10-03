"""Destination A1 · mini-unit 1 — to be; there is / there are; this / that (Destination Unit 1)."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, PicLabel, Reading, Section, TrueFalse, Unscramble, WordSearch, WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.model import Box, Heading, Para, Table
from sinf.unit import UnitSpec, V

from .common import BADGE, NOTE

VOCAB = [
    V("board", "doska", "board"), V("desk", "parta", None), V("door", "eshik", "door"),
    V("window", "deraza", "window"), V("lamp", "chiroq", "lamp"), V("chair", "stul", "chair"),
    V("computer", "kompyuter", "computer"), V("bag", "sumka", "bag"), V("book", "kitob", "book"),
    V("clock", "soat", "clock"),
]
EXTRA = [V("there is", "bor (birlik)", None), V("there are", "bor (ko'plik)", None),
         V("this / these", "bu / bular", None), V("that / those", "o'sha / o'shalar", None)]

INFO = UnitInfo(
    number=1, title="be, there is / are, this / that", topic="Our classroom: where things are",
    book="Destination A1, Unit 1 — to be; there is / there are; it's; this / these / that / those",
    vocabulary="board, desk, door, window, lamp, chair, computer, bag, book, clock",
    grammar=["to be: I am · you / we / they are · he / she / it is (+ negative and questions)",
             "there is (one) / there are (many); there isn't / aren't; Is there …? Are there …?",
             "it's · this / these (near) · that / those (far)"],
)

CARD = [
    Heading("am / is / are · there is / there are", 1),
    Table([["to be", "there is / there are"],
           ["I **am** · you **are** · he / she / it **is**\nwe / you / they **are**\nI'm not · he isn't · they aren't\n"
            "**Is** she ten? Yes, she **is**.",
            "There **is** a board. (1)\nThere **are** two windows. (2, 3 …)\nThere **isn't** a clock. · There **aren't** "
            "any books.\n**Is there** a lamp? Yes, there **is**.\n**Are there** any chairs? No, there **aren't**."]],
          widths=[0.45, 0.55], header=True, style="grid", size=10.5),
    Table([["this", "these", "that", "those"], ["**This** is a book.", "**These** are books.", "**That** is a door.",
                                               "**Those** are doors."]],
          widths=[1] * 4, header=True, style="grid", size=10.5, align="center"),
    Box([Para("'There is' — bir narsa; 'there are' — ikki va undan ko'p. 'There is two chairs' — xato! "
              "'Bor' so'zi o'zbekchada bitta, inglizchada ikkita shakl bor.")], kind="tip", title="Eslatma"),
]

LESSONS = [
    Lesson.std(
        title="am, is, are",
        focus="to be with all pronouns; negatives and questions",
        aims=["use am / is / are correctly with I, you, he, she, it, we, they", "ask and answer yes / no questions with be"],
        language=["I am · she is · they are", "I'm not · he isn't · Are you …? Is he …?"],
        materials=["Pronoun cards", "Grammar card", "Worksheet A exercise B; Worksheet B exercises A, C"],
        greeting="Greet pupils and introduce yourself: 'I am Miss … I am a teacher.' Write 'I am' on the board.",
        warmup="**Who am I?** Hold a picture (a teacher, a doctor); pupils ask 'Are you a teacher?' (yes / no).",
        present="Build the table on the board: I am, you are, he / she / it is, we / you / they are. Add contractions, then "
                "negatives and questions. Use classroom examples ('The door is brown. The windows are big.').",
        practice="Worksheet A exercise B (circle) and Worksheet B exercise A; fast finishers do exercise E (true / false).",
        produce="**Ask and answer**: pupils stand in two lines and ask 'Are you nine?' 'Is your name Bobur?' — short answers only.",
        wrap="Teacher says a pronoun, pupils say the form: 'he' → 'is'. Homework.",
        homework="Write six sentences about your family with am / is / are.",
        assessment="Listen for am / is / are in the pairs.",
        tips=["O'zbek tilida 'bo'lmoq' bog'lovchisi gapda ko'rinmaydi ('Men o'quvchiman'). Inglizchada **am/is/are** shart.",
              "Qisqartma: I'm, he's, they're — og'zaki nutqda ko'p ishlatiladi.",
              "Support: pronoun–verb matching cards. Extension: add Where / What questions."],
    ),
    Lesson.std(
        title="There is, there are",
        focus="there is / there are; there isn't / aren't; Is there …? Are there …?",
        aims=["describe a room: There is a board. There are two windows.", "ask and answer: Is there a clock? Are there any books?"],
        language=["There is a board. · There are two windows.", "There isn't a clock. · Are there any books? — No, there aren't."],
        materials=["A picture of a classroom", "Flashcards of classroom things", "Worksheet A exercises A, C–E"],
        greeting="Ask 'What is in our classroom?' and collect words on the board.",
        warmup="**Count and say**: point at things in the room: 'There is one door. There are two windows.'",
        present="Write the two patterns (there is + one, there are + many). Show negatives and questions. Use a picture of a "
                "classroom and change details to practise.",
        practice="Worksheet A exercises A (label), C (fill in), D (word search), E (complete words).",
        produce="**Classroom survey**: pairs draw their ideal classroom and describe it: 'There are three computers.'",
        wrap="Teacher says a number and a noun; pupils make the sentence. Homework.",
        homework="Describe your bedroom with there is / there are (Worksheet B exercise F).",
        assessment="Check is / are agreement with singular and plural nouns.",
        tips=["'There is + bitta', 'there are + ko'p' — sonlarni doskada raqam bilan ko'rsating: 1 → is, 2+ → are.",
              "'Is there …?' savolida 'any' faqat ko'plik uchun: Are there any books?",
              "Support: use pictures with numbers. Extension: add prepositions (on the wall)."],
    ),
    Lesson.std(
        title="This, that, these, those",
        focus="it's; this / these (near) and that / those (far)",
        aims=["use this / these for near things and that / those for far things", "say and write: These are my pens. That is the door."],
        language=["This is a book. · These are books. · That is a door. · Those are doors.", "It's a clock. They're clocks."],
        materials=["Objects near and far", "Worksheet B exercises B–D"],
        greeting="Hold a book: 'This is a book.' Point to the board: 'That is the board.'",
        warmup="**Near or far?** Pupils stretch their arm for 'that / those' and keep it close for 'this / these'.",
        present="Show the 2 × 2 table (near / far, one / many). Practise with real objects at different distances.",
        practice="Worksheet B exercises B (circle), C (unscramble) and D (reading).",
        produce="**Classroom shop**: customers point and ask for 'this pen' or 'those books'; the shopkeeper answers 'Here you are.'",
        wrap="Teacher points; pupils say 'This / That / These / Those …'. Homework.",
        homework="Take four photos or draw four pictures (near / far, one / many) and label them.",
        assessment="Observe the correct choice in the shop role-play.",
        tips=["Masofani imo-ishora bilan bog'lang: yaqin — qo'l bilan ushlab, uzoq — qo'lni cho'zib ko'rsating.",
              "'these / those' — ko'plik: -s qo'shimchasi ikkalasida ham kerak (books, doors).",
              "Support: gestures and real objects. Extension: add adjectives (that big door)."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "G", "T-Ss"),
    ),
]

A = [
    PicLabel("Look and write the words.", items=[
        ("board", "board"), ("door", "door"), ("window", "window"), ("lamp", "lamp"), ("chair", "chair"),
        ("computer", "computer"), ("bag", "bag"), ("clock", "clock")], cols=4),
    Circle("Choose the correct word (A, B or C).", items=[
        "I {*am|is|are} in Class 3.", "She {am|*is|are} my sister.", "We {am|is|*are} friends.",
        "They {am|is|*are} at school.", "The door {am|*is|are} brown.", "The windows {am|is|*are} big."]),
    Fill("Write is or are.", items=[
        "There {is} a board on the wall.", "There {are} two windows.", "There {is} a clock near the door.",
        "There {are} thirty books on the shelf.", "There {is} a computer on the desk."], bank=True),
    WordSearch("Find eight classroom words.", words=["board", "door", "window", "lamp", "chair", "computer", "clock",
                                                      "bag"], size=10, seed=31),
    Gaps("Look and complete the words.", items=[
        ("window", "window"), ("computer", "computer"), ("clock", "clock"), ("lamp", "lamp"), ("chair", "chair"),
        ("board", "board")]),
    TrueFalse("Write T (true) or F (false).", items=[
        ("I am ten and you are nine.", True), ("There is two doors in our classroom.", False),
        ("Those are my pens. (far away)", True), ("She am my friend.", False),
        ("There are some chairs.", True)]),
]

B = [
    Circle("Choose the correct word (A, B or C).", items=[
        "{*Am|Is|Are} I late?", "{Am|*Is|Are} he your brother?", "{Am|Is|*Are} they at home?",
        "Aziz {*isn't|aren't|amn't} here today.", "I {*'m not|isn't|aren't} hungry.", "{Am|Is|*Are} you ready?"]),
    Circle("Choose this, that, these or those.", items=[
        "{*This|That} is my bag. (in my hand)", "{This|*That} is the board. (on the far wall)",
        "{*These|Those} are my pens. (in my hand)", "{These|*Those} are the windows. (far away)"]),
    Unscramble("Put the words in the right order.", items=[
        "There is a board.", "There are two windows.", "Is there a clock?", "These are my books."]),
    Reading("Read and answer.", title="Our classroom", text=(
        "This is our classroom. It is big and clean. There is a board on the wall and there is a clock next to the door.\n\n"
        "There are twenty chairs and ten desks. There are three windows. There isn't a computer, but there are a lot of "
        "books on the shelf."), questions=[
        ("Is there a clock?", "Yes, there is."), ("How many windows are there?", "There are three."),
        ("Is there a computer?", "No, there isn't.")]),
    WriteAbout("Write about your classroom or your bedroom.", frames=[
        "There is a ___ .", "There are ___ ___ .", "There isn't a ___ ."], lines=3,
        model=["There is a board. There are twenty chairs. There isn't a computer."]),
]

QUIZ = [
    Section("Part 1 · Words", [
        PicLabel("Look and write the words.", items=[
            ("board", "board"), ("door", "door"), ("window", "window"), ("lamp", "lamp"), ("chair", "chair"),
            ("clock", "clock")], bank=False, cols=3, size=34)]),
    Section("Part 2 · Grammar", [
        Circle("Choose the correct word.", items=[
            "She {am|*is|are} nine.", "There {*are|is} three windows.", "{*Is|Are} there a clock?",
            "{*Those|That} are the doors. (far away)"]),
        Fill("Complete the sentences.", items=[
            "I {am} ten years old.", "There {is} a board.", "{Are} there any chairs? — Yes, there are.",
            "{These} are my books. (near)"], extra_words=["those", "is"])]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="My room", text=(
            "There is a bed in my room. There are two chairs and a lamp. There isn't a computer."), questions=[
            ("Is there a bed?", "Yes, there is."), ("How many chairs are there?", "Two."),
            ("Is there a computer?", "No, there isn't.")]),
        Unscramble("Put the words in the right order.", items=[
            "There is a lamp.", "Are there any books?", "Those are my bags."])]),
]

SPEC = UnitSpec(number=1, slug="unit-1-be-there-is-this-that", title="be, there is / are, this / that", info=INFO,
                vocab=VOCAB, extra_vocab=EXTRA, lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="Classroom words, be, there is / are", sheet_b_name="Questions, this / that, reading",
                card=CARD, intro_note=NOTE)
