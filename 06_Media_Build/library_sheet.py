"""Render a numbered contact sheet from a SQL query against library.db.

Usage: python3 sheet.py <out_name> <limit> "<where clause>"
Indices drawn on each tile map to the printed sha list, so picks can be made by
number. EXIF orientation is normalized — the archive has rotated phone shots.
"""
import os
import sqlite3
import sys

from PIL import Image, ImageDraw, ImageFont, ImageOps

DB = os.path.expanduser("~/Poseidon/visual-library/library.db")
PHOTOS = os.path.expanduser("~/Poseidon/visual-library/photos")
FONT = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"

out, limit, where = sys.argv[1], int(sys.argv[2]), sys.argv[3]

con = sqlite3.connect(DB)
rows = con.execute(f"""
    SELECT r.sha256, COALESCE(s.label,''), substr(COALESCE(c.caption,''),1,90)
    FROM refs r
    LEFT JOIN vlm_captions c ON c.ref_id = r.id
    LEFT JOIN subject_final s ON s.ref_id = r.id
    WHERE {where}
    ORDER BY r.filesize DESC LIMIT {limit}
""").fetchall()

TW, TH, COLS = 360, 270, 4
grid = [r for r in rows if os.path.exists(os.path.join(PHOTOS, r[0] + ".jpg"))]
n_rows = (len(grid) + COLS - 1) // COLS
sheet = Image.new("RGB", (TW * COLS, TH * n_rows), (18, 18, 18))
d = ImageDraw.Draw(sheet)
f = ImageFont.truetype(FONT, 30)

for i, (sha, label, cap) in enumerate(grid):
    im = Image.open(os.path.join(PHOTOS, sha + ".jpg"))
    im = ImageOps.exif_transpose(im)          # archive has rotated phone shots
    im.thumbnail((TW, TH))
    ox, oy = (i % COLS) * TW, (i // COLS) * TH
    sheet.paste(im, (ox + (TW - im.width) // 2, oy + (TH - im.height) // 2))
    d.rectangle([ox + 4, oy + 4, ox + 52, oy + 42], fill=(0, 0, 0, 220))
    d.text((ox + 12, oy + 8), str(i + 1), font=f, fill=(255, 214, 120))

sheet.save(f"{out}.jpg", quality=88)
for i, (sha, label, cap) in enumerate(grid):
    print(f"{i+1}\t{sha[:12]}\t{label}\t{cap}")
