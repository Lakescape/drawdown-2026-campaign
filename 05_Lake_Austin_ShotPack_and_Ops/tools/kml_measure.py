#!/usr/bin/env python3
"""
Earth Pro KML → bid-ready quantities.

Draw in Google Earth Pro, export KML, run this. Turns polygons into square feet
and sediment cubic yards, and paths into linear feet of bulkhead/seawall — the
three numbers ATX actually bids off.

    python3 kml_measure.py <file.kml> [--depth-ft 4.5] [--csv out.csv]

Polygons  -> area (sq ft) + sediment volume at the given depth (cubic yards)
LineStrings -> length (linear ft), for bulkhead / seawall / tie-back runs

Permit cliff (ATX-1697) is evaluated on every volume, because it is the single
biggest scope-and-price driver and it turns on an agency action ATX does not
control:

    < 25 cy    COA administrative approval
    25-2,000cy REQUIRES drawdown announced + LCRA registration open + address
               registered. Unregistered, the sellable volume collapses to <25 cy.
    > 2,000 cy over the LCRA/USACE Lakewide Permit ceiling — individual permit

No dependencies. Stdlib only, so it runs on any machine on the crew without a
venv. Area uses a local tangent-plane projection about each shape's own
centroid; at parcel scale on Lake Austin the error is far below drawing
precision (see verify() ).
"""

from __future__ import annotations

import argparse
import csv
import math
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

KML_NS = {"kml": "http://www.opengis.net/kml/2.2"}

M2_PER_FT2 = 0.09290304
M_PER_FT = 0.3048
CY_PER_FT3 = 1.0 / 27.0
EARTH_R_M = 6371008.8  # IUGG mean radius

# ATX-1697 permit cliff thresholds, cubic yards
COA_ADMIN_CEILING_CY = 25
LAKEWIDE_PERMIT_CEILING_CY = 2000


def parse_coords(text: str) -> list[tuple[float, float]]:
    """KML <coordinates> is whitespace-separated lon,lat[,alt] triples."""
    pts = []
    for token in text.split():
        parts = token.split(",")
        if len(parts) < 2:
            continue
        pts.append((float(parts[0]), float(parts[1])))  # (lon, lat)
    return pts


