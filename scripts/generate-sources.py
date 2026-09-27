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
    i.openTypeOS2Selection = []
    i.openTypeOS2Type = [0]
    i.openTypeOS2UnicodeRanges = [0, 1]
    i.openTypeOS2CodePageRanges = [0, 0]
    i.openTypeOS2TypoAscender = tokens.ASC
    i.openTypeOS2TypoDescender = tokens.DESC
    i.openTypeOS2TypoLineGap = 0
    i.openTypeOS2WinAscent = tokens.ASC + 100
    i.openTypeOS2WinDescent = abs(tokens.DESC) + 100
    i.postscriptFontName = f"{family}-{style}"
    i.postscriptFullName = f"{family} {style}"
    i.postscriptIsFixedPitch = is_mono
    i.postscriptUnderlinePosition = -50
    i.postscriptUnderlineThickness = 10

    f.kerning.groups = kerning[0]
    f.kerning.kerning = kerning[1]
    f.features.text = features_text

    # Guard against the rectangle-with-a-Bengali-codepoint failure mode.
    bengali.assert_not_shipped(glyph_names)

    f.glyphOrder = glyph_names
    for name in glyph_names:
        if name not in builder:
            continue
        g = f.newGlyph(name)
        g.width = tokens.WX_MONO if is_mono else tokens.WX_DEF
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
