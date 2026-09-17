# LCD v2 — BUILD NOTES (round 4)

`renders/LCD_v2/LCD_v2_916.mp4` · 1080×1920 · 30 fps · **900 frames / 30.000 s** ·
h264 yuv420p · faststart · the Suno bed from the master at offset 0.0 s.
md5 `15da99ea60788db462a0c100d486fb8a`.

Builder: `06_Media_Build/build_lcd_v2.py` **in the worktree**. Nothing under
`/Users/austinlakescapes/drawdown-2026-campaign/06_Media_Build` was written, moved or
renamed — it is imported (`resolve`, `BANNED`, `COUNT`, `C7_TWO_MACHINE` from
`build_timeline_cut.py`) and read as bytes (the bed, and the v1 master for the
comparison sheet). Every output is under `renders/LCD_v2/`. Round 3's outputs are kept
in `renders/LCD_v2/_r3/`. Nothing posted. No logins. Offline.

---

## DIRECTIVE F — a hierarchy decision for Nate, stated up front

**Card 1 is `DRAWDOWN 2026` as the headline (DM Serif Text, 86 px) over
`LAKE AUSTIN` as the eyebrow (DM Sans 700, 28 px, bronze).** v1 had it the other way
round: `LAKE AUSTIN` was the larger line and `DRAWDOWN 2026` sat under it in copper at
roughly two-thirds the size.

Both words are approved and neither is changed. What changed is which one the first
three seconds are *about*. The piece is a drawdown announcement — the event is the
news, the lake is the place — and the eyebrow is the right slot for a place. Every
other card in the film uses the same shape (place/qualifier small and bronze, claim
large and cream), so v1's inversion also made card 1 the only card that read
differently from the other three.

**This is a deliberate change, not a silent one. If Nate wants the v1 order back it is
a two-line swap in `CARDS["s1"]` and nothing else in the build moves.**

---

## The round-4 directives, each measured

| # | Directive | Delivered | Result |
|---|---|---|---|
| **A** | End card = navy `#1B2A4A` with the approved wide Lake Austin aerial `8c7fd940fc1f` under it at ≤ 15 %, gblur ≥ 40. Phone number ≥ 7:1. | Aerial at **15 %**, gaussian **sigma 120 in 2× space = 60 px at 1×**, darkened 0.55 / desaturated 0.40 before the blend. `cta_number` measures **12.33:1 mean · 12.03:1 worst-local 16×16 tile** against the ground rows behind its own ink. | **PASS** (floor 7.0) |
| **B** | Every type element ≥ 4.5:1 at its hold frame, per card, printed. Lower-third device is a bottom gradient on the picture — no box, no slab. | 18 text elements × 21 sampled frames, each measured at **its own ink box** with the type's alpha used as a hole-punch so cream glyphs cannot inflate the "ground". Worst in the film is `s3_eyebrow` at **4.76:1**. Table below and in `logs/contrast_table.md`. | **PASS**, zero failures |
| **C** | f0 is the thumbnail: wordmark + its rule fully on at f0, no ramp. Whole-frame YAVG f0–f10 flat within ±2. | `lockup` and `lockup_tick` are `hard=True` — **alpha 1.0 on f0**, no entrance. Both scrims are at full value on f0. YAVG **f0 82.16 · f5 82.51 · f10 82.53**, spread **+0.42**. | **PASS** (floor ±2.0) |
| **D** | Align by ink not alpha bbox; first letter's stem at x=84 ±2; rules start at 84 exactly; ONE bronze rule length (176 px); ONE eyebrow spec; end card ≤ two families. | Every element placed by `place_x()` = **measured rendered ink x0**, then a glyph-class trim **capped at 2 px** (was −6/−3). Delivered margin ink x0 ∈ **{82, 83, 84}**. All **seven** rules are **176 × 3 px** including the lockup's. End card: **DM Serif Text 400 + DM Sans 400/700** — two families, two sans weights. | **PASS** |
| **E** | The payoff beat moves: band \|dframe\| ≥ 1.0 on every 1 s window; the 12.900 re-frame is a real hard cut or a ≥ 2 %/s push. | **f387 = 12.900 s is a real hard cut** to a second framing on a second plate. Payoff = 03a (12.900–16.567) + 03b (16.567–20.233), pushing **3.82 %/s** and **4.09 %/s** with a lateral creep on top. Delivered per-second **[5.17, 1.94, 1.73, 1.78, 2.72, 1.48, 1.54, 1.41, 2.50]**, min **1.41**. | **PASS** (floor 1.0) |
| **F** | Hierarchy disclosure. | Stated above, first thing in this file. | done |
| **G** | Keep the Suno bed at 0.0, the five approved plates in the master's order, verbatim words, cuts on the measured grid, deepest ink clear of y1436, CTA at full opacity 4.000 s. | Bed `02_LakeComingDown_v2.mp3` offset 0.0 s, untouched musically. Master order and the master's own card-to-plate pairing **restored**. Copy guard passes on 19 strings. All seven cuts are computed downbeats of the 130.85 BPM grid. Deepest ink **y = 1362** (74 px clear). CTA at full opacity **f780–f899 = 120 frames = 4.000 s**, asserted by the build. | **PASS** |

