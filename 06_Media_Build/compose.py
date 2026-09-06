"""Build 9:16 composites from real ATX library stills, plus the title cards.

Landscape phone photos are letterboxed over a blurred, darkened cover-crop of
themselves — the frame stays 9:16 for social without cropping away the subject.
Composites render at 1350x2400 so the ffmpeg Ken Burns push has real pixels to
work with when it scales down to 1080x1920.

No image-to-video: these are real machines on a real lake, and a generative
model would invent geometry. Motion comes from camera moves over true frames.
"""
import os
import sqlite3

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

DB = os.path.expanduser("~/Poseidon/visual-library/library.db")
PHOTOS = os.path.expanduser("~/Poseidon/visual-library/photos")
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
W, H = 1350, 2400
CREAM = (244, 239, 230, 255)
COPPER = (232, 176, 112, 255)

# Gate 4 shot list: (slot, sha prefix, mode, line it carries)
#
# mode "bleed" = cover-crop to full 9:16. Fills the frame, card sits on image.
# mode "fit"   = letterbox over blur. Used ONLY where a side crop could push a
#                machine out of frame and break the two-machine count in C7.
#                Claim safety beats composition on those two shots.
PICKS = [
    ("s01", "924c9e39682b", "bleed", "L1 submerged hydrilla — 'never actually seen it'"),
    ("s02", "43f28fb00bb4", "bleed", "L1 canal mat + far-bank bulkhead"),
    ("s03", "0beab2b84bbe", "bleed", "L2 muddy exposed bank"),
    ("s04", "b91a25c6c384", "bleed", "L2 eroded bank at waterline"),
    ("s05", "870b907f2401", "bleed", "L3 calm water, boom, boathouse — the honest beat"),
    ("s06", "fd49bf6ffe3e", "fit", "L4 TWO Truxors staged — C7 count"),
    ("s07", "83f97f1642cd", "bleed", "L5 weed pile on bulkhead"),
    ("s08", "083f40bf8835", "bleed", "L5 damaged dock, exposed piling"),
    ("s09", "b0e39a623f7c", "bleed", "L6 sediment pile on muddy shoreline"),
    ("s10", "cd351a221a00", "bleed", "L6 Truxor beside cut-weed pile"),
    ("s11", "c6b6853c038a", "fit", "L7 TWO Truxors working — C7 count + capacity"),
    ("s12", "ca77ddebe73b", "bleed", "L8 two Truxors docked, calm"),
    ("s13", "360fb66761d0", "bleed", "L8 calm water and lawn"),
    ("s14", "84a901e3a7c3", "bleed", "L9 dock + boathouse — Lake Austin"),
]

CARDS = [
    ("k1", [("TEN YEARS UNDERWATER", 84, CREAM)], 0.72, "bottom"),
    # Nate 2026-09-06: ABOUT 10 FT campaign-wide (LCRA). 10–12 retired.
    ("k2", [("ABOUT 10 FEET", 68, CREAM),
            ("OCT 12 – NOV 30 · LCRA", 48, COPPER)], 0.70, "bottom"),
    # k3 deleted 2026-09-04: "NOTHING IS OFFICIAL YET" — the hedge was retired
    # 2026-08-29 (LCRA announced); the drawdown IS official and the phrase is
    # banned from every cut and caption. Masters that carry it on-frame are
    # flagged NEEDS-RECUT on the desk.
    ("k4", [("TWO AMPHIBIOUS MACHINES", 58, CREAM),
            ("COMMITTED IN JULY", 44, COPPER)], 0.70, "bottom"),
    ("k5", [("TYPICALLY 30–40% LESS", 62, CREAM),
            ("ON DRY GROUND", 46, COPPER)], 0.70, "bottom"),
    ("k6", [("ROUGHLY 25 WORKING DAYS", 56, CREAM),
            ("THEN WE'RE FULL", 46, COPPER)], 0.70, "bottom"),
    # k7 deleted 2026-09-04: "$695 PRIORITY ASSESSMENT / 100% CREDITED" —
    # $695, credited, and assessment are banned (Nate 2026-08-31).
    ("k8", [("ATX LAKESCAPES", 82, CREAM),
            ("LAKE AUSTIN IS OUR HOME WATER", 40, COPPER)], 0.46, "full"),
]

