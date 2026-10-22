# Bengali Design Specification — Khulna

Status: **design phase, not implemented.** No Bengali glyphs are generated.
The inventory and shaping requirements below are machine-readable in
`sources/design/bengali.py`, which is the normative reference.

---

## 0. Why this document exists

An earlier iteration added 47 Bengali glyphs built from the same `rect`
primitives as the Latin set. They compiled, produced correct cmap entries,
and passed every automated check in the repo. They were wrong on screen.

This document exists so that "coverage" and "support" stop being confused.
A codepoint in the cmap is coverage. Support is coverage **plus** correct
outlines **plus** a shaping system that makes the sequences a reader
actually types come out right.

---

## 1. Design language: Bengali must be Khulna

The Bengali must not be a Bengali font with Khulna's name on it. It is one
system expressed in two scripts, so the Latin system is the constraint.

| Property    | Latin system says               | Bengali must therefore                                     |
| ----------- | ------------------------------- | ---------------------------------------------------------- |
| Stroke      | uniform, 80/1000                | matra 76/1000, body strokes 80/1000                        |
| Contrast    | none (monoline)                 | none — do not introduce modulated strokes                  |
| Terminals   | flat, horizontal cut            | flat, horizontal; matra terminals align to the column      |
| Proportions | wide, geometric, circular bowls | match the same geometric rhythm, not text-book proportions |
| Personality | plain, engineered, unhurried    | plain, engineered, unhurried                               |

### 1.1 Vertical metrics

Bengali has no cap height. The relevant anchors are the matra and the
baseline. These live in `tokens.py` and must not be duplicated:

```
BNG_MATRA_Y    = 620   top of the headline
BNG_MATRA_THICK = 76    headline weight (slightly < Latin 80)
BNG_BODY_TOP   = 560   consonant body meets the matra
BNG_BODY_BOT   =  60   consonant body baseline
BNG_DESC       = -220  descender depth
BNG_WX         = 560   default advance
```

The matra is the defining structural feature of the script: it is a
continuous horizontal rule that consonants hang from. Losing it destroys
the script. Every base consonant must connect to it.

---

## 2. Glyph inventory

Full machine-readable inventory: `bengali.BENGALI_INVENTORY`.

| Group                    | Count | Range         | Notes                                     |
| ------------------------ | ----- | ------------- | ----------------------------------------- |
| Independent vowels       | 11    | U+0985–U+0994 | inherent shapes, no matra variants needed |
| Velars ক খ গ ঘ ঙ         | 5     | U+0995–U+0999 | bowl + stem                               |
| Palatals চ ছ জ ঝ ঞ       | 5     | U+099A–U+099E | bowl + descending stem                    |
| Retroflexes ট ঠ ড ঢ ণ    | 5     | U+099F–U+09A3 | wedge/hook, no bowl                       |
| Dentals ত থ দ ধ ন        | 5     | U+09A4–U+09A8 | bowl + stem, thinner than velars          |
| Labials প ফ ব ভ ম        | 5     | U+09AA–U+09AE |                                           |
| Approximants য র ল ৱ ঴ ব | 6     | U+09AF–U+09B5 | য/র/ল take half forms                     |
| Sibilants শ ষ স হ        | 4     | U+09B6–U+09B9 |                                           |
| Additional ড় ঢ় য়      | 3     | U+09DC–U+09DF | via nukta                                 |
| Matras                   | 10    | U+09BE–U+09CC | **must be GDEF mark class**               |
| Marks                    | 4     | U+0981–U+0984 | anusvara, candrabindu, visarga, khanda ta |
| Digits                   | 10    | U+09E6–U+09EF |                                           |
| Punctuation              | 2+    | U+0964–U+0965 | danda, double danda                       |

Out of scope for v1: Vedic extensions (U+1CD0–U+1CFF), Bengali-specific
`৺` (U+09FA), and the rare `ঃ`-final forms.

### 2.1 Nukta forms

`ড় ঢ় য়` are canonically `ড় = ড + ়`. Implement via `ccmp` decomposition
plus explicit precomposed glyphs; do not rely on the shaper to compose a
nukta that has no base in the font.

---

## 3. Conjunct architecture

### 3.1 The eleven akhand conjuncts

Required by `akhn` (`bengali.AKHN_CONJUNCTS`):

```
ক্ত ক্থ ক্ন ক্ম ক্র ক্ল ক্ষ জ্ঞ ত্র শ্র প্র
```

These must exist as real glyphs with ligature substitutions, not as
runtime-merged half forms.

### 3.2 Positional forms

Every base consonant that can join needs up to four drawn forms:

| Form     | Tag            | When                                     |
| -------- | -------------- | ---------------------------------------- |
| Isolated | (default cmap) | word-initial, or after a non-joiner      |
| Initial  | `init`         | at word start, joiner to the right       |
| Medial   | `medi`         | between two joiners                      |
| Final    | `fina`         | joiner to the left, nothing to the right |

Plus `pres` / `abvs` / `psts` / `blws` for matras that sit before, above,
after, or below the base.

### 3.3 Repha

`র` (ra) forms a repha above the cluster when it carries a hasant and is
not word-final. Requires `rphf` and the `hasant` (0x09CD) form.

### 3.4 Conjunct depth

Real Bengali text nests conjuncts (`ক্ষ্ম`, `জ্জ্ঝ`, `ত্ত্র`). Half forms
(`half`) plus `vatu` are what make depth tractable. A font that only
handles the 11 akhand conjuncts will break on ordinary words.

---

## 4. Required OpenType features

`bengali.REQUIRED_FEATURES` is the normative list. All must compile:

```
ccmp locl akhn rphf rkrf blwf half pstf vatu pres abvs blws psts haln
calt init medi fina abvm blwm
```

A Bengali font is not done when the base glyphs exist. It is done when
these lookups compile, HarfBuzz produces correct output for the fixture
corpus, and FontBakery's Bengali checks pass.

---

## 5. GPOS requirements

- Matra marks carry the `mark` class in GDEF with correct
  `markAttachment` anchors, not `base`/`ligature`.
- `abvm` / `blwm` must attach marks with per-class anchor pairs, and
  must not collide with the matra.
- Advance widths must derive from `BNG_WX` and stay on the family's
  vertical rhythm; Bengali must not sit lower or higher than Latin in
  mixed-script lines. Mixed Latin/Bengali baseline and line-box behaviour
  is an explicit acceptance criterion.

---

## 6. Acceptance criteria

Bengali support ships only when all of these hold:

1. `bengali.is_implemented()` returns `True` and real outlines exist.
2. Every group in `BENGALI_INVENTORY` has drawn glyphs.
3. All 11 akhand conjuncts render as single glyphs.
4. `REQUIRED_FEATURES` all compile into GSUB.
5. GDEF has a populated `mark` class for all matras and marks.
6. HarfBuzz fixtures in `tests/shaping/` pass — at minimum:
   `ক কি কী ক্র ক্ল ক্ত ক্ষ জ্ঞ শ্র প্র ত্র` and 3-deep conjuncts.
7. FontBakery Bengali checks pass.
8. Visual regression baselines exist for a Bengali corpus.
9. Browser rendering verified (Chrome, Safari, Firefox).
10. Mixed Latin/Bengali line rendering verified in the website tester.
11. Integrated into Sans, Mono, and the variable font.

---

## 7. Out of scope

- Copying an existing Bengali typeface's outlines.
- Deriving Bengali letterforms from the Latin primitive set.
- Shipping codepoint coverage ahead of outlines (see §0).
