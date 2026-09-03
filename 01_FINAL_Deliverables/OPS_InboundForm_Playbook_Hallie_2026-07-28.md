# DRAWDOWN 2026 — INBOUND FORM PLAYBOOK (Hallie)

Date: 2026-07-28
Owner: Hallie Emerson (SDR) · Backup: Nathan
Scope: interim Google Form only. Superseded the moment the Netlify inbound goes live.

---

## THE LINK

```
https://docs.google.com/forms/d/e/1FAIpQLScNaVBHgE8aM-JC2VMuJKAAIJRJQ4LL8C7d4hBEildfed_bbg/viewform
```

Public — no Google sign-in needed. Verified with a signed-out fetch (HTTP 200) on 2026-07-28.

**What it asks:** email · client name* · property address* · phone* · cove or street · how did you hear about us* · type of work · description · permit status · urgency 1–5 · access constraints. (* = required)

**What it does NOT do:** take photos. Google Forms forces a sign-in on any form with a file upload, which is what was locking clients out. Photos come in by email after submission — the form says so.

---

## BEFORE YOU SEND — 3 things

1. **Test it yourself.** Fill it out end to end from a signed-out browser (incognito). Confirm it submits and you get the response-copy email.
2. **Delete your test row.** It lands as a real response and fires a real notification. Clear it before the clients get the link, or the first "lead" in the sheet is you.
3. **Get yourself on notifications.** They currently go to Nathan only — he enabled them under his account. If a lead lands and it pings him instead of you, the 5-minute SLA is already blown. Cheapest fix: Nathan links the response sheet (Responses → Link to Sheets) and shares it with you; you watch the sheet. Adding you as a form collaborator also works but is a cross-org grant (the form lives in the Victory Boat Lifts Workspace) and may be blocked.

---

## EMAIL TEMPLATE — first two clients

Send from your own address, one at a time, not a blast. These are warm past clients; it should read like you typed it.

> **Subject:** Your shoreline, before the water drops
>
> Hi [First],
>
> Quick one. The City of Austin and LCRA have announced a drawdown this fall — the water drops a projected ten to twelve feet for roughly six to eight weeks. The dates aren't fixed yet, but it's happening, and it's the first meaningful low-water window in nearly a decade.
>
> When the water drops, everything that's been underwater on your shoreline for ten years — the bulkhead, the sediment, the base of the dock — is exposed and, for a few weeks, practical to fix. At full water the same work means crews working blind from barges, and it typically runs thirty to forty percent more.
>
> We're doing Priority Assessments ahead of the window. $695, and every dollar credits toward whatever work you decide to do — the credit holds for 12 months, so if the timing shifts it still applies. You get an on-site evaluation of the bulkhead, sediment depth, dock structure and drainage, photo and video documentation, and a written prioritized scope: what has to happen in this window, what can wait, and roughly what each piece costs.
>
> Because you've worked with us before, I'm sending you the request form ahead of anyone else:
>
> [LINK]
>
> Takes about two minutes. If you've got photos of your shoreline, email them to nate@atxlakescapes.com after you submit — that's what we assess from.
>
> Any questions, just reply here or call me.
>
> Hallie
> ATX Lakescapes

---

## SMS TEMPLATES

**Hard rule (SMS suite global rule 1): no links in outbound texts.** Reply YES is the only CTA. The link goes out *after* they reply, in the 1:1 thread, from you. Do not paste the form link into a first-touch text.

### Outbound first touch — past client (approved asset A1, verbatim)

> Hey [First], Nathan at ATX Lakescapes. Lake Austin's first drawdown in a decade is projected for Oct-Nov. Past clients book first. Reply YES to hold one.

153 characters. GSM-7. Do not retype it with smart quotes from a word processor — that silently breaks the encoding. If you rewrite it at all, re-run the GSM-7 check in the platform and re-count to under 160.

### After they reply YES — 1:1, this is where the link is allowed

> Perfect. Here's the request form — takes 2 min and gets you in the queue: [LINK] Any photos of your shoreline, text or email them over and I'll get them to Nathan.

### If they reply with a question

Do not send the link first. Answer the question, then offer the form. Any human reply pauses every sequence for that contact and routes to a human inside the 5-minute SLA.

---

## WHAT NEVER GOES IN EITHER TEMPLATE

Three laws from the CRM/SLA spec, and they are not style preferences:

1. **No invented numbers.** No slot counts, no "X spots left", no "we've booked N this week". The retired "47 machine-days / 31 spoken for" line is hard-blocked in the asset linter. The only live numbers anyone may quote are the ones on the current published Mon/Thu pin.
2. **The 2 machines / ~25 working days line is conditional.** It's real, but only send it once equipment status is verified that morning. Don't reach for it to add urgency.
3. **No referral-credit mentions.** The $500 referral program launches in October. No pre-window asset mentions it, in any channel.

Also: don't promise a drawdown date. LCRA announced the drawdown on 2026-08-29, but the WINDOW is projected, not confirmed — "it's happening, the dates aren't set" is the honest framing. The 12-month credit is what removes the risk, so lead with that instead of a date.

---

## WHEN A SUBMISSION LANDS

1. Claim it — you own the response.
2. Call within 5 minutes. Not text, not email. Call.
3. Log it same day. No log = it didn't happen.
4. If they're a fit, book the assessment. If they want to ease in, offer the photo assessment: they send shoreline photos, we give an honest read on whether the $695 is worth it.

---

## KNOWN GAPS (not yours to fix — flagging so nothing gets assumed)

- The form footer reads "This form was created inside of Victory Boat Lifts." It's owned by that Workspace, not ATX. Fine for two known clients; not fine for a public blast.
- Nothing connects the form to Linear or Slack. A submission writes a spreadsheet row and sends an email — no card, no SLA clock, no ledger entry. The webhook script exists (`03_Sync_Engine/form_webhook.gs`) but is unwired; it needs a `/webhooks/form` endpoint that isn't built.
- `#drawdown-inbound`, `#drawdown-pipeline` and `#drawdown-war-room` don't exist yet. `#drawdown-planning` is the only drawdown channel in the workspace.
- All of the above is why this form is interim. The Netlify inbound replaces it.
