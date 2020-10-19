def cria_matriz(ordem):
    matriz = []
    for linhas in range(ordem):
        linhas = []
        for colunas in range(ordem):
            linhas.append(0)
        matriz.append(linhas)
    return matriz

def preencher_matriz(matriz, ordem):
    for linhas in range(ordem):
        for colunas in range(ordem):
            if linhas == 0 or linhas == 5 or colunas == 0 or colunas == 5:
                matriz[linhas][colunas] = 1
            elif linhas == 1 and 0 < colunas < 5 or linhas == 4 and 0 < colunas < 5\
            or colunas == 1 and 0 < linhas < 5 or colunas == 4 and 0 < linhas < 5:
                matriz[linhas][colunas] = 2
            else:
                matriz[linhas][colunas] = 3
            
    return matriz

def mostrar_matriz(matriz, ordem):
    for linhas in range(ordem):
        for colunas in range(ordem):
            print(f"{matriz[linhas][colunas]:^2}",end=" ")
        print()
    
ordem = 6
matriz = cria_matriz(ordem)
matriz = preencher_matriz(matriz, ordem)
mostrar_matriz(matriz, ordem)

