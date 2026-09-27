import { publishRelease } from "../tools/fonttools";

async function main() {
  await publishRelease();
  console.log("Release complete.");
}

main().catch((error) => {
  console.error("Release failed:", error);
  process.exit(1);
});