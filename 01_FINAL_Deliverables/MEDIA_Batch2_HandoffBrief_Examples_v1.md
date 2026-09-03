# DRAWDOWN 2026 — MEDIA BATCH 2 HANDOFF BRIEF + QUALITY-BAR EXAMPLES
## Deliverables 2.1–2.7 — Complete Specs + Finished Exemplars for the Claw Team / Grok

Version: v1
Date: 2026-07-27
Author: Swarm — Specialist Writer (Media Batch 2)
Status: HANDOFF-READY — one draft + one self-review pass complete; NOT board-reviewed, NOT for publication

---

## HOW TO USE THIS DOCUMENT (read this first, 90 seconds)

This brief is self-contained. You do **not** need any other session context to produce Batch 2 media creative. It contains:

1. **THE RULES** — the working law (AGENTS.md, verbatim) plus the campaign facts that every deliverable must obey.
2. **PER-DELIVERABLE SPECS + EXAMPLES** — for each of 2.1–2.7: the exact production spec, then 1–3 **finished, exemplary examples** written to the quality bar. Your output should match or beat these examples in voice, specificity, and rule compliance. Do not copy them — they exist to set the floor, not the ceiling.
3. **HANDOFF INSTRUCTIONS** — file naming, where outputs land, the QA gate, and what to escalate.

**The examples are finished work.** If you are unsure whether something you wrote is good enough, hold it next to the matching example and ask: is it this specific, this calm, this rule-clean?

---

## SECTION 1 — THE RULES

### 1A. AGENTS.md — the working law (verbatim, abridged to what governs Batch 2; source: AGENTS.md, updated 2026-07-24)

> ## Ground rules (both agents)
>
> 1. **Real numbers only.** Never invent scarcity: slot counts, machine-days, crew counts, booking counts come from the Mon/Thu published count or are written as [X] placeholders. This rule has already caught multiple violations — it is the campaign's core trust mechanism.
> 2. **Tone:** calm authority, local expertise, real scarcity. Never hype, never corporate. Tests: "Would Nathan say this at a BBQ?" / "Would a $5M homeowner read this?"
> 3. **Shoreline work only** — this is a contractor play, not an environmental pitch. Do not assert the drawdown "is happening"; use "lined up," "projected," "pointing to."
> 4. **Never claim competitor incapacity.** State what ATX has locked, not what others can't get.
> 5. **SMS copy must be GSM-7 safe** (no em dashes, smart quotes, emoji) and ≤160 chars rendered with worst-case fills. Em dashes force UCS-2 and split messages.
> 6. **Aesthetic:** Cormorant Garamond + Source Sans 3; #f7f5f0 / #c4923a / #1a1a1a. No gradients, no neon.
>
> ## Folder contract
>
> - `07_Swarm_Deliverables_FINAL/` — board-reviewed, red-teamed FINAL files. Do not edit in place; new versions get new filenames (v2, v3…).
> - `08_Agent_IO/kimi_inputs/` — briefs/context handed TO Kimi.
> - `08_Agent_IO/kimi_outputs/` — drafts/data Kimi produces for review or for Grok to consume.
> - `08_Agent_IO/grok_inputs/` — briefs/context handed TO Grok (e.g., social post generation briefs, approved angles, scarcity numbers of the day).
> - `08_Agent_IO/grok_outputs/` — Grok's social drafts, saved here for QA before anything is scheduled.
>
> ## File naming
>
> `[AGENT]_[TYPE]_[DESCRIPTION]_[vN]_[STATUS].md` — e.g. `GROK_SOCIAL_IGCarousel_Angle3_v1_DRAFT.md`, `KIMI_BRIEF_SocialWeek1_v1_FINAL.md`.
> Status flow: DRAFT → BOARDREVIEW → FINAL. Nothing publishes from DRAFT.
>
> ## Handoff protocol (social posts)
>
> 1. Kimi writes the weekly social brief (angles, verified scarcity numbers, offer rules) → `grok_inputs/`.
> 2. Grok generates posts → saves to `grok_outputs/` with naming above.
> 3. QA pass (red team checklist: real numbers? GSM-7 if SMS-adjacent? BBQ test? no exclusivity claims?) → approved posts marked FINAL.
> 4. Only FINAL posts go to scheduling. Kanban/Asana card links the Drive file.
>
> ## Watch-outs
>
> - .gdoc/.gsheet files in Drive are pointer files — agents reading via the local mount cannot open their contents; export to .md/.xlsx first.
> - If Drive for desktop is set to "stream," a file may need to be opened once in Finder to hydrate before an agent can read it.
> - Anything touching legal/financial/customer-private material goes to a review queue, not final storage.

