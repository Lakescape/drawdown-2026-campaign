# Drawdown Command Center (live app)

The **campaign OS SPA** lives in a dedicated repo:

**→ https://github.com/Lakescape/drawdown-command-center**

## Why separate?

- `drawdown-2026-campaign` = FINAL copy, funnel maps, zone scorecards, media handoffs, ops docs  
- `drawdown-command-center` = runnable sales pipeline + zone intelligence + marketing goals UI  

## Ownership (quick)

| Surface | Owns |
|---|---|
| Command Center | Inbound, stages, zones, deposit cash, media, capacity model |
| Jobber | Crew schedule after deposit |
| Asana | Final company record book |
| Slack | Alerts only (`#drawdown-inbound`) |
| Netlify | Public Assessment form → webhook |

## Handoff

See in app repo:

- `docs/HANDOFF_PACKAGE.md`
- `docs/SOP_DAILY.md`
- `HANDOFF_DRAWDOWN_COMMAND_CENTER.md` (devil's advocate)

Zone data in the app was sourced from:

`05_Lake_Austin_ShotPack_and_Ops/ops/zone_scorecard.csv`

Pushed 2026-07-31 by Grok Build.

## Go live

Full checklist: in app repo → `docs/GO_LIVE.md`

1. Import `drawdown-command-center` on Vercel  
2. Set `SLACK_INBOUND_WEBHOOK_URL`  
3. Password-protect production  
4. Point Netlify form → `https://<prod>/api/inbound`  
5. Pin URL in `#drawdown-war-room`
