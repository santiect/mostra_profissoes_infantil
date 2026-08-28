"""
Dados do "Desafio do Luigi": 7 pontos (a pizzaria + 6 amigos) e os tempos
(minutos) entre cada par de pontos. Usado pelo solver, pelo gerador da folha
de atividade e pelo gerador da imagem da solucao.
"""

NODES = ["P", "A", "B", "C", "D", "E"]

NAMES = {
    "P": "Pizzaria do Luigi",
    "A": "Ana",
    "B": "Bruno",
    "C": "Carla",
    "D": "Diego",
    "E": "Elisa",
}

# tempos em minutos entre cada par de pontos (grafo completo, simetrico).
# os 6 pontos ficam desenhados em circulo (P, A, B, C, D, E, nessa ordem),
# mas a rota otima NAO e o contorno do circulo (isso seria obvio demais de
# adivinhar so de olhar o desenho): o caminho barato e o ziguezague
# P-B-D-A-C-E-P, que cruza o meio do desenho. Alem disso, a ligacao P-A e
# uma armadilha bem curta que engana quem sempre escolhe o amigo mais
# proximo (o guloso sai de P por A, mas depois paga caro pra fechar a rota).
EDGES = {
    ("P", "B"): 4, ("B", "D"): 2, ("D", "A"): 4, ("A", "C"): 2, ("C", "E"): 4, ("E", "P"): 2,
    ("P", "A"): 1,
    ("P", "C"): 12, ("P", "D"): 13,
    ("A", "B"): 13, ("A", "E"): 12,
    ("B", "C"): 14, ("B", "E"): 13,
    ("C", "D"): 15,
    ("D", "E"): 14,
}


def dist(u, v):
    if u == v:
        return 0
    return EDGES.get((u, v)) or EDGES[(v, u)]


def tour_cost(tour):
    return sum(dist(tour[i], tour[i + 1]) for i in range(len(tour) - 1)) + dist(tour[-1], tour[0])


def all_edges():
    """Todas as 21 arestas do grafo completo como (u, v, tempo)."""
    return [(u, v, t) for (u, v), t in EDGES.items()]
