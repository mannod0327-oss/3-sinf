"""Destination A1 · mini-unit 7 — food and shopping (Destination Units 22–24)."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, OddOne, PicLabel, Reading, Section, Unscramble, WordSearch, WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.model import Box, Heading, Para, Table
from sinf.unit import UnitSpec, V

from .common import BADGE, NOTE

VOCAB = [
    V("bread", "non", "bread"), V("milk", "sut", "milk"), V("cheese", "pishloq", "cheese"), V("rice", "guruch", "rice"),
    V("eggs", "tuxumlar", "egg"), V("apples", "olmalar", "apple"), V("tomatoes", "pomidorlar", "tomato"),
    V("potatoes", "kartoshkalar", "potato"), V("water", "suv", "water"), V("juice", "sharbat", "juice"),
]
EXTRA = [
    V("shop", "do'kon", "shop"), V("money", "pul", "money"), V("a kilo of", "bir kilo", None),
    V("a bottle of", "bir shisha", None), V("a packet of", "bir paket", None), V("a loaf of", "bir bo'lak (non)", None),
    V("a box of", "bir quti", "box"), V("sum", "so'm", "coin"),
]

INFO = UnitInfo(
    number=7, title="Food and shopping", topic="Buying food: quantities and prices",
    book="Destination A1, Units 22–24 — Countable and uncountable nouns; Vocabulary: Food and shopping",
    vocabulary="bread, milk, cheese, rice, eggs, apples, tomatoes, potatoes, water, juice",
    grammar=["countable (eggs, apples) and uncountable (milk, bread): some, any, a kilo of, a bottle of …",
             "How much is it? — It's 4,000 sum. · How much are the apples? — They're 10,000 sum.",
             "I'd like a loaf of bread, please. · Can I have …?"],
)

CARD = [
    Heading("Food and shopping", 1),
    Table([["a kilo of", "a bottle of", "a packet of", "a loaf of", "a box of"],
           ["apples\npotatoes\ntomatoes", "milk\nwater\njuice", "rice\ncheese", "bread", "eggs"]],
          widths=[1] * 5, header=True, style="grid", size=10.5, align="center"),
    Table([["Shop talk", ""],
           ["Can I help you?", "Yes, please. **I'd like** a loaf of bread."],
           ["Anything else?", "**Can I have** a bottle of milk, please?"],
           ["Here you are.", "**How much** is it? — It's 16,000 sum. — Thank you!"]],
          widths=[0.4, 0.6], header=True, style="grid", size=10.5),
    Box([Para("**some** (+): I'd like some bread. **any** (− ?): We haven't got any eggs. Have you got any milk? "
              "**How much** + uncountable (milk) · **How many** + plural (eggs).")], kind="grammar",
        title="some · any · How much · How many"),
    Box([Para("'Non' sanalmaydi: **a loaf of bread** yoki **some bread**. Narx: 'It's 4,000 sum' (so'm). "
              "Ko'plik narx: 'They're 10,000 sum'.")], kind="tip", title="Eslatma"),
]

LESSONS = [
    Lesson.std(
        title="Food words",
        focus="Vocabulary — ten food and drink words; countable and uncountable",
        aims=["name ten foods and drinks", "say if a noun is countable (eggs) or uncountable (milk)"],
        language=["bread, milk, cheese, rice, eggs, apples, tomatoes, potatoes, water, juice", "some · any"],
        materials=["Flashcards (games/flashcards.pdf)", "Word card (grammar-card.pdf)", "Worksheet A exercises A, E"],
        greeting="Ask 'What do you have for breakfast?' and write answers on the board.",
        warmup="**Feel and guess**: pupils touch real food or toys in a bag and guess the word.",
        present="Present the flashcards. Sort them into two columns: things we can count (eggs, apples) and things we "
                "can't (milk, rice).",
        practice="Worksheet A exercises A (label), B (match quantities), C (complete the words) and E (odd one out).",
        produce="**My shopping basket**: pupils draw a basket with five items and say 'I've got some bread and two apples.'",
        wrap="Teacher says a word; pupils say 'countable' or 'uncountable'. Homework.",
        homework="Learn the words; draw your breakfast (Worksheet A exercise F).",
        assessment="Check pupils' sorting into countable and uncountable.",
        tips=["'non', 'sut', 'guruch', 'suv' — sanalmaydigan; 'two breads' xato. 'a loaf of bread' deb ayting.",
              "Ko'plik: tomato → tomatoes, potato → potatoes (-es). Eslatib o'ting.",
              "Support: pictures only. Extension: add 'honey', 'sugar'."],
    ),
    Lesson.std(
        title="How much? A kilo of…",
        focus="Quantities and prices: a kilo of, a bottle of, a packet of, a loaf of; How much is it?",
        aims=["use a kilo of, a bottle of, a packet of, a loaf of, a box of", "ask and answer about prices in sum"],
        language=["a kilo of apples · a bottle of milk · a packet of rice · a loaf of bread · a box of eggs",
                  "How much is it? — It's 4,000 sum."],
        materials=["Price tags (in sum) for pictures or real items", "Worksheet A exercise B; Worksheet B exercises A–B"],
        greeting="Hold up a price tag: 'How much is the bread? It's 4,000 sum.'",
        warmup="**Price guess**: pupils guess the price of an item; closest wins.",
        present="Show each quantity phrase with a picture. Write 'How much is it?' and 'How much are they?' with answers.",
        practice="Worksheet A exercise B (match) and Worksheet B exercises A (circle) and B (complete the dialogue).",
        produce="**Price chain**: pupils pass a tag around: 'How much are the apples?' — 'They're 10,000 sum.'",
        wrap="Teacher says a price; pupils say what it could be. Homework.",
        homework="Make a price list of five items at home or in a shop.",
        assessment="Check it's / they're with prices.",
        tips=["'How much is the bread?' (birlik) / 'How much are the apples?' (ko'plik) — is / are farqiga e'tibor bering.",
              "Raqam: 4,000 = four thousand. Katta sonlarni sekin o'qing.",
              "Support: price tags with numbers written in words. Extension: add change (change — qaytim)."],
    ),
    Lesson.std(
        title="At the shop",
        focus="Role-play: I'd like … Can I have …? How much is it?",
        aims=["buy and sell food in a role-play", "write a short shop dialogue"],
        language=["Can I help you? — I'd like a loaf of bread, please. — Here you are. — How much is it?"],
        materials=["Play money (sum)", "Food picture cards", "Worksheet B exercises C–E"],
        greeting="Set up a shop corner with cards and play money. 'Welcome to my shop!'",
        warmup="**Shopkeeper's memory**: pupils name items on the table; you cover one — which is missing?",
        present="Model the dialogue with a volunteer. Write the key phrases on the board.",
        practice="Worksheet B exercises C (unscramble), D (reading) and E (writing a dialogue).",
        produce="**Shop role-play**: pairs swap roles (shopkeeper / customer) and buy three things each.",
        wrap="Volunteers perform for the class; the class says what they bought. Homework.",
        homework="Write a four-line shop dialogue.",
        assessment="Observe I'd like / Can I have / How much in the role-play.",
        tips=["Muloyim iboralar: **please**, **thank you**, **here you are**. Ularni doim talab qiling.",
              "'I'd like' = 'I would like' (istayman) — qisqartma sifatida o'rgating.",
              "Support: dialogue frame. Extension: add 'Anything else?'"],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "Ss-Ss", "T-Ss"),
    ),
]

A = [
    PicLabel("Look and write the words.", items=[
        ("bread", "bread"), ("milk", "milk"), ("cheese", "cheese"), ("rice", "rice"), ("egg", "eggs"),
        ("apple", "apples"), ("tomato", "tomatoes"), ("potato", "potatoes")], cols=4),
    Match("Match the quantity to the food. Use each food once.", pairs=[
        ("a kilo of", "apples"), ("a bottle of", "milk"), ("a packet of", "rice"), ("a loaf of", "bread"),
        ("a box of", "eggs")], seed=541),
    Gaps("Look and complete the words.", items=[
        ("cheese", "cheese"), ("tomato", "tomatoes"), ("potato", "potatoes"), ("juice", "juice"), ("water", "water"),
        ("apple", "apples")]),
    WordSearch("Find eight food words.", words=["bread", "milk", "cheese", "rice", "eggs", "apples", "tomatoes",
                                                "potatoes"], size=10, seed=37),
    OddOne("Circle the one you can count (the odd one out).", rows=[
        (["milk", "water", "rice", "apples"], "apples"), (["eggs", "apples", "tomatoes", "bread"], "bread"),
        (["juice", "cheese", "potatoes", "water"], "potatoes")]),
    Draw("Draw your shopping basket. Write: I'd like ___ .", prompts=["My shopping basket"]),
]

B = [
    Circle("Choose the correct word (A, B or C).", items=[
        "I'd like {*some|any|many} bread, please.", "Have you got {some|*any|many} milk?",
        "How {*much|many|long} is the bread? — It's 4,000 sum.", "How {*many|much|long} eggs do you want?",
        "I'd like {*a kilo of|a bottle of|a loaf of} apples.", "We haven't got {some|*any|a} cheese."]),
    Fill("Complete the shop dialogue.", items=[
        "— Can I {help} you? — {Yes}, please.", "— I'd {like} a loaf of bread.", "— Here you {are}.",
        "— {How much} is it? — It's 4,000 sum."], bank=True, extra_words=["much"]),
    Unscramble("Put the words in the right order.", items=[
        "I'd like some bread.", "How much is it?", "Have you got any milk?", "Here you are."]),
    Reading("Read and answer.", title="At the shop", text=(
        "Malika is at the shop with her mum. They need bread, milk and eggs. The bread is 4,000 sum. The milk is "
        "12,000 sum.\n\n"
        "Mum buys a loaf of bread and a bottle of milk. There aren't any eggs today."), questions=[
        ("How much is the bread?", "4,000 sum."), ("What does Mum buy?", "A loaf of bread and a bottle of milk."),
        ("Are there any eggs?", "No, there aren't.")]),
    WriteAbout("Write a shop dialogue (4 lines).", frames=[
        "— Can I help you?", "— I'd like ___ , please.", "— Here you are.", "— How much is it?"], lines=4,
        model=["— Can I help you? — I'd like a kilo of apples, please. — Here you are. — How much is it? — "
               "It's 10,000 sum."]),
]

QUIZ = [
    Section("Part 1 · Food words", [
        PicLabel("Look and write the words.", items=[
            ("bread", "bread"), ("milk", "milk"), ("cheese", "cheese"), ("egg", "eggs"), ("apple", "apples"),
            ("tomato", "tomatoes")], bank=False, cols=3, size=34)]),
    Section("Part 2 · Grammar", [
        Circle("Choose the correct word.", items=[
            "I'd like {*some|any} rice.", "Have you got {some|*any} cheese?", "How {*much|many} is the milk?",
            "A {*loaf|bottle} of bread."]),
        Fill("Complete the sentences.", items=[
            "I'd {like} a kilo of tomatoes.", "{How much} is the juice?", "There aren't {any} eggs.",
            "Here you {are}."], extra_words=["some"])]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="Bobur's shopping", text=(
            "Bobur buys a packet of rice and a kilo of apples. The rice is 9,000 sum. The apples are 10,000 sum. "
            "There aren't any tomatoes."), questions=[
            ("What does Bobur buy?", "A packet of rice and a kilo of apples."), ("How much is the rice?", "9,000 sum."),
            ("Are there any tomatoes?", "No, there aren't.")]),
        Unscramble("Put the words in the right order.", items=[
            "Can I have some milk?", "How much is the bread?", "There aren't any eggs."])]),
]

SPEC = UnitSpec(number=7, slug="unit-7-food-shopping", title="Food and shopping", info=INFO, vocab=VOCAB,
                extra_vocab=EXTRA, lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="Food words and quantities", sheet_b_name="Shop talk, some / any, reading, writing",
                card=CARD, intro_note=NOTE)
