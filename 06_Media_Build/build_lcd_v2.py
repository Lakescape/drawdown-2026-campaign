#!/usr/bin/env python3
"""LCD v2 — round 6.  DRAWDOWN_LakeComingDown 9:16, 1080x1920, 30fps, 900 frames.

READ-ONLY BOUNDARY
    Nothing under 06_Media_Build is written, moved or renamed.  It is imported
    (resolve / BANNED / COUNT / C7_TWO_MACHINE from build_timeline_cut.py) and
    read as bytes (the Suno bed, the v1 master for the comparison sheet).
    Every output goes under renders/LCD_v2/.  Nothing posts.  Offline.

POLE: ENEMY.  Declared once, here, and the grade travels inside it —
    hydrilla S~47 and cool, WE WORK THE BED S~62 and warm.  Not one flat number.

ROUND 4 (head of production).  Directives A-G, each measured in BUILD_NOTES.
  A · END CARD GROUND is navy #1B2A4A with the approved WIDE LAKE AUSTIN AERIAL
      8c7fd940fc1f under it at 15 % opacity, gaussian sigma 120.  The film ends
      on the lake, restored — never on the enemy image.  Phone-number contrast
      is measured against the ground rows behind its own ink and must be >= 7:1.
  B · EVERY text element >= 4.5:1 at its hold frame, measured per card, printed
      as a table.  The lower-third device is a bottom GRADIENT on the picture —
      no box, no slab.
  C · FRAME 0 IS THE THUMBNAIL.  Wordmark and its rule are at full opacity on
      f0 with no ramp, and the whole-frame YAVG over f0-f10 is flat within +-2.
  D · ONE left edge (ink x0 = 84 +- 2, by measured ink, not alpha bbox), ONE
      bronze rule length (176 px), ONE eyebrow spec (+0.20em), and at most two
      families on the end card — DM Serif Text 400 + DM Sans 400/700.
  E · THE PAYOFF BEAT MOVES.  The Truxor material is TWO beats with a real hard
      cut between two framings on two different plates, each pushing >= 2 %/s.
  F · HIERARCHY: card 1 is DRAWDOWN 2026 (headline) over LAKE AUSTIN (eyebrow),
      a deliberate change from v1 where LAKE AUSTIN was the larger line.
  G · Kept: the Suno bed at offset 0.0, the five approved plates IN THE
      MASTER'S ORDER with the master's own card-to-plate pairing, verbatim
      words, cuts on the measured beat grid, deepest ink clear of y1436, and
      the locked CTA at full opacity for 4.000 s.

  Also closed this round, from the critic list:
    · the end card's pinned em-dash rectangles — DELETED.  split_date() strips
      the delimiter, the round-trip copy assert still passes, and the date
      column is RIGHT-ALIGNED so all four gutters are equal.
    · drop shadow OFF on every end-card element (a self-authored ground).
    · '~3 weeks to target' at 32 px / 70 % cream — no longer a peer of the
      four dated rows.
    · lockup tracking 0.18 -> 0.20; its tick is the 176 px bronze rule module.
    · the end card group is optically centred: equal void above and below.
    · scrim transitions are ZERO frames, landing on the cut.  No 4 f ramp.
    · the film opens on the AERIAL, not the hydrilla — the legible frame.

Run:  python3 build_lcd_v2.py
"""
import json, os, re, shutil, subprocess, sys

# The source tree is READ ONLY — CPython would otherwise drop a __pycache__
# directory into it just by importing build_timeline_cut.
sys.dont_write_bytecode = True
sys.path.insert(0, "/Users/austinlakescapes/drawdown-2026-campaign/06_Media_Build")
from build_timeline_cut import resolve, BANNED, COUNT, C7_TWO_MACHINE  # noqa: E402

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont  # noqa: E402

# ── paths ────────────────────────────────────────────────────────────────────
SRC = "/Users/austinlakescapes/drawdown-2026-campaign/06_Media_Build"        # READ ONLY
V2 = "/Users/austinlakescapes/drawdown-2026-campaign/.claude/worktrees/platform-native-renders/06_Media_Build"
OUT = os.path.join(V2, "renders", "LCD_v2")
STRAPS, SEG, QC, LOGS = (os.path.join(OUT, d) for d in ("straps", "seg", "qc", "logs"))
BED = os.path.join(SRC, "audio", "suno", "02_LakeComingDown_v2.mp3")
MASTER = os.path.join(SRC, "DRAWDOWN_LakeComingDown_916_SUNO_BED.mp4")
FINAL = os.path.join(OUT, "LCD_v2_916.mp4")
SILENT = os.path.join(OUT, "LCD_v2_916_SILENT.mp4")

FONTS = "/Users/austinlakescapes/ATX-Proposal-System/fonts/"
# Directive D: the end card's dates are DM Sans 400 and the phone number is
# DM Sans 700.  Two families on the card, two weights inside the sans.
SERIF, SANS7 = FONTS + "DMSerifText-400.ttf", FONTS + "DMSans-700.ttf"
SANS4 = FONTS + "DMSans-400.ttf"

VW, VH, FPS, NF = 1080, 1920, 30, 900
NAVY, CREAM, BRONZE = (27, 42, 74), (250, 246, 240), (196, 151, 110)
SCRIM_RGB = (8, 14, 24)

# ── beat grid, measured on 02_LakeComingDown_v2.mp3 ──────────────────────────
BPM, BEAT, PHASE = 130.85, 0.458541, 0.0551
BAR = BEAT * 4
DOWNBEATS = [2, 57, 112, 167, 222, 277, 332, 387, 442, 497, 552,
             607, 662, 717, 772, 827, 882]

# ── type scale: ONE ratio, 1.25, anchored at 28 ──────────────────────────────
#   Directive D.  Dates are DM Sans 400 at 40; the phone number is DM Sans 700.
#   T_NOTE is the one sub-ordinate size — '~3 weeks to target' is a note hanging
#   off the Oct 12 row, not a fifth dated fact, so it is smaller AND dimmer.
T_EYEBROW, T_LEAD, T_TAG, T_NOTE, T_DATE, T_TITLE, T_HEAD2, T_HEAD1 = \
    28, 35, 30, 32, 40, 55, 69, 86
NOTE_A = 178                    # 70 % cream on the note row
LEAD2 = 72                      # two-line serif leading at 69
CAP_W = 840                     # hard line cap, build fails rather than shrinks
BOX = (60, 140, 900, 1436)      # safe box: TikTok dead zones 140 / 484 / 60 / 180
INK_FLOOR = 1340                # every lower-third's LAST ink bottom lands here
GRID_X = 84                     # flush left, everywhere.  Nothing is centred.
TICK_Y = 158                    # lockup rule — the 176 px module, bronze, and
                                # ABOVE the wordmark.  Below it, a 176 px rule
                                # under a 315 px wordmark reads as a truncated
                                # underline stopping mid-word; above it, the
                                # same module reads as an accent rule, which is
                                # what it is everywhere else in the film.
RULE_W = 176                    # THE RULE MODULE.  Directive D: ONE length,
RULE_H = 3                      # 176 px, everywhere — the lockup tick included.
#   The end-card schedule.  Directive + critic: the pinned em-dash rectangles
#   are GONE (they rendered at cap height and read as macrons), and the date
#   column is RIGHT-ALIGNED so every gutter is identical instead of swinging
#   83 px.  The right edge is solved so the LONGEST date cell starts exactly on
#   the film's one margin, x = 84 — so the block still anchors at the margin
#   and only the three shorter dates rag, which is how a schedule is set.
COL_GUTTER = 48

# ── the words.  Verbatim from build_lake_coming_down.py CARDS + TIMELINE_CARD ─
CTA_LINE1, CTA_LINE2 = "Text TRUXOR to", "254-780-6971"
CTA_VERBATIM = "Text TRUXOR to 254-780-6971"

CARDS = {
    # s2's eyebrow is BACK to the master's exact string.  Round 5 re-typeset it
    # to "LCRA · OCT 12 – NOV 24" — same claim, same dates, but an uninstructed
    # change to approved on-screen copy.  Reverted, not flagged.
    "s1": dict(eyebrow="LAKE AUSTIN",            head=["DRAWDOWN 2026"]),
    "s2": dict(eyebrow="LCRA: Oct 12 – Nov 24",  head=["ABOUT 10 FEET"]),
    "s3": dict(eyebrow="COMMITTED IN JULY",      head=["TWO AMPHIBIOUS", "TRUXORS"]),
    "s4": dict(eyebrow="SCRAPE · HAUL · COVER",  head=["WE WORK THE BED"]),
}
DATES = ["Oct 12 — Lowering begins", "~3 weeks to target",
         "Nov 2–24 — Dry floor window", "Nov 24 — Refill starts",
         "Nov 30 — Normal pool"]
LOCKUP = "ATX LAKESCAPES"
END_TITLE = "LAKE AUSTIN DRAWDOWN"
# restored from the master's TIMELINE_CARD, verbatim, lower case, under the
# divider — the copy deletion that sat in round 5's Known gaps.
END_TAG = "scrape · haul · cover"


def split_date(s):
    """(date cell, event cell).  '~3 weeks to target' has no date cell: it is a
    sub-note of the Oct 12 row and reads as one by grid position, not by an
    ad-hoc 48 px indent that carries no other signal."""
    return tuple(s.split(" — ")) if " — " in s else ("", s)


def track_em(text, base):
    """Tracking is an ALL-CAPS device.  A mixed-case string gets +0.01em, never
    the caps value — wide tracking opens lowercase counters and 'Text' visibly
    falls apart at 35 px."""
    return base if text == text.upper() else 0.01

