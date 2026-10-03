"""Destination A1 · mini-unit 2 — present simple with jobs (Destination Units 2 and 4)."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, OddOne, PicLabel, Reading, Section, Unscramble, WordSearch, WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.model import Box, Heading, Para, Table
from sinf.unit import UnitSpec, V

from .common import BADGE, NOTE

VOCAB = [
    V("teacher", "o'qituvchi", "teacher"), V("doctor", "shifokor", "doctor"), V("cook", "oshpaz", "cook"),
    V("farmer", "dehqon", "farmer"), V("pilot", "uchuvchi", "pilot"), V("singer", "qo'shiqchi", "singer"),
    V("artist", "rassom", "artist"), V("firefighter", "o't o'chiruvchi", "firefighter"),
    V("police officer", "politsiyachi", "police"), V("mechanic", "mexanik", "mechanic"),
]
EXTRA = [
    V("teaches", "o'rgatadi", None), V("helps", "yordam beradi", None), V("cooks", "pishiradi", None),
    V("grows", "yetishtiradi", None), V("flies", "uchadi, boshqaradi", None), V("sings", "kuylaydi", None),
    V("paints", "rasm chizadi", None), V("repairs", "ta'mirlaydi", None),
]

INFO = UnitInfo(
    number=2, title="Present simple: jobs", topic="People and what they do",
    book="Destination A1, Units 2 and 4 — Present simple 1 and 2",
    vocabulary="teacher, doctor, cook, farmer, pilot, singer, artist, firefighter, police officer, mechanic",
    grammar=["he / she / it + verb-s: A teacher teaches children.",
             "I / you / we / they + verb: Pilots fly planes.",
             "doesn't / don't + verb; Do / Does + subject + verb?"],
)

CARD = [
    Heading("Present simple — what do they do?", 1),
    Table([["+", "−", "?"],
           ["A teacher **teaches** children.\nPilots **fly** planes.", "A doctor **doesn't cook**.\nFarmers **don't fly** planes.",
            "**Does** a cook **make** food? Yes, he **does**.\n**Do** pilots **fly** planes? Yes, they **do**."]],
          widths=[0.33, 0.33, 0.34], header=True, style="grid", size=10.5),
    Table([["+ s", "+ es", "y → ies"], ["cook → cooks\nsing → sings\npaint → paints", "teach → teaches\nfix → fixes\n"
                                          "go → goes", "study → studies\nfly → flies\ncarry → carries"]],
          widths=[0.3, 0.35, 0.35], header=True, style="grid", size=10.5),
    Box([Para("**he / she / it** → verb + **s**. A teacher **teach**s, a pilot **fl**ies. After **doesn't / does** the verb "
              "has no -s: A cook **doesn't** make**s** … ✗ — A cook **doesn't make** …")], kind="grammar", title="Watch out"),
    Box([Para("'U o'qiydi' (u = he/she) — inglizchada **teaches**. Fe'lga -s qo'shishni unutmang: 'He teach' — xato.")],
        kind="tip", title="Eslatma"),
]

LESSONS = [
    Lesson.std(
        title="Jobs",
        focus="Vocabulary — ten jobs and what they do",
        aims=["name ten jobs", "say what people do: A pilot flies planes."],
        language=["teacher, doctor, cook, farmer, pilot, singer, artist, firefighter, police officer, mechanic",
                  "A teacher teaches. · A doctor helps people."],
        materials=["Flashcards (games/flashcards.pdf)", "Word card (grammar-card.pdf)", "Worksheet A exercises A–B"],
        greeting="Ask 'What do your parents do?' and collect jobs in Uzbek and English.",
        warmup="**Mime the job**: pupils mime a job; the class guesses in English.",
        present="Present the ten job flashcards with a typical action for each and a short sentence ('A cook makes food.').",
        practice="Worksheet A exercises A (label) and B (match job and action). Play **What's missing?**",
        produce="**Who am I?** Pairs: one pupil says 'I fly planes. Who am I?' The partner answers 'You are a pilot.'",
        wrap="Teacher says an action; pupils say the job. Homework.",
        homework="Learn the jobs; ask two adults about their jobs and write them in English.",
        assessment="Flash cards at random for 5 pupils; note gaps.",
        tips=["Kasblar oldidan 'a' / 'an' qo'yiladi: a teacher, an artist — ikkalasini mashq qiling.",
              "'police officer' — ikki so'z; 'police' ko'plik sifatida ishlatiladi ('The police are here').",
              "Support: match jobs with pictures only. Extension: add 'at work' places (school, hospital)."],
    ),
    Lesson.std(
        title="He teaches, she cooks",
        focus="Present simple: he / she + verb-s; I / you / we / they + verb",
        aims=["use the third-person -s / -es / -ies", "contrast: Pilots fly. A pilot flies."],
        language=["A teacher teaches children. · Pilots fly planes.", "flies · goes · does · studies"],
        materials=["Flashcards", "Worksheet A exercises C–E; Worksheet B exercise A"],
        greeting="Say 'A teacher teaches' on the board and underline -es.",
        warmup="**Verb race**: two teams write the third-person form of a verb on the board.",
        present="Write two columns: I / you / we / they (base verb) and he / she / it (+ s, + es, + ies). Sort ten verbs.",
        practice="Worksheet A exercises C (complete), D (odd one out) and E (word search); Worksheet B exercise A.",
        produce="**Job riddles**: pupils write two sentences about a job ('He helps sick people. He works in a hospital.') and read "
                "them for the class to guess.",
        wrap="Quick-fire: teacher says 'pilot — fly'; pupils say 'A pilot flies planes.' Homework.",
        homework="Write five sentences about jobs in your family (he / she + verb-s).",
        assessment="Check for missing -s in the riddles.",
        tips=["Uchinchi shaxs -s — o'zbekchada yo'q. Doskada qizil bilan yozing va har gapdan keyin tekshiring.",
              "'flies', 'studies': y → ies qoidasini jadval bilan ko'rsating.",
              "Support: give the -s ending on cards. Extension: add adverbs (always, usually)."],
    ),
    Lesson.std(
        title="Does a cook fly planes?",
        focus="Present simple: negatives, questions and short answers",
        aims=["say what people don't do: A doctor doesn't cook.", "ask and answer: Does a pilot fly planes? Yes, he does."],
        language=["A doctor doesn't cook. · Farmers don't fly planes.", "Does a cook make food? — Yes, he does. / Do pilots fly? — Yes, they do."],
        materials=["Job cards", "Worksheet B exercises A–E"],
        greeting="Ask 'Does a teacher cook food?' — pupils answer 'No, he doesn't.'",
        warmup="**True or false?** Read sentences about jobs; pupils stand for true and sit for false.",
        present="Write the negative and question patterns on the board; underline that the verb has no -s after doesn't / does.",
        practice="Worksheet B exercises B (fill in), C (unscramble) and D (reading).",
        produce="**Guess the job**: a pupil chooses a job card; the class asks 'Does he fly planes?' (only yes / no) until they "
                "guess.",
        wrap="Teacher reads three sentences; pupils correct the wrong one. Homework.",
        homework="Write four questions about jobs and their answers.",
        assessment="Listen for Do / Does and the bare verb.",
        tips=["'Does he teaches?' — xato. 'Does' dan keyin fe'l asl holda: 'Does he teach?'.",
              "Qisqa javob: Yes, he **does**. / No, he **doesn't**."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "Ss-Ss", "T-Ss"),
    ),
]

A = [
    PicLabel("Look and write the jobs.", items=[
        ("teacher", "teacher"), ("doctor", "doctor"), ("cook", "cook"), ("farmer", "farmer"), ("pilot", "pilot"),
        ("singer", "singer"), ("artist", "artist"), ("firefighter", "firefighter")], cols=4),
    Match("Match the job to what the person does.", pairs=[
        ("A teacher", "teaches children."), ("A doctor", "helps sick people."), ("A cook", "makes food."),
        ("A farmer", "grows vegetables."), ("A pilot", "flies planes."), ("A singer", "sings songs.")], seed=401),
    Fill("Write the correct form of the verb.", items=[
        "A teacher {teaches} (teach) children.", "A cook {cooks} (cook) plov.", "A pilot {flies} (fly) a plane.",
        "An artist {paints} (paint) pictures.", "A mechanic {fixes} (fix) cars."], bank=False),
    OddOne("Circle the odd one out.", rows=[
        (["teacher", "doctor", "pilot", "banana"], "banana"), (["cook", "farmer", "singer", "chair"], "chair"),
        (["artist", "mechanic", "firefighter", "window"], "window")]),
    WordSearch("Find eight jobs.", words=["teacher", "doctor", "cook", "farmer", "pilot", "singer", "artist",
                                          "mechanic"], size=10, seed=32),
    Draw("Draw a job you like. Write: A ___ ___s ___ .", prompts=["My job"]),
]

B = [
    Circle("Choose the correct word (A, B or C).", items=[
        "A doctor {*helps|help|helping} sick people.", "Pilots {*fly|flies|flying} planes.",
        "My mum {*cooks|cook|cooking} plov.", "A teacher {teach|*teaches|teachs} children.",
        "Singers {*sing|sings|singing} songs.", "A farmer {grow|growes|*grows} vegetables."]),
    Fill("Complete with doesn't, don't, does or do.", items=[
        "A doctor {doesn't} cook food.", "Farmers {don't} fly planes.", "{Does} a cook make food? — Yes, he does.",
        "{Do} pilots fly planes? — Yes, they do."], bank=True),
    Unscramble("Put the words in the right order.", items=[
        "A teacher teaches children.", "Pilots fly planes.", "Does a doctor cook?", "A cook doesn't fly planes."]),
    Reading("Read and answer.", title="Who am I?", text=(
        "1. I work in a school. I teach children English and Maths. I don't work at night. Who am I?\n\n"
        "2. I work in a kitchen. I make plov and soup. I don't fly planes. Who am I?"), questions=[
        ("Who works in a school?", "A teacher."), ("Who makes plov?", "A cook."),
        ("Does the cook fly planes?", "No, he doesn't.")]),
    WriteAbout("Write about a job in your family.", frames=[
        "My ___ is a ___ .", "He / She ___s ___ .", "He / She doesn't ___ ."], lines=3,
        model=["My uncle is a driver. He drives a bus. He doesn't fly planes."]),
]

QUIZ = [
    Section("Part 1 · Jobs", [
        PicLabel("Look and write the jobs.", items=[
            ("teacher", "teacher"), ("doctor", "doctor"), ("pilot", "pilot"), ("singer", "singer"),
            ("artist", "artist"), ("farmer", "farmer")], bank=False, cols=3, size=34)]),
    Section("Part 2 · Grammar", [
        Circle("Choose the correct word.", items=[
            "A cook {*makes|make} food.", "Pilots {*fly|flies} planes.", "{*Does|Do} a doctor help sick people?",
            "A farmer {*doesn't|don't} fly planes."]),
        Fill("Write the correct form of the verb.", items=[
            "A teacher {teaches} (teach) English.", "An artist {paints} (paint) pictures.",
            "Doctors {help} (help) sick people.", "She {studies} (study) English."], bank=False)]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="My dad", text=(
            "My dad is a farmer. He grows tomatoes and apples. He doesn't work in an office. "
            "He gets up at five o'clock."), questions=[
            ("What is his job?", "He is a farmer."), ("What does he grow?", "Tomatoes and apples."),
            ("Does he work in an office?", "No, he doesn't.")]),
        Unscramble("Put the words in the right order.", items=[
            "She teaches children.", "Does he fly planes?", "Cooks don't sing."])]),
]

SPEC = UnitSpec(number=2, slug="unit-2-present-simple-jobs", title="Present simple: jobs", info=INFO, vocab=VOCAB,
                extra_vocab=EXTRA, lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="Jobs and verbs", sheet_b_name="Present simple: sentences, questions, reading",
                card=CARD, intro_note=NOTE)
