"""Guess What! Level 3 · Unit 1 — In the garden."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, OddOne, PicLabel, Reading, Section, Unscramble, WordSearch, WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.unit import UnitSpec, V

from .common import BADGE, GRADE_TIP_20

VOCAB = [
    V("tree", "daraxt", "tree"),
    V("leaf", "barg", "leaf"),
    V("caterpillar", "kapalak qurti", "caterpillar"),
    V("rabbit", "quyon", "rabbit"),
    V("butterfly", "kapalak", "butterfly"),
    V("flower", "gul", "flower"),
    V("grass", "o'tloq, maysa", "grass"),
    V("tortoise / turtle", "toshbaqa", "tortoise", ws="tortoise"),
    V("guinea pig", "dengiz cho'chqasi", None),
    V("snail", "salyangoz", "snail"),
]

INFO = UnitInfo(
    number=1, title="In the garden", topic="Garden animals and plants; describing pets",
    vocabulary="tree, leaf, caterpillar, rabbit, butterfly, flower, grass, tortoise/turtle, guinea pig, snail",
    grammar=["Possessive adjectives: (His) pet is (big). (Our) pet is (orange).",
             "What's that? It's a (snake). What are those? They're (flowers)."],
    skills="Listening: What can you see at the zoo?",
    phonics="ee / ea — chimpanzees, eat",
    story_value="Respect and listen to others",
    talk_time="Asking to borrow something",
    clil="Science — What types of habitats are there?",
)

LESSONS = [
    Lesson.std(
        title="Garden words",
        focus="Vocabulary — ten garden animals and plants",
        aims=["name the ten garden words from the flashcards",
              "say what they can see in a garden: I can see a (snail)"],
        language=["tree, leaf, caterpillar, rabbit, butterfly, flower, grass, tortoise (turtle), guinea pig, snail",
                  "I can see a … / What animal is it?"],
        materials=["Flashcards (games/flashcards.pdf)", "Student's Book: Vocabulary page + audio",
                   "Worksheet A (exercises A–B)"],
        greeting="Greet the class, take the register in English ('Who is away today?'). Write the date and the "
                 "unit title **In the garden** on the board.",
        warmup="Mime and guess. Pupils come to the front and mime a snail (very slow), a rabbit (hop), a "
               "butterfly (flap). The class guesses in Uzbek; you give the English word once and everybody repeats.",
        present="Flash the ten cards one by one: 'Look! A rabbit. Rabbit.' Choral repetition → rows → individuals "
                "(whisper / shout / sing). Student's Book: *Listen and point*, then *Listen, point and repeat*. "
                "Teach 'tortoise' and 'turtle' together — same animal.",
        practice="Card games: **What's missing?** (hide one card), **Slow reveal** (uncover a card bit by bit), "
                 "**Flyswatter** (two pupils race to touch the named card). Then Worksheet A, exercises A and B "
                 "in pairs.",
        produce="**Guess my picture** in pairs: one pupil thinks of a card and gives clues ('It's small. It's got a "
                "shell.'), the partner answers 'A snail!'. Model one round with a volunteer first.",
        wrap="Hold up three cards in a row; the class says the words without help. Set homework.",
        homework="Learn the ten words. Draw your garden and label five things in English (Worksheet A, exercise F).",
        assessment="Point to a card at random for 5 pupils (no prompting) and tick the class list.",
        tips=["Kapalak qurti (caterpillar) va kapalak (butterfly) — ikki so'z, ammo ikkita rasm bilan bog'lang: "
              "'caterpillar → butterfly' o'sish zanjiri so'zlarni eslab qolishga yordam beradi.",
              "'tortoise' va 'turtle' o'zbek tilida bitta — 'toshbaqa'. Ikkalasi to'g'ri ekanini ayting.",
              "Support: give weaker pupils a picture-only card to point to first. Extension: fast finishers write "
              "a colour next to each word (green tree, white rabbit)."],
    ),
    Lesson.std(
        title="Whose pet is it?",
        focus="Grammar 1 — possessive adjectives my, your, his, her, our, their, its",
        aims=["use my / your / his / her / our / their to say who owns a pet",
              "say and write: His pet is big. Our pet is orange."],
        language=["(His) pet is (big). (Our) pet is (orange).", "my · your · his · her · its · our · their"],
        materials=["Pictures of children with pets (draw 4 on the board)", "Student's Book Grammar page 1",
                   "Worksheet B, exercise A"],
        greeting="Ask three pupils 'What's your favourite animal?' and give the answer to the class: 'Aziz's favourite "
                 "animal is a rabbit.' (Keep the structure visible on the board.)",
        warmup="Review the ten words with the **Flyswatter** game (pairs at the board, words written in a circle).",
        present="Draw a boy (Tom) and a girl (Lily) each with a pet. Say: 'This is Tom. **His** pet is a rabbit. This is "
                "Lily. **Her** pet is a snail.' Point to yourself + class: 'Our class pet is a tortoise.' Build a "
                "table on the board: I → my, you → your, he → his, she → her, we → our, they → their. Colour "
                "the boy words blue, girl words red.",
        practice="Student's Book Grammar exercises (listen, then point at the picture). Worksheet B, exercise A "
                 "(circle the correct word) — do item 1 together, the rest individually, then check in pairs.",
        produce="**Pet chain**: pupil A says 'My pet is a rabbit. It is white.' Pupil B turns to C and says "
                "'His pet is a rabbit. Its colour is white.' Practise in rows of five.",
        wrap="Quick-fire: point to a pupil and ask the class 'Is it his or her pet?' Homework.",
        homework="Workbook grammar page; write three sentences about your family's pets (real or imaginary) "
                 "using my / his / her.",
        assessment="Listen for my/his/her during the pet chain; note pupils who confuse his and her.",
        tips=["O'zbek tilida 'u' jinsni ajratmaydi (he = she = u), shuning uchun **his / her** aralashtiriladi. "
              "Doimo rasm bilan mashq qiling: o'g'il bola → his, qiz bola → her.",
              "'its' (uning — jonivor yoki narsa uchun) va 'it's' (it is) — talaffuzi bir xil, yozilishi boshqa. "
              "Hozircha faqat eshitib tushunishi yetarli.",
              "Support: sentence frames on the board. Extension: add a colour and a size ('Their pet is big and "
              "orange.')."],
    ),
    Lesson.std(
        title="What's that? What are those?",
        focus="Grammar 2 — that / those for things that are far away; singular and plural",
        aims=["ask and answer: What's that? It's a … / What are those? They're …",
              "use singular for one thing and plural (-s / leaves) for more than one"],
        language=["What's that? — It's a (snake).", "What are those? — They're (flowers).",
                  "plurals: flowers, snails, rabbits, leaves"],
        materials=["Flashcards stuck far from pupils (on the back wall)", "Chant / song from the audio",
                   "Worksheet B exercises B–C"],
        greeting="Ask 'What's the date today? What's the weather like?' Review his / her with two pupils.",
        warmup="**Pelmanism by touch**: stick eight flashcards on the wall at the back. Point and ask 'What's that?' "
               "Pupils answer 'It's a tree.' Then point to two cards: 'What are those?' → 'They're …'.",
        present="Show the difference: hold a card near you — 'This is a rabbit.' Point to a far card — 'That is a "
                "rabbit.' Then two far cards — 'Those are rabbits.' Write the questions on the board with the "
                "matching answers, colour 'that/those'. Note the irregular plural **leaf → leaves**.",
        practice="Play the chant from the course audio (Unit 1) and do the actions; Student's Book Grammar "
                 "exercises. Worksheet B, exercises B and C.",
        produce="**Mystery bag / far-away quiz**: in groups of four, pupils ask 'What's that?' about pictures the "
                "teacher places around the room and score a point for each full-sentence answer.",
        wrap="Class chain: each pupil asks a neighbour 'What are those?' pointing to two picture cards.",
        homework="Activity Book grammar page; find two things far from you at home and write 'What's that?' questions "
                 "for them.",
        assessment="Note whether pupils add -s for plurals and choose It's / They're correctly.",
        tips=["'that' va 'this' farqi: o'zbek tilida ham 'bu' (yaqin) / 'u, o'sha' (uzoq) bor — o'sha bilan "
              "bog'lang.",
              "'They're' /ðeɪə/ — 'th' tovushi: til uchi tishlar orasida. 'They're' ni 'Dey're' deb aytmaslikka "
              "e'tibor bering.",
              "Support: use gestures (point near / far). Extension: pupils add colours: 'They're green leaves.'"],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "G", "T-Ss"),
    ),
    Lesson.std(
        title="At the zoo",
        focus="Skills: Listening and writing — What can you see at the zoo?",
        aims=["listen for specific animals and ticking what is mentioned",
              "write two or three sentences about a pet or a zoo animal"],
        language=["I can see a … / It's … / Their pet is …", "zoo animals from earlier units"],
        materials=["Student's Book Listening page + audio", "Worksheet B, exercises D–F",
                   "Pictures of zoo animals (optional)"],
        greeting="Greet and review: 'What's that?' pointing to animal pictures. Write today's aim on the board: "
                 "**I can listen and write about animals.**",
        warmup="**Animal sounds**: make a sound or show a silhouette, pupils name the animal in English.",
        present="Pre-listening: look at the Student's Book picture and predict: 'What can you see at the zoo?' Collect "
                "words on the board. Play the audio once for gist (which animals?), then again for detail "
                "(tick / match).",
        practice="Do the listening task, then check together. Pupils read the short text in Worksheet B exercise D "
                 "('Lily's garden') and answer the questions in complete sentences.",
        produce="Writing: using the help box in Worksheet B exercise E, pupils write three sentences about their "
                "pet or a pet they would like. Volunteers read aloud.",
        wrap="Gallery walk: pupils swap notebooks and tick one thing they like in a friend's text. Homework.",
        homework="Finish the writing and draw the pet. Learn the spelling of *caterpillar* and *butterfly*.",
        assessment="Collect five notebooks: check possessives (his/her), plural -s, capital letters and full stops.",
        tips=["Listening: ikki marta eshittiring — birinchi marta umumiy ma'no, ikkinchi marta tafsilot.",
              "Yozuvda katta harf va nuqtani alohida ta'kidlang: 'My pet is a rabbit.'",
              "Support: give a gapped text. Extension: add a second sentence with *because* (oral only)."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "S", "Ss-Ss"),
    ),
    Lesson.std(
        title="Listen to each other",
        focus="Story value (respect and listen to others), Talk time (asking to borrow something), Say it! ee / ea",
        aims=["follow the unit story and say why it is important to listen to others",
              "ask politely to borrow something: Can I borrow your …? Yes, here you are. Thank you.",
              "pronounce /iː/ in chimpanzees, eat, tree, leaf"],
        language=["Can I borrow your (pencil), please? — Sure. / Here you are. — Thank you.",
                  "Sound: ee / ea → /iː/ (tree, leaf, eat, chimpanzee)"],
        materials=["Student's Book story page + audio", "Student's Book Say it! page", "classroom objects to borrow"],
        greeting="Greet the class and ask 'Did you listen well today?' Show a finger on the lips: 'Listen, listen, "
                 "listen.'",
        warmup="**Chinese whispers** with the sentence 'The rabbit eats the green leaf.' — see how listening changes the "
               "message.",
        present="Story: look at the pictures first ('What can you see?'), listen and follow in the book. Ask "
                "simple comprehension questions ('Who is listening? Who is not listening?') and discuss the value "
                "in Uzbek, then summarise in English ('Listen to others.').",
        practice="Talk time: present the model dialogue ('Can I borrow your pencil, please?'). Practise in open pairs, "
                 "then closed pairs with real classroom objects. Say it!: listen, repeat, then list more ee/ea words.",
        produce="**Borrow and return**: pupils walk around with two objects and ask classmates to borrow one, using "
                "polite phrases, then return it with 'Thank you.'",
        wrap="Sing or chant the tongue twister from Say it! slowly, then fast. Homework.",
        homework="Activity Book story page; learn the dialogue 'Can I borrow your …?'.",
        assessment="Listen for please / thank you in the pair work and note pupils who use both.",
        tips=["'Can I borrow…' ni 'Can I take…' bilan aralashtirmang: borrow = vaqtincha olish. Qaytarishni "
              "ta'kidlang.",
              "/iː/ — o'zbek tilidagi 'i' dan uzunroq. 'eat' va 'it' farqini juft so'zlar bilan mashq qiling."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "Ss-Ss", "Ss-Ss", "T-Ss"),
    ),
    Lesson.std(
        title="Habitats",
        focus="CLIL Science — What types of habitats are there?",
        aims=["name three habitats (for example forest, ocean, desert) and an animal from each",
              "explain in a short sentence where an animal lives: A snail lives in the garden"],
        language=["habitat · forest · ocean · desert · garden · lives in", "A (tortoise) lives in a (desert)."],
        materials=["Student's Book CLIL pages + video if available", "A4 paper and crayons", "Pictures of habitats"],
        greeting="Greet and ask 'Where do you live?' — 'I live in Tashkent / in a village.'",
        warmup="**Where is my home?** Mime an animal; the class guesses the animal and its habitat.",
        present="Show three habitat pictures. Teach *habitat* = the natural home of an animal or plant. Match animals "
                "to habitats in pairs (tortoise – desert / garden, snail – garden, dolphin – ocean…).",
        practice="Student's Book CLIL activities (watch / read / match). Pupils complete a simple table: Animal | "
                 "Habitat on the board.",
        produce="**Habitat poster** in groups: draw one habitat and stick or draw three animals in it with the label "
                "'A … lives in the …'. Display on the wall.",
        wrap="Each group presents one sentence from their poster; class says which habitat it is.",
        homework="Find one animal that lives near your home and draw its habitat.",
        assessment="Use a simple rubric for the poster: labels (1), sentence (1), teamwork (1).",
        tips=["'habitat' — 'yashash muhiti' deb tushuntiring; fan (Science) bilan bog'lang.",
              "Mahalliy misollar: camel in the desert (tuya — cho'l), fish in the river (daryo)."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "Ss-Ss", "G", "G / T-Ss"),
    ),
    Lesson.std(
        title="Unit 1 revision and quiz",
        focus="Revision of Unit 1 language; quick quiz",
        aims=["use garden vocabulary, possessives and that / those accurately",
              "show what they have learned in the unit quiz"],
        language=["All language from Unit 1"],
        materials=["Unit quiz (worksheets/quiz.pdf)", "Bingo cards (games/bingo.pdf)", "Flashcards"],
        greeting="Greet and explain that today is revision and a short quiz: 'No stress — show what you know!'",
        warmup="**Bingo** with the ten garden words (8 different cards ready to print).",
        present="Quick review on the board: fill a mind-map with the unit vocabulary, the possessive table and the "
                "question words.",
        practice="Pairs: revise using the Pairs (memory) cards. Pupils correct three mistakes you deliberately write on "
                 "the board (his/her, plural -s, that/those).",
        produce="Quiz (15 minutes, 20 points). Collect and mark with the key.",
        wrap="Praise progress. Share two common mistakes from the quiz and correct them together.",
        homework="Correct your quiz mistakes; choose one new animal word to teach the class next lesson.",
        assessment="Mark the quiz (answer keys PDF). Record scores and pupils who need extra practice.",
        tips=[GRADE_TIP_20,
              "Weak pupils: read the instructions aloud and allow one pair check. Extension: write a short "
              "riddle about a garden animal."],
        interactions=("T-Ss", "Ss-Ss", "T-Ss", "Ss-Ss", "S", "T-Ss"),
    ),
]

A = [
    PicLabel("Look and write the words.", items=[
        ("tree", "tree"), ("leaf", "leaf"), ("caterpillar", "caterpillar"), ("rabbit", "rabbit"),
        ("butterfly", "butterfly"), ("flower", "flower"), ("tortoise", "tortoise"), ("snail", "snail")]),
    Match("Match the English words to the Uzbek words.", pairs=[
        ("tree", "daraxt"), ("rabbit", "quyon"), ("snail", "salyangoz"), ("leaf", "barg"),
        ("butterfly", "kapalak"), ("flower", "gul")], seed=11),
    Gaps("Look and complete the words. Some letters are missing.", items=[
        ("caterpillar", "caterpillar"), ("butterfly", "butterfly"), ("tortoise", "tortoise"),
        ("rabbit", "rabbit"), ("snail", "snail"), ("grass", "grass")]),
    WordSearch("Find the garden words.", words=["tree", "leaf", "snail", "rabbit", "flower", "grass",
                                                "butterfly", "tortoise", "caterpillar"], size=12, seed=5),
    OddOne("Circle the odd one out.", rows=[
        (["rabbit", "tortoise", "flower", "snail"], "flower"),
        (["tree", "grass", "butterfly", "leaf"], "butterfly"),
        (["snail", "caterpillar", "rabbit", "leaf"], "leaf"),
        (["flower", "tree", "grass", "tortoise"], "tortoise")]),
    Draw("Draw your garden. Label five things.", prompts=["My garden"]),
]

B = [
    V("tree", "daraxt", "tree"),
    V("leaf", "barg", "leaf"),
    V("caterpillar", "kapalak qurti", "caterpillar"),
    V("rabbit", "quyon", "rabbit"),
    V("butterfly", "kapalak", "butterfly"),
    V("flower", "gul", "flower"),
    V("grass", "o'tloq, maysa", "grass"),
    V("tortoise / turtle", "toshbaqa", "tortoise", ws="tortoise"),
    V("guinea pig", "dengiz cho'chqasi", None),
    V("snail", "salyangoz", "snail"),
]

INFO = UnitInfo(
    number=1, title="In the garden", topic="Garden animals and plants; describing pets",
    vocabulary="tree, leaf, caterpillar, rabbit, butterfly, flower, grass, tortoise/turtle, guinea pig, snail",
    grammar=["Possessive adjectives: (His) pet is (big). (Our) pet is (orange).",
             "What's that? It's a (snake). What are those? They're (flowers)."],
    skills="Listening: What can you see at the zoo?",
    phonics="ee / ea — chimpanzees, eat",
    story_value="Respect and listen to others",
    talk_time="Asking to borrow something",
    clil="Science — What types of habitats are there?",
)

LESSONS = [
    Lesson.std(
        title="Garden words",
        focus="Vocabulary — ten garden animals and plants",
        aims=["name the ten garden words from the flashcards",
              "say what they can see in a garden: I can see a (snail)"],
        language=["tree, leaf, caterpillar, rabbit, butterfly, flower, grass, tortoise (turtle), guinea pig, snail",
                  "I can see a … / What animal is it?"],
        materials=["Flashcards (games/flashcards.pdf)", "Student's Book: Vocabulary page + audio",
                   "Worksheet A (exercises A–B)"],
        greeting="Greet the class, take the register in English ('Who is away today?'). Write the date and the "
                 "unit title **In the garden** on the board.",
        warmup="Mime and guess. Pupils come to the front and mime a snail (very slow), a rabbit (hop), a "
               "butterfly (flap). The class guesses in Uzbek; you give the English word once and everybody repeats.",
        present="Flash the ten cards one by one: 'Look! A rabbit. Rabbit.' Choral repetition → rows → individuals "
                "(whisper / shout / sing). Student's Book: *Listen and point*, then *Listen, point and repeat*. "
                "Teach 'tortoise' and 'turtle' together — same animal.",
        practice="Card games: **What's missing?** (hide one card), **Slow reveal** (uncover a card bit by bit), "
                 "**Flyswatter** (two pupils race to touch the named card). Then Worksheet A, exercises A and B "
                 "in pairs.",
        produce="**Guess my picture** in pairs: one pupil thinks of a card and gives clues ('It's small. It's got a "
                "shell.'), the partner answers 'A snail!'. Model one round with a volunteer first.",
        wrap="Hold up three cards in a row; the class says the words without help. Set homework.",
        homework="Learn the ten words. Draw your garden and label five things in English (Worksheet A, exercise F).",
        assessment="Point to a card at random for 5 pupils (no prompting) and tick the class list.",
        tips=["Kapalak qurti (caterpillar) va kapalak (butterfly) — ikki so'z, ammo ikkita rasm bilan bog'lang: "
              "'caterpillar → butterfly' o'sish zanjiri so'zlarni eslab qolishga yordam beradi.",
              "'tortoise' va 'turtle' o'zbek tilida bitta — 'toshbaqa'. Ikkalasi to'g'ri ekanini ayting.",
              "Support: give weaker pupils a picture-only card to point to first. Extension: fast finishers write "
              "a colour next to each word (green tree, white rabbit)."],
    ),
    Lesson.std(
        title="Whose pet is it?",
        focus="Grammar 1 — possessive adjectives my, your, his, her, our, their, its",
        aims=["use my / your / his / her / our / their to say who owns a pet",
              "say and write: His pet is big. Our pet is orange."],
        language=["(His) pet is (big). (Our) pet is (orange).", "my · your · his · her · its · our · their"],
        materials=["Pictures of children with pets (draw 4 on the board)", "Student's Book Grammar page 1",
                   "Worksheet B, exercise A"],
        greeting="Ask three pupils 'What's your favourite animal?' and give the answer to the class: 'Aziz's favourite "
                 "animal is a rabbit.' (Keep the structure visible on the board.)",
        warmup="Review the ten words with the **Flyswatter** game (pairs at the board, words written in a circle).",
        present="Draw a boy (Tom) and a girl (Lily) each with a pet. Say: 'This is Tom. **His** pet is a rabbit. This is "
                "Lily. **Her** pet is a snail.' Point to yourself + class: 'Our class pet is a tortoise.' Build a "
                "table on the board: I → my, you → your, he → his, she → her, we → our, they → their. Colour "
                "the boy words blue, girl words red.",
        practice="Student's Book Grammar exercises (listen, then point at the picture). Worksheet B, exercise A "
                 "(circle the correct word) — do item 1 together, the rest individually, then check in pairs.",
        produce="**Pet chain**: pupil A says 'My pet is a rabbit. It is white.' Pupil B turns to C and says "
                "'His pet is a rabbit. Its colour is white.' Practise in rows of five.",
        wrap="Quick-fire: point to a pupil and ask the class 'Is it his or her pet?' Homework.",
        homework="Workbook grammar page; write three sentences about your family's pets (real or imaginary) "
                 "using my / his / her.",
        assessment="Listen for my/his/her during the pet chain; note pupils who confuse his and her.",
        tips=["O'zbek tilida 'u' jinsni ajratmaydi (he = she = u), shuning uchun **his / her** aralashtiriladi. "
              "Doimo rasm bilan mashq qiling: o'g'il bola → his, qiz bola → her.",
              "'its' (uning — jonivor yoki narsa uchun) va 'it's' (it is) — talaffuzi bir xil, yozilishi boshqa. "
              "Hozircha faqat eshitib tushunishi yetarli.",
              "Support: sentence frames on the board. Extension: add a colour and a size ('Their pet is big and "
              "orange.')."],
    ),
    Lesson.std(
        title="What's that? What are those?",
        focus="Grammar 2 — that / those for things that are far away; singular and plural",
        aims=["ask and answer: What's that? It's a … / What are those? They're …",
              "use singular for one thing and plural (-s / leaves) for more than one"],
        language=["What's that? — It's a (snake).", "What are those? — They're (flowers).",
                  "plurals: flowers, snails, rabbits, leaves"],
        materials=["Flashcards stuck far from pupils (on the back wall)", "Chant / song from the audio",
                   "Worksheet B exercises B–C"],
        greeting="Ask 'What's the date today? What's the weather like?' Review his / her with two pupils.",
        warmup="**Pelmanism by touch**: stick eight flashcards on the wall at the back. Point and ask 'What's that?' "
               "Pupils answer 'It's a tree.' Then point to two cards: 'What are those?' → 'They're …'.",
        present="Show the difference: hold a card near you — 'This is a rabbit.' Point to a far card — 'That is a "
                "rabbit.' Then two far cards — 'Those are rabbits.' Write the questions on the board with the "
                "matching answers, colour 'that/those'. Note the irregular plural **leaf → leaves**.",
        practice="Play the chant from the course audio (Unit 1) and do the actions; Student's Book Grammar "
                 "exercises. Worksheet B, exercises B and C.",
        produce="**Mystery bag / far-away quiz**: in groups of four, pupils ask 'What's that?' about pictures the "
                "teacher places around the room and score a point for each full-sentence answer.",
        wrap="Class chain: each pupil asks a neighbour 'What are those?' pointing to two picture cards.",
        homework="Activity Book grammar page; find two things far from you at home and write 'What's that?' questions "
                 "for them.",
        assessment="Note whether pupils add -s for plurals and choose It's / They're correctly.",
        tips=["'that' va 'this' farqi: o'zbek tilida ham 'bu' (yaqin) / 'u, o'sha' (uzoq) bor — o'sha bilan "
              "bog'lang.",
              "'They're' /ðeɪə/ — 'th' tovushi: til uchi tishlar orasida. 'They're' ni 'Dey're' deb aytmaslikka "
              "e'tibor bering.",
              "Support: use gestures (point near / far). Extension: pupils add colours: 'They're green leaves.'"],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "G", "T-Ss"),
    ),
    Lesson.std(
        title="At the zoo",
        focus="Skills: Listening and writing — What can you see at the zoo?",
        aims=["listen for specific animals and ticking what is mentioned",
              "write two or three sentences about a pet or a zoo animal"],
        language=["I can see a … / It's … / Their pet is …", "zoo animals from earlier units"],
        materials=["Student's Book Listening page + audio", "Worksheet B, exercises D–F",
                   "Pictures of zoo animals (optional)"],
        greeting="Greet and review: 'What's that?' pointing to animal pictures. Write today's aim on the board: "
                 "**I can listen and write about animals.**",
        warmup="**Animal sounds**: make a sound or show a silhouette, pupils name the animal in English.",
        present="Pre-listening: look at the Student's Book picture and predict: 'What can you see at the zoo?' Collect "
                "words on the board. Play the audio once for gist (which animals?), then again for detail "
                "(tick / match).",
        practice="Do the listening task, then check together. Pupils read the short text in Worksheet B exercise D "
                 "('Lily's garden') and answer the questions in complete sentences.",
        produce="Writing: using the help box in Worksheet B exercise E, pupils write three sentences about their "
                "pet or a pet they would like. Volunteers read aloud.",
        wrap="Gallery walk: pupils swap notebooks and tick one thing they like in a friend's text. Homework.",
        homework="Finish the writing and draw the pet. Learn the spelling of *caterpillar* and *butterfly*.",
        assessment="Collect five notebooks: check possessives (his/her), plural -s, capital letters and full stops.",
        tips=["Listening: ikki marta eshittiring — birinchi marta umumiy ma'no, ikkinchi marta tafsilot.",
              "Yozuvda katta harf va nuqtani alohida ta'kidlang: 'My pet is a rabbit.'",
              "Support: give a gapped text. Extension: add a second sentence with *because* (oral only)."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "S", "Ss-Ss"),
    ),
    Lesson.std(
        title="Listen to each other",
        focus="Story value (respect and listen to others), Talk time (asking to borrow something), Say it! ee / ea",
        aims=["follow the unit story and say why it is important to listen to others",
              "ask politely to borrow something: Can I borrow your …? Yes, here you are. Thank you.",
              "pronounce /iː/ in chimpanzees, eat, tree, leaf"],
        language=["Can I borrow your (pencil), please? — Sure. / Here you are. — Thank you.",
                  "Sound: ee / ea → /iː/ (tree, leaf, eat, chimpanzee)"],
        materials=["Student's Book story page + audio", "Student's Book Say it! page", "classroom objects to borrow"],
        greeting="Greet the class and ask 'Did you listen well today?' Show a finger on the lips: 'Listen, listen, "
                 "listen.'",
        warmup="**Chinese whispers** with the sentence 'The rabbit eats the green leaf.' — see how listening changes the "
               "message.",
        present="Story: look at the pictures first ('What can you see?'), listen and follow in the book. Ask "
                "simple comprehension questions ('Who is listening? Who is not listening?') and discuss the value "
                "in Uzbek, then summarise in English ('Listen to others.').",
        practice="Talk time: present the model dialogue ('Can I borrow your pencil, please?'). Practise in open pairs, "
                 "then closed pairs with real classroom objects. Say it!: listen, repeat, then list more ee/ea words.",
        produce="**Borrow and return**: pupils walk around with two objects and ask classmates to borrow one, using "
                "polite phrases, then return it with 'Thank you.'",
        wrap="Sing or chant the tongue twister from Say it! slowly, then fast. Homework.",
        homework="Activity Book story page; learn the dialogue 'Can I borrow your …?'.",
        assessment="Listen for please / thank you in the pair work and note pupils who use both.",
        tips=["'Can I borrow…' ni 'Can I take…' bilan aralashtirmang: borrow = vaqtincha olish. Qaytarishni "
              "ta'kidlang.",
              "/iː/ — o'zbek tilidagi 'i' dan uzunroq. 'eat' va 'it' farqini juft so'zlar bilan mashq qiling."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "Ss-Ss", "Ss-Ss", "T-Ss"),
    ),
    Lesson.std(
        title="Habitats",
        focus="CLIL Science — What types of habitats are there?",
        aims=["name three habitats (for example forest, ocean, desert) and an animal from each",
              "explain in a short sentence where an animal lives: A snail lives in the garden"],
        language=["habitat · forest · ocean · desert · garden · lives in", "A (tortoise) lives in a (desert)."],
        materials=["Student's Book CLIL pages + video if available", "A4 paper and crayons", "Pictures of habitats"],
        greeting="Greet and ask 'Where do you live?' — 'I live in Tashkent / in a village.'",
        warmup="**Where is my home?** Mime an animal; the class guesses the animal and its habitat.",
        present="Show three habitat pictures. Teach *habitat* = the natural home of an animal or plant. Match animals "
                "to habitats in pairs (tortoise – desert / garden, snail – garden, dolphin – ocean…).",
        practice="Student's Book CLIL activities (watch / read / match). Pupils complete a simple table: Animal | "
                 "Habitat on the board.",
        produce="**Habitat poster** in groups: draw one habitat and stick or draw three animals in it with the label "
                "'A … lives in the …'. Display on the wall.",
        wrap="Each group presents one sentence from their poster; class says which habitat it is.",
        homework="Find one animal that lives near your home and draw its habitat.",
        assessment="Use a simple rubric for the poster: labels (1), sentence (1), teamwork (1).",
        tips=["'habitat' — 'yashash muhiti' deb tushuntiring; fan (Science) bilan bog'lang.",
              "Mahalliy misollar: camel in the desert (tuya — cho'l), fish in the river (daryo)."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "Ss-Ss", "G", "G / T-Ss"),
    ),
    Lesson.std(
        title="Unit 1 revision and quiz",
        focus="Revision of Unit 1 language; quick quiz",
        aims=["use garden vocabulary, possessives and that / those accurately",
              "show what they have learned in the unit quiz"],
        language=["All language from Unit 1"],
        materials=["Unit quiz (worksheets/quiz.pdf)", "Bingo cards (games/bingo.pdf)", "Flashcards"],
        greeting="Greet and explain that today is revision and a short quiz: 'No stress — show what you know!'",
        warmup="**Bingo** with the ten garden words (8 different cards ready to print).",
        present="Quick review on the board: fill a mind-map with the unit vocabulary, the possessive table and the "
                "question words.",
        practice="Pairs: revise using the Pairs (memory) cards. Pupils correct three mistakes you deliberately write on "
                 "the board (his/her, plural -s, that/those).",
        produce="Quiz (15 minutes, 20 points). Collect and mark with the key.",
        wrap="Praise progress. Share two common mistakes from the quiz and correct them together.",
        homework="Correct your quiz mistakes; choose one new animal word to teach the class next lesson.",
        assessment="Mark the quiz (answer keys PDF). Record scores and pupils who need extra practice.",
        tips=[GRADE_TIP_20,
              "Weak pupils: read the instructions aloud and allow one pair check. Extension: write a short "
              "riddle about a garden animal."],
        interactions=("T-Ss", "Ss-Ss", "T-Ss", "Ss-Ss", "S", "T-Ss"),
    ),
]

A = [
    PicLabel("Look and write the words.", items=[
        ("tree", "tree"), ("leaf", "leaf"), ("caterpillar", "caterpillar"), ("rabbit", "rabbit"),
        ("butterfly", "butterfly"), ("flower", "flower"), ("tortoise", "tortoise"), ("snail", "snail")]),
    Match("Match the English words to the Uzbek words.", pairs=[
        ("tree", "daraxt"), ("rabbit", "quyon"), ("snail", "salyangoz"), ("leaf", "barg"),
        ("butterfly", "kapalak"), ("flower", "gul")], seed=11),
    Gaps("Look and complete the words. Some letters are missing.", items=[
        ("caterpillar", "caterpillar"), ("butterfly", "butterfly"), ("tortoise", "tortoise"),
        ("rabbit", "rabbit"), ("snail", "snail"), ("grass", "grass")]),
    WordSearch("Find the garden words.", words=["tree", "leaf", "snail", "rabbit", "flower", "grass",
                                                "butterfly", "tortoise", "caterpillar"], size=12, seed=5),
    OddOne("Circle the odd one out.", rows=[
        (["rabbit", "tortoise", "flower", "snail"], "flower"),
        (["tree", "grass", "butterfly", "leaf"], "butterfly"),
        (["snail", "caterpillar", "rabbit", "leaf"], "leaf"),
        (["flower", "tree", "grass", "tortoise"], "tortoise")]),
    Draw("Draw your garden. Label five things.", prompts=["My garden"]),
]

# fix: the Match above must pair tree→daraxt and flower→gul; rebuilt below for clarity
A[1] = Match("Match the English words to the Uzbek words.", pairs=[
    ("tree", "daraxt"), ("rabbit", "quyon"), ("snail", "salyangoz"), ("leaf", "barg"),
    ("butterfly", "kapalak"), ("flower", "gul")], seed=11)

B = [
    Circle("Circle the correct word.", items=[
        "This is Tom. {*His|He} pet is big.",
        "We have a class tortoise. {*Our|We} tortoise is orange.",
        "This is Lily. {*Her|She} rabbit is white.",
        "Tom and Max have a snail. {*Their|They} snail is slow.",
        "I have a tortoise. {*My|I} tortoise is old.",
        "You have a guinea pig. {*Your|You} guinea pig is cute."]),
    Circle("Circle the correct words.", items=[
        "{*What's|What are} that? It's a snake.",
        "{What's|*What are} those? They're flowers.",
        "What are those? {It's|*They're} butterflies.",
        "What's that? {*It's|They're} a caterpillar."]),
    Fill("Complete the sentences with words from the box.", items=[
        "{What's} that? — It's a tortoise.",
        "{What are} those? — They're leaves.",
        "That is Anna's pet. {Her} pet is a guinea pig.",
        "These are Max and Tom's rabbits. {Their} rabbits are white.",
        "It's our snail. {Our} snail is slow."], extra_words=["His"]),
    Unscramble("Put the words in the right order.", items=[
        "What's that?", "It's a big tree.", "Their pet is orange.", "They're green leaves."]),
    Reading("Read and answer.", title="Lily's garden", text=(
        "This is Lily's garden. It is small but beautiful. She has a big tree and red flowers.\n\n"
        "Her pet is a tortoise. It is old and green. Its name is Slowly.\n\n"
        "Lily's brother has a rabbit. His rabbit is white and small."), questions=[
        ("What is Lily's pet?", "A tortoise."),
        ("What colour is her tortoise?", "It is green."),
        ("What colour is her brother's rabbit?", "It is white.")]),
    WriteAbout("Write about your pet (or a pet you like).", frames=[
        "My pet is a ___ .", "It is ___ and ___ .", "Its name is ___ ."], lines=3,
        model=["My pet is a rabbit. It is small and white. Its name is Snowy."]),
]

QUIZ = [
    Section("Part 1 · Words", [
        PicLabel("Look and write the words.", items=[
            ("tree", "tree"), ("rabbit", "rabbit"), ("butterfly", "butterfly"), ("snail", "snail"),
            ("tortoise", "tortoise"), ("flower", "flower")], bank=False, cols=3, size=34)]),
    Section("Part 2 · Grammar", [
        Circle("Circle the correct word.", items=[
            "Lily has a rabbit. {*Her|His} rabbit is white.",
            "We have a snail. {*Our|Their} snail is slow.",
            "What {*are|is} those? They're flowers.",
            "{*What's|What are} that? It's a tree."]),
        Fill("Complete the sentences.", items=[
            "Max has a tortoise. {His} tortoise is old.",
            "{What's} that? — It's a butterfly.",
            "{What are} those? — They're leaves.",
            "Anna and Lily have a pet. {Their} pet is a guinea pig."], extra_words=["Her"])]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="Tom's pet", text=(
            "Tom has a pet. It is a rabbit. Its name is Fluffy. His rabbit is big and brown. "
            "Fluffy eats grass and green leaves."), questions=[
            ("What is Tom's pet?", "A rabbit."),
            ("What is its name?", "Fluffy."),
            ("What does it eat?", "Grass and green leaves.")]),
        Unscramble("Put the words in the right order.", items=[
            "Her pet is a snail.", "What are those?", "It's a green leaf."])]),
]

SPEC = UnitSpec(number=1, slug="unit-1-in-the-garden", title="In the garden", info=INFO, vocab=VOCAB,
                lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="Words", sheet_b_name="Possessives, that / those, reading, writing",
                intro_note="Language aims match the Cambridge 'Guess What!' Level 3 course map. Page numbers are "
                           "not given because editions differ — use the page that matches the lesson aim.")
