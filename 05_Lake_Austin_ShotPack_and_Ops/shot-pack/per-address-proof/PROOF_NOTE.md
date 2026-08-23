# PROOF NOTE — ATX-2156 Per-address drawdown visual renderer (PoC)

Date: 2026-08-23 · Branch: `MACBOSS/ATX-2156-per-address-drawdown-visual`
Renderer: `05_Lake_Austin_ShotPack_and_Ops/tools/per_address_visual.py`

## What this proves

An address (or prop_id) resolves to a sales-ready PNG: the true 2017 drawdown
aerial frame for the lot's zone, the caller's own TCAD parcel boundary as an
inset map panel, an exposed-area callout, and the mandated hedged caption.

## Render method: INSET, not overlay — and why

The 2017 frames are Google Earth Pro screen grabs taken at tilted `LookAt`
views (see `tools/capture_2017_frames.py`: lon/lat + range + tilt + heading per
shot, then a pixel-crop of a full-screen grab). The pixel-to-ground mapping of
a tilted Earth Pro viewport is a perspective projection that is **not
recoverable from repo data** — no camera intrinsics, no ground-control points.
Exact georegistration is therefore not provable, so per the task brief the
parcel boundary is drawn as an **inset map panel beside the aerial** (gold
#c4923a stroke, ~15% gold fill, north-up, aspect-true in the TCAD state-plane
foot coordinates) and the image itself discloses: *"Inset for location
reference — the aerial frame is not georectified."* No aerial was warped, no
boundary fabricated. Honesty over flash.

## The 3 proof renders (all tier-A zones, one from N8 Greenshores)

| # | Address | Zone | Exposed acres (from lot_exposure) | Output | Exit |
|---|---------|------|-----------------------------------|--------|------|
| 1 | 1500 1/2 CITY PARK RD (prop 130505) | n08-greenshores | 21.178 → shown 21.18 | `PROOF_n08-greenshores_1500-1-2-city-park-rd.png` (3,390,422 B) | 0 |
| 2 | 2215 WESTLAKE DR (prop 119693) | n03-mount-bonnell-shores | 4.62 | `PROOF_n03-mount-bonnell-shores_2215-westlake-dr.png` (4,076,574 B) | 0 |
| 3 | 4109 LAKEPLACE LN (prop 474429) | n04-watersedge | 1.722 → shown 1.72 | `PROOF_n04-watersedge_4109-lakeplace-ln.png` (3,890,967 B) | 0 |

Commands run (from `05_Lake_Austin_ShotPack_and_Ops/tools/`):

```
python3 per_address_visual.py "1500 1/2 CITY PARK RD" --data-root /Users/austinlakescapes/drawdown-2026-campaign/05_Lake_Austin_ShotPack_and_Ops
python3 per_address_visual.py "2215 WESTLAKE DR"      --data-root /Users/austinlakescapes/drawdown-2026-campaign/05_Lake_Austin_ShotPack_and_Ops
python3 per_address_visual.py "4109 LAKEPLACE LN"     --data-root /Users/austinlakescapes/drawdown-2026-campaign/05_Lake_Austin_ShotPack_and_Ops
```

All three exited 0; all three PNGs are non-empty (sizes above) and were
visually inspected: inset parcel boundary present and plausible, gold callout
"NN.NN ACRES EXPOSED" legible with floor/pool subline, caption bar shows
address, zone name, tier, and the exact hedged line — "January–February 2017
drawdown conditions. The 2026 window is projected, not confirmed."

`--data-root` was needed because the input data (lot_exposure, TCAD geojson,
2017 frames) currently lives uncommitted in the main checkout; the script
defaults to its own repo copy once those inputs land on a branch. No input
file was modified — outputs went only to the new `shot-pack/per-address-proof/`
folder in this worktree.

Edge paths also exercised: `--prop-id` input (exit 0), unknown address
(exit 1 with close-match suggestions), and the zone-level fallback —
parcel missing → zone frame + "Zone-level view — parcel boundary pending",
no boundary drawn (verified via direct `render(..., geometry=None, ...)` call;
every one of the 881 CSV lots in fact has a TCAD parcel, so the fallback
cannot trigger on current data).

## Numbers provenance

- Exposed acres: `ops/lot_exposure_482ft.csv` per-lot `exposed_acres`, verbatim
  (display rounded to 2 decimals).
- Drawdown floor 481.69 ft / full pool 492.04 ft: `ops/lot_exposure_482ft.json`
  metadata (`floor_ft`, `pool_ft`).
- Zone name / tier: same CSV. Nothing is computed by the renderer.

## Environment

System python3 (macOS), Pillow 12.3.0 already installed. **No pip installs
were needed** (pyshp/geopandas not required — GeoJSON parsed with stdlib
`json`; inset drawn with Pillow). Fonts: Cormorant Garamond + Source Sans 3
from `~/Library/Fonts` (variable TTFs), with Times/Helvetica fallbacks.

## Data gaps found (for the capture pipeline, not fixable here)

1. **N8 and N6 tier-A frames are contaminated.** The source PNGs
   `N8-greenshores-on-lake-austin__2017_context.png` and
   `N6-the-courtyard-gated-bull-creek-arm__2017_context.png` contain a dark
   terminal/AI-panel window captured mid-screen (≈60–65% dark pixels in the
   panel region vs ≈15–35% vegetation-dark in clean frames). N8 is mandated
   for this proof, so proof #1 shows it as-is — originals must not be
   modified. Recommend recapturing N8 (and N6) before customer use. The third
   proof slot was moved from N6 (5505 PARADOX CV) to N4 (4109 LAKEPLACE LN)
   for this reason.
2. **tier-A folder holds only 6 of 16 tier-A zone frames** (N1, N3, N4, N5,
   N6, N8). Zones such as S8, S2, S4, S6, N15, N16 (tier A per
   `lot_exposure_482ft.csv`) have no frame in `screenshots-2017/tier-A/`, so
   per-address renders for those zones currently fall to the last-resort
   search and would exit 2 if nothing matches.
3. TCAD GeoJSON polygons carry an extra nesting level (`coordinates` one
   level deeper than strict RFC 7946 for Polygon); the renderer tolerates
   this when extracting rings.
