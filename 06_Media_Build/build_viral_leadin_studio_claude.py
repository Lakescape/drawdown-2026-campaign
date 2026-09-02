"""Viral hydrilla lead-in — 15.0s, 9:16, SILENT master. Claude studio pass.

⚠️  FILENAME COLLISION 2026-08-31 20:34: a second writer created
    `build_viral_leadin_studio.py` and overwrote
    `DRAWDOWN_ViralHydrilla_916_STUDIO.mp4` mid-session. Both preserved under
    `archive/*_OTHERAGENT_2026-08-31T2034.*`. This file is the Claude build and
    owns its own name so the two lanes stop fighting. Master filename stays as
    the kickoff specified.

Craft rules carried over from compose.py (the 77s Truxor cut):

  * Composite the picture at 1350x2400 so the Ken Burns move always DOWNSCALES
    into 1080x1920. Never upscale a Jobber-ceiling 1080x810 phone photo to fake
    a push.
  * "bleed" = cover-crop to 9:16. "fit" = letterbox over a blurred, darkened
    cover of itself, used ONLY where a side crop could push a machine out of
    frame and break the two-machine count in C7. Claim safety beats framing.
  * The strap does NOT ride the Ken Burns move. Picture moves, type is locked
    and rendered native at 1080x1920 so it is never resampled. Baking type into
    the plate and zooming it is the tell of a one-liner.

Every plate is a real Poseidon still, sha-pinned, caption-audited and eyeballed
on this Mac. No i2v, no t2v — HIGGSFIELD-LEARNINGS Rule 11: specialty equipment
is shot, never generated.

EXCLUDED: @two_machines (1334bce67b99). Caption + eyeball both confirm a single
yellow knuckleboom excavator on a floating barge. One machine, no amphibious
undercarriage. Hard C7 fail.

Claim ledger bindings (../MEDIA_ClaimLedger_Drawdown_v1.md):
  beat 2 -> C3   ten-year window, no hedge required
  beat 3 -> C7   two amphibious machines — must SHOW two, and show the
                 undercarriage. FIT mode exists for this line and only this line.
           C2   "PROJECTED" 10–12 ft retained verbatim
           C1   drawdown is exploratory -> hedged on the same plate, not an
                end card ("NOTHING IS OFFICIAL YET")
  beat 4 -> C11  must read as Lake Austin

Stripped per Nate 2026-08-31: $695, credited, assessment, "walk yours",
"I'll tell you to your face". This is a lead-in, not a Priority Assessment ad.
"""
from __future__ import annotations

import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

OUT = Path(__file__).resolve().parent
PHOTOS = Path.home() / "Poseidon/visual-library/photos"
FRAMES = OUT / "_studio_frames_claude"
MASTER = OUT / "DRAWDOWN_ViralHydrilla_916_STUDIO_CLAUDE.mp4"

W, H = 1080, 1920          # delivery
CW, CH = 1350, 2400        # composite — 1.25x delivery, headroom for the move
FPS = 30
XFADE = 10                 # frames of dissolve between beats (0.33s)

BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
CREAM = (244, 239, 230)
COPPER = (232, 176, 112)

