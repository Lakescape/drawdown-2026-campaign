"""DRAWDOWN_ViralHydrilla_916_STUDIO — 15s 9:16 silent viral lead-in.

Studio pass on Hermes' preview. Four Poseidon plates, audited by caption AND
eyeballed this Mac, pinned by sha256. Composites render at 1350x2400 so the
ffmpeg Ken Burns push has real pixels when it lands on 1080x1920. Cards render
native at 1080x1920 so the type is never resampled.

C7 law: the two-machine beat must show TWO machines with amphibious
undercarriage. @two_machines (1334bce67b99) is a knuckleboom crane on a barge —
EXCLUDED. The count plate is c6b6853c038a, letterboxed (FIT) because a 9:16
cover-crop of a 1080x810 native clips the second machine out of frame.

No image-to-video. No generated machines (HIGGSFIELD-LEARNINGS Rule 11).
"""
import os
import sqlite3
import subprocess

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

DB = os.path.expanduser("~/Poseidon/visual-library/library.db")
PHOTOS = os.path.expanduser("~/Poseidon/visual-library/photos")
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
CW, CH = 1350, 2400          # composite canvas
VW, VH = 1080, 1920          # delivery
CREAM = (244, 239, 230, 255)
COPPER = (232, 176, 112, 255)
OUT = "DRAWDOWN_ViralHydrilla_916_STUDIO.mp4"
WORK = "_studio"

# (slot, sha prefix, mode, seconds, ken-burns direction, why this plate)
BEATS = [
    ("v1", "924c9e39682b", "bleed", 3.30, "in",
     "HOOK — submerged hydrilla mass beside a dock edge, clear water. Muted-legible."),
    ("v2", "f730acf1ac49", "bleed", 4.35, "out",
     "STAKES — looking down off a dock into weed-choked water. You walk over it."),
    ("v3", "c6b6853c038a", "fit", 4.35, "in",
     "CAPABILITY — TWO Truxors working, one throwing spray. C7 count + amphibious."),
    ("v4", "83f97f1642cd", "bleed", 4.35, "out",
     "INFORM — hauled hydrilla mound on a bulkhead, dump trailer behind. Scrape/haul proof."),
]

# (slot, [(text, size, colour)], y-fraction)
CARDS = [
    ("v1", [("THIS IS UNDER", 96, CREAM),
            ("YOUR DOCK.", 96, CREAM)], 0.74),
    ("v2", [("NEARLY TEN YEARS", 74, CREAM),
            ("SINCE ANYONE COULD SEE IT.", 44, CREAM)], 0.74),
    ("v3", [("TWO TRUXORS.", 78, CREAM),
            ("PROJECTED 10–12 FT.", 60, CREAM),
            ("NOTHING IS OFFICIAL YET", 36, COPPER)], 0.74),
    ("v4", [("SCRAPE. HAUL. STAPLE.", 62, CREAM),
            ("254-780-6971", 84, COPPER)], 0.74),
]

con = sqlite3.connect(DB)


def resolve(prefix):
    row = con.execute("SELECT sha256 FROM refs WHERE sha256 LIKE ?",
                      (prefix + "%",)).fetchone()
    if not row:
        raise SystemExit(f"UNPINNED: {prefix} not in Poseidon")
    return row[0], os.path.join(PHOTOS, row[0] + ".jpg")


