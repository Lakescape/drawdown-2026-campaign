---
name: atx-viral-video-producer
version: 2.0
authority: MASTER — replaces fragmented video skills for short-form production
triggers: ["produce video", "make a reel", "viral video", "hero reel", "batch 2 video", "full media pipeline", "generate reel"]
owner: Nathan / Grok CMO
---

# ATX Viral Video Producer — Master Skill v2.0

**Purpose**  
This is the single executable skill that owns the entire short-form video pipeline for ATX Lakescapes.  
When activated, Grok does not stop at a script. It produces a complete, ready-to-generate package that includes:

1. Strategy + Gate 0 verdict
2. Timed script
3. Exact image generation prompts (with negatives)
4. Image-to-video / motion prompts
5. Audio / VO / music direction
6. On-screen text + end card specs
7. Caption + CTA
8. Self-critique + improvement pass
9. Final assembly notes

The goal is that another Grok instance (or the same one) can take the output of this skill and generate the actual pixels and motion with minimal additional human direction.

---

## Governing Rules (non-negotiable)

- **Epic Mundane Doctrine** (Six Pillars) is the greenlight gate.
- **Gate 0 language only** while in Controlled Acceleration: hedged drawdown language only.
- Real numbers only: 2 amphibious machines locked · ~25 working days · committed in July. Live counts = [X] + “as of [Mon/Thu]’s count”.
- Tone: calm authority, local expertise, understatement. BBQ test + $5M homeowner test.
- Aesthetic: #f7f5f0 / #c4923a / #1a1a1a · Cormorant Garamond + Source Sans 3 · no gradients, no neon, no stock gloss.
- Offer travels as a unit: $695 · 100% credited · 12-month validity.
- No competitor incapacity claims. No referral credit pre-window.

---

## How to Run This Skill (Full Pipeline)

### INPUT
User provides one of:
- A simple brief (“Hero awareness reel for the drawdown”)
- A specific script number from Batch 2
- A reference to an existing concept

### STAGE 1 — Strategy + Gate 0 (mandatory)
Output a short block:

```
Title:
Pole: (Preparation / Capability / Problem / etc.)
Awareness stage:
Primary objective:
Keyword/CTA:
Pillar check (all 6): PASS/FAIL
Gate 0 Verdict: GREENLIGHT / REVISE / REJECT
```

If not GREENLIGHT, stop and revise.

### STAGE 2 — Timed Script (8–15s)
Produce the full table:

| Time | Visual | Sound | Text Overlay |

Hook must land in 0–2s. End with the offer line only.

### STAGE 3 — Keyframe Generation Prompts
For every major shot, write:

**Shot X — [Name]**  
Model: Flux / Grok Imagine / Midjourney (state preference)  
Prompt: [full detailed prompt]  
Negative: [strong negatives]  
Aspect: 9:16 or 16:9 for later crop  
Notes: continuity, lighting, what must match previous shot

Generate at least 2–3 keyframe prompts per script.

### STAGE 4 — Motion / Image-to-Video Prompts
For each keyframe that needs motion:

**Motion Prompt for Shot X**  
Tool: Kling / Runway / Luma / Sora (state)  
Prompt: [camera move + subject behavior + duration]  
Duration: 2–4s  
Camera: [push / pan / orbit / static]  
Intensity: subtle / medium

### STAGE 5 — Audio Direction
- VO script (if any) with exact pauses
- Music bed description + reference energy
- SFX list (water, machine, footsteps, etc.)
- Target loudness: –14 LUFS
- Sonic logo / end hit

### STAGE 6 — Caption + CTA + End Card
Full platform caption (Gate 0 compliant)  
Primary CTA  
End card exact text + visual description

### STAGE 7 — Self-Critique Loop (mandatory)
Before finalizing, run this internal critique:

1. Does the hook work muted in the first 2 seconds?
2. Is every scarcity number approved or [X]?
3. Does it pass the BBQ test and the $5M homeowner test?
4. Is the offer complete and clean?
5. Would this look at home in a premium regional magazine / Villeneuve trailer hybrid?

If any answer is weak, rewrite the weak section and note the change.

### STAGE 8 — Final Package Output
Deliver everything above in one clean markdown file named:

`GROK_VIDEO_[Title]_v1_DRAFT.md`

Then list the exact next generation actions:
- Which keyframes to generate first
- Which motion passes to run
- Assembly order

---

## Quality Bar

The output of this skill must be so complete that:
- A human can drop the prompts straight into Grok Imagine / Flux / Kling
- The resulting clips can be assembled in CapCut or Resolve with almost no additional creative decisions
- The caption is ready to paste

If the skill produces only a script or only a concept, it has failed.

---

## Relationship to Previous Skills

This master skill absorbs and supersedes:
- strategy-brief-builder
- pillar-gate-checker
- reel-script-assassin
- visual-prompt-architect
- video-visual-direction
- ai-keyframe-generator
- image-to-video-motion
- video-audio-direction

Use those only as reference libraries. This skill is the production engine.

---

## Drawdown-Specific Overlay

While Controlled Acceleration is active:
- Preferred poles: Preparation / Capability / Option Protection
- Never claim the drawdown is confirmed
- Live slot counts only as [X]

---

**Activation example**  
User: “Run atx-viral-video-producer on the Hero Drawdown Reel”  
Grok executes Stages 1–8 and returns the full package.
