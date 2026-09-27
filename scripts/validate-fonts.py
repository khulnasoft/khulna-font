from fontTools.ttLib import TTFont
from pathlib import Path
import sys

fonts = [
    "dist/KhulnaSans-Regular.ttf",
    "dist/KhulnaMono-Regular.ttf",
]

errors = []
for path in fonts:
    if not Path(path).exists():
        errors.append(f"Missing: {path}")
        continue
    try:
        font = TTFont(path)
        name_table = font["name"]
        family = name_table.getName(1, 3, 1, 1033)
        if not family:
            errors.append(f"No family name in {path}")
        print(f"OK: {path} family={family}")
        font.close()
    except Exception as e:
        errors.append(f"Error reading {path}: {e}")

if errors:
    for e in errors:
        print(f"ERROR: {e}")
    sys.exit(1)

print("All fonts validated.")