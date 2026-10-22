import { generateSpecimen } from "../tools/fonttools";

async function main() {
  await generateSpecimen("specimens", "fonts/KhulnaSans/build");
  console.log("Specimen generation complete.");
}

main().catch((error) => {
  console.error("Specimen generation failed:", error);
  process.exit(1);
});
