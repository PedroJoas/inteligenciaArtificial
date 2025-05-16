def busca_alfa_beta(grafo, vertice):
    v = valor_max(grafo, vertice, float('-inf'), float('inf'))
    return v

def valor_max(grafo, vertice, alpha, beta):
    if isinstance(grafo[vertice][0], int):
        return max(grafo[vertice])
    
    v = float('-inf')
    for filho in grafo[vertice]:
        v = max(v, valor_min(grafo, filho, alpha, beta))
        if v >= beta:
            return v
        alpha = max(alpha, v)
    return v

def valor_min(grafo, vertice, alpha, beta):
    if isinstance(grafo[vertice][0], int):
        return min(grafo[vertice])
    
    v = float('inf')
    for filho in grafo[vertice]:
        v = min(v, valor_max(grafo, filho, alpha, beta))
        if v <= alpha:
            return v
        beta = min(beta, v)
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

print(busca_alfa_beta(grafo, 'A'))  # Saída correta: 5