---

## DIRECTIVE B — the contrast table

Ground is measured **through the type's own alpha** (glyph pixels punched out), at each
element's own ink box, on the delivered JPEG frames. "Worst-local" is the brightest
16×16 ground tile under that element — the number that actually decides legibility.

| card | element | ratio (mean ground) | ratio (worst-local 16×16) | floor | pass |
|---|---|---|---|---|---|
| all cards (f0–f899) | `lockup` | 8.54:1 | **7.09:1** | 6.0 | PASS |
| card 1 DRAWDOWN 2026 | `s1_eyebrow` | 5.62:1 | **5.39:1** | 4.5 | PASS |
| card 1 DRAWDOWN 2026 | `s1_head` | 14.50:1 | **13.30:1** | 4.5 | PASS |
| card 2 ABOUT 10 FEET | `s2_eyebrow` | 5.99:1 | **5.40:1** | 4.5 | PASS |
| card 2 ABOUT 10 FEET | `s2_head` | 15.25:1 | **13.14:1** | 4.5 | PASS |
| card 3 TWO AMPHIBIOUS TRUXORS | `s3_eyebrow` | 5.64:1 | **4.76:1** | 4.5 | PASS |
| card 3 TWO AMPHIBIOUS TRUXORS | `s3_head` | 15.23:1 | **11.76:1** | 4.5 | PASS |
| card 4 WE WORK THE BED | `s4_eyebrow` | 6.18:1 | **5.14:1** | 4.5 | PASS |
| card 4 WE WORK THE BED | `s4_head` | 14.84:1 | **13.00:1** | 4.5 | PASS |
| card 5 END CARD | `end_title` | 13.28:1 | **13.00:1** | 4.5 | PASS |
| card 5 END CARD | `end_date0` | 13.16:1 | **12.95:1** | 4.5 | PASS |
| card 5 END CARD | `end_date1` (the note) | 13.02:1 | **12.89:1** | 4.5 | PASS |
| card 5 END CARD | `end_date2` | 12.68:1 | **12.38:1** | 4.5 | PASS |
| card 5 END CARD | `end_date3` | 12.33:1 | **12.08:1** | 4.5 | PASS |
| card 5 END CARD | `end_date4` | 12.16:1 | **12.03:1** | 4.5 | PASS |
| card 5 END CARD | `end_tag` (bronze) | 5.02:1 | **4.91:1** | 4.5 | PASS |
| card 5 END CARD | `cta_lead` | 12.47:1 | **12.30:1** | 4.5 | PASS |
| card 5 END CARD | **`cta_number`** | **12.33:1** | **12.03:1** | **7.0** | **PASS** |

The exact per-frame log is `logs/contrast.txt`; the table alone is
`logs/contrast_table.md`. The bronze rules are **not** in the table: they are ornament,
not text, and they are excluded by name in `proof()` rather than quietly averaged in.

**`end_tag` is measured as bronze**, because it *is* bronze now. Round 3 restored the
master's copper tag but kept measuring it against cream's luminance — a pass it did not
have. At `#C4976E` on this ground it is 4.91:1, which is a real pass with 0.4 to spare.

---

