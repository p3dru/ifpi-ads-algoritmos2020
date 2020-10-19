def cria_matriz(x):
    matriz = []
    for linhas in range(x):
        linhas = []
        for colunas in range(x):
            linhas.append(float(input()))
        matriz.append(linhas)
    return matriz

def soma_específicos(matriz):
    soma = 0
    for linhas in range(12):
        for colunas in range(12):
            if linhas == 0 and 0 < colunas < 11 or\
               linhas == 1 and 1 < colunas < 10 or\
               linhas == 2 and 2 < colunas < 9 or\
               linhas == 3 and 3 < colunas < 8 or\
               linhas == 4 and 4 < colunas < 7:
                soma += matriz[linhas][colunas]
    print(f"{soma:.1f}")

def media_específicos(matriz):
    soma = media = 0
    for linhas in range(12):
        for colunas in range(12):
            if linhas == 0 and 0 < colunas < 11 or\
               linhas == 1 and 1 < colunas < 10 or\
               linhas == 2 and 2 < colunas < 9 or\
               linhas == 3 and 3 < colunas < 8 or\
               linhas == 4 and 4 < colunas < 7:
                soma += matriz[linhas][colunas]
                media += 1
    media = soma / media
    print(f"{media:.1f}")


opcao = input()
matriz = cria_matriz(12)
if opcao == "S":
    soma_específicos(matriz)
if opcao == "M":
    media_específicos(matriz)
