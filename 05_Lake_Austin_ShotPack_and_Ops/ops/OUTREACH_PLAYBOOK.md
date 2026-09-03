# ATX Lakescapes — Layer 5: OUTREACH PLAYBOOK (Lake Austin, dam to dam)

**Prepared:** 2026-07-27 | **Owner:** L5 outreach | **Applies to:** all 39 waterfront zones (Tier A/B/C, both shores), ~1,900 Jobber clients + full lakefront-owner prospect universe
**Companion doc:** `OUTREACH_COMPLIANCE.md` — no sequence ships until its pre-flight checklist passes.
**Inputs relied on:** `HOA_CONTACTS.md` (mgmt-company leverage, CAUTION-tier boards), `L3_workops.json` (removal zones Z1–Z6, ramps, permits), `L1_profile_report.md` (1,947 Jobber rows, 12 tagged, gate-code/slip/boat fields present).

---

## PART 1 — TAG TAXONOMY (canonical, machine-readable)

### 1.1 Design rules

- Tags are **flat strings**, lowercase, `namespace:value`. One value per namespace per contact (except `seq:` and `campaign:`, which are multi-value).
- **Jobber is the system of record.** Tags sync from Jobber → outreach tools nightly; DNC writes back immediately (see §3 and Compliance doc §8).
- Current Jobber tagging is a blank slate (12 of 1,947 rows tagged; legacy values `Builder`, `boatcover`, `Hydraulic Lifts`, `Shorescreen` are preserved as `legacy:{value}` and do not affect priority).
- The 318 Jobber rows with no usable address get `geo:unresolved` and are excluded from zone/pod assignment until geocoded; 13 partial free-text address rows (e.g., "B Dock 2 slips") go to manual review.

### 1.2 Geography tags

| Tag | Format | Values | Notes |
|---|---|---|---|
| Zone | `zone:{slug}` | `n01`…`n16` (north shore), `s01`…`s20` (south shore); 39 assigned zones total | Slug = shore letter + zero-padded number from the zone map (e.g., `zone:n05` = Mount Bonnell Shores, `zone:s05` = St. Tropez, `zone:n16` = Steiner Ranch, `zone:s19` = Apache Shores). Off-lake addresses: `zone:none`. |
| Pod | `pod:{zone-slug}-{NN}` | e.g., `pod:n05-02` | 3–12-customer clusters by proximity **and shared access corridor** (same gate, same ramp, same canal grid, same driveway arm). Pods are the route-density unit for door-hanger/yard-sign economics. Prospects inherit the pod of their parcel. |
| Tier | `tier:{A\|B\|C}` | A = $3–15M waterfront estates; B = $0.5–2.5M lakefront/lake-access; C = context (inland, commercial-adjacent, off-lake Jobber towns e.g. Marble Falls/Kingsland) | From parcel valuation; C-tier contacts are never in sales sequences, only referral/review asks. |
| Shore | `shore:{N\|S}` | N or S of the main channel | Drives morning/afternoon route logic and drawdown access planning. |
| Ops zone | `ops:{Z1..Z6}` | Z1 Lower Lake (Tom Miller Dam→360, Island canal grid); Z2 360–Bull Creek arm; Z3 Mid Lake (360→Emma Long/Commons Ford, Bee Creek); Z4 North-shore mid-upper (Emma Long→Selma Hughes, Turkey Creek); Z5 Upper Lake (Quinlan→Mansfield Dam, Steiner frontage); Z6 Apache Shores interior | A contact may carry one ops tag = the removal zone its slip/shoreline falls in. This tag drives sediment/slip-dredging messaging and disposal logistics (dewatering staging at Emma Long for Z3, Walsh for Z1, etc.). |

### 1.3 Segment tags (exactly one per contact)

