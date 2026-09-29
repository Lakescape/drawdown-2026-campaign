# 06_Media_Build — agent notes

## ffmpeg still-image builds
- `-loop 1 -framerate 30 -i still.jpg` — always set `-framerate` to match `zoompan fps=`. Default is 25 fps, so each beat runs 5/6 length, `xfade` offsets overrun, and later beats silently repeat the last plate. ffmpeg still exits 0.
- Exit 0 plus the right duration is not proof. Extract frames at t=1, mid-beat of each beat, and the last frame (`ffmpeg -ss T -i out.mp4 -frames:v 1 qc.png`), then look at them.
- Final CTA card: no alpha `fade=t=out`, so the phone number holds to the last frame.

## Plates and claims
- QC rejects any card that claims something the crop removed (C7-class). Example: "UNDER YOUR DOCK" over a bleed crop that cut the dock out.
- `bleed` = cover-crop. `fit` = letterbox, only when a cover-crop drops a machine and breaks the C7 two-machine count. Do not "fix" FIT plates by cropping.
- Verify handoff pins against Poseidon before use: `sqlite3 ~/Poseidon/visual-library/library.db "select caption,vlm_label from vlm_captions where ref_id like '<sha12>%'"`.
- On-screen text needs a row in `../MEDIA_ClaimLedger_Drawdown_v1.md`. If a brief line has no row, write the conflict in the week's BOARD.md. Never swap it silently.

## Files
- Never overwrite another lane's mp4. New slug per build. Retire with a `_RETIRED-<reason>-<date>` rename, never a delete.
