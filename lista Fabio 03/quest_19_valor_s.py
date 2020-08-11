loop = int(input("Digite um valor para o loop: "))
soma = 0
diminuicao = 0
for x in range(loop):
    x += 1
    if x % 2 != 0:
        soma += x / (loop - diminuicao)
        diminuicao += 1
    else:
        soma -= (loop - diminuicao) / x
        diminuicao += 1

print(f"A soma das frações é {soma:.2f}")
