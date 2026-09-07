"""Viral lead-in (Claude lane) + a two-line VO in the "MikeRow Story Teller" voice.

Victoria, sit-down board 2026-09-06 (Q02): "combo of 1 and then 3 — talking about
the drawdown's official part, simply explaining coming down 10 ft. Can use the
cloned voice, the Mike Rowe one." So: two lines, not four; the ElevenLabs voice
named "MikeRow Story Teller" (s4rOmUeb79uIbzKAm7kQ, category=generated — not a
clone of a real person); the silent Claude master stays the master and this ships
as a separate file.

Key is read at runtime from InsightEngine/.env, never written here. Renders are
gitignored with the rest of the media.
"""
import json
import os
import re
import subprocess
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
MAIN = os.path.expanduser("~/drawdown-2026-campaign/06_Media_Build")
ENV = os.path.expanduser("~/InsightEngineMacOSPRO/InsightEngine/.env")
VOICE_ID = "s4rOmUeb79uIbzKAm7kQ"          # MikeRow Story Teller
MODEL = "eleven_multilingual_v2"
SRC = os.path.join(MAIN, "DRAWDOWN_ViralHydrilla_916_STUDIO_CLAUDE.mp4")
MP3 = os.path.join(MAIN, "vo_mikerow_leadin.mp3")
DST = os.path.join(MAIN, "DRAWDOWN_ViralHydrilla_916_STUDIO_CLAUDE_VO_MikeRow.mp4")

# Two lines. Beat 1 (0–3.3 s) is the dock/hydrilla plate, beat 3 (7.65–12 s) is the
# two-Truxor plate with ABOUT 10 FT. OCT 12. on it — the second sentence lands there.
# v2 (sit-down 2026-09-06, Nate): "add two more sentences — the most informative
# thing." Took the two that are already true on the cards and in the caption:
# the machines + the job, and the ask. Held back until sourced: "licensed for
# TPWD removal", "number-one monthly maintenance weed company in Central Texas",
# "doing this for ten years" — none is in the claim ledger; see BOARD 2026-09-06.
SCRIPT = (
    "This is what's under Lake Austin docks.  "
    "The drawdown's official — about ten feet, from October twelfth.  "
    "Two amphibious machines. We scrape it, haul it off, cover it.  "
    "Text TRUXOR for a free estimate."
)
BANNED = re.compile(r"explor|unofficial|nothing is official|projected|ten to twelve|695|credit|assessment|extinct", re.I)
assert not BANNED.search(SCRIPT), "banned phrase in the read"
DELAY_MS = 500


def api_key():
    with open(ENV) as fh:
        m = re.search(r"^\s*ELEVENLABS_API_KEY\s*=\s*(.+)$", fh.read(), re.M)
    assert m, "ELEVENLABS_API_KEY not in " + ENV
    return m.group(1).strip().strip("\"'")


def tts():
    # curl, not urllib: python 3.14 on this Mac has no CA bundle wired up
    # (CERTIFICATE_VERIFY_FAILED). The key goes in via an env var, never argv.
    body = json.dumps({
        "text": SCRIPT, "model_id": MODEL,
        "voice_settings": {"stability": 0.5, "similarity_boost": 0.75, "style": 0.15, "use_speaker_boost": True},
    })
    subprocess.run(["curl", "-sS", "--fail", "-o", MP3,
                    "-H", "xi-api-key: " + api_key(), "-H", "Content-Type: application/json",
                    "-d", body, "https://api.elevenlabs.io/v1/text-to-speech/" + VOICE_ID], check=True)
    d = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", MP3],
                       capture_output=True, text=True).stdout.strip()
    print(f"wrote {os.path.basename(MP3)} {float(d):.2f}s")
    global TEMPO
    TEMPO = max(1.0, min(1.10, float(d) / 13.6))   # nudge ≤10% so the read lands by 14.2 s
    assert float(d) / TEMPO <= 14.2, f"read is {d}s — too long for a 15 s picture even at 1.10x"


TEMPO = 1.0


def mux():
    # delay, tempo nudge, loudnorm to -16 LUFS (speech-only track), pad to picture length
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", SRC, "-i", MP3,
                    "-filter_complex", f"[1:a]atempo={TEMPO:.3f},adelay={DELAY_MS}|{DELAY_MS},loudnorm=I=-16:TP=-1.5:LRA=7,apad[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
                    "-shortest", "-movflags", "+faststart", DST], check=True)
    r = subprocess.run(["ffmpeg", "-i", DST, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    tail = r.split("Summary:")[-1]
    m = re.search(r"I:\s+(-?[\d.]+) LUFS.*?Peak:\s+(-?[\d.]+) dBFS", tail, re.S)
    print(f"wrote {os.path.basename(DST)}  I {m.group(1)} LUFS  TP {m.group(2)} dBFS")


if __name__ == "__main__":
    tts()
    mux()
