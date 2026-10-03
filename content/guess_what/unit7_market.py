"""Guess What! Level 3 · Unit 7 — At the market."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, OddOne, PicLabel, Reading, Section, Unscramble, WordSearch, WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.unit import UnitSpec, V

from .common import BADGE, GRADE_TIP_20

VOCAB = [
    V("lemons", "limonlar", "lemon"),
    V("limes", "laymlar (yashil limon)", None),
    V("watermelons", "tarvuzlar", "watermelon"),
    V("coconuts", "kokos yong'oqlari", "coconut"),
    V("grapes", "uzum", "grapes"),
    V("mangoes", "mangolar", "mango"),
    V("pineapples", "ananaslar", "pineapple"),
    V("pears", "noklar", "pear"),
    V("tomatoes", "pomidorlar", "tomato"),
    V("onions", "piyozlar", "onion"),
]

EXTRA = [
    V("apples", "olmalar", "apple"), V("bananas", "bananlar", "banana"), V("carrots", "sabzilar", "carrot"),
    V("potatoes", "kartoshkalar", "potato"), V("cucumbers", "bodringlar", "cucumber"),
    V("lots of", "ko'p", None), V("some", "bir nechta, ozgina", None), V("any", "biron, hech qanday", None),
]

INFO = UnitInfo(
    number=7, title="At the market", topic="Fruit and vegetables; how many there are",
    vocabulary="lemons, limes, watermelons, coconuts, grapes, mangoes, pineapples, pears, tomatoes, onions",
    grammar=["There (are lots of) (grapes). There (are some) (tomatoes). There (aren't any) (limes).",
             "Are there any (pears)? Yes, there are. / No, there aren't."],
    skills="Listening: Do you like smoothies?",
    phonics="ch — chipmunks, pouches",
    story_value="Reuse old things",
    talk_time="Making choices",
    clil="Science — What parts of plants can we eat?",
)

LESSONS = [
    Lesson.std(
        title="Fruit and vegetables",
        focus="Vocabulary — ten fruit and vegetables (plural nouns)",
        aims=["name ten fruit and vegetables in the plural", "spell plurals: lemons, tomatoes, mangoes, onions"],
        language=["lemons, limes, watermelons, coconuts, grapes, mangoes, pineapples, pears, tomatoes, onions"],
        materials=["Flashcards or real fruit", "Student's Book Vocabulary page + audio", "Worksheet A exercises A–B"],
        greeting="Bring a bag with fruit. Ask 'What's in my bag?' and write **At the market** on the board.",
        warmup="**Feel and guess**: a pupil puts a hand in the bag and guesses the fruit by touch; class helps with "
               "Uzbek words.",
        present="Present the ten words with flashcards or real items. Stress the plural: 'One lemon. Two lemons.' Note the "
                "spelling: tomato → tomatoes, mango → mangoes. Student's Book: *Listen and point*, *Listen, point "
                "and repeat*.",
        practice="Worksheet A exercises A (label) and B (match singular and plural). Play **What's missing?**",
        produce="**Market stall**: pairs build a stall on the desk with cards and sell: 'Two mangoes, please.' — 'Here you "
                "are.'",
        wrap="Teacher holds up a card; pupils say the plural word. Homework.",
        homework="Learn the words and draw your favourite fruit stall (Worksheet A exercise F).",
        assessment="Point at cards for 5 pupils; note plural errors.",
        tips=["O'zbek bozorida ('bozor') bu mevalarning ko'pi bor — mahalliy nomlar bilan bog'lang: uzum, olma, nok, "
              "tarvuz.",
              "Ko'plik: -o bilan tugaydigan so'zlar (tomato, mango, potato) → -es. Bular istisno; jadval qilib yozing.",
              "Support: flashcards with pictures only. Extension: pupils write a colour next to each fruit."],
    ),
    Lesson.std(
        title="There are lots of grapes",
        focus="Grammar 1 — There are lots of / some + plural nouns",
        aims=["describe a market stall: There are lots of grapes. There are some tomatoes.",
              "choose lots of (many) or some (a few)"],
        language=["There (are lots of) (grapes). There (are some) (tomatoes)."],
        materials=["Flashcards in groups on the board (8 grapes, 3 tomatoes)", "Student's Book Grammar page 1",
                   "Worksheet B exercise A"],
        greeting="Ask 'How many pupils are there in our class?' and count together.",
        warmup="**How many?** Show a card with a number of dots or fruit for three seconds; pupils guess 'lots' or 'some'.",
        present="Draw a stall on the board: 10 grapes, 3 tomatoes. Say: 'There are lots of grapes. There are some "
                "tomatoes.' Write the frame: There are lots of / some + plural noun. Drill with changing pictures.",
        practice="Student's Book Grammar activities (listen and tick). Worksheet B exercise A (circle).",
        produce="**Stall descriptions**: pupils draw their own stall with different amounts and describe it to a partner, who "
                "draws what they hear.",
        wrap="Quick-fire: show a picture; pupils say 'There are lots of …' or 'some …'. Homework.",
        homework="Workbook grammar page; describe your kitchen: 'There are some …'",
        assessment="Check are + plural and lots of / some.",
        tips=["'There are' + ko'plik. O'zbekcha 'bor' bir xil, lekin inglizchada **is** (birlik) va **are** (ko'plik) "
              "farqlanadi.",
              "'lots of' = 'a lot of' (ko'p); suhbatda juda ko'p ishlatiladi.",
              "Support: gesture for lots (arms wide) and some (two fingers). Extension: add colours."],
    ),
    Lesson.std(
        title="Are there any pears?",
        focus="Grammar 2 — There aren't any … / Are there any …? Yes, there are. / No, there aren't.",
        aims=["say what is not there: There aren't any limes.",
              "ask and answer: Are there any pears? Yes, there are. / No, there aren't."],
        language=["There (aren't any) (limes).", "Are there any (pears)? — Yes, there are. / No, there aren't."],
        materials=["A stall picture with some items missing", "Chant from the audio", "Worksheet B exercises B–D"],
        greeting="Show an empty basket: 'Are there any apples?' — 'No, there aren't.'",
        warmup="**Fruit basket**: show a covered picture; pupils guess with 'Are there any pears?' (you answer yes / no).",
        present="Show a stall with only grapes and onions. Model: 'Are there any pears? No, there aren't. There aren't any "
                "pears.' Write the pattern and colour any. Compare some (positive) and any (negative and "
                "questions).",
        practice="Play the chant / Student's Book Grammar audio. Worksheet B exercises B (read and answer), C (fill in) and "
                 "D (unscramble).",
        produce="**Spot the difference**: pairs have two stall pictures; they ask 'Are there any …?' to find five "
                "differences.",
        wrap="Teacher asks about a picture; pupils answer with full short answers. Homework.",
        homework="Activity Book grammar page; write three sentences about a picture of a shop.",
        assessment="Check some / any and short answers.",
        tips=["**some** — darak gap; **any** — inkor va so'roq gap. Bu qoida o'zbek tilida yo'q; rangli qilib yozing.",
              "'aren't' /ɑːnt/ — 'r' aytilmaydi (Britaniya). 'There aren't any' uch so'zni bir ovozda o'qishni mashq qiling.",
              "Support: sentence frames. Extension: add 'but there are some …'."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "Ss-Ss", "T-Ss"),
    ),
    Lesson.std(
        title="Do you like smoothies?",
        focus="Skills: Listening — Do you like smoothies? + writing a recipe",
        aims=["listen for fruit and numbers in a smoothie recipe", "write a short smoothie recipe"],
        language=["smoothie · milk · ice · blend", "There are … / Put … in the glass."],
        materials=["Student's Book Listening page + audio", "Worksheet B exercise E", "recipe cards"],
        greeting="Ask 'Do you like smoothies?' and count hands.",
        warmup="**Design a smoothie**: pupils call out fruit; write a class smoothie on the board.",
        present="Pre-listening: look at the pictures and name the fruit. Play the audio twice: first for gist, then to tick "
                "the ingredients.",
        practice="Check in pairs, then class. Pupils read the market text (Worksheet B exercise B) to find what there is.",
        produce="Writing: pupils write a short recipe: 'My smoothie: two bananas, some grapes…'. Volunteers read aloud.",
        wrap="Class votes for the best smoothie recipe. Homework.",
        homework="Finish the recipe; draw the smoothie.",
        assessment="Collect five recipes; check plurals and some / lots of.",
        tips=["Ta'mlar haqida yozish bolalarga yoqadi — 'mening sevimli sharbatim' bilan bog'lang.",
              "Support: give a recipe template. Extension: add 'There aren't any …' for things they hate."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "S", "T-Ss"),
    ),
    Lesson.std(
        title="Reuse old things",
        focus="Story value (reuse old things), Talk time (making choices), Say it! ch",
        aims=["follow the story and say how to reuse old things",
              "make a choice: Would you like a mango or a pear? — A mango, please.",
              "pronounce /tʃ/ in chipmunk, chips, cheese, chair"],
        language=["Would you like a (mango) or a (pear)? — A (mango), please.", "Sound: ch → /tʃ/ (chipmunks, chips)"],
        materials=["Student's Book story + audio", "Student's Book Say it! page", "real items (old jars, boxes)"],
        greeting="Show an old jar: 'Is it rubbish? What can we do?' Elicit ideas (pencil pot, flower pot).",
        warmup="**Rubbish or treasure?** Show items; pupils say how to reuse them.",
        present="Story: predict from pictures, listen, answer 'What do they reuse? Why?' Discuss in Uzbek, then conclude "
                "in English: 'Reuse old things.'",
        practice="Talk time: model 'Would you like a mango or a pear?'; practise in pairs with fruit cards. Say it!: listen, "
                 "repeat, find more ch words.",
        produce="**Fruit shop role-play**: pairs — shopkeeper offers two choices; customer chooses with 'please' and "
                "'thank you'.",
        wrap="Chant the Say it! tongue twister. Homework.",
        homework="Activity Book story page; reuse one item at home and draw it.",
        assessment="Listen for correct choices and polite language in the role-play.",
        tips=["'Would you like…?' — 'Xohlaysizmi?' Muloyim taklif; 'Do you want…?' dan ko'ra odobliroq.",
              "/tʃ/ o'zbekcha 'ch' ga o'xshash — oson tovush; ammo 'chair' ni 'cher' emas /tʃeə/ deb mashq qiling."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "Ss-Ss", "Ss-Ss", "T-Ss"),
    ),
    Lesson.std(
        title="Plants we eat",
        focus="CLIL Science — What parts of plants can we eat?",
        aims=["name the parts of a plant we eat: roots, stems, leaves, flowers, fruit, seeds",
              "say: We eat the roots of a carrot"],
        language=["roots · stem · leaves · fruit · seeds", "We eat the (roots) of a (carrot)."],
        materials=["Student's Book CLIL pages", "real carrot, celery or cabbage, apple, rice", "a plant diagram"],
        greeting="Show a carrot: 'Is this a fruit or a vegetable? Which part of the plant is it?'",
        warmup="**Which part?** Show real items; pupils point to the diagram part.",
        present="Teach the plant parts with the diagram. Sort items: carrot (root), celery (stem), cabbage (leaves), "
                "apple (fruit), rice (seeds).",
        practice="Student's Book CLIL activities; pupils complete a two-column table: Plant | Part we eat.",
        produce="**Plant plate**: pupils draw a plate with a meal using six parts of plants and label them.",
        wrap="Pupils read their plate labels to a partner. Homework.",
        homework="Find three vegetables at home and say which part we eat.",
        assessment="Sorting table (6 items) and plate rubric: labels (1), accuracy (1), neatness (1).",
        tips=["Mahalliy misollar: sabzi (root), ko'k piyoz (leaves), olma (fruit), guruch (seed) — palov mavzusi bolalarga "
              "tanish.",
              "Support: pictures for each part. Extension: write a full sentence for each part."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "S", "Ss-Ss"),
    ),
    Lesson.std(
        title="Unit 7 revision and quiz",
        focus="Revision of Unit 7; quick quiz",
        aims=["use fruit vocabulary and There are / aren't any accurately", "complete the unit quiz"],
        language=["All language from Unit 7"],
        materials=["Quiz (worksheets/quiz.pdf)", "Bingo (games/bingo.pdf)", "Flashcards"],
        greeting="Greet and set the goal: 'Show what you know about the market.'",
        warmup="**Bingo** with the ten fruit and vegetables (8 different cards ready to print).",
        present="Mind-map on the board: fruit and vegetables, there are lots of / some / any, questions.",
        practice="Pairs: Pairs game; correct three wrong sentences (There is lots of grapes / Are there some pears?).",
        produce="Quiz (15 minutes, 20 points). Collect and mark with the key.",
        wrap="Go over common mistakes; praise progress.",
        homework="Correct your quiz mistakes.",
        assessment="Mark with the answer keys and record results.",
        tips=[GRADE_TIP_20, "Weak pupils: read instructions aloud. Extension: write a dialogue at a fruit stall."],
        interactions=("T-Ss", "Ss-Ss", "T-Ss", "Ss-Ss", "S", "T-Ss"),
    ),
]

A = [
    PicLabel("Look and write the words.", items=[
        ("lemon", "lemons"), ("watermelon", "watermelons"), ("coconut", "coconuts"), ("grapes", "grapes"),
        ("mango", "mangoes"), ("pineapple", "pineapples"), ("pear", "pears"), ("tomato", "tomatoes")], cols=4),
    Match("Match the singular to the plural.", pairs=[
        ("a tomato", "tomatoes"), ("a mango", "mangoes"), ("a lemon", "lemons"), ("an onion", "onions"),
        ("a pear", "pears"), ("a pineapple", "pineapples")], seed=81),
    Gaps("Look and complete the words.", items=[
        ("lemon", "lemons"), ("watermelon", "watermelons"), ("coconut", "coconuts"),
        ("pineapple", "pineapples"), ("tomato", "tomatoes"), ("onion", "onions")]),
    WordSearch("Find the fruit and vegetables.", words=["lemons", "limes", "grapes", "mangoes", "pears",
                                                        "tomatoes", "onions", "coconuts"], size=11, seed=13),
    OddOne("Circle the odd one out.", rows=[
        (["mangoes", "pears", "onions", "grapes"], "onions"),
        (["onions", "tomatoes", "carrots", "pears"], "pears"),
        (["watermelons", "pineapples", "mangoes", "potatoes"], "potatoes")]),
    Draw("Draw your fruit stall. Label five things.", prompts=["My market stall"]),
]

B = [
    Circle("Circle the correct words.", items=[
        "There {*are|is} lots of grapes.",
        "There {*are|is} some tomatoes.",
        "There aren't {*any|some} limes.",
        "{*Are|Is} there any pears?",
        "Yes, there {*are|is}.",
        "No, there {*aren't|isn't}."]),
    Reading("Read and answer.", title="At the market", text=(
        "It is Saturday. Malika and her mum are at the market. There are lots of tomatoes and onions. "
        "There are some pears and grapes. There aren't any mangoes today.\n\n"
        "Malika likes pineapples, but there aren't any. Mum buys tomatoes, pears and lemons."), questions=[
        ("Are there any mangoes?", "No, there aren't."),
        ("Are there any pears?", "Yes, there are."),
        ("What does Mum buy?", "Tomatoes, pears and lemons.")]),
    Fill("Complete the sentences.", items=[
        "There {are} lots of grapes.",
        "There {aren't} any limes.",
        "{Are} there any pears? — Yes, there {are}.",
        "There are {some} tomatoes."], extra_words=["is"]),
    Unscramble("Put the words in the right order.", items=[
        "There are lots of grapes.", "Are there any pears?", "No, there aren't.", "There aren't any limes."]),
    WriteAbout("Write about a market stall.", frames=[
        "There are lots of ___ .", "There are some ___ .", "There aren't any ___ ."], lines=3,
        model=["There are lots of grapes. There are some pears. There aren't any mangoes."]),
]

QUIZ = [
    Section("Part 1 · Words", [
        PicLabel("Look and write the words.", items=[
            ("lemon", "lemons"), ("grapes", "grapes"), ("mango", "mangoes"), ("pineapple", "pineapples"),
            ("tomato", "tomatoes"), ("onion", "onions")], bank=False, cols=3, size=34)]),
    Section("Part 2 · Grammar", [
        Circle("Circle the correct word.", items=[
            "There {*are|is} some pears.",
            "There aren't {*any|some} lemons.",
            "{*Are|Is} there any onions?",
            "No, there {*aren't|isn't}."]),
        Fill("Complete the sentences.", items=[
            "There {are} lots of watermelons.",
            "There {aren't} any coconuts.",
            "{Are} there any grapes? — Yes, there are.",
            "There are {some} tomatoes."], extra_words=["is"])]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="Anna's stall", text=(
            "Anna has a fruit stall. There are lots of pears and some pineapples. "
            "There aren't any grapes today. She has two baskets of lemons."), questions=[
            ("Are there any pineapples?", "Yes, there are."),
            ("Are there any grapes?", "No, there aren't."),
            ("What has she got in two baskets?", "Lemons.")]),
        Unscramble("Put the words in the right order.", items=[
            "There are some pears.", "Are there any mangoes?", "There aren't any limes."])]),
]

SPEC = UnitSpec(number=7, slug="unit-7-at-the-market", title="At the market", info=INFO, vocab=VOCAB,
                extra_vocab=EXTRA, lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="Fruit and vegetables", sheet_b_name="There are / aren't any, Are there any…?")
