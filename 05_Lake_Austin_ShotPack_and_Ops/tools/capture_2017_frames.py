#!/usr/bin/env python3
"""Capture the 2017 Lake Austin drawdown frames from Google Earth Pro.

Why this exists: Earth Pro is a Qt app with no accessible outline rows, so the
Places sidebar cannot be scripted by UI element, and clicking it by pixel breaks
the moment the list scrolls or the window moves. Instead we hand Earth a
one-placemark KML per shot — it flies to that LookAt on open — then screen-grab.

Only ONE aerial exists inside the 2017 drawdown: 1/8/2017. Verified across five
placemarks spanning both banks. Set the time slider to it once, by hand, before
running this; the selection persists as Earth flies. See
DATA_2017_Drawdown_LakeLevels_VERIFIED.md — on that date the lake was 486.57 ft,
5.95 ft down of an eventual 10.83 ft, i.e. 55% of the way to the floor.

Usage:
    python3 capture_2017_frames.py --check          # verify setup, capture nothing
    python3 capture_2017_frames.py --limit 3        # first 3, to eyeball
    python3 capture_2017_frames.py                  # all 49 (resumes)
    python3 capture_2017_frames.py --tier A --detail

Resumable: existing output files are skipped, so a crashed or interrupted run
picks up where it stopped.
"""
import argparse
import os
import re
import subprocess
import sys
import time
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
PACK = os.path.abspath(os.path.join(HERE, "..", "shot-pack"))
KML = os.path.join(PACK, "lake-austin-shotlist.kml")
OUTROOT = os.path.join(PACK, "screenshots-2017")
TMP = "/tmp/ge2017"
NS = {"k": "http://www.opengis.net/kml/2.2"}

# Viewport crop from a full-screen grab, in native pixels. Left edge clears the
# Places sidebar; bottom clears the status bar but keeps the Google attribution,
# which must stay in any published frame.
CROP = (640, 180, 3456, 2020)

TIER_OF = {
    "TIER A — high-$$ priority": "tier-A",
    "TIER B — secondary": "tier-B",
    "TIER C — context/benchmark": "tier-C",
    "COVES · CHANNELS · CANAL FEATURES": "tier-coves",
}

