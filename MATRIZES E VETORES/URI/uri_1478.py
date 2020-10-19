def cria_vetor(x):
    matriz = []
    for linhas in range(x):
        linhas = []
        for colunas in range(x):
            linhas.append(0)
        matriz.append(linhas)
    return matriz

def preencher_vetor(matriz, x):
    diferenca = 1
    for linhas in range(x):
        for colunas in range(x):
            diferenca = linhas - colunas
            if diferenca >= 0:
                diferenca = diferenca + 1
            else:
                diferenca = (diferenca - 1) * -1
            matriz[linhas][colunas] = diferenca
    return matriz

def exibir_matriz(matriz, x):
    for linhas in range(x):
        for colunas in range(x):
            if linhas < x:
                print(f"{matriz[linhas][colunas]:3d}", end=" ")
            else:
                print(f"{matriz[linhas][colunas]:3d}", end="")
        print()
    
tamanho = int(input())
while tamanho != 0:
    matriz = cria_vetor(tamanho)
    matriz = preencher_vetor(matriz, tamanho)
    exibir_matriz(matriz, tamanho)
    print()
    tamanho = int(input())
