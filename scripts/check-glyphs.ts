import { checkGlyphCoverage } from "../tools/fonttools";

async function main() {
  const results = await checkGlyphCoverage([
    "fonts/KhulnaSans/build",
    "fonts/KhulnaMono/build",
  ]);

  for (const result of results) {
    console.log(`${result.path}: ${result.coverage}% coverage`);
    if (result.missing.length > 0) {
      console.log(`  Missing: ${result.missing.join(", ")}`);
    }
  }
}

main().catch((error) => {
  console.error("Glyph check failed:", error);
  process.exit(1);
});