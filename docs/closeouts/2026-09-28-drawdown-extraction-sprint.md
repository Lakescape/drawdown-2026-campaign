## Sprint Plan: Drawdown Extraction (mini-sprint)
**Dates:** 2026-09-28 — 2026-09-28 (one session) | **Team:** 1 supervisor + 3 worker agents
**Sprint Goal:** Every reusable drawdown asset sits in a draft PR in its right repo, and the drawdown repo is marked cancelled.

Plan of record: `docs/closeouts/2026-09-28-drawdown-extraction-plan.md`.

### Wave 0 decisions (defaults taken on Nate's "get it done", 2026-09-28)
| # | Decision | Taken |
|---|---|---|
| 1 | Mogul PR #113 | Left for Nate. It is BLOCKED on a required review; agents do not bypass branch protection. Wave 1 adds new files only and avoids #113's files, so it does not wait on the merge. |
| 2 | Drawdown PRs #14, #6 | Close as stale, with a comment pointing here. |
| 3 | Mogul drawdown folders | Banner in place. No move, no delete. |
| 4 | Hermes `drawdown_pipeline_mirror` | Retire in a draft PR. No deploy, no runtime change until Nate merges. |
| 5 | Scheduling-pack generator | Cut. Posting runs elsewhere. |

### Capacity
| Lane | Repo | Allocation | Notes |
|---|---|---|---|
| Supervisor | drawdown-2026-campaign | Wave 0 + Wave 4 | Closes PRs, banner, tag, verifies worker diffs |
| Worker A (sonnet) | ATX-Media-Mogul | Wave 1 | Fresh worktree off `origin/main` in `~/ATX-Media-Mogul` |
| Worker B (sonnet) | DockBotclaw | Wave 2 | Fresh worktree off `origin/main` |
| Worker C (sonnet) | DockbotHermes | Wave 3 | Fresh worktree off `origin/main` (local main is behind) |

### Sprint Backlog
| Priority | Item | Owner | Dependencies |
|---|---|---|---|
| P0 | Mogul: `pipeline/playbooks/ffmpeg-still-build-rules.md` + CLAUDE.md pointer | A | None |
| P0 | Mogul: claim-ledger and shot-list QC templates | A | None |
| P0 | Mogul: `pipeline/scripts/compose_stills.py` (parameterized) | A | None |
| P0 | Mogul: port `assert_c7` count-claim guard into `scripts/visual-library/registry.py` | A | None |
| P0 | Mogul: CANCELLED banner on its drawdown folders | A | None |
| P0 | Close drawdown PRs #14, #6; README banner; tag `archive/2026-09-28` | Supervisor | None |
| P0 | Hermes: retire `drawdown_pipeline_mirror` (draft PR) | C | None |
| P1 | Mogul: Suno lyrics playbook, ElevenLabs VO helper, defect post-mortems doc, platform-attention doctrine, platform-native-renders arch doc | A | None |
| P1 | DockBotclaw: Slack sales-board setup playbook (diffed), dcc-close-book decision patterns note, AGENTS.md rule port | B | None |
| P1 | Hermes: media-QC job spec from HERMES_QC_STUDIO | C | None |
| P2 | Mogul: `build_timeline_cut.py` / `build_real_motion.py` genericized; weeks BOARD workflow merged into `weekly-writers-room.md` | A | Stretch |
| Cut | Scheduling-pack generator, `asana_sync.py`, ShotPack tools, `build_lcd_v2.py` whole-file port | — | Decision 5 / plan |

### Risks
| Risk | Impact | Mitigation |
|---|---|---|
| Wave 1 collides with PR #113 | Merge conflict | Wave 1 never touches #113's files or `marketing/platform-routing.md` |
| Wrong clone edited | Lost or duplicated work | Only `~/ATX-Media-Mogul`, `~/DockBotclaw`, `~/DockbotHermes`, each in a new worktree |
| Campaign strings leak into shared code | Stale claims in future cuts | Grep gate: no `drawdown`, `Oct 12`, `Truxor CTA`, phone numbers or voice IDs in migrated files outside banners |
| Hermes runtime change goes live | Unreviewed prod change | Draft PR only; nothing deployed |
| Linear MCP disconnected | Tracking rule unmet | Record as pending; file the Linear project when the connector is back |

### Definition of Done
- [ ] One draft PR per target repo, never merged by an agent
- [ ] Python files pass `python3 -m py_compile`
- [ ] Grep gate clean on migrated files
- [ ] Supervisor has read each diff, not just each agent's report
- [ ] Drawdown repo carries the banner and the `archive/2026-09-28` tag

### Key Dates
| Date | Event |
|---|---|
| 2026-09-28 | Sprint start, workers dispatched |
| 2026-09-28 | Diff review and closeout |
| Next session | Nate reviews and merges the draft PRs (and #113) |
