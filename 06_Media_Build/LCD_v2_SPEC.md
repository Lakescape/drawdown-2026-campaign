# LCD v2 — BUILD SPEC (locked)

`DRAWDOWN_LakeComingDown_916_v2.mp4` · 1080×1920 · 30 fps · **900 frames = 30.000 s**

Winner: **PREMIUM BRAND FILM (Littoralis-grade)** — 2 of 3 judges, and the only
treatment scoring 9 on doctrine with all three. Every word on screen is a word
Nate already approved, the full date table survives, the Truxor beat survives,
the locked CTA is added and holds four seconds. Craft grafts below come from the
other two treatments where they do not contradict it.

**Read-only boundary.** Nothing under
`/Users/austinlakescapes/drawdown-2026-campaign/06_Media_Build` is written, moved
or renamed. It is imported (`resolve`, `clip`, `BANNED`, `COUNT`,
`C7_TWO_MACHINE`) and read as bytes (the bed). All new code goes in
`…/.claude/worktrees/platform-native-renders/06_Media_Build/`; every output goes
under `…/renders/LCD_v2/`. Nothing posts. No logins. Offline.

---

## 0. Provenance correction — read this before touching copy

`BUILDER-MAP.md` says the shipped master came from `build_timeline_cut.py`'s
`lake-coming-down` cut. **It did not.** Verified this session by direct read:
the master's on-screen words are `build_lake_coming_down.py`'s `CARDS` block
(lines 36–45) and `TIMELINE_CARD` block (lines 47–57), verbatim, and appear
nowhere in `build_timeline_cut.py`. Anyone rebuilding off BUILDER-MAP alone
ships the wrong words.

v2 keeps **`build_lake_coming_down.py`'s copy** (the words Nate saw and
approved) and borrows **`build_timeline_cut.py`'s `resolve()`/`clip()`
mechanism** (sha-pin + local-bytes + EXIF-vs-registry orientation guard).

Bed version: `02_LakeComingDown_v1.mp3`, offset 0.0 s. `build_lake_coming_down.py`'s
docstring says v2; the wired `CUTS` entry and Victoria's 2026-09-06 Cut Room pick
both say v1, and every timing below is measured against v1. **A swap to v2
invalidates the entire cut map** — re-measure, do not re-mux.

---

## 1. Sources — all four verified on disk this session

| Slot | Absolute path | Verified |
|---|---|---|
| clip 008 | `/Users/austinlakescapes/ATX-Jobs/06_Drawdown_Sales_Engine/00-source/aerials/2026-08-11-drawdown-scouting/2026-08-11_la-rob-roy_drawdown-scouting_drone-wide_008.mp4` | 1280×720 · 30 fps · 115.232 s |
| clip 018 | `…/2026-08-11_la-rob-roy_drawdown-scouting_drone-wide_018.mp4` | 1280×720 · 30 fps · 25.266 s |
| clip 014 | `…/2026-08-11_la-rob-roy_drawdown-scouting_drone-wide_014.mp4` | 1280×720 · 30 fps · 129.099 s |
| plate C7 | `/Users/austinlakescapes/Poseidon/visual-library/photos/c6b6853c038a87b18338b0a6fd0c94a377f84947475caa53cbab3da44d1cff83.jpg` | 1080×810 · registry match · **in `C7_TWO_MACHINE`** |
| plate haul | `/Users/austinlakescapes/Poseidon/visual-library/photos/cd351a221a006e2ad2efe8a172cdb45ac3a541fb67076f81705805b27dd552d2.jpg` | 1080×810 · registry match |
| bed | `/Users/austinlakescapes/drawdown-2026-campaign/06_Media_Build/audio/suno/02_LakeComingDown_v1.mp3` | 36.97 s, trimmed 0:30 |

Resolve plates by prefix through the imported `resolve()` — never hard-code the
sha path above; it is listed only as proof the bytes exist.

---

## 2. The beat grid — cuts are the mix, not the clock

Measured offline (`renders/LCD_v2/analysis/beatgrid.py`, numpy spectral-flux
onset envelope + autocorrelation). **Graft from KINETIC TYPE — it is the only
number in the set three judges could not make lie, and it is already on disk.**

- **136.00 BPM · beat 0.44118 s · bar 1.76471 s · downbeat phase +0.2206 s**
- Downbeat frames @30 fps: **f7 60 112 165 218 271 324 377 430 483 536 589 642 695 748 801 854 907**
- Strongest onsets: 29.33 · 19.16 · 15.21 · 21.39 · 24.92 · 28.90 · 25.80 · 25.37 · 22.27 · 10.80 · 30.22 · 28.46 · 14.33
- RMS energy holes (where a black frame may go): **7.0–8.6 s**, 11.0 s, 18.0 s, 25.0 s

**Conflict resolved.** The winner cut its Truxor beat at 9.900 s off a 0.32 s-granularity
RMS sample. The beat grid resolves the same swell at **10.800 s (f324)**, which is
both a computed downbeat *and* a top-ten onset. The higher-resolution measurement
wins: **every picture boundary in v2 is a downbeat frame.** The reveal is still on
the loudest thing in the first half — it is now on the transient rather than 0.9 s
into the decay.