## The lower-third device (directive B), and what it cost

A bottom gradient on the picture — black `rgb(8,14,24)`, alpha 0 at y720 rising to full
by y1070, held to y1420, tail 0.16 — **no box, no slab, no plate behind any glyph.**

Peak alpha is **0.84**, solved from the worst ground that ever sits under a bronze
eyebrow (169.8 on the Truxor plate) and then *verified on the delivered file* rather
than assumed. Directive B's 0.55 was tried and measures **3.4:1** on that beat, so it
would have shipped a failing card. 0.84 is the number the measurement produced.

It is one constant, held across the **entire picture section** — 0.58 top, 0.84 lower,
**exactly one transition in the whole film**, at f772, and that transition rides the
6-frame dissolve into the end card. Round 3 switched it per card-carrying shot, which is
what produced the pumps at f277/f332/f662.

**Cost, stated plainly:** the gradient darkens rows 1070–1420 on beats that carry no
eyebrow too, and it halves any motion measurement taken through it — which is why
directive E is reported twice below.

---

## DIRECTIVE E — the payoff beat, and the two numbers

Measured on the **picture band** (crop 1080×972 at y480), quarter-scaled to 270×243
gray, mean absolute inter-frame difference, one value per 1 s window. The scale is
declared because the number is resolution-dependent: at native resolution `noise=alls=3`
grain alone puts a floor under it and the metric stops measuring the camera.

| 1 s window | 12–13 | 13–14 | 14–15 | 15–16 | 16–17 | 17–18 | 18–19 | 19–20 | 20–21 |
|---|---|---|---|---|---|---|---|---|---|
| **delivered** | 5.17 | 1.94 | 1.73 | 1.78 | 2.72 | 1.48 | 1.54 | 1.41 | 2.50 |
| picture only | 10.84 | 3.24 | 3.21 | 3.32 | 5.00 | 2.66 | 2.75 | 2.47 | 4.30 |

Floor is held on the **delivered** file: min **1.41**. The picture-only row is printed
so the gradient's cost is visible rather than hidden — it is the same band with no
chrome over it.

Full 30-window list for both is `logs/motion.txt`.

**How the beat was made to move, without breaking C7.** Round 3 refuted this directive
and the refutation was half right: at scale 1.62 the yard plate's two machines span
enough of the window that a 14 % push is the ceiling, and 14 % over one 5.5 s beat is
2.55 %/s — legal, but it measured 1.03 through the gradient because *a pure zoom has
zero displacement at frame centre*. Three changes fixed it and none of them touched C7:

1. **Two beats, not one.** A real hard cut at **f387 = 12.900 s**, the exact frame the
   directive names, onto a second plate. Each beat is 3.667 s, so the same push budget
   buys 3.82 %/s and 4.09 %/s instead of 2.55 %/s.
2. **A lateral creep** on top of the push — 110 px (03a) and 150 px (03b) in 2× space
   across the beat. A creep moves every pixel including the ones at the centre.
3. **Scale 1.62 → 1.45 on the yard plate**, which *widens* the window from 667 to 745
   source px and buys the creep its headroom. Both Truxors stay whole for the entire
   beat — verified on the delivered first, middle and last frames.

---

## The Truxor beat — C7 kept, and Lake Austin put back under it

Round 3's critic was right that `fd49bf6ffe3e` is a yard plate with no water in it, and
right that swapping to it was the only way to satisfy C7. The fix here is the one the
critic specified: **split the beat.**

- **03a · f387–496 · 12.900–16.567 s · `fd49bf6ffe3e`** — carries the count card
  `COMMITTED IN JULY / TWO AMPHIBIOUS TRUXORS`. Exactly two Truxors, both whole, both
  branded, rubber tracks fully exposed, **no third hull of any kind**. In
  `C7_TWO_MACHINE`, so the imported `COUNT` guard passes it and **fails the build the
  moment anyone moves the count word off it**.
- **03b · f497–606 · 16.567–20.233 s · `c6b6853c038a`** — the master's own b3: two
  machines working the bed, spray, water, shoreline, Lake Austin. **No type at all.**
  No strap means no count claim, so the pontoon float behind the machines is never
  presented as anything, and C7 never applies to the plate.

