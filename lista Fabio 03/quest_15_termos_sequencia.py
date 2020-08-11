quantidade_voltas = int(input("Digite a quantidade de termos: "))
inicio = 1
incremento = 1
for x in range(quantidade_voltas):
    print(inicio, end=", ")
    incremento += 1
    inicio += incremento
print("...")
print()
