numero = int(input("Digite um número: "))
if numero == 2 or numero == 3 or numero == 5 or numero == 7:
    print(f"O numero {numero} é primo")
else:
    if numero % 2 == 0 or numero % 3 == 0 or numero % 5 == 0 or numero % 7 == 0:
        print(f"O numero {numero} não é primo")
    else:
        print(f"O numero {numero} é primo")