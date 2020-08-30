valor_limite = int(input("Digite um valor limite: "))
contador = 1
for numero in range(1, valor_limite + 1):
    if numero % 2 == 0:
        print(numero)
