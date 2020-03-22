def e_par(x):
    if x % 2 == 0:
        print(f"O número {x} é par")
    else:
        print(f"O número {x} é ímpar")

numero = int(input("Digite um número: "))
e_par(numero)