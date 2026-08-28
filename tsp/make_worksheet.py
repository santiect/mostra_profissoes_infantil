"""Gera worksheet/pizza_challenge.svg: a folha A4 do desafio do Luigi."""
import math
import os

from data import NAMES, NODES, all_edges
from label_layout import place_labels
from layout import CANVAS_W, CANVAS_H, NODE_COLORS, NODE_RADIUS, positions

OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "worksheet", "pizza_challenge.svg")


def house_icon(cx, cy, r, color):
    """Casinha simples: quadrado + telhado triangular."""
    w = r * 1.15
    roof_h = r * 0.75
    body_top = cy - r * 0.15
    body_h = r * 1.05
    x0, x1 = cx - w / 2, cx + w / 2
    return f'''
    <g>
      <rect x="{x0:.1f}" y="{body_top:.1f}" width="{w:.1f}" height="{body_h:.1f}"
            rx="6" fill="#fff7e6" stroke="{color}" stroke-width="5"/>
      <polygon points="{cx - w * 0.62:.1f},{body_top:.1f} {cx:.1f},{body_top - roof_h:.1f} {cx + w * 0.62:.1f},{body_top:.1f}"
               fill="{color}" stroke="{color}" stroke-width="4" stroke-linejoin="round"/>
      <rect x="{cx - r * 0.16:.1f}" y="{body_top + body_h - r * 0.55:.1f}" width="{r * 0.32:.1f}" height="{r * 0.55:.1f}"
            fill="{color}"/>
    </g>'''


def pizzeria_icon(cx, cy, r, color):
    """Uma lojinha (pizzaria): toldo listrado, fachada, porta, janela redonda
    com uma fatia de pizza dentro - para destacar que e um estabelecimento,
    diferente das casinhas dos amigos."""
    w = r * 1.9
    body_h = r * 1.25
    body_top = cy - r * 0.05
    x0 = cx - w / 2
    awning_h = r * 0.55
    teeth = 6
    tooth_w = w / teeth
    teeth_path = []
    for k in range(teeth):
        tx0 = x0 + k * tooth_w
        tx1 = tx0 + tooth_w
        tcolor = "#e63946" if k % 2 == 0 else "#ffffff"
        teeth_path.append(
            f'<path d="M {tx0:.1f} {body_top - awning_h:.1f} L {tx1:.1f} {body_top - awning_h:.1f} '
            f'L {tx1:.1f} {body_top:.1f} A {tooth_w/2:.1f} {tooth_w/2:.1f} 0 0 1 {tx0:.1f} {body_top:.1f} Z" '
            f'fill="{tcolor}" stroke="#b5121b" stroke-width="1.5"/>'
        )
    return f'''
    <g>
      <rect x="{x0:.1f}" y="{body_top:.1f}" width="{w:.1f}" height="{body_h:.1f}"
            fill="#fff7e6" stroke="{color}" stroke-width="5"/>
      {''.join(teeth_path)}
      <rect x="{x0:.1f}" y="{body_top - awning_h - 10:.1f}" width="{w:.1f}" height="10"
            fill="{color}"/>
      <circle cx="{cx:.1f}" cy="{body_top + body_h * 0.42:.1f}" r="{r * 0.42:.1f}"
              fill="#ffffff" stroke="{color}" stroke-width="4"/>
      <path d="M {cx:.1f} {body_top + body_h * 0.42 - r * 0.28:.1f}
               L {cx + r * 0.26:.1f} {body_top + body_h * 0.42 + r * 0.18:.1f}
               A {r * 0.32:.1f} {r * 0.32:.1f} 0 0 1 {cx - r * 0.26:.1f} {body_top + body_h * 0.42 + r * 0.18:.1f} Z"
            fill="#ffd166" stroke="#e63946" stroke-width="3" stroke-linejoin="round"/>
      <circle cx="{cx:.1f}" cy="{body_top + body_h * 0.42:.1f}" r="{r * 0.05:.1f}" fill="#e63946"/>
      <rect x="{cx - r * 0.22:.1f}" y="{body_top + body_h - r * 0.62:.1f}" width="{r * 0.44:.1f}" height="{r * 0.62:.1f}"
            fill="{color}" stroke="#7a1620" stroke-width="2"/>
      <circle cx="{cx + r * 0.14:.1f}" cy="{body_top + body_h - r * 0.3:.1f}" r="3" fill="#ffe6a8"/>
    </g>'''


