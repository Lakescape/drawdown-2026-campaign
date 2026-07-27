# DRAWDOWN 2026 — EMAIL SEQUENCE SUITE: REVIEW NOTES
## Companion to COPY_EmailSequenceSuite_v1_FINAL.md (Deliverable 1.3)

Version: v1 FINAL | Date: 2026-07-26 | Author: Swarm | Status: FINAL

---

## 1. WHAT CHANGED FROM THE SOURCE DRAFT (Sales Copy Suite §1)

The source draft was a starting point, not a finish. Material changes:

1. **Deleted the invented "47 machine-days / 31 spoken for" email (source B3).** Those numbers predate the real-numbers rule. Replaced with the approved structural scarcity: 2 amphibious machines locked, ~25 working days. The B3 subject is now built from the true numbers.
2. **Re-anchored the entire calendar to Day 1 = Mon Jul 27, 2026, 10:00 AM CT** (updated execution calendar). The source had undated relative days; the FINAL has a date-anchored, send-window-compliant table (no weekends, 9 AM–6 PM, Monday ≥10 AM).
3. **Hedged all drawdown language.** Source B1 said "Lake Austin is dropping 10 feet" — an assertion. Bodies now use "the City and LCRA are exploring" / "lined up" / "projected." *(Correction recorded in §7: the internal round missed one unhedged line — the A1 Subject A/B — so "throughout" was not true at first FINAL. Fixed in the external round.)*
4. **Removed invented specificity:** source A2's "I'm holding 2 slots open for [Cove Name] residents" (invented number) → 48-hour hold language consistent with the approved Call Script. Source B1's "most important 6 weeks of the decade for your property value" (hype) → cut.
5. **Added A4 ALT variant + conditional-send gate** so the waitlist email only claims "full" when the wave is actually full.
6. **Added waitlist-integrity note** resolving the A4 (past-client, Aug 10) vs. B4 (cold, "after Friday Aug 14") cutoff divergence — different lists, different real cutoffs.
7. **Added compliance and deliverability usage rules** (list basis, domain warming, batching, suppression shared with the SMS suite) — absent from the source.
8. **Added a kill-switch pivot email** mirroring the SMS suite's pivot text (risk register: drawdown delayed/cancelled = low probability, critical impact).
9. **Added C2's second finding and C3's truth-gate** on "another client is waiting" — fake urgency removed by rule, not by hope.
10. **Aligned with the Master Call Script:** 48-hour holds, "either way you win" framing, 12-month credit validity, 15–25% deposits, referral-program silence before October.

---

## 2. SKILL POLL — LAYER 2 (6 agents, simulated)

| Agent | Vote | Key note |
|-------|------|----------|
| Creative Director | STRONG | "One job per email is honored. A1 reads like a neighbor with news, not a campaign." |
| Copywriter (self-audit) | ACCEPTABLE | Round-1 draft's B1 leaned on "rare opportunity" framing — too close to hype. Revised to lead with who Nathan is and why the email exists. |
| Media Strategist | ACCEPTABLE | Wanted deliverability rules (batching, domain warming, plain-text) — added as Usage rules 1–2. |
| Sales Engineer | STRONG | "Funnel logic matches the call script: hold mechanics, credit terms, deposit deadlines all consistent. Conditional A4 prevents a false 'full' claim." |
| QA / Devil's Advocate | STRONG | "Invented numbers are gone. The C3 truth-gate is the right way to kill fake urgency." |
| Board Reviewer | STRONG | "Passes the $5M-homeowner read test. Calm, specific, no desperation." |

**Result: 4 STRONG / 2 ACCEPTABLE → met the 4+ STRONG threshold after one revision round** (revision addressed the Copywriter and Media Strategist notes in full: B1 opener rewritten; Usage rules 1–2 added).

**Revision rounds used: 1 of 3.**

---

## 3. BOARD REVIEW MEMO — LAYER 4

**Verdict: APPROVED WITH NOTES** (all notes applied to FINAL)

