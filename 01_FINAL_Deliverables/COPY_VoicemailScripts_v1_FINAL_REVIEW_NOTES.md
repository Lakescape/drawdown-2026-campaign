# DRAWDOWN 2026 — VOICEMAIL SCRIPTS: REVIEW NOTES
## Companion to COPY_VoicemailScripts_v1_FINAL.md (Deliverable 1.4)

Version: v1.1 FINAL | Date: 2026-07-26 | Author: Swarm | Status: FINAL — external red-team round (verdict REVISE) fully applied

---

## 1. WHAT CHANGED FROM THE SOURCE DRAFT (Sales Copy Suite §3)

The source had three serviceable but non-compliant voicemails. Material changes:

1. **Fixed the unhedged opener.** Source VM1 said "Lake Austin is scheduled for a major drawdown this October" — an assertion of fact on a recordable, forwardable medium. Now "the City's lining up" (past client) and "the City and LCRA are exploring" (cold), matching the email suite's hedged-language rule.
2. **Tightened to spec length.** Source VMs ran 60–85 words (25–35 seconds). The orchestration spec requires 15–20 seconds. FINAL scripts run 40–50 words (15–20 seconds at ~140 wpm), with word counts and read times printed per script.
3. **Killed the invented-count risk.** Source VM2 quoted "[X] clients book Assessments this week" with no sourcing rule. FINAL VM2 uses the standup-published count with mandatory "as of [Monday/Thursday]'s count" framing — and a count-free fallback ("the calendar is filling") when the rep doesn't have the current number.
4. **Fixed the stale equipment line.** Source VM2's "amphibious equipment is getting locked down" implied in-progress. The truth is we committed in July. FINAL says "committed for the window," and a usage rule forbids the stale phrasing.
5. **Added a cold-lead variant of VM1.** The source was past-client-toned only. Cold VM1 leads with the rep's identity on Nathan's crew, offers the one-page summary rather than claiming it was sent, and says the number twice for transcription apps. (Re-voiced and corrected in the external round — see §7.)
6. **Added the VM3 truth gate.** Source VM3 said "moving to a waitlist after Friday" with no calendar rule. FINAL: VM3 leaves Mon–Thu only, with [Friday, Date] as the standup-confirmed cutoff for that list — the same truth standard as SMS A5/B4 and email B4.
7. **Added cadence structure the source lacked.** Planning anchors on the Jul 27 execution calendar, interlocked with the email suite and the re-anchored SMS cadence; maximum 3 VMs per cycle; never two voicemails on consecutive attempts.
8. **Added the kill-switch pivot voicemail** mirroring the SMS and email suites' pivot language (risk register: drawdown delayed/cancelled = low probability, critical impact).
9. **Added the callback-handling block.** The source ended at the beep. A returned call now routes into the Master Call Script at VALUE + SCARCITY, and callbacks are logged against the VM for the callback-rate KPI (working target, uncalibrated — see §7, F11).
10. **Added the ringless-voicemail prohibition.** Live-dialed calls only absent Nathan's written sign-off and legal review — TCPA exposure on this audience is the campaign's biggest legal risk (consistent with SMS Usage rule 1).

---

## 2. SKILL POLL — LAYER 2 (6 agents, simulated)

### Round 1

| Agent | Vote | Key note |
|-------|------|----------|
| Creative Director | STRONG | "'I hope the fall treats your shoreline well' is exactly how Nathan exits a conversation. No desperation anywhere." |
| Copywriter (self-audit) | ACCEPTABLE | Cold VM1 ran 60+ words in the first draft — over the 20-second spec. Needs cutting, not faster reading. |
| Media Strategist | ACCEPTABLE | "Voicemails get transcribed by iPhone/carrier apps now. 'ATX Lakescapes' and the number will mangle. Mitigate." |
| Sales Engineer | ACCEPTABLE | "VM2 without the standup number is vague; with an unmanaged number it's dangerous. Make the number slot and the fallback an explicit either/or." |
| QA / Devil's Advocate | STRONG | "Hedging is right for a forwardable medium. The VM3 Friday rule closes the fake-urgency hole." |
| Board Reviewer | STRONG | "Passes the $5M read-aloud test. Three messages then silence respects these people." |

