# ATX Lakescapes — Layer 5: OUTREACH COMPLIANCE RULEBOOK

**Prepared:** 2026-07-27 | **Applies to:** every sequence S1–S7 in `OUTREACH_PLAYBOOK.md` | **Jurisdiction:** all contacts are Texas residents/businesses (Lake Austin, Travis County) — federal + Texas law both apply, and the stricter rule always wins.
**Status note:** Rules current as of 2026-07-27. Two items are in flux and flagged: the FCC "global revocation" provision (delayed to 2027-01-31) and the pending FCC rulemaking on TCPA revocation scope. Recheck before each campaign quarter.
**This is an operational rulebook, not legal advice; route edge cases to counsel.**

---

## 1. Regulatory map (what governs what)

| Channel | Federal law | Federal regulator/rule | Texas law |
|---|---|---|---|
| Commercial email | CAN-SPAM Act, 15 U.S.C. §§ 7701–7713 | FTC; 16 CFR 316 | Texas DTPA if deceptive (Tex. Bus. & Com. Code § 17.41 et seq.) |
| Live telemarketing calls | TCPA 47 U.S.C. § 227 + Telemarketing Sales Rule | FCC 47 CFR § 64.1200; FTC 16 CFR § 310 | Tex. Bus. & Com. Code chs. 301, 302, 304, 305 (as amended by SB 140, eff. 2025-09-01) |
| Marketing texts (SMS/MMS) | TCPA (texts = "calls" per FCC) | 47 CFR § 64.1200 | Same Texas chapters — SB 140 expressly added texts to "telephone solicitation" (§ 302.001(7)) |
| Autodialed/prerecorded calls | TCPA | 47 CFR § 64.1200(a) | Texas ch. 305 (automatic dialing/announcing devices) |
| Direct mail / door-hangers | No federal marketing statute (USPS rules, trespass/HOA gate rules apply) | — | Deceptive-practices floor only (DTPA) |

---

## 2. CAN-SPAM Act — commercial email rules (all sequences using email)

Source: FTC, "CAN-SPAM Act: A Compliance Guide for Business," https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business ; statute 15 U.S.C. §§ 7701–7713.

Operational requirements (apply to **every** commercial email — S1–S7, B2B included; there is no B2B exemption):

1. **No false/misleading header information.** From/To/Reply-To and routing info must accurately identify ATX Lakescapes as the sender (15 U.S.C. § 7704(a)(1)).
2. **No deceptive subject lines.** Subject must reflect content (§ 7704(a)(2)). Practical: "Drawdown confirmed — registration open" may be sent **only after** agency confirmation (Playbook S7); before that it is a deceptive-deadline violation.
3. **Identify the message as an ad** (§ 7704(a)(5)(A)(i)); FTC allows flexibility in how, but it must be clear and conspicuous.
4. **Valid physical postal address** in every message — street address, registered PO box, or private mailbox (§ 7704(a)(5)(A)(iii)). Use the ATX Lakescapes shop mailing address in every footer; the ESP does not insert this for you.
5. **Clear opt-out mechanism**, functioning for at least 30 days after send (§ 7704(a)(3), (a)(5)(A)(ii)).
6. **Honor opt-outs within 10 business days**; no fee, no login, no information beyond the email address; no selling/transferring opted-out addresses (§ 7704(a)(4)). House standard: suppression within 24 hours (see §8).
7. **Monitor third parties.** You cannot contract away liability — both the company whose product is promoted and the sender can be held liable (FTC guide, item "Monitor what others are doing on your behalf"). Applies to any marketing agency, list vendor, or VA sending for us; contracts must require CAN-SPAM compliance and give us suppression-list access.

