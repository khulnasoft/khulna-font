#!/usr/bin/env python3
"""Visual regression test generator.

Renders specimen images for every release and compares against
the previous release to detect silent metric changes.
"""

import subprocess
from pathlib import Path

SNAPSHOTS = Path("tests/snapshots")
FONTS = {
    "sans-regular": "dist/KhulnaSans-Regular.ttf",
    "mono-regular": "dist/KhulnaMono-Regular.ttf",
}

SPECIMEN_TEXT = {
    "latin": "The quick brown fox jumps over the lazy dog",
    "numerals": "0123456789 0O 1lI 5S 2Z",
    "code": "const agent = await createAgent();",
    "punctuation": "! \" # $ % & ' ( ) * + , - . / : ; < = > ? @",
}


def render_specimen(name: str, font_path: str, text: str, size: int = 48):
    """Render a specimen image using fontTools + PIL."""
    from PIL import Image, ImageDraw, ImageFont

    font = ImageFont.truetype(font_path, size)
    lines = text.split("\n")
    line_height = size + 8
    img = Image.new("RGB", (800, len(lines) * line_height + 40), "white")
    draw = ImageDraw.Draw(img)

    for i, line in enumerate(lines):
        draw.text((20, 20 + i * line_height), line, font=font, fill="black")

    out_path = SNAPSHOTS / f"{name}.png"
    img.save(out_path)
    print(f"  Rendered {out_path}")
    return out_path


def compare_snapshots(baseline: Path, current: Path) -> bool:
    """Compare two snapshot images pixel-by-pixel."""
    from PIL import Image

    if not baseline.exists():
        print(f"  No baseline: {baseline}")
        return True

    img1 = Image.open(baseline)
    img2 = Image.open(current)

    if img1.size != img2.size:
        print(f"  Size mismatch: {img1.size} vs {img2.size}")
        return False

    pixels1 = list(img1.getdata())
    pixels2 = list(img2.getdata())
    diff = sum(1 for a, b in zip(pixels1, pixels2) if a != b)
    total = len(pixels1)
    ratio = diff / total

    print(f"  Diff: {diff}/{total} ({ratio:.2%})")
    return ratio < 0.01  # 1% threshold


def main():
    SNAPSHOTS.mkdir(parents=True, exist_ok=True)

    for name, font_path in FONTS.items():
        if not Path(font_path).exists():
            print(f"  SKIP {name}: font not found")
            continue

        for spec_name, text in SPECIMEN_TEXT.items():
            out_path = render_specimen(f"{name}-{spec_name}", font_path, text)

            baseline = SNAPSHOTS / f"baseline-{name}-{spec_name}.png"
            if baseline.exists():
                match = compare_snapshots(baseline, out_path)
                if not match:
                    print(f"  REGRESSION DETECTED: {name}-{spec_name}")

    print("Visual regression check complete.")


if __name__ == "__main__":
    main()