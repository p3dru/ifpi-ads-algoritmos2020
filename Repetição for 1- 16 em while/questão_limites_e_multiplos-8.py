numero = int(input("Digite um número: "))
limite_inferior = int(input("Digite um limite inferior: "))
limite_superior = int(input("Digite um limite superior: "))
print(f"O números que são múltiplos de {numero} são: ")
while limite_inferior <= limite_superior:
    if limite_inferior % numero == 0:
        if limite_inferior + numero < limite_superior:
            print(f"{limite_inferior}", end=", ")
            limite_inferior += 1
        elif limite_superior - limite_inferior < numero:
            print(f"{limite_inferior}" , end="")
            limite_inferior += 1
        else:
            print(f"{limite_inferior}", end=" e ")
            limite_inferior += 1
    else:
        limite_inferior += 1
