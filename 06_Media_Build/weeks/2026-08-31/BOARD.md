# Week of 2026-08-31 — short drawdown pieces

Handshake for **Hermes + Claude Code**. Dump brainstorm here. One session = one row.

**Kitchen:** `~/drawdown-2026-campaign/06_Media_Build/`  
**Kickoff (full rules):** `../KICKOFF-WEEK-REELS-2026-08-30.md`  
**Desk:** `http://localhost:8080/?closeBook=1&tab=media` — captions, not the editor.

## Direction

Close week. Public posts = **window + $695**, not named-lot iron, not CY. Craft = Ken Burns over real Poseidon stills, ~12s, one idea, one CTA. Silent first. Hedge in the same breath.

## Board

| # | Piece | Script | Status | File |
|---|--------|--------|--------|------|
| 0 | Viral lead-in 15.3s | Hydrilla Horror (no $695) | **G3 draft on desk, unsigned** — Nate watch | `DRAWDOWN_ViralHydrilla_916_STUDIO.mp4` + `build_viral_leadin_studio.py` + `resolve/viral-leadin/`. Silent master. Hermes previews `DRAWDOWN_ViralHydrilla_916_v1*.mp4` left in place. |
| 1 | Honest Math | 06 | **G3 draft, unsigned** — Nate watch | `DRAWDOWN_Math_916_FINAL.mp4` + `build_math_card.py` |
| 2 | Exposed Truth | 01 | **G3 draft, unsigned** — Nate watch | `DRAWDOWN_ExposedTruth_916_DRAFT.mp4` + `SHOTLIST_ExposedTruth_01_2026-08-30.md` |
| 3 | Fleet still | — | plate on desk | `~/drawdown-sprint/dcc-close-book/public/media/fleet.jpg` — LinkedIn caption |
| 4 | Under the dock | 04 | only if a real plate exists | skip otherwise |
| 5 | Scrape Haul Staple | method explainer | **G3 draft on desk, unsigned** — Nate watch | `DRAWDOWN_ScrapeHaulStaple_916_STUDIO.mp4` + `build_scrape_haul_staple.py` + `resolve/scrape-haul-staple/`. Silent master, 15.00s. Beat 3 ships as **COVER** — the erosion-matting plate with matching copy, NOT a type card. Corrected 2026-09-02, see below. |

Skip: generated Meet-the-Machine (02/05), Neighbor (07) without a real booking, `AI生成` vision clip, Vercel ship, Studio Post Ready.

## Dump (append, don’t rewrite history)

