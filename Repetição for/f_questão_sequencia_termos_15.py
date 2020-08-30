termos = int(input("Digite o numero de termos: "))
contador = 1
inicio = 1
for numeros in range(inicio, termos + 1):
    print(f"{inicio}", end="... ")
    contador += 1
    inicio += contador
