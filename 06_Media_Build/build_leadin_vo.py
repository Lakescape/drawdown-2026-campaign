"""Lead-in v3 — VO in Victoria's cloned ElevenLabs voice, muxed onto v2.

The claim ledger's binding note: C1 and C4 are the legal exposure, and the video
"must be at least as careful, spoken not just captioned." So the drawdown hedge
is SPOKEN here — "exploring", "projected" — not left to a card. No version
before v3 cleared that bar.

Voice: "Victoria Short Record", the ONLY category=cloned voice in the ATX
ElevenLabs account (confirmed by Nate 2026-08-31). The other 49 are premade,
professional-library, or generated. Victoria consented to the clone; the script
below is hers to approve separately — a voice clone is not a blank cheque.

Key is read at runtime from InsightEngine/.env. It is NEVER written here, and
the rendered mp3/mp4 are gitignored alongside every other render.

Superseded, do not ship: truxor-leadin-15-vo.mp4 (Hermes, 2026-08-30) used the
Aug-4 scratch VO — not a Nate read, not an approved voice.
"""
import json
import os
import re
import subprocess
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
ENV = os.path.expanduser("~/InsightEngineMacOSPRO/InsightEngine/.env")
VOICE_ID = "QKljEqkNTmMOcROLnPla"          # Victoria Short Record

# Nate confirmed the VOICE is Victoria (2026-08-31). Victoria has NOT read these
# four lines. Consenting to a clone existing is not consenting to a script, and
# this is her voice on customer-facing marketing making a hedged claim about a
# lake drawdown. Flipping this is a person's decision, not an agent's.
SCRIPT_APPROVED_BY_VICTORIA = False
MODEL = "eleven_multilingual_v2"
SRC = os.path.join(HERE, "DRAWDOWN_LeadIn_916_v2_DRAFT.mp4")
MP3 = os.path.join(HERE, "vo_victoria_leadin.mp3")
DST = os.path.join(HERE, "DRAWDOWN_LeadIn_916_v3_VO_DRAFT.mp4")

# Timed to v2's four cards: hydrilla 0-3.5 | bank 3.5-6.5 | two Truxors 6.5-13 |
# $695 13-16. "Six ninety-five" is spelled out because TTS reads "$695"
# inconsistently. "L C R A" is spaced so it is read as letters.
SCRIPT = (
    "Ten years of high water hid this shoreline on Lake Austin.  "
    "The City and L C R A are drawing Lake Austin down — projected, ten to twelve feet.  "
    "We committed two amphibious machines in July.  "
    "Six ninety-five to walk yours. Credited back in full."
)
DELAY_MS = 1200        # so "six ninety-five" lands with the $695 card


def api_key():
    with open(ENV) as fh:
        m = re.search(r"^\s*ELEVENLABS_API_KEY\s*=\s*(.+)$", fh.read(), re.M)
    assert m, "ELEVENLABS_API_KEY not in " + ENV
    return m.group(1).strip().strip("\"'")


def tts():
    req = urllib.request.Request(
        "https://api.elevenlabs.io/v1/text-to-speech/" + VOICE_ID,
        data=json.dumps({
            "text": SCRIPT,
            "model_id": MODEL,
            "voice_settings": {"stability": 0.55, "similarity_boost": 0.8,
                               "style": 0.0, "use_speaker_boost": True},
        }).encode(),
        headers={"xi-api-key": api_key(), "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as r, open(MP3, "wb") as out:
        out.write(r.read())
    print("wrote", os.path.basename(MP3))


def measure(chain):
    """Pass 1. Single-pass loudnorm lands ~3 LU low on a clip this sparse."""
    p = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", MP3, "-af",
         chain + ",loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
        capture_output=True, text=True)
    d = json.loads(re.search(r"\{[^{]*input_i.*?\}", p.stderr, re.S).group(0))
    return ("measured_I={input_i}:measured_TP={input_tp}:measured_LRA={input_lra}"
            ":measured_thresh={input_thresh}:offset={target_offset}").format(**d)


def mux():
    pre = "adelay=%d|%d,apad=whole_dur=16" % (DELAY_MS, DELAY_MS)
    # volume+limiter closes the last ~1.3 LU: 1.7s of the 16s is silence, which
    # drags the integrated figure down even after two-pass loudnorm.
    af = ("[1:a]%s,loudnorm=I=-14:TP=-1.5:LRA=11:%s:linear=true,"
          "volume=1.3dB,alimiter=limit=0.891:level=disabled[a]" % (pre, measure(pre)))
    subprocess.run([
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
        "-i", SRC, "-i", MP3, "-filter_complex", af,
        "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
        "-t", "16", "-movflags", "+faststart", DST,
    ], check=True)
    print("wrote", os.path.basename(DST))


if __name__ == "__main__":
    assert SCRIPT_APPROVED_BY_VICTORIA, (
        "Victoria has not approved this script. Do not generate her voice saying "
        "words she has not read. Flip SCRIPT_APPROVED_BY_VICTORIA once she has.")
    assert os.path.exists(SRC), "build the v2 picture first: " + SRC
    tts()
    mux()
    # measured on the shipped draft: I=-14.3 LUFS, true peak -0.9 dBFS, 16.000s
