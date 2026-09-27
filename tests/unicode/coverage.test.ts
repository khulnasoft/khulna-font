import { describe, it, expect } from "vitest";
import { TTFont } from "fontTools";

const SANS_PATH = "fonts/KhulnaSans/build/KhulnaSans-Regular.ttf";
const MONO_PATH = "fonts/KhulnaMono/build/KhulnaMono-Regular.ttf";

function loadFont(path: string): TTFont {
  const font = new TTFont(path);
  return font;
}

describe("Unicode coverage", () => {
  it("Sans should have basic Latin", () => {
    const font = loadFont(SANS_PATH);
    const cmap = font.getBestCmap();
    expect(cmap).toBeDefined();
    expect(cmap?.[0x0041]).toBe("A");
    expect(cmap?.[0x0061]).toBe("a");
    expect(cmap?.[0x0030]).toBe("zero");
  });

  it("Mono should have basic Latin", () => {
    const font = loadFont(MONO_PATH);
    const cmap = font.getBestCmap();
    expect(cmap).toBeDefined();
    expect(cmap?.[0x0041]).toBe("A");
    expect(cmap?.[0x0061]).toBe("a");
  });

  it("Sans should have punctuation", () => {
    const font = loadFont(SANS_PATH);
    const cmap = font.getBestCmap();
    expect(cmap?.[0x002E]).toBe("period");
    expect(cmap?.[0x002C]).toBe("comma");
    expect(cmap?.[0x0021]).toBe("exclam");
    expect(cmap?.[0x003F]).toBe("question");
  });

  it("Sans should have symbols", () => {
    const font = loadFont(SANS_PATH);
    const cmap = font.getBestCmap();
    expect(cmap?.[0x002B]).toBe("plus");
    expect(cmap?.[0x003C]).toBe("less");
    expect(cmap?.[0x003E]).toBe("greater");
    expect(cmap?.[0x002F]).toBe("slash");
  });

  it("Sans should have arrows", () => {
    const font = loadFont(SANS_PATH);
    const cmap = font.getBestCmap();
    expect(cmap?.[0x2190]).toBe("arrowleft");
    expect(cmap?.[0x2192]).toBe("arrowright");
    expect(cmap?.[0x2191]).toBe("arrowup");
    expect(cmap?.[0x2193]).toBe("arrowdown");
  });
});