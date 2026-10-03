"""Destination A1 · mini-unit 3 — My home (Destination Unit 3, vocabulary)."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, OddOne, PicLabel, Reading, Section, Unscramble, WordSearch, WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.unit import UnitSpec, V, picture_card

from .common import BADGE, NOTE

VOCAB = [
    V("living room", "mehmonxona", "tv"), V("bedroom", "yotoqxona", "bed"), V("kitchen", "oshxona", "kitchen"),
    V("bathroom", "hammom", "bath"), V("garden", "bog'", "garden"), V("door", "eshik", "door"),
    V("window", "deraza", "window"), V("sofa", "divan", "sofa"), V("lamp", "chiroq", "lamp"),
    V("chair", "stul", "chair"),
]
EXTRA = [V("table", "stol", None), V("fridge", "muzlatgich", None), V("carpet", "gilam", None),
         V("cupboard", "shkaf", None), V("flat", "kvartira", None), V("house", "uy", "house")]

INFO = UnitInfo(
    number=3, title="My home", topic="Rooms and furniture; where things are",
    book="Destination A1, Unit 3 — Vocabulary: My home",
    vocabulary="living room, bedroom, kitchen, bathroom, garden, door, window, sofa, lamp, chair",
    grammar=["There is / there are + a room or a thing; Is there …? Are there …?",
             "Where is the lamp? It's on / in / next to / under the …",
             "I sleep in the bedroom. We cook in the kitchen."],
)

CARD = picture_card(VOCAB, "My home", cols=5,
                    tip="In + xona nomi: **in** the kitchen, **in** the bedroom. 'Uyda' = **at home** (the yo'q!).")

LESSONS = [
    Lesson.std(
        title="Rooms in my home",
        focus="Vocabulary — rooms and what we do in them",
        aims=["name five rooms and the garden", "say what we do in each room: I sleep in the bedroom."],
        language=["living room, bedroom, kitchen, bathroom, garden", "I sleep / cook / wash / watch TV in the …"],
        materials=["Flashcards (games/flashcards.pdf)", "Word card (grammar-card.pdf)", "Worksheet A exercises A, B"],
        greeting="Ask 'Do you live in a flat or a house?' and write the answers on the board.",
        warmup="**Floor plan**: draw a simple plan of a flat on the board and name the rooms with the class.",
        present="Present the room flashcards, one at a time, and attach an action: bedroom = sleep, kitchen = cook, bathroom = "
                "wash. Choral repetition. Stick the cards on the plan.",
        practice="Worksheet A exercises A (label), B (match sentences to rooms) and C (complete the words).",
        produce="**Where am I?** One pupil mimes (sleeping, cooking); the class asks 'Are you in the bedroom?'",
        wrap="Teacher says an action; pupils say the room. Homework.",
        homework="Draw a plan of your home and label four rooms (Worksheet A exercise F).",
        assessment="Point at cards for 5 pupils; note gaps.",
        tips=["'in the kitchen' (artikl bilan), lekin 'at home' (artiklsiz) — alohida eslatib qo'ying.",
              "'living room' — mehmonxona; ko'p o'zbek oilalarida 'zal' deyiladi. Ikkalasi ham bir xil xona.",
              "Support: use the picture card. Extension: add 'balcony' and 'hall'."],
    ),
    Lesson.std(
        title="Furniture and where it is",
        focus="Furniture words and prepositions: in, on, next to, under, behind",
        aims=["name furniture (sofa, lamp, chair, window, door)", "say where it is: The lamp is on the table."],
        language=["The lamp is on the table. · The chair is next to the window.", "in · on · under · next to · behind"],
        materials=["Furniture flashcards", "Preposition pictures from the Round-Up pack (or a ball and a box)", "Worksheet A D–E; B exercises A–B"],
        greeting="Hold a lamp or its picture: 'Where is the lamp? It's on the table.'",
        warmup="**Where's the ball?** Hide a ball and ask 'Is it under the chair?' until pupils find it.",
        present="Present furniture words with the flashcards. Revise prepositions with real objects.",
        practice="Worksheet A exercises D (word search) and E (odd one out); Worksheet B exercises A (circle) and B (fill in).",
        produce="**Describe and draw**: pairs describe a room ('There is a sofa next to the window.') while the partner draws.",
        wrap="Check the drawings against the descriptions. Homework.",
        homework="Write four sentences about furniture in your bedroom.",
        assessment="Check correct prepositions in the describe-and-draw task.",
        tips=["'in / on / under' — rasm yoki haqiqiy buyum bilan; o'zbekcha '-da, ustida, tagida'.",
              "'There is / are' oldingi bo'limda — takrorlab o'ting.",
              "Support: preposition pictures. Extension: add 'between'."],
    ),
    Lesson.std(
        title="My dream home",
        focus="Describe a home: There is / are, has got, adjectives",
        aims=["describe their home or dream home in 4–5 sentences", "ask and answer about each other's homes"],
        language=["There is a big garden. · There are two bedrooms. · My room isn't big.", "Is there a …? Yes, there is."],
        materials=["Paper and crayons", "Worksheet B exercises C–E"],
        greeting="Show a picture of a big house: 'Is this your home? No, it's my dream home.'",
        warmup="**Yes or no?** Pupils ask about a hidden picture of a home: 'Is there a garden?'",
        present="Model a description on the board using the frames from Worksheet B exercise E, then read the sample text "
                "(Worksheet B exercise D).",
        practice="Worksheet B exercises C (unscramble), D (reading) and E (writing).",
        produce="**Home interview**: pairs ask 'How many rooms are there? Is there a garden?' and draw each other's home.",
        wrap="Gallery walk: pupils read two descriptions and tick one sentence they like. Homework.",
        homework="Finish your description and add a drawing.",
        assessment="Mark Worksheet B exercise E for there is / are and room vocabulary.",
        tips=["Hikoya yozishda ketma-ketlik: avval xonalar, keyin mebel, so'ng bog'.",
              "Support: gapped model text. Extension: add adjectives (big, small, new, old, beautiful)."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "Ss-Ss", "Ss-Ss"),
    ),
]

A = [
    PicLabel("Look and write the words.", items=[
        ("tv", "living room"), ("bed", "bedroom"), ("kitchen", "kitchen"), ("bath", "bathroom"), ("garden", "garden"),
        ("door", "door"), ("window", "window"), ("sofa", "sofa")], cols=4),
    Match("Match the sentence to the place.", pairs=[
        ("You sleep here.", "bedroom"), ("You cook here.", "kitchen"), ("You wash here.", "bathroom"),
        ("You watch TV here.", "living room"), ("You play outside here.", "garden"), ("You sit here.", "sofa")],
          seed=501),
    Gaps("Look and complete the words.", items=[
        ("kitchen", "kitchen"), ("bed", "bedroom"), ("bath", "bathroom"), ("window", "window"), ("garden", "garden"),
        ("chair", "chair")]),
    WordSearch("Find eight words.", words=["kitchen", "bedroom", "bathroom", "garden", "window", "door", "sofa", "lamp"],
               size=11, seed=33),
    OddOne("Circle the odd one out.", rows=[
        (["sofa", "chair", "lamp", "kitchen"], "kitchen"), (["bedroom", "bathroom", "kitchen", "window"], "window"),
        (["door", "window", "sofa", "banana"], "banana")]),
    Draw("Draw a plan of your home. Label four rooms.", prompts=["My home"]),
]

B = [
    Circle("Choose the correct word (A, B or C).", items=[
        "There {*is|are|am} a sofa in the living room.", "There {is|*are|am} two windows.",
        "The lamp is {*on|in|under} the table.", "I sleep in the {*bedroom|kitchen|garden}.",
        "We cook in the {*kitchen|bathroom|bedroom}.", "My bed is {*next to|between|under} the window."]),
    Fill("Complete the sentences with words from the box.", items=[
        "[[prep-on|36]] The ball is {on} the box.", "[[prep-under|36]] The ball is {under} the table.",
        "[[prep-next to|36]] The ball is {next to} the box.", "[[prep-behind|36]] The ball is {behind} the box."],
         bank=True, extra_words=["in"]),
    Unscramble("Put the words in the right order.", items=[
        "There is a sofa.", "There are two windows.", "Is there a garden?", "The lamp is on the table."]),
    Reading("Read and answer.", title="My flat", text=(
        "I live in a flat in Tashkent. There are three rooms: a living room, a bedroom and a kitchen.\n\n"
        "There is a big sofa and a TV in the living room. My bed is next to the window. There isn't a garden."),
        questions=[("How many rooms are there?", "There are three."), ("Where is the sofa?", "In the living room."),
                   ("Is there a garden?", "No, there isn't.")]),
    WriteAbout("Write about your home or your dream home.", frames=[
        "There is a ___ .", "There are ___ ___ .", "My ___ is next to the ___ .", "There isn't a ___ ."], lines=4,
        model=["There is a big garden. There are two bedrooms. My bed is next to the window. There isn't a swimming pool."]),
]

QUIZ = [
    Section("Part 1 · Words", [
        PicLabel("Look and write the words.", items=[
            ("tv", "living room"), ("bed", "bedroom"), ("kitchen", "kitchen"), ("bath", "bathroom"),
            ("window", "window"), ("sofa", "sofa")], bank=False, cols=3, size=34)]),
    Section("Part 2 · Grammar", [
        Circle("Choose the correct word.", items=[
            "There {*is|are} a lamp.", "There {is|*are} three chairs.", "{*Is|Are} there a garden?",
            "The ball is {*under|in} the chair."]),
        Fill("Complete the sentences.", items=[
            "I sleep in the {bedroom}.", "We cook in the {kitchen}.", "There {isn't} a garden.",
            "{Are} there any windows?"], extra_words=["bathroom", "aren't"])]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="Jasur's house", text=(
            "Jasur lives in a house. There are four rooms and a garden. There is a lamp in his bedroom. "
            "There isn't a TV in the kitchen."), questions=[
            ("How many rooms are there?", "Four."), ("Is there a garden?", "Yes, there is."),
            ("Is there a TV in the kitchen?", "No, there isn't.")]),
        Unscramble("Put the words in the right order.", items=[
            "There is a sofa.", "Where is the lamp?", "The bed is next to the window."])]),
]

SPEC = UnitSpec(number=3, slug="unit-3-my-home", title="My home", info=INFO, vocab=VOCAB, extra_vocab=EXTRA,
                lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="Rooms and furniture", sheet_b_name="there is / are, prepositions, reading, writing",
                card=CARD, card_name="Word card", intro_note=NOTE)