| Segment | Definition | Lake Austin examples |
|---|---|---|
| `segment:estate-dock` | Main-body frontage, private dock/boathouse, estate parcel | Tarrytown (n01), Rivercrest (s10), Rob Roy (s13), Davenport waterfront (s07), Four Seasons/Bridge Point (n-shore, pre-turnover) |
| `segment:canal-slip` | Canal-grid or marina-basin parcels with a deeded slip | The Island at Mount Bonnell (n05, Z1), Oyster Landing condos/slips (s03), St. Tropez private marina lots (s05) |
| `segment:arm-cottage` | Creek-arm/cove frontage, shallower water, hydrilla/sediment pressure | Bull Creek arm (n06 Courtyard side, Z2), Bee Creek (Z3), Turkey Creek (Z4), Panther Hollow (Z5), Cuernavaca/Austin Lake Hills (s15/s16) |
| `segment:hoa-park-adjacent` | Lots whose lake access runs through an HOA park/ramp/day-dock | Greenshores (n08), Apache Shores (s19), Lake Pointe (s18), Steiner Ranch Lake Club sections (n15/n16) |
| `segment:marina-commercial` | Marinas, clubs, restaurants, mixed-use waterfront (B2B) | Oyster's Landing Marina (s03), Lake Austin Marina basin (Z1), Hula Hut/Abel's/Mozart's node |
| `segment:ramp-corridor` | Parcels within ~1.5 mi land drive of a barge-capable public ramp where corridor staging is the pitch | Walsh Boat Landing corridor (Z1), Loop 360 (Z2), Emma Long (Z3), Mary Quinlan (Z4/Z5) |
| `segment:club-resort` | Membership clubs, resorts, hospitality-managed residences (B2B) | Steiner Ranch Lake Club, Tarrytown Boat Club, Lake Hills Community Association (voluntary), Four Seasons Private Residences |
| `segment:inland-offlake` | Jobber clients/prospects off Lake Austin (other Highland Lakes, inland Austin) | Marble Falls, Kingsland, Point Venture rows from L1; excluded from Lake Austin sequences |

### 1.4 Priority tags and scoring rule

`priority:{P1|P2|P3}` is **computed, not hand-set**, and recomputed nightly:

```
priority_score = tier_w × density_w × status_w × ops_w

  tier_w:    A = 3,  B = 2,  C = 1
  density_w: pod active+lapsed client count  ≥9 → 3,  4–8 → 2,  ≤3 → 1
  status_w:  active-client = 3,  lapsed = 2,  prospect = 1
  ops_w:     address inside Z1, Z2, or Z3 = 3,  Z4–Z6 = 2,  no ops zone = 1

P1: score ≥ 40   (e.g., A-tier active client in a dense Z1 pod: 3×3×3×3 = 81)
P2: score 16–39
P3: score < 16
```

Hard overrides (evaluated after scoring):
1. `lifecycle:do-not-contact` present → priority forced to P3 and all sequences suppressed.
2. `campaign:drawdown-2026` armed (LCRA/COA confirmation) → +1 tier_w equivalent bump (multiply score by 1.5, round down) for every contact whose parcel has lakebed exposure (all segments except `inland-offlake`, `marina-commercial`).
3. Booked job in Jobber within last 30 days → `seq:*` tags cleared (no marketing during active work).
4. `segment:inland-offlake` or `tier:C` → never P1.

### 1.5 Lifecycle tags (exactly one)

| Tag | Rule |
|---|---|
| `lifecycle:active-client` | Jobber job/invoice within trailing 18 months (matches TSR EBR window) |
| `lifecycle:lapsed` | Jobber history but nothing in 18+ months |
| `lifecycle:prospect` | No Jobber history (lakefront-owner universe) |
| `lifecycle:do-not-contact` | Any opt-out on any channel, complaint, or CAUTION-tier board individual (see §3.4) |

### 1.6 Data-enrichment tags (from Jobber marine fields — 72 gate codes, slip numbers, boat fields)

- `field:gate-code` — gate code on file (signals gated-community client; use for service logistics, never in copy)
- `field:slip-number` — slip on file (prime dredging/maintenance upsell target)
- `field:boat` — vessel on file (draft → sediment-depth relevance)
- `geo:unresolved` — address unusable (318 rows); geocode before sequencing

### 1.7 Campaign tags

