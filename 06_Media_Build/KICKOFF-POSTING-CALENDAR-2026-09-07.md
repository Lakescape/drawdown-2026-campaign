# Kickoff — posting calendar (Hermes → Claude) 2026-09-07

Nate: put the posts on the calendar. LCD 30s with the song is the **main attractor**.
Socials + Google Business. Hallie posts. Nothing auto-sends.

## The place (already exists — do not invent a fourth)

| Surface | Path | Job |
|---|---|---|
| Slot list | `06_Media_Build/PRODUCTION_SCHEDULE_2026-09-07.md` | dates |
| Pack builder | `06_Media_Build/build_scheduling_pack.py` | one folder per slot + `caption.txt` |
| Pack | `06_Media_Build/SCHEDULING_PACK/` | Hallie drag-drops into Meta / TikTok / GBP |
| Click calendar | `~/drawdown-2026-campaign/.lavish/calendar/calendar.html` | Nate clicks a tile, file plays |
| Desk | `dcc-close-book` `?closeBook=1&tab=media` | copy caption, not the scheduler |
| Handshake | `weeks/2026-08-31/BOARD.md` | append only |

Rebuild: `python3 build_scheduling_pack.py && python3 build_calendar_page.py`

## Files (kitchen `~/drawdown-2026-campaign/06_Media_Build/`)

| Piece | File | State |
|---|---|---|
| **HERO** Lake Coming Down 30s + song | `DRAWDOWN_LakeComingDown_916_SUNO_BED.mp4` | Nate likes this; Truxor beats in. Desk: `dcc-close-book/public/media/lake-coming-down-v1bed.mp4` |
| Method 15s | `DRAWDOWN_ScrapeHaulStaple_916_SUNO_MudWindow_v2.mp4` | signed |
| Turnkey 18s | `DRAWDOWN_Turnkey_916_SUNO_BED.mp4` | **DRAFT — Gate 3** |
| Work the Bed 30s | `DRAWDOWN_WorkTheBed_916_STUDIO_CountryA_from28s.mp4` | approved |

Do **not** post: `$695` cuts, `*ViralHydrilla_916_v1*`, barge-as-Truxor, method v2 until pick.

## Spread Nate locked 2026-09-07

- **One magnet:** LCD 30s. Same file on IG Reel, TikTok, FB Reel, lake groups, **and GBP listing video**.
- **GBP:** listing video + one Google Post. Leave it. Do not stack five videos on Maps.
- **Do not** drop method + viral + LCD the same day.
- Turnkey follows **+4–5 days** and only after Nate Gate 3.
- CTA: Text TRUXOR to 254-780-6971. No $695.

## Calendar slots (after rebuild)

| Date | What |
|---|---|
| Mon Sep 7 | Method (already packed) |
| Wed Sep 9 | Viral lead-in + VO |
| Fri Sep 11 | S01 story + S02 feed |
| **Mon Sep 14** | **LCD HERO** IG/TT/FB **+ GBP listing video** |
| Wed Sep 16 | Method rerun |
| Fri Sep 18 | S03 + S07 |
| Mon Sep 21 | Work the Bed |
| Wed Sep 23 | Turnkey **DRAFT** — do not Meta-schedule until Gate 3 |
| Wed Sep 30 | LCD rerun (IG/TT only — GBP stays the Sep 14 listing video) |

## Claude does

1. Confirm pack folders exist for Sep 14 LCD + GBP and Sep 23 turnkey.
2. Rebuild calendar if `pack.json` is stale.
3. Append BOARD (do not overwrite).
4. **Do not post.** Do not Meta-login. Do not GBP-login.
5. If a slot file is missing, stop and name it.

Pickup: `claude attach` in `06_Media_Build`.
