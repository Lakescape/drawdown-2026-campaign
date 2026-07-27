---
version: 1.0
date: 2026-07-27
author: DRAWDOWN 2026 Swarm — Team Onboarding Writer (Deliverable 5.3)
status: FINAL
pipeline: Draft → Skill Poll → Revision → Board Review → Red Team → Final (see REVIEW_NOTES)
governs: Role assignments for the 4-rep floor + Operations Lead, effective Day 1 (Mon Jul 27, 2026)
binding_sources: COPY_CallScript_Master_v1_FINAL · SALES_SlackBoard_Rulebook_v1_FINAL · RECONCILIATION_Sheet_2026-07-27 · TEAM_Kickoff_Rollout_2026-07-27
---

# DRAWDOWN 2026 — ROLE-SPECIFIC PLAYBOOKS
## Deliverable 5.3 — Hunter · Closer · Farmer · Operations Lead

**How to read this:** Your role is your center of gravity, not a cage. Everyone claims inbound in ≤5 minutes, everyone logs in Linear by 6 PM, everyone obeys the Ten Rules. Where two documents disagree, the Reconciliation Sheet wins. KPI figures marked **uncalibrated** are planning numbers — they get reset against real data at the Monday pipeline review; nobody is managed to an uncalibrated number in week one.

**The shared spine (all four roles):**
- Business hours 9:00 AM–6:00 PM CT, Mon–Fri. No outbound 6 PM–9 AM, ever. No weekend sends.
- Card format, all six fields: `Name — cove/street — source — last touch date — next action — rep initials`.
- Slack is the floor; Linear is the proof. No same-day log = it didn't happen.
- Quote only the pinned war-room counters, framed "as of [Monday/Thursday]'s count."
- The offer: $695 Assessment, 100% credited, 12-month validity. Collected AT BOOKING (payment link or logged 48-hour hold). "Pay on site" does not exist.
- Gates: 40 by Aug 31 · 60 by mid-Sep · **80 paid-or-held by Sep 30** · <60 on Sep 30 = DIAGNOSE.

---

## ROLE 1 — HUNTER
### Lead generation & cold outreach

**Role definition.** The Hunter owns the top of the board: Stage 1 (New Warm Lead) and the first conversation in Stage 2. You work the cold lists (public-records waterfront parcels), the B-wave SMS/email sends, and fresh list assignments read at standup. Your product is not appointments yet — it is **two-way conversations with the right lake owners**, run through Master Script Scenario 2. You are the campaign's first impression; sounding like you know their shoreline is the whole game.

**Daily routine.**
1. **8:00 AM standup** — take the day's list assignment; create Stage 1 cards same day, before the first send, all six fields filled.
2. **Power-dial block, 8:30–11:30** — first touches. Day-1 assignments are touched Day 1 (the scheduled SMS blast *is* the assignment touch — sent manually from the platform until automation L3, with 10DLC / suppression / A2 truth-floor gates checked before every send).
3. **Inbound rotation when assigned** — watch `#drawdown-inbound`; claim with 👀 inside 5 minutes; first working touch within 2 business hours of claim. A human watches the channel for the first hour after every blast.
4. **11:30–12:00 / 4:30–5:00** — board edits and card hygiene (quick single-line edits only during power-dial hours).
5. **Afternoon block** — second/third attempts on no-answers (voicemail VM1, then cadence), gatekeeper follow-ups (always book the Thursday callback), Stage 1 aging sweep — no card of yours sits 2 business days untouched.
6. **By 6:00 PM** — Linear: `lead_name, source, cove/street, assigned_date, first_touch_datetime, touch_channel, touch_outcome, after_hours_tag, rep`.

**Tools used.** Slack (`#drawdown-inbound`, `#drawdown-pipeline`, `#drawdown-war-room`) · Linear (same-day ledger) · SMS/email platform (manual sends until L3) · Calendly/CRM for bookings · Drive `07_Swarm_Deliverables_FINAL/` · the Desk Card (Deliverable 5.2) taped within reach.

