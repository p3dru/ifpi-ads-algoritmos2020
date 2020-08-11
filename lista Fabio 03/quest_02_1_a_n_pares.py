def par(n):
    if n % 2 == 0:
        print(n)

numero = int(input("Digite um numero: "))
for i in range(numero + 1):
    par(i + 1)