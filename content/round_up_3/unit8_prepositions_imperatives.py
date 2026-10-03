"""Round-Up 3 · mini-unit 8 — prepositions of place and imperatives (Round-Up Units 13 and 14)."""
from sinf.exercises import (
    Circle, Draw, Fill, Gaps, Match, OddOne, PicLabel, Reading, Section, Unscramble, WordSearch, WriteAbout,
)
from sinf.lesson import Lesson, UnitInfo
from sinf.model import Box, Heading, Para, Table
from sinf.unit import UnitSpec, V

from .common import BADGE, GRADE_TIP_20

VOCAB = [
    V("in", "ichida", "prep-in"), V("on", "ustida", "prep-on"), V("under", "tagida", "prep-under"),
    V("next to", "yonida", "prep-next to"), V("behind", "orqasida", "prep-behind"),
    V("in front of", "oldida", "prep-in front of"), V("between", "orasida", "prep-between"),
]
EXTRA = [
    V("Sit down.", "O'tiring.", "sit"), V("Stand up.", "Turing.", "stand"), V("Open your book.", "Kitobni oching.", "open"),
    V("Be quiet.", "Jim bo'ling.", "quiet"), V("Listen.", "Tinglang.", "eyes"),
    V("Don't run.", "Yugurmang.", "run"), V("Don't shout.", "Baqirmang.", "shout"),
]

INFO = UnitInfo(
    number=8, title="Where is it? Do! Don't!", topic="Prepositions of place and classroom commands",
    book="Round-Up 3, Unit 13 (prepositions of place) and Unit 14 (imperative)",
    vocabulary="in, on, under, next to, behind, in front of, between (+ commands: sit down, stand up, open your book, "
               "be quiet, listen, don't run, don't shout)",
    grammar=["Where is the ball? It's in / on / under / next to / behind / in front of / between …",
             "Imperatives: Sit down. · Open your book. · Don't run. · Let's play."],
)

CARD = [
    Heading("Where is it? — Do! Don't!", 1),
    Table([["[[prep-in|54]]\n**in**", "[[prep-on|54]]\n**on**", "[[prep-under|54]]\n**under**", "[[prep-next to|54]]\n**next to**"],
           ["[[prep-behind|54]]\n**behind**", "[[prep-in front of|54]]\n**in front of**", "[[prep-between|54]]\n**between**",
            "The ball is **in** the box."]],
          widths=[1] * 4, style="grid", size=11, align="center"),
    Box([Para("**Do:** Sit down. · Open your book. · Listen, please. · Let's play!"),
         Para("**Don't:** Don't run. · Don't shout. · Don't open the window.")],
        kind="grammar", title="Imperatives (commands)"),
    Box([Para("Buyruq shaklida 'you' aytilmaydi: 'Sit down!' (siz o'tiring). Inkor: **Don't** + fe'l. "
              "'in / on / under' ni rasm bilan yodlang: o'zbekchadagi '-da, -ning ustida, tagida' ga mos keladi.")],
        kind="tip", title="Eslatma"),
]