# grade = (brightness, contrast, saturation) — phone stills off Jobber run flat
# and dark under water. Lift, do not stylise.
BEATS = [
    dict(
        tag="@hydrilla_under_dock",
        sha="f730acf1ac49dae940dcd30e7597b1caa554d6d60fbd1a4b1531b5eb99d069ef",
        secs=3.40, mode="bleed", bias=(0.50, 0.52), zoom=(1.000, 1.075),
        grade=(1.26, 1.14, 1.18), pan=None,
        lines=[("THIS IS UNDER", 104, CREAM), ("YOUR DOCK.", 104, CREAM)],
        note="dock rail + fender, POV straight down into a full hydrilla bed",
    ),
    dict(
        tag="@hydrilla_submerged_bed",
        sha="924c9e39682b244ced6fb2cea57ab18a8f81c95cf7a3ea2af904ff2d944206cc",
        secs=4.20, mode="bleed", bias=(0.56, 0.55), zoom=(1.090, 1.000),
        grade=(1.03, 1.06, 1.08), pan=None,
        lines=[("TEN YEARS.", 92, CREAM), ("YOU'VE NEVER SEEN IT.", 62, CREAM)],
        note="clear water over a submerged mound — C3, the thing you can't see",
    ),
    dict(
        tag="@truxors_pair_working",
        sha="c6b6853c038a87b18338b0a6fd0c94a377f84947475caa53cbab3da44d1cff83",
        # FIT + 4:5 pre-crop. The 1080x810 native has ~30% dead sky; cropping to
        # 4:5 (verified by eye: BOTH machines still in frame with margin) lets
        # the plate fill 70% of canvas height instead of 37%. Zoom is pinned at
        # 1.000 so nothing can walk out of frame — the move is a vertical pan
        # inside the letterbox slack, which cannot touch the count.
        secs=4.20, mode="fit", bias=(0.50, 0.50), zoom=(1.000, 1.000),
        grade=(1.02, 1.05, 1.06), pan=(0.355, 0.425),
        lines=[("TWO TRUXORS.", 88, CREAM),
               ("PROJECTED 10–12 FT.", 58, CREAM),
               ("NOTHING IS OFFICIAL YET", 38, COPPER)],
        note="C7 count — one cutting, one at the bank, pontoon decks visible",
    ),
    dict(
        tag="@truxor_hauled_windrow",
        sha="cd351a221a006e2ad2efe8a172cdb45ac3a541fb67076f81705805b27dd552d2",
        # bias left of centre so the hauled windrow stays in frame with the
        # machine — a centred crop kept the Truxor and threw away the proof.
        secs=4.20, mode="bleed", bias=(0.28, 0.52), zoom=(1.020, 1.085),
        grade=(1.08, 1.07, 1.06), pan=None,
        # A bare number is a dead CTA: QUO_SMS_KEYWORD_ONLY is live, so an
        # unmatched SMS logs "not ingesting" and creates NO lead. The keyword is
        # TRUXOR, not DOCK — keyword-routing-test.md:148 records that DOCK maps
        # to L2 dock-repair (smsKeywordMatch.ts serviceHint), which would route a
        # hydrilla lead to the wrong service line.
        lines=[("SCRAPE. HAUL. STAPLE.", 72, CREAM),
               ("LAKE AUSTIN IS OUR HOME WATER", 34, COPPER),
               ("TEXT TRUXOR TO 254-780-6971", 56, CREAM)],
        note="machine + the windrow it hauled out — the work, on our water (C11)",
    ),
]

FIT_AR = 0.80              # 4:5 pre-crop for the count plate
FIT_WIDTH = 1.00           # of canvas — safe because zoom is pinned at 1.000


def grade(im: Image.Image, g: tuple[float, float, float]) -> Image.Image:
    b, c, s = g
    im = ImageEnhance.Brightness(im).enhance(b)
    im = ImageEnhance.Contrast(im).enhance(c)
    return ImageEnhance.Color(im).enhance(s)


def cover(im: Image.Image, w: int, h: int, bias: tuple[float, float]) -> Image.Image:
    sc = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
    x = int((im.width - w) * bias[0])
    y = int((im.height - h) * bias[1])
    return im.crop((x, y, x + w, y + h))