(System-of-record note from the same file: Slack is the sales floor, Linear is the ledger, Drive holds files/briefs only. Batch 2 outputs are files — they land in Drive `08_Agent_IO/` or GitHub `REVIEW/`, never in Slack/Linear as primary storage.)

### 1B. Campaign facts — enforce in every deliverable, no exceptions

| Fact | Approved language |
|------|-------------------|
| Drawdown status | **Updated 2026-08-29 — LCRA announced it.** The event may be stated: "the City and LCRA have announced a drawdown." The DEPTH and the WINDOW stay hedged: "projected for October–November," "a projected ten-to-twelve-foot drop." Never an unhedged date. |
| Assessment offer | **$695, 100% credited toward any work, credit valid 12 months.** These three elements travel together. |
| Scarcity (the ONLY approved structural numbers) | **2 amphibious machines locked · ~25 working days in-window · committed in July.** Live slot/booking counts come only from the Mon/Thu published count, quoted as "as of [Monday/Thursday]'s count." Anything else = [X]. |
| Retired line (never reuse) | ~~"47 machine-days available. 31 spoken for."~~ — invented, caught, retired. Do not resurrect it or anything like it. |
| Competitors | State what ATX locked ("We committed in July"). Never state or imply competitors can't get equipment, can't get permits, or aren't prepared. |
| Audience | $2M+ Lake Austin waterfront owners. Write for the country-club reader: understatement wins, exclamation points lose. |
| Tone test | "Would Nathan say this at a BBQ?" + "Would a $5M homeowner read this without flinching?" If either fails, rewrite. |
| Aesthetic | Warm editorial. Cormorant Garamond (display) + Source Sans 3 (body). Palette: #f7f5f0 paper, #c4923a gold, #1a1a1a ink. **No gradients, no neon, no stock-photo gloss.** |
| Referral credit | **Do not mention the $500 referral credit in any pre-window asset.** Program launches in October. |
| SMS-adjacent copy | GSM-7 safe, ≤160 chars worst-case rendered (rule 5 above). Flag any asset that will be adapted to SMS. |

---

## SECTION 2 — PER-DELIVERABLE SPECS + EXAMPLES

### 2.1 — META/INSTAGRAM AD COPY (12 ANGLES)

**Spec (from Swarm Quick-Start Guide, Deliverable 2.1):** Produce 12 Meta/Instagram ad sets — **4 problem-aware / 4 solution-aware / 4 most-aware.** Each ad set must include:

- **Headline** — 40 characters max
- **Primary text** — 125 characters max (count the rendered characters, including spaces)
- **CTA button text** (Meta standard: Learn More, Book Now, Get Quote, etc.)
- **Targeting recommendation** (audience definition, not budget)
- **A/B test pairing** (which other ad set in your 12 it tests against, and what variable differs)

**Awareness-level discipline:**
- *Problem-aware:* reader knows their shoreline might have issues, doesn't know the drawdown exists or matters. Job = connect hidden damage to a rare, time-limited chance to see it.
- *Solution-aware:* reader knows work needs doing, doesn't know why now or why us. Job = the window + the equipment + the credited assessment.
- *Most-aware:* reader knows the offer, hasn't acted. Job = real arithmetic and a clean, dignified close. Live counts only as [X] with "as of [day]'s count" phrasing.

**Character limits are hard.** Write the copy, then count. Do not estimate.

#### EXAMPLE AD SET 2.1-A (Problem-Aware) — "What's Under Your Dock"

- **Headline (23 chars):** What's under your dock?
- **Primary text (124 chars):** A drawdown is lining up for Lake Austin. A decade of hidden bulkhead damage becomes visible — and fixable. Assessments open.
- **CTA:** Learn More
- **Targeting:** Lake Austin waterfront homeowners — geo-radius on Lake Austin shoreline parcels (78730, 78732, 78733, 78734, 78746 + waterfront polygon); homeowner; property value $2M+; age 45–70; exclude existing ATX client list.
- **A/B pairing:** Test against 2.1 problem-aware angle "10 Years of High Water" — same audience, hook variable differs (question hook vs. time-depth hook). Keep winner; kill loser at the kill rule in 2.7.

#### EXAMPLE AD SET 2.1-B (Solution-Aware) — "The Credited Assessment"

