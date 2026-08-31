#!/usr/bin/env python3
"""Pull Sentinel-2 imagery of Lake Austin at the 2017 drawdown floor, plus a
matched full-pool scene, as a true before/after pair.

Why this instead of Google Earth Pro: Google flew Lake Austin exactly ONCE
during the 2017 drawdown — 1/8/2017, when the lake was 486.57 ft, only 55% of
the way down. Sentinel-2 revisits every ~5 days and caught 2017-01-30 at 0.25%
cloud, with the lake at 482.02 ft — its floor. That is the image the campaign
actually wants, and no GUI automation is involved.

Tradeoff, stated plainly: Sentinel-2 is 10 m/pixel. Excellent for whole-lake and
cove-scale exposed shoreline. It will NOT resolve an individual dock. For
lot-level detail, use the lidar DEM path instead (1 m, computed from elevation).

Lake levels come from DATA_2017_Drawdown_LakeLevels_VERIFIED.md (TWDB record).
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
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "shot-pack", "sentinel-2017")

# Lake Austin: Mansfield Dam down to Tom Miller Dam.
BBOX = (-97.92, 30.28, -97.77, 30.40)

# Verified daily elevations (ft MSL) for the dates we pull.
LEVELS = {"2017-01-30": 482.02, "2017-01-07": 488.5, "2017-02-16": 491.5}
NORMAL_POOL = 492.04
FLOOR = 481.69

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def search(start, end, limit=40):
    u = (f"{STAC}?collections=sentinel-2-l2a"
         f"&bbox={BBOX[0]},{BBOX[1]},{BBOX[2]},{BBOX[3]}"
         f"&datetime={start}T00:00:00Z/{end}T23:59:59Z&limit={limit}")
    req = urllib.request.Request(u, headers=UA)
    return json.loads(urllib.request.urlopen(req, timeout=60, context=ctx).read())


def cloud(f):
    return f["properties"].get("eo:cloud_cover", 100.0)


def clip(item, dest, label):
    """Window the scene's 10 m true-colour COG to the lake bbox."""
    href = item["assets"]["visual"]["href"]
    with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR",
                      AWS_NO_SIGN_REQUEST="YES"):
        with rasterio.open(href) as src:
            tf = Transformer.from_crs("EPSG:4326", src.crs, always_xy=True)
            x0, y0 = tf.transform(BBOX[0], BBOX[1])
            x1, y1 = tf.transform(BBOX[2], BBOX[3])
            win = from_bounds(min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1),
                              transform=src.transform)
            arr = src.read((1, 2, 3), window=win)
    rgb = np.transpose(arr, (1, 2, 0))
    im = Image.fromarray(rgb.astype("uint8"), "RGB")
    im.save(dest)
    print(f"  {label}: {item['properties']['datetime'][:10]}  "
          f"cloud {cloud(item):.2f}%  {im.size[0]}x{im.size[1]}px  -> {os.path.basename(dest)}")
    return {"date": item["properties"]["datetime"][:10], "id": item["id"],
            "cloud_cover": round(cloud(item), 2), "size": list(im.size), "file": os.path.basename(dest)}


def main():
    os.makedirs(OUT, exist_ok=True)
    manifest = {"bbox": list(BBOX), "normal_pool_ft": NORMAL_POOL, "floor_ft": FLOOR,
                "source": "Sentinel-2 L2A via earth-search.aws.element84.com",
                "gsd_m": 10, "scenes": {}}

    # 1. The floor. Lake at 482.02 ft — 10.0 ft below normal pool.
    floor_scene = min(search("2017-01-29", "2017-01-31")["features"], key=cloud)
    manifest["scenes"]["drawdown_floor"] = clip(
        floor_scene, os.path.join(OUT, "lake-austin_2017-01-30_FLOOR_482ft.png"), "FLOOR")
    manifest["scenes"]["drawdown_floor"]["lake_level_ft"] = 482.02
    manifest["scenes"]["drawdown_floor"]["ft_below_normal"] = round(NORMAL_POOL - 482.02, 2)

    # 2. Matched full-pool control — same season, so vegetation and sun angle
    #    do not become a confound. Cleanest winter scene we can find.
    cands = []
    for a, b in (("2017-11-01", "2018-03-01"), ("2016-11-01", "2016-12-31")):
        try:
            cands += search(a, b)["features"]
        except Exception as e:
            print(f"  (skipped {a}..{b}: {type(e).__name__})")
    full = min(cands, key=cloud)
    manifest["scenes"]["full_pool"] = clip(
        full, os.path.join(OUT, f"lake-austin_{full['properties']['datetime'][:10]}_FULL.png"),
        "FULL POOL")

    with open(os.path.join(OUT, "manifest.json"), "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"\nwrote {OUT}/manifest.json")


if __name__ == "__main__":
    main()
