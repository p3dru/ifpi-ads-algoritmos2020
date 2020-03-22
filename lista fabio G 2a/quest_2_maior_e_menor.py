numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite outro número: "))
if numero_2 > numero_1:
    print(f"O {numero_2} é maior que o {numero_1}.")
elif numero_1 > numero_2:
    print(f"O {numero_1} é maior que o {numero_2}")
else:
    print("Os números são iguais.")