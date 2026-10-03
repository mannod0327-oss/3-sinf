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
    V("Maths", "matematika", "maths"), V("English", "ingliz tili", "abc"),
    V("Science", "tabiiy fan", "science room"), V("Art", "tasviriy san'at", "paint"),
    V("Music", "musiqa", "music room"), V("PE", "jismoniy tarbiya", "run"),
    V("swimming club", "suzish to'garagi", "swimming"), V("chess club", "shaxmat to'garagi", "chess"),
]

INFO = UnitInfo(
    number=3, title="School days", topic="Days of the week, school subjects and after-school clubs",
    vocabulary="Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday",
    grammar=["Have we got (Science) on (Tuesday)? Yes, we have. / No, we haven't.",
             "What (club) has she got (in the evening)? She's got (swimming club) (in the evening)."],
    skills="Listening: Have you got a favourite day of the week?",
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
        warmup="**Human calendar**: seven pupils hold the day cards and stand in a line in the wrong order; the class "
               "tells them where to go ('Monday, here!').",
        present="Teach the days with the flashcards and a rhythm (clap on the stressed syllable: MON-day, TUES-day). Use "
                "the pictures as memory aids (moon, fire, wind, lightning, heart, planet, sun). Student's Book: "
                "*Listen and point*, *Listen, point and repeat*.",
        practice="Worksheet A exercises A (order), B (match with Uzbek) and C (complete the words). Chant the days "
                 "forwards and backwards.",
        produce="**Today, tomorrow, yesterday**: in pairs, pupil A says 'Today is Wednesday.' Pupil B says 'Tomorrow is "
                "Thursday.' Then 'Yesterday was Tuesday.' Swap.",
        wrap="Whole-class chant of the week with the actions. Homework.",
        homework="Learn to spell the seven days. Draw this week's calendar with one picture per day (Worksheet A, "
                 "exercise F).",
        assessment="Ask six pupils 'What day is it tomorrow?' without help.",
        tips=["Kun nomlari bosh harf bilan yoziladi: Monday, Tuesday… (o'zbek tilida kichik harf).",
              "'Wednesday' talaffuzi /ˈwenzdeɪ/ — 'd' aytilmaydi. 'Thursday' — 'th' tovushiga e'tibor bering.",
              "Support: use the picture cards while ordering. Extension: name the month and date too."],
    ),
    Lesson.std(
        title="Have we got Science on Tuesday?",
        focus="Grammar 1 — Have we got …? Yes, we have. / No, we haven't.",
        aims=["ask and answer about the timetable: Have we got Maths on Monday?",
              "use on + day of the week and short answers Yes, we have. / No, we haven't."],
        language=["Have we got (Science) on (Tuesday)? — Yes, we have. / No, we haven't.",
                  "Maths, English, Science, Art, Music, PE"],
        materials=["Class timetable (real or drawn on the board)", "Subject flashcards", "Worksheet B exercises A–B"],
        greeting="Review days with the human-calendar game. Ask 'What lessons have we got today?'",
        warmup="**Guess the lesson**: mime a subject (painting, singing, running) — the class says the subject.",
        present="Project the class timetable. Ask and answer with the whole class: 'Have we got Maths on Monday? Yes, "
                "we have.' 'Have we got PE on Wednesday? No, we haven't.' Underline **on + day** and the short "
                "answers.",
        practice="Pairs: use the Student's Book timetable to ask and answer. Worksheet B exercises A (circle) and B (read "
                 "Anna's timetable and answer).",
        produce="**Timetable interview**: pupils ask three classmates 'Have you got … on …?' and record yes / no on a "
                "grid, then report: 'We've got Art on Friday.'",
        wrap="Whole class: teacher says a subject and day — pupils answer Yes, we have / No, we haven't. Homework.",
        homework="Copy your own school timetable in English (days and subjects).",
        assessment="Listen for have/haven't and on + day; note errors for the next lesson.",
        tips=["O'zbekcha 'bizda … bor / yo'q' — inglizcha 'we have got / we haven't got'. 'Got' ni tashlab "
              "ketishmasin.",
              "Kun oldidagi predlog: **on Monday**, lekin 'in the morning'. Ikkalasini ajratib yozib qo'ying.",
              "Support: colour-code the days. Extension: ask about two subjects in one question."],
    ),
    Lesson.std(
        title="What club has she got?",
        focus="Grammar 2 — has got, clubs and parts of the day",
        aims=["ask and answer: What club has she got in the evening? She's got swimming club.",
              "use in the morning / afternoon / evening"],
        language=["What (club) has (she) got (in the evening)? — She's got (swimming club) (in the evening).",
                  "in the morning · in the afternoon · in the evening"],
        materials=["Club posters (swimming, chess, art, football)", "Student's Book Grammar page 2", "Worksheet B exercises C–D"],
        greeting="Ask 'What clubs have we got at school?' and list them on the board.",
        warmup="**Who is it?** Describe a pupil's clubs ('He's got chess club on Monday.') — the class guesses the pupil.",
        present="Show a weekly club timetable for a fictional child (Lily). Model the question and answer, then build the "
                "he / she forms: 'has got' = 's got. Compare: We've got / She's got.",
        practice="Student's Book Grammar activities. Worksheet B exercises C (unscramble) and D (fill in).",
        produce="**Class club chart**: groups collect and report 'Amir has got chess club on Tuesday afternoon.'",
        wrap="Quick-fire: teacher names a child and a day; the class says the club. Homework.",
        homework="Activity Book grammar page; write two sentences about a friend's clubs.",
        assessment="Check has / have and 's got in the group reports.",
        tips=["'has got' — he/she/it; 'have got' — I/you/we/they. O'zbek tilida bunday farq yo'q, shuning uchun "
              "jadval yordam beradi.",
              "Qisqa shakl: **She's got** = She has got. **We've got** = We have got."],
    ),
    Lesson.std(
        title="My favourite day",
        focus="Skills: Listening — Have you got a favourite day of the week? + writing a timetable",
        aims=["listen for days and subjects and complete a timetable",
              "write a short text about their school day"],
        language=["My favourite day is …, because I've got … on … ", "days, subjects"],
        materials=["Student's Book Listening page + audio", "Worksheet B, exercise E", "a blank timetable grid"],
        greeting="Ask 'Have you got a favourite day?' and count hands for each day on the board.",
        warmup="**Timetable bingo**: pupils write five day-subject pairs; you call pairs, they cross them out.",
        present="Pre-listening: read the instructions and look at the picture. Play the audio twice — first for gist (who "
                "likes which day), then to complete the timetable.",
        practice="Check answers in pairs, then with the class. Pupils read Anna's timetable (Worksheet B, exercise B) again "
                 "and find the busiest day.",
        produce="Writing: pupils write four sentences about their favourite school day using the help box. Volunteers "
                "read aloud.",
        wrap="Graph the favourite days on the board and say 'Friday is our class favourite.' Homework.",
        homework="Finish the text; draw your timetable for one day.",
        assessment="Collect five texts: check on + day, subjects and 've got.",
        tips=["Tinglash: ikki marta qo'ying; birinchi marta kunlarni, ikkinchi marta fanlarni toping.",
              "Support: provide a half-filled timetable. Extension: add 'because it's …' (oral)."],
        interactions=("T-Ss", "S", "T-Ss", "S / Ss-Ss", "S", "T-Ss"),
    ),
    Lesson.std(
        title="Be resourceful",
        focus="Story value (be resourceful), Talk time (asking if places are open), Say it! oa / ow",
        aims=["follow the story and explain in simple words what 'resourceful' means",
              "ask if a place is open: Is the library open today? Yes, it is. / No, it's closed.",
              "pronounce /əʊ/ in goat, snow, boat, road"],
        language=["Is the (library) open (on Sundays)? — Yes, it is. / No, it's closed.",
                  "Sound: oa / ow → /əʊ/ (goats, snow, boat)"],
        materials=["Student's Book story + audio", "Student's Book Say it! page",
                   "open/closed signs for school places"],
        greeting="Show an OPEN and a CLOSED sign and ask 'Is our library open today?'",
        warmup="**Open or closed?** Hold up a sign and a place flashcard; pupils say 'The library is open!'",
        present="Story: predict from pictures, listen, answer 'What problem have they got? How do they solve it?' "
                "Discuss 'resourceful' (finding a clever way to solve a problem) in Uzbek and English.",
        practice="Talk time: model the question and answers, practise in open and closed pairs with the signs. Say it!: listen, "
                 "repeat, brainstorm more oa / ow words.",
        produce="**Open for business**: pairs create a timetable for three places (library, shop, gym) and role-play "
                "asking if they are open.",
        wrap="Chant the Say it! tongue twister slowly then fast. Homework.",
        homework="Activity Book story page; ask at home when a local shop is open.",
        assessment="Listen for Is … open? and correct short answers.",
        tips=["'open' = ochiq, 'closed' = yopiq. Vaqt so'rash uchun 'on Sundays' (yakshanba kunlari).",
              "/əʊ/ diftongi — 'o' + 'u' ga yaqin; 'snow' ni 'snou' deb mashq qiling."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "Ss-Ss", "Ss-Ss", "T-Ss"),
    ),
    Lesson.std(
        title="Night and day animals",
        focus="CLIL Science — Which animals are nocturnal?",
        aims=["say what nocturnal and diurnal mean in simple words",
              "sort animals into day and night animals"],
        language=["nocturnal · at night · during the day", "An owl is nocturnal. It sleeps during the day."],
        materials=["Student's Book CLIL pages + video if available", "animal pictures (owl, bat, rabbit, tortoise…)",
                   "a two-column table: Day | Night"],
        greeting="Turn the lights off for a moment: 'Is it day or night?' Introduce 'night'.",
        warmup="**Day or night?** Show animal pictures; pupils stand (day) or sit (night) for each.",
        present="Explain 'nocturnal' with the owl and bat; compare with animals that are active during the day. Build "
                "the table on the board.",
        practice="Student's Book CLIL activities; pupils complete their own Day | Night table.",
        produce="**Fact cards** in groups: each group writes two sentences about one nocturnal animal and draws it.",
        wrap="Groups read their cards; the class says 'day animal' or 'night animal'.",
        homework="Find one nocturnal animal from Uzbekistan and draw it.",
        assessment="Fact card rubric: correct sentence (1), drawing (1), teamwork (1).",
        tips=["'nocturnal' — 'tungi'. Mahalliy misol: 'yarqanot' (bat), 'boyo'g'li' (owl).",
              "Fan darsi bilan integratsiya: hayvonlarning kun tartibi."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "G", "T-Ss"),
    ),
    Lesson.std(
        title="Unit 3 revision and quiz",
        focus="Revision of Unit 3; quick quiz",
        aims=["use the days, subjects and have got questions accurately", "complete the unit quiz"],
        language=["All language from Unit 3"],
        materials=["Quiz (worksheets/quiz.pdf)", "Bingo (games/bingo.pdf)", "Flashcards"],
        greeting="Greet and explain the plan: game, revision, quiz.",
        warmup="**Bingo** with the days and subjects (8 different cards ready to print).",
        present="Mind-map on the board: days, subjects, have got questions and short answers.",
        practice="Pairs: play the Pairs game; then correct three wrong sentences on the board.",
        produce="Quiz (15 minutes, 20 points). Collect and mark with the key.",
        wrap="Go over common mistakes; praise progress.",
        homework="Correct your quiz mistakes.",
        assessment="Mark with the answer keys and record results.",
        tips=[GRADE_TIP_20, "Weak pupils: read instructions aloud. Extension: write a timetable for an imaginary school."],
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
        "{*Have|Has} we got Science on Tuesday?",
        "{Have|*Has} she got swimming club in the evening?",
        "Have we got Art on Friday? — Yes, we {*have|has}.",
        "Has he got chess club on Monday? — No, he {*hasn't|haven't}.",
        "We've got Maths {*on|in} Monday.",
        "She's got swimming club {*in|on} the evening."]),
    Reading("Read Anna's timetable and answer.", title="Anna's timetable", text=(
        "Monday: Maths, English\n\nTuesday: Science, Art\n\nWednesday: Music, PE\n\n"
        "Thursday: English, Maths\n\nFriday: Art, Science"), questions=[
        ("Has Anna got Science on Tuesday?", "Yes, she has."),
        ("Has she got Music on Friday?", "No, she hasn't."),
        ("What has she got on Wednesday?", "She's got Music and PE."),
        ("Has she got English on Thursday?", "Yes, she has.")]),
    Unscramble("Put the words in the right order.", items=[
        "Have we got Science on Tuesday?", "Yes, we have.", "What club has she got?",
        "She's got swimming club in the evening."]),
    Fill("Complete the sentences.", items=[
        "{Have} we got Art on Monday? — No, we {haven't}.",
        "What club {has} he got on Friday? — He's got chess club.",
        "She's got music club {in} the afternoon.",
        "{Has} he got PE on Thursday? — Yes, he {has}."], extra_words=["hasn't"]),
    WriteAbout("Write about your school day.", frames=[
        "On Monday I've got ___ and ___ .", "My favourite day is ___ .", "I've got ___ club on ___ ."], lines=3,
        model=["On Monday I've got Maths and English. My favourite day is Friday. I've got chess club on "
               "Wednesday."]),
]

