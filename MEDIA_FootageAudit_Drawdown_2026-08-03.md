# Gate 2 — Footage Audit: DRAWDOWN clip pack

Audited 2026-08-03. Every clip sampled at 4 points across its full 8s run
(frames 24/72/120/168), not one thumbnail. Source:
`~/Poseidon/projects/2026-07-27_atx_drawdown_reels/shots/`

## Verdicts

| Clip | What is literally in frame | Machine type | Count | Reads Lake Austin? | Verdict |
|---|---|---|---|---|---|
| S2-01 | Excavator climbing muddy bank, boulder, brown water, **leafless trees** | conventional steel track | 1 | ❌ northern, early spring | **REJECT** for C7/C11; texture only |
| S2-02 | Extreme CU track shoe compressing mud | conventional track shoe | 1 (partial) | ⚪ no location signal | texture only |
| S2-02-v2 | Same, tighter, yellow body visible | conventional track shoe | 1 (partial) | ⚪ no location signal | texture only |
| S2-03 | Excavator beside floating dock, teal water, **dry treeless hills** | conventional | 1 | ❌ western reservoir look | **REJECT**; also letterboxed frame 1 |
| S2-03-v2 | Excavator beside covered boathouse, green wooded hills, brown water | conventional | 1 | ✅ plausibly Hill Country | best location clip |
| S5-01 | Pull-back from one machine to a group | conventional (wide shoe) | **1 → 3 → 2** | ✅ plausible | usable ONLY at clip t≥5.5s |
| S5-02 | Cold blue-grey shoreline, coiled rope on mats, bare treeline | none | 0 | ❌ clearly northern, late fall | **REJECT** — was the v1 opener |

## The blocking finding

**Zero of seven clips show amphibious or pontoon undercarriage.** Every machine
in the pack is a conventional steel-track excavator.

Claim C7 — *"two amphibious machines… equipment that can work the soft lake bed
where conventional machines can't go"* — is the offer's entire differentiator,
and this footage actively contradicts it. A waterfront owner who knows equipment
sees conventional tracks and concludes the capacity story is marketing.