con = sqlite3.connect(DB)


def resolve(prefix):
    row = con.execute("SELECT sha256 FROM refs WHERE sha256 LIKE ?", (prefix + "%",)).fetchone()
    return os.path.join(PHOTOS, row[0] + ".jpg") if row else None


def cover(im, w, h):
    s = max(w / im.width, h / im.height)
    im = im.resize((int(im.width * s) + 1, int(im.height * s) + 1), Image.LANCZOS)
    return im.crop(((im.width - w) // 2, (im.height - h) // 2,
                    (im.width - w) // 2 + w, (im.height - h) // 2 + h))


def crop_ar(im, ar):
    """Centre-crop to aspect ratio ar (w/h) without scaling."""
    w, h = im.size
    nw, nh = (int(h * ar), h) if w / h > ar else (w, int(w / ar))
    return im.crop(((w - nw) // 2, (h - nh) // 2, (w - nw) // 2 + nw, (h - nh) // 2 + nh))


for slot, prefix, mode, note in PICKS:
    path = resolve(prefix)
    if not path or not os.path.exists(path):
        print("MISSING", slot, prefix)
        continue
    im = ImageOps.exif_transpose(Image.open(path)).convert("RGB")

    if mode == "bleed":
        out = cover(im, W, H)
    else:
        out = cover(im, W, H).filter(ImageFilter.GaussianBlur(38))
        out = ImageEnhance.Brightness(out).enhance(0.55)
        # Both count shots are 1080x810 native — Jobber's ceiling, no higher-res
        # original exists, and no high-res two-machine alternate is in the
        # library. So: keep the full 4:3 frame (a 4:5 or 9:16 crop would need a
        # 1.7x upscale, and a 9:16 crop clips the second machine outright,
        # breaking C7). Scale to canvas width only — same 1.25x the bleed shots
        # already take — and frame it as a deliberate photo-with-caption.
        fg = im.copy()
        s = W / fg.width
        fg = fg.resize((W, int(fg.height * s)), Image.LANCZOS)
        px, py = 0, int(H * 0.42) - fg.height // 2
        out.paste(fg, (px, py))
        ImageDraw.Draw(out).rectangle(
            [px, py, px + fg.width - 1, py + fg.height - 1],
            outline=(244, 239, 230), width=3)

    out.save(f"comp_{slot}.jpg", quality=93)
    print(slot, mode, note)


def scrim(img, mode):
    d = ImageDraw.Draw(img)
    if mode == "bottom":
        top = int(H * 0.52)
        for y in range(top, H):
            t = (y - top) / (H - top)
            d.line([(0, y), (W, y)], fill=(10, 18, 24, int(195 * t ** 0.75)))
    else:
        d.rectangle([0, 0, W, H], fill=(10, 18, 24, 165))


for name, lines, yf, mode in CARDS:
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    scrim(img, mode)
    d = ImageDraw.Draw(img)
    rendered = [(t, ImageFont.truetype(BOLD, s), c) for t, s, c in lines]
    heights = [d.textbbox((0, 0), t, font=f)[3] for t, f, _ in rendered]
    gap = 26
    total = sum(heights) + gap * (len(rendered) - 1)
    y = int(H * yf) - total // 2

    if mode == "bottom":
        widest = max(d.textbbox((0, 0), t, font=f)[2] for t, f, _ in rendered)
        plate = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(plate).rounded_rectangle(
            [(W - widest) // 2 - 60, y - 40, (W + widest) // 2 + 60, y + total + 40],
            radius=22, fill=(10, 18, 24, 155))
        img.alpha_composite(plate)
        d = ImageDraw.Draw(img)

    for i, (t, f, c) in enumerate(rendered):
        w = d.textbbox((0, 0), t, font=f)[2]
        x = (W - w) // 2
        d.text((x + 3, y + 3), t, font=f, fill=(0, 0, 0, 175))
        d.text((x, y), t, font=f, fill=c)
        y += heights[i] + gap
    img.save(f"card_{name}.png")
    print(name, "card ok")
