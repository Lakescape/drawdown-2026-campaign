# LCD v2 — ROUND 5 (mechanical)

`renders/LCD_v2/_r5/LCD_v2_916.mp4` · 1080×1920 · 30 fps · **900 frames / 30.000 s** ·
h264 yuv420p · faststart · md5 `f23ec45dffcac653b2289242d1450708`.

Three named defects, nothing else. No redesign, no new taste calls. Every on-screen word
is byte-identical to round 4 (the copy guard passes on the same 19 strings, CTA verbatim
and once). No plate changed. The Suno bed is `02_LakeComingDown_v2.mp3` at offset 0.0 s,
untouched. Round 4's deliverables under `renders/LCD_v2/` were not written to — every
output of this run is under `_r5/`. Nothing posted. Offline.

**Loudness, two-pass `loudnorm` preserved.** Pass 1 measured
`I −14.99 · TP −1.47 · LRA 8.20 · offset −0.06` (`_r5/logs/loudnorm_pass1.json`); pass 2
applied those with `linear=true`. **Delivered: I −14.1 LUFS · LRA 7.6 LU · TP −2.0 dBTP**
(`_r5/logs/loudness.txt`). Identical to round 4 — the audio chain was not touched.

**TikTok dead-zone proof** — `_r5/tiktok_proof.png`, taken on the delivered t = 28.0 s
frame, top 140 / bottom 484 / left 60 / right 180 in red. **No text pixel is inside red.**
The build's own bbox check on all 25 layers prints `CLEAR`; deepest ink is y = 1362,
74 px clear of the y1436 floor.

---

## 1 · HYDRILLA SHIMMER — fixed

**Cause was not motion interpolation.** There is no `minterpolate` / `mci` anywhere in
this build and there never was. The plate `5a4942b7731d` (beats 02a/02b) was the only
material in the film carrying `jit = 0.55` — the two-frequency handheld shake, ~3.5 px
peak per frame in 2× space — and a handheld shake over a still-water specular reflection
does not read as a camera, it reads as the water flickering. That is the whole defect.

**Fix:** `jit → 0.00` on both beats, and the beat is now driven by the same continuous
`zoompan` push every other plate uses — `(1.000 → 1.100)` over 110 f = 3.667 s =
**2.73 %/s**, monotone, inside the 2–4 %/s band, restarting on the f277 framing change
exactly as 03a/03b restart on theirs.

Measured on the round-4 file and the round-5 file with one script, `_r5/measure_r5.py`
(full output `_r5/R5_MEASURE.txt`).

### Delivered band metric — the metric on which "every other beat is 1.6–2.5" is true

crop 1080×972 @ y480 → 270×243 gray, mean absolute inter-frame difference.

| beat | | round 4 | round 5 | target |
|---|---|---|---|---|
| **02a** f167–276 | 1 s windows | 5.77 · 3.39 · 4.64 | **2.33 · 1.63 · 1.70** | each in 1.0–3.5 ✔ |
| | beat mean | 4.48 | **1.71** | |
| | worst single frame | 9.10 | **2.77** | |
| | peak / mean | **2.03× — SPIKE** | **1.62×** | ≤ 2.0× ✔ |
| **02b** f277–386 | 1 s windows | 4.88 · 2.99 · 4.31 | **2.08 · 1.50 · 1.55** | each in 1.0–3.5 ✔ |
| | beat mean | 3.99 | **1.56** | |
| | worst single frame | 7.68 | **2.58** | |
| | peak / mean | 1.93× | **1.65×** | ≤ 2.0× ✔ |

Rest of the film on the same metric, unchanged: 1.41 – 2.72. **The hydrilla beats are no
longer distinguishable from any other beat**, which was the point — round 4 ran 2–3× hot.

### Picture-only band metric — the metric that produced the 8.48 / 7.96 reading

Same crop, measured on `seg/picture.mp4` before the lower scrim. This is where the
critic's numbers come from, exactly: round 4 reads **8.48** (02a) and **7.96** (02b) in
`renders/LCD_v2/logs/motion.txt`.

| beat | round 4 | round 5 | film range, round 5 |
|---|---|---|---|
| 02a | 8.48 | **3.63** (windows 3.53 · 3.63 · 3.72) | 2.47 – 5.18 |
| 02b | 7.96 | **3.16** (windows 3.14 · 3.18) | 2.47 – 5.18 |