LESSONS = [
    Lesson.std(
        title="Where is the ball?",
        focus="Prepositions of place: in, on, under, next to, behind, in front of, between",
        aims=["say where something is", "ask and answer: Where is the ball? It's under the table."],
        language=["in · on · under · next to · behind · in front of · between", "Where is …? It's …"],
        materials=["A ball and a box (real objects)", "Flashcards of the seven pictures", "Grammar card"],
        greeting="Hide a small toy in the classroom and ask 'Where is it?' Let pupils guess with Uzbek, then model 'It's under the book.'",
        warmup="**Hot and cold**: one pupil leaves; the class hides an object; on return the pupil asks 'Is it in the bag?'",
        present="Use the ball and the box to show all seven prepositions, then show the flashcards. Drill with gestures "
                "(hands in / on / under).",
        practice="Worksheet A exercises A (label the pictures), B (circle) and D (complete). Pairs place objects and describe.",
        produce="**Barrier game**: pairs sit back to back; A places a ball on a picture of a room and describes it; B draws.",
        wrap="Teacher places the ball; pupils chorus 'It's in front of the box!' Homework.",
        homework="Draw your room and write five sentences: 'My bag is next to the chair.'",
        assessment="Listen for correct prepositions in the barrier game.",
        tips=["'in / on / under' o'zbekchada -da, -ning ustida, -ning tagida; rasm + harakat bilan o'rgating.",
              "'in front of' — uch so'zli ibora: bir birlik sifatida o'rgating.",
              "Support: use real objects. Extension: add 'opposite' and 'near'."],
    ),
    Lesson.std(
        title="Do! Don't!",
        focus="Imperatives: Sit down. Don't run.",
        aims=["understand and give classroom commands", "say what we do and don't do in class"],
        language=["Sit down. · Stand up. · Open your book. · Be quiet. · Don't run. · Don't shout."],
        materials=["Command flashcards", "Worksheet B exercises A–E"],
        greeting="Give commands in English with gestures: 'Stand up. Sit down.'",
        warmup="**Simon says**: pupils follow only the commands with 'Simon says'.",
        present="Show the command cards and act each one. Write the pattern: verb (Do) / Don't + verb. Stress: no 'you', "
                "no -s.",
        practice="Worksheet B exercises A (circle), B (fill), C (unscramble) and D (class rules text).",
        produce="**Class rules poster**: groups write four rules with Do and Don't and draw icons for each.",
        wrap="Groups present their poster; class acts out the rules. Homework.",
        homework="Write four home rules: 'Don't …', 'Wash your hands.'",
        assessment="Check verb base forms (Sit, not Sits) and Don't + verb.",
        tips=["Buyruq = fe'lning asl shakli: 'Sit down' (Sits emas). O'zbekchada ham buyruq oddiy: 'O'tir!'.",
              "Muloyimlik: 'Sit down, please.' — 'please' ni doim ayting.",
              "Support: picture cards with commands. Extension: add 'Let's …'."],
    ),
    Lesson.std(
        title="Treasure hunt",
        focus="Prepositions and imperatives together",
        aims=["give and follow instructions to find something", "use prepositions and imperatives in one text"],
        language=["Look under the chair. · Go to the window. · It's behind the door."],
        materials=["A hidden 'treasure' (toy or sweet)", "Clue cards", "Worksheet A exercise E; Worksheet B exercise E"],
        greeting="Show the treasure box: 'Where is the treasure? Let's find it!'",
        warmup="**Give a command**: pupils give the class one-word commands in turn (stand, jump, sit).",
        present="Read the first clue aloud: 'Look under the big book.' Model following it and reading the next clue.",
        practice="Groups follow four clue cards with imperatives and prepositions; each clue leads to the next.",
        produce="**Write your own clues**: pairs write three clues for another pair using 'Look …' and prepositions.",
        wrap="The group that finds the treasure reads the last clue aloud. Homework.",
        homework="Write two treasure-hunt clues for your family.",
        assessment="Check that clues use correct prepositions and imperatives.",
        tips=["Xavfsizlik: yugurmang, sekin yuring — 'Don't run!' qoidasini amalda qo'llang.",
              "Support: give a clue frame. Extension: pupils draw a map."],
        interactions=("T-Ss", "T-Ss", "T-Ss", "G", "Ss-Ss", "T-Ss"),
    ),
]

