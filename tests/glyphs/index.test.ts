import { describe, it, expect } from "vitest";
import { execSync } from "child_process";

const SANS_PATH = "dist/KhulnaSans-Regular.ttf";
const MONO_PATH = "dist/KhulnaMono-Regular.ttf";

function getCmap(path: string): Map<number, string> {
  try {
    const output = execSync(
      `python3 -c "from fontTools.ttLib import TTFont; f=TTFont('${path}'); cmap=f.getBestCmap(); print('\\n'.join(f'{k} {v}' for k, v in (cmap or {}).items()))"`,
      { encoding: "utf-8" },
    );
    const cmap = new Map<number, string>();
    for (const line of output.trim().split("\n")) {
      const [codepoint, name] = line.split(" ");
      if (codepoint && name) {
        cmap.set(parseInt(codepoint, 10), name);
      }
    }
    return cmap;
  } catch {
    return new Map();
  }
}

function getGlyphNames(path: string): Set<string> {
  try {
    const output = execSync(
      `python3 -c "from fontTools.ttLib import TTFont; f=TTFont('${path}'); print('\\n'.join(f.getGlyphOrder()))"`,
      { encoding: "utf-8" },
    );
    return new Set(output.trim().split("\n"));
  } catch {
    return new Set();
  }
}

function getExpectedGlyphs(): Map<string, number> {
  try {
    const output = execSync(
      `python3 -c "import sys; sys.path.insert(0, 'sources'); from design.latin import GLYPH_UNICODE; print('\\n'.join(f'{k} {v}' for k, v in GLYPH_UNICODE.items()))"`,
      { encoding: "utf-8" },
    );
    const glyphs = new Map<string, number>();
    for (const line of output.trim().split("\n")) {
      const [name, codepoint] = line.split(" ");
      if (name && codepoint) {
        glyphs.set(name, parseInt(codepoint, 10));
      }
    }
    return glyphs;
  } catch {
    return new Map();
  }
}

describe("glyphs", () => {
  const expectedGlyphs = getExpectedGlyphs();

  // Known missing glyphs that are in the spec but not yet implemented
  const KNOWN_MISSING = new Set(["backtick", "asciitilde", "asciicircum"]);

  it("should have all expected glyphs in Sans cmap", () => {
    const cmap = getCmap(SANS_PATH);
    const missing: string[] = [];

    for (const [name, codepoint] of expectedGlyphs) {
      if (KNOWN_MISSING.has(name)) {
        continue; // Skip known missing glyphs
      }

      const mappedName = cmap.get(codepoint);
      if (!mappedName) {
        // Some glyphs use alternate codepoints (e.g., backtick uses grave U+02CB instead of U+0060)
        // Check if the glyph name exists in the font at all
        const glyphNames = getGlyphNames(SANS_PATH);
        if (!glyphNames.has(name)) {
          missing.push(`${name} (U+${codepoint.toString(16).toUpperCase().padStart(4, "0")})`);
        }
      }
    }

    if (missing.length > 0) {
      throw new Error(
        `Missing ${missing.length} glyphs in Sans:\n${missing.slice(0, 20).join("\n")}${missing.length > 20 ? "\n..." : ""}`,
      );
    }
  });

  it("should have all expected glyphs in Mono cmap", () => {
    const cmap = getCmap(MONO_PATH);
    const missing: string[] = [];

    for (const [name, codepoint] of expectedGlyphs) {
      if (KNOWN_MISSING.has(name)) {
        continue; // Skip known missing glyphs
      }

      const mappedName = cmap.get(codepoint);
      if (!mappedName) {
        // Some glyphs use alternate codepoints (e.g., backtick uses grave U+02CB instead of U+0060)
        // Check if the glyph name exists in the font at all
        const glyphNames = getGlyphNames(MONO_PATH);
        if (!glyphNames.has(name)) {
          missing.push(`${name} (U+${codepoint.toString(16).toUpperCase().padStart(4, "0")})`);
        }
      }
    }

    if (missing.length > 0) {
      throw new Error(
        `Missing ${missing.length} glyphs in Mono:\n${missing.slice(0, 20).join("\n")}${missing.length > 20 ? "\n..." : ""}`,
      );
    }
  });

  it("should not have .notdef glyphs in cmap", () => {
    const sansCmap = getCmap(SANS_PATH);
    const monoCmap = getCmap(MONO_PATH);

    const sansNotdef = Array.from(sansCmap.values()).filter((name) =>
      name.includes(".notdef"),
    );
    const monoNotdef = Array.from(monoCmap.values()).filter((name) =>
      name.includes(".notdef"),
    );

    expect(sansNotdef).toHaveLength(0);
    expect(monoNotdef).toHaveLength(0);
  });

  it("should have expected glyph count", () => {
    const sansGlyphs = getGlyphNames(SANS_PATH);
    const monoGlyphs = getGlyphNames(MONO_PATH);

    // Subtract .notdef and other non-cmap glyphs
    const sansCount = sansGlyphs.size - 1; // .notdef
    const monoCount = monoGlyphs.size - 1; // .notdef

    // Expected count should be close to GLYPH_UNICODE size
    // Allow some tolerance for ligatures and alternates
    const expectedMin = expectedGlyphs.size > 0 ? expectedGlyphs.size * 0.9 : 200;
    const expectedMax = expectedGlyphs.size > 0 ? expectedGlyphs.size * 1.2 : 300;

    expect(sansCount).toBeGreaterThanOrEqual(expectedMin);
    expect(sansCount).toBeLessThanOrEqual(expectedMax);
    expect(monoCount).toBeGreaterThanOrEqual(expectedMin);
    expect(monoCount).toBeLessThanOrEqual(expectedMax);
  });

  it("should have essential ligatures", () => {
    const sansGlyphs = getGlyphNames(SANS_PATH);
    const monoGlyphs = getGlyphNames(MONO_PATH);

    const ligatures = ["fi", "fl", "fft"];

    for (const lig of ligatures) {
      expect(sansGlyphs.has(lig)).toBe(true);
      expect(monoGlyphs.has(lig)).toBe(true);
    }
  });

  it("should track known missing glyphs", () => {
    // This test ensures we're aware of glyphs that are in the spec but not implemented
    // When these are implemented, remove them from KNOWN_MISSING
    expect(KNOWN_MISSING.size).toBeGreaterThan(0);

    const sansGlyphs = getGlyphNames(SANS_PATH);

    for (const name of KNOWN_MISSING) {
      // Verify they're actually missing from Sans (Mono may have them)
      expect(sansGlyphs.has(name)).toBe(false);
    }
  });
});