**Targets / KPIs.**
- First touch on 100% of list assignments within 24 hours (binding SLA — Day-1 assignments Day 1).
- Inbound claims ≤5 minutes, 100% of the time (binding — this is the campaign's edge).
- Stage 1 cards never age past 2 business days untouched (binding SLA).
- Dials + first touches per day: **uncalibrated** — the Monday review sets the week's dialing plan against the gate curve; volume expectations are set in the room, not invented here.
- Stage 1→2 contact rate: tracked weekly; **uncalibrated** until 2 weeks of real data.

**Script pointers (use the FINALs — do not rewrite).**
- `COPY_CallScript_Master_v1_FINAL` — **Scenario 2 (Cold Lead)** is your home base: the "you can hang up on me" opener, Branch 2A (how did you get my number — "straight answer: property records"), Branch 2B (the one-sentence save + clean exit), Branch 2G (gatekeeper = a name plus a channel is a win), Branch 2C (hydrilla deflection), Branch 2E ("just send me information" → trade it for a Thursday call).
- `COPY_SMS_SequenceSuite` — B-wave texts, sent as written, never retyped outside the platform.
- `COPY_VoicemailScripts` — VM1 for no-answers; you speak as yourself ("[Your name] from Nathan's team").
- `COPY_ObjectionCheatSheet` — quick-scan index when a cold call goes sideways.
- `ASSET_OnePager_Summary_v1_FINAL` — the Branch 2E leave-behind; **production gate: QR link + Nathan's direct line must be filled before any send (Ops confirms).**

**Escalation paths.**
- Inbound unclaimed at 5 minutes → Nathan, directly in `#drawdown-inbound` (hard rule).
- Card aging past 2 business days → flagged by name at standup; you lose new-list assignments that day until the backlog clears.
- DNC on first touch → log immediately, Stage 7. DNC overrides every SLA. A DNC violation is a firing-level conversation.
- Structural emergency mentioned on any call → Nathan same day, regardless of window.
- Angry homeowner, press contact, any ask to bend the Ten Rules → Nathan, immediately.

---

## ROLE 2 — CLOSER
### Assessment follow-up, proposals & contracts

**Role definition.** The Closer owns the middle and bottom of the board: Stage 2 (Contacted) through Stage 6 (Deposit Received). You run the 48-hour engaged cadence, convert conversations into **paid-or-held bookings**, deliver scopes inside 3 business days, and work the two-track proposal cadence to a cleared 15–25% deposit. Your product is **revenue with clean paperwork** — a deposit that is cleared, a slot that is locked, a Linear record that proves all of it.

**Daily routine.**
1. **8:00 AM standup** — report yesterday's bookings/holds with payment status; confirm tomorrow's visits have 24-hour reminders queued.
2. **Morning block** — committed next touches first (a date promised to a homeowner outranks everything on your list), then 48-hour-cadence touches on every engaged Stage 2 card.
3. **Booking mechanics, every time:** specific date + time → $695 payment link paid *during the call* (or explicit logged 48-hour hold with expiry) → confirmation text with your direct number *before hangup* → `#drawdown-won` post with payment/hold status (no post, no count) → referral names logged immediately.
4. **Scope duty** — completed assessments (Stage 4) get their written prioritized scope + rough pricing **delivered within 3 business days**; findings summarized in Linear first; failing bulkheads / big sediment flagged to `#drawdown-ops` same day.
5. **Proposal cadence (Stage 5), two tracks, no channel doubling:** Sequence C texts — C1 ≤60 min after delivery, C2 Day 3, C3 Day 7 (sent **manually** from the platform until L3, FINAL copy as written) — plus your phone track: Day 2 check-in, Day 4 value call, Day 7 decision call with a direct ask.
6. **Deposit mechanics:** ask stated explicitly (typically $7,500 mid / $15,000 high; 15–25% range) → Stage 6 only when funds **clear** → `#drawdown-won` post **with the dollar amount** → personal welcome touch within 24 hours (business-hours rule; never automated) → Ops handoff within 2 business days.
7. **By 6:00 PM** — Linear per the Stage 2/3/5/6 field sets (`outcome, next_touch_date, hold_expiry, last_twoway_reply_date, payment_status, sequenceC_log, quoted_amount, deposit_ask, decision_date…`).

**Tools used.** Slack (`#drawdown-pipeline`, `#drawdown-won`, `#drawdown-war-room`, `#drawdown-ops` for findings flags) · Linear · SMS/email platform (manual Sequence C until L3) · payment link tooling · Calendly/CRM · proposal template in Drive · Desk Card.

**Targets / KPIs.**
- 100% of bookings paid-or-held at booking (binding — unpaid = not booked, never enters the gate count).
- 24-hour reminder on 100% of booked visits (binding; checked at standup).
- No-show rebooked within 1 business day (binding SLA).
- Scope delivered ≤3 business days, 100% (binding SLA — speed-to-scope is where conversion is won).
- Proposal→deposit conversion: planning floor **25%** — a conservative capacity-math floor per Reconciliation Sheet (e), reviewed weekly against actuals, **not a target**. Anything above floor is upside.
- Show rate (booked → attended): **uncalibrated** — target set after 2 weeks of real booking data; do not invent one.
- Personal gate contribution: **uncalibrated** — the 40/60/80 curve is a team number; individual booking quotas are set at the Monday review against the week's dialing plan.

**Script pointers (use the FINALs — do not rewrite).**
- `COPY_CallScript_Master_v1_FINAL` — the **Close** blocks in all four scenarios (always two options: Assessment or photo assessment); Branch 1D/1E (hold mechanics + booking confirmation); the **10-objection Rebuttal Library** — especially #1 (too expensive), #2 (think about it), #6 (competitor quoted less — arm them with the scope, never attack), #9 ($695 value), #10 (spouse → materials + 3-way call + hold date); **Hard Rule 7** escalation triggers.
- `COPY_SMS_SequenceSuite` + `COPY_EmailSequenceSuite` — **Sequence C** (C1/C2/C3), FINAL in both suites, used as written.
- `COPY_ProposalTemplate` — 3-tier, $695 credit line-itemed on every option; tiers $15–25K / $35–55K / $65–95K, typical ~$48K.
- `COPY_ObjectionCheatSheet` — desk-speed index to the same library.
- Desk Card (5.2) — commission quick-look: $50 booked-**and-attended**, $100 per proposal, 4–5% of closed work.

**Escalation paths.**
- Pricing negotiation on a full-cove/high-ticket prospect → Nathan immediately (he owns final closes). Card stays in stage with `ESCALATED TO NATHAN [date]`.
- "Another company quoted me less" on a high-ticket → Rebuttal 6 + flag Nathan same day (competitor intelligence feeds the risk register).
- Second no-show → Nathan decides personally whether to keep working it (capacity threat, treated as an ops problem).
- Scope undelivered at 3 business days → Ops Lead pinged; at 5 → Nathan takes the card personally.
- Any refund or scope-change request → Nathan same day. Never a rep decision, ever.
- Missed committed touch → standup flag; second consecutive miss → Ops Lead reassigns the card.

---

## ROLE 3 — FARMER
### Past clients, referrals & HOA / multi-property

**Role definition.** The Farmer owns the relationships that compound: the past-client list (highest-conversion source in the campaign), referral leads, HOA/multi-property threads, and the Stage 7 nurture pen. You run Master Script Scenarios 1, 3, and 4. Your product is **trust converted into bookings today and referral inventory for October** — you protect the relationship above any single sale, because past clients are the referral engine for the next decade.

**Daily routine.**
1. **8:00 AM standup** — take the day's past-client/referral assignments; verify CRM history before every dial (what we did, when — if you don't know their history, you are not ready to dial; referrer booking status verified before every referral call).
2. **Morning block** — past-client calls (Scenario 1): the 90-second neighbor opener, real listen, 48-hour hold mechanics, **never pressure a past client past one hold + one callback**.
3. **Referral calls (Scenario 3)** — confirm exactly what the referrer said; never exaggerate involvement (they will check); offer same-route grouping in the referrer's cove; **text the referrer thanks the same day** — referrals compound when acknowledged.
4. **Referral embargo discipline (binding until Oct 15):** log referral names now, tell the homeowner "our program launches in October — I'll note your neighbor now so you're first in line." The $500 credit is never quoted before launch. Use `COPY_ReferralScripts` **pre-launch version ONLY**.
5. **HOA threads (Scenario 4)** — board-packet-first offer; get on the next board agenda (that is the real close); separate individual lots from common shoreline as distinct scopes; put the permit timeline in writing for slow boards. **Never quote group terms, discount percentages, or minimum property counts on the phone — Nathan sets them in writing first (none exist yet).**
6. **Nurture duty (Stage 7)** — one Branch 1F email on clean declines; no calls for 10 days after a decline; reactivations rewritten as new cards tagged `reactivated` (silence clock restarts); 12-month credit holders get a manual 6-month check-in — log the date at entry.
7. **By 6:00 PM** — Linear per Stage 1/2/7 field sets (`lost_reason` picklist, `credit_expiry`, `reactivation_date`…).

