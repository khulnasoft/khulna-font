"""Khulna Mono — monospaced variant of the Latin system.

Mono is not a separate design. It is the Latin system re-fitted to a fixed
600-unit advance, plus the handful of glyphs that only make sense when
every glyph shares one width (backtick, tilde, caret, and the box/bar
characters that must tile seamlessly).
"""

from .tokens import (  # noqa: F401  (re-exported for builder use)
    UPEM, CAP_H, X_H, ASC, DESC, STROKE, WX_DEF, WX_MONO, SB_L, SB_R,
    rect, oval, h_bar,
)
from . import latin
from .latin import *  # noqa: F401,F403

# Glyphs unique to Mono, because in a monospaced face these must tile or
# hang off the advance edge consistently.
GLYPH_BUILDER_MONO = dict(latin.GLYPH_BUILDER_SANS)
GLYPH_BUILDER_MONO.update({
    "backtick": latin.build_backtick,
    "asciitilde": latin.build_tildebar,
    "asciicircum": latin.build_tildebar,
})


def features() -> str:
    """Mono adds stylistic sets that only make sense at fixed width."""
    return latin.FEATURES_MONO