A = [
    PicLabel("Look and write the word.", items=[
        ("prep-in", "in"), ("prep-on", "on"), ("prep-under", "under"), ("prep-next to", "next to"),
        ("prep-behind", "behind"), ("prep-in front of", "in front of"), ("prep-between", "between")], cols=4, size=52),
    Circle("Look and circle the correct word.", items=[
        "[[prep-in|50]] The ball is {*in|on|under} the box.", "[[prep-on|50]] The ball is {in|*on|under} the box.",
        "[[prep-under|50]] The ball is {in|on|*under} the table.", "[[prep-next to|50]] The ball is {*next to|behind|on} the box.",
        "[[prep-behind|50]] The ball is {in front of|*behind|under} the box.",
        "[[prep-between|50]] The ball is {*between|on|in} the boxes."]),
    Gaps("Look and complete the words.", items=[
        ("prep-under", "under"), ("prep-behind", "behind"), ("prep-between", "between")], cols=3, size=46),
    Fill("Complete the sentences.", items=[
        "The cat is {under} the table.", "The book is {on} the desk.", "The bag is {next to} the chair.",
        "The boy is {behind} the door."], bank=True, extra_words=["in"]),
    WordSearch("Find words.", words=["under", "behind", "between", "table", "ball"], size=9, seed=28),
    Draw("Draw a ball in a box, on a box and under a table. Write the words.", prompts=["My pictures"]),
]

B = [
    Circle("Circle the correct word.", items=[
        "{*Sit|Sits} down, please.", "{*Don't|Doesn't} run in the classroom.", "{*Open|Opens} your book.",
        "Let's {*play|plays} a game.", "{*Be|Is} quiet, please.", "{*Don't|Not} shout."]),
    Fill("Complete the rules.", items=[
        "{Listen} to the teacher.", "{Don't} run in the corridor.", "{Sit} down when the teacher comes in.",
        "{Open} your book."], bank=True, extra_words=["Stand"]),
    Unscramble("Put the words in the right order.", items=[
        "Sit down, please.", "Don't shout.", "Open your book.", "Look under the chair."]),
    Reading("Read and answer.", title="Our class rules", text=(
        "Sit down when the teacher comes in. Open your book. Listen carefully.\n\n"
        "Don't shout. Don't run in the classroom. Be kind to your friends."), questions=[
        ("What do we do when the teacher comes in?", "We sit down."), ("Can we shout in class?", "No, we can't."),
        ("How do we treat our friends?", "We are kind to them.")]),
    WriteAbout("Write four rules for your classroom or your home.", frames=[
        "Listen to ___ .", "Don't ___ .", "Be ___ .", "Open / Close ___ ."], lines=4,
        model=["Listen to the teacher. Don't shout. Be kind. Open your book."]),
]

QUIZ = [
    Section("Part 1 · Where is it?", [
        PicLabel("Look and write the word.", items=[
            ("prep-in", "in"), ("prep-on", "on"), ("prep-under", "under"), ("prep-next to", "next to"),
            ("prep-behind", "behind"), ("prep-between", "between")], bank=False, cols=3, size=46)]),
    Section("Part 2 · Grammar", [
        Circle("Circle the correct word.", items=[
            "{*Sit|Sits} down.", "{*Don't|Doesn't} run.", "The cat is {*under|in} the table.",
            "Let's {*go|goes} to the park."]),
        Fill("Complete the sentences.", items=[
            "The ball is {in} the box.", "{Open} your book, please.", "The bag is {behind} the door.",
            "{Don't} shout."], extra_words=["on"])]),
    Section("Part 3 · Reading and writing", [
        Reading("Read and answer.", title="Class rules", text=(
            "In our class we listen to the teacher. We don't shout. We sit on our chairs. "
            "We put our bags under the desks."), questions=[
            ("Do they shout?", "No, they don't."), ("Where do they sit?", "On their chairs."),
            ("Where do they put their bags?", "Under the desks.")]),
        Unscramble("Put the words in the right order.", items=[
            "Don't run.", "The book is on the desk.", "Open your bag."])]),
]

SPEC = UnitSpec(number=8, slug="unit-8-prepositions-imperatives", title="Where is it? Do! Don't!", info=INFO,
                vocab=VOCAB, extra_vocab=EXTRA, lessons=LESSONS, worksheet_a=A, worksheet_b=B, quiz=QUIZ,
                badge=BADGE, sheet_a_name="Prepositions of place", sheet_b_name="Imperatives, class rules, writing",
                card=CARD,
                intro_note="Adapted for Grade 3 (age 8–9, CEFR A1): the ideas come from the Round-Up 3 unit; all "
                           "exercises and texts are new.")
