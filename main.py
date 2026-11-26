#!/usr/bin/env python3
"""Spotlight @crisxai5 — creative generator for the make.fun bounty
"Spotlight @crisxai5: AI & Crypto Expert on X".

Original work, written for this entry. It does two things:

1. Draws an original, phone-readable spotlight card (1080x1350) with PIL
   and saves it as ``spotlight.png`` — the image to attach to the X post.
2. Writes the recommended post copy (a short intro / recommendation
   focused on @crisxai5 as an AI & crypto expert) to ``entry.txt``.

Both files go to ``$MAKEFUN_OUTPUT_DIR`` (default ``/output``).

Run locally:
    MAKEFUN_OUTPUT_DIR=output python3 main.py

NOTE: entry.txt carries a ``[MAKEFUN-PLAY-CODE]`` placeholder. Before
posting, replace it with one of the account's real play codes from
GET /api/competitions/u-tina-spotlight-crisxai5-ai-crypto-expert-on-x-7c1ed9ad/play-code.
Never invent a code — a made-up code fails the gate.
"""

import os
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

HANDLE = "@crisxai5"
PROFILE_URL = "https://x.com/crisxai5"

# Recommended post copy: punchy, authentic, under 280 characters.
# Play-code placeholder MUST be replaced with a real code before posting.
POST_COPY = (
    "One follow that upgrades your whole timeline.\n\n"
    "@crisxai5 breaks down AI agents, crypto insights & Web3 innovation "
    "\u2014 practical signal, no hype.\n\n"
    "If AI x crypto is your edge, this is the follow.\n"
    "https://x.com/crisxai5\n\n"
    "#AI #Crypto #AIAgents #Web3\n"
    "[MAKEFUN-PLAY-CODE]"
)

PILLARS = [
    ("AI AGENTS", "Practical agent workflows, explained simply."),
    ("CRYPTO INSIGHTS", "Signal over noise on the market that matters."),
    ("WEB3 INNOVATION", "On-chain automation and what's next."),
]

CARD_W, CARD_H = 1080, 1350
BG_TOP = (13, 18, 38)
BG_BOTTOM = (24, 10, 46)
ACCENT = (56, 224, 255)
ACCENT2 = (167, 120, 255)
CARD_BG = (255, 255, 255)
INK = (16, 22, 40)
MUTED = (90, 100, 125)
WHITE = (255, 255, 255)


def _font(bold: bool, size: int) -> ImageFont.FreeTypeFont:
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold
        else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            continue
    return ImageFont.load_default()


def _gradient(size):
    base = Image.new("RGB", size, BG_TOP)
    top = Image.new("RGB", size, BG_TOP)
    bottom = Image.new("RGB", size, BG_BOTTOM)
    mask = Image.linear_gradient("L").resize(size)
    return Image.composite(bottom, top, mask)


def draw_card() -> Image.Image:
    """Draw the 1080x1350 spotlight card. All art is generated here."""
    img = _gradient((CARD_W, CARD_H))
    d = ImageDraw.Draw(img, "RGBA")

    # Accent rings around a monogram badge.
    cx, cy, r = CARD_W // 2, 280, 130
    d.ellipse([cx - r - 26, cy - r - 26, cx + r + 26, cy + r + 26],
              outline=ACCENT2, width=4)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255, 22),
              outline=ACCENT, width=6)
    d.text((cx, cy - 8), "C5", font=_font(True, 120), fill=WHITE, anchor="mm")
    d.text((cx, cy + 180), "AI x CRYPTO", font=_font(True, 32),
           fill=ACCENT, anchor="mm")

    d.text((CARD_W // 2, 540), "MUST-FOLLOW ON X", font=_font(True, 44),
           fill=ACCENT2, anchor="mm")
    d.text((CARD_W // 2, 625), HANDLE, font=_font(True, 118),
           fill=WHITE, anchor="mm")
    d.text((CARD_W // 2, 712), "AI & Crypto Expert",
           font=_font(True, 56), fill=WHITE, anchor="mm")
    d.text((CARD_W // 2, 770),
           "AI agents  \u00b7  crypto insights  \u00b7  Web3 innovation",
           font=_font(False, 32), fill=(200, 210, 235), anchor="mm")

    # Three pillar cards.
    y = 850
    for title, desc in PILLARS:
        d.rounded_rectangle([70, y, CARD_W - 70, y + 128], radius=24,
                            fill=CARD_BG)
        d.rectangle([70, y, 86, y + 128], fill=ACCENT)
        d.text((116, y + 26), title, font=_font(True, 40), fill=INK)
        wrapped = textwrap.fill(desc, width=46)
        d.text((116, y + 76), wrapped, font=_font(False, 29), fill=MUTED)
        y += 148

    d.text((CARD_W // 2, 1300), "FOLLOW @crisxai5  \u00b7  x.com/crisxai5",
           font=_font(True, 34), fill=(200, 210, 235), anchor="mm")
    return img


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    card = draw_card()
    card.save(OUT_DIR / "spotlight.png")
    (OUT_DIR / "entry.txt").write_text(POST_COPY + "\n", encoding="utf-8")
    print(f"Wrote {OUT_DIR / 'spotlight.png'} ({CARD_W}x{CARD_H})")
    print(f"Wrote {OUT_DIR / 'entry.txt'} "
          f"({len(POST_COPY)} chars of post copy)")


if __name__ == "__main__":
    main()
