# DRAWDOWN 2026 — SMS SEQUENCE SUITE
## Deliverable 1.2 — 12 Texts: Past Client (5) + Cold Lead (4) + Post-Assessment (3)

Version: v1 FINAL (2 external red-team rounds applied)
Date: July 24, 2026
Author: DRAWDOWN 2026 Swarm — Copywriter (Agent 2), Board Reviewed (Agent 6), Red Teamed (Agent 5) + Independent External Devil's Advocate
Status: FINAL — APPROVED WITH NOTES; EXTERNAL RED-TEAM ROUNDS 1 and 2 (both verdict REVISE, incl. 2 blockers) fully applied — see COPY_SMS_SequenceSuite_v1_FINAL_REVIEW_NOTES.md

---

## GLOBAL RULES (READ BEFORE SENDING)

1. **Reply YES is the only CTA.** No links in outbound texts. Links go out only after a reply, in a 1:1 thread, from the rep.
2. **Every customer-facing text in this file — sequences, opt-out, kill-switch — must pass a GSM-7 check inside the sending platform before any send.** Do not paste in smart quotes from a word processor — that silently re-breaks this.
3. **Character counts** below are raw counts including bracketed placeholders. Worst-case rendering (10-letter first name + max-length field fills per the placeholder table) verified under 160 for every text, including the opt-out confirmation and the kill-switch pivot. Do not lengthen any text without re-counting.
4. **Scarcity is structural, not invented.** A3 uses the real capacity model: 2 amphibious machines locked, ~25 productive days (target case, Operations Playbook). No made-up "X slots left" numbers appear anywhere in this suite.
5. **First blast: Day 1 = Monday, July 27, 2026, 10:00 AM CT** (campaign calendar decision — supersedes the earlier Aug 6 anchor). Date-anchored calendar for sequences A and B:

| Text | Date | Time |
|------|------|------|
| A1 / B1 | Mon Jul 27 | 10:00 AM |
| A2 | Fri Jul 31 | 10:15 AM |
| B2 | Mon Aug 3 | 10:15 AM (Day+5 landed Sat Aug 1 — weekend shift per Usage Block rule 8) |
| A3 | Mon Aug 3 | 10:00 AM (Monday rule: 10:00 AM or later; staggered before the B2 batch) |
| B3 | Fri Aug 7 | 4:40 PM |
| A4 | Fri Aug 7 | 5:05 PM (staggered after the B3 batch) |
| A5 / B4 | Thu Aug 13 | 10:00 AM (held to Thursday per Usage Block rule 5 — "after Friday" = Aug 14, the claim stays true) |

Sequence C is event-anchored (Day 0 = assessment report delivery), not calendar-anchored.

---

## SEQUENCE A — PAST CLIENT REACTIVATION (5 texts)

Audience: Lake Austin owners we have already worked for. These people know us. Sound like it.

**A1 — Mon Jul 27, 10:00 AM** (first touch; pairs with the same-day personal email)
> Hey [First], Nathan at ATX Lakescapes. Lake Austin's first drawdown in a decade is projected for Oct-Nov. Past clients book first. Reply YES to hold one.

Character count: 153

**A2 — Fri Jul 31, 10:15 AM** (non-responders only)
> [First], we worked your shoreline before, so you know what's under that water. The assessment is $695, fully credited. Reply YES and I'll save you a slot.

Character count: 154

**A3 — Mon Aug 3, 10:00 AM** (non-responders; the structural-scarcity text — verify equipment status before sending, see Usage Block rule 4; staggered before the B2 batch)
> [First], 2 amphibious machines locked and 25 working days this window. Once those days are booked, we're done. An assessment locks your place. Reply YES.

Character count: 153

**A4 — Fri Aug 7, 5:05 PM** (non-responders; late-day send, reads like a thought Nathan had on the dock; staggered after the B3 batch)
> No pressure, [First]. Didn't want you hearing about the drawdown from a neighbor in Oct. $695, credited, tells you what you're dealing with. Reply YES.

Character count: 151

**A5 — Thu Aug 13, 10:00 AM** (final; lands on a Thursday so "after Friday" is true tomorrow)
> Last note from me, [First]. We waitlist new assessments after Friday. Reply YES if you want in; otherwise I'll check back after the window. Nathan

Character count: 146

(After A5: silence. No sixth text. They move to the post-window nurture track per the Operations cadence.)

---

## SEQUENCE B — COLD LEAD (4 texts)

Audience: Lake Austin waterfront owners with no prior relationship. Highest deliverability and legal risk in the suite — see Usage Block rules 1-3 before this sequence goes anywhere.

**B1 — Mon Jul 27, 10:00 AM** (first touch; identity-first opener so it never reads as spam)
> Hi [First], Nathan Menkin here. My crew works these shorelines. The lake could drop 10+ ft this Oct-Nov, first time in a decade. Worth a look? Reply YES.

Character count: 153

**B2 — Mon Aug 3, 10:15 AM** (non-responders; the education text; shifted off the weekend per Usage Block rule 8)
> [First], most owners don't know their bulkhead is failing until the water drops and shows it. A $695 assessment, fully credited, gives answers. Reply YES.

Character count: 154

**B3 — Fri Aug 7, 4:40 PM** (non-responders; the commitment text — only send once the machines are actually locked, see Usage Block rule 4)
> [First], we locked our amphibious machines back in July. Slots go to past clients and referrals first. Reply YES and I'll hold one.

Character count: 131

**B4 — Thu Aug 13, 10:00 AM** (final; lands on a Thursday)
> [First], last note. New assessments go to waitlist after Friday. Reply YES if you want your shoreline checked before the water drops. Nathan, ATX Lakescapes

Character count: 156

