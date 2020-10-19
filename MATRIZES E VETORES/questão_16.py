def cria_matriz(ordem):
    matriz = []
    for linha in range(ordem):
        linha = []
        for coluna in range(ordem):
            linha.append(0)
        matriz.append(linha)
    return matriz

def preenche_matriz_identidade(matriz, ordem):
    for linhas in range(ordem):
        for colunas in range(ordem):
            if colunas == linhas:
                matriz[linhas][colunas] = 1
    return matriz

def mostrar_matriz(matriz, ordem):
    for linha in range(ordem):
        for coluna in range(ordem):
            print(f"{matriz[linha][coluna]:^3}", end=" ")
        print()

ordem = int(input("Digite a ordem da matriz: "))
matriz = cria_matriz(ordem)
matriz = preenche_matriz_identidade(matriz, ordem)
mostrar_matriz(matriz, ordem)