**Transition rule, one sentence:** *hard cut where the mix hits, one 0.5 s
dissolve on the only rise that is not a hit, and one 7-frame hard black in the
music's own hole.* Nothing else. No wipes, no slides, no second `xfade` mode.

| Boundary | Frame | t | Type | Why |
|---|---|---|---|---|
| 1→2 | f112 | 3.733 (midpoint 3.750) | **0.5 s dissolve** | the 3.2–3.8 s swell is a rise, not a hit |
| black in | f218 | 7.267 | hard | downbeat inside the 7.0–8.6 s RMS hole |
| black out | f225 | 7.500 | hard | 7 f is the floor — shorter reads as a decode glitch |
| 2→3 | **f324** | **10.800** | **hard** | **THE TRUXOR BEAT** — downbeat + top-ten onset |
| 3→4 | f536 | 17.867 | hard | downbeat, 17.28–17.60 hit cluster |
| 4→5 | f642 | 21.400 | hard | downbeat, onset 21.39 (4th strongest) |
| 5→6 | f748 | 24.933 | hard | downbeat, onset 24.92; card arrives, then gets hit at 25.37 and 25.80 |

---

## 3. Frame geometry (fixed for all 30 s)

- Sharp source band **1080×608 at y 470–1078** — seated above optical centre.
  Every source is *downscaled* into it (1280×720 proxies, 1080×810 plates). **No
  upscaling anywhere.**
- Behind it, a cover of the same frame, blurred and pushed toward navy, fills
  1080×1920. One ground colour across six different sources.
- **2 px bronze hairline** on the band's top edge (y=470) and bottom edge (y=1076).
- Navy field above carries the lockup; navy field below carries the lower-third.
- **Nothing is centred anywhere in the film, including the end card.** Everything
  flush left at **x = 60**. *(Graft from EDITORIAL — the hard flush-left grid is
  the one move that kills the reused-centered-slab tell, and it costs nothing.)*

**No 2.39 letterbox.** At 1080 wide it is a 452 px band with 1,470 px of dead
navy under it — a poster, and a poster is what Nate already rejected.

---

## 4. Shot table — 0 → 30 s

Text positions are **Pillow draw origins** (`d.text((x, y), …)`, default anchor),
because that is what the builder calls. Ink extents are the measured
`textbbox` offsets. All widths measured this session against the real font files.

### Shot 1 — f0–f111 · 0.000–3.733 · clip 008 @ in = 100.0 s

| Element | Text (verbatim) | Font / size | x | origin y | width | ink y | in / out |
|---|---|---|---|---|---|---|---|
| Lockup | `ATX LAKESCAPES` | DM Sans 700 / 26 / +0.18em | 60 | 156 | 281 | 163–182 | f0–f12; **never animates again** |
| Lockup tick | — | bronze 80×2 | 60 | 200 | 80 | 200–202 | with lockup |
| Rule | — | bronze 120×2 | 60 | 1150 | 120 | 1150–1152 | f18–f30 |
| Eyebrow | `LAKE AUSTIN` | DM Sans 700 / 30 / +0.20em | 60 | 1180 | 251 | 1188–1210 | f24–f36 |
| Headline | `DRAWDOWN 2026` | DM Serif Text 400 / 96 | 60 | 1240 | **770** | 1274–1341 | f30–f42 |

Motion: band push **1.000 → 1.025** over 112 f, cubic-out. Clip at 1/1.6 speed,
deshake + minterpolate. Type out f96–f104 (8 f), clear of the dissolve.
Sound: bed fades in over f0–f15; the 3.2–3.8 s swell breaks on the dissolve.

### Shot 2a — f112–f217 · 3.733–7.267 · clip 018 @ in = 8.0 s

| Element | Text | Font / size | x | origin y | width | ink y | in / out |
|---|---|---|---|---|---|---|---|
| Rule | — | bronze 120×2 | 60 | 1150 | 120 | 1150–1152 | f124–f136 |
| Eyebrow | `LCRA: Oct 12 – Nov 24` | DM Sans 700 / 30 / +0.20em | 60 | 1180 | 435 | 1188–1210 | f130–f142 |
| Headline | `ABOUT 10 FEET` | DM Serif Text 400 / 96 | 60 | 1240 | 646 | 1274–1341 | f136–f148 |

Motion: push **1.025 → 1.000** over 106 f. Type out f206–f214 — **the type is
gone before the black.** A black frame over live type reads as a decode glitch.

### — f218–f224 · 7.267–7.500 · **HARD BLACK #000000, 7 frames, no type**

*Graft from KINETIC TYPE (named by two judges). Not graded — must be true 0,0,0.
Cut in and cut out, never faded.* It sits in the measured 7.0–8.6 s RMS hole:
the music drops out, so does the picture. This is the one extra picture event
that answers the winner's only real weakness (fewest events of the three), and
it costs one `color=c=black` segment.

### Shot 2b — f225–f323 · 7.500–10.800 · clip 018 @ in = 10.5 s — **NO TYPE**

