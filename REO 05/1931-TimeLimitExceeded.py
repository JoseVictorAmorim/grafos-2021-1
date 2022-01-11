# Davi Alves Carvalho
# Ewerton Keiji Onga
# José Victor Amorim Morais

from heapq import *
x = 2**33

def dijkstra(grafo, custo, visitado, inicio, fim):
    custo[inicio] = 0
    pq = []
    heappush(pq, [custo[inicio], inicio, 0])
    while (pq):
        tempo, v, pago = heappop(pq)
        if (visitado[v] != 2): 
            visitado[v] += pago
            for u in grafo[v]:
                if (((u[0] == fim and 1 - pago == 0) or (u[0] != fim)) and tempo + u[1] < custo[u[0]]):
                    custo[u[0]] = tempo + u[1]
                heappush(pq, [tempo + u[1], u[0], 1 - pago])

def preencher(grafo):
    u, v, c = map(int, input().split())
    grafo[u] += [[v, c]]
    grafo[v] += [[u, c]]

cidades, estradas = map(int, input().split())
grafo = [[] for i in range(cidades + 1)]
for i in range(estradas):
    preencher(grafo)  

custo, visitado = [x] * (cidades + 1), [0] * (cidades + 1)
dijkstra(grafo, custo, visitado, 1, cidades)

if (custo[cidades] == x):
    print(-1)
else:
    print(custo[cidades])