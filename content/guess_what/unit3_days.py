"""Guess What! Level 3 · Unit 3 — School days."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, Order, PicLabel, Reading, Section, TrueFalse, Unscramble, WordSearch,
    WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.unit import UnitSpec, V

from .common import BADGE, GRADE_TIP_20

# The pictures are memory aids (Moon-day, Sun-day …), not claims about word origins.
VOCAB = [
    V("Monday", "dushanba", "moon"),
    V("Tuesday", "seshanba", "fire"),
    V("Wednesday", "chorshanba", "wind"),
    V("Thursday", "payshanba", "lightning"),
    V("Friday", "juma", "heart"),
    V("Saturday", "shanba", "planet"),
    V("Sunday", "yakshanba", "sun"),
]

EXTRA = [
    V("Math", "matematika", "math"), V("English", "ingliz tili", "abc"),
    V("Science", "tabiiy fan", "science lab"), V("Art", "tasviriy san'at", "paint"),
    V("Music", "musiqa", "music room"), V("P.E.", "jismoniy tarbiya", "run"),
    V("swimming club", "suzish to'garagi", "swimming"), V("chess club", "shaxmat to'garagi", "chess"),
]

INFO = UnitInfo(
    number=3, title="School days", topic="Days of the week, school subjects and after-school clubs",
    vocabulary="Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday",
    grammar=["Do we have (science) on (Tuesday)? Yes, we do. / No, we don't.",
             "What (club) does she have (in the evening)? She has (swimming club) (in the evening)."],
    skills="Listening: Do you have a favorite day of the week?",
    phonics="oa / ow — goats, snow",
    story_value="Be resourceful",
    talk_time="Asking if places are open",
    clil="Science — Which animals are nocturnal?",
)

LESSONS = [
    Lesson.std(
        title="The days of the week",
        focus="Vocabulary — Monday to Sunday",
        aims=["say the seven days in order", "say which day is today, tomorrow and yesterday"],
        language=["Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday",
                  "Today is … / Tomorrow is … / Yesterday was …"],
        materials=["Flashcards (one day each, with the memory picture)", "Student's Book Vocabulary page + audio",
                   "Worksheet A exercises A–C"],
        greeting="Greet the class and ask 'What day is it today?' — write the weekday on the board with today's date.",
        warmup="**Human calendar**: seven students hold the day cards and stand in a line in the wrong order; the class "
               "tells them where to go ('Monday, here!').",
        present="Teach the days with the flashcards and a rhythm (clap on the stressed syllable: MON-day, TUES-day). Use "
                "the pictures as memory aids (moon, fire, wind, lightning, heart, planet, sun). Student's Book: "
                "*Listen and point*, *Listen, point and repeat*.",
        practice="Worksheet A exercises A (order), B (match with Uzbek) and C (complete the words). Chant the days "
                 "forwards and backwards.",
        produce="**Today, tomorrow, yesterday**: in pairs, student A says 'Today is Wednesday.' Student B says 'Tomorrow is "
                "Thursday.' Then 'Yesterday was Tuesday.' Swap.",
        wrap="Whole-class chant of the week with the actions. Homework.",
        homework="Learn to spell the seven days. Draw this week's calendar with one picture per day (Worksheet A, "
                 "exercise F).",
        assessment="Ask six students 'What day is it tomorrow?' without help.",
        tips=["Kun nomlari bosh harf bilan yoziladi: Monday, Tuesday… (o'zbek tilida kichik harf).",
              "'Wednesday' talaffuzi /ˈwenzdeɪ/ — 'd' aytilmaydi. 'Thursday' — 'th' tovushiga e'tibor bering.",
              "Support: use the picture cards while ordering. Extension: name the month and date too."],
    ),
    Lesson.std(
        title="Do we have Science on Tuesday?",
        focus="Grammar 1 — Do we have …? Yes, we do. / No, we don't.",
        aims=["ask and answer about the schedule: Do we have Math on Monday?",
              "use on + day of the week and short answers Yes, we do. / No, we don't."],
        language=["Do we have (science) on (Tuesday)? — Yes, we do. / No, we don't.",
                  "math, English, science, art, music, P.E."],
        materials=["Class schedule (real or drawn on the board)", "Subject flashcards", "Worksheet B exercises A–B"],
        greeting="Review days with the human-calendar game. Ask 'What lessons do we have today?'",
        warmup="**Guess the lesson**: mime a subject (painting, singing, running) — the class says the subject.",
        present="Project the class schedule. Ask and answer with the whole class: 'Do we have math on Monday? Yes, "
                "we do.' 'Do we have P.E. on Wednesday? No, we don't.' Underline **on + day** and the short "
                "answers.",
        practice="Pairs: use the Student's Book schedule to ask and answer. Worksheet B exercises A (circle) and B (read "
                 "Anna's schedule and answer).",
        produce="**Schedule interview**: students ask three classmates 'Do you have … on …?' and record yes / no on a "
                "grid, then report: 'We have art on Friday.'",
        wrap="Whole class: teacher says a subject and day — students answer Yes, we do / No, we don't. Homework.",
        homework="Copy your own school schedule in English (days and subjects).",
        assessment="Listen for do / don't and on + day; note errors for the next lesson.",
        tips=["O'zbekcha 'bizda … bormi?' — inglizcha **Do we have …?** Savolni 'do' boshlaydi, 'have' esa o'zgarmaydi. "
              "Javob: Yes, we **do**. / No, we **don't**.",
              "Kun oldidagi predlog: **on Monday**, lekin 'in the morning'. Ikkalasini ajratib yozib qo'ying.",
              "Support: color-code the days. Extension: ask about two subjects in one question."],
    ),
    Lesson.std(
        title="What club does she have?",
        focus="Grammar 2 — does / has, clubs and parts of the day",
        aims=["ask and answer: What club does she have in the evening? She has swimming club.",
              "use in the morning / afternoon / evening"],
        language=["What (club) does (she) have (in the evening)? — She has (swimming club) (in the evening).",
                  "in the morning · in the afternoon · in the evening"],
        materials=["Club posters (swimming, chess, art, soccer)", "Student's Book Grammar page 2", "Worksheet B exercises C–D"],
        greeting="Ask 'What clubs do we have at school?' and list them on the board.",
        warmup="**Who is it?** Describe a student's clubs ('He has chess club on Monday.') — the class guesses the student.",
        present="Show a weekly club schedule for a fictional child (Lily). Model the question and answer, then build the "
                "he / she forms: **does** + have in the question, **has** in the answer. Compare: We have / She has.",
        practice="Student's Book Grammar activities. Worksheet B exercises C (unscramble) and D (fill in).",
        produce="**Class club chart**: groups collect and report 'Amir has chess club on Tuesday afternoon.'",
        wrap="Quick-fire: teacher names a child and a day; the class says the club. Homework.",
        homework="Workbook grammar page; write two sentences about a friend's clubs.",
        assessment="Check does / do and has / have in the group reports.",
        tips=["Javobda 'has' — he/she/it; 'have' — I/you/we/they. Savolda esa **does she have …?** ('has' emas!). "
              "O'zbek tilida bunday farq yo'q, shuning uchun jadval yordam beradi.",
              "Qisqa javob: Yes, she **does**. / No, she **doesn't**."],
    ),
    Lesson.std(
        title="My favorite day",
        focus="Skills: Listening — Do you have a favorite day of the week? + writing a schedule",
        aims=["listen for days and subjects and complete a schedule",
              "write a short text about their school day"],
        language=["My favorite day is …, because I have … on … ", "days, subjects"],
        materials=["Student's Book Listening page + audio", "Worksheet B, exercise E", "a blank schedule grid"],
        greeting="Ask 'Do you have a favorite day?' and count hands for each day on the board.",
        warmup="**Schedule bingo**: students write five day-subject pairs; you call pairs, they cross them out.",
        present="Pre-listening: read the instructions and look at the picture. Play the audio twice — first for gist (who "
                "likes which day), then to complete the schedule.",
        practice="Check answers in pairs, then with the class. Students read Anna's schedule (Worksheet B, exercise B) again "
                 "and find the busiest day.",
        produce="Writing: students write four sentences about their favorite school day using the help box. Volunteers "
                "read aloud.",
        wrap="Graph the favorite days on the board and say 'Friday is our class favorite.' Homework.",
        homework="Finish the text; draw your schedule for one day.",
        assessment="Collect five texts: check on + day, subjects and I have.",
        tips=["Tinglash: ikki marta qo'ying; birinchi marta kunlarni, ikkinchi marta fanlarni toping.",
              "Support: provide a half-filled schedule. Extension: add 'because it's …' (oral)."],
        interactions=("T-Ss", "S", "T-Ss", "S / Ss-Ss", "S", "T-Ss"),
    ),
    Lesson.std(
        title="Be resourceful",
        focus="Story value (be resourceful), Talk time (asking if places are open), Say it! oa / ow",
        aims=["follow the story and explain in simple words what 'resourceful' means",
              "ask if a place is open: Is the library open today? Yes, it is. / No, it's closed.",
              "pronounce /oʊ/ in goat, snow, boat, road"],
        language=["Is the (library) open (on Sundays)? — Yes, it is. / No, it's closed.",
                  "Sound: oa / ow → /oʊ/ (goats, snow, boat)"],
        materials=["Student's Book story + audio", "Student's Book Say it! page",
                   "open/closed signs for school places"],
        greeting="Show an OPEN and a CLOSED sign and ask 'Is our library open today?'",
        warmup="**Open or closed?** Hold up a sign and a place flashcard; students say 'The library is open!'",
        present="Story: predict from pictures, listen, answer 'What problem do they have? How do they solve it?' "
                "Discuss 'resourceful' (finding a clever way to solve a problem) in Uzbek and English.",
        practice="Talk time: model the question and answers, practice in open and closed pairs with the signs. Say it!: listen, "
                 "repeat, brainstorm more oa / ow words.",
        produce="**Open for business**: pairs create a schedule for three places (library, store, gym) and role-play "
                "asking if they are open.",
        wrap="Chant the Say it! tongue twister slowly then fast. Homework.",
        homework="Workbook story page; ask at home when a local store is open.",
        assessment="Listen for Is … open? and correct short answers.",
        tips=["'open' = ochiq, 'closed' = yopiq. Vaqt so'rash uchun 'on Sundays' (yakshanba kunlari).",
              "/oʊ/ diftongi — 'o' + 'u' ga yaqin; 'snow' ni 'snou' deb mashq qiling."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "Ss-Ss", "Ss-Ss", "T-Ss"),
    ),
    Lesson.std(
        title="Night and day animals",
        focus="CLIL Science — Which animals are nocturnal?",
        aims=["say what nocturnal and diurnal mean in simple words",
              "sort animals into day and night animals"],
        language=["nocturnal · at night · during the day", "An owl is nocturnal. It sleeps during the day."],
        materials=["Student's Book CLIL pages + video if available", "animal pictures (owl, bat, rabbit, turtle…)",
                   "a two-column table: Day | Night"],
        greeting="Turn the lights off for a moment: 'Is it day or night?' Introduce 'night'.",
        warmup="**Day or night?** Show animal pictures; students stand (day) or sit (night) for each.",
        present="Explain 'nocturnal' with the owl and bat; compare with animals that are active during the day. Build "
                "the table on the board.",
        practice="Student's Book CLIL activities; students complete their own Day | Night table.",
        produce="**Fact cards** in groups: each group writes two sentences about one nocturnal animal and draws it.",
        wrap="Groups read their cards; the class says 'day animal' or 'night animal'.",
        homework="Find one nocturnal animal from Uzbekistan and draw it.",
        assessment="Fact card rubric: correct sentence (1), drawing (1), teamwork (1).",
        tips=["'nocturnal' — 'tungi'. Mahalliy misol: 'yarqanot' (bat), 'boyo'g'li' (owl).",
              "Fan darsi bilan integratsiya: hayvonlarning kun tartibi."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "G", "T-Ss"),
    ),
    Lesson.std(
        title="Unit 3 review and quiz",
        focus="Review of Unit 3; quick quiz",
        aims=["use the days, subjects and do / does questions accurately", "complete the unit quiz"],
        language=["All language from Unit 3"],
        materials=["Quiz (worksheets/quiz.pdf)", "Bingo (games/bingo.pdf)", "Flashcards"],
        greeting="Greet and explain the plan: game, review, quiz.",
        warmup="**Bingo** with the days and subjects (8 different cards ready to print).",
        present="Mind-map on the board: days, subjects, do / does questions and short answers.",
        practice="Pairs: play the Pairs game; then correct three wrong sentences on the board.",
        produce="Quiz (15 minutes, 20 points). Collect and mark with the key.",
        wrap="Go over common mistakes; praise progress.",
        homework="Correct your quiz mistakes.",
        assessment="Mark with the answer keys and record results.",
        tips=[GRADE_TIP_20, "Weak students: read instructions aloud. Extension: write a schedule for an imaginary school."],
        interactions=("T-Ss", "Ss-Ss", "T-Ss", "Ss-Ss", "S", "T-Ss"),
    ),
]

A = [
    Order("Put the days in order.", items=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",
                                            "Sunday"], seed=31),
    Match("Match the English days to the Uzbek days.", pairs=[
        ("Monday", "dushanba"), ("Tuesday", "seshanba"), ("Wednesday", "chorshanba"), ("Thursday", "payshanba"),
        ("Friday", "juma"), ("Saturday", "shanba"), ("Sunday", "yakshanba")], seed=32),
    Gaps("Look and complete the days.", items=[
        ("moon", "Monday"), ("fire", "Tuesday"), ("wind", "Wednesday"), ("lightning", "Thursday"),
        ("heart", "Friday"), ("planet", "Saturday"), ("sun", "Sunday")], cols=4, size=30),
    Fill("Write the missing day.", items=[
        "Today is Monday. Tomorrow is {Tuesday}.",
        "Today is Wednesday. Yesterday was {Tuesday}.",
        "Yesterday was Friday. Today is {Saturday}.",
        "Today is Thursday. Tomorrow is {Friday}.",
        "Tomorrow is Sunday. Today is {Saturday}.",
        "Yesterday was Wednesday. Today is {Thursday}."], bank=True),
    TrueFalse("Write T (true) or F (false).", items=[
        ("Saturday comes after Friday.", True), ("Monday comes after Tuesday.", False),
        ("There are seven days in a week.", True), ("Thursday comes before Wednesday.", False),
        ("Sunday comes after Saturday.", True)]),
    WordSearch("Find the seven days.", words=["monday", "tuesday", "wednesday", "thursday", "friday", "saturday",
                                              "sunday"], size=11, seed=9),
    Draw("Draw this week's calendar. Put one picture for each day.", prompts=["My week"]),
]

B = [
    Circle("Circle the correct words.", items=[
        "{*Do|Does} we have science on Tuesday?",
        "{Do|*Does} she have swimming club in the evening?",
        "Do we have art on Friday? — Yes, we {*do|does}.",
        "Does he have chess club on Monday? — No, he {*doesn't|don't}.",
        "We have math {*on|in} Monday.",
        "She has swimming club {*in|on} the evening."]),
    Reading("Read Anna's schedule and answer.", title="Anna's schedule", text=(
        "Monday: math, English\n\nTuesday: science, art\n\nWednesday: music, P.E.\n\n"
        "Thursday: English, math\n\nFriday: art, science"), questions=[
        ("Does Anna have science on Tuesday?", "Yes, she does."),
        ("Does she have music on Friday?", "No, she doesn't."),
        ("What does she have on Wednesday?", "She has music and P.E."),
        ("Does she have English on Thursday?", "Yes, she does.")]),
    Unscramble("Put the words in the right order.", items=[
        "Do we have science on Tuesday?", "Yes, we do.", "What club does she have?",
        "She has swimming club in the evening."]),
    Fill("Complete the sentences.", items=[
        "{Do} we have art on Monday? — No, we {don't}.",
        "What club {does} he have on Friday? — He has chess club.",
        "She has music club {in} the afternoon.",
        "{Does} he have P.E. on Thursday? — Yes, he {does}."], extra_words=["doesn't"]),
    WriteAbout("Write about your school day.", frames=[
        "On Monday I have ___ and ___ .", "My favorite day is ___ .", "I have ___ club on ___ ."], lines=3,
        model=["On Monday I have math and English. My favorite day is Friday. I have chess club on "
               "Wednesday."]),
]

QUIZ = [
    Section("Part 1 · Words", [
        Order("Put the days in order.", items=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
              seed=41)]),
    Section("Part 2 · Grammar", [
        Circle("Circle the correct word.", items=[
            "{*Do|Does} we have math on Monday?",
            "Does she have art on Tuesday? — Yes, she {*does|do}.",
            "We have science {*on|in} Friday.",
            "What club {*does|do} he have in the evening?"]),
        Fill("Complete the sentences.", items=[
            "Today is Tuesday. Tomorrow is {Wednesday}.",
            "{Do} we have English on Thursday? — Yes, we do.",
            "Does he have P.E. on Monday? — No, he {doesn't}.",
            "She has chess club {in} the evening."], extra_words=["does"])]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="Max's Friday", text=(
            "Max has art and music on Friday. He doesn't have math. In the afternoon he has soccer "
            "club."), questions=[
            ("Does Max have art on Friday?", "Yes, he does."),
            ("Does he have math on Friday?", "No, he doesn't."),
            ("What club does he have in the afternoon?", "Soccer club.")]),
        Unscramble("Put the words in the right order.", items=[
            "Do we have art on Monday?", "Yes, we do.", "She has swimming club."])]),
]

SPEC = UnitSpec(number=3, slug="unit-3-school-days", title="School days", info=INFO, vocab=VOCAB, extra_vocab=EXTRA,
                lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="Days of the week", sheet_b_name="do / does + have, schedule, writing")
