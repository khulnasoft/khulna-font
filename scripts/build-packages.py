#!/usr/bin/env python3
"""Package generator — copies built fonts from dist/ into npm packages.

This ensures packages are always derived from dist/, never hand-copied.
"""

import shutil
from pathlib import Path

DIST = Path("dist")
VAR_DIST = Path("dist/var")
PACKAGES = {
    "packages/khulna/fonts": [
        "KhulnaSans-VF.woff2",
        "KhulnaMono-Regular.woff2",
    ],
    "packages/khulna-sans/fonts": [
        "KhulnaSans-VF.woff2",
        "KhulnaSans-Regular.woff2",
    ],
    "packages/khulna-mono/fonts": [
        "KhulnaMono-Regular.woff2",
    ],
}

CSS_TEMPLATE = """\
@font-face {{
  font-family: "{family}";
  src: url("../fonts/{filename}") format("woff2");
  font-style: normal;
  font-weight: {weight};
  font-display: swap;
}}

:root {{
  --font-{css_var}: "{family}";
}}

.khulna-{css_var} {{
  font-family: var(--font-{css_var});
}}
"""


def generate_css(pkg_root, family, filename, weight, css_var):
    css_dir = Path(pkg_root) / "css"
    css_dir.mkdir(parents=True, exist_ok=True)
    css_path = css_dir / "index.css"
    css_path.write_text(CSS_TEMPLATE.format(
        family=family, filename=filename, weight=weight, css_var=css_var,
    ))
    print(f"  Wrote {css_path}")


def main():
    for pkg_dir, files in PACKAGES.items():
        pkg_path = Path(pkg_dir)
        font_dir = pkg_path / "fonts"
        font_dir.mkdir(parents=True, exist_ok=True)

        for filename in files:
            src = DIST / filename
            if not src.exists():
                src = VAR_DIST / filename
            if not src.exists():
                print(f"  MISSING: {filename}")
                continue
            dst = font_dir / filename
            shutil.copy2(src, dst)
            print(f"  Copied {filename} -> {dst}")

        pkg_root = str(pkg_path.parent) if str(pkg_path).endswith("/fonts") else pkg_dir
        if "khulna-sans" in pkg_dir:
            generate_css(pkg_root, "Khulna Sans", "KhulnaSans-Regular.woff2", "100 900", "sans")
        elif "khulna-mono" in pkg_dir:
            generate_css(pkg_root, "Khulna Mono", "KhulnaMono-Regular.woff2", "100 900", "mono")
        elif pkg_dir.endswith("khulna"):
            generate_css(pkg_root, "Khulna Sans", "KhulnaSans-Regular.woff2", "100 900", "sans")
            generate_css(pkg_root, "Khulna Mono", "KhulnaMono-Regular.woff2", "100 900", "mono")

    print("Package generation complete.")


if __name__ == "__main__":
    main()