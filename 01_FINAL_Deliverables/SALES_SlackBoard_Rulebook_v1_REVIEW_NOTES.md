# DRAWDOWN 2026 — REVIEW NOTES
## Deliverable 3.3 — SALES_SlackBoard_Rulebook_v1
### Pipeline Record: 6 internal layers + 1 external red-team round (Layer 7)

**Companion to:** `SALES_SlackBoard_Rulebook_v1_FINAL.md` (v1.1)
**Revision rounds used:** 2 internal + 1 external = 3 of 3.
**Date:** 2026-07-27 · **Author:** DRAWDOWN 2026 Swarm — Sales Engineering Agent
**Reconciled against:** `RECONCILIATION_Sheet_2026-07-27.md` (authoritative; supersedes conflicting lines here and in the rulebook)

---

## LAYER 1 — DRAFT (Round 1)

**Sources read in full before drafting (mandatory):**
1. `SLACK_SALES_BOARD_SETUP.md` (Google Drive, canonical, updated 2026-07-24) — the board this rulebook governs.
2. `DRAWDOWN_2026_Master_Attack_Plan.md` — money model, cadence, gates, capacity.
3. `COPY_CallScript_Master_v1_FINAL.md` — the conversational meaning of "contacted" (two-way exchange, one of three outcomes) and "booked" (date+time committed + confirmation text sent before hangup).

**Round 1 draft characteristics (later revised):**
- Applied the interim 3-business-day SLA uniformly to all stages.
- Stage 3 exit required only "visit performed" — payment status not gated.
- Included an 8th board stage ("Scheduled for Drawdown") mirroring Master Plan Part 6.
- Stage 5 assumed an automated Resend follow-up sequence.
- No worked examples; card-move etiquette was 3 bullets.

---

## LAYER 2 — SKILL POLL (6 specialist roles, Round 1)

| # | Role | Verdict | Key objection |
|---|---|---|---|
| 1 | **Sales Operations Manager** | STRONG | Board mechanics sound; but a uniform 3-day SLA is unenforceable mush — SLAs must differ by stage or reps will ignore all of them. |
| 2 | **Frontline Rep (usability)** | WEAK | Stage 3 "visit performed" exit lets a rep move a card with the $695 uncollected — I'll inherit that argument at the door. Also: who fixes a corrupted pinned post at 10 AM during power dialing? Unanswered. |
| 3 | **Nathan (CEO / final closer)** | STRONG | Escalation triggers match Call Script Hard Rule 7. Demanded: no refund decision anywhere but his desk, and DNC framed as firing-level. |
| 4 | **Ops Lead (capacity)** | STRONG | Handoff boundary acceptable ONLY if Stage 6 stays the sales terminal stage and scheduling lives in `#drawdown-ops` — the 7-post board is the approved setup spec; an 8th post contradicts it. |
| 5 | **Data Steward (Linear)** | STRONG | Per-stage field lists are loggable by 6 PM. Required: Linear named explicitly as the restore source for corrupted pinned posts, or the log rule has no teeth. |
| 6 | **Real-Numbers / Compliance Guard** | WEAK | Gate counts must survive backward moves (no-shows) without cooking the numbers. ~~"Every automation claim must trace to a FINAL asset"~~ — *claim corrected in Layer 7: the accurate standard is "every automation claim traces to a FINAL asset or a named manual fallback executing a FINAL asset."* |

**Round 1 gate result: 4 STRONG / 2 WEAK → FAIL** (threshold: 4+ STRONG required, but both WEAKs struck binding campaign rules — asset finality and stack conformity — so the draft went to full revision rather than passing on a technicality).

---

## LAYER 3 — REVISION (Round 2 changes)

1. **Per-stage SLAs replaced the uniform 3-day rule.** *(Confirmed correct by Reconciliation Sheet d: "per-stage SLAs govern; 3.3 has landed.")*
2. **Stage 3 exit gate hardened.** *(Superseded by Layer 7 / Sheet a: the fee gate moved from Stage 3 EXIT to Stage 3 ENTRY — collected at booking.)*
3. **8th stage removed.** "Scheduled for Drawdown" documented as Ops-owned in `#drawdown-ops`; Stage 6 handoff is the boundary. Deviation from Master Plan Part 6's 8-stage list is deliberate and recorded here.
4. **Asset discipline:** all automation references audited against FINAL assets. ~~"nurture/follow-up sequences are NOT FINAL — one-pager flagged as open dependency"~~ — *partially stale after Layer 7: Sequence C is FINAL (SMS + Email suites); the one-pager is FINAL (Jul 26). Only the Stage 7 nurture sequence remains an open dependency. See Layer 7.*
5. **Card-move etiquette expanded** to 7 rules including the ✏️ claim protocol, power-dial-hours edit restriction, skeleton lock (Harper/Lucas only), and Linear-as-restore-source.
6. **Worked examples added** (3 cards) per assignment spec. *(Timestamps later corrected in Layer 7.)*

