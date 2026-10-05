"""Guess What! Level 3 · Unit 8 — At the beach."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, OddOne, PicLabel, Reading, Section, Unscramble, WordSearch, WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.unit import UnitSpec, V

from .common import BADGE, GRADE_TIP_20

VOCAB = [
    V("sun", "quyosh", "sun"),
    V("burger", "burger", "burger"),
    V("fries", "kartoshka fri", "fries"),
    V("sunglasses", "quyoshdan saqlovchi ko'zoynak", "sunglasses"),
    V("swimsuit", "cho'milish kiyimi", "swimsuit"),
    V("shorts", "shortik (kalta shim)", "shorts"),
    V("towel", "sochiq", None),
    V("shell", "chig'anoq", "shell"),
    V("ocean", "okean", "ocean"),
    V("sand", "qum", "sand"),
]

EXTRA = [
    V("mine", "meniki", None), V("yours", "seniki, sizniki", None), V("his", "uniki (erkak)", None),
    V("hers", "uniki (ayol)", None), V("ours", "bizniki", None), V("theirs", "ularniki", None),
    V("purple", "binafsha", None), V("the purple one", "binafsha rangdagisi", None),
]

INFO = UnitInfo(
    number=8, title="At the beach", topic="Beach things; whose things are these",
    vocabulary="sun, burger, fries, sunglasses, swimsuit, shorts, towel, shell, ocean, sand",
    grammar=["Which (towel) is (theirs)? The (purple) one.",
             "Whose (jacket) is this? It's (mine). Whose (shoes) are these? They're (Sally's)."],
    skills="Reading: What do you like doing on vacation?",
    phonics="ph / f — dolphins, fish",
    story_value="Appreciate your family and friends",
    talk_time="Deciding how to travel",
    clil="Math — Are ocean animals symmetrical?",
    review="Review Units 7 and 8 (and the Chants pages)",
)

LESSONS = [
    Lesson.std(
        title="Beach words",
        focus="Vocabulary — ten things at the beach",
        aims=["name ten beach words", "say what they can see or have at the beach: I have sunglasses."],
        language=["sun, burger, fries, sunglasses, swimsuit, shorts, towel, shell, ocean, sand"],
        materials=["Flashcards", "Student's Book Vocabulary page + audio", "Worksheet A exercises A–B"],
        greeting="Greet the class and ask 'Do you like the beach or the mountains?' Write **At the beach** on the board.",
        warmup="**Pack your bag**: students say 'In my bag there's a towel' and add one more item each, chain-style (use "
               "the words learned so far).",
        present="Present the ten words with flashcards and gestures (put on sunglasses, wave for the ocean). Note "
                "'shorts' and 'sunglasses' are always plural. Student's Book: *Listen and point*, *Listen, point and "
                "repeat*.",
        practice="Worksheet A exercises A (label) and B (match with Uzbek). **What's missing?** and **Slow reveal**.",
        produce="**I spy at the beach**: pairs — 'I spy with my little eye something yellow.' Partner guesses 'sun!' "
                "Use a beach scene drawn on the board.",
        wrap="Teacher says a word; students hold up the right card. Homework.",
        homework="Learn the words and draw a beach picture with five labels (Worksheet A exercise F).",
        assessment="Point at cards for 5 students; note gaps.",
        tips=["'shorts', 'sunglasses' — har doim ko'plikda ('a shorts' emas). O'zbekchada ham 'ko'zoynak' birlikda, "
              "inglizchada esa ko'plik — diqqat bering.",
              "'fries' — qovurilgan kartoshka (britaniyacha 'chips'). 'ocean' — okean ('sea' — dengiz); plyaj haqida gapirganda 'ocean'.",
              "Support: picture-only cards. Extension: add colors to each item."],
    ),
    Lesson.std(
        title="Whose is it?",
        focus="Grammar 1 — Whose … is this / are these? It's mine. They're Bobur's.",
        aims=["ask and answer: Whose jacket is this? It's mine. Whose shoes are these? They're Bobur's.",
              "use possessive 's and mine, yours, his, hers, ours, theirs"],
        language=["Whose (jacket) is this? — It's (mine).", "Whose (shoes) are these? — They're (Bobur's).",
                  "mine · yours · his · hers · ours · theirs"],
        materials=["Real items (a jacket, shoes, a bag) or pictures", "Student's Book Grammar page 1",
                   "Worksheet B exercises A–B"],
        greeting="Hold up a student's bag: 'Whose bag is this?' Wait for 'It's mine!' or 'It's Aziz's.'",
        warmup="**Lost property**: collect five items on a table; ask 'Whose is this?' and return them with 'It's yours!'",
        present="Model with real items: 'Whose jacket is this? It's Anna's. It's hers.' Write the pattern and a mini table: "
                "my → mine, your → yours, his → his, her → hers, our → ours, their → theirs. Teach 's for one "
                "owner: Bobur's.",
        practice="Student's Book Grammar activities. Worksheet B exercises A (circle) and B (fill in).",
        produce="**Lost and found role-play**: one student is the teacher with items; others claim them: 'Whose shoes are "
                "these?' — 'They're mine!'",
        wrap="Quick-fire: point at items in the room and ask 'Whose is it?' Homework.",
        homework="Workbook grammar page; write five sentences about things in your bag.",
        assessment="Check mine / yours / his / hers and 's.",
        tips=["'mine' = 'meniki', 'yours' = 'seniki', 'his/hers' = 'uniki' — o'zbek tilida -niki qo'shimchasi "
              "shu ma'noni beradi. Bu o'xshashlikni ko'rsating.",
              "'Bobur's' — egalik 's. Ko'plik -s bilan adashtirmang: boys (ko'plik) va boy's (egalik).",
              "Support: use real items. Extension: add 'because' (oral)."],
    ),
    Lesson.std(
        title="Which one is theirs?",
        focus="Grammar 2 — Which towel is theirs? The purple one.",
        aims=["ask and answer: Which towel is theirs? The purple one.",
              "use color + one to point at a thing"],
        language=["Which (towel) is (theirs)? — The (purple) one.", "the red one · the blue one · the yellow one"],
        materials=["Colored paper 'towels' in different colors", "Chant from the audio", "Worksheet B exercises C–D"],
        greeting="Hold up three colored papers: 'Which one is mine?' Elicit 'The red one.'",
        warmup="**Color flash**: hold up a color; students say the color and 'one': 'The blue one!'",
        present="Stick three towels on the board with owners (Anna, the boys, Mom and Dad). Model: 'Which towel is "
                "theirs? The yellow one.' Write the pattern and color theirs / one.",
        practice="Play the chant / Student's Book Grammar audio. Worksheet B exercises C (unscramble) and D (read and "
                 "answer).",
        produce="**Beach picture dictation**: pairs — A describes a beach scene ('The red towel is hers.'), B draws "
                "and colors it; compare.",
        wrap="Teacher points at a towel; students say whose it is. Homework.",
        homework="Workbook grammar page; draw three towels and write whose they are.",
        assessment="Check color + one and possessive pronouns in the dictation.",
        tips=["'one' — oldingi otni takrorlamaslik uchun: 'the purple towel' → 'the purple **one**'. O'zbekchada "
              "takrorlamaslik oddiy, inglizchada 'one' kerak.",
              "Support: give color words on the board. Extension: add 'and the blue one is mine.'"],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "Ss-Ss", "T-Ss"),
    ),
    Lesson.std(
        title="What do you like doing on vacation?",
        focus="Skills: Reading and writing — a vacation text and a postcard",
        aims=["read a short text about a vacation and answer questions", "write a short postcard"],
        language=["vacation · postcard · Dear … · Love, …", "I like swimming. / We're at the beach."],
        materials=["Student's Book Reading page", "Worksheet B exercise E (postcard)", "postcard template"],
        greeting="Ask 'Where do you go on vacation?' and collect answers on the board.",
        warmup="**Vacation charades**: mime vacation activities (swimming, eating, sunbathing); the class guesses.",
        present="Before reading: look at the pictures and predict. Read aloud once while students underline the activities. "
                "Check new words with pictures.",
        practice="Silent reading and questions (Student's Book, then Worksheet B exercise D). Check in pairs.",
        produce="Writing: students write a postcard using the frame in Worksheet B exercise E and decorate it.",
        wrap="Post the postcards on a class 'vacation wall' and read two aloud. Homework.",
        homework="Finish the postcard; send one to a family member.",
        assessment="Collect five postcards; check Dear / Love, capital letters and the structures of the unit.",
        tips=["Otkritka formatini ko'rsating: Dear … (yuqorida), Love, … (pastda). Bu real hayotiy ko'nikma.",
              "Support: gapped model postcard. Extension: add one sentence with 'but'."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "S", "Ss-Ss"),
    ),
    Lesson.std(
        title="Family and friends",
        focus="Story value (appreciate your family and friends), Talk time (deciding how to travel), Say it! ph / f",
        aims=["follow the story and say why we appreciate family and friends",
              "decide how to travel: Shall we go by bus? — Let's go by car!",
              "pronounce /f/ in dolphin, fish, phone, fun"],
        language=["Shall we go by (bus)? — Good idea! / No, let's go by (car).", "Sound: ph / f → /f/ (dolphins, fish)"],
        materials=["Student's Book story + audio", "Student's Book Say it! page", "transport flashcards"],
        greeting="Ask 'Who is your best friend? Why?' and write **friends and family** on the board.",
        warmup="**Thank you cards**: students draw a quick card for a friend and say 'Thank you for being my friend.'",
        present="Story: predict from pictures, listen, answer 'What do the friends do? How do they feel?' Discuss "
                "appreciation in Uzbek, then conclude in English: 'Love your family and friends.'",
        practice="Talk time: model 'Shall we go by bus?', practice with transport cards in open and closed pairs. Say it!: "
                 "listen, repeat, find more f / ph words.",
        produce="**Trip planner**: groups decide how to travel to a beach (bus, car, train, plane) using the new phrases "
                "and present their decision.",
        wrap="Chant the Say it! tongue twister. Homework.",
        homework="Workbook story page; plan a family trip in English.",
        assessment="Listen for Shall we …? and accepting / refusing politely.",
        tips=["'by bus / by car / by train' — 'by' + transport (artikelsiz). 'on foot' — piyoda.",
              "/f/ o'zbekcha 'f' — qiyinchilik yo'q; 'ph' harf birikmasi ham /f/ beradi (phone, dolphin)."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "Ss-Ss", "G", "T-Ss"),
    ),
    Lesson.std(
        title="Symmetry in the ocean",
        focus="CLIL Math — Are ocean animals symmetrical?",
        aims=["say what symmetrical means and find symmetrical shapes",
              "say: A starfish is symmetrical. A shell is / isn't symmetrical."],
        language=["symmetrical · line of symmetry · the same on both sides", "It is / isn't symmetrical."],
        materials=["Student's Book CLIL pages", "paper, scissors, crayons", "pictures of a butterfly, starfish, fish, shell"],
        greeting="Fold a paper heart and cut it: 'Look — both sides are the same!'",
        warmup="**Mirror game**: pairs copy each other's movements like a mirror.",
        present="Explain symmetry: fold a picture in half — if both halves match, it is symmetrical. Show ocean animal "
                "pictures and test them with folded paper or a mirror line.",
        practice="Student's Book CLIL activities; students draw the line of symmetry on pictures.",
        produce="**Symmetry art**: fold paper, paint on one side, press and open — label 'It's symmetrical.'",
        wrap="Gallery walk: students say whether each art piece is symmetrical. Homework.",
        homework="Find three symmetrical things at home.",
        assessment="Check line-of-symmetry drawings (4 pictures).",
        tips=["'symmetrical' — 'simmetrik'. Ikki tomoni bir xil — Navro'z naqshlari, atlas, gilam naqshlarida "
              "ko'p uchraydi: mahalliy misollar keltiring.",
              "Support: pre-folded paper. Extension: draw own symmetrical ocean animal."],
        interactions=("T-Ss", "Ss-Ss", "T-Ss", "S / Ss-Ss", "S", "Ss-Ss"),
    ),
    Lesson.std(
        title="Unit 8 review and quiz",
        focus="Review of Unit 8; quick quiz",
        aims=["use beach vocabulary, Whose / Which and possessive pronouns accurately", "complete the unit quiz"],
        language=["All language from Unit 8"],
        materials=["Quiz (worksheets/quiz.pdf)", "Bingo (games/bingo.pdf)", "Flashcards"],
        greeting="Greet and set the goal: 'Show what you know about the beach.'",
        warmup="**Bingo** with the ten beach words (8 different cards ready to print).",
        present="Mind-map on the board: beach words, whose / which, mine – yours – his – hers – ours – theirs.",
        practice="Pairs: Pairs game; correct three wrong sentences (It's my / Whose shoes is this?).",
        produce="Quiz (15 minutes, 20 points). Collect and mark with the key.",
        wrap="Go over common mistakes; praise progress.",
        homework="Correct your quiz mistakes.",
        assessment="Mark with the answer keys and record results.",
        tips=[GRADE_TIP_20, "Weak students: read instructions aloud. Extension: write a postcard from the beach."],
        interactions=("T-Ss", "Ss-Ss", "T-Ss", "Ss-Ss", "S", "T-Ss"),
    ),
    Lesson.std(
        title="Review: Units 7 and 8 and Chants",
        focus="Student's Book Review pages for Units 7 and 8; chants",
        aims=["recycle Unit 7 and Unit 8 language in games and puzzles",
              "perform the course chants with confidence"],
        language=["Unit 7 and Unit 8 language"],
        materials=["Student's Book Review (Units 7 and 8) + audio", "Chants pages (end of the book)",
                   "Workbook review pages"],
        greeting="Greet the class and explain that today is the last review of the year with games and chants.",
        warmup="**Two-unit quiz show**: two teams answer quick questions from both units.",
        present="Go through the Review page instructions and model one item of each type.",
        practice="Students do the Review activities in pairs (listening / speaking / games). Monitor and note errors.",
        produce="**Chant concert**: groups perform one chant each with actions for the class.",
        wrap="Students write what they are proud of in English this year. Homework.",
        homework="Workbook review pages.",
        assessment="Observation checklist: there are / any, whose / which, possessive pronouns; chant performance.",
        tips=["Bu dars yakuniy (4-chorak) nazorat ishiga tayyorgarlik sifatida ham ishlaydi.",
              "Support: give the chant text to read along. Extension: students create a new verse."],
        interactions=("T-Ss", "G", "T-Ss", "Ss-Ss", "G", "T-Ss"),
    ),
]

A = [
    PicLabel("Look and write the words.", items=[
        ("sun", "sun"), ("burger", "burger"), ("fries", "fries"), ("sunglasses", "sunglasses"),
        ("swimsuit", "swimsuit"), ("shorts", "shorts"), ("shell", "shell"), ("ocean", "ocean")], cols=4),
    Match("Match the English words to the Uzbek words.", pairs=[
        ("sun", "quyosh"), ("sand", "qum"), ("ocean", "okean"), ("shell", "chig'anoq"),
        ("towel", "sochiq"), ("shorts", "shortik")], seed=91),
    Gaps("Look and complete the words.", items=[
        ("sunglasses", "sunglasses"), ("swimsuit", "swimsuit"), ("shorts", "shorts"), ("shell", "shell"),
        ("burger", "burger"), ("fries", "fries")]),
    WordSearch("Find the beach words.", words=["burger", "fries", "sunglasses", "swimsuit", "shorts", "towel",
                                               "shell", "ocean", "sand"], size=12, seed=14),
    OddOne("Circle the odd one out.", rows=[
        (["sun", "sand", "ocean", "burger"], "burger"),
        (["shorts", "swimsuit", "sunglasses", "fries"], "fries"),
        (["burger", "fries", "shell", "sandwich"], "shell")]),
    Draw("Draw a beach. Label five things.", prompts=["At the beach"]),
]

B = [
    Circle("Circle the correct words.", items=[
        "Whose jacket is this? — It's {*mine|my}.",
        "Whose shoes are these? — They're {*Aziz's|Aziz}.",
        "That is Anna's bag. It's {*hers|her}.",
        "Those are Tom's shorts. They're {*his|he}.",
        "Which towel is {*theirs|their}? — The purple one.",
        "This is our umbrella. It's {*ours|our}."]),
    Fill("Complete the sentences.", items=[
        "{Whose} jacket is this? — It's mine.",
        "{Whose} shoes are these? — They're Bobur's.",
        "Which towel is {theirs}? — The purple one.",
        "That bag is Malika's. It's {hers}."], extra_words=["his"]),
    Unscramble("Put the words in the right order.", items=[
        "Whose jacket is this?", "It's mine.", "Which towel is theirs?", "The purple one."]),
    Reading("Read and answer.", title="A day at the beach", text=(
        "It is hot and sunny. Dilnoza and her family are at the beach. There are three towels. The red towel is "
        "Dilnoza's. It's hers. The blue towel is her brother's. It's his.\n\n"
        "The yellow towel is Mom and Dad's. It's theirs. Dilnoza has sunglasses and a shell. The shell is hers, "
        "but the sunglasses are Dad's."), questions=[
        ("Whose is the red towel?", "It's Dilnoza's. It's hers."),
        ("Which towel is theirs?", "The yellow one."),
        ("Whose are the sunglasses?", "They're Dad's.")]),
    WriteAbout("Write a postcard from the beach.", frames=[
        "Dear ___ ,", "I'm at the beach. The ocean is ___ . I have ___ .", "My towel is the ___ one.",
        "Love, ___"], lines=4,
        model=["Dear Grandma, I'm at the beach. The ocean is blue. I have sunglasses and a shell. "
               "My towel is the green one. Love, Dilnoza"]),
]

QUIZ = [
    Section("Part 1 · Words", [
        PicLabel("Look and write the words.", items=[
            ("sun", "sun"), ("sunglasses", "sunglasses"), ("swimsuit", "swimsuit"), ("shorts", "shorts"),
            ("shell", "shell"), ("ocean", "ocean")], bank=False, cols=3, size=34)]),
    Section("Part 2 · Grammar", [
        Circle("Circle the correct word.", items=[
            "Whose jacket is this? — It's {*mine|my}.",
            "That is Lily's towel. It's {*hers|her}.",
            "Which towel is {*theirs|their}? — The blue one.",
            "Whose shoes are these? — They're {*Tom's|Tom}."]),
        Fill("Complete the sentences.", items=[
            "{Whose} bag is this? — It's mine.",
            "This is our umbrella. It's {ours}.",
            "Which towel is {yours}? — The red one.",
            "Those are Max's shorts. They're {his}."], extra_words=["hers"])]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="On the sand", text=(
            "There are two towels on the sand. The green one is Lily's. It's hers. The purple one is Tom's. "
            "It's his. There are sunglasses next to the purple towel. They're Tom's too."), questions=[
            ("Whose is the green towel?", "It's Lily's. It's hers."),
            ("Which towel is Tom's?", "The purple one."),
            ("Whose are the sunglasses?", "They're Tom's.")]),
        Unscramble("Put the words in the right order.", items=[
            "Whose shoes are these?", "They're mine.", "The purple one is hers."])]),
]

SPEC = UnitSpec(number=8, slug="unit-8-at-the-beach", title="At the beach", info=INFO, vocab=VOCAB,
                extra_vocab=EXTRA, lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="Beach words", sheet_b_name="Whose…? Which…? mine, yours, his, hers")
