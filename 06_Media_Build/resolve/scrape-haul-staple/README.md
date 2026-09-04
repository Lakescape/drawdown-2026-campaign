# resolve/scrape-haul-staple — DRAWDOWN_ScrapeHaulStaple_916_STUDIO

**ffmpeg is the preview. Resolve is the finisher.** The mp4 at
`06_Media_Build/DRAWDOWN_ScrapeHaulStaple_916_STUDIO.mp4` is a claim-clean,
QC-passed cut you can post as-is. This bin is what you rebuild it from when you
want the real type pass — Arial is a placeholder.

Built 2026-09-01 by `06_Media_Build/build_scrape_haul_staple.py`.
Packet: `weeks/2026-08-31/GROK_VIDEO_ScrapeHaulStaple_v1_DRAFT.md`.

## Spec

| | |
|---|---|
| Master | `DRAWDOWN_ScrapeHaulStaple_916_STUDIO.mp4` |
| Duration | **15.00 s** (450 frames) |
| Format | 1080x1920, 30 fps, H.264 CRF 18, yuvj420p full-range (color_range=pc), +faststart |
| Audio | **none.** No stream at all — not a null AAC track (Nate 2026-08-31). |
| Beats | 4 plates, 0.35 s crossfades |

## Beats

**Straps come from this table, not the packet.** The packet is the ask that
went in; its Stage 2 table still cuts the retired `STAPLE. / Woven tarp.
12-inch overlap.` card. Rebuilding from the packet reconstructs an overclaim
this record exists to prevent.

| # | In | Sha256 | Mode | Strap | Why |
|---|----|--------|------|-------|-----|
| 1 | 0.00 | `c6b6853c038a87b18338b0a6fd0c94a377f84947475caa53cbab3da44d1cff83` | **fit** | `SCRAPE.` / `We cut it off the bed.` | Two Truxors working, one throwing spray. C7 count + amphibious undercarriage. |
| 2 | 4.00 | `83f97f1642cd2172ab76216d46fbee631e81d36e942516fc5136febd889ab75c` | **fit** | `HAUL.` / `Off your lot.` | Spoil mound on the work platform with the LOAD TRAIL dump trailer on the bank behind it. |
| 3 | 9.00 | `247ed525d59d` (prefix as pinned in `BEATS`) | **fit** | `COVER.` / `Mat on the bed.` | Green erosion-control matting rolled onto a scraped bed. Honest product, honest strap — a mat, not a tarp. |
| 4 | 13.00 | `870b907f2401c31452ee002d03078b75be932bfcdba8d642e8d5a65abb6e89ac` | bleed | `That's the job.` / `254-780-6971` | Operator POV over the cutter head, cut weed on the rake, clean water beyond. |

## The staple gap — why beat 3 says COVER, not STAPLE

A full sweep of Poseidon's **3,619 VLM captions** for
`staple / overlap / geotextile / weed barrier / landscape fabric / woven tarp /
polyethylene / burlap / coir` returns **zero hits**. Nothing in the library shows
a woven tarp, a stapled seam, or a 12-inch overlap.

The nearest real plates are **green erosion-control blanket / matting on a bank**
— `247ed525d59d` (a crew rolling matting out over scraped muck at the water's
edge), `049c9c5aefa0`, `af49fffbf0ab`, `7a549dd65708`, `4b0528304977`. Different
product, different job. Nate 2026-09-01 ruled it carries the beat as COVER
with matching copy. `247ed525d59d` is filed in `stills/` as
`GAP-CANDIDATE_…` **for Nate's ruling only** — do not cut it under
"Woven tarp. 12-inch overlap." That is the same overclaim class as the
`@two_machines` barge, one notch smaller.

**To close the gap: shoot it.** One frame of woven tarp on a dry bed with the
overlap and a staple visible replaces this card. Do not generate one
(HIGGSFIELD-LEARNINGS Rule 11).

## Deliberate deviation from the packet

The packet pins beat 2 as **bleed**. It ships **fit**. A 9:16 cover-crop of the
1080x810 native keeps the spoil mound and **cuts the dump trailer out of frame**
— and the trailer is the only thing in the picture that makes "Off your lot."
honest. Same rule that makes beat 1 fit. Do not "fix" this by cropping in
Resolve.

Both fit beats **pull out** (1.05 → 1.00) rather than pushing in, so each beat
ends on the complete frame and the claim-critical element (second machine /
trailer) can never be zoomed off the edge.

## Banned on this cut — do not reintroduce

- `@two_machines` / `1334bce67b99…` — a knuckleboom excavator on a floating
  platform. One machine, no amphibious undercarriage. C7 fail.
- Any generated tarp, mat, or machine. Rule 11.
- The inspection unit, "credited", "assessment", "extinct", CY volumes — Nate 2026-08-31.
- "exploring", "unofficial", "nothing is official yet" — **the drawdown is
  official** (Nate 2026-08-31). None of it appears on this cut.

## Contents

- `stills/` — source plates at native resolution, sha in the filename
- `composites/` — the 1350x2400 beat composites and the 1080x1920 strap PNGs
- `qc/` — the four mid-beat extractions this cut was verified against

## 2026-09-04 — orientation fix

`247ed525d59d` carries a stale EXIF Orientation=6 tag over upright 1080x810
pixels; the 09-01 build trusted the tag and shipped the COVER beat rotated 90
degrees. The builder now checks EXIF-transposed orientation against the
registry's `refs.width/height`, ignores a lying tag (printed, never silent),
and fails closed on any remaining mismatch. Master rebuilt + re-QC'd
2026-09-04, md5 `2e68544f616ce8f0…`; `qc/` and `composites/` in this bin are
from the rebuilt cut (`card_b3.png` was also missing before this refresh).
Full record: `weeks/2026-08-31/BOARD.md`, 2026-09-04 correction.
