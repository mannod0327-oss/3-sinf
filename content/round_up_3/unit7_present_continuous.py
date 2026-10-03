"""Round-Up 3 · mini-unit 7 — present continuous (Round-Up Unit 8)."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, PicLabel, Reading, Section, Unscramble, WordSearch, WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.model import Box, Heading, Para, Table
from sinf.unit import UnitSpec, V

from .common import BADGE, GRADE_TIP_20

VOCAB = [
    V("run", "yugurmoq", "run"), V("swim", "suzmoq", "swimming"), V("read", "o'qimoq", "read"),
    V("write", "yozmoq", "write"), V("sing", "kuylamoq", "sing"), V("dance", "raqsga tushmoq", "dance"),
    V("cook", "pishirmoq", "pot"), V("draw", "rasm chizmoq", "paint"), V("play football", "futbol o'ynamoq", "football"),
    V("sleep", "uxlamoq", "sleep"),
]
EXTRA = [V("now", "hozir", None), V("at the moment", "hozirgi paytda", None), V("Look!", "Qara!", None),
         V("Listen!", "Eshit!", None)]

INFO = UnitInfo(
    number=7, title="Present continuous", topic="What is happening now",
    book="Round-Up 3, Unit 8 — Present continuous",
    vocabulary="run, swim, read, write, sing, dance, cook, draw, play football, sleep (+ now, at the moment, Look!, Listen!)",
    grammar=["am / is / are + verb-ing (running, making, swimming)",
             "negative: I'm not · he isn't · they aren't; questions: Is she …? Are they …?",
             "now (present continuous) vs every day (present simple)"],
)

CARD = [
    Heading("Present continuous — now!", 1),
    Table([["", "+", "−", "?"],
           ["I", "I **am** read**ing**.", "I **am not** reading.", "**Am** I reading?"],
           ["he / she / it", "She **is** sing**ing**.", "She **isn't** singing.", "**Is** she singing?"],
           ["you / we / they", "They **are** danc**ing**.", "They **aren't** dancing.", "**Are** they dancing?"],
           ["short answers", "Yes, I **am**. / Yes, she **is**.", "No, I'm **not**. / No, she **isn't**.", ""]],
          widths=[0.2, 0.27, 0.27, 0.26], header=True, style="grid", size=10.5),
    Table([["+ ing", "drop e + ing", "double the letter + ing"],
           ["play → playing\nread → reading", "make → making\ndance → dancing", "run → running\nswim → swimming\nsit → sitting"]],
          widths=[0.3, 0.3, 0.4], header=True, style="grid", size=10.5),
    Box([Para("**now, at the moment, Look!, Listen!** → present continuous. **every day, always, usually** → present simple.")],
        kind="grammar", title="Which one?"),
    Box([Para("Ko'p xato: 'I reading' (am tushib qoladi). 'Men o'qiyapman' = 'I **am** reading'. "
              "Har doim **am / is / are + -ing**.")], kind="tip", title="Eslatma"),
]

LESSONS = [
    Lesson.std(
        title="What is she doing?",
        focus="Present continuous — statements and -ing spelling",
        aims=["say what people are doing now: She is reading", "spell -ing correctly (make → making, run → running)"],
        language=["I am reading · he is singing · they are dancing", "running · swimming · making"],
        materials=["Action flashcards", "Grammar card", "Worksheet A exercises A–C"],
        greeting="Ask 'What are you doing now?' — 'I'm sitting. I'm listening.'",
        warmup="**Freeze mime**: pupils mime an action; you freeze them and ask the class 'What is he doing?'",
        present="Mime and say 'I am reading.' Write am / is / are + -ing on the board and colour the parts. Show three spelling "
                "rules with examples (play, make, run).",
        practice="Worksheet A exercises A (circle), B (label the pictures) and C (write the -ing form).",
        produce="**Picture talk**: pairs describe what people in a picture are doing: 'The girl is dancing. The boys are "
                "running.'",
        wrap="Quick-fire: teacher mimes; pupils say the full sentence. Homework.",
        homework="Write six sentences about what people in your family are doing now.",
        assessment="Check am / is / are and the -ing spelling.",
        tips=["O'zbekcha '-yapti, -moqda' (o'qiyapti) = inglizcha **am/is/are + -ing**. O'xshashlikdan foydalaning.",
              "Eng ko'p xato: 'She reading' (is tushib qolgan). Har gapda bog'lovchi fe'lni baland ayting.",
              "Support: -ing cards. Extension: add negative sentences."],
    ),
    Lesson.std(
        title="Is he running? No, he isn't.",
        focus="Present continuous — negatives, questions and short answers",
        aims=["say what is not happening: He isn't running", "ask and answer: Are they dancing? Yes, they are."],
        language=["He isn't running. · I'm not sleeping.", "Are they dancing? — Yes, they are. / No, they aren't."],
        materials=["Action flashcards", "Worksheet B exercises A–C"],
        greeting="Ask 'Are you sleeping?' — 'No, I'm not.' Elicit short answers.",
        warmup="**Yes / no mime**: one pupil mimes; the class asks 'Are you swimming?' until they guess.",
        present="Write the negative (am not, isn't, aren't) and the question pattern (Am I, Is he, Are they) on the board. "
                "Show short answers.",
        practice="Worksheet B exercises A (circle), B (fill in) and C (unscramble).",
        produce="**Yes / no 20 questions**: one pupil chooses a picture; the class asks 'Is she running?' (yes / no) to find it.",
        wrap="Teacher says a wrong sentence about a picture; pupils correct it: 'No, she isn't reading. She's writing.' Homework.",
        homework="Write three negative sentences and three questions about a picture.",
        assessment="Listen for inversion in questions (Is she …? not She is …?).",
        tips=["Savol: 'Is she reading?' (Is oldinda). O'zbek tilida ohang yoki '-mi' — inglizchada so'z tartibi o'zgaradi.",
              "Qisqa javob: Yes, she **is**. (is'ni qisqartirmang: 'Yes, she's' xato).",
              "Support: question frames. Extension: add What / Where questions (oral)."],
    ),
    Lesson.std(
        title="Now or every day?",
        focus="Present continuous (now) vs present simple (every day)",
        aims=["choose present continuous for now and present simple for habits", "contrast: I read every day. I'm reading now."],
        language=["I play football every Sunday. I'm playing now.", "now · at the moment · every day · usually"],
        materials=["Picture pairs (habit and now)", "Worksheet B exercises D–E"],
        greeting="Write 'every day' and 'now' on the board and ask 'What do you do every day? What are you doing now?'",
        warmup="**Now or every day?** Read sentences; pupils stand for 'now' and sit for 'every day'.",
        present="Show two columns on the board: every day → present simple, now → present continuous. Sort key words and "
                "sample sentences.",
        practice="Worksheet B exercises D (reading) and E (writing).",
        produce="**Mime it**: one pupil mimes an action and the class says 'He is swimming now. He swims every Friday.'",
        wrap="Teacher says key words; pupils hold up 'simple' or 'continuous' cards. Homework.",
        homework="Write two sentences for four verbs: one for every day and one for now.",
        assessment="Mark Worksheet B exercise E for choosing the right tense.",
        tips=["Signal so'zlar yordam beradi: **now, at the moment, Look!** → -ing. **every day, usually, always** → -s.",
              "Ikkalasini bir jadvalda ranglab ko'rsating: ko'k — odat, qizil — hozir.",
              "Support: signal-word table. Extension: add a third column (yesterday — later)."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "S", "T-Ss"),
    ),
]

A = [
    Circle("Circle the correct words.", items=[
        "She {*is|are} reading.", "They {*are|is} dancing.", "I {*am|is} writing.", "He is {*running|runing}.",
        "We are {*swimming|swiming}.", "She is {*making|makeing} a cake."]),
    PicLabel("Look and write the -ing words.", items=[
        ("run", "running"), ("swimming", "swimming"), ("read", "reading"), ("write", "writing"), ("sing", "singing"),
        ("dance", "dancing"), ("pot", "cooking"), ("paint", "drawing")], cols=4),
    Fill("Write the -ing form.", items=[
        "He is {running} (run).", "She is {making} (make) a cake.", "They are {swimming} (swim).",
        "I am {dancing} (dance).", "We are {sitting} (sit)."], bank=False),
    Match("Match the verb to its -ing form.", pairs=[
        ("play", "playing"), ("make", "making"), ("run", "running"), ("swim", "swimming"), ("dance", "dancing"),
        ("read", "reading")], seed=351),
    WordSearch("Find eight -ing words.", words=["running", "swimming", "reading", "writing", "singing", "dancing",
                                                "cooking", "drawing"], size=11, seed=27),
    Draw("Draw what you are doing now. Write: I am ___ing.", prompts=["I am ________ ing."]),
]

B = [
    Circle("Circle the correct words.", items=[
        "He {*isn't|don't} running.", "I {*'m not|isn't} sleeping.", "{*Is|Does} she singing?",
        "{*Are|Is} they dancing?", "Yes, she {*is|does}.", "No, they {*aren't|don't}."]),
    Fill("Complete the sentences with am, is, are, isn't or aren't.", items=[
        "She {is} cooking plov.", "They {aren't} sleeping. They are playing.", "{Are} you reading? — Yes, I {am}.",
        "He {isn't} swimming. He is running."], bank=True),
    Unscramble("Put the words in the right order.", items=[
        "Is she reading?", "They aren't sleeping.", "I am writing a letter.", "He isn't running."]),
    Reading("Read and answer.", title="In the park", text=(
        "It is Saturday. Aziz and Malika are in the park. Aziz is running with his dog. Malika is reading a book on the "
        "bench.\n\n"
        "Two boys are playing football. A girl is singing. The dog isn't sleeping — it is running after a ball!"),
        questions=[("Who is running with a dog?", "Aziz."), ("What is Malika doing?", "She is reading a book."),
                   ("Is the dog sleeping?", "No, it isn't.")]),
    WriteAbout("Write about a picture of a park or a school yard (now) and about what you do every day.", frames=[
        "Look! A boy is ___ing.", "Now I am ___ing.", "Every day I ___ ."], lines=3,
        model=["Look! A boy is running. Now I am writing. Every day I walk to school."]),
]

QUIZ = [
    Section("Part 1 · -ing words", [
        PicLabel("Look and write the -ing words.", items=[
            ("run", "running"), ("swimming", "swimming"), ("read", "reading"), ("write", "writing"),
            ("dance", "dancing"), ("sing", "singing")], bank=False, cols=3, size=34)]),
    Section("Part 2 · Grammar", [
        Circle("Circle the correct word.", items=[
            "She {*is|are} dancing.", "They {*aren't|isn't} sleeping.", "{*Are|Is} you reading?",
            "He is {*making|makeing} a cake."]),
        Fill("Complete the sentences.", items=[
            "I {am} writing now.", "We {are} swimming.", "{Is} he running? — No, he isn't.",
            "They {aren't} singing."], extra_words=["is"])]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="Now", text=(
            "Look! Dilnoza is dancing. Bobur is playing football. The cat isn't sleeping. It is running."),
            questions=[("What is Dilnoza doing?", "She is dancing."), ("Who is playing football?", "Bobur."),
                       ("Is the cat sleeping?", "No, it isn't.")]),
        Unscramble("Put the words in the right order.", items=[
            "She is singing.", "Are they running?", "I'm not sleeping."])]),
]

SPEC = UnitSpec(number=7, slug="unit-7-present-continuous", title="Present continuous", info=INFO, vocab=VOCAB,
                extra_vocab=EXTRA, lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="-ing forms", sheet_b_name="Negatives, questions, now vs every day", card=CARD,
                intro_note="Adapted for Grade 3 (age 8–9, CEFR A1): the ideas come from the Round-Up 3 unit; all "
                           "exercises and texts are new.")