1. *Note 1 — Anchor conflict:* "The SMS suite still shows Aug 6 dates. The email file must not silently diverge." → Applied: anchor-shift note placed directly under the calendar table, flagged to the orchestrator; the other writer's file was not touched.
2. *Note 2 — A4 honesty:* "'Slots are full' is a factual claim." → Applied: A4 is conditional, A4 ALT provided, standup confirmation required.
3. *Note 3 — Sequence C:* "These three emails make the money. Their data fields need the same discipline as SMS C2." → Applied: [Finding]/[Deposit]/[Date] filled from the client file only; email doesn't send without the report in hand.

**Board standard applied:** would this impress a $5M homeowner? The emails assume intelligence, state real constraints, offer a clean exit (B1/B4 "reply NO"), and never beg. Yes.

---

## 4. DEVIL'S ADVOCATE RED TEAM — LAYER 5

### Five specific weaknesses (found and dispositioned)

1. **A3's "as of this morning's count" is only as true as the rep's discipline.** If a rep reuses Monday's number on Thursday, the claim is stale and the scarcity becomes fake. → *Mitigation:* Usage rule 4 + placeholder table make the standup count a send-time requirement; sales lead owns the number.
2. **A4 and B4 reference different waitlist cutoffs four days apart.** A homeowner on both lists (past client also on the cold list) could spot the divergence and read it as manipulation. → *Mitigation:* waitlist-integrity note + shared suppression list; cutoffs confirmed per list at the Aug 6 standup.
3. **B1 from Nathan's personal address at cold-list volume risks sender-reputation damage** right before the money sequence (C) depends on inbox placement. → *Mitigation:* Usage rules 1–2 (list basis, domain warming, batching); Day-1 shift option if the domain isn't warm.
4. **C3's "another client is waiting on that equipment day" is a specific factual claim** — the single easiest place for fake urgency to creep back in. → *Mitigation:* Usage rule 5 truth-gate: if it isn't literally true, the sentence is cut before sending.
5. **A5's "reply EARLY for next-window priority" presumes goodwill after a non-conversion.** If the drawdown slips entirely, a "how did your shoreline fare" email could read as tone-deaf. → *Mitigation:* A5 is event-anchored and hedged ("whenever the next window comes… could be years"); kill-switch email supersedes it if the window moves.

### Three concrete improvements (applied)

1. **Added the kill-switch pivot email** (Usage rule 8) — the source suite had no answer for a delayed drawdown mid-sequence.
2. **Added A/B subject lines for all 12 emails** so the team can test toward the 40%+ open target instead of guessing.
3. **Added the A4 ALT variant** — converts a potential false claim into an honest "last call" with a confirmed Friday cutoff.

### One worst-case scenario

**The drawdown is cancelled in mid-August, after A3/B3 have sent the real-numbers scarcity emails.** Owners who booked feel the urgency was manufactured; "2 machines, 25 days" becomes evidence against us at the country club. *Contained by:* (a) every scarcity claim is structurally true regardless of the window (machines really were committed in July — that's the risk we took, and it's honest to say so); (b) the kill-switch email leads with "nothing is lost — your assessment and credit carry over," making early movers whole; (c) the 12-month credit is the financial proof that moving early cost nothing. The campaign's defense is that it never asserted the drawdown was certain — which is exactly why the hedged-language rule exists.

---

## 5. FINAL DISPOSITION — LAYER 6

- Board verdict: **APPROVED WITH NOTES** — all notes applied.
- Red-team improvements: **3 of 3 applied**; 5 weaknesses dispositioned with mitigations written into the Usage block (rules 1, 2, 4, 5, 6, 8).
- Revision rounds used: **1 of 3** (internal round only — superseded by the cumulative count in §7 after the external red-team round).
- Cross-file consistency check vs. COPY_CallScript_Master_v1_FINAL and COPY_SMS_SequenceSuite_v1_FINAL: offer terms ($695, 100% credit, 12-month validity), hold mechanics (48 hours), deposit range (15–25%), scarcity numbers (2 machines / ~25 days), referral-program silence, opt-out dignity — **all consistent.** *(Qualified in §7: SMS-suite alignment is conditional on its pending re-anchor + hedging fixes, being handled by its writer in parallel.)*

