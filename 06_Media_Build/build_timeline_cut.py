"""Shared 9:16 timeline builder — real clips and real stills, straps, xfade, optional bed.

One builder, several cuts. `python3 build_timeline_cut.py lake-coming-down` or
`... bulkhead`. Each cut is a BEATS list at the bottom of this file, nothing else.

What it refuses to do (the rules this folder learned the hard way):
- No generated pixels. Clips are the 2026-08-11 DJI proxies (real Lake Austin,
  see PROVENANCE.md there); stills are Poseidon plates pinned by sha256.
- Proxies are 1280x720 — NEVER upscaled to fill 9:16. Letterboxed over a blurred
  cover of themselves (compose.py "fit" precedent).
- Registry width/height beats the EXIF tag on stills; mismatch fails closed.
- A count word (TWO / BOTH / PAIR) may only ride a C7-eyeballed plate.
- Banned strings fail the build before ffmpeg runs.
- Audio: `-an` silent master always; a bed master only if BED is set, trimmed to
  the picture with a 1.5 s tail fade. Loudness is measured after, not assumed.

Ships `<name>.mp4` (silent), `<name>_<bed>.mp4` (with bed), and a resolve bin
`resolve/<slug>/` with every strap PNG, one QC frame per beat, and PINS.md.
"""
import hashlib
import os
import re
import sqlite3
import subprocess
import sys

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.expanduser("~/Poseidon/visual-library/library.db")
PHOTOS = os.path.expanduser("~/Poseidon/visual-library/photos")
AERIALS = os.path.expanduser("~/ATX-Jobs/06_Drawdown_Sales_Engine/00-source/aerials/2026-08-11-drawdown-scouting")
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
W, H, FPS, XF = 1080, 1920, 30, 0.35
SLOW = 1.6                      # clip playback = 1/SLOW speed (Victoria 2026-09-06)
CREAM, COPPER = (244, 239, 230, 255), (232, 176, 112, 255)
BANNED = re.compile(r"695|CREDITED|ASSESSMENT|NOTHING IS OFFICIAL|EXPLORING|UNOFFICIAL|EXTINCT|\bCY\b", re.I)
COUNT = re.compile(r"\b(TWO|BOTH|PAIR|2)\b")
C7_TWO_MACHINE = {"c6b6853c038a", "fd49bf6ffe3e"}

con = sqlite3.connect(DB)


def clip(n):
    return f"{AERIALS}/2026-08-11_la-rob-roy_drawdown-scouting_drone-wide_{n}.mp4"


def resolve(prefix):
    row = con.execute("SELECT sha256, width, height FROM refs WHERE sha256 LIKE ?", (prefix + "%",)).fetchone()
    if not row:
        raise SystemExit(f"UNPINNED: {prefix}")
    path = os.path.join(PHOTOS, row[0] + ".jpg")
    if not os.path.exists(path):
        raise SystemExit(f"NO LOCAL BYTES: {row[0]}")
    raw = Image.open(path)
    im = ImageOps.exif_transpose(raw).convert("RGB")
    if (im.width > im.height) != (row[1] > row[2]) and (raw.width > raw.height) == (row[1] > row[2]):
        print(f"  EXIF tag ignored for {row[0][:12]} — registry says {row[1]}x{row[2]}")
        im = raw.convert("RGB")
    if (im.width > im.height) != (row[1] > row[2]):
        raise SystemExit(f"ORIENTATION: {row[0][:12]}")
    return row[0], im


def cover(im, w, h):
    s = max(w / im.width, h / im.height)
    im = im.resize((int(im.width * s) + 1, int(im.height * s) + 1), Image.LANCZOS)
    l, t = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((l, t, l + w, t + h))