**Tools used.** Slack (`#drawdown-pipeline`, `#drawdown-won`, `#drawdown-inbound`) · Linear · CRM property histories · SMS/email platform (manual sends until L3) · Drive assets · Desk Card.

**Targets / KPIs.**
- 100% of past-client calls made with verified CRM history (binding readiness rule).
- 100% of referral offers logged same-day (binding, Script Branch 1E).
- Referral thanks-text to referrer same day, 100% (binding).
- Zero embargo breaches: no $500 referral credit quoted before Oct 15 (binding).
- Zero group-terms quotes before Nathan's written terms (binding, Hard Rule 4).
- Past-client booking rate, referral→booking rate, nurture reactivation count: **uncalibrated** — tracked at the Monday review; no invented targets in week one. Note: past-client list is the highest-conversion source (campaign planning assumption — the ≥5-booked check at the Jul 30 standup gates the A2 vs A2 ALT email decision).

**Script pointers (use the FINALs — do not rewrite).**
- `COPY_CallScript_Master_v1_FINAL` — **Scenario 1 (Past Client)** incl. the "[X] bookings are real" conditional line and Branch 1F gracious exit; **Scenario 3 (Referral)** incl. Branch 3C (never invent a neighbor's story) and 3D (encourage them to verify you — strongest trust signal); **Scenario 4 (HOA)** incl. Branch 4B (packet before presentation), 4C (common shoreline as its own scope), 4D (get exact terms in writing — never ad-lib), 4E (written timeline for slow boards); Rebuttals 3 (insurance), 4 (HOA approval — the Assessment needs none), 5 (selling the property), 7 (not sure anything needs fixing).
- `COPY_ReferralScripts` — **pre-launch version only until Oct 15.**
- `ASSET_OnePager_Summary_v1_FINAL` — leave-behind, production gate applies (QR + Nathan's line, Ops confirms).
- `COPY_EmailSequenceSuite` — the Branch 1F nurture email is the ONLY nurture touch until a FINAL nurture sequence exists (open dependency — flagged to orchestrator).

**Escalation paths.**
- Any HOA group-terms ask → Nathan, in writing, before any HOA card enters Stage 5.
- Board wants a presentation → schedule it; Nathan looped in on high-value communities.
- Reactivated high-ticket lead out of Nurture → Nathan notified **at entry**, not at close.
- Structural emergency at any past-client or common-area property → Nathan same day + `#drawdown-ops` flag.
- DNC violation (yours or witnessed) → Nathan immediately; firing-level.
- Anyone angry, press contact, refund request → Nathan, immediately.

---

## ROLE 4 — OPERATIONS LEAD
### Equipment, crew, permits & scheduling

**Role definition.** The Operations Lead owns the physical truth of the campaign: 2 amphibious machines locked in July, ~25 productive days, 3 planned crews, the production calendar, the permit pipeline, and the capacity model that tells sales what it is allowed to sell. You run `#drawdown-ops`, take the Stage 6 handoff, and own every number sales may never touch. Your product is **a calendar that cannot be oversold and a window that cannot be missed.** Ops owns the math — never the reps.

**Daily routine.**
1. **8:00 AM standup** — confirm today's site visits have assessors assigned; flag any booking-to-visit gap problems; hear findings flags from the floor.
2. **Capacity model (continuous)** — deposits and expected packages vs. 2 machines / ~25 working days. Deposits are the ONLY legitimate "slots remaining" input. Update machine-days committed on every Stage 6 entry. Sales may never oversell the pinned counters — you are the backstop.
3. **Findings triage** — same-day review of `#drawdown-ops` flags from Stage 4 (failing bulkhead, structural emergency, large sediment volume); feed the capacity model; structural emergencies go to Nathan same-day regardless of window.
4. **Permits** — run the LCRA / City of Austin queue (2–6 weeks depending on work — the number the HOA script cites); single permit packages for grouped properties where the City allows; every Assessment scope carries permit guidance.
5. **Scheduling** — lock production slots on cleared deposits; confirm the Stage 6 handoff in `#drawdown-ops` within 2 business days; apply grouped-properties-first sequencing as the calendar fills (**policy confirmation pending — see Placeholders; until confirmed, sequencing preference is stated to reps as provisional**); second no-shows are treated as an operations problem — capacity math, not blame.
6. **Standup & review support** — Monday 8:30 AM pipeline review: present the capacity check (item 6 on the fixed agenda) and the rotating one-stage pre-review spot-check; Harper runs daily hygiene, Lucas backs up — you audit the auditors.
7. **By 6:00 PM** — Linear for every ops event: `assessor_assigned, slot_dates, ops_handoff_date`, permit submissions, equipment status.

**Tools used.** Slack (`#drawdown-ops`, `#drawdown-war-room`, `#drawdown-pipeline` read-only on card lines) · Linear · production calendar · permit portals (LCRA / City of Austin) · equipment vendor channels (O'Shea/Wilco holds) · capacity model sheet · CRM spec §8 (you own the Slack bot token + SMS webhook URL and the automation L3 scheduler build, mid-Aug).

**Targets / KPIs.**
- Ops handoff confirmed ≤2 business days from cleared deposit, 100% (binding SLA; you get pinged at 2, Nathan copied at 3).
- 24-hour reminder coverage on every booked visit (shared binding duty — checked at standup).
- Findings flags acknowledged same day, 100% (binding).
- Permit submissions inside scope-delivery week wherever the queue allows; permit lead time vs. the 2–6 week range tracked per job (**uncalibrated** — baseline being built this window).
- Machine-day utilization vs. the ~25-day plan: tracked weekly; utilization target **uncalibrated** until the first real scheduling data exists.
- Show-rate input: second no-shows converted to a scheduling policy decision within 1 week (process target).

**Script & document pointers (use the FINALs — do not rewrite).**
- `SALES_SlackBoard_Rulebook_v1_FINAL` — your governing document: Stage 3 (assessor assignment, reminders, no-show protocol), Stage 4 (findings flags, 3-day scope SLA), Stage 6 (handoff mechanics), Daily Board Hygiene, Monday review item 6, Card-Move Etiquette rule 5 (Linear restores — Harper/Lucas perform, you verify capacity-side).
- `COPY_CallScript_Master_v1_FINAL` — **know what reps are promising**: the scarcity language (2 machines, ~25 days, committed in July — the approved structural scarcity), Placeholder 7 (**grouped-jobs-first sequencing claim — you confirm the policy in writing before reps use it**), Hard Rule 7 (emergencies).
- `RECONCILIATION_Sheet_2026-07-27` — (a) paid-or-held counting, (e) gate math and the 25% planning floor your capacity model uses.
- `COPY_ProposalTemplate` — deposit structure 15–25% ($7,500 mid / $15,000 high) — the numbers your capacity model ingests.
- Deliverable 5.2 Desk Card — the live-count [X] boxes your Mon/Thu counter feeds supply.

**Escalation paths.**
- Structural emergency (from any source) → Nathan same day, regardless of window; site safety call is yours to make and defend.
- Capacity breach risk (deposits trending past machine-day supply) → Nathan at the **first** Monday review where the model shows it — never after the oversell.
- Handoff unconfirmed at 2 business days → you are the escalation recipient; at 3, Nathan is copied — fix it before 3.
- Equipment hold/deposit problems (O'Shea/Wilco) → Nathan immediately; the Jul 31 equipment hold deposit deadline is a campaign-critical date.
- Permit queue slippage threatening an October start → Nathan + the affected closer same day; HOA scopes get a written revised timeline (boards respond to documents).
- Any rep quoting unpinned capacity numbers → name-check at standup; repeat → Nathan.

---

## PLACEHOLDERS / OPEN DEPENDENCIES (binding — none may be improvised)

1. **HOA group terms** (discount structure, minimum property count) — Nathan, in writing, before any HOA card enters Stage 5. Until then: Farmer offers packet/presentation only.
2. **Grouped-jobs-first sequencing policy** — Operations Lead confirms in writing before reps use the priority claim (Call Script Placeholder 7).
3. **Referral program terms** — $500 credit embargoed until Oct 15; `COPY_ReferralScripts` pre-launch version only.
4. **Individual volume quotas** (dials/day, bookings/week per rep) — set at Monday pipeline reviews against the gate curve; deliberately **uncalibrated** here.
5. **Show-rate target** — after 2 weeks of real booking data; not invented.
6. **Priority scoring rubric** (Stage 4 high/mid/low) — Ops Lead publishes the written standard; working rubric until then.
7. **Nurture sequence asset (Stage 7)** — no FINAL exists; nurture is limited to the single Branch 1F email until one passes the swarm pipeline (flagged to orchestrator).
8. **One-pager production gate** — QR link + Nathan's direct line filled before first use; owner: Ops Lead.
9. **Rep initials roster** — Harper, by Jul 29; canonical initials on all cards.
10. **Automation L3 (Railway/Inngest, mid-Aug)** — until live, all waves and Sequence C fire manually; owner: Operations Lead.

---

*TEAM_RolePlaybooks_4Roles v1.0 FINAL | DRAWDOWN 2026 | ATX Lakescapes — Confidential, internal use only*
*Companion to TEAM_QuickReferenceCard_v1_FINAL (5.2). Role assignments effective Day 1: Monday, July 27, 2026. Where any line here disagrees with RECONCILIATION_Sheet_2026-07-27, the sheet wins.*
