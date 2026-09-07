"""Build the clickable campaign calendar Lavish page from pack.json — no hand-typed data."""
import json, os, shutil, datetime, html

MEDIA = os.path.expanduser("~/drawdown-2026-campaign/06_Media_Build")
PACK = os.path.join(MEDIA, "SCHEDULING_PACK")
OUT = os.path.expanduser("~/drawdown-2026-campaign/.lavish/calendar")
os.makedirs(OUT, exist_ok=True)
rows = json.load(open(os.path.join(PACK, "pack.json")))

# copy each asset once, thumbnail the images
seen = {}
for r in rows:
    src = os.path.join(PACK, r["folder"], r["file"])
    dst = os.path.join(OUT, r["file"])
    if r["file"] not in seen:
        if r["kind"] == "image":
            from PIL import Image
            im = Image.open(src); im.thumbnail((420, 746)); im.save(dst, quality=82)
        else:
            shutil.copy2(src, dst)
        seen[r["file"]] = True
    r["caption"] = open(os.path.join(PACK, r["folder"], "caption.txt")).read().strip()

# calendar grid: Sep 7 → Oct 12
start = datetime.date(2026, 9, 7)
end = datetime.date(2026, 10, 18)
by_date = {}
for r in rows:
    by_date.setdefault(r["date"], []).append(r)

MILE = {"2026-10-12": ("LOWERING STARTS", "about a foot a day"),
        "2026-11-24": ("REFILL BEGINS", ""), "2026-11-30": ("NORMAL POOL", "")}

cells = []
d = start - datetime.timedelta(days=start.weekday())
while d <= end:
    key = d.isoformat()
    items = by_date.get(key, [])
    cls = "day"
    if d < start: cls += " past"
    if key in MILE: cls += " mile"
    if items: cls += " has"
    inner = [f'<div class="dnum">{d.day}</div>']
    if key in MILE:
        inner.append(f'<div class="milelabel">{MILE[key][0]}</div>')
    for r in items:
        icon = "▶" if r["kind"] == "video" else "▣"
        inner.append(f'<button class="slot {r["kind"]}" data-lavish-action data-file="{html.escape(r["file"])}" '
                     f'data-kind="{r["kind"]}" data-title="{html.escape(r["title"])}" data-plat="{html.escape(r["platform"])}" '
                     f'data-folder="{html.escape(r["folder"])}" data-caption="{html.escape(r["caption"])}" '
                     f'onclick="show(this)">{icon} {html.escape(r["title"].split(" — ")[0])}</button>')
    cells.append(f'<div class="{cls}"><div class="dwrap">{"".join(inner)}</div></div>')
    d += datetime.timedelta(days=1)

nvid = len({r["file"] for r in rows if r["kind"] == "video"})
nimg = len({r["file"] for r in rows if r["kind"] == "image"})

