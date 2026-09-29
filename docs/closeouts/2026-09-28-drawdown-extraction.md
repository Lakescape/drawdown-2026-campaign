# Closeout — drawdown extraction (2026-09-28)

**State:** IN-FLIGHT. All work is in draft PRs. Nothing is merged.

**Landed (merged):** none.

**Open draft PRs:**
- ATX-Media-Mogul #114 `feat/drawdown-extract-wave1`: ffmpeg/QC rules, claim-ledger and shot-list templates, `compose_stills.py`, `assert_count_claim`, VO helper, Suno method, post-mortems, attention doctrine, render arch doc, banners on Mogul's drawdown folders.
- DockBotclaw #260 `feat/drawdown-extract-wave2`: Slack sales-board playbook, close-book decision patterns, 5 operating-manual rules.
- DockbotHermes #52 `feat/drawdown-extract-wave3`: retires `drawdown_pipeline_mirror`, media-QC job spec, drops the dead drawdown media root from `daily-ops-extract.py` (79fb72b).
- drawdown-2026-campaign #15 `worktree-docs-media-build-claude-md`: cancelled banner, extraction plan, sprint plan, this file.

**Other actions:** closed drawdown PRs #14 and #6 as stale. Tagged `archive/2026-09-28` at `aecc9d4`.

**Uncommitted:** none in the four worktrees used.

**Blocked on:** Nate, for reviews and merges. Mogul #113 is BLOCKED on a required review, and #114 follows it.

**Next action:** Review and merge Mogul #113, then #114, #260, #52 and #15, then run `hermes cron remove drawdown-pipeline-mirror` and delete `~/.hermes/scripts/drawdown-pipeline-mirror.sh*`.

**Do NOT repeat:**
- Check whether the project is still alive (the memory index) before writing rules into its repo.
- In a worktree-isolated session, run git in another repo as `cd /absolute/path && git ...`. `git -C`, `~` paths and loops get refused by the guard.
- Hermes `hermes-common.test.sh` already fails on `origin/main` (missing `morning-briefing` in `config/cron-jobs.reference.json`). It is not caused by #52.
- Seven drawdown Linear projects (P-ATX-261, 267, 300, 316, 321, 329, 331) still show Backlog, Planned or In Progress. P-ATX-331 (water-up execution) is live work. The rest need a cancel-or-keep call from Nate.
