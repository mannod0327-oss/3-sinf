"""Round-Up 3 · mini-unit 4 — articles a / an / the (Round-Up Unit 4)."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, OddOne, PicLabel, Reading, Section, TrueFalse, Unscramble, WordSearch,
    WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.model import Box, Heading, Para, Table
from sinf.unit import UnitSpec, V

from .common import BADGE, GRADE_TIP_20

VOCAB = [
    V("apple", "olma", "apple"), V("orange", "apelsin", "orange"), V("egg", "tuxum", "egg"),
    V("elephant", "fil", "elephant"), V("umbrella", "soyabon", "umbrella"), V("ice cream", "muzqaymoq", "ice cream"),
    V("ant", "chumoli", "ant"), V("banana", "banan", "banana"), V("dog", "it", "dog"), V("book", "kitob", "book"),
]
EXTRA = [V("the sun", "quyosh", "sun"), V("the moon", "oy", "moon"), V("the sea", "dengiz", "sea"),
         V("the teacher", "o'qituvchi", "teacher")]

INFO = UnitInfo(
    number=4, title="Articles: a, an, the", topic="Which little word? a / an / the / nothing",
    book="Round-Up 3, Unit 4 — Articles",
    vocabulary="apple, orange, egg, elephant, umbrella, ice cream, ant, banana, dog, book (+ the sun, the moon)",
    grammar=["a before a consonant sound (a dog), an before a vowel sound (an egg)",
             "the for a thing we both know, or only one (the sun)",
             "no article with plural things in general (I like dogs) and with names"],
)

CARD = [
    Heading("a · an · the · —", 1),
    Table([["a", "an", "the", "— (nothing)"],
           ["a dog · a banana · a book", "an egg · an apple · an umbrella", "the sun · the teacher · the dog (we know it)",
            "I like dogs. · Aziz is here."],
           ["consonant **sound**", "vowel **sound** (a, e, i, o, u)", "one special thing", "many things in general; names"]],
          widths=[0.2, 0.25, 0.3, 0.25], header=True, style="grid", size=10.5),
    Box([Para("I have **a** dog. **The** dog is brown. (first time: a → next time: the)"),
         Para("an hour (we say 'our') · a university (we say 'you')")], kind="grammar", title="First time → second time"),
    Box([Para("O'zbek tilida a / an / the yo'q: 'Men mushuk ko'rdim' = 'I saw **a** cat'. Sanalgan yakka narsa oldida "
              "a / an qo'ying; tanish narsa oldida the.")], kind="tip", title="Eslatma"),
]

LESSONS = [
    Lesson.std(
        title="a or an?",
        focus="a / an with one thing",
        aims=["use a before consonant sounds and an before vowel sounds", "say: an apple, a banana"],
        language=["a dog · a banana · a book · an apple · an egg · an elephant · an umbrella"],
        materials=["Flashcards (games/flashcards.pdf)", "Two boxes labelled a and an", "Grammar card"],
        greeting="Hold up a flashcard: 'What's this? It's an apple.' Write 'an apple' on the board.",
        warmup="**a or an?** Pupils stand for 'an' and sit for 'a' as you say the word.",
        present="Sort the flashcards into two boxes (a / an). Underline the first sound and say it: /æ/, /e/, /ɪ/, /ɒ/, /ʌ/ → "
                "vowel sounds → an.",
        practice="Worksheet A exercises A (label with articles), C (circle) and D (word search). Pairs sort the flashcards.",
        produce="**Shopping list**: pupils write five things they want to buy with the correct article and read it out.",
        wrap="Quick-fire: teacher says a word, pupils say 'a …' or 'an …'. Homework.",
        homework="Write ten nouns with a / an (five from your room, five from your bag).",
        assessment="Listen for a / an in the shopping list activity.",
        tips=["O'zbek tilida artikl yo'q — **'I have cat'** xatosi juda keng tarqalgan. Har bir yakka ot oldida "
              "a / an tekshiring.",
              "Qoida harfga emas, **tovushga** bog'liq: an hour /aʊə/, a university /juː/.",
              "Support: sorting cards only. Extension: add adjectives (an old umbrella)."],
    ),
    Lesson.std(
        title="the",
        focus="the: something we know, the second time, or only one",
        aims=["use the for something already mentioned or unique", "tell a mini-story: I have a dog. The dog is brown."],
        language=["I have a dog. The dog is brown.", "the sun · the moon · the sea · the teacher"],
        materials=["Picture cards", "Worksheet A exercise E; Worksheet B exercises A, B"],
        greeting="Say 'I have a pet. The pet is a cat.' and ask pupils 'What's my pet?'",
        warmup="**Story chain**: pupil A says 'I have a cat.' Pupil B says 'The cat is black.' and adds 'I have a …' for C.",
        present="Show the rule with two sentences: first mention = a / an, second mention = the. Add things that are "
                "unique (the sun, the moon).",
        practice="Worksheet A exercise E (write the) and Worksheet B exercises A and B.",
        produce="**Two-sentence stories**: pairs write and tell a short story with 'a' first and 'the' second.",
        wrap="Volunteers read their story; class checks a / the. Homework.",
        homework="Write a four-sentence story about an animal using a and the.",
        assessment="Check a → the in the stories.",
        tips=["'the' tanish narsa: suhbatdosh nimani nazarda tutganimni biladi. O'zbekchada buni 'o'sha' bilan ifodalash mumkin.",
              "'the' talaffuzi: undosh oldida /ðə/, unli oldida /ði/ — hozircha faqat /ðə/.",
              "Support: give sentence starters. Extension: add adjectives."],
    ),
    Lesson.std(
        title="a, an, the or nothing?",
        focus="Choose the right article (or none)",
        aims=["choose a, an, the or no article in short texts", "use no article with plurals in general and names"],
        language=["I like dogs. · Aziz is my friend. · We have lunch at one."],
        materials=["Article cards (a, an, the, —)", "Worksheet B exercises C–E"],
        greeting="Write 'I like ___ ice cream. / I have ___ apple.' on the board and ask which word fits.",
        warmup="**Article cards**: pupils hold up a / an / the / — cards for gaps you read aloud.",
        present="Sum up on the board with four examples (one per column of the grammar card). Explain that plural general "
                "nouns and names take no article.",
        practice="Worksheet B exercises C (unscramble), D (reading) and E (writing).",
        produce="**Article auction**: teams 'buy' correct sentences with play money; wrong sentences lose money.",
        wrap="Teacher reads three sentences; pupils hold up the right article card. Homework.",
        homework="Correct five sentences with article mistakes (on your worksheet).",
        assessment="Mark Worksheet B exercise E for articles.",
        tips=["'I like the dogs' (hamma itlarni emas, umuman) — xato; umumiy fikrda artikl ishlatilmaydi.",
              "'We have lunch at one' — ovqat nomlari oldida artikl yo'q.",
              "Support: articles in a table. Extension: write a riddle using a / the."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "G", "T-Ss"),
    ),
]

A = [
    PicLabel("Look and write a or an + the word.", items=[
        ("apple", "an apple"), ("orange", "an orange"), ("egg", "an egg"), ("elephant", "an elephant"),
        ("umbrella", "an umbrella"), ("banana", "a banana"), ("dog", "a dog"), ("book", "a book")], cols=4),
    OddOne("Circle the word that needs 'a', not 'an'.", rows=[
        (["apple", "egg", "dog", "orange"], "dog"), (["ice cream", "umbrella", "banana", "ant"], "banana"),
        (["elephant", "book", "egg", "apple"], "book")]),
    Circle("Circle a or an.", items=[
        "I've got {a|*an} apple.", "He has {*a|an} dog.", "It's {a|*an} umbrella.", "She eats {a|*an} egg.",
        "This is {*a|an} book.", "I see {a|*an} elephant."]),
    WordSearch("Find eight words.", words=["apple", "orange", "egg", "elephant", "umbrella", "banana", "dog", "book"],
               size=10, seed=24),
    Fill("Write the, a or an.", items=[
        "{The} sun is hot today.", "I've got {a} dog. {The} dog is brown.", "{The} moon is in the sky.",
        "She has {an} apple. {The} apple is red."], bank=True),
    Draw("Draw an elephant, a banana and an umbrella. Write the words with a / an.", prompts=["Articles picture"]),
]

B = [
    Circle("Circle a, an or the.", items=[
        "I've got {*a|an|the} cat.", "She eats {a|*an|the} orange every day.", "{*The|A|An} sun is hot.",
        "I like {a|the|*–} dogs.", "Aziz has {a|*an|the} umbrella. {*The|A|An} umbrella is blue."]),
    Fill("Write a, an, the or – (nothing).", items=[
        "I have {a} pet. {The} pet is a rabbit.", "We have {–} lunch at one o'clock.", "{–} Malika is my friend.",
        "Look at {the} moon!", "He has {an} egg."], bank=True),
    Unscramble("Put the words in the right order.", items=[
        "I have a dog.", "She has an orange.", "The sun is hot.", "We like ice cream."]),
    Reading("Read and answer.", title="A pet story", text=(
        "Malika has a cat and a dog. The cat is black and the dog is brown. The dog likes an old ball.\n\n"
        "In the morning the cat sleeps. The dog plays with the ball. Malika loves her pets."), questions=[
        ("What pets has Malika got?", "A cat and a dog."), ("What colour is the dog?", "It is brown."),
        ("What does the dog like?", "An old ball.")]),
    WriteAbout("Write about a pet (real or imaginary) with a, an and the.", frames=[
        "I have a ___ .", "The ___ is ___ .", "It likes ___ ."], lines=3,
        model=["I have a rabbit. The rabbit is white. It likes carrots."]),
]

QUIZ = [
    Section("Part 1 · a or an", [
        PicLabel("Look and write a or an + the word.", items=[
            ("apple", "an apple"), ("banana", "a banana"), ("egg", "an egg"), ("dog", "a dog"),
            ("umbrella", "an umbrella"), ("book", "a book")], bank=False, cols=3, size=34)]),
    Section("Part 2 · Grammar", [
        Circle("Circle the correct word.", items=[
            "I've got {*an|a} orange.", "{*The|A} moon is in the sky.", "We like {*–|the} cats.",
            "She has {*a|an} ruler."]),
        Fill("Write a, an or the.", items=[
            "He has {an} elephant toy.", "I have {a} cat. {The} cat is white.", "{The} sun is yellow."],
            extra_words=["–"])]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="Sardor's pet", text=(
            "Sardor has a parrot. The parrot is green. It eats an apple every day."), questions=[
            ("What has Sardor got?", "A parrot."), ("What colour is the parrot?", "It is green."),
            ("What does it eat every day?", "An apple.")]),
        Unscramble("Put the words in the right order.", items=[
            "She has an egg.", "The dog is big.", "I like dogs."])]),
]

SPEC = UnitSpec(number=4, slug="unit-4-articles", title="Articles: a, an, the", info=INFO, vocab=VOCAB,
                extra_vocab=EXTRA, lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="a / an / the — forms", sheet_b_name="Articles in sentences, reading, writing",
                card=CARD,
                intro_note="Adapted for Grade 3 (age 8–9, CEFR A1): the ideas come from the Round-Up 3 unit; all "
                           "exercises and texts are new.")
