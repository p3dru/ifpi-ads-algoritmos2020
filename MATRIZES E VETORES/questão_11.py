def cria_matriz(ordem):
    matriz = []
    for voltas in range(ordem):
        linha = []
        for voltas in range(ordem):
            linha.append(0)
        matriz.append(linha)
    return matriz

def preencher_matriz(matriz, ordem):
    for linhas in range(ordem):
        for colunas in range(ordem):
            matriz[linhas][colunas] = int(input(f"Digite o valor [{linhas}][{colunas}]: "))
    return matriz

def mostrar_matriz_formatada(matriz, ordem):
    for linhas in range(ordem):
        for colunas in range(ordem):
            print(f"{matriz[linhas][colunas]:^3}", end=" ")
        print()

def mostrar_matriz_transposta(matriz, ordem):
    for linhas in range(ordem):
        for colunas in range(ordem):
            print(f"{matriz[colunas][linhas]:^3}", end=" ")
        print()


ordem = int(input("Digite a ordem: "))
matriz = cria_matriz(ordem)
matriz = preencher_matriz(matriz, ordem)
mostrar_matriz_formatada(matriz, ordem)
print()
mostrar_matriz_transposta(matriz, ordem)