### 2026-08-30 Hermes
- 77s Truxor = Claude Code / Opus, Aug 4, `compose.py`. Not Cursor. Scratch VO, Arial, too long for a lead-in.
- Hermes cut silent 16s: hydrilla → projected 10–12 ft → iron → $695.
- Registry play (Cursor ATX-1867, this Mac): `registry.py` 39 assets. DRAWDOWN pins mac-usable: @bulkhead_undercut, @two_machines, @farshore_golden (claim_ok). @dock_lowwater is mythology — do not caption as proof. Stills copied to `resolve/leadin-lineup/stills/`. @truxor tag is pending (no sha). Cloud gaps: no Drive on the claim plates.
  - **ERRATUM 2026-08-31 (appended, Hermes' line left intact): `@two_machines` is
    NOT `claim_ok`.** Its source frame is a knuckleboom crane on a barge — one
    machine, no amphibious undercarriage. It fails C7 and must be treated as
    EXCLUDED until the pin is relabelled on PR #83. C7-safe substitutes, both
    eyeballed, sha-pinned in `compose.py`: `c6b6853c038a` (two Truxors working,
    pontoons visible) and `fd49bf6ffe3e` (two Truxors staged).
- Claude Code then built Script 06 type card (12s, cream, `[X]` literal). Watch it before 01.

### 2026-08-30 Nate ruling
- **`truxor-leadin-15-vo.mp4` DOES NOT SHIP.** Scratch VO is not a Nate read and
  not a Nate-approved voice. Delete or archive it; do not put it on the desk.
- New VO to be recorded in Nate's wife's ElevenLabs voice. Script below, unread.

### 2026-08-31 C7 defect — desk was shipping a false equipment claim
- `leadin-registry-silent.mp4` (registered `M-TRUXOR-LEADIN`, status draft) had a
  **TWO AMPHIBIOUS MACHINES** card over a frame showing **one knuckleboom crane
  on a barge**. No second machine, no pontoon undercarriage. Violates C7.
- Root cause is the pin, not the render: `@two_machines` is mislabeled at source
  (`resolve/leadin-lineup/stills/03_@two_machines.jpg` is the crane barge).
- That pin lives on **unmerged PR #83** (ATX-1867). The asset-registry skill is
  installed on every seat but `scripts/visual-library/registry.py` is NOT on
  main — the commands in the skill fail. Doc shipped, mechanism did not.
- Desk swapped to `leadin-v3-victoria.mp4` (C7-verified plates, spoken hedge).
  Resolve is still the intended finisher; this is a claim-clean stand-in.

### 2026-08-31 Nate — viral, not inspection. Full studio.
- Forget $695 / assessment as the lead-in closer. Hook + inform. CTA = TRUXOR / 254-780-6971.
- `@two_machines` barge called out again on the Hermes viral cut. Swapped preview to `c6b6853c038a` (two Truxors, letterboxed) + `924c9e39682b` (underwater hydrilla for "never seen it").
- Hermes `build_viral_hydrilla.py` is a **preview**. Kickoff for Claude: `KICKOFF-VIRAL-LEADIN-STUDIO-2026-08-31.md`.
- Do not recut Math / Exposed Truth this session.

### 2026-08-31 Hermes QC (collab with Claude 3a7599b1)
- Claude dropped `DRAWDOWN_ViralHydrilla_916_STUDIO.mp4` (15.3s). C7 PASS on beat 3 (`c6b6853c038a`, two Truxors, not barge).
- Notes in `weeks/2026-08-31/HERMES_QC_STUDIO.md`: swap beats 1↔2 pictures so "UNDER YOUR DOCK" sits on the dock-edge plate; soften letterbox; true silent; desk draft.
- No $695 on this cut.

## Open questions
- [ ] Nate VO on the 16s, or ship silent?
- [ ] Slot count `[X]` — wait for a real Mon/Thu count
- [ ] Day 4 / Day 7 still empty on the old campaign calendar — fill from 01/fleet, don’t invent a seventh reel

### 2026-08-31 Claude studio — viral lead-in SHIPPED to desk (draft)

**`DRAWDOWN_ViralHydrilla_916_STUDIO.mp4` — 15.30 s · 1080x1920 · 30 fps · CRF 18 · faststart · SILENT.**
Built by `build_viral_leadin_studio.py` (new slug, new filter graph — the Hermes
previews `DRAWDOWN_ViralHydrilla_916_v1*.mp4` were left untouched).
Resolve bin + README: `resolve/viral-leadin/`. Desk: `public/media/viral-leadin-studio.mp4`,
`mediaDesk.ts` row `M-VIRAL-LEADIN-STUDIO`, **status draft**. Not posted. Not shipped to Vercel.

Gate 0 carried from the Grok draft: title *Hydrilla Horror — the window* · pole
Problem→Capability · CTA **TRUXOR / 254-780-6971** · six pillars PASS with
**pillar 6 (offer unit) OVERRIDDEN** — Nate stripped the inspection. GREENLIGHT.

**Four plates, audited by Poseidon caption then eyeballed on this Mac:**

| # | In | sha256 | Mode |
|---|----|--------|------|
| 1 | 0.00 | `f730acf1ac49dae940dcd30e7597b1caa554d6d60fbd1a4b1531b5eb99d069ef` | bleed |
| 2 | 2.95 | `924c9e39682b244ced6fb2cea57ab18a8f81c95cf7a3ea2af904ff2d944206cc` | bleed |
| 3 | 6.95 | `c6b6853c038a87b18338b0a6fd0c94a377f84947475caa53cbab3da44d1cff83` | **fit** |
| 4 | 10.95 | `83f97f1642cd2172ab76216d46fbee631e81d36e942516fc5136febd889ab75c` | bleed |

Overlay strings, exact:
`THIS IS UNDER / YOUR DOCK.` · `NEARLY TEN YEARS / SINCE ANYONE COULD SEE IT.` ·
`TWO TRUXORS. / PROJECTED 10–12 FT. / NOTHING IS OFFICIAL YET` ·
`SCRAPE. HAUL. STAPLE. / 254-780-6971` (holds to the last frame).

**Audit of the banned pin, independently confirmed.** Poseidon's own VLM caption
for `1334bce67b99` reads *"A yellow excavator is positioned on a floating
platform at a dock on Lake Austin"* — `vlm_label=dredging`. One machine, no
amphibious undercarriage. The 2026-08-31 erratum above is correct and the pin
stays EXCLUDED until PR #83 relabels it. `c6b6853c038a` caption reads *"Two
Truxor weed removal machines operating on a lake"* and the frame shows both,
on water, one throwing spray. C7 satisfied on count **and** equipment type.

**Ledger note (not a conflict, a resolution).** Nate's beat-2 string was
`TEN YEARS. YOU'VE NEVER SEEN IT.` Read literally that asserts ten years of
unseen weed growth, which **has no ledger row** — and Gate 1's rule is "no row
here, no claim on screen." The rowed fact is **C3**, *"first meaningful
low-water window in nearly ten years."* Card 2 was written as
**`NEARLY TEN YEARS / SINCE ANYONE COULD SEE IT.`** — same two beats, same
cadence, now anchored to C3 and asserting nothing about the future. Flagging it
rather than swapping it silently. **C1 is never asserted on this cut**; the one
number carries `PROJECTED` *and* `NOTHING IS OFFICIAL YET` on the same card,
because a silent master cannot hedge in the VO.

**Two QC defects caught and fixed before delivery — both invisible in a green render:**

1. **The cut collapsed onto the last plate.** `-loop 1 -i still.jpg` defaults to
   **25 fps** while `zoompan(fps=30)` labels its output 30 fps, so every beat ran
   5/6 of its nominal length, the xfade offsets walked past the end of their
   inputs, and beats 2–4 all rendered plate 4. ffmpeg exited 0 and said nothing.
   Caught only by extracting mid-beat frames. Fix: `-loop 1 -framerate 30 -i`.
   **A clean exit code is not QC. Pull frames.**
2. **Card 1 contradicted its frame.** `924c9e39682b` opened the cut under
   `THIS IS UNDER YOUR DOCK.` — but the 9:16 bleed crop cuts away the dock edge,
   so the card claimed a dock the viewer cannot see. Same class of failure as the
   barge, one notch smaller. Plates 1 and 2 were swapped: the hook is now
   `f730acf1ac49`, shot looking straight down off a dock deck, dock hardware in
   frame. Card and frame now agree.

Also fixed: the FIT letterbox band was floating (raised to 0.44), and the closing
card no longer fades out — the phone number holds on the last frame.

**VO: wording locked, unread, not muxed.** `weeks/2026-08-31/VO_ViralLeadin_Studio_LOCKED.md`
(41 words, ~15 s, C1/C2/C3/C7 traced). Victoria has still not approved a script,
so the master ships silent per the 2026-08-30 Nate ruling. No splice of the 77 s
scratch VO. `build_leadin_vo.py` holds the clone path when she signs off.

Open for Nate: the straps are still Arial. Picture is real and claim-clean; the
type wants a Resolve pass, which is what `resolve/viral-leadin/` is staged for.

### 2026-08-31 Nate — drawdown is official
- Stop saying exploring / unofficial / “nothing is official yet.” C1 hedge retired by Nate.
- Depth may still be projected 10–12 ft (C2) if a number is on screen.
- Horror reel still has `NOTHING IS OFFICIAL YET` on card 3 — do **not** recut it in the scrape session. Flag for a later type pass.

### 2026-08-31 Hermes → Claude: Scrape. Haul. Staple.
- Separate 15s method explainer. Kickoff `KICKOFF-SCRAPE-HAUL-STAPLE-2026-08-31.md`.
- Slug `DRAWDOWN_ScrapeHaulStaple_916_STUDIO.mp4`. Do not overwrite the horror lead-in.

### 2026-09-01 Claude studio — Scrape. Haul. Staple. SHIPPED to desk (draft)

**`DRAWDOWN_ScrapeHaulStaple_916_STUDIO.mp4` — 15.00 s (450 frames) · 1080x1920 ·
30 fps · CRF 18 · faststart · TRULY SILENT (no audio stream at all, not a null
AAC track).** Built by `build_scrape_haul_staple.py` — new slug, new builder. The
viral lead-in and the Math / Exposed Truth cuts were not touched.

Resolve bin + README: `resolve/scrape-haul-staple/` (`stills/`, `composites/`,
`qc/`). Desk: `public/media/scrape-haul-staple-studio.mp4`, `mediaDesk.ts` row
`M-SCRAPE-HAUL-STAPLE`, **status draft**. Not posted. Not shipped to Vercel.
`npx tsc --noEmit` on the close-book exits 0.

**Beats — four real plates.** Beat 3 is a COVER picture, not the type card this section originally described (corrected 2026-09-02).

| # | In | Sha256 | Mode | Strap |
|---|----|--------|------|-------|
| 1 | 0.00 | `c6b6853c038a87b18338b0a6fd0c94a377f84947475caa53cbab3da44d1cff83` | **fit** | `SCRAPE.` / `We cut it off the bed.` |
| 2 | 4.00 | `83f97f1642cd2172ab76216d46fbee631e81d36e942516fc5136febd889ab75c` | **fit** | `HAUL.` / `Off your lot.` |
| 3 | 9.00 | `247ed525d59d` (prefix as pinned in `BEATS`) | **fit** | `COVER.` / `Mat on the bed.` |
| 4 | 13.00 | `870b907f2401c31452ee002d03078b75be932bfcdba8d642e8d5a65abb6e89ac` | bleed | `That's the job.` / `254-780-6971` |

**THE STAPLE GAP — logged, not faked.** Swept all **3,619 Poseidon VLM captions**
for `staple / overlap / geotextile / weed barrier / landscape fabric / woven tarp
/ polyethylene / burlap / coir`. **Zero hits.** Nothing in the library shows a
woven tarp, a stapled seam, or a 12-inch overlap.

The nearest real thing is **green erosion-control matting on a bank** —
`247ed525d59d` is a crew rolling matting out over scraped black muck at the
water's edge, and it is genuinely close in shape (fabric, over a scraped bed,
while the water is down). It is still a **different product doing a different
job**, and "Woven tarp. 12-inch overlap." over green erosion netting is the same
overclaim class as the `@two_machines` barge, one notch smaller.

