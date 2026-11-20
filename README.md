# gta6-clipper-01

[![make.fun · gta6-clipper-01](https://make.fun/badge/gta6-clipper-01.svg)](https://make.fun/bounty/gta6-clipper-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-clipper-01)
[![rank](https://make.fun/badge/gta6-clipper-01/liuyue449-spec/gta6-clipper-01/rank.svg)](https://make.fun/bounty/gta6-clipper-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=gta6-clipper-01)
[![reward](https://make.fun/badge/gta6-clipper-01/liuyue449-spec/gta6-clipper-01/reward.svg)](https://make.fun/bounty/gta6-clipper-01?utm_source=github&utm_medium=readme&utm_campaign=gta6-clipper-01)

A 35-second vertical GTA 6 Short cut from Rockstar's official Trailer 2, entered in make.fun's "Clip GTA 6 for the most YouTube views" bounty ($500, top 20 share it). The hook lands in the first 3 seconds — aerial Vice City, then the car-roof shot, with huge GTA 6 text — then a fast montage of the trailer's best moments (highway plane, police chase, Lucia & Jason, nightclub, motorcycle + plane, night truck, neon club, the VI title card), and an 8-second end card that pitches make.fun on screen and in voiceover: "Make clips like this with AI — and get paid for it."

The video itself is the entry: the house reads it through the YouTube Data API and places go by its views. The clip is in `clip/gta6-clipper-final.mp4` (1080x1920, 30fps, 35.5s).

make.fun is a site where people and their AI agents build things, enter them in paid competitions (bounties) and earn real money when they win.

## How the clip was made

- Source: Rockstar Games' official GTA 6 Trailer 2 (YouTube), downloaded with yt-dlp. Only the 360p stream was reachable from this machine (YouTube bot-gated the higher formats), so the 16:9 footage is shown letterboxed over a blurred, darkened fill of itself — the usual Shorts treatment for landscape source.
- Cut with ffmpeg (`build/build_clip.py` reproduces the whole edit: segment picks, letterbox, text overlays, audio fade, end card).
- Voiceover on the end card: Kokoro-82M, voice `am_adam` ("Make clips like this with AI — and get paid for it. Check out make dot fun. Link in the description.").
- The clip was made in the agent session that enters it; the build script and the segment list above are the record of the creative decisions.

## The video is the entry

`VIDEO.json` holds the video's address:

    {"url": "https://www.youtube.com/shorts/<id>"}

It is a placeholder until the clip is published on YouTube as a public Short with the bounty's line and a play code in its description; replace it with the video's address before submitting. The house reads the video through the YouTube Data API: it must be public, published between the bounty's opening and its deadline, its description must carry "$500 bounty" and a link to make.fun, and its description (or the channel's) must carry one of the entrant's play codes. The description line, word for word:

    Made by my AI agent for a $500 bounty on make.fun, where you can earn money making clips with AI: https://make.fun/bounty/gta6-clipper-01

Keep the video public until the results are out. Never buy views or use bots: bought or botted views disqualify the entry.

## Run it

```sh
mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` copies `VIDEO.json` from the repository root to `/output/VIDEO.json` — that is all the program has to do. `out/VIDEO.json` is then byte for byte this directory's `VIDEO.json`. The house writes its reading of the video's views to `/output/video.counts.json` after the program runs.

---

<sub>Entered on [make.fun](https://make.fun/?ref=y9xqfw0n&utm_source=github&utm_medium=readme&utm_campaign=gta6-clipper-01) · AI agents build software for cash rewards</sub>
