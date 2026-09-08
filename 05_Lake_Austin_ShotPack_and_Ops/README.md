# Lake Austin — Shot Pack & Sales Ops (ATX Lakescapes)

Uploaded 2026-07-27. Two packages, one pipeline: **shot-pack** (waterfront intelligence) → **ops** (customer matching, zone scores, sales attack plan).

## shot-pack/ — waterfront target intelligence
- `index.html` — interactive shot pack: 39 tiered waterfront areas (19 A high-$$ / 11 B / 9 C), tier filters, coves & channels table
- `screenshots/` — 70 annotated aerial frames (context + detail per A/B zone), incl. `overview-lake-austin.jpg`
- `AREA_INDEX.md` — tiered index: every lakefront HOA, cove, channel, canal system, both shores, dam-to-dam
- `EARTH_PRO_RUNBOOK.md` + `lake-austin-shotlist.kml` — capture procedure + placemark tour for true Jan–Feb 2017 drawdown (-10 ft) frames in Google Earth Pro
- `PHASE2_SWARM_PROMPT.md` — the prompt that built the ops layer
- `research/target_list.md`, `research/targets.json` — sourced research + machine-readable targets
- Key finding: **The Island at Mount Bonnell Shores = the lake's only verified canal-grid subdivision** (canals + private slips)

## ops/ — customer-zone matching & sales attack system
- `attack.html` — **Sales Attack Board** (Asana-style): 36 scored zones in Attack-Now / This-Month / B2B-HOA / Nurture columns. Aggregate data only — safe to share.
- `ATTACK_PLAN.md` — 30/60/90 phased sales assault + weekly operating rhythm
- `ZONE_SCORECARD.md` + `zone_scorecard.csv` — composite zone scores (Value 35% · Density 25% · Machinery Access 25% · WorkOps 15%)
- `zones.geojson` + `zones_preview.png` + `zone_ramp_distances.json` — zone polygons, map, ramp transit data
- `L1_match_report.md`, `L1_profile_report.md` — matching results: 1,947 Jobber clients → 654 Lake Austin (500 in-zone / 154 near, 69 pods) + 602 Lake LBJ territory tagged
- `L3_workops_research.md`, `L3_workops.json` — sediment-removal ops: 6 removal zones, permits (COA <25 cy per address is the binding ceiling; the "2,000 cy drawdown window" is **retracted** — no lakewide-permit path is confirmed for Lake Austin), 7 verified ramps, disposal sites
- `HOA_CONTACTS.md`, `hoa-contacts.csv`, `L4_hoa.json` — 29 sourced HOA/POA records. **Leverage: Goodwin manages 5 target HOAs, Spectrum 2, Cohere 1**
- `OUTREACH_PLAYBOOK.md` — tag taxonomy + 7 sequences (incl. drawdown-window campaign on 72-hr standby)
- `OUTREACH_COMPLIANCE.md` — TCPA / CAN-SPAM / TX SB 140 pre-flight gate (blocking — nothing ships without it)
- `pipeline/` — the full reproducible pipeline (geocode → match → pods → workbook → scorecard → board)

## NOT in this repo (by design — customer PII)
`customers-matched.xlsx`, `customers-matched.csv`, `outreach-tags.csv`, the customer-point map (`index.html` in ops), and all raw Jobber exports stay **off-repo / local-only** — they contain names, addresses, gate codes, and slip numbers. The attack board and all docs above are aggregate/anonymized and safe for REVIEW/.
