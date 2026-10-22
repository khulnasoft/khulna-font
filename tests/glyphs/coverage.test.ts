import { describe, it, expect } from "vitest";
import * as fs from "fs";

describe("Font files", () => {
  it("Sans TTF should exist", () => {
    expect(fs.existsSync("dist/KhulnaSans-Regular.ttf")).toBe(true);
  });

  it("Mono TTF should exist", () => {
    expect(fs.existsSync("dist/KhulnaMono-Regular.ttf")).toBe(true);
  });

  it("Sans WOFF2 should exist", () => {
    expect(fs.existsSync("dist/KhulnaSans-Regular.woff2")).toBe(true);
  });

  it("Mono WOFF2 should exist", () => {
    expect(fs.existsSync("dist/KhulnaMono-Regular.woff2")).toBe(true);
  });

  it("Sans TTF should be non-empty", () => {
    const stat = fs.statSync("dist/KhulnaSans-Regular.ttf");
    expect(stat.size).toBeGreaterThan(1000);
  });

  it("Mono TTF should be non-empty", () => {
    const stat = fs.statSync("dist/KhulnaMono-Regular.ttf");
    expect(stat.size).toBeGreaterThan(1000);
  });
});

describe("Build pipeline", () => {
  it("UFO sources should exist", () => {
    expect(
      fs.existsSync("fonts/KhulnaSans/sources/KhulnaSans-Regular.ufo"),
    ).toBe(true);
    expect(
      fs.existsSync("fonts/KhulnaMono/sources/KhulnaMono-Regular.ufo"),
    ).toBe(true);
  });

  it("UFO should have fontinfo.plist", () => {
    expect(
      fs.existsSync(
        "fonts/KhulnaSans/sources/KhulnaSans-Regular.ufo/fontinfo.plist",
      ),
    ).toBe(true);
    expect(
      fs.existsSync(
        "fonts/KhulnaMono/sources/KhulnaMono-Regular.ufo/fontinfo.plist",
      ),
    ).toBe(true);
  });

  it("UFO should have glyphs directory", () => {
    const sansGlyphs = fs.readdirSync(
      "fonts/KhulnaSans/sources/KhulnaSans-Regular.ufo/glyphs",
    );
    const monoGlyphs = fs.readdirSync(
      "fonts/KhulnaMono/sources/KhulnaMono-Regular.ufo/glyphs",
    );
    expect(sansGlyphs.length).toBeGreaterThan(100);
    expect(monoGlyphs.length).toBeGreaterThan(100);
  });
});
