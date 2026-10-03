"""Destination A1 · mini-unit 5 — hobbies and pastimes (Destination Unit 6, vocabulary)."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, OddOne, PicLabel, Reading, Section, Unscramble, WordSearch, WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.unit import UnitSpec, V, picture_card

from .common import BADGE, NOTE

VOCAB = [
    V("play chess", "shaxmat o'ynamoq", "chess"), V("play football", "futbol o'ynamoq", "football"),
    V("go cycling", "velosipedda sayr qilmoq", "cycling"), V("go swimming", "suzishga bormoq", "swimming"),
    V("read books", "kitob o'qimoq", "read"), V("draw pictures", "rasm chizmoq", "paint"),
    V("dance", "raqsga tushmoq", "dance"), V("sing", "qo'shiq aytmoq", "sing"),
    V("play computer games", "kompyuter o'yinlarini o'ynamoq", "play computer"),
    V("go fishing", "baliq ovlashga bormoq", "fishing"),
]
EXTRA = [V("like", "yoqtirmoq", "thumbs up"), V("love", "juda yaxshi ko'rmoq", "heart"),
         V("enjoy", "zavqlanmoq", "happy"), V("hate", "yomon ko'rmoq", "angry")]

INFO = UnitInfo(
    number=5, title="Hobbies and pastimes", topic="What I like doing in my free time",
    book="Destination A1, Unit 6 — Vocabulary: Hobbies and pastimes",
    vocabulary="play chess, play football, go cycling, go swimming, read books, draw pictures, dance, sing, "
               "play computer games, go fishing",
    grammar=["like / love / enjoy / hate + verb-ing: I like dancing.",
             "play + game, go + -ing activity, read / draw / sing: collocations",
             "What do you like doing? · Do you like reading? — Yes, I do."],
)

CARD = picture_card(VOCAB, "Hobbies and pastimes", cols=5,
                    tip="**play** + o'yin (chess, football) · **go** + -ing (go swimming) · hobby + **-ing**: I like **swimming**.")

LESSONS = [
    Lesson.std(
        title="My free time",
        focus="Vocabulary — ten hobbies; play / go collocations",
        aims=["name ten hobbies", "use play, go and other verbs with the right hobby"],
        language=["play chess / football / computer games · go cycling / swimming / fishing · read books · draw pictures · dance · sing"],
        materials=["Flashcards (games/flashcards.pdf)", "Word card (grammar-card.pdf)", "Worksheet A exercises A, B, E"],
        greeting="Ask 'What do you do in your free time?' and write answers in two columns (play / go).",
        warmup="**Charades**: pupils mime hobbies; the class guesses 'You play chess!'",
        present="Present the ten flashcards with actions. Group them by verb: **play** (chess, football, computer games), **go** "
                "(cycling, swimming, fishing), others.",
        practice="Worksheet A exercises A (label), B (match with Uzbek) and C (play / go / – circle).",
        produce="**Hobby bingo**: pupils write five hobbies on a grid; the teacher mimes, pupils cross out.",
        wrap="Teacher says the hobby; pupils say the full phrase. Homework.",
        homework="Learn the ten phrases and draw your favourite hobby (Worksheet A exercise F).",
        assessment="Check that pupils use play / go correctly.",
        tips=["'play chess' (o'ynamoq) lekin 'go swimming' (-ga bormoq): fe'l hobbyga bog'liq — jadval qiling.",
              "'draw pictures', 'read books' — fe'l o'zi yetarli (play / go yo'q).",
              "Support: pictures only. Extension: add 'play the guitar', 'do karate'."],
    ),
    Lesson.std(
        title="I like dancing",
        focus="like / love / enjoy / hate + -ing",
        aims=["say what they like and don't like doing: I like dancing. I don't like fishing.",
              "ask and answer: Do you like swimming? — Yes, I do."],
        language=["I like / love / enjoy / hate + -ing", "Do you like …ing? — Yes, I do. / No, I don't."],
        materials=["Hobby flashcards", "Emotion cards (like, love, enjoy, hate)", "Worksheet B exercises A–C"],
        greeting="Ask 'Do you like swimming?' — thumbs up or down.",
        warmup="**Like line**: pupils stand on a line from 'hate' to 'love' for each hobby you call.",
        present="Write the pattern: I like / love / enjoy / hate + verb-ing. Show -ing endings (dance → dancing, swim → swimming). "
                "Show questions and short answers.",
        practice="Worksheet B exercises A (circle), B (fill in) and C (unscramble).",
        produce="**Class survey**: pupils ask three classmates 'What do you like doing?' and record answers in a table.",
        wrap="Report: 'Aziz likes playing chess. Malika loves dancing.' Homework.",
        homework="Write five sentences with like / love / enjoy / hate + -ing.",
        assessment="Check -ing after like and he / she + s in the reports.",
        tips=["'like' dan keyin fe'l + -ing: 'I like dance' — xato; 'I like dancing'.",
              "Report'da: He like**s** …: -s unutilmasin.",
              "Support: sentence frames. Extension: add reasons with 'because'."],
    ),
    Lesson.std(
        title="Hobby poster",
        focus="Describe my hobbies in writing and speaking",
        aims=["write 4–5 sentences about their hobbies", "present a hobby poster to the class"],
        language=["I love …ing. · I like …ing. · I don't like …ing. · I go … on Saturdays."],
        materials=["Paper, crayons", "Worksheet B exercises D–E"],
        greeting="Show an example poster ('My hobbies') with drawings and words.",
        warmup="**Guess my hobby**: you give three clues; pupils guess.",
        present="Read the model text (Worksheet B exercise D) and underline like / love / enjoy + -ing.",
        practice="Worksheet B exercises D (reading) and E (writing).",
        produce="**Hobby poster**: pupils draw their hobbies and write three sentences, then present them in groups.",
        wrap="Gallery walk: pupils tick a hobby they also like. Homework.",
        homework="Finish your poster and ask a family member about their hobbies.",
        assessment="Poster rubric: hobbies (1), sentences (1), neatness (1).",
        tips=["Taqdimot: har bir bola 2–3 gap aytsin; xatolarni darhol tuzatmang, oxirida umumiy fikr bildiring.",
              "Support: gapped text. Extension: compare two friends' hobbies."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "S / G", "G / T-Ss"),
    ),
]

A = [
    PicLabel("Look and write the hobbies.", items=[
        ("chess", "play chess"), ("football", "play football"), ("cycling", "go cycling"), ("swimming", "go swimming"),
        ("read", "read books"), ("paint", "draw pictures"), ("dance", "dance"), ("fishing", "go fishing")], cols=4),
    Match("Match the English phrase to the Uzbek phrase.", pairs=[
        ("play chess", "shaxmat o'ynamoq"), ("go swimming", "suzishga bormoq"), ("read books", "kitob o'qimoq"),
        ("go fishing", "baliq ovlashga bormoq"), ("draw pictures", "rasm chizmoq"), ("dance", "raqsga tushmoq")],
          seed=521),
    Circle("Choose play, go or – (nothing).", items=[
        "I {*play|go|–} chess.", "She {play|*goes|–} swimming.", "They {*play|go|–} football.",
        "He {play|*goes|–} fishing.", "We {*–|play|go} read books on Sundays.", "I {play|go|*–} draw pictures."]),
    Gaps("Look and complete the words.", items=[
        ("chess", "chess"), ("football", "football"), ("swimming", "swimming"), ("fishing", "fishing"),
        ("dance", "dance"), ("sing", "sing")]),
    WordSearch("Find eight hobby words.", words=["chess", "football", "swimming", "fishing", "dance", "sing", "read",
                                                 "draw"], size=10, seed=35),
    Draw("Draw your favourite hobby. Write: I love ___ing.", prompts=["I love ________ ing."]),
]

B = [
    Circle("Choose the correct word (A, B or C).", items=[
        "I like {*swimming|swim|swims}.", "She loves {dance|dances|*dancing}.", "They enjoy {*playing|play|plays} chess.",
        "He hates {*fishing|fish|fishes}.", "Do you like {*reading|read|reads}?", "She {*likes|like|liking} singing."]),
    Fill("Complete the sentences with the -ing form.", items=[
        "I like {swimming} (swim).", "She loves {dancing} (dance).", "He enjoys {reading} (read) books.",
        "They hate {running} (run) in the rain."], bank=False),
    Unscramble("Put the words in the right order.", items=[
        "I like swimming.", "Does she enjoy dancing?", "He doesn't like fishing.", "We love playing football."]),
    Reading("Read and answer.", title="My hobbies", text=(
        "My name is Bobur. I love playing football and I go swimming on Saturdays. I like reading books too.\n\n"
        "I don't like playing computer games. My sister Malika enjoys dancing and drawing pictures. "
        "She doesn't like fishing."), questions=[
        ("What does Bobur love?", "Playing football."), ("When does he go swimming?", "On Saturdays."),
        ("Does Malika like fishing?", "No, she doesn't.")]),
    WriteAbout("Write about your hobbies.", frames=[
        "I love ___ing.", "I like ___ing.", "I don't like ___ing.", "I go ___ on ___ ."], lines=4,
        model=["I love dancing. I like reading books. I don't like fishing. I go swimming on Saturdays."]),
]

QUIZ = [
    Section("Part 1 · Hobbies", [
        PicLabel("Look and write the hobbies.", items=[
            ("chess", "play chess"), ("football", "play football"), ("cycling", "go cycling"),
            ("swimming", "go swimming"), ("read", "read books"), ("dance", "dance")], bank=False, cols=3, size=34)]),
    Section("Part 2 · Grammar", [
        Circle("Choose the correct word.", items=[
            "I like {*swimming|swim}.", "She {*loves|love} dancing.", "Do you like {*reading|read}?",
            "We {*play|go} chess."]),
        Fill("Write the -ing form.", items=[
            "I like {dancing} (dance).", "He enjoys {swimming} (swim).", "They love {playing} (play) football.",
            "She hates {fishing} (fish)."], bank=False)]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="Dilnoza's hobbies", text=(
            "Dilnoza loves drawing pictures. She likes dancing too. She doesn't like playing computer games. "
            "On Sundays she goes cycling with her dad."), questions=[
            ("What does Dilnoza love?", "Drawing pictures."), ("Does she like computer games?", "No, she doesn't."),
            ("Who does she go cycling with?", "With her dad.")]),
        Unscramble("Put the words in the right order.", items=[
            "I love dancing.", "Do you like swimming?", "She doesn't like fishing."])]),
]

SPEC = UnitSpec(number=5, slug="unit-5-hobbies-pastimes", title="Hobbies and pastimes", info=INFO, vocab=VOCAB,
                extra_vocab=EXTRA, lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="Hobby words, play / go", sheet_b_name="like + -ing, reading, writing", card=CARD,
                card_name="Word card", intro_note=NOTE)
