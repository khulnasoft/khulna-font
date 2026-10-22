import { buildVariableFont } from "../tools/fonttools";
import { generateWoff2 } from "../tools/fonttools";

async function main() {
  console.log("Building Khulna Sans...");
  await buildVariableFont("fonts/KhulnaSans/sources", "fonts/KhulnaSans/build");
  await generateWoff2("fonts/KhulnaSans/build", "fonts/KhulnaSans/build");

  console.log("Building Khulna Mono...");
  await buildVariableFont("fonts/KhulnaMono/sources", "fonts/KhulnaMono/build");
  await generateWoff2("fonts/KhulnaMono/build", "fonts/KhulnaMono/build");

  console.log("Build complete.");
}

main().catch((error) => {
  console.error("Build failed:", error);
  process.exit(1);
});
