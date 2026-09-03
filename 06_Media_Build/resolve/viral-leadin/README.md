# resolve/viral-leadin — DRAWDOWN_ViralHydrilla_916_STUDIO

**ffmpeg is the preview. Resolve is the finisher.** The mp4 in
`06_Media_Build/DRAWDOWN_ViralHydrilla_916_STUDIO.mp4` is a claim-clean,
QC-passed cut you can post as-is; this bin is what you rebuild it from when you
want the real type pass (Arial is a placeholder — the straps want a Resolve
font pass, per the Grok draft's own self-critique).

Built 2026-08-31 by `06_Media_Build/build_viral_leadin_studio.py`.

## Spec

| | |
|---|---|
| Master | `DRAWDOWN_ViralHydrilla_916_STUDIO.mp4` |
| Duration | **15.30 s** |
| Format | 1080x1920, 30 fps, H.264 CRF 18, yuv420p, +faststart |
| Audio | **silent** (48 kHz stereo AAC null track so IG/TT don't reject it) |
| Beats | 4 plates, 0.35 s crossfades |

## The four plates — pinned by sha256, audited by caption AND eyeballed

| # | In | Sha256 | Mode | Why |
|---|----|--------|------|-----|
| 1 | 0.00 | `f730acf1ac49dae940dcd30e7597b1caa554d6d60fbd1a4b1531b5eb99d069ef` | bleed | HOOK. Looking straight down off a dock deck into weed-choked water. The dock **is** in frame, so "THIS IS UNDER YOUR DOCK." does not overclaim. |
| 2 | 2.95 | `924c9e39682b244ced6fb2cea57ab18a8f81c95cf7a3ea2af904ff2d944206cc` | bleed | STAKES. Clear water, a hydrilla mound you only see when the lake drops. |
| 3 | 6.95 | `c6b6853c038a87b18338b0a6fd0c94a377f84947475caa53cbab3da44d1cff83` | **fit** | CAPABILITY. TWO Truxors on the water, one throwing spray. C7 count + amphibious. |
| 4 | 10.95 | `83f97f1642cd2172ab76216d46fbee631e81d36e942516fc5136febd889ab75c` | bleed | INFORM. Hauled hydrilla mound on a bulkhead, dump trailer behind. Scrape/haul proof. |

**Plate 3 is FIT (letterboxed), not bleed, and that is deliberate.** Native is
1080x810; a 9:16 cover-crop clips the second machine out of frame and breaks the
C7 count. Claim safety beats composition on that shot. Do not "fix" it by
cropping in Resolve.

## Banned on this cut — do not reintroduce

- `@two_machines` / sha `1334bce67b99…` — **a yellow knuckleboom excavator on a
  floating platform.** One machine, no amphibious undercarriage. C7 fail.
  Confirmed against the Poseidon caption this session (`vlm_label=dredging`).
- `@dock_lowwater` — mythology, not fleet evidence.
- `$695`, "credited", "assessment", "walk yours", "I'll tell you to your face" —
  Nate 2026-08-31 stripped the inspection offer from the lead-in.
- Splicing the 77 s scratch VO.
- Any invented slot count.

## Overlay strings — exact

```
0.00–3.30   THIS IS UNDER
            YOUR DOCK.

2.95–7.30   NEARLY TEN YEARS
            SINCE ANYONE COULD SEE IT.

6.95–11.30  TWO TRUXORS.
            PROJECTED 10–12 FT.
            NOTHING IS OFFICIAL YET          (copper)

10.95–15.30 SCRAPE. HAUL. STAPLE.
            254-780-6971                     (copper, holds to last frame)
```

## Ledger trace (`../../MEDIA_ClaimLedger_Drawdown_v1.md`)

| Card | Row | Hedge |
|---|---|---|
| THIS IS UNDER YOUR DOCK. | none needed — describes the frame | n/a |
| NEARLY TEN YEARS / SINCE ANYONE COULD SEE IT. | **C3** ("first meaningful low-water window in nearly ten years") | C3 does not hedge |
| TWO TRUXORS. | **C7** — two machines, amphibious undercarriage, both in frame | none |
| PROJECTED 10–12 FT. | **C2** | "projected" kept |
| NOTHING IS OFFICIAL YET | **C1** — the hedge, in the same breath, on the same card | mandatory, present |
| SCRAPE. HAUL. STAPLE. | service description, not a metric claim | n/a |

**C1 is never asserted on this cut** — nothing says the drawdown is happening.
The only number is hedged twice (`PROJECTED` + `NOTHING IS OFFICIAL YET`).

## Files

- `stills/01–04_*.jpg` — the original Poseidon plates, untouched, named by sha.
- `stills/QC_t*.png` — the QC frames pulled from the master.
- `composites/comp_v*.jpg` — 1350x2400 composites the Ken Burns runs on.
- `composites/card_v*.png` — 1080x1920 type cards (native res, never resampled).

## Rebuild

```bash
cd ~/drawdown-2026-campaign/06_Media_Build
python3 build_viral_leadin_studio.py
```

## Known ffmpeg trap this build hit

`-loop 1 -i still.jpg` defaults to **25 fps** while `zoompan(fps=30)` labels the
output 30 fps. Every beat then runs 5/6 of its nominal length, the xfade offsets
walk past the end of their inputs, and the whole cut collapses onto the last
plate — silently, with a clean exit code. Caught by QC frame extraction, not by
ffmpeg. Fix is `-loop 1 -framerate 30 -i`. **Always QC-extract mid-beat frames;
a green render proves nothing.**