# ── picture lattice.  Every boundary is a computed downbeat of the v2 grid. ───
#   Bar = 55 f.  Bar counts 1 / 2 / 2 / 1 / 1 / 2 / 2 / 1 — NOT a metronome.
#   Modes are the master's own: the two soft wide plates run full-bleed (a
#   band on them reads as an out-of-focus smear — measured, see BUILD_NOTES),
#   the two sharp 1080x810 plates run in the fit band.  `scale` is the fit
#   plate scale and is ignored in bleed, where `pan` alone picks the window.
#   THE ENEMY OPENS THE FILM.  Round 5 led with the softest plate in the cut
#   (a 1080x607 aerial covered 3.16x) and buried the hydrilla — the thing the
#   piece is actually about — at 9.2 s with no card on it.  The hydrilla now
#   takes the 4-beat opening bar and the aerial starts at f57, where it still
#   runs 9.2 s and stays the film's spine.  Cut frames, bar counts and the bed
#   grid are all unchanged; bar counts are now 1/2/2/1/3/2/1.
#
#   `jitter` is handheld amplitude at 2x — band-limited positional noise, two
#   incommensurate frequencies near 1.2 Hz, no rotation.  It rides the two
#   ENEMY beats only.  The Truxor and haul beats keep their locked-off pushes,
#   so urgency resolves into craft instead of the whole film being one pole's
#   move language.  A jittered shot needs a base zoom of 1.05 for pan headroom.
#   `vpan` is where the band sits VERTICALLY on a fit plate (0.5 = centred, the
#   old hard-coded behaviour).  It exists because the C7 claim needs the
#   amphibious undercarriage in frame and a centred band cuts it off.
#   THE MASTER'S ORDER, and the master's own card-to-plate pairing (directive G):
#     aerial -> DRAWDOWN 2026 · hydrilla -> ABOUT 10 FEET ·
#     truxors -> TWO AMPHIBIOUS TRUXORS · haul -> WE WORK THE BED · card.
#   Round 6 opened on the hydrilla and moved ABOUT 10 FEET onto the aerial.
#   Both are reverted: the aerial is the legible frame (measured f0 YAVG 58.1
#   on the hydrilla against 60.9 with far more local contrast on the aerial,
#   and at thumbnail scale the weed mat has no readable subject at all), and
#   the master's pairing is the approved one.
#
#   DIRECTIVE E — THE PAYOFF BEAT MOVES.  The Truxor material is now TWO beats
#   with a REAL HARD CUT between two framings on two different plates:
#     03a  fd49bf6ffe3e  f332-441  carries the count word.  In C7_TWO_MACHINE,
#          exactly two whole Truxors, rubber tracks exposed, no third hull.
#     03b  c6b6853c038a  f442-551  the master's own b3 — two machines working
#          the bed, water and shoreline in frame.  NO TYPE, therefore no count
#          claim, therefore C7 never applies to the pontoon float behind them.
#   Each beat pushes over 2 %/s, which one 5.5 s beat on the yard plate could
#   not do without clipping Truxor #2.  Two beats solve the kinetic floor AND
#   put Lake Austin back under the money shot.
#   `drift` is a lateral creep in 2x px across the whole beat, on top of the
#   push.  A pure zoom has ZERO displacement at frame centre, which is why one
#   of these beats measured 0.64 against directive E's floor of 1.0 while
#   pushing at a compliant 2.4 %/s: the rate was legal and the middle of the
#   picture still was not moving.  A creep moves every pixel.
#   name  plate          mode   f0   f1   scale  pan   vpan  push          sat  warm  sharp jit  drift
SHOTS = [
    ("01a", "8c7fd940fc1f", "bleed",   0, 166, 1.10, 0.18, 0.50, (1.000, 1.120), 45, -0.022, 1.05, 0.00,    0),
    ("02a", "5a4942b7731d", "bleed", 167, 276, 1.05, 0.62, 0.50, (1.120, 1.050), 40, -0.008, 0.60, 0.55,    0),
    ("02b", "5a4942b7731d", "bleed", 277, 386, 1.05, 0.33, 0.50, (1.050, 1.120), 40, -0.008, 0.60, 0.55,    0),
    # f387 = 12.900 s — the frame directive E names.  It is a REAL HARD CUT to
    # the payoff, and the payoff is two beats on two plates, each pushing well
    # over 2 %/s with a lateral creep on top so the centre of frame moves too.
    ("03a", "fd49bf6ffe3e", "fit",   387, 496, 1.45, 0.415, 0.62, (1.000, 1.140), 56,  0.006, 0.00, 0.00, 110),
    ("03b", "c6b6853c038a", "fit",   497, 606, 1.45, 0.46, 0.42, (1.000, 1.150), 54,  0.004, 0.00, 0.00,  150),
    ("04a", "cd351a221a00", "fit",   607, 716, 1.20, 0.50, 0.50, (1.000, 1.085), 62,  0.018, 0.00, 0.00,    0),
    ("04b", "cd351a221a00", "fit",   717, 771, 1.46, 0.36, 0.50, (1.085, 1.000), 62,  0.018, 0.00, 0.00,    0),
    # DIRECTIVE A: navy #1B2A4A with the approved wide Lake Austin aerial under
    # it at 15 % and sigma 120.  The film ends on the lake, restored.
    ("05",  "8c7fd940fc1f", "card",  772, 899, 1.00, 0.50, 0.50, (1.000, 1.000), 50,  0.000, 0.00, 0.00,    0),
]
CUTS = [5.567, 9.233, 12.900, 16.567, 20.233, 23.900, 25.733]

GRADE = ("format=gbrp,"
         "curves=r='0/0.055 0.25/0.300 0.55/0.600 1/0.970'"
         ":g='0/0.052 0.25/0.280 0.55/0.565 1/0.950'"
         ":b='0/0.078 0.25/0.290 0.55/0.535 1/0.915',"
         "selectivecolor=greens=0.00 0.16 0.14 0.10:cyans=0.06 0.02 -0.04 0.04"
         ":blues=0.04 0.02 -0.06 0.02,"
         "eq=contrast=1.05:saturation=0.88:gamma=1.02:gamma_r=1.010:gamma_b=0.990,"
         "colorbalance=rm=0.012:bm=-0.018:rh=0.040:gh=0.012:bh=-0.050,"
         "eq=brightness=0.035,"
         "unsharp=5:5:0.35:5:5:0.0,"
         "vignette=angle=PI/9:x0=w/2:y0=h/2,"
         "noise=alls=3:allf=t+u")
# the card ground gets NOTHING but dither — it is composited in Pillow at
# exact values, so what proof() measures is what the encoder receives.
CARD_GRADE = "noise=alls=3:allf=t+u"
CARD_MIX = 0.15        # DIRECTIVE A: aerial under navy at <= 15 %
CARD_SIGMA = 120       # 2x space — 60 px at 1x, well over the 40 px floor

# ═════════════════════════════════════════════════════════════════════════════
# 1.  COPY GUARD — nothing renders until this passes
# ═════════════════════════════════════════════════════════════════════════════
BRIEF_BAN = re.compile(
    r"\$?695|inspection|unofficial|credited|assessment|exploring|"
    r"projected\s*10-12|extinct", re.I)

# The MASTER'S pairing, restored (directive G).  s3's count word rides
# fd49bf6ffe3e, which is in C7_TWO_MACHINE — the imported COUNT guard proves it
# and fails the build the moment anyone moves it.  03b carries NO type, so no
# count is claimed over c6b6853c038a and C7 never applies to it.
CARD_PLATE = {"s1": "8c7fd940fc1f", "s2": "5a4942b7731d",
              "s3": "fd49bf6ffe3e", "s4": "cd351a221a00"}


def guard():
    """Nothing renders until this passes."""
    strings = [LOCKUP, END_TITLE, END_TAG, CTA_LINE1, CTA_LINE2] + DATES
    for c in CARDS.values():
        strings += [c["eyebrow"]] + c["head"]
    bad = []
    for s_ in strings:
        if BANNED.search(s_):
            bad.append(f"BANNED term in {s_!r}")
        if BRIEF_BAN.search(s_):
            bad.append(f"BRIEF-BANNED term in {s_!r}")
    for k, c in CARDS.items():
        for line in c["head"] + [c["eyebrow"]]:
            if COUNT.search(line) and CARD_PLATE[k] not in C7_TWO_MACHINE:
                bad.append(f"COUNT word {line!r} rides non-C7 plate {CARD_PLATE[k]}")
    if " ".join([CTA_LINE1, CTA_LINE2]) != CTA_VERBATIM:
        bad.append("CTA is not the locked string verbatim")
    if strings.count(CTA_LINE2) != 1:
        bad.append("the CTA number appears more than once on screen")
    # every card's plate must actually be on screen for that card's whole window
    for k, (f0, fo) in SCHED.items():
        plates = {p for _, p, _, a, b, *_ in SHOTS if not (b < f0 or a > fo + 12)}
        if CARD_PLATE[k] not in plates:
            bad.append(f"{k} claims plate {CARD_PLATE[k]} but rides {plates}")
    for _, prefix, *_ in SHOTS:
        if prefix:
            resolve(prefix)                  # sha pin + local-bytes check
    # the schedule must survive the split without losing or inventing a glyph
    for d in DATES:
        a, b = split_date(d)
        if (a + " — " + b if a else b) != d:
            bad.append(f"date split is lossy for {d!r}")
    if bad:
        for b in bad:
            print("COPY GUARD FAIL:", b)
        raise SystemExit(2)
    print("copy guard OK — %d strings, CTA verbatim & once, COUNT rides %s (C7)"
          % (len(strings), CARD_PLATE["s3"]))


# ═════════════════════════════════════════════════════════════════════════════
# 2.  TYPE PRIMITIVES
# ═════════════════════════════════════════════════════════════════════════════
_probe = ImageDraw.Draw(Image.new("RGB", (8, 8)))

# Optical alignment BY GLYPH CLASS.  Round 5 trimmed "O C G S D 2 0" and nothing
# else, which gave the glyph needing the LEAST correction a -4 px trim and the
# two needing the MOST (a diagonal apex, and T's overhanging arm) none at all —
# the correction was inverted.  Trims are quoted at 86 px and scale with size.
#   DIRECTIVE D caps the trim at 2 px, so every first letter's ink — stem, apex
#   or shoulder — lands inside x = 84 +- 2.  Round 6's -6/-3 put a diagonal at
#   78 and called it one margin; it was three margins.  The optical correction
#   survives, at the size the directive allows.
DIAGONAL = set("AWVYTJ")        # apex or arm meets the margin at a point: -2
ROUNDED = set("OCGQSD20")        # shoulder meets it on a tangent:          -1
_K_DIAG, _K_ROUND = -2.0 / 86.0, -1.0 / 86.0


def font(p, s):
    return ImageFont.truetype(p, s)


def optical(text, size):
    c = text[:1]
    if c in DIAGONAL:
        return int(round(size * _K_DIAG))
    if c in ROUNDED:
        return int(round(size * _K_ROUND))
    return 0                                  # flat stems sit on the margin


_ink_cache = {}


def ink_lsb(text, path, size, em=0.0):
    """Real left side bearing in RENDERED pixels — the distance from the draw
    origin to the first lit column.  textbbox reports the layout box and returns
    0 here for every string, which is why round 5's elements landed at four
    different left edges while claiming one margin."""
    key = (text, path, size, round(em, 4))
    if key in _ink_cache:
        return _ink_cache[key]
    pad, w = 200, int(size * len(text) * 1.6) + 600
    im = Image.new("L", (w, int(size * 3) + 120), 0)
    d = ImageDraw.Draw(im)
    f = font(path, size)
    if em:
        x = float(pad)
        for ch in text:
            d.text((x, size), ch, font=f, fill=255)
            x += _probe.textlength(ch, font=f) + size * em
    else:
        d.text((pad, size), text, font=f, fill=255)
    b = im.getbbox()
    _ink_cache[key] = (0, 0) if b is None else (b[0] - pad, b[2] - b[0])
    return _ink_cache[key]


def ink_w(text, path, size, em=0.0):
    return ink_lsb(text, path, size, em)[1]


