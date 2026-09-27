"""Shared design tokens for the Khulna type system.

Every script and every script (Indic) must derive its metrics from these
values so that the Latin and Bengali systems stay metrically compatible.
Changing a value here changes the whole family.
"""

UPEM = 1000
CAP_H = 700
X_H = 520
ASC = 750
DESC = -250
STROKE = 80
WX_DEF = 500
WX_MONO = 600
SB_L = 60
SB_R = 60

# Bengali-specific vertical metrics. The matra (headline) sits above the
# consonant body; Bengali has no true cap height, so x-height-relative
# placement is used instead.
BNG_MATRA_Y = 620        # top of the matra / headline stroke
BNG_MATRA_THICK = 76     # matra stroke weight, slightly under Latin STROKE
BNG_BODY_TOP = 560       # where consonant bodies meet the matra
BNG_BODY_BOT = 60        # baseline of the consonant body
BNG_DESC = -220          # descender depth for ra-barpay etc.
BNG_WX = 560             # default advance for a full consonant

# ── Diacritic metrics ─────────────────────────────────
# Spacing modifier letters are drawn in their own vertical zones rather
# than borrowed from a nearby glyph. Above-marks sit just above cap
# height; below-marks hang below the baseline. Mark weight is lighter
# than the text stroke, which is how a monoline system keeps small marks
# from reading heavier than the letters they sit on.
ACC_BASE = CAP_H          # 700 — baseline of the above-mark zone
ACC_TOP = CAP_H + 95     # 795 — top of the above-mark zone
ACC_W = 68               # mark stroke weight
ACC_MID = ACC_BASE + 47  # vertical centre of the above-mark zone
ACC_BELOW = -150         # deepest extent of below-marks
ACC_SPAN = WX_DEF         # marks span the full advance

# Horizontal inset so a mark never touches the sidebearing.
ACC_INSET = 110



def rect(p, x0, y0, x1, y1):
    p.moveTo((x0, y0))
    p.lineTo((x1, y0))
    p.lineTo((x1, y1))
    p.lineTo((x0, y1))
    p.closePath()


def oval(p, cx, cy, r):
    p.moveTo((cx + r, cy))
    p.curveTo((cx + r, cy + r), (cx, cy + r), (cx, cy))
    p.curveTo((cx - r, cy), (cx - r, cy - r), (cx, cy - r))
    p.curveTo((cx + r, cy - r), (cx + r, cy), (cx + r, cy))


def h_bar(p, x0, y, w, sw=None):
    sw = sw or STROKE
    rect(p, x0, y - sw // 2, x0 + w, y + sw // 2)