**What was actually built** (corrected 2026-09-02 — the next two sentences used to
say the beat was a cream type card and the plate was parked out of the cut; both
were wrong): the plate IS beat 3, at `fit`, and the *copy* was changed to match it
rather than the beat being replaced. The strap reads `COVER.` / `Mat on the bed.`
Green matting on screen, a mat in the words. The tarp claim is never asserted over
it, which is what this section exists to prevent. A copy of the plate is also
staged as
`resolve/scrape-haul-staple/stills/GAP-CANDIDATE_erosion-matting-NOT-a-tarp_247ed525d59d.jpg`.
Four more of the same class: `049c9c5aefa0`, `af49fffbf0ab`, `7a549dd65708`,
`4b0528304977`.

**To close it properly: shoot it.** One frame of woven tarp on a dry bed with the
overlap and a staple visible lets beat 3 carry `STAPLE.` and makes the piece match
its own title. Do not generate one — Rule 11.

**Deliberate deviation from the packet: beat 2 ships FIT, not bleed.** A 9:16
cover-crop of the 1080x810 native keeps the spoil mound and **cuts the LOAD TRAIL
dump trailer out of frame** — and the trailer is the only thing in the picture
that makes "Off your lot." honest. Same rule that already makes the two-machine
plate fit: claim safety beats composition. Both fit beats **pull out**
(1.05 → 1.00) instead of pushing in, so each beat *ends* on the complete frame
and the claim-critical element can never be zoomed off the edge — which is the
generalised fix for the "card contradicted its frame" defect from 2026-08-31.

