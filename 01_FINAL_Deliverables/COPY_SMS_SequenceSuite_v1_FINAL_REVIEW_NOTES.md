# DRAWDOWN 2026 — SMS SEQUENCE SUITE: REVIEW NOTES
## Process Record for Deliverable 1.2 (Layers 2, 4, 5)

Version: v1 FINAL
Date: July 24, 2026
Author: DRAWDOWN 2026 Swarm — full 6-role panel
Status: Companion to COPY_SMS_SequenceSuite_v1_FINAL.md

---

## LAYER 2 — SKILL POLL (on Layer 1 draft)

Minimum 4 STRONG required to proceed without revision.

| Role | Vote | Notes |
|------|------|-------|
| Creative Director | STRONG | A4 ("didn't want you hearing about the drawdown from a neighbor") is the standout — that's the BBQ test passing. B3 carries the real edge. |
| Copywriter | STRONG | Voice is consistent across all 12; no hype words anywhere; YES-only CTA holds. |
| Media Strategist | ACCEPTABLE | Em/en dashes in draft force UCS-2 encoding — single-segment limit drops from 160 to 70 chars. Strip to GSM-7. Also: day-of-week isn't enough; needs time-of-day windows and staggered batch guidance. |
| Sales Engineer | ACCEPTABLE | A3's structural scarcity (2 machines / ~25 days) is the right move, but it's the TARGET capacity case — floor case is 1 machine / 20 days. Needs a verify-before-send rule. No exit criteria defined for replies mid-sequence. |
| QA / Devil's Advocate | WEAK | (By design — only challenges.) No opt-out handling anywhere. B4 renders at exactly 160 chars with the 6-letter sample name (Marcus); an 8-letter name (Margaret) pushes it over — a zero-margin flaw. "First drawdown in a decade" appears too often. B1 cold opener from an unknown sender is the highest spam-complaint risk in the suite. |
| Board Reviewer | STRONG | Passes the $5M-homeowner read test. Wants reply ownership and the 5-minute SLA written into the usage block. |

**Tally: 3 STRONG / 2 ACCEPTABLE / 1 WEAK → below the 4-STRONG bar → REVISION REQUIRED.**

## LAYER 3 — REVISION (all notes addressed)

1. All em/en dashes and non-GSM-7 characters stripped; every text re-verified single-segment GSM-7 at worst-case fill (8-letter name).
2. Time-of-day windows added to every text; weekday-only send windows codified in Usage Block.
3. A3 carry rule added: verify equipment lock status before each send; floor-case rewrite instruction included.
4. B1 rewritten identity-first ("Nathan Menkin here. My crew works Lake Austin shorelines.") to blunt spam-complaint risk.
5. B4 trimmed to 156 raw for headroom.
6. Opt-out handling section added (immediate suppression, single confirmation text, CRM logging).
7. Reply triage + 5-minute SLA added to Usage Block.
8. Repetition of "first drawdown in a decade" reduced to one text per sequence.
9. Aug 8 falls on a Saturday — flagged; Day 1 send date deferred to Aug 5 standup decision (added to placeholders).

## LAYER 4 — BOARD REVIEW MEMO

**Verdict: APPROVED WITH NOTES**

The suite reads like a neighbor on the lake, not a platform. A4 is the best text in the package — it creates urgency out of social embarrassment rather than discount pressure, which is exactly right for this audience. The structural-scarcity approach in A3/B3 (real machines, real days) is defensible in a way "only 3 slots left!!!" never is.

Conditions of approval (all satisfied in FINAL):
1. No text ships without the opt-out protocol in place.
2. Cold sequence does not send until 10DLC registration is confirmed and consent basis documented per segment.
3. A3/B3 scarcity claims must be re-verified against the capacity dashboard before each send wave.

## LAYER 5 — DEVIL'S ADVOCATE RED TEAM REPORT

**Five specific weaknesses:**

1. **Deliverability fingerprinting.** 200+ identical texts from new 10DLC numbers in one morning is textbook carrier filtering. The sequence dies silently — no error, just 40% non-delivery nobody notices until reply rates crater.
2. **TCPA exposure on the cold list.** Sequence B texts numbers with no prior relationship. One complaint from one attorney homeowner on Lake Austin and the story travels the coves faster than any marketing we could buy. Legal risk concentrates entirely in B1.
3. **A3's claim is conditional and nobody owns the check.** "2 amphibious machines" is only true if O'Shea/Wilco holds are signed (Phase 0, due July 31). If holds slip to the floor case, A3 as drafted is a lie in writing, sent to people who will repeat it at the yacht club.
4. **C2's [Finding] is a loaded gun.** The entire neighbor illusion depends on one rep copy-pasting the right line from the right report. A generic "bulkhead" or — worst — the wrong client's finding on a $5M property is unrecoverable.
5. **YES-only CTA has no escape valve.** Wealthy owners reply with questions ("can you look at the neighbor's too?"). If reps treat non-YES replies as silence and let the cadence keep firing, hot leads get A5'd into the waitlist while actively trying to buy.

