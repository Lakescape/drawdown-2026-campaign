# Platform-native renders — research (2026-09-07)

**Linear:** Lake Austin Drawdown Campaign — media blitz + revenue capture (Oct 2026) · issues filed 2026-09-07 (see arch doc)
**Map:** `docs/maps/platform-native-renders.html` · **FigJam:** https://www.figma.com/board/kguEVAEMPpCFkfknnwkueB
**Arch doc:** `docs/architecture/platform-native-renders-2026-09-07.md`

## Why

Nate, 2026-09-07 22:59: the calendar ships **the same file** to IG Reels, TikTok, FB Reels and the
GBP listing. `build_scheduling_pack.py` copies one mp4 into four folders. That is the single biggest
reason the work reads "not enterprise grade": every platform paints its own UI over the frame, and
none of our straps, CTAs or hooks were placed with that UI in mind. A $50k agency edit is not
prettier footage — it is one pillar cut re-laid-out per feed, with a QC gate nothing skips.

## What we already own (do not rebuild)

| Asset | Where | State |
|---|---|---|
| Gated production pipeline (G0 → G3 → Routing Gate) | `~/ATX-Media-Mogul/pipeline/WORKFLOW-MAP.md`, `gates-sop.md` | Built, law |
| Visual identity constants (strap font, colors, −14 LUFS, hook timing) | `~/ATX-Media-Mogul/doctrine/visual-identity.md` | Built |
| Per-platform publish rules | `~/ATX-Media-Mogul/marketing/platform-routing.md` | **"Per-platform rules — TBD, Nate decision"** — the gap |
| Two-pass `loudnorm` to −14 LUFS | `06_Media_Build/build_leadin_vo.py:75-90` | Built, reuse |
| Pillar master builder (Pillow cards + ffmpeg) | `06_Media_Build/build_lake_coming_down.py` | Built |
| Scheduling pack + click calendar | `build_scheduling_pack.py`, `build_calendar_page.py` | Built 2026-09-07 |
| Drawdown media calendar (phased, ATX-1630) | `~/ATX-Media-Mogul/marketing/calendar/drawdown-2026/` | Built 2026-08-02 — **carries superseded `$695` / "credited" / "exploring" language**; do not lift copy from it |
| Poseidon LUTs | `~/Poseidon/luts/MANIFEST.yaml` | `present_luts: []` — none authored |
| Poseidon Resolve MCP studio | `~/poseidon-studio/POSEIDON_PRODUCTION_STUDIO_GUIDE.md` | Install guide only; not the path for this campaign |
| Rig skills | `embedded-captions`, `graphic-overlays`, `motion-graphics`, `general-video` (HyperFrames) | Installed; slice 2 candidates for captions + hook cards |

## Gary Vaynerchuk, *Day Trading Attention* (2024) — the framework, from the PDF on disk

Source: `My Drive/Ai PDFs/InsightEngine/Gary V marketing info.pdf` (text extracted to job tmp, 696 lines).
Three parts. Quoted where it matters.

**PAC — Platforms and Culture.** "Audit each platform at the time you're reading this and fill out
the following chart" of each platform's current features and creative units. Concretely: the chart
is a living per-platform spec, not a one-time read. Our version = `PLATFORMS` table in
`build_platform_renders.py` plus the safe-zone numbers below, re-audited before each campaign.

**SOC — Strategic Organic Content.** The variables, in the book's order:

1. **Hook** — "everything that appears in the first three seconds or so. That includes the title,
   the thumbnail, any captions you might use, the opening lines, the character or person in the
   video, and the overall design and format of the post."
2. **Copy optimized for the platform** — "people increasingly use platforms like TikTok and
   Instagram as search engines, the copy (the caption) on your post plays a huge role." One example
   ends the video with a CTA to "read the caption" where the long copy lives.
3. **Platform-native sound** — Chipotle "repurposed a TikTok to an Instagram Reel. It was the same
   video with the same copy, but the trending sound … was different on each platform."
4. **Cohort call-out** — the headline "directly calls out a cohort" (his example: people over
   thirty). Ours: Lake Austin waterfront owners; sub-cohorts = boat-lift owners, bulkhead owners,
   past clients.
5. **Profile hygiene** — when they click through "they know exactly who you are and what you do."
6. **UI-aware layout** — his own note on a Fox Financial Facebook Reel: "try some with the subtitles
   placed a little higher on the screen so that it's not hidden behind the Facebook Reels user
   interface." This is the safe-zone rule, in his words.
