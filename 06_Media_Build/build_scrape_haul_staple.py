"""DRAWDOWN_ScrapeHaulStaple_916_STUDIO — 15s 9:16 silent method explainer.

One job, three verbs. A Lake Austin homeowner should be able to repeat it after
fifteen silent seconds: SCRAPE the marked bed, HAUL the spoil off the lot,
COVER the bed with erosion mat. Nate 2026-09-01: do not put “woven tarp /
12-inch overlap” on a plate that is not a tarp.

Plates are real Poseidon frames, sha-pinned, caption-audited AND eyeballed on
this Mac. No image-to-video, no generated machines, no generated tarp
(HIGGSFIELD-LEARNINGS Rule 11 — specialty equipment cannot be text-generated,
and neither can a job we have not photographed).

COVER beat (Nate 2026-09-01): real green erosion-control matting
`247ed525d59d` — crew rolling mat onto a scraped bed. Honest strap:
COVER. / Mat on the bed. Not “woven tarp. 12-inch overlap.” FIT so the
mat stays in 9:16.

C7: every equipment claim must be true of the frame it sits on.
  - SCRAPE  c6b6853c038a  FIT — two Truxors, one throwing spray. A 9:16 cover
    crop of the 1080x810 native clips the second machine out of frame.
  - HAUL    83f97f1642cd  FIT — spoil mound on the work platform with the
    LOAD TRAIL dump trailer on the bank behind it. "Off your lot." is only
    honest while the trailer is in frame, and a 9:16 crop cuts the trailer.
    This is a deliberate deviation from the packet's "bleed".
  - HOLD    870b907f2401  bleed — operator POV over the cutter head, cut weed
    on the rake, clean water and a boathouse beyond. Claims nothing but itself.

Both FIT beats pull OUT (1.05 -> 1.00) rather than pushing in, so the beat ENDS
on the complete frame and the claim-critical thing (second machine / trailer)
can never be zoomed off the edge.
"""
import os
import sqlite3
import subprocess

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

DB = os.path.expanduser("~/Poseidon/visual-library/library.db")
PHOTOS = os.path.expanduser("~/Poseidon/visual-library/photos")
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
CW, CH = 1350, 2400          # composite canvas — real pixels for the Ken Burns
VW, VH = 1080, 1920          # delivery
CREAM = (244, 239, 230, 255)
COPPER = (232, 176, 112, 255)
INK = (18, 26, 32, 255)
FPS = 30
XF = 0.35
OUT = "DRAWDOWN_ScrapeHaulStaple_916_STUDIO.mp4"
WORK = "_shs"

# (slot, sha prefix or None, mode, seconds, ken-burns, why this plate)
# starts land on 0 / 4 / 9 / 13, total 15.00 after the crossfades eat the overlap
BEATS = [
    ("b1", "c6b6853c038a", "fit", 4.35, "out",
     "SCRAPE — two Truxors working the bed, one throwing spray. C7 count and "
     "amphibious undercarriage both visible."),
    ("b2", "83f97f1642cd", "fit", 5.35, "out",
     "HAUL — spoil mound on the work platform, LOAD TRAIL dump trailer on the "
     "bank behind. The trailer is what makes 'Off your lot.' honest."),
    ("b3", "247ed525d59d", "fit", 4.35, "out",
     "COVER — green erosion-control matting rolled onto a scraped bed. "
     "Honest product. Not a woven tarp."),
    ("b4", "870b907f2401", "bleed", 2.00, "in",
     "HOLD — operator POV over the cutter head with cut weed on it, clean "
     "water beyond. The CTA plate."),
]

# straps over the picture beats — (slot, [(text, size, colour)], y-fraction)
CARDS = [
    ("b1", [("SCRAPE.", 104, CREAM),
            ("We cut it off the bed.", 46, CREAM)], 0.76),
    ("b2", [("HAUL.", 104, CREAM),
            ("Off your lot.", 46, CREAM)], 0.76),
    ("b3", [("COVER.", 104, CREAM),
            ("Mat on the bed.", 46, CREAM)], 0.76),
    ("b4", [("That's the job.", 62, CREAM),
            ("254-780-6971", 84, COPPER)], 0.76),
]

