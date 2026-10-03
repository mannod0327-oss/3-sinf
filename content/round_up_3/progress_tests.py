"""Round-Up 3 · progress tests A (mini-units 1–4) and B (mini-units 5–8), 30 points each."""
from sinf.exercises import Circle, Fill, PicLabel, Reading, Section, Unscramble, WriteAbout

TESTS = [
    dict(
        slug="progress-test-A", title="Progress test A", scope="Mini-units 1–4: plurals · be / have got / can · "
                                                              "possessives · articles",
        sections=[
            Section("Part 1 · Choose", [
                Circle("Circle the correct word.", items=[
                    "I've got two {*boxes|boxs}.", "There are three {*children|childs} in the garden.",
                    "She has {*an|a} orange.", "Aziz {*is|am|are} my friend.", "They {*have|has} got a dog.",
                    "A fish {*can|cans} swim.", "This is Anna. {*Her|His} bag is red.", "I like {a|the|*–} dogs."])]),
            Section("Part 2 · Complete", [
                Fill("Complete the sentences.", items=[
                    "I have two {feet}.", "We have {some} bread.", "They {are} at school.",
                    "That bag is Malika's. It's {hers}.", "Fish {can't} fly.", "I have {a} dog. {The} dog is brown.",
                    "She has {an} apple."], extra_words=["is", "any"])]),
            Section("Part 3 · Words", [
                PicLabel("Look and write the words.", items=[
                    ("pencil", "pencil"), ("scissors", "scissors"), ("swimming", "swim"), ("fly", "fly")],
                    bank=False, cols=4, size=36)]),
            Section("Part 4 · Reading and sentences", [
                Reading("Read and answer.", title="My friend", text=(
                    "This is my friend Jasur. He has got a bike and two birds. The birds can sing. "
                    "Jasur can't swim, but he can run fast. His bag is green. It is on the chair."), questions=[
                    ("What has Jasur got?", "A bike and two birds."), ("Can Jasur swim?", "No, he can't."),
                    ("Where is his bag?", "On the chair.")]),
                Unscramble("Put the words in the right order.", items=[
                    "She has got a cat.", "These are my pens.", "Can you swim?"])]),
            Section("Part 5 · Writing", [
                WriteAbout("Write 4 sentences about you.", frames=[
                    "I am ___ .", "I have got ___ .", "I can ___ .", "My ___ is ___ ."], lines=4,
                    model=["I am nine. I have got a cat and a bike. I can swim. My bag is blue."], marks=4)]),
        ]),
    dict(
        slug="progress-test-B", title="Progress test B", scope="Mini-units 5–8: quantity · present simple · "
                                                              "present continuous · prepositions and imperatives",
        sections=[
            Section("Part 1 · Choose", [
                Circle("Circle the correct word.", items=[
                    "There are {*some|any} eggs.", "Is there {some|*any} milk?", "How {*many|much} apples are there?",
                    "He {*plays|play} football every day.", "She {*doesn't|don't} watch TV.",
                    "They {*are|is} dancing.", "[[prep-under|40]] The cat is {*under|in|on} the table.",
                    "{*Don't|Doesn't} run in the classroom."])]),
            Section("Part 2 · Complete", [
                Fill("Complete the sentences.", items=[
                    "I haven't got {any} cheese.", "{How much} bread is there?", "Aziz {goes} (go) to school at eight.",
                    "{Does} she study English?", "I am {running} (run) now.", "{Are} they singing?",
                    "The book is {on} the desk.", "{Sit} down, please."], extra_words=["some", "Do"])]),
            Section("Part 3 · Words", [
                PicLabel("Look and write the words.", items=[
                    ("egg", "eggs"), ("pot", "cooking"), ("prep-behind", "behind"), ("prep-between", "between")],
                    bank=False, cols=4, size=40)]),
            Section("Part 4 · Reading and sentences", [
                Reading("Read and answer.", title="Dilnoza's Sunday", text=(
                    "Dilnoza usually gets up at eight on Sunday. Today she isn't sleeping — she is cooking plov with her "
                    "mum. There is a lot of rice, but there aren't any carrots.\n\n"
                    "Her brother is running in the garden. The dog is under the tree."), questions=[
                    ("What is Dilnoza doing now?", "She is cooking plov."),
                    ("Are there any carrots?", "No, there aren't."), ("Where is the dog?", "Under the tree.")]),
                Unscramble("Put the words in the right order.", items=[
                    "Is there any milk?", "He doesn't play football.", "Sit down, please."])]),
            Section("Part 5 · Writing", [
                WriteAbout("Write 4 sentences: what you do every day and what you are doing now.", frames=[
                    "Every day I ___ .", "I usually ___ .", "Now I am ___ing.", "I'm not ___ing."], lines=4,
                    model=["Every day I walk to school. I usually eat breakfast at seven. Now I am writing. "
                           "I'm not sleeping."], marks=4)]),
        ]),
]
