"""Latin glyph construction for Khulna Sans / Khulna Mono.

Geometric skeleton: uniform stroke, flat terminals, no optical modulation.
Glyphs are built from primitives so that the family reads as one system.
"""

from .tokens import (
    UPEM, CAP_H, X_H, ASC, DESC, STROKE, WX_DEF, WX_MONO, SB_L, SB_R,
    ACC_BASE, ACC_TOP, ACC_W, ACC_MID, ACC_BELOW, ACC_SPAN, ACC_INSET,
    rect, oval, h_bar,
)


# ── Glyph builders (uppercase) ────────────────────────

def build_A(p):
    w = WX_DEF; hw = STROKE + 40
    rect(p, SB_L, 0, SB_L + hw, CAP_H)
    rect(p, w - SB_R - hw, 0, w - SB_R, CAP_H)
    h_bar(p, SB_L + hw, CAP_H * 0.62, w - 2 * (SB_L + hw) - hw)


def build_B(p):
    w = WX_DEF; hw = STROKE; rb = w - SB_R - hw
    rect(p, SB_L, 0, SB_L + hw, CAP_H)
    rect(p, rb, 0, rb + hw, CAP_H)
    rect(p, rb, CAP_H * 0.38, rb + hw * 2, CAP_H * 0.62)
    rect(p, rb, CAP_H * 0.1, rb + hw * 1.5, CAP_H * 0.38)
    rect(p, rb, CAP_H * 0.62, rb + hw * 2, CAP_H * 0.88)


def build_C(p):
    w = WX_DEF; hw = STROKE
    rect(p, w - SB_R - hw, 0, w - SB_R, CAP_H)
    rect(p, SB_L + hw, CAP_H * 0.12, w - SB_R, CAP_H * 0.22)
    rect(p, SB_L + hw, CAP_H * 0.78, w - SB_R, CAP_H * 0.88)
    rect(p, SB_L, 0, SB_L + hw, CAP_H * 0.12)
    rect(p, SB_L, CAP_H * 0.88, SB_L + hw, CAP_H)


def build_D(p):
    w = WX_DEF; hw = STROKE; rb = w - SB_R - hw
    rect(p, SB_L, 0, SB_L + hw, CAP_H)
    rect(p, rb, 0, rb + hw, CAP_H)
    rect(p, SB_L + hw, CAP_H * 0.1, rb, CAP_H * 0.22)
    rect(p, SB_L + hw, CAP_H * 0.78, rb, CAP_H * 0.9)


