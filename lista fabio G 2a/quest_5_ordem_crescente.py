numero_1 = int(input("Digite um numero: "))
numero_2 = int(input("Digite um numero: "))
numero_3 = int(input("Digite um numero: "))
if numero_1 > numero_2 >= numero_3:
    print(f"A ordem crescente é {numero_3} -> {numero_2} -> {numero_1}")
elif numero_1 > numero_3 >= numero_2:
    print(f"A ordem crescente é {numero_2} -> {numero_3} -> {numero_1}")
elif numero_2 > numero_1 >= numero_3:
    print(f"A ordem crescente é {numero_3} -> {numero_1} -> {numero_2}")
elif numero_2 > numero_3 >= numero_1:
    print(f"A ordem crescente é {numero_1} -> {numero_3} -> {numero_2}")
elif numero_3 > numero_1 >= numero_2:
    print(f"A ordem crescente é {numero_2} -> {numero_1} -> {numero_3}")
elif numero_3 > numero_2 >= numero_1:
    print(f"A ordem crescente é {numero_1} -> {numero_2} -> {numero_3}")
else:
    print("Os 3 numeros são iguais")