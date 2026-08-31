# Script 01 "The Exposed Truth" — sha-pinned shot list + audit

Render: `DRAWDOWN_ExposedTruth_916_DRAFT.mp4` · 1080x1920 · 30fps · 360 frames
· 12.000s · silent · REAL-ONLY (Rule 11 — no i2v, no generated geometry)
Recipe: `build_exposed_truth.py`. Gate status: **G3 draft, unsigned.**

## Plates used (sha256 pinned in full — a prefix is not a pin)

| Beat | t | sha256 | Carries |
|---|---|---|---|
| 1 | 0.0–4.0 | `b91a25c6c384fd90ae51690299c5a1df617b8699a3d474d417500ba025e40fa3` | eroded bank meeting shallow water |
| 2 | 4.0–7.0 | `b0e39a623f7c4756cfba906edb7f54f4be9f487b36059988cd2bc5d882cc3949` | sediment shelf above shallow water |
| 3 | 7.0–10.0 | `b0e39a623f7c…` (same plate, push continues) | as above |
| 4 | 10.0–12.0 | — paper end card, no plate | CTA |

## Overlay strings (exact)

```
10 YEARS OF HIGH WATER / HID THIS
SEDIMENT SHELVES YOU / CAN'T SEE AT FULL POOL
A PROJECTED DRAWDOWN MAKES IT / VISIBLE — AND FIXABLE
$695 ASSESSMENT. / 100% CREDITED.
```

Ledger: C3 (nearly ten years) unhedged — correct. C1/C2 require the drawdown
hedge; **"A PROJECTED drawdown"** carries it on screen, in the same breath, not
in an end card. No line claims the drawdown is happening.

## Audit — 5 plates opened, 3 rejected

Captions are a SEARCH INDEX, not claim evidence. Every plate was opened.

| sha | Caption said | Frame actually showed | Verdict |
|---|---|---|---|
| `ceec62cc3f39` | "staining from water exposure" | dirty concrete walkway cap, no high-water band | REJECT |
| `f77fcd1b3b8b` | "worker … near a wooden dock" | shirtless, chest-deep, no PPE — off-brand | REJECT |
| `083f40bf8835` | "broken decking and exposed piling" | palm frond over a work site; EXIF-rotated 90° | REJECT |
| `b91a25c6c384` | "erosion … exposed soil" | matches | ACCEPT |
| `b0e39a623f7c` | "pile of … sediment" | matches | ACCEPT |

**Two of the three rejects are on the 77s cut's own PICKS list in `compose.py`
(s08 = `083f40bf8835`).** Worth a re-check of that cut's remaining picks.

## Cut from the script, and why

- **"rotting tie-backs"** — the library holds **zero** captions containing
  `bulkhead` or `tie-back`. No frame can carry it, so the phrase is gone rather
  than illustrated with something else. The captioner says "retaining wall" (55)
  and "seawall" (11); trade vocabulary does not appear at all.
- **Beat 3's crew member pointing at damage** — no acceptable plate. The
  "and fixable" turn rides the sediment frame instead.

## Open

- All 3,632 refs are `permission_status = internal_only` and
  `customer_identifiable = 0`. No row is anything else, so the field is an
  untouched default carrying no signal — `status='approved'` (3,557) is the gate
  the 77s cut actually used. Both plates here are approved. Flagging, not blocking.
