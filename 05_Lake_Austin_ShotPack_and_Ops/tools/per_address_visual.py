#!/usr/bin/env python3
"""Per-address drawdown visual renderer (ATX-2156 proof of concept).

Takes a Lake Austin waterfront address (or prop_id) and produces a sales-ready
image: the caller's own lot boundary beside the true 2017 drawdown aerial frame
for its zone, with an exposed-area callout and a hedged caption.

Render method — inset, not overlay: the 2017 frames are Google Earth Pro screen
grabs taken at a tilted LookAt (see tools/capture_2017_frames.py). Their
pixel-to-ground mapping is a perspective projection that is not recoverable
from repo data, so exact georegistration is not provable. We therefore draw the
TCAD parcel boundary as an inset map panel beside the aerial frame and say so
on the image. Honesty over flash: the boundary is never warped onto the aerial.

Every number on the image comes from ops/lot_exposure_482ft.csv / .json
(floor_ft, pool_ft, per-lot exposed acres). Nothing is recomputed here.

Usage:
    python3 per_address_visual.py "1500 1/2 CITY PARK RD"
    python3 per_address_visual.py --prop-id 130505
    python3 per_address_visual.py "2215 WESTLAKE DR" --data-root /path/to/05_Lake_Austin_ShotPack_and_Ops

Exit codes: 0 rendered (including the zone-level fallback), 1 address not
found, 2 zone frame not found.
"""
import argparse
import csv
import difflib
import json
import os
import re
import sys

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.abspath(os.path.join(HERE, ".."))

# Campaign palette / type
BG = (247, 245, 240)        # #f7f5f0
INK = (26, 26, 26)          # #1a1a1a
GOLD = (196, 146, 58)       # #c4923a
GOLD_FILL = (243, 233, 215)  # gold at ~15% over white (<=20% fill rule)
CARD = (255, 255, 255)
MUTED = (110, 104, 94)

HEDGED_LINE = ("January\u2013February 2017 drawdown conditions. "
               "The 2026 window is projected, not confirmed.")
PENDING_LABEL = "Zone-level view \u2014 parcel boundary pending"

USER_FONTS = os.path.expanduser("~/Library/Fonts")
SERIF = [
    os.path.join(USER_FONTS, "CormorantGaramond[wght].ttf"),
    "/System/Library/Fonts/Times.ttc",
]
SANS = [
    os.path.join(USER_FONTS, "SourceSans3[wght].ttf"),
    "/System/Library/Fonts/Helvetica.ttc",
]


def load_font(candidates, size, weight=None):
    for path in candidates:
        if os.path.exists(path):
            try:
                font = ImageFont.truetype(path, size)
                if weight is not None:
                    try:
                        font.set_variation_by_axes([weight])
                    except Exception:
                        pass
                return font
            except Exception:
                continue
    return ImageFont.load_default()


def norm_addr(s):
    return re.sub(r"\s+", " ", s.strip().upper())


def slugify(s):
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return re.sub(r"-{2,}", "-", s)


def title_addr(s):
    # "1500 1/2 CITY PARK RD" -> "1500 1/2 City Park Rd"
    return " ".join(w.capitalize() if not w[0].isdigit() else w
                    for w in s.lower().split(" "))


def load_lots(data_root):
    with open(os.path.join(data_root, "ops", "lot_exposure_482ft.csv"),
              newline="") as fh:
        return list(csv.DictReader(fh))


def load_meta(data_root):
    with open(os.path.join(data_root, "ops", "lot_exposure_482ft.json")) as fh:
        j = json.load(fh)
    return {k: j[k] for k in ("floor_ft", "pool_ft")}


def find_lot(lots, address=None, prop_id=None):
    if prop_id is not None:
        for r in lots:
            if r["prop_id"] == str(prop_id):
                return r
        return None
    want = norm_addr(address)
    for r in lots:
        if r["address"].strip() and norm_addr(r["address"]) == want:
            return r
    return None


def find_parcel(data_root, prop_id):
    with open(os.path.join(data_root, "data",
                           "tcad_waterfront_parcels.geojson")) as fh:
        g = json.load(fh)
    for f in g["features"]:
        if str(f["properties"].get("PROP_ID")) == str(prop_id):
            return f["geometry"]
    return None


def iter_rings(coords):
    """Yield linear rings from Polygon/MultiPolygon-style coordinates,
    tolerating the extra nesting level present in the TCAD export."""
    if not coords:
        return
    first = coords[0]
    if isinstance(first, (list, tuple)) and len(first) >= 2 and \
            isinstance(first[0], (int, float)):
        yield coords
    else:
        for sub in coords:
            yield from iter_rings(sub)


