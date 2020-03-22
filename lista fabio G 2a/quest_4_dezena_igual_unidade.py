numero = int(input("Digite um número de 2 digitos: "))
dezenas = numero // 10
unidades = numero % 10
if dezenas == unidades:
    print("A dezena é igual às unidades.")
else:
    print("A dezena é diferente das unidades.")