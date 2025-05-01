def busca_custo_uniforme(grafo, ponto_inicial, ponto_final):
    fila = [(ponto_inicial, 0)]
    visitados = []

    while fila:
        fila.sort(key=lambda x:x[1])
        print(fila)
        vertice = fila.pop(0)
        cidade_atual = vertice[0]
        peso = vertice[1]
        visitados.append(cidade_atual)

        if cidade_atual == ponto_final:
            menor_custo = peso
            break
        
        for cidade, custo in grafo[cidade_atual]:
            fila_temp = list(map(lambda x: x[0], fila))
            custo_atual = custo + peso
            if cidade not in visitados and cidade not in fila_temp:
                fila.append((cidade, custo_atual))

            elif any(c == cidade for c in fila_temp):
                if fila[fila_temp.index(cidade)][1] > custo_atual:
                    fila[fila_temp.index(cidade)] = (cidade, custo_atual)


    return visitados, menor_custo


cidades = {
    'Arad': [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
    'Zerind': [('Arad', 75), ('Oradea', 71)],
    'Oradea': [('Zerind', 71), ('Sibiu', 151)],
    'Timisoara': [('Arad', 118), ('Lugoj', 111)],
    'Lugoj': [('Timisoara', 111), ('Mehadia', 70)],
    'Mehadia': [('Lugoj', 70), ('Dobreta', 75)],
    'Dobreta': [('Mehadia', 75), ('Craiova', 120)],
    'Craiova': [('Dobreta', 120), ('Pitesti', 138), ('Rimnicu Vilcea', 146)],
    'Sibiu': [('Arad', 140), ('Oradea', 151), ('Fagaras', 99), ('Rimnicu Vilcea', 80)],
    'Fagaras': [('Sibiu', 99), ('Bucharest', 211)],
    'Rimnicu Vilcea': [('Sibiu', 80), ('Craiova', 146), ('Pitesti', 97)],
    'Pitesti': [('Rimnicu Vilcea', 97), ('Craiova', 138), ('Bucharest', 101)],
    'Bucharest': [('Fagaras', 211), ('Pitesti', 101), ('Giurgiu', 90), ('Urziceni', 85)],
    'Giurgiu': [('Bucharest', 90)],
    'Urziceni': [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
    'Hirsova': [('Urziceni', 98), ('Eforie', 86)],
    'Eforie': [('Hirsova', 86)],
    'Vaslui': [('Urziceni', 142), ('Iasi', 92)],
    'Iasi': [('Vaslui', 92), ('Neamt', 87)],
    'Neamt': [('Iasi', 87)]
}

visitados, custo_final = busca_custo_uniforme(cidades, 'Arad', 'Bucharest')

print(visitados)
print(custo_final)
