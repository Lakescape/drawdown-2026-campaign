# Layer 1 — Customer-Zone Matching Report (2026-07-27)

## Inputs
- Jobber Clients 1 of 2 + 2 of 2: **1947 unique customers** (0 duplicate J-IDs; 2 archived, 49 companies)
- Addressable rows: 1642 · No address on file: 305

## Geocoding (100% LOCAL — no customer data ever transmitted)
Census batch API unreachable from sandbox; rebuilt as fully-local OSM geocoder (OpenStreetMap address points + street ways downloaded via Overpass GET; matching done on-machine).
- By confidence: {"EXACT": 549, "QUEUE": 457, "STREET_NUM_NEAR": 380, "NO_ADDRESS": 305, "NO_PARSE": 145, "STREET_LEVEL": 69, "INTERPOLATE": 42}
- **Effective placement rate (EXACT+INTERPOLATE+STREET_NUM_NEAR+STREET_LEVEL): 53.4%**

## Zone assignment (nearest-centroid, caps: IN≤0.75km, NEAR≤1.5km)
- {"UNMATCHED": 907, "IN_ZONE": 500, "OFF_LAKE": 386, "NEAR": 154}

## Top zones by matched customers
                        zone_id                                      zone_name value_tier shore  IN_ZONE  NEAR  total
s04-westlake-lake-austin-marina S4 · Westlake Dr corridor / Lake Austin Marina          A     S       55     1     56
                 s10-rivercrest                               S10 · Rivercrest          A     S       50     0     50
       n03-mount-bonnell-shores    N3 · Mount Bonnell shores / Dry Creek mouth          A     N       43     1     44
       n09-ski-shores-pearce-manana        N9 · Ski Shores / Pearce / Manana strip          A     N       40     4     44
                n08-greenshores                N8 · Greenshores on Lake Austin          A     N       40     3     43
                s02-laguna-loma                               S2 · Laguna Loma          A     S       36     1     37
     n02-laguna-gloria-mayfield            N2 · Laguna Gloria / Mayfield shore          C     N       30     7     37
 n12-river-place-panther-hollow         N12 · River Place / Panther Hollow arm          B     N        9    24     33

## Pods
- 69 pods across 32 zones (3–12 target size, DBSCAN eps=350m)

## Data-quality surprises
- **3 customers hold slip numbers** (marina/dry-storage segment — prime for slip-dredging/dock work)
- **72 gate codes on file** (access intelligence already in Jobber — protect it, it is sensitive)
- Existing Jobber Tags nearly empty (12 rows) — the new tag taxonomy fills that vacuum
- Review queue: 907 rows needing human address fixes

## Outputs
- customers-matched.xlsx (Matched / Zone Summary / Pod Summary / Review Queue / Outreach Tags)
- customers-matched.csv · outreach-tags.csv · review queue sheet · zones.geojson · zones_preview.png · zone_ramp_distances.json
