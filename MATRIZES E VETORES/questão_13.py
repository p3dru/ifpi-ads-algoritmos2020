def criar_matriz(x):
    matriz = []
    for linhas in range(x + 2):
        linhas = []
        for colunas in range(x):
            if linhas < x:
                linhas.append(int(input("Digite um valor: ")))
            else:
                contador = 0
                linhas.append(linhas[contador])
                contador += 1
        matriz.append(linhas)
    return matriz

def determinante(matriz, x):
    principal = secundaria = 1
    determinante = 0
    if x == 2:
        principal = matriz[0][0] * matriz[1][1]
        secundaria = matriz[1][0] * matriz[1][0]
        determinante = principal - secundaria
    else:
        
        
def mostrar_matriz(matriz, x):
    for linhas in range(x):
        for colunas in range(x):
            print(f"{matriz[linhas][colunas]:^3f}", end=" ")
        print()


ordem = int(input("Digite a ordem da matriz: "))
matriz = criar_matriz(ordem )
"""determinante = determinante(matriz, ordem)"""
print()
mostrar_matriz(matriz, ordem)
print()
print(f"A determinante da matriz é: ")

"""Esboço da 13, cansei dela tbm"""