**Worst-case scenario:** The City/LCRA delays or cancels the drawdown after sequences are live (Risk Register: Low probability, Critical impact). Hundreds of "first drawdown in a decade" texts are in the wild, scarcity claims are suddenly false, and ATX Lakescapes becomes the company that cried wolf on a lake where everyone knows everyone.

**Three concrete improvements (all applied in FINAL):**

1. Stagger sends in batches of 40-50 and require each rep to hand-rewrite A1/B1 in their own voice — same beats, different words — to break the fingerprint (Usage Block rule 2).
2. Pre-send compliance gate: 10DLC confirmed + documented consent basis per cold segment; unclear segments get calls and door hangers instead of texts (Usage Block rule 1).
3. Kill-switch pivot text (148 chars, pre-approved, in Usage Block rule 7) ready to send to everyone mid-sequence the hour a delay is announced, converting scarcity copy into continuity copy.

**Devil's Advocate severity: 5 weaknesses found. Standard met.**

## LAYER 6 — FINAL

All red-team improvements applied. All character counts re-verified. Board conditions satisfied. No further revision without new information (equipment lock status, confirmed send date, or a window shift).

---

## EXTERNAL RED-TEAM ROUND (Independent Devil's Advocate — after FINAL)

**Verdict: REVISE.** The external reviewer independently verified all char counts for A1-C3 and the kill-switch as exact, then found 10 issues. All 10 fixes applied to COPY_SMS_SequenceSuite_v1_FINAL.md:

| # | Issue | Fix Applied |
|---|-------|-------------|
| 1 | Opt-out confirmation contained a literal em dash (U+2014) — the only customer-facing GSM-7 violation, signed "Nathan"; stated count of 52 included surrounding quotes | Replaced with "You're off the list. Sorry to bother you. Nathan" (48 chars, pure ASCII) |
| 2 | Global Rule 3's "8-letter worst case" claim was false — C3 rendered at exactly 160 with 8 letters, split at 9 | Rule 3 rewritten: worst case = 10-letter first name + max-length field fills per placeholder table, verified under 160 for every text including opt-out and kill-switch |
| 3 | Placeholder table had no length discipline | Added Max Length and Format columns: [First] 10 / [Finding] 24 / [Date] 10 ("Fri Sep 18") / [Deposit] 7 ("$X,XXX") |
| 4 | C3 raw 159 = zero margin | Adopted reviewer rewrite verbatim (149 raw) |
| 5 | Monday Aug 10 start option violated the file's own no-Monday-morning rule; relative day-numbering landed touches on weekends | Aug 10 start option deleted; date-anchored calendar published (Day 1 = Thu Aug 6): A1/B1 Thu Aug 6 9:40 AM; A2 Mon Aug 10 10:15 AM; B2 Tue Aug 11 10:15 AM; A3 Thu Aug 13 9:50 AM; B3 Mon Aug 17 4:40 PM; A4 Mon Aug 17 5:05 PM (staggered after B3 batch); A5/B4 Thu Aug 20 10:00 AM. Usage Block rule 5 amended for consistency: Monday sends at 10:00 AM or later (the old blanket Monday-morning ban conflicted with the mandated calendar). All touches inside the file's send windows. |
| 6 | Mandating rep rewrites invited smart quotes/em dashes back in | Appended to Usage Block rule 2: rewrites typed directly into the SMS platform and re-validated for GSM-7 before queueing — never composed in Word/Notes/iMessage |
| 7 | "60 days" re-blast figure appears in no source doc | Marked as new policy — Nathan to confirm at Aug 5 standup (flag added inline and in placeholder table) |
| 8 | A3's "only 2 amphibious machines" ignored the owned Truxor T50 | Changed to "2 amphibious machines locked" (also dropped "about" to preserve worst-case margin: 153 raw) |
| 9 | Global Rule 2 covered sequences only | Amended: every customer-facing text — sequences, opt-out, kill-switch — must pass a GSM-7 check inside the sending platform before any send |
| 10 | This file's Layer 2 poll said "Margaret" was a 6-letter name — it is 8 | Corrected above: 6-letter sample was Marcus; Margaret (8) is the name that pushed B4 over |

