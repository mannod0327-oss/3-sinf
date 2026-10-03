"""Destination A1 · progress tests A (mini-units 1–5) and B (mini-units 6–9), 30 points each."""
from sinf.exercises import Circle, Fill, PicLabel, Reading, Section, Unscramble, WriteAbout

TESTS = [
    dict(
        slug="progress-test-A", title="Progress test A", scope="Mini-units 1–5: be / there is · jobs · my home · "
                                                              "present continuous · hobbies",
        sections=[
            Section("Part 1 · Choose", [
                Circle("Circle the correct word.", items=[
                    "I {*am|is|are} nine years old.", "{*Is|Are} there a lamp on the desk?",
                    "There {is|*are} three windows in the room.", "{*These|This} are my books.",
                    "My mum {*teaches|teach} English.", "Pilots {*fly|flies} planes.",
                    "He {*is|are|am} riding a bike.", "I like {*dancing|dance|dances}."])]),
            Section("Part 2 · Complete", [
                Fill("Complete the sentences.", items=[
                    "There {isn't} a computer on the desk.", "{Are} there two windows?",
                    "My dad is a farmer. He {grows} (grow) vegetables.", "{Does} the doctor work in a hospital?",
                    "I {am} washing my hands.", "They {are} riding bikes.", "She {isn't} eating. She is drinking juice.",
                    "I like {swimming} (swim)."], extra_words=["is", "do"])]),
            Section("Part 3 · Words", [
                PicLabel("Look and write the words.", items=[
                    ("doctor", "doctor"), ("kitchen", "kitchen"), ("bike", "ride a bike"), ("swimming", "go swimming")],
                    bank=False, cols=4, size=40)]),
            Section("Part 4 · Reading and sentences", [
                Reading("Read and answer.", title="Bobur in the park", text=(
                    "Bobur is in the park. He is flying a kite. His sister Zilola is riding a bike. There are two dogs "
                    "near the bench.\n\n"
                    "Bobur's mum is a doctor. She works in a hospital, but today she isn't working."), questions=[
                    ("What is Bobur doing?", "He is flying a kite."), ("How many dogs are there?", "Two."),
                    ("Is Bobur's mum working today?", "No, she isn't.")]),
                Unscramble("Put the words in the right order.", items=[
                    "There is a book on the desk.", "He is riding a bike.", "Does she like dancing?"])]),
            Section("Part 5 · Writing", [
                WriteAbout("Write 4 sentences about you.", frames=[
                    "I like ___ing.", "My mum / dad is a ___ . She / He ___s.", "In my room there is a ___ .",
                    "Now I am ___ing."], lines=4,
                    model=["I like dancing. My dad is a teacher. He teaches Maths. In my room there is a big lamp. "
                           "Now I am writing."], marks=4)]),
        ]),
    dict(
        slug="progress-test-B", title="Progress test B", scope="Mini-units 6–9: school life · food and shopping · "
                                                              "weather and seasons · clothes and appearance",
        sections=[
            Section("Part 1 · Choose", [
                Circle("Circle the correct word.", items=[
                    "We {*have|has} Maths on Monday.", "I like Art {*because|but} it's fun.",
                    "How {*much|many} is the milk?", "There aren't {some|*any} apples.",
                    "It's {*sunny|sun} today.", "What's the weather {*like|is}?", "She {*has|is} got long hair.",
                    "They {*are|is} wearing gloves."])]),
            Section("Part 2 · Complete", [
                Fill("Complete the sentences.", items=[
                    "{What's} your favourite subject?", "I like English {because} it is fun.",
                    "I'd like a bottle of {water}, please.", "{How much} is the bread?",
                    "In {summer} it's hot and sunny.", "I wear a {coat} in winter.", "He {has} got short hair.",
                    "She {is} wearing a red dress."], extra_words=["have", "autumn"])]),
            Section("Part 3 · Words", [
                PicLabel("Look and write the words.", items=[
                    ("bread", "bread"), ("maths", "Maths"), ("snowman", "snowy"), ("scarf", "scarf")],
                    bank=False, cols=4, size=40)]),
            Section("Part 4 · Reading and sentences", [
                Reading("Read and answer.", title="Aziza at the market", text=(
                    "It is Saturday and it is sunny. Aziza is at the market with her dad. She is wearing a yellow dress "
                    "and a white hat.\n\n"
                    "They want some tomatoes and a loaf of bread. 'How much is the bread?' asks Dad. 'It's 4,000 sum,' "
                    "says the shop assistant."), questions=[
                    ("What's the weather like?", "It's sunny."),
                    ("What is Aziza wearing?", "A yellow dress and a white hat."),
                    ("How much is the bread?", "4,000 sum.")]),
                Unscramble("Put the words in the right order.", items=[
                    "How much is the milk?", "I like winter because it's snowy.", "They are wearing hats."])]),
            Section("Part 5 · Writing", [
                WriteAbout("Write 4 sentences about you.", frames=[
                    "My favourite subject is ___ because ___ .", "I like ___ .", "In ___ it's ___ .",
                    "I'm wearing ___ ."], lines=4,
                    model=["My favourite subject is Art because it is fun. I like apples. In summer it's hot and sunny. "
                           "I'm wearing a blue T-shirt."], marks=4)]),
        ]),
]
