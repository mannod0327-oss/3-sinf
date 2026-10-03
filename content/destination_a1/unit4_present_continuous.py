"""Destination A1 · mini-unit 4 — present continuous: at the park (Destination Unit 5)."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, PicLabel, Reading, Section, Unscramble, WordSearch, WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.model import Box, Heading, Para, Table
from sinf.unit import UnitSpec, V

from .common import BADGE, NOTE

VOCAB = [
    V("wash my hands", "qo'limni yuvmoq", "soap"), V("listen to music", "musiqa tinglamoq", "music"),
    V("talk", "gaplashmoq", "speech"), V("eat lunch", "tushlik qilmoq", "eat"), V("drink juice", "sharbat ichmoq", "drink"),
    V("ride a bike", "velosiped haydamoq", "bike"), V("fly a kite", "varrak uchirmoq", "kite"),
    V("take photos", "rasmga olmoq", "camera"), V("play chess", "shaxmat o'ynamoq", "chess"),
    V("climb a tree", "daraxtga chiqmoq", "climb"),
]
EXTRA = [V("now", "hozir", None), V("at the moment", "hozirgi paytda", None), V("Look!", "Qara!", None),
         V("park", "bog' (park)", "tree")]

INFO = UnitInfo(
    number=4, title="Present continuous: at the park", topic="What are people doing now?",
    book="Destination A1, Unit 5 — Present continuous",
    vocabulary="wash my hands, listen to music, talk, eat lunch, drink juice, ride a bike, fly a kite, take photos, "
               "play chess, climb a tree",
    grammar=["am / is / are + verb-ing: She is riding a bike.",
             "negative: He isn't eating. · They aren't talking.",
             "questions: What are you doing? · Is he flying a kite? — Yes, he is."],
)

CARD = [
    Heading("What are they doing? — present continuous", 1),
    Table([["+", "−", "?"],
           ["I **am** eat**ing**.\nShe **is** ride**ing** → riding.\nThey **are** talk**ing**.",
            "I **am not** eating.\nHe **isn't** flying a kite.\nThey **aren't** talking.",
            "**What** are you doing?\n**Is** she riding a bike? — Yes, she **is**.\n**Are** they talking? — No, they **aren't**."]],
          widths=[0.33, 0.33, 0.34], header=True, style="grid", size=10.5),
    Table([["+ ing", "drop e + ing", "double letter + ing"],
           ["play → playing\nclimb → climbing", "ride → riding\ntake → taking\nmake → making", "run → running\nswim → swimming\nsit → sitting"]],
          widths=[0.3, 0.3, 0.4], header=True, style="grid", size=10.5),
    Box([Para("**Look! Listen! now! at the moment!** → present continuous.")], kind="grammar", title="Signal words"),
    Box([Para("'U velosiped haydayapti' = 'He **is** riding a bike' — 'is' ni tushirmang. Har gapda **am / is / are**.")],
        kind="tip", title="Eslatma"),
]

LESSONS = [
    Lesson.std(
        title="At the park",
        focus="Vocabulary — ten actions people do in the park",
        aims=["name ten actions", "say what a person is doing in a picture"],
        language=["wash my hands, listen to music, talk, eat lunch, drink juice, ride a bike, fly a kite, take photos, "
                  "play chess, climb a tree"],
        materials=["Flashcards (games/flashcards.pdf)", "A big picture of a park with many people", "Worksheet A exercises A–B"],
        greeting="Show a picture of a park: 'Where is this? What can you see?'",
        warmup="**Mime and guess**: pupils mime actions; the class says 'You are riding a bike!'",
        present="Present the ten flashcards with actions. Choral repetition. Stick cards on the park picture.",
        practice="Worksheet A exercises A (label), B (match with Uzbek) and C (complete the words).",
        produce="**Spot the person**: you describe a person in the park picture ('He is flying a kite.'); pupils point.",
        wrap="Teacher mimes; pupils say the action. Homework.",
        homework="Learn the ten phrases and draw a park scene (Worksheet A exercise F).",
        assessment="Point at cards for 5 pupils; note gaps.",
        tips=["'take photos' va 'take a photo' — ikkalasi ham to'g'ri; 'make photos' xato.",
              "'wash my hands', 'fly a kite' — butun ibora sifatida yodlating.",
              "Support: pictures only. Extension: add 'feed ducks', 'play football'."],
    ),
    Lesson.std(
        title="She is riding a bike",
        focus="Present continuous: statements and negatives; -ing spelling",
        aims=["say and write what people are doing and are not doing", "spell -ing forms (riding, taking, running)"],
        language=["She is riding a bike. · They aren't talking.", "ride → riding · take → taking · sit → sitting"],
        materials=["Park picture", "Worksheet A exercises C–E; Worksheet B exercise A"],
        greeting="Ask 'What are you doing now?' — 'I'm sitting. I'm listening.'",
        warmup="**Freeze!** Pupils mime an action; you freeze them: 'What is he doing?'",
        present="Write am / is / are + -ing on the board and the three spelling rules with examples. Use the park picture: "
                "'The girl is flying a kite. The boys aren't eating.'",
        practice="Worksheet A exercises C (complete), D (word search) and E (-ing forms); Worksheet B exercise A (circle).",
        produce="**Describe the picture**: pairs write five sentences about people in the park picture.",
        wrap="Pairs read one sentence aloud; the class says true or false. Homework.",
        homework="Write six sentences about the people in a picture.",
        assessment="Check am / is / are and -ing spelling.",
        tips=["O'zbekcha '-yapti' = am/is/are + -ing. 'She riding' xatosi: 'is' ni qo'shing.",
              "Imlo: ride → riding (e tushadi), run → running (undosh ikkilanadi).",
              "Support: spelling cards. Extension: add negatives for every sentence."],
    ),
    Lesson.std(
        title="What are they doing?",
        focus="Present continuous: questions and short answers",
        aims=["ask and answer: What is he doing? Is she riding a bike? — Yes, she is.", "describe a picture in 5 sentences"],
        language=["What are you doing? · Is he flying a kite? — Yes, he is. / No, he isn't.", "Are they talking? — Yes, they are."],
        materials=["Picture cards", "Worksheet B exercises B–E"],
        greeting="Mime an action and ask 'What am I doing?' Elicit full sentences.",
        warmup="**Yes / no guess**: a pupil chooses a hidden action card; the class asks 'Are you riding a bike?'",
        present="Write the question patterns on the board: What + am / is / are + subject + -ing? and Is / Are + subject + -ing? "
                "with short answers.",
        practice="Worksheet B exercises B (fill in), C (unscramble) and D (reading).",
        produce="**Park detectives**: pairs have two park pictures with five differences; they ask 'Is the boy eating?' to find "
                "them.",
        wrap="Report: 'In my picture the girl is flying a kite, but in yours she is riding a bike.' Homework.",
        homework="Write five questions about a picture and their answers.",
        assessment="Listen for inversion in questions (Is he …? not He is …?).",
        tips=["Savol: 'Is he flying?' (Is oldinda). O'zbekchada '-mi' yuklamasi — inglizchada so'z tartibi o'zgaradi.",
              "Qisqa javob: Yes, he **is**. (not 'Yes, he's')."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "S / Ss-Ss", "Ss-Ss", "T-Ss"),
    ),
]

A = [
    PicLabel("Look and write the phrases.", items=[
        ("soap", "wash my hands"), ("music", "listen to music"), ("speech", "talk"), ("eat", "eat lunch"),
        ("drink", "drink juice"), ("bike", "ride a bike"), ("kite", "fly a kite"), ("camera", "take photos")], cols=4),
    Match("Match the English phrase to the Uzbek phrase.", pairs=[
        ("ride a bike", "velosiped haydamoq"), ("fly a kite", "varrak uchirmoq"), ("take photos", "rasmga olmoq"),
        ("play chess", "shaxmat o'ynamoq"), ("climb a tree", "daraxtga chiqmoq"),
        ("listen to music", "musiqa tinglamoq")], seed=511),
    Gaps("Look and complete the words.", items=[
        ("music", "music"), ("camera", "photos"), ("kite", "kite"), ("drink", "juice"), ("soap", "hands"),
        ("chess", "chess")]),
    WordSearch("Find eight words.", words=["music", "photos", "kite", "juice", "chess", "tree", "bike", "lunch"],
               size=10, seed=34),
    Fill("Write the -ing form.", items=[
        "She is {riding} (ride) a bike.", "He is {taking} (take) photos.", "They are {running} (run) in the park.",
        "I am {sitting} (sit) on the bench.", "We are {flying} (fly) a kite."], bank=False),
    Draw("Draw yourself in the park. Write: I am ___ing.", prompts=["I am ________ ing."]),
]

B = [
    Circle("Choose the correct word (A, B or C).", items=[
        "She {*is|are|am} riding a bike.", "They {am|is|*are} playing chess.", "I {*am|is|are} listening to music.",
        "He {*isn't|aren't|don't} eating lunch.", "{*Is|Are|Does} she flying a kite?", "{Is|*Are|Do} they talking?"]),
    Fill("Complete the sentences.", items=[
        "What {are} you doing? — I {am} taking photos.", "{Is} he climbing a tree? — Yes, he {is}.",
        "They {aren't} eating. They are drinking juice."], bank=True),
    Unscramble("Put the words in the right order.", items=[
        "She is riding a bike.", "They aren't talking.", "What are you doing?", "Is he flying a kite?"]),
    Reading("Read and answer.", title="Saturday in the park", text=(
        "It is Saturday. Dilnoza and Aziz are in the park. Dilnoza is riding her bike. Aziz is flying a kite.\n\n"
        "Two boys are playing chess. A man is taking photos. A girl is drinking juice. Nobody is sleeping!"), questions=[
        ("What is Dilnoza doing?", "She is riding her bike."), ("Is Aziz flying a kite?", "Yes, he is."),
        ("Is anybody sleeping?", "No, nobody is.")]),
    WriteAbout("Write about people in a park (look at a picture or imagine).", frames=[
        "A boy is ___ing.", "Two girls are ___ing.", "A man isn't ___ing.", "I am ___ing."], lines=4,
        model=["A boy is flying a kite. Two girls are riding bikes. A man isn't sleeping. I am taking photos."]),
]

QUIZ = [
    Section("Part 1 · Words", [
        PicLabel("Look and write the phrases.", items=[
            ("soap", "wash my hands"), ("music", "listen to music"), ("bike", "ride a bike"), ("kite", "fly a kite"),
            ("camera", "take photos"), ("chess", "play chess")], bank=False, cols=3, size=34)]),
    Section("Part 2 · Grammar", [
        Circle("Choose the correct word.", items=[
            "He {*is|are} riding a bike.", "They {*are|is} playing chess.", "She {*isn't|aren't} sleeping.",
            "{*Is|Are} he flying a kite?"]),
        Fill("Write the -ing form.", items=[
            "She is {taking} (take) photos.", "They are {running} (run).", "I am {listening} (listen) to music.",
            "He is {riding} (ride) a bike."], bank=False)]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="Look!", text=(
            "Look! Malika is flying a kite. Her brother is climbing a tree. Their dad is taking photos. "
            "Their mum isn't talking — she is listening to music."), questions=[
            ("What is Malika doing?", "She is flying a kite."), ("Who is climbing a tree?", "Her brother."),
            ("Is their mum talking?", "No, she isn't.")]),
        Unscramble("Put the words in the right order.", items=[
            "He is riding a bike.", "Are they playing chess?", "I'm not sleeping."])]),
]

SPEC = UnitSpec(number=4, slug="unit-4-present-continuous-park", title="Present continuous: at the park", info=INFO,
                vocab=VOCAB, extra_vocab=EXTRA, lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ, badge=BADGE,
                sheet_a_name="Park actions and -ing forms", sheet_b_name="Statements, questions, reading, writing",
                card=CARD, intro_note=NOTE)
