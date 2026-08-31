"""Script 06 "The Honest Math" — 12s, 9:16, typography only, silent.

No footage, no generator. Four cumulative states on paper tone, hard cuts.
ffmpeg on this Mac is built WITHOUT drawtext, so type is rendered in PIL and
ffmpeg only holds the stills — the same split compose.py already uses.

Colors are compose.py's: CREAM ground, COPPER as rule only. Copper is never
body text here — it is 4.5:1-failing on cream at these sizes. Ink is the
doctrine strap color #0f0f23.

Placeholders [Mon/Thu] and [X] render LITERALLY. Do not fill them in code;
the slot count comes from Nate's count, not from a script.
"""
import os
import subprocess

from PIL import Image, ImageDraw, ImageFont

OUT = os.path.dirname(os.path.abspath(__file__))
W, H = 1080, 1920
CREAM = (244, 239, 230)
COPPER = (232, 176, 112)
INK = (15, 15, 35)          # doctrine strap #0f0f23
MARGIN = 96
FPS = 30

BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
REG = "/System/Library/Fonts/Supplemental/Arial.ttf"
if not os.path.exists(REG):
    REG = "/Library/Fonts/Arial.ttf"
for f in (BOLD, REG):
    assert os.path.exists(f), "missing font: " + f

# (text, font path, size, seconds this state holds) — states are CUMULATIVE
LINES = [
    ("$695.", BOLD, 190),
    ("100% credited toward any work.", REG, 58),
    ("Valid 12 months. Written scope.\nReserved slot.", REG, 46),
    ("As of [Mon/Thu]’s count: [X] slots remain.", REG, 46),
]
HOLDS = [2.0, 3.0, 3.0, 4.0]     # 12.0s total, per the script's time column


def wrap(draw, text, font, maxw):
    if "\n" in text:                  # explicit break beats a greedy orphan
        out = []
        for part in text.split("\n"):
            out += wrap(draw, part, font, maxw)
        return out
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=font) <= maxw or not cur:
            cur = t
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def render(state):
    """state = how many lines are visible (1..4)."""
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    maxw = W - 2 * MARGIN

    blocks = []
    for i, (text, path, size) in enumerate(LINES[:state]):
        font = ImageFont.truetype(path, size)
        blocks.append((wrap(d, text, font, maxw), font, size))

    total = sum(len(ls) * int(s * 1.24) + (0 if i == 0 else int(s * 0.9))
                for i, (ls, f, s) in enumerate(blocks))
    y = (H - total) // 2 - 40

    for i, (ls, font, size) in enumerate(blocks):
        if i:
            y += int(size * 0.9)
        for ln in ls:
            d.text((MARGIN, y), ln, font=font, fill=INK)
            y += int(size * 1.24)
        if i == 0:                      # copper rule under the price
            y += 14
            d.rectangle([MARGIN, y, MARGIN + 168, y + 8], fill=COPPER)
            y += 34

    if state == 4:                      # small wordmark on the final state
        wm = ImageFont.truetype(BOLD, 30)
        d.text((MARGIN, H - MARGIN - 30), "ATX LAKESCAPES", font=wm, fill=INK)

    p = os.path.join(OUT, "_math_s%d.png" % state)
    img.save(p)
    return p


frames = [render(n) for n in (1, 2, 3, 4)]

lst = os.path.join(OUT, "_math_concat.txt")
with open(lst, "w") as fh:
    for p, hold in zip(frames, HOLDS):
        fh.write("file '%s'\nduration %.3f\n" % (p, hold))
    # The concat demuxer needs the last file listed twice for its duration to
    # apply, but that trailing entry then plays as its own segment (measured:
    # 16.0s instead of 12.0s). -t pins the total; the tail is identical pixels,
    # so the truncation is invisible.
    fh.write("file '%s'\n" % frames[-1])

dst = os.path.join(OUT, "DRAWDOWN_Math_916_DRAFT.mp4")
subprocess.run([
    "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
    "-f", "concat", "-safe", "0", "-i", lst,
    "-vf", "scale=%d:%d,fps=%d,format=yuv420p" % (W, H, FPS),
    "-t", "%.3f" % sum(HOLDS),
    "-an", "-c:v", "libx264", "-crf", "19", "-preset", "slow",
    "-movflags", "+faststart", dst,
], check=True)
print("wrote", dst)
