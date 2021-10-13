import networkx as nx

def fnc(grafo, est):
    sGrafo = 0
    for i in range(0,est):
        entrada = input("")
        x, y, z = entrada.split()
        x = int(x)
        y = int(y)
        z = int(z)
        
        grafo.add_edge(int(x), int(y), weight=int(z))
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
        grafo = nx.Graph()
        economia = fnc(grafo, estradas)
        print(economia)
    else:
        break