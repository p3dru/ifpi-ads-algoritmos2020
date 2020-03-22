numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite outro número: "))
numero_3 = int(input("Digite mais um número: "))
if numero_3 == numero_2 == numero_1:
    print("Os 3 números são iguais.")
elif numero_1 == numero_2 or numero_1 == numero_3 or numero_2 == numero_3:
    print("Apenas dois numeros são iguais.")
else:
    print("Nenhum número é igual.")
