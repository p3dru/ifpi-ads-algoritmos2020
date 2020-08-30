limite_inferior = int(input("Digite o limite inferior: "))
limite_superior = int(input("Digite o limite superior: "))
print(f"Os números ímpares entre {limite_inferior} e {limite_superior} são:")
for numero in range(limite_inferior, limite_superior + 1):
    if numero % 2 != 0:
        print(f"{numero}", end=" ")
