"""Build the Meta Business Suite / IG / TikTok scheduling pack.

Nate, sit-down 2026-09-06: "schedule them in Meta Business Suite — build the pack",
"same with our IG and tiktok etc". One dated folder per posting slot, each holding
the exact file to upload and the caption to paste. Nothing posts itself.
"""
import os, shutil, json, datetime, hashlib

MEDIA = os.path.expanduser("~/drawdown-2026-campaign/06_Media_Build")
OUT = os.path.join(MEDIA, "SCHEDULING_PACK")
CARDS = os.path.join(MEDIA, "cards")

RENDERS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "renders")
# substring of the slot's platform string -> render subfolder from build_platform_renders.py
PLATFORM_KEYS = [("IG Reels", "ig-reels"), ("TikTok", "tiktok"), ("FB", "fb-reels"), ("Google Business", "gbp")]

CTA = "Text TRUXOR to 254-780-6971."
TAGS = "#lakeaustin #drawdown #hydrilla #atxlakescapes #austintx #lakelife #dockrepair"

# (date, weekday, platform, kind, source file, title, caption)
SLOTS = [
    # 2026-09-07: the SIGNED method cut is v1 (Nate 09-06). v2 was built after that
    # sign, in response to Victoria's copy note, and the v2-vs-v1 pick came back
    # unanswered — the answers board returned singer/read/lcd/type/cards10/poster/more
    # and no `reels`. Today's slot ships the signed asset; v2 waits for the pick.
    ("2026-09-07", "Mon", "IG Reels · TikTok · FB", "video", "DRAWDOWN_ScrapeHaulStaple_916_SUNO_MudWindow_v2.mp4",
     "Method cut — scrape haul cover",
     "Three words. That's the dry-window job.\n\nScrape the marked bed.\nHaul the spoil off your lot.\nCover the bed while the lake is down.\n\nLake Austin comes down about 10 feet starting Oct 12. Seven weeks of dry ground, then it refills.\n\n" + CTA),
    ("2026-09-09", "Wed", "IG Reels · TikTok", "video", "DRAWDOWN_ViralHydrilla_916_STUDIO_CLAUDE_VO_MikeRow.mp4",
     "Viral lead-in + VO",
     "This is what's under Lake Austin docks. Ten years of it — and you've never seen it.\n\nThe drawdown is official. About 10 feet, starting Oct 12.\n\nTwo amphibious machines. We scrape it, haul it off, cover it.\n\n" + CTA),
    ("2026-09-11", "Fri", "IG Story", "image", "DRAWDOWN_Card_S01_dates_916.jpg", "S01 — the dates",
     "Oct 12 – Nov 30. Lake Austin comes down about 10 feet. LCRA and the City announced it.\n\n" + CTA),
    ("2026-09-11", "Fri", "IG Feed · FB · LinkedIn", "image", "DRAWDOWN_Card_S02_under-your-dock_45.jpg",
     "S02 — under your dock",
     "This is under your dock. Nearly ten years since anyone could see it.\n\nWhen the lake drops about 10 feet on Oct 12, you get seven weeks of dry ground to deal with it.\n\n" + CTA),
    ("2026-09-14", "Mon", "IG Reels · TikTok · FB", "video", "DRAWDOWN_LakeComingDown_916_v2_SUNO_BED.mp4",
     "Lake Coming Down — HERO attractor",
     "Oct 12, the lake starts down. About a foot a day, to roughly 10 feet below normal.\n\nNobody's seen that lakebed since 2017. You get seven weeks — Nov 24 it starts refilling.\n\nThe next window may be eight to ten years away.\n\n" + CTA),
    ("2026-09-14", "Mon", "Google Business Profile", "video", "DRAWDOWN_LakeComingDown_916_v2_SUNO_BED.mp4",
     "GBP — listing video + Google Post",
     "Lake Austin drops Oct 12. About 10 feet, LCRA. We scrape, haul, and cover while it's down.\n\nText TRUXOR to 254-780-6971."),
    ("2026-09-16", "Wed", "IG Reels · TikTok", "video", "DRAWDOWN_ScrapeHaulStaple_916_SUNO_MudWindow_v2.mp4",
     "Method cut rerun",
     "Scrape the marked bed. Haul the spoil off your lot. Cover it while the lake is down.\n\nThree words, one dry window.\n\n" + CTA),
    ("2026-09-18", "Fri", "IG Story", "image", "DRAWDOWN_Card_S03_past-the-dock_916.jpg", "S03 — past the dock",
     "It doesn't stop at the dock. Hydrilla runs the whole shallow shelf.\n\n" + CTA),
    ("2026-09-18", "Fri", "IG Feed · FB · LinkedIn", "image", "DRAWDOWN_Card_S07_two-machines_45.jpg",
     "S07 — two machines",
     "Two amphibious machines, committed for the drawdown window.\n\nThey work where a truck can't and a boat won't.\n\n" + CTA),
    ("2026-09-21", "Mon", "IG Reels · TikTok · FB", "video", "DRAWDOWN_WorkTheBed_916_STUDIO_CountryA_from28s.mp4",
     "Work the Bed — the song",
     "We work the bed.\n\nTwo amphibious machines. Scrape it, haul it, cover it — while Lake Austin is down.\n\nLake Austin is home.\n\n" + CTA),
    ("2026-09-23", "Wed", "IG Reels · TikTok · FB", "video", "DRAWDOWN_Turnkey_916_SUNO_BED.mp4",
     "Turnkey — DRAFT until Nate Gate 3",
     "Lake Austin comes down Oct 12.\n\nYou don't file the City permit. You don't file LCRA. We do.\n\nOur crew. Our iron. Amphibious Truxors on the bed.\nOff the barge. Into the dump trailer. Gone off your lot.\n\nWe run it. You don't.\n\n" + CTA),
    ("2026-09-25", "Fri", "IG Story ×3", "image", "DRAWDOWN_Card_S04_scrape_916.jpg", "S04–S06 — scrape / haul / cover",
     "Scrape. Haul. Cover. Post all three back to back as one story run.\n\n" + CTA),
    ("2026-09-25", "Fri", "IG Feed · FB", "image", "DRAWDOWN_Card_S06_cover_45.jpg", "S06 — cover",
     "Cover the bed while the lake is down. A covered bed doesn't grow back through the mat.\n\n" + CTA),
    ("2026-09-28", "Mon", "IG Reels · TikTok · FB", "video", "DRAWDOWN_Bulkhead_916_STUDIO.mp4",
     "Bulkhead — what the water hides",
     "What the water hides.\n\nYour wall. Your dock footings. You'll see them Oct 12 — and you can fix them on dry ground.\n\n" + CTA),
    ("2026-09-30", "Wed", "IG Reels · TikTok", "video", "DRAWDOWN_LakeComingDown_916_v2_SUNO_BED.mp4",
     "Lake Coming Down rerun", "Twelve days out. About 10 feet. Seven weeks.\n\n" + CTA),
    ("2026-10-02", "Fri", "IG Story", "image", "DRAWDOWN_Card_S08_seven-weeks_916.jpg", "S08 — seven weeks",
     "Seven weeks. Oct 12 to Nov 30. Then it refills.\n\n" + CTA),
    ("2026-10-05", "Mon", "IG Story · FB", "image", "DRAWDOWN_Card_S09_seven-days_916.jpg", "S09 — 7 days",
     "7 days. Lake Austin comes down Monday, Oct 12.\n\n" + CTA),
    ("2026-10-07", "Wed", "IG Reels · TikTok", "video", "DRAWDOWN_WorkTheBed_916_STUDIO_CountryA_from28s.mp4",
     "Work the Bed rerun", "Five days out. We work the bed.\n\n" + CTA),
    ("2026-10-12", "Mon", "IG Story · FB · TikTok", "image", "DRAWDOWN_Card_S10_monday_916.jpg", "S10 — MONDAY",
     "The lake starts down today. About a foot a day.\n\nSeven weeks of dry ground starts now.\n\n" + CTA),
]