- **Headline (32 chars):** The $695 that buys you certainty
- **Primary text (115 chars):** $695 Assessment: photos, written scope, reserved calendar slot. 100% credited. 2 machines locked. ~25 working days.
- **CTA:** Book Now
- **Targeting:** Retargeting pool — website visitors last 30 days, IG/FB engagers on drawdown content, email list non-openers; exclude booked assessments and deposits.
- **A/B pairing:** Test against 2.1 solution-aware angle "Two Machines" — same retargeting pool, lead variable differs (offer-first vs. equipment-first).

#### EXAMPLE AD SET 2.1-C (Most-Aware) — "The Count"

- **Headline (30 chars):** [X] slots left — then waitlist
- **Primary text (124 chars):** As of [Mon/Thu]'s count, [X] slots remain. $695, fully credited, 12-month validity. Book now — first in gets the calendar.
- **CTA:** Book Now
- **Targeting:** Warm retargeting only — assessment-page visitors who didn't book, email clickers, lead-form openers. Exclude booked/deposited. Never run most-aware copy to cold audiences.
- **A/B pairing:** Test against 2.1 most-aware angle "The Honest Math" — same warm pool, close variable differs (scarcity-first vs. arithmetic-first). Fill [X] and the count day at send time from the published Mon/Thu count — never from memory.

---

### 2.2 — VIDEO SCRIPTS (8 REELS/TIKTOK)

**Spec (Deliverable 2.2):** Produce 8 short video scripts — **8–15 seconds each**, with **visual direction for every shot**, **music/sound cues**, **hook in the first 2 seconds**, and **text overlay specs.**

**Craft rules:**
- The first 2 seconds decide everything. Lead with the image, not the logo. No branded openers.
- Sound design is lake-real: water, machinery at distance, footsteps on a dock. Music is sparse, low, instrumental — or none.
- Text overlays: Source Sans 3, #1a1a1a on #f7f5f0 lower-third band, or #f7f5f0 on dark footage. No animated sticker-style captions.
- Vertical 9:16, 1080×1920. Captions burned in (most watch muted).
- Every script ends with ONE on-screen line: the offer. No verbal CTA read by a voiceover if a text line does it quieter.

#### EXAMPLE SCRIPT 2.2-A — "The Exposed Truth" (12 sec, problem-aware / educational)

| Time | Visual | Sound | Text overlay |
|------|--------|-------|--------------|
| 0:00–0:02 | Drone drops fast toward a Lake Austin cove; waterline stains visible on a bulkhead | Ambient lake; a low single piano note | **10 years of high water hid this.** |
| 0:02–0:06 | Slow pan along the exposed bulkhead: rotting tie-back, sediment shelf, leaning section | Water lapping; footsteps on wet gravel | Sediment 2–4 ft behind the wall. Tie-backs rotting where you can't see. |
| 0:06–0:10 | Crew member crouches, points at the tie-back, looks up at camera (no talking head — just presence) | Natural sound swells slightly | A drawdown makes it visible — and fixable. |
| 0:10–0:12 | Cut to paper-tone end card, gold rule, logo small | Silence | **$695 Assessment. 100% credited.** Book before the window. |

- **Format:** 9:16, captions burned in, post to Reels + TikTok + FB Reels.
- **Shot note:** If no drawdown footage exists yet, use past low-water project footage or a bulkhead inspection clip — never stock.

#### EXAMPLE SCRIPT 2.2-B — "Meet the Machine" (10 sec, equipment flex / solution-aware)

| Time | Visual | Sound | Text overlay |
|------|--------|-------|--------------|
| 0:00–0:02 | Amphibious excavator tracks churn from water onto soft mud in one motion — the money shot | Real machine audio, loud and close | **It floats. It crawls.** |
| 0:02–0:05 | Close-up: tracks gripping sediment where a conventional machine would sink | Machine idle; wind | Works the soft lake bed. |
| 0:05–0:08 | Wide shot: machine working a shoreline, dock in frame, Hill Country behind | Audio pulls back; one low cello note enters | We locked two of them. In July. |
| 0:08–0:10 | Paper-tone end card | Silence | **~25 working days. That's the window.** Book your Assessment — $695, credited. |

- **Format:** 9:16, captions burned in, Reels-first.
- **Rule check:** "We locked two of them. In July." states what ATX has — it never says what anyone else can't get. Keep it that way.

---

### 2.3 — STATIC IMAGE AD CONCEPTS (6)