HTML = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Drawdown 2026 — Campaign Calendar</title>
<style>
:root{{--ink:#121A20;--ink2:#1B252D;--ink3:#232F38;--cream:#F4EFE6;--dim:#9AA5AD;--copper:#E8B070;--good:#7FB069;--mono:ui-monospace,SFMono-Regular,Menlo,monospace}}
*{{box-sizing:border-box;min-width:0}}
body{{margin:0;background:var(--ink);color:var(--cream);font:15px/1.5 -apple-system,"Source Sans 3",Helvetica,Arial,sans-serif}}
.wrap{{max-width:1400px;margin:0 auto;padding:26px 20px 90px}}
header{{border-bottom:1px solid #2b3740;padding-bottom:16px;margin-bottom:20px}}
.kicker{{font-family:var(--mono);font-size:11px;letter-spacing:.14em;color:var(--copper);margin:0 0 6px}}
h1{{font-size:32px;margin:0 0 8px}}
.lede{{color:var(--dim);margin:0;max-width:840px}}
.stats{{display:flex;gap:12px;flex-wrap:wrap;margin-top:14px}}
.stats div{{background:var(--ink2);border:1px solid #2b3740;border-radius:10px;padding:9px 13px;font-family:var(--mono);font-size:11px;color:var(--dim)}}
.stats b{{display:block;color:var(--copper);font-size:17px;font-family:inherit}}
.legend{{display:flex;gap:16px;flex-wrap:wrap;margin:16px 0 6px;font-size:12.5px;color:var(--dim)}}
.legend span{{display:flex;align-items:center;gap:6px}}
.dot{{width:10px;height:10px;border-radius:3px;display:inline-block}}
.cal{{display:grid;grid-template-columns:repeat(7,1fr);gap:7px;margin-top:10px}}
.hd{{font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;color:var(--dim);text-align:center;padding:4px 0}}
.day{{background:var(--ink2);border:1px solid #2b3740;border-radius:9px;min-height:104px;padding:7px}}
.day.past{{opacity:.3}}
.day.has{{border-color:#3a4a56}}
.day.mile{{border-color:var(--copper);background:rgba(232,176,112,.09)}}
.dnum{{font-family:var(--mono);font-size:11px;color:var(--dim);margin-bottom:5px}}
.milelabel{{font-family:var(--mono);font-size:9.5px;letter-spacing:.06em;color:var(--copper);margin-bottom:5px;line-height:1.3}}
.slot{{display:block;width:100%;text-align:left;margin:0 0 4px;padding:6px 7px;border-radius:6px;border:0;cursor:pointer;
  font:600 11.5px/1.35 inherit;color:var(--cream);background:var(--ink3)}}
.slot.video{{background:rgba(232,176,112,.17);color:#F6D9B4}}
.slot.image{{background:rgba(127,176,105,.15);color:#CDE4C2}}
.slot:hover{{outline:1px solid var(--copper)}}
#panel{{position:fixed;inset:auto 0 0 0;background:var(--ink2);border-top:1px solid var(--copper);
  padding:18px 22px 22px;display:none;max-height:78vh;overflow:auto;box-shadow:0 -18px 44px rgba(0,0,0,.55)}}
#panel.on{{display:block}}
.pgrid{{max-width:1360px;margin:0 auto;display:grid;gap:22px;grid-template-columns:minmax(0,250px) minmax(0,1fr)}}
@media(max-width:720px){{.pgrid{{grid-template-columns:1fr}}}}
#pmedia video,#pmedia img{{width:100%;border-radius:10px;display:block;background:#000}}
#ptitle{{font-size:20px;font-weight:700;margin:0 0 4px}}
#pmeta{{font-family:var(--mono);font-size:11px;color:var(--dim);margin-bottom:12px}}
#pcap{{background:var(--ink);border:1px solid #2b3740;border-radius:10px;padding:13px 15px;white-space:pre-wrap;font-size:14px;color:#DCD6CB}}
.close{{position:absolute;top:14px;right:20px;background:none;border:0;color:var(--dim);font-size:24px;cursor:pointer}}
footer{{color:var(--dim);font-size:13px;margin-top:26px;border-top:1px solid #2b3740;padding-top:18px}}
code{{font-family:var(--mono);font-size:.9em;color:var(--copper)}}
form.decide{{margin-top:22px}}
fieldset{{border:1px solid #2b3740;border-radius:12px;padding:14px 16px 16px;background:rgba(27,37,45,.5)}}
legend{{font-family:var(--mono);font-size:11px;letter-spacing:.12em;color:var(--copper);padding:0 8px}}
.choices{{display:grid;gap:8px;grid-template-columns:repeat(auto-fit,minmax(min(100%,250px),1fr))}}
.choice{{display:flex;gap:10px;padding:10px 12px;border:1px solid #2b3740;border-radius:10px;cursor:pointer;background:var(--ink)}}
.choice:has(input:checked){{border-color:var(--copper);background:rgba(232,176,112,.08)}}
.choice input{{margin-top:4px;accent-color:var(--copper)}}
.choice b{{display:block}}.choice i{{font-style:normal;color:var(--dim);font-size:13px}}
textarea{{width:100%;margin-top:12px;min-height:70px;background:var(--ink);color:var(--cream);border:1px solid #2b3740;border-radius:10px;padding:10px;font:inherit}}
button.q{{background:var(--copper);color:var(--ink);border:0;border-radius:10px;padding:10px 16px;font-weight:700;cursor:pointer;font:inherit;margin-top:12px}}
.queued{{font-family:var(--mono);font-size:12px;color:var(--good);margin-left:10px}}
</style></head><body><div class="wrap">

<header>
  <p class="kicker">ATX LAKESCAPES · DRAWDOWN 2026 · CAMPAIGN CALENDAR</p>
  <h1>Every post, every date, click to see it</h1>
  <p class="lede">The whole runway from tomorrow to the day the lake starts down. Click any tile: the actual file plays and the caption that ships with it is right there. All of it is built, signed, and sitting in <code>06_Media_Build/SCHEDULING_PACK/</code> — one folder per slot, file plus <code>caption.txt</code>, ready to load into Meta Business Suite.</p>
  <div class="stats">
    <div>Slots<b>{len(rows)}</b></div>
    <div>Unique videos<b>{nvid}</b></div>
    <div>Unique stills<b>{nimg}</b></div>
    <div>First post<b>Mon Sep 7</b></div>
    <div>Lowering<b>Mon Oct 12</b></div>
    <div>Refill<b>Tue Nov 24</b></div>
  </div>
  <div class="legend">
    <span><i class="dot" style="background:rgba(232,176,112,.6)"></i> reel / video</span>
    <span><i class="dot" style="background:rgba(127,176,105,.6)"></i> still / story</span>
    <span><i class="dot" style="background:var(--copper)"></i> LCRA milestone</span>
  </div>
</header>

<div class="cal">
  <div class="hd">MON</div><div class="hd">TUE</div><div class="hd">WED</div><div class="hd">THU</div><div class="hd">FRI</div><div class="hd">SAT</div><div class="hd">SUN</div>
  {"".join(cells)}
</div>

<form class="decide" data-lavish-question="calendar" onsubmit="q(event)">
  <fieldset><legend>Anything you'd move</legend>
    <div class="choices">
      <label class="choice"><input type="radio" name="calendar" value="calendar approved — load the pack into Meta"><span><b>Approved</b><i>Load the pack and schedule it.</i></span></label>
      <label class="choice"><input type="radio" name="calendar" value="move something — notes below"><span><b>Move something</b><i>Which slot, to when.</i></span></label>
      <label class="choice"><input type="radio" name="calendar" value="caption edits — notes below"><span><b>Caption edits</b><i>Which post, what line.</i></span></label>
      <label class="choice"><input type="radio" name="calendar" value="more posts per week"><span><b>Denser</b><i>More than 3+1 a week.</i></span></label>
    </div>
    <textarea name="why" placeholder="Date + what changes."></textarea>
    <button class="q" type="submit">Queue</button><span class="queued" id="qd"></span>
  </fieldset>
</form>

<footer>
  <b>Reality check:</b> nothing here posts itself. The pack is files and captions; a person loads them into Meta Business Suite (IG + FB together) and TikTok separately.
  Everything from Oct 12 on is a placeholder until somebody shoots the window — the shoot list is in <code>PRODUCTION_SCHEDULE_2026-09-07.md</code>, and the first item is still a tarp with the overlap and a staple visible.
</footer>
</div>

<div id="panel">
  <button class="close" onclick="document.getElementById('panel').classList.remove('on')">×</button>
  <div class="pgrid">
    <div id="pmedia"></div>
    <div>
      <p id="ptitle"></p>
      <div id="pmeta"></div>
      <div id="pcap"></div>
    </div>
  </div>
</div>

<script>
function show(el){{
  var d = el.dataset;
  document.getElementById('pmedia').innerHTML = d.kind === 'video'
    ? '<video src="' + d.file + '" controls autoplay playsinline></video>'
    : '<img src="' + d.file + '" alt="">';
  document.getElementById('ptitle').textContent = d.title;
  document.getElementById('pmeta').textContent = d.plat + '  ·  ' + d.file + '  ·  SCHEDULING_PACK/' + d.folder + '/';
  document.getElementById('pcap').textContent = d.caption;
  document.getElementById('panel').classList.add('on');
}}
function q(ev){{
  ev.preventDefault();
  var f = ev.currentTarget, fd = new FormData(f);
  var pick = fd.get('calendar'), why = (fd.get('why')||'').toString().trim();
  if(!pick && !why) return;
  var msg = 'Campaign calendar: ' + (pick || '(notes only)');
  if(why) msg += ' — "' + why + '"';
  if(window.lavish && window.lavish.queuePrompt){{
    window.lavish.queuePrompt(msg, {{tag:'calendar', text:'Calendar: ' + (pick||'notes'), element:f, queueKey:'calendar',
      data:{{question:'calendar', answer:pick||null, rationale:why||null}}}});
  }}
  document.getElementById('qd').textContent = '✓ queued';
}}
</script>
</body></html>
"""
open(os.path.join(OUT, "calendar.html"), "w").write(HTML)
print("wrote calendar.html;", len(rows), "slots,", len(seen), "assets copied")
