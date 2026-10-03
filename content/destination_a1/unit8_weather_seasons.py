"""Destination A1 · mini-unit 8 — weather and seasons (Destination Unit 30, vocabulary)."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, OddOne, PicLabel, Reading, Section, Unscramble, WordSearch, WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.unit import UnitSpec, V, picture_card

from .common import BADGE, NOTE

VOCAB = [
    V("sunny", "quyoshli", "sun"), V("rainy", "yomg'irli", "rain"), V("windy", "shamolli", "wind"),
    V("cloudy", "bulutli", "cloud"), V("snowy", "qorli", "snowman"), V("hot", "issiq", "hot"),
    V("cold", "sovuq", "cold"), V("spring", "bahor", "spring"), V("summer", "yoz", "summer"),
    V("autumn", "kuz", "autumn"), V("winter", "qish", "winter"),
]
EXTRA = [V("stormy", "bo'ronli", "thunder"), V("warm", "iliq", None), V("What's the weather like?", "Ob-havo qanday?", None),
         V("Navro'z", "Navro'z (21-mart)", "flower")]

INFO = UnitInfo(
    number=8, title="Weather and seasons", topic="What's the weather like? Four seasons in Uzbekistan",
    book="Destination A1, Unit 30 — Vocabulary: Weather and seasons, nature and ecology",
    vocabulary="sunny, rainy, windy, cloudy, snowy, hot, cold, spring, summer, autumn, winter",
    grammar=["What's the weather like? — It's sunny / It's raining.",
             "In summer it's hot. · In winter it's cold and snowy.",
             "I like summer because it's hot. · We wear coats in winter."],
)

CARD = picture_card(VOCAB, "Weather and seasons", cols=4,
                    tip="Mavsum oldidan **in**: in spring, in summer, in autumn, in winter. 'It's sunny' (it is). "
                        "Navro'z — 21-mart, bahor boshlanishi.")

LESSONS = [
    Lesson.std(
        title="What's the weather like?",
        focus="Vocabulary — weather words; It's sunny / rainy / windy / cloudy / snowy",
        aims=["name seven weather words", "ask and answer: What's the weather like? It's sunny."],
        language=["sunny, rainy, windy, cloudy, snowy, hot, cold, stormy", "What's the weather like? — It's …"],
        materials=["Flashcards (games/flashcards.pdf)", "Word card (grammar-card.pdf)", "Worksheet A exercises A, B"],
        greeting="Look out of the window: 'What's the weather like today?'",
        warmup="**Weather mime**: pupils mime weather (shiver for cold, fan for hot, blow for windy); the class guesses.",
        present="Present the flashcards. Teach 'It's + adjective'. Choral repetition with actions.",
        practice="Worksheet A exercises A (label), C (complete) and D (word search).",
        produce="**Weather report**: pairs make a TV weather report for four cities with weather pictures.",
        wrap="Teacher shows a card; pupils say 'It's windy.' Homework.",
        homework="Learn the weather words; draw today's weather (Worksheet A exercise F).",
        assessment="Point at cards for 5 pupils; note gaps.",
        tips=["'It's sunny' — 'It' ob-havoda majburiy: 'Is sunny' xato. O'zbekchada 'Havo ochiq' — egasi yo'q.",
              "'hot' (havo issiq) va 'warm' (iliq) farqi — 'cold' va 'cool' bilan solishtiring.",
              "Support: pictures only. Extension: add 'foggy', 'stormy'."],
    ),
    Lesson.std(
        title="Four seasons",
        focus="Seasons and their weather; Navro'z",
        aims=["name the four seasons and say the weather: In summer it's hot.", "match seasons with months"],
        language=["spring, summer, autumn, winter", "In spring it's warm and rainy. · In winter it's cold and snowy."],
        materials=["Season posters", "Worksheet A exercise B; Worksheet B exercises A–C"],
        greeting="Ask 'Which season is it now? What's your favourite season?'",
        warmup="**Season corners**: four corners of the room are the four seasons; pupils run to the season you call.",
        present="Show a year circle with months and seasons. Link Navro'z (21 March) with spring.",
        practice="Worksheet A exercise B (match seasons and weather); Worksheet B exercises A (circle), B (fill in) and C "
                 "(unscramble).",
        produce="**Season talk**: pairs ask 'What's the weather like in winter?' and answer for Uzbekistan.",
        wrap="Teacher names a month; pupils say the season. Homework.",
        homework="Write four sentences about the four seasons where you live.",
        assessment="Check In + season and It's + adjective.",
        tips=["O'zbekistonda 4 fasl aniq: bahor (Navro'z), yoz (juda issiq), kuz, qish. Mahalliy tajribadan foydalaning.",
              "'autumn' /ˈɔːtəm/ — 'n' aytilmaydi.",
              "Support: month cards. Extension: add 'because' reasons."],
    ),
    Lesson.std(
        title="My favourite season",
        focus="Opinions and clothes: I like … because …; We wear … in …",
        aims=["say their favourite season and why", "link weather and clothes: We wear coats in winter."],
        language=["I like summer because it's hot. · We wear coats in winter. · I don't like winter because it's cold."],
        materials=["Clothes flashcards (coat, scarf, gloves, hat, cap)", "Worksheet B exercises D–E"],
        greeting="Show a coat and a hat: 'When do we wear these?'",
        warmup="**What do we wear?** Call a weather word; pupils name clothes.",
        present="Model: 'I like autumn because it's windy and I fly a kite.' Write the frame on the board.",
        practice="Worksheet B exercises D (reading) and E (writing).",
        produce="**Season poster**: groups draw one season with weather, clothes and activities and present it.",
        wrap="Gallery walk: pupils vote for their favourite poster. Homework.",
        homework="Finish your text and add a picture.",
        assessment="Poster rubric: weather (1), clothes (1), sentences (1).",
        tips=["Sabab bog'lovchisi: 'because'. Gapni 'because' dan boshlamang: 'I like summer because it's hot.'",
              "Support: gapped model text. Extension: compare two seasons."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "G", "T-Ss"),
    ),
]

A = [
    PicLabel("Look and write the weather words.", items=[
        ("sun", "sunny"), ("rain", "rainy"), ("wind", "windy"), ("cloud", "cloudy"), ("snowman", "snowy"),
        ("hot", "hot"), ("cold", "cold"), ("thunder", "stormy")], cols=4),
    Match("Match the season to the weather.", pairs=[
        ("In spring", "it's warm and rainy."), ("In summer", "it's hot and sunny."),
        ("In autumn", "it's windy and cloudy."), ("In winter", "it's cold and snowy.")], seed=551),
    Gaps("Look and complete the words.", items=[
        ("sun", "sunny"), ("cloud", "cloudy"), ("wind", "windy"), ("summer", "summer"), ("autumn", "autumn"),
        ("winter", "winter")]),
    WordSearch("Find eight words.", words=["sunny", "rainy", "windy", "cloudy", "snowy", "spring", "summer",
                                           "autumn"], size=10, seed=38),
    OddOne("Circle the odd one out.", rows=[
        (["sunny", "rainy", "windy", "Monday"], "Monday"), (["spring", "summer", "autumn", "March"], "March"),
        (["hot", "cold", "warm", "apple"], "apple")]),
    Draw("Draw the weather today. Write: It's ___ .", prompts=["Today it's ________ ."]),
]

B = [
    Circle("Choose the correct word (A, B or C).", items=[
        "It's {*rainy|rain|rains} today.", "In summer it {*is|are|has} hot.", "What's the weather {*like|likes|is}?",
        "I like winter {*because|so|but} I like snow.", "We wear coats {*in|on|at} winter.", "It's {*raining|rain|rains} now."]),
    Fill("Complete the sentences with words from the box.", items=[
        "What's the weather {like}?", "It's {sunny} today.", "In {summer} it's hot.", "I wear a {coat} in winter."],
         bank=True, extra_words=["hat"]),
    Unscramble("Put the words in the right order.", items=[
        "What's the weather like?", "It's sunny today.", "In winter it's cold.", "I like summer because it's hot."]),
    Reading("Read and answer.", title="Seasons in Uzbekistan", text=(
        "In Uzbekistan there are four seasons. In spring it is warm and sometimes rainy. Navro'z is in March.\n\n"
        "In summer it is very hot and sunny. In autumn it is windy and the leaves fall. In winter it is cold and sometimes "
        "snowy."), questions=[
        ("How many seasons are there?", "Four."), ("When is Navro'z?", "In March (in spring)."),
        ("What is the weather like in summer?", "It is very hot and sunny.")]),
    WriteAbout("Write about your favourite season.", frames=[
        "My favourite season is ___ .", "It's ___ and ___ .", "We wear ___ .", "I like ___ because ___ ."], lines=4,
        model=["My favourite season is spring. It's warm and rainy. We wear light coats. I like spring because "
               "it's Navro'z."]),
]

QUIZ = [
    Section("Part 1 · Weather words", [
        PicLabel("Look and write the words.", items=[
            ("sun", "sunny"), ("rain", "rainy"), ("wind", "windy"), ("cloud", "cloudy"), ("hot", "hot"),
            ("cold", "cold")], bank=False, cols=3, size=34)]),
    Section("Part 2 · Grammar", [
        Circle("Choose the correct word.", items=[
            "It's {*sunny|sun} today.", "In winter it's {*cold|hot}.", "What's the weather {*like|is}?",
            "I like summer {*because|but} it's hot."]),
        Fill("Complete the sentences.", items=[
            "What's the weather {like}?", "In {winter} it's cold and snowy.", "It's {raining} now.",
            "We wear coats {in} winter."], extra_words=["on", "summer"])]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="Autumn", text=(
            "It is autumn. It is windy and cloudy. Aziz is flying a kite in the park. He is wearing a coat. "
            "He likes autumn because it is windy."), questions=[
            ("What's the weather like?", "It is windy and cloudy."), ("What is Aziz doing?", "He is flying a kite."),
            ("Why does he like autumn?", "Because it is windy.")]),
        Unscramble("Put the words in the right order.", items=[
            "It's sunny today.", "What's the weather like?", "I like winter."])]),
]

SPEC = UnitSpec(number=8, slug="unit-8-weather-seasons", title="Weather and seasons", info=INFO, vocab=VOCAB,
                extra_vocab=EXTRA, lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="Weather and seasons", sheet_b_name="Weather talk, opinions, reading, writing",
                card=CARD, card_name="Word card", intro_note=NOTE)
