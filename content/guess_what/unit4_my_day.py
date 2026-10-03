"""Guess What! Level 3 · Unit 4 — My day."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, Order, PicLabel, Reading, Section, Unscramble, WordSearch, WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.unit import UnitSpec, V

from .common import BADGE, GRADE_TIP_20

VOCAB = [
    V("get up", "uyg'onmoq, o'rnidan turmoq", "get up"),
    V("get dressed", "kiyinmoq", "get dressed"),
    V("have breakfast", "nonushta qilmoq", "breakfast"),
    V("clean my teeth / brush my teeth", "tishimni tozalamoq", "teeth"),
    V("go to school", "maktabga bormoq", "go to school"),
    V("have lunch", "tushlik qilmoq", "lunch"),
    V("go home", "uyga qaytmoq", "go home"),
    V("have dinner", "kechki ovqat yemoq", "dinner"),
    V("have a shower / take a shower", "cho'milmoq, dush qabul qilmoq", "shower"),
    V("go to bed", "uxlashga yotmoq", "bed"),
]

EXTRA = [
    V("seven o'clock", "soat yetti (aniq)", "clock-0700"),
    V("half past seven", "yetti yarim", "clock-0730"),
    V("eight o'clock", "soat sakkiz (aniq)", "clock-0800"),
    V("half past eight", "sakkiz yarim", "clock-0830"),
    V("twelve o'clock", "soat o'n ikki (aniq)", "clock-1200"),
    V("half past three", "uch yarim", "clock-0330"),
]

INFO = UnitInfo(
    number=4, title="My day", topic="Daily routines and telling the time (o'clock, half past)",
    vocabulary="get up, get dressed, have breakfast, clean my teeth, go to school, have lunch, go home, have dinner, "
               "have a shower, go to bed",
    grammar=["I (have dinner) at (half past seven). What time do you (get up)? I (get up) at (seven o'clock).",
             "So do I. / I don't."],
    skills="Reading: Do you have a healthy lifestyle?",
    phonics="ue / ew / oo — blue, chew, food",
    story_value="Take exercise",
    talk_time="Asking the time",
    clil="Maths — What's the time around the world?",
    review="Review Units 3 and 4",
)

LESSONS = [
    Lesson.std(
        title="My day words",
        focus="Vocabulary — ten daily routines",
        aims=["name ten daily routines", "say what they do: I get up. I go to school."],
        language=["get up, get dressed, have breakfast, clean my teeth, go to school, have lunch, go home, "
                  "have dinner, have a shower, go to bed"],
        materials=["Flashcards", "Student's Book Vocabulary page + audio", "Worksheet A exercises A and C"],
        greeting="Greet the class. Ask 'What time do you get up?' (answers in Uzbek are fine) and write **My day** on the board.",
        warmup="**Mime the morning**: pupils stand and mime waking up, getting dressed, brushing teeth — you say the phrase "
               "and the class repeats and acts.",
        present="Present the ten cards in daily order with actions. Choral and individual repetition. Student's Book: "
                "*Listen and point*, *Listen, point and repeat*.",
        practice="Worksheet A exercise A (label pictures) and C (put the day in order). Check with the cards on the board.",
        produce="**Mime and guess** in pairs: one pupil mimes a routine, the other says 'You get up!' Swap.",
        wrap="Teacher says a routine; pupils do the action without speaking. Homework.",
        homework="Learn the ten phrases. Draw your morning and label it (Worksheet A, exercise F).",
        assessment="Point to cards at random for 5 pupils; note those who need review.",
        tips=["'have breakfast / lunch / dinner' — 'have' + ovqat nomi. O'zbekchada 'nonushta qilmoq', lekin "
              "inglizchada 'eat' emas 'have' ishlatiladi.",
              "'clean my teeth' (Britaniya) = 'brush my teeth' (AQSh) — ikkalasi ham to'g'ri.",
              "Support: daily-order picture strip on the wall. Extension: add 'wash my face'."],
    ),
    Lesson.std(
        title="What time is it?",
        focus="Telling the time (o'clock, half past) and the pattern I get up at seven o'clock",
        aims=["tell the time on the hour and the half hour", "say: I get up at seven o'clock. I have dinner at half past seven."],
        language=["What time is it? — It's (seven o'clock). / It's (half past seven).",
                  "I (get up) at (seven o'clock)."],
        materials=["A big cardboard clock with moving hands", "Worksheet A exercise B, Worksheet B exercise B",
                   "Clock faces (drawn by pupils)"],
        greeting="Ask 'What time is it now?' Show the real classroom clock.",
        warmup="**Clock mime**: use your arms as clock hands: 'It's three o'clock!' Pupils copy.",
        present="Teach o'clock first (minute hand on 12), then half past (minute hand on 6). Show each with the cardboard "
                "clock and say it three times. Then link to routines: 'I get up at seven o'clock.'",
        practice="Worksheet A exercise B (match clocks and times) and Worksheet B exercise B (write the times). "
                 "Student's Book time activities.",
        produce="**Set the clock**: pairs — A says 'half past eight', B sets their cardboard clock; then swap and add a "
                "routine: 'I go to school at half past eight.'",
        wrap="Race: teacher says a time, pupils hold up the right clock drawn on mini-whiteboards.",
        homework="Draw four clocks and write the times. Write two sentences: I … at …",
        assessment="Check who confuses o'clock and half past.",
        tips=["O'zbekcha 'soat yetti yarim' = 7:30 = inglizcha 'half past seven'. So'zma-so'z o'xshash, shuning "
              "uchun pupillar tez o'zlashtiradi.",
              "'at' + vaqt: at seven o'clock. O'zbek tilidagi '-da' qo'shimchasiga mos keladi.",
              "Support: clock with numbers written. Extension: add 'a quarter past' (oral)."],
    ),
    Lesson.std(
        title="What time do you get up?",
        focus="Grammar — What time do you …? I … at …; So do I. / I don't.",
        aims=["ask and answer: What time do you get up? I get up at seven.",
              "agree or disagree: So do I. / I don't."],
        language=["What time do you (get up)? — I (get up) at (seven o'clock).", "So do I. / I don't."],
        materials=["Routine flashcards + clocks", "Student's Book Grammar pages", "Worksheet B exercises A, C, D"],
        greeting="Ask three pupils 'What time do you get up?' and write the answers on the board.",
        warmup="**Find someone who…**: pupils stand and look for classmates who get up at the same time.",
        present="Model the dialogue with a pupil: 'I get up at seven.' — 'So do I.' — 'I get up at half past six.' — 'I don't. "
                "I get up at seven.' Write it on the board and mark So do I = the same / I don't = different.",
        practice="Student's Book Grammar activities (listen and choose, then speak). Worksheet B exercises A (circle), C (fill) "
                 "and D (unscramble).",
        produce="**Class survey**: pupils ask three classmates two questions and respond with So do I / I don't, then "
                "report: 'Aziz and I get up at seven.'",
        wrap="Whole-class chain: 'I get up at … ' — next pupil 'So do I.' / 'I don't. I …'. Homework.",
        homework="Activity Book grammar page; ask a family member two questions and write the answers.",
        assessment="Check do / don't, at + time and So do I in the survey.",
        tips=["'So do I' = 'Men ham' (xuddi shunday); 'I don't' = 'Men esa yo'q'. O'zbek tilidagi 'men ham' bilan "
              "bog'lang.",
              "Ko'p xato: 'What time you get up?' (do tushib qoladi). Doskada savol sxemasini: What time + do + you.",
              "Support: sentence strips. Extension: add a reason: 'I get up at six because I go to school early.'"],
        interactions=("T-Ss", "Ss-Ss", "T-Ss", "S / Ss-Ss", "Ss-Ss", "T-Ss"),
    ),
    Lesson.std(
        title="A healthy lifestyle",
        focus="Skills: Reading and writing — Do you have a healthy lifestyle?",
        aims=["read a short text about a day and answer questions", "write four sentences about their own day"],
        language=["healthy · exercise · sleep · breakfast", "I get up at …, I go to bed at …"],
        materials=["Student's Book Reading page", "Worksheet B exercises E–F"],
        greeting="Ask 'Are you healthy? What do you do to be healthy?' (answers in Uzbek and English).",
        warmup="**Healthy or not?** Show picture cards (fruit, sweets, sport, computer); pupils show thumbs up or down.",
        present="Pre-reading: predict from the pictures and title. Read aloud once; pupils underline the times they "
                "hear. Check words: healthy, sleep, exercise.",
        practice="Silent reading and questions (Student's Book, then Worksheet B exercise E). Check in pairs.",
        produce="Writing: using the frame in Worksheet B exercise F, pupils write four sentences about their day. "
                "Volunteers read aloud.",
        wrap="Pupils swap texts and tick 'healthy' things; class discusses what makes a healthy day. Homework.",
        homework="Finish the writing; add one healthy idea ('I play football.').",
        assessment="Collect five texts; check at + time, routine phrases and capital letters.",
        tips=["'healthy' — sog'lom; 'lifestyle' — hayot tarzi. Oddiy so'zlar bilan: 'sport, sleep, good food'.",
              "Support: provide a gapped text. Extension: compare two friends' days."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "S", "Ss-Ss"),
    ),
    Lesson.std(
        title="Take exercise!",
        focus="Story value (take exercise), Talk time (asking the time), Say it! ue / ew / oo",
        aims=["follow the story and say why exercise is good",
              "ask the time politely: Excuse me, what time is it? It's half past three.",
              "pronounce /uː/ in blue, chew, food, moon"],
        language=["Excuse me, what time is it? — It's (half past three). — Thank you.",
                  "Sound: ue / ew / oo → /uː/ (blue, chew, food)"],
        materials=["Student's Book story + audio", "Student's Book Say it! page", "cardboard clocks"],
        greeting="Do two minutes of exercise with the class (stretch, jump) and ask 'Do you like exercise?'",
        warmup="**Exercise clock**: call a time; pupils do that many jumps (seven o'clock = seven jumps).",
        present="Story: predict from the pictures, listen, answer 'Who takes exercise? Why?' Discuss in Uzbek, then "
                "conclude in English: 'Take exercise. It's good for you.'",
        practice="Talk time: model 'Excuse me, what time is it?'; practise in pairs using the cardboard clocks. Say it!: listen, "
                 "repeat, then find more oo / ue / ew words.",
        produce="**What time is it, Mr Wolf?** The class asks the time; the 'wolf' answers with a time until they say "
                "'It's dinner time!' — then everyone runs.",
        wrap="Chant the Say it! tongue twister. Homework.",
        homework="Activity Book story page; do exercise with a family member.",
        assessment="Listen for Excuse me and a correct time answer in the pairs.",
        tips=["'Excuse me' — 'Kechirasiz'. Mulozamat iborasini har doim birga o'rgating.",
              "/uː/ — o'zbekcha 'u' dan uzun. 'food' va 'foot' farqini juftliklar bilan mashq qiling."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "Ss-Ss", "G", "T-Ss"),
    ),
    Lesson.std(
        title="Time around the world",
        focus="CLIL Maths — What's the time around the world?",
        aims=["compare times in different places using a simple time-zone map",
              "say: It's twelve o'clock in Tashkent. It's ten o'clock in Moscow."],
        language=["It's (twelve o'clock) in (Tashkent). It's (ten o'clock) in (Moscow).", "earlier · later"],
        materials=["Student's Book CLIL pages", "a world map or globe", "paper plates to make clocks"],
        greeting="Show a globe. Ask 'Where is Uzbekistan?' and find Tashkent.",
        warmup="**Noon somewhere**: 'It's twelve o'clock in Tashkent. What time is it in Moscow?' — pupils guess.",
        present="Explain that different places have different times. Use cities with no summer-time change: Moscow is two "
                "hours earlier, Dubai one hour earlier, Delhi half an hour later and Tokyo four hours later than "
                "Tashkent.",
        practice="Student's Book CLIL activities (time-zone map and questions). Pupils complete a small table: City | Time "
                 "when it is 12:00 in Tashkent.",
        produce="**Time-zone clocks** in groups: make four paper-plate clocks and set them to the times of four cities, "
                "label them and present.",
        wrap="Each group says one sentence: 'It's four o'clock in Tokyo.' Homework.",
        homework="Ask a family member if they have friends or relatives in another country; find the time there.",
        assessment="Check the group clocks are correct (Moscow 10, Dubai 11, Delhi 12:30, Tokyo 16 when it is 12 in Tashkent).",
        tips=["Bu yerda yozgi vaqtga o'tmaydigan shaharlarni tanlang (Moskva, Dubay, Dehli, Tokio) — javoblar "
              "yil bo'yi to'g'ri bo'ladi. Toshkent = UTC+5.",
              "Support: provide ready-made clock faces. Extension: pupils calculate the time in a fifth city."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "G", "T-Ss"),
    ),
    Lesson.std(
        title="Unit 4 revision and quiz",
        focus="Revision of Unit 4; quick quiz",
        aims=["use routine phrases and the time accurately", "complete the unit quiz"],
        language=["All language from Unit 4"],
        materials=["Quiz (worksheets/quiz.pdf)", "Bingo (games/bingo.pdf)", "Flashcards"],
        greeting="Greet and set the goal: 'Today we show what we know about our day.'",
        warmup="**Bingo** with the ten routine phrases (8 different cards ready to print).",
        present="Mind-map on the board: routines, o'clock / half past, the question and So do I / I don't.",
        practice="Pairs: Pairs game; spot three mistakes on the board (What time you get up? / I get up in seven).",
        produce="Quiz (15 minutes, 20 points). Collect and mark with the key.",
        wrap="Go over common mistakes; praise progress.",
        homework="Correct your quiz mistakes.",
        assessment="Mark with the answer keys and record results.",
        tips=[GRADE_TIP_20, "Weak pupils: read instructions aloud. Extension: write a timetable for a perfect Saturday."],
        interactions=("T-Ss", "Ss-Ss", "T-Ss", "Ss-Ss", "S", "T-Ss"),
    ),
    Lesson.std(
        title="Review: Units 3 and 4",
        focus="Student's Book Review pages for Units 3 and 4",
        aims=["recycle Unit 3 and Unit 4 language in games and puzzles",
              "show confidence with days, have got questions, routines and time"],
        language=["Unit 3 and Unit 4 language"],
        materials=["Student's Book Review (Units 3 and 4) + audio", "Activity Book review pages",
                   "Flashcards from both units"],
        greeting="Greet the class and explain that today is a mixed review with games.",
        warmup="**Two-unit quiz show**: two teams answer quick questions from both units.",
        present="Go through the Review page instructions and model one item of each activity type.",
        practice="Pupils do the Review activities in pairs (listening / word puzzles / speaking). Monitor and note errors.",
        produce="Play the review board game; every square needs a full-sentence answer.",
        wrap="Pupils write one thing they can do well and one thing to practise. Homework.",
        homework="Activity Book review pages.",
        assessment="Observation checklist: days, have got, routines, times.",
        tips=["Bu dars 2-chorak nazorat ishiga tayyorgarlik sifatida ham ishlaydi.",
              "Support: pair weaker pupils with stronger ones. Extension: pupils write their own review questions."],
        interactions=("T-Ss", "G", "T-Ss", "Ss-Ss", "G", "T-Ss"),
    ),
]

A = [
    PicLabel("Look and write the phrases.", items=[
        ("get up", "get up"), ("get dressed", "get dressed"), ("breakfast", "have breakfast"),
        ("teeth", "clean my teeth"), ("go to school", "go to school"), ("lunch", "have lunch"),
        ("shower", "have a shower"), ("bed", "go to bed")], cols=4),
    Match("Match the clocks to the times.", pairs=[
        ("[[clock-0700|34]]", "seven o'clock"), ("[[clock-0730|34]]", "half past seven"),
        ("[[clock-0800|34]]", "eight o'clock"), ("[[clock-0830|34]]", "half past eight"),
        ("[[clock-1200|34]]", "twelve o'clock"), ("[[clock-0330|34]]", "half past three")], seed=51),
    Order("Put the day in order (1–8).", items=[
        "I get up.", "I get dressed.", "I have breakfast.", "I go to school.", "I have lunch.", "I go home.",
        "I have dinner.", "I go to bed."], seed=52),
    Gaps("Look and complete the words.", items=[
        ("breakfast", "breakfast"), ("lunch", "lunch"), ("dinner", "dinner"), ("shower", "shower"),
        ("go to school", "school"), ("teeth", "teeth")]),
    WordSearch("Find the words from the unit.", words=["breakfast", "dinner", "lunch", "school", "shower", "teeth",
                                                       "dressed", "home"], size=11, seed=10),
    Draw("Draw a clock. What time do you get up? Write the time.", prompts=["I get up at ________ ."]),
]

B = [
    Circle("Circle the correct words.", items=[
        "I {*get|gets} up at seven o'clock.",
        "What time {*do|does} you have breakfast?",
        "I go to school {*at|in} eight o'clock.",
        "It's 7:30. It's {*half past|o'clock} seven.",
        "I get up at seven. — {*So|Too} do I.",
        "I go to bed at nine. — I {*don't|do}. I go to bed at eight."]),
    PicLabel("Look at the clocks. Write the times.", items=[
        ("clock-0700", "seven o'clock"), ("clock-0830", "half past eight"), ("clock-1200", "twelve o'clock"),
        ("clock-0330", "half past three"), ("clock-0930", "half past nine"), ("clock-0600", "six o'clock")],
        cols=3, size=46),
    Fill("Complete the dialogue with words from the box.", items=[
        "What time {do} you get up?",
        "I get up {at} seven o'clock.",
        "I have breakfast at eight o'clock. — {So} do I.",
        "I go to bed at nine o'clock. — I {don't}. I go to bed at half past eight."], extra_words=["does"]),
    Unscramble("Put the words in the right order.", items=[
        "What time do you get up?", "I get up at seven o'clock.", "So do I.", "I have lunch at twelve o'clock."]),
    Reading("Read and answer.", title="Lucas's day", text=(
        "I get up at seven o'clock. I have breakfast at half past seven. I go to school at eight o'clock.\n\n"
        "I have lunch at one o'clock. I go home at three o'clock. I have dinner at six o'clock and I go to "
        "bed at half past eight."), questions=[
        ("You are Lucas. What time do you get up?", "At seven o'clock."),
        ("What time do you have lunch?", "At one o'clock."),
        ("What time do you go to bed?", "At half past eight.")]),
    WriteAbout("Write about your day.", frames=[
        "I get up at ___ .", "I have breakfast at ___ .", "I go to school at ___ .", "I go to bed at ___ ."], lines=3,
        model=["I get up at seven o'clock. I have breakfast at half past seven. I go to school at eight o'clock. "
               "I go to bed at nine o'clock."]),
]

QUIZ = [
    Section("Part 1 · Words", [
        PicLabel("Look and write the phrases.", items=[
            ("get up", "get up"), ("breakfast", "have breakfast"), ("go to school", "go to school"),
            ("lunch", "have lunch"), ("dinner", "have dinner"), ("bed", "go to bed")], bank=False, cols=3,
            size=34)]),
    Section("Part 2 · Grammar", [
        Circle("Circle the correct word.", items=[
            "I {*get|gets} up at half past seven.",
            "What time {*do|does} you go to school?",
            "I have lunch {*at|on} twelve o'clock.",
            "I have breakfast at eight. — {*So|Too} do I."]),
        Fill("Complete the sentences.", items=[
            "What time {do} you get up?",
            "I go to school {at} eight o'clock.",
            "I have dinner at six. — I {don't}. I have dinner at seven.",
            "It's 9:30. It's half past {nine}."], extra_words=["does"])]),
    Section("Part 3 · Clocks and writing", [
        PicLabel("Write the times.", items=[
            ("clock-0800", "eight o'clock"), ("clock-0730", "half past seven"), ("clock-0330", "half past three")],
            bank=False, cols=3, size=44),
        Unscramble("Put the words in the right order.", items=[
            "What time do you get up?", "I go home at three o'clock.", "So do I."])]),
]

SPEC = UnitSpec(number=4, slug="unit-4-my-day", title="My day", info=INFO, vocab=VOCAB, extra_vocab=EXTRA,
                lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="Daily routines and clocks", sheet_b_name="What time do you…? So do I / I don't")
