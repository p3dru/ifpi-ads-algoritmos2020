def cria_matriz(x):
    matriz = []
    for linhas in range(x):
        linhas = []
        for colunas in range(x):
            linhas.append(0)
        matriz.append(linhas)
    return matriz

def preenche_matriz(matriz, x):
    for linhas in range(x):
        for colunas in range(x):
            matriz[linhas][colunas] = int(input(f"Digite um valor para a posição [{linhas}][{colunas}]: "))
    return matriz

def linha_maior(matriz, x):
    soma = maior = linha = 0
    for linhas in range(x):
        for colunas in range(x):
            soma += matriz[linhas][colunas]
        if linhas == 0:
            maior = soma
            linha = linhas
        else:
            if soma > maior:
                maior = soma
                linha = linhas
    return linha

def linha_menor(matriz, x):
    soma = menor = linha = 0
    for linhas in range(x):
        for colunas in range(x):
            soma += matriz[linhas][colunas]
        if linhas == 0:
            menor = soma
            linha = linhas
        else:
            if soma < menor:
                menor = soma
                linha = linhas
    return linha
    
            
def mostrar_matriz(matriz, x):
    for linhas in range(x):
        for colunas in range(x):
            print(f"{matriz[linhas][colunas]:^3}", end=" ")
        print()

ordem = int(input("Digite a ordem da matriz: "))
print()
matriz = cria_matriz(ordem)
matriz = preenche_matriz(matriz, ordem)
maior = linha_maior(matriz, ordem)
menor = linha_menor(matriz, ordem)
print()
mostrar_matriz(matriz, ordem)
print()
print(f"A maior soma está na linha {maior}")
print(f"A menor soma está na linha {menor}")

"""Professor, tem um erro que eu não consegui resolver, é na parte de printar a linha menor, cansei de perder tempo nela"""
