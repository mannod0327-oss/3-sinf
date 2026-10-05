"""Icon registry.

Every picture used in the worksheets is an emoji drawn from the Twemoji set
(graphics CC-BY 4.0, (c) Twitter Inc. and other contributors / jdecked).
Content files refer to icons by a short English name; this module maps the name
to a Twemoji code point and to a pre-rendered PNG in ``tools/assets/emoji``.

``EMOJI`` holds the code point; ``CHAR`` is derived from it so that the
Markdown output can show the native emoji on GitHub.
"""
from __future__ import annotations

from pathlib import Path

ASSET_DIR = Path(__file__).resolve().parent.parent / "assets" / "emoji"

# name -> Twemoji file stem (hex code points joined by "-", fe0f dropped)
EMOJI: dict[str, str] = {
    # --- people & family -------------------------------------------------
    "boy": "1f466", "girl": "1f467", "man": "1f468", "woman": "1f469",
    "baby": "1f476", "grandpa": "1f474", "grandma": "1f475", "family": "1f46a",
    "child": "1f9d2", "friends": "1f46b", "teacher": "1f9d1-200d-1f3eb",
    "student": "1f9d1-200d-1f393",
    # --- animals & insects -----------------------------------------------
    "cat": "1f431", "dog": "1f436", "bird": "1f426", "fish": "1f41f",
    "horse": "1f434", "cow": "1f42e", "sheep": "1f411", "chicken": "1f414",
    "duck": "1f986", "elephant": "1f418", "monkey": "1f412", "lion": "1f981",
    "bear": "1f43b", "frog": "1f438", "mouse": "1f42d", "pig": "1f437",
    "parrot": "1f99c", "giraffe": "1f992", "crocodile": "1f40a",
    "tiger": "1f42f", "rabbit": "1f430", "tortoise": "1f422", "snail": "1f40c",
    "snake": "1f40d", "butterfly": "1f98b", "caterpillar": "1f41b",
    "bee": "1f41d", "ant": "1f41c", "ladybird": "1f41e", "shark": "1f988",
    "dolphin": "1f42c", "whale": "1f433", "octopus": "1f419", "crab": "1f980",
    "goat": "1f410", "panther": "1f406", "chipmunk": "1f43f", "camel": "1f42b",
    "chimpanzee": "1f412",
    # --- nature & weather ------------------------------------------------
    "tree": "1f333", "palm": "1f334", "leaf": "1f343", "flower": "1f338",
    "sunflower": "1f33b", "grass": "1f33f", "seedling": "1f331",
    "mountain": "26f0", "sun": "2600", "cloud": "2601", "rain": "1f327",
    "snow": "2744", "wind": "1f4a8", "moon": "1f319", "star": "2b50",
    "rainbow": "1f308", "sea": "1f30a", "beach": "1f3d6", "sand": "1f3d6",
    "globe": "1f30d", "fire": "1f525", "umbrella": "2602",
    # --- school ------------------------------------------------------------
    "reception": "1f6ce", "dining hall": "1f37d", "library": "1f4da",
    "classroom": "1f3eb", "science room": "1f52c", "gym": "1f3cb",
    "art room": "1f3a8", "music room": "1f3b5", "playground": "1f6dd",
    "sports field": "1f3df", "pencil": "270f", "pen": "1f58a", "book": "1f4d5",
    "notebook": "1f4d3", "bag": "1f392", "ruler": "1f4cf", "scissors": "2702",
    "calendar": "1f4c5", "clock": "1f550", "computer": "1f4bb",
    "homework": "1f4dd", "board": "1f4cb", "bell": "1f514",
    # --- daily routine -----------------------------------------------------
    "get up": "23f0", "get dressed": "1f455", "breakfast": "1f373",
    "teeth": "1faa5", "go to school": "1f392", "lunch": "1f372",
    "go home": "1f3e0", "dinner": "1f357", "shower": "1f6bf", "bed": "1f6cf",
    "sleep": "1f634",
    # --- home activities ---------------------------------------------------
    "juice": "1f9c3", "sandwich": "1f96a", "dishes": "1f9fd",
    "play computer": "1f579", "read": "1f4d6", "tv": "1f4fa",
    "music": "1f3a7", "cake": "1f382", "car": "1f697", "soap": "1f9fc",
    # --- hobbies & sports --------------------------------------------------
    "piano": "1f3b9", "guitar": "1f3b8", "recorder": "1fa88", "models": "1f9f1",
    "films": "1f3ac", "karate": "1f94b", "gymnastics": "1f938",
    "table tennis": "1f3d3", "badminton": "1f3f8", "volleyball": "1f3d0",
    "football": "26bd", "basketball": "1f3c0", "swimming": "1f3ca",
    "tennis": "1f3be", "cycling": "1f6b4", "chess": "265f", "drum": "1f941",
    "violin": "1f3bb", "sing": "1f3a4", "dance": "1f483", "paint": "1f3a8",
    # --- food & drink ------------------------------------------------------
    "lemon": "1f34b", "watermelon": "1f349", "coconut": "1f965",
    "grapes": "1f347", "mango": "1f96d", "pineapple": "1f34d", "pear": "1f350",
    "tomato": "1f345", "onion": "1f9c5", "apple": "1f34e", "banana": "1f34c",
    "orange": "1f34a", "strawberry": "1f353", "peach": "1f351",
    "cherries": "1f352", "melon": "1f348", "carrot": "1f955",
    "potato": "1f954", "cucumber": "1f952", "corn": "1f33d", "bread": "1f35e",
    "cheese": "1f9c0", "egg": "1f95a", "milk": "1f95b", "rice": "1f35a",
    "noodles": "1f35c", "pizza": "1f355", "burger": "1f354", "chips": "1f35f",
    "hot dog": "1f32d", "ice cream": "1f368", "cake slice": "1f370",
    "cookie": "1f36a", "chocolate": "1f36b", "tea": "1f375", "water": "1f4a7",
    "meat": "1f356", "salad": "1f957", "smoothie": "1f964", "honey": "1f36f",
    "plate": "1f37d",
    # --- beach & clothes ---------------------------------------------------
    "sunglasses": "1f576", "swimsuit": "1fa71", "shorts": "1fa73",
    "shell": "1f41a", "boat": "26f5", "tshirt": "1f455", "jeans": "1f456",
    "dress": "1f457", "cap": "1f9e2", "shoe": "1f45f", "socks": "1f9e6",
    "coat": "1f9e5", "scarf": "1f9e3", "gloves": "1f9e4", "hat": "1f452",
    # --- transport ---------------------------------------------------------
    "bus": "1f68c", "bike": "1f6b2", "train": "1f686", "plane": "2708",
    # --- house -------------------------------------------------------------
    "house": "1f3e0", "sofa": "1f6cb", "chair": "1fa91", "door": "1f6aa",
    "window": "1fa9f", "bath": "1f6c1", "lamp": "1f4a1", "key": "1f511",
    "toy": "1f9f8", "ball": "26bd", "gift": "1f381", "balloon": "1f388",
    # --- body & feelings ---------------------------------------------------
    "eye": "1f441", "nose": "1f443", "mouth": "1f444", "ear": "1f442",
    "hand": "270b", "foot": "1f9b6", "tooth": "1f9b7", "happy": "1f60a",
    "sad": "1f622", "angry": "1f620", "tired": "1f634", "hungry": "1f924",
    "hot": "1f975", "cold": "1f976",
    # --- symbols -----------------------------------------------------------
    "tick": "2705", "cross": "274c", "question": "2753", "heart": "2764",
    "sparkles": "2728", "trophy": "1f3c6", "medal": "1f3c5", "pin": "1f4cc",
    "speech": "1f4ac", "ear-listen": "1f442", "pencil-write": "270f",
    "magnifier": "1f50d", "party": "1f389", "thumbs up": "1f44d",
    # --- school subjects, weekdays, misc -----------------------------------
    "maths": "1f522", "abc": "1f524", "run": "1f3c3", "lightning": "26a1",
    "planet": "1fa90", "recycle": "267b", "paper": "1f4c4", "bottle": "1f9f4",
    "jar": "1fad9", "can": "1f96b", "globe2": "1f310", "desert": "1f3dc",
    "mountain2": "1f3d4", "city": "1f3d9", "village": "1f3d8", "tent": "26fa",
    "pot": "1f372", "watch": "231a", "drumstick": "1f941", "music note": "1f3b6",
    "wave": "1f44b", "hands": "1f64c", "clap": "1f44f", "muscle": "1f4aa",
    "idea": "1f4a1", "brain": "1f9e0", "eyes": "1f440", "speaker": "1f50a",
    "books": "1f4da", "backpack": "1f392", "taxi": "1f695", "walk": "1f6b6",
    "camera": "1f4f7", "phone": "1f4f1", "kite": "1fa81", "sandcastle": "1f3d6",
    "ship": "1f6a2", "fishing": "1f3a3", "anchor": "2693",
    # --- jobs, shops, weather, directions ------------------------------------
    "box": "1f4e6", "doctor": "1f9d1-200d-2695-fe0f", "cook": "1f9d1-200d-1f373",
    "farmer": "1f9d1-200d-1f33e", "pilot": "1f9d1-200d-2708-fe0f", "singer": "1f9d1-200d-1f3a4",
    "artist": "1f9d1-200d-1f3a8", "firefighter": "1f9d1-200d-1f692", "police": "1f46e",
    "mechanic": "1f9d1-200d-1f527", "scientist": "1f9d1-200d-1f52c", "astronaut": "1f9d1-200d-1f680",
    "money": "1f4b5", "shop": "1f3ea", "basket": "1f9fa", "cart": "1f6d2", "coin": "1fa99",
    "thermometer": "1f321", "snowman": "2603", "fog": "1f32b", "thunder": "26c8",
    "arrow up": "2b06", "arrow left": "2b05", "arrow right": "27a1", "stop": "1f6d1", "map": "1f5fa",
    "gem": "1f48e", "crown": "1f451", "flag": "1f3c1", "bathroom": "1f6bf", "kitchen": "1f373",
    "bedroom": "1f6cf", "living room": "1f6cb", "garden": "1f337", "hall": "1f6aa", "sit": "1f9d8",
    "stand": "1f9cd", "write": "270d", "open": "1f4d6", "quiet": "1f92b", "shout": "1f4e2",
    "hug": "1f917", "wash hands": "1f9fc", "brush": "1faa5", "clap hands": "1f44f", "jump": "1f938",
    "climb": "1f9d7", "fly": "1f54a", "eat": "1f374", "drink": "1f964", "smile": "1f600",
    "spring": "1f331", "summer": "1f31e", "autumn": "1f342", "winter": "2744",
    "tall": "1f992", "short": "1f415", "long hair": "1f469", "glasses": "1f453", "beard": "1f9d4",
    "baby2": "1f476", "old man": "1f474", "old woman": "1f475", "young": "1f9d2",
}

