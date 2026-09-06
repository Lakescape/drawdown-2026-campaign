# audio/suno — generated tracks

Generated 2026-09-04 via Suno MCP (AceData), model `chirp-v5-5`, custom mode.
Prompts are verbatim from `PROMPTS.md` in this folder — nothing was rewritten.

Two variants per prompt (Suno returns a pair). Pick one per slot, delete the other,
or keep both as alternates. **Nobody has listened to these yet — see Open below.**

| File | Track | Dur | Mean dB | Peak dB | Vocal | Suno task |
|---|---|---:|---:|---:|---|---|
| `01_MudWindow_v1.mp3` | Mud Window | 19.72 s | −17.1 | −1.8 | instrumental | `c402d707-eefc-42bf-a6b8-e67122f75ff4` |
| `01_MudWindow_v2.mp3` | Mud Window | 17.16 s | −16.5 | −2.3 | instrumental | same task |
| `02_LakeComingDown_v1.mp3` | Lake Coming Down | 36.96 s | −15.1 | −1.2 | instrumental | `f6ff2335-0816-461b-8e81-718b830d6f3a` |
| `02_LakeComingDown_v2.mp3` | Lake Coming Down | 39.00 s | −15.6 | −1.5 | instrumental | same task |
| `03_WorkTheBed_v1.mp3` | Work the Bed | 25.76 s | −16.9 | −2.2 | male vocal | `f2d6718d-8f3b-435b-98b9-7c610b8e8594` |
| `03_WorkTheBed_v2.mp3` | Work the Bed | 27.80 s | −16.0 | −0.8 | male vocal | same task |

Durations are Suno's own reported values; `ffprobe` agrees to the truncated second.
Levels measured with `ffmpeg -af volumedetect`. No clipping on any track.
Cost 0.56 credit per task, **1.68 total**. Generation took 62-97 s per task.

## What was sent to Suno

Style strings, lyric blocks and exclusions are exactly the three prompts in
`PROMPTS.md`. Parameters added on top of them:

| Prompt | model | instrumental | duration req | vocal_gender | negative_tags |
|---|---|---|---:|---|---|
| 1 Mud Window | chirp-v5-5 | true | 20 | — | pop vocal, EDM, meme bass, whistle, stock epic trailer choir |
| 2 Lake Coming Down | chirp-v5-5 | true | 40 | — | same |
| 3 Work the Bed | chirp-v5-5 | false | 30 | m | same + autotune, jingle, carnival barker |

`duration` is a target, not a guarantee — Suno's own docs say the track "lands near
this value but is not guaranteed to match it exactly." Actuals above are 2–5 s under
each request, which is inside the intended range for all three slots.

Track 3's lyric is the locked chorus + tag from `PROMPTS.md`, unmodified. It contains
none of the banned terms (exploring, unofficial, nothing is official yet, six ninety
five, extinct, $695). "Cover it" matches the corrected COVER beat — the third beat of
the Scrape/Haul cut is a matting picture, not a stapled tarp.

## Open — needs a human ear before any of this ships

1. **Nobody has listened.** Duration and level are measured; *musical* fit is not.
   Whether a track passes the BBQ test cannot be read off a waveform.
   On the vocal-free question there is now one piece of real evidence: polling the
   two instrumental tasks returns `lyric: ""` - Suno generated no lyric at all for
   them, so the `instrumental: true` flag took. That rules out sung words. It does
   not rule out wordless vocal pads, which still needs an ear.
   Track 3's lyric echoes back byte-identical to what was sent, so Suno rewrote
   nothing and no banned term entered through the model.
2. **Pick one variant per slot.** Six files, three slots.
3. **Trim in Resolve.** Slot 1 is specified as a 15 s reel bed; the takes are 17–19 s.

## Cover art - pulled, and mostly not usable

Six covers downloaded from `cdn2.suno.ai/image_<audio_id>.jpeg`, one per take, named
`<slot>_<Title>_v<n>_cover.jpeg`. All verified `image/jpeg`.

