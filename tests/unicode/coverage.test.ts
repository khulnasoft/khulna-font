import { describe, it, expect } from "vitest";
import { execSync } from "child_process";

const SANS_PATH = "dist/KhulnaSans-Regular.ttf";
const MONO_PATH = "dist/KhulnaMono-Regular.ttf";

function getCmap(path: string, codepoint: number): string | null {
  try {
    const output = execSync(
      `python3 -c "from fontTools.ttLib import TTFont; f=TTFont('${path}'); cmap=f.getBestCmap(); print(cmap.get(${codepoint}) if cmap else '')"`,
      { encoding: "utf-8" },
    );
    return output.trim() || null;
  } catch {
    return null;
  }
}

describe("Unicode coverage", () => {
  it("Sans should have basic Latin", () => {
    expect(getCmap(SANS_PATH, 0x0041)).toBe("A");
    expect(getCmap(SANS_PATH, 0x0061)).toBe("a");
    expect(getCmap(SANS_PATH, 0x0030)).toBe("zero");
  });

  it("Mono should have basic Latin", () => {
    expect(getCmap(MONO_PATH, 0x0041)).toBe("A");
    expect(getCmap(MONO_PATH, 0x0061)).toBe("a");
  });

  it("Sans should have punctuation", () => {
    expect(getCmap(SANS_PATH, 0x002e)).toBe("period");
    expect(getCmap(SANS_PATH, 0x002c)).toBe("comma");
    expect(getCmap(SANS_PATH, 0x0021)).toBe("exclam");
    expect(getCmap(SANS_PATH, 0x003f)).toBe("question");
  });

  it("Sans should have symbols", () => {
    expect(getCmap(SANS_PATH, 0x002b)).toBe("plus");
    expect(getCmap(SANS_PATH, 0x003c)).toBe("less");
    expect(getCmap(SANS_PATH, 0x003e)).toBe("greater");
    expect(getCmap(SANS_PATH, 0x002f)).toBe("slash");
  });

  it("Sans should have arrows", () => {
    expect(getCmap(SANS_PATH, 0x2190)).toBe("arrowleft");
    expect(getCmap(SANS_PATH, 0x2192)).toBe("arrowright");
    expect(getCmap(SANS_PATH, 0x2191)).toBe("arrowup");
    expect(getCmap(SANS_PATH, 0x2193)).toBe("arrowdown");
  });
});