def place_x(text, path, size, em=0.0, margin=GRID_X, opt=True):
    """Draw origin that lands this string's INK on `margin`, then the class
    trim on top.  One margin for the whole film: flat stems at ink x0 = 84.
    `opt=False` PINS a column — the end card's event column was x0 = 336 on
    three rows and 335 on 'Nov 2–24' because the trim fired on that row's D."""
    return (margin - ink_lsb(text, path, size, em)[0]
            + (optical(text, size) if opt else 0))


def place_right(text, path, size, em, right):
    """Draw origin that lands this string's INK RIGHT edge on `right`.  The
    date column is right-aligned so all four gutters are identical."""
    lsb, w = ink_lsb(text, path, size, em)
    return right - w - lsb


def measure(text, path, size, em=0.0):
    f = font(path, size)
    b = _probe.textbbox((0, 0), text, font=f)
    if em == 0.0:
        return b[2] - b[0], b[1], b[3]
    w = sum(_probe.textlength(ch, font=f) + size * em for ch in text) - size * em
    return int(round(w)), b[1], b[3]


def draw_tracked(d, xy, text, path, size, fill, em=0.0):
    f = font(path, size)
    x, y = xy
    if em == 0.0:
        d.text((x, y), text, font=f, fill=fill)
        return
    for ch in text:
        d.text((x, y), ch, font=f, fill=fill)
        x += _probe.textlength(ch, font=f) + size * em


def layer(draw_fn, shadow=True):
    """One element -> its own RGBA 1080x1920 layer, with the film's one shadow."""
    im = Image.new("RGBA", (VW, VH), (0, 0, 0, 0))
    draw_fn(ImageDraw.Draw(im))
    ink = im.getbbox()          # BEFORE the shadow — GaussianBlur(8) inflates
                                # the alpha bbox by ~20 px and round 6 quoted
                                # that inflated number as the left margin.
    if not shadow:
        im.info["inkbox"] = ink
        return im
    sh = im.split()[3].point(lambda a: int(a * 0.60))
    sh_im = Image.new("RGBA", (VW, VH), (0, 0, 0, 0))
    sh_im.putalpha(sh)
    sh_im = sh_im.filter(ImageFilter.GaussianBlur(8))
    out = Image.new("RGBA", (VW, VH), (0, 0, 0, 0))
    out.alpha_composite(sh_im, (0, 3))
    out.alpha_composite(im)
    out.info["inkbox"] = ink
    return out


def assert_safe(name, im, width_cap=CAP_W):
    bb = im.getbbox()
    if bb is None:
        raise SystemExit(f"EMPTY LAYER {name}")
    x0, y0, x1, y1 = bb
    if not (x0 >= BOX[0] and y0 >= BOX[1] and x1 <= BOX[2] and y1 <= BOX[3]):
        raise SystemExit(f"SAFE ZONE VIOLATION {name}: bbox={bb} box={BOX}")
    if x1 - x0 > width_cap:
        raise SystemExit(f"LINE CAP VIOLATION {name}: {x1-x0}px > {width_cap}")
    return bb


def smoothstep(t):
    t = max(0.0, min(1.0, t))
    return t * t * (3 - 2 * t)


# ═════════════════════════════════════════════════════════════════════════════
# 3.  ELEMENTS  (name -> layer, in-frame, out-frame or None)
# ═════════════════════════════════════════════════════════════════════════════
IN_F, OUT_F = 5, 8            # CONSTRAINTS §7: entrance duration under 6 frames
RISE = 16                     # …and a 16 px upward translate over those 5 frames
ELEMENTS = []
BBOXES = []
INKBOX = []                   # (name, bbox) BEFORE the shadow — directive D

# card windows: (first frame of the rule, frame the headline starts leaving)
#   s1 starts on f0: the hook copy owned only 1.13 s of its own picture when
#   the rule landed at f8.  Rule f0 · eyebrow f6 · headline f12 — full by f17
#   (0.57 s), which is the critic's own fix; the 5 f ease is untouched.
SCHED = {"s1": (0, 156), "s2": (177, 370), "s3": (392, 480), "s4": (612, 755)}
CARD_IN = 772                 # the end card's own first frame
CTA_IN = 775                  # CTA full at f780 -> f899 = 120 f = 4.000 s


def add(name, im, fin, fout=None, move=False, hard=False):
    """`hard` = no entrance at all: full opacity on its first frame.  Directive
    C — frame 0 is the thumbnail, so the wordmark and its rule cannot ramp."""
    BBOXES.append((name, assert_safe(name, im)))
    INKBOX.append((name, im.info.get("inkbox") or im.getbbox()))
    ELEMENTS.append(dict(name=name, im=im, fin=fin, fout=fout, move=move,
                         hard=hard))


def build_elements():
    # ── lockup, f0 -> f899, never animates again ────────────────────────────
    #   DIRECTIVE D — the lockup is inside the film's own system now.  Round 6
    #   ran it at +0.18em while both caps eyebrows ran +0.20em (two values for
    #   one 28 px caps role) and gave its tick a cream-43 % bar at the measured
    #   wordmark width while all seven other rules were bronze — so the film
    #   showed two rule treatments under a note claiming one.  Tracking is
    #   +0.20em and the tick IS the rule module: bronze, 176 x 3, at x = 84.
    #   DIRECTIVE C — both are `hard`: full opacity on f0, no ramp, because f0
    #   is the thumbnail.
    lock_x = place_x(LOCKUP, SANS7, T_EYEBROW, 0.20)
    add("lockup", layer(lambda d: draw_tracked(
        d, (lock_x, 186), LOCKUP, SANS7, T_EYEBROW, CREAM + (255,), 0.20)),
        0, hard=True)
    add("lockup_tick", layer(lambda d: d.rectangle(
        [GRID_X, TICK_Y, GRID_X + RULE_W - 1, TICK_Y + RULE_H - 1],
        fill=BRONZE + (255,))), 0, hard=True)

    # ── four lower-thirds, all bottom-anchored on INK_FLOOR ─────────────────
    for key in ("s1", "s2", "s3", "s4"):
        c = CARDS[key]
        f0, fo = SCHED[key]
        head, size = c["head"], (T_HEAD1 if len(c["head"]) == 1 else T_HEAD2)
        lead = LEAD2 if len(head) > 1 else 0
        _, t0_last, t1_last = measure(head[-1], SERIF, size)
        y_last = INK_FLOOR - t1_last
        origins = [y_last - lead * (len(head) - 1 - i) for i in range(len(head))]
        _, t0_first, _ = measure(head[0], SERIF, size)
        head_ink_top = origins[0] + t0_first
        eb, eb_em = c["eyebrow"], track_em(c["eyebrow"], 0.20)
        _, et0, et1 = measure(eb, SANS7, T_EYEBROW, eb_em)
        eyebrow_y = head_ink_top - 48 - (et1 - et0) - et0
        rule_y = eyebrow_y + et0 - 48
        eb_x = place_x(eb, SANS7, T_EYEBROW, eb_em)

        add(f"{key}_rule", layer(lambda d, ry=rule_y: d.rectangle(
            [GRID_X, ry, GRID_X + RULE_W - 1, ry + RULE_H - 1],
            fill=BRONZE + (255,))), f0, fo + 6)
        add(f"{key}_eyebrow", layer(
            lambda d, t=eb, ey=eyebrow_y, ex=eb_x, em=eb_em: draw_tracked(
                d, (ex, ey), t, SANS7, T_EYEBROW, BRONZE + (255,), em)),
            f0 + 6, fo + 3, move=True)

        def _head(d, hd=head, sz=size, og=origins):
            for line, oy in zip(hd, og):
                d.text((place_x(line, SERIF, sz), oy), line,
                       font=font(SERIF, sz), fill=CREAM + (255,))
        add(f"{key}_head", layer(_head), f0 + 10, fo, move=True)

    # ── end card.  Flat #1B2A4A ground; END_LIFT = 0, so the block reaches the
    #    dead-zone edge instead of floating with 677 empty rows beneath it.
    #   GEOMETRY IS SOLVED, NOT TYPED.  The group is laid out from its own ink
    #   with one spacing scale (48 / 72 / 96), then OPTICALLY CENTRED between
    #   the lockup and the safe floor, so the 303 px void above the title and
    #   the 507 px void beneath the phone number both disappear by
    #   construction instead of by a hand-tuned END_LIFT that measured itself
    #   against the safe box and not against the frame.
    TOP_BOUND = 186 + measure(LOCKUP, SANS7, T_EYEBROW, 0.20)[2]   # ink bottom
    ink_h = lambda t, p, s, e=0.0: (measure(t, p, s, e)[2] - measure(t, p, s, e)[1])

    _, tt0, tt1 = measure(END_TITLE, SERIF, T_TITLE)
    anchor = 0                             # relative; centred at the end
    title_y = anchor - tt0
    ruleA = anchor + (tt1 - tt0) + 48

    # THE SCHEDULE.  No separator glyph at all.  The pinned em-dash rectangles
    # rendered at cap height on every row — five tick marks floating above the
    # words like macrons — and on 'Nov 2–24' one landed 5 px after the row's
    # own en dash, reading as a typo.  split_date() already treats ' — ' as a
    # delimiter, the round-trip assert in guard() still proves no approved word
    # changed, and the structure now comes from the columns themselves.
    # The date column is RIGHT-ALIGNED, which is how a schedule is set and the
    # only thing that makes all four gutters equal (they swung 83 px to 10 px
    # when it was left-aligned).  Its right edge is solved so the LONGEST date
    # cell starts exactly on the film's one margin, x = 84.
    rows = [split_date(s) for s in DATES]
    dcells = [a for a, _ in rows if a]
    COL_RIGHT = GRID_X + max(ink_w(a, SANS4, T_DATE) for a in dcells)
    COL_EVENT = COL_RIGHT + COL_GUTTER

    d0_ink = ruleA + RULE_H + 96
    row_ink = [d0_ink + 72 * i for i in range(5)]

    def _sz(i):
        """'~3 weeks to target' is a NOTE hanging off the Oct 12 row, not a
        fifth dated fact.  Round 6 set it in the same face, size, weight and
        value as the four dated rows with an empty date cell, so it read as a
        row whose date had gone missing.  32 px at 70 % cream, in the event
        column: two signals, both subordinate."""
        return (T_NOTE, NOTE_A) if not rows[i][0] else (T_DATE, 255)

    def _row_y(i, txt, sz):
        return row_ink[i] - measure(txt, SANS4, sz)[1]

    last_bot = max(row_ink[i] + ink_h(rows[i][1], SANS4, _sz(i)[0])
                   for i in range(5))
    ruleB = last_bot + 96
    tag_ink = ruleB + RULE_H + 48
    _, gt0, gt1 = measure(END_TAG, SANS7, T_TAG, 0.01)
    tag_y = tag_ink - gt0
    _, ct0, ct1 = measure(CTA_LINE1, SANS7, T_LEAD, 0.01)
    cta1_y = tag_y + gt1 + 72 - ct0
    _, nt0, nt1 = measure(CTA_LINE2, SANS7, T_HEAD1, 0.02)
    cta2_y = cta1_y + ct1 + 48 - nt0

    # ── centre the group.  Everything above is relative to title ink top = 0.
    grp_h = (cta2_y + nt1)                     # ink top 0 -> ink bottom
    LIFT = TOP_BOUND + (BOX[3] - TOP_BOUND - grp_h) // 2
    title_y += LIFT
    ruleA += LIFT
    ruleB += LIFT
    tag_y += LIFT
    cta1_y += LIFT
    cta2_y += LIFT
    row_ink = [v + LIFT for v in row_ink]
    print("  end card — group %d px, void above %d, void below %d, "
          "date column right-aligned on x=%d, event column x=%d"
          % (grp_h, LIFT - TOP_BOUND, BOX[3] - (LIFT + grp_h),
             COL_RIGHT, COL_EVENT))

    # CTA first — it is the reason the card exists and it holds the final beat.
    # Lead-in tracking is +0.01em, NOT +0.06em: wide tracking is an all-caps
    # device and at 35 px it opened the counters until the word "Text" fell
    # apart.  The 35 -> 86 size step already carries the hierarchy.
    #   NO DROP SHADOW ANYWHERE ON THE CARD.  A 0/+3 px, 8 px-blur, 60 %-black
    #   halo does zero legibility work on a ground this build authored itself —
    #   it measured a local ground of L 23-27 against a median of 38, which
    #   means the advertised ratio was taken against the wrong number — and it
    #   is a second emphasis device on a card whose whole system is one bronze
    #   rule.  It stays on the photo straps, where it earns its keep.
    NS = dict(shadow=False)
    add("cta_lead", layer(lambda d: draw_tracked(
        d, (place_x(CTA_LINE1, SANS7, T_LEAD, 0.01), cta1_y), CTA_LINE1,
        SANS7, T_LEAD, CREAM + (255,), 0.01), **NS), CTA_IN, move=True)
    add("cta_number", layer(lambda d: draw_tracked(
        d, (place_x(CTA_LINE2, SANS7, T_HEAD1, 0.02), cta2_y), CTA_LINE2,
        SANS7, T_HEAD1, CREAM + (255,), 0.02), **NS), CTA_IN, move=True)
    add("end_title", layer(lambda d: d.text(
        (place_x(END_TITLE, SERIF, T_TITLE), title_y), END_TITLE,
        font=font(SERIF, T_TITLE), fill=CREAM + (255,)), **NS),
        CARD_IN, move=True)
    # the master's TIMELINE_CARD sets this tag in COPPER.  Round 6 shipped it
    # cream, which left a 4.3 s card with bronze only in two hairlines and made
    # the tag read as the first line of the CTA block.  Restored to #C4976E.
    add("end_tag", layer(lambda d: draw_tracked(
        d, (place_x(END_TAG, SANS7, T_TAG, 0.01), tag_y), END_TAG,
        SANS7, T_TAG, BRONZE + (255,), 0.01), **NS), CARD_IN + 6, move=True)
    add("end_ruleB", layer(lambda d: d.rectangle(
        [GRID_X, ruleB, GRID_X + RULE_W - 1, ruleB + RULE_H - 1],
        fill=BRONZE + (255,)), **NS), CARD_IN + 4)
    add("end_ruleA", layer(lambda d: d.rectangle(
        [GRID_X, ruleA, GRID_X + RULE_W - 1, ruleA + RULE_H - 1],
        fill=BRONZE + (255,)), **NS), CARD_IN + 4)
    for i, (dcell, ecell) in enumerate(rows):
        def _row(d, dc=dcell, ec=ecell, idx=i):
            sz, av = _sz(idx)
            if dc:
                d.text((place_right(dc, SANS4, sz, 0.0, COL_RIGHT),
                        _row_y(idx, dc, sz)), dc, font=font(SANS4, sz),
                       fill=CREAM + (255,))
            # the event column is PINNED — opt=False — so 'Dry floor window'
            # cannot land on 335 while the other three land on 336.
            d.text((place_x(ec, SANS4, sz, 0.0, COL_EVENT, opt=False),
                    _row_y(idx, ec, sz)), ec, font=font(SANS4, sz),
                   fill=CREAM + (av,))
        add(f"end_date{i}", layer(_row, **NS), CARD_IN + 8 + 4 * i, move=True)

    deepest = max(b[3] for _, b in BBOXES)
    print("elements OK — %d layers, deepest ink y=%d (floor %d, clearance %d)"
          % (len(ELEMENTS), deepest, BOX[3], BOX[3] - deepest))
    # DIRECTIVE G — the locked CTA at FULL opacity for exactly 4.000 s.
    full = [f for f in range(NF)
            if alpha_at(next(e for e in ELEMENTS if e["name"] == "cta_number"),
                        f)[0] >= 0.999]
    print("  CTA full opacity f%d-f%d = %d frames = %.3f s"
          % (full[0], full[-1], len(full), len(full) / FPS))
    if len(full) != 120:
        raise SystemExit(f"CTA hold is {len(full)} f, not 120 (4.000 s)")
    # DIRECTIVE D — ONE left edge, proved on the ink, not on the alpha bbox.
    # Every element that starts at the film's margin must land on 84 +- 2.
    off = [(n, b[0]) for n, b in INKBOX
           if not n.startswith("end_date") and abs(b[0] - GRID_X) > 2]
    edges = sorted({b[0] for n, b in INKBOX if not n.startswith("end_date")})
    print("  left edge — margin ink x0 values %s%s"
          % (edges, "" if not off else f"   OUT OF BAND: {off}"))
    if off:
        raise SystemExit("LEFT EDGE VIOLATION (directive D, 84 +- 2): %s" % off)
    return deepest