Picture only, 3.3 s. *Graft from EDITORIAL (named by two judges): silence on the
type layer is what makes the next card land, and it is the cheapest way to stop
reading as a template.* In-point 10.5 s continues the same drone drift across the
black (8.0 + 2.354 s of source consumed by 2a, + 0.146 s across the black at
1/1.6). Motion: push 1.000 → 1.020.

### Shot 3 — f324–f535 · 10.800–17.867 · **THE TRUXOR BEAT** · plate `c6b6853c038a`

C7-verified: exactly two machines, amphibious undercarriage visible. Centre-cropped
1080×810 → `crop=1080:608:0:101`.

| Element | Text | Font / size | x | origin y | width | ink y | in |
|---|---|---|---|---|---|---|---|
| Rule | — | bronze 120×2 | 60 | 1150 | 120 | 1150–1152 | f330–f342 |
| Eyebrow | `COMMITTED IN JULY` | DM Sans 700 / 30 / +0.20em | 60 | 1180 | 393 | 1188–1210 | f336–f348 |
| Headline L1 | `TWO AMPHIBIOUS` | DM Serif Text 400 / 76 | 60 | 1210 | 620 | 1236–1290 | f342–f354 |
| Headline L2 | `TRUXORS` | DM Serif Text 400 / 76 | 60 | 1304 | 330 | 1330–1384 | f342–f354 |

Leading 94 px. Motion: push **1.000 → 1.030** over 212 f (3 % is the ceiling on a
plate this size). Type out f512–f520.
**The count word `TWO` rides `c6b6853c038a`, which is in `C7_TWO_MACHINE` — the
imported `COUNT` guard passes it and fails any future edit that moves it.**

### Shot 4 — f536–f641 · 17.867–21.400 · clip 014 @ in = 60.0 s

| Element | Text | Font / size | x | origin y | width | ink y | in / out |
|---|---|---|---|---|---|---|---|
| Rule | — | bronze 120×2 | 60 | 1150 | 120 | 1150–1152 | f542–f554 |
| Headline | `WE WORK THE BED` | DM Serif Text 400 / 88 | 60 | 1240 | **762** | 1271–1333 | f554–f566 |

No eyebrow — this beat has none in the master. Motion: push 1.025 → 1.000.
Type out f620–f628.

### Shot 5 — f642–f747 · 21.400–24.933 · plate `cd351a221a00` (Truxor beside the cut-weed mound)

**Graft from KINETIC TYPE — one word per beat across three consecutive beats.**
Judge 1: *"the only moment in any treatment that a viewer would rewatch."* The
three words and their order are the master's verbatim `SCRAPE · HAUL · COVER`;
only the separator glyph and the line breaks change, which is layout, not copy.

| Element | Text | Font / size | x | origin y | width | ink y | lands |
|---|---|---|---|---|---|---|---|
| Rule | — | bronze 120×2 | 60 | 1096 | 120 | 1096–1098 | f642 |
| L1 | `SCRAPE` | DM Serif Text 400 / 88 | 60 | 1126 | 309 | 1157–1219 | **f642** (beat) |
| L2 | `HAUL` | DM Serif Text 400 / 88 | 60 | 1220 | 224 | 1253–1313 | **f655** (beat) |
| L3 | `COVER` | DM Serif Text 400 / 88 | 60 | 1314 | 272 | 1345–1407 | **f668** (beat) |

Leading 94 px, same as the shot-3 two-line block — one number, not two. Three
consecutive beats at 0.441 s (13.24 f) apart. 8-frame in each, the fastest type
in the film, on the flattest part of the bed. Nothing else moves. No type-out —
the hard cut at f748 kills it. Motion: push 1.000 → 1.025.

### Shot 6 — f748–f899 · 24.933–30.000 · **END CARD** — solid navy `#1B2A4A`, no photograph

The master's full date table, verbatim, intact. Nothing moves once it is up.

| Element | Text (verbatim) | Font / size | x | origin y | width | ink y | in |
|---|---|---|---|---|---|---|---|
| Lockup | `ATX LAKESCAPES` | DM Sans 700 / 26 / +0.18em | 60 | 156 | 281 | 163–182 | held from f0 |
| Lockup tick | — | bronze 80×2 | 60 | 200 | 80 | 200–202 | held |
| Title | `LAKE AUSTIN DRAWDOWN` | **DM Serif Text 400 / 64** | 60 | 470 | **766** | 493–538 | f748–f760 |
| Rule | — | bronze 180×2 | 60 | 576 | 180 | 576–578 | f748–f760 |
| Date 1 | `Oct 12 — Lowering begins` | DM Sans 400 / 40 | 60 | 660 | 477 | 671–709 | f752–f764 |
| Date 2 | `~3 weeks to target` | DM Sans 400 / 40 | 60 | 732 | 351 | 743–781 | f756–f768 |
| Date 3 | `Nov 2–24 — Dry floor window` | DM Sans 400 / 40 | 60 | 804 | 554 | 815–853 | f760–f772 |
| Date 4 | `Nov 24 — Refill starts` | DM Sans 400 / 40 | 60 | 876 | 396 | 887–916 | f764–f776 |
| Date 5 | `Nov 30 — Normal pool` | DM Sans 400 / 40 | 60 | 948 | 417 | 959–997 | f768–f780 |
| Rule | — | bronze 180×2 | 60 | 1100 | 180 | 1100–1102 | f764–f776 |
| **CTA** | **`Text TRUXOR to 254-780-6971`** | **DM Sans 700 / 52 / +0.02em** | **60** | **1150** | **809** | **1164–1203** | **f768–f780** |