**Spec (Deliverable 2.3):** Produce 6 static image ad concepts. Each includes: **headline, visual description (what the image shows), background/color specs, CTA, size/format (feed vs. story vs. carousel).**

**Craft rules:**
- Premium, editorial, local. Real Lake Austin imagery: real coves, real bulkheads, real machines, real water stains. If a concept could be shot anywhere in America, it fails.
- No stock-photo vibes: no handshake photos, no generic excavator renders, no sunset clip-art. Shoot list or real archive only.
- Type: Cormorant Garamond for headlines, Source Sans 3 for supporting. Generous whitespace. The ad should look like a page from a good regional magazine that happens to have a button.

#### EXAMPLE CONCEPT 2.3-A — "The Count" (scarcity editorial card)

- **Headline:** Two machines. Twenty-five working days.
- **Visual description:** No photo — a typographic card. Headline set large in Cormorant Garamond, #1a1a1a ink on #f7f5f0 paper. Below, a thin #c4923a gold rule, then three short lines in Source Sans 3: "Committed in July. / ~25 working days in-window. / As of [Mon/Thu]'s count: [X] assessment slots remain."
- **Background/color specs:** #f7f5f0 flat background. No texture, no gradient, no shadow. Gold (#c4923a) used once — the rule line only.
- **CTA:** Book Now → "Book your $695 Assessment — fully credited."
- **Size/format:** 1:1 feed (1080×1080) primary; 4:5 (1080×1350) crop for IG feed. Not a story format — this one reads, not glances.
- **Why it works:** It looks like the truth, not an ad. The scarcity is structural and approved — 2 machines, ~25 days, committed in July — with the live count as [X].

#### EXAMPLE CONCEPT 2.3-B — "The Cove at Low Water" (photo, local/specific/real)

- **Headline:** Your shoreline is about to tell you the truth.
- **Visual description:** Real drone photograph of a named Lake Austin cove (e.g., the mouth of a recognizable cove on the west side) at an existing low-water mark — bulkhead waterlines, exposed sediment bars, docks sitting high. Shot at soft morning light. Headline set in Cormorant Garamond, #f7f5f0, upper third of frame over sky/water. Small gold sub-line: "A drawdown is lining up for October–November."
- **Background/color specs:** Photograph, not design. Type only in the quiet zone of the image (sky). #c4923a reserved for the one sub-line; body text #f7f5f0 with a 40% #1a1a1a scrim only if legibility demands it.
- **CTA:** Learn More → "See what a $695 Assessment covers."
- **Size/format:** 4:5 IG/FB feed (1080×1350); 9:16 story crop (1080×1920) with headline moved to the top safe zone.
- **Why it works:** A $5M homeowner recognizes that cove. Specificity is the premium signal; nobody else on the lake is running their shoreline.

---

### 2.4 — EMAIL SUBJECT LINES (20 PAIRS)

**Spec (Deliverable 2.4):** Produce 20 subject line + preview text pairs — **5 curiosity / 5 urgency / 5 benefit / 5 social-proof.** Subject: **50 chars max.** Preview: **90 chars max.** Open-rate target 40%+.

**Craft rules:**
- Pairs work as a unit: the preview completes or sharpens the subject, never repeats it.
- No clickbait the email can't pay off. The body must deliver the subject's promise in the first two lines.
- Most-aware/urgency pairs quote live counts only as "[X], as of [day]'s count."
- Voice: a note from Nathan, not a broadcast. Lowercase-free is fine; SHOUTING is not. No emoji. Em dashes fine in email (GSM-7 applies to SMS only).

#### FINISHED EXAMPLE PAIRS (5)

| # | Category | Subject (chars) | Preview text (chars) |
|---|----------|-----------------|----------------------|
| 1 | Curiosity | What's under your dock at 10 feet lower? (40) | Most owners find out in November. The ones who book now find out in writing. (76) |
| 2 | Urgency | 2 machines. ~25 working days. That's the window. (48) | As of [day]'s count, [X] assessment slots remain — then it's the waitlist. (74) |
| 3 | Benefit | Know your shoreline before the water drops (42) | $695. Full documentation. Written scope. 100% credited toward any work. (71) |
| 4 | Social proof | Your neighbors are already on the list (38) | [X] past clients booked this week. The most common reaction: "I had no idea." (77) |
| 5 | Curiosity | The lake will show you everything this fall (43) | A ten-to-twelve-foot drop exposes a decade of damage — for a few weeks only. (76) |

