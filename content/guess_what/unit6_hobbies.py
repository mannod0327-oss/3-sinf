"""Guess What! Level 3 · Unit 6 — Hobbies."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, OddOne, PicLabel, Reading, Section, TrueFalse, Unscramble, WordSearch,
    WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.unit import UnitSpec, V

from .common import BADGE, GRADE_TIP_20

VOCAB = [
    V("play the piano", "pianino chalmoq", "piano"),
    V("play the guitar", "gitara chalmoq", "guitar"),
    V("play the recorder", "fleyta chalmoq", "recorder"),
    V("make models", "maketlar yasamoq", "models"),
    V("make films / make movies", "kino (film) suratga olmoq", "films"),
    V("do karate", "karate bilan shug'ullanmoq", "karate"),
    V("do gymnastics", "gimnastika bilan shug'ullanmoq", "gymnastics"),
    V("play table tennis / Ping-Pong", "stol tennisi o'ynamoq", "table tennis"),
    V("play badminton", "badminton o'ynamoq", "badminton"),
    V("play volleyball", "voleybol o'ynamoq", "volleyball"),
]

EXTRA = [
    V("on Saturdays", "shanba kunlari", "calendar"), V("in the morning", "ertalab", "sun"),
    V("in the afternoon", "tushdan keyin", "cloud"), V("in the evening", "kechqurun", "moon"),
    V("after school", "darsdan keyin", "bag"),
]

INFO = UnitInfo(
    number=6, title="Hobbies", topic="Hobbies and sports; what people do and when",
    vocabulary="play the piano, play the guitar, play the recorder, make models, make films, do karate, do gymnastics, "
               "play table tennis, play badminton, play volleyball",
    grammar=["She (does karate) (on Sundays).",
             "Does she (do gymnastics) (in the evening)? Yes, she does. / No, she doesn't."],
    skills="Reading: What sports do you like?",
    phonics="sh — sharks, fish",
    story_value="Try new things",
    talk_time="Encouraging others to try things",
    clil="Music — What type of musical instrument is it?",
    review="Review Units 5 and 6",
)

LESSONS = [
    Lesson.std(
        title="Hobby words",
        focus="Vocabulary — ten hobbies and sports",
        aims=["name ten hobbies", "say what hobbies they like: I play the guitar. I do karate."],
        language=["play the piano / guitar / recorder, make models / films, do karate / gymnastics, "
                  "play table tennis / badminton / volleyball"],
        materials=["Flashcards", "Student's Book Vocabulary page + audio", "Worksheet A exercises A–B"],
        greeting="Greet the class. Ask 'What do you like doing after school?' and write **Hobbies** on the board.",
        warmup="**Charades**: pupils mime a hobby; the class guesses in Uzbek and you give the English phrase.",
        present="Present the ten cards with actions. Show the verb patterns: **play** + instrument / ball game; **do** + "
                "karate / gymnastics; **make** + models / films. Student's Book: *Listen and point*, *Listen, point "
                "and repeat*, number game ('Is he playing the piano? Number 4!').",
        practice="Worksheet A exercises A (label) and B (match with Uzbek). Play **What's missing?**",
        produce="**Is he playing the piano?** Pairs play the Student's Book number game: one pupil asks yes / no "
                "questions until they guess the picture number.",
        wrap="Teacher says a phrase; pupils act it. Homework.",
        homework="Learn the phrases and draw your hobby (Worksheet A exercise F).",
        assessment="Point at cards for 5 pupils; note gaps.",
        tips=["'play / do / make' — uchta fe'l, o'zbekchada ko'pincha 'qilmoq / chalmoq'. Jadval: play + gitara, "
              "do + karate, make + kino.",
              "'recorder' — bolalar fleytasi (blokflöyta). Mahalliy maktab musiqa xonasidagi 'nay' bilan solishtiring.",
              "Support: pictures only. Extension: add two more hobbies."],
    ),
    Lesson.std(
        title="She does karate on Sundays",
        focus="Grammar 1 — he / she + does / plays / makes; on Sundays, in the evening, after school",
        aims=["say what a person does and when: She does karate on Sundays.",
              "use on + day, in the morning / afternoon / evening, after school"],
        language=["She (does karate) (on Sundays). He plays / makes / does …",
                  "on Saturdays · in the evening · after school"],
        materials=["A weekly hobby chart for one child (draw on the board)", "Flashcards", "Worksheet B exercise A"],
        greeting="Ask 'What does your friend do on Saturdays?' pointing to a pupil and model 'She plays …'.",
        warmup="**What does she do?** Show a weekly hobby chart of an imaginary child and pupils guess the hobby from a mime.",
        present="Read the chart: 'Lily plays badminton on Saturdays. She does karate on Sundays. She makes models after "
                "school.' Underline the verb endings (plays, does, makes) and the time phrases. Point out the "
                "irregular forms do → does, go → goes.",
        practice="Student's Book Grammar activities (listen, then true / false). Worksheet B exercise A (circle).",
        produce="**Hobby chart**: pupils draw a weekly chart for an imaginary friend and tell a partner: 'Bobur plays "
                "volleyball on Fridays.'",
        wrap="Quick-fire: name a child and a day; pupils say the sentence. Homework.",
        homework="Workbook grammar page; write three sentences about a friend's hobbies and when.",
        assessment="Check -s / -es endings and the time phrases.",
        tips=["Vaqt predloglari: **on** + kun (on Sundays), **in** + kun qismi (in the evening), **after** school. "
              "Ularni uchta rangda yozing.",
              "'does' — bu yerda asosiy fe'l ('do karate'), 'do' ning he/she shakli.",
              "Support: sentence frames. Extension: add 'and' to join two hobbies."],
    ),
    Lesson.std(
        title="Does she do gymnastics?",
        focus="Grammar 2 — Does she …? Yes, she does. / No, she doesn't.",
        aims=["ask and answer: Does she do gymnastics in the evening? Yes, she does.",
              "ask about time: When does he play volleyball?"],
        language=["Does she (do gymnastics) (in the evening)? — Yes, she does. / No, she doesn't."],
        materials=["Club timetables (Student's Book club notes or your own)", "Chant from the audio", "Worksheet B exercises B–C"],
        greeting="Ask 'Does your friend play football?' and elicit 'Yes, he does.'",
        warmup="**Yes / no race**: two teams; you ask 'Does she play the piano?' pointing to a picture; fastest correct answer "
               "scores.",
        present="Use the Student's Book club notes (two children and their clubs): 'Does he play tennis on Tuesdays? Yes, "
                "he does.' 'Does she play volleyball in the morning? No, she doesn't.' Build the pattern on the board.",
        practice="Play the chant / Student's Book Grammar audio. Worksheet B exercises B (fill) and C (unscramble).",
        produce="**Club detectives**: pairs get different timetables; A asks yes / no questions to fill in their "
                "missing days.",
        wrap="Teacher asks five questions about the timetables; pupils answer chorally. Homework.",
        homework="Activity Book grammar page; write four questions about a friend's hobbies.",
        assessment="Check Does + bare verb and short answers.",
        tips=["'Does' bor joyda asosiy fe'lga -s qo'shilmaydi: Does she **do**, Does he **play**.",
              "Support: question frames on strips. Extension: ask 'When…?' questions."],
        interactions=("T-Ss", "G", "T-Ss", "S / Ss-Ss", "Ss-Ss", "T-Ss"),
    ),
    Lesson.std(
        title="What sports do you like?",
        focus="Skills: Reading and writing — What sports do you like?",
        aims=["read a text about a boy and his sports and answer questions",
              "write about their favourite sport"],
        language=["He goes to a football club on Tuesdays.", "favourite sport · healthy diet"],
        materials=["Student's Book Reading page", "Worksheet B exercises D–E"],
        greeting="Ask 'Who likes football?' Count hands and write the class results.",
        warmup="**Sports survey**: pupils stand and group themselves by favourite sport.",
        present="Before reading: look at the picture and predict. Read aloud once while pupils underline the sports. Check "
                "'healthy diet' with pictures.",
        practice="Silent reading, then the comprehension questions (Student's Book, then Worksheet B exercise D). Check in "
                 "pairs.",
        produce="Writing: pupils write four sentences about their favourite sport using the help box (Worksheet B "
                "exercise E).",
        wrap="Class chart: 'Football is our class favourite.' Homework.",
        homework="Finish the writing; add a drawing.",
        assessment="Collect five texts; check verb endings and time phrases.",
        tips=["'goes to a club' — 'to'garakka qatnaydi'. 'go' → 'goes' (-es) ni alohida ko'rsating.",
              "Support: cloze text. Extension: write about a sport they want to try."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "S", "T-Ss"),
    ),
    Lesson.std(
        title="Try new things",
        focus="Story value (try new things), Talk time (encouraging others), Say it! sh",
        aims=["follow the story and say why it is good to try new things",
              "encourage a friend: Come on, try it! You can do it! Well done!",
              "pronounce /ʃ/ in shark, fish, she, shop"],
        language=["Come on — try it! · You can do it! · Well done!", "Sound: sh → /ʃ/ (sharks, fish)"],
        materials=["Student's Book story + audio", "Student's Book Say it! page"],
        greeting="Ask 'What new thing did you try this year?' (Uzbek is fine).",
        warmup="**Try it!** Pupils try an unusual action (write with the other hand) while the class shouts 'You can do it!'",
        present="Story: predict from pictures, listen, answer 'Who can play? Who is afraid? Who helps?' Discuss the value "
                "and conclude in English: 'Try new things.'",
        practice="Talk time: model 'Come on — try it!' and practise in open and closed pairs with one pupil hesitating. "
                 "Say it!: listen, repeat, find more sh words.",
        produce="**Try this!** Pairs role-play: one tries a new hobby (table tennis), the other encourages.",
        wrap="Chant the Say it! tongue twister. Homework.",
        homework="Activity Book story page; try one new thing and tell the class.",
        assessment="Listen for encouraging phrases and /ʃ/.",
        tips=["/ʃ/ o'zbekcha 'sh' ga o'xshash — bu tovush bolalarga oson. 'fish' oxiridagi 'sh' ni cho'zib mashq qiling.",
              "Ruhlantirish iboralarini har dars boshida ishlating: 'Well done!'"],
        interactions=("T-Ss", "T-Ss", "T-Ss", "Ss-Ss", "Ss-Ss", "T-Ss"),
    ),
    Lesson.std(
        title="Musical instruments",
        focus="CLIL Music — What type of musical instrument is it?",
        aims=["name four instrument families: string, woodwind, brass, percussion",
              "say what type an instrument is: A guitar is a string instrument"],
        language=["string · woodwind · brass · percussion · instrument", "A (piano) is a (string) instrument."],
        materials=["Student's Book CLIL pages", "pictures of instruments (drum, dutar, flute, trumpet, guitar)",
                   "recycled card, rice / beans, tape (to make a drum)"],
        greeting="Play a short clip or make a sound; ask 'What instrument is it?'",
        warmup="**Name that sound**: pupils guess the instrument from a sound or mime.",
        present="Introduce the four families with pictures. Include a local instrument: the dutar is a string "
                "instrument, the doira is a percussion instrument.",
        practice="Student's Book CLIL activities; pupils sort instruments into four columns.",
        produce="**Make a drum**: from recycled card (Student's Book project); decorate and play a rhythm.",
        wrap="Each group plays a rhythm; the class says 'It's a percussion instrument.' Homework.",
        homework="Find one instrument at home or in your neighbourhood and say its type.",
        assessment="Sort instruments correctly (4 points) and explain one in English.",
        tips=["Mahalliy cholg'ular: dutar (string), doira (percussion), nay (woodwind), karnay (brass). Bu darsni "
              "o'zbek madaniyati bilan bog'lash tushunishni oshiradi.",
              "Xavfsizlik: doira yasashda qaychi va yelimni nazorat qiling."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "G", "T-Ss"),
    ),
    Lesson.std(
        title="Unit 6 revision and quiz",
        focus="Revision of Unit 6; quick quiz",
        aims=["use hobby phrases, does / doesn't and time phrases accurately", "complete the unit quiz"],
        language=["All language from Unit 6"],
        materials=["Quiz (worksheets/quiz.pdf)", "Bingo (games/bingo.pdf)", "Flashcards"],
        greeting="Greet and set the goal: 'Show what you know about hobbies.'",
        warmup="**Bingo** with the ten hobbies (8 different cards ready to print).",
        present="Mind-map on the board: hobbies, time phrases, She does… / Does she…?",
        practice="Pairs: Pairs game; correct three wrong sentences (She play / Does she does).",
        produce="Quiz (15 minutes, 20 points). Collect and mark with the key.",
        wrap="Go over common mistakes; praise progress.",
        homework="Correct your quiz mistakes.",
        assessment="Mark with the answer keys and record results.",
        tips=[GRADE_TIP_20, "Weak pupils: read instructions aloud. Extension: write a timetable for a busy friend."],
        interactions=("T-Ss", "Ss-Ss", "T-Ss", "Ss-Ss", "S", "T-Ss"),
    ),
    Lesson.std(
        title="Review: Units 5 and 6",
        focus="Student's Book Review pages for Units 5 and 6",
        aims=["recycle Unit 5 and Unit 6 language in games and puzzles",
              "show confidence with likes, does / doesn't and hobbies"],
        language=["Unit 5 and Unit 6 language"],
        materials=["Student's Book Review (Units 5 and 6) + audio", "Activity Book review pages",
                   "Flashcards from both units"],
        greeting="Greet the class and explain that today is a mixed review with word puzzles.",
        warmup="**Two-unit quiz show**: two teams answer quick questions from both units.",
        present="Go through the Review page: backwards-word puzzles and the matching tasks. Model one item.",
        practice="Pupils do the Review activities in pairs (listening / word puzzles / speaking). Monitor and note errors.",
        produce="Pupils make their own backwards-word puzzle for a friend (like 'yalp llabyellov') and swap.",
        wrap="Pupils write one thing they can do well and one thing to practise. Homework.",
        homework="Activity Book review pages.",
        assessment="Observation checklist: -s endings, does / doesn't, hobbies.",
        tips=["Bu dars 3-chorak nazorat ishiga tayyorgarlik sifatida ham ishlaydi.",
              "Support: give a list of words to hide. Extension: add a sentence to each puzzle."],
        interactions=("T-Ss", "G", "T-Ss", "Ss-Ss", "Ss-Ss", "T-Ss"),
    ),
]

A = [
    PicLabel("Look and write the phrases.", items=[
        ("piano", "play the piano"), ("guitar", "play the guitar"), ("recorder", "play the recorder"),
        ("models", "make models"), ("films", "make films"), ("karate", "do karate"),
        ("gymnastics", "do gymnastics"), ("table tennis", "play table tennis")], cols=4),
    Match("Match the English phrases to the Uzbek phrases.", pairs=[
        ("play the piano", "pianino chalmoq"), ("do karate", "karate bilan shug'ullanmoq"),
        ("make models", "maketlar yasamoq"), ("play volleyball", "voleybol o'ynamoq"),
        ("play the guitar", "gitara chalmoq"), ("make films", "kino suratga olmoq")], seed=71),
    Gaps("Look and complete the words.", items=[
        ("piano", "piano"), ("guitar", "guitar"), ("karate", "karate"), ("gymnastics", "gymnastics"),
        ("volleyball", "volleyball"), ("badminton", "badminton")]),
    WordSearch("Find the hobby words.", words=["piano", "guitar", "recorder", "models", "films", "karate",
                                                "gymnastics", "tennis", "badminton", "volleyball"], size=12, seed=12),
    Circle("Circle the correct verb: play, do or make.", items=[
        "I {*play|do} the piano.", "She {*does|plays} karate.", "We {*make|play} models.",
        "They {*play|make} volleyball.", "He {*does|makes} gymnastics.", "I {*make|do} films."]),
    Draw("Draw your hobby.", prompts=["My hobby: ________"]),
]

B = [
    Circle("Circle the correct words.", items=[
        "Lily {*plays|play} badminton on Saturdays.",
        "She {*does|do} karate on Sundays.",
        "Tom {*makes|make} models after school.",
        "{*Does|Do} she do gymnastics in the evening?",
        "Yes, she {*does|do}.",
        "No, he {*doesn't|don't}."]),
    Fill("Complete the sentences.", items=[
        "{Does} Dilshod play tennis on Mondays? — Yes, he {does}.",
        "{Does} Malika play volleyball in the morning? — No, she {doesn't}.",
        "Bobur {makes} films on Mondays.",
        "She {plays} the guitar in the morning."], extra_words=["do"]),
    Unscramble("Put the words in the right order.", items=[
        "She does karate on Sundays.", "Does she do gymnastics?", "Yes, she does.", "He plays the piano in the evening."]),
    Reading("Read and answer.", title="Dilshod's week", text=(
        "Meet Dilshod. He is nine years old and he wants to be a swimmer. Dilshod goes to a swimming club on "
        "Mondays and Wednesdays after school. He does karate on Fridays.\n\n"
        "On Saturdays he plays table tennis with his brother. Dilshod has a healthy diet. His favourite drink "
        "is apple juice!"), questions=[
        ("What club does Dilshod go to?", "A swimming club."),
        ("Does he do karate on Fridays?", "Yes, he does."),
        ("Does he play table tennis on Sundays?", "No, he doesn't. He plays on Saturdays.")],
        lines_per_answer=1),
    WriteAbout("Write about your favourite sport or hobby.", frames=[
        "My favourite sport is ___ .", "I play / do ___ on ___ .", "I like it because ___ ."], lines=3,
        model=["My favourite sport is volleyball. I play volleyball on Saturdays. I like it because it is fun."]),
]

QUIZ = [
    Section("Part 1 · Words", [
        PicLabel("Look and write the phrases.", items=[
            ("piano", "play the piano"), ("guitar", "play the guitar"), ("models", "make models"),
            ("karate", "do karate"), ("badminton", "play badminton"), ("volleyball", "play volleyball")],
            bank=False, cols=3, size=34)]),
    Section("Part 2 · Grammar", [
        Circle("Circle the correct word.", items=[
            "She {*does|do} gymnastics on Sundays.",
            "Tom {*plays|play} table tennis after school.",
            "{*Does|Do} he make films? — No, he doesn't.",
            "Yes, she {*does|do}."]),
        Fill("Complete the sentences.", items=[
            "She {does} karate in the evening.",
            "He {plays} the guitar on Saturdays.",
            "{Does} Lily make models? — Yes, she does.",
            "No, he {doesn't}."], extra_words=["do"])]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="Bobur's week", text=(
            "Bobur is very busy. He plays volleyball on Saturdays and does gymnastics on Sundays. "
            "He makes models on Mondays after school. He doesn't play on the computer in the evening."),
            questions=[
            ("When does Bobur play volleyball?", "On Saturdays."),
            ("Does he do gymnastics on Sundays?", "Yes, he does."),
            ("Does he play on the computer in the evening?", "No, he doesn't.")]),
        Unscramble("Put the words in the right order.", items=[
            "She plays the piano.", "Does he do karate?", "He doesn't play badminton."])]),
]

SPEC = UnitSpec(number=6, slug="unit-6-hobbies", title="Hobbies", info=INFO, vocab=VOCAB, extra_vocab=EXTRA,
                lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="Hobbies and sports", sheet_b_name="She does… Does she…? reading, writing")
