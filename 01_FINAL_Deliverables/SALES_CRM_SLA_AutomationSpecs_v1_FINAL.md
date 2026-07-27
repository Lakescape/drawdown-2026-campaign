# DRAWDOWN 2026 — CRM AUTOMATION + SLA SPECS
## Deliverable 3.2 — Trigger Map · 5-Minute SLA Automation · Tagging · Sequence Rules · Lead Scoring · Data Discipline · Railway/Mastra Implementation

Version: v1 FINAL
Date: 2026-07-27
Author: DRAWDOWN 2026 Swarm — Sales Engineer writer agent (6-layer pipeline complete: Draft → Skill Poll (6 roles) → Revision → Board Review → Devil's Advocate red team → Final)
Status: FINAL — Board approved with notes; internal devil's-advocate round (6 weaknesses) AND independent external red-team round (verdict REVISE, 7 findings incl. 1 near-blocker) fully applied per RECONCILIATION_Sheet_2026-07-27.md — see SALES_CRM_SLA_AutomationSpecs_v1_REVIEW_NOTES.md
Cited source of authority: **RECONCILIATION_Sheet_2026-07-27.md** (published 2026-07-27 — supersedes any conflicting line in this or any FINAL deliverable; settles after-hours hours, manual send ownership pre-L3, Sequence C manual operation, per-stage SLAs, and gate table)

---

## 0. SYSTEM OF RECORD MAP (READ BEFORE BUILDING ANYTHING)

| System | Role | What it owns | What automation may do |
|---|---|---|---|
| **Slack** | Sales floor | Working surface. `#drawdown-inbound` is where ALL replies land first. | Post cards, start/close SLA clocks, detect 👀 claims, escalate. Never drafts customer-facing copy. |
| **Linear** | Ledger | Single source of truth for lead state, tags, scores, and every event. Same-day by 6:00 PM CT. | Real-time writes for automated events; reminder cron for rep-logged events. |
| **Google Drive** | Files | Assessment reports, proposals, capacity model sheet. | Read references only; humans author files. |
| **GitHub — Lakescape/drawdown-2026-campaign** | Review bench | Versioned FINAL copy assets (SMS/email suites), specs, automation code. | Automation pulls FINAL assets from tagged releases only. |
| **Jobber** | Field CRM | Clients, jobs, scheduling once an assessment is booked. | Create draft client/job at Assessment Booked; ops confirms. |
| **Railway (Mastra agents + Inngest)** | Automation engine | Webhooks, crons, classification, SLA timers. | Everything in this spec. |
| **Asana** | PARKED | Post-campaign mirror only. | **Nothing. No automation writes to Asana during the campaign.** |

> *Provenance note: Jobber = field CRM from Nathan's production stack; not part of the campaign's approved ground-rule stack (Slack / Linear / Drive / GitHub) — listed for completeness.*

**Three laws that override every rule below:**

1. **Automation never invents a number.** No slot counts, no machine-days, no "X booked this week" in any automated payload. Live numbers are human-published (Mon/Thu counters) and human-quoted. Anything unknown is `[X]` and blocks the send.
2. **Only ONE fully automated customer-facing message exists:** the opt-out confirmation ("You're off the list. Sorry to bother you. Nathan" — 48 chars, GSM-7). Every other customer-facing send is either a scheduled FINAL asset with human gates, or a human typing.
3. **No automated message ever answers a reply.** Any human reply pauses that contact's sequences and routes to a human inside the 5-minute SLA.

---

## 1. TRIGGER DEFINITIONS (EVENT CATALOG)

All triggers fire through the automation engine (Railway). Each event carries an idempotency key (`source + external_id`) so retries never double-post, double-count, or double-send.

### T-01 — Inbound SMS reply (Twilio webhook → `POST /webhooks/twilio/sms`)

Classifier (Mastra triage agent, rules-first, LLM fallback) sorts the reply into exactly one class:

| Class | Examples | Automated action |
|---|---|---|
| `YES` | "YES", "yes", "interested", "tell me more" | Upsert lead in Linear → post card to `#drawdown-inbound` → **start 5-min SLA clock** → pause ALL sequences for this contact → set `engagement.replied_yes` (scoring, §5) |
| `QUESTION` | "how long does it take?" | Same as YES (reply routes to human per SMS Usage rule 3) → sequence pauses |
| `NO` | "no", "not interested" | Suppress sequences for contact, tag `sup:declined`, move card to CLOSED LOST / NURTURE, log to Linear. No SLA post. No reply text. The Script Branch 1F follow-up email is sent manually by the rep (no automation). |
| `OPT_OUT` | STOP, UNSUBSCRIBE, REMOVE, "take me off your list" in any wording | **Immediately send the single opt-out confirmation** (exact approved string, nothing else) → write permanent suppression (`sup:opt-out`) shared across SMS + email + 2027 lists → log to Linear. No SLA post, no further contact ever. |
| `OTHER` | Ambiguous | Treat as QUESTION (human decides). Err toward a human, never toward automation. |

### T-02 — Inbound email reply (Resend inbound webhook → `POST /webhooks/resend/inbound`)

- Any human reply → pause sequence → upsert lead → post to `#drawdown-inbound` → SLA clock.
- Auto-replies (OOO, bounce, list-unsubscribe headers) are filtered out before classification. A `List-Unsubscribe` / "unsubscribe" click maps to OPT_OUT handling (minus the SMS confirmation text; email suppression is silent, logged only).

### T-03 — Inbound call (Twilio voice webhook → `POST /webhooks/twilio/voice`)

- Answered call → rep logs outcome manually (Linear, same-day).
- Missed call / voicemail → transcription posted to `#drawdown-inbound` with SLA clock; callback assigned via claim.

### T-04 — Website chat message (chat platform webhook → `POST /webhooks/chat`)

- New message → upsert lead → post to `#drawdown-inbound` → SLA clock. Chat platform identity is a placeholder (§8) — the FAQ asset (`COPY_LiveChatFAQ_v1_FINAL.md`) arms the chat widget; a human answers inside the SLA.

### T-05 — Assessment booked (Calendly webhook OR rep action → `POST /webhooks/booking`)

1. Upsert lead → move card to **ASSESSMENT BOOKED** (pinned post 3).
2. Post to `#drawdown-won`: `📅 ASSESSMENT BOOKED — [Name] — [cove] — [source] — rep [initials]` (no invented numbers; the booking itself is the news).
3. Counter update: `assessments_booked +1` in the derivation store (§6 — published Mon/Thu, not live-quoted).
4. Confirmation sequence fires: confirmation email (from FINAL assets) + 1:1 confirmation text **from the rep's number, human-approved** before queue.
5. Create **draft** client + job in Jobber (ops confirms before scheduling). Suppress from sequences A/B permanently.

### T-06 — Proposal / report sent (rep logs in Linear; report file lands in Drive)

- Card → **PROPOSAL SENT** (pinned post 5).
- Arms the Sequence C cadence anchors relative to **report delivery = Day 0**: C1 within 60 min of delivery (event-anchored, any day), C2 Day 3 10:15 AM, C3 Day 7 9:50 AM — weekend shift to Monday 10:00 AM for C2/C3 only (C1 exempt per suite rules).
- C2/C3 fire only if no response and no deposit; `[Finding]`, `[Second finding]`, `[Deposit]`, `[Date]` are human-filled from the client's actual file before the queue releases (§4, gate table).

### T-07 — Deposit received (payment webhook OR ops manual entry → `POST /webhooks/deposit`)

1. Post to `#drawdown-won`: `💰 DEPOSIT — [Name] — $[actual amount] — [package tier] — rep [initials]` (real amount from the payment record, never typed by automation).
2. **Capacity decrement:** machine-days reserved per the client's proposal are committed in the derivation store (§6). Ops Lead owns the math; automation only moves the number the ops capacity model (Drive sheet) says to move.
3. Card → **DEPOSIT RECEIVED (LOCKED)**. Sequence C stops. Contact fully suppressed from all campaign outreach.
4. **Anti-spoofing (W5):** signature verification is mandatory. Any deposit event without a valid processor signature — or any manual entry from a non-ops user ID — is **quarantined to `#drawdown-war-room` for human confirmation**. A quarantined event never posts to `#drawdown-won` and never decrements capacity until a human clears it.

### T-08 — Kill-switch (manual, Nathan only — slash command or admin button)

- Activating the switch **halts every sequence immediately** (all queued sends cancelled within one sweep cycle, ≤60 s).
- Queues the approved pivot assets (SMS pivot text, 148 chars; email pivot per suite Usage rule 8) for **human review**, then batch-send inside legal send windows. Detection of a window shift is a human judgment — automation never self-triggers the kill-switch.

### Idempotency + dedupe rules

- Key: `{channel}:{external_message_id}`. Twilio `MessageSid`, Resend `message_id`, Slack `event_id`, Calendly `event_uuid`.
- A second inbound from the same contact inside 10 minutes **threads onto the existing SLA card** — it does not start a second clock or double-post.
- Every automation run writes a Linear event the moment it completes (§6). If the Linear write fails, the run is retried 3× then alerted to `#drawdown-war-room` — a send without a ledger entry is treated as a failed send.

---

## 2. THE 5-MINUTE SLA AUTOMATION

### State machine

```
UNCLAIMED --(👀 by rostered rep)--> CLAIMED --(rep resolves)--> RESOLVED
    |                                 |
    |--(T+5m)--> ESCALATED_5          |--(T+15m still open)--> FOLLOWUP_NUDGE
    |--(T+15m)--> ESCALATED_15        
    |--(T+60m)--> SLA_INCIDENT        
```

### Claim detection

- Source: Slack Events API `reaction_added` on the SLA card in `#drawdown-inbound`.
- A claim is valid only if: (a) the emoji is `👀` (`eyes`), (b) the reacting user ID is in the **rep roster** (Harper, Lucas, the 4 sales reps, Nathan) — bot reactions never count, (c) it is the first valid reaction on that card.
- On valid claim the bot threads: `Claimed by @[rep] at [HH:MM CT] — SLA [MET by X:XX / MISSED by X:XX]`. Subsequent 👀 reactions are ignored (no re-claim gaming).

### Escalation ladder (clock running, still unclaimed)

| Time | Action |
|---|---|
| T+5 min | DM Nathan + reply in card thread: `@nathan — unclaimed inbound, 5 min`. Tag `SLA_BREACH_5` in Linear. **This is the contractual SLA from the Slack board spec — non-negotiable.** |
| T+15 min | Post to `#drawdown-war-room`: unclaimed inbound + card link; page Harper/Lucas as backup triage; second DM to Nathan. |
| T+60 min | Declare **SLA INCIDENT**: war-room incident post, auto-added to next 8:00 AM standup agenda, Nathan reassigns the lead manually. Logged as `sla_incident` event in Linear. |

### Monitoring — heartbeat (failure detection)

- `fn.heartbeat` (§7) posts a **webhooks-alive check to `#drawdown-war-room` every morning before 10:00 AM CT**, ahead of the day's first send window. A silent morning (no heartbeat, or any endpoint reporting down) **blocks that day's batch release at the human gate** — the list-owning rep does not release a blast until replies are confirmed landing in `#drawdown-inbound`. This is the standing mitigation for a silently dead webhook endpoint on a blast day.

### After-hours rule

- **SLA business hours: Mon–Fri, 9:00 AM–6:00 PM CT** (decided — reconciliation sheet (b)).
- Inbound outside those hours is **captured immediately** (lead upserted, card posted to `#drawdown-inbound`, tagged `AFTER_HOURS`) but the SLA clock is **held** and arms at **9:00 AM the next business day**. Saturday/Sunday inbounds arm Monday 9:00 AM. There is no auto-acknowledgment text.
- **Never auto-text at night:** no automated outbound of any kind between 6:00 PM and 9:00 AM CT, ever. Sole exception: the opt-out confirmation, which sends immediately at any hour because honoring an opt-out is a compliance duty, not marketing.

### SLA metrics (derived, not live-quoted)

- `% claimed < 5 min` per rep per week; median claim time; incident count. Working-assumption target: **≥95% claimed inside 5 min** (uncalibrated — first two weeks set the real baseline).

---

## 3. TAGGING LOGIC

Linear is the only writer of record. Slack cards mirror a subset (`src`, `geo`, `pri`, next action) in the pinned-post card format: `Name — cove/street — source — last touch date — next action — rep initials`.

| Namespace | Values | Set by |
|---|---|---|
| `src:` | `warm` (past client), `cold`, `referral`, `paid`, `organic`, `hoa` | Import list on load; `referral` requires the referrer's name in the record |
| `stage:` | `new-warm-lead`, `contacted`, `assessment-booked`, `assessment-completed`, `proposal-sent`, `deposit-received`, `scheduled-for-drawdown`, `closed-lost-nurture` (8 stages per Master Plan; Slack board collapses to 7 pinned posts — `scheduled-for-drawdown` rides on the DEPOSIT RECEIVED post) | Automation on T-05/T-06/T-07; reps otherwise |
| `geo:` | Cove / street, normalized free text (e.g., `geo:wichita-falls-cove`); lake segment fallback | Rep at first touch; drives P1–P4 property signals |
| `pri:` | `P1`–`P4` job potential (§5): P1 = high-ticket signals (known failing structure, high-value cove, referral of a past high-ticket client); P2 = mid-size likely; P3 = assessment-likely; P4 = weak/unknown | Scoring model proposes; rep confirms at first touch. Automation never finalizes `pri:` alone. |
| `sup:` | `opt-out` (permanent, cross-channel, survives into 2027 lists), `do-not-contact` (Nathan-only, stronger than opt-out — includes no calls/no door hangers), `declined` (said NO, nurture-eligible after the window), `kill-switch-pivot-sent` | Opt-out automation; DNC is manual |
| `seq:` | Last asset sent per channel, e.g. `seq:sms-a3`, `seq:email-b2` | Automation, on every send |

**Suppression is checked before every single send** — a suppressed contact cannot receive any asset from any sequence, and the check runs at send time, not queue time.

---

## 4. SEQUENCE RULES — WHAT FIRES WHICH ASSET

Assets are pulled from GitHub (`Lakescape/drawdown-2026-campaign`, tagged `v1-FINAL`) — never edited in the sending tool. SMS re-validated for GSM-7 at queue time; any rep rewrite is typed into the platform and re-validated before queueing (SMS Usage rule 2).

**Ownership note (reconciliation sheet — Day-1 manual operations):** every scheduled send Jul 27–Aug 13 in the table below is performed **manually by the list-owning rep** (backup: Nathan) until L3 — see §7 "Pre-L3 manual send ownership." The Inngest scheduler rows describe the end-state automation for future/event-driven sends; during Jul 27–Aug 13 the "Human gate" column IS the mechanism.

| Automation | Fires | Source asset | Human gate before release |
|---|---|---|---|
| Inngest sequence scheduler | SMS A1–A5 (Jul 27, Jul 31, Aug 3, Aug 7, Aug 13 — per FINAL calendar) | `COPY_SMS_SequenceSuite_v1_FINAL.md` | A3: equipment status = target case (2 machines locked, ~25 days) verified morning-of. Batches of 40–50, staggered, inside 9:30–11:30 AM / 4:30–5:30 PM windows. |
| Inngest sequence scheduler | SMS B1–B4 (Jul 27, Aug 3, Aug 7, Aug 13) | same | B1: 10DLC approved + documented consent basis per number (Usage rule 1). B3: machine holds actually signed. |
| Inngest sequence scheduler | Email A1–A5, B1–B4 (per FINAL calendar; A4 conditional, A2 truth-floor) | `COPY_EmailSequenceSuite_v1_FINAL.md` | A2: Thursday standup count ≥5 booked past-client assessments, else A2 ALT. A4: past-client wave genuinely filled, else A4 ALT after sales lead confirms cutoff. Batches 40–50, weekdays 9 AM–6 PM, Monday ≥10 AM. |
| Event engine (T-06) | SMS + Email C1–C3 (Day 0 / 3 / 7, weekend shift for C2/C3) | both suites, Sequence C | `[Finding]`/`[Second finding]`/`[Deposit]`/`[Date]` filled by rep/Closer from the client's actual file. C3's "another client is waiting" must be literally true or the sentence is cut. |
| T-05 | Booking confirmation email + rep 1:1 text | FINAL confirmation assets | Rep approves the text before queue. |
| Opt-out automation (T-01/T-02) | Opt-out confirmation SMS only | Approved 48-char string | None — fires immediately, no gate. |
| Kill-switch (T-08) | Pivot SMS + pivot email | Approved pivot assets | Nathan reviews the queue, then release inside send windows. |

### NEVER automated (hard list)

1. **Calls.** No auto-dialer, no AI voice. Humans dial.
2. **Proposals.** Drafted by humans from `COPY_ProposalTemplate_v1_FINAL.md`, sent by humans.
3. **Voicemail drops.** Manual, per the voicemail scripts.
4. **Anything quoting live numbers.** Mon/Thu counters are human-published; any `[X]` in an asset is human-filled at send time from that morning's published count. Automation carries zero numeric scarcity claims.
5. **Answering replies.** Any reply → human inside the SLA.
6. **Referral-credit mentions pre-window.** The $500 referral program launches in October; no pre-window asset mentions it (Email Usage rule 7).
7. **Asana writes.** Parked until post-campaign mirror.

---

## 5. LEAD SCORING + DEAD-LEAD DETECTION

### Scoring model (simple, additive, explainable — weights UNCALIBRATED, first two weeks calibrate)

`Score = Source (0–30) + Engagement (0–40) + Property signals (0–30)` → 0–100

| Component | Signal | Points (working assumption) |
|---|---|---|
| Source | warm past client / referral / HOA / organic / paid / cold | 30 / 28 / 20 / 15 / 12 / 8 |
| Engagement | replied YES; replied with question; answered a call; opened email (cap 10); clicked (cap 5) | 25 / 20 / 15 / 1 each / 2 each |
| Property | known failing bulkhead or past repair; high-value cove (ops list); visible sediment/dock damage from photos or past job file | 15 / 8 / 7 |

- `pri:` mapping (working assumption): P1 ≥ 75 · P2 55–74 · P3 35–54 · P4 < 35.
- Score recomputes on every event. Every factor is visible on the lead record — a rep can always answer "why is this a P1?" in one sentence. No black-box scoring.
- Suppressed contacts are unscored and excluded from every list.

### Dead-lead detection

- **Dead** = full sequence completed (A5/B4 or final C3) with no reply, OR 10 days silence on an engaged lead per the Week-2 cadence rule.
- Dead leads move to the **nurture pool** (`stage:closed-lost-nurture`, card to pinned post 7). No further chasing.
- **60-day re-blast gate (pending Nathan confirmation at the Aug 5 standup — not yet policy):** if confirmed, the nurture pool may not be re-blasted for 60 days from last touch. Until confirmed, no re-blast of the nurture pool is scheduled at all; if the gate is approved, a re-blast would additionally require: fresh consent-basis check, new creative (never re-send the old sequence verbatim), and sales-lead approval. Opt-outs and DNCs are never in the nurture pool — they are permanently out.

---

## 6. DATA DISCIPLINE

1. **Same-day ledger.** Every automated event writes to Linear in real time. Every manual rep activity (sends, replies worked, objections heard, bookings, deposits) is logged by **6:00 PM CT** — an Inngest cron at 5:45 PM posts each rep's unlogged gaps to `#drawdown-war-room`. No logging = it didn't happen (Slack board hard rule 4).
2. **Mon/Thu counter derivation** (Harper + Lucas publish, Ops Lead owns the math):
   - `ASSESSMENTS BOOKED` = count of leads at stage ≥ `assessment-booked`, minus cancellations.
   - `MACHINE-DAYS` = from the ops capacity model (Drive sheet; floor 1 machine/20 days, target 2/25, stretch 3/30 — whichever case is real).
   - `SLOTS REMAINING` = capacity machine-days − committed machine-days (booked assessments + deposited jobs).
   - Automation computes the **draft** derivation Mon/Thu 7:45 AM CT and posts it to Harper/Lucas as a DM; humans verify against the Drive sheet and update the pinned counter in `#drawdown-war-room`. The pin — not the database — is what reps may quote (Slack board hard rule 1).
   - **Fallback:** if draft counters aren't human-verified by the 8:00 AM standup, the standup reads the previous pin and states so explicitly; the pin updates after verification, never before.
3. **No invented scarcity, enforced three ways:** (a) automation payloads contain no numeric scarcity fields at all; (b) `[X]` placeholders block the send until human-filled from the published count; (c) any asset text quoting a number must match the current pin or the queue refuses release. The retired "47 machine-days / 31 spoken for" line is hard-blocked in the asset linter.

---

## 7. IMPLEMENTATION — RAILWAY / MASTRA + INNGEST (LOCAL-FIRST)

No Zapier, no n8n. All glue is Inngest functions + Mastra agents in the campaign repo, transportable to the VPS unchanged.

### Services (all on Railway)

| Service | Purpose |
|---|---|
| `drawdown-api` | Webhook receiver + signature verification + event normalizer |
| `drawdown-db` | Postgres (event store, idempotency keys, sequence state, SLA timers) |
| `drawdown-agents` | Mastra agents: `triage-classifier` (reply classes, §1), `sla-watcher` (state machine, §2) |
| `inngest` | Function runner + cron schedules |

### Webhook endpoints

| Endpoint | Source | Verification |
|---|---|---|
| `POST /webhooks/twilio/sms` | Twilio inbound SMS | `X-Twilio-Signature` |
| `POST /webhooks/twilio/voice` | Twilio voice / voicemail transcription | `X-Twilio-Signature` |
| `POST /webhooks/resend/inbound` | Resend inbound email | svix signature |
| `POST /webhooks/chat` | Website chat platform (TBD — §8) | platform secret |
| `POST /webhooks/booking` | Calendly | webhook signing key |
| `POST /webhooks/deposit` | Payment processor / ops manual | processor signature |
| `POST /webhooks/slack/events` | Slack Events API (`reaction_added`) | Slack signing secret |

### Inngest functions

| Function | Trigger | Job |
|---|---|---|
| `fn.inbound-triage` | event: `inbound.*` | Classify → upsert → post → arm SLA |
| `fn.sla-sweep` | cron `* * * * *` (every 60 s) | Advance SLA state machine; fire 5/15/60 escalations; honor after-hours hold |
| `fn.heartbeat` | cron `50 9 * * *` (9:50 AM CT daily) | Webhooks-alive check on every endpoint (Twilio SMS/voice, Resend, Slack events, chat, booking, deposit) → post result to `#drawdown-war-room` before the 10:00 AM send window; a silent morning blocks that day's batch release at the human gate |
| `fn.after-hours-release` | cron `0 9 * * 1-5` (9:00 AM CT weekdays) | Arm clocks for `AFTER_HOURS` cards |
| `fn.sequence-scheduler` | cron, post-L3 future/event-driven sends only (the Jul 27–Aug 13 FINAL calendar is fully manual — see "Pre-L3 manual send ownership") | Queue next batch (40–50) of due assets; suppression check; GSM-7 check; gate check |
| `fn.sequence-c-engine` | event: `report.delivered` | C1 within 60 min; schedule C2/C3 with weekend shift |
| `fn.counter-derivation` | cron `45 7 * * 1,4` (Mon/Thu 7:45 AM CT) | Draft counters → DM Harper/Lucas |
| `fn.linear-reminder` | cron `45 17 * * 1-5` (5:45 PM CT) | Post unlogged gaps to war-room |
| `fn.jobber-sync` | event: `assessment.booked` | Create draft client/job in Jobber |
| `fn.kill-switch` | manual (Nathan) | Cancel all queued sends ≤60 s; queue pivot assets for review |

### Pre-L3 manual send ownership (reconciliation sheet — Day-1 manual operations)

**Until the Railway/Inngest scheduler is live (L3, mid-Aug), every scheduled send in the FINAL calendar — Jul 27 through Aug 13 — is sent MANUALLY.** No automation sends any blast in this window.

- **What is manual:** SMS A1–A5 and B1–B4; email waves A and B; and every Sequence C touch (C1 ≤60 min after report delivery / C2 Day 3 / C3 Day 7 — Sequence C is FINAL in both suites and fires manually per reconciliation sheet (c); the Rulebook's Day 2/4/7 phone-call cadence complements the C texts, it does not replace them).
- **Who sends:** the **list-owning rep** sends each asset from the SMS/email platform at the scheduled time. **Backup: Nathan.**
- **Same gates apply, human-enforced:** 10DLC approval + documented consent basis before Sequence B; suppression check at send time; A2 truth-floor (≥5 booked past-client assessments at the Thursday standup, else A2 ALT); A4 conditional on a genuinely filled past-client wave; equipment-status verification before A3/B3; `[X]` counts hand-filled from the published Mon/Thu pin; GSM-7 validation before every text queues; batch sizes of 40–50, staggered, inside the legal send windows.
- **First-hour watch:** a human watches `#drawdown-inbound` for the first hour after every blast — no exceptions, starting with the Jul 27 10:00 AM A1/B1 wave (standup agenda item, Jul 27).
- **What this means for L3:** the full FINAL calendar ends **Aug 13** (SMS A5/B4; email B4 was Aug 11; A5 email is event-anchored to window close). By the time L3 lands (Aug 15+), **"remaining sends" = none**. L3 therefore arms **future/event-driven automation only**: Sequence C engine for new report deliveries, inbound triage + SLA, heartbeat, counters, kill-switch — never a retroactive calendar blast. A5 (post-window email) is queued manually when the actual window close is known, or by the scheduler if L3 is live and stable by then.

### Local-first build path (build here, transport to VPS)

- **L0 (Jul 27–Aug 1):** Repo scaffold in `Lakescape/drawdown-2026-campaign`: webhook receivers with signature verification, Postgres via Docker, Inngest dev server, Slack app in test workspace. Fake-webhook fixtures for every trigger. Nothing touches production numbers.
- **L1 (Aug 1–Aug 7):** Triage classifier + SLA state machine against fixtures; Slack app installed in the real workspace (read-only first, then post to a private `#drawdown-inbound-test`). `slack_bot_token`, Twilio, Resend, Linear keys in `.env` locally.
- **L2 (Aug 8–Aug 14):** Cut `#drawdown-inbound` to live webhooks behind feature flags (SMS first, then email, then voice/chat). Shadow mode 48 h: automation posts to test channel while humans run the floor; compare.
- **L3 (Aug 15+):** Full live. Note: the FINAL send calendar ends Aug 13, so there are **no remaining calendar sends to arm** — L3 arms future/event-driven automation only (Sequence C engine for new report deliveries, inbound triage + SLA, heartbeat, counters; see "Pre-L3 manual send ownership" above). Deploy to Railway from the same repo (`railway up` / GitHub-linked deploy); the local-first config maps 1:1 to Railway env vars — no code changes, matching the local-first → VPS transport decision.
- **L4 (post-campaign):** Asana mirror + 2027 nurture handoff.

### Failure modes

- Webhook retries: idempotency keys absorb them; classifier is deterministic on keywords (STOP/YES/NO) with LLM fallback only for `OTHER` — and `OTHER` always errs toward a human.
- Silent webhook death: `fn.heartbeat` posts a webhooks-alive check to `#drawdown-war-room` every morning before 10:00 AM CT; a silent morning blocks that day's batch release at the human gate (no blast ships until inbound is confirmed live).
- Slack/Linear/Twilio outage: events buffer in Postgres, replay in order on recovery; SLA clocks pause during a detected Slack outage (can't claim what you can't see).
- Asset linter runs in CI on the repo: blocks smart quotes (GSM-7), blocked phrases ("47 machine-days"), unhedged drawdown claims ("is happening" → must be "projected/lined up/exploring").

---

## 8. PLACEHOLDERS TO FILL

| Placeholder | Needed for | Owner | Due |
|---|---|---|---|
| `slack_bot_token` + Slack app scopes (`reactions:read`, `chat:write`, channels) | All Slack automation | Operations Lead | Aug 1 |
| Twilio 10DLC approval status + documented consent basis for B-list | Sequence B, T-01 | Nathan / Ops | **before Jul 27** |
| Linear API key + custom fields (`src/stage/geo/pri/sup/seq`) | All ledger writes | Operations Lead | Aug 3 |
| Website chat platform identity + webhook secret | T-04 | Operations Lead | Aug 8 |
| Calendly webhook signing key (per-rep links) | T-05 | Operations Lead | Aug 5 |
| Deposit payment source (processor webhook vs. ops manual entry) | T-07 | Nathan | Aug 15 |
| Rep roster Slack user IDs (claim validation) | §2 claim detection | Operations Lead | Aug 1 |
| 60-day cold-list re-blast policy confirmation | §5 dead-lead gate (pending — not policy until confirmed) | Nathan, Aug 5 standup | Aug 5 |
| Lead-score weights + P1–P4 thresholds | §5 (UNCALIBRATED working assumptions) | Sales lead, after 2 weeks of data | Aug 14 |
| High-value cove list (property signals) | §5 scoring | Ops Lead | Aug 8 |
| Jobber API credentials + draft-job mapping | `fn.jobber-sync` | Operations Lead | Aug 15 |

---

*SALES_CRM_SLA_AutomationSpecs_v1_FINAL | ATX Lakescapes | Confidential — Internal Use Only*
*Pairs with: COPY_SMS_SequenceSuite_v1_FINAL.md, COPY_EmailSequenceSuite_v1_FINAL.md, SLACK_SALES_BOARD_SETUP.md, DRAWDOWN_2026_Master_Attack_Plan.md, RECONCILIATION_Sheet_2026-07-27.md. Per-stage SLAs govern per the Slack Board Rulebook (Deliverable 3.3, FINAL 2026-07-27) — reconciliation sheet (d); the interim 3-business-day touch rule is superseded.*