**Self-review note on the set:** #2 and #4 carry [X]/[day] placeholders by design — fill from the published Mon/Thu count at send time. #4's quote is the approved recurring client line from the email suite; do not fabricate new testimonials — pull real quotes from assessment files with permission, or keep this approved line.

---

### 2.5 — CONTENT TEMPLATES (6 REUSABLE)

**Spec (Deliverable 2.5):** Produce 6 reusable content templates — **(1) scarcity update, (2) social proof, (3) equipment flex, (4) process authority, (5) neighbor-shade, (6) educational.** Each template needs: **fill-in-the-blank format, one filled example, and channel recommendations (IG, FB, email, SMS).**

**Craft rules:**
- Templates are production tools: a rep or Grok should be able to fill one in under 5 minutes from the Mon/Thu count.
- Every template's [X] fields map to a named source (published count, client file, equipment status). If a field has no source, it doesn't exist.
- SMS variants of any template must be GSM-7 safe and ≤160 chars worst-case rendered.
- Neighbor-shade never names a street address or a person without written permission. Cove-level references ("your cove," "the west side") are the default.

#### EXAMPLE TEMPLATE 2.5-A — SCARCITY UPDATE

**Fill-in-the-blank:**

> **[X] Priority Assessment slots remain — as of [Mon/Thu]'s count**
>
> 2 amphibious machines locked.
> ~25 working days in the projected window.
> [X] properties on the Priority List.
>
> First in gets the calendar.
> Book your $695 Assessment — 100% credited, valid 12 months: [link]

**Field sources:** [X] slots + [X] properties → Mon/Thu published count, read at standup. Machines/days → approved structural numbers, no source needed. [link] → booking page.

**Filled example (as if from a Thursday count):**

> **11 Priority Assessment slots remain — as of Thursday's count**
>
> 2 amphibious machines locked.
> ~25 working days in the projected window.
> 19 properties on the Priority List.
>
> First in gets the calendar.
> Book your $695 Assessment — 100% credited, valid 12 months: atxlakescapes.com/assessment

**Channel recommendations:** IG/FB feed (typographic card, concept 2.3-A style), IG Story (countdown sticker optional), email block inside sequence emails, Nextdoor. **SMS variant:** "ATX Lakescapes: 11 assessment slots left as of Thu's count. $695, fully credited. Book: [short link] Reply STOP to opt out" — GSM-7, ≤160 chars. *(Filled numbers shown for illustration only — the live send uses the real published count.)*

#### EXAMPLE TEMPLATE 2.5-B — NEIGHBOR-SHADE

**Fill-in-the-blank:**

> **Someone in [Cove/Neighborhood] just locked their Priority Assessment.**
>
> They'll know exactly what their shoreline needs before the projected window opens.
> Will you?
>
> $695. Fully credited. 12-month validity. [link]

**Field sources:** [Cove/Neighborhood] → real booking, cove-level only, confirmed at standup; must be literally true when posted. Never an address, never a name, without written permission.

**Filled example:**

> **Someone on the west side just locked their Priority Assessment.**
>
> They'll know exactly what their shoreline needs before the projected window opens.
> Will you?
>
> $695. Fully credited. 12-month validity. atxlakescapes.com/assessment

**Channel recommendations:** Nextdoor (native fit), FB/IG feed targeting that cove's polygon, email PS line in Sequence B. **Not for SMS** — neighbor-shade over text reads as surveillance; keep SMS to straight scarcity. **Integrity rule:** if no real booking exists in that cove, the template does not run. There is no generic version of neighbor-shade.

---

### 2.6 — LOCAL MEDIA PITCH DECK (5 OUTLETS + PRESS RELEASE)

**Spec (Deliverable 2.6):** Produce pitches for **KVUE (news desk), KXAN (investigative/feature), Austin American-Statesman (business/real estate), Austin Business Journal, Austin Monitor (city/environment).** Each pitch includes: **subject line, 3-paragraph pitch, why now / why ATX Lakescapes / why this outlet, suggested interview questions, contact strategy.** Plus **1 press release template.**

**Craft rules:**
- Journalists smell hype. The pitch is calm, factual, and offers access: the machines, the crew, a shoreline owner, the exposed lake bed.
- Updated 2026-08-29: LCRA announced the drawdown, so the event may be stated to press as fact. "Projected" still applies to the DEPTH and the WINDOW. Never let ATX be the source that over-asserts a City decision on dates.
- Timing per the Media Dominance Calendar: KVUE ~Oct 15, Austin Monitor ~Oct 30, Statesman ~Nov 1, ABJ ~Nov 15, KXAN ~Oct 22. Pitches are written now, sent on schedule, and re-verified for hedging the week they send.

