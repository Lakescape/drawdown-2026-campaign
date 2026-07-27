# DRAWDOWN 2026 — COMPLETE SALES FUNNEL MAP
## Deliverable 3.1 — REVIEW NOTES (6-Layer Pipeline Documentation + External Red-Team Round)

Version: v1 FINAL (rev. 2026-07-27 — external red-team round applied)
Date: 2026-07-27
Author: DRAWDOWN 2026 Swarm — Sales Engineering Writer Agent
Companion to: SALES_FunnelMap_Complete_v1_FINAL.md
Revision rounds: 3 of 3 (Round 1 draft → poll+revision; Round 2 internal Devil's Advocate applied → Final; Round 3 independent external red team REVISE (light) → all 10 fixes applied → re-FINAL). At the round cap; any further changes require a new version number.

---

## LAYER 1 — DRAFT

Sources read before drafting (all four mandatory inputs):
1. `01_Master_Plan/DRAWDOWN_2026_Master_Attack_Plan.md` — funnel math, capacity model, cadence, Kanban stages, risk register.
2. `04_Operations/DRAWDOWN_2026_Operations_Playbook.md` — capacity table, sequencing, deposit structure, post-job/referral protocol.
3. `batch1_sales_copy/COPY_CallScript_Master_v1_FINAL.md` — the four conversion scenarios, rebuttals, hard rules, placeholders (incl. the 48-hr hold, photo-assessment downsell, referral-at-booking ask).
4. Drive: `SLACK_SALES_BOARD_SETUP.md` — 6 channels, 7 pinned stage posts, card format, Mon/Thu counters, 5-min SLA, same-day Linear rule.

Also skimmed for cadence grounding: COPY_SMS_SequenceSuite_v1_FINAL.md (Sequences A/B/C, Jul 27 anchor, structural-scarcity rules) and COPY_EmailSequenceSuite_v1_FINAL.md (C1/C2/C3 event anchors, hedged-language rules).

Draft decisions:
- 10 stages (0–9) instead of the board's 7 pinned posts, because intake (0), scheduling (7), completed job (8), and referral loop (9) are real funnel steps that live outside the sales board (ops channel + Linear) — the map reconciles both rather than pretending the board is the whole funnel.
- Per-channel conversion table rather than a single blended column, so the weekly review can kill/throttle individual channels.
- Revenue check computed honestly: 15 deposits at 15/60/25 mix ≈ $812K contract value — below the $1M headline. Surfaced as "the single most important number in this document" rather than smoothed over.

---

## LAYER 2 — SKILL POLL (6 roles)

| Role | Verdict | Key input |
|---|---|---|
| Sales Engineer | STRONG | Stage definitions map 1:1 to the 7 pinned posts + ops stages; fallbacks chain correctly (hold → photo assessment → info-for-call). |
| Conversion Copywriter | STRONG | Every human touchpoint reuses FINAL script language; no new customer-facing copy invented; hedged-language rule enforced in automations. |
| Ops / Capacity Planner | STRONG | Oversell guard placed at Stage 6→7 (upstream of scheduling), consistent with the real-time capacity dashboard rule; deposit→capacity feed ownership (Ops Lead, never reps) preserved. |
| RevOps / Data Analyst | WEAK (Round 1) | Objected that a single blended funnel table would hide channel failure; demanded per-channel rates, explicit "uncalibrated" labels, and kill/throttle triggers with tripwires. |
| Field Rep (practitioner) | STRONG | Stall rule + 3-touch minimum workable inside the daily cadence (8:00 standup, power-dial block, 6:00 PM logging); referral-at-booking ask already in script muscle memory. |
| Finance / CAC Guardian | STRONG (with note) | $450 CAC target preserved; flagged that rep labor, not ad spend, is the real acquisition cost — weekly review must track fully-loaded CAC, and paid is the first throttle. |

**Poll result: 5 STRONG / 1 WEAK → passes the 4+ STRONG gate; RevOps objections drove the Round 2 revision.**

---

## LAYER 3 — REVISION (Round 2 changes applied)

Applied from the RevOps WEAK vote:
1. Split the funnel math table into per-channel columns (S1–S5) instead of blended-only.
2. Added explicit kill/throttle triggers to Section 5c (CAC 2-week rule, spam-complaint pause, 60%-of-assumption root-cause rule).
3. Labeled every non-source number `working assumption, uncalibrated`; added placeholder P7 making the Friday review the calibration mechanism.

Also tightened: ASCII flowchart added for Slack-posting contexts where mermaid won't render.

---

## LAYER 4 — BOARD REVIEW MEMO

**To:** Nathan Menkin
**From:** DRAWDOWN 2026 Swarm — Sales Engineering
**Re:** Deliverable 3.1 Complete Funnel Map — approval request

1. **What this is:** the full funnel from five lead sources to completed job and referral loop, with per-stage conversion assumptions, fallbacks, automation triggers, human touchpoints, and Slack/Linear mapping. It runs entirely on the FINAL stack decisions — Slack floor, Linear ledger, Drive files, Jul 27 cadences untouched.
2. **The number you need to see:** 15 deposits at the standard mix ≈ $812K contract value (~$860K gross with kept assessment fees — corrected from $869K in the external round, see below). That is the floor path. $1M needs ~18–20 deposits or a richer high-ticket/HOA mix. The funnel review ritual (Fridays 4:00 PM) is built to catch which lever to pull by mid-August.
3. **The model's honesty:** every conversion rate except the campaign-set floors (25% proposal→deposit planning floor, 15/60/25 mix, capacity model) is labeled uncalibrated. The gates (40 by Aug 31 / 60 by mid-Sep / 80 by Sep 30 — corrected to Order of Operations framing in the external round) are achievable under the model but the Aug 31 checkpoint leans heavily on warm-list engagement — if warm engagement lands under ~45%, Checkpoint 1 is the first thing that breaks.
4. **Verdict requested:** APPROVED WITH NOTES — notes being placeholders P1–P9, of which P1 (list counts), P3 (paid budget), and P4 (HOA group terms) are yours.

**Board verdict: APPROVED WITH NOTES.**

---

## LAYER 5 — DEVIL'S ADVOCATE RED TEAM (internal)

### Weaknesses (7)

1. **List composition is invented.** 150 warm / 800 cold / 50 HOA is a modeling assumption calibrated backward from the 80-booking gate. If the real warm list is 80 names, the Aug 31 checkpoint (40) is mathematically dead on arrival and the map won't know until P1 is filled. *Mitigation: P1 due before Day 1; Checkpoint 1 tripwire in Section 5c.*
2. **The funnel as modeled does not reach $1M.** 15 deposits ≈ $812K. The map says so plainly (Section 5b), but the campaign's headline is $1M — a reader skimming for the headline could miss that the base case under-delivers it by ~20%.
3. **25% proposal→deposit is a floor, not evidence.** No historical Lake Austin baseline is cited. If real conversion is 18%, deposits drop to 11 and revenue to ~$600K — the Floor case. The sensitivity table covers it, but the base case presents 25% as the planning number. *(Settled by reconciliation sheet (e): 25% is explicitly a conservative planning floor, not a target.)*
4. **Paid channel is a ghost limb.** No approved budget, no CPL baseline, no creative performance data. The $12K / 60-lead / 7-bookings line is arithmetic on a placeholder (P3). CAC $450 for a $48K construction ticket in a 13-week window is untested.
5. **Referral loop timing mismatch.** Post-job referrals (Stage 9) mostly land after the window closes — they feed the next window, not this one. The map handles this by making Stage 3's referral-at-booking ask the in-window engine, but the "referral loop" in the funnel title oversells its in-window contribution.
6. **Show-rate assumption (93%) ignores October reality.** Assessments run Aug–Oct against competing contractor calls, hurricane-season weather, and seller-market homeowner distraction. An 80% show rate cuts proposals to ~53.
7. **No cost of failure is monetized.** No-shows, slipped jobs, and refunded/released holds have real dollar costs (assessor time, held slots) that appear nowhere in the model — margin analysis assumes clean flow.

### Improvements (3)

1. **Added per-channel kill/throttle triggers** (Section 5c) so underperformance is a Friday decision rule, not a vibes debate — paid throttles first, protecting the warm/referral core.
2. **Promoted the referral-at-booking ask to a named in-window engine** (Stage 3 + Section 5a referral column) instead of relying on post-job referrals that arrive too late.
3. **Defined the oversell guard explicitly** (Stage 7): committed $ vs. remaining crew-days checked weekly, waitlist with priority sequencing before any oversell — converts the capacity ceiling from a risk into a scarcity asset.

### Worst-case scenario

**The drawdown is delayed or cancelled** (Risk Register: low probability, critical impact). State of play: ~$48K in kept assessment fees (corrected figure — non-converters only), ~15 deposits held under contract, scarcity language ("we committed in July," "machine-days") deployed publicly for 3+ months. Fallout: deposit-handling per contract terms, 12-month credits absorb assessment holders, and the brand must pivot messaging to next-window pre-booking without the scarcity claims retroactively reading as invented. Defense in depth already in the map: hedged language at every stage (nothing promised as certain), 12-month credit validity, flexible assessment timing, and the waitlist/nurture infrastructure converting this window's pipeline into the next window's head start. The funnel survives the worst case as a pipeline asset even if the revenue event moves.

---

## LAYER 6 — FINAL (internal)

Internal Devil's Advocate findings disposition:
- W1, W3, W4, W6 → accepted; handled via placeholders (P1, P3, P7), sensitivity table, and weekly calibration ritual. Not fixable in a document — fixable only with actuals.
- W2 → accepted; Section 5b "Honest read" callout.
- W5 → accepted; referral-at-booking promoted, post-job loop re-scoped as next-window engine.
- W7 → accepted as a known gap; monetized failure-cost modeling recommended as a candidate for a future deliverable (flag to orchestrator — not in current queue).
- Improvements I1–I3 → all applied in Round 2.
- Worst-case → defenses verified present in the FINAL; no new mechanism needed.

**Internal rounds used: 2 of 3. Board verdict: APPROVED WITH NOTES. Status: FINAL.**

---

## EXTERNAL ROUND — INDEPENDENT RED TEAM (2026-07-27) — verdict REVISE (light)

An independent red team returned REVISE (light) with 10 fixes (4 MAJOR, 2 MINOR, 4 cross-document consistency). The orchestrator published `RECONCILIATION_Sheet_2026-07-27.md`, which settles the contested points and supersedes conflicting lines; it is now cited as a source in the FINAL header and added as Ground Rule 6. **All 10 fixes applied; disposition below. No fix was rejected.**

| Fix | Severity | Issue | Disposition |
|---|---|---|---|
| F1 | MAJOR | §5a booking rates applied to "engaged" counts made the 85% "qualified conversation" row decorative (double-count risk) | **Applied — preferred option chosen.** Booking-rate basis relabeled "engaged → booked"; the "Qualified conversation (85%)" row deleted; qualification folded into the engaged→booked rates. Rates were always computed on the engaged basis, so no booking numbers changed (82 booked stands). Explanatory note added to §5a; Stage 2 conversion line rewritten to match. The alternative (recompute from qualified ≈70 bookings, restate gates) was rejected per the fix's own preference and because it would break the OoO gate pacing. |
| F2 | MAJOR | §5b fee line "82 × $695 ≈ $57K" double-counted the 13 converters' credited fees | **Applied.** Now "(82 booked − 13 package buyers) × $695 ≈ $48K," labeled "non-converters only," with explanatory parenthetical. Funnel gross corrected ~$869K → **~$860K**. Honest-read callout updated. |
| F3/X2 | MAJOR | Stage 2 fallback implied an after-hours auto-acknowledgment text | **Applied.** Line replaced: after-hours replies captured immediately, tagged AFTER_HOURS, SLA clock arms 9:00 AM next business day per reconciliation sheet (b); explicit statement that no auto-acknowledgment exists and no automated outbound runs 6:00 PM–9:00 AM CT (opt-out confirmation sole exception). Hard Rule 4 and the mermaid/ASCII charts updated to match. |
| F4/X5 | MAJOR | Anchor table cited "Campaign decision" for gates and 25% floor | **Applied.** Gates now cited to the Order of Operations per reconciliation sheet (e): 80 by Sep 30, <60 = DIAGNOSE floor, checkpoints 40 by Aug 31 / 60 by mid-Sep. 25% labeled a conservative planning floor, not a target. Plain sentence added: the Master Plan's "50%+" ambition was judged unachievable as a plan number; planning at 25%, reviewed weekly. §6 gate table and §7 agenda item 1 restated to the OoO framing; the superseded "40/60/80 by Aug 31/Sep 30/Oct 31" framing removed everywhere. |
| F5 (F8/X-STALE-2) | MAJOR | "until Deliverable 3.3 lands" staleness in §3 header, §10, P10 | **Applied.** All three locations now read: per Deliverable 3.3 (FINAL, 2026-07-27), which supersedes the interim 3-business-day rule (reconciliation sheet (d)). P10 marked RESOLVED. |
| F6 (F5) | MINOR | "Blended CAC $450 — Master Plan Part 2" overstated the source | **Applied.** Anchor row now: "$450 mid-size tier CAC — Master Plan Part 2 (no blended figure in source; blended to be derived from mix)." §2 S4 note, §5c CAC rows, and §7 agenda updated to "mid-size tier" wording. |
| F7 (F6) | MINOR | §6 Gate 1 "≈42 pace" presented as fact | **Applied.** All three model-pace figures in §6 now carry "ramp assumption, uncalibrated" labels. |
| F8 (X4) | Consistency | Booking definition needed the paid-or-held rule explicit | **Applied.** Stage 3 definition now states per reconciliation sheet (a): unpaid = not booked; "pay on site" does not exist; gate counts include only paid-or-held bookings. Stage 3 automation trigger renamed "assessment-payment record" and explicitly distinguished from the Stage 6 package deposit; Stage 6 definition notes the distinction; Hard Rule 8 added; charts updated. |
| F9 (X7) | Consistency | Friday review vs. Monday pipeline review overlap | **Applied.** §7 gains a "Division of labor" block: Friday 4 PM owns throttle/kill decisions, budget shifts, channel emphasis; Monday 8:30 pipeline review (Rulebook) owns the week's dialing plan; Friday feeds Monday, decisions handed over for execution. |
| F10 | Process | REVIEW_NOTES must record this round and drop stale flags | **Applied.** This section added; stale "confirm 3.3 is queued" orchestrator flag deleted (3.3 exists and is FINAL); gate framing, CAC wording, rounds count, and fee figures corrected throughout these notes; worst-case fee figure updated to $48K. |

**Additional consistency sweeps made while applying the fixes (no new content, alignment only):** Stage 1 fallback/automation lines now note manual sends until automation L3 and the first-hour inbound watch (reconciliation sheet, Day-1 manual operations); Stages 4–5 note Sequence C fires manually until L3 per sheet (c); §9 P9 retargeted from "Gate 2 (Sep 30)" to "the Sep 30 gate."

**External round disposition: 10/10 fixes applied, 0 rejected, 0 deferred. Round 3 of 3 — at cap. Status: FINAL (rev. 2026-07-27).**

---

## PLACEHOLDER LIST (carried in the FINAL, Section 9)

P1 actual list counts (Harper/Lucas, before Jul 27) · P2 live counters (Mon/Thu) · P3 paid budget line (Nathan) · P4 HOA group terms in writing (Nathan) · P5 grouped-jobs-first confirmation (Ops Lead) · P6 rep numbers/sender ID (Jul 27 EOD) · P7 conversion baselines from actuals (Friday ritual) · P8 hold-release policy terms (Sales Lead) · P9 waitlist terms/language (Nathan + Ops) · ~~P10~~ RESOLVED per Deliverable 3.3 (FINAL, 2026-07-27)

## FLAGS TO ORCHESTRATOR

1. Failure-cost modeling (no-shows, released holds, slipped jobs) has no owner in the current deliverable queue — candidate for a batch-3 addendum. *(Unchanged from internal round.)*
2. ~~Confirm 3.3 is queued~~ — **withdrawn**: Deliverable 3.3 exists (FINAL, 2026-07-27); reconciliation sheet (d) confirms its per-stage SLAs supersede the interim 3-business-day rule. No action needed.

---

*Review Notes v1 FINAL (rev. 2026-07-27, external red-team round applied) | Deliverable 3.1 | DRAWDOWN 2026 | ATX Lakescapes — Confidential, internal use only*