## 6. OPEN FLAGS FOR THE ORCHESTRATOR

1. **SMS suite re-anchor:** COPY_SMS_SequenceSuite_v1_FINAL.md still shows the Aug 6 Day-1 calendar. It needs re-anchoring to Mon Jul 27, 10:00 AM (owned by another writer — flagged, not modified).
2. **One-page summary asset** (offered in B1): text exists in the Warm List Sales Machine §1, but a designed printable asset is unowned in the deliverable queue. Same gap flagged by the Call Script writer — add it to the queue.
3. **Standup confirmations needed (Aug 6 standup or earlier):** per-list waitlist cutoffs, 60-day cold re-blast policy, sending-domain warm status, live count publication process.
4. **Report-template taxonomy:** C1's priority levels (Critical / Soon / Monitor / OK) match the source Sales Copy Suite, but the owner of the assessment report template must confirm that taxonomy before C1 first sends (external finding F7).

---

## 7. EXTERNAL RED-TEAM ROUND (independent review, 2026-07-26)

**Verdict: REVISE — 5 findings, no blockers. All fixes applied to the FINAL file.**

| # | Finding | Severity | Fix applied |
|---|---------|----------|-------------|
| F4 | A1 Subject A/B "The lake drops this fall — you're getting this before anyone else" was an unhedged assertion with a flat date — violating Global Rule 2 and falsifying this file's own "hedged throughout" claim | MAJOR | Subject A/B replaced with "A drawdown is being lined up for this fall — past clients hear it first" |
| F5 | A2's social-proof claims ("your neighbors are booking," "[X] past clients have booked since Monday") had no truth-floor gate | MAJOR | Usage rule 6a added: A2 sends only if the Thursday Jul 30 standup count shows ≥5 booked past-client Assessments; below that, A2 ALT sends (new ALT written — subject "the first assessments are on the calendar," body identical minus the count sentence) |
| F6 | Event-anchored C2 "Day 3" / C3 "Day 7" could land on weekends | MINOR | Usage rule 6b added: event-anchored sends landing Sat/Sun shift to the following Monday 10:00 AM (C1 Day 0 excepted — it fires within 60 minutes of report delivery) |
| F7 | C1 taxonomy "Critical / Soon / Monitor / Sound" diverged from the source suite's "OK" | MINOR | "Sound" → "OK," plus a verification note against whoever owns the assessment report template |
| F8 | A2 P.S. "that's the order this always goes in" implied drawdown-campaign experience ATX has never had | MINOR | Changed to "that's the order it goes in" |
| — | Placeholder table phone-line dates | — | Updated to the campaign-wide decision: Nathan's direct line live by Jul 26; rep direct lines by Jul 27 EOD (supersedes earlier dates) |

**Correction to the record:** §1 item 3 of these notes originally claimed hedging was applied "throughout." The external review proved that false — the A1 Subject A/B was an unhedged assertion. The claim is corrected in §1, and the miss is recorded here rather than edited away.

**Revision rounds used (cumulative):** 2 of 3 (1 internal poll-driven + 1 external red-team).

**Cross-file consistency — now qualified:** the §5 consistency statement stands for offer terms, holds, deposits, scarcity numbers, and referral silence vs. the Call Script. Consistency with the SMS suite is **conditional on that suite's pending re-anchor to Jul 27 and its own hedging fixes, which its writer is handling in parallel** — until that file lands its update, treat calendar and language alignment across the two files as provisional.

**Updated disposition:** FINAL stands. External findings were quality-floor issues (truth-gates, hedging, taxonomy), not structural — no rewrite required, no third round anticipated.

---

*COPY_EmailSequenceSuite_v1_FINAL_REVIEW_NOTES | ATX Lakescapes | Confidential — Internal Use Only*
