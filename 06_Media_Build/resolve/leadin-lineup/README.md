# Lead-in lineup — Resolve, not ffmpeg

ffmpeg concat is a **preview**. Lineup, fonts, and VO live in **DaVinci Resolve**.
Campaign notes already said this: finish brand fonts + VO in Resolve before post.

## Open

1. DaVinci Resolve (installed).
2. New project: **1080×1920, 24 fps**, Rec.709.
3. Media pool: drop this whole folder (`picture/` + `audio/`).
4. Optional: File → Import Timeline → FCPXML → `LeadIn_lineup.fcpxml` (starting guess only).

## How to cut it

Lock **A1** to a VO clip. Slip **V1** pictures under the words. Do not chop the VO to match a pre-spliced mp4.

| Track | Use |
|-------|-----|
| A1 | `audio/VO_victoria_14s.wav` — short lead-in read (~14s). Start here. |
| A1 alt | `audio/VO_full_77s.wav` — original 77s scratch if you want the long read. |
| A2 | Line stems `VO_L1` … `VO_L8` if you rebuild from the 77s VO. Handles on each. |
| V1 | `picture/V1` hydrilla → `V2` drop → `V3` iron → `V4` $695. Each has handles. |
| V1 alt | `picture/V_leadin_v2_silent16.mp4` — Claude’s silent 16s (C7 card swap). Lay VO on top and slip. |

Suggested starting offsets (24 fps, change in Resolve):

| Picture | Timeline in | Why |
|---------|-------------|-----|
| V1 hydrilla | 00:00 | “Ten years…” |
| V2 drop | ~00:05 | “projected 10–12 ft” |
| V3 iron | ~00:09 | machines |
| V4 $695 | ~00:13 | offer |

Cards are already burned into these picture clips. Replacing type with Cormorant is a **new title track**, not a recut of the stills.

## Do not

- Post `truxor-leadin-15-vo.mp4` (ffmpeg splice — jumps).
- Treat a muxed mp4 as the master.
- Generate new hero stills.

Deliver from Resolve: 9:16, CRF 19 master into `06_Media_Build/`, then copy to Command Center as `draft`.