**QC: four mid-beat frames pulled and eyeballed** (`QC_shs_t2.0/6.5/11.0/14.2.png`,
copied into the Resolve bin). Two Truxors present under `SCRAPE.`; dump trailer
present under `HAUL.`; card matches frame on all four; no beat collapse; `ffprobe`
reports 15.000000 s, 450 frames, **one stream, video only**. The `-framerate 30`
guard from the last session is carried into the new builder with the reason in a
comment — a clean ffmpeg exit is still not QC.

**Nate 2026-08-31 rules honoured on this cut:** the drawdown is **official** — the
words *exploring*, *unofficial*, *nothing is official yet* appear nowhere in the
picture, the straps, or the desk caption. No inspection unit, no *credited*, no
*assessment*, no *extinct*, no CY. `@two_machines` untouched and still excluded.
No t2v anywhere.

Open for Nate: (1) does green erosion matting get to carry the staple beat with
reworded copy, or does somebody shoot the tarp — his call, not mine; (2) straps
are still Arial, which is what `resolve/scrape-haul-staple/` is staged for.

### 2026-09-02 CORRECTION — beat 3 is COVER, and this board said otherwise

Recovering this session's work for commit surfaced a mismatch between what this
board recorded and what `build_scrape_haul_staple.py` actually renders. Two
independent PR reviewers flagged it on PR #4 before the merge; the code confirms
it. The board was wrong, not the cut.