if os.path.isdir(OUT):
    shutil.rmtree(OUT)
os.makedirs(OUT)
rows, missing = [], []
for date, wd, plat, kind, src, title, caption in SLOTS:
    p = os.path.join(CARDS if kind == "image" else MEDIA, src)
    if not os.path.exists(p):
        missing.append(src); continue
    slug = f"{date}_{title.split(' — ')[0].replace(' ', '-').replace('/', '-')}"
    d = os.path.join(OUT, slug)
    os.makedirs(d, exist_ok=True)
    shutil.copy2(p, os.path.join(d, src))
    # Per-platform renders (build_platform_renders.py): when they exist for this master,
    # Hallie uploads <slot>/<platform>/ — the file cut for that app — not the master.
    stem = os.path.splitext(src)[0]
    plats = []
    for key, sub in PLATFORM_KEYS:
        r = os.path.join(RENDERS, stem, sub, "render.mp4")
        if key in plat and os.path.exists(r):
            os.makedirs(os.path.join(d, sub), exist_ok=True)
            shutil.copy2(r, os.path.join(d, sub, f"{stem}__{sub}.mp4"))
            shutil.copy2(os.path.join(RENDERS, stem, sub, "safezone_proof_cta.png"), os.path.join(d, sub, "safezone_proof.png"))
            plats.append(sub)
    with open(os.path.join(d, "caption.txt"), "w") as f:
        if "Google Business" in plat:
            f.write(caption.rstrip() + "\n")
        else:
            f.write(caption + "\n\n" + TAGS + "\n")
    rows.append(dict(date=date, weekday=wd, platform=plat, kind=kind, file=src, title=title,
                     folder=slug, md5=hashlib.md5(open(p, "rb").read()).hexdigest()[:12],
                     bytes=os.path.getsize(p), platform_renders=plats))

