def par(x):
    if x % 2 == 0:
        print(f"O número {x} é par")
    else:
        print(f"O numero {x} é ìmpar")

valor_1 = int(input("Digite o primeiro valor: "))
valor_2 = int(input("Digite o segundo valor: "))
resto_da_div = valor_1 % valor_2
if resto_da_div == 1:
    soma = valor_2 + valor_1 + resto_da_div
    print(soma)
elif resto_da_div == 2:
    par(valor_1)
    par(valor_2)
elif resto_da_div == 3:
    mult = (valor_2 + valor_1) * valor_1
    print(mult)
elif resto_da_div == 4:
    if valor_2 != 0:
        div = (valor_1 + valor_2) / valor_2
        print(div)
else:
     print(valor_1 ** 2)
     print(valor_2 ** 2)