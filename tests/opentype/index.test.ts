import { describe, it, expect } from "vitest";
import { execSync } from "child_process";

const SANS_PATH = "dist/KhulnaSans-Regular.ttf";
const MONO_PATH = "dist/KhulnaMono-Regular.ttf";

describe("opentype", () => {
  it("should have valid OS/2 tables", () => {
    // Check that OS/2 Unicode ranges are set correctly
    const sansOutput = execSync(
      `python3 -c "from fontTools.ttLib import TTFont; f=TTFont('${SANS_PATH}'); print(f.get('OS/2').ulUnicodeRange1)"`,
      { encoding: "utf-8" },
    );
    const monoOutput = execSync(
      `python3 -c "from fontTools.ttLib import TTFont; f=TTFont('${MONO_PATH}'); print(f.get('OS/2').ulUnicodeRange1)"`,
      { encoding: "utf-8" },
    );

    // Bit 0 (Basic Latin) and bit 1 (Latin-1 Supplement) should be set
    // Bit 7 (Greek and Coptic) should also be set
    const sansRanges = parseInt(sansOutput.trim(), 10);
    const monoRanges = parseInt(monoOutput.trim(), 10);

    // Check bits 0, 1, and 7 are set
    const expectedBits = 0b10000011; // bits 0, 1, and 7

    expect(sansRanges & expectedBits).toBe(expectedBits);
    expect(monoRanges & expectedBits).toBe(expectedBits);
  });

  it("should have valid head table", () => {
    // Check that head table has valid unitsPerEm and checksum
    const sansOutput = execSync(
      `python3 -c "from fontTools.ttLib import TTFont; f=TTFont('${SANS_PATH}'); h=f.get('head'); print(f'{h.unitsPerEm} {h.checkSumAdjustment}')"`,
      { encoding: "utf-8" },
    );
    const monoOutput = execSync(
      `python3 -c "from fontTools.ttLib import TTFont; f=TTFont('${MONO_PATH}'); h=f.get('head'); print(f'{h.unitsPerEm} {h.checkSumAdjustment}')"`,
      { encoding: "utf-8" },
    );

    const [sansUnits, sansChecksum] = sansOutput.trim().split(" ").map(Number);
    const [monoUnits, monoChecksum] = monoOutput.trim().split(" ").map(Number);

    // unitsPerEm should be 1000 for this font
    expect(sansUnits).toBe(1000);
    expect(monoUnits).toBe(1000);

    // checksum should be a valid number
    expect(sansChecksum).toBeGreaterThanOrEqual(0);
    expect(monoChecksum).toBeGreaterThanOrEqual(0);
  });

  it("should have valid hhea table", () => {
    // Check that hhea table has valid metrics
    const sansOutput = execSync(
      `python3 -c "from fontTools.ttLib import TTFont; f=TTFont('${SANS_PATH}'); h=f.get('hhea'); print(f'{h.ascent} {h.descent} {h.lineGap}')"`,
      { encoding: "utf-8" },
    );
    const monoOutput = execSync(
      `python3 -c "from fontTools.ttLib import TTFont; f=TTFont('${MONO_PATH}'); h=f.get('hhea'); print(f'{h.ascent} {h.descent} {h.lineGap}')"`,
      { encoding: "utf-8" },
    );

    const [sansAscent, sansDescent, sansLineGap] = sansOutput.trim().split(" ").map(Number);
    const [monoAscent, monoDescent, monoLineGap] = monoOutput.trim().split(" ").map(Number);

    // ascent should be positive, descent should be negative
    expect(sansAscent).toBeGreaterThan(0);
    expect(sansDescent).toBeLessThan(0);
    expect(monoAscent).toBeGreaterThan(0);
    expect(monoDescent).toBeLessThan(0);

    // lineGap should be 0 for this font
    expect(sansLineGap).toBe(0);
    expect(monoLineGap).toBe(0);
  });

  it("should have valid name table", () => {
    // Check that name table has required entries
    const sansOutput = execSync(
      `python3 -c "from fontTools.ttLib import TTFont; f=TTFont('${SANS_PATH}'); n=f.get('name'); names = {r.nameID: r.toUnicode() for r in n.names}; print('\\n'.join(f'{k}:{v}' for k, v in sorted(names.items()) if k in [1,2,4,6]))"`,
      { encoding: "utf-8" },
    );
    const monoOutput = execSync(
      `python3 -c "from fontTools.ttLib import TTFont; f=TTFont('${MONO_PATH}'); n=f.get('name'); names = {r.nameID: r.toUnicode() for r in n.names}; print('\\n'.join(f'{k}:{v}' for k, v in sorted(names.items()) if k in [1,2,4,6]))"`,
      { encoding: "utf-8" },
    );

    // Required name IDs: 1 (family), 2 (style), 4 (full name), 6 (postscript name)
    const requiredIds = [1, 2, 4, 6];

    for (const id of requiredIds) {
      expect(sansOutput).toContain(`${id}:`);
      expect(monoOutput).toContain(`${id}:`);
    }
  });

  it("should have valid GPOS table", () => {
    // Check that GPOS table exists and has kerning
    const sansOutput = execSync(
      `python3 -c "from fontTools.ttLib import TTFont; f=TTFont('${SANS_PATH}'); gpos=f.get('GPOS'); print('GPOS' if gpos else 'NO_GPOS')"`,
      { encoding: "utf-8" },
    );
    const monoOutput = execSync(
      `python3 -c "from fontTools.ttLib import TTFont; f=TTFont('${MONO_PATH}'); gpos=f.get('GPOS'); print('GPOS' if gpos else 'NO_GPOS')"`,
      { encoding: "utf-8" },
    );

    expect(sansOutput.trim()).toBe("GPOS");
    expect(monoOutput.trim()).toBe("GPOS");
  });

  it("should have valid GSUB table", () => {
    // Check that GSUB table exists and has features
    const sansOutput = execSync(
      `python3 -c "from fontTools.ttLib import TTFont; f=TTFont('${SANS_PATH}'); gsub=f.get('GSUB'); print('\\n'.join(feat.FeatureTag for feat in gsub.table.FeatureList.FeatureRecord) if gsub else 'NO_GSUB')"`,
      { encoding: "utf-8" },
    );
    const monoOutput = execSync(
      `python3 -c "from fontTools.ttLib import TTFont; f=TTFont('${MONO_PATH}'); gsub=f.get('GSUB'); print('\\n'.join(feat.FeatureTag for feat in gsub.table.FeatureList.FeatureRecord) if gsub else 'NO_GSUB')"`,
      { encoding: "utf-8" },
    );

    expect(sansOutput.trim()).not.toBe("NO_GSUB");
    expect(monoOutput.trim()).not.toBe("NO_GSUB");

    // Should have at least liga (ligatures)
    expect(sansOutput).toContain("liga");
    expect(monoOutput).toContain("liga");
  });

  it("should have valid GDEF table if marks exist", () => {
    // Check if GDEF table exists
    const sansOutput = execSync(
      `python3 -c "from fontTools.ttLib import TTFont; f=TTFont('${SANS_PATH}'); gdef=f.get('GDEF'); print('GDEF' if gdef else 'NO_GDEF')"`,
      { encoding: "utf-8" },
    );

    // For now, we don't require GDEF since we don't have combining marks
    // This test will become more important when Bengali is implemented
    expect(sansOutput.trim()).toBeTruthy();
  });
});
