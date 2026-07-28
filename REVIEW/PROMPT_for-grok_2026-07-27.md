# Copy-paste prompt for Grok — Batch 2 fix pass + system v2.2

---

A review pass landed on your Batch 2 work and the production system. Both files are in the repo — read them first, they're specific:

- `REVIEW/FINDINGS_2026-07-27_claude-code.md` — findings on `GROK_MEDIA_VideoScripts_8Reels_v1_DRAFT`
- `REVIEW/FINDINGS_2026-07-27_claude-code_SYSTEM-v2.1.md` — findings on the video production system v2.1

The scripts are strong work — spec-complete, correct offer triad, no invented scarcity, no competitor-incapacity claims, all inside the 8–15s bound. The findings are about the gates, not your craft.

## Do these, in order

**1. Fix the two MAJORs in the 8-reel draft.** Ship as `GROK_MEDIA_VideoScripts_8Reels_v2_DRAFT.md` (new filename per the versioning rule, don't edit v1 in place):

- **Scripts 4 and 6** both say "**When** the water drops" in a burned-in overlay. That asserts the drawdown as fact — direct violation of the hedging rule. Your Script 3 gets it right ("a rare low-water window **is lining up**"). Fix 4 and 6 to match that register.
- **Script 1** says "**Sediment 2–4 ft** behind the wall." That's an unsourced specific presented as a general truth about the viewer's property. Either cite a source or drop to observed language ("Sediment builds behind the wall. Tie-backs rot where you can't see."). Real-numbers-only is the campaign's core trust mechanism.

**2. Split all 8 scripts into REAL-ONLY vs AI-ELIGIBLE and put it in the doc.**
Your own doctrine already has the law — "AI generates mythology and scale. Real footage carries evidence. AI never pretends to be the proof." It just isn't enforced anywhere in the pipeline, so 4 scripts shipped requiring archive footage an AI pipeline can't produce.

- REAL-ONLY: 1, 4, 6, 8 — anything showing "our work," a real cove, or a past project. Script 8 literally says "We've done this work before" over "real archive."
- AI-ELIGIBLE: 2, 5 (equipment capability, non-project-specific), 7 (pure typography).

Add a per-shot `REAL | AI` column to every script table. Unresolved = blocks generation.

**3. Add Pillar 7 to the system as a hard veto.** This is the highest-value edit in either document:

> **7. Verifiable Truth (VETO).** Every factual claim traces to a source: an approved structural number, a published Mon/Thu count, or a documented measurement. Every drawdown reference is hedged. No competitor incapacity, stated or implied. Any single failure = REJECT, regardless of pillars 1–6.

Why: all six current pillars test *craft* (blockbuster treatment, polarity, visual narrative, specificity, escalation). None tests *truth*. That's how the 8-reel draft self-QA'd 8/8 — including `[x] Hedged language only` — while shipping two rule violations. Pillars 1–6 can trade off. Pillar 7 can't.

**4. Split Stage 7 (self-critique).** Keep the self pass, add an adversarial pass by a *different* agent prompted to refute, defaulting to REJECT when uncertain, scoring only Pillar 7 + the campaign rule table. Output goes to `REVIEW/FINDINGS_*`. Self-review catches taste and misses blind spots — that's what a blind spot is.

**5. Fix the kill/scale contradiction.** The system says "never optimize toward clicks or engagement. Only booked Assessments count," then sets a kill rule of CTR < 0.8% after 1,500 impressions. That *is* optimizing toward clicks. Kill and scale on **cost per booked assessment**; demote CTR and CPL to diagnostics that explain failure rather than decide it. Note that per-asset attribution is noisy at low volume — judge at campaign level until an asset clears a minimum booked count.

## Two things already done on this side, don't duplicate

- **Script 7 "The Honest Math" is produced.** Pure typography, 10s, 1080×1920, campaign palette (#f7f5f0 / #c4923a / #1a1a1a). No AI generation, no footage. Note: the locked brand fonts (Cormorant Garamond, Source Sans 3) are **not installed** on the production machine — it rendered with Didot/Helvetica substitutes. Someone needs to install the real faces before this ships.
- **Scripts 2 and 5 are in AI generation now** (9:16, equipment/capability shots only, no implied past project). Prompts are written cool/neutral deliberately — the render model has a structural warm bias and blows out on warm prompt language. **Warmth belongs in the grade and the typography, never in the generation prompt.** Your Script 3 opens on "golden hour," which will blow out if generated rather than shot.

## Useful numbers for the credit ceiling item

Measured on a full 4-shot episode through the studio, 2026-07-27:
- 4 shots (8s each) = **88 credits ≈ $8.80**, ~22cr/shot, 11.4 min wall time
- Requested `quality: high` silently ran `veo-3-1-fast` — verify before assuming you're buying the high tier
- **1-of-4 selects discipline = 4× that.** A 4-shot hero reel with proper selects ≈ **$35** in generation. Cheap — but it should be stated in Gate 0 so scaling to 50 assets is a decision, not a surprise.

## Ground rules unchanged

DRAFT → BOARDREVIEW → FINAL. Nothing publishes from DRAFT. New versions get new filenames. Findings land in `REVIEW/`. Linear is the task ledger, Drive holds files, Slack is the sales floor.
