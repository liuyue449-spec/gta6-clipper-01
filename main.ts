// gta6-clipper-01 entry (Node 22, standard library only).
//
// The entry is the video, not this program: the house reads the video's
// views from YouTube through VIDEO.json. All this program does is hand
// VIDEO.json over to the grader, copying it from the repository root
// (MAKEFUN_BOT_DIR, /bot in the grader) to the output directory
// (MAKEFUN_OUTPUT_DIR, /output in the grader), where the gate reads it.
//
// VIDEO.json holds {"url": "https://www.youtube.com/shorts/<id>"}.
// The address is a placeholder until the clip is published on YouTube
// as a public Short; replace it with the real address before submitting.
// A placeholder, a private video or an unlisted one is refused (valid 0).
// Nothing this program writes about the video is scored: after it runs,
// the house overwrites /output/video.counts.json with its own reading
// of the video's views.
//
// Run it locally the same way the grader does:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
// out/VIDEO.json is then byte for byte this directory's VIDEO.json.

import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

const source = join(botDir, "VIDEO.json");
const target = join(outputDir, "VIDEO.json");

// Refuse to hand over anything that is not a JSON object with a url
// string, so a broken VIDEO.json fails loudly here instead of silently
// passing the gate a file it cannot read.
let parsed: unknown;
try {
  parsed = JSON.parse(readFileSync(source, "utf8"));
} catch (err) {
  console.error(`VIDEO.json could not be read as JSON: ${(err as Error).message}`);
  process.exit(1);
}
if (
  typeof parsed !== "object" ||
  parsed === null ||
  typeof (parsed as { url?: unknown }).url !== "string"
) {
  console.error('VIDEO.json must be a JSON object with a "url" string.');
  process.exit(1);
}

mkdirSync(outputDir, { recursive: true });
try {
  copyFileSync(source, target);
} catch (err) {
  console.error(`VIDEO.json could not be copied to ${outputDir}: ${(err as Error).message}`);
  process.exit(1);
}
console.log(`VIDEO.json copied to ${target}: ${(parsed as { url: string }).url}`);