#### FINISHED EXAMPLE PITCH — KVUE (news desk, target send ~Oct 15)

**Subject:** Rare Lake Austin drawdown — local crew restoring shorelines before refill

**3-paragraph pitch:**

> The City of Austin and LCRA have announced the first meaningful Lake Austin drawdown in nearly a decade — a ten-to-twelve-foot drop projected for October–November. When the water falls, a decade of hidden damage on private shorelines becomes visible for the first time: failing bulkheads, rotting tie-backs, two to four feet of sediment.
>
> My company, ATX Lakescapes, has committed two amphibious machines — equipment that can work the soft exposed lake bed — and our crews will be restoring shorelines across Lake Austin through the roughly 25-working-day window. It is one of the rare chances to film this kind of work: machines working where the lake floor used to be underwater, homeowners seeing their shoreline's real condition for the first time in ten years.
>
> I'd like to offer your news desk access: a working shoreline site, the amphibious equipment in operation, and a waterfront homeowner who can speak to what the low water revealed. Happy to coordinate around your schedule — the work runs daily while the window is open. Nathan Menkin, ATX Lakescapes — [phone] | [email].

**Why now:** First meaningful drawdown in ~10 years is lining up; the window is short and visual — it is news that disappears when the lake refills.
**Why ATX Lakescapes:** We have the amphibious equipment committed and the properties booked — we can put a crew, a machine, and a homeowner in front of a camera within days, not weeks.
**Why KVUE:** KVUE's audience is the Lake Austin basin's neighbors; this is a local-economy-meets-local-environment story with strong visuals, which is KVUE's wheelhouse.

**Suggested interview questions (offer these):**
1. What does a drawdown expose on a typical Lake Austin shoreline that owners can't see at full water?
2. Why does this work require amphibious equipment — what happens to conventional machines out there?
3. How many properties can realistically be restored inside one window, and what happens to owners who miss it?
4. What should a waterfront owner do right now if they suspect damage?

**Contact strategy:** News desk assignment email + one follow-up call two business days later. If no response by Oct 20, route the same access offer to KXAN's feature desk (their scheduled slot) rather than double-pitching KVUE reporters individually.

#### PRESS RELEASE SKELETON (template — fill on the scheduled date)

> **FOR IMMEDIATE RELEASE** — [Date]
>
> **Headline:** ATX Lakescapes Restores Lake Austin Shorelines During Projected Drawdown Window
>
> **Dateline:** AUSTIN, Texas —
>
> **¶1 — The news:** The City of Austin and LCRA have announced the first meaningful Lake Austin drawdown in ~10 years, projected for [Oct–Nov]. ATX Lakescapes crews are restoring private shorelines during the roughly [25]-working-day window.
>
> **¶2 — What's happening:** Two amphibious machines, committed in July, working the exposed lake bed: bulkhead repair, sediment removal, dock structure work. [X] properties scheduled, per the current count.
>
> **¶3 — Quote (Nathan):** "A drawdown shows you a decade of truth about your shoreline in a few weeks. Our job is to be ready when the water drops — equipment, permits, crews — so owners can fix in weeks what would otherwise wait years."
>
> **¶4 — Context:** What a drawdown is; why the work is impractical at full water; what the window makes possible. Hedged language throughout.
>
> **¶5 — Boilerplate:** About ATX Lakescapes — Lake Austin shoreline construction and restoration. Contact: Nathan Menkin, [phone], [email], atxlakescapes.com.
>
> **Media assets available:** Drone footage, site access, homeowner interviews (with permission), equipment b-roll.

---

### 2.7 — AD SPEND ALLOCATION + TARGETING SPECS

**Spec (Deliverable 2.7):** Produce the complete media plan — **channel allocation ($5,300/mo — SEE FLAG BELOW), audience definitions, campaign structure (ad sets, budgets, bidding), creative rotation schedule, optimization rules (kill under X, scale over Y), reporting dashboard specs.**

> **[X] BUDGET CONFIRMATION FLAG:** The $5,300/mo total and the channel split below come from the Media Dominance Calendar and are **[X] pending Nathan's confirmation.** All dollar figures in this framework are placeholders until confirmed. The *structure* (percentages, rules, audiences) is deliverable now; the *dollars* are not.

