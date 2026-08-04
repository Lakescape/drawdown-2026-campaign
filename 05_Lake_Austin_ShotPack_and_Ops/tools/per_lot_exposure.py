#!/usr/bin/env python3
"""Per-lot exposed lakebed for a Lake Austin drawdown level.

METHOD NOTE — read before quoting any number to a homeowner.

Exposed lakebed lies BELOW the full-pool shoreline. Parcel boundaries generally
stop AT that shoreline, so the exposed ground is usually NOT inside the lot. A
naive "clip exposure to parcel polygon" returns ~zero for almost every property
and is the wrong question anyway.

So each exposed 25 ft cell is allocated to the NEAREST waterfront parcel, capped
at --max-dist feet. The output is therefore "exposed lakebed in front of this
lot", not "land you own that surfaces". Say it that way to customers. Where two
lots face each other across a narrow cove the midline splits them, which is the
sensible reading.

Bathymetry: TWDB 2008-12 survey (see per_zone_exposure.py for provenance and the
lake-wide QC against TWDB's elevation-area table).
Parcels: TCAD via City of Austin ArcGIS, EPSG:2277 — same CRS as the bathymetry,
so no reprojection of either.
"""
import argparse
import csv
import json
import os
import ssl
import urllib.parse
import urllib.request

import numpy as np
import shapefile
from pyproj import Transformer
from scipy.spatial import cKDTree
from shapely.geometry import Point, shape
from shapely.geometry import Polygon as ShPolygon
from shapely.prepared import prep
from shapely.strtree import STRtree

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "..", "data", "twdb-austin-2008")
OUT = os.path.join(HERE, "..", "ops")
PARCEL_CACHE = os.path.join(HERE, "..", "data", "tcad_waterfront_parcels.geojson")
LAYER = ("https://services.arcgis.com/0L95CJ0VTaxqcmED/ArcGIS/rest/services/"
         "EXTERNAL_tcad_parcel/FeatureServer/0")

FULL_POOL, FLOOR_2017, CELL_FT, ACRE = 492.04, 481.69, 25.0, 43560.0
SSL_CTX = ssl.create_default_context()
SSL_CTX.check_hostname = False
SSL_CTX.verify_mode = ssl.CERT_NONE


def post(url, data):
    req = urllib.request.Request(url, data=urllib.parse.urlencode(data).encode(),
                                 headers={"User-Agent": "Mozilla/5.0"})
    return json.loads(urllib.request.urlopen(req, timeout=180, context=SSL_CTX).read())


def fetch_parcels(lake, buffer_ft):
    """Waterfront parcels = those intersecting the lake polygon buffered outward."""
    if os.path.exists(PARCEL_CACHE):
        print("using cached parcels:", os.path.basename(PARCEL_CACHE))
        return json.load(open(PARCEL_CACHE))

    ring = lake.buffer(buffer_ft).simplify(20.0)
    geoms = [ring] if ring.geom_type == "Polygon" else list(ring.geoms)
    geom = {"rings": [list(g.exterior.coords) for g in geoms],
            "spatialReference": {"wkid": 2277}}
    feats, offset = [], 0
    while True:
        r = post(LAYER + "/query", {
            "where": "1=1", "geometry": json.dumps(geom),
            "geometryType": "esriGeometryPolygon", "inSR": "2277", "outSR": "2277",
            "spatialRel": "esriSpatialRelIntersects",
            "outFields": "PROP_ID,SITUS,LAND_VALUE,NBHD,ZONING,PID_10",
            "returnGeometry": "true", "f": "geojson",
            "resultOffset": str(offset), "resultRecordCount": "2000",
        })
        got = r.get("features", [])
        feats.extend(got)
        print(f"  fetched {len(feats):,}")
        if len(got) < 2000:
            break
        offset += 2000
    fc = {"type": "FeatureCollection", "features": feats}
    json.dump(fc, open(PARCEL_CACHE, "w"))
    return fc