**What ships.** `BEATS` holds four picture entries. Beat 3 is
`("b3", "247ed525d59d", "fit", 4.35, "out")` — the green erosion-control matting
plate — carrying the strap `COVER.` / `Mat on the bed.`

**What this board claimed.** That beat 3 was a type-only card reading
`STAPLE.` / `Woven tarp.` / `12-inch overlap.`, and that the matting plate was
parked as a GAP-CANDIDATE "for a Nate ruling, not for a cut." The plate is in the
cut. It has been since the piece was built.

**Nothing overclaims.** Whoever built it swapped the *copy* rather than the beat:
green matting on screen, "Mat on the bed." in the words. The tarp claim was never
asserted over a matting picture — which is the failure this section was written to
prevent. The Poseidon sweep below stands and is still the reason there is no tarp
beat: 3,619 captions, zero hits.

**Two things left open by this correction:**

1. `STAPLE_CARD` at `build_scrape_haul_staple.py:81` is **dead code** — no `BEATS`
   entry uses `mode == "card"`, so the `if mode == "card"` branches at lines 109
   and 185 never execute. That dead constant still reads
   `STAPLE.` / `Woven tarp.` / `12-inch overlap.` It is one `BEATS` edit away from
   putting the retired tarp claim on screen. Delete it, or wire it deliberately.

2. The piece is still titled **Scrape. Haul. Staple.** while its third beat says
   COVER. Either the title follows the picture, or somebody shoots the tarp and
   the beat follows the title. Nate's call, not the builder's.

The upstream briefs — `KICKOFF-SCRAPE-HAUL-STAPLE-2026-08-31.md`,
`CLAUDE_PROMPT_SHS.txt`, and `GROK_VIDEO_ScrapeHaulStaple_v1_DRAFT.md` — still
specify the type-only beat. They are left as written: they are the ask that went
in, not the record of what came out. This board is the record.

### 2026-09-04 CORRECTION — the COVER beat shipped sideways; caught by audit, rebuilt

A max-effort Fable audit of the finished cut extracted real frames and found the
9–13s COVER beat rendered **rotated 90°** — trees horizontal, crew sideways —
in the 09-01 17:54 master, the desk copy, and the QC frame that had been filed
as passing.

**Root cause.** The Poseidon jpg for `247ed525d59d` stores upright landscape
pixels (1080x810, matching `refs.width/height`) under a **stale EXIF
Orientation=6 tag**. `ImageOps.exif_transpose` trusted the tag and swung the
correct scene into a sideways 810x1080 portrait, which the FIT branch pasted
nearly full-frame. The other three plates carry Orientation=1, which is why only
beat 3 broke. The repo still displays upright in orientation-ignoring viewers —
so the 09-01 COVER ruling was made on an upright image the cut did not show.

**Fix (this branch).** `build_scrape_haul_staple.py` now treats the registry's
`refs.width/height` as display truth: when the EXIF transpose contradicts the
registry and the raw pixels agree with it, the tag is ignored (printed, not
silent); if orientation still contradicts the registry after that, the build
**fails closed** instead of shipping a sideways plate. Photo bytes untouched —
the store is content-addressed and a byte edit would change the sha.

**Rebuilt + re-verified 2026-09-04.** New master md5 `2e68544f616ce8f0` — master,
desk copy `scrape-haul-staple-studio.mp4`, and worktree build byte-identical.
All four QC frames re-extracted and eyeballed: two Truxors + spray under
SCRAPE., LOAD TRAIL trailer legible under HAUL., **upright** matting under
COVER., cutter-head CTA under HOLD. ffprobe: 15.000s, 450 frames, 30fps,
1080x1920, single video stream, no audio. `resolve/scrape-haul-staple/qc/` and
`composites/` refreshed from this build (composites had also been missing
`card_b3.png`). Spec note: output is full-range `yuvj420p` (`color_range=pc`),
not the `yuv420p` the README claimed — README corrected rather than re-grading
a look already approved.

QC lesson, standing: **extraction is not a verdict.** The failing frame was
pulled twice on 09-01 (17:54 and 18:00) and still shipped, because the check
stopped at strap-matches-frame. Each QC frame now gets an explicit pass on
claim, strap, orientation, and crop before "verified" is written anywhere.

### 2026-09-04 NATE RULING — COVER is the third verb, campaign-wide; the hedge is off every card

Two open questions closed in one pass, because both lived on the same cards.