# ═════════════════════════════════════════════════════════════════════════════
# 4.  SCRIMS — measured, per shot.  This is lockup_trim() / eyebrow_trim().
# ═════════════════════════════════════════════════════════════════════════════
#   WCAG: cream #FAF6F0 L=0.930 · bronze #C4976E L=0.348
#   cream >= 6.0 : 1  ->  ground L <= 0.1133  ->  8-bit <= 96
#   bronze >= 4.5 : 1  ->  ground L <= 0.0384  ->  8-bit <= 55
#   A SCRIM IS CHROME.  Chrome does not animate to the picture.  Round 5 drove
#   both scrims off per-shot measured luma, so the frame's own architecture
#   changed shape at every cut, vanished entirely for 5.5 s, and pumped four
#   times BETWEEN cuts — including a -78 level drop one frame after a cut and a
#   +72 rise with no type on screen at all.  Both are now ONE constant value,
#   switching only ON CUT FRAMES, with a 4-frame ramp.
#   EYE_TARGET was 36, which solved to a 0.86 lower scrim — and a 0.86 scrim
#   over rows 1070-1420 leaves 14 % of the picture visible across 60 % of the
#   band, on every beat, whether or not that beat carries an eyebrow.  That is
#   a craft cost paid film-wide to protect four straps, and it halved the
#   measured motion of the picture underneath it.  44 is solved against bronze
#   at 4.5:1 with margin (bronze needs ground <= 55) and the DELIVERED ratio is
#   still measured per element, per frame, and printed.
LOCK_TARGET, EYE_TARGET = 86.0, 39.0
TOP_A = 0.58                  # ONE constant, solved against the WORST-LOCAL
                              # 16x16 ground tile, not the mean.  The critic's
                              # 0.45 measures 4.6:1 there and 0.52 measures
                              # 5.21:1 — both under the 6:1 floor this build
                              # holds everywhere else.  0.58 measures 6.2:1.
TOP_FULL, TOP_FADE = 300, 480          # 180 px of ramp — 140 shows an edge in
                                       # flat sky.  Linear, not smoothstep.
SCRIM_TOP, SCRIM_BOT, SCRIM_A = 720, 1070, 0.64
SCRIM_FADE0, SCRIM_FADE1, SCRIM_TAIL = 1420, 1780, 0.16
SNAP_F = 0                             # ZERO.  Round 6's 4-frame ramp was a
                                       # measured 43.6-level pump over 133 ms
                                       # in rows y1100-1920 *after* the money
                                       # cut, with the picture underneath
                                       # static — the lower half visibly wiped
                                       # down.  A cut hides a step; a 4-frame
                                       # ramp advertises one.  Both scrims now
                                       # switch ON the cut frame, in 0 frames,
                                       # and switch exactly once in the film.

LOCK_A = [0.0] * NF                    # per-frame top-scrim alpha
SCRIM_M = [1.0] * NF                   # per-frame lower-scrim multiplier


def need_alpha(v_ground, v_target, cap):
    if v_ground <= v_target:
        return 0.0
    return min(cap, (v_ground - v_target) / max(1.0, v_ground - SCRIM_RGB[1]))


