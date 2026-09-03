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
`TWO TRUXORS. / PROJECTED 10–12 FT.` ·
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
rather than swapping it silently. **C1 was retired 2026-08-29** — LCRA announced
the drawdown — so the event hedge came off this card. The one number still
carries `PROJECTED`, which stays mandatory whether or not the master is silent.

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
- Horror reel had `NOTHING IS OFFICIAL YET` on card 3. **Closed 2026-09-02** — the line is removed from both viral builders and the masters were re-rendered. C1 retired at source in `MEDIA_ClaimLedger_Drawdown_v1.md`.

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