#### Proposed channel allocation (baseline from Media Dominance Calendar — every figure [X] pending confirmation)

| Channel | Monthly budget | Share | Purpose |
|---------|---------------|-------|---------|
| Meta (FB/IG) | $[2,000] | [38]% | Primary lead gen, retargeting, lookalikes |
| Google Search | $[1,500] | [28]% | "Lake Austin drawdown," "bulkhead repair Austin," "dock repair Lake Austin" |
| Google Display | $[500] | [9]% | Site retargeting, competitor-keyword conquesting |
| Nextdoor | $[300] | [6]% | Hyper-local cove/neighborhood targeting |
| Direct Mail | $[1,000] | [19]% | 500 waterfront owners, 2 waves |
| **Total** | **$[5,300]/mo** | 100% | |

**Phase weighting:** Pre-window (Jul–Sep) = full budget. Active window (Oct–Nov) = shift ~[40]% of paid spend into organic/earned media support (the work itself is the content). Post-window (Dec+) = maintenance + referral program spend only.

#### Audience definitions

| Audience | Definition | Use |
|----------|-----------|-----|
| **A1 — Cold waterfront** | Geo: Lake Austin shoreline parcels (78730/78732/78733/78734/78746 + waterfront polygon); homeowner; est. property value $2M+; age 45–70 | Problem-aware ads (2.1) |
| **A2 — Lookalike** | 1% LAL on past-client list + booked-assessment list (seed ≥[X] — flag if seed too small) | Solution-aware ads |
| **A3 — Warm retargeting** | Site visitors 30d, IG/FB engagers 60d, lead-form openers, email clickers | Solution- + most-aware ads |
| **A4 — Exclusions** | Booked assessments, deposits, completed jobs, suppression list | Excluded from ALL sets |
| **A5 — Nextdoor** | Cove-by-cove sponsorship, Lake Austin neighborhoods | Scarcity + neighbor-shade templates |

#### Campaign structure (Meta example)

- **Campaign 1 — Prospecting (COLD):** A1 + A2 audiences · problem- and solution-aware creative · [60]% of Meta budget · lowest-cost bidding, CBO.
- **Campaign 2 — Retargeting (WARM):** A3 · solution- and most-aware creative · [40]% of Meta budget · cost-cap at $[X] per lead.
- **Ad sets:** one awareness level per ad set, 2–3 ads per set, A/B pairs from 2.1 kept in the same set for clean reads.

#### Creative rotation schedule

- Weekly refresh: new scarcity count card every Mon + Thu (ties to published counts).
- Full creative rotation every [14] days or when frequency > [3.0] on warm audiences.
- Retire any creative whose hook is beaten 2 tests running.

#### Optimization rules (kill/scale)

| Rule | Threshold (all [X] pending) |
|------|------------------------------|
| **Kill** an ad | CPL > $[X] after [2,000] impressions OR CTR < [0.8]% after [1,500] impressions |
| **Kill** an ad set | CPL > $[X] after [7] days at full budget |
| **Scale** | CPL < $[X] AND ≥[5] leads/week → raise budget [20]% every [3] days, never more per step |
| **Pause all** | Kill-switch: City/LCRA shifts the drawdown window → pause everything same-day, pivot messaging per the email suite's kill-switch protocol |
| **Never optimize toward** | Clicks or engagement. The only conversion that counts is a booked Assessment. |

#### Reporting dashboard specs

Weekly one-pager (Mondays, alongside the published count): spend by channel, impressions, CTR, CPL, booked assessments, deposits, cost per booked assessment, slot count remaining. Targets from the Media Dominance Calendar: 50K paid impressions/week, 20 assessment form fills/week. Actuals vs. target, no vanity metrics.

---

## SECTION 3 — HANDOFF INSTRUCTIONS (CLAW TEAM / GROK)

### 3.1 What you produce

Full Batch 2: **2.1** twelve ad sets · **2.2** eight video scripts · **2.3** six static concepts · **2.4** twenty subject/preview pairs · **2.5** six content templates · **2.6** five outlet pitches + press release · **2.7** media plan. The examples in Section 2 are the quality bar — finished, rule-clean, on-voice. Match the voice; don't clone the lines.

### 3.2 File naming (from AGENTS.md, mandatory)

`[AGENT]_[TYPE]_[DESCRIPTION]_[vN]_[STATUS].md` — for this batch: `GROK_MEDIA_..._v1_DRAFT.md`