def fit_plate(im):
    """Letterbox the full frame over a blurred, darkened cover of itself. No upscale past width."""
    bg = ImageEnhance.Brightness(cover(im, W, H).filter(ImageFilter.GaussianBlur(38))).enhance(0.5)
    s = min(W / im.width, 1.0) if im.width >= W else W / im.width
    fg = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
    bg.paste(fg, ((W - fg.width) // 2, int(H * 0.44) - fg.height // 2))
    return bg


def strap(lines, dark=False):
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if dark:
        d.rectangle([0, 0, W, H], fill=(10, 18, 24, 235))
    top = int(H * 0.50)
    for y in range(top, H):
        t = (y - top) / (H - top)
        d.line([(0, y), (W, y)], fill=(10, 18, 24, int(205 * t ** 0.7)))
    rendered = [(t, ImageFont.truetype(BOLD, s), c) for t, s, c in lines]
    heights = [d.textbbox((0, 0), t, font=f)[3] for t, f, _ in rendered]
    gap = 22
    total = sum(heights) + gap * (len(rendered) - 1)
    y = (int(H * 0.5) if dark else int(H * 0.74)) - total // 2
    widest = max(d.textbbox((0, 0), t, font=f)[2] for t, f, _ in rendered)
    if widest > W - 80:
        raise SystemExit(f"STRAP OVERFLOW: {lines}")
    if not dark:
        plate = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        ImageDraw.Draw(plate).rounded_rectangle(
            [(W - widest) // 2 - 52, y - 36, (W + widest) // 2 + 52, y + total + 36], radius=20, fill=(10, 18, 24, 160))
        img.alpha_composite(plate)
        d = ImageDraw.Draw(img)
    d.rectangle([(W - 120) // 2, y - 30, (W + 120) // 2, y - 24], fill=COPPER)
    for i, (t, f, c) in enumerate(rendered):
        x = (W - d.textbbox((0, 0), t, font=f)[2]) // 2
        d.text((x + 3, y + 3), t, font=f, fill=(0, 0, 0, 180))
        d.text((x, y), t, font=f, fill=c)
        y += heights[i] + gap
    return img


def build(slug, out_name, beats, bed=None):
    work = os.path.join(HERE, f"_{slug}")
    rbin = os.path.join(HERE, "resolve", slug)
    os.makedirs(work, exist_ok=True)
    os.makedirs(rbin, exist_ok=True)
    pins, segs = [], []
    for i, (kind, src, tin, dur, lines) in enumerate(beats):
        text = " ".join(t for t, _, _ in lines).upper()
        if BANNED.search(text):
            raise SystemExit(f"BANNED: beat {i} {text!r}")
        if COUNT.search(text) and not (kind == "still" and src in C7_TWO_MACHINE):
            raise SystemExit(f"C7: beat {i} claims a count over a non-verified plate")
        sp = os.path.join(work, f"strap{i}.png")
        strap(lines, dark=(kind == "card")).save(sp)
        seg = os.path.join(work, f"seg{i}.mp4")
        n = int(dur * FPS)
        fade = f"format=rgba,fade=t=in:st=0.45:d=0.35:alpha=1,fade=t=out:st={dur - 0.30:.2f}:d=0.30:alpha=1"
        if kind == "clip":
            path = clip(src)
            assert os.path.exists(path), path
            # Victoria 2026-09-06: the drone is moving while it records, so the
            # cuts feel shaky. Deshake, then slow to 1/SLOW speed with motion
            # interpolation so it reads as a glide, not a duplicated-frame judder.
            pre = f"deshake=rx=32:ry=32:edge=mirror,setpts={SLOW}*PTS,minterpolate=fps={FPS}:mi_mode=mci:mc_mode=aobmc:vsbmc=1,"
            fc = (f"[0:v]{pre}split=2[bg][fg];"
                  f"[bg]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},boxblur=42:1,eq=brightness=-0.18[bgb];"
                  f"[fg]scale={W}:-2[fgs];[bgb][fgs]overlay=(W-w)/2:(H-h)/2,fps={FPS},setsar=1[base];"
                  f"[1:v]{fade}[s];[base][s]overlay=0:0,format=yuv420p[v]")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(tin), "-t", f"{dur / SLOW + 0.5:.2f}", "-i", path,
                            "-loop", "1", "-framerate", str(FPS), "-t", f"{dur:.2f}", "-i", sp,
                            "-filter_complex", fc, "-map", "[v]", "-t", f"{dur:.2f}", "-an",
                            "-c:v", "libx264", "-crf", "18", "-preset", "slow", seg], check=True)
            pin = f"clip {src} in={tin}s"
        else:
            if kind == "still":
                sha, im = resolve(src)
                plate = fit_plate(im) if (im.width / im.height) > (W / H) else cover(im, W, H)
                pin = f"still {sha}"
            else:  # card — dark type plate over a blurred frame of the named clip
                bp0 = os.path.join(work, f"cardbase{i}.jpg")
                subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(tin), "-i", clip(src), "-frames:v", "1", bp0], check=True)
                plate = ImageEnhance.Brightness(cover(Image.open(bp0).convert("RGB"), W, H).filter(ImageFilter.GaussianBlur(30))).enhance(0.55)
                pin = f"card over clip {src} t={tin}s"
            bp = os.path.join(work, f"plate{i}.jpg")
            plate.save(bp, quality=95)
            z = f"1.0+0.06*on/{n}" if i % 2 == 0 else f"1.06-0.06*on/{n}"
            fc = (f"[0:v]scale=2160:3840:flags=lanczos,zoompan=z='{z}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d=1:s={W}x{H}:fps={FPS},setsar=1[base];"
                  f"[1:v]{fade}[s];[base][s]overlay=0:0,format=yuv420p[v]")
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", str(FPS), "-t", f"{dur:.2f}", "-i", bp,
                            "-loop", "1", "-framerate", str(FPS), "-t", f"{dur:.2f}", "-i", sp,
                            "-filter_complex", fc, "-map", "[v]", "-t", f"{dur:.2f}", "-an",
                            "-c:v", "libx264", "-crf", "18", "-preset", "slow", seg], check=True)
        segs.append(seg)
        pins.append((i, kind, pin, dur, text))
        print(f"beat {i} {kind:5s} {dur:.2f}s  {pin}  — {text}")

    # xfade chain
    ins = []
    for s in segs:
        ins += ["-i", s]
    parts, chain, elapsed, starts = [], "0:v", beats[0][3], [0.0]
    for i in range(1, len(segs)):
        off = elapsed - XF
        parts.append(f"[{chain}][{i}:v]xfade=transition=fade:duration={XF}:offset={off:.2f}[x{i}]")
        chain = f"x{i}"
        starts.append(off)
        elapsed = off + beats[i][3]
    total = elapsed
    fg = ";".join(parts) if parts else f"[0:v]null[x0]"
    chain = chain if parts else "x0"
    out = os.path.join(HERE, out_name + ".mp4")
    subprocess.run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", fg, "-map", f"[{chain}]",
                    "-t", f"{total:.2f}", "-an", "-c:v", "libx264", "-crf", "18", "-preset", "slow",
                    "-pix_fmt", "yuv420p", "-r", str(FPS), "-movflags", "+faststart", out], check=True)
    outs = [out]
    if bed:
        bed_name, bed_path, *rest = bed
        bed_in = rest[0] if rest else 0.0          # seconds into the track to start
        outb = os.path.join(HERE, f"{out_name}_{bed_name}.mp4")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", out, "-ss", f"{bed_in:.2f}", "-i", bed_path,
                        "-af", f"atrim=0:{total:.2f},afade=t=in:st=0:d=0.5,afade=t=out:st={total - 1.5:.2f}:d=1.5",
                        "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                        "-shortest", "-movflags", "+faststart", outb], check=True)
        outs.append(outb)

    # proof: QC frame mid-beat, straps, pins, md5
    for i, (kind, src, tin, dur, lines) in enumerate(beats):
        t = starts[i] + dur / 2
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.2f}", "-i", out, "-frames:v", "1",
                        os.path.join(rbin, f"QC_b{i}_t{t:.1f}.png")], check=True)
        os.replace(os.path.join(work, f"strap{i}.png"), os.path.join(rbin, f"strap_b{i}.png"))
    with open(os.path.join(rbin, "PINS.md"), "w") as f:
        f.write(f"# {out_name} — pins\n\nBuilt by `build_timeline_cut.py {slug}`. {total:.2f} s, {W}x{H}, {FPS} fps, CRF 18, xfade {XF}s.\n\n")
        for o in outs:
            md5 = hashlib.md5(open(o, "rb").read()).hexdigest()
            f.write(f"- `{os.path.basename(o)}` md5 `{md5}`\n")
        f.write("\n| beat | start | dur | source | strap | QC (claim · strap · orientation · crop) |\n|---|---|---|---|---|---|\n")
        for (i, kind, pin, dur, text), st in zip(pins, starts):
            f.write(f"| {i} | {st:.2f} | {dur:.2f} | {pin} | {text} | pending eye pass |\n")
    print(f"\nWROTE {[os.path.basename(o) for o in outs]} total={total:.2f}s  bin={rbin}")