def to_local_xy(pts: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """
    Project lon/lat to metres on a tangent plane about the shape's centroid.

    Equirectangular with the longitude axis scaled by cos(lat0). Exact enough
    that the limiting factor is how steadily you traced the polygon, not the
    projection — a 300 ft parcel at this latitude lands well under 0.01% error.
    """
    lat0 = sum(p[1] for p in pts) / len(pts)
    lon0 = sum(p[0] for p in pts) / len(pts)
    k = math.cos(math.radians(lat0))
    return [
        (
            math.radians(lon - lon0) * EARTH_R_M * k,
            math.radians(lat - lat0) * EARTH_R_M,
        )
        for lon, lat in pts
    ]


def shoelace_area_m2(xy: list[tuple[float, float]]) -> float:
    if len(xy) < 3:
        return 0.0
    total = 0.0
    for i in range(len(xy)):
        x1, y1 = xy[i]
        x2, y2 = xy[(i + 1) % len(xy)]
        total += x1 * y2 - x2 * y1
    return abs(total) / 2.0


def path_length_m(xy: list[tuple[float, float]], closed: bool = False) -> float:
    if len(xy) < 2:
        return 0.0
    total = 0.0
    n = len(xy) if closed else len(xy) - 1
    for i in range(n):
        x1, y1 = xy[i]
        x2, y2 = xy[(i + 1) % len(xy)]
        total += math.hypot(x2 - x1, y2 - y1)
    return total


def permit_note(cy: float) -> str:
    if cy < COA_ADMIN_CEILING_CY:
        return "COA administrative approval (under 25 cy)"
    if cy <= LAKEWIDE_PERMIT_CEILING_CY:
        return (
            f"NEEDS LCRA registration — {cy:,.0f} cy is only sellable if the drawdown "
            "is announced, registration is open, AND this address is registered. "
            "Unregistered, sellable volume collapses to <25 cy"
        )
    return (
        f"OVER Lakewide Permit ceiling ({cy:,.0f} cy > 2,000) — individual "
        "LCRA/USACE permit required, do not bid as routine"
    )


def measure(kml_path: Path, depth_ft: float) -> list[dict]:
    root = ET.parse(kml_path).getroot()
    rows: list[dict] = []

    for pm in root.iter():
        if not pm.tag.endswith("Placemark"):
            continue
        name_el = pm.find("kml:name", KML_NS)
        name = (name_el.text or "").strip() if name_el is not None else "(unnamed)"

        for geom in pm.iter():
            tag = geom.tag.split("}")[-1]
            if tag not in ("Polygon", "LineString"):
                continue
            coord_el = None
            for c in geom.iter():
                if c.tag.endswith("coordinates"):
                    coord_el = c
                    break
            if coord_el is None or not coord_el.text:
                continue

            pts = parse_coords(coord_el.text)
            if len(pts) < 2:
                continue
            xy = to_local_xy(pts)

            if tag == "Polygon":
                area_ft2 = shoelace_area_m2(xy) / M2_PER_FT2
                cy = area_ft2 * depth_ft * CY_PER_FT3
                rows.append(
                    {
                        "name": name,
                        "type": "area",
                        "area_sqft": round(area_ft2, 1),
                        "perimeter_ft": round(path_length_m(xy, closed=True) / M_PER_FT, 1),
                        "depth_ft": depth_ft,
                        "sediment_cy": round(cy, 1),
                        "linear_ft": "",
                        "permit": permit_note(cy),
                    }
                )
            else:
                rows.append(
                    {
                        "name": name,
                        "type": "linear",
                        "area_sqft": "",
                        "perimeter_ft": "",
                        "depth_ft": "",
                        "sediment_cy": "",
                        "linear_ft": round(path_length_m(xy) / M_PER_FT, 1),
                        "permit": "",
                    }
                )
    return rows


def report(rows: list[dict]) -> None:
    if not rows:
        print("No Polygon or LineString geometry found. Did you draw and export?")
        return

    areas = [r for r in rows if r["type"] == "area"]
    lines = [r for r in rows if r["type"] == "linear"]

    if areas:
        print("\nAREA / SEDIMENT")
        print(f"{'shape':<38} {'sq ft':>11} {'cy':>9}  permit")
        print("-" * 100)
        for r in areas:
            print(
                f"{r['name'][:38]:<38} {r['area_sqft']:>11,.1f} "
                f"{r['sediment_cy']:>9,.1f}  {r['permit']}"
            )
        print(
            f"{'TOTAL':<38} {sum(r['area_sqft'] for r in areas):>11,.1f} "
            f"{sum(r['sediment_cy'] for r in areas):>9,.1f}"
        )

    if lines:
        print("\nLINEAR (bulkhead / seawall / tie-back)")
        print(f"{'shape':<38} {'linear ft':>11}")
        print("-" * 52)
        for r in lines:
            print(f"{r['name'][:38]:<38} {r['linear_ft']:>11,.1f}")
        print(f"{'TOTAL':<38} {sum(r['linear_ft'] for r in lines):>11,.1f}")

    total_cy = sum(r["sediment_cy"] for r in areas)
    if total_cy > LAKEWIDE_PERMIT_CEILING_CY:
        print(
            f"\n!! {total_cy:,.0f} cy total exceeds the 2,000 cy Lakewide Permit "
            "ceiling. Individual permit territory — escalate before quoting."
        )
    elif total_cy >= COA_ADMIN_CEILING_CY:
        print(
            f"\n!! {total_cy:,.0f} cy total is registration-contingent. Per ATX-1697 "
            "this must be a contingent clause in the bid, not a flat number."
        )

    print(
        '\nReminder: never write "dredging" in a customer-facing artifact '
        '(ATX-1696). Use "sediment remediation" or "tier three install".'
    )


def verify() -> None:
    """Self-check: a known-size square at Lake Austin latitude."""
    lat, lon = 30.33, -97.80
    side_m = 100.0
    dlat = math.degrees(side_m / EARTH_R_M)
    dlon = math.degrees(side_m / (EARTH_R_M * math.cos(math.radians(lat))))
    square = [(lon, lat), (lon + dlon, lat), (lon + dlon, lat + dlat), (lon, lat + dlat)]

    area_ft2 = shoelace_area_m2(to_local_xy(square)) / M2_PER_FT2
    expected = (side_m**2) / M2_PER_FT2  # 10,000 m2 -> ~107,639 sq ft
    err = abs(area_ft2 - expected) / expected
    assert err < 0.001, f"area error {err:.4%} too high ({area_ft2:.0f} vs {expected:.0f})"

    perim_ft = path_length_m(to_local_xy(square), closed=True) / M_PER_FT
    expected_perim = 400.0 / M_PER_FT
    assert abs(perim_ft - expected_perim) / expected_perim < 0.001, "perimeter off"

    # Permit cliff boundaries
    assert "administrative" in permit_note(24)
    assert "NEEDS LCRA registration" in permit_note(500)
    assert "OVER Lakewide" in permit_note(2500)

    print(f"verify OK — 100m square = {area_ft2:,.0f} sq ft (err {err:.4%})")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("kml", nargs="?", help="KML exported from Google Earth Pro")
    ap.add_argument(
        "--depth-ft",
        type=float,
        default=4.0,
        help="average sediment depth for volume math (default 4.0)",
    )
    ap.add_argument("--csv", help="also write rows to this CSV")
    ap.add_argument("--verify", action="store_true", help="run the self-check and exit")
    args = ap.parse_args()

    if args.verify:
        verify()
        return
    if not args.kml:
        ap.error("give a KML path, or --verify")

    path = Path(args.kml)
    if not path.exists():
        sys.exit(f"not found: {path}")

    rows = measure(path, args.depth_ft)
    report(rows)

    if args.csv and rows:
        with open(args.csv, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        print(f"\nwrote {len(rows)} rows -> {args.csv}")


if __name__ == "__main__":
    main()