7. **Direct-response CTA on a brand video** — True Classic: comedy scenarios "with direct-response
   elements to grow sales." Ours is locked: TEXT TRUXOR to 254-780-6971.

**PCS — Post-Creative Strategy.** "Listening to actual consumers and gathering insights": read the
comments, audit "each platform's comments section capabilities," feed the next cut. Mogul already
has the sink for this — `marketing/performance-log.md`, texts-per-1k-views. The loop closes when the
SOC pass for cut N+1 reads the PCS notes from cut N.

**What the framework is NOT:** it is not a rule to make ten different videos. It is one pillar, cut
natively per feed, judged by the comments. That matches Nate's "one magnet" call exactly.

## Safe zones (1080×1920) — 2026 third-party guides, not platform-published

| Platform | Top | Bottom | Left | Right | Confidence |
|---|---|---|---|---|---|
| TikTok | 130–140 | 400–484 | 60 | 180 | Guides agree within ±80 px on the bottom |
| IG Reels | 108–130 | 320–400 | 60 | 120–140 | Guides agree |
| FB Reels | ≈ IG | ≈ IG | ≈ IG | ≈ IG | **Unverified** — "may differ slightly" |
| GBP listing video | — | — | — | — | **Unverified** — no UI overlay documented; thumbnails crop |

Sources: [Zeely TikTok safe zones](https://zeely.ai/blog/tiktok-safe-zones/) ·
[CreaMate TikTok safe zone](https://creamate.ai/en/blog/tiktok-safe-zone-guide) ·
[Kreatli TikTok safe zone](https://kreatli.com/guides/tiktok-safe-zone) ·
[Outfy Instagram safe zone](https://www.outfy.com/blog/instagram-safe-zone/) ·
[Zeely Instagram safe zones](https://zeely.ai/blog/master-instagram-safe-zones/) ·
[Verve IG Reels safe zones](https://vervecreative.studio/instagram-reels-safe-zones-and-tips/).

Rule adopted: use the **conservative** end of each range, and render a proof PNG per platform so
the numbers are checked on our own frames instead of trusted.

## MKT1 connector — verdict

Ran `mkt1_skills_list` and `mkt1_templates`. Nothing in MKT1 edits, grades, or lays out video —
it is B2B SaaS GTM strategy (positioning, ICP, channel, AEO, hiring). Two pieces earn a slot:

1. **`mkt1_gaccs`** — one GACCS brief (Goals, Audience, Creative, Channels, Stakeholders) for the
   Drawdown campaign. This is the creative brief a top agency writes before any cut; it becomes the
   input to every SOC pass. Run once, keep in `docs/research/`.
2. **`mkt1_channel_strategy`** — only if we want a second opinion on IG/TikTok/FB/GBP weighting.

Skip the rest for this work. Running `mkt1_positioning` or `mkt1_big_bets` here would produce
InsightEngine SaaS strategy, not better reels.

## Blocker found during recon — Routing Gate

Every post's CTA is TEXT TRUXOR to 254-780-6971. Per Mogul law nothing publishes until the keyword
test logs PASS. State on 2026-09-07:

- `pipeline/keyword-routing-test.md` gate status: **BLOCKED (2026-08-03)**; no dated PASS block.
- `published/publish-log.md`: empty.
- ATX-1748 (In Progress, Urgent): webhook registered 2026-08-13, secret set; last live test (`DOCK`,
  2026-08-13) **FAIL**; "One live `TRUXOR` from a non-business phone remains."
- Quo inbox scan (Aug 1 → Sep 7, 50 of 344 contacts): no inbound `TRUXOR` seen.

The Sep 14 hero points at an unproven keyword. The fix is one text from a phone not on the business
account, watch for the Slack lead card, log PASS. Two minutes of Nate's time; nothing in this
research unblocks it.

## Risks

- Safe-zone numbers drift; platforms move UI without notice. Mitigation: proof PNG per render, re-audit per campaign (PAC).
- Slice 1 renders do not re-position straps — a strap already in a dead zone stays there until slice 2. The QC sheet says so explicitly.
- Drawdown media-calendar in Mogul carries banned copy (`$695`, "credited", "exploring"). Any SOC pass that lifts from it fails `voice-qa`.
- Sound swap per platform (SOC #3) needs a licensed / in-app sound per platform; burned Suno bed is fine for GBP and FB, weaker on TikTok. Decision deferred to slice 3.