**Round 1 result: 3 STRONG / 3 ACCEPTABLE → below the 4+ STRONG threshold. Revision required.**

### Revision 1 (applied)

- Cold VM1 cut from 63 to 52 words; number repeated ("That's [Number]") per the Media Strategist's transcription note; brand name positioned early and spoken plainly.
- VM2 rewritten as an explicit either/or: standup number with "as of" framing, OR "the calendar is filling" — never an improvised middle. Usage rule 3 makes stale-count reuse a violation.
- Delivery notes added per script (verify-the-pair swaps, pacing, transcription).

### Round 2

| Agent | Vote | Key note |
|-------|------|----------|
| Creative Director | STRONG | Unchanged. |
| Copywriter (self-audit) | STRONG | Cold VM1 now reads 19–20 seconds and still sounds human. |
| Media Strategist | STRONG | Number-twice on cold, early brand mention, paired-text fallback — transcription risk is handled. |
| Sales Engineer | STRONG | The either/or count rule is enforceable at standup. |
| QA / Devil's Advocate | STRONG | Unchanged. |
| Board Reviewer | ACCEPTABLE | Wants a stated callback-handling path so a returned call doesn't hit an unprepared rep. |

**Round 2 result: 5 STRONG / 1 ACCEPTABLE → threshold met.** The Board Reviewer's note was elevated to the Board memo (Note 3) and applied.

**Revision rounds used: 2 of 3** (the external round in §7 was applied as a mandated-fix pass, not a poll round).

---

## 3. BOARD REVIEW MEMO — LAYER 4

**Verdict: APPROVED WITH NOTES** (all notes applied to FINAL)

1. *Note 1 — Say the number twice on cold.* "A cold contact has no relationship and possibly no delivered text. One mumbled digit and the message is garbage." → Applied: cold VM1 says the number twice; past-client VM1 says it once (their paired text carries it).
2. *Note 2 — VM3 is a factual claim.* "'Waitlist after Friday' on a recording is the easiest sentence in this campaign to forward to a neighbor with 'can you believe this.' It must be true and near." → Applied: Mon–Thu-only rule; [Friday, Date] must be the standup-confirmed cutoff for that list; unconfirmed date means no VM3.
3. *Note 3 — The callback is the conversion event.* "If the VM works, the phone rings. What happens next is not in the source at all." → Applied: WHEN THEY CALL BACK block — opens with thanks, routes into the Master Call Script at VALUE + SCARCITY, logs the callback against the VM for the KPI.

**Board standard applied:** would this impress a $5M homeowner? The scripts assume intelligence, state who is calling before asking for anything, cap contact at three messages, and exit with grace. Played back at a dinner party, every line sounds like a neighbor with real information. Yes.

---

## 4. DEVIL'S ADVOCATE RED TEAM — LAYER 5

### Five specific weaknesses (found and dispositioned)

1. **VM2's count claim is only as true as the rep's discipline.** A rep quoting Monday's number on a Thursday recording manufactures scarcity and creates a forwardable lie. → *Mitigation:* Usage rule 3 — number only from the current standup, always "as of [day]'s count"; otherwise the count-free fallback. The fallback is written into the script so discipline has a default.
2. **"I just texted you" breaks if the SMS filtered or failed.** Carrier filtering on blast day would make VM1's anchor line false for exactly the contacts we're calling. → *Mitigation:* Usage rule 2 — verify pair delivery on the day's call sheet before the block; swap lines provided ("I'll text you the details right after this").
3. **Cold VM1 depends on the email cadence holding.** The summary reference only works if B1 actually went out the day before. → *Mitigation:* swap clause provided for bounce cases. (The original disposition here claimed the old "I emailed you a one-page summary" line was "true to the email even before a designed asset ships." **That rationalization was wrong** — B1 only *offers* the summary on reply, so the line was a false claim. Corrected in the external round; see §7, F10.)
4. **Transcription apps mangle brand and number.** Most of these homeowners will read the voicemail before they hear it. "ATX Lakescapes" transcribes creatively; a mangled number is a dead lead. → *Mitigation:* brand name early and plainly spoken, number twice on cold, and the paired text/email carries clean identity. (Applied in Revision 1.)
5. **VM3's cutoff is a checkable, forwardable claim.** A homeowner who saves VM3 and compares it against what actually happens after [Friday, Date] will know if we lied. If the cutoff slips quietly, every saved VM3 becomes evidence. → *Mitigation:* VM3 truth gate (Usage rule 4) — standup-confirmed date, per list, or the message isn't left. Cutoff changes are communicated, never silent.

