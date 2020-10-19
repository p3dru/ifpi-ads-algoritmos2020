def cria_matriz(ordem):
    matriz = []
    for linhas in range(ordem):
        linhas = []
        for colunas in range(ordem):
            linhas.append(0)
        matriz.append(linhas)
    return matriz

def preenche_matriz(matriz, ordem):
    for linhas in range(ordem):
        for colunas in range(ordem):
            matriz[linhas][colunas] = int(input(f"Digite o valor para [{linhas}][{colunas}]: "))
    return matriz

def preenche_matriz_com_matriz_existente(matriz_invertida, ordem, matriz):
    for linhas in range(ordem):
        for colunas in range(ordem):
            matriz_invertida[linhas][colunas] = matriz[colunas][linhas]
    return matriz_invertida

def verificar_se_é_simetrica(matriz, matriz_2, ordem):
    total = 0
    for linha in range(ordem):
        for coluna in range(ordem):
            if matriz[linha][coluna] == matriz_2[linha][coluna]:
                total += 1
    if total == ordem ** 2:
        print("A matriz é simétrica")
    else:
        print("A matriz não é simétrica")

ordem = int(input("Digite a ordem da matriz: "))
matriz = cria_matriz(ordem)
matriz = preenche_matriz(matriz, ordem)
matriz_invertida = cria_matriz(ordem)
matriz_invertida = preenche_matriz_com_matriz_existente(matriz_invertida, ordem, matriz)
verificar_se_é_simetrica(matriz, matriz_invertida, ordem)


"""Outra solução seria apenas comparar se a matriz[linha][coluna] == matriz[coluna][linhas] e somar 1 se fosse verdade"""
