def busca_a_estrela(grafo, heuristicas, ponto_inicial, ponto_final):
    vertice = (ponto_inicial,0)
    visitados = []

    while True:
        no_atual, custo_atual = vertice
        
        visitados.append(no_atual)
        if no_atual == ponto_final:
            menor_custo = custo_atual
            break

        grafo[no_atual].sort(key=lambda x: x[1] + heuristicas[x[0]] + custo_atual)
        vertice = grafo[no_atual][0]

        
    return visitados, menor_custo


grafo = {
    1: [(2, 2), (3, 3)],
    2: [(4, 2), (5, 4)],
    3: [(5, 2), (6, 5)],
    4: [(7, 2)],
    5: [(7, 1), (8, 3)],
    6: [(8, 2), (9, 4)],
    7: [(10, 3)],
    8: [(10, 2), (11, 4)],
    9: [(11, 1)],
    10: [(12, 2)],
    11: [(12, 1)],
    12: [(13, 2)],
    13: []
}

heuristicas = {
    1: 11,
    2: 10,
    3: 9,
    4: 10,
    5: 8,
    6: 7,
    7: 7,
    8: 6,
    9: 6,
    10: 5,
    11: 4,
    12: 2,
    13: 0
}

visitados, menor_custo = busca_a_estrela(grafo, heuristicas, 1, 13)

print(visitados)
print(menor_custo)