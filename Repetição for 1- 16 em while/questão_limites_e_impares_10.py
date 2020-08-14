limite_inferior = int(input("Digite o limite inferior: "))
limite_superior = int(input("Digite o limite superior: "))
print("Os números ímpares entre {limite_inferior} e {limite_superior} são:")
while limite_inferior < limite_superior:
    if limite_inferior % 2 != 0:
        print(f"{limite_inferior}", end=" ")
    limite_inferior += 1
