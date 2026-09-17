#!/usr/bin/env python3
"""
Earth Pro KML → bid-ready quantities.

Draw in Google Earth Pro, export KML, run this. Turns polygons into square feet
and sediment cubic yards, and paths into linear feet of bulkhead/seawall — the
three numbers ATX actually bids off.

    python3 kml_measure.py <file.kml> [--depth-ft 4.5] [--csv out.csv]

Polygons  -> area (sq ft) + sediment volume at the given depth (cubic yards)
LineStrings -> length (linear ft), for bulkhead / seawall / tie-back runs

Permit posture is evaluated on every volume, because it is the single biggest
scope-and-price driver on drawdown work.

    < 25 cy    City of Austin allows without a variance — LDC 25-8-261(C)(9)(a).
               This is the binding ceiling on Lake Austin.
    > 25 cy    City variance required, AND separate LCRA HLDO authorization.
    > 500 cy   LCRA HLDO Tier II individual permit (also >500 LF disturbed).

CORRECTED 2026-08-05. Earlier versions of this tool encoded a "2,000 cy LCRA
Lakewide Permit" ceiling. That was WRONG and is retracted — see
ATX-Jobs/2026-2708-scenic-williams/20-analysis/PERMIT-AUTHORITY-v2-2026-08-04.md
section 3. The 2,000 cy figure comes from a lake-lowering registration model on
LCRA-OPERATED lakes (Inks Lake). LCRA's published lakewide permits cover Lake
Buchanan and Lake Travis ONLY. Lake Austin is a City lake and is not on them.
There is no confirmed 2,000 cy path on Lake Austin.

Open question that can override all of the above: LCRA HLDO Tier I carves out
"commercial dredge and fill activity" verbatim. ATX performing work for hire may
be excluded from the Tier I shortcut even under 500 cy, forcing Tier II on
routine jobs. Unresolved - call LCRA Water Quality 512-578-2324.

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

# Permit thresholds, cubic yards. See module docstring for sources and the
# 2026-08-05 correction that removed the retracted 2,000 cy figure.
COA_NO_VARIANCE_CEILING_CY = 25  # LDC 25-8-261(C)(9)(a) — binding on Lake Austin
HLDO_TIER_II_CY = 500  # LCRA HLDO: above this, individual Tier II permit


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
    if cy < COA_NO_VARIANCE_CEILING_CY:
        return "City OK without variance (under 25 cy, LDC 25-8-261(C)(9)(a)); LCRA HLDO still applies"
    if cy <= HLDO_TIER_II_CY:
        return (
            f"CITY VARIANCE REQUIRED — {cy:,.0f} cy is over the 25 cy no-variance ceiling. "
            "Plus LCRA HLDO authorization. Tier I may be unavailable: the ordinance carves out "
            "'commercial dredge and fill activity' and ATX works for hire — unresolved"
        )
    return (
        f"LCRA HLDO TIER II — {cy:,.0f} cy exceeds 500 cy, individual permit required, "
        "plus City variance. Do not bid as routine"
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
    if total_cy > HLDO_TIER_II_CY:
        print(
            f"\n!! {total_cy:,.0f} cy total exceeds the 500 cy LCRA HLDO Tier II line. "
            "Individual permit plus City variance — escalate before quoting."
        )
    elif total_cy >= COA_NO_VARIANCE_CEILING_CY:
        print(
            f"\n!! {total_cy:,.0f} cy total is over the City's 25 cy no-variance ceiling. "
            "Bid it as a variance-contingent clause with a <25 cy fallback, not a flat number."
        )

    if lines:
        total_lf = sum(r["linear_ft"] for r in lines)
        if total_lf > 500:
            print(
                f"\n!! {total_lf:,.0f} LF of shoreline disturbed exceeds the 500 LF "
                "HLDO Tier II line independently of volume."
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

    # Permit boundaries. The 2,000 cy figure is retracted — assert it is gone,
    # so a re-introduction fails loudly instead of quietly shipping a wrong ceiling.
    assert "without variance" in permit_note(24)
    assert "CITY VARIANCE REQUIRED" in permit_note(400)
    assert "TIER II" in permit_note(2500)
    assert "TIER II" in permit_note(501)
    for cy in (24, 400, 501, 2500):
        assert "2,000" not in permit_note(cy), "retracted 2,000 cy ceiling reintroduced"

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