- `campaign:hydrilla-2026` — hydrilla pressure messaging (~36% lake coverage July 2026, grass-carp program context)
- `campaign:drawdown-watch` — pre-confirmation nurture (drawdown under study, not confirmed)
- `campaign:drawdown-2026` — **armed only on COA/LCRA confirmation of a drawdown AND publication of the authorization path for it**; carries `dd:registered` / `dd:unregistered` sub-state for that path's enrollment status. ⚠️ No Lake Austin lakewide-permit registration path is confirmed to exist — see `20-analysis/PERMIT-AUTHORITY-v2-2026-08-04.md` §3.
- `seq:{S1..S7}` — current sequence enrollment (multi-value disallowed; one sequence at a time)
- `touch:{n}` + `touch-last:{YYYY-MM-DD}` — cadence position (stored in outreach tool, mirrored to Jobber note)

### 1.8 CSV header spec — `outreach-tags.csv` (one row per contact, nightly export)

```csv
jobber_id,contact_name,email,phone_mobile,phone_landline,service_address,city,zip,zone,pod,tier,shore,ops,segment,lifecycle,priority,priority_score,field_gate_code,field_slip_number,field_boat,geo_unresolved,campaigns,seq,touch,touch_last,email_optout,sms_optout,call_optout,dnc_registry_scrub_date,tx_nocall_scrub_date,consent_sms_date,consent_sms_source,last_reply_date,last_booked_date,do_not_contact,notes
```

Column rules:
- `zone,pod,tier,shore,ops,segment,lifecycle,priority` hold **bare values** (`n05`, `n05-02`, `A`, `N`, `Z1`, `canal-slip`, `active-client`, `P1`) — namespace prefixes are implicit; tag-string form is used only inside Jobber.
- `campaigns` is pipe-delimited (`hydrilla-2026|drawdown-watch`).
- `email_optout/sms_optout/call_optout/do_not_contact` are `TRUE/FALSE`; `do_not_contact=TRUE` is the master kill-switch and must equal OR of the three opt-outs plus manual flags.
- `consent_sms_date/consent_sms_source` document prior express written consent for texting (required before ANY marketing text; see Compliance §3).
- `dnc_registry_scrub_date`/`tx_nocall_scrub_date` prove the ≤31-day federal scrub and Texas No-Call scrub.

---

## PART 2 — OUTREACH SEQUENCES (7)

Channel shorthand: **E**mail, **P**hone (live, manual dial), **T**ext (consent-gated), **M**ail (postcard/letter), **D**oor-hanger. Federal/Texas constraints per channel are in the Compliance doc channel matrix (§6) — the cadences below already respect them (no marketing texts without written consent, calls 9am–9pm Mon–Sat / noon–9pm Sun Texas time, DNC-scrubbed lists).

### S1 — A-tier canal-grid estate (The Island / Oyster Landing / St. Tropez marina lots)

- **Goal:** 8–12 slip-dredging + bulkhead inspections booked before any fall drawdown; 2–3 full bulkhead replacements.
- **Audience:** `tier:A AND segment:canal-slip AND ops:Z1 AND lifecycle:(active|lapsed|prospect) AND NOT do-not-contact`. Pod-first rollout: `pod:n05-*` then `s03`, `s05`.
- **Message angle:** Canal grids trap sediment — the Island canals and Oyster Landing basin shoal visibly at 492.13 ft and will be mudflats in a -10 ft drawdown; bulkheads on these 1970s–80s canals are at end-of-life; <25 cy/address City of Austin administrative approval (LDC §25-8-261(C)(9)(a)) covers routine slip cleanouts, and anything larger needs a City variance plus an LCRA HLDO answer — **do not quote a volume allowance above 25 cy**. Lead with a free slip-depth + bulkhead condition survey (sounding pole + photo report).
- **Cadence:**
  - Touch 1 — **E** (CAN-SPAM compliant; existing clients) or **M** (prospects, oversized postcard with canal-depth photo): "What's under your slip?" survey offer.
  - Touch 2 (+7 days) — **P** live call (DNC-scrubbed; EBR clients callable even if registered): schedule the survey; reference gate/access familiarity where `field:gate-code`.
  - Touch 3 (+10 days) — **D** door-hanger timed to a Z1 crew day at Walsh Boat Landing staging ("we're on your canal Thursday") + **T** only if `consent_sms_date` exists.
