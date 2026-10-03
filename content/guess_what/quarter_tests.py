"""Quarter tests (nazorat ishlari) for Guess What! Grade 3 — 40 points each, with listening scripts and keys."""
from __future__ import annotations

from pathlib import Path

from sinf.exercises import (
    Circle, Fill, NumberPics, OddOne, Order, PicLabel, Reading, Section, TrueFalse, Unscramble, WriteAbout,
    sheet, total_points,
)
from sinf.model import Box, Bullets, Doc, Heading, Para, Spacer, Table
from sinf.render_docx import render_docx
from sinf.render_pdf import render_pdf

from .common import BADGE

GRADE_TABLE = [
    ["Mark", "Level", "Points (of 40)", "Percent"],
    ["5", "a'lo (excellent)", "35 – 40", "86 – 100 %"],
    ["4", "yaxshi (good)", "29 – 34", "71 – 85 %"],
    ["3", "qoniqarli (satisfactory)", "22 – 28", "55 – 70 %"],
    ["2", "qoniqarsiz (unsatisfactory)", "0 – 21", "below 55 %"],
]

WRITING_RUBRIC = [
    ["Criterion", "2 points", "1 point", "0 points"],
    ["Content", "all 4–5 sentences answer the task", "2–3 sentences on task", "off-topic or one sentence"],
    ["Grammar", "structures from the unit are mostly correct", "some correct, some errors", "no correct structures"],
    ["Spelling & punctuation", "capital letters, full stops, words spelled correctly (0–2 slips)",
     "several slips but meaning is clear", "meaning is hard to follow"],
]


def _writing(instruction: str, frames: list[str], model: list[str]) -> WriteAbout:
    return WriteAbout(instruction, frames=frames, lines=5, model=model, marks=6)


QUARTERS = []

# ---------------------------------------------------------------- quarter 1 ----
QUARTERS.append(dict(
    n=1, slug="quarter-1-test", scope="Welcome · Unit 1 In the garden · Unit 2 At school",
    sections=[
        Section("Part 1 · Listening", [
            NumberPics("Listen and write the numbers 1–5 in the boxes.",
                       icons=["tree", "butterfly", "rabbit", "flower", "snail"], heard=[1, 4, 3, 2, 0],
                       script=["Number 1. — What's that? — It's a butterfly.",
                               "Number 2. — What's that? — It's a snail.",
                               "Number 3. — What's that? — It's a flower.",
                               "Number 4. — What's that? — It's a rabbit.",
                               "Number 5. — What's that? — It's a tree."]),
            TrueFalse("Listen and write T (true) or F (false).", items=[
                ("Anna is in the gym.", False), ("Tom and Max are on the sports field.", True),
                ("Lily is painting in the Art room.", True), ("Anna is reading a book.", True),
                ("Tom and Max are in the library.", False)],
                script=["Anna is in the library. She's reading a book.",
                        "Tom and Max are on the sports field. They're playing football.",
                        "Lily is in the Art room. She's painting a picture."])]),
        Section("Part 2 · Vocabulary", [
            PicLabel("Look and write the words.", items=[
                ("caterpillar", "caterpillar"), ("tortoise", "tortoise"), ("library", "library"),
                ("sports field", "sports field")], bank=False, cols=4, size=36),
            Fill("Write the missing month.", items=[
                "The month after May is {June}.", "The month before December is {November}.",
                "The month after July is {August}.", "The month before March is {February}."])]),
        Section("Part 3 · Grammar", [
            Circle("Circle the correct word.", items=[
                "Anna has a tortoise. {*Her|His} tortoise is old.",
                "We have a cat. {*Our|Their} cat is black.",
                "{What's|*What are} those? They're butterflies.",
                "The children are {in|*on} the playground.",
                "What are you {*doing|do}? — I'm reading."]),
            Fill("Complete the sentences.", items=[
                "{When's} your birthday? — It's in April.", "{What's} that? — It's a snail.",
                "Tom {is} painting in the Art room.", "They're {in} the library.",
                "{Can} I open the window, please? — Yes, you can."], extra_words=["Where's", "are"])]),
        Section("Part 4 · Reading", [
            Reading("Read and answer.", title="Lucas's school", text=(
                "This is Lucas. He's nine years old and he's from Tashkent. His birthday is in September.\n\n"
                "His school is big and clean. It's break time now. Lucas is on the playground. He's playing with his "
                "friends. Lily is in the library. She's reading a book."), questions=[
                ("When is Lucas's birthday?", "It's in September."),
                ("Where is Lucas?", "He's on the playground."),
                ("What is Lily doing?", "She's reading a book.")]),
            Unscramble("Put the words in the right order.", items=[
                "Where are they?", "Her pet is a snail.", "When's your birthday?"])]),
        Section("Part 5 · Writing", [
            _writing("Write 4–5 sentences about your school or your pet.", [
                "My school has a ___ and a ___ .", "My pet is a ___ . Its name is ___ .",
                "At break time I'm on the ___ ."],
                ["My school has a library and a gym. At break time I'm on the playground. My pet is a rabbit. "
                 "Its name is Snowy. It is white."])]),
    ]))

