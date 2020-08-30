limite_inferior = int(input("Digite um inicio: "))
limite_superior = int(input("Digite um fim: "))
print(f"Os números pares entre {limite_inferior} e {limite_superior} são: ")
for numero in range(limite_inferior, limite_superior + 1):
    if numero % 2 == 0:
        print(f"{numero}... ", end="")
