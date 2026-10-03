"""Destination A1 · mini-unit 6 — school life (Destination Unit 9, vocabulary)."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, OddOne, PicLabel, Reading, Section, Unscramble, WordSearch, WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.unit import UnitSpec, V, picture_card

from .common import BADGE, NOTE

VOCAB = [
    V("Maths", "matematika", "maths"), V("English", "ingliz tili", "abc"), V("Science", "tabiiy fan", "science room"),
    V("Art", "tasviriy san'at", "paint"), V("Music", "musiqa", "music room"), V("PE", "jismoniy tarbiya", "run"),
    V("Geography", "geografiya", "globe"), V("teacher", "o'qituvchi", "teacher"), V("pupil", "o'quvchi", "student"),
    V("homework", "uy vazifasi", "homework"),
]
EXTRA = [V("easy", "oson", None), V("difficult", "qiyin", None), V("fun", "qiziqarli", None),
         V("boring", "zerikarli", None), V("favourite", "sevimli", None), V("because", "chunki", None)]

INFO = UnitInfo(
    number=6, title="School life", topic="School subjects, the timetable and what I think about them",
    book="Destination A1, Unit 9 — Vocabulary: School life",
    vocabulary="Maths, English, Science, Art, Music, PE, Geography, teacher, pupil, homework",
    grammar=["We have Maths on Monday. · The teacher gives us homework.",
             "What's your favourite subject? — My favourite subject is Art.",
             "I like Art because it's fun. · Maths is difficult."],
)

CARD = picture_card(VOCAB, "School life", cols=5,
                    tip="**We have Maths on Monday** (have — 'bizda … bor'). **because** = chunki: I like Art **because** it's fun.")

LESSONS = [
    Lesson.std(
        title="School subjects",
        focus="Vocabulary — subjects, teacher, pupil, homework",
        aims=["name seven school subjects and three school words", "say what you do in each subject"],
        language=["Maths, English, Science, Art, Music, PE, Geography, teacher, pupil, homework"],
        materials=["Flashcards (games/flashcards.pdf)", "Word card (grammar-card.pdf)", "Worksheet A exercises A–C"],
        greeting="Ask 'What subjects do you have at school?' and write the answers on the board.",
        warmup="**Mime the lesson**: pupils mime a subject (painting, singing, running); the class says 'Art! Music! PE!'",
        present="Present the flashcards with an action each (Maths = count on fingers, Art = draw). Choral repetition.",
        practice="Worksheet A exercises A (label), B (match), C (complete the words).",
        produce="**What do you do in …?** Pairs ask 'What do you do in Music?' — 'We sing.'",
        wrap="Teacher says an action; pupils say the subject. Homework.",
        homework="Learn the words; write your timetable in English (Worksheet A exercise F).",
        assessment="Point at cards for 5 pupils; note gaps.",
        tips=["Fanlar nomi bosh harf bilan yoziladi (Maths, English, Art). 'PE' = 'physical education'.",
              "'Science' o'zbek maktabida 'tabiiy fan' (3–4-sinf) — o'sha fan.",
              "Support: pictures only. Extension: add 'History' and 'IT'."],
    ),
    Lesson.std(
        title="Our timetable",
        focus="We have … on …; the teacher gives us …",
        aims=["talk about the timetable: We have Maths on Monday.", "ask and answer: What do you have on Tuesday?"],
        language=["We have Maths on Monday. · What do you have on Tuesday? — We have Science and Art."],
        materials=["Class timetable", "Worksheet B exercises A–C"],
        greeting="Show the class timetable: 'What do we have today?'",
        warmup="**Timetable bingo**: pupils write five day–subject pairs and cross them out when called.",
        present="Write 'We have + subject + on + day' and the question with an example from the timetable.",
        practice="Worksheet B exercises A (circle), B (fill in) and C (unscramble).",
        produce="**Timetable interview**: pairs compare timetables: 'What do you have on Friday?' — 'We have PE.'",
        wrap="Teacher names a day; pupils say the subjects. Homework.",
        homework="Write four sentences about your timetable.",
        assessment="Check have / has and on + day.",
        tips=["'We have Maths' — o'zbekchada 'bizda matematika bor'. 'have' dan keyin 'got' shart emas (Destination'da 'have').",
              "Kun oldidagi predlog: on Monday; kun qismi: in the morning."],
    ),
    Lesson.std(
        title="I like it because…",
        focus="Opinions: favourite subject, easy / difficult / fun / boring, because",
        aims=["say their favourite subject and give a reason", "write 4–5 sentences about school"],
        language=["My favourite subject is Art. · I like Art because it's fun. · Maths is difficult, but I like it."],
        materials=["Opinion cards (easy, difficult, fun, boring)", "Worksheet B exercises D–E"],
        greeting="Ask 'What's your favourite subject?' and make a class chart.",
        warmup="**Opinion line**: pupils stand on a line from 'boring' to 'fun' for each subject.",
        present="Model: 'I like English because it's fun.' Write because on the board with the four opinion words.",
        practice="Worksheet B exercises D (reading) and E (writing).",
        produce="**Class survey poster**: groups ask classmates and make a chart: 'Art is our favourite subject.'",
        wrap="Report the survey results. Homework.",
        homework="Write why you like one subject and don't like another.",
        assessment="Mark Worksheet B exercise E for because and opinion words.",
        tips=["'because' = chunki; gap ikkiga bo'linadi: I like Art **because** it's fun (nuqta qo'ymang).",
              "'boring' (zerikarli) va 'bored' (zerikkan) ni aralashtirmang — hozircha faqat 'boring'.",
              "Support: opinion cards. Extension: compare two subjects."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "G", "T-Ss"),
    ),
]

A = [
    PicLabel("Look and write the words.", items=[
        ("maths", "Maths"), ("abc", "English"), ("science room", "Science"), ("paint", "Art"), ("music room", "Music"),
        ("run", "PE"), ("globe", "Geography"), ("homework", "homework")], cols=4),
    Match("Match the subject to what you do.", pairs=[
        ("You paint.", "Art"), ("You sing.", "Music"), ("You run and jump.", "PE"), ("You count.", "Maths"),
        ("You learn about countries.", "Geography"), ("You learn about plants and animals.", "Science")], seed=531),
    Gaps("Look and complete the words.", items=[
        ("science room", "science"), ("globe", "geography"), ("teacher", "teacher"), ("student", "pupil"),
        ("homework", "homework"), ("abc", "english")]),
    WordSearch("Find eight words.", words=["maths", "english", "science", "art", "music", "geography", "teacher",
                                           "pupil"], size=10, seed=36),
    OddOne("Circle the odd one out.", rows=[
        (["Maths", "Art", "Music", "teacher"], "teacher"), (["Art", "Music", "PE", "Monday"], "Monday"),
        (["easy", "difficult", "fun", "Music"], "Music")]),
    Draw("Draw your favourite subject. Write: My favourite subject is ___ .", prompts=["My favourite subject"]),
]

B = [
    Circle("Choose the correct word (A, B or C).", items=[
        "We {*have|has|having} Maths on Monday.", "My favourite subject {*is|are|am} Music.",
        "I like English {*because|and|but} it's fun.", "Our teacher {*gives|give|giving} us homework.",
        "PE {*isn't|aren't|don't} boring.", "What {*do|does|are} you have on Tuesday?"]),
    Fill("Complete the sentences with words from the box.", items=[
        "{What's} your favourite subject?", "My favourite subject {is} Art.", "I like Music {because} it's fun.",
        "We {have} English on Wednesday."], bank=True, extra_words=["are"]),
    Unscramble("Put the words in the right order.", items=[
        "We have Maths on Monday.", "What is your favourite subject?", "I like Art because it's fun.",
        "The teacher gives us homework."]),
    Reading("Read and answer.", title="My school week", text=(
        "I'm in Class 3. We have Maths and English on Monday. On Tuesday we have Science and Art.\n\n"
        "My favourite subject is Art because it is fun. Maths is difficult, but I like it. Our teacher, Mrs Karimova, "
        "gives us homework on Fridays."), questions=[
        ("What do they have on Tuesday?", "Science and Art."), ("What is the writer's favourite subject?", "Art."),
        ("When does the teacher give homework?", "On Fridays.")]),
    WriteAbout("Write about your favourite subject.", frames=[
        "My favourite subject is ___ .", "I like it because ___ .", "We have it on ___ .", "I don't like ___ ."],
        lines=4,
        model=["My favourite subject is English. I like it because it is fun. We have it on Monday and Wednesday. "
               "I don't like Geography."]),
]

QUIZ = [
    Section("Part 1 · Words", [
        PicLabel("Look and write the words.", items=[
            ("maths", "Maths"), ("paint", "Art"), ("music room", "Music"), ("run", "PE"), ("globe", "Geography"),
            ("homework", "homework")], bank=False, cols=3, size=34)]),
    Section("Part 2 · Grammar", [
        Circle("Choose the correct word.", items=[
            "We {*have|has} Art on Friday.", "I like PE {*because|and} it's fun.", "My favourite subject {*is|are} Maths.",
            "What {*do|does} you have on Monday?"]),
        Fill("Complete the sentences.", items=[
            "{What's} your favourite subject?", "We {have} Music on Tuesday.", "Maths is {difficult}, but I like it.",
            "I like English {because} it is fun."], extra_words=["easy", "has"])]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="Sardor's Monday", text=(
            "On Monday we have Maths, English and PE. My favourite subject is PE because it is fun. "
            "I don't like Maths. It is difficult."), questions=[
            ("What do they have on Monday?", "Maths, English and PE."), ("What is Sardor's favourite subject?", "PE."),
            ("Why doesn't he like Maths?", "Because it is difficult.")]),
        Unscramble("Put the words in the right order.", items=[
            "We have PE on Monday.", "What is your favourite subject?", "I like Art."])]),
]

SPEC = UnitSpec(number=6, slug="unit-6-school-life", title="School life", info=INFO, vocab=VOCAB, extra_vocab=EXTRA,
                lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="Subjects and school words", sheet_b_name="Timetable, opinions, reading, writing",
                card=CARD, card_name="Word card", intro_note=NOTE)
