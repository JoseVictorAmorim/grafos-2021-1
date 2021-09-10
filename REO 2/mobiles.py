# Davi Carvalho
# Ewerton Keiji Onga
# José Victor

def dfs(grafo, vertice_fonte):
  visitado = []
  pilha = [vertice_fonte]

  while pilha:
    atual = pilha.pop()
    visitado.append(atual)

    if atual in grafo:
      for filho in grafo[atual]:
        if not filho in visitado:
          pilha.append(filho)

  return len(visitado) - 1

while True:
  try:
    # pq definida como um "dicionário"
    # Ex: {0: [1], 1: [2], 2: [4, 3, 5]}
    # o mobile será basicamente uma árvore, aonde os elementos que não estão na minha pq
    # são elementos folha da arvore

    # Nesse exemplo:
    #      0
    #      |
    #      1
    #      |
    #      2
    #   /  |  \
    #   4  3  5

    priority_queue = {}

    num_pecas = int(input())

    # Já inicio a saida de uma forma, que se o programa rodar sem um break a saida vai ser bem
    saida = "bem"

    # Preenchendo pq
    for i in range(num_pecas):
      peca_filho, peca_pai = map(int, input().split(" "))
      if not peca_pai in priority_queue:
        priority_queue[peca_pai] = []
      priority_queue[peca_pai].append(peca_filho)

    # para cada filho de cada pai eu preciso ver quantas casas eu visito no bfs
    # ou seja, quantos filhos esse filho tem
    # considerando o mesmo exemplo:
    # 0 = [4]
    # 1 = [3]
    # 2 = [0, 0, 0]
    # Quando é um array de tamanho único, significa que ele só tem um caminho possível (1 aresta)
    # Quando é um array de tamanha diferente significa que ele tem mais de um filho
    for pai in priority_queue:
      # esse if que diminui total o tempo de processamento, eu só verifico
      # pais com mais de um filho, naquele exemplo seria só o 2, pois se só tem 1 filho
      # ele é automaticamente balanceado
      if len(priority_queue[pai]) > 1:
        num_filhos = []
        for filho in priority_queue[pai]:
          num_filhos.append(dfs(grafo=priority_queue, vertice_fonte=filho))
        if not all(num == num_filhos[0] for num in num_filhos):
          # Esse if fiz de uma maneira mais "pythonica"
          # pra cada item do array ele tá comparando com o primeiro pra ver e criando um outro array com essa comparação
          # nesse caso: [0, 0, 0] = [True, True, True]
          # nesse caso: [0, 2, 0] = [True, False, True]
          # Se todos items forem true é balanceado
          # como coloquei um "not" ele vai mandar a saida = "mal" e sair do loop quando um item for False
          saida = "mal"
          break
    
    print(saida)
  except (EOFError, ValueError) as error:
    break