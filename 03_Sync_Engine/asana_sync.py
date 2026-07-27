#!/usr/bin/env python3
"""
DRAWDOWN 2026 — Asana System-of-Record Sync Engine
ATX Lakescapes / NateDOG Holdings

Pipeline:  Linear (working tracker) + Slack (ambient intel) -> Asana (final source of truth)
Design rules:
  - OWNED SOLO: runs locally (Kimi cron) or under Inngest/Railway unchanged. No third-party agent.
  - CONSERVATIVE: never deletes in Asana. Completes only. Conflicts are logged, not guessed.
  - IDEMPOTENT: sync_map.json maps Linear issue IDs -> Asana task GIDs. Safe to re-run.
  - GRACEFUL: every connector self-skips when its token/config is missing. --dry-run prints plan.

Config files (plain text, one value per file) in ~/.config/drawdown2026/:
  linear_api_key        Linear personal API key (required for Linear source)
  linear_team_key       Linear team key or name fragment (optional, narrows query)
  asana_pat             Asana Personal Access Token (required for writes)
  asana_project_gid     Asana project GID to sync into (required for writes)
  slack_bot_token       Slack bot token xoxb-... (optional)
  slack_channel_ids     Comma-separated channel IDs to harvest (optional)

State: ./state/sync_map.json, ./state/last_run.txt
Logs:  JSONL appended to Drive 09_Sync_Logs/ (falls back to ./logs/ if Drive unavailable)
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

CONFIG_DIR = Path.home() / ".config" / "drawdown2026"
HERE = Path(__file__).resolve().parent
STATE_DIR = HERE / "state"
DRIVE_LOG_DIR = Path(
    "/Users/austinlakescapes/Library/CloudStorage/"
    "GoogleDrive-nate@atxlakescapes.com/My Drive/"
    "DRAWDOWN 2026 - Full Campaign System/09_Sync_Logs"
)
LOCAL_LOG_DIR = HERE / "logs"

LINEAR_GQL = "https://api.linear.app/graphql"
ASANA_API = "https://app.asana.com/api/1.0"


# ---------------------------------------------------------------- utilities

def read_config(name):
    p = CONFIG_DIR / name
    if p.is_file():
        v = p.read_text(encoding="utf-8").strip()
        return v or None
    return None


def http_json(url, payload=None, headers=None, method=None, timeout=30):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method or ("POST" if data else "GET"))
    req.add_header("Content-Type", "application/json")
    for k, v in (headers or {}).items():
        req.add_header(k, v)
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return json.loads(resp.read().decode())


def load_json(path, default):
    if path.is_file():
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            return default
    return default


def log_line(log_path, record):
    record = dict(record)
    record["ts"] = datetime.now(timezone.utc).isoformat()
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")


# ---------------------------------------------------------------- linear

def fetch_linear_updates(api_key, team_hint, since_iso):
    """Fetch Linear issues updated since `since_iso`. Returns list of dicts."""
    headers = {"Authorization": api_key}  # Linear PAT: raw key, no Bearer
    team_filter = ""
    if team_hint:
        teams = http_json(LINEAR_GQL, {"query": "{ teams { nodes { id key name } } }"}, headers)
        match = None
        for t in teams.get("data", {}).get("teams", {}).get("nodes", []):
            if team_hint.lower() in (t.get("key", "") + t.get("name", "")).lower():
                match = t["id"]
                break
        if match:
            team_filter = f', team: {{ id: {{ eq: "{match}" }} }}'

    query = """
    query($since: DateTimeOrDuration!) {
      issues(filter: { updatedAt: { gte: $since } %s }, first: 100,
             orderBy: updatedAt) {
        nodes {
          id identifier title url priority dueDate updatedAt
          state { name type }
          assignee { displayName }
          description
          labels { nodes { name } }
        }
      }
    }""" % team_filter

    out = []
    res = http_json(LINEAR_GQL, {"query": query, "variables": {"since": since_iso}}, headers)
    for n in res.get("data", {}).get("issues", {}).get("nodes", []):
        out.append({
            "linear_id": n["id"],
            "identifier": n.get("identifier", ""),
            "title": n.get("title", ""),
            "url": n.get("url", ""),
            "state": (n.get("state") or {}).get("name", ""),
            "state_type": (n.get("state") or {}).get("type", ""),
            "due": n.get("dueDate"),
            "priority": n.get("priority"),
            "assignee": (n.get("assignee") or {}).get("displayName", ""),
            "labels": [l.get("name", "") for l in (n.get("labels") or {}).get("nodes", [])],
            "description": (n.get("description") or "")[:2000],
            "updatedAt": n.get("updatedAt", ""),
        })
    return out


# ---------------------------------------------------------------- slack

def fetch_slack_intel(bot_token, channel_ids, since_epoch):
    """Harvest recent Slack messages as intel (NOT auto-promoted to tasks).
    Promotion to Asana tasks requires an explicit rule from Nathan."""
    headers = {"Authorization": f"Bearer {bot_token}"}
    out = []
    for ch in channel_ids:
        url = (f"https://slack.com/api/conversations.history?channel={ch}"
               f"&oldest={since_epoch}&limit=100")
        res = http_json(url, headers=headers)
        if not res.get("ok"):
            out.append({"channel": ch, "error": res.get("error", "unknown")})
            continue
        for m in res.get("messages", []):
            if m.get("subtype") in ("channel_join", "channel_leave", "bot_message"):
                continue
            out.append({"channel": ch, "ts": m.get("ts"), "user": m.get("user", ""),
                        "text": (m.get("text") or "")[:1000]})
    return out


# ---------------------------------------------------------------- asana

PRIORITY_MAP = {1: "Urgent", 2: "High", 3: "Medium", 4: "Low"}  # Linear 0 = no priority


def asana_task_payload(issue):
    notes = [
        f"Source: Linear {issue['identifier']} — {issue['url']}",
        f"Linear state: {issue['state']}",
    ]
    if issue["assignee"]:
        notes.append(f"Linear assignee: {issue['assignee']}")
    if issue["labels"]:
        notes.append(f"Labels: {', '.join(issue['labels'])}")
    if issue["description"]:
        notes += ["", issue["description"]]
    notes += ["", "Synced by drawdown asana_sync.py — do not edit this block by hand."]
    payload = {
        "name": f"[{issue['identifier']}] {issue['title']}" if issue["identifier"] else issue["title"],
        "notes": "\n".join(notes),
    }
    if issue["due"]:
        payload["due_on"] = issue["due"]
    return payload


def sync_to_asana(pat, project_gid, issues, sync_map, dry_run):
    headers = {"Authorization": f"Bearer {pat}"}
    results = {"created": [], "updated": [], "completed": [], "skipped": [], "errors": []}
    for issue in issues:
        lid = issue["linear_id"]
        gid = sync_map.get(lid)
        done = issue["state_type"] in ("completed", "canceled")
        try:
            if gid is None:
                if dry_run:
                    results["created"].append(f"DRY: would create [{issue['identifier']}] {issue['title']}")
                    continue
                payload = asana_task_payload(issue)
                payload["projects"] = [project_gid]
                if done:
                    payload["completed"] = True
                res = http_json(f"{ASANA_API}/tasks", {"data": payload}, headers, method="POST")
                new_gid = res["data"]["gid"]
                sync_map[lid] = new_gid
                results["created"].append(f"{issue['identifier']} -> asana {new_gid}")
            else:
                if dry_run:
                    verb = "complete" if done else "update"
                    results["updated"].append(f"DRY: would {verb} {issue['identifier']} (asana {gid})")
                    continue
                payload = asana_task_payload(issue)
                if done:
                    payload["completed"] = True
                http_json(f"{ASANA_API}/tasks/{gid}", {"data": payload}, headers, method="PUT")
                (results["completed"] if done else results["updated"]).append(issue["identifier"])
        except urllib.error.HTTPError as e:
            body = ""
            try:
                body = e.read().decode()[:300]
            except Exception:
                pass
            results["errors"].append(f"{issue['identifier']}: HTTP {e.code} {body}")
        except Exception as e:  # noqa: BLE001 — log and continue, one bad issue must not kill the run
            results["errors"].append(f"{issue['identifier']}: {e}")
        time.sleep(0.3)  # stay well under Asana rate limits
    return results


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="print plan, write nothing")
def execute(dry_run=False, full=False):
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    sync_map_path = STATE_DIR / "sync_map.json"
    last_run_path = STATE_DIR / "last_run.txt"
    sync_map = load_json(sync_map_path, {})

    if full:
        since_iso = "2026-06-24T00:00:00.000Z"
        since_epoch = 0
    else:
        last = last_run_path.read_text().strip() if last_run_path.is_file() else None
        since_iso = last or "2026-07-22T00:00:00.000Z"
        since_epoch = int(datetime.fromisoformat(last.replace("Z", "+00:00")).timestamp()) if last else 0

    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    datestamp = datetime.now().strftime("%Y%m%d")
    log_dir = DRIVE_LOG_DIR if DRIVE_LOG_DIR.parent.is_dir() else LOCAL_LOG_DIR
    log_path = log_dir / f"asana_sync_{datestamp}.jsonl"

    summary = {"mode": "dry-run" if dry_run else "live", "since": since_iso,
               "log": str(log_path), "sources": {}, "asana": None}

    # --- Linear ---
    linear_key = read_config("linear_api_key")
    issues = []
    if not linear_key:
        summary["sources"]["linear"] = "SKIPPED — no ~/.config/drawdown2026/linear_api_key"
    else:
        try:
            issues = fetch_linear_updates(linear_key, read_config("linear_team_key"), since_iso)
            summary["sources"]["linear"] = f"{len(issues)} issues updated since {since_iso}"
        except Exception as e:  # noqa: BLE001
            summary["sources"]["linear"] = f"ERROR — {e}"
            log_line(log_path, {"event": "linear_error", "error": str(e)})

    # --- Slack (intel only, logged — no auto-promotion without a rule) ---
    slack_token = read_config("slack_bot_token")
    slack_channels = (read_config("slack_channel_ids") or "").split(",")
    slack_channels = [c.strip() for c in slack_channels if c.strip()]
    if not slack_token or not slack_channels:
        summary["sources"]["slack"] = "SKIPPED — no slack_bot_token / slack_channel_ids"
    else:
        try:
            intel = fetch_slack_intel(slack_token, slack_channels, since_epoch)
            for item in intel:
                log_line(log_path, {"event": "slack_intel", **item})
            summary["sources"]["slack"] = f"{len(intel)} messages logged to {log_path.name}"
        except Exception as e:  # noqa: BLE001
            summary["sources"]["slack"] = f"ERROR — {e}"

    # --- Asana ---
    asana_pat = read_config("asana_pat")
    project_gid = read_config("asana_project_gid")
    if not issues:
        summary["asana"] = "nothing to sync"
    elif not asana_pat or not project_gid:
        summary["asana"] = ("SKIPPED — need asana_pat + asana_project_gid in "
                            "~/.config/drawdown2026/ (Linear side fetched fine)")
    else:
        results = sync_to_asana(asana_pat, project_gid, issues, sync_map, dry_run)
        summary["asana"] = results
        if not dry_run:
            sync_map_path.write_text(json.dumps(sync_map, indent=2))

    if not dry_run:
        last_run_path.write_text(now_iso)

    log_line(log_path, {"event": "run_summary", **{k: (v if k != "asana" else "see stdout")
                                                    for k, v in summary.items()}})
    return {
        "summary": f"Linear: {summary['sources'].get('linear')} | Slack: {summary['sources'].get('slack')} | Asana: {summary['asana'] if isinstance(summary['asana'], str) else json.dumps(summary['asana'])}",
        "detail": summary,
    }


def run(ctx):
    """Managed-runner entrypoint (Blueprint code Automation)."""
    inp = ctx.get("input") if isinstance(ctx, dict) else None
    dry_run = bool(isinstance(inp, dict) and inp.get("dry_run"))
    full = bool(isinstance(inp, dict) and inp.get("full"))
    return {"artifact": execute(dry_run=dry_run, full=full)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="print plan, write nothing")
    ap.add_argument("--full", action="store_true", help="ignore last-run watermark, rescan 30 days")
    args = ap.parse_args()
    artifact = execute(dry_run=args.dry_run, full=args.full)
    print(json.dumps({"artifact": artifact}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
