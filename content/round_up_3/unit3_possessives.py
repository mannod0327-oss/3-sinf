"""Round-Up 3 · mini-unit 3 — possessives and demonstratives (Round-Up Unit 3)."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, PicLabel, Reading, Section, Unscramble, WordSearch, WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.model import Box, Heading, Para, Table
from sinf.unit import UnitSpec, V

from .common import BADGE, GRADE_TIP_20

VOCAB = [
    V("pen", "ruchka", "pen"), V("pencil", "qalam", "pencil"), V("book", "kitob", "book"),
    V("bag", "sumka, ryukzak", "bag"), V("ruler", "chizg'ich", "ruler"), V("notebook", "daftar", "notebook"),
    V("scissors", "qaychi", "scissors"), V("computer", "kompyuter", "computer"), V("chair", "stul", "chair"),
    V("desk", "parta", None),
]
EXTRA = [
    V("my – mine", "mening – meniki", None), V("your – yours", "sening – seniki", None),
    V("his – his", "uning – uniki (erkak)", None), V("her – hers", "uning – uniki (ayol)", None),
    V("our – ours", "bizning – bizniki", None), V("their – theirs", "ularning – ularniki", None),
    V("this / these", "bu / bular (yaqin)", None), V("that / those", "o'sha / o'shalar (uzoq)", None),
]

INFO = UnitInfo(
    number=3, title="Possessives, this / that", topic="Whose is it? Near and far things",
    book="Round-Up 3, Unit 3 — Possessives / Demonstratives",
    vocabulary="pen, pencil, book, bag, ruler, notebook, scissors, computer, chair, desk",
    grammar=["my, your, his, her, its, our, their + noun; Aziz's book",
             "mine, yours, his, hers, ours, theirs (without a noun)",
             "this / these (near) — that / those (far)"],
)

CARD = [
    Heading("Whose is it?", 1),
    Table([["I", "you", "he", "she", "it", "we", "they"],
           ["**my** pen", "**your** pen", "**his** pen", "**her** pen", "**its** tail", "**our** pen", "**their** pen"],
           ["**mine**", "**yours**", "**his**", "**hers**", "—", "**ours**", "**theirs**"]],
          widths=[1] * 7, header=True, style="grid", size=10.5, align="center"),
    Box([Para("Aziz**'s** book · Malika**'s** bag · the boys**'** ball (more than one boy)."),
         Para("This pen is **mine**. = This is **my** pen.")], kind="grammar", title="'s and pronouns"),
    Table([["near (1)", "near (many)", "far (1)", "far (many)"],
           ["**this** pen", "**these** pens", "**that** pen", "**those** pens"]],
          widths=[1] * 4, header=True, style="grid", size=11, align="center"),
    Box([Para("Uzoqdagi narsa — o'zbekcha 'u, o'sha'; yaqin narsa — 'bu'. Inglizcha: **this / these** = bu, "
              "**that / those** = u (o'sha). Ko'plik: this → these, that → those.")], kind="tip", title="Eslatma"),
]

LESSONS = [
    Lesson.std(
        title="my, your, his, her, our, their",
        focus="Possessive adjectives and possessive 's",
        aims=["say who things belong to: This is my pen. That is Aziz's bag.", "use 's for one owner"],
        language=["my · your · his · her · its · our · their", "Aziz's book · Malika's bag"],
        materials=["Real objects (pens, books, bags)", "Flashcards", "Worksheet A exercises A, B; Worksheet B exercise A"],
        greeting="Hold up a pupil's bag: 'Whose bag is this?' Elicit 'It's Bobur's bag.'",
        warmup="**Lost property**: put five objects on a table; pupils claim theirs: 'It's my pen!'",
        present="Write the pronoun row (I, you, he …) and the matching possessive (my, your …). Show 's with real owners "
                "(Aziz's book). Colour the boy words blue and the girl words red.",
        practice="Worksheet A exercises A (label) and B (match), Worksheet B exercise A (circle). Check in pairs.",
        produce="**Pass and say**: pupils pass objects around a circle and say 'This is Anna's ruler. Her ruler is red.'",
        wrap="Teacher points at objects; pupils say 'That is … 's … ' Homework.",
        homework="Write six sentences with my, your, his, her about things in your bag.",
        assessment="Note who confuses his and her.",
        tips=["'his / her': o'zbekchada bitta 'uning' — rasm bilan mashq qiling.",
              "'its' (uning — narsa/hayvon) bilan 'it's' (it is) farqi — hozircha eshitish darajasida.",
              "Support: use real owners. Extension: add 'because' reasons."],
    ),
    Lesson.std(
        title="mine, yours, his, hers",
        focus="Possessive pronouns: This pen is mine.",
        aims=["use mine, yours, his, hers, ours, theirs without a noun", "answer Whose … is this?"],
        language=["This pen is mine. · That bag is hers. · Whose is this? — It's yours."],
        materials=["Real objects", "Worksheet A exercise B; Worksheet B exercises B–C"],
        greeting="Ask 'Whose is this?' holding different pupils' items.",
        warmup="**Mine!** Pupils race to grab the item you name and say 'It's mine!'",
        present="Write two sentences side by side: 'This is my pen.' / 'This pen is mine.' Show the pronoun table "
                "(mine, yours, his, hers, ours, theirs). Stress: no noun after mine / yours …",
        practice="Worksheet A exercise B (match adjectives to pronouns) and Worksheet B exercises B and C.",
        produce="**Whose is it?** In groups, pupils put items in a bag; one pupil draws an item and asks 'Whose is this?' "
                "— the owner says 'It's mine!'",
        wrap="Quick-fire: point at things and pupils say 'It's his / hers / theirs.' Homework.",
        homework="Workbook: fill in the possessive pronoun table and write four sentences.",
        assessment="Check that pupils do not add a noun after mine / hers.",
        tips=["'mine' = 'meniki' (-niki qo'shimchasi): 'Bu qalam meniki' = 'This pencil is mine'. O'xshashlik yordam beradi.",
              "'This is mine pen' — keng tarqalgan xato: mine dan keyin ot kelmaydi.",
              "Support: pronoun table on the board. Extension: add Whose are these? They're Malika's."],
    ),
    Lesson.std(
        title="this, that, these, those",
        focus="Near and far; one and many",
        aims=["use this / these for near things and that / those for far things", "ask What's this? What are those?"],
        language=["This is a pen. · These are pens. · That is a chair. · Those are chairs."],
        materials=["Objects near and far", "Worksheet B exercise B"],
        greeting="Hold a book near you and point to a far one: 'This book … that book.'",
        warmup="**Near or far?** Point and say 'this' or 'that'; pupils raise hand near / arm far.",
        present="Stand at the front; show this / these with objects in your hands and that / those with objects at the back. "
                "Write the four forms in a 2 × 2 table (near/far, one/many).",
        practice="Worksheet B exercise B (circle). Pairs point at classroom objects and ask What's this? / What are those?",
        produce="**Classroom shop**: one pupil is the shopkeeper; customers ask for 'this pen' or 'those pencils' and point.",
        wrap="Whole-class drill with pointing. Homework.",
        homework="Draw four pictures (near / far, one / many) and label them this, these, that, those.",
        assessment="Observe correct choice in the shop role-play.",
        tips=["Masofa tushunchasini **ishora** bilan bog'lang: yaqin — qo'l ichida, uzoq — qo'lni cho'zing.",
              "'these / those' ko'plik; 'these' /ðiːz/, 'those' /ðəʊz/ — 'th' talaffuziga e'tibor bering.",
              "Support: gestures. Extension: add colours (that red pen)."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "Ss-Ss", "G", "T-Ss"),
    ),
]

A = [
    PicLabel("Look and write the words.", items=[
        ("pen", "pen"), ("pencil", "pencil"), ("book", "book"), ("bag", "bag"), ("ruler", "ruler"),
        ("notebook", "notebook"), ("scissors", "scissors"), ("computer", "computer")], cols=4),
    Match("Match the possessive adjective to the pronoun.", pairs=[
        ("my", "mine"), ("your", "yours"), ("her", "hers"), ("our", "ours"), ("their", "theirs")], seed=331),
    Circle("Circle the correct word.", items=[
        "This is {*my|mine} pen.", "This pen is {my|*mine}.", "That is {*her|hers} bag.", "That bag is {her|*hers}.",
        "These are {*our|ours} books.", "Those books are {our|*ours}."]),
    Gaps("Look and complete the words.", items=[
        ("pencil", "pencil"), ("ruler", "ruler"), ("notebook", "notebook"), ("scissors", "scissors"),
        ("computer", "computer"), ("chair", "chair")]),
    WordSearch("Find eight school words.", words=["pencil", "ruler", "notebook", "scissors", "bag", "computer",
                                                  "desk", "chair"], size=11, seed=23),
    Draw("Draw your school bag. Label five things: my ___ .", prompts=["My school bag"]),
]

B = [
    Circle("Circle the correct word.", items=[
        "This is Anna. {*Her|His} bag is red.", "Tom and I have a dog. {*Our|Their} dog is big.",
        "Aziz has a pen. {*His|Her} pen is blue.", "You have a ruler. {*Your|My} ruler is long.",
        "The cat has a ball. {*Its|It's} ball is yellow.", "Malika and Dilnoza have bags. {*Their|Our} bags are new."]),
    Circle("Circle this, that, these or those.", items=[
        "{*This|That} is my book. (It is in my hand.)", "{This|*That} is the board. (It is far away.)",
        "{*These|Those} are my pens. (They are in my hand.)", "{These|*Those} are the windows. (They are far away.)"]),
    Fill("Complete with mine, yours, his, hers, ours or theirs.", items=[
        "This is my pen. It's {mine}.", "That is your bag. It's {yours}.", "These are Bobur's books. They're {his}.",
        "That is Malika's ruler. It's {hers}.", "We have a dog. It's {ours}."], bank=True, extra_words=["theirs"]),
    Unscramble("Put the words in the right order.", items=[
        "This is my pen.", "That bag is hers.", "These are Aziz's books.", "Whose ruler is this?"]),
    Reading("Read and answer.", title="Lost property", text=(
        "It is Monday morning. There is a blue bag on the desk. \"Whose bag is this?\" asks Miss Nodira. "
        "\"It's mine,\" says Sardor.\n\n"
        "There are two pencils too. \"Those pencils are Malika's,\" says Sardor. \"They're hers.\" Malika says, "
        "\"Thank you!\""), questions=[
        ("Whose is the blue bag?", "It's Sardor's. It's his."), ("Whose are the pencils?", "They're Malika's."),
        ("Who says 'Thank you'?", "Malika.")]),
    WriteAbout("Write about things in your bag.", frames=[
        "This is my ___ .", "That is ___'s ___ .", "These are my ___ ."], lines=3,
        model=["This is my pen. That is Aziz's ruler. These are my books."]),
]

QUIZ = [
    Section("Part 1 · Words", [
        PicLabel("Look and write the words.", items=[
            ("pen", "pen"), ("pencil", "pencil"), ("ruler", "ruler"), ("scissors", "scissors"), ("bag", "bag"),
            ("computer", "computer")], bank=False, cols=3, size=34)]),
    Section("Part 2 · Grammar", [
        Circle("Circle the correct word.", items=[
            "This is Bobur. {*His|Her} bag is green.", "That book is {*hers|her}.", "{*These|This} are my pens.",
            "{*Those|That} are the windows. (far away)"]),
        Fill("Complete the sentences.", items=[
            "This is my pen. It's {mine}.", "We have a cat. {Our} cat is black.", "That is Anna's bag. It's {hers}.",
            "{This} is my ruler. (near)"], extra_words=["their"])]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="Whose is it?", text=(
            "There is a red ball in the garden. It's Aziz's ball. It's his. There are two bikes too. "
            "They're Malika's and Dilnoza's. They're theirs."), questions=[
            ("Whose is the red ball?", "It's Aziz's. It's his."), ("How many bikes are there?", "Two."),
            ("Whose are the bikes?", "They're Malika's and Dilnoza's. They're theirs.")]),
        Unscramble("Put the words in the right order.", items=[
            "That is her pen.", "These books are ours.", "Whose bag is this?"])]),
]

SPEC = UnitSpec(number=3, slug="unit-3-possessives-this-that", title="Possessives, this / that", info=INFO,
                vocab=VOCAB, extra_vocab=EXTRA, lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="School things and possessives", sheet_b_name="my / mine, this / that, reading",
                card=CARD,
                intro_note="Adapted for Grade 3 (age 8–9, CEFR A1): the ideas come from the Round-Up 3 unit; all "
                           "exercises and texts are new.")
