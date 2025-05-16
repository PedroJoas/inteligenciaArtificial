def valor_max(grafo, vertice):
    if isinstance(grafo[vertice][0], int):
        return max(grafo[vertice])
    
    v = float('-inf')
    for filho in grafo[vertice]:
        v = max(v, valor_min(grafo, filho))
    return v

def valor_min(grafo, vertice):
    if isinstance(grafo[vertice][0], int):
        return min(grafo[vertice])
    
    v = float('inf')
    for filho in grafo[vertice]:
        v = min(v, valor_max(grafo, filho))
    return v

grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [3, 5],
    'E': [6, 9],
    'F': [1, 2],
    'G': [0, -1]
}

resultado = valor_max(grafo, 'A')
print(resultado)  
