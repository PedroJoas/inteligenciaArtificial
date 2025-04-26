class Buscas:
    def __init__(self):
        pass

    def dfs(self,grafo, ponto_inicial, ponto_final):
        visitados = []
        pilha = [ponto_inicial]

        while pilha:
            vertice = pilha.pop()
            if vertice not in visitados:
                visitados.append(vertice)
            if vertice == ponto_final:
                print('Achei chefe')
                break

            for v in grafo[vertice]:
                if v not in visitados:
                    pilha.append(v)
        return visitados
    
    def bfs(self,grafo, ponto_inicial, ponto_final):
        fila = [ponto_inicial]
        visitados = []
        while fila:
            vertice = fila.pop(0)
            if vertice not in visitados:
                visitados.append(vertice)

            if vertice == ponto_final:
                print('Achei chefe')
                break

            for n in grafo[vertice]: 
                if n not in visitados:
                    fila.append(n)

        return visitados
    

graph = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Fagaras': ['Sibiu', 'Bucharest'],
    'Rimnicu Vilcea': ['Sibiu', 'Pitesti', 'Craiova'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucharest'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Bucharest': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni'],
    'Giurgiu': ['Bucharest'],
    'Urziceni': ['Bucharest', 'Hirsova', 'Vaslui'],
    'Hirsova': ['Urziceni', 'Eforie'],
    'Eforie': ['Hirsova'],
    'Vaslui': ['Urziceni', 'Iasi'],
    'Iasi': ['Vaslui', 'Neamt'],
    'Neamt': ['Iasi']
}

buscas = Buscas()

print('DFS:')
print(buscas.dfs(graph,ponto_inicial='Arad', ponto_final='Bucharest'))

print('BFS')
print(buscas.bfs(graph,ponto_inicial='Arad', ponto_final='Bucharest'))
