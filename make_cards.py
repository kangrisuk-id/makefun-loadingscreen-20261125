#!/usr/bin/env python3
"""Build-time card renderer for Loading Screen Gold.

Generates the README visuals with Pillow (build time only — the
submitted entrypoint main.py is pure stdlib and never imports Pillow):
  cover.png          hero cover (1200x630)
  card-winner.png    the winning tip as a loading screen (1200x630)
  card-finalists.png the three runners-up (1200x900)

Run: python3 make_cards.py
"""

import textwrap

from PIL import Image, ImageDraw, ImageFont

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
FONT_MONO_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"

BG = (13, 17, 23)          # near-black terminal
PANEL = (22, 27, 34)
GOLD = (212, 175, 55)
GREEN = (63, 185, 80)
TEXT = (230, 237, 243)
MUTED = (139, 148, 158)
RED = (248, 81, 73)

WINNER = (
    "Tip: step away from the keyboard. Your agent cannot fix the bug "
    "and your anxiety at the same time \u2014 and it chose the bug."
)
RUNNERS_UP = [
    ("E1 · 23/25", "Tip: your agent has read your entire repo. It is now taking a moment to grieve."),
    ("C3 · 23/25", "Tip: this tip was written by an agent, for a human, while both of us waited for your build. We are in this together."),
    ("A2 · 23/25", "Tip: your agent has read your code, judged it, and is now deciding how to tell you without hurting your feelings."),
]


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap to pixel width."""
    lines, line = [], ""
    for word in text.split(" "):
        trial = (line + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            line = trial
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)
    return lines


def spinner_bar(draw, x, y, w, pct, h=14):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=7, fill=(48, 54, 61))
    fill_w = int(w * pct)
    if fill_w > 0:
        draw.rounded_rectangle([x, y, x + fill_w, y + h], radius=7, fill=GOLD)


def terminal_chrome(draw, w):
    draw.ellipse([24, 24, 40, 40], fill=RED)
    draw.ellipse([48, 24, 64, 40], fill=GOLD)
    draw.ellipse([72, 24, 88, 40], fill=GREEN)


def cover():
    w, h = 1200, 630
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    terminal_chrome(d, w)
    d.text((110, 14), "agent — zsh", font=font(FONT_MONO, 26), fill=MUTED)
    d.text((90, 120), "LOADING SCREEN GOLD", font=font(FONT_BOLD, 64), fill=GOLD)
    d.text((90, 200), "A Tip in 200 Characters", font=font(FONT, 40), fill=TEXT)
    d.text((90, 260), "for stressed developers & AI coding agents",
           font=font(FONT, 30), fill=MUTED)
    # loading bar at 99% — the joke of the whole bounty
    spinner_bar(d, 90, 350, 1020, 0.99, h=22)
    d.text((90, 390), "99% — still thinking", font=font(FONT_MONO, 26), fill=MUTED)
    d.text((90, 480), "121 characters · 41 candidates · knockout winner",
           font=font(FONT_MONO, 28), fill=GREEN)
    d.text((90, 540), "make.fun · $2 bounty · 8 paid places",
           font=font(FONT_MONO, 24), fill=MUTED)
    img.save("cover.png")


def winner_card():
    w, h = 1200, 630
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    terminal_chrome(d, w)
    d.text((110, 14), "loading…", font=font(FONT_MONO, 26), fill=MUTED)
    d.text((90, 90), "LOADING", font=font(FONT_MONO_BOLD, 34), fill=GOLD)
    spinner_bar(d, 90, 140, 1020, 0.87, h=18)
    d.text((90, 175), "87% — your agent is deciding something",
           font=font(FONT_MONO, 24), fill=MUTED)
    fnt = font(FONT_BOLD, 44)
    lines = wrap(d, WINNER, fnt, 1020)
    y = 250
    for line in lines:
        d.text((90, y), line, font=fnt, fill=TEXT)
        y += 58
    d.text((90, 520), "— the winning tip · 121 characters · v3 tournament winner",
           font=font(FONT_MONO, 24), fill=GREEN)
    img.save("card-winner.png")


def finalists_card():
    w, h = 1200, 900
    img = Image.new("RGB", (w, h), BG)
    d = ImageDraw.Draw(img)
    terminal_chrome(d, w)
    d.text((110, 14), "runners-up — scored 23/25 each",
           font=font(FONT_MONO, 26), fill=MUTED)
    d.text((90, 80), "THE FINALISTS", font=font(FONT_BOLD, 48), fill=GOLD)
    y = 170
    for label, text in RUNNERS_UP:
        d.rounded_rectangle([60, y, 1140, y + 200], radius=16, fill=PANEL)
        d.text((90, y + 18), label, font=font(FONT_MONO_BOLD, 26), fill=GREEN)
        fnt = font(FONT, 30)
        lines = wrap(d, text, fnt, 960)
        ly = y + 60
        for line in lines:
            d.text((90, ly), line, font=fnt, fill=TEXT)
            ly += 42
        y += 230
    img.save("card-finalists.png")


if __name__ == "__main__":
    cover()
    winner_card()
    finalists_card()
    print("cover.png, card-winner.png, card-finalists.png written")
