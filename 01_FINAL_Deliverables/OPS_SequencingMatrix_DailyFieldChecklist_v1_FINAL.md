---
version: 1.0
date: 2026-07-27
author: DRAWDOWN 2026 Swarm — Operations Agent (Deliverables 4.1 + 4.2)
status: FINAL
sources:
  - DRAWDOWN_2026_Operations_Playbook.md (PRIMARY — capacity, equipment, sequencing rules, daily routines, quality gates, safety)
  - DRAWDOWN_2026_Order_of_Operations.md (gates, critical path, Phase 3 execution)
reconciled_by: RECONCILIATION_Sheet_2026-07-27.md (published 2026-07-27 — supersedes any conflicting line in this document)
---

# DRAWDOWN 2026 — JOB SEQUENCING MATRIX + DAILY FIELD OPERATIONS CHECKLIST
## Deliverables 4.1 + 4.2 (combined) — How Jobs Get Ordered and How Every Field Day Runs

**Stack (binding):** Slack is the floor — `#drawdown-ops` for equipment, permits, and weather. Linear is the ledger — every field day is logged same-day by 6:00 PM. Reps quote only the pinned counters in `#drawdown-war-room`, updated Monday + Thursday, always framed "as of [Monday/Thursday]'s count."

**Window language (binding):** Hedged only — "projected October–November," "the City and LCRA are lining up." We sell preparation, not prophecy.

