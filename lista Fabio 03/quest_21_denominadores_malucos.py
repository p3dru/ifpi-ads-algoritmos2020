numerador = 1
denominador = 1
soma = 0
for x in range(50):
    x += 1
    soma += numerador / denominador
    numerador += 2
    denominador += 1
print(f"A soma entre as frações de 1/1 à 99/50 é {soma:.2f}")
