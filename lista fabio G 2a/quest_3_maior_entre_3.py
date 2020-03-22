numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite outro número: "))
numero_3 = int(input("Digite mais um número: "))
if numero_1 > numero_2 > numero_3 or numero_1 > numero_3 > numero_2:
    print(f"O maior número lido é o {numero_1}.")
elif numero_2 > numero_3 > numero_1 or numero_2 > numero_1 > numero_3:
    print(f"O maior número lido é o {numero_2}.")
elif numero_3 > numero_2 > numero_1 or numero_3 > numero_1 > numero_2:
    print(f"O maior número lido é o {numero_3}.")
else:
    print("Os 3 números são iguais.")