- **Suppression:** booked survey → exit; any reply → human takeover; opt-out → `lifecycle:do-not-contact`; no 4th touch in 90 days.
- **Gate:** **Direct homeowner.** No HOA approval needed for marketing to Island/Oyster Landing owners (Island HOA contact NOT FOUND — do not attempt B2B there). St. Tropez marina work coordinates with Goodwin (S5).

### S2 — A-tier main-body estate (Tarrytown, Rivercrest, Rob Roy, Davenport waterfront, Bridge Point)

- **Goal:** Position ATX Lakescapes as the estate shoreline steward: bulkhead aging assessments + dock-repair pipeline; 4–6 assessments/mo.
- **Audience:** `tier:A AND segment:estate-dock AND priority:(P1|P2) AND NOT do-not-contact`.
- **Message angle:** 1960s–80s timber/steel bulkheads along Tarrytown and Rivercrest are failing in slow motion; City of Austin dock registration (5-year renewals, site-plan review before alteration) and LCRA HLDO Tier I notification make DIY repairs a compliance trap; we handle permit paperwork end-to-end. For Bridge Point/Four Seasons: developer-side vendor onboarding via Eric Moreland Group is the only door (no resident list yet).
- **Cadence:**
  - Touch 1 — **M** (letter, not postcard — privacy-appropriate for $3–15M owners): shoreline-stewardship intro + bulkhead aging photo sheet.
  - Touch 2 (+14 days) — **E** (if address known from Jobber; prospects get second **M**): "3 permits your bulkhead repair actually needs" educational piece (COA registration, HLDO Tier I, CWA 404 lakewide coverage).
  - Touch 3 (+14 days) — **P** (EBR clients) or **D** (gated prospects — hanger at gatehouse per gate policy; never trespass a gated drive).
- **Suppression:** same as S1; also suppress any parcel with an active permit application by another contractor if known (professional courtesy + avoids confusion).
- **Gate:** **Direct homeowner** for n01/s10 (no HOA in Tarrytown or Rivercrest — confirmed); **B2B-first** for Rob Roy (Spectrum gate), Davenport (Goodwin gate), Bridge Point (developer gate). Do not cold-call River Place/Courtyard board members individually (CAUTION rule, HOA_CONTACTS.md).

### S3 — B-tier volume pod (Cuernavaca/Austin Lake Hills, Apache Shores, Lake Pointe, Greenshores, Courtyard)