QUIZ = [
    Section("Part 1 · Words", [
        Order("Put the days in order.", items=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
              seed=41)]),
    Section("Part 2 · Grammar", [
        Circle("Circle the correct word.", items=[
            "{*Have|Has} we got Maths on Monday?",
            "Has she got Art on Tuesday? — Yes, she {*has|have}.",
            "We've got Science {*on|in} Friday.",
            "What club {*has|have} he got in the evening?"]),
        Fill("Complete the sentences.", items=[
            "Today is Tuesday. Tomorrow is {Wednesday}.",
            "{Have} we got English on Thursday? — Yes, we have.",
            "Has he got PE on Monday? — No, he {hasn't}.",
            "She's got chess club {in} the evening."], extra_words=["has"])]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="Max's Friday", text=(
            "Max has got Art and Music on Friday. He hasn't got Maths. In the afternoon he has got football "
            "club."), questions=[
            ("Has Max got Art on Friday?", "Yes, he has."),
            ("Has he got Maths on Friday?", "No, he hasn't."),
            ("What club has he got in the afternoon?", "Football club.")]),
        Unscramble("Put the words in the right order.", items=[
            "Have we got Art on Monday?", "Yes, we have.", "She's got swimming club."])]),
]

SPEC = UnitSpec(number=3, slug="unit-3-school-days", title="School days", info=INFO, vocab=VOCAB, extra_vocab=EXTRA,
                lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="Days of the week", sheet_b_name="have got questions, timetable, writing")