def top_scrim():
    im = Image.new("RGBA", (VW, VH), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for y in range(TOP_FADE):
        a = 1.0 if y <= TOP_FULL else 1.0 - (y - TOP_FULL) / (TOP_FADE - TOP_FULL)
        d.line([(0, y), (VW, y)], fill=SCRIM_RGB + (int(255 * a),))
    return im


def low_scrim():
    """Profile normalised to a 1.0 peak — the per-shot peak alpha is applied
    by bake_type, so a shot that needs 0.86 gets 0.86 and is not silently
    clipped back to the profile constant."""
    im = Image.new("RGBA", (VW, VH), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    tail = SCRIM_TAIL / SCRIM_A
    for y in range(SCRIM_TOP, VH):
        if y <= SCRIM_BOT:
            a = smoothstep((y - SCRIM_TOP) / (SCRIM_BOT - SCRIM_TOP))
        elif y <= SCRIM_FADE0:
            a = 1.0
        else:
            k = smoothstep(min(1.0, (y - SCRIM_FADE0) / (SCRIM_FADE1 - SCRIM_FADE0)))
            a = 1.0 + (tail - 1.0) * k
        d.line([(0, y), (VW, y)], fill=SCRIM_RGB + (int(255 * a),))
    return im


# ═════════════════════════════════════════════════════════════════════════════
# 5.  TYPE OVERLAY SEQUENCE — smoothstep alpha + 16 px rise, baked per frame
# ═════════════════════════════════════════════════════════════════════════════
def alpha_at(el, f):
    if f < el["fin"]:
        return 0.0, 0
    if el.get("hard"):
        return 1.0, 0
    if f < el["fin"] + IN_F:
        s = smoothstep((f - el["fin"]) / IN_F)
        a, dy = s, int(round(RISE * (1.0 - s))) if el["move"] else 0
    else:
        a, dy = 1.0, 0
    if el["fout"] is not None and f >= el["fout"]:
        a *= max(0.0, 1.0 - (f - el["fout"]) / OUT_F)
    return a, dy


def _fade(im, a):
    o = im.copy()
    o.putalpha(o.split()[3].point(lambda v, m=a: int(v * m)))
    return o


def bake_type():
    shutil.rmtree(STRAPS, ignore_errors=True)
    os.makedirs(STRAPS)
    low, top = low_scrim(), top_scrim()
    cache = {}
    for f in range(NF):
        st = tuple((round(a, 3), dy) for a, dy in (alpha_at(e, f) for e in ELEMENTS))
        sa = round(SCRIM_M[f], 2)          # already snapped to cut frames
        la = round(LOCK_A[f], 2)
        key = st + (sa, la)
        if key in cache:
            os.link(cache[key], f"{STRAPS}/t_{f:04d}.png")
            continue
        im = Image.new("RGBA", (VW, VH), (0, 0, 0, 0))
        if la > 0.005:
            im.alpha_composite(_fade(top, la))
        if sa > 0.005:
            im.alpha_composite(_fade(low, min(1.0, sa)))
        for e in ELEMENTS:
            a, dy = alpha_at(e, f)
            if a <= 0.001:
                continue
            lay = e["im"] if a >= 0.999 else _fade(e["im"], a)
            im.alpha_composite(lay, (0, dy))
        p = f"{STRAPS}/t_{f:04d}.png"
        im.save(p, compress_level=1)
        cache[key] = p
    print("type sequence baked — %d frames, %d distinct" % (NF, len(cache)))


# ═════════════════════════════════════════════════════════════════════════════
# 6.  PICTURE BASE PLATES  (2x, so the sharp plate lands ~1:1 after downscale)
# ═════════════════════════════════════════════════════════════════════════════
BW, BH = VW * 2, VH * 2
FIT_TOP, FIT_H = 480 * 2, 972 * 2            # fit band y 480..1452 at 1x
FEATHER = 160                                # 80 px at 1x, linear — not 24
_plates = {}


def load_plate(prefix):
    if prefix not in _plates:
        _plates[prefix] = resolve(prefix)
    return _plates[prefix]


def cover(im, w, h):
    s = max(w / im.width, h / im.height)
    return im.resize((max(w, int(im.width * s) + 1),
                      max(h, int(im.height * s) + 1)), Image.LANCZOS)


def blurred_ground(im, sigma, bright, sat):
    big = cover(im, BW, BH)
    g = big.crop(((big.width - BW) // 2, (big.height - BH) // 2,
                  (big.width - BW) // 2 + BW, (big.height - BH) // 2 + BH))
    g = g.filter(ImageFilter.GaussianBlur(sigma))
    g = ImageEnhance.Brightness(g).enhance(bright)
    return ImageEnhance.Color(g).enhance(sat)


def base_plate(prefix, mode, scale, pan, vpan=0.5):
    if mode == "card":
        # DIRECTIVE A.  Navy #1B2A4A with the approved WIDE LAKE AUSTIN AERIAL
        # under it at CARD_MIX opacity and gaussian sigma CARD_SIGMA (>= 40 at
        # 1x; this runs in 2x space, so 120 here is 60 at 1x).  The film ends
        # on the lake, restored — never on the enemy image, and never on a
        # photograph legible enough to become a second subject.  The aerial is
        # darkened and desaturated BEFORE the blend, so the ground stays a
        # field: measured p5/p95 spread and the phone number's own local ratio
        # are both printed by proof().
        sha, im = load_plate(prefix)
        lake = blurred_ground(im, CARD_SIGMA, 0.55, 0.40)
        return sha, Image.blend(Image.new("RGB", (BW, BH), NAVY),
                                lake, CARD_MIX), None

    sha, im = load_plate(prefix)
    if mode == "bleed":
        big = cover(im, int(BW * scale), int(BH * scale))
        x = int((big.width - BW) * pan)
        y = (big.height - BH) // 2
        return sha, big.crop((x, y, x + BW, y + BH)), None
    # GROUND: sigma 300, not 52, and pulled 40 % to the ATX navy token.  At 52
    # the plate's own horizon survived as a visible seam near y500 — so 54 % of
    # the phone screen was blurred filler with a line through it, the second
    # template tell after the end card.  The 80 px feather itself measured
    # correct (10-90 % over 95 px top, 162 px bottom); the defect was the
    # ground's CONTENT, so the content is what goes.
    ground = blurred_ground(im, 300, 0.92, 0.62)
    ground = Image.blend(ground, Image.new("RGB", ground.size, NAVY), 0.40)
    sw = int(BW * scale)
    sharp = im.resize((sw, int(im.height * sw / im.width)), Image.LANCZOS)
    cx = int((sw - BW) * pan)
    cy = max(0, int((sharp.height - FIT_H) * vpan))
    sharp = sharp.crop((cx, cy, cx + BW, cy + FIT_H))
    # 80 px LINEAR feather — a smoothstep ramp concentrates the step into 9-12 px
    # and reads as a hard letterbox window.  Linear does not.
    mask = Image.new("L", (BW, FIT_H), 255)
    md = ImageDraw.Draw(mask)
    for i in range(FEATHER):
        v = int(255 * (i / FEATHER))
        md.line([(0, i), (BW, i)], fill=v)
        md.line([(0, FIT_H - 1 - i), (BW, FIT_H - 1 - i)], fill=v)
    ground.paste(sharp, (0, FIT_TOP), mask)
    return sha, ground, None


def band_luma(prefix):
    _, im = load_plate(prefix)
    g = im.convert("L")
    return sum(g.getdata()) / (g.width * g.height)


def graded_still(png, post, tag):
    p = png.replace(".png", f"_{tag}.png")
    run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-i", png,
         "-vf", post + ",format=yuv420p", p])
    im = Image.open(p).convert("RGB")
    im.load()
    os.remove(p)
    return im


def region_luma(im, box):
    return sum(im.convert("L").crop(box).getdata()) / \
        ((box[2] - box[0]) * (box[3] - box[1]))


# ═════════════════════════════════════════════════════════════════════════════
# 7.  RENDER
# ═════════════════════════════════════════════════════════════════════════════
def run(cmd, **kw):
    p = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if p.returncode:
        sys.stderr.write(p.stderr[-4000:])
        raise SystemExit("ffmpeg failed: " + " ".join(cmd[:6]))
    return p


LOCK_BOX = (120, 280, 840, 520)        # x60-420 / y140-260 at 1x, doubled
EYE_BOX = (120, 2200, 1800, 2580)      # x60-900 / y1100-1290 at 1x, doubled


MAX_STEP = 6.0        # max YAVG a cut may step.  Brief asks for +/-8.

# ── HANDHELD.  §7: camera moves are locked-off/slow-push (Payoff) OR
#    handheld/urgent (Enemy), never mixed within one pole.  Round 5 declared
#    ENEMY and then measured 0.40-1.12 degrained inter-frame diff on every one
#    of nine shots — Payoff move language on an Enemy piece, on all of it.
#    Two incommensurate low frequencies near 1.2 Hz, no rotation.  Amplitudes
#    are 2x-space px; the dominant term gives ~2 px/frame at 1x, the pair
#    ~3.5 px/frame peak, inside the critic's 2-4.  A jittered shot carries a
#    base zoom of 1.05, which is where the +-25 px of pan headroom comes from.
JX1, JX2, JY1, JY2 = 16.0, 9.0, 13.0, 7.0


def jx(a):
    if a <= 0.001:
        return "iw/2-(iw/zoom/2)"
    return (f"iw/2-(iw/zoom/2)+{JX1*a:.2f}*sin(2*PI*1.20*on/{FPS})"
            f"+{JX2*a:.2f}*sin(2*PI*0.77*on/{FPS}+1.7)")


def jy(a):
    if a <= 0.001:
        return "ih/2-(ih/zoom/2)"
    return (f"ih/2-(ih/zoom/2)+{JY1*a:.2f}*sin(2*PI*1.05*on/{FPS}+0.9)"
            f"+{JY2*a:.2f}*sin(2*PI*0.63*on/{FPS}+2.4)")


def measure_shots():
    """Pass A.  Build every base plate, measure it graded, and CHAIN the
    brightness trims so no cut can step more than MAX_STEP.  Round 4 trimmed
    only the two Truxor beats against one reference, which left -19 YAVG at
    hydrilla->Truxor and -38 into the end card.  This walks the whole film."""
    meas = []
    for name, prefix, mode, f0, f1, scale, pan, vpan, push, sat, warm, shp, jit, drift in SHOTS:
        sha, plate, live = base_plate(prefix, mode, scale, pan, vpan)
        png = f"{SEG}/base_{name}.png"
        plate.save(png)
        lpng = None
        if mode == "card":
            # the flat token is not graded, not saturation-matched and not
            # walked by the brightness chain — the whole point of it is that
            # #1B2A4A arrives at the encoder as #1B2A4A.
            g_im = graded_still(png, CARD_GRADE, "p2")
            meas.append(dict(name=name,
                             sha=f"{sha} @ {CARD_MIX:.0%} / sigma {CARD_SIGMA}"
                                 f" over #1B2A4A", png=png, lpng=None,
                             base=CARD_GRADE, mean=region_luma(g_im, (0, 0, BW, BH)),
                             lock=0.0, eye=0.0, s_raw=0.0, smul=1.0, fixed=True))
            continue
        base = GRADE
        # the two wide plates are 1080x607 / 1080x810 covered to 1080x1920 —
        # a 3.16x / 2.37x resample, and measurably the softest frames in the
        # film.  An extra unsharp on those beats only, so the hook is not the
        # mushiest thing in the cut.
        if shp > 0.01:
            base += f",unsharp=7:7:{shp:.2f}:7:7:0.0"
        if abs(warm) > 0.001:
            base += f",colorbalance=rm={warm:.3f}:bm={-warm:.3f}"
        s_im = graded_still(png, base, "p1")
        s_raw = sum(s_im.convert("HSV").split()[1].getdata()) / (s_im.width * s_im.height)
        smul = max(0.75, min(1.85, sat / s_raw))
        if abs(smul - 1.0) > 0.01:
            base += f",eq=saturation={smul:.3f}"
        g_im = graded_still(png, base, "p2")
        meas.append(dict(name=name, sha=sha, png=png, lpng=lpng, base=base,
                         mean=region_luma(g_im, (0, 0, BW, BH)),
                         lock=region_luma(g_im, LOCK_BOX),
                         eye=region_luma(g_im, EYE_BOX),
                         s_raw=s_raw, smul=smul, fixed=False))
    # chain: every shot pulled to within MAX_STEP of the previous, trimmed shot.
    # The flat card is excluded — a designed ground is an event, not a step, and
    # it has the film's one cross-dissolve in front of it.
    tgt = meas[0]["mean"]
    for i, m in enumerate(meas):
        if m["fixed"]:
            m["trim"], m["target"] = 0.0, m["mean"]
            continue
        t = (m["mean"] - 9.0) if i == 0 else \
            min(max(m["mean"], tgt - MAX_STEP), tgt + MAX_STEP)
        m["trim"] = max(-0.14, min(0.14, (t - m["mean"]) / 255.0))
        tgt = m["mean"] + m["trim"] * 255.0
        m["target"] = tgt
        # the trim shifts the two scrim drivers with it
        m["lock"] += m["trim"] * 255.0
        m["eye"] += m["trim"] * 255.0
    return meas


def render_segments(pins):
    shutil.rmtree(SEG, ignore_errors=True)
    os.makedirs(SEG)
    meas = measure_shots()
    for m, (name, prefix, mode, f0, f1, scale, pan, vpan, (z0, z1), sat, warm, shp, jit, drift) \
            in zip(meas, SHOTS):
        # 04b carries a 6-frame handle: the cut into the end card is the one
        # boundary that steps more than +/-8 YAVG (picture -> a navy ground),
        # and a 6 f cross-dissolve is the fix the brief names for exactly that.
        n = f1 - f0 + 1 + (XFADE_F if name == "04b" else 0)
        sha, png, lpng, trim = m["sha"], m["png"], m["lpng"], m["trim"]
        s_raw, smul, vl, ve = m["s_raw"], m["smul"], m["lock"], m["eye"]
        post = m["base"] + (f",eq=brightness={trim:.4f}" if abs(trim) > 0.002 else "")
        z = (f"{z0:.3f}+{z1-z0:.3f}*on/{n}" if z1 >= z0
             else f"{z0:.3f}-{z0-z1:.3f}*on/{n}")
        xs = jx(jit) + (f"+{drift:.1f}*on/{n}" if drift else "")
        zp = (f"zoompan=z='{z}':d={n}:x='{xs}':y='{jy(jit)}'"
              f":s={BW}x{BH}:fps={FPS}")
        vf = f"{zp},scale={VW}:{VH}:flags=lanczos,{post},format=yuv420p"
        run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
             "-loop", "1", "-framerate", str(FPS), "-t", f"{n/FPS:.5f}", "-i", png,
             "-vf", vf, "-frames:v", str(n),
             "-c:v", "libx264", "-crf", "16", "-preset", "slow",
             "-pix_fmt", "yuv420p", "-r", str(FPS), "-an", f"{SEG}/{name}.mp4"])
        pins.append(dict(shot=name, sha=sha, mode=mode, f0=f0, f1=f1,
                         t0=round(f0 / FPS, 3), t1=round((f1 + 1) / FPS, 3),
                         scale=scale, pan=pan, vpan=vpan, push=[z0, z1],
                         brightness_trim=round(trim, 4), pole_sat=sat,
                         graded_sat=round(s_raw, 1), sat_mul=round(smul, 3),
                         lockup_luma=round(vl, 1), lockup_scrim=0.0,
                         eyebrow_luma=round(ve, 1), scrim_peak=0.0))
        print(f"  seg {name:<4} {mode:<4} {sha[:12]} {n:>3}f  trim {trim:+.4f}"
              f"  S {s_raw:5.1f}->{sat} x{smul:.3f}")


