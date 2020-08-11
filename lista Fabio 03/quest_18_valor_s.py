loop = int(input("Digite um valor: "))
soma = 0
diminuicao = 0
for x in range(loop):
    soma += (x + 1) / (loop - diminuicao)
    diminuicao += 1
print(f"A soma das frações é {soma:.2f}")
