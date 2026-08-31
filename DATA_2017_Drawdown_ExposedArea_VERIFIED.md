# How much of Lake Austin came out of the water in 2017 — verified

Source of record: **TWDB 2008-12 volumetric (bathymetric) survey of Lake Austin**,
elevation–area–capacity table
`https://www.twdb.texas.gov/surfacewater/surveys/completed/files/Austin/2008-12/Austin_2008-12.txt`
Lake levels: TWDB daily record (see `DATA_2017_Drawdown_LakeLevels_VERIFIED.md`).

Sanity check on the table before trusting it: at 492.8 ft it gives 1,589 acres
and 24,644 acre-ft — Lake Austin's published surface area and capacity. It reads
elevations as negative values; take the absolute value.

## The numbers

| | Elevation | Surface | Storage |
|---|---|---|---|
| Normal pool, pre-drawdown | 492.04 ft | 1,538.6 acres | 23,458 acre-ft |
| Jan 8 2017 — the only Google aerial | 486.57 ft | 1,253.4 acres | 15,796 acre-ft |
| **Floor, Jan 13 2017** | **481.69 ft** | **1,015.1 acres** | **10,269 acre-ft** |

**Exposed lakebed: 523.5 acres — 34% of the lake's surface.**
**Water removed: 13,189 acre-ft ≈ 4.3 billion gallons.**

Average exposed band, spread over roughly 2 × 20.25 miles of shoreline:
**about 107 ft per side.**

## Why the satellite estimate was wrong — and superseded

An NDWI water-mask difference on Sentinel-2 (2017-01-30 floor vs 2018-02-04 full
pool, both 0.06% cloud) returned only 87–123 acres. Do not use that figure.

The tell is in the disagreement pattern: at the floor the satellite gave 929.6
acres against TWDB's 1,015.1 — within 8%. At full pool it gave 1,016.9 against
1,538.6 — off by 34%. A systematic NDWI bias would miss both by a similar
margin. A clipped bounding box only bites at full pool, when the lake is at its
widest. The analysis bbox cut the wide upper reach near Mansfield Dam.

The Sentinel imagery is still useful — it is the only picture of the lake at its
actual floor, and the overlay shows *where* the exposure is. The acreage number
must come from TWDB.

## What this changes about the story

Two earlier conclusions were wrong and are corrected here:

1. **"The drawdown isn't visually dramatic"** — true from directly overhead, and
   still true: 107 ft of exposed bank on a 600-ft-wide lake is a thin ribbon at
   satellite scale. But **34% of the surface** and **4.3 billion gallons** are
   not small numbers, and they are the honest framing.
2. **"Use the lidar DEM for per-lot exposure"** — will not work. USGS 3DEP 1 m
   lidar (`TX_Central_B1_2017`) was flown at full pool: its minimum elevation is
   490.79 ft, its dominant values are 491.9/492.1 ft, and there are **zero cells
   below 481.69 ft**. Lidar does not penetrate water, so the drawdown band is
   not in that dataset at all. Verified by remote window read — no download.

## The right path to per-lot exposure

TWDB's shapefile package (92 MB) contains what the lidar lacks:

- `Austin2009_5ftcont.shp` — 5 ft **bathymetric** contours
- `Austin09_Lake08_stpl83.shp` — full-pool shoreline polygon
- `Austin2009_allpts4TIN_stpl83.shp` — survey points for a TIN

Bathymetric contours below the waterline plus lidar above it give a complete
surface. Intersect the 481.69–492.04 ft band with `ops/zones.geojson` (39
polygons) for per-zone acreage, or with parcel geometry for per-lot square
footage. Needs `shapely` + `pyshp`; contours are at 5 ft intervals so the band
edges interpolate.

## Lines that are now defensible

> Last time, Lake Austin dropped 10.8 feet over about seven weeks.
> That took 4.3 billion gallons out of the lake and put **523 acres** of
> lakebed — a third of the surface — in the open air.
> On an average lot that is roughly **107 feet** of bank you could stand on.

Every figure above traces to a state survey or a state daily record.
