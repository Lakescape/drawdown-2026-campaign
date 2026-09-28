# Drawdown extraction plan — 2026-09-28

The Lake Austin drawdown is cancelled (Nate, 2026-09-28). This plan moves the reusable, campaign-neutral pieces out of `~/drawdown-2026-campaign` and `~/drawdown-sprint`, and leaves the dated campaign content behind as an archive.

Source: read-only inventory run 2026-09-28 across Mogul, DockBotclaw, Hermes and both drawdown trees. Nothing below has moved yet. Nate approves before any wave starts.

## Canonical targets (use these, not the look-alikes)

| Repo | Canonical path | Notes |
|---|---|---|
| ATX-Media-Mogul | `~/ATX-Media-Mogul` | `~/InsightEngineMacOSPRO/ATX-Media-Mogul` is a second clone. Do not edit there. Checked-out branch is stale, so branch from `origin/main` in a fresh worktree. |
| DockBotclaw | `~/DockBotclaw` | Checked out on a cursor branch. Branch from `origin/main`. |
| DockbotHermes | `~/DockbotHermes` | `~/DockBotHermes`, `~/DockBothermes`, `~/dockbothermes` are the same directory. Local `main` is behind `origin/main`. `~/DockbotHermes-main` is a stale clone. `~/dockbothermes-wt` is not Hermes. |

## Already done — do not redo

- Mogul PR #113 (`feat/craft-rebuild-loop-extract`, open): rebuild-loop playbook, two Workflow scripts, `platform_renders.py`, `platform-routing.md` repoint. Scripts still carry LCD-specific lines on purpose.

## Wave 0 — decisions (Nate)

1. Merge Mogul PR #113 first. Wave 1 edits sit next to it and `platform-routing.md` would conflict otherwise.
2. Close drawdown-campaign PRs #14 (C1/C2 hedge) and #6 (permit retraction) as stale.
3. Branch `worktree-docs-media-build-claude-md` (06_Media_Build/CLAUDE.md + this plan): its rules move to Mogul in Wave 1; keep the branch only as the record of this plan, no PR.
4. Mogul's own drawdown folders (`projects/DRAWDOWN-2026`, `docs/campaigns/drawdown-2026`, `marketing/calendar/drawdown-2026`, `scripts/visual-first/drawdown_runtime.py`, `visual-library/campaign-handoff.py`): archive in place or move under `archive/`.
5. Hermes `drawdown_pipeline_mirror`: retire, or generalize into a campaign-neutral mirror.

## Wave 1 — ATX-Media-Mogul (one PR, after #113 merges)

| From (drawdown-2026-campaign) | To (Mogul) | Work |
|---|---|---|
| `06_Media_Build/CLAUDE.md` | `pipeline/playbooks/ffmpeg-still-build-rules.md` + pointer in `pipeline/CLAUDE.md` | Copy. Rules are already campaign-neutral. |
| `06_Media_Build/compose.py` | `pipeline/scripts/compose_stills.py` | Parameterize paths; keep bleed vs fit. |
| `06_Media_Build/build_timeline_cut.py`, `build_real_motion.py`, `build.filter` | `pipeline/scripts/` | Generalize; drop campaign strings. |
| `06_Media_Build/build_leadin_registry.py` (`assert_c7`) | `scripts/visual-library/registry.py` | Port the count-claim guard only. |
| `06_Media_Build/library_sheet.py` | — | Compare with `visual-library/build-sheet.py`; likely drop. |
| `06_Media_Build/build_vo_mikerow.py`, `build_leadin_vo.py` | `pipeline/scripts/vo_elevenlabs.py` | Strip voice IDs and campaign names; IDs from env. |
| `06_Media_Build/audio/suno/README.md`, `PROMPTS.md`, `LYRIC-HARD-PASS` | `pipeline/playbooks/suno-lyrics.md` | Method only, no drawdown lyrics. |
| `MEDIA_ClaimLedger_Drawdown_v1.md`, `MEDIA_ShotList_QC_Drawdown_v1.md` | `pipeline/templates/_TEMPLATE-claim-ledger.md`, `_TEMPLATE-shotlist-qc.md` | Keep structure, blank the rows. |
| `MEDIA_Production_Process_v1_2026-08-03.md` | craft-rebuild-loop playbook | Keep only the four defect post-mortems. |
| `REVIEW/SKILL_Platform_Attention_Economics_v1.md` | `doctrine/platform-attention-economics.md` | PR #113 references PAC/SOC; this is the source. |
| `06_Media_Build/weeks/README.md` (BOARD / CURRENT) | `pipeline/weekly-writers-room.md` | Diff and merge; do not duplicate. |
| `06_Media_Build/build_scheduling_pack.py`, `build_calendar_page.py`, `SCHEDULING_PACK/README.md` | `pipeline/scripts/` next to `publish-scheduler.py` | Nothing self-posts; keep that rule. |
| `docs/architecture/platform-native-renders-2026-09-07.md`, `docs/research/…` | `docs/architecture/`, `docs/research/` | Arch doc behind PR #113's renderer. |

Size: >3 files, one lane. Dispatch to one worktree session (Claude or Cursor) with this table as the contract.

## Wave 2 — DockBotclaw

| From | To | Work |
|---|---|---|
| `02_Operating_System/SLACK_SALES_BOARD_SETUP.md` | `docs/playbooks/` | Diff against the asana sales-pipeline rules doc first. |
| `02_Operating_System/AGENTS.md` | — | Read for any rule not already in DockBotclaw; port lines, not the file. |
| `~/drawdown-sprint/dcc-close-book/docs/decisions/` (6 ADRs) | `docs/decisions/` as one pattern note | Keep the principles (honesty pass, deposit cash is not project value, no priced proposal until confirmed). The app stays behind. |

## Wave 3 — DockbotHermes

| From | To | Work |
|---|---|---|
| `06_Media_Build/weeks/2026-08-31/HERMES_QC_STUDIO.md` | Hermes QC job spec | Genericize as a media-QC job. |
| `drawdown_pipeline_mirror` | — | Per Wave 0 decision 5. |
| `03_Sync_Engine/asana_sync.py` | — | Skip. Overlaps the Hermes Asana stage-gate work. |

## Wave 4 — archive

- Add a README banner in `~/drawdown-2026-campaign`: "Cancelled 2026-09-28. Reusable parts moved per docs/closeouts/2026-09-28-drawdown-extraction-plan.md."
- Tag `archive/2026-09-28`. Archiving the GitHub repo is Nate's call.

## Stay behind (stale, do not migrate)

`01_FINAL_Deliverables`, `04_Source_Package_v2`, `06_Command_Center`, `06_Media_Build/SCHEDULING_PACK/<dated slots>`, `cards`, `resolve/*`, `weeks/2026-08-31`, `archive`, `05_Lake_Austin_ShotPack_and_Ops/{ops,shot-pack,tools}`, `DATA_2017_*`, `MEDIA_Script_Drawdown_v1_LOCKED.md`, `CLOSEOUT-*`, `REVIEW/GROK_*`, `skills/atx-viral-video-producer` (duplicated by Mogul skills), `drawdown-sprint/drawdown-2026-site`, the old `drawdown-command-center` copy, the `dcc-close-book` app.

## Least confident decisions

1. Whether `build_lcd_v2.py` (1,616 lines) holds a generic assembler worth extracting. Plan says mine it during Wave 1, not migrate it whole.
2. Whether the scheduling-pack generator is still wanted now that posting runs elsewhere.
3. Whether Mogul's own drawdown folders should move to `archive/` or stay in place with a banner.