- **Goal:** Route-density bookings: sell clustered shoreline-maintenance days (hydrilla-skimming, debris, minor dock repair) priced per pod day, not per trip.
- **Audience:** `tier:B AND segment:(arm-cottage|hoa-park-adjacent) AND lifecycle:(active|lapsed|prospect) AND pod density_w ≥ 2 AND NOT do-not-contact`.
- **Message angle:** "Your pod, one crew, one mobilization fee." Hydrilla is at ~36% coverage lake-wide and grass carp won't clear swim areas and slip mouths on the arms; we batch 3–12 neighbors on the same access corridor so the barge/mobilization cost is split. Volume economics is the whole pitch — name the pod's corridor (e.g., "the Quinlan Park corridor," "the General Williamson park gate") so it reads as local, not blasted.
- **Cadence:**
  - Touch 1 — **E** blast to the pod (clients) + **M** postcard (prospects) with the pod-cluster offer and a named pod-day date.
  - Touch 2 (+7 days) — **T** (consent-holders only) or **P**: "2 of your neighbors are on the [date] route — want slot 3?" (Only make neighbor claims that are true.)
  - Touch 3 (+7 days) — **D** door-hangers along the access corridor the morning of the crew day + yard sign at the first job (with owner's written OK).
- **Suppression:** pod-day full → sequence pivots remaining contacts to next pod-day date; LHCA members-only park (Cuernavaca) — no staging claims without member sponsorship; violators-towed policy means never promise park access.
- **Gate:** **Hybrid.** Direct homeowner for arm-cottage; **B2B gate required** where access/staging runs through HOA park (Apache Shores → Spectrum, Lake Pointe → Cohere, Greenshores → CAUTION/unverified mgmt, Courtyard → Goodwin). The S5 B2B sequence must land before S3 door-hangers in gated pods.

### S4 — Ramp-corridor (Walsh, Loop 360, Emma Long, Mary Quinlan)

- **Goal:** Fill the sediment-removal calendar in Z1–Z4 by selling around our staging reality: we already pay the ramp fees and mobilization, so corridor homeowners get slip/shoreline cleanout pricing without a mobilization charge.
- **Audience:** `segment:ramp-corridor AND ops:(Z1|Z2|Z3|Z4) AND lifecycle:(active|lapsed|prospect) AND NOT do-not-contact`, radius-banded by ramp: Walsh (Z1), 360/Pennybacker (Z2), Emma Long (Z3), Mary Quinlan (Z4/Z5).
- **Message angle:** Operational honesty: "Our barge is launching at Emma Long the week of [date]; disposal runs to our dewatering yard, not your lawn." Address the objection B-tier owners have: sediment jobs smell like permit hell — we carry COA <25 cy admin approval or drawdown registration, TCEQ turbidity BMPs, and spoil handling (TDS Creedmoor / clean-fill reuse) as standard.
- **Cadence:**
  - Touch 1 — **M** postcard: ramp-week announcement for their corridor (photo of barge at their ramp).
  - Touch 2 (+5 days) — **P** live calls (scrubbed; 9am–9pm M–Sat): book corridor-week inspections.
  - Touch 3 (ramp-week) — **D** hangers on corridor streets + **E** recap with before/after sonar shots from that week's jobs.
- **Suppression:** ramp closure risk (360 and Mary Quinlan close below 492 ft) — if lake drops, sequence auto-pauses and pivots contacts into S7/drawdown messaging instead of selling barge work we can't stage.
- **Gate:** **Direct homeowner.** Commercial use of Walsh requires a PARD permit — that's our ops problem, not marketing copy; never imply City endorsement.

### S5 — HOA / management-company B2B (Goodwin / Spectrum / Cohere leverage play)

- **Goal:** Get ATX Lakescapes on the approved-vendor lists of Goodwin & Company (5 target associations: Courtyard n06, St. Tropez s05, Davenport s07, SRROA n16, River Place Estates n12), Spectrum (Apache Shores s19, Rob Roy s13), and Cohere (Lake Pointe s18) — one relationship each, 8 gated lakefront communities. Secondary: common-area shoreline work (HOA parks, day docks, marina at St. Tropez, Steiner Lake Club frontage) as B2B contracts.
- **Audience:** Management-company account managers and on-site offices from HOA_CONTACTS.md leverage map: Goodwin (855-289-6007 / account managers per association), Spectrum Austin (512-834-3900), Cohere Lake Pointe (lakepointe@coherelife.com); plus Legacy Southwest (Riverplace), Alamo/on-site (Steiner Master), Inframark (River Place LD). **CAUTION-tier boards (Mt Bonnell Shores volunteer board, LHCA, Greenshores-unverified, Coldwater, Watersedge, Hidden Valley) are NOT in this sequence** — general-contact-form/PO-box only, never individual directors.
- **Message angle:** Vendor-packet play: COI + W-9 + license/insurance + Lake Austin permit fluency (COA dock registration, COA <25 cy administrative approval + variance path, HLDO Tier I/II, TPWD/LCRA aquatic-treatment approvals) + references from their own communities (only with client permission). Offer a no-cost common-area shoreline condition report (their park/day-dock/marina) as the door-opener — that's a deliverable the manager can hand their board.
- **Cadence:**
  - Touch 1 — **E** to the named account manager (B2B email still requires CAN-SPAM footer) with one-page vendor packet + specific community reference ("we already serve 6 Steiner Ranch lakefront owners").
  - Touch 2 (+10 days) — **P** to the management office main line (business numbers; DNC Registry doesn't cover B2B lines but log opt-outs anyway) asking for the vendor-application process.
  - Touch 3 (+14 days) — **M** physical packet to the office address (Goodwin 11960 Jollyville Rd / per-association site; Spectrum 901 S. MoPac Bldg 1 Ste 300; Cohere on-site team) + offer to present at a board meeting (Courtyard meets 3rd Tuesdays; Apache Shores 3rd Wednesdays).
- **Suppression:** "we have a vendor" → tag `b2b:incumbent-vendor`, recycle in 6 months; any manager opt-out propagates to every association that manager controls (do not route around a Goodwin "no" via a different Goodwin manager).
- **Gate:** This **is** the gate. S2/S3/S7 homeowner touches inside gated communities may proceed in parallel, but door-hanger/staging activity in those communities waits for S5 clearance.

### S6 — Existing-client maintenance upsell (slip-number / gate-code / boat-field holders)

- **Goal:** Convert the 1,900-row Jobber base into recurring shoreline-maintenance plans; reactivate lapsed marine clients; monetize the marine data fields (72 gate codes, slip numbers, boat fields) nobody has ever marketed against.
- **Audience:** `lifecycle:(active|lapsed) AND NOT do-not-contact`, ranked: (1) `field:slip-number` + `ops:Z1-Z3`, (2) `field:boat`, (3) `field:gate-code`, (4) remainder by priority. Exclude `segment:inland-offlake` from lake-specific offers (they get a versioned other-lakes offer or nothing).
- **Message angle:** "We already know your gate code and your slip — let us keep it dredged, floated, and insured-up." Annual plan bundles: spring hydrilla skim + fall slip-depth sounding + storm-debris response + dock/bulkhead photo inspection (documentation owners want for insurance and resale). Lapsed angle: "your last service was [date]; Lake Austin hasn't sat still since" with the 2017-drawdown-to-today shoreline change.
- **Cadence:**
  - Touch 1 — **E** personalized with their actual Jobber fields (last service date, slip # if present). Personalization is the deliverability and conversion lever; no generic blasts.
  - Touch 2 (+7 days) — **P** (EBR = exempt from DNC Registry restriction within 18-mo purchase / 3-mo inquiry windows, but honor internal opt-outs instantly; log EBR basis per call).
  - Touch 3 (+7 days) — **T** appointment-setter text **only** where `consent_sms_date` exists; otherwise second **E** with plan-pricing one-pager.
- **Suppression:** plan sold → move to `lifecycle:active-client` + service-comms stream (transactional, CAN-SPAM-exempt-primary-purpose but still no false headers); decline → 180-day recycle; any "stop" on any channel → immediate `do-not-contact`.
- **Gate:** **Direct homeowner.** Where the client's gate code belongs to a Goodwin/Spectrum/Cohere community, no additional B2B permission is needed to service an existing client (resident authorization covers contractor entry), but S5 goodwill applies.

### S7 — Drawdown-window campaign (TRIGGERED — do not arm early)

- **Trigger (all required):** (a) City of Austin/LCRA formally announce a Lake Austin drawdown (fall-2026 window under study as of 2026-07-27; Jan–Feb window being petitioned by Friends of Lake Austin), AND (b) the agencies publish the actual authorization path for work in that window (⚠️ **not** assumed to be an LCRA/USACE lakewide permit — no such path is confirmed for Lake Austin; see `PERMIT-AUTHORITY-v2-2026-08-04.md` §3). Until both, only `campaign:drawdown-watch` nurture runs (educational, no deadline claims — **never** claim a drawdown date before confirmation).
- **Goal:** 100% of lakefront contacts registered (or ATX-registered-on-behalf) before the window; pre-sold bulkhead/slip/ramp repair schedule packed across all six ops zones; land-based pricing (no barge) locked in writing.
- **Audience:** everyone `zone:*` lakefront except `do-not-contact` and `inland-offlake`; priority order P1→P3; pod-clustered for Z5 (upper lake ramp scarcity — land-based crews) and Z6 (Apache Shores interior — POA permission mandatory).
- **Message angle:** The drawdown is the once-a-decade window: exposed lakebed makes wall/slip/ramp repair and slip cleanouts reachable, site-plan exemption applies to ≤25 cy cleanouts, and land-based equipment replaces barge day-rates. ⚠️ **Quote no volume allowance above the City's 25 cy** unless the announced authorization path states one in writing — the old "2,000 cy per registered address" line is retracted (`PERMIT-AUTHORITY-v2-2026-08-04.md` §3). Deadline pressure is real and legal **only because** the window is agency-announced — cite the announcement in every piece.
- **Cadence (compressed, 3 touches in 21 days):**
  - Touch 1 (announcement +0–3 days) — **E** all opted-in + **M** postcard all lakefront: "The drawdown is confirmed. Registration is open. Here's your address-specific plan." Include registration deadline and our we-register-you offer.
  - Touch 2 (+7 days) — **P** call blitz in pod order (EBR first, then scrubbed prospects) + **T** to consent-holders with registration-confirmation links.
  - Touch 3 (+14 days) — **D** door-hangers + yard signs in booked pods; final-deadline **E**.
- **Suppression:** `dd:registered` → shift to scheduling stream, stop selling; window closes → all drawdown creative killed same day (stale deadline claims = deceptive); if the drawdown is cancelled, every armed contact gets a correction touch (trust preservation).
- **Gate:** **Hybrid.** Registration is per-address (homeowner signs or authorizes us); Z6 Apache Shores interior and any HOA-park staging require the S5 B2B relationships already in place. This sequence is where S5 pays off.

---

## PART 3 — FOLLOW-UP & TAGGING RULES (every touch updates tags)

### 3.1 Event → tag-update table (enforced in outreach tool, synced to Jobber same day)

| Event | Tag mutation | Timing |
|---|---|---|
| Any reply (email/text/phone/mail QR) | Remove from `seq:*`; create Jobber task for human follow-up; `last_reply_date` set | Immediate |
| Positive reply / request for quote | `priority` bump one level (P3→P2→P1, P1 stays); note angle that worked | Immediate |
| Booked (survey/job/plan) | `lifecycle:active-client`; clear `seq:*` and `campaign:*` sales tags; `last_booked_date` set; move to service-comms stream | Immediate |
| Completed job | Recompute `density_w` for the pod (pod count +1); if job created a new pod member, split/merge pods at ≥12/≤3 thresholds | Nightly |
| Email unsubscribe / "stop" text / verbal "don't call" / written request | `lifecycle:do-not-contact` + channel flag(s) + master `do_not_contact=TRUE`; propagate per Compliance §8 (Jobber, outreach platform, dialer, SMS platform, mail house suppression file) | Same business day; legal max 10 business days (CAN-SPAM), 10 business days (TCPA revocation), but house standard = 24h |
| Hard bounce / disconnected number | Channel flag `email:invalid` / `phone:invalid`; attempt append; after 2 failures suppress channel | Nightly |
| No response after touch 3 | `seq:*` cleared; 90-day cooling tag `cooldown:until-YYYY-MM-DD`; re-eligible to a *different* sequence after cooldown | Nightly |
| Drawdown registration confirmed for address | add `dd:registered`, remove from S7 selling touches | Immediate |
| New parcel sale (new owner) | `lifecycle:prospect` reset, `touch` reset, new-owner welcome angle | On TCAD refresh |

### 3.2 DNC propagation (summary — full procedure in Compliance §8)

One opt-out, everywhere: Jobber tag → outreach platform suppression → dialer DNC → SMS platform blocklist → mail suppression file → re-export `outreach-tags.csv` flag check blocks all seven sequences. A contact with `do_not_contact=TRUE` may still receive **transactional** service communications (scheduling, invoices) but zero marketing.

### 3.3 Reply-to-booking SLA

P1 replies: human response within 2 business hours. P2: same business day. P3: next business day. All replies answered by a named person (never a no-reply address) — replies are where A-tier estate work is won.

### 3.4 CAUTION-tier standing rule

Volunteer/self-managed boards (Mt Bonnell Shores, LHCA/Cuernavaca, Greenshores-unverified, Coldwater, Watersedge, Hidden Valley, Austin Lake Estates, civic orgs like WANG): outreach only via official contact form/PO box/office email, never to individual board members' personal contacts, and any member of those boards who is individually in our customer/prospect file is marketed to **as a homeowner only**, with zero reference to their board role.

---

*End of playbook. Compliance pre-flight (OUTREACH_COMPLIANCE.md §9) must pass before any sequence ships.*
