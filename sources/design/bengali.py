"""Bengali script support for Khulna — DESIGN PHASE, NOT YET IMPLEMENTED.

STATUS: intentionally empty. Do not add glyphs here until the letterforms
exist. See sources/design/BENGALI_SPEC.md for the full specification.

Why this file is empty
---------------------
Bengali is an abugida. Every consonant is a skeleton that hangs from a
matra (headline) and combines with vowel signs, with half-forms, and with
each other to form conjuncts. It cannot be approximated with the Latin
primitive set in tokens.py (rect/oval/h_bar) — a `rect` skeleton produces
something that occupies the right codepoint and renders as noise.

A previous iteration generated 47 Bengali glyphs as Latin-shaped
rectangles. They compiled, produced correct cmap entries, passed every
automated check, and were completely wrong on screen. That is the failure
mode this module exists to prevent.

Adding a glyph here requires, per sources/design/BENGALI_SPEC.md:
  1. A drawn skeleton with matra, not a primitive assembly
  2. Registration in BENGALI_INVENTORY below with its shaping roles
  3. The matching GSUB lookup (init/medi/fina/pres/abvs/blws/akhn)
  4. A HarfBuzz shaping fixture in tests/shaping/

Codepoint coverage without correct outlines and shaping is not Bengali
support. Shipping it as such is worse than shipping nothing.
"""

# ── Inventory (specification only — no outlines) ───────────────────
#
# Roles:
#   base       consonant, has isolated + initial + medial + final forms
#   independent vowel, has its own inherent shape
#   matra      dependent vowel sign, attaches left/right/below/above
#   mark       anusvara / visarga / candrabindu
#   nukta      modifies preceding base into a new consonant
#
# Unicode ranges: U+0980–U+09FF (Bengali), U+1CD0–u1CFF (Vedic extensions,
# out of scope for v1).

BENGALI_INVENTORY = {
    # Independent vowels
    "independent_vowels": {
        "a": 0x0985, "aa": 0x0986, "i": 0x0987, "ii": 0x0988,
        "u": 0x0989, "uu": 0x098A, " vocalic_r": 0x098B, "e": 0x098F,
        "ai": 0x0990, "o": 0x0993, "au": 0x0994,
    },
    # Consonants, by phonetic class
    "velars": {
        "ka": 0x0995, "kha": 0x0996, "ga": 0x0997, "gha": 0x0998,
        "nga": 0x0999,
    },
    "palatals": {
        "ca": 0x099A, "cha": 0x099B, "ja": 0x099C, "jha": 0x099D,
        "nya": 0x099E,
    },
    "retroflexes": {
        "tta": 0x099F, "ttha": 0x09A0, "dda": 0x09A1, "ddha": 0x09A2,
        "nna": 0x09A3,
    },
    "dentals": {
        "ta": 0x09A4, "tha": 0x09A5, "da": 0x09A6, "dha": 0x09A7,
        "na": 0x09A8,
    },
    "labials": {
        "pa": 0x09AA, "pha": 0x09AB, "ba": 0x09AC, "bha": 0x09AD,
        "ma": 0x09AE,
    },
    "approximants": {
        "ya": 0x09AF, "ra": 0x09B0, "la": 0x09B2,
        "vocalic_l": 0x09B1, "zha": 0x09B4, "va": 0x09B5,
    },
    "sibilants_and_h": {
        "sha": 0x09B6, "ssha": 0x09B7, "sa": 0x09B8, "ha": 0x09B9,
    },
    # Additional consonants used in conjuncts
    "additional": {
        "rra": 0x09DC, "rha": 0x09DD, "yya": 0x09DF,
    },
    # Dependent vowel signs (matras) — must be marked in GDEF
    "matras": {
        "aa": 0x09BE, "i": 0x09BF, "ii": 0x09C0, "u": 0x09C1,
        "uu": 0x09C2, "vocalic_r": 0x09C3, "e": 0x09C7, "ai": 0x09C8,
        "o": 0x09CB, "au": 0x09CC,
    },
    # Signs and modifiers
    "signs": {
        "anusvara": 0x0982, "chandrabindu": 0x0981, "visarga": 0x0983,
        "khanda_ta": 0x0984,  # kills a preceding consonant
    },
    # Nukta forms
    "nukta_forms": {
        "rra": 0x09DC, "rha": 0x09DD, "yya": 0x09DF,
        "nna": 0x09A3, "rra_alt": 0x09DC,
    },
    # Punctuation and digits
    "punctuation": {
        "danda": 0x0964, "ddanda": 0x0965,
        "question": 0x0967,  # actually Bengali digits; see digits
    },
    "digits": {
        "0": 0x09E6, "1": 0x09E7, "2": 0x09E8, "3": 0x09E9,
        "4": 0x09EA, "5": 0x09EB, "6": 0x09EC, "7": 0x09ED,
        "8": 0x09EE, "9": 0x09EF,
    },
}

# The 11 canonical conjuncts required by the `akhn` feature, per the
# standard Bengali shaping model. These must exist as real glyphs with
# proper ligature substitutions.
AKHN_CONJUNCTS = [
    ("ka", "tta"),      # ক্ত
    ("ka", "tha"),      # ক্থ
    ("ka", "nna"),      # ক্ন
    ("ka", "ma"),       # ক্ম
    ("ka", "ra"),       # ক্র
    ("ka", "la"),       # ক্ল
    ("ka", "ssa"),      # ক্ষ
    ("ja", "nya"),      # জ্ঞ
    ("ta", "ra"),       # ত্র
    ("sha", "ra"),      # শ্র
    ("pa", "ra"),       # প্র
]

# Coeng (virama) — the joiner that triggers conjunct formation.
COENG = 0x09CD

# GSUB features required, in order. A Bengali font is not done until all
# of these compile and pass HarfBuzz fixtures.
REQUIRED_FEATURES = [
    "ccmp",   # decompose / canonical composition
    "locl",   # localise
    "akhn",   # the 11 akhand conjuncts
    "rphf",   # repha — ra above, with the hasant form
    "rkrf",   # ra-with-kera forms
    "blwf",   # below-base forms
    "half",   # half forms
    "pstf",   # post-base forms
    "vatu",   # vattu variants
    "pres",   # pre-base substitutions
    "abvs",   # above-base substitutions
    "blws",   # below-base substitutions
    "psts",   # post-base substitutions
    "haln",   # halant forms
    "calt",   # contextual alternates
    "init",   # initial forms
    "medi",   # medial forms
    "fina",   # final forms
    "abvm",   # above-base mark positioning
    "blwm",   # below-base mark positioning
]


def is_implemented() -> bool:
    """Bengali is not implemented until real outlines exist here."""
    return False


def assert_not_shipped(glyph_names):
    """Guard: fail loudly if placeholder Bengali reaches a built font.

    Called by the generator so that a rectangle-with-a-Bengali-codepoint
    can never again pass silently through QA.
    """
    bad = [g for g in glyph_names if g.startswith("bangla_")]
    if bad:
        raise AssertionError(
            f"Placeholder Bengali glyphs must not be built: {sorted(bad)}\n"
            "See sources/design/BENGALI_SPEC.md. Real outlines are required."
        )