XFADE_F = 6                      # the one dissolve: 04b -> end card, f772


def concat_picture():
    run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
         "-i", f"{SEG}/04b.mp4", "-i", f"{SEG}/05.mp4", "-filter_complex",
         f"[0:v][1:v]xfade=transition=fade:duration={XFADE_F/FPS:.5f}"
         f":offset={(SHOTS[-2][4] - SHOTS[-2][3] + 1) / FPS:.5f}[v]",
         "-map", "[v]", "-c:v", "libx264", "-crf", "16", "-preset", "slow",
         "-pix_fmt", "yuv420p", "-r", str(FPS), "-an", f"{SEG}/04b_05.mp4"])
    with open(f"{SEG}/list.txt", "w") as fh:
        for n, *_ in SHOTS:
            if n == "05":
                continue
            fh.write(f"file '{SEG}/{'04b_05' if n == '04b' else n}.mp4'\n")
    run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
         "-f", "concat", "-safe", "0", "-i", f"{SEG}/list.txt",
         "-c", "copy", f"{SEG}/picture.mp4"])


# scrim drive regions, on a 270x480 proxy of the DELIVERED picture (1x/4)
LOCK_ROI = (15, 36, 105, 56)        # x60-420  y144-224
EYE_ROI = (15, 280, 225, 318)       # x60-900  y1120-1272


def measure_scrims(pins):
    """Ground luma, measured on the RENDERED picture one sample per frame,
    before the type layer exists — so nothing here is guessed off a still and
    the zoompan's own travel is included.  It no longer sets a per-shot alpha:
    it sets ONE constant for the whole film, because a scrim is chrome."""
    d = subprocess.run(["ffmpeg", "-v", "error", "-i", f"{SEG}/picture.mp4",
                        "-vf", "scale=270:480,format=gray", "-f", "rawvideo", "-"],
                       capture_output=True).stdout
    W, H = 270, 480
    fr = [d[i * W * H:(i + 1) * W * H] for i in range(len(d) // (W * H))]

    def roi(buf, r):
        x0, y0, x1, y1 = r
        t = n = 0
        for yy in range(y0, y1):
            row = buf[yy * W + x0: yy * W + x1]
            t += sum(row)
            n += len(row)
        return t / max(1, n)

    # Pass 1: what each shot's ground actually is, for the record and for the
    # ONE constant.  Nothing here becomes a per-shot alpha any more.
    worst_eye, card_shots = 0.0, []
    for m, (name, _p, mode, f0, f1, *_r) in zip(pins, SHOTS):
        vl = max(roi(fr[f], LOCK_ROI) for f in range(f0, min(f1 + 1, len(fr))))
        ve = max(roi(fr[f], EYE_ROI) for f in range(f0, min(f1 + 1, len(fr))))
        carries = mode != "card" and any(
            not (SCHED[k][1] + OUT_F + 6 < f0 or SCHED[k][0] > f1)
            for k in SCHED)
        if carries:
            worst_eye = max(worst_eye, ve)
            card_shots.append((f0, f1))
        m["lockup_luma"], m["eyebrow_luma"] = round(vl, 1), round(ve, 1)
        m["carries_card"] = carries
        print(f"  ground {name:<4} lockup {vl:5.1f}   eyebrow {ve:5.1f}"
              f"   card {'yes' if carries else 'no'}")

    # Pass 2: ONE lower value, held across the WHOLE PICTURE SECTION — not just
    # the beats that carry a card.  Round 6 switched it per card-carrying shot,
    # which is what produced the transitions at f277/f332/f662 the critic
    # measured as pumps.  Held flat there is exactly ONE transition in the
    # film, at the cut into the end card, and it is a step, not a ramp.
    # Directive B's floor is 0.55; it is raised only if a measured ground under
    # a real eyebrow needs more, and the delivered ratio is printed either way.
    peak = max(0.55, min(0.90, need_alpha(worst_eye, EYE_TARGET, 0.90)))
    on = [f < CARD_IN for f in range(NF)]
    _snap(SCRIM_M, on, peak)
    _snap(LOCK_A, on, TOP_A)
    # the film's ONE dissolve is the picture cut into the end card.  Both
    # scrims ride it out across exactly those 6 frames, so the chrome leaves
    # WITH the picture it belongs to rather than stepping off a static frame.
    for i in range(XFADE_F):
        f = CARD_IN + i
        if f < NF:
            k = 1.0 - (i + 1) / XFADE_F
            SCRIM_M[f], LOCK_A[f] = peak * k, TOP_A * k
    for m in pins:
        m["lockup_scrim"] = TOP_A if m["shot"] != "05" else 0.0
        m["scrim_peak"] = 0.0 if m["shot"] == "05" else round(peak, 3)
    edges = [f for f in range(1, NF) if on[f] != on[f - 1]]
    print(f"  lower scrim: ONE value {peak:.2f} (worst eyebrow ground "
          f"{worst_eye:.1f}), transitions at {edges} — all cut frames")
    print(f"  top scrim:   ONE value {TOP_A:.2f}, solid to y{TOP_FULL}, "
          f"linear to 0 by y{TOP_FADE}; off on the flat card")


def _snap(track, on, value):
    """Piecewise constant, switching only where `on` switches — which is only
    ever a cut frame — with a SNAP_F ramp that COMPLETES BY the cut going off
    and starts ON the cut going on.  f0 starts at full: round 5 ramped the
    lower scrim in over f0-f10 and dropped the most-viewed third of a second in
    the file by 7.2 levels per frame with no cut and no type on screen."""
    for f in range(NF):
        track[f] = value if on[f] else 0.0
    if SNAP_F <= 0:
        return                                          # step ON the cut frame
    for c in range(1, NF):
        if on[c] == on[c - 1]:
            continue
        if on[c - 1] and not on[c]:                     # going off
            for i in range(SNAP_F):
                f = c - SNAP_F + i
                if f >= 0:
                    track[f] = value * (1.0 - (i + 1) / SNAP_F)
        else:                                           # coming on
            for i in range(SNAP_F):
                if c + i < NF:
                    track[c + i] = value * (i + 1) / SNAP_F


def overlay():
    run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
         "-i", f"{SEG}/picture.mp4",
         "-framerate", str(FPS), "-i", f"{STRAPS}/t_%04d.png",
         "-filter_complex",
         "[0:v][1:v]overlay=0:0:format=auto,format=yuv420p[v]",
         "-map", "[v]", "-frames:v", str(NF),
         "-c:v", "libx264", "-crf", "16", "-preset", "slow",
         "-pix_fmt", "yuv420p", "-r", str(FPS), "-an",
         "-movflags", "+faststart", SILENT])


def mux():
    # -2 dB from just after the card lands (f772 = 25.733 s): the card is
    # quieter than the film, so the last thing you hear is the room getting
    # smaller behind the phone number.  The 28.5 s tail still decays to
    # silence at 30.000 under the CTA.
    pre = ("atrim=0:30,afade=t=in:d=0.5,"
           "volume='if(gte(t,26.0),0.794,1.0)':eval=frame,"
           "afade=t=out:st=28.5:d=1.5")
    p = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", BED, "-af",
         pre + ",loudnorm=I=-14:TP=-1.5:LRA=9:print_format=json",
         "-f", "null", "-"], capture_output=True, text=True)
    d = json.loads(re.search(r"\{[^{]*input_i.*?\}", p.stderr, re.S).group(0))
    with open(f"{LOGS}/loudnorm_pass1.json", "w") as fh:
        json.dump(d, fh, indent=2)
    meas = ("measured_I={input_i}:measured_TP={input_tp}:measured_LRA={input_lra}"
            ":measured_thresh={input_thresh}:offset={target_offset}").format(**d)
    run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
         "-i", SILENT, "-i", BED, "-filter_complex",
         f"[1:a]{pre},loudnorm=I=-14:TP=-1.5:LRA=9:{meas}:linear=true,"
         f"volume=-0.6dB,alimiter=limit=0.841:level=disabled[a]",
         "-map", "0:v", "-map", "[a]", "-c:v", "copy",
         "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
         "-t", "30", "-movflags", "+faststart", FINAL])


