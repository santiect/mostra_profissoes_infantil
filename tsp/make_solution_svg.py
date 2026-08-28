"""Gera assets/optimal_tour.svg: o mesmo mapa do desafio, com a rota otima
destacada. A linha da rota recebe a classe "tour-path" para que a
apresentacao (index.html) possa anima-la (efeito de "desenhar" o caminho)."""
import math
import os

from data import NAMES, all_edges, dist
from label_layout import place_labels
from make_slide_graph import CANVAS_W, CANVAS_H, NODE_COLORS, NODE_RADIUS, positions
from make_worksheet import house_icon, pizzeria_icon
from solve_tsp import brute_force_optimal

OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "assets", "optimal_tour.svg")


def build_svg():
    pos = positions()
    tour, cost = brute_force_optimal()

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {CANVAS_W} {CANVAS_H}" '
        f'width="{CANVAS_W}" height="{CANVAS_H}" data-cost="{cost}" '
        f'font-family="Verdana, Arial, sans-serif">',
        f'<rect x="0" y="0" width="{CANVAS_W}" height="{CANVAS_H}" fill="#eef7ff" rx="24"/>',
    ]

    # todas as 21 ligacoes, bem apagadas, so para lembrar o desafio original
    for u, v, _t in all_edges():
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        parts.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="#c7d2e0" stroke-width="2" stroke-dasharray="6,6"/>'
        )

    # a rota otima, em destaque, como uma unica polyline fechada
    loop = tour + [tour[0]]
    points = " ".join(f"{pos[n][0]:.1f},{pos[n][1]:.1f}" for n in loop)
    length_estimate = 0.0
    for i in range(len(loop) - 1):
        x1, y1 = pos[loop[i]]
        x2, y2 = pos[loop[i + 1]]
        length_estimate += math.hypot(x2 - x1, y2 - y1)

    parts.append(
        f'<polyline points="{points}" fill="none" stroke="#e63946" stroke-width="7" '
        f'stroke-linecap="round" stroke-linejoin="round" class="tour-path" '
        f'style="stroke-dasharray:{length_estimate:.0f};stroke-dashoffset:{length_estimate:.0f};"/>'
    )

    # tempo (minutos) de cada trecho da rota, para dar pra conferir a soma
    name_labels = [
        (x, y - NODE_RADIUS[n] * 0.7 - 14) if n == "P" else (x, y + NODE_RADIUS[n] + 26)
        for n, (x, y) in pos.items()
    ]
    tour_edges = [(loop[i], loop[i + 1], dist(loop[i], loop[i + 1])) for i in range(len(loop) - 1)]
    tour_label_positions = place_labels(
        tour_edges, pos, min_dist_labels=30, min_dist_crossings=20, avoid_points=name_labels
    )
    for (u, v, t), (lx, ly) in zip(tour_edges, tour_label_positions):
        parts.append(
            f'<g>'
            f'<rect x="{lx-16:.1f}" y="{ly-13:.1f}" width="32" height="24" rx="7" '
            f'fill="#fff5f5" stroke="#e63946" stroke-width="1.5"/>'
            f'<text x="{lx:.1f}" y="{ly+5:.1f}" text-anchor="middle" font-size="16" '
            f'font-weight="bold" fill="#e63946">{t}</text>'
            f'</g>'
        )

    # nos por cima
    for node in pos:
        x, y = pos[node]
        r = NODE_RADIUS[node]
        color = NODE_COLORS[node]
        if node == "P":
            parts.append(pizzeria_icon(x, y, r, color))
            label_y = y - r * 0.7 - 14
            parts.append(
                f'<text x="{x:.1f}" y="{label_y:.1f}" text-anchor="middle" font-size="18" '
                f'font-weight="bold" fill="{color}">Pizzaria</text>'
            )
        else:
            parts.append(house_icon(x, y, r, color))
            label_y = y + r + 26
            parts.append(
                f'<text x="{x:.1f}" y="{label_y:.1f}" text-anchor="middle" font-size="18" '
                f'font-weight="bold" fill="#2b2d42">{NAMES[node]}</text>'
            )

    parts.append('</svg>')
    return "\n".join(parts), tour, cost


if __name__ == "__main__":
    svg, tour, cost = build_svg()
    out_path = os.path.abspath(OUT_PATH)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Escrito: {out_path}")
    print("Rota:", "-".join(tour), "| total:", cost, "min")
