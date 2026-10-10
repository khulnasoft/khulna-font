"""Khulna FontBakery profile — real check IDs.

Replaces the previous profile.yaml, which used entirely fabricated check IDs
(e.g. com.google.fonts/check/001) that do not exist in fontbakery. Every ID
below is a real, registered fontbakery check.

Usage:
    fontbakery check-profile fontbakery/khulna_profile.py dist/KhulnaSans-Regular.ttf
"""

PROFILE = {
    "include_profiles": ["opentype"],
    "sections": {
        "Metadata": [
            "opentype/name/postscript_name_consistency",
            "opentype/vendor_id",
            "googlefonts/vendor_id",
            "googlefonts/name/license",
            "googlefonts/name/license_url",
            "googlefonts/family/has_license",
            "googlefonts/license/OFL_copyright",
            "googlefonts/license/OFL_body_text",
            "name/no_copyright_on_description",
        ],
        "Glyph Coverage": [
            "notofonts/cmap/alien_codepoints",
            "notofonts/cmap/unexpected_subtables",
            "cmap/format_12",
            "base_has_width",
            "case_mapping",
        ],
        "Metrics": [
            "family/win_ascent_and_descent",
            "googlefonts/use_typo_metrics",
            "caps_vertically_centered",
            "typoascender_exceeds_Agrave",
        ],
        "OpenType": [
            "opentype/gdef_mark_chars",
            "opentype/gdef_non_mark_chars",
            "opentype/gdef_spacing_marks",
            "opentype/layout_valid_script_tags",
            "gpos_kerning_info",
            "gpos7",
        ],
        "Shaping": [
            "shaping/collides",
            "shaping/forbidden",
            "shaping/regression",
        ],
        "Outline Quality": [
            "outline_alignment_miss",
            "outline_colinear_vectors",
            "outline_direction",
            "outline_jaggy_segments",
            "outline_semi_vertical",
            "outline_short_segments",
        ],
    },
}
