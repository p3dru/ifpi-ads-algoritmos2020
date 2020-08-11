limite_inferior = int(input("Digite um início: "))
limite_superior = int(input("Digite um fim: "))
for x in range(limite_inferior, limite_superior + 1):
    if x % 2 != 0:
        if x < limite_superior - 1:
            print(x, end=" -> ")
        else:
            print(x)
