# HERMES QC — Turnkey (Claude Gate, not a recut)

**2026-09-07 19:30.** Two Hermes chats (`140924_7b83fa` this desk + `145230_83e616` studio) both edited `build_turnkey.py`. That stops now. Claude owns Gate-OK. Hermes does not rebuild.

## Lock

- Do **not** run `python3 build_turnkey.py` unless a beat FAILs C7 and you log why.
- Do **not** t2v. Do **not** swap plates unless a named house is in frame.
- Do **not** post. Do **not** Vercel. Nate Gate 3 after you stamp.

## Cut on disk

| File | Notes |
|------|--------|
| `DRAWDOWN_Turnkey_916_STUDIO.mp4` | silent, ~18s, 1080×1920 |
| `DRAWDOWN_Turnkey_916_SUNO_BED.mp4` | Mud Window v2 mux, desk `public/media/turnkey-studio.mp4` |
| Builder | `build_turnkey.py` |

## Beats to OK

| t | Beat | Plate | Strap | QC frame |
|---|------|-------|-------|----------|
| ~1.2 | permits | `153d39cdb0eb` bleed | YOU DON'T FILE A THING / WE HANDLE COA & LCRA | `resolve/turnkey/qc/QC_turnkey_t1.2.png` |
| ~5.0 | crew | `c6b6853c038a` FIT | OUR CREW. OUR IRON. / AMPHIBIOUS TRUXORS | `resolve/turnkey/qc/QC_turnkey_t5.0.png` |
| ~8.8 | haul 1 | `83f97f1642cd` **bleed ax=0.90** | OFF THE BARGE. | `resolve/turnkey/qc/QC_turnkey_t8.8.png` |
| ~12.5 | haul 2 | `5e85f06eda86` bleed portrait | INTO THE TRAILER. / GONE OFF YOUR LOT. | `resolve/turnkey/qc/QC_turnkey_t12.5.png` |
| ~16.5 | close | `870b907f2401` bleed | WE RUN IT. YOU DON'T. / 254-780-6971 | `resolve/turnkey/qc/QC_turnkey_t16.5.png` |

Nate 2026-09-07: pickup bed `c30cdc0fe978` is **banned**. Haul is barge → Load Trail, then packed trailer. `@two_machines` barge pin banned. No $695. COVER/tarp is not this cut.

## What we already eyeballed

- t5.0: two Truxors, pontoons, FIT letterbox, C7 holds.
- t8.8: LOAD TRAIL body + barge pile both read (right-bias). Last letter of the brand is tight on the right edge.
- t12.5: standing in packed dump bed, lake ahead, no named house. Porta-john on a barge in the background — shop, not a customer lot.

## Claude deliverable

Write `weeks/2026-08-31/GATE3_TURNKEY.md`:

```
Verdict: PASS | FAIL
Per beat: PASS/FAIL + one line
If FAIL: which frame, which claim, stop. Do not rebuild until Nate says.
If PASS: ready for Nate Gate 3. Do not mark posted.
```

Append one paragraph to `weeks/2026-08-31/BOARD.md`. Do not rewrite the board.