**Every one is 360x360.** That is Suno's thumbnail, not a marketing asset. It is under
Instagram square (1080), well under podcast art (3000), and will look soft anywhere it
is not a tiny inline thumb. Do not upscale a 360px model output and call it artwork.

What they actually depict, having looked at them:

| Cover | Reads as | Verdict |
|---|---|---|
| 01 Mud Window | cracked glass pane half-sunk in black muck, water lily, rain | on-theme, abstract, the strongest of the six |
| 02 Lake Coming Down | cracked dry lakebed, rusted iron fence, faux-Polaroid border | thematically close to a drawdown; the fake film frame is a style choice, not ours |
| 03 Work the Bed | crayon sketch, a hand planting in a raised **garden bed** | semantic miss - the model read "bed" as gardening. Unusable. |

**The Rule 11 risk did not materialise, and that is worth stating.** None of the six
depicts a machine, a crew, or an identifiable shoreline. They are abstract or
illustrative, so none of them can be mistaken for a real plate of our iron or our
water. If a future cover ever does show equipment, it does not ship - same rule that
keeps generated machines out of the reels.

Treat these as scratch. Real cover art, if any slot needs it, comes from the Poseidon
library like every other picture on this campaign.

## Track 3 cover, regenerated - `cover-v2/`

Suno has no cover-only regenerate; its art is bundled with a generation, and
`suno_upload_cover` is cover *songs*, not images. So slot 3's garden-bed miss was
redone on a real image model instead, which also clears the 360px ceiling.

Artlist MCP, model **Nano Banana 2** (`modelId` 2251), 2k, `num_images: 4`, two calls:

| Files | Aspect | Size | Generation |
|---|---|---|---|
| `03_WorkTheBed_cover_sq1-4.png` | 1:1 | 2048x2048 | `01a06ef0-ae91-757d-85de-475a5ed249e9` |
| `03_WorkTheBed_banner_wide1-4.png` | 16:9 | 2752x1536 | `01a06ef0-8139-7659-a757-8b10d9e52770` |

520 price units per call, 1040 total. `contact_sheet.jpg` is a 2x2 of the four
squares (1 top-left, 2 top-right, 3 bottom-left, 4 bottom-right) for quick compare.

⚠️ **The 16:9 set was an accident worth knowing about.** Asking for "square 1:1" in
the prompt text does nothing - the model default won and `resolvedSettings` came back
`16:9`. Aspect ratio has to go in `settings`, not the prompt. The wide set is kept
because it was already paid for and works as header/YouTube art, not because it was
asked for.

**All four squares read as an exposed lakebed** - cracked mud flats, a pale waterline
band on limestone, cedar, a remaining channel of water. Pick by treatment: 1 is the
boldest and flattest, which is what survives being shown at thumbnail size; 4 is the
softest and most naturalistic; 2 carries a white paper border; 3 is the busiest.

**sq1 is now embedded on both track 3 takes.** `03_WorkTheBed_v1.mp3` and `_v2.mp3`
carry it as ID3v2.3 attached art, resized to 1000x1000 JPEG (174 KB). Full-size
2048x2048 stays in `cover-v2/` as the master; `03_WorkTheBed_cover_EMBED.jpg` is the
derivative that went into the tags.

1500x1500 was tried first and rejected - at 609 KB the art was larger than the audio
it was riding on. 1000x1000 at q6 is the trade that keeps the file sane.

Audio was stream-copied, not re-encoded: durations are byte-identical at 25.7735 s and
27.8135 s, and mean volume reads -16.9 / -16.0 dB before and after. Tags set: title
"Work the Bed", artist "ATX LakeScapes", album "Drawdown 2026", date 2026. Tracks 1
and 2 were not touched and remain single-stream audio.

