#!/usr/bin/env python3
"""Build the gta6-clipper-01 Short from Rockstar's official GTA 6 Trailer 2.

Source: footage/gta6-trailer2.mp4 (official Trailer 2, 640x360, downloaded
from Rockstar Games' YouTube channel with yt-dlp, android client).
Voiceover: footage/voiceover.wav (Kokoro-82M, am_adam).

Layout: 1080x1920 vertical. The 16:9 trailer footage is shown letterboxed
(1080x608) over a blurred, darkened fill of itself -- the standard Shorts
treatment for landscape source, and it keeps the visible picture at a
1.7x upscale instead of a 5x vertical-crop upscale.
Hook in the first 3 seconds: aerial Vice City, then the car-roof shot,
with huge GTA 6 text. Montage of the trailer's best moments, then an
8-second end card that pitches make.fun on screen and in voiceover.
"""
import subprocess
import sys

SRC = "footage/gta6-trailer2.mp4"
VO = "footage/voiceover.wav"
OUT = "clip/gta6-clipper-final.mp4"
FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

# (source start seconds, duration, on-screen text, fontsize)
SEGMENTS = [
    (6.2, 1.5, "GTA 6", 150),  # aerial Vice City; the trailer is black until ~6.0s
    (110.0, 2.0, "VICE CITY IS BACK", 64),
    (35.0, 3.0, "MAY 26, 2026", 72),
    (45.0, 3.0, "", 0),
    (65.0, 3.0, "LUCIA & JASON", 64),
    (90.0, 3.0, "", 0),
    (140.0, 3.0, "", 0),
    (145.0, 3.0, "", 0),
    (125.0, 3.0, "", 0),
    (160.0, 3.0, "", 0),
]
ENDCARD = 8.0

def dt(text, fontsize, y, color="white"):
    return (
        f"drawtext=fontfile={FONT}:text='{text}':fontsize={fontsize}:"
        f"fontcolor={color}:box=1:boxcolor=black@0.55:boxborderw=24:"
        f"x=(w-text_w)/2:y={y}"
    )

parts = []
vlabels, alabels = [], []
for i, (ss, dur, text, fs) in enumerate(SEGMENTS):
    parts.append(
        f"[0:v]trim=start={ss}:duration={dur},setpts=PTS-STARTPTS,"
        f"fps=30,split=2[bg{i}][fg{i}];"
        f"[bg{i}]scale=1080:1920:force_original_aspect_ratio=increase,"
        f"crop=1080:1920,gblur=sigma=30,eq=brightness=-0.18[bg{i}f];"
        f"[fg{i}]scale=1080:608[fg{i}f];"
        f"[bg{i}f][fg{i}f]overlay=(W-w)/2:(H-h)/2"
        + (f",{dt(text, fs, 880)}" if text else "")
        + f",format=yuv420p,setsar=1[v{i}];"
        f"[0:a]atrim=start={ss}:duration={dur},asetpts=PTS-STARTPTS[a{i}]"
    )
    vlabels.append(f"[v{i}]")
    alabels.append(f"[a{i}]")
n = len(SEGMENTS)
interleaved = "".join(f"[v{i}][a{i}]" for i in range(n))
parts.append(
    interleaved +
    f"concat=n={n}:v=1:a=1[mv][ma]"
)
# End card: dark card, pink make.fun pitch, voiceover delayed 0.6s.
parts.append(
    f"color=c=0x0d0d17:s=1080x1920:r=30:d={ENDCARD},"
    f"{dt('MAKE CLIPS LIKE THIS', 72, 600)},"
    f"{dt('WITH AI - AND GET PAID', 72, 710, '0xFF71CE')},"
    f"{dt('make.fun', 170, 880, '0xFF71CE')},"
    f"{dt('make.fun/bounty/gta6-clipper-01', 40, 1140)},"
    f"{dt('$500 bounty - link in description', 40, 1220)},"
    f"format=yuv420p,setsar=1[ev];"
    f"[1:a]adelay=600|600,apad=whole_dur={ENDCARD},afade=t=out:st={ENDCARD-0.6}:d=0.6[ea]"
)
# Fade the trailer audio out under the last second of the montage.
parts.append("[ma]afade=t=out:st=26.5:d=1[maf]")
parts.append("[mv][maf][ev][ea]concat=n=2:v=1:a=1[outv][outa]")

fc = ";".join(parts)
cmd = [
    "ffmpeg", "-y", "-v", "error", "-i", SRC, "-i", VO,
    "-filter_complex", fc,
    "-map", "[outv]", "-map", "[outa]",
    "-c:v", "libx264", "-preset", "medium", "-crf", "20",
    "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart",
    OUT,
]
print(" ".join(cmd)[:400], "...")
r = subprocess.run(cmd)
sys.exit(r.returncode)
