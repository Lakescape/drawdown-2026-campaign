# FINDINGS — 2026-09-07 — D06 official-facts evals

**Reviewed:** `REVIEW/D06_OFFICIAL_FACTS_COPY_CANDIDATE.md` (customer email + customer text) at `4e475958450d4f5e2a2489b340948bef83658a7f`  
**Companion:** `REVIEW/ATX-1641_SCORECARD.md`  
**Against:** Stage 9 (`GROK_SYSTEM_v2.3_Stage9_Locked.md`), Pillar 7, BBQ + $5M tests, Platform Attention Economics (email/SMS rows), SMS suite send laws (GSM-7, ≤160, one job), D06 locked-facts overlay  
**Not reviewed:** video, reels, hero assembly, July `*_v1_FINAL*` suites (those are not current official copy)

**Do not publish. Do not send. Do not merge. No git tag.**

Nate approved the facts-and-voice candidate at `8624043`. This pass is the send-readiness eval that package never got: Stage 9 + the human tests + the engineering checks most AI media production skips.

---

## Verdict

| Gate | Result |
|------|--------|
| D06 locked-facts candidate (Nate-approved copy) | **PASS** — claims stay inside the lock; capacity stays UNKNOWN |
| Human tests (BBQ / $5M / dock read-aloud) | **Email: PASS with notes. Text: FAIL as a send.** |
| Stage 9 as a *send-ready* package | **REVISE** — default adversarial posture does not clear the text |
| Ready to publish or send | **NO** |

**One-line:** The email is a neighbor note that survives the dock. The text is a press release stuffed into iMessage. Do not send either until the text is cut to a real SMS and the refill-vs-window dates are said the way the City said them.

---

## Overlay (read this before applying July Gate 0)

July Stage 9 still lists “unhedged drawdown language” as a hard fail. **That rule is superseded for this candidate.** City of Austin / LCRA announced August 20, 2026. D06 forbids the old hedge register. Stating the announced window is correct. The official caveat (“may be shortened or canceled”) is the hedge that remains.

Pillar 7 still applies: every claim must trace to the D06 lock or the primary announcement. Capacity stays UNKNOWN. No number.

---

## Human tests (the ones that actually decide)

These are the campaign’s two standing human tests, plus the email-suite dock rule: read it out loud; if it sounds like a marketing department and not Nathan talking across a dock, cut it.

### BBQ test — “Would Nathan say this at a neighborhood barbecue, drink in hand, no agenda?”

**Email: PASS.**  
Read at speaking pace, ~30 seconds. Dates, drop, caveat, then a single ask. No exclamation points, no fake urgency, no “limited calendar” theater. The stiffest line is “We book in the order requests come in,” which is the lock talking, not a slogan. A human Nate would more likely say “we take them in the order they come in.” Same fact.

The press-officer tell is the opener: “On August 20, 2026, the City of Austin and LCRA announced…” At a BBQ he would say “City and LCRA set it — October 12 through November 30.” On a September 7+ send, leading with a mid-August announcement date also reads like leftover news.

**Text: FAIL.**  
No one at a BBQ recites the whole bulletin, then the offer, then the phone number, in one breath. The first six words are Nate. Everything after is a memo.

### $5M homeowner test — “Would they feel *more* respect for us after reading this?”

**Email: PASS, with two questions they will ask.**  
Calm, no hype, no invented scarcity, no competitor shot. A $5M homeowner will still stop on:

1. “The window is October 12 through November 30. Refill is November 24.” That pair looks like a contradiction until you know refill *begins* Nov 24 and the lake is expected back by Nov 30.
2. “$695, credited for 12 months” — credited toward what, and what happens to it if the City shortens or cancels the window? The copy asks for money in the same breath as “they may cancel.”

Those are respect problems if they go unanswered, not tone problems.

**Text: FAIL if this is a cold send; borderline as a past-client ping.**  
Length + UCS-2 encoding (see below) makes it look like a blast, not a neighbor. Sequence B of the SMS suite already named TCPA exposure on a $5M cold list as the campaign’s biggest legal risk. This text does not say who it is for, has no STOP protocol, and does not use the suite’s YES-only CTA.

### Dock read-aloud (performed)

Email: I would tap send to a past client, after fixing the refill sentence.  
Text: I would not tap send. I would cut it in half or make it two texts. The campaign’s own SMS law is one job, GSM-7, worst-case under 160. This is 266–272 characters with a 4–10 letter first name.

---

## Tests most AI media production misses (this is the point of the pass)

