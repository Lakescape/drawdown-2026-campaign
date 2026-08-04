#!/usr/bin/env python3
"""Quantify the land Lake Austin's 2017 drawdown actually exposed.

The eyeball test on true-colour Sentinel-2 fails: Lake Austin is a steep-sided
river-canyon reservoir, so a 10 ft drop uncovers a horizontal band only a few
metres wide over much of its length — 1-3 pixels at 10 m GSD. That is a geometry
fact about the lake, not a defect in the imagery, and it means the "dramatic
aerial before/after" the campaign assumed exists may not exist at wide scale.

So measure instead of squint. NDWI = (green - nir) / (green + nir); water is
NDWI > threshold. Land exposed by the drawdown = water at full pool AND NOT
water at the floor. Report it in acres and render it highlighted.

Scenes (both 0.06% cloud, same season, verified levels from TWDB):
  2017-01-30  481.98 ft  drawdown floor
  2018-02-04  492.08 ft  full pool
  delta 10.10 ft
"""
import json
import os
import ssl
import urllib.request

import numpy as np
import rasterio
from PIL import Image
from pyproj import Transformer
from rasterio.windows import from_bounds

STAC = "https://earth-search.aws.element84.com/v1/search"
UA = {"User-Agent": "Mozilla/5.0"}
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "..", "shot-pack", "sentinel-2017")
BBOX = (-97.92, 30.28, -97.77, 30.40)
NDWI_T = 0.0
FLOOR_DATE, FULL_DATE = "2017-01-30", "2018-02-04"

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def scene(date):
    u = (f"{STAC}?collections=sentinel-2-l2a"
         f"&bbox={BBOX[0]},{BBOX[1]},{BBOX[2]},{BBOX[3]}"
         f"&datetime={date}T00:00:00Z/{date}T23:59:59Z&limit=10")
    d = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=UA),
                                          timeout=60, context=ctx).read())
    return min(d["features"], key=lambda f: f["properties"].get("eo:cloud_cover", 100))


def band(item, key):
    href = item["assets"][key]["href"]
    with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR", AWS_NO_SIGN_REQUEST="YES"):
        with rasterio.open(href) as src:
            tf = Transformer.from_crs("EPSG:4326", src.crs, always_xy=True)
            x0, y0 = tf.transform(BBOX[0], BBOX[1])
            x1, y1 = tf.transform(BBOX[2], BBOX[3])
            win = from_bounds(min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1),
                              transform=src.transform)
            a = src.read(1, window=win).astype("float32")
            res = src.res[0]
    return a, res


def water_mask(item):
    g, res = band(item, "green")
    n, _ = band(item, "nir")
    ndwi = (g - n) / np.maximum(g + n, 1e-6)
    return ndwi > NDWI_T, res


def main():
    os.makedirs(OUT, exist_ok=True)
    floor_it, full_it = scene(FLOOR_DATE), scene(FULL_DATE)

    w_floor, res = water_mask(floor_it)
    w_full, _ = water_mask(full_it)
    h = min(w_floor.shape[0], w_full.shape[0])
    w = min(w_floor.shape[1], w_full.shape[1])
    w_floor, w_full = w_floor[:h, :w], w_full[:h, :w]

    exposed = w_full & ~w_floor           # was water at full pool, dry at the floor
    px_m2 = res * res
    acre = 4046.86

    print(f"pixel {res:.0f} m  grid {w}x{h}")
    print(f"  water @ full pool  {FULL_DATE}: {w_full.sum():>7} px  "
          f"{w_full.sum()*px_m2/acre:>8.1f} acres")
    print(f"  water @ floor      {FLOOR_DATE}: {w_floor.sum():>7} px  "
          f"{w_floor.sum()*px_m2/acre:>8.1f} acres")
    print(f"  EXPOSED by drawdown           : {exposed.sum():>7} px  "
          f"{exposed.sum()*px_m2/acre:>8.1f} acres")
    if w_full.sum():
        print(f"  = {100*exposed.sum()/w_full.sum():.1f}% of the full-pool surface")

    # Render: full-pool true colour with newly-exposed ground burned in.
    href = full_it["assets"]["visual"]["href"]
    with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR", AWS_NO_SIGN_REQUEST="YES"):
        with rasterio.open(href) as src:
            tf = Transformer.from_crs("EPSG:4326", src.crs, always_xy=True)
            x0, y0 = tf.transform(BBOX[0], BBOX[1])
            x1, y1 = tf.transform(BBOX[2], BBOX[3])
            win = from_bounds(min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1),
                              transform=src.transform)
            rgb = np.transpose(src.read((1, 2, 3), window=win), (1, 2, 0))[:h, :w].astype("float32")

    tint = rgb.copy()
    tint[exposed] = tint[exposed] * 0.25 + np.array([255, 140, 40]) * 0.75
    Image.fromarray(tint.astype("uint8"), "RGB").save(
        os.path.join(OUT, "lake-austin_2017_EXPOSED_overlay.png"))

    stats = {
        "floor_date": FLOOR_DATE, "floor_ft": 481.98,
        "full_date": FULL_DATE, "full_ft": 492.08, "delta_ft": 10.10,
        "gsd_m": res, "ndwi_threshold": NDWI_T,
        "full_pool_acres": round(float(w_full.sum()) * px_m2 / acre, 1),
        "floor_acres": round(float(w_floor.sum()) * px_m2 / acre, 1),
        "exposed_acres": round(float(exposed.sum()) * px_m2 / acre, 1),
    }
    with open(os.path.join(OUT, "exposure_stats.json"), "w") as f:
        json.dump(stats, f, indent=2)
    print("\nwrote lake-austin_2017_EXPOSED_overlay.png + exposure_stats.json")


if __name__ == "__main__":
    main()