**The verb.** The lead-ins closed on `SCRAPE. HAUL. STAPLE.` while the method cut
teaches `SCRAPE. HAUL. COVER.` A homeowner who saw both learned a contradiction.
Nate's call: **COVER everywhere.** COVER is the verb backed by a real
photographed plate; STAPLE has no honest image anywhere in Poseidon (3,619
captions swept, zero hits), and the method cut's third beat is erosion matting.
The corpus still documents the actual operation — "staple woven tarp, 12 IN
overlap" is what the crew does, and the close-sheet warranty still says so
verbatim. The cards changed, not the job. Re-open the verb only when somebody
shoots a woven tarp with the overlap and a staple visible.

This supersedes the COPY RULING at `build_real_motion.py:24`, which read
"'STAPLE' is correct and stays." That ruling was right about the corpus and
wrong about the pictures: the corpus records what we DO, the cards record what
we can SHOW.

**The hedge.** `NOTHING IS OFFICIAL YET` was burned into the lead-in masters —
not just captions — and LCRA announced on 2026-08-29. Every occurrence is now
`THE DRAWDOWN IS OFFICIAL`. `PROJECTED 10–12 FT.` is untouched: the depth is
still a projection and stays hedged.

**Builders changed** — `build_viral_leadin_studio_claude.py`,
`build_viral_leadin_studio.py`, `build_real_motion.py`, `build_viral_hydrilla.py`.
Both viral lead-ins rebuilt 2026-09-04 22:27 and QC'd by eye at the two changed
plates in each: C7 holds (two Truxors, pontoon decks, spray in frame), end card
reads COVER, hedge plate reads OFFICIAL. Masters promoted to the main checkout
and refreshed in the Cut Room. `build_real_motion.py` and `build_viral_hydrilla.py`
are corrected at source but NOT rebuilt — their masters are older drafts nobody
has picked; they build clean whenever somebody wants them.

**Still open on these two:** the VO. One cut speaks the retired hedge, and
Victoria has never approved any script. Nothing is muxed. That is question 05 in
the Cut Room.

### 2026-09-06 — bed picked, still series built, schedule pinned to the LCRA calendar

**Q01 settled.** Victoria queued *Mud Window v2* in the Cut Room. Picked master is
`DRAWDOWN_ScrapeHaulStaple_916_SUNO_MudWindow_v2.mp4` — video stream md5
`4eed1544dd58b0c21030597c5e47337c`, identical to the fixed silent master, so the
bed rode the corrected picture. Nate sign is the only thing left on it.

**Dates are real now.** LCRA / City of Austin release: lowering **Oct 12**, ~1 ft/day,
target 481.8–482.8 ft msl ("about 10 feet"), refill from **Nov 24**, normal pool
**Nov 30**. ⚠️ The cuts say `PROJECTED 10–12 FT.`; LCRA says about 10. Ledger row
for Nate — two numbers are on two surfaces until he picks.

**Still-card series S01–S08** — `build_plate_cards.py` → `cards/`, 9:16 + 4:5, eight
real plates, all eyeballed, verdicts in `cards/PINS.md`. Dates · Under Your Dock ·
Past The Dock · Scrape · Haul · Cover · Two Machines (C7: `fd49bf6ffe3e`, pontoons
visible) · Seven Weeks CTA. `53482b8a99a8` excluded — bytes sideways, registry
disagrees, guard can't certify.

**Schedule:** `PRODUCTION_SCHEDULE_2026-09-07.md` — W37→W41 runway from the
library (3 videos + 8 stills ready, 3 pieces to BUILD, 2 NEEDS-VO/CALL), W42→W48
live from field capture with the six-item Rule 11 shoot list. Do-not-post list
names every dirty file in this folder and why.

**Found and parked:** `Weed Barrier Photo.png` / `Weed Mat Framed.png` at repo root
(09-02) are LakeMat.com screenshots — third-party, not plates. 59 "tarp" captions in
Poseidon are boat covers and tarped loads. Still no stapled-bed photo. COVER stands.

### 2026-09-06 (evening) — end to end, with proof

Nate: "get it done all the way end to end with proof." Three more pieces, one shared
builder, one measured proof sheet.

- **`build_timeline_cut.py`** — the shared module the 09-04 audit asked for: real
  clips and real stills, fit-letterbox, registry-wins orientation guard, C7 count
  check, banned-string check, xfade chain, optional bed, and it writes its own
  resolve bin (straps, one QC frame per beat, PINS.md with md5). Two cuts live at
  the bottom of the file; a third is a BEATS list.
