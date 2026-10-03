"""Round-Up 3 · mini-unit 6 — present simple (Round-Up Unit 7)."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, PicLabel, Reading, Section, Unscramble, WordSearch, WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.model import Box, Heading, Para, Table
from sinf.unit import UnitSpec, V

from .common import BADGE, GRADE_TIP_20

VOCAB = [
    V("get up", "uyg'onmoq", "get up"), V("eat", "yemoq", "eat"), V("drink", "ichmoq", "drink"),
    V("read", "o'qimoq", "read"), V("play", "o'ynamoq", "football"), V("watch", "tomosha qilmoq", "tv"),
    V("study", "o'qimoq, o'rganmoq", "homework"), V("walk", "piyoda yurmoq", "walk"), V("sleep", "uxlamoq", "sleep"),
    V("cook", "pishirmoq", "pot"),
]
EXTRA = [
    V("always", "doim", None), V("usually", "odatda", None), V("sometimes", "ba'zan", None),
    V("never", "hech qachon", None), V("every day", "har kuni", None),
]

INFO = UnitInfo(
    number=6, title="Present simple", topic="What we do every day; habits and routines",
    book="Round-Up 3, Unit 7 — Present simple",
    vocabulary="get up, eat, drink, read, play, watch, study, walk, sleep, cook (+ always, usually, sometimes, never)",
    grammar=["I / you / we / they + verb; he / she / it + verb-s (-es, -ies)",
             "don't / doesn't + verb; Do / Does + subject + verb?",
             "adverbs of frequency: always, usually, sometimes, never"],
)

CARD = [
    Heading("Present simple — every day", 1),
    Table([["", "+", "−", "?"],
           ["I / you / we / they", "I **play** football.", "I **don't play** football.", "**Do** you **play** football?"],
           ["he / she / it", "He **plays** football.", "He **doesn't play** football.", "**Does** he **play** football?"],
           ["short answers", "Yes, I **do**. / Yes, he **does**.", "No, I **don't**. / No, he **doesn't**.", ""]],
          widths=[0.2, 0.27, 0.27, 0.26], header=True, style="grid", size=10.5),
    Table([["+ s", "+ es (s, sh, ch, x, o)", "y → ies"],
           ["play → plays\nread → reads", "watch → watches\ngo → goes · do → does\nwash → washes", "study → studies"]],
          widths=[0.3, 0.4, 0.3], header=True, style="grid", size=10.5),
    Box([Para("always · usually · sometimes · never — **before** the verb: She **always** eats breakfast. "
              "(after *am / is / are*: He is **never** late.)")], kind="grammar", title="How often?"),
    Box([Para("Uchinchi shaxs (he, she, it) da fe'lga **-s / -es** qo'shiladi: 'He play' emas, 'He plays'. "
              "'doesn't' dan keyin -s **yo'q**: He doesn't play (plays emas).")], kind="tip", title="Eslatma"),
]

LESSONS = [
    Lesson.std(
        title="He plays, she watches",
        focus="Present simple — affirmative; the third-person -s / -es / -ies",
        aims=["say what people do every day using I / we / they and he / she", "spell -s, -es and -ies endings"],
        language=["I play · she plays · he watches · she goes · he studies"],
        materials=["Verb flashcards", "Grammar card", "Worksheet A exercises A–C"],
        greeting="Ask three pupils 'What do you do after school?' and write the answers on the board.",
        warmup="**Mime and guess**: mime a verb; pupils say 'He plays!' (third person).",
        present="Write two columns: I / we / they (no change) and he / she / it (+ s). Sort the verbs; highlight -es "
                "(watches, goes, does) and -ies (studies).",
        practice="Worksheet A exercises A (circle), B (label) and C (fill in with the verb in brackets).",
        produce="**Family facts**: pupils write and say three sentences about a family member: 'My dad drinks tea. He reads "
                "a book.'",
        wrap="Quick-fire: teacher says a pronoun + verb; pupils say the full sentence. Homework.",
        homework="Write six sentences about what people in your family do every day.",
        assessment="Check for missing -s in the family facts.",
        tips=["'-s' qo'shimchasi o'zbek tilida yo'q — **eng ko'p xato**: 'He play'. Doim 'he / she / it + s' "
              "qoidasini baland ovoz bilan takrorlang.",
              "-es / -ies: 'watches' /ɪz/ ni alohida mashq qiling.",
              "Support: give the -s ending on cards. Extension: add adverbs (always, usually)."],
    ),
    Lesson.std(
        title="I don't, he doesn't, do you?",
        focus="Present simple — negatives and questions",
        aims=["say what they and others do not do", "ask and answer Do you …? Does she …?"],
        language=["I don't drink coffee. · She doesn't watch TV.", "Do you play football? — Yes, I do. / No, I don't."],
        materials=["Picture cards", "Worksheet B exercises A–C"],
        greeting="Ask 'Do you watch TV in the morning?' and elicit short answers.",
        warmup="**Truth or lie?** Pupils say sentences about themselves; the class guesses: 'Do you play the piano?'",
        present="Write the negative and question patterns on the board (don't / doesn't + verb; Do / Does + subject + "
                "verb). Underline: after doesn't / does, the verb has **no -s**.",
        practice="Worksheet B exercises A (circle), B (fill in) and C (unscramble).",
        produce="**Find someone who…**: pupils ask 'Do you drink milk?' and write names; then report: 'Bobur doesn't drink "
                "milk.'",
        wrap="Teacher asks five yes / no questions about a picture; pupils answer. Homework.",
        homework="Write five negative sentences about yourself and five questions for a friend.",
        assessment="Listen for do / does and the bare verb after them.",
        tips=["'Does he plays?' — xato; 'does' dan keyin asl fe'l: 'Does he **play**?'.",
              "Qisqa javoblar: Yes, he **does**. / No, he **doesn't**. — ko'p takrorlang.",
              "Support: question frames. Extension: add Wh- words (What do you …?)."],
    ),
    Lesson.std(
        title="How often?",
        focus="Adverbs of frequency: always, usually, sometimes, never",
        aims=["say how often they do things", "interview a partner about daily habits"],
        language=["I always get up at seven. · She usually walks to school. · He never watches TV in the morning."],
        materials=["A frequency line on the board (never — sometimes — usually — always)", "Worksheet B exercises D–E"],
        greeting="Ask 'Do you always eat breakfast?' and show the frequency line.",
        warmup="**Stand on the line**: call a sentence ('I eat breakfast'); pupils stand at always / usually / sometimes / never.",
        present="Show the four adverbs with percentages on the line (100% / 80% / 50% / 0%). Write two sentences: adverb "
                "before the verb.",
        practice="Worksheet B exercises D (reading) and E (writing with adverbs).",
        produce="**Habit interview**: pairs ask 'Do you always …? How often do you …?' and write three sentences about "
                "their partner.",
        wrap="Report: 'Malika never eats cheese.' Homework.",
        homework="Write four sentences with always, usually, sometimes and never about your week.",
        assessment="Check word order (adverb before the verb).",
        tips=["'always / usually / sometimes / never' gapda **fe'l oldida**: 'I **always** eat'. O'zbekchada odatda "
              "fe'l oldida ('men doim yeyman') — bu yerda o'xshashlik bor.",
              "Support: frequency line visible. Extension: add 'every day / twice a week'."],
        interactions=("T-Ss", "G", "T-Ss", "S / Ss-Ss", "Ss-Ss", "T-Ss"),
    ),
]

A = [
    Circle("Circle the correct verb.", items=[
        "He {*plays|play} football.", "They {*play|plays} in the park.", "She {*watches|watchs} TV.",
        "My brother {*studies|studys} English.", "We {*eat|eats} dinner at six.", "It {*sleeps|sleep} all day."]),
    PicLabel("Look and write the verbs.", items=[
        ("get up", "get up"), ("eat", "eat"), ("drink", "drink"), ("read", "read"), ("football", "play"),
        ("tv", "watch"), ("homework", "study"), ("pot", "cook")], cols=4),
    Fill("Write the correct form of the verb.", items=[
        "Aziz {plays} (play) football.", "Malika {reads} (read) a book.", "My mum {cooks} (cook) plov.",
        "He {watches} (watch) TV.", "She {studies} (study) English."], bank=False),
    Gaps("Look and complete the verbs.", items=[
        ("eat", "eat"), ("drink", "drink"), ("read", "read"), ("homework", "study"), ("walk", "walk"),
        ("sleep", "sleep")]),
    WordSearch("Find eight verbs.", words=["drink", "read", "play", "watch", "study", "walk", "sleep", "cook"],
               size=10, seed=26),
    Draw("Draw your morning. Write: I get up at ___ .", prompts=["My morning"]),
]

B = [
    Circle("Circle the correct words.", items=[
        "I {*don't|doesn't} drink coffee.", "She {don't|*doesn't} watch TV.", "{*Do|Does} you play the piano?",
        "{Do|*Does} he read every day?", "No, she {don't|*doesn't}.", "He doesn't {*like|likes} cheese."]),
    Fill("Complete the sentences with do, does, don't or doesn't.", items=[
        "{Do} you like milk? — Yes, I do.", "{Does} she play football? — No, she {doesn't}.",
        "We {don't} eat meat.", "My brother {doesn't} study on Sundays."], bank=True),
    Unscramble("Put the words in the right order.", items=[
        "She doesn't watch TV.", "Do you play football?", "He reads a book every day.", "I never drink coffee."]),
    Reading("Read and answer.", title="Sardor's Saturday", text=(
        "Sardor gets up at eight o'clock on Saturday. He eats breakfast with his family. Then he plays football with his "
        "friends. He never watches TV in the morning.\n\n"
        "In the afternoon he studies English. He usually goes to bed at nine o'clock."), questions=[
        ("What time does Sardor get up?", "At eight o'clock."),
        ("Does he watch TV in the morning?", "No, he doesn't."),
        ("What does he do in the afternoon?", "He studies English.")]),
    WriteAbout("Write about a friend's day. Use always, usually, sometimes or never.", frames=[
        "My friend ___ always ___ .", "He / She never ___ .", "He / She sometimes ___ ."], lines=3,
        model=["My friend Dilnoza always eats breakfast. She never watches TV in the morning. She sometimes plays "
               "chess."]),
]

QUIZ = [
    Section("Part 1 · Verbs", [
        PicLabel("Look and write the verbs.", items=[
            ("get up", "get up"), ("eat", "eat"), ("drink", "drink"), ("read", "read"), ("tv", "watch"),
            ("sleep", "sleep")], bank=False, cols=3, size=34)]),
    Section("Part 2 · Grammar", [
        Circle("Circle the correct word.", items=[
            "She {*plays|play} chess.", "He {*doesn't|don't} eat cheese.", "{*Does|Do} he study English?",
            "They {*watch|watches} TV."]),
        Fill("Write the correct form of the verb.", items=[
            "My dad {drinks} (drink) tea.", "Aziz {goes} (go) to school.", "She {doesn't} like milk.",
            "{Do} you play football?"], bank=False)]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="Malika's day", text=(
            "Malika gets up at seven o'clock. She always eats breakfast. She walks to school. "
            "She never watches TV in the morning."), questions=[
            ("What time does Malika get up?", "At seven o'clock."), ("How does she go to school?", "She walks."),
            ("Does she watch TV in the morning?", "No, she doesn't.")]),
        Unscramble("Put the words in the right order.", items=[
            "She doesn't eat meat.", "Does he play football?", "I usually walk to school."])]),
]

SPEC = UnitSpec(number=6, slug="unit-6-present-simple", title="Present simple", info=INFO, vocab=VOCAB,
                extra_vocab=EXTRA, lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="Verbs and the third-person -s", sheet_b_name="Negatives, questions, how often",
                card=CARD,
                intro_note="Adapted for Grade 3 (age 8–9, CEFR A1): the ideas come from the Round-Up 3 unit; all "
                           "exercises and texts are new.")
