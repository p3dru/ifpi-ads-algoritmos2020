valor_limite = int(input("Digite um valor limite: "))
contador = 1
while contador <= valor_limite:
    if contador % 2 == 0:
        print(contador)
        contador += 1
    else:
        contador += 1