- **`DRAWDOWN_LakeComingDown_916_STUDIO[_LakeComingDown_v2].mp4`** — 30.00 s, the
  first piece with real motion: five 2026-08-11 DJI proxies (letterboxed, never
  upscaled) + LCRA calendar + Lake Coming Down v2 bed (I −14.5 LUFS, TP −1.7).
  Clips 001/004/006 excluded (person on a private dock). ⚠️ Beat 1 is one
  recognisable residence — honest, Nate's call, one-line swap.
- **`DRAWDOWN_Bulkhead_916_STUDIO.mp4`** — 15.00 s silent, three real low-water
  plates, no price, no percentage. First build came out 14.00 s (2 s card);
  rebuilt with a 3 s card.
- **S09 / S10** countdown cards on the S01 plate.
- **`PROOF_2026-09-06.md`** — every duration, picture, audio, loudness and md5 read
  off the files by script at write time; QC frames listed; banned-string grep
  across the live builders. Five videos, ten stills, all eye-passed.

Still Nate's: sign · 10 ft vs 10–12 ft · lead-in lane · the residence beat.
Still Victoria's: Q02 bed, Q03 vocal, Q05 script, taste on the cards.

### 2026-09-06 17:43 NATE RULINGS — ABOUT 10 FT · house beat stays · SIGNED

Three calls in one line: "Lets go with the about 10ft right? 2 is fine, and sign."

**Depth.** ABOUT 10 FT campaign-wide — LCRA's number (target 481.8–482.8 ft msl).
The one-pager's `PROJECTED 10–12 FT.` is retired from every card. Changed at source:
`build_viral_leadin_studio.py` v3, `build_viral_leadin_studio_claude.py` beat 3
(+ C2 ledger note), `build_viral_hydrilla.py`, `build_real_motion.py`, `compose.py`
k2, `build_plate_cards.py` docstring. Both viral lead-ins rebuilt 17:45–17:46 with
`ABOUT 10 FT. OCT 12.` / `THE DRAWDOWN IS OFFICIAL · LCRA`; depth card eyeballed
on both. Desk captions swept (10 to 12 → about 10; also caught two captions still
saying "scrape, haul, staple" — now cover).

**Lake Coming Down beat 1** (the recognisable residence) stays.

