import { describe, it, expect } from "vitest";
import { execSync } from "child_process";

const SANS_TTF = "dist/KhulnaSans-Regular.ttf";
const MONO_TTF = "dist/KhulnaMono-Regular.ttf";

describe("Font metadata", () => {
  it("Sans should have correct family name", () => {
    const output = execSync(
      `python3 -c "from fontTools.ttLib import TTFont; f=TTFont('${SANS_TTF}'); print(f['name'].getName(1,3,1,1033))"`,
      { encoding: "utf-8" }
    );
    expect(output.trim()).toBe("Khulna Sans");
  });

  it("Mono should have correct family name", () => {
    const output = execSync(
      `python3 -c "from fontTools.ttLib import TTFont; f=TTFont('${MONO_TTF}'); print(f['name'].getName(1,3,1,1033))"`,
      { encoding: "utf-8" }
    );
    expect(output.trim()).toBe("Khulna Mono");
  });

  it("Sans should have version", () => {
    const output = execSync(
      `python3 -c "from fontTools.ttLib import TTFont; f=TTFont('${SANS_TTF}'); print(f['name'].getName(5,3,1,1033))"`,
      { encoding: "utf-8" }
    );
    expect(output.trim()).toBeTruthy();
  });
});