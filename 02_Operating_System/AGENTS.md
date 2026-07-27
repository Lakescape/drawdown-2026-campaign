---
world: atx-lakescapes
para: project
status: active
sensitivity: internal
canonical: true
project: drawdown-2026
updated: 2026-07-24
---

# AGENTS.md — DRAWDOWN 2026 (Kimi + Grok working agreement)

## SYSTEM OF RECORD (updated 2026-07-24 21:05 — overrides anything conflicting below)

**Slack = the sales board.** The living pipeline — leads, replies, assessments booked, deposits, daily counts — is worked in Slack channels. This is where reps live during the window.
**Linear = the record keeper.** Task ledger + build log of everything agents create (deliverables, briefs, syncs). If it was made or decided, it gets a Linear issue. Linear is the audit trail, not the sales floor.
- **Google Drive** = files and briefs only (scripts, social drafts, deliverables, logs). Drive never holds task status.
- **Asana** = optional company-wide mirror, LATER. Sync engine stays disabled until after the first wave of Assessments/deposits; then transports to Railway/Hermes.
- **NEXT_ACTIONS.md is DEPRECATED** — kept for history only.
- The `08_Agent_IO/` loop (kimi_inputs/outputs, grok_inputs/outputs) stays — it is a file lane, not a board.
- **Daily flow:** Slack activity (sends, replies, bookings, deposits) is logged to Linear same-day — Slack is the floor, Linear is the ledger. Setup spec: `SLACK_SALES_BOARD_SETUP.md` in this folder.

## Ground rules (both agents)

1. **Real numbers only.** Never invent scarcity: slot counts, machine-days, crew counts, booking counts come from the Mon/Thu published count (see NEXT_ACTIONS.md #6) or are written as [X] placeholders. This rule has already caught multiple violations — it is the campaign's core trust mechanism.
2. **Tone:** calm authority, local expertise, real scarcity. Never hype, never corporate. Tests: "Would Nathan say this at a BBQ?" / "Would a $5M homeowner read this?"
3. **Shoreline work only** — this is a contractor play, not an environmental pitch. Do not assert the drawdown "is happening"; use "lined up," "projected," "pointing to."
4. **Never claim competitor incapacity.** State what ATX has locked, not what others can't get.
5. **SMS copy must be GSM-7 safe** (no em dashes, smart quotes, emoji) and ≤160 chars rendered with worst-case fills. Em dashes force UCS-2 and split messages.
6. **Aesthetic:** Cormorant Garamond + Source Sans 3; #f7f5f0 / #c4923a / #1a1a1a. No gradients, no neon.

## Folder contract

- `07_Swarm_Deliverables_FINAL/` — board-reviewed, red-teamed FINAL files. Do not edit in place; new versions get new filenames (v2, v3…).
- `08_Agent_IO/kimi_inputs/` — briefs/context handed TO Kimi.
- `08_Agent_IO/kimi_outputs/` — drafts/data Kimi produces for review or for Grok to consume.
- `08_Agent_IO/grok_inputs/` — briefs/context handed TO Grok (e.g., social post generation briefs, approved angles, scarcity numbers of the day).
- `08_Agent_IO/grok_outputs/` — Grok's social drafts, saved here for QA before anything is scheduled.

## File naming

`[AGENT]_[TYPE]_[DESCRIPTION]_[vN]_[STATUS].md` — e.g. `GROK_SOCIAL_IGCarousel_Angle3_v1_DRAFT.md`, `KIMI_BRIEF_SocialWeek1_v1_FINAL.md`.
Status flow: DRAFT → BOARDREVIEW → FINAL. Nothing publishes from DRAFT.

## Handoff protocol (social posts)

1. Kimi writes the weekly social brief (angles, verified scarcity numbers, offer rules) → `grok_inputs/`.
2. Grok generates posts → saves to `grok_outputs/` with naming above.
3. QA pass (red team checklist: real numbers? GSM-7 if SMS-adjacent? BBQ test? no exclusivity claims?) → approved posts marked FINAL.
4. Only FINAL posts go to scheduling. Kanban/Asana card links the Drive file.

## Watch-outs

- .gdoc/.gsheet files in Drive are pointer files — agents reading via the local mount cannot open their contents; export to .md/.xlsx first.
- If Drive for desktop is set to "stream," a file may need to be opened once in Finder to hydrate before an agent can read it.
- Anything touching legal/financial/customer-private material goes to a review queue, not final storage (per 00_Command_Center/AI_AGENT_INDEX.md).