**SIGNED:** method cut + Mud Window v2, both viral lead-ins (silent — lane pick is
Victoria's), Lake Coming Down, Bulkhead, cards S01–S10. Desk rows flipped to
`ready_to_copy`. PROOF regenerated with the new md5s. Still not posted; Hallie posts
from the desk.

**Still Victoria's:** Q02 bed (v2 default), Q03 vocal, Q04 lane, Q05 script, taste.

### 2026-09-06 17:55 VICTORIA'S PRODUCER PASS — seven calls, all actioned

Found sitting in Lavish's store (`~/.lavish-axi/state.json`, `pending_prompts: 7`)
— queued three minutes after my last poll, and the long poll keeps dying on this
Mac's memory. Lesson: after any reply, run one short `--timeout-ms` poll before
reporting "0 pending"; and the store on disk is the ground truth, not the last
poll's answer.

| Q | Victoria | Done |
|---|---|---|
| 02 | Lake Coming Down **v1** | rebuilt with v1 bed |
| 03 | vocal: **undecided — needs a real demo first** | Work the Bed full-lyric demo generating on Suno, task `1f1394b9-66e5-4690-90cc-27d088f9158b` |
| 04 | lead-in lane: **STUDIO_CLAUDE** | studio lane retired on disk (`…_RETIRED-lane-not-picked-2026-09-06.mp4`), off the desk and out of `public/media` |
| 05 | VO: **send the script — I'll read it as written** | 08-31 wording was dead (spoke "exploring" + "projected ten to twelve"). Re-locked to the current cards, 34 words; `VO_ViralLeadin_Victoria_READ.txt` + inline in the Cut Room |
| 07 | cards: **all eight go** | — |
| 08 | schedule: **cadence right** — "we might still add more to this but it's a good start" | — |
| 09 | **swap the house beat** | Lake Coming Down beat 1 → clip 018 t=8 (cove edge, weed mat, no residence). Nate had said it could stay; producer wins on taste, honesty unchanged |

PROOF regenerated. Lake Coming Down ships as `_LakeComingDown_v1.mp4` now; the v2
mux is deleted, not archived — nothing was ever posted from it.

### 2026-09-06 21:30→ SIT-DOWN — Nate + Victoria on the answers board (`.lavish/answers/`)

Live session, answers actioned as they landed:

| Board | They said | Built |
|---|---|---|
| 01 singer | "different voice — Texas country, Kenny Chesney, upbeat" → **Country A, from 0:28** → **"reel goes"** | Suno re-audition (task `e95b8228`, two 80 s takes). `DRAWDOWN_WorkTheBed_916_STUDIO_CountryA_from28s.mp4` — 30 s, real drone opener + four plates + CTA, bed offset 28 s (`build_timeline_cut.py` bed tuple now takes a start). −14.8 LUFS. **Approved.** |
| 02 VO | "combo of 1 and 3, simply explaining coming down 10 ft, the Mike Rowe cloned voice" → "great, add two more sentences, the most informative" | `build_vo_mikerow.py` — ElevenLabs "MikeRow Story Teller" (`s4rOmUeb79uIbzKAm7kQ`, category *generated*, not a person's clone), curl not urllib (py3.14 has no CA bundle). v2 read 13.42 s, muxed at −16.3 LUFS. **Held until sourced:** "licensed for TPWD removal", "number-one monthly maintenance weed company in Central Texas", "ten years" as company age — none in the claim ledger. Added instead: the machines + the job, and "free estimate". |
| 03 Lake Coming Down | "transitions shaky — the drone is moving; slow it or cut it" | `deshake` + `setpts=1.6*PTS` + `minterpolate` on every clip beat (`SLOW=1.6`). Rebuilt, frames checked clean. |
| 04 method cut | "simpler, more explanatory for our ICPs, two amphibious machines, leverage the bulkhead's framework" · "bulkhead is great, 3rd video on point" | `DRAWDOWN_Method_916_STUDIO_v2[_MudWindow_v2].mp4` — same four plates, story straps: SEE THAT? THAT'S UNDER YOUR DOCK · TWO AMPHIBIOUS MACHINES. BUILT TO CUT IT · SCRAPE IT. HAUL IT OFF YOUR LOT · COVER IT. IT DOESN'T GROW BACK THROUGH. v2-vs-v1 call open. |
| 05 type | **A — Arial stays** | nothing rebuilds |

Lavish lesson, again: the foreground poll returned answers within seconds when they
were actively queuing; the ten-minute wait moved it to background and it survived.
The store (`~/.lavish-axi/state.json`) stayed the source of truth throughout.

**Mogul check (Nate asked 22:21 "are you using all the power of atx-media-mogul?").** Honest
answer: laws yes, pipeline no. Ran `pipeline/scripts/voice-qa.sh` over every strap, caption and
the VO — 0 hard, 0 warn. Not used: `gen-line.sh` (AI generation — Rule 11 bans it for anything
with a machine in it), the gate-log format, Resolve power grades (none authored), `ATX_GRADE`
ffmpeg pass (available, not applied blind). Doctrine conflict logged in PROOF: Mogul
visual-identity (Inter/Cloud White) vs campaign AGENTS.md (Cormorant/Source Sans) vs tonight's
ruling (Arial). One reconciliation, not three.

### 2026-09-07 — final answers in, pack and calendar built

The last seven prompts came back off the answers board (the poll died on memory
again; the store had them all — `pending_prompts: 7`).

| Board | Answer | Done |
|---|---|---|
| 01 | Work the Bed reel **goes** | scheduled W39 Mon |
| 02 | **VO v2 goes — Wednesday post** | scheduled Sep 9. The three unsourced claims stayed out of the read |
| 03 | *"this one is just like We Work the Bed now isn't it?"* | correct — the two 30 s pieces had converged. Split: Work the Bed owns the verbs, Lake Coming Down owns the calendar. Recut with a different opener, dated straps, and a hedged C4 close. Also pulled a second recognisable house (011 t=40 → 014 t=60) |
| 05 | Type **A — Arial** | nothing rebuilt |
| 06 | **All ten cards go** | scheduled across W37–W41 |
| 07 | **Meta Business Suite pack** — "same with our IG and tiktok etc" | `SCHEDULING_PACK/`, 18 dated slots, file + caption per folder, 172 MB, captions voice-QA clean |
| 08 | *"a full calendar layout so we can visually click and assess everything"* | `.lavish/calendar/calendar.html` — grid, click a tile, the real file plays with its caption |

Both new builders read from the signed masters and from `pack.json`; nothing in the
pack or the calendar is hand-typed, so a rebuild cannot drift from what ships.