**Title is 64 px, not 72.** Measured: at 72 px `LAKE AUSTIN DRAWDOWN` is **862 px**
wide → right edge 922, outside both the 840 cap and the x=900 wall, and the
build guard would abort. At 64 px it is **766 px** → right edge 826. *(Caught by
judge 3; confirmed by measurement this session. Two more of the winner's estimates
were also wrong and are corrected above: `WE WORK THE BED` is 762 not ~690,
`TWO AMPHIBIOUS` is 620 not ~555 — both still fit.)*

**CTA at full opacity from f780 to f899 — 26.000 s → 30.000 s, exactly 4.000 s.**
The last date finishes building on the same frame. Nothing on screen moves for
the last four seconds; stillness is the punctuation.

---

## 5. Type system

Loaded by **absolute path** with `ImageFont.truetype()`. `fc-list` cannot see
these — they are not in `~/Library/Fonts` — which is irrelevant, because all type
is Pillow-rendered. Any tool that picks fonts by *name* (Resolve, AE, a font
dialog) will silently substitute; installing the four TTFs into `~/Library/Fonts`
would close that trap.

```
SERIF = /Users/austinlakescapes/ATX-Proposal-System/fonts/DMSerifText-400.ttf
SANS7 = /Users/austinlakescapes/ATX-Proposal-System/fonts/DMSans-700.ttf
SANS4 = /Users/austinlakescapes/ATX-Proposal-System/fonts/DMSans-400.ttf
```

Not used: **Arial Bold** (`/System/Library/Fonts/Supplemental/Arial Bold.ttf`) —
the v1 builder's only font and the thing Nate saw. Not used: **Inter** — it is the
ATX-Media-Mogul identity, a different system.

**Identity conflict, resolved.** KINETIC TYPE proposed Inter Bold / Cloud White /
Deep Space / Electric Orange. Rejected on three grounds: the existing twenty
DRAWDOWN cards already borrowed ATX-Proposal bronze, so shipping Mogul puts two
identities side by side; `~/.claude/hooks/design-system-guard.sh` enforces the
ATX-Proposal tokens on this tree; and the DM files are on disk and load by path
tonight. **v2 is ATX-Proposal: navy ground, bronze as a guest, DM Serif single
weight.**

| Role | Font | Size | Tracking | Case |
|---|---|---|---|---|
| End-card title | DM Serif Text 400 | 64 | 0 | Title |
| Headline 1-line | DM Serif Text 400 | 96 | 0 | UPPER |
| Headline 1-line long | DM Serif Text 400 | 88 | 0 | UPPER |
| Headline 2-line / stacked verbs | DM Serif Text 400 | 76 / 88 | 0 | UPPER |
| Date line | DM Sans 400 | 40 | 0 | Sentence |
| Eyebrow | DM Sans 700 | 30 | +0.20em | UPPER |
| Lockup | DM Sans 700 | 26 | +0.18em | UPPER |
| CTA | DM Sans 700 | 52 | +0.02em | **Sentence — verbatim, never up-cased** |

Tracking is not a Pillow feature: draw glyph-by-glyph advancing
`d.textlength(ch, font) + size * em`.

**Line length: hard cap 840 px measured.** The build **fails**, it does not
shrink to fit. Silent shrinking is how a type system rots.

**Colour tokens** (`~/ATX-Proposal-System/ATX-PROPOSAL-DESIGN-SYSTEM.css`):
navy `#1B2A4A` · cream `#FAF6F0` (all headline and date type) · bronze `#C4976E`
· black `#000000` (punctuation frames only).

**THE ONE EMPHASIS DEVICE: the 2 px bronze rule.** Band hairlines, the 120 px
tick above every lower-third, the 180 px rules on the end card. Bronze appears on
exactly four element types — rule, eyebrow, CTA-adjacent rule, band hairline —
which is the locked "bronze is a guest" rule. No boxes, no plates, no scrims
behind type, no coloured headline, no underline, no size jump for emphasis. If a
beat needs more emphasis than the rule gives it, the copy is wrong, not the design.

**Drop shadow** on type over picture only: 0/+3 px, `(0,0,0,153)`, `GaussianBlur(8)`.
None on the end card.

**Lockup is set as type, not a logo file** — no vector ATX mark exists on this
machine. If Nate produces one it drops into the x60/y156 slot with no other change.

---

## 6. Grade — one chain, every picture source

Applied to the **sharp band** after crop/scale and **before** compositing over
the blur ground, so type stays pure cream and no shot shifts against another.
All filters verified compiled into ffmpeg 8.1.1 this session.

