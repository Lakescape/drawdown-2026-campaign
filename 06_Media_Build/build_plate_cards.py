"""DRAWDOWN still-card series — one verified Poseidon plate, one strap, two crops.

Feed / story stills for the pre-window runway (2026-09-07 → 2026-10-11). Every
card is a REAL ATX job photo pinned by sha256 and eyeballed before its strap was
written. No generated plates (Rule 11). No count word rides a plate that was not
eyeballed as showing two machines (C7).

Registry width/height is the display truth — the same stale-EXIF guard as
build_scrape_haul_staple.py (audit 2026-09-04). A plate whose stored pixels are
sideways (53482b8a99a8) is excluded rather than rotated.

Dates and depth come from the LCRA / City of Austin release of 2026-08-20:
Oct 12 – Nov 30, "about 10 feet", target 481.8–482.8 ft msl, refill from Nov 24.
Cards say ABOUT 10 FT because that is what LCRA said; the video cuts still carry
PROJECTED 10–12 FT from the one-pager — ledger row open for Nate.

Outputs: cards/DRAWDOWN_Card_S0N_<slug>_916.jpg (1080x1920) and _45.jpg (1080x1350)
plus cards/PINS.md.
"""
import os
import sqlite3

from PIL import Image, ImageDraw, ImageFont

DB = os.path.expanduser("~/Poseidon/visual-library/library.db")
PHOTOS = os.path.expanduser("~/Poseidon/visual-library/photos")
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cards")
CREAM = (244, 239, 230, 255)
COPPER = (232, 176, 112, 255)
SIZES = {"916": (1080, 1920), "45": (1080, 1350)}

# (slot, slug, sha prefix, crop bias (0=top..1=bottom), [(line, size, colour)], why)
CARDS = [
    ("S01", "dates", "153d39cdb0eb", 0.5,
     [("OCT 12 – NOV 30.", 84, CREAM),
      ("LAKE AUSTIN COMES DOWN ABOUT 10 FT.", 40, CREAM),
      ("LCRA · CITY OF AUSTIN · ANNOUNCED", 30, COPPER)],
     "hydrilla mat on the surface, wooded shoreline behind — the lake as it sits today"),
    ("S02", "under-your-dock", "2ef68855dbdd", 0.5,
     [("THIS IS UNDER", 92, CREAM),
      ("YOUR DOCK.", 92, CREAM),
      ("NEARLY TEN YEARS SINCE ANYONE SAW IT", 32, COPPER)],
     "dock deck in frame, water below choked with hydrilla — the card does not overclaim"),
    ("S03", "past-the-dock", "5a4942b7731d", 0.5,
     [("IT DOESN'T STOP", 80, CREAM),
      ("AT THE DOCK.", 80, CREAM),
      ("HYDRILLA · LAKE AUSTIN", 32, COPPER)],
     "aerial, dense hydrilla under a reflected sky — scale of the bed"),
    ("S04", "scrape", "ad415a4dd4ce", 0.45,
     [("SCRAPE.", 120, CREAM),
      ("THE MARKED BED. MUCK, HYDRILLA, DEBRIS.", 36, CREAM)],
     "operator seat POV, harvested hydrilla load on the deck, autumn trees — one machine, no count claim"),
    ("S05", "haul", "c30cdc0fe978", 0.5,
     [("HAUL.", 120, CREAM),
      ("SPOIL LEAVES YOUR LOT.", 36, CREAM)],
     "truck bed loaded with cut vegetation under a tarp — haul-off proof, spoil actually leaving"),
    ("S06", "cover", "247ed525d59d", 0.5,
     [("COVER.", 120, CREAM),
      ("MAT ON THE BED WHILE THE LAKE IS DOWN.", 36, CREAM)],
     "crew laying green erosion matting on a scraped bed — the COVER plate from the method cut; stale EXIF, registry wins"),
    ("S07", "two-machines", "fd49bf6ffe3e", 0.5,
     [("TWO MACHINES.", 84, CREAM),
      ("COMMITTED.", 84, CREAM),
      ("LAKE AUSTIN IS OUR HOME WATER", 32, COPPER)],
     "two Truxors staged, pontoon undercarriage visible — C7 eyeballed (BOARD 2026-08-31 erratum)"),
    ("S08", "seven-weeks", "6d6bac95fc82", 0.5,
     [("SEVEN WEEKS.", 92, CREAM),
      ("OCT 12 TO NOV 30. THEN IT REFILLS.", 36, CREAM),
      ("TEXT TRUXOR · 254-780-6971", 40, COPPER)],
     "Truxor working a dense mat with the open lake behind — the CTA card"),
    # W41 countdown — same plate as S01 so the series reads as one thread
    ("S09", "seven-days", "153d39cdb0eb", 0.5,
     [("7 DAYS.", 130, CREAM),
      ("LAKE AUSTIN COMES DOWN MONDAY, OCT 12.", 36, CREAM)],
     "S01 plate again — countdown card, posts Mon Oct 5"),
    ("S10", "monday", "153d39cdb0eb", 0.5,
     [("MONDAY.", 130, CREAM),
      ("THE LAKE STARTS DOWN TODAY. ABOUT A FOOT A DAY.", 34, CREAM),
      ("TEXT TRUXOR · 254-780-6971", 36, COPPER)],
     "S01 plate again — day-of card, posts Mon Oct 12"),
]