# ---------------------------------------------------------------- quarter 2 ----
QUARTERS.append(dict(
    n=2, slug="quarter-2-test", scope="Unit 3 School days · Unit 4 My day",
    sections=[
        Section("Part 1 · Listening", [
            Circle("Listen. Dilnoza talks about her day. Circle the times.", items=[
                "Get up: {*7:00|8:00}", "Go to school: {8:00|*8:30}", "Have lunch: {*12:00|1:00}",
                "Go home: {*3:00|3:30}", "Go to bed: {8:30|*9:00}"],
                script=["Hello! I'm Dilnoza. I get up at seven o'clock. I go to school at half past eight.",
                        "I have lunch at twelve o'clock. I go home at three o'clock. I go to bed at nine o'clock."]),
            TrueFalse("Listen and write T (true) or F (false).", items=[
                ("They've got Science on Tuesday.", True), ("They've got PE on Wednesday.", False),
                ("They've got Music on Wednesday.", True), ("Lily has got swimming club on Friday.", True),
                ("They've got PE on Thursday.", True)],
                script=["Anna: Have we got Science on Tuesday? — Tom: Yes, we have.",
                        "Anna: Have we got PE on Wednesday? — Tom: No, we haven't. We've got Music on Wednesday and "
                        "PE on Thursday.",
                        "Anna: Has Lily got swimming club? — Tom: Yes, she has. She's got swimming club on Friday."])]),
        Section("Part 2 · Vocabulary", [
            PicLabel("Look and write the phrases.", items=[
                ("get up", "get up"), ("lunch", "have lunch"), ("go home", "go home"), ("bed", "go to bed")],
                bank=False, cols=4, size=36),
            Order("Put the days in order (1–4).", items=["Tuesday", "Wednesday", "Thursday", "Friday"], seed=201)]),
        Section("Part 3 · Grammar", [
            Circle("Circle the correct word.", items=[
                "{*Have|Has} we got Maths on Monday?",
                "Has she got PE on Tuesday? — No, she {*hasn't|haven't}.",
                "I {*get|gets} up at seven o'clock.",
                "What time {*do|does} you go to school?",
                "I go to bed at nine. — {*So|Too} do I."]),
            Fill("Complete the sentences.", items=[
                "We've got Science {on} Wednesday.", "What club {has} he got in the evening?",
                "I have lunch {at} half past twelve.", "It's 7:30. It's {half past} seven.",
                "I go to bed at eight. — I {don't}. I go to bed at nine."], extra_words=["in", "have"])]),
        Section("Part 4 · Reading", [
            Reading("Read and answer.", title="Anna's week", text=(
                "Hi! I'm Anna. On Monday I've got Maths and English. I've got Art on Tuesday.\n\n"
                "I get up at half past six on school days. I go to school at eight o'clock and I have lunch at one "
                "o'clock. In the evening I've got swimming club."), questions=[
                ("You are Anna. What have you got on Tuesday?", "Art."),
                ("What time do you get up?", "At half past six."),
                ("What club have you got in the evening?", "Swimming club.")]),
            Unscramble("Put the words in the right order.", items=[
                "What time do you get up?", "Have we got Art on Friday?", "So do I."])]),
        Section("Part 5 · Writing", [
            _writing("Write 4–5 sentences about your school day.", [
                "On Monday I've got ___ and ___ .", "I get up at ___ .", "I go to school at ___ .",
                "I've got ___ club on ___ ."],
                ["On Monday I've got Maths and English. I get up at seven o'clock. I go to school at half past "
                 "eight. I've got chess club on Wednesday."])]),
    ]))