```
format=gbrp,
curves=r='0/0.055 0.25/0.300 0.55/0.600 1/0.970':g='0/0.052 0.25/0.280 0.55/0.565 1/0.950':b='0/0.078 0.25/0.290 0.55/0.535 1/0.915',
selectivecolor=greens=0.00 0.16 0.14 0.10:cyans=0.06 0.02 -0.04 0.04:blues=0.04 0.02 -0.06 0.02,
eq=contrast=1.05:saturation=0.88:gamma=1.02:gamma_r=1.010:gamma_b=0.990,
colorbalance=rm=0.012:bm=-0.018:rh=0.040:gh=0.012:bh=-0.050,
unsharp=5:5:0.35:5:5:0.0,
vignette=angle=PI/6:x0=w/2:y0=h/2,
noise=alls=3:allf=t+u,
format=yuv420p
```

Intent: lift the blacks off zero and warm the highlights so it reads as film,
then push greens to olive so the hydrilla reads sick instead of pretty. Curves
set a 5.2–7.8 % black floor (blue highest, so shadows sit blue-grey not crushed)
and roll the top to 0.915–0.970 so nothing clips on an OLED. `selectivecolor`
greens take emerald weed to olive. `eq` drops saturation to 0.88 so the grade is
the only colour statement. `colorbalance` puts warmth exclusively in the
highlights. `unsharp` recovers the 1280→1080 downscale. Vignette + 3-point grain
is what stops it looking like a phone.

**Blur ground** (same frame, so consistency is structural):

```
[src]split[band][bg];
[bg]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,
    gblur=sigma=48,eq=brightness=-0.185:saturation=0.50:contrast=0.92,
    colorbalance=rs=-0.02:bs=0.05[ground];
[ground][graded_band]overlay=0:470[frame];
[frame]drawbox=x=0:y=470:w=1080:h=2:color=0xC4976E@0.85:t=fill,
       drawbox=x=0:y=1076:w=1080:h=2:color=0xC4976E@0.85:t=fill[out]
```

The ground converges on `#1B2A4A` from every source, which is what makes the end
card feel like the same object rather than a different document.

**End card:** no grade. Flat `#1B2A4A` plus the same `noise=alls=3` so it does
not band on a phone and matches the film's texture.
**Black punctuation frames:** not graded. True 0,0,0.

**No LUT, no Resolve.** `~/Poseidon/luts/` contains zero `.cube` files (its own
manifest confirms) and the two `power-grades/marine/*.drx` files document their
scripted path as unverified live. This chain renders tonight.

---

## 7. Motion

**Type — opacity only, forever.** Nothing slides, scales, tracks in, blurs in,
counts up or types on.

- In: 12 frames (0.400 s), cubic-out on alpha. Verb stack (shot 5): 8 frames.
- Out: 8 frames (0.267 s), linear, ending clear of the cut.
- Stagger within a lower-third: rule at f+0, eyebrow at f+6, headline at f+12.
  That 12-frame gap is the whole designed-not-templated feeling and it is free.
- Implementation: Pillow renders each **element** to its own transparent
  1080×1920 RGBA PNG; ffmpeg `overlay` +
  `format=rgba,fade=t=in:st=…:d=0.4:alpha=1,fade=t=out:st=…:d=0.267:alpha=1`.
  **No `drawtext` anywhere.**

**Shots — one move per beat, 2.5 % (3.0 % ceiling on the plates), alternating in/out
so consecutive shots never push the same direction.**

```
push in : zoompan=z='1.000+0.025*on/n':d=<frames>:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=1080x608:fps=30
push out: zoompan=z='1.025-0.025*on/n':...      (shot 3 uses 1.000+0.030*on/n)
```

**Anti-stepping:** render zoompan at 2× (`scale=2160:1216` first, `s=2160x1216`,
then `scale=1080:608:flags=lanczos`). zoompan quantises to integer source pixels;
at 1× a 2.5 % move over 200 frames visibly ratchets. This is the one thing in the
v1 builder worth keeping.

**Clips additionally:** `deshake=rx=32:ry=32:edge=mirror` → `setpts=1.6*PTS` →
`minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:vsbmc=1`.

**Never animated:** the lockup (once at f0–f12, then held 30 s), the bronze rules'
geometry, any type position, the band's position or size, the grade, and the end
card in its entirety. If a thing is moving in this film it is the water, the
aircraft, or a 2.5 % push.

---

## 8. Safe zones

Box: **x 60–900, y 140–1436** (TikTok-conservative; also clears Reels' bottom
484 px and the right-hand icon column). Picture bleeds full 1080×1920 — only
**text** is constrained. Max text width **840 px**, enforced as a build-time hard fail.

| Extreme | Element | Value | Wall | Margin |
|---|---|---|---|---|
| leftmost | every element | x = 60 | 60 | 0 (on the line, by design) |
| widest | `Text TRUXOR to 254-780-6971` @52 +0.02em | 809 px → right edge **869** | 900 | +31 |
| widest serif | `DRAWDOWN 2026` @96 | 770 px → right edge 830 | 900 | +70 |
| topmost text | end-card title ink | y = 493 | 140 | +353 |
| **lowest text** | shot 5 `COVER` ink bottom | **y = 1407** | 1436 | **+29** |

**Deepest text pixel anywhere in the film: y = 1407.** v1's box bottom sat at
y≈1710 — 274 px *inside* the reserved zone — because nothing checked.

