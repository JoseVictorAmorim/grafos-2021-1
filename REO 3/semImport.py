import heapq

def fnc(grafo, est):
    sGrafo = 0
    for i in range(0,est):
        entrada = input("")
        x, y, z = entrada.split()
        x = int(x)
        y = int(y)
        z = int(z)

        n_out[x].append((y, z))
        n_out[y].append((x, z))
        sGrafo += z
    
    min = nx.minimum_spanning_tree(grafo)
    sMin = 0

    for(x, y, w) in min.edges.data('weight'):
        sMin += int(w)
    return(sGrafo - sMin)

while True:
    entrada = input()
    juncoes, estradas = entrada.split(" ")
    juncoes = int(juncoes) 
    estradas = int(estradas) 
    if(juncoes and estradas > 0):
        grafo = []
        n_out = [[] for i in range(n)]
        economia = fnc(grafo, estradas)
        print(economia)
    else:
        break