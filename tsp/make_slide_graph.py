"""Gera assets/challenge_graph.svg: versao "de tela" (paisagem, sem moldura
de folha impressa) do mapa do desafio, para usar animada na apresentacao.
A folha para imprimir (worksheet/pizza_challenge.svg) continua sendo gerada
por make_worksheet.py; este script e so para o slide."""
import math
import os

from data import NAMES, all_edges
from label_layout import place_labels
from make_worksheet import house_icon, pizzeria_icon

OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "assets", "challenge_graph.svg")

CANVAS_W = 900
CANVAS_H = 660
CENTER = (450, 345)
RADIUS = 235

from data import NODES

NODE_COLORS = {
    "P": "#e63946", "A": "#ff8fa3", "B": "#4ecdc4",
    "C": "#ffd166", "D": "#6bcb77", "E": "#4d96ff",
}
NODE_RADIUS = {n: (40 if n == "P" else 32) for n in NODES}


def positions():
    cx, cy = CENTER
    pts = {}
    step = 360.0 / len(NODES)
    for i, node in enumerate(NODES):
        angle = math.radians(-90 + i * step)
        pts[node] = (cx + RADIUS * math.cos(angle), cy + RADIUS * math.sin(angle))
    return pts


def build_svg():
    pos = positions()
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {CANVAS_W} {CANVAS_H}" '
        f'width="{CANVAS_W}" height="{CANVAS_H}" font-family="Verdana, Arial, sans-serif">',
    ]

    name_labels = []
    for n, (x, y) in pos.items():
        if n == "P":
            name_labels.append((x, y - NODE_RADIUS[n] * 0.7 - 14))
        else:
            name_labels.append((x, y + NODE_RADIUS[n] + 26))
    edges = all_edges()
    label_positions = place_labels(edges, pos, min_dist_labels=34, min_dist_crossings=22, avoid_points=name_labels)

    for (u, v, t), (lx, ly) in zip(edges, label_positions):
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        parts.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="#b8c4d6" stroke-width="2" stroke-dasharray="7,6"/>'
        )
        parts.append(
            f'<g>'
            f'<rect x="{lx-16:.1f}" y="{ly-13:.1f}" width="32" height="24" rx="7" '
            f'fill="#ffffff" stroke="#b8c4d6" stroke-width="1.3"/>'
            f'<text x="{lx:.1f}" y="{ly+5:.1f}" text-anchor="middle" font-size="16" '
            f'font-weight="bold" fill="#2b2d42">{t}</text>'
            f'</g>'
        )

    for node in pos:
        x, y = pos[node]
        r = NODE_RADIUS[node]
        color = NODE_COLORS[node]
        if node == "P":
            parts.append(pizzeria_icon(x, y, r, color))
            parts.append(
                f'<text x="{x:.1f}" y="{y - r*0.7 - 14:.1f}" text-anchor="middle" font-size="18" '
                f'font-weight="bold" fill="{color}">Pizzaria</text>'
            )
        else:
            parts.append(house_icon(x, y, r, color))
            parts.append(
                f'<text x="{x:.1f}" y="{y + r + 26:.1f}" text-anchor="middle" font-size="18" '
                f'font-weight="bold" fill="#2b2d42">{NAMES[node]}</text>'
            )

    parts.append('</svg>')
    return "\n".join(parts)


if __name__ == "__main__":
    svg = build_svg()
    out_path = os.path.abspath(OUT_PATH)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Escrito: {out_path}")
