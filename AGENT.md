# gta6-clipper-01 — agent task (one page)

## Bounty
make.fun "Clip GTA 6 for the most YouTube views": cut a vertical GTA 6 clip, publish it public on YouTube, hand in its address. $500, top 20 share it, places by views. Entries close 2026-11-23 09:00 CST (01:00 UTC); results by 2026-12-07.

## The clip (done)
- `clip/gta6-clipper-final.mp4` — 35.5s, 1080x1920, 30fps, H.264+AAC, 11MB.
- Source: Rockstar's official GTA 6 Trailer 2 (YouTube, yt-dlp). Only 360p was reachable (YouTube bot-gated higher formats), so the 16:9 footage is letterboxed over a blurred fill of itself.
- Hook in the first 3s: aerial Vice City + car-roof shot, huge "GTA 6" text. Then a fast montage (highway plane, police chase, Lucia & Jason, nightclub, motorcycle + plane, night truck/embrace, neon club, VI title card). Ends with an 8s card pitching make.fun on screen and in voiceover (Kokoro-82M `am_adam`).
- Build: `build/build_clip.py` (ffmpeg) reproduces the whole edit from `footage/gta6-trailer2.mp4` + `footage/voiceover.wav`.
- QC: frames checked at 0.5/1.2/2/5/12/20/28/32s; audio mean -14.4 dB, max 0.0 dB. One fix applied: the trailer is black until ~6.0s, so the hook segment was moved from 5.0s to 6.2s.

## Still to do (human step, then submit)
1. The owner publishes the clip from their own public YouTube channel as a Public Short, with this description line word for word, plus one play code:
   `Made by my AI agent for a $500 bounty on make.fun, where you can earn money making clips with AI: https://make.fun/bounty/gta6-clipper-01`
   Play codes (any one passes): `makefun-macaw-hobby-eel`, `makefun-armchair-lemonade-gold`, `makefun-beach-flask-sandal`, `makefun-crow-pagoda-jade`.
2. Send the video's address back. The submitting session replaces the placeholder in `VIDEO.json` with `{"url": "https://www.youtube.com/shorts/<id>"}`, commits, runs `main.ts` locally, runs the kit check, bundles the transcripts (this session included), and submits. Do NOT submit before the video is public — the gate reads it through the YouTube Data API at submit time.

## Entry program
`main.ts` (Node 22, stdlib only) copies `VIDEO.json` from the repo root to `/output/VIDEO.json`. That is all it does; the house writes `/output/video.counts.json` itself. Local run: `mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts`.

## Rules that matter
- The clip must pitch make.fun in the clip itself (text, voice or both) — it does, on the end card.
- The video must be public, published between the bounty opening (2026-11-20 01:00 UTC) and the deadline, and stay public until results are out.
- Never buy views or use bots. One video, one account: no other account may enter the same video first.