# the type-only staple plate — dark ink on cream, no picture to overclaim
STAPLE_CARD = [("STAPLE.", 118, INK),
               ("Woven tarp.", 56, INK),
               ("12-inch overlap.", 56, INK)]

con = sqlite3.connect(DB)


def resolve(prefix):
    row = con.execute("SELECT sha256 FROM refs WHERE sha256 LIKE ?",
                      (prefix + "%",)).fetchone()
    if not row:
        raise SystemExit(f"UNPINNED: {prefix} not in Poseidon")
    path = os.path.join(PHOTOS, row[0] + ".jpg")
    if not os.path.exists(path):
        raise SystemExit(f"NO LOCAL BYTES: {row[0]}")
    return row[0], path


def cover(im, w, h):
    s = max(w / im.width, h / im.height)
    im = im.resize((int(im.width * s) + 1, int(im.height * s) + 1), Image.LANCZOS)
    return im.crop(((im.width - w) // 2, (im.height - h) // 2,
                    (im.width - w) // 2 + w, (im.height - h) // 2 + h))


os.makedirs(WORK, exist_ok=True)
pins = []
for slot, prefix, mode, dur, kb, why in BEATS:
    if mode == "card":
        pins.append((slot, "TYPE-ONLY", mode, dur, why))
        img = Image.new("RGB", (VW, VH), CREAM[:3])
        d = ImageDraw.Draw(img)
        rendered = [(t, ImageFont.truetype(BOLD, s), c) for t, s, c in STAPLE_CARD]
        heights = [d.textbbox((0, 0), t, font=f)[3] for t, f, _ in rendered]
        gap = 26
        total = sum(heights) + gap * (len(rendered) - 1)
        y = int(VH * 0.50) - total // 2
        # hairline rule above the type — reads as a deliberate plate, not a hole
        d.line([(VW * 0.28, y - 74), (VW * 0.72, y - 74)], fill=INK[:3], width=3)
        for i, (t, f, c) in enumerate(rendered):
            w = d.textbbox((0, 0), t, font=f)[2]
            d.text(((VW - w) // 2, y), t, font=f, fill=c[:3])
            y += heights[i] + gap
        img.save(f"{WORK}/comp_{slot}.jpg", quality=96)
        print(f"{slot} card  TYPE-ONLY — {why}")
        continue

    sha, path = resolve(prefix)
    pins.append((slot, sha, mode, dur, why))
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    if mode == "bleed":
        out = cover(im, CW, CH)
    else:
        out = cover(im, CW, CH).filter(ImageFilter.GaussianBlur(38))
        out = ImageEnhance.Brightness(out).enhance(0.50)
        fg = im.copy()
        s = CW / fg.width
        fg = fg.resize((CW, int(fg.height * s)), Image.LANCZOS)
        px, py = 0, int(CH * 0.42) - fg.height // 2
        out.paste(fg, (px, py))
        ImageDraw.Draw(out).rectangle(
            [px, py, px + fg.width - 1, py + fg.height - 1],
            outline=CREAM[:3], width=3)
    out.save(f"{WORK}/comp_{slot}.jpg", quality=94)
    print(f"{slot} {mode:<5} {sha[:12]} {im.width}x{im.height} — {why}")

# straps native 1080x1920 so the type is never resampled
for slot, lines, yf in CARDS:
    img = Image.new("RGBA", (VW, VH), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    top = int(VH * 0.50)
    for y in range(top, VH):
        t = (y - top) / (VH - top)
        d.line([(0, y), (VW, y)], fill=(10, 18, 24, int(205 * t ** 0.70)))
    rendered = [(t, ImageFont.truetype(BOLD, s), c) for t, s, c in lines]
    heights = [d.textbbox((0, 0), t, font=f)[3] for t, f, _ in rendered]
    gap = 20
    total = sum(heights) + gap * (len(rendered) - 1)
    y = int(VH * yf) - total // 2
    widest = max(d.textbbox((0, 0), t, font=f)[2] for t, f, _ in rendered)
    plate = Image.new("RGBA", (VW, VH), (0, 0, 0, 0))
    ImageDraw.Draw(plate).rounded_rectangle(
        [(VW - widest) // 2 - 52, y - 34, (VW + widest) // 2 + 52, y + total + 34],
        radius=20, fill=(10, 18, 24, 165))
    img.alpha_composite(plate)
    d = ImageDraw.Draw(img)
    for i, (t, f, c) in enumerate(rendered):
        w = d.textbbox((0, 0), t, font=f)[2]
        x = (VW - w) // 2
        d.text((x + 3, y + 3), t, font=f, fill=(0, 0, 0, 180))
        d.text((x, y), t, font=f, fill=c)
        y += heights[i] + gap
    img.save(f"{WORK}/card_{slot}.png")

# ── filter graph ──────────────────────────────────────────────────────────
ins, parts, labels = [], [], []
for i, (slot, _, mode, dur, kb, _) in enumerate(BEATS):
    # -framerate is REQUIRED. Without it -loop 1 feeds 25 fps into a filter that
    # labels its output 30, every beat runs 5/6 of its nominal length, the xfade
    # offsets walk past the end of their inputs and the whole cut collapses onto
    # the last plate — with ffmpeg exiting 0 and saying nothing. (QC 2026-08-31.)
    ins += ["-loop", "1", "-framerate", str(FPS), "-t", f"{dur:.2f}",
            "-i", f"{WORK}/comp_{slot}.jpg"]
    n = int(dur * FPS)
    if mode == "card":
        parts.append(f"[{i}:v]scale={VW}:{VH}:flags=lanczos,fps={FPS},"
                     f"setsar=1,format=yuv420p[b{i}]")
    else:
        z = f"1.02+0.08*on/{n}" if kb == "in" else f"1.05-0.05*on/{n}"
        parts.append(
            f"[{i}:v]scale=2160:3840:flags=lanczos,"
            f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
            f"d=1:s={VW}x{VH}:fps={FPS},"
            f"setsar=1,format=yuv420p[b{i}]")
    labels.append(f"b{i}")

card_slots = [c[0] for c in CARDS]
for slot in card_slots:
    ins += ["-loop", "1", "-framerate", str(FPS), "-i", f"{WORK}/card_{slot}.png"]

chain = labels[0]
starts = [0.0]
for i in range(1, len(BEATS)):
    off = starts[i - 1] + BEATS[i - 1][3] - XF
    parts.append(f"[{chain}][{labels[i]}]xfade=transition=fade:duration={XF}:"
                 f"offset={off:.2f}[x{i}]")
    chain = f"x{i}"
    starts.append(off)
TOTAL = starts[-1] + BEATS[-1][3]

cur = chain
for j, slot in enumerate(card_slots):
    i = [b[0] for b in BEATS].index(slot)
    ci = len(BEATS) + j
    s0 = starts[i] + 0.45
    s1 = starts[i] + BEATS[i][3] - 0.30
    fades = f"fade=t=in:st={s0:.2f}:d=0.35:alpha=1"
    if i < len(BEATS) - 1:
        fades += f",fade=t=out:st={s1:.2f}:d=0.30:alpha=1"
    parts.append(f"[{ci}:v]format=rgba,{fades}[c{j}]")
    parts.append(f"[{cur}][c{j}]overlay=0:0:enable='between(t,{starts[i]:.2f},"
                 f"{starts[i]+BEATS[i][3]:.2f})'[o{j}]")
    cur = f"o{j}"

cmd = ["ffmpeg", "-y", *ins,
       "-filter_complex", ";".join(parts),
       "-map", f"[{cur}]",
       "-t", f"{TOTAL:.2f}",
       "-an",                       # truly silent — no stream, not a null track
       "-c:v", "libx264", "-crf", "18", "-preset", "slow",
       "-pix_fmt", "yuv420p", "-r", str(FPS),
       "-movflags", "+faststart", OUT]
print("\ntimeline:", [f"{s:.2f}" for s in starts], "total", f"{TOTAL:.2f}s")
subprocess.run(cmd, check=True)
print("\nWROTE", OUT)
for slot, sha, mode, dur, why in pins:
    print(f"  {slot}  {dur:>4.1f}s  {mode:<5} {sha}")
