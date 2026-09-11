# LCD v2 — ROUND 6 (plates)

`renders/LCD_v2/_r6/LCD_v2_916.mp4` · 1080×1920 · 30 fps · **900 frames / 30.000 s** ·
h264 yuv420p · faststart · md5 `e8c658f043acf938c70d34d5e06621af` · 32,105,105 bytes.

Rendered 2026-09-10 beside round 5 (`LCD_OUT=…/_r6`), compared against round 5 in
`_r6/BEFORE_AFTER.png`. Round 5's outputs were not written to. **Nothing posted. Not signed.**

## What this round is

Every round before this one graded, sharpened and scrimmed the same two soft plates:
`8c7fd940fc1f` (1080×607, covered **3.16×** for the hook) and `5a4942b7731d` (1080×810,
covered 2.37×, a reflected sky on still water). Round 4's own Known-gaps list named the
consequences — gap 8 *"the first 12.9 s are the softest frames in the film, and no grade
fixes that … the only real fix is a higher-resolution aerial"* and gap 6 *"the hydrilla
beats read cool and steel-blue"*. Both were the plates, not the chain.

**The plates exist.** `~/Library/CloudStorage/GoogleDrive-…/My Drive/Oyster Landing
Businesses/Cut areas drone footage/` holds 30 DJI Fly drone stills from **2025-10-13**,
4096×3072, top-down over the Oyster Landing (Lake Austin) docks: dock fingers with boats in
their slips, sitting in a solid hydrilla mat. A 9:16 window on one is **1728×3072 native** —
the hook is a downsample for the first time in this film.

Four are now sha-pinned in the Poseidon registry (`~/Poseidon/visual-library/library.db`,
bytes at `visual-library/photos/<sha>.jpg`, originals copied to
`~/Poseidon/projects/oyster-landing-cut-areas-2025-10-13/photos/`):

| sha256 (12) | source file | used as | registry |
|---|---|---|---|
| `d6ac3e52945b` | `dji_fly_20251013_122500_0318_…_photo.JPG` | **01a — the hook** (DRAWDOWN 2026) | `pending_approval` · `customer_identifiable=1` |
| `7c078e758eeb` | `dji_fly_20251013_122532_0323_…_photo.JPG` | **02a** (ABOUT 10 FEET) | same |
| `ee147aed310d` | `dji_fly_20251013_122520_0321_…_photo.JPG` | **02b** (ABOUT 10 FEET, hard cut at f277) | same |
| `f21311051e34` | `dji_fly_20251013_122454_0317_…_photo.JPG` | hook alternate, unused | same |

`customer_identifiable=1` is deliberate: these are a commercial client's docks and their
customers' boats. `permission_status` is the ingest default `internal_only`. **Nate signs the
plates at Gate 0** — the registry row is a pin, not a clearance.

## Every changed line vs round 5

`git diff 4e9c2ae -- 06_Media_Build/build_lcd_v2.py`. Functional changes and nothing else:

| # | line | round 5 | round 6 | why |
|---|---|---|---|---|
| 1 | `SHOTS` 01a | `8c7fd940fc1f`, pan 0.18, sat 45, warm −0.022, sharp 1.05 | `d6ac3e52945b`, pan 0.42, sat 56, warm 0, sharp 0 | the hook plate. No unsharp — nothing to rescue |
| 2 | `SHOTS` 02a | `5a4942b7731d`, pan 0.62, sat 40, warm −0.008, sharp 0.60 | `7c078e758eeb`, pan 0.55, sat 54, warm 0, sharp 0 | hydrilla beat, plate 1 |
| 3 | `SHOTS` 02b | `5a4942b7731d`, pan 0.33 (same plate) | `ee147aed310d`, pan 0.45 | hydrilla beat, plate 2 — a real hard cut at f277, the 03a/03b shape |
| 4 | `CARD_PLATE` s1 / s2 | `8c7fd940fc1f` / `5a4942b7731d` | `d6ac3e52945b` / `7c078e758eeb` | the copy guard pins each card to the plate it rides; it correctly refused the first run |
| 5 | `EYE_TARGET` | 39.0 | 33.0 | see §scrim |

**Untouched:** every string (copy guard passes on the same 19, CTA verbatim and once), every
cut frame, the beat grid, the grade curve, both scrim geometries, the type scale, all rules,
the end card and its stagger, `SEAM_F`/`SEAM_LIFT`, the safe box, the audio chain, the navy
end-card ground and its `8c7fd940fc1f` wash at 15 % (directive A — the film still ends on the
lake). Plates 03a/03b/04a/04b unchanged.