That is 3.667 s of yard (the iron, the claim) and 3.667 s of lake (the work, the place),
and the second one is the silence beat the cut was missing.

---

## Every critic finding from the last round

| Finding | What was done |
|---|---|
| **End-card dashes render at cap height and read as macrons.** | The pinned dash rectangles are **deleted entirely**. `split_date()` already treats `" — "` as a delimiter, and a round-trip assert in `guard()` proves no approved glyph changed. |
| **The ragged gutter was relocated, not fixed** (83 px → 10 px swing). | The date column is **right-aligned**, so all four gutters are **identically 48 px**. Its right edge is solved so the *longest* cell (`Nov 2–24`) starts exactly on the film's margin, x = 84 — the block still anchors at the margin and only the three shorter dates rag, which is how a schedule is set. |
| **Two dashes 10 px apart on the `Nov 2–24` row.** | Gone with the dash. |
| **Drop shadow on a flat self-authored ground.** | Shadow alpha **0 on every end-card element**. It stays on the photo straps, where it earns its keep. This also means the advertised ratios are now measured against the real local ground, not a halo the build put there itself. |
| **`~3 weeks to target` claims equal status with the dated facts.** | **32 px at 70 % cream**, in the event column with an empty date cell. Two subordinating signals, not one, and no copy touched. |
| **Lockup is outside its own system, twice** (+0.18em vs +0.20em; cream-43 % tick vs bronze rules). | Tracking **+0.20em**, matching every other 28 px caps eyebrow. The tick is now **the 176 px bronze rule module** — and it moved **above** the wordmark, because 176 px under a 315 px wordmark is a truncated underline stopping mid-word, while the same module above it is an accent rule. |
| **303 px void between lockup and end-card title.** | The end-card group is **solved and optically centred**: laid out from its own ink on one 48/72/96 scale, then placed so the void above equals the void below. Delivered **163 px above, 164 px below** inside the safe box. |
| **Event column is x0 = 336 on three rows and 335 on `Nov 2–24`.** | The column is **pinned** — `place_x(..., opt=False)` — so the glyph-class trim cannot fire inside a column. All four event cells and the note row land on **x0 = 310** exactly. |
| **Scrim ramp is a visible pump at the money shot** (43.6 levels over 133 ms after the cut). | `SNAP_F = 0`. Scrims are piecewise constant and there is **exactly one transition in the film**, at f772, riding the dissolve. The 4-frame ramp does not exist any more. |
| **Hook opens on the darkest, least legible frame.** | Option (a), the critic's own: **the film opens on the aerial**, f0–166. The hydrilla moves to f167–386 where it owns 7.33 s across two framings and still carries `ABOUT 10 FEET` — the master's own pairing, also restored. f0 YAVG is **82.2** against v1's 58.1. |
| **The hook copy owns only 1.13 s of its own picture.** | Card 1 lands on **f0**: rule f0, eyebrow f6, headline f12, full by **f17 (0.567 s)**, held to f156. **4.6 s** of hold, up from 1.13 s. The ease is untouched. |
| **Eyebrow ease runs long against the stated bar.** | All entrances are one constant, `IN_F = 5` frames, smoothstep. The stagger is a start-time offset only. |
| **End card is 7.90 s of zero picture events; the CTA needs 2.5 s and holds 7.97 s.** | The card is now **f772–899 = 4.267 s**, and the CTA holds **exactly 4.000 s** at full opacity. **110 frames went back to the picture** — they bought the second Truxor beat. |
| **End card, bottom void.** | See known gaps below — this is the one finding that is answered but not eliminated. |
| **C7 beat is the authenticity regression.** | Split, as above. Yard plate carries the count; the master's water plate returns for 3.667 s underneath no type at all. |
| **End card, bronze has left.** | `scrape · haul · cover` is **`#C4976E`** again, verbatim from the master's `TIMELINE_CARD`, and it is now measured as bronze (4.91:1). |
| **Picture ground, mixed grammar** (two beats full-bleed, two in a fit band). | **Not fixed. Refuted with a measurement — see below.** |
| **Loop seam still steps 13.2 luma levels.** | **Not fixed, and not claimed.** It is now +24.1. See known gaps. |