def find_zone_frame(data_root, lot):
    """Zone frame = screenshots-2017/tier-<tier>/<CODE>-*.png, where CODE is
    the leading token of zone_name ('N8 \u00b7 Greenshores...' -> 'N8')."""
    code = lot["zone_name"].split("\u00b7")[0].strip()
    shots = os.path.join(data_root, "shot-pack", "screenshots-2017")
    candidates = [os.path.join(shots, f"tier-{lot['zone_tier']}"), shots]
    for d in candidates:
        if not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            if name.startswith(code + "-") and name.endswith(".png"):
                return os.path.join(d, name)
    # last resort: any tier dir
    for tier in ("tier-A", "tier-B", "tier-C", "tier-coves", "tier-overview"):
        d = os.path.join(shots, tier)
        if os.path.isdir(d):
            for name in sorted(os.listdir(d)):
                if name.startswith(code + "-") and name.endswith(".png"):
                    return os.path.join(d, name)
    return None


def draw_inset(draw, card_box, geometry, prop_id, lot, meta, fonts):
    x0, y0, x1, y1 = card_box
    draw.rectangle(card_box, fill=CARD, outline=GOLD, width=3)
    pad = 28
    cx = x0 + pad
    cy = y0 + pad
    f_small, f_tiny, f_stat, f_statlbl = fonts

    draw.text((cx, cy), "PARCEL BOUNDARY (TCAD)", font=f_small, fill=GOLD)
    cy += 54

    # Map area
    map_box = (cx, cy, x1 - pad, y1 - 300)
    draw.rectangle(map_box, fill=BG, outline=(220, 214, 202), width=2)

    rings = [r for r in iter_rings(geometry["coordinates"]) if len(r) >= 3]
    xs = [p[0] for r in rings for p in r]
    ys = [p[1] for r in rings for p in r]
    minx, maxx, miny, maxy = min(xs), max(xs), min(ys), max(ys)
    spanx = max(maxx - minx, 1e-9)
    spany = max(maxy - miny, 1e-9)
    mw = map_box[2] - map_box[0] - 2 * pad
    mh = map_box[3] - map_box[1] - 2 * pad
    scale = min(mw / spanx, mh / spany)
    ox = map_box[0] + pad + (mw - spanx * scale) / 2
    oy = map_box[1] + pad + (mh - spany * scale) / 2

    def to_px(p):
        # State-plane feet, Y north-up -> screen Y down
        return (ox + (p[0] - minx) * scale, oy + (maxy - p[1]) * scale)

    for i, ring in enumerate(rings):
        pts = [to_px(p) for p in ring]
        if i == 0:
            draw.polygon(pts, fill=GOLD_FILL)
        draw.line(pts + [pts[0]], fill=GOLD, width=5, joint="curve")

    # North marker
    nx, ny = map_box[2] - pad - 8, map_box[1] + 14
    draw.text((nx, ny), "N \u2191", font=f_tiny, fill=MUTED)

    ty = map_box[3] + 22
    draw.text((cx, ty), f"Prop ID {prop_id}", font=f_tiny, fill=MUTED)
    ty += 34
    draw.text((cx, ty), "Inset for location reference \u2014 the aerial",
              font=f_tiny, fill=MUTED)
    draw.text((cx, ty + 26), "frame is not georectified.",
              font=f_tiny, fill=MUTED)

    # Exposed-area callout: number straight from lot_exposure, never computed
    acres = float(lot["exposed_acres"])
    inner_w = x1 - pad - cx
    sy = y1 - 185
    draw.text((cx, sy), f"{acres:.2f}", font=f_stat, fill=GOLD)
    w = draw.textlength(f"{acres:.2f}", font=f_stat)
    draw.text((cx + w + 14, sy + 44), "ACRES EXPOSED", font=f_statlbl, fill=INK)
    draw.text((cx, sy + 108), "lakebed in front of lot", font=f_tiny, fill=MUTED)
    sub = (f"drawdown floor {meta['floor_ft']:.2f} ft \u00b7 "
           f"full pool {meta['pool_ft']:.2f} ft")
    f_sub2 = f_tiny
    if draw.textlength(sub, font=f_sub2) > inner_w:
        f_sub2 = load_font(SANS, 22, weight=400)
    draw.text((cx, sy + 140), sub, font=f_sub2, fill=MUTED)