**Runnable proof, not an assertion.** After rendering each element PNG, take
`Image.getbbox()` on the alpha channel and assert
`bbox[0] >= 60 and bbox[1] >= 140 and bbox[2] <= 900 and bbox[3] <= 1436`, plus
`bbox[2] - bbox[0] <= 840`. Raise `SAFE ZONE VIOLATION: <text> bbox=<box>` and
abort **before ffmpeg runs**. *(Alpha-bbox rather than `textbbox` is the graft
from KINETIC TYPE — it measures the pixels that actually ship, including the
shadow, which a metrics table misses.)* Element layers are static and the fade
scales alpha uniformly, so 20 layer checks cover all 900 frames.

---

## 9. Sound

Bed: `02_LakeComingDown_v1.mp3`, offset 0.0 s — the exact file and offset Nate
approved. Untouched musically. No VO, no SFX.

**No sonic logo.** `~/Poseidon/music/` holds a README and an empty `suno/`;
`atx-sonic-logo-3s.wav` and `atx-blitz-10s.wav` are named in the Mogul doctrine
and are not on disk. The tail is the bed's own final hit decaying under the CTA.
Real asset gap — commission it once, do not fake it here.

**Level map**
- 0.000–0.500 — `afade=t=in:d=0.5`. Cold open rises with the picture.
- 0.500–24.933 — **0 dB flat.** No ducking: there is no VO, so a duck would only
  announce itself. Legibility is optical (drop shadow + darkened ground).
- **25.400–30.000 — −2.0 dB**, ramped over 0.4 s. The card is quieter than the
  film. That is the whole premium tell: the last thing you hear is the room
  getting smaller behind the phone number. *(Judge 1's named steal.)*
- 28.500–30.000 — `afade=t=out:st=28.5:d=1.5`, so the 28.46 s hit lands at full
  weight **under** the CTA and decays to silence at 30.000.

**Where the hits land**
- 3.750 dissolve = the 3.2–3.8 s swell
- **10.800 hard cut = the Truxor plate.** v1 put that reveal on a −21.5 dBFS dip.
- 17.867 = the 17.28–17.60 cluster · 21.400 = onset 21.39
- 24.933 = onset 24.92; the card **arrives**, then gets hit at 25.37 and 25.80
- 26.691 downbeat (biggest onset cluster) lands on the fully-built card
- 28.46 final hit under the CTA at full opacity

**Loudness — two-pass `loudnorm`, exactly the pattern in
`/Users/austinlakescapes/drawdown-2026-campaign/06_Media_Build/build_leadin_vo.py`
lines 70–95.**

```python
def measure(chain):                       # pass 1
    p = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", BED, "-af",
         chain + ",loudnorm=I=-14:TP=-1.5:LRA=9:print_format=json",
         "-f", "null", "-"], capture_output=True, text=True)
    d = json.loads(re.search(r"\{[^{]*input_i.*?\}", p.stderr, re.S).group(0))
    return ("measured_I={input_i}:measured_TP={input_tp}:measured_LRA={input_lra}"
            ":measured_thresh={input_thresh}:offset={target_offset}").format(**d)

def mux():                                # pass 2
    pre = ("atrim=0:30,afade=t=in:d=0.5,"
           "volume='if(gte(t,25.4),0.794,1.0)':eval=frame,"
           "afade=t=out:st=28.5:d=1.5")
    af = ("[1:a]%s,loudnorm=I=-14:TP=-1.5:LRA=9:%s:linear=true[a]"
          % (pre, measure(pre)))
    subprocess.run([
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
        "-i", SILENT, "-i", BED, "-filter_complex", af,
        "-map", "0:v", "-map", "[a]", "-c:v", "copy",
        "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
        "-t", "30", "-movflags", "+faststart", DST], check=True)
```

`linear=true` is mandatory — a single static gain plus limiting rather than
re-compression, so the song's own dynamics (which are the edit's timing
reference) survive. The `volume`+`alimiter` tail from `build_leadin_vo.py` is
**not** carried over: that file needed it because 1.7 s of its 16 s is silence
dragging the integrated figure down. This bed is continuous music for 30 s. If
the measured integrated still lands more than 0.5 LU low, add
`volume=<delta>dB,alimiter=limit=0.891:level=disabled` after loudnorm — and
record it in PINS.md.

Target LRA is **9**, not 7. v1 shipped LRA 9.9 / TP −1.7; the defect that
actually bites on a phone is the true peak, and squashing to 7 shaves the
transients every cut above is timed to. Measure and record; never assume.

---

## 10. Cover frame

**t = 13.600 s (f408).** Inside shot 3, 2.8 s after the Truxor cut, with the full
lower-third settled: two amphibious machines, undercarriage visible, cream serif
`TWO AMPHIBIOUS / TRUXORS` over bronze rule, at rest. It is the C7 claim and the
brand in one still.

```bash
ffmpeg -y -ss 13.600 -i renders/LCD_v2/DRAWDOWN_LakeComingDown_916_v2.mp4 \
  -frames:v 1 -q:v 2 renders/LCD_v2/DRAWDOWN_LakeComingDown_916_v2_COVER.jpg
```