# American English names for pictures that already exist under their British name, so a content
# file can use either spelling (the Guess What! pack follows the American edition).
EMOJI.update({
    "turtle": EMOJI["tortoise"], "ocean": EMOJI["sea"], "cafeteria": EMOJI["dining hall"],
    "science lab": EMOJI["science room"], "movies": EMOJI["films"], "ping-pong": EMOJI["table tennis"],
    "soccer": EMOJI["football"], "fries": EMOJI["chips"], "math": EMOJI["maths"],
})


def codepoint(name: str) -> str | None:
    """Return the Twemoji stem for ``name`` or ``None`` when we have no picture."""
    return EMOJI.get(name)


def char(name: str) -> str:
    """Return the native emoji character (used in Markdown output)."""
    if name.startswith("clock-") and len(name) == 10 and name[6:].isdigit():
        return "🕒"
    if name.startswith("prep-"):
        return "📦"
    stem = EMOJI.get(name)
    if not stem:
        return ""
    return "".join(chr(int(p, 16)) for p in stem.split("-"))


GENERATED_DIR = ASSET_DIR.parent / "generated"


def clock_png(hour: int, minute: int) -> Path:
    """Analogue clock face drawn on demand (``[[clock-0730]]`` in any text)."""
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    path = GENERATED_DIR / f"clock-{hour:02d}{minute:02d}.png"
    if path.exists():
        return path
    import math

    import cairosvg

    cx = cy = 100.0

    def hand(angle_deg: float, length: float, width: float, color: str) -> str:
        a = math.radians(angle_deg - 90)
        x, y = cx + length * math.cos(a), cy + length * math.sin(a)
        return (f'<line x1="{cx}" y1="{cy}" x2="{x:.1f}" y2="{y:.1f}" stroke="{color}" '
                f'stroke-width="{width}" stroke-linecap="round"/>')

    parts = ['<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" viewBox="0 0 200 200">',
             '<circle cx="100" cy="100" r="94" fill="#ffffff" stroke="#1B6CA8" stroke-width="8"/>']
    for n in range(1, 13):
        a = math.radians(n * 30 - 90)
        tx, ty = cx + 72 * math.cos(a), cy + 72 * math.sin(a) + 7
        parts.append(f'<text x="{tx:.1f}" y="{ty:.1f}" font-family="DejaVu Sans" font-weight="bold" '
                     f'font-size="20" text-anchor="middle" fill="#1F2933">{n}</text>')
    for n in range(60):
        a = math.radians(n * 6 - 90)
        r1, r2 = (86, 92) if n % 5 else (84, 92)
        parts.append(f'<line x1="{cx + r1 * math.cos(a):.1f}" y1="{cy + r1 * math.sin(a):.1f}" '
                     f'x2="{cx + r2 * math.cos(a):.1f}" y2="{cy + r2 * math.sin(a):.1f}" '
                     f'stroke="#9FB3C8" stroke-width="{2 if n % 5 else 3}"/>')
    parts.append(hand((hour % 12) * 30 + minute * 0.5, 44, 8, "#1F2933"))
    parts.append(hand(minute * 6, 66, 5, "#E8871E"))
    parts.append('<circle cx="100" cy="100" r="6" fill="#1F2933"/></svg>')
    cairosvg.svg2png(bytestring="".join(parts).encode(), write_to=str(path), output_width=256, output_height=256)
    return path