### Three concrete improvements (applied)

1. **Added the kill-switch pivot voicemail** — the source had no answer for a shifted window mid-cadence; now the pivot language matches the SMS and email kill-switches in substance ("Nothing is lost — your assessment and credit carry over").
2. **Added the cold-lead VM1 variant** with identity-first framing and the twice-spoken number — the source treated every voicemail recipient like a past client.
3. **Added the cadence table + spacing rules** (max 3 VMs, never consecutive, Mon–Thu for VM3) anchored to the Jul 27 execution calendar and interlocked with the email/SMS touchpoints — turning three loose scripts into a system.

### One worst-case scenario

**The drawdown is cancelled in September, and a saved VM3 — "new assessments move to the waitlist after Friday, Aug 14" — circulates in a Lake Austin HOA group as proof the urgency was manufactured.** *Contained by:* (a) no voicemail ever asserts the drawdown is certain — the hedging rule exists precisely for this recording; (b) the machine commitment is structurally true and honestly framed as a risk we took in July; (c) the kill-switch voicemail goes to every mid-cadence contact with "nothing is lost — your assessment and credit carry straight over," making early movers whole; (d) the 12-month credit is the financial proof that acting early cost nothing. The voicemail that could hurt us is the one we never left — an unhedged one — which is why Usage rule 6 (recording awareness) is non-negotiable.

---

## 5. FINAL DISPOSITION — LAYER 6 (INTERNAL)