ADDR_CACHE = os.path.join(HERE, "..", "data", "coa_waterfront_addresses.json")
ADDR_LAYER = ("https://services.arcgis.com/0L95CJ0VTaxqcmED/ArcGIS/rest/services/"
              "LOCATION_address_points/FeatureServer/0")


def fetch_addresses(lake, buffer_ft):
    if os.path.exists(ADDR_CACHE):
        return json.load(open(ADDR_CACHE))
    ring = lake.buffer(buffer_ft + 400).simplify(20.0)
    polys = [ring] if ring.geom_type == "Polygon" else list(ring.geoms)
    geom = {"rings": [list(g.exterior.coords) for g in polys],
            "spatialReference": {"wkid": 2277}}
    out, offset = [], 0
    while True:
        r = post(ADDR_LAYER + "/query", {
            "where": "1=1", "geometry": json.dumps(geom),
            "geometryType": "esriGeometryPolygon", "inSR": "2277", "outSR": "2277",
            "spatialRel": "esriSpatialRelIntersects",
            "outFields": "FULL_STREET_NAME", "returnGeometry": "true", "f": "json",
            "resultOffset": str(offset), "resultRecordCount": "2000",
        })
        got = r.get("features", [])
        for f in got:
            g = f.get("geometry") or {}
            if "x" in g:
                out.append({"x": g["x"], "y": g["y"],
                            "addr": (f["attributes"].get("FULL_STREET_NAME") or "").strip()})
        if len(got) < 2000:
            break
        offset += 2000
    json.dump(out, open(ADDR_CACHE, "w"))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--floor", type=float, default=FLOOR_2017)
    ap.add_argument("--pool", type=float, default=FULL_POOL)
    ap.add_argument("--cell", type=float, default=CELL_FT)
    ap.add_argument("--buffer", type=float, default=30.0,
                    help="ft outward from full-pool shoreline to catch adjacency")
    ap.add_argument("--max-dist", type=float, default=600.0,
                    help="ft; exposed cells farther than this from any lot are unallocated")
    ap.add_argument("--top", type=int, default=20)
    a = ap.parse_args()

    lr = shapefile.Reader(os.path.join(DATA, "Austin09_Lake08_stpl83"))
    lake = shape(lr.shape(0).__geo_interface__)
    sr = shapefile.Reader(os.path.join(DATA, "Austin2009_allpts4TIN_stpl83"))
    xy = np.asarray([s.points[0] for s in sr.shapes()])
    z = np.asarray([float(r[1]) for r in sr.records()])

    minx, miny, maxx, maxy = lake.bounds
    GX, GY = np.meshgrid(np.arange(minx, maxx, a.cell), np.arange(miny, maxy, a.cell))
    pts = np.column_stack([GX.ravel(), GY.ravel()])
    pl = prep(lake)
    pts = pts[np.fromiter((pl.contains(Point(p)) for p in pts), bool, len(pts))]
    bed = z[cKDTree(xy).query(pts, k=1)[1]]
    exposed = pts[(bed >= a.floor) & (bed < a.pool)]
    cell_area = a.cell ** 2
    print(f"exposed cells: {len(exposed):,}  = {len(exposed)*cell_area/ACRE:,.1f} acres\n")

    print("fetching TCAD waterfront parcels...")
    fc = fetch_parcels(lake, a.buffer)

    # Boundary vertices per parcel, densified so long straight edges stay near.
    verts, owner = [], []
    parcels = []
    for i, f in enumerate(fc["features"]):
        if not f.get("geometry"):
            continue
        g = shape(f["geometry"])
        polys = [g] if g.geom_type == "Polygon" else list(g.geoms)
        idx = len(parcels)
        p = f["properties"]
        parcels.append({
            "prop_id": p.get("PROP_ID"), "situs": (p.get("SITUS") or "").strip(),
            "land_value": p.get("LAND_VALUE"), "nbhd": p.get("NBHD"),
            "area_sqft": round(g.area), "cells": 0,
        })
        for poly in polys:
            line = poly.exterior
            n = max(int(line.length / 15.0), 8)
            for k in range(n):
                pt = line.interpolate(k / n, normalized=True)
                verts.append((pt.x, pt.y))
                owner.append(idx)
    print(f"parcels: {len(parcels):,}   boundary nodes: {len(verts):,}")

    dist, near = cKDTree(np.asarray(verts)).query(exposed, k=1)
    ok = dist <= a.max_dist
    for j in np.asarray(owner)[near[ok]]:
        parcels[j]["cells"] += 1
    print(f"allocated {ok.sum():,} of {len(exposed):,} exposed cells "
          f"({100*ok.sum()/len(exposed):.1f}%); "
          f"{(~ok).sum():,} beyond {a.max_dist:.0f} ft of any lot")

    # TCAD's public SITUS is only the house number, and LAND_VALUE comes back
    # empty, so join the city address points for a usable street address.
    print("\njoining addresses + zones...")
    addrs = fetch_addresses(lake, a.buffer)
    geoms = []
    for f in fc["features"]:
        if f.get("geometry"):
            geoms.append((shape(f["geometry"]), f))
    tree = STRtree([g for g, _ in geoms])
    fidx = {id(g): i for i, (g, _) in enumerate(geoms)}
    for ap_ in addrs:
        pt = Point(ap_["x"], ap_["y"])
        for hit in tree.query(pt):
            g = geoms[hit][0] if isinstance(hit, (int, np.integer)) else hit
            gi = hit if isinstance(hit, (int, np.integer)) else fidx[id(hit)]
            if g.contains(pt):
                parcels[gi].setdefault("addresses", []).append(ap_["addr"])
                break

    zones = json.load(open(os.path.join(OUT, "zones.geojson")))
    tf = Transformer.from_crs("EPSG:4326", "EPSG:2277", always_xy=True)
    zpolys = []
    for f in zones["features"]:
        g = shape(f["geometry"])
        zpolys.append((ShPolygon([tf.transform(x, y) for x, y in g.exterior.coords]),
                       f["properties"]))
    for i, (g, _) in enumerate(geoms):
        c = g.representative_point()
        for zg, zp in zpolys:
            if zg.contains(c):
                parcels[i]["zone"] = zp.get("zone_id")
                parcels[i]["zone_name"] = zp.get("name")
                parcels[i]["zone_tier"] = zp.get("value_tier")
                break

    rows = []
    for p in parcels:
        if not p["cells"]:
            continue
        sq = p["cells"] * cell_area
        ads = sorted(set(p.get("addresses", [])))
        rows.append({**{k: v for k, v in p.items() if k not in ("cells", "addresses")},
                     "address": ads[0] if ads else "",
                     "address_count": len(ads),
                     "exposed_sqft": int(sq), "exposed_acres": round(sq / ACRE, 3)})
    rows.sort(key=lambda r: -r["exposed_sqft"])
    named = sum(1 for r in rows if r["address"])
    print(f"  addresses matched on {named:,} of {len(rows):,} lots")

    print(f"\nlots with exposure: {len(rows):,}")
    print(f"{'situs':40} {'exposed sqft':>13} {'lot sqft':>10}")
    for r in rows[:a.top]:
        print(f"  {(r['situs'] or '(no situs)')[:38]:38} {r['exposed_sqft']:>13,} {r['area_sqft']:>10,}")

    sq = [r["exposed_sqft"] for r in rows]
    print(f"\nmedian {int(np.median(sq)):,} sqft   mean {int(np.mean(sq)):,}   max {max(sq):,}")

    dest = os.path.join(OUT, f"lot_exposure_{a.floor:.0f}ft.json")
    json.dump({"floor_ft": a.floor, "pool_ft": a.pool, "cell_ft": a.cell,
               "max_alloc_dist_ft": a.max_dist,
               "method": "exposed cells allocated to nearest waterfront parcel; "
                         "represents lakebed IN FRONT OF the lot, not land the owner holds",
               "lots": rows}, open(dest, "w"), indent=2)
    with open(dest.replace(".json", ".csv"), "w", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print("wrote", os.path.basename(dest), "+ .csv")


if __name__ == "__main__":
    main()
