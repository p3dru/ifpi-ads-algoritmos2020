def cria_matriz(ordem):
    matriz = []
    for linhas in range(ordem):
        linhas = []
        for colunas in range(ordem):
            linhas.append(float(input()))
        matriz.append(linhas)
    return matriz

def exibir_matriz(matriz, ordem):
    for linhas in range(ordem):
        for colunas in range(ordem):
            print(f"{matriz[linhas][colunas]:^4}", end=" ")
        print()

def somar_específicos(matriz, ordem):
    soma = 0
    for linhas in range(ordem):
        for colunas in range(ordem):
            if colunas == 0 and 0 < linhas < 11 or \
               colunas == 1 and 1 < linhas < 10 or\
               colunas == 2 and 2 < linhas < 9 or\
               colunas == 3 and 3 < linhas < 8 or\
               colunas == 4 and 4 < linhas < 7:
                soma += matriz[linhas][colunas]
    print(soma)

def media_específicos(matriz, ordem):
    media = soma = 0
    for linhas in range(ordem):
        for colunas in range(ordem):
            if colunas == 0 and 0 < linhas < 11 or \
               colunas == 1 and 1 < linhas < 10 or\
               colunas == 2 and 2 < linhas < 9 or\
               colunas == 3 and 3 < linhas < 8 or\
               colunas == 4 and 4 < linhas < 7:
                soma += matriz[linhas][colunas]
                media += 1
    media = soma / media
    print(f"{media:.1f}")
                

ordem = 12
opcao = input()
matriz = cria_matriz(ordem)
if opcao == "S":
    somar_específicos(matriz, ordem)
if opcao == "M":
    media_específicos(matriz, ordem)
