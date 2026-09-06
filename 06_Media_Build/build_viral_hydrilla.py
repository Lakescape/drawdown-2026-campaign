"""Viral hydrilla-horror 15s. Registry plates. No $695. Silent straps first."""
from __future__ import annotations

import os
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

OUT = Path(__file__).resolve().parent
PHOTOS = Path.home() / "Poseidon/visual-library/photos"
W, H, FPS = 1080, 1920, 24
CREAM = (244, 239, 230)
INK = (15, 15, 35)
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

# (tag, sha, secs, mode, [strap lines])
# mode cover-bottom | cover-center | fit (letterbox — keep TWO Truxors in frame)
BEATS = [
    (
        "@hydrilla_cove_carpet",
        "4e23ecccd59fef3d1ab765cafe811662a91d9dab1705f13c9b0797cf3eac6570",
        3.0,
        "cover-bottom",
        ["THIS IS UNDER", "YOUR DOCK."],
    ),
    (
        "@hydrilla_underwater",
        "924c9e39682b244ced6fb2cea57ab18a8f81c95cf7a3ea2af904ff2d944206cc",
        4.0,
        "cover-center",
        ["TEN YEARS.", "YOU'VE NEVER SEEN IT."],
    ),
    (
        "@truxors_pair_working",
        "c6b6853c038a87b18338b0a6fd0c94a377f84947475caa53cbab3da44d1cff83",
        4.0,
        "fit",
        ["TWO TRUXORS.", "PROJECTED 10–12 FT."],
    ),
    (
        "@farshore_golden",
        "5f82b8e9583becd31b381c1f8dbd8306d688bc1ff24222e398a64a6dce20488e",
        4.0,
        "cover-center",
        # Nate 2026-09-04: COVER campaign-wide — the verb we can photograph.
        ["SCRAPE. HAUL. COVER.", "254-780-6971"],
    ),
]


def cover(im: Image.Image, w: int, h: int, bias: str) -> Image.Image:
    s = max(w / im.width, h / im.height) * 1.10
    im = im.resize((int(im.width * s) + 1, int(im.height * s) + 1), Image.LANCZOS)
    left = (im.width - w) // 2
    top = im.height - h if bias == "bottom" else (im.height - h) // 2
    top = max(0, min(top, im.height - h))
    return im.crop((left, top, left + w, top + h))


def fit(im: Image.Image, w: int, h: int) -> Image.Image:
    """Letterbox over a blurred cover so both machines stay in frame."""
    bg = cover(im, w, h, "center").filter(ImageFilter.GaussianBlur(28))
    bg = ImageEnhance_dark(bg)
    s = min(w / im.width, h / im.height)
    nw, nh = int(im.width * s), int(im.height * s)
    fg = im.resize((nw, nh), Image.LANCZOS)
    bg.paste(fg, ((w - nw) // 2, (h - nh) // 2))
    return bg


def ImageEnhance_dark(im: Image.Image) -> Image.Image:
    from PIL import ImageEnhance
    return ImageEnhance.Brightness(im).enhance(0.45)


def strap(lines: list[str]) -> Image.Image:
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    top = int(H * 0.50)
    for y in range(top, H):
        t = (y - top) / (H - top)
        d.line([(0, y), (W, y)], fill=(8, 12, 16, int(230 * t ** 0.7)))
    font = ImageFont.truetype(BOLD, 64)
    sizes = []
    for t in lines:
        bb = d.textbbox((0, 0), t, font=font)
        sizes.append((t, bb[2] - bb[0], bb[3] - bb[1]))
    gap = 16
    total = sum(h for _, _, h in sizes) + gap * (len(sizes) - 1)
    y = int(H * 0.72) - total // 2
    for t, tw, th in sizes:
        d.text(((W - tw) // 2, y), t, font=font, fill=CREAM)
        y += th + gap
    return img


def main() -> None:
    tmp = OUT / "_viral_frames"
    tmp.mkdir(exist_ok=True)
    n = 0
    for tag, sha, secs, mode, lines in BEATS:
        src = PHOTOS / f"{sha}.jpg"
        if not src.exists():
            raise SystemExit(f"missing {tag} {src}")
        rgb = Image.open(src).convert("RGB")
        if mode == "fit":
            plate = fit(rgb, W, H).convert("RGBA")
        elif mode == "cover-bottom":
            plate = cover(rgb, W, H, "bottom").convert("RGBA")
        else:
            plate = cover(rgb, W, H, "center").convert("RGBA")
        still = Image.alpha_composite(plate, strap(lines)).convert("RGB")
        count = int(secs * FPS)
        for i in range(count):
            z = 1.0 + 0.07 * (i / max(count - 1, 1))
            cw, ch = int(W / z), int(H / z)
            x, y = (W - cw) // 2, (H - ch) // 2
            fr = still.crop((x, y, x + cw, y + ch)).resize((W, H), Image.LANCZOS)
            fr.save(tmp / f"{n:05d}.jpg", quality=92)
            n += 1
    dest = OUT / "DRAWDOWN_ViralHydrilla_916_v1.mp4"
    subprocess.check_call(
        [
            "ffmpeg", "-y", "-framerate", str(FPS),
            "-i", str(tmp / "%05d.jpg"),
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18",
            "-movflags", "+faststart", str(dest),
        ]
    )
    print(f"wrote {dest} frames={n}")


if __name__ == "__main__":
    main()