Secondary: only 2 of 7 clips plausibly read Central Texas. Claim C11 ("our home
water") is unsupported, and the v1 opener contradicted it outright.

**Conclusion: this clip pack cannot carry this offer. Not fixable in the edit.**

---

# ADDENDUM 2026-08-04 — the earlier "no real footage" verdict was WRONG

I searched Drive and iCloud and concluded no ATX amphibious media existed. I had
not searched `~/Poseidon/visual-library`. It does exist, and it is substantial.

## The archive

`~/Poseidon/visual-library/library.db` — 7,198 photos, 3,632 embedded (SigLIP
1152-dim), 3,619 VLM captions, 38,450 tags, plus `subject_final` labels and 41
human ground-truth rows. Photos stored by sha256 under `photos/`. Semantic
search is available; caption text search is faster for most lookups.

Subject distribution (top): `weed_hydrilla` 928 · `boat_lift` 406 ·
`dock_repair` 272 · `dock_build` 267 · **`truxor` 240** · `depth_measurement` 210
· `shoreline_restoration` 207 · `boathouse_covered` 145 · `dredging` 103 ·
`piling` 24.

⚠️ The taxonomy in `taxonomy.yaml` is built for the **lift-repair** domain — its
`equipment` facet has no excavator/amphibious labels at all. Searching by tag
finds nothing; searching **captions** finds everything. Anyone using this library
for marketing needs to know that.

## C7 is now supportable — the machine is the Truxor

203 photos carry "Truxor" in the caption. Reviewed 16 at full size:

- Blue/white **Truxor amphibious tool carrier, pontoon-tracked** — unmistakable, and
  exactly the "works soft lakebed where conventional machines can't" claim.
- **Frames with two Truxors together exist** — one in-canal working pair, one
  bank-staged pair with implements laid out. C7's *count* is satisfiable from a
  real frame.
- Setting reads unmistakably Central Texas — cypress, limestone, hill-country
  canals, residential Lake Austin docks. **C11 is satisfiable.**
- Also present: transport-on-trailer, detached implements, operator-at-controls,
  hydraulic arm close-ups, full deck loads of cut vegetation.

This also explains the `Taylor Slough / Equipment Photos` folder — white steel
fabrication, European setting. That is almost certainly Truxor/Dorotea factory
build documentation, not a field shoot.

**Revised verdict on C7: supportable from real photography. Blocking issue cleared.**

## What is still thin — and it is a scope problem, not a media problem

Reviewed 16 shoreline/dredging/piling frames. Honest read:

- Dominated by hydrilla mats, algae, cut-weed piles on lawns, muddy banks, one
  sediment pile. Documentation-grade, not marketing-grade.
- Several are **rotated/tilted** — EXIF orientation not normalized. Must be
  corrected before use, and it will cost some frames.
- One referenced file is missing from `photos/`.
- **Almost no bulkhead structure, tie-back, or undermined-piling imagery.**

The gap is the offer, not the archive. The library documents **weed removal and
dredging** — ATX's actual amphibious business. The drawdown one-pager sells
**bulkhead, sediment behind bulkhead, tie-back replacement, undermined dock
structure**. Those are different scopes with different pictures.

Two honest ways forward:

1. **Lean the video on what's proven** — soft-lakebed capability, sediment and
   dredging, the Truxor fleet. C5/C6 stay, but the "sediment removal behind a
   bulkhead" example carries the mechanism instead of tie-backs.
2. **Capture the structural scope** — a short list, but it must be shot.

## Open question for Nate — blocking Gate 4

**Are the "two amphibious machines committed for the window" the Truxors, or
amphibious excavators being brought in?**

If Truxors: C7 is fully covered by existing photography today.
If excavators: the count-and-equipment frame still has to be shot, and the
Truxor footage supports the capability claim but not that specific sentence.

I am not going to guess this one — it is the load-bearing sentence in the offer.

## Original search (Drive / iCloud) — kept for the record

| Location | Contents | Usable? |
|---|---|---|
| `Taylor Slough (VIP Shared)/Equipment Photos` (19 photos) | Fabrication/assembly of white steel lake-remediation apparatus + electrical control panels. Overseas setting — European signage, city skyline, block walls. | ❌ not the amphibious excavators |
| `Lake Remediation Pilot & Solution` | no image/video files | ❌ |
| `Tmp media video` | 3 photos, Quebec waterfront | ❌ |
| `03_Marketing_Media` (DRAWDOWN package) | one markdown calendar, no media | ❌ |

No footage of ATX's own amphibious machines exists in any searched local or
synced location.

## Capture list — what unblocks this

Phone video is fine. 4K if the phone offers it, **shot vertical**, locked off
(set it on the tailgate), 10–15s per shot, no narration needed.

| # | Shot | Carries | Why it must exist |
|---|---|---|---|
| 1 | Both machines side by side, wide, both fully in frame, nothing else | C7 | The count claim. One frame, two machines, no ambiguity. |
| 2 | Slow walk-around of one machine's **pontoon undercarriage** | C7 | The differentiator. This is the single most valuable shot on the list. |
| 3 | Machine moving across soft mud/lakebed where a conventional track would sink | C6, C7 | Proves the capability rather than asserting it. |
| 4 | Any recognizable Lake Austin marker — Pennybacker bridge, a known cove, hill-country limestone bluff | C11 | The location claim. |
| 5 | Bulkhead with the decade waterline stain, water below it | C2 | The "ten years underwater" hook. |
| 6 | Sediment/undercut behind a bulkhead, or an exposed dock piling base | C6 | The "not possible any other way" claim. |
| 7 | Nate, to camera, 20s, saying the hedge in his own words | C1, C4, C10 | A hedge from the owner's mouth beats any caption. |

Shots 1–3 are blocking. 4–7 raise it from adequate to good.

Once these exist, the generated clips are still useful — as texture between real
shots, never under an equipment or location claim.
