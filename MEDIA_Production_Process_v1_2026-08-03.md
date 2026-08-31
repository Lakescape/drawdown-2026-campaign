# Media Production Process v1 — ATX / IE video + still assets

Written 2026-08-03 after a freeballed DRAWDOWN highlight cut exposed the gaps.
Owner: Nate. Applies to every client- or market-facing video and still.

> ⚠️ **SUPERSEDED 2026-08-04 — not process. Do not put this on a reading list.**
> Studio gate law governs every ATX/IE asset:
> `~/InsightEngineMacOSPRO/ATX-Media-Mogul/STUDIO-WORKFLOWS.md` (five gates),
> `doctrine/pillar-gate-checklist.md` (Gate 0), `pipeline/gates-sop.md`.
> This file duplicated gate law that already existed. It is kept **only** for the
> four documented defect post-mortems in §1 — read those, follow the gates.
> See `KICKOFF-NEXT-SESSION.md` ("Do not write a parallel process doc").

---

## 1. What actually went wrong (evidence, not vibes)

Four defects in one 76-second cut. Each was caught only *after* render, by
sampling frames — none by design.

| # | Defect | Root cause |
|---|---|---|
| 1 | VO ran 20s against a 15s spec | No script lock. Copy written and voiced in the same step. |
| 2 | Brand copper on cream sublines illegible over bright water/sand | No legibility spec. Brand color used without a contrast check against actual plates. |
| 3 | VO asserted the drawdown as fact; the source one-pager hedges it | No claim ledger. Copy written from memory of the source, not against it. |
| 4 | "2 MACHINES" card over a frame showing **three** machines | **No footage audit.** Clips were treated as interchangeable B-roll without logging what is actually in frame. |

**Defect 4 is the real one.** 1–3 are process misses that a checklist fixes.
4 says we cut a sales claim against footage nobody had watched shot-by-shot.

## 2. The deeper problem: the footage isn't ours

The DRAWDOWN clips are **generated stock**, not ATX field footage. Consequences:

- Machines are not consistently amphibious — the equipment the offer is built on.
- The opening shot reads cold/northern, not Central Texas.
- No ATX branding, no ATX crew, no Lake Austin landmark anyone recognizes.
- Machine count, machine type, and shoreline character vary shot to shot.

We are selling *"we committed two amphibious machines and this is our home
water."* Generic lake footage undercuts that claim every time it's on screen.

**Standing rule: a claim about ATX's equipment, crew, or lake must be carried by
ATX's own footage.** Generated media is legal for mood, texture, and abstraction
— never for depicting our capacity, our machines, or our jobs.

The unlock is already available: ATX has ~2,300 clients of Jobber job photos.
Image-to-video animates a real dock, real crew, real Lake Austin. That path
produces better assets than any prompt, and it is defensible.

## 3. The gates

No step starts until the prior gate is signed off. Gates 1–4 cost nothing.

### Gate 1 — Claim ledger (before any copy)
Every on-screen or spoken claim gets a row. No row, no claim.

| Claim | Exact source | Hedged in source? | Carried by |
|---|---|---|---|
| 10–12 ft over 6–8 weeks | one-pager ¶2 | yes — "exploring" | card + VO |
| 30–40% less on dry ground | one-pager, Why-the-window | no | card + VO |
| 2 amphibious machines, ~25 working days | one-pager, Capacity | no | card + VO |
| $695, 100% credited, 12-mo validity | one-pager, Priority Assessment | no | card + VO |

If the source hedges, **the asset hedges in the same breath** — not in a
disclaimer at the end.

### Gate 2 — Footage audit (before any cut)
Every candidate clip logged before it can be used:

`id · duration · what is literally in frame · machine type · machine count · reads as Lake Austin? · usable for which claims · reject reason`

A clip with a moving subject gets **entry and exit noted** — that is exactly what
the 3-machines defect was. Audit the timeline of the shot, not one thumbnail.

### Gate 3 — Script lock
Copy approved as text, read aloud against a stopwatch, and checked against the
claim ledger. **Then** voiced. VO duration is an output, never a target to hit
after the fact.

### Gate 4 — Shot list
Every beat mapped: `time · clip id · in/out · claim on screen · why this shot carries this claim`.
The Gate 2 audit must confirm the frame does not contradict the card. Signed off
before a single render.

### Gate 5 — Render
Master at CRF 19. Delivery at CRF 23, ≤6 Mbps, faststart.

### Gate 6 — QC (frame-sampled, mandatory)
- Sample **≥3 frames inside every card window** — start, middle, end. One frame is not coverage.
- Text-vs-frame contradiction check (counts, equipment type, season, location).
- Legibility at phone size: view the frame at 25% and read the smallest line.
- Contrast: no brand color used on text without checking it over the actual plate.
- Audio: no clipped head or tail; VO ends before the video fade.

## 4. Credit policy

- Anything over **500 credits** in one call stops and asks. (Video ran 1,500/clip.)
- Prefer image-to-video from a real ATX photo over text-to-video from a prompt —
  cheaper, and it depicts something true.
- Log spend per asset. Today's four assets cost ~760 credits, ~4,500 declined.

## 5. What this replaces

Generate → look → patch → look → patch. That loop found real defects, but it
finds them after spend and after the asset exists, which is the expensive place
to find them. Gates 1–4 are free.
