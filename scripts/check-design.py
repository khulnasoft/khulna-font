#!/usr/bin/env python3
"""Static integrity checks on the Khulna design source.

Catches the failure modes that are silent at runtime:

  1. Duplicate keys in a dict literal, OR duplicate function definitions.
     Python collapses both silently, so two entries for the same glyph name
     — or two defs of build_tilde — resolve to whichever came last, with no
     warning. This actually happened twice: a real circumflex registered
     alongside a placeholder reusing build_c, and build_tildebar defined
     twice.
  2. A codepoint mapped to more than one glyph name.
  3. A builder with no codepoint that is not an intentional ligature
     output (fi / fl / fft are produced by GSUB and must NOT be encoded).
  4. A codepoint in GLYPH_UNICODE with no corresponding builder.
  5. Any build_bangla_* builder, which must not exist until the Bengali
     letterforms are real.

    python3 scripts/check-design.py
"""

import ast
import collections
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE))

LATIN_PY = BASE / "sources" / "design" / "latin.py"

# Glyphs deliberately left unencoded because OpenType generates them.
LIGATURE_OUTPUTS = {"fi", "fl", "fft"}


def check_duplicate_dict_keys(path):
    """Find duplicate literal keys in any dict in the file."""
    tree = ast.parse(path.read_text())
    problems = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.Dict):
            continue
        keys = [k.value for k in node.keys
                if isinstance(k, ast.Constant) and isinstance(k.value, str)]
        counts = collections.Counter(keys)
        for key, n in counts.items():
            if n > 1:
                problems.append((key, n, node.lineno))
    return problems


def check_duplicate_functions(path):
    """Find functions defined more than once at module level.

    A second `def build_tilde` silently replaces the first, so the earlier
    definition is dead code and the later one always wins.
    """
    tree = ast.parse(path.read_text())
    seen = collections.defaultdict(list)
    for node in tree.body:
        if isinstance(node, ast.FunctionDef):
            seen[node.name].append(node.lineno)
    return [(name, lines) for name, lines in seen.items() if len(lines) > 1]


def main():
    from sources.design import latin, mono

    failures = []

    # 1. duplicate dict keys
    dups = check_duplicate_dict_keys(LATIN_PY)
    for key, n, lineno in dups:
        failures.append(
            f"duplicate key {key!r} x{n} in a dict literal at "
            f"{LATIN_PY.name}:{lineno} (silently collapsed by Python)"
        )

    # 1b. duplicate function definitions
    for name, lines in check_duplicate_functions(LATIN_PY):
        failures.append(
            f"function {name!r} defined {len(lines)}x at "
            f"{[f'{LATIN_PY.name}:{n}' for n in lines]} "
            f"(later definition silently wins)"
        )

    # 2. duplicate codepoints
    rev = collections.defaultdict(list)
    for name, cp in latin.GLYPH_UNICODE.items():
        rev[cp].append(name)
    for cp, names in rev.items():
        if len(names) > 1:
            failures.append(
                f"U+{cp:04X} mapped to multiple glyphs: {sorted(names)}"
            )

    # 3/4. builder <-> unicode agreement.
    # A glyph only needs a builder in ONE of the two registries: Mono adds
    # backtick / asciitilde / asciicircum, which Sans does not have.
    all_builders = set(latin.GLYPH_BUILDER_SANS) | set(mono.GLYPH_BUILDER_MONO)
    for name in all_builders:
        if name not in latin.GLYPH_UNICODE and name not in LIGATURE_OUTPUTS:
            failures.append(
                f"builder {name!r} has no codepoint and is not a known "
                f"ligature output"
            )
    for name in latin.GLYPH_UNICODE:
        if name not in all_builders:
            failures.append(
                f"GLYPH_UNICODE has {name!r} but no builder exists"
            )

    # 5. no placeholder Bengali
    bangla = [n for n in all_builders if n.startswith("bangla_")]
    if bangla:
        failures.append(
            f"placeholder Bengali builders present: {sorted(bangla)} — "
            f"see sources/design/BENGALI_SPEC.md"
        )

    if failures:
        print(f"FAIL — {len(failures)} design source problem(s):")
        for p in failures:
            print(f"  - {p}")
        return 1

    print("OK — design source integrity checks passed.")
    print(f"  {len(latin.GLYPH_BUILDER_SANS)} builders, "
          f"{len(latin.GLYPH_UNICODE)} codepoints, "
          f"{len(LIGATURE_OUTPUTS)} intentional ligature outputs")
    return 0


if __name__ == "__main__":
    sys.exit(main())
