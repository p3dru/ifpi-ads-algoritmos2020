def cria_matriz(ordem):
    matriz = []
    for elementos in range(ordem):
        linhas = []
        for elementos in range(ordem):
            linhas.append(0)
        matriz.append(linhas)
    return matriz

def preencher_matriz(matriz, ordem):
    contador = 1
    for linhas in range(ordem):
        for colunas in range(ordem):
            if contador < 10:
                print(f"0{contador:^2}", end=" ")
            else:
                print(f"{contador:^3}", end=" ")
            contador += 1
        print()
                
ordem = 5
matriz = cria_matriz(ordem)
matriz = preencher_matriz(matriz, ordem)
