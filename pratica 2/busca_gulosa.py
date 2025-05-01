def busca_gulosa(grafo, heuristicas, ponto_inicial, ponto_final):
    vertice = (ponto_inicial,0)
    visitados = []

    while True:
        no_atual, custo_atual = vertice
        
        visitados.append(no_atual)
        if no_atual == ponto_final:
            menor_custo = custo_atual
            break
        
        grafo[no_atual].sort(key=lambda x: heuristicas[x[0]] + custo_atual)
        vertice = grafo[no_atual][0]

        
    return visitados, menor_custo

grafo = {
    1: [(2, 2), (3,5)],
    2: [(4,2), (5,4)],
    3: [(6,2)],
    4: [(7,3)],
    5: [(7,2), (8,3)],
    6: [(8,2)],
    7: [(9,2)],
    8: [(9,1)],
    9: [(10,2)],
    10: [(11,1)],
    11: [(12,1)]
}

heuristicas = {
    1:12,
    2:10,
    3:8,
    4:9,
    5:6,
    6:7,
    7:4,
    8:5,
    9:3,
    10:2,
    11:1,
    12:0
}

visitados, menor_custo = busca_gulosa(grafo, heuristicas, 1, 12)

print(visitados)
print(menor_custo)