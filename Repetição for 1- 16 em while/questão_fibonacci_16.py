termos = int(input("Digite a quantidade de termos que deseja: "))
primeiro = contador = 0
segundo = 1
terceiro = segundo + primeiro
while contador < termos:
    if contador == 0:
        print(f"{primeiro}", end=" ")
        contador += 1
    elif contador == 1:
        print(f"{segundo}", end=" ")
        contador += 1
    else:
        terceiro = segundo + primeiro
        print(terceiro, end=" ")
        primeiro = segundo
        segundo = terceiro
        contador += 1
