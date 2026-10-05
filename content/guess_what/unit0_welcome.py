"""Guess What! Level 3 · Welcome unit — friends, months and birthdays."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, Order, PicLabel, Reading, Section, TrueFalse, Unscramble, WordSearch,
    WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.unit import UnitSpec, V

from .common import BADGE, GRADE_TIP_20

# The pictures are season / event memory aids for the months.
VOCAB = [
    V("January", "yanvar", "snow"), V("February", "fevral", "wind"), V("March", "mart", "seedling"),
    V("April", "aprel", "rain"), V("May", "may", "flower"), V("June", "iyun", "sun"),
    V("July", "iyul", "watermelon"), V("August", "avgust", "beach"), V("September", "sentabr", "bag"),
    V("October", "oktabr", "leaf"), V("November", "noyabr", "cloud"), V("December", "dekabr", "gift"),
]

EXTRA = [
    V("Lucas", "Lukas (o'g'il bola)", "boy"), V("Max", "Maks (o'g'il bola)", "boy"),
    V("Lily", "Lili (qiz bola)", "girl"), V("Tom", "Tom (o'g'il bola)", "boy"),
    V("Anna", "Anna (qiz bola)", "girl"),
]

INFO = UnitInfo(
    number=0, title="Welcome", topic="The course friends; questions; months of the year and birthdays",
    vocabulary="Lucas, Max, Lily, Tom, Anna; the twelve months",
    grammar=["Review of questions (What's your name? How old are you? Where are you from?)",
             "When's your birthday? It's in (December)."],
    skills="Reading: Do you have an email penpal?",
    phonics="a / ai — snakes, tails",
    story_value="Work together",
    talk_time="Asking for permission",
    clil="Art — What can you see in a landscape painting?",
)

LESSONS = [
    Lesson.std(
        title="Meet the friends",
        focus="The five course characters; review of personal questions",
        aims=["introduce themselves: My name's … I'm … years old. I'm from …",
              "ask and answer: What's your name? How old are you? Where are you from?"],
        language=["What's your name? — My name's … · How old are you? — I'm … · Where are you from? — I'm from …",
                  "Lucas, Max, Lily, Tom, Anna"],
        materials=["Student's Book Welcome pages + audio", "name labels", "character pictures (Lucas, Max, Lily, Tom, Anna)"],
        greeting="Greet the class warmly: 'Welcome to Grade 3!' Give each student a name label.",
        warmup="**Name ball**: throw a soft ball; the catcher says 'My name's …' then throws to someone else.",
        present="Introduce the five friends with the Student's Book pictures: 'This is Lucas. He's nine. He's from …' "
                "Students listen and point to the characters. Teach the three questions with gestures.",
        practice="Pairs: ask and answer the three questions. Worksheet B exercises A–B.",
        produce="**Class interview**: students walk around and fill a card: name, age, town for three classmates.",
        wrap="Report: 'Bobur is nine. He's from Tashkent.' Homework.",
        homework="Write three sentences about yourself.",
        assessment="Listen to each student introduce themselves; note those who need support.",
        tips=["Yangi o'quv yilida ismlar va yoshni so'rash — eng yaxshi muloqot boshlanishi. Hammani gapirishga "
              "undang.",
              "'I'm from Tashkent' — 'Men Toshkentdanman'. 'from' (-dan) ni albatta qo'shish kerak.",
              "Support: give answer frames. Extension: add 'I have a brother.'"],
    ),
    Lesson.std(
        title="Months of the year",
        focus="Vocabulary — the twelve months",
        aims=["say the twelve months in order", "say which month it is now and when they were born"],
        language=["January, February, March, April, May, June, July, August, September, October, November, December"],
        materials=["Flashcards (one month each)", "Student's Book Welcome pages + audio", "Worksheet A exercises A–C"],
        greeting="Ask 'What day is it? What month is it?' Write the month on the board.",
        warmup="**Human year**: twelve students hold the month cards and stand in a circle in the wrong places; the class "
               "tells them where to go.",
        present="Teach the months with the flashcards in groups of four (winter / spring / summer / fall). Use the "
                "pictures as memory aids. Chant them with a rhythm.",
        practice="Worksheet A exercises A (order), B (match with Uzbek) and C (complete the words).",
        produce="**Line up by birthday**: students ask 'When's your birthday?' and line up from January to December "
                "without speaking Uzbek.",
        wrap="Whole-class chant of the months with actions. Homework.",
        homework="Learn to spell the months. Draw your birthday cake (Worksheet A exercise F).",
        assessment="Ask five students 'What month is after …?'",
        tips=["Oylar bosh harf bilan yoziladi: March (o'zbek tilida 'mart' kichik harf).",
              "Qiyin so'zlar: February (Feb-ru-ary), August, September. Bo'g'inlarga bo'lib mashq qiling.",
              "Support: use the picture cards. Extension: name the season for each month."],
    ),
    Lesson.std(
        title="When's your birthday?",
        focus="Grammar — When's your birthday? It's in (December). + Reading: an email penpal",
        aims=["ask and answer: When's your birthday? It's in December.",
              "read a short penpal email and write one"],
        language=["When's your birthday? — It's in (December).", "penpal · email · Dear … / Hi …"],
        materials=["Student's Book Welcome pages + audio", "Worksheet B exercises C–E", "birthday cards or paper"],
        greeting="Sing or chant 'Happy birthday'. Ask 'Whose birthday is in January?'",
        warmup="**Birthday circle**: students stand in a circle; you call a month and those born in it swap places.",
        present="Model the question and answer with two students, then write it on the board with **in** + month highlighted.",
        practice="Pairs: class survey of birthdays. Worksheet B exercises C (unscramble) and D (read the penpal email).",
        produce="Writing: students write an email to a penpal (Worksheet B exercise E) and swap with a partner.",
        wrap="Class graph of birthdays by month; 'Most birthdays are in …'. Homework.",
        homework="Finish your email; ask two family members when their birthdays are.",
        assessment="Collect five emails: check My name is / I'm / It's in and capital letters.",
        tips=["'in' + oy (in March), 'on' + sana (on the 5th). Bu sinfda faqat 'in' ni o'rgating.",
              "Elektron xat (email): Hi/Dear … va oxirida ism. Yozuv odatini shakllantiring.",
              "Support: give a gapped email. Extension: add 'I like …' sentences."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "Ss-Ss", "S", "T-Ss"),
    ),
    Lesson.std(
        title="Work together",
        focus="Story value (work together), Talk time (asking for permission), Say it! a / ai, CLIL Art (landscape)",
        aims=["follow the story and say why it is good to work together",
              "ask permission politely: Can I open the window, please? — Yes, you can. / Sorry, you can't.",
              "pronounce /eɪ/ in snake, tail, rain, cake",
              "name parts of a landscape: mountains, river, trees, sky"],
        language=["Can I (open the window), please? — Yes, you can. / Sorry, you can't.",
                  "Sound: a / ai → /eɪ/ (snakes, tails)", "landscape · mountains · river · trees · sky"],
        materials=["Student's Book story + audio + Say it! page", "Student's Book CLIL page", "paper and crayons"],
        greeting="Ask two students to carry a big box together: 'Can you do it alone? Let's work together!'",
        warmup="**Group puzzle**: each group builds a simple jigsaw; the fastest group says what helped them.",
        present="Story: predict from pictures, listen, answer 'Who works together? What happens?' Talk time: model the "
                "permission dialogue with two students; practice in pairs. Say it!: listen and repeat /eɪ/.",
        practice="Art (CLIL): look at the landscape painting in the Student's Book and name what you can see: 'I can see "
                 "mountains.' Students complete a simple table: Foreground | Background.",
        produce="**Group landscape**: each group draws one large landscape, each student adds one thing and asks "
                "permission ('Can I use the green pencil, please?').",
        wrap="Groups present their painting: 'We can see a river and some trees.' Homework.",
        homework="Workbook Welcome pages; draw a landscape you know in Uzbekistan.",
        assessment="Listen for permission phrases and please / thank you.",
        tips=["'Can I …?' — ruxsat so'rash. 'May I' ham to'g'ri, ammo bu sinfda 'Can I' yetarli.",
              "/eɪ/ diftongi o'zbek tilida yo'q — 'ey' ga yaqin; 'snake' ni 'sneyk' deb mashq qiling.",
              "Bu dars mazmuni 2 ta darslik bo'limini (Story + CLIL) birlashtirgan; vaqt yetmasa Art qismini keyingi darsga "
              "qoldiring."],
        interactions=("T-Ss", "G", "T-Ss", "S / Ss-Ss", "G", "T-Ss"),
    ),
]

A = [
    Order("Put the months in order (1–12).", items=[
        "January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
        "November", "December"], seed=101),
    Match("Match the English months to the Uzbek months.", pairs=[
        ("January", "yanvar"), ("February", "fevral"), ("March", "mart"), ("April", "aprel"), ("May", "may"),
        ("June", "iyun"), ("July", "iyul"), ("August", "avgust"), ("September", "sentabr"), ("October", "oktabr"),
        ("November", "noyabr"), ("December", "dekabr")], seed=102),
    Gaps("Look and complete the months.", items=[
        ("snow", "January"), ("seedling", "March"), ("flower", "May"), ("sun", "June"), ("leaf", "October"),
        ("gift", "December")]),
    WordSearch("Find eight months.", words=["january", "february", "march", "april", "june", "july", "august",
                                            "september"], size=11, seed=15),
    TrueFalse("Write T (true) or F (false).", items=[
        ("December is the last month of the year.", True), ("March comes before February.", False),
        ("There are twelve months in a year.", True), ("June comes after May.", True),
        ("September is the first month.", False)]),
    Draw("Draw a birthday cake. Write the month of your birthday.", prompts=["My birthday is in ________ ."]),
]

B = [
    Circle("Circle the correct words.", items=[
        "{*What's|Where's} your name?",
        "{*How|What} old are you?",
        "{*Where|What} are you from?",
        "{*When's|Where's} your birthday?",
        "It's {*in|on} December.",
        "{*Can|Do} I open the window, please?"]),
    Fill("Complete the dialogue.", items=[
        "{What's} your name? — My {name} is Anna.",
        "{How} old are you? — I'm nine.",
        "{When's} your birthday? — It's {in} March."], extra_words=["Where's"]),
    Unscramble("Put the words in the right order.", items=[
        "When's your birthday?", "It's in December.", "Can I open the window?", "Yes, you can."]),
    Reading("Read and answer.", title="An email from Max", text=(
        "Hi! My name is Max. I'm nine years old. I'm from Scotland. My birthday is in July.\n\n"
        "I have a dog and a rabbit. I like soccer and swimming. Do you have an email penpal? "
        "Please write to me! Max"), questions=[
        ("How old is Max?", "He's nine."),
        ("Where is he from?", "He's from Scotland."),
        ("When's his birthday?", "It's in July.")]),
    WriteAbout("Write an email to a penpal.", frames=[
        "Hi! My name is ___ .", "I'm ___ years old. I'm from ___ .", "My birthday is in ___ .",
        "I like ___ ."], lines=4,
        model=["Hi! My name is Dilnoza. I'm nine years old. I'm from Samarkand. My birthday is in May. "
               "I like drawing and swimming."]),
]

QUIZ = [
    Section("Part 1 · Months", [
        Order("Put the months in order (1–6).", items=["January", "February", "March", "April", "May", "June"],
              seed=111)]),
    Section("Part 2 · Grammar", [
        Circle("Circle the correct word.", items=[
            "{*When's|Where's} your birthday?",
            "It's {*in|on} August.",
            "{*How|Where} old are you?",
            "{*Can|Are} I sit here, please?"]),
        Fill("Complete the sentences.", items=[
            "{What's} your name? — I'm Lucas.",
            "{Where} are you from? — I'm from Tashkent.",
            "When's your birthday? — It's {in} October.",
            "{Can} I open the door, please? — Yes, you can."], extra_words=["How"])]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="Anna's email", text=(
            "Hello! My name is Anna. I'm ten years old. I'm from London. My birthday is in December. "
            "I have a cat."), questions=[
            ("How old is Anna?", "She's ten."),
            ("Where is she from?", "She's from London."),
            ("When's her birthday?", "It's in December.")]),
        Unscramble("Put the words in the right order.", items=[
            "What's your name?", "I'm from Samarkand.", "Yes, you can."])]),
]

SPEC = UnitSpec(number=0, slug="unit-0-welcome", title="Welcome", info=INFO, vocab=VOCAB, extra_vocab=EXTRA,
                lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="Months of the year", sheet_b_name="Questions, birthdays, penpal email",
                intro_note="The Welcome unit has four lessons in the annual plan (Story, Talk time, Say it! and CLIL "
                           "share the last lesson).")
