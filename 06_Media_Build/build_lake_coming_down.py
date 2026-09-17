"""DRAWDOWN_LakeComingDown_916_STUDIO — ~30s 9:16 aerial reel, silent-first.

W38 hero piece. Four Lake Austin aerials + a timeline card. No machines, no
tarp — this is the scale piece. The bed is Lake Coming Down v2 (Suno, instrumental).
"""
import os, sqlite3, subprocess
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

DB = os.path.expanduser("~/Poseidon/visual-library/library.db")
PHOTOS = os.path.expanduser("~/Poseidon/visual-library/photos")
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
CW, CH = 1350, 2400
VW, VH = 1080, 1920
CREAM = (244, 239, 230, 255)
COPPER = (232, 176, 112, 255)
INK = (18, 26, 32, 255)
FPS = 30
XF = 0.40
OUT = "DRAWDOWN_LakeComingDown_916_STUDIO.mp4"
WORK = "_lcd"

BEATS = [
    # slot, sha prefix, mode, seconds, kb, why
    ("b1", "8c7fd940fc1f", "bleed", 6.40, "in",
     "AERIAL 1 — wide Lake Austin, coves, shoreline. Establishes the lake."),
    ("b2", "5a4942b7731d", "bleed", 6.40, "in",
     "AERIAL 2 — dense hydrilla bed under reflected sky. The problem scale."),
    ("b3", "c6b6853c038a", "fit", 6.40, "out",
     "TRUXORS 1 — two Truxors working the bed, throwing spray. C7 count & iron."),
    ("b4", "cd351a221a00", "fit", 6.40, "out",
     "TRUXORS 2 — Truxor beside massive cut-weed mound on shoreline. Real harvest."),
    ("b5", None, "card", 6.00, None,
     "TIMELINE CARD — dates from LCRA release."),
]

CARDS = [
    ("b1", [("LAKE AUSTIN", 82, CREAM),
            ("DRAWDOWN 2026", 56, COPPER)], 0.80),
    ("b2", [("ABOUT 10 FEET", 74, CREAM),
            ("LCRA: Oct 12 – Nov 24", 42, COPPER)], 0.80),
    ("b3", [("TWO AMPHIBIOUS TRUXORS", 64, CREAM),
            ("COMMITTED IN JULY", 48, COPPER)], 0.80),
    ("b4", [("WE WORK THE BED", 72, CREAM),
            ("SCRAPE · HAUL · COVER", 46, COPPER)], 0.80),
]

TIMELINE_CARD = [  # TYPE-ONLY cream card at the end
    ("LAKE AUSTIN DRAWDOWN", 62, INK),
    ("Oct 12 — Lowering begins", 46, INK),
    ("~3 weeks to target", 38, INK),
    ("Nov 2–24 — Dry floor window", 46, INK),
    ("Nov 24 — Refill starts", 46, INK),
    ("Nov 30 — Normal pool", 46, INK),
    ("", 34, INK),
    ("scrape · haul · cover", 38, COPPER),
    ("254-780-6971", 58, COPPER),
]

con = sqlite3.connect(DB)

