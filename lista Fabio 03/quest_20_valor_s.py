loop = int(input("Digite o valor de loops: "))
soma = 0
numerador = 1
for x in range(loop):
    x += 1
    if x % 2 != 0:
        soma += numerador / x
    else:
        soma -= numerador / x
print(f"A soma das frações é {soma:.2f}")