def crop_ar(im: Image.Image, ar: float) -> Image.Image:
    w, h = im.size
    nw, nh = (int(h * ar), h) if w / h > ar else (w, int(w / ar))
    return im.crop(((w - nw) // 2, (h - nh) // 2, (w - nw) // 2 + nw, (h - nh) // 2 + nh))


def plate(beat: dict) -> tuple[Image.Image, int]:
    """Return the 1350x2400 composite and the foreground height (0 if bleed)."""
    src = PHOTOS / f"{beat['sha']}.jpg"
    if not src.exists():
        raise SystemExit(f"missing plate {beat['tag']} {src}")
    im = grade(ImageOps.exif_transpose(Image.open(src)).convert("RGB"), beat["grade"])

    if beat["mode"] == "bleed":
        return cover(im, CW, CH, beat["bias"]), 0

    fgsrc = crop_ar(im, FIT_AR)
    bg = ImageEnhance.Brightness(
        cover(im, CW, CH, (0.5, 0.5)).filter(ImageFilter.GaussianBlur(34))
    ).enhance(0.40)
    fw = int(CW * FIT_WIDTH)
    fg = fgsrc.resize((fw, round(fgsrc.height * fw / fgsrc.width)), Image.LANCZOS)
    return (bg, fg.height), fg  # placed per-frame so the pan can move it


def strap(lines) -> Image.Image:
    """Fixed-size 1080x1920 overlay: bottom scrim + plate + type. Never zooms."""
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    top = int(H * 0.46)
    for y in range(top, H):
        t = (y - top) / (H - top)
        d.line([(0, y), (W, y)], fill=(8, 14, 20, int(232 * t ** 0.72)))

    rendered = []
    for text, size, colour in lines:
        f = ImageFont.truetype(BOLD, size)
        while d.textbbox((0, 0), text, font=f)[2] > W - 130 and size > 22:
            size -= 2
            f = ImageFont.truetype(BOLD, size)
        bb = d.textbbox((0, 0), text, font=f)
        rendered.append((text, f, colour, bb[2], bb[3]))

    gap = 22
    total = sum(r[4] for r in rendered) + gap * (len(rendered) - 1)
    y = int(H * 0.775) - total // 2
    widest = max(r[3] for r in rendered)

    pl = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    ImageDraw.Draw(pl).rounded_rectangle(
        [(W - widest) // 2 - 46, y - 34, (W + widest) // 2 + 46, y + total + 34],
        radius=20, fill=(8, 14, 20, 150))
    img.alpha_composite(pl)

    d = ImageDraw.Draw(img)
    for text, f, colour, tw, th in rendered:
        x = (W - tw) // 2
        d.text((x + 3, y + 3), text, font=f, fill=(0, 0, 0, 180))
        d.text((x, y), text, font=f, fill=colour)
        y += th + gap
    return img


def kenburns(pic: Image.Image, z: float) -> Image.Image:
    cw, ch = round(CW / z), round(CH / z)
    x, y = (CW - cw) // 2, (CH - ch) // 2
    return pic.crop((x, y, x + cw, y + ch)).resize((W, H), Image.LANCZOS)


def render_beat(beat: dict) -> list[Image.Image]:
    built = plate(beat)
    if beat["mode"] == "fit":
        (bg, fgh), fg = built
    else:
        bg, fg, fgh = built[0], None, 0

    ov = strap(beat["lines"])
    n = round(beat["secs"] * FPS)
    z0, z1 = beat["zoom"]
    fade = int(FPS * 0.35)
    out = []
    for i in range(n):
        t = i / max(n - 1, 1)
        if fg is None:
            base = bg
        else:
            base = bg.copy()
            yc = beat["pan"][0] + (beat["pan"][1] - beat["pan"][0]) * t
            py = int(CH * yc) - fgh // 2
            base.paste(fg, ((CW - fg.width) // 2, py))
            ImageDraw.Draw(base).rectangle(
                [(CW - fg.width) // 2, py,
                 (CW - fg.width) // 2 + fg.width - 1, py + fgh - 1],
                outline=CREAM, width=3)
        fr = kenburns(base, z0 + (z1 - z0) * t).convert("RGBA")
        a = min(1.0, i / fade) if fade else 1.0
        layer = ov if a >= 1.0 else Image.blend(
            Image.new("RGBA", (W, H), (0, 0, 0, 0)), ov, a)
        out.append(Image.alpha_composite(fr, layer).convert("RGB"))
    return out


def main() -> None:
    FRAMES.mkdir(exist_ok=True)
    for old in FRAMES.glob("*.jpg"):
        old.unlink()

    reels = []
    for b in BEATS:
        reels.append(render_beat(b))
        print(f"  {b['tag']:26s} {b['mode']:5s} {b['secs']}s  {b['sha'][:12]}  {b['note']}")

    timeline: list[Image.Image] = list(reels[0])
    for nxt in reels[1:]:
        tail, head = timeline[-XFADE:], nxt[:XFADE]
        timeline = timeline[:-XFADE]
        for i, (a, bb) in enumerate(zip(tail, head)):
            timeline.append(Image.blend(a, bb, (i + 1) / (XFADE + 1)))
        timeline.extend(nxt[XFADE:])

    for i, fr in enumerate(timeline):
        fr.save(FRAMES / f"{i:05d}.jpg", quality=95, subsampling=0)

    subprocess.check_call([
        "ffmpeg", "-y", "-loglevel", "error",
        "-framerate", str(FPS), "-i", str(FRAMES / "%05d.jpg"),
        "-c:v", "libx264", "-preset", "slow", "-crf", "18",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(MASTER),
    ])
    print(f"\nwrote {MASTER}  frames={len(timeline)}  {len(timeline)/FPS:.2f}s  SILENT")


if __name__ == "__main__":
    main()