CUTS = {
    "lake-coming-down": dict(
        out_name="DRAWDOWN_LakeComingDown_916_STUDIO",
        # Victoria 2026-09-06 (Cut Room Q02): v1. 36.96 s covers the 30 s picture.
        bed=("LakeComingDown_v1", os.path.expanduser(
            "~/drawdown-2026-campaign/06_Media_Build/audio/suno/02_LakeComingDown_v1.mp3")),
        # Victoria 2026-09-06: "this one is just like We Work the Bed now, isn't it?"
        # She was right — both opened on clip 015 and both said SCRAPE/HAUL/COVER.
        # Split the jobs: Work the Bed owns the VERBS, this one owns the CALENDAR.
        # Different opener, no verb beat, and it closes on the window, not the method.
        beats=[
            ("clip", "008", 100.0, 5.6, [("OCT 12.", 110, CREAM), ("THE LAKE STARTS DOWN.", 52, CREAM)]),
            # Victoria 2026-09-06: the recognisable residence (clip 009 t=30) is
            # swapped out. 018 t=8 is a cove edge with a weed mat and no house.
            ("clip", "018", 8.0, 5.6, [("ABOUT 10 FEET.", 84, CREAM), ("A FOOT A DAY · LCRA", 40, COPPER)]),
            ("clip", "014", 15.0, 5.6, [("NOBODY'S SEEN THIS", 62, CREAM), ("SINCE 2017.", 92, CREAM)]),
            # 011 t=40 put a recognisable lakefront house back in frame — the same
            # thing Victoria pulled out of beat 1. 014 t=60 is open creek and weed.
            ("clip", "014", 60.0, 5.6, [("YOU GET SEVEN WEEKS.", 66, CREAM), ("NOV 24 IT STARTS REFILLING", 34, COPPER)]),
            # C4 in the claim ledger is hedged at source and the hedge is mandatory.
            ("clip", "021", 10.0, 5.6, [("THE NEXT WINDOW", 70, CREAM), ("MAY BE EIGHT TO TEN", 56, CREAM), ("YEARS AWAY.", 70, CREAM)]),
            ("card", "008", 100.0, 3.75, [("BOOK THE WINDOW.", 76, CREAM), ("TEXT TRUXOR", 62, COPPER), ("254-780-6971", 62, COPPER)]),
        ]),
    # Victoria + Nate, sit-down 2026-09-06: "the bulkhead video is great — copy and
    # photos telling a story. Leverage that framework against the first video."
    # Same four real plates as the method cut, re-strapped: hook → the machines →
    # the job → the promise. Two amphibious machines said out loud (C7 plate).
    "method-v2": dict(
        out_name="DRAWDOWN_Method_916_STUDIO_v2",
        bed=("MudWindow_v2", os.path.expanduser(
            "~/drawdown-2026-campaign/06_Media_Build/audio/suno/01_MudWindow_v2.mp3")),
        beats=[
            ("still", "870b907f2401", 0, 4.35, [("SEE THAT?", 92, CREAM), ("THAT'S UNDER YOUR DOCK.", 62, CREAM), ("HYDRILLA · LAKE AUSTIN", 32, COPPER)]),
            ("still", "c6b6853c038a", 0, 4.35, [("TWO AMPHIBIOUS MACHINES.", 66, CREAM), ("BUILT TO CUT IT.", 84, CREAM), ("THEY WORK WHERE TRUCKS CAN'T", 32, COPPER)]),
            ("still", "83f97f1642cd", 0, 4.35, [("SCRAPE IT.", 84, CREAM), ("HAUL IT OFF YOUR LOT.", 62, CREAM), ("MUCK · HYDRILLA · DEBRIS — GONE", 32, COPPER)]),
            ("still", "247ed525d59d", 0, 3.0, [("COVER IT.", 84, CREAM), ("IT DOESN'T GROW BACK THROUGH.", 50, CREAM), ("TEXT TRUXOR · 254-780-6971", 36, COPPER)]),
        ]),
    # Victoria 2026-09-06 sit-down: singer = Country take A, "starting at 28 seconds".
    # Music-led reel: the song carries it, straps stay short and match the lyric.
    "work-the-bed": dict(
        out_name="DRAWDOWN_WorkTheBed_916_STUDIO",
        bed=("CountryA_from28s", os.path.expanduser(
            "~/drawdown-2026-campaign/06_Media_Build/audio/suno/03_WorkTheBed_COUNTRY_v1.mp3"), 28.0),
        beats=[
            ("clip", "015", 3.0, 5.6, [("LAKE AUSTIN", 96, CREAM), ("IS HOME.", 96, CREAM)]),
            ("still", "c6b6853c038a", 0, 5.6, [("TWO AMPHIBIOUS", 78, CREAM), ("MACHINES.", 96, CREAM)]),
            ("still", "ad415a4dd4ce", 0, 5.6, [("SCRAPE IT.", 110, CREAM)]),
            ("still", "c30cdc0fe978", 0, 5.6, [("HAUL IT.", 110, CREAM)]),
            ("still", "247ed525d59d", 0, 5.6, [("COVER IT.", 110, CREAM)]),
            ("card", "015", 5.0, 3.75, [("WE WORK THE BED.", 76, CREAM), ("TEXT TRUXOR", 60, COPPER), ("254-780-6971", 60, COPPER)]),
        ]),
    "bulkhead": dict(
        out_name="DRAWDOWN_Bulkhead_916_STUDIO",
        bed=None,
        beats=[
            ("still", "4f8cf6f78230", 0, 4.35, [("WHAT THE WATER", 84, CREAM), ("HIDES.", 84, CREAM), ("LAKE AUSTIN · LOW WATER", 32, COPPER)]),
            ("still", "f2d734030d78", 0, 4.35, [("YOUR WALL.", 84, CREAM), ("YOUR FOOTINGS.", 84, CREAM), ("YOU'LL SEE THEM OCT 12", 32, COPPER)]),
            ("still", "7b73d148d588", 0, 4.35, [("FIXED ON", 84, CREAM), ("DRY GROUND.", 84, CREAM), ("WHILE THE LAKE IS DOWN", 32, COPPER)]),
            ("card", "015", 5.0, 3.0, [("TEXT TRUXOR", 84, CREAM), ("254-780-6971", 72, COPPER)]),
        ]),
}

if __name__ == "__main__":
    slug = sys.argv[1]
    c = CUTS[slug]
    build(slug, c["out_name"], c["beats"], c["bed"])