def luigi_character(cx, cy):
    """Luigi de corpo inteiro: chapeu de chef, bigode, avental e uma
    caixa de pizza nas maos - o narrador do desafio."""
    return f'''
    <g>
      <ellipse cx="{cx:.1f}" cy="{cy+150:.1f}" rx="70" ry="14" fill="#000000" opacity="0.06"/>
      <path d="M {cx-46:.1f} {cy+150:.1f}
               C {cx-58:.1f} {cy+70:.1f} {cx-52:.1f} {cy+18:.1f} {cx:.1f} {cy+14:.1f}
               C {cx+52:.1f} {cy+18:.1f} {cx+58:.1f} {cy+70:.1f} {cx+46:.1f} {cy+150:.1f} Z"
            fill="#ffffff" stroke="#dcdcdc" stroke-width="3"/>
      <path d="M {cx-46:.1f} {cy+150:.1f} C {cx-58:.1f} {cy+70:.1f} {cx-52:.1f} {cy+18:.1f} {cx:.1f} {cy+14:.1f}
               L {cx:.1f} {cy+150:.1f} Z" fill="#e63946" opacity="0.12"/>
      <rect x="{cx-16:.1f}" y="{cy+40:.1f}" width="32" height="40" rx="6" fill="#e63946"/>
      <circle cx="{cx:.1f}" cy="{cy-38:.1f}" r="52" fill="#ffd9a0" stroke="#e07a3f" stroke-width="4"/>
      <path d="M {cx-46:.1f} {cy-60:.1f}
               a 46 36 0 0 1 92 0
               q 6 -30 -16 -32 q -6 12 -18 4 q -8 -16 -20 -4 q -6 -10 -18 -4 q -18 8 -20 36 Z"
            fill="#ffffff" stroke="#dcdcdc" stroke-width="2"/>
      <rect x="{cx-40:.1f}" y="{cy-96:.1f}" width="80" height="14" rx="6" fill="#ffffff" stroke="#dcdcdc" stroke-width="2"/>
      <circle cx="{cx-18:.1f}" cy="{cy-42:.1f}" r="5.5" fill="#2b2d42"/>
      <circle cx="{cx+18:.1f}" cy="{cy-42:.1f}" r="5.5" fill="#2b2d42"/>
      <circle cx="{cx-18:.1f}" cy="{cy-24:.1f}" r="9" fill="#ffb37a" opacity="0.7"/>
      <circle cx="{cx+18:.1f}" cy="{cy-24:.1f}" r="9" fill="#ffb37a" opacity="0.7"/>
      <path d="M {cx-22:.1f} {cy-14:.1f} q 10 12 22 12 q 12 0 22 -12
               q -10 10 -22 10 q -12 0 -22 -10 Z" fill="#5c3a21"/>
      <path d="M {cx:.1f} {cy-10:.1f} q 6 -6 12 -2" stroke="#5c3a21" stroke-width="3" fill="none" stroke-linecap="round"/>
      <path d="M {cx:.1f} {cy-10:.1f} q -6 -6 -12 -2" stroke="#5c3a21" stroke-width="3" fill="none" stroke-linecap="round"/>
    </g>'''


