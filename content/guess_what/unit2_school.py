"""Guess What! Level 3 · Unit 2 — At school."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, OddOne, PicLabel, Reading, Section, Unscramble, WordSearch, WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.unit import UnitSpec, V

from .common import BADGE, GRADE_TIP_20

VOCAB = [
    V("reception", "qabulxona", "reception"),
    V("dining hall / cafeteria", "oshxona, ovqatlanish zali", "dining hall", ws="dining"),
    V("library", "kutubxona", "library"),
    V("classroom", "sinf xonasi", "classroom"),
    V("Science room / lab", "fan (tabiiy fanlar) xonasi", "science room", ws="science"),
    V("gym", "sport zali", "gym"),
    V("Art room", "tasviriy san'at xonasi", "art room"),
    V("Music room", "musiqa xonasi", "music room", ws="music"),
    V("playground", "o'yin maydonchasi", "playground"),
    V("sports field", "sport maydoni", "sports field"),
]

EXTRA = [
    V("reading", "o'qimoqda", "read"), V("singing", "kuylamoqda", "sing"),
    V("painting", "rasm chizmoqda", "paint"), V("running", "yugurmoqda", "run"),
    V("paper", "qog'oz", "paper"), V("plastic", "plastmassa", "bottle"),
    V("glass", "shisha", "jar"), V("metal", "metall", "can"),
]

INFO = UnitInfo(
    number=2, title="At school", topic="Places in school; what people are doing now",
    vocabulary="reception, dining hall, library, classroom, Science room, gym, Art room, Music room, playground, "
               "sports field",
    grammar=["Where are (they)? (They)'re (on the sports field).",
             "What are (you) doing? (We)'re (playing baseball)."],
    skills="Reading: What places can you find in your school?",
    phonics="i / igh — tigers, night",
    story_value="Keep your environment clean",
    talk_time="Offering help",
    clil="Science — What materials can we recycle?",
    review="Review Units 1 and 2",
)

LESSONS = [
    Lesson.std(
        title="Places in school",
        focus="Vocabulary — ten school places",
        aims=["name ten places in a school", "say where people usually are: You read in the library"],
        language=["reception, dining hall, library, classroom, Science room, gym, Art room, Music room, "
                  "playground, sports field", "This is the … / You (read) in the …"],
        materials=["Flashcards", "Student's Book Vocabulary page + audio", "Worksheet A (exercises A–B)",
                   "Plan of your school drawn on the board"],
        greeting="Greet the class. Ask 'Where are we now?' — 'We're in the classroom.' Write **At school** on the board.",
        warmup="**Walk and talk**: take the class on a two-minute walk around the corridor or draw the school plan on the "
               "board and ask 'What's this place?' — pupils say it in Uzbek, you give the English word.",
        present="Stick the flashcards on the school plan. Teach each place with an action or sound (library = finger on lips, "
                "gym = lift arms, music room = sing). Choral and individual repetition. Student's Book: *Listen, point "
                "and repeat*.",
        practice="**What's missing?** and **Slow reveal** with the cards; then Worksheet A exercise A (label the pictures) "
                 "and B (match the sentences to the places) in pairs.",
        produce="**Guess the place**: one pupil mimes an activity (reading, eating, painting), the class asks 'Are you in "
                "the library?' (yes / no) until they guess.",
        wrap="Race: two teams write as many school places as they can on the board in one minute.",
        homework="Learn the ten words and draw your dream school with five labelled places (Worksheet A, exercise F).",
        assessment="Check which pupils can name all places without looking (board-race score).",
        tips=["'dining hall' (Britaniya) va 'cafeteria' (AQSh) — bir xil joy. 'Science room' = 'science lab'.",
              "O'zbek maktablarida 'oshxona' (ovqatlanish xonasi) — 'dining hall' ga mos keladi.",
              "Support: pupils match picture to word first. Extension: add 'Where do you …?' questions."],
    ),
    Lesson.std(
        title="Where are they?",
        focus="Grammar 1 — Where are they? They're in / on the …",
        aims=["ask and answer: Where are they? They're on the sports field",
              "choose in or on correctly: in the library, on the playground"],
        language=["Where are (they)? — They're (on the sports field).", "in the (library) · on the (playground)"],
        materials=["Flashcards on the school plan", "Student's Book Grammar page 1", "Worksheet B, exercise A"],
        greeting="Ask 'Where is Aziz?' (pointing at an absent pupil's seat) — 'He's not here.' Introduce 'Where is / "
                 "are…?'",
        warmup="Play **Hide the card**: hide a flashcard behind a pupil; class asks 'Is it in the library?' until they guess.",
        present="Put two or three name cards (Anna, Tom, Lily) on the plan. Say: 'Where are Tom and Lily? They're in the "
                "gym.' Show the pattern on the board with colours: **in** + closed room (classroom, library, gym), **on** + "
                "outdoor area (playground, sports field). Drill with picture cards.",
        practice="Student's Book Grammar exercises. Worksheet B, exercise A — do items 1–2 together, rest alone, then "
                 "check in pairs.",
        produce="**Where are they?** Pairs: pupil A holds a picture of children in a school place, pupil B asks "
                "'Where are they?' and A answers 'They're in/on …'. Swap cards and repeat.",
        wrap="Teacher points to a place on the plan; pupils chorus 'They're in the …'. Homework.",
        homework="Activity Book grammar page; write three sentences: Where are your family now? (in / at home, at work).",
        assessment="Listen for correct in / on in the pair work; note who uses them confidently.",
        tips=["O'zbek tilida joylashuv qo'shimchalari (-da) bir xil; inglizchada esa **in / on / at** ajratiladi. "
              "Oddiy qoida: yopiq xona → in; ochiq maydon → on.",
              "'They're' → 'they are'. Kichik doskada 'they + are' deb yozib ko'rsating.",
              "Support: colour-code in (blue) and on (green). Extension: add 'near / next to'."],
    ),
    Lesson.std(
        title="What are you doing?",
        focus="Grammar 2 — present continuous: What are you doing? We're playing baseball",
        aims=["ask and answer: What are you doing? I'm reading / We're playing",
              "form -ing verbs (reading, playing, running, painting)"],
        language=["What are (you) doing? — (We)'re (playing baseball).", "I'm / He's / She's / We're / They're + verb-ing",
                  "reading, singing, painting, running, playing"],
        materials=["Action cards (draw or use flashcards)", "Chant from the audio", "Worksheet B exercises B–C"],
        greeting="Ask five pupils 'What are you doing now?' — 'I'm sitting. I'm listening.'",
        warmup="**Simon says** with -ing: 'Simon says: you're jumping!' Pupils act and say 'I'm jumping.'",
        present="Mime reading and say 'I'm reading.' Write am/is/are + -ing on the board; show the five subject forms. "
                "Point out the spelling of running (double n) — practise on the board. Mime three actions and ask "
                "'What am I doing?'",
        practice="Play the chant / Student's Book Grammar audio; do the action drill. Worksheet B, exercises B and C.",
        produce="**Mime and guess** in groups of four: one pupil mimes, others ask 'Are you playing football?' / "
                "'What are you doing?' — use both question forms.",
        wrap="Pupils stand; you say 'Everybody is singing!' — they sing and say 'We're singing.' Homework.",
        homework="Write five sentences about what people in your family are doing now.",
        assessment="Check am/is/are agreement: write three wrong sentences on the board and ask pupils to fix them.",
        tips=["'-ing' shakli o'zbek tilidagi '-yapti / -moqda' ga o'xshaydi: 'o'qiyapman' = 'I'm reading'. Bu "
              "o'xshashlikdan foydalaning.",
              "Ko'p xato: 'I reading' (am tushib qoladi). Har safar 'I'm' ni baland ovoz bilan ayting.",
              "Support: give a sentence frame 'I'm ___ing'. Extension: negative 'I'm not running.'"],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "G", "T-Ss"),
    ),
    Lesson.std(
        title="Places in our school",
        focus="Skills: Reading and writing — What places can you find in your school?",
        aims=["read a short text about a school and answer questions",
              "write three sentences about their own school"],
        language=["Our school has a … and a … · At break time we're …", "There is/are is not needed yet — use 'has'"],
        materials=["Student's Book Reading page", "Worksheet B, exercises E–F", "highlighters or coloured pencils"],
        greeting="Ask 'What places are there in our school?' Brainstorm quickly on the board.",
        warmup="**Word snake**: write a long string of school words without spaces on the board; pupils separate them.",
        present="Before reading: look at the text's pictures and predict. Read aloud once while pupils underline the school "
                "places they know. Check meaning of any unknown words with pictures.",
        practice="Pupils read again silently and complete the comprehension questions (Student's Book, then Worksheet B "
                 "exercise E). Check in pairs, then whole class.",
        produce="Writing: pupils write three sentences about their school using the help box in Worksheet B exercise F. "
                "Volunteers read theirs aloud.",
        wrap="Swap texts: each pupil ticks one good sentence in a friend's text and adds a smiley. Homework.",
        homework="Finish the writing; bring a photo or drawing of a place in your school.",
        assessment="Collect five texts; look for school words, present continuous and capital letters.",
        tips=["Matn o'qishdan oldin rasmlarni ko'rib, taxmin qiling — bu tushunishni osonlashtiradi.",
              "Yozuv: 'Our school has a library.' — 'has' (bitta narsa) va 'have' (ko'p) farqini ko'rsating.",
              "Support: give a gapped model text. Extension: add two sentences about what people are doing."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "S", "Ss-Ss"),
    ),
    Lesson.std(
        title="Keep it clean",
        focus="Story value (keep your environment clean), Talk time (offering help), Say it! i / igh",
        aims=["follow the story and say why we should keep the school clean",
              "offer and accept help: Can I help you? — Yes, please. / No, thank you.",
              "pronounce /aɪ/ in tiger, night, light, like"],
        language=["Can I help you? — Yes, please. / No, thank you.", "Sound: i / igh → /aɪ/ (tiger, night, light)"],
        materials=["Student's Book story + audio", "Student's Book Say it! page", "a bin and some scrap paper"],
        greeting="Drop a piece of paper on the floor and ask 'Is this OK?' Discuss in Uzbek, then 'Keep our school clean!'",
        warmup="**Clean-up race**: two teams throw scrap paper into a bin, saying 'Clean, clean, clean!'",
        present="Story: predict from pictures, listen and follow, answer 'Who helps? Who is not helping?' Discuss the "
                "value and conclude in English: 'We keep our school clean.'",
        practice="Talk time: model 'Can I help you?'; practise in open pairs, then closed pairs with real tasks "
                 "(carry a bag, open a door). Say it!: listen, repeat, then brainstorm more i / igh words.",
        produce="**Helpers**: pairs invent a two-line dialogue where one offers help and the other accepts or refuses "
                "politely, then act it out.",
        wrap="Class chant of the Say it! tongue twister. Homework.",
        homework="Activity Book story page; help someone at home and say 'Can I help you?'",
        assessment="Listen for Can I help you? and polite answers in the pair work.",
        tips=["/aɪ/ tovushi o'zbekcha 'ay' ga yaqin. 'night' ni 'nayt' deb mashq qiling, 'g' aytilmaydi.",
              "Tozalik mavzusini maktab hayotiga bog'lang: 'Keling, sinfimizni toza saqlaymiz.'"],
        interactions=("T-Ss", "G", "T-Ss", "Ss-Ss", "Ss-Ss", "T-Ss"),
    ),
    Lesson.std(
        title="Recycle it!",
        focus="CLIL Science — What materials can we recycle?",
        aims=["name four recyclable materials: paper, plastic, glass, metal",
              "say what can be recycled: We can recycle paper"],
        language=["paper · plastic · glass · metal · recycle", "We can recycle (paper). / It's made of (glass)."],
        materials=["Student's Book CLIL pages", "real objects (a can, a plastic bottle, paper, a jar) or pictures",
                   "four boxes or bags labelled with the materials"],
        greeting="Hold up an empty bottle: 'What is it? Is it rubbish?' Introduce 'recycle'.",
        warmup="**Sort it!** Pupils put real objects into the four labelled boxes and say 'It's paper.'",
        present="Explain the recycling symbol and the four materials with real objects. Write 'We can recycle paper, "
                "plastic, glass and metal.' on the board.",
        practice="Student's Book CLIL activities (watch / match). Pupils complete a short sorting table in their notebooks.",
        produce="**Recycling poster** in groups: title 'Please recycle!', pictures of four materials, one sentence for "
                "each. Display around the classroom.",
        wrap="Each group reads one sentence; class holds up the correct material object.",
        homework="Bring one item that can be recycled (clean) for the class recycling box.",
        assessment="Poster rubric: four materials (1), sentences (1), neat work (1).",
        tips=["'recycle' — 'qayta ishlash'. O'zbekistondagi 'chiqindini saralash' tashabbuslariga bog'lang.",
              "Xavfsizlik: faqat toza, o'tkir qirrasiz buyumlar olib kelinsin (shisha emas, plastik/qog'oz)."],
        interactions=("T-Ss", "G", "T-Ss", "S / Ss-Ss", "G", "T-Ss"),
    ),
    Lesson.std(
        title="Unit 2 revision and quiz",
        focus="Revision of Unit 2; quick quiz",
        aims=["use school vocabulary and present continuous accurately", "complete the unit quiz"],
        language=["All language from Unit 2"],
        materials=["Quiz (worksheets/quiz.pdf)", "Bingo cards (games/bingo.pdf)", "Flashcards"],
        greeting="Greet and set the goal: 'Today we show what we know about our school.'",
        warmup="**Bingo** with the ten school places (8 different cards ready to print).",
        present="Mind-map on the board: school places, in / on, am/is/are + -ing. Pupils add one example each.",
        practice="Pairs: Pairs (memory) game; then 'spot the mistake' (three wrong sentences on the board).",
        produce="Quiz (15 minutes, 20 points). Collect and mark with the key.",
        wrap="Share the most common mistakes and correct them together. Praise progress.",
        homework="Correct your quiz mistakes.",
        assessment="Mark the quiz with the answer keys; note pupils to support before the quarter test.",
        tips=[GRADE_TIP_20,
              "Weak pupils: read instructions aloud. Extension: write three sentences about a friend who is in "
              "the library now."],
        interactions=("T-Ss", "Ss-Ss", "T-Ss", "Ss-Ss", "S", "T-Ss"),
    ),
    Lesson.std(
        title="Review: Units 1 and 2",
        focus="Student's Book Review pages for Units 1 and 2",
        aims=["recycle Unit 1 and Unit 2 language in games and puzzles",
              "show confidence with possessives, that/those, in/on and present continuous"],
        language=["Unit 1 and Unit 2 language"],
        materials=["Student's Book Review (Units 1 and 2) + audio", "Activity Book review pages",
                   "Flashcards from both units"],
        greeting="Greet the class and explain that today is a mixed review with games.",
        warmup="**Two-unit quiz show**: two teams answer quick questions from both units (What's that? Where are they?).",
        present="Go through the Review page instructions and model one item of each activity type.",
        practice="Pupils do the Review activities in pairs (listening / word puzzles / speaking). Monitor and note errors.",
        produce="Play the board game from the Review page, using the target questions each time a pupil lands on a "
                "square.",
        wrap="Pupils write one thing they are good at and one thing to practise. Homework.",
        homework="Activity Book review pages.",
        assessment="Observation checklist: possessives, that/those, in/on, -ing forms.",
        tips=["Bu dars chorak nazorat ishiga tayyorgarlik sifatida ham ishlaydi (test-1 ga qarang).",
              "Support: pair weaker pupils with stronger ones. Extension: write their own review questions."],
        interactions=("T-Ss", "G", "T-Ss", "Ss-Ss", "G", "T-Ss"),
    ),
]

A = [
    PicLabel("Look and write the places.", items=[
        ("reception", "reception"), ("dining hall", "dining hall"), ("library", "library"),
        ("classroom", "classroom"), ("science room", "science room"), ("gym", "gym"),
        ("art room", "art room"), ("playground", "playground")], cols=4),
    Match("Match the sentences to the places.", pairs=[
        ("You read books here.", "library"), ("You eat lunch here.", "dining hall"),
        ("You play on the slide here.", "playground"), ("You run races and play football here.", "sports field"),
        ("You paint pictures here.", "art room"), ("You sing songs here.", "music room"),
        ("You do experiments here.", "science room"), ("You do gymnastics here.", "gym")], seed=21),
    Gaps("Look and complete the words.", items=[
        ("library", "library"), ("classroom", "classroom"), ("playground", "playground"),
        ("reception", "reception"), ("science room", "science"), ("music room", "music")]),
    WordSearch("Find the school words.", words=["library", "classroom", "playground", "gym", "reception",
                                                "science", "music", "dining"], size=11, seed=8),
    OddOne("Circle the odd one out.", rows=[
        (["library", "classroom", "sunflower", "gym"], "sunflower"),
        (["playground", "sports field", "garden", "library"], "library"),
        (["paint", "sing", "run", "library"], "library")]),
    Draw("Draw your dream school. Label five places.", prompts=["My dream school"]),
]

B = [
    Circle("Circle the correct words.", items=[
        "Where {*are|is} Anna and Lily? — They're {*in|on} the library.",
        "Where {is|*are} the boys? — They're {in|*on} the playground.",
        "Tom {*is|are} in the gym.",
        "The children are {in|*on} the sports field.",
        "We are {*in|on} the Art room.",
        "Where {*is|are} the teacher? — She's {*in|on} the classroom."]),
    Circle("Circle the correct words.", items=[
        "Lily is {*reading|reads} a book in the library.",
        "The boys are {*running|runs} on the sports field.",
        "What {*is|are} he doing? — He's painting.",
        "We {*are|is} singing in the Music room.",
        "What are you {*doing|do}? — I'm writing."]),
    Fill("Complete the sentences with words from the box.", items=[
        "{Where} are the children? — They're in the dining hall.",
        "What are you {doing}? — We're {playing} basketball.",
        "Tom {is} painting in the Art room.",
        "The girls are {singing} in the Music room."], extra_words=["are"]),
    Unscramble("Put the words in the right order.", items=[
        "Where are they?", "They're on the playground.", "What are you doing?",
        "We're reading in the library."]),
    Reading("Read and answer.", title="Our school", text=(
        "This is our school. It is big and clean. It has a library, a gym and a Music room.\n\n"
        "It is break time. Some boys are playing football on the sports field. Some girls are reading in the "
        "library. Mr Karimov is in the gym. He is the PE teacher."), questions=[
        ("What are the boys doing?", "They're playing football."),
        ("Where are the girls?", "They're in the library."),
        ("Who is in the gym?", "Mr Karimov (the PE teacher).")]),
    WriteAbout("Write about your school.", frames=[
        "My school has a ___ and a ___ .", "At break time I'm on the ___ .", "I'm ___ ing."], lines=3,
        model=["My school has a library and a gym. At break time I'm on the playground. I'm playing football."]),
]

QUIZ = [
    Section("Part 1 · Words", [
        PicLabel("Look and write the places.", items=[
            ("library", "library"), ("gym", "gym"), ("playground", "playground"), ("art room", "art room"),
            ("dining hall", "dining hall"), ("music room", "music room")], bank=False, cols=3, size=34)]),
    Section("Part 2 · Grammar", [
        Circle("Circle the correct word.", items=[
            "Where {*are|is} they? — They're on the sports field.",
            "Tom and Max are {*in|on} the gym.",
            "What are you {*doing|do}? — We're reading.",
            "Lily {*is|are} painting a picture."]),
        Fill("Complete the sentences.", items=[
            "{Where} is Anna? — She's in the library.",
            "We're {singing} in the Music room.",
            "What are they {doing}? — They're running.",
            "The boys {are} playing football."], extra_words=["is"])]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="Break time", text=(
            "It is break time. Anna and Lily are in the library. They are reading books. "
            "Tom and Max are on the sports field. They are playing football. "
            "Mrs Nazarova is in the dining hall."), questions=[
            ("Where are Anna and Lily?", "In the library."),
            ("What are Tom and Max doing?", "Playing football."),
            ("Where is Mrs Nazarova?", "In the dining hall.")]),
        Unscramble("Put the words in the right order.", items=[
            "Where are they?", "We're in the gym.", "She is reading a book."])]),
]

SPEC = UnitSpec(number=2, slug="unit-2-at-school", title="At school", info=INFO, vocab=VOCAB, extra_vocab=EXTRA,
                lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="School places", sheet_b_name="in / on, present continuous, reading, writing")