# ---------------------------------------------------------------- quarter 3 ----
QUARTERS.append(dict(
    n=3, slug="quarter-3-test", scope="Unit 5 Home time · Unit 6 Hobbies",
    sections=[
        Section("Part 1 · Listening", [
            NumberPics("Listen and write the numbers 1–5 in the boxes.",
                       icons=["cake", "tv", "read", "dishes", "music"], heard=[3, 4, 0, 2, 1],
                       script=["It's Saturday afternoon at Karim's house.",
                               "Number 1: Malika is doing the dishes. Number 2: Dad is listening to music.",
                               "Number 3: Mum is making a cake. Number 4: Karim is reading a book.",
                               "Number 5: Grandpa is watching TV."]),
            TrueFalse("Listen and write T (true) or F (false).", items=[
                ("Aziza plays the piano on Mondays.", True), ("She does gymnastics on Tuesdays.", False),
                ("She plays volleyball on Saturdays.", True), ("She plays table tennis.", False),
                ("She makes films on Sundays.", True)],
                script=["Aziza plays the piano on Mondays. She does gymnastics on Wednesdays and she plays "
                        "volleyball on Saturdays.",
                        "She doesn't play table tennis. On Sundays she makes films with her brother."])]),
        Section("Part 2 · Vocabulary", [
            PicLabel("Look and write the phrases.", items=[
                ("juice", "drink juice"), ("sandwich", "eat a sandwich"), ("homework", "do homework"),
                ("car", "wash the car")], bank=False, cols=4, size=36),
            PicLabel("Look and write the phrases.", items=[
                ("piano", "play the piano"), ("karate", "do karate"), ("badminton", "play badminton"),
                ("models", "make models")], bank=False, cols=4, size=36)]),
        Section("Part 3 · Grammar", [
            Circle("Circle the correct word.", items=[
                "Tom {*likes|like} washing the car.",
                "She {*doesn't|don't} enjoy doing homework.",
                "{*Does|Do} he like listening to music?",
                "Lily {*does|do} karate on Sundays.",
                "{*Does|Do} she play the guitar in the evening?"]),
            Fill("Complete the sentences.", items=[
                "My dad {likes} making cakes.", "He {doesn't} like washing the car.",
                "{Does} she enjoy reading? — No, she doesn't.", "She plays the piano {on} Mondays.",
                "Bobur plays volleyball {after} school."], extra_words=["does", "in"])]),
        Section("Part 4 · Reading", [
            Reading("Read and answer.", title="Dilya's Saturday", text=(
                "Dilya likes Saturdays. In the morning she does gymnastics. In the afternoon she makes a cake with "
                "her mum.\n\n"
                "She doesn't like doing the dishes, but she enjoys listening to music. In the evening she plays the "
                "guitar."), questions=[
                ("What does Dilya do in the morning?", "She does gymnastics."),
                ("Does she like doing the dishes?", "No, she doesn't."),
                ("Does she play the guitar in the evening?", "Yes, she does.")]),
            Unscramble("Put the words in the right order.", items=[
                "Does he enjoy doing the dishes?", "She does karate on Sundays.",
                "He doesn't like reading books."])]),
        Section("Part 5 · Writing", [
            _writing("Write 4–5 sentences about a friend or a family member.", [
                "My ___ likes ___ing.", "He / She doesn't like ___ing.", "He / She plays / does ___ on ___ .",
                "Does he / she ...? Yes / No."],
                ["My brother likes playing volleyball. He doesn't like doing the dishes. He plays volleyball on "
                 "Saturdays. Does he enjoy making films? Yes, he does."])]),
    ]))