def render(lot, geometry, frame_path, meta, out_path):
    W, H = 2560, 1600
    img = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(img)

    f_title = load_font(SERIF, 76, weight=600)
    f_sub = load_font(SANS, 36, weight=400)
    f_hedge = load_font(SANS, 32, weight=400)
    f_small = load_font(SANS, 30, weight=600)
    f_tiny = load_font(SANS, 26, weight=400)
    f_stat = load_font(SERIF, 96, weight=600)
    f_statlbl = load_font(SANS, 30, weight=600)
    f_framelbl = load_font(SANS, 26, weight=400)

    margin = 60
    cap_top = H - 300

    frame = Image.open(frame_path).convert("RGB")

    aerial_region = (margin, margin, 1820, cap_top - 70)
    card_box = (1880, margin, W - margin, cap_top - 70)

    # Aerial frame, aspect-preserved, thin ink border
    rw = aerial_region[2] - aerial_region[0]
    rh = aerial_region[3] - aerial_region[1]
    scale = min(rw / frame.width, rh / frame.height)
    fw, fh = int(frame.width * scale), int(frame.height * scale)
    frame = frame.resize((fw, fh), Image.LANCZOS)
    fx = aerial_region[0] + (rw - fw) // 2
    fy = aerial_region[1] + (rh - fh) // 2
    img.paste(frame, (fx, fy))
    draw.rectangle((fx - 2, fy - 2, fx + fw + 1, fy + fh + 1),
                   outline=INK, width=2)
    draw.text((fx, fy + fh + 14),
              "Zone context frame \u2014 2017 drawdown aerial",
              font=f_framelbl, fill=MUTED)

    if geometry is not None:
        draw_inset(draw, card_box, geometry, lot["prop_id"], lot, meta,
                   (f_small, f_tiny, f_stat, f_statlbl))
    else:
        # Fallback: never fabricate a boundary
        draw.rectangle(card_box, fill=CARD, outline=GOLD, width=3)
        label = PENDING_LABEL
        f_pend = f_sub
        inner_w = card_box[2] - card_box[0] - 56
        if draw.textlength(label, font=f_pend) > inner_w:
            f_pend = load_font(SANS, 28, weight=400)
        lw = draw.textlength(label, font=f_pend)
        draw.text(((card_box[0] + card_box[2] - lw) / 2,
                   (card_box[1] + card_box[3]) / 2 - 20),
                  label, font=f_pend, fill=INK)

    # Caption bar
    draw.line((margin, cap_top, W - margin, cap_top), fill=GOLD, width=4)
    ty = cap_top + 34
    draw.text((margin, ty), title_addr(lot["address"].strip() or lot["situs"].strip() or f"Prop {lot['prop_id']}"),
              font=f_title, fill=INK)
    ty += 100
    draw.text((margin, ty),
              f"{lot['zone_name']}  \u00b7  Tier {lot['zone_tier']}",
              font=f_sub, fill=INK)
    ty += 62
    draw.text((margin, ty), HEDGED_LINE, font=f_hedge, fill=MUTED)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    img.save(out_path, "PNG")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("address", nargs="?", help="situs address, e.g. \"1500 1/2 CITY PARK RD\"")
    ap.add_argument("--prop-id", help="TCAD prop_id (overrides address)")
    ap.add_argument("--data-root", default=PACK,
                    help="path to 05_Lake_Austin_ShotPack_and_Ops holding the inputs "
                         "(default: this repo's copy)")
    ap.add_argument("--out-dir",
                    default=os.path.join(PACK, "shot-pack", "per-address-proof"),
                    help="output folder (default: shot-pack/per-address-proof)")
    args = ap.parse_args()

    if not args.address and not args.prop_id:
        ap.error("give an address or --prop-id")

    lots = load_lots(args.data_root)
    meta = load_meta(args.data_root)
    lot = find_lot(lots, address=args.address, prop_id=args.prop_id)
    if lot is None:
        what = f"prop_id {args.prop_id}" if args.prop_id else f"address {args.address!r}"
        print(f"error: {what} not found in lot_exposure_482ft.csv", file=sys.stderr)
        if args.address:
            known = [r["address"].strip() for r in lots if r["address"].strip()]
            close = difflib.get_close_matches(norm_addr(args.address), known, n=3)
            if close:
                print("closest matches:", file=sys.stderr)
                for c in close:
                    print(f"  {c}", file=sys.stderr)
        return 1

    frame_path = find_zone_frame(args.data_root, lot)
    if frame_path is None:
        print(f"error: no 2017 frame found for zone {lot['zone']} "
              f"({lot['zone_name']})", file=sys.stderr)
        return 2

    geometry = find_parcel(args.data_root, lot["prop_id"])
    if geometry is None:
        print(f"note: parcel {lot['prop_id']} not in TCAD geojson \u2014 "
              f"rendering zone-level fallback", file=sys.stderr)

    street = lot["address"].strip() or f"prop-{lot['prop_id']}"
    out_name = f"PROOF_{lot['zone']}_{slugify(street)}.png"
    out_path = os.path.join(args.out_dir, out_name)
    render(lot, geometry, frame_path, meta, out_path)

    method = "inset" if geometry is not None else "zone-fallback"
    print(f"ok: {out_path}  [{method}; frame={os.path.basename(frame_path)}]")
    return 0


if __name__ == "__main__":
    sys.exit(main())
