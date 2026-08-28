"""Posiciona os rotulos de tempo das arestas sempre EM CIMA da propria linha,
evitando dois problemas de legibilidade num grafo completo bem cheio de
linhas cruzando:
  1) um rotulo pousar em cima de outro rotulo (dois numeros amontoados);
  2) um rotulo pousar bem no cruzamento de DUAS OUTRAS linhas, o que faz
     parecer que o numero poderia pertencer a qualquer uma delas.
Para isso, calculamos os pontos onde os tracos se cruzam e tratamos esses
pontos como "zonas proibidas", junto com os rotulos ja posicionados.
"""

CANDIDATE_TS = [0.5, 0.32, 0.68, 0.22, 0.78, 0.4, 0.6, 0.15, 0.85]


def _segment_intersection(p1, p2, p3, p4):
    """Ponto onde os segmentos (p1,p2) e (p3,p4) se cruzam no INTERIOR de
    ambos (nao nas pontas) - ou None se nao se cruzam assim."""
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4
    d = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    if abs(d) < 1e-9:
        return None
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / d
    u = ((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2)) / d
    if 0.06 < t < 0.94 and 0.06 < u < 0.94:
        return (x1 + t * (x2 - x1), y1 + t * (y2 - y1))
    return None


def crossing_points(edges, pos):
    """Todos os pontos onde duas arestas (que nao compartilham uma ponta) se
    cruzam no meio do desenho."""
    pts = []
    for i in range(len(edges)):
        u1, v1, _ = edges[i]
        for j in range(i + 1, len(edges)):
            u2, v2, _ = edges[j]
            if {u1, v1} & {u2, v2}:
                continue
            pt = _segment_intersection(pos[u1], pos[v1], pos[u2], pos[v2])
            if pt:
                pts.append(pt)
    return pts


def place_labels(edges, pos, min_dist_labels=46, min_dist_crossings=30, avoid_points=None):
    """Escolhe, para cada aresta, um ponto sobre ela propria para o rotulo,
    longe dos rotulos ja colocados, longe de cruzamentos com outras arestas,
    e (se informado) longe de pontos extras como os textos com os nomes."""
    danger = crossing_points(edges, pos)
    placed = list(avoid_points or [])
    result = []
    for (u, v, _t) in edges:
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        best_pt, best_score = None, -1.0
        for tc in CANDIDATE_TS:
            lx = x1 + (x2 - x1) * tc
            ly = y1 + (y2 - y1) * tc
            label_d = min((((lx - px) ** 2 + (ly - py) ** 2) ** 0.5 for px, py in placed), default=1e9)
            cross_d = min((((lx - cx) ** 2 + (ly - cy) ** 2) ** 0.5 for cx, cy in danger), default=1e9)
            ok = label_d >= min_dist_labels and cross_d >= min_dist_crossings
            score = min(label_d, cross_d * (min_dist_labels / min_dist_crossings))
            if ok:
                best_pt = (lx, ly)
                break
            if score > best_score:
                best_score, best_pt = score, (lx, ly)
        placed.append(best_pt)
        result.append(best_pt)
    return result
