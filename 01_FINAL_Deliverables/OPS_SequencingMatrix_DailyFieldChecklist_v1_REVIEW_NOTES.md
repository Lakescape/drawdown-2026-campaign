# DRAWDOWN 2026 — REVIEW NOTES
## Deliverables 4.1 + 4.2 — OPS_SequencingMatrix_DailyFieldChecklist_v1
### Pipeline Record: draft → skill poll → 1 revision → board memo → red team → FINAL

**Companion to:** `OPS_SequencingMatrix_DailyFieldChecklist_v1_FINAL.md` (v1.0)
**Revision rounds used:** 1 of 1 (quota-conscious run)
**Date:** 2026-07-27 · **Author:** DRAWDOWN 2026 Swarm — Operations Agent
**Reconciled against:** `RECONCILIATION_Sheet_2026-07-27.md` (authoritative; supersedes conflicting lines here)

---

## LAYER 1 — DRAFT

**Sources read in full before drafting (mandatory):**
1. `DRAWDOWN_2026_Operations_Playbook.md` (PRIMARY) — P1–P4 table, six sequencing rules, morning/on-site/evening routines, quality gates, safety, client-update scripts, troubleshooting.
2. `DRAWDOWN_2026_Order_of_Operations.md` — Phase gates, item 56 (crew scheduling matrix due Sep 30), item 65 ($500 referral credit, Oct 15), equipment lock owners/deadlines.
3. `RECONCILIATION_Sheet_2026-07-27.md` — binding answers; (b) after-hours silence applied to the client-update rhythm.

**Draft characteristics (later revised):**
- Playbook client-update times copied verbatim (evening touch at 6:00 PM).
- Decision tree existed but lacked a "stop at first NO" instruction and reason-code logging.
- Equipment table lacked rental hold-status placeholders; rental machines had no idle rule.
- Worked examples were two; a third (neighbor batching) added in revision.

---

## LAYER 2 — SKILL POLL (6 specialist roles, Round 1)

| # | Role | Verdict | Key objection |
|---|---|---|---|
| 1 | **Operations Lead (field reality)** | STRONG | Daily checklist runnable Day 1. Demanded: no cross-lake machine moves after 1:00 PM, and a named fallback ladder so weather days never idle a crew. |
| 2 | **Crew Lead (usability)** | WEAK | "Evening update at 6 PM" collides with the 6:00 PM silence rule — which do I follow? Also: what happens if the permit isn't physically in the packet? Must be a checkbox answer, not a judgment call. |
| 3 | **Nathan (CEO)** | STRONG | Margin protection rule correct: amphibious ($1,200–1,800/day) never on P4 without sign-off. Wanted every escalation path ending at his desk only for true emergencies — confirmed: equipment-in-water, structural collapse. |
| 4 | **Safety Officer** | STRONG | PPE/emergency items match Playbook §7 verbatim. Required lightning = immediate stop + Ops Lead all-clear in `#drawdown-ops`, not crew-level judgment. Adopted. |
| 5 | **Data Steward (Linear)** | STRONG | 6:00 PM same-day log rule preserved; required reason codes (e.g., WEATHER) so idle/weather days are auditable, and Gate 2 logged before work passes 50%. Adopted. |
| 6 | **Compliance / Real-Numbers Guard** | WEAK | Rental hold status must not be asserted — Playbook says HOLD NEEDED, deposits due Jul 31. Marked [X]. All window language hedged. Referral credit dated Oct 15 per OoO item 65, not "always on." |

**Round 1 gate result: 4 STRONG / 2 WEAK → FAIL → full revision (both WEAKs struck binding rules: after-hours silence and real-numbers).**

---

## LAYER 3 — REVISION (Round 1, final round used)

Changes applied:
1. **Evening client touch moved to 5:45 PM** with an explicit 6:00 PM CT cutoff, citing Reconciliation (b) — resolves Crew Lead + Compliance WEAKs.
2. **Permit-not-in-packet = do not depart, call Operations Lead** — added as a hard checkbox (B.1) and as Day-1 Test question 1.
3. **Reason codes** added to weather/breakdown logging (WEATHER etc.); Gate 2 must be logged before 50% is passed.
4. **Rental hold status** converted to `[X]` placeholders with owner (Benjamin) and deadline (Jul 31, OoO item 12).
5. **Half-day adjacency rule** (A.2 rule 4) and **weather fallback ladder** (A.4 rule 5) added per Operations Lead.
6. **Third worked example** (neighbor batching → cove block) added; referral credit explicitly gated to Oct 15 activation.

---

## LAYER 4 — BOARD MEMO (simulated leadership review)

**To:** Nathan, Operations Lead, Benjamin
**From:** Swarm Operations Agent
**Re:** Deliverables 4.1 + 4.2 — verdict request

One-file combined deliverable as ordered. Part A sequences by P-class → cove block → machine → week, with hard gates (permit + deposit) that no job bypasses. Part B is a zero-ambiguity crew checklist with a five-question Day-1 self-test. Every unknown is a registered `[X]` placeholder with an owner and a deadline from the Order of Operations — no invented numbers. Binding conflicts resolved in favor of the Reconciliation Sheet (5:45 PM evening touch) and the Playbook (P-class table verbatim).

**Board verdict: PASS.** No blocking objections. Two non-blocking notes: (1) cove sequence map (A.2 rule 3) is the document's biggest open dependency — due with the Sep 30 scheduling matrix; (2) Day-1 Test should be administered verbally at Safety Training Day 2 (Sep 28, OoO item 58) rather than trusted as self-study.

---

## LAYER 5 — RED TEAM

**Five weaknesses:**
1. **Single amphibious point of failure.** If the T50 or the rental goes down mid-cove-block, P1/P2 sequencing collapses onto the long-reach backup — a different capability class. Mitigation exists (breakdown cascade) but the schedule impact of a 3+ day outage is not modeled.
2. **Cove-block rigidity.** Batch-first sequencing can delay a lone P1 in a cove with no block. The decision tree handles it (create a new block) but Week 1–2 P1s need a standing "drop-everything" override that the matrix only implies.
3. **Neighbor-batching assumption.** Example 3 assumes neighbors book and permits clear by Week 4 — permit timelines (14–45 days) may not fit inside a drawn-down window for late-booked add-ons. Framed as upside, not plan; still, sales should not promise it.
4. **6:00 PM log deadline vs. field reality.** Late-running jobs put Crew Leads past 6 PM at the staging area; the log rule has no stated grace path (log from the truck?). Minor, but enforceability will drift.
5. **Client update load on Crew Leads.** Three scripted touches/day/job plus Linear logging plus change-order discipline is real overhead on a working foreman; multi-crew coves need the Operations Lead to absorb updates (noted, but not resourced).

**Three improvements:**
1. Model a **machine-outage scenario** in the Sep 30 scheduling matrix: 3-day amphibious loss, resequenced cove blocks, revenue at risk.
2. Add an explicit **P1 emergency override** line to the matrix ("a P1 with active collapse risk preempts any scheduled machine day, posted to #drawdown-ops within 30 minutes").
3. Give the **Linear log a mobile path** (log-from-site counts as on-time; staging-area arrival not required) to protect the 6 PM deadline.

---

## LAYER 6 — PLACEHOLDER REGISTER

Full register lives in the FINAL document (8 placeholders). Summary: staging address, cove route map, machine-move hours, T50 crew assignment → Operations Lead; rental hold status → Benjamin; add-on target per cove → Nathan; Ops Lead phone number → before Oct 1. None block Day 1 readiness except rental hold confirmation (Jul 31, OoO item 12 — already on the critical path).

**END OF REVIEW NOTES**
