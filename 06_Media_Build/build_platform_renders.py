"""Slice 1 tracer: one pillar master -> per-platform renders + safe-zone proof + QC sheet.

Nate 2026-09-07: "we don't have each video custom edited specifically to the platform."
This proves the per-platform path end to end and makes each platform's UI dead zones
visible on OUR frames. It does not re-lay-out straps yet (slice 2). Nothing posts.

Arch: docs/architecture/platform-native-renders-2026-09-07.md
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
MEDIA = os.path.expanduser("~/drawdown-2026-campaign/06_Media_Build")
OUT = os.path.join(HERE, "renders")
W, H = 1080, 1920

# ponytail: safe-zone pixels come from 2026 third-party guides, not platform-published
# specs. fb-reels and gbp rows are UNVERIFIED. The proof PNG is the real check —
# Nate eyeballs it on a phone. Re-audit per campaign (Gary V "PAC" chart).
#            top  bottom left right max_s lufs cover_s  source
PLATFORMS = {
    "ig-reels": (130, 400, 60, 140, 90, -14.0, 0.0, "guides 2026"),
    "tiktok":   (140, 484, 60, 180, 60, -14.0, 0.0, "guides 2026"),
    "fb-reels": (130, 400, 60, 140, 90, -14.0, 0.0, "UNVERIFIED assumed = IG"),
    "gbp":      (100, 100, 60,  60, 30, -14.0, 1.0, "UNVERIFIED no UI overlay documented"),
}


def sh(*args):
    return subprocess.run(args, check=True, capture_output=True, text=True)


def probe(path):
    j = json.loads(sh("ffprobe", "-v", "error", "-print_format", "json",
                      "-show_streams", "-show_format", path).stdout)
    v = next(s for s in j["streams"] if s["codec_type"] == "video")
    n, d = v["r_frame_rate"].split("/")
    return dict(duration=float(j["format"]["duration"]), w=int(v["width"]),
                h=int(v["height"]), fps=round(int(n) / int(d), 3),
                audio=any(s["codec_type"] == "audio" for s in j["streams"]))


def lufs(path, target):
    """loudnorm pass 1: returns measured input stats as a dict."""
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", path, "-af",
                        f"loudnorm=I={target}:TP=-1.5:LRA=11:print_format=json",
                        "-f", "null", "-"], capture_output=True, text=True)
    s = r.stderr
    return json.loads(s[s.rfind("{"):s.rfind("}") + 1])


def render(src, dst, spec, m):
    top, bottom, left, right, max_s, target, _, _ = spec
    af = (f"loudnorm=I={target}:TP=-1.5:LRA=11:measured_I={m['input_i']}:"
          f"measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}:"
          f"measured_thresh={m['input_thresh']}:linear=true")
    sh("ffmpeg", "-y", "-hide_banner", "-i", src, "-t", str(max_s),
       "-vf", f"scale={W}:{H}:flags=lanczos,fps=30,format=yuv420p",
       "-af", af, "-c:v", "libx264", "-profile:v", "high", "-crf", "18",
       "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", dst)


def proof(src, dst, spec, t=5.0):
    top, bottom, left, right = spec[:4]
    boxes = [f"drawbox=0:0:{W}:{top}:red@0.45:fill",
             f"drawbox=0:{H - bottom}:{W}:{bottom}:red@0.45:fill",
             f"drawbox=0:0:{left}:{H}:red@0.45:fill",
             f"drawbox={W - right}:0:{right}:{H}:red@0.45:fill",
             f"drawbox={left}:{top}:{W - left - right}:{H - top - bottom}:green@1:6"]
    sh("ffmpeg", "-y", "-hide_banner", "-ss", str(t), "-i", src, "-frames:v", "1",
       "-vf", ",".join(boxes), dst)


def cover(src, dst, t):
    sh("ffmpeg", "-y", "-hide_banner", "-ss", str(t), "-i", src, "-frames:v", "1", "-q:v", "2", dst)


def build(piece):
    src = os.path.join(MEDIA, piece)
    if not os.path.exists(src):
        sys.exit(f"MISSING master: {src}")
    name = os.path.splitext(piece)[0]
    base = os.path.join(OUT, name)
    os.makedirs(base, exist_ok=True)
    src_meta = probe(src)
    rows = []
    for plat, spec in PLATFORMS.items():
        d = os.path.join(base, plat)
        os.makedirs(d, exist_ok=True)
        top, bottom, left, right, max_s, target, cover_s, source = spec
        m = lufs(src, target)
        render(src, os.path.join(d, "render.mp4"), spec, m)
        proof(src, os.path.join(d, "safezone_proof.png"), spec)
        # CTA beat: the strap most likely to sit under the caption block lives at the end
        proof(src, os.path.join(d, "safezone_proof_cta.png"), spec, t=max(0.0, src_meta["duration"] - 2.0))
        cover(src, os.path.join(d, "cover.jpg"), cover_s)
        out = probe(os.path.join(d, "render.mp4"))
        out_lufs = float(lufs(os.path.join(d, "render.mp4"), target)["input_i"])
        checks = {
            "res_1080x1920": (out["w"], out["h"]) == (W, H),
            "fps_30": abs(out["fps"] - 30) < 0.01,
            "duration_le_max": out["duration"] <= max_s + 0.05,
            "lufs_within_1": abs(out_lufs - target) <= 1.0,
            "audio_present": out["audio"],
        }
        qc = dict(platform=plat, source=source, safe_zone=dict(top=top, bottom=bottom, left=left, right=right),
                  max_s=max_s, target_lufs=target, out_lufs=round(out_lufs, 2),
                  duration=round(out["duration"], 3), trimmed=src_meta["duration"] > max_s + 0.05,
                  checks=checks, PASS=all(checks.values()))
        json.dump(qc, open(os.path.join(d, "qc.json"), "w"), indent=2)
        rows.append(qc)
    md = [f"# QC sheet — {piece}", "",
          f"Source: `{src}` · {src_meta['duration']:.3f}s · {src_meta['w']}x{src_meta['h']} · {src_meta['fps']} fps",
          "", "Slice 1 tracer. Measurable checks only. **Straps are not re-laid-out yet** — open each",
          "`safezone_proof.png`: red = platform UI dead zone, green box = safe. Anything red-over-text fails the human check.",
          "**Nothing here posts.** Routing Gate (ATX-1748) must log PASS before any of it ships.", "",
          "| Platform | Safe zone T/B/L/R | Max s | Out s | Out LUFS | Checks | Verdict | Proof (5 s / CTA beat) |",
          "|---|---|---|---|---|---|---|---|"]
    for q in rows:
        z = q["safe_zone"]
        failed = [k for k, v in q["checks"].items() if not v]
        md.append(f"| {q['platform']} | {z['top']}/{z['bottom']}/{z['left']}/{z['right']} ({q['source']}) | {q['max_s']} | "
                  f"{q['duration']} | {q['out_lufs']} | {'all ok' if not failed else ', '.join(failed)} | "
                  f"{'PASS' if q['PASS'] else 'FAIL'} | `{q['platform']}/safezone_proof.png` / `safezone_proof_cta.png` |")
    open(os.path.join(base, "QC_SHEET.md"), "w").write("\n".join(md) + "\n")
    for q in rows:
        print(f"{'PASS' if q['PASS'] else 'FAIL'}  {q['platform']:9s} {q['duration']:6.2f}s  {q['out_lufs']:6.2f} LUFS  {q['source']}")
    print("sheet:", os.path.join(base, "QC_SHEET.md"))
    return rows


if __name__ == "__main__":
    pieces = sys.argv[1:] or ["DRAWDOWN_LakeComingDown_916_SUNO_BED.mp4"]
    for p in pieces:
        rows = build(p)
        # self-check: the tracer is only "done" if every artifact exists and the math held
        base = os.path.join(OUT, os.path.splitext(p)[0])
        for q in rows:
            for f in ("render.mp4", "safezone_proof.png", "safezone_proof_cta.png", "cover.jpg", "qc.json"):
                assert os.path.getsize(os.path.join(base, q["platform"], f)) > 0, (q["platform"], f)
            assert q["duration"] <= q["max_s"] + 0.05, q
        assert os.path.exists(os.path.join(base, "QC_SHEET.md"))