# ------------------------------------------------ quarter 4 (final test) --------
QUARTERS.append(dict(
    n=4, slug="quarter-4-final-test", scope="Unit 7 At the market · Unit 8 At the beach + the whole year",
    sections=[
        Section("Part 1 · Listening", [
            NumberPics("Listen and write the numbers 1–5 in the boxes.",
                       icons=["pineapple", "tomato", "grapes", "lemon", "mango"], heard=[3, 4, 1, 0, 2],
                       script=["At the market.",
                               "Number 1: There are lots of lemons. Number 2: Are there any mangoes? Yes, there are.",
                               "Number 3: There are some tomatoes. Number 4: Look at the pineapples!",
                               "Number 5: The grapes are sweet."]),
            TrueFalse("Listen and write T (true) or F (false).", items=[
                ("The red towel is Anna's.", True), ("The blue towel is Lily's.", False),
                ("The yellow towel is Lily's.", True), ("There are some shells on the sand.", True),
                ("There are lots of burgers.", False)],
                script=["Anna, Tom and Lily are at the beach. The red towel is Anna's. It's hers. The blue towel is "
                        "Tom's. It's his. The yellow towel is Lily's.",
                        "There are some shells on the sand, but there aren't any burgers."])]),
        Section("Part 2 · Vocabulary", [
            PicLabel("Look and write the words.", items=[
                ("sunglasses", "sunglasses"), ("swimsuit", "swimsuit"), ("shell", "shell"),
                ("watermelon", "watermelons")], bank=False, cols=4, size=36),
            OddOne("Circle the odd one out.", rows=[
                (["rabbit", "snail", "flower", "tortoise"], "flower"),
                (["library", "gym", "playground", "juice"], "juice"),
                (["karate", "piano", "badminton", "towel"], "towel"),
                (["Monday", "Friday", "January", "Sunday"], "January")])]),
        Section("Part 3 · Grammar", [
            Circle("Circle the correct word.", items=[
                "There {*are|is} lots of grapes.",
                "{*Are|Is} there any pears? — No, there aren't.",
                "Whose shorts are these? — They're {*mine|my}.",
                "She {*plays|play} the guitar on Saturdays.",
                "What are they {*doing|do}? — They're swimming."]),
            Fill("Complete the sentences.", items=[
                "There aren't {any} limes.", "{Whose} towel is this? — It's hers.",
                "Which towel is {theirs}? — The purple one.", "I get up {at} seven o'clock.",
                "{Does} he like swimming? — Yes, he does."], extra_words=["Do", "some"])]),
        Section("Part 4 · Reading", [
            Reading("Read and answer.", title="A trip to the beach", text=(
                "It's a hot day. Bobur and his family are at the beach. There are lots of people on the sand.\n\n"
                "Bobur's sister is in the sea. She's wearing her swimsuit. Bobur is eating a burger. His dad is "
                "reading a book. The blue towel is Dad's. It's his."), questions=[
                ("Where is Bobur's family?", "They're at the beach."),
                ("What is Bobur eating?", "A burger."),
                ("Whose is the blue towel?", "It's Dad's. It's his.")]),
            Unscramble("Put the words in the right order.", items=[
                "Whose jacket is this?", "There are some pears.", "What time do you get up?"])]),
        Section("Part 5 · Writing", [
            _writing("Write a postcard from the beach (4–5 sentences).", [
                "Dear ___ ,", "I'm at the beach. The sea is ___ .", "There are lots of ___ . I'm ___ing.",
                "Love, ___"],
                ["Dear Grandma, I'm at the beach. The sea is blue. There are lots of shells. I'm swimming. "
                 "Love, Dilnoza"])]),
    ]))


def _key_intro(q: dict, total: int) -> list:
    part_rows = [["Part", "Points"]]
    for sec in q["sections"]:
        part_rows.append([sec.title, str(sum(e.points for e in sec.exercises))])
    part_rows.append(["**Total**", f"**{total}**"])
    return [
        Heading("How to use this key", 2),
        Bullets([
            "Time: 40 minutes (listening about 10 minutes, then the other parts). Pupils need a pencil.",
            "Listening: read each script **twice**, slowly and clearly, with a short pause between the lines. "
            "Do not help pupils with answers.",
            "Give 1 point for every correct item. Accept correct answers with small spelling slips only if the word "
            "is recognisable; do not give the point if the grammar is wrong.",
            "Writing (6 points): use the rubric below.",
        ]),
        Table(part_rows, widths=[0.7, 0.3], header=True, style="grid", size=10),
        Spacer(2),
        Heading("Marks", 3),
        Table(GRADE_TABLE, widths=[0.12, 0.4, 0.25, 0.23], header=True, style="grid", size=10),
        Para("Mark thresholds follow the usual 86 / 71 / 55 percent bands; adjust them if your school uses a "
             "different scale.", "note"),
        Heading("Writing rubric", 3),
        Table(WRITING_RUBRIC, widths=[0.22, 0.28, 0.27, 0.23], header=True, style="grid", size=9.5),
        Spacer(3),
    ]