def build_E(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, SB_L + hw, CAP_H)
    rect(p, SB_L, 0, w - SB_R, hw)
    rect(p, SB_L, CAP_H // 2 - hw // 2, SB_L + hw * 2, CAP_H // 2 + hw // 2)
    rect(p, SB_L, CAP_H - hw, w - SB_R, CAP_H)


def build_F(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, SB_L + hw, CAP_H)
    rect(p, SB_L, 0, w - SB_R, hw)
    rect(p, SB_L, CAP_H // 2 - hw // 2, SB_L + hw * 2, CAP_H // 2 + hw // 2)


def build_G(p):
    w = WX_DEF; hw = STROKE
    rect(p, w - SB_R - hw, 0, w - SB_R, CAP_H)
    rect(p, SB_L + hw, CAP_H * 0.78, w - SB_R, CAP_H * 0.88)
    rect(p, SB_L + hw, CAP_H * 0.12, w - SB_R, CAP_H * 0.22)
    rect(p, SB_L, 0, SB_L + hw, CAP_H * 0.12)
    rect(p, SB_L, CAP_H * 0.88, SB_L + hw, CAP_H)
    rect(p, SB_L + hw, CAP_H * 0.38, SB_L + hw * 2, CAP_H * 0.5)


def build_H(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, SB_L + hw, CAP_H)
    rect(p, w - SB_R - hw, 0, w - SB_R, CAP_H)
    h_bar(p, SB_L + hw, CAP_H // 2, w - 2 * (SB_L + hw) - hw)


def build_I(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, w - SB_R, hw)
    rect(p, SB_L, CAP_H - hw, w - SB_R, CAP_H)
    rect(p, SB_L, 0, SB_L + hw, CAP_H)
    rect(p, w - SB_R - hw, 0, w - SB_R, CAP_H)


def build_J(p):
    w = WX_DEF; hw = STROKE
    rect(p, w - SB_R - hw, 0, w - SB_R, CAP_H)
    rect(p, SB_L, CAP_H - hw, w - SB_R, CAP_H)
    rect(p, SB_L + hw, CAP_H * 0.5, w - SB_R, CAP_H * 0.62)
    rect(p, SB_L + hw, CAP_H * 0.5, SB_L + hw * 2, DESC)


def build_K(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, SB_L + hw, CAP_H)
    rect(p, SB_L + hw, CAP_H // 2, w - SB_R, CAP_H // 2 + hw)
    rect(p, SB_L + hw, DESC, w - SB_R, DESC + hw)
    rect(p, w - SB_R - hw, 0, w - SB_R, CAP_H)


def build_L(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, SB_L + hw, CAP_H)
    rect(p, SB_L, DESC, w - SB_R, DESC + hw)


def build_M(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, SB_L + hw, CAP_H)
    rect(p, w - SB_R - hw, 0, w - SB_R, CAP_H)
    rect(p, SB_L + hw, 0, SB_L + hw * 2, CAP_H)
    rect(p, w - SB_R - hw * 2, 0, w - SB_R - hw, CAP_H)
    h_bar(p, SB_L + hw, 0, w - 2 * (SB_L + hw) - 2 * hw)


def build_N(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, SB_L + hw, CAP_H)
    rect(p, w - SB_R - hw, 0, w - SB_R, CAP_H)
    rect(p, SB_L + hw, 0, SB_L + hw * 2, CAP_H)
    rect(p, w - SB_R - hw * 2, 0, w - SB_R - hw, CAP_H)


def build_O(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L + hw, 0, w - SB_R, CAP_H)
    rect(p, SB_L, 0, SB_L + hw, CAP_H * 0.12)
    rect(p, SB_L, CAP_H * 0.88, SB_L + hw, CAP_H)


def build_P(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, SB_L + hw, CAP_H)
    rect(p, SB_L + hw, CAP_H * 0.38, w - SB_R, CAP_H * 0.62)
    rect(p, w - SB_R - hw, CAP_H * 0.38, w - SB_R, CAP_H * 0.62)
    rect(p, SB_L + hw, CAP_H * 0.1, w - SB_R, CAP_H * 0.22)


def build_Q(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L + hw, 0, w - SB_R, CAP_H)
    rect(p, SB_L, 0, SB_L + hw, CAP_H * 0.12)
    rect(p, SB_L, CAP_H * 0.88, SB_L + hw, CAP_H)
    rect(p, w // 2, DESC + hw, w // 2 + hw // 2, DESC + hw * 2)


def build_R(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, SB_L + hw, CAP_H)
    rect(p, SB_L + hw, CAP_H * 0.38, w - SB_R, CAP_H * 0.62)
    rect(p, w - SB_R - hw, CAP_H * 0.38, w - SB_R, CAP_H * 0.62)
    rect(p, SB_L + hw, CAP_H * 0.1, w - SB_R, CAP_H * 0.22)
    rect(p, w - SB_R - hw, 0, w - SB_R, CAP_H)


def build_S(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L + hw, 0, w - SB_R, hw)
    rect(p, SB_L, 0, SB_L + hw, CAP_H * 0.5)
    rect(p, SB_L + hw, CAP_H - hw, w - SB_R, CAP_H)
    rect(p, w - SB_R - hw, CAP_H * 0.5, w - SB_R, CAP_H)
    rect(p, SB_L + hw, CAP_H * 0.38, w - SB_R - hw, CAP_H * 0.62)


def build_T(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, w - SB_R, hw)
    rect(p, w // 2 - hw // 2, 0, w // 2 + hw // 2, CAP_H)


def build_U(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, SB_L + hw, CAP_H)
    rect(p, w - SB_R - hw, 0, w - SB_R, CAP_H)
    rect(p, SB_L + hw, CAP_H * 0.5, w - SB_R - hw, CAP_H)
    rect(p, SB_L + hw, CAP_H * 0.5, SB_L + hw * 2, DESC)
    rect(p, w - SB_R - hw * 2, CAP_H * 0.5, w - SB_R - hw, DESC)


def build_V(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, SB_L + hw, CAP_H * 0.85)
    rect(p, w - SB_R - hw, 0, w - SB_R, CAP_H * 0.85)
    rect(p, SB_L + hw, CAP_H * 0.7, w - SB_R - hw, CAP_H)
    rect(p, SB_L + hw, CAP_H * 0.7, w // 2, DESC)
    rect(p, w // 2, CAP_H * 0.7, w - SB_R - hw, DESC)


def build_W(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, SB_L + hw, CAP_H)
    rect(p, w - SB_R - hw, 0, w - SB_R, CAP_H)
    rect(p, SB_L + hw, CAP_H * 0.7, SB_L + hw * 2, CAP_H)
    rect(p, w - SB_R - hw * 2, CAP_H * 0.7, w - SB_R - hw, CAP_H)
    h_bar(p, SB_L + hw, CAP_H * 0.7, w - 2 * (SB_L + hw) - 2 * hw)
    rect(p, w // 2 - hw // 2, CAP_H * 0.7, w // 2 + hw // 2, DESC)


def build_X(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, SB_L + hw, CAP_H)
    rect(p, w - SB_R - hw, 0, w - SB_R, CAP_H)
    rect(p, SB_L + hw, CAP_H * 0.7, w - SB_R - hw, CAP_H)
    rect(p, SB_L + hw, DESC, w - SB_R - hw, DESC + hw)


def build_Y(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, SB_L + hw, CAP_H // 2)
    rect(p, w - SB_R - hw, 0, w - SB_R, CAP_H // 2)
    rect(p, w // 2 - hw // 2, 0, w // 2 + hw // 2, CAP_H)


def build_Z(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, w - SB_R, hw)
    rect(p, SB_L, CAP_H - hw, w - SB_R, CAP_H)
    rect(p, w - SB_R - hw, 0, w - SB_R, CAP_H)
    rect(p, SB_L, 0, SB_L + hw, CAP_H)


# ── Glyph builders (lowercase) ────────────────────────

def build_a(p):
    w = WX_DEF
    rect(p, SB_L, 0, w - SB_R, X_H)
    rect(p, SB_L, 0, SB_L + STROKE, X_H)
    rect(p, w - SB_R - STROKE, 0, w - SB_R, X_H)
    rect(p, SB_L + STROKE, X_H // 2, w - SB_R, X_H // 2 + STROKE)
    rect(p, SB_L, DESC, w - SB_R, DESC + STROKE)


def build_b(p):
    w = WX_DEF
    rect(p, SB_L, 0, SB_L + STROKE, ASC)
    rect(p, SB_L, ASC - STROKE, w - SB_R, ASC)
    rect(p, SB_L, DESC, SB_L + STROKE, 0)
    rect(p, w - SB_R - STROKE, 0, w - SB_R, ASC)


def build_c(p):
    w = WX_DEF
    rect(p, SB_L + STROKE, 0, w - SB_R, X_H)
    rect(p, SB_L, 0, SB_L + STROKE, X_H // 2)
    rect(p, SB_L, X_H // 2, SB_L + STROKE * 2, X_H // 2 + STROKE)
    rect(p, SB_L, X_H - STROKE, SB_L + STROKE * 2, X_H)


def build_d(p):
    w = WX_DEF
    rect(p, w - SB_R - STROKE, 0, w - SB_R, ASC)
    rect(p, SB_L, ASC - STROKE, w - SB_R - STROKE, ASC)
    rect(p, w - SB_R - STROKE, DESC, w - SB_R, 0)
    rect(p, SB_L, 0, SB_L + STROKE, ASC)


def build_e(p):
    w = WX_DEF
    rect(p, SB_L, 0, w - SB_R, X_H)
    rect(p, SB_L, 0, SB_L + STROKE, X_H)
    rect(p, SB_L, X_H // 2, w - SB_R, X_H // 2 + STROKE)
    rect(p, w - SB_R - STROKE, 0, w - SB_R, X_H // 2)
    rect(p, SB_L + STROKE, X_H - STROKE, w - SB_R, X_H)


def build_f(p):
    w = WX_DEF
    rect(p, SB_L, DESC, SB_L + STROKE, ASC)
    rect(p, SB_L, ASC - STROKE, w - SB_R, ASC)
    rect(p, w // 2 - STROKE // 2, X_H // 2, w // 2 + STROKE // 2, X_H)
    rect(p, w // 2 - STROKE // 2, X_H // 2, w - SB_R, X_H // 2 + STROKE)


def build_g(p):
    w = WX_DEF
    rect(p, SB_L, 0, SB_L + STROKE, ASC)
    rect(p, SB_L, ASC - STROKE, w - SB_R, ASC)
    rect(p, SB_L + STROKE, X_H // 2, w - SB_R, X_H // 2 + STROKE)
    rect(p, w - SB_R - STROKE, 0, w - SB_R, X_H // 2)
    rect(p, SB_L + STROKE, X_H - STROKE, w - SB_R, X_H)
    rect(p, SB_L, DESC, w - SB_R, DESC + STROKE)


def build_h(p):
    w = WX_DEF
    rect(p, SB_L, 0, SB_L + STROKE, ASC)
    rect(p, SB_L, ASC - STROKE, SB_L + STROKE * 2, ASC)
    rect(p, SB_L + STROKE, X_H // 2, SB_L + STROKE * 2, X_H // 2 + STROKE)
    rect(p, w - SB_R - STROKE, 0, w - SB_R, ASC)


def build_i(p):
    w = WX_DEF
    rect(p, w // 2 - STROKE // 2, 0, w // 2 + STROKE // 2, X_H)
    rect(p, w // 2 - STROKE // 2, ASC - STROKE, w // 2 + STROKE // 2, ASC)
    rect(p, SB_L, DESC, SB_L + STROKE, X_H // 2)


def build_j(p):
    w = WX_DEF
    rect(p, w // 2 - STROKE // 2, DESC, w // 2 + STROKE // 2, X_H)
    rect(p, w // 2 - STROKE // 2, ASC - STROKE, w // 2 + STROKE // 2, ASC)
    rect(p, SB_L, DESC, SB_L + STROKE, X_H // 2)


def build_k(p):
    w = WX_DEF
    rect(p, SB_L, 0, SB_L + STROKE, ASC)
    rect(p, SB_L + STROKE, ASC // 2, w - SB_R, ASC // 2 + STROKE)
    rect(p, SB_L + STROKE, DESC, w - SB_R, DESC + STROKE)
    rect(p, w - SB_R - STROKE, 0, w - SB_R, ASC)


def build_l(p):
    w = WX_DEF
    rect(p, SB_L, DESC, SB_L + STROKE, ASC)
    rect(p, SB_L, ASC - STROKE, w - SB_R, ASC)


def build_m(p):
    w = WX_DEF
    rect(p, SB_L, 0, SB_L + STROKE, ASC)
    rect(p, SB_L + STROKE, X_H // 2, SB_L + STROKE * 2, X_H // 2 + STROKE)
    rect(p, w - SB_R - STROKE, 0, w - SB_R, ASC)


def build_n(p):
    w = WX_DEF
    rect(p, SB_L, 0, SB_L + STROKE, ASC)
    rect(p, SB_L + STROKE, X_H // 2, SB_L + STROKE * 2, X_H // 2 + STROKE)
    rect(p, w - SB_R - STROKE, 0, w - SB_R, ASC)


def build_o(p):
    w = WX_DEF
    rect(p, SB_L + STROKE, 0, w - SB_R, X_H)
    rect(p, SB_L, 0, SB_L + STROKE, X_H // 2)
    rect(p, SB_L, X_H // 2, SB_L + STROKE * 2, X_H // 2 + STROKE)
    rect(p, SB_L, X_H - STROKE, SB_L + STROKE * 2, X_H)


def build_p(p):
    w = WX_DEF
    rect(p, SB_L, 0, SB_L + STROKE, ASC)
    rect(p, SB_L, ASC - STROKE, w - SB_R, ASC)
    rect(p, SB_L + STROKE, X_H // 2, w - SB_R, X_H // 2 + STROKE)
    rect(p, w - SB_R - STROKE, 0, w - SB_R, X_H // 2)
    rect(p, SB_L + STROKE, X_H - STROKE, w - SB_R, X_H)
    rect(p, SB_L, DESC, w - SB_R, DESC + STROKE)


def build_q(p):
    w = WX_DEF
    rect(p, w - SB_R - STROKE, 0, w - SB_R, ASC)
    rect(p, SB_L, ASC - STROKE, w - SB_R - STROKE, ASC)
    rect(p, w - SB_R - STROKE * 2, X_H // 2, w - SB_R - STROKE, X_H // 2 + STROKE)
    rect(p, SB_L, 0, w - SB_R - STROKE, X_H // 2 + STROKE)
    rect(p, SB_L, DESC, w - SB_R, DESC + STROKE)


def build_r(p):
    w = WX_DEF
    rect(p, SB_L, 0, SB_L + STROKE, ASC)
    rect(p, SB_L + STROKE, X_H // 2, SB_L + STROKE * 2, X_H // 2 + STROKE)


def build_s(p):
    w = WX_DEF
    rect(p, SB_L + STROKE, 0, w - SB_R, STROKE)
    rect(p, SB_L, 0, SB_L + STROKE, X_H // 2)
    rect(p, SB_L + STROKE, X_H - STROKE, w - SB_R, X_H)
    rect(p, w - SB_R - STROKE, X_H // 2, w - SB_R, X_H)
    rect(p, SB_L + STROKE, X_H // 2 - STROKE, w - SB_R - STROKE, X_H // 2 + STROKE)


def build_t(p):
    w = WX_DEF
    rect(p, SB_L, DESC, SB_L + STROKE, ASC)
    rect(p, SB_L, ASC - STROKE, w - SB_R, ASC)
    rect(p, w // 2 - STROKE // 2, X_H // 2, w // 2 + STROKE // 2, X_H)
    rect(p, w // 2 - STROKE // 2, X_H // 2, w - SB_R, X_H // 2 + STROKE)


def build_u(p):
    w = WX_DEF
    rect(p, SB_L, 0, SB_L + STROKE, ASC)
    rect(p, SB_L + STROKE, X_H // 2, SB_L + STROKE * 2, X_H // 2 + STROKE)
    rect(p, w - SB_R - STROKE, 0, w - SB_R, ASC)


def build_v(p):
    w = WX_DEF
    rect(p, SB_L, 0, SB_L + STROKE, X_H // 2)
    rect(p, w - SB_R - STROKE, 0, w - SB_R, X_H // 2)
    rect(p, SB_L + STROKE, X_H // 2, w // 2, ASC)
    rect(p, w // 2, X_H // 2, w - SB_R - STROKE, ASC)


def build_w(p):
    w = WX_DEF
    rect(p, SB_L, 0, SB_L + STROKE, X_H // 2)
    rect(p, w - SB_R - STROKE, 0, w - SB_R, X_H // 2)
    rect(p, SB_L + STROKE, X_H // 2, SB_L + STROKE * 2, ASC)
    rect(p, w - SB_R - STROKE * 2, X_H // 2, w - SB_R - STROKE, ASC)
    h_bar(p, SB_L + STROKE, X_H // 2, w - 2 * (SB_L + STROKE) - 2 * STROKE)


def build_x(p):
    w = WX_DEF
    rect(p, SB_L, 0, SB_L + STROKE, X_H)
    rect(p, w - SB_R - STROKE, 0, w - SB_R, X_H)
    rect(p, SB_L + STROKE, X_H // 2, w - SB_R - STROKE, X_H)
    rect(p, SB_L + STROKE, DESC, w - SB_R - STROKE, DESC + STROKE)


def build_y(p):
    w = WX_DEF
    rect(p, SB_L, 0, SB_L + STROKE, X_H // 2)
    rect(p, w - SB_R - STROKE, 0, w - SB_R, X_H // 2)
    rect(p, SB_L + STROKE, X_H // 2, w // 2, ASC)
    rect(p, w // 2, X_H // 2, w - SB_R - STROKE, ASC)
    rect(p, SB_L, DESC, w - SB_R, DESC + STROKE)


def build_z(p):
    w = WX_DEF
    rect(p, SB_L, 0, w - SB_R, STROKE)
    rect(p, SB_L, X_H - STROKE, w - SB_R, X_H)
    rect(p, w - SB_R - STROKE, 0, w - SB_R, X_H)
    rect(p, SB_L, 0, SB_L + STROKE, X_H)


# ── Glyph builders (digits) ───────────────────────────

def build_zero(p):
    w = WX_DEF
    oval(p, w // 2, CAP_H // 2, CAP_H // 2 - STROKE)
    rect(p, w // 2 - STROKE // 2, 0, w // 2 + STROKE // 2, CAP_H)


def build_one(p):
    w = WX_DEF
    rect(p, w // 2 - STROKE // 2, DESC, w // 2 + STROKE // 2, ASC)
    rect(p, SB_L, ASC - STROKE, w - SB_R, ASC)


def build_two(p):
    w = WX_DEF
    rect(p, SB_L, 0, w - SB_R, STROKE)
    rect(p, w - SB_R - STROKE, 0, w - SB_R, CAP_H // 2)
    rect(p, SB_L, CAP_H // 2 - STROKE // 2, w - SB_R - STROKE, CAP_H // 2 + STROKE // 2)
    rect(p, SB_L, CAP_H // 2, SB_L + STROKE, CAP_H)
    rect(p, SB_L, CAP_H - STROKE, w - SB_R, CAP_H)


def build_three(p):
    w = WX_DEF
    rect(p, SB_L, 0, w - SB_R, STROKE)
    rect(p, SB_L, CAP_H - STROKE, w - SB_R, CAP_H)
    rect(p, w - SB_R - STROKE, 0, w - SB_R, CAP_H)
    rect(p, SB_L, CAP_H // 2 - STROKE // 2, w - SB_R - STROKE, CAP_H // 2 + STROKE // 2)


def build_four(p):
    w = WX_DEF
    rect(p, SB_L, 0, SB_L + STROKE, CAP_H)
    rect(p, w // 2 - STROKE // 2, CAP_H // 2, w // 2 + STROKE // 2, CAP_H)
    rect(p, w // 2 - STROKE // 2, CAP_H // 2, w - SB_R, CAP_H // 2 + STROKE)


def build_five(p):
    w = WX_DEF
    rect(p, SB_L, 0, w - SB_R, STROKE)
    rect(p, SB_L, 0, SB_L + STROKE, CAP_H // 2)
    rect(p, SB_L, CAP_H // 2 - STROKE // 2, w - SB_R, CAP_H // 2 + STROKE // 2)
    rect(p, w - SB_R - STROKE, CAP_H // 2, w - SB_R, CAP_H)
    rect(p, SB_L, CAP_H - STROKE, w - SB_R, CAP_H)


def build_six(p):
    w = WX_DEF
    rect(p, SB_L + STROKE, 0, w - SB_R, X_H)
    rect(p, SB_L, 0, SB_L + STROKE, X_H // 2)
    rect(p, SB_L, X_H // 2, SB_L + STROKE * 2, X_H // 2 + STROKE)
    rect(p, SB_L, X_H - STROKE, SB_L + STROKE * 2, X_H)
    rect(p, SB_L, DESC, w - SB_R, DESC + STROKE)
    rect(p, SB_L, 0, SB_L + STROKE, ASC)


def build_seven(p):
    w = WX_DEF
    rect(p, SB_L, 0, w - SB_R, STROKE)
    rect(p, w - SB_R - STROKE, 0, w - SB_R, CAP_H)
    rect(p, SB_L + STROKE, CAP_H - STROKE, w - SB_R - STROKE, CAP_H)


def build_eight(p):
    w = WX_DEF
    oval(p, w // 2, CAP_H // 2, CAP_H // 2 - STROKE)
    oval(p, w // 2, DESC + STROKE, CAP_H // 2 - STROKE)
    rect(p, w // 2 - STROKE // 2, CAP_H // 2 - STROKE // 2, w // 2 + STROKE // 2, CAP_H // 2 + STROKE // 2)


def build_nine(p):
    w = WX_DEF
    rect(p, w - SB_R - STROKE, 0, w - SB_R, ASC)
    rect(p, SB_L + STROKE, CAP_H // 2, w - SB_R, CAP_H // 2 + STROKE)
    rect(p, SB_L + STROKE, CAP_H // 2 - STROKE, w - SB_R - STROKE, CAP_H // 2 + STROKE)
    rect(p, SB_L, X_H - STROKE, SB_L + STROKE * 2, X_H)
    rect(p, SB_L, DESC, w - SB_R, DESC + STROKE)


# ── Glyph builders (punctuation) ──────────────────────

def build_period(p):
    w = WX_DEF; r = STROKE // 2
    rect(p, w // 2 - r, DESC + r, w // 2 + r, DESC + 3 * r)


def build_comma(p):
    w = WX_DEF; r = STROKE // 2
    rect(p, w // 2 - r, DESC + r, w // 2 + r, DESC + 3 * r)
    rect(p, w // 2 - r, DESC - r, w // 2 + r, DESC + r)


def build_exclam(p):
    w = WX_DEF; hw = STROKE
    rect(p, w // 2 - hw // 2, ASC - hw, w // 2 + hw // 2, ASC)
    rect(p, w // 2 - hw // 2, DESC, w // 2 + hw // 2, ASC - hw)
    rect(p, w // 2 - hw, DESC, w // 2 + hw, DESC + hw)


def build_question(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L + hw, 0, w - SB_R, X_H // 2)
    rect(p, w - SB_R - hw, 0, w - SB_R, X_H // 2)
    rect(p, SB_L, X_H // 2 - hw // 2, w - SB_R, X_H // 2 + hw // 2)
    rect(p, w // 2 - hw // 2, ASC - hw, w // 2 + hw // 2, ASC)
    rect(p, w // 2 - hw, DESC, w // 2 + hw, DESC + hw)


def build_semicolon(p):
    w = WX_DEF; hw = STROKE
    rect(p, w // 2 - hw // 2, 0, w // 2 + hw // 2, X_H // 2)
    rect(p, w // 2 - hw // 2, X_H // 2, w // 2 + hw // 2, X_H // 2 + hw)
    rect(p, w // 2 - hw, DESC, w // 2 + hw, DESC + hw)


def build_colon(p):
    w = WX_DEF; hw = STROKE
    rect(p, w // 2 - hw // 2, ASC // 2, w // 2 + hw // 2, ASC // 2 + hw)
    rect(p, w // 2 - hw // 2, DESC + hw, w // 2 + hw // 2, DESC + 2 * hw)


def build_hyphen(p):
    w = WX_DEF
    rect(p, SB_L, CAP_H // 2 - STROKE // 2, w - SB_R, CAP_H // 2 + STROKE // 2)


def build_underscore(p):
    w = WX_DEF
    rect(p, SB_L, DESC, w - SB_R, DESC + STROKE)


def build_asterisk(p):
    w = WX_DEF; hw = STROKE
    rect(p, w // 2 - hw // 2, CAP_H - hw, w // 2 + hw // 2, CAP_H)
    rect(p, w // 2 - hw // 2, 0, w // 2 + hw // 2, hw)


def build_mu(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, SB_L + hw, X_H // 2)
    rect(p, w - SB_R - hw, 0, w - SB_R, X_H // 2)
    rect(p, SB_L + hw, X_H // 2, w - SB_R - hw, X_H // 2 + hw)
    rect(p, SB_L, DESC, w - SB_R, DESC + hw)


def build_cent(p):
    w = WX_DEF; hw = STROKE
    rect(p, w // 2 - hw // 2, DESC, w // 2 + hw // 2, ASC)
    rect(p, SB_L, ASC - hw, w - SB_R, ASC)
    rect(p, SB_L, DESC, w - SB_R, DESC + hw)


def build_yen(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, w - SB_R, hw)
    rect(p, w // 2 - hw, 0, w // 2 + hw, ASC)
    rect(p, SB_L, ASC - hw, w - SB_R, ASC)


def build_asciicircum(p):
    w = WX_MONO; hw = STROKE
    rect(p, w // 2 - hw, ASC - hw * 2, w // 2 + hw, ASC - hw)
    rect(p, w // 2 - hw // 2, ASC - hw * 2, w // 2 + hw // 2, ASC)






































































































def build_backtick(p):
    w = WX_MONO; hw = STROKE
    rect(p, w // 2 - hw // 2, ASC - hw, w // 2 + hw // 2, ASC)
    rect(p, w // 2 - hw, ASC - hw * 2, w // 2 + hw, ASC - hw)


def build_tildebar(p):
    """Full-width flat bar for Mono asciitilde (~)."""
    w = WX_MONO; hw = STROKE
    rect(p, SB_L, X_H // 2, w - SB_R, X_H // 2 + hw // 2)


def build_slash(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, DESC, SB_L + hw, ASC)
    rect(p, w - SB_R - hw, DESC, w - SB_R, ASC)


def build_backslash(p):
    w = WX_DEF; hw = STROKE
    rect(p, w - SB_R - hw, DESC, w - SB_R, ASC)
    rect(p, SB_L, DESC, SB_L + hw, ASC)


def build_bar(p):
    w = WX_DEF; hw = STROKE
    rect(p, w // 2 - hw // 4, DESC, w // 2 + hw // 4, ASC)














def build_less(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, CAP_H // 2 - hw // 2, w - SB_R, CAP_H // 2 + hw // 2)
    rect(p, SB_L, DESC, w // 2, CAP_H // 2 - hw // 2)
    rect(p, w // 2, CAP_H // 2 + hw // 2, w - SB_R, DESC)


def build_greater(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, CAP_H // 2 - hw // 2, w - SB_R, CAP_H // 2 + hw // 2)
    rect(p, SB_L, CAP_H // 2 + hw // 2, w // 2, DESC)
    rect(p, w // 2, DESC, w - SB_R, CAP_H // 2 - hw // 2)


def build_quotesingle(p):
    w = WX_DEF; hw = STROKE
    rect(p, w // 2 - hw // 4, ASC - hw, w // 2 + hw // 4, ASC)


def build_quotedbl(p):
    w = WX_DEF; hw = STROKE
    rect(p, w // 2 - hw // 2, ASC - hw, w // 2 + hw // 2, ASC)
    rect(p, w // 2 - hw // 2, ASC - hw * 2, w // 2 + hw // 2, ASC - hw)


def build_at(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L + hw, 0, w - SB_R, X_H)
    rect(p, SB_L, 0, SB_L + hw, X_H // 2)
    rect(p, SB_L, X_H // 2, SB_L + hw * 2, X_H // 2 + hw)
    rect(p, SB_L, X_H - hw, SB_L + hw * 2, X_H)


def build_dollar(p):
    w = WX_DEF; hw = STROKE
    rect(p, w // 2 - hw // 2, DESC, w // 2 + hw // 2, ASC)
    rect(p, SB_L + hw // 2, DESC, w // 2 - hw // 2, DESC + hw)
    rect(p, w // 2 + hw // 2, ASC - hw, w - SB_R - hw // 2, ASC)
    rect(p, SB_L, CAP_H // 2 - hw // 2, w // 2 - hw // 2, CAP_H // 2 + hw // 2)
    rect(p, w // 2 + hw // 2, CAP_H // 2 - hw // 2, w - SB_R, CAP_H // 2 + hw // 2)


def build_percent(p):
    w = WX_DEF; hw = STROKE
    oval(p, SB_L + WX_DEF // 4, CAP_H // 2, CAP_H // 4)
    oval(p, w - SB_R - WX_DEF // 4, CAP_H // 2, CAP_H // 4)
    rect(p, SB_L + WX_DEF // 4 - hw // 2, CAP_H // 2 - hw // 2, SB_L + WX_DEF // 4 + hw // 2, CAP_H // 2 + hw // 2)
    rect(p, w - SB_R - WX_DEF // 4 - hw // 2, CAP_H // 2 - hw // 2, w - SB_R - WX_DEF // 4 + hw // 2, CAP_H // 2 + hw // 2)


def build_ampersand(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, SB_L + hw, X_H)
    rect(p, w - SB_R - hw, 0, w - SB_R, X_H)
    rect(p, SB_L + hw, X_H // 2, w - SB_R - hw, X_H // 2 + hw)


def build_pound(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, SB_L + hw, CAP_H)
    rect(p, w - SB_R - hw, 0, w - SB_R, CAP_H)
    h_bar(p, SB_L, CAP_H // 2, w - 2 * SB_L)
    h_bar(p, SB_L, CAP_H // 4, w - 2 * SB_L)
    h_bar(p, SB_L, CAP_H * 3 // 4, w - 2 * SB_L)


def build_section(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L + hw, 0, w - SB_R, hw)
    rect(p, SB_L, 0, SB_L + hw, CAP_H)
    rect(p, w - SB_R - hw, 0, w - SB_R, CAP_H)
    rect(p, SB_L + hw, CAP_H - hw, w - SB_R, CAP_H)


def build_degree(p):
    w = WX_DEF
    oval(p, w // 2, CAP_H // 2, STROKE * 2)


def build_plus(p):
    w = WX_DEF; hw = STROKE
    rect(p, w // 2 - hw // 2, CAP_H // 2 - hw // 2, w // 2 + hw // 2, CAP_H // 2 + hw // 2)
    rect(p, SB_L, CAP_H // 2 - hw // 2, w - SB_R, CAP_H // 2 + hw // 2)


def build_minus(p):
    w = WX_DEF
    rect(p, SB_L, CAP_H // 2 - STROKE // 2, w - SB_R, CAP_H // 2 + STROKE // 2)


def build_equal(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, CAP_H // 2 - hw, w - SB_R, CAP_H // 2)
    rect(p, SB_L, CAP_H // 2 + hw // 2, w - SB_R, CAP_H // 2 + hw // 2 + hw)


def build_ellipsis(p):
    w = WX_DEF; hw = STROKE
    for i in range(3):
        x = w // 2 - hw + i * hw * 2
        rect(p, x, DESC + hw, x + hw, DESC + 2 * hw)


def build_quoteleft(p):
    w = WX_DEF; hw = STROKE
    rect(p, w // 2 - hw // 4, ASC - hw, w // 2 + hw // 4, ASC)


def build_quoteright(p):
    w = WX_DEF; hw = STROKE
    rect(p, w // 2 - hw // 4, ASC - hw, w // 2 + hw // 4, ASC)


def build_quotedblleft(p):
    w = WX_DEF; hw = STROKE
    rect(p, w // 2 - hw, ASC - hw, w // 2 - hw // 2, ASC)
    rect(p, w // 2 + hw // 2, ASC - hw, w // 2 + hw, ASC)


def build_quotedblright(p):
    w = WX_DEF; hw = STROKE
    rect(p, w // 2 - hw, ASC - hw, w // 2 - hw // 2, ASC)
    rect(p, w // 2 + hw // 2, ASC - hw, w // 2 + hw, ASC)


    # ── Diacritics ──────────────────────────────────────
    # Drawn in the shared accent zones (tokens.ACC_*). These previously
    # borrowed unrelated builders — a cedilla was a comma, a breve was a
    # filled period square, a caron was two vertical bars. Each is now the
    # shape its name describes, at mark weight rather than text weight.


def build_acute(p):
    """Acute: a single stroke rising left-to-right."""
    y0, y1 = ACC_BASE, ACC_TOP
    p.moveTo((ACC_INSET, y0))
    p.lineTo((ACC_SPAN - ACC_INSET, y1))
    p.lineTo((ACC_SPAN - ACC_INSET - ACC_W, y1))
    p.lineTo((ACC_INSET + ACC_W, y0))
    p.closePath()


def build_grave(p):
    """Grave: mirror of acute, falling left-to-right."""
    y0, y1 = ACC_BASE, ACC_TOP
    p.moveTo((ACC_INSET, y1))
    p.lineTo((ACC_SPAN - ACC_INSET, y0))
    p.lineTo((ACC_SPAN - ACC_INSET - ACC_W, y0))
    p.lineTo((ACC_INSET + ACC_W, y1))
    p.closePath()


def build_circumflex(p):
    """Circumflex: two strokes rising to a central peak."""
    apex = ACC_SPAN // 2
    p.moveTo((ACC_INSET, ACC_BASE))
    p.lineTo((apex, ACC_TOP))
    p.lineTo((ACC_SPAN - ACC_INSET, ACC_BASE))
    p.lineTo((ACC_SPAN - ACC_INSET - ACC_W, ACC_BASE))
    p.lineTo((apex, ACC_TOP - ACC_W))
    p.lineTo((ACC_INSET + ACC_W, ACC_BASE))
    p.closePath()


def build_caron(p):
    """Caron (inverted circumflex): peak pointing down."""
    apex = ACC_SPAN // 2
    p.moveTo((ACC_INSET, ACC_TOP))
    p.lineTo((apex, ACC_BASE))
    p.lineTo((ACC_SPAN - ACC_INSET, ACC_TOP))
    p.lineTo((ACC_SPAN - ACC_INSET - ACC_W, ACC_TOP))
    p.lineTo((apex, ACC_BASE + ACC_W))
    p.lineTo((ACC_INSET + ACC_W, ACC_TOP))
    p.closePath()


def build_tilde(p):
    """Tilde: a true S-wave, crest then trough.

    This was previously drawn with straight diagonals, which made it
    outline-identical to the circumflex — a peak, not a wave. Built from
    two cubic segments: one crest, one trough, crossing at both ends and
    at the centre.
    """
    x0 = ACC_INSET
    x1 = ACC_SPAN - ACC_INSET
    # A tilde is a delicate mark: lighter weight and smaller amplitude than
    # the other accents, sized so the full band (2*amp + t) still fits the
    # 95-unit accent zone. ym is biased up by t/2 because the band's lower
    # edge is offset downward from the upper edge.
    ym = ACC_MID - 23
    amp = 24
    t = 46
    q1, q3 = x0 + 30, x1 - 30
    c1, c3 = x0 + 120, x1 - 120

    p.moveTo((x0, ym))
    p.curveTo((q1, ym + amp), (c1, ym + amp), (ACC_SPAN // 2, ym))
    p.curveTo((c3, ym - amp), (q3, ym - amp), (x1, ym))
    p.lineTo((x1, ym + t))
    p.curveTo((q3, ym - amp + t), (c3, ym - amp + t), (ACC_SPAN // 2, ym + t))
    p.curveTo((c1, ym + amp + t), (q1, ym + amp + t), (x0, ym + t))
    p.closePath()


def build_macron(p):
    """Macron: a flat horizontal bar at accent height."""
    rect(p, ACC_INSET, ACC_MID - ACC_W // 2,
         ACC_SPAN - ACC_INSET, ACC_MID + ACC_W // 2)


def build_breve(p):
    """Breve: a shallow cup opening upward, like a flattened U."""
    cx, r = ACC_SPAN // 2, (ACC_SPAN // 2) - ACC_INSET
    depth = 120
    p.moveTo((ACC_INSET, ACC_TOP))
    p.curveTo((cx, ACC_TOP - depth), (ACC_SPAN - ACC_INSET, ACC_TOP),
              (ACC_SPAN - ACC_INSET, ACC_TOP))
    p.lineTo((ACC_SPAN - ACC_INSET - ACC_W, ACC_TOP))
    p.curveTo((cx, ACC_TOP - depth + ACC_W * 1.6),
              (ACC_INSET + ACC_W, ACC_TOP), (ACC_INSET, ACC_TOP))
    p.closePath()


def build_ring(p):
    """Ring: a small circle above the letter."""
    cx, cy = ACC_SPAN // 2, ACC_MID
    r = 62
    cx0, cx1 = cx - r, cx + r
    k = r * 0.5523
    sw = ACC_W / 2
    # outer then inner contour, wound opposite, to leave a ring
    p.moveTo((cx + r, cy))
    p.curveTo((cx + r, cy + k), (cx + k, cy + r), (cx, cy + r))
    p.curveTo((cx - k, cy + r), (cx - r, cy + k), (cx - r, cy))
    p.curveTo((cx - r, cy - k), (cx - k, cy - r), (cx, cy - r))
    p.curveTo((cx + k, cy - r), (cx + r, cy - k), (cx + r, cy))
    p.closePath()
    ri = r - sw
    ki = ri * 0.5523
    p.moveTo((cx + ri, cy))
    p.curveTo((cx + ri, cy - ki), (cx + ki, cy - ri), (cx, cy - ri))
    p.curveTo((cx - ki, cy - ri), (cx - ri, cy - ki), (cx - ri, cy))
    p.curveTo((cx - ri, cy + ki), (cx - ki, cy + ri), (cx, cy + ri))
    p.curveTo((cx + ki, cy + ri), (cx + ri, cy + ki), (cx + ri, cy))
    p.closePath()


def _dot(p, cx, cy, r):
    """A filled dot, used by dieresis and dotaccent."""
    k = r * 0.5523
    p.moveTo((cx + r, cy))
    p.curveTo((cx + r, cy + k), (cx + k, cy + r), (cx, cy + r))
    p.curveTo((cx - k, cy + r), (cx - r, cy + k), (cx - r, cy))
    p.curveTo((cx - r, cy - k), (cx - k, cy - r), (cx, cy - r))
    p.curveTo((cx + k, cy - r), (cx + r, cy - k), (cx + r, cy))
    p.closePath()


def build_dieresis(p):
    """Dieresis: two dots side by side."""
    r = 52
    _dot(p, ACC_SPAN // 2 - 95, ACC_MID, r)
    _dot(p, ACC_SPAN // 2 + 95, ACC_MID, r)


def build_dotaccent(p):
    """Dot above: a single dot at accent height."""
    _dot(p, ACC_SPAN // 2, ACC_MID, 52)


def build_tonos(p):
    """Greek tonos: a raised comma-like mark."""
    cx, cy = ACC_SPAN // 2, ACC_MID
    r = 58
    k = r * 0.5523
    p.moveTo((cx + r * 0.5, cy + r))
    p.curveTo((cx + r, cy + k * 0.5), (cx + k, cy - r), (cx - r * 0.3, cy - r))
    p.lineTo((cx - r * 0.3, cy - r + ACC_W))
    p.curveTo((cx + k * 0.4, cy - r + ACC_W),
              (cx + r - ACC_W, cy + k * 0.4 - ACC_W * 0.6),
              (cx + r * 0.5 - ACC_W * 0.4, cy + r - ACC_W))
    p.closePath()


def build_hookabove(p):
    """Hook above: a small rising hook, drawn as a clean L-shape.

    The previous version had a 14-degree jaggy segment that triggered
    fontbakery's outline_jaggy_segments and outline_short_segments checks.
    """
    x0 = ACC_INSET + 40
    y0 = ACC_BASE
    p.moveTo((x0, y0))
    p.lineTo((x0 + ACC_W, y0))
    p.lineTo((x0 + ACC_W, ACC_TOP - ACC_W))
    p.lineTo((x0 + ACC_W + 80, ACC_TOP - ACC_W))
    p.lineTo((x0 + ACC_W + 80, ACC_TOP - ACC_W + ACC_W))
    p.lineTo((x0, y0 + ACC_W))
    p.closePath()


def build_horn(p):
    """Horn: a small rising wedge, as in Vietnamese ơ / ư."""
    x0 = ACC_INSET + 20
    p.moveTo((x0, ACC_BASE))
    p.lineTo((x0 + 70, ACC_TOP))
    p.lineTo((x0 + 70 + ACC_W, ACC_TOP))
    p.lineTo((x0 + ACC_W, ACC_BASE))
    p.closePath()


def build_hungarumlaut(p):
    """Double acute: two parallel rising strokes, kept inside the inset.

    x0 is offset by ACC_W so the stroke's lower-left corner lands exactly
    on ACC_INSET rather than ACC_W short of it.
    """
    for dx in (0, 130):
        x0 = ACC_INSET + ACC_W + dx
        p.moveTo((x0, ACC_BASE))
        p.lineTo((x0 + 80, ACC_TOP))
        p.lineTo((x0 + 80 - ACC_W, ACC_TOP))
        p.lineTo((x0 - ACC_W, ACC_BASE))
        p.closePath()


def build_cedilla(p):
    """Cedilla: a small hook hanging below the baseline."""
    cx = ACC_SPAN // 2
    p.moveTo((cx, 10))
    p.lineTo((cx + ACC_W, 10))
    p.curveTo((cx + ACC_W, -70), (cx - 10, ACC_BELOW + 40), (cx - 95, ACC_BELOW))
    p.lineTo((cx - 95 - ACC_W * 0.8, ACC_BELOW + ACC_W))
    p.curveTo((cx + ACC_W * 0.2, ACC_BELOW + ACC_W * 2.4),
              (cx + ACC_W * 2.1, -60), (cx, 10 + ACC_W))
    p.closePath()


def build_ogonek(p):
    """Ogonek: a tail descending below the baseline, curving right."""
    cx = ACC_SPAN // 2
    p.moveTo((cx, 0))
    p.lineTo((cx + ACC_W, 0))
    p.curveTo((cx + ACC_W, -80), (cx + 40, ACC_BELOW + 30), (cx + 110, ACC_BELOW))
    p.lineTo((cx + 110 + ACC_W, ACC_BELOW + ACC_W))
    p.curveTo((cx + ACC_W * 2.2, ACC_BELOW + ACC_W * 2.6),
              (cx + ACC_W * 2.0, -70), (cx, 0 - ACC_W))
    p.closePath()


def build_guilsinglleft(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, CAP_H // 2 - hw // 2, SB_L + hw, CAP_H // 2 + hw // 2)
    rect(p, SB_L + hw, CAP_H // 2 - hw // 2, SB_L + hw * 2, CAP_H // 2 + hw // 2)
    rect(p, w - SB_R - hw, CAP_H // 2 - hw // 2, w - SB_R, CAP_H // 2 + hw // 2)


def build_guilsinglright(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, CAP_H // 2 - hw // 2, SB_L + hw, CAP_H // 2 + hw // 2)
    rect(p, SB_L, CAP_H // 2 - hw // 2, w - SB_R, CAP_H // 2 + hw // 2)
    rect(p, w - SB_R - hw, CAP_H // 2 - hw // 2, w - SB_R, CAP_H // 2 + hw // 2)


def build_emdash(p):
    w = WX_DEF
    rect(p, SB_L, CAP_H // 2 - STROKE, w - SB_R, CAP_H // 2 + STROKE)


def build_endash(p):
    w = WX_DEF
    rect(p, SB_L, CAP_H // 2 - STROKE // 2, w - SB_R, CAP_H // 2 + STROKE // 2)


def build_parenleft(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, DESC, SB_L + hw, ASC)
    rect(p, SB_L + hw, DESC, SB_L + hw * 2, DESC + hw)
    rect(p, SB_L + hw, ASC - hw, SB_L + hw * 2, ASC)


def build_parenright(p):
    w = WX_DEF; hw = STROKE
    rect(p, w - SB_R - hw, DESC, w - SB_R, ASC)
    rect(p, w - SB_R - hw * 2, DESC, w - SB_R - hw, DESC + hw)
    rect(p, w - SB_R - hw * 2, ASC - hw, w - SB_R - hw, ASC)


def build_braceleft(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L + hw, DESC, SB_L + hw * 2, DESC + hw)
    rect(p, SB_L, DESC, SB_L + hw * 2, ASC)
    rect(p, SB_L + hw, ASC - hw, SB_L + hw * 2, ASC)


def build_braceright(p):
    w = WX_DEF; hw = STROKE
    rect(p, w - SB_R - hw * 2, DESC, w - SB_R - hw, DESC + hw)
    rect(p, w - SB_R - hw * 2, DESC, w - SB_R, ASC)
    rect(p, w - SB_R - hw * 2, ASC - hw, w - SB_R, ASC)


def build_bracketleft(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, DESC, SB_L + hw, ASC)
    rect(p, SB_L, DESC, w - SB_R, DESC + hw)
    rect(p, SB_L, ASC - hw, w - SB_R, ASC)


def build_bracketright(p):
    w = WX_DEF; hw = STROKE
    rect(p, w - SB_R - hw, DESC, w - SB_R, ASC)
    rect(p, SB_L, DESC, w - SB_R, DESC + hw)
    rect(p, SB_L, ASC - hw, w - SB_R, ASC)


def build_lessequal(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, CAP_H // 2 - hw // 2, w - SB_R, CAP_H // 2 + hw // 2)
    rect(p, SB_L, DESC, w // 2, CAP_H // 2 - hw // 2)
    rect(p, w // 2, CAP_H // 2 + hw // 2, w - SB_R, DESC)


def build_greaterequal(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, CAP_H // 2 - hw // 2, w - SB_R, CAP_H // 2 + hw // 2)
    rect(p, SB_L, CAP_H // 2 + hw // 2, w // 2, DESC)
    rect(p, w // 2, DESC, w - SB_R, CAP_H // 2 - hw // 2)


def build_notequal(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, CAP_H // 2 - hw // 2, w - SB_R, CAP_H // 2 + hw // 2)
    rect(p, SB_L, DESC, w // 2, CAP_H // 2 - hw // 2)
    rect(p, w // 2, CAP_H // 2 + hw // 2, w - SB_R, DESC)
    rect(p, w // 2 - hw // 2, CAP_H // 2 - hw // 2, w // 2 + hw // 2, CAP_H // 2 + hw // 2)


def build_multiply(p):
    w = WX_DEF; hw = STROKE
    rect(p, w // 2 - hw // 2, CAP_H // 2 - hw // 2, w // 2 + hw // 2, CAP_H // 2 + hw // 2)
    rect(p, SB_L, CAP_H // 2 - hw // 2, w - SB_R, CAP_H // 2 + hw // 2)


def build_divide(p):
    w = WX_DEF; hw = STROKE
    rect(p, w // 2 - hw // 2, DESC, w // 2 + hw // 2, ASC)
    rect(p, SB_L, CAP_H // 2 - hw // 2, w - SB_R, CAP_H // 2 + hw // 2)
    rect(p, SB_L, DESC, w - SB_R, DESC + hw)
    rect(p, SB_L, ASC - hw, w - SB_R, ASC)


def build_paragraph(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, SB_L + hw, ASC)
    rect(p, w - SB_R - hw, 0, w - SB_R, ASC)
    rect(p, SB_L + hw, DESC, SB_L + hw * 2, DESC + hw)
    rect(p, w - SB_R - hw * 2, DESC, w - SB_R - hw, DESC + hw)


def build_copyright(p):
    w = WX_DEF; hw = STROKE
    oval(p, w // 2, CAP_H // 2, CAP_H // 2 - hw)
    rect(p, w // 2 - hw // 2, CAP_H // 2, w // 2 + hw // 2, CAP_H)


def build_registered(p):
    w = WX_DEF; hw = STROKE
    oval(p, w // 2, CAP_H // 2, CAP_H // 2 - hw)
    rect(p, w // 2 - hw // 2, CAP_H // 2, w // 2 + hw // 2, CAP_H)
    rect(p, SB_L, DESC, w - SB_R, DESC + hw)


def build_trademark(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, w - SB_R, hw)
    rect(p, SB_L, 0, SB_L + hw, CAP_H)
    rect(p, w - SB_R - hw, 0, w - SB_R, CAP_H)
    rect(p, SB_L, CAP_H - hw, w - SB_R, CAP_H)


def build_periodcentered(p):
    w = WX_DEF; hw = STROKE
    r = hw // 2
    rect(p, w // 2 - r, CAP_H // 2 - r, w // 2 + r, CAP_H // 2 + r)


def build_guillemotleft(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, CAP_H // 2 - hw // 2, SB_L + hw, CAP_H // 2 + hw // 2)
    rect(p, SB_L + hw, CAP_H // 2 - hw // 2, SB_L + hw * 2, CAP_H // 2 + hw // 2)
    rect(p, w - SB_R - hw, CAP_H // 2 - hw // 2, w - SB_R, CAP_H // 2 + hw // 2)


def build_guillemotright(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, CAP_H // 2 - hw // 2, SB_L + hw, CAP_H // 2 + hw // 2)
    rect(p, w - SB_R - hw * 2, CAP_H // 2 - hw // 2, w - SB_R - hw, CAP_H // 2 + hw // 2)
    rect(p, w - SB_R - hw, CAP_H // 2 - hw // 2, w - SB_R, CAP_H // 2 + hw // 2)


def build_arrowleft(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, CAP_H // 2 - hw // 2, w - SB_R, CAP_H // 2 + hw // 2)
    rect(p, w // 2, CAP_H // 2 - hw // 2, w // 2 + hw, DESC)
    rect(p, w // 2, CAP_H // 2 - hw // 2, w // 2 + hw, ASC)


def build_arrowright(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, CAP_H // 2 - hw // 2, w - SB_R, CAP_H // 2 + hw // 2)
    rect(p, w // 2 - hw, DESC, w // 2, CAP_H // 2 + hw // 2)
    rect(p, w // 2 - hw, ASC, w // 2, CAP_H // 2 + hw // 2)


def build_arrowup(p):
    w = WX_DEF; hw = STROKE
    rect(p, w // 2 - hw // 2, DESC, w // 2 + hw // 2, ASC)
    rect(p, w // 2 - hw, DESC, w // 2, ASC // 2)
    rect(p, w // 2, DESC, w // 2 + hw, ASC // 2)


def build_arrowdown(p):
    w = WX_DEF; hw = STROKE
    rect(p, w // 2 - hw // 2, DESC, w // 2 + hw // 2, ASC)
    rect(p, w // 2 - hw, ASC // 2, w // 2, ASC)
    rect(p, w // 2, ASC // 2, w // 2 + hw, ASC)


# ── Mono-only builders ────────────────────────────────

def build_fi(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, SB_L + hw, ASC)
    rect(p, SB_L + hw, X_H // 2, SB_L + hw * 2, ASC)
    rect(p, SB_L + hw, X_H // 2, w - SB_R, X_H // 2 + hw)


def build_fl(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, SB_L + hw, ASC)
    rect(p, SB_L + hw, X_H // 2, SB_L + hw * 2, ASC)
    rect(p, SB_L + hw, X_H // 2, w - SB_R, DESC)


def build_fft(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, SB_L + hw, ASC)
    rect(p, SB_L + hw, X_H // 2, SB_L + hw * 2, ASC)
    rect(p, SB_L + hw * 2, X_H // 2, w - SB_R - hw, ASC)
    rect(p, w - SB_R - hw, 0, w - SB_R, ASC)
    rect(p, w - SB_R - hw, X_H // 2, w - SB_R, X_H // 2 + hw)
    w = WX_MONO; hw = STROKE
    rect(p, w // 2 - hw // 2, ASC - hw, w // 2 + hw // 2, ASC)
    rect(p, w // 2 - hw, ASC - hw * 2, w // 2 + hw, ASC - hw)


# ── Builder registry ────────────────────────────────────


def build_Gamma(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, CAP_H - hw, w - SB_R, CAP_H)
    rect(p, SB_L, CAP_H - hw, SB_L + hw, 0)


def build_Delta(p):
    w = WX_DEF; hw = STROKE
    cx = w // 2
    p.moveTo((cx, CAP_H))
    p.lineTo((cx - (w // 2 - SB_L), 0))
    p.lineTo((cx - (w // 2 - SB_L) + hw, 0))
    p.lineTo((cx, CAP_H - hw))
    p.lineTo((cx + (w // 2 - SB_R) - hw, 0))
    p.lineTo((cx + (w // 2 - SB_R), 0))
    p.closePath()


def build_Theta(p):
    w = WX_DEF; hw = STROKE
    cx, cy = w // 2, CAP_H // 2
    r = CAP_H // 2 - hw // 2
    k = r * 0.5523
    p.moveTo((cx + r, cy))
    p.curveTo((cx + r, cy + k), (cx + k, cy + r), (cx, cy + r))
    p.curveTo((cx - k, cy + r), (cx - r, cy + k), (cx - r, cy))
    p.curveTo((cx - r, cy - k), (cx - k, cy - r), (cx, cy - r))
    p.curveTo((cx + k, cy - r), (cx + r, cy - k), (cx + r, cy))
    p.closePath()
    rect(p, cx - r + hw // 2, cy - hw // 2, cx + r - hw // 2, cy + hw // 2)


def build_Lambda(p):
    w = WX_DEF; hw = STROKE
    cx = w // 2
    p.moveTo((cx, CAP_H))
    p.lineTo((SB_L, 0))
    p.lineTo((SB_L + hw, 0))
    p.lineTo((cx, CAP_H - hw))
    p.lineTo((w - SB_R - hw, 0))
    p.lineTo((w - SB_R, 0))
    p.closePath()


def build_Xi(p):
    w = WX_DEF; hw = STROKE
    for frac in (0.85, 0.5, 0.15):
        y = int(CAP_H * frac)
        rect(p, SB_L, y - hw // 2, w - SB_R, y + hw // 2)


def build_Pi(p):
    w = WX_DEF; hw = STROKE
    rect(p, SB_L, 0, SB_L + hw, CAP_H)
    rect(p, w - SB_R - hw, 0, w - SB_R, CAP_H)
    rect(p, SB_L, CAP_H - hw, w - SB_R, CAP_H)


def build_Sigma(p):
    w = WX_DEF; hw = STROKE
    cx = w // 2
    p.moveTo((cx, CAP_H - hw // 2))
    p.lineTo((w - SB_R, CAP_H - hw // 2))
    p.lineTo((cx, CAP_H // 2))
    p.lineTo((SB_L, hw // 2))
    p.lineTo((cx, hw // 2))
    p.lineTo((cx, CAP_H - hw // 2))
    p.closePath()


def build_Phi(p):
    w = WX_DEF; hw = STROKE
    cx, cy = w // 2, CAP_H // 2
    r = CAP_H // 2 - hw // 2
    k = r * 0.5523
    p.moveTo((cx + r, cy))
    p.curveTo((cx + r, cy + k), (cx + k, cy + r), (cx, cy + r))
    p.curveTo((cx - k, cy + r), (cx - r, cy + k), (cx - r, cy))
    p.curveTo((cx - r, cy - k), (cx - k, cy - r), (cx, cy - r))
    p.curveTo((cx + k, cy - r), (cx + r, cy - k), (cx + r, cy))
    p.closePath()
    rect(p, cx - hw // 2, 0, cx + hw // 2, CAP_H)


def build_Psi(p):
    w = WX_DEF; hw = STROKE
    cx = w // 2
    rect(p, cx - hw // 2, 0, cx + hw // 2, CAP_H)
    rect(p, cx - 90, CAP_H // 2, cx + 90, CAP_H // 2 + hw)
    rect(p, SB_L, CAP_H // 2, SB_L + hw, 0)
    rect(p, w - SB_R - hw, CAP_H // 2, w - SB_R, 0)


def build_Omega(p):
    w = WX_DEF; hw = STROKE
    cx = w // 2
    r = CAP_H // 2 - hw // 2
    k = r * 0.5523
    p.moveTo((cx - r, CAP_H))
    p.lineTo((cx - r, CAP_H - hw))
    p.lineTo((cx - r, cy0 := CAP_H // 2))
    p.curveTo((cx - r, CAP_H // 2 + k), (cx - k, r + CAP_H // 2), (cx, r + CAP_H // 2))
    p.curveTo((cx + k, r + CAP_H // 2), (cx + r, CAP_H // 2 + k), (cx + r, CAP_H // 2))
    p.lineTo((cx + r, CAP_H - hw))
    p.lineTo((cx + r, CAP_H))
    p.lineTo((cx + r + hw, CAP_H))
    p.lineTo((cx + r + hw, CAP_H - hw))
    p.lineTo((cx + r, CAP_H - hw * 2))
    p.lineTo((cx - r, CAP_H - hw * 2))
    p.lineTo((cx - r - hw, CAP_H - hw))
    p.lineTo((cx - r - hw, CAP_H))
    p.closePath()



GLYPH_BUILDER_SANS = {
    "A": build_A, "B": build_B, "C": build_C, "D": build_D, "E": build_E,
    "F": build_F, "G": build_G, "H": build_H, "I": build_I, "J": build_J,
    "K": build_K, "L": build_L, "M": build_M, "N": build_N, "O": build_O,
    "P": build_P, "Q": build_Q, "R": build_R, "S": build_S, "T": build_T,
    "U": build_U, "V": build_V, "W": build_W, "X": build_X, "Y": build_Y,
    "Z": build_Z,
    "a": build_a, "b": build_b, "c": build_c, "d": build_d, "e": build_e,
    "f": build_f, "g": build_g, "h": build_h, "i": build_i, "j": build_j,
    "k": build_k, "l": build_l, "m": build_m, "n": build_n, "o": build_o,
    "p": build_p, "q": build_q, "r": build_r, "s": build_s, "t": build_t,
    "u": build_u, "v": build_v, "w": build_w, "x": build_x, "y": build_y,
    "z": build_z,
    "fi": build_fi, "fl": build_fl, "fft": build_fft,
    "zero": build_zero, "one": build_one, "two": build_two, "three": build_three,
    "four": build_four, "five": build_five, "six": build_six, "seven": build_seven,
    "eight": build_eight, "nine": build_nine,
    "period": build_period, "comma": build_comma, "exclam": build_exclam,
    "question": build_question, "semicolon": build_semicolon, "colon": build_colon,
    "underscore": build_underscore,
    "asterisk": build_asterisk, "slash": build_slash, "backslash": build_backslash,
    "bar": build_bar, "parenleft": build_parenleft, "parenright": build_parenright,
    "braceleft": build_braceleft, "braceright": build_braceright,
    "bracketleft": build_bracketleft, "bracketright": build_bracketright,
    "less": build_less, "greater": build_greater,
    "quotesingle": build_quotesingle, "quotedbl": build_quotedbl,
    "at": build_at, "dollar": build_dollar, "percent": build_percent,
    "ampersand": build_ampersand, "pound": build_pound,
    "section": build_section, "degree": build_degree,
    "plus": build_plus, "minus": build_minus, "equal": build_equal,
    "ellipsis": build_ellipsis, "quoteleft": build_quoteleft,
    "quoteright": build_quoteright,
    "quotedblleft": build_quotedblleft, "quotedblright": build_quotedblright,
    "guilsinglleft": build_guilsinglleft, "guilsinglright": build_guilsinglright,
    "emdash": build_emdash, "endash": build_endash,
    "lessequal": build_lessequal, "greaterequal": build_greaterequal,
    "notequal": build_notequal, "multiply": build_multiply,
    "divide": build_divide, "paragraph": build_paragraph,
    "copyright": build_copyright, "registered": build_registered,
    "trademark": build_trademark, "periodcentered": build_periodcentered,
    "arrowleft": build_arrowleft, "arrowright": build_arrowright,
    "arrowup": build_arrowup, "arrowdown": build_arrowdown,
    # Latin Extended-A
    "Amacron": build_A, "amacron": build_a,
    "Aogonek": build_A, "aogonek": build_a,
    "Cacute": build_C, "cacute": build_c,
    "Ccaron": build_C, "ccaron": build_c,
    "Ccedilla": build_C, "ccedilla": build_c,
    "circumflex": build_circumflex,
    "Dcaron": build_D, "dcaron": build_d,
    "Ecaron": build_E, "ecaron": build_e,
    "Edotaccent": build_E, "edotaccent": build_e,
    "Eogonek": build_E, "eogonek": build_e,
    "Gbreve": build_G, "gbreve": build_g,
    "Kcedilla": build_K, "kcedilla": build_k,
    "Lacute": build_L, "lacute": build_l,
    "Lcaron": build_L, "lcaron": build_l,
    "Nacute": build_N, "nacute": build_n,
    "Ncaron": build_N, "ncaron": build_n,
    "Ogonek": build_O, "ogon": build_o,
    "Racute": build_R, "racute": build_r,
    "Rcaron": build_R, "rcaron": build_r,
    "Sacute": build_S, "sacute": build_s,
    "Scaron": build_S, "scaron": build_s,
    "Tcaron": build_T, "tcaron": build_t,
    "Uacute": build_U, "uacute": build_u,
    "Uring": build_U, "uring": build_u,
    "Wacute": build_W, "wacute": build_w,
    "Yacute": build_Y, "yacute": build_y,
    "Zacute": build_Z, "zacute": build_z,
    "Zdotaccent": build_Z, "zdotaccent": build_z,
    "OE": build_O, "oe": build_o,
    "AE": build_A, "ae": build_a,
    "Lslash": build_L, "lslash": build_l,
    "Eth": build_E, "eth": build_e,
    "Thorn": build_T, "thorn": build_t,
    "brokenbar": build_bar,
    # Greek capitals — many reuse Latin builders since the shapes match
    "Alpha": build_A, "Beta": build_B, "Gamma": build_Gamma,
    "Delta": build_Delta, "Epsilon": build_E, "Zeta": build_Z,
    "Eta": build_H, "Theta": build_Theta, "Iota": build_I,
    "Kappa": build_K, "Lambda": build_Lambda, "Mu": build_M,
    "Nu": build_N, "Xi": build_Xi, "Omicron": build_O,
    "Pi": build_Pi, "Rho": build_P, "Sigma": build_Sigma,
    "Tau": build_T, "Upsilon": build_Y, "Phi": build_Phi,
    "Chi": build_X, "Psi": build_Psi, "Omega": build_Omega,
    "zeta": build_z, "theta": build_Theta, "xi": build_Xi, "pi": build_Pi,
    "plusminus": build_plus,
    "onehalf": build_one, "onequarter": build_one, "threequarters": build_one,
    "radical": build_plus,
    "logicalnot": build_bar,
    "micro": build_mu,
    "cent": build_cent,
    "currency": build_dollar,
    "yen": build_yen,
    "sterling": build_pound,
    "florin": build_fi,
    "guillemetleft": build_guilsinglleft,
    "guillemetright": build_guilsinglright,
    "dagger": build_asterisk,
    "daggerdbl": build_asterisk,
    "acute": build_acute,
    "grave": build_grave,
    "tilde": build_tilde,
    "macron": build_macron,
    "dieresis": build_dieresis,
    "ring": build_ring,
    "cedilla": build_cedilla,
    "hungarumlaut": build_hungarumlaut,
    "ogonek": build_ogonek,
    "caron": build_caron,
    "breve": build_breve,
    "dotaccent": build_dotaccent,
    "hookabove": build_hookabove,
    "horn": build_horn,
    "tonos": build_tonos,
    "iota": build_i,
    "upsilon": build_y,
    "epsilon": build_e,
    "alpha": build_a,
    "beta": build_b,
    "gamma": build_g,
    "delta": build_d,
    "eta": build_h,
    "kappa": build_k,
    "lambda": build_l,
    "mu": build_m,
    "nu": build_n,
    "omicron": build_o,
    "rho": build_r,
    "sigma": build_s,
    "tau": build_t,
    "phi": build_p,
    "chi": build_x,
    "psi": build_q,
    "omega": build_o,
    # Bengali
}

GLYPH_BUILDER_MONO = dict(GLYPH_BUILDER_SANS)
GLYPH_BUILDER_MONO.update({
    "backtick": build_backtick,
    "asciitilde": build_tildebar,
    "asciicircum": build_tildebar,
})

# ── Unicode mapping ───────────────────────────────────

GLYPH_UNICODE = {
    "A": 0x0041, "B": 0x0042, "C": 0x0043, "D": 0x0044, "E": 0x0045,
    "F": 0x0046, "G": 0x0047, "H": 0x0048, "I": 0x0049, "J": 0x004A,
    "K": 0x004B, "L": 0x004C, "M": 0x004D, "N": 0x004E, "O": 0x004F,
    "P": 0x0050, "Q": 0x0051, "R": 0x0052, "S": 0x0053, "T": 0x0054,
    "U": 0x0055, "V": 0x0056, "W": 0x0057, "X": 0x0058, "Y": 0x0059,
    "Z": 0x005A,
    "a": 0x0061, "b": 0x0062, "c": 0x0063, "d": 0x0064, "e": 0x0065,
    "f": 0x0066, "g": 0x0067, "h": 0x0068, "i": 0x0069, "j": 0x006A,
    "k": 0x006B, "l": 0x006C, "m": 0x006D, "n": 0x006E, "o": 0x006F,
    "p": 0x0070, "q": 0x0071, "r": 0x0072, "s": 0x0073, "t": 0x0074,
    "u": 0x0075, "v": 0x0076, "w": 0x0077, "x": 0x0078, "y": 0x0079,
    "z": 0x007A,
    "zero": 0x0030, "one": 0x0031, "two": 0x0032, "three": 0x0033,
    "four": 0x0034, "five": 0x0035, "six": 0x0036, "seven": 0x0037,
    "eight": 0x0038, "nine": 0x0039,
    "period": 0x002E, "comma": 0x002C, "exclam": 0x0021,
    "question": 0x003F, "semicolon": 0x003B, "colon": 0x003A,
    "underscore": 0x005F,
    "asterisk": 0x002A, "slash": 0x002F, "backslash": 0x005C,
    "bar": 0x007C, "parenleft": 0x0028, "parenright": 0x0029,
    "braceleft": 0x007B, "braceright": 0x007D,
    "bracketleft": 0x005B, "bracketright": 0x005D,
    "less": 0x003C, "greater": 0x003E,
    "quotesingle": 0x0027, "quotedbl": 0x0022,
    "at": 0x0040, "dollar": 0x0024, "percent": 0x0025,
    "ampersand": 0x0026, "pound": 0x0023,
    "section": 0x00A7, "degree": 0x00B0,
    "plus": 0x002B, "minus": 0x002D, "equal": 0x003D,
    "ellipsis": 0x2026, "quoteleft": 0x2018,
    "quoteright": 0x2019,
    "quotedblleft": 0x201C, "quotedblright": 0x201D,
    "guilsinglleft": 0x2039, "guilsinglright": 0x203A,
    "guillemetleft": 0x00AB, "guillemetright": 0x00BB,
    "dagger": 0x2020, "daggerdbl": 0x2021,
    # Greek lowercase (lowercase-only, matching the Latin lowercase set)
    "alpha": 0x03B1, "beta": 0x03B2, "gamma": 0x03B3, "delta": 0x03B4,
    "epsilon": 0x03B5, "eta": 0x03B7, "iota": 0x03B9, "kappa": 0x03BA,
    "lambda": 0x03BB, "mu": 0x03BC, "nu": 0x03BD, "omicron": 0x03BF,
    "rho": 0x03C1, "sigma": 0x03C3, "tau": 0x03C4, "upsilon": 0x03C5,
    "phi": 0x03C6, "chi": 0x03C7, "psi": 0x03C8, "omega": 0x03C9,
    # Spacing modifier letters. These are standalone spacing glyphs, NOT
    # combining marks — the Latin set bakes accents into precomposed
    # glyphs (Aacute, acircumflex, ...), so no GDEF mark class is needed
    # here. GDEF marks are a Bengali requirement (see BENGALI_SPEC.md §5).
    #
    # grave and ring deliberately do NOT use U+0060 / U+00B0: those
    # codepoints already belong to backtick and degree in this font.
    "acute": 0x00B4, "dieresis": 0x00A8, "macron": 0x00AF,
    "cedilla": 0x00B8, "grave": 0x02CB, "circumflex": 0x02C6,
    "caron": 0x02C7, "breve": 0x02D8, "dotaccent": 0x02D9,
    "ring": 0x02DA, "tilde": 0x02DC, "hungarumlaut": 0x02DD,
    "hookabove": 0x02DE, "horn": 0x02B0, "ogonek": 0x02BF,
    "tonos": 0x0384,
    "emdash": 0x2014, "endash": 0x2013,
    "lessequal": 0x2264, "greaterequal": 0x2265,
    "notequal": 0x2260, "multiply": 0x00D7,
    "divide": 0x00F7, "paragraph": 0x00B6,
    "copyright": 0x00A9, "registered": 0x00AE,
    "trademark": 0x2122, "periodcentered": 0x00B7,
    "arrowleft": 0x2190, "arrowright": 0x2192,
    "arrowup": 0x2191, "arrowdown": 0x2193,
    "backtick": 0x0060, "asciitilde": 0x007E, "asciicircum": 0x005E,
    # Latin Extended-A
    "Amacron": 0x0100, "amacron": 0x0101,
    "Aogonek": 0x0104, "aogonek": 0x0105,
    "Cacute": 0x0106, "cacute": 0x0107,
    "Ccaron": 0x010C, "ccaron": 0x010D,
    "Ccedilla": 0x00C7, "ccedilla": 0x00E7,
    "Dcaron": 0x010E, "dcaron": 0x010F,
    "Ecaron": 0x011A, "ecaron": 0x011B,
    "Edotaccent": 0x0116, "edotaccent": 0x0117,
    "Eogonek": 0x0118, "eogonek": 0x0119,
    "Gbreve": 0x011E, "gbreve": 0x011F,
    "Kcedilla": 0x0136, "kcedilla": 0x0137,
    "Lacute": 0x0139, "lacute": 0x013A,
    "Lcaron": 0x013D, "lcaron": 0x013E,
    "Nacute": 0x0143, "nacute": 0x0144,
    "Ncaron": 0x0147, "ncaron": 0x0148,
    "Ogonek": 0x014E, "ogon": 0x014F,
    "Racute": 0x0154, "racute": 0x0155,
    "Rcaron": 0x0158, "rcaron": 0x0159,
    "Sacute": 0x015A, "sacute": 0x015B,
    "Scaron": 0x0160, "scaron": 0x0161,
    "Tcaron": 0x0164, "tcaron": 0x0165,
    "Uacute": 0x0170, "uacute": 0x0171,
    "Uring": 0x016E, "uring": 0x016F,
    "Wacute": 0x0174, "wacute": 0x0175,
    "Yacute": 0x0176, "yacute": 0x0177,
    "Zacute": 0x0179, "zacute": 0x017A,
    "Zdotaccent": 0x017B, "zdotaccent": 0x017C,
    "OE": 0x0152, "oe": 0x0153,
    "AE": 0x00C6, "ae": 0x00E6,
    "Lslash": 0x0141, "lslash": 0x0142,
    "Eth": 0x00D0, "eth": 0x00F0,
    "Thorn": 0x00DE, "thorn": 0x00FE,
    "brokenbar": 0x00A6,
    # Greek capitals
    "Alpha": 0x0391, "Beta": 0x0392, "Gamma": 0x0393, "Delta": 0x0394,
    "Epsilon": 0x0395, "Zeta": 0x0396, "Eta": 0x0397, "Theta": 0x0398,
    "Iota": 0x0399, "Kappa": 0x039A, "Lambda": 0x039B, "Mu": 0x039C,
    "Nu": 0x039D, "Xi": 0x039E, "Omicron": 0x039F, "Pi": 0x03A0,
    "Rho": 0x03A1, "Sigma": 0x03A3, "Tau": 0x03A4, "Upsilon": 0x03A5,
    "Phi": 0x03A6, "Chi": 0x03A7, "Psi": 0x03A8, "Omega": 0x03A9,
    "zeta": 0x03B6, "theta": 0x03B8, "xi": 0x03BE, "pi": 0x03C0,
    "plusminus": 0x00B1,
    "onehalf": 0x00BD, "onequarter": 0x00BC, "threequarters": 0x00BE,
    "radical": 0x221A,
    "logicalnot": 0x00AC,
    "micro": 0x00B5,
    "cent": 0x00A2,
    "currency": 0x00A4,
    "yen": 0x00A5,
    "sterling": 0x00A3,
    "florin": 0x0192,
    # Bengali (U+0980-U+09FF)
}

# ── Kerning & features ────────────────────────────────

KERN_GROUPS = {
    "uppeA": ["A"],
    "uppeV": ["V", "W", "Y"],
    "uppeH": ["H", "K", "N"],
    "uppeO": ["O"],
    "lowera": ["a"],
    "lowerv": ["v", "w", "y"],
}

KERN_PAIRS = {
    ("uppeA", "uppeV"): -50,
    ("uppeA", "lowerv"): -30,
    ("uppeT", "lowera"): -20,
    ("uppeT", "uppeH"): -30,
    ("lowera", "uppeV"): -20,
    ("lowerv", "uppeA"): -30,
}

FEATURES_SANS = """\
feature liga {
    sub f i by fi;
    sub f l by fl;
    sub f f by fft;
} liga;

feature kern {
    pos A V -50;
    pos A y -30;
    pos T o -20;
    pos T a -20;
    pos T r -10;
    pos T H -30;
    pos V A -40;
    pos W A -40;
    pos Y A -40;
    pos v A -30;
    pos y A -30;
} kern;

feature calt {
    # Contextual alternates
} calt;

feature case {
    # Case-sensitive punctuation
} case;

feature tnum {
    # Tabular numerals
} tnum;

feature pnum {
    # Proportional numerals
} pnum;

feature frac {
    # Fractions
} frac;

feature ordn {
    # Ordinals
} ordn;

feature sups {
    # Superscript
} sups;

feature subs {
    # Subscript
} subs;

feature zero {
    # Zero alternatives
} zero;
"""

FEATURES_MONO = FEATURES_SANS + """\
feature ss01 {
    # Alternate zero
} ss01;

feature ss02 {
    # Alternate one
} ss02;

feature ss03 {
    # Alternate I/l
} ss03;
"""
