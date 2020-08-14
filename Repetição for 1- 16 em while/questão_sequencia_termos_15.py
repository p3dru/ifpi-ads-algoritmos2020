termos = int(input("Digite o numero de termos: "))
contador = 1
inicio = 1
while contador <= termos:
    print(f"{inicio}", end="... ")
    contador += 1
    inicio += contador