Rule 11 holds on all eight: no machine, no crew, no identifiable shoreline, no text.
They are plainly illustration and cannot be read as a plate of our iron or our water.
That is the *only* reason generated art is acceptable in this slot at all - it is a
mood cover, never evidence.

## Full-length songs — `songs/`

The three prompts in `PROMPTS.md` produced 17-39 s beds. These are actual songs,
~3 minutes, written against the lyric rules in `LYRICS-v2.md`. Same model, same
banned-term discipline, male vocal, no autotune.

| File | Song | Dur | Mean dB | Peak dB | Suno task |
|---|---|---:|---:|---:|---|
| `A_TheWindow_v1.mp3` | The Window | 189.7 s | −14.7 | −0.7 | `2cf30972-06e6-4fc7-a64c-c42f46e9ecd4` |
| `A_TheWindow_v2.mp3` | The Window | 191.5 s | −14.9 | −1.7 | same |
| `B_WorkTheBed_v1.mp3` | Work the Bed | 179.3 s | −16.0 | −1.9 | `1cf87001-7b1a-428a-8aad-7cea5f48f884` |
| `B_WorkTheBed_v2.mp3` | Work the Bed | 178.6 s | −14.9 | −1.2 | same |
| `C_HomeWater_v1.mp3` | Home Water | 185.2 s | −15.3 | **−0.1** | `411ecdea-3b99-4e4d-84ba-3fcae57a5f8f` |
| `C_HomeWater_v2.mp3` | Home Water | 184.5 s | −15.8 | −0.6 | same |

Requested 190 / 180 / 185 s and got 189.7 / 179.3 / 185.2. The short beds all landed
2-5 s under target; at full length the model hits the mark. Duration is more reliable
the more room it has.

⚠️ **`C_HomeWater_v1` peaks at −0.1 dB.** Not clipped, but there is effectively no
headroom — it will clip on any re-encode or loudness-normalised platform. Prefer v2
(−0.6 dB) or pull v1 down ~1 dB before use.

## Work the Bed, re-cut with the phone number — `songs/B_WorkTheBed_tel_*.mp3`

Nate's call 2026-09-04: put the number in the tag. Task
`da50df8e-2aee-4c2f-bc87-54a03b79ad9f`, everything else identical to the B takes above.

| File | Dur | Mean dB | Peak dB |
|---|---:|---:|---:|
| `B_WorkTheBed_tel_v1.mp3` | 185.05 s | −14.7 | −1.3 |
| `B_WorkTheBed_tel_v2.mp3` | **122.17 s** | −15.4 | −1.2 |

⚠️ **v2 came back 63 s short of the 185 s request** — a different arrangement, not a
truncated file (it is a complete render, just briefer). Every other generation this
session landed within 5 s of target. Check where it ends before using it; v1 is the
one that matches the brief.

Sung as `Two five four. Seven eight oh. Six nine seven one.` — digits spelled for the
same reason `CAPTIONS_2026-08-30` spells "six ninety-five": models read raw digit
strings inconsistently. The style string directs the tag as spoken-sung and flat, and
`chanted numbers` plus `advertisement` were added to the negative tags, because a sung
phone number is the jingle failure the brief bans. **Whether it actually avoids that
is an ear question, not a measurable one.** If it reads as an ad, the fix is a spoken
end-card over the instrumental rather than a sung tag.

The earlier `B_WorkTheBed_v1/v2.mp3` are kept — same song without the number.

## Suno-written and second-person cuts