**Knock-on trims required by fix 2's new 10-letter worst case** (verified programmatically, GSM-7/ASCII throughout): B1 "Worth a look at yours?" → "Worth a look?" (149 raw); B2 "gives you answers" → "gives answers" (154 raw); C1 "credited to the job" → "credited" (146 raw); C2 "Happy to talk it through" → "Happy to talk" (128 raw).

**New verified worst-case char counts** (10-letter first name + max field fills; raw count in parentheses):
A1 158 (155) | A2 157 (154) | A3 156 (153) | A4 154 (151) | A5 149 (146) | B1 152 (149) | B2 157 (154) | B3 157 (154) | B4 159 (156) | C1 149 (146) | C2 150 (128) | C3 154 (149) | Opt-out 48 (48) | Kill-switch 151 (148)

**External round severity: 10 issues found and remediated. Suite re-issued as FINAL.**

---

## EXTERNAL RED-TEAM ROUND 2 (Independent Devil's Advocate — after Round 1 re-issue)

**Verdict: REVISE — 2 BLOCKERS + related issues.** Also flagged: the campaign calendar moved — outreach Day 1 is now Mon Jul 27, 2026, 10:00 AM CT, superseding the Aug 6 anchor. All fixes applied to COPY_SMS_SequenceSuite_v1_FINAL.md:

| # | Issue | Fix Applied |
|---|-------|-------------|
| 1 (BLOCKER) | Global Rule 5 + calendar still anchored to Thu Aug 6 | Re-anchored to Mon Jul 27, 2026, 10:00 AM CT. Full table rebuilt with original spacing logic, weekdays only, 9 AM-6 PM, Mondays at 10:00 AM or later: A1/B1 Mon Jul 27 10:00 AM; A2 Fri Jul 31 10:15 AM; B2 Mon Aug 3 10:15 AM (Day+5 landed Sat Aug 1 — weekend shift); A3 Mon Aug 3 10:00 AM (Monday rule; staggered before B2 batch); B3 Fri Aug 7 4:40 PM; A4 Fri Aug 7 5:05 PM (staggered after B3 batch); A5/B4 Thu Aug 13 10:00 AM (Day+14 landed Mon Aug 10 — held to Thursday per the file's own A5/B4 rule; "after Friday" = Aug 14 stays true). Sequence C stays event-anchored. |
| 2 (BLOCKER) | A1 asserted the drawdown as fact ("comes Oct-Nov") | Hedged: "is projected for Oct-Nov". Trims to fit worst case: "Nathan from" → "Nathan at"; "get first slots. Reply YES and I'll hold one." → "book first. Reply YES to hold one." (153 raw / 156 worst) |
| 3 (BLOCKER) | B1 asserted as fact ("The lake drops 10+ ft Oct-Nov") | Hedged: "The lake could drop 10+ ft this Oct-Nov". Trim: "works Lake Austin shorelines" → "works these shorelines" (153 raw / 156 worst) |
| 4 (BLOCKER) | B3 competitor-incapacity claim ("only crew with amphibious equipment locked") disprovable by any competitor with a Truxor | Replaced with committed-in-July framing: "we locked our amphibious machines back in July" (131 raw / 134 worst). Usage Block rule 4 extended: B3 does not send until holds are actually signed. |
| 5 | No weekend-shift rule for event-anchored C sends | Added Usage Block rule 8 verbatim: "Event-anchored sends (C2, C3) that would land on a Saturday or Sunday shift to the following Monday at 10:00 AM." Also referenced in the Sequence C intro. |
| 6 | Phone-line readiness rows used stale dates | Replaced with the campaign-wide decision: Nathan's direct line live by Jul 26; rep direct lines + sender IDs live by Jul 27 EOD (supersedes the call script's Aug 3 date). The obsolete Day-1-confirmation and 10DLC-date rows were removed; Usage Block rule 1 compliance gate moved to "before July 27". |
| 7 | Process file accuracy | This section records the round. Audit of this file for unconditional "cross-file consistent" claims: none exist (the only "consistent" claim is an unrelated voice-consistency poll note in Layer 2). The single cross-file dependency — the call script's Aug 3 rep-line date — is now recorded as superseded/conditional in the FINAL file's placeholder table. |

**New verified worst-case char counts for the rewritten texts** (10-letter first name + max field fills; raw in parentheses): A1 156 (153) | B1 156 (153) | B3 134 (131). All other texts unchanged from Round 1 and still passing.

**External round 2 severity: 2 blockers + 5 related issues found and remediated. Suite re-issued as FINAL.**

---

*Revision rounds used: 1 of 3 allowed (internal) + 2 external red-team rounds (both applied in full).*
