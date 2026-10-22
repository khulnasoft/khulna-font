import { generateCss } from "../tools/fonttools";

async function main() {
  await generateCss("packages/khulna-sans/css", "fonts/KhulnaSans/build");
  await generateCss("packages/khulna-mono/css", "fonts/KhulnaMono/build");
  console.log("CSS generation complete.");
}

main().catch((error) => {
  console.error("CSS build failed:", error);
  process.exit(1);
});
