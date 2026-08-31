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
| 0 | Lead-in 16s | registry Ken Burns | **v4 silent — claim_ok pins only** | `DRAWDOWN_LeadIn_916_v4_REGISTRY_SILENT.mp4`. Splice VO archived. Wait on wife EL voice. |
| 1 | Honest Math | 06 | **G3 draft, unsigned** — Nate watch | `DRAWDOWN_Math_916_FINAL.mp4` + `build_math_card.py` |
| 2 | Exposed Truth | 01 | **G3 draft, unsigned** — Nate watch | `DRAWDOWN_ExposedTruth_916_DRAFT.mp4` + `SHOTLIST_ExposedTruth_01_2026-08-30.md` |
| 3 | Fleet still | — | plate on desk | `~/drawdown-sprint/dcc-close-book/public/media/fleet.jpg` — LinkedIn caption |
| 4 | Under the dock | 04 | only if a real plate exists | skip otherwise |

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

### Next Claude session
Script 01 only. Audit Poseidon by caption. Pin sha256. Do not recut 16s or 12s math unless Nate says.

## Open questions
- [ ] Nate VO on the 16s, or ship silent?
- [ ] Slot count `[X]` — wait for a real Mon/Thu count
- [ ] Day 4 / Day 7 still empty on the old campaign calendar — fill from 01/fleet, don’t invent a seventh reel