---

## 11. Build procedure

```bash
export V2=/Users/austinlakescapes/drawdown-2026-campaign/.claude/worktrees/platform-native-renders/06_Media_Build
mkdir -p "$V2/renders/LCD_v2"/{straps,seg,qc,logs}   # already created
```

1. **`$V2/build_lcd_v2.py` — reuse the v1 source mechanism, do not rewrite it.**

   ```python
   import sys
   sys.path.insert(0, "/Users/austinlakescapes/drawdown-2026-campaign/06_Media_Build")
   from build_timeline_cut import resolve, clip, BANNED, COUNT, C7_TWO_MACHINE
   ```

   `build_timeline_cut.py` guards its work behind `if __name__ == "__main__":`, so
   importing runs only the sqlite connect. `resolve(prefix)` gives the sha pin,
   the local-bytes check and the registry-beats-EXIF orientation guard for free.

2. **Guard the copy before anything renders.** Run `BANNED` over every string in
   the shot table; run this brief's extra terms too —
   `\$695|inspection|unofficial|credited|assessment|exploring|projected 10-12|extinct`
   — case-insensitive. Run `COUNT`: it may only hit on a beat whose source is in
   `C7_TWO_MACHINE`. Assert `Text TRUXOR to 254-780-6971` appears exactly once.
   Non-zero exit on any hit. **Nothing renders until this passes.**

3. **Strap PNGs (Pillow 10.4.0, installed).** One transparent 1080×1920 RGBA per
   *element* — not per beat — so each fades on its own stagger. Fonts by absolute
   path. Tracking drawn glyph-by-glyph. Drop shadow = same text at +0/+3 in
   `(0,0,0,153)` on its own layer, `GaussianBlur(8)`, composited under. Then the
   §8 alpha-bbox assertion on every layer. Write to `renders/LCD_v2/straps/`.

4. **Per-segment silent encodes → `renders/LCD_v2/seg/NN.mp4`.** Seven segments:
   `01` (clip 008, 120 f incl. handle), `02a` (clip 018 @8.0, 113 f),
   `BLACK` (7 f), `02b` (clip 018 @10.5, 99 f), `03` (plate C7, 212 f),
   `04` (clip 014 @60.0, 106 f), `05` (plate haul, 106 f), `06` (end card, 152 f).

   Clip segment (band at 2×, then down):
   ```
   -ss 100.0 -t 6.40 -i <clip 008>
   -filter_complex "[0:v]deshake=rx=32:ry=32:edge=mirror,setpts=1.6*PTS,
    minterpolate=fps=30:mi_mode=mci:mc_mode=aobmc:vsbmc=1,
    scale=2160:1216:flags=lanczos,
    zoompan=z='1.000+0.025*on/n':d=120:x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s=2160x1216:fps=30,
    scale=1080:608:flags=lanczos,<GRADE>[band]; …<BLUR GROUND>…"
   ```
   Clip in-duration = output_seconds × 1.6 (the 1/1.6 slow), plus 0.5 s pad.
   Plate segment: `-loop 1 -t <dur> -i <resolve path>` → `crop=1080:608:0:101`
   → `scale=2160:1216` → same zoompan → `scale=1080:608` → GRADE.
   End card: flat `#1B2A4A` 1080×1920 drawn in Pillow + `noise=alls=3`, then its
   element overlays.
   Black: `-f lavfi -i color=c=black:s=1080x1920:r=30 -t 0.2333`.

   **Encode every segment with byte-identical flags** —
   `-c:v libx264 -crf 16 -preset slow -pix_fmt yuv420p -r 30 -an`. The concat
   demuxer's `-c copy` fails on any parameter mismatch, and the lavfi black is
   the likely offender.

5. **The one dissolve.** Pre-render the `01`↔`02a` pair:
   ```
   ffmpeg -i seg/01.mp4 -i seg/02a.mp4 -filter_complex \
     "[0:v][1:v]xfade=transition=fade:duration=0.5:offset=3.5[v]" -map "[v]" … seg/01_02a.mp4
   ```
   `01` is 4.000 s, `02a` is 3.767 s → pair is exactly **7.267 s / 218 frames**,
   dissolve midpoint 3.750. `fade` is the only `xfade` mode used; fifty others
   exist and using a second one is how a spot starts looking like a template.

6. **Assemble.** `seg/list.txt` = `01_02a`, `BLACK`, `02b`, `03`, `04`, `05`, `06`.
   ```
   ffmpeg -f concat -safe 0 -i seg/list.txt -c copy -movflags +faststart \
     renders/LCD_v2/DRAWDOWN_LakeComingDown_916_v2_SILENT.mp4
   ```
   **Confirm `ffprobe` reports 900 frames / 30.000 s before going further.**

7. **Bed.** The two-pass `loudnorm` from §9 → `renders/LCD_v2/DRAWDOWN_LakeComingDown_916_v2.mp4`.

8. **Cover frame** per §10.

