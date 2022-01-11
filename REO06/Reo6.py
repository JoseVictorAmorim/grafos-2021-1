class Grafo:

  def __init__(self, num_vertices):
    self.num_vertices = num_vertices
    self.vertices = [[-1 for i in range(num_vertices)] for j in range(num_vertices)]

  def adicionar_vertice(self, a, b, p):
    self.vertices[a][b] = p
    self.vertices[b][a] = p

  def floyd_warshall(self):
    for i in range(self.num_vertices):
      for j in range(self.num_vertices):
        if j == i:
          continue
        for k in range(self.num_vertices):
          if k == j or i == k:
            continue
          if self.vertices[j][i] != -1 and self.vertices[i][k] != -1 and self.vertices[j][i] * self.vertices[i][k] > self.vertices[j][k]:
            self.vertices[j][k] = self.vertices[j][i] * self.vertices[i][k]

while True:
  try:
    n, m = map(int, input().split())
    grafo = Grafo(n)
    for i in range(m):
      a, b, p = map(int, input().split())
      grafo.adicionar_vertice(a - 1, b - 1, p / 100)
    
    grafo.floyd_warshall()
    print("%.6f" % (grafo.vertices[0][n - 1] * 100), "percent")
  except ValueError:
    break
