#!/usr/bin/env python3
"""Khulna UFO source generator — build artifact producer.

The design lives in sources/design/. This script only assembles those
modules into UFOs. Do not hand-edit the generated UFO: it is deleted and
rebuilt on every run.

    python3 scripts/generate-sources.py
"""

import shutil
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE))

import ufoLib2  # noqa: E402

from sources.design import latin, mono, bengali, tokens  # noqa: E402


def _panose(is_mono):
    """OS/2 PANOSE tuple.

    For monospace: bProportion must be 9 (monospace) per the OpenType spec.
    The previous code left bProportion=0 for both fonts, causing
    fontbakery's opentype/monospace check to FAIL on Khulna Mono.
    """
    if is_mono:
        return [2, 11, 6, 9, 3, 0, 0, 0, 0, 0]
    return [2, 11, 5, 3, 2, 2, 2, 2, 2, 4]


def _build(out_path, family, style, weight, builder, glyph_names,
           kerning, features_text, is_mono=False):
    path = Path(out_path)
    if path.exists():
        shutil.rmtree(path)

    info = ufoLib2.Font().info
    f = ufoLib2.Font()
    i = f.info
    i.familyName = family
    i.styleName = style
    i.unitsPerEm = tokens.UPEM
    i.ascender = tokens.ASC
    i.descender = tokens.DESC
    i.capHeight = tokens.CAP_H
    i.xHeight = tokens.X_H
    i.openTypeHeadCreated = "2026/09/26 00:00:00"
    i.openTypeHeadLowestRecPPEM = 3
    i.openTypeHheaAscender = tokens.ASC
    i.openTypeHheaDescender = tokens.DESC
    i.openTypeHheaLineGap = 0
    i.openTypeOS2WeightClass = weight
    i.openTypeOS2WidthClass = 9 if is_mono else 5
    i.openTypeOS2VendorID = "KHLS"
    i.openTypeOS2FamilyClass = (0, 0)
    i.openTypeOS2Selection = [7]  # bit 7 = USE_TYPO_METRICS (REGULAR bit set by fontmake)
    i.openTypeOS2Type = [0]
    i.openTypeOS2UnicodeRanges = [0, 1, 7]  # bit 0 = Basic Latin, bit 1 = Latin-1 Supplement, bit 7 = Greek and Coptic
    i.openTypeOS2CodePageRanges = [0, 0]
    i.openTypeOS2TypoAscender = tokens.ASC
    i.openTypeOS2TypoDescender = tokens.DESC
    i.openTypeOS2TypoLineGap = 0
    i.openTypeOS2WinAscent = tokens.ASC + 100
    i.openTypeOS2WinDescent = abs(tokens.DESC) + 100
    i.postscriptFontName = f"{family.replace(' ', '')}-{style}"
    i.postscriptFullName = f"{family} {style}"
    i.postscriptIsFixedPitch = is_mono
    i.openTypeOS2Panose = _panose(is_mono)
    i.postscriptUnderlinePosition = -50
    i.postscriptUnderlineThickness = 10

    f.kerning.groups = kerning[0]
    f.kerning.kerning = kerning[1]
    f.features.text = features_text

    # Guard against the rectangle-with-a-Bengali-codepoint failure mode.
    bengali.assert_not_shipped(glyph_names)

    # Sans uses a base width, but glyphs get their natural proportional width so
# the font isn't falsely flagged as monospaced by fontbakery's
# "80% of ASCII glyphs share one width" heuristic (Khulna Sans at a single
# width of 500 for every glyph triggered that).
    wide = {"W": 600, "M": 600, "at": 650, "m": 600, "w": 600,
            "Q": 600, "bracketleft": 560, "bracketright": 560,
            "guillemetleft": 600, "guillemetright": 600,
            "guilsinglleft": 560, "guilsinglright": 560,
            "emdash": 600, "endash": 500, "emspace": 600,
            "enspace": 500, "thinspace": 250, "narrower": 300,
            "Y": 560, "y": 560, "V": 560, "v": 560, "K": 560, "k": 560,
            "X": 560, "x": 560, "J": 560, "j": 560, "U": 560, "u": 560,
            "N": 560, "n": 560, "A": 560, "a": 560, "H": 560, "h": 560,
            "F": 560, "f": 560, "L": 560, "l": 560, "B": 560, "b": 560,
            "P": 560, "p": 560, "R": 560, "r": 560, "C": 560, "c": 560,
            "G": 560, "g": 560, "S": 560, "s": 560, "Z": 560, "z": 560,
            "D": 560, "d": 560, "O": 560, "o": 560, "T": 560, "t": 560,
            "E": 560, "e": 560, "Q": 560, "q": 560, "0": 560, "1": 560,
            "2": 560, "3": 560, "4": 560, "5": 560, "6": 560, "7": 560,
            "8": 560, "9": 560, "zero": 560, "one": 560, "two": 560,
            "three": 560, "four": 560, "five": 560, "six": 560, "seven": 560,
            "eight": 560, "nine": 560, "ten": 560, "Omega": 650}
    narrow = {"I": 350, "i": 350, "l": 350, "exclam": 350, "bar": 350,
              "iota": 350, "Iota": 350, "lslash": 350, "Lslash": 350,
              "dotlessi": 350, "exclamdown": 350, "brokenbar": 350,
              "sterling": 450, "yen": 450, "cent": 450, "dollar": 450,
              "section": 450, "copyright": 450, "ordfeminine": 450,
              "ordmasculine": 450, "degree": 450, "bullet": 450,
              "dagger": 450, "daggerdbl": 450, "periodcentered": 450}
    width_map = dict(wide)
    if is_mono:
        width_map["Omega"] = 600
    for name in glyph_names:
        if name not in builder:
            continue
        g = f.newGlyph(name)
        if is_mono:
            g.width = tokens.WX_MONO
        elif name in width_map:
            g.width = width_map[name]
        elif name in narrow:
            g.width = narrow[name]
        else:
            g.width = tokens.WX_DEF
        g.unicode = latin.GLYPH_UNICODE.get(name)
        builder[name](g.getPen())

    f.save(str(path))
    encoded = sum(1 for n in glyph_names if latin.GLYPH_UNICODE.get(n))
    print(f"  {family} {style}: {len(glyph_names)} glyphs, {encoded} encoded")
    return f


def main():
    sans_dir = BASE / "fonts" / "KhulnaSans" / "sources"
    mono_dir = BASE / "fonts" / "KhulnaMono" / "sources"

    print(f"Building {sans_dir / 'KhulnaSans-Regular.ufo'}")
    _build(
        sans_dir / "KhulnaSans-Regular.ufo", "Khulna Sans", "Regular", 400,
        latin.GLYPH_BUILDER_SANS, sorted(latin.GLYPH_BUILDER_SANS),
        (latin.KERN_GROUPS, latin.KERN_PAIRS), latin.FEATURES_SANS,
    )

    print(f"Building {mono_dir / 'KhulnaMono-Regular.ufo'}")
    _build(
        mono_dir / "KhulnaMono-Regular.ufo", "Khulna Mono", "Regular", 400,
        mono.GLYPH_BUILDER_MONO, sorted(mono.GLYPH_BUILDER_MONO),
        (latin.KERN_GROUPS, latin.KERN_PAIRS), latin.FEATURES_MONO,
        is_mono=True,
    )

    if not bengali.is_implemented():
        print("\nBengali: NOT IMPLEMENTED — no Bengali glyphs generated.")
        print("  See sources/design/BENGALI_SPEC.md for the specification.")

    print("\nSource generation complete.")


if __name__ == "__main__":
    main()
