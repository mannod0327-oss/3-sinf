"""Round-Up 3 · mini-unit 1 — Plurals, a / an, some (Round-Up Unit 1)."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, PicLabel, Reading, Section, TrueFalse, Unscramble, WordSearch, WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.model import Box, Heading, Para, Table
from sinf.unit import UnitSpec, V

from .common import BADGE, GRADE_TIP_20

VOCAB = [
    V("cat – cats", "mushuk", "cat"), V("box – boxes", "quti", "box"), V("bus – buses", "avtobus", "bus"),
    V("baby – babies", "chaqaloq", "baby"), V("leaf – leaves", "barg", "leaf"),
    V("child – children", "bola", "child"), V("man – men", "erkak", "man"), V("foot – feet", "oyoq (kafti)", "foot"),
    V("tooth – teeth", "tish", "tooth"), V("sheep – sheep", "qo'y", "sheep"), V("fish – fish", "baliq", "fish"),
    V("mouse – mice", "sichqon", "mouse"),
]
EXTRA = [V("milk", "sut", "milk"), V("water", "suv", "water"), V("bread", "non", "bread"), V("rice", "guruch", "rice")]

INFO = UnitInfo(
    number=1, title="Plurals, a / an, some", topic="One or many? Regular and irregular plurals; a, an, some",
    book="Round-Up 3, Unit 1 — Plurals of countable and uncountable nouns",
    vocabulary="cat, box, bus, baby, leaf, child, man, foot, tooth, sheep, fish, mouse (+ milk, water, bread, rice)",
    grammar=["Regular plurals: -s, -es, -ies (cats, boxes, babies) and -ves (leaves)",
             "Irregular plurals: children, men, feet, teeth, mice, sheep, fish",
             "a / an with one thing, some with many things and with milk, water, bread, rice"],
)

CARD = [
    Heading("One or many? — plurals", 1),
    Table([["Rule", "One", "Many"],
           ["+ s", "a cat · a book", "cats · books"],
           ["+ es (s, x, ch, sh, o)", "a bus · a box · a watch · a tomato", "buses · boxes · watches · tomatoes"],
           ["y → ies (after a consonant)", "a baby · a story", "babies · stories"],
           ["f → ves", "a leaf · a wolf", "leaves · wolves"],
           ["**Irregular**", "child · man · woman · foot · tooth · mouse", "children · men · women · feet · teeth · mice"],
           ["**Same word**", "a sheep · a fish", "sheep · fish"]],
          widths=[0.3, 0.35, 0.35], header=True, style="grid", size=11),
    Box([Para("**a** cat · **an** apple · **some** cats · **some** milk"),
         Para("milk, water, bread, rice — one thing, no plural: **some** milk, not milks.")], kind="grammar",
        title="a · an · some"),
    Box([Para("O'zbek tilida ko'plik -lar (mushuk**lar**). Inglizchada -s / -es qo'shiladi, ba'zi so'zlar butunlay "
              "o'zgaradi (child → children). Sonlardan keyin ham ko'plik: two book**s**, three child**ren**.")],
        kind="tip", title="Eslatma"),
]

LESSONS = [
    Lesson.std(
        title="Regular plurals",
        focus="One or many: -s, -es, -ies, -ves",
        aims=["say and write regular plurals (cats, boxes, babies, leaves)", "choose the correct ending"],
        language=["one cat – two cats · one box – two boxes · one baby – two babies · one leaf – two leaves"],
        materials=["Flashcards (games/flashcards.pdf)", "Grammar card (grammar-card.pdf)", "Worksheet A exercises A, C"],
        greeting="Greet the class and count objects in the room together: 'One desk, two desks …'",
        warmup="**How many?** Show one flashcard and then two: 'One cat. Two … ?' — pupils complete the plural.",
        present="Put four columns on the board (+s, +es, -ies, -ves) and sort the flashcards into them while saying the "
                "words. Underline the endings and point out the spelling change baby → babies.",
        practice="Worksheet A exercises A (complete the plurals with pictures) and C (circle the correct spelling). "
                 "Check with the class using whiteboards.",
        produce="**Plural race**: two teams write as many plurals as they can in two minutes from the flashcard words.",
        wrap="Teacher says a singular word; pupils clap and answer with the plural. Homework.",
        homework="Workbook: write the plurals of ten nouns from your bag or room.",
        assessment="Check the spelling of -es and -ies plurals on the whiteboards.",
        tips=["Ko'plik qo'shimchasini ajratib ko'rsating: -lar (o'zbekcha) = -s / -es. Raqamdan keyin ham ko'plik "
              "kerak: 'three box' emas, 'three boxes'.",
              "'-es' ni aniq talaffuz qiling /ɪz/: boxes, buses.",
              "Support: sorting with cards only. Extension: add leaf → leaves, knife → knives."],
    ),
    Lesson.std(
        title="Irregular plurals",
        focus="child → children, man → men, foot → feet, tooth → teeth, mouse → mice, sheep, fish",
        aims=["say the seven irregular plurals", "use them in short sentences"],
        language=["one child – two children · one man – two men · one foot – two feet · one tooth – two teeth · "
                  "one mouse – two mice · one sheep – two sheep"],
        materials=["Picture cards of the irregular nouns", "Worksheet A exercises B, D, E"],
        greeting="Ask 'How many children are there in our class?' — 'There are … children.'",
        warmup="**Odd words**: write ten plurals on the board; pupils stand when they hear one that is irregular.",
        present="Show pairs of pictures (one / two) and build the list on the board in two colours: regular and "
                "irregular. Drill the irregular ones with gestures (feet = stamp, teeth = smile).",
        practice="Worksheet A exercises B (match), D (word search) and E (true or false). Play **Plural dominoes** in pairs.",
        produce="**Picture dictation**: pupils listen and draw 'two sheep, three children, four mice' and compare.",
        wrap="Whole-class chant: 'child-children, man-men, foot-feet, tooth-teeth.' Homework.",
        homework="Learn the seven irregular plurals and draw them (Worksheet A exercise F).",
        assessment="Check who says 'childs' or 'mans'; note for reteaching.",
        tips=["'childs', 'mans', 'foots' — bu eng keng tarqalgan xato (o'zbekcha -lar qoidasini umumlashtirish). "
              "Bu so'zlarni 'maxsus ro'yxat' sifatida yodlatish kerak.",
              "'sheep' va 'fish' — bir xil: 'one sheep, two sheep'.",
              "Support: use the picture cards. Extension: add woman – women, person – people."],
    ),
    Lesson.std(
        title="a, an or some?",
        focus="a / an with one thing; some with many and with milk, water, bread, rice",
        aims=["use a, an and some correctly", "say what they have got: I've got an apple and some bread"],
        language=["a cat · an apple · some cats · some milk", "I've got … / We've got …"],
        materials=["Real or picture items (apple, egg, bread, milk)", "Worksheet B exercises A–E"],
        greeting="Show items one by one: 'What have I got? An apple. Some bread.'",
        warmup="**Sort the basket**: pupils put items into two boxes — *a / an (one)* and *some (many / uncountable)*.",
        present="Explain: a before a consonant sound, an before a vowel sound; some for many or for things we don't count. "
                "Write five examples on the board.",
        practice="Worksheet B exercises A (circle), B (fill), C (unscramble). Check in pairs.",
        produce="**Shopping basket**: pairs choose five items from a picture list and say 'I've got a book, two pencils and "
                "some paper.'",
        wrap="Reading (Worksheet B exercise D) and writing (exercise E). Homework.",
        homework="Write what is in your school bag with a / an / some.",
        assessment="Mark Worksheet B exercise E for a / an / some and plural endings.",
        tips=["O'zbek tilida artikl yo'q — **a / an** ni tushirib qoldirish keng tarqalgan xato ('I have cat' o'rniga "
              "'I have a cat').",
              "'an' — unli **tovush** oldidan: an apple, an orange, an elephant (harf emas, tovush).",
              "Support: a / an sound sort with cards. Extension: add an hour, a university (oral)."],
        interactions=("T-Ss", "G", "T-Ss", "S / Ss-Ss", "Ss-Ss", "S"),
    ),
]

A = [
    Fill("Write the plural.", items=[
        "[[cat|22]] one cat — two {cats}", "[[box|22]] one box — two {boxes}", "[[bus|22]] one bus — two {buses}",
        "[[baby|22]] one baby — two {babies}", "[[leaf|22]] one leaf — two {leaves}",
        "[[tomato|22]] one tomato — two {tomatoes}"], bank=True),
    Match("Match the singular to the plural.", pairs=[
        ("a child", "children"), ("a man", "men"), ("a foot", "feet"), ("a tooth", "teeth"), ("a mouse", "mice"),
        ("a sheep", "sheep")], seed=301),
    Circle("Circle the correct spelling.", items=[
        "two {*boxes|boxs}", "three {*babies|babys}", "four {*leaves|leafs}", "five {*buses|buss}",
        "six {*children|childs}", "two {*tomatoes|tomatos}"]),
    WordSearch("Find eight plurals.", words=["boxes", "babies", "leaves", "children", "mice", "feet", "teeth",
                                             "buses"], size=10, seed=21),
    TrueFalse("Write T (true) or F (false).", items=[
        ("One sheep, two sheeps.", False), ("One mouse, two mice.", True), ("One child, two childs.", False),
        ("One foot, two feet.", True), ("One baby, two babies.", True), ("One bus, two buss.", False)]),
    Draw("Draw two children, three sheep and four leaves. Write the words.", prompts=["Plurals picture"]),
]

B = [
    Circle("Circle a, an or some.", items=[
        "I've got {*an|a|some} apple.", "She has {a|*an|some} orange.", "There is {a|an|*some} milk in the glass.",
        "We've got {a|an|*some} bread.", "He's got {*a|an|some} book.", "It's {a|*an|some} elephant."]),
    Fill("Complete the sentences with the plural.", items=[
        "I've got two {feet}.", "There are three {sheep} in the field.", "Two {children} are in the garden.",
        "The cat catches two {mice}.", "I clean my {teeth} every day."], bank=True),
    Unscramble("Put the words in the right order.", items=[
        "I've got two boxes.", "There are three babies.", "We've got some bread.", "She has an orange."]),
    Reading("Read and answer.", title="At the farm", text=(
        "Aziz and Malika are at the farm. They see three sheep and two cows. There are four babies in the barn.\n\n"
        "There are two men and three children too. Aziz has a sandwich and some milk."), questions=[
        ("How many sheep are there?", "There are three."),
        ("Who has some milk?", "Aziz."),
        ("How many children are there?", "There are three.")]),
    WriteAbout("Write about your bag or your room.", frames=[
        "I've got two ___ .", "I've got three ___ .", "I've got some ___ ."], lines=3,
        model=["I've got two books. I've got three pencils. I've got some paper."]),
]

QUIZ = [
    Section("Part 1 · Plurals", [
        Fill("Write the plural.", items=[
            "[[cat|22]] one cat — two {cats}", "[[bus|22]] one bus — two {buses}",
            "[[baby|22]] one baby — two {babies}", "[[leaf|22]] one leaf — two {leaves}",
            "[[child|22]] one child — two {children}", "[[mouse|22]] one mouse — two {mice}"], bank=False)]),
    Section("Part 2 · a, an, some", [
        Circle("Circle the correct word.", items=[
            "I've got {*an|a} egg.", "We've got {a|*some} rice.", "She has two {*boxes|boxs}.",
            "He has {*a|an} banana."]),
        Match("Match the singular to the plural.", pairs=[
            ("a man", "men"), ("a foot", "feet"), ("a tooth", "teeth"), ("a sheep", "sheep")], seed=311)]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="My room", text=(
            "I have a bed and two chairs in my room. I have an umbrella and some books. "
            "There are three pictures on the wall."), questions=[
            ("How many chairs are there?", "Two."), ("Has the writer got an umbrella?", "Yes, he / she has."),
            ("How many pictures are there?", "Three.")]),
        Unscramble("Put the words in the right order.", items=[
            "There are two sheep.", "She has an apple.", "I've got some milk."])]),
]

SPEC = UnitSpec(number=1, slug="unit-1-plurals-a-an-some", title="Plurals, a / an, some", info=INFO, vocab=VOCAB,
                extra_vocab=EXTRA, lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="Plural forms", sheet_b_name="a / an / some, reading, writing", card=CARD,
                intro_note="Adapted for Grade 3 (age 8–9, CEFR A1): the ideas come from the Round-Up 3 unit; all "
                           "exercises and texts are new.")