def cover(im, w, h):
    s = max(w / im.width, h / im.height)
    im = im.resize((int(im.width * s) + 1, int(im.height * s) + 1), Image.LANCZOS)
    return im.crop(((im.width - w) // 2, (im.height - h) // 2,
                    (im.width - w) // 2 + w, (im.height - h) // 2 + h))


os.makedirs(WORK, exist_ok=True)
pins = []
for slot, prefix, mode, dur, kb, why in BEATS:
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
        px, py = 0, int(CH * 0.40) - fg.height // 2
        out.paste(fg, (px, py))
        ImageDraw.Draw(out).rectangle(
            [px, py, px + fg.width - 1, py + fg.height - 1],
            outline=(244, 239, 230), width=3)
    out.save(f"{WORK}/comp_{slot}.jpg", quality=94)
    print(f"{slot} {mode} {sha[:12]} {im.width}x{im.height} — {why}")

# Cards native 1080x1920 — type never resampled.
for slot, lines, yf in CARDS:
    img = Image.new("RGBA", (VW, VH), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    top = int(VH * 0.50)
    for y in range(top, VH):
        t = (y - top) / (VH - top)
        d.line([(0, y), (VW, y)], fill=(10, 18, 24, int(205 * t ** 0.70)))
    rendered = [(t, ImageFont.truetype(BOLD, s), c) for t, s, c in lines]
    heights = [d.textbbox((0, 0), t, font=f)[3] for t, f, _ in rendered]
    gap = 22
    total = sum(heights) + gap * (len(rendered) - 1)
    y = int(VH * yf) - total // 2
    widest = max(d.textbbox((0, 0), t, font=f)[2] for t, f, _ in rendered)
    plate = Image.new("RGBA", (VW, VH), (0, 0, 0, 0))
    ImageDraw.Draw(plate).rounded_rectangle(
        [(VW - widest) // 2 - 52, y - 36, (VW + widest) // 2 + 52, y + total + 36],
        radius=20, fill=(10, 18, 24, 160))
    img.alpha_composite(plate)
    d = ImageDraw.Draw(img)
    for i, (t, f, c) in enumerate(rendered):
        w = d.textbbox((0, 0), t, font=f)[2]
        x = (VW - w) // 2
        d.text((x + 3, y + 3), t, font=f, fill=(0, 0, 0, 180))
        d.text((x, y), t, font=f, fill=c)
        y += heights[i] + gap
    img.save(f"{WORK}/card_{slot}.png")

FPS = 30
XF = 0.35                     # crossfade between beats

# ── filter graph ──────────────────────────────────────────────────────────
ins, parts, labels = [], [], []
for i, (slot, _, _, dur, kb) in enumerate(
        [(s, a, m, d, k) for s, a, m, d, k, _ in
         [(b[0], b[1], b[2], b[3], b[4], b[5]) for b in BEATS]]):
    ins += ["-loop", "1", "-t", f"{dur:.2f}", "-i", f"{WORK}/comp_{slot}.jpg"]
    n = int(dur * FPS)
    # push in / pull out. zoompan on an upscaled still keeps the move jitter-free.
    if kb == "in":
        z = f"1.02+0.09*on/{n}"
    else:
        z = f"1.11-0.09*on/{n}"
    parts.append(
        f"[{i}:v]scale=2160:3840:flags=lanczos,"
        f"zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':"
        f"d=1:s={VW}x{VH}:fps={FPS},"
        f"setsar=1,format=yuv420p[b{i}]")
    labels.append(f"b{i}")

for i, (slot, *_ ) in enumerate(BEATS):
    ins += ["-loop", "1", "-i", f"{WORK}/card_{slot}.png"]

# xfade chain
chain = labels[0]
elapsed = BEATS[0][3]
for i in range(1, len(BEATS)):
    off = elapsed - XF
    parts.append(f"[{chain}][{labels[i]}]xfade=transition=fade:duration={XF}:"
                 f"offset={off:.2f}[x{i}]")
    chain = f"x{i}"
    elapsed = off + XF + BEATS[i][3] - XF + XF  # beat i starts at off+XF
    elapsed = off + BEATS[i][3]
TOTAL = elapsed

# card overlays — fade in after the plate has landed, out before the cut
starts, t = [], 0.0
for i, b in enumerate(BEATS):
    starts.append(t)
    t += b[3] - (XF if i < len(BEATS) - 1 else 0)

cur = chain
for i, (slot, *_) in enumerate(BEATS):
    ci = len(BEATS) + i
    s0 = starts[i] + 0.45
    s1 = starts[i] + BEATS[i][3] - 0.30
    parts.append(
        f"[{ci}:v]format=rgba,fade=t=in:st={s0:.2f}:d=0.35:alpha=1,"
        f"fade=t=out:st={s1:.2f}:d=0.30:alpha=1[c{i}]")
    parts.append(f"[{cur}][c{i}]overlay=0:0:enable='between(t,{starts[i]:.2f},"
                 f"{starts[i]+BEATS[i][3]:.2f})'[o{i}]")
    cur = f"o{i}"

fg = ";".join(parts)
cmd = ["ffmpeg", "-y", *ins,
       "-f", "lavfi", "-t", f"{TOTAL:.2f}", "-i", "anullsrc=r=48000:cl=stereo",
       "-filter_complex", fg,
       "-map", f"[{cur}]", "-map", f"{2*len(BEATS)}:a",
       "-t", f"{TOTAL:.2f}",
       "-c:v", "libx264", "-crf", "18", "-preset", "slow",
       "-pix_fmt", "yuv420p", "-r", str(FPS),
       "-c:a", "aac", "-b:a", "96k", "-shortest",
       "-movflags", "+faststart", OUT]
print("\ntimeline:", [f"{s:.2f}" for s in starts], "total", f"{TOTAL:.2f}s")
subprocess.run(cmd, check=True)
print("\nWROTE", OUT)
for slot, sha, mode, dur, why in pins:
    print(f"  {slot}  {dur:>4.1f}s  {mode:<5} {sha}")
