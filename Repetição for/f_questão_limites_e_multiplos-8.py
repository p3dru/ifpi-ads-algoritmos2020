numero = int(input("Digite um número: "))
limite_inferior = int(input("Digite um limite inferior: "))
limite_superior = int(input("Digite um limite superior: "))
print(f"O números que são múltiplos de {numero} são: ")
for numeros in range(limite_inferior, limite_superior + 1):
    if numeros % numero == 0:
        if numeros + numero < limite_superior:
            print(f"{numeros}", end=", ")
        elif limite_superior - numeros < numero:
            print(f"{numeros}" , end="")
        else:
            print(f"{numeros}", end=" e ")
