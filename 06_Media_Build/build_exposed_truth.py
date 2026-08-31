"""Script 01 "The Exposed Truth" — 12s, 9:16, Ken Burns over REAL Poseidon
stills, silent. No generator, no i2v (Rule 11).

AUDIT RESULT (2026-08-30). Four plates were opened and eyeballed; three were
rejected because the VLM caption did not match the frame:

  ceec62cc3f39  "staining from water exposure"      -> dirty walkway cap, no
                                                       high-water band. REJECT
  f77fcd1b3b8b  "worker ... near a wooden dock"     -> shirtless, chest-deep,
                                                       no PPE. Off-brand. REJECT
  083f40bf8835  "broken decking and exposed piling" -> palm frond over a work
                                                       site. EXIF-rotated. REJECT
  b91a25c6c384  "erosion ... exposed soil"          -> ACCEPT, verified
  b0e39a623f7c  "pile of ... sediment"              -> ACCEPT, verified

Captions are a SEARCH INDEX, not claim evidence. Every plate gets opened.

The library holds ZERO captions containing "bulkhead" or "tie-back", so the
script's "rotting tie-backs" cannot be carried by any frame. That phrase is
dropped rather than illustrated with something else. The hedge "A projected
drawdown" is kept verbatim — C1/C2 in the claim ledger make it mandatory.
"""
import os
import subprocess

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

OUT = os.path.dirname(os.path.abspath(__file__))
PHOTOS = os.path.expanduser("~/Poseidon/visual-library/photos")
W, H, FPS = 1080, 1920, 30
CREAM = (244, 239, 230)
COPPER = (232, 176, 112)
INK = (15, 15, 35)
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

# sha256 pinned in full — a prefix is not a pin
PLATES = {
    "bank": "b91a25c6c384fd90ae51690299c5a1df617b8699a3d474d417500ba025e40fa3",
    "sed": "b0e39a623f7c4756cfba906edb7f54f4be9f487b36059988cd2bc5d882cc3949",
}

# (plate, seconds, [(line, size, color)])  — None plate = paper end card
BEATS = [
    ("bank", 4.0, [("10 YEARS OF HIGH WATER", 60, CREAM),
                   ("HID THIS", 60, CREAM)]),
    ("sed", 3.0, [("SEDIMENT SHELVES YOU", 52, CREAM),
                  ("CAN'T SEE AT FULL POOL", 52, COPPER)]),
    ("sed", 3.0, [("A PROJECTED DRAWDOWN MAKES IT", 40, CREAM),
                  ("VISIBLE — AND FIXABLE", 48, COPPER)]),
    (None, 2.0, [("$695 ASSESSMENT.", 58, INK),
                 ("100% CREDITED.", 44, INK)]),
]


def cover(im, w, h):
    s = max(w / im.width, h / im.height)
    im = im.resize((int(im.width * s) + 1, int(im.height * s) + 1), Image.LANCZOS)
    return im.crop(((im.width - w) // 2, (im.height - h) // 2,
                    (im.width - w) // 2 + w, (im.height - h) // 2 + h))


def strap(lines, paper=False):
    """Static overlay. Never baked into the plate — the push must not move it."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if not paper:
        top = int(H * 0.52)
        for y in range(top, H):
            t = (y - top) / (H - top)
            d.line([(0, y), (W, y)], fill=(10, 18, 24, int(200 * t ** 0.75)))
    rend = [(t, ImageFont.truetype(BOLD, s), c) for t, s, c in lines]
    hs = [d.textbbox((0, 0), t, font=f)[3] for t, f, _ in rend]
    gap = 22
    total = sum(hs) + gap * (len(rend) - 1)
    y = int(H * (0.50 if paper else 0.74)) - total // 2
    if paper:                                   # thin gold rule above the type
        d.rectangle([96, y - 58, 96 + 168, y - 50], fill=COPPER)
    if not paper:
        # Rounded plate behind the type. The scrim alone is ~112/255 at this
        # height and CREAM over sunlit water failed legibility. Same fix the
        # 77s cut already carries in compose.py CARDS "bottom" mode.
        widest = max(d.textbbox((0, 0), t, font=f)[2] for t, f, _ in rend)
        plate = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(plate).rounded_rectangle(
            [(W - widest) // 2 - 52, y - 34, (W + widest) // 2 + 52, y + total + 34],
            radius=22, fill=(10, 18, 24, 190))
        img.alpha_composite(plate)
        d = ImageDraw.Draw(img)
    for i, (t, f, c) in enumerate(rend):
        x = 96 if paper else (W - d.textbbox((0, 0), t, font=f)[2]) // 2
        if not paper:
            d.text((x + 3, y + 3), t, font=f, fill=(0, 0, 0, 180))
        d.text((x, y), t, font=f, fill=c)
        y += hs[i] + gap
    if paper:
        wm = ImageFont.truetype(BOLD, 30)
        d.text((96, H - 96 - 30), "ATX LAKESCAPES", font=wm, fill=INK)
    return img


segs = []
for i, (plate, dur, lines) in enumerate(BEATS):
    sp = os.path.join(OUT, "_et_strap%d.png" % i)
    strap(lines, paper=plate is None).save(sp)
    seg = os.path.join(OUT, "_et_seg%d.mp4" % i)
    frames = int(dur * FPS)

    if plate is None:                            # paper end card, no motion
        base = Image.new("RGB", (W, H), CREAM)
        bp = os.path.join(OUT, "_et_base%d.jpg" % i)
        base.save(bp, quality=95)
        vf = "scale=%d:%d,fps=%d" % (W, H, FPS)
    else:
        src = os.path.join(PHOTOS, PLATES[plate] + ".jpg")
        assert os.path.exists(src), "missing plate " + plate
        im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
        bp = os.path.join(OUT, "_et_base%d.jpg" % i)
        cover(im, 1350, 2400).save(bp, quality=95)
        # slow push, ~6% over the beat. Motion comes from the camera move over a
        # true frame — never from a model inventing geometry.
        vf = ("zoompan=z='min(zoom+0.00035,1.06)':d=%d"
              ":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
              ":s=%dx%d:fps=%d" % (frames, W, H, FPS))

    subprocess.run([
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
        "-loop", "1", "-t", "%.3f" % dur, "-i", bp, "-i", sp,
        "-filter_complex", "[0:v]%s[bg];[bg][1:v]overlay=0:0,format=yuv420p[v]" % vf,
        "-map", "[v]", "-t", "%.3f" % dur, "-an",
        "-c:v", "libx264", "-crf", "18", "-preset", "slow", seg,
    ], check=True)
    segs.append(seg)

lst = os.path.join(OUT, "_et_concat.txt")
with open(lst, "w") as fh:
    for s in segs:
        fh.write("file '%s'\n" % s)

dst = os.path.join(OUT, "DRAWDOWN_ExposedTruth_916_DRAFT.mp4")
subprocess.run([
    "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
    "-f", "concat", "-safe", "0", "-i", lst,
    "-c:v", "libx264", "-crf", "18", "-preset", "slow",
    "-an", "-movflags", "+faststart", dst,
], check=True)
print("wrote", dst)
