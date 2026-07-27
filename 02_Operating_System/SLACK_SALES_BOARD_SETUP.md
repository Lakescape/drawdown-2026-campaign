---
world: atx-lakescapes
para: project
status: active
sensitivity: internal
canonical: true
project: drawdown-2026
updated: 2026-07-24
---

# SLACK SALES BOARD — Setup Spec

Slack is the sales floor. Linear is the ledger. This spec is the one-time setup; after this, reps run the day out of Slack and everything gets logged to Linear same-day.

## Channel structure (create once)

| Channel | Purpose | Who posts |
|---|---|---|
| `#drawdown-war-room` | Daily standup notes, decisions, Nathan announcements | Nathan, Ops Lead |
| `#drawdown-inbound` | Every inbound reply (SMS YES, email, call-back, chat) lands here FIRST. 5-minute SLA clock starts here. | SMS platform webhook / reps |
| `#drawdown-pipeline` | The board. One pinned post per stage, updated live (see below) | Reps update their own cards |
| `#drawdown-won` | Assessments booked, deposits received — with $ amounts. Morale + real-time capacity signal. | Anyone who books/collects |
| `#drawdown-ops` | Equipment status, crew scheduling, permit flags, weather | Ops Lead |
| `#drawdown-content` | Social drafts from `grok_outputs/` awaiting QA; approved posts get ✅ and a schedule date | Marketing + Nathan |

## The board itself (in `#drawdown-pipeline`)

Slack has no native kanban, so the board is **7 pinned posts, one per stage**, each a simple list reps edit:

1. NEW WARM LEAD
2. CONTACTED
3. ASSESSMENT BOOKED
4. ASSESSMENT COMPLETED
5. PROPOSAL SENT
6. DEPOSIT RECEIVED (LOCKED)
7. CLOSED LOST / NURTURE

Card format (one line per lead, rep edits the pinned post):
`Name — cove/street — source — last touch date — next action — rep initials`

Stage rules come from Deliverable 3.3 (Kanban spec) when produced: entry/exit criteria, SLA per stage, escalation path. Until then: a card may not sit in any stage more than 3 business days without a touch.

## Pinned counters (top of `#drawdown-war-room`, updated Mon + Thu)

```
ASSESSMENTS BOOKED: [X]   SLOTS REMAINING: [X]   MACHINE-DAYS: [X]
Last updated: [date] by [name]
These are the ONLY numbers reps may quote. If it's not on this pin, it doesn't exist.
```

## Daily cadence

- **8:00 AM** — standup (15 min, agenda in war-room). Yesterday's sends/replies/bookings, today's list assignments, number check.
- **During day** — replies land in `#drawdown-inbound`, claimed with a 👀 reaction, worked, moved through `#drawdown-pipeline`. Wins to `#drawdown-won`.
- **6:00 PM** — same-day log: every send, reply, objection, booking, deposit written into Linear (the ledger). No logging = it didn't happen.
- **Mon + Thu** — Harper/Lucas update the pinned counters.

## Automation hooks (when tokens exist)

- SMS platform → `#drawdown-inbound` webhook (reply YES triggers the 5-min SLA timer).
- Kimi morning briefing (8:17 AM cron, currently posts to conversation + Drive log) → also posts to `#drawdown-war-room` once `slack_bot_token` is configured.
- `#drawdown-won` deposits feed the capacity model — Ops Lead owns the math, never the reps.

## Hard rules

1. Reps quote only the pinned counters. (Real-numbers rule.)
2. A reply unclaimed for 5 minutes gets escalated to Nathan — the SLA is the campaign's edge.
3. Nothing customer-facing is drafted in Slack and sent directly — scripts come from `07_Swarm_Deliverables_FINAL/`, social from `08_Agent_IO/grok_outputs/` after QA.
4. Linear logging is same-day, every day. Slack is the floor; Linear is the proof.
