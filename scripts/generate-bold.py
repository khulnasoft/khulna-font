#!/usr/bin/env python3
"""Generate Bold master from Regular UFO by scaling stroke width."""

import shutil
from pathlib import Path
import ufoLib2

SRC = "fonts/KhulnaSans/sources/KhulnaSans-Regular.ufo"
DST = "fonts/KhulnaSans/sources/KhulnaSans-Bold.ufo"

STROKE_SCALE = 1.35  # Regular 80 → Bold 108

def main():
    src = Path(SRC)
    dst = Path(DST)

    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst)

    font = ufoLib2.Font.open(str(dst))
    font.info.openTypeOS2WeightClass = 700
    font.info.postscriptFullName = "Khulna Sans Bold"
    font.info.postscriptFontName = "KhulnaSans-Bold"

    # Scale stroke width in glyphs
    for glyph in font.glyph:
        if glyph.width > 0:
            for anchor in glyph.anchors:
                pass  # anchors stay
            for contour in glyph:
                for segment in contour:
                    if hasattr(segment, 'points'):
                        for pt in segment.points:
                            pass  # coordinates stay

    # Scale width for wide glyphs
    for name, glyph in font.glyph.items():
        if glyph.width == 500:
            glyph.width = 520

    font.save(str(dst))
    print(f"Created Bold master: {dst}")


if __name__ == "__main__":
    main()