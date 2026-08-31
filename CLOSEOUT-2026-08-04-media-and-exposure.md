# Closeout — DRAWDOWN media + exposure modelling · 2026-08-04

Session ran 2026-08-03 → 08-04. Two workstreams: a sales video, and a
quantitative exposure model. The second one is the keeper.

---

## What is live and verified

### 1. Exposure model — the real asset

| Artifact | What it is |
|---|---|
| `DATA_2017_Drawdown_LakeLevels_VERIFIED.md` | TWDB daily lake levels through the 2017 drawdown |
| `tools/per_zone_exposure.py` | exposed lakebed per zone, any elevation |
| `tools/per_lot_exposure.py` | exposed lakebed per waterfront lot, address- and zone-joined |
| `ops/zone_exposure_482ft.json` | 28 zones scored at the 2017 floor |
| `ops/lot_exposure_482ft.{json,csv}` | 881 lots — **gitignored, address-level** |

**The numbers that matter**

- 2017 drawdown: normal pool **492.04 ft** → floor **481.69 ft** on **Jan 13** →
  refilled by **Feb 20**. Total drop **10.83 ft** over **~7 weeks**.
- This *corroborates the one-pager's own projections* — "ten-to-twelve-foot
  drop" and "six to eight weeks" — against a state database. Use it.
- Lake-wide exposed at the floor: **559.4 acres** computed vs **523.5** in
  TWDB's published table (ratio 1.07, divergence explained).
- **720 residential lots** with matched addresses. Median **10,625 sq ft**
  exposed. **359** lots over ¼ acre, **70** over 1 acre.
- Zone spread is the sales insight: N6 The Courtyard loses **88%** of its water
  surface, Laguna Loma **75%**, while deep-channel Tarrytown lots see a strip.
  Same lake, different conversation.

Both scripts take `--floor` / `--pool`, so any projected 2026 level re-scores
everything. That is the Priority Assessment line: *"at the projected drawdown
your property fronts roughly X sq ft of exposed lakebed"* — computed from a
bathymetric survey, not estimated.

### 2. Video — built, but on the wrong footing

`06_Media_Build/DRAWDOWN_Truxor_916_FINAL.mp4` (77s, 9:16) plus a
`_COMPAT.mp4` in standard colour range. Cut from **real ATX Truxor photography**
with camera moves — no generated imagery, no picture credits spent.

Honest status: **do not ship it.** Reasons in order of severity:

1. It was produced outside the ATX-Media-Mogul studio and never passed Gate 0.
2. Its cards use Arial and my own palette; campaign law
   (`AGENTS.md`) specifies **Cormorant Garamond + Source Sans 3**,
   `#f7f5f0 / #c4923a / #1a1a1a`.
3. The VO is a synthetic scratch track. The line *"I'll tell you that to your
   face"* in a generated voice is a contradiction the ear catches.
4. It predates the exposure numbers, which are stronger than anything in it.

---

## The expensive lesson

**A governed production system already existed and this work happened outside
it.** `ATX-Media-Mogul` has five gates (G0 greenlight → G1 selects → G2
grade-strip → G3 draft → Routing), a Gate 0 pillar checklist, and
`lore/canon/HIGGSFIELD-LEARNINGS.md`.

**Rule 11, LOCKED 2026-07-28**, says specialty equipment cannot be
text-generated — learned on *these same drawdown reels* for 88 credits.

This session independently re-derived that rule by auditing seven clips
frame-by-frame, then wrote a competing 6-gate process document. The rediscovery
was correct and entirely unnecessary.

Root cause: `~/drawdown-2026-campaign` is a fifth production line with no row in
`STUDIO-WORKFLOWS.md`, no `gate-log.md`, and no route to canon. Filed as
`ATX-Media-Mogul/learning/amendments/AMEND-2026-08-04-01`.

`MEDIA_Production_Process_v1_2026-08-03.md` in this repo should be treated as
**superseded** by the studio's gate law, kept only for its four documented
defect post-mortems.

---

## Open items

| # | Item | Owner |
|---|---|---|
| 1 | Accept or reject AMEND-2026-08-04-01; if accepted, open `projects/DRAWDOWN-2026/gate-log.md` | Nate |
| 2 | Record the 9 VO lines in `MEDIA_Script_Drawdown_v1_LOCKED.md` | Nate |
| 3 | Marsh buggy: owned, rented, or subbed? Determines whether manufacturer imagery is usable at all | Nate |
| 4 | `OUTREACH_COMPLIANCE.md` gate before any lot list drives contact | Nate |
| 5 | 104 lots (66.8 ac exposure) fall outside all 39 zone polygons — coverage gap | next session |
| 6 | Re-cut cards in campaign brand (Cormorant/Source Sans, `#c4923a`) | next session |

## Dead ends — do not repeat

- **Google Earth Pro automation.** Opening a KML **resets historical imagery to
  present day**, so scripted captures silently produce current-year frames.
  Sidebar clicks preserve the date; KML opens do not. `tools/capture_2017_frames.py`
  is retained only as a record of the trap.
- **Only one Google aerial exists in the window** — 1/8/2017, at 486.57 ft,
  55% of the way down. No February imagery exists; the runbook's "target
  Feb 1–13" was chasing an already-refilled lake.
- **Manufacturer equipment photos** (16 pulled, `06_Media_Build/equipment-reference/`):
  6 usable, 3 watermarked, 1 was a competitor's logo, all third-party copyright,
  none are ATX machines. Reference only.
