---
version: 1.1
date: 2026-07-27
author: DRAWDOWN 2026 Swarm — Sales Engineering Agent (Deliverable 3.3)
status: FINAL
governs: SLACK_SALES_BOARD_SETUP.md (pinned-post board in #drawdown-pipeline)
reconciled_by: RECONCILIATION_Sheet_2026-07-27.md (published 2026-07-27 — supersedes any conflicting line in this document; external red-team round applied, see REVIEW_NOTES Layer 7)
---

# DRAWDOWN 2026 — SLACK BOARD RULEBOOK
## Deliverable 3.3 — Stage Definitions, SLAs, Automations & Board Rituals for the Pinned-Post Sales Board

**Day 1: Monday, July 27, 2026.**
**The board:** 7 pinned posts in `#drawdown-pipeline`, one per stage. There is no kanban software. Slack is the floor; Linear is the proof (6 PM same-day log rule).
**Card format (unchanged, mandatory, all six fields):**
`Name — cove/street — source — last touch date — next action — rep initials`

This rulebook supersedes the interim rule ("no card sits more than 3 business days without a touch") with per-stage SLAs below — confirmed by Reconciliation Sheet (d). Where a stage is silent, the 3-business-day interim rule still applies.

**Real-numbers rule (binding everywhere in this document):** Reps quote only the pinned counters in `#drawdown-war-room` (updated Mon + Thu by Harper/Lucas), always framed as "as of [Monday/Thursday]'s count." Window language is always hedged: "the City and LCRA are lining up," "projected October–November." We sell preparation, not prophecy.

**Automation caveat (binding):** Slack webhook/bot tokens and the Railway/Inngest scheduler (automation L3, mid-Aug) are not yet live. Every "automation rule" below names the manual owner who performs the action until the token exists. No SLA in this document depends on software that doesn't exist yet. All FINAL sequence assets (outreach waves A/B, Sequence C) fire **manually from the platform by the assigned rep** until L3 — see Reconciliation Sheet (c) and "Day-1 manual operations."

**After-hours rule (binding, Reconciliation Sheet b):** No automated outbound of any kind between 6:00 PM and 9:00 AM CT, ever (the compliance-required opt-out confirmation is the sole exception). After-hours replies are captured immediately, tagged AFTER_HOURS, and any SLA clock arms at 9:00 AM the next business day. **All SLA business hours in this document = 9:00 AM–6:00 PM CT, Mon–Fri.**

---

## STAGE 1 — NEW WARM LEAD

**What this stage is:** A name we are allowed to work but have not yet had a two-way conversation with. Two sources: (a) assigned warm/cold list leads, (b) inbound replies landing in `#drawdown-inbound`.

### Entry criteria (card moves IN when ALL are true)
- **Outbound-sourced:** Lead appears on the rep's list assignment read at that morning's 8:00 AM standup. Card created the same day, before the first send.
- **Inbound-sourced:** Reply (SMS YES, email, call-back, chat) has landed in `#drawdown-inbound` AND been claimed with a 👀 reaction. The claiming rep creates the card immediately — the 5-minute claim SLA clock started when the reply landed (or at 9:00 AM for AFTER_HOURS replies), not when the card was written.
- All six card fields are filled. "Next action" for a new card is always a first touch with a date (e.g., "SMS blast 7/27" or "call 7/28 AM"). A card with an empty next-action field is a format violation (see Daily Hygiene).

### Exit criteria (card moves OUT when ONE is true — owning rep moves it)
- **→ Stage 2 (Contacted):** A live two-way exchange has occurred — call answered and conversation held per the Master Call Script (any of the 4 scenarios), OR a genuine reply exchange by SMS/email. A sent SMS, a voicemail, or a delivered email does NOT count. "Contacted" means they talked back.
- **→ Stage 7 (Closed Lost/Nurture):** Wrong number / not waterfront / explicit Do-Not-Call on first touch attempt. Log DNC immediately — DNC overrides every SLA in this document.

### Automation rules
- **On entry (inbound):** SMS platform webhook posts the reply to `#drawdown-inbound`; 5-minute timer starts. *Manual fallback until token exists:* rep on inbound rotation watches the SMS platform inbox and posts the reply text into `#drawdown-inbound` themselves. A human watches `#drawdown-inbound` for the first hour after every blast (Reconciliation Sheet, Day-1 manual operations).
- **On entry (outbound):** Outreach waves (SMS A1–A5 / B1–B4, email waves A/B — FINAL assets) are sent **manually from the platform by the assigned rep at the scheduled time** until automation L3, with the standard gates (10DLC, suppression, A2 truth-floor). Backup: Nathan.
- **On exit → Stage 2:** No channel post. The move itself is the signal.
- **Sequence enrollment:** None at this stage beyond the outreach waves above and the Accelerated Outreach Sequence cadence assigned at standup (Week 1 saturation per Master Plan Part 3).

### SLA
- **Inbound:** 5 minutes to claim (hard rule — this is the campaign's edge), measured within SLA business hours (9 AM–6 PM Mon–Fri). After-hours replies are tagged AFTER_HOURS and the clock arms at 9:00 AM the next business day (Reconciliation Sheet b). First working touch within 2 business hours of claim.
- **Outbound:** First touch within 24 hours of list assignment (Day 1 assignments are touched Day 1 — the SMS blast is the assignment).
- **Aging:** Card may not sit in Stage 1 more than **2 business days** without a logged touch attempt (tighter than the 3-day interim rule — unworked new leads are the cheapest loss in the campaign).

### Escalation path
- Inbound unclaimed at 5 minutes → ping **Nathan** directly in `#drawdown-inbound` (hard rule #2 from setup spec).
- Card aging past 2 business days → flagged by name at next morning's standup; rep loses new-list assignments that day until the backlog is worked.

### Linear logging requirement (by 6:00 PM same day)
Fields: `lead_name` · `source` (list name or inbound channel) · `cove/street` · `assigned_date` · `first_touch_datetime` · `touch_channel` · `touch_outcome` (connected / voicemail / no-answer / DNC) · `after_hours_tag` (Y/N) · `rep`.

---

## STAGE 2 — CONTACTED

**What this stage is:** We've had a real conversation. Per the Master Call Script, every contact ends in exactly one of three outcomes: booked Assessment, scheduled next touch with a date, or a clean gracious exit. This stage holds the middle outcome.

### Entry criteria
- Two-way conversation completed and the outcome was **"scheduled next touch (with a date)"** — including 48-hour holds, spouse-callbacks, gatekeeper Thursday follow-ups, and "send the one-pager, call me Thursday" trades. The one-pager send uses ASSET_OnePager_Summary_v1_FINAL (QR link + Nathan's direct line filled per its production gate — see Placeholders).
- Card's "next action" field carries the committed date. "I'll follow up sometime" is a script violation, not a next action.

### Exit criteria (owning rep moves it)
- **→ Stage 3 (Assessment Booked):** Homeowner committed to a specific date + time AND the $695 is collected at booking (payment link, or an explicit logged 48-hour hold) AND the confirmation text was sent before hangup (Script Branch 1E, amended by Reconciliation Sheet a). **Unpaid and un-held = not booked.**
- **→ Stage 7 (Closed Lost/Nurture):** Clean decline (Script Branch 1F), OR 10 consecutive days of silence (clock defined under SLA below) despite the 48-hour cadence, OR DNC.
- **Escalation out (not a stage move):** Pricing negotiation on a full-cove prospect, an HOA requesting group terms, or any mention of a structural emergency → Nathan, same day (Script Hard Rule 7). The card stays in Stage 2 with "ESCALATED TO NATHAN [date]" in the next-action field until he hands it back.

### Automation rules
- **On exit → Stage 3:** Rep posts the booking to `#drawdown-won` with the assessment date and payment/hold status. This post is the trigger Harper/Lucas use for the Mon/Thu counter update — no post, no count.
- **Sequence enrollment:** None new beyond the campaign outreach waves (SMS/email waves A/B — FINAL, sent manually from the platform by the assigned rep until automation L3, per Reconciliation Sheet Day-1 manual operations). The 48-hour engaged cadence itself is rep-driven calls/texts per the Master Call Script (FINAL); no separate engaged-follow-up asset exists or is required.

### SLA
- **Touch cadence:** Every **2 business days** while engaged (the script's 48-hour rule), within business hours.
- **Silence limit — clock definition:** 10 **consecutive calendar days of silence, measured from the homeowner's last two-way reply. Our touches do not reset the clock.** When the clock completes, move to Stage 7 Nurture. Do not keep a silent card warm in Stage 2 to flatter the count.
- **Held slots:** A 48-hour hold that expires without payment or decision → one scheduled callback (per Script Rebuttal 2), then Nurture if no. The hold expiry is logged in Linear.

### Escalation path
- Missed committed next-touch date → flagged at standup same morning; the date was a promise to the homeowner.
- Second consecutive missed touch → Ops Lead reassigns the card at standup (initials change on the card; Linear note records the reassignment).

### Linear logging requirement
Fields: `contact_datetime` · `scenario_used` (1–4) · `objections_heard` (from the 10-objection library, verbatim tags) · `outcome` (booked / scheduled_next_touch / gracious_exit) · `next_touch_date` · `hold_expiry` (if any) · `last_twoway_reply_date` (drives the silence clock) · `escalation` (none / Nathan–pricing / Nathan–HOA / Nathan–emergency).

---

## STAGE 3 — ASSESSMENT BOOKED

**What this stage is:** A $695 Priority Assessment with a real date on the calendar and the money handled. **This is the gated number.** The assessment gates count only **paid-or-held** cards in this stage and beyond — unpaid = not booked (Reconciliation Sheet a).

### Entry criteria (ALL true)
- Specific date + time committed by the homeowner.
- **$695 collected AT BOOKING** — payment link paid during the call, OR an explicit 48-hour hold, logged with its expiry. "Pay on site" does not exist. A booking without payment or a logged hold is not a booking and does not enter this stage or the gate count.
- Confirmation text sent with the rep's direct number (Script Branch 1E) before the call ended.
- Booking posted to `#drawdown-won` (with payment/hold status).
- Referral names offered on the call logged immediately (Script Branch 1E).

### Exit criteria (owning rep moves it, except where noted)
- **→ Stage 4 (Assessment Completed):** Site visit performed and photo/video documentation captured. (The $695 is already collected — it was the entry gate.)
- **→ Stage 2 (Contacted):** No-show or reschedule request. Card moves BACK with next action "rebook by [date]." Also: a 48-hour hold that expires unpaid → card moves BACK to Stage 2 (it was never a paid booking). A backward move is normal and must never be hidden to protect the gate count — Harper/Lucas adjust the counter down on the next Mon/Thu update, and the Monday review tracks the show rate (uncalibrated working assumption: show-rate target to be set after 2 weeks of real data; do not invent one).
- **→ Stage 7:** Homeowner cancels and declines rebooking (credit validity 12 months noted in Linear; refund of a paid booking is Nathan's call, never the rep's).

### Automation rules
- **On entry:** `#drawdown-won` post (above). Harper/Lucas fold the booking into the pinned counters at the next Mon/Thu update: `ASSESSMENTS BOOKED: [X]   SLOTS REMAINING: [X]   MACHINE-DAYS: [X]`. Only paid-or-held bookings count.
- **Reminder:** Confirmation text at booking + reminder text 24 hours before the visit, both within business hours. *Manual fallback until tokens exist:* the owning rep sends both from their own number; the 24-hour reminder is checked at standup for tomorrow's visits.
- **Sequence enrollment:** None.

### SLA
- **Booking-to-visit gap:** Book within 10 business days wherever calendar allows; the script sells urgency and a 3-week-out booking contradicts it.
- **48-hour hold:** Expires unpaid → one callback, then Stage 2. Holds never count twice and never survive past expiry on the board.
- **24-hour reminder:** Mandatory; missing it is a hygiene violation.
- **No-show rebook:** Within **1 business day** of the missed visit.
- **Aging:** A card whose visit date has passed with no outcome logged by 6 PM that day is an automatic standup flag.

### Escalation path
- No-show not rebooked within 1 business day → standup flag + Nathan pinged if the lead is full-cove/high-ticket potential.
- Second no-show → Nathan decides personally whether to keep working it or move to Nurture. Chronic no-shows threaten the 2-machine / ~25-working-day capacity plan and are treated as an operations problem, not a rep problem.

### Linear logging requirement
Fields: `booking_datetime` · `visit_datetime` · `payment_status` (paid / hold_active w/ expiry — no other values exist) · `payment_method` (link / hold) · `confirmation_sent` (Y/N) · `reminder_24h_sent` (Y/N) · `assessor_assigned` · `outcome` (completed / no-show / rescheduled / cancelled / hold_expired) · `rebook_date` (if any).

---

## STAGE 4 — ASSESSMENT COMPLETED

**What this stage is:** We have their $695 (collected at booking), their documentation, and their truth. Now we owe them a written prioritized scope — fast.

### Entry criteria (ALL true)
- Site visit performed; photo/video documentation captured.
- Findings summarized in Linear (what must happen this window vs. what can wait).

### Exit criteria (owning rep moves it)
- **→ Stage 5 (Proposal/Scope Sent):** The written prioritized scope with rough order-of-magnitude pricing has been **delivered** to the homeowner (email or hand-delivery — sent, not drafted). Delivery starts the Sequence C clock (below).
- **→ Stage 7 (Closed Lost/Nurture):** Assessment-only outcome — shoreline sound, no work recommended. The rep must say so plainly (Script Rebuttal 9 integrity promise). Card moves to Nurture with the 12-month credit noted; this is a good outcome, not a failure, and reps are never penalized for it.

### Automation rules
- **On entry:** If findings show a failing bulkhead, structural emergency, or large sediment volume → rep flags `#drawdown-ops` same day. Ops Lead feeds this to the capacity model (Ops owns the math, never the reps). Structural emergencies are also flagged to Nathan same-day regardless of window (Script Hard Rule 7).
- **On exit → Stage 5:** No channel post; the scope document is attached to the Linear issue. Sequence C1 fires within 60 minutes of delivery (see Stage 5).
- **Sequence enrollment:** None at this stage.

### SLA
- **Scope delivery:** Within **3 business days** of the site visit (tighter than interim — speed-to-scope is where conversion is won; the homeowner is never hotter than the week after we walked their shoreline).
- **Aging:** 3 business days without scope sent → automatic flag.

### Escalation path
- Scope not delivered at 3 business days → Ops Lead pinged (scope writing is the bottleneck to watch) + flagged at standup.
- 5 business days → Nathan takes the card personally. A stale completed assessment is a refund request waiting to happen.

### Linear logging requirement
Fields: `visit_date` · `findings_summary` · `priority_score` (high/mid/low — uncalibrated working rubric until Ops publishes a scoring standard; do not invent thresholds) · `estimated_tier` (assessment-only / mid ~$48K / high ~$95K) · `scope_sent_date` · `documentation_link`.

---

## STAGE 5 — PROPOSAL / SCOPE SENT

**What this stage is:** The money conversation. Written scope and pricing are in the homeowner's hands; we are working toward the 15–25% deposit.

### Entry criteria
- Written prioritized scope + pricing delivered, with delivery date/time logged (this starts the Sequence C clock).
- Deposit ask stated explicitly (typically $7,500 mid-size / $15,000 high-ticket per the money model; 15–25% range).

### Exit criteria (owning rep moves it)
- **→ Stage 6 (Deposit Received):** Deposit funds **cleared** — not promised, not "check's in the mail," cleared.
- **→ Stage 7 (Closed Lost/Nurture):** Explicit decline, OR 10 consecutive days of silence (same clock definition as Stage 2: from the last two-way reply; our touches — calls or C texts — do not reset it) after the full two-track cadence below.

### Automation rules
- **On entry — two tracks fire; neither duplicates a channel (Reconciliation Sheet c):**
  - **Sequence C (SMS/email track — FINAL in both suites):** C1 within 60 minutes of scope/report delivery, C2 on Day 3, C3 on Day 7. Until automation L3 (Railway/Inngest scheduler, mid-Aug), **the owning rep sends each C touch MANUALLY from the SMS/email platform on schedule.** C touches are never improvised — the FINAL asset copy is used as written.
  - **Phone track (rep-driven calls):** Day 2 check-in call, Day 4 value call, Day 7 decision call. These PHONE CALLS complement the C texts — they do not replace them, and no rep text may double a C touch on the same channel and day.
- **On exit → Stage 6:** `#drawdown-won` post **with the deposit dollar amount** (real capacity signal, per setup spec). Harper/Lucas update counters at next Mon/Thu; Ops Lead updates machine-days committed.

### SLA
- **First follow-up:** Day 2 phone call after scope delivery (within business hours), alongside the C-text schedule above.
- **Cadence:** A phone touch every 2 business days; a direct decision ask on the Day 7 call.
- **Decision window:** 10 consecutive days of silence (clock per Stage 2 definition) after the full two-track cadence → Stage 7 Nurture. Do not leave zombie proposals in Stage 5 to pad the pipeline.

### Escalation path
- Any pricing negotiation on a full-cove prospect → Nathan immediately (he owns final closes).
- "Another company quoted me less" on a high-ticket → Script Rebuttal 6, and flag Nathan same day (competitor intelligence feeds the risk register).
- 10-day silence → move to Nurture, no escalation — this is routine.

### Linear logging requirement
Fields: `scope_sent_date` · `quoted_amount` · `tier` · `deposit_ask` · `sequenceC_log` (C1/C2/C3 sent dates, manual sender initials) · `followup_call_dates[]` · `objections_heard` · `decision_date` · `outcome` (deposit / declined / silent→nurture).

---

## STAGE 6 — DEPOSIT RECEIVED (LOCKED)

**What this stage is:** Terminal stage on the sales board. Money cleared, calendar slot locked. *Note:* the Master Plan lists an 8th kanban stage, "Scheduled for Drawdown" — that stage is owned by Operations and lives in `#drawdown-ops`, not on this 7-post sales board. The handoff below is the boundary.

### Entry criteria (ALL true)
- Deposit funds cleared (15–25% of package).
- Production calendar slot locked by Ops Lead.
- `#drawdown-won` post with $ amount published.

### Exit criteria
- **Off-board handoff:** Ops Lead confirms scheduling into the drawdown production calendar in `#drawdown-ops`. The card is then marked `HANDED TO OPS [date]` and left on the pinned post until the Monday review confirms the handoff, after which the line is removed. Sales no longer owns the card — but the homeowner relationship does not end; post-job review/referral asks are an Ops workflow, not this board.
- **Exception exit → Nathan:** Refund request or major scope change. Not a rep decision, ever.

### Automation rules
- **On entry:** `#drawdown-won` $ post (above); counters update Mon/Thu; Ops Lead updates the capacity model (2 machines locked, ~25 working days — deposits are the only legitimate "slots remaining" input).
- **Welcome touch:** Rep sends a personal confirmation/thank-you within 24 hours of cleared deposit, within business hours (if funds clear after 6 PM, the welcome touch fires at 9 AM the next business day). Manual, always — this one should never be automated.

### SLA
- **Welcome touch:** Within 24 hours of cleared funds, business-hours rule above.
- **Ops handoff:** Within **2 business days** of cleared funds.

### Escalation path
- Handoff not confirmed at 2 business days → Ops Lead pinged directly; Nathan copied at 3.
- Any refund/scope-change request → Nathan same day.

### Linear logging requirement
Fields: `deposit_amount` · `deposit_pct_of_package` · `date_cleared` · `payment_method` · `package_value` · `slot_dates` · `ops_handoff_date` · `welcome_touch_date`.

---

## STAGE 7 — CLOSED LOST / NURTURE

**What this stage is:** Not a graveyard — a holding pen with rules. Contains clean declines, 10-day silents, DNCs (flagged), expired holds, and sound-shoreline assessment-only completions. Nurture cards are the 2027+ pipeline and this fall's referral sources.

### Entry criteria (ONE true, always with a lost reason)
- Clean decline (Script Branch 1F) · 10-day silence from Stage 2 or 5 · DNC · assessment-only completion · expired 48-hour hold after the callback · second no-show decision by Nathan.

### Exit criteria (owning rep moves it — reactivation only)
- **→ Stage 2 (Contacted):** The homeowner reaches out or replies to a nurture touch. Card line is rewritten (not resurrected in place) with source tagged `reactivated` and the original lost reason preserved in Linear. A reactivated card re-enters the 2-business-day cadence immediately, and the silence clock restarts from the reactivation reply.

### Automation rules
- **On entry (decline path):** One follow-up email per Script Branch 1F ("no calls, just the occasional email"). The broader nurture sequence asset is **not FINAL** (see Placeholders) — until it is, nurture touches are limited to that single email plus the Monday/Thursday public slot-count content the homeowner may see.
- **No calls for 10 days** after a decline (script rule, binding).
- **DNC:** Honored immediately and permanently. No automation, no exception, no re-entry.

### SLA
- No touch SLA — this stage is intentionally low-frequency.
- **Audit:** Every Nurture card is eyeballed at the Monday pipeline review; anything older than 30 days with no reactivation signal drops to a quarterly check.
- **12-month credit holders** (assessment-only completions and cancellations) get a manual check-in at the 6-month mark — log the date now.

### Escalation path
- DNC violation by any rep → Nathan, immediately, and it's a firing-level conversation. Nothing in this campaign justifies burning the lake's phone list.
- Reactivated high-ticket lead → Nathan notified at entry, not at close.

### Linear logging requirement
Fields: `lost_reason` (picklist: price / timing / spouse-no-decision / competitor / no-need-sound-shoreline / DNC / silent / hold-expired / no-show×2) · `lost_date` · `nurture_enrolled` (Y/N) · `credit_expiry` (if applicable) · `reactivation_date` (if any).

---

## DAILY BOARD HYGIENE RITUAL

**Owner:** Harper (primary), Lucas (backup). Not optional, not delegable to a rep who "has time."

**When:** 4:45 PM daily, inside the reps' 4:30–5:00 pipeline-review block and before the 6:00 PM Linear cutoff.

**The 10-minute audit, every day:**
1. **Format sweep** — every card line on all 7 pinned posts has all six fields. Missing next-action or last-touch date → rep fixes before 6 PM.
2. **SLA sweep** — last-touch dates checked against the per-stage SLAs above (including silence-clock checks on Stage 2/5 cards against `last_twoway_reply_date`, and hold-expiry checks on Stage 3). Breaches get a ⚠️ reaction on a reply under the pinned post and a name-check at tomorrow's standup.
3. **Counter sanity** — `#drawdown-won` posts since the last counter update vs. the pinned counter number. Paid-or-held only. Discrepancies go to Harper/Lucas for the next Mon/Thu update.
4. **Linear cross-check** — every board move today has a matching Linear entry by 6 PM. **Slack is the floor; Linear is the proof. No logging = it didn't happen.**

**Monday pre-review spot-check:** Ops Lead audits one full stage (rotating) before the Monday review — a second pair of eyes on the person who audits everyone else.

---

## WEEKLY PIPELINE REVIEW — MONDAYS, 8:30 AM (after standup), `#drawdown-war-room`

**Owner:** Nathan. **Attendees:** all reps, Harper/Lucas, Ops Lead. **Length:** 30 minutes, standing.

**Measured against the gates (Reconciliation Sheet e — supersedes the older "40/60/80 by Aug 31/Sep 30/Oct 31" framing):**
- **Target: 80 paid-or-held assessments booked by Sep 30. DIAGNOSE floor: <60 by Sep 30 triggers the diagnosis protocol.**
- **Interim checkpoints: 40 by Aug 31; 60 by mid-September (exact date confirmed at the first Monday pipeline review).**

**The fixed agenda:**
1. **Gate position:** Paid-or-held bookings vs. the gate curve. Behind gate → the week is a dialing week, decided in the room, not discovered on Friday. **This review owns the week's dialing plan.**
2. **Friday funnel handoff:** The Friday 4 PM funnel review (Funnel §7) owns throttle/kill decisions on channels and lists; its output feeds this Monday meeting and is read before the dialing plan is set.
3. **Show rate:** Last week's booked visits vs. completed (working assumption — target uncalibrated until 2 weeks of real data).
4. **Stage conversion:** Stage 1→2 contact rate, 2→3 booking rate, 4→5 scope speed, 5→6 deposit rate. Planning floor for proposal→deposit is **25%** (conservative capacity-math floor per Reconciliation Sheet e — NOT a target; reviewed weekly against actuals). Any stage converting at half the team median gets a script/cadence review that week.
5. **Aging report:** Every card past SLA, by name and rep — including silence-clock and hold-expiry breaches.
6. **Capacity check (Ops Lead owns the math):** Deposits and expected packages vs. 2 locked machines and ~25 working days. Sales may never oversell the pinned counters.
7. **Nurture sweep:** Reactivations, 6-month credit check-ins due, DNC count.
8. **Escalation queue:** Every `ESCALATED TO NATHAN` card resolved or re-committed with a date.

Output: a single pinned-thread reply in `#drawdown-war-room` with the week's numbers — the same numbers reps may quote until Thursday's counter update.

---

## CARD-MOVE ETIQUETTE (edit conflicts on shared pinned posts)

The board is 7 shared documents. These rules prevent the two ways it dies: silent overwrites and corrupted posts.

1. **Reps edit only their own cards** — identified by rep initials. Never touch another rep's line, including "fixing" it. Flag it in the daily hygiene audit instead.
2. **Claim the post before a big edit:** drop a ✏️ reaction on the pinned post, edit, remove the reaction. If someone else's ✏️ is on the post, wait or do your Linear entry first. During power-dial hours (8:30–11:30) card edits are quick single-line updates only — batch reformatting happens at 11:30–12:00 or 4:30–5:00.
3. **One line per card, always.** Edit your line in place; never delete and re-add (it scrambles position and history). Backward moves (Stage 3 → 2, including expired holds) are deleted from the higher stage's post and added to the lower one in the same editing session.
4. **Pinned-post skeleton is locked.** Only Harper/Lucas edit headers, stage titles, or ordering. Reps touch card lines only.
5. **Linear is the recovery source.** If a pinned post is corrupted (simultaneous-edit collision, accidental deletion), restore from the 6 PM Linear log — this is why the log rule is absolute. Harper/Lucas perform restores; the rep whose card was affected verifies. Recommended practice: log bookings to Linear immediately after the `#drawdown-won` post rather than waiting for 6 PM.
6. **New cards go at the bottom** of the stage post. Order within a stage is arrival order, not priority — priority lives in the standup, not the post layout.
7. **No customer-facing content in a card line.** Card lines are operational shorthand; language that could embarrass us if screenshotted never appears on the board.

---

## WORKED EXAMPLES — 3 CARDS THROUGH THE BOARD

All timestamps CT. SLA business hours 9 AM–6 PM Mon–Fri; no outbound 6 PM–9 AM. Business-day SLAs shown in practice. (Names fictional; mechanics real.)

### Card A — past client, full run to deposit (the happy path)

| When | Move | Detail |
|---|---|---|
| Mon Jul 27, 8:00 AM | → Stage 1 | List assignment at standup. Card: `J. Hartwell — Westlake Cove — past client 2023 bulkhead — 7/27 — SMS blast today — KL` |
| Mon Jul 27, 10:00 AM | (touch) | SMS blast sent manually from the platform (pre-L3 rule). Logged 6 PM. |
| Tue Jul 28, 10:40 AM | → Stage 2 | Hartwell replies, 8-min call, Scenario 1. Outcome: scheduled next touch — 48-hr hold, call Thu 7/30. Card next action: `call 7/30 re: hold`. `last_twoway_reply_date 7/28`. |
| Thu Jul 30, 2:15 PM | → Stage 3 | Books Tue Aug 4, 9 AM — **$695 payment link paid during the call**. Confirmation text sent 2:19 PM. `#drawdown-won` post (paid). Counter folds in Mon Aug 3 update. |
| Mon Aug 3, 9:15 AM | (touch) | 24-hr reminder text sent (checked at standup). |
| Tue Aug 4, 11:30 AM | → Stage 4 | Visit done, docs captured (fee already collected at booking). Findings: failing tie-backs, 3 ft sediment → flagged `#drawdown-ops` same day (priority signal). |
| Fri Aug 7, 10:00 AM | → Stage 5 | Scope + pricing delivered ($52K, deposit ask $10K ≈ 19%). Inside the 3-business-day SLA. **C1 text sent manually 10:45 AM (≤60 min).** |
| Mon Aug 10, 9:30 AM | (phone track) | Day-2 check-in call. Objection: spouse → 3-way call set for Mon evening (Rebuttal 10). **C2 text fires Wed Aug 12 (Day 3).** |
| Wed Aug 12, 4:30 PM | → Stage 6 | 3-way call Mon 5:30 PM; deposit $10,000 cleared Wed 4:30 PM. `#drawdown-won` post with $. Welcome text Wed 4:50 PM (inside business hours). **C3 (Day 7) suppressed — deposit converts before it fires.** Ops handoff confirmed Thu Aug 13 (within 2 business days). Card: `HANDED TO OPS 8/13`. |
| **Elapsed: 17 days, 8 touches + C1/C2, zero SLA breaches.** | | |

### Card B — cold lead, dies in Stage 2, reactivates (the nurture path + silence clock)

| When | Move | Detail |
|---|---|---|
| Wed Jul 29, 8:00 AM | → Stage 1 | Cold list, public-records source. First touch call 9:45 AM — voicemail (not a move). |
| Fri Jul 31, 11:05 AM | → Stage 2 | Connects on 3rd attempt, Scenario 2. "Just send me information" → one-pager sent within the hour (QR link + Nathan's line filled per production gate), callback traded for Tue Aug 4 (Branch 2E). `last_twoway_reply_date 7/31`. |
| Tue Aug 4 → Mon Aug 10 | (cadence) | Aug 4 callback — no answer. Touches Aug 6, Aug 10 per 48-hr cadence. **No two-way reply since Jul 31 — the silence clock runs from Jul 31; our touches do not reset it.** |
| Tue Aug 11, 8:00 AM | → Stage 7 | 10 consecutive silent days completed Mon Aug 10; moved at standup Aug 11. Lost reason: `silent`. No calls 10 days. One Branch 1F nurture email sent. |
| Wed Sep 9, 4:40 PM | → Stage 2 (reactivated) | Homeowner replies to a public slot-count post: "Is it too late?" Card rewritten, source `reactivated`, silence clock restarts from Sep 9, 2-business-day cadence resumes. Books Sep 11 with payment link paid on the call → Stage 3. |
| **Lesson: the 10-day rule didn't kill the lead — it parked it honestly, the clock was auditable, and the gate count stayed real.** | | |

### Card C — inbound YES, 5-minute SLA, dies at proposal (the SLA path)

| When | Move | Detail |
|---|---|---|
| Mon Aug 17, 1:03 PM | inbound | SMS YES lands in `#drawdown-inbound` via webhook (business hours — clock live immediately). |
| Mon Aug 17, 1:05 PM | claim + → Stage 1 | 👀 claim at 1:05 — inside the 5-min SLA. Card created 1:07 PM. |
| Mon Aug 17, 2:30 PM | → Stage 3 | Call within 2 business hours. Books Aug 20 assessment — **$695 payment link paid during the call** — confirmation text sent 2:44 PM, `#drawdown-won` posted (paid). |
| Thu Aug 20, 1:00 PM | → Stage 4 | Visit completed, docs captured (fee already collected at booking). Findings modest. |
| Mon Aug 24, 9:15 AM | → Stage 5 | Scope sent ($41K, deposit ask $7,500). 2 business days — inside SLA. **C1 sent manually 9:55 AM.** |
| Aug 26 / 28 / Sep 1 | (two tracks) | C2 fires Day 3 (Aug 27); Day-2 and Day-4 phone calls Aug 26, 28; Day-7 decision call Sep 1 (C3 same day, text channel only — no doubling): "We're going to wait." Graceful exit, Script rules. |
| Tue Sep 1, 4:00 PM | → Stage 7 | Lost reason: `timing`. Credit valid 12 months — `credit_expiry 2027-08-20` logged; 6-month check-in scheduled. |
| **Lesson: a clean decline at Stage 5 is a completed process, not a failure — both cadence tracks ran without channel duplication, and the card carried a real lost reason and a future credit.** | | |

---

## PLACEHOLDERS / OPEN DEPENDENCIES (must be filled from live sources; none may be improvised)

1. **Slack bot token + SMS webhook URL** — until configured, all "automation" above runs on the named manual fallback. Owner: **Operations Lead** (per CRM spec §8).
2. **Rep initials roster** — canonical initials for all 4 reps + Harper/Lucas, pinned with the board posts. Owner: Harper, by Jul 29.
3. **Nurture sequence asset (Stage 7 only)** — referenced by Script Branch 1F but **no FINAL nurture email sequence exists in the deliverable queue**. Flagged to orchestrator: until one passes the swarm pipeline, Stage 7 automation is limited to the single Branch 1F email. **Uncalibrated.** (Note: Sequence C is FINAL and covers Stage 5 — this gap is Stage 7 nurture only.)
4. **One-pager EXISTS** (ASSET_OnePager_Summary_v1_FINAL.html/.md, batch1_sales_copy, FINAL Jul 26 — it closes the old Call Script placeholder #9). **Residual gate: QR link + Nathan's direct line must be filled before any print/send** (production gate in its REVIEW_NOTES). Owner: Ops Lead, before the first Stage-2 trade.
5. **Priority scoring rubric** (Stage 4) — Ops Lead to publish a written standard; high/mid/low is a working assumption until then. **Uncalibrated.**
6. **Show-rate target** (Stage 3, Monday review) — set after 2 weeks of real booking data; not invented here. **Uncalibrated.**
7. **Assessment booking calendar** (Calendly/CRM live slots) — live by Aug 5 per Call Script placeholders.
8. **HOA group terms** — Nathan in writing before any HOA card enters Stage 5 (Call Script Hard Rule 4).
9. **Initial counter values** (slots remaining / machine-days) — Harper/Lucas publish with the first Mon/Thu update after equipment locks confirm; until then reps say "the calendar is filling" and nothing more specific.
10. **Automation L3 (Railway/Inngest scheduler, mid-Aug)** — until live, Sequence C and outreach waves A/B fire manually per the Reconciliation Sheet. Owner: Operations Lead.

---

*SALES_SlackBoard_Rulebook v1.1 FINAL | DRAWDOWN 2026 | ATX Lakescapes — Confidential, internal use only*
*Governs the pinned-post board defined in SLACK_SALES_BOARD_SETUP.md. Extends it; contradicts nothing in it. Reconciled against RECONCILIATION_Sheet_2026-07-27.md — where any campaign document disagrees with that sheet, the sheet wins. Effective Day 1: Monday, July 27, 2026.*
