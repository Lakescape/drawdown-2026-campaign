#!/usr/bin/env python3
"""Per-zone exposed lakebed for a given Lake Austin drawdown level.

Lidar cannot answer this — USGS 3DEP was flown at full pool and has zero returns
below 481.69 ft. The bathymetry comes from TWDB's 2008-12 volumetric survey:
41,429 sounding points with elevations, plus the full-pool shoreline polygon
whose area (69,234,398 sq ft = 1,589 acres) matches TWDB's published table
exactly, which is the check that the file is what it claims to be.

Method: nearest-neighbour interpolate the soundings onto a 25 ft grid clipped to
the lake polygon, then per zone count cells whose bed elevation falls between the
floor and the pre-drawdown pool. Grid is 25 ft against ~41 ft mean sounding
spacing, so cells are finer than the data — the limit is survey density, not the
grid.

Self-check: the lake-wide total must land near TWDB's elevation-area table
(523.5 acres between 481.69 and 492.04 ft). The script prints the ratio; treat a
large divergence as a defect, not a result.

CRS note: shapefiles are NAD83 State Plane Texas Central FIPS 4203, US survey
FEET (EPSG:2277). zones.geojson is WGS84 and gets reprojected.
"""
import argparse
import json
import os

import numpy as np
import shapefile
from pyproj import Transformer
from scipy.spatial import cKDTree
from shapely.geometry import Polygon, shape
from shapely.prepared import prep

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data", "twdb-austin-2008")
ZONES = os.path.join(HERE, "..", "ops", "zones.geojson")
OUT = os.path.join(HERE, "..", "ops")

FULL_POOL = 492.04     # pre-drawdown, 2016-12-28
FLOOR_2017 = 481.69    # 2017-01-13
CELL_FT = 25.0
ACRE_SQFT = 43560.0
TWDB_EXPECTED_ACRES = 523.5


def load_lake():
    r = shapefile.Reader(os.path.join(DATA, "Austin09_Lake08_stpl83"))
    poly = shape(r.shape(0).__geo_interface__)
    return poly, r.record(0)[0]


def load_soundings():
    r = shapefile.Reader(os.path.join(DATA, "Austin2009_allpts4TIN_stpl83"))
    xy, z = [], []
    for sh, rec in zip(r.shapes(), r.records()):
        p = sh.points[0]
        xy.append((p[0], p[1]))
        z.append(float(rec[1]))
    return np.asarray(xy), np.asarray(z)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--floor", type=float, default=FLOOR_2017,
                    help="drawdown floor elevation, ft MSL")
    ap.add_argument("--pool", type=float, default=FULL_POOL,
                    help="pre-drawdown pool elevation, ft MSL")
    ap.add_argument("--cell", type=float, default=CELL_FT)
    a = ap.parse_args()

    lake, lake_elev = load_lake()
    xy, z = load_soundings()
    print(f"lake polygon @ {lake_elev} ft   {lake.area/ACRE_SQFT:,.1f} acres")
    print(f"soundings: {len(z):,}   bed elevation {z.min():.1f}..{z.max():.1f} ft")
    print(f"band: {a.floor} -> {a.pool} ft   grid {a.cell:.0f} ft\n")

    minx, miny, maxx, maxy = lake.bounds
    gx = np.arange(minx, maxx, a.cell)
    gy = np.arange(miny, maxy, a.cell)
    GX, GY = np.meshgrid(gx, gy)
    pts = np.column_stack([GX.ravel(), GY.ravel()])

    # keep only cells inside the reservoir
    pl = prep(lake)
    from shapely.geometry import Point
    inside = np.fromiter((pl.contains(Point(p)) for p in pts), bool, len(pts))
    pts_in = pts[inside]
    print(f"grid cells in lake: {inside.sum():,}  "
          f"({inside.sum()*a.cell**2/ACRE_SQFT:,.1f} acres)")

    bed = z[cKDTree(xy).query(pts_in, k=1)[1]]
    exposed = (bed >= a.floor) & (bed < a.pool)
    cell_area = a.cell ** 2
    total_ac = exposed.sum() * cell_area / ACRE_SQFT
    ratio = total_ac / TWDB_EXPECTED_ACRES
    print(f"lake-wide exposed: {total_ac:,.1f} acres   "
          f"(TWDB table {TWDB_EXPECTED_ACRES}, ratio {ratio:.2f})")
    if not 0.75 < ratio < 1.35:
        print("  !! diverges from TWDB — treat per-zone numbers as indicative only")

    zones = json.load(open(ZONES))
    tf = Transformer.from_crs("EPSG:4326", "EPSG:2277", always_xy=True)
    rows = []
    for f in zones["features"]:
        g = shape(f["geometry"])
        zp = Polygon([tf.transform(x, y) for x, y in g.exterior.coords])
        pz = prep(zp)
        sel = np.fromiter((pz.contains(Point(p)) for p in pts_in), bool, len(pts_in))
        if not sel.any():
            continue
        water_ac = sel.sum() * cell_area / ACRE_SQFT
        exp_ac = (sel & exposed).sum() * cell_area / ACRE_SQFT
        p = f["properties"]
        rows.append({
            "zone_id": p.get("zone_id"), "name": p.get("name"),
            "shore": p.get("shore"), "tier": p.get("value_tier"),
            "full_pool_water_acres": round(water_ac, 1),
            "exposed_acres": round(exp_ac, 1),
            "pct_of_zone_water_exposed": round(100 * exp_ac / water_ac, 1) if water_ac else 0.0,
            "exposed_sqft": int(exp_ac * ACRE_SQFT),
        })

    rows.sort(key=lambda r: -r["exposed_acres"])
    print(f"\n{'zone':44} {'tier':>4} {'water ac':>9} {'exposed ac':>11} {'%':>6}")
    for r in rows[:14]:
        print(f"  {r['name'][:42]:42} {r['tier']:>4} "
              f"{r['full_pool_water_acres']:>9.1f} {r['exposed_acres']:>11.1f} "
              f"{r['pct_of_zone_water_exposed']:>6.1f}")
    print(f"\nzones with water: {len(rows)}   "
          f"sum exposed {sum(r['exposed_acres'] for r in rows):,.1f} acres")

    out = {
        "floor_ft": a.floor, "pool_ft": a.pool, "drop_ft": round(a.pool - a.floor, 2),
        "grid_ft": a.cell, "source": "TWDB 2008-12 volumetric survey (soundings + lake polygon)",
        "lakewide_exposed_acres": round(total_ac, 1),
        "twdb_table_acres": TWDB_EXPECTED_ACRES, "qc_ratio": round(ratio, 3),
        "zones": rows,
    }
    dest = os.path.join(OUT, f"zone_exposure_{a.floor:.0f}ft.json")
    json.dump(out, open(dest, "w"), indent=2)
    print("wrote", os.path.basename(dest))


if __name__ == "__main__":
    main()
