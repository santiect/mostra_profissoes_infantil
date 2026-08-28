"""Layout (posicoes 2D) compartilhado entre a folha de atividade e a imagem
da solucao, para que ambas mostrem o mesmo "mapa" do desafio do Luigi."""
import math

from data import NODES

# canvas no formato A4 (proporcao 1 : 1.4142), em unidades SVG
CANVAS_W = 1000
CANVAS_H = 1414

CENTER = (500, 810)
RADIUS = 360

# P no topo do circulo, amigos em sequencia no sentido horario -> as arestas
# "baratas" do anel ficam visualmente entre vizinhos, e a ligacao-armadilha
# B-E aparece como uma corda cruzando o meio do desenho, igual as demais.
_START_ANGLE = -90.0
_STEP = 360.0 / len(NODES)

NODE_COLORS = {
    "P": "#e63946",
    "A": "#ff8fa3",
    "B": "#4ecdc4",
    "C": "#ffd166",
    "D": "#6bcb77",
    "E": "#4d96ff",
    "F": "#c084fc",
}

NODE_RADIUS = {n: (60 if n == "P" else 46) for n in NODES}


def positions():
    cx, cy = CENTER
    pts = {}
    for i, node in enumerate(NODES):
        angle = math.radians(_START_ANGLE + i * _STEP)
        x = cx + RADIUS * math.cos(angle)
        y = cy + RADIUS * math.sin(angle)
        pts[node] = (x, y)
    return pts