### Refuted, with the measurement

**"Pick one: bleed all four, or band all four."** The four plates are not one kind of
asset. `8c7fd940fc1f` is **1080 × 607** and `5a4942b7731d` is 1080 × 810; covering them
to 1080 × 1920 is a 3.16× and 2.37× resample. The two sharp 1080 × 810 machine plates
are 2.37× as well *if bled*, but only 1.20–1.46× into the fit band — and those are the two
beats where the subject is a machine with legible branding and an undercarriage the C7
claim depends on. Bleeding them costs that legibility to buy consistency; banding the
two soft wide plates costs nothing visible because there is no detail to preserve, but
it puts a 452 px window of mush in the middle of a navy field, which is the poster Nate
already rejected. The alternation is a real decision about two real asset classes, and
the boundary lands on f387 — the money cut — where an audience reads a change of
grammar as the point of the cut, not as a template tell.

---

## What changed vs v1

- **Structure.** v1: **one** scene change in 30 s, at 24.43 s. v2: picture events at
  **5.567 · 9.233 · 12.900 · 16.567 · 20.233 · 23.900** plus the 6-frame dissolve at
  25.733 — **seven**, every one a computed downbeat of the measured 130.85 BPM grid
  (`logs/scenes_full_010.txt`).
- **The locked CTA exists.** `Text TRUXOR to 254-780-6971`, verbatim, asserted once by
  the copy guard, at **full opacity f780–f899 = exactly 4.000 s**. v1 shows a bare
  number and no call to action at all.
- **Nothing below y1436.** Deepest ink **y = 1362**, 74 px of clearance. v1's text box
  bottom sits at ≈ y1710 — 274 px inside the reserved caption/engagement strip.
  `tiktok_proof.png` re-checked on the delivered t = 28 frame: **no text pixel in red**.
- **One type system, by absolute path.** DM Serif Text 400 + DM Sans 700 + DM Sans 400.
  `grep -c Arial build_lcd_v2.py` == **0**. v1: Arial Bold on all five title cards plus
  a second bold sans on the end card.
- **One left edge.** Every element positioned by measured rendered ink; delivered margin
  x0 ∈ {82, 83, 84}. v1 centred its end card and boxed its captions.
- **One emphasis device.** The 176 × 3 px bronze rule, seven times. No slabs, no scrims
  behind glyphs, no coloured headline, no underline. v1 boxed every caption in a dark
  rounded slab.
- **Loudness measured, not assumed.** Two-pass `loudnorm` → delivered **I −14.0 LUFS ·
  LRA 7.6 LU · TP −2.0 dBTP** (`logs/loudness.txt`). v1: I −14.5 · LRA 9.9 · TP −1.7,
  from an `afade`-only mux with no `loudnorm` pass at all.
- **C7 is provable.** The count word rides `fd49bf6ffe3e`; the imported `COUNT` guard
  fails the build if it ever rides a plate outside `C7_TWO_MACHINE`.

---

## Fonts (absolute paths)

```
/Users/austinlakescapes/ATX-Proposal-System/fonts/DMSerifText-400.ttf
/Users/austinlakescapes/ATX-Proposal-System/fonts/DMSans-700.ttf
/Users/austinlakescapes/ATX-Proposal-System/fonts/DMSans-400.ttf
```

Loaded by `ImageFont.truetype()` on an absolute path. All type is Pillow-rendered — no
`drawtext` anywhere, so nothing can silently substitute a face. Arial is not used.

| Role | Font | Size | Tracking | Colour |
|---|---|---|---|---|
| Headline, one line | DM Serif Text 400 | 86 | 0 | cream `#FAF6F0` |
| Headline, two line | DM Serif Text 400 | 69 (72 lead) | 0 | cream |
| End-card title | DM Serif Text 400 | 55 | 0 | cream |
| Phone number | DM Sans 700 | 86 | +0.02em | cream |
| CTA lead-in | DM Sans 700 | 35 | +0.01em | cream |
| Eyebrow | DM Sans 700 | 28 | +0.20em caps | bronze `#C4976E` |
| Lockup | DM Sans 700 | 28 | +0.20em | cream |
| End-card tag | DM Sans 700 | 30 | +0.01em | bronze |
| Date row | DM Sans 400 | 40 | 0 | cream |
| Note row | DM Sans 400 | 32 | 0 | cream @ 70 % |

