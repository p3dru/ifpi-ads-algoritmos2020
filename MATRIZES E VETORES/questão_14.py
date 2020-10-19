def cria_matriz(ordem):
    matriz = []
    for elemento in range(ordem):
        linha = []
        for elementos in range(ordem):
            linha.append(0)
        matriz.append(linha)
    return matriz

def preenche_matriz(matriz, ordem):
    for linhas in range(ordem):
        for colunas in range(ordem):
            matriz[linhas][colunas] = int(input(f"Digite o valor [{linhas}][{colunas}]: "))
    return matriz

def menor(matriz, ordem):
    menor = matriz[0][0]
    linha = 0
    coluna = 0
    for linhas in range(ordem):
        for colunas in range(ordem):
            if menor > matriz[linhas][colunas]:
                menor = matriz[linhas][colunas]
                linha = linhas
                coluna = colunas
    return menor, linha, coluna

def maior(matriz, ordem):
    maior = matriz[0][0]
    linha = 0
    coluna = 0
    for linhas in range(ordem):
        for colunas in range(ordem):
            if maior < matriz[linhas][colunas]:
                maior = matriz[linhas][colunas]
                linha = linhas
                coluna = colunas
    return maior, linha, coluna
    
ordem = int(input("Digite a ordem da matriz: "))
matriz = cria_matriz(ordem)
matriz = preenche_matriz(matriz, ordem)
menor_da_matriz = menor(matriz, ordem)
print(f"O menor número digitado na matriz é: {menor_da_matriz[0]} na posição[{menor_da_matriz[1]}][{menor_da_matriz[2]}]")
maior_da_matriz = maior(matriz, ordem)
print(f"O maior número digitado na matriz é: {maior_da_matriz[0]} na posição[{maior_da_matriz[1]}][{maior_da_matriz[2]}]")

