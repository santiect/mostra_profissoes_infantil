"""
O Desafio do Luigi: caixeiro-viajante (TSP) com 6 amigos.

Compara a estrategia gulosa (vizinho mais proximo) com a solucao otima
(busca exaustiva, viavel pois sao so 7 pontos -> 360 ciclos possiveis).
"""
import itertools

from data import NODES, NAMES, dist, tour_cost


def greedy_nearest_neighbor(start="P"):
    unvisited = set(NODES) - {start}
    tour = [start]
    current = start
    while unvisited:
        nxt = min(unvisited, key=lambda v: dist(current, v))
        tour.append(nxt)
        unvisited.remove(nxt)
        current = nxt
    return tour


def brute_force_optimal(start="P"):
    others = [n for n in NODES if n != start]
    best_tour, best_cost = None, float("inf")
    for perm in itertools.permutations(others):
        tour = [start, *perm]
        cost = tour_cost(tour)
        if cost < best_cost:
            best_tour, best_cost = tour, cost
    return best_tour, best_cost


def describe(tour):
    cost = tour_cost(tour)
    steps = " -> ".join(NAMES[n] for n in tour) + f" -> {NAMES[tour[0]]}"
    return steps, cost


if __name__ == "__main__":
    greedy = greedy_nearest_neighbor()
    greedy_steps, greedy_cost = describe(greedy)

    optimal, optimal_cost = brute_force_optimal()
    optimal_steps, _ = describe(optimal)

    print("=== Estrategia gulosa (vizinho mais proximo) ===")
    print(greedy_steps)
    print(f"Tempo total: {greedy_cost} minutos\n")

    print("=== Solucao otima (busca exaustiva entre 360 rotas) ===")
    print(optimal_steps)
    print(f"Tempo total: {optimal_cost} minutos\n")

    print(f"Economia ao usar a rota otima: {greedy_cost - optimal_cost} minutos")
    print("\nOrdem otima (codigos):", "-".join(optimal))