def resolve(prefix):
    row = con.execute("SELECT sha256 FROM refs WHERE sha256 LIKE ?",
                      (prefix + "%",)).fetchone()
    if not row:
        raise SystemExit(f"UNPINNED: {prefix}")
    path = os.path.join(PHOTOS, row[0] + ".jpg")
    if not os.path.exists(path):
        raise SystemExit(f"NO BYTES: {row[0]}")
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
        rendered = [(t, ImageFont.truetype(BOLD, s), c) for t, s, c in TIMELINE_CARD if t]
        heights = [d.textbbox((0, 0), t, font=f)[3] for t, f, _ in rendered]
        gap = 22
        total = sum(heights) + gap * (len(rendered) - 1)
        y = int(VH * 0.38) - total // 2
        d.line([(VW * 0.20, y - 60), (VW * 0.80, y - 60)], fill=INK[:3], width=3)
        for t, f, c in rendered:
            tw = d.textbbox((0, 0), t, font=f)[2]
            d.text(((VW - tw) // 2, y), t, font=f, fill=c[:3])
            y += heights.pop(0) + gap
        img.save(f"{WORK}/comp_{slot}.jpg", quality=96)
        print(f"{slot} card  TYPE-ONLY — {why}")
        continue

    sha, path = resolve(prefix)
    pins.append((slot, sha, mode, dur, why))
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    # Orientation guard: if transpose flips dimensions vs registry, trust registry
    reg_w, reg_h = con.execute(
        "SELECT width,height FROM refs WHERE sha256=?", (sha,)
    ).fetchone()
    if (im.width, im.height) != (reg_w, reg_h):
        if (im.height, im.width) == (reg_w, reg_h):
            print(f"  ⚠ {slot} EXIF rotated vs registry — trusting registry, ignoring transpose")
            im = Image.open(path).convert("RGB")
        else:
            raise SystemExit(
                f"ORIENTATION FAIL {slot}: transpose {im.width}x{im.height} ≠ registry {reg_w}x{reg_h}"
            )
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

# strap overlays
for slot, lines, yf in CARDS:
    img = Image.new("RGBA", (VW, VH), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    top = int(VH * 0.50)
    for ly in range(top, VH):
        t_alpha = (ly - top) / (VH - top)
        d.line([(0, ly), (VW, ly)], fill=(10, 18, 24, int(205 * t_alpha ** 0.70)))
    rendered = [(t, ImageFont.truetype(BOLD, s), c) for t, s, c in lines]
    heights = [d.textbbox((0, 0), t, font=f)[3] for t, f, _ in rendered]
    gap = 20
    total_h = sum(heights) + gap * (len(rendered) - 1)
    y = int(VH * yf) - total_h // 2
    widest = max(d.textbbox((0, 0), t, font=f)[2] for t, f, _ in rendered)
    plate = Image.new("RGBA", (VW, VH), (0, 0, 0, 0))
    ImageDraw.Draw(plate).rounded_rectangle(
        [(VW - widest) // 2 - 52, y - 34, (VW + widest) // 2 + 52, y + total_h + 34],
        radius=20, fill=(10, 18, 24, 165))
    img.alpha_composite(plate)
    d = ImageDraw.Draw(img)
    for t, f, c in rendered:
        tw = d.textbbox((0, 0), t, font=f)[2]
        x = (VW - tw) // 2
        d.text((x + 3, y + 3), t, font=f, fill=(0, 0, 0, 180))
        d.text((x, y), t, font=f, fill=c)
        y += heights.pop(0) + gap
    img.save(f"{WORK}/card_{slot}.png")

# ── ffmpeg filter graph ───────────────────────────────────────────────────
ins, parts, labels = [], [], []
for i, (slot, _, mode, dur, kb, _) in enumerate(BEATS):
    ins += ["-loop", "1", "-framerate", str(FPS), "-t", f"{dur:.2f}",
            "-i", f"{WORK}/comp_{slot}.jpg"]
    n = int(dur * FPS)
    if mode == "card":
        parts.append(f"[{i}:v]scale={VW}:{VH}:flags=lanczos,fps={FPS},"
                     f"setsar=1,format=yuv420p[b{i}]")
    else:
        z = f"1.02+0.07*on/{n}" if kb == "in" else f"1.04-0.04*on/{n}"
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
    if i in (1, 2):  # keep cards 2 + 3 visible across their beats
        fades = f"fade=t=in:st={s0:.2f}:d=0.35:alpha=1,fade=t=out:st={s1:.2f}:d=0.30:alpha=1"
    parts.append(f"[{ci}:v]format=rgba,{fades}[c{j}]")
    parts.append(f"[{cur}][c{j}]overlay=0:0:enable='between(t,{starts[i]:.2f},"
                 f"{starts[i]+BEATS[i][3]:.2f})'[o{j}]")
    cur = f"o{j}"

cmd = ["ffmpeg", "-y", *ins,
       "-filter_complex", ";".join(parts),
       "-map", f"[{cur}]",
       "-t", f"{TOTAL:.2f}",
       "-an",
       "-c:v", "libx264", "-crf", "18", "-preset", "slow",
       "-pix_fmt", "yuv420p", "-r", str(FPS),
       "-movflags", "+faststart", OUT]
print("\ntimeline:", [f"{s:.2f}" for s in starts], "total", f"{TOTAL:.2f}s")
subprocess.run(cmd, check=True)
print("\nWROTE", OUT)
for slot, sha, mode, dur, why in pins:
    print(f"  {slot}  {dur:>4.1f}s  {mode:<5} {sha}")