**One eyebrow spec, one rule.** `track_em()` gives the +0.20em caps value to an all-caps
string and +0.01em to a mixed-case one — `LCRA: Oct 12 – Nov 24` is the only mixed-case
eyebrow in the film, and wide tracking on lowercase opens the counters until the word
falls apart at 28 px. That is one rule with a defined branch, not two specs.

**Colour tokens** are the ATX Proposal system: navy `#1B2A4A` · cream `#FAF6F0` ·
bronze `#C4976E`. Nothing else is defined anywhere in the build.

---

## The grade

One chain, every picture source, applied after the crop/scale and before the composite:

```
format=gbrp,
curves=r='0/0.055 0.25/0.300 0.55/0.600 1/0.970'
      :g='0/0.052 0.25/0.280 0.55/0.565 1/0.950'
      :b='0/0.078 0.25/0.290 0.55/0.535 1/0.915',
selectivecolor=greens=0.00 0.16 0.14 0.10:cyans=0.06 0.02 -0.04 0.04
              :blues=0.04 0.02 -0.06 0.02,
eq=contrast=1.05:saturation=0.88:gamma=1.02:gamma_r=1.010:gamma_b=0.990,
colorbalance=rm=0.012:bm=-0.018:rh=0.040:gh=0.012:bh=-0.050,
eq=brightness=0.035,
unsharp=5:5:0.35:5:5:0.0,
vignette=angle=PI/9:x0=w/2:y0=h/2,
noise=alls=3:allf=t+u
```

Then, per shot: an extra `unsharp` on the two soft wide plates only; a `colorbalance`
warm/cool trim; a solved `eq=saturation` that lands each beat on its pole value; and a
`eq=brightness` trim **chained** so no cut steps more than 6 YAVG on the graded still.
The pole is **ENEMY** and the grade travels inside it — the hydrilla runs cool and
desaturated (S 40), the Truxor beats warm and up (S 54–56), the haul warmest (S 62).
Per-shot values are the picture table in `PINS.md`.

The end-card ground gets **no grade at all** — only `noise=alls=3:allf=t+u` — because it
is composited in Pillow at exact values, so what `proof()` measures is what the encoder
received.

---

## The audio chain

Bed: `audio/suno/02_LakeComingDown_v2.mp3`, **offset 0.0 s**, untouched musically. No
VO, no SFX, no sonic logo (there is no such asset on this machine — a real gap, not a
thing to fake).

```
atrim=0:30,
afade=t=in:d=0.5,
volume='if(gte(t,26.0),0.794,1.0)':eval=frame,      # −2 dB once the card lands
afade=t=out:st=28.5:d=1.5,
loudnorm=I=-14:TP=-1.5:LRA=9:<measured pass-1 values>:linear=true,
volume=-0.6dB,
alimiter=limit=0.841:level=disabled
```

Two-pass: pass 1 measures with `print_format=json` (kept at
`logs/loudnorm_pass1.json`), pass 2 applies the measured values with `linear=true`, so
it is a static gain plus limiting rather than re-compression and the song's own dynamics
— the edit's timing reference — survive.

**Delivered: I −14.0 LUFS · LRA 7.6 LU · TP −2.0 dBTP** (`logs/loudness.txt`).

The card is quieter than the film by 2 dB, so the last thing the viewer hears is the
room getting smaller behind the phone number, and the tail decays to silence at 30.000.

---

## How to run

```bash
cd /Users/austinlakescapes/drawdown-2026-campaign/.claude/worktrees/platform-native-renders/06_Media_Build
python3 build_lcd_v2.py
```

~2.5 min on this machine. It is idempotent and writes only under `renders/LCD_v2/`.
The build **aborts before ffmpeg ever runs** on: a banned or brief-banned term in any
on-screen string; a count word over a plate outside `C7_TWO_MACHINE`; a CTA that is not
the locked string verbatim, or that appears more than once; a lossy date split; an
unpinned or byte-missing plate; any layer whose alpha bbox leaves the safe box
`(60, 140, 900, 1436)` or exceeds the 840 px line cap; any margin element whose ink x0
is outside 84 ± 2; and a CTA hold that is not exactly 120 frames.

