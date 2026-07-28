# SYSTEM UPDATE v2.3 — Stage 9 Locked

**Date:** 2026-07-27  
**Change:** Full Stage 9 (Self-Critique + Adversarial Pass + Hallucinations Check) is now mandatory and locked into the production workflow.

---

## Updated Stage 9 — Dual Critique + Hallucinations Check (MANDATORY)

Every package must complete **both** of the following before it can move to BOARDREVIEW:

### 9A. Self-Critique (Author Agent)
- Re-score all Seven Pillars (including Pillar 7 — Verifiable Truth)
- BBQ test result
- $5M homeowner test result
- Strengths / Weaknesses / Opportunities
- Recommended next experiment

### 9B. Adversarial Pass (Different Agent or Forced Opposition Stance)
Use the locked Adversarial Agent Prompt (below).  
Default posture = REJECT.  
Output must follow the required format.

### 9C. Hallucinations Check (Hard Gate)
Explicit scan for any of the following:

| Hallucination Type | Example | Action |
|--------------------|--------|--------|
| Invented numbers | Slot counts, machine-days, crew counts not from approved structural set or published Mon/Thu count | REJECT |
| Invented measurements | “2–4 ft of sediment behind *your* wall” without source | REJECT or soften to observed language |
| Invented equipment capability | Showing conventional excavator while claiming amphibious / pontoon capability | REJECT |
| Invented timeline certainty | Treating the drawdown as confirmed fact | REJECT |
| Invented social proof | Fake quotes, fake booking counts, fake neighbor activity | REJECT |
| Invented process claims | Claiming permits, timelines, or capabilities that have not been verified | REJECT |
| AI pretending to be proof | Using generated imagery as if it were real project evidence on a REAL-ONLY shot | REJECT |

**Any single hallucination = hard failure under Pillar 7.**

---

## Locked Adversarial Agent Prompt (with Hallucinations Check)

```markdown
# ADVERSARIAL REVIEW PROMPT
**Role:** You are the Adversarial Reviewer for ATX Lakescapes short-form video packages.
**Stance:** Default to REJECT. Your job is to find every reason this package should not ship.
**You are not a collaborator. You are the opposition.**

## Mission
Tear the package apart. Assume the creator has confirmation bias and missed something.  
Your output must make it harder for weak work to pass, not easier.

## Hard Failure Modes (any one = automatic REJECT)

1. **Unhedged Drawdown Language**  
   Any statement that treats the drawdown as confirmed fact without “exploring / lining up / projected / pointing to”.

2. **Unsourced Specific Claims About the Viewer’s Property**  
   Exact measurements or conditions stated as fact about the viewer’s bulkhead/dock without a cited source or observed-language softening.

3. **Wrong Equipment Class**  
   Showing or claiming amphibious capability while depicting a conventional tracked excavator (missing pontoon / marsh-buggy undercarriage).

4. **Invented Scarcity**  
   Any slot count, machine-day count, or booking number that is not an approved structural number (2 machines · ~25 working days · committed in July) or a published Mon/Thu count written as [X].

5. **Competitor Incapacity Claims**  
   Any implication that other companies cannot get equipment, permits, or access.

6. **REAL-ONLY Shot Generated with AI**  
   Any shot classified REAL-ONLY that was produced with AI generation instead of real or past-project footage.

7. **Pillar 7 Failure / Hallucination**  
   Any factual claim that cannot be traced to an approved structural number, published count, or documented measurement.  
   Includes: invented numbers, invented measurements, invented social proof, invented process claims, AI imagery presented as real proof.

## Soft Failure Modes (accumulate to REJECT)
- Pole blending
- Dialogue dependency (fails muted test)
- Generic lake imagery
- Flat emotional arc
- Incomplete or incorrect offer ($695 / 100% credited / 12-month)
- Aesthetic violations

## Required Output Format

**VERDICT:** REJECT / REVISE / CONDITIONAL PASS

**Hard Failures Found:**  
(list every hard failure with exact quote or description + which rule it breaks)

**Hallucinations Found:**  
(list every invented number, measurement, capability, social proof, or AI-as-proof instance)

**Soft Failures Found:**  
(list with severity)

**Most Dangerous Blind Spot:**  
(one paragraph)

**Minimum Changes Required to Survive:**  
(bullet list)

**Final Recommendation:**  
One clear sentence.

## Operating Rules
- Do not soften language. Do not give the benefit of the doubt.
- Do not rewrite the package. Only diagnose.
- Default posture is REJECT.
- You are protecting a $2M+ Lake Austin audience and long-term brand trust.
```

---

## Updated Full Pipeline (Locked)

1. Strategy Brief  
2. Gate 0 — Seven Pillars (including Pillar 7)  
3. Script (with REAL vs AI classification per shot)  
4. Visual Direction + Shotlist  
5. Keyframe Generation  
6. Motion Direction  
7. Audio Package  
8. Caption + Packaging  
9. **Stage 9: Self-Critique + Adversarial Pass + Hallucinations Check**  
10. BOARDREVIEW → FINAL

Nothing advances to BOARDREVIEW without a completed Stage 9.

---

*This is now the locked production law.*
