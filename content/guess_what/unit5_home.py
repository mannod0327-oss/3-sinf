"""Guess What! Level 3 · Unit 5 — Home time."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, OddOne, PicLabel, Reading, Section, Unscramble, WordSearch, WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.unit import UnitSpec, V

from .common import BADGE, GRADE_TIP_20

VOCAB = [
    V("drink juice", "sharbat ichmoq", "juice"),
    V("eat a sandwich", "buterbrod yemoq", "sandwich"),
    V("do the dishes", "idish-tovoq yuvmoq", "dishes"),
    V("play on the computer", "kompyuterda o'ynamoq", "play computer"),
    V("read a book", "kitob o'qimoq", "read"),
    V("watch TV", "televizor ko'rmoq", "tv"),
    V("do homework", "uy vazifasini bajarmoq", "homework"),
    V("listen to music", "musiqa tinglamoq", "music"),
    V("make a cake", "tort (kek) tayyorlamoq", "cake"),
    V("wash the car", "mashinani yuvmoq", "car"),
]

EXTRA = [
    V("like", "yoqtirmoq", "thumbs up"), V("enjoy", "zavqlanmoq", "happy"),
    V("love", "juda yaxshi ko'rmoq", "heart"), V("hate", "yomon ko'rmoq", "angry"),
]

INFO = UnitInfo(
    number=5, title="Home time", topic="Home activities; likes and dislikes (he / she)",
    vocabulary="drink juice, eat a sandwich, do the dishes, play on the computer, read a book, watch TV, do homework, "
               "listen to music, make a cake, wash the car",
    grammar=["He (doesn't like) (reading books).",
             "Does he (enjoy) (doing the dishes)? Yes, he does. / No, he doesn't."],
    skills="Listening: Are you helpful at home?",
    phonics="th — panthers, three",
    story_value="Show forgiveness",
    talk_time="Suggesting food to make",
    clil="Geography — Where do people live?",
)

LESSONS = [
    Lesson.std(
        title="At home",
        focus="Vocabulary — ten things we do at home",
        aims=["name ten home activities", "say what they do at home: I watch TV. I do my homework."],
        language=["drink juice, eat a sandwich, do the dishes, play on the computer, read a book, watch TV, "
                  "do homework, listen to music, make a cake, wash the car"],
        materials=["Flashcards", "Student's Book Vocabulary page + audio", "Worksheet A exercises A–B"],
        greeting="Greet the class and ask 'What do you do after school?' (Uzbek is fine). Write **Home time** on the board.",
        warmup="**Mime the chore**: students mime an activity; the class shouts the Uzbek word; you give the English phrase.",
        present="Present the ten phrases with actions and flashcards. Choral and individual repetition. Student's Book: "
                "*Listen and point*, *Listen, point and repeat*. Note 'do' with homework / dishes, 'make' with cake, "
                "'watch' with TV.",
        practice="Worksheet A exercises A (label the pictures) and B (match with Uzbek). Play **What's missing?**",
        produce="**Mime and guess** in groups: 'Are you washing the car?' — 'Yes, I am.' Keep the -ing forms simple and "
                "oral.",
        wrap="Teacher says a phrase, students do the action; then they say it back without a prompt. Homework.",
        homework="Learn the phrases and draw your favorite home activity (Worksheet A exercise F).",
        assessment="Point at cards for 5 students; note gaps.",
        tips=["'do / make / watch' fe'llari: 'do homework', 'make a cake', 'watch TV'. O'zbekchada hammasi "
              "'qilmoq' — shuning uchun fe'l + ot juftliklarini jadval qilib yozing.",
              "'homework' sanalmaydigan ot: 'a homework' deb aytilmaydi.",
              "Support: flashcards with pictures only. Extension: add two home activities of their own."],
    ),
    Lesson.std(
        title="He likes… He doesn't like…",
        focus="Grammar 1 — third person -s and doesn't + like / enjoy + -ing",
        aims=["say what he / she likes or doesn't like: He doesn't like reading books.",
              "use verb + -ing after like and enjoy: likes watching TV"],
        language=["He (doesn't like) (reading books).", "She likes / enjoys (listening to music)."],
        materials=["Picture cards of family members (mom, dad, brother)", "Flashcards", "Worksheet B exercise A"],
        greeting="Ask 'Does your brother like soccer?' (yes / no, in any language) and write 'likes' on the board.",
        warmup="**Like / don't like lines**: students move to one side of the room for 'I like…' and the other for 'I don't like…'.",
        present="Show a boy (Karim) with thumbs up for watching TV and thumbs down for doing the dishes. Say: 'Karim "
                "likes watching TV. He doesn't like doing the dishes.' Write the rule: he / she + likes; doesn't + "
                "like. Verb + -ing after like / enjoy.",
        practice="Student's Book Grammar activities. Worksheet B exercises A (circle) and B (complete with words from "
                 "the box).",
        produce="**Family talk**: students tell a partner two sentences about a family member: 'My mom likes cooking. "
                "She doesn't like washing the car.'",
        wrap="Quick-fire: show a picture and a thumb; students say the full sentence. Homework.",
        homework="Workbook grammar page; write three sentences about your family's likes.",
        assessment="Check likes / doesn't like and -ing forms in the family talk.",
        tips=["Uchinchi shaxs -s: he/she/it **likes**. O'zbek tilida bunday qo'shimcha yo'q, shuning uchun "
              "doskada doimo qizil rangda yozing.",
              "'doesn't' dan keyin fe'l asl holatda: He doesn't **like** (likes emas). Bu eng keng tarqalgan xato.",
              "Support: sentence frames. Extension: add a reason with 'because' (oral)."],
    ),
    Lesson.std(
        title="Does he enjoy it?",
        focus="Grammar 2 — Does he / she …? Yes, he does. / No, he doesn't.",
        aims=["ask and answer yes / no questions: Does he enjoy doing the dishes?",
              "use short answers: Yes, he does. / No, she doesn't."],
        language=["Does he (enjoy) (doing the dishes)? — Yes, he does. / No, he doesn't.",
                  "Does she like (making cakes)?"],
        materials=["Activity cards (a picture + a thumb up/down)", "Chant from the audio", "Worksheet B exercises C–D"],
        greeting="Ask 'Does Anna like reading?' about a student, pointing to her. Elicit 'Yes, she does.'",
        warmup="**Yes / no cards**: hold up the 'does' and 'doesn't' cards as the class answers your questions.",
        present="Board table: Does he/she + verb …? → Yes, he/she does. / No, he/she doesn't. Show that after 'does' the "
                "verb is bare (enjoy, like). Drill with picture questions.",
        practice="Play the chant / Student's Book Grammar audio. Worksheet B exercises C (unscramble) and D (read and "
                 "answer).",
        produce="**Guess who it is**: a student chooses a famous person or a classmate; the class asks 'Does he like "
                "soccer?' (only yes/no answers) until they guess.",
        wrap="Teacher asks five quick questions about a picture family; students answer in chorus. Homework.",
        homework="Workbook grammar page; write four yes / no questions about a friend.",
        assessment="Listen for Does + bare verb and the correct short answer.",
        tips=["Savol shakli: **Does** + he/she + fe'l (asl holat). 'Does he likes' — eng ko'p xato; har safar "
              "to'g'rilab boring.",
              "Qisqa javob: Yes, he **does**. / No, he **doesn't**. Uzun javobni talab qilmang.",
              "Support: give a question frame. Extension: students ask 'Why?' and answer 'Because…'"],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "Ss-Ss / G", "T-Ss"),
    ),
    Lesson.std(
        title="Are you helpful at home?",
        focus="Skills: Listening — Are you helpful at home? + writing about a family",
        aims=["listen for what people do and do not like doing at home",
              "write four sentences about a family member"],
        language=["helpful · at home", "He / She likes … He / She doesn't like …"],
        materials=["Student's Book Listening page + audio", "Worksheet B exercise E", "picture cards of chores"],
        greeting="Ask 'Are you helpful at home?' and count the hands.",
        warmup="**Chore race**: two teams mime chores; the first to guess the phrase scores a point.",
        present="Pre-listening: look at the pictures, name chores. Play the audio twice: first for gist (who helps), "
                "then to check likes and dislikes.",
        practice="Check in pairs and with the class. Students read the Saturday text (Worksheet B exercise D) and find "
                 "who does what.",
        produce="Writing: using the help box, students write four sentences about a family member's likes and "
                "dislikes. Volunteers read aloud.",
        wrap="Students swap texts and check a sentence they like. Homework.",
        homework="Finish the text; add a drawing of the family.",
        assessment="Collect five texts: check -s, doesn't + verb, -ing forms.",
        tips=["Tinglash: rasmlarni avval nomlang — so'zlar eshitilganda tanish bo'ladi.",
              "Support: provide a cloze text. Extension: write what they do to help at home."],
        interactions=("T-Ss", "G", "T-Ss", "S / Ss-Ss", "S", "Ss-Ss"),
    ),
    Lesson.std(
        title="Say sorry, forgive",
        focus="Story value (show forgiveness), Talk time (suggesting food to make), Say it! th",
        aims=["follow the story and explain in simple words why we forgive friends",
              "suggest what to make: Let's make a cake! — Good idea! / No, let's make …",
              "pronounce /θ/ in three, panther, thank you"],
        language=["Let's make (a cake). — Good idea! / OK. / No, let's make (a salad).",
                  "Sound: th → /θ/ (three, panthers, thank you)"],
        materials=["Student's Book story + audio", "Student's Book Say it! page", "pictures of food"],
        greeting="Ask 'Do you say sorry when you're wrong?' Write **sorry / forgive** on the board.",
        warmup="**Say sorry**: pairs practice 'I'm sorry.' — 'That's OK.' with different situations.",
        present="Story: predict from the pictures, listen, answer 'Who is sorry? Who forgives?' Discuss in Uzbek, then "
                "conclude in English: 'Friends forgive.'",
        practice="Talk time: model 'Let's make a cake! — Good idea!', practice in open and closed pairs with food pictures. "
                 "Say it!: put your tongue between your teeth; repeat three / thank you / panther.",
        produce="**Class menu**: groups decide what to make for a class party using Let's… / Good idea!, then present "
                "their menu.",
        wrap="Chant the Say it! tongue twister. Homework.",
        homework="Workbook story page; suggest a meal to cook at home.",
        assessment="Listen for correct /θ/ and Let's … in the menu task.",
        tips=["'th' (/θ/) — til uchi tishlar orasida. O'zbek tilida bu tovush yo'q, ko'p bolalar 's' yoki 't' "
              "deyishadi ('sree', 'tree'). Ko'zgu bilan mashq qiling.",
              "'Let's' = 'Keling, …ylik'. 'Good idea!' — maqullash."],
        interactions=("T-Ss", "Ss-Ss", "T-Ss", "Ss-Ss", "G", "T-Ss"),
    ),
    Lesson.std(
        title="Where do people live?",
        focus="CLIL Geography — Where do people live?",
        aims=["name different places people live (city, village, mountains, desert)",
              "say: People live in (cities). Some people live in (tents)."],
        language=["city · village · mountains · desert · tent", "People live in (villages)."],
        materials=["Student's Book CLIL pages", "pictures of homes", "A4 paper and pencils"],
        greeting="Ask 'Do you live in a city or a village?' and count the answers.",
        warmup="**Where is it?** Show pictures of homes; students say 'city / village / mountains / desert'.",
        present="Compare homes around the world (apartment, house, yurt / tent, mountain house). Introduce the sentence "
                "frames.",
        practice="Student's Book CLIL activities. Students match people to places in a short table.",
        produce="**My home poster**: students draw their home and its surroundings and write one sentence.",
        wrap="Gallery walk: students read two classmates' posters. Homework.",
        homework="Ask an older relative where people lived in your area long ago.",
        assessment="Poster rubric: picture (1), sentence (1), neatness (1).",
        tips=["'yurt' — 'o'tov' (ko'chmanchi uyi) — o'zbek madaniyatiga bog'lang.",
              "Mahalliy misollar: Samarkand (city), a village in Khorezm, Chimgan mountains, Kyzylkum desert."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "S", "Ss-Ss"),
    ),
    Lesson.std(
        title="Unit 5 review and quiz",
        focus="Review of Unit 5; quick quiz",
        aims=["use home activities, likes / doesn't like and Does he…? accurately", "complete the unit quiz"],
        language=["All language from Unit 5"],
        materials=["Quiz (worksheets/quiz.pdf)", "Bingo (games/bingo.pdf)", "Flashcards"],
        greeting="Greet and set the goal: 'Show what you know about home time.'",
        warmup="**Bingo** with the ten home activities (8 different cards ready to print).",
        present="Mind-map on the board: activities, likes / doesn't like, Does he…?",
        practice="Pairs: Pairs game; then correct three wrong sentences (He don't like / Does he likes).",
        produce="Quiz (15 minutes, 20 points). Collect and mark with the key.",
        wrap="Go over common mistakes; praise progress.",
        homework="Correct your quiz mistakes.",
        assessment="Mark with the answer keys and record results.",
        tips=[GRADE_TIP_20, "Weak students: read instructions aloud. Extension: write five questions for a class survey."],
        interactions=("T-Ss", "Ss-Ss", "T-Ss", "Ss-Ss", "S", "T-Ss"),
    ),
]

A = [
    PicLabel("Look and write the phrases.", items=[
        ("juice", "drink juice"), ("sandwich", "eat a sandwich"), ("dishes", "do the dishes"),
        ("play computer", "play on the computer"), ("read", "read a book"), ("tv", "watch TV"),
        ("homework", "do homework"), ("music", "listen to music")], cols=4),
    Match("Match the English phrases to the Uzbek phrases.", pairs=[
        ("drink juice", "sharbat ichmoq"), ("read a book", "kitob o'qimoq"), ("watch TV", "televizor ko'rmoq"),
        ("do homework", "uy vazifasini bajarmoq"), ("wash the car", "mashinani yuvmoq"),
        ("make a cake", "tort tayyorlamoq")], seed=61),
    Gaps("Look and complete the words.", items=[
        ("juice", "juice"), ("sandwich", "sandwich"), ("computer", "computer"), ("homework", "homework"),
        ("cake", "cake"), ("music", "music")]),
    WordSearch("Find the words.", words=["juice", "sandwich", "dishes", "computer", "book", "music", "cake",
                                         "homework", "car"], size=11, seed=11),
    OddOne("Circle the odd one out.", rows=[
        (["juice", "sandwich", "cake", "computer"], "computer"),
        (["read", "watch", "listen", "sandwich"], "sandwich"),
        (["wash", "make", "cake", "do"], "cake")]),
    Draw("Draw your favorite home activity.", prompts=["I like ________ ."]),
]

B = [
    Circle("Circle the correct words.", items=[
        "Tom {*likes|like} reading books.",
        "Anna {*doesn't|don't} like washing the car.",
        "{*Does|Do} he enjoy doing the dishes?",
        "Yes, he {*does|do}.",
        "No, she {*doesn't|don't}.",
        "They {*like|likes} watching TV.",
        "He doesn't {*like|likes} playing on the computer."]),
    Fill("Complete the sentences with words from the box.", items=[
        "Karim {likes} watching TV.",
        "He {doesn't} like doing the dishes.",
        "{Does} she enjoy making cakes? — Yes, she {does}.",
        "My mom {enjoys} listening to music."], extra_words=["do"]),
    Unscramble("Put the words in the right order.", items=[
        "He doesn't like reading books.", "Does she enjoy making cakes?", "Yes, she does.", "No, he doesn't."]),
    Reading("Read and answer.", title="Saturday at home", text=(
        "Karim's family is busy on Saturday. Karim washes the car. His sister Malika does the dishes. "
        "She doesn't like doing the dishes, but she likes listening to music.\n\n"
        "Dad reads a book. Mom makes a cake. Karim enjoys making cakes too."), questions=[
        ("Does Karim wash the car?", "Yes, he does."),
        ("Does Malika like doing the dishes?", "No, she doesn't."),
        ("What does Dad do?", "He reads a book.")]),
    WriteAbout("Write about a person in your family.", frames=[
        "My ___ likes ___ing.", "He / She doesn't like ___ing.", "Does he / she enjoy ___ing? Yes / No."], lines=3,
        model=["My mom likes cooking. She doesn't like washing the car. Does she enjoy listening to music? "
               "Yes, she does."]),
]

QUIZ = [
    Section("Part 1 · Words", [
        PicLabel("Look and write the phrases.", items=[
            ("juice", "drink juice"), ("read", "read a book"), ("tv", "watch TV"), ("homework", "do homework"),
            ("cake", "make a cake"), ("car", "wash the car")], bank=False, cols=3, size=34)]),
    Section("Part 2 · Grammar", [
        Circle("Circle the correct word.", items=[
            "Tom {*likes|like} reading books.",
            "She {*doesn't|don't} like doing the dishes.",
            "{*Does|Do} he enjoy making cakes?",
            "Yes, he {*does|do}."]),
        Fill("Complete the sentences.", items=[
            "Malika {likes} listening to music.",
            "He {doesn't} like washing the car.",
            "{Does} she enjoy doing homework? — No, she doesn't.",
            "They {enjoy} playing on the computer."], extra_words=["do"])]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="Dad's day", text=(
            "Dad likes cooking. He makes a cake on Sundays. He doesn't like washing the car. "
            "He enjoys listening to music."), questions=[
            ("Does Dad like cooking?", "Yes, he does."),
            ("Does Dad like washing the car?", "No, he doesn't."),
            ("What does he enjoy?", "Listening to music.")]),
        Unscramble("Put the words in the right order.", items=[
            "Does he enjoy reading?", "She doesn't like cooking.", "Yes, he does."])]),
]

SPEC = UnitSpec(number=5, slug="unit-5-home-time", title="Home time", info=INFO, vocab=VOCAB, extra_vocab=EXTRA,
                lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="Home activities", sheet_b_name="likes / doesn't like, Does he…? reading, writing")