**Capacity baseline (from Ops Playbook §1, Target case):** 3 crews, 2 amphibious machines (Truxor T50 owned — CONFIRMED, plus O'Shea/Wilco rental holds), 2–3 conventional machines + mats, ~25 productive days in-window, 72–75% utilization, $16,500 average revenue per crew-day.

**Real-numbers rule (binding):** No invented names, dates, addresses, or counts. Unknowns are `[X]` placeholders.

---
---

# PART A — JOB SEQUENCING MATRIX (Deliverable 4.1)

## A.1 Priority Classes (from Ops Playbook §4 — verbatim criteria)

| Priority | Criteria | Equipment | Timing |
|----------|----------|-----------|--------|
| **P1 — Critical** | Failing bulkhead, safety hazard, structural collapse risk | Amphibious first | Week 1–2 |
| **P2 — High-Value** | Large sediment volume, multiple structures, high-ticket | Amphibious second | Week 2–4 |
| **P3 — Standard** | Routine repair, single structure, mid-ticket | Conventional + mats | Week 3–6 |
| **P4 — Fill** | Small jobs, touch-ups, add-ons | Conventional | Week 5–8 |

**Hard gates before ANY job enters the schedule (Ops Playbook §4 rules 3–4; Quality Gate 1):**

1. Permit in hand and valid — no exceptions, 7-day buffer before work starts.
2. Deposit received and confirmed.
3. Materials on-site or en route.
4. Equipment inspected and ready.
5. Client confirmed and available.
6. Weather forecast reviewed — no severe weather.

A job missing any gate does not get a crew-day. It waits. A waiting job never idles a crew — see A.4 fallback rules.

## A.2 Geographic Clustering Rules

1. **Cove-first grouping.** Jobs are grouped by cove before they are grouped by date. The scheduling unit is a **cove block**: all jobs in one cove, sequenced together, one mobilization.
2. **One machine move per cove block.** The amphibious unit enters a cove once and does not leave until every amphibious-requiring job in that cove is complete or blocked. Cross-lake machine moves cost [X] hours each — they are the single largest non-productive time sink and are scheduled, never improvised.
3. **Move order follows the lake, not the calendar.** Cove blocks are ordered to form a continuous path along the shoreline (no backtracking). Route: [X — cove sequence map from Ops Lead's scheduling matrix, due Sep 30 per Order of Operations item 56].
4. **Half-day adjacency.** A crew finishing a job by 1:00 PM moves only to a job in the same or adjacent cove. A crew never starts a cross-lake move after 1:00 PM.
5. **Staging discipline.** All machines return to the staging area — [X — staging address] — nightly unless a multi-day cove block justifies on-site mooring, decided by the Operations Lead and posted in `#drawdown-ops`.

## A.3 Equipment Efficiency Rules (Amphibious vs. Land Crews)

| Machine | Source | Status | Daily Rate | Assigned To |
|---------|--------|--------|------------|-------------|
| Truxor T50 (amphibious) | ATX Lakescapes (owned) | **CONFIRMED** | $0 | Crew [X] — amphibious lead |
| Amphibious excavator (CAT/EIK) | O'Shea | [X — hold status; deposit due Jul 31 per OoO item 12] | $1,200–1,800/day | Crew [X] |
| Marsh buggy (pontoon excavator) | Wilco | [X — hold status; deposit due Jul 31 per OoO item 12] | $800–1,200/day | Backup / second amphibious |
| Long-reach excavator (40–60 ft) | United Rentals | BACKUP | $600–900/day | On failure of primary |
| Conventional machines + mats | Local rental | HOLD NEEDED | $200–300/day (mats) | Crews 2 & 3 (land) |

**Rules:**

1. **Amphibious machines run P1/P2 only.** Playbook §4: amphibious units handle 1–2 P1/P2 jobs per day. A $1,200–1,800/day machine on a P4 touch-up is burning the margin. No exceptions without Operations Lead sign-off posted in `#drawdown-ops`.
2. **Rental machines are never idle.** If the amphibious queue is empty (permit wait, weather, gap between cove blocks), the rental unit works the highest-priority permitted P3 in its current cove or returns to staging — an idle day is reported in the 6:00 PM Linear log with a reason code.
3. **Land crews carry P3/P4.** Conventional machines + mats handle routine repair, single-structure, and fill work. Land crews do not wait on the amphibious schedule; they run their own cove blocks in parallel.
4. **Truxor T50 first.** The owned machine ($0/day) absorbs the most machine-hours of any unit. When a P1/P2 job can be done by either the T50 or a rental, the T50 does it.
5. **Breakdown cascade** (Ops Playbook §12): stop work → secure site → call backup source (long-reach on retainer) → notify client → reschedule. Post the breakdown in `#drawdown-ops` within 30 minutes.

## A.4 Weather Buffer Rules

1. **2–3 buffer days per week** are built into every weekly schedule (Playbook §4 rule 5). Saturday is the standing buffer/catch-up day; Sunday is rest.
2. **Forecast checked 3× daily** by the Operations Lead: 6:00 AM, 12:00 PM, 3:00 PM — posted to `#drawdown-ops` when conditions change a go/no-go.
3. **24-hour rain delay = automatic reschedule.** Client notified 12 hours in advance (Playbook §12).
4. **Lightning = stop work immediately**, secure equipment, seek shelter (Safety Protocol, emergency table). Resume only on Operations Lead's all-clear in `#drawdown-ops`.
5. **No idle crews on weather days.** Displaced crews shift, in this order: (a) next permitted job in the same cove, (b) indoor/prep work — materials staging, equipment service, job packet prep, (c) catch-up on documentation backlog. The weather day and the fallback used are logged in Linear by 6:00 PM.
6. **Buffer days are spent last.** A clean week does not spend its buffer; a buffer day is consumed only when a scheduled day is lost.

## A.5 Neighbor Coordination Rules

1. **Grouped cove jobs share machine time.** When 2+ jobs exist in one cove, they are batched into a single cove block and share the amphibious unit's mobilization. Per-job mobilization cost drops; per-cove revenue rises.
2. **Sell the neighbors before the machine arrives** (Playbook §4 rule 6 — efficiency + social proof). When a P1/P2 job is booked in a cove, the sales team works adjacent properties immediately: door hangers (OoO items 31/37), yard sign on the active job (item 32), "your neighbor's shoreline is getting fixed" framing. Target: [X] add-on jobs per anchored cove.
3. **One client-contact window per cove.** Where multiple clients share a cove block, the Operations Lead sends a single cove-level schedule note (machine arrival, expected days, noise window) rather than per-job surprises — individual daily updates still go per A/B below.
4. **Add-ons discovered on-site are P4 by default** — scoped in writing (change order protocol, Playbook §9), slotted into the current cove block only if the block has slack; otherwise scheduled to the Week 5–8 P4 window.
5. **Neighbor discount/referral:** $500 credit for booked referrals (OoO item 65, activated Oct 15). Crew leads hand the referral card; they never quote pricing.

## A.6 Sequencing Decision Tree

Run this for every job, in order. Stop at the first NO.

```
1. Is the permit IN HAND and valid?                    —NO→ Permit Coordinator; 7-day buffer rule. Job waits.
   YES ↓
2. Is the deposit RECEIVED and confirmed?              —NO→ Closer owns it. Job is not scheduled.
   YES ↓
3. Priority class? (Playbook §4 criteria)
   • Failing bulkhead / safety hazard / collapse risk  → P1
   • Large sediment / multi-structure / high-ticket    → P2
   • Routine repair / single structure / mid-ticket    → P3
   • Small job / touch-up / add-on                     → P4
   ↓
4. Which cove? → attach to that cove's block.
   • Does a block exist for this cove this window?     —NO→ create one; order it into the shoreline path (A.2 rule 3).
   ↓
5. Which machine?
   • P1/P2 → amphibious (T50 first, rental second).
   • P3/P4 → conventional + mats.
   • Machine already mobilized in this cove? → job inherits the mobilization (A.5 rule 1).
   ↓
6. Which week?
   • P1 → Week 1–2 · P2 → Week 2–4 · P3 → Week 3–6 · P4 → Week 5–8.
   • Conflict inside the window? Higher P-class wins the machine day;
     displaced job takes the next same-cove day, then buffer day (A.4 rule 6).
   ↓
7. Weather check (3× daily) + Gate 1 items 3–6 clear?   —NO→ fallback ladder (A.4 rule 5). Log reason code.
   YES ↓
   SCHEDULED — post crew, machine, cove, and date to #drawdown-ops; enter in Linear.
```

## A.7 Worked Examples

**Example 1 — P1 + P2 sharing one cove and one machine.**
Cove [X-A] has a P1 failing bulkhead (structural collapse risk) and a P2 large-volume sediment job two lots down, both permitted, both deposits confirmed. Decision tree: both P-class jobs → amphibious; both same cove → one cove block, one mobilization. Sequence: Week 1, Day 1–2 the amphibious crew repairs the P1 bulkhead (P1 outranks P2 for the machine day); Day 3–4 the same machine, already in the cove, runs the P2 sediment removal. Mobilizations: 1 instead of 2. Client updates run independently per job (morning/midday/evening, Part B.4). The P2 client's schedule note explains the Day 3 start up front — set at booking, not improvised.

**Example 2 — Thursday rainout absorbed by the buffer.**
Week 3: Crew 1 (amphibious) is mid-block in Cove [X-B] on a P2 restoration; Crews 2 and 3 (land) are on P3s in Coves [X-C] and [X-D]. Wednesday 3:00 PM forecast shows Thursday storms with lightning risk. Operations Lead posts the rain call to `#drawdown-ops` Wednesday evening; clients notified 12 hours ahead (Playbook §12). Thursday: Crew 1 does equipment service + materials staging at the staging area; Crew 2's P3 is under-roof-adjacent prep work; Crew 3 shifts to the next permitted job in the same cove. Friday all crews resume; Saturday (standing buffer) absorbs the half-day slip on Crew 1's P2. No client delivery date moves more than 1 day; the rain day and fallbacks are logged in Linear by 6:00 PM Thursday with reason code WEATHER.

**Example 3 — Neighbor batching turns one P3 into a cove block.**
A P3 dock repair is booked in Cove [X-E] (single structure, mid-ticket — conventional + mats). Sales works the cove before the machine mobilizes: door hangers on [X] adjacent waterfront lots, yard sign on the active job, referral card with the $500 credit (active Oct 15). Result: two neighbors book — one P3 bulkhead patch, one P4 touch-up — both permitted by Week 4. All three jobs batch into one Week 4 cove block: one conventional machine + mats, one mobilization, three invoices. The P4 lands inside its Week 5–8 class window only if the cove block can't absorb it — here it can, because the machine is already mobilized (A.5 rules 1 and 4). Sequencing inside the block: P3 dock (Day 1–2), P3 bulkhead (Day 3), P4 touch-up (Day 4 morning); machine demobilizes Day 4 by 1:00 PM and moves only to an adjacent cove (A.2 rule 4).

---
---

# PART B — DAILY FIELD OPERATIONS CHECKLIST (Deliverable 4.2)

**Who uses this:** the Crew Lead. A new Crew Lead can run Day 1 from this checklist alone. Every item is a checkbox. No item requires interpretation — if it can be misread, it names the person who decides (Crew Lead → Operations Lead → Nathan, in that order).

**Times are CT.** The 6:00 PM Linear log is a hard same-day deadline (Linear is the ledger; Slack is the floor).

## B.1 Morning — Staging Area (6:30 AM – 7:30 AM)

- [ ] **6:30** — Arrive at staging area ([X — address]). Confirm crew attendance; any absence texted to Operations Lead now.
- [ ] **6:35** — Weather check (Operations Lead posts the 6:00 AM go/no-go to `#drawdown-ops`). If NO-GO: stand by for fallback assignment (Part A.4 rule 5). Do not depart.
- [ ] **6:45** — Equipment inspection on every machine assigned today: fluids, tracks, attachments, safety features functional. Any fault → photograph, post to `#drawdown-ops`, do not operate.
- [ ] **6:50** — PPE check, every person: hard hat, hi-vis vest, steel-toed boots, gloves. Life jackets for anyone working near or over water. Eye protection if cutting/grinding/chemicals. Hearing protection for equipment operators.
- [ ] **6:55** — Site kit confirmed: first aid kit accessible, fire extinguisher accessible, emergency contacts posted, phones/radios charged.
- [ ] **7:00** — **Safety briefing (5 minutes, mandatory, all hands):** today's job site hazards, water exposure points, emergency procedure for the top risk (equipment-in-water: stop work, assess stability, 911 + Nathan).
- [ ] **7:10** — Job packet review: scope, hazards, access instructions, **permit physically in the packet**. No permit in packet → do not depart; call Operations Lead. (Gate: permit must be in hand — Part A.1.)
- [ ] **7:15** — Load trucks with today's materials per job packet. Confirm deposit-confirmed job only (if unsure, check with Operations Lead — never argue payment with a client).
- [ ] **7:30** — Depart for first job site. Post departure to `#drawdown-ops` (crew, machine, destination cove).

## B.2 On-Site — Arrival & Setup

- [ ] **T-minus-30 min** — Client notified of arrival (call or text from Crew Lead; scripted morning message at B.4).
- [ ] **On arrival** — Site safety setup: cones, barriers, signage. Public water/land access points blocked off.
- [ ] **Before photos — minimum 20,** matching angles you'll repeat at completion; drone if available.
- [ ] **Client walk-through** if the client is present: confirm scope matches the job packet, point out safety zones. Scope questions → Operations Lead. Crew Leads never renegotiate scope or price.
- [ ] **Log start time** in the daily log (Linear entry opened now, closed at 6:00 PM).

## B.3 On-Site — During Work

- [ ] **Progress photos every 2 hours** from the same angles as the before set.
- [ ] **Safety check every 4 hours:** PPE compliance, equipment safety features, site hazards re-assessed, no incidents.
- [ ] **Daily log notes running all day:** hours, conditions, issues, scope changes. Notes are written when they happen, not reconstructed at 5 PM.
- [ ] **Midday (12:00 PM)** — Crew Lead check-in with Operations Lead; midday client update sent on multi-day jobs (B.4).
- [ ] **Scope change identified?** Stop that portion of work → Operations Lead assesses time/cost/materials → client notified within 4 hours → written change order within 24 hours → client approval in writing before changed work continues. **No verbal approvals. Ever.** (Playbook §9.)
- [ ] **50% complete (multi-day jobs) — Gate 2:** progress photos uploaded, scope adherence check, client satisfaction pulse check, budget check, safety check. All five logged in Linear before work passes 50%.
- [ ] **Any incident** (equipment in water, injury, structural collapse, hazmat, severe weather): follow the emergency table — stop work, secure, call 911 where indicated, then Operations Lead, then Nathan. Post to `#drawdown-ops` within 30 minutes.

## B.4 Client-Update Rhythm (every active job, every day on-site)

All three touches are sent by the Crew Lead (or Operations Lead on multi-crew coves) from the company line. All outbound client messages go **before 6:00 PM CT** — no automated outbound of any kind between 6:00 PM and 9:00 AM CT, ever (Reconciliation Sheet (b)). The evening touch is sent at 5:45 PM, not 6:00 PM.

- [ ] **Morning (~8:00 AM):** "Good morning [Name]. Crew [X] is on-site at [Address] today. Expected work: [scope]. Weather: [conditions]. We'll send progress photos this afternoon."
- [ ] **Midday (~12:00 PM, multi-day jobs):** lunch-time progress note — what's done, what's next this afternoon. (Playbook: "client update at lunch.")
- [ ] **Afternoon (~4:00 PM):** "Update from [Address]: [progress summary]. [X]% complete. Remaining work: [scope]. Tomorrow: [plan]. Photos attached."
- [ ] **Evening (5:45 PM, before the 6:00 PM silence window):** "Day complete at [Address]. [Summary]. Crew returns tomorrow at [time]. Call or text if you have questions: [Operations Lead number]."

Window language in every message: hedged — "projected October–November," never a promised refill date.

## B.5 On-Site — Completion (end of job, or end of day on multi-day jobs)

- [ ] **Final inspection with Crew Lead** against job packet scope.
- [ ] **After photos — minimum 20,** matching the before angles exactly.
- [ ] **Client walk-through and sign-off** (signature on completion form; if client absent, Operations Lead schedules sign-off within 24 hours — job is not "complete" in Linear without it).
- [ ] **Site cleanup and restoration** to pre-work condition.
- [ ] **Waste documented:** every load photographed, load ticket + landfill weight ticket collected (Playbook §8 — manifest + photo, no exceptions).
- [ ] **Equipment reload and maintenance check** before departure.
- [ ] **Gate 3 (final day of job):** final photos uploaded and labeled, sign-off obtained, as-built documentation complete, waste disposal documented, equipment cleaned and inspected, site restored. Review request + referral request are sent by the Operations Lead within 24 hours — not by the crew.

## B.6 Evening — Staging Area (5:00 PM – 6:00 PM)

- [ ] **5:00** — Return to staging area. (Machines moor on-site only if Operations Lead approved it in `#drawdown-ops` — Part A.2 rule 5.)
- [ ] **5:15** — Equipment cleaning and basic maintenance. Faults found → photograph, post to `#drawdown-ops`, flag for morning inspection.
- [ ] **5:30** — **Daily log submitted to Linear:** photos (before/progress/after), notes, hours, conditions, issues, change orders, reason codes for any idle or weather time. **Hard deadline 6:00 PM same day — Linear is the ledger; a day not logged is a day that didn't happen.**
- [ ] **5:45** — Evening client touch sent (B.4) — inside the 6:00 PM cutoff.
- [ ] **5:45** — **Next-day prep confirmed:** permits in packet for tomorrow's jobs, materials loaded or staged, access instructions confirmed, tomorrow's weather checked (Operations Lead's 3:00 PM forecast + evening recheck).
- [ ] **6:00** — Crew dismissed. Operations Lead files the end-of-day report to Nathan and confirms tomorrow's priority list (Playbook §13).

## B.7 Day-1 Test for a New Crew Lead

If you can answer these five from this document alone, you're ready:

1. What do you do if the permit isn't in the job packet at 7:10 AM? *(Don't depart; call Operations Lead.)*
2. When does a scope change resume? *(After written client approval of the change order — never verbal.)*
3. What's the photo minimum, and when? *(20 before, every 2 hours during, 20 after, matched angles.)*
4. When is the Linear log due? *(6:00 PM same day, hard deadline.)*
5. What's the latest a client message can go out? *(5:45 PM send, 6:00 PM CT absolute cutoff.)*

---

## PLACEHOLDER REGISTER

| Placeholder | Owner | Needed By |
|---|---|---|
| [X] — cross-lake machine move time (hours) | Operations Lead | Sep 30 scheduling matrix (OoO item 56) |
| [X] — cove sequence map / shoreline route order | Operations Lead | Sep 30 scheduling matrix |
| [X] — staging area address | Operations Lead | Aug 31 equipment delivery (OoO item 39) |
| [X] — O'Shea / Wilco rental hold status + unit assignments | Benjamin | Jul 31 hold deposits (OoO item 12) |
| [X] — amphibious lead crew assignment (T50) | Operations Lead | Sep 14 crew hiring complete (OoO item 44) |
| [X] — target add-on jobs per anchored cove | Nathan | First Monday pipeline review |
| [X] — Operations Lead phone number (client scripts) | Operations Lead | Oct 1 Day 1 |
| Cove names in worked examples ([X-A] through [X-E]) | Operations Lead | When real jobs are booked |

---

*ATX Lakescapes | DRAWDOWN 2026 Swarm | July 27, 2026*
*This document is subordinate to the Operations Playbook and the Reconciliation Sheet. Where they conflict with this document, they win.*
