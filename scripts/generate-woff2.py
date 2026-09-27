import sys
from pathlib import Path
from fontTools.ttLib import TTFont

# Compress every TTF under dist/, including dist/var/, so the variable font
# WOFF2 never goes stale relative to its TTF.
ttfs = sorted(Path("dist").rglob("*.ttf"))
if not ttfs:
    sys.exit("No TTFs found under dist/")

for ttf in ttfs:
    woff2 = ttf.with_suffix(".woff2")
    font = TTFont(ttf)
    font.flavor = "woff2"
    font.save(woff2)
    font.close()
    print(f"{ttf}: TTF={ttf.stat().st_size} WOFF2={woff2.stat().st_size}")