def build_svg():
    pos = positions()
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {CANVAS_W} {CANVAS_H}" '
        f'width="210mm" height="297mm" font-family="Verdana, Arial, sans-serif">',
        f'<rect x="0" y="0" width="{CANVAS_W}" height="{CANVAS_H}" fill="#ffffff"/>',
        # cantos decorativos so com contorno, para gastar pouca tinta na impressao
        f'<circle cx="60" cy="60" r="34" fill="none" stroke="#ffd166" stroke-width="4"/>',
        f'<circle cx="{CANVAS_W-70}" cy="90" r="24" fill="none" stroke="#ff8fa3" stroke-width="4"/>',
        f'<circle cx="{CANVAS_W-50}" cy="{CANVAS_H-70}" r="30" fill="none" stroke="#6bcb77" stroke-width="4"/>',
        f'<circle cx="55" cy="{CANVAS_H-60}" r="22" fill="none" stroke="#4d96ff" stroke-width="4"/>',
        # titulo
        f'<text x="{CANVAS_W/2}" y="95" text-anchor="middle" font-size="46" font-weight="bold" fill="#e63946">'
        f'Ajude o Luigi a entregar as pizzas! \U0001F355</text>',
        f'<text x="{CANVAS_W/2}" y="140" text-anchor="middle" font-size="24" fill="#264653">'
        f'Saia da pizzaria, visite cada amigo uma única vez e volte para a pizzaria.</text>',
        f'<text x="{CANVAS_W/2}" y="172" text-anchor="middle" font-size="24" fill="#264653">'
        f'Risque a lápis o caminho que você acha mais rápido. Os números são minutos!</text>',
        luigi_character(150, 310),
        f'<rect x="230" y="240" width="740" height="118" rx="24" fill="#ffffff" stroke="#ffd166" stroke-width="4"/>',
        f'<polygon points="230,320 230,355 272,320" fill="#ffffff" stroke="#ffd166" stroke-width="4"/>',
        f'<text x="600" y="272" text-anchor="middle" font-size="20" fill="#264653">'
        f'"As pizzas estão quentinhas...</text>',
        f'<text x="600" y="298" text-anchor="middle" font-size="20" fill="#264653">'
        f'preciso entregar rápido, antes</text>',
        f'<text x="600" y="324" text-anchor="middle" font-size="20" fill="#264653">'
        f'que esfriem! Me ajudam?" - Luigi</text>',
    ]

    # arestas tracejadas (grafo completo) com rotulo dos tempos. cada rotulo
    # fica sempre EM CIMA da sua propria linha, longe de outros rotulos, longe
    # de cruzamentos com outras linhas, e longe dos nomes/pizzaria (senao fica
    # ambiguo a qual aresta o numero pertence) - ver tsp/label_layout.py.
    name_labels = []
    for n, (x, y) in pos.items():
        if n == "P":
            name_labels.append((x, y - NODE_RADIUS[n] * 0.6 - 22))
        else:
            name_labels.append((x, y + NODE_RADIUS[n] + 34))
    edges = all_edges()
    label_positions = place_labels(edges, pos, avoid_points=name_labels)

    for (u, v, t), (lx, ly) in zip(edges, label_positions):
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        parts.append(
            f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
            f'stroke="#8d99ae" stroke-width="2.5" stroke-dasharray="9,7"/>'
        )
        parts.append(
            f'<g>'
            f'<rect x="{lx-19:.1f}" y="{ly-15:.1f}" width="38" height="28" rx="8" '
            f'fill="#ffffff" stroke="#8d99ae" stroke-width="1.5"/>'
            f'<text x="{lx:.1f}" y="{ly+6:.1f}" text-anchor="middle" font-size="19" '
            f'font-weight="bold" fill="#2b2d42">{t}</text>'
            f'</g>'
        )

    # nos (casas + pizzaria) por cima das linhas
    for node in pos:
        x, y = pos[node]
        r = NODE_RADIUS[node]
        color = NODE_COLORS[node]
        if node == "P":
            parts.append(pizzeria_icon(x, y, r, color))
            label_y = y - r * 0.6 - 22
            parts.append(
                f'<text x="{x:.1f}" y="{label_y:.1f}" text-anchor="middle" font-size="24" '
                f'font-weight="bold" fill="{color}">Pizzaria</text>'
            )
        else:
            parts.append(house_icon(x, y, r, color))
            label_y = y + r + 34
            parts.append(
                f'<text x="{x:.1f}" y="{label_y:.1f}" text-anchor="middle" font-size="24" '
                f'font-weight="bold" fill="#2b2d42">{NAMES[node]}</text>'
            )

    # caixa de resposta no rodape
    box_y = CANVAS_H - 150
    parts.append(
        f'<rect x="80" y="{box_y}" width="{CANVAS_W-160}" height="95" rx="16" '
        f'fill="#ffffff" stroke="#e63946" stroke-width="3" stroke-dasharray="4,4"/>'
    )
    parts.append(
        f'<text x="110" y="{box_y+40}" font-size="22" fill="#264653">'
        f'Meu caminho: ______________________________________</text>'
    )
    parts.append(
        f'<text x="110" y="{box_y+78}" font-size="22" fill="#264653">'
        f'Tempo total: __________ minutos</text>'
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
