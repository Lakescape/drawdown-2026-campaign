# Gate 1 — Claim Ledger: DRAWDOWN sales highlight

Source of truth: `01_FINAL_Deliverables/ASSET_OnePager_Summary_v1_FINAL.md`
Rule: no row here, no claim on screen or in VO. If the source hedges, the asset
hedges in the same breath — not in an end-card disclaimer.

| # | Claim | Exact source | Source hedges? | Asset must hedge? | Footage required to carry it |
|---|---|---|---|---|---|
| C1 | Drawdown is happening — Oct 12 to Nov 30, 2026 | LCRA announcement, **2026-08-29**; dates per LCRA release (down from Oct 12, refill from Nov 24, normal pool Nov 30) | no — announced, dated | **NO.** State the event and the dates as fact. Retired: "exploring", "unofficial", "nothing is official yet", "this fall" with no date. | any low-water shoreline |
| C2 | About 10 ft drop (target 481.8–482.8 ft msl) | LCRA's own number — Nate ruling **2026-09-06**, campaign-wide | no | **NO.** Say "about 10 feet". Retired: "projected", "10–12", "ten to twelve". | exposed shoreline / waterline stain |
| C3 | First meaningful window in ~10 years | "first meaningful low-water window in nearly ten years" | no | no | — |
| C4 | Next comparable window 8–10 yrs out | "**may be** eight to ten years away" | **YES** | **YES** | — |
| C5 | 30–40% cheaper during drawdown | "typically 30–40% less expensive" | "typically" | keep "typically" | dry-ground work vs barge work |
| C6 | Some work impossible at full pool | "simply not possible any other way" | no | no | sediment behind bulkhead / tie-back |
| C7 | **2 amphibious machines committed** | "committed two amphibious machines… equipment that can work the soft lake bed where conventional machines can't go" | no | no | **must show 2, and must show amphibious undercarriage** |
| C8 | ~25 working days of capacity | "roughly 25 working days" | "roughly" | keep "roughly" | — |
| C9 | $695 assessment, 100% credited, 12-mo | Priority Assessment block | no | no | — |
| C10 | We'll tell you if nothing's needed | "we'll tell you that to your face" | no | no | — |
| C11 | Lake Austin is our home water | "it's our home water" | no | no | **must read as Lake Austin** |

## Binding notes

- **C7 is the offer's differentiator.** It is the reason the $695 is worth
  booking and the reason capacity is scarce. Any frame under this claim must
  show amphibious/pontoon undercarriage and must show exactly two machines.
- **C11 is a location claim.** Generic lake footage silently contradicts it.
- **C1 retired 2026-08-29, dated 2026-09-04, depth fixed 2026-09-06.** LCRA announced
  the drawdown 2026-08-29 (source: Nate, 2026-09-02). Nate 2026-09-04: hedge retired,
  dates on screen. Nate 2026-09-06: ABOUT 10 FT campaign-wide, LCRA's number, 10–12
  retired. The builders on `main` (`compose.py`, `build_lcd_v2.py`, `build_plate_cards.py`,
  `build_scheduling_pack.py`) already ship these strings; this ledger now matches them.
  No LCRA notice document is filed in this repo — cite the LCRA release directly
  before any external legal use.
- **C4 remains the legal exposure.** The one-pager is careful; the video must
  be at least as careful, spoken not just captioned.

## v1 script defects caught by this ledger

| Defect | Ledger row |
|---|---|
| VO said the drawdown is being "lined up" as fact | C1 — hedge omitted |
| Card/VO said "2 MACHINES" over a frame containing three | C7 — count |
| Every machine on screen has conventional steel tracks | C7 — equipment type |
| Opening shot reads northern, not Central Texas | C11 — location |
