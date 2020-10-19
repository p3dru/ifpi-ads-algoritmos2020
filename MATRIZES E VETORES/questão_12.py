def cria_matriz(ordem):
    matriz = []
    for linhas in range(ordem):
        linha = []
        for colunas in range(ordem):
            linha.append(0)
        matriz.append(linha)
    return matriz

def preencher_matriz(matriz, ordem):
    for linhas in range(ordem):
        for colunas in range(ordem):
            matriz[linhas][colunas] = int(input(f"Digite o valor para [{linhas}][{colunas}]: "))
    return matriz

def mostrar_matriz(matriz, ordem):
    for linhas in range(ordem):
        for colunas in range(ordem):
            print(f"{matriz[linhas][colunas]:^3}", end=" ")
        print()

def soma_diagonal_principal(matriz, ordem):
    total = 0
    for linhas in range(ordem):
        for colunas in range(ordem):
            if colunas == linhas:
                total += matriz[linhas][colunas]
    return total

def soma_diagonal_secundaria(matriz, ordem):
    total = 0
    for linhas in range(ordem):
        for colunas in range(ordem):
            if linhas + colunas == ordem - 1:
                total += matriz[linhas][colunas]
    return total

def soma_dos_elementos_soltos(matriz, ordem):
    total = 0
    for linhas in range(ordem):
        for colunas in range(ordem):
            if linhas != colunas and linhas + colunas != ordem - 1:
                total += matriz[linhas][colunas]
    return total

ordem = int(input("Digite a ordem da matriz: "))
matriz = cria_matriz(ordem)
matriz = preencher_matriz(matriz, ordem)
print()
mostrar_matriz(matriz, ordem)
print()
diagonal_principal = soma_diagonal_principal(matriz, ordem)
diagonal_secundaria = soma_diagonal_secundaria(matriz, ordem)
soma_restante = soma_dos_elementos_soltos(matriz, ordem)
print(f"A soma da diagonal principal é {diagonal_principal}\n"
      f"A soma da diagonal secundaria é {diagonal_secundaria}\n"
      f"A soma dos demais é {soma_restante}")