**Re-poll (Round 2):** Roles 2 and 6 re-reviewed. Role 2: STRONG. Role 6: STRONG. **Result: 6/6 STRONG → PASS.**

---

## LAYER 4 — BOARD REVIEW MEMO (submitted with Round 2 draft)

> **To:** DRAWDOWN 2026 Board · **From:** Swarm Sales Engineering · **Re:** Deliverable 3.3, Round 2
>
> The rulebook defines entry/exit/SLA/escalation/Linear fields for all 7 pinned-post stages, plus daily hygiene (Harper, 4:45 PM), the Monday gate review ~~(40 by Aug 31 / 60 by Sep 30 / 80+ by Oct 31)~~ *(superseded by Sheet e: 80 by Sep 30, DIAGNOSE floor <60; checkpoints 40 by Aug 31, 60 by mid-September)*, edit-conflict etiquette, and 3 timestamped worked examples. Two decisions need board awareness, not approval: (a) the Master Plan's 8th kanban stage is folded into an Ops handoff to preserve the approved 7-post Slack setup; (b) ~~two automation conveniences (nurture sequence, one-pager) are deliberately NOT referenced~~ *(corrected in Layer 7: Sequence C FINAL and one-pager FINAL; only the Stage 7 nurture sequence remains unowned)*. Risk the board should hold: SLA enforcement is human-powered until Slack tokens exist — the document is honest about this and names a manual owner for every automation.

**Board response:** Approved to proceed to Devil's Advocate. One note — "make sure the worked examples show a backward move so reps believe it's allowed." (Covered.)

---

## LAYER 5 — DEVIL'S ADVOCATE RED TEAM (internal)

### Weaknesses (6)

1. **Pinned posts don't scale.** A single Slack post holding 40+ card lines becomes uneditable — no overflow mechanism (e.g., splitting a stage post into Part 1/Part 2).
2. **SLA enforcement is entirely human.** Until tokens exist, breaches are discovered at 4:45 PM hygiene or next standup, up to a full day late. *(Partially mitigated by Layer 7: Sheet b defines SLA business hours 9–6 and arms after-hours clocks at 9 AM — but discovery remains manual.)*
3. **Gate inflation incentive.** Gates count *bookings*; pencil bookings can inflate the count. *(Substantially mitigated by Layer 7 / Sheet a: only paid-or-held bookings count — a pencil booking with no payment link or logged hold no longer enters Stage 3 or the gate count at all.)*
4. **Stage 6 → Ops handoff can strand deposits.** Money collected; accountability has a seam. *(Mitigated: `HANDED TO OPS` marker survives on the board until Monday review confirmation.)*
5. **Reactivation can launder a neglected lead.** *(Mitigated in Layer 7: `last_twoway_reply_date` is now a required Linear field, so reset clocks are auditable.)*
6. **Edit-conflict etiquette relies on discipline during the exact hours discipline is lowest.** The Linear restore path will be used in anger at least once in August.

### Improvements (3) — all adopted

1. Show-rate + booking-quality audit added to the Monday review.
2. Linear named as restore source; restores Harper/Lucas-only with rep verification.
3. Stage 6 `HANDED TO OPS [date]` marker persists until Monday review confirms handoff.

### Worst-case scenario

**Mid-September, gate pressure at its peak.** Two reps edit the Stage 3 pinned post simultaneously at 10:15 AM; Slack's last-write-wins silently drops 14 card lines including 5 assessment dates. The Linear restore works only for cards logged by 6 PM the previous day — same-morning bookings exist only in the rep's memory. Reconstruction takes two days; two homeowners who experienced silence decline (one a ~$95K full-cove prospect). The gate is missed and the capacity model — built on inflated numbers — has committed machine-days against phantom demand. **Mitigations in the document:** Linear restore path (Rule 5 + "log bookings immediately after the won-post" practice), power-dial edit restriction, show-rate tracking, paid-or-held gate (Sheet a — pencil bookings no longer count), no-show backward-move normalization. **Residual risk accepted:** the restore path cannot recover same-day unlogged bookings.

