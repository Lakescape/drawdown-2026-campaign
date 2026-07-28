# FINDINGS — 2026-07-27 — claude-code — VIDEO PRODUCTION SYSTEM v2.1

**Reviewed:** ATX Video Production System v2.1 (doctrine + Six Pillars + master skill + gates + eval), and `skills/atx-viral-video-producer/SKILL.md` v2.0 as implemented.
**Method:** not an abstract read. I reviewed this system's **actual output** first (`GROK_MEDIA_VideoScripts_8Reels_v1_DRAFT`, findings filed same day) and worked backward from what its gates let through.

---

## The evidence that drives every finding below

The 8-reel draft ran the full system. Its self-QA checklist ticked **8/8 boxes**, including `[x] Hedged language only` and `[x] Structural numbers only`.

Both of those were false:
- Scripts 4 and 6 shipped "**When** the water drops" — unhedged, asserting the drawdown as fact, in a **burned-in overlay**.
- Script 1 shipped "**Sediment 2–4 ft** behind the wall" — an unsourced specific measurement, against the campaign's core trust rule.

Additionally, 4 of 8 scripts require **real archive footage** ("Never stock," "real archive," "We've done this work before") while the pipeline is AI-generation-first. Nothing in the system flagged the conflict.

**A system whose own checklist certifies compliance it did not achieve has a structural gap, not an execution problem.** That is the thesis of this review.

---

## What is genuinely strong (keep, do not dilute)

1. **EPIC MUNDANE doctrine.** Rare and correct. Most contractor content dies of literalism; this fixes it at the root.
2. **Two-pole discipline (Enemy | Payoff), declared before writing.** Prevents tonal mush — the most common failure in short-form.
3. **"If it needs words to work, it failed the form."** Right call for muted-autoplay reality.
4. **Pillar 5 (Lake Austin specificity).** This is the actual moat. Generic-lake content is infinitely reproducible by competitors; $250k wake boats, Ipe, LCRA, named coves are not.
5. **Routing Gate = keyword live + 15-step test before publish.** The rarest thing in any content system: a hard stop tying publication to *lead capture actually working*. Most teams publish into a broken funnel. Keep this above all else.
6. **Real Proof / AI Myth Law.** Exactly the right law. See G2 — it has no enforcement.

---

## GAPS

### G1 — Gate 0 scores *craft*, never *truth*. This is the big one.
All Six Pillars are aesthetic/narrative tests (blockbuster treatment, polarity, comedy-with-truth, visual narrative, specificity, escalation). **Not one pillar asks "is this claim true and permitted."** So a script can score a clean GREENLIGHT while violating hedged-language and real-numbers rules — which is precisely what happened.

**Fix — add Pillar 7 as a hard veto, not a score:**
> **7. Verifiable Truth (VETO).** Every factual claim traces to a source: an approved structural number, a published Mon/Thu count, or a documented measurement. Every drawdown reference is hedged. No competitor incapacity, stated or implied. Any single failure = REJECT, regardless of pillars 1–6.

Pillars 1–6 are scored and can trade off. Pillar 7 cannot. A beautiful non-compliant piece is worth less than nothing — it damages the trust the campaign is built on.

### G2 — The Real Proof / AI Myth Law has no gate artifact
The doctrine states it. Pipeline Stage 4 mentions "Real footage vs AI mythology designation." But nothing *blocks* on it, so 4 scripts sailed through demanding archive footage the pipeline cannot produce.

**Fix:** make the designation a **required, per-shot, machine-checkable column** produced at Gate 0 — not Stage 4. Every shot is `REAL` or `AI` before a single credit is spent. Then:
> **Hard rule:** any shot that depicts a *specific past ATX project, a real client property, or implies "our work"* is `REAL`. AI may render capability, scale, mythology, and typography — never evidence.

Gate 0 output gains one line: `REAL shots: N · AI shots: M · unresolved: 0`. Unresolved > 0 blocks.

### G3 — Self-critique is performed by the author
Stage 7 asks the producing agent to critique its own work against the pillars. That agent ticked 8/8 on a draft with two rule violations. **Self-review reliably catches taste and reliably misses blind spots** — the miss is the definition of a blind spot.

