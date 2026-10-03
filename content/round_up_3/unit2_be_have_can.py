"""Round-Up 3 · mini-unit 2 — be, have got, can (Round-Up Unit 2)."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, PicLabel, Reading, Section, Unscramble, WordSearch, WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.model import Box, Heading, Para, Table
from sinf.unit import UnitSpec, V

from .common import BADGE, GRADE_TIP_20

VOCAB = [
    V("swim", "suzmoq", "swimming"), V("run", "yugurmoq", "run"), V("jump", "sakramoq", "jump"),
    V("ride a bike", "velosiped haydamoq", "bike"), V("sing", "kuylamoq", "sing"), V("dance", "raqsga tushmoq", "dance"),
    V("draw", "rasm chizmoq", "paint"), V("play football", "futbol o'ynamoq", "football"),
    V("climb", "tirmashmoq", "climb"), V("fly", "uchmoq", "fly"),
]
EXTRA = [
    V("I", "men", None), V("you", "sen, siz", None), V("he", "u (erkak)", None), V("she", "u (ayol)", None),
    V("it", "u (hayvon, narsa)", None), V("we", "biz", None), V("they", "ular", None),
]

INFO = UnitInfo(
    number=2, title="be, have got, can", topic="Who I am, what I have and what I can do",
    book="Round-Up 3, Unit 2 — Personal pronouns / 'be' / 'have got' / 'can'",
    vocabulary="swim, run, jump, ride a bike, sing, dance, draw, play football, climb, fly; pronouns I, you, he, she, it, "
               "we, they",
    grammar=["be: I am · he / she / it is · you / we / they are (+ negative and questions)",
             "have got: I / you / we / they have got · he / she / it has got",
             "can / can't + verb: She can swim. He can't fly."],
)

CARD = [
    Heading("be · have got · can", 1),
    Table([["", "be", "have got", "can"],
           ["I", "I **am** ten.", "I **have got** a bike.", "I **can** swim."],
           ["you", "You **are** my friend.", "You **have got** a cat.", "You **can** run."],
           ["he / she / it", "He **is** tall.", "She **has got** a dog.", "It **can** fly."],
           ["we / they", "We **are** at school.", "They **have got** a car.", "They **can** sing."],
           ["−", "I **am not** / she **isn't** / they **aren't**", "I **haven't got** / he **hasn't got**",
            "I **can't** / she **can't**"],
           ["?", "**Are** you ten? Yes, I **am**.", "**Has** she got a cat? No, she **hasn't**.",
            "**Can** you swim? Yes, I **can**."]],
          widths=[0.15, 0.29, 0.29, 0.27], header=True, style="grid", size=10),
    Box([Para("**can** + verb without -s or 'to': He can swim (not 'he cans swim', not 'he can to swim').")],
        kind="grammar", title="Remember"),
    Box([Para("'Men bolaman' = 'I **am** a boy' — inglizchada 'am / is / are' tushirib qoldirilmaydi. "
              "'Menda mushuk bor' = 'I **have got** a cat'. 'Men suza olaman' = 'I **can** swim'.")],
        kind="tip", title="Eslatma"),
]

LESSONS = [
    Lesson.std(
        title="I am, you are, he is",
        focus="be with pronouns; negatives and questions",
        aims=["use am / is / are with I, you, he, she, it, we, they", "ask and answer: Are you ten? Yes, I am."],
        language=["I am · you are · he / she / it is · we / you / they are", "I'm not · isn't · aren't · Are you …?"],
        materials=["Pronoun cards (I, you, he, she, it, we, they)", "Grammar card", "Worksheet A exercise A; Worksheet B exercise B"],
        greeting="Greet the class and introduce yourself: 'I am Miss … I am a teacher.' Invite pupils to do the same.",
        warmup="**Pronoun pick**: point to people and say the pronoun (you, he, she, we, they) — pupils repeat.",
        present="Write the table on the board: I am / you are / he is … Colour the forms. Use the contractions I'm, you're, "
                "he's. Then show the negative (I'm not / he isn't) and questions (Are you …?).",
        practice="Worksheet A exercise A (circle) and Worksheet B exercise B (fill in). Pairs check each other.",
        produce="**Mingle**: pupils ask 'Are you nine?' 'Are you from Tashkent?' and answer with short answers.",
        wrap="Quick-fire: point at a pupil and say a pronoun; pupils say the full sentence 'He is …'. Homework.",
        homework="Write five sentences about yourself with am / is / are.",
        assessment="Listen for am / is / are in the mingle activity.",
        tips=["'am / is / are' ni tushirmaslik: o'zbekcha 'Men ikkinchi sinfman' da bog'lovchi fe'l yo'q — "
              "inglizchada esa shart.",
              "he / she — o'zbekcha 'u' ikkalasi uchun bitta: rasm bilan farqlang.",
              "Support: show a pronoun–verb matching chart. Extension: add a question with Wh- words (oral)."],
    ),
    Lesson.std(
        title="I've got, she's got",
        focus="have got / has got (statements, negatives, questions)",
        aims=["say what they and others have got", "ask and answer: Has she got a cat? No, she hasn't."],
        language=["I've got · he's got · they've got", "haven't got · hasn't got · Have you got …? Has she got …?"],
        materials=["Picture cards (cat, dog, bike, computer, car)", "Worksheet A exercise B; Worksheet B exercise D"],
        greeting="Ask 'Have you got a pet?' and collect answers on the board.",
        warmup="**Bag reveal**: take items from a bag: 'I've got a book. I've got an apple. Have you got an apple?'",
        present="Show a boy and a girl with pictures. Model 'He has got a bike. She has got two cats.' Write the pattern with "
                "have for I / you / we / they and has for he / she / it.",
        practice="Worksheet A exercise B (fill), Worksheet B exercise D (reading). Pairs ask and answer with picture cards.",
        produce="**Find someone who has got…**: pupils walk around and find classmates with a pet, a bike, a brother.",
        wrap="Report back: 'Bobur has got a bike.' Homework.",
        homework="Write what you and your family have got (six sentences).",
        assessment="Check have / has agreement in the report-back.",
        tips=["'have got' = 'menda bor'. 'He have got' — keng tarqalgan xato; he/she/it → **has**.",
              "Qisqa shakl: I've got, he's got (has got) — 'he's' = he is ham bo'lishi mumkin; kontekst bilan tushuntiring.",
              "Support: use sentence frames. Extension: add number words (two brothers)."],
    ),
    Lesson.std(
        title="I can, I can't",
        focus="can / can't for ability; questions and short answers",
        aims=["say what they and animals can and can't do", "ask and answer: Can you swim? Yes, I can."],
        language=["I can swim. · He can't fly.", "Can you ride a bike? — Yes, I can. / No, I can't."],
        materials=["Ability flashcards (games/flashcards.pdf)", "Worksheet A exercises C–E; Worksheet B exercises A, C, E"],
        greeting="Ask 'Can you swim?' — show thumbs up / down; count the class.",
        warmup="**Animal charades**: mime an animal; the class guesses 'It can fly. It's a bird.'",
        present="Use the ability flashcards: 'I can swim. Can you swim?' Build the pattern on the board, including can't "
                "and the question form. Stress: can + bare verb.",
        practice="Worksheet A exercises C (match animals and abilities), D (word search) and E (pictures). Worksheet B "
                 "exercise A (circle).",
        produce="**Find someone who can…**: pupils ask 'Can you dance? Can you ride a bike?' and record names on a chart.",
        wrap="Class result: 'Nine pupils can swim.' Homework.",
        homework="Write three things you can do and three you can't do (Worksheet B exercise E).",
        assessment="Listen for can + bare verb in the survey.",
        tips=["'can' dan keyin fe'l o'zgarmaydi: She can **swim** (swims emas).",
              "'can't' talaffuzi /kɑːnt/ — 'can' /kæn/ bilan adashtirmang; urg'u va ovoz cho'zilishiga e'tibor.",
              "Support: pictures for each verb. Extension: add adverbs (well, fast)."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "Ss-Ss", "T-Ss"),
    ),
]

A = [
    Circle("Circle am, is or are.", items=[
        "I {*am|is|are} nine years old.", "Aziz {am|*is|are} my friend.", "We {am|is|*are} in Class 3.",
        "They {am|is|*are} at school.", "You {am|is|*are} my best friend.", "It {am|*is|are} a cat."]),
    Fill("Write have or has.", items=[
        "I {have} got a bike.", "Malika {has} got a cat.", "We {have} got a big garden.",
        "He {has} got two brothers.", "They {have} got a dog."], bank=True),
    Match("Match the animal to what it can do.", pairs=[
        ("A fish", "can swim"), ("A bird", "can fly"), ("A rabbit", "can jump"), ("A cat", "can climb"),
        ("A dog", "can run"), ("A parrot", "can talk")], seed=321),
    PicLabel("Look and write what they can do.", items=[
        ("swimming", "swim"), ("run", "run"), ("jump", "jump"), ("bike", "ride a bike"), ("sing", "sing"),
        ("dance", "dance"), ("paint", "draw"), ("football", "play football")], cols=4),
    WordSearch("Find eight verbs.", words=["swim", "run", "jump", "climb", "sing", "dance", "draw", "fly"],
               size=10, seed=22),
    Draw("Draw something you can do. Write: I can ___ .", prompts=["I can ________ ."]),
]

B = [
    Circle("Circle the correct words.", items=[
        "A fish {*can|can't} swim.", "A cat {can|*can't} fly.", "{*Can|Do} you ride a bike?",
        "She can {*swim|swims}.", "He {*can|cans} run fast.", "Dogs {*can't|can} fly."]),
    Fill("Complete the sentences with am, is or are.", items=[
        "Hello! I {am} Sardor.", "This {is} my sister. She {is} seven.", "We {are} in Class 3.",
        "{Is} he your brother? — Yes, he {is}."], bank=True),
    Unscramble("Put the words in the right order.", items=[
        "She has got a cat.", "Can you swim?", "I am not a teacher.", "They haven't got a car."]),
    Reading("Read and answer.", title="Meet Jasur", text=(
        "Hi! I am Jasur. I am ten and I am from Samarkand. I have got a brother and a sister.\n\n"
        "I can swim and ride a bike, but I can't play the guitar. My sister has got a parrot. The parrot can talk!"),
        questions=[("Where is Jasur from?", "He is from Samarkand."),
                   ("What can Jasur do?", "He can swim and ride a bike."),
                   ("What can the parrot do?", "It can talk.")]),
    WriteAbout("Write about yourself.", frames=[
        "I am ___ years old.", "I have got ___ .", "I can ___ but I can't ___ ."], lines=3,
        model=["I am nine years old. I have got a brother and a bike. I can swim but I can't play the guitar."]),
]

QUIZ = [
    Section("Part 1 · Words", [
        PicLabel("Look and write.", items=[
            ("swimming", "swim"), ("sing", "sing"), ("bike", "ride a bike"), ("dance", "dance"), ("jump", "jump"),
            ("run", "run")], bank=False, cols=3, size=34)]),
    Section("Part 2 · Grammar", [
        Circle("Circle the correct word.", items=[
            "She {am|*is|are} nine.", "They {*have|has} got a dog.", "He {*has|have} got a bike.",
            "Fish {*can|cans} swim."]),
        Fill("Complete the sentences.", items=[
            "I {am} ten years old.", "We {are} at school.", "{Can} you run? — Yes, I can.",
            "She {hasn't} got a cat. She has got a dog."], extra_words=["is"])]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="My pets", text=(
            "I have got a cat and a parrot. The cat can climb. The parrot can talk, but it can't swim."),
            questions=[("What has the writer got?", "A cat and a parrot."), ("What can the cat do?", "It can climb."),
                       ("Can the parrot swim?", "No, it can't.")]),
        Unscramble("Put the words in the right order.", items=[
            "I can ride a bike.", "She isn't my sister.", "Have you got a pen?"])]),
]

SPEC = UnitSpec(number=2, slug="unit-2-be-have-got-can", title="be, have got, can", info=INFO, vocab=VOCAB,
                extra_vocab=EXTRA, lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="be, have got, can — forms", sheet_b_name="Use: sentences, reading, writing", card=CARD,
                intro_note="Adapted for Grade 3 (age 8–9, CEFR A1): the ideas come from the Round-Up 3 unit; all "
                           "exercises and texts are new.")
