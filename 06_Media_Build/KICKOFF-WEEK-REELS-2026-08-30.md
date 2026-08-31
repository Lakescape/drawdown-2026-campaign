# Claude Code kickoff — week of short drawdown pieces

**Paste the block at the bottom into a fresh Claude Code session.**
**Workdir:** `~/drawdown-2026-campaign` (open `06_Media_Build/`).
**This week’s dump:** `weeks/CURRENT` → `weeks/2026-08-31/BOARD.md` (rotates Mondays).
**Date:** 2026-08-30. Owner: Nate. Hermes already cut the 16s lead-in — do not redo it.

---

## Direction (why this week exists)

We are in **close week**, not awareness week. Tyler 1pm and the rest of the book are work bids. Public posts still sell the **$695 Priority Assessment** and the **window**, not a named lot and not a CY lump.

The 77s Truxor cut proved the craft: Ken Burns over **real Poseidon stills**, 9:16, cards on picture, no generated geometry. It failed as a lead-in because it was a film. Hermes trimmed it to 16s silent. Now fill the rest of week-1 like the locked 8-reel scripts — **12s, one idea, one CTA**.

Voice: calm authority. BBQ test. $5M homeowner test. Hedge in the same breath as the claim.

## Week board (build these, in order)

| Day | Asset | Script | What Claude does | Done when |
|-----|--------|--------|------------------|-----------|
| 0 | Lead-in 16s | trim | **Already on disk.** Caption in Command Center. | Nate watches; Hallie can pack |
| 1 | Honest Math | 06 | Type-only 12s. Paper/cream. `$695` → credited → 12 mo → `[X] slots` placeholder. **No AI, no footage.** | mp4 + 4 frames |
| 2 | Exposed Truth | 01 | 12s Ken Burns, REAL-ONLY Poseidon plates. Hook: *10 years of high water hid this.* End: `$695 Assessment. 100% credited.` | sha-pinned shot list + silent mp4 |
| 3 | Fleet still | — | Do not animate. Caption for LinkedIn (Nate voice). File already at `~/drawdown-sprint/dcc-close-book/public/media/fleet.jpg` | caption + pack path |
| 4 | Under the dock | 04 | Only if audit finds a real bulkhead/sediment plate. Else stop and say so. | silent 11s or a written skip |

**Do not start this week:** generated Meet-the-Machine (02), generated Two-Machines (05), Neighbor (07) without a real west-side booking, the `AI生成` vision clip, Resolve brand-font pass unless Nate asks after silent cuts exist.

## Prompt flow (how to work with Claude)

One session = one row. Do not stack 01+06+04 in one chat.

```
1. READ     studio gate law + KICKOFF-NEXT-SESSION.md + claim ledger + the one script
2. AUDIT    Poseidon stills (captions, not tags). Log machine count / type / Lake Austin?
3. LOCK     overlay lines vs ledger. Stopwatch. Silent first.
4. COMPOSE  reuse compose.py (bleed vs fit). New filter graph, new slug.
5. RENDER   9:16 1080x1920, silent, faststart, CRF 19 master.
6. QC       extract t=1, mid, end. Reject if card contradicts frame.
7. DESK     copy mp4 → dcc-close-book/public/media/ + mediaDesk.ts row (status: draft)
8. STOP     show Nate 4 frames + duration. Silent cut = Gate 3 draft, not a final.
            Nothing publishes without Nate's logged Gate 3 + Routing Gate PASS.
            No post. No Vercel ship.
```

If Claude wants to “improve” photography with a generator: **no**. If it wants a 45s or 77s cut: **no**. If VO wants to say the drawdown *is happening*: **no**.

## Copy-paste — start Claude here

```
You are in ~/drawdown-2026-campaign/06_Media_Build.

There is no CLAUDE.md in this folder. Studio gate law governs — read first:
- ~/InsightEngineMacOSPRO/ATX-Media-Mogul/STUDIO-WORKFLOWS.md   (the five gates)
- ~/InsightEngineMacOSPRO/ATX-Media-Mogul/lore/canon/HIGGSFIELD-LEARNINGS.md  (Rule 11)
- ~/drawdown-2026-campaign/KICKOFF-NEXT-SESSION.md   (this campaign's standing rules)
Then:
- MEDIA_ClaimLedger_Drawdown_v1.md
- REVIEW/GROK_MEDIA_VideoScripts_8Reels_v2_DRAFT.md (Script 06 only for this session)
Do NOT read MEDIA_Production_Process_v1_2026-08-03.md as process — superseded 2026-08-04.
Do NOT write a parallel process doc.
- compose.py header (Ken Burns over real Poseidon stills — that is the craft)

Context: Hermes already cut a silent 16s lead-in from DRAWDOWN_Truxor_916_FINAL.mp4
(hydrilla → projected 10–12 ft → iron → $695). Do not recut it.

This session: build Script 06 “The Honest Math” (~12s, typography only, no footage, no AI).
9:16, 1080x1920, silent. Paper/cream. Lines in order:
  $695.
  100% credited toward any work.
  Valid 12 months. Written scope. Reserved slot.
  As of [Mon/Thu]’s count: [X] slots remain.
Keep [X] as a visible placeholder — do not invent a slot count.
Hedge nothing here; these lines are unhedged in the ledger (C9). Do not add “drawdown is happening.”

Reuse brand colors from compose.py (cream / copper). Prefer Arial for now — fonts are a later Resolve pass. Legible over the card, not copper-on-bright-water.

Deliver: DRAWDOWN_Math_916_FINAL.mp4 in this folder, 4 extracted frames, duration, and the exact overlay strings. Do not copy to Vercel. Do not mark posted. Do not commit unless I say.

If anything in the ledger or script conflicts, stop and ask. One piece only.
```

Next sessions: same block, swap “Script 06” for **01** then **04**. For 01/04, add: *audit Poseidon by caption; pin sha256; bleed/fit per compose.py; two-machine claims need two amphibious machines in frame.*
