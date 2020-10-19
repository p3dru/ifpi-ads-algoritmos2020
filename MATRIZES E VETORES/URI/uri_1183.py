def cria_matriz(x):
    matriz = []
    for linhas in range(x):
        linhas = []
        for colunas in range(x):
            linhas.append(float(input()))
        matriz.append(linhas)
    return matriz

def somar_acima(matriz):
    soma = 0
    for linhas in range(12):
        for colunas in range(12):
            if linhas == 0 and 0 < colunas < 13 or\
               linhas == 1 and 1 < colunas < 13 or\
               linhas == 2 and 2 < colunas < 13 or\
               linhas == 3 and 3 < colunas < 13 or\
               linhas == 4 and 4 < colunas < 13 or\
               linhas == 5 and 5 < colunas < 13 or\
               linhas == 6 and 6 < colunas < 13 or\
               linhas == 7 and 7 < colunas < 13 or\
               linhas == 8 and 8 < colunas < 13 or\
               linhas == 9 and 9 < colunas < 13 or\
               linhas == 10 and 10 < colunas < 13 or\
               linhas == 11 and 11 < colunas < 13:
                soma += matriz[linhas][colunas]
    print(soma)

def media_acima(matriz):
    soma = media = 0
    for linhas in range(12):
        for colunas in range(12):
            if linhas == 0 and 0 < colunas < 13 or\
               linhas == 1 and 1 < colunas < 13 or\
               linhas == 2 and 2 < colunas < 13 or\
               linhas == 3 and 3 < colunas < 13 or\
               linhas == 4 and 4 < colunas < 13 or\
               linhas == 5 and 5 < colunas < 13 or\
               linhas == 6 and 6 < colunas < 13 or\
               linhas == 7 and 7 < colunas < 13 or\
               linhas == 8 and 8 < colunas < 13 or\
               linhas == 9 and 9 < colunas < 13 or\
               linhas == 10 and 10 < colunas < 13 or\
               linhas == 11 and 11 < colunas < 13:
                soma += matriz[linhas][colunas]
                media += 1
    media = soma / media
    print(f"{media:.1f}")

opcao = input()
matriz = cria_matriz(12)
if opcao == "S":
    somar_acima(matriz)
if opcao == "M":
    media_acima(matriz)