C7_TWO_MACHINE = {"c6b6853c038a", "fd49bf6ffe3e"}
COUNT_WORDS = ("TWO ", "BOTH ", "PAIR ")

con = sqlite3.connect(DB)


def resolve(prefix):
    row = con.execute("SELECT sha256, width, height FROM refs WHERE sha256 LIKE ?",
                      (prefix + "%",)).fetchone()
    if not row:
        raise SystemExit(f"UNPINNED: {prefix} not in Poseidon")
    path = os.path.join(PHOTOS, row[0] + ".jpg")
    if not os.path.exists(path):
        raise SystemExit(f"NO LOCAL BYTES: {row[0]}")
    return row[0], path, row[1], row[2]


def load_upright(prefix):
    """Registry width/height wins over the EXIF tag; fail closed on disagreement."""
    from PIL import ImageOps
    sha, path, rw, rh = resolve(prefix)
    raw = Image.open(path)
    im = ImageOps.exif_transpose(raw).convert("RGB")
    if (im.width > im.height) != (rw > rh) and (raw.width > raw.height) == (rw > rh):
        print(f"  EXIF tag ignored for {sha[:12]} — registry says {rw}x{rh}")
        im = raw.convert("RGB")
    if (im.width > im.height) != (rw > rh):
        raise SystemExit(f"ORIENTATION: {sha[:12]} is {im.width}x{im.height}, registry {rw}x{rh}")
    return sha, im


def cover(im, w, h, bias):
    s = max(w / im.width, h / im.height)
    im = im.resize((int(im.width * s) + 1, int(im.height * s) + 1), Image.LANCZOS)
    left = (im.width - w) // 2
    top = int((im.height - h) * bias)
    return im.crop((left, top, left + w, top + h))


def strap(w, h, lines):
    img = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    top = int(h * 0.45)
    for y in range(top, h):
        t = (y - top) / (h - top)
        d.line([(0, y), (w, y)], fill=(10, 18, 24, int(215 * t ** 0.7)))
    rendered = [(t, ImageFont.truetype(BOLD, s), c) for t, s, c in lines]
    heights = [d.textbbox((0, 0), t, font=f)[3] for t, f, _ in rendered]
    gap = 20
    total = sum(heights) + gap * (len(rendered) - 1)
    y = int(h * 0.76) - total // 2
    d.rectangle([(w - 120) // 2, y - 46, (w + 120) // 2, y - 40], fill=COPPER)
    for i, (t, f, c) in enumerate(rendered):
        tw = d.textbbox((0, 0), t, font=f)[2]
        if tw > w - 80:
            raise SystemExit(f"STRAP OVERFLOW: {t!r} is {tw}px wide")
        x = (w - tw) // 2
        d.text((x + 3, y + 3), t, font=f, fill=(0, 0, 0, 180))
        d.text((x, y), t, font=f, fill=c)
        y += heights[i] + gap
    wm = ImageFont.truetype(BOLD, 26)
    d.text((48, 44), "ATX LAKESCAPES", font=wm, fill=CREAM)
    d.text((48, h - 74), "254-780-6971", font=wm, fill=COPPER)
    return img


def main():
    os.makedirs(OUT, exist_ok=True)
    pins = []
    for slot, slug, prefix, bias, lines, why in CARDS:
        text = " ".join(t for t, _, _ in lines).upper()
        if any(cw in text for cw in COUNT_WORDS) and prefix not in C7_TWO_MACHINE:
            raise SystemExit(f"C7: {slot} claims a count over a non-verified plate")
        sha, im = load_upright(prefix)
        for tag, (w, h) in SIZES.items():
            plate = cover(im, w, h, bias).convert("RGBA")
            out = Image.alpha_composite(plate, strap(w, h, lines)).convert("RGB")
            out.save(os.path.join(OUT, f"DRAWDOWN_Card_{slot}_{slug}_{tag}.jpg"), quality=94)
        pins.append((slot, slug, sha, why))
        print(f"{slot} {slug:16s} {sha[:12]} {im.width}x{im.height} — {why}")
    with open(os.path.join(OUT, "PINS.md"), "w") as f:
        f.write("# Still-card series — pins\n\nBuilt by `build_plate_cards.py`. Every plate is a real ATX job photo, "
                "sha-pinned, orientation-guarded, eyeballed before the strap was written.\n\n"
                "| slot | slug | sha256 | why this plate | QC (claim · strap · orientation · crop) |\n|---|---|---|---|---|\n")
        for slot, slug, sha, why in pins:
            f.write(f"| {slot} | {slug} | `{sha}` | {why} | pending eye pass |\n")
    print(f"\nWROTE {len(pins)} cards x {len(SIZES)} crops → {OUT}")


if __name__ == "__main__":
    main()