Examples:
- `GROK_MEDIA_MetaAdCopy_12Angles_v1_DRAFT.md`
- `GROK_MEDIA_VideoScripts_8Reels_v1_DRAFT.md`
- `GROK_MEDIA_StaticConcepts_6_v1_DRAFT.md`
- `GROK_MEDIA_SubjectLines_20Pairs_v1_DRAFT.md`
- `GROK_MEDIA_ContentTemplates_6_v1_DRAFT.md`
- `GROK_MEDIA_MediaPitches_5PlusPR_v1_DRAFT.md`
- `GROK_MEDIA_AdSpendPlan_v1_DRAFT.md`

Status flow: **DRAFT → BOARDREVIEW → FINAL. Nothing publishes from DRAFT.**

### 3.3 Where outputs land

- Primary: Google Drive → `DRAWDOWN 2026 - Full Campaign System/08_Agent_IO/grok_outputs/`
- Alternate (if the GitHub lane is active for this batch): `REVIEW/` folder in the campaign repo
- Drive watch-outs: .gdoc/.gsheet are pointer files — save as .md. If Drive is set to "stream," open the folder once in Finder to hydrate before writing.
- Slack and Linear log the *existence* of the file (Slack = floor, Linear = ledger). The file itself lives in Drive/GitHub only.

### 3.4 The QA gate — red-team checklist (run on every file before it can move to BOARDREVIEW)

1. **Real numbers?** Every scarcity figure is either the approved structural set (2 machines / ~25 working days / committed in July), a published Mon/Thu count quoted as "as of [day]'s count," or an [X] placeholder. Zero invented numbers. The retired "47/31" line appears nowhere.
2. **Hedged drawdown language?** "Exploring / lining up / projected / pointing to." No "is happening," no unhedged dates.
3. **No competitor incapacity?** Every equipment line states what ATX locked — never what others can't get.
4. **GSM-7 if SMS-adjacent?** Any asset that will be adapted to SMS: no em dashes, no smart quotes, no emoji, ≤160 chars worst-case rendered, and flagged as SMS-adjacent in the file.
5. **BBQ test?** Read it out loud. Would Nathan say this at a BBQ? Would a $5M homeowner read it without flinching? No hype, no corporate, no exclamation-point urgency.
6. **Offer integrity?** $695 / 100% credited / 12-month validity — correct and complete wherever the offer appears. No $500 referral credit anywhere pre-window.
7. **Character limits?** 2.1 headlines ≤40, primary ≤125 (counted, not estimated). 2.4 subjects ≤50, previews ≤90. Count with the [X] fills at worst case.
8. **Aesthetic?** Cormorant Garamond + Source Sans 3; #f7f5f0 / #c4923a / #1a1a1a; no gradients, no neon, no stock-photo gloss; local/specific/real imagery only.
9. **Neighbor-shade truth?** Every neighbor-shade instance maps to a real, cove-level, current booking — or it doesn't run.
10. **One job per asset?** Every ad, script, and email pair has exactly one CTA.

**Any check fails → stays DRAFT, fix, re-run. All pass → mark BOARDREVIEW and hand to the board.**

### 3.5 What to escalate (do NOT improvise these)

- **Any number you don't have.** Write [X] and flag it. Escalate to the Mon/Thu count owner. Never estimate.
- **Drawdown status changes.** If City/LCRA news breaks mid-production, stop and escalate — hedging language may need to change campaign-wide (kill-switch protocol lives in the email suite).
- **Real testimonials.** Only quotes from client files with permission, or the approved recurring line. New quotes need Nathan's sign-off — escalate.
- **Naming people, addresses, HOAs.** Any asset that names a person, street, or HOA escalates for written permission before BOARDREVIEW.
- **Budget figures.** $5,300/mo and the channel split are [X] pending Nathan. Do not publish dollar commitments.
- **Legal/financial/customer-private material** → review queue, not final storage (per AGENTS.md watch-outs).
- **Press pitches before send dates.** KVUE pitch is written now but sends ~Oct 15; re-verify hedging the week it sends. Escalate if the calendar shifts.

---

*MEDIA_Batch2_HandoffBrief_Examples_v1 | ATX Lakescapes | DRAWDOWN 2026*
*Status: HANDOFF-READY. This brief is internal tooling — examples set the quality bar and are not themselves scheduled for publication without the standard DRAFT → BOARDREVIEW → FINAL flow.*