| File | Song | Dur | True peak | Origin |
|---|---|---:|---:|---|
| `D_DryLakeLine_v1.mp3` | Dry Lake Line | 184.4 s | −0.8 dB | **Suno wrote the lyrics**, `79008dc4` |
| `D_DryLakeLine_v2.mp3` | Dry Lake Line | 185.3 s | −1.0 dB | same |
| `E_NeverSeenIt_v1.mp3` | Never Seen It | 185.0 s | −1.8 dB | second-person rewrite, `c236a4be` |
| `E_NeverSeenIt_v2.mp3` | Never Seen It | 147.5 s | −1.8 dB | same |
| `B_WorkTheBed_endcard.mp3` | Work the Bed | 188.6 s | −0.7 dB | spoken end card over `B_v1` |
| `B_WorkTheBed_cover_v1_norm.mp3` | Bare Wire Take | 120.5 s | −0.78 dB | acoustic cover of `tel_v1`, `bfcb30a8` |
| `B_WorkTheBed_cover_v2_norm.mp3` | Bare Wire Take | 123.0 s | −0.52 dB | same |

**Dry Lake Line is Suno's own lyric**, generated from a brief rather than written
here, then run through the campaign gate. One change was required: it sang
*"the dozer gone quiet"* and we do not run dozers on the bed — that is the
`@two_machines` class of equipment claim. Changed to *"the diesel gone quiet"*,
same meter. Its suggested style also called for gang oohs and handclaps, which the
brief bans; those went into negative tags instead. Everything else passed clean.

**Never Seen It is the rehearsal experiment** from
`LYRIC-EXCAVATION-2026-09-04.md` — B's arrangement and style string byte for byte,
with point of view as the only variable. 14 second-person tokens against 2
first-person. Its bridge names the risk out loud (*"Nobody's going to scare you /
The lake is coming down, that's all"*) because fear-framing is the failure mode of
the disclosure angle.

⚠️ **The raw cover takes clipped.** `bfcb30a8` returned audio peaking at **+0.04 dB
and +0.21 dB** on the right channel — above full scale. Flat factor 0.000, so not
hard-clipped into square waves, but it would clip on any decode or re-encode. The
`_norm` copies are limited to −1 dBTP; the raw `B_WorkTheBed_cover_v1/v2.mp3` are
kept unmodified beside them. Nothing else generated this session went over.

⚠️ **Cover does not preserve length.** 185 s in, 120 s and 123 s out — Suno's cover
re-arranges rather than re-voices. Treat it as a shorter sparser reading, not a
like-for-like alternate.

Second takes of A, B, C and tel now live in `songs/alternates/`.

## Cover art, tracks 1 and 2

Same treatment as track 3: 2048x2048 squares from Artlist / Nano Banana 2, four each,
1:1 set in `settings` this time.

| Track | Generation | Reads as |
|---|---|---|
| 01 Mud Window | `01a06f11-3fb4-7cb3-a529-a64dc2542287` | night rain on black lake muck, thin gold band on the horizon |
| 02 Lake Coming Down | `01a06f11-4bde-7e40-affa-f027d0beb3b1` | golden-hour drawdown, concentric waterline rings on limestone, water pulled back to a channel |

`sq1` from each is embedded. Contact sheets: `01_MudWindow_sheet.jpg`,
`02_LakeComingDown_sheet.jpg` (1 top-left, 2 top-right, 3 bottom-left, 4 bottom-right).

Rule 11 holds across all sixteen images now: no machine, no crew, no identifiable
shoreline, no text anywhere.

## Every file now carries embedded art

All six beds and all six song takes have ID3v2.3 attached art at 1000x1000, and tags
(title / artist ATX LakeScapes / album Drawdown 2026 / 2026). Song art mapping:

- The Window → the golden drawdown cover
- Work the Bed → the cracked lakebed cover
- Home Water → the dark water cover

Every embed was verified before the original was replaced: duration byte-identical and
mean volume unchanged, because audio is stream-copied and never re-encoded.

## Still needs a human ear

Twelve files, six slots. Nothing here has been listened to. Levels, durations, art and
banned terms are all machine-verified; whether any of it is *good* is not.

## Files are gitignored on purpose

`.gitignore` excludes `06_Media_Build/audio/**/*.mp3|wav|m4a|flac`. The prompts and
this README are the tracked source; the audio is regenerable output, same rule as
every render and scratch frame in `06_Media_Build`.