PREPOSITIONS = ("in", "on", "under", "next to", "behind", "in front of", "between")


def prep_png(kind: str) -> Path:
    """Box-and-ball pictures for prepositions of place (``[[prep-in]]``, ``[[prep-next to]]`` …)."""
    GENERATED_DIR.mkdir(parents=True, exist_ok=True)
    path = GENERATED_DIR / f"prep-{kind.replace(' ', '_')}.png"
    if path.exists():
        return path
    import cairosvg

    def box(x: float, y: float, w: float, h: float, fill: str = "#C98A4B") -> str:
        return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="{fill}" stroke="#7A4E21" '
                f'stroke-width="4"/>')

    def ball(cx: float, cy: float, r: float = 22) -> str:
        return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#E8871E" stroke="#9A4F00" stroke-width="4"/>'
                f'<circle cx="{cx - r * 0.3}" cy="{cy - r * 0.3}" r="{r * 0.22}" fill="#FFD9A0"/>')

    ground = '<rect x="0" y="178" width="200" height="6" fill="#9FB3C8"/>'
    shapes = {
        "in": box(55, 126, 90, 52, "#E2B27A") + ball(100, 120) + box(55, 140, 90, 38),
        "on": box(65, 118, 70, 60) + ball(100, 96),
        "under": ('<rect x="45" y="88" width="110" height="12" rx="3" fill="#C98A4B" stroke="#7A4E21" '
                  'stroke-width="4"/><rect x="52" y="100" width="10" height="78" fill="#C98A4B" stroke="#7A4E21" '
                  'stroke-width="3"/><rect x="138" y="100" width="10" height="78" fill="#C98A4B" stroke="#7A4E21" '
                  'stroke-width="3"/>' + ball(100, 152, 20)),
        "next to": box(28, 118, 70, 60) + ball(146, 154, 24),
        "behind": ball(112, 132, 26) + box(52, 118, 76, 60),
        "in front of": box(78, 110, 84, 68) + ball(88, 150, 26),
        "between": box(20, 118, 60, 60) + box(120, 118, 60, 60) + ball(100, 154, 20),
    }
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200" viewBox="0 0 200 200">'
           '<rect width="200" height="200" rx="14" fill="#F4F9FF"/>' + ground + shapes[kind] + "</svg>")
    cairosvg.svg2png(bytestring=svg.encode(), write_to=str(path), output_width=256, output_height=256)
    return path


def png(name: str) -> Path | None:
    """Return the path of the pre-rendered PNG for ``name`` (or ``None``)."""
    if name.startswith("prep-") and name[5:] in PREPOSITIONS:
        return prep_png(name[5:])
    if name.startswith("clock-") and len(name) == 10 and name[6:].isdigit():
        return clock_png(int(name[6:8]), int(name[8:10]))
    stem = EMOJI.get(name)
    if not stem:
        return None
    path = ASSET_DIR / f"{stem}.png"
    return path if path.exists() else None


def has(name: str) -> bool:
    return png(name) is not None