---

## LAYER 6 — FINAL (v1.0, internal)

All three adopted improvements incorporated. Round 2 draft + DA amendments = v1.0 FINAL. **Internal revision rounds used: 2 of 3.**

---

## LAYER 7 — EXTERNAL RED-TEAM ROUND (2026-07-27) → v1.1

**Independent red team verdict: REVISE — 1 blocker + 6 majors/minors.** Orchestrator published `RECONCILIATION_Sheet_2026-07-27.md` settling the contested points; sheet items (a)–(e) + Day-1 manual operations applied in full. All fixes below verified against the sheet. **This consumed the third and final revision round.**

### Fixes applied

| # | Ref | Severity | Issue | Resolution |
|---|---|---|---|---|
| 1 | R1 | **BLOCKER** | Stale one-pager placeholder (rulebook Placeholder #4 + two rows here) claimed the one-pager didn't exist. | Corrected: one-pager EXISTS — `ASSET_OnePager_Summary_v1_FINAL.html/.md` (batch1_sales_copy, FINAL Jul 26; closes old Call Script placeholder #9). Residual production gate: QR link + Nathan's direct line filled before any print/send. Owner: Ops Lead, before first Stage-2 trade. |
| 2 | R2/X3 | MAJOR | Stage 5 automation + Stage 2 note wrongly claimed "no FINAL sequence asset." | Deleted. Per Sheet (c): Sequence C (C1 ≤60 min after report delivery / C2 Day 3 / C3 Day 7) is FINAL in both SMS and Email suites, fired MANUALLY from the platform by the owning rep until automation L3 (mid-Aug). Rulebook rewritten so Stage 5 runs two explicit tracks — C texts (SMS/email) + Day 2/4/7 PHONE calls — neither duplicating a channel. Role 6's Layer-2 quote corrected accordingly. |
| 3 | R3 | MAJOR | Card A taught a violation: SMS blast logged 9:12 AM. | Changed to 10:00 AM. All three worked examples re-audited for window compliance (no outbound 6 PM–9 AM per Sheet b): Card A's deposit/welcome moved from 6:00/6:20 PM to 4:30/4:50 PM; reminder texts set at 9:15 AM; all other timestamps verified inside business hours. |
| 4 | R4/X4 | MAJOR | "$695 paid on site" contradicted Sheet (a). | Rewritten per Sheet (a): $695 collected AT BOOKING (payment link, or explicit logged 48-hour hold). Unpaid = not booked; "pay on site" does not exist. Fee gate moved from Stage 3 exit → Stage 3 entry; Stage 4 entry no longer re-checks payment; Linear `fee_status` → `payment_status (paid / hold_active w/ expiry)`; hold-expiry → backward move to Stage 2; Card A and Card C examples corrected to payment-during-call. Gates count paid-or-held only. |
| 5 | R5 | MINOR | Stage 2 dead pointer "(See Placeholders)" with no matching placeholder. | Pointer removed. Stage 2 automation now states: no separate engaged-follow-up asset exists or is required — the 48-hour cadence is rep-driven per the FINAL Call Script, alongside FINAL outreach waves A/B fired manually. |
| 6 | R6 | MINOR | Stage 2 silence clock undefined; Card B unauditable. | Clock defined verbatim: "10 consecutive calendar days of silence measured from the homeowner's last two-way reply; our touches do not reset it." `last_twoway_reply_date` added as a required Linear field. Card B re-dated: last two-way Jul 31 → touches Aug 4/6/10 (no reset) → 10 silent days complete Mon Aug 10 → Stage 7 at standup Tue Aug 11. Fully auditable. |
| 7 | R7/X6 | MINOR | Placeholder #1 owner wrong. | Slack bot token + webhook owner changed Harper → **Operations Lead** (CRM spec §8). New Placeholder #10 (automation L3) also assigned to Operations Lead. |
| 8 | X7 | MINOR | Monday review didn't acknowledge the Friday funnel review. | Added: Monday 8:30 pipeline review owns the week's dialing plan; the Friday 4 PM funnel review (Funnel §7) owns throttle/kill decisions and feeds Monday (agenda item 2). |

### Sheet-mandated corrections beyond the fix list (applied to keep the rulebook reconciled)

- **Sheet (e) — gates superseded:** Monday review gate table replaced. New: **80 paid-or-held by Sep 30 (target), <60 by Sep 30 = DIAGNOSE floor; interim checkpoints 40 by Aug 31, 60 by mid-September (exact date set at first Monday review).** The 25% proposal→deposit planning floor (not a target) added to the conversion agenda item. Old "40/60/80 by Aug 31/Sep 30/Oct 31" framing removed from the rulebook and struck above.
- **Sheet (b) — after-hours rule:** Added as a binding global rule (no outbound 6 PM–9 AM CT; AFTER_HOURS tag; clocks arm 9 AM; SLA business hours 9 AM–6 PM Mon–Fri). Stage 1 inbound SLA, Stage 6 welcome touch, and Linear fields updated; worked examples audited (Fix 3).
- **Sheet (c) + Day-1 manual operations:** Stage 1 automation now names FINAL outreach waves A/B (SMS A1–A5/B1–B4, email waves A/B) sent manually by the assigned rep with 10DLC/suppression/A2 gates; human watches `#drawdown-inbound` for the first hour after every blast; backup Nathan.

### Placeholder / open-dependency list (post-Layer-7, corrected)

| # | Placeholder | Owner | Needed by | Status |
|---|---|---|---|---|
| 1 | Slack bot token + SMS webhook URL (manual fallbacks named until then) | **Operations Lead** (CRM spec §8) | ASAP | Open |
| 2 | Canonical rep-initials roster pinned with board posts | Harper | Jul 29 | Open |
| 3 | Nurture email sequence (Stage 7 only) — no FINAL asset; Stage 7 limited to Script Branch 1F single email. UNCALIBRATED. | Orchestrator (queue gap) | Before Sep nurture volume matters | **Flagged — unowned** |
| 4 | ~~One-pager asset~~ **RESOLVED:** one-pager EXISTS (FINAL Jul 26). Residual gate: QR link + Nathan's direct line filled before any print/send. | **Ops Lead** | Before first Stage-2 trade | Production gate open |
| 5 | Stage 4 priority-scoring rubric (high/mid/low working assumption). UNCALIBRATED. | Ops Lead | ~mid-Aug | Open |
| 6 | Show-rate target. UNCALIBRATED until 2 weeks of real data. | Nathan + Ops Lead | ~Aug 10 | Open by design |
| 7 | Live booking calendar (Calendly/CRM slots) | Campaign ops | Aug 5 | Open |
| 8 | HOA group terms in writing (Call Script Hard Rule 4) | Nathan | Before any HOA card reaches Stage 5 | Open |
| 9 | Initial counter values (slots remaining / machine-days) | Harper/Lucas + Benjamin | First Mon/Thu update post-lock | Open |
| 10 | Automation L3 (Railway/Inngest scheduler) — until live, Sequence C and waves A/B fire manually per Sheet | Operations Lead | Mid-Aug | Open |

### Uncalibrated working assumptions (explicitly labeled in the FINAL document)

- Stage 4 priority rubric (high/mid/low) — no scoring standard exists yet.
- Show-rate target — deliberately not invented; set from real data after 2 weeks.
- Stage 7 nurture cadence beyond the single Branch 1F email — asset gap (Stage 5 is now covered by FINAL Sequence C).
- Booking-to-visit gap guidance (10 business days, Stage 3) — sales-judgment norm, not a measured optimum.

### Deliberate deviations (recorded, not hidden)

1. **8-stage Master Plan kanban → 7-stage board.** "Scheduled for Drawdown" is Ops-owned (`#drawdown-ops`); the approved setup spec's 7-post board governs.
2. **Uniform 3-day interim SLA → per-stage SLAs.** Ratified by Sheet (d).
3. ~~"No automation reference to any non-FINAL asset"~~ **Corrected in Layer 7:** the rulebook now references FINAL Sequence C and FINAL waves A/B (manual until L3), the FINAL one-pager, and the FINAL Call Script. The only remaining unowned asset dependency is the Stage 7 nurture sequence.
4. **Gate table deviates from the Master Plan's 40/60/80-by-Oct-31 framing** — per Sheet (e), which supersedes it campaign-wide.

### Layer 7 verdict

All 8 numbered fixes + 3 sheet-mandated corrections applied and verified against `RECONCILIATION_Sheet_2026-07-27.md`. **v1.1 FINAL. Revision rounds exhausted (3 of 3):** any further changes require a v2 with a fresh pipeline.

---

*Review Notes — SALES_SlackBoard_Rulebook v1.1 | DRAWDOWN 2026 Swarm | 2026-07-27*
*Reconciled against RECONCILIATION_Sheet_2026-07-27.md — where any campaign document disagrees with that sheet, the sheet wins.*