Outputs: `LCD_v2_916.mp4`, `LCD_v2_916_SILENT.mp4`, `LCD_v2_916_COVER.jpg`,
`BEFORE_AFTER.png`, `tiktok_proof.png`, `PINS.md`, `qc/` (21 frames), `logs/`
(probe, loudness, loudnorm pass 1, three scene-change passes, contrast per frame,
contrast table, YAVG full + head, motion).

---

## Known gaps

1. **The loop seam is not closed, and this build does not claim it is.** f0 YAVG **82.2**
   (aerial) against f899 **58.0** (end card) — a **+24.1** step on a platform that
   auto-loops. v1's own seam on the same measure was **−93.2** (measured in round 3) and round 3's was +11.7, so
   this is far better than the master and **worse than round 3** — the cost of opening on
   the legible frame instead of the dark one, which directive C and the hook finding both
   required. Closing it needs either an opening plate that sits near 45 YAVG (there isn't
   one in the approved five) or a darker end card (which would trade against directive A's
   7:1). Left open deliberately.
2. **The end card's bottom void is answered against the safe box, not against the frame.**
   The group is centred with 163/164 px of void inside `140–1436`, but the phone number's
   ink bottom is y1272 and the frame is 1920 tall, so **648 rows of navy sit under it** —
   484 of which are TikTok's reserved strip and 164 of which are the balanced void. On
   TikTok this is correct. **Shipped byte-identical as the GBP listing video, where there
   is no platform chrome, it will read bottom-heavy.** The fix is a GBP variant that
   re-centres the same group in the full 1920 — one constant, `BOX[3]`, and a re-run.
3. **`s3_eyebrow` at 4.76:1 is the film's thinnest margin.** It clears the 4.5 floor by
   0.26, and it is bronze on the brightest ground in the cut. If the Truxor plate is ever
   re-graded brighter, that is the element that fails first.
4. **The 0.84 lower gradient is heavy**, and it is the reason the delivered motion numbers
   are roughly half the picture-only numbers. It is what the measurement demanded, but a
   plate-side fix — grading the eyebrow region of the Truxor plate down instead of
   scrimming the whole film — would buy back both the darkness and the motion. Not
   attempted this round.
5. **The `-9.8` YAVG step at f607** (03b → 04a) is the one cut outside ±8. It is a real
   exposure change between two different plates and the brightness chain is already at its
   ±0.14 clamp on that pair.
6. **The hydrilla beats read cool and steel-blue**, because the plate is a reflected sky on
   still water. Saturation was pulled to 40 and the cool trim to −0.008 this round, which
   removed the violet cast round 3 had; it is now blue-grey rather than lilac. If Nate
   wants it olive-green it needs a channel-mixer step, not a saturation number.
7. **`scene changes (full)` at threshold 0.25 reports nothing.** Every boundary is found at
   0.10, and two are found at 0.25 on the band alone. The full-frame score never crosses
   0.25 because the graded, gradient-covered frames are more similar to each other than the
   raw plates are. The 0.10 list is the honest one and it is the one quoted above.
8. **The first 12.9 s are the softest frames in the film, and no grade fixes that.**
   `8c7fd940fc1f` is **1080 × 607** and `5a4942b7731d` is 1080 × 810; covering either to
   1080 × 1920 is a 3.16× / 2.37× resample. An extra `unsharp=7:7:1.05` (aerial) and
   `7:7:0.60` (hydrilla) runs on those beats only, so they are not the mushiest thing in
   the cut, but on `BEFORE_AFTER.png` the v2 hook still reads softer than its type does.
   The only real fix is a higher-resolution aerial. Both plates are approved and neither
   was re-cropped tighter than the source allows — **no upscaling beyond the fit-band
   minimum anywhere in the build.**
9. **Nothing has been through a platform round trip.** Every number here is measured on the
   local file. Re-encoding by TikTok/Instagram/GBP will move the true peak and can smear a
   6-frame dissolve. **Nothing posts. Nate sees it first.**
