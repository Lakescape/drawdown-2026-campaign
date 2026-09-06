# Hard pass — drawdown song lyrics against the savage voice

2026-09-06. Ran `atx-savage-voice` + `doctrine/voice-negative-constraints.md` +
`doctrine/two-poles-reference.md` against all five songs. This supersedes the
craft judgments in `LYRIC-EXCAVATION-2026-09-04.md`; it does not supersede the
claim rules in `LYRICS-v2.md`.

## The scanner does not catch this

`bash pipeline/scripts/voice-qa.sh LYRICS-v2.md` → **0 hard, 0 warn.** Clean.

The lyrics pass every mechanical gate and are still weak, which is exactly what
the doctrine predicts: the scanner catches banned phrases and the retired 512
number; rhythm, specificity, pole tie-back and hook strength are human. No
automated check in this repo would have flagged what is wrong here.

## Root cause — I wrote to the wrong brief

I wrote to `PROMPTS.md`: *"calm authority, BBQ-test, not a carnival, not a
jingle."* That brief is real, but it is the **reel VO brief**, not the brand
voice. The brand voice is `atx-savage-voice`: Abbott Elementary deadpan ×
Liquid Death, 30–40% meaner than corporate, **funny because specific and true**.

Never loaded that skill. Result: five songs in one register — reverent,
elegiac, crew-centric, zero jokes, zero receipts. Respectful where the brand is
supposed to be sharp.

## Structural failure — pole blending

`two-poles-reference.md`: *"Every piece commits to exactly ONE pole... Tonal
blending mid-piece is an automatic reject (Pillar 2)."* None of the five
declared a pole. Four blend.

| Song | Pole behaviour | Verdict |
|---|---|---|
| A The Window | ENEMY verse 1 → PAYOFF chorus/verse 3 (craft) → ENEMY bridge | **blended — auto-reject** |
| B Work the Bed | crew craft throughout, but PAYOFF is *reverent status object*, not a task list | neither pole cleanly |
| C Home Water | PAYOFF reverent, correctly no jokes | on-pole, but sincere-corporate not savage |
| D Dry Lake Line | ENEMY texture with no monster and no threat answered | ambient, unresolved |
| E Never Seen It | ENEMY setup, then the bridge **cancels the pole** | **anti-pattern** |

E is the sharpest failure and it is mine. *"Nobody's going to scare you / The
lake is coming down, that's all"* — I wrote that to defuse the fear-selling
risk. Against this doctrine it is a piece apologising for its own pole. The
right fix for fear-selling is meanness aimed at hydrilla and neglect, never at
the customer's anxiety — not disarming the piece.

## Line-level: where the voice actually dies

| Line | Class |
|---|---|
| "You take care of it because it's yours" | flatters the reader; no noun, no receipt |
| "Home water, home water / We don't work anywhere else" | flatters us, agency voice |
| "Same water, same limestone / Same mud beneath it all" | vibes, not receipts |
| "Lake Austin is home" | slogan with nothing under it |
| "It's your bulkhead down there leaning" | closest to savage in the whole set — concrete noun, true, unflattering |

Suno's `D` is **better on craft than mine** and it is worth saying why: *"fence
wire, bottle glass, and a rusted pan"* is receipts energy. Specific objects, no
adjectives. That is the thing my lyrics do not do once.

## Savage rewrite — ENEMY pole, declared

**Pole:** ENEMY · **Avatar:** waterfront owner who has not looked · **Keyword:**
`DOCK` (L5 reuses DOCK — see CTA conflict below) · **Angle:** Hydrilla Horror

```
[Verse 1]
Forty feet of salad
Growing off your bulkhead
Ten years down there in the dark
And you paid the mortgage on it

[Chorus]
Water's coming down
Salad's coming out
Scrape it, haul it, cover it
That's the whole mechanism

[Verse 2]
Your lift has been eating hydrilla
Since the last time that it ran
There's a cable down there fraying
And a slip you can't get into

[Chorus]
Water's coming down
Salad's coming out
Scrape it, haul it, cover it
That's the whole mechanism

[Bridge]
Ten years of high water
Was an expensive lid

[Verse 3]
It fills back up in spring
And whatever's still down there
Stays down there
Nobody is coming back for it

[Chorus]
Water's coming down
Salad's coming out
Scrape it, haul it, cover it
That's the whole mechanism
```

⚠️ *"Forty feet of salad"* is lifted almost verbatim from the skill's own
worked-example table (*"Your shoreline is 40 feet of salad"*). It is the
canonical savage line for this exact subject, not something I invented — flagging
it so nobody mistakes it for original work or ships it thinking it is fresh.

Dropped "very" from the bridge after the scanner flagged it as a weak qualifier.
It was right: deadpan does not take intensifiers, and *"an expensive lid"* is the
harder read.

Deadpan test: read flat, no emphasis. *"Was an expensive lid"* and *"you
paid the mortgage on it"* still land. No exclamation point anywhere, no wink.
Meanness points at hydrilla, the lid, and the delay — never at a person.

⚠️ No CTA line in the lyric. See the conflict below; the keyword cannot be sung
until routing passes, and the bare number is the safe form.

## Four conflicts that need a Nate ruling — I am not resolving these

1. **Depth.** `LYRICS-v2.md` sings *"Ten to twelve, and they're calling it
   projected."* `atx-savage-voice` says **about 10 feet, explicitly not
   "10–12"** — and then flags its own numbers **UNRATIFIED** against
   `brain/decisions/0002-drawdown-copy-sot-final.md`. Two sources of truth
   disagree and the newer one says do not trust it yet. **Nothing sings a depth
   until this is ruled.**

2. **Which brief governs a song.** `atx-savage-voice`'s "When to use" lists
   captions, straps, hooks, 10s hero copy. **Songs are not on that list.** If
   songs are savage-governed, the whole set gets rewritten. If they are scored
   beds carrying the reel's tone, `PROMPTS.md` was the right brief and only the
   craft was weak. Your call — it changes everything downstream.

3. **CTA keyword.** `PROMPTS.md` says CTA = **TRUXOR**. The skill rules L5
   Drawdown reuses **DOCK**, and `DRAWDOWN` was explicitly ruled down to DOCK.
   Separately: **live routing status is FAIL** (ATX-1957 / ATX-1958 open), so
   nothing publishes on any keyword regardless. The songs currently sing a bare
   number and no keyword, which is the safe state.

4. **The $695 Assessment.** `LYRICS-v2.md` bans `$695`, `credited`,
   `assessment` per your 2026-09-01 ruling for the reels. The skill states the
   Assessment is the live offer and calls keyword-only CTA that ignores it an
   anti-pattern. Both cannot be right for the same piece.

## What I am not claiming

I still have not heard any of these songs. This pass is on the words on the
page against written doctrine. Whether the savage rewrite *sings* — whether
"an expensive lid" survives a melody — is a different question and needs an
ear, not another gate.
