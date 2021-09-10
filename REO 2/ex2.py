# Davi Carvalho
# Ewerton Keiji Onga
# José Victor

def visita(filaP, visitado, grid):
    u, v = filaP.pop(0)
    for dr in [(-1,0),(+1,0),(0,-1),(0,+1)]:
        uu, vv = u + dr[0], v + dr[1]
        if (0 <= uu and uu < h and 0 <= vv and vv < l and visitado[uu][vv] == 0 and grid[u][v] == grid[uu][vv]):
                visitado[uu][vv] = 1
                filaP.append((uu,vv))
    return filaP


h, l = map(int,input().split())
grid = [[int(x) for x in input().split()] for i in range(h)]
visitado = [[0 for j in range(l)] for i in range(h)]

res = h * l

for i in range(h):
    for j in range(l):
        if visitado[i][j] != 0:
            continue
        fila = [(i,j)]
        visitado[i][j] = 1
        cont = 0
        while fila:
            cont += 1
            fila = visita(fila, visitado, grid)
        res = min(res, cont)

print(res)