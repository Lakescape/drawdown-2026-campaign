# Gates 4–6 record: DRAWDOWN Truxor cut v1

Deliverable: `DRAWDOWN_Truxor_916_FINAL.mp4` — 1080x1920, 77.25s, 24fps, 29 MB.
Built entirely from **real ATX photography** in `~/Poseidon/visual-library`.
Zero generated imagery. Zero generation credits spent on picture.

## Method — stills with camera moves, NOT image-to-video

Image-to-video was available and was deliberately not used. These are real
machines on a real lake making a specific factual claim about equipment and
count. A generative model asked to animate them will invent geometry — a
pontoon that morphs, a third machine that fades in. That is precisely the
failure the claim ledger exists to prevent, and no amount of QC downstream
makes an invented frame acceptable.

Motion is Ken Burns pushes and pulls over true frames, alternating direction,
slowed on longer holds so the move never reaches its limit early.

## Shot list (as built)

| # | In | Dur | sha256 | Mode | Carries |
|---|---|---|---|---|---|
| 1 | 0.0 | 5.0 | `924c9e39682b` | bleed | L1 submerged hydrilla — "never actually seen it" |
| 2 | 5.0 | 4.8 | `43f28fb00bb4` | bleed | L1 canal mat + far-bank bulkhead |
| 3 | 9.8 | 4.7 | `0beab2b84bbe` | bleed | L2 muddy exposed bank |
| 4 | 14.5 | 4.7 | `b91a25c6c384` | bleed | L2 eroded bank at waterline |
| 5 | 19.2 | 6.8 | `870b907f2401` | bleed | L3 calm water — the honest beat |
| 6 | 26.0 | 6.0 | `fd49bf6ffe3e` | **fit** | **L4 two Truxors staged — C7 count** |
| 7 | 32.0 | 5.0 | `83f97f1642cd` | bleed | L5 weed pile on bulkhead |
| 8 | 37.0 | 5.3 | `083f40bf8835` | bleed | L5 damaged dock, exposed piling |
| 9 | 42.3 | 5.2 | `b0e39a623f7c` | bleed | L6 sediment pile |
| 10 | 47.5 | 6.3 | `cd351a221a00` | bleed | L6 Truxor beside cut-weed pile |
| 11 | 53.8 | 9.4 | `c6b6853c038a` | **fit** | **L7 two Truxors working — C7 count + capacity** |
| 12 | 63.2 | 5.3 | `ca77ddebe73b` | bleed | L8 two Truxors docked, calm |
| 13 | 68.5 | 6.2 | `360fb66761d0` | bleed | L8 calm water and lawn |
| 14 | 74.7 | 2.5 | `84a901e3a7c3` | bleed | L9 dock + boathouse — Lake Austin |

**Why two shots are `fit` and not full-bleed.** Both count shots are 1080x810
native — Jobber's ceiling; the "originals" on disk are the same size, and the
library holds no high-res two-machine alternate (only 4 Truxor photos exceed
1600px, none showing a pair). A 9:16 crop clips the second machine on both,
which breaks C7 outright. A 4:5 crop keeps both but needs a 1.7x upscale. So
they run at full canvas width, 4:3, native sharpness, framed as a
photo-with-caption. **Claim integrity beat composition.**

## Gate 6 QC — defects found and fixed

| # | Defect | Detected by | Fix |
|---|---|---|---|
| 1 | Photos floating small in a large blurred field; cards stranded on empty blur | frame sampling | full-bleed 9:16 cover-crop for 12 of 14 shots |
| 2 | Outro so dark the image under the lockup was unreadable | frame sampling | scrim alpha 210 → 165 |
| 3 | After the bleed fix, the two count shots looked worst by contrast | frame sampling | see #4 |
| 4 | `PIL.thumbnail()` silently refuses to upscale, so fit shots pasted at 1080 native onto a 1350 canvas — the "bigger crop" fix made them *smaller* | reading the frames, not the code | explicit `resize()` to canvas width |

Defect 4 is the instructive one: the code was correct in intent and the change
was applied, but the output moved the wrong direction. Only looking at the
rendered frame catches that class of bug.

## Count verification — the claim that matters

`TWO AMPHIBIOUS MACHINES` window (27.0–31.5s): sampled 28s, 29s, 30s, 31s —
**exactly two Truxors in every frame.**

`ROUGHLY 25 WORKING DAYS` window (55.5–62.5s): sampled 57s, 58s, 60s, 61s, 62s —
**exactly two Truxors in every frame.**

This is the check that failed in the generated-footage cut, where a third
machine drifted through frame mid-shot. Sampling one frame per card would have
passed that cut too. Sample the window, not the thumbnail.

## Remaining gaps — honest

- **VO is a synthetic scratch track.** Nate reads the final. "I'll tell you that
  to your face" in a generated voice is a contradiction the ear catches.
- **No bulkhead/tie-back structural imagery.** L5 is carried by an exposed
  piling and a weed pile against a retaining wall — adjacent, not exact. The
  library documents weed removal and dredging; the offer sells structural
  shoreline work.
- **No drawdown footage exists** — by definition, it hasn't happened. Every
  low-water frame is normal-pool shoreline, which is honest but not dramatic.
- **:45 cutdown not built** — lines 1,2,3,4,7,8,9. Trivial once the real VO lands.