**Disclosed:** on this second metric one of 02a's three windows reads **3.72**, i.e. 0.22
over a 3.5 ceiling. Two things about that number. It is now *below the film's median* on
its own metric (03a reads 4.72, the haul beat 5.18), so the beat is no longer an outlier
in either direction. And it is **not the push**: dropping the push from 12 % to 10 % moved
it 3.74 → 3.72. The residual is `noise=alls=3:allf=t+u` grain plus the plate's own
high-frequency texture, and the only way to take it lower is to remove grain from that
beat alone — a look change, which is out of scope for a mechanical round. On the metric
where the "1.6–2.5" baseline is true, every window is inside 1.0–3.5 with margin.

---

## 2 · END-CARD STAGGER ORDER — fixed

**Round 4:** `end_title` f772 · `end_ruleA/B` f776 · `end_tag` f778 · `cta_lead` **f775** ·
`cta_number` **f775** · dates f780/784/788/792/796. At f780 the title, tag, "Text TRUXOR
to" and the number were all at full while the four dated rows were still animating in
above them — the card resolved bottom-up and the number arrived before the schedule it is
the answer to.

**Round 5 order, printed by the build:**

```
end_title@f772 -> end_ruleA@f773 -> end_date0@f775 -> end_date1@f777
-> end_date2@f779 -> end_date3@f781 -> end_date4@f783 -> end_ruleB@f784
-> end_tag@f785 -> cta_lead@f786 -> cta_number@f787
```

wordmark + its rule are already on (f0, `hard=True`, directive C) → title → dates → tag →
"Text TRUXOR to" → **the number last**. Stagger is 2 frames instead of 4 so the whole
cascade fits before the number's deadline. **Entrances are untouched: `IN_F = 5`,
smoothstep, 16 px rise, unchanged.**

| | round 4 | round 5 | required |
|---|---|---|---|
| number's entrance | f775 (4th of 11) | **f787 — last of 11** | last ✔ |
| number reaches full | f780 · 26.000 s | **f792 · 26.400 s** | ≤ f792 / 26.400 ✔ |
| number holds at full | f780–899 = 120 f = 4.000 s | **f792–899 = 108 f = 3.600 s** | ≥ 3.6 s ✔ |
| anything entering after it | tag, dates | **none** | none ✔ |

Both facts are now build asserts, not prose: the run aborts if `cta_number` is not the
last entrance, if it reaches full after f792, or if the hold falls under 108 frames.

**Stated plainly:** the CTA hold is 0.400 s shorter than round 4. That is the direct cost
of putting the number last, and 3.600 s is the floor this round was given.

---

## 3 · LOOP SEAM — closed to +7.5

**Round 4:** f899 YAVG **58.0** against f0 **82.2** — a **+24.1** step on auto-loop
(measured at 108×192 and at full resolution; both give the same number. The +28 figure in
the round-4 critique is a third scale; on this build's own YAVG log it is +24.1, and the
before/after below is like-for-like on one script).

**Fix — the ground, not the type, and the opening frame is untouched.** Over the card's
last **10 frames** an `eq=brightness` ramp on the **card segment only** lifts the ground
`+0.075` (≈ +19 encoded levels) on a smoothstep, so it settles rather than flashes. The
navy token `#1B2A4A` is unchanged for the 118 frames the card actually holds — the base
luma was **not** lifted, because lifting it costs contrast across the whole card instead
of across ten frames.

| | round 4 | round 5 |
|---|---|---|
| f0 YAVG | 82.2 | **82.2** (unchanged — directive C spread f0–f10 still +0.42) |
| f899 YAVG | 58.0 | **74.6** |
| **seam step** | **+24.1** | **+7.5** ✔ (target ≤ 12) |
| card tail f889→f899 | 58.0 flat | 58.0 · 58.0 · 57.0 · 57.0 · 60.0 · 64.8 · 66.8 · 69.7 · 71.7 · 74.6 · 74.6 |
| `cta_number` at f899 | 12.03:1 | **8.82:1** ✔ (floor 7.0) |