def build_tests(pack_root: Path) -> list[Path]:
    made: list[Path] = []
    out = pack_root / "tests"
    for q in QUARTERS:
        total = total_points(q["sections"])
        assert total == 40, f"{q['slug']} has {total} points"
        title = f"Quarter {q['n']} test" if q["n"] < 4 else "Final test (Quarter 4)"
        sub = f"{q['scope']} · 40 points · 40 minutes"
        student = sheet(title, q["sections"], subtitle=sub, badge=BADGE, kind="test")
        made += [render_pdf(student, out / f"{q['slug']}.pdf"), render_docx(student, out / f"{q['slug']}.docx")]
        key = sheet(title, q["sections"], subtitle=sub, badge=BADGE, key=True, kind="test")
        key.blocks = _key_intro(q, total) + key.blocks
        made.append(render_pdf(key, out / f"{q['slug']}-KEY.pdf"))
    made += build_speaking(out)
    return made


# ---------------------------------------------------------------- speaking ------
SPEAKING_CARDS = {
    1: ["What's your name? How old are you?", "When's your birthday?", "What's that? (point to a picture of a snail)",
        "What's your pet's name? / What pet do you like?", "Where are you now? What are you doing?",
        "Where is the library? Where is the gym?"],
    2: ["What day is it today? What day is it tomorrow?", "Have we got English on Monday?",
        "What club have you got?", "What time do you get up?", "What time do you go to school?",
        "What time do you go to bed? (answer, then: So do I / I don't)"],
    3: ["What do you like doing at home?", "Does your mum like cooking?", "What doesn't your dad like doing?",
        "What hobby have you got? When do you do it?", "Does your friend play a sport? When?",
        "Can you play an instrument? Does your friend play?"],
    4: ["What fruit do you like? Are there any mangoes on the picture?", "Are there any tomatoes? How many?",
        "Whose bag is this? (point)", "Which towel is yours? (pictures)", "What do you like doing on holiday?",
        "Tell me about your day (three sentences)."],
}

SPEAKING_RUBRIC = [
    ["Criterion", "2 points", "1 point", "0 points"],
    ["Understanding & answering", "answers most questions, even with a little help",
     "answers some questions with repetition or hints", "rarely answers"],
    ["Vocabulary & structures", "uses words and structures from the quarter", "uses a few words, many gaps",
     "only single words or none"],
    ["Pronunciation & fluency", "easy to understand, short pauses", "sometimes hard to understand",
     "very hard to understand"],
]


def build_speaking(out: Path) -> list[Path]:
    blocks = [
        Heading("How to run the speaking check", 2),
        Bullets([
            "Do it during the week of the quarter test: 3 minutes per pupil, in pairs or one-to-one while the class "
            "works on a quiet task.",
            "Start with an easy warm-up (name, age). Then ask 3–4 questions from the quarter's card; repeat or "
            "rephrase once if needed.",
            "Score with the rubric (maximum 6). Record it next to the written test; it does not replace the written "
            "mark — use it to give a fairer overall picture.",
        ]),
        Heading("Rubric (6 points)", 2),
        Table(SPEAKING_RUBRIC, widths=[0.25, 0.27, 0.27, 0.21], header=True, style="grid", size=9.5),
    ]
    for n, qs in SPEAKING_CARDS.items():
        label = f"Quarter {n}" if n < 4 else "Final (Quarter 4)"
        blocks.append(Heading(f"Question card · {label}", 2))
        blocks.append(Table([[f"**{i}**", q] for i, q in enumerate(qs, 1)], widths=[0.08, 0.92], style="grid",
                            size=10.5, row_height=10))
    doc = Doc(title="Speaking check — rubric and question cards", blocks=blocks, badge=BADGE,
              subtitle="Quarters 1–4", kind="test")
    return [render_pdf(doc, out / "speaking-check.pdf"), render_docx(doc, out / "speaking-check.docx")]
