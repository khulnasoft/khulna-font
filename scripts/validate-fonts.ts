import { validateFonts } from "../tools/fonttools";

async function main() {
  const results = await validateFonts([
    "fonts/KhulnaSans/build",
    "fonts/KhulnaMono/build",
  ]);

  for (const result of results) {
    if (!result.valid) {
      console.error(`Validation failed for ${result.path}:`, result.errors);
      process.exit(1);
    }
  }

  console.log("All fonts validated successfully.");
}

main().catch((error) => {
  console.error("Validation failed:", error);
  process.exit(1);
});
