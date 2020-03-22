numero = float(input("Digite um número: "))
decimais = numero - int(numero)
int_faltando = 1 - decimais
if decimais >= 0.5:
    print(numero + int_faltando)
else:
    print(numero - decimais)