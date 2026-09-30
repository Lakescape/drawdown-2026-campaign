# Closeout — Comfy CLI + Turnkey recut

**Date:** 2026-09-09 (work started 2026-09-07)
**Sessions:** `20260907_140924_7b83fa` (this desk) · `20260907_145230_83e616` (studio)
**State:** IN-FLIGHT

## Landed

- Comfy CLI **1.20.0** (`pip --user`), OAuth to `cloud.comfy.org`, skills installed (`comfy`, `comfy-debug`, `comfy-relay`, `comfy-director`, `comfy-build`, `comfy-deploy`).
- Binary: `~/Library/Python/3.14/bin/comfy` — not on default PATH until that dir is exported.
- Kickoff rewritten to sit **on** the studio pipeline: `KICKOFF-COMFY-TYPECARDS-2026-09-07.md` (do not Ideogram-replace Poseidon plates).
- Turnkey recut on disk: `DRAWDOWN_Turnkey_916_SUNO_BED.mp4` (~18s), desk `public/media/turnkey-studio.mp4`.
  - Pickup `c30cdc0fe978` **banned**.
  - Haul 1: `83f97f1642cd` bleed ax=0.90 — LOAD TRAIL + barge. Strap `OFF THE BARGE.`
  - Haul 2: `5e85f06eda86` packed bed. Strap `INTO THE TRAILER.`
- QC packet for Claude: `weeks/2026-08-31/HERMES_QC_TURNKEY.md` + `CLAUDE_PROMPT_TURNKEY_QC.txt`. BOARD appended.

## Uncommitted / not posted

Kitchen mp4s are gitignored (correct). Builder + kickoff + QC markdown sit dirty in `06_Media_Build/` — keep. Nothing published.

## Blocked on

- **Claude GATE3** — `GATE3_TURNKEY.md` was never written. `claude --bg` returned idle (`2d0e05b1`). Nate must `claude attach` and paste the prompt.
- **Comfy generate** — HTTP **402**, wallet **$0.00**. No pixels. Billing: https://cloud.comfy.org/billing
- Dual Hermes on `build_turnkey.py` — stopped after Nate called it.

## Next action

Nate: `cd ~/drawdown-2026-campaign/06_Media_Build && claude attach 2d0e05b1` then paste `CLAUDE_PROMPT_TURNKEY_QC.txt`. One stamp. No second Hermes recut.

## Do NOT repeat

- Two Hermes chats editing the same `build_*.py`.
- Cream Ideogram cards for a cut that already has Poseidon plates.
- `claude --bg "long prompt"` and assuming it ran — it can sit idle.
- t2v of Truxor / mat / barge we already shot.
- $695 on a viral/turnkey reel.
- Pickup-bed plate as “haul off.”

## ROI (this session `7b83fa`)

Hermes meter: `grok-4.6` / `xai-oauth`. `estimated_cost_usd=0`, `actual_cost_usd` unknown (SuperGrok included — cash outlay **$0**). Comfy spend **$0** (402).

List-price shadow (xAI grok-4.6: $2/M in, $0.50/M cached, $6/M out; reasoning counted as out):

| | Input | Cached | Output+reason | List $ |
|--|------:|-------:|--------------:|-------:|
| This desk `7b83fa` | 2.02M | 21.4M | 0.10M | **$15.37** |
| Studio twin `83e616` | 2.44M | 14.3M | 0.08M | **$12.53** |
| Combined | | | | **~$28** |

~90% of the list-price is **cached input** (AGENTS.md + Comfy skill dump + dual chats rereading the same kitchen). Cash is $0 on SuperGrok; the waste is tokens, not a card charge.

**What $15 of attention bought:** CLI installed, one honest 402, Turnkey haul that actually shows the Load Trail, a lock so Claude stamps instead of a third recut.

**What it did not buy:** a posted reel, Comfy stills, GATE3.
