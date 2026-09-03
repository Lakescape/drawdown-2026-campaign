"""Drawdown hero from REAL drone motion + one verified Truxor plate. Silent.

Rule 11 (LOCKED 2026-07-28): specialty equipment cannot be text-generated.
Everything here is real capture. NOTHING from ~/Poseidon/gen-dataset/ or any
ai-generated/ dir — those carry .prompt.txt siblings and are model output.

SOURCE AUDIT 2026-09-01. Nate asked for "action videos of the Truxors rolling."
25 real DJI clips exist (~/Downloads, captured 2026-08-11 and 08-18, never
ingested). They show Lake Austin shorelines, boathouses, weed mats and low
water. They show ZERO machines and zero crew. So the machine beat stays a
verified STILL with a camera move over it; motion is used only where real
motion exists. When machine footage gets shot, beat 3 swaps to a clip.

TWO DECLARED DEVIATIONS:
1. The DJI files are DJI Fly *cache proxies* — 1280x720 landscape, not the
   originals still on the card. A 9:16 centre crop is 405x720, which would need
   a 2.67x upscale to reach a 1080x1920 hero. Refused. Instead the frame is
   letterboxed over a blurred cover-fill (compose.py "fit" precedent) so the
   subject is never upscaled. Pull the originals and this gets sharper for free.
2. Beats 1 and 4 are DIFFERENT COVES. They are NOT captioned as a before/after
   pair — that would fabricate a transformation nobody filmed. Beat 4 carries
   the work ("SCRAPE. HAUL. STAPLE."), never a results claim.

COPY RULINGS: "STAPLE" is correct and stays — the corpus documents the actual
operation, "staple woven tarp 12 IN overlap"; "seal" appears zero times as a
service. "WEED ANNIHILATORS" per Nate 2026-09-01, replacing "Truxors".
"""
import re
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

OUT = Path(__file__).resolve().parent
# Canonical home since 2026-09-01. Was ~/Downloads, where these sat unfiled for
# three weeks. See PROVENANCE.md there: proxies are master-of-record (card wiped),
# zone set by Nate not GPS, drone-wide is the default not a classification.
AERIALS = (Path.home() / "ATX-Jobs/06_Drawdown_Sales_Engine/00-source/aerials"
           / "2026-08-11-drawdown-scouting")
PHOTOS = Path.home() / "Poseidon/visual-library/photos"
W, H, FPS = 1080, 1920, 30
CREAM, INK, COPPER = (244, 239, 230), (15, 15, 35), (232, 176, 112)
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

BEFORE = AERIALS / "2026-08-11_la-rob-roy_drawdown-scouting_drone-wide_015.mp4"
OPEN = AERIALS / "2026-08-11_la-rob-roy_drawdown-scouting_drone-wide_011.mp4"
MACHINE_SHA = "c6b6853c038a87b18338b0a6fd0c94a377f84947475caa53cbab3da44d1cff83"

# carried forward from build_leadin_registry.py — a count word may only ride a
# plate that was eyeballed and actually shows two machines
C7_TWO_MACHINE_SHAS = {
    MACHINE_SHA,
    "fd49bf6ffe3ed6cf079ec16f333c149cf0cb3372ab684cf9d1a11e80ddf3c8c9",
}
# A count word may only ride a plate eyeballed as showing two machines.
# Word-boundary matched: a naive "2 " substring also fires on "10-12 FT",
# which blocked legitimate hedged copy on 2026-09-01.
COUNT_RE = re.compile(r"\b(TWO|BOTH|PAIR|2)\b")

# (kind, source, in_point, seconds, headline, subline, sub_color)
BEATS = [
    ("clip", BEFORE, 6.0, 3.4, "THIS IS UNDER", "YOUR DOCK.", None),
    # "LAKE AUSTIN, THIS FALL" asserted a season. This commit's own rule says
    # "DATES — still projected... nothing here asserts a date", and the new C1
    # row keeps DATES hedges mandatory. Subline now carries the announced fact
    # AND the open timing, which is where the uncertainty actually lives.
    ("clip", BEFORE, 13.0, 3.2, "PROJECTED 10–12 FT", "ANNOUNCED. NO DATE SET.", COPPER),
    ("still", MACHINE_SHA, 0, 3.2, "TWO WEED ANNIHILATORS", "COMMITTED IN JULY", COPPER),
    ("clip", OPEN, 40.0, 3.2, "SCRAPE. HAUL. STAPLE.", "LAKE AUSTIN IS OUR HOME WATER", COPPER),
    ("card", None, 0, 2.0, "$695 ASSESSMENT.", "100% CREDITED.", None),
]


def assert_c7(beats):
    for kind, src, _i, _s, head, sub, _c in beats:
        line = f"{head} {sub or ''}".upper()
        if COUNT_RE.search(line) and src not in C7_TWO_MACHINE_SHAS:
            raise SystemExit(f"C7: {head!r} claims a count over a non-verified plate")


