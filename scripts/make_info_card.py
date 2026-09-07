#!/usr/bin/env python3
"""Hand-author the neofetch-style info card SVG.

Each line fades and slides in on a short stagger (CSS keyframes inside
the SVG — GitHub plays them). STATIC=1 emits a frozen frame for Quick Look.

Usage: python scripts/make_info_card.py
Writes info-card.svg.
"""
import html
import os

BG = "#0A0B0D"
BORDER = "#1C1E22"
KEY = "#3ECF8E"   # single accent, matches banner
VAL = "#F2F3F5"
DIM = "#8A8F98"
QUIET = "#5C6169"

W = 560
LINE_H = 27
STAGGER = 0.28

TITLE = "shahbod@github"
ROWS = [
    ("", ""),
    ("Name", "Shahbod"),
    ("Location", "Germany"),
    ("Role", "Data & Process Analyst"),
    ("", ""),
    ("Built", "Data & Process Automation"),
    ("Also", "PostgreSQL, Citus & Superset"),
    ("", ""),
    ("Stack", "Python, Docker, Airflow"),
    ("Focus", "Data Engineering"),
    ("", ""),
]


def main() -> None:
    static = os.environ.get("STATIC") == "1"
    # dynamic height: header block + rows (blank rows are shorter)
    blanks = sum(1 for k, v in ROWS if not k and not v)
    lines = len(ROWS) - blanks
    H = round(90 + blanks * LINE_H * 0.45 + lines * LINE_H + 20)
    anim_css = "" if static else (
        ".ln{opacity:0;transform:translateX(-8px);"
        "animation:in .45s ease-out forwards}"
        "@keyframes in{to{opacity:1;transform:none}}"
    )

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        f'font-family="ui-monospace,SFMono-Regular,Menlo,Consolas,monospace" font-size="14">',
        f"<style>{anim_css}</style>",
        f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="6" fill="{BG}" stroke="{BORDER}"/>',
        # flat title row — no traffic-light chrome, no glow
        f'<text x="24" y="34" fill="{QUIET}" font-size="12" letter-spacing="0.5">{TITLE}</text>',
        f'<line x1="1" y1="50" x2="{W - 1}" y2="50" stroke="{BORDER}"/>',
    ]

    y = 84
    delay = 0.15
    for key, val in ROWS:
        delay += STAGGER * 0.55
        if not key and not val:
            y += LINE_H * 0.45
            continue
        if key:
            parts.append(
                f'<g class="ln" style="animation-delay:{delay:.2f}s">'
                f'<text x="24" y="{y}"><tspan fill="{KEY}">{html.escape(key)}</tspan>'
                f'<tspan fill="{QUIET}">: </tspan>'
                f'<tspan x="130" fill="{VAL}">{html.escape(val)}</tspan></text></g>'
            )
        else:
            parts.append(
                f'<g class="ln" style="animation-delay:{delay:.2f}s">'
                f'<text x="130" y="{y}" fill="{DIM}">{html.escape(val)}</text></g>'
            )
        y += LINE_H

    parts.append("</svg>")

    with open("info-card.svg", "w") as f:
        f.write("\n".join(parts))
    print("wrote info-card.svg")


if __name__ == "__main__":
    main()