with open(os.path.join(OUT, "pack.json"), "w") as f:
    json.dump(rows, f, indent=2)

md = ["# Scheduling pack — Meta Business Suite / IG / TikTok",
      "",
      "Built by `proof/pack.py` from the signed masters. **Nothing here posts itself.**",
      "One folder per slot: the exact file to upload and `caption.txt` to paste.",
      "",
      "Nate, sit-down 2026-09-06: *\"schedule them in Meta Business Suite — build the pack\"*, *\"same with our IG and tiktok etc\"*.",
      "",
      "## How to load a week",
      "",
      "1. Meta Business Suite → Planner → Create post → pick Instagram + Facebook.",
      "2. Drag the file from the slot folder. Paste `caption.txt`.",
      "3. Set the date and 9:00 AM CT. Schedule.",
      "4. TikTok is a separate upload — same file, same caption, TikTok's own scheduler (up to 10 days out).",
      "5. **Google Business Profile (Sep 14 only):** upload the same Lake Coming Down 30s as the **listing video**, then a Google Post with that folder's `caption.txt`. Leave it up. Do not stack method/viral/turnkey on the listing.",
      "",
      "Reels are 1080×1920. Feed stills marked `_45` are 1080×1350 (4:5). Stories use the `_916`.",
      "",
      "**Platform subfolders.** When a slot folder holds `ig-reels/`, `tiktok/`, `fb-reels/` or `gbp/`, upload THAT file to that app, not the master beside it. Each subfolder carries its own `safezone_proof.png` (red = the app's UI, green = safe).",
      "",
      "| Date | Day | Platform | Piece | File | Folder |",
      "|---|---|---|---|---|---|"]
for r in rows:
    md.append(f"| {r['date']} | {r['weekday']} | {r['platform']} | {r['title']} | `{r['file']}` | `{r['folder']}/` |")
md += ["", f"{len(rows)} slots · {sum(r['bytes'] for r in rows)/1e6:.1f} MB.",
       "", "⚠️ Every caption avoids the banned set (no $695, credited, assessment, exploring, unofficial, projected 10–12, extinct). Verified by `voice-qa.sh`."]
if missing:
    md += ["", "**MISSING masters — slots skipped:**"] + [f"- `{m}`" for m in missing]
open(os.path.join(OUT, "README.md"), "w").write("\n".join(md) + "\n")
print(f"{len(rows)} slots, {len(missing)} missing")
for m in missing:
    print("  MISSING", m)
