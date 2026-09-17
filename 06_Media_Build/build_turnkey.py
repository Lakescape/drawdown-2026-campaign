"""DRAWDOWN_Turnkey_916_STUDIO — 15s 9:16 Turnkey & Permitting Explainer.

Pitches the zero-headache, 100% turnkey service:
- We file the City of Austin & LCRA permits
- Amphibious fleet protects lawn & bulkhead
- Complete haul-off (not piled in yard)
- Bed covered and pinned before refill
"""
import os, sqlite3, subprocess
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

DB = os.path.expanduser("~/Poseidon/visual-library/library.db")
PHOTOS = os.path.expanduser("~/Poseidon/visual-library/photos")
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
CW, CH = 1350, 2400          # composite canvas
VW, VH = 1080, 1920          # delivery viewport
CREAM = (244, 239, 230, 255)
COPPER = (232, 176, 112, 255)
INK = (18, 26, 32, 255)
FPS = 30
XF = 0.35
OUT = "DRAWDOWN_Turnkey_916_STUDIO.mp4"
WORK = "_turnkey"

# (slot, sha prefix, mode, seconds, kb_direction, why)
BEATS = [
    ("b1", "153d39cdb0eb", "bleed", 3.60, "in",
     "HOOK: shoreline — YOU DON'T FILE A THING / WE HANDLE COA & LCRA"),
    ("b2", "c6b6853c038a", "fit", 4.00, "out",
     "FLEET: two Truxors, pontoons (C7) — OUR CREW. OUR IRON."),
    ("b3", "83f97f1642cd", "bleed", 4.00, "in",
     "HAUL 1: right-bias 9:16 ax=0.90 — LOAD TRAIL + barge pile. OFF THE BARGE."),
    ("b4", "5e85f06eda86de4b", "bleed", 4.40, "in",
     "HAUL 2: standing in the packed dump trailer, lake ahead — INTO THE TRAILER. "
     "Portrait 810x1080, fills 9:16. Not a366 (identifiable houses)."),
    ("b5", "870b907f2401", "bleed", 3.40, "in",
     "CLOSE: cutter POV — WE RUN IT. YOU DON'T. / 254-780-6971"),
]

CARDS = [
    ("b1", [("YOU DON'T FILE A THING", 62, CREAM),
            ("WE HANDLE COA & LCRA", 48, COPPER)], 0.76),
    ("b2", [("OUR CREW. OUR IRON.", 68, CREAM),
            ("AMPHIBIOUS TRUXORS", 48, COPPER)], 0.76),
    ("b3", [("OFF THE BARGE.", 84, CREAM)], 0.82),
    ("b4", [("INTO THE TRAILER.", 72, CREAM),
            ("GONE OFF YOUR LOT.", 46, COPPER)], 0.78),
    ("b5", [("WE RUN IT. YOU DON'T.", 62, CREAM),
            ("TEXT TRUXOR · 254-780-6971", 48, COPPER)], 0.76),
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

def cover(im, w, h, ax=0.5, ay=0.5):
    s = max(w / im.width, h / im.height)
    im = im.resize((int(im.width * s) + 1, int(im.height * s) + 1), Image.LANCZOS)
    maxx, maxy = im.width - w, im.height - h
    x = int(maxx * ax)
    y = int(maxy * ay)
    return im.crop((x, y, x + w, y + h))

os.makedirs(WORK, exist_ok=True)
pins = []

for slot, prefix, mode, dur, kb, why in BEATS:
    sha, path = resolve(prefix)
    pins.append((slot, sha, mode, dur, why))
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")
    # Registry orientation guard
    reg_w, reg_h = con.execute("SELECT width,height FROM refs WHERE sha256=?", (sha,)).fetchone()
    if (im.width, im.height) != (reg_w, reg_h):
        if (im.height, im.width) == (reg_w, reg_h):
            print(f"  ⚠ {slot} EXIF rotated vs registry — trusting registry")
            im = Image.open(path).convert("RGB")
        else:
            raise SystemExit(f"ORIENTATION FAIL {slot}: {im.width}x{im.height} ≠ {reg_w}x{reg_h}")

    if mode == "bleed":
        # b3: trailer is top-right of the landscape — center crop hides it.
        ax = 0.90 if slot == "b3" else 0.50
        out = cover(im, CW, CH, ax=ax, ay=0.0)
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

# Native 1080x1920 straps
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
    if slot == "b3":
        # Tiny push only — 1.09 center-zoom ate the LOAD TRAIL on the right edge.
        z = f"1.00+0.03*on/{n}"
    else:
        z = f"1.02+0.07*on/{n}" if kb == "in" else f"1.05-0.05*on/{n}"
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
    parts.append(f"[{chain}][{labels[i]}]xfade=transition=fade:duration={XF}:offset={off:.2f}[x{i}]")
    chain = f"x{i}"
    starts.append(off)
TOTAL = starts[-1] + BEATS[-1][3]

cur = chain
for j, slot in enumerate(card_slots):
    i = [b[0] for b in BEATS].index(slot)
    ci = len(BEATS) + j
    s0 = starts[i] + 0.40
    s1 = starts[i] + BEATS[i][3] - 0.30
    fades = f"fade=t=in:st={s0:.2f}:d=0.35:alpha=1"
    if i < len(BEATS) - 1:
        fades += f",fade=t=out:st={s1:.2f}:d=0.30:alpha=1"
    parts.append(f"[{ci}:v]format=rgba,{fades}[c{j}]")
    parts.append(f"[{cur}][c{j}]overlay=0:0:enable='between(t,{starts[i]:.2f},{starts[i]+BEATS[i][3]:.2f})'[o{j}]")
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
    print(f"  {slot}  {dur:>4.1f}s  {mode:<5} {sha[:12]}")
