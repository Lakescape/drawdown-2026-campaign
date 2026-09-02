# Resolve bin — viral hydrilla lead-in (Claude studio pass, 2026-08-31)

**ffmpeg is the preview. Resolve is the finisher.** The mp4 in `preview/` is a
proof of the cut, not the deliverable. Conform in Resolve when Nate signs the
picture.

⚠️ `resolve/viral-leadin/` (no suffix) belongs to a **second writer** that was
building the same piece in the same directory at 20:34–20:36 on 2026-08-31.
Different plates, different builder. Do not mix the two bins. See BOARD.md.

## The cut

15.00s · 1080x1920 · 30fps · h264 CRF 18 · faststart · **silent, no audio track**

| # | in–out | plate | sha256 (first 12) | mode | move | strap |
|---|--------|-------|-------------------|------|------|-------|
| 1 | 0.00–3.40 | `@hydrilla_under_dock` | `f730acf1ac49` | bleed | push 1.000→1.075 | THIS IS UNDER / YOUR DOCK. |
| 2 | 3.07–7.27 | `@hydrilla_submerged_bed` | `924c9e39682b` | bleed | pull 1.090→1.000 | TEN YEARS. / YOU'VE NEVER SEEN IT. |
| 3 | 6.93–11.13 | `@truxors_pair_working` | `c6b6853c038a` | **fit** | vertical pan, zoom pinned 1.000 | TWO TRUXORS. / PROJECTED 10–12 FT. / *NOTHING IS OFFICIAL YET* |
| 4 | 10.80–15.00 | `@truxor_hauled_windrow` | `cd351a221a00` | bleed | push 1.020→1.085 | SCRAPE. HAUL. STAPLE. / *LAKE AUSTIN IS OUR HOME WATER* / 254-780-6971 |

Dissolves: 0.33s (10 frames) between every beat. Straps fade in over 0.35s and
are locked — they do **not** ride the Ken Burns move.

Copper (`#E8B070`) carries the hedge and the location line. Cream (`#F4EFE6`)
carries the claim and the phone.

## Conform notes for Resolve

- Stills in `stills/` are the ungraded Poseidon originals at native resolution.
  The grade applied by the builder is a lift, not a look:
  b/c/sat = `1.26/1.14/1.18` (1) · `1.03/1.06/1.08` (2) · `1.02/1.05/1.06` (3) ·
  `1.08/1.07/1.06` (4). Replace with the ATX_GRADE arc in Resolve.
- **Shot 3 is FIT (letterboxed) and that is not a style choice.** `c6b6853c038a`
  is 1080x810 native — a 9:16 cover-crop clips the second Truxor out of frame
  and breaks claim **C7** (must show two machines *and* the amphibious
  undercarriage). The builder pre-crops it to 4:5, verified by eye that both
  machines survive, then pins zoom at 1.000 so nothing can walk out during the
  move. **If you reframe this shot in Resolve, re-verify the count.**
- Type is Arial Bold because ffmpeg is a preview. Do a real font pass in Resolve.
- No audio. Master ships silent; see the VO script in BOARD.md — it is written
  and unread, and it is not to be muxed until Victoria approves the words.

## Excluded plates

| Plate | Why |
|---|---|
| `@two_machines` `1334bce67b99` | Single yellow knuckleboom excavator on a floating barge. Not two, not amphibious. Hard **C7** fail. Caption and eyeball agree. |
| `@dock_lowwater` | Mythology tier — never captioned as fleet proof. |
| `@bulkhead_undercut` | Nate rejected it as the "never seen it" plate. |
| `4e23ecccd59f` `@hydrilla_cove_carpet` | Runner-up hook. Good weed carpet, but a white pickup and a house crowd the frame and the weed reads as surface mat, not "under your dock." |
| `5e7f6f6bd182` | Two Truxors, but *loaded on a barge* — staged, not working. |
| `fd49bf6ffe3e` | Two Truxors staged on a ramp. Real and C7-clean; working beats staged, so it is the fallback if Nate wants a cleaner count read. |

## Claim ledger bindings

`../../MEDIA_ClaimLedger_Drawdown_v1.md`

- **C3** — beat 2. Ten-year window. Source does not hedge, asset does not hedge.
- **C7** — beat 3. Two amphibious machines. Frame shows two Truxors, one cutting
  and one at the bank, pontoon decks visible.
- **C2** — beat 3. "PROJECTED" retained verbatim.
- **C1** — beat 3. Drawdown is exploratory. Hedged **on the same plate**
  ("NOTHING IS OFFICIAL YET"), not deferred to an end card.
- **C11** — beat 4. Reads as Lake Austin, and says so.

Stripped per Nate 2026-08-31: **$695, credited, assessment, "walk yours",
"I'll tell you to your face."** This is a lead-in, not a Priority Assessment ad.