# ═════════════════════════════════════════════════════════════════════════════
# 8.  PROOF
# ═════════════════════════════════════════════════════════════════════════════
#   sampled inside every card's HOLD (all elements at full opacity), plus the
#   thumbnail frame, both sides of the money cut, and the CTA's 4 s hold.
QC_T = (0.00, 0.17, 0.33, 1.00, 3.00, 5.00, 7.00, 8.50, 10.50, 12.00,
        13.50, 15.00, 16.00, 17.50, 19.50, 21.50, 23.00, 25.00,
        26.50, 28.00, 29.60)


def grab(src, t, dst, scale=None):
    vf = f"scale={scale}" if scale else "null"
    run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error", "-ss", f"{t}",
         "-i", src, "-frames:v", "1", "-vf", vf, "-q:v", "2", dst])


def contrast_ratio(v):
    c = v / 255.0
    lin = c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return lin


def wcag(l_text, l_ground):
    """Direction-agnostic.  Bronze (L 0.348) can sit on a ground either side of
    itself; the old form assumed the text was always the lighter one and would
    have under-reported a light-ground failure as a pass."""
    hi, lo = max(l_text, l_ground), min(l_text, l_ground)
    return (hi + 0.05) / (lo + 0.05)


def proof():
    shutil.rmtree(QC, ignore_errors=True)
    os.makedirs(QC)
    for t in QC_T:
        grab(FINAL, t, f"{QC}/t_{t:05.2f}.jpg")
    with open(f"{LOGS}/probe.txt", "w") as fh:
        fh.write(subprocess.run(
            ["ffprobe", "-v", "error", "-select_streams", "v:0", "-count_frames",
             "-show_entries", "stream=nb_read_frames,r_frame_rate,width,height,pix_fmt",
             "-show_entries", "format=duration", "-of", "default=nw=1", FINAL],
            capture_output=True, text=True).stdout)
    p = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", FINAL,
                        "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True)
    open(f"{LOGS}/loudness.txt", "w").write(p.stderr[-2500:])
    # 0.25 is the strict count; 0.10 is the like-for-like number, because the
    # shipped master only reports its own 6.433 s cut at 0.10.
    for tag, crop, th in (("full", "null", 0.25), ("band", "crop=1080:972:0:480", 0.25),
                          ("full_010", "null", 0.10)):
        p = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", FINAL,
                            "-vf", f"{crop},select='gt(scene,{th})',showinfo",
                            "-f", "null", "-"], capture_output=True, text=True)
        ts = re.findall(r"pts_time:([\d.]+)", p.stderr)
        open(f"{LOGS}/scenes_{tag}.txt", "w").write("\n".join(ts))
        print(f"  scene changes ({tag}):", [round(float(x), 3) for x in ts])
    # Delivered contrast, on the delivered frames.  GROUND ONLY: the type's own
    # alpha is used as a hole-punch, because averaging cream glyphs into the
    # "ground" mean biases it up and reports the film as safer than it is.
    #  EVERY TEXT ELEMENT, PER ELEMENT, ON ITS OWN INK ROW.  Round 5 looped
    #  only the lockup and the eyebrows — which is exactly why a build calling
    #  itself measured shipped the locked CTA at 3.64:1 and the end title at
    #  3.93:1 mean / 1.72:1 worst-local.  Every date line is now measured at
    #  ITS OWN y, not inside one band that a row scan can miss.
    L_CREAM, L_BRONZE = 0.930, 0.348
    #  cta_number carries directive A's own floor, 7:1, not the 4.5 the rest of
    #  the film holds — it is the only element the whole piece exists to make
    #  legible.  The lockup keeps 6.0 because it sits on live picture.
    FLOOR = {"lockup": 6.0, "cta_number": 7.0}
    masks, boxes, lum = {}, {}, {}
    for e in ELEMENTS:
        a = e["im"].split()[3]
        bb = a.getbbox()
        if bb is None or e["name"].endswith(("_rule", "ruleA", "ruleB",
                                             "lockup_tick")):
            continue                      # ornament, not text — no text floor
        mk = Image.new("L", (VW, VH), 255)
        mk.paste(0, (0, 0), a.point(lambda v: 255 if v >= 8 else 0))
        masks[e["name"]] = mk
        boxes[e["name"]] = (max(0, bb[0] - 6), max(0, bb[1] - 4),
                            min(VW, bb[2] + 6), min(VH, bb[3] + 4))
        # end_tag is BRONZE now (the master's TIMELINE_CARD sets it in copper),
        # so it must be measured as bronze.  Round 6 would have measured a
        # bronze glyph against cream's luminance and reported a pass it did
        # not have.
        lum[e["name"]] = (L_BRONZE if (e["name"].endswith("_eyebrow")
                                       or e["name"] == "end_tag") else L_CREAM)

    def masked_stats(gray, mask, box):
        """mean and WORST-LOCAL (16x16 tile max) ground under an element."""
        g, mk = gray.crop(box), mask.crop(box)
        w, h = g.size
        gd, md = list(g.getdata()), list(mk.getdata())
        tot = n_ = 0
        worst = 0.0
        for ty in range(0, h, 16):
            for tx in range(0, w, 16):
                s = c = 0
                for yy in range(ty, min(ty + 16, h)):
                    base = yy * w
                    for xx in range(tx, min(tx + 16, w)):
                        if md[base + xx] > 127:
                            s += gd[base + xx]
                            c += 1
                if c >= 24:
                    worst = max(worst, s / c)
                tot += s
                n_ += c
        return tot / max(1, n_), worst

    lines, fails = [], []
    worst_by = {}
    for t in QC_T:
        f = int(round(t * FPS))
        im = Image.open(f"{QC}/t_{t:05.2f}.jpg").convert("L")
        for e in ELEMENTS:
            n = e["name"]
            if n not in masks or alpha_at(e, f)[0] <= 0.9:
                continue
            mean, wl = masked_stats(im, masks[n], boxes[n])
            r = wcag(lum[n], contrast_ratio(mean))
            rw = wcag(lum[n], contrast_ratio(wl))
            floor = FLOOR.get(n, 4.5)
            lines.append(f"t={t:5.2f}  {n:<12} ground mean={mean:6.1f} "
                         f"worst16={wl:6.1f}  ratio {r:6.2f}:1  "
                         f"worst-local {rw:5.2f}:1  floor {floor:.1f}  "
                         f"{'ok' if rw >= floor else 'FAIL'}")
            if n not in worst_by or rw < worst_by[n][1]:
                worst_by[n] = (r, rw, floor)
            if rw < floor:
                fails.append(f"{n}@t={t}")
    # DIRECTIVE B — the table, by card, at each element's hold frame.
    CARD_OF = {"s1": "card 1  DRAWDOWN 2026", "s2": "card 2  ABOUT 10 FEET",
               "s3": "card 3  TWO AMPHIBIOUS TRUXORS",
               "s4": "card 4  WE WORK THE BED"}

    def card_of(n):
        if n.startswith(("s1", "s2", "s3", "s4")):
            return CARD_OF[n[:2]]
        if n.startswith(("cta_", "end_")):
            return "card 5  END CARD"
        return "all cards  (held f0-f899)"

    tbl = ["| card | element | ratio (mean ground) | ratio (worst-local 16x16)"
           " | floor | pass |", "|---|---|---|---|---|---|"]
    for k, v in sorted(worst_by.items(), key=lambda kv: (card_of(kv[0]), kv[0])):
        tbl.append(f"| {card_of(k)} | `{k}` | {v[0]:.2f}:1 | **{v[1]:.2f}:1** "
                   f"| {v[2]:.1f} | {'PASS' if v[1] >= v[2] else 'FAIL'} |")
    open(f"{LOGS}/contrast.txt", "w").write(
        "\n".join(lines) + "\n\nWORST PER ELEMENT (worst-local 16x16 tile)\n" +
        "\n".join(f"  {k:<12} mean {v[0]:6.2f}:1   worst-local {v[1]:5.2f}:1"
                  f"   floor {v[2]:.1f}   {'ok' if v[1] >= v[2] else 'FAIL'}"
                  for k, v in sorted(worst_by.items())) +
        "\n\nDIRECTIVE B TABLE\n\n" + "\n".join(tbl) + "\n")
    open(f"{LOGS}/contrast_table.md", "w").write("\n".join(tbl) + "\n")
    # DIRECTIVE A — the phone number, measured against the ground rows behind
    # its own ink on the aerial-under-navy card.  Floor is 7:1, not 4.5:1.
    cta_r, cta_wl, _ = worst_by.get("cta_number", (0.0, 0.0, 7.0))
    print(f"  DIRECTIVE A — cta_number vs its own ground rows: "
          f"mean {cta_r:.2f}:1 · worst-local {cta_wl:.2f}:1 "
          f"(floor 7.0) {'PASS' if cta_wl >= 7.0 else 'FAIL'}")
    worst_l = worst_by.get("lockup", (0, 99, 6))[1]
    worst_e = min([v[1] for k, v in worst_by.items()
                   if k.endswith("_eyebrow")] or [99.0])
    worst_cta = min([v[1] for k, v in worst_by.items()
                     if k.startswith(("cta_", "end_"))] or [99.0])
    print(f"  contrast — {len(worst_by)} text elements x {len(QC_T)} frames."
          f"  lockup {worst_l:.2f}:1 (floor 6.0) · eyebrow {worst_e:.2f}:1"
          f" · end card {worst_cta:.2f}:1 (floor 4.5)")
    print("  contrast FAILURES:", fails if fails else "none")
    # motion + loop seam
    p = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", FINAL,
                        "-vf", "scale=108:192,signalstats,metadata=print:key=lavfi"
                        ".signalstats.YAVG", "-f", "null", "-"],
                       capture_output=True, text=True)
    y = [float(v) for v in re.findall(r"YAVG=([\d.]+)", p.stderr)]
    open(f"{LOGS}/yavg.txt", "w").write("\n".join(f"{i} {v:.2f}"
                                                  for i, v in enumerate(y)))
    if len(y) >= NF:
        steps = [(i, round(y[i] - y[i - 1], 1))
                 for i in (167, 277, 387, 497, 607, 717, 772) if i < len(y)]
        print("  YAVG step at each cut:", steps)
        print(f"  loop seam f0={y[0]:.1f} f899={y[-1]:.1f} "
              f"step={y[0]-y[-1]:+.1f}")
        # DIRECTIVE C — frame 0 is the thumbnail, so the opening must not ramp
        # its exposure.  Whole-frame YAVG over f0-f10 flat within +-2.
        head = y[:11]
        print("  DIRECTIVE C — YAVG f0/f5/f10 = "
              f"{y[0]:.2f} / {y[5]:.2f} / {y[10]:.2f}  spread f0-f10 "
              f"{max(head)-min(head):+.2f} (floor +-2.0) "
              f"{'PASS' if max(head)-min(head) <= 2.0 else 'FAIL'}")
        open(f"{LOGS}/yavg_head.txt", "w").write(
            "\n".join(f"f{i} {v:.2f}" for i, v in enumerate(head)) + "\n")
    # motion: mean inter-frame diff on a 108x192 gray, per 5 s window.  The
    # last 6 s is the number the critic pinned (v2 round 4 = 0.153, v1 = 0.914).
    #  DIRECTIVE E — measured ON THE PICTURE BAND (crop 1080x972 at y480, the
    #  fit band, quarter-scaled to 270x243 gray), one number per 1 s window.
    #  Quarter scale is declared because the number is resolution-dependent:
    #  at native resolution `noise=alls=3` grain alone puts a floor under it
    #  and the metric stops measuring the camera.
    def band_motion(src):
        d = subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-vf",
                            "crop=1080:972:0:480,scale=270:243,format=gray",
                            "-f", "rawvideo", "-"], capture_output=True).stdout
        fs = 270 * 243
        fr = [d[i * fs:(i + 1) * fs] for i in range(len(d) // fs)]
        out = []
        for s in range(30):
            idx = range(max(1, s * FPS), min(len(fr), (s + 1) * FPS))
            v = [sum(abs(p - q) for p, q in zip(fr[i], fr[i - 1])) / fs
                 for i in idx]
            out.append(round(sum(v) / max(1, len(v)), 2))
        return out

    #  Two numbers, because they answer two different questions.  `picture` is
    #  the camera — the picture band with no chrome on it.  `delivered` is that
    #  same band seen through the lower scrim, which by design darkens rows
    #  1070-1420 and therefore suppresses any measurement taken through it.
    #  Directive E's floor is held on the DELIVERED file; the picture number is
    #  printed so the scrim's cost is visible rather than hidden.
    per_s = band_motion(FINAL)
    pic_s = band_motion(f"{SEG}/picture.mp4")
    open(f"{LOGS}/motion.txt", "w").write(
        "band |dframe| per 1 s window (crop 1080x972@y480 -> 270x243 gray)\n"
        "  s   delivered   picture-only\n" +
        "\n".join(f"{s:2d}-{s+1:2d}s   {a:6.2f}      {b:6.2f}"
                  for s, (a, b) in enumerate(zip(per_s, pic_s))) + "\n")
    print("  band |dframe| per 1 s window (delivered):", per_s)
    print("  band |dframe| per 1 s window (picture)  :", pic_s)
    pay_f = [s for s in SHOTS if s[0].startswith("03")]         # 03a..03b
    t0, t1 = pay_f[0][3] // FPS, pay_f[-1][4] // FPS
    pay, payp = per_s[t0:t1 + 1], pic_s[t0:t1 + 1]
    print(f"  DIRECTIVE E — payoff beat s{t0}-s{t1} delivered {pay} "
          f"min {min(pay)} · picture {payp} min {min(payp)} "
          f"(floor 1.0) {'PASS' if min(pay) >= 1.0 else 'FAIL'}")
    grab(FINAL, 15.00, os.path.join(OUT, "LCD_v2_916_COVER.jpg"))
    return y


def before_after():
    for t in (1, 5, 15, 28):
        grab(MASTER, t, f"{QC}/v1_{t}.jpg")
        grab(FINAL, t, f"{QC}/v2_{t}.jpg")
    CW_, CH_ = 400, 711
    pad, hdr = 14, 46
    sheet = Image.new("RGB", (pad + 4 * (CW_ + pad), hdr + 2 * (CH_ + hdr + pad)),
                      (18, 20, 24))
    d = ImageDraw.Draw(sheet)
    f_lab, f_row = font(SANS7, 22), font(SANS7, 26)
    for r, (tag, pre) in enumerate((("v1  SHIPPED MASTER", "v1"),
                                    ("v2  ROUND 4", "v2"))):
        ry = hdr + r * (CH_ + hdr + pad)
        d.text((pad, ry - 34), tag, font=f_row, fill=(232, 226, 216))
        for c, t in enumerate((1, 5, 15, 28)):
            im = Image.open(f"{QC}/{pre}_{t}.jpg").convert("RGB").resize((CW_, CH_))
            x = pad + c * (CW_ + pad)
            sheet.paste(im, (x, ry))
            d.rectangle([x, ry + CH_ - 34, x + CW_, ry + CH_], fill=(0, 0, 0))
            d.text((x + 10, ry + CH_ - 30), f"{pre}  t = {t}.0 s", font=f_lab,
                   fill=(240, 236, 228))
    sheet.save(os.path.join(OUT, "BEFORE_AFTER.png"))


def tiktok_proof():
    grab(FINAL, 28.0, f"{QC}/tt.jpg")
    im = Image.open(f"{QC}/tt.jpg").convert("RGB")
    ov = Image.new("RGBA", im.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(ov)
    red = (220, 30, 40, 115)
    for box in ([0, 0, VW, 140], [0, VH - 484, VW, VH], [0, 0, 60, VH],
                [VW - 180, 0, VW, VH]):
        d.rectangle(box, fill=red)
    out = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
    d2 = ImageDraw.Draw(out)
    d2.text((70, VH - 460), "TikTok dead zones  top 140 / bottom 484 / left 60"
            " / right 180 — no text pixel is inside red",
            font=font(SANS7, 22), fill=(255, 255, 255))
    out.save(os.path.join(OUT, "tiktok_proof.png"))
    bad = [n for n, b in BBOXES
           if b[1] < 140 or b[3] > VH - 484 or b[0] < 60 or b[2] > VW - 180]
    print("  tiktok dead-zone check:", "CLEAR" if not bad else f"VIOLATIONS {bad}")
    return bad


def write_pins(pins, deepest, y):
    md5 = lambda p: subprocess.run(["md5", "-q", p], capture_output=True,
                                   text=True).stdout.strip()
    L = ["# LCD v2 — PINS (round 4)", "",
         "pole         ENEMY (declared; the grade travels inside it)",
         f"bed          {BED}  offset 0.0 s  "
         "(waveform r=1.0000 vs the shipped master; v1 correlates r=0.014)",
         f"master ref   {MASTER}  md5 {md5(MASTER)}",
         f"grid         {BPM} BPM · beat {BEAT:.6f}s · bar {BAR:.6f}s · phase +{PHASE}s",
         f"downbeats/f  {DOWNBEATS}",
         f"cuts (hard)  {CUTS}   — bar counts 3/2/2/2/2/1/1, then the card",
         f"rule module  {RULE_W} px drawn x {RULE_H} px, EVERY rule in the film"
         " including the lockup's (directive D: one length everywhere).  A"
         " picture rule's alpha bbox is wider and 40 px tall because of"
         " GaussianBlur(8) on its shadow — the DRAWN constant is the module,"
         " and the end-card rules carry no shadow at all.",
         f"lockup rule  the same {RULE_W} px bronze module, ABOVE the wordmark",
         f"scrims       top {TOP_A} constant (y{TOP_FULL} solid, linear to 0 by"
         f" y{TOP_FADE}); lower ONE constant held across the whole picture"
         " section.  Exactly one transition in the film, at f772, and it rides"
         " the 6 f dissolve into the end card.  No ramp on any cut.",
         "", "## fonts (absolute, ImageFont.truetype)", ""]
    L += [f"  {p}" for p in (SERIF, SANS7, SANS4)]
    L += ["", "  Two families.  DM Serif Text 400 for headlines and the end-card",
          "  title; DM Sans 700 for the lockup, eyebrows, the tag, the CTA lead",
          "  and the phone number; DM Sans 400 for the end-card dates and the",
          "  one note row (directive D).  No Arial anywhere."]
    L += ["", "## picture", "",
          "| shot | sha256 | mode | frames | t | scale | pan | push | eq trim |"
          " S in | S pole | S × | lockup luma | top scrim | eyebrow luma | scrim peak |",
          "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for p in pins:
        L.append("| {shot} | `{sha}` | {mode} | {f0}–{f1} | {t0}–{t1} | {scale} |"
                 " {pan}/{vpan} | {push} | {brightness_trim:+.4f} | {graded_sat} |"
                 " {pole_sat} | {sat_mul} | {lockup_luma} | {lockup_scrim} |"
                 " {eyebrow_luma} | {scrim_peak} |".format(**p))
    L += ["", "## type — per-element INK bbox (pre-shadow) and alpha bbox", "",
          "| element | ink x0 | ink y0 | ink x1 | ink y1 | ink w |"
          " alpha y1 | headroom to 1436 |",
          "|---|---|---|---|---|---|---|---|"]
    ib = dict(INKBOX)
    for n, b in BBOXES:
        k = ib.get(n, b)
        L.append(f"| {n} | {k[0]} | {k[1]} | {k[2]} | {k[3]} | {k[2]-k[0]} |"
                 f" {b[3]} | {1436-b[3]} |")
    L += ["", f"deepest ink  y = {deepest}", ""]
    if y:
        L += [f"loop seam    f0 YAVG {y[0]:.1f} · f899 YAVG {y[-1]:.1f} ·"
              f" step {y[0]-y[-1]:+.1f}", ""]
    L += [f"md5 {os.path.basename(FINAL)}   {md5(FINAL)}",
          f"md5 {os.path.basename(SILENT)}  {md5(SILENT)}", ""]
    open(os.path.join(OUT, "PINS.md"), "w").write("\n".join(L))


# ═════════════════════════════════════════════════════════════════════════════
def main():
    for d in (OUT, STRAPS, SEG, QC, LOGS):
        os.makedirs(d, exist_ok=True)
    assert os.path.exists(BED), BED
    guard()
    deepest = build_elements()
    pins = []
    print("segments:")
    render_segments(pins)
    concat_picture()
    print("scrims:")
    measure_scrims(pins)           # exact, on the rendered picture
    bake_type()                    # …which bake_type consumes
    overlay()
    mux()
    print("proof:")
    y = proof()
    before_after()
    bad = tiktok_proof()
    write_pins(pins, deepest, y)
    nb = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0",
                         "-count_frames", "-show_entries",
                         "stream=nb_read_frames", "-of", "csv=p=0", FINAL],
                        capture_output=True, text=True).stdout.strip().strip(",")
    dur = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                          "format=duration", "-of", "csv=p=0", FINAL],
                         capture_output=True, text=True).stdout.strip()
    print(f"\nWROTE {FINAL}\n  frames {nb}  duration {dur}  deepest ink y={deepest}")
    if nb != str(NF):
        raise SystemExit(f"FRAME COUNT {nb} != {NF}")
    if bad:
        raise SystemExit("dead-zone violations: " + ", ".join(bad))


if __name__ == "__main__":
    main()
