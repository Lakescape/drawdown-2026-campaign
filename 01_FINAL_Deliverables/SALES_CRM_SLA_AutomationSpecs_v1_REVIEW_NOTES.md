# DRAWDOWN 2026 — CRM AUTOMATION + SLA SPECS
## Deliverable 3.2 — REVIEW NOTES (6-Layer Pipeline Record)

Version: v1 FINAL
Date: 2026-07-27
Author: DRAWDOWN 2026 Swarm — Sales Engineer writer agent
Revision rounds used: **3 of 3** (Round 1: Skill Poll + revision; Round 2: Devil's Advocate + final revision; Round 3: independent external red team, verdict REVISE — 7 findings incl. 1 near-blocker, all applied per RECONCILIATION_Sheet_2026-07-27.md)
Board verdict: **APPROVED WITH NOTES** (no launch blockers; external-round near-blocker C1 resolved by the Pre-L3 manual send ownership subsection; placeholders tracked in §8 of the FINAL)

---

## LAYER 1 — DRAFT

Draft built against four mandatory sources, reconciled before writing:

1. `DRAWDOWN_2026_Master_Attack_Plan.md` — 8 Kanban stages, $695 credited assessment, 15–25% deposits, capacity floor/target/stretch, team ownership.
2. `DRAWDOWN_2026_Order_of_Operations.md` — tooling deadlines (Slack Aug 3, CRM import Aug 3, Calendly Aug 5, first counters Aug 5), "AI builds, humans execute" rule.
3. `COPY_SMS_SequenceSuite_v1_FINAL.md` — Reply YES only CTA, GSM-7, opt-out protocol (single 48-char confirmation, permanent suppression), kill-switch pivot text, send windows, 60-day re-blast policy (pending Nathan Aug 5), Day 1 = Mon Jul 27, 2026.
4. `SLACK_SALES_BOARD_SETUP.md` (Google Drive) — 6 channels, `#drawdown-inbound` first landing, 👀 claim, 5-min escalation to Nathan, 7 pinned stage posts, pinned Mon/Thu counters by Harper/Lucas, 6:00 PM Linear rule, "reps quote only the pin."

Also cross-read for consistency: `COPY_EmailSequenceSuite_v1_FINAL.md` (12-email calendar, hedged language, A4 conditional, A2 truth-floor, shared suppression, kill-switch pivot email, referral-silence rule).

**Reconciliation decisions made in the draft:**
- Slack channel structure follows the Drive board spec (6 channels), which supersedes the older 3-channel list in the Order of Operations.
- Kanban uses the Master Plan's 8 stages; the Slack board's 7 pinned posts map with `scheduled-for-drawdown` riding on the DEPOSIT RECEIVED post (noted in §3).
- Opt-out confirmation is the single exception to "no automated outbound at night" — compliance duty beats the quiet-hours rule (§2).

---

## LAYER 2 — SKILL POLL (6 roles, verdicts)

| Role | Verdict | Key note |
|---|---|---|
| Sales Engineer (systems) | STRONG | Event catalog is complete for the four inbound classes + three lifecycle events; idempotency/dedupe specified. |
| Deliverability & Compliance Lead | STRONG | GSM-7 at queue time, batch 40–50 staggering, 10DLC gate on Sequence B, opt-out honored immediately at any hour, suppression checked at send time not queue time. |
| Sales Rep (floor user) | STRONG | Claim mechanics are ungameable (first valid 👀 only); after-hours leads surface at standup before their clock starts; nothing asks a rep to quote a number that isn't on the pin. |
| Ops Lead (capacity owner) | STRONG | Automation computes draft counters only; ops owns the math; deposit → machine-day decrement moves only what the Drive capacity sheet says. |
| Nathan as CEO (edge case) | ADEQUATE → STRONG after fix | Asked: "What stops automation from texting a $5M homeowner at 11 PM?" — quiet-hours rule made absolute with the single compliance exception; kill-switch cannot self-trigger. |
| QA / Devil's Advocate seat | ADEQUATE → STRONG after fix | Demanded explicit "NEVER automated" list and Asana-parked enforcement — both added as hard rules. |

**Result: 6 roles polled, 4+ STRONG after Layer-3 fixes → gate passed.**

---

## LAYER 3 — REVISION (Round 1 applied)

- Added §4 "NEVER automated" hard list (7 items: calls, proposals, voicemail drops, live numbers, reply answering, pre-window referral credit, Asana writes).
- Made quiet-hours absolute (6 PM–9 AM CT) with the opt-out-confirmation exception stated explicitly.
- Added kill-switch self-trigger ban (human judgment only).
- Added asset-linter CI rules (smart quotes, blocked "47 machine-days" line, unhedged drawdown verbs).
- Added Slack-outage SLA pause (can't claim what you can't see).

---

## LAYER 4 — BOARD REVIEW MEMO (to Nathan)

**What this spec is:** the complete automation contract for the sales floor — every trigger, the 5-minute SLA machine, tagging, which automation may fire which FINAL asset, scoring, ledger discipline, and the Railway/Mastra + Inngest build path.

**What Nathan must personally decide (4 items):**
1. 60-day cold-list re-blast policy — confirm at Aug 5 standup (inherited from SMS suite placeholders; written in non-imperative voice in §5 until confirmed).
2. ~~After-hours 9:00 AM arm vs. 8:00 AM standup ordering~~ — **DECIDED by reconciliation sheet (b), 2026-07-27:** SLA business hours 9:00 AM–6:00 PM Mon–Fri; after-hours clocks arm 9:00 AM next business day; no automated outbound 6 PM–9 AM ever (opt-out confirmation sole exception); no auto-acknowledgment text. Removed from the decision list and the placeholder table.
3. Deposit receipt source: payment-processor webhook vs. ops manual entry — by Aug 15.
4. Kill-switch authority — spec restricts activation to Nathan only; confirm that's the intent (recommended: yes).

**What is deliberately NOT in this spec:** Kanban entry/exit criteria and per-stage SLAs; commission automation; field-ops scheduling. Per reconciliation sheet (d), per-stage SLAs now govern via the Slack Board Rulebook (Deliverable 3.3, FINAL 2026-07-27) — the interim 3-business-day touch rule is superseded and the "until 3.3 lands" framing is stale.

**Risk flagged to the board:** the largest dependency is human, not technical — 10DLC approval and B-list consent documentation before Jul 27. If it slips, Sequence B falls back to calls + door hangers per SMS Usage rule 1; the automation spec already supports that (Sequence B simply never arms).

---

## LAYER 5 — DEVIL'S ADVOCATE RED TEAM

**Verdict: REVISE** (6 weaknesses, 3 improvements, 1 worst-case; no launch blockers — all applied in Round 2).

### Weaknesses found (6)

- **W1 — SLA clock vs. standup race.** An 11 PM hot YES arms at 9:00 AM, but standup is 8:00 AM — the team could discuss it before its clock exists. *Fix (Round 2):* §2 after-hours note made the ordering explicit and routed it to Nathan. *Final resolution (external round):* reconciliation sheet (b) settled it — SLA business hours 9:00 AM–6:00 PM Mon–Fri, clocks arm 9:00 AM next business day, no auto-acknowledgment; the 8:00 AM line and the confirm-with-Nathan placeholder were removed from the FINAL.
- **W2 — Claim gaming / fat-finger.** A rep could 👀 then ignore. *Fix:* first-valid-reaction-only, threaded claim receipt with MET/MISSED stamp, 15-min FOLLOWUP_NUDGE on claimed-but-open cards, weekly per-rep claim metrics.
- **W3 — Classifier edge: sarcastic "YES".** A cold lead replying "YES, leave me alone" would get treated as a hot lead and an opt-out simultaneously. *Fix:* rules-first classifier with `OTHER` fallback that always errs toward a human; opt-out keywords dominate YES when both present (opt-out checked first).
- **W4 — Draft-counter leak.** If the Mon/Thu draft derivation were posted publicly, reps would quote unpublished numbers. *Fix:* draft goes to Harper/Lucas as **DM only**; the pin is the sole quotable surface (§6.2).
- **W5 — Deposit webhook spoofing.** A forged deposit event would post a fake 💰 to `#drawdown-won` and corrupt capacity. *Fix:* processor signature verification required; manual-entry path restricted to ops user IDs; any deposit event without valid signature is quarantined to war-room for human confirmation.
- **W6 — Weekend event-anchored C1.** C1 sends within 60 minutes of report delivery regardless of day — a Saturday report means a Saturday text. This is inherited from the FINAL suites (intentional exception). *Fix:* documented as inherited behavior, not changed here; flagged so nobody "fixes" it in code later.

### Improvements proposed (3) — all applied

- **I1:** Idempotency keys now include channel prefix (`twilio:`, `resend:`…) to prevent cross-channel ID collisions.
- **I2:** 10-minute threading window added — a second inbound from the same contact threads onto the existing SLA card instead of double-posting.
- **I3:** Send-time suppression check (not just queue-time) added — a contact who opts out between queue and send never receives the asset.

### Worst-case scenario (1)

**Scenario:** Twilio webhook endpoint silently down during the Jul 27 10:00 AM A1/B1 blast — YES replies pile up unseen for hours, the 5-minute SLA is breached at scale on day one, and hot past-client leads go cold while the floor looks empty.
**Mitigations in spec:** (a) L2 shadow mode (48 h) runs before any live cutover; (b) Twilio-side outage → events buffer and replay in order, SLA clocks pause during detected Slack/Twilio outage; (c) a daily webhooks-alive heartbeat to war-room before the 10:00 AM send window — a silent morning blocks the day's blast at the human gate. **Honesty correction recorded in the external round:** at the time this was written, mitigation (c) and the first-hour human watch below were claimed here but were NOT actually present in the FINAL file — the two claim-vs-file gaps the external red team caught (C2 and part of C1). Both are now genuinely in the spec: `fn.heartbeat` exists in the §7 function table + §7 failure modes + a §2 monitoring subsection, and the first-hour watch is a hard rule in §7 "Pre-L3 manual send ownership." **Residual risk accepted:** the first blast day gets a human watching `#drawdown-inbound` continuously for the first hour (standup agenda item Jul 27 — now codified as "First-hour watch" after EVERY blast, not just day one).

---

## LAYER 6 — FINAL (Round 2)

Round-2 revision applied W1–W6, I1–I3, and the worst-case mitigations. Spec re-verified against all four source docs for drift (dates, channel names, counter owners, opt-out string, kill-switch assets, send windows) — clean. Round 3 was initially judged unnecessary — **that judgment was wrong about claim-vs-file fidelity** (see the external round below): two mitigations recorded here as "in spec" were not actually in the FINAL file. Process fix adopted: every "applied" claim is now verified against the FINAL file line-by-line before this document ships (see the verification table in the external round section).

---

## EXTERNAL RED-TEAM ROUND (2026-07-27) — independent reviewer, verdict REVISE (1 near-blocker)

The orchestrator published **RECONCILIATION_Sheet_2026-07-27.md**, which settles the contested points and supersedes any conflicting line in this deliverable. All 7 findings applied; the sheet is now cited in the FINAL header.

| # | Severity | Finding | Fix applied in FINAL (verified location) |
|---|---|---|---|
| C1/X1 | **Near-BLOCKER** | Manual send ownership unspecified — the spec implied the Inngest scheduler fires the Jul 27–Aug 13 calendar, but automation isn't live until L3 (mid-Aug), by which point the calendar is over | New §7 subsection **"Pre-L3 manual send ownership"**: every scheduled send Jul 27–Aug 13 (SMS A1–A5, B1–B4; email waves A/B; Sequence C touches) is sent MANUALLY from the platform by the list-owning rep (backup: Nathan) with the same gates (10DLC, suppression, A2 truth-floor); explicit note that the FINAL calendar ends Aug 13 so "remaining sends" at L3 = none — L3 arms future/event-driven automation only; **first-hour human watch on `#drawdown-inbound` after every blast** codified. Matching edits: §4 ownership note, L3 bullet rewritten, `fn.sequence-scheduler` row re-scoped to post-L3 only (reconciliation sheet, "Day-1 manual operations" + (c)) |
| C2 | MAJOR | Heartbeat claimed in REVIEW_NOTES but missing from the FINAL — a silently dead webhook on a blast day had no written detection | `fn.heartbeat` added to the §7 Inngest function table (cron `50 9 * * *`, 9:50 AM CT daily), a "Silent webhook death" bullet in §7 failure modes, and a §2 "Monitoring — heartbeat" subsection: webhooks-alive check posted to war-room before 10:00 AM; a silent morning blocks that day's batch release at the human gate. The notes' claim is now true. |
| C3 | MAJOR | Hours contradiction: 8:00 AM business-hours line vs. 9:00 AM arm time, plus an open "confirm with Nathan" placeholder | Per reconciliation sheet (b): §2 after-hours rule now reads SLA business hours **9:00 AM–6:00 PM Mon–Fri**, clocks arm 9:00 AM next business day, no automated outbound 6 PM–9 AM ever (opt-out confirmation sole exception), no auto-acknowledgment text. The 8:00 AM line and the 8-vs-9 placeholder (§8 and board memo item 2) removed — decided, not pending. |
| C4 | MINOR | T-01 `NO` class left the Branch 1F follow-up email unowned | One line added to the T-01 `NO` row: "The Script Branch 1F follow-up email is sent manually by the rep (no automation)." |
| C5 | MINOR | §6.2 had no fallback if Mon/Thu draft counters go unverified by standup | Fallback bullet added to §6.2: standup reads the previous pin and states so explicitly; the pin updates after verification, never before. |
| C6 | MINOR | 60-day re-blast gate written in imperative voice while still unconfirmed | §5 gate rewritten as "pending Nathan confirmation at the Aug 5 standup — not yet policy"; no nurture re-blast scheduled at all until confirmed; §8 placeholder row annotated accordingly. |
| C7 | MINOR | Jobber appeared in the system map without provenance, blurring the approved stack | Provenance note added under the §0 table: Jobber = field CRM from Nathan's production stack; not part of the campaign's approved ground-rule stack — listed for completeness. |

### Claim-vs-file verification (process fix — every "applied" claim checked against the FINAL)

| Claim in these notes | In FINAL? | Where |
|---|---|---|
| Pre-L3 manual ownership + first-hour watch | ✅ YES | §7 "Pre-L3 manual send ownership"; §4 ownership note |
| `fn.heartbeat` daily webhooks-alive check | ✅ YES | §7 Inngest functions table; §7 failure modes; §2 Monitoring subsection |
| SLA hours 9 AM–6 PM; no 8:00 AM line; no 8-vs-9 placeholder | ✅ YES | §2 after-hours rule; §8 table (row removed) |
| Branch 1F manual follow-up on NO | ✅ YES | §1 T-01 `NO` row |
| Unverified-counter fallback | ✅ YES | §6.2 fallback bullet |
| 60-day gate in pending/non-imperative voice | ✅ YES | §5 dead-lead detection; §8 annotation |
| Jobber provenance note | ✅ YES | §0, beneath system map table |
| First-valid-👀-only claim detection (Round 2) | ✅ YES | §2 claim detection |
| 10-minute threading window (I2) | ✅ YES | §1 idempotency rules |
| Send-time suppression check (I3) | ✅ YES | §3, final line |
| DM-only draft counters (W4) | ✅ YES | §6.2 |
| Deposit signature verification / quarantine (W5) | ✅ YES — *gap caught during this very verification pass: the quarantine language was still missing from the FINAL despite the Round-2 "applied" claim; added now* | §1 T-07 step 4 (anti-spoofing quarantine); §7 webhook endpoints table (processor signature) |
| Reconciliation sheet cited as source of authority | ✅ YES | FINAL header, "Cited source of authority" line + footer "Pairs with" |

**Round-3 verdict after fixes: PASS — near-blocker C1 closed, both MAJORs closed, all MINORs closed, zero remaining claim-vs-file gaps.**

## PLACEHOLDER LIST (carried to FINAL §8 — after external round)

1. `slack_bot_token` + app scopes — Ops Lead, Aug 1
2. Twilio 10DLC approval + B-list consent basis — Nathan/Ops, **before Jul 27**
3. Linear API key + custom fields — Ops Lead, Aug 3
4. Website chat platform identity + webhook secret — Ops Lead, Aug 8
5. Calendly webhook signing key — Ops Lead, Aug 5
6. Deposit payment source (webhook vs. manual) — Nathan, Aug 15
7. Rep roster Slack user IDs — Ops Lead, Aug 1
8. 60-day cold-list re-blast policy (pending — not policy until confirmed) — Nathan, Aug 5 standup
9. Lead-score weights + P1–P4 thresholds (UNCALIBRATED) — Sales lead, Aug 14
10. High-value cove list — Ops Lead, Aug 8
11. Jobber API credentials + draft-job mapping — Ops Lead, Aug 15

*(Removed after the external round: the after-hours arm-vs-standup ordering placeholder — decided by reconciliation sheet (b).)*

---

*SALES_CRM_SLA_AutomationSpecs_v1_REVIEW_NOTES | ATX Lakescapes | Confidential — Internal Use Only*
