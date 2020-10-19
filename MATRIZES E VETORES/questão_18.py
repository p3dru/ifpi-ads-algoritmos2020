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
            matriz[linhas][colunas] = int(input(f"Digite o valor da posição [{linhas}][{colunas}]: "))
    return matriz

def soma_positivos(matriz, ordem):
    soma = 0
    for linhas in range(ordem):
        for colunas in range(ordem):
            if matriz[linhas][colunas] > 0:
                soma += matriz[linhas][colunas]
    return soma

def soma_negativos(matriz, ordem):
    soma = 0
    for linhas in range(ordem):
        for colunas in range(ordem):
            if matriz[linhas][colunas] < 0:
                soma += matriz[linhas][colunas]
    return soma

ordem = int(input("Digite a ordem da matriz: "))
matriz = cria_matriz(ordem)
matriz = preenche_matriz(matriz, ordem)
soma_positivos = soma_positivos(matriz, ordem)
soma_negativos = soma_negativos(matriz, ordem)
print(f"A soma dos números positivos é {soma_positivos}")
print(f"A soma dos números negativos é {soma_negativos}")
