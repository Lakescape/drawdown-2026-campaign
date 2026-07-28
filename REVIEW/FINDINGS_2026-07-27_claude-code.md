# FINDINGS — 2026-07-27 — claude-code

**Reviewed:** `REVIEW/GROK_MEDIA_VideoScripts_8Reels_v1_DRAFT.md` (Deliverable 2.2, 8 reels)
**Against:** `01_FINAL_Deliverables/MEDIA_Batch2_HandoffBrief_Examples_v1.md` §1A/1B, `02_Operating_System/AGENTS.md`, `RECONCILIATION_Sheet_2026-07-27.md`
**Reviewer context:** also assessing production feasibility through the Poseidon studio (AI generation pipeline, DockBotclaw).

**Overall:** high quality. Spec-complete (visual direction per shot, sound cues, 2-second hook, overlay specs, 9–13s all inside the 8–15s bound). Offer triad correct in every script. No invented scarcity; no competitor-incapacity claims; the retired "47 machine-days" line does not appear. Two MAJORs below are rule violations, not taste.

---

## BLOCKER

### B1 — "Never stock" + real-archive requirement is incompatible with AI-generated footage
**Where:** Script 1 shot note ("Use real past low-water or inspection footage if current drawdown footage does not yet exist. **Never stock.**"); Script 4 ("archival or illustrative low-water reveal"); Script 6 ("real or past project"); Script 8 ("**real archive**", "We've done this work before").

**Issue:** These scripts require *real ATX footage of real past work*. The Poseidon studio produces **synthetic (Veo) footage**. Generating a shoreline that implies "our past project" — especially under Script 8's "We've done this work before" — would put fabricated evidence in front of the exact audience whose trust the campaign is built on. This is the same class as the retired "47 machine-days" line: an invented specific presented as fact. It also contradicts the existing house rule that named-project imagery must be real, not AI.

**Suggested fix:** Split the 8 into two production tracks before anything is generated:
- **REAL-ONLY (no AI):** Scripts 1, 4, 6, 8 — anything showing "our work," a real cove, or past projects. Shoot or pull from archive. `05_Lake_Austin_ShotPack_and_Ops/shot-pack/` already has a KML shotlist + Earth Pro runbook for exactly this.
- **AI-ELIGIBLE:** Scripts 2, 5 (equipment/machine capability, non-project-specific), 7 (pure typography — no footage at all).
Decision needed from Nathan before any generation spend.

---

## MAJOR

### M1 — Unhedged drawdown language in Scripts 4 and 6
**Where:** Script 4, 0:02–0:07 overlay: "**When the water drops**, a decade of damage becomes visible." · Script 6, 0:00–0:03 overlay: "**When the water drops**, the work becomes possible."

**Issue:** Direct violation of the hedging rule (Brief §1B: never assert the drawdown is happening; use "lined up / projected / pointing to"). "When" presumes occurrence and states it as certainty in a burned-in overlay — the least deniable place it could appear. Script 3 ("a rare low-water window **is lining up**") and Script 6's own later line ("if it opens") show the correct register, which makes the inconsistency more conspicuous, not less.

**Suggested fix:** "**If** the water drops…" or "As the water drops…" or recast: "A low-water window would make a decade of damage visible."

### M2 — "Sediment 2–4 ft behind the wall" asserts an unsourced specific
**Where:** Script 1, 0:02–0:06 overlay.

**Issue:** "Real numbers only" is the campaign's core trust mechanism. This is a concrete measurement presented as a general truth about the viewer's bulkhead, with no source in any campaign document. If a $5M homeowner's wall has 8 inches of sediment, the brand just missed by 4×.

**Suggested fix:** Source it, or hedge to observed language: "Sediment builds behind the wall. Tie-backs rot where you can't see." Loses nothing.

---

## MINOR

### m1 — Script 3 opens on "golden hour" (production hazard)
**Where:** Script 3, 0:00–0:02 visual.
**Issue:** If produced by AI, "golden hour" is an explicitly banned prompt term in the studio's locked render learnings — the model has a structural warm bias and blows out on that phrase. Note the distinction: the campaign's warm-editorial *palette* (#c4923a gold accent on #f7f5f0 paper) is a graded/typographic warmth, not blown-out golden-hour glow. If shot real, no issue.
**Suggested fix:** Specify "late-afternoon side light, neutral white balance, gold reserved for the end card," or shoot it real.

### m2 — Em dashes in burned-in overlays that may be repurposed to SMS
**Where:** Script 1 ("visible — and fixable"), Script 2 end card ("$695 Assessment — fully credited"), Script 6 ("$695 Assessment — 100% credited").
**Issue:** Brief rule 5 requires GSM-7 safety for SMS-adjacent copy and asks that such assets be flagged. Overlay lines are the most likely copy to be lifted into SMS/captions verbatim.
**Suggested fix:** Flag these lines as "video-only, re-write before SMS reuse," or swap to a colon/period now.

### m3 — Script 5 cannot be pre-rendered
**Where:** Script 5 end card: "As of [Mon/Thu]'s count: [X] slots remain."
**Issue:** Correctly uses the placeholder — but that makes this asset a **template**, not a fixed deliverable. It must be re-rendered against each Mon/Thu published count, and goes stale within days.
**Suggested fix:** Treat Script 5 as a reusable template with a burn-in step in the publish workflow; note its shelf life explicitly so nobody schedules a stale count.

### m4 — Script 8 makes a time-sensitive operational claim
**Where:** Script 8: "Past clients are already being reached," "We're already calling."
**Issue:** True only if outreach is actually live at publish. Day-1 manual ops run Jul 27–Aug 13 per the Reconciliation Sheet, so plausible now — but this reel becomes false if scheduled ahead of, or long after, the calling window.
**Suggested fix:** Bind Script 8 to a publish window in the calendar; verify at schedule time.

---

## Production note (not a finding)

Script 7 is pure typography — no footage dependency, fully producible today, and the offer-clearest of the eight. Strongest candidate for first asset out the door while B1 is being decided.

The draft's own "next: generate keyframes/motion for Script 1 and Script 2 as priority pilots" should be re-ordered if B1 lands REAL-ONLY: **Script 1 is in the real-footage bucket.** Pilots would become Scripts 2 and 7.
