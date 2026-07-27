# L1 Profile Report — Jobber Client Merge

## Inputs
- `Jobber Clients 1 of 2.xlsx`: 1648 rows × 40 cols
- `Jobber Clients 2 of 2.xlsx`: 299 rows × 40 cols
- Concatenated: 1947 rows (columns identical across both files: True)

## Deduplication
- Duplicates removed on J-ID: 0
- Duplicates removed on normalized name+service-address (J-ID missing): 0
- **Final row count: 1947** (J-ID missing in 0 rows)

## Record composition
- Archived: 2 archived / 1945 active
- Is Company?: 49 companies / 1898 persons

## Address completeness
| Category | Count | % |
|---|---|---|
| Usable Service address (street + city or zip) | 1626 | 83.5% |
| Billing-only (Service missing, Billing usable) | 3 | 0.2% |
| No usable address at all | 318 | 16.3% |

- Service Street 1 present: 1639; Service City present: 1663; Service ZIP present: 1599
- 13 rows have a Service Street 1 but no city AND no ZIP (partial / free-text addresses like "B Dock 2 slips", "Hollows Cobalt 262") — these will go to the review queue.
- Many no-address rows have only a city (e.g., Marble Falls, Point Venture, Kingsland — off-lake towns) or nothing at all.

## Existing Tags distribution
- `(none)`: 1935
- `Builder`: 10
- `boatcover`: 1
- `Builder, Hydraulic Lifts, Shorescreen`: 1

**Only 12 of 1,947 rows carry any tag** — tagging is essentially unused; the zone/tier system built here starts from a blank slate.

## Marina signals (PFT fields)
- PFT[Slip Number] populated: 3 rows
- PFT[Gate Code] populated: 72 rows
- PFT[Boat or Vessel] populated: 9 rows