9. **Proof → `renders/LCD_v2/logs/` and `qc/`.** Nothing is claimed done without it.
   1. `ffprobe` duration == 30.000 ±0.033 and nb_frames == 900 → `probe.txt`
   2. `ffmpeg -i final -af ebur128=peak=true -f null -` → `loudness.txt`
   3. `ffmpeg -i final -vf "select='gt(scene,0.25)',showinfo" -f null -` →
      `scenes.txt`; assert boundaries within ±0.05 s of
      **7.267 · 7.500 · 10.800 · 17.867 · 21.400 · 24.933**
   4. Frame grabs at t = 0.20 · 1.50 · 3.75 · 7.35 · 9.00 · 11.60 · 13.60 ·
      19.00 · 22.20 · 26.50 · 29.00 → `qc/`
   5. `PINS.md` — full sha256 of both plates, the three aerial filenames with
      in-points, the bed filename + offset, the four font paths, the beat/frame
      table, both output md5s, the measured I/TP/LRA, and the per-element bbox
      table with headroom.
10. **Human gate.** Eye-pass the QC frames for (a) any text below y=1436, (b) the
    end-card CTA legible at phone size, (c) plate `c6b6853c038a` showing exactly
    two machines with amphibious undercarriage legible after the cold grade,
    (d) no recognisable lakefront residence in clip 018 @10.5 s — that in-point
    is 2.5 s past Victoria's vetted one and is the only unvetted frame in the
    film. **Nothing posts. Nate sees it first.**

Runtime: ~6–9 min. `minterpolate` on the three clip segments is the whole cost.

**HyperFrames is not used** — `npx` could not fetch or cache it offline.
**Resolve is not used** — no `.cube` files, unverified `.drx` path.

---

## 12. BEFORE / AFTER — six checkable statements, true of v2 and false of v1

| # | Statement | v2 check | v1 measured |
|---|---|---|---|
| 1 | **≥5 real scene changes**, each within ±0.05 s of a computed downbeat. | `select='gt(scene,0.25)',showinfo` → boundaries at 7.267 / 7.500 / 10.800 / 17.867 / 21.400 / 24.933 | **1** scene change in 30 s, at 24.43 s |
| 2 | **The locked CTA `Text TRUXOR to 254-780-6971` is on screen at full opacity for exactly 4.000 s** (f780–f899). | strap-table string assert + QC frame at t=29.00 | **absent entirely** — the end card shows only the bare number `254-780-6971` |
| 3 | **No rendered text pixel exists below y = 1436.** Deepest is y=1407. | alpha-bbox assertion on all 20 element layers, build aborts on violation | text box bottom ≈ **y1710**, 274 px inside the reserved 484 px caption/engagement strip |
| 4 | **The two-machine reveal lands on a measured onset, not a dip** — hard cut at f324 / 10.800 s, a computed downbeat and a top-ten onset. | `scenes.txt` boundary + `BEATGRID.md` downbeat list | machine reveal at ~13.1 s landed on a **−21.5 dBFS dip** in the mix |
| 5 | **One type system: every glyph comes from `~/ATX-Proposal-System/fonts/`** (DM Serif Text 400 + DM Sans 400/700). Zero glyphs from Arial Bold; no second face on the end card. | font paths in `PINS.md`; `grep -c "Arial" build_lcd_v2.py` == 0 | Arial Bold on all five title cards **plus a different bold sans on the end card** |
| 6 | **Delivered loudness is measured, not assumed: LRA ≤ 9.0 LU and I within −14.0 ±0.5 LUFS**, recorded in `logs/loudness.txt`. | two-pass `loudnorm=I=-14:TP=-1.5:LRA=9:linear=true`, then `ebur128=peak=true` | **LRA 9.9 LU**, TP −1.7 dBTP, from an ad-hoc `afade`-only mux with **no loudnorm pass at all** |

---

## 13. Least confident decisions

1. **Moving the Truxor cut from 9.900 to 10.800.** Two measurements of one swell
   disagree; I took the beat grid over the 0.32 s RMS sample. If it feels late on
   a phone, the fallback is f318 (10.600) — but do not re-derive the whole timeline.
2. **Stacking `SCRAPE / HAUL / COVER`.** Same words, same order; the `·`
   separators and line breaks change. I read that as layout. If Nate reads it as
   copy, revert to one line at DM Serif 68 (measured 722 px, fits).
3. **Clip 018 @ 10.5 s is the film's only unvetted in-point.** Blocking eye-pass
   item, step 9(d). If it carries a residence, shorten shot 2b instead of
   reaching into the unvetted clip pool.
4. **The 7-frame hard black.** Platform re-encoding can smear it, and some
   autoplay feeds read it as a stutter. 7 f is the floor — check it survives a
   round trip before this pattern is reused across the campaign.
5. **LRA 9 rather than 7.** Judges 1 and 2 both liked 7. I kept the transients.
6. **The end card is 5.07 s of static navy — 17 % of the spot.** Deliberate; the
   CTA holds four full seconds. If retention data later says viewers drop at
   25 s, the fix is the last aerial at 15 % opacity behind the navy, never a
   shorter CTA.
7. **Nothing here has rendered yet.** Every width above is a real Pillow
   measurement taken this session, but every *timing* is a prediction against the
   measured bed. Step 9 exists because of that.