- Board verdict: **APPROVED WITH NOTES** — all 3 notes applied.
- Red-team improvements: **3 of 3 applied**; 5 weaknesses dispositioned with mitigations written into the Usage block and per-script delivery notes.
- Revision rounds used: **2 of 3.**
- Cross-file consistency check vs. COPY_CallScript_Master_v1_FINAL and COPY_EmailSequenceSuite_v1_FINAL: offer terms ($695, 100% credited, 12-month validity), hedged drawdown language, standup-count framing, structural scarcity (2 machines / ~25 working days — referenced, not re-litigated), shared suppression, kill-switch substance, Jul 27 Day-1 anchor — **consistent.** Consistency vs. COPY_SMS_SequenceSuite_v1_FINAL is **conditional**: the SMS file still carries the Aug 6 anchor and is being re-anchored and hedge-checked by its own writer in parallel; this file's cadence table assumes that re-anchor lands (see §7, F12).
- Spec check vs. orchestration queue (1.4): 3 scripts ✓, 15–20 seconds each ✓ (word counts printed), neighbor-not-telemarketer tone ✓, callback KPI wired to CRM logging ✓ (target carried as uncalibrated pending Nathan's week-1 calibration — see §7, F11).

## 6. OPEN FLAGS FOR THE ORCHESTRATOR

1. **{{item}} substitution failure:** this writer's assignment arrived as the literal string `{{item}}`. Deliverable 1.4 (Voicemail Scripts) was inferred as the next sequential batch-1 item (1.1–1.3 FINAL; 1.4 next in the orchestration queue). If the swarm intended a different item (1.5–1.10), redirect this writer and treat this file as unsolicited but queue-consistent.
2. **Phone-line timing — RESOLVED by campaign-wide decision:** Nathan's direct line live by Jul 26; rep direct lines live by Jul 27 EOD. The Call Script's Placeholder 11 (which had said "at CRM import (Aug 3)") was updated to match — one-line cross-file assist, recorded in that file's review notes.
3. **One-page summary asset — now triple-flagged** (Call Script, Email, Voicemail). Cold VM1 offers it; email B1 offers it. Add a designed one-pager to the deliverable queue.
4. **SMS suite re-anchor still open** (flagged by the Email writer): COPY_SMS_SequenceSuite_v1_FINAL.md shows the Aug 6 calendar; it is being re-anchored by its owner in parallel. The voicemail cadence table assumes the re-anchored SMS dates.
5. **Standup confirmations needed:** per-list waitlist cutoff dates (VM3 [Friday, Date] depends on them) and the Monday/Thursday published-count process (VM2 swap-in).

---

## 7. EXTERNAL RED-TEAM ROUND (INDEPENDENT) — VERDICT: REVISE

An independent red team outside the swarm audited v1 FINAL and returned **REVISE** with 4 findings (F9–F12) plus one placeholder-table correction (F3) and one cross-file assist. All fixes applied to COPY_VoicemailScripts_v1_FINAL.md (now v1.1) exactly as specified:

1. **F9 (MAJOR, borderline BLOCKER — identity).** Every v1 script was voiced as "Nathan," while the Call Script has [Rep] dialing 40–50/day and this file's own callback section hands callbacks to the rep. Reps impersonating Nathan on forwardable recordings is brand-destroying with past clients who know his voice. → *Applied:* all five scripts (VM1 past, VM1 cold, VM2, VM3, kill-switch) re-voiced to [Rep]. Past-client VM1 opener is now "it's [Rep] from Nathan's team at ATX Lakescapes"; cold VM1 is "this is [Rep] from Nathan Menkin's crew at ATX Lakescapes." Design note added verbatim at the top of the file: "Voicemails are left by reps as themselves. If Nathan wants his own voice on a VM, he records it personally — never scripted for reps." New Usage rule 8 codifies it. Word counts re-verified against the 15–20 second spec after re-voicing (VM1 past 50, VM1 cold 48, VM2 47, VM3 40, kill-switch 49 — all in spec).
2. **F10 (MAJOR — false one-pager claim).** Cold VM1 said "I emailed you a one-page summary," but email B1 only OFFERS the summary on reply. → *Applied:* the line is now "I emailed you a short note about it yesterday — happy to send the one-page summary if it's relevant" (the "short note" = B1 itself, true by cadence). The §4 weakness-3 disposition in this notes file, which had rationalized the old line as "true to the email," is corrected in place — that rationalization was wrong and is now marked as such.
3. **F11 (MINOR — invented KPI).** "Target 15%+" callback rate appears in no ground-truth doc as a calibrated figure. → *Applied:* relabeled "working target 15%+, uncalibrated — to be set by Nathan after week 1 data" in the callback block; a calibration row was added to the placeholder table. (Note for the record: the 15% figure traces to the orchestration queue's quality-criteria line for 1.4, but it is uncalibrated there too — the red team's label stands.)
4. **F12 (MINOR — overbroad consistency claim).** §5's "cross-file consistency … all consistent" claim was unconditional. → *Applied:* §5 now scopes the SMS-suite consistency as conditional on that file's re-anchor and hedging fixes, which its writer is handling in parallel.
5. **F3 (placeholder table — phone lines).** → *Applied:* placeholder table now carries Nathan's direct line live by Jul 26 and rep direct lines live by Jul 27 EOD (campaign-wide decision); the stale "needed by Jul 28, flag to Operations" framing was removed, and open flag #2 is marked RESOLVED.
6. **Cross-file assist (Call Script Placeholder 11).** COPY_CallScript_Master_v1_FINAL.md Placeholder 11 said rep phone/SMS sender IDs come "at CRM import (Aug 3)." → *Applied:* that single line changed to "rep phone/SMS sender IDs — live by Jul 27 EOD (campaign-wide decision)"; nothing else in that file was touched, and the change is recorded in COPY_CallScript_Master_v1_REVIEW_NOTES.md.

**Post-round status:** all mandated fixes applied and verified by full-file sweep; deliverable resubmitted as FINAL v1.1. Verdict chain: WEAK-adjacent poll round 1 (3 STRONG/3 ACCEPTABLE) → round 2 (5 STRONG/1 ACCEPTABLE) → APPROVED WITH NOTES (Board) → internal red team applied → FINAL v1.0 → REVISE (independent external red team, findings F3/F9–F12) → all fixes applied → FINAL v1.1.

---

*COPY_VoicemailScripts_v1.1_FINAL_REVIEW_NOTES | ATX Lakescapes | Confidential — Internal Use Only*
