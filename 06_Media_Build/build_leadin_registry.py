"""Lead-in picture track from the unified registry. Silent. No t2v.

Pins come from `registry.py resolve --seat mac`. Bytes stay in Poseidon.
claim_ok:false plates are not used as fleet evidence.

  @bulkhead_undercut  R approved claim_ok
  @two_machines       R approved — ONE excavator on a platform, NOT two.
                      Card must not claim a count. See assert_c7().
  @farshore_golden    R approved claim_ok

Not used: @dock_lowwater (mythology), spliced 77s VO (does not ship).
"""
from __future__ import annotations

import os
import re
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent
W, H, FPS = 1080, 1920, 24
CREAM = (244, 239, 230)
INK = (15, 15, 35)
COPPER = (232, 176, 112)
BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

# Full sha from registry resolve 2026-08-31 — a prefix is not a pin
PLATES = [
    (
        "@hydrilla_cove_carpet",
        "4e23ecccd59fef3d1ab765cafe811662a91d9dab1705f13c9b0797cf3eac6570",
        5.0,
        "10 YEARS HID THIS",
    ),
    (
        "@two_machines",
        "1334bce67b99a938b4331157a242a2ddf57235faa636f411ffd8ca37643ec874",
        5.0,
        # WAS "TWO AMPHIBIOUS MACHINES" — sha 1334bce6 shows ONE excavator on a
        # floating platform. Nate's 2026-08-14 ruling stands on machine CLASS
        # ("the platform is what C7 actually claims"); it does not license the
        # COUNT. C7 requires "must show 2". This line says only what the frame
        # carries. Shipped to the desk once as a false claim — see
        # drawdown-2026-campaign@073e0d3.
        "AMPHIBIOUS PLATFORM",
    ),
    (
        "@farshore_golden",
        "5f82b8e9583becd31b381c1f8dbd8306d688bc1ff24222e398a64a6dce20488e",
        4.0,
        "LAKE AUSTIN — HOME WATER",
    ),
]
PHOTOS = Path.home() / "Poseidon/visual-library/photos"

# Only these plates were eyeballed and actually show two amphibious machines
# with pontoon undercarriage. A card may claim a count ONLY over one of them.
C7_TWO_MACHINE_SHAS = {
    "c6b6853c038a87b18338b0a6fd0c94a377f84947475caa53cbab3da44d1cff83",
    "fd49bf6ffe3ed6cf079ec16f333c149cf0cb3372ab684cf9d1a11e80ddf3c8c9",
}
# A count word may only ride a plate eyeballed as showing two machines.
# Word-boundary matched: a naive "2 " substring also fires on "10-12 FT",
# which blocked legitimate hedged copy on 2026-09-01.
COUNT_RE = re.compile(r"\b(TWO|BOTH|PAIR|2)\b")


def assert_c7(plates) -> None:
    """A count word on a plate that cannot carry it is the C7 defect. Twice now."""
    for tag, sha, _secs, line in plates:
        if COUNT_RE.search(line.upper()) and sha not in C7_TWO_MACHINE_SHAS:
            raise SystemExit(
                f"C7: {tag} card {line!r} claims a count, but {sha[:12]} is not a "
                "verified two-machine plate. Use one of C7_TWO_MACHINE_SHAS or "
                "drop the count from the card."
            )


def cover(im: Image.Image, w: int, h: int, bias: str = "center") -> Image.Image:
    s = max(w / im.width, h / im.height) * 1.08
    im = im.resize((int(im.width * s) + 1, int(im.height * s) + 1), Image.LANCZOS)
    left = (im.width - w) // 2
    if bias == "bottom":
        top = im.height - h
    else:
        top = (im.height - h) // 2
    top = max(0, min(top, im.height - h))
    return im.crop((left, top, left + w, top + h))


def overlay(text: str) -> Image.Image:
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    top = int(H * 0.58)
    for y in range(top, H):
        t = (y - top) / (H - top)
        d.line([(0, y), (W, y)], fill=(10, 18, 24, int(210 * t ** 0.75)))
    font = ImageFont.truetype(BOLD, 48)
    bbox = d.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    d.text(((W - tw) // 2, int(H * 0.78)), text, font=font, fill=CREAM)
    return img


def paper_card() -> Image.Image:
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    d.rectangle([96, 820, 96 + 168, 828], fill=COPPER)
    f1 = ImageFont.truetype(BOLD, 58)
    f2 = ImageFont.truetype(BOLD, 44)
    d.text((96, 860), "$695 ASSESSMENT.", font=f1, fill=INK)
    d.text((96, 940), "100% CREDITED.", font=f2, fill=INK)
    return img


def main() -> None:
    tmp = OUT / "_leadin_reg_frames"
    tmp.mkdir(exist_ok=True)
    assert_c7(PLATES)
    frames: list[Path] = []
    n = 0
    for tag, sha, secs, line in PLATES:
        src = PHOTOS / f"{sha}.jpg"
        if not src.exists():
            raise SystemExit(f"missing Poseidon bytes for {tag}: {src}")
        bias = "bottom" if tag == "@hydrilla_cove_carpet" else "center"
        plate = cover(Image.open(src).convert("RGB"), W, H, bias=bias).convert("RGBA")
        card = overlay(line)
        still = Image.alpha_composite(plate, card).convert("RGB")
        count = int(secs * FPS)
        for i in range(count):
            # slow push ~6%
            z = 1.0 + 0.06 * (i / max(count - 1, 1))
            cw, ch = int(W / z), int(H / z)
            x = (W - cw) // 2
            y = (H - ch) // 2
            fr = still.crop((x, y, x + cw, y + ch)).resize((W, H), Image.LANCZOS)
            p = tmp / f"{n:05d}.jpg"
            fr.save(p, quality=92)
            frames.append(p)
            n += 1
    card = paper_card()
    for i in range(int(2.0 * FPS)):
        p = tmp / f"{n:05d}.jpg"
        card.save(p, quality=92)
        n += 1
    dest = OUT / "DRAWDOWN_LeadIn_916_v4_REGISTRY_SILENT.mp4"
    subprocess.check_call(
        [
            "ffmpeg", "-y", "-framerate", str(FPS),
            "-i", str(tmp / "%05d.jpg"),
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18",
            "-movflags", "+faststart", str(dest),
        ]
    )
    print(f"wrote {dest} frames={n} tags={[t for t, *_ in PLATES]}")


if __name__ == "__main__":
    main()