(After B4: full stop. Cold non-responders move to low-frequency nurture. Do not re-blast this list for 60 days — new policy, Nathan to confirm at Aug 5 standup.)

---

## SEQUENCE C — POST-ASSESSMENT FOLLOW-UP (3 texts)

Audience: completed assessments. These texts convert reports into deposits. Every field must come from the client's actual file. (Event-anchored sends that land on a weekend shift to Monday 10:00 AM — Usage Block rule 8.)

**C1 — Day 0, within 60 minutes of the report email landing** (the ping that gets the report opened)
> [First], your shoreline report is in your inbox: photos, scope, pricing. Your $695 is credited. Reply YES and we'll set a time to walk through it.

Character count: 146

**C2 — Day 3, 10:15 AM** (if no response to the report; [Finding] must be the single most important line from THEIR report — never a generic word like "bulkhead," see Usage Block rule 6)
> [First], one thing from your report I'd handle first: [Finding]. Happy to talk. Your slot holds until [Date]. Reply YES to chat.

Character count: 128

**C3 — Day 7, 9:50 AM** (if no deposit; [Date] = the actual Friday, [Deposit] = actual figure from their proposal, typically 15-25% of package)
> [First], deposit due [Date] holds your equipment day; another client is waiting on it. $[Deposit] locks your dates. Reply YES and I'll send the link.

Character count: 149

---

## OPT-OUT HANDLING (NON-NEGOTIABLE)

- Any reply of STOP, UNSUBSCRIBE, REMOVE, or "take me off your list" in any wording is honored immediately — no exception, no "one more text."
- Send exactly one confirmation, nothing else: "You're off the list. Sorry to bother you. Nathan" (48 chars)
- Log the suppression in the CRM so no future sequence (including 2027) touches that number.
- YES replies, questions, and everything else route to a human rep within the 5-minute SLA. No automated follow-up ever answers a reply.

## HOW TO RUN THIS SEQUENCE (USAGE BLOCK)

1. **Compliance first (cold sequence especially).** Confirm 10DLC registration is approved and every number on the B-list has a documented consent basis before July 27. TCPA exposure on a cold SMS to a $5M homeowner is the single biggest legal risk in this campaign. If consent basis is unclear for any segment, that segment gets calls and door hangers instead — not texts.
2. **Deliverability.** Never blast 200+ identical texts in one hour. Stagger sends in batches of 40-50 across the morning, and rotate the hand-written variants each rep keeps (every rep should personally rephrase A1/B1 in their own voice — same beats, different words). Identical high-volume fingerprints are how carriers filter you. Rep rewrites must be typed directly into the SMS platform and re-validated for GSM-7 before queueing — never composed in Word/Notes/iMessage.
3. **Reply triage.** YES → rep calls within 5 minutes. Question reply ("how long does it take?") → rep answers personally, sequence pauses. NO → suppress and tag. Silence after the final text → nurture bucket, no further chasing.
4. **Verify scarcity before every send.** A3 assumes the target capacity case (2 amphibious machines locked, ~25 productive days). If equipment holds land at the floor case (1 machine, 20 days), rewrite A3 to match before it sends. B3 asserts the machines were locked in July — do not send it until the holds are actually signed. The weekly "slots remaining" number published each Monday/Thursday may be swapped into A3/B3 by the sales lead — real numbers only, straight from the capacity dashboard.
5. **Send windows.** Weekdays 9:30-11:30 AM or 4:30-5:30 PM only, always within 9 AM-6 PM. No weekend or evening sends; Monday sends go out at 10:00 AM or later. A5/B4 must land on a Thursday or the "after Friday" line is a lie.
6. **C2 data discipline.** The [Finding] field is filled by the rep from the assessment report before the text sends. If the report isn't in front of them, the text doesn't go out. A wrong or generic finding on a $5M property reads as mail-merge and kills the neighbor illusion.
7. **Kill-switch (drawdown delay/cancellation).** If the City/LCRA shifts the window — a Low-probability, Critical-impact risk in the register — stop all sequences immediately and send this pivot text to everyone mid-sequence:
   > [First], update: the City shifted the drawdown timing. Your assessment and credit carry over to the new window. Nothing lost. Reply YES for details.

   Character count: 148. Then rebuild cadence around the new window dates.
8. **Weekend shift (Sequence C).** Event-anchored sends (C2, C3) that would land on a Saturday or Sunday shift to the following Monday at 10:00 AM.

---

## PLACEHOLDERS TO FILL

| Placeholder | Max Length | Format | Source | Filled By |
|-------------|-----------|--------|--------|-----------|
| [First] | 10 chars | Plain first name | CRM contact record | Automated merge |
| [Finding] | 24 chars | Short phrase from the report | Client's actual assessment report | Rep, manually, before C2 sends |
| [Date] | 10 chars | "Fri Sep 18" | Real calendar date (slot-hold expiry / deposit deadline) | Rep / CRM automation |
| [Deposit] | 7 chars | "$X,XXX" | Client's actual proposal (15-25% of package; typically $7,500 mid / $15,000 high) | Closer |
| Nathan's direct line live | — | — | Campaign-wide decision: live by Jul 26 | Nathan / Operations Lead |
| Rep direct lines + sender IDs live | — | — | Campaign-wide decision: live by Jul 27 EOD (supersedes the call script's Aug 3 date) | Operations Lead |
| 60-day cold-list re-blast policy | — | — | New policy, not in source docs | Nathan, confirm at Aug 5 standup |
| Live "slots remaining" swap-in number (optional, A3/B3) | — | — | Capacity dashboard, published Mon/Thu | Sales Lead |

---

*COPY_SMS_SequenceSuite_v1_FINAL | ATX Lakescapes | Confidential — Internal Use Only*