KML_TEMPLATE = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2"><Document>
<Placemark><name>{name}</name>
<LookAt><longitude>{lon}</longitude><latitude>{lat}</latitude>
<altitude>0</altitude><range>{rng}</range><tilt>{tilt}</tilt>
<heading>{head}</heading>
<altitudeMode>relativeToGround</altitudeMode></LookAt>
<Point><coordinates>{lon},{lat},0</coordinates></Point>
</Placemark></Document></kml>
"""


def slugify(name):
    s = name.split("·", 1)
    code = s[0].strip() if len(s) > 1 else ""
    rest = s[1].strip() if len(s) > 1 else name
    rest = re.sub(r"[^\w\s-]", "", rest, flags=re.UNICODE)
    rest = re.sub(r"\s+", "-", rest).strip("-").lower()
    return f"{code}-{rest}"[:70] if code else rest[:70]


def osa(script):
    return subprocess.run(["osascript", "-e", script],
                          capture_output=True, text=True).stdout.strip()


def parse_placemarks():
    root = ET.parse(KML).getroot()
    out = []
    for folder in root.findall(".//k:Folder", NS):
        fname = folder.find("k:name", NS)
        tier = TIER_OF.get(fname.text.strip() if fname is not None else "", "tier-other")
        for pm in folder.findall("k:Placemark", NS):
            nm = pm.find("k:name", NS)
            la = pm.find("k:LookAt", NS)
            if nm is None or la is None:
                continue
            g = {c.tag.split("}")[1]: (c.text or "0") for c in la}
            out.append({
                "name": nm.text.strip(), "slug": slugify(nm.text.strip()), "tier": tier,
                "lon": g.get("longitude", "0"), "lat": g.get("latitude", "0"),
                "range": float(g.get("range", "1500")),
                "tilt": g.get("tilt", "0"), "heading": g.get("heading", "0"),
            })
    # placemarks outside any folder (e.g. the whole-lake overview)
    seen = {p["name"] for p in out}
    for pm in root.findall(".//k:Placemark", NS):
        nm = pm.find("k:name", NS)
        la = pm.find("k:LookAt", NS)
        if nm is None or la is None or nm.text.strip() in seen:
            continue
        g = {c.tag.split("}")[1]: (c.text or "0") for c in la}
        out.insert(0, {
            "name": nm.text.strip(), "slug": slugify(nm.text.strip()), "tier": "tier-overview",
            "lon": g.get("longitude", "0"), "lat": g.get("latitude", "0"),
            "range": float(g.get("range", "1500")),
            "tilt": g.get("tilt", "0"), "heading": g.get("heading", "0"),
        })
    return out


def fly(pm, rng):
    os.makedirs(TMP, exist_ok=True)
    path = os.path.join(TMP, "shot.kml")
    with open(path, "w") as f:
        f.write(KML_TEMPLATE.format(name=pm["name"], lon=pm["lon"], lat=pm["lat"],
                                    rng=int(rng), tilt=pm["tilt"], head=pm["heading"]))
    subprocess.run(["open", "-a", "Google Earth Pro", path], check=False)


def grab(dest, settle):
    """Screen-grab Earth Pro and crop to the 3D viewport."""
    from PIL import Image
    osa('tell application "Google Earth Pro" to activate')
    time.sleep(settle)
    raw = os.path.join(TMP, "raw.png")
    subprocess.run(["screencapture", "-x", "-o", raw], check=True)
    im = Image.open(raw)
    # Guard: a different screen size means CROP is wrong and every frame would
    # be silently mis-framed. Fail loudly instead.
    if im.size != (3456, 2234):
        print(f"  !! screen is {im.size}, expected (3456, 2234) — adjust CROP", file=sys.stderr)
    im.crop(CROP).save(dest)
    return im.size


def check():
    ok = True
    if not os.path.exists(KML):
        print("MISSING KML:", KML); ok = False
    # The app bundle is "Google Earth Pro" but the process reports as "Google Earth".
    running = osa('tell application "System Events" to (name of processes) contains "Google Earth"')
    print("Earth Pro running:", running)
    if running != "true":
        print("  -> launch Earth Pro, load the shotlist KML, set the time slider to 1/8/2017")
        ok = False
    pms = parse_placemarks()
    print(f"placemarks parsed: {len(pms)}")
    for t in sorted({p['tier'] for p in pms}):
        print(f"  {t}: {sum(1 for p in pms if p['tier']==t)}")
    print("output root:", OUTROOT)
    print("\nBEFORE RUNNING: set the historical-imagery slider to 1/8/2017 by hand.")
    print("The date persists as Earth flies; this script does not set it.")
    return ok


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--tier", default="")
    ap.add_argument("--detail", action="store_true", help="also capture a tighter frame")
    ap.add_argument("--settle", type=float, default=9.0, help="seconds to let tiles stream in")
    ap.add_argument("--force", action="store_true", help="re-capture existing files")
    a = ap.parse_args()

    if a.check:
        sys.exit(0 if check() else 1)

    pms = parse_placemarks()
    if a.tier:
        pms = [p for p in pms if p["tier"].endswith(a.tier)]
    if a.limit:
        pms = pms[:a.limit]

    os.makedirs(TMP, exist_ok=True)
    log = open(os.path.join(OUTROOT, "capture_log.tsv"), "a")
    done = skipped = 0

    for i, pm in enumerate(pms, 1):
        d = os.path.join(OUTROOT, pm["tier"])
        os.makedirs(d, exist_ok=True)
        shots = [("context", pm["range"])]
        if a.detail:
            shots.append(("detail", max(pm["range"] * 0.35, 250)))

        for kind, rng in shots:
            dest = os.path.join(d, f"{pm['slug']}__2017_{kind}.png")
            if os.path.exists(dest) and not a.force:
                skipped += 1
                continue
            print(f"[{i}/{len(pms)}] {pm['slug']} ({kind}, range {int(rng)}m)")
            fly(pm, rng)
            time.sleep(2.0)          # let the fly-to animation start
            grab(dest, a.settle)
            done += 1
            log.write(f"{time.strftime('%Y-%m-%dT%H:%M:%S')}\t{pm['tier']}\t{pm['slug']}\t{kind}\t{int(rng)}\t{dest}\n")
            log.flush()

    log.close()
    print(f"\ncaptured {done}, skipped {skipped} (already present)")
    print("VERIFY: spot-check that each frame's imagery reads 1/8/2017 before use.")


if __name__ == "__main__":
    main()
