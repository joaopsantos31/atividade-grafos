listaVertices = []
listaArestas = []

# Inserir e remover vértices
def inserirVertice(lista):
    vertice = input(f"\nDigite o vértice: ")

    if vertice not in lista:
        lista.append(vertice)
    else:
        print(f"\nO vértice já está no grafo.")

# Inserir e remover arestas

def inserirAresta(lista):
    verticeOrigem = input("\nDigite o vértice de origem: ")
    verticeDestino = input("\nDigite o vértice de destino: ")

    if verticeOrigem not in listaVertices:
        print(f"O vértice de origem {verticeOrigem} não está no grafo.")
    elif verticeDestino not in listaVertices:
        print(f"O vértice de destino {verticeDestino} não está no grafo.")
    else:
        lista.append([verticeOrigem, verticeDestino])

def removerAresta(lista):
    verticeOrigem = input(f"\nDigite o vértice de origem: ")
    verticeDestino = input(f"\nDigite o vértice de destino: ")

    for i in range(len(lista)):
        if lista[i][0] == verticeOrigem:
            if lista[i][1] == verticeDestino:
                lista.pop(i)
                print(f"\nA aresta foi removida")
                break
        print(f"\nA aresta não existe")

# Calcular grau de cada vértice

def calcularGrau(lista, vertice):
    contadorVertice = 0

    if vertice in listaVertices:
        for i in range(len(lista)):
            if lista[i][0] == vertice:
                contadorVertice += 1
            if lista[i][1] == vertice:
                contadorVertice += 1

        print(f"O grau do vértice {vertice} é: {contadorVertice}")

# Verificar se existe uma aresta que vai de um vértice para o outro

def verificarAresta(lista):
    verticeOrigem = input(f"\nDigite o vértice de origem: ")
    verticeDestino = input(f"\nDigite o vértice de destino: ")

    for i in range(len(lista)):
        if lista[i][0] == verticeOrigem:
            if lista[i][1] == verticeDestino:
                print(f"\nA aresta existe")
                break
        print(f"\nA aresta não existe")

# Verificar os vizinhos de um vértice

def verificarVizinhos(lista):
    vertice = input(f"\nDigite o vértice: ")
    vizinhos = []

    for i in range(len(lista)):
        if lista[i][0] == vertice:
            vizinhos.append(lista[i][1])

    print(f"\nOs vizinhos do vértice {vertice} são: {vizinhos}")


# Verificar se existe um percurso entre dois vértices

def verificarPercurso(lista):
    verticeOrigem = input(f"\nDigite o vértice de origem: ")
    verticeDestino = input(f"\nDigite o vértice de destino: ")

    visitados = [verticeOrigem]
    fila = [verticeOrigem]

    while len(fila) > 0:
        atual = fila.pop(0)

        for i in range(len(lista)):
            if lista[i][0] == atual and lista[i][1] not in visitados:
                visitados.append(lista[i][1])
                fila.append(lista[i][1])

    if verticeDestino in visitados:
        print(f"\nExiste um percurso de {verticeOrigem} até {verticeDestino}")
    else:
        print(f"\nNão existe percurso de {verticeOrigem} até {verticeDestino}")