Per-frame contrast across the whole ramp is `_r5/measure_seam_contrast.py`, measured with
`proof()`'s own hole-punch method on the delivered frames:

| frame | `cta_number` | `cta_lead` | `end_title` | `end_date0` | `end_tag` (bronze) |
|---|---|---|---|---|---|
| f890 (pre-ramp) | 12.03 | 12.30 | 13.01 | 12.94 | 4.91 |
| f893 | 11.68 | 11.94 | 12.52 | 12.43 | 4.76 |
| f894 | 10.69 | 10.94 | 11.57 | 11.49 | **4.37 FAIL** |
| f896 | 9.68 | 9.97 | 10.62 | 10.52 | **3.97 FAIL** |
| f899 | **8.82** | 9.08 | 9.67 | 9.60 | **3.63 FAIL** |

### The one regression this fix creates, stated up front

**`end_tag` — `scrape · haul · cover`, bronze `#C4976E` — drops under the 4.5:1 floor on
f894–f899. Six frames. 200 ms.** It holds 4.91:1 for the other 3.93 s of the card. The
build prints it as a failure rather than hiding it: `contrast FAILURES: ['end_tag@t=29.93']`.

**It is arithmetic, not an oversight.** Bronze needs a ground ≤ 55 for 4.5:1. The card
ground measures 49.6, so bronze has **+5.5 levels of headroom**. Closing a 24-level seam
to ≤ 12 needs **at least +12.2 levels**. There is no lift that satisfies both, and every
alternative I could reach for is a change this round was told not to make:

- a smaller lift → tag still fails (at the minimum +12.2 it reads 4.08:1) *and* the seam
  misses its target;
- lifting the base ground instead → costs the tag for the whole card, not for 200 ms;
- darkening f0 → forbidden, the opening frame's legibility is fixed;
- fading the tag out under the ramp → works perfectly, and is a new taste call.

The brief's own constraint named one floor for this fix — the number at ≥ 7:1 — and the
number holds **8.82:1** at f899. If Nate would rather keep the tag at 4.91:1 all the way
to f899 and live with a +24 seam, that is one constant: `SEAM_LIFT = 0.0`.

---

## Everything measured, round 4 → round 5

| | round 4 | round 5 |
|---|---|---|
| frames / duration | 900 / 30.000 s | 900 / 30.000 s |
| deepest ink | y 1362 (74 px clear) | y 1362 |
| left edge, margin ink x0 | {82, 83, 84} | {82, 83, 84} |
| directive C, YAVG spread f0–f10 | +0.42 PASS | **+0.42 PASS** |
| directive A, `cta_number` worst-local | 12.03:1 | **8.82:1** PASS (floor 7.0) |
| lockup worst-local | 7.09:1 | **6.71:1** PASS (floor 6.0) |
| worst eyebrow | 4.76:1 (`s3_eyebrow`) | **4.76:1** PASS |
| directive E, payoff min | 1.41 | **1.41** PASS (floor 1.0) |
| cuts / scene changes @0.10 | 5.567 · 9.233 · 12.9 · 16.567 · 20.233 · 23.9 | identical |
| loudness | I −14.1 · LRA 7.6 · TP −2.0 | **identical** |
| TikTok dead zones | CLEAR | **CLEAR** |
| contrast failures | none | **`end_tag` f894–899 (see §3)** |

`lockup` moved 7.09 → 6.71 because the hydrilla beats no longer shake: the worst-local
ground tile under the wordmark is now sampled from a stiller picture. Still 0.71 over its
floor, and it is the same scrim at the same 0.58.

---

## Every changed line vs round 4

`git diff` of `06_Media_Build/build_lcd_v2.py` against `8e44574` (round 4) — **+77 / −17**,
of which 51 added lines are comments. The functional changes are these and nothing else:

| # | line(s) | round 4 | round 5 | why |
|---|---|---|---|---|
| 1 | `OUT = …` (was L62) | `os.path.join(V2, "renders", "LCD_v2")` | `os.environ.get("LCD_OUT") or sys.argv[1] or <same default>` | **output-dir override.** Default unchanged; `STRAPS/SEG/QC/LOGS/FINAL/SILENT` all derive from `OUT`, so one constant relocates the whole run |
| 2 | `SHOTS` 02a | `(1.120, 1.050)`, `jit 0.55` | `(1.000, 1.100)`, `jit 0.00` | defect 1 |
| 3 | `SHOTS` 02b | `(1.050, 1.120)`, `jit 0.55` | `(1.000, 1.100)`, `jit 0.00` | defect 1 |
| 4 | `CTA_IN` | `775` | `786` | defect 2 — "Text TRUXOR to" |
| 5 | new: `CTA_NUM_IN` | — | `787` | defect 2 — the number, last |
| 6 | new: `DATE_IN`, `DATE_STEP` | — | `CARD_IN + 3`, `2` | defect 2 — the schedule cascade |
| 7 | new: `CTA_HOLD_MIN` | — | `108` | defect 2 — 3.600 s floor |
| 8 | `add("cta_number", …)` | `CTA_IN` | `CTA_NUM_IN` | defect 2 |
| 9 | `add("end_tag", …)` | `CARD_IN + 6` | `CARD_IN + 13` | defect 2 |
| 10 | `add("end_ruleB", …)` | `CARD_IN + 4` | `CARD_IN + 12` | defect 2 |
| 11 | `add("end_ruleA", …)` | `CARD_IN + 4` | `CARD_IN + 1` | defect 2 |
| 12 | `add(f"end_date{i}", …)` | `CARD_IN + 8 + 4 * i` | `DATE_IN + DATE_STEP * i` | defect 2 |
| 13 | CTA hold assert | `if len(full) != 120: raise` | `if len(full) < CTA_HOLD_MIN: raise` | defect 2 |
| 14 | new assert + print | — | aborts unless `cta_number` is the last entrance and full by f792; prints the whole stagger | defect 2, made a gate |
| 15 | `render_segments`, `post` | — | `if name == "05":` append the smoothstep `eq=brightness … :eval=frame` | defect 3 |
| 16 | new: `SEAM_F`, `SEAM_LIFT` | — | `10`, `0.075` | defect 3 |
| 17 | `QC_T` | ends `29.60` | `… 29.60, 29.93` | defect 3 — so the ramp's own frames are measured for contrast, not skipped |
| 18 | `before_after()` | `MASTER`, `"v1  SHIPPED MASTER"` / `"v2  ROUND 4"` hard-coded | `LCD_CMP_REF` / `LCD_CMP_A` / `LCD_CMP_B` env, same defaults | so row 1 can be round 4 instead of v1 |

**Untouched:** every string, every plate, every cut frame, the beat grid, the grade, both
scrims and their one transition, the type scale, all seven rules, `IN_F`/`OUT_F`/`RISE`,
the safe box, the copy/COUNT/C7 guards, the whole audio chain, `CARD_MIX`, `CARD_SIGMA`,
the navy/cream/bronze tokens, and the end-card geometry solver.

### How this render was produced

```bash
cd /Users/austinlakescapes/drawdown-2026-campaign/.claude/worktrees/platform-native-renders/06_Media_Build
LCD_OUT="$PWD/renders/LCD_v2/_r5" \
LCD_CMP_REF="$PWD/renders/LCD_v2/LCD_v2_916.mp4" \
LCD_CMP_A="r4  ROUND 4 (LCD_v2_916.mp4)" \
LCD_CMP_B="r5  ROUND 5 (_r5/LCD_v2_916.mp4)" \
python3 build_lcd_v2.py
```

`python3 build_lcd_v2.py` with no env still writes `renders/LCD_v2/` exactly as round 4
did. `06_Media_Build` (the source tree) was neither written nor renamed —
`sys.dont_write_bytecode = True` still holds and no `__pycache__` exists there.

---

## Known gaps carried forward from round 4, unchanged

Round-4 gaps 2 (end-card bottom void on a GBP cut), 3 (`s3_eyebrow` at 4.76:1), 4 (the
0.84 lower gradient), 5 (the −9.8 YAVG step at f607), 6 (the hydrilla reads cool), 7 (no
scene change crosses 0.25 full-frame), 8 (the wide plates are soft) and 9 (nothing has
been through a platform round trip) are all still true and were not in scope. Gap 1 — the
loop seam — is closed.

**New this round:** `end_tag` under 4.5:1 for the final 6 frames, §3. Nothing else moved.

**Nothing posts. Nate sees it first.**
