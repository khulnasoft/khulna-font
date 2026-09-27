"""Khulna design source — the canonical design system.

The generated UFO is a build artifact. The modules here are the source of
truth:

    tokens.py   shared metrics and drawing primitives
    latin.py    Latin glyph construction, kerning, OpenType features
    mono.py     monospaced re-fit of the Latin system
    bengali.py  Bengali inventory + shaping spec (not yet implemented)

BENGALI_SPEC.md holds the Bengali design specification.
"""

from . import tokens, latin, mono, bengali  # noqa: F401

__all__ = ["tokens", "latin", "mono", "bengali"]
