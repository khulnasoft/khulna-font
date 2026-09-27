#!/usr/bin/env python3
"""HarfBuzz shaping fixtures for Khulna.

Shaping is where a script either works or silently does not. Codepoint
coverage in the cmap proves nothing: `ক্র` can be "covered" and still
render as three disconnected glyphs. These fixtures assert the actual
glyph sequence HarfBuzz produces.

Each fixture is (name, text, expectation). Expectations are one of:

  ("glyphs", [names])   exact glyph sequence
  ("count", n)          exactly n glyphs, names not pinned
  ("joins", True)       the run contains no .notdef and glyph count is
                        less than the codepoint count, i.e. substitution
                        or ligature formation actually happened

Run directly to print a report:

    python3 scripts/shaping-check.py
"""

import sys
from pathlib import Path

import uharfbuzz as hb

BASE = Path(__file__).resolve().parent.parent

# ── Fixtures ───────────────────────────────────────────────────────
# Latin: prove the existing OpenType work still holds after the refactor.
LATIN_FIXTURES = [
    ("liga fi",  "fi",      ("glyphs", ["fi"])),
    ("liga fl",  "fl",      ("glyphs", ["fl"])),
    ("liga ff",  "ff",      ("glyphs", ["fft"])),
]

# Bengali: the sequences that must work before Bengali ships.
# These are expected to FAIL until bengali.is_implemented() is True —
# that is the point. They are the definition of done.
BENGALI_FIXTURES = [
    ("isolated ka",   "ক",    ("count", 1)),
    ("matra i",       "কি",   ("joins", True)),
    ("matra ii",      "কী",   ("joins", True)),
    ("matra u",       "কু",   ("joins", True)),
    ("akhn kta",      "ক্ত",  ("joins", True)),
    ("akhn kta+ra",   "ক্ত্র", ("joins", True)),
    ("akhn kma",      "ক্ম",  ("joins", True)),
    ("akhn kla",      "ক্ল",  ("joins", True)),
    ("akhn ksha",     "ক্ষ",  ("joins", True)),
    ("akhn jnya",     "জ্ঞ",  ("joins", True)),
    ("akhn tra",      "ত্র",  ("joins", True)),
    ("akhn shra",     "শ্র",  ("joins", True)),
    ("akhn pra",      "প্র",  ("joins", True)),
    ("repha",         "র্��", ("joins", True)),
    ("deep conjunct", "ক্ষ্ম", ("joins", True)),
    ("mixed script",  "aকb",  ("count", 3)),
]


def shape(font_path, text):
    """Return (glyph names, glyph ids) HarfBuzz produces for `text`."""
    blob = hb.Blob.from_file_path(str(font_path))
    face = hb.Face(blob)
    font = hb.Font(face)
    buf = hb.Buffer()
    buf.add_str(text)
    buf.guess_segment_properties()
    hb.shape(font, buf, {})
    gids = [i.codepoint for i in buf.glyph_infos]
    names = [font.get_glyph_name(g) or f"gid{g}" for g in gids]
    return names, gids


def check(font_path, fixtures, label):
    print(f"\n=== {label} ({Path(font_path).name}) ===")
    passed = failed = 0
    for name, text, (kind, expect) in fixtures:
        try:
            names, gids = shape(font_path, text)
        except Exception as e:  # noqa: BLE001
            print(f"  ERROR {name}: {e}")
            failed += 1
            continue

        n_codepoints = len(text)

        if kind == "glyphs":
            ok = names == expect
        elif kind == "count":
            ok = len(gids) == expect
        elif kind == "joins":
            # substitution or ligature formation actually happened,
            # and nothing fell back to .notdef
            ok = len(gids) < n_codepoints and 0 not in gids
        else:
            ok = False

        if ok:
            passed += 1
            print(f"  PASS {name:16} {text!r:12} -> {names}")
        else:
            failed += 1
            print(f"  FAIL {name:16} {text!r:12} -> {names} (want {kind}={expect})")
    print(f"  {passed} passed, {failed} failed")
    return passed, failed


def main():
    sys.path.insert(0, str(BASE))
    from sources.design import bengali

    sans = BASE / "dist" / "KhulnaSans-Regular.ttf"
    if not sans.exists():
        sys.exit(f"missing {sans} — run scripts/generate-sources.py first")

    total_f = total_p = 0

    p, f = check(sans, LATIN_FIXTURES, "Latin / OpenType")
    total_p += p; total_f += f

    if bengali.is_implemented():
        p, f = check(sans, BENGALI_FIXTURES, "Bengali shaping")
        total_p += p; total_f += f
    else:
        print("\n=== Bengali shaping ===")
        print(f"  SKIPPED — bengali.is_implemented() is False.")
        print(f"  {len(BENGALI_FIXTURES)} fixtures are pending. See")
        print(f"  sources/design/BENGALI_SPEC.md §6 for acceptance criteria.")

    print(f"\nTotal: {total_p} passed, {total_f} failed")
    return 1 if total_f else 0


if __name__ == "__main__":
    sys.exit(main())
