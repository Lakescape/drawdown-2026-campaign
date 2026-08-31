# Kickoff — next DRAWDOWN production session

Paste the block at the bottom into a new session. Everything above it is why.

---

## Read these first, in this order

1. `~/InsightEngineMacOSPRO/ATX-Media-Mogul/STUDIO-WORKFLOWS.md` — the five
   gates and the "WHICH PATH DO I USE?" table. **This is the system. Use it.**
2. `~/InsightEngineMacOSPRO/ATX-Media-Mogul/lore/canon/HIGGSFIELD-LEARNINGS.md`
   — 11 LOCKED rules. Rule 11 is about this exact campaign.
3. `~/InsightEngineMacOSPRO/ATX-Media-Mogul/doctrine/pillar-gate-checklist.md`
   — Gate 0. Six pillars, all must PASS, Nate signs.
4. `CLOSEOUT-2026-08-04-media-and-exposure.md` (this repo) — what exists.
5. `MEDIA_ClaimLedger_Drawdown_v1.md` — 11 claims mapped to one-pager lines.

## Working rules for this campaign

- **Studio gates govern.** `MEDIA_Production_Process_v1_2026-08-03.md` in this
  repo is superseded; it duplicated gate law that already existed.
- **Rule 11 is absolute.** Any shot whose value depends on ATX equipment is
  real footage or image-to-video from a real reference. Never text-to-video.
  Real photography exists — `~/Poseidon/visual-library`, 203 captioned Truxor
  frames, searchable by **caption** (the tag taxonomy has no equipment facet).
- **Brand law:** Cormorant Garamond + Source Sans 3,
  `#f7f5f0` / `#c4923a` / `#1a1a1a`. No gradients. From campaign `AGENTS.md`.
- **Hedge in the voice, not the caption.** The one-pager says "exploring" and
  "projected". So must the VO.
- **Sample the whole card window.** A single generated clip changed machine
  count 1 → 3 → 2 inside 8 seconds. One frame per card would have passed it.
- **Numbers come from the ledger or the exposure model.** Never from memory.

## The strongest material available

Verified against TWDB, not estimated:

- 2017: **492.04 ft → 481.69 ft**, floor **Jan 13**, refilled by **Feb 20**.
  **10.83 ft over ~7 weeks** — corroborates the one-pager's own projections.
- **559.4 acres** exposed lake-wide (TWDB table: 523.5).
- **720 residential lots**, median **10,625 sq ft** exposed; 70 lots over an acre.
- Zone spread: **N6 The Courtyard 88%** of its water surface, Laguna Loma 75%.

Re-run at any projected level:

```bash
cd ~/drawdown-2026-campaign/05_Lake_Austin_ShotPack_and_Ops/tools
python3 per_zone_exposure.py --floor 484 --pool 492.8
python3 per_lot_exposure.py  --floor 484 --pool 492.8
```

## Do not repeat

- Google Earth Pro scripted capture — opening a KML resets historical imagery
  to present day; frames come back current-year and look plausible.
- Chasing February 2017 aerials — the lake had already refilled.
- Manufacturer equipment photos — third-party copyright, not ATX machines.

---

## Paste this into the new session

```
DRAWDOWN 2026 production session.

Read first:
  ~/InsightEngineMacOSPRO/ATX-Media-Mogul/STUDIO-WORKFLOWS.md
  ~/InsightEngineMacOSPRO/ATX-Media-Mogul/lore/canon/HIGGSFIELD-LEARNINGS.md  (esp. Rule 11)
  ~/InsightEngineMacOSPRO/ATX-Media-Mogul/doctrine/pillar-gate-checklist.md
  ~/drawdown-2026-campaign/CLOSEOUT-2026-08-04-media-and-exposure.md
  ~/drawdown-2026-campaign/MEDIA_ClaimLedger_Drawdown_v1.md

Both repos live under /Users/austinlakescapes/ and are reachable by absolute
path from any session. No /add-dir needed (it does not exist in the desktop
app). If you want ATX-Media-Mogul to be the session's home, start the session
with that folder selected — the drawdown repo stays reachable either way.

Outcome for this session (one line): a Gate 0 pillar check for DRAWDOWN,
filled out and ready for my sign-off, with the concept built on the verified
exposure numbers rather than the generated clip pack.

Constraints:
- Studio gate law governs. Do not write a parallel process doc.
- Rule 11: equipment shots are real footage or i2v from a real reference.
- Brand: Cormorant Garamond + Source Sans 3, #f7f5f0 / #c4923a / #1a1a1a.
- Every number from the claim ledger or the exposure model. None from memory.
- Do not touch doctrine/ or pipeline/gates-sop.md — propose via
  learning/amendments/ only.

First thing I want to see: the Gate 0 scoresheet, six pillars, one line each.
```