Craft evals score how it sounds. These score whether it is *true in the world* and *sendable as a human*.

### 1. Primary-source check (not the brief, the announcement)

Locked facts vs the August 20 City / LCRA release:

| Lock / copy | Primary source | Result |
|-------------|----------------|--------|
| Announced Aug 20, 2026 | City press release dated August 20, 2026 | Match |
| about ten feet | “lowered by about 10 feet” | Match |
| Oct 12 through Nov 30 2026 | “from Oct. 12 through Nov. 30, 2026” | Match |
| refill Nov 24 | “refill is scheduled to **begin** Nov. 24”; expected back in the normal range **by Nov. 30** | Copy flattens “begins” into “is” |
| may be shortened or canceled | “flooding or potential power shortages could cause the drawdown to be shortened or canceled” | Match (cause omitted, caveat kept) |
| Mansfield Dam to Tom Miller Dam; not Lady Bird | In the City memo and release | Copy says “Lake Austin” only — true, but list hygiene still matters |

Sources: [City of Austin press release](https://www.austintexas.gov/communications/news/city-austin-and-lcra-announce-planned-lake-austin-drawdown-fall), [LCRA release (same text)](https://www.lcra.org/news/news-releases/city-of-austin-and-lcra-announce-planned-lake-austin-drawdown-this-fall/), [City Watershed page](https://www.austintexas.gov/lakeaustin), [Aug 20 City memo](https://services.austintexas.gov/edims/document.cfm?id=479526).

Press will also say “first since 2017” / “almost 10 years.” That is **out of the D06 lock**. This candidate does not use it. Do not “improve” the copy by adding it.

### 2. Calendar physics (the $5M reread)

Official hydrograph, not in the customer copy:

- Drop starts Oct 12 at **no more than about a foot a day**.
- **About three weeks** to the lowered target (so full low water is not day one).
- Held low **about four weeks**.
- Refill **begins** Nov 24 at up to ~2 feet/day.
- Expected back to normal **by** Nov 30 (full-lake-to-full-lake window).

The copy’s two-sentence stack — window through Nov 30, then “Refill is November 24” — is lock-legal and customer-confusing. This is the failure mode AI production hits when it pastes a fact sheet without simulating the reader’s second pass.

### 3. SMS engineering (GSM-7 + real length)

Campaign law from the SMS suite: every customer text must pass GSM-7 in the sending platform; worst-case merge under 160; no smart punctuation from a word processor.

Measured on the D06 customer text:

| Fill | Characters | GSM-7 | What the carrier does |
|------|------------|-------|------------------------|
| `Nate` (4) | 266 | FAIL (`U+2014` em dash after the name) | UCS-2; 70-char single-segment limit; this becomes ~4 concatenated segments |
| `Alexandria` (10, suite worst-case) | 272 | FAIL (same dash) | ~5 UCS-2 segments |

Even if the em dash is swapped to a hyphen or period, the text is still ~266 characters — **two GSM-7 segments**, not one. The July suite failed an earlier draft on exactly this dash, then stripped every one. This candidate walked the same rake.

Email subject also uses an em dash. Fine for email. Fatal if someone pastes the subject into SMS.

### 4. Offer completeness vs money-if-canceled

Stage 9 soft fail: incomplete offer (`$695` / credited / 12-month). D06 lock is `$695 credited 12 months` — the candidate follows the lock and does **not** say “100% credited toward any work you approve.” A $5M reader hears a fee, not a credit against work.

The next sentence in the world is: they may cancel the window. The SMS suite already has a kill-switch line that the assessment and credit carry over. This candidate never says that. Asking for $695 beside “may be canceled” without the carry-over is how you look like you sold a window, not an assessment.

### 5. “Lake Austin down about ten feet” (SMS parse)

Email: “announced a Lake Austin drawdown of about ten feet” — future/event. Clear.  
Text: “Lake Austin down about ten feet, Oct 12 through Nov 30” — can read as *the lake is already down*. It is not (as of this eval date). Compression error. Human would catch it; models optimizing for brevity miss it.

### 6. Audience, TCPA, and identity

The candidate does not say past-client vs cold. Email sign-off is Nathan; that fits past clients. Cold SMS in this campaign required identity-first *and* documented consent *and* 10DLC. This text is “Reply or call (254) 780-6971” — two CTAs, a phone number, no STOP. Past-client 1:1: usable after a cut. Cold blast: do not send.

### 7. Phone number check (the placeholder fill)

`(254) 780-6971` matches the public ATX Lakescapes / Austin lakescapes LLC number ([Procore listing](https://network.procore.com/p/austin-lakescapes-llc-leander-1), [reviews page call link](https://atxlakescapes.com/reviews/)). **PASS.** Do not swap it.

### 8. Channel contract (Platform Attention Economics)

| Channel | Contract | D06 |
|---------|----------|-----|
| Email | Direct value, personal, 80–150 words, one CTA | 79 words. Slightly short, still personal. Dual path (reply *or* call) is one job. |
| SMS | Extreme brevity, first 6 words, &lt;160 ideal, reply rate | First 6 words pass. Length fails. CTA is not YES-only. |

### 9. Stale-news lead

Eval date is 2026-09-07. Leading with “On August 20, 2026” tells a September reader we are forwarding a three-week-old press release. The dates of the *window* still matter. The announcement date is for the scorecard, not the first line of a late send.

### 10. What we correctly did *not* add

No equipment-allocation story. No working-day count. No capacity number. No provenance claim. No “nothing official” hedge. Capacity remains UNKNOWN. That is the whole point of D06. Do not “enrich” the eval by putting those back.

---

## Stage 9A — Self-critique

**Pillars (Gate 0 craft, applied only where the channel can fail them):**

| # | Pillar | Email | Text |
|---|--------|-------|------|
| 1 | Blockbuster treatment of the banal | N/A (not a reel) | N/A |
| 2 | Eternal polarity (enemy *or* payoff) | Announcement + offer in one note — acceptable for this brief | Same, cramped |
| 3 | Dark comedy / ironic grandeur | N/A | N/A |
| 4 | Pure visual / muted | N/A | N/A |
| 5 | Lake Austin status subtext | Weak — “your shoreline,” no cove, no neighbor knowledge | Weaker |
| 6 | Escalation to payoff | Clear ask | Ask buried under dates |
| 7 | Verifiable truth (hard veto) | Dates match the lock and the release; refill wording is flattened | Same flatten + “down about ten feet” parse |

**BBQ:** email PASS / text FAIL  
**$5M:** email PASS with questions / text FAIL as a blast  
**Strengths:** short; lock-faithful; no invented scarcity; phone is real; caveat is official.  
**Weaknesses:** text is not a text; refill sentence; offer unit incomplete; send laws ignored.  
**Next experiment (only after Nate marks send copy):** one GSM-7 SMS ≤160 that keeps the window dates, the caveat, $695 credited 12 months, booked in order, and the phone — and one email sentence that says refill *begins* Nov 24, back by Nov 30.

---

## Stage 9B — Adversarial pass

**Stance:** default REJECT. Not a collaborator.

**VERDICT: REVISE** (REJECT as send-ready; do not treat Nate’s facts approval as a send approval)

**Hard failures found:**

1. **SMS send law (campaign, not July video Gate 0).** Customer text is 266–272 characters and contains `U+2014`, so it cannot ship as a single GSM-7 segment. The SMS suite already called this a ship blocker once.

**Hallucinations found:**  
None of the invented-number / fake-social-proof / fake-equipment class. “Refill is November 24” is a **flattening** of “refill begins November 24,” not a new date. Still a customer-facing truth problem.

**Soft failures found:**

- Incomplete offer unit vs Stage 9 (`toward any work` not stated).
- Dual CTA on SMS vs YES-only law.
- No audience, no STOP, no send-window note.
- Status line in the file still says “pending Nate copy approval” after Nate approved `8624043` (metadata, not customer copy).
- Email slightly under the 80-word floor — not a fail.

**Most dangerous blind spot:**  
Shipping the text as-is. A $5M homeowner gets a four-segment UCS-2 blast that says the lake is “down,” asks for $695, and mentions cancelation in the same bubble. That is how this brand becomes a cove story. The email’s refill/window stack is the second-place blind spot: one careful reader forwards it to a neighbor with “their dates don’t even agree.”

**Minimum changes required to survive a send:**

- Cut the customer text to GSM-7, worst-case ≤160 (10-letter first name). No em dash, no en dash, no smart quotes.
- Say refill **begins** Nov 24; window is full-lake to full-lake through Nov 30. Do not invent drop-rate or “three weeks” in customer copy unless Nate adds them to the lock.
- Keep capacity UNKNOWN. Do not add a number to “fix” urgency.
- Decide past-client vs cold before any send. Cold SMS still needs the suite’s consent/10DLC gate.
- Do not send, publish, or tag off this eval.

**Final recommendation:**  
Keep the Nate-approved email bones; do not send the current text; do not merge until send copy is a separate, eval-passing revision.

---

## Stage 9C — Hallucinations check

| Type | Result |
|------|--------|
| Invented numbers (capacity, crew, machine-days) | None. Capacity UNKNOWN. |
| Invented measurements about the reader’s property | None. |
| Invented equipment capability | None. |
| Invented timeline certainty | Announced window stated as announced; caveat present. Refill wording flattened (see above). |
| Invented social proof | None. |
| Invented process claims (permits, what’s in the assessment) | None — and that thinness is why the $695 line feels unfinished. |
| AI-as-proof imagery | N/A (copy only). |

**Pillar 7:** no hard invented-fact fail. Calendar flattening is the remaining truth debt.

---

## D06 lock scan (candidate + scorecard)

Automated scan of `D06_OFFICIAL_FACTS_COPY_CANDIDATE.md` for the D06-forbidden register: **no hits.**  
Scorecard still marks capacity **UNKNOWN** and invents no counts.

Customer-facing copy uses only: Aug 20 City/LCRA announcement, about ten feet, Oct 12 through Nov 30 2026, refill Nov 24, may be shortened or canceled, $695 credited 12 months, booked in order, phone `(254) 780-6971`.

---

## Finding list (swarm format)

### BLOCKER

**B1 — Customer text is not sendable as SMS**  
**Where:** `D06_OFFICIAL_FACTS_COPY_CANDIDATE.md` → Customer text  
**Issue:** 266–272 characters + em dash → UCS-2, 4–5 segments. Violates the SMS suite’s GSM-7 and ≤160 laws. Fails BBQ, $5M-as-blast, and the dock send test.  
**Fix:** Rewrite as a real SMS (ASCII punctuation, ≤160 worst-case). Do not paste the email into a text. Re-count after every edit.

### MAJOR

**M1 — “Refill is November 24” vs window through November 30**  
**Where:** email body (and the same pair in the text)  
**Issue:** Official language is refill *begins* Nov 24, expected back by Nov 30. Side-by-side, the copy looks internally wrong to a careful homeowner.  
**Fix:** One clarifying clause. Do not add drop-rate or week-counts unless Nate expands the lock.

**M2 — Fee next to cancelation, credit not explained**  
**Where:** offer sentence in both channels  
**Issue:** $695 + “credited for 12 months” + “may be shortened or canceled” with no “toward work” and no carry-over if the window moves.  
**Fix:** Nate call: restore “credited toward any work you approve, 12 months” if he wants the Stage 9 offer unit; say the credit stands if the City shifts the window. Stay inside the lock if he does not.

**M3 — SMS “Lake Austin down about ten feet”**  
**Where:** customer text  
**Issue:** Reads as present tense. The lake is not down on a September send.  
**Fix:** Match the email’s “drawdown of about ten feet” / “drops about ten feet.”

### MINOR

**m1 — File status still says pending Nate approval** after approval at `8624043`. Update the banner when send copy is decided; do not treat this as a customer-copy change.  
**m2 — Audience unspecified.** Past-client vs cold changes TCPA, opener, and whether this text may exist at all.  
**m3 — Email opener dated August 20** will feel stale on a mid-September send. Lead with the window, not the press date.  
**m4 — Dual CTA** (reply or call) is acceptable in email; on SMS it fights the YES-only law.

---

## What this eval did *not* do

- Did not rewrite the Nate-approved customer copy.
- Did not merge, tag, publish, or send.
- Did not close Linear.
- Did not invent capacity, holds, or bookings.
- Did not run live sends, inbox previews in Gmail, or a carrier 10DLC test — those still have to happen in the sending platform before any blast.

---

## Sources

- [City of Austin and LCRA Announce Planned Lake Austin Drawdown this Fall](https://www.austintexas.gov/communications/news/city-austin-and-lcra-announce-planned-lake-austin-drawdown-fall) (Aug 20, 2026)
- [LCRA news release, same announcement](https://www.lcra.org/news/news-releases/city-of-austin-and-lcra-announce-planned-lake-austin-drawdown-this-fall/) (Aug 20, 2026)
- [City of Austin — Lake Austin drawdown page](https://www.austintexas.gov/lakeaustin)
- [City memo to Mayor and Council](https://services.austintexas.gov/edims/document.cfm?id=479526) (Aug 20, 2026)
- [ATX Lakescapes reviews / call number](https://atxlakescapes.com/reviews/)
- [Austin lakescapes LLC Procore listing](https://network.procore.com/p/austin-lakescapes-llc-leander-1)
