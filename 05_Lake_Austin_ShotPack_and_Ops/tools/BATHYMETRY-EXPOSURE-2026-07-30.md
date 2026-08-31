# Lake Austin Drawdown — Exposed Lakebed by Elevation

Date: 2026-07-30
Source: **TWDB Volumetric Survey of Lake Austin, December 2008 Survey** (published June 2010, prepared for the City of Austin) — `twdb.texas.gov/hydro_survey/Austin/2008-12/Austin2009_FinalReport.pdf`, Appendices A + B, elevation-area and elevation-capacity tables at 0.1 ft increments.
Datum: NGVD 29. Conservation pool **492.8 ft msl**. Normal operating range 491.8–492.8 ft.

Answers "how much lakebed comes out of the water, and where" with measured numbers instead of photographs. No 2017 imagery required.

---

## Headline

| Drawdown | Surface elev | Lake area | **Newly exposed** | Water removed |
|---|---|---:|---:|---:|
| none (conservation pool) | 492.8 ft | 1,589 ac | — | — |
| **−10 ft** | 482.8 ft | 1,067 ac | **522 acres** | 13,219 acre-ft |
| **−11 ft** | 481.8 ft | 1,021 ac | **568 acres** | 14,263 acre-ft |
| **−12 ft** | 480.8 ft | 966 ac | **623 acres** | 15,257 acre-ft |

**A 10–12 ft drawdown exposes 522–623 acres — 33–39% of the lake's entire surface.** That is the total addressable work surface for the window, and it is the number that should anchor capacity planning, not a slot count.

522 acres = 22.7 million sq ft. 623 acres = 27.1 million sq ft.

## −12 ft is not an arbitrary target — it is the physical floor

Tom Miller Dam's **gated spillway crest sits at 480.8 ft** (Table 1 of the survey), exactly the −12 ft figure. That is the lowest elevation reachable by gate operation. Below it, drawdown requires turbine or other releases.

So when the City says "10 to 12 feet," the deep end of that range is the dam's own hydraulic limit, and 480.8 ft is very likely the hard floor. Useful for planning: **do not scope work below 480.8 ft**.

## Exposure is close to linear — about 50 acres per foot

Acres lost per foot of drop, read off the area table:

| Band | ac/ft | | Band | ac/ft |
|---|---:|---|---|---:|
| 492.8→492 | 66 | | 486→485 | 50 |
| 492→491 | 50 | | 485→484 | 56 |
| 491→490 | 45 | | 484→483 | 45 |
| 490→489 | 48 | | 483→482 | 46 |
| 489→488 | 60 | | 482→481 | 52 |
| 488→487 | 58 | | 481→480 | 60 |
| 487→486 | 48 | | | |

Range 45–66, averaging ~52 ac/ft. **Each additional foot of drawdown is worth roughly the same amount of new work surface as the last one.** There is no elevation where exposure suddenly jumps — so a shallower-than-hoped drawdown costs work proportionally, not catastrophically. Ten feet instead of twelve loses ~101 acres, about 16% of the exposed surface.

## Average exposed band — and why the average is the wrong number

522 acres spread along the shoreline gives an average exposed width of roughly **70–110 ft** measured out from the current waterline, depending on the shoreline-length figure used (Lake Austin runs ~20 miles dam to dam, but true shoreline including both banks and every cove is materially longer; the range above spans 40–60 miles of shoreline).

⚠️ **Treat that only as a sanity check, never as a per-property estimate.** The whole business case lives in the variance around it:

- **Steep bluff frontage** (Mount Bonnell, Rockcliff, cliff-top estates) exposes a narrow band — 10–30 ft. These properties barely change. This is exactly why the Google 1/8/2017 frame looks like a full lake at N3: deep narrow reach, steep banks, little visible change.
- **Shallow coves and flats** (the Williams cove, creek arms, delta mouths) expose 200–400+ ft and go fully dry. These are the "beached" properties, and they are where the work is.

**That split is the entire targeting problem, and this table cannot resolve it per-address.** It gives the lake-wide totals only.

## To get per-property numbers

The survey's per-address answer lives in deliverables that are **not** in the PDF:

1. **5-ft bathymetric contour map** (Figure 5) — in the report as a figure, not as data.
2. **1 ft × 1 ft raster / TIN model** of the lake bottom — built for the survey, referenced throughout, not published in the PDF.

Request from the TWDB Hydrographic Survey Program: **(512) 936-0815**, or `Hydrosurvey` per the completed-surveys page. Ask for the Lake Austin 2008 TIN/raster and contour shapefiles in NAD83 State Plane Texas Central (feet).

With that raster, exposed area and remaining toe depth per property frontage is a straightforward clip-and-threshold — the same shape as `kml_measure.py`, but computed against elevation instead of a traced polygon.

## ⚠️ The 2008 date cuts against us exactly where we sell

The survey is **18 years old**, and its own comparison table shows Lake Austin *gaining* ~44 acre-ft/year of capacity between 1999 and 2008 — scour, or methodology differences; TWDB did not determine which.

That lake-wide trend is small (~790 acre-ft over 18 years, ~3%). **The local problem is worse.** Sediment accumulating in coves since 2008 is invisible to this dataset, and cove siltation is the specific thing ATX gets paid to remove. So:

**A 2008 bathymetry will show MORE water and LESS sediment than is actually there in the silted coves.** It errs in the direction that under-sells the work. Good for conservative bidding, bad for estimating volume — never quote a sediment volume off this dataset. Use it for targeting and exposure, use a probe for volume.

TWDB's own recommendation was to resurvey within 10 years, or after a major flood, **and to make the next one a sedimentation survey** (which measures sediment thickness directly). That has not happened. Worth knowing: if the City commissions one ahead of the 2026 drawdown, it would be the single most valuable dataset in this business.

## What this is good for

- **Targeting** — which reaches go dry, ranked, lake-wide
- **Capacity framing** — 522–623 acres is a real, sourced, defensible number; it replaces every invented slot count
- **Equipment split** — dry frontage takes conventional plant, frontage with remaining water and soft bed is amphibious-only
- **Not for volume** — see the 2008 caveat above
