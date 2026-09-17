# Earth Pro → Square Footage → Bid Quantities

**Goal:** one repeatable loop any crew member can run that turns a Lake Austin property into the three numbers ATX bids off — **square feet**, **sediment cubic yards**, **linear feet of bulkhead** — plus the permit posture that governs whether the volume is even sellable.

**Time:** ~3 min per property after the first one. **Cost:** free, no API key.

Pairs with `../shot-pack/EARTH_PRO_RUNBOOK.md` (which covers *imagery capture* for sales/media). This doc covers *measurement* for bidding. Same tool, different job.

---

## Why Earth Pro and not the satellite scraper

`atx-lakescapes/10_drawdown_2026/lake_austin_satellite_scraper.py` pulls Google Maps Static tiles. Keep it — it is good bulk recon for Grok's deck. It cannot do this job:

| | Static Maps scraper | Earth Pro |
| -- | -- | -- |
| Returns a measurement | No — returns a PNG | **Yes — area and length directly** |
| Historical (drawdown) imagery | No, current only | **Yes, time slider** |
| Centers on | Street-name geocode | Whatever you point at |
| Cost | Per-request API quota | Free |

Measuring off a raster means tracing pixels and converting by a scale factor. Earth Pro hands you the geometry. Don't approximate a number you can have exactly.

---

## The loop

### 1. Open the property (30 sec)

Earth Pro → search the address. If it's one of the 39 tracked areas, `File ▸ Open ▸ ../shot-pack/lake-austin-shotlist.kml` and double-click the placemark instead — that gets you the vetted camera.

⚠️ Several pins in that KML are flagged estimates (N4, N6, N11, S5, S13, S14, S15 and others — full list in `EARTH_PRO_RUNBOOK.md` §5). Confirm the shoreline visually before you trust the location.

### 2. Set the imagery you want to measure against (30 sec)

- **Current condition** (default) — for what's there now.
- **2017 drawdown** — click the clock icon, drag to **Feb 1–13, 2017**. This is the only imagery that shows the lakebed exposed, which is where sediment extent is actually visible instead of inferred.

Measuring sediment against current (full-pool) imagery is guesswork. Measure it against 2017 and note that you did.

### 3. Draw (60–90 sec)

**Sediment / work area → polygon.** Toolbar `Add Polygon`. Click the boundary of the work area. Name it something a stranger can read: `4506 Westlake — sediment behind bulkhead`.

**Bulkhead / seawall / tie-back run → path.** Toolbar `Add Path`. Trace the wall. Name it `4506 Westlake — bulkhead run`.

Draw as many as the job has. One polygon per distinct area, one path per distinct run — the tool totals them and the bid wants them itemized anyway.

Tip: Earth Pro's own **Ruler ▸ Polygon** tab shows live area while you drag, if you want a sanity number before exporting.

### 4. Export (15 sec)

Right-click the folder holding your shapes in *Places* → **Save Place As…** → **KML** (not KMZ). Save next to this tool.

### 5. Run the math (5 sec)

```bash
python3 kml_measure.py 4506-westlake.kml --depth-ft 4.5 --csv 4506-westlake.csv
```

`--depth-ft` is the average sediment depth. Get it from a probe on site. Until you have one, the tiered profiles in `atx-lakescapes/10_drawdown_2026/lake_austin_gis_targets.csv` give a starting range per cluster (Class A runs 4–6 ft, Class B 2–3 ft at bulkhead toes) — but a range is an assumption, and the bid must say so.

Output gives you, per shape and totalled: square feet, perimeter, sediment cubic yards, linear feet, and the permit posture for that volume.

---

## The permit posture is the output that matters most

⚠️ **CORRECTED 2026-08-05.** An earlier version of this runbook and of `kml_measure.py` stated a
**"25 – 2,000 cy LCRA Lakewide Permit"** path. **That was wrong and is retracted.** The 2,000 cy figure
comes from a lake-lowering registration model on **LCRA-operated** lakes (Inks Lake). LCRA's published
lakewide permits cover **Lake Buchanan and Lake Travis only** — Lake Austin is a City lake and is not on
them. Source: `ATX-Jobs/2026-2708-scenic-williams/20-analysis/PERMIT-AUTHORITY-v2-2026-08-04.md` §3.

The tool now evaluates two independent triggers — **volume and linear feet** — because either one alone
pushes the job into Tier II:

| Trigger | Posture |
| -- | -- |
| **< 25 cy** | City allows without a variance — LDC **§25-8-261(C)(9)(a)**. LCRA HLDO authorization still applies separately |
| **> 25 cy** | **City variance required** — this is the binding ceiling on Lake Austin — *plus* LCRA HLDO |
| **> 500 cy** | **LCRA HLDO Tier II** individual permit, plus the City variance |
| **> 500 LF shoreline disturbed** | **Tier II independently of volume.** A long wall run can trip this at low cubic yardage |

A polygon that computes to 800 cy is not an 800 cy job. It is a **variance-contingent** 800 cy job with a
**<25 cy fallback**. Both numbers belong in the bid as a contingent clause — never one flat number.

🛑 **The open question that can override all of it.** LCRA HLDO Tier I carves out, verbatim,
*"commercial dredge and fill activity."* ATX performs the work for hire, so the cheap Tier I
written-notification path may be unavailable **even under 500 cy** — which would push routine jobs to
Tier II and change lead time and cost on every drawdown bid. **Unresolved. Call LCRA Water Quality
512-578-2324.** Until that is answered, do not promise a Tier I timeline to any client.

---

## Two language rules that bite here

1. **Never write "dredging" in a customer-facing artifact** (ATX-1696). It can trigger retroactive WUI code enforcement on an incomplete structure. Approved: **"sediment remediation"** or **"tier three install."** This already went wrong once on quote #1994.
2. **No invented scarcity anywhere near these numbers.** Volume and square footage are measurements; slot counts and machine-days are not, and the FINAL CRM spec bans inventing them. Structural capacity claims wait on ATX-1625 (equipment hold, still `hold:unconfirmed`).

---

## Making it repeatable for the team

What the loop already gives you: a stable interchange format (KML), exact math, permit logic applied automatically, and CSV out for the bid engine. Any crew member with Earth Pro can produce identical numbers.

What is still manual, deliberately: **deciding what's in scope.** Tracing the boundary is the judgment call — where sediment actually needs removing, which wall section is failing, what the client is willing to pay to fix. That is the part you don't want automated, and it is the part that takes 90 seconds.

Next automation step, when volume justifies it (not yet):

- Batch mode — a folder of KMLs → one CSV, so a day of field digitizing lands as one file.
- Feed the CSV into the drawdown-bid skill (ATX-1694) so quantities become a priced scope without retyping.
- Auto-segmentation of sediment extent from 2017 imagery. Real, but it needs a labelled set of traced polygons first — which this loop produces as a side effect. Do 20 properties by hand before considering it.

Do **not** build batch mode or segmentation before the loop has been run on real jobs. The first ten properties will change the field names.
