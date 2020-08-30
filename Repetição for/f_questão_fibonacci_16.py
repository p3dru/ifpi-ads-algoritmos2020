termos = int(input("Digite a quantidade de termos que deseja: "))
primeiro = 0
segundo = 1
terceiro = segundo + primeiro
for numeros in range(0, termos):
    if numeros == 0:
        print(f"{primeiro}", end=" ")
    elif numeros == 1:
        print(f"{segundo}", end=" ")
    else:
        terceiro = segundo + primeiro
        print(terceiro, end=" ")
        primeiro = segundo
        segundo = terceiro