**Penalty:** up to **$53,088 per non-compliant email** — the FTC inflation adjustment effective 2025-01-17 (16 CFR § 1.98, https://www.ecfr.gov/current/title-16/chapter-I/subchapter-A/part-1/section-1.98 ; FTC guide). Penalty is per message, not per campaign; a 500-address non-compliant blast is theoretical exposure in the tens of millions. Recent FTC enforcement: Verkada $2.95M, Experian $650K (missing opt-out mechanism).

Deliverability layer (not law, but enforced like it): Google/Yahoo bulk-sender rules require SPF/DKIM/DMARC and one-click List-Unsubscribe for 5,000+/day senders, spam-complaint rate <0.3% (https://support.google.com/a/answer/81126). Our volumes are under the threshold; still authenticate all sending domains.

---

## 3. TCPA — calls and texts (federal)

Statute: 47 U.S.C. § 227; rules: 47 CFR § 64.1200 (https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-L/section-64.1200).

### 3.1 Consent standard

- **Marketing calls/texts to cell phones using an automatic telephone dialing system (ATDS) or prerecorded/artificial voice require prior express written consent (PEWC)** — a written, signed agreement clearly authorizing marketing calls/texts to that number, with the number specified and consent not a condition of purchase (47 CFR § 64.1200(a)(2), (f)(9); note post-*Facebook v. Duguid*, 592 U.S. 395 (2021), "ATDS" is narrow, but **prerecorded/artificial voice and DNC rules apply regardless of dialing technology**).
- **ATX Lakescapes house rule (stricter than statute): no marketing text is ever sent without documented PEWC** recorded as `consent_sms_date` + `consent_sms_source` in `outreach-tags.csv`. Cold texting prospects is banned outright — see also Texas §4 (SB 140 makes marketing texts telephone solicitations, and the 2025 settlement leaves cold texting fully exposed).
- Live, manually dialed calls to cell phones and calls to landlines do not require PEWC but **do** require DNC compliance (§3.2) and quiet hours (§3.3).

### 3.2 Do-Not-Call

- **National DNC Registry:** no telemarketing calls to registered residential/wireless numbers absent an exemption (47 CFR § 64.1200(c)(2); TSR 16 CFR § 310.4(b)(1)(iii)(B)). **Scrub cadence: registry version no more than 31 days old at call time** (16 CFR § 310.4(b)(3)(iv), https://www.law.cornell.edu/cfr/text/16/310.4). Subscribe at https://telemarketing.donotcall.gov (FY2026: first 5 area codes free, $82/area code after — Austin needs 512/737; source: FTC registry site).
- **Established Business Relationship (EBR) exemption:** may call registered numbers for 18 months after a purchase/transaction or 3 months after an inquiry (16 CFR § 310.2(n); FCC equivalent 47 CFR § 64.1200(f)). Our `lifecycle:active-client` tag is deliberately keyed to the 18-month window; log the EBR basis for every exempt call. **EBR never overrides an internal opt-out** — once a person says don't call, they go on the entity-specific internal DNC list (16 CFR § 310.4(b)(1)(iii)(A)) and stay there until they ask back in.
- **Internal DNC policy:** written policy, maintained list, trained personnel — required for the TSR safe harbor (16 CFR § 310.4(b)(3)) and FCC rules (47 CFR § 64.1200(d): written policy available on demand, honor requests up to 5 years).
- **Texas No-Call List** scrub also required — see §4.3 (Texas applies its own list and a 60-day window to texts).

### 3.3 Quiet hours

- Federal: no telephone solicitations **before 8:00 a.m. or after 9:00 p.m.** local time of the called party (47 CFR § 64.1200(c)(1); TSR 16 CFR § 310.4(c)). Plaintiffs' firms are actively suing over marketing texts received outside these hours even with consent (Benesch, "Time Of Day TCPA Cases Inundate The Federal Docket," 2025, https://www.beneschlaw.com/insight/time-of-day-tcpa-cases-inundate-the-federal-docket/) — so quiet hours apply to our texts too.
- **Texas is stricter — and controls:** 9:00 a.m.–9:00 p.m. Monday–Saturday, 12:00 noon–9:00 p.m. Sunday (Tex. Bus. & Com. Code ch. 301; Kelley Drye, "Texas Mini-TCPA Law – FAQs for Marketing Texts," https://www.kelleydrye.com/viewpoints/blogs/ad-law-access/texas-mini-tcpa-law-faqs-for-marketing-texts ; Olshan, https://www.olshanlaw.com/Advertising-Law-Blog/Texas-Telemarketing-Law-Expands-to-Include-SMS-MMS-Messaging). All ATX Lakescapes contacts are Central Time; platforms must hard-block sends outside these windows.

### 3.4 Consent revocation (2024 FCC order — live rules)

FCC Report & Order FCC 24-24 (adopted Feb. 2024), 47 CFR § 64.1200(a)(10):
- **In force since 2025-04-11:** consumers may revoke consent **by any reasonable means**; revocation must be honored **within 10 business days** (house standard: 24h); texts must honor at minimum the keywords **STOP, QUIT, END, REVOKE, OPT OUT, CANCEL, UNSUBSCRIBE**; if texting is not two-way capable, each message must disclose an alternate opt-out method. Sources: CommLawGroup ICYMI Jan. 2026, https://commlawgroup.com/2026/icymi-issue-6-january-2026/ ; MS Law Group, https://mslawgroup.com/delayed-again-fcc-pushes-back-tcpas-revoke-all-rule-to-january-31-2027/.
- **Delayed portion:** the "global revocation" amendment (one opt-out kills all robocalls/texts from that caller across topics and channels) was waived to 2026-04-11, then extended again to **2027-01-31** by FCC Consumer & Governmental Affairs Bureau order (Jan. 2026) pending an Oct. 2025 rulemaking (FCC 25-…, comments closed Feb. 2026). Sources: NatLawReview 2026-01-13, https://natlawreview.com/article/portion-tcpa-global-revocation-rules-further-extended-now-effective-january-2027 ; Lexology 2026-01-15.
- **House rule: comply with global revocation NOW.** Our master `do_not_contact` flag already propagates one opt-out across email/text/call/mail (§8) — cheaper than tracking which revocation scopes are technically in force.

### 3.5 One-to-one consent rule — dead, but document anyway

The FCC's 2023 "1:1 consent" rule (lead-gen leads valid for one seller only) was **vacated by the Eleventh Circuit in *Insurance Marketing Coalition v. FCC*, No. 24-10277 (Jan. 24, 2025)** and the FCC formally removed the nullified rule in July 2025 (ActiveProspect 2026 compliance guide, https://activeprospect.com/blog/call-center-regulations/). Consequence: no federal 1:1 requirement, but we still (a) buy no third-party "aged leads" for texting — consent must name ATX Lakescapes, and (b) retain consent proofs (signed form, web checkbox + timestamp + IP) for 5 years.

### 3.6 Caller ID & disclosures

Transmit accurate caller ID with a number that accepts do-not-call requests during business hours (47 CFR § 64.1601(e)). No spoofing (also Texas ch. 304 caller-ID rules). Live calls open with caller name, ATX Lakescapes, and purpose (TSR; Texas ch. 302/304 disclosure duties).

### 3.7 TCPA penalties

Private right of action: **$500 per violation, up to $1,500 per willful/knowing violation**, uncapped, class-action friendly (47 U.S.C. § 227(b)(3)); FCC forfeitures and state AG actions stack on top. ViSalus TCPA judgment: $925M (class). There is no small-business carve-out.

---

## 4. Texas mini-TCPA (SB 140 era — effective 2025-09-01)

### 4.1 What changed

SB 140 (89th Leg.) amended Tex. Bus. & Com. Code **§ 302.001(7)** so "telephone solicitation" now includes "a call or other transmission, including a transmission of a text or graphic message or of an image" — SMS/MMS marketing is telephone solicitation, manual or automated. Statute: https://statutes.capitol.texas.gov/Docs/BC/htm/BC.302.htm. Analyses: Kean Miller, https://www.keanmiller.com/insights/blog/texas-law-blog/dont-text-with-texas-expansive-regulations-now-in-effect-for-text-messages-to-texas-residents/ ; Sakari, https://sakari.io/blog/texas-sms-marketing-laws-and-regulations-compliance-guide-for-businesses-texting-texas-customers.

### 4.2 Registration, bond, and the November 2025 settlement

- Chapter 302 obligates sellers making telephone solicitations (now incl. texts) to **register with the Texas Secretary of State** ($200 filing fee), post a **$10,000 bond/security**, make disclosures, and file quarterly reports. Violations of ch. 302 carry **statutory damages of $5,000 per violation** plus fees (Kean Miller, above; registration forms via TX SOS).
- **November 2025 settlement:** Texas agreed that **genuinely consent-based** marketing-text programs are exempt from ch. 302 registration/bond/quarterly reporting — but this is not a free pass: chs. 304/305 remain fully in force, the exemption does not cover cold texting, and the burden of proving consent/exemption sits on the sender. Sources: NatLawReview, "Texas SB 140 After the November Settlement: Consent In, Cold Texting Out" (2026-01-29), https://natlawreview.com/article/texas-sb-140-after-november-settlement-consent-cold-texting-out ; Varnum, https://www.varnumlaw.com/insights/texas-sb-140/.
- **ATX Lakescapes determination:** because our text program is consent-only (§3.1 house rule) we rely on the consent-based exemption and document it; **if any cold-text campaign is ever proposed, ch. 302 registration + $10,000 bond must be completed first, or the campaign does not run.** Call-only B2B programs should still be reviewed against the ch. 302.051–061 exemptions with counsel before first dial.

### 4.3 Texas No-Call List and DTPA linkage

- Texas No-Call List (administered via the PUC/AG): scrub telemarketing lists (now including text lists) and honor the **60-day prohibition window** after a number is added (NatLawReview settlement article, above; Texas No-Call program, https://www.texasnocall.com).
- SB 140 made violations of chs. 302, 304 (No-Call/caller-ID), and 305 **automatic violations of the Texas Deceptive Trade Practices Act (Tex. Bus. & Com. Code § 17.41 et seq.)**: private lawsuits with no administrative prerequisites, economic + mental-anguish damages, **treble damages for knowing/intentional violations, mandatory attorney's fees**, and repeat-recovery exposure (Sakari and Kean Miller, above). One 8:59 a.m. text is now a DTPA suit.

### 4.4 Texas quiet hours (controlling standard)

9:00 a.m.–9:00 p.m. Mon–Sat; 12:00 noon–9:00 p.m. Sun, recipient local time (ch. 301 "telephone solicitors"; texts reasonably covered via ch. 304's definition — Kelley Drye FAQ, §3.3 above). Stricter than federal 8–9, so **Texas hours govern all ATX Lakescapes calls and texts.**

---

## 5. Direct mail & door-hangers

No federal marketing-consent statute, but: (a) honest content only (DTPA deceptive-acts floor; no fake drawdown deadlines — S7 creative is killed the day the window closes); (b) respect gated access — hangers at the gatehouse per gate policy, never past a locked gate (HOA gate codes in Jobber are for service logistics, not marketing distribution); (c) USPS requirements for permit imprints if bulk mail is used; (d) opted-out contacts (`do_not_contact=TRUE`) are also suppressed from mail — it is not a backchannel around an opt-out.

---

## 6. Channel matrix by sequence

Legend: ✅ allowed under stated conditions | ⚠️ restricted | ❌ prohibited

| Seq | Email | Live phone call | Marketing text | Mail | Door-hanger |
|---|---|---|---|---|---|
| **S1 A-tier canal estate** | ✅ CAN-SPAM footer; prospects OK (cold email legal under CAN-SPAM) | ✅ DNC+TX scrub, TX hours; EBR clients exempt from registry restriction | ⚠️ PEWC only | ✅ | ✅ gate-policy |
| **S2 A-tier main-body estate** | ✅ | ✅ same | ⚠️ PEWC only (rare in this segment — assume no) | ✅ letter-preferred | ⚠️ gatehouse drop only in gated communities |
| **S3 B-tier volume pod** | ✅ | ✅ scrubbed, TX hours | ⚠️ PEWC only | ✅ postcard | ✅ only after S5 B2B clearance in HOA-gated pods |
| **S4 Ramp-corridor** | ✅ | ✅ scrubbed, TX hours | ⚠️ PEWC only | ✅ | ✅ |
| **S5 HOA/mgmt B2B** | ✅ CAN-SPAM still applies (no B2B exemption) | ✅ business lines (registry covers residential; log opt-outs anyway) | ⚠️ only on express opt-in from the manager | ✅ physical vendor packet | ❌ n/a |
| **S6 Existing-client upsell** | ✅ personalized | ✅ EBR (18-mo/3-mo) + internal-DNC honored | ⚠️ PEWC only | ✅ | ⚠️ only if already servicing at the property |
| **S7 Drawdown campaign** | ✅ (post-confirmation claims only) | ✅ scrubbed; EBR first | ⚠️ PEWC only | ✅ | ✅ per gate policy; Z6 Apache Shores needs POA permission |

Universal ❌: marketing texts without PEWC; any channel to `do_not_contact=TRUE`; calls/texts outside Texas quiet hours; pre-confirmation drawdown deadline claims.

---

## 7. Record-keeping (retention schedule)

| Record | Retention | Basis |
|---|---|---|
| DNC registry subscription, download timestamps, scrub logs (federal + Texas No-Call) | 5 years | TSR safe harbor 16 CFR § 310.4(b)(3)(iv); record rules 16 CFR § 310.5; FCC 47 CFR § 64.1200(d) |
| PEWC consent records (form, timestamp, IP, number, scope, language shown) | 5 years after last use | TCPA burden of proof on caller |
| Opt-out/revocation log (channel, date, method, propagation confirmations) | 5 years | FCC revocation rules; TSR internal-DNC |
| Campaign scripts, creative, send/call logs, EBR basis per exempt call | 5 years | TSR 16 CFR § 310.5; Texas ch. 302 recordkeeping expectation (Porter Hedges SB 140 summary, https://www.porterhedges.com/anti-corruption-and-compliance-blog/texas-expands-mini-tcpa-requirements-to-include-text-messages) |
| Vendor contracts + compliance certifications (any third-party sender/dialer/mail house) | life of contract + 5 years | CAN-SPAM third-party monitoring duty |
| TX SOS registration/bond (if ever required — see §4.2) + renewal certs | current + 5 years | Tex. Bus. & Com. Code ch. 302 |

Storage: consent + opt-out logs live in Jobber custom fields/notes (system of record) and are mirrored in the outreach platform; exports archived monthly.

---

## 8. DNC / opt-out propagation procedure (one opt-out, everywhere)

1. **Capture (any channel):** unsubscribe link, "STOP"-class keyword, verbal request on a call, mail/written request, or email reply asking to stop. Agent/platform records: contact ID, channel, timestamp, exact words/method.
2. **Tag (same business day, target ≤24h):** set `lifecycle:do-not-contact`, channel opt-out flag(s), and master `do_not_contact=TRUE` in Jobber (system of record). Legal outer limits — 10 business days (CAN-SPAM § 7704(a)(4)(A)(i)) and 10 business days (FCC revocation rule, 47 CFR § 64.1200(a)(10)) — are backstops, not targets.
3. **Propagate (same day):** Jobber sync pushes suppression to: (a) email platform global suppression list; (b) SMS platform blocklist (keyword automation + manual entry); (c) dialer/call-tool internal DNC; (d) mail-house suppression file for the next drop; (e) `outreach-tags.csv` regeneration — nightly export fails validation if any `do_not_contact=TRUE` row carries an active `seq:` value.
4. **Verify:** weekly audit — 20-record sample of opt-outs checked against all five systems; monthly full reconciliation of Jobber vs. platform suppression counts; results logged (feeds §7 records).
5. **Scope:** revocation of texting consent also kills marketing calls and mail for that contact (house adoption of the delayed FCC global-revocation standard, §3.4). Transactional service messages (scheduling, invoices, job updates) continue — they are outside CAN-SPAM's "commercial primary purpose" and TCPA telemarketing rules, but must contain no promotional content (a promo line converts them into marketing).
6. **B2B contacts:** a management-company opt-out (e.g., Goodwin corporate) propagates to every association that company manages in our map — no routing around via individual account managers.
7. **Reactivation:** only on a new, documented, affirmative opt-in from the contact; never unilaterally.

---

## 9. Pre-flight compliance checklist — must pass before ANY sequence ships

Sign-off: marketing owner + one non-sender reviewer. File completed checklist with campaign records (5-year retention).

**Audience & data**
- [ ] Audience export regenerated ≤7 days ago; `do_not_contact=TRUE`, `lifecycle:do-not-contact`, `tier:C` (sales sequences), `geo:unresolved`, and `segment:inland-offlake` (lake offers) all excluded.
- [ ] Every call/text number scrubbed against National DNC ≤31 days (16 CFR § 310.4(b)(3)(iv)) **and** Texas No-Call ≤60 days; scrub dates logged in `dnc_registry_scrub_date` / `tx_nocall_scrub_date`.
- [ ] EBR exemption list built for registered numbers being called: 18-mo purchase / 3-mo inquiry basis documented per record.
- [ ] Every SMS recipient has `consent_sms_date` + `consent_sms_source` (PEWC). Zero exceptions.
- [ ] CAUTION-tier screen: no individual volunteer-board members targeted as board members (Playbook §3.4).

**Content**
- [ ] Email: accurate From/subject, ad identification, physical postal address, working opt-out link (tested this week), List-Unsubscribe header.
- [ ] No drawdown deadline/date claims unless both S7 trigger conditions (agency announcement + published authorization path) are met and cited in the piece.
- [ ] No claims of City/LCRA/HOA endorsement; permit statements match `L3_workops.json` (<25 cy/address under LDC §25-8-261(C)(9)(a); anything larger = City variance + LCRA HLDO answer; HLDO Tier II at 500 cy **or** 500 LF; Tier III commercial dredging not available on Lake Austin).
- [ ] ⛔ **No piece quotes a volume allowance above 25 cy.** The "2,000 cy per registered address" / "LCRA-USACE Lakewide Permit" path is **retracted** — it is an Inks Lake model, and LCRA's lakewide permits cover Buchanan and Travis only. See `PERMIT-AUTHORITY-v2-2026-08-04.md` §3.
- [ ] Neighbor/pod claims in S3 copy are literally true as of send date.

**Operations**
- [ ] Send/dial windows hard-set to Texas quiet hours (9a–9p M–Sat, 12p–9p Sun CT).
- [ ] Caller ID = real ATX Lakescapes number accepting DNC requests; opening script includes name/company/purpose.
- [ ] Text platform auto-honors STOP/QUIT/END/REVOKE/OPT OUT/CANCEL/UNSUBSCRIBE; two-way enabled or alternate opt-out disclosed.
- [ ] Suppression propagation (§8) tested end-to-end this quarter; opt-out SLA = 24h staffed.
- [ ] Third-party vendors (if any) under contract with CAN-SPAM/TCPA compliance clauses + suppression access.
- [ ] Cold-text check: if any text in this sequence goes to a non-consented number → **STOP** — TX SOS registration + $10,000 bond decision required first (§4.2).
- [ ] Tagging automation live: reply/book/opt-out mutations from Playbook §3.1 verified in staging.

---

## 10. Penalty reference (why this document exists)

| Regime | Exposure | Source |
|---|---|---|
| CAN-SPAM | Up to **$53,088 per email** (per recipient-message) | 16 CFR § 1.98 (eff. 2025-01-17); FTC guide |
| TCPA | **$500/violation; $1,500 willful**, uncapped, private class actions | 47 U.S.C. § 227(b)(3) |
| Texas ch. 302 | **$5,000/violation** statutory damages + fees (registration regime) | Kean Miller SB 140 analysis |
| Texas chs. 304/305 via DTPA | Economic + mental-anguish damages, **treble** for knowing violations, mandatory attorney's fees, repeat recoveries | Tex. Bus. & Com. Code § 17.50; SB 140 linkage (Sakari/NatLawReview) |
| TSR/DNC | FTC civil penalties per call (adjusted; see 16 CFR § 1.98) + state AG actions | FTC, "Complying with the Telemarketing Sales Rule," https://www.ftc.gov/business-guidance/resources/complying-telemarketing-sales-rule |

### Source index (all accessed 2026-07-27)

- FTC CAN-SPAM guide: https://www.ftc.gov/business-guidance/resources/can-spam-act-compliance-guide-business
- CAN-SPAM statute: 15 U.S.C. §§ 7701–7713
- FTC penalty table: 16 CFR § 1.98 — https://www.ecfr.gov/current/title-16/chapter-I/subchapter-A/part-1/section-1.98
- TCPA statute/rules: 47 U.S.C. § 227; 47 CFR § 64.1200 — https://www.ecfr.gov/current/title-47/chapter-I/subchapter-B/part-64/subpart-L/section-64.1200
- TSR: 16 CFR § 310.4 — https://www.law.cornell.edu/cfr/text/16/310.4 ; FTC TSR guide: https://www.ftc.gov/business-guidance/resources/complying-telemarketing-sales-rule
- National DNC Registry (telemarketer access): https://telemarketing.donotcall.gov
- FCC revocation order status: https://commlawgroup.com/2026/icymi-issue-6-january-2026/ ; https://mslawgroup.com/delayed-again-fcc-pushes-back-tcpas-revoke-all-rule-to-january-31-2027/ ; https://natlawreview.com/article/portion-tcpa-global-revocation-rules-further-extended-now-effective-january-2027
- 1:1 consent vacatur (IMC v. FCC, 11th Cir. Jan. 24, 2025) + July 2025 rule removal: https://activeprospect.com/blog/call-center-regulations/
- TCPA quiet-hours litigation: https://www.beneschlaw.com/insight/time-of-day-tcpa-cases-inundate-the-federal-docket/ ; 47 CFR § 64.1200(c)(1)
- Texas ch. 302 statute: https://statutes.capitol.texas.gov/Docs/BC/htm/BC.302.htm
- SB 140 analyses: https://www.keanmiller.com/insights/blog/texas-law-blog/dont-text-with-texas-expansive-regulations-now-in-effect-for-text-messages-to-texas-residents/ ; https://sakari.io/blog/texas-sms-marketing-laws-and-regulations-compliance-guide-for-businesses-texting-texas-customers ; https://www.porterhedges.com/anti-corruption-and-compliance-blog/texas-expands-mini-tcpa-requirements-to-include-text-messages ; https://www.olshanlaw.com/Advertising-Law-Blog/Texas-Telemarketing-Law-Expands-to-Include-SMS-MMS-Messaging
- SB 140 November 2025 settlement: https://natlawreview.com/article/texas-sb-140-after-november-settlement-consent-cold-texting-out ; https://www.varnumlaw.com/insights/texas-sb-140/
- Texas quiet hours: https://www.kelleydrye.com/viewpoints/blogs/ad-law-access/texas-mini-tcpa-law-faqs-for-marketing-texts
- Texas No-Call List: https://www.texasnocall.com
- Google bulk-sender rules: https://support.google.com/a/answer/81126

*Recheck flagged in-flux items (FCC global-revocation rulemaking; any 2026 Texas rulemaking or SOS guidance on SB 140) quarterly.*