def strap(head, sub, sub_color):
    """Viral-weight type: heavy headline, dark plate, copper sub. Static overlay."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    top = int(H * 0.55)
    for y in range(top, H):
        t = (y - top) / (H - top)
        d.line([(0, y), (W, y)], fill=(8, 14, 20, int(215 * t ** 0.7)))

    fh = ImageFont.truetype(BOLD, 78 if len(head) <= 18 else 62)
    fs = ImageFont.truetype(BOLD, 40)
    hw = d.textbbox((0, 0), head, font=fh)[2]
    sw = d.textbbox((0, 0), sub, font=fs)[2] if sub else 0
    y = int(H * 0.72)
    widest = max(hw, sw)
    plate = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(plate).rounded_rectangle(
        [(W - widest) // 2 - 46, y - 40, (W + widest) // 2 + 46, y + 150],
        radius=26, fill=(8, 14, 20, 200))
    img.alpha_composite(plate)
    d = ImageDraw.Draw(img)
    d.text(((W - hw) // 2, y), head, font=fh, fill=CREAM)
    if sub:
        d.rectangle([(W - 120) // 2, y + 96, (W + 120) // 2, y + 101], fill=COPPER)
        d.text(((W - sw) // 2, y + 114), sub, font=fs, fill=sub_color or CREAM)
    return img


def fit_916(im):
    """Letterbox over a blurred cover. NEVER upscales the subject — see deviation 1."""
    cov = ImageOps.fit(im, (W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(42))
    cov = Image.eval(cov, lambda p: int(p * 0.5))
    s = W / im.width
    fg = im.resize((W, int(im.height * s)), Image.LANCZOS)
    cov.paste(fg, (0, (H - fg.height) // 2))
    return cov.convert("RGB")


def card():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([96, 840, 96 + 180, 850], fill=COPPER)
    d.text((96, 890), "$695 ASSESSMENT.", font=ImageFont.truetype(BOLD, 66), fill=INK)
    d.text((96, 978), "100% CREDITED.", font=ImageFont.truetype(BOLD, 48), fill=INK)
    d.text((96, 1070), "254-780-6971", font=ImageFont.truetype(BOLD, 44), fill=INK)
    d.text((96, H - 130), "ATX LAKESCAPES", font=ImageFont.truetype(BOLD, 32), fill=INK)
    return img


def main():
    assert_c7(BEATS)
    tmp = OUT / "_rm"
    tmp.mkdir(exist_ok=True)
    segs = []
    for n, (kind, src, tin, secs, head, sub, sc) in enumerate(BEATS):
        sp = tmp / f"s{n}.png"
        # the paper card draws its own type; a strap would double it
        (Image.new("RGBA", (W, H), (0, 0, 0, 0)) if kind == "card"
         else strap(head, sub, sc)).save(sp)
        seg = tmp / f"seg{n}.mp4"
        if kind == "clip":
            assert Path(src).exists(), f"missing real clip: {src}"
            base = tmp / f"b{n}.jpg"          # probe one frame to build the blur bed
            subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(tin), "-i", str(src),
                            "-frames:v", "1", str(base)], check=True)
            # Blurred cover bed, same as the still path. Padding to black left the
            # 720p source as a strip floating on black — unusable for social.
            fc = (f"[0:v]split=2[bg][fg];"
                  f"[bg]scale={W}:{H}:force_original_aspect_ratio=increase,"
                  f"crop={W}:{H},boxblur=42:1,eq=brightness=-0.18[bgb];"
                  f"[fg]scale={W}:-2[fgs];"
                  f"[bgb][fgs]overlay=(W-w)/2:(H-h)/2,fps={FPS}[base];"
                  f"[base][1:v]overlay=0:0,format=yuv420p[v]")
            subprocess.run([
                "ffmpeg", "-v", "error", "-y", "-ss", str(tin), "-t", str(secs), "-i", str(src),
                "-i", str(sp), "-filter_complex", fc,
                "-map", "[v]", "-an", "-c:v", "libx264", "-crf", "18", "-preset", "slow",
                str(seg)], check=True)
        else:
            if kind == "still":
                im = ImageOps.exif_transpose(Image.open(PHOTOS / f"{src}.jpg")).convert("RGB")
                bed = fit_916(im)
            else:
                bed = card()
            bp = tmp / f"b{n}.jpg"
            bed.save(bp, quality=95)
            frames = int(secs * FPS)
            vf = (f"zoompan=z='min(1.0+0.0004*on,1.06)':d={frames}"
                  f":x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':s={W}x{H}:fps={FPS}")
            subprocess.run([
                "ffmpeg", "-v", "error", "-y", "-i", str(bp), "-i", str(sp),
                "-filter_complex", f"[0:v]{vf}[bg];[bg][1:v]overlay=0:0,format=yuv420p[v]",
                "-map", "[v]", "-t", str(secs), "-an", "-c:v", "libx264", "-crf", "18",
                "-preset", "slow", str(seg)], check=True)
        segs.append(seg)

    lst = tmp / "concat.txt"
    lst.write_text("".join(f"file '{s}'\n" for s in segs))
    dst = OUT / "DRAWDOWN_RealMotion_916_v1_DRAFT.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0",
                    "-i", str(lst), "-c:v", "libx264", "-crf", "18", "-preset", "slow",
                    "-an", "-movflags", "+faststart", str(dst)], check=True)
    print("wrote", dst.name)


if __name__ == "__main__":
    main()