**Fix:** Stage 7 splits.
- **7a Self-critique** (keep — cheap, catches craft).
- **7b Adversarial pass** — a *different* agent, prompted to **refute**, defaulting to REJECT when uncertain, scoring only Pillar 7 + the campaign rule table. Output lands in `REVIEW/FINDINGS_*` (the process already exists — it just wasn't being used on media).

### G4 — Gate 0 is graded by the party that wants to generate
"No generation until GREENLIGHT" is the right rule, undermined by the greenlighter and the generator being the same agent with the same incentive.

**Fix:** Gate 0 GREENLIGHT requires the 7b adversarial signature, or Nathan's. Self-greenlight is not a gate.

### G5 — Kill/scale rules contradict the stated objective
The doc says *"Never optimize toward clicks or engagement. Only booked Assessments count."* — then sets a kill rule of **CTR < 0.8% after 1,500 impressions**. That is optimizing toward clicks.

**Fix:** kill/scale on **cost per booked assessment** (you have the number: $695 revenue at booking, so CPA ceiling is a real, computable figure). Demote CTR and CPL to **diagnostics** — they explain *why* something is failing, they do not decide life or death. Add the honest caveat: at low volume, per-asset attribution is noisy; judge at the campaign level until an asset clears a minimum booked count.

### G6 — No cost ceiling per concept, and now there's no excuse — real numbers exist
The system spends generation credits with no per-piece budget. Measured, from the first full episode through the Poseidon studio (EP-ATX-106, 2026-07-27):

| Measure | Actual |
|---|---|
| 4 shots (8s, 16:9) | **88 credits ≈ $8.80** |
| Per shot | ~22 credits ≈ $2.20 |
| Generation wall time | 11.4 min |
| Requested `quality: high` | silently ran `veo-3-1-fast` — verify before assuming high-tier spend |

**Fix:** Gate 0 states a **credit ceiling** for the concept. Note the multiplier the doc leaves implicit: **1-of-4 selects discipline = 4× generation cost** (~$8.80/shot delivered, not $2.20). A hero reel at 4 shots with 1-of-4 ≈ **$35** in generation. That is cheap — but it should be *stated*, so scaling to 50 assets is a decision, not a surprise.

### G7 — Nothing mandates the training-data ledger
`video-performance-log` exists as an optional modular skill. It should be mandatory infrastructure. Every generation already can be logged with prompt (authored **and** provider-enhanced), params, cost, latency, output path, plus the eventual gate outcome — that corpus is what makes a cheaper in-house model possible later, and it is only valuable if it accumulates from the first shot.

**Fix:** ledger write is **not optional and not a skill** — it is a pipeline step. No ledger row = the stage did not complete. (This is already live in the studio: `~/Poseidon/gen-dataset/ledger.jsonl`.)

### G8 — Two gate systems with colliding names
The doc's chain (Gate 0/1/2/3/Routing) and the live studio board chain (`[GATE] GEN → GRADE → ASSEMBLE → [G2] → [G3] → EXPORT → [PUBLISH-PREP]`) are different systems sharing labels. "Gate 2" means grade-strip in both — lucky. "Gate 1 (selects)" has **no card on the board**, so selects discipline is unenforced in the tool that actually runs production.

**Fix:** one chain, mapped explicitly:

| Doc gate | Board card | Enforced by |
|---|---|---|
| Gate 0 Pillars + Pillar 7 veto | `[GATE] <EP> · CONCEPT` *(new card — does not exist yet)* | adversarial pass + Nathan |
| Gate 1 Selects (1-of-4) | `[GATE] <EP> · GEN` (existing) | Nathan |
| Gate 2 Grade strip | `[GATE] <EP> · G2` (existing, now produces `review/grade-strip.jpg`) | Nathan |
| Gate 3 Draft sign-off | `[GATE] <EP> · G3` (existing) | Nathan |
| Routing Gate | `[GATE] <EP> · PUBLISH-PREP` (existing) | Nathan + keyword live test |

Adding the CONCEPT card is the only build required, and it makes Gate 0 auditable instead of conversational.

### G9 — Minor: aesthetic lock vs. render reality
Aesthetic lock is warm editorial (`#c4923a` gold / `#f7f5f0` paper). The AI render learnings ban warm-language prompts because the model blows out on them. These are reconcilable but not currently reconciled: **warmth belongs to the grade and the typography, not the prompt.** Script 3's "golden hour" open is the live example. State it in the doctrine so no one prompts their way into it.

---

## Proposed edits, in priority order

1. **Add Pillar 7 (Verifiable Truth) as a veto.** One paragraph. Highest value in the document.
2. **Move REAL/AI designation to Gate 0** with a zero-unresolved block.
3. **Split Stage 7 into self + adversarial**, adversarial by a different agent, output to `REVIEW/`.
4. **Rewrite kill/scale on cost-per-booked-assessment**; demote CTR/CPL to diagnostics.
5. **Add a credit ceiling line to Gate 0**, with the 4× selects multiplier stated.
6. **Promote the ledger from optional skill to mandatory pipeline step.**
7. **Publish the gate-mapping table**; add the CONCEPT card to the board.
8. **Add the warmth-in-grade-not-prompt note** to the doctrine.

Items 1–3 would have caught every finding in today's 8-reel review. Items 4–8 are scale insurance.

---

## One structural observation

The system is **strong on craft and weak on truth** — which is exactly inverted from the risk profile of this campaign. The audience is $2M+ waterfront owners; the campaign's own stated core mechanism is *"real numbers only… this rule has already caught multiple violations."* The doctrine knows this. The gates don't enforce it yet.

Craft failures cost you a mediocre reel. Truth failures cost you the buyer.