## The scrim, and why one constant moved

The lower scrim is ONE value solved against the worst eyebrow ground in the film. With
`EYE_TARGET = 39` that ground (131.9, the Truxor beat) solved to **0.79** — and at 0.79 the
bronze eyebrows measured **4.33:1** on the green mat and on the Truxor plate, under the 4.5
floor. `33` solves to **0.84**, the exact value round 5 delivered. Same craft cost round 4
already stated (16 % of the picture through the band, measured motion halves under it);
no new cost.

## Everything measured, round 5 → round 6

| | round 5 | round 6 |
|---|---|---|
| frames / duration | 900 / 30.000 s | 900 / 30.000 s |
| hook plate, cover factor | 1080×607, **3.16× up** | 4096×3072, **0.63× down** |
| deepest ink | y 1362 (74 px clear) | y 1362 |
| left edge, margin ink x0 | {82, 83, 84} | {82, 83, 84} |
| directive C, YAVG spread f0–f10 | +0.42 PASS | **+0.39 PASS** |
| f0 YAVG (the thumbnail) | 82.2 | **64.1** |
| loop seam f899 → f0 | +7.5 | **−10.5** (target ≤ ±12) |
| YAVG step at each cut | f607 was **−9.8**, the one outside ±8 | 0.4 · −3.4 · 0.5 · 7.1 · −3.4 · −0.5 · 5.7 — **all inside ±8** |
| lower scrim | 0.84 | 0.84 |
| directive A, `cta_number` worst-local | 8.82:1 | **8.82:1** PASS (floor 7.0) |
| lockup worst-local | 6.71:1 | **9.31:1** PASS (floor 6.0) |
| worst eyebrow | 4.76:1 (`s3_eyebrow`) | **5.06:1** PASS |
| directive E, payoff min (delivered / picture) | 1.41 / — | **1.41 / 2.47** PASS (floor 1.0) |
| cuts / scene changes | 5.567 · 9.233 · 12.9 · 16.567 · 20.233 · 23.9 | identical |
| loudness | I −14.0 · LRA 7.7 · TP −2.0 | **identical** (audio chain untouched) |
| TikTok dead zones | CLEAR | **CLEAR** |
| contrast failures | `end_tag` f894–899 | **`end_tag` f894–899 only** — carried, see below |

## Known gaps — round 4's nine, re-read against this build

| # | gap | state |
|---|---|---|
| 1 | loop seam | **closed in r5, still closed** (−10.5; the sign flipped because f0 is now the darker frame) |
| 2 | end-card bottom void on the GBP cut | open — one constant `BOX[3]` and a GBP variant; not this round |
| 3 | `s3_eyebrow` thinnest margin | **improved** 4.76 → 5.06 |
| 4 | the 0.84 lower gradient is heavy | open — unchanged; the plate-side fix is still the honest one |
| 5 | −9.8 YAVG step at f607 | **closed** — −3.4; the new hydrilla beats sit closer to the Truxor plate |
| 6 | hydrilla reads cool / steel-blue | **closed** — the plate is green; per-shot sat 54, no cool trim |
| 7 | no scene change crosses 0.25 full-frame | open — same chain, same reason |
| 8 | first 12.9 s are the softest frames | **closed** — every plate in the film is now ≥ 1080 native in the window |
| 9 | no platform round trip | open — nothing posts |
| r5 | `end_tag` bronze under 4.5:1 for f894–899 (200 ms, the seam ramp) | **carried, unchanged** — r5 named it a taste call (fade the tag under the ramp, or `SEAM_LIFT = 0.0`); still Nate's |

## How this render was produced

```bash
cd ~/drawdown-2026-campaign/.claude/worktrees/platform-native-renders/06_Media_Build
R=$PWD/renders/LCD_v2
LCD_OUT=$R/_r6 LCD_CMP_REF=$R/_r5/LCD_v2_916.mp4 \
  LCD_CMP_A="r5  ROUND 5" LCD_CMP_B="r6  ROUND 6 (plates)" python3 build_lcd_v2.py
```

`LCD_OUT` must be absolute — a relative value makes the concat `list.txt` double the path.

## What this does NOT do

- Does not touch `SCHEDULING_PACK/`. The pack still ships round 5 (`f23ec45d…`) in three
  slots, and round 5 was never signed either — that is the open finding from 09-10, not
  something this round fixes. Sign r5 or r6; then the pack rebuilds from the signed master.
- Does not post. Does not change the Sep 7 `DRAWDOWN_LakeComingDown_916_SUNO_BED.mp4` the
  schedule doc names as signed.

**Nothing posts. Nate sees it first.**